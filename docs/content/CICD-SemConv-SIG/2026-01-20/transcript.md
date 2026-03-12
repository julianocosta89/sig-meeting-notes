SIG: CI/CD SemConv SIG
Date: 2026-01-20
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Christophe** 00:11 Hello.
**Alan Clucas** 00:13 Hello?
**Adriel Perkins** 01:28 Good day.
**Christophe** 01:32 Hello.
**Adriel Perkins** 01:34 How's everyone today?
**Alan Clucas** 01:38 Alright. You?
**Christophe** 01:41 Binance you?
**Adriel Perkins** 01:43 Doing okay, thank you.
Give everyone just a minute.
Alright, I'll go ahead and share the screen, and we can get started with some triage, and then we can move to, specific… Agenda items?
**Neil Y** 03:00 Hi, how are you today?
**Adriel Perkins** 03:01 Good, how are you?
**Neil Y** 03:03 Good, I don't mean to interrupt, I'm new here, but I just figured I'd, show up, I'm interested in, maybe helping out. This is, semantic conventions, yes?
**Adriel Perkins** 03:12 For CICD, yes.
**Neil Y** 03:14 CICD, yes, great, great, yes. I probably won't be necessarily in this group directly. I haven't really decided, but I wanted to show up and just kind of get a little bit of a broad, view of things, so thanks for having me.
**Adriel Perkins** 03:25 Awesome, yeah, thank you for joining.
**Neil Y** 03:26 This is…
**Adriel Perkins** 03:27 Do you want to, like, introduce yourself and maybe ask some questions? We got a few minutes we can spend on that.
**Neil Y** 03:33 Oh, sure, I mean, yeah, absolutely, if you'd like. My name is, Neil Yashinsky. I am here on my own capacity. I am formerly of Grafana Labs, where I was an observability architect.
And I've been, pursuing a new project of mine, full-time, called Contacts Core. And Context Core is an attempt to extend the… breadth, I guess, of OpenTelemetry into first project management, just for the sake of, like, not having to, like, have more project management tools, right? And just have that whole… other layer of data that's siloed and not built in with everything else, and Maybe using, like, traces, metrics, and spans to represent progress, and be able to leverage that metadata, basically, from, you know, initiation design through development, deployment, operations, and ideally optimization, that's out of scope, but really just kind of creating the context.
If you will, to have better insight be, like, pre-deployment, really, and, like, what is these applications for? And not… not a heavy, what you call footprint? Light footprint.
that can help, jumpstart your observability journey down the line, because you've kind of, well, programmatically generated, I guess, procedurally generated or whatever, from the artifacts and the labor you use to build those artifacts.
**Adriel Perkins** 05:12 Neat!
Welcome aboard!
**Neil Y** 05:14 Thanks.
**Adriel Perkins** 05:15 That's, that's, pretty, pretty cool.
**Neil Y** 05:19 Oh, thanks.
**Adriel Perkins** 05:20 Especially since some of the project management goes right into DORA.
visibility.
I had a couple gigs of… I've taken some of the events that come from, like, GitHub issues, or, you know, Jira, projects, and taken those and, like, kind of applied semantic, OTEL standards to them, and then been able to use them correlated with, like, you know, the SHAs that are in some of the source code to be able to understand more effectively, just work cycle time, but also, you know, change lead time on the door metric. So, I think that you're thinking about, the project side of the house.
Or product, whichever one you want to call it.
**Neil Y** 06:02 And hopefully, like, the kind of key is just, like, automated status reports.
And be able to… You know, infer from developer metrics, etc, derive metrics from blogs.
where tasks are, and thus you can also do a dashboard for status. That's always up to date.
**Adriel Perkins** 06:25 Yeah. Awesome.
**Christophe** 06:29 One issue that might be of interest to you is the CICD producing long-running traces.
**Neil Y** 06:37 Yep.
**Christophe** 06:37 I found out that one, and it's actually a specification issue.
Is that, what you're working on.
**Neil Y** 06:45 Oh, great, yeah.
Well, thanks for having me, and, you know, if there is, especially, like, small tasks, I mean, I've been coding for longer than I care to admit, but, you know, I'm looking for a few good, like, what commits or whatever to, like, get my feet wet into the hotel contribution world, so I like to, learn by doing, so just, you know, I'm gonna be quiet in a minute and, you know, just listen to, you know, you folks talk, but, in the background, if you're like, oh, this is kind of an easy thing, or wish we'd had some You know, intern level, someone with, experience or exposure.
Let me know, I'm here for help.
**Adriel Perkins** 07:27 Cool, I appreciate it.
**Neil Y** 07:28 Certainly. Thanks for all your work, as well.
**Adriel Perkins** 07:34 All right, we'll go into a little bit of triage for the next few minutes. This is the long-running traces issue, that Kristoff was… was talking about. It's on our project board. It's quite an interesting read. Alan originally opened it up, and then, Carlos is working with the spec SIG to, Just figure out how we can drive that forward.
I did talk to… I think we all talked to Kristoff last week? I think that was in the call, but he said it'd be… it'd be a few weeks before he was able to circle back with some… some updates on that, so… This one, as discussed, I did go ahead and open up all the remaining issues that were in the stretch goals section. There's one on every single repository.
I'm waiting for one of the TC members to tie them to this, issue as sub-issues, so that we can see them all, but they have been added.
On the Python side, Which, ironically, isn't showing up here on subissues. What?
Interesting.
**Christophe** 08:49 Nice, hopefully someone.
**Adriel Perkins** 08:50 There it is.
**Christophe** 08:51 So, we'll pick it up.
**Adriel Perkins** 08:53 Yeah. On the Python one?
It is in progress.
And, hey, I've got two approvals now. So… actually, they should hopefully get merged, very soon.
**Alan Clucas** 09:17 I was gonna say, I've… I've put in to talk about the Go one, because I volunteered to do it.
I just wanted to check that what we're expecting out of this Is only getters and setters, effectively, and a carrier, rather than a propagator.
forego. I believe that's everything. I… I've… I'm catching up, basically.
And the spec says it differs between different implementations.
the main reason I'm querying it is because on… there's a slight wording difference between OpenTelemetry Go and OpenTelemetry Go Contrib. In OpenTelemetry Go Contrib.
The propagators directory is called propagators, and contains propagators.
And in OpenTelemetry Go, it's called propagation, and contains things like carriers.
**Neil Y** 10:15 That's odd.
**Adriel Perkins** 10:15 Good.
That's a great question to ask on the issue, and at, Robert, pay… Payjack? Yeah, paycheck.
I would add him with that question. That is interesting. The… so, we… for context on the… on the spec, Originally, I just had propagators.
And then there was, you know, Robert brought up that there's another way to do it, which is carriers. And so… After that, I added this section for supplementary guidance, which was just not really… it's not really the spec. It's just, hey, you have a couple options that you can do to meet the spec.
One is a dedicated propagator, the other is just operation on the carriers with any arbitrary text format propagator. I think Robert's… preference is the text map propagator, carrier path.
But like… OTEL Swift, for example, and OTELPython originally actually both had dedicated propagators for it. So… I've just been of the takes, like, whatever people want to do, like, if they have a preference within their language, that's fine.
I did carriers and Python for the re-implementation, and they seem to be completely fine with that and support it. I do think carriers is probably the better of the two approaches, but… it's totally up to the… to the language maintainers and SIGs. Given that you… there's that nuance in the contribib rep repo, I would ask, and I would… I would just add him in there. You could even chat with him on Slack, too, he's pretty… he's pretty open.
**Alan Clucas** 12:09 Okay.
I will do that. Thank you.
**Adriel Perkins** 12:13 You're welcome.
I did respond to the JavaScript one, so I think that individual may be picking this one up soon.
In fact, that JavaScript one kind of outlines some of the information that you and I just talked about, Alan, about the, the dedicated propagator and not doing anything with process spawning, so… I don't know if you want to check it out or not, but it's there.
Everything else, I think, pretty much stays the same. Is there anything specifically anyone wants to talk about?
**Neil Y** 13:02 I'll ask one more question about the long-running traces, if you don't mind.
**Christophe** 13:07 Yeah, go ahead.
**Neil Y** 13:09 Was the idea of… of… If you will, having the same parent span as the original trace, and have it be served as an… like, a new, whatever that'd be, child's fan, I guess? Or… was it recreate, so yeah, I guess that's really the question. Is it… is it… Somehow leveraging… finding a way to restart the existing span, or, like, it's a new child span above the span that timed out before? Does that make sense?
**Christophe** 13:44 So, the basic data model of spans and traces for CICD is that we have a parent span of the full job.
And then we have child spans for tasks.
The problem with long-running spends is If you start some in the SDK.
**Neil Y** 14:03 It could get interrupted.
**Christophe** 14:05 And you won't see it in your observability backends until the whole span is finished.
So you will never see in-progress bands.
**Neil Y** 14:17 I see.
**Alan Clucas** 14:17 I also have the problem that my… Program that is running the span, it wants to call the SDK and start the span so that it can have children.
But it's, it's a Kubernetes.
**Christophe** 14:37 Program that, quite happily, right now, will run on a…
**Alan Clucas** 14:40 a pod that might die, it might run on a node that's a spot node, and will get interrupted that way. So I would like to be able to recreate these spans… without them having… I'd like to be able to recreate the same span ID, as my top-level span, and have all my children coming from it, starting and ending, potentially in different programs, which is a broken model for the SDK at the moment.
**Neil Y** 15:08 Yeah, because it's interesting that you mention that, because, when I worked at AppDynamics, there was this concept of a business transaction.
ever familiar with that at all? And it, like, brought to… like, if, you know, I was, let's just say I bought something online.
the business transaction, like, goes through that purchase, but can also include, like, shipping and stuff. So, like, when the shipping is complete, you can tell that… how long, like, the whole order process took. It was included in that. And so there's this, I guess, broader context.
That you can tie these separate pieces together as a single… megaprocessor, or super process, or something like that? And is the… is the thought that this will… Because it's so long, it has to have pieces outside of its own context, that it can kind of piece together with the broader pieces of the whole?
Am I… am I understanding it correctly, or is it just another recreation of a new span from the parent, you know? So… so maybe… maybe a reattempt, or… or even if I heard you right, like, the same span over again, we're just… Trying to keep it alive longer?
**Alan Clucas** 16:20 Yeah, I… I… my pref… my… my personal feeling is… for my use case, is I want it to be the same span that I can… keep alive in… and have… alive in… not multiple programs, multiple executables at once, but… But re… reinvigorate it in a new executable, so that where… because the… the alternative where… you have… A sort of long-running span that's made up of multiple children.
or multiple elements, is… requires the… the user interface to… well, not requires. Ideally, the user interface for… a split span versus a single span doesn't… it doesn't appear differently to the end user when they are viewing this in a… in a… in whatever tool they're using, Grafana, perhaps, because that's confusing. Why should they… care whether, you know, whether the controller that was running this thing died or didn't die. They shouldn't have to see the difference. So their ideal… the ideal outcome is that they get to see you know, the same thing. But, you know, the controller restart might be an important event in why they're CI run, for example.
didn't perform the same way as it did before. So you might need to see that information, but it shouldn't be apparent if all you care about is the overall, sort of, I just want to get top-level general flow for my thing. You should have to see it differently if the controller restarted.
**Neil Y** 18:00 Right, I see. So leveraging existing ID is, like.
brass tacks, if it will revive the chain of evidence, or chain of identification, to include the… Okay, thank you so much, appreciate that background.
**Alan Clucas** 18:14 So that a single top-level span, the CI model is the single top-level span, is an entire CI-run workflow, whatever.
**Neil Y** 18:26 Makes sense, thank you.
**Christophe** 18:28 And how it's solved is, in the SDK, you can basically create spans from a known context, so a given span ID. It's just a bit more involved.
For example, similar to how you can open a context from HTTP request.
you could inject your own context ID, if you have a deterministic way of generating that ID.
Or you store it somewhere.
**Neil Y** 18:54 Okay.
**Christophe** 18:55 And in the SDK, you can also create a span and open it in the past. So that you say…
**Neil Y** 19:00 Huh?
**Christophe** 19:01 It has already been ongoing for X amount of time.
**Neil Y** 19:05 Interesting.
**Christophe** 19:06 But still, that's a lot more involved than just in your program saying, I'm starting a span now.
And it lasts however long it lasts.
**Neil Y** 19:16 Because you have to kind of pick up where it was kicked off from the first place, right?
**Christophe** 19:20 Exactly, so you need to persist that, and…
**Neil Y** 19:24 Interesting.
**Christophe** 19:25 So, that part is not the problem in the specification. The specification is really a problem.
That we only sensor span once it's done.
So in the protocol, we cannot send any in-progress spams.
So, also in your observability backends.
**Neil Y** 19:46 You cannot display.
**Christophe** 19:48 A span that hasn't been received yet.
**Neil Y** 19:51 Right, right, right. So you want to, like, have a, like, a work started, almost, kind of metadata, or insight, or whatever you call it, datum, I guess.
**Christophe** 20:01 You could send a log record, that it has started, so an event, basically.
And from that, you can reconstruct the span later on.
**Neil Y** 20:12 Right.
**Christophe** 20:12 Transformations like that are done, it's just not specified.
**Neil Y** 20:19 Okay, here's a dumb question, then, forgive me, it seems like… is that just why you should create, like… a first parent spend that is already… oh, because it wouldn't be done yet, would it? It still has to wait for the child span to finish.
**Christophe** 20:32 Exactly.
**Neil Y** 20:33 I see, I see, yeah. I guess you could have, like, a meta span of sorts, like a span span, but it's like, hey, I did this thing, so you can report on it or whatever, but it kind of breaks the model, I feel like, because then you have this.
**Christophe** 20:49 Yeah, so basically you would see your first task, it would arrive as a child span, and then you would start seeing sibling spans.
**Neil Y** 20:57 Right, I guess maybe, like, a tracking… a tracking span initiated or something like that kind of doesn't break the model totally, sort of?
**Christophe** 21:05 I guess you could have a parent spend that's very short, and then have everything under 8, but…
**Neil Y** 21:11 I thought a child span underneath the parent that's like, hey, this process is started by this parent.
**Christophe** 21:18 You could, you could consider the checkout as that.
Of course, most shops have a checkout.
**Neil Y** 21:27 Okay, I'll stop talking now, because I'm very new, and I don't really understand all the details, and I don't want to disrupt, your, you know, the follow-up, but I… but again, I appreciate the context very much.
**Christophe** 21:36 you know.
And the solution we had in the GitHub receive of the OpenTelemetry Collector was we basically just created everything after we received the finished event. So anytime we had a task finished, or a job finished.
We created the full span.
Because we also had deterministic IDs. So we could construct span IDs, trace IDs from that.
**Neil Y** 22:03 Right.
Okay, that makes sense.
**Dotan Horovits** 22:08 Neil, by the way, there are no dumb questions, I think your feedback is important, and by the way, I highly encourage you to, oh, now I can see your face, so, thanks for chiming in on this discussion. The discussion has been going on for some time, but maybe if you want to chime in on the GitHub issues, you can see the discussion there, and maybe, first of all, maybe some of the questions will be answered there, and if not.
more than happy to have you comment there so that we can have your feedback persisted and feed into the discussion. So, looks like you're knowledgeable and passionate about the topic, so do feel free to look into the respective GitHub repos, and also, sounds like you bring a lot of experience from, you said, AppD and others, so, definitely relevant. One more thing that you mentioned, I think there's no contradiction either or. I think what you mentioned is something that has been, keeping on coming, like, you mentioned, like.
I would call it a session that is actually comprised of multiple traces, and that, what you said, I think you called it actually a process, or something like that.
It's a whole different… exactly, and this is actually sort of a whole different set of… a problem space where you really have, like, not just asynchronous, but sort of a process that has multi-phase, some of this are human intervention, or something like that, so you finish one phase, I don't know, login, so you have one interaction, and then you go and check against the database. Something like that, and this usually, you may have even multiple traces.
that comprise the whole end-to-end process. So I think… I do see the similarities that you, that might have resembled, but I think… so this is a whole separate category of maybe another meta-concept above the trace that brings several traces together into a whole flow, or process, or a session, or whatever you'd like to call it. So there's no contradiction, I think, with what you said at the beginning.
**Neil Y** 24:03 And I kind of look at it as, like, this is what Alan wants to track, so it's, you know, ideally, it can support his business case, rather than shoehoring it into some other model that exists, or whatever.
Not that you're suggesting that, but just… I was. So I appreciate the, the, encouragement, and I will do my best to, you know, do so. Thanks.
**Dotan Horovits** 24:22 Yeah, happy to have you, and looking forward, and that's what I'm saying. We're happy to have new faces here, and new feedback, and it's really helpful for us, so don't be shy to chime in.
**Neil Y** 24:32 I'll try not to make you, regret that advice.
That's…
**Dotan Horovits** 24:43 Adriel, back to you.
**Adriel Perkins** 24:46 I don't think we have anything else, so go on once.
One twice?
Alright, well, it was good to see everyone. Y'all have a great rest of your day and week, and we'll catch you up next week.
**Christophe** 24:59 You too?
**Dotan Horovits** 25:00 Thanks, everyone, a good one.
**Christophe** 25:01 to you.
**Neil Y** 25:01 Appreciate you. Take care, bye.
**Dotan Horovits** 25:03 Bye-bye.
