SIG: OpenTelemetry Profiling
Date: 2026-10-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Scott Gerring** 02:21 Hello?
**Nayef Ghattas** 02:24 Hello.
**Florian Lehner** 02:27 Hello?
**Scott Gerring** 02:29 I managed to join the right meeting this time. I'm very proud of myself.
**Nayef Ghattas** 02:36 Oh, you mean with the Zoom migration and all?
**Scott Gerring** 02:39 Yeah, it was all too confusing for me.
**Florian Lehner** 02:44 And also just before you switched time zones.
**Scott Gerring** 02:48 Yeah, when are we switching time zones again, European gang?
**Florian Lehner** 02:54 End of October, I guess?
**Scott Gerring** 02:58 I won't be here. That's good.
**Ivo Anjo** 03:46 Hello.
**Nayef Ghattas** 03:52 Hello.
**Scott Gerring** 04:28 Are we going to be lost without Felix again?
**Nayef Ghattas** 04:39 Are you volunteering for taking notes?
**Scott Gerring** 04:42 I'm not important enough, I'm afraid.
**Florian Lehner** 04:52 I can do so.
**Nayef Ghattas** 04:57 Thank you.
**Florian Lehner** 04:58 Let's just wait some more minutes and I guess you probably know better than that Felix is not joining. Don't know.
**Nayef Ghattas** 05:06 Yeah, Felix is off for two weeks.
**Florian Lehner** 05:10 Okay.
Then I'm hoping just… Okay, I will wait 2 more minutes, and then just start.
If you have any items you want to discuss, please add it to the agenda.
Also, feel free to add your name to the attendees list.
Okay, then, let's go. Let's start with, receiving action items. I did see that Alex will not, or will not be able to join today, but, The first… Two review action items are on his plate. There is a PR he's looking for. Sorry, I need to probably.
Share my screen.
So… You probably notice I'm not used to everything, so one second.
screen share… Now you should be able to see my screen.
Okay, cool. Starting back, yeah, Alexi won't be able to attend this meeting today.
But he has two action items. I think one of them… Needs more attention.
At least.
feedback.
I don't know why it's not loading, probably.
**Scott Gerring** 07:56 I think GitHub was struggling earlier.
**Florian Lehner** 08:11 Oh, yeah.
Yeah, I just opened the GitHub status page and today I seem to have a problem.
Oh.
Things I didn't notice the last weeks, and I didn't miss.
Yeah, I think, if you have time and GitHub is available again.
Then please have a look.
at the PR Alexi has opened. I didn't have time to look at it. I know he tagged me on this. I probably will take a look tomorrow.
come Yeah, but if you have some spare time, please have a look at it.
Then I would continue to the second one, write a doc proposal for the sample type period semantics.
I see that… Here's an update for today.
And Felix, provided some input.
Which seemed to overlap with a later point.
I'm not familiar with the topic, if someone wants To speak about it, or make…
**Nayef Ghattas** 09:29 Yeah, I think Alexei had a doc, and then there was general approval on, like, consensus that this doc makes sense, but we need to turn it into a concrete proposal, so I think Felix has an action item in the in the action items to do that, and I think we should… we can just cross out Alexi's action item for this.
**Florian Lehner** 09:53 Okay, then… Then I probably will just move on.
To be fair, I didn't pay attention to this document.
In the last few weeks.
Then I will continue with, I have also an open PR.
on the SIG Profiling SIC Profiling repository for ProfCheck. If you have some spare time, please have a look.
It's about… Duplicate, attributes, so, that we are conformed with, our… Specification that we… that attributes should be only once in the dictionary.
Okay, then I will just go on to the next one with Nayef.
**Nayef Ghattas** 10:53 Yes, so I had a review on the versioning change.
That has now all the approvals needed to be merged, so I wanted to check whether anyone in the SIG had any last-minute reservations. If not, I'm going to ask.
Josh and, and or Tigran to merge it.
one of the review items from Robert was that we should document somewhere the initial, like, versioning document that we had.
That explains, like, the alternatives we considered, and why we are doing this, and that has all the details that would bloat the spec if we put them in the spec.
So, we discussed, like, about where to put that doc, and I suggested that we put it in the SIG Profiling repo, somewhere, so I wanted to make sure that this works for everyone, and if it does, I'll open a PR on SIG Profiling to do that.
**Florian Lehner** 12:03 Yeah, I'm opening the document on SICK Profiling works for me.
Yeah. If if you have opened the Pr. Then I will merge the pull request on the profile on the propo.
repository. I think I have.
**Nayef Ghattas** 12:20 Oh, you have permissions. Awesome.
**Florian Lehner** 12:22 Yeah, so if you open the PR, I will… Just push the merge button.
**Nayef Ghattas** 12:29 Okay, thank you.
**Florian Lehner** 12:37 Yeah, that's a permission I just gained recently.
Okay, then… I will hand over to… If there's nothing, on this topic anymore?
Then I will hand over.
Is Tom… Tommy here?
**Nayef Ghattas** 13:01 I think we did that already, and we crossed it and put it in the Achieve action item. I don't know why they are in the…
**Florian Lehner** 13:12 Okay, it doesn't seem like that. Okay.
Okay.
**Nayef Ghattas** 13:17 Yeah, let me cross it and move it as well. The long story short is that this is already implemented in the profiler right now.
**Florian Lehner** 13:27 Okay, cool. Perfect. That's the best action items.
**Nayef Ghattas** 13:31 Yeah.
**Florian Lehner** 13:32 Just already done.
Okay, I just saw that, Scott's topic and Ivo's topic was also crossed out.
In the active action items list above.
**Scott Gerring** 13:43 Yeah, I think we don't have anything outstanding there, hey Ivo.
Shipping.
**Ivo Anjo** 13:49 I think, yeah, I… there's… there might be more things coming up, but I'm not sure we… at this point, we have a lot to… Kind of actively work on.
**Nayef Ghattas** 14:00 Did we resolve the question of what happens when there are multiple process… when there are multiple resource attributes that come from multiple different signals, and which one do we put in the process context in SDKs? I think that was one of the points that Jonathan raised on Slack.
**Scott Gerring** 14:18 I think Jonathan is pursuing that upstream with the SPEC-SIG, right, Ivo?
That's something that he took as an action.
**Jonathan Halliday (IBM)** 14:27 I think it's actually entity SIG, but yeah.
**Scott Gerring** 14:30 Sorry. Oh, you're here.
**Jonathan Halliday (IBM)** 14:31 I spoke to the army. I spoke to the Java people about it and They said, yeah, this is a headache for other things as well.
Particularly when you get into op-amp and dynamic reconfiguration and things like that, with resources. That can change on the fly.
So they're looking at putting in some sort of more general structure that models the resources as sort of first-class entities, and… Those resources can then be handed off to where they're currently used in things like the Chase Exporter.
But can also be, accessed through Official getters, so there will be, in the case of the Java SDK, something on Global OpenTelemetry that allows you to say.
Give me a resource, please.
which is what we need. So yeah, there's some kind of plan in progress.
I'm in the the Java meeting straight after this one. I'll try and see.
What's going on with this?
The downside of them trying to do some kind of general solution like that is it will likely take longer than doing some sort of ad hoc targeted thing just for us, but at least it'll be robust once it's done.
**Scott Gerring** 15:47 Do you have a feeling for how much of a priority it is on their side? Out of curiosity.
**Jonathan Halliday (IBM)** 15:54 Profiling is definitely not a priority, because there's not enough users for it yet.
The entities thing as a whole, more useful, more more use cases for it, so that will bump it up the priorities a bit. But Yeah, more complicated. God only knows how long it's going to take.
I know some of the Java people sit on the entity SIG. I don't, so I don't have good visibility into… How quickly they move.
There are, I guess, some things we can… we can do in the meantime.
Like, I think we're going to need some kind of API service.
for the… The OTEP side of this.
And we're going to need some kind of configuration so you can turn it on or off and specify what exactly is getting exported.
I wonder…
**Scott Gerring** 16:56 I wonder if that's, I guess your suggestion is that we add it to the existing OTIP as something that we define in there.
**Jonathan Halliday (IBM)** 17:03 Yeah.
I think it belongs in the OTEP because with something like an environment variable, you want it to be cross language.
**Scott Gerring** 17:12 Yep.
**Jonathan Halliday (IBM)** 17:12 So that if you configure how does my, my Golang binary export this, you can then move that knowledge, that configuration to your Java binary or whatever.
It should be consistent, and the place to do that is the OTEP.
**Scott Gerring** 17:27 If we just PR it into the OTEP, is that going to be enough for the Java SDK to be happy to adopt it, or are they going to want to wait until it's in the spec itself?
**Jonathan Halliday (IBM)** 17:38 With something like an environment variable… Yeah, probably.
I think the OTEP is…
**Scott Gerring** 17:47 sufficient.
**Jonathan Halliday (IBM)** 17:47 enough to get us started with. I mean, realistically, we can't put things straight in the spec. They have to go via the OTEP.
**Scott Gerring** 17:56 I can just try that. I mean, I'll start a thread in the Slack so we can decide what we want to call it and what the values should…
**Jonathan Halliday (IBM)** 18:02 Yeah, I mean, I came up with a name, and then I.
**Scott Gerring** 18:05 sort.
**Jonathan Halliday (IBM)** 18:06 I hesitated a little bit. I thought, is this a simple on or off, or do we want pluggable implementations? So we can say, set this environment variable. Well, in the case of Java, you'd set it to a class name or something like that.
So you can you can choose which implementation you've got. Because, this this came up in Java because the implementation I've written is for Panama, so it's Java 25.
And I thought, what if someone wants to plug in their own implementation that's using You know, JNI on older.
Java, is there an integration point they can do that? I've got an interface, but there's no way to specify the implementation of that interface. So I thought, okay, what if this environment variable is a… A name, and we define, you know, a couple of plausible values for it.
That kind of issue is, I think.
what we want to be talking about and putting into the Otep.
**Scott Gerring** 19:03 Do you want to… I mean, seeing as you've already thought about it, do you want to start the.
**Jonathan Halliday (IBM)** 19:06 Yeah.
**Scott Gerring** 19:07 I'm.
**Jonathan Halliday (IBM)** 19:07 I think we've already got discussion threads for this on on slack. I'll try to get around to updating them.
**Scott Gerring** 19:14 Yeah, I mean, I'm more than happy to go and try and change the OTEP once we all kind of roughly agree, and maybe it'll be a quick one. The last time we made an addendum to it, it went in really quickly, so maybe this would as well.
**Jonathan Halliday (IBM)** 19:23 Yeah.
**Scott Gerring** 19:25 Well.
**Jonathan Halliday (IBM)** 19:26 This looks like in beyond that I mean, is is there a programmatic Api? Maybe there isn't. But In the case of Java, you've you know, you're configuring everything. You've got global open telemetry, and that gives you some way to build, you know, exporters for each of the signal types, and so on. Is is there some way to treat this a little bit like an exporter? So you say.
I want one of these to Be my… a process context publisher or something like that. Because if there is, we need to get a bit deeper into the The spec of what that looks like.
For the programmatic API. It might be that for now, the environment variable is enough to get started with.
**Scott Gerring** 20:07 Yeah, I was gonna…
**Jonathan Halliday (IBM)** 20:07 Probably just want, you know, turn it off.
**Scott Gerring** 20:11 Yeah, I guess…
**Jonathan Halliday (IBM)** 20:11 Or turn it on. We need to discuss what the default is as well.
**Scott Gerring** 20:15 Yeah, I was gonna say, I guess we don't really need to have to eat the elephant, and it sounds like the trick in Java was that there's just not… there's no way we can make the Java SDK accept any mechanism to turn it on and off, so if we can unblock that, and then kind of pursue the…
**Jonathan Halliday (IBM)** 20:30 because.
**Scott Gerring** 20:30 Like, in parallel?
**Jonathan Halliday (IBM)** 20:31 It's hard. I can try to push them to.
Use a, you know, totally unofficial, not documented anywhere environment variable, but…
**Scott Gerring** 20:39 But we can probably get that into.
**Jonathan Halliday (IBM)** 20:41 Definitely push back on that.
**Scott Gerring** 20:42 But I think we could get an environment variable into the OTEP without too much drama. And then if we just do that and then we pursue the SDK configuration angle kind of in parallel, then maybe we're in a good spot.
**Jonathan Halliday (IBM)** 20:52 Sounds like a plan, yeah.
**Scott Gerring** 20:54 It.
**Jonathan Halliday (IBM)** 20:56 I mean, I don't think there's a rush on it, because until they figure out What we're doing with resources, it won't merge anyway, but still good to talk about.
**Scott Gerring** 21:06 Ivo Nayef Por.
**Ivo Anjo** 21:08 Maybe Nayef.
**Scott Gerring** 21:09 Go for it.
**Nayef Ghattas** 21:10 No, go first, go first.
**Ivo Anjo** 21:13 Because I wanted to go a bit back to kind of, ask if, I'm… I heard something, and I'm not sure I underst… I interpreted, so I wanted to clarify. I guess… Do we think we'll need to configure the risk?
the resource, like, okay, we'll need to configure things inside the resource, or, like, or when we say, like, I'll configure between resources or something, it's like.
**Jonathan Halliday (IBM)** 21:41 Okay, so.
**Ivo Anjo** 21:42 For resources, which one or something?
**Jonathan Halliday (IBM)** 21:44 Yeah, exactly. The situation we're in at the moment is that It is possible there is no resource.
In which case, yes, you have to configure it, otherwise there isn't one. It is possible there are multiple resources, in which case your configuration might be as simple as, I want that one, please.
It might be that you want a custom resource, so there are some that exist, but you want a different one.
But even if there is one, and even if you say which one you want, it's hard to get at in Java, because nothing in the current spec says that the components that have it have to expose it, and they don't, currently.
So I would have to go to the Java people and say, add a getter for that. And they'll say, that's not part of the specified API.
There's also some lifecycle issue in that the resources don't exist until the exporters come up, which is quite late in the the bootstrap. So we can't have process context until that point.
And there's no lifecycle hooks defined for getting a callback when initialization is complete.
So there's no way for the SDK to say, okay, this resource is here now, here you are. Please publish it.
I don't think we want to specify lifecycle hooks exactly, but It's… It's another stumbling block to integrating this in that if I say, can I have a lifecycle hook, please? They'll say, no, there's no spec for that.
**Ivo Anjo** 23:20 Okay, thanks. Yeah, thanks for clarifying. I was thinking something slightly different, so that's much more.
**Jonathan Halliday (IBM)** 23:25 Yeah, I mean, I can hack this. I've got it working by making changes to the SDK, but getting it merged is… is going to be hard without some kind of spec saying, this is the way it's going to work across all the other SDKs, because, again, we want some consistency in this.
At the moment, there's too much freedom in implementations. Like, one SDK could decide, oh, we're going to require a custom resource, and it's going to be configured using these properties.
Another SDK could say, oh, we're going to take the one from the trace exporter, and if there isn't a trace exporter, you don't get process context either.
And it's going to be a mess for users, right? They're going to have to understand the implementation details of each language SDK, and I don't think we want to be in that situation.
**Nayef Ghattas** 24:19 So, it sounds like we want two things, at least. The first one is an environment variable to be able to turn it off, or turn it on, and decide if it's on and off by default.
**Jonathan Halliday (IBM)** 24:31 Yes.
**Nayef Ghattas** 24:33 And the second thing is figure out what we put in there. And one thought I had regarding that is that I know that it's the case in Go, and I suspect it's the case in most SDKs that there is the concept of a default resource.
So, maybe one simple way to go around this is to say that when this is enabled, at least in the beginning, we just put the default resource in it, and.
**Jonathan Halliday (IBM)** 25:00 If someone's overriding it.
**Nayef Ghattas** 25:03 This, but I'll have to check.
**Jonathan Halliday (IBM)** 25:05 I know out of the box, the default resource in Java isn't actually initialized. It will just give you like empty string or something, which is useless. I'll have to check. I think you're right. I think there is a way to initialize it.
And if that can be done from.
Environment variables or such like already, that's probably fine.
But again, it's a lifecycle thing, because if we try to bring up process context before whatever reads those variables and sets up the default resources have a chance to do its thing. It's not going to be there yet.
**Nayef Ghattas** 25:40 Yeah, I think we have ways to deal with that in the… profiler and in the spec, right, if we listen on specific system calls, and then… and I believe that was already implemented in the eBPF profiler to deal with, like, delayed resource initialization and have the reader reread it from the… from the process context.
**Jonathan Halliday (IBM)** 26:05 Yeah, but in the Java SDK, for example, you'd have to have something that was spawning a thread and was going to periodically poll to see if the resource was there or something, because there's no callback hook, right?
**Nayef Ghattas** 26:17 Yeah, I see. Or add the callback hook.
**Jonathan Halliday (IBM)** 26:20 Yes, exactly.
**Nayef Ghattas** 26:20 Yeah, yeah, yeah.
**Jonathan Halliday (IBM)** 26:22 But I need to know what I'm asking the SDK people to add and why.
**Nayef Ghattas** 26:28 Okay.
**Jonathan Halliday (IBM)** 26:28 Yeah, we have a path forward. Let's move on.
**Florian Lehner** 26:34 Okay, thanks for the discussion. I was out.
on the topic, so I cannot contribute much on this.
But yeah, I agree that, Making changes to the OTEP should be straightforward.
The next two items… are by Felix, and as he's out, and also as Alex is out, I think we can skip them unless someone wants to speak up for them.
Doesn't look like this.
Then this will bring us to the end of the review action items and We have our first agenda topic with Roger.
Roger, do you want to start?
**Roger** 27:22 Yeah, sure. Well, this topic is about a PR that I opened a couple of days ago. It's about… just removing a main.go file that we have had in the ebpf profiler.
Repository for a while and actually it's been kind of the entry point.
for just using the eBPF profiler for years probably already.
But just a few months ago, we kind of added, another way of creating a binary that it's embedding into the open… an OpenTelemetry collector, so using it as As a receiver, So we made the, let's say, the VPF profiler and OpenTelemetry collector, first-class citizen, right?
And the issue is that now we have these two ways of launching the eBPF Profiler. And it seems that the, let's say, the legacy way.
It's being, let's say, Well, it has less configuration options and less features than the collector, because some of the new ones that we added in the last two months, they were not added there.
So, that's basically why I… put that PR just to remove it and just, let's say, support the eBPF profiler as a receiver.
Example.
And I think so far the maintainers agreed on removing it, but Yeah, we just wanted to ask here if anyone is still kind of relying on that binary, or still using it, and things that.
We should keep it.
And if no one, yeah, no one is opposed, we just, I mean, just, we will just remove it.
Yeah, the little thing is that One of the, let's say, of the… Points of keeping it was, to have it as an example of using as a library, right? It's one of the promise that we made for this, For this, receiver.
But I think that could be solved in other ways, like in a with an integration test or a main, a main test or something else. But we don't need to keep like, say.
Well, the CILA flags, et cetera, et cetera, and.
Also, another point, sorry, of removing it is that we have some custom code that actually is embedded into the eBPF Profiler binary, that it's an OTLP receiver, sorry, reporter.
So basically you can send the data through this reporter.
And I think it doesn't make sense to have it there, because the community already has an OTLP exporter with far far more configuration options and features so we can just remove that code as well.
yeah Florian any comment.
**Florian Lehner** 30:41 Yeah, I'm super fine with removing, this, main executable, The only reason I did not approve it is the CI checks did not pass it due to the license stuff.
But once this is fixed, I'm happy to approve it.
5?
**Nayef Ghattas** 31:01 So, I was just going to flag that I think at some point I discussed with… we discussed with Dale's team. And they were not using the collector, but they were using the… The standalone binary that the profiler provides, plus the… Yeah, the custom exporter that we have inside the repo.
So just raising that, because, like, if we're going to merge it, this will likely break things for them, which could be, like, an acceptable, things.
**Roger** 31:35 Okay, so you mentioned about the Baylor folks using it, right?
**Nayef Ghattas** 31:38 No, not beta, like, Dale, I don't know… I don't know, Ivo, if you know, the person who works on Ruby, he's one of the… Ruby approvals on the repo.
**Roger** 31:50 Okay, yeah, I got it. Yeah, maybe I can ping him in a Slack, just a quick message on the app he makes.
**Ivo Anjo** 31:58 Yeah, he's very responsive on Slack. I believe it's at Shopify. It's from Shopify.
**Nayef Ghattas** 32:03 Okay, bye.
**Roger** 32:05 Cool. Cool, great. Thank you.
Better to notify everyone.
**Florian Lehner** 32:21 Okay, thank you, Dan. I think going to the next topic, Ivo.
So the next topic is with Ivo and he's asking for review on the design document about Node.js thread context.
Not sure if you want to add something, or just ask for… Feedback, Ivo.
**Ivo Anjo** 33:18 Yeah, just for the reviews, me and Scott have been stabbing at Attila's document for a bunch of time. I think it's good for external consumption, and I think it's… Well, personally, we've poked a lot of holes, so I think it should be, like, read it, see if you understand it, or if there's some obvious thing that's not there, and hopefully, yeah.
Give feedback. But yes, I think it should be in good state to do that.
**Florian Lehner** 33:55 Cool. Yeah, I can. Maybe Roger has some thoughts on it.
**Roger** 34:03 I haven't had time to take a look at it. I need to spend some time.
**Florian Lehner** 34:10 Okay, yeah, same for me, I didn't have time yet to look at it,
**Scott Gerring** 34:14 Have any of the dash zero slash former polar signals folk had a look? Do you know Ivo?
They're probably the closest to it in this group.
**Ivo Anjo** 34:23 They have looked at the implementation and have reviewed a bunch of the work in the implementation. I am not sure if they looked at the document. I can ask.
I can ask them to look at it as well.
**Scott Gerring** 34:34 Yeah.
