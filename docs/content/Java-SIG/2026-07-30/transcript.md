SIG: Java SIG
Date: 2026-07-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:04:54 Hey, folks.
Here's hoping everybody finds the, new meeting link.
John Watson 00:05:03 Are we… do we need to create a Linux Foundation account, or is guest okay?
Trask Stalnaker 00:05:12 Seems like you're here.
John Watson 00:05:15 I didn't know if there was expectations that we should have Linux Foundation accounts.
Trask Stalnaker 00:05:20 No.
I have one… Cause I need it for some other things.
John Watson 00:05:40 Jack, what is Rain Tank Inc?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:05:45 Yeah, that's, confused me as well. That's, like, the parent company of Grafana Labs.
John Watson 00:05:54 Okay.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:05:54 I don't know, someone, I was talking with Armin about this. Armin noticed that, like, you know, you know Honeycomb? Have you ever seen, like, people with, like, a reference to Hound technologies?
Yeah, so it's, like, Hound Technologies, DBA, doing business as Honeycomb. And so, like, it's like that type of relationship, where there was some name for a company, and like, you know, it was all incorporated under that, and then they have, like, you know, the practical name that everybody knows.
Not my decision. Naming's hard, I guess, for corporations, too.
Trask Stalnaker 00:06:33 Yeah, I don't know why the, the… maybe it's… maybe it's those of us who have the… Linux Foundation accounts, that it is linking it to our employer, because mine had suddenly said Microsoft, Also, on all the meetings.
Haven't figured out how to fix that other than one by one.
Should we… does anybody want to try to join the old meeting link, just to make sure nobody's over there?
Jay DeLuca 00:07:16 to the Lord.
Trask Stalnaker 00:07:17 The old meeting link is.
Jay DeLuca 00:07:19 I was just there, because I went there first, so I'll go.
Trask Stalnaker 00:07:21 Oh.
Jay DeLuca 00:07:21 look.
Trask Stalnaker 00:07:22 Nice. Thanks.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:07:26 Must be doing something different than everybody else, because I've had, like, none of this… the meeting problems others have discussed. My calendar just was updated, and I just always clicked the link in the calendar, and everything works.
Trask Stalnaker 00:07:41 What, calendaring system do you use?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:07:44 Google Calendar.
jason 00:07:47 Yep.
Trask Stalnaker 00:07:48 Not only why.
jason 00:07:52 That's what makes.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:07:52 So is it like… is it something like the other calendar systems, like, made a copy of the meeting records at, like, a point in time, and therefore, like, those point-in-time copies are out of date now?
jason 00:08:07 It's the only way I can do it.
Trask Stalnaker 00:08:12 I've got it to work, it seems to update my Outlook calendar, But… Yeah, I've heard a lot of cases that that synchronization hasn't worked for people.
Cool, let's get going.
Oh yes, we are here.
And… Sure, we will invent more topics, but Jonathan, let's start with you.
Jonathan Halliday (IBM) 00:08:52 Yeah, this is just a quick sort of F4. And I warn I've got some time to work on profiling-related things.
want, really, is the thread context OTEP, because that's what's going to… allow Trace Context to… be correlated with profile information. So we can take a profile and, Tie it back to the context, or more likely look at a trace and say, this trace is a bit unusual, and then drill down from the trace to the profile, and… ideally go right down to method level and say, I see the method that's causing this trace to take an unusually long time.
So that's… that's the kind of use case.
So to get there, we need some… some new pieces, and really, this is a question of, is there an appetite to have them upstream in the SDK already at this stage?
It's quite early in that there isn't yet widespread adoption of the profiling stuff. It's getting there. The eBay profiler is available, the backends are… Are starting to become available, but it'll… it'll take a while for people to adopt this.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:10:11 And it'll be slower to adopt if, if things like OpenTelemetry Java are laggards and, you know…
Jonathan Halliday (IBM) 00:10:17 Yeah, it's a thing that we'.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:10:18 It reaches.
Jonathan Halliday (IBM) 00:10:19 a certain…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:10:19 Level of maturity.
Jonathan Halliday (IBM) 00:10:20 Yeah, there needs to be an implementation there that people can… can adopt, because.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:10:26 Right?
Jonathan Halliday (IBM) 00:10:26 You know, very unlikely to write their own.
We've discussed some of this previously, and the consensus seemed to be that going down a JNI route to do the native bids was a non-starter, because we don't really want to be mucking about maintaining native library code. So that tends to point at this using Panama, which means, in terms of LTS releases, Java 25 only.
So that simplifies the build. It doesn't necessarily simplify the test, because we need… Environments that have, 25 on them.
But by and large, it should be straightforward to get the first bits of this. It's just a protobuf.
Format, so I just need some code to be able to write things into the buffer.
We need some kind of API, so you can tell it what you want to publish. Some of that could potentially be kind of automatic, it'll gather up environment variables and things for you.
But… some kind of configuration surface where you say, these are the things I want to include.
The tricky bit, I think, might be lifecycle related, in that, if context changes during the process lifetime, you want to republish it.
So whether we need some kind of notification mechanism, or some kind of trigger that allows that to be semi-automated, I don't know.
Haven't really thought it through yet.
So that's the process thing that publishes environment variables and other, sort of.
JVM-level stuff, and then there's this thread context one, which publishes, the actual traits, but it requires the process context one.
For the thread context, the tricky bit is dealing with virtual threads, so I've got a parallel conversation going on with some of our JDK people about ways to speed that up. The clunky way to do it is to use JVMTI callbacks, but god, are they expensive at runtime.
Trick-drigging something every mountain on the mount of a virtual fair just is.
Painful.
So I'm looking at whether we can get something built in. The kind of less clunky but still not requiring OpenJDK changes way to do this is to instrument virtual thread.java at classload.
Which clearly requires background manipulation, but hey, instrumentation does that anyway, so… We've kind of got the infrastructure for that.
It's still somewhat expensive in that it needs a J&I call, but one of the options I'm exploring with the OpenJDK people is expanding, Panama to be able to talk to thread locals.
So this is sea level thread locals, TLS variables, are not currently in scope for Panama.
But that's a kind of generally useful feature. So, although it's more engineering work, they're more likely to be interested in it than they are in putting in hotel-specific stuff into OpenJDK, which is kind of… hmm… a little bit niche, and they don't really want the maintenance burden. So that's a tougher sell, even though it's a quite small footprint code change.
So anyway, yeah, ongoing OpenJDK work, for this meeting, it's more about what bits of these two OTEPs might we want in the SDK, or in Contrib, and…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:14:07 So, I can give my two cents. So… I'm in favor of this going directly to the core repository, not to contribib. I think there are things that need to be hashed out in the spec.
You know, this was an OPTEP that landed, it talks about some things. It's vague on other things. You know, you talked about, like, you know, configuration and hooks. Like, what are the things that actually make this happen? And somebody needs to go right down in the spec what SDK requirements are for this. Like, what are the hooks that are leveraged in the SDK, or maybe new ones are needed, that allow you to, You know, detect that some change in context was made that needs to be written to this, like, shared memory location.
You know, two come to mind. We've got span processor, so maybe this could be implemented as, like, a span processor, or maybe, there's also, like, context storage. There's a hook and context storage that allows you to, like, detect when, like, a new context was attached to a scope.
Jonathan Halliday (IBM) 00:15:09 Yeah, that's how the current prototype works for thread-level stuff, yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:15:15 Yeah, so those are the two that come to mind. Are those sufficient? I'm not deep enough in this space to know for sure, but, you know, I'm willing to… you know, experiment in OpenTelemetry Java. We have the right tools to be able to experiment, we have the ability to mark modules as experimental, we have internal code, so we have all sorts of facilities to be able to, like, you know, roll something out that, can inform the spec work and, you know, hopefully eventually mature into something.
Jonathan Halliday (IBM) 00:15:47 Sounds good.
Trask Stalnaker 00:15:54 Yeah, I would love to see it go straight to the core repo, also, from… I agree, I think that will help everything move forward in the spec, also giving confidence to other people that it's being worked on.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:11 And Jonathan, one other thing about the Java 25 requirement, you might know this already, I think you were saying some things that hint at this, but, you know, we have prior art for different capabilities that sort of are, language version dependent.
You know, at one point, our clock implementation, you know, changed based on whether you had Java 9+.
We have some… some stuff in terms of string serialization for Protobuff, which is Java version dependent, and Yeah.
Jonathan Halliday (IBM) 00:16:42 I can certainly see things in there that load different code, depending which runtime they're on.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:48 Yeah, so, yeah, exactly.
Yeah, that's a…
Jonathan Halliday (IBM) 00:16:51 thing that doesn't load at all, unless it's on a certain version. That, I think, is new.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:58 that… That…
Trask Stalnaker 00:17:00 You give it a no-op.
Default.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:17:07 Yeah, so you make it, you make it not work.
Jonathan Halliday (IBM) 00:17:09 You guys?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:17:10 not blow up, so… Yeah.
Jonathan Halliday (IBM) 00:17:12 Yep.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:17:14 That's the goal. And I think technically our build, are we on… what's the latest version of Java in our matrix? I think it's Java 25, or maybe 26 now, so, I think we… We have GitHub runners that…
John Watson 00:17:29 There was a PR for 26, I don't know where it ended up landing, if it ended up going through or not.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:17:34 It landed, yeah, we're on 26, so…
Trask Stalnaker 00:17:36 But we, we accidentally dropped 25.
Which we should keep, since it's an LTS.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:17:44 We should do that.
I'll make a note.
Yeah, so, looking forward to whatever you propose, Jonathan.
Jonathan Halliday (IBM) 00:18:01 Great, well, I'll just gradually make a start on it, and yeah, there'll be PRs and questions coming your way in due course.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:18:09 Sounds good.
Jonathan Halliday (IBM) 00:18:10 Thanks.
Trask Stalnaker 00:18:16 Alright, Jack?
attribute limits.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:18:22 Yeah, this is a draft PR, But I want to discuss it anyways, because John's here. So this… This sort of ballooned out of, you know, somebody else had this, seemingly benign, fix to an issue, and the… the… the issue was… that we… our attributes map, which is the internal implementation of attributes we use in Log Record Builder and Span Builder. It didn't have last-right-win semantics.
And that's, like, something that's required by the spec.
And so, you know, they… they had this implementation that jumped through a bunch of hoops to try to have last-right-win semantics while not degrading performance.
And… you know, I didn't like how big and messy attributes map was getting, and it sort of triggered this, like, this old thought that I've had, which is, like, why does Attributes Map exist at all? And the only reason attributes map exists… why do we have two implementations of attributes? The only reason it exists is because, you know, we… what attributes map does is it, like, dynamically enforces attributes limits. So, like.
As you're adding attributes, as you're putting key-value pairs in, it will apply the count limits and the length limits that you configure on your, you know, your tracer provider and your logger provider.
And, so the… the reason you can't do that with the standard attributes implementation that's in the API is that there's no concept of limits in the OpenTelemetry API module. We have, you know, that's strictly, like, an SDK-level function. And so, you know.
I went with a different approach. I was like, hey, what if we solve this, this last win semantics problem and try to solve other problems at the same time by promoting attribute limits to be an API-level concept?
And so, you know, that would allow us to get rid of this attributes map implementation altogether.
And, you know.
there's this other sort of related conversation that's been happening at the spec, which is about depth limits as well. Right now, we have a count limit and a length limit, but there should be a depth limit, because we have any value attribute type, so, you know, you need to do the thing where you don't allow for arbitrary depth and things like that.
So that's sort of… segues into this conversation as well. But, you know, I have a draft PR here. I think the API is pretty good. You know, I think the performance is good. There's no, you know, meaningful degradation in the attributes API performance.
And the question is sort of, like, conceptual. Like, do we like going in this direction?
Trask Stalnaker 00:21:27 Jack, could you remind me why we need an implementation of it in the API? Why that's not just a no-op?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:21:41 Why we need an implementation of…
Trask Stalnaker 00:21:44 of attributes map.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:21:48 We need an… we need an implementation of Attributes Map in the SDK. That's… that's where it exists today. So, essentially, we have two attributes implementations that are working. One is like, you know, you're calling the APIs, and you build up a set of attributes, and you either attach it to a measurement you're trying to record for a metric, or you say, set all attributes on a span, or set all attributes on a log. And, you know, the API-based attributes implementation is the thing you're building up there.
And then internally, for logs and spans.
not metrics, because there is no incrementally adding attributes to metrics, but for logs and spans, every time you add either a bundle of attributes or an individual one, it manifests as, like, set calls on this attributes map implementation, which is, like, an internal class within the SDK.
And so, that's the frustrating point, is like, why do we have this attributes map implementation at all, which, like.
you know, if we go to the source code, attributes map, it extends HashMap, and so it's a very different implementation as well. You know, our API-based implementation is, like, maintains key values in an array, and the, you know, the attributes map one is, like, an extension and customization of a hash map, so they operate differently as well.
It's… it's sort of always rubbed me the wrong way that we have both.
John Watson 00:23:15 Yeah, historically, the one in the API was optimized for memory, and the one in the SDK at the, like, the attributes map was optimized for speed.
So… They had… they had different… operating characteristics.
Yeah. But it's, like.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:23:36 Feet of what?
John Watson 00:23:38 Well, I mean, the adding stuff to a HashMap is very… like, getting stuff out of a HashMap is very fast. Getting stuff… putting stuff into a HashMap is very fast. Putting stuff… like, managing the array and the array-backed attributes is not as fast. But it's very, very memory efficient.
Once you've got it into the concise, compact, deduplicated array.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:01 Yeah, and there's two things you need to do, like, two things you mentioned. So, add to a map and get from a map. So, when you add to the map, you have to… you essentially have to, like.
in the array-based implementation, you have to scan through the entries and look for duplicates and do that type of thing. So it's like a scan against the entries. And that might happen, like, you know, from time to time.
And then for reading back values out of the map, yes, like, a map's always going to be faster than scanning through an array, although I'll say, like, at small attribute sizes, it probably doesn't matter. It's, like, it matters more as the number of attributes get bigger, and I would also say that it's uncommon.
Because the only time you're actually reading out of this HashMap-based implementation is when you're in a span processor that is still, like, reading the span in, like, a mutable state.
Where you're saying, like, hey, get attribute foo out of this readable span, and then do something with it. Because by the time you get to the exporter, that attributes map gets mutated into, like, the standard array-based implementation anyways. So, exporters, you know, don't get to benefit from whatever those read mechanics are, there's no difference.
John Watson 00:25:19 And exporters often don't need to be able to pick out individual items, which is the thing that the map is much faster at.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:26 Right, they're just iterating through all.
John Watson 00:25:28 Yeah, and iterating through all is going to be faster out of an array.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:33 Right.
Trask Stalnaker 00:25:39 So, I'm trying to think through, why does attributes limit need to leak into the API?
Why can't it be… Hidden in the SDK.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:25:55 So, if you want to do… if you want to have one implementation of attributes.
And you want that implementation of attributes to do all the things it needs to do, which are, Have this last wins mechanics and be able to enforce limits then you need… and that one implementation lives in the API, then you need the API-based implementation to be able to enforce limits as you're building it up, because that's currently being performed in the SDK implementation.
Trask Stalnaker 00:26:29 Right, so that was my… the first question I was trying to understand is… is, why we need an any implementation in the API.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:43 in any implementation.
John Watson 00:26:44 because…
Trask Stalnaker 00:26:45 Why isn't there?
John Watson 00:26:46 Because all the… because you have to be able to actually… like, baggage is in the API, and all these things that actually also can have attributes on them. Actually, does baggage have attributes? I don't remember.
But, we have to be able to actually send concrete stuff into the API.
And attributes is not, if I recall… is it… I don't think it's an interface, or… I guess it must be an interface.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:27:11 It's an interface, yeah.
John Watson 00:27:12 We have to ask…
Trask Stalnaker 00:27:13 Could it be no up?
In the… why can't the API version be no-op?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:27:20 So, there's several APIs that accept attributes, and if, you know, if they're only a no-op implementation available.
in the API, then, then that we'd break those APIs, like, day one. And so, you know, there's a method on span to set all attributes, not one, but set all.
every time you record a measurement to a metric instrument, you're recording an attribute set, not a single, like, you know, not single key-value pairs. So if you didn't have a concrete implementation in the API, those would just… those would not work.
Trask Stalnaker 00:27:59 But,
Jack Berg (Raintank, Inc. – Grafana Labs) 00:27:59 Maybe I'm missing something.
Trask Stalnaker 00:28:01 a millop concrete.
why can't… why can't API have a no-op implementation? Like, I'm…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:28:10 So, think about a counter recording, like, a value, 1. And so you're saying, I want to record 1 to, you know, the series represented by these attributes. If that attribute was a no-op.
like, that information that is intended to be in that attributes, like, set, is erased by the time the SDK needs to, you know, do something useful with it.
Trask Stalnaker 00:28:31 Why can't the SDK… If the SDK is there, it provides its own… I mean, kind of like we do with tracers, you know, with everything else, there's a no-op in the API. If the SDK is there, you get the SDK implementation.
John Watson 00:28:47 So you'd have to then, every time you wanted to do anything with attributes, you'd have to ask the OpenTelemetry object for an implementation.
Which would be pretty awkward. I mean, yes, we could have done that, but that would be a pretty awkward way to interact with something that should just be some data.
Trask Stalnaker 00:29:07 Okay.
John Watson 00:29:08 I mean, I think we could have gone down that road, but I think we wanted to actually have some concrete stuff to work with, rather than having to ask the APIs for implementations every time we wanted to do something.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:29:23 Yeah, and I would say the ship has probably sailed on that because of just the structure of the APIs that exist today. Like, it'd be… it'd be hard to do that in anything but a 2.0. Probably impossible to do in anything but a 2.0, and even 2.0 would be very consequential.
Trask Stalnaker 00:29:39 So we wanted to or not. Okay. Okay, yeah, yeah, yeah, yeah, that… that helps my mental map then.
jason 00:29:47 So attributes limits… attribute limits is not a spec'd API, right? So this is adding a new API.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:29:55 It sort of is a spec'd API. I think I would argue that we're out of spec right now. Like, if you go to the common attributes definition of the spec, it talks about these three configurable parameters as, you know, as the limits that, like, you know, that SDKs should enforce on attributes.
So, the fact that we…
jason 00:30:15 A's should enforce.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:30:18 Well, the problem with the attributes section of the spec is that it doesn't actually differentiate between API and SDK, like other portions. So, like, you know, I was saying SDKs, I guess, in the general sense, where, you know, people refer to an overall language implementation as an SDK.
But, like, I'll double-check that as we're talking, like, you know, I'm not entirely confident, I'm not… Yeah, right here. This is the document that, that the limits are…
jason 00:30:48 Yeah. I just… I'm wondering if it doesn't warrant some clarification on the spec as well.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:30:57 Which part?
That…
jason 00:31:00 Yeah, the fact that we're having, like, a real API.
Yeah, because I agree that this section of the spec could be made clearer.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:31:21 That is interesting. They, this document does… It is in the comments section, but it uses the terms API and SDK, and the limits part is specifically in the SDK part.
And so…
jason 00:31:35 Because maybe it was thought that, like, it's just an implementation detail. Like, the SDK shouldn't be unbounded, you know, I could see someone thinking that, but not… codifying that there should be an API that allows the user to configure those limits.
It's a subtle… it's a subtle difference, right?
It's new.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:31:55 Yeah, and, and, you know, I guess, like, assuming that the spec was written, like, consistently and coherently everywhere is, like, the wrong assumption, is, like.
jason 00:32:05 Yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:32:05 over time by a bunch of different authors, and, like, you know, all sorts of natural inconsistencies sort of develop over time. And the one that I'm thinking about here is, like, you know, you say that the API documents assume that the concept of a bag of attributes exists.
And it's, like, you know, it assumes that you can record a bag of attributes on a metric, and you can record a bag of attributes on a log in a span. And then separately, it talks about those limits. And the idea that, you know, you could have an attributes concept.
And, like, separately have, like, a limits concept that was not sort of embedded in the attributes concept.
And… and track things, like, you know, how many attributes were dropped because they exceeded the limit.
and things like that, which are expected contracts of, like, OTLP export. I don't think it actually adds up. I think it's, like, logically inconsistent.
Trask Stalnaker 00:33:04 But I… I think this gets back to the question of, I mean, the early… earlier discussion, which was my confusion of the… the API. Why can't, you know, the… I always think of the API as just being a bunch of no-ops, and so technically you don't need attribute limits in the API.
But, given the way that our SDK, our API SDK is structured, our API is structured.
We've leaked that in.
Which I think is… is fine, right? We have reasons. And now the… Worse thing is that we are not… our SDK is not compliant.
And to fix the SDK to be compliant, we have to do something like this.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:33:58 Yeah, and as you're saying that, I'm just thinking about what it would actually look like to be able to you know, continue like we have today, where we have a concrete implementation of attributes in the API, but actually take this attributeLimits class and only have that in the SDK.
you know, and, you know, have the SDK be able to construct, like, standard standard attributes instances, but, you know, with these limits applied. Like, is it possible to do that?
John Watson 00:34:30 I mean, we could add… an API… like I suggested we could have done originally, which is, like, get… limited, or get… I mean, we could add an API that's… to the OpenTelemetry API that would give you back an implementation, and the SDK one… would support the limits part, but I don't know… it's a little bit strange if you need to actually write instrumentation Like, does instrument… should instrumentation be concerned with the limits.
Because we're basically now giving that to the… to instrumentation to be able to interact with. And that feels a little… It feels a little weird.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:35:22 Yeah, I agree.
Best one.
John Watson 00:35:27 Wonderful.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:35:27 From the same line of reasoning, it also feels weird that, you know, instrumentation could have the ability to construct attributes with limits, you know, with this PR, as proposed. You know, whether you're getting those attributes with limits from, you know, the open telemetry instance, or just constructing it yourself.
you know, I guess instrumentation has that question to answer, like, hey, when I'm constructing a bag of attributes, should I be aware of limits or no?
John Watson 00:35:53 And the… the limit… so the way that the spec is written at the moment, the SDK enforces it… enforces the limits blanket across all Usages of attributes?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:04 No, it's got these awkward exceptions, which several of us want to resolve. The limits don't apply to metrics, and the limits don't apply to resources or scopes.
It's silly.
John Watson 00:36:17 Exactly.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:36:18 entities.
John Watson 00:36:20 I'm just thinking that we… like, I'm feeling like if we… people want to… well, I mean, we are kind of a little bit stuck. Like, either we need to give it to instrumentation.
Which feels strange, like, instrumentation.
Trask Stalnaker 00:36:33 I don't want it.
John Watson 00:36:34 Yeah, yeah, I don't think…
Trask Stalnaker 00:36:35 As an instrumentation out there.
John Watson 00:36:37 Yeah, yeah, no, I think it feels strange. It's not something that the instrumentation should be concerned with, it's an operational concern, right? And so it's not something that we should be leaking into the API from an inst… because instrumentation isn't going to know what to do with it. Like, it can't do anything with that stuff, right?
So… I guess the question is… how do we… how do we get out of this sticky situation where the SDK needs to do the enforcement?
But we don't have a way… like, it's like the SDK needs to somehow decorate all the attributes that are sent into it with an enforcer.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:37:18 We could subclass the, the API's implementation of attributes.
And, you know, structure the parent class that's in the API in a way that facilitates subclassing and limits of enforcement.
So, and, you know.
Trask Stalnaker 00:37:36 At least we didn't.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:37:36 Basically.
Trask Stalnaker 00:37:37 The constructor, yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:37:40 Right.
John Watson 00:37:41 Well, so let's… let's go down the… my thought, like, what if every time the SDK got an attributes got attributes, it wrapped it in something that did the limit enforcement. Is that something that's feasible to implement? Like, could we put hooks into the… like, internal hooks into the implementation that aren't exposed on the API that it would allow? I'm not exactly sure how that would work, but…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:38:05 You're saying something similar. Like, that's kind of where my head's going, John.
John Watson 00:38:09 So you have a subclass that… can enforce them, but would only enforce them if the SDK was involved.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:38:17 Correct. The parent class is structured in a way that facilitates this subclassing and limit enforcement. So, like, you know, the parent class is sort of, like, in the API, knows what the SDK wants to do and needs to do.
jason 00:38:31 That has to be on the builder, though, right? It can't be on the attributes?
Because the attributes, like, by the time you have attributes, the ship has sailed, right?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:38:39 Correct, it does have to be on the builder. Yeah.
John Watson 00:38:43 Unless it's invincible.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:38:44 lies.
John Watson 00:38:45 Unless Attributes had a… a function… I don't know exactly how that would work.
I guess, like, you can make this.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:38:55 work.
John Watson 00:38:56 Okay, I like to see it, because I think putting it on the builder immediately exposes it to the API, right? That's the problem, right?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:39:04 Right, and I'm all about, like, you know, not exposing all this to the API, like… No.
Trask Stalnaker 00:39:12 I like your optimism, Jack.
jason 00:39:15 Anyway.
John Watson 00:39:16 Okay, if you've got an idea, I'd like… I'm very happy to see what it looks like. Sounds cool.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:39:21 Alright, thanks for the discussion, I appreciate it.
Trask Stalnaker 00:39:29 I see Felix here. Felix, are you… online sh… I did, I did… I… I missed last week, but I did watch the recording.
I don't know if we want to… chat, I think… takeaway was, Felix, you were going to open a issue?
Felix Wong (International Business Machines Corporation) 00:39:53 Right, yeah, but I haven't got the chance to do that yet, yeah.
Trask Stalnaker 00:39:57 Okay.
Yeah, I think it would be great if you could open that, Because… And just Jack and John, just to share kind of my… thoughts… I mean, I would… Especially since it's in… it's a sticky situation, given that it's in the API.
that CVE.
Not really, like, it definitely doesn't go against any of our policies, I agree. But I can kind of understand a little bit better why… the micro-profile folks want to… are pinned at a certain API version… Anyway, like, I would like to…
John Watson 00:40:52 I'd like to hear that, because I… I still don't understand why that's the case.
Trask Stalnaker 00:41:00 because their SDK… their SDK implements that specific API version.
That's the… that they… they are kind of contractually supporting that.
API version for their users, and… nothing more. If they bump the API version.
suddenly there's a lot more API surface that their users can use, which… They would have to, then support.
Felix Wong (International Business Machines Corporation) 00:41:39 Right.
John Watson 00:41:43 Is there a concrete example of what doesn't have default implementations, or is it just they just don't want to support it?
Trask Stalnaker 00:41:51 It's a user expectation. My understanding is it's user expectation, then, that, like, users would start using these new methods.
Yes, nothing would break, but the new methods would no-op, and would do nothing, and would Trigger, you know, support questions.
Felix Wong (International Business Machines Corporation) 00:42:14 Right, I think our… one of our, important points is not vendor login, right? So, I mean, different vendors will implement the micro-profile specifications as well. So, suppose, like, they… if one customer, like, implementing running their application on IBM… IBM's implementation, they can take it to, like, some other vendor implementation without modifying their code. So if we suddenly support, like, extra APIs, and then they… the customer's starting to use it, and, like, they bring it to another, like, vendor's implementation, which doesn't have that new APIs, that their application will be broken.
John Watson 00:42:59 So, I think my suggestion is… Well, I think the first thing is, I think that from a support perspective, we just can't guarantee that we're going to be able to do, kind of, infinite patches on any version throughout history. Like, I just… it's not feasible. Like, we just can't guarantee that. So, my recommendation would be fork.
like, you just need to fork from that… from the spot where you need to do it, and own that. Because I don't think there's really another way to go.
Unless… if you really can't go forward, like, you're gonna have to fork.
Felix Wong (International Business Machines Corporation) 00:43:33 Will you guys, like, considering, like, the Java, also doing that, like, the LTS versions? Like, I mean, you marked some of the versions that you support longer?
Trask Stalnaker 00:43:46 So, I'd like to… I mean… I mean, I… Totally agree, John, that we can't guarantee that we're going to patch everything, and we're not going to patch backport patches to 62 minor versions.
The possible… path forward.
That… Would be, to kind of go back in retros and say, okay, we're gonna take this version that MicroProfile is on, this minor version.
and declare that as, like, an LTS miner version.
And we're only gonna backport to that.
And I totally agree, like, we wouldn't… do this. Like, there has to be some… some limits there.
But I… I feel like microprofiles, you know, it is an important part of the ecosystem.
And so I could see… trying to make… I could see trying to make a case for that.
And then making sure that, you know, microprofile going forward, if they want… if they need to, you know, pin something in the future, we mark that as, you know, sort of an LTS minor version.
Yeah, definitely. In a way that…
Felix Wong (International Business Machines Corporation) 00:45:13 That sounds good, yeah, to me, yeah.
Trask Stalnaker 00:45:16 Yeah, yeah, I'm not saying that's what we would do, I'm just saying that's the case I would, I could see trying to make.
Felix Wong (International Business Machines Corporation) 00:45:25 Right, okay.
Trask Stalnaker 00:45:26 Yeah, Jack.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:45:28 So that suggestion sort of fit… I know you listened to the recording, so that fits into this, like, this kind of realm of possibilities, which is like, hey, adjust the policy.
And, then the question is, like, what does the shape of the adjusted policy look like? And what you're saying is, like, retroactively mark various, minor versions, TBD, as some sort of LTS.
And, like, maybe the litmus test for what that could look like, because I don't like saying that we're going to have LTS versions based on, like.
you know, one library or ecosystem's dependency on something, but, like, you know, maybe the litmus test is something like, hey, we had a major expansion of the API in this version. Like, we stabilized metrics, we stabilized logs.
Something like… something like that, and we can find the minor versions in which those events happen.
Suppose we can do that.
what does the LTS mean? Because 1.0 was published in February of 2021.
Trask Stalnaker 00:46:37 Felix, what, what ver… I think Felix is on one diet 19?
Felix Wong (International Business Machines Corporation) 00:46:44 Huh.
Trask Stalnaker 00:46:44 camera.
Felix Wong (International Business Machines Corporation) 00:46:45 Yeah, let me double check.
Trask Stalnaker 00:46:47 Or is it really 1.0?
Felix Wong (International Business Machines Corporation) 00:46:50 Not 1.0, I think, definitely, not that O. Let me double check,
Jack Berg (Raintank, Inc. – Grafana Labs) 00:46:58 I think I remember, like, 1.11 or something?
Felix Wong (International Business Machines Corporation) 00:47:02 At least 1.19 or something.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:07 1.19…
Trask Stalnaker 00:47:09 Still over 3 years old.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:11 Exactly, and so, like, we need to be on the same page about, you know, what expectations are around LTS, because I get that, like, you know, a well-funded, you know, corporate-based project thing can have, like, sort of maybe indefinite LTS, but 3 years seems pretty long for LTS, for, you know, a minor version, so… Okay.
Trask Stalnaker 00:47:36 also make a differentiation between API and SDK, potentially, and… Only… backport CVEs that impact the API, which would reduce our surface area a ton.
I mean, I think it's gonna be pretty rare for us to have CVEs in the API.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:47:59 Yeah, it's pretty rare for us to have CVEs at all. I think this is our first one.
But, yeah.
Trask Stalnaker 00:48:05 Had to hit the API.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:48:07 Right.
Yeah. But yeah, that's, like, a different version of, like, an adjusted policy. So adjust the policy to have different rules or guidance for the API versus SDK.
John Watson 00:48:17 So I'm gonna be a super jerk.
I'm gonna say if IBM would actually contribute full-time resources to this project, I would feel a lot different about this.
Trask Stalnaker 00:48:32 I mean, Jonathan's IBM…
John Watson 00:48:34 Yeah, I said full-time… I said full-time, and I don't think… I don't see Jonathan in… on the maintainer track, or even at the moment on the approver track.
Trask Stalnaker 00:48:45 But, I mean, I'm gonna… I'm gonna push back, John,
John Watson 00:48:49 I was being a jerk, and I'm aware of it, but I think this is a.
Trask Stalnaker 00:48:52 No, no.
John Watson 00:48:53 Like, this is an open source… a big, important open source project, and if you want this kind of bespoke support, you gotta… you gotta put people on it.
Trask Stalnaker 00:49:03 what I'm gonna… Pushback on, though, is… What the time involved to… like, if we construct a narrow policy.
Say, you know, even if we just say, retroactively, 1.19, And API is… we consider an LTS.
The… I mean, it's… What do we think… do we think is gonna take more than a day?
to…
John Watson 00:49:41 I don't even know if we can build that version at this point with our build system.
Trask Stalnaker 00:49:48 I… I mean, I… if it was that limited in scope, I would volunteer to… drive that release.
The question to me is, you know, we have, like, what does… how… how do we… you know, I think there's… there's bigger questions around it, you know, and that's why I think… I do think I would like an issue from Felix to.
Felix Wong (International Business Machines Corporation) 00:50:17 Okay.
Trask Stalnaker 00:50:17 late… tracked.
Felix Wong (International Business Machines Corporation) 00:50:19 Yeah, yeah.
Trask Stalnaker 00:50:21 it well.
And then I totally agree with John and Jack that this is asking for a policy expansion, and we have to decide what that sort of policy expansion is. Can it be narrow? Can it… can the maintainers feel comfortable about that? Because I am… I'm not… I'm not a maintainer, so, like, I'm not… responsible, sort of, ongoing for that, and dealing with necessarily, you know, people complaining about one-offs and that sort of thing. So, I agree, it's more complicated. I don't mean to make it sound Super simple.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:51:05 Hey, Felix, question for you on Microprofile. What's the… what's the LTS policy there, in terms of years that this… this older version of MicroProfile, you know, is expected to have CVEs?
Felix Wong (International Business Machines Corporation) 00:51:19 Yeah, the micro profile itself is just a specification, so it was up to the vendor defining what are their policies.
Right? So, for Open Liberty, that implements MicroProfile itself, so we have we don't remove any old features, right? So… and we have a LTS policy for… Patching, worsens that back up to 2 years.
But the problem is we don't deprecate any features. So, like, the original 1.19, we are still supporting it in the current Open Liberty version.
So, that is why that, we have to patch it. I mean, it would be nice if we can say that, oh, you are on 1.19 and it's too old, we don't support that, but our policy I mean, allows users to switch from features to features, but, I mean, we're supporting them in every release.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:52:32 I guess I don't quite understand that, Couple of things about that, like, so… If… if micro-profile is just a specification, Then, you know, it doesn't have any… LTS, you know, guarantees, it's up to the implementations, and it's the micro-profile specification that has, you know, this issue, this dependency on, like, an old version of the OpenTelemetry API. It's like microprofile is saying, we have no LTS definition, but they're, you know, setting a higher bar for their dependencies than for themselves.
Because, you know, microprofile is just a specification, but the specification has a dependency which needs, like, you know, a backported CBE. So that's a strange sort of, contrast, and then I guess, I didn't understand the two-year bit, like, like, what… what… like, in your head, what could a policy look like from… from open telemetry that would satisfy the constraints of, like, this problem you found yourself in?
Like, you know, if we said, like, hey, we have these minor versions which have, you know, like, are marked as LTS or something, what… like, I'm gonna tell you right now, like, saying indefinite CVE backporting to LTS minor versions is off the table. You have to… you have to tell me a number of years.
Felix Wong (International Business Machines Corporation) 00:53:58 I agree, like, there will be a, yeah, a time limit, right? So, I do agree that your point, right? So… Yeah, so I guess I would bring it back to, like, the internal discussion as well within IBM, and I think then I can, like, articulate what I mean, what help we will need from, like, the open telemetry.
Java, group, in, in that issue, then.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:54:32 Okay, that would be very helpful.
Trask Stalnaker 00:54:35 Yeah, yeah, I think that's a really important, number of years. And the other question that, Felix, if you can take back.
is… Is there a way going forward? Like, I understand the situation you're in right now with this.
But is there anything you all can change going forward to not have this recur.
Like, is there some way that you all can… say, in your next version of your specification, not pinning it to a specific version of the OpenTelemetry API?
Felix Wong (International Business Machines Corporation) 00:55:15 Right, I… I think we might be able to, like, take it for, a discussion, I mean, in our, microphone meeting as well.
Yeah, I think… Deep, deep… Because I think that would…
Trask Stalnaker 00:55:30 That would make… that would make us pro… that would make us feel a lot better, or that would make me feel a lot better about, you know.
Pushing for this as a one-time, one-off kind of thing that we do to support the micro-profile group.
Felix Wong (International Business Machines Corporation) 00:55:46 I think, like, the last year or this year's, I think more… all the later versions of the spec… of the specification are more stable compared to, like… like 2021, 2022, like, those ones only have traces, right? I mean, some of them were having… Like, and then we introduce the, like, metrics and logs later on, right? So those are bigger changes for us.
I think now we have all three signals in it, and we are, like, just making stable changes and moving forward, right?
Trask Stalnaker 00:56:21 Yeah, I mean, for the most part, yes, there will, you know, there could be future things, like, I don't know if the entity work will leak into the API, configuration work, could…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:56:35 Profiling.
Trask Stalnaker 00:56:37 Yeah.
So there's definitely some, you know, the big signals are there, but there could be more… features added to the API, for sure. So, you know, and we always add them with no op implement… default implementation, so it's not breaking, it's just a matter of, you know.
Whether you all can set that expectation with your user and your specification, that it's not pinned to a specific version.
Felix Wong (International Business Machines Corporation) 00:57:10 Yeah, yep.
Yeah, I can bring it back, too.
John Watson 00:57:14 I think it would be fine to pin it to a specific major version.
Totally. It's the individual minor version, I think that's where the issue is.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:57:28 And I think there's a lesson here that we probably already know already, and we made this decision consciously, which is, like, we need to do everything we can to take concrete implementations of things, or limit the expansion of concrete implementations of things in the API.
you know, this problem emerged. We have a CVE in the API because we have W3, we have the baggage, context propagator, as part of the API, and there's reasons for that. But, like, you know, let's do everything we can to avoid things like that going forward, to make that, like, you know, a one-off exception.
Versus the rule, and… Yeah.
John Watson 00:58:07 Yeah, context and propagation is a… A very specific, tricky one.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:58:12 Right.
Trask Stalnaker 00:58:14 Context, I totally agree with baggage. I'm kind of confused about the spec on that, but… That's not here or there.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:58:27 Yeah, unfortunately, the ship has sailed, and we can't easily unwind it.
Trask Stalnaker 00:58:35 Cool, so Felix, you owe, why don't you… Wait until you… Discuss internally, and then, if you can open an issue, With, kind of, your findings and addressing these questions, and then we can have, kind of, a follow-up discussion after that.
Felix Wong (International Business Machines Corporation) 00:59:00 Yep, sounds good.
John Watson 00:59:01 Trask and Jack, do you think this is a thing that is worth having a bigger discussion? Not… I mean, this isn't a… this can't just be a Java issue, right? There's going to be, potentially, this could affect any language.
Do you think it's worth having a bigger discussion at the TC level, or the GC level, about what sort of guarantees The project should be providing to cases like this?
Trask Stalnaker 00:59:29 I think it's pretty clear, like, that we are doing… our current policy is the project-wide policy, and these major… our LTS is our major versions.
John Watson 00:59:41 Right, and that's why I'm saying… that's why I'm saying it might be worth having the discussion at the higher level, because of specifically what you just said.
Trask Stalnaker 00:59:50 Yeah… We could… we could mention the problem that arose, like, in the maintainer meeting.
I just feel like MicroProfile kind of got into a… got themselves into kind of a sticky… Wicked.
I'm hoping this is not a common problem, I haven't heard of it.
Anywhere else in… These… many years.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:00:20 I think it would be hard for me to actually articulate this problem in, like, a generic way. You know, it's… Like, I get what you're saying, John. I just… you know, I… you have to just know so much about, like, the Java ecosystem, and what MicroProfile did as a specification with implementations, and the fact that, you know, we have these minor versions.
And we're really intent on, you know, sticking with our minor version strategy. There's, like, there's so many things that kind of coalesced to make this problem have happened.
John Watson 01:00:56 Yeah, mostly I'm just trying to think that it would be good if we had air cover around decision making.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:01:04 I think we do. I think the project policy is pretty clear here, and I think we're sort of, you know, trying to be more accommodating than the project requires us.
Trask Stalnaker 01:01:18 I do think the way I would describe it more generally, though, would be If there are other implementations of SDKs.
If other people make an implementation of the API, they might… Theoretically want something like that.
But again.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:01:43 The project policy.
Trask Stalnaker 01:01:45 Yeah, of the API, pinning the.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:01:49 Despite it being minor.
Yeah.
Trask Stalnaker 01:01:51 Yeah.
But I almost don't want to open that Pandora's box, because I don't think it's a good project-wide change to have LTS minor versions.
I just… I'm… I'm only making the case here, because it's micro-profile.
And, I would like to support them.
If we can find… and help them to find a way forward. I think, Felix, that would go a long way towards making us comfortable, is if you all could come up with a way forward where this wouldn't be a problem in the future.
Felix Wong (International Business Machines Corporation) 01:02:33 Yep, sure, yep. Really appreciate you guys' help.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:02:39 Alright, thanks, Felix.
Felix Wong (International Business Machines Corporation) 01:02:42 Thanks.
Trask Stalnaker 01:02:43 Alright.
End of, we are at our time, and we… Hit our agenda.
So, thank you all.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:02:52 See ya.
Felix Wong (International Business Machines Corporation) 01:02:53 Thanks, Spite.
