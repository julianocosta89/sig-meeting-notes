SIG: Kotlin SIG
Date: 2026-07-27
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Francisco Prieto** 02:04 Hey, everyone.
**Ramachandra Bhardwaj** 02:07 Hello.
**Jamie Lynch** 02:14 Hey, everyone.
**Ramachandra Bhardwaj** 02:17 Hello.
**Jamie Lynch** 02:41 I'll just put a link to the meeting notes in the chat, so… Generally, what we do.
As I think there's a couple of new faces around here, if you're attending, you can add yourself as an attendee, and if you have anything you want to discuss.
Feel free to… Have stuff to the agenda.
**Ramachandra Bhardwaj** 03:08 Hey guys, I am a bit new over here. So, I just joined the, channel on Slack, two days ago.
It's just that, like, I am familiar with OpenTelemetry, I just want to kind of learn a bit more regarding how things are being done here, and, you know, contribute a bit more.
So, I already have a friend who is, like, a member of OpenTelemetry C++. He advised me, and to kind of, you know, get into this community, because it's really wonderful, and the amount of learning which will be there would be wonderful. So, I work with OpenTelemetry, Python, and Java, as part of my, I would say I am, like, an SRE for an organization, so… It's like, I kind of work with the Python and, the, Java libraries, so I'm, you know, like, willing to kind of learn more and implement, and learn a bit of the internals which are there over here. So, yeah, excuse me if I'm a bit nervous, but, this is my first time over here, and yeah.
**Jamie Lynch** 04:11 Oh, no, absolutely. It's awesome to have new faces on the call. Yeah, so thanks for coming on. So I'm Jamie, I'm one of the maintainers of OpenTelemetry Kotlin.
Yeah, we're definitely looking for folks who are willing to help out, so even just showing up, to these calls and, like, listening in and asking questions, that's super helpful.
Yeah, we're also looking for, like, people to, like, go through issues or open PRs. I think we've got loads of stuff on the issue tracker, so, Yeah, well, any and all contributions are helpful.
**Ramachandra Bhardwaj** 04:54 So…
**Jamie Lynch** 05:05 I'll just give it a couple more minutes for folks to show up. I think Hanson probably will be joining us, I know, but Jason… Said he's gonna be a bit delayed.
And yeah, feel free to add stuff to the agenda, because it's quite light right now.
I guess, if we don't… Of any other items, we'll just probably end up paying for EPRs.
**Francisco Prieto** 05:31 I don't have much.
**Jamie Lynch** 05:58 Cool, we can probably just make a start then.
And if folks do have anything they want to add to the agenda, or just discuss generally, then yeah.
Feel free to pop it into the doc, or just… Yeah.
Cool, so first agenda item, we probably need to think about a new release.
So… Let's check them.
That last shit. Yeah, so our last release was about 3 weeks ago.
So I think… It's probably time to kick one off.
was anyone aware of anything that we wanted to ship before then? I think I'll publicize it in Slack as well, Just because there's a couple of folks who would normally be here today.
**Hanson Ho** 06:53 If we haven't done that, update semantic conventions to the latest version.
I could put in a PR for that if we haven't done that.
**Jamie Lynch** 07:10 Yeah.
That'd be good to do.
Anything else?
Okay, if there's not anything else on that, just wait on the Slack. After… this meeting, asking probably Jason and Carlos if there's anything they want to include in that release, and if not, I'll kick it off.
Probably sometime this week.
Did anyone else have anything I wanted to add to the agenda?
**Hanson Ho** 08:01 Yeah, what's the latest on stabilization? Because I know a bunch of, milestones got created, but where are we in, stabilizing, I think, context is next. I think we've done attributes.
Because those are blockers for, logging and tracing.
**Jamie Lynch** 08:24 Yeah, that's a good point.
Yeah, so we do have milestone… a milestone for this now, called API Stabilization.
So… Yeah, I think Context API is the one for, kind of, effects for logging and tracing API, so that'd be good to… go over. It's supposed to just kind of a placeholder.
Basically saying, let's discuss… what the context API looks like, and what needs to change, if anything.
Bone.
**Hanson Ho** 09:04 Thank you.
**Jamie Lynch** 09:06 Go ahead.
**Hanson Ho** 09:07 Do we have an issue, or, because I know there's conversations around things like, automatic context propagation, things like that, but a lot of that is implementation. I think the API is… is… probably more… Or less controversial? Well, I mean, other than, like, whether or not we have a default of, of, thread base, and I think most of us agree that… well, I don't speak for anybody, I don't think we should have a thread-based one, and I don't know if we've come up with a consensus as a default.
**Jamie Lynch** 09:50 So, on the milestone, there was only one remaining issue, which was Creating a coroutine-based approach for storing the current context.
I've… opened a PR… that effectively… follows the same approach that OpenTelemetry Java is using, So you can basically use a cobutine context element to store the current context in a thread local, basically, whenever a coroutine starts or ends.
So, I guess that's the one part of the API service that we're currently missing.
**Jason Plumb** 10:37 Can you talk… Jamie, can you talk me through that? Because I'm… I don't… maybe I just take it for granted, because I've seen this stuff so long, but, like, what is even in the context API? Like, if I'm looking… on the spec, I see there's get the current context, attach context, and detach context.
Is that the entirety of the API?
**Jamie Lynch** 11:00 Yeah, I think that's, like… Part of it.
**Jason Plumb** 11:05 Oh, there's, there's Prieto…
**Jamie Lynch** 11:06 combo.
**Jason Plumb** 11:07 Yeah, let's create a key and get a value, set a value.
**Jamie Lynch** 11:11 Yeah, there's also a scope, but yeah, the contacts interface is probably a good place to… Start… So… Let's see… Yeah, so you can… Set values with a context key.
So it'll just be an arbitrary value.
**Jason Plumb** 11:31 Yeah.
**Jamie Lynch** 11:31 Reeve values given a context key.
You can attach a scope, which then is basically just a token to detach a context.
And then you can, like, store stuff, so spans and package.
Which is basically shorthand for… Setting keys.
**Jason Plumb** 11:55 Right, so if our goal is to stabilize this context API, this looks good to me, I think we can ship it.
Right? Like, I don't… I'm trying to tease apart that distinction between the implementation, being able to track context across threads or coroutines, versus just the API surface.
**Jamie Lynch** 12:14 Yeah.
**Jason Plumb** 12:16 And if we have to expand the API surface because we were too short-sighted and the coroutine stuff requires some extra, we can always add stuff, right? That's… when the implementation is coming, that's when we can add stuff, if needed.
It feels like this is pretty good so far.
**Hanson Ho** 12:35 Is default behavior part of the API contract?
**Jason Plumb** 12:38 I don't believe so.
**Hanson Ho** 12:40 Okay.
**Jason Plumb** 12:43 The… I think the only… Well, I wish… I wish Carlos was here, because he might know better than me.
I think the only case where that is true is for the propagators.
it's kind of a… maybe it's… arguably it's a design mistake that there has to be default propagators implemented in the API, but whatever, like, that chip has sailed so long ago.
I think everything else is just API.
**Jamie Lynch** 13:12 Cool. Yeah, it's… Definitely. I feel like I'm happy with the shape of these interfaces, and the signatures, and… yeah, everything else will just kind of follow on from that. I mean, it's just the one thing to follow in the implementation, really.
I think… Well, I guess, first off, does anyone disagree with that on this call?
Cool. Then, I think what I will do is… a good Razor PR to remove the experimental API annotations from these interfaces, but I'll… wait for Carlos to weigh in.
on bad PR before merging it.
**Jason Plumb** 14:04 Cool, I like that. Yeah.
**Hanson Ho** 14:15 There may be a few that are like that, like baggage, for instance. Those… even the propagator one, actually. Well, maybe not the implementation, but the API. They're… they're pretty straightforward about what they do. It's… it's how they're used, and… deployed, that is probably more controversial. I don't even think actually is that controversial with baggage.
It's very much, an outside the mainstream thing.
For us.
**Jamie Lynch** 14:51 Okay, cool.
Is there anything else you wanted to touch on… on that issue?
**Hanson Ho** 15:00 No, I just want to see what's next, cause,
**Jamie Lynch** 15:07 Cool. Yeah, I guess more generally… Those are kind of vague.
remaining API services, so… I doubt we'll get through all of them today, and… Yeah, I mean, we can spend a bit of time going through one or two of these, if folks want to do that. We could also review asynchronously. I'm… Open to what people want to do.
**Hanson Ho** 15:43 If there's time going through… Oh, go ahead.
**Jason Plumb** 15:46 I was just gonna say, I'm cool looking at a few of these smaller ones and not metrics.
**Hanson Ho** 15:52 Yes.
**Jamie Lynch** 15:53 a while.
**Hanson Ho** 15:54 Anything under tracing that is effectively blocking us, and logging too, but these are effectively the same.
**Jason Plumb** 16:02 I also apologize for having connected late, but I wanted to make sure that we acknowledge, is it Ramachandra? It looks like you've joined us maybe for the first time?
**Ramachandra Bhardwaj** 16:11 Yeah, I… This is my first time joining over here. I kind of, am not that well-versed with open source contributions, so I just want to kind of, you know, get into this and learn, but yeah, like, coming to OpenTelemetry, I would say I'm not, completely new to it, because I… kind of, like, worked on integrating it with few services for my organization, so I just want to kind of learn how the internals work, and yeah, just kind of contribute as much as possible.
**Jason Plumb** 16:44 Cool. Yeah, welcome aboard. Nice to have you.
Have you… I mean, so, you've looked at the source code for this repo, hopefully the Kotlin repo, and you're familiar with some of the contributing standards for OpenTelemetry?
Little bit.
**Ramachandra Bhardwaj** 17:08 The thing is, regarding standards, I wouldn't say I'm that familiar with it, but I just wanted to kind of ask.
how the entire life cycle of, you know, just kind of reviewing and adding a feature kind of goes, and that's the first thing. And second thing, I just wanted to kind of ask, is there any kind of, you know, beginner-first issue that I could kind of work on and, you know, just get started right off the bat?
**Jason Plumb** 17:34 Cool. Jamie, do you want to respond to that, or should I?
**Jamie Lynch** 17:38 Would you mind taking me in a little bit, and I can jump in?
**Jason Plumb** 17:43 Yeah, sure.
**Ramachandra Bhardwaj** 17:44 Yeah, sure.
**Jason Plumb** 17:44 So… Yeah, so I think, first thing to do is to look at the, like.
go to the repository on GitHub, and look at, like, the contributing.md file, look at the community guidelines, or the contributing guidelines on the community repo for OpenTelemetry 2, if you're new to that. And that will kind of give the foundations of, like, what we expect from people either contributing code.
The thing I think we're bad about in a lot of the repos that I help out with, and this occurred to me last week, actually, is we should have a clearer statement in there that we always welcome contributions in the form of code reviews.
So if you want to read a pull request that's open, if you have expertise, or if you have a familiarity with a certain area, or a coding style, or… If you see stuff that you think.
In an existing PR, like, not one that you've written, but someone else has submitted, if you want to review that and leave comments, or give a review, that's, like, certainly welcome, and that informs the other approvers. With more eyes, you know, we get better output, is the idea. So, cool.
As far as looking for issues, I think we're pretty good about using labels. When you go to the list of issues, there are some that… hopefully there are some that are listed as good first issue.
We can look at that real quick, Jamie, and see…
**Jamie Lynch** 19:10 We can have a look, yeah.
**Jason Plumb** 19:11 Yeah.
**Francisco Prieto** 19:15 I think there is none right now.
**Jason Plumb** 19:17 Okay.
**Jamie Lynch** 19:18 Oh, cool question.
I'm sure there probably are some good first issues.
**Francisco Prieto** 19:26 There's also…
**Jason Plumb** 19:27 He's done a really good job Amy's done a really good job of keeping the scope of these, like, fairly small, so there are a lot of… there are a lot of, issues that are kind of small.
well-contained scope, because in some of these… in some existing, like, longer-lived open source projects, you go in and as soon as you pick an issue, it's just, like, this thread that starts unraveling, and that's not the case here yet, because it's still pretty green.
I don't… I don't have ideas off the top of my head as to what… what to suggest, but… It does call out that we could be better about new first issue labeling.
**Jamie Lynch** 20:03 Yeah, for sure. I would say that the metrics API Has a lot of stuff that needs… doing, so… Yeah, I don't know.
hopefully that's not, like, too far off the deep end, like, just going into the metrics API. But there's a bunch of, like, interfaces.
Where you can kind of, like, have a look at the specification.
And, effectively, you'd just be, like, defining, like, a Kotlin interface for, like, measurement, for example.
**Jason Plumb** 20:44 And using Java probably as a reference, like, comparing what the Java APIs look like, and trying to kind of… follow suit, but maybe where it makes sense to vary and keep it more Kotlin idiomatic, that would be the thing to do.
**Ramachandra Bhardwaj** 20:59 I did notice similarities between the Kotlin and Java implementations. The first one is the scope, and the thing is, I work with Python implementation as well. That kind of heavily, you know, relies on context managers.
And that's the reason I did not find scope there, and yeah, like, I think with a bit of, like, I have a bit of knowledge regarding the Java, Open Delemetry repo, so maybe that as a reference, I think I can start implementing… implementing this one, yeah.
**Jason Plumb** 21:30 Cool.
**Jamie Lynch** 21:32 Awesome.
**Jason Plumb** 21:33 Nice.
**Jamie Lynch** 21:33 And, yeah, I'd say probably just… have a look through the issue tracker, and I guess pick something that… Would be interesting for yourself, or useful for yourself.
And yeah, feel free to ping me if you have any questions about what an issue entails, or how to go about it.
**Jason Plumb** 21:57 And if you want to send an indication that you're looking into something or starting work on it, you can just comment in the issue and say, please assign to me, and one of the Contributors will assign it to you, and that way… that just sends a signal that you're looking at it so someone else doesn't duplicate the work.
**Ramachandra Bhardwaj** 22:13 Yeah.
**Hanson Ho** 22:17 If you want something more self… Oh, go ahead.
Oh.
if you want something more self-contained, you can just, yeah, like Jason said, look through the issues. There are ones that are like, you know, we're missing this test case, or something, like, smaller, without having to, like, you know, build an implementation or interface from scratch as well. So, depends on when you want to… something kind of, you know, very small, or something that's a little meatier. There are 66 issues, there could probably be a bit more, so take your pick.
**Ramachandra Bhardwaj** 22:58 I think I would just kind of go through the performance and, like, go back, I mean, come back here and just, like, ask for an issue that I feel is, comfortable for me, but yeah, thanks a lot for kind of giving the, overview regarding how the current state of the, repository is.
**Jason Plumb** 23:17 Cool, yeah, thanks again for showing up and offering to help out, it's great.
**Jamie Lynch** 23:21 Yeah, thanks.
Cool.
What else should we testify?
**Hanson Ho** 23:36 If there's time, let's go over some of the, the APIs, I think, right?
**Jason Plumb** 23:40 Yeah, so after context, what about baggage? Are we close on baggage?
**Jamie Lynch** 23:46 Let's have a look.
So…
**Jason Plumb** 23:53 the top one.
**Jamie Lynch** 23:54 Yeah, stabilization… Package API, yes, that's just a placeholder. Yeah.
Let's have a look.
Yeah, so in terms of baggage, we've got… functions to… Get a value as a string… Set.
A value is a string of a ton of new baggage.
And remove it, and also coerce it to a map.
**Jason Plumb** 24:39 Which those map in the spec to getValue, getAllValues, setValue, removeValue.
And then… there's a way to clear… But that's really in the context, so… The baggage API must provide a way to remove all baggage entries from a context.
Do we have that yet?
It might be on context, right?
**Jamie Lynch** 25:05 We do, yes, on the context, so you can get clear of the.
**Jason Plumb** 25:10 Okay, so that's good. And then propagation. Do we have… we have a text map?
I mean, this is an implementation detail now, but do we have a text map propagator? We probably do.
**Jamie Lynch** 25:21 I believe we do.
**Jason Plumb** 25:22 Yeah.
I mean, I think this is pretty good, too.
New… this is an implementation detail, like, new… New values overwrite old values.
**Jamie Lynch** 25:42 Well, we can find out if it does that.
**Jason Plumb** 25:44 Yeah, sounds like a test case that we probably have coverage for already.
**Hanson Ho** 25:49 If we don't, that's okay, it's the API.
Or for this effort. It's not okay, okay.
**Jamie Lynch** 26:04 Let's see… so that's just a map.
Of baggage entry, so yeah, it should just override the baggage entry.
**Jason Plumb** 26:15 Interesting, though, there's maybe a… there's maybe an edge case here, where if we've… If we're one under the max entries… I don't know.
Do we still replace?
I don't care.
Yeah, this is good. I think we can… I think we're stable. I mean, I think we've covered the API enough to call baggage stable, so baggage and context.
with, you know, with Carla size would help, but I, I mean, I think baggage is close. What else?
**Jamie Lynch** 26:46 Yeah.
**Hanson Ho** 26:48 propagator?
**Jamie Lynch** 27:01 Okay, we can have a look at Fuck it, What's the best one?
**Jason Plumb** 27:11 I think the API's a little bit larger for this one.
**Jamie Lynch** 27:21 It might be taxed.
protection.
**Jason Plumb** 27:23 map propagator is in the API.
**Jamie Lynch** 27:25 Yeah.
**Jason Plumb** 27:26 Yeah.
And then it has… Inject and extract. Yep, we've got those covered.
I'm just… I'm scrolling quickly through the API on my end and just… Fewing stuff at you.
The context is a required component of both of those, yep.
**Hanson Ho** 27:50 Some of these being very straightforward, they're…
**Jason Plumb** 27:54 And the spec is, like, mixing API and other stuff sometimes, so it's a little bit hard to read, but you know this.
Still scanning here, so back to inject. A setter to set… A propagation key-value pair, which smells like inject to me.
Yeah, that is inject. Okay, I'm, I'm… okay.
Yeah, I think we're good on that. Text map extract, it's kind of the same thing.
Get and get all. So this is… let's see… So somewhere there's gotta be a keys function. So this is under text map.
Do we have a class called TextMap? We have a getter and setter.
**Jamie Lynch** 29:10 Yeah, don't we have a… We do have keys on TextMapGetter.
Don't remember what it's called Text Map.
**Jason Plumb** 29:20 Yeah… we don't have a class called TextMap.
Or we do.
We don't.
**Jamie Lynch** 29:27 No.
**Jason Plumb** 29:29 I don't know that that's required. Let's see…
**Hanson Ho** 29:32 Yeah, a getter and setter effectively… That serves the function of… of… that's the implementation, or the implementation of a text map ought to have.
Getters and setters.
**Jason Plumb** 29:43 Yeah.
It's got a keys function, yep, okay, and it's got a GET and a get all, that's… that maps all directly onto the API.
And then probably the same thing for the setter.
injectors and extractors as separate interfaces. Languages can choose to have A propagator type as a single object.
Or it can split them. We've chose to split them, lovely.
Implementations must… this is implementations, not APIs.
Does… text map… Propagator have a parent type?
**Hanson Ho** 30:30 Nope.
**Jason Plumb** 30:30 Okay.
**Jamie Lynch** 30:31 Bye.
**Hanson Ho** 30:33 Carrier doesn't even know how to type.
Carrier's just a ephemeral thing. Anything could be a carrier.
**Jason Plumb** 30:41 Yeah, totally, because it depends on the library, and, like, in most implementations.
like, one for HTTP, or, you know, probably dozens for HTTP, but, like.
Yeah, it depends on the underlying library protocol, all that stuff.
Like, the way you inject or extract contacts is different.
for a protocol like HTTP versus I don't know, message queue, or, you know, a database, what have you.
**Hanson Ho** 31:09 So the API seems very generic. It's like, these are the keys, this is how you grab stuff from the carrier, this is how you put stuff in the carrier.
It ought not function anything… it ought not do anything more than that.
**Jason Plumb** 31:27 Yeah… So, one thing that I'm looking at is whether or not We need a propagator, and it seems like… We don't, but we might have something that's missing. So, I'm reading the… I'm just live on this call, I'm reading the API and looking at the implementation, looking at the Java implementation, and there is a section in the API that talks about doing composites.
So if you have propagators being able to composite them, do we have a way to do that?
**Jamie Lynch** 32:02 That sounds familiar. I think in the…
**Jason Plumb** 32:05 In Java, they live on the interface.
**Jamie Lynch** 32:09 So, we have a draft PR opens up by… one, cool.
basically eat.
That's a composite sampler.
**Hanson Ho** 32:21 Yeah.
**Jason Plumb** 32:22 Yeah, not propagator.
**Jamie Lynch** 32:24 at Propagator, I think there is a… A way of doing that.
It might be on the…
**Hanson Ho** 32:33 Implementation.
**Jamie Lynch** 32:43 Yeah.
So…
**Hanson Ho** 32:46 Dsl.
**Jamie Lynch** 32:47 Hey.
Various publicators and… Yeah, composite Plumb together.
**Jason Plumb** 32:54 Yeah, this would be a question for Carlos, then. Like, does this need to live in the API?
At least on… Let's see, Java… It looks like it… doesn't?
**Jamie Lynch** 33:13 Yeah, sorry.
**Jason Plumb** 33:14 Let me double check.
**Jamie Lynch** 33:16 I think right now, yeah, this isn't the SDK.
Package, and not, like, a… publicly facing… like, API.
Moto.
So, I guess it depends on whether it is written in the spec as well.
**Hanson Ho** 33:32 This does seem super implementation-y.
**Jason Plumb** 33:36 Yeah, in Java, it lives in its own module called Context.
Or propagation, let's see.
Oops.
**Hanson Ho** 33:48 So basically, there's, like, a… cross-section of… that's, like, splits API and SDK by having both an API and an SDK.
That's not… I mean, it is what it is, but…
**Jason Plumb** 34:00 Yeah, context is its own module in Java.
So I don't think we need it in the API, is what I'm hearing. It's what it feels like to me.
And, okay, so the composite stuff, we do have. It's not in the API proper, it's in the SDK API, I'm gonna hand-wave over that. It'd be cool to maybe have final thumbs up from Carlos, but it feels good to me.
**Hanson Ho** 34:25 I feel like our SDK APIs were the, where the not-true API stuff are living.
That is… it's like the S… It's the CK API, for lack of a better term. So… I think, at least directionally, we're not including something that we don't want to support in the future. If anything, it is… it is… we want to move more stuff into the API. So, If Carlos signs off on it, I'm happy with… A minimum set.
And if we want to add it later, we don't even have the revenue version, or major version.
**Jason Plumb** 35:05 So do we have a way on the main OpenTelemetry interface?
To get the global propagators?
**Jamie Lynch** 35:17 Let's check.
**Hanson Ho** 35:21 Yes. Yes.
**Jamie Lynch** 35:23 Well, it would be one propagator,
**Jason Plumb** 35:26 Yeah. So they… the spec is, again, weird, but it says… The OTEL API must provide a way to obtain a propagator for each supported propagator type.
I guess if we only have TexMac Propagator.
Then… we're… we've completed that requirement.
**Hanson Ho** 35:48 In the API, it only takes…
**Jason Plumb** 35:50 in the API.
**Hanson Ho** 35:52 Which is true.
In Java, are there other propagator types in the API? Or are there, again, all the propagator modules, so…
**Jamie Lynch** 36:04 Bombay.
**Jason Plumb** 36:05 Yes, go ahead.
**Jamie Lynch** 36:08 Oh, I was gonna say the spec says that TexMap propagator is the only type right now, but it might be open in future, but I'd be interested to hear any further context, Jason.
**Jason Plumb** 36:21 Yeah, there's an intermediary type in Java called context propagators.
when you call get propagate, so on the OTel API, you can call getPropagators. It returns this context propagators interface.
An implementation of that interface, and it has methods to create… from a text create context propagators, get a no-op context propagators, or to get a text map propagator. So that's the only… that's the only type they support.
That was the question, right? Like, are there others? It's just… just technical.
**Hanson Ho** 37:02 Yeah.
So is a context propagator a propagator, or it's just using that word?
**Jason Plumb** 37:08 It's like a wrapper, it's plural. It's like context propagators, so it's, like, kind of utility class around this stuff.
**Hanson Ho** 37:16 Okay, if it's not implementing the interface, then it's not.
**Jason Plumb** 37:20 It is, it is the interface, and there's only one implementation, it's the default one.
**Hanson Ho** 37:26 Oh, right, because there's no… there's no higher level… yeah, textile propagator is the highest interface, so there's no…
**Jason Plumb** 37:33 It is, yeah.
This is just sort of, like, a wrapper utility around that.
**Hanson Ho** 37:37 Yeah…
**Jason Plumb** 37:38 Yeah, I think… I think we're good, then. Let me make sure there's nothing else. So, global… Getting set… oh, set global propagator?
What? I don't think Java has that, does it?
**Hanson Ho** 37:54 And that wouldn't be part of the propagator interface, that'd be part of the OpenTelemetry interface, right?
**Jason Plumb** 38:00 It smells like that from the… from the spec.
Sets the global propagator instance. Ugh, I don't think… I don't think we have that.
**Hanson Ho** 38:15 The word global just…
**Jason Plumb** 38:21 Oh, wait, wha- oh.
Interesting.
So there is a method on the… I'm, again, quoting from Java over here. On the OpenTelemetry interface, there's a method called propagating.
you pass it one of these context propagators, which you can create one of those with a text map propagator. And when you call propagating.
with this new thing, what you get back is another OpenTelemetry instance, or presumably a wrap… like, it's unclear if you get back a different instance or not, that's not part of the contract, but presumably that's the one you want to be using from there on out.
If you've called propagating.
**Hanson Ho** 39:04 So you're deriving a new instance of OpenTelemetry from the text map.
**Jason Plumb** 39:08 I mean, that's probably not what's actually doing, cause… I'm guessing it's just… Swapping out an implementation, but… They're kind of treating it like it's immutable.
**Hanson Ho** 39:22 So if it's not in the API docs, That doesn't sound like something we should include.
**Jason Plumb** 39:29 It's… what do you mean, if it's not in the API docs?
**Hanson Ho** 39:31 So, does the API docs, or the API specification talk about context propagating wrapper?
**Jason Plumb** 39:37 No, but it says you have to have the ability to set the global propagator.
So, that vowel there on line 74, that's settable, right?
It's not, because it's a vowel. So…
**Hanson Ho** 39:51 Instead of a pre-build.
Potentially.
**Jamie Lynch** 39:58 I guess?
**Hanson Ho** 39:59 It's configurable.
**Jamie Lynch** 40:00 problem.
From my point of view, I think the… we're able to configure the propagator that's used for an OpenTelemetry instance, and… that might not be semantically exactly the same, so I think we should check with Carlos, but it feels like that's the spirit of what it's trying to achieve.
**Jason Plumb** 40:27 Yeah, I can't tell from the spec, it's kind of… terse, and I'm also just kind of reading on the fly, but…
**Jamie Lynch** 40:33 Hmm.
**Jason Plumb** 40:34 We… I think we're missing the setter.
the global setter for the… set the global propagator, that seems like an API that we're missing.
**Hanson Ho** 40:47 This notion of global is…
**Jason Plumb** 40:49 Not great.
**Hanson Ho** 40:52 Yeah,
**Jason Plumb** 40:55 Yeah.
**Hanson Ho** 40:56 Unnecessary. And not great.
**Jason Plumb** 41:01 Yeah, I mean, I don't know the context around this, but I'm, you know, this is something that might have been bike shed for a long time, 5 years ago.
**Hanson Ho** 41:09 Can we read the 39 comment?
Issue with the bike shedding, because.
**Jason Plumb** 41:14 I mean, I'd have to go track it down.
**Hanson Ho** 41:17 How many global things, like, truly global, not, like, instance-wide, do we have on the API?
**Jason Plumb** 41:26 In Kotlin.
**Hanson Ho** 41:27 In college, yeah.
**Jamie Lynch** 41:31 I don't think we have any globals right now.
**Jason Plumb** 41:34 Yeah.
**Jamie Lynch** 41:35 Voice, we kind of made.
**Hanson Ho** 41:37 I… I would hate to… I would want to clarify the utility of this before adding it, because.
**Jason Plumb** 41:44 Well, and… well, so, like, in Java, for example, it's not truly global, right? Like, they've… they've worked… like, maybe the spirit is you need a way to set it after OpenTelemetry has already been created, for whatever reason.
And that's fine, it doesn't mean it's necessarily global, it's just, like, there is one for the OpenTelemetry instance, is the way I read that. And the way that… it seems like the way that Java has worked around it is by returning an instance that you should then use that's been configured.
**Hanson Ho** 42:13 if we're saying propagators can be, reassigned at runtime after its initial creation, I think that's very fair.
**Jason Plumb** 42:22 Yeah.
**Hanson Ho** 42:25 So if we can clarify that point, maybe we'll mention Carlos… just at-mention Carlos and say, hey, what does global mean? Because, effectively, Java is not implementing a global, it is implementing a clone.
To get around mutability reasons.
**Jason Plumb** 42:43 I think it's worse than that, actually.
**Hanson Ho** 42:45 Okay, what?
**Jason Plumb** 42:46 I'm looking at it now, and I'm like, if you have an instance of OpenTelemetry, and you call propagating.
So, that's… Oh, wait, what?
**Hanson Ho** 43:00 These are all sounds I don't like to hear.
**Jason Plumb** 43:03 Okay, sorry, I missed… I missed this when I was reading it the first time.
**Hanson Ho** 43:06 Don't forget.
**Jason Plumb** 43:07 Propagating is a static method, it's not… a method on OpenTelemetry. It's a static method.
I don't think they have a setter. I think they don't have a way to set the global.
Which I wonder if there's… I'm gonna see if there's an issue, just because I think it's funny, and we're all standard time.
**Hanson Ho** 43:29 I'll take a look at when that line where the spec was added. If it's, like, 5 years ago, no one's touched it. It may just be something that… you think about when you initially create the API, and you don't think about it after, because who the hell would want to do that?
**Jason Plumb** 43:51 Well, this is something we've identified, at least, is maybe… maybe a speed bump or a hurdle before we can stabilize propagators, but I think that's… I mean, we're looking pretty good. So, context baggage, propagator, all… I mean, context and prop… and baggage, to me, look good. Propagator, maybe this is the remaining open question?
**Jamie Lynch** 44:11 You know? Yeah, this is awesome. I will… Go away and probably update those issues tomorrow, and… like, remove annotations with PRs, tagging relevant people,
**Jason Plumb** 44:25 Yeah, awesome.
That's killer.
**Jamie Lynch** 44:27 Cool. Yeah, I know we're nearly at time, I just wanted to mention again, I think we're due a release, so… if… Anyone had anything they wanted to get included in this, probably now's the time to… Tell you what it is.
Otherwise I'll try and ship it mid-next week.
This week, sorry.
**Jason Plumb** 44:55 That seems good to me.
We are using the environment secrets now, right? So, if it breaks… Hopefully it doesn't break.
**Jamie Lynch** 45:03 Exciting times.
**Jason Plumb** 45:05 Did I… I removed them, I think, right? Yeah. The… the non-environment secrets, I think I removed.
Double checking.
**Jamie Lynch** 45:14 Yeah, so fingers crossed to…
**Jason Plumb** 45:16 I did.
**Jamie Lynch** 45:17 Just fuck.
**Jason Plumb** 45:18 Okay, it will. It'll be fine. It'd be great. Yeah.
**Jamie Lynch** 45:24 Cool. Anything else anyone wants to touch on quickly?
**Ramachandra Bhardwaj** 45:33 I just went through the, sorry.
So, yeah, I just went through the issues. So, instead of that, I just found out that, yeah, measurement is one thing that you just mentioned, right? That we kind of need to implement the API for that. And the other issues that I saw is there isn't the support for OTLP gRPC export. Is that also a bit of a… Like, primary issue that we need to kind of have, or… Maybe I could just pick up the measurement, API implementation.
**Jamie Lynch** 46:07 Yeah, I'd say that in terms of scope, probably the measurement API feels like a smaller one to get started with.
I think GRPC… I think, yeah, that… I don't think anyone's working on that one specifically. There is someone… working on, I think Jason… exports of OTLP.
Yeah, if someone's not assigned to an issue, feel free to comment on it, and one of us will assign you.
**Jason Plumb** 46:44 Cool.
Thanks, everyone!
**Ramachandra Bhardwaj** 46:48 Thank you.
Thanks. Bye.
