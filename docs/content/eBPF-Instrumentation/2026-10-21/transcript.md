SIG: eBPF Instrumentation
Date: 2026-10-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang (Raintank, Inc. – Grafana Labs)** 00:10 Yeah, Andre.
**Endre Sara** 00:11 Hello!
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 00:14 Good to see you.
**Endre Sara** 00:15 Happy Wednesday!
How are you?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 00:19 I'm good, thank you. How are you?
**Endre Sara** 00:21 I'm great, I'm so happy.
I'm sure you had something to do with this, 339 biller release being out.
Which is very exciting.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 00:34 Alright, and that was all on the rest of the, on the rest of the team, I think.
**Endre Sara** 00:40 I was chatting with Mario, and There were some concerns without it, and with it, everybody's happy, so thank you.
**Gregor Zeitlinger** 00:53 Hello!
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 00:54 Right.
**Gregor Zeitlinger** 01:10 Cheers!
**Rafael Roquetto (Isovalent)** 01:28 I like regarding, Gregor.
**Gregor Zeitlinger** 01:39 Sorry, what did you say?
**Rafael Roquetto (Isovalent)** 01:41 I was just messing with you. I just said I like your garden.
**Gregor Zeitlinger** 01:49 I have to keep it up every day?
**Tyler Yahn (Splunk)** 02:05 How y'all doing? Looks like we have a… Full house already.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:12 Good, good, how are you?
**Tyler Yahn (Splunk)** 02:14 Good, good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:20 I got sick on my way back, so a little bit under the weather, but otherwise, not too bad this morning.
**Tyler Yahn (Splunk)** 02:29 Did you get, COVID, by chance?
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:30 Yeah, maybe, maybe, I just feel that way.
**Tyler Yahn (Splunk)** 02:34 I had, actually a few friends… yeah, I got the same thing, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:39 It's mild, though. I don't have a fever, it's just sore throat and… Runny nose.
**Tyler Yahn (Splunk)** 02:45 Yeah, still not fun.
Well, cool. We could probably jump in here in just a second. If you haven't yet, please go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, go ahead and add them there as well, and I'll start, sharing my screen.
Okay, cool. Alright.
So, to start us off, I wanted to talk about the release we got out last week, for those that aren't aware, or, are more interested in it. So, We were talking with some of the collector folks, and, one of the things that, like, kind of stood out was the fact that the, collector receiver, it needed an update, to, to get released with, the latest collector contrib, Docker image, and so… It was one of those things where we pushed a fix, but it still needed to get its own release. And the fact that we had coupled the… the… the receiver module with the OB module meant that we can't do another release without it, and… It was becoming pretty obvious. That was kind of like… going to be a glaring error. There was also some pretty big gotchas of, like, that receiver itself is marked as alpha, there's definitely some… You know, questions we had around the configuration, if that's actually what we wanted to stabilize, So, yeah, it seemed, at that point, like, we've been fighting an uphill battle, and so it warranted another release candidate. In the process, getting out, V05… or V015.2, due to some releasing snafus of trying to split the, the modules, there was some, like, releasing issues there.
But yeah, that is essentially, like, a new module now. It's under the OB module itself, so it's the… You know, it has this import path.
in, theory, like, we could start setting up tooling to have it… I mean, our tooling should release it, it's just that we might want to also set up tooling to, like, maybe make it more first class on how we do these releases. But essentially, like.
It should be able to be released. We don't plan on releasing any sort of 1.0 RC for it, so it's just going to continue on its own track in the same versioning scheme that it already was.
The 1.0 RC2 was made last Friday, so we're at day 5 of this, so we've got, 9 more days until we want to make the actual release, which kind of puts it back to the SIG, like, we're looking for feedback on this, if you haven't yet, already pulled in the, V015 please do so, check it out, or just check out this RC. There's, I think, like, a few package upgrades between the two, that ended up happening, but, like, it's not too big of a difference. But yeah, it would be ideal to have this evaluated. I've heard taken a look at it a few places, but obviously the more eyes on it, the better.
Yeah.
Any thoughts or questions on that one?
If not, we can keep going.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:08 Yeah, I just had a question. So then, does this now… allow us to add that option that the user wanted to use the… since it's not stable, this module, that we can potentially still…
**Tyler Yahn (Splunk)** 06:22 I think potentially is carrying a lot of weight in that. We still need… we still need buy-in from the collector team on, like, that configuration change, and, like, yeah, there's also, like.
One of the other things that, like, I was talking with the collector team on when we were originally doing this is the fact that, like, the log correlation stuff that we do doesn't work, just because it's not part of that configuration.
But they were saying, like, well, that might actually make sense to be another, like, component in the collector itself, just to be, like, you know, a receiver really should be receiving information and passing it along, but, like.
There are things that do mutation, there are things that, like.
you know, essentially our extensions to the collector, so maybe something that we could package there. For the cube stuff, I think, like, there's still that open question around, like.
**how do we get this information back without blowing out the API? Yeah, so, like, it may be that we just add that configuration because we can turn it on, but it also may be that, like, the collector can, you know, they want to have, like, a pipeline where that information is coming to the receiver if we subscribe to it or something like that, so… Nikola Grcevski @ Grafana / OpenTelemetry** 07:26 Gotcha.
**Tyler Yahn (Splunk)** 07:27 Yeah, I mean, the answer is, the door is not closed now, yes. It's just, yeah, we need to do the actual work to figure out if it's the right solution, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:35 Right, gotcha. Okay.
**Tyler Yahn (Splunk)** 07:39 But yeah, cool. Yeah, there's… I think there's… I think there's a few things we could probably clean up there as well, but yeah.
Okay.
Moving on, I wanted to ask about, propagating Java trace context. So… at a high level, this is, like, you're welcome to take a look at this PR. It's getting close to being reviewable, But I just… I wanted to ask more at a higher level, if we want to do this. So I was, you know.
We do this in Go, where we're able to propagate context across the language, and it just, I took a look at this.
The only reason I asked this question is it kind of seems obvious that we would want to do this, but we haven't done it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:24 It's just that… Yeah.
**Tyler Yahn (Splunk)** 08:25 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:26 It's great, man, yeah, yeah, it's great, yeah. We should do this, and we should do it for Node.js, too. Like, it… it's just that nobody's… nobody's got into it yet.
**Tyler Yahn (Splunk)** 08:35 Okay. Yeah.
Yeah, I mean, I think that there's obviously, like, this HTTP client stuff is, like, the basic stuff, like HTTP1, right before TLS. There's still, like, a bunch of other things that I'd like to take a look at in Java.
Node.js as well. I actually think at Python, we could also do something here. Like, there's definitely, I think, a very similar approach we could take. So, I think there's, like, 3 languages… 3 more languages we could add context propagation for. For… for, you know, HTTP, but I think there's also stuff in messaging systems, and I mean, there's a whole host of things.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:10 Yeah, 100%, I agree. We should just keep on pushing on this. I think probably the instinct path can be done, too. I don't think it's… we have in the agent.
The correlation all's done, so…
**Tyler Yahn (Splunk)** 09:23 Yeah, actually, I have a prototype for that as well. I think you're right. So, yeah, like, I do think… I think there's, like… I think there's, like, a ton of features that actually can be added. I think our Asian is actually pretty, pretty easy to do this. I don't know… I imagine Gregor is on the call… Nikola Grcevski @ Grafana / OpenTelemetry 09:39 Cheers.
**Tyler Yahn (Splunk)** 09:39 Gregor… yeah, Gregor is on the call. So, I know, Gregor, you've… you're coming from, like, the Java agent world itself, so, yes.
one of the things that, like, I'm doing here, like, it's… it's… obviously, I'd love your review on this, maybe in a little bit, if you wanted to wait till I actually, like, change it, but, like, the idea is essentially just hugging into, like, the methods for, like, these, these, HTTP client send stuff, but… I guess I'm more asking, like, from the Java agent perspective, like.
are there big, holistic things that, like, you want to do right now, if you had to do it over again? Like, to try to just target trace correlation? Like, would you approach this in a different way, or is this a pretty good, solid approach, in your opinion?
**Gregor Zeitlinger** 10:21 I mean, if I would do it differently in Java Agent.
**Tyler Yahn (Splunk)** 10:26 Well, yeah, yeah. I mean, so, I know that the job agent went through a lot of… not a lot, a few different iterations, like, in how they hooked into particular programs, like, and then, like, going into the, like, the, the JFR stuff, even, like, for metrics, like, there was definitely, like, iterations where they dove deeper and deeper into, like, the Java bytecode itself to start doing, like, their hooks.
And this is, at a pretty high level, still, you know, just hooking into actual method calls. I don't know… if you were gonna look at that, like, would you… is this how the Java agent does this? Or, like, even if it is, like, is that the right way to go about it?
**Gregor Zeitlinger** 11:07 I don't know what else you would do. You always have to hook into some methods For… no, sorry, not always.
in some frameworks, you have a callback interface, and that is also being used in the Java agent.
But there's a whole bunch of frameworks where this is not possible or not good enough, and therefore bytecode transformation is used.
**Tyler Yahn (Splunk)** 11:32 Okay.
Yeah, cool. It's more just a sanity check. It may just seem like a stupid question, because it is, but but yeah.
**Gregor Zeitlinger** 11:39 There are those two ways, I just had to think about it.
**Tyler Yahn (Splunk)** 11:43 Cool, alright, yeah.
That sounds good. I will continue, cleaning this up, and then hopefully, actually, I think we should probably get this into a reviewable state soon, and then I'll probably start opening issues, before I actually open other PRs to track all the other work that I was looking at, just to, like, get more feedback in that sense.
This was meant more as a prototype, but then it, like, was… I don't know, it seemed achievable just to do it in a PR, so… Cool.
**Gregor Zeitlinger** 12:10 Yeah, feel free to ping me when, when you want to review.
**Tyler Yahn (Splunk)** 12:14 Okay, I will do that. Thank you.
Okay, next up… I wanted to talk about this dynamic Instrumentation. Yeah, this is exactly what I was looking for. We've got a new, branch on the main repository.
And, it's for this new feature, it's doing these dynamic configuration things for adding dynamic instrumentation.
Which is, really an amazing idea. So, like, I'm really excited about it.
this is the only thing I wanted to ask about, was just, is she tracking some of this work? It looks like you're already… you're already on it. So, yeah.
Cool.
Cool. Also, if folks, are interested in this, or I know the other folks that are, like, you know, maybe taking a look at this, this is the place, I think, maybe we can unify our conversation on it. Looks like Gregor also has, you know, already started work in doing additional, you know, implementation work, so this is great, yeah.
I'm really excited about this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:18 Yeah, me too. That's very awesome.
**Tyler Yahn (Splunk)** 13:22 Okay.
Next up, Gregor, you wanna talk about lightweight connector info? Does it fit OB's scope?
**Gregor Zeitlinger** 13:30 Yeah, so this is a feature, just to be transparent, that is inspired by a Grafana feature in Tempo, and, since this is a useful feature, I want to propose, ask if this would also fit the OP scope.
The related feature that we already have are, metrics for, client, what is it called? I'm messing up the notes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:59 Service graph, service graph metrics.
**Gregor Zeitlinger** 14:01 Thank you, Nikola. Serve Metrics. And the lightweight connection info is a version of that that uses, fewer time series.
And, yeah.
if that would fit Obi, I'm happy to do it there. In fact, I started the POC there.
But we would also implement it in our Baylor distribution if it does not fit here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:32 Yeah, I can maybe add a little bit more color here. So, essentially, the service graph metrics Do have proper histograms, and they do have proper, like, Counts and latency per connection.
Some customers don't want to pay for that. They think it's just too much, and they would rather just have Connectivity graph without having… needing to know exactly how much each of the connections did.
So… It essentially is just a lighter way service graph metrics.
We've had a request from people saying, no, this is costing us too much, we don't want to have this.
But they like to have service graphs.
**Tyler Yahn (Splunk)** 15:19 I mean, it seems reasonable to me, I don't… Yeah, I mean, if… that seems like a res… like, a good approach. Like, definitely reduction in metric size is definitely, I'm sure, a desire for features.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:33 Cool. Yeah, it's an opt-in. I mean, it would be simply, if you want to use the lighter one, you pay less, you get less info, but… Yeah. It costs you much less, and some people just prefer the connectivity, not the actual details per… a request.
**Tyler Yahn (Splunk)** 15:51 Yeah, I… I think it, like, the opt-in approach is, I think, the right way to do it, and so… We find out it was actually the 80%, and then we can maybe move in our V2 to doing that by default, but yeah, I think that that's the way to do it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:04 Cool.
**Tyler Yahn (Splunk)** 16:07 Okay, cool. Gary, you also have the next topic, so… You wanted to talk about mice, I'm guessing, right?
**Gregor Zeitlinger** 16:16 Yeah, I already tried last week, but it wasn't… a little bit half-baked, so now, I created an issue that, Has, all of the There is to know, and… it's not so much about performance as I thought it was, but it's still simpler to do, and in a nutshell, you have your correct version of Clang and Go and so on, whenever you go into the directory or run a MES task, and that is basically the selling point.
And, you can see the tasks, that I have in the PR that I created are named the same as in Make, so it… the look and feel is pretty much the same, but you have to install this No tool.
That's basically it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:17 Yeah, I was initially against this, to be honest, because I was like, yeah, one more build system.
But I think Gregor showing me that, you know, you can… like, for example, like, if I had a certain Clang version on my system.
I would definitely… Mike would just use that.
But this actually allows you to kind of pin the dependency, and it stores all the build tools that you need specifically for your system into a separate, kind of like, private directory on the system, so… your default client could be whatever version, but OB builds with 22. 1.8, and that's what you're gonna get every time you build Obi, which I think is pretty cool.
It's almost like Pi and… In a sense.
You can kind of have your own custom Python version for this folder.
Yeah, it's exactly…
**Gregor Zeitlinger** 18:07 the same idea. It's just that it's not for one particular language, but it's for a tool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:12 everything. Tools, yeah.
**Tyler Yahn (Splunk)** 18:17 Is there any way to just make it backwards compatible?
Meaning that, like, you can keep these make commands, and they just colonize?
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:27 That's good. That's cool.
**Gregor Zeitlinger** 18:29 I… Guess you could do that, I have to check it out, Nikola Grcevski @ Grafana / OpenTelemetry 18:37 Oh, that's a pretty cool idea.
**Tyler Yahn (Splunk)** 18:41 Right, cause then, I mean… If you wanted to use, like, something like this, right, like, maybe you just run mize directly, but, like, if you wanted to… You know, if you wanted to keep any sort of systems or any sort of processes you already had, like, you could just… Not even notice.
Like, maybe, maybe the make command will automatically install mice if it's not there as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:58 Well, yeah, that's a good idea.
**Gregor Zeitlinger** 19:02 I'm not sure if that is what everyone would want, but at least we could, like.
spit out an error and say, you have to install Mies first.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:13 Yeah.
**Tyler Yahn (Splunk)** 19:14 Okay.
**Gregor Zeitlinger** 19:15 Yeah, okay, great feedback, thanks.
**Rafael Roquetto (Isovalent)** 19:17 So, where, where does, for instance, where does the… I'm completely ignorant on this, where does, for instance, it pulls plane from? So it doesn't use Docker anymore, like, doesn't pull a Docker image, or how does that work?
**Gregor Zeitlinger** 19:32 So, it has a registry, but most of the time, you just point it to the GitHub repository, and I can actually open the PR where this is, so I can show you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:50 Yeah, my understanding is it has its own repository of packages, and then it knows how to get to them, similar like any package manager, and it's just gonna pull them into a local cache folder.
**Gregor Zeitlinger** 20:02 Do you see my screen?
**Tyler Yahn (Splunk)** 20:04 Yep.
**Rafael Roquetto (Isovalent)** 20:05 Yeah, yeah, yeah.
**Gregor Zeitlinger** 20:18 So, Clang, yeah, Clang is directly in the native registry, but all it does, it points to a longer version entry like this, And, one other one is Clang Tidy, for example. Here you have the GitHub, Location, where this is…
**Rafael Roquetto (Isovalent)** 20:41 I see. So then it kind of… it's like, go to… it will download the binaries to some sort of cache in my home deer, and we'll use it from there. Yeah. I see.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:51 Cool. Exactly.
**Rafael Roquetto (Isovalent)** 20:52 Alright, that's cool.
Alright, thanks.
**mattia** 20:56 I see that thePF2Go version is pinned as well. What happens, for example, if we forget to update that, but we update the library?
**Gregor Zeitlinger** 21:09 The what Work version?
**mattia** 21:11 The… Nikola Grcevski @ Grafana / OpenTelemetry 21:12 eBPF to go.
The one that's on line 40, because… Yeah.
**Gregor Zeitlinger** 21:19 Okay, if we don't update that, but we update it in Go.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:26 Yeah.
**mattia** 21:27 Yeah.
**Gregor Zeitlinger** 21:27 Yeah, this is, this is something that I usually, prevent, by adding either a test or a renovate rule. I have, similar, scenarios on other projects. I think a unit test in this case would be more appropriate to catch this. So it… when on every CI run, it would tell you if this differs, and then it would just fail.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:56 Or maybe a pre-commit hook.
**Gregor Zeitlinger** 21:59 Yeah, some kind of test.
Could also be a pre-commit hook, right?
**mattia** 22:07 Okay.
**Gregor Zeitlinger** 22:10 Yeah, so I… if you like it in general, then I, of course, would be happy about a detailed, review so that I can take all of that into account.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:24 Yeah, it's good.
**Tyler Yahn (Splunk)** 22:30 Yeah, that sounds good.
Let's, let's, I think, maybe take a closer look.
**Gregor Zeitlinger** 22:36 Yep, thanks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:38 Oh, and I think the real benefit is for newcomers to the project, they don't have to make sure that their dependencies are all matched to whatever we have, right, as they're developing, I think.
It might be easier to bootstrap, but…
**Tyler Yahn (Splunk)** 22:51 I don't know, I feel like that might be long-term, members here as well. I could speak personally.
Okay.
Yeah, no, that's a good point.
Okay, Rafael, last up, you wanted to ask if we can close, an issue?
**Rafael Roquetto (Isovalent)** 23:13 Yeah, that's the one with the Kubernetes metadata, the… the informer.
That looks on a callback, I don't know if you remember that one.
**Tyler Yahn (Splunk)** 23:23 Yeah, it's been a little bit, but I kind of remember this.
**Rafael Roquetto (Isovalent)** 23:28 Okay, so long story short, the issue is if you have a blocking observer that never returns on the on callback, so on is the… you pass a callback to it, that it gets executed, and if the callback blocks, everything blocks.
And I don't believe this is a bug, I think this is, like, this by design. The whole thing is synchronous by design, and I… which is a pretty common approach. I don't, I was reviewing, the assignees, PRs, and that's when I started thinking about it. I said, you know, hold on, I don't think this is an issue, because if… if… Usually, at least in my experience, when you have some sort of synchronous callback, mechanism like this.
I mean, whoever is using that should know that you shouldn't block the handler, and what you're doing? Go is very easy, just spawn a goal routine and return early.
So this is one point that I… I… I have in mind, because otherwise we need to… I had a lot of plumbing for nothing, and then for really quick handlers.
then you're paying the overhead of whatever… another TU, which doesn't really… so much… it's just more complexity for nothing, in my opinion. And then the other point is, I don't think it's an issue at the moment. Like, even… we don't have anything blocking, so it's much simpler to just… You know, got a blocking hinder, the problem is the hinder should fix it, not… not the… this plumbing.
**Tyler Yahn (Splunk)** 25:06 well, okay, it's not about, like, we wrote code that is… Intentionally blocking or slow, it's that, like… it can actually happen in the wild. Like, this is where that came from, was… I was looking at this in, like, a… Yeah, so, like, if you have multiple OBs sitting in some sort of, like, cluster system, and, like, one of them is running on some sort of, like, reduced CPU usage, or it is… it is getting, like, constrained in any way, like, this… this process itself can become constrained. And in the process becoming constrained, that means all of the other clustered OBs, therefore, are… are… Are held up on this process.
**Rafael Roquetto (Isovalent)** 25:45 Are you sure?
I mean, maybe I'm just…
**Tyler Yahn (Splunk)** 25:48 It's been a while.
**Rafael Roquetto (Isovalent)** 25:49 the issue?
Yeah, like, if I understood, like, if you go to the… if you look at these, I don't know, the Blockium server code there.
But maybe I misunderstood the issue. Like, Basically, you pass the informer event.
If that on blocks, it blocks the current process, right?
Like, if, any… the on method there, on the blockyObserver blocks, Then the whole… Things stops flowing.
And then the process stops, and then whatever happens because the process stops, you know, goes downstream, there's a side effect of that.
But what I'm arguing is that if there is a handler that's blocking.
it's up to the handle not to block by, you know, dispatching it to a separate thread or something, instead of us, the plumbing itself having to change. That's… that's my point. Like, which is, you know, in… It's a pretty common… pattern, like, when you're dealing with callbacks or event handlers, like, you don't assume the… whoever's invoking the event handler is asynchronous.
And… unless you know for sure, it gives you a guarantee in the contract, and therefore, you know, usually on callback paths, you basically make it quick, or dispatch to a separate thread for processing.
But this should be up to the hinder, in my opinion, not to the invoker.
**Tyler Yahn (Splunk)** 27:19 Yeah, but do we.
**Rafael Roquetto (Isovalent)** 27:20 And then…
**Tyler Yahn (Splunk)** 27:20 handlers?
**Rafael Roquetto (Isovalent)** 27:22 I think so, right? This is… or that's the part I might be missing, then. I was under the impression that that this is all internal, but maybe I misread everything, so I'm gonna go have a look again.
**Tyler Yahn (Splunk)** 27:36 Well, I mean, I… I… even if it is, like, I was having stalled… OB's causing, like, downstream, and this is the case that I created. I don't know… it's been a while since I've looked at this, so I may be misremembering things, but, like.
Yeah, like, that was… this was just a test reproducing this idea, like, and it was showing it locally, but, like, it was a… it was a clustered behavior event that I was actually seeing.
**Rafael Roquetto (Isovalent)** 27:59 Okay. If… if we're having stalled OBIS, then I would be curious to see why it was stalling, because obviously, if we… if we do anything like this, where the on becomes asynchronous, and… I don't know how we would implement that properly, I mean, it's possible, but, like, for instance, what the guy was saying.
It was just adding another queue on top of a queue, you know, it's just pushing the problem downstream, in a way, but that aside, that's just, like, doesn't have to be done like this.
I would be curious to know why a handler is blocking. Like, why is it OB blocking? Because it might be… Maybe this is the only way to fix it, but maybe…
**Tyler Yahn (Splunk)** 28:41 Well, I don't.
**Rafael Roquetto (Isovalent)** 28:41 Like, covering the bug.
**Tyler Yahn (Splunk)** 28:43 I don't know if that's, like, the right way to fix it either, though. Yeah, I kind of agree with you, like, not pushing it downstream, but I do think that, like.
If you have, like, a fan-out implementation, you can also have, you know.
A correctness avenue, where essentially you fire and forget, so you pass it off to somebody, and you put that, like… in a way where you're expecting them to have some sort of callback, or you can spawn the go routine yourself, and, like, just move on. But, like… Yeah, like, you know, having a fan-out architecture made just you want to do that, like, fire and forget, rather than, you know, more of a UDP idea, it was kind of what I was thinking, but like… Yeah, I mean, like, I guess you could try to build in, you know, a correctness pattern the whole way down, but it was more of having it just be lossy. Like, having something that's going to time out or be slow, like.
Lose the information and not cause other things downstream to fail.
**Rafael Roquetto (Isovalent)** 29:39 I'm not completely opposed to that, I just think it comes with a trade-off. Like, if you look at the two PRs that were raised on that, it did massively complicating things, that now it's just basically, if you look at the implementation, I think it was the basenodifier.notify.
from the top of my mind, I could be wrong. It's a pretty straightforward, like, 10-line thing is a loop that loops off over all the notifiers and invokes them. I think that was it, but and then the whole thing becomes very complicated.
So I wasn't convinced, okay, is it worth all this code? Then we have to maintain, test, and make sure it's correct. If there is… Someone blocking somewhere that shouldn't be blocking, and then you just, like, spawn a go routine or something like that.
It becomes… it adds another queue, like, this implementation adds another queue, it does… a lot of things, so I would like to understand why it's blocking. Maybe it's not reproducible? I mean, with your use case there, obviously it forces blocking, but I would argue that blocking handler is wrong by design, because it shouldn't block, it should… You know, dispatch it.
But if there is a real use case where some other process, like this thing is chain rea… there's a chain reaction where it's causing to block it, it's outside of our control, then I agree. Then we gotta do something about it. We can be… held hostages of external processes, but I… maybe I misunderstood, I thought it was somewhat internal.
somewhere in the hinders.
**Tyler Yahn (Splunk)** 31:14 Yeah, I mean, I can go back and take a look. Like I said, I may be, misremembering, but, yeah. It's from April, so yeah, like… Yeah, I, I, I… It was a real issue, or I… one of the issues that I opened was a real issue. Maybe this isn't the one I'm thinking of, but yeah, it looks like it is, so I could take another look.
**Rafael Roquetto (Isovalent)** 31:33 Okay, I'll have another look as well, and then we can, chat asynchronously, and… or on the issue, actually, it's better, because then… and then… and then we take it from there.
**Tyler Yahn (Splunk)** 31:43 Yeah, that sounds good, yeah.
**Rafael Roquetto (Isovalent)** 31:45 Okay, cool, thanks.
**Tyler Yahn (Splunk)** 31:46 Yeah.
Okay.
Cool.
Alright, that's the end of the written agenda. Any other… Topics folks had in mind?
Mattias moved on to the next generation. He doesn't even run his own commands.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:11 That's pretty true.
**Tyler Yahn (Splunk)** 32:12 The referral.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:13 Okay, the meis would be easier even for the agent to set it up, right? It can just download the dependencies and everything, so you don't have to even… Install anything on your system, I guess.
Is that a good…
**Rafael Roquetto (Isovalent)** 32:26 What do you get there, it's just AI.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:28 learning.
**Rafael Roquetto (Isovalent)** 32:28 you know, material.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:29 Yeah.
**Rafael Roquetto (Isovalent)** 32:29 beach.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 32:32 Speaking of randomly downloading things from the internet,
**mattia** 32:35 You caught me.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 32:39 The… I don't know if we need to bump to, go 126.10, This, vulnerability that's out with, Certificates and things.
I don't know if anyone's looked at this yet. If not, I can… I can do the bump.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:56 Express Renovators.
**Tyler Yahn (Splunk)** 32:57 Hasn't picked it up, but yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:59 I think we got a security report or something. I got in, I think it was a GitHub, that notification about security, but Renovate hasn't kicked in yet, yeah.
**Tyler Yahn (Splunk)** 33:12 Yeah, and then there's also, if it's a GitHub security notification, you can usually have Dependabot also do it as well.
But, yeah, Steven, if you wanted to just go ahead and make the PR, that sounds good, too.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 33:24 Yeah, I don't know if, renovate and Dependabot.
Because we still have this multi-step, like, we need to update the build image first.
**Tyler Yahn (Splunk)** 33:34 for our…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 33:35 Yeah. Published that.
**Tyler Yahn (Splunk)** 33:38 Rights.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 33:40 So, well, I'll go ahead and do that.
**Tyler Yahn (Splunk)** 33:43 Okay, yeah, alright, this one's good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:46 Cool. I just wanted to bring, one topic. I started working on that peer metadata exchange between different versions of OB. I put up a PR out there.
Going through the co-pilot preview for now, I think I resolved the last issue, but essentially, outside of Kubernetes.
We'll start exchange, if it's enabled by, through an option.
Obis can start exchanging information with one another about What their services are, so that… We can complete peer information and service graphs and all that stuff.
So…
**Tyler Yahn (Splunk)** 34:21 This is, like, the kube metadata, like, API, essentially, but it's outside of Kubernet? Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:26 Yeah, outside of, so, no cache, and I think Mario, mentioned to me, that he might be looking at to make the centralized cache so he can deploy it in that mode too, hopefully using the same principles and the same format for the request responses, but this is more like peer-to-peer. So, it's not doing anything for… Yeah, it's not doing any broadcasts, it just simply says, oh, I see something on my network, I have detection of what's my network, that… I'm talking to, I don't know the name of that service, it has an IP. Let me see if there's an OB there on that side, so I can ask it for this information.
And then…
**Tyler Yahn (Splunk)** 35:11 How does discovery work? Like, how does it know where all the other OBs are?
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:14 Well, technically, it just looks at the IP addresses of the stuff it doesn't know. So, it saw an IP address, I don't have any metadata about that service, I don't know what that is, but let's try to see if there's an OB on that IP address, essentially.
**Tyler Yahn (Splunk)** 35:29 Oh, so, so it's like… I know that it should be listening on port whatever, so it's just gonna say, like, hey, this IP address… so, okay.
How, so… what happens, though, if Obi's not making any sort of communication that it's gonna see? Because doesn't that mean that, like, OB has to talk to a service it knows?
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:50 Yeah, it talks to another OB, so essentially, I just say, on this board, that's our listener port.
for the metadata exchange, and if that service has a port open, if that IP has that port open on that side, it will try to talk to it, essentially.
**Tyler Yahn (Splunk)** 36:05 Yeah, but, like, so… so say, like, so say Obi's, like, monitoring, you know, service A talking to B or something like that, right? Yeah, yeah, yeah. And then there's another OB monitoring C talking to D, right? Yeah. But, like, that second OB's never gonna talk to service A or B.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:24 No, but… okay, so A and B… are monitored by OB-Wan, let's say.
**Tyler Yahn (Splunk)** 36:30 Yeah, yes, Obi- yeah, sure.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:32 B, like, C and D are monitored by OB2.
So, if Obi-Wan sees that A is talking to C, which is not monitored by the same Obi, they will say, okay, I see an IP address over there, that… I don't know what that is.
and then it just proactively says, is there an OB2 there that will listen on this board and give me metadata about what that service is?
**Tyler Yahn (Splunk)** 36:57 Oh, okay, so it's just assuming that Obi's listening on the same IP address, because it'll be on the same host? Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:02 Yeah, yeah.
**Tyler Yahn (Splunk)** 37:03 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:03 And if it's not there, it's not there. So if you don't configure it, it's just gonna say, okay, there's nothing listed on that port, I'm gonna stop asking for it, so I'm sort of blind, I have no idea.
what the PR name is, but, So I was trying to do the same thing, peer-to-peer, of… And the way it's done, it's like, it's not talking every time, it builds these caches, there's… there's time to live, and after that time to live, it tries to refresh the metadata, so it's not gonna… just keep on sending requests all the time, it just periodically scans metadata from remote ones.
That he knows off.
**Tyler Yahn (Splunk)** 37:39 So, could you, This sounds good, and, like, I think we should stay right where we're at, for what you just described for, like, the initial one. But, like, can you see the, like, this being expanded into, like, having a more, like, robust discovery protocol where you could seed it with other OBs from, like, a configuration?
And then in the protocol itself, like, when you ask OB, not only, like, what do these IPs mean, but also you could ask that same OB, like, what other OBs do you know about, or what other, like, data do you know about?
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:10 Yeah, yeah, we can expand it like that.
Okay.
**Tyler Yahn (Splunk)** 38:13 Alright.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:13 Yeah.
Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 38:15 But the IPs are going to be changing all the time there, right? So, is it really suitable for configuration? You've got, like, auto-scaling groups, and you've got nodes coming up and down all over?
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:24 I mean, you can do ciders.
You can do ciders.
Yeah.
**Tyler Yahn (Splunk)** 38:29 I think it should be as well, because you're not running in Kubernetes, right? Like, those… I would expect in that situation, the IPs might be a little bit more stable.
I guess maybe not, maybe we're talking about, like, EC2 instances or something like that?
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:41 Yeah, red, red, red, blue, green, blue, blue, green deploys, and stuff like that.
**Tyler Yahn (Splunk)** 38:46 Yeah, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:47 Yeah.
So, I mean, like.
**Tyler Yahn (Splunk)** 38:49 If that's the case, like, these precedings doesn't really make any sense, but, like, the… like, the total totality of it might make sense, you know?
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:58 Yeah.
**Nimrod Avni** 39:00 How about, like, Like, security aspect of, like, you're just… you're just pinging a random, like, a port on… on some random server, and you expect to… share information between each other, and, like, I don't know. Especially if you're expanding it to, like, bring me other OBs, and then, like, you fan out to even more servers. I don't know if we… I mean, it's interesting if we can… if there's some way we can, like… verify that something, you know, I guess no secret exchange, that'll be probably too much, but I don't know if we can… Nikola Grcevski @ Grafana / OpenTelemetry 39:37 Yeah, yeah, I… I thought about that.
**Nimrod Avni** 39:39 Or do it on Secret Key or something, and hoping they'll share it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:43 Yeah, so there is that. So I added that support, so there's HTTPS added, and there's a Bayer token, so you configure your OBs to have that token, and they secretly communicate if you're worried about security.
I even added the certificate authority, if you have one, that you can configure that will do that. So, all that is implemented, so… It's optional features, so you don't have to enable it. If people are security conscious, and they don't want this kind of exchange, they can hopefully, when Mario implements the central repository.
But that requires more deployment overhead, right? So for somebody outside of Kubernetes, this is a little more complicated, because now they have to start a VM with a central CubeCash sort of equivalent.
That is true.
**Nimrod Avni** 40:30 even, like, if you're using OB… in Kubernetes, you can even kind of replace the cache with this, like… it reminds me of… it's some kind of, like, gossip protocol, like… Nikola Grcevski @ Grafana / OpenTelemetry 40:43 Yeah, exactly, yeah.
**Nimrod Avni** 40:45 Talking between each other, so you can kind of replace the cubecache if… If you don't want to run that… Nikola Grcevski @ Grafana / OpenTelemetry 40:51 Yeah, so right now, in this first implementation, I just consider if we have Kubernetes, I turn this off, but… Having said that, you're absolutely right, we could potentially build it to support Kubernetes in a more lighter weight than having a global kubecache and having the metadata of all services. You can start pulling the metadata from remote.
about the services you care about. So, each individual OB cares about these ones. It doesn't have to care about something completely unrelated in the cluster, because in the services it's monitoring, never talk to those other guys. So, potentially reduce the memory with this concept.
There's a couple of gotchas there. I mean, I read through the PR, I thought about, long and hard, about how do I make it The best possible, but there's still gonna be places where we can't.
The main challenge is ambiguity.
Right.
I mean, it's unlikely, but it will happen, that people on… will put two separate clients on a single VM that will talk to a server. So now, coming to the server, you have no idea which client is talking to you.
So you can't disambiguate between which service is talking to you.
But, I mean, in that case, it degrades into trying to get that host name.
So it's pleased to know the host.
Rather than the IP address.
But for most standard scenarios, when people put, like, NGINX, then an application layer, and then a database, those kind of scenarios, I think.
Well, will function properly.
I mean, I don't know how complex people's setups go with VMs, and how difficult That's how many difficult scenarios there will be, but this will not handle everything, but it'll handle something, so… Better than… I mean… maybe 70-80% of the scenarios that people deploy, like, I don't know, I have a Rails application front-ended by Apache, and I have a SQL database at the back, this will work, so…
**Gregor Zeitlinger** 43:06 I'm wondering if this autoscaling problem, if this could somehow be tackled So, let's say you… you get another client from the same service that is talking to you. Can you somehow figure out That, that this is a client of the same service type by… because it's somehow talking to the same endpoint or something like that?
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:33 Yeah, it does some of that.
I tried to do some bingery to figure out if the service name was the same, and then I consider it that's okay. If the service name is the same. Let's say you have, like, some scaled parent process, like a Python that runs multiple subprocesses, that's all there. So, if the service names match, it considers those PIDs as non… Ambiguous?
Because they will all inherit the same service name.
by OB, right? OB will find that all named the same.
So then, that's not… Ambiguous.
But, if somebody created a Python and a Ruby application, and they all talk to the same backend.
from the same VM, then… yeah, that doesn't work. I can't tell them apart on the server side. I can tell them apart from the client side, but not on the server side.
it is kind of smart, like, it does support, if one service on one VM, talks to another service, another VM, but they use different ports, that works. But if it's the same port, multiple clients, then… Because I use the server port as a key identifier in the…
**Tyler Yahn (Splunk)** 45:06 Okay. Cool, yeah, we'll have to take a look at the PR. Thanks for… thanks for bringing that up, I think that's really interesting. Definitely something that would be helpful.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:15 Yeah, we're trying to get this non-Kubernetes story to be much better, here internally Grafana.
for the… for the OB project, and so… Yeah, no, we've… yeah, we focused a lot on Kubernetes, and… but there's so many people that just don't run Kubernetes.
**Tyler Yahn (Splunk)** 45:34 I just keep, realizing there's still so much work to do, even though it's already… Nikola Grcevski @ Grafana / OpenTelemetry 45:38 Yeah.
**Tyler Yahn (Splunk)** 45:39 lot of awesomeness.
Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:41 Yeah, there's a lot of good stuff, but there's so much work to do. I agree. Yeah.
But I have to say, actually, I'm quite optimistic, because we did all that work to kind of find the names of services. It kind of works pretty well. I'm actually surprised. I've been trying it on various things, and it gets it every time, so I'm optimistic about that.
Haven't found a… A deficiency, yeah.
**Tyler Yahn (Splunk)** 46:06 Yeah, nice, okay.
Sounds good.
Okay, any other topics folks had, or… Things that they're working on.
**Nimrod Avni** 46:18 Yeah, I actually kind of tried playing around. I think someone, we previously mentioned, I'll send it in the chat, the… semantic convention conformance, REPL, which, basically, like, does comparisons, like, runs a bunch of test scenarios against different SDKs, and, basically says which, I don't know, the correct… both the correctness and the, like, how much of the schema to cover. So I started playing around with, like, adding Obi to it.
I have an issue, and I have some, like, draft PRs on my end.
it works, and, like, it's really cool, like, we cover… and it's nice because you, like… instead, you, like, you can compare OB to every SDK on every scenario, because we cover everything, and not just a particular language or protocol.
I had some rough times trying the, like, the instrumentation part is basically, you have, like, a very short-lived process that lives for, like, 100 milliseconds, then closes, so I had to do some hacks there, and I'm also hoping the PR now to kind of help us improve that with instrumenting short-lived processes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:28 Oh, that'll be awesome.
**Nimrod Avni** 47:30 So, once I… and also, I may find a bunch of bugs, which I'll open, but once I have something up there, I'll let you know there. I'll let you know here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:44 Yeah, it's great. Yeah, I've been thinking about the short-lived processes as well.
It's almost like the challenge is… To metadata, by the time we find what the language is and instrument it, it goes away.
**Nimrod Avni** 47:59 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:01 But I was thinking that maybe… And especially as important, like, they… I don't know if you're following, they have this agent substrates.
It's a new concept in Kubernetes. They've figured out that for agents, they don't want to run pods.
Apparently, because pods are too heavy and sort of longer-lived than agents would need to be, and all these agents take so much resources, they work with GPUs, that's a scarce resource and whatnot. So they're working on this concept called substrates, and substrates, I guess, and it's something that can just go away. Run for a while, and then get parked, almost like frozen.
In memory, and it got offloaded, and then brought back up to life in Kubernetes.
And we will not do well there.
Because… technically, from a PID perspective, the pit dies and then gets resurrected as a new pit.
But the metadata is the same, so I was thinking of maybe we start process it once, get all the way, realize it's dead, but then cache it, and then it comes back up. We realize, oh, it's the same inode or something. Yeah, this substrates, yes, that's it.
And then, then we can actually, sort of.
Capture the telemetry much quicker, because we know it's,
**Nimrod Avni** 49:29 Yeah, even, like, I think we had something similar to this, like, instead of some schedule that scrapes all the processes, we, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:41 Yeah.
**Nimrod Avni** 49:42 them live via, like, eBPFS or something.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:44 Yeah, ExitV and Fork, and yeah, yeah, yeah. We need something to do something like that, just like we do with the OpenPort, that immediately drives Instrumentation pipeline, so this should do too, and… Capture the telemetry, maybe buffer it?
Until the processing pipeline Finishes, and then… Decorate it, push it forward, yeah.
**Nimrod Avni** 50:10 Yeah, right now I'm just, like, creating the process and saying, like, you know, hold until OB… like, I scrape OB internal metrics until we find it discovered, and then, like, okay, continue. Do your thing.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:21 Yeah, yeah, yeah, yeah.
**Nimrod Avni** 50:23 Kind of awkward, but… Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:27 Cool.
**Tyler Yahn (Splunk)** 50:33 Well, cool, yeah, definitely. Please let us know when there's something to take a look at. Yeah, I'm interested. I'm sure Trask is really excited about that, too, so, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:41 Yeah, very exciting.
Cool.
**Tyler Yahn (Splunk)** 50:43 Yeah.
Awesome. Alright, well, that looks like the end. If, folks have more things to talk about, please go ahead and, message us in Slack, otherwise, yeah, we could probably end the meeting here.
Thanks, everyone, for joining. We'll see you all in a week's time, or asynchronously. Until then. Bye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:02 Bye now.
**Gregor Zeitlinger** 51:02 Bye.
