SIG: Client Instrumentation SIG
Date: 2026-05-12
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/S40A9h15q4rpTaUctg5THSGNhVYFNeXRoKBizXK0ocZnO3na0lY1PrBRfA3Dc3aE.NNY_qEya1Tq5s_CC
============================================================

## Zoom Recording Transcript

**Martin Kuba** 05:38 Hey, Jason.
**Jason Plumb** 05:40 Hey.
**Martin Kuba** 05:41 Scott…
**Jason Plumb** 05:45 Can we get this Fireflies AI shit out of here, please? What is this?
**Martin Kuba** 05:52 I don't know, can I… I don't know what…
**Jason Plumb** 05:55 I don't know if there's a way to drop it.
**Martin Kuba** 06:00 Yeah.
**Scott Solmonson** 06:01 Hey, guys.
That's not me, but…
**Jason Plumb** 06:05 Yeah, I would like that not to be here.
**Hanson** 06:09 Yeah.
**Martin Kuba** 06:10 I don't know how to remove it.
**Hanson** 06:13 Who's the.
**Jason Plumb** 06:14 Oh, hold on, there's some shit in the chat. Type pause to pause recording, stop recording… By continuing, you agree to their privacy policy. Oh my god, everything is terrible.
**Hanson** 06:27 Recording… And so…
**Scott Solmonson** 06:32 The owner should be able to kick that participant, I would think.
**Jason Plumb** 06:35 There's… unfortunately, there's no owner.
It's not like… oh, there it goes.
Damn, okay.
**Martin Kuba** 06:42 I, I know.
Okay. Alright.
**Jason Plumb** 06:44 Bye. Never do that again.
I wonder who added that.
**Hanson** 06:50 Yeah.
**Martin Kuba** 06:52 They've been showing up in a lot of meetings, and not just as Fireflies, other AI.
**Jason Plumb** 06:57 Yeah.
**Martin Kuba** 06:58 Excellent.
**Jason Plumb** 06:59 Yeah.
**Scott Solmonson** 07:00 In the chat, I see Bhupinder Singh invited it here to record and take notes.
But whether that's real or not, who knows?
**Jason Plumb** 07:09 Okay.
Well, it doesn't need to be actively in the meeting, it can always just go steal the recordings and do it there without our knowledge, so at least it's not in our face. Ugh.
**Hanson** 07:22 Yep.
**Martin Kuba** 07:26 M.
The meetings are recorded, so there's no need for these things.
**Jason Plumb** 07:31 Right.
**Martin Kuba** 07:36 Hello, how are you guys doing?
**Jason Plumb** 07:41 Good. Hanson's getting some traction on his crash event.
**Hanson** 07:46 Yeah, I… when it's, like, your fifth priority, it's really hard to… so I totally understand from other people's perspectives on my perspective, too.
Oh yeah, I did this a couple weeks ago, let's go back.
I'm very bad at being distracted. I'm just replying to your post, Martin, from last week. So, about metrics. You might have moved on already, but.
**Martin Kuba** 08:09 Substant thing.
**Hanson** 08:11 Yeah.
Yeah, it's…
**Martin Kuba** 08:14 It's tough when these, like, discussions take, like, span… span months, and… like, you have, like, too many of them going on.
I feel like the same, like, with these metrics, I just wanted to capture it, like, so that I can just move on, like…
**Hanson** 08:30 Yeah, I think we've all written multiple times, you know, the use case and how it could be used, but the limitations, and it feels like we're repeating the same things over and over again.
But, you know, let's do it one more time, and hopefully this time we'll get into a documentation, we don't have to write about it again.
**Martin Kuba** 08:51 Yeah.
It was… it was a bit surprising to me.
to, to hear, like, so many people say that they actually think that metrics in the client SDKs, like, is something that they would… might want.
**Jason Plumb** 09:04 Yeah, yeah, that's interesting.
**Hanson** 09:08 Until they look at the data that they get, and they see, oh, I can't have I can record for all… I can't… When you have an environment where the devices are so heterogeneous, and you don't… you can't identify it.
**Martin Kuba** 09:28 No.
**Hanson** 09:31 Are you… oh, you're on mute, Jason?
**Jason Plumb** 09:34 Sorry, I had a personal thing going on.
**Hanson** 09:35 No, no worries, no worries. Do we have an agenda? I haven't looked at the…
**Martin Kuba** 09:40 There's nothing on the agenda.
**Hanson** 09:42 Okay.
Well, we can talk about this, then.
I think people go into it, says, I want metrics, because how can you not have metrics? And we're like, yeah, right, we want metrics. But it's metrics lowercase m they want, not OTel metrics, and I don't think people realize the limitations of OTel metrics, and why decisions were made like that. So… if you come in, you're like, hey, we've got metrics. We have things that look like they're counting stuff, or rates. It just looks… the shape looks correct, but the limitations make it so that what you can gather is not useful for RUM use cases. It's not useful for identifying gaps in particular, you know, slivers of the population segments.
If you just want to capture, like, for my entire, you know, population, or some, like, you know, low cardinality, you know, groupings that you can have, sure, but how useful is that? And do you actually need metrics to capture that kind of stuff?
And can you do this another way, by deriving your own metrics with logs and spans?
So…
**Martin Kuba** 10:56 Yeah. So, like, I… I've been, like… so, like, this is, like, where I'm kind of landing at the moment. Like, you can tell me, like, if I… if you agree or not.
I'm not going to, like, push for metrics… metrics, like, in, like, full-on support in the SDK, like, you know… Having it, like, in the distribution, or, like, having it optimized.
or building, like, instrumentations that generate metrics. I still, like, I think that's… I think it's a secondary use case. I don't want to dismiss that there are use cases, that people want to use them.
So, like, I would say, I think what we're gonna do is, like, document it in the… in the SDK somewhere, like… like, what… Like, how we… you know, that… If people want to use the Metrics SDK, go ahead, but just be aware of these things.
You know? Yeah.
Yeah.
**Hanson** 11:55 I think that's where I ultimately land as well. It's like, there… I can't say there's no use case, but I would say the use case is marginal, and we shouldn't bend over backwards to support it, but if someone wants to do the work to basically get Hotel metrics that they can just show in their dashboards without having, you know, additional processing on their end.
cool, but it's a… It doesn't add very much.
Given the way the spec is right now. Now, if we could modify the spec.
But that's a whole new discussion. Like, I would love hotel metrics to be useful for these dynamic environments and heterogeneous runtimes and all that stuff, but… Yeah. That sounds like a…
**Jason Plumb** 12:47 Yeah, for a certain class of problem, it's still a good idea. Like, if you're asking, like, on average, how many times do people reach level 3 in our game, like, that's a good metric to have, right? Throw out all the resource stuff, you only care about application concerns, that's an application level metric, and you go from there.
**Martin Kuba** 13:08 Damn.
**Hanson** 13:09 They certainly can't use that with events.
Measure that, because…
**Jason Plumb** 13:14 You could if you aggregate. I mean, there are people still wanting to do that, where it's like, they're gonna keep a count and then emit an event once a minute with that data. Like, that's a metric!
**Martin Kuba** 13:24 I mean, that's essentially what we do, like, in the Web SDK for Grafana right now.
**Jason Plumb** 13:28 Right.
**Martin Kuba** 13:30 And you can actually… Sorry, and like, Neuralink did the same thing. Like, we did not, like, do aggregation in the browser SDK. Like, we did the aggregation in the back, in the ingest.
So…
**Jason Plumb** 13:42 Yep.
**Hanson** 13:43 Because you want to cut that. You don't want to just say, answer that top-line question of how many players have reached level 3. You want to say, okay, but what about in America? What about with certain device profiles? What about in the intersection of these dimensions, you know?
**Jason Plumb** 14:00 So if you're omitting the full fidelity telemetry, then you can decide what's important after the fact without having to redeploy your app.
**Martin Kuba** 14:08 Yeah.
**Jason Plumb** 14:09 Yeah.
**Martin Kuba** 14:09 And, like, I think, you know, like, I guess, like, the thing that I've been struggling with is, like, I hear people say, like, well, what if I don't have control over this in the backend?
You know…
**Jason Plumb** 14:20 I didn't… what did you say, Martin? I didn't catch it.
**Martin Kuba** 14:22 Sorry, like, so I… like, if people say, like, well, what if I don't have control over this in the backend?
**Jason Plumb** 14:29 Right.
**Martin Kuba** 14:30 you know, I don't have a collector, or I don't have control of the collector, My guess is that, like, most vendors will handle this correctly. Or, like.
will support this in some way, you know, like the aggregation across… across… in a lot of different instances of the client. So I don't know if it's a real… how real this… this is, like, for… for people out there.
**Jason Plumb** 14:55 I think most… I think most time series databases will struggle with high cardinality still.
So if you don't have control over it, I think you're just gonna explode your database.
**Martin Kuba** 15:08 Sure, yeah.
**Jason Plumb** 15:09 So then the solution is to drop the data, but you can't drop the data that I think you've got maybe even larger problems.
**Hanson** 15:17 So…
**Martin Kuba** 15:19 Gotta answer.
**Hanson** 15:20 Oh, so I think, you know, if they don't have control, if basically their IT is saying, you have this collector endpoint that can take open telemetry, logs, metrics, and spans, we don't do any aggregation. Logs show up in a certain way, spans show up in a certain way, so we have to fit your thing into a metric.
they'll, like, okay, we can produce a metric, but I think what they're gonna get is just not what they want, or what they require. So unless what they require is that higher level top line. So even if you give it to them, and they do it.
They get the data. Hey, it's a metric, it's a dashboard, but it doesn't tell me very much. So, now, if that's enough, then, you know, case problem solved. It's a checkbox.
But I feel like it's one of those checkbox things, you know, in order to complete your implementation, rather than actually providing useful data. But maybe some people here are just for the checkboxes, and that's a valid use case too, I suppose.
So I think your approach sounds correct, Martin, to say, hey, sure, why not? But these are the limitations.
**Martin Kuba** 16:26 Yeah.
**Hanson** 16:27 You get what you get!
**Martin Kuba** 16:29 And one of the… one of the limitations that, that I think needs to be documented is… is… and I'm also, like, curious, like, what are your thoughts on this, is, so I've been talking to… I've been going to the entities, SIG, Because they're very interested how we're going to, you know, deal with, like, sessions, specifically as entities, right? So, like, entities that might mutate, right?
And because they end up on the resource, this has… this impacts the metrics SDK in a way that, like, it doesn't for logs or events or spans.
So they would, like… if he could just, like, sidestep the whole matrix things, then, like, we wouldn't have to, like, even have this discussion, but because… Because, like, some people are saying, okay, I want metrics, now we have to kind of answer this question of, like, how do you… if we want to send Send certain entities as resources, then… then, you know, what is… like, what should you do? And again, I don't know, like, how much of an issue this is in the backends, because I don't know, like, how many backends will actually take all the resource attributes and use them as dimensions, or in some way.
That's… that would have a negative impact, I don't know. But I would just, like, in the documentation, I would say, okay, like, if you want to use the Metrics SDK, Then create a resource without these These… these entities, right?
And then it's fine.
I guess.
**Hanson** 18:03 So that… I think that's where… so I haven't been to the metric… or the NND SIG in almost a year, probably, but when I was there, they talked about identifying and non-identifying, attributes within resources.
So, or with the entity resource providers. So, if we're trying to model a session ID, as, a resource, is that going to be identifying or non-identifying?
**Martin Kuba** 18:29 Well, the session ID would be identifying.
**Hanson** 18:32 Which is… makes it incompatible with, with metrics. So these two, if you put it together, entities, session entity plus metrics SDK equals high cardinality, that… that is a non-starter. So that, you could basically say, you can't do that. So basically, if you support If you want to use the Metrics SDK, cool, but make sure your entity is low cardinality.
**Martin Kuba** 18:53 Yeah, yeah.
**Hanson** 18:55 Which means there's no session. And they'll be like, I can't get session metrics? Yeah, I know.
I've been saying that.
**Martin Kuba** 19:02 Yeah. So… But does that even make sense, though? Like, session metric? Session metrics?
**Hanson** 19:08 it makes sense in the sense that you want to know what the, I don't know, frustration rate for a particular session is. And that is tracked as, like, an every 15 second, you know, I don't know, polling, or whatever it is.
I could see that being useful.
But I could also see that being not compatible with the current no-tel metric setup.
So, I would say that's even, frankly, more useful than using hotel metrics for client-facing apps right now.
But, you know, that's… they're all valid in some way, and I would say this is more valid, more, like, more useful, but it's just not possible right now. So…
**Martin Kuba** 19:54 Ma'am.
Yeah, I guess, I guess what I meant is, if you, if you were generating metrics for each session, you'd have, like, thousands, thousands, or, you know, tens of thousands time series, like, I don't know, like, how… That's not… I don't think that's what you want.
**Scott Solmonson** 20:16 That's not exactly a metric anymore, isn't that, conceptually just, I'm capturing information in a single trace?
A single session.
**Martin Kuba** 20:24 Yeah.
**Hanson** 20:25 Board events, or… yeah, yeah.
**Scott Solmonson** 20:27 More events, yeah.
**Hanson** 20:27 But I think people want it… they look at, like, counts, and they look at rate, and they immediately see metrics. So it's another one of those things where it kind of smells like it fits, but it doesn't super fit.
So, no, you're completely right that, you can have a dashboard, you know, for each session.
And people say, yeah, for rum, I do want that.
But it doesn't make sense, if you look at it, you know, as a whole.
So, client metrics is a different, different beast.
**Martin Kuba** 21:06 No.
**Hanson** 21:08 Much more suitable for events, for a hotel, if you can do it, so…
**Martin Kuba** 21:12 Talking about sessions, like, do you, in Android, do you right now send session ID as a resource attribute?
Yeah? No?
**Jason Plumb** 21:20 No, it's a… it's a telemetry attribute.
**Martin Kuba** 21:23 Okay, are you… do you have plans to… to change that?
**Jason Plumb** 21:27 Yep. When… when entities stabilizes, maybe.
And when there's spec around session, maybe.
But it's hard… it's hard to think about doing… Drastic changes like that without a little bit of spec support first.
And I am not trying to drive that presently. If someone else wants to drive that initiative forward, meaning doing code-level prototyping at the same time they're doing spec work, then I support that, but I don't have the… I don't have the cycles for it right now.
**Hanson** 22:02 I thought I did a year ago, and it keeps… Like, be more, like, wishful thinking, because it does take… a wide… swath of changes. With entities, at least now, there's something there to basically say, hey, you know…
**Jason Plumb** 22:17 Where is the entity spec these days? It's not stable yet, right?
**Martin Kuba** 22:21 It's not stable, no.
**Hanson** 22:24 Besides Java, is there another implementation?
JavaScript, I guess, maybe?
**Martin Kuba** 22:29 I think JavaScript had a prototype also.
**Jason Plumb** 22:31 Yeah, I think Java only has a prototype.
**Martin Kuba** 22:33 Yeah.
**Hanson** 22:34 Oh, okay.
**Jason Plumb** 22:35 I think I did one of them.
**Hanson** 22:37 He did. A while ago.
**Jason Plumb** 22:38 A while ago.
**Hanson** 22:42 I think what… once the prototype is in, it's relatively trivial. Like, right now, the only thing the session exists is the ID. And really, it's the session in which the span started. It's not… session. Spans and sessions, so, you know, whatever. So, like, the final hookup is probably the easiest part. It's defining everything else that's the harder part. It's like… We already have what it, you know, in the session ID has a semantic convention, so… and we have previous and next, so… The building blocks are getting up there.
**Martin Kuba** 23:20 Yeah, I mean, I… I guess, yeah, I guess I'm not, like, less… I'm the most… the thing that I'm most interested in is just putting that session ID in the resource attributes.
you know, I don't know about the other stuff yet, like, sending events, or, like, how the SDK is gonna look like, or, like, what… like, what the plumbing is gonna be in the SDK for this, but I just wanna, like, get the data model… modeling right.
**Jason Plumb** 23:53 Yep. Yeah, we've always… I mean, that's… I'm still with you on that, for sure. We've always wanted it to be a resource attribute. The fact that it was immutable was the problem why we couldn't do it.
**Hanson** 24:05 That hasn't changed, right?
**Jason Plumb** 24:07 It's complicated, right? Depends.
**Hanson** 24:11 Like, right now, with entities, are we saying if you support the entity spec, then you can mutate?
Certain resource attributes are declared via entity providers.
**Jason Plumb** 24:20 So, Martin, correct me if I'm wrong, since you've actually been paying attention to this shit, but last I checked, you can set… you can… there's an API now to change a resource attribute, and when you do that, it produces a new resource. So the resource is still immutable.
What you get then is a changed, a different instance of the resource with new stuff on it. That… which means, or implies, that all of the users of that resource will need to start using the new thing if they care about the change.
Is that still the case, Martin?
**Martin Kuba** 24:54 So I'm not sure… about, like, so, like, I would just… I know that the thing that has been merged… Recently is… Isn't… is the for entity method.
On the provider, so you can call, like, specifically for the metric.
Metric, like, meter provider.
You can, you can call forEntity on it.
Give it an entity, and then it returns a new provider.
With the updated resource.
**Jason Plumb** 25:28 So you mutate at the provider level.
**Martin Kuba** 25:31 Yeah.
**Jason Plumb** 25:32 Right, so anybody who's holding a tracer, for example.
If there's instrumentation or whatever that's just holding a tracer and making traces all day long.
And someone goes and changes the entity, it'll never see that change.
**Martin Kuba** 25:45 No, not that… yeah.
**Jason Plumb** 25:47 It would need to go and fetch or be aware of changes to its underlying tracer provider so that it can get the new representation.
**Martin Kuba** 25:55 Yeah.
**Jason Plumb** 25:55 It's a far… it's… so it's a… at least in Java, it's where I kind of ran out of steam, was that it's a… it's a pretty far-reaching change to expect every single component that touches those providers to be able to sort of be aware enough to refresh its instance to pick up changes.
Hanson has this horrified look on his face.
**Hanson** 26:19 Well, I mean, it just means… it's dynamic in the sense that any new providers going forward, it's dynamic. That's right, that's right. But if you don't backfill, you can't really do that. Like, a session has to be, you know.
synchronous change for all providers and all resources. Resources then become dynamic. You basically have to cut your payload when there is a shift. And transitioning sessions is a very interesting use case, because race conditions abound. So…
**Jason Plumb** 26:56 I think there was… I think the API to account for that was, like, a listener pattern, or some sort of observer pattern, where you can, like, get notified that the thing has changed, and then you can refresh your instance. You're… yeah.
**Martin Kuba** 27:07 So, actually, so I have, like, a quick prototype for this, like, if I can show… show you the.
**Jason Plumb** 27:12 There you go.
**Martin Kuba** 27:12 If you have time.
**Jason Plumb** 27:14 We got 7 minutes.
**Martin Kuba** 27:15 settlement, so…
**Jason Plumb** 27:16 an empty agenda.
**Hanson** 27:19 Oh, yeah, let's just take a look at the code.
**Martin Kuba** 27:22 So the only way that I could… the only direct thing to solve this is, like, Is to, have… So, like, we have the… we're gonna have this package for the SDK, and the SDK can do the plumbing, but the SDK would… essentially, when it's instantiating the… something like the logger provider, it would have… It has… it would have, like, its own, like, entity-aware provider.
So, which has… which has… which is actually, like, a proxy pattern. It… it, it, like, delegates to, like, internal, like, instance of the actual provider, and when you call, like, setEntity on it, it, it rebuilds this… this delegate provider behind the scenes.
Right? Like, and it uses, like, this, So one thing that, like, the entity stick has done, they provided… they worked on… Defining the algorithm for merging.
resource attributes, like, if there's a new entity, like, how would you rebuild the resource? So that's… That's, like, the… that's what I'm using here, like.
**Jason Plumb** 28:30 Yeah.
**Martin Kuba** 28:30 into the resource, and then you create a new logo provider.
And then all the instrumentations that have instances of a logger, they actually have instances of this proxy logger, which… then they don't have to update it, like, they just keep holding on to the same instance, and then when they call emit.
Then, you know, it just delegates to the logger from the new logger provider.
**Jason Plumb** 28:54 So, Martin, I have a to-do list, and literally the very last thing that I've put at the bottom of my to-do list, not on purpose, it's just ended up there, is to prototype this same pattern in Android.
**Martin Kuba** 29:06 Okay, nice.
**Jason Plumb** 29:09 I think we talked about it, but it's been months, I think.
**Martin Kuba** 29:12 Yeah.
**Jason Plumb** 29:12 It's just…
**Martin Kuba** 29:14 That's good to know that, like, you're… you're thinking the same.
**Jason Plumb** 29:17 Yeah, yeah, I think… I think there's a… I think there's a path for it. I think it's actually not that… Bad?
But, you know, until we get in there and see how it feels, I don't feel that strongly about it yet.
**Martin Kuba** 29:33 Yup.
**Hanson** 29:33 Can we actually make the resource, instead of, like, a created instance when we, you know, instantiate a provider, can we basically make a resource provider and dynamically create it, as needed?
So, basically, we push this down one further level. So, the proxy would be the resource provider.
And all the other… the alts… resource.
Loggers and logger and span providers will basically have, like, a resource provider injected into it, and then that's what, like, every time you cut a new envelope, you create an instance of the resource.
Instead of saying, you know what, we already have it.
**Martin Kuba** 30:17 Yeah, I just don't know, like, if the… like, I guess the… I don't know, like, if the SDK… sorry, like, yeah, like, the JavaScript SDK, or, like, the Java SDK would allow you to… to just, like, use, or just replace the resource in…
**Hanson** 30:32 Whoa.
**Martin Kuba** 30:32 local provider.
**Hanson** 30:33 It won't. This prototype will basically be hacking the SDK itself.
**Martin Kuba** 30:39 Okay.
**Hanson** 30:40 Because it feels like if you're saying providers' resources are dynamic, then there needs to be a way of like, to say, hey, just listen through a pattern everywhere. It's so fundamental in how resources… it's altering the lifecycle of a resource. I think it needs to have fundamental changes baked into the SDK.
It feels like. We can certainly make it work without it, with a similar pattern, like, with the proxies, but it feels like a… glossing over something that fundamentally should be part of the SDK.
**Martin Kuba** 31:13 Yeah, and that was, like, when I was talking to, What about this? Like, we were talking about this in the entity SIG. That's, like, Josh, Josh Surath.
That's kind of, like, the conclusion that he came to, like, that we should just have our own, like, client… client SDK spec.
**Jason Plumb** 31:30 Awesome.
**Hanson** 31:33 So this is not a problem for backends. They're okay with providers basically snapshotting the resource at creation time.
**Martin Kuba** 31:43 Yeah, I guess, that's what they're saying.
**Jason Plumb** 31:45 I think that's just been the status quo forever.
Yeah.
It was like, you have your setup phase, you determine the… Source of all telemetry, and then you go with it.
**Martin Kuba** 31:56 Yeah.
**Jason Plumb** 31:56 And it doesn't change.
Until you restart.
**Hanson** 32:00 But I… So I thought adding entities and making the resource dynamic, part of it is… is… altering the life cycle of the resource. But it seems like it… it turned into a papering over,
**Jason Plumb** 32:15 No, I think… no, I think you're accurate. I think… I think the resource is dynamic, but it's not mutable, right? Those are… those are different things. And there's now, during the lifecycle of an application, there's more than one resource. If you're… if you have entities built, you will have more than one instance of the resource over time.
**Hanson** 32:33 So, at instantiation time, a provider has an instance of a resource. So, if it's mutable, then you can change properties on it. That's bad. But… Dynamic means the relationship is not hard-coded at the instantiation time, that could be replaced. Or is that considered mutability? Like, for replacing the object? I guess, effectively, it is, so maybe this is by design?
**Jason Plumb** 33:09 You'd have to defer to the entities, Sig, for an answer on that one, I don't know. I mean… Yeah. I think you've described it accurately, I just don't know if that's the intent. It feels like it is, yeah.
**Hanson** 33:21 It must be, it's been a year, so they must have combed over the same… every new person comes in and asks the same question.
Probably.
**Martin Kuba** 33:28 And, like, I… I don't know enough either, like, I… Like, I didn't quite understand how this four-entity pattern that they introduced in the spec, how… like, what use cases exactly it solves, other than, like, it allows me to… To start reporting data on… On something that's… on a new resource, essentially.
But… but then you have, like, two separate providers, like, happen, like, you know, running at the same time now. So, like, how is that… you know, like, what is that managed? Like, what if you… like, you know, like I was saying, like, for clients, like.
this doesn't help us, like, this seems like if you had a single instrumentation that was creating its own provider, like, sure, but, like, if you wanted to have it, like.
globally, then… You know, how does that help us, so…
**Hanson** 34:26 So basically, with this pattern, every session change would have to reset all the providers. Or do something like what you did, which is proxy, or use a delegate that will have the correct one. Yeah, totally.
**Jason Plumb** 34:39 That's… I mean, that is the… I think that is the design right now.
**Hanson** 34:43 That's… It's so clunky at a fundamental level, which is… like, I think I understand special use cases, needing to have some clunkiness, but this is, like… fundamental.
**Jason Plumb** 34:56 Like, and if it's not plumbed correctly, there can be huge areas of your app that don't see the changes. That's the… that's the thing that I keep sticking with.
**Hanson** 35:04 Yeah, exactly.
**Jason Plumb** 35:07 Okay, I gotta go.
**Martin Kuba** 35:08 Yeah, right.
See you.
**Jason Plumb** 35:10 Come on, I think.
