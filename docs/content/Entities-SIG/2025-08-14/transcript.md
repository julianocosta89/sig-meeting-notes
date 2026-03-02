SIG: Entities SIG
Date: 2025-08-14
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/G7No9cOOFhpeZlFFjk1vl2QMvaAOb8rwvduDSZVA3pnITH5JVvWlzJxD4GFPVY0f.HAlhne9sumMS_mRp
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:24 Hey, can you hear me?
This is working.
**Dmitrii Anoshin** 01:26 Hello, I can hear you.
**Josh Suereth** 01:28 Okay.
Cool.
Right.
Oh, failed.
Yup.
So, feel free to open or add status here.
Okay. Cool.
So… I'm gonna add, … one more topic.
Okay, can we… is my screen visible?
**Dmitrii Anoshin** 02:44 Yes.
**Josh Suereth** 02:45 Cool.
Alright, so I have two things to update, and I was just going through our project to see if there's anything else to add. First off, and…
I might wait till, possibly Ted or Daniel are here, but API updates… I finished the delayed startup prototype for Java.
So, the basic gist of this is there is a, … You know, entity detector.
…
That basically has a, what do they call it, completable… Result code…
This is the kin of future, and it says detect, and then you get a, entity provider.
Something like this.
So it kinda looks like that.
And then, when you construct an SDK, when you construct the entity provider, you register these things.
So, we'll say something like Entity Provider.
This is Java code, so apologies, turn this into the equivalent in your language. Builder. You know, set…
… initial… Detectors, dot dot dot, that's set, … Initialization timeout.
Boom. Okay.
So, basically what the prototype does, and I got it working, …
when you create a new entity builder in the SDK, you set the set of initial detectors that need to run, you set an initialization timeout, you build. If the, … when the initialization timeout is done, it basically forces the resource through.
At that point in time.
So, whatever, the… Yeah.
There's a thing that sits and listens to the SDK provider.
and it waits for the timeout, and it will block export calls until the timeout's done, basically, using, like, thread primitives. So it'll actually block waiting for the resource to be available before it allows things to go through.
However, we also have, and I think we could do this…
I could actually do this so that we don't need to block in Java, but that's a different story. We set initial detectors, and we set the initial institution timeout on the provider. So the way the entity provider works is it goes and kicks off these threads to say, go detect resources, right?
It doesn't necessarily kick off a thread, it assumes that if you're… if you need to do something threaded, you will do so yourself.
But you… you give it a promise, if you will, or a future, if you're familiar with async08. In OpenTelemetry Java, that thing is called completable result code. So this is basically saying, hey, go detect things. If you're asynchronous, just tell us when you're done with this async future.
We will wait up to n, you know, milliseconds, which I think the default I had was something like 20 or 200, and when that set of milliseconds is done.
Even if the entities aren't done.
We force-initialize the entity provider and continue on.
So, force initialized means whatever entities have been discovered by that point, that's your set for the initial resource. You get a resource initialized event.
…
I can show you the code. I didn't have a chance to update the code, because I, it's been kind of a crazy two weeks for me. Sorry, to push the code into GitHub.
I'm just describing how it works. But, feasibly, this worked…
it's a little bit gunky, or how do I want to phrase it? Like, I…
I think people will only implement it correctly by paying attention or copy-pasting.
Similar to some of the initial metric SDK work.
So, but it does… It does work. I think it's viable. I don't think it adds, …
More complexity than is necessary, given what we're trying to do.
… But yeah, so I'm confident that we could go forward with this.
design.
And it, it can work.
Daniel, you came in late. Tldr, I got the prototype working where…
Entity provider, you set an initialization timeout, you set detectors. This is the Java equivalent of a promise, if you will.
So a detector says, takes in an entity provider, runs detection, and returns a promise when it's done. Completable result code is a promise of a success or failure message.
**Daniel Dyla (Dynatrace)** 07:50 Okay.
**Josh Suereth** 07:52 And so, what we have then is on the provider, when you say build, it will create the provider and return it, so you can immediately start using it.
But the initialization event, right? We have 3 events that fire. We have initialization, we have resource change, and we have resource or entity deleted.
Okay? …
The initialization event will not fire until that timeout is done, or all of those completable result codes are done.
So, in my test code, that's immediately. I need to expand some test code with some delays to make sure that this all works with the delays and things, but, yeah. Anyway, so that's, that's the gist of that.
If you add a listener later, you immediately get an initialization message with the current state of the resource, and then you're given a, …
Update events as they occur, right?
I also created a container that I use for the rest of the SDK, where basically the container is something like, … what did I call it? …
There is a class… Latest resource supplier, right? Which, I guess it implements.
entity listener…
And in Java, we don't have functions and things, so we are suppliers of resource. And then this just has git resource on it, right?
And that Git resource is… this is, ThreadSafe.
And what I do is I pass an instance of this into all the other SDK components, so they're actually listening to events. That instance is what's responsible for blocking that component from exporting until initialization is done. It also has a timeout.
So the way this thing works, to keep things safe, when, if the timeout is reached on this thing, independently of entity detector, a default resource is returned. The default being, like, service unknown, or whatever, whatever the default was before.
Otherwise it waits for the resource event. Now, theoretically, that should not happen because of the entity provider having a timeout that will force initialization to come out the door.
right, of whatever entities have been reported. We should not have an issue where this one came in, but I actually had to cover both, you know, it's concurrency, it's asynchronous, it's L. I had to cover both timeout problems of… there's the timeout on the initialization for the entity provider of when to send initialization signals.
on the other side, I didn't want to just hard block, right? Because I think that… that would be hugely problematic. So the SDK is not blocked.
Right.
Now… I feel like this is rather complex.
But it works! And I think we could do this in JavaScript, I think we could do this in Go.
**Daniel Dyla (Dynatrace)** 10:57 It's definitely implementable in JavaScript. I guess the only… like, API…
interface is the actual… is the entity provider interface, right? Or the…
Yeah, and then the rest of this is all… SDK… Concerns? Even the…
Each individual entity detector, I guess, is even….
**Josh Suereth** 11:22 That… that's an SDK concern. I think we could… we could make… what I… what I'm not sure of, and this is where I was trying to divorce API SDK split for Entity Detector. I was trying to make that extension be something more stable than the SDK.
So I was hoping we could have, like, a registry of that, but I think this gets into the config, folks, and talking to config. I can show this if…
The important thing for those entity detectors is how are users going to interact with them? And if we look at…
spec… Hold on.
Configuration… If we look at declarative configuration and the data model, I believe…
Is this where we talk about it? No, that's the key value stuff.
It might be in the SDK that this is called out.
Supported SDK extension plugins… yeah, resource detector is supposed to be a supported extension plugin.
Right? And so the only, the only way that resource detector works now links to resource detection.
Come on, go back.
The way that that works now, if I recall correctly, for resource detector is, they are saying that there is such a thing as a resource detector.
And then somewhere in here, it defines, like, 4 different resources that you can use.
Where was that?
Might not be in this file. I just… I remember the PR, but I don't remember where it landed. …
Anyway, so in terms of SDK extensions, there is this notion of a resource detector, …
That is an SDKey plugin interface.
And that SDK plugin interface is something that would be, …
Configured by name, so you'd have a list in the configuration.
So, I think that's okay and acceptable. What I kind of wanted was for, …
that interface would be incredibly stable, so even if we refactor the SDK,
we could reuse that interface. I don't know if that's actually practical, though, given the…
prototype I've been doing, right? I… effectively, I haven't been able to find a way to have Entity Detector be
a piece of instrumentation, purely. It has to interact with the SDK in some fashion.
**Daniel Dyla (Dynatrace)** 14:07 Yeah, the… this, like, configuring by name… is somewhat problematic in JavaScript.
…
because we either have to build in a set of, like, blessed resource detectors or entity detectors into the SDK,
that are bundled with it and deployed with it, or the end user has to have some code that tells the SDK that they exist to begin with, in which case, like, configuring them by…
Yeah, a config file.
has… not no value, but a lot of the value's diminished. It's kind of annoying to have to…
you know, have some set of code that… that sets up, here's all the resource detectors that I'm going to configure, and then configure them somewhere else. Yeah. We have the same problems with every…
extension point in JS. It's my understanding that in… You know, some languages, like Java, just…
literally having them as a dependency is good enough. They can be found. ….
**Josh Suereth** 15:14 It depends on your security model, but most people don't lock it down that way, so yes.
**Daniel Dyla (Dynatrace)** 15:19 Yeah. We can't really do that.
So, because…
I mean, you probably would have been able to, like, 5 years ago, because you would have just dynamically required it, but now that ESM…
Requires everything to be static, it's a lot harder.
Not impossible, necessarily. We could get it done if we need to, but that's… that's kind of a problem in JS. None of the API that you pointed out in your, that you were just pseudocoding there is a problem for us.
I guess the detect method…
Is just returning, like, success fail, and it's actually calling methods on the entity provider.
**Josh Suereth** 15:59 Yeah, the way I would write this in vanilla, like, not OpenTelemetry Java would be something like future, success.
Right.
**Daniel Dyla (Dynatrace)** 16:09 Oh, yeah.
**Josh Suereth** 16:10 JavaScript and TypeScript would be promise of success.
**Daniel Dyla (Dynatrace)** 16:13 Yeah, exactly.
**Josh Suereth** 16:14 Or success… status code, I guess, is actually… it's result code.
Is technically what it is.
Yep. Where result code is an enum of success and failure.
**Daniel Dyla (Dynatrace)** 16:24 Yeah, and if it's a failure, you just log it and move on, I guess. There's not a lot you can do.
**Josh Suereth** 16:29 Yeah, yeah, I actually, oh yeah, that's right, catastrophic logs.
Catastrophic failure. Logging.
…
Basically, the thing that the prototype still needs, it all works, right? But we need to figure out what a decent default timeout is.
how to deal with catastrophic failures. Like, I think we just need to go through and look at, okay, what are all the ways this can fail, and what's the right way to fail? I am trying to fail open as often as possible, meaning if this all fails.
We need a way for the user to understand it failed, and at least get them some kind of information about what's going on, because zero visibility is 10 times worse than poor visibility.
**Daniel Dyla (Dynatrace)** 17:17 Yep.
it all seems fairly reasonable to me. I'm a little bit… the supplier thing, I think I'm a little fuzzy on.
I'll go through the code when you get it onto GitHub, though, it's… it's probably.
**Josh Suereth** 17:31 Yes.
You can… so there's basically an atomic reference.
Which is… which is our, like, atomic pointer, right, of a resource.
So it's private, right?
Atomic Reference Resource… equals blah blah blah blah, getResource basically returns… resource.get.
here, so you have a thread-safe way of getting the current resource, except there's, …
With tons of magic to block on initialization.
Right? Which I can… I can show you what that code is. It'll look different in different languages, because it depends what concurrency primitives are allowed, whether or not you can block.
whether or not await works. It's… that's gonna be fun to rewrite in different languages. I actually… and I'm not joking, I actually am excited to write that in different languages, because I love concurrency.
But I also know that if I'm enjoying the code, it probably shouldn't be written.
Yeah. Anyway, okay, so, yeah, the resource, that's basically what that does, and then we have, like, you know, void on, resource init, we get a resource, and we just say resource.setResourceR,
…
I'll say set are. I actually use lazy set, and I can tell you why in Java. The answer is…
Java's… memory model.
was entirely to… safe, to some extent. So, …
Yeah, if you're curious about CPU caching and concurrency, if you call set on an atomic reference in Java, it will force a memory flush and memory barrier right there when you call set.
Okay? Which, effectively, when you call git, will happen on the other side anyway.
So if you call lazy set.
you don't force a memory barrier, it actually just puts it on the CPU queue to happen at some point, and then you just continue on processing.
And the first time someone says get with a memory concurrency primitive, then all your caches are flushed, and the data will be sent to you. So, like, 9 times out of 10, you actually want lazy set instead of set for performance reasons.
But if you read the docs, they say use set, not lazy set, and that's been a source of contention between me and some of the
other Java people.
So, anyway, TLDR, always test, and always, benchmark.
Which is the next step here. Alright, cool. So for next steps for this, catastrophic failure.
What do we want to do on catastrophic failure? Just log?
… the decisions I made in the prototype were, there's a default resource that will go out, no matter what.
Right, so if all this timing stuff takes too long and it's not there, we'll still allow data to go through after a certain timeout, it just won't have all the attributes, and that's fine.
We send out with some default, like, we don't know what the resource is.
**Daniel Dyla (Dynatrace)** 20:53 Yeah, you have the service name, and…
instance ID that's just a UUID and essentially nothing else. I guess the SDK info.
**Josh Suereth** 21:02 Yeah.
**Daniel Dyla (Dynatrace)** 21:04 Yeah, I mean, that's what happens now if you don't set anything, so it seems reasonable.
**Josh Suereth** 21:09 Okay, and then the default timeout, what… I was just gonna match whatever Node.js has initially. What are you sitting at right now?
**Daniel Dyla (Dynatrace)** 21:17 Might be a second, it might be less than that.
**Josh Suereth** 21:22 Okay.
**Daniel Dyla (Dynatrace)** 21:27 I… I can't.
**Josh Suereth** 21:28 Think of it off the top of my head, but….
**Daniel Dyla (Dynatrace)** 21:30 I'll… I'll look real quick.
**Josh Suereth** 21:33 I think if we specify this, that's going to be a recommendation, not a requirement.
Because my guess is different environments might have different, sensitivity to timeouts.
Alright, we only have 8 minutes left, and I want to move on. Are there any overall major concerns, with the prototype and the API status so far?
Okay.
… Let's go on to the next topic, the n variable stuff that, Dimitri, you were working on.
… I… I want to ask whether we should put together
This was in our OTEP, but I don't think enough people read it, and we had some discussions on the PR, and I think we have to change where the PR is, we talked about that last time.
The question I wanted to ask this time is, should we put together either an OTEP or some sort of paper
About pushing identity versus pulling identity.
Right? So the idea that there is some system that will push identity down
To the workload in an environment variable, and we want to interact with that, like the operator.
**Dmitrii Anoshin** 22:49 Right? Where the operator will push identity via n variable.
**Josh Suereth** 22:52 And we interact. And that we need, you know, right now.
all of our resource detection pulls, so it makes API calls, it goes external. But actually, we should allow push identity as well.
So it can push down into n variable. I think that's the key thing that I have to continually argue with people, that I want written down somewhere people read.
**Dmitrii Anoshin** 23:15 Probably OTEP specific about just, like, The concept of, …
Providing identity, providing entity, whether it's push and pull, to describe both how they're different and…
I mean, just, like, general idea and, like.
mechanics, around pushing as well.
Because my point here is that maybe describing environmental variables and just push an identity as one attempt is maybe too niche.
**Josh Suereth** 23:58 Oh, yeah, I think… well, and we already have an OTEP that says we'll push identity with end variables. Like, we already have an OTEP for your… that describes exactly what you're proposing.
**Dmitrii Anoshin** 24:10 Mmm.
**Josh Suereth** 24:10 That was agreed to, right? As, like, there will be a way to push entity via environment variable.
what… what I'm afraid… like, what I want to do, though, is make sure that people understand that rationale somewhere, that it hangs somewhere, that it's described, that it's more advertised.
Because I think if you read that OTEP, or I think people haven't read that OTEP, because it has a thousand things in it.
**Dmitrii Anoshin** 24:33 Right.
So do you think that that needs to be another attempt for that?
**Josh Suereth** 24:39 Maybe…
I don't know, yeah, I… OTEPs are heavyweight, so that's why I'm trying to… I'm asking, what do we feel like we need to do here?
**Dmitrii Anoshin** 24:48 Yeah, I would say just expanding on how we push identity doesn't justify having a specific hotel for that, but if it's some generalized way that would describe, in general, how we
D, like… Let's say, provide identities.
Like, to, to… M… a meeting.
like, entity?
**Josh Suereth** 25:18 Yeah.
**Dmitrii Anoshin** 25:19 Maybe that one would be… I mean, that would be just an extension over Europe, but that's not…
too specific, I would say. But I don't know, that's my opinion. If you think that's not much to be written for data type, I would say we can just keep the existing document, or, like, maybe expand it a bit, not only about, like.
specific rules that we apply for the N variables, but also would provide some description why is that needed?
**Josh Suereth** 25:51 Yeah, well, that's why, if we go to your PR here, right, we have basically specified entity information via environment variable.
And so this is, this is where I think,
the justification for why we need this did not… it's in the OTEP, but it didn't make it to the spec.
So I guess, should we… should we create that somewhere, and where would that somewhere be?
Yeah, my thinking right now was either we need another OTEP to socialize it, which I kind of don't want to do, because I feel like we've already had this approved, and it's not contentious when people understand what we're trying to do.
it's only contentious when they think we're trying to make configuration, which we're not. So, that's why I think somewhere in here…
would make sense. Either in the README, where we can talk about, like, you know, we can give a better overview of entities, and talk about, you know, this involves resource identity, and here's the ways to, like, pass identity down.
You know, there's using detectors to go reach out and look up identity, or we provide an environment variable way to push identity into processes.
**Dmitrii Anoshin** 27:10 Would you….
**Josh Suereth** 27:11 Get the identity into the environment variable. It will pick it up that way.
**Dmitrii Anoshin** 27:16 I see, yeah, that's what we agreed last time. I just haven't done the changes, because I saw some discussions in the spec that I wasn't able to participate, so I wanted to check with you, because those discussions all about environmental variable versus config.
And, is that still relevant?
Or, like, we just….
**Josh Suereth** 27:40 just proceed.
Yeah, it's relevant in the sense of, if you think that what we're doing is configuration.
Then what we're doing is on hiatus, where it shouldn't do it.
But what we're doing is not configuration, what we're doing is actually, like, like, pushing identity to something via n channel. So it's almost like the, trace context propagation over end variable.
See, I… and, you know, Identity via N variable, yeah.
**Dmitrii Anoshin** 28:09 Okay, I just want to confirm that it's still the path we're taking, because after all this discussion that I wasn't part of in this pack, it may be changed somehow, you haven't, … we didn't have a chance to think about it, and you… that's why I….
**Josh Suereth** 28:28 The only discussion that I think we need to address over time is, like, right now, for that same use case, folks are using the hotel resource attribute and variable.
Which isn't necessarily configuration, right? And so, will config interact with that appropriately? It kind of has to.
Otherwise, they're completely broken. I think we're giving them an alternative where config and env will work together for pushing identity. So I think that's… that's the only thing we need to, like, continue to… to discuss and show, is, like, how… how will this interact with OTL resource? Like, what should the operator build and implement in the future, for example?
**Dmitrii Anoshin** 29:07 So we still want to potentially have a configuration-based approach as well, in addition to this.
**Josh Suereth** 29:15 Yeah.
**Dmitrii Anoshin** 29:16 Okay, sounds good.
**Josh Suereth** 29:17 Yep.
**Dmitrii Anoshin** 29:18 Sounds good to me. I'll proceed with this in that case.
**Josh Suereth** 29:24 Cool.
Alright, and then, I don't think anyone else added a topic, but I was just gonna go to the…
Project triage. Quick.
To make sure we're making some progress. For context, one thing I wanted to add that the GC is doing… we're out of time, so we'll take 2 seconds for this. The GC has added a new project board that will track status and timelines for things.
And so, these projects become more and more important. So, what we're gonna be able to do is we're gonna be able to update whether we're on track, delayed, deferred. We're gonna have a target date of when we think we're gonna hit milestones.
And this will be the central source of truth for us to track it. We just add details and information here, and there'll be an overall OpenTelemetry status tracker timeline with deliverables, and we will show up there from this.
Project Court.
So, right now, I think on track, actually, it should be…
probably at risk, just because we're redoing the API. The timeline we have is that this resource entity mapping
like, Phase 1 specification work would be, you know, release candidate worthy by the end of this year, which is in 6 months.
So, given, like, redoing the API and stuff, I'm not sure.
But, it… if we can…
My hope is we can get this stuff all cleared out, look at how fast these things move through for progress, and use that to do better estimates. …
Yeah.
But given that, I think we need a full OTEP for the entity API specification, …
I'm a bit nervous, because the first one took us months to get that approved.
So, timeline-wise, I'm not sure how we can finish a specification and prototypes and implementations and languages if we're not starting right now.
Right.
So I think we probably need to change this to not be on track, or create a different target date for when we think we're gonna have stuff out the door.
Any thoughts or concerns there?
**Daniel Dyla (Dynatrace)** 31:42 I mean…
I… I think it's not unreasonable to think it… we might be on track. You know, I don't know, maybe at-risk is correct, but, …
I think 6 months seems reasonable, to be honest.
I don't think… you know, the OTEP process is always what takes a really long time. But…
I think the initial, like, data model
settled a lot of the questions, and follow-up OTEPs should be faster, I would hope.
**Josh Suereth** 32:17 Okay.
**Daniel Dyla (Dynatrace)** 32:18 Who knows?
**Josh Suereth** 32:19 when you see the concurrency of this prototype, I do expect a lot of pushback from maintainers, which is why, I do… I think we could write the OTEP for the entity API,
today. Like, I think given the discussion we just had on failures and the state of the prototype, we could probably write that OTEP in draft form. So maybe I'll get on that and try to have that ready quickly.
But I think we need a prototype in Go, for sure. Javascript, I think we're confident we can build that prototype, that's not a problem. I do think we need to do Go, and see what that looks like before…
I'd be confident we get through quickly.
**Daniel Dyla (Dynatrace)** 33:00 Yeah, I mean, the lack of concurrency in JS is a challenge sometimes, but it, you know, for things like this, it's kind of a benefit that there's a lot of, like, thread safety concerns and stuff like that that just… I mean, I won't say they necessarily 100% go away, but it's a lot easier in a lot of cases.
**Josh Suereth** 33:20 Yeah.
But then you don't get to write any of the fun code.
Yeah.
**Daniel Dyla (Dynatrace)** 33:25 Yeah.
Oh, no.
**Josh Suereth** 33:27 When are you trying to optimize for a single, you know, CPU execution cycle to look at lock? That's the fun stuff.
Anyway….
**Daniel Dyla (Dynatrace)** 33:36 In JavaScript.
**Josh Suereth** 33:37 In JavaScript, yeah, exactly.
**Daniel Dyla (Dynatrace)** 33:39 Yeah. Exactly.
Alright, I… we're over time, and I have to go to the other SIG.
**Josh Suereth** 33:46 Cool. I think we can probably call it here too, so thank you, but I think all of the in-progress stuff is still in progress. Dimitri, is there anything you have updates for here?
**Dmitrii Anoshin** 33:59 Not yet, not at this point, yeah.
**Josh Suereth** 34:01 Yeah, that's, that's what I thought, so… …
Yeah, Daniel, this one… or, we'll ask Daniel later. This one, I think…
We have a state forward here, but the…
Complex attributes and resource actually did hit, so we'll have to make sure we make some progress on that as well.
Cool. Does anyone have time to pick up anything else, would be my last question, and then we'll call it.
Nope. Okay.
Alright, see y'all next week.
