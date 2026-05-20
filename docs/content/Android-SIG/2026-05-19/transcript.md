SIG: Android SIG
Date: 2026-05-19
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 02:19 Hello.
**Jason Plumb** 02:21 Good.
Getting set up. One sec.
**Cesar Munoz** 02:38 Good morning.
**Hanson Ho** 02:40 Hey!
**Jason Plumb** 02:42 Good morning, Cesar.
How's that look?
There we go.
Well, the empty agenda!
**Hanson Ho** 03:03 And yet, they'll still take an hour, because… We're gonna find items.
**Jason Plumb** 03:09 We're pretty good about that.
Yeah. Welcome new Jason, at least I'm gonna call you New Jason for one…
**Hanson Ho** 03:17 Sounds like a good idea.
**Jason Morris** 03:20 Yeah?
**Jason Plumb** 03:20 Are you with Embrace?
**Jason Morris** 03:23 Yes.
**Jason Plumb** 03:23 Nice, nice, welcome aboard.
**Jason Morris** 03:25 Thank you.
**Jason Plumb** 03:27 And I have, for years, been mostly just putting Jason in these meeting notes, but I'm gonna qualify it now.
There we go, I can no longer get away with that.
**Hanson Ho** 03:37 I mean, I always put my last name, but seriously, I should be.
**Jason Plumb** 03:41 There's no other Hansons, come on.
**Hanson Ho** 03:43 There are few, there are few.
**Jason Plumb** 03:46 Not in OpenTelemetry.
**Hanson Ho** 03:50 Still win the Google Wars. The architect from Singapore?
**Jason Plumb** 03:54 Oh, okay.
**Hanson Ho** 03:55 Ugh.
**Jason Plumb** 03:57 Well, without an agenda, we'll do the thing we can normally do, which is just look at new pull requests, look at new issues, maybe that'll spark some ideas, or get the juices flowing, and we can talk about a release.
So, let's look at issues first. It looks like David, who is on the call, has submitted a long press click detection, as promised. That's awesome. I have not looked at it at all yet, and it looks like other people have, so I'm guessing that's on its way. Is there anything to talk about on that one?
Sounds like… not. What's… I think we've got a little traction on the semantic convention behind this one, right?
Hanson, I think I saw some updates.
**Hanson Ho** 04:41 Yeah, I updated it a week… couple weeks ago, maybe, or…
**Jason Plumb** 04:45 Okay.
**Hanson Ho** 04:46 Last week.
**Jason Plumb** 04:48 Okay, and I, I think, yeah… Give… give one of these, maybe somebody will notice that.
I would love to get this in, it's been just going off for so long.
**Hanson Ho** 05:03 Yeah.
**Jason Plumb** 05:04 Nope.
Okay, what else? There's nothing really new here. Let's check out issues.
And David, I'll monitor chat if there's anything you wanted to… comment about your PR, but it looks like it's going, and I honestly have not looked at it yet.
Let's see… Yes, I think we talked about this last week, right?
**Cesar Munoz** 05:39 Yep.
Yeah, I just created the issue, but forgot to.
Follow up on that.
**Jason Plumb** 05:44 Probably boost that up a little bit, with a little… a couple sentences of content, maybe, so that we remember what we were talking about.
**Cesar Munoz** 05:53 Yeah.
**Jason Plumb** 05:57 Yeah, this is interesting.
Yeah, let's… let's talk about common.
So, as a quick refresher… The common module has a few, kind of, critical pieces of… our project.
Guess we could peek in here first.
The most notable of which is the OpenTelemetry Rum Builder and the pre… whatever it is, pre-configured, predefined… Aren't those… no, those are in core, different than common, sorry. I'm gonna have another sip of this coffee.
Alright, so what is in here? Roam constants… Network extractor… Carrier… Carrier seems like it might be specific to one instrumentation, but I'm guessing it has to be shared, huh?
**Hanson Ho** 07:11 If it's a… Sort of a data class type thing that needs to be… Yeah, I…
**Jason Plumb** 07:20 Like, maybe it's part of the network change detection stuff, which kind of leaked out.
**Jamie Lynch** 07:26 Yeah. It feels like… There are a few things in there that could probably be in more specific controls, and that is one of them.
**Jason Plumb** 07:35 Yeah, and the network stuff seems to kind of be a natural grouping for this so far.
time… And utils, okay, that's cool.
So the question being posed is, what do we want to do with it? Should we work towards stabilizing it? Should… like, as its own artifact? And I think it sounds like Jamie says, I'm not sure that we're needing to do this.
Because it's mostly internal.
**Jamie Lynch** 08:08 Yeah, exactly.
**Jason Plumb** 08:09 Yeah.
**Hanson Ho** 08:10 It… it ought to be. I feel like there's probably a few things in there that can get rid of it, that we can pull out, but, like, everything in there should just be… You need this because you need one of the actual dependencies.
Or not even, maybe.
**Jason Plumb** 08:26 So, Constance is not marked internal.
So, we do have people that could be using this, and what in here is interesting?
There's no way this is still used, is it?
App star spanning.
**Hanson Ho** 08:46 If it's used, it would have been used in an instrumentation.
Do we still…
**Jason Plumb** 08:51 Generate a startup span?
**Hanson Ho** 08:55 Probably.
I don't think you removed it, right?
**Jason Plumb** 09:00 We do. Okay, so it's activity start.
It's not really… Hmm.
Hmm.
It's weird, I don't like that the app start is hidden within the activity instrumentation.
Seems like that ought to be a separate thing. I'm going to make an issue for that.
**Hanson Ho** 09:27 debate what AppStart means.
That'll be fun.
**Jason Plumb** 09:32 We could spend an hour doing that.
**Hanson Ho** 09:39 But that's probably stuff that's been there for, like, 5 years, right?
**Jason Plumb** 09:44 Easily, yeah.
**Cesar Munoz** 09:44 Yeah.
**Jason Plumb** 09:46 4, at least.
**Cesar Munoz** 09:47 And I think it's the case for the whole common… Module, and probably the other service module.
I agree to separate issues, but those… I would say that they look quite similar in terms of They should be just internal tools that We moved around.
Because we've done… A lot of refactorings to this repo.
And now that I think we've reached, somewhat stable architecture for the project.
It's probably a good idea to say.
what I think is what Jamie was mentioning, which is… Probably just… Remove them, maybe just move the code that is in there to the places where it's actually needed, and Just ideally not stabilize those at all.
I mean, this… this constants… They're not internal, but essentially, they mostly just… Define stuff that should be defined in the semantic conventions anyway.
So, people shouldn't be using those.
**Jason Plumb** 11:00 Right, I mean, we should at least… we should at least market, maybe, whatever the thing is, experimental. Is that the attribute that we use? The annotation?
**Cesar Munoz** 11:12 Probably, it's just that I'm not sure that we had that by the time this was created, you know, it's like…
**Jason Plumb** 11:17 Right, right, but we could go back and add it.
**Cesar Munoz** 11:20 Yeah.
**Jason Plumb** 11:21 As a stopgap measure, so that people know that it's… An incubating… is it incubating or experimental? I forget.
**Hanson Ho** 11:31 It's experimental for us. It's experimental for us, but it's incubating for… for the rest of the hotel. Well, actually, is this in here, or is this in college only? The experimental?
**Jamie Lynch** 11:43 annotation in, in the Android, repo is called Incubating. I could be wrong about that, just go check.
**Jason Plumb** 11:53 Oops.
**Hanson Ho** 11:54 Those seem like constants that no one should… we should not need to refer to across projects unless the instrumentation is across projects.
**Jason Plumb** 12:03 It's true, like, a bunch of these should just be localized to the instrumentation that they're used by, but… Yeah, let's… let's look for opportunities to do that. Like, if these can be moved into instrumentations.
Like, a bunch of these are not… I mean, screen name is probably used everywhere.
But as an attribute, is it? Probably, like, one or two places tops.
So I don't know that it needs to be all the way up here, so let's look for opportunities to move Roam constants.
**Hanson Ho** 12:34 I think… I think, what Cesar's saying is, is basically we had a bunch of old stuff that left… left tendrils in common, and we didn't… like, when we pulled stuff out into their own modules, we didn't really complete the job, a lot of it just stayed here. So, it may be, like, this is the last 5% of, like, let's… let's clean up common so that doesn't contain anything that we want to stabilize at all.
So that it'll be obvious that it's one of these things that… Do not need that.
**Jason Plumb** 13:03 Yeah.
**Cesar Munoz** 13:05 Yeah, I think that.
**Hanson Ho** 13:09 I can't imagine there's that much stuff in there, other than utilities.
**Jason Plumb** 13:14 Yeah, I mean, these are abstractions that we use, you know, how to get the system time.
In a non-platform-specific way.
Which is very similar to clock, isn't it?
**Cesar Munoz** 13:27 I think this was mostly to… for tests, to use for tests.
**Jason Plumb** 13:35 Yeah, but if we have that, don't we also have the clock interface?
**Hanson Ho** 13:42 I suspect this is, again, something that existed a long time ago, and probably wouldn't be necessary right now, but some tests or something is still depending on it.
**Jamie Lynch** 13:50 We've got hotel android Clock.
And… Bath looks like it does a similar job.
Totally.
**Jason Plumb** 13:58 Okay, so let's… let's look at combining those.
**Hanson Ho** 14:03 Seems like it wraps system time and override that, and… We have that already.
**Jason Plumb** 14:10 What's it called, Jamie? Android System Clock?
**Jamie Lynch** 14:13 There was Hotel Android Clock, and there's an old space named Clock.
**Jason Plumb** 14:21 And what was the other one?
**Jamie Lynch** 14:23 Oh, so looking at a hotel android clock is just a… our implementation of, OpenTelemetry Java's clock interface.
**Hanson Ho** 14:33 You open the electric clock out.
**Jason Plumb** 14:36 But we should look at what it would take to combine those. The main thing is, what does this provide? It provides… Current time Millies. I think we can get that from the clock.
**Hanson Ho** 14:45 I suspect all this is doing is someone's calling it set for test. Their limitations depend on this system time. It could probably be swapped in to hotel clock.
**Jason Plumb** 14:56 Yeah.
**Cesar Munoz** 14:57 I mean, it can probably even… probably can even be removed. I mean, we don't… that's the thing.
**Hanson Ho** 15:01 Yes.
**Cesar Munoz** 15:02 modules are… just… Leftovers.
**Hanson Ho** 15:06 Yeah, I suspect most of that stuff could be inlined if it's constants, removed if there's something else, and the only truly shared things would probably internal utilities.
**Cesar Munoz** 15:19 Yeah.
**Jason Plumb** 15:20 So to kind of recap what I'm hearing is when it comes to common, which is what we started looking at, we think it's a bunch of leftovers. We're not inclined to stabilize it if we can kind of… let's shrink its footprint, and then revisit stabilizing, right? Like, let's see if we can get rid of a bunch of it, or move it around into places where it's used more.
And then see if it makes sense to stabilize it, because it is a bit of a… just a kitchen sink, it feels like, right now.
**Hanson Ho** 15:45 If we have an issue, we should probably just rename it, or, like, add in the description. Basically, try to get rid of as much as this as possible, or move it to the appropriate modules, and then see where we're left with. I suspect it's just not going to be very much at the end.
**Jason Plumb** 16:12 Okay, I will add a comment in the issue related to that.
Cool, so now there's discussion of services and core.
Let's talk about services first, because that's going to be less exciting, I hope.
Alright, services… We don't have a README for this, do we? Nope.
**Cesar Munoz** 16:45 Yo.
**Jason Plumb** 16:46 I mean.
**Cesar Munoz** 16:46 Services has always been… Ment as an internal set of tools.
Really.
**Jason Plumb** 16:53 Yeah.
**Cesar Munoz** 16:54 The fact that we have it as a standalone module is because we wanted to use these tools across instrumentations, as far as I'm aware.
Our instrumentations.
**Jason Plumb** 17:03 But remember that instrumentations can be written by third parties.
**Cesar Munoz** 17:08 Which…
**Jason Plumb** 17:08 Would you…
**Cesar Munoz** 17:09 Shouldn't use those.
It's fine, I mean, third parties can create their own tools.
**Hanson Ho** 17:17 So are… are things in there, like, things that abstract away the Android lifecycle? Yeah. Or broadcast changes to sessions?
Things that are reasonable for instrumentation to depend on, but… but, I think that's.
**Cesar Munoz** 17:36 I think we can… we can see it as a reusable set of entry points.
For us to avoid, you know, just repeating the same under SDK goals.
All over the place.
It's mostly done to avoid repeating stuff.
Internally.
It also helps with I think for lifecycle stuff, it has, like, a… there are some of them which have state for callbacks and things like that, probably. I don't remember all the details, but it's… I mean, everything that is done here, any user can do just by having an instance of a context, an Android context, so…
**Hanson Ho** 18:22 So the interface is on that, then?
Are public, then, isn't it?
**Jason Plumb** 18:29 Technically, right now, this is public, yeah.
I know, sorry, it's an internal package.
**Hanson Ho** 18:35 Okay.
**Jason Plumb** 18:39 So that should send a message, but it's not enforced, right? So someone could certainly use this internal package.
And… Say YOLO.
**Hanson Ho** 18:48 So, if I'm a… if I'm a… if I'm a Joe Schmoe developer, and, I want to add some instrumentation.
and I don't add anything… I'm not adding it to the OpenTelem2 Android repo. It is not expected that they could use these, regardless of the visibility set on those objects, because this is internal.
Are we saying that, then, this is, by definition, something that's with… only consumable within the instrumentation, that we have, that adhere to the… the instrumentation interface?
Because it would be fair game for… for instrumentation in our repo to use this stuff, right?
**Cesar Munoz** 19:36 Yeah, I'm not sure I'm following, but I guess… So you're saying if a user creates their own instrumentation, they… Shouldn't be able to see these types.
**Hanson Ho** 19:49 No, I…
**Cesar Munoz** 19:49 That's correct.
**Hanson Ho** 19:50 I'm asking our intentions, because we have… we have, like… what we consider the SDK core.
kind of stuff. And then we have, like, instrumentation, which is a little bit removed from that, that we do separate some stuff from very internals to our instrumentation, that we load.
But then third parties can write their own instrumentation that don't adhere to the, you know, our instrumentation, spec.
**Cesar Munoz** 20:20 Love it.
they still have to adhere to the under-instrumentation interface.
It's just that… but these… but these services are not part of that.
That's a separate API.
**Hanson Ho** 20:33 Okay.
Because who can depend?
**Jason Plumb** 20:35 just for the sake of discussion, if there was a user who is building an app, it's an app developer, and they're wiring OpenTelemetry Android, and they've been using it for months, and they're happy with it, they're like, oh, I want to start doing something with the cache, and they come across the cache service, right? The cache storage.
They could consider using that interface right now, even though it's in internal.
So that sends one message, like, yeah, probably don't want to use this, it is internal to us. But we do publish these as a services jar that they could take a dependency on, they could technically start using these classes, right?
**Cesar Munoz** 21:13 I guess, yeah, but they shouldn't because they're internal.
**Jason Plumb** 21:16 But do we think that this is a strong enough message?
**Cesar Munoz** 21:21 It's the same message sent upstream, so…
**Jason Plumb** 21:24 It's true.
**Hanson Ho** 21:30 So, if that's the case, then we should at least have a README, or something like that.
**Jason Plumb** 21:35 Yeah.
**Hanson Ho** 21:36 That telegraphs, the meaning of internal to be, hey, this is strictly not supported, or usage is not supported, and it's not versioned, and therefore.
We don't have to stabilize it.
I'm putting a question mark.
**Cesar Munoz** 21:53 Yeah, that's fine, yeah.
**Hanson Ho** 21:54 into that, whether… whether we want to do that is…
**Jamie Lynch** 21:59 Nope.
**Cesar Munoz** 21:59 I think that's fine.
**Jamie Lynch** 22:01 Just to… just swing up another point about the services module.
I think Core depends on it, and then the instrumentation API itself depends on it.
So…
**Jason Plumb** 22:16 The instrumentation API does.
**Jamie Lynch** 22:20 I believe so, yeah.
So… Effectively, all our instrumentations have access to services, so…
**Jason Plumb** 22:29 Through… what again?
**Jamie Lynch** 22:31 I… Couldn't follow the chain, but I can.
**Jason Plumb** 22:34 Yeah.
**Jamie Lynch** 22:35 see the symbol in my IDE when I, try and use one of those symbols.
So, yeah, I think… To me, it feels like this would be a good one to break apart a little bit.
Like, certainly, I don't see a reason why the activity instrumentation needs to know about, like, network services, for instance.
And it also drags in a few transitive dependencies.
**Jason Plumb** 23:04 Look at that, yeah.
But, again, this is… this is… it's okay, though, for our inter… I think what I heard Cesar say earlier is that it's okay for our internal instrumentation to use these internal services as a way to uniformly abstract away the platform details.
**Jamie Lynch** 23:25 Yeah, I think it's fine to use these internally. I would… Suggest there's perhaps a better way of organizing them so that It's more specific to, like.
the instrumentations that need them. So, for instance, Like, the activity… instrumentation, And anything that, like, tracks the screen, we could maybe have, like, a… A module within instrumentation that kind of performs that service, and then activity, fragment, etc. could depend on that.
**Cesar Munoz** 24:04 Got it, you mean to split that module into the actual instrumentations that use it, and then just probably remove it?
Yeah, I think that… I mean, if it's possible, that would be great.
**Hanson Ho** 24:17 It's a bit of a kitchen sink right now, so it's not… we can't discern relationships in terms of, like, what instrumentations depend on what services.
So, by definition, then everything is exported. So, if we move… separate into, you know, different modules, like Jamie says, like, you know, network services and, you know, lifecycle services, then at least the dependency becomes a little bit more, granular.
**Jason Plumb** 24:45 Yeah, I don't have a strong mental model of where that stuff gets used. I think because it's kind of at the top level, it's probably used in… more places than I think it maybe ought to be, or is, but until we get in there, I don't… I don't have a strong sense of it right now.
**Cesar Munoz** 25:04 I can, have a look and add a comment of, you know, the current usages.
of services, and yeah, I know that… I think there were a couple of instrumentations. For example, I think they once… There was one for… there's one for activities and one for fragments, these two.
**Jason Plumb** 25:25 Yeah.
**Cesar Munoz** 25:26 We're actually in services, or, well… that, I think they'd share some services, in which case… if I understand correctly, Jamie, what you mentioned.
For those cases, we could just create a new… Share module, but it's only shared across these two or number of consumers, and that would be it. It wouldn't be, like, a global… module for… yeah.
**Jamie Lynch** 25:59 Yeah, that's correct. Yeah.
**Cesar Munoz** 26:01 God.
Yeah, that sounds good.
**Jason Plumb** 26:06 Well, much like Common, it sounds like right now our goal is not yet to attempt to stabilize services, because we don't want it to get used anyway, and if we stabilize, it might send a different message, right?
**Cesar Munoz** 26:18 Yeah.
**Hanson Ho** 26:25 We've kind of punted on a lot of this… reorganization, refactoring stuff, and now that we're talking about stabilization and APIs, it's… it's pulling that stuff back in, because if our modules aren't… don't have clean separation between API implementation and dependencies.
that's really hard to say what is stable and what that drags in. So, it feels like if we want to do stabilization, we at least have to make another… do another pass on this common stuff. All these kitchen sink modules that we've kind of just dumped stuff into.
And be like, okay, well, what is the surface here? Do we even need it? Like, I'm looking at the surfaces, and it's like.
is it the only reason that they're in there that cord needs them, as well as instrumentation? Because if it's only instrumentation, shouldn't they just be in the instrumentation API, or something, you know, along those lines?
**Jason Plumb** 27:18 I think you're asking good questions, but the quick answer is that these were here to just abstract out some calls that couple.
**Hanson Ho** 27:26 Oh, yes.
**Jason Plumb** 27:27 Yeah.
**Hanson Ho** 27:28 But now it's that second step of.
**Jason Plumb** 27:30 Oh, yeah. Yup.
**Hanson Ho** 27:31 Yeah.
**Cesar Munoz** 27:32 Yeah, I think it's the right time now, because it's… the reason they're there is because up until recently, we didn't even know what the… all of the APIs, or at least the instrumentation ones, will look like, finally.
Yeah. So I'm guessing we're like, but what if we need it when they become stable, or something like that, so… but now it's clear.
**Jason Plumb** 27:55 Alright, before I click on this one, does everybody want to do some stretching, or maybe get limbered up, because… Core…
**Hanson Ho** 28:06 Speaking of kitchen sinks…
**Cesar Munoz** 28:08 I remember once with discussed that probably everything that's in core might get replaced by the, Kotlin SDK, right? In the future.
**Jason Plumb** 28:24 Mmm…
**Cesar Munoz** 28:25 Not every…
**Hanson Ho** 28:27 Not everything. The Kotlin SDK is not really Android-aware, so if there's anything that… in core that's building on top of Android APIs.
**Cesar Munoz** 28:37 Got it.
**Jason Plumb** 28:40 Well, the existence of an internal package sends a suggestion that everything that's not in there is not an internal, which means it's external.
**Hanson Ho** 28:50 There's an instrumentation package in Core as well, so… Is that the instrumentation API?
**Jason Plumb** 28:56 It's the loader, which is an internal thing, right?
Even though it's not labeled as such. But we're the only ones that should implement this.
And the impulse.
Yeah, this could… this could live somewhere else, conceivably.
**Hanson Ho** 29:19 That's beautiful.
**Jason Plumb** 29:19 You know, it's a core piece of functionality. We do need the ability to load instrumentations.
What's in this map?
**Hanson Ho** 29:27 spring.
**Jason Plumb** 29:29 This is, the binding that allows us to read the stuff. So we have this scheduling bit that every so often will read the telemetry back off of disk.
And I believe that's because that… Peace does not exist in the dependency.
If I remember.
So, signal from Disk Exporter, it reads and exports previously cached signals.
**Cesar Munoz** 29:55 Yeah.
**Jason Plumb** 29:56 So it knows where to find… Spans metrics, logs, and then it has a timeout, and so it, you know.
**Cesar Munoz** 30:04 I think we're probably not gonna be able to tell Whether we're gonna stabilize quarter or not.
Right now, because it's… It kind of, to me, follows probably a similar pattern to common and services, in which Now that you're opening up folders here.
I'm starting to remember that there's so much stuff here that probably can either get moved or removed.
for example, I have so many questions, like, we have… a pre-configure way of initializing OTEL.
Which…
**Jason Plumb** 30:46 Yes.
**Cesar Munoz** 30:46 I don't… Honestly, I don't think why we should have that.
Or, we have a configuration object that it kind of overlaps a lot with the DSL from the agent, so this kind of things is like… Probably we just need to clean stuff up first, but it's gonna be… The core is gonna be… That's a tough one.
**Jason Plumb** 31:16 So, I think the history originally was, like, the OpenTelemetry Rum Builder kind of had two jobs. It was, like, the thing that you… because it was all Java back in the day. You used the builder pattern to… poke all of your configuration in there, and when you called build, it did two things. It created the underlying OpenTelemetry SDK instance, and then it also wired up and stitched in all of the surrounding instrumentation and exporter stuff.
And so, it was kind of like this dual-purpose class.
And it fully encapsulated the creation of the OpenTelemetry SDK.
And some users are like, it's too restrictive.
And instead of creating the entire… like, instead of recreating the entire surface area.
of the OpenTelemetry SDK, the upstream SDK, we created this, pre-configured Rum Builder, and that means that your OpenTelemetry SDK is already configured by you. So that kind of splits out… it attempted to split out those responsibilities a little bit, and really, I mean, this is almost, and I haven't looked in here, and I'm kind of scared to, but this is almost just, like.
an SDK builder, and this is like, okay, now that you've built the SDK, let's do all the RUM stuff. That's the… that's kind of where the design evolved to.
So this allowed users that wanted to be able to fine-tune or control every little piece of their SDK to be able to do that by passing in the SDK, that they already have created for themselves.
But this is a pretty… terrible interface, like, you know, I don't know that anybody's using this. Maybe people are.
I think at one point.
**Hanson Ho** 33:05 Fuck.
**Jason Plumb** 33:05 Blunk might have been.
**Hanson Ho** 33:07 I thought people were saying we can't… there are things that the… the actual interface that we exposed couldn't do, so we had to bring in core and do some stuff on here. This is like our get-out, you know, latch to say, you have everything now.
**Jason Plumb** 33:21 But that's also really… yeah, and that's exactly… you're exactly right. But that's kind of before we started beefing up the agent, right? And before the DSL had started to mature, which… I think it's still… I mean, we have the agent marked as stable, so it's, like, it's getting there. It's pretty mature. We're adding capabilities to it as the need arises, so… I feel like… You know, this is still here as, like, a fallback for, like, those hardcore users or distros that may want to manage every aspect, but we don't expect most users to be using that.
**Cesar Munoz** 33:54 The thing is that with the pre-configure builder.
**Jason Plumb** 33:58 Yeah.
**Cesar Munoz** 33:59 it's kind of like we have not two, but we actually have three layers of configurations, and we have the DSL, then we have the ROM builder, and then we have the pre-configured ROM builder.
**Jason Plumb** 34:10 Yeah.
**Cesar Munoz** 34:10 And the last one is used by the ROM builder. It is. Because in the end… in the end, I think what ROM… the pre-configured RAM Builder does, mostly, is just to… install the instrumentations that are in the class path. I think that's really mostly what it does.
But, it's like, if a user uses that, they wouldn't have Really, any of the… I really can't think of why would, like, they wouldn't have this buffering, or you know… explore.
**Jason Plumb** 34:52 They would have to wire it up themselves. They could use disk buffering, but they would need to do a lot of the work that's in the agent.
**Cesar Munoz** 35:00 Yeah, but it's like, at that point, it's like, you might.
**Jason Plumb** 35:03 I know.
**Cesar Munoz** 35:03 use Upstream SDK.
**Jason Plumb** 35:05 But yeah.
It's true.
I think you're calling out a good point, though. This, really, the purpose of this class is kind of just to load the instrumentations, right? So when you call build, that's what it does. It also does the crash flush handler.
And that's really it. I don't know that there's a lot else going on in here.
But this is the thing that returns the instance of OpenTelemetry ROM.
Right, this is ultimately what creates it.
**Hanson Ho** 35:38 Can we deprecate things in a minor version?
**Cesar Munoz** 35:44 Yeah, I think we've.
**Jason Plumb** 35:44 Yeah, as long as they're not stabilized, we have to be careful if they're stable.
**Hanson Ho** 35:49 Can we deprecate?
these interfaces?
As a signal that we might want to remove them.
And see if anybody… you know.
**Cesar Munoz** 35:59 Complaints, yeah.
**Hanson Ho** 36:00 or say, hey, I need this because of XYZ. And then, if we don't have that in the DSL, we build it in.
Because it does seem that…
**Jason Plumb** 36:10 Do you want to deprecate both of them?
**Hanson Ho** 36:14 I want to deprecate anything that we think are redundant and not necessary.
Oh, that's redundant. I want to deprecate anything that we don't intend to stabilize.
**Cesar Munoz** 36:28 That makes sense.
**Jason Plumb** 36:29 I'm hesitant… to do that, because I don't think we have… a clear direction, and anybody who is using that today that sees a deprecation should at least be able to read some sort of, like, migration guide, or upgrade path, or like… like, if you see… if you upgraded to the new version, the new minor version, and you see that a class that you're using is deprecated, you should at least be able to… Read to something that tells you how to go forward, instead of having to figure it out yourself. And I don't think that we have that guidance yet.
**Hanson Ho** 36:58 Well, I think the intention is… is… is we're saying we're gonna go into the DSL, we're not gonna expose 100% of the functionality, so, you know, say what you want.
We'll put it there.
Or, we have to have this similar latch that says, here's everything.
In which case, we have some sort of this.
So, either we get rid of this completely and say DSL's the way to go, or we have to stabilize something that is… The kitchen sink. Everything. So, we should pick one.
**Jason Plumb** 37:37 I'm okay with that.
**Cesar Munoz** 37:38 Procreating this one.
The only use case that I see that we won't be able to address with the DSL.
And the reason why I think the other one probably should stay… maybe. I guess it depends.
It's for users who… don't want to use Kotlin, but I think that's… You know, probably not that many.
But still, that's the one thing that I see.
The other one useful for.
**Jason Plumb** 38:17 So, I don't love this. This is a… kind of a large surface area.
But I do like that we have a way to create an instance of OpenTelemetry ROM with your own SDK that you've already preconfigured, because I think… the number of knobs that you can turn to create an SDK is much larger than we want to have in our agent APIs, in our DSL.
**Jamie Lynch** 38:44 Can folks even use that constructor if it's marked as internal?
how… how would people use this? Would they scan a… object return from some function somewhere, and I may add instrumentations.
**Jason Plumb** 39:02 That is… no, it's a good point.
**Cesar Munoz** 39:04 I've been this.
**Hanson Ho** 39:05 terrific.
**Cesar Munoz** 39:05 Sorry, factory.
**Hanson Ho** 39:06 Yeah, there must be a factory method, right?
**Cesar Munoz** 39:09 But the… I think in… I mean, Jason, when you say that you like that users can create their own ROM instance.
just by having their OpenTelemetry SDK.
**Jason Plumb** 39:22 Yeah…
**Cesar Munoz** 39:23 I think that's also possible by creating your own implementation of OpenTelemetry ROM.
Right.
Because in the end, it's an interface, so…
**Jason Plumb** 39:42 You mean their own implementation?
**Cesar Munoz** 39:44 Yeah.
**Jason Plumb** 39:46 Oh.
Yeah.
It's true, I hadn't… Oh, it's interesting, I hadn't anticipated people providing their own implementation of… this interface.
**Hanson Ho** 40:02 Oof.
**Cesar Munoz** 40:05 I mean, if you really want to have control of every single little detail, it's like… No.
**Jason Plumb** 40:15 It's true. To answer Jamie's question then, though, I think… I don't know that you can use this anymore, like, maybe we did intentionally cut this off.
I don't remember this being internal, is what I'm saying.
But we had to have made that decision at some point in the past.
Which is why I was looking at Blaine, I'm like, when… when did this actually change in this PR? It was probably like this for a while.
He's got me curious now.
It was internal already, huh?
So, more than a year, it's been internal.
**Cesar Munoz** 40:59 I think there's a factory, let me check.
**Jason Plumb** 41:05 Where would that factor even be?
**Cesar Munoz** 41:09 I think it was in the… in the interface, the sedimentary ROM.
**Hanson Ho** 41:15 It's probably a static method. They're all static methods here.
**Jason Plumb** 41:18 On the RUM… on the… where? On OpenTelemetry Rum?
**Cesar Munoz** 41:25 Yeah.
But I guess that was before it was moved into its own… Module, rolling.
**Jason Plumb** 41:31 Well, let's look for usages of the pre-configured thinger.
Right, like, where's this?
Let me select you.
No, I don't think there's a way to… I don't think there's a way to make one.
Which, that's in our favor, right? That gives us much more leeway. Then we… then the only thing we have to deal with is the other builder.
This one, right?
Which is also internal. So basically, we've sent the message that no one should be… no one can create instances of these, but this one has a create. Okay.
So that's Alma.
**Cesar Munoz** 42:32 There's a, there's a type named, ROMBuilder. It's in.
**Jason Plumb** 42:39 really…
**Cesar Munoz** 42:39 Whereas?
It's in Core, from Builder. I think that's where they are.
Yeah, the factories are…
**Jason Plumb** 42:54 But not the pre-configure, you still can't pass an SDK in.
I know it's lost.
Okay.
**Hanson Ho** 43:02 It's, it's an internal thing now, of, of, OpenSelm to Run Builder.
**Jason Plumb** 43:11 It's interesting, like, I haven't… we haven't heard… I don't think we've heard any pushback on that, have we?
**Cesar Munoz** 43:18 No.
Not that I'm aware of.
**Jason Plumb** 43:23 I feel like this would have been here for a while.
So it sounds like right now there is no way to bring your own SDK. So that idea… Has probably been gone for some time.
**Hanson Ho** 43:41 I remember we had a discussion where somebody was trying to add, some modifier to something, and then they couldn't do it because this has been taken out of, you know, something that they could do.
This was a while ago.
**Cesar Munoz** 44:03 But what's it regarding the, pre-configure builder, or just a regular builder?
**Hanson Ho** 44:09 Well, it would be that the only way for them to do it would be to pass in their own instance of the OpenTelemetry SDK, and I don't think that was possible at that, when we talked about that.
I could be misremembering, but I remember… Cuz… For a while there, we had this hatch that says, hey, do whatever you want, but then we closed it.
And somebody came and said, hey, I want to do this, and we built it into… something.
**Jason Plumb** 44:36 Let me know if you can find that, or that issue, or where that was from, because I… I'm not remembering that.
**Hanson Ho** 44:47 Yeah, I'll take a look at the… at the dock.
I remember we talked about it.
**Jason Plumb** 44:54 Yeah, there's no create method on this, right?
Just to double check.
**Hanson Ho** 45:01 The only place… the only place in production that calls it is… is in, OpenTelemetry Run Builder.
**Jason Plumb** 45:06 Yep.
**Hanson Ho** 45:09 So we kind of use it as, like, an internal object, I think.
**Jason Plumb** 45:12 That's right.
Yeah, that's an interesting separation now, that this is purely an internal constructor, it's only ever used internally Yeah, interesting. I think that opens up some possibilities.
I think core… I mean, my opinion for a while has been that core is probably one of the last things we want to stabilize.
I think it's good for us to be talking about it and thinking about it.
**Cesar Munoz** 45:47 Yeah, but I think it does make sense that it is… Probably actually the last thing.
We should stabilize.
**Jason Plumb** 45:58 We have… A release coming up soon, I believe.
Like, next week, or this week?
**Cesar Munoz** 46:11 I'll extract the.
**DavidGrath** 46:13 I think it's to Dana.
**Jason Plumb** 46:18 Today, Mmm.
**DavidGrath** 46:20 Yeah, I checked your website.
**Jason Plumb** 46:22 Okay, that's a stupid one, this thing.
Oh, man.
**Hanson Ho** 46:30 What is this?
**Jason Plumb** 46:32 Oh, this is something I hacked, I'll put it in the thing. I just hacked this together because I'm always asking, like, when this question is, and like, you know, here's our favorite. And the, like, our… our field team is always asking this question, like, I always have to go, like, trace down the dependency hierarchy, and this tries to do that for you, so I'll link to it.
It's just hosted on GitHub pages.
So… Yeah, according to this, we should be releasing today, because the rule used is, we said, the Tuesday after the third Monday.
However, it depends on the upstream, and the upstream, I think, has not happened yet.
Oh, it just happened 12 hours ago.
So, we're due for a release.
I haven't thought about what's in this, but I think we have at least one module that got stable in this release.
**Cesar Munoz** 47:27 Also, we have the, URL… override for the DSL config.
**Jason Plumb** 47:33 Yeah,
**Cesar Munoz** 47:36 So yeah.
**Jason Plumb** 47:39 Okay. Well, I'm gonna be running… the Kotlin release as well, so I will… I will just do both. I can just do them in parallel.
If that's cool with you, Cesaro, or Jamie, unless you… unless you really wanted to do it.
**Cesar Munoz** 47:57 I'm fine with that. If you need help, because, I mean.
it's more work for you, so… that's fine, I can take a look at the Android one.
**Jason Plumb** 48:07 Okay, do you want to run it this time?
**Cesar Munoz** 48:09 Yeah, I'll take a look at it.
Well, I'll just start the process today.
**Jason Plumb** 48:16 I appreciate that, I know it's getting late there, so thanks for…
**Cesar Munoz** 48:20 That's fine, no worries.
**Jason Plumb** 48:23 And I don't think there's anything that we need to go in there this time that's open.
As much as I want this to go in, we can't yet.
**Hanson Ho** 48:36 Nope.
**Jason Plumb** 48:38 Okay.
I clicked on something earlier, we're off-topic, but I clicked on, what was it, this… this one. I think we can close this, right? I think we have strict mode documentation?
**Cesar Munoz** 48:54 I think we do, we do, right? We created a…
**Jason Plumb** 48:56 Yeah, I think we can…
**Cesar Munoz** 48:57 down.
**Jason Plumb** 48:58 I think it's in Doc.
Yeah.
**Hanson Ho** 49:04 Somebody added it a while ago.
**Jason Plumb** 49:06 Okay.
Cool, yeah, I mean, there's a lot of… there's a lot of triaging across these issues that probably needs to happen, and should be, like, an improved, sustaining effort that all of us contribute to, but I just happened to see that one, I was like, I know that we have that doc!
So we don't have to do that here, but, without any other agenda items, we can… Either do some of that, or we can end it.
Or we can go back to something that we might have skipped over.
**Hanson Ho** 49:43 Well, Jamie being out for 6 weeks, we didn't talk about, but…
**Jason Plumb** 49:48 Yeah, Jamie is gonna be out for 6 weeks.
**Jamie Lynch** 49:53 Yep, so… I'll see you all in July.
**Jason Plumb** 49:56 You got names picked out? You don't have to tell us what they are, but do you have names picked out?
**Jamie Lynch** 50:01 We got a name, but we're gonna wait till it comes out, but I'm not sure.
**Jason Plumb** 50:05 Yeah, of course, cool, cool, cool.
It's exciting.
**Jamie Lynch** 50:08 Naming is always the hardest thing, just like in…
**Hanson Ho** 50:13 It's… it's better than off by 1.
**Jason Plumb** 50:14 You came in.
**Hanson Ho** 50:16 Oh, there's two!
That's… that's much harder.
**Jason Plumb** 50:20 That's a very good point, Hanson. Yeah, you don't want that off-by-one error.
Okay, cool, well, we're nearly at time, I guess we could end it.
Going once.
Going twice.
Cool. Well, I think that was productive. I think we got some good stuff. I will take my action items. Cesar, thank you for running the release.
And… Yep.
**Hanson Ho** 50:49 The FY… the SDK pre-configure run builder, I can change it to internal, and it still builds fine. So no one possibly is using it outside.
**Jason Plumb** 50:59 You changed the class to internal?
**Hanson Ho** 51:01 Yeah.
**Jason Plumb** 51:02 Yeah.
Yeah, okay. Cool.
**Cesar Munoz** 51:08 Well, thanks.
**Jason Plumb** 51:09 Sophia.
**Cesar Munoz** 51:09 Better.
**Hanson Ho** 51:10 Yep.
