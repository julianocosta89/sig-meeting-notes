SIG: Collector SIG
Date: 2026-03-11
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Andrzej Stencel** 02:28 It's not easy to fill in the… Attendee list.
**atoulme** 02:34 Hello.
**Andrzej Stencel** 03:56 We have a lot of people, but not many topics to talk about.
**atoulme** 04:04 Yep.
Please put your info into the doc if you have. If you have any items you want to talk about, this is the time. Put it in the agenda, otherwise it's going to be a very short meeting.
**jmacdonald** 04:34 Antoine, I'm having trouble opening the doc… the meeting notes. Is there some change of the document or permissions?
Or could you paste a link to see if that's the right one?
**atoulme** 04:43 Yeah, it's in the… okay, thank you. Yeah, someone just pasted it in the chat again.
I guess someone needs to go fix that agenda item. I think the doc changed, and the invite did not change.
**Jade Guiton** 05:00 I… I'm pretty sure it's changed at this point.
You may need to, like…
**atoulme** 05:06 Whoa.
**Jade Guiton** 05:07 New version of the calendar invite from the official calendar, though?
**jmacdonald** 05:10 Oh, okay, that's what happened. That makes sense. Calendars are hard.
Especially when you use Outlook.
**atoulme** 05:17 Outlook is hard.
**jmacdonald** 05:20 Thank God.
Okay, well, I've been speaking now, so here's a question. Does anybody have an agenda item other than the standing item that's at the top of the notes there?
**Blake Rouse** 05:35 I do. It was actually just a call-out for the RFC for… I was gonna put it in there at the link.
or partial reload on the collector. I was just trying to get more eyes on it. I put it in the Slack channel.
As well. So, I'm just gonna put the link in here. It's just a call out for… we had talked about it in this call before, gone through the RFC, and it's kind of just sitting there in the process, so if anyone has any comments or anything to look at?
or any comments about the RFC, that would be great.
That's… that's all I really have.
**jmacdonald** 06:15 Thanks, Blake. I'm gonna try and find… I hear… I found it, Yeah, I put it in the… I finally got it in the document, too. There you go, okay. And, why don't I… I don't know, why don't I share, since I'm here?
So, I do remember you discussing this at least once.
Yep.
And I…
**atoulme** 06:38 will say that I haven't read your RFC.
**jmacdonald** 06:40 I was just being honest.
But catching up here, this is a request for all of us to review, appreciate that. And, would you like to just give us a, like, one-minute rundown or two-minute rundown, Blake, since we… you have our ears?
**Blake Rouse** 06:56 Sure, yeah, so the rundown on this is… motivation behind this is, extending the, way Graph is built to support partial reloading. And by partial reloading, I mean the code would analyze the difference between what it currently has and what it needs to get to, and make those changes. It would result in restarting any of the components that have changed.
And depending on its position in the pipeline would result in other components being restarted that make that basically graph through the pipeline. So, example being, if a processor changed, the processors would be restarted, and the receivers would be restarted, but the exporters would not be restarted. And you know, and then obviously there's the divide between pipelines. If you change something in a logs pipeline, it doesn't restart any of the metrics pipeline. So any of those things, are done in Divide. The motivations here highlight motivations between why restarting these all the time based on a change that's unrelated to this change is bad, and the issues that it causes, and how, you know, having this in the collector core would be beneficial. Also talks about how a feature flag would be used to where this would not touch any of the current pieces of core, so providing stability to what Core has today, and then also talk… I don't know if it's in here, but just to call out, from an elastic standpoint, we would enable it as soon as the feature flag was available, and we would be using it, in production.
For that. Cool. And there's been some other people on here that have highlighted some other things, like in the profiler, which was donated to the collector, where restarting is quite heavy, so not restarting in that regard is good as well, so… That's kind of the… longer than 2 minutes, but shorter than 5.
**atoulme** 09:03 Is it okay if I ask you a few questions?
**Blake Rouse** 09:07 Huh?
If everyone else is on the call's fine with it, I'm fine with it, yeah.
**jmacdonald** 09:10 Sounds good. Let's do it.
**atoulme** 09:12 So, Blake, do you have a prototype of this working?
**Blake Rouse** 09:16 I do. There's actually a PR of it.
**atoulme** 09:19 Okay.
**Blake Rouse** 09:20 Yep.
**atoulme** 09:21 on.
**Blake Rouse** 09:21 PR. I actually have two PRs, one is just doing it for the receivers, and one is taking it all the way to the end.
And doing, like, the whole thing. Obviously, we wouldn't merge that one like that, we would do it in pieces, but yeah, there's a prototype.
**atoulme** 09:35 Do you have a… what is your contention when, let's say, you have multiple partial reloads?
Is that even possible?
**Blake Rouse** 09:44 Give me what you mean by multiple partial revolts.
**atoulme** 09:47 Let's say you have two requests at the same time to reload two different pipelines.
**Blake Rouse** 09:52 So you… so you're… so you reload the config and both pipelines are changing?
**atoulme** 09:56 Yeah, or, but not at the same time.
**Blake Rouse** 10:00 Well, so it would be the first one, and then when that one's complete, then we'd perform the second one.
**atoulme** 10:05 Okay, so this is a queue, okay.
**Blake Rouse** 10:06 Yeah, yeah, it's a key.
**atoulme** 10:07 Okay, good to know. Okay. Is that… is that spelled out? Is there… is there a contention there? Is there a way to wait for a reload? How does that…
**Blake Rouse** 10:17 Calling reload… when the SIGUP happens and the reload, it is, blocking. Like, it won't take another SIGUP until that one completes.
**atoulme** 10:29 Oh, you're doing this through SIGAP, so the SIGAP only, like.
**Blake Rouse** 10:32 Well, no, it's not through SIGAT, I was just saying, like, SIGA, it's any time a wash occurs, right? So, like, when a wash occurs on a config watcher, like the config profile, it will not… it's like a serialized loop, so, like, it performs the action and then comes back. Does that make sense?
**atoulme** 10:49 It does. Is there an agent management hook into this discussion, or no?
**Blake Rouse** 10:54 I've brought it up in the off-amp, calls, they… and they are interested in it. I'm trying to get their eyes on it as well, if that's what you mean from the… from the.
**atoulme** 11:03 That's what I mean. Thank you.
**Blake Rouse** 11:05 I've been joining the OpAMP6 and trying to bring attention to them. And they were very interested in it. They're also interested in the future… they kind of already kind of wanted to jump, and I said, I think we will get there to the future possibility, which is highlighted at the end.
Which is, hot reload. There are some cases where they just want to change, say, like, the sample rate, and the fact that we're restarting the whole collector just to change the sample rate, but even the fact they even restart anything to change the sample rate, they want to take it to the next level and have a reload interface for some components. If you implement that reload interface, then you can dynamically reload without any restarting.
And so that's kind of like a feature thing as well.
**atoulme** 11:45 Yep.
That's interesting. Okay.
Okay, thanks.
**Blake Rouse** 11:51 Yep.
**jmacdonald** 11:54 Yeah, I understand that there's two levels here. One is you can start and stop components using the ordinary component interface, shut them down, restart them, and you're using, essentially, a topographical sort, I guess. And then the hot reload would be, like, more like sending a message or calling interface saying, you know, you are part of a pipeline, we're not changing that, but here's a new configuration for you. And we vetted, I guess, that there's no, like.
You know, external change there. So, like, you know, if you have edges leading to other nodes, that the edges aren't changing in that case, because that would be a larger change.
**Blake Rouse** 12:31 Right, correct. It would have to… yeah, so, like, I think this just becomes, like, a little bit more of a… we do this first, then we add that next, because what… that next piece would look at it and say, like, okay.
you know, here's what's changing. Is everything that's changing? Support hot reload? If it does, we can go down that path. If not, then we're gonna have to do something like, we'll have to restart, you know.
Even if it supports reload, it might have to be restarted, because something else has changed in its path that requires the whole piece to restart.
**Andy Keller** 13:03 Yeah, just for some context, Blake and I… Blake did bring this to the AMP SIG, and we've talked about it there, and And that's where I was talking to him about some ideas we've had on, You know, maybe a way to ask a component if it can support this new configuration without rebuilding the pipeline, and leaving it kind of component by component, and… but that's really follow-on effort, and I don't think incompatible with this effort.
**jmacdonald** 13:36 Yeah, that sounds doable. There's something I've been working on, the OpenPR about component interfaces, and as long as we respect the component interface guidelines, you know, adding a new interface that you can check, you know, do you implement this, is okay, as long as we follow the rules.
Cool. Yeah, this sounds good to me. I haven't actually looked… so, there are two issues linked here. Did you say there was a PR we could look at to tell us, the size? Is that what the PRR… yeah.
Is there a PR? That's my question.
**Blake Rouse** 14:07 Yeah, there is a PR, the full PR is… is… is very large.
**jmacdonald** 14:13 I think that was my question, which is sort of, like, how big is the change? Is it sort of, like, hidden in the graph package, which is an internal package, or is it, like, spreading around the whole repo? You know, does it factor.
**Blake Rouse** 14:26 No, it actually is just in, service internal graph?
And barely in service. It's all in graph, so basically.
**jmacdonald** 14:37 That sounds better. You know, like, a large PR is okay if it's in one place. If it's spread across the repo, those become tricky.
**Blake Rouse** 14:43 No, no, it's all in one place, and like I said, it does use a feature flag to keep it isolated. So, like, without the feature flag on, Current path.
New feature… feature flag on, sorry, feature flag off, current path, feature flag on, new path, new functions, new everything.
Obviously trying to reuse what can be reused, but it doesn't… I guess what I'm saying is there's, like, no even modify lines in the graph, like, it's all…
**jmacdonald** 15:08 Okay, so you basically… so yeah, maybe, As a potential future reviewer of this work, my request is always that you sort of try to avoid, like, unnecessary change for a large PR. Like, if you can make a new file, like, that helps us read it, because you're not touching the old file and that sort of thing. Like, reviewing the diffs and saying, oh, this is an accident, I don't need to make that change will help, just to bring down the size of the PR.
Yes.
request.
**Blake Rouse** 15:33 So, yeah, I can move… probably most of us could live next to Graph, like, in, like, Graph… like, partial or something, and put it there.
**jmacdonald** 15:42 too.
**Blake Rouse** 15:43 Yeah, Graph 2, I don't know, like, yeah, we could do something like that. Yeah, that's just… PR, would you… I guess I can put… should… would you… would it be good for me to put this PR link in that description of the…
**jmacdonald** 15:56 Yeah, that would help. I think that would help. Sure. It's just so, so someone who's reading the RFC can kind of glance at it and say, oh yeah, this is huge, bigger than I expected, or this is large, but write what I expected, for example.
**Blake Rouse** 16:09 Okay, yeah, I'll update the description to add that.
**jmacdonald** 16:12 Cool, thank you. Alright, this is a request for all of us to review this. Rfcs are important changes.
Oh, well, thank you, Blake.
**Blake Rouse** 16:22 No, I…
**Jade Guiton** 16:22 I can't signify.
**Blake Rouse** 16:23 I'm looking at it.
**jmacdonald** 16:24 More questions.
**Jade Guiton** 16:26 Yes, so we've talked about this partial reload idea before, and I guess one thing I'd like to clarify is that Is the motivation, like, the use case, specifically when you have multiple pipelines, and you want to reload one receiver in one pipeline, but not in another pipeline?
**Blake Rouse** 16:49 No, and our specific… our first use case… we have a lot of use cases for this, but our first use case is that you're adding a new receiver to an existing pipeline.
**Jade Guiton** 16:58 Hmm.
I see, that makes sense.
Right, I just wanted to understand if this was about minimizing the downtime when you're reloading one specific receiver… minimizing the downtime on the receiver when you're reloading it, but it sounds like it's more about minimizing downtime on other unrelated receivers, essentially.
**Blake Rouse** 17:19 Yes, definitely more about related receivers, yes.
They already, you know, they already have events in the pipeline, they're already flowing, we don't want to… all the, you know, stop all that stuff just to add one new receiver. That's just easy to just… Plug in, right?
**Jade Guiton** 17:37 Hmm, makes sense.
Are you muted, Josh, if you're talking?
**Andrzej Stencel** 18:01 Josh?
You're muted.
**jmacdonald** 18:07 Well, now that I'm speaking, I'll continue unless someone wants to run the meeting. So, I'm gonna move backwards in the agenda and suggest we talk about Paulo's topic next. Thank you.
**Paulo Janotti** 18:23 Very briefly, so we've been doing, Windows, AMD quite some time as Tier 2, and I, I'm happy to report that we have had getting, I think, in the next… next… last 8 months, kind of good contributions on Windows.
both for bug fixes and additional features that were kind of, very natural for Windows, AD-related stuff, this kind of thing.
And, I can list in the issue, the contributions, so it becomes clear who are the people that are involved.
But, I think we are kind of, we have, kind of, enough contributors working on Windows that we can consider moving Windows AMD to Tier 1 support.
And, the Windows arm, we are actually doing more than what we did for 386.
And, the consideration there is that, for me, I think it's very natural that we move this to Windows, to support Tier 2. I have a machine. If, if we need, I have a Windows arm at hand, and we have the runners.
So, I think for Windows Arm, it's more kind of, hey, we are doing this already for Windows AMD, so let's bump Windows Arm to that level. And the first one is.
as I said, I haven't been seeing good contributions coming on the Windows side in the last 8 months, and I think there is enough people that care about that deployment for us to move to Tier 1.
**jmacdonald** 20:26 I would second that. I'm obviously biased by my employer being Microsoft, but I've also noticed this contributor, Douglas Kamata, in the last year, really stepping up Windows support, so just because of Douglas' involvement, I would be willing to say yes on that one, too.
he's not in the room, otherwise I would, you know… Applaud him, for that.
**Paulo Janotti** 20:47 Yeah, yeah, I've been in contact with him, quite a bit, about some, issues and, deployments and these things, and he's on top of the things, too.
**jmacdonald** 20:59 Yeah. Well, you have my support. I don't know if there's a vote we need to take, or how this issue moves forward. Other than, you know, I'll be glad to stamp my approval on this issue. Is there… who's the deciding party at this point? I mean, the maintainers… I'm not one of the maintainers. May I ask, who would decide this?
**Andrzej Stencel** 21:22 I think we don't have a process for that, right, Antoine?
**atoulme** 21:25 Yeah, it's just rough consensus, I guess. Just, you know, it's been open long enough, no one's complaining, let's do it.
**jmacdonald** 21:32 Okay, well, I propose that if you support Windows and you're on the call right now, go add your, you know, thumbs up on this issue one way or another. If you don't support it, that's actually more important, and give us the reasons why.
**atoulme** 21:47 So that's your consensus, right? So if you want, you can also say, you have about a week to make your case known. If in a week we don't hear back, it's happening.
**jmacdonald** 21:59 Okay, yeah.
I'll be… I'll be glad to write that sentence as well.
**atoulme** 22:05 I can do that.
**jmacdonald** 22:06 Okay, Antoine, why don't you do that? Thank you. And I'm gonna put my thumbs up on it.
**atoulme** 22:12 Thank you, sir.
**jmacdonald** 22:12 And just to declare my… myself.
I'm a Microsoft employee. So… Very good. And the ARM stuff, too, I know we're, yes, we want that. Thank you. Well, I propose we move on to Mikolai.
**Mikołaj Świątek** 22:36 Yep, since we're here and we don't have anything in the agenda, I wanted to bring up this little thing that came up when I was working on status reporting for components.
So, just so… for anyone who isn't aware how this works exactly, inside the collector, there is a state machine that enforces state transitions for the components. So, for example, if you're in a okay state, you cannot move back to a starting state.
If you try to do that, then it will just be quietly dropped.
Nope.
what the machine… the machine was actually quite strict, and what it was doing, like, for example, if you got an okay… if you're in an okay status, and you tried to send another OK status, it would also drop that.
That I fixed, because we now have metadata added to component statuses, and we don't want that metadata, if it changes, we don't want to drop it.
Well, there's a certain problem with this. The certain problem has to do with shared components. Shared components are special kind of components which are secretly just one component, but appear as multiple components to the component graph, and to the status reporting, and so on. And shared components Kind of take over.
the status reporting, but not exactly. So what actually happens is that if you have a shared component, that shared component is going to emit its own starting status, and then the graph itself will also omit the starting status.
And right now, that's okay, because it'll just be dropped. Some other things might also happen that are unfortunate. For example, the component will start.
It will emit some amount of statuses on its own, and then the component graph will try to start another shirt, another component, which is actually secretly the component that we already started, and it will emit starting again.
And it will also get dropped by the, by the graph, by the state machine. So right now, we don't really see any problems with this, but if we try to relax the state machine so that we can re-emit statuses to emit metadata.
these problems come up. Another problem that comes up that might eventually be relevant to, To remote management, because for remote management in particular, it might be useful to continue running even if a component doesn't start.
Right? We'd only start the components that we can.
and continue running. Right now, emitting permanent errors from components not starting for shared components is also broken, just because they emit a permanent error only once. And in the subsequent attempts, they just attend, they've already started. So there's a bunch of these problems.
that aren't urgent, because right now they just don't appear. They block certain improvements.
My main problem, and I kind of wanted… I was hoping to get some, to put this in front of people with better familiarity of the collector codebase. I'm not sure that there's a fix to this that doesn't involve, like, adding a new interface and moving things around a lot, because… If you look at the actual graph.
the graph just kind of emits start. Like, the graph emits a bunch of statuses when it starts components, or when they fail, it emits, like, a permanent error, whatever that's called.
**atoulme** 26:08 Yep.
**Mikołaj Świątek** 26:10 And, there isn't really any way to tell from the outside.
**atoulme** 26:15 - Yeah, I think you're touching on something that, internal shared components.
**Mikołaj Świątek** 26:20 on its own, right?
**atoulme** 26:21 Sit.
**jmacdonald** 26:22 Yeah, I put a link, because it took me a minute to catch up there.
So, shared components, for those of us who aren't on the same page, is this mechanism by which we achieve sharing of ports and so on, so logs, traces, and metrics, and profiles all go over one port. Those are a shared component if you're the OTLP receiver, just to bring us on the same page. Thank you.
**Mikołaj Świątek** 26:43 Yes.
**atoulme** 26:44 It's a… it's a big, big technical debt pit, because we have the exact same code in Contrib.
To be clear.
**jmacdonald** 26:51 It's not the exact same.
**atoulme** 26:54 Don't exist.
**jmacdonald** 26:55 Sorry, excuse me.
**atoulme** 26:55 It's been worse.
**jmacdonald** 26:56 I've struggled with it.
**atoulme** 26:56 Right.
**jmacdonald** 26:57 well, because I migrated some code out of the core into the contrib when I did OTel Arrow, and I noticed that those two interfaces are not quite the same.
**atoulme** 27:05 That's true, so it's even worse.
I think that's actually creating a lot of tension, because if you were to try to do your own component out there, and you need this functionality, you'll end up recreating this.
Okay, I think in the first place, like, first, we need to discuss, is the internal shared component needs to have a life of its own, or needs to be, kind of.
At some point dealt with. Like, this component exists because graph is not perfect.
In the first place.
**Mikołaj Świątek** 27:40 Yeah, and like, the component… the status reporting in general is, like, relatively new. I don't think there's even a lot of components which emit statuses right now, so the.
**atoulme** 27:52 Oh my gosh.
**Mikołaj Świątek** 27:53 Do you disagree? Do you do… are there some…
**atoulme** 27:56 Oh, no, you're completely right. It's… the status… Status Saga is its own… It's its own trail of tears, because it was implemented because someone wanted to have a better health check.
And the health check would have been very descriptive, because you would have exactly known which particular components were bad or good.
Because the collector health is very complex. You can have half of your collector on fire, and the rest of it can still work. And so, they were working towards having a better view into that, and I think eventually things just didn't pan out. They… They, they finished the status reporting.
And then there was no follow-up at the health check level. So, there isn't a use of those status reports that actually warrants all the All the pain that went into making them happen.
Alright.
**Mikołaj Świątek** 28:46 No, no, it does. The Health Track V2 extensions, and soon the actual Health Track V1 extension, because they're gonna be…
**atoulme** 28:55 together.
**Mikołaj Świątek** 28:55 S?
**atoulme** 28:56 They do use it, they do, they do publish it. We actually use it. You use the Health Check V2? Okay.
**Mikołaj Świątek** 29:03 Yeah, absolutely. Absolutely. It works. That's not actually… that's not actually a big problem. We even, like… Cool.
We're even gonna try to code on it a little bit, I think, once we get some other stuff sorted out.
**atoulme** 29:17 to hear about this. Thank you.
**Mikołaj Świątek** 29:19 Yeah, it also has to do with the remote management use case, right? This is.
**atoulme** 29:25 Yeah, for sure. And the special reload discussion we just had? Probably all.
**Mikołaj Świątek** 29:29 Yes, yes.
**atoulme** 29:29 incident.
**Mikołaj Świątek** 29:30 Yeah.
Absolutely.
So, like, the main thing this is currently blocking right now, just to put us on the same page, is, for example, you can't really do status reporting with stuff like Receiver Creator.
Because in Receiver Creator, Receiver Creator is a single component from the perspective of, the, on the component graph. So, you can… you can emit a single status that actually has a bunch of other sub-component statuses in your metadata.
That's not a problem, but if those are, like, right now, this works for OK and recoverable error, but if you try to use any of these other statuses this way.
You're gonna… they're just gonna be swallowed by the state machine.
And that's the… that's the core issue. But I tried to… I tried… I looked a little bit quite confused for, like, for something like a simple fix, but I don't think there's a simple fix with this that doesn't make… the graph aware of the fact that shared component wants to do its own status reporting completely.
**atoulme** 30:42 Yep.
Oh, I actually have some issues open on shared component, because I tried to make it so it would become a package.
Because… so even from a stability standpoint, we have a number of components that depend on this internal, feature.
which we are trying to move to the package so that it would be something that we could then reuse and contribute in other places, and I just hurt a lot from that, because it didn't work. I didn't manage to get it to all the way there. And I walked away from this thinking that there is a design flaw in the way we've been doing this graph thing.
Because that shared component is a crutch to… kind of get by. It doesn't make sense.
And I did not do… I'm just not smart enough to, or don't have the time to think about it more.
So I'm not surprised that you're having issues that just report on that, because we bumped into this pretty hard, and whatever fix you want to apply there, I'm me, happy to review.
But I, I cannot help you with design.
**jmacdonald** 31:45 Yeah, I kind of second that. I've seen the shared component problem, but I… but I haven't studied it enough. It sounds like there's a connection, Blake, with the work that you're doing, and I would be suggesting or looking to you, perhaps, to offer, any ideas that you come across, in this.
**Blake Rouse** 32:01 Yeah, this is actually… yeah, this is actually, something that definitely directly relates to the partial reload. I feel like partial reloading a shared component sounds like that's gonna be a problem, so we probably need to look at this.
Related to that as well. And see.
**jmacdonald** 32:21 Since there's a moment here in the meeting, at least there's some time left, I want to follow through, circle back to this topic of health check V1 and V2. I know some of the history, but not all of it, and I know that there is, an effort was started, it took… it moved a little slowly, it… it's faced opposition, it didn't completely fail, didn't completely succeed, and we were left a little bit in a place where there's some confusion, honestly, that just came out. I don't quite understand the state of the world with status reporting. Could someone here, you know, enlighten us?
**Mikołaj Świątek** 32:54 I can, I can enlighten, because at Elastic, we actually use it. It, it's like, we actually emit…
**jmacdonald** 32:59 That's what I'm looking.
**Mikołaj Świątek** 33:00 It goes through a little bit more layers of abstraction, because what we actually do is we wrap things like Filebeat in auto receivers, and we do existing status reporting for example, for Filebeat, goes through the auto framework and outside. So, we do that, and it works.
So… and it's like, we didn't even really run into any problems with the… with either the reporting framework or the extension itself. All of that works fine. It reports statuses for components fine.
it's not even particularly complicated. Like, the main thing that I think remains here is that there's some edge cases, like this, like the shared component stuff is an example, and I was, for example, quite surprised when I learned that the internal… that there is this state machine inside that, you know, polices statuses, status transitions.
The other thing was that… the main thing is basically that most of the components in either Core or Contrip just don't really have this wired.
They just don't emit statuses. But if you start emitting statuses, it works fine.
So, that's the state from my perspective. You can use the HealthTrackv2 extensions soon, the Health Trackv1 extension, this way, and that works perfectly fine.
**jmacdonald** 34:33 Is there, like, a technical debt or a maintenance item where we just haven't followed through to complete or finish the work? Like, could we remove V1 at this point?
Other than stability promises?
**Mikołaj Świątek** 34:44 I think the plan is the reverse. The plan is to make V1 do the thing V2 does, and then deprecate V2.
**jmacdonald** 34:53 Hmm.
**Mikołaj Świątek** 34:55 Because we don't want to forever have health check v2 extension, we just want to have a health check extension. I'm not actually sure, you would have to ask, I think, Evan Bradley, who I think is not here today.
**jmacdonald** 35:07 Yeah.
Okay.
Fair enough. Great, this interests me, just to see us, you know.
We should be able to evolve our interfaces without breaking users. This is an example.
Well, folks, I, Brought us through this far. Does anybody have another topic?
Sounds like no. I like to end meetings early, so there it is.
Unless anyone stops me, I'm ending it now. Thank you all.
**atoulme** 35:43 Thank you, Josh.
**Andrzej Stencel** 35:43 Thanks, everyone.
**Andy Keller** 35:45 Thank you.
**Jade Guiton** 35:45 everyone.
