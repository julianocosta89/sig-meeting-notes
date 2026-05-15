SIG: Python SIG
Date: 2026-05-14
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:02:06 Hello.
Diego Hurtado Pimentel 00:02:10 Hello?
Nope.
Erdenesaikhan Tserendavga 00:02:15 Hello, everyone.
lciukaj@splunk.com 00:03:36 Hello, everyone.
davidperez 00:03:39 Hi.
How's it going?
lciukaj@splunk.com 00:03:44 Good.
How are you?
davidperez 00:03:47 Doing well, doing well.
lciukaj@splunk.com 00:03:50 haven't been here for a while, I think it was, like, 2 years ago last time, when I joined PythonSig, so…
davidperez 00:03:58 Oh, nice, nice. This is, this is my second meeting, Ever. But it's good to meet you all.
Welcome back.
lciukaj@splunk.com 00:04:09 Likewise, yeah. Happy to be here.
I was more involved in end-user SIG, so… now, switching slightly towards the Python.
davidperez 00:04:19 Awesome.
Aaron Abbott 00:04:25 Hello everyone, how's it going?
Riccardo Magliocchetti 00:04:34 Aaron, can you run the meeting, please?
Aaron Abbott 00:04:37 Yeah, sure.
Riccardo Magliocchetti 00:04:38 Thanks.
Aaron Abbott 00:05:17 Alright, I guess we can get started. I don't know… Let me share my screen.
Tammy, are you around?
Did the triage.
Tammy Baylis 00:05:28 Hey, everyone. Yeah, I… I can't really share a screen, though, but if, if you, Erin, can show the board, and I… I do have one, PR I want to… Mentioned kind of as part of triage.
Let me see, where is it?
Alright, so I have linked, PR from the core repo 503.2 That… I just wanted to briefly… Oh, where is it?
Thank you.
Aaron Abbott 00:06:16 Hmm.
Go ahead.
Tammy Baylis 00:06:19 Yeah, thank you. So this one's been open for a while, and, and, OP Krishna, he's been quite, quite diligent with this PR, getting back to all our feedback and stuff like that, including the, changelog issue, and… I think, for those of us who've really looked at the exporters before, I think it'd be great if we could have a look, because, OP's done their due diligence and put in an issue with the spec, and I'll comment on the ticket later.
what I'm about to say, but there is an open spec issue.
It's an opt-in feature, and it's an approach that's different from the existing metrics batching logic from both gRPC and HTTP exporters, because it's… More of a reactive unhan… reactive handling of unexpected 413s, and… Yeah, I think they brought up some good points, but yeah, I'd like us to take a look, because this has been open for a while and actively worked on.
Aaron Abbott 00:07:32 Okay.
So maybe I'll just add this to the agenda? Does that sound good?
Tammy Baylis 00:07:37 Okay, sure.
Aaron Abbott 00:07:39 Okay.
Yeah, thanks for raising this one. If you could, Tim, if you could leave, like, a… maybe it's already there, but a link to the spec discussion?
Yeah.
Tammy Baylis 00:07:49 I'll do that right.
Now, where are we at?
Aaron Abbott 00:08:00 And I put it in the agenda.
Tammy Baylis 00:08:02 Thank you.
Aaron Abbott 00:08:04 Okay, yeah, we'll go.
Tammy Baylis 00:08:07 to the board.
Aaron Abbott 00:08:08 Yeah.
These are peers. Yeah, Let me know what I should… what I should do, Tammy. You want me to…
Tammy Baylis 00:08:27 Yeah, yeah, scroll… scroll to the bottom of no status, and maybe, we can take 3 more minutes of the 5-minute time box to see what might be ready in no status to move to ready to review.
Aaron Abbott 00:08:41 Okay. Cool.
I'll just open some of these up.
I wish you could, like, preview the PRs without… Opening it up separately, but… Okay, we have this one.
I feel like I saw a similar… PR already, I think… I don't think Leighton's here, but he was… he lost some comments on it.
Anything to say here, Tammy?
Tammy Baylis 00:09:08 Oh, yeah, I listened to it last night.
There's quite a few being spun off of the linked issue. I'm not sure what's going on there. Maybe some bots.
Aaron Abbott 00:09:18 Yeah.
Did they… yeah, they didn't leave a comment on there. Okay. I mean, if it's a… it's just a straight duplicate, I'd recommend we close this one. What do you think?
Tammy Baylis 00:09:33 Yeah, I think that's fair. Any objections?
Thanks, Erin.
Aaron Abbott 00:09:41 Yep.
Let's take a look at this one.
Oh, this is… so this is the issue.
Tammy Baylis 00:09:51 Yeah…
Aaron Abbott 00:09:53 I'll just leave a comment on here, Alright, we'll see if people respond to that.
Somebody let me know when we're at timeboxed, but I'll just keep going through.
Marcelo’s Phone 00:10:14 Thank you so much, flexibility.
This shouldn't miss.
I am so confused.
Tammy Baylis 00:10:21 One more, one more minute.
Aaron Abbott 00:10:24 So I think… I don't.
Marcelo’s Phone 00:10:25 Oh, sorry, fuck, sorry, yeah, my bad.
Aaron Abbott 00:10:27 Okay.
Tammy Baylis 00:10:28 Oh, girl.
Aaron Abbott 00:10:32 Alright, this one, ad optionally should be client response body size.
The sun's great.
Yep, okay. They updated the changelog, I think, this one, so should we move it to, like, needs review, or ready for review?
Tammy Baylis 00:10:47 Ready for review, yes, thank you.
Aaron Abbott 00:10:49 Yes.
Okay, we're done.
We're done okay.
Tammy Baylis 00:10:53 I believe so. Thank you, Erin.
Aaron Abbott 00:10:56 Alright.
Cool, let's go back to the agenda.
Okay, what we're working on this week… yeah, I don't think we need to go through this one, but… Just go straight to the topics, then.
And I guess I'm up.
Oh, also, folks, please add your name to the attendees list if you're around. It's nice just to know who is in the call.
And we can… we can drop a link to the doc if anybody needs it in the chat, but… Yeah, this… this one, I think, was from last week, this is from me. It's a little bit freeform.
And I think we actually have made some progress on some of this stuff already, so… I… I just wanted to, you know, check in on the contributor experience for everybody.
Kind of on behalf of the maintainers. I know there was a lot of PRs that were waiting.
Maybe a little over a week ago, there was, like, over 50 in the… Project board that we're… Kind of just waiting for maintainers.
So I think we made pretty good progress through that.
I know also the changelog… so we did the changelog different changes, which added Town Cryer, so thanks, Emilio and Mike for that.
I tried setting up the GitHub merge queue, we need a couple more… Things here, so… I think it was called Merge… I forget the exact thing.
But the GitHub actions were broken.
Mike Goldsmith 00:12:27 I think it was Merge Update, something like that.
Aaron Abbott 00:12:30 Yeah.
Yeah, it's kind of crazy, but it seemed a little invasive to actually fix this, because the payload of the… of, like, the… check body is very different from the pull request, so… I think… we could simply just skip some of the checks, which don't work. I think the CI ones would be fine, but the changelog and check links… From what I've seen, they don't… they wouldn't work because they have to go and look at the diff.
Yeah, I'll continue working on that, but yeah, I guess the greater kind of goal here is just to make… make it easier for us to merge PRs in, like, a timely way, and also just… to get feedback from people on other things that could improve the contributor experience, I think.
Yeah, I really appreciate all the reviews and the work that everybody puts into this, so I want to make sure it's, You know, like, a fun and good experience for everybody, so… Besides these things, I kind of wanted to open it up.
See if anybody else had feedback or suggestions on improving the contributor experience.
And if not, that's okay, I have a couple more things I can blob about, so… This one, I think we did for GenAI, so trust me, this cool… dashboard. I think it might be a little bit duplicative of, like, the project board we have.
I think, Mike, you have a lot of context here. I don't know, what do you think about doing something like this? Would it be helpful for Python?
Mike Goldsmith 00:14:20 Yeah, I think it is good. I think the thing that I like about this is that it shows the… who's been assigned, if someone's been assigned, say they want to take ownership of it, but then it clearly identifies whether it's waiting on maintainers, waiting on the contributor, or waiting for approvals from the approvers group. So it's a little bit easier It's like, it does the natural grouping for you. I think it's very similar to the board, so I think I wouldn't be upset with having both, and then you've got a preference of which one you look at.
But yeah, they serve similar issues… similar purposes, but just in a slightly different format.
Aaron Abbott 00:14:56 Okay.
So I think the lift is pretty small, so maybe we could just do this. I think there's… there's already this Python script that Trask wrote, so… Unless anybody has objections to that, I think, just… Right up.
Cool.
And then I think one other thing I had, I could mention just from the project board, like you mentioned, Mike, this waiting on maintainers is actually kind of useful, so I think what I found with a lot of the ones in the project board here was… the approved PRs that need… sorry, I'm sorry. The approved PRs column, they're kind of de facto waiting for maintainers, either to move them to ready to merge, or to kind of give more feedback. So I think… like, a lot of them, I, you know, they had 2 approvals from approvers already, I don't think they really needed any Feedback from maintainers, so… the kind of idea I had was, when people open issues, If, like, we could get a consensus on if the contribution is accepted, or… as long as the contribution or the basis of, like, the idea that's being implemented is not controversial, we could just go ahead and move them right to, oh my god, it keeps moving back.
move it right to ready to merge once it has, like, the requisite number of approvals.
And I think that would make it easier to just stick them in the merge queue and not have to… Let them live in this approved column forever.
Mike Goldsmith 00:16:35 I think it'd be interesting to define what is then required for deciding whether it's just approved and you want Maintainer, like, a review on it as well.
Because just having two approvers is that enough all the time? Like, I get that it's then… it's open to discussion of, like, is it two approvers, isn't it fine to move to MergeQ, or is it something that you… like, there's a certain criteria that you need a maintainer's input on before you feel as though that's ready to do that. Having guidance on that would probably be useful.
Aaron Abbott 00:17:10 Yep.
We can work on that. Ricardo, any…
Riccardo Magliocchetti 00:17:16 Yeah, like… for me, like, I prefer to have, like, the… To consider ready to merge.
Something like a maintainer has taken a look at that, and is willing to press, The button to merge, or to add to the merge queue.
More than it has to approve… approve us already.
Aaron Abbott 00:17:51 So was… did you have, like, a… basically working as intended, Ricardo.
Is that what you're saying?
Riccardo Magliocchetti 00:18:02 Yeah, like… like, I… I was just describing as I see the… like, as I consider that column.
on the board.
So it's like… like, I won't promote automatically… PRs once we have the two approvals.
But I'll wait.
For a maintainer to… To be willing to… to take a look and press the… Merch, but yeah.
Aaron Abbott 00:18:34 Okay.
That's fair.
Okay, I don't want to take too much time here, so unless anybody has some last-minute thoughts, maybe we can move on to the, Actual people's agenda items.
Sound… sound good?
Okay, great. With that in mind, I think, Diego, are you around?
Diego Hurtado Pimentel 00:18:59 Right, thank you, Aaron.
Aaron Abbott 00:19:01 Yes.
Diego Hurtado Pimentel 00:19:02 Boom.
Aaron, can you open that link, please?
Thank you. Alright, so… there is this, feature in the injector.
Oh, no, let me… Start again. So there's this project, you know, the injector that, aims to provide automatic instrumentation by just, installing Python packages, using Like, Debian packages, or stuff like that, right? Stuff that you style with ABT, or JAM, or… And the… right now, it doesn't support Python automatically.
So I'm collaborating with this. I just started, Yesterday, so I still don't have much context. I was going to ask you if, any of you have, more information regarding, why don't, we have, file support. But earlier this morning, I just received, some more Slack messages with more information.
So, yeah, pretty much, I guess, I'm just gonna let you know that I'm working on this. Ricardo, I think you… Well, for your hand raised.
Riccardo Magliocchetti 00:20:28 Yeah, like, I think that… like, as far as I remember, there was discussion in the… Inject… injector, Zach channels… like, the maintainer of this were afraid of the protot dependency.
Diego Hurtado Pimentel 00:20:45 What the fuck off the fence.
Yeah, that's something…
Riccardo Magliocchetti 00:20:50 Yeah.
Because, like, I have, like, But the experience with that, like, breaking, Like, a mismatch of, protot version breaking, instrumented apps.
And so, for memory, we… like, not having an exporter, a protobuf less exporter was a blocker for them.
Diego Hurtado Pimentel 00:21:17 Yeah, I saw some messages, regarding that, about, I think, gRPC being a dependency that may… may break some apps. But yeah, I'll be working on this, So… Right now, Yeah, so as I just mentioned, I was going to ask you if anyone of you had more context, but since now I have more context, I guess I'm just gonna… But you know that I'm… Gonna be working on this.
So, thank you.
Riccardo Magliocchetti 00:21:52 Yeah, let me add that I think we have already an issue on the OpenTeametry Python repo, and the discussion on… on the very same issue. Like, I don't remember the specific issue name.
But I remember, but… At least Lucas took a stab at this.
By creating, Like, we… I think he created, an exporter using the Rust protobuf implementation.
And so we don't have a runtime dependency.
On the protocol package.
Diego Hurtado Pimentel 00:22:36 Okay.
Riccardo Magliocchetti 00:22:37 And I can search for the issue.
Diego Hurtado Pimentel 00:22:40 All right If you can, send me that issue in via Slack, I'll… Appreciate that.
Alright, that's it. Thank you, Aaron.
Aaron Abbott 00:22:56 Cool.
That's exciting. Glad to have somebody working on that.
Okay, next one, Lucas, you're on?
lciukaj@splunk.com 00:23:05 Yes, that's me.
Thanks. So, yeah, so I would like to ask you, what is your opinion about that, proposal that I have, this enhancement? So, I was discussing that internally with Pablo. I believe Pablo is on the call here.
With us, so we're discussing that, and to give you a little bit of the background, so I'm working mainly with manufacturing customers, with industrial customers, and… there is definitely interest in expanding open telemetry in that area, so that's kind of my personal mission. I'm trying, you know, to… I'm working on a couple of initiatives in that area, and one of them is about providing auto-instrumentation for OPC UA. So for those of you who are not aware what OPC UA is, it's like a modern, lightweight protocol which is used in industrial networks, so currently, like, the PLC manufacturers are including OPC UA servers natively, so you can connect to them in more, like, a client-server way, like, as we know from applications. So there is, like, definitely, like, the digital transformation going there, part of Industrial 4.0 initiative. And in Python, apparently, is one of the most, or growing languages that are being used for adopting OPC UA in that environment. So, my idea here is to provide auto-instrumentation capabilities for async UA, that is the Python library, which is also kind of growing with many GitHub stars and many contributors.
So, I already have, like, prototype of that in my repo. I tested that, like, end-to-end, even I spent some time experimenting with that, so I have a working solution, but Pablo told me that maybe better to discuss with the community before submitting PR, and maybe do it in more, like, baby steps with some, like.
simple instrumentation for just one span in the OPC or async U way, just to make sure this is working, and then maybe move forward if there is, like, approval from the community. So I just want to get your opinion on that. If this is something we would like to continue here, if that makes sense, I know that you're your board is full of other PRs, lots of codes to be reviewed, so I would like to get your opinion. What do you think about that?
Aaron Abbott 00:25:35 Yeah, yeah, super cool.
And thank you for writing up the, the description here. So I think I had two questions. The first one is, do we have, any semantic conventions for For this, I'm not very familiar with this space.
lciukaj@splunk.com 00:25:51 Yeah, that is… that is a good question, and I also included that in the issue text, that we don't have a semantic convention. That is something, actually, I'm thinking about also starting some initiative. I already opened the issue on OpenTelemetry Community to get a couple of other folks who are working in that area, because I'm not sure if we need to… if you need the semantic convention for OPC UA, I'm thinking more about semantic convention for other industrial protocols, like, more in the bundle, like, maybe ModeBus and OPC UA, and some others, like, try to generalize it somehow, and then we could take it from there. But as of now, we don't have semantic conventions for this.
Aaron Abbott 00:26:36 Okay, yeah, cool. I think… yeah, okay, perfect. I was gonna ask… I don't know who put their hand up first, but I was gonna ask.
Ludmila Molkova 00:26:44 Ricardo was first.
Aaron Abbott 00:26:46 Yeah, go ahead, Ricardo.
Riccardo Magliocchetti 00:26:49 what… I was going to ask, the semantic question, and then, Are you… like, have you tried to try to contribute, an instrumentation directly into the… Into this package, instead of in our own trip, because, like, since, like, we have a lot of Backlog, and we don't have specific knowledge of All the libraries we have instrumentation for.
Some… since this is, like, really, like, vertical on… On a s- on a, like, a market and, like, specific technology, like, maybe it is better to have it Nia.
The code, this traumatic code, more than… I don't worry.
lciukaj@splunk.com 00:27:38 Not yet, Ricardo, but that was the feedback I got from Pablo as well, to check with async UA folks if it would be possible to implement it natively in the library, instead of, like, having wrappers here from the Python perspective.
I don't know, I need to reach out. I was about to open some issue there, but I need to do it, like, next step.
What they think about it.
Riccardo Magliocchetti 00:28:12 Thanks, Ludumina.
Ludmila Molkova 00:28:16 Yeah, things are… so, it seems you do have semantic conventions, you just don't have them documented anywhere except this, this, issue, like, the attribute names you're mentioning. This is their, they're semantic conventions. I think the… The normal law would be that you… it would be cool to propose it to to be native instrumentation. Native instrumentations might be hard for people, because they need to take dependency on open telemetry, but it could be an instrumentation library that leaves next to the original package or packages, and then it's… I think it's called first-party instrumentation. It's like a plugin, and this… this approach can be easier for Library owners to… Consider.
And when… like, hopefully it works, and then it's probably up to the, I'm not a pipe maintainer, don't take me as an authority. It's up to maintainers to decide whether this can live in this repo.
If it does, in Python Contributory Python country, then, the semantic conventions, it would be pretty much impossible to contribute anything to semantic conventions now, unless there is a SIG for it, that's cross-language, maybe cross-technology.
It's… it's a long pass.
It should not be a blocker, though. We can have conventions documented Somewhere else, or here.
But then it creates some additional… Questions on… how it works across languages, and so on. But, I mean, this can be taken step by step.
lciukaj@splunk.com 00:30:08 Yeah.
So something I'm confused a bit, so maybe someone can explain to me, so what would be the difference of having this native instrumentation in the async UA library versus, like, the instrumentation package as part of the OpenTelemetry Python contrib?
Aaron Abbott 00:30:28 Yeah, so…
Ludmila Molkova 00:30:31 -Oh.
Aaron Abbott 00:30:32 Yeah, so the difference would basically be that the code would be directly in this repo. So, you would add a dependency on OpenTelemetry API here, which is very lightweight, and then you would, you know, add the calls directly as if you had written the code in your own application.
lciukaj@splunk.com 00:30:48 And… but this is not, like, auto-instrumentation in that case, right? So, like, developer of this async UA would need to, like.
Do it manually in the code, correct?
Aaron Abbott 00:31:03 Yeah, that's right. What do you mean by it's not auto-instrumentation, though? Like, is the goal to have it out of source?
lciukaj@splunk.com 00:31:09 Yeah.
That's what I was thinking.
Aaron Abbott 00:31:12 Yeah, I mean, that's the main trade-off, so I… I… I'm curious why you would want it out of source if… like, I don't know if these maintainers would… would accept that, but, you know, typically, I think that's the vision of OpenTelemetry, is that everybody will… kind of like how logging works, you know, like, you just set up loggers, and then everything magically works.
lciukaj@splunk.com 00:31:33 Okay.
Lukas 00:31:36 Just to add something with the native instrumentation, like, if you wanted to get it to work with auto instrumentation, like, you can always add your own entry point, So that it gets injected.
And probably the best way to do this is to have it as a separate package, like, installable as an extra, and then in your… the main package, you'd only depend on API, and then Extra would pull in everything else and do all the auto-configuration if you wanted to do that.
lciukaj@splunk.com 00:32:08 Okay.
But then it can be either part of Contrib, or it can be, like, a separate project, right? External project.
Lukas 00:32:17 I mean, also the benefit with it being native is you're not relying on… we do a lot of monkey patching, which can be unsafe.
So, like, you want to avoid that, and then I think the other point being made here is that this is very domain-specific, so… Having it in this repo With people that are knowledgeable on the topic is preferable.
So… Yeah, I think that's… that's just the… what the points people are making here.
And then there's also the topic of, like, popularity, Which I don't know if that was brought up, but, Like, we want to make sure the package is popular enough so that It's continued to be maintained in the contribute boat if it were to be added.
lciukaj@splunk.com 00:33:07 Okay, sounds good. Thanks for clarifying.
Alright, so I think as a next step, I will reach out to that folks and check with them what they think, if that makes sense.
To include that natively in that library.
And the OpenTelemetry capabilities.
However, for me, like.
I'm more like end user. I don't consider myself… don't consider myself as a developer, so I'm… I'm more end user, so… having… The auto instrumentation or the package that you can just attach is always a benefit, like, instead of… messing with the code, so… Anyway, okay, so thanks for the feedback, I appreciate that. So, I will take it from there, I will open the… an issue to a CDA, group, and let's see what they think about.
pabcolli 00:34:05 Yeah, I just wanted to say, I think there's… there may be an intermediate solution where async UA, instead of writing to the OTEL API, they could introduce some callbacks, some sort of formal functionality that we could hook into, that an instrumentation could hook into, rather than monkey patching.
But I also wanted to say that I'm, am definitely on board.
to… Help maintain and review.
This package, if we wanna… If we want to host it, in contriv. But, Yeah, so hopefully we'll hear back from the ACNQA folks and, maybe report back.
lciukaj@splunk.com 00:34:51 Thanks, Pablo.
Aaron Abbott 00:34:58 Okay.
Cool.
Let's move along, then. Ricardo, you're up?
Riccardo Magliocchetti 00:35:06 Yeah, it was just, like, a budget question. Like, I've seen, But all the instrumentation JNA IPFs were closed.
But we are still… I think, the OTNA package in Contrib.
And someone's wondering if… Is that supposed to move as well, or… Not.
Ludmila Molkova 00:35:32 Yeah, it's just, I need some help if people have any capacity, people who work on GenAI to We need to remove things that… will continue its life in New Repo.
And we… for the packages that we are going to rename.
We'll need to… before we move everything out, we need to release the last version of it.
So that we update the docs on PyPi and point to the new location. So it might happen in a few stages, but do we have people who work on Gym AI here, beyond me, and… There, Randy.
Mike Goldsmith 00:36:20 over here.
Ludmila Molkova 00:36:21 Ladies, then Mike, then Josh, and a lot of other people. Can we start doing this?
Mike Goldsmith 00:36:32 Yep.
Yeah, I created a migration issue in the new GenI report, and this includes doing… Naming which libraries we want to move across, and what sort of things we need to do with them, so… Yeah, the bootstrap one, so I've started to do some things in there, and yeah, we can make sure that we do… I can't remember if I put in there that we need to do a final release, but it should be on there, as part of the migration process.
Ludmila Molkova 00:36:59 Yeah, thanks. Suri is asking if we can do it as a large bulk PR, a small PR. I think we have to do it in multiple PRs, because We can… we cannot just drop everything at once, because we still need to release the last version of it.
Of some of it.
Like, OpenAI agents. I think we can just go ahead and remove packages that never were released.
I think… There are a couple of them, at least.
Because they're already in the new repo.
We cannot just remove OpenTelemetry OTL GenAI, because these other libraries depend on the local Version of it for testing.
We can… rare.
We can change it.
Right, we can… if we release a new version of Open… like, so there is a lot of coordination that needs to happen before we can move everything out.
That's what I'm saying.
Riccardo Magliocchetti 00:38:02 Thanks, by the way, like, I'm not asking like, not pushing this to be removed, that was just, like, a question, like… So, take your time, we have no hurry, I guess.
Ludmila Molkova 00:38:15 I think it's important, because it creates confusion, and it potentially creates situations where people will assume one and… well, essentially confusion. So I think it's… it's important for us to clean things up as soon as possible.
Aaron Abbott 00:38:33 Okay.
So maybe we can, we can update this issue.
And kind of once we're agreed on the plan. I mean, we could always just update the READMEs.
To make it clear what the plan is, you know, like, hey, this thing will be removed at some point, and then link to this bootstrap issue, or something like that. That sounds good.
Mike Goldsmith 00:38:53 Yep.
Yeah, I can do that, I'll do that tomorrow. I'll update this, and I'll… I can at least do the README updates and make sure we've got a process for doing the migration from Contrib to this new repo.
Ludmila Molkova 00:39:04 Thanks a lot.
Aaron Abbott 00:39:05 Awesome.
Right.
Anything else there, Ricardo? Good to move on.
Riccardo Magliocchetti 00:39:13 Thanks, of course.
Aaron Abbott 00:39:15 Great. Okay, we have your rounded media?
Emídio 00:39:20 Hey, yeah, I believe, don't remember when, but we discussed about using Renovate instead of the Pinabot.
So I created this PR with a configuration that I believe is, is a good start point for us.
The main, The main thing here is, we can have some paths to ignore, like with, requirements.txt files, we don't want to track.
And another thing is, for example, today, GitHub Actions workflows we… we… we can't merge the… the PRs, depending on what creates for those workflows, because we generate workflows using the talks.generatedWorkflows, right? So, see, I always fail with that.
And with Renovate, we can just do a regex.
To update those files well, if you… if you open the… if you can open the files.
You can see.
The first thing, yup.
Yeah, in line 26.
Yeah, line 26, we're saying, like, for GitHub Actions, Manager.
you also update the Ginger 2 files.
Aaron Abbott 00:40:45 Nice.
Emídio 00:40:45 and say I won't fail.
Yeah, this is a pretty basic configuration, grouping all patch versions, mineral measures, and grouping docs and CI dependencies in one pull request to make our life easier.
Go ahead.
Aaron Abbott 00:41:05 That's the biggest one for me, is… Especially because… I mean, maybe it'll be better with the merge queue, but it's nice to have… Some of them grouped together, in my opinion.
Emídio 00:41:18 Yeah, I have, there are some, paths in the ignored list, like, benchmark. Benchmark requirements.txt files.
and dev requirements as well, but I didn't want to introduce a lot of PRs at this moment.
We can reveal later if, everyone is okay.
Aaron Abbott 00:41:45 Yep, Ricardo?
Riccardo Magliocchetti 00:41:47 Yeah, quick question.
And, like, Is the renovator a bit smarter and dependable to them?
Like, it's able to handle the… like, in a couple of packages, we have the pattern where we recreate the latest and lowest, requirements files from, a source one, is it able to understand that, and… Try to act on that.
Emídio 00:42:15 Yes, if we take a look on line 12, there is a log file maintenance.
that's the way, Renovator works, with log files. Like, we are using UVP Compile to generate the log file, right?
So, it can understand.
Riccardo Magliocchetti 00:42:33 Nice.
Thanks.
Emídio 00:42:38 Yeah.
Yeah, please take a look, and if you are good with the configuration.
And we can, set up, set up Renovate.
Aaron Abbott 00:42:50 Yeah.
Emídio 00:42:51 Amazon. Yep.
Aaron Abbott 00:42:52 Yeah, I was gonna ask the same thing as, Ricardo there, like, so does it parse this comment, and then it knows how to do it, or, like… Yeah, Python's a bit of a mess, I guess, is what I'm saying, so I'm not surprised if some of this stuff doesn't work.
Emídio 00:43:07 Yeah, my understanding is that it, it can underst… it can, parse this… Including the UV.log format as well. I believe it's the PAP6.1 standard, yeah.
Okay. I'm not 100% sure, because I didn't… I don't know, how the PRs would be opened, but… I know that there is a support for the lock file.
Aaron Abbott 00:43:34 Bye.
So is there… I guess, like, what's the testing plan for this? Should we just, like… we could keep this and Dependabot for some time, so we… like, in my opinion, we could merge this, and then see what happens, and play around with the config, and… I guess the alternative would be if you wanted to try it on a… on your fork or something like that. I was just wondering if we have, like, a testing plan.
Emídio 00:43:56 Yeah, I've… I have agreed on my fart out there.
Yeah, you can send a description which files… are being tracked.
Oh, God.
Aaron Abbott 00:44:13 Basic, ginger files. Cool.
Emídio 00:44:16 Yeah, the test requirement's latest, so there's…
Aaron Abbott 00:44:21 Yeah.
Well, hopefully, yeah, hopefully these ones work, because… like, I wonder… I think we also have some .in files in Contrib that are used to generate the oldest and latest, but, you know, like, I'm not… I'm not super married to those either, so if we can make it work better… it probably has better support than PandaBot, from what I've seen, regardless, but… Yeah, this looks good.
Ludmila Molkova 00:44:48 We're doing the renovating in Gen AI repo, and it's still too new to tell how all it works.
But I excluded the oldest.
Because we don't want to update dependencies in the oldest, right? They're intentionally old.
But then, it means that all the common dependencies that should not be, like, tested against version ranges. They should be somewhere else, not in this.
Latest, oldest.
Emídio 00:45:21 Makes sense, yeah. Yeah, on the package rules, we can also skip some dependencies if you want.
Like, if we don't want to bump PyTest or, let's say, eSphinx for documentation, we can do that.
Ludmila Molkova 00:45:36 Yeah.
Aaron Abbott 00:45:38 Yeah, I think there's some nuance there, we'll have to play around with it, like… We, like, we should be generating the oldest from, like, you usually have this requirements.in file or something like that, and then the… Like, in my opinion, it would be fine to keep the lowest dependencies, But maybe it's okay to update transitive ones, because I think what ends up happening is, like, if you look at our repo, we have like, one… it says 1.1 thousand, you know, dependable alerts, but most… most of these are in lock files, because we're testing these old dependencies, so… I guess either we have to live with that, or we'll have to figure out a way to make it less painful.
Ludmila Molkova 00:46:20 I mean, we need to test with… let's say, if you test it in our requests, and we support a version… a range of requests version that we instrument, right? We need to keep the… It tests for some old versions.
God.
Aaron Abbott 00:46:35 Exactly.
Ludmila Molkova 00:46:36 And I think there is a way, Trask explained, there is a way to exclude Like… like, donned fire on certain things and transitive dependencies.
Used for tests, so that it doesn't show as one key, security and quality alerts.
Aaron Abbott 00:46:59 Yeah.
Okay, so I think… let me just, like, write down here, I think we are all… unless anybody disagrees, I don't know, but it sounds like you're in agreement.
Riccardo Magliocchetti 00:47:17 Sounds good to me.
Aaron Abbott 00:47:20 Okay, cool.
Tammy, you're up then.
Tammy Baylis 00:47:28 Hey, thanks.
Aaron Abbott 00:47:29 This is the one I added for you.
Tammy Baylis 00:47:31 Yeah, I added the link below that point with the comment I added a bit ago.
Yeah, this is the issue. If we could open the other link… yes, thank you.
I've just pinged all the other approvers to take a look. There's, an open spec issue OP created to continue this discussion, and there's been no responses yet. I figure this is… Yeah, it's… it adds complexity, but it is an opt-in.
So I wanted to get other people's thoughts. I know, Lucas, Lucas Herring's already reviewed this. I've talked about it a little bit, I guess this is also one of those scenarios where, it'd be good to have… maintainers have a look, like, this is not approved yet, but there's… it's an older… the exporters are an older codebase, so it'd be good to tap into prior art in people's heads, but yeah, long-winded way of saying, please take a look at this one.
Aaron Abbott 00:48:39 Yeah, thank… thank you for raising this. So, I… I wanted to call out… I can try to dig it up, but, David, one of my coworkers, David Ashbel, He recently did some changes for batching. Let's see if I can pull it up quickly.
Which were merged, but these… these were, like, these were not adaptive, these were more, like.
adding some configuration parameters, and I think we actually already have that in the OTLP exporters. We let people choose the batch size.
So they can kind of configure it, but there's definitely some… some overlap, so I think we can… I think, like, I'll tag him on this issue and see if he has any thoughts, but… My kind of immediate concern is, like.
If it's resource exhausted, this can mean… That you ran out of quota.
And, you know, resizing the responses isn't particularly helpful there, so I think there's something already in the spec about Yeah, they're probably aware of this retry info thing where it's supposed to return.
A back-off to tell you how long to wait.
But, yeah, I think… I think we talked about this last week, but I'm a little concerned about introducing, like, foot guns, where people can figure something, and then they just make their situation worse.
And.
Tammy Baylis 00:49:55 Yeah… Yeah, I'm not sure how to… I wasn't sure how to word that, so I'm glad I'm asking you.
Yeah, Lucas, you have your hand up.
Lukas 00:50:05 I think the original issue was raised because, like, people are getting, 413s from, like, LLM spans, which can be massive, and currently we only… allow limits on the number of spans in a batch, if I remember correctly, not the total size.
So… my take is that, like, I don't think this is the right way to handle it, I think we should just add a configurable option to say, like, max export payload size bytes or whatever. The other point that… Of this is, like, if you're using a collector, it's also not really… useful, either. Like, this feels like it should be something handled in the collector itself.
Because I don't think the collector currently returns 413s anyways.
So… like… Yeah, I personally don't think it makes sense to add this, but… I do think, though, that adding a, like, payload Like, a export batch size limit would be helpful, though.
Dylan Russell 00:51:13 Like, a bite-sized limit?
Lukas 00:51:15 Yeah, exactly, instead of just a number of spans.
Ludmila Molkova 00:51:20 I think it was discussed in the spec at some point, and it's de facto impossible because the badge processor doesn't Before calling the exporter and actually serializing everything, it doesn't know.
What the size will be.
Lukas 00:51:37 I mean… I guess maybe I don't quite understand. It should be possible in the export implementation to split it into multiple HTTP calls.
Ludmila Molkova 00:51:47 Oh, and the exporter.
Lukas 00:51:49 Yeah, because it gets a… a list of… what is it, like, readable span?
Yeah. And we can just basically… Yeah, there's multiple ways to do it, but it's definitely doable.
Aaron Abbott 00:52:04 Yeah, and I think this is another thing that we have to address, because we did implement this in the exporter, but not… the spec is for the metric reader, which is why the issue that Lamila mentioned exists, but we kind of did something different, so… Yeah, I… That… does that make sense, Lindel, though, if we introduced… like, it seems bad to have batching in two places in the spec, right?
Ludmila Molkova 00:52:33 I think this is the spec question, how to do this properly, and I don't think you need to block on this.
But also… There isn't to split, there could be so many.
It's like, do you want to implement The individual solutions for specific problems inside the… Exporter.
The approach… the other approach could be that You provide enough extensibility so people can write this logic themselves?
Or if this problem is widespread enough that we need to have a common solution.
Aaron Abbott 00:53:28 Yeah.
So, I mean… Yeah, that would be good to get more signal on, like, what the… how widespread the issue is, I think.
I don't… so Adrian filed this, it looks like Adrian's still responding on the bug, so maybe we can get… Some more feedback on, like, the specific setup.
and where this is being run into, yeah, I mean, I know LLM spins, sure, but, like, if we're sending to a collector and whatnot, but, Yeah, I think… so it sounds like we should just surface this to the spec, but Ludmil, you mentioned, like, we could not block. Could you say more?
Ludmila Molkova 00:54:03 Yeah, so I imagine if we… if it's widespread.
Then it becomes this, the cross-language concern.
what can we do in the meantime? One approach is, okay, people should configure… we just tell people to configure smaller Batch size, in terms of count.
The other approach… the exporter… Allows people to re… Rebatch it. That's a bad hook.
it's probably… if it's a whole… some form of a custom solution extensibility point, that's just that people just write a different exporter, or a layer above exporter, right? It has to be inside the exporter. Sorry, it could be a custom transport, I don't… I'm in the design phase, I don't know.
Aaron Abbott 00:55:21 Yeah, I think… like, knowing that the issue is specific to Gen AI and the solutions that we've already discussed for that Libila, like, I feel like Like, we know… we already know about the problem, and that it's probably better not to send, like, a video Inside of a trace attribute, so… if that's the whole context of it, I feel like we should try to continue solving this in OTEL, because the problem's a bit unbounded. Like, we said 2 megabytes here, but it could be much bigger.
But, but yeah, maybe, like… Yeah, I agree, I don't have a good… good way to fix this, because it's just not… it's not easy to detect the size, or to communicate between the SDK and the exporters.
Ludmila Molkova 00:56:09 Yeah.
Let me, read the third issue, and I'll, try to understand whether… We can do something in the LLM space.
To me, it sounds like that… Unless it's a burning need that we actually experience with rather Bring it to the spec, and… I'm pretty sure there is an issue, I can dig it up.
Aaron Abbott 00:56:41 Okay.
Tammy Baylis 00:56:43 Yeah, thank you, that'd be great. Should I also point them towards, the GenAI SIG, if this is indeed an LLM telemetry issue?
Ludmila Molkova 00:56:55 Yeah, please do, and I think I've seen this contributor in Gen AI space.
So, yeah, please point them, and I'll take a look. Okay, so there isn't a specification issue, cool. I'll see what happens there.
Tammy Baylis 00:57:09 Thank you.
Ludmila Molkova 00:57:10 Thanks.
Aaron Abbott 00:57:12 Yeah, thanks again for raising this one, Tammy. I'll, I'll see if I can get David to take a look at the spec issue as well.
Cool. Anything else on this one?
Tammy, will you also reply to, to the user on this PR, I would appreciate it.
Tammy Baylis 00:57:33 Yes, I'll do that.
Aaron Abbott 00:57:34 Okay, great.
Cool.
And last item here, Redima, are you on?
Ridhima Satam 00:57:43 Yep.
So, I think there is just one comment from, Lyudmila. If you have time, couple of minutes, we can just go over that.
Mmm.
Yeah, so… here we are trying to produce, workflow and agent spans, and if you go to the last comment, I think, Lyudmila, what you are suggesting is, in a line graph.
When there is a node, are you suggesting we should have an invoke agent span, even if there is no actual create agent and invoking of an agent? Right now, it's just limited to that.
Ludmila Molkova 00:58:23 Yeah, I think we need to have some idea of how we model length chain. And if I look into what Open Inference did, or it seems like use, and probably OpenLeetry, they represent the node as an agent, and then the whole graph is probably a workflow.
I don't know if it makes total sense, but that's what people already did. We can… it would be great to, like, write it down. We can have a… just a small, I don't know, issue, or…
Ridhima Satam 00:58:57 Incident.
Ludmila Molkova 00:58:58 semantic conventions, or because length chain is not even just writing-specific, right?
Ridhima Satam 00:59:02 People usually.
Ludmila Molkova 00:59:03 Or, pull request that documents how link chain is modeled, what aligns with what, and then then it kind of becomes trivial. You… you worked on this more than I, you have more context, and I'm… I just don't know what's the right way to model it, but I think we should document the.
Ridhima Satam 00:59:23 Where'd imagine.
Ludmila Molkova 00:59:23 right way. And if, other libraries, like Open Inference, BlankFuse, and so on, they, they follow the different approach, we should understand why.
Ridhima Satam 00:59:35 Okay, so do you want me to make changes in this PR itself as well? For those missing… spans of the nodes where there is no agent? Like, do we want to have invoke agent right now on that?
Or do we want to skip in this PR, and you're suggesting to open another PR so that we can have a proper… Oh.
A description of how we are modeling langchain land graph.
And how we want to add nodes.
Or I can just talk to you maybe offline also.
Ludmila Molkova 01:00:11 Yeah, I mean, the… the one of the passes forward to not to overload this pure, I see, is that, we can, if you could create an issue in… in Python Gen AI on how to model link chain.
And we will have a design there. And this PR, what I wanted to make sure it does not prevent us from adding adjunct later. I don't mind having a workflow to start with.
Ridhima Satam 01:00:37 Bye.
Ludmila Molkova 01:00:38 As long as we know how it will integrate with other spent.
Ridhima Satam 01:00:44 Sure, yeah. So for this PR as well, like, where we are identifying agent.
As an invoke agent, we are trying to see if there is any metadata passed as an Asian name. So if, on… the Langgraph node is identified on the Langchain side, like, on the callback handler side, so if you want, we can later just add into it, like, if it's a node, we can just create an invoke agent. I can add more, description in the comment itself, and that would make it clear for you. But yeah, I'll open the ticket as well. Thanks for your inputs.
Ludmila Molkova 01:01:19 Yeah, nice, thank you, Anders. I think, Leighton mentioned that, there is a person from Microsoft, Kumar.
Ridhima Satam 01:01:28 In touch with him. Yeah, I'm in.
Ludmila Molkova 01:01:29 So nice.
Ridhima Satam 01:01:30 Yeah.
Cool. Yeah. We had a discussion, like, so he has some PRs, so he will wait on some of my changes, and then he's going to exclude those from his PRs. So, yeah.
Ludmila Molkova 01:01:41 Awesome.
Ridhima Satam 01:01:43 Yep.
Ludmila Molkova 01:01:43 Thank you. And sorry for, like, the charm with the repos in the middle of your work.
Ridhima Satam 01:01:48 Oh, no, that's okay. Yeah, I have to move this PR to the new, report. I get it, yeah. Thank you.
Ludmila Molkova 01:01:53 Thank you.
Aaron Abbott 01:01:56 Alright, thank you all. We're a little over, but got through a lot. Appreciate it.
Ludmila Molkova 01:02:02 Thanks.
Mike Goldsmith 01:02:02 Take the room.
Riccardo Magliocchetti 01:02:03 Max.
Dylan Russell 01:02:04 Yes.
