SIG: Entities SIG
Date: 2025-09-25
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:50 Hey, you're welcome.
**Hunter Sherman (SolarWinds)** 00:59 Good morning.
**Josh Suereth** 01:32 Alright, so, sorry.
I was just catching up on something else,
If you aren't aware, and you're trying to use OpenTelemetry Go modules, we, we had an SSL cert die, so we're fixing that.
Yep.
That's fun. The problem with having two domain names and forgetting about one.
Yeah, so feel free to add your name, add agenda items. I think, I have a big topic I want to talk about, which, we mentioned briefly in…
Last week, we mentioned in the SemConf group, we had a discussion about it there, and then we talked about it in the spec.
So, cool.
With that, I might get started, because we only have 30 minutes, so… Welcome, everybody.
Alright, so first I'll just set the context, this is a new OTEP,
That, is basically a rethink as we were prototyping the existing OTEP around mutable resource. Effectively, the more I was prototyping
how the SDK would change from metrics, the more painful it got, to the point where I got to a point I don't think someone would accept the PR, even with cleanup.
So, in developing that PR, though, some of the infrastructure that I was building gave me an idea of an alternative that I think might give us what we need for the browser SIG.
and, still allow, you know, the same model that we need overall to accomplish this. So basically, in this OTEP, we're changing what we had before. So the previous OTEP was, you know, I have this notion of discovering a session entity, I grab my meter, or sorry.
Previous OTEP was, I grab my meter, I grab a histogram, I discover my session entity, I provide the session entity to the entity provider, and I record my latency. These two could happen, or sorry, these three.
Would happen, like, somewhere in line, right?
what we're changing now is instead, I need to get my session entity, grab a meter for that session entity specifically, so that the metric system can actually allocate the right set of memory.
and the right aggregation components for that entity, and understand that, okay, now I'm dealing with this session. And then I get my histogram and record my latency. So this is kind of a shift.
That's basically the TLDR. If we want to look at the details of what this looks like.
I will show… maybe we'll do this one?
We talk about the motivation's very similar, and then it also talks about the motivation for changing from the previous OTEP, and then the explanation. Basically, in this, resource will remain immutable.
resource itself. So we can still use resource to identify an SDK,
We will expand resource to have identifying attributes, which solves, like, the op-amp problem, where op-amp doesn't trust all resource attributes, and you can put descriptive attributes in resource, and everything's still gravy there. We can decide what to do with descriptive attributes, but effectively, immunability on resource means
the set of entities chosen, and the IDs of those entities.
Instrumentation scope would be enhanced with entity.
And, similar to resource, so I could, like, get a meter for an entity, and so if I have, like, mute, like.
identities that change or want to record information within the context of an SDK, I can do so. This actually gives us some multi-tenancy capabilities that we didn't have previously, or were super awkward, where we forced people to instantiate different SDKs completely.
So that's… that's… that I actually is, somewhat attractive as well. So, effectively, what this is proposing right now is, if entity X exists on instrumentation scope.
What that means is that I'm observing X in the context of the resource.
So, if I have a session in scope, and I have, like, a device in resource, this means that I am session X on device Y.
And that's what all my metrics and logs and things mean.
Okay.
There's a few open questions in here. I never wrote the introduction, my bad.
But effectively, every single getAsignalReporter operation, you insta… we… this is what it looks like today.
Attributes, by the way, is not well implemented across the ecosystem. And I think the system I needed to build in Metrics SDK to make
Mutable resource work is exactly what we'd have to build to make this work overall, and it's actually way easier if we do it in this mechanism.
Anyway, so going forward, there'd be an entities parameter. We can specify an entity.
Right. So that's the type ID description URL. Not a lot changes. The other thing I kept here, and we can decide if we like it, was an explicit resource listener and resource initialization to allow the async
initialization we need for JavaScript, and to make sure there's an explicit, like, I'm in startup mode and resource might not be done, and then I'm finished. And that there could be a failure if we allow async
async instantiation of resource, but honestly, like, because we have SDKs that have to deal with that, this just makes it explicit.
I'm happy to cut all of this, and somehow resolve this as bugs in the spec around async, that's fine too, it doesn't have to be, it doesn't have to match this, but…
Anyway, I did keep that. Alright.
The protocol change would be similar to what we did for resource. We could either add entity refs, or we could actually just create entities, because right now, a lot of people aren't filling out implementation scope attributes at all.
Sorry.
Yeah. Alright. Trade-offs and mitigations. Primary trade-off we're making around here is breaking changes and subtle differences. So…
One of the problems here is that we need to understand two instrumentation scopes are different because they have different entity data.
it's not clear if, people consuming OTLP are actually engaging with Attribute on instrumentation scope, where they would understand that there's a difference. If I… if I…
If I am correct, I actually don't think that's the case in a lot of scenarios. I know that Prometheus, it's not true.
Or it's partially true.
appropriately aggregating and finding data about an entity. If the entity is reporting instrumentation scope, then if we wanted to, like, aggregate across resources, it gets awkward, right? So that's a problem.
Prior art and alternatives, I call out some of the things we did with OpenCensus that just don't work in OpenTelemetry. You can look at that detail if you want, but it leads to a much, much, much, much uglier API, but way more flexibility.
And then semantic conventions, we already define an entity, we use it to report resource, but interestingly enough, in semantic conventions, when we say a metric has to be attached to an entity, we don't mention whether that entity would be on resource or instrumentation scope or anything. We just say it has to be associated with an entity, regardless of how that association occurs.
So this would not be a breaking change if, some of these entities are in scope and some of them are in resource for semantic conventions.
There's a few open questions here we can walk through, but I actually want to dive into,
One of the ques… one of the things from…
David Ashpole, let me spend two more minutes going through some of these open questions, and then we'll get into that one. But, you know, what safeguards does the SDK provide against high cardinality entities? This is a issue that we saw
today with our instrumentation API.
So, when we're observing, multiple tenant systems, like, where session changes, or if I'm observing, I have to, like… I think this was a, Apache Pulsar, where they were observing topics and subscribers, and subscribers could change significantly from, like, one report to another.
They ran into an issue where we would actually… exhaust memory from high cardinality
metrics and, like, tracking. So, we probably need to have safeguards in place where I can't just, you know, create a bajillion of these and blow up my memory. We might have to have garbage collection, that kind of thing.
What happens if an entity exists on instrumentation scope and resource simultaneously? The plan in this, OTEP that we can discuss more in detail is that this would be disallowed.
They have to be disjoint. If you want to… if you want to report session and instrumentation scope, it cannot be in resource.
So the idea would be that,
You can always collapse these things down to get a set of entities that you're talking about.
How do we represent entity and instrumentation scope? Again, I mentioned that above. We could decide to do something direct, we could decide to use the current entity ref tactic we have for, resource.
Are descriptive attributes allowed to change in resource? Again, it's not clear how we would do this or what we would do. Today, that might break,
That breaks the data model, but probably not anyone in practice. The proposal here is to avoid the specification change breakage, as we just say, set of entities on resource becomes locked, all identified attributes are locked. Over time, we can decide if we want to allow descriptive attributes to change.
In the context of, you know, what's happening in the SDK. But we wouldn't allow those sets to change.
Alright, what's the expected impact on collector components? We will… this is similar to entities overall. We will need to have, the processors and OTTL components kind of updated to interact with entities on instrumentation scopes, similarly to what we need to do for resource.
How do we guide developers on when to use instrumentation scope versus resource? So basically, the… the rule of thumb here that we're proposing
is the resource is the identity of the SDK itself, and the most closely associated thing to the SDK.
And its identity needs to be stable for the lifetime of that SDK, and then scope is for things that have an identity you want to record that doesn't match the lifetime of the SDK.
Okay, this is… this is kind of a big shift.
There's future possibilities around here around expanding multi-tenant capabilities to record data on behalf of things, multiple things.
Yeah, curious on initial reactions and thoughts. We talked about this briefly last week, but I don't think everyone was here.
**Daniel Dyla (Dynatrace)** 13:08 I can't see him, so just… Dimitri's first.
**Josh Suereth** 13:11 Order. Go for it.
**Dmitrii Anoshin** 13:13 Yeah, yeah, I missed the previous call, so I don't have the context to…
Why that would be required, essentially, introducing entities.
other,
instrumentation scope. I guess this is something that comes from the limitations of the SDKs and, like, how we initialize them, etc.
I'm fine.
If that's the case, I just, like, from the outside perspective, from the collector perspective, a data model perspective, what would be… do we have any, like, distinction, a clear distinction between which entities go to
Resource, or which entity goes to, instrumentation scope.
**Josh Suereth** 14:01 Yeah, from a data model perspective, we need to treat those as flattenable, is what the proposal is. And the distinction is, resource is a controllable, observable thing, whereas entity might be something else you can observe within the context of resource.
Sorry, instrumentation scope entity would be something else.
**Dmitrii Anoshin** 14:27 Okay. Also, Collector itself can, like, Produce the data, right?
And, there are… I guess there are some rules.
when some entities go to instrumentation scope and resource and SDK, but I don't think they, like, those limitations are gonna apply to the collector. So the question is.
collector typically would just add everything to resource and don't create instrumentation scope entities. Is that correct, I understand it?
By collector creating data, I mean, like, let's say, host metrics receiver, essentially, like, metrics that are created from host, which associated with the entity of the particular host, or, like, Kubernetes pod, or anything.
**Josh Suereth** 15:16 Yeah, this is where things get interesting. I think a collector might engage with that. For example, process metrics. If process metrics are attached to the process entity, then what we might have is a resource as the host of the collector.
And there would be a scope for a process, and inside of that would be metrics about the process.
**Dmitrii Anoshin** 15:36 Currently, every… we produce several resources per each,
process. And I don't see clear guidance why we should, like, why we would need to make this one resource on the host, and…
**Daniel Dyla (Dynatrace)** 15:56 I think one potential reason would be just that there's less duplication in the OTLP data model if you create multiple scopes versus creating multiple resources.
**Dmitrii Anoshin** 16:05 I see what you mean, okay.
**Daniel Dyla (Dynatrace)** 16:07 I mean, that's a minor,
improvement, but an improvement is an improvement. I think it's more about conceptually, though. I would say resources are things that are, like.
survive the length of… I come from the SDK world, so I'm gonna phrase it in SDK terms, hopefully it will make sense.
the resource would take entities that don't change or survive over the entire course of the SDK.
So, like, it'll always be running on the same host, it would always be running in the same process. That may not be always exactly true of the collector for the same things, but then the scope would be things that could come and go, like a session could be created or destroyed.
Or things where you may have to,
monitor more than one. So, like, two different network interfaces. You may have, again, the resource has the host, but you have a scope per network interface, for generating metrics on that. And then, I think.
conceptually, in the collector, it's not that different than just creating a different resource for each one of these things, but it provides a more clear distinction, and a minor OTLP size benefit.
**Dmitrii Anoshin** 17:27 Yeah, I see the distinction in minority size benefit, but from the other hand, it's a significant complexity increase.
Which we would, like, all the clients would need to handle, and collector would need to handle. And especially if we're gonna deprecate attributes on the instrumentation scope in favor of different model for the entities.
That's gonna be even more confusing.
**Daniel Dyla (Dynatrace)** 17:50 I don't think we're deprecating those attributes, are we?
**Dmitrii Anoshin** 17:54 That's what Josh mentioned, we can…
**Josh Suereth** 17:56 Yeah, bro.
**Dmitrii Anoshin** 17:57 Entity, not entity ref, but entity itself on the instrumentation scope.
**Josh Suereth** 18:03 Yeah, the proposal I have right now is not to do that, but I think it's an open question of whether we would, yeah.
By the way, Dimitri, David Ashpole had some good feedback, which was basically, we could use the same mechanism, in the SDK,
To basically construct a sub-resource from a resource, but instead of putting an instrumentation scope.
We actually construct a new thing on providers, where we could say, bind entity, and that would return a new provider that you can use to get meters, so that
The SDK would actually be multi-tenant by default, where the SDK would store multiple resources.
and providers will have to understand that, like, a resource is a sub-resource of another. It's an interesting proposal that would kind of match what you're saying. So, I just want to call that out. There's a link from David about that, and it's something I need… I wanted to think through and talk about here, but let's go through the rest of the concerns, because I think, you're… you're not alone, and I… yeah, anyway.
**Dmitrii Anoshin** 19:04 Yeah, from my perspective, it's just, like, a significant complexity, and we already have to handle with different layers of everything else, and adding another…
**Daniel Dyla (Dynatrace)** 19:13 the original question is, why is this required? The collector never treated resources as immutable to begin with, but it is specified as immutable in the SDK, or in the specification. So that was the initial reason that this got brought up.
And then, as we were spitballing and prototyping ways to solve that, we came to this solution, which, has other benefits as well, on the SDK side.
**Josh Suereth** 19:43 Yeah, it's also true that inside of the SDK,
If we want resource to be immutable.
The current, like, asynchronous updating it out of band path, actually really…
makes metrics kind of, in my opinion, untenable. Like, what we really want with metrics and what we're running into problems with is controlling the memory bounds of how much is used, and so explicitly saying, okay, I now need metrics that talk about X, and allocating that memory at that point in time.
and being able to clean up that memory when you're done, that actually is important for metrics, even in a Java world. And I linked the bug in the OTEP around something we ran into there, but it's… if you think about the performance of metrics and how to make things be optimal.
We… we… I destroyed everything with the previous OTEP, like, it was pretty bad.
**Daniel Dyla (Dynatrace)** 20:37 because.
**Josh Suereth** 20:37 We managed to make it work, but when we added in the concurrency primitives, it just got uglier and uglier and uglier, and almost untenable, in my opinion, in terms of, like, I think we were solving the wrong problems.
So…
**Dmitrii Anoshin** 20:50 Nice.
**Josh Suereth** 20:51 Yeah.
**Dmitrii Anoshin** 20:53 Okay. Yeah, just to… I just remember that a couple of weeks ago, we decided that we're gonna break that…
a rule which was never followed, that the resource itself has to be immutable, and we have… that's why we have entities with identifying and descriptive attributes. So that's not… not the case anymore. We still…
**Josh Suereth** 21:15 We decided…
We got a lot of pushback on that. A lot, like, the most significant, comments that are unresolved are basically, like.
That… that is a braking change, and we'll have to account for that as a braking change.
**Dmitrii Anoshin** 21:30 Okay.
**Daniel Dyla (Dynatrace)** 21:30 I would also say that the… the mutable resources
I think most SDKs do treat them as immutable. It's the collector that's not most of the time.
**Dmitrii Anoshin** 21:43 What if we add another… What if we add another…
set of attributes into the resource mutable attributes. And we only keep identifying immutable attributes in the old
Attributes field.
And we have another one, descriptive attributes, for example.
And that one's gonna be… I'm just speaking from the data model perspective, sorry, I'm not sure how it's gonna play out with the SDK.
**Josh Suereth** 22:10 You know, we talked about this, right? Like, the main issue right now is when people consume resource, they want those mutable attributes in it, because they're using it for slicing and dicing. Like, we're basically in a rock and a hard spot. I think the reality is, I still think we want to move to resource as mutable.
And it… but we just… it's a braking change, that's all. So, like, we should still go that direction, we just have to call it a braking change and account for it.
No matter what. And so, in this OTEP, in the previous OTEP, we still do that. This is more motivated as, like, partly that resource as mutable as a breaking change, but also the… in my opinion, the implementation in the SDK is the most significant thing driving me towards this alternative solution.
I think… I think, like, the performance of the SDK, the data model in the SDK, the way that you interact with it, and the kind of things that we can do.
this, the previous OTEP, I think, would… would…
require everyone to make a 2.0, and also would cause a set of problems that I think aren't easily solvable, and would just remain unsolved.
**Dmitrii Anoshin** 23:20 I… I was sure that, resource
as beautiful, gonna be breaking change, given that
Users use resource for identifying… they use only attributes field from the resource to, like.
to consider something as an identifiable piece of the resource. And if we add something else on top of the additional field.
That isn't considered.
**Daniel Dyla (Dynatrace)** 23:48 If we added an additional field, the problem is backwards compatibility.
existing consumers of a resource, which means both local and remote. So you have OTLP consumers, but then also things like spam processors are just reading resource attributes. If they don't get updated, they'll miss out on those attributes, and users will be annoyed.
It's not something that we could never move to, it's just… we'd have to do it in a stepwise fashion, where we introduce it over time with some duplication of data and configuration flags and that type of thing.
**Josh Suereth** 24:22 Yeah. We only have about 5 minutes left, so Ted, I want to hear what you have to say, and then I think we need to talk about, we need to talk about having more time, and maybe this meeting time to be an hour again. Go ahead, Ted.
**Ted Young** 24:37 Yeah.
This seems like a tricky wicket. Like, I do want to respect making resources mutable, you know, as a breaking change, and figuring out what we have to…
there to get around that, but I'm totally confused.
About how there's… Some problem with resources being mutable, but the problem vanishes if we switch the implementation.
I'm just not… it's just not clear to me how… how that…
Solve the problems, but my bigger concern is just that instrumentation scope feels totally incorrect.
place in our data model for the instrumentation, so…
a lexical scope, right? It's like, here's information about
the source code and, you know, the providency And fixing stuff like session, field site.
Sort of like what we're doing with span attributes. It's like, well, we could just shove it in here, and it would, like, technically work.
But it doesn't feel like, like, the right place.
So I guess that… that's… I don't have an answer, but I'm just pointing that out.
However we're solving it with instrumentation Scope, couldn't we just relabel that to something that…
**Josh Suereth** 26:01 Yeah, yeah, yeah, okay.
Institution scope is lexical.
This is contextual.
It was wrong. I hear ya, I hear ya.
**Daniel Dyla (Dynatrace)** 26:14 See, I never thought of instrumentation scope as…
lexical from day one. I always thought of it as contextual. I've always thought of instrumentation scope as the scope of the thing you're instrumenting, and then the instrumentation library name as just, like.
this is the library that happened… that's… that's the lexical scope that you're talking about. It's like, this is what I happen to use to monitor this thing. But I always thought of the scope as the contextual scope.
So it's interesting. Is that… is it specified that it's the lexical scope anywhere?
I think that's maybe an implied thing.
**Ted Young** 26:50 My assumption was, like, if we were to lean on it, you know, more, it would be about trying to put more source code information into it in a programmatic way.
Where you could start using that to link back to…
We haven't leveraged instrumentation scope very hard, so I think it's totally reasonable for there to be differences of opinion to that.
Where we'd go with it.
**Daniel Dyla (Dynatrace)** 27:19 So actually, the first sentence there, a logical unit of software with which the emitted telemetry can be associated makes me think it is the thing being monitored, not the thing doing the monitoring.
**Ted Young** 27:31 Sorry, that's what I meant, right? It's, like, the scope of the… The thing being instrumented.
And maybe it's both things, in the cases where something's not self-instrumented, you need to be like, here's the target package.
**Josh Suereth** 27:49 Here.
**Ted Young** 27:53 It was the place we were always gonna put… put all of that in.
**Josh Suereth** 27:58 Yeah, I… I… I… I hear ya. I… I feel,
It's interesting the number of implementations I've seen completely ignore instrumentation scope.
in that I… yeah, there's a piece of me that just…
the value that we have right now is that we put schema URL on it.
**Daniel Dyla (Dynatrace)** 28:22 Yeah. And the instrumentation library name that has value.
**Josh Suereth** 28:28 Well, yeah, to, like, debug things. Yep, agreed. But it's, it's like…
I don't want… I hear what you're saying, Ted. I honestly feel like we need some place to store contextual.
So, like, if instrumentation scope is lexical, we need some place to have contextual additions? Yeah, yeah, I hear that.
**Ted Young** 28:48 It's like, let's just not shove this stuff somewhere random, that's all, right?
**Josh Suereth** 28:53 No, no, no, no, I did… I did think about… so basically what I am proposing right now is that this actually becomes a hodgepodge of contextual and,
Lexical.
because we actually don't, differentiate, contextual and lexical anywhere else. So we literally don't have any place to have, like, context that is…
not lexical, if you know what I mean, at all.
So, so we have, like, span where you can throw stuff, we have resource where you can throw stuff, but we don't really have, like, the notion of context and, like, even baggage attributes. Like, if you wanted to implicitly interact with him, where do you put them?
You know?
**Ted Young** 29:38 We don't have trace-level context, that's it. We have span-level context, right? We don't have trace-level context. We do have…
process-level context, which is what resources the SDK. I mean, you know, I'm hearing some debate here, like, some people are saying it's, like, SDK context.
you know, I thought of it as, like, process-level on-tech.
**Daniel Dyla (Dynatrace)** 30:01 Well, it's both. That's part of the problem, is that it's every… it's all those contexts smashed together. It's everything that you think might not change.
**Ted Young** 30:08 Instrumentation scope in particular. So, we should never be, like, you know, doing a fingerprinting approach, but I can tell you, we're already looking at instrumentation scope at Grafana Labs as a way to, like.
If we're trying to catalog schemas of, like, stuff coming out of OTEL with Weaver.
You know, instrumentation scope is one of the things you look at.
Or, like… Being able to classify.
**Josh Suereth** 30:36 Yeah, yeah, but here's the thing. It has attributes, and guess how those are getting used? Those are getting contextual attributes.
And so people who use them are using them contextually, not lexically.
So, like, I hear what you're saying, it's just… so, first of all, if it was going to be lexical, I don't think we should have added attributes ever, because all of a sudden, that makes it start to have contextual things. Because we don't have a contextual solution. So, I think this is a discussion we have to continue, we're out of time.
And, like, David Ashpole's comments, I really want everyone to take a look at, like, this, this idea as well, because I think that this might, this might be… this solves the API problem.
Of having, entities that have a different life cycle of the underlying process resource, right?
In a way that we need. We just need to then figure out a data model for how to report these. Do we put them in resource? Do we put them something between resource and scope? I… like, we can sort that out.
**Ted Young** 31:37 Yeah. But I think…
**Josh Suereth** 31:38 What I want to understand, first of all, the direction of binding, please comment on that in here, please comment on the thing, on the overall OTEP, because I really want to make relatively quick process here, or quick progress, and I was reusing the previous prototype.
Because, honestly, like, it had half of what we needed, just…
had a bit of, like, a lot of complexity with mutating resources in SDKs. If we can find a way to make that mutation explicit in the API,
90% of that problem goes away.
For metrics. Okay.
Last thing in the last 2 minutes. I think we need an hour, I think we need a new time. I can send out a poll, but real quickly, what day of the week is most
available for people for an hour. I assume we need something that is Pacific-friendly and EU-friendly.
So I think it'd be around this time every day.
What day of the week are we feeling?
**Daniel Dyla (Dynatrace)** 32:43 I think we…
**Josh Suereth** 32:44 Pacific.
You want what?
**Daniel Dyla (Dynatrace)** 32:48 I think we can't go any earlier because of Pacific, but we could maybe go one hour… later? I don't know.
**Josh Suereth** 32:54 We could do one hour later. That starts to overlap with things where I think people can't attend, possibly, like the Kubernetes Operator SIG, the Java SIG.
**Daniel Dyla (Dynatrace)** 33:03 Oh, I didn't mean today, I meant just in general.
**Josh Suereth** 33:06 Oh, in general, yeah. Basically, would people be comfortable with a Friday meeting, I guess is what I'm asking, because I'm looking at the calendar. Semantic Convention, Spec, and TC are Monday, Tuesday, Wednesday at this time, so I can't really… like, I'm screwed.
**Daniel Dyla (Dynatrace)** 33:21 I'm fine with Friday. I know there are no Hotel Friday meetings, but it is… for European folks, it would be kind of a bummer to have, like, a 5pm Friday meeting.
**Josh Suereth** 33:32 Yeah…
**Ted Young** 33:34 Can we start 30 minutes earlier? Like, would people be able to start at 7.30 a.m. Pacific?
**Josh Suereth** 33:41 I can do that. Would folks be okay with 30 minutes earlier? No?
**Dmitrii Anoshin** 33:45 We're gonna be, 30 minutes late every day, because there is systems multi-conventions working really well.
**Daniel Dyla (Dynatrace)** 33:52 What about right after the SEMCOM meeting? That's 12 Eastern, 8 Pacific,
**Josh Suereth** 33:59 Yeah, that could work.
**Daniel Dyla (Dynatrace)** 34:00 6PM on Monday?
**Josh Suereth** 34:02 6pm Monday, yeah, for Europe, and .
**Daniel Dyla (Dynatrace)** 34:05 Yeah.
**Dmitrii Anoshin** 34:07 What, what, what PhD?
**Daniel Dyla (Dynatrace)** 34:10 Pacific, that'd be 8 AM.
Or, no, that would be, sorry, 9A, right?
**Josh Suereth** 34:14 I am, yeah.
**Daniel Dyla (Dynatrace)** 34:15 10, 11, yeah, 12, Jesus.
Clearly, I couldn't have a math major to work here.
**Josh Suereth** 34:24 I'll put out a straw poll for options, and we'll see what gets the most, but we'll try Monday at 9, and we'll try Friday. Monday at 9.30 minutes earlier today, what?
**Daniel Dyla (Dynatrace)** 34:34 9… 9 Pacific Standard.
**Josh Suereth** 34:36 Pacific, yeah. Meaning, I'll be eating lunch while we meet, but it's fine.
**Daniel Dyla (Dynatrace)** 34:40 Yeah, that's 12 o'clock for me, too. The 1-2 time zone.
**Josh Suereth** 34:44 Yep. Fun times. Alright, cool. I'll send that out. Thank you, everybody, for the extra time, and yeah, we'll see ya. Look forward to the discussion on the OTEP.
