SIG: eBPF Instrumentation
Date: 2026-11-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Aryan Bakliwal (Accuknox)** 00:28 Hello.
**Stephen Lang** 00:32 Aye.
**Giuseppe Ognibene (Coralogix)** 01:04 Hi, everyone.
**Aryan Bakliwal (Accuknox)** 01:09 Hello.
**Gregor Zeitlinger** 01:10 Hello.
**Mike Dame (Odigos)** 01:44 Hey, everyone.
**Rafael Roquetto** 01:48 Hey there.
**Gregor Zeitlinger** 02:03 Who's driving the meeting when…
**Mike Dame (Odigos)** 02:05 Yeah.
**Gregor Zeitlinger** 02:05 Apologies.
**Mike Dame (Odigos)** 02:06 I was just gonna say, we're all just gonna sit here and wait for Tyler to come back.
**Gregor Zeitlinger** 02:10 And an hour later, nothing has happened.
**Rafael Roquetto** 02:15 Is he, is he, like, on leave?
**Gregor Zeitlinger** 02:19 No, I'm just looking at the meeting notes, it says out of office.
**Rafael Roquetto** 02:22 Awesome.
**Mike Dame (Odigos)** 02:23 I think he said in Slack, too, that he was gonna miss today.
**Stephen Lang** 02:27 It's Thanksgiving tomorrow, so maybe long weekend.
**Mike Dame (Odigos)** 02:31 Yep.
**Stephen Lang** 02:40 Well, should we get started?
**Rafael Roquetto** 02:42 Yeah, you can drive it, Steven.
**Stephen Lang** 02:44 So, Gregor, you're first up on the agenda.
**Gregor Zeitlinger** 02:49 Yeah, so we have discussed, dynamic instrumentation before.
But, there was a good idea, to, make this available in main before everything lands, without, making anything unstable. And the key is, if we, add this in an experimental way, so that, both in the configuration, it's clear, that this is work in progress, and also in the, Go signatures.
Then we can ship this incrementally. Right now.
Which lives in a feature branch, which, it's… it adds some, Bookkeeping, and also it is not, tested as well, and… It has more merge conflicts accumulating over time.
Yeah, is this something that we have already established as a pattern, or do we need to discuss this in general?
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:04 Oh my god.
I don't know, like… Maybe we keep that branch of… I don't know what all was discussed. I understand that, And Tyler had an impression that maybe We didn't want to, like, be back and forth or something on certain Like, public interfaces and whatever.
When we're building this stuff out, so we keep our contract of stability.
But… I think there's ways to work around that, I just don't want that branch to drift off too much. Maybe we should take point and keep on merging main into it.
To make it not drift off, but then how rig numbers back eventually? Do we just do one big pull request, and… I don't want to double review code as well, because I'm reviewing the changes that are coming in, but then they're coming in a branch that then is going to have to go into main, and With how much review Overhead we have at the moment.
Yeah.
Bear with me.
**Gregor Zeitlinger** 05:05 Yeah, I guess…
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:06 flag, maybe under experimental folder, maybe we keep it all in package internal for now, and… Make sure we don't have any public packages, maybe there's a solution here.
Mattia?
**Gregor Zeitlinger** 05:18 I think I could work it out.
**Mattia** 05:20 Sorry. So, in my experience, Fisher Branches always ends up getting messy and unmanageable. So, I think Fischer Flaggers, Stephen suggested, is the best idea.
Maybe we can, find a way to mark this kind of features, Alpha or beta or whatever, so the config can change during development.
I think we should get in Maine as soon as possible.
**Gregor Zeitlinger** 05:50 We… we are… also have a pattern that I know from Java, but it is not Java-specific, how to mark such features, I think alpha or something like that in the declarative configuration, so we would not be making that up.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:10 Okay, let's do that then.
Let's attempt that. Let's merge your two changes back in.
In Maine, let's open a PR with whatever you have so far, and I think just be careful around public interfaces, so we don't introduce any until the work is done.
Right.
Because that's also out of our contract, not just the config options, we can easily mark them experimental, or prefix them with experimental, so that or maybe add them to the experimental, like, subcategory, but also, like, keeping our contracts on the go side to be, consistent. Just make sure it's all in package internal, or… It's not public, somehow.
**Gregor Zeitlinger** 06:54 Does it make sense to add automation around that, so that we know when this changes?
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:02 We've talked about that, yeah? I mean, because people break it all the time. We miss things on pull requests, and then usually Tyler has to fix them up later.
Okay.
**Gregor Zeitlinger** 07:12 Then I will look into that separately. So, adding that first, and then we can be more confident that we're not breaking anything accidentally.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:23 Yep.
**Gregor Zeitlinger** 07:24 Okay, cool, thanks.
**Stephen Lang** 07:28 Thanks, Crico.
Next up, Mattia, GPU device metrics. I believe there was some discussion with, Yes. Ongoing work with, with Marc as well.
**Mattia** 07:39 Yeah, so basically yesterday I opened this PR, and then I found out Marc has been working on it as well.
**Marc Tudurí** 07:45 As well.
**Mattia** 07:46 Or, bila?
So…
**Marc Tudurí** 07:50 Yeah.
**Mattia** 07:51 Yeah, we…
**Marc Tudurí** 07:51 Fundoitu.
Please.
**Mattia** 07:54 Some heckle.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:55 Marc you have echo?
**Marc Tudurí** 07:58 Yeah, it's me when I… Go ahead.
**Mattia** 08:02 Yeah, so, yeah, we need to agree if we want this feature in Hobby, and get to, like, get to an agreement regarding metric names that are not published in the semantic conventions. Because right now, I think in my branch, there are some… That are made up by Claude. And in Marc's branch, there is also some others that are made up, so we need to get to an agreement on that.
As for features, I think we can just merge both of them. The more metrics, the better.
**Marc Tudurí** 08:43 Yeah, I think you're… you're hot a few more, right?
And… But I think what I also added, it was beyond, NVIDIA, I think I… for Intel and AMD.
**Mattia** 08:57 Yes, there is also Intel, and then me, and There is, there is a difference, which I think is the one that we should discuss more. Maybe, maybe we can do this offline.
Regarding the way it attaches to NVML, because I think… So, from what Claude told me, Grafana Grafana Bila has 2, builds for that. There is one build with, Giib C, whatever.
And, my thing just starts a sub-process inside the obese memory.
So we shall discuss that.
**Marc Tudurí** 09:40 Yeah, we added…
**Mattia** 09:44 Sorry?
**Marc Tudurí** 09:49 No, I think we added, like, this, pure go, to do the linking, but Nikola, you said that… what Macias… Proposal is better, like,
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:04 I mean, it might be better, I mean, because then we don't have to create a separate bill for Muzzle and GwiC, because even with PureGo.
It still depends.
whatever we link with. I mean, we should check that. If PureGo solves that problem, then we don't have an issue, but I think we still need a Mazel Gippe.
I mean, Muzzle is really just Alpine running on Kubernetes, but… Yeah. So, I mean, I guess the main question I had is, does SIG agree that we should add this?
Does everybody want it? Any opposition to adding GPU metrics? Because my main concern was, like, we didn't even Think about this.
was because… I mean, CPU metrics were rejected when we donated the project.
Saying there's a… Sort of a conflict would be… I don't know, the collector doing this, and… Why duplicate it? But I don't know… I know the collector doesn't do GPUs, so maybe… Maybe we should do this. I'm 0-4.
I vote for, but I just want to hear if there's any opposition.
**Marc Tudurí** 11:10 Maybe we should open, like, a proposal? We already have the pull request, but, like, a GitHub issue with the proposal, and… People can decide, or vote, or whatever.
**Mike Dame (Odigos)** 11:24 One thing that I just… when you mentioned duplicate, like, just at KubeCon, I saw, like, the Inspector Gadget people gave a talk on basically doing NVML GPU metrics with eBPF through Inspector Gadgets, so…
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:39 Thanks, baby.
**Mike Dame (Odigos)** 11:39 maybe there's something to learn from there, or if that could be another point of duplication and just trying to figure out what it is that OB adds over that.
I mean, we do the, like, hotel formatting and everything in the pipeline in it, but something to think about. Maybe I can find a link to that talk.
And I'll add it into the notes here. I saw someone adding the bullet point, so I'll find it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:05 Yep.
I mean, there's plenty of these.
Yeah, there's plenty of these added. Sorry, Rory. And… I would like to say, like, from my experience, people want to use one agent. When they deploy, they don't want to install, like, five different tools, so if we're going to help this with a… especially with a collector story, you know, installing the collector with OB enabled.
you get… Instrumentation across the board. I think it's a very valuable position. Otherwise, there's plenty of projects out there. I mean, I know Inspector Judge is CFCF, but there's… outside of CNCF, people build collectors with GPU support and whatnot.
Go ahead, Roy, sorry.
**Roy Reshef (Kubex)** 12:46 Yeah, just as a reference, we open-sourced, It was before KubeCon, I believe.
this exporter that I just shared the link, I authored it. It's… it does not use eBPF. It goes… it runs as a daemon set, it goes… it has something similar to the CADS cache to be able to map, you know, process ID to which container it is.
And… it does use SeaGo.
And it just goes to the NVML driver and picks up the metrics from there. I mean, you can use it as a reference if you want, or whatever.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:25 Yeah.
This is great. I actually wanted to ask you about this, it's good that you're on this call, because I know you… you were trying to figure out how exactly to calculate GPU utilization per process. Is that in this process? In this?
Is that your secret sauce?
**Roy Reshef (Kubex)** 13:40 Well, no, what we did here, I mean, the biggest problem that you have with NVML is that NVIDIA broke pretty much every observation rule… observability rule, sorry, under the sun. Their GPU utilizations are… More of a activity signal than relay utilization.
And to start with, they provide it as percent.
I mean, like, unlike CPU utilization that you don't I mean, CAdvisor or Node Exporter, they don't give you CPU utilization as a percentage. They give you, in… You know, a counter of seconds incremented, and you compute the percentage on your own.
NVIDIA doesn't do that.
They give you a percentage, and they give you a different kind of percentage.
So, first of all, I ignored the general GPU utilization percent, because that is truly meaningless.
Yeah, I can… I even know how they calculate it. They look at a period of… A sixth of a second?
And if the container was, or if the GPU was doing something.
Even for 5 microseconds, this whole period is considered to be used, so it's useless for any practical purpose.
What I used is the… the SM utilization percent, which they provide.
The streaming multi-threaded, multi-threaded… utilization percent, which is more meaningful, but again, they provide it as a percent, so what I do, I actually… I collect it every second as a percent, and I… I multiply the percent that I get by seconds. So I create a percent second as a counter, which you can increment.
And then you have to look at the rate of this to get the real utilization percent.
There's also memory utilization percent, but this one is actually, it's… it's not the memory utilization, let's say, like, 2.5GB out of 4GB of memory, were utilized, it's… How busy was a memory controller moving bytes in or out?
So it's… it is… it's there, I collect it, it's not very useful. I mean, well, it is useful if you want to know… If writing or reading from the GPU is your bottleneck.
But it's not useful to know, hey, this workload is, you know, hogging the GPU in terms of how much memory it needs.
So, I also added there a metric of the actual memory utilization that I get from NVML, and also the percentage of that I mean, our biggest problem was that NVIDIA DCGM exporter has very bad connectivity to containers. It relies on the device plugin, which now DRA will also deprecate altogether, but even before DRA, and it doesn't deal with… cases of GPU sharing using other CAIC scheduler or HAMI Core.
He just doesn't know how to do it.
And that's the gap I was trying to bridge there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:15 So this is all in the Densify dev, or whatever?
**Roy Reshef (Kubex)** 17:19 Yeah, yeah, it's there. It's open source. I mean, you can do whatever you want with this. We… we started as a closed source, and I think back in September or October, we open sourced it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:30 Yeah, it's Apache 2.0. So this would be compatible. I mean, we should look into this and see if we can actually then combine all three.
And build something that's… that's good.
**Mattia** 17:44 Yeah, thanks, Roy.
**Roy Reshef (Kubex)** 17:46 No promo. But again, this is totally without eBPF. This is just…
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:49 Yeah, yeah, yeah, no, there's going to be FNR implementation.
**Mattia** 17:52 Yeah, mine as well. It's, it's just NVML.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:56 And it works nicely with our CUDA metrics, which means maybe we should be extending this to RockM or Vulkan, or any of the other ones that we can find. And that… the CUDA metrics with the GPU metrics go really well together.
for observability. They provide real insights as to what was happening, so… Yes?
I would say let's do it. If people are, like, seeing excitement around this, I think it's a good idea. Otherwise, we wouldn't have added it in Below.
I mean?
And thanks, Mike, for pointing out the inspector gadget.
I mean, let's look into that as well, see if it's any different than ours.
Maybe we can borrow some ideas.
Yeah.
I'll save all of this.
**Mattia** 18:43 links, and I will copy ideas from everyone.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:47 Mark, are you okay with working with Mattia to merge our changes upstream?
**Marc Tudurí** 18:50 Is that true? Yeah. If there's an agreement, then no.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:54 Yeah, we added AMD and Intel, I know they're not important, but… I've also had requests from customers, the TPU from Google, That seems another can of worms. It's available through APIs.
I don't know, if you're on Kubernetes, there's a specific port, apparently, you can hit on the node, and they give you the metrics. There's also the library Google provides, I don't know which one's better.
But it must be installed, and it's not always installed.
I don't know.
Seems a little bit harder than this.
But… Yeah.
**Stephen Lang** 19:37 Mattia, Marc, can I suggest that you maybe create an issue in the OB repo, just to, maybe bring some of this discussion and… Document any decisions that are made.
**Mattia** 19:48 Yep.
Oh, dude.
**Roy Reshef (Kubex)** 19:52 And Mattia, if you want any… any reference to… if you have any question about this repo, just reach out directly to me. I mean… I pretty much offered it, so I know roughly what it is doing.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:09 Roy, thank you so much. Will you be okay with reviewing some of this code? I can ping you directly?
**Roy Reshef (Kubex)** 20:15 Yeah, it's all a matter of availability, you know, I did not contribute to OB yet, just because I'm so swamped with tons of other things, but yeah, I will be glad to do some review here, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:32 Thank you.
**Roy Reshef (Kubex)** 20:33 No problem.
**Stephen Lang** 20:39 Alright, Mattia, you have the next one as well, around, release.
1.1.0.
**Mattia** 20:47 Oh, yes, I wanted to ask if we are ready to… Kick off the next release.
I checked in the GitHub milestone tags. There's only one PR, I think.
mine.
**Gregor Zeitlinger** 21:05 I have one thing, just… I realize, forgot to put it on the agenda.
This is a PR that, needs to go in. Let me just open it.
Sorry that I forgot… got it before.
**Mattia** 21:24 No problem. If you passed it in the chat, I can add the tag for the release.
**Gregor Zeitlinger** 21:31 Yep.
Yep, let me do that.
I edited.
We discussed it, in a, private chat.
**Mattia** 21:51 Yep, yeah, yeah.
**Gregor Zeitlinger** 21:54 And since this is recorded, we'll leave it at that, I guess.
**Mattia** 21:59 Sure.
Okay, I think it's two PRs now. I think we can, Oh, if Tyler is not… Tyler, I think, has requested some changes, and I think his review needs to be… dismissed.
For Mattia to be nursed? Yeah. Not sure we can do that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:21 Yeah, I think we can. I mean, if you've addressed these comments, and… I mean, we need a router maintainer to approve. I approved already.
I mean, if there's anything that's missing, we can fix it later. That's not a… I mean, his last comment was just, small change that you have to make, I think that's addressed, so…
**Mattia** 22:45 Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:46 I think we can… we can do that, and just, another reviewer, approver, Please?
So that… We have another green checkmark, and… That should be good to go.
**Mattia** 23:02 Yeah, I will try to get both PRs merged by tomorrow then, and I will start the release process. If anyone else has some other PRs that, wants in before 110, Just ping me.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:18 Yeah, okay. I'll approve yours, Gregor, I think I know… That one's about, so… Yeah.
**Gregor Zeitlinger** 23:29 Okay, thank you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:31 Yeah, so one more maintainer, please. Can you look at Mattia's? Mattia, do you want to post that, if people are not aware?
the CP start job trace from Redis?
So… Yeah.
**Mattia** 23:49 Oh, I was muted.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:50 Oh, yeah. Oh, it's in the chat, okay.
One more, approver, please.
We should be good to go.
**Stephen Lang** 24:05 Gregor, the PR that you posted, does that need to be tracked as the 1.1 milestone?
**Gregor Zeitlinger** 24:14 Yep, let me add that.
**Mattia** 24:21 I think I already did.
**Gregor Zeitlinger** 24:23 It already is, yep.
**Stephen Lang** 24:30 Alright, Giuseppe, you're next up.
**Giuseppe Ognibene (Coralogix)** 24:35 Yeah. So, I just want to point out that I opened a discussion about, OBCLI and OPAM.
If you miss it, please take a look. I think we should decide all together what to do.
So, that's all.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:00 Is this gonna be a problem with building the collector?
**Giuseppe Ognibene (Coralogix)** 25:07 Sorry.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:08 TLDR? Sorry, what's the TLDR? Sorry, I haven't… I don't know if I missed that.
**Giuseppe Ognibene (Coralogix)** 25:14 I can send.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:20 Oh, you're just wanting, reviews here, right? Yeah, okay.
**Giuseppe Ognibene (Coralogix)** 25:29 Come on.
this one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:33 I'll review. Thank you.
**Giuseppe Ognibene (Coralogix)** 25:43 That's all.
**Stephen Lang** 25:45 All right, cool. Please take a look for, the RFC.
And looks like you have a shared discussion, Nikola, as well.
Rust.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:55 Yeah, I just wanted to bring it up that, please watch out, so Pino and I will try to get, Rust support in. To some extent, I think we had a chat this morning, maybe it won't be full support, not 100%, because there's lots of gotchas.
Mainlining differences, symbols missing, various libraries being used, but we hope to get closer to, While we have it go?
Now, while working on this, I discovered some interesting things, some gotchas that I wasn't expecting. For example, So, maybe… add a… inject a header for, say, for Go.
The memory's always available to BPF because it's… manage GoHeap.
But when you do it with Rust, I mean, if the pages are loaded, the BPF cannot actually load it.
So, Usually, it's not a problem. It's just the first request we cannot inject, but then later on, the page gets touched eventually by, by Rust, and memory gets loaded into process memory, so things work. But we'll have various degrees of success, it won't be a clear cut. We do support this.
We just have to be conscious that, there might be many, many improvements we can do over the next period of time.
But yeah.
Just wanted to bring it up.
Hopefully, with many people moving to Rust for performance reasons, it seems to be the trend, with agents being able to spew out code overnight and rewrite people's services.
Apparently there's talk about rewriting Prometheus in Rust.
I mean, Google, I think, wants to make that happen.
And, I think the memory usage is 10 times less, and CPU improved.
Two, or three times, so… Maybe.
**Roy Reshef (Kubex)** 27:57 Yeah, I brought it up in the last, meeting. You are not, you're not there. I also saw the… I mean… I wasn't a KubeCon, but I got a… The hype, or the… the trend, from there.
Tyler reacted, he was a bit, defensive about it, he said that he's not sure that all of these memory savings are from Rust.
And he attributed a lot of them for using, what's his name? Arrow, the columnar, Data store, so that may be the case, but… Yeah, there is a talk, there is already a Slack channel to Rustify Prometheus.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:43 Yeah, yeah, I know. I'm actually gonna give you an example. I have a friend who works on this, whatever.
startup, he's got his camera system, whatever.
And most of the… the stuff he's doing is just math, 3D math, and all this, and the application is written in .NET.
And over the years, as .NET Core has progressed, improvement has been massive, so sometimes he would just… I think his biggest upgrade was maybe .NET Core 5. He has just got 20% boost without doing anything, just compiler and garbage collector got better. And then he asked Claude to wipe code rewrite this in Rust, and… Went 5 times faster.
Just like that. I mean, he doesn't know what to do with his code now, because he cannot maintain the Rust, he doesn't know any Rust. He's a .NET developer, but .NET has a pretty decent runtime. I mean, compared to Go, I think it's better. The compiler and the garbage collector are… more advanced. So, I believe the hype.
**Roy Reshef (Kubex)** 29:52 Yeah, well, I can tell you, we tried too. We took that same GPU exporter that I sent you, and it wasn't even overnight, a couple of hours, My boss has access through CNCF to Cloud Ultimate, so that gives you quite a bit of tokens. So, he just converted it to Rust. We have a branch server where this thing is in Rust now. Again, we have a bit of an… Well, it… the thing is that what I do have… I even have a GPU-kind cluster at my feet, but these are toy GPUs.
So, you know, there's a limit to what I can render, and I… it's not really tested in production environment, where you have massive GPUs, and you have GPU sharing, and between, you know, multiple workloads. So, yes, it is better, but what is better? It's not factor 10, it's maybe… factor 2, or less than this, but it's… it's not an indication. You need a real… production environment with, you know, expensive GPUs to test it, so… At least for this one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:06 Well, I mean, here's… here's what I've been… thinking about, like, one of the biggest bottlenecks we have in OBI right now is the pipeline that processes the events from eBPF. We do a lot of processing there. We have all these protocols we recognize, and there's… and we've made attempts to improve that, performance of that, but if you took anything like the… Payload extraction and all that stuff, that's a lot of manipulation, and if you have high volume of requests, that just suffers. And you hog up the pipeline for the eBPF side, and all of a sudden, you have two choices, either start dropping events, or start growing memory, which we choose to drop events. And it's not great.
If we can rewrite it in Rust, it's much more performant, that gives us a lot more opportunity.
Maybe we can just rewrite that part. I mean, I'm not saying this easily, but maybe we should first look and optimize this. Maybe with Go Memory Arenas, we can shave some of that garbage allocation cost.
But the GOGC is just not up to this task.
In my opinion, for the volume of…
**Rafael Roquetto** 32:15 There is… there's a matter of philosophy as well. Like, I think a language like Rust and C++, there's a bunch of, like, you pay for what you use for, you know, zero allocations, and I think this is not the focus of most of, you know, the goal sphere, especially, like, for system programming, so… I think a lot of the pipeline That we do now, that… could have been, or could be rewritten.
Could, rewritten it in big quotes, because this is, like, you're saying.
a very difficult test, I'm not saying it's trivial, maybe we'll, you know, I'm not saying it would succeed, but in theory, it could be rewritten to, like, I would love to see very little memory locations, zero-cost copying, you know, like, move semantics that, you know, you get for free.
In Rust, what do you call it? They borrow, borrowing, they call it. So, which, in a language like Go, it's not as natural, or sometimes not even possible, to kind of… A craft like that.
**Roy Reshef (Kubex)** 33:20 But And what you can also do, going back to Tyler's comment, is even in Go, you can check the impact of moving to a columnar approach. I do not know if it's relevant for the pipeline, Nikola, I do not know the pipeline very well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:34 No, I mean, we can… we can definitely pay more attention there in that code and see if we can actually speed things up.
But… I mean, we did a lot of work, I… I think, to improve it. We did have a bug report. Somebody said we moved to a new version of Vela, and all of a sudden.
we see half the events, and what I found out was that, yeah, just pipeline couldn't keep up. So I worked to improve a lot of the, kind of, quick checks to discard a protocol. It's really not that, it's really not that.
But… yeah, when it comes to payload extraction, it's just, It's another can of worms, then, and it just gets really slow.
But maybe we can do something… better in the GO side.
First attempt at, and if we really can't push the… boundary higher and make it better, then we maybe consider rewriting some parts, not everything, but just very specific things, especially if you have the ability to now as we're talking about touching LLP, sorry, NVIDIA NMVL, whatever it's called.
So we'll call these C codes, so that's just equivalent. We could… Somehow make this happen.
**Rafael Roquetto** 34:56 just for the record, like, the same discussion happened, mostly firmly in Tetragon as well, because Tetragon needs to run in some really constrained environments, like, really low memory.
And someone even floated the idea of rewriting C++ in this case. It wasn't me.
So yeah, it is, I guess what I'm trying to say, it is… It is an issue that is recurrent, across projects. And it was in the same… in the same kind of pipeline, you know, theBPF event delivery.
Still… it's the same as Olbi, you know, like, same kind of issues, and it's not easy to… To fix, but obviously, rewriting these should be the last resort.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:42 Yeah, and then who's going to maintain it, and we all need to learn Rust, and it becomes, Otherwise, we're… if agents just do this, then… When they mess up, we don't know how to… what to do.
**Rafael Roquetto** 35:56 Yeah, I think this is one of the reasons why Isovent just released this, Shirudo thing, and they wrote it in C. I think this was one of the reasons, but I'm just speculating, yeah.
**Gregor Zeitlinger** 36:09 Yeah, just wanted to add… that, rewriting parts of an application in Rust, when you come from Go is, is very difficult. I read about a lot of projects that tried to do that, and it got very difficult, because there is no natural way how Those two languages communicate.
I don't recall all the details, but it was very difficult.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:37 Yeah. No, you have to be Sego, some sort of… calling conventions for that, but I think, fortunately for us, I think Maybe the saving grace is that for a lot of these parsers, all we need is the buffers, so if we supply the buffers, then have something that can easily produce you back a span, I don't think it's that big of a deal to keep them separate.
But I don't know.
Yeah.
**Gregor Zeitlinger** 37:03 Yeah, we could definitely try it out.
**Stephen Lang** 37:10 Alright.
Next up is Rafael with Tabs vs. Spaces.
**Rafael Roquetto** 37:15 Yes.
Yeah, so, actually, it's just, I wanted to… since I got Mattia in the call, I just wanted to… thought it was easier to talk to him about these, this PR.
It is… So, if you are about… people parsing JSON, basically, to sanitize text.
Mattia, I saw your… your benchmarks, and I kinda… I agree with you, like, it would be… It would be better if we don't have to write this mentally, this scanner. I don't particularly think the scanners do… complicated, but less is more in this case, in terms of code. So I was just wondering, like, I'm a bit ambivalent about this, not sure how to go about this, like, do we ask the contributor then to rewrite, or do you have a branch that we could, kind of… I could do and profile it more, if you think, or… What are your thoughts?
**Mattia** 38:12 I have the patch. I could just put the patch in the comment, but I think it's better to give authors a chance to do that themselves.
**Rafael Roquetto** 38:25 Okay, all right. And do you know, like, I'm not too familiar with Elastic, like, I was trying to find out with AI, for the, like, base, optimal case and base case, like, average case, when you have, like, I don't know, 1KB of Things flowing through.
the difference is very little. Like, like your benchmark said, like, there is… I mean, there's more locations and everything, but it doesn't really… For the average case, it doesn't really make a lot of difference in the grand scheme of things.
In terms of CPU. It only starts becoming a problem when you have, like, really huge payloads, like 64 kilobytes.
Then it becomes something, like, to worry. Do you know if this is… If this… this is something that happens in real life, like, to the point that we should…
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:16 Oh, yeah.
**Rafael Roquetto** 39:17 pay attention.
**Mattia** 39:17 I have no clue.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:19 Oh, yeah.
**Rafael Roquetto** 39:20 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:21 I mean, it depends how much payload we can capture, but… Elasticsearch people do all sorts of things.
I mean, if you're looking at the… Response from Elastic.
That… That is a different ballgame, because then people put logs in Elasticsearch, so yeah, you can get a lot of data back.
In terms of requests going forward, there's, like, the bulk insert API, so that's going to be massive.
So, it depends how much we capture from the eBPF side of that request, and see how much we can parse and sanitize.
But the limit will be the eBP aside, but the request will be large. There will be plenty of large requests for the last thing.
**Rafael Roquetto** 40:08 Because, like, quick simulation, very, like, freaking dirty simulation, so take this with a block of salt, that I did it for, like, thousand requests, with 64KB payloads, then it does increase the CPU by 1.9%, additionally. So… I mean… That's why I'm… I don't know what to do with this, personally. I'm ambivalent, because I see Mattia's point, and I agree with it, like, if we don't have to write code that is already there, it's better.
But on the other side, there is the performance, which I don't know, the theory is one thing, you have practice, it doesn't really matter that much, so… Yeah, that's, I'm on the wall, on the fence here.
**Mattia** 40:47 My thinking process is, if this is already implemented in the standard library, it's because they handle edge cases that the AI or the author might not have seen, and I think it's just safer to use the standard library.
Even if it's a little bit slower.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:09 But would the Steiner Library be able to decode the partial payload and sanitize it?
Because… I guess the partial payloads are the biggest challenge, because if the payload is large, like somebody did a bulk insert in Elasticsearch in one big giant post request, or patch, whatever it was.
Anyway, we won't be able to parse it with the standard.
Jason.
Oh, we have a…
**Mattia** 41:38 Truncated the test case.
Which is 6 times slower.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:48 So, I don't know if this thing is actually better at… handling cases like that. Maybe that's one of the advantages?
Yeah.
**Mattia** 41:56 I guess so.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:58 Because if you set a low… like, imagining people would set 64K for the payload extraction, but maybe… Many will not, and they'll do 4K, so then most requests will be truncated.
So, then the question is, can this handle truncated? And if it does, how well does it handle that case compared to the baseline?
Because that's the name of the game. Like, it's easy to… Kind of handled a simple case, but…
**Stephen Lang** 42:29 Nikola, on the truncation, do you think the new streaming support in Go might be able to handle that? Because it's going to be… Just, pausing, like, Partial payloads by its nature, presumably.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:42 So this, is this what Mattia put in here, the experiment, Go ExperimentJSONV2? Is that the one, or…
**Stephen Lang** 42:50 I don't know if, Mattia, if you use the new… Features in Go 1.27.
The link that I posted in the chat.
**Mattia** 42:58 So this one, I will, proceed to the one.
The test on the right uses JSON V2.
**Stephen Lang** 43:07 Okay, yeah, cool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:08 JSOv2, so I should push them towards JSO v2 if that's able to handle the truncation well, then I would just…
**Rafael Roquetto** 43:15 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:15 make sure.
**Mattia** 43:16 No, it's actually… the truncation is actually slower than the JSON valid of the V1.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:22 Oh, God.
**Mattia** 43:22 two times slower.
**Rafael Roquetto** 43:26 Yeah, absolutely.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:27 Wow.
**Rafael Roquetto** 43:27 400… 419 nanoseconds. The thing is, the truncated… one caveat here, the truncated on the… this PR column.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:36 Which is the…
**Rafael Roquetto** 43:37 scanner is ZRA locked? Because when it sees an invalid, it just discards it, so it's not.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:42 Providence.
But that is a blocker. In my opinion, that's a blocker, because, I mean, most will be truncated. I'm sorry to say that, but… Depending on the customers, yeah.
**Rafael Roquetto** 43:55 I think, I think that's a, that kind of settles it.
In, in that sense.
**Mattia** 44:01 You mean the standard library is dropping it, or the customer.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:05 No, he's luck.
**Mattia** 44:05 He goes…
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:06 His library is dropping.
**Mattia** 44:07 Because I see zero outlooks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:09 Yeah, it's because… Yeah, because as soon as it's truncated, it just, Yeah.
**Rafael Roquetto** 44:19 Let me, let's, look, let's do it like this, if you guys agree. Like, I think this is a blocker, I agree, then, if this wasn't a blocker, like, but I think it would complicate things, but I don't know, I'll think a little bit about it, but maybe I agree with JSON valid.
Maybe this is a good compromise, as same Mattia.
I don't know, the JSON text is lower.
maybe there's something we can tweak, I don't know, I don't know these libraries very well, like, I think it warrants… Like, I don't think we should merge the PR as is, then, and I think it works a little bit more, like… research, I can… I can help you with that. What do you guys think?
**Mattia** 45:11 Also, keep in mind that the JSON text one can't be merged as well, because we need to build with GoExperiment, we are putting some new code into the JSON part, which is not ideal.
I would either go with this author one, if it's able to handle truncated, or with the JSON valid.
If you…
**Rafael Roquetto** 45:36 Okay, so which one would you go? Like, the JSON text? No.
**Mattia** 45:39 No, first or second. If the first, like, my preference is the second, because I think the… Performance impact is not that bigger.
if the first one is also able to handle truncated payloads, then we should evaluate it.
**Rafael Roquetto** 46:01 Okay, okay, no, I think that makes sense. I think, obviously, you should be able to… We can make it handle truncated, but at which cost, I don't know. Probably it's too much complexity, I'm guessing. Maybe not. That's what I'm… I'll try to find out. If it's something simpler.
or trivial, which I doubt it, then maybe we can consider it. Otherwise, I think… Yeah, JSON vetted is the way to go, as well. And even if… even if it's simpler, maybe Jason White is still the way to go. So,
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:31 Yeah.
**Rafael Roquetto** 46:33 I personally need to digest this a bit, but I don't have strong opinions, that's why I brought this.
I think you got really valid, like, valid points there, Mattia.
Alright, yeah.
I'll think about it a bit, and see why the offer responds as well, and then we don't merge the PR yet, then.
Thanks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:01 Cool.
I think we have a little bit more time. I think there's a pull request to right-size the net tolling from 16MB to 1MB. Do we think that's… gonna work? I mean… Do we need only 1MB for the ring buffer?
**Rafael Roquetto** 47:22 Sorry, which pull request?
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:23 There's a Polish voice by, david Ashport?
**Rafael Roquetto** 47:27 it?
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:27 Yeah, I just.
**Mike Dame (Odigos)** 47:29 I was just looking at that. I mean, it seems like it, Like, with the scaling factor that we have, it sounds like you can… Request more if you want, but… Yeah, he had kind of a history on it that it seems like it came from, like, a pre-bayla decision that's kind of just been carried over, and it sounds like it's not really…
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:51 they're gonna be.
**Mike Dame (Odigos)** 47:52 that big by default anymore.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:54 Okay, okay.
**Mike Dame (Odigos)** 47:55 That seems pretty sound… like, the scaling is what was, like.
I thought, okay, sure, if you can change that, then yeah, you'll be able to see that you're dropping things, and you can turn it up if you want, but… I think it's, like, it supports, like, 10,000… In-flight requests.
I mean, at some places, that's not a lot, but I think for most, that's probably… Okay. Sufficient.
**Mattia** 48:17 I think we have some constant somewhere that, That has, like, 30K maximum requests, or something like that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:27 Yeah, okay. That's usually what we do with 30K, but, I mean, if we wanted 10K… Network requests.
Maybe that's…
**Mattia** 48:41 I think maybe it's safer to put it to 4MB?
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:46 And the…
**Mattia** 48:46 16 to 1 directly.
**Rafael Roquetto** 48:51 I mean, this ring buffer is only used as a fallback path. Oh, right? Oh, okay. So… so this is… if I… so… the net only drains… drains the map, and if you cannot, for instance, because there are some issues, sometimes you cannot insert on the map, use a fallback path. I think… I mean, I think reasonable, but the only… the way to find out is, like, to kind of, stress test it, like, maybe it's not, maybe it is, so…
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:18 No, you're reasonable. It's probably… it probably was copypasta from… From the application observability ring buffer size, yeah.
Okay.
**Mike Dame (Odigos)** 49:28 It looked like we have this, like, in-kernel aggregation now, too. I don't know what that is, but it sounded like that kind of handled a lot of it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:36 Yeah, yeah, yeah.
Okay, cool.
**Rafael Roquetto** 49:38 And I got a PR on draft that Mario already reviewed, but I'd like to kind of stress test it. That simplifies this a lot, in terms of maps.
For NetOly, that I started on the KubeCon Contributor Fest.
So, I can maybe… next week, I can maybe have a look, if this can wait, but I think… otherwise, I would say, like, I think 1MB would be fine, and if… It's not good engineering, but if people start complaining about it, we can always increase it or make it configurable.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:15 Sounds good.
**Rafael Roquetto** 50:16 In the… yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:17 Yeah, sounds good. Okay, let's do that.
**Stephen Lang** 50:24 Alright, cool. Has anybody got anything else they'd like to add to the agenda, or discuss to bring up?
**Rafael Roquetto** 50:33 There was another PR from David, that he was pruning… I haven't looked into it this morning yet. He was pruning, the… let me find the PR, hold on, it's easier than me,
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:47 Out of that, I wanted to ask Fostum, anybody going?
I'm… I am gone. I just wanted to.
**Mattia** 50:56 Awesome.
**Rafael Roquetto** 50:57 notes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:57 Yeah.
**Mattia** 50:58 Probably, I'm going, yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:00 So…
**Marc Tudurí** 51:01 so…
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:02 They talk proposals, and… in… And for the, observability track, December 2nd, so… Blog enrichment, maybe?
**Mattia** 51:14 Maybe, let's see.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:17 I think that's pretty cool. It's, like, the right kind of audience. The people will really enjoy that.
**Mattia** 51:25 I can try, I can try.
I think about…
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:28 Tino and I are submitting about Rust, even though we haven't done the work, but we're gonna try.
There's also the Hotel Unplugged happening right after. I know some of you went last year.
It's again on the Monday right after.
**Rafael Roquetto** 51:46 Toye, sorry.
The… he…
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:50 You're looking at UPI?
**Rafael Roquetto** 51:51 He's the right official, I'll have a look. Okay, cool, nevermind.
For Fosden?
Me and Nikola also submitted your thoughts, on eBPF, about Obi.
When we… when are we gonna hear back?
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:09 Who knows?
Who knows? That's somewhere in December, so…
**Rafael Roquetto** 52:13 Somewhere in December, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:16 There's also language tracks. I mean, we do a lot of coverage for various languages, so… Maybe.
That's another option.
Go. There's GoTrack.
Nice.
Rust.
I don't know if there's rest this year.
That's also an option. I don't know if they're open still.
very… has different deadline.
**Giuseppe Ognibene (Coralogix)** 52:44 Did you submit something for a maintenance truck at Cubicon Europe?
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:49 No.
**Giuseppe Ognibene (Coralogix)** 52:52 I think it's the only one that's still open.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:55 Still open for Coop County Room?
**Giuseppe Ognibene (Coralogix)** 52:59 Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:01 That's a good one? Another one good one.
**Stephen Lang** 53:12 Alright, if there's nothing else, sounds like we're done.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:16 Sounds good.
**Rafael Roquetto** 53:18 Alright. Thanks, guys. See you later.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:20 They are.
**Marc Tudurí** 53:20 Yeah, bye. Bye-bye.
**Roy Reshef (Kubex)** 53:24 Cheers.
