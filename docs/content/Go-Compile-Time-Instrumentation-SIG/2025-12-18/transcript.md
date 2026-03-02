SIG: Go Compile Time Instrumentation SIG
Date: 2025-12-18
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Kemal Akkoyun** 09:32 Sorry for being late.
**Przemyslaw Delewski** 09:35 Aye, no problem.
**Huxing Zhang** 09:41 Aye.
Nice to see you again.
**Kemal Akkoyun** 09:49 I am here…
Alright.
I agree.
**Huxing Zhang** 09:59 I have a vacation from next week.
There, all of you from next week, about 2 weeks off?
**Przemyslaw Delewski** 10:13 More or less, I think.
**Huxing Zhang** 10:15 Okay, that's cool.
It's a good time to… for you to have your… Holiday, right.
**Kemal Akkoyun** 10:24 Yeah.
Also, Open Telemetry decided not to, like, cancel all the meetings, I think, and they're automatically canceled for the last two weeks, so…
This is our last chance to meet.
**Huxing Zhang** 10:37 Yeah, yeah, yeah.
The NASDA meeting in 2025.
**Kemal Akkoyun** 10:42 Yes.
So, do we have any agenda items?
Right now, besides… Duh.
**Przemyslaw Delewski** 10:54 Yeah, so as I mentioned, some time ago, I recently
I was rethinking what we did so far. Also, I was working on some sites project, and…
Wanted to share with you some thoughts about that.
So that's one item from my site.
**Kemal Akkoyun** 11:15 Okay.
And we, need to, like, I don't think we need to do, like, this… discuss anything about the release, we just, like, it's waiting for a single item, then we can cut it.
**Huxing Zhang** 11:34 Shall we, take a look at the release my, project milestones, and check if what, what's the current status of this project?
**Kemal Akkoyun** 11:47 Yes, let me open that.
And share my… Bring… Okay, so… where are we? Yes, that's our version.
Yeah, I updated this issue. You can see this, right?
**Huxing Zhang** 12:08 Yeah.
**Kemal Akkoyun** 12:09 I updated the issue, I think I removed all the issues that he said, like, it's not…
Important… yeah, the only… Remaining, like, big task is 218.
And then there's this validation thing, but I guess, like, Javier has already been, doing something about it, if I'm not…
Mistaken, and it's also, like, running the demo application and making sure that context propagation works.
With the tool.
Check.
It's not a big deal.
But then I remembered we also said that we would like to rename the CLI to OTLC, and, like, we also wanted to, like.
pronounce that, like, Otelic, so maybe we can do that, before the release. That's one issue.
And this one. I think that's it, and we are nearly done.
Do you think anything we miss?
**Huxing Zhang** 13:24 What's the opinion of this, rename… renaming? What… what… what is your going into…
prefer? What was your preferred? Any other ideas of, other alternative, names, or…
**Kemal Akkoyun** 13:42 I think we discussed that on Slack?
If you still have, like, different alternatives.
**Huxing Zhang** 13:48 Is there any consensus on that?
**Przemyslaw Delewski** 13:54 Hmm, I'm not sure.
**Huxing Zhang** 13:56 But…
**Przemyslaw Delewski** 13:57 Maybe we should, you know, have more time to think about it?
**Kemal Akkoyun** 14:04 Now, of course, I mean, until we release it officially, we can change these things. So maybe, okay, I…
We don't need to create an issue right now, and we can wait.
**Huxing Zhang** 14:19 Yeah, I think we can put the issue there, and maybe it's not included in the next release, right?
**Kemal Akkoyun** 14:28 Fines… So, yeah, that one…
Maybe I can say that, like, the name is still… Not decided.
yes.
Okay.
I think Yi Yang already
Said that he will take care of this next week, and then we can cut the release.
I think… I don't remember if we merged, we also have a release automation, yeah. So, we also have this. Probably we would love to
actually merge this before we actually cut the release. Maybe I should add this.
To the list, and to the milestone.
Anything else?
No?
Alright.
I think this was ready… We can actually merge this.
All right, so, that's the release.
Viva Lame, Release next week.
Any objections to that?
Okay.
**Huxing Zhang** 16:39 Nope.
Thanks, I think that's a good news. And, so, before we're doing this release, maybe, what, what,
Is there any vote we have to really do before it, or we just publish the release in GitHub?
after we reach… because from next week, you… you are going to, enter into the, holidays, Christmas days, holidays, so…
**Kemal Akkoyun** 17:09 Yep.
**Huxing Zhang** 17:10 We can take over the task to publish the release.
So what? Okay.
**Kemal Akkoyun** 17:18 Yeah, I can help… still help, here and there. I will be… I will have access to computer, but, like, if after Yi Yang finished that… finished that task and merged that release drafter thing, maybe you can just cut the release. It's just about tagging, right?
Or, like, making sure that, I don't know, we have some documentation around that. I don't think, like, people just gonna use it, as is, but yeah, we should aim for, like, V0,
0.1 or something, as the release, but we can discuss this also, like, I will be available, so, then we can just release it. Maybe, I don't know, we can…
Announce that in the social media, media, in our, like.
Social accounts, but that would be extent of it, right?
I don't think we need to write a blog post, like, it's not that big of a deal. Maybe our, like, first initial major release, we should definitely write an OpenTelemetry blog,
Publish a blog post, whatnot. But, yeah, we are far from that.
**Huxing Zhang** 18:30 Okay.
So what is the number, version number of this radius? It's 0.
1.
**Kemal Akkoyun** 18:39 I think 0.1 sounds good to me. What do you think?
**Przemyslaw Delewski** 18:43 Yeah.
**Huxing Zhang** 18:44 21 dot, dot zero.
**Kemal Akkoyun** 18:48 Yeah, I think.
we can have a lot of releases, like… yeah, after this one, we can start cutting, like, releases, like, pretty frequently, right? Whenever we have something fixed, whatnot, or, like, we added a feature, we can just, like, release. And if we can also automate that, that would be easy.
Yeah.
**Huxing Zhang** 19:09 So, from this release, we can have some, like.
In every one or two months, we have, a fixed, Period, release period, right?
**Kemal Akkoyun** 19:23 Yeah, Legion.
Yeah, like, that's one of the things that…
We can discuss. So, we can discuss… if you want to do that right now, we can also, like, do that.
We can decide on a release, like… Cadence, right?
**Huxing Zhang** 19:48 Yes.
**Kemal Akkoyun** 19:48 We already have this, like, release automation.
I might, like, vote for, like, every 6 weeks or so, which is… I think it's a good cadence. Or we can do… like, we don't need to come up with a cadence as well, like, we can just say that, like, whenever we have something big.
that, like, we're releasing, right? We can also do that.
But having a release cadence helps, because then we can assign release shepherds, right?
and release shepherds can be responsible for, like, making sure that all the PRs are merged, all the pressing issues are fixed, and then, yeah, they can ping people around, push people around to cut the release.
Yeah, if you want, we can also do that.
What are your thoughts?
**Huxing Zhang** 20:44 Yeah, I'm think… we are doing this internally in our… within our company, so I would suggest that you do have that. What do you think?
**Kemal Akkoyun** 21:01 I'm buying me.
Any ideas, Primarchy?
Pines?
It's a silent consensus, okay?
Or, it's not that big of a deal right now.
everything works. Okay, I'm gonna create an issue for this, right?
So, let's say that… This is also true, like, create a release MD?
Right? And… Does cadence, like, the 6-week cadence work, everyone?
**Huxing Zhang** 21:47 Yeah,
That's good.
**Kemal Akkoyun** 22:04 I guess, starting from… 2026.
Yeah, we can document the release process.
If we have any scripts, like…
That we come up with, we have the release drafter, we need to see that in action, like,
Whatnot, and then, yeah.
I think it's… It starts.
Okay, I'm creating this issue, and if anyone wants to take this, go ahead.
Okay… But we need to merge.
The release draft, right?
Okay.
Let me put this in here… Cool.
Yeah, we need more excitement in the room, like, everyone is in the morning. Maybe we need more coffee or something. We are cutting our first release, come on.
**Huxing Zhang** 23:28 Yes, yes.
**Kemal Akkoyun** 23:31 Okay, next topic, KubeCon, like, KubeCon updates, but before that, Premier Chick, you said that you have a topic, maybe you would like to put that in the agenda, or you can take it over now?
**Huxing Zhang** 23:43 You can go first, Ben, you can go first.
**Przemyslaw Delewski** 23:47 Okay, so, let me maybe share the screen.
**Kemal Akkoyun** 23:51 I'll stop sharing, yeah.
**Przemyslaw Delewski** 23:54 So, I'm sick a bit, so we will see if that will go smoothly, but I have some small presentation, just to, you know, structure what I would like to tell, and not forget about something.
I hope you see that.
**Kemal Akkoyun** 24:14 What is this tool? I really like that.
**Przemyslaw Delewski** 24:16 So the presentation was created via Cloud Code, and it… I was used also MARP, so… as a format.
So, basically, that's… that's the thing.
And, so, I wanted to ask, to talk about a few aspects. So, recently, I was working on, as I mentioned, an on-site, project, on-site project, and
it is mostly VIPE-coded, so it's 90% of it is VIP-coded, so I wanted to check some specific aspects of our domain, let's say. And,
I am mostly focusing on a few things. One of them is developer experience and debuggability of our tool first, and then also of the
The final execute table that is produced.
And, first thing is, is, that I would like to talk is a tool exec. So, for now, we are using tool exec to, you know.
to do our stuff, to inject the code, to do other things, and that means that we are somewhere here. So we are a plugin, and we are controlled by the Go compiler.
Which means that it's very hard, you know, to attach the bugger. It's possible, but it requires some tricks, and maybe some additional code also in the tool itself to, you know, to stop somewhere
To maybe, wait for some specific event, and then…
you can attach the bugger to it, but it's not very easy to do now, and you cannot basically, you know, set the breakpoint and go through one point to another in easy way. That's something that bothers me.
So, I was started to thinking,
To, to do that from the other direction, and maybe… You know, to control…
to control compiler, so we would be a kind of orchestrator. So, basically, what I did, I did the very similar thing, what we have in the setup stage. So basically, first I am generating
this build, GoBuild, log, go build log, and then, I'm just, traversing through it, I'm updating this Go, build log.
Whenever it's needed. So if I will match some function that, we would like to instrument.
or some, you know, file, and so on, then I will change this just, the Go file, and I am replaying the compilation process. And, you know, that's, that works in the same way as,
as we currently, do in using tool exec, basically. Of course, there might be some corner cases to that, but,
doing this way, I can easily connect the bugger and, you know, do that step by step and so on.
And I will show you how this works in practice, because I have also a small demo for that.
The second fig… any questions so far, maybe?
Okay, so the second thing that I was thinking about is this hook definition that we have already. So, for now, we are using YAML for defining hooks.
But, there are some… you know, for simple cases, it works perfectly. But whenever you have some,
you know, more sophisticated case, it… the YAML is not very good to express that, because it's not possible to express that. For instance, we… we have this problem already in our code, in the, you know,
runtime hook. So we have a runtime hook that is here, in the YAML code, but we also need to add this return variable to the function signature, and we are using normal Go code to do that.
So, which means that we are mixing these two things, and one thing is in our tool, so part of the code is in our tool, and part is in YAML code. And we cannot express that in YAML, you know, code itself.
So, that's, I think that it would be good.
To have one way of expressing such features or such things.
And probably in YAML it's not possible, in my opinion, so maybe, maybe it would be better to use just, you know, Go code as some kind of DSL, and that's an example of Go.
DSL here to describe the same hook as you have on the left. And of course, on top of that, we can have,
We can have YAM as well, for very simple definition, but internally, we could use also, you know, some kind of DSL that describes these definitions.
And as you know, in Go, we can do everything we can imagine, so that's basically the goal.
And bet… and that's… That's the slides. So now,
I would like to show you this vibe-coded tool that I did. So, basically.
So the tool has a few slides, sorry, a few switches. And one of the most important is compile, and so it compiles, it takes one parameter, which is this go
file this GoDSL definition that I mentioned, which describes the hooks. But also, I built an UI for that, so I will show you how it works.
So, the UI, basically, it's a… it's a simple HTTP server, and the UI is in HTML and so on. So, you can see here this project.
This is a very simple project that I would like to instrument, so there are a few methods, as you can see.
here, very, very simple. I can… This… yeah. Like, this UI looks really professional. Is this, like, cloud code generated? No, this is not… sorry, this is cloud code generated, and
as I mentioned, I… if I assume all the hours I spend during this project, it may be one day. So, that's… I've coded this in one day, basically.
Now, I can, I can just run at this execute table that is, after compilation of this project, because I did it, before. So, as you can see, it, it, it ran, and it outputted hello here.
And now, I can show you how, how we can instrument, this code with using this UI. So, basically, there is a view menu, there is few, few menus here, so I can look all the functions that…
We'll… we can instrument that these functions,
this is all the functions that will be, you know, compiled, when we compile this project. So, also, from the standard library and third-party libraries, we can look at the, you know, for instance, packages that will be used.
to compile these projects. We… we can look at the work directory, how it will finally… will look.
**Kemal Akkoyun** 32:44 Wow, this is… this looks impressive, yes.
**Przemyslaw Delewski** 32:48 Yeah, and then finally, there is also a static code graph.
So you can look at the static call graph of this application, and here, you can also select a specific function that you would like to inject into. So when I will do that, for instance, here…
here, and generate hooks, you will get this DSL, this small DSL, Go DSL, already. You can also, of course, you can change that, and you can extend that, and so on.
And then, we can save that.
I will create a new, new directory for that, and…
I will save that in this file.
And now, if we will back, we should have it, here…
Okay, and now, so now I can compile this code, using this new, new hook.
Do I have to… You know, tell the tool to use this parameter.
Which is… which is, just parked… 2… to these hooks.
Yeah, and it, it opened this window, you can see,
Something goes wrong, so I probably made mistake in.
**Kemal Akkoyun** 34:32 Generate hooks, you wrote generated hooks. There's an additional deal.
**Przemyslaw Delewski** 34:36 Okay, okay, okay, thank you.
So, again, generate hoop.
**Yi Yang** 34:44 No worries.
**Przemyslaw Delewski** 34:48 So on again.
Yeah, and it…
it traversed for the, you know, the compile log, this GoBit log, and it matched 3 functions here that we selected.
So it instrumented these, three functions, and finally, it successfully, you know, created the execute table. So when I will run it again, now…
We should…
we should, see something like that. It's not on par yet with our tool regarding this instrumentation, but I think that when I will spend one day more, I will have it, so…
**Kemal Akkoyun** 35:36 I think, yeah, this is awesome. I think we should just, like, this will help a lot of, like, integration writers and, like, the instrumentation writers, this will help really, like.
It's extremely helpful, that's what I'm trying to sell, and definitely we should put that in the repo, and put documentation, and, like, record a demo, whatnot, and this is how you can use to generate hooks, and…
basically add instrumentation, because this would enable all the, like, the third-party people that they don't know a lot about the tool, but they come here and try to add the new instrumentation, they can experiment with that. This is basically, like, an integration writing studio or something. Yes, that's…
**Przemyslaw Delewski** 36:21 Something like that, but this is… you know, I just wanted to ask you if that would be, of course, you know, useful from your perspective, because, as I mentioned, it's a kind of side project from my side, so…
Yeah.
**Kemal Akkoyun** 36:37 Or, like, that's definitely useful, and we should, like, in my opinion, we should definitely have in the tool. Like, from the first aspect.
I think the… You mentioned that
we can't express a lot of things in the YAML, but we should keep the YAML files, but we can have the Go DSL, or these files as, like, an intermediate representation, so either you can write these Go files.
or you can write the YAML file, it should be, like, interchangeable. But I really like the aspect of, like, the keep the YAML files lean.
not put, like, a lot of complicated GoCode in the YAML file, because then you cannot use the linters, compilers, whatever. It's hard to, like, debug.
But put all the things in the Go files, like, besides the, like, the YAML files, so that we can just interact with, put debug points, whatever, use the linter, whatnot. I like that aspect as well.
So, yeah, if we change anything around our tool, yeah, we should, like.
implement in a such way that it wouldn't, like, change the YAML, like, yeah, niche the YAML files.
**Przemyslaw Delewski** 37:46 Yeah, okay. So, I just wanted, you know, to extract these cases where we need
you know, modify some, let's say, more sophisticated code, like in runtime. So, currently, only our tool can instrument runtime library, and I want
extract that to have a way to say that in a…
Not in a tool, but in a, you know, hook definition itself.
**Kemal Akkoyun** 38:15 Yeah. One of the things, like, the side effects of that, like, having the separation of these, like, files, one of the things that I'm trying to, like, create a POC is, like, doing runtime injection as well,
Instead of, like, the compile time injection, and if we have these, like, hoops, like, defined like that, like, before and after function, you can… we can actually reuse all this instrumentation with another tool, like a compile time… not a runtime injector tool.
we can also enable another use case. There's another project in OpenTelemetry called Injector, and they are trying to do something… similar things, and they don't have any goal support.
But, yeah, it…
We can extend in the feature, like, add a runtime injection feature to them, to that project, and
if we publish all these instrumentation in another repo, we can reuse them. So…
That all comes together with the last week, the last meeting that we have, so that another use case for having a separate registry for all these instrumentation is that
basically.
A tool to inject in compile time, another tool to inject those things in the runtime.
**Przemyslaw Delewski** 39:36 Okay.
Maybe one last week, I can show you that we can look also how now the work directory looks like in the main file, so that's the instrumented main file.
**Kemal Akkoyun** 39:48 This isn't…
killer future for me, to be honest. Like, while developing these things, like, this… probably this one that I would use, like, most likely, right? Open a thing and see, like, what it's actually generated. Oh, there's a mistake there, like, let's fix it.
One suggestion to this tool is if you can have an LSP support to these parts, and so that we can have linters, fixers.
**Przemyslaw Delewski** 40:12 Yeah.
**Kemal Akkoyun** 40:12 That would be amazing.
**Przemyslaw Delewski** 40:14 Yeah, that was something I'm thinking about, but it requires some time, you know, to do that.
**Kemal Akkoyun** 40:20 Yeah, like, you don't need to do this all by yourself, right?
make this, like, open a PR after this got a mature state, I think, in a subdirectory in our tool, put it in there, and let's start developing everything together, right? Like, if… and we can open issues, whatnot, and it's like…
And we can decide, like, when we have the second repo, I think this would fit better to, like, an instrumentation repo more, and we can move, this one with all the instrumentation to another repo and say that, like, this is how, actually, you create these instrumentations. That would be awesome.
**Przemyslaw Delewski** 40:59 Also, the one thing that I would like to add is to, you know, to ability to debug the final execute table. So, there will be probably another button here. To debug, you will be able to set breakpoints.
In the, in this, in this code, and you can, you know, debug this final, final instrumented code, so…
**Kemal Akkoyun** 41:23 This is… this is really good. This is really good, like, really check kiss and kudos, like, I… like, this, I never thought about this, but, like, thinking that the amount of time that we spend on writing integrations in our, like, with our tool, Orchestrian, this would help a lot. This is also helpful with the, like.
the engineers that are trying to onboard to the project, because sometimes it's not, like, super clear for them to what happens if I do that, what is generated, and, like, with this, it's, like, easier to already, like, have an idea.
**Przemyslaw Delewski** 42:01 So basically, just to sum it up, my goal now would be to, you know, to polish this source code, because as I mentioned, it's 90% of that was just pipe-coded, but I can prepare a pull requests from that.
And, it also, maybe implement some missing functionalities and some corner cases, so basically that's it, that's the plan.
Okay.
And sorry for my voice, because I'm sick, as I mentioned.
**Kemal Akkoyun** 42:35 I have to admit, this is the…
the most cool, like, the coolest use case that I've seen generated by a, like, a cloud code or an agent decoding, right? This is, like, I've seen a lot of people do stuff, but this is actually useful.
Okay, thank you.
**Przemyslaw Delewski** 42:52 Okay, thank you.
So…
**Huxing Zhang** 42:55 That's it, basically.
Thank you. I already have another suggestion. I think we can maybe have some extensions and something like the existing coding IDEs.
For example, VS Code. We are the.
**Przemyslaw Delewski** 43:12 Yeah, so, basically, this could be also a plugin for the VS Core or something like that, but I wanted to have, you know…
a separate tool to have a full control over it. So, basically, that's… that's how I… I decided to build this one. But, of course, everything here I built here, we can also provide as a plugin to existing, you know, IDs.
**Kemal Akkoyun** 43:42 Okay, so, I need to go pretty soon, so let's, jump into the next topic. Alright, so we have, KubeCon EU update, so, who wants to talk about this?
**Huxing Zhang** 43:59 I'd like to ask the status of the CFPs you have submitted, either an update from your site, because I have…
to… I have, applied two proposals, they got rejected, you know, from their main… main conference, but I'm still having some… waiting for the notice of the…
Co-located events, maybe.
**Kemal Akkoyun** 44:30 Yeah, so I haven't, submitted anything for the main track, so we are waiting for, the co-located events, which is specifically observability Day. We have two talks in there.
Okay. Concerning this, SIG.
And I also submitted, to the maintainer's day, track, whatever you want to call it.
Also submitted to the maintainer's track.
So this idea came from, like, when we are having discussions, so the idea is
This will be a meta-talk, it's not technical, it's about, like, donating a project to OpenTelemetry.
And the idea was, bring the… so there are two successful donations right now. One is EBPF-based auto-instrumentation tool, Bela, and it forked into two different projects. One is OBI, and the other one is Go Auto Instrumentation, and our compile time instrumentation. So…
We will talk about how we managed to pull that out.
Right? So, there will be three parties in this talk. One person from the Open Telemetry Governance Committee, one from the Auto Instrumentation side, Bela, probably someone from Grafana.
and… I…
Some created the talk and submitted myself, and I will represent to the compile time instrumentation. That being said, if I got accepted to the observability today as well, we can shift things around, right?
One of you can get, one of the technical talks, whatnot, like, we can decide.
All of these are going to be announced in the…
So the co-located events, if I'm not mistaken, around 7th of October, January, not October, or, like, somewhere around that, like, the first two weeks.
And the maintainer's one after the second half of the January, so we will know everything at the end of January, basically, whether we have any acceptance for KubeCon EE.
**Huxing Zhang** 46:44 Okay, sounds good.
**Kemal Akkoyun** 46:46 I will keep you updated, and yeah, as I told you, depending on the situation, you can change seats, they are open to that, usually.
Then we can have, like, we can try to have tickets, and yeah.
I think one… one of them is already, like, submitted with PremierCheck, right?
**Przemyslaw Delewski** 47:05 Yes, and it means that this maintainer talk is already… accept it, right? Because.
**Kemal Akkoyun** 47:13 It's not accepted, but I, like, I think it's a pretty cool topic, and people would love to hear about that. I have really high hopes on that talk.
**Przemyslaw Delewski** 47:24 Oh, okay.
Because, I was thinking that it's, you know, accepted because it's my tail.
So, it's accepted, you know, out of my.
**Kemal Akkoyun** 47:37 Usually.
Yes, that's true, but it is also, like, it's… so technically, in KubeCon, each project has a slot, or depending on the size of the project, two slots, for a talk, but it's for the main track, right? This is for the day zero.
basically, like, the maintainers, meet up, this talk for that track. So this is different. This is like a co-located event, right?
So it's not automagically accepted, so we need to still wait for, wait for how, like, they would react. But again, I think this is a pretty cool topic, especially considering the track that we are submitting this. I have high hopes.
**Huxing Zhang** 48:24 Yeah.
I don't… I also very like this idea as well.
**Kemal Akkoyun** 48:31 Cool!
Do we have any other topics?
Awesome. Let's try to submit, like, cut the release next week.
Yeah.
It was a great year, all in all. Like, it was some of the… some of the times it felt slow, but I think towards the end of the year, we kind of picked it up, and we got a momentum. I think we should just, like, continue doing this for the next… next year.
**Huxing Zhang** 49:00 Yeah, this is a good wrap-up of the year 2025, I think. Yeah.
**Kemal Akkoyun** 49:07 My goal is to, like, to cut the stable release, or at, like, at the end of Q2. So, yeah, let's, let's aim for that.
**Huxing Zhang** 49:16 Yeah.
So, maybe after, Next year, we can… next meeting, maybe we can discuss about the…
Future works, after the first release, yeah.
**Kemal Akkoyun** 49:33 Yeah.
Definitely.
Cool. Any last words?
**Huxing Zhang** 49:42 Every Christmas.
**Przemyslaw Delewski** 49:43 Yeah, Merry Christmas and Happy New Year.
Yeah, happy holidays, everyone. Alright. Yeah. Then, bye-bye!
**Huxing Zhang** 49:51 Goodbye.
**Przemyslaw Delewski** 49:52 Thank you, bye.
