SIG: Go Compile Time Instrumentation SIG
Date: 2025-07-31
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/LwNUp54zuOyYB8uXo8RdaIHC5SZvV_-5TcHlN3fqOf5CmtB9JDdyQL8OAZ6ZaAVK.esCilxFCgLbJB724
============================================================

## Zoom Recording Transcript

**Przemyslaw Delewski** 05:07 Hi.
**Romain Marcadier** 05:11 Hey!
How are you?
**Przemyslaw Delewski** 05:15 Good, thank you. And you.
**Romain Marcadier** 05:18 Not bad kind of having a pretty pretty busy.
**Ziming Liu** 05:29 Okay?
Bye.
**Romain Marcadier** 05:51 Actually been doing a lot of rest of late, and that reminded me
how much some other languages do a better job than go at making things easier for them.
**Przemyslaw Delewski** 06:05 Yeah.
**Huxing Zhang** 07:12 Okay.
Hello. Hello.
**Przemyslaw Delewski** 07:17 Hi.
**Huxing Zhang** 07:21 Who's gonna be the host of today?
**Przemyslaw Delewski** 07:26 I think that it's a Roman turn.
**Huxing Zhang** 07:28 Oh, Roman!
**Romain Marcadier** 07:30 Yep.
**Huxing Zhang** 07:35 I think we have been skipped 2 or 3 weeks.
**Przemyslaw Delewski** 07:41 I think 3 weeks. Even so.
**Huxing Zhang** 07:44 Yeah.
**Romain Marcadier** 07:49 Yeah, I think we skipped 3 in a row.
Alright, Premikha! Confirming that the golfer community engagement stuff is not ready to discuss today.
**Przemyslaw Delewski** 08:21 Yeah. So I have all the
information gathered from these people some. But I haven't. I haven't done some conclusions, some some synthesis of this to have a conclusion. So probably next week I will have it.
And yeah.
**Romain Marcadier** 08:42 Do we have anyone else who has an agent? Items that they want to pop on the list while we're
waiting a moment.
My guess not so much.
**Huxing Zhang** 09:07 What is the progress of our current project? I I'd like to confirm the progress, because recently I have
got too much attention on other projects. And we are working on the
like like, Jane, I stuff quite a lot. And so I currently yeah, spend less time in this project. So I'd like to query about the status of this project.
**Przemyslaw Delewski** 09:37 Yeah, I I think that we can look at the list of the issues that are.
you know, mention it in 1 1 of the issue.
and then everything will be mostly clear.
So there is this split implementation task, right?
Issue where we have a list of of tasks, and to, as I see.
Most of the set of faces implemented already. At least, this is
1st version of this set of face
mostly done. Everything was done by Yank.
So that's a great job.
**Huxing Zhang** 10:32 Cool.
So what is the what do you think
is the percentage of the progress that we are working
towards the like? First, st M. Ap version of that project.
**Przemyslaw Delewski** 10:55 So for Mvp. I think we have to also implement this second phase, and
to to be able to instrument Http, at least right? That that was the goal.
and very simple Http application.
**Huxing Zhang** 11:12 Yeah, this is based on the work that Young has provided, or we can do in parallel.
**Przemyslaw Delewski** 11:22 Probably we can paralyze somehow this. But this, I think this task, you know, depends on each other on each others
very often, because you have to, let's say, do something regarding this task, and then the other task. And
yeah, so there are some dependencies, in my opinion.
**Huxing Zhang** 11:45 Okay.
**Ziming Liu** 11:46 I think, for the net. Http. Plugin. There is already
implementation in the open telemetry Country Repository. We can just based on the
code of that and do some do some simple modification, using the using. The open instrumental. Api
think the most key point is to is to help Yuan to build the compilation framework.
It is the most important thing.
**Przemyslaw Delewski** 12:33 Yeah.
**Romain Marcadier** 12:52 All right.
**Przemyslaw Delewski** 12:54 Roman, could you open this? 29 issue?
Yeah. So here, as we can see, there are 4 or 5, maybe missing tasks
and the instrumentation. We have 3 in instrumentation phase.
and maybe Ian could tell something about it, but in my opinion they are somehow dependent. So.
**Romain Marcadier** 13:30 So.
Oh, ju-choo!
Right! They are fairly dependent. Like parallelizing them would require 1st crystallizing interfaces.
**Przemyslaw Delewski** 13:48 Yes.
**Romain Marcadier** 13:49 And then implementations can be decoupled.
The risk there being that
crystallizing the interfaces. Upfront is kind of bottom up style work, which usually means mistakes will be made, and then rework is going to be necessary. And then that's going to change the interfaces
and stuff. But yeah, overall, it might still make faster progress than sterilizing it.
So trade-offs, trade-offs.
**Huxing Zhang** 14:57 Just want to make sure. That is all. Are all the tasks being assigned assigned to do. They have
assignee, or they still like pending, to assign.
**Przemyslaw Delewski** 15:15 They are pending at the moment.
**Huxing Zhang** 15:23 So currently, we are depending on
work that young has been done. Okay? Right?
**Kemal Akkoyun** 15:35 Assign them. Now we can assign them. Now.
if there are some volunteers first.st
**Yi Yang** 15:49 Sorry. I think I have finished the setup phase, just the instrument. The instrument phase is ready for implementation.
Is there any questions?
Oh, okay, okay.
**Huxing Zhang** 16:25 Young. Do you think that you will going to finish this? All 3
faces, or you need help from others to 2 days.
**Yi Yang** 16:38 In. In my opinion.
I think the setup setup phase is, is complete. We created the the. We create a new file and import the hook functions. So in next phase, we we can.
We can inject this functions into a target function. Yeah, I think so- so I think the instrumentation phase is ready for make implementation.
Actually, I want, I want. I wonder if Roma or Pres are interested in implement implementing them.
**Romain Marcadier** 17:23 Yes, so
as much as I would really really like to write this moment I am taken by a high priority item.
so I cannot start right away.
It is probably going to be one or 2 weeks before I complete that thing I'm currently busy with.
and then afterwards I should be able to start prioritizing some of these stuff, and ideally, I would not want
to effectively pose for that long
cause I can forward. So I'm
I might be able to get a little time aside to make some progress on this, but this is probably going to be a couple of hours on Fridays, and not much more for the next. Probably 2 weeks.
**Przemyslaw Delewski** 18:20 So, yeah, I have very similar situations. So I will be very busy for the next 2 weeks, and then I will have a 1 1 week vacation. So maybe after this time I could, you know.
Take some tasks, but during this 1st 2 weeks it will be rather hard for me.
**Kemal Akkoyun** 18:44 I'm in a similar situation as well. Funny enough. I need couple of weeks I have a conference that I need to attend the middle of August, and after that I will be
free and focused on this work. Actually.
**Yi Yang** 19:04 Okay. No. Hurry.
**Kemal Akkoyun** 19:09 I think we have 2 options either.
**Yi Yang** 19:12 Okay, you.
**Kemal Akkoyun** 19:13 Yeah, you can give it a try like, no pressure like for the next couple of weeks, or we can wait, and there will be more people available, and we can work on.
Put it together.
**Yi Yang** 19:30 Yeah, maybe I can. I can take a try to implement the the load or or the match, and I will, and leave the instrument work for others.
**Przemyslaw Delewski** 19:46 That would be great.
**Kemal Akkoyun** 19:47 One second.
**Romain Marcadier** 20:01 Okay.
are we? Good on this front?
My guess we are premek. I guess we can go to the agent at points that you had.
**Przemyslaw Delewski** 20:27 Yes, so so I was thinking about this problem.
It was also raised on one of the meetings that I had with one of the golfers.
And
so before that, you know, I wasn't thinking about in much detail about this problem. But now it seems I was wondering if we have some solution for that.
and it seems that you, Roman, have some thoughts about that and Yank as well.
and maybe we can discuss it a little bit here, and maybe prepare some kind of Adr Idr
to describe the architecture that you would like to have, or some, you know, design decisions.
and then maybe we can continue on that also offline. I think that that would
makes sense for me, and if we will have some progress we will have a document for that.
We can also discuss that next time on the meeting.
**Romain Marcadier** 21:44 Yeah.
So the whole dependency conflict thingy as is like when we built orchestrian, was one of the
perhaps more complicated themes to resolve.
There's actually 2 facets to this problem. I think one of them is
you know, making sure that we don't.
Koh's
unwarranted changes to the dependency closure of the instrumented application. So like, you know, for example, if the application depends on a specific version of a package, and we upgrade that package
to maybe an incompatible version.
**Przemyslaw Delewski** 22:38 Yes.
**Romain Marcadier** 22:38 In the back of the customer. This is not good like, you know. Not not all. Go packages follow Samber particularly well, so we we do have it. It actually is one thing where we
run into issues somewhat regularly. And the second one is, we also need to make sure that we don't introduce dependency cycles. So the dependency cycle situation is actually largely handled
by what we've discussed so far, which is, we inject hook functions that are bound via Golink name.
and effectively, this breaks dependency cycles, right? It just means all components need to be compiled.
And then the the cycle is fulfilled by the Linker. But the Linker is not sensitive to cycle issues. So this is fine.
And then the dependency resolution thingy, as I was saying over, slack the
perhaps main reason for why I'm advocating for making sure that we set up the customers project in such a way that everything we need possibly at instrumentation. Time is accurately modeled in the go mode and go some files.
So this way we can guarantee that the dependency, the complete dependency closure of the application is actually
under the customer's control, and they don't get upgraded in their backs.
That kind of implies you need a setup phase, and you need to modify some code. So we've we've kind of discussed this in the past, where
we felt like it was necessary or desirable, at least
to set up this open mode.
We the lowest with orchestrian today
and I guess each week I am getting.
I mean, I'm not getting an issue about this each week. But I'm regularly getting issues about this.
And each time I get an issue about this makes me regret allowing this a little bit more.
But essentially we have issues. For, for example, the datadog Tracer library
has a dependency on a v 0 dot, something package that has breaking changes regularly.
and when we do gomut tidy, and that package is not in the closure just yet, it gets default, resolved to the latest release.
and sometimes one symbol from it disappears, and that symbols. For example, we recently had a case with a symbol that was used by the tracer itself.
and then the latest version no longer has this symbol because it was renamed to somewhere else. And so now everyone who does go get dash U gets broken.
and everyone who uses orchestrian PIN, which is our setup command without having this package in their closure, yet basically gets broken. And we need to release a new version of the tracers that is fixed with everything and whatnot. It's
a little annoying, and I guess we, the issue is mitigated. If people check in
stuff such that Gomod contains everything, and then, if go mode models all the dependencies, then you don't have a risk of conflict, because.
your package resolution is guaranteed to return stuff that is tracked in go mode.
So you don't get surprised. You don't get to possibly resolve to a different version than what currently is in the customer's code, and all dependencies that are shared between instruments and the instrumented app are effectively resolved to a single version, canonically and and in a user control manner.
**Przemyslaw Delewski** 26:37 Do you have maybe some links to the issues that you already have regarding orchestrian, or
or maybe I can find them on on the Github.
**Romain Marcadier** 26:53 I'm
cause cause several of these have been reported internally, and so I don't have a.
**Przemyslaw Delewski** 27:05 Okay.
**Romain Marcadier** 27:05 Show, for instance, but we might have.
We probably have some traces of that. I can definitely show it.
I think we do have an issue about the latest tracer 0 dot dependency version.
The irony actually of this is the package which is causing us issues the most frequently with this kind of like, go get dash, U kind of issues is actually open telemetry.
**Przemyslaw Delewski** 27:36 Okay.
**Romain Marcadier** 27:38 But but yeah, I will
probably not today. But I'll try to dig up stuff and put references in there. I'll just make a note for myself.
**Przemyslaw Delewski** 27:51 Yeah, the
because I'm thinking about, you know, starting, documenting this. And it would be good to have at least description of some problems that we experienced in the past
to to have a good understanding what we would like to do. You know.
**Romain Marcadier** 29:00 Right and so I guess.
Ye young did put some stuff in the slack with respects to these 2.
I don't know, young, do you? Wanna comment this further.
**Yi Yang** 29:30 That's I don't have further comments, basically the same as you.
**Romain Marcadier** 29:37 Cool, cool. Yeah, good. So so it does seem like.
we largely agree on this stuff. So we probably just want to write something to formalize this and provide examples of the type of issues
that
this sets out to avoid. And ideally, we can circulate this back with the golfers who raised the issue
and see if they the holes in that.
Basically I I think it should be fine. But never heard.
**Przemyslaw Delewski** 30:16 Yes.
**Romain Marcadier** 30:16 They can think of the ways that this is insufficient.
**Przemyslaw Delewski** 30:20 Yes, that's a good plan, so formalizing it, and then
send it to to for the further review.
**Romain Marcadier** 30:53 Okay, I'll put an action item on myself to write the doc for that.
How do I turn it into a checkbox?
Doesn't matter so much. But
no
oh, well, that'll that'll do it for now I'll I'll figure out the checkbox situation after the call.
cool.
Is there anything else. We wanna discuss there.
**Przemyslaw Delewski** 32:10 We can also mention that our talk submitted to the Kubecon by camel was not accepted. Unfortunately.
**Kemal Akkoyun** 32:23 Yes, it's not even wait listed. So it was hard to rejection this time.
**Przemyslaw Delewski** 32:28 I mean, don't think.
**Kemal Akkoyun** 32:29 It's it's.
**Romain Marcadier** 32:31 I mean, this is like, this is like my experience, 100% of the time. So far. So you know.
**Przemyslaw Delewski** 32:39 It's it seems that maybe this is too specialized, you know.
talk because my experience is that they are mostly accepting some introductions, or maybe basic talks about something. So.
**Romain Marcadier** 32:58 It could. It might be an audience match issue. It's kind of tricky, right? Because
**Przemyslaw Delewski** 33:05 This might be a little too low level for Kubecon, I guess. Yeah, yes.
**Kemal Akkoyun** 33:10 Yeah. But the way we written the proposal was for platform engineers, and it was a bit of a high level.
Maybe we can just like work on that proposal a little bit more. That's why, like, it wasn't the top proposals that we submitted to the open pandemic community which details this was very high level. There is a way that you can use. Yeah, we we can try next cube con work on the wording a bit, and then the tool will be out hopefully by then. Because we have more than 6 months now.
And yeah, let's see. Fingers crossed. I didn't want to like submit specifically for, like observable to audience, or like open telemetry audience. I think, like people are already aware of that. That we are working on the tool.
So we need to have a broader audience.
**Romain Marcadier** 34:04 Yeah.
**Przemyslaw Delewski** 34:05 And.
**Romain Marcadier** 34:09 Cool cool, I mean. Anyway, you can't always win so.
**Kemal Akkoyun** 34:16 Yes.
**Huxing Zhang** 34:17 It, took.
**Kemal Akkoyun** 34:17 Yeah. But the the conference talk that I'm going to be giving in Uk London golf recon. Uk, it will be about
this practically. So, yeah, yeah, they will get mentioned.
**Przemyslaw Delewski** 34:32 Yes.
**Huxing Zhang** 34:34 You know, talking about the conference where are helping to? I'm also working on organizing the Kcd Hangzhou in China. And yeah, we will definitely can have some chance to maybe talk about this.
Yeah, we we will try to submit a talk
there. It's going to be like in 11 November of this year. Yeah.
**Romain Marcadier** 35:13 No right.
Any other topic going once, going twice, gun
alright. I guess we get half an hour back.
careful not to use it all on the same things.
Thanks everyone for your attendance. See you next week, or in 2 weeks, or whatever have a good one.
**Przemyslaw Delewski** 35:42 Thank you.
**Huxing Zhang** 35:43 Same case.
**Ziming Liu** 35:43 Bye-bye, bye.
