SIG: Arrow SIG
Date: 2026-01-13
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Albert Lockett 00:01:07 Hey, CJO.
Cijo Thomas (Microsoft) 00:01:12 Hello.
Albert Lockett 00:01:16 How's it going?
Cijo Thomas (Microsoft) 00:01:18 Good. I finally made it to the meeting.
I always miss this one because I didn't have it in my calendar, but now I have it.
Albert Lockett 00:01:27 That was good.
Laurent Querel 00:02:10 Hi guys, la peignirill.
Gokhan Uslu 00:02:17 Hello?
Laurent Querel 00:03:34 Albert just shared, the meeting notes, Google Doc that we are using.
to keep track on, on this, SIG meetings, so, like, Anki actually went to, To look at it, add their name into the, attendees list.
And, and potentially had some, topic… That you, you'd like to discuss?
Gokhan Uslu 00:04:17 There's one thing that… I have in mind.
Laurent Querel 00:04:22 So…
Gokhan Uslu 00:04:23 The authentication is a cross-cutting concern, so, and, you know, you would like To always have a fresh token, etc, and exporters needed, and all that stuff, for example, when it comes to Oauth-based authentication, or…
Laurent Querel 00:04:42 You know?
Gokhan Uslu 00:04:43 You know what I'm talking about. So, I would like to look into… You know, implementing a solution, designing a solution for non-implementing, designing a solution for it.
And, and I'm also still relatively new, but, you know.
I have enough grit, so no problem there. I will… I can take care of that. I just need a little bit of an idea about what direction that… We want to have, when it comes to, solving that problem, what kind of mindset you would like to have, and how to Where to start, the design process in general, just to get some thoughts and ideas and… You know, I think some diam.
Laurent Querel 00:05:35 makes sense.
Could you, maybe just add, a description of this topic into the agenda.
And I think we could spend 15 minutes on that.
Just to make sure that we are all on the same page, and like you said, because it's an important aspect.
Avine, thinking about a specification will definitely make sense.
Well, that's, yeah, so please, describe the, your, your, What you have in mind, and we will discuss it during the meeting.
Gokhan Uslu 00:06:15 Okay.
Thank you.
Laurent Querel 00:06:20 I think Joshua joined us, so Josh, I'll let you drive the meeting.
jmacdonald 00:06:29 Yes, hello. I will try my best to run the meeting, and I would love to not talk very much. So I put my own, important list of PRs to review. I put my own PR there, and I think we should not discuss it today, because I've spent quite a bit of time talking with people who are in the room about it already today. So, I think, I would like to run the meeting, and looking at the two that are, up.
that I see.
I would start with, Drew's issue, and Drew, if you'd like to present, I think you might want to take over.
Oh, is Drew not here? I see Drew may not be here.
Well, since True is not here, I will…
drewrelmas 00:07:16 right here.
jmacdonald 00:07:18 Oh, there you are.
Can't see my own eyes. Okay, Drew, would you like to take, the first item, and take the lead?
drewrelmas 00:07:27 Sure, I can share… Let me know if that comes through.
jmacdonald 00:07:36 Yes, yeah.
drewrelmas 00:07:37 Okay, so this issue is, related to… just repo hygiene and maintenance in general. We had a couple talk… we had talked about this in the last SIG. We also have Tom here, who is interested in becoming a triager in the repo.
I've talked with Josh as well about, you know, how we have 186 issues, and how he would, in an ideal world, like.
Many, many, fewer than that.
So, I also talked offline about this a little bit with Albert, specifically around cleaning up the different OTEP nodes that we all are developing. I think it might be time to bring… it a little bit closer to the collector repo structure, where we actually classify things in exporter, processor, and receiver nodes as well. I know we use the term experimental, but they should really be contribib, I think, like contrib, processor, contributor, contribver for these components that aren't necessarily part of the core data flow, but might belong in a contribib rep repo eventually when we have it.
I also… Josh mentioned to Josh privately, like, I know we have, what is it? Crace… crates?
source, OTAP, I think, is where all the nodes are. I'm wondering if we just rename that to be nodes instead, make it a little clearer.
That's, like, one topic, and then I also just wanted to… I don't know how much we can talk about it in this venue. Maybe it's something separate I can talk about with Tom as he wants to start picking up the triage responsibilities.
But I think being careful about, issue type usage, I saw Albert actually start… to, Oops, here we go. Start to use, task, feature, and bug, which helps kind of clarify the scope of work. I really like what he did with making the parent item a feature, and individual, sub-issues.
tasks underneath, that makes it very clear. And then the final piece that I was going to talk about was, I know we have a lot of labels that all kind of refer to core data flow, concepts, and I'm wondering if we really need that many labels, or if we can settle on one to represent OTEP, or OTAP data flow, like.
engine capability, and then, Albert and I were discussing maybe labels per component, per node. I don't know if per node is the right thing. Per node, source folder, similar to how the collector does it. So, that's my spiel. I'll stop here if anyone else wants to say anything.
Laurent Querel 00:10:50 That's really cool. I really like to put some order there. It's definitively, A little bit of this.
And if it's a good time to do something.
Regarding the… renaming of the tap and experimental stuff, stuff, I would suggest to, Like you said, nodes, but prefixing it with score for the tap.
So, it's clear that it's related to core nodes, and for experimental, related to country-nodes.
So we… we know that it's of some, the same nature, or the same kind, but, One is for core, and one is for Contrio.
drewrelmas 00:11:36 Just a suggestion, and .
Laurent Querel 00:11:40 I know that, you'd like also to, to have some credits, published, for me, the… The main constraint, or the main conditions to be able to do that are first to… Establish a proper prefix for all the crates related to this project.
Then making sure that we, we have good names for the… or good suffix.
For the existing crates, and we follow some kind of convention for the new one.
And then… Also, making sure that all of us, we agree on the fact that, Right now, the API… let's say the stability level is still… Pure development, in my opinion.
So we will not offer any stability in terms of API, even if they are published on Craze.io.
That for me is, A strong requirement.
Right now.
Because I think it's too early to, to make the API, level 1.
to… by any means, so I think… I still think that we need to… to be able to refine the API, even the public API, as we want.
At least for the next, for the next tutorial.
Maybe we can think about stabilizing some of those API during the next quarter, but for now.
I don't think it will be reasonable.
drewrelmas 00:13:31 Regarding the labor.
Laurent Querel 00:13:35 I'm perfectly aligned with what you said.
Yeah, I think that's, I think the, Also, the effort that we started on the, the telemetry, semantic conventions and all the guidelines that we started to put into this project that are not yet fully Followed, but at least we have a bunch of documents describing them.
Regarding the label, I think that would be nice, if we can also align When that makes sense, labels with the entity model that we are… We start to put in place.
So we have, entities like pipelines, nodes, channel.
And we will refine that a little bit further.
So, we should retrieve the same terminology, at least for a subset of those labels, and I see here the pipeline, that's cool.
Yeah, I think that's the main feedback based on what you just said.
For me.
drewrelmas 00:14:51 Okay, it's good to hear. I think we're mostly on the same page. I view a lot… I view a lot of this repo reorganization as A precursor to… Us, you know, deciding to publish crates. But beyond that, it also just makes our lives easier as we're doing PR reviews and issue triage.
You know, I left some general goals up at the top. You know, ideally, I'd like to see every issue having a label. I want to make sure, like, try and use good first issue and help wanted accurately. And also, you know, ideally, every PR is linked to an actual issue.
Yeah.
So, with that, I think I should stop for today, because, you know, we're taking 10 minutes on this, but if anyone has feedback about this, you know, we can feel free to message me offline.
or Tom, as well, and hopefully we can start to do some of these throughout the repo, and at least take a look at our existing backlog and try and start classifying them, with labels and types.
Laurent Querel 00:16:05 It's all agreement.
drewrelmas 00:16:09 Alright, if anyone else wants to take over… I will stop.
jmacdonald 00:16:15 Thanks, Drew.
Yeah, I've tried to take notes, I think I captured it.
There's a… there's a… an issue number for publishing the crates as well that's got a few more things that people have said or want to see before we choose our, before we finish deciding to publish those crates.
For myself, I wonder if using the OpenTelemetry prefix is a good idea. I think it might be. It's one that we already have access to and have used a prefix across the OpenTelemetry project before, so… That's worth exploring. We have some deduplication to do at that level as well. The proto-crate inside of… sorry, the proto-module inside of the OTAP DFP data crate is duplicate with the OpenTelemetry protocrate, for example.
I see a comment from CJ. There's no prefix reservation, so sounds like we'd go through the ordinary crates.io release process, and I still think we could use the OpenTelemetry prefix.
Cijo Thomas (Microsoft) 00:17:25 We can if it's not taken by someone else.
jmacdonald 00:17:28 Right.
Laurent Querel 00:17:30 Wait, which is, not a pro… not a… I mean, not a problem due to us, but it's definitively a problem in general for credits.io. Unfortunately, people can hijack, A prefix just to… Put us in situations that will not be present.
But we can't do anything for that, unfortunately.
accept reserve, those, those create names. The… Open telemetry dash something.
So you are already using that CGO for the REST client SDK, right?
Cijo Thomas (Microsoft) 00:18:09 Yeah, but it's not just us, like, anyone else can create a crate with… starts with OpenElementary-foobar.
it all looks the same, but if you look at the actual CreateStore.io page, then there is a section called Publisher or Owner. That's where it shows, okay, this is published by OpenTelemetry, the other is published by someone else, so that's the only way you can put some legal or official status to it. The name itself is… it can be anything. It's very different from every other language, where, like, OpenTelemetry.east or OpenTelemetry Star is reserved by the OpenTelemetry organization, so nobody can publish to that.
But unfortunately, grades.io does not have that.
Laurent Querel 00:18:52 Yeah.
A question for people that are running the REST client SDK and API.
If we use the same prefix between those projects, Then we… without additional… a separating element, then we could face some… some collision, or, I mean, some discussion about potential conflict collision. So, for example, if we… for us, we have, try to remember all the crates that we have. That could be… So, Joshua mentioned the proto.
So that's a typical example where we could, An interest to share the same… the same crate, which is fine.
Cijo Thomas (Microsoft) 00:19:43 But we could end up into a situation where.
Laurent Querel 00:19:47 We want to name a crate with, something that is meaningful for us, but which is not something That is necessarily the same meaning for the REST Client SDK.
And then we end up with… a need to find a new name, which is okay, but I'm just trying to think about Do we need to use exactly the same prefix, or… Maybe for us, if we give you hotel-something, and for you, you already use open telemetry, and then we have a different scope.
Cijo Thomas (Microsoft) 00:20:24 Yeah, so do you already put a suggestion which I think is very good, like, you can use OpenTelemetry-OTAP, then the actual component name for anything published from the IRO project?
Laurent Querel 00:20:39 Okay. That's a very long name, but, okay.
drewrelmas 00:20:47 Josh is also…
jmacdonald 00:20:48 Listen.
drewrelmas 00:20:48 regretting in the thing, we use Hotel Arrow, as that's the name of the repo.
Albert Lockett 00:20:58 Yeah, that's…
jmacdonald 00:20:59 I wrote some down, some of the ideas I heard in the notes.
I don't have a strong opinion.
Shorter names are better.
Laurent Querel 00:21:11 Yeah.
Hotel-hotap, dash something.
Oh, open telemetry that shut up, it's long.
Albert Lockett 00:21:20 like, the OTAB… is already an abbreviation that contains OpenTelemetry, right? So, like, OTEL, OTAP would be, like, interpreted as, like, OpenTelemetry, OpenTelemetry error protocol, so it might be redundant.
Laurent Querel 00:21:32 Mmm, yeah, I agree.
I agree. Okay.
Albert Lockett 00:21:41 No, no excuse.
Laurent Querel 00:21:42 So I guess we have to think about it a little bit more, and Anyway, we are in the process of cleaning up the… or preparing the for the publication of those credits, so we still have time to decide, I guess.
jmacdonald 00:22:03 I proposed that, one of us, and I will determine who, after the meeting, one of us on the Microsoft side would be glad to Try and finalize a list of what's required, name review, checklists, and so on. That could probably fall under Tom to find any other issues and make sure they're complete, as we triage So, we'll take another look at that, next week.
I guess, to continue with the meeting, I can share now, my screen, and CJO, you have an item up, and there's nothing after that until Gokan, so why don't you go first, CJO?
Cijo Thomas (Microsoft) 00:22:45 Okay, yeah, I'll quickly share my screen.
jmacdonald 00:22:50 Sure.
Cijo Thomas (Microsoft) 00:22:54 Can you, tell me what you see? I have multiple windows?
Laurent Querel 00:22:59 I see the Google Doc.
Cijo Thomas (Microsoft) 00:23:01 For meeting notes, okay, so you should be able to see the… the peripherals page. That's what I intend to show you. So this is something which I briefly asked, probably in, like, December timeframe. So, when we run load tests, especially the one which tests the engine to the extreme.
By putting, like, very large amount of load, we are seeing, like, data loss, like, consistently.
It was, like, within, like, 0.1% or 1%, but sometimes it spikes to, like, 1.6.
And this is consistently happening, except in, like, yeah, in some cases it doesn't, but then there are other tests where we are, like, consistently, losing some percentage of logs, like this one, yeah, except, like, 4 times, we were always losing, sometimes as high as 5%. Initially, I thought it's because, like, we are missing something in the the puff test, when we are doing the saturation test, where we are pumping a lot of load. But then I also look at the filtering.
test, which… in which case, we are filtering, like, we are, by design, filtering some logs, like, approximately 95% of them, so the remaining is, like, 6%. So, even in that case, we are losing logs. So, for example… In this case, like, by design, we are supposed to filter, like, about 94%, but the blue one, which is OTAP and OTLP, in those cases, we are, like, losing 100% of the log, so we are effectively losing the 6%. The same page shows the collector one.
This is collector, and you can see Collector is only dropping 94, not 100, so it is only doing what it is supposed to do.
So my question is, does anyone have any, like.
ideas on what might be the reason why we are losing data. It's, I know that we are, like, doing some stress testing, but I expect We should be either applying back pressure, or we should be losing faith.
some internal log, which tells that, okay, I'm losing something, but I don't find anything here. So, I will be… I was trying to look at it in detail, but I haven't done that yet. My first question is, does anyone have any indusions or clues about what might be going wrong?
Laurent Querel 00:25:29 On my side, no, I don't have a… it's a surprise, not a good surprise.
Yeah, we definitely need to investigate that.
So… How many, how much, when you say you… you put the system under stress.
How much, logs did you.
Cijo Thomas (Microsoft) 00:25:59 Let's look at one specific one, so maybe I'll use any of the… so these are all the stress tests, maybe let's focus on this one, where we… use, like, 2 cores for the engine, and it's almost at 90-something CPU, and the max is also around that. So this is, like, almost saturated. Not quite 100, but pretty close to that. And in that case, we are…
Laurent Querel 00:26:26 What I don't understand is when you say 2Core, two-core for what? For the, for the system under test, or for the system that is generating the load?
Cijo Thomas (Microsoft) 00:26:35 No, this is, the system under test, which is the data flow engine.
Laurent Querel 00:26:40 Okay, and the system under… but, so, back to my question, so you measure this, close to 100% CPU usage.
With 2Core, but for which, number of, for which rate in terms of logs.
Cijo Thomas (Microsoft) 00:26:57 For which?
Laurent Querel 00:26:58 How much blogs are you generating in the traffic generation stage?
Cijo Thomas (Microsoft) 00:27:03 Yeah, so that's shown here. So we are producing approximately 300,000 plus logs.
And we are receiving, and the fake backend is receiving, like, 1% less than what we produce. That's why the lowest percentage is around, like, 1-2%.
Laurent Querel 00:27:21 Okay. And those 300,000, that's the number of logs per segund, or the…
Cijo Thomas (Microsoft) 00:27:28 For a second, yeah.
Laurent Querel 00:27:29 Yeah.
So that's very strange, because… on my own server, and we have something weird there, definitively, and I don't know if it's a bug, if it's a… where is the bug, but there is a bug. On my side, I measured 1.7 million logs per second.
of Procore.
And I don't think I had observed a loss in that case.
Yeah, so the… definitively, there is some, some issues.
I don't have any, any, Ideas, where… why we are observing that.
Cijo Thomas (Microsoft) 00:28:15 Okay, yeah, then I'll start digging into it. Anyone else, like, with any clues where I can go and investigate?
Oh, just one more thing to add, it's not just the case where we are hitting, like, 100% CPU, so this is the filtering case where we are, like.
CPU is barely, like, half, like, this is not even 50%.
Even in that case, we are… in this case, like, this test sheet designed for, like, filtering scenario, so it is supposed to filter, like, approximately 94%.
of the log, so we should be seeing, 94.70. Yeah, this is the expected outcome, but this one is, like, 100. In this case, we are not even putting the system under, like, huge pressure. It's, like, normal CPU, like, RAM is, like.
few megabytes, and we have a straight comparison with Collector, where Collector is doing the right thing. It's, doing, like, only doing what it is supposed to do.
Laurent Querel 00:29:12 Yeah.
Cijo Thomas (Microsoft) 00:29:13 I have a similar question, this is something in the Slack also, we are trying to discuss this one. So, so this test, this page shows, the same test targeting TF Engine and Collector, same load, same configuration, and I was a bit surprised that there isn't much difference between the resource consumption in collector and DF engine, that was also a surprise to me, because based on what, Laurent, you mentioned, I was expecting, like, a significant more.
like… Yeah. So, this is the case, like, this is a… DF engine, we are taking around 40, like, all 4 scenarios we are only doing.
40 megabytes, and collector is also, pretty much same, except the… Yeah, I mean, it's around… 20, 40 megabits, but the moment OTAPs involved.
Then Collector goes crazy.
So in the typical, like, OTLP to OTLP scenarios, it's, like, collector is, like, quite comparable to Rust engine. The green one is the OTLP to OTLP, which is the common scenario. So you can see collector is also doing, like, pretty decent, like, even lower, slightly lower than DF engine.
And…
Laurent Querel 00:30:35 So that is, for… Because I could understand why it's closed if we have, A low number in terms of, log rates.
Oh.
Cijo Thomas (Microsoft) 00:30:49 So, doing, like, 100,000 plus, so this is the log.
Producing the rate at which we are producing. So, the incoming load is around 100,000.
per second, and the receiving is, like, 5 to 6,000, because we are dropping, like, 95% due to filtering. So it's not, like, very low load, But yeah, the outcome, the net egress is, like, very low, like, 5000 per second.
Laurent Querel 00:31:22 You know?
Yeah, I expect the difference being much bigger when we increase significantly the number of logs per solution.
But we… it looks like we, we have some issues anyway there in this specific setup.
And maybe into the engine itself, so…
Cijo Thomas (Microsoft) 00:31:42 Okay. Anyway, like, to, like, investigate this one, Lauren. Like, I just wanted to see if anyone has any cute ideas, so we'll continue investigating this one, and maybe I'll find something by the next time we meet.
On the same topic, there is another thing which I… I don't have the exact data, but I… this page was… or this kind of test was… what it is doing is it tests with 1 core, 2 core, 4 core, 8-core, 16 core, where the engine is running. So if the thread per core Share nothing architecture is to be trusted, then… when we go from one core to two, and so we… we should see a proportionate growth, but we are not… we are still growing, like, linearly, but sublinearly. We're not, like, when we go from 1 to… 16, we are not seeing 16 times the throughput.
But we are probably seeing, like, maybe 10 times. So we are not linearly scaling, so it shows that there is some contention, like, there is some mutex or something which is affecting the throughput as we increase the number of cores, but I mean, this is very hard to look at these numbers as is, so I have a, to-do.
To clearly show the routine.
Laurent Querel 00:32:49 to combine the chart together, yeah. Yep, yeah. Yeah, that's super interesting. I think that would be a fundamental for us to make sure that we, We don't introduce any regulation. Maybe we did recently, so… Yeah, that's super interesting stuff.
Cijo Thomas (Microsoft) 00:33:09 Yeah, I will do one thing, I'll just… I mean, I have one issue created already, but I'll create a better chart so we can easily see how much, like, I don't know what's the right word, like, scaling factor or something, just to see, like, if it's 1, which means we are linearly, truly scaling. If it's 0, we are not scaling at all.
So I'll produce a chart which shows the actual, like, scaling fat, how much we are scaling with the number of cores.
And then, I'll create an issue to track with that, and hopefully, like, I'll be able to get to the why, like, why we are losing data, but otherwise, I'll reach out to some people. I haven't had the chance to look into the, like, engine internals yet, so that's why I'm trying to see if anyone has any quick answers.
Laurent Querel 00:33:49 Me too.
Cijo Thomas (Microsoft) 00:33:49 I'll continue to investigate this and update my findings in next week.
Laurent Querel 00:33:54 And, and if you, during your investigation, you see, Some missing metrics that could be helpful to, to track that.
Cijo Thomas (Microsoft) 00:34:04 Yep.
Laurent Querel 00:34:05 Yeah, that's…
Cijo Thomas (Microsoft) 00:34:07 That is the main reason why I added some logs internally, because I know that we are losing locks, but it's… hard to know without any metrics or logs, so that's one of the reasons why I started adding, some logs here and there, just to my own investigation. But now, I've reached a point where those logs are not telling anything, because we don't have full instrumentation yet, so I'll have to dig more into it to figure out why.
The good thing is, it's reproduced locally, so if you're on the same load in my local machine, I can also see that it's losing log, so it's not, like, hard to reproduce, which at least gives me something to go on.
Laurent Querel 00:34:45 Okay.
And, regarding the sublinear, scale.
I think one aspect that we need to… to check is, the number of, Parallel connection that is reaching the system under test.
To make sure that we, we are… because one aspect that is still not addressed properly into the engine itself is when we have A bad distribution in terms of, connection.
Based on the quadruple, client IP address port, same thing for the server side.
Cijo Thomas (Microsoft) 00:35:30 So the load balancing mechanism that we use rely on the…
Laurent Querel 00:35:34 This quadruple, and the kernel will use the quadruple to load balance We have options, here at FI for… A better load balancing that we could integrate.
But, right now, it's only based on that, on the regular, kernel level load balancing for, SOU Sport option for sockets. So the, Depending on how the traffic is venerated.
We could end up to an unbalanced situation, which could explain why we don't have a linear scale. I don't know if it's that… if that's the case there.
But that could be the problem.
Cijo Thomas (Microsoft) 00:36:18 Okay, yeah.
Yeah, okay, I'll keep investigating, I… hopefully, like, I'll get something, but if I get stuck, I'll reach out to, like, one of the maintainers in Slack.
Laurent Querel 00:36:29 Okay.
Cijo Thomas (Microsoft) 00:36:31 Thank you, that's all I had to cover on this topic. Josh, feel free to take over.
jmacdonald 00:36:40 Thanks, CJ.
I put some notes in the document. I feel like we should mention it could be that there are bugs in the OTLP or the OTAP conversion that we haven't spotted yet.
I'm totally interested in knowing what's going on.
Also, you know, like, this is… there's a… there's a specification or an RFC in the Go Collector repository that's about Standardizing pipeline metrics.
And the standard metrics are meant to help us with identifying this type of leakage or loss. Like, you… if every component records the number of items that come in or are consumed, and the number of items that go out or are produced, and then you can see in a chain of components exactly which one is not producing the right number, assuming that you sort of instrument from the outside. Like, if the pipeline itself or the channels themselves were to instrument the numbers consumed and produced, we would spot the number that differ, and we could even spot numbers that are dropped, sort of, in handling. Like, if you consume something and don't produce it, and you don't have the right metric, it's because of a code bug, and we should be able to spot that in the metrics as well.
Laurent Querel 00:37:53 So, we have that now, by the way.
end of December, I added, the channel matrix?
That report, the number of batches.
Yeah, right now it's at the batch level, so we need to put that more at the signal level.
But we have the infrastructure now to follow that automatically without any modification on the node implementation.
jmacdonald 00:38:22 Sounds like CJO could use those metrics then, I would hope. That would be maybe an ideal, at least.
Cijo Thomas (Microsoft) 00:38:28 I'll start with, like, using those metrics in the performance test, so we'll have those metrics handy, and then see if any of those metrics can give you the answer, like, as to why or where we are losing.
Laurent Querel 00:38:41 Yeah, the only missing part, I think, right now for this investigation, regarding the input-output of each node is the fact that right now, the channel matrix are at the batch level.
Which would be… Not good enough for this investigation, because you need to look at the… the signal level. The reason why they are not there, is… is not because I forgot them, it's more because… We have some optimization that prevent us to to determine… Without losing the optimization when we, what number of signals we have into a specific, With that batch.
Cijo Thomas (Microsoft) 00:39:28 So…
Laurent Querel 00:39:29 I think what we need to do is to have A debug, or no… not a debug mode, but, We need some kind of feature or something like that, that will fork the engine to… Report the number of signals per batch.
So every, Channel extremity.
And in normal mode, we, we will just report them when they are accessible without de-optimizing, the, what we have in place.
I hope that makes sense.
Cijo Thomas (Microsoft) 00:40:11 Okay, yeah, I didn't quite catch the last part, but that's partially because I haven't done enough, like, research into what kind of things goes on inside the engine.
So I'll do that.
Laurent Querel 00:40:22 Okay, I will, I will send you a message, or I will describe that into the hotel dev… the Hotel RO dev channel.
Yeah. Later to build.
jmacdonald 00:40:33 Can you say more about what you meant when you said batch level, not signal level? I think I'm missing it as well.
Laurent Querel 00:40:39 True.
So… the channel, that are used for the communication between the nodes.
from the receiver to the processors to the exporters, those channels transport OTAP batch message.
An OTAP batch message is basically a batch that is either represented as OTL key bytes.
That's the optimization I was referring to.
or they are, OTAP, batches.
And they are represented as a set of Apaccio records.
when they are represented as Apache Arrow Records.
It's super… it's basically cost-free to report the number of signals.
We just have to look at the main hotel Record.
And then we can just return the number of lines that is into this, Aperture will be called.
when it's OTLP bytes, If we want to detect the number of signals, then we have to translate that either into OTLP representation.
Or into a type of presentation, like we do automatically when some of the processor or exporter that require to have a An understanding of the content, they, they, they trigger this deoptimization.
But, there are some… pipelines, and and for example, some of the pipelines that are used into the continuous benchmark and IT benchmark.
They don't trigger that and keep the optimization.
So, if we… if by measuring things, it's like a continuous… In the quantum world, if we start to measure things, then we remove… by observing that, we remove some optimization… some of the optimizations.
So what I'm saying is… For the benchmark.
So we need to do two things. For the benchmark, we don't want to remove the optimization.
So we can't, Collect… for some of the pipeline, we can't collect the per signal versus per batch matrix.
But we need that to do some investigation, or to do some validation process.
So, in that case, I'm suggesting to have a special mode, like a feature, or… Maybe a parameter.
Where the… the per-signal matrix will be collected.
With the effect of sometimes removing sub-optimization.
But, and then we will have enough information automatically to… To investigate and look where we are losing, potentially, some signals.
I hope that's… it's no… more clear.
jmacdonald 00:43:47 Yeah, I was, I wasn't following at the beginning, but now I get it, and I mean, you're right, it would cost us something to scan the OTLP bytes using our view, even, you know, it's not… it's zero copy, but it's something.
And so you might not always want to configure the… signal count metric. There was actually a long discussion this week and last week at the hotel specifications SIG about conditionalizing metrics and, like, level of detail and so on, so we're talking about a good, hard problem.
The terminology that the collector, the Go collector uses here, that I'm more familiar with, not to make that sound better, but just, is the idea that we count requests We count, items, and we count bytes. Those are, the ones that I know, and so the request is always one per batch.
items is a signal definite… per signal definition. It's number of spans, number of log records, number of metric data points, is sort of like the words that I'm familiar with in the hotel world, as well. But when you say signal, I have seen that used, and it's not totally uncommon to call them signals.
And then the matter of bytes is one that, it is expensive when you're in the OpenTelemetry Go Collector to count bytes. It's the same sort of situation you explained with counting items in our pipeline. You have to do some work to count bytes, and so you wouldn't always want to do that.
Nevertheless, someone might want to turn it on because they're, for example, monitoring compression, which is something I was doing a couple years ago.
So, asking for bytes metrics is reasonable as well. You expect to pay for it, hopefully not too much.
And the same goes for items. Those are quantities you want to rate limit by as well. So, anyway, those are things we can talk about again.
Thank you.
I know that.
Laurent Querel 00:45:47 The signal terminology that I used, is… Commonly used in the semantic prevention world.
Of OpenTelemetry, maybe not in the rest of the OpenTelemetry.
jmacdonald 00:45:59 Maybe it's just me, it's out of date. Thank you.
Yeah.
profiles, anyways. Okay, so, looking at the notes, that we have here in front of us, I want to give a moment, to… to at least two more agenda items ahead of us.
I've crossed out my own because I don't want to talk about it. It's not ready, so I know what I need to do there. Aaron, who's on the call, I see, has put up, I'll say, a large PR. These are big PRs so we can, you know, move fast, and I have reviewed it.
Couple of us here have, and I just want to give you a moment to describe it, Aaron, or ask for any specific help.
Also, I want to plug the very good screenshot of, anyway, Ratatouille Library. Cool stuff. For anything you want to say, please do.
Aaron Marten 00:46:49 Sure, yeah, we could definitely use some more eyeballs on the PR. Yeah, I know this one, this one is a big change. This is, like, the third, major PR For Quiver itself. So the… I think the bullet points kind of describe what's… what's, what's in this one.
The main, kind of, big feature is this actually kind of completes the end-to-end ability to, ingest data into Quiver. The previous PRs wrote out to the write-ahead log and the segment file format.
This one allows you to actually… it finds a read API, so you can consume consume these segments, it introduces this notion of subscriber, so you can have multiple subscribers, reading these segments out of Quiver.
Subscribers can report back progress on individual bundles inside of a segment, so they can mark those complete. And all the bundles in a segment have been marked complete, the segment will get cleaned up.
Let's see, there's a feature for, having a shared disk budget, so you can say, like.
You know, I've got several different, Quiver engine instances, so, like, for different signals, for example.
And then, they have a shared disk budget, with a cap enforcement, so we could say, like, I don't want to use any more than, like, you know, 300 megabytes or whatever.
And then, it will make sure to apply back pressure if we're, hitting those, hitting those limits.
Some of this was cleanup, and then, yeah, the thing that Josh alluded to was this quiver end-to-end crate, which is a new bin crate that I added. This was mostly for my own, kind of.
Wanting to do, you know, start doing end-to-end testing on Quiver in isolation before we get started on, the next phase, which is going to be creating a, processor in Hotel Arrow, the persistence processor that will, use Quiver. So, this is the… Oh, sorry, I'm not sharing my screen, so you can't see this, but if you scroll down to the comment, you'll see I pasted the screenshot in there.
Yeah, so this is the… the ReptaTui-based, interface in that… in the end tool.
And you can, you know, if you check out this branch and build it, you can run it yourself.
And it will… you'll kind of see it, data flowing through there. The default is just to have it You know, single producer, single consumer.
You can tweak some of those parameters, and I'm sure there are, you know, plenty of additional ways we can enhance this tool to do, kind of, local testing of quiver in isolation.
But it helped it flush out, quite a number of bugs during development, in this PR.
Yeah, I guess that's about all I want to say. It is a big PR. My apologies for it being so big. I expect this is, like, the last really big PR that's going to come through related to Quiver. Everything from here on out should be More bite-sized.
Laurent Querel 00:49:56 I think Sheila Ron has his hand up.
Yeah, that's fantastic, fantastic PR. I didn't, I started to, to look at it yesterday, but, I need much more time, but I will definitely, continue later today, and probably tomorrow morning.
Yeah, definitely, I will focus on that in terms of review.
review tasks, by the end of tomorrow.
Aaron Marten 00:50:33 Cool, thanks.
jmacdonald 00:50:35 Thank you. My comment, just to follow the fun, fun screenshot here, is that this would make a great exporter for the data flow engine itself. You can imagine configuring a bunch of queries and having it paste up, terminal UI for us to watch our own telemetry.
In flight. That'd be fun. Could use the queries of the pipeline metrics that we just discussed.
Very cool, very cool.
Alright.
Thank you.
So I know a couple more people are going to review your PR. Thank you very much, Erin. All right.
And then, let's see, I know that GoCan asked in the beginning, and now has entered, this item, so I just want to pre… let's see, prefix this with, that I know some of this topic, and I know, I think we're talking sort of about how you configure these things that in the Go Collector, we call extensions.
what's an extension? I don't think we need to go exactly into that yet, but it is kind of close. And so, Gokan, are you on the call?
gokhan 00:51:40 Yeah.
So, I, in general, wanted to hear about anyone who has any thoughts and ideas, or any vision about how this should be implemented. By this, I mean, what I'm trying to specifically solve is, the authentication, Based on token-based authentication with headers, for the GigaLay… for the Azure Monitor Exporter that I'm running.
But, you know, authentication can be done in many ways. MTLS can be authentication, so I don't want to create an umbrella term, and I don't want to also, like, just talk about it in terms of whether it should be an extension or not. It could be a library, it could be anything. I just wanted to understand if anyone have any expectation, vision, and idea about how Cross-cutting, how auth should be, implemented as a cross-cutting, concern, or, like, be designed as a cross-cutting concern, when it comes to specifically header-based, HTTP-based, or gRPC, you know.
There's stuff like that.
Laurent Querel 00:52:53 I didn't thought too much about it yet.
Definitely an interesting topic to, to address.
gokhan 00:53:02 So, a few things that I know we would need is, for example, we would need to refresh the token periodically, so there would need to be at least some kind of… Job.
Running.
I can… async thing. So that, that would need to start and stop, probably, like, an extension, or probably, like, an exporter, whatever, or probably, like, a proper processor, whatever, or, like, anything, pretty much. And then, it would also, need to Be usable by the consumer so that, you know, you can access that.
token, something like that. Or at least you can… maybe, like, an HTTP effect… HTTP client factor, for example, if this focused on HTTP, or, like, gRPC client factor, or whatever you might, think of, yeah.
Albert Lockett 00:53:55 One thing I would mention is that, I vaguely recall that we had a conversation about this, maybe a few months ago, related to… and it was in the context of, having the Parquet exporter work with, Azure, Azure's object storage solution, and I'll post the PR in the, in the meeting notes to have a look at. This is some work that, that Jake did for us, to add a, an Azure Cloud Auth.
module, into the, the OTAP, Crate, and so the thinking was that maybe this would be, something that… yeah, so I posted the PR there, 1517. The thinking was that, like, maybe, this could be the start of a module that would have some, utilities, and, and some configuration structs for.
different, components that need to interact with, with cloud storage to use. Yeah, so you can see that here we have, this auth method, enum, and, and so in the Parquet exporter, this, this was included, in the config, and then so you could.
You could put this in the in your component's configuration, and then this would drive code that would figure out how to authenticate to Azure. So anyway, just throwing it out there that that's at least, like, one pattern that, that we already have.
Jake, I see you're on the call. I don't know if you have anything else to add about this, or if I'm kind of putting you on the spot, but, anyway, this could be a start of what you're trying to, implement GoCan.
Jake Dern 00:55:51 Yeah, I think you summed it up pretty well. Not too much to add for me other than, you know, I think, like, one disadvantage of having the pattern that you mentioned, where we embed, like, a similar config in every single struct, is that then each one of those, like, individual components would probably be, like, managing their own, like, different auth instance. So, like, for example, for Azure, they would each be having their own individual token credential that they construct, so… I think, like, the benefit of the pattern of pulling this out into, like, an extension or something is that then every component can query that at runtime and be sharing that credential, if that makes sense.
Laurent Querel 00:56:30 Yeah, I think definitively, for the… By grant engine in general, what we try to do is to, reify, as much as possible, cross-cutting capabilities when we see the retry processor, or soon we will have a failover processor.
the, the ACNAC mechanism… The back pressure mechanism that we put in place.
they are independent of NUD's implementation, and that's an important design decision. I think we should observe the same kind of approach for the, the OAT, for the OAT component.
So I totally agree with what you just said, Jake.
And, I think this topic is big enough to require like we did for Quiver, for example, we had, A very detailed specification.
On which we had, multiple, round of, review… review.
and feedback, I think we should start with exactly the same approach.
Because it's a, it's a, it's a critical, part of the system.
I think we need to review that, extensively, and, and, Provide feedback, and then start the implementation.
Once we, we all agree on the design.
gokhan 00:58:04 Yeah, makes sense. I have a similar idea as well, and yeah, this initial feedback helps. I also think, Having… for example, if there's going to be an, Azure authentication method like, to the same, for the same identity or whatsoever, they should be possible to, be shared across, like, multiple exports or something like that, so that… Yeah, there don't have to be multiple jobs running, they're all trying to get the tokens, etc, stuff like that.
jmacdonald 00:58:44 That's sort of the basic, sort of outline of an extension in the Go Collector, is that it's this entity which you configure with a specific configuration struct. There can be more than one of them in a configuration. They have names, so you can choose the first configuration or the second configuration of a particular type.
Which means you could have more than one Azure authentication credential in a single pipeline if you need it, or you could have one and reuse it and multiple exporters if you need it. So aside from having a name and an entity and a configuration.
They have a start and a stop method, or something similar to that. And then after that, that's the sort of, like.
the engine knows how to start them and stop them. When we call it an extension, what we mean is that there's some other API that you can get to somehow, and this is where, like, it's a question of how we do it in Rust. Like, you can get to that same extension that we said was an auth.
And we say, okay, now I know that I'm using HTTP, and I want an auth, so please give me the request middleware thing for off.
Because that's what I need, and then, you know, hopefully, dynamically, you can sort that out and get the thing that you need at runtime through the extension, which the engine doesn't know really much about. It's only the components that need to know, know how to use them.
Laurent Querel 01:00:03 Laurent? Yeah, yeah, so we… unless, Last element I think we need to take into consideration for this design.
This design has to be… has to support, even if it's not necessarily the first version, but has to support multi-tenancy.
We, we, we need to be able to, to support complicated enterprise-related deployment, where for the same pipeline… a tap data flow engine. We can support multiple pipelines.
And some of them could be attached to a tenant.
They could have different policies in terms of, authentication.
They could bring their own, certificates. This kind of things need to be, in my opinion, Supported, into this, new system.
gokhan 01:01:05 What do you mean by multi-tenancy in this context?
Laurent Querel 01:01:10 Oh, so you, So we have one process, or multiple, let's say, instances that will be deployed on Kubernetes, for example.
But each of those symptoms is… or pods, could, process the, the traffic The talented traffic of different tenants.
A tenant is basically when you… for example, Azure. Azure is, a platform where people can deploy their infrastructure, their software and so on, their SaaS infrastructure.
And, under the wood, Azure is a multi-tenant Infrastructure, so you can… you can share the same resources for multiple Azure customers.
We could imagine that, the, this, engine system, OTAP data flow engine.
Could be used in a search deployment, where we have to support multiple tenants with the same process.
gokhan 01:02:18 So would that mean, like, for example, just, guessing here?
there's one pipeline instances running, and there's an exporter there. That exporter should be capable of exporting to multiple tenants, or do you mean, like, I could have multiple exporters that use multiple authentication configurations for different The, you know, like, tenants and stuff like that.
Laurent Querel 01:02:46 We could imagine various deployment mode.
Soon the system will support the ability to run multiple pipelines. We could have… we could imagine a mapping where We have one pipeline per tenant, that's an option, or we could imagine a single pipeline for multiple tenants.
And what I'm saying is, I think we, for this authentication mechanism, on the… The policy that will be attached to this authentication could be different depending on this tenant ID that we can collect either from HTTP headers or from some other mechanism that we need to define.
gokhan 01:03:31 Okay, I understand. I don't know if, at least, I didn't get exactly how it would work if it was a single pipeline instance for multiple tenants, because that also would mean that exporter need to support it, or something like that.
jmacdonald 01:03:46 Well, I think the way I would interpret those words, again, kind of projecting this into my mental model for an extension in the Go Collector, is that, in this more complex scenario, you might have a different auth extension implementation that knows something about the scheme you're using.
So, in this enterprise environment, you would configure the fancy multi-tenant extension for auth, which knows to extract a specific header, like HTTP header, through configuration, and then, like, once it's extracted that header value, for example, maybe it turns that into an endpoint name for the Azure Auth… component underneath it, so it's like a virtual… auth component that looks at a header, figures out the endpoint name, and then constructs an Azure auth on the fly. That would be an extension you could implement in the Go Collector right now.
Just by providing that interface.
Laurent Querel 01:04:43 Yeah, that sounds good. So the… having, an extension mechanism or something similar to that, that is flexible enough to authorize this kind of advanced Deployment and configuration. That's… that was my, the sense of my own remark.
gokhan 01:05:02 Okay, thank you.
jmacdonald 01:05:04 All right, thank you. Well, we're over time, everybody. Thanks for hanging on. If you're still here. Some people have dropped, and I think we should, end the meeting, and thank you very much. I'll see you next time.
Laurent Querel 01:05:14 Right, thank you so much.
Albert Lockett 01:05:15 Thanks, everyone. Have a nice evening.
gokhan 01:05:17 Bye.
Tom Tan 01:05:17 Thank you.
