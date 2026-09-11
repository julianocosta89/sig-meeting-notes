SIG: Android SIG
Date: 2026-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Cesar Munoz** 01:01 Hey, Jason.
**Jason Plumb** 01:03 Hey, good morning, good evening. I thought maybe I was in the wrong meeting for a second.
**Cesar Munoz** 01:09 Well, it's quite early.
I guess.
**Jason Plumb** 01:15 Yeah.
**Cesar Munoz** 01:18 Hello? Hello? Shaw.
Hanson?
**Hanson Ho** 01:24 Hello?
**Jason Plumb** 01:26 Now we're getting the band back together, look at this, everyone just showed up at once.
**Hanson Ho** 01:32 Beard and glasses, and Jamie showed up. With neither.
No hair, so… Same with me.
**Jason Plumb** 01:47 September 10th.
**Cesar Munoz** 01:52 Pretty light agenda.
**Jason Plumb** 01:56 Yeah, it seems like it.
Give it another minute, in case people think of things they want to talk about.
Okay, let's jump right into the first agenda item, Ben and Vishwan.
**Vishwan aranha** 02:44 I was just wondering, like, if, what do we need to do to get, like, a pro or access request, so…
**Jason Plumb** 02:54 This is a good.
**Cesar Munoz** 02:55 Question.
**Jason Plumb** 02:55 Go ahead, Cesar.
**Cesar Munoz** 02:59 You mean to be… to become an approver?
**Vishwan aranha** 03:02 Yes, to become an approver.
**Cesar Munoz** 03:05 Well… I think you guys spoiled the surprise now.
That's all I can say.
Actually, this week, just this week, we were talking about that. You… Guys have… have been… Great contributors.
For a while now, so we were actually discussing this But now… but now it's not a surprise anymore, so I guess.
That's all I can say. Yeah, basically, what you've done… In the past.
Couple of weeks.
More, it's, it's what's needed, and, and… at least I can say for myself that I'm very grateful for For your contributions, so I think it's fair.
Yeah.
**Jason Plumb** 03:55 Yeah, yeah, absolutely. I'll just second what Cesar said. Yeah, what you all have been doing to help further this project has been super appreciated and very helpful. And yeah, we did want to extend, an opportunity to grow your influence in this repo by becoming an approver. I think, you both have been very helpful in reviewing PRs, which is, like, one of the main Responsibilities for approvers.
As far as, like, the process goes, I think there is something… written in the community repo, and I can link to that, but usually it's, kind of maintainer-driven. It's always acceptable to bring up this idea. If someone feels like they have been contributing or wants to grow their influence, that's always an option. Please, everyone's welcome to do that.
And… Then we can take it under consideration. I think… I think the process is pretty light.
There's some requirements that I think described in community.
But as far as the actual logistics of how that happens now, it's just in our hands, and we have to do it. Like, it's a maintainer problem now.
Let's see.
**Cesar Munoz** 05:09 To look for that link.
**Jason Plumb** 05:17 Let's see, I think there are, like, yeah, I think there's levels somewhere that are described.
**Cesar Munoz** 05:30 There is… Jamie just shared it.
**Jason Plumb** 05:33 Oh, you got it in chat? Okay.
Thank you.
**Cesar Munoz** 05:37 Thank you.
**Jason Plumb** 05:39 I was close, though.
Yeah, so I'll just link to this in our doc, just to have that as a reference.
And then I… I think we should be able to do that in the next day or so. And then, I'm also, just for transparency, I'm also gonna ask Manuel, if we can move him to Emeritus. That's one of the other statuses. I think it's also… Yeah, so… he's gotten busy, I'm assuming he's off doing other things. I think we're gonna probably move him to Emeritus, because he hasn't been really present or contributing, which is… which is fine, right? That's the way these projects go sometimes, and if he… if he frees up and wants to help out again, that's… that's great, he can come back. But yeah, so that's in maintainer hands. I think we should be able to do that this week.
Which means today or tomorrow, for me.
But yeah, thanks again, I mean, your contributions have been super great, and we appreciate it.
**Vishwan aranha** 06:37 Thank you, Chris.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 06:38 Curious.
**Jason Plumb** 06:45 Okay, moving on to next steps on these PRs, let's talk about this one.
**Vishwan aranha** 06:50 All right, I… this is a quick follow-up from some of the stuff that we already discussed last week. Like, I'm proposing, like, for 2048, just the gist of it, like, I'm proposing a storage hook for, like, existing session manager.
And before coding or doing any implementation, I'd like to agree on, like, whether Restart, resumes the saved session, or, like, creates a linked one.
And, how we handle, like, a slow or, like, failed storage.
**Jason Plumb** 07:20 Okay, so it's kind of 3 open questions on 2048. Yeah.
Is what I think I heard.
So the first one is, storage hook.
**Vishwan aranha** 07:32 Yeah.
**Jason Plumb** 07:34 And then session… new or linked?
**Vishwan aranha** 07:38 Yeah.
**Jason Plumb** 07:39 And then…
**Vishwan aranha** 07:41 Like, how do we handle a slower like, failed storage.
**Jason Plumb** 07:45 Okay.
And are these questions, like, outlined in this issue?
**Vishwan aranha** 07:52 Yes, I think I've been talking back and forth with Cesar and Jamie, so if you guys have anything to add, feel free. You can go through that.
**Jason Plumb** 08:06 Cool, I'll open it up to them. I have not been very present on this. I have extenuating circumstances to deal with on my end.
**Jamie Lynch** 08:15 Well, I think, from my perspective, it was just… trying to figure out what the API looks like, from the perspective of someone who's actually using the library, and how they would configure this. And I think the question in my mind is whether we want a separate way of setting session storage and generating a session ID, or whether we just have some… Some way of setting… something that retrieves a session ID, and then that object is responsible for Like, over-persistence and… Bits like that.
**Cesar Munoz** 09:01 Yep.
So, from my side, I… there's… there's… I guess two… two things that I… Kind of already mentioned in the issue, but just to… To give a, A summary?
First of all, actually, well, this is… I didn't mention this, but I was actually surprised when I learn about this issue, so thank you for bringing it up.
that… I really thought that we were storing the session ID on disk.
And it turns out that we aren't. Like, we have… We have a mechanism, there's an API, called… well, session storage. I have it here.
And I thought that that was… Being used to store stuff, this stuff in disk.
But it turns out that the only implementation that we have for it is in memory.
And… and that's the one that we use. So… from what I understand from this issue, and please correct me if I'm wrong, Vishwan.
So I guess we're… I'm just trying to summarize it in my own words. It's like we're trying to find out a way, essentially.
To store sessions in this.
Such an agreed.
And… so… If that's the case, I already provided my… my proposal. Essentially, it's just adding A way for users to provide that.
interface.
Of their own.
As part of the DSL config.
Now, I think there's another… Ongoing, conversation there, which is where should this… ability to configure the session storage be added into the DSL.
And I think that's where we haven't still gotten to a consensus, but essentially, yeah.
Probably that's why we need to talk a bit further.
Just for the record, just to give my context on What session storage is for the agent.
To me, the session itself, it's something that it's… not thoroughly defined yet in OpenTelemetry.
Aside from the fact that it has an ID.
And… I'm trying to focus on keeping the abstractions of general abstractions obsession on that only, which is… there is an ID.
To me, Whether we store it, or whether we decide there is a timeout.
Or, things like that are… are all our own… Opinions on how to handle a session.
And so, this part then falls into that.
So… I'm saying this because… I think one of the… if I understood correctly, one of the discussions in the thread is that maybe this should be part of the, overall session provider API, or something like that?
And I wouldn't put it there, because it's not… I mean, again, it's what we decide to do with sessions, which is to store them, but… I imagine a case where maybe there's an app that wants to treat a session as a… As something that is alive, as… as long as the app's process is running, that's it. So that could be a way to treat a session.
Or maybe even less than that time.
And in those cases, I don't see that they will need to store things, ever. So… so I don't… if I don't fit it as a very… Generic, general purpose.
use case, then it's something I wouldn't put in the general purpose.
API. So…
**Vishwan aranha** 13:13 I'm happy to keep the persistent optional and leave the, like, provider API, like, unchanged for, and Jamie, would configuring storage on, like, existing session manager work for what you had in mind? I saw your recent comments.
**Jamie Lynch** 13:29 So… I think the design that I would have… Initially chosen is, like, just a really simple interface, but… is just, like, a one function interface that returns the current session ID.
And… Then the implementation details are… up to whatever implements that, basically, because then we could implement our own that, by default, persists, like, the session ID, between processes.
We could even provide… implementations that are just, in memory, so they die when a process dies, and… Yeah, I think that's where my… head is at. I think… Also, one other requirement, there might be a slight tangent, I think it'd be useful to have some sort of notification of when a session has changed.
**Jason Plumb** 14:38 We have that.
**Hanson Ho** 14:41 We have an event.
**Jason Plumb** 14:44 No, you can now… you can observe it.
Yeah, if you can get the session manager, you can add an observer.
**Hanson Ho** 14:50 Perfect.
**Jason Plumb** 14:50 And the observer is notified I don't know where that interface is…
**Jamie Lynch** 14:57 Okay. We should have done.
**Jason Plumb** 14:58 Well, that was the intent of this, though, is to be able to be notified.
**Hanson Ho** 15:01 Perfect.
**Jason Plumb** 15:01 Or to be able to do specific handling when a session changes or ends.
**Jamie Lynch** 15:06 Is it possible to… configure that fiber DSL, or if not, I imagine it shouldn't be too tricky to add that on.
**Jason Plumb** 15:14 I hope so, is the answer. Yeah, it should be.
**Hanson Ho** 15:18 So… so here's an interesting question. I think there's an unstated implication in the current design that process termination kills a session.
Because the ID that we generate, We don't persist it between processes.
So… If we were to save it and then resurrect it, we would be changing that.
So far, in the agent, we've treated session like what it is treated in, in OTEL, which is, it's a property of a thing that exists.
So, anything we persists is… the hotel things that exist, so logs and spans and perhaps metrics.
Persisting in ID across will break that, which is fine, if we want to basically say sessions now extend across processes, but it also means that a session can persist across two app versions, two resources, basically, SDK versions, anything.
**Jason Plumb** 16:26 What's the use case here to persisted? It's not… is it for crash handling? Because I thought it was persisted already as part of the crash handling. Is it… what's the other use case that you're thinking of?
**Jamie Lynch** 16:36 I think activity timeouts are also one. Like, you can have… For example, you might have a user who goes into their phone, opens an app.
Flicks to another app, for a couple of seconds, and then goes back to the original app.
Cool.
**Jason Plumb** 16:57 Is that the intent… is that one of the intended use cases here?
**Vishwan aranha** 17:00 So, the use case I had in mind is, like, connecting activity before and after the normal process recreation, so not just, like, crash handling. That, that doesn't have to mean that reusing the same session ID. We could, like, start a new session and the link to the previous one, so we preserve the connection without, like, treating the two app versions as, like, one session.
Like, would that address the concern?
**Hanson Ho** 17:23 If we're pulling from memory, it reduces the complexity by a ton, so all you… all you need to basically get current session ID or whatever, and then… and then you can do it. Persisting across processes, that's when all the complication comes in. And also, it kind of… breaks some assumptions that we have about when a session terminates. Because in the scenario Jamie described, you… close an… you background an app, go to another app. If at that point, the process terminates, what happens right now is when you come back, it's a cold launch, and we have a new session.
it doesn't resume the existing session, even if it's within the timeout period. If the process is still alive, then you can get from memory the session ID, and you don't need to… you don't need to, you know, retrieve it from disk. So if what we're lacking is… is just, hey, what's the current session? Like, you know, asking the agent that, then I think adding that, will… will support it, and without having us to open the Pandora's box of Cross-process sessions, which… useful, but… a lot of… a lot of edge cases. Like… like… Providence and things like that.
**Jason Plumb** 18:37 Yeah, so…
**Cesar Munoz** 18:38 I…
**Jason Plumb** 18:39 Ed.
**Cesar Munoz** 18:40 Well, I just wanted to add one more example. I think it might be useful in some cases, So, for example, I've used very old phones that, sometimes I'm in an app, and then they ask me for, I don't know, filling in some data.
And then I have to look for that data in another app.
And so I… I don't close the app, but I just minimize it, if you will, and then go to the other app, but the phone is so old that by the time I go back to the first app.
The process was… killed. And to me.
I would say that it's the same session, technically, I just quickly just went to look for something else.
to finish what I was doing.
So, I think it would make sense in that case.
And I've also… heard about… A potential use case for this.
That even includes crashes.
So, I know that there are some people who treat trashes as, As a… as a something, which is part of something bigger, which might be called Something like frustration.
Signals for a user.
And we may say that If a user reopens an app, Quickly, you know.
after, I don't know, after it crashes.
Maybe it's because they haven't finished what they meant to do with the app open, and they have to finish it, and if that happens again.
I guess if we keep this session in disk, we may see that in a single session.
in the span of, I don't know, 15 minutes.
There were 3 crashes, that's a major, like, frustration signal that we could gather from that experience.
So maybe in that case.
you know, if we were to kill that session on every new launch, it would think that, you know, it would look like everything was, you know, great. There was a crash per session, but, you know.
Isolating in that session, so… I think there are some use cases. I know it's tricky to make it work. The, proposal that I think Which one?
is adding here, or at least the one that I've been following, is mostly about to provide a setter for users to… provide their own storage mechanism. That's what I understood. I don't know if we're also trying to provide a default disk storage implementation.
or the like, but… but that's kind of like I understood, at least to provide that configuration setting.
**Hanson Ho** 21:29 So let me be clear. I think persisting is actually totally fine to do. A very good use case would be native crash handling, and, you know, unexpected process termination. You know what the session was before, so you can actually log telemetry for that session. I think that's… that's… that's useful.
And the possibility of, in the future, you know, grouping all that stuff, that's great, too. I think the part that gets trickier is continuing a session.
across processes. So, if we have an API to get an ID, the current session, if we persist it so that we can get what the last session was, or something like that, which will solve a lot of the, telemetry happened in the previous process, use cases. As long as we don't… continue the session, I think it… You get 90% of the, of the, of the, of the utility without crossing that knowing threshold of things getting complicated.
**Jason Plumb** 22:35 I wanted to speak to this here. So, like, normal process recreation loses the current session. That's always been the original design, like, that's very much intentional. When you close the app and you start it up again, there's supposed to be a new session. So I think that talking through these use cases is really important, and for us to understand These non-standard cases where an app Might be restarted, or these other reasons for having a session continue between launches.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 23:05 So, I just want to add a note. So, I think this goes back to, you know, session not being defined properly within OTEL.
**Jason Plumb** 23:15 It does, yes.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 23:16 Yeah, so, and I, I think, like, we, we are, like, very tightly coupling it to the app's lifecycle, and I mean, that definitely makes a lot of things easier for us.
But I think, like, where we are coming from is, we try to look at session as a user trying to achieve a specific objective within an application. So there might be, You know, he's going to a banking application, maybe trying to download some statements, he's looking at, some data within the application. So, in between, like, so he might switch to other apps, maybe, you know, or, or filing, you know, filling up some application form. Like, he might have to go to the file storage apps and, like, upload certain apps, or edit something. So.
Over a course of time, like, he's achieving a specific use case within the app, and, like, we want to link all of that together and, like, present that as a session.
On the observability side, on the dashboard side. So that's where we, the use case for, you know, linking, even, even through different, different process life cycles, or, like, across, process that, we want to do. And… Yeah.
**Jason Plumb** 24:36 Let me just jump in. So, I think in the normal use case where you're just switching between apps, I think the typical expectation is that the app doesn't get restarted most of the time, that you can switch to your password manager, get your password, come back to your banking app and log in, and it still is gonna be the same session.
If, in the event, the platform does cause the app to be terminated and then, like, restarted, and you do get another session, it should be possible to still stitch those sessions together, right? So if you have… five sessions, they certainly wouldn't overlap in time, meaning the start of each session is progressive on a timeline, and you have the phone identity through the resource information. So you should be able to stitch… if you so choose to, you could, in your backend, stitch those together, I believe.
Or present them, you know, present them as one experience in a UI.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 25:29 Correct.
**Cesar Munoz** 25:30 I agree, but that sounds hacky.
I mean, like, you know, it's… I know that there are use cases for storing this and this.
And to continue the session after the process gets restarted.
I, I… We don't have to do it by default, but I think we can enable users who wants to… who wants that? But, I mean, this… this…
**Jason Plumb** 25:55 I agree.
**Cesar Munoz** 25:55 Storage, Saturn.
**Jason Plumb** 25:56 I like the idea of maybe putting a time on it, like, oh, you relaunched the app within 30 seconds, or 20 seconds, or some, like, kind of small number. You're probably doing the same thing. You're probably still just continuing what you were doing before.
So, facilitating that through storage, I think, is a super helpful use case that we don't yet support.
**Vishwan aranha** 26:14 And also, like, would that depend on, like, having a stable device ID? Like, how would we connect those on… those sessions, like, for an app that doesn't provide one?
**Jason Plumb** 26:24 We… we should have identity information in the resource that allows you to uniquely identify it.
**Hanson Ho** 26:32 we should be generating some ID, so that we can link stuff across, because otherwise devices don't report identity, and we can't actually use… even if it does, we can't use it, because that's PII. So we should generate, some key that is…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 26:47 We have a session ID, yeah. We generate a session ID on init. It's a random UUID.
I think it's called the app install ID or something.
**Cesar Munoz** 27:00 I do, yeah.
**Vishwan aranha** 27:01 Damn.
**Hanson Ho** 27:02 And that is effectively the key that binds everything together. If the user clears, cache, it basically resets the device, and that's… that's not… that's not a vector we can protect from.
So just to go back to the session point a bit, I think… I mean, talking a lot about it is because Embrace has actually gone through this whole shebang, the last few months, of redefining what session means. And… there are effectively session in terms of what the SDK observes, because process… has a lot of performance implications.
But the user experience is… is almost an overlapping, concern. So you want to track users across app processes. That can be considered a session. An app process and being alive, and collecting memory, leaking memory, going up and down. That also can be considered a session.
There is no right way, which is why I think OpenTelemetry's definition being whatever the hell the app or agent wants.
**Jason Plumb** 28:11 We needed to…
**Hanson Ho** 28:11 Correct one.
**Jason Plumb** 28:12 and…
**Hanson Ho** 28:12 But yeah, the agent needs a definition, and the agent definition currently is process-based. So to change… to provide a setter for users to basically change that, I think that's… that's… Probably okay, might be… there might be some potholes there, but the default of linking is very… would be very controversial, because, it would be changed… Yeah, between users. Between… between, users of the agent.
Because, anybody who's using this distribution, if they get… so if you ship this, and it's by default linking, you know, based on the timeout.
you're gonna have a lot of behavior differences, whoever… who expects the current behavior. This is effectively an API. We have implicitly said process termination creates a new session.
So, if we… if we want to go away from that as a default, it… it would require a lot of changes.
**Jason Plumb** 29:13 I fully expect, when we form the session SIG and Bike Shed for a few months and come up with a concrete definition of this stuff, that we're gonna have… it's gonna be a breaking change, I imagine. Like, it's gonna… it's gonna change behaviors.
**Cesar Munoz** 29:26 Yeah, I mean, and right now.
I don't think we should change the default behavior, because it would be a breaking change, and the agent, it's already stable, so… But, aside from that, I do think it's… I don't think… I don't see an issue with providing A way for users to have this…
**Jason Plumb** 29:47 I agree.
**Cesar Munoz** 29:48 way they want to. If they want to store things in disk, I think it's fine. And the APIs are already there. I mean, session storage is a very simple interface. You know, it just… allows you to save and retrieve a session, that's… that's all it does.
So, anybody can do their implementation, it should be fine.
**Jason Plumb** 30:07 But we don't have a way to provide one yet through the DSL, that's what's lacking, right? So we called that out, I think.
**Vishwan aranha** 30:13 I'm glad…
**Cesar Munoz** 30:14 That's what Vishwan is suggesting. Cool. Yeah, sorry, Vishwan.
**Vishwan aranha** 30:18 optional… can the optional storage look like move ahead independently with no change to the default, for sure? Like, while the broader session definition is, like, worked out with the other team and stuff?
**Jason Plumb** 30:29 Yeah, I think that's totally fine.
**Vishwan aranha** 30:31 Okay, so I'll basically keep 2048, like, focused on making the existing session storage configurable, like, with the, probably the in-memory, like, default unchanged. Is the session block the right place for that setter, or should I look into something else?
**Jason Plumb** 30:49 Let's look. I don't remember what that looks like.
This is pretty light.
Yeah, this seems like a natural place for it, is my instinct.
**Cesar Munoz** 31:09 Yeah, we can set up servers right now.
Yeah, I think this will be a nice place.
**Vishwan aranha** 31:14 Okay, I can start with that thing.
**Hanson Ho** 31:16 Some, like, initial session ID provider or something like that, the session ID that gets used, you know, up on init.
Is that something that…
**Cesar Munoz** 31:25 No.
**Jason Plumb** 31:26 Session story.
**Cesar Munoz** 31:27 So…
**Hanson Ho** 31:28 story.
**Cesar Munoz** 31:29 Session storage.
**Vishwan aranha** 31:30 All right.
**Cesar Munoz** 31:30 It's the… it's what we currently use to store the session in memory, but it's an interface, so… Can provide your own, and then you save it into disk.
**Hanson Ho** 31:43 So to hydrate it, you need something else, right?
**Jason Plumb** 31:48 On next.
**Cesar Munoz** 31:49 What do you mean, like…
**Jason Plumb** 31:50 Yeah, yeah, yes.
**Cesar Munoz** 31:52 Oh yeah, your implementation.
**Jason Plumb** 31:54 It's true, yeah, you would need to be able to get your session provider in there that's disk-aware.
Yes. Is it provider the right term? Am I… is it manager or provider?
Generator?
**Hanson Ho** 32:06 Provider would be… would be… because it might not be doing a new thing.
**Cesar Munoz** 32:14 So, in the manager… the manager is our… is our provider.
Social.
**Jason Plumb** 32:18 Where is… interface. What is that interface?
**Cesar Munoz** 32:23 session provider.
**Jason Plumb** 32:24 Yes.
**Cesar Munoz** 32:25 session module.
**Hanson Ho** 32:27 session provider… Oh, okay.
**Jason Plumb** 32:30 Agent, okay, because this is all agent, okay.
Got it, yeah, there's the top-level API. Yeah.
This is where such a provider is, yeah.
Cool.
So you would also need a way to provide your own session provider that is disk-aware, and can provide the one initially attained from disk, and then delegate to probably the existing one afterward.
**Cesar Munoz** 32:52 I don't think that would be needed. I mean, to me, session provider, if you set your own session provider, you essentially override everything that we do in the engine.
And… I guess that could be a way for you to achieve it.
But… as a tangent… tangential note, we still don't have in the DSL a way to provide a session provider.
I think Jamie was working on that.
But if we want to… if users want to keep the same session manager's, logic.
And on top of that, they want to… control where the session ID is stored, then I think the simplest thing to do is to expose session storage.
In the DSL.
That's what I was suggesting. Because session storage is currently used by our session manager.
when it needs to store stuff, which currently goes into an in-memory session storage implementation, so it technically just stores it in a memory. So, there it is, in line 21.
**Jason Plumb** 34:07 I think… Go ahead, Jamie.
**Jamie Lynch** 34:10 No, I was just gonna say that if we have session ID, session provider as kind of an escape hatch, if folks want to provide an alternative, like, session management, then that feels okay by me.
**Jason Plumb** 34:25 It's… it's not clear to me on relaunch, though, how you, rehydrate that storage session and start providing from that.
Because storage is only the right side of it, it's not the read side of it.
**Hanson Ho** 34:38 Yeah, that's what I…
**Cesar Munoz** 34:39 Yeah, it's both.
**Jason Plumb** 34:41 You think so?
**Cesar Munoz** 34:42 Yeah, take a look at session storage.
**Jason Plumb** 34:46 I wish I could, I don't know how to use computers.
**Cesar Munoz** 34:50 Sorry.
I sent the link there in the chat.
**Jason Plumb** 34:54 So, it's with the GET, you think?
**Cesar Munoz** 34:57 Yeah.
**Jason Plumb** 35:00 who calls this Oh my god.
**Hanson Ho** 35:07 Is this a get current, basically? Is that what that is?
**Jason Plumb** 35:12 I mean, it gets the session, the session with an ID, is that correct?
I hate that I have to jump through these different packages.
**Hanson Ho** 35:19 I guess the implementation could be aware, that there is no session, like, it's an initial launch, and then basically pull it from disk. So yeah, this interface might do it.
You would have to set the timestamp as well, I suppose, but…
**Jason Plumb** 35:38 Yeah, there's… there's a few moving pieces. I think it's worth prototyping, or at least trying to get working.
But first step, you can build the storage, right?
**Vishwan aranha** 35:50 Yeah, and can we also check the manager's, like, startup path to see whether it reads the save session, like, before creating a new one?
**Jason Plumb** 35:59 I don't think it does today.
**Hanson Ho** 36:02 Wait, I thought we're building APIs… So that you could hook in your own stuff.
**Jason Plumb** 36:07 Oh my god, how insane.
**Hanson Ho** 36:08 Isn't the manager… internal.
**Jason Plumb** 36:12 It is, it's an implementation.
**Hanson Ho** 36:14 Yeah, so the problem, I think, with interlining interfaces is you have to do everything. Like, we either say, you do everything, or you use our thing. And doing everything implies a lot.
**Vishwan aranha** 36:31 Yeah. Yeah, and basically the goal is to, like, let users plug in their own storage, not, like, change the default startup behavior. I was only, like, checking that existing manager uses the supplied storage, or on, like, first access, or not.
**Jason Plumb** 36:44 Yeah, it's an init here, right?
**Hanson Ho** 36:47 it's… session storage is, default parameter, so theoretically, if you can pass in a new implementation, when Session Manager is, is initialized, if you could do that through the DSL, then you should be able to, to do this. And in fact, then, It seems like you could do everything, all the persistent stuff, In its own implementation, and that might be the only thing you need, because that does both the right path and the read path.
**Cesar Munoz** 37:18 Yeah, that's how I see.
**Jason Plumb** 37:20 Yeah, so the session manager's created, in the… in the bowels of the agent when you initialize it. So, you know, there'd be some changes in here to use the overrides from the DSL.
**Cesar Munoz** 37:34 Yeah.
**Jason Plumb** 37:36 Make sense?
**Vishwan aranha** 37:37 Yes, makes sense. So, I'll basically start with that wiring, like, keep the default unchanged, and, like, add tests showing the custom storage is, like, used for both reads and writes.
So, I'll cover all grounds possible, and definitely I'm planning to divide it into smaller chunks as we decide on things, so it's easier to review and add feedback, and we can also discuss through the PRs as we go.
**Hanson Ho** 37:59 So the provider… oh, sorry, go ahead, nevermind.
**Jason Plumb** 38:02 And maybe we also just get rid of this while we're in here, messing with this?
Like, I don't know that we need a create method, right? It's very non… non-Kotlin.
We'd just create one of these?
**Hanson Ho** 38:16 Yeah, why would… Where would be…
**Cesar Munoz** 38:19 It's strange, but is it public, though?
**Jason Plumb** 38:23 Probably…
**Cesar Munoz** 38:23 It is probably…
**Jason Plumb** 38:23 There's probably some Java usages somewhere, like, this might have history.
I'm sure this happens.
**Cesar Munoz** 38:28 sister.
**Hanson Ho** 38:31 Maybe if you use core, you have to call it yourself, or some, some stuff, some, some, some reason like that.
**Cesar Munoz** 38:38 Well, this is all in the agents, so…
**Jason Plumb** 38:40 Yeah.
**Hanson Ho** 38:41 Okay, okay, alright.
**Jason Plumb** 38:43 Okay, I think this was a really good discussion. Hopefully, we answered some of those questions. Are there any… open uncertainty. I mean, there's gonna be some discoveries and surprises maybe along the way, Vishwan, but I think, hopefully, we've gotten you unblocked on this stuff.
**Vishwan aranha** 38:59 Yes, and if… like, as I go through it, I'll basically start with… I check the callers and API compatibility first, like, I can keep the cleanup separate, so the storage, change, like, stays easy to review, so… Cool, that's great. Basically, the storage wiring is clear now. One remaining question I have, like, should custom storage handle its own failures, or, like, should the manager provide a fallback?
I'm happy to work through that in the free PR, too, if you guys are not sure on that.
**Hanson Ho** 39:27 I think… I think if the implementation is handling its own storage and retrieval, only it can handle failures.
I don't think… I don't think the interface also has, like, a… I think save doesn't return a Boolean, right? I think… I think there's no way from the interface to telegraph that savings.
But that… that could be changed, I suppose. So I think, I think the API can probably provide, some, some status about whether the save actually worked.
And then you can handle it on your own.
**Vishwan aranha** 40:01 Sounds good to me. So I can start with that. And I will, document everything in the… take a task itself, so you guys can also have a look again. If, if, like, after this call, if you find that there's some old code that could be an issue, we can, like, raise that as a question.
**Jason Plumb** 40:20 Cool.
And I've been taking notes sort of up here, but I think we've also covered these too, is that right?
**Vishwan aranha** 40:29 Yeah, so basically it's like, It was, like, a general discussion, so to cover it with everyone, yeah.
**Jason Plumb** 40:35 Jumped around quite a bit, but I think we got there.
Okay.
Are we ready to move on to Hanson's topic?
**Hanson Ho** 40:44 Yeah! Okay. Are we? I don't know, are we?
**Jason Plumb** 40:47 I'm ready.
**Hanson Ho** 40:48 Okay.
So the Kotlin API is… is getting closer and closer to, stability. I think we crossed a big hurdle with, the propagator stuff, this week, saying that we don't have to provide a default global propagator that propagates, even if it's turned off. Correct me if I'm wrong, Jamie, that's what I interpreted that as.
Thank you.
**Jason Plumb** 41:13 Correct.
**Hanson Ho** 41:14 Okay, yes. It took a long time, but yes.
I, I want to say that's one of the few blocking things to make sure contacts is stabilized, which is one of the blocking things for making, span and, log or events stabilize. It will be a while, but soon.
**Jamie Lynch** 41:43 -
**Hanson Ho** 41:43 when… when will we, when… what level of stabilization, rather, what APIs do we need to have stabilized before we start adopting it?
specifically, do we have to have the metrics API stabilized before, you know, we start serving?
the Kotlin API? Or is there a way of getting it, like, an experimental version in, or… what is the path? I want to understand the path of getting Kotlin API into… into this.
Not SDK, just API.
**Jason Plumb** 42:18 Sure, right, and the API would still be backed by the underlying Java SDK. Like, we would still be using that implementation in the short term.
**Hanson Ho** 42:25 Yep, so, whatever, whatever, thread local defect… default context propagation that, that Java has, we will continue to keep, etc, etc.
**Jason Plumb** 42:36 Yep.
**Hanson Ho** 42:41 What do you think, Jamie?
T-U-L.
**Jamie Lynch** 42:46 Yeah, I think definitely we'd… Need to start off with… basically just using the Kotlin API that decorates for hostilemmetry Java SDK.
And… Yeah, I guess I don't see too much of an obstacle to maybe just starting off Like, Doing that in, like, one particular module or one particular class.
Because it does kind of allow you to mix and match, So we could dip our toe in the water with something internal, if folks feel okay about that.
Or maybe, like, even the Justin test code.
**Jason Plumb** 43:38 So, the… I think the biggest challenge right now is that we have the OpenTelemetry Realm class, interface.
And it exposes the OpenTelemetry interface, which is from Java.
Great.
So if we're looking at the high… the highest level stuff that users deal with, they deal with the OpenTelemetry realm, which directly, on its API, which is stable.
I believe.
Yeah.
So this is a stable API, and we expose another stable eye in the form of the upstream OpenTelemetry API. So for us to change that to a Kotlin implementation would be a breaking change.
That's kind of the first… thing to call out. Like, details aside, right? Like, that's the… that's the main thing that stands out to me.
**Jamie Lynch** 44:33 I think… I think there's a difference there between… shifting… Open Solometry Android's API to use Kotlin types versus using OpenTelemetry Gotland to provide that, OpenTelemetry Java API.
So, currently, it would be capable of providing an instance, with that particular type.
Everyone does.
To supply that.
**Jason Plumb** 45:04 Meaning, Kotlin could supply this type, this Java type.
from the Java implementation… the Java implementation of the API.
Okay, the Kotlin Java API implementation. God, that's really… I don't know how to describe it. You know what I'm saying, but it's… There's too many descriptors in there.
**Cesar Munoz** 45:26 In case I don't understand that.
**Jason Plumb** 45:28 Go ahead.
**Cesar Munoz** 45:29 So that the API So we're talking about only the API from Kotlin?
which would be backed by the Java's functionality.
and then… there is a way for us to get, if understood correctly, an OpenTelemetry Java instance out of the Kotlin API.
**Jamie Lynch** 45:59 Yeah, that's correct. It basically just unmaps the decorator.
**Cesar Munoz** 46:05 which will still be backed by all the Java functionality.
**Hanson Ho** 46:13 the… the babiest of the baby steps is what Jamie said. We could have… we could have one internal module import the Kotlin API, and use that we don't even have to expose that externally, until we're ready. And when we're ready, we could even expose it as, like, experimental or something like that.
Switching the main OpenTelemetry to the Kotlin version will require a major version bump.
And I'm… that is… that is on the roadmap, but that is so far along the line that I'm not even, like, thinking about it. I'm just thinking about baby… just a little tiny spoonful of baby Kotlin API, for internal consumption, and then validating, da-da-da, whatever, you know.
building up to, something, where we expose the Kotlin API as an alternative, experimental, whatever, So that will obviously need a little bit more, evaluation, but, like, the baby step, if we have, like, a, internal unstable, module that we want to kind of drip feed this to. I might be a good candidate.
**Jason Plumb** 47:37 So I was…
**Cesar Munoz** 47:37 I think it sounds good. It… Well, I just wanted… wanted to say, I think it sounds good, I guess, but I guess my… idea of adopting the Kotlin API is for users to use the Kotlin API, so it's kind of like… what are we testing if we are still gonna provide the Java API? It's just that it was built with the Kotlin code.
I don't know, at the end of the day, we're still… You know? You know what I mean? We're still providing the Java API, so… I think it's fine, you know, if we want to test the ability for the Kotlin API to create Java's tough.
But aside from that, I will… ex… probably… I'm just thinking out loud, maybe we don't have to do this, but maybe… Maybe we'll have, like, a 2.0 branch.
that… Just swaps the, opens the inventory API from Java for the one from Kotlin, and then… We run the tests there and see… If something breaks, And it's not too important, maybe we can flag it as a limitation or whatever?
But, but maybe that… Maybe we can… do some snapshots of this 2.0 incubating All of the suffixes that we come up with.
and then people can start trying it out. Maybe there could be a way to… To see… to test its… its stability?
We can also add the… what you guys mentioned, it's just that, to me, we'll… in the end, won't actually test the Kotlin API, or at least won't provide users for a way to do so.
Which I guess is the end goal.
**Hanson Ho** 49:32 Yeah, I think, what I wanted to discuss was how harsh and dramatic the shift is.
So on the one end is, is, you know, cutting a 2.0, exposing a brand new API, and say, you can do the migration.
On the other end is we slowly adopt it internally, so that we, as a project, build confidence in it, and then expose it as experimental. And then people could do migrations, depending on the experimental API, so that when we actually swap it, so they can do their own testing to see their workflow using this API, and see if anything changes. And then when we actually do the official swap.
It's not like you have to go. I mean, at that point, you have to go, but you could have tested it before. Because to say that you can't upgrade until you change all your API, would be pretty harsh, and having, like, a medium step of, you can try it out before we swap over might be nice. And I'm wondering if we need to, What steps would we need in between that?
**Cesar Munoz** 50:34 I mean, that's fine, maybe I'm… I don't understand it.
I'm just saying… you say that you want people to try it out?
But then, what I… what I… what comes to my mind is that, in the end, they will be trying out Watt, still Java.
I mean, based on what I… from what I understood, we're still going to provide them with a Java API.
That was built using the Kotlin code.
So, in the end, we are the ones who will be using the Kotlin API internally, and for users, they… And the backend for it will still be Java still, so… If there is a way, maybe… maybe I'm not visualizing it properly, but if there is a way for users to try the Kotlin API, even though we don't provide the Kotlin API, Then… okay, sounds good.
It's just that I don't see it.
**Jason Plumb** 51:31 Yeah, maybe we could do it with an extension or something, right?
But anyway, I brought up this PR that Jamie opened a while ago, just as, like, a kick the tires on this thing, what does it look like? And this might be a little outdated now, but it was an example of, like, what if we used the OpenTelemetry Kotlin, I guess just these two packages, but we could do something similar for the API, and you look at how it's implemented, right? Instead of saying.
Opentelemetry LogsBridge, Log Builder build, and getting the Log Builder, or logger.
instead of going down this API path, there's a different API path, which is, give me the OTel Kotlin API, and then that's the way to get the logger.
Right? You don't have to go through the logs bridge. So, these are, like, this is where the rubber hits the road. This is, like, the actual API changes.
I think there's totally room to do this internally, like, for our instrumentations and stuff.
the question for me, I mean, I definitely understand where Cesar's coming from, is like, how does that actually help us? I think the answer… at least part of the answer in my brain is, it helps us to vet the Kotlin APIs earlier.
In code that isn't necessarily user-facing API stable. So, like, instrumentation's being one of these candidates.
And also, it lessens our burden for 2.0 when we hope to switch to… or some future major version bump.
When we want to switch everything to be, like, pure Kotlin API.
**Hanson Ho** 53:09 And socialization, too. Like, I think to say that, hey, we've been exposing this API in some way or fashion for months before we do the the hard cut over, I think, I think… like, I think this, this PR probably… well, I mean, other than dependency and how things are pulled in, this file change, or something like that, would be what I would imagine, like, the baby step would be, the two Kotlin, 2. Kotlin API. If that's kept internal, then, then customer… or, you know, users of the agent won't have access to it, but, you know, internally.
we have access to it. And this is… this will be effectively how we, change our internal APIs, or usage of the Java APIs into Kalin, so that when we internally, all the instrumentation is free of the Java API, and then when we switch over, then there is effectively no API change within our thing.
So I guess the secondary benefit is that it helps with our migration. We will be able to, like, you know, transparently.
You know, move implementations, if we just swap that.
**Cesar Munoz** 54:17 I think I got it. I think I better understand it now. Thank you. I don't know if we will be able to create a Kotlin extension that is internal, and that we can also use Across, submodules.
I wouldn't see an issue with just creating a module that… Might be optional, in that whoever wants to add it gets this, kotling Extension.
**Jason Plumb** 54:48 Is that what this is?
**Cesar Munoz** 54:49 projects.
**Jason Plumb** 54:49 Is that what this was?
**Cesar Munoz** 54:50 a… Okay.
**Jamie Lynch** 54:53 So…
**Cesar Munoz** 54:54 markets.
**Jamie Lynch** 54:54 Yeah, the extensions, I think… BO is an extension in that module, so… Yeah, folks could add a dependency on that and convert the existing OpenTelemetry Android like, Java types to Kotlin today, if they so wished.
**Cesar Munoz** 55:15 I, I think this could be… I mean, I get… I guess, I guess, to me, the nice test would be for users to actually use it. And I wasn't seeing that based on what we were discussing earlier. And so, to me, if… We, just provide them a way for them to convert… well, this, this… Line that you just highlighted, and then they can try try it out right away. I think that would be actually a better way to test it.
Okay.
**Jason Plumb** 55:49 Especially if we can mark it experimental, because I'm a little twitchy about putting too much non-stable API surface in a stable API, so as long as we're very clear about it being, like, an experimental opt-in thing, then I think it's fine.
**Hanson Ho** 56:04 Inside of me are two wolves. Oh, go ahead.
**Jason Plumb** 56:07 Jamie.
**Jamie Lynch** 56:08 I was gonna say, as, like, two actions, what I'd be happy to do is I can take a look at resurrecting this PR, which is kind of for the internal usage, and I can see if there's a way that allows folks to opt in to getting that, got an API, publicly, pin.
Requiring some sort of opt-in.
**Jason Plumb** 56:33 I think that's a good first next step. Yeah, I think that's great.
**Hanson Ho** 56:39 Cool.
This is my… this is a medium wolf. My, my conservative wolf is slow drip with internal. My aggressive wolf is slap it on, and say, use it. You could, as long as you opt in, use the entire thing. But a medium would be probably slap it on, but not…
**Jason Plumb** 56:59 This is the deal breaker, though, maybe, like, we have to keep this.
**Hanson Ho** 57:04 Yes.
**Jason Plumb** 57:05 I mean, unless we do a version bump, we can't change that.
**Hanson Ho** 57:08 Oh, no, that…
**Jason Plumb** 57:09 Yeah.
**Hanson Ho** 57:10 Even my aggressive wolf isn't saying, you know, change that, like, right away.
**Jason Plumb** 57:17 The burden of stability.
Cool, we are basically at time.
I will just point out that, in case it wasn't obvious, I think I think I mentioned it, but I think this got out last week.
There's some great stuff in here.
Probably already saw it, but I'll just mention it in case you hadn't.
**Cesar Munoz** 57:41 Thank you.
**Jason Plumb** 57:46 Alright, everyone, thanks for your help, appreciate you being here, good discussion today.
And I'll see you around!
**Vishwan aranha** 57:53 Yes, excellent.
**Cesar Munoz** 57:54 Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 57:55 Here you go. Bye, guys.
