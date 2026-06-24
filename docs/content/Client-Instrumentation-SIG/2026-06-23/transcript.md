SIG: Client Instrumentation SIG
Date: 2026-06-23
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 03:58 Hello.
Guess we're waiting for… I guess I start the meeting, I guess, I could… Do the dock if, no one else shows up.
Typically, Martin will run this.
But if he's not here today, I could do it.
We can wait… well, I mean, it's 9.04, so… Why don't I just do it? If he shows up, I could, revert this factual.
so here's the doc for any folks that are new, for agenda items.
I'm gonna share my screen… Everybody can see it.
Whoops.
Supposed to be sharing a window.
Let's share properly.
Everybody can see my, screen.
Cool.
What we lack are agenda items!
So, A bit of an… I'll wait a couple minutes and see if anybody wants to add a… Agend items, but, I'll add one.
So for… for folks new to this meeting, we typically talk about Cross-cutting concerns of end-user apps.
And the way we all use OpenTelemetry a little bit differently, for various platforms, that share… share the… I am not in the back end.
kind of distinction. So a lot of semantic convention talk, a lot of usage talk, et cetera, et cetera.
Alright, so I can start if… There's no other one. Topics. So we added the, crashed semantic invention, a few weeks ago, and on Android, we were… we wanted to use it. It basically changes the event name from device.crash to app.crash, and, you know, tweaks a couple things. Actually, not really a lot of other things. But… We decided to hold off for now, because we have to decide, whether or not we want to, actually, replace the existing log that we have that is not a semantic convention. The name is different, so typically, if it's a semantic convention, we don't change, until there's a major version.
Or, or, you know, if it's a net new one, then it's totally fine. But what we have was basically an undefined state that some people are practically using.
So we were excited to, like, switch it over, but then we kind of backed off and said, oh, maybe, maybe we shouldn't do that, simply because there are people who are downstream, or, yeah, who are expecting to, you know, to have this name.
So, we were wondering, how we want to kind of go about, rolling this out. So, do we treat what the previous state is as a de facto convention, and follow the same rules of deprecation, and then, you know, et cetera, et cetera, before we swap this in?
Do we rip the band-aid and say, hey, it's not Spanish Convention before, so we'll just… it's the Spanish Convention now, so hey, even though it's a minor version, we're there.
Or do we want to do a fallback mode? Which is basically, we will… for new folks who are coming to the project, we'll use the correct semantic convention ones, but there is a legacy fallback mode you could basically use to go use the old step. Will be, you know, basically a configuration flag that applies to the whole whole project. The institution under our control will fire with either legacy names or the correct names. And then defaulting to on or off, you know, things like that. So… I was wondering what other platforms are doing, when they have, effectively, new semantic conventions, that are not simply additive to, the attributes.
But rather is a swap of either meaning or name.
**Cleo Schneider** 10:24 Yeah, we definitely have.
have run into this issue, this sort of migration issue.
And I think for… for logs and for traces, there's some amount that we can sort of mask for customers in the… in… in our read APIs to read both and stitch those things together in some way. Metrics is where it gets really gnarly, though.
Because, you know, some of those metrics are namespaced, and then you can't actually do aggregations across those two different populations for reasons, you know? So we haven't figured out a great solution to that, but that's definitely something that we care about, and are thinking about, and would love for this group to Put some intention behind, like, what do we expect?
you know, hotel, SDK developers, basically, to do.
Yeah, and it feels like there needs to be some mapping layer. You know, there needs to be some way to say, these things, they're the same, we should treat them as the same. I'm not… I don't know what… what that thing is.
**Hanson Ho** 11:45 Yeah, it's… it's… it's… I think… I think the tricky… the trick here for us is… is if we are going from one semantic convention to another, or we're doing different versions, there… there are protocols to basically say, hey, you know, you pin yourself to a specific semantic convention, and if you iterate on the other, you move on to the other one, you… you can expect some changes, because some of them are marked as development, or whatever it is.
But we're basically starting off on nothing. So, do we treat it as nothing? Or do we basically treat it as a de facto version. It's almost like… the easiest thing to do would be… would be to just treat it as a thing, but then there's no version, right? I mean, in the old… if there was an old version, just say, hey, I want version 2.
Right now, it's like, I want version null. Yeah. So, effectively, this is, this is… and… and what we don't want is, is, like, proliferation of, oh, I want Legacy for this, and… but the new for that, because we haven't really used that before, so… that combination is just messy, so I think for us, like, we are really… we're likely gonna go with, like, the fallback kind of mechanism, basically version null, and then it's just a matter of defaulting on or off.
But, so, and… but that's at the production side, obviously. On the… on the collector side, they could do whatever they want. So they could do their own mapping, you know, I only care about these three events, they look the same, we treat them as the same. They could even, like, you know, at the collector side, you know, remap and literally treat it as one, so they don't have to change their dashboards or whatever. But that's up to them. On the SDK layer, we still have to maintain that level of.
what do we output, you know? And Others must have done it for hotel, because… most of the client instrumentation are new, and are being semantic conventionized. So… what… what have others done? I think we were a little bit less careful for some of the other ones, or some of the other ones are… are… I should say, if they're just additive, then we're like, you know, it's okay. But this one is a little name change, so we're like, ugh, I don't know about that.
**Bryan Atkinson** 14:10 Seems to me Clients are uniquely challenging here.
because, you know, people ship these apps with a specific version, and so this isn't even a problem that's gonna go away when we go from null to 1. I mean, it's… different clients writing telemetry, using different versions of the spec is just a problem.
Like, they're writing it at the same time, you know, is just the problem, I think.
You do need a solution for.
**Hanson Ho** 14:38 Yeah, the long…
**Cleo Schneider** 14:39 once it's shipped, it's there forever, because, like, getting a user to upgrade their app is impossible, you know? So, like, the moment that it's out in a mobile app, you can consider that a forever problem, you know?
**João Oliveira** 14:55 Thank you.
Oh, sorry, go ahead.
**Hanson Ho** 14:58 No, go ahead, go Xiao.
**João Oliveira** 14:59 Yeah, just sharing that. We… we've been seeing a lot… and I think OpenTelemetry is… is… very attractive, especially in the client instrumentation space, to the sort of devices that are very rarely updated, even if it's not, Because the users don't want… don't want it. Sometimes it's just, you know, over-the-air updates are just, complex.
And so we, you know, we sort of expect… Already for… to have a wide range Of… of versions that, that need to be… be supported. You know, we have customers talking about… talking to us about 20-year… Span, like, having two updates in a 20-year time span, which is absolutely crazy.
But… I think open… open telemetry does, you know, lean itself a lot to these customers, because obviously they don't want to vendor lock these devices. That's… that's… obvious. I think in this, in this, This is very complex, and I think every approach that you sort of suggested, Hansen, as its, pros and cons, like, everything, really.
For me, I think the one, sort of guideline that makes sense is for… you know, a given SDK version To be fully compliant with a given semantic convention version.
So that, you know, if you're… you know if you're on SDK version X, you're on SENCOV Y 100%.
And that… You know, telemetry from a single source is… is… stays somewhat predictable within that version.
I think where it starts to be really problematic is… when, you know, get a couple of events. One is, is, is, working with, is compliant with version, I don't know, 1.2, the other is 1.3.
And so… when we talk about the null problem, you know, if you're on version 1.2, and on version 1.2, that's… the semantic convention for that field is none, is null. I think it's totally acceptable to… to, to, you know, not comply to the newest versions.
But as soon as you swap.
It, it, it should be, transparent. And so… Where I want to get to, maybe, is, I think the, the sort of… Legacy fallback, the last option you described, where you're like, you might want to legacy fallback, is the more robust one, even though it might be a bit confusing, but maybe it becomes more manageable.
If we… if we say something like, this SDK version goes up to semantic convention version X, But you can configure it to go back I don't know, maybe not all of the versions in history, but, you know, there's a… a sort of trail of versions that you can sort of configure the the SDK to go back to, and maybe that makes it a little bit more manageable. I… The closing remark, I admit that I don't know if this is entirely Feasible to… to… to implement or not.
**Hanson Ho** 18:43 So typically, instrumentation will bind itself to a particular SEMCON version. So it'll be like, I'm… I'm blah blah instrumentation version 5, I look at convention version 4. So if you upgrade me to 6, I might be using, you know, a different version, and… and that's generally… and if… and only upgrade the instrumentation, if… if you're ready on the back end to take in the new telemetry from the new version.
on Android, and I… probably for other end-user-facing SDKs and instrumentation.
there's a monolithic nature to… to it, so, we can't piecemeal say, hey, I want older versions of the instrumentation, but keep, like, the new versions of, of, of, of SDK, or the agent. So you're basically… you… you take all, or you take, you take none. So it's… it's, it's… it's… it's doubly confusing, in that we can't advertise, oh yeah, we are using semantic convention in version X, because we aren't at all. Or rather, some instrumentation is and some isn't. So, where… users of the SDK instrumentation typically have the choice, to, like, opt in and opt out, by what version they take in. We basically say, you're getting it all, you're getting none of it. So, partly it's architecture, partly it's just the nature of… the way these interpretations are written, they're bound to an interpretation API, that we expose in the project. So, these are, you know, for lack of a better, sense, it's one… It's one thing. And maybe the other client SDKs are kind of a little bit more modular in that way, but, I don't think there's anybody here that is familiar, unless Brian, Cleo, you've looked at the OpenSelemetry web SDKs and browser SDKs and instrumentation.
**Bryan Atkinson** 20:49 Not to the point to be able to answer that question.
**Cleo Schneider** 20:58 Oh, hopefully… soon.
**Hanson Ho** 21:04 Yeah, it's… we have a lot of, emerging problems that I think, it'd be good to kind of, like, share, here, even if we have our own kind of solutions. We're probably just gonna go with, you know.
Fallback flag, which basically opts you out of, of… All the semantic conventions. All defined as some… specific set of instrumentation that has been upgraded to, the, the, to, to the semantic conventions.
Probably default.
off.
I don't… I don't want to promote… legacy behavior as the easy way. I want to make you have to work for legacy, and by work, I mean setting an attribute. It's not that much work as an app developer, so I'm hopeful… I'm hopeful that's acceptable. But I guess we're not… necessarily always used directly, were used by some upstream SDK, like, you know, or a vendor that wraps it, like Elastic or other folks. So, they could make the choice for their customers, I suppose.
**Bryan Atkinson** 22:14 We're… I mean, so we're… we're new to… to… to OTEL here, and this is, I think, one of the biggest challenges that… that we've identified, is that it's, like, it's kind of… for us, this is a big shift in the sense that you know, with OTLP, like, we do have a server that, you know, receives these OTLP, or these OTL requests, like, with the logs or whatever, and so we could conceivably do something… And, like, you know, put some mapping in, detect the version of the data that's being sent, and then, you know, map it on the server side. But then, how does that… like, how would that be, you know.
part of the convention itself, right? Now, if we were to do that, we wouldn't be able to say we're OTEL compliant here, because we're doing a bunch of manipulation.
On the receiving end.
**Hanson Ho** 23:08 Collector manipulation is actually a fairly, or we wouldn't even call manipulation, but, like, cleansing mapping is, is, I think a accepted, part of the SDK, or the, the hotel toolbox. But where it gets kind of hairy is.
you could do everything there, and the SDK could just be a mess. In which case, then.
using a collector piece is not optional, but effectively mandatory, which increases the friction of adoption. So, I think at the SDK level.
we need to be as, as, as, as predictable, and ideally as configurable as, as, as we can without going overboard. And if what we, what we offer, like, at least this is kind of my opinion, if what we offer isn't, isn't satisfactory for all the use cases. Well, there's your, your kind of, you know, ejector seat, or kind of a, you know, secret passage of Doing stuff yourself.
Hell, you could even do it on the SDK level with an exporter by doing that remapping. Well, maybe not, actually. That'd be pretty hacky, changing it at the exporter level.
**Bryan Atkinson** 24:21 How… can that mapping somehow be encoded in the convention, you know, to say, like, so, semantic convention, you know.
1.0.2, you know, there's some, you know, deprecated field in the previous minor version, and the new field is, you know, properly described in the convention. Like, can that mapping be somehow Enforced on the collector side.
**Cleo Schneider** 24:47 I think the thing that is wild about that, though, is that, like, yeah, in new versions, you'll have that information, but most of your apps are going to be sending the old version with no information and no knowledge of the new semantic convention. So it really does push the problem into the collector, which then makes your data less portable.
Because now, each collector is gonna do something somewhat custom in order to make this all… viable for you, right? And… and a sort of continuous experience for you. And so, it's a, it's a really hard problem, I think… Yeah, I don't, you know, like, once it's out there, I don't know how you future-proof it, right? You can't. You just can't.
**Hanson Ho** 25:39 One thing good about these mobile apps is that, and I think for web, it's actually probably pretty easy because, you know, you control the application code, I mean.
as much as you can, but, you know, for mobile, there is a… there is an aging out, even though, adoption of new versions is slow. Folks do… gradually age out, because of upgrade… phone upgrades or uninstalls, and, if your Apple, draconian, OS update policies will make certain apps, unusable, after a few years. So, Android, unfortunately, we still support SDK21, We just went to 37, so that's 16 years. So, you know… And you can also say, I don't care about those people, which is another valid way of going. So there are ways of, like, you know, 20 years is… theoretically possible, but we could safely ignore data coming in from 20 years ago. In fact, on Android, it's really impossible. But, the cutoff, the practical cutoff, if you say, hey.
these are really old users, we don't care, it's not worth it for us to do that kind of consolidation, or, not consolidation, reconciliation.
So, sometimes it takes care of itself, but it does take a few years, and that's… that's the, that's… that's significant. It's not… it's not, you know, a few months, it's probably a few years, a couple years at least.
So for other…
**Ben Joseph** 27:22 Sorry, Hanson, I just want to bring up, like, so, I was talking to this, talking to Martin about the same problem last week, and he brought up Autel schemas, I think, which should help with this problem on the consumer side.
But I think it's also expected that with the telemetry, we send the schema version, which I, at least for Android, I do not see.
But has anybody explored this as a possible solution, at least on the collector side?
**Hanson Ho** 27:53 We haven't, just because the schema version is, I believe, tied to, the tracer or the logger, and not necessarily the event.
If I remember correctly. So I don't know how that maps into this whole thing. Certainly, semantic conventions aren't bubbled up through that.
So, there may be something there, but I haven't worked… I'm not familiar enough with that layer to see if that's a viable solution. And, of course, for our specific problem, it's not one old semantic version.
to another. It's no semantic invention, two semantic invention. So, you know, it's a bit of a… it's a bit of a… an edge case, which is good, because it's, you know, not applicable for a lot of people, but also bad, because we have nothing to fall back on. It's literally… Alright, here's the… you're… you didn't have cement before, now you do, so… Well, we're coming up on time. Is there another… we have about 2 minutes. If there's somebody who has another topic you want to discuss before, we could kind of… go there.
But if not, Yeah, we'll see y'all in two weeks. Hopefully I'll have my… the async stuff that we talked about, two weeks ago, ready in a… in a PR or something that we could, you know, discuss further. Thank you for the suggestions last week. I just haven't had time to go and actually do it.
**Cleo Schneider** 29:34 Sweet.
And… may… we might have an interesting persistence thing to… to show as well. So, yeah, I'm really curious where that landed, Hanson.
**Hanson Ho** 29:48 No, I think the suggestion is great. It just adds to what we initially thought about, and allows for a little bit more, a little bit more nuanced. So, it's just kind of flushing… well, it really is just taking… literally taking an hour to write this stuff down. Which sometimes, when it's, like, the ninth thing, it's… it… The queue is prioritized, so…
**Cleo Schneider** 30:11 Yep.
**Hanson Ho** 30:11 Totally. Let's not starve all the way to next year, but… Good seeing y'all.
Happy Tuesday, and see you in two weeks.
**Cleo Schneider** 30:24 See you next time, y'all.
**Hanson Ho** 30:26 I…
