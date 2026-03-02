SIG: Go SIG
Date: 2025-11-27
Duration: 36 minutes
Zoom Recording URL: https://zoom.us/rec/share/fcF5Wk7lOfcx31TuIxd-UMLrEo5sPF77EsWRf3k-Wt0oxWKd5r5-pwl-0cdBrOpu.50EYZV6xj2aOxUaq
============================================================

## Zoom Recording Transcript

**Michal Jarmolkiewicz** 01:10 Hey?
**Damien Mathieu** 01:15 Hi!
**Pellared** 02:50 Hello, Dara, I've been 3 minutes, my daughter, this is me, and I'm alone.
**Nico Hertz** 02:59 Ayy.
**Michal Jarmolkiewicz** 03:03 Okay.
**Nico Hertz** 03:06 Nice meeting you, hon.
**Pellared** 03:23 Hello?
**Damien Mathieu** 03:25 Hey!
**Pellared** 03:27 I mean, can I ask you to drive the meeting today? I'm alone with my two daughters, and I, you know, go back and forth to help them.
**Damien Mathieu** 03:35 Yes.
I mean, I think the schedule is actually, seems like… it looks like the only thing there is, is, your enabled PR. I know Nico also has, a topic, to bring. Do you want to start, Robert, just in case you have to drop afterwards?
**Pellared** 03:56 Like, so I'll just quickly share. So, my ask is very quick.
It's just about asking for review, and I saw, Damien, you already reviewed DPR.
So, basically, and I also saw that you have been discussing this, last week, which seemed that there was an approval.
From the… from everyone on the last sick meeting, so yeah. So this is basically it, and asking for reviews, and yeah, I do not want to take… take any more time. So, for other… for any other talks, feel free to add your agenda items, but even if so, if there's anything…
Just, yeah, just, yeah, just pick up.
By the way, were I sharing? Was I sharing this screen anyway, or not?
**Damien Mathieu** 04:41 You… yes, you have been sharing your screen for a few seconds.
**Pellared** 04:45 Okay.
**Damien Mathieu** 04:48 Yeah, I mean, I've already been reviewing, but, anyone else, please feel free to do so, too.
You can…
**Pellared** 04:57 even… I also… I want to maybe stress, because we have a few people here, we like reviewers. We… we do not like… we have a few maintenance approvers, but the thing that we often struggle
is to have time to, you know, to get any help with the reviews. So, even if you're not an approver, and even if you think that your review does not count, it's not true.
each review counts, and it's important for us. Yeah.
**Damien Mathieu** 05:25 And it's a great way to learn more about the project.
Okay, Nico, you wanted to talk about,
the runtime PPROF, and changes to the public API to support that?
**Nico Hertz** 05:46 Yeah, sure. First, thing to mention, if there is any PR to review, I'm happy to take a look. I'm probably super new, so…
as you said, probably it's not gonna count a lot, but I'm happy to take a look and…
I want to learn more about this project, so…
So, yeah, about my PR…
Actually, I didn't have, like, much time to prepare a lot. Maybe I can just share the screen and…
and walk… walk you through the PR, and… So…
This… well, I'm sharing something else.
Alright, give me a second.
I think it's this one.
So, yeah, I mean, this PR got much bigger than it was initially intended.
But it's actually a pretty simple idea.
So I noticed that I was doing some profiling.
And notice that the… the tracer is actually creating,
tasks on this, Go profiling.
So, I started… I mean, I didn't know that was the behavior, so I looked into it.
And started learning more about this.
So, basically, as it mentions here.
So, right now, the current behavior is, like, I mean, there is no public API for this.
you just create spans, I mean, for distributed tracing.
And the spans also create these tasks.
Which are visible on the profiles.
And the change that I'm proposing is
Give more control to the user, basically.
So, if you want to create a task, you want to create a region, which is a different,
Concept on this, execution tracer.
I mean, maybe to show the…
The behavior, the easiest is to go to the test.
**Pellared** 08:33 just to understand it better. So, basically, right now, it's producing too much noise, right? Because an application can be… that's the problem, right? And also, the task is more, like, high level, if I remember correctly, for pre-proof, and the regions are more, like, subsections, right?
**Nico Hertz** 08:53 Yeah, so on the, like, the semantics of the… of the runtime tracer are that, yeah, a task is usually a high level.
like, an HTTP call.
Or, maybe, consume… if you have, like, a Kafka consumer, maybe that could be also another task.
And then, if you wanna… Measure, portions of the task.
This is usually done through… Throughoutians.
And the difference being is that a task will create a context.
while the Christians don't… do not have a context.
You know that in the distributed tracing, you have a context for every span.
But in the regions don't have a context, so they… Are intended to measure,
a portion of a… of a go routine, but not across…
**Pellared** 09:51 So…
**Nico Hertz** 09:53 Yeah, right now it's creating a task for every span.
Which is not, yeah, it's not the idea, like, it's creating a lot of tasks.
**Pellared** 10:04 Okay, so the idea of the region and task is still contained in a single goroutine, right?
**Nico Hertz** 10:12 A task can span across multiple routes.
**Pellared** 10:17 Okay.
**Nico Hertz** 10:17 Sorry, yeah, the task can span across multiple varieties.
But the region is only for a single orbiting.
**Pellared** 10:26 Okay…
Soap.
Okay, I just think if there may be a problem, if you have a region.
Which is kind of big.
Yeah, bye.
So, it depends… sparven, you can sparse different, you know, spence?
Which can be…
Then create a new routine can be either handled, like, you know, some consumer-producer in separate Go routines.
But I don't think it's a semantical problem.
Right?
**Nico Hertz** 11:10 And once again, the…
**Pellared** 11:12 I don't think… because right now, you know, a span can, in theory, you know, create a new span, it can pass the context to something which creates a new goroutine, it can pass, you know, so kind of this… the child span could be inter-processed in, you know, in some different goroutine, and the same can happen to regions.
And also, a region could… and a new span can also then, you know, distribute some work to other giroutines. So, in theory, one region could also kind of, you know, create new regions in other giroutines. So the question is if it's a semantical problem or not.
**Nico Hertz** 11:47 So the… so if you are creating regions, with… with this, you should,
I have guaranteed that it's not gonna span multiple go routines.
So that's the responsibility of the programmer, of the user.
So that's why… so the… right now, the default was creating tasks.
Because it doesn't know if the… if the span will… will… Cover multiple origins or not.
month.
So what I'm proposing is.
Either do it manually, so you know if your span will land on the same routine or not.
Or there is… so that's, the most I'm proposing, Are either manual instrumentation.
So you… you are creating the regions, and you… Are responsible for… Hating them, right?
Or there is also something I'm calling auto-instrumentation or auto-profiling.
In which case, It's gonna create a task for the root span, and then regions.
But then you need to hint the tracer that the span is gonna… Cover multiple routines.
So, that's one of the cases.
I think it's here…
So, if you know that your span is going to cover multiple Go routines.
Uni, and you are using auto-instrumentation, which is this… this optional mode.
then you need to tell the tracer that this span is gonna… is… I'm calling it async end.
The name can be changed.
So, in… in this, if you have auto-profiling, and…
And there is a span that is annotated with this.
Then the tracer is gonna create a task, not the region.
This is an optional mode. The other mode is do it manually, Or the default, is…
It will only create a task
for the… for the root, and then nothing else. Like, if you have a…
distributed tracing, and you have an HTTP API,
He's gonna get a task for every request, and that's it.
Which I think makes sense, like, I mean, you have, like, a GET request, and then you have a task associated with that request.
So, these are the modes. I think I have the explanation of the modes.
I have it somewhere here…
So, these are the modes. The default is only going to create a task for the root span.
Then Otto is going to create a task for the route, and then regions for the children.
But then, if you have a… I mean, I'm…
this also, like, I'm thinking that in most… for most applications, you are not gonna have spans that
cover multiple routines. I don't know if you agree on that, like, on most cases.
That's gonna… not gonna be the case. And I know that there can be cases.
**Pellared** 15:35 I remember that some Kafka library and instrumentation does it, but this is the only case which I remember, that some Kafka library basically consumes the messages on separate threads, correctly, sorry, but yeah.
It's a special case.
**Nico Hertz** 15:54 Okay, so in that case, I mean, you can do manual instrumentation, or you can annotate with this async end.
So, it doesn't get the…
**Pellared** 16:03 problem.
**Nico Hertz** 16:03 I give them options.
**Pellared** 16:05 That people who already instrumented these libraries will not change the codebase, so it's no, it's like…
It's kind of a little… I'm not sure if it's a breaking change, but yeah, I say it's still optional. The default will be the same, right? The existing one.
**Damien Mathieu** 16:23 I agree, the default should not change, and…
I think, your, I mean, the approach should be in smaller steps, especially because you are making changes to the public API, which is really tied to the specifications, and this is really not specified.
**Pellared** 16:49 Yeah, so, first of all, I think, Nico, that, first of all, good job on doing DPR. I think it's a good stuff to discuss, brainstorm, and explain, so I think it was not a wasted work. Even if you, even, you know, we can even look at it.
The thing is that I think that what Damon said, a problem will be with the changing the public APIs, especially the trace APIs. I don't think it will be easy, it will be an acceptable change.
But still, it doesn't mean that, you know, some pieces from your PR could not be adopted. For example, a subset of it. For instance, only created this route task, which may… which may be a good option just, you know, to reduce the noise created in the profiles.
still, I think the most needed
I think, at this point, is a good description.
With the problem, what is the problem of the current, you know, kind of…
Each, each option, and what are the benefits, cons.
And, you know, some background, maybe also this information and hyperlinks to the, to the PProf semantics, to the runtime semantics, because, just without these two lines, we are lost. Similarly, that you are probably lost when you were trying to develop something here.
**Damien Mathieu** 18:07 Also, because you…
**Nico Hertz** 18:08 Yeah, I know, I.
**Damien Mathieu** 18:09 yard change.
**Nico Hertz** 18:10 Good.
**Damien Mathieu** 18:12 Your PR also changed a lot, from when you opened it to today.
**Pellared** 18:18 Could you maybe start creating an issue first, and discuss this, you know, mention this PR, maybe you can even change it to a draft?
and, you know, described, you know, these proposals, you know, I think these are basically a few proposals, so, so that we can discuss each of them, maybe not even separately, but kind of together think about them. What do you think? Does it make sense for Unico?
Doesn't seem reasonable?
**Nico Hertz** 18:44 Yeah, so you were asking me to create sort of a document explaining all the alternatives or the considerations.
**Pellared** 18:51 Yeah, so we can… so that people who are also not on the call, that will in future also leave UDPR, will be able to do it.
**Nico Hertz** 19:00 Yeah, yeah, sure, no problem. I mean, I guess a simpler alternative, if we want to have, like, a first step.
could be… I mean, right now the… we have this iteration with the quantum tracer.
But there is no way for the user to disable it. Like, if you have…
**Pellared** 19:21 I totally agree. I totally agree. It's maybe, it's maybe a first step.
**Nico Hertz** 19:26 Definitely a problem, and it's a simple problem, like, so…
maybe, like, a first step, like, if you… if we don't want to change the API,
so much in a single PR.
Could be to disable or enable this?
default narration, like, there are some smart steps we can take. I still think that these modes make sense.
But yeah, I'm open.
**Pellared** 19:56 But I think before you are right, if we start with the smaller one, first of all, it will be easier for us to understand, to understand the problem. Also, the people who review it will also already get some knowledge about it, so the next steps, which are, you know, more kind of complex, or a little bit more mature.
will be easier to digest for ourselves. And also, you can refer to the easiest one first.
**Nico Hertz** 20:22 Yeah, yeah, sure, no problem.
**Pellared** 20:24 So…
**Nico Hertz** 20:26 So then I create the…
sort of the explanation, and ping you guys on Slack, or maybe Sean next week.
**Pellared** 20:35 You can just… so, if you just want to…
go ahead with disabling. I think you can even create just a PR, but if you can create an issue, it's always nice to have an issue, because if you have some alternatives, is it better to discuss
it on an issue and other, you know, things which are not tightly coupled to the PR. So I just suggest to create an issue, and even after creating an issue, just start doing the PR, because I don't think it will be controversial.
Probably we'll have some conversations around naming these options, but this is, you know, just nitpicking, and overall the idea to disable it seems fine to me.
And…
**Damien Mathieu** 21:15 Keep your current PR around, just as a proof of concept of the final idea, basically.
**Nico Hertz** 21:25 Yeah, yeah, sure, definitely.
So yeah, okay then, so I create the issue, a simple issue first, which is disabling, or the fact that we can't disable it now.
And then a second document, explaining more and more staff, just as, discussion, and…
Anything else?
I think these two items… Sounds good.
Awesome.
Then, like, for… for me, as, to start, as a contributor, any… any suggestion, like, like, small bugs, or I know, like, I… first PR, and it's a huge, it wasn't intended this way, but…
I'm very happy to also take smaller bags or reviews, if there are any…
**Damien Mathieu** 22:25 There are… I think there are a couple issues that need to be looked at.
If you… I mean, if you want to dig into the code, we currently, at least in Contrip, but there are also in the core repository, we have several flaky tests in Contrip that are very boring.
And so, there are issues for both of them, so if you want to take a look at that, that's definitely something that can be looked at.
**Nico Hertz** 22:54 Okay, perfect. I'll take the look.
Thanks.
**Damien Mathieu** 23:03 I don't know, do we… does anyone else have anything else they want to… to bring up?
**Pellared** 23:11 have some good first issues, or need help issues, which you can look. Also, PRs which are open. Even if you look at the submitting notes, you can see that last time, it was,
It was not followed here. So, I'll just call out one more thing.
I try to also keep seek meetings notes after the discussion, after the meetings here.
after we have the transcript, so basically, LLMs are helping us to generate it. So, for instance, here you can see that after the last Sikh meeting, there was an ask to review some AutelConfRC support PR, which is basically in GoConstrip.
yeah, there were some PRs to review the sync map histograms at the Exemplar Reservoir, so these are PRs on, on AutoGo, so if you want just to know what's happening now, you know, just to, to
to be more in the loop, you can look at these ones, but if you just want to ad hoc look at something, just look at the open… at the issues. So, it's your preference, you can, you know.
Spend an hour and look around, and then decide what is the best for you.
I'll put this to the chat.
It's also… I think it's also pinned. It should be pinned, by the way, if you go to the issues.
Yes, this is Pint here.
So it should be easy to find.
**Nico Hertz** 24:40 Hmm.
**Pellared** 24:44 Oh, no.
Okay, any other comments or questions to Nico? Or Nico, do you have any more questions?
Any other topics?
Mikhail Bryan?
Are you… you're here the first time, or…
**Michal Jarmolkiewicz** 25:05 Yes, yes, exactly. I'm here, first time, I just came to, like, introduce myself.
And basically, ask if anyone needs some help, and with any task in any review, I can gladly help with it.
**Pellared** 25:22 Yeah, we'll need a lot of help, we need a lot of reviews, etc. So, question, do you need a buddy, or do you want to take your time? Do you want me to write to you on Slack? Are you a CNCF Slack, by the way?
**Michal Jarmolkiewicz** 25:34 Yeah, yeah, I have a Slack. Maybe, you know if I can have a buddy that can guide me through?
Like, you know, just tell me exactly which task to do. Yeah, and just a few… give me a few hints on how's the workflow here, and all the stuff like that.
**Bryan Boreham** 25:57 And, hello? Not my first time. I do have… I sort of have a bit of a habit of asking stupid questions, and I have a lot of…
**Damien Mathieu** 26:05 There's no such thing.
**Pellared** 26:07 Just from your… not from you, at least.
**Bryan Boreham** 26:10 So, some… well, a colleague was asking about Kafka instrumentation, and so we… we came across… there's…
there's one, auto-instrumentation in OpenTelemetry Go for Kafka. There are four…
auto-instrumentations in OpenTelemetry Go. And so the question is, why are they not in Contrib?
**Damien Mathieu** 26:36 So, there used to be one for Sarama.
It still exists, but we were lacking contributors, so we deprecated and removed it, and the Shopify folks took it over onto themselves, so now the Sarama instrumentation is directly under Shopify.
**Bryan Boreham** 27:00 Okay, now, but my question is more, why are these four things in OpenTelemetry Go?
They don't seem to have any particular pattern. Is this, like, maybe somebody showed up and
made a PR, and…
**Damien Mathieu** 27:12 Four things for Kafka?
**Bryan Boreham** 27:14 No, for auto instrumentation… let me find the link.
**Damien Mathieu** 27:17 Oh.
It's, it's a tricky story.
Yeah, the ca- the number of…
auto instrumentations is basically because, there has been a lot of, donations from eBPF to Auto Instrumentation staff.
I think there are some attempts to bring them back together, but I'm not sure.
Actually, there is a auto-instrumentation, go auto-instrumentation, SIG meeting, that's… I think it's tomorrow morning.
**Pellared** 27:52 I'm not sure if it was not, like, 2 hours ago or something like that.
**Damien Mathieu** 27:59 It's tomorrow morning EU time. No, it was this morning, sorry. It's at 8 AM GMT on Thursdays.
No, not very US-centric, sorry.
**Bryan Boreham** 28:14 Yeah, so I found… I found the page I was talking about. I mean, so 3 of them are in… well, 2 of them are in the Go standard library, so… so there's maybe… maybe there's that argument. One of them is gRPC, again, a very central thing. But the fourth one is this…
like, segment I.O, Kafka, go…
which is one of 20 Kafka libraries, you know, what… I just… the question is, why is it… why is it singled out as to be, kind of, to have this special place?
**Pellared** 28:45 Okay, if I remember correctly, the segment I.O. is because it was one of the first donations where co-instrumentation was there, and I think Odiegos had a client who basically asked for it.
So, it's basically just, you know, when it was first won, we just wanted to have any adoption, and even though this library was not popular at all, but there was someone who wanted it, so it was, you know, we get some clients who wanted to try it out, so, yeah, let's do it if we have any, you know, reception.
**Bryan Boreham** 29:15 Right.
Yeah, no, okay, thanks, that answers the question. I mean, it makes sense, and,
By the way, I made a PR to add it to the registry.
**Damien Mathieu** 29:27 And to be fair, this group is focused on the Go SDK, not really the auto transportation. Tyler is not here today because of Thanksgiving, but if you come back next week, he will definitely be able to help you more there.
**Bryan Boreham** 29:41 Okay.
I didn't realize there was a separate group. Thank you.
**Pellared** 29:44 There's… there's, I think, also a third one, because right now there's also EBPF instrumentation, which is like OB.
**Damien Mathieu** 29:53 APIs, something like that.
**Pellared** 29:55 OBI, or OB? Yeah, OBI. Which basically kind of merges Go instrumentation, and I think networking is part of networking instrumentation, and it also supports Rust, some C++, and maybe some other libraries, so the idea is that they basically maybe have one eBPF, you know.
Component instead of having 10, or each… for each language, so yeah.
A lot of things happening here.
**Bryan Boreham** 30:25 Okay, thank you.
**Damien Mathieu** 30:28 And to be fair, I think because of
how Go is architected with its static nature, auto-instrumentation is tricky, because it can actually happen through monkey patching or dependency injection, and so that's really why
you have so many possibilities. I don't know if it's still used, but when it started, there was, like, the current one that's using, like, auto-instrumentation with eBPF, and there's another one that, like, auto-updated your code to manually add instrumentation.
**Pellared** 31:03 compile, which uses GoCompile instrumentation, right?
**Damien Mathieu** 31:07 Yes.
**Pellared** 31:07 This is the go-tool train, compiler tool train.
**Damien Mathieu** 31:10 So, yeah, it's…
it's… yeah, I agree, it's tricky and hard to really understand which one to use at the moment.
I would really join the Go to an instrumentation SIG meeting if you have more questions.
**Bryan Boreham** 31:27 Thank you.
**Pellared** 31:28 You can also ask on the Slack channel, there's a dedicated one called, AutoGo Instrumentation. So our is AutoGo, and there's a separate one.
dash instrumentation, which is not about instrumentation service, it's about automatic instrumentation. This is kind of a confusing name, but it is just a legacy that there was a pattern that Java instrumentation was for automatic instrumentation, so for .NET.
Yeah, thanks, Damien.
Oh, we won't.
You think me?
**Damien Mathieu** 32:00 Actually, I think I gave you the wrong one.
**Pellared** 32:16 Damon, do you have maybe some other tips for Mikhail and Yuko?
Because I would only probably suggest looking at the contributing MD, if you have some time. There's, like, a few things about our style patterns, but maybe that means something comes to your mind.
**Damien Mathieu** 32:32 I mean, yeah, I would definitely recommend looking at contributing.md, possibly issues or open pull requests, just looking at how things are being done.
We are very much, I know not every open source project is onto that, but they are very much into atomic PRs, so pull requests that to one thing and just one thing. If you say end in your PR, it probably should be two PRs.
And so that really means lots of PRs, but also it's much easier to review each of them.
we have…
Plenty of open issues, but not necessarily tagged with first good contributions. So, yeah, look at the recent ones.
And if you feel like one of them,
If it seems interesting to you, look it up.
**Michal Jarmolkiewicz** 33:29 Okay, thanks for our advice.
**Nico Hertz** 33:32 Thanks, and just a comment, I'm thinking this, or open the PR, like, if I see some issue that I'm interested in.
**Damien Mathieu** 33:41 If you have a fix for an issue, just open APR, yes.
You can ask to be assigned on the issue, but that's not mandatory.
Just if you see that Anover PR is linked on the issue and already open, don't work on that issue.
**Nico Hertz** 33:57 No idea.
**Pellared** 33:59 But sometimes, you can double-check, because sometimes people create issues, they receive comments, and they got stale, and we forgot about closing them, and
unassigning the issue. So, even if an issue is assigned, it doesn't been that it is up-to-date. We are not doing a good job with unassigning people from the issues.
**Damien Mathieu** 34:21 If you want, kind of Toyota work, you can go through all assigned issues and see if they have not been updated in a while and do not have an open PR, then you can ask the person if they are still looking into it.
**Nico Hertz** 34:37 Okay.
Thank you.
**Damien Mathieu** 34:42 Okay, is there any other unrelated question, or, I don't know, a nice use of the Go SDK in the wild?
It's…
end of November, so it's a bit early, but in case you didn't know, OpenTelemetry is doing an event on the Monday after FOSDEM in Brussels. It's February 2nd, I think.
I will be there, if you happen to be around Brussels and Belgium at that time. I think it's gonna be a nice time. It's not a conference, it's an un-conference, so the idea is there are no set subjects, and we define the subjects during the day.
**Nico Hertz** 35:35 I may read far, but sounds good. Maybe… Aye.
And I'm not sure if this time, but maybe sometime in the future.
**Damien Mathieu** 35:48 Okay, have a good evening, then? Or day.
**Pellared** 35:53 Yeah, thanks for the meeting. See you guys!
**Michal Jarmolkiewicz** 35:56 Thanks, boy.
**Nico Hertz** 35:57 Right.
