SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-07-08
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 00:48 Hi, Richard.
**Richard Nikula** 00:53 I'm okay.
**Ruediger Schulze (IBM)** 00:56 Antoine.
**atoulme** 00:59 Hello.
Okay.
**Ruediger Schulze (IBM)** 01:05 So…
**atoulme** 01:20 Thank you for the doc.
**Ruediger Schulze (IBM)** 01:33 Oh.
I added one agenda point for today.
**atoulme** 01:39 Okay.
**Ruediger Schulze (IBM)** 01:40 I would like to give you a preview.
on the PR for… The HMC-related content, it's not ready yet, but to give a little bit, maybe, me to… our content to look at.
And I realize, obviously, by the type of data we need to, you know, there's model and semantic conventions, and then there's generated documentation, but you can't add additional content to the documentation, to the MD files.
Obviously, this is something that we want to do to make this content more explainable.
**atoulme** 02:20 Yep.
**Ruediger Schulze (IBM)** 02:20 That's not there yet, and obviously there's also… the HMC API is quite powerful, so it's a little bit also tricky of how to do… do we do this split?
**atoulme** 02:31 Mmhm.
**Ruediger Schulze (IBM)** 02:32 Okay.
Essentially, I started to lay this out in terms of what entities are there. And then you get into this discussion, what kind of metrics you have and what kind of attributes you have. And then you get into, and this is one thing that I wanted to mention.
Let me see where this is. CPU utilization is an interesting one.
Obviously, there is system CPU utilization.
**atoulme** 03:01 Okay.
**Ruediger Schulze (IBM)** 03:03 But the mainframe has different type of processors, right?
And, Do we have this here? Yeah, I think that's here. Right. So, you can have a, you can have a.
You can have metrics that are specific to the CPU type. There's general purpose processor But there's, for instance, processors which are dedicated for Linux workload. There's processors which are used for Java, as an example, Java workloads within CUS.
There's a few more, if you think about coupling facility and so on.
And then there is also this concept of shared processors and dedicated processors.
And you get data for, you know, all combinations or all reasonable combinations.
And obviously we have system utilization as a concept in the semantic conventions.
But when we now define this utilization from a mainframe point of view.
what would we actually do? Would we use system CPU utilization and just add additional attributes like it's done here, right? But my understanding is, and that's why this question, does that then actually require that we need to define also a new metric, so, which I did here, which is mainframe host CPU utilization. And, host is… is being here the representation that's really from the physical box perspective. It's also a topic to… to discuss. Obviously, Richard… that's the CAIC utilization, or the, you know, CPU utilization at the CAIC level. Now… In the light of aligning names, I used host here. But these are the type of questions, Antoine, that we get into.
**atoulme** 05:02 Okay.
**Ruediger Schulze (IBM)** 05:03 And what I essentially want to propose as we move forward is I will take a chance to look at this, maybe comment.
I don't know.
what I would… probably do right now continue to prepare the Pr. To. You know what seems to be reasonable for a start, and then we get anyway into into the revenue, you know.
review cycle. I probably also want to ask the semantic conventions team on on those specific questions of how that should be dealt. But that's, you know, one of the questions that we had already for long. And now we need to essentially find a response to this.
**atoulme** 05:49 Alright, so… This is interesting PR, but just from a mechanical standpoint, there are some changes in there related to how you generate markdown and whatnot.
That feels like they could land first.
**Richard Nikula** 06:04 Andre, your little fate, can you?
Bring up your volume a little bit.
**atoulme** 06:09 Sure.
Let me see. Maybe I'm on the wrong mic. Hang on.
Oh yeah, that would not work, you know.
of that.
Is it better?
**Ruediger Schulze (IBM)** 06:22 Yes.
**atoulme** 06:23 Okay, so, just looking at this, right, your PR seems to have…
**Richard Nikula** 06:27 It's like a different person talking. It's like amazing. Sorry.
**atoulme** 06:32 It's better when I have the dedicated microphone. I was using my microphone, which is, like, way over there.
So, alright, so if I'm understanding correctly, your PR has multiple things that is going on at the same time, which is maybe, maybe we can land some of it already, which is anything on the templates we could land right now, because it's just mechanical changes to how you generate the YAML and whatnot, right? So… And then we would want to really take the time to review that host metric utilization, the CPU utilization, for example, and all the concepts you're pushing around HMC.
you're… you want to discuss specifically CPU utilization in mainframes, and you're asking, I think, the right question, which is why why do we care what are the use cases around that, right? Why… is this good enough? Does this help you understand utilization of your mainframe?
Or are we leaving some ambiguity that might actually create tension down the road?
Umm.
I'm sure, Richard, you would be able to review that.
This is also one map to what HMCZ API looks like, right?
**Ruediger Schulze (IBM)** 07:43 Yeah, this is actually data that you could get from the API.
But there's even a PDF for this, right? So you can go through. Richard, you will know this. There are metric groups on the HMC. And that's essentially aligning here with the metrics group expose.
This one is here for the CAIC metric group, but there are, you know, I think it's 9 or 10 metric groups, and then This is not sufficient in a way, if you want to understand the the full, you know.
let's say, There's a couple of additional configuration data, which also by the Prometheus exporter are being treated as metrics because they complete the picture for if you want to do certain calculations that are relevant for the mainframe management, LPOM management.
then you need to have this information available as well. So, the… the truth is to go with metrics groups plus this additional configuration, and essentially what's on the… on the Prometheus OSX portal today.
**atoulme** 08:54 I see. Okay.
Well!
my point of view is that if we're mapping 1.1 to existing API, then we're good. This is better than what we had before.
**Richard Nikula** 09:05 Okay.
**atoulme** 09:06 Is there a discussion to be had about the quality of this particular representation of the data?
We can have that, and if there's discussions to be had about the naming of it.
I'm going to opt out, because I think it's better… what you have now is better than before.
**Ruediger Schulze (IBM)** 09:26 Okay.
**atoulme** 09:27 Not helpful, but…
**Ruediger Schulze (IBM)** 09:29 Yeah, okay.
Yeah, so…
**atoulme** 09:31 Not an expert enough.
**Ruediger Schulze (IBM)** 09:32 So… Right. I mean, the other challenge is quite big, so maybe, like you said, right, you know, I mean, this was a template I came across while working on this thing, that somehow a template was a topic.
And tab… the template will actually go away, maybe you have heard that the, they are working on having common templates being established, and obviously we want to rely on them, and not, yeah.
having our own. So this is more the workaround.
**atoulme** 10:04 Yep, that'.
**Ruediger Schulze (IBM)** 10:05 Alright,
**atoulme** 10:08 That's cool though.
**Ruediger Schulze (IBM)** 10:09 Yeah, I know.
**atoulme** 10:10 We could add a CI check at some point that would… this is… again, sorry, I'm taking this down to really simple things, but… Your PR would add additional markdown generation.
One thing we should do is that we should just have a CI down the road where we regenerate everything and we make sure there's no changes.
So that you have a way to kind of move forward.
And check that the code generation works.
It's good.
**Ruediger Schulze (IBM)** 10:40 Yep.
**atoulme** 10:41 This is trivial stuff, but I can… I can make sure we follow up on that.
Umm.
Okay.
And HMC itself, so I remember having a discussion with Richard like two months ago about that.
Where I brought up all those rich metrics from HMC, there was a lot of stuff you could get, right? Some of it even down to the wattage of your power cord, talking to different parts of the mainframe. So again, I'm not that familiar with everything.
Are we trying to be comprehensive of everything we can do with all the HTMC API, or are we being choosy about which metrics we want to map?
**Ruediger Schulze (IBM)** 11:23 I actually wanted to lay it out for.
what is on the API, in the sense, like, I described it to the Prometheus exporter, that actually has this data that you just mentioned, so power data, obviously, is also of interest.
Because there's a… The way I always viewed it, it's kind of like the base, right? You start from the bottom, then we understand how to represent these different concepts. Okay, I agree, power chords is a very special thing, so that's… Yeah, maybe something to not be, you know, so focused on. Yeah.
But if it comes to adopter cards, they have representation also in the upper layers. So crypto adopter cards as an example. We want to start with this on the lowest layer, then we have at least a naming scheme of how they would appear.
if we go up to the operating system, figure out it doesn't work. Okay, we can change it, obviously. But my thinking was always, let's start from the bottom and then build it up to whatever the you know, operating systems or higher layers that need to represent these. Obviously you get then also in this more okay, it's than shared resources, apparently. How does that reflect in this? We will probably see a couple of these questions coming up.
**atoulme** 12:51 Let's see So… What's in the way of making this PR move out of draft?
**Ruediger Schulze (IBM)** 12:58 It's, it's, it's… I think I need another week to at least add more content, and…
**atoulme** 13:05 Well.
**Ruediger Schulze (IBM)** 13:06 I would put it into open state and everybody can look at it. Okay.
And yeah, wanted to show you this. If you have, I mean, put it into a draft of it. If if somebody has comments already now, then please feel free to add them. Otherwise we we can do that as we progress. And then… Yeah, then we have something to debate on, right, obviously.
**atoulme** 13:34 Sounds good. Sounds good.
**Ruediger Schulze (IBM)** 13:35 That's great. Thank you for that.
**atoulme** 13:37 I work.
**Ruediger Schulze (IBM)** 13:38 Yeah, and like I said, I really think we need to invest a little bit then, and it's maybe also part of the review process, to add additional data, or not data, more comments onto… to the DMD files there, and so… I think the… maybe one of the tests, Antoine, is… if, based on the… on what is written there, and what is being generated, if this makes sense… From your perspective, not coming with a mainframe background in this case is maybe the first test to validate that what we did is the right thing.
**atoulme** 14:12 I see. So we'd be able to… Yeah, test that with an existing setup, and… Yeah, yeah, that makes sense.
**Ruediger Schulze (IBM)** 14:22 Yeah, so, yeah, go ahead, go ahead.
**atoulme** 14:25 The current Prometheus exporter's metric names do not match exactly what you have here.
**Ruediger Schulze (IBM)** 14:29 No, no, they, they, let's see, we had actually an Excel file there at some point. Let me see if I can find the link here.
Okay.
**atoulme** 14:39 Oh, you have a mapping, okay.
**Ruediger Schulze (IBM)** 14:41 Yeah, it's, it's… Let's just add a spreadsheet here.
at.
Conventions.
Yeah, right? So At some point, we worked on this. It's probably not the final version that we at some point looked at. But if you look in here, there's some of this what I put actually into the PR already prepared. And you have the Prometheus exporter names.
And obviously here you have this concept for each and every processor type, you have a specific metric name that's actually, at least as I understand, semantic conventions we wouldn't do, right? We would do utilization or count and then specify this with the attribute as an example.
**atoulme** 15:29 Yep.
**Ruediger Schulze (IBM)** 15:30 Because they're.
**atoulme** 15:30 not allow you to re-aggregate if you.
**Ruediger Schulze (IBM)** 15:32 Right, right, yeah. And that's, yeah, the usage ratio, this is my utilization example that I had earlier, right? So you have to see, here you can see this, you have the processor type there, and you have the, it says shared or dedicated, which we currently refer as mode, CPU mode.
And… and that covers then already… I don't know how many of these are, maybe 20, 20-something different metrics that… that you have here.
And same then for adapter. So we probably would not introduce for each and every adapter different metric, but have the specification again with the adapter type.
And in a sense, it also comes down with the quotes, right? You just have one metric, and then you would specify these, you know, different quotes.
If you are interested in this, yeah.
**atoulme** 16:29 So maybe this is taking you into a different direction, but there's an existing Commifix exporter. It's written in Python, right?
**Ruediger Schulze (IBM)** 16:37 Yo.
**atoulme** 16:37 And it's probably using the ZHMC client written in Python.
I see you also have one written in Go.
Are both of them… is a Go client? Seems like it's less supported. It doesn't…
**Ruediger Schulze (IBM)** 16:51 Actually, I just take my perspective here. I only keep hearing about the Python one.
**atoulme** 17:00 Yep.
**Ruediger Schulze (IBM)** 17:01 If there's a go one, I was… I have to… in all honesty, I wasn't aware.
So. Doesn't mean anything.
**atoulme** 17:09 to make those changes at the point of that client, at that homing fuse exporter level.
Or even if we make that PromVis exporter now able to just also have an open telemetry.
exporter, right, of some sort, it would be written in Python.
**Ruediger Schulze (IBM)** 17:25 Yeah, that's, that's probably.
**atoulme** 17:26 Okay.
**Ruediger Schulze (IBM)** 17:27 What… what would be most reasonable? So, the… the exploitations that I'm aware of, they are the Python one, that doesn't mean anything, obviously. But yeah, that that's that's my knowledge.
**atoulme** 17:44 That's okay. So, yeah.
Yeah, because you probably… if you're doing this type of significant changes in semantics, and we should take the time to do that, we might then have some sort of a feedback for that client to say, well, the Python The problem is export is actually getting a bit in the way of.
progress here, where it should be better to just have the native OpenTelemetry stuff working the right way in the first place, and we're going to come and change the code, build separately from the Polymerase exporter, and OpenTelemetry exporter is going to use those semantics. And you can use the semantic convention that you're building right now could generate Python code.
I've done that for…
**Ruediger Schulze (IBM)** 18:30 I see. Okay. Okay. And, yeah, I've seen this. I haven't tried this myself yet. So there's this annotation, statement that you can add, obviously, to define the type. And, what tooling would you use to, to generate the Python code from an hotel perspective?
**atoulme** 18:50 So that's the funny part. You see how you've built with Jinja all those templates for Markdown. Well, you can generate Python code using Jinja too.
**Ruediger Schulze (IBM)** 18:59 I see. Okay.
**atoulme** 19:01 And that's what I've done for Java, like, for IBM MQ, I have a Weaver model, and I'm using it to generate all the definitions of all the… all the Java metric, so, you know, if it's of type sum, then we're going to generate the… the code in Java is going to look like this. If it's gauged, then it's going to look like that.
And then we just do that as a follow-up, and it's actually not that hard to put together. The biggest problem was to make sure that we're able to get the right API in place for the Java SDK, so we were able to kind of… changed a bit the way things are done, because the SDKs have opinions about the gauges and counters, and we're in a different world where we're going to emit directly data points.
**Ruediger Schulze (IBM)** 19:47 Yep.
**atoulme** 19:48 So it's So, in that case, we don't create… we don't create counters and gauges that are sitting inside the code and monitoring the execution of code. We're actually going to say, no, no, you're going to create this metric, it's going to have that name, and it's going to have the value reported by this.
**Ruediger Schulze (IBM)** 20:04 Right, right, yeah.
**atoulme** 20:05 It turns to be pretty straightforward. But yeah, we it's going to be.
It's gonna be that way. We don't have to think about it yet, we certainly do not have to do any of that today, or in the near future, but that might be a discussion to have, is to have a lib, a Python lib that is built that is just a set of types that… you can allow that, or you could also just, make it a separate Weaver task inside some Python project.
That is able to iterate over a fixed tag of your semantic conventions and say, okay.
**Ruediger Schulze (IBM)** 20:41 Yeah, okay.
**atoulme** 20:42 Everything.
**Ruediger Schulze (IBM)** 20:42 Yeah, I see. Yeah, that sounds good.
Okay, that's interesting.
Yeah, let's, let's come back to that. Once we have this, you know, PR done, then we can actually look at, how to bring these things together, right?
**atoulme** 21:01 Yeah, yeah, for sure.
**Ruediger Schulze (IBM)** 21:02 Sounds good.
**atoulme** 21:03 No worries. It's not urgent. It's not today. That's for sure.
**Ruediger Schulze (IBM)** 21:07 Okay.
**atoulme** 21:08 Okay. So yeah, it's good to have, sorry, I'm, I'm putting this together for myself. okay. I'm, I'm okay here. Yeah.
**Ruediger Schulze (IBM)** 21:16 No, no. Yeah. So this is all what I have for today. So I would essentially work down the list here to have something for review then. And.
This is a, yeah, obviously the larger list here, this will be more condensed as we, as we just spoke.
Right.
Okay.
**atoulme** 21:39 Everything making sense. Richard, you're good with this development.
**Richard Nikula** 21:45 There's too many Richards around, but yeah.
**atoulme** 21:47 Sorry. Good day.
Yep.
Okay.
All right.
**Ruediger Schulze (IBM)** 21:54 Good. If there's nothing else, I would actually say maybe we are good for today and we meet next week and look at hopefully then a more complete PR.
**atoulme** 22:05 Thank you. See you next week.
**Ruediger Schulze (IBM)** 22:07 But…
