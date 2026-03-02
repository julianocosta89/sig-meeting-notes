SIG: Android SIG
Date: 2026-01-13
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:48 Good morning.
Knowing full well it's not morning for many people.
**Jamie Lynch** 00:57 Right.
**Jason Plumb** 00:58 Damn.
**João Oliveira** 00:59 Hey, folks.
**Jason Plumb** 01:01 I've been awake for several minutes.
Cesar!
**Cesar Munoz** 01:30 Hello!
**Jason Plumb** 01:31 Hey, welcome back, happy new year!
**Cesar Munoz** 01:34 Thank you. Happy New Year.
**Jason Plumb** 01:37 Good to see you, good to see you.
**Cesar Munoz** 01:42 To see you too, glad to be back.
**Jason Plumb** 01:47 Someone's got some notifications, is that you?
I got a couple of those, yeah.
**Cesar Munoz** 01:54 And emails, and… yeah.
**Jason Plumb** 01:56 I was just hearing some beeping.
Okay, let's go ahead and get started, since we're already at 2 after.
I front-loaded a few things in the release… in the notes here. The first one I wanted to talk about is the release.
With help from Hanson and others, we managed to get the…
1.0 release out, and for some reason, middle click on this mouse is no longer working, and I'm bummed.
Yeah, so… You know, it was a…
Not uncomplicated, this release process.
You know, we were at 0.0.whatever.rc.1? Yeah, so we went from 1.0RC1 to a regular 1.0.
I will say that the build automation has a lot of expectations around the format of this string.
And to get it to properly account for
that string format, and to do that in a branch in a way that made sense was not really doable, so I just did it, like, manually with pull requests. Like, I basically mimicked what the automation would be doing if it knew how to handle these, which meant
Updating a bunch of files, like, just with versions in them, and, updating the changelog, which is usually more automated, and then…
PRing that, and then having Hansen approve it, and then merging it, and then watching it fail, and then repeating with small changes. And really, I think it… I think this did work the first time to get 1.0 out, and then I realized, oh, I forgot to drop alpha.
from the agent. So we… we, we have a 10 alpha agent without RC, and then I immediately turned around and did 101 without alpha. So, the agent is currently at 101 non-alpha.
Everything else is at 101 alpha.
**Cesar Munoz** 04:01 Sounds good.
**Jason Plumb** 04:02 Yeah.
**Cesar Munoz** 04:03 What I didn't understand… Is that, well.
The… the stuff that you did, that you had to do manually.
Was it only needed because of the transition between, you know, from the RC
number to the… okay, so it's… it's something that…
I guess my question is something that we…
Might not need to change the automation stuff.
to… You know, for future… versions, or…
**Jason Plumb** 04:38 Yeah, so I put an item in here to sort of talk about that. I don't know the answer, that's up for us to decide. I will tell you right now that it will not… like, the build automation right now does not support RC whatever.
If you want to go from 2.0.0RC1 to 2.0, or even to RC2, I don't think it will work in its current state.
**Cesar Munoz** 05:02 Got it.
**Hanson Ho** 05:03 And I think
Yeah. I think there's some, we can't release a patch release with the current automation either. I think, there needs to be additional work to support patch releases, so I think there's probably going to be a bit of work that we want to do, even just to support the patch release case and not have to do this, yet again.
**Jason Plumb** 05:24 Yeah, the unfortunate thing is that it's hard to test. Like, it's in GitHub Actions mostly, and then testing that is hard without actually doing the release. So, I mean…
**Cesar Munoz** 05:35 Oh, we're gonna be testing…
**Jason Plumb** 05:37 On every new release. I know.
Yeah, well, like, RC1 to RC2 is probably, you know, if we burned a few versions while testing, that would probably not be the end of the world, but
We wouldn't… we wouldn't want to necessarily publish, like, a 2.0 as a test
test version, but anyway, we got some work to do there. I would love some help. I think we probably do support patches. Go ahead.
**Cesar Munoz** 06:04 No, I was just gonna say, if nobody else wants it, I would like to have a look at this automation
Changes.
It's always a fun, challenge.
**Jason Plumb** 06:18 Oh yeah, yeah, for sure. I kind of have fun with it, too.
**Cesar Munoz** 06:22 Yeah.
**Jason Plumb** 06:24 We have someone on the call that I don't think we've met before, and I want to make sure that we welcome them, and that we're inviting for new people who join us, so… so welcome. I don't want to attempt to pronounce your name until I hear you do it first.
**João Oliveira** 06:36 All right, yeah, that's perfectly normal. It's Joanne.
**Jason Plumb** 06:41 Drone.
Okay, I thought.
**João Oliveira** 06:43 safe.
**Jason Plumb** 06:43 I apologize for messing that up in the future.
**João Oliveira** 06:46 No, that's… it's totally fine, no worries, it's a hard thing to…
**Jason Plumb** 06:50 To get…
**João Oliveira** 06:51 Exactly right.
**Jason Plumb** 06:52 Well, welcome. We have this document that I pasted in the meeting chat, which is also linked to from the community page, and if you want to add your name there, and who you're with, and any agenda items, feel free to stick them down at the bottom. I think that we will probably have time. We usually…
We usually have time to go through stuff that's not on the agenda, even though I front-loaded a bunch of stuff today. So, the link is in the Zoom chat if you don't have it. But yeah.
**João Oliveira** 07:17 Amazing.
**Jason Plumb** 07:18 Thanks, thanks for…
**Cesar Munoz** 07:19 Yeah, welcome. You are… Johan. You are…
**João Oliveira** 07:24 dwell.
**Cesar Munoz** 07:25 Thank you all.
**João Oliveira** 07:27 Welcome. Yeah. Thanks. And, and…
**Cesar Munoz** 07:30 Also, I would like to just quickly,
Thank, you know, everybody on the… recent work, I, I…
I've gone through a lot of issues. I probably haven't read everything in detail, but I noticed that
There were some, there was a lot of work, and so… just…
Yeah, that was it, just thank you for, you know, That worked.
And it's great that… We got to the first table release, and, and…
It seems to be doing good, so… Yeah.
Good stuff.
**Jason Plumb** 08:10 Yeah, and one thing I wanted to call out here, I second all of that. I wanted to call it that we are now on the hook to not break the agent initializer API. I know we've been running a little quick and loose on those API files, and like, at least when I review.
I usually don't pay that much credence, but at least on the agent now, we need to pay extra attention to those when reviewing.
So that we don't introduce a breaking change on the agent.
The other APIs we are allowed to.
Our preference is not to. We definitely want to be very careful about any breaking changes anywhere that we make at this point, but the agent is, like, kind of a…
Affirm… Affirm don't break me, or we have to rev to 2-0.
**Hanson Ho** 08:52 So, and…
**Jason Plumb** 08:54 Go ahead.
**Hanson Ho** 08:55 Sorry, by breaking, it just means,
making things that used to work not work, or adding API is okay. So changing that API file is totally fine if you're adding things on top of, and not redefining the semantic meaning of things, and making sure.
what used to work still works, so, and that's not to say it's impossible, because there is 2.0, and there is a Kotlin API that, we'll want to implement eventually, which will require 2.0, but…
It just means that anything breaking.
we will have to do 2.0, which we may need to, you know, do it manually if the RC stuff is still, an issue.
**Jason Plumb** 09:43 Yep, which is not the end of the world.
**Cesar Munoz** 09:47 Oh, by the way, congrats on the, OTL cotling… intra- approval.
I noticed it recently.
**Jason Plumb** 10:01 Oh, we lost your audio scissor.
**Cesar Munoz** 10:03 Can you hear me?
**Jason Plumb** 10:04 Yep, now we can.
**Cesar Munoz** 10:06 Yeah. No.
I was just gonna say, I don't know for how long it has been there, but it's… I just noticed.
Yesterday, and just want to say congrats.
I think it's a great step towards, you know, a better support for Android, too.
**Jason Plumb** 10:23 It's been there for days, Cesar. Several days now.
**Cesar Munoz** 10:26 I'll go ahead.
Haven't missed much then.
**Jason Plumb** 10:31 Yeah, so that's awesome, right? So we know this is bootstrapped.
Always looking for contributors, and yeah, it's, it's, it's, it's considerable, like, this is, this is awesome, like, it's off to a great start.
We'll have to at some point talk about the roadmap for adopting that in Android, but not today. Probably not next week or this month, but, you know, eventually we'll get there. That's the… on the roadmap, right?
Okay, I think that gets through all of this stuff.
Yep, bootstrapped. Okay, so…
you know, we're talking stability a little bit. We can start now, I think, identifying other components that we want to become stable, so…
The way that we do that with automation right now is simply by putting this hotel stable equals… False?
What?
Oh. Oh. Okay, I need to change that. Someone needs to PR that. It could be me.
I'm glad we… I'm glad we're doing this exercise, because that would break a build, in the future, and we would publish an alpha again,
I must have only changed it in the branch.
Yeah, I bet you this is true.
Yeah, okay, so the release branch for 1.0 has that, but we need to… do we need to make that equivalent change on main branch.
So that future… release branches have that as true. The question is, what other components in our repo
Can we start thinking about making true?
you know, core is a big commitment. That API surface is still quite large.
You know, on the OpenTelemetry Rum Builder.
If it's stable, people will use it, and they will have the expectation that it doesn't change. So that's one thing to think about.
The instrumentation API is maybe not that bad.
Right, this is… I think this is a pretty small footprint.
So that's one thing to think about.
Although we have had a little bit of thrash on this class.
And I don't think we have to decide anything today, but I think, collectively, I would love for us to be thinking about what might come next, right? Because the agent, although we see that as, like, the main interface to a bunch of what we're doing in OpenTelemetry Android, there are definitely users who are only interested in using Core.
And… I think there will be probably… there's likely to be users that are only interested in using instrumentation.
So that's one thing to think about. I don't think we can reasonably do session until we get more done on the semantic conventions.
But yeah, any thoughts on what might come next?
**Jamie Lynch** 13:41 Yeah, I'd agree that the instrumentation API and Core were probably good targets for what to do next.
Yeah, I guess it'd also be good to discuss
how much we want to put on OpenTelemetry Rum Builder versus OpenTelemetry Rum Initializer, and…
How those two kind of interact with each other.
**Jason Plumb** 14:06 Yeah, I mean, that's a good segue to the next topic as well.
**Cesar Munoz** 14:11 Regarding… regarding… I agree with the instrumentation, but I have my doubts about core.
Well, I'm not sure if it has changed.
a lot since I last… Took a look at it, but…
My idea of it was that it was gonna be, like, our, playground, if you will.
Of adding new stuff, and, and, and, and…
See if it helps the agent.
And… while at the same time, Probably unblocking some… Strange use cases.
For… for people who… Are not satisfied with the initializer.
So…
If, like, if we go… if we say we're gonna stabilize it, then that would mean that we won't be able to break anything.
Then, then, you know… It's probably gonna make things a bit… More difficult to… to…
Less flexible, at least, so…
Now, again, I haven't checked it out. I know that there were some APIs moved out of probably core.
So maybe that's the, the stuff that we… Can, you know, play with.
And I have to have another look, but on the fridge.
But at first glance, it looks like core…
Might be actually the last thing we stabilize.
**Jason Plumb** 15:43 Okay, even after some instrumentations, like, there's probably some instrumentation that's gonna be hard to stabilize.
Because ideally, we would have matching stable semantic conventions. Like, usually with instrumentation, part of the stabilization of an individual module, like, I'm just picking on fragment.
Would be to have the semantic conventions for that telemetry also be stable.
And they're definitely not.
**Hanson Ho** 16:09 And we'll probably need the API to be stable as well, the instrumentation API.
**Jason Plumb** 16:14 Probably before the instrumentation, yeah, yeah.
That's a good call-out.
**Hanson Ho** 16:20 I feel like instrumentation API is probably the… the easiest next thing, and maybe most impactful. I think… I think core would…
be most impactful, but, you know, I think it says are brought up, it's… it's probably the most, twisty-bendy. Whereas if we have a stable instrumentation API, folks can then build on top of that their own custom instrumentation to do whatever they want. And… and perhaps
this first step is about, having a 1.0 that provides the basics.
That say, hey, we're not going to get rid of, you know, providing the application, or, you know, something that, that, you know, we know instrumentation needs that OTEL APIs don't, don't offer, or we need to shim, or whatever. So that is probably a good candidate if we want to march towards this as…
I mean, frankly, just looking at what we have right now, is anything in there objectionable in terms of, hey, do we want to support this perpetually?
And then pay, you know, peeling things back, and if, if…
some… like, I would imagine there may be some APIs that's only required for one or two instrumentation packages, and if that's the case, then we don't feel like it's worthy of inclusion in this API. We pull it out and implement it within those packages. Finding…
oh yeah, this is core. I was like, this is an instrumental.
**Jason Plumb** 17:42 Sure.
**Hanson Ho** 17:43 I feel like finding, finding a, a… a… a…
no pun intended, core subset of instrumentation API, would be the good next step for stabilization.
**Jason Plumb** 18:00 Yeah, this is large. Yeah, okay. So, yeah, getting this, stable… Quite a town.
**Hanson Ho** 18:06 It's also got a lot of Java-y kind of grossness. It does. I look at the… there's a constructor, I think there's, like, 8 overloads or something like that. I'm like, oh, no, that's not a good API.
Bro.
**Cesar Munoz** 18:18 Probably a lot, now that I think about it, probably a lot of core my… be replaced by…
the… the, authoring SDK, right? In a way. So, maybe…
**Hanson Ho** 18:34 Potentially.
it's not Kotlin SDK, at least, like, Kotlin kind of syntax and semantics, if we want to go that direction. I haven't audited this in, you know, and I think everything got dumped in there. I think this is, like, the remainder, so this is going to naturally be messy, and probably require.
**Cesar Munoz** 18:54 Yeah.
**Hanson Ho** 18:54 further, tweaking, so…
**Jason Plumb** 19:00 Yeah, every.
**Cesar Munoz** 19:01 Yeah, I agree.
**Jason Plumb** 19:01 Every little bit helps, for sure. If there's areas in here that we can shrink down because they're already covered by stuff in the agent, or if there's, like, stuff that we think ought to be in the agent, then, yeah, I think every little bit…
Will be beneficial.
**Hanson Ho** 19:16 Or… or if it gets… because I think there's a lot of these things that are, like…
syntactic sugar to help customize. I think that is a forever path, because somebody will want something. At the end of the day, they'll need to basically get access to the OpenTelemetry instance and configure on that, and if we're able to bust that out and basically say, hey, you know.
if you want to plug your own configuration in for OpenTelemetry, then…
do it here. We don't have…
you know, sugar for that. I think we may end up…
doing that, and if we do that, we may be able to, like, remove a bunch of stuff that is basically just a bridge to that. And that may… that may kind of check out a lot of stuff that we don't want to actually have support.
**Cesar Munoz** 20:09 Yeah, just one example that… just a quick example that comes to my mind regarding the utility of core versus the agent is that
Which is related to a couple of PRs that I haven't looked in detail, but…
Based on the titles, kind of get an idea.
Let's say that we're gonna…
Provide a, specialized, clock implementation.
for Android devices, and we want to use whatever. I mean, you could do it many ways.
But there's one that we think it's the best for most cases.
So, I will say, in that case, core… We'll just have a setter.
For, clock implementation.
And the agent won't have any way to set it.
But instead, we'll have our implementation that we decide is the best for most people, so that people using the agent won't have to care about
Setting a clock, so…
That's why I think core is kind of, like, nice to have it kind of there in the background.
Able to get anything and said anything.
**Jason Plumb** 21:28 Yeah, and when.
**Cesar Munoz** 21:28 And it's gonna be messy.
**Jason Plumb** 21:29 when it's not stable, we're allowed to more easily make changes to it, and maybe try some stuff that's… that we may not be making a solid commitment to. I… I agree. The way that that's done in…
upstream Java Core is through the use of,
Experimental or incubating features, which they peel off into special packages called incubating, so that anybody who's using those kind of knows very clearly that it's incubating.
There might be a similar strategy that we can use with extensions or something in Core.
And maybe we start with everything being incubating, or with, you know, a few exceptions, then we just… it's just… it ends up being a lot of, like,
Kind of thrash and moving stuff around to go through that incubating stage.
And…
some stuff kind of stalls out when it hits incubating, and it… I don't know. I don't love that approach, but it is some… we have some options to play with if we wanted to make core stable.
But I think discussing clock is a nice segue to the next topic.
Which I had front-loaded on here about this one. So Jamie put in a bunch of work to do…
The ability to override clock, which was addressing this thing…
So, you probably saw this one.
There's a couple of things here about the nanotime being paused when the device goes to sleep.
So you can get…
inaccurate time measurements on certain telemetry, I think, is the basic idea. And they're like, you know, the advice is to use a different clock, right? It's to use… well, they're saying nano… elapsed real-time nanos. There was some back and forth on whether that's the right approach.
If you haven't seen this thread, go ahead and read it. But Jamie added an API. Why don't I just let you talk about it, Jamie?
**Jamie Lynch** 23:29 Yeah, sure. So, basically, I just…
adds an API that allows you to set a custom clock using, I think, the OpenTelemetry API.
Rather than kind of relying on the clock.get default static, so it allows you to thread through your own instance if you…
want to override the default behavior, but I think, more importantly, it's…
I think it's going to be quite useful for testing, as it allows you to set Unknown value.
And to, like, move the clock forwards and backwards and see… How the system behaves.
So yeah, there was another PR that actually changes the implementation. This just keeps it as the…
Default implementation for now.
**Jason Plumb** 24:24 Yep, and there's no other implementations of clock that come with this PR.
**Jamie Lynch** 24:28 Yeah.
**Jason Plumb** 24:29 Here's a follow-up PR.
Yeah.
**Hanson Ho** 24:31 So this is, I think, a good case study, because, Clock is an OpenTelemetry, you know, core concept.
If we're just threading things through.
And basically maintaining an API in that.
do we want… I mean, we could do it at the… at the agent level, so it becomes, like, you know, part of our, kind of, overall easy initialization API. But if there are other things that are a little bit more obscure, that we may not want to put up there,
how do we do so that we don't have to, like, modify the core API as well? Because we're essentially saying, hey, the OpenSelem3 instance, you need to configure that. If we bust that out, then we don't have to worry about it in core. We can still provide an easy access in… for certain things in the agent layer.
So,
for clock, we can talk about whether we want to do that or not, but I think, in general, it's… this is kind of like the flow chart that we should go through. It's like, hey, what… why do we have to modify core? Well, we have to modify core.
This one, I think we should… we should do at the agent level, but, you know, let's…
**Jason Plumb** 25:47 Yeah, I think… I agree that this is a good case study. My initial reaction was that by… if Agent… if we expect Agent to be our main interface that most users are using to bootstrap Android.
Having a method on there for clock might give the wrong impression, or it may give the impression to the user that they need to specify a clock, when the default should, we hope, the default, which right now, let's say the default doesn't work because of that issue by using nanotime.
Once we fix that, once we come up with our own
clock implementation that addresses that issue, which Jamie's already done, then there should be almost no need for users to ever specify their own clock, is my expectation. And that by having that API up there, it kind of suggests that users need to specify their own.
I'm kind of backing down from that stance. I think… I think the existence of an API doesn't necessarily encourage users
Or it doesn't suggest to users that they need to use it, it's something that they can use.
So I'm gonna back down from that stance. I think…
I don't… I don't believe myself around that part. Where is it? Suggest to users. Yeah, I don't think it actually does.
**Jamie Lynch** 27:03 Right.
**Jason Plumb** 27:04 Or at least not strongly. Go ahead.
**Jamie Lynch** 27:06 Yeah, I think definitely the way the API is written is just in the DSL, so you'd need to go and.
**Jason Plumb** 27:13 like…
**Jamie Lynch** 27:14 Opt into creating a new clock.
Yeah, we could, like, add some documentation saying it's not expected that users are actually gonna set this for the majority of use cases, or,
Yeah, I'm also pretty open to just putting it on an internal interface somewhere, rather than publicly exposing it.
**Hanson Ho** 27:38 as long as it's easy to override it for tests. So…
**Jamie Lynch** 27:41 Yeah, unless, yeah.
**Jason Plumb** 27:43 Yeah, yeah, yeah, that's… I mean, and that, to Jamie's point, that's a very good call-out, is that if we have tests that do measurements or, like, include telemetry, being able to control the clock is, like, crucial for that. If we ever want to do, like, full assertions, otherwise then you're asserting on everything that's not time.
Which is annoying.
**Hanson Ho** 28:02 I think.
**Cesar Munoz** 28:02 you think.
**Hanson Ho** 28:03 it's being… Oh, go ahead.
**Cesar Munoz** 28:06 Well, I'm… Well, a couple of things.
It seems like having, core… I'm just gonna,
refer to what I mentioned about, you know, adding a setter to core, and then not having
Any possibility to configure something on the agent so that we control everything?
That happens on the agent.
I think that's an approach, but probably for core, I think it's fine, because as Hanson mentioned, it's…
It's part of the… core of Autel Java.
So… so… It's probably fine to have a setter in the edging itself.
I'm guessing that, just back at, mentioning the example of having stuff in core that we might want to test out, or we don't want people using the agent API to use it.
Might be for some stuff that we're not quite sure about,
But I think, yeah, clock, it's quite a…
straightforward API that it's, you know, all over the place, so…
Now, there's one… there's… well, all over the place, respawly doesn't mean what I think it means.
In any way, in any case, it's everywhere.
So…
what's the term that people use when they want to sell stuff? Ubiquitos. Yeah. So, something like that. Yeah, fancy stuff.
**Jason Plumb** 29:42 Well, yeah, so to that point, I was surprised at the number of classes that changed in this PR. I was… this is, like, it was, honestly, more than I expected. I was like, oh, this goes everywhere. And that's because lots of things have…
I think…
**Cesar Munoz** 29:55 default, yeah, they just, like, they just get default.
Now, if we provide a clock setter.
In the agent. Does that mean we have to… expose some, hotel dependencies.
as APIs.
Because I think Clock is not part of the AutoJava API.
**Jason Plumb** 30:19 And it's decay.
**Hanson Ho** 30:23 the… So…
this is… may be a bit of a tangent, but, I think going through the process of building out the Kotlin stuff, there's a lot of, API things that you would think are APIs that are in the SDK packages. So…
**Cesar Munoz** 30:43 Lynn.
**Hanson Ho** 30:43 So clearly, I think for 1X, we could… we could… we're dependent on Java, so all the interfaces are like that.
But for 2.0, I think we could be a little bit… if we moved to Kotlin, then we could be a bit more,
selective, independent, and only depend on the API, and not have, like, this issue. But, yeah, this is definitely something that we have to contend with.
And I don't know if you can get away from it. Like, exporter, and processor is part of the SDK. So, I think the ideal of only, depending on API, when we're talking about our core being Java, is
Impossible, if they want to do… Add a spam processor.
So, for 1X, I don't think it's… I think it's unfortunately fine to have to drag that in.
So…
**Cesar Munoz** 31:43 Yeah, that's fair enough, just wanted to point out. And to be honest, it's strange to me that it's not part of the API.
Things like clock, and, and… I didn't know the exporters also are not part of it. It's… it's strange.
**Jason Plumb** 31:56 I was trying to find in the.
**Cesar Munoz** 31:57 there.
**Jason Plumb** 31:57 specification where the clock exists, and I can't, so if anyone knows where that is, tell me.
I'm sure it's in here, but I'm not awake enough to find it.
**Hanson Ho** 32:08 I don't know if it is…
I think it's because… it's not API because it's not something that is… it's… it's for Java only.
I think other clocks look different, and there's no…
I think there's an implicit, hey, system, something gets clock.
**Jason Plumb** 32:28 Yeah…
**Hanson Ho** 32:29 That's the only way I can explain it's why some of this stuff is not… is considered language implementation only, is in the SDK and not in the API, but…
I don't agree with that.
**Jason Plumb** 32:41 Yeah, well, and if something like clock… if the existing clock implementation in the SDK, which is an interface, I believe.
**Cesar Munoz** 32:50 Yeah.
**Jason Plumb** 32:52 if that's not in the specification, then in the Kotlin equivalent SDK implementation, you know, it doesn't have to behave the same at all, right? If it's not in the spec, it can behave completely differently.
**Hanson Ho** 33:08 It could still be in the API package if it's on the spec, I think.
You know, there could be things in there that's…
you know, that we could consider an API. Like, if we start doing agent APIs, for instance, you know, that is an API. Whether we want to put it in a different package, like, you know…
Android API or Java API.
**Jason Plumb** 33:26 Java Core has been… Java Core has been pretty strict, and I'm sure that you can find exceptions to this, but they've been pretty strict about attempting to, at least.
only include stuff in the core API packages that are part of the spec.
At least publicly. Publicly, yeah.
**Hanson Ho** 33:42 So… so things like clock… secret. Folks… yeah, so folks can't… Okay.
**Jason Plumb** 33:52 Which is why I was trying to find it in spec, but I don't know, like, is there a spec API or SDK spec in OTEL?
**Hanson Ho** 34:04 This could also potentially be one of those things that was put there initially, and, you know, it…
folks never went back to revisit it because of compatibility issues and things like that. It may not have been what would be done right now if they were starting from scratch, so…
But it is what it is right now, for, I think, for 1X. We…
if we want to expose this as part of the API,
Which I think is something we… we probably want to do. Well, we're gonna have to just… sorry, you have to take the SDK package.
**Jason Plumb** 34:43 Yeah, so I would like us to really figure this out. So it sounds like we're… it sounds like we're okay with adding it to…
The agent.
Is what it's sounding like.
**Cesar Munoz** 34:57 Yeah, it sounds good to me.
**Jason Plumb** 34:58 Okay.
**Cesar Munoz** 34:59 So I wanted to call out that we're gonna have, if it's not there already, to, you know, expose the SDK
library as a… as an API.
**Jason Plumb** 35:10 It's not a new change.
**Hanson Ho** 35:12 Yeah, I think right there, that SD resources resource builder is also part of the SDK.
**Cesar Munoz** 35:18 Adam.
Okay, so…
**Jason Plumb** 35:21 Alright, so it sounds like we've made a decision.
So I think I'm… I think I'm gonna approve this then, I think it's… it's good to go.
I just wanted us to, to be, like, careful and talk about that assignment.
So that, that then leads to the other pull request, which is the actual clock implementation.
Which I think I've been ignoring… oh, it has conflicts now, but I've been ignoring it until we figured out that other answer. But yeah, so this one does,
Use the elapsed real-time nanos.
as part of its implementation, so that's great. I think it's gonna solve a certain class of problem for us. It still doesn't address the desire to fetch time from an NTP server.
But you know, that can still… there's still an issue out there for that.
**Jamie Lynch** 36:21 Yeah, I'd be kind of curious to hear what other folks are doing for
like, obtaining time in Vowan SDKs? Like, do people follow this approach, where you use elapsed real-time nanos, and then
add coin-time millis, or do you use, like, NTB?
**Cesar Munoz** 36:43 The fetching time from… NTP server…
if I… it's been a while, but I think I…
subtract the current system elapsed time from what the MTP server returns.
So that I get the delta, and then for follow-up NTP queries.
**Jamie Lynch** 37:08 I use that value.
**Cesar Munoz** 37:11 Which I think is similar to the implementation of using the…
Well, I haven't checked the details, but from using the system, elapsed time… And subtracted from, from…
The, current time at the beginning, and…
I don't know if that… well, I need to check your PR more in detail, but essentially, I…
Take this delta and keep it.
For further, you know, queries to the NTP server.
**Jason Plumb** 37:46 I mean, to me, that approach makes a lot of sense.
**Cesar Munoz** 37:51 Yeah, but you depend on the NTP server to be available, so…
The clock that we're using falls back
just to the regular system clock if there's no NTP server.
**Jason Plumb** 38:05 I think that's the best you can do, right? Best you can hope for?
**Cesar Munoz** 38:08 units.
**Hanson Ho** 38:10 A lot of times you're out of range, or you're on a plane, you know, you're not able to reach that. I think the important part… the important thing is that, there's consistency throughout the duration of the lifetime of the process, so you don't have, like, you know, clock shifts, when you start a span, or…
So that even if the absolute time is… is off by some… some drift, the relative times between events, are consistent. And I think that's… that's the most important part.
So, embrace,
**Jason Plumb** 38:45 For, like, a rum… for, like, a rum display.
But if you're… but if you're, like, just to throw a different use case in here, if you're trying to correlate, some catastrophic… catastroph… catastrophic event happening on the server side with user events also experiencing pain, then you want absolute times to line up there.
Right? I mean, the alaft is less important than the absolute in that case.
**Hanson Ho** 39:12 Yeah, yes, but I think there's just a difficulty in general to make sure the absolute times line up, perfectly, especially the outlier. So it's almost one of those cases where, you know, in the aggregate, times are going to be generally correct, and you kind of drop that, but in the specific, you know, there's only one case to consider, which is low relative.
So, both, ideally, is important, and if you could, like, you know, when the SDK starts, you're able to reach the server, get the absolute time, minimize drift, set that, that's best, but you also don't want to, like.
hold the SDK until you get that time, so it's almost like it's the last fetch that is, you know, the best, and there's a… it becomes one of those things where it just gets tricky to get that extra little bit, so,
As long as you can kind of understand what the implementation is and where the… where it falls down, then that's the most important part.
Which is why setting your own clock is a good idea, because some people will want the absolute time to be most correct, and they may want to even, you know, pause the standardization based on getting that initial timestamp back, and they'll be able to replace this with, you know, us adding this into the agent API.
**Jason Plumb** 40:32 Do you… does Embrace have their own implementation or a clock? Like, do you… what do you do?
**Jamie Lynch** 40:38 Yeah, we basically followed the approach of SPR, so we use the elapsed real-time nanos, and then add-on, system coin-time millers.
**Jason Plumb** 40:47 What was the acronym you used? SBR?
**Jamie Lynch** 40:49 Elapsed, elapsed no time. We basically do what's in this, chainset we just discussed.
**Jason Plumb** 40:55 Okay, this one.
**Jamie Lynch** 40:58 Cool.
**Jason Plumb** 40:59 Okay, cool.
**Hanson Ho** 41:01 Yeah, I think that's like a typical Android approach, is, you know, not trust the sleep time, and basically count, you know, a lapse.
**Jason Plumb** 41:11 I don't want to necessarily put everyone on the spot, but if you know what it is, feel free to contribute it here for Datadog or Honeycomb. But it sounds like…
Totally.
**Mustafa Haddara** 41:20 Honeycomb doesn't do anything special.
**Jason Plumb** 41:22 Okay.
**Mustafa Haddara** 41:23 We should use the hotel clock.
**Hanson Ho** 41:25 And I think the hotel clock locks, the time, when a span starts. So a span…
I think there's a reference to the clock instance for each span, or at least the start time, so you're not gonna get, like, a shift between, but between spans and.
**Jason Plumb** 41:46 No.
**Hanson Ho** 41:47 Clocks can shift, right?
**Jason Plumb** 41:48 The span has a timestamp on it, yeah.
Cool. Disk buffering, are we ready to move on, or we don't talk about clocks? Anything else anybody wants to ask or add?
Alright, moving on. This breaking change, oh yeah.
**Cesar Munoz** 42:12 Well… It sounds scary, but it's… okay, so…
It's just that I wanted to bring attention to this issue. The,
It's been a while since I wanted to stabilize this buffering.
And the last time, I added a lot of changes to the Surface API,
But, just to make it, more intuitive to use.
But… I didn't change the, behavior.
However, this issue basically mentions that there is a behavior
Right now, which is that on every call to the next
For the iterator, so that you get the next item on disk.
the…
This buffering assumes that if you want to get the next item, it's because you already used the current one, so it deletes the current item, and then
Returns the next one.
Now, this person, mentions that, and I think it's fair.
That it's kind of like doing…
you know, on next, it's doing more than it should, because, you know, it probably… you shouldn't do this deletion of the existing item.
Automatically, and they proposed two alternatives.
I like the second alternative, which is to just manually call the iterator.remove.
function when you want to remove the item.
And, so, now, if we add this change, essentially…
It will be kind of a breaking change, because now people who might be using it today will have to call remove, so that they don't, you know, keep the data in disk.
But I think, I mean, in hindsight, I don't remember, I added a comment explaining more details, but essentially.
I think it's fair. Like, the behavior of automatically deleting stuff when calling next was something I added just to try to keep stuff
as we did in Auto Android. But it's probably not something that works for other use cases, so…
And it's kind of like a hidden behavior, if you will.
So, I think it's fair. I'm not opposed to adding this breaking change.
And… and just mark the… the library stable afterwards. But still.
I wanted to, I don't know, know your opinion on this.
If you have anything.
You know, against… Added this change.
Or you can have a loop later in detail, if you like. It doesn't have to…
I don't have to get a response right now.
**Jason Plumb** 45:12 I have a couple of opinions, I wanted to make sure other people have room to chime in.
Alright, I'll share my opinions. I hate the iterator pattern. Sucks. Not your implementation of it here, just in general. I never use it. I think it… I don't… it… whatever. I'm over it. I'm done with iterators.
**Cesar Munoz** 45:34 It's a Java… react, you know.
**Jason Plumb** 45:38 It is, yeah.
I mean, that raises a question, too, like, when we're trying to go pure Kotlin, what do we do for disk buffering? Oh no, we're gonna have to rebuild it again!
I think that coordinating… so, I'm fine with breaking changes to this API. Coordinating the upgrade of contribib with our implementation that needs to call remove, we'll have to just collectively remember to do that.
It would be cool if there were a way to force that.
So that any user would, like, would see some breakage or something.
I don't know.
It's too early for me to think of anything clever that we could do to… to force that to happen, but…
**Cesar Munoz** 46:25 Yeah, but in…
**Jason Plumb** 46:26 I was going, sir.
**Cesar Munoz** 46:26 Sure, you're not… yeah, okay, you're not…
like, against adding this kind of change, okay.
**Jason Plumb** 46:32 No, I think it's good.
Yeah, this person has a good point, that, you know, just calling next shouldn't have side effects.
Yeah.
**Cesar Munoz** 46:42 Yeah, that's true.
**Hanson Ho** 46:43 Yeah, that's the only comment I want to make, is, yeah.
You should be able to iterate without… modifying.
**Jason Plumb** 46:53 Yep.
So I don't have responded yet, yeah. I haven't had a chance to look at this yet, but I think it's a good change.
**Cesar Munoz** 47:05 Cool?
Thank you.
And since we have a bit of time, lastly, I just wanted to… well, unless somebody wants to add anything else.
To that topic.
If not, I wanted to mention, somebody opened an issue… sorry, I'm looking for it.
in Autel Android, Regarding GRPC.
So…
**Jason Plumb** 47:39 Gross.
**Cesar Munoz** 47:41 Sorry, PC.
**Jason Plumb** 47:43 Oop, did I say that out loud?
**Cesar Munoz** 47:44 No, don't worry, don't worry.
So, technically, this person can make it work with Core.
**Jason Plumb** 47:54 Yep.
**Cesar Munoz** 47:54 It's gonna be a lot of work.
But they can make it work. I just wanted to make sure
Because I remember, like, it's been a while since I, you know, haven't seen the source code, but I remember for a while, we had in the agent both options of sending HTTP or gRPC.
And it's fine. Right now, we have only HTTP, and I think that's what people should use. But, you know, we're gonna get these kind of issues created, so…
Is there… If we made the decision of just supporting HTTP in the agent.
And I think it's… it's…
Probably gonna be helpful to mention it somewhere in, like, in a doc where we say why we decided to do something like that. Maybe that could be helpful for these kind of issues.
And if not, then probably we should consider adding
this new DSL option for gRPC, but, you know, just wanted to bring it up. I'm fine with either option.
Actually, no, I think it's better to just keep HTTP, but…
Again, it's not… it's not my call, so…
Just wanted to bring attention to it.
**Jason Plumb** 49:15 Yeah, that's a good point. It's a good thing for us to be talking about.
**Hanson Ho** 49:27 I mean, this is another case study in…
you need to configure the OpenTelemetry instance. You want to add your own exporter. In theory, it should be, you know, easy to do, just drop it in. But then you have to set all the configuration yourself.
**Jason Plumb** 49:44 Yeah, so I was looking at where that happens, so we… yeah, we just… So… yeah.
We would need something in the initializer that is aware that we support multiple types. We'd have to somehow key on that to decide which class to instantiate here, right?
**Cesar Munoz** 50:06 If we want to add that support.
**Jason Plumb** 50:09 Yeah, if we wanted to support it. I think, you know, I think a strawman implementation would help us to talk about it, to see how…
How bad it is to use or to implement.
It does seem fine to me as long as we keep HTTP as a reasonable default.
Like, as long as we don't force the users to have to pick one, then I'm okay with us having it.
**Hanson Ho** 50:33 So what does the API look like, then?
**Jason Plumb** 50:35 I don't know, that's why I'm saying a strawman implementation might help us here.
**Cesar Munoz** 50:49 If I remember correctly, right now in the DSL, you have to call…
HTTP… something, and provide your endpoint.
**Jason Plumb** 50:57 Yes, I was… I had that up, let's see… Here…
Oh, that middle mouse button, I need that to be working.
So, you can set all this stuff, but in the… Endpoint.
**Cesar Munoz** 51:19 the…
**Jason Plumb** 51:20 Yeah.
**Hanson Ho** 51:26 Like, it's implied.
Yeah.
You need another… another endpoint configuration that's like gRPC endpoint configuration.
That thing gets exposed at the top.
**Cesar Munoz** 51:38 Yeah, and you will have to add here… another…
method, both for gRPC in the…
link that I just shared.
**Jason Plumb** 51:51 Which is… oh yeah, which is what?
**Cesar Munoz** 51:54 In the Zoom chat.
Therapy, because that… this is the first…
place that people get to configure stuff in the DSL. So, I guess we decide to add it, we'll have to add a new function, gRPCS.
**Jason Plumb** 52:11 Yeah. Yep.
**Hanson Ho** 52:19 And is that gonna be sufficient, having…
to, basically, out-of-the-box exporters? Or will somebody want, like, a third, or a fourth, or a custom?
And… because basically, if we do this, we're like, okay, cool. And then a third one, or a custom one, you have to go in the core. And how often…
**Jason Plumb** 52:38 OpenTelemetry has some language about this, I think, which is, that gRPC and HTTP are the main ones, with Proto being the default, kind of.
payload encoding, but there is also JSON encoding, which I think the web…
thinking with my client telemetry hat on. I think the web users love the JSON encoded…
telemetry format. I think if there was some other format, like, someone's like, oh, I need my Kafka exporter, like, okay, just use Core. Like, at that point, I think it's easy to say, we're not putting that in the agent, you know?
**Hanson Ho** 53:17 Like, if GRPC is called out as a privileged, you know, hey, these are the two main ones, I think adding support is reasonable, then.
**Jason Plumb** 53:23 It is, yeah.
**Cesar Munoz** 53:30 It sounds like we do want to add support for it.
Based on comments.
**Jason Plumb** 53:36 I think so.
**Cesar Munoz** 53:39 Okay.
**Jason Plumb** 53:40 Give him a thumbs up.
There you go.
Good idea.
**Cesar Munoz** 53:48 Okay.
Cool.
**Hanson Ho** 53:52 And this would not be a breaking change, because it's an addition, so no need to go too over.
**Cesar Munoz** 53:56 Yeah.
**Jason Plumb** 54:01 So we, we usually try and end these a little bit early, FiveTel, in keeping with other conventions at OTEL, but I do want to call out this community, you know, this I.O.
PR… If you haven't seen it, please give it a review. That's not PRs, this is PRs.
Yeah, so I don't know who this person is, but they decided to contribute a bunch of documentation for Android.
And I think it's getting pretty close.
There have been a lot of comments on it.
I think Jamie and I have looked at it,
It's awesome, though, because we've been dragging our feet about adding anything to the doc site about Android. Like, there's just that placeholder that's been there for, like, 6 months or more, and this person took it on, which is great, so I think…
they were like, I think I'm good, and then I was like, you didn't address any of my comments, and I think we've just thrashed a little bit, but they're circling back, let's see. Oh yeah, so…
C.
Yeah, I was like, there's a bunch of stuff I mentioned that you didn't resolve.
They're like, let me get on it, there's another… okay, so I haven't… I need to circle back on it, but I think it's getting pretty close, I think a first pass is better than nothing, so…
Cool. Sounds good. That's all. I'll have a look. Yeah.
Awesome.
Well, we did it. Thanks again for all the help.
And I'll see you in a week.
**Cesar Munoz** 55:37 Yeah, thank you.
**Jason Plumb** 55:38 Alright, take it easy. Bye.
