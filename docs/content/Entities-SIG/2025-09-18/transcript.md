SIG: Entities SIG
Date: 2025-09-18
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/fPYknKiH7mVISDLhJgITug6E8W5z2i2Bot1WfimOKaUlfvC2jfQ_HWbTwfWZs6CQ.FSuDlHAfrex8WyFT
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:56 Hey.
**Daniel Dyla (Dynatrace)** 01:04 Morning.
**Josh Suereth** 01:05 How's it going, man?
**Daniel Dyla (Dynatrace)** 01:07 Good, you?
**Josh Suereth** 01:08 Not bad, not bad. I,
It's been a busy time here.
So… I'm still…
**Daniel Dyla (Dynatrace)** 01:17 Hopefully busy in a good way.
**Josh Suereth** 01:19 I… I would… I would always rather be busy than bored.
**Daniel Dyla (Dynatrace)** 01:23 Huh.
**Josh Suereth** 01:28 So…
Yeah. I have a little bit of travel coming up, and then, KubeCon. I was booking travel for that.
So…
**Daniel Dyla (Dynatrace)** 01:35 Oh, you are going to KubeCon. I'm not going this time.
**Josh Suereth** 01:41 Oh, I'm sorry, I have family down there, so, like, it's a short hop, and then I get to actually see some of my extended cousins and things that I haven't seen in a while.
**Daniel Dyla (Dynatrace)** 01:51 Oh, that's cool.
**Josh Suereth** 01:52 Yeah.
So… Sorry, we'll miss you, man.
**Daniel Dyla (Dynatrace)** 01:57 Yeah.
I, I always go to all of them. This would be the first one I've missed in a long time.
**Josh Suereth** 02:03 I'm surprised you didn't decide to just bike down.
**Daniel Dyla (Dynatrace)** 02:08 I'm doing a… I got a bike race this weekend.
**Josh Suereth** 02:11 Yeah.
**Daniel Dyla (Dynatrace)** 02:12 A little bit shorter than from here to Georgia, but…
**Josh Suereth** 02:15 There, there is a trail, isn't there? Can't you, like, Appalachian… no. The Appalachian Trail isn't bikeable. Is there, like, a rail.
**Daniel Dyla (Dynatrace)** 02:22 Oh, there's.
**Josh Suereth** 02:23 Like, up and down the states, yeah.
**Daniel Dyla (Dynatrace)** 02:25 There is, yeah, there's a… there's a trail that… I mean, there's a… there's a lot of linked trails that you could do it if you really wanted to.
**Josh Suereth** 02:34 Yeah.
Well, anyway, let's get started. If it's just you and me, the meeting… you and I already talked about the meeting times.
That's why I decided to raise it. So let's talk a little bit about the OTEP.
**Daniel Dyla (Dynatrace)** 02:51 Okay.
**Josh Suereth** 02:51 And then when people join, we can dive into more things, so…
**Daniel Dyla (Dynatrace)** 02:55 Alright.
**Josh Suereth** 02:56 Yeah, let's cover what was changed in some of the open comments. So, first off…
Oh, this is the change about how things are fundamental with trade-off and mitigation. I left this open for us to talk about today. I added some backwards compatibility stuff, we'll talk about that.
Why is locking… oh, there's an example implementation in the spec. I'm thinking about just getting rid of it.
But I can leave it there. It talks a lot about how to do synchronization and primitives, and I think all of it is now in the description above.
But… and I'd rather link to real prototypes than, like, the pseudocode? I don't know.
What do you think?
**Daniel Dyla (Dynatrace)** 03:44 Yeah, I think that that's a better idea.
**Josh Suereth** 03:47 Okay.
**Daniel Dyla (Dynatrace)** 03:48 Because not all implementations even need locking, like, there's no locking in Node.js, for obvious reasons.
**Josh Suereth** 03:54 Yeah, all the locking is in your platform.
**Daniel Dyla (Dynatrace)** 03:57 Huh.
**Josh Suereth** 03:58 Yeah.
Okay. And then, what was the other one? Oh, complaints about the pseudocode syntax of choice.
Okay, so let's see. This was another problem with stable spec, about how do we resolve stable. I'm gonna walk into that in a little bit.
Especially real use amount of analytics, this proposal.
And its analysis mixes to potentially several different things. Truly immutable resources, and mutable states of the device.
Making resources mutable does not solve the inadequacy of the OpenTelemetry model for ROM and analytics Realm.
Mutable state requires different handling than resources on several levels.
Does the state mutate? But it can also be different for different concurrently running bits of code, background thread, yes. This, this actually goes into some of the discussion you and I had,
This is why I'm actually thinking…
I'm starting to really question… I still think we want resource and entities together, but mutable resource, I'm starting to question whether we want to go a different route with entities and scope.
**Daniel Dyla (Dynatrace)** 05:09 Yeah, I've been thinking about it a little bit more over the last week, and, like, more people have been raising the… the braking,
You know, the idea that this is a breaking change,
to allow resource to be mutable. If we…
Like, the resource as it is defined today.
What we were trying to capture is essentially what we are now trying to capture as identifying entity attributes.
**Josh Suereth** 05:44 Yep.
**Daniel Dyla (Dynatrace)** 05:46 which shouldn't mutate. I guess maybe you could add or remove an entity, But…
Generally, they should be stable over the lifetime of the entity.
**Josh Suereth** 06:01 Well, and it doesn't solve… like, to this… to this question here, this doesn't solve the need of, like, oh, I have a background thread that's running with resource A, and then I have something else which is actually activity, you know, A and activity B, and I want to report them both from the same frickin' SDK. How do I do that? Like, it doesn't actually solve that.
So, the more… the more I've gotten into this, and I hate to do this again, I… I actually think that we should…
I'm okay spending more time on the entity provider. I… you can look at my… my, PR on…
mutable resource. I… I think I'm changing my opinion here.
we can… we can… I'll walk through… I'll walk through some of the stuff I wrote.
But yeah, we'll walk through the counterproposal in my straw man, and we can discuss what we think. So if we look here at what was changed, some of this might be the same no matter what, but effectively, where do we have? That's the API for entity things. Okay.
Entity provider creation, right? We have this explicit notion of creation of an entity provider. You give it a set of resource detectors, and you give it an initialization timeout for when to abandon and say, cool, I need a resource no matter what. I'm done figuring out who I am.
you have to allow, initial resource detection and creation, but we should not block other SDK providers from initializing. This is, like, the JavaScript use case, or Node.js. Alright.
what I added… Was, upon failure.
To detect within a timeout, right?
A resource should be constructed and made available.
Get resource operations must be unblocked, and onResourceInitializationEvent must be fired to all event entity listeners.
The call must provide the failure status of, like, what happened.
So that you know that, that, like, entity or resource wasn't fully initialized, here's why.
That would be an update, I think, to JS, but I'm guessing you already have something like that?
**Daniel Dyla (Dynatrace)** 08:17 Yeah, I mean, yes, it's… we have a similar mechanism,
I wish I could share the prototype. I haven't pushed it any… I haven't pushed the latest version anywhere. I'll… I'll do that today, so that we can talk about it more intelligently. But, sure. Yeah, that's not… that's not all that different than what I have.
**Josh Suereth** 08:38 Let me grab, then, the entity listener, wherever I defined that. We have onResourceInitialize, onEntityState, onEntityDelete, right?
If we were to get rid of mutable resources, I think this would be the only message that gets sent.
In the prototype, if we keep things the way they are now, but we might not…
We… anyway, we might be able to do something different, too. The difference that I added here is onResourceInitialize sends the resource and a status.
Of resource initialization.
**Daniel Dyla (Dynatrace)** 09:08 So… The status would essentially be success, failure…
**Josh Suereth** 09:12 Yeah. Time.
**Daniel Dyla (Dynatrace)** 09:13 Yeah, okay.
**Josh Suereth** 09:14 What I did for the Java prototype, because sending status is annoying.
And they don't have, like, a status type I could just reuse. I have two methods. One that sends the resource, one that's… I have onResourceInitialized and onResourceInitialized with failure.
as, like, two separate methods in JavaScript, and I feel like that still abides by the spec and is not a problem, right? It's… because it's the…
Spirit of the spec.
**Daniel Dyla (Dynatrace)** 09:43 Yeah, I think it's fine.
**Josh Suereth** 09:45 Yeah, but just, just if you were… oh, shoot, you know what, I didn't push that either. That's in my local…
That's in my local changes. I should push that publicly so you can look at it, but that's how I implemented this when I went to do it.
Alright, other things that were added, so we call out the two states of entity provider, and then on creation…
That was all this…
Calls to get resources are blocked until it's completed with the timeout. We have add or update, what else do we add? It is down further.
the SDK changes. We have the open question on how to deal with metrics on mutation, and honestly, that has been a quagmire of hell.
I think that I… I want to put the straw man proposal up before we go into details of what that looks like, because I didn't update the spec at all, it's really ugly, what I've implemented.
But the thing I want to talk about is this trade-offs and mitigations, right?
So this change on the surface breaks a key assumption in the resource SDK. A resource is an immutable representation of the entity producing telemetry as attributes.
It allows downstream consumers the resource to treat attributes as a fingerprint for identifying origin of telemetry, streamlined joins, etc, etc. This change also impacts the Go SDK.
However, as we control the implementation, we as designers have options for how to prevent this from breaking the Go SDK. Go actually uses the fingerprint of resource, like, in its own implementation.
directly.
**Daniel Dyla (Dynatrace)** 11:24 Okay.
**Josh Suereth** 11:25 I think others… don't in a way that would break them, at least not in Java.
Okay, anyway, we expect the impact of immutability change to have limited impact, right?
As only new instrumentation and features, like browser-based instrumentation.
would be expected to leverage the mutable capabilities. Existing working OpenTelemetry setups should not break, and the design of the entity provider and entity in the protocol has been crafted to avoid the most breaking change possible.
However, it's still fundamentally a change.
Right? So here's what we do.
We have two-phase rollout. We have an opt-in behavior to the breaking change. So the idea would be, we roll this out where in phase one.
Entity shows up in resource, but you cannot mutate resource without some of opt-in flag or configuration.
Like, that behavior is completely opt-in.
Meaning, by default, if I upgrade OpenTelemetry, I will not have mutating resources, and I cannot break. A user has to take some configuration action to see that.
We would also notify everyone of this change and say, hey, by the way, resource is now immutable, deal with it, right?
And then in Phase 2, after we feel like enough change has happened in the ecosystem and it's no longer a assumption that resources are immutable.
We would allow… We would allow the mutation to be done without some kind of flag or opt-in.
**Daniel Dyla (Dynatrace)** 13:01 Okay.
**Josh Suereth** 13:03 I, you know… I feel like we're gonna have something like this regardless of what we do.
**Daniel Dyla (Dynatrace)** 13:10 There, yeah, there's gonna have to be something like this, because it is… you know.
We have to control, you know, the braking change, essentially, to make sure we don't… Break people.
**Josh Suereth** 13:24 Yep.
**Daniel Dyla (Dynatrace)** 13:24 And allow them to… Choose when they take that on.
**Josh Suereth** 13:29 Yeah.
Alright.
Let's…
Let's go to your straw man.
Alright, so here's the fundamental things, right? Resource… remains immutable.
After initialization. So we keep the initialization stuff we had before, okay?
**Daniel Dyla (Dynatrace)** 14:01 Okay.
**Josh Suereth** 14:02 Where we allow initialization to be somewhat asynchronous, and we update the spec to have that, because we need to account for that, no matter what.
Okay. Second thing is, scope.
now allows… Entity Ref.
I don't know why I'm making that all caps.
It's like I'm yelling at you. Hold on. Notation scope now allows entity ref.
And entities for its attributes.
We might even, just for instrumentation scope, want to put entities in directly.
when dealing with mutable, entities in OpenTelemetry.
We passed them in… I'm grabbing meter… Tracer.
Logger.
etc. So this would be, I would have, you know, meter provider.
P equals blah blah blah blah blah… This discovers… the immutable… resource.
And then I would have p.getMeter, 4… You know, meter name.
And then I would have entity.
Session, you know?
**Daniel Dyla (Dynatrace)** 15:30 Yeah. Okay.
**Josh Suereth** 15:31 Try to avoid using real syntax there? Yep, I gotcha.
Yeah, this register, or this, obtains…
A scope that will report against a mutable entity.
That entity is considered bound… Internal…
scoped to the immutable resource entities. Okay.
Yeah, so something like that. So the… basically, you know, if I'm reporting against a session, I can get a meter… if I just get meter, it's against the baseline resource. If I say get meter 4, or whatever the hell we want to call this, it would be a meter against a specific entity, like a session.
And I would have that for Tracer, I would have that for Logger, it would just be consistent everywhere. So this, this expands instrumentation scope to include entity ref.
And it gives us the capability where now, the user
is kind of telling us about these things. We already have dynamic allocation in our spec around, scope.
Right? So, for meter, for example, if I pull a different scope, I get a different area of memory where I record metrics, and I report against that scope, and there's a set of attributes for them, right? So…
if I have a mutating entity, I would have a scope that has that entity in it that I would report metrics against, and have another scope where I report metrics against it. The problem we have here is we don't have scope cleanup.
So the last thing would be…
We need a way to allow scope cleanup.
When… An entity is killed.
The instrumentation scope.
Needs to be cleaned.
For example, flushing.
Or, yeah, removing… in memory storage metrics. I feel like for…
Traces and logs, because we're using a, a buffer pattern, generally.
With our processing pipeline, there isn't really anything to clean up.
**Daniel Dyla (Dynatrace)** 17:58 Yeah.
stateless.
**Josh Suereth** 18:01 Yeah.
**Daniel Dyla (Dynatrace)** 18:02 There's another problem here, which is that when the instrumentation gets the meter for the session.
Now the instrumentation needs to… Pass an entity, where does it get that entity?
Like, that it has to either construct its own entity, or…
We need a way to query the entity…
Provider for a particular entity by its name or type.
Yeah. And… I think that… and, you know, what if it's not resolved yet?
I think there's complexity there, especially since none of our other APIs, you know.
We typically don't have the ability to read data back out via the API and instrumentation.
So…
**Josh Suereth** 18:57 Yes.
**Daniel Dyla (Dynatrace)** 18:58 You know, if you construct a session entity and construct it slightly differently than your session detector, you know, than something else.
**Josh Suereth** 19:11 So today, though, in our API, you could construct a instrumentation scope and put session ID as an attribute on it.
Like, that's a thing you could do today, which is what you're saying is.
**Daniel Dyla (Dynatrace)** 19:22 Yeah.
**Josh Suereth** 19:22 Like, legitimately, this… this is something I can already do today, I'm just not using entities for it.
**Daniel Dyla (Dynatrace)** 19:35 Yep, that's true.
Let's see…
**Josh Suereth** 19:44 The other thing I'll call out with this proposal is, the profiling SIG?
Actually, I don't know if you saw what they were trying to do to our protocol buffer?
But they actually had this notion of hierarchical resources that you report against for profiling, that we said, no, no, you can't do this. But they wanted to have a, like, a resource proto where then, like, a profile would be, like, a sub-resource from the proto.
Their example is they're using eBPF, right? So there's a, like, a process somewhere on a Cates node, and it's watching the other processes. So that process is the resource, but it will report profiles on behalf of all the things it's looking at via eBPF.
And so they want its resource to be the thing that's reported, but then when they report a profile, they want it to be against the resource that is the process it's inspecting.
And they want to share information in their batch.
Kind of aggregate.
So this actually gives them a way forward as well.
**Daniel Dyla (Dynatrace)** 20:53 There are details we would need to worry about, like what happens if… You get a meter for…
An entity that already exists in the resource, versus…
doesn't exist in the resource? Like, do those behave differently, or do they… we just pretend it's okay and report them in both places, and let the backend deal with it?
**Josh Suereth** 21:21 Yeah, let me add that as another thing to talk about problem.
What if the scope wants to record a human resource, or an entity?
That is already in the resource.
Yep.
**Daniel Dyla (Dynatrace)** 21:38 The instrumentation scope… currently does not have resource, right? It only has attributes?
**Josh Suereth** 21:46 It only has… it doesn't have entity, it only has attributes, yeah.
**Daniel Dyla (Dynatrace)** 21:50 And it also does not have its own resource, though.
**Josh Suereth** 21:54 Instrumentation scope is attached to resource, so if we look at,
Here. I… I don't know if this works for other people, maybe I'm too deep in the weeds, but I think in terms of our proto.
So, if we look at, you know, let's pick Trace.
The way… the way everything works is trace data is a set of resource spans, resource spans is a resource, and then scope spans.
And then instrumentation scope is in scope spans, where it's a set of spans attached to a scope.
So implicitly, what this means is the scope is attached to a resource.
So what we would have.
**Daniel Dyla (Dynatrace)** 22:37 Got it.
**Josh Suereth** 22:37 We have entities at this level.
That denote the immutable set of information. And we would have entities at this level that would be the mutable pieces of information, or that change within the resource, but are still somewhat identifying, or that you need to join against, that are, you know, beyond just a span or a metric, or things like that.
**Daniel Dyla (Dynatrace)** 22:59 Got it, okay.
**Josh Suereth** 23:05 And then… If you want to see… I think Instrumentation Scope is actually in here for some reason.
It doesn't have its own… Yeah, it's right here.
It just has a set of attributes.
And so I'm suggesting we could just put entity ref in here as well, the way we did the resource.
**Daniel Dyla (Dynatrace)** 23:32 And reference those attributes.
**Josh Suereth** 23:34 Yep.
But then the API would be just provide an entity wholesale. So the API you use in instrumentation is, give me an entity.
I know, for example, this literally broke Java. I don't think Java actually supports it at all yet.
So I'll have to figure out how to make them support it, but if I support it via…
**Daniel Dyla (Dynatrace)** 23:56 or anybody.
**Josh Suereth** 23:57 It'd be so much better.
**Daniel Dyla (Dynatrace)** 24:00 I'm not sure anybody actually supports it yet.
**Josh Suereth** 24:03 There's… the collector does, and there's something… there's a few things. When was this added?
Where's the blame button? Let's take a look.
**Daniel Dyla (Dynatrace)** 24:14 Dude, that had it a long time ago.
**Josh Suereth** 24:16 Yeah.
This is the OTEP. This is what I was looking for, so…
You know, short name. Oh, this… that was… that was the one. Oh, God. Yeah, I remember that. Okay. Differentiating the type of data emitted from scopes that belongs to different data domains. For example, profile and data emitted as log records, or client-side data emitted as log records needs to be differentiated. So you can be routed and processed differently in the backends. That is…
Make scope consistent with other things. ResourcePan, yeah.
This is not quite the use case that we have in mind here.
I feel like it's in line with it slightly, though.
**Daniel Dyla (Dynatrace)** 25:10 Yeah, it's… it's at least related.
**Josh Suereth** 25:13 Yeah.
**Daniel Dyla (Dynatrace)** 25:17 So… but it, like, I assume there were prototypes done for this, so what languages were the prototypes done in?
**Josh Suereth** 25:25 This one might… what year was this? 10 months.
**Daniel Dyla (Dynatrace)** 25:30 It was 3 years ago.
**Josh Suereth** 25:33 Oh, win rate.
**Daniel Dyla (Dynatrace)** 25:34 is just a warning. It was 3 years ago.
**Josh Suereth** 25:37 Yeah So, I think, I think that this, this,
This predates when we force prototypes.
**Daniel Dyla (Dynatrace)** 25:46 Yeah, so the reason I'm asking is because I know this isn't implemented in JavaScript, you just said it's not implemented in Java.
I… I don't know if there are any SDKs that have actually implemented this.
**Josh Suereth** 25:58 I should say, I think it's partially implemented in Java, it's not implemented in some key things, yeah.
**Daniel Dyla (Dynatrace)** 26:02 Okay.
**Josh Suereth** 26:03 Yeah, well, this is our opportunity to implement it.
**Daniel Dyla (Dynatrace)** 26:08 Well…
**Josh Suereth** 26:08 So it's our operator.
**Daniel Dyla (Dynatrace)** 26:10 It's an opportunity to implement it, but it's also… we don't have the same constraints we did on the top-level resource in terms of backwards compatibility.
Yes. So we could just have an entities, like a repeated entities field, and call it a day.
**Josh Suereth** 26:25 That's actually kind of what I'm thinking, too. Like, just, literally, we could put straight-up entities on there, yeah.
should I put this together as an actual OTEP? What do you think?
**Daniel Dyla (Dynatrace)** 26:45 I… Think that this…
that it would be a good idea. I guess the question is, is this more work Versus just…
Convincing people that mutable resource is okay, or that the level of mutation we have in resource is okay, and are the use cases that this unlocks worth
The pain of going, not all the way back to the beginning, but certainly back a couple of steps.
**Josh Suereth** 27:14 True.
**Daniel Dyla (Dynatrace)** 27:15 I would say yes, but I'm not the one that is writing this OTEP and doing a lot of… you've done most of the work that would be backtracked on, so…
**Josh Suereth** 27:24 Yeah, no, so, from my perspective, what this might do, this might delay our ability to support the browser, but it does, it does three things that I like. One is, we could implement the SDK with entities.
and take, like, what we have here and turn it immediately into a spec PR, because we would no longer need an OTEP for entities, because we're not actually breaking things.
If we keep things immutable, right? We're just adding the boundaries with entities, so I think it unblocks spec work.
The second thing I like is the work… the hard, unanswered question in the OTEP today is what to do when a resource mutates with metrics.
Doesn't have that problem.
Yeah, it has a GC cleanup problem.
which, honestly, entity, you know, mutation had that problem too, but this unlocks a new set of use cases that I think are super valuable. It answers a lot of feedback on the OTEP with people who have legit concerns, and…
It…
It gives us kind of a first-class mechanism for understanding if someone is trying to store data separately for different… like, it gives us a multi-tenancy story, basically.
Where we can have… I'm collecting data on behalf of A, and on behalf of B.
And I can do that in the API.
That is something previously only the collector could do.
Or, sorry, I guess the API and SDK could do it, you just had to reinstantiate the API and SDK for every different resource you wanted to report against.
**Daniel Dyla (Dynatrace)** 29:02 Yeah, it just sucks to do.
**Josh Suereth** 29:04 Yeah.
**Daniel Dyla (Dynatrace)** 29:05 I'm sure there are people doing it, but I wouldn't want to.
I… Yeah, there are details to work out, but I think… Until we have an OTEP we probably…
can't really talk too much about them. Like, one of… one would be… what then goes in the top-level resource? Do we… do we…
put only… Like, the initialization attributes, or the initialization entities in there, and… Leave everything else off.
And maybe only the identifying attributes of the initialization attributes, making it, like, you know, moving us back to, this is immutable again.
**Josh Suereth** 29:49 I think… I think we can move back to Immutable. By the way, we're… we're out of time. I have another, like, 2 minutes, but,
I'll put… I'll put together my thoughts in the notes up. I think that's a good question. My… my straw man is still, resource actually remains immutable post-initialization, because keeping the identity stable is important for things like op-amp.
Or, like, the control of that resource. So, like, we need a stable ID that represents this thing. And so, resource is the stable ID, and we're creating this scope entity that can be for things that could mutate. And so, if I'm in, say, a phone.
The identifier of the phone itself might be my stable ID.
And then the session can be, you know, my, my mutating ID.
And that's how.
**Daniel Dyla (Dynatrace)** 30:38 They're…
**Josh Suereth** 30:38 Following these things.
**Daniel Dyla (Dynatrace)** 30:40 There are still… we still have to determine where to put things like…
the IP address, which is mutable, but it is not, like.
you know, your instrumentation isn't going to be reporting mutations of an IP address, it's going to assume that that's handled somewhere else.
**Josh Suereth** 30:57 Yeah, I think we can actually… that's why I think we can allow descriptive attributes and entities on resource.
Like, I think that's actually fine.
It's more than…
**Daniel Dyla (Dynatrace)** 31:08 mutate.
**Josh Suereth** 31:09 They might mutate behind the scenes, but the resource would never report them differently.
And we have the distinction between identifying and descriptive now, so if you're trying, like, if OpAmp today… and I think I put this somewhere where I talk about the problem with identity, but, like, op-amp today, collectors today, a lot of vendors today, don't look at every resource attribute for identity.
They actually pick and choose. So they're using, like, service instance ID. They're not using all of them, right?
Or they have some hard-coded, really complicated algorithm. So what we're doing is saying, cool, you already do crazy-ass things in resource because there's descriptive attributes in there. We're gonna make it standard. You can just look at the identified ones that are labeled.
That solves problem A.
We're still not going to change resource after we've initialized.
But if you have a different thread that's telling you things are changing, you can actually identify, okay, the instrumentation's out of date, but I have update information that the IP address is something different now.
You know, like, you can resolve that on the data side.
**Daniel Dyla (Dynatrace)** 32:11 Okay.
**Josh Suereth** 32:13 So, alright, I'll put the OTEP together, I think it's worthwhile. The more I hack on this, the more the SDK gets uglier and uglier, to the point I don't think anyone will accept my PR.
That's a sign to me that we've gone too far.
You know?
**Daniel Dyla (Dynatrace)** 32:28 Yeah, yeah, I mean, that's why you do prototypes, right?
**Josh Suereth** 32:31 Yep. Yep. Okay, cool. Alright, well, we'll see y'all next week.
**Daniel Dyla (Dynatrace)** 32:36 Yep, see you next week.
