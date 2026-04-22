SIG: CI/CD SemConv SIG
Date: 2026-04-21
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/Loi88PaAb7glLHt66rYiX--NlKth7HiIhQxaW9DE3XWdry3P7Bio6HUDkVXl5ami.4pWyyn8KqSjNIgYl
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 01:11 Good day.
**Christophe Kamphaus** 01:13 alone.
**Adriel Perkins** 01:15 How are you?
**Christophe Kamphaus** 01:16 you.
Why not you.
**Adriel Perkins** 01:18 Doing well, thank you.
Doing what?
Alright, I guess we can go ahead and get started.
Looks like it might just be us this morning.
Alright, I'm gonna quote the board. Well, actually, I'm gonna review some of the stuff for the 7th, so… I am working on this. I've got a PR that's open to fix, some issues, add some rate limiting, and then I'm gonna move the receiver to beta, and then traces to alpha.
So I am actively working on that.
I have not added these work items to the board yet, but I will do that as on my to-do list.
And then… I had a question about this one.
don't remember what we were… I don't remember what we kind of, like, Ended up with?
But… Yeah, did we want to go with having an exec or not? I think we ended up with the… we don't need to add, the complexity of an exec span. Is that right?
**Christophe Kamphaus** 04:13 I think what we came out with, that maybe we want to have something where we can group Every… all the… Spence where it's executing.
So we would have 1… For the queue, one for cleanup, and anything in between.
To also maps and to saturation metric.
**Adriel Perkins** 04:43 Via an attribute on the spam?
**Christophe Kamphaus** 04:50 So that's the… Good question.
Because currently we have C… pipeline, The pipeline run span defined, and we have the task spend defined… But nothing where we could say, this part is now for the queue, and this is for cleanup.
No.
**Adriel Perkins** 05:18 Okay.
**Christophe Kamphaus** 05:23 I'm wondering, do we need it?
**Adriel Perkins** 05:27 Yeah.
I'm not sure we need exact, but we, like, Q was definitely… beneficial Because you can't tell by default.
without, like, omitting… either… I mean, you can put the… you can put an attribute as a metric on a span.
I can tell you that information up front, but… the experience that some asked for, they wanted a little bit better than that. So that's the way we just did it in the GitHub receiver as a preface to all this.
But, like, that's, you know, exact time is calculatable.
By deriving total time minus the queue time, so you kind of have it there.
**Christophe Kamphaus** 06:17 So basically, you want to be able to have a span-to-metric conversion.
To have this possibility.
**Adriel Perkins** 06:30 Yeah, that's what the community… well, that's what at least one member in the community was asking for on the GitHub receiver.
**Alan Clucas** 06:38 I am. There is already, in OpenTelemetry Collector, a span to metrics.
Conversha, if you want one.
**Adriel Perkins** 06:48 Oh, yeah, the red metric, connector.
**Alan Clucas** 06:52 No, there's a generic… generic thing, I believe.
I've used it before.
It can, I'll find it for you.
**Christophe Kamphaus** 07:03 If my memory serves right, then you can just say counts as spans according to these attributes. It's something like that you can do.
**Alan Clucas** 07:13 Yeah.
**Adriel Perkins** 07:13 I think that's the account connector.
And I think the span metrics connector is one dedicated for red metrics.
OHR, rate, error, duration.
But I will say, they added, like.
a ton of new components since the last time I checked.
When I checked last week, I was like, oh, that's a new component. So, yeah, they've been adding a lot.
I tell you what, for this one, I'm gonna just write up My thoughts on an issue on this, that we can, like… Kind of tactically talk about the two.
Potential options.
Because we don't have an issue for that, right?
**Christophe Kamphaus** 07:58 No.
**Adriel Perkins** 08:00 Okay.
I will… I will take care of that on my to-do list this week.
That's the update on the GitHub receiver.
And it looks like Robert has something, so Robert, next 10 minutes-ish plus are yours, if you want to chat about that.
**Pellared** 08:26 Yeah, sure. Do you want to share… you can share your screen.
So… I was working recently on… together with Alan, on implementing it within Go, and then I was reviewing other languages and making specification updates, and I just want to keep the momentum and work on stabilizing this document.
And I would be very glad to have your input regarding this document, if there's anything that, that we or even I should work on address before it gets stable.
So far, my only question, which is, in my opinion, a blocker, is like, should this carrier be in the SDK, or is it fine to have it in CodeWrip? Maybe should it be… have a recommendation to have an SDK?
I'm just… I do not have any strong opinion here, so… but if you have any ideas, you can… yeah, we can address them.
You can… we can discuss it now, or also async.
I will probably create an issue in the separate issue specification about stabilizing this document anyway, so we can gather all our thoughts there. I just didn't have time to do it. I decided to discuss it, like, 3 minutes ago. That probably is the right time to start working on this.
**Adriel Perkins** 09:42 Okay, no, appreciate all the work that you've been doing on this to carry this forward. It's been super helpful.
Yeah, we can definitely review it, give it a… give a look on Maine, and make any comments.
For this SDK on contrib portion, It almost feels like every language does it slightly differently, to an extent.
like, for Python, well, actually, it's probably linear.
**Pellared** 10:16 Like, SDK is not maybe even not the appropriate term, I mean, like, the core repository, because I remember the other carriers, like, for HTTP, are often in the core library.
Because the thing is that often instrumentation libraries are using it, so it feels like almost API thing.
And I thought that maybe it should be good to suggest to have it in co-repository.
But I would not be surprised that even without this language, it may land there at some point of time. But maybe it could be a good recommendation to suggest that it's in the core contribut Not core reposition, not contribute.
**Christophe Kamphaus** 10:56 That's my thought as well.
I was thinking, how is HTTP propagation handled? Is it in the core? Probably because it's something very… That's everything we'd need to use.
And here, as well, for environment variable propagation.
You could add it to any kind of CLI utility.
**Pellared** 11:20 Exactly.
**Christophe Kamphaus** 11:22 I think it makes sense to have it in core.
**Adriel Perkins** 11:25 That's my thinking as well. In Python, it is in core, it's just hidden, because it's experimental. So it's, like, explicit opt-in, not defaulted… default import.
But I think for… I don't know, one of the other ones, it was like… was it Java? Maybe Java was asked to put it in… in Trib?
So…
**Alan Clucas** 11:46 certainly was… was originally going to go into main… the non-contrip.
And then…
**Adriel Perkins** 11:52 Yeah.
I think the more that it stabilizes, the more likely it is to be, like, it makes sense to be in core, but I do think, like, long-term it makes sense to be in core.
That way, it's just available as a mechanism, because people are going to use it.
And, you know, it's one less thing to import.
**Pellared** 12:20 Okay, note taken.
Okay, so… also, I will probably also work on the C++ and… And Python implementation? I do not remember. I don't think it was implemented in PHP, right?
Anyone who remembers?
**Adriel Perkins** 12:43 Actually, they might have, they might have.
**Pellared** 12:48 I will just write, double check.
**Adriel Perkins** 12:56 Go Python… C++.
Java…
**Christophe Kamphaus** 13:03 Oh, it sees the issue.
**Adriel Perkins** 13:04 No, okay, it's open.
Let's make sure that nothing has been managed.
No, it looks like… looks like we're good. No one's implemented in PHP.
**Pellared** 13:14 In the agenda?
**Adriel Perkins** 13:16 Yeah.
There you go.
**Pellared** 13:40 What about JS, probably missing as well.
No figures.
**Adriel Perkins** 13:48 Someone was planning on working on it, but it doesn't look like it got… Done.
Yep.
Or at least a PR with, referencing it wasn't opened, so…
**Pellared** 14:11 Okay.
Is there an issue for .NET?
**Adriel Perkins** 14:20 There… do-do-do-do-do… Yes, here.
**Pellared** 14:25 Yes, first one.
**Adriel Perkins** 14:27 Yep.
**Pellared** 14:28 Okay.
I'll also try to… Work or help addressing this, maybe find some people, or maybe, yeah.
I would try to look at it as well.
complete just in the specification, but something that users actually can use. That's the more important thing.
**Adriel Perkins** 14:49 Did your PR to fix SWIFT get merged in?
**Pellared** 14:54 They are not responding, I have no bloody idea what's going on with this week.
Autoscope. It looks very dead.
**Carlos Alberto Cortez** 15:04 Like, the project itself, you mean? Like, the scene?
**Pellared** 15:06 Jeff?
Okay.
**Carlos Alberto Cortez** 15:08 I will follow up on that. You know, like, the DC has to be in contact with them, so I will be checking what's still there. Yeah, that's amazing. Yeah, but that's, that's up here. Let's see.
Yeah, my impression is that some Sikhs, actually, they have only a couple of people dedicated to them.
But that depends a lot on their employers, and that's… They come get off. Okay, but anyway, I will follow up.
**Pellared** 15:35 Thank you. Thanks, Carlos.
**Adriel Perkins** 15:39 Yep, thank you.
Alright, awesome. Anything else on this one?
**Pellared** 15:50 Thank you for my stay.
**Adriel Perkins** 15:52 Cool. Thank you, Robert.
All right, any other, topics for the meeting?
**Christophe Kamphaus** 16:08 Yeah, trust me.
**Carlos Alberto Cortez** 16:08 It's cookie from.
**Christophe Kamphaus** 16:10 Go ahead.
**Carlos Alberto Cortez** 16:12 Quickly, yeah, mine probably is shorter. I'm still, like, working on the prototype for the, processor, getting additional operations for the, like, for reporting all the Spanish bands, so that's still in the works. The prototype was easy to do, the only thing is that I have to, work and iterate on the, specification PR, which I hope to have ready later this week, so next Tuesday we can discuss that.
**Adriel Perkins** 16:37 Okay.
Do you think, do you think that that processor is gonna run into issues if we… if we add things like Q spans, or exec spans, or… And what I mean by that is, like, actually spans with the name of Q prepended to it.
Versus just, like, you know, a dedicated span for a queue at a task. Does that make sense?
**Carlos Alberto Cortez** 17:02 Yeah, I don't imagine problems at this point, but let's see. I'm very curious about, yeah, I think that, yeah, 16% prototype, you can see some of the details, but to me, right now, I don't see any problems. I could see it will be more of a design thing that the conversation with the other Sikhs to make sure that this looks fine to them.
But yeah, I don't… I don't envision anything funky. Or, well, actually, it depends. Are you talking about the adding? Because that's about talking about the new operation to the spam processor interfaces. If you are talking about the processor we specifically want, that could be, like, a different thing, yeah.
**Adriel Perkins** 17:50 So, is your proposal tab, too, then?
Or would it be, like, dedicated… Sorry, I didn't… I didn't entirely follow what you meant there.
**Carlos Alberto Cortez** 17:59 Yeah, basically, you know, there are two things that I have to do. The first one is adding the operations to all the spam processors.
Like, in the interface itself, we'll have, in theory, one or many new methods. So you have on start and onEnd, and there's one that is in development.
Like, on before end. But now, I will be adding this new operation on spam processors, which will be unchanged, most likely.
with the type of change. So that change, it's totally, it's totally fine. And I'm guessing, you're talking about the specific lifespan Or lifecycle spam processor, we will have.
You're talking about…
**Adriel Perkins** 18:38 Okay.
**Carlos Alberto Cortez** 18:39 Right, okay, the second part, yeah. I don't know, good question, yeah, in that regard. Sorry, I didn't have connected the two things. Okay, let's discuss in private. If you have something to point me to, that I can read, that would be good.
**Adriel Perkins** 18:53 Yeah, I do.
**Carlos Alberto Cortez** 18:54 So, I would say that this process will happen after the previous thing is at least in development stage, but it still would be great to start getting, you know.
like, beforehand, so we are… we can predict what will happen, yeah. So yeah, let's do that in private, yeah. Send me something, and I will read. Perfect, thank you.
**Adriel Perkins** 19:16 Cool, thank you.
**Pellared** 19:20 Carlos, do you want to discuss this kind of… because I remember the discussion, I don't know if it was from the spec, or it was just from the, OTEP, or something regarding the decision be… behind, in the processor to have something, like, unchanged, to have it, like, one… For all, or one… or a distinct… Functionality for each, you know.
thing which… that is changing? Is it something that you want to discuss, or not really?
**Carlos Alberto Cortez** 19:49 So, right now, my prototype is very simple. It's just basically… You receive something, You have literally one operation on spam processors on change, and then you have a minimum with the kind, and then some specific payload that you receive.
This is something very straightforward, and actually, I think we will have to discuss that with the specification seed, I would say, first, yeah. Something that we will have to discuss here will be Once that part is actually accepted, then we will have to come back here and discuss the life cycle spam processor.
**Pellared** 20:29 So my quick feedback, before the spec meeting, maybe it will make it easier for you, that, you know, it very depends on the language, but in many languages, it will be a method for each change.
It will be faster, because it will be… Better strongly typed.
And these payloads could be smaller. You will not need to have some payload, would be, you know, like a big ball of mud, for instance.
but you have, you know, a very small payloads for each event, and you have one on change, then you'll need to do some, I don't know, you know, casting or things like that for the payload, and I think it may be very difficult for some languages to do it in a performant way.
**Carlos Alberto Cortez** 21:11 Okay, okay, that makes sense. Okay, in that case, since I still have time, I will probably iterate on a parallel prototype that does, like, different operations instead of a single.
**Pellared** 21:23 Because I think for some languages, it will be, like, it doesn't matter, like, what is the decision, but for some languages, the decision to have, you know, one method per each, you know, event, you know, type, which is changing.
it'll be more performant and better. That's why I'll probably lean towards those proposals, but having both… if you have time, having both on the table will be good for discussion, and even, you know.
Showcasing the differences.
**Carlos Alberto Cortez** 21:48 Okay, yeah, yeah, good point. Okay, yeah, I will try my best. It should be straightforward, at least to showcase how it could look inside. Okay, perfect, thank you, thank you, we'll do that.
**Christophe Kamphaus** 22:00 No problem.
Thank you for working on this.
**Adriel Perkins** 22:07 Absolutely.
**Christophe Kamphaus** 22:11 From my side, I've worked on the PR, just the clarification one.
So, I had some feedback I will address today.
And I opened an issue for the consistent spelling of CICD.
**Adriel Perkins** 22:26 Okay.
**Christophe Kamphaus** 22:26 Historically, we have not been very consistent. We either use CICD or uppercase written together. Sometimes we use CI slash CD.
And we should probably standardize on one spelling.
**Adriel Perkins** 22:45 Well, brill.
**Christophe Kamphaus** 22:45 Any opinions on this?
**Adriel Perkins** 22:49 Ci Splash CD.
View my… Because they are two separate things, so…
**Alan Clucas** 23:03 I agree.
**Christophe Kamphaus** 23:12 On white.
We'll, we'll try to do the rename after my current PR is song.
**Adriel Perkins** 23:21 I appreciate it.
**Christophe Kamphaus** 23:25 That's all from my side.
**Adriel Perkins** 23:31 Cool, I'll continue working on the collector stuff, for GitHub.
I had a quick question for you, Alan. When is, when is tracing gonna be in Workflows 4.1?
Is that when it's gonna be…
**Alan Clucas** 23:43 It's going to be in 4.1, it's merged in Maine. 4.1, we are aiming… release candidates next month, so… how long does the release cycle take? Depends.
Alright, yep.
Yeah, so… May or June.
I'm hoping.
**Adriel Perkins** 24:01 Okay.
Thank you.
**Alan Clucas** 24:04 Yeah.
**Adriel Perkins** 24:06 That was a selfish question, for what it's worth.
Okay, I was trying to implement it the other day, and it's like, no, it's not in yet. It's in Maine.
**Alan Clucas** 24:15 Yeah, yeah, so if you… there are latest tags you could I've run 4.0 with just switching the workflow controller to 4.1. That will work. So you could just… You can install latest if you want to.
Bug, test it for us.
Should work. There's, if you want a complete working stack with Grafana, there's a document now… we publish documents from main, so the, Workflows docs have a page with, like, spin-off and a cluster with everything in it working.
**Adriel Perkins** 24:54 Okay, cool.
**Alan Clucas** 24:54 If you're okay, because you need, you need to inject the OpenTelemetry.
Environment variables into the workflow pods in order that they then emit their… Spans to the same endpoint, and everything appears at the end.
Right place at the end, which you can do with the operator, or… Using the controller to do it.
**Adriel Perkins** 25:20 Oh, cool.
All right, well, if there's nothing else, it was good seeing y'all. Thank you for the hard work, and we'll catch you next week.
**Christophe Kamphaus** 25:32 Bieom.
**Adriel Perkins** 25:34 Go.
