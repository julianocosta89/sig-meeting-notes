SIG: Entities SIG
Date: 2025-11-24
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/K1AG-D5hhZ91kn6jQ_UjWp5yQmgIvTuuSubwFazGGUW_Sl9tCYj66uOpIYJa7mLM.d1dePD5SRRGk97xu
============================================================

## Zoom Recording Transcript

**krajo Krajcsovits** 00:22 By whom?
**Daniel Dyla (Dynatrace)** 00:28 Hello?
**krajo Krajcsovits** 00:35 Yep, hi, I'm just listening in.
I'm actually in the Romitus SIG.
Just wants to get a sense of… Where this project is.
**Daniel Dyla (Dynatrace)** 00:47 Awesome.
I'm sure glad… I'm sure Josh will be happy to hear from you.
**Ted Young** 01:12 What up, y'all?
**Daniel Dyla (Dynatrace)** 01:14 How's it going.
**Ted Young** 01:18 Ready to be on vacation.
**Daniel Dyla (Dynatrace)** 01:23 You taking a big one for the holidays?
**Ted Young** 01:26 Yeah, I'm gonna take this week off.
**Daniel Dyla (Dynatrace)** 01:28 Oh, cool.
What are you doing here, then?
**Ted Young** 01:33 there was, like, a little bit, like, a slight rump of stuff, so I was like, my Monday morning will be spent.
Nipping all the buds.
So that I can post the week off in peace.
And then I saw this meeting, and I was like, oh, the meeting… this meeting's actually happening. If I miss it, then I'll miss, like, the next 8 weeks of it, probably, so…
**Daniel Dyla (Dynatrace)** 01:55 Yeah, I think we canceled, like, 3 in a row.
**Ted Young** 01:57 I'm kind of on…
**Daniel Dyla (Dynatrace)** 01:58 Unfortunate timing, but… It is what it is, I suppose.
**Ted Young** 02:03 I was like, I'll show up for this, why not?
**Daniel Dyla (Dynatrace)** 02:06 worked out well for me, because I didn't have a lot of time to work on entities' stuff anyways, so… I got to skip 3 weeks of telling people, sorry, I didn't do what I promised I would do.
**Josh Suereth** 02:20 Or didn't do all of it. I did some of it.
**Ted Young** 02:22 Yeah.
I thought, someone, maybe it was you, Josh, added, like, stability to the… Meeting agenda.
**Josh Suereth** 02:30 Yeah, I do.
**Ted Young** 02:32 It relates directly to what you were just saying, Daniel. It's like…
**Daniel Dyla (Dynatrace)** 02:36 Yep.
**Ted Young** 02:36 We're all overclocked, and, like, that's actually…
That's actually the point behind the point of this stability initiative. It's just drawing
Down how many new things we're gonna start to zero, until we stop feeling like this.
**Daniel Dyla (Dynatrace)** 02:55 Yeah. I really hope this one doesn't draw… this is not included in that drawdown.
**Ted Young** 03:00 I want to say, like, we have a commitment to, like, we have to, like, finish everything we've committed to starting.
**Daniel Dyla (Dynatrace)** 03:06 Yeah, okay.
**Ted Young** 03:07 Stability doesn't mean we're stopping the new initiatives, it just means we're not…
**Daniel Dyla (Dynatrace)** 03:13 The entrance of the funnel.
**Ted Young** 03:15 start anything new, and we're gonna try to, like, work with the SDK SIGs in particular in some kind of, like.
There needs to be some new way of working with the SDK SIGs around stability that doesn't feel like everyone's, like, off on their own, but also doesn't feel like, new features, new features!
**Josh Suereth** 03:38 So, yeah, that's… that leads into things. I… I got the worst,
Head cold after KubeCon, so apologies for not making it last week, and just sort of not showing up.
But yeah, I feel like this is what I would call the KubeCon shuffle.
I don't know if I'm presenting, but .
**Daniel Dyla (Dynatrace)** 03:59 You are not presenting.
**Josh Suereth** 04:00 Here, I'll present it.
That's the KubeCon shuffle right there, of prepping for KubeCon, going to KubeCon, dealing with the repercussions of coming back from KubeCon in a super spreader event, and then,
You know.
**Ted Young** 04:13 Yeah.
**Josh Suereth** 04:13 Now we're back into the day-to-day.
Alright, let's get started, because we got a bunch to get through.
First off, prototyping efforts. So this is the OTEP around, allowing, kind of, multiple resources to be reported from an SDK. We took a different approach, Ted, than the, like, listener approach.
And this one prototyped way easier, and I actually have it working in Java. There's still some to-dos, I think, but I think I'm confident committing to the OTEP at this point.
But I think we… what I wanted to ask was,
Is there anything else… given stability, we might just aim for the OTEP to be approved, but not implement all the way through?
Because there's, like, a question of, like, I don't want to start new work, but I want us to be confident in this direction before we commit. So the question I have overall with this OTEP is what more do we want to see happen, and what other prototyping do we want to do with it?
Right.
**Daniel Dyla (Dynatrace)** 05:15 But… Yeah, so…
**Ted Young** 05:16 Sorry, go ahead, Daniel.
**Daniel Dyla (Dynatrace)** 05:18 at the very least, we have to… you know, I took the SDK details section. I did work on that. It's short, but I think what I have would actually serve as a…
Minimal starting point, and then we can handle the rest and spec later.
I did, while working on it.
Have a series of questions, though, which are at the bottom of the agenda here.
I don't know how you handled each of these in your prototype, because I haven't, looked through the prototype that you posted in the channel yesterday yet.
**Josh Suereth** 05:54 Let's put them up here.
**Daniel Dyla (Dynatrace)** 05:56 Yeah, I… Wasn't sure when you would want to talk about them.
I know your prototype does share the export pipeline, but…
I think we have to define what happens when you…
shut down a child provider, for example. If it shuts down the export pipeline, you've obviously, caused an oopsie.
should it flush the export pipeline, though, without shutting it down? Like, what all… if I shut down a child provider.
I assume it flushes…
**Josh Suereth** 06:30 But does it…
**Daniel Dyla (Dynatrace)** 06:32 And then does not shut down its children. But does that flush also potentially flush
It's parent and or sibling providers.
If you're sharing an export pipeline, that may happen just…
You know, as a consequence. It might be okay, but we should define that.
Let's see…
**Josh Suereth** 06:58 I'll tell you what I want to do, and I didn't finish implementing this, because I got… I have to untangle Java's SDK more… so, like, Java's SDK right now, for metrics at least.
is really, really, really highly tightly tied for one reader, one SDK, or sorry, one set of readers, one SDK, and it, like, dives deep very quickly.
And so I actually have to re-architect a good bit of the, hierarchy. It's not, like, like, in terms of details and complexity, none of that really changes, but I have to redo some of the hierarchy. But the… my thinking is, the way I want this to be, if you look at this with, like, creating the sub thing, flush should flush.
everything. Like, when you flush, you just flush everything, because it's too expensive for us to do anything else. But, close is like… or shutdown, and close, or whatever you call it in your language.
is the equivalent of, kind of, cleaning up memory. So if you think of this as allocating, like, for a sub-resource that lives with a different lifetime, when I shut that thing down, what I'm saying is, as soon as you're done processing whatever's held in this memory, the next export.
Clean it up. You're done. Like, it's like a GC signal.
So that's how I'd like to deal with it. I actually have to do a good bit more work in, like.
In Java ended up with a doubly linked list, otherwise that would have been true.
**Daniel Dyla (Dynatrace)** 08:23 Yeah, we have all the same problems in JS because our metrics SDK is essentially a port of the Java SDK.
**Josh Suereth** 08:34 I apologize for all my sins.
**Daniel Dyla (Dynatrace)** 08:36 It is what it is. I wasn't the one that wrote it, so that was… when I was trying to, prototype, I was running into similar problems, and I… since I was not the one that wrote the metrics SDK, I was, you know.
trying to learn as I was going, but it is what it is. I agree with you on flush and shutdown. I think that flush, we should define as… when you flush something.
without shutting it down, what you're trying to say is…
get all of this to my backend as fast as possible, because something might happen. Like, you might be in a lambda, the lambda function's about to end, you don't know if you'll be properly cleaned up or not, you're just trying to flush.
So what you're trying to do is mark.
**Josh Suereth** 09:20 at the.
**Daniel Dyla (Dynatrace)** 09:20 leased everything from this provider as, please export now. If other things also get exported right now as a side effect, I think that's totally acceptable. So if we say, you flush a parent, all of its children should be flushed.
If you flush a child.
its parent and siblings might be flushed, but that's not a requirement, right? It's not a requirement that they are…
separated. Because if there are some shared components, like a shared export pipeline, the flush might happen anyways, and we just have to say that's fine.
That's the way that I would handle it. The shutdown? Similar, except I would say… a…
The export pipeline Cannot shut down until all of the associated, providers… are shut down.
So you have to either have a reference count, or some mechanism, which I'm sure will be language-specific.
But it has to have… we cannot have the situation where an exporter shuts down, and some provider is still trying to write to it.
**Josh Suereth** 10:41 Yes. What I… what I actually was thinking was, if the parent shuts down, all children shut down as well. So, like, there's… there's an owner, if you will.
**Daniel Dyla (Dynatrace)** 10:50 Yeah, that's fine, but if a child shuts down.
**Josh Suereth** 10:53 It should not be able to merge together.
**Daniel Dyla (Dynatrace)** 10:54 not shut down its… so then that means each provider has to know whether or not it is a child or a parent provider.
**Josh Suereth** 11:04 Yes, although what, what I did was actually subtly different. When I create… so in the Java prototype, I was a bit lazy. Let me see if I can find and show this.
In the SDK, We'll look at tracing, right? Because that's the… For symptoms.
**Daniel Dyla (Dynatrace)** 11:23 Most… well, yeah.
**Josh Suereth** 11:25 And this is a little bit ugly, I think, but if we look at with entity.
And I didn't implement this for a generic amount of entities, but it's, like, the same, because all this does is effectively make a new resource, with a specific entity in it.
And then merges it with the existing one to make sure the entity's there. I have an ignore shutdown processor that I just wrapped the pipeline in.
**Daniel Dyla (Dynatrace)** 11:50 Okay.
**Josh Suereth** 11:51 Because the way shutdown works in tracing in Java is the actual processor handles shutdown and understands the state of it.
So, because… so basically, anytime I instantiate a child, I just say, ignore shutdown things. Otherwise, everything's exactly the same.
**Daniel Dyla (Dynatrace)** 12:08 Yep, you did the same thing I did. I didn't give mine nearly… I didn't give it a descriptive name at all, actually. It's just a nameless object that pretends to be a spam processor and shut down as a no-op.
**Josh Suereth** 12:22 And it proxies to the…
**Daniel Dyla (Dynatrace)** 12:25 to the child span processor. I did more or less the same thing.
**Josh Suereth** 12:28 Okay.
**Daniel Dyla (Dynatrace)** 12:30 Great minds think alike, right? Well, it's the obvious solution.
**Josh Suereth** 12:34 Yeah. But…
**Daniel Dyla (Dynatrace)** 12:36 So…
there's… there's other questions further down in the list that came from this. If you're taking spam providers that were… er, spam providers… spam processors that were potentially written by end users, can we assume that they are stateless enough
To handle multiple resources from multiple different providers, is this…
You know, even if it's not a breaking change in,
the API itself, is it a breaking change in spirit? Like, what are the chances that there are out there spam processors that are gonna break if you start sending different resources to them?
ditto to export pipelines, because I can tell you with confidence, the JS exporters will break.
**Josh Suereth** 13:30 Oh, interesting.
Huh.
**Daniel Dyla (Dynatrace)** 13:35 Because the way that we handled the immutability of resource to begin with is we…
capture the resource on the first export, and then we use that for every subsequent export. We never look at resource again.
**Josh Suereth** 13:51 Yeah. For Java, they have a cache.
Of the bytes of the resource that they use every time they export?
But it's actually a cache of any possible resource. Like, it was designed as if resource could change, even though it can't.
We got lucky there.
**Daniel Dyla (Dynatrace)** 14:07 Yeah, we're not so lucky. I know Mark Pickler has rewritten a bunch of the exporters since…
the early days when they were written, so it's possible that those assumptions don't exist anymore, but I don't think so.
So we'll have to look into
there may be other SDKs, and then certainly.
**Josh Suereth** 14:26 End user components, where they've written their own spam processors and stuff. Entirely possible that those are all broken.
**Daniel Dyla (Dynatrace)** 14:33 And that they would not be shared among multiple providers gracefully.
**Josh Suereth** 14:39 Yeah, that's… that's a good point. I'm trying to remember some of the other implementations that I reviewed.
And how, like, where resource came in.
**Daniel Dyla (Dynatrace)** 14:50 Yep. In the interest of time, should I just quickly go through each of my questions, and then… because I don't… I didn't put them in any sort of priority order.
**Josh Suereth** 14:58 That's… that's fine, yeah, I… in the interest of time, go through them in whatever order you feel like makes sense, but I want to make sure we're not covering these, yeah.
**Daniel Dyla (Dynatrace)** 15:05 Yeah, I'll go top to bottom. So, the next one I have here is, how do we distinguish between stateful and stateless components? So, you cannot share parts of the metric pipeline because they are metric storage. You could share parts of the trace pipeline, like the…
You know, span processor, because they're theoretically stateless.
How do we distinguish? Do we distinguish?
If we clone them.
we have to have a generic clone mechanism, which doesn't exist now, which would mean that you can only use this on what I would call V2 span processors, and then that's…
you know, a significantly bigger change than what we were originally talking about, so I think that that quickly goes down a road that we don't necessarily want to go down.
skipping… I know that we can address these later. Skipping to the next one, we have, I believe, the configuration one is next.
Oh no, yeah, real… real providers versus light providers. So right now, in your prototype and in my prototype.
We are… if you do…
for entity on a tracer provider, you get another tracer provider, which is the exact same class and all of that.
There are configuration implications to that, especially once you get into file-based configuration and op-amp. If you change a child configuration, what happens to its parent? If you change a parent configuration, what happens to its child, if anything?
I would propose that we go to a light provider, which does not have any of its own configuration, which looks at the parent configuration
and… You know, essentially… Inherits everything from the parent and has no configuration of its own.
Again, we can… skip…
past that for now. Actually, the rest of the questions I have are kind of addressed by discussion we've already had.
So…
**Josh Suereth** 17:27 I, I was also kind of thinking about this, yeah, like, do we need to have the ability to address these things with config?
And, and…
**Daniel Dyla (Dynatrace)** 17:34 I would prefer…
**Josh Suereth** 17:35 Because they're dynamic. Yeah, I would say.
**Daniel Dyla (Dynatrace)** 17:38 prefer not. I would say, if you are inheriting, or, you know, whatever word we want to use, creating a child provider using an entity.
Everything should be the same.
Except that is a new resource going through to the export pipeline.
**Josh Suereth** 17:57 Well, specifically for OpAMP, I think we don't want to have a different resource for OpAMP, because that would actually imply that you would actually have to make a new connection and say, I'm a different agent with this resource.
**Daniel Dyla (Dynatrace)** 18:10 Yeah, we don't want.
**Josh Suereth** 18:10 Which is not… we don't want that at all.
whether or not you can address it with other config. Like, we might… we might think about having, like, oh, your view config can target resource attributes in addition to, like, the metric name, right?
**Daniel Dyla (Dynatrace)** 18:25 I would much rather do that based on a generic, like, entity filter. Like, target, say, if something comes in with this entity, treat it in this way.
And then, you know, if that matches on a child, then great, and if it doesn't, then also great. I would rather not address…
the provider, I would rather filter based on, the telemetry that it generates.
Yeah, that makes sense.
**Josh Suereth** 18:56 I'm also thinking about, if you think about, like, our general use cases, right? So, metric provider. It's the export pipeline, which is how often to report data.
we don't really want to change that based on the notion that there's different entities… like, let's talk about browser session, right? I want to report the same way, regardless of whether the session has changed or if I have multiple sessions. Additionally, the metric itself, if I define a metric view.
I don't care which session I'm recording the view on, it's gonna be the same metric. It's just the session changed. So, like, that shouldn't change, right? If we look at spans, it's how much to batch, where to batch, right? And then,
the actual location that you fire the data at, it's the sampler of the span. Those shouldn't change based on resource, and if they need to, resource should go into the sampler, right? So that you can make a decision based on yourself.
That, like, so my opinion is, none of that configuration actually should be changing, generally, from this feature.
However, there might be something. Like, when I was looking through the SDK and what we provide, I didn't see anything where I felt like we had to do it, or it actually made sense to. I felt like it would actually be a detriment to.
But it's possible there's something you want to do based on the existence of one of these things. So, for now, I think we should just defer, like, let's go with light.
and try to make it not a one-way door decision, where, like, if we ever wanted to make it be a first-class thing, we have a way to do it. But for all the areas of the SDK today, I don't think we need it.
**Daniel Dyla (Dynatrace)** 20:31 Okay, so would it be sufficient to specify the SDK in, like, the light mode, and then add a note in that say, like, you know, in the future, we may…
you know.
like, how do you define future requirements? Because I don't want, like, the Python SDK to, follow the light spec and implement it in such a way that when we go to add, like, oh, we actually do need this to be addressable, they revolt because we told them that wasn't going to happen.
**Josh Suereth** 21:08 I mean, is there a way to make it so people don't revolt when you change things in general?
**Daniel Dyla (Dynatrace)** 21:13 No, I know, but I think.
**Josh Suereth** 21:14 We're already… Yeah, go ahead.
**Daniel Dyla (Dynatrace)** 21:17 I think we could just add a note, like, a non-normative note, that's like, provider… child providers do not have their own configuration right now, but may in the future. And, like, that would be it. That's all we…
We add…
**Josh Suereth** 21:35 That's… that's fair. That's fair. We have to… I'm a little bit nervous about that, though. I feel like if we were to add it, we would want to do it
In a way that we evaluate the backwards compatibility of it at that time.
**Daniel Dyla (Dynatrace)** 21:48 Okay.
**Josh Suereth** 21:50 Yeah, so I guess we could just go light, and then if we decide we want real later, and…
**Daniel Dyla (Dynatrace)** 21:56 the SDKs say that's breaking for us, then we just accept that as, like.
We made that decision, and it is the way it is. The cards fell the way they did.
**Josh Suereth** 22:05 Well, I also think that we should instead think about exposing resource everywhere.
like, make… like, the thing that we're gonna have to do in this one is make sure, like, if we want to have sampler be aware of resource, we can do that. If we want to have, you know, for example.
that… the fact that your export pipelines are broken because of multiple resources, that's the battle I want to have right now, and I think if we do that, we actually can remove a lot of the friction where we might not… we'll be able to get this config without breaking. Go ahead, Ted.
**Ted Young** 22:37 Yeah, I mean, I think I just wanted to express a general thought or concern, which is, like.
between config files, op-amp, and now, like, the entities changes, and the stabilization effort, where we want to encourage SDK maintainers to come up with, like, a simpler way.
to be able to, like, set up and install SDKs. I just feel like if we don't end up providing maintainers with, like, a lot of guidance about how to wrangle this, like, collection of stuff…
like, that… I could see people rebelling, or just kind of, like, not implementing a lot of this stuff.
Unless we come up with some kind of coherent plan.
**Daniel Dyla (Dynatrace)** 23:20 I think it's simpler than… than maybe you're thinking, especially if we go with the light, no-configuration version.
The children can just proxy their configuration to the parent, and…
The only real change is that… Processors… Need to…
Potentially accept different resources as they change.
**Ted Young** 23:56 Oh, yeah, this isn't a criticism of this approach. I actually think this approach, especially the light one, yeah, like, this is looking good to me. I'm just saying this… this is a lot, and we should err on the side of, like.
maybe… Over-explaining the architecture or an implementation plan with this, like, collection of Stuff.
**Daniel Dyla (Dynatrace)** 24:22 Yeah.
**Ted Young** 24:23 this, but also, if we really want op-amp, and we really want config files, I just feel like…
Maintainers often are left guessing at the details, and we would probably do well to…
**Josh Suereth** 24:35 Yep.
**Ted Young** 24:37 Go hard with the explanations for these things.
**Josh Suereth** 24:39 So this is where, if we go back to the first discussion we had, Daniel, this is why I think it's lightweight, is the question is, are we reusing
the export pipeline.
And our answer is yes, right? And there's no…
**Daniel Dyla (Dynatrace)** 24:53 Yeah, shit.
**Josh Suereth** 24:53 I need, like…
If we focus on making the export pipelines reusable as the thing that this is doing, across, like, this layered
Meter provider, tracer provider, log provider.
the configuration part, the op-amp part, should not change. That's owned by the parent. And then we talk about how to make a child that reuses the parent's export pipeline. That should be the focus. And so I think when it comes to whether it's light or heavy.
It's fine to be light or heavy as long as the thing that you're instantiating is reusing the key aspects of the parent, and that we focus on what gets reused and what has to change, right?
**Daniel Dyla (Dynatrace)** 25:33 Well, I think a consequence of a shared export pipeline is that the configuration cannot be, you know, the child cannot have its own configuration, because too many of the configurations affect export details.
**Josh Suereth** 25:47 Absolutely, yeah.
**Daniel Dyla (Dynatrace)** 25:49 So, I think that those decisions are intertwined.
**Josh Suereth** 25:52 Yep, exactly.
So, if we were to expose anything that had config at an entity level, it would be a brand new thing. So I think it's outside the scope of this, and we should focus on how to
Demonstrate to people how to do the layering, and how to do the sharing.
Yeah.
**Daniel Dyla (Dynatrace)** 26:09 Okay, so then let me real quick run through and…
I think decisions that we've made, we want to go light with the provider.
Which means that we can ignore op-amp and file config for the children. They just get their parents' configuration.
When… A child is… shut down.
Its parent should not shut… you know, it should…
whatever you called your, your proxy component, like the ignore shutdown span processor, or something along those lines.
And… Let's see…
Second question, how do we distinguish between stateful and stateless? We… the assumption is that all components are reusable.
Unless…
except the metrics, I think the state is in the metric reader, right? Isn't that where all of the…
where all of the metric stream state is stored, so that has to be recreated.
I can't remember. I have to go… it's been, like, 2 weeks since… you're muted.
**Josh Suereth** 27:42 It's, it's not, no, it's not a metric reader. Metric Reader reads a metric producer.
The metric producer's the thing that has all the state. But, like, what we have to do is the producer has to be able to produce all of the metrics.
So, like, the way… the way it was… it was done in, Java, the metric producer actually
Isn't tied to a resource?
And so we… I had to create this inter… well.
This… it pre-exists, by the way. So the initial Java API has this thing called a collection registration, which is a producer of metrics. It has a method called Collect All Metrics, which gives you all the metric data that you turn into OTLP.
that thing is what I hijacked. So I took that thing and made it so that it can understand there is now tenant data. So there's, like, the original resource, and there's all the sub-resources, and you can have them flushed out. I have a bunch of cleanup I want to do to that, for how it's structured, because it's basically, like, it allocates a set of metric data that everyone, whenever you grab a meter, it reports against this
Bundle of thing. And then when you create a new resource, it creates a new piece of data that you allocate all of your meters against that new bundle.
And if you shut down the meter provider, I can kill that bundle, and then…
you know, continue reporting against, like, whatever's left. So it's like this… Pre-allocated set of, you know.
metric area.
That has a tenancy unit to it, but that's all hidden behind this collection registration thing that metric readers get access to. So a metric reader has to have a way to, say, collect all metrics. That's the place where you need to understand the tenancy and be able to look at all the children.
So, you're right that it somehow interacts with Metric Reader, but it depends on how you architect it.
**Daniel Dyla (Dynatrace)** 29:32 Right, and when metric reader reads metrics.
It should get metrics from all of the providers that are in the tree, which is fine.
I… yeah, we have this component I think we stole from Java, so you should be familiar with it. It's, like, meter provider shared state, or something like that, which is where all of the metric stream state is actually stored. Yeah. I thought that was in the metric reader, but I guess it's in the meter provider.
**Josh Suereth** 30:03 It's… oh, God, if you… I… it's… it's kind of… it's split across everything. It's in… it's in everything.
**Daniel Dyla (Dynatrace)** 30:10 Yeah.
**Josh Suereth** 30:10 But that's the thing I'm gonna start decomposing. So there'll be… so instead of calling it meter provider shared state, there'll be, like, a, you know, global metric storage, or, or, you know.
Metric storage thing that will, inside of it, have things for all the resources.
**Daniel Dyla (Dynatrace)** 30:26 Yep, that's totally fine.
But obviously, that component can't just be, like, reused, at least without being changed. If it becomes multi-resource aware, then it could be reused. But then…
If you flush it, does it flush…
All of the meter providers, that's probably fine.
**Josh Suereth** 30:46 It…
**Daniel Dyla (Dynatrace)** 30:46 Because the metric reader already is.
**Josh Suereth** 30:49 Yeah.
Remember that with metrics, you have to deal with pull versus push?
So, Flush does absolutely nothing if you're doing, like, Prometheus export.
It's a no-op, because it can't. You have to wait for them to call you to get the data anyway. That's what makes metrics so complicated, because, like.
like, cleanup, for example. When can I delete the metric storage? I have to wait for Prometheus to ask for metrics, and then I can say, cool, I just collected the metrics, and I will never get new ones because that provider shut down. Now I can delete the data.
**Daniel Dyla (Dynatrace)** 31:22 Yeah, I guess… V…
**Josh Suereth** 31:24 Pain in the butt.
**Daniel Dyla (Dynatrace)** 31:25 situations where you're likely to call flush, you're unlikely to be using pull-based metrics anyways. I'm thinking of browser, Lambda, Android.
like, those aren't being scraped by Prometheus either way.
**Josh Suereth** 31:39 And there, the periodic metric reader just grabs all the metrics and fires them out.
**Daniel Dyla (Dynatrace)** 31:43 Yeah.
**Josh Suereth** 31:44 So if we wanted to figure out how to flush only do a subset, we might… we'd have to sort out some sort of detail there with the metric reader.
**Daniel Dyla (Dynatrace)** 31:53 So I guess the decision is we want to share all components that it's possible to share. It may turn out that there are some that we have to recreate, but if we… ideally, we make them multi-resource capable and share them.
**Josh Suereth** 32:11 Yes. Yeah. This is where my current thinking is, and again, partly it's because I don't think… I don't think we have options unless we do a big SDK rev.
On metrics, but… I think for the metric reader thing,
we get Metric Reader to be multi-resource aware, and we do the same thing we're doing everywhere else, where…
You get all the data, right?
**Daniel Dyla (Dynatrace)** 32:36 Okay. I think we should do an audit of the existing SDKs to make sure that that's not a ridiculous lift.
Because…
I think it's gonna be a lot of work. This is going to be the bulk of the actual…
hard part of all of this change. Like, trace is easy, logs is easy, metrics is not going to be easy.
**Josh Suereth** 33:00 I mean, trace I did in 10 minutes, logs I did in 5 minutes, because I did trace. Metrics took me, like, a few hours, so I hear ya.
**Daniel Dyla (Dynatrace)** 33:10 I think the batch span processor in JS is already multi-resource capable, just because of the way that we made it. I think we keyed on resource.
Ted, you got your hand up.
**Ted Young** 33:23 Yeah, I mean, and similar to the last time, if…
the… the bulk of the difficulty here is around metrics. I am curious, like, how much do SDK maintainers… like, how much of an appetite is there for, like, metrics 2.0?
In general.
Like, do we have a pile of annoyances with how metrics work in OTEL?
That we would like to fix with the re-architecture.
Because…
**Daniel Dyla (Dynatrace)** 33:49 I do not want that. As a maintainer, I am not interested in a metrics rewrite right now.
**Josh Suereth** 33:56 I know Go just went through a giant optimization
swing with, like, their stuff, so I don't…
I hear what you're saying, I think it's something to think through, but to me, the biggest problem with metrics is we have two implementations of metrics. We have what .NET did with their push versus pull, we have what Java did with what their push versus pull, and everyone kind of, cribbed from one of those two implementations.
Right? And, it…
the .NET one is the one I'm, like, talking to Daniel, I'm nervous about .NET. We should probably get someone
in the .NET group to kind of work through this with us, because they don't have a reader.
There you go.
**Daniel Dyla (Dynatrace)** 34:40 So…
**Josh Suereth** 34:41 It's an exporter interface that does both.
and somehow has access to internal storage in weird ways. So… So the question is…
**Daniel Dyla (Dynatrace)** 34:50 do we… Ignore that.
And use SHOULD… Everywhere for the implementation
and then must only on behavioral things. Like, the flush must flush these metrics, the shutdown must flush and clean up memory, the,
the configuration…
must be the same as the parent. And then all of the implementation details around, your reusing metrics components, the multi-resource, metric storage, all of that, we say, should. And that way.
NET is free to… like, if they have to recreate components because of the way they did it, then fine. As long as the end user behavior… there's only… there's only 3 end-user behaviors we care about. I'm creating…
based on an entity, I'm flushing, and I'm shutting it down. Those are the only 3 things that users are gonna care about. And as long as those are the same, the implementation details
Ideally, we want them to be as similar as possible among SDKs to make future additions?
More palatable, because when we add a new feature, we want to know, is this possible to implement everywhere?
But end users don't care about that, and I view that as we're trying to be as nice to the maintainers as we can, but if they have to go their own way in order to meet the core constraints of
The user requirements, then that's fine.
**Ted Young** 36:45 Given that we don't want metrics 2.0, that sounds very reasonable.
**Daniel Dyla (Dynatrace)** 36:49 Right. So then, some SDKs may say, we have to go to 2.0 to make this happen.
But I don't think so. As long as we leave it open.
**Ted Young** 36:59 They can have freedom to do whatever they need to do to make it work.
**Josh Suereth** 37:03 The thing is, though, so I think you're right, if we stick to these three, these are the three things we want to make sure the spec calls out.
Like, these are the musts.
But… The reason the metric spec is so confusing as crap right now is because we were flexible.
And, if you look at some of where the shoulds are and things, it's not an easy spec to read, and it's led to some really weird implementations. So, I agree with you, Daniel, like, we have to go that way, because that's what we already did.
Going back, if we could have been more…
prescriptive about the outcomes without… and had a better way to, like, outline what they were, I think we should have.
**Daniel Dyla (Dynatrace)** 37:47 Yeah. Unfortunately, it's too late.
At least for…
it's too late for the specification. Some of the SDKs may decide, you know what, we do have this metric tech debt, we want to go back and rewrite metrics, and we're gonna follow all these shoulds, and…
we're gonna implement it the way that, you know, if you had a greenfield implementation today, I think it would be pretty clear what to do based on the current spec. The problem was we had…
the metrics SDK specification had essentially two, if not three major versions, depending on how you're counting, and the implementations were trying to follow that without fully rewriting.
**Josh Suereth** 38:34 Yep, and I think if we had…
Yeah, there's one piece of the metrics SDK spec that I wish I could just kill.
That I don't think we're using in practice that makes it really complicated as well, but that's the… the whole diff-based algorithm, where you can have multiple exporters and be able to do deltas on all of them.
If I could redo everything, I'd kill that, but that's a different… anyway, that's what makes this hard, as well, because if you want to clean up a provider, you actually have to track how many of the diff producers are done with the data before you can kill it.
**Ted Young** 39:11 I think we should do a Metrics 2.0 in general at some point.
We don't, but we can punt on that for, like, a year.
**Josh Suereth** 39:19 Yeah, well, I… We can… we can do a… we can do a whole 2.0. There's always 2030.
2.0… Yeah, you can…
**Ted Young** 39:27 But my point is, like, tracing is kind of fine, like, logging is kind of fine, metrics is the one place where, from every direction, we get a lot of, like, angst about hotel metrics, where… but I think it's totally fine for us to just sit on that for a while.
Say, we're gonna sim this in, we're gonna put shoulds everywhere so everyone can make it work, and then at some point later, we will try to burn the house down, but we're not gonna do that.
**Daniel Dyla (Dynatrace)** 39:55 I think those 3 points that Josh put down are the only… like, as far as… a user…
And this should be our driving, you know, the North Star here, is these are the things the users care about. Everything else is a convenience for us, and if we have to drop them, then fine.
**Josh Suereth** 40:15 Yep.
Okay.
**Daniel Dyla (Dynatrace)** 40:17 Okay. I have dominated, like, 40 minutes of this meeting, so if you have additional questions about my questions.
**Josh Suereth** 40:24 This is the most important thing. So, the next thing I wanted to find out is…
So, you were working on the SDK spec, right?
**Daniel Dyla (Dynatrace)** 40:32 I know.
**Josh Suereth** 40:33 Can you take over that OTEP and finish with these three questions? Are you okay doing that?
**Daniel Dyla (Dynatrace)** 40:39 Yeah.
**Josh Suereth** 40:41 Yeah, take over. Okay, good, because I… what I want to do then is… I think we know where we want to go with that OTEP and get that to a point, where we're comfortable with what that looks like, and we're comfortable… I want to get that OTEP to the point we can unblock
The browser-related multi-session stuff.
And then what I want to do is start looking at landing specification work. Specifically, the previous OTEP, where we had entity detector.
and resource merge.
What I'd like to do, my target here is I want to unblock the environment variable push-based entity
discovery, where in configuration, instead of the configuration, file having, like, here's a specific resource, it has, I will pull my entity from environment as a thing, right? I want to get that out.
I wanna get…
code gen for Weaver on entities. We have a bunch of entities in Weaver for Kubernetes that I could codegen stuff to make an entity for, like, the collector, for, you know, JavaScript, for Java, whatever.
I want to actually be able to write that code, Jen.
Somewhere. Somehow.
And I have target languages that I'm thinking about of JavaScript, Java, and Go.
But mostly, this is kind of my big… one of my big focuses is, like, let's get Entity Detector and merge.
into the specification.
Somehow with the SDK. I'd like to start working on that. And I think, given where we are with this OTEP,
And given where we had been previously with the OTEP, we did not change resource merge. In fact, we actually use it exactly as defined previously in both of our examples, right, Daniel?
**Daniel Dyla (Dynatrace)** 42:30 I believe so, yeah.
**Josh Suereth** 42:31 Okay, this notion of entity detector, since we're… we're not making an entity provider that is public right now.
I think creating a detector that can look at entities and report resource with entities makes sense. I don't know if we need an explicit entity detector. We might be able to reuse existing resource detector things, but I want to have it be resource… sorry, entity aware.
And so that…
I have an idea for how to do that in Java, pretty dead simple. For Go, I think we need to do a little bit of work.
And then I want to write an implementation of the environment variable entity propagation thing, where we have a detector that will detect entities using that environment variable that is in the spec.
**Daniel Dyla (Dynatrace)** 43:18 Okay.
**Josh Suereth** 43:18 Okay, so that's kind of the next block of work I want to start
I'd like to land the specification this year, if possible, or we need to go update our status of the project as at risk, again.
That's the.
**Daniel Dyla (Dynatrace)** 43:34 I… I guess, you know…
probably many people have famously said this, but I believe that this part will be less complex, and should be…
Possible to get done more quickly.
**Josh Suereth** 43:49 I think the reality is, we as a group have thought about this for over a year.
And we already are comfortable with the solution we have in place. Actually getting it into the specification means we have to go through everyone else reviewing it for the first time, again.
Yeah.
**Daniel Dyla (Dynatrace)** 44:07 So you're worried about the review process, not the writing process.
**Josh Suereth** 44:12 Yes. That's where, like, we already have the resource merge spec written.
So, I'm thinking about putting together a PR this week to push that out.
And then finding a way to, like, make a prototype of an entity detector that uses environment variable.
that works with existing resource detection, as is in Java.
And then do the same for Go.
Okay. And then showcase, like, how this will work for us, right? Like, what we're gonna do going forward. The getting entity and resource merge, this is the thing I really, really, really, really want to land in SDKs. The entity detector with end variable propagation, I think, is an easy extension.
in SDKs, once we have it.
So I'd like to really start pushing on this. I… my thinking is, man, it's November 24th, I'm gone December 18th for 3 weeks, so that gives us 2 weeks to actually have something in the spec merged, if we want to get this merged in the spec.
Practically, because it'll be a week to kind of build out some case…
I'm thinking we're not getting this done this year.
That said.
**Daniel Dyla (Dynatrace)** 45:31 Probably… probably not.
**Josh Suereth** 45:33 That said, I still want this to be, like, the major focus for this group going forward, for the next three.
**Daniel Dyla (Dynatrace)** 45:38 I think if we're gonna set a goal then, I think… a…
a solution that we're, you know, a written specification that we are happy with as a final spec for this before you leave. If it's not merged before you leave, then so be it.
**Josh Suereth** 45:58 Okay.
That sounds good. So the next thing I'll do for entities is I will get the resource merge specification
put into a PR for the spec, and we can start working through that.
**Daniel Dyla (Dynatrace)** 46:11 Okay.
**Josh Suereth** 46:12 Okay.
Cool.
Yeah, go ahead.
**Daniel Dyla (Dynatrace)** 46:19 Yeah, I was just gonna read the next item on the list, I guess that's what you were gonna do anyway. Also, Creo joined here, I don't know if I pronounced your name correctly, from the Prometheus SIG, and I want to make sure that we have time to, address any questions that he has, since I assume
I assume you joined for a reason?
**krajo Krajcsovits** 46:42 Yeah, hi, thank you. You priced it low enough, it doesn't matter.
Yeah, my only reason is to kind of gauge where this work is, because on the Promatus side, you know, we are thinking hard on how to make the…
Attributes to labels.
conversion work, and entities are very interesting, because they clarify, like, what is actually identifying and what is not.
In a more explicit way. So, that's my main reason being here, just to get to gauge of…
where this project is.
**Daniel Dyla (Dynatrace)** 47:25 Okay. Well, I guess most of our discussion here has probably been…
may be relevant to that, but I guess what I can say is we're happy with the data model, which is probably what you care about the most.
So… If I… my gut feeling, you know, I can't claim to have thought a ton about
Prometheus specifically, but my gut feeling would be that it is safe to, take any identifying entity attributes and apply them as metric labels, and unsafe to do that with any descriptive attributes.
**krajo Krajcsovits** 48:08 Right.
**Ted Young** 48:11 I would say it would be great to get
This clarified as part of getting all of this stuff stable.
Right. It would be unfortunate to stabilize all of this and then discover some thorny issue around.
**Josh Suereth** 48:24 Well…
So I think the main problem we have right now for Prometheus is you can't fill out that section of OTLP with any of our implementations without using someone's branch.
of an SDK. So, like, that's why I really want to get this part of the specification written, resource merge, entity and resource, like, let's get that in so people can start experimenting with this as it flies around.
The merge algorithm, I'm already really happy with, especially when I wrote, like, integration tests, in Java. Oh my gosh, it's so nice to have resource kind of be override in, like, bulk entity one or another.
Makes testing way easier. Yeah, I was really happy with that. So, yeah, to answer… to answer…
The status of things.
You know, we started working on some harder problems where we were worried our initial prototypes would fail.
And we did a lot of investigation into this, where entities can change, like browser-based metric reporting is one of the things, where a session can change while the SDK remains alive. And so if we tie to a specific set of entities.
when you start the SDK,
you have a problem. Like, how do you report data against a browser session if that session can change for the lifespan of the SDK?
The thing we were talking about earlier was how to resolve that.
And so we're actually really comfortable with that solution, and a lot of the key data modeling we did around entity is working really well with that.
So, like I said, I think when I finally sat down and wrote the metrics thing, it took me…
like, two and a half hours to actually do metrics in Java, which is not bad, but for the… for the span, like, processor, it was, like, two minutes, because all the crazy amount of work we did in making this merge algorithm, which I don't know how many hours we put on.
That's done, that works. That's the hard part, is like, you know, how to understand what is in a resource, how the entity relates, and all that. Once that's done, the rest of this is relatively easy.
**krajo Krajcsovits** 50:40 So, what I'm getting at is that you're really working on the implantation SDK side, the spec is fairly stable, you don't expect, like, huge changes.
Which is…
**Josh Suereth** 50:52 Not to the data model, yeah. The data model is in the specification and marked as experimental, but we have not found any reason to change it just now.
The main thing we actually hear about a lot, though.
Is folks want the relationships between entities. And that's… that is something we might think about, but it shouldn't fundamentally change anything you're doing.
Go ahead, Ted. Yeah, yeah, sorry.
**Ted Young** 51:18 I just want to point out, you know.
we're gonna get a lot more feedback on our data model and everything else once we have implementations out there. Part of the reason we're not getting feedback is, like, the backend, like, vendor observability database people probably are not paying a ton of attention to this.
And once we are actually emitting data, they will.
I'm not saying they're gonna come to us with, like, a bunch of, like, feedback and problems, but…
you know.
**Josh Suereth** 51:49 Oh, there's, there's a class… actually. I'm, I'm fully expecting… so, like, we're… we're defining an open-world ecosystem here for entities. We, we ran this through, in KubeCon, we did, like, a, you know, a user…
session where we had a bunch of people, and I drew a diagram on the board of how this all works, and people were really excited by it, and kind of understand the data model, and they like it. Biggest question, again, is how do I understand what relationships exist and what they are?
That we'll have to sort out. But…
There's a class of people who make resource-based databases who will be very angry at our data model.
Because it is not a UUID per resource.
And so that's the thing that I expect… I expect to get a lot of hate about that, just for everyone's context. If we drive past that to, hey, here's the problems we solved, do you have a solution to those problems? And if they say, no, cool, that's feedback we'll just work past. But if they say yes, that's feedback we need to listen to.
**krajo Krajcsovits** 52:57 Right, I mean, from Prometu's side, that's not a problem. We don't… we don't do UUID, really. We're just interested in, you know, getting clarity on… on what is… identifying what is…
descriptive.
And then building, metadata.
Like, much better support for metadata, or alternatively, huge number of labels, and then you're good.
**Ted Young** 53:22 And I think having your all input… I mean, the next step of this also, correct me if I'm wrong, Josh, is sitting down and defining all of these identities, right? And when we do that, like, actually having, like, Prometheus people
give feedback about what kind of labels they want to see. Probably, like, the most helpful time.
**Daniel Dyla (Dynatrace)** 53:40 Work is already underway.
**Josh Suereth** 53:41 Yeah, that's already started, actually. And we do have some Prometheus people, like, I think Arthur San Sylvia has been involved with that a little bit.
David Ashpole, who's, like, our liaison between OTEL and Prometheus, he's one of the leaders of the… the Kubernetes one is the one that's the biggest one, so we're trying to do all the Kubernetes-related
identifying attributes right now. So if you want to take a look at what that group has done, we can point you that way, too.
**krajo Krajcsovits** 54:09 Yeah, yeah, I know those people, I'm sitting with them in the Prometheus, so yeah, I get that. Thank you.
**Josh Suereth** 54:14 Awesome. And thanks for coming, man.
If you have any other feedback, let us know.
**krajo Krajcsovits** 54:20 As soon as I try it out. Alright.
**Josh Suereth** 54:25 Awesome. With that…
I'm gonna update this… I'll leave the status for one more week, and let's see how far we get, and I'll update the… our… I'll update our target…
release for the… for our current project in, the project board for OTEL. Implications of stabilization effort. One of the things that I think is actually going to be true, we have a Phase 1 and a Phase 2 for entities.
And I think we're gonna get this, this entity resource relationship stuff out.
the relationship signal for entities. I have a feeling that we're gonna have to hold on that work.
For some time. I do think it's going to be the most demanded thing as soon as we launch this, and so we'll have to evaluate it against the priority order, but I just want to set an expectation with everyone that, depending on where stability stuff is.
For me personally, I'm putting stability work ahead of entities, which you've seen with the past 3 cancellations. So, like, anything about getting Weaver and semantic convention stability federated, I am putting above work on entities.
Right?
I'm still making progress on both, because that's how I roll. I'd get bored if I only did one thing. But,
that's how I'm rolling, and I think when we get to this part where we have this environment variable propagation, we have it in resource, we have this OTEP that we can pull the trigger on running through implementation anytime we need.
great. We might need to put some pause on things to, like, get stability shored up, and then come back with a heavier effort. So, my thinking is, let's get everything shored up this year.
let's… let's get as much done as we can, let's get, like, the initial specification done where Prometheus can leverage identifying descriptive attributes, let's get that out for people to…
Hit on, and try, and, like, tinker with.
And then, in the summer of next year, let's…
see where things stand for whether… and we can decide Phase 2 at that point. So let's try to get this all out to make sure people are actually toying with it by the summer, and then let's evaluate where we are and how much room OpenTelemetry has to keep pushing through for Phase 2. Does that sound reasonable to everybody?
I do think when Phase 1 is out, Phase 2 will be immediately demanded, but that's,
I… if that's not true, we have… we have a time to pause and focus on stability, so…
We should think about it.
Cool.
Anything else?
Long meeting when you skip 3, right?
**Daniel Dyla (Dynatrace)** 57:10 Yeah.
**Josh Suereth** 57:12 Okay.
Alright, I'll see y'all next week.
**Daniel Dyla (Dynatrace)** 57:15 See you next week.
