SIG: Specification SIG
Date: 2025-09-02
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:12 Hi, Roddy.
**Reiley Yang** 01:13 Well, I'm gonna…
**Liudmila Molkova** 01:16 It's quiet here.
**Reiley Yang** 01:19 I think a lot of folks just came back from vacation.
**Liudmila Molkova** 01:24 Right.
Hi, Dan.
**Daniel Dyla (Dynatrace)** 01:29 Hello.
**Robert Pająk** 01:32 I will connect you to me?
**Reiley Yang** 01:34 Yeah, I can, go over.
Nice to meet you.
**Robert Pająk** 01:37 Hello?
**Trask Stalnaker** 01:47 Hello, hello.
**Reiley Yang** 02:05 Give, one minute for folks to join.
**Robert Pająk** 02:13 Is it better now, or worse? Just checking different microphones?
**Reiley Yang** 02:20 It's working, I can hear you, the audio quality is not great, though.
**Robert Pająk** 02:24 So this is worse quality, or the previous one better?
**Reiley Yang** 02:30 I think slightly better.
**Robert Pająk** 02:32 This one? Okay.
**Reiley Yang** 02:46 Okay, let's start.
Welcome, everyone. So, we have a list of topics. I think, Dobert, you go first.
**Robert Pająk** 02:55 Do you want me to share? Maybe it'll be easier? I… no, I already shared, so… Okay.
**Reiley Yang** 03:01 I can click the links.
**Robert Pająk** 03:03 Okay, so the first one is, I think we started last week?
It's about, preparing a changelog for the upcoming, OpenTelemetry portal release.
So, if you open it, it has been opened for a few days, so it just may be a last call or anyone, making sure that everything in the release which was supposed to be included is included, and also double-checking the changeable countries, and asking someone from the DC to merge it, probably even today. I think the plan was even considering merging it sooner, but I think we can do it, yeah, today, in a few hours.
**Tigran Najaryan** 03:42 I think we have enough approvals, Robert, no need to wait for any more, I'm gonna merge it now.
**Robert Pająk** 03:47 Okay.
Thanks.
**Reiley Yang** 03:52 Yeah, I'll handle the release.
So I'm moving to the next one.
**Robert Pająk** 03:57 So, next one, once the release… I have put the wrong hyperlink, probably. Probably is my fault. I may have made… if you go to the pull request.
I think it's my error. I think I… Change the text, but…
**Reiley Yang** 04:14 month.
So you want… you want to go to the… the PR segment?
**Robert Pająk** 04:19 07, yeah, yeah, just change the hyperlink, probably, I… Probably is my… Let me see… So, this one is basically blocked on the release, because you want to have first the release. So, basically, it's about removing the attribute values restriction. So, basically, it's about extending the attribute types, which we have been discussed Or a few months. So this is basically to make sure that, So this is the part of the proto.
to notify the, like, open to the OTLP consumers that they should expect that extended attributes are an acceptable, basically, payload. So, this is only for the proto part, this is not the specification API in the SDK. This will come later, and this is also the next points in the… today's agenda.
There have been some questions regarding profiling.
There were similar questions before in the OTEP, like, do you need to extend these attributes for profiles? These are the same questions as for metrics, which we had previously for metrics. Basically, it's about having consistency, it's about having the same, using the same APIs, the same code.
for any attributes in the collector, in the SDKs, etc. And I think I answered the conversation below.
But yeah, if there's any concerns, I just wanted to call it out here. But I think that even in the profiling SIG, there… there is a pre-acceptance towards… towards it.
But if I'm wrong, then… then yeah, I'm here, or we can… we can talk about it later. It doesn't need to be merged soon.
Josh, I think you want to say something, assuming you opened your camera up, but maybe I'm wrong.
**Josh Suereth** 06:23 No, that was… I didn't realize my camera was off. That's it, sorry.
**Robert Pająk** 06:27 Okay, yeah, so that's it. Any questions?
Okay, let's go further then.
So yeah, the next one here… So, I tried to basically create a PR, it's a draft, because Trask is also trying to first make a first validation, but since one week has passed, maybe I think that maybe there are more volunteers to make a quick look at it. Basically.
This is how I think the specification could look like when the extended attributes are being stable. So, this is, like, not the intermediate, this is, like, the end goal, how I personally see that the specification can look like. So, basically, it's about changing the definition of the extended attributes from the log data model, and moving it to the, to the common attributes model, and also making sure that it doesn't have any breaking change, meaning that the existing, for example, attribute arrays of primitis values are still kept, which was not explicitly, for example, described in the logs attributes, so yeah, that's basically it. It's a pretty big PR, but it's mostly, like, moving it's mostly restructuring, or sometimes rewarding things, or just using different words, different structure, but it's mostly moving things around. I also added one proposal how attribute limits could be handled.
based on the initial proposal from Udomoa, but yeah, this is just a draft, maybe also for, kind of, for more conversation, and the purpose of this PR is, one, to just have some basically, I think it will be easier for people when we just have smaller PRs, how it fits in the just larger end goal. The second reason is that this PR can be used for, for Languages want to validate future changes.
So, that may not… may be needed for the, OpenTelemetry APIs. The third reason is that it can be used for the OpenTelemetry I.O. blog post, to just share with the community where you are going, where you are going.
Yeah, that's all from my side. Any questions or concerns, remarks?
**Reiley Yang** 09:18 Do you expect people to review and put comments on the draft PR?
**Robert Pająk** 09:23 So I made it as a draft, because, it's not… I do not feel it's really ready, but if anyone from the TC has already some time, and just you want to volunteer, I think a few people can take a look.
I just think that it would be good if at least two, for example, two people will take a look, but no more than that, probably.
Just to have some, you know, pre-review.
**Reiley Yang** 09:52 Okay, thank you.
Any questions?
**Robert Pająk** 09:59 No, that's all from my side. I'm happy that I made it in 10 minutes. Thank you.
**Reiley Yang** 10:03 Okay.
Then, moving to Josh.
**Josh Suereth** 10:09 Yeah, so two things. First, the entity end variable. I just wanted to put some context on this PR. It has approvals, but there's still, I think, one comment, the plan is to resolve before it's there.
And that's from Daniel, and I just updated it today. But basically, what I want to call out with this PR, this is specifying environment variables where platforms can provide entities Or resource attributes, if you will, that are mergeable.
And then this has to interact with the SDK in some fashion. The key thing about this PR that we talked about in comments, and you can look through Resolve comments to see that, is there's pieces of the specification for entities missing, because we haven't written them yet.
And this is step one. So, this PR will be deferring to parts of the specifications don't exist. One of them is going to be this environment variable resource detector.
That this thing is designed to interact with. And so, rather than trying to fully specify, like, the pieces of the SDK that are absolutely needed for the environment variable.
The plan is, from the entity Sig discussion, to just reference pieces of the spec that don't exist. This is still in development, this is still, like, us creating our spec to begin with.
And I just want to give people that context as they review it, just so we don't have that question get asked again and answered again. If you need… if you need, like, rationale and understanding, look through the comments between, I think, both Carlos and Lyudmila.
And, Dimitri, you can see that, that thread there. So this is, like, kind of a, hey, what's the status of this? It does have enough approvals to merge, there's one change we're gonna make, and It… it… if you look at the entity's spec.
You will notice it reference things that don't exist yet, they're coming. Like, just, you know, we're building as we go.
**Reiley Yang** 12:00 Thanks, Josh.
Dan, is there something you want to add? Or the comment is self-contained?
**Daniel Dyla (Dynatrace)** 12:06 No, the comment itself is fine. I haven't seen it since the update because I've been on vacation, but I will re-review it this afternoon.
**Josh Suereth** 12:16 I don't know if Dimitri updated it yet, Daniel. If you scroll down, you can see I come… there's a comment from me, specifically with the wording that has to change.
So this, this, I think, has to change before this gets merged. We talked about this in the entity SIG, and we agreed, but this is where, instead of trying to reference things that exist in the spec, we're going to reference something that doesn't exist yet.
**Reiley Yang** 12:46 Okay, any questions?
Okay, we'll move on to the next topic.
**Josh Suereth** 13:01 Wiki-style red links, yes. So this, this is, another topic. I just pushed a few changes to this, honestly, like, right before the meeting, but we're reviving the entity provider OTEP as part of the entity spec. So, for context.
And to remind everyone, we wanted to make an SDK change for entities around resource detection.
And as we're working through it, we know that the client-side SIG and the browser SIG want to be able to update resources on the fly.
Meaning, like, resource and SDK lifetimes do not align.
They're not the same.
So we're working on an OTEP around what that looks like, and we realized the SDK that we were providing is kind of tangled up in this API right now.
So we're trying to make sure that we have a clear definition of what we're going with going forward. We've… all the entity SDK prototypes have been updated to work with an API, and we're kind of building this out now. So this… this has been changed, and I think there's two interesting pieces to it for everyone to take a look at.
There's a bunch of old, stale comments that I didn't have a chance to mark as resolved, but if you look at files changed.
The first important change is actually the SDK itself around resource.
The SDK itself, we already have this issue today with our SDKs. There's going to be an explicit initialization phase.
for, creating a resource. So I think that is… if… if you go to the SDK, where it talks about, on… on creation.
Yeah, it's… it's further up, Riley. I can present if you want. Or we can… I can just talk through it, here.
Yeah, let me… let me pull it up quick, and… Give me one second, sorry.
What's the wrong one?
This is where I regret having 10,000 tabs open. It never finds the one I want.
Okay.
Alright, we want to go with the rich div.
Okay.
So that's the API details. So let's talk about SDK, things that change.
Effectively, we create a new SDK component called an entity provider, which is responsible for, resource. There's a listener mechanism which decomposes the SDK around resource startup and then resource change over time.
And we have this notion of resource initialize and then update events, where entities are added or removed from the resource or changed.
The entity provider… has an explicit two stages to it. This is actually true a little bit today in the JavaScript or TypeScript implementation of OpenTelemetry.
Because resource detection is asynchronous in OpenTelemetry, we actually don't know when it's fully done, and we can't block until everything's done. In some languages, we can.
So what we're calling out here is we're calling out that, there will be two phases to the SDK. There will be a resource detection phase, where things aren't quite done.
And there'll be an initialization phase where things are done.
We're also calling out that, when you create something, you kick off the resource… when you create this entity provider, it kicks off that resource detection phase.
And there's a set of behaviors the SDK has during that initialization phase.
And then once the initialization is complete, you go into, like, you know, things are set up.
I will call out, in the Java prototype.
We actually have it so that if you want to have synchronous startup the way that Java does today, that is a configuration option. And if you want to have asynchronous startup.
you can also do that as well. Like, you can choose… you can actually opt into this behavior. So that might be a direction we go for SDKs, with how we specify this, but this is explicit. It accounts for some of the complexities that exist today in JavaScript.
and it opens up the door for the ability for things to change going forward, right? Please take a look at this, because the key initialization aspect of the SDK is something we've been prototyping and experimenting with, and this is what the specification looks like for that today, and so I think this is worth investigating. What is still an open question, and why this is still, like, we still have some things to do in prototyping land, in entities world, is, basically questions around, what happens when a resource changes. What… what… what's the behavior? It's not just about spans, it's basically what do we do with metrics, what do we do with logs, what do we do with spans? The initial prototypes, we're actually pretty happy with the behavior for spans and logs. We think it actually matches what users will want. Metrics is something we need to do a little bit of work on.
But that's… that's kind of the open question, is like, if… if I'm in a browser, and the session has changed.
What do I do with metrics I was collecting against the previous session? Do I report them now? Do I store them on the side? You know, those are things that we're kind of prototyping and experimenting with in the entity SIG. So that's still TBD.
The key thing we want folks to look at here is we have refined the listener interface, basically just adds this initialization step to deal with that practice of initialization might take a while, and you don't want all these events firing while initialization's going on.
And we've added explicit, kind of, initialization specification for what has to happen and what can't happen.
there is a fallback where if initialization doesn't finish, the SDK eventually just lets things through no matter what, with some default resource, right? This can't block indefinitely.
If you want to see the prototype of this, there's a prototype in Java. I believe it's still the draft PR against Java. If not, it's linked to in the description, and we can look through that. Anyway, I wanted to give everyone a heads up and get your attention to this. I think there's a lot in here.
There's also this optional capability I wanted to walk through, where optionally.
you know, async loading is a thing that you can opt into with Java. We're exploring what that looks like as well.
Because I know some SDKs and APIs really want, like, fully synchronous, you know, everything is locked down when they start.
for the purpose of, of, what we're seeing, though, I think this, this listener capability and, and, being more, flexible is going to be important going forward. Okay, anyway, with that, I don't know if anyone from EntitySig, Ted, Daniel, Dimitri, I don't know if Dimitri's here, if any folks want to say more, feel free. Otherwise.
we can discuss here, we can discuss on the thing. I was mostly trying to just get folks' attention to the work that's being done.
**Daniel Dyla (Dynatrace)** 20:34 I don't have much to add. I would just say for JS, startup has to be synchronous, but some of the resources have to be asynchronous, so we defer the asynchronous waiting to the export pipeline, but that's… more of a detail, I guess, as far as this specification is concerned.
**Josh Suereth** 20:55 Yeah, and the Java prototype, like I said, you can optionally do that. So, we can actually defer The ability to… for things to… to export until resource collection has finished, or… You can force it to happen immediately by a choice of which thread executor you use.
Yep. And then on Thursday, we talked about.
**Daniel Dyla (Dynatrace)** 21:18 when a resource changes with a metric, we wanted to, like, close out the metric, export it, and start a new one. Have you done any prototyping or spec work on that since we talked about it Thursday?
**Josh Suereth** 21:31 No, I took a long weekend, so literally after that meeting, I was out. Yeah. Okay.
**Ted Young** 21:44 You know, the only thing I would add is, and thank you for moving this forward, Josh, the only thing I would add is with config files out there as well, it just feels like a number of things related to startup and initialization, changing, and I feel like that's also an area, in cases where people are doing all of the SDK bootstrapping, by hand instead of automating it away somehow.
That's maybe an area where different languages might find some way to improve things, so I just wonder if this is also an opportunity for SDK maintainers to, like, think about initialization in their language, and, like, are there ways for that to be a simpler experience for the people who are doing the setup by hand?
**Josh Suereth** 22:37 That's a great question. I… I actually think, The ability for things to dynamically change in an SDK, like it's set up in config, is a hard problem.
And is… effectively, we're solving half of that with entities and resources now, right? We're doing… we're doing a piece of it with some of this async startup.
If we wanted to have a model where the SDK can react to configuration changes and reboot portions of it, that's… that's kind of a broader discussion we should think about. Yeah, the scope of this OTEP is just… that in relation to resource detection, right? But I think you're right that there's possibly, like, a lot of similarities in terms of, like, events and listening and reacting to change that we probably want to build in if we have the capability to dynamically reconfigure an SDK remotely, right, with config coming in.
Or react to a file change, right?
**Ted Young** 23:37 Yeah, exactly. It's not something specific to this particular, change. I'm just noting we don't… we don't really have a process for doing… like, language-level initiatives. I know some SDKs have done this, like, I think in JavaScript recently, there was, like, an SDK 2.0 initiative to just clean up some stuff.
It's not the kind of thing we would put into the spec, necessarily.
I'm just noting, like, with this extra complexity coming down the pipe, it's also an opportunity to maybe… Flip that around and be like, well, is there a cleaner way to do things?
**Daniel Dyla (Dynatrace)** 24:14 I think we may want to put some of it in the spec and be more explicit about the phases of startup and how they're meant to interact, because we want… OTEL to feel the same in different languages.
Yes, JS did just go to SDK 2.0. We're gonna rev to 3.0 next year, like, that… our plan is to kind of start getting on that, and… and cleaning up some of those older things, and… and not supporting everything forever, because forever is a long time.
But I think it's an opportunity for other languages to… or including JS, not just other languages, for all of the SDKs.
To feel like more of a cohesive product.
yeah, I would actually specify some of those things.
**Ted Young** 25:08 Cool. Well, I think that would probably… If that's the case, then it'll probably work better if we've got multiple SIGs.
chewing through this stuff in, like, a similar time frame. And we tend not to coordinate that way, so I'm just noting that. Like, we tend not to do that kind of coordination.
**Daniel Dyla (Dynatrace)** 25:27 Maybe as the config sig, winds down or reaches, you know.
Their sort of completion milestone, maybe a, you know, maybe a related SIG about startup and initialization can follow from that.
Because I think a lot of SDKs, including JS, will have to change the way they start up in order to consume files effectively.
**Ted Young** 25:55 Yeah.
**Josh Suereth** 25:56 Yeah, I agree. It sounds like we want an SDK initialization SIG, the more we talk here, yeah.
**Ted Young** 26:04 I mean, I'm sure there's also ways where languages would want to also pivot towards being more language-specific, maybe. At any rate, we've had years of feedback from users, so it's an opportunity to maybe Just do some reviewing around initialization and seeing if there's a better way to do it in general.
**Josh Suereth** 26:25 Yeah.
Absolutely, absolutely. Okay, great feedback, everyone, thank you. If you… if you have any concerns about, like, specifics in this, if you want to see some of the designs and changes, or the motivation, this… the motivation hasn't changed, explanation hasn't changed, high-level details sort… has slightly.
And you can read the details of what the API does, why it exists, that's similar to what the entity provider was before. The big change that we just dropped was the SDK details and this initialization phase that we needed.
To make this all work. So, please take a look. Overall initialization, SIG, I think I agree with. I would like to, with entities, I would like to make progress relatively quickly, so what I'd want to do if we decide to have an initialization-focused thing and have that all work at the same time.
I think there's two ways we could go about it. One is.
We let EntitySIG run forward with what they're doing.
And we use them as a template for what initialization will look like across the SDK, and we apply it in other ways.
Number two is, we could try to cut scope of entity SIG to not include initialization. Unfortunately, I think that would just kill the entity SIG. So, that's kind of why I don't think that's really a choice here. But that does mean there might be some risk going with number one, so wanted to call it out. Anyway, thank you, everybody.
**Reiley Yang** 27:52 I have a quick question. So, for entities that keep changing, is there a flag or something that can be carried as part of the data payload to indicate whether the resource is up-to-date or is outdated?
You mentioned if there's a, like, delayed initialization, and we cannot wait for indigenate amount of time, we'll just send the data anyways with the default. Then, as a consumer, do I have a way to tell the difference between the default versus the real one?
**Josh Suereth** 28:26 We… we could add that, yeah. Like, if you… like, that's actually trivial to add. It's not in the prototype right now, but… but that's… yeah, that's a good idea. So feel free to, like, make a comment on the spec about that, because I think we could absolutely do that.
**Reiley Yang** 28:41 Thank you.
**Daniel Dyla (Dynatrace)** 28:42 I agree. I think you could have possibly, like, some sort of resource attribute that just says, like, there were uninitialized, you know, unknowns here.
**Ted Young** 28:54 Yeah, I think… I think there are also edge cases in general around this stuff.
**Reiley Yang** 28:59 And that's…
**Ted Young** 29:01 why… getting more eyes on it in different languages would be helpful. It's also why I feel like we can't break it up into smaller pieces. Everyone who's done a prototype has come back and said, like, the entity stuff itself is, like, actually very simple. It's the wiring.
Where the questions come up, and what… how do you handle edge cases around… Change happening at the entity level in these kind of asynchronous systems.
**Daniel Dyla (Dynatrace)** 29:30 We do have the dropped attributes count. It doesn't tell you why they were dropped, and typically, right now, I think the assumption is that you violated some sort of limit.
but that would give you some idea that you're missing something.
**Josh Suereth** 29:47 Except you don't know. Like, I like that idea, Daniel, it's just, so the only thing we know when we decide to move on… it depends on how you've implemented it, right?
From the initialization of the SDK standpoint, we can force an initialization event after a timeout, right?
But we only know which resource detectors failed. We don't know how many attributes each one would provide.
**Daniel Dyla (Dynatrace)** 30:13 Yeah, okay.
**Josh Suereth** 30:14 have their names. Like, we could actually say, like, here's the ones that failed, right? And we could… we could use their names. So that's actually a useful… it's even more than what Riley was saying. We could say, here's the things that weren't finished.
When I reported. So, it's, like, I don't know my host, I don't know my network, but I did know my service, right? We could report that, and that's actually really interesting.
The way that it's implemented in Java, though, I actually have timeouts on both sides of the listener.
And so, if the listener on this side fails, he has no information.
he doesn't… like, all he knows is that it failed and didn't initialize. He doesn't know why the entity provider didn't fail, because it's possible someone made a bad resource detector that never completes. And so I was protecting against that. So I protected both sides in the initial prototype. However, we could… we could… we could do… We can figure this out. Like, I think this is something for us to explore. So we could have a thing where it's like, if all you have is a signal, hey, this resource wasn't fully initialized, I think that's good.
And where we know what didn't initialize, we could report it, right? So we could report these resource detectors weren't done, or these entities weren't finished being discovered.
That's something we could actually put into the spec. I like going both of those directions, but we don't know how many attributes is the main thing, so we have to find a new signal, or find a new place to put this.
**Ted Young** 31:38 There's… there's also a question about, What is the entity's provider doing as far as this kind of protection versus what are the detectors doing, and where do you put the configuration. The bit that we've looked into this so far for handling problems with change, like flapping, for example, what if you have something that's flapping, changing very rapidly?
And… it seems like a lot of these are pretty case-by-case, so we're inclined to say more of the configuration and logic would be in the detectors than having, like, a generic way of handling this, beyond just handling a literally dysfunctional detector that's just jammed.
So… there's also that. Like, detectors should potentially, on their own, give up, and then return something themselves that's, like, valuable, explaining how they failed, because they're the thing that actually has the information, not the energy provider. It doesn't know why a detector failed.
When it doesn't return.
**Reiley Yang** 32:56 Yeah, makes sense.
Any other comments?
Okay, so we're done with the topics today. If there's anything people want to add, I'll just ask, like, 1, 2, 3.
Anything?
2, 3, okay, thanks, Aura.
Have a great one. Bye.
