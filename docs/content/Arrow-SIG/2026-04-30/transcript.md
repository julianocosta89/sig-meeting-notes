SIG: Arrow SIG
Date: 2026-04-30
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 00:58 Hey guys.
**Jake Dern** 01:05 Bake.
**Laurent Querel** 01:17 There it is.
**Jake Dern** 01:20 Hello.
**Aaron Marten** 01:21 Right.
**Laurent Querel** 03:39 Okay, so we are a little bit slow this morning, didn't sleep enough.
So, so, so… is… Joshua with us.
**drewrelmas** 03:55 I have not seen your hotline this morning yet.
**Laurent Querel** 03:58 Okay.
So I encourage everyone to… filling the, The Google Doc, this one. I see already a lot of people there, that's cool.
Then we, we will start with the triage, as usual.
And, and then, please add some topics in the agenda.
I know that we already have one organic benchmark with Jake, But if you have some isotopic, you're welcome.
**jmacdonald** 04:36 Good morning.
**Laurent Querel** 04:38 Oh, Josh.
**jmacdonald** 04:40 True.
**Laurent Querel** 04:41 Great.
I was just saying that, We will start with the triage, as usual, and then start with some topic.
And oncology one to… To add something there.
So, let's start with the issues.
And, last time, accepted this idea, yeah.
Still deciding, so it looks like we have to go back a bit more.
Yeah, quite be you.
**jmacdonald** 05:22 I feel like we didn't update the notes, but I was trying to keep the issue number that we fixed, finished finished.
**Laurent Querel** 05:29 So, okay.
**jmacdonald** 05:30 We went through 2725 last time.
I don't think I…
**Laurent Querel** 05:35 Mercury.
**jmacdonald** 05:36 Triage accepted, though.
**Laurent Querel** 05:38 20… 20 watts, sorry.
**jmacdonald** 05:40 2725 is what the notes say.
**Laurent Querel** 05:45 Okay.
Okay.
Included?
**jmacdonald** 05:54 I think that inclusive.
**Laurent Querel** 05:58 Okay.
**jmacdonald** 05:59 Yeah, I… the OTLP protobuf message size limit is one that, we talked about for sure last time, and that was the last.
**Laurent Querel** 06:07 Thank you.
So I remember this one, proposal from, Jake.
To… to improve the… the effect on blur, and and basically, mimic the same interface that, Tokyo MPMC MPSC, is, is providing in terms of, You reserve… you basically say to the channel that you'd like to send one message.
And you enter into the body of the EF, or the body of the… I think it's the… Yes.
In that case, it's a select, but anyway, you basically reserve… you specify that you have to get a permit to send a message, and then This send message will be, invaluable.
And that will, solve some issues that we have today.
Personally, like, the proposal.
Don't think it's, A problem, Any, feedback on that?
**jmacdonald** 07:31 So the idea is an asynchronous, reservation.
**Laurent Querel** 07:35 Yes.
**jmacdonald** 07:38 It's amazing.
**Laurent Querel** 07:38 the same interface that exists already on TokyQ MPSC.
**jmacdonald** 07:43 That's good information.
**Laurent Querel** 07:49 Okay, jake, you want to add something on that?
**Jake Dern** 07:54 Oh, I was just gonna say, yeah, the benefit is really just that you get a future that resolves only when, you're ready to actually send. So, that's the thing that basically we're missing, and yeah, whether the interface looks exactly like that or not, that's, like, the thing that I'm after. Yeah.
**Laurent Querel** 08:13 Yeah, I think it's a nice addition.
Okay, I think we will do a massive update, instead of an individual update for the… the tag.
So, I was, sorry.
Yeah, yeah, benchmark consistently, show a negative alerts, so that's also you, Jake. Maybe a few words on this one?
**Jake Dern** 08:38 Yeah, it's really just an issue with, like, how we're pulling the metrics, and the fact that the metrics become unavailable as soon as we shut down. So, we always shut down the load generator first, so as soon as we, like, send that signal, the metrics are deregistered for the pipeline.
So we always miss, like, the, like, most recent few data points that the receiver has exported, so…
**Laurent Querel** 08:59 Dude.
**Jake Dern** 09:00 We'll consistently get, like, a negative result, yeah.
**Laurent Querel** 09:03 I don't know why, but I was thinking that I already fixed this issue, looks like it's not the case.
**Jake Dern** 09:09 Yeah, you… thing in there that, like, makes sure we gather the, the last, like, metric when we send the shutdown, in the admin server, but I think, like, the metric is still deregistered, like, from the registry, so you can't scrape it. Like, I think we…
**Laurent Querel** 09:22 Hmm.
**Jake Dern** 09:22 Like, we make sure we collect it, but then, like, the registry, like, says, oh, these metrics don't exist anymore, like, immediately, still.
**Laurent Querel** 09:29 Okay, I see. Excellent. Okay, yeah, not a big… I think it's something easy to fix.
**Jake Dern** 09:36 Yeah, we could delay, or having a way to push the metrics would fix, too.
**Laurent Querel** 09:40 Metric, description, conflict, duplicate, pending, same… Oh, I think this one is… Close, right? Do we have a… Congress?
**jmacdonald** 09:51 I have, well, Andres is on the call, and I think, there was some discussion with CJO about the sort of open telemetry data model here.
Yeah.
I agree.
**Laurent Querel** 10:02 And I think, if I remember well, the conclusion was… that's, it's, it's not, I mean, it's… authorize a load in, in…
**jmacdonald** 10:15 Yeah, so my understanding is that we… OpenTelemetry allows the same metric to be defined in multiple scopes. Intention there is that it means the same thing, that you have different instrumentation scopes producing the same instrument… same semantic, essentially.
In this case, I believe we just, introduced a feature which has already merged, I think, to put view capability so that we can select which one we want. I don't think this is a bug, per se.
**Laurent Querel** 10:47 Okay.
**Andres Borja** 10:48 Oh, so… Well, I think we are expecting that in the code, you know, we are using the, you know, cannot… the name of space is not called naming space, it's the… Let's go.
**jmacdonald** 11:01 Nope.
**Andres Borja** 11:02 Anyway, it should be working, technically, but we are seeing some, log messages in, you know, in our logs.
Where it's… it looks like some of the metrics suck from time to time, there's just… Kind of, like, override each other, and they don't respect that namespace.
So, something is odd. I was not able to reproduce it, like, locally, but it looks like CGO added some other instructions of how to reproduce it.
I hope it's not, like, a race condition or anything like that, but, yeah, it looks awesome.
**jmacdonald** 11:41 I see. This is a bug. Okay. Thank you, Andres. Let's just leave this file.
**Laurent Querel** 11:47 And someone will welcome that, right?
**jmacdonald** 11:49 Yeah.
**Laurent Querel** 11:50 Okay.
**jmacdonald** 11:52 Thank you, Andres.
**Laurent Querel** 11:54 Thank you. Supported CTL transform statement in the transform processor, so, yes… That's a definitive real goal, let's see, is there any…
**drewrelmas** 12:10 I'm not sure we have Mark on the call. Mark, if you're here, please speak up, but Mark is a Microsoft contributor who is interested in starting to work in the repo. He's sent out a few PRs already.
I think the intention here, and there's been other discussion on other issues about… how we organize the various transform languages we support in the repo, but I think we're all aligned in general on this, in that we're working on this columnar query engine, and we have our AST, And we want to do the parser for OTTL so people familiar with OTTL can take advantage of the same transform engine.
**Laurent Querel** 12:58 Yeah, yeah, perfect. Yeah, we… just to summarize for people that, in terms of language, we have OTTL, which is the… the language used inside OpenTelemetry that already… that is already supported in the Go Collector.
which is, like, a YAML-based, Language… But tailored for open telemetry signal.
We have OPL, which is a new language with, A pipe-oriented interface.
Stream-oriented language.
With the same, philosophy.
So, meaning that it's, it's optimized, and I'm focusing only on open telemetry, so… what that means is, with OTTL or OPL, The system only understands open telemetry signal, and can only generate open telemetry signal.
And then we have a third language named KQL, derived from… I mean… which is a language implemented by Microsoft outside of OpenTelemetry.
Which is a little bit more general.
Does not provide the same kind of guarantee, but also have some additional, interests, and one of them is probably the fact that, it's already used by, multiple, many, Microsoft users.
So they have… they share a lot… right now, they share the same EST, but they don't necessarily share the same query engine.
So the question will be, and I think we answered that recently, but OTTL and OPL will share the same gene?
the same EST.
And, on the engine side.
Albert is basically adding some new capability to the query engine to cover the most important OTTL, Let's say, transform capability, or filtering capabilities.
That were not already covered.
**drewrelmas** 15:19 Yeah, my only ask would be, Albert, if you coordinate with Mark, because I know he was interested in not just doing the OTTL parser, but also potentially taking some small expression implementation in the engine, so we just want to avoid, duplicating work there.
**Laurent Querel** 15:36 Perfect, that's the good news.
**Albert Lockett** 15:38 Yeah, of course, yeah, I can coordinate with Mark. I don't see him on the call, but I'll reach out on Slack.
**Laurent Querel** 15:48 Okay, excellent. Shortened Ubuntu ARM build time. So, Josh?
**jmacdonald** 15:55 Yeah, this one's me. We still… we have this issue, like, the build is always red, and it sometimes is CodeCov, but sometimes… but, like, the window… the ARM build is very slow, and basically times out every time. And the Windows build is also suspicious of… with all the flaky tests, which I think is mostly a build time issue.
As well, or some sort of provisioning problem. So both of those, builds are causing us to, like.
slow down our build queue, our merge queue, and so on. My proposal was for, at least for the ARM build, we, set the features, so we're not building all features on ARM, just, like, it's not helpful to us, because it's timing out every time.
**Laurent Querel** 16:38 Okay.
In order to keep the triage section of this meeting not too long, is there a last issue you'd like to discuss before we switch to the demo or topics?
**jmacdonald** 16:58 Let me just click through. Everyone should do this, but let me look through real quick.
**Laurent Querel** 17:02 Wicked.
**jmacdonald** 17:18 Yeah, I think we… I mean, one thing we… my… No, nothing looks urgent. I was gonna ask about Aaron's issue with Global Tracing Subscriber, but we could take that offline, I can talk to him about it.
**Laurent Querel** 17:32 Okay.
Okay, okay, for… The rest of the folks in the… In, in this, SIG meeting, is there any, thing that you'd like to discuss before we switch to demo and, Engineer topic.
Thank you. Bye.
**Utkarsh Umesan Pillai** 17:53 I had one thing, sorry, Ron.
**Laurent Querel** 17:55 Yep.
**Utkarsh Umesan Pillai** 17:55 I had… I've created an issue for adding Windows EDW receiver as a contract.
Yeah, I just wanted to, also mention that someone from Microsoft has, like, agreed to work on it, and, like, will be willing to work on it, and he's also joined the call, for the first time, so…
**Laurent Querel** 18:14 Okay.
**Utkarsh Umesan Pillai** 18:15 Yeah, so, Swapnell, if you want, like, just give a small intro.
**Swapnil Ashtekar** 18:22 Yeah, sure. Thanks, thanks, Utt.
Hi everyone, this is, Swap Milaf.
I'm Senior Software Engineer at Microsoft, and I will be contributing on this ETW receiver, for OTEL.
**Laurent Querel** 18:38 Nice.
So it's… if I understand well, it's relatively close. That's the equivalent of the user event, the Linux user event, but for Windows, right?
**Utkarsh Umesan Pillai** 18:49 Yes.
**Swapnil Ashtekar** 18:50 Yes.
**Laurent Querel** 18:51 Okay.
That's great.
I mean, it's, adding the… Fast receiver, formative integration is definitely,
**jmacdonald** 19:02 Can we say a little bit about, I saw, I saw in the issue, OneCollect is named, and I've been doing some work up at the top. Session Management Library will be OneCollect, and this is a library that we could be using, or probably will be using, for profiles once we get to profiles in OTAP, like this, so I've been working on a little bit of roadmap work, and it covers OneCollect.
coming to us, and so I'm excited to see this.
I was wondering if we could talk a little bit about what that means.
**Utkarsh Umesan Pillai** 19:30 Sure, Yeah, so for consuming ETW events, like, the very first thing you have to do is create a session where you tell which providers to subscribe to, at what keywords and levels, and… and then you have to decode events, so that will give you… let's say, let me just give you, like, a binary payload, but you should know how to decode them into What the event data actually was.
So… OneCollect has, along with those, the profiling features, it also has this… it also offers a session management feature where you can tell which ETW providers or producers you're interested in, and it will do the session management of, like, subscribing to them, registering interests, and all of those things for you.
And, yeah, go ahead.
**jmacdonald** 20:18 Maybe at a high level, I think this is something that not many people know, and a lot of us are Microsoft employees here, but just to make clear for the group, like, this is a… diagnostic interface that lets you, essentially share your schema out of band with the actual data. So you're sending a very compact data record, ideally at high throughput through this ETW channel, and the subscription that you're talking about, the session state that you're talking about, is getting that schema information and anything else that you need to resolve, actually, first symbols and so on. It gets quite a bit more complicated once you're asking to symbolize or take profiles and so on from those.
and unwind stacks, but that's also in scope of what OneCollect does.
**Utkarsh Umesan Pillai** 21:02 Yeah.
**Laurent Querel** 21:03 question regarding this library. I was aware of it because I think Joshua and a few of you already mentioned it.
But I didn't look, in the detail of it.
I'm just wondering how well aligned this OneCollect library is with the thread per core approach that we have.
And the fact that we are using a local, a local long time, for Tokyo.
**Utkarsh Umesan Pillai** 21:34 Yeah, so… For Linux, at least for the user events part, I think the PR that Lalith has out already, he is… I'm not sure if he's using OneCollect for session management, because I think he's using, per core… every core's FT, and, like.
Our worker thread, which is pinned to one core, will only listen to subscribe to the.
**Laurent Querel** 21:57 Huh.
**Utkarsh Umesan Pillai** 21:57 FD for that code, but for Windows, we have a limitation from the Windows kernel side itself.
So we are forced to listen to just one merged event stream. The kernel merges events from across all the cores.
And, the… you have to provide a callback, that's all you can configure, and… So this merging happens… Regard… I mean, we cannot get around it.
So…
**Laurent Querel** 22:24 Okay.
**Utkarsh Umesan Pillai** 22:25 what I'm suggesting in this, like, issue here is that we… just try to minimize the cross-core, cache bouncing, as much as we can. So what we do is, like.
the merged events.
We have a thread where we listen to the merged event stream from the kernel, and then we hand off work to all these, pinned worker threads.
That…
**Laurent Querel** 22:53 Okay.
**Utkarsh Umesan Pillai** 22:54 Yeah, that's kind of similar to, I think we had another issue on, SREU support not being supported on Windows the way we want.
So, something similar here again, like, when you don't have kernels.
Support for distributing events, then you have to, like, Basically, do something at a user space level itself.
You can just minimize stuff until… Gotcha.
**Laurent Querel** 23:21 Okay, sounds good.
**Utkarsh Umesan Pillai** 23:22 Yep, yep.
**Laurent Querel** 23:23 Yeah, that looks very similar on the… The general approach.
Like, the topic mechanism that we have.
**Utkarsh Umesan Pillai** 23:35 Yes.
**Laurent Querel** 23:36 It's like, we have a topic where This topic will be filled with… Etw Windows event.
And we will be able to consume it from regular receivers. I'm just creating a… a parallel with, with another construct that we have, but I think that will be more or less the same
**Utkarsh Umesan Pillai** 24:01 Yeah, understood.
**Laurent Querel** 24:02 The same problem and the same benefit.
**Utkarsh Umesan Pillai** 24:06 So, I did look at the topic approach as well, and I think there's a… like, it forces the contract as OTAP, so when I looked at incorporating topics here, what I found was the… callback thread, which has… which gets the merged events, it would have to also batch, and, like, prepare OTAP batches to hand out to the other pinned threads, which… basically, I thought it was, like, it was increasing work for the… for the callback there. Like, that's the…
**Laurent Querel** 24:38 Huh.
**Utkarsh Umesan Pillai** 24:39 That's anyway the serialization point, or, like, the contention point, so we want to do as less work there as possible.
Yeah. So, that's… That's why I didn't, I think we can make it work with topic, but then topic receiver should allow… Same day.
**Laurent Querel** 24:57 I was, I was just, creating a parallel, not necessarily suggesting to… to reuse topic. That was more my point. Okay, so good.
**Utkarsh Umesan Pillai** 25:08 Yeah, yeah. And, Josh, another thing, like, with, so Swapnil and I would also be working with the OneCollect folks, and try to add the decoding of ETW events logic in their, crate, because they don't have that as of today. They only have decoding logic for Linux.
**jmacdonald** 25:25 Great. Yeah, I was just looking at OneCollect yesterday, I have some other reasons to be talking about this, so we'll follow up together on that. Thank you so much.
**Utkarsh Umesan Pillai** 25:32 Okay.
**Laurent Querel** 25:36 Okay, so I think, except if you have a last topic to discuss, part of the triage, I suggest to move here.
So I see, two topic, processor chain, a stopwatch timer.
And, the benchmark… So we have 30 minutes.
We… I think we can split that in two.
And depending on the remaining time, I could have another topic to discuss, but let's talk about those two first.
Drew?
Do you want to, yeah, I know.
**drewrelmas** 26:18 I know processor chain was briefly discussed last week. Unfortunately, I was out of office and unable to attend, but in watching the summary and having follow-up conversation with Ukarsh and Josh.
I think while processor chain is important on its own merits for the channel reduction and memory consumption impact, that really, I was… we were kind of rushing it to achieve this much more minimal goal of simply having a… cumulative, or a, composite process duration. So… I… I know we had… I had initially discounted this because I was super excited about the memory reduction and actually implementing processor chain, but, I've gone back to the drawing board, and I think have a pretty workable solution for the context-propagated stopwatch, which we had kind of thrown a lot around a little, and this PR is my attempt at that.
So I don't have too much to say. I feel like the PR is in a pretty good state. It is limited only to local Processors, not shared processors.
And it also requires, you know, timed adoption, which is, you know, I actually made a sub-issue, when I found that some of our processors, including transform processor, don't actually use timed, so they don't produce a duration metric, so that's a follow-up that I want to… But the benefit of that, like, the main thing I want to say is the… processor chain design I was pursuing placed, like, some structural… it was related to structural limitations on what each processor does. So, like.
you know, we talked about, can it do async work? Does it need a separate, like, process? Does each processor need a separate process in line function that does a duple… essentially duplicating code, but only doing safe operations?
This approach… works for all processors. It's simply a function of tagging some stopwatch metadata on PData as it goes through the pipeline. And the engine knows, based on the config YAML, what processor to, like, reset or start timing, and then what processor to stop and report on. So, this is much more generic, and it isn't tied to The actual implementation details of what each processor does.
**Laurent Querel** 29:15 Okay, I have two questions.
Yes. So, first, I'm not sure to understand why timed is… So…
**drewrelmas** 29:29 So timed… timed today is where processors who call timed, accumulate, into… it's like compute.processor… or processor.compute.successorfailed.duration, right? So I'm essentially hooking into that same… points.
In the flow to accumulate the.
**Laurent Querel** 29:58 But will not that be possible to derive, I mean, to let the engine Do the work, because process or expose a method process.
with a result. So the… the… The outcome of the process is already known by the engine.
**drewrelmas** 30:19 I see, and so…
**Laurent Querel** 30:20 And so, you mentioned that you have a configuration where you specify the beginning and the end.
Of the show.
Just wondering why we need to ask every Processor author to do that.
**drewrelmas** 30:36 Yup, that's a… that's a fair question.
And this is actually semi-related to another issue I had opened, where I had noticed that For some processors who do use timed, they're still doing work outside of the timed boundary, so that work isn't actually being captured.
**Laurent Querel** 30:58 and…
**drewrelmas** 30:59 duration metrics. So, I think what you're asking is.
Can we just, at the engine level, make sure that all calls to the process function are timed, and… Maybe we don't even need the times.
To be invoked by a processor author.
**Laurent Querel** 31:17 Yeah, that's… Something to explore, in my opinion, to make this thing more general.
The second one, is more problematic, I think, right now.
But I'm just wondering where it's only local processor. Right now, I think we don't have.
**drewrelmas** 31:34 We don't have shared processor, yeah, so I was just curious.
**Laurent Querel** 31:37 It's not a big deal, but the question is why we have this limit.
**drewrelmas** 31:46 I don't think I have a proper answer besides I was just trying to limit,
**Laurent Querel** 31:54 Okay.
**drewrelmas** 31:54 consideration, so I can definitely think about that.
**Laurent Querel** 31:57 Yeah, I think once this one is explored, and maybe… We conclude that that could be done, at the engine level and not inside the processor.
then this one will, I think, be served too.
Because for the engine, once we have this wrapper around the local processor and shared processor, they are behaving the same.
So, I will not be surprised, once we have that explored, that will be… will go away definitively.
**drewrelmas** 32:33 Okay, I can, yeah, I'll definitely…
**Laurent Querel** 32:34 That, that looks… so I will, I will let that open, and I will… I know that I am super, super late on, review in general, this one, the extension, sorry for that, guys.
had some internal stuff to do recently, but, I will, Spend the rest of the week, today and tomorrow to… Produce the gap.
**drewrelmas** 33:03 Was there any other commentary on that before we switch away? Josh, I thought I heard you say something.
**jmacdonald** 33:07 Oh, yeah, I was… two things. I think the stopwatch work is okay. I assigned Copilot for review, because there were a few nits I could see, but it looks like they've been handled. And then for Gokan, I know a lot of people are waiting for the work on extensions, I just don't… I don't want to make more pressure for it, so thank you, Laurent.
**Laurent Querel** 33:25 Okay. But, so, talking about review and things like that, I think we… we need… during the review, I will classify, at least in two categories, the type of PR that we have.
One is, oh, we have a new capability, a new processor, a new receiver.
Does not really have an impact on the rest, Or we have, a fix An improvement in terms of performance.
And there is another category, which is, the interface… Of the engine itself, or the overall behavior.
I think, for me, this one entered into this category.
And that's where I'll… Because we have more and more contributors, and because we… We are closer and closer to something that is more stable.
That's definitely where we need to be very careful and make sure that we We all agree on the interface, and that's why I will not be… I mean, for me, if we have to spend a little bit more time on this one, which is fundamental.
My message is I prefer to keep this one in the… In the… Here are two reviews, and making sure that we all agree on how it's, designed.
Makes sense.
**drewrelmas** 35:11 Yeah.
**jmacdonald** 35:11 Yes, thank you. We will be more careful, of course, with PRs that affect the whole codebase.
**Laurent Querel** 35:19 I'm not saying that you are not careful, I'm just, saying that, just using this opportunity to mention that, for reviewer, the… in my opinion, we have to keep that in mind, and I'm not saying that this one is… is going wrong. Just saying that it's important to be all aligned on this type of PR.
Okay, Drew, you want to add something else?
**drewrelmas** 35:52 No, that was… that was it. You've given some good feedback, and I'm gonna go take a look.
**Laurent Querel** 35:59 Okay, great. Jake?
**Jake Dern** 36:02 Yeah, you mind if I, take over the screen share, actually? I wanna… there's a couple things I wanna take a look at.
**Laurent Querel** 36:08 Yeah, good.
**Jake Dern** 36:11 Awesome.
Alright, can people see my screen? Does it look okay?
**Laurent Querel** 36:19 this…
**Jake Dern** 36:20 Okay, yeah, so I think people probably noticed, last week, so I originally filed this issue after we implemented, or after I implemented, the smooth mode for the fake data, receiver, and so… For folks that don't know what this does is it, rather than sending all of the data for the per second rate as fast as it can at the start of the second.
It instead tries to space it out over the course of the entire second.
And so this had some results that I was not expecting, namely that a lot of our benchmarks are showing, like, massively increased CPU utilization. And this ended up being… it kind of sent me down a rabbit hole that I think is interesting for, like, a few reasons, but… Initially, like, in my investigation, basically I could not reproduce this locally to the extent that I saw it on the server. So… What I did was, like, I took the same benchmarks, I ran them on my machine, I ended up seeing, like, and you can see, In this table here, but rather than seeing this massive sort of, like, oh, you know.
like, 100%, in some cases, like, degradation in performance, I'm just seeing, like, a couple percent. So, like, for example, you know, you can see here, like, the average CPU utilization went from, like, 20 to 23 on my laptop. So I spent some time investigating this, and, you know, yeah, I think there's… you know, a reasonable explanation for why we're seeing a little bit of degradation in this case, like increased contact switches, that kind of stuff, which I kind of summarized here in the spreadsheet.
But I noticed that, Basically, the performance that I'm seeing on my laptop and the performance that we're seeing on the server is kind of diverging in, like, a lot of different ways beyond this, even.
And so I just kind of wanted to also show, a couple other graphs in my… Zoom is getting in the way here, but let me just show the nightly batch processor benchmarks, so… So these ones are interesting because I also run a pass-through test.
Where, we don't have any batch processor involved at all, just as kind of a baseline.
And so you can see here, like, this is where, we made the change, but even before that change, there was kind of this massive difference between OTLP and, like, OTAP pass-through.
Like, you know, two and a half to, like, three times less efficient for OTLP versus OTAP.
Which is kind of unexpected, actually.
When you think about it, because for the pass-through case, we're doing literally nothing.
You know, for OTLP, we're not decoding the, you know, the protobuf bytes, right? Like, we're just accumulating them.
Into a buffer, and then just kind of sending them down the pipe.
And so I would actually expect to see… you know, less, resource utilization for, for OTLP compared to OTAP.
And when I run this locally on my machine, that's actually, like, exactly what I do see. I do see a slight reduction in CPU utilization for a pass-through for OTLP versus OTEP.
So that's a little bit unusual, and I tried to get some more data points from, from Albert and Laurent.
And I just kind of have a little summary here for what I found. So you can see, like, this is output from the orchestrator. These are all running the exact same, like, pass-through.
Benchmark that we have.
And, you know, the CPU, like, average on mine for OTLP for doing a pass-through is 13%, for OTAP it's 15%.
That's kind of what I would expect. Laurent has a server, a 72-core Xeon that he ran it on, and he got results that were, like, exactly the same as what we're seeing on the runner machine that we're running all of our benchmarks on in the Hotel Arrow repo, so he saw 50%.
For OTAP, and 58% for OTLP. This is, like, basically exactly the same, because I believe this is also using smooth mode, so this is, like, exactly the same as what we're seeing, on the server after the smooth mode change.
And then Albert was kind enough to also run this, like, last minute, right before the meeting on his M3 Mac.
And he sees something kind of similar to the server, but with, like, much better performance. So, average of 6% CPU for OTAP and 14% for OTLP, so significantly worse for OTLP, but the performance is still overall pretty good.
And so something else, like, I'm kind of, like, pointing out here is also that, this performance for, like, pass-through on the server is, like, unexpectedly very bad. Like, 50%.
100,000 per second is, like, quite low, or, sorry, quite high CPU utilization, and, like, a pretty low, potential maximum throughput, and so, Anyway, I don't have, like, a massive conclusion to this yet, or, like, an explanation, but I think, like, just to summarize, like, kind of the things that we're seeing is, like.
one we're seeing, you know, on, like, potentially large server machines, or… I guess, you know, Albert's laptop is a different case, but we're seeing this huge spike, comparing smooth mode versus the previous mode.
We're also seeing this, like, massive discrepancy between OTLP and OTAP performance, even for pass-through, which is odd.
And then kind of, like, the third thing that we're seeing is, like, the performance overall, on, like, at least the two servers that we tried is, like, much, much worse than it is on a laptop.
And these are, like… Yeah, go ahead.
**Laurent Querel** 41:42 Jake?
**Jake Dern** 41:43 Yep.
**Laurent Querel** 41:43 We… we… the… the… Complementary information that, on the same server.
Depending on if I'm running, manually, the tests.
Without Docker involved.
Pierces, the test that is basically mimicking exactly what we do on the… And the… the runner that we use for this… for those benchmarks.
I see a massive difference… difference.
So, I need to redo it, but I'm usually using the same server for my own test.
I'm never using Docker when I'm doing those tests, Day to day.
And I'm able to achieve, much better performance that… because the result that you've shown before, Into the terminal.
they were… something like 50% CPU usage for a throughput of 100K, which is very bad.
**Jake Dern** 42:43 Yeah, yep.
**Laurent Querel** 42:44 I'm able to achieve, 1 million message per second, signal per second, We use something like, 90%.
Of CPU usage. So, we have something, somewhere, I don't know exactly what, which is totally odd, because… Looks like with just 200K, we are already close to the maximum.
when, for the same machine, without Docker, I need to… do that 10 times to reach the same level of CPU usage.
Yeah, so we have something to investigate there, defensively.
**Jake Dern** 43:25 Yeah.
That is interesting, and I wonder if you'll see, like, the comparative difference as well. Because, yeah, it seems like we have, like, kind of, like, three, like, mysteries. Like, one is, like, worse performance… with maybe Docker.
**Laurent Querel** 43:39 No.
**Jake Dern** 43:40 server machine, not really sure. The other is, like, the comparative difference, like, OTLP looks worse.
than OTAP. And then, like, the third is, you know, smooth looks, like, much worse, than open mode, which is the old one.
I kind of like all three of these are their own mystery.
**Laurent Querel** 44:04 Yeah, the number 3, I think we have a beginning of explanation.
Yeah, we have… At least… at least for… Yeah, we have a beginning of explanation, I think, Dan.
**Jake Dern** 44:16 Yeah, I think we have a beginning of an explanation that says, like, why smooth would be a little bit worse than open. It's not clear, like, why it would be, like, 2% worse on, you know, my laptop, and then, like, 100 or 200%.
**Laurent Querel** 44:28 Yeah, I bet.
**Jake Dern** 44:29 On the server, that's weird.
**Laurent Querel** 44:30 Yeah, I agree, but I think it's on the number one. This big difference, once we have the number one explained.
**Jake Dern** 44:39 Yeah.
**Laurent Querel** 44:40 you will no longer see this, sodly difference between smooth and open. And then we will enter into, I think, a reasonable explanation for smooth versus open.
**Jake Dern** 44:51 Yeah. Yeah, I think that's totally fair, for sure. So.
**jmacdonald** 44:57 Profiles help us here? I've… I've been using Samply, according to the instructions. It works, at least, a little bit. Have… have we looked deeper?
**Jake Dern** 45:06 Yeah, so I did take a couple profiles, specifically looking at smooth versus open, and you don't really see anything in the profile at all. I think the performance difference is mostly coming from, things like context switches and that kind of stuff, which is mostly invisible.
On the profile, like, I did some… After the profile didn't show anything, like, that's when I started looking at this, kind of information, looking at perf counters.
And the two things that you see, like, are massively different between the scenarios are, like, what the page folds look like and what the context switches look like, and I think this is, like, a reasonable explanation.
I was not able… I don't have a server, so… I was not able to profile anything, you know, like on the GitHub runner machine or anything like that, to see if there was a difference there, but I also suspect the profiles would look the same, and it would probably be something more like this.
**jmacdonald** 45:56 stupid.
**Jake Dern** 45:56 look at.
**jmacdonald** 46:00 Thanks, Jake.
**Laurent Querel** 46:01 Okay, so we will definitely spend a lot of time on that, just to… to clarify that before the observability submit. We want to make sure that we have a very good story.
**jmacdonald** 46:15 Yeah, alright. Good mysteries, though. I wrote down the mysteries in the notes.
**Laurent Querel** 46:21 Nice. Jake, do you want to talk about the… If it's not really, no worries. Do you want to talk about the benchmark?
the V2 of the benchmark UI, on which you worked.
**Jake Dern** 46:39 Oh yeah, sure, I could do that. I mean, it's not, you know, 100% done for sure, but if we have time and people are kind of curious, I guess I can reshare. I'm serving some of it, so… Basically, I'm trying to, you know, create this comparison tool, focusing on not just, like, the data flow engine versus, like, the OpenTelemetry collector, but also comparing things like compression and protocol and that kind of stuff.
I've been designing it, like, very specifically to work on basically the exact same, like, methodology that we have, in the Hotel Arrow repo for how we do things, so the idea would be, that this site would be served, you know, just kind of, like, based on some, you know, like, similar method that we have today, where… You know, we run an orchestrator.
We produce, like, some results from that. We take it, we run a script, we crunch it, we produce some, like, static, you know, HTML and that kind of thing automatically based on that.
And then we serve it up in kind of, like, a more, like, slightly more modern site.
And so, this is, like, kind of… what it is so far. The idea is that it kind of has this, like, decoupled notion of, you know, test suites, where I might run something like, the data flow engine at 100, 200, 300, 400K.
You know, with no compression, and just in a pass-through scenario.
And I could run that separately, and I could define a bunch of, like, test suites like that. And then what I can do is I can take them, and I can, via, like, some manifest, define a comparison.
And the intent there is just to say, like, well.
I don't want to put two things on a chart anywhere that should not be compared for, like, some reason, because, you know, they're different in the sense of, like, the work that they did, or the data, like, generation parameters were a little bit different, or something like that.
So I've kind of, like, composed them up into, like, different, what I'm calling, like, comparisons.
So you could look at, like, the engines and protocols comparison, for example.
And see how, you know, different protocols, different compressions, and different binaries are comparing across different throughput rates.
So, you know, on the chart here, it's like a simple bar chart. 100, 200, 300, 400K, you can switch, like, what metric that you're looking at. There's, like, some indicators if there was a problem that was detected, like back pressure.
You can click on a bar, and you can see, like, kind of, like, the raw output from, you know, the metrics that the orchestrator was collecting, and kind of, like, what looks bad.
If you want to click on, like, a file and see, like, hey, what was the backend config that we actually ended up using for this test, you can see that.
You know, all of this kind of stuff, and, you know, can select and remove datasets and that kind of thing, so… Yeah, that's what I'm working on.
**Laurent Querel** 49:29 Nice.
**jmacdonald** 49:30 This is very cool.
**Laurent Querel** 49:31 vote.
**Jake Dern** 49:32 Yeah, and this is, like, mostly focused on, you know, doing comparisons. You'll notice there's no, like, historical trend here. Like, the x-axis, on this graph is not, like, a commit, it's, you know, like a throughput rate. But I think we could imagine, like, repurposing a very similar UI, you know, also to do, like, the historical trends for, like, one throughput instead. So, and maybe swapping out this bar chart for… For a line graph, if there's gonna be a lot of, like, data points on it, but… yeah.
That's the idea.
**jmacdonald** 50:02 That question.
**Laurent Querel** 50:03 connected.
**jmacdonald** 50:04 It's cool.
**Laurent Querel** 50:04 really good.
**jmacdonald** 50:05 Sorry, I just noticed the back pressure detected. How'd you, how'd you tease that out?
**Jake Dern** 50:10 Oh, yeah, we're mostly looking at the, the produced, data rate, and then we're looking at, like, the back end, yeah, we're looking at the produced data rate, basically. So, like, if there's back pressure, you know, there'll be, like, like, this will be below what's expected, so, you know, instead of, like, 400K, for example, like, you'll see, What am I looking at? Let me not look at the badge processor.
**jmacdonald** 50:31 It tends to be when they approach 100% CPU, it looks like.
**Jake Dern** 50:34 Yeah, exactly.
Where is one? Here's one. Yeah, you'll see, like, okay, well, the offered load was 300K for, like, the first 4 seconds, then, oh, all of a sudden, like, it dropped, and we never really got above, like, 240 sustained.
And so the average ended up being 274, like, that's how we detect that.
Yeah. So every test knows…
**Laurent Querel** 50:52 For the…
**Jake Dern** 50:53 should it be?
**Laurent Querel** 50:54 Is it correct? Yeah, it's a combination between back pressure and loss.
**Jake Dern** 51:00 Yeah, I'm also flagging dropped logs, but to be honest with you, the dropped logs are still a little bit goofy, just due to the limitations we were talking about before, where, you know, we don't necessarily get the…
**Laurent Querel** 51:11 We are talking about the OTC right now.
And, not the OTAP.
**Jake Dern** 51:17 For this one, yeah, we're looking at O2.
**Laurent Querel** 51:19 Yeah, and what is saying me that we… I'm aware of the issue when we stopped the experiment, but if you look at the regime.
The throughput over the time, even before we start the experiment.
You are about, 200, 74, At the end of, yes, at the end, can you go, just go over the, the last two that punt in… yes.
**Jake Dern** 51:50 Yeah, 250…
**Laurent Querel** 51:51 What, 15?
**Jake Dern** 51:52 Yeah.
**Laurent Querel** 51:52 If you look at the other side, we are above that.
**Jake Dern** 51:57 Yeah.
**Laurent Querel** 51:57 Not the… in the backend receiver, right?
**Jake Dern** 52:00 Yep.
**Laurent Querel** 52:02 Oh, no, yeah, we have $2.50 or so?
**Jake Dern** 52:07 Yeah, 251 here, and 251 here.
**Laurent Querel** 52:09 Okay, but I didn't interpret correctly, though. I was thinking that we were observing less… Which… Make me thinking that, yeah, we have some data that are lost.
So it's not only, like, pressure in that case, but maybe that's not the issue here.
**Jake Dern** 52:27 It definitely is possible still, that there's, like, some data lost when we, like, sent the shutdown, especially if the hotel collector itself was super backed up internally.
Which I think it was backed up internally, because you can see we sustained 300K for a while, and then at some point, you know, we were starting to get back pressure, from the hotel collector, so it probably was backed up internally, and when we shut it down.
I don't know. My understanding is it's supposed to flush everything that it has?
But I don't know if it actually successfully did that or not, so it is possible we lost some stuff, I don't know.
**Laurent Querel** 53:02 Good.
Yeah, I think that in terms of signal to… To extract and to put on top of the bar charts.
So the, I mean, the percentage of dropped lugs, the back pressure, and the crash event.
I think that these three needs to be representative in one way or the other.
Because if we increase the… the throughput, so right now you are about, 400K.
But we see that for OTAP, we are far from the maximum So we will push the system much more.
And I will not be surprised if… well, yes, we'll tap.
**Jake Dern** 53:50 Yeah, I'm just filtering it down a little so people can…
**Laurent Querel** 53:54 Yeah, for a tap and not a TLP, maybe.
**Jake Dern** 53:57 Yeah, sure. We'll go down, yeah.
**Laurent Querel** 53:59 Oh, wait a minute… oh, okay.
Yes, we all vote, 17.
And… Yeah, so we already… so we already saturated the Go Collector, even with the 300K scenario.
**Jake Dern** 54:17 Nope.
**Laurent Querel** 54:18 And we are close to saturation with the 200.
So we should be able to demonstrate up to 1 million. On my machine, I can reach the 1.2 million.
You know, and that's where the system saturate.
I would not be surprised if we observe some very bad behavior in the Go Collector, if we go over 400K, So that's why I'm thinking that we need to To figure out a way to operate on those, different type of failure.
**Jake Dern** 54:52 Yeah, absolutely. And definitely feedback taken on the little triangle being probably a little bit too small in terms of an indicator.
I'll find a better way to do that, but what I am happy with now is, at least in terms of the way that the site is constructed, I think it's, like, very simple and could be very close to, like, a drop-in replacement for what we have. Yeah.
**Laurent Querel** 55:15 that you already.
**Jake Dern** 55:16 interest, yeah.
**jmacdonald** 55:17 There's something interesting here that I'm picking up on, which we might eventually tease out from the experiment, which, seen in the past, and it's sort of like there's a state change or a phase change that happens in this pipeline when you hit the point of back pressure. And it looks to me like, and I've seen this in experimental… experiments before.
You can sustain a load until, like, the first trip happens, and as soon as you start hitting that limit, and back pressure starts happening, the state changes into a worse place, where it's actually not able to go anywhere near that limit, and that's where it looks like it held the line for a while, and then it tripped over itself, and then it stumbled for a very long time, and it kept tripping over itself, like it's never going to recover. I've seen that In OpenTelemetry SDKs as well, and it comes from, like, having a single queue that you end up filling up, and then once you start having backpressure and sort of scheduling between tasks, you can't produce the same rate as you were because of some sort of thrashing behavior. So I would keep my eyes open for that sort of behavior.
**Jake Dern** 56:23 Yeah, absolutely. Yeah, definitely.
I have also seen the same thing. You might remember I did a lot of batch processor testing. Yes, I do remember that. At the end of my Microsoft tenure.
**jmacdonald** 56:37 Applying it again, so thank you, this is great.
**Jake Dern** 56:40 Yep, yep.
**Laurent Querel** 56:42 So, Another interesting point here is, so it's a HTML interface, obviously, where all the data could be downloaded directly from the web page. So basically, we can host that into GitHub pages.
And and we will add, progressively additional engine.
So today, we have this, open telemetry Collector, and, and, the data flow engine.
That's an interesting discussion, maybe, for later.
Can we add, I don't know, Victor and so.
**jmacdonald** 57:21 Boone's bad.
**Laurent Querel** 57:22 sorry?
**jmacdonald** 57:24 Fluent bit is, one of the ones that we have our eyes on right now. I would love to see that.
**Laurent Querel** 57:31 Yeah.
**Jake Dern** 57:31 Yeah, absolutely. I mean, yeah, you know, this is all just kind of driven off of the same orchestrator framework before, so if we can, you know, construct an orchestrator framework, like, test situation for this, and… Yeah, I mean…
**Laurent Querel** 57:44 Yeah, that would be great.
**Jake Dern** 57:45 No problem, yeah.
**Laurent Querel** 57:46 Yeah.
**jmacdonald** 57:47 It does seem like it can be a static site. I could imagine we generate a Parquet file, and then, what, DuckDB WASM stuff these days for that sort of interactive visualization.
**Jake Dern** 57:58 Yeah, absolutely. The way it works today is, like, very similar, to what we already have, which is where we generate these data.js files.
you know, that have the data, which is what you're seeing on the right here, and then, you know, they're just, like, exporting some variable, or, like, setting some variable in the window or something. But yeah, everything is loaded, like, completely statically, so part of the, like, build for this is it, like, rips through all the data that we have, and then, you know, it'll construct, like, script tags to load, that data into the appropriate, like, pages and that kind of stuff, so…
**jmacdonald** 58:30 Got it.
**Jake Dern** 58:30 Very fast, yeah, and very static.
**Laurent Querel** 58:33 And, sophie and Deep, is there any other, Engine that we need to compare to.
**jmacdonald** 58:44 I… I mean, you mentioned Vector. I… I see less direct calls for that, but we… we definitely see there's a major FluentBit user base that we would love to target.
**Laurent Querel** 58:58 Okay.
Great. I think we are close to the end. Is there one last question? We have one minute.
**jmacdonald** 59:09 Hmm.
Nothing from me. Thank you all.
**Laurent Querel** 59:13 Thank you.
Have a good day.
**jmacdonald** 59:16 See you Tuesday.
**Laurent Querel** 59:17 Yep.
**jmacdonald** 59:19 Cheers.
**Laurent Querel** 59:20 just…
