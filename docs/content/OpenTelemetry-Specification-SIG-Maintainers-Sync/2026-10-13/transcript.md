SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-10-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Reiley Yang (Microsoft Corporation) 00:00:23 Hey, morning, Alex, David.
David Ashpole (Google LLC) 00:00:27 Morning.
Alex Boten 00:00:29 Loom.
Joshua MacDonald (Microsoft) 00:03:16 Good morning.
Are we here?
Can you hear me?
Alex Boten 00:03:22 I can hear you.
Joshua MacDonald (Microsoft) 00:03:23 Very good.
I like it when it works. So, here we are, another Tuesday.
It's my week, so I'll open us up here. We have a whole theme today about the collector.
And we're going to… so this is one of our, kind of, periodic check-ins with the SIGs.
And today we have a collector SIG, including myself and a few others, to present more than one topic.
And then I see the rest of the agenda, so fill yours, your items in. I've put 15 minutes for the first topic.
we could end up at least with half an hour on the collector, so I think we should just go. And so, without more I'll say that I can say, we'll introduce, I think, Alex or Pablo to take us into the first topic.
Alex Boten 00:04:14 Yeah. Pablo, do you want to screen share since you'll be driving a lot of the.
Pablo Baeyens 00:04:20 Yeah. Presentation.
Joshua MacDonald (Microsoft) 00:04:22 Unshare.
Pablo Baeyens 00:04:26 Let's see if this works.
Okay… Can you see my screen?
Alex Boten 00:04:38 Also, sorry, I didn't realize we packed so many collector topics in this meeting. I guess it'll be pretty collector-heavy.
Joshua MacDonald (Microsoft) 00:04:45 Anyways, good.
Alex Boten 00:04:47 Yeah. All right. So hello.
Everyone… Before we jump into the Collector V1 update, I did want to give a little heartbeat kind of status update of what the Collector has been up to.
Also wanted to take a moment to celebrate some of the, like, pretty big achievements that we have within that SIG.
For example, we've had over 390 contributors this year, if you believe LFX. I don't know, you… you know, your mileage may vary with those stats, but that's kind of what it's reporting. We have a very large number of Maintainers, approvers, and triagers. It is a lot of work, because as you can see in the next point, one of the challenges that this group has is that we have 250 components and more.
And we do have over 180 different code owners, which means that we have, like, A nightmare of reviews that we kind of go through every day, every week.
We also have one of the unique challenges of having 3 different kind of components that people care about. We care… end users will care about the binaries we produce.
This will come out of the releases repository. Component owners, like many of the ones listed here, will care about the APIs, and so when we talk about the V1 release, we're going to talk about multiple kind of areas that we have to focus on when we're doing… when we're doing that work.
And… as we're pushing forward with the V1, it's also, you know, it's also really important to continue supporting all of the people that are putting in time to fix bugs, you know, create new features within the collector, so it's… It is a lot of work to do all those reviews and try to move the V1 forward, so if other folks from other SIGs have thoughts around how we can make things better, if there's tooling that works that we can share across the repos or whatever, like, we're happy to have those conversations. But for now, I think we're going to talk more about the V1 priorities.
Pablo Baeyens 00:06:49 Right. Okay, so I'm going to… walk you through what we've done so far, and what Alex and me are proposing to do next.
So, some of you may be aware that around 2024, maybe even late 2023, we defined a GA roadmap for the collector that included an OTLP V1 distro. That would be a collector distro that has just OTLP receiver, OTLP exporter, and maybe you can do some processing in between.
And… In this roadmap, this meant both Go API stability for some things, namely, for example, the Go modules that are used for building something like the OTLP receiver, or OTLP exporters, and it includes some goals about the collector, like it should be observable, it should be scalable, some documentation goals, and some goals about, like.
Technical support, how long a distribution would be supported for, and such.
So since 2024, the progress is tracked on this issue. I think you should all be able to access the slides. If not, send me a message.
We've had 26 Go modules that are released as V1 point something.
Including things like the loading of configuration, and the core APIs for most component kinds. Connectors are not there, but if you want to build an exporter, receiver, extension, processor, with some caveats, you could maybe get to.
Having a stable, Go away, Peter.
And a lot of progress on batching, I don't know if I'll wait for the next topic from Jay McTeague.
Now, we also had another plan.
that we started working on late last year on some high-priority components. This came after the Technical Oversight Committee feedback regarding open sanitary graduation, and it struck on this other issue.
So, we went through the collector survey data, we got feedback from different vendors on what were the top most used components, and we came with a list of 7 components that we should focus on at first, since they were very widely used.
On… In that sense, well, we have… Define how you get a component to be V1. We have released our first component as we want, the Kubernetes Attributes Processor.
And then there's been progress on other components, for example.
Thank you, Receiver.
Most of the work has been happening at the spec level on defining the transformation between Infuse data model and the HLP data model, but it is going forward. Then… On the transform processor and filter processor, which are also on the high priority list.
We are aiming to have OTTL The Go package sort of defines OTTL, the Open Source Transformation Language, BB1 soon, probably next release.
And we've also had efforts around… Automatically generating documentation, and automatically verifying some of the requirements on the component graduation process.
Now, we want to combine these two things I mentioned on a new RFC proposal that Alex and I have been working on.
Because, well, it's… it's been… Quite a long time since we… that are like Go on.
releasing V1, and we want to something be very or confused about it not being V1.
And so we want to focus on end users of collector distros, as opposed to something like custom distro, or something like, component developers or vendors that build their own Sort of distribution.
And what we want to do, basically, is that by KubeCon Europe 2027, we would like to release a V1 core distro.
And leave some of the stuff that we were working on, for V2.
What does it mean concretely? Sorry, Alex, I'm going very fast, maybe you want to intervene at some point, but…
Alex Boten 00:11:34 Nope, you're doing great. Keep going.
Pablo Baeyens 00:11:37 Okay.
Sure. So, so, what we're doing… As part of this proposal, we keep on validating the stability of the remaining components from that high priority list.
We want to prepare the core distro for BMV1, that means modifying the component list and having a mechanism to be stable by default. I'll cover that, in a… future slide. And some parts of the OTOP V1 distro roadmap, we also want to continue doing. For example, batching, Jim McD will talk about that, and also three core Go API, Go modules we want to release as V1.
Three remaining ones.
Then I think the more important stuff is what we do not plan to do according to this proposal. So one of them is… We… want to drop… we've effectively been working as if semantic convention stabilization is a requirement for a component to be released as V1. For example, this is what we did with the Kubernetes attributes processor.
But we want to sort of drop that requirement and allow, for example, something like the host metrics receiver, if it's not ready by… if its semantic conventions are not ready by KubeCon EU, to be released as V1, and the stable semantic conventions will go in another major version.
We are also proposing to drop new pipeline telemetry, so this is a rework of the internal telemetry of the collector that is available under an alpha feature gate.
With the idea being that this would still be something that we want to release eventually, but not on the V version.
We're not stabilizing all components on the distro, so there will be some components that are still not V1.
We… so some of the high-priority components have subcomponents, things like the resource detection processor, or you could see stance operators on the file log receiver as subcomponents. We also don't want to, like.
Look at all of them individually and, do major improvements of them.
or OTTL functions could be another good example.
Basically, if there's something that is very experimental or dubious, we would get it under a feature gate, but otherwise we would consider what is today as the B1.
And, well, we are focusing on users of binaries, so other parts of the collector, contrib distro, CPE profiling, the Go APIs, those wouldn't go.
With this.
And the last thing I want to mention, so here… I said, I can assume to be stable by default, as part of preparing the core distro.
This would be something for a different RFC.
The goal is that the collector feels stable by default when you use it, and it's easy to understand when you opt into something unstable. And the idea would be to have something like Release trains… we already have that, but The idea would be that by default, you can only use stable components and only have access to stable features, and if you want to have unstable components, if you want to have unstable features, you would have to pass a CLI flag, or maybe something in the configuration, to be able to use those. And you can choose what level of stability you want in your collector experience.
And that is all. Thank you.
Joshua MacDonald (Microsoft) 00:15:12 All right. Well, that was great. I imagine there may be questions or discussion topics.
Tigran Najaryan (Splunk Inc.) 00:15:18 I… I have a question, actually, about the V1 and, I guess, after the V1 thing.
I think… So, looking back at, I guess, at the time when I was a maintainer, I think one thing that I did Wrong was that I was maybe too careful in trying to get the V1 right, and… And that delayed.
the, I guess, the… what we want it to be, the V1, right?
I think… Like I said, looking back, I would do this differently.
I will get the V1 out much sooner, and… Then iterate on new major versions.
Even allowing breaking changes in the internal APIs.
While continuing supporting previous major versions through compatibility shims.
you are the maintainers, obviously, you get to decide now how you want to approach this, but I just wanted to, I guess.
say that I would not mind if you consider this path for the future, where you iterate much faster, come up with newer versions, and are not afraid of breaking changes to the internal APIs, allowing you to evolve it Much faster, in more interesting ways.
Yeah. And I'm talking about internal APIs, right? Not the end-user observable, like, configuration, that's probably a different consideration. But internal APIs, I would love to see more innovation happening there.
Which is not held back by the need for compatibility.
Alex Boten 00:16:58 Yeah, I think. Thanks for saying that, Tigran. I think.
I think the… the current state of where we are, and, you know, if we look back at the last two years of trying to get to V1, this was, like, the second or third attempt at V1 that we've made, and I think the same, pattern that you were describing of being very careful with our releases is kind of what's been holding us back a little bit, and… And realistically, people are running the collector in production today, so for them, it's already stable. And so all we're doing is we're… that's right, all we're doing is we're calling a V0, a V1, and we're… tying all of our changes that we're making to, like, one major version, which is the V0, and we're calling it, like, a pre… preview one, but, like, it's really not that what it is today, so… I think that's that's the driver for the new RFC that we've published. We just want to like finally call this thing a V1 and allow us to move on to like the next version.
Tigran Najaryan (Splunk Inc.) 00:17:53 Yeah. Okay, cool. Thank you.
Pablo Baeyens 00:17:56 Yeah, I guess I'll add a third second comment, which is that unfortunately, the… I feel like the… feeling of users about the version of a component is a bit tied to the Go modules because of OCB. Like, the way we name a component, like, V1, that is also the… the Go API of the component is also versioned in that way. And so, I think, unfortunately, we have that Bernard's iPhone: dependency there, but we are trying to do things like, if.
particular Go module is… not part of the public API, of the component, then we do not need to mark that as V1 to have the component be V1.
That was a bit confusing, maybe, but yeah, we're trying to not mark everything as V1, just the things that we feel like we really need.
Tigran Najaryan (Splunk Inc.) 00:18:55 Okay.
Cool. Thank you, guys.
I know this is an enormous amount of work, so thank you for doing it.
Joshua MacDonald (Microsoft) 00:19:04 Yeah, so I thought I'd ask a question, maybe sort of a leading question, or opportunity to discuss. The question is about module compatibility as we go forward. It's one of the most challenging aspects of working in Go, as far as I can tell, is, managing breaking API changes as we change module versions, major versions, minor versions. It's, we at this point in time, I believe, are facing a quandary of not knowing how to add anything after we stabilize the first V1.
of some of our libraries, because they're the low-level libraries. We're talking about config HTP, config gRPC. These, are used by every component, basically, and if we stabilize them, now we're in a place where it's hard to experiment and evolve. Do you have any thoughts or comments?
Pablo Baeyens 00:20:00 I feel like we need to get comfortable with the fact that we're going to have some configuration fields that will be deprecated, and just be fine with that. We're going to make mistakes, and we need to just… that with that on prevent it to the extent possible, but I think we're already doing that to some extent.
Joshua MacDonald (Microsoft) 00:20:23 That sounds good. My… I mean, that was a leading question. I think that there are some techniques that we can use in Go that would give us the ability to carefully evolve, but it… there is also sort of, like, a no-going-back this problem, where once you've created an interface, like, it has to be there forever, or you will break it. And the only way to get off of it is to change to a new major version.
And this came up recently, for example, with… there was a request to add a new extension, which is, like, very, like, good rationale behind it, but that's, like, let's not slow down the V1 train by adding a new thing at the last minute.
That we don't know how to manage the compatibility of.
So there's still some sort of jitters here.
Okay.
Any more questions?
Okay, I can lead us now into another topic that's connected, and let me pull up my document.
Oh boy, where is my… where's my share button?
There it is.
Cool.
Okay.
I think I got the right window. Okay, so.
Pablo and Alex have referred to a, project.
Involving the batch processor.
One of our oldest, and so I'm… what I'm sharing here is a blog post that I have drafted. This is not an approved blog post, but this is something that we've been talking about doing for quite a while. So, if you.
We'll take a look at this, post. There's a link in the notes. You can see that… well, let me start with the background.
We made a plan. This is the RFC from the collector repo, and it says, basically, here are the problems that we found with the batch processor. It's a 6-year-old component at this point, actually 7. It came in with the original open census, and has been with us, probably stabilized, one of the first ones to stabilize. It looks like it hasn't really changed much in the basic form since 2021.
And so, the problems that we found with it, you know, I'm gonna switch back to the blog post, but the idea here is that, the, component itself lacked three major pro… there were three major problems here. So… so the initial one, the one that kind of, like, led the… the cause was about control over batch size. You want to set a limit. What's that limit in? Is that limit something you'd like a byte limit? Because that's where it gets hard. Right now, we have the batch processor.
It is a data-oriented processor, so it takes bytes, or it takes, sorry, it takes objects in, it does batching work, and it sends objects out. That's the model of the collector pipeline. We call it PDATA. So, you have these objects coming into the batch processor, objects going out.
And the problem is that it was difficult to set a limit in bytes. You could fake it by setting a limit in terms of the OTLP bytes encoding, but that's not what most exporters, at least at the time several years ago, most exporters weren't OTLP, and they were trying to set bytes in their own protocol. So, this led to a proposal, which has taken several years to complete.
The other sort of defects in the legacy batch processor that we all knew about several years ago.
have to do with concurrency, and the connection with the other queuing that's happening in the pipeline. So, the legacy batch processor was designed to be run as a processor, and then there was a queue queue functionality available in most exporters, but putting the batch processor before the queue made some problems. And it causes us to have to worry about concurrency, and something like back pressure, and error propagation. So the three other categories of… the two other categories of problem that we know about are concurrency control, back pressure, and error propagation, all of which were sort of, like, very brittle and not solved by the batch processor.
So these were the problems that we started with. And, I'm sort of showing you some of its legacy configuration. This is what an original batch processor would look like. If you just set the batch processor with its defaults, what you get is a 200 millisecond timeout and a 8,192 item limit.
minimum limit. So this is saying that I want you to put batches together for at least up to 200 milliseconds, and up to… sorry, at least 8,000 items. If you go above that, it's happy to let you send a bigger request. Now, if you want to put a limit in items, this is how you did it. You set send batch max size.
And so this would say you have two limits now. One is a minimum size for your batch, one is a maximum size for your batch, and the code is able to manipulate these requests until it has exactly that many items in it. Upper bounds and lower bounds. And so that's where we were. Six years ago, that was the batch processor.
So, aware of all these defects, and the user's requests were piling up, a new project began.
And so this was led by Bogdan and Dimitri. I don't know if Dimitri's on the call, but, I volunteered to kind of help clean this up, because I was one of the users who was very frustrated with batch processors several years ago. So, the new configuration, it's called QBatch.
and it exists as part of this library we call exporter helper.
QBatch combines the queuing and the batching, and this is pretty well justified. It takes a minute to understand that queuing and batching are pretty connected, because you have to imagine that there's going to be some memory sitting there, that's the stuff that's in your queue, and it's the pool over which you are batching.
The original configuration where you had a batch processor separate from the queue was a little confusing because you had two configurations, and their concurrency and their back pressure relationship was very unclear.
So in this new organization, we've combined everything. You put the queue first, and the batch processor second.
So, this is the combined configuration that you have now for these… this QBatch processor. And it control… it solves all the problems that I've mentioned. So, first, you have a concurrency control. That's how many exports are simultaneously allowed.
You also have a limit that's for the queue. How many items are allowed into my queue? And this controls how much data you're willing to accept.
While returning success to the user. Now, if you crash. and you're an ephemeral queue, you will lose some data. So this is the control over how much ephemeral data is there out of the box. You can add storage, we'll talk about that in a sec, but basically we're saying that this is the risk factor. If I crash, I'm going to lose this much data out of the box default.
So you set your queue, and you can set a sizer. So now we have the ability to say that my queue is limited in bytes, or my queue is limited in items.
Because we're in the exporter, we can now measure bytes in terms of the actual data, not in the protocol that we care about. So, saying that your queue is in, has a sizer of requests or bytes means that you're actually measuring what's sitting there in a queue, as opposed to You know, only counting items the way the original batch processor would do.
So then, two more very important controls which were added. The first one's called block on overflow, and this says that if you get to the queue and it's full, you have two choices. You can return a failure fast, like a retry after, or just, like, I'm overloaded. Something unavailable, retriable.
Or, you can wait for your context timeout. And not all receivers have context, but most do, and so this would allow you to say.
Slow yourself down when the queue is full, and that's really helpful for managing load in a system.
But connected with block on overflow is another behavior that some users want.
Which is wait for result. So this is saying, if you are in that ephemeral queue state, and you want to have a blocking back pressure full system, there's one more thing you might ask, which is, I want to wait for the response and know if it succeeded or failed. This is what we call error propagation. And the original batch processor made it impossible.
So… so the wait… wait for result is this, the new feature that we added. It's about a year and a half old now, and I would call this the point where the new batch… QBatch mechanism stabilized.
And this gives you the ability to, slow down and understand when failures are happening, so that you can push back and retry.
And this helps users not lose data.
Okay, so inside of the queue batch configuration is where the batch configuration sits. So this batch enabled… this batch and the enabled flag here are the option to enable batching over your queue. So in this mode, what the batcher is doing is pulling out of the queue whatever's sitting there until it can find a full request and then sending it. Again, limited by the number of consumers.
So this is what you would get. This is actually the out-of-the-box default. Actually, not the out-of-the-box default. Let me show the… defaults, I wrote them somewhere. So again, the original defaults from the batch process are carried over, so your default is items as your sizer, 8,192 items is the minimum size, and 200 milliseconds.
From… Okay, so I've now explained the basic queuing mechanism, this is… oh, I did not mean that. Okay, here we go. The queuing mechanism, includes num consumers, wait for over… block on overflow, wait for result, sizers, and limits, right, on the queue size. This is the batch configuration now. First, you have to enable it. It's not enabled by default.
And that's something I'm going to talk about. And then you have these sort of standard flags that look this… or configuration fields that look the same as the original batch processor. You have a minimum size, a maximum size, but now you have a sizer, and you can say that you want your limit set in bytes. So that's… that's what's new.
And this has been, again, kind of stable for about 18 months, so we're… now we're pushing to get it to be the standard and get rid of the old code.
If you turn on batching, you will get all the defaults, and that's some work that took a long time to settle in the collector codebase. We added this thing called config optional. It lets you have an enabled flag, and it manages the configuration to have a default when you're… even when you're disabled. So that… came first, and we got config optional to work. So if you turn on batching, you'll just get a bunch of defaults. That was one of the problems a couple years ago.
And now, I just want to mention that there are a few other pieces of functionality in here.
the, the persistent queues have been added, and so, because the queue already had that support, now what we're saying is that you can put your data into the queue. Instead of being ephemeral, you can give it a storage extension and write your data to disk.
Somewhere in this… document, I'm just kind of skipping through it. We added, the ability to do partitioning. Both the old batch processor and the new batch processor do this. So this is to say… to say that you have some metadata, some header values, for example, on your request, and you need to make sure that the batches retain that identity, so that you can have, say, an identifying token, like an access token of some sort, and say the batches will only be produced with the same value for that metadata. Both of these support that, so I didn't go into it in much detail.
The… so… so now you see the whole picture. You've got this Q… so, actually, I didn't tell you the whole picture. So the whole picture is that you're using your exporter now. We recommend you to use the exporter. It has QBatch built in. This field is called Sending Q. Most users are going to go that way.
We found that there were maybe 5% of users who would sort of flag this as an issue. I still need a processor, they would say, and we looked at why and found some valid reasons. So there is still a need for a batch processor, it's just not very common.
One of… some of the examples, and I need to add text on this, but we put it in the RFC, which is to say, like, if you're doing group by, like, you… there's a group by attribute, attribute processor in the collector contrib, it literally recommends you to use a batch processor, because it does better with bigger… with bigger inputs. So if you have a processor that wants bigger inputs, you want a batch processor ahead of it. And what we've done is take the new functionality that was built in the exporter, and apply it backwards to a new component. So this is the replacement processor. It is not a batch processor, because we're taking away the old configuration, and we're giving the new configuration. So here's a processor that does this QBatch functionality.
And the defaults are set to look like the old batch processor, so this can basically drop into the… anywhere you have the old batch processor, you could just drop this in, although what we're recommending is a migration to use the exporter helper batcher, if you can. Gives you more control over bytes limits and so on.
So, the processor is here if you need it. Some of the other scenarios we know about are if you have multiple exporters.
Having a consolidated batcher gives you a little bit of memory savings since you're not creating multiple copies of your export request. It works better if you're doing OTLP, you know, for example, but this is the type of support we have now. Now, last point here, and then I'll be done, is that we are intending to change the default. So as we turned on this or built this new functionality into the Q processor, now it's called QBatch.
We left it off by default, because it was going to create some confusion for users who have been programmed to use the batch processor for 7 years or whatever.
So, the plan is covered in detail in our migration document. It's basically saying that sometime in early 2027, we're going to switch to default. And right about this now is when we're going to do some preparatory work. So, this blog post will publish after it gets some review, assuming.
The plan says that next we're going to deprecate the batch processor. We've put in a few mitigations for the next few months that are going to help users.
We're going to update the documentation. And the mitigations are that we have a feature flag. You can try this out now to turn on batching by default.
We have a… a detection that's in flight hasn't merged yet, but the idea is that if you're in a simple configuration and you have two batchers and we can see it, we're going to warn you about it. And the last thing.
didn't get the link formatted here right, but we added support in this MDataGen tool, which is the collector tool that builds source code from metadata YAML.
The metadata… the mdatagen command will now have some support for opting in to a declarative mechanism. You can… every component will be able to declare their batch processor configuration, their QBatch configuration, and that'll become part of the documentation. So there are three choices. You can say, I'm taking the default, and if you take the default, it means you're declaring, I accept that my batch processor default will change, it becomes enabled in early 2027. So that default is going to change.
If you want to set an override now, users can just go ahead and enter the configuration they want. The defaults won't matter. But if you want to set an override.
If you're a component author who has very specific reasons not to want batching, and some do.
Then what you'll do is you'll go into your metadata YAML and declare, I have overrides, this is my batch processor configuration. And then what we're gonna do is just test that you honor your configuration, and that gives you the permission to use any starting configuration you want, and it will be documented. You just have to give a little bit of rationale.
There's one more case, which is like, I have no sending queue. There's a few special cases like that, where there's literally no batching or queuing available, and that's okay too, you just have to say it's omitted.
And that is the complete plan. I will now see if anyone has questions.
Thank you.
Tigran Najaryan (Splunk Inc.) 00:35:50 I'm curious about how the… Error back propagation works, but… Probably, I can… I can take that offline.
Joshua MacDonald (Microsoft) 00:35:59 Yeah, I mean, I can say briefly, it only works when you don't have a persistent queue. So if you choose the storage extension, then it disables the ability to do wait for result.
And then I did review the code, I could probably tell you how it works, but it's, you know, you gotta look at the code. There's… there's a sort of context-based weight that happens, there's… I think there's a channel, and so on, basically saying that if you're in memory, you have an ephemeral queue.
it knows how to wait so that the, the caller doesn't return until the error is available. And the error is broadcast to all the waiters who were part of that batch, and it just requires tracking who's in which batch. There are a few cases where you cross a batch boundary, and you end up having to wait for multiple Responses, and that's all integrated into the code.
Tigran Najaryan (Splunk Inc.) 00:36:42 I see, okay.
Joshua MacDonald (Microsoft) 00:36:43 Bogdan wrote all that. We should get him here to speak about it.
Tigran Najaryan (Splunk Inc.) 00:36:46 Okay, okay, thank you.
Joshua MacDonald (Microsoft) 00:36:50 Any more questions? I don't see any hands.
And then, if that's the case, we can move on. Thanks for listening, all. Let's see, then we have Jade to talk about something, which will be disabling… I can't see… disabling default resource attributes.
Is this about the detector issue? Jod, why don't you take over?
Jade Guiton 00:37:16 Yeah, it's not about resource vectors per se. It's not actually a presentation. It's more of a question.
Joshua MacDonald (Microsoft) 00:37:22 sure.
Jade Guiton 00:37:22 the spec SIG.
Should I? Yeah, you can open the the issue. But basically.
We recently added support in the collector for the declarative config in one more location, which is the configuration for setting the resource attributes used by the collector in its own internal telemetry.
The old format we had for resource attributes is what you see at the top here, where we just have resource and then keys and then string values.
And the new format is the declarative config with a list of name-value pairs.
And this works fine for the most part. One issue, however, is that the old syntax had a feature which is that if you set the value to null.
it disables whatever default value we would give to that attribute, because the collector supplies three attributes by default. Service name, service version, and service instance ID.
And so someone… rightfully posted a bug report that the new syntax does not allow you to do this.
Now… The question is, How should we allow this capacity in the collector?
Notably, the whole purpose of the exercise was to make sure that the collector fits with the SDK declarative config and its semantics.
But it's not clear how we can make that feature work with the the declarative config.
Notably, if we look in the configuration repo.
Null is an allowed value. But unlike what I initially assumed, I assumed it was about like empty type values.
It seems the null… the meaning of null here is that the entry is ignored.
Which… it's not clear if the entry is ignored allows for a behavior like disabling an attribute that was… that has a default value provided by the application.
So… we… I think there's essentially three possible correct behaviors here. The first one is that the collector kind of follows what it used to do, and says that null equals disable the attribute altogether, especially if it was initially provided.
Or we follow the, current behavior that's in the OTEL configuration repo. The entry is ignored, and we take that to mean that it's as if the entry wasn't there.
Which means there is no way to disable.
an existing attribute, then we have to find a collector-specific way to do that, which is fine, it just requires a bit more, it just requires, like, a second, different bit of syntax.
Or, we find some way within declarative config to do that. For instance, if we decide that An entry is ignored if the resolved value of an attribute ends up to be null, including overwrites to previous attributes.
Kind of a loophole to say that if you set null, it means disabled, even if there is something else providing that key.
And finally, I guess another possibility is that this declarative config syntax was made before complex attributes were invented, before the empty type was added to OTLP.
Which, in principle, is what null should be mapped to, so maybe that should be the correct behavior. That's kind of what I assumed at first, but it's not super useful, so I'm not going to push for that being the new behavior.
So yeah, I would like to… ask, I guess, the spec SIG what they think the correct behavior should be in OTELCONF, which implements the declarative config, because at the moment the behavior is not right, no matter what we choose.
And… Do we have a way… should we do our own thing in the collector, or can we piggyback off the declarative config for this?
Yes, Jack.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:41:47 Yeah, thanks for bringing this question. So.
What did I want to say about this? So… I think this is… this is something that needs to be clarified in the… in… the declarative config schema. This situation where you want to null out or erase, like, an attribute that is provided by default, it's actually kind of an edge case, because everything in declarative config is, like, there's, like, a what-you-see-is-what-you-get philosophy. There's no, like.
with only a few exceptions, there's nothing that, like, happens automatically. If you want an attribute, you need to write the attribute. If you want, like, a resource detector, you need to specify that that resource detector in your config.
There's very little automatic behavior, and these… the service name and service instance ID, and then the telemetry SDK names, telemetry SDK, those are some of the edge cases of, like, resource attributes that are, you know, that are available by default because of, you know, other spec language that sort of supersedes this what you see is what you get philosophy.
And, And yeah, you know, I think it's reasonable to want to null those out, or, you know, omit them. And, you know, this is a matter, in my opinion, of changing the description of the, of this type in the schema to just, you know, elaborate on what null means in this context. And, you know, I think I'm kind of with what I think you were suggesting, which is, like, if null is present, that's sort of, like, the interpretation I would, you know, go for is that it should erase any value that was provided elsewhere.
Lovely.
Jade Guiton 00:43:32 Alright, interesting.
Speaking of resource detectors, do you happen to know how… if there's any language in the declarative config that says how they interact?
like how the retail detect the attributes provided by retail detectors interact with the explicit list of attributes.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:43:50 Yes, there is a priority between them. The explicit list has priority over resource detectors.
Jade Guiton 00:43:59 That makes sense.
And I'm guessing that, yeah, so the behavior of null of can you disable an attribute from a result detector through the explicit list, I guess, yeah, this would also apply to that case.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:11 It would also apply to that case, but there's also a separate mechanism to filter attributes that are provided from resource detectors. So then I guess there's two mechanisms to erase attributes provided from detectors.
Jade Guiton 00:44:24 Hmm.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:25 That's no matter.
Jade Guiton 00:44:27 That's true.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:28 Got it.
Jade Guiton 00:44:29 I guess we could, like, consider the default attributes in the collector to be a resource detector, in a way.
And…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:36 They are in a way, but like, yeah, they really are sort of their own thing. They're provided at like a lower level than, you know, traditionally we think of resource detectors. Like, so yeah, they're kind of an enigma.
Jade Guiton 00:44:53 Yeah, that makes sense to me.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:44:59 Okay, yeah, so, if you, like, why don't we do this? Why don't we open an issue in the configuration repository, and we can follow up from there? I don't think this is, like, you know, should be incredibly controversial. I could be wrong, but it seems reasonable to me, and I review a lot of the PRs over there, so… Yeah.
Jade Guiton 00:45:18 All right, yeah, I'll do that. Thank you very much.
Joshua MacDonald (Microsoft) 00:45:21 All right. Thanks, Charlotte. Thanks, Jack.
And, let's see, Ted, looks like you have the topic up next.
Ted Young (Raintank, Inc. – Grafana Labs) 00:45:31 Yes!
So, this came out of the Packaging SIG SBOMs, software bill of materials. This is basically a manifest file explaining what you shipped.
It came up again because we're looking at Linux package management, and as part of building those things, you have an option for including an SBOM. This is becoming a bit of… Regulatory compliance.
Various different regulatory frameworks, especially in finance, starting to come out, that include these, so seems like a good time for us to figure out what our story should be.
This is something that the Security SIG thought about, but from pawing through their materials, it wasn't clear if they had gotten all the way to the point of… of, like, a clear, actionable checklist that all the SIGs could follow.
So if we've already got that, that would be great.
If there's still room for debate.
Seems like it would be a good time to get that cleared up.
So… Curious if people have any thoughts in a couple minutes we have here. Otherwise, please put your thoughts on that GitHub issue.
Reiley Yang (Microsoft Corporation) 00:46:56 Yeah, Ted, if you check the last link I put in this section, I have a PR. I think in that PR, we start to raise the bar, and we hope that all the SIGs can first list all the artifacts that they're shipping. Then for each artifact, we're going to require them to give the SBOM and maintain that.
So, I think before Ice Bomb, the question is, do we understand what artifacts are reshaping? And currently, I think the answer is we don't have a clear list.
Some SIGs don't have that, so I feel like… I suggest that we put more energy on the pull request, and try to get that merged and agreed with the maintainers. Then once we, like, for each SIG, we can list, these are the artifacts we ship.
Then, well, the next step is for each artifact, we can see whether we have the SBOM or not. And if the SBOM is being maintained in a standard format, or there might be a SIG-specific thing they want to do extra work for SBOM. I think there are multiple formats people can use. So we do have some recommendation, but I think the challenge is, let's list all the artifacts we ship first.
Does that make sense?
Ted Young (Raintank, Inc. – Grafana Labs) 00:48:12 Yeah, totally. I think it would be nice to go from, when I did look through the recommendations, it looked like optional, like, oh, there's this format, there's this other format. It would be great if we could turn it into, like, just an actionable checklist that everyone could follow consistently.
But glad to see that the security SIG's thinking about this.
Cool. That's all I got.
Joshua MacDonald (Microsoft) 00:48:40 Thanks, Ted. Yeah, so Alex put a link to the collectors SBOM artifacts are now being published. Looks like .NET is doing that as well. So the keyword here is SIGSTOR, as far as I understand. That's something we should be doing.
I definitely agree this is important.
Yep.
Reiley Yang (Microsoft Corporation) 00:48:58 Yeah, and another thing for Icebomb is, here, I think, Ted, you were more focusing on the packages that we release, so it could either be something like an SDK library, or it could be a collector binary.
But I think Icebomb is also required for other type of artifacts. For example, if OpenTelemetry.io is building a website.
then that website, like, when people use that, they want to… the website itself can have security issues. Like, I've seen a lot when people report, like, you don't have the right certificate, chain, or you have some, like, expired, like, root CA or something.
Or you might have a vulnerable thing. So for all the artifacts, I want to expand that, not just package.
Ted Young (Raintank, Inc. – Grafana Labs) 00:49:44 Hmm, that's good to know.
Reiley Yang (Microsoft Corporation) 00:49:45 And we have containers, we have other things, so for, like, whatever SBOM would apply to, I think we should list that you have this artifact, and then you need to have SBOM.
Ted Young (Raintank, Inc. – Grafana Labs) 00:49:57 Yeah, makes sense.
Thank you. Yeah, and the goal is regulatory compliance, just so people are clear.
No.
Jason Plumb 00:50:07 the.
Joshua MacDonald (Microsoft) 00:50:07 Yeah, so I think we're going to find that the companies who have more regulatory oversight are going to be more caring more about this. Certainly my employer does, and that's probably clear. So if you're interested in this, help us out.
Ted Young (Raintank, Inc. – Grafana Labs) 00:50:22 Yeah.
Give us your requirements, just so we know what they are.
Joshua MacDonald (Microsoft) 00:50:26 Right.
Cool. Okay, well, looks like… Jack wants to celebrate our new TC members. I could have done the same. Jack?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:50:35 Yeah, I have the next two topics, and the first one is, you know, I don't think we actually announced this anywhere except for via PRs in the community repo, but we have two new TC members that were added, I think, a week or two ago at this point, Alex Boten and Robert Paycheck, so congratulations to both of them. And, you know, I thought this was as good of a place as any to talk about it, because as TC members, they become maintainers of the spec repo, and this is the spec SIG. So, you know, I think next time we'll probably do a blog post or something like that, but, you know, by the time we realized that would have been appropriate, the ship had kind of sailed, or at least it was, you know, it was kind of late.
But yeah, welcome and congratulations to Alex and Robert.
So…
Joshua MacDonald (Microsoft) 00:51:23 Yeah. Welcome, and congratulations.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:27 Would anyone like to speak? Yeah. Anything you want to say, Robert or Alex?
Reiley Yang (Microsoft Corporation) 00:51:35 Worst thing in town for us.
Alex Boten 00:51:39 I don't have a song, but thank you.
Joshua MacDonald (Microsoft) 00:51:43 I guess carry on. Jack looks like the number 60 is standing out to me. Please tell us. Yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:48 Yeah, so, okay, so one of the things Alex was talking about as, you know, a new TC member is sort of, that we're both interested in revitalizing or continuing to vitalize this.
you know, what we're calling SIG heartbeats. So you've seen some of these before. Alex and Pablo gave one today about the collector and its V1. But the basic idea is that we want to hear from the other SIGs that comprise the OpenTelemetry community once in a while at the spec SIG. And you know that that can be a challenge, right? There's 60 distinct SIGs. It turns off spread across this. And so, like, you know, if every single one of them updates, we're only going to hear from them, like, you know, if we do one update a week, we're only going to hear from them less than once a year. So.
Yeah, you know, but still, we want to do this. We think it's important to hear from the various SIGs because of a couple of reasons. One, we want to promote this notion of the spec call as a synchronous hotel town square. We have asynchronous forms for this, but, you know, synchronous communication is good, it's fast, it's effective.
And we also want to keep the community in the loop of current activities in the SIGs and challenges of SIGs as well, right? So different communities are doing different processes, some of which have been successful. We want people to be able to attend the SIG, the spec call, hear what other SIGs are doing that might be working for them, and maybe bring some of those over to their own SIG for some cross-pollinization things.
And, you know, if there are challenges that are recurring across SIGs, we want to be able to do, like, pattern recognition against that, and just, like, you know, notice that, like, 3, 5 SIGs are experiencing the same issue, and try to make some sort of concerted effort to address it. So, yeah, the basic format of what we're proposing is a lightning talk format, where, you know, we go sequentially through all the SIGs, and we have the opportunity to change the order to whatever we feel is appropriate. And we don't make these updates too long. We think 5 minutes is sufficient as, like, the default.
And you can talk for longer if you have more to share or like a deeper dive that you want to go into. But we think a short five minute update on your SIG with a prompt that is something like I've included here in the notes. So like, what are the three most important things happening in your SIG?
what do you need from the community? Like, do you need, you know, more people to participate? Do you need anything from the GC or the TC? Do you need any, like, you know, help from other SIGs? Do we need any, like, kind of cross-SIG collaboration?
And then just like an open-ended thing, like what's one thing that your SIG does that nobody else does? So trying to do that cross-pollination thing.
Yeah, and, you know, we think that we want to do this, and we want to, like, learn as we go, and adjust as we go as well. So, you know, Alex and Pablo, thanks for giving an update this week. I'm volunteering to do next week's update. I'm going to give an update on the Java SIG, and, you know, I guess the… what you can expect other people on this call, and other people not on this call as well, is that, like, you know, the TC is going to do some curation around this, and some scheduling around this, and we might reach out to you to request volunteers as well, so look forward to that.
That's all I have to say.
All right.
Joshua MacDonald (Microsoft) 00:55:31 Here I am, yes. Any last remarks? We made it to the end, and there's a few minutes.
I love it when we make it to the end with time. So well done, everybody.
Josh Suereth (Google LLC) 00:55:44 Can I ask a question?
One quick question. So, who's next for… whatever we'll call it, Heartbeats. I keep wanting to call it a spotlight, but it's Heartbeat.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:55:54 I'm next. I'm gonna give an update on the Java SIG, and then we are going to try to… this is my proposal, we try to schedule it, like, 2-3 weeks out, always, so that there's, like, a queue coming up.
So, you know, we… I'm thinking put together a Google Sheet where we, like, have the confirmed schedule, and we track who's done it in the past, and, you know, that'll prompt us, you know, the spec maintainers, the TC members, to continue to do curation of this list as it comes up.
Joshua MacDonald (Microsoft) 00:56:25 The, notes doc for this meeting has a tab with that table that I'm showing you here, and so I just updated you for next week, Jack, and then if anybody wants to claim two weeks out, it looks like we have that spot available.
Or else we can move into November, but, yeah, think of if you want to present two weeks from now, and we could do that too.
Sweet.
Daniel Dyla (Dynatrace) 00:56:51 I.
Joshua MacDonald (Microsoft) 00:56:51 couple.
Daniel Dyla (Dynatrace) 00:56:52 Couple of, like, related questions, about, like, the process. Like, one, is this expected to be, like, the TC sponsor or spec sponsor for the SIG to give the call… the talk, or is it a maintainer, or can it be any?
2… there's 60 SIGs, I see 21 people here, likely only… half of the people here are even Maintainers. How do we get this… spread around to the other SIGs, and does it then become… mandatory for a maintainer from those SIGs to attend this meeting, if it's truly gonna be, like, the maintainer town hall.
Like, how… how aggressively do we want to Push this, because it says all SIGs in caps.
That makes me think that this is something we're trying to… Get more people here more regularly, and how aggressive do we want to be about that?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:57:50 Yeah, so I have thoughts, and I'm not too rigid in any of them, and so I think we need to learn and adjust, but I think it's really healthy to have a single meeting that, like, collects liaisons from all the different SIGs within the community. Like, my ideal vision of this meeting is that there is a maintainer-type persona or a lead-type persona of each SIG that, you know, attends the town square and can, you know, listen and bring information back to their respective SIG and bring feedback and perspective from their SIG back to the town square.
Like, I think that that'd be a really healthy place to be. And about 6 to 12 months ago, somewhere in that range, the SPAC was actually in a really bad place. Like, attendance was dwindling, it was down to, like, you know, 6 to 8 people, and, you know, we couldn't have effective discussions. And we've improved since then. You know, we regularly have 20 to 25 people, but I think we can do even better, and that's, like, kind of one of the goals of this, is to, like.
To create the, you know, a perception that, you know, you want to attend the spec call, that there's actually information that is useful for you to hear.
That, like, provides that incentive to you to… for you to go spend an hour a week making the effort to come and join this call.
As for who I think should give this update, I think it shouldn't be a GC or TC member, you know, unless, unless, like, that's, like, some sort of fallback. Ideally, it would be an approver or maintainer of this SIG, and, you know, it's an opportunity for them to get up in front of the community, and, and, you know, sort of grow, and, you know, public speak, all those things.
So, Yeah, like maybe promote the next set of potential TC members as well. So.
Those are my rough thoughts. Open to feedback.
Joshua MacDonald (Microsoft) 00:59:43 Inspiring, Jack. Thank you.
Yeah.
Daniel Dyla (Dynatrace) 00:59:46 That all makes sense to me.
Joshua MacDonald (Microsoft) 00:59:48 I was gonna say, if there are 60 SIGs and there are less than 50 weeks of meeting in a year, I wonder what the pace should be, actually.
It makes me think that we have too many SIGs, but that's a separate topic. And we are out of time, so I think we have to leave it just about there.
Reiley Yang (Microsoft Corporation) 01:00:08 Thanks, Harold.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:00:10 Otherwise, he's heard on this. Yeah, alright. Talk to you next time.
Joshua MacDonald (Microsoft) 01:00:13 Thanks.
