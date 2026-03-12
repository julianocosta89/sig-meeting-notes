SIG: .NET SIG
Date: 2026-03-03
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 00:38 Hello, mate.
**Martin Costello** 00:40 Hey Raj, how's it going?
**Rajkumar Rangaraj** 00:42 Yeah, it's going good. How's it going for you?
**Martin Costello** 00:44 Yeah, not bad. Just got back from holiday, so big pile of stuff to catch up on.
**Rajkumar Rangaraj** 00:53 I asked Blanche to join today to go over the logs bridge. Hopefully, I think he will join. We can continue the discussion.
**Matthew Hensley / Grafana Labs** 02:14 Hello, folks.
**Rajkumar Rangaraj** 02:25 Martin, would you be able to drive today?
**Martin Costello** 02:29 I can try, but there's a GitHub… there's a GitHub incident that's just started, so…
**Rajkumar Rangaraj** 02:36 Okay.
**Martin Costello** 02:37 Let me just get, let me just get the repo up.
So, do you want to do, The agenda items first, and then go through the issues.
**Rajkumar Rangaraj** 03:08 Yeah, that's better, yes.
**Martin Costello** 03:13 Dated.
Cool, I'll… Make this part of the next item.
There we could just talk it all through at once. So, do you want to start, Matt, as it's your overall item?
**Matthew Hensley / Grafana Labs** 03:51 Sure, can y'all hear me okay?
**Martin Costello** 03:53 Yep.
**Matthew Hensley / Grafana Labs** 03:54 Got myself a new headset, so I'm not sure.
Saw where Ludmilla was collecting some… 2026 initiatives for anyone involved in semantic conventions.
I thought it might be a good exercise for this group, too, just… Make a list of… kind of opportunities or things people are looking to do. I know there's only so much bandwidth amongst Regular contributors, but we have some new people that have been Joining and, wanting to pitch in.
So I thought having a nice list of at least high-level topics, and… Places to get involved might be good for the year.
I took a quick stab and just put down a couple of the obvious ones.
Yeah, that's… Nothing too complex.
Just wanted to see what, everyone else thought about… At least doing the high-level version.
**Martin Costello** 04:53 Makes sense to me. Would it make sense to have… Like, a top-level… Issue to track all the sub-items.
**Matthew Hensley / Grafana Labs** 05:07 I don't personally… I mean, we haven't done a lot with, like, GitHub projects.
So much in this group.
But however we want to organize, that means something… To point people to would just save everybody some time.
I couldn't ask a good way to get involved, so…
**Martin Costello** 05:26 Yeah, I wasn't thinking anything too complicated, just like, A way to just link it into, like, a coherent, this is what we're thinking of doing this year.
Rather than us just having, like, disparate pile of issues. Because, like, it took me… it took me a while to find the declarative config one.
**Rajkumar Rangaraj** 05:46 I think we should add, if we are planning to drive this initiative in any order, I would say, have a milestone every release, what's the… time we want to do the release. For example, once the logs bridge is ready.
We could have in the earlier milestone, depending upon the work, and base it upon, so we can do the release, and people can test and provide feedback also during the beta phases.
That's what we have been doing in this repo earlier. We can continue to do that.
**Martin Costello** 06:30 Okay, that makes… that makes sense to me.
So… so that was… is there anything anymore on a log bridge as a specific item?
**Rajkumar Rangaraj** 06:42 The logs, which I… we have Blanche here. If you remember, like, two weeks back, we had a discussion. I think most of the work is already complete, I believe, and Blanche did the work, so we can get to know from here where do we stand if he remembers it.
And then we can plan on, who can do what, and how we can take it forward.
Blanche, you want to take it over?
**Mike "Blanch" Blanchard** 07:12 I will do my best.
**Rajkumar Rangaraj** 07:13 Yeah, thank you.
**Mike "Blanch" Blanchard** 07:15 So, you know, it's been a long time since I looked at it.
I think the last I saw, there were PRs adding, like, support for the event name?
Which was a newer thing that happened in the spec.
A long time ago, there was a branch.
Probably still exists. There's, like, a main logs… Branch out there.
So when I originally started working on this, what I was trying to do was… create… God, were they called? Appenders at the time?
We wanted to support SiriLog and N-Log and be able to bridge them into the SDK.
So there was a branch where I had… those libraries built using the log bridge.
I don't know if it would compile, but it… it came up often. People would ask for this. And I'd always tell people, like, yep, what you need to do is resurrect those two projects, throw them in contribib.
Implement them using the log bridge.
Release them as alphas or previews so that we could get feedback from the community.
the feedback I was looking for is… The bridge as I wrote it, I tried to make it as spec-compliant as I could.
we shipped… in the SDK logs.
really early in the OpenTelemetry universe lifecycle, like, long before the log bridge existed, before there was, I think, even a stable log spec.
And we did some things in the SDK that kind of put us in contention with what became the final specification.
Like, our log record… API has some iLogger stuff that leaked into it, right? It has, like, Exception.
I think it has category names still.
Originally, it had state that was an object.
And I tried to retrofit, like, the iRead-only list attributes, and there's some stuff obsolete, and it's kind of a mess. So when it came to the log bridge.
The spec says, you know, you should be able to effectively pass an OLTP or OTLP, any structure as a log body, we don't really support that in the SDK, so it's… it's as close as I could make it.
The API that existed was for the simple case where you want to pass key-value pairs.
My intention was to always add an overload where you could do something to pass, basically, a structure, and then solve that in the SDK somehow.
That never happened.
And I also never saw, like, a strong user demand for that feature. It's part of the spec, but it doesn't seem like .NET users are screaming for that.
It is something SiriLog supports. So when you write a Siri log message, it has this destructuring syntax, where you can pass it just, you know, here's a class.
And it will walk that thing and decompose it into properties. So the Siri log bridge that I did just doesn't support that.
There is a Siri log open telemetry package.
that if I recall, it doesn't use the SDK, it's just implemented fully. I think it only supports OTLP, and it effectively has its own exporter.
the Siri log maintainer was kind of involved with us a little bit. We were commenting on his PRs, he was commenting on ours.
The eventual hope is he would own something and contribib that plugged into the SDK, so serialog users could use other exporters and other SDK features. I don't know where he stands on desire to do that, I have no idea, but… That's kind of the state.
I don't know if you… if you want to open the code, we can kind of look at it, but… That's sort of a nutshell of everything. Now, there was a lot of pushback from, really, the Microsoft team, so my team, Raj, you know, Riley, we sort of in-fought a little bit on this, like.
Should we even have the bridge? Because iLogger itself is a bridge. The iLogger interface just maps to providers, and OpenTelemetry SDK is a provider. We discussed with the .NET team, Noah, Tarek.
Should there be something in .NET?
to do, effectively, what OpenTelemetry wants. There wasn't really any desire from .NET to do that, because from their perspective, more or less, they already have that. And I think, Raj, you did some proof of concepts, like implementing the bridge strictly on iLogger.
it works, I mean, people are doing it. Effectively, our SDK does it. It doesn't solve any of the same problems, because iLogger itself it doesn't have a data model. You can't give it, like, an any structure. You just give it, like, a state, and it… you just basically kick the can down to whatever iLogger provider is gonna… Handle that state and do the right thing with it, so…
**Rajkumar Rangaraj** 12:59 That's correct, Blanche. And if I understand correctly, as you are saying that, the Nova and Tariq were all… were fine. They are not going to introduce anything in the .NET at this point. I think we need to build something at the SDK, so whatever you have it, I think we need to invest in further and take it forward.
At this point.
**Mike "Blanch" Blanchard** 13:22 Yeah, I think, you know, what I did is very efficient, and it solves probably, you know, most use cases. If you really need the complex destructuring and you're using SiriLog, you're probably happy with what you're already using, the packages that already exist. I don't know if necessarily we need to support that stuff, it just is part of the spec.
So we're always gonna be out of compliance.
And I don't know how to solve that, because it's deep in the SDK, you know, it's like one of the core things, is we have our log record, it has its API, that's what we expose to exporters, you know, it's… it's tightly coupled at this point to anyone that's built an exporter on the .NET SDK, and… breaking it.
Would be a big change.
And… I don't know if it's really necessary, like, you know, if you want To support complex destructuring.
It's tricky to do because… When somebody writes a log statement, and they give you that data.
there's two things that can happen. If we're using, like, a simple exporter.
You process that before you return to that call.
Everything's great. Great.
If you need to put it in a batch, You're kind of… in dangerous water, because that thing that's being logged, like, let's say it's a user class, and, you know, the first log statement is like, okay, here's the user before, and then a bunch of mutation happens, and then they log user after. If we just stored that class in memory.
eventually the exporter would probably, you know, export something that has been mutated after the log, and the data would be incorrect. You have to capture… when you're processing that emit log or that log statement, you have to capture everything you need if you're putting it in a batch.
So, in order to do the complex case, now you're looking at, like, reflection.
you're looking at buffering all that in memory, you know, if somebody gives you an array of nested things, you're looking at a lot of complexity, cyclomatic complexity, like, it's not a trivial thing to do in a high-performance way. So what I would hate to see happen, like, let's say.
We bit the bullet, and we blew up the log record, and we supported this complex thing.
The most important case is what we're already doing, where you get simple key-value pairs. I would hate to see us, like, buffer all that into memory, and do a bunch of reflection, or do, like, a bunch of crazy work for the simple case.
we really would only want users to pay that cost if they really needed that feature. Does that kind of make sense?
That would be just my… my primary concern is, like, not… let's not take a huge perf impact for a feature that no one is using today, and I don't know, I haven't seen the issues in a long time, but I don't know if anyone is even screaming for this support.
**Alan West** 16:24 I think… I think one of the things that you're… one of the found… like, foundational assumptions of what you're going on right now is that if the API were to take just, like, an object, and we wanted to somehow, like, destructure that, but if we… conceivably, like, we could have a different API that took some sort of, like, an open telemetry type that was meant to… more match.
The specification, or at least the data model.
And… Tell users that they have to use that if they want this, like, you know, this any type.
**Mike "Blanch" Blanchard** 17:05 Yes. So I can…
**Alan West** 17:07 Can we open the log bridge, the public…
**Mike "Blanch" Blanchard** 17:11 Like, in the API project.
I'll kind of give my thoughts on what I was planning to do.
So go to, like, the opentelemetry.api, project.
And then in the… probably in the logs folder.
It's probably… Logger?
So… So there's that emit log call.
Which is, like, a helper for the second one. That's kind of the heavy lifter.
So this is kind of the contract where you can say, okay, here's the log data and the attributes. That's sort of the case we support today. What I imagined was adding another overload That gives you that first parameter. Okay, here's the log data, you know, severity, severity text, that stuff. And then there would be a second thing that's like.
I imagine, like, an interface, or it could be… Something more perverse, like, you know, a source generator where it's giving you a callback to some generated code, and what that code would do is… Own how to serialize the thing.
what I would do is pass that down with the log record into the SDK, so if you're in that simple case, and you want to write it out, you know, inline.
you call that code, it writes it, you know, to some API, and then you're just forwarding that to some byte array or ETW, you just write it right out to the destination. So you never write it to, like, a buffer.
When you don't need to.
In the batch case, we would call that same code, but we would serialize it to some memory that we have pooled, so that we can stuff it, you know, in memory until that batch is written out, and then it would just write out what we already captured.
what that would accomplish is, it would keep the perf pretty good, and it wouldn't involve, like, reflection. We would basically tell the user, like, if you want that support, you have to satisfy some contract that's gonna make sure, you know, the perf is maintained, and we don't take on… Some mass of reflection or some other solution to try to do that heavy lifting.
**Martin Costello** 19:40 So, it sounds a little… I just… oh, drag a tab on. It sounds a little bit like how, the scope stuff works in iLogger.
Where, like, you… there's a generic method, and you're given an action.
And then it does whatever you want on that.
So it sounds a bit like… You're proposing something similar, where you, like, if you want to log a custom type.
You also provide the implementation of how to turn that type Into the thing you want to log.
**Mike "Blanch" Blanchard** 20:13 Yo.
More or less. And then we could be nice, and like… We could provide a source generator so that, you know, we can just spit that code out using reflection at compile time.
So when, you know, the binary ships, it's all nice and compact and ready to go, and… doesn't require… you know, it would be native AOT compliant. It wouldn't require runtime stuff.
Now, that doesn't have to be done.
you know, to expose this and ship this, that could be, like, you know, something that is added.
Those are just my thoughts on how I would… how I intended to bring this into full compliance with the spec at some point.
So basically, you have two emit log calls. You have one that's, like, the simple case where it's, okay, here's the static data, here's the attributes, and then we have a… Heavier method that's like, here's the static stuff, and then here is the serializer for the payload.
**Martin Costello** 21:23 There might be some prior art as well in the .NET extensions repo, like, all the, like, the log redaction infrastructure, Because that's probably… Does similar things where it takes complicated things, and then… adjusts Stuff on the way down to the logo.
**Mike "Blanch" Blanchard** 21:47 For sure, it's sort of a can of worms when you get into that world. So, like, prior to working on OpenTelemetry.net, I was contributing a lot to system.text.json.
And you just, you get into this world where… Okay, we're gonna give you a serializer, and we're gonna pick some types, you know, date, time, string.
dictionary, what you'll get is just this constant stream of people asking, like, oh, I want you or I, oh, I need version, oh, I need the date only. So you… my recommendation would be If… We do this.
Start with a policy that's like, here's the types we're gonna support and why, and we're gonna draw the line somewhere.
Otherwise, you're gonna open yourself up to just… constant feature creep.
There's a lot of types in the BCL.
datetime, GUID, URI, version, like, it's just… it's endless, and… People will always want their… random thing.
**Martin Costello** 23:01 Yeah, I think for STJ, I think… I can't remember when, if this landed when it was brand new, or if it took a release or two, but, like, having the extensibility on the converters.
probably helped reduce that, because if people really wanted a type, there was the infrastructure to write their own JSON for that.
**Mike "Blanch" Blanchard** 23:22 Yup.
Good to have a solution there, saying, like, hey, if you need something more custom, here's how you make it extensible.
**Martin Costello** 23:42 I've lost the tablet. I was gonna say, but the… Would you be able to, like, put a very… if it's not already in here, put, like, a very high-level Summary of what we just discussed into the issue here.
And then we can circle back around to looking at what we'd actually… the concrete implementation we need to do.
Great, thanks. Any more on Logs Bridge?
3, 2…
**Rajkumar Rangaraj** 24:22 One, one more question to Blanche. Blanche, if we need to do, the stabilization of, the logs bridge. How much effort do you think is needed? Do you think just switching those experimental to… like the… Removing the experimental flag, would that help, or do you think… I know there are the challenges, which you'll discuss, that we can go on and do it incrementally. We don't need to wait for the initial version.
So, based on, whatever you have worked with, would that help? Just switching the… removing the experimental flag?
**Mike "Blanch" Blanchard** 25:04 I mean, that would make it stable.
**Rajkumar Rangaraj** 25:07 Yeah.
**Mike "Blanch" Blanchard** 25:07 what, you know, what Riley always told me, was… We needed customer feedback.
**Rajkumar Rangaraj** 25:17 That we can gather through the beta versions, also.
**Mike "Blanch" Blanchard** 25:26 So it's pretty early in the year, you know, if you want to switch it to stable, spit out a beta.
Try to find some customers, that would sound like a good plan.
**Rajkumar Rangaraj** 25:41 Julius was asking about it. Like, Julius, do you have any other questions for us? You have been bringing this for a very long time.
the…
**Julius Koval** 25:50 Well, yeah, I guess I was mostly curious about, You know, what it would take to stabilize it, and if I could help somehow.
Regarding customers, I'm actually using the API, so… There's that.
Yeah.
But I don't really have other questions.
**Rajkumar Rangaraj** 26:19 Thanks, Milaj. Thanks, guys.
**Alan West** 26:21 Julius, another question to you. So, what is… From the standpoint of what you'd like to, contribute, what's… what's all on your mind? I mean, you want to stabilize the API, but, you know, like, of the thing… of the other things that Blanche mentioned, like, the various appenders that had been prototyped for, like, Serialog and N-Log and so on, and then this… this, discussion about complex types. What… What's within the scope of, kind of, what you would like to… contribute or work on, or have bandwidth for? Is it just the API, or is it some of those other things?
**Julius Koval** 27:07 Well, I, I actually have made an appender for in-law.
Okay. Which is kind of the reason why I'm bringing this up.
Sweet.
**Alan West** 27:18 Okay.
**Julius Koval** 27:19 Yeah, so, I mean, like Blanche mentioned, an appender for Serlock actually exists, so I'm not sure… How much demand there would be for… one based on SDK, but, Yeah, I don't have any experience with Serialog either way, but… Yeah. There was a…
**Rajkumar Rangaraj** 27:39 There was a work from Pyotr. He did create… moved this upenders from the main logs branch to the OpenTelemetry a year back, I believe.
So, he… the… Proof of concept or the working prototype has already been there based on the experimental, if anyone was trying to take a stab on it.
**Alan West** 28:04 Yeah.
Cool, yeah, I mean, I like the plan of, basically removing the experimental stuff, getting this in a beta release.
maybe, maybe even Julius, like, If you'd be interested, putting your n-log appender that you've developed in the contrib repository so that we have, you know, kind of like a whole… End-to-end story for, the API that we can hopefully get people using and feedback on, and so on.
**Julius Koval** 28:40 I mean… Sorry, I'm muted myself.
Well, I mean, people are already using it, I'm not sure how much putting it in the country repository would… Help with that.
**Alan West** 29:00 Oh, okay, I see. You're already, you're already hosting the appender elsewhere.
**Julius Koval** 29:03 Yeah.
**Alan West** 29:04 Yeah, it's no good.
**Julius Koval** 29:08 Anyway, one more thing I wanted to mention… Regarding the complex types.
Right now, last time I checked at least, essentially, our custom… Serializer kind of figures out what the… what the objects are, and based on that, it serializes them. So why not just keep doing that?
**Mike "Blanch" Blanchard** 29:38 I think what we do today is we only capture, like, top-level key-value pairs, and only if the thing is, like, an IRE-only list, or one of those similar types. We don't, like, do a deep copy.
**Martin Costello** 30:22 Okay, is… is that everything unlocked?
**Julius Koval** 30:25 Yeah, just one thing, so I guess, what's the… Conclusion regarding… What needs to be done?
With the Logs Bridge.
**Alan West** 30:43 Julius, would you be interested in opening a PR to basically remove all the experimental stuff, and… We can start, start from there.
**Julius Koval** 30:52 Yup.
**Alan West** 30:52 for doing that.
**Rajkumar Rangaraj** 30:55 And we need to ensure that it has enough test coverage when we move it to stable, and if we figure out there are Tests missing for that, probably we may need to cover and ensure that it is completely covered.
**Julius Koval** 31:10 Yeah, I'll take a look.
**Martin Costello** 31:12 Just… just for my own clarity, do you… do you mean make the experimental stuff not experimental, rather than remove the experimental stuff?
**Rajkumar Rangaraj** 31:22 If you go to the… you have that open somewhere. Can you move to that tab, the where Blanche asked you to open an OpenTelemetry API.
**Martin Costello** 31:35 owed the code.
**Rajkumar Rangaraj** 31:37 the courier.
And open the logger itself after.
Yeah, the top, if you see, we are doing an if exposed experimental feature, then it's marked as public.
So, instead of… we just need to remove that and make the internal as public.
**Martin Costello** 31:59 Right, okay, yeah, so… stop it being experimental, rather than remove the experimental stuff, yeah.
**Rajkumar Rangaraj** 32:06 GIF.
**Martin Costello** 32:10 Cool, I just wanted to check.
Okay, so the next item… Is we've had declarative config kicking around for a while.
And it went stable.
last week, I think?
So, I think I… Alan and I talked about this a little bit at Hotel Unplugged, and we went to the discussion group there. It's like, We've sort of just been kicking the can down the road on doing it, knowing that it was eventually going to be a thing we were going to have to do.
And I guess now it's stable. It's… there's only so far the can can be kicked, so I guess we should come up with a plan on what to actually do about this, because I know… The auto instrumentation has, like, a… vendored… one of the YAML libraries is vendored into it, and it has… it supports, like, a subset of declarative config.
But at some point, we're going to have to bring it into the SDK.
**Rajkumar Rangaraj** 33:19 Would you mind bringing this up in the next SIG or the future SIG? I just need to get into the spec and understand the details related to it. So far, I've not been through this one.
**Martin Costello** 33:32 Okay, that's fine.
**Rajkumar Rangaraj** 33:33 I don't know about others, if they have some other feedback to share, maybe we can go over it.
**Martin Costello** 33:48 Doesn't sound like it. Okay, we can talk about that next week, then.
**Rajkumar Rangaraj** 33:54 Thanks, Dr.
**Martin Costello** 33:55 various contexts level 2? Did you want to talk about that one, Matt?
**Rajkumar Rangaraj** 34:03 I think that's fine, yes.
**Matthew Hensley / Grafana Labs** 34:07 There's not much to it besides, Peter opened up a… Another issue, there's been a whole series of these against the runtime, but… For some of the hotel sampling spec stuff around the probabilistic sampler.
The existing propagation stuff is not adequate, because it only implements Trace Context Level 1.
Level 2, so… Definitely baked into the runtime, and… looks like… This attempt might get it for .NET 11.
**Rajkumar Rangaraj** 34:41 Yeah, this is targeted for .NET 11, I think. The .NET is supportive and at least adding. I also reviewed and left my feedback towards the end.
**Martin Costello** 34:52 Yeah, I guess we're waiting for this one to go through the API review.
**Rajkumar Rangaraj** 34:56 Yeah.
**Martin Costello** 35:00 If this is going to be in diagnostic source, then we'll be able to support it for every runtime.
**Rajkumar Rangaraj** 35:11 We can check around that time, Martin, like, the… trade-offs of bringing this one… this… is this that big feature for the older framework, or… we can have a discussion around that thing.
**Martin Costello** 35:25 Okay.
And… and… Excuse me. And then the last item that's in the list is .NET elements, so I've got a PR open In both of the repos.
that updates all the libraries and adds the TFMs and stuff, but there's… isn't currently… really anything there, other than it's .NET 11.
But, Preview 2 lands next week, and that's got some… updates for ASP.NET Core. They've implemented the semantic conventions for tags, if I remember correctly, so there'll be some work to do in the PR to, like.
do. If .NET 11, don't add the custom stuff, let the runtime do it, otherwise stay the way it is.
**Rajkumar Rangaraj** 36:20 if you feel a feature branch would help to track this efficiently, I'm also fine with this PR. If you feel the feature branch would Help more, probably we can consider that too.
**Martin Costello** 36:36 Yeah, that might… that might be a good idea, just so that… It's easier if other people want to help.
Because otherwise, then it's people merging into my fork, and it gets confusing, so a branch might be easier.
**Rajkumar Rangaraj** 36:50 Yep.
**Martin Costello** 36:51 But, I'll do that next week, after…
**Rajkumar Rangaraj** 36:55 Yeah, nothing.
**Martin Costello** 36:56 guns.
**Rajkumar Rangaraj** 36:57 Yes.
**Martin Costello** 36:59 But, the only… I think the only other thing off the top of my head that's tracing relevant in .NET 11 is that they seem to be doing a push for Blazor.
But I know we've had conversations in the past where we don't really do anything Blazor-related yet, so I don't know if it's… That's worth ignoring at this stage or not.
Anything else for… 2026 that isn't on this list, that anyone thinks should maybe be on the list?
**Rajkumar Rangaraj** 37:41 I don't think we have anything bigger apart from this.
**Martin Costello** 37:53 Okay, cool. Before I go to the open issues and PRs, is there anything else… Anyone wanted to discuss that's not currently on the agenda?
**Zach Montoya** 38:05 I actually have one question, I guess for the 2026. What's, how are we tracking for the profiling signal?
I haven't really tuned into its current development, but I know that it's being iterated on. Is that something that needs to be brought in… that can be brought into the .NET SDK, or are we just leaving that for the auto-instrumentation?
**Rajkumar Rangaraj** 38:32 I think that we should leave the profiling for auto-instrumentation. I don't think it anyways will fit in here.
**Zach Montoya** 38:44 Yeah, I guess my… Only follow-up question to that is if there's any parts of, like, profiling data that we might want to get from the runtime, just so that we can offer that if you do a… encode set up with the SDK, rather than having to rely on auto-instrumentation. I'm not sure if that's… Come up before?
**Rajkumar Rangaraj** 39:10 At least I haven't heard of that, heard in the fig, maybe. Alan is not here, like, he has a… Blanche, have you ever heard about those kind of conversations here, earlier?
**Mike "Blanch" Blanchard** 39:23 I zoned out, sorry.
**Zach Montoya** 39:26 Oh, I was asking about for the profiling signal. I know we have, implementation in the auto-instrumentation, project, but I was wondering if there's any requests or any conversations about getting some of the data from the runtime itself, just through its, Like, the data it exports through, like.
I don't know, meter, listener, or something like that. If there's anything that users want.
Just from the runtime, without having to attach auto instrumentation?
**Mike "Blanch" Blanchard** 40:02 I don't recall anything specific, but I feel like Noah would be very interested in this.
**Zach Montoya** 40:12 Okay, yeah, I just wanted to see, because I know profiling is still under development, and… That would be something, maybe, if there's any topics that we should address in the SDK, we should… Yeah, keep track of it for the high-level 2026 roadmap.
**Mike "Blanch" Blanchard** 40:29 Rod, you might want to ask Noah to take a look at whatever profiling spec work is happening.
**Rajkumar Rangaraj** 40:35 I think he was engaged in the profiling spec work, that's what I recall. I'll bring this up and check with him.
**Mike "Blanch" Blanchard** 40:45 Cool.
**Matthew Hensley / Grafana Labs** 40:49 And I'll just say, if there's anything that, we'd like to do, but we don't have enough time to do, I think… Making sure to write those down would be great. It's just even nice to have for people to be able to join in and contribute.
**Rajkumar Rangaraj** 41:07 Maybe it's a time for us to revisit our issues. Sorry, someone tried to speak and I interrupted.
**Mike "Blanch" Blanchard** 41:14 I was just gonna… mention.
Historically, way back to the beginning of this effort.
I haven't seen the profiling spec, but if it's an API spec.
the mission with OpenTelemetry.net is .NET runtime would be the API.
We didn't really want an OpenTelemetry.api.
like, you take activity, meter, most of what is in the spec API is built into runtime, very intentionally, because we didn't want to force an OpenTelemetry package into the universe, right? If everybody can just do it with runtime.
then your instrumentation is just there, anybody can take the SDK and just grab it.
So if the profiling spec is… API-driven, then try to not build it into our stuff. Try to lean on Noah and Tarek to do it in runtime.
And they'll be very happy to do that, so long as the spec is, like, a stable thing. They're not really interested in… Doing that work until there's some level of stability, but that's the ultimate direction.
Does that kind of make sense?
**Zach Montoya** 42:47 Yep, yeah, that makes sense. I'm, you know, actually unclear about what the state of the spec is right now, but, it seems like… The standardization is primarily on the format.
And then maybe, like, a couple different types, like… CPU or heap, so I think, there's probably not much to do… within, like, in the SDK at all.
And even within the .NET runtime itself, once stabilized, I don't know if… I don't know what that would look like for trying to export that sort of data, like CPU profiles from the runtime, or just letting a separate observer handle that.
But yeah, that makes sense to me.
**Mike "Blanch" Blanchard** 43:38 Nope.
**Martin Costello** 43:42 Cool, thanks, Zach. Any other ideas, pie in the sky, one of, nice-to-haves that can go in the list?
**Zach Montoya** 43:56 One more. Sorry, I just keep thinking of things, Is… op-amp?
planning to do SDK-level controls, because that might be something to bring into the SDK.
**Martin Costello** 44:11 So, there is some work happening for OpAMP, But, Steve from Elastic… And… I can't remember his name off the top of my head.
But there is work for OpAMP happening in Contrib, I think?
Yeah, open crime, yeah.
**Zach Montoya** 44:41 Interesting, okay. I'll… I'll definitely try to follow that.
**Martin Costello** 44:49 Anymore? Last chance?
Okay, cool. Let's just turn to the issues… The only one new since last week, because I don't know what we've already talked about, because I've not been here the last two weeks.
is… this issue… I think I already commented on this one.
Oh, yeah, I remember this one. So, someone's reported there's an overflow.
this, I forget which method it is, but if it returns long.max value randomly, then it overflows and breaks.
it seems… Relatively trivial to me, for that to be fixed.
Although the person who reported it said that they couldn't compile it to fix it themselves, but they haven't replied to me on giving any more details on why they couldn't compile it, in case that's something else we can fix. And then I thought this was funny. I assumed this is some sort of AI.
went, hi, I can fix this for you, and… but then it appears to be suggesting that we pay them to do so.
So I replied and said, you don't do that.
And then… pull requests… There's this one… Can't remember what's going on with this one.
Oh, gods have looked at this one.
And there's been some feedback, plus the build's completely broken.
And…
**Rajkumar Rangaraj** 46:44 Single line change, right? That one.
**Martin Costello** 46:48 Is that the PR?
**Rajkumar Rangaraj** 46:50 So, I don't even know whether, without, like, any benchmark or anything, whatever it's trying to prove is the right thing.
**Martin Costello** 46:59 Well, it doesn't currently compile, so… I'm guessing it's probably using an overload that's only in a brand new version or something.
**Rajkumar Rangaraj** 47:07 Yeah.
**Martin Costello** 47:08 But the thing I was unsure of, and then I sort of… stepped back from it, as Peter was getting involved, is… The justification appears to be doing a trade-off.
**Rajkumar Rangaraj** 47:23 I also wanted… I started on it, like, it needs a… we need to go ahead and take a look into the source code for the spin enter and all that. So before we invest that much of time, we need to understand whether it improves any performance or it brings.
like, what's the overhead it solves? If there is nothing, it does not make sense to invest that time in it.
**Martin Costello** 47:44 Yeah, I think Pyotr already looked at the code.
**Rajkumar Rangaraj** 47:47 Yeah.
**Martin Costello** 47:48 But, but yeah, I agree that… This needs the contributor to give us some numbers.
**Rajkumar Rangaraj** 47:56 Yeah.
**Martin Costello** 48:00 And then… there's another PR I opened two weeks ago, it's still in draft, we don't need to talk about it now, but if people could look at it, one of the items on the… what's it called again? The CLO monitor was about generating SBOMs.
I've… done an approach on how we could possibly do that here, but it does change the way that the artifacts are attached to the release. The details are in here, but I've left it in draft until there's an agreement on exactly how we want to do it, and then I'll either… update the PR, or if we're happy with the approach, I'll just move it out of draft.
So that's all that's in. Main repo, and then… contract… Oh, I've already got the tab open.
Contrip, so yeah, so someone opened an issue to implement, DB response returned rows.
And opened a PR for that.
I… but they didn't sign the CLA, so I said, if you sign the CLA, CLA, we'll look at it. I know they said they're trying to get approval from their manager, so… I haven't bothered looking at the change before then.
But it's one of the in-development attributes, which is why we didn't put it into the SQL client to start with.
And then, as you'll hear, Raj.
**Rajkumar Rangaraj** 49:38 I need to take a look into it.
**Martin Costello** 49:40 Okay, yeah, because, they, they asked, they poked me on, Slack yesterday and asked.
If someone was going to take a look at it, so that's why I typed on it.
Pull requests… So… See, from the last… That one… I'll just open the one in the new tab.
So, this is one I just did yesterday. I had a quick look at a PR you did while I was away, Matt, and I just… I spotted that there was a code pattern that was repeated, so I just put a little bit of refactoring on top of your refactoring.
So it's just a test change… Is there any more?
I'll look at this again in a minute, Fanchica. I can't remember what we're waiting on for this one to, Get merged… There's a change here that's to do… Is this… Geneva… yeah, I think I left this one for you, Raj, because it was Geneva, but it seems reasonable to me.
And then there's this other PR that PR has approved. The only thing I wasn't so sure about on this one was because it's a stable package, and it's a breaking change.
Late.
it's not an API-breaking change, but it's a behavioral change.
It's like, what's the process for us?
taking and releasing such changes, because I don't think, since I've been getting involved In depth here that we've done one of those in a package that hasn't been beta.
**Rajkumar Rangaraj** 52:00 Do you think, is it worth taking this? Like, if it is correcting something, even though it's breaking?
**Martin Costello** 52:05 So, I didn't go and check what the semantic convention said, but according to the description, it makes us follow the semantic conventions for gRPC correctly.
**Rajkumar Rangaraj** 52:17 Okay, let's take a look at it a bit to find a reasonable way we can include it.
**Martin Costello** 52:23 Okay, I'll take a look at that tomorrow, and cross-reference it and double-check.
But.
**Matthew Hensley / Grafana Labs** 52:29 And there's been some change with RPC submitted dimensions.
obviously going RC.
But also, there's some pushback from, CRPC folks.
So… I suspect, I'll have something for that on Thursday, to see how it actually aligns with what we're gonna do.
**Martin Costello** 52:53 Okay, yeah, I guess it makes sense if there's some other stuff you need to change.
the… We wait until they're both in, so we don't have to make two braking changes in quick succession.
**Matthew Hensley / Grafana Labs** 53:09 Yep, I just let this one sit for a minute while we figure it out, because… gRPC stuff is experimental, and the RPC stuff's trying to stabilize, and… JRPC may not come along with that, so… It's gonna be an interesting one to try to resolve.
**Martin Costello** 53:28 Cool. That was all of the issues and PRs from the last week.
Is there anything anyone else wants to talk about?
I'll take that as an edit.
Alright, thanks for coming along, everyone. See you next time.
**Zach Montoya** 53:57 Thanks.
