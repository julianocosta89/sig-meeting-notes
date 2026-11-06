SIG: FaaS WG
Date: 2026-11-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Benson (Mainwave)** 01:07 Hello, hello.
**James Thompson** 01:09 Hello.
**Tyler Benson (Mainwave)** 01:13 How are things going?
**James Thompson** 01:15 Yeah, alright.
**Tyler Benson (Mainwave)** 01:17 Thanks for, staying up late for us.
**James Thompson** 01:20 That's fine.
**Tyler Benson (Mainwave)** 02:20 I'm trying to look at those PRs that you asked for real quick.
See if we have anyone else joining.
**James Thompson** 02:30 Yeah.
**SÖ Serkan Özal** 02:31 Hello.
Hello, Tyler. Hello, James.
**James Thompson** 02:35 Bye.
**Tyler Benson (Mainwave)** 02:36 Hey, Serkan.
**SÖ Serkan Özal** 02:38 Hi, how are you guys?
**Tyler Benson (Mainwave)** 02:39 Good evening.
**SÖ Serkan Özal** 02:41 Yeah.
Morning for you, right?
**Tyler Benson (Mainwave)** 02:45 Yep. Morning for me. I'm, 11 o'clock Eastern.
**James Thompson** 02:51 Yeah. And morning, technically, for me.
**Tyler Benson (Mainwave)** 02:55 Yeah, James is up late for us.
So, besides the, the stabilization stuff that James is working on, Serkan, do you have anything you wanted to talk about today?
**SÖ Serkan Özal** 03:16 Not for me, I mean, I just… checking TPRs for the cementing conventions from James. That seems okay, but no topic other than that.
**Tyler Benson (Mainwave)** 03:31 Okay?
So, James, you've been doing a lot of work for us, you've been doing a great job, Do you want to just run through what, what you… any… is there anything you want to talk about? I… I guess we can just give the floor to you and, let you run this show.
**James Thompson** 03:53 Yeah, so probably the main thing that I'm interested in is having a look at the project proposal.
Alright, which I sent the link to.
Right, so that way it's easier for us to progress through the stabilization of the conventions.
Because a lot of those conventions have been around for 6 years, and… Nothing's progressed.
**Tyler Benson (Mainwave)** 04:19 Yes.
**James Thompson** 04:21 Right, so…
**Tyler Benson (Mainwave)** 04:22 Do you want to share your screen, and you can just walk us through it?
**James Thompson** 04:25 Yeah, I'm on my iPad, because I didn't want to be on a computer this late.
**Tyler Benson (Mainwave)** 04:30 Yes, okay.
**James Thompson** 04:31 Give me a second…
**Tyler Benson (Mainwave)** 04:32 Right?
**James Thompson** 04:33 I'll just open it up.
Chair… Screen.
I'm…
**Tyler Benson (Mainwave)** 04:58 Great, I see it.
**James Thompson** 05:00 Okay… Now… And… let me switch to… Yeah.
So, what I've done is seek to describe the key things that… and… For me, I'd much rather have it in small.
stages for us, rather than trying to model things on the go.
Okay.
So, what I have broken down into these three stages. So, stage one.
Focusing on the review of existing conventions.
Alright, and then looking at what is not following naming conventions now, right? And getting those updated sooner rather than later.
Okay.
Then, we'll need a discussion around defining event sheets, right?
We… my idea being, we have one entity to describe what is being run, right? So that's the function name, version, etc.
And a separate one to describe where it's being run. This is similar to what the CICD conventions do, for example, okay?
And as part of this stage would be the promotion of the attributes from development to alpha Beta. So if something's recently been renamed, we can bump it to Alpha.
Right, and… but if something's been long-standing, like 6 years, for example, and not the case of a lot of them, we can bump it to beta, so that way, if you look at the conventions, you can see this is already beta, right?
And that way, it also provides us an indicator of what's been reviewed.
Okay?
And obviously, we want to look at the span definitions, right? And I've put a focus on… HTTP requests, and the messaging one, so PubSub. I think that they're the two key ones for the definitions at the first stage to focus on, because as we can see, if we looked at the OpenTelemetry website.
The specification for the fa… the… FaaS conventions are a lot smaller compared to the HTTP. There's a little comment that says.
Alright, it extends the HTTP, but that extension hasn't been documented in the YAML. So, looking at defining those extensions.
Okay.
One thing I have done is I put metric changes out of scope for Stage 1.
Reason for that is, I… My feeling is, looking at it, the metrics will need a lot more Review, comparing what the provider's already doing.
Right? And there's likely to be more significant changes to this, so I'd rather keep it… small and scoped on stage one.
Okay.
And then… and then after… once we've completed those, then move on to Stage 2, which is where we do that metric review, because looking at the metrics as they stand now, we… we can… Likely consolidate down the metrics.
Right? So we have a… a metric that counts the… how many times a… Function is called, alright, and then have an attribute to indicate whether that function call was a cold start or not, rather than having a separate cold start metric.
Okay.
And once we have done that, obviously making sure we can align the collector, receivers, scrapers to it.
And promote the entities.
Okay.
Yeah.
**Tyler Benson (Mainwave)** 08:43 Yeah, it makes sense.
**James Thompson** 08:46 Right? And then stage 3, stabilizing conventions.
Right? Once we've fully confirmed the viability of them, we've gone through updating the convention… more and more of the instrumentations. We haven't run into scenarios that we haven't catered for.
Right.
But one of the big things is I put cron and event-driven, i.e. file changes, spans, out of scope.
Right, because when I look at it, those scenarios are quite different to the HTTP, because HTTP, you have A clear parent span of what's initiating it.
Alright, so you have a HTTP client coming in, and that initiates it. Whereas, if you're looking at a cron task.
What do you have to initiate it?
Right? And… For example, a file change.
That needs more work, and… Ideally, the way I see it, it's almost like it's a workflow.
This… this file has changed, it triggers this.
And this flows on from it.
Right, so… I'd like to leave that… those two scenarios separate, and then follow up after we've stabilized the core conventions.
**Tyler Benson (Mainwave)** 10:03 Yeah, that's reasonable. I think, the… those are not as common as the, the HTTP-triggered lambdas, or, spans.
**James Thompson** 10:16 Yeah, yeah, and like, those conventions for the Cronin event will still have would eventually end up with the same attributes, but the span themselves won't be classified as stable.
Right? So that we can go through and make changes to it if we need.
Right, because at the moment, like, we've got FaaS. document.
Right? But when you see FaZUP document, you don't realize it's supposed to be describing the document that that was changed to initiate the Task, for example.
Right. Yeah.
Okay.
And obviously, looking for people's names to put down. I've gone through and looked at all the different components across the repositories of OTAL, and just tag all the different component owners to see if I can get input from any of them.
Right? But obviously, needing people's names to put down feedback on things, it's… That should be made more clear, and stuff like that.
**Tyler Benson (Mainwave)** 11:25 Great.
Are there any, changes that you're going through, or is it just basically formalizing everything that's existing. You're not proposing any changes, are you?
**James Thompson** 11:41 Like, there'll be summary names?
Alright?
**Tyler Benson (Mainwave)** 11:45 Okay. Alright.
**James Thompson** 11:46 Alright? Like…
**Tyler Benson (Mainwave)** 11:47 You want to talk about any of those right now, or should we just read those offline?
**James Thompson** 11:52 I've, like, One example is… Right?
changing FaaS. instance attribute name to FaaS. instance.id to follow the convention.
**Tyler Benson (Mainwave)** 12:07 Yeah.
**James Thompson** 12:07 Right?
**Tyler Benson (Mainwave)** 12:08 You're not sharing your screen anymore, just in case you were…
**James Thompson** 12:12 Did it stop? Is, or did it stop?
Yeah.
But…
**Tyler Benson (Mainwave)** 12:22 But, okay, yeah, that… I don't think I have a problem with that, as long as that follows the, conventions better.
**James Thompson** 12:32 Yeah.
Excellent.
**Tyler Benson (Mainwave)** 12:39 I'm a little rusty on a lot of those, existing conventions, to be honest.
**James Thompson** 12:44 Yeah.
And, yeah, I'll… Yes, the sharing screen from the iPad's not the best experience.
**Tyler Benson (Mainwave)** 12:53 It's all good.
**James Thompson** 12:56 Yep.
Yeah, like, I, I think, I think the main… attribute naming that… that warrants some thought discussion is… Currently, we have FaaS. dot trigger.
Alright.
In Elastic, it was FaZ.trigger.type.
Alright.
I'm proposing to change it to FaaS.invoction.initiator, because what we have… Let me… Give me a second, let me get up the current conventions.
GitHome… Smooth.
convention… And… what I want dogs.
Registration… I'll turn… She is gone.
Oop.
Come on… Yeah.
So, here's the attributes we currently have.
Right?
So… what I'm… thinking, right, and proposing, is changing this FaaS. trigger Right, to FaaS.inbroxion.initiator, right? So that way.
It nicely complements the ID for the invouction, the start time, And… So, if it's a cold start, so we have a clear object of an invouction, with different properties describing, is it a cold start, what's the ID of it, what initiated it?
**Tyler Benson (Mainwave)** 15:00 Okay.
**James Thompson** 15:02 Cause… yeah.
Because otherwise, if we want to mirror Elastic, it becomes FaZ.triggerType.
Right?
So, but… Fazed up trigger type.
has a convention of using the term PubSub, whereas OTEL uses messaging to describe messaging.
So I'd rather align to the OTel than the elastic values, so I think having it as the initiator.
Makes it nicer.
And at the same time, when we eventually look at the cron, those event scenarios, we can have a trigger there that describes it. What's the trigger? Was it a file change?
Stuff like that.
Right, but that's future…
**Tyler Benson (Mainwave)** 15:50 descent.
**James Thompson** 15:52 Right? Otherwise, we could end up with a workflow trigger type and a FaaS trigger type, and they differ. It can lead to confusion, I thought.
**Tyler Benson (Mainwave)** 16:03 Okay?
**James Thompson** 16:04 Yeah.
**Tyler Benson (Mainwave)** 16:07 So, one thing that might be a little difficult is, some of those Some of these semantic inventions have been around long enough that Vendors may have kind of built up their product around certain expectations.
And so, You might… you might get some pushback from vendors that don't want to have to change things.
Just a warning there.
**James Thompson** 16:43 Yeah.
Nope.
**Tyler Benson (Mainwave)** 16:47 Anyway… Well, I think this is good progress, I can certainly try to, spend some time going through this, offline, but thanks for the introduction.
Serkan, do you have any… Feedback or concerns?
**SÖ Serkan Özal** 17:11 No, actually, I had already reviewed the other two namings, the call start and the instance ID. I was just not aware of the new initiator things, so that's kind of new to me.
But yeah, that seems, I mean, right way to… to rename the semantic attribute to the correct name, but as you said, there might be pushback from the vendors as They are, I mean… Using the, the applicant attributes.
**Tyler Benson (Mainwave)** 17:45 Do you have, an area where you kind of call out some of these more significant changes, James?
**James Thompson** 17:55 Oh, I… Like, I… I haven't gone into that level of detail in the document.
Right.
Right, because the detail's supposed to kick off the project.
Alright. But… I don't… Envision much changes other than what's already being proposed.
Right, so… Changing the trigger to initiator, right? That's probably the biggest change.
**Tyler Benson (Mainwave)** 18:28 Okay.
**James Thompson** 18:29 Nope.
Yeah, but… because, like, FaaS name stays the same, FaaS version, all that stays the same, right?
**Tyler Benson (Mainwave)** 18:40 One thing I think you're also going to run into, is it's one thing just to get the, the semantic convention, document updated.
But then there's also going to be a fair bit of work going through all of the instrumentation across all the different projects, and getting those updated.
as well.
**James Thompson** 19:02 Yep, yeah, and I agree, right? And that's part of the reason why I reached out to all the different Component is to see if any of them were on board.
Right? And then I can update some… As well, and stuff like that.
**Tyler Benson (Mainwave)** 19:19 Okay.
**James Thompson** 19:19 Yeah.
**Tyler Benson (Mainwave)** 19:20 Great.
Okay, well, awesome. I'll, I'll try and find some time, over the next week to review this a little bit more. At this point, are you just waiting for, approvals from us, or… or what?
**James Thompson** 19:40 Alright, so… Looking for approvals, alright?
We will need to reach out.
to the TCG lead, For this project to get their sponsorship of it as well.
**Tyler Benson (Mainwave)** 20:00 Okay?
**James Thompson** 20:01 Yeah, so I need to… Look up who that is.
**Tyler Benson (Mainwave)** 20:11 I would suggest reaching out to, Carlo, Marlos?
He would probably be a good one to start with.
**James Thompson** 20:25 Yeah, okay.
**Tyler Benson (Mainwave)** 20:33 Great. In the, the meeting notes for today, do you want to just list out all of these, documents? Do you have access to that?
**James Thompson** 20:44 I'll… it's a Google Drive, I'll just need to find a link to it.
**Tyler Benson (Mainwave)** 20:49 It's in the calendar invite.
**James Thompson** 20:52 Give me a second… Calendar…
**SÖ Serkan Özal** 21:02 Yeah, just there.
**James Thompson** 21:05 Meeting… Meetings on the internet.
Yep, okay, yeah, I can go through updating that.
**Tyler Benson (Mainwave)** 21:22 Great.
Also, great work on keeping all of the Dependabot stuff up to date. Thanks for all that.
**James Thompson** 21:32 Yeah, yep, and… I think… We also just need to look at the JavaScript Layer.
update, as well.
**Tyler Benson (Mainwave)** 21:46 Yeah. Do you use, the OTEL Lambda stuff a lot with work?
**James Thompson** 21:53 Not really.
**Tyler Benson (Mainwave)** 21:55 So what got you into this area?
**James Thompson** 21:58 It's just an area I've been interested, interested in, and it's a way to contribute.
**Tyler Benson (Mainwave)** 22:05 Okay.
Great.
Well, I think, doesn't seem like we've got anyone else attending today, but thanks for the overview, and I'll try and take a look.
**James Thompson** 22:22 Okay, thank you.
**SÖ Serkan Özal** 22:24 8.
**Tyler Benson (Mainwave)** 22:24 Have a great day.
**SÖ Serkan Özal** 22:25 I assume.
**Tyler Benson (Mainwave)** 22:26 That's what I think.
**SÖ Serkan Özal** 22:27 Yeah, bye.
