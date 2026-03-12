SIG: CI/CD SemConv SIG
Date: 2026-01-27
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/Ik22WFeffixXtiL3eO38iUdam71uZ8c5ZU6ZsVDETN8HbfjALmbaVzIXyz-XVAQY.gd4EFZf6xR3lbl6t
============================================================

## Zoom Recording Transcript

**Alan Clucas** 00:27 Hello.
**neilyashinsky** 00:29 Hey, Ellen, how are you today?
**Alan Clucas** 00:30 I'm right. How are you?
**neilyashinsky** 00:32 Very good. I will, just pop on camera for a bit. I got, some of the sniffles, so I… I'm trying to spare you from some of the worst of it. It's a lovely, lovely backshot. Where are you, calling in from?
**Alan Clucas** 00:45 This is kind of my… it's like a shed on the back of the house.
**neilyashinsky** 00:51 Oh my god, I relate to that so hard. Maybe that's why I loved it so much, because you might have a very similar view. In fact, in the confines of this call, I will confess that I love sitting on my deck so much that I used to take conference calls in my kid's little playhouse in the rain.
And I called it the Junior Executive Conference Room.
So much better, as probably you can attest to, like, being outside if you have to be on a computer all day. If you're outside in, you know, the fresh air or whatever, it's Very much better.
**Alan Clucas** 01:22 It's… it's… I'm not actually outside, I'm… but it is… it's… it's… That is the back wall of the house, but there is a…
**neilyashinsky** 01:30 side ass.
**Alan Clucas** 01:30 kind of wall.
**neilyashinsky** 01:31 Hahaha.
**Alan Clucas** 01:31 There's lots of light here.
**neilyashinsky** 01:33 I don't know.
**Alan Clucas** 01:34 I don't like it when it's dark all the time, so…
**neilyashinsky** 01:37 So you would consider it, then, inside, I guess, but almost outside?
**Alan Clucas** 01:41 Yeah, it's… it's cold here. If I was actually outside.
**neilyashinsky** 01:44 Pretty crazy.
**Alan Clucas** 01:46 And wet, as well. We've just had a big storm come through in the UK, so…
**neilyashinsky** 01:49 Oh, nice. I feel like that, right?
**Alan Clucas** 01:52 Had flooding and stuff, so…
**neilyashinsky** 01:54 Oh, that's not nice, yeah, no, that's never… I mean, you know… It's part of the cycles or whatever, but yeah, we just got hit with some pretty bad snow. I think it was negative 14 on Friday, from a windshield perspective.
**Alan Clucas** 02:05 I've got a friend who lives in Texas, and, like, my view of Texas is, you know, cowboys and deserts and stuff, and, you know, he's saying it's, like, colder than I've ever lived in.
**neilyashinsky** 02:18 True Texas. Hey, Christoph, we'll stop talking about the weather as soon as you want to, but the true Texas is a land full of contradictions in every sense of the word. And I'll say I love visiting Texas, would personally choose not to live there, but I love visiting Texas.
But I will just say, with zero characterization, that I've never been to a place with so many… Churches, and so many… There's a whole variety, but I'm just gonna call them strip clubs, gentlemen's clubs.
But it's such close proximity, because Texas has no, what's it called, laws regarding, like, zoning, what we would call it in the States. No zoning laws almost at all. And so there's this whole dizzying array of… these places of worship very much… I mean, you don't find them a lot necessarily next door to each other, but just, like, the very close proximity, and the… The, I'll say the rich tapestry that it forms, I liked Houston a lot. Dallas is… Batistans… I mean, they have their charms, don't get me wrong. I'm not here to hate on anyone. I live in the Detroit area, which everyone will, you know, at some point, as well, I've told you how, whatever, rough, terrible, you know, had a really bad reputation. Not saying there was not crime and whatnot, but reputations are kind of its own thing.
You might even say reputations are all, but that's more of a shout-out to my Bernard Cornwell friends out there, anybody?
That's actually where I, again, I don't want to interrupt things, it seems like we're still in a prep mode, but I spent my, kind of my time during the pandemic reading historical fiction, including, the Saxon Chronicles, and where I became a little bit of a… UK history… Fanatic is probably the wrong word, but, you know, it's just like, You can learn a lot about the world by studying cultures that have gone through a lot of cycles and things, and… For various reasons, I wasn't interested in paying attention to the news, directly.
So, it's like, oh, let's find out what the… what life was like in 9th century… I guess if I wanted to be canonically accurate, I'd say 9th century Wessex, right? England wasn't a place yet in the 9th century, give or take?
**Alan Clucas** 04:42 Yeah, I'd say that too. I'm not really a… I'm not the expert either, but…
**neilyashinsky** 04:47 Only through fiction have I become an expert in history, which is a weird thing to, like, acknowledge.
But, yeah, Bernard Cornwell's an interesting author because he, he dates ancestry back to Saxons, in the, you know, in the 9th or 10th century or whatever, at Bamberg, I believe it's called, Bamberg now? Which at the time was called Bevenburg.
And so it tells, like, kind of… it's a little bit of the history of the unification of England, and Alfred the Great.
Who is the only English king with an honorific of the great, which is, you know, something I had no, you know, and still really don't have any context of appreciating that or not, but it's a thing I… it's a fact I can state.
I've babbled on now for 5 minutes about history that I really don't know a lot about, so I'm just gonna be quiet, go back on mute like I was supposed to, and let the adults talk, let the grown-ups talk.
**Alan Clucas** 05:47 I don't know whether we're, expecting anyone else.
I haven't actually checked the.
**Christophe Kamphaus** 05:51 Usually, Atriel or Dotin are joining us.
I'm not sure.
I haven't seen any message on Slack from them.
Okay, looks like Totan will not be able to make it, so I will just go ahead.
And, present myself this time.
Let's see, where do I have the screen?
So usually we start out by filling out today's Agenda… So if you have any topics you want to discuss, feel free to add some here.
In the And we also start with some triage.
And it doesn't look like anything changed since last week, so… That would be quick, son.
**Alan Clucas** 06:48 I've, put up a PR for Golang Environment Burial Context Propagation, So, that's… I've done my bit for that, but it hasn't had any… review yet.
But, so the middle one of those ones in the center of the screen, yeah.
**Christophe Kamphaus** 07:10 Okay, so…
**Alan Clucas** 07:10 That's why, that's the issue.
And there's a PR up against that.
It should be…
**Christophe Kamphaus** 07:22 this one?
**Alan Clucas** 07:22 There we are, yes.
**Christophe Kamphaus** 07:24 Okay, I can take a look, but, yeah, I'm not a maintainer of the Go SDK.
**Alan Clucas** 07:31 I'm… they require maintainers to be for, these things, so I… one thing I was going to raise, I don't know whether you are capable of sponsoring membership of OpenTelemetry, Christoph, or…
**Christophe Kamphaus** 07:52 No. I just became an approver in the SumConf.
**Alan Clucas** 07:56 It'd be both.
**Christophe Kamphaus** 07:57 But nothing further.
**Alan Clucas** 07:59 I will ask… I think Adrielle would be capable of being a sponsor, so…
**Christophe Kamphaus** 08:03 Or at least ping the guy who should take a look.
And I guess it doesn't certify you.
**Alan Clucas** 08:11 It's whether… whether I own it, or whether… I'm happy to own it, because I'm… I will use it once it's merged, and released.
it's… it's… the actual code is simple, that's… there's more tests than there is code. It's… and it requires, yeah, requires a change to code owners, but I haven't done it in there because I haven't had a response from… I didn't know whether… I can't remember his name, Pella Red?
Wanted to own it, or whether he wanted me to own it.
It's just the way I, GoContrip requires, has to have an owner for each.
So… module.
**Christophe Kamphaus** 08:56 No, I think it makes sense, so… They don't become orphaned.
**Alan Clucas** 09:00 So I'm happy to do that, but I would need.
become a member of OpenTelemetry in order for that to be workable, so… which I'm happy to do. I've… I've got more PRs open in… more PRs in OpenTelemetry Operator.
And things. So, I feel like I've probably done enough.
Anyway.
**neilyashinsky** 09:22 No seek.
**Alan Clucas** 09:24 Thank you.
**Christophe Kamphaus** 09:25 I can take a look and maybe open an issue in the community of OpenTelemetry to propose you as a new member.
**Alan Clucas** 09:34 Okay, I'll, I'll ping Adriel and Dotem and see whether…
**Christophe Kamphaus** 09:43 Yeah, there is a defined process for how you can become a member, and…
**Alan Clucas** 09:47 I think it requires one or two PRs and contributions, so…
**Christophe Kamphaus** 09:51 If you have those open…
**Alan Clucas** 09:54 I've got at least 4 merged across OpenTelemetry.
**Christophe Kamphaus** 09:58 I think such should be enough.
**Alan Clucas** 10:00 Yeah.
And too, too open.
this one and OpenTelemetry operator init container support, which is the biggest thing I've introduced.
**Christophe Kamphaus** 10:56 I will take a look for that one.
**Alan Clucas** 10:58 Okay.
**Christophe Kamphaus** 11:13 Do we have any other agenda items?
**Alan Clucas** 11:21 I don't have anything on… Working through tracing still in… other workflows, I've got to the phase of writing tests for it.
But I'm not attempting to implement CRCD SEMCOM yet. I'm going to release… I want to get it out, so I'm going to try and release it as, like, an alpha thing, and then saying all the spans you see may be different later.
Because, I want to see what people in the real world care about.
You got it?
**neilyashinsky** 11:51 I'll start drafting somewhere.
**Alan Clucas** 11:52 Yeah.
**Christophe Kamphaus** 11:54 Yeah, we are now at the point where we need feedback from the community.
To, see where we can improve.
**Alan Clucas** 12:02 But, I will try and then do another change to… I… because Workflows is not strictly… well, it's not always used for CICD, in fact, it's probably used more for data than… CI, at least. I'll, It'll have to be somehow optional.
**neilyashinsky** 12:21 But probably just…
**Alan Clucas** 12:24 the span names will be different if you enable it or something, not sure.
**Christophe Kamphaus** 12:30 I don't know if you saw the issue about the unified, conventions?
**Alan Clucas** 12:38 No, I haven't seen that one. That looks interesting.
**Christophe Kamphaus** 12:42 Maybe you can take a look for that one.
Okay, I think it also has a PR open, but it has, okay, maybe I'm… At least there's a proposal for renaming.
**Alan Clucas** 12:57 Okay, yep.
**Christophe Kamphaus** 12:58 We were missing sponsorship, and prototypes that would implement these conventions.
**Alan Clucas** 13:08 Okay.
Yeah, I'll have a look at that then, that's, that's very, very interesting.
**neilyashinsky** 13:15 I was thinking the same.
**Christophe Kamphaus** 13:20 Yeah, for this one, we would also probably need Other implementations beyond the CICD space.
And I think that would… Yeah, we would need to find those implementations.
**Alan Clucas** 13:37 Yeah.
**neilyashinsky** 13:40 I have… Interesting, I just started looking at the standard… The, what is it? AI agent semantic conventions?
And, I'm just so new that I don't want to say more… But just that, I'd be happy to take a closer look, because I do think I, I… Let's say… have some insight into how I might have approached this, but it was a little while ago, I don't remember exactly the decisions I made, I can't… I can't recall it back yet.
But I just… I just cut… put eyes on the… the thread or whatever, and maybe I'll… Have a chance to take a look, and between now and the next time we meet, attempt to try and have something a little, well, cohesive to add.
To the conversation.
**Christophe Kamphaus** 14:38 Now, basically, conceptually, Any workflow, any drop, Would be described similarly?
I guess.
The question is more, is there something special for just the ICD, or the others like AI workflows?
That would make it impossible to… abstracted, and have a unified… semantic convention.
And would it be easy enough for someone just coming fresh, coming new to the OpenTelemetry SamConf.
to find what he's looking for, if it's… unified. If someone is looking for CICD conventions, we'd say find this is.
So these are the kind of questions we would need to answer on this issue before we can unify it as well.
So yeah, if you have any feedback, feel free to comment on that issue.
**Alan Clucas** 15:48 Yeah.
**Christophe Kamphaus** 15:55 Oh, hey, I see Carlos has joined us.
**Carlos Alberto Cortez** 16:01 Yeah, that was correct. I wanted to discuss something quickly, well, more than discuss, probably just ask for feedback. I don't see Adriel, but, probably Christoph and the rest of you have an opinion on this one. Let me just write while I talk. This is regarding the long term.
Rolling spans the discussion we had in the past.
And, the interesting thing about that one is that, as you know, there has been interest from the community for a long time. The problem was how to tackle this.
and that… So, long story short, after all that discussion, the initial approach Apparently approved by the, by the spec.
People who come to, you know, to discuss the spec stuff, they said that we should go with a spam processor that could be triggering events, you know?
when your Spanish, like, long-running Spanish is starting, and when it's ending, I'm sending heartbeats to the backend, or somewhere, so you know the Spanish is still… You know, happening.
**Christophe Kamphaus** 17:07 So basically, when you start the span in your SDK, it would emit an event.
**Carlos Alberto Cortez** 17:13 And taught B-Defense.
Correct, yes, exactly. Yeah, and the idea is that, backends, or probably, and this is one of the questions, probably it would be interesting to have a prototype that includes a collector processor that could, in theory, would be waiting for such events.
And then, once it's… it knows that… the span is ended, he can actually, you know, do something more. And this overlaps with the next question, which is, This is something somebody mentioned, and we don't have to discuss that here in depth, but if you have any opinion, there are… so Trask was saying, I think it was Trask.
that probably if your application… I remember, actually, it was both Trask and somebody else, that if you have too many long-running spans, they will create a problem memory-wise, because then you have a lot of operations happening there, probably, potentially.
waiting. And then you are wasting memory, or using memory for no reason. So instead of that, you don't actually create any span.
So that could be an option, but the problem, of course, in that case is that then you would need the collector processor I mentioned before, where you would be actually creating such a span at the… at the collector level, but also the problem is, and this is probably more important.
span, context propagation-wise, because when you have an actual span, even if it's in memory, and it's taking forever to end, and it's taking, as I said before, some memory, you still have that context, which you can propagate. So I don't know what, like, how much is interest, based on your own experience, for these long-running spans.
whether you actually need to have, like, a single monolithic, let's say, span that is huge, and it has a lot of information, but still, it's one huge monolithic span, or you have an actual hierarchy, you know, different spans. That could impact how the prototype Goes one direction or the other one.
**neilyashinsky** 19:21 Go ahead, I was gonna ask if you had a sense of, like, the types of… jobs, for lack of a better word, that are running, that are taking this, you know, program or whatever, is it… a really large, synchronous process that's taking a long time? Is it a… is it… are there asynchronous elements? Is it heterogeneous? I'm just curious if you had, like, a particular… you know, Thing in mind, a long thread in mind that you're trying to track or trace?
**Christophe Kamphaus** 19:50 In CICD, it could be all of that.
**neilyashinsky** 19:53 NCICD. Huh,
**Carlos Alberto Cortez** 19:56 There was also an example about LLM, like, you are, you know, you're sending a prompt.
**neilyashinsky** 20:00 Right.
**Carlos Alberto Cortez** 20:00 And let's say it may take 7 minutes before you get something back.
And you want, you know, the… like, people to know that these 7 minutes of operation is still happening, not that, like, you got stuck, you know?
**neilyashinsky** 20:14 Go ahead, please, please.
**Alan Clucas** 20:16 No, no, sorry. See, it's… what you're… you're… so I wrote… just to give you some context, I wrote, the issue that's in the SEMCOMF repo. I was the original author of that, so… This covers… Spans that might be 7 minutes long.
And where the collector Lives for the entirety of the span, which is not guaranteed in… Kubernetes, I would… Want my collectors to be vaguely ephemeral.
And… Not to have storage, ideally, so… It doesn't solve… some of my problems that I wanted solving, I think, but I'm gonna… let's… I won't… I'm not trying to diss it, let's, let's try and… So, one of the things I want to be able to do is for the emitter of the span.
So the whole workflow is run by a controller in Kubernetes, in my case, I've got workflows, and that would want to be able to start the span, but the span may not finish for days, to be honest. It's not, like, minutes or hours. It can be really, really long times.
I know people who run week-long workflows. It's rare, and I would discourage it, but, you know, that does happen.
They are spending a lot of money on the process.
So, you know, they're processing their entire data set.
Right, right. The entire world, you know, trying to do forecasting and stuff. Anyway, so they… And this is not… this is not CI, really, this is data processing, but it's… it's the same software that… and the workflow controller can quite happily, right now, run on spot nodes and be killed, and it can't reject… we can't continue the span for the workflow or Even just phases of the workflow, individual steps within it, can't be continued.
and… Yes, I… I would like… it would be nice that… Partway through a workflow, a user… from a user experience, the user can come and look in there at the trace for the workflow and see what's happened, why it's taken twice as long today to get to step 5 than it did yesterday, or whatever. You know, they can try and analyze the differences midway through, because they can get to that all that information.
So that's the problem it feels like you're solving at the moment, but I still wouldn't be able to… With the SDK, I feel. Would I be able to emit a heartbeat from a completely new process, knowing the span and trace ID, so if, if they're… if they generate, you know, deterministic span… trace IDs, I could emit the start in one process and then continue it in another process, or anything like that. Is that something you're considering?
**Carlos Alberto Cortez** 23:40 Could you elaborate on that one? Like…
**Alan Clucas** 23:45 So… Argo Workflows runs in Kubernetes only.
and would run, is… is a controller in the strict Kubernetes sense of the word. It, it runs something akin to a Kubernetes job where there are multiple pods, rather than one pod. Yep.
But that controller can die and restart. That is a normal part of the process. As it currently runs, you could… You can reconfigure it, you can even do, like, version upgrades, and the workflow that is running Controlled by that controller continues running.
and fall.
Other purposes in this, that is fine. I mean, it feels weird when you look… let's go to metrics, where I presume you're aware, you know, counter metrics occasionally reset to zero when the controller restarts, but We work around that in the final end.
delivery of metrics. You don't tend to actually look at the raw metrics, you use Various mechanisms to make it so that that makes sense to the human. And I have a problem that I would like to omit. Trace is that I would like to have my top level, my root span.
top-level trace, whatever, trace ID, being the workflow, because that's what CID, CD, SEMCOM suggests, and… but I came up with it independently. That was all I wanted to happen, and then I found CICD And… But they agreed, and then I struggled with, I can make this work if the controller survives, but I can't make it work if the controller restarts.
**Carlos Alberto Cortez** 25:35 Yeah, but the controller… Go, go ahead.
**Christophe Kamphaus** 25:38 Yeah, on Jenkins, we have the exact same problem.
The master could restart and lose the top-level span, trace, whatever.
And any jobs that are durable would keep running and emitting child spans, so for sure, we want to have this hierarchy.
It keeps the context.
And, yeah, we need to be able to resume a previous top-level span.
**Carlos Alberto Cortez** 26:07 Okay, so in that case, yeah, like, child-parent relationship is super important, okay?
**Christophe Kamphaus** 26:14 Yeah.
Also, I think… The separate aspect here is… In whatever observability backend.
I guess that's a separate issue, but we want to be able to display it in a convenient way. I think at the moment, that would be displaying spans, and no defense.
**Alan Clucas** 26:36 Yeah.
**neilyashinsky** 26:40 I'd love to… No, go ahead, Alan, please.
**Alan Clucas** 26:43 Yes, my, my ideal is that the end user of these woods.
not… be aware that the controller had restarted. The span would look identical under both scenarios. I mean, there might be… it might be an important thing that slowed down the workflow. It shouldn't slow down very much. If it's a… but it's a very fast-running workflow, it might be. But my ideal would be They shouldn't have to do any special understanding, because quite a lot of our users are quite Data users tend to be more naive than CI users.
**neilyashinsky** 27:23 Carlos, maybe I jump in for a moment, because I feel like this is a perfect opportunity for me to kind of talk a little bit about…
**Alan Clucas** 27:33 why I jump into the CICD semantic group in particular when I… I don't even know how to spell CICD, but…
**neilyashinsky** 27:42 The reason that I'm here is that, you know, someone just mentioned about how, like, the users are separated from the jobs and the details, and… One thing that I've noticed over my time in technology is that we very rarely, if ever.
have a common language across, like, the delivery into deployment, or, you know, from initiation through dev through operations. And so that's when a lot of disconnects happen, first, because we're not necessarily observing the right things to start with, because we don't understand how it was built.
And so that's why I have a lot of interest in long-running traces, and just the TLDR on that is I use a pre-flight emitter, and basically, like, hey, this thing's starting.
Anything that I am trying to understand and isolate for, like, operation time or, like, long run time, I use logs with annotations back.
So that way, for me, it's an easy way to maintain a level of granularity around the things that matter without, you know, getting bogged down in a lot of… spans, for lack of a better word, I guess fans that aren't adding a lot of value. And so that's why, I feel like, you know, in some ways, if we can derive context from… In this case, if we can derive context from the CICD, And have that context to be… not just preserve, but acknowledge and leveraged in the observability, I think Rastoff just mentioned, like, so that when these things start breaking, or they go down, or whatever, they're performing poorly.
the observability setup is already leveraging, you know, the metadata that's been baked into the CI-CD conventions to start with. And that… as much as that wasn't part of your question.
I feel like that's a little bit of the answer, and, like, having the right metadata inside those spans, or what have… inside the telemetry data itself that allows you to perform the introspection that you need to… I mean, at the end of the day, we're trying to… optimize operations, I suppose, right? Not just, like, traces for the perspective of traces themselves? I mean, observability being a good thing for us.
But it's to optimize or to find problems and spot them, yeah.
I don't know if that was useful, hopefully it wasn't.
**Carlos Alberto Cortez** 30:07 Yeah, if you have any examples of any open source stuff, about this kind of, item, it would be great. You can post that, and I can follow up with that.
**neilyashinsky** 30:17 Yeah, like, semantic conventions into the long-running… well, I don't consider them long-running in my implementation, but, like, how I do the pre-flight, checklist for my spans, is that… I mean, I don't know of any other ones, but I'd be happy to share, yeah. Do you wanna… maybe I'll shoot my email to you, or how can we best connect offline?
**Carlos Alberto Cortez** 30:39 Oh…
**neilyashinsky** 30:40 I don't think I'm on the Slack yet.
**Carlos Alberto Cortez** 30:42 Yeah, you're… if you want the Slack, if not, I can probably paste my email here. Yeah, whatever's.
**neilyashinsky** 30:47 Yes.
I don't think I've gotten a slap.
**Carlos Alberto Cortez** 30:49 I will, yeah, I will, yeah, I will write my email here, in the chat, but otherwise, Slack, yeah. The advantage of Slack is that, you know, people can reference that in case somebody comes and discloses that some… for their, you know, development on that, or anything.
**Christophe Kamphaus** 31:05 Also, the chat is recorded.
**Carlos Alberto Cortez** 31:08 Oh, right, yeah.
**Christophe Kamphaus** 31:09 publicly accessible.
**Carlos Alberto Cortez** 31:11 Hope I don't get so much spam. Anyway, I guess that the last question on this front for now, while I'm still digging, because… Sorry, I was, I'm working on the prototype and all that. There's a prototype for that, which does, bare… bare stuff. It's solid, I could say, for .NET, but other than that.
Those… this group have… Any opinion besides, what they said, especially regarding the initial approach, that besides actually having the span, you could be Extending these logo bands.
for, you know, like, I could say that when you start Spanish, it could be the closest that you can get to pre-flight, reporting, and then you have the heartbeat, and then you have the end.
Is that something that would be fine? That would mean that you have both the span and the events, and somehow the vendors, the backends, or the collector, they would need to do some messaging, you know.
To, to report this.
Is that something that sounds, from the… from your goals, let's say, that certainly could be an off, or is that something that you would… You would imagine it wouldn't be enough, for one reason or another.
**Christophe Kamphaus** 32:23 Let's see if I understand you right.
You basically propose A solution that would not include any spec changes.
So we would define semantic conventions for events and mapping them to and from spans, from the CI-CD spans.
**Carlos Alberto Cortez** 32:43 It could require spec changes, but only regarding adding a new processor.
A spam processor that would be… firing, basically, shortband, you know, the same combo bands, you would be purporting them. But that would mean that everything would have to, you know, include this spam processor.
**Christophe Kamphaus** 33:05 Okay, and that could be done in a generic way for any kind of span.
**Carlos Alberto Cortez** 33:11 And this could… yeah, this could mean that it would be also an opt-in. Like, most people wouldn't need that, but if you need that, then just, you know, declare as part of your configuration that you're using this processor, and then, you know, just do your stuff.
**Christophe Kamphaus** 33:29 I think it sounds like a very interesting way of solving it.
I'm not sure how it fits, work on the backend side.
**Carlos Alberto Cortez** 33:42 Yeah, actually, that was kind of my question, because, I mean, honestly, the prototype, as I said before, there's something almost on for .NET. I would write one for Java, present that in the spec call soon, but eventually, I would like to see some backend trying to support this, you know?
And, because I think we will need… somebody to actually think from the vendor side, whether that could be enough or not, you know? So, I get that kind of disclaimer that I used to work at a company called LightStep.
And there was something like this that we had called Meta Events.
That would be reporting, you know, the heartbeat and everything regarding spans, you know?
And, we know that something like this could be enough.
But that's how our implementation works. I don't know whether, like, other implementations that could have any additional capabilities could require something more exotic, you know?
**neilyashinsky** 34:39 when you, Christoph, when you said back-end.
It was you, Christopher who said that right, Is that… I wasn't entirely sure, is that backend, is that, like, persistence in a database backend?
**Christophe Kamphaus** 34:53 In an observability backend, for example.
**Carlos Alberto Cortez** 34:55 cure.
**neilyashinsky** 34:56 Correct.
**Christophe Kamphaus** 34:56 check or have this open issue where they want to be able to display incomplete spans, so that's what I was thinking of.
**neilyashinsky** 35:05 Yeah.
**Carlos Alberto Cortez** 35:06 Well… this is… this… there's… actually, that's another topic that we could discuss probably further, but there is, an experiment that somebody, from the TC called Josh Surrett, he was playing with, which is that you could be having, like… because I would say they overlap, like, running… long running spans, they overlap with the needles.
sending, incomplete spans that you are losing, technically, because the application is crashing. So, basically, he was trying to do something that what Prometheus does, which is that you have a you know, you have some, set of, span records integrated into disk.
And then if the application, you know, crashes, it will check whether there were, like, any pending spans to be sent. Just recover them and send them, you know?
Yeah, so this is kind of an overlap with this, that one.
**neilyashinsky** 36:00 Yeah.
**Alan Clucas** 36:01 Would we require… My implementation, I would much rather be emitting spans as I can, or partial span events, continuously… ish.
**Carlos Alberto Cortez** 36:17 Yeah, correct, yeah, yeah, yeah.
**Alan Clucas** 36:19 some cadence, just, and then if I know I'm crashing, because mostly it's not really a crash, in my case, it's a known… a sick hang-up kind of thing, because I'm being transitioned to a new node.
Yeah.
**Carlos Alberto Cortez** 36:33 In that case, you can actually define a different architecture to solve that, yeah.
**neilyashinsky** 36:38 I think… I feel like it's a scrape versus scrape versus push all over again, right? In the sense that, like, if it's healthy enough, it'll admit out But if it's not healthy enough, it doesn't, right? And, like, scraping, obviously, you can be too unhealthy to be scraped, I guess, as well. But then you have the failure of the scrape job itself.
As you're, you know, observability signal or whatever, and so that's, I think, the essence of my… like, how I would analyze this problem is which… which telemetry signals you need for which use cases, and when can you log versus when can you trace? Because I feel like, especially if there's a large volume of spans, like that heartbeat, if it's just, like, I have a process running for, like, Alan's friend's running the process for a week, and now I've got a week worth of heartbeats, like.
Does that really… how am I… I mean, you can definitely check when you haven't gotten a heartbeat in a minute or two, and you can detect that.
So it's not like there's no value, but I feel like that's where the… the rubber will meet the road in terms of the… Telemetry data that you're generating, and how you'll… Leverage that to solve your problem that you're… that you're instrumenting for.
**Carlos Alberto Cortez** 38:02 Yeah, and a slightly related question regarding that is, like, for this issue that Christoph is showing.
Instead of using log events to, you know, to send the hard beats, it's like, we will be resending instead, like, the incomplete spans.
Like, you know, basically could just span with some flag, probably, saying this is not yet complete.
Or sending the end timestamp as none, which means that, you know, it hasn't finished, either way, or both.
The only problem for that is that, There was first some fear that implementations have small details around how they handled and timestamp.
But more importantly, the fact that some backends seem to be, like, observability backends, even, like, the one, for example, Jaeger, which is open source, they… they are append only, you know? So you are… they don't support, like, getting spanned once, like, once more, and updating that. It's, like, that's… that's breaking their invariance or something like that.
**Alan Clucas** 39:06 Yeah.
**Carlos Alberto Cortez** 39:10 So, I guess that, okay, so we don't have to keep discussing that for now, but, basically, I got some additional information from you, which is great, and I will keep working on this prototype. As I said before, this is what's initial agreement for the specification group. Let's hope we can make progress for that. If not, we will have to come back to this option B, which is sending the actual incomplete spans, you know? But then you would have to be sending the entire thing a few times, you know? And if it's running for days, probably that's not the best of any way.
**neilyashinsky** 39:41 Yeah, there's a non-zero chance we may have a little bit of overlap. I'd love to connect after this and see if there's something that I'm But, but I've… That might illuminate…
**Christophe Kamphaus** 39:52 Yeah, for sure, if you send in complete spends, you open also many questions, like.
**Carlos Alberto Cortez** 39:57 Yeah.
**Christophe Kamphaus** 39:57 Do you need to resend all the attributes? Do you only reference the initial span?
What happens if you have load balancing of collectors in the middle?
**Alan Clucas** 40:07 Yeah.
**Christophe Kamphaus** 40:08 That's not true.
**neilyashinsky** 40:10 And now that…
**Carlos Alberto Cortez** 40:10 Yeah, Greg, I…
**neilyashinsky** 40:12 Right.
**Alan Clucas** 40:12 I don't think the collectors can do the job of… of… Coalescing this, because they're stateless at the moment.
As far as I know, I mean, generally stateless.
**Carlos Alberto Cortez** 40:23 Mostly, yeah. It depends on the components, but yeah, like, I think that's the best way to go for now, and if not, it could be opening, you know, a can of worms, for sure.
**Alan Clucas** 40:33 Yeah. I… I'm… I'm good with not spend… sending heartbeat events at all.
I don't see the need to send heartbeats, but what I do need to be able to send is the heartbeats and the start event are good from a presentation point of view, because you've got your top-level span appearing if it's a long thing. That's a presentation layer thing, but what I can't… Sort of work out how to do is, is, emit my end event in a different process from when I started it in a way that kind of… and I can fabricate it, I suppose, in the same way that something like GitHub or GitLab does. It's an app?
the entire thing.
**neilyashinsky** 41:31 that's basically what I do, is, like, have a little wrapper around it, and it's… it's kinda… it's a pretend span, in that, like, it's not… following the spec to the letter of the law in, like, how a span is supposed to operate, but it's like… You know, an extra… Special Spanish.
**Alan Clucas** 41:49 I've got a fair number of these is the trouble, because quite a lot of things can span controller restarts.
And I suppose I can rebuild them all.
**Carlos Alberto Cortez** 42:01 Yeah. By the way, I had to drop, what, Neil, I have your email, but Alan, Alan, let's say in Doja, I'm a little bit curious about your own needs, especially how you manage to… how you prepare the context, so you can understand in a different process, if I understood correctly. So let's talk offline. You're in Slack, right?
**Alan Clucas** 42:22 Yeah, I mean, suck.
**Carlos Alberto Cortez** 42:23 Okay, perfect. Suddenly, I had to jump because I have other calls to attend, etc. But yeah, I think it was initial, feedback that will hopefully help me.
To grab all my prototype and keep on working.
**Christophe Kamphaus** 42:35 Valleco Nachos, amigo.
**Carlos Alberto Cortez** 42:37 Where am I?
**Alan Clucas** 42:38 Thank you.
**Carlos Alberto Cortez** 42:39 50 rounds.
**Christophe Kamphaus** 42:40 Zoom.
**neilyashinsky** 42:42 Yeah, Alan, I was just wondering if, like, your last job in that job is basically a push to something else, right? That's like, hey, this was done.
And that's what you would connect with your pre-flight.
event.
Those two things.
If that's not too…
**Alan Clucas** 43:02 Yeah, I mean, basically, I need just to… I've got all the attributes I need at the end of the event as well as the start. It's not like, that's all fine, all I need to do is make sure I'm properly recording the start time, so I can just emit the entire… entire fabric. I need the spans to exist in the SDK. I can create them, but just they never get emitted.
Because I've crashed. Crashing's the wrong word, we don't tend to… Right, right. It's not crashing that I'm trying to solve for, I'm trying to solve for.
**neilyashinsky** 43:35 Graceful restarts, continuous graceful restarts.
We're experiencing a response time approaching infinity?
**Alan Clucas** 43:45 So I… I have a… I need the spans to exist in order that, just from the way the Go SDK works, it's way easier if the spans exist and they get stored in what's in the Go context, etc, so that all trial spans… there are some… a lot of short-lived trial spans that If they don't get emitted because the controller's restarting, it's… that's not going to be a real issue.
**neilyashinsky** 44:12 Okay, you…
**Alan Clucas** 44:14 Yeah, you can… you can then… I could just fabricate them, but I just need to store all of the start time information, is the trouble.
**neilyashinsky** 44:21 I was just gonna say, you know, the right recording rule might be really useful here, because that way you can, you know, generate some of that metadata along the way, and you don't have to rely on it being in the span in the first place, but you can still, through annotation and baggage and context and whatnot.
Have those details in the span.
But is… it's generated from, you know, the log entries and whatnot.
**Alan Clucas** 44:48 Yeah, no, I mean, I don't want to generate from log entries. I could generate from log entries, but then every user of workflows We'll need to run some… horrid log processing, running over days of the workflow controllers emitting a massive number, at least they're now properly, JSON-formatted logs, so it makes it easier to tie the things together, but there's a huge amount of data coming out of the logging.
**neilyashinsky** 45:18 Well, that's.
**Alan Clucas** 45:19 it's a single log for everything in that controller, there's no… it's got appropriate attributes to it, but again, I don't want to be doing it that way, the point is to get real spans that you don't need to.
**Christophe Kamphaus** 45:33 Yeah, you could send this study fund… through a separate pipeline, which is basically what Carlos also mentioned. We see spam processor emitting events.
But then you would need something at the destination or in the.
**neilyashinsky** 45:48 Right.
**Alan Clucas** 45:50 Exactly.
**Christophe Kamphaus** 45:50 together.
**neilyashinsky** 45:51 That's what I was saying, the recording rule on the back end, if you will, and the log events are only the exceptions. They're only… not the mundane behavior, but you log when something is really log-running, for example, or the exceptional behavior that you're looking for.
And those are logged, and that way you can generate a log on the, on the rare events, not the, you know, commonly occurring events.
**Alan Clucas** 46:19 They can be relatively commonly occurring, and my shortest spans are about a second long. That could… could exist at… could start and end in different controllers.
**neilyashinsky** 46:30 I'm not, I'm not in your environment every day, so I'm not trying to tell you you're.
**Alan Clucas** 46:34 No!
**neilyashinsky** 46:34 Only, only, only, pretending like I'm a straw man over here, for you to whack against.
**Alan Clucas** 46:41 You could generate almost everything that I want to get out of… I mean, I'm adding loads more detail for tracing.
**neilyashinsky** 46:48 Right, right.
**Alan Clucas** 46:48 But you could generate a lot of this from logs, the higher level stuff, but it just… It just feels… you can't then implement CICD SEMCOM. It's not.
Unless you're… implementing a log processor that can transform it all into span, so that then you can view it all as one overall trace. Is that… am I getting that wrong?
**neilyashinsky** 47:13 No, well, I mean, I think you're right, but I don't think that's that hard, because you already have the backend system set up to do all this. And I honestly, that's why… I think I…
**Alan Clucas** 47:24 Yeah, you're, you're searching… gigs, if not more, of logs in order to generate these spam pairings.
**neilyashinsky** 47:33 Imagine…
**Christophe Kamphaus** 47:34 Well, he's sending it through a separate pipeline.
**neilyashinsky** 47:36 Right, yes, yes, I think… I don't know if it's necessarily a dual emissions approach. There's more than one way to architect this inside the containers.
But, essentially, the ability to… generate… Telemetry around the… things that you don't have visibility for today, right? You've got some gaps in your visibility, that's why you're trying to do this. And so, rather than increasing the amount of data that you're flowing through your existing telemetry channels to instead supplement that with a secondary pipeline to use Christoph's language, emission architecture, whatever it is that is… Focus narrowly on what you're trying to solve.
**Alan Clucas** 48:34 So you're suggesting a dedicated, stateful… processor.
**neilyashinsky** 48:41 It doesn't have to be stateful, I don't think, but it could, if your architecture lends itself to that. I think you could do it…
**Alan Clucas** 48:47 Cool.
**neilyashinsky** 48:48 Okay, yes, stateful, I think, in your… I want to be charitable, not charitable, open-minded, because I… stateful is kind of like I locked into an HTTP method, mindset, and I think what you're describing is a persistence layer to track.
To track the…
**Alan Clucas** 49:09 Yeah, that's what I mean by stateful. I mean, a stateless thing in Kubernetes has no memory of anything that happened.
**neilyashinsky** 49:16 Right.
**Alan Clucas** 49:17 Before now, apart from by things that it can immediately observe now that are.
**neilyashinsky** 49:22 Yes, yes.
This is… this is actually where I… just a little bit more about Context Core is… people and agents, you know, LLM agents have similar challenges, and so does, actually, you highlighted as well, so do pods, so do containers. As they come into the universe or whatever, they pop onto the scene and they have no context of what happened before, and there's no metadata.
reliable or protocol-based for them to, like, hey, you know, what happened on the last page, or whatever. And so, that's what I attempt to create for… People and machines together is a queryable… metadata layer that brings together development with operations. In this case, you know, the CI-CD part of development, and allows you to generate a secondary telemetry pipeline of sorts that allows metadata Observation, if you will, or metadata process observation, so that you're not just… Monitoring traces as, like, a part of the application with, you know, from one pod to another, but you're just using that same model Now on your business processes that those applications were built to support.
And so, because you have a single querying interface regarding data, the data model's unified, or you have to unify it, or… there's ways to do that, but basically an abstraction layer that allows you to connect one to the other in a way that's useful for your introspectrum.
**Christophe Kamphaus** 51:02 Yeah, for that spendings might be useful.
**neilyashinsky** 51:06 Sorry, Christoph, what was that?
**Christophe Kamphaus** 51:09 You could use span links to link different spans from different traces.
**neilyashinsky** 51:13 Yes.
**Alan Clucas** 51:17 No.
Maybe I'll…
**neilyashinsky** 51:21 Maybe I'll have, enough confidence to share a little bit more code. Oh, you know, it's like my third meeting, or not even… like, my third overall meeting, I think it's my second time on this call, and so I have a little bit of, like, I don't know what it is, maybe still a little bit of, What do they call that, Where you're, pretending… you're afraid you're just pretending to be, you know, three kids in a trench coat.
**Christophe Kamphaus** 51:45 Post us information.
**neilyashinsky** 51:46 Pastor, thank you, Christoph. I was suffering a bit from my imposter syndrome.
But I will say that my perspective is unique, perhaps, or it's attempting to be, because we have these disparated data silos across the operations of our applications, and we haven't yet found the right metadata layer or right abstraction to bring them together in a way that… Makes it easier to… observe things from the technical and the business, if you will, standpoint. Like, the people who care about this stuff. In the end of the day, I think it's visibility for them into its effectiveness as a… whatever.
Whatever it's designed to do.
And so, we gotta infer all that, it's really hard. I'm like, God forbid, if you wanted to, like, optimize this process now, like, if it's just, like, taking a simple e-commerce example or something like that, like, you need a whole new context layer now to understand, like, what your actual users are doing. None of that's… Generatable in today's current systems, which means that you have to, like… then there's, like, customer data pipelines involved, and data warehouses, and it's… just spirals out of control.
**Christophe Kamphaus** 52:56 Yeah, switching out between different solutions.
**neilyashinsky** 52:59 Yeah, you have this huge drift, and the data model just, like.
I mean, there's data, there's, like, a lot of smart inferences. I don't think I was like, gosh, this is so brilliant for me to do this. I'm like, why hasn't anybody tried this before? It's like, it is all more or less right there, like, if you kind of, you know, think about a fax machine's just a telephone with a waffle iron connected to it, that sort of thing.
That's a Simpsons quote, forgive me.
I'll go back to yelling at clouds, but yeah, I'm happy to chat more about this, because I do think that this is, You are, I see the opposite side of the coin all the time, right? I'm not building CICD pipelines, but I'm helping provide insight into, you know, the operations of those from, you know, usually it's… I mean, sometimes it's, like, the build engineering perspective or whatever of, like, why is this taking so long, but… More often than not, it's like, why is it taking so long for my application to continue to evolve, right? Because, you know, the build process takes 5 hours or whatever, like, how quickly can we move if it's 5 hours? 5 hours at a time, basically.
I'll be quiet, but yeah, that's where I think…
**Christophe Kamphaus** 54:12 to interrupt you.
**neilyashinsky** 54:13 Okay, good, thank you, I appreciate the validation.
**Alan Clucas** 54:15 this.
Yeah, it's cool.
**Christophe Kamphaus** 54:24 I think we don't have any more topics today.
**Alan Clucas** 54:29 Yep.
**neilyashinsky** 54:31 Great conversation, thanks so much for sharing.
**Christophe Kamphaus** 54:33 Thank you very much as well.
**neilyashinsky** 54:34 Oh, that's.
**Alan Clucas** 54:35 Thank you.
**neilyashinsky** 54:35 Happy to be of service.
**Christophe Kamphaus** 54:36 See you next time.
**neilyashinsky** 54:37 Like a 4K.
Cheers. Bye.
**Alan Clucas** 54:39 See you.
**Christophe Kamphaus** 54:40 Cheers.
