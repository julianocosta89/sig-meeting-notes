SIG: Android SIG
Date: 2026-03-31
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Jason Plumb 00:03:30 Hey, good morning.
Cesar Munoz 00:03:33 Hello.
Hey. Morning.
Jason Plumb 00:03:38 How's it going?
Cesar Munoz 00:03:39 David?
All good.
What was ScoopCon?
Jason Plumb 00:03:48 I had a really good time. I think, I definitely liked the pre-events a little more, like the Maintainer Summit and the Observability Day were kind of the strong… the strong days for me, but it was good all around.
Cesar Munoz 00:04:01 Sounds great.
Jason Plumb 00:04:02 Yeah.
It's interesting.
Cesar Munoz 00:04:11 experience.
Usually, the only thing I don't like is jet lag, but apart from that.
Jason Plumb 00:04:16 Yeah, I'm still jet-lagged. I got back on Sunday, so this is, like.
The beginning of day two for me.
Cesar Munoz 00:04:25 I see. At least you have a short week this week, don't you?
Jason Plumb 00:04:32 I don't think so, no.
Cesar Munoz 00:04:35 Okay.
Jason Plumb 00:04:38 Were you thinking holiday or something?
Cesar Munoz 00:04:40 There's a public holiday, I think it's across many… countries over here, the Good Friday… Stuff like that.
I guess it's not…
Jason Plumb 00:04:50 Yeah, exactly.
Cesar Munoz 00:04:50 They're ready there.
Jason Plumb 00:04:52 Yeah, because Easter's coming up, right? I think we don't get it.
Cesar Munoz 00:04:55 Got it.
Jason Plumb 00:04:56 Yeah.
Cesar Munoz 00:04:58 Hey, Jamie.
Jason Plumb 00:05:02 Hello. Okay, well, I'm sharing, so okay, we can probably get started, although… Servi dropped a couple of things in… the agenda, which is also something I wanted to talk about, so thanks to her for doing that.
I can reach out to her and see if she's gonna join.
Cesar Munoz 00:05:23 Got him.
Jason Plumb 00:05:41 Alright, well, let's, let's skip over those and come back to them, and I want to add another thing that I've been thinking about. Okay.
So, let's just push these first two on the stack, and maybe she'll show up, and then Cesar can talk about next steps regarding this thing.
Cesar Munoz 00:05:58 Got it.
Okay, this is the old.
Jason Plumb 00:06:02 Yeah.
Cesar Munoz 00:06:03 you know, issue about the instrumentation API changes.
It's a big change.
So, you know, even though it has a couple of approvals, I… I wouldn't like to merge it if there are some concerns.
And it seems like you have a couple JSONs, so I wanted to discuss those.
Jason Plumb 00:06:26 Yes, and I have been away and super underwater on workloads, so I'm probably not up to speed on the latest comments.
Cesar Munoz 00:06:37 Got it.
Jason Plumb 00:06:38 So, session… right, so… I think it exposed the session provider on the API, and the session provider is not yet stable, was the… I think the point I was making…
Cesar Munoz 00:06:52 I think that was one of them, yes.
Jason Plumb 00:06:55 Okay.
Cesar Munoz 00:06:58 Yeah, because we used to, well, we still do, provide a getter for the session ID.
But after these changes, that getter wouldn't be needed.
Because we will expose the accession provider.
Which is just an interface that has the same getter.
Jason Plumb 00:07:17 Yes.
Cesar Munoz 00:07:17 an ID, so… Yeah, the concern was to… if we need to stabilize that interface, I think it's fine, it only has that… that getter.
But then we were talking about what to do about the server observers… I'm sorry, the session observer stuff.
Which are also some APIs from the same module.
It sounds like you wanted to also stabilize those, because we are using them in one of our instrumentations.
I'm a bit confused by that, because, like, at first it sounded like stabilizing one of the interfaces was… Concerning, and now it sounded like we wanted to stabilize more.
as a solution, so that was a bit confusing to me. It was one of the things that I wanted to… I mean, I'm fine… To stabilize them, because essentially they're just… observer… Type of, you know, contracts.
But, yeah, that's kind of the discussion here.
Jason Plumb 00:08:33 Cool, so, yeah, I will jump in on that. I think, the main… the main point I was trying to raise is that if we… if… like, this is an instrumentation API enhancement intended to lead us towards stabilizing the instrumentation API. And if we have a stable instrumentation API, I don't think that we can use or expose in a first-class stable API, other interfaces which have not yet been stabilized.
If that makes sense. So I think we want.
Cesar Munoz 00:09:05 Yeah, that's fine.
Jason Plumb 00:09:06 Any other modules or interfaces that are used by this API, I think, need to be stable either at the same time or before, which is the only reason I was suggesting that as one of two options, right?
So.
Cesar Munoz 00:09:20 That makes sense. Regarding session provider, I think it's fine to stabilize it.
Jason Plumb 00:09:25 Okay, I think it's also probably not a big deal. I wish we had better spec support for that, or… you know, I wish there was something in the spec about client mobile telemetry and session provider, and I think that got stalled out, like, a year ago, and we don't yet have that really codified.
But I think we could still stabilize, I agree. It's a pretty small interface, and changes around that probably aren't too bad.
The oxygen.
Cesar Munoz 00:09:51 really talking about spec, I also wish we had the crash one.
Jason Plumb 00:09:55 I know.
Cesar Munoz 00:09:56 There, but that's another topic.
Jason Plumb 00:09:57 Yeah.
Cesar Munoz 00:09:57 Yeah, sorry, go ahead.
Jason Plumb 00:09:59 That's alright. So, I was suggesting that we could just expose the session ID, and you said no, because there's instrumentations that want to monitor For the session changes.
And I was like, I don't see that happening, and you're like, yep, it is, and I was like, oh, I didn't see that.
Right, and so we have this crappy cast… Which I hate.
But it's the only way for this instrumentation to know that, you know, to get… to get registered.
Jamie Lynch 00:10:35 So, my understanding is that instrumentation is the only thing that's actually using session ID provider right now.
Cesar Munoz 00:10:43 Yeah.
Jamie Lynch 00:10:44 I'm…
Jason Plumb 00:10:44 Do we not… do we not expose that on the OpenTelemetry Realm Builder?
I think… so I think the intention was for users in user space to also be able to subscribe to session changes, right? Which is what that provides.
the… the observer.
Cesar Munoz 00:11:04 With this change, that would be possible? Yeah.
But, like, right now… Using the agent, I don't think users can do that.
Jason Plumb 00:11:17 Okay.
So, let me look at the implementation one more time.
So the instrumentation… Test package… Where is it? This one. Okay, so install then becomes OpenTelemetry Rum. This is our stable That's also a stable interface.
And then the application context. Okay.
And… So, one other thought is that if we wanted to… do the thing I was suggesting, where we only return the session ID, right, so this idea… And we don't… so let's just… let's just talk this through real quick. So, if we don't stabilize session provider and observer, or publisher.
If we just want to return the session ID…
Cesar Munoz 00:12:32 Yeah.
Jason Plumb 00:12:33 Then, what we would need is a matching method to be able to monitor for session changes.
Like, ad observer.
And… what does that interface look like right now?
Let's see… So we have a session…
Cesar Munoz 00:12:52 Okay, you mean to keep the getter and add… another method into OpenTelemetry ROM to observe sessions.
Jason Plumb 00:13:00 Yes.
So it would be add session observer, but that's also not a non-stable interface, so we can't do that without stabilizing session. Okay, so all roads right now are kind of leading toward… dialing in session, is what I'm thinking.
Cesar Munoz 00:13:18 Yeah.
Jason Plumb 00:13:19 So, if we stabilize this, then I think I'm okay with this PR.
Cesar Munoz 00:13:26 I mean, I think it's fine, like, the observer… It's just, it just returns the session when something changes.
And the session just has an ID.
And I don't see it, you know, getting removed, getting rid of that ID in the future. Maybe we could add more stuff, but…
Jason Plumb 00:13:46 No, I think this is fine. I think this is great.
I'm willing to take this on, like, I'm not scared of the API surface here.
I think it's… I think it's okay.
Cesar Munoz 00:14:00 Okay, so one more thing, regarding the, cast that you didn't like.
Jason Plumb 00:14:08 Yeah.
Cesar Munoz 00:14:09 One way to avoid casting or checking for… for that casting would be to either making session provider extend session publisher.
or making Session Provider have a session publisher Getter, or something like that.
Jason Plumb 00:14:27 But this, this will go away with your change.
Right? Doesn't it go away?
What class is that? That's, that's the session instrumentation?
Cesar Munoz 00:14:38 Session… Session provider.
Jason Plumb 00:14:42 I think that change goes away, right? So this… Oh, it still has to do this.
Cesar Munoz 00:14:48 Admin session provider is still just that simple interface.
Jason Plumb 00:14:52 Oh, it's because we only have a getter for the provider.
Cesar Munoz 00:14:55 Yeah.
Jason Plumb 00:14:56 So we do have that thing that extends, it's the session manager, right?
Cesar Munoz 00:15:01 Yes, we… our session manager has, you know, implements both provider and publisher.
Jason Plumb 00:15:08 And what's…
Cesar Munoz 00:15:09 10.
Jason Plumb 00:15:12 What? That's in the… age.
Cesar Munoz 00:15:15 agent.
Jason Plumb 00:15:16 Not in this session.
Okay…
Cesar Munoz 00:15:20 Yeah, this is our opinion authorization provider, which is also a publisher.
Jason Plumb 00:15:27 We can't expose this, okay.
I mean, first of all, it's in the wrong module. Okay, so you're saying we could have another interface that… or we could have one extend the other, which I'm… yeah, or we could have a third interface that's both.
Somehow.
Cesar Munoz 00:15:40 I mean, we can also leave the cast check.
you know, it's… I'm just giving it as an option, given that.
Jason Plumb 00:15:47 Yeah, no, I appreciate that.
I mean, we could also add the publisher.
As a getter.
Cesar Munoz 00:15:57 Yeah, true.
Jason Plumb 00:15:59 Or that method I was talking about, which is, like, add… add observer.
Add session observer. Those are two ways of solving the same thing.
One of them exposes the internals a slight bit more.
Cesar Munoz 00:16:15 I mean, it's fine, it's just, I guess, my only… Which is… my only concern, like, world concern is really… Time will tell.
That I… that I can see is… It seems like adding more session-related methods to the OpenTelemetry ROM instance.
My… laid us into a kind of… Pattern, where we will add everything into that.
Jason Plumb 00:16:48 I know, you're worried, yeah, that's a legit concern. I appreciate that.
Cesar Munoz 00:16:51 There's… I mean… It's what Andre did with Context.
It's basically a God object there.
Jason Plumb 00:16:59 Yeah.
Cesar Munoz 00:17:00 If we want to go with that route, I mean, I just want to make sure we all know that That's what will happen, in that we're fine with that.
Otherwise, I mean… I guess, just providing one getter for the session provider.
Kind of leaves everything related to sessions within the session provider.
And, you know, that will keep things modularized in a way.
those… those two approaches. I don't know which one's better, to be honest. I'm not saying that.
One is worse, or something like that, it's just… Yeah.
Jason Plumb 00:17:45 Yeah, I… so… If, instead of provider, we had something that was both a provider and a publisher.
In the session package that we're… in the session module that we're trying to stabilize, then this problem goes away.
Cesar Munoz 00:18:03 Yeah.
Yeah, we could merge what's in the, Pro… in the publisher, within the provider, and make the provider a publisher too, or just keep the publisher independently, but make the provider extended.
Jason Plumb 00:18:22 Yeah…
Cesar Munoz 00:18:23 That… or make the publisher… sorry, the provider have a… getter for a publisher, I guess. Those are the three things that I come up with right now.
Jason Plumb 00:18:37 And these instrumentations have to have… because they're auto-serviced, they have to have a noARG constructor, so we can't really… what I'm getting at is I wonder if… I wonder if there's another way to give it the session publisher? Like, is this… this… this setup stuff for the session and its publisher Is available before instrumentations are installed.
Could we have another… I'm just riffing here on ideas, I don't know that this is a good idea.
But if we had another interface that was, like, needs… let's just call it Session Observer, for example. If the instrumentation was a session observer, Or had a getter for a collection of session observers, or something.
then we could invoke that, and have that be a separate concern from install, right? So what I think the tell is, maybe, here, is that we're trying to force a new… what I'm trying to do is to force a new session interface, and it's really this… this chimera that's doing two very separate intentions, and that, to me, is a smell, right? That you have a thing that we're forcing to do two things when it should just be one thing.
But maybe there's a different way of solving this problem, and that's allowing these instrumentations to get Or to add observers through another mechanism that's outside of install.
I know there's only one that does it now, so it's hard to know that there's a pattern there.
Cesar Munoz 00:20:10 Yeah, I mean, I… I'm not sure I follow, but if you, if you like… Maybe, maybe, you know, adding a comment later, and I'll check it if… for some ideas.
I guess, if I understand correctly.
It… it will kind of make the instrumentation The instrumentation itself will have to Somehow tell that it's… that it can receive Or that it can observe sessions.
So that… I guess, in a way, we still will be doing the cast thing, it's just somewhere else, right?
Because in this case, when we install the instrumentation, we will have to check if the instrumentation is also this other type.
So that we called, I don't know.
Oh, I think the publisher or something.
Jason Plumb 00:21:04 I think we could still leave the session provider on there.
Or the getter for the ID, either one, then. But if we can avoid doing this cast by pulling this into some other… Interface method that doesn't exist yet.
Then that would allow us to… Just make this, you know, a getter, and then we don't have to stabilize session.
Because it would not be part of the… instrumentation API. It'd be a different.
Cesar Munoz 00:21:35 Okay.
Got it, you're saying as an alternative, just don't… to not having to… Stabilized session, altogether.
Jason Plumb 00:21:44 I mean, I think that's a byproduct. I feel like I need to riff on this and actually just try a couple of things, and see if it feels bad.
Because it's 8 o'clock in the morning, I haven't thought about this for more than a few minutes.
Cesar Munoz 00:21:59 Yeah, no worries. But I also don't have jet lag.
Jason Plumb 00:22:02 And I don't wanna… I don't wanna stall this PR anymore, because it's been way too long already, and I feel bad about it, but… I think it's also okay to get this in without stabilizing the instrumentation API, yet. Like, this is… this is probably progress.
And it has approvals.
Cesar Munoz 00:22:20 If you ask me, I'm fine. I mean, the session so far It's quite simple.
And the stuff that it has, I think it's… I don't see it going away. I don't see the session ID going away, for example.
So, I'm fine with stabilizing it.
Yeah, I think… It's… it's also… I mean, if you… if you can have a look, I mean, I don't want to rush or anything, but I think that if we want to, in the end, if we decide going with this approach, where we will Exposed session provider.
I think it's important to do so before the next release.
Jason Plumb 00:23:05 I agree, so I was just gonna suggest that we make a milestone that includes this PR.
Cesar Munoz 00:23:11 Okay.
Jason Plumb 00:23:12 make progress on that. So you want… you… I mean, you think we should get the instrumentation API stable before the next release?
Cesar Munoz 00:23:19 Yes, because otherwise, we will have to… Because the next release will stabilize OpenTelemetry ROM, if I'm not mistaken.
So…
Jason Plumb 00:23:32 Yes.
Cesar Munoz 00:23:34 You know, in this PR, I'm removing a method from that interface, so that wouldn't be possible afterwards.
Jason Plumb 00:23:44 Oh, you are removing one from there.
Cesar Munoz 00:23:47 Yeah, the session ID getter.
Jason Plumb 00:23:50 Oh, because it forces going through a provider?
Cesar Munoz 00:23:53 Yeah.
Jason Plumb 00:23:55 This one.
Cesar Munoz 00:23:55 kind of redundant.
Jason Plumb 00:23:57 Yeah, no doubt.
Cesar Munoz 00:23:58 there.
Jason Plumb 00:23:59 Well, yeah, because I don't love the law of Demeter problem there.
Cesar Munoz 00:24:05 You know, like, changing… chaining… Called…
Jason Plumb 00:24:08 I mean…
Cesar Munoz 00:24:09 It's fair, to be honest.
Jason Plumb 00:24:11 It also forces the type to be exposed and disencapsulated it before.
Why is software so hard? David, were you gonna say something?
Okay.
Cesar Munoz 00:24:30 I think it's always hard to try to make things future-proof.
You know?
Sorry, David.
Jason Plumb 00:24:43 Okay, no, sounds like no. Yeah, so this has not been released yet, but I think we have this already set up to stabilize the OpenTelemetry…
Cesar Munoz 00:24:54 Yeah.
Jason Plumb 00:24:55 interface.
So… Interesting. Hmm.
Cesar Munoz 00:25:00 I mean… You know, you can take a look.
Offline, and yeah, because… I guess it's not… it wouldn't be nice if we, like, rushed this decision right now, if you haven't, you know.
Properly seen it.
But yeah, that's what… that was my concern, like… Creating a release before this.
Jason Plumb 00:25:30 Jamie, any concerns with stabilizing session as it exists today?
Jamie Lynch 00:25:35 I think.
I've got a few things I'd like to change.
Just in terms of… like, idiomatic Kotlin syntax. Okay.
I guess so, yeah.
Jason Plumb 00:25:51 Yeah, okay.
Jamie Lynch 00:25:52 Until we've had it not so bad.
Jason Plumb 00:25:55 Yeah, especially if it's, yeah, if it's, just, like.
syntax or feel stuff, I think that's great. I think there's room to do that.
When was our last release? Because I feel like we might be behind.
Oh, we're behind.
We're violating our own… we're violating our own policy.
Cesar Munoz 00:26:16 Or are we? Because do we wait for all the upstream stuff to get released before we do our release?
If that's the case…
Jason Plumb 00:26:28 A week after the release of Upstream. So, Upstream is… when was that released?
Last week. So we're close.
Cesar Munoz 00:26:36 Yeah, but I…
Jason Plumb 00:26:37 Let's good.
Cesar Munoz 00:26:38 Do you know if, Contrip has been released recently? Because I…
Jason Plumb 00:26:43 It is not.
Cesar Munoz 00:26:43 Okay, it hasn't.
Jason Plumb 00:26:52 Yeah, that's behind.
Cesar Munoz 00:26:54 I was actually waiting for that as well.
Jason Plumb 00:26:56 For something in disk buffering?
Cesar Munoz 00:27:02 Yeah.
Jason Plumb 00:27:03 That's the only thing we use from here, right?
Cesar Munoz 00:27:04 Oh, yeah, the API 21, fakes.
Jason Plumb 00:27:08 Yes.
Okay.
Well, we should release this, this, like, probably ASAP.
It looks like it's been forgotten, so I can… I'll take an action item to do that today, assuming it's fine with everyone.
Jamie Lynch 00:27:35 I think I'll try and, list out the things that I would like to change about the session API. I'll probably just try and throw a PR up.
Jason Plumb 00:27:46 Cool. I want to make sure we have plenty of time to get to Service stuff, because I think it's pretty big as well, but I want, just really quickly on this… on this call, before I… get too much more brain damage. I want to add this to a milestone and throw a couple of other placeholders in there real quick. Why is this being like this?
So I want to make a new milestone for… what's our next version?
Cesar Munoz 00:28:11 Oof.
Jason Plumb 00:28:12 Check something?
3?
Cesar Munoz 00:28:17 3.
Jason Plumb 00:28:19 Okay.
I'm very hopeful here.
Okay… And I want to make a new issue, which is, stabilize… Session?
And it already pre-fills that milestone. Good. So, what was your PR called?
It's, a 3385. Sorry for just doing this live, but…
Cesar Munoz 00:28:58 I don't worry.
Jason Plumb 00:29:00 I think it's gonna be…
Cesar Munoz 00:29:00 No, I think it's…
Jason Plumb 00:29:03 Oh, it doesn't autocomplete these? Oh, man.
I'm so sad.
Cesar Munoz 00:29:07 it is… 1645.
Jason Plumb 00:29:11 Oh, one sec… oh, it's a comment?
Cesar Munoz 00:29:14 Yeah.
Jason Plumb 00:29:15 Yes, okay.
Cesar Munoz 00:29:23 Cool, thank you.
Jason Plumb 00:29:25 Yeah, yeah, and I think there's, That's cool. Somebody's ahead of me on this one. And then, it's probably Servi, you sneaky thing. And then… I… There's one more that I thought of. Oh, yeah, so need, contrib.
Right?
Like, that should happen automatically.
Cesar Munoz 00:29:56 Yeah.
Jason Plumb 00:30:02 Yep.
Jamie, should we publish a disk buffering from Kotlin?
And then we can source that instead of contribib.
Jamie Lynch 00:30:23 Just to put you in spot.
Jason Plumb 00:30:28 I got enough fish to fry right now.
Jamie Lynch 00:30:30 Yeah, that'd be quite an undertaking.
Jason Plumb 00:30:33 Yeah, okay, so I think we're good on this milestone. I think that this will help us. Okay, cool, yes. Anything else before I stop talking about this?
Cesar Munoz 00:30:45 No, it's okay for me.
Jason Plumb 00:30:47 Okay.
Phew!
Alright.
And I think we've kind of talked about the release.
Alright, let's go back up and talk about Serbi's situation with the AndroidX thing that I took a wild stab at and failed.
And… it looks like… Yeah, so… is everyone caught up to speed on what this is?
Do you want to summarize… do you want to give us the quick 2-second summary, Serbi?
Surbhi Agarwal 00:31:34 Yes.
So… Thank you.
First is, I didn't sneak it in into that milestone, maybe crank dead.
Jason Plumb 00:31:42 Okay.
Surbhi Agarwal 00:31:43 Yeah.
Jason Plumb 00:31:44 Frank's not on this call, though, is he?
Surbhi Agarwal 00:31:47 He is not…
Jason Plumb 00:31:48 Okay.
Surbhi Agarwal 00:31:50 Yeah…
Jason Plumb 00:31:51 Well, that was quick, because that milestone was brand new.
Surbhi Agarwal 00:31:54 Yeah, I don't know how that happened.
Jason Plumb 00:31:58 Okay.
Now, now you got me wondering, will this show us?
It was, it was a PR. It was not, it was not issue, it was a PR.
this… Supply.
No.
Surbhi Agarwal 00:32:17 Maybe all open issues got marked? No, but… I think summer polish shoes.
Jason Plumb 00:32:25 Let's see… I don't know how it showed up in the milestone.
Surbhi Agarwal 00:32:30 Yeah…
Jason Plumb 00:32:32 Oh.
Cesar Munoz 00:32:33 Hey, what's.
Jason Plumb 00:32:33 I added it last week. I did it last week!
Cesar Munoz 00:32:36 Oh.
Jason Plumb 00:32:36 Alright, well, jet lag brain strikes again. Alright, back on track, sorry, thank you.
Surbhi Agarwal 00:32:42 Yeah, so basically, what is happening is… There is dependency on these AndroidX libraries that are spilling into the host apps via our SDK, and they might always not be needed, so we can do some cleanup here, and We faced a customer issue, which was difficult to find, and in the end, it turned out that we were upgrading their version of Android X Core and Android X Navigation. That was leading them to see a flicker when their app started. They couldn't handle the newer dependencies, versions.
So, that's why this is, something that is probably important that we should look into. So, I did took, some time to look into this, and… There are a few things that we can do. There are not many of these libraries, so I added a comment in the end about certain libraries and what we can do about those. So, four solutions I mentioned here.
So, AndroidX Core is sort of a base library, which we probably can't get rid of.
It… right now, we only use it for network monitor, for checking the permission, phone state permission in the… for carrier details, so… but then I do see it is being added at… in a lot of modules, that can probably be corrected. But yeah, the first solution was to use minimum needed version. So, wherever we can't get rid of the dependency, we can… it's only a problem if we update the host steps dependency to a higher version. It's not a problem if we are on a lower version.
version, and they are anyway on a higher version. It resolves to the higher version itself, right?
So, if we keep our dependency versions to the lowest needed, that way we prevent These issues for the host app.
And that if they are even on a lower version than the version we have kept it on, then the feature won't work for them. So they anyway have to upgrade, there's a different problem there, right?
And… some contenders for this could be the AndroidX Core Library, the AndroidX annotation Library, which we use.
The lifecycle one, because app lifecycle management is sort of important.
And then the one solution could be to keep them to compile only. That prevents it from spilling into the host app. And some good contenders for that is these few auto… the service provider interface-related dependencies that we have currently in all the modules. They can be compile only, they do not need to be there at runtime. And this, obviously, I have not tested it, but that could be a solution for them.
And the other thing that came up was to separate things into separate modules, isolate into separate modules where possible. So, a good contender for that is the visible screen service that is used by the activity and fragment instrumentations. It is also used by Core to assist that span and log processor, which adds screen.name to all the spans and logs.
So, this could probably live within its own separate module.
Where it can be used by the relevant instrumentations.
So this gets rid of the AndroidX fragment dependency, it puts it where it is needed.
Specifically. And then the last one was to use reflection.
I did see Cesar did mention something about reflection in the PR. So, basically, R8 minification would remove the class and reflection would fail if it is looking for that class via name, right? There is a solution for that, like, you can use aggregate keep annotation for that class.
But it is a library class, so you can add a ProGuard rule.
to ensure that Ari doesn't remove it.
I did look into whether, like, it… usually reflection is not good, right? So, I did check that it wasn't causing any performance concerns here, it was a quick check. So, only once it is checking whether that navigation host So, where we are using this AndroidX… navigation, library, invisible Screen Service, like, it's in my PR, the… solution in my PR I'm talking about.
So, if we go to that…
Jason Plumb 00:37:44 This PR?
Surbhi Agarwal 00:37:45 Yaw.
So, basically, what I did here was invisible screens. So, I removed the dependency on AndroidX navigation. Now, this visible service only visible screen service only depends on AndroidX fragment. That is needed, that we can't get rid of. So, here, navigation was only used for this nav host fragment, which we wanted to ignore. So, what it does it… does is, only once it figures out whether nav host Class is on the class path.
And if it is not, it, the check of whether a particular fragment is a Nav host fragment fails.
this check of reflection is only once, and otherwise the recurrent call wherein it is checking is nav host on line 108 below. That is just a simple call like the isInstance call, so it is not adding any performance impact.
Cesar Munoz 00:38:45 Yeah, I took a quick look. I haven't checked the whole context of the issue.
As you said, survey, it is possible to make things work with reflection.
It's just that it would require us to be… more… For us to be aware of that, And to create… ways for it not to fail, or to create some sort of crash, or something like that. So it's not that it… it is possible, but it's just… it adds… some… some level of frag… fragility, fragility to… to… to the code base that… I mean… It's just one more point of failure that we're adding to the project, so…
Surbhi Agarwal 00:39:35 Yo.
Cesar Munoz 00:39:36 It's usually not a good idea because of that.
I mean, it might work… once, but then, I don't know, maybe something else changes… In that library, especially it's a library that we don't have any control of, where maybe other stuff that are needed by that class RUs, you know, With reflection, or whatever, internally, and then that also breaks it.
I mean… It's not impossible, but it's just fragile. It makes the codebase fragile, so I think we should avoid it, usually, you know, resorting to brokard rules or stuff like that.
In my experience, tends to be the last resort.
So… what I was trying to mention in your PR was.
It looks like the depend… these dependencies are part of a… I haven't taken a deep look, but it seems like dependencies are part of the… one of the service tools.
Surbhi Agarwal 00:40:36 Yo.
Cesar Munoz 00:40:37 And what I was mentioning there is, like.
I was trying to take a step back, And think, you know.
If it makes sense for the tool that uses this library to be part of a service tool to begin with, because service tools are meant to be shared tools for… I explained it there better.
But essentially, if we're only using this in a module, or maybe two that are specifically, you know, scoped to one or two instrumentation, then probably the option two, which I think is not option three.
will make more sense, which I think is the one that I… kind of talk about in your PR?
Yup. Now… One question that I have about the issue That the user created is… They're having this issue where they're… Dependencies get updated because… They are including the instrumentation that relies On this.
Surbhi Agarwal 00:41:44 No.
Cesar Munoz 00:41:44 This dependency themselves? No.
Surbhi Agarwal 00:41:47 No, so we depend on the services module.
And that way, the services module has the visible screen, so that's where we are spilling the AndroidX navigation and AndroidX core dependencies, which is problematic for them.
Jason Plumb 00:42:03 And there was something from CORE as well, wasn't there?
Surbhi Agarwal 00:42:07 Yeah, core we do not use.
It was Android X code dependency.
Jason Plumb 00:42:13 Okay.
Cesar Munoz 00:42:14 Got it. So… If possible, ideally for me, would be to, try to see if it makes sense for this tool to be… to be in services, tools, and… and if not, then move it to the places where it's used. And if in the future… I mean, I guess this is a… it's another issue, but… I just wanted to mention that I think that if, in the future, some user adds an instrumentation that carries a… Transitive dependency with it.
That it's needed, because it makes sense for that instrumentation to work.
And they don't like kids because it causes this kind of issues.
in those scenarios, I think… We should… I mean… What I'm trying to say is that if that dependency makes sense, because a user needs an instrumentation, and the instrumentation needs that dependency.
I guess in those cases, I don't see why we should… address the issue, because it's like, if you need that instrumentation, and that instrumentation relies on this dependency, then you have to be willing to get in this instrument… this dependency.
There, updated, so…
Jason Plumb 00:43:37 Bo… Fair enough, but what's the downsides with this approach, then?
Surbhi Agarwal 00:43:43 This is not applicable everywhere. So, I just quickly want to answer what Cesar was saying. Please. So, basically… you are, like, like, you are right in saying that if the customer uses that instrumentation, they would have that dependency. But the problem is.
their, like, Android X dependencies, apps are sensitive to them, because it affects how their UI works, and Android X has not done a good word… has not been good in terms of backward compatibility, right? It causes breaking changes.
So, we should not update their version to the… because apps do not have the bandwidth.
that when they use our SDK, they also update their UI altogether, right? Just to use our SDK. That's not a… good ask of them. So, it can be easily mitigated by us keeping the dependency to the minimal needed version. That way, we do not affect them, and they can onboard to our SDK quickly without needing the UI changes, right?
Cesar Munoz 00:44:52 Well, that's true, you mean pinning, pinning a lower version.
And living there.
Surbhi Agarwal 00:44:56 No, they can pin a lower version, that's a solution that we have given them right now that we are using.
Jason Plumb 00:45:03 I say they're saying we can pin, like, Android.
Cesar Munoz 00:45:05 Yeah.
Jason Plumb 00:45:06 lower version.
Surbhi Agarwal 00:45:06 He can, yeah, yeah.
Jason Plumb 00:45:07 That was the first option, right?
Jamie Lynch 00:45:10 Yeah.
Cesar Munoz 00:45:11 Yeah, that's another option.
Jason Plumb 00:45:12 Jamie.
Jamie Lynch 00:45:13 Another side of this is that… If we aren't on newer versions, then some folks will be blocked from using newer versions of AndroidX libraries.
If we go too far back.
But I guess that depends on how far back we go.
There's also the option for folks to downgrade the Gradle dependency.
Like, you can alter… What version it gets resolved to.
Surbhi Agarwal 00:45:45 But, like, that's not a good solution, because you get to know it later. So, like, we spent considerable amount of time figuring out that this dependency version upgrade is an issue for them, and then we figured out, okay, you pin it to the lower version. And having that code block wherein you are pinning the dependencies to the lower version in your app is also not a good ask of them. Like, it is difficult to maintain.
Cesar Munoz 00:46:11 I guess we can try to… to, as much as we can, as much as possible, to not be… turn this into an issue for them. But I guess to a point, and probably this is something that Jamie was referring to as well.
I mean, you mentioned, survey, that Google hasn't done a good job keeping backwards compatibility with this library, so wouldn't that mean that if we pin within our library, we pin an older version of this Android X library, wouldn't that… probably make it not compatible with the latest Android X versions.
Later, that will cause another issue, kind of the inverse of this.
Jason Plumb 00:46:51 Yeah, exactly.
Surbhi Agarwal 00:46:53 Could it be an issue with the inverse thing? Mostly, it is not.
it adds features. So, what I was referring to was, like, AndroidX Core, if you guys remember. After 1.13.0, anybody who upgraded beyond that, they needed to upgrade that compile SDK and target SDK to more than 35, otherwise Android build would fail.
So, I think going to higher version is a problem.
And anyway, so keeping the lower version is not a problem. Why? Because when the host tab uses our SDK, the Gradle resolves it to their version only, not the lower version that we are using here. But our SDK should work with that. And it would work.
It is not removing stuff, probably.
Yeah, that's a good… that's a thing, yeah.
Cesar Munoz 00:47:51 I'm open to pinning a lower version, but if it starts causing issues in the future, I… every time we discuss about issues like this, I remind… it reminds me of the Katherine… sorry, no, the, yeah, the Catherine minimum version support for OKHCCP.
where we contacted the OK HTTP team And they told us that if we needed to use an older version of Kotlin, then we had to use an older version of OKTP.
Yeah. And that, to me, that… I mean, at the moment, I thought, well, they're quite, you know, lazy, aren't they?
But now, I understand them. It's like, it's difficult to keep up, you know.
With, you know, security and compatibility issues and all the stuff, while at the same time keeping Support for very old versions.
So…
Jason Plumb 00:48:46 So… Are there… are there places in non-instrumentation code where this option does not work? So, I think what I was… Lazily trying to do was to reduce… or… runtime… declaration on these, and only have it be compile-only. Meaning… if these classes are there, they get used. If they're not, maybe we… if it's in instrumentation code, I'm fine with that instrumentation failing if the user hasn't provided these libraries.
If it's in core, then it's a bigger problem.
Cesar Munoz 00:49:23 The one issue that I see with this option, compile only, is that Let's say it relies on a library that we add as a compile only, because we assume that it will be present in the host app.
Jason Plumb 00:49:37 Right.
Cesar Munoz 00:49:38 If it's not present in the host app, then we have to resort to reflection to check that it's there.
Jason Plumb 00:49:49 Because it could be used anywhere in the instrumentation, and we don't want a no-class stuff found.
Cesar Munoz 00:49:53 Yeah.
Jason Plumb 00:49:57 Yeah.
This is a pickle. I don't like it.
Surbhi Agarwal 00:50:13 Yeah, we definitely need a mix of, like, a mixed strategy. I think keeping runtime dependency on things Like, keeping them… Isolated to the places where they are needed.
And then having them runtime only as needed is, like, the right approach.
So, they… if they want to use that instrumentation, they get that runtime dependency. But sometimes here, we are, like, having them have it without having to use the instrumentation. That… those things we should correct for.
Cesar Munoz 00:50:53 Yeah, I agree.
Do you think options, right?
Jason Plumb 00:50:59 Yeah, it sounds like we're leaning toward 3.
Surbhi Agarwal 00:51:02 No, it doesn't work everywhere. So, like, option 3, I think we are leaning towards for the visible screen service.
Which reduces the dependence on AndroidX navigation, and AndroidX Fragment as well. But then, core module… AndroidX Core, Lifecycle, annotation, these we cannot get rid of.
So, like, for them, we… like, the solution I thought could work was using the minimum needed version, but we are thinking about having the inverse problem, right? Like, that… And using compile only for the Google dependencies, I think that would work as well, because they are anyway not needed at runtime. But, like, the first solution, like, what is the solution for AndroidX code lifecycle and annotation, then?
Jamie Lynch 00:51:59 Would it be worth…
Cesar Munoz 00:51:59 a little…
Jamie Lynch 00:52:00 maybe… Doing the things we know will work, like the fragment and navigation, and… basically keeping… reducing the scope of, like, these Android apps dependencies as much as possible, and then we could… Kind of see what… The glass radius would be of any… Change for, like, options 1, 2, 3, or 4?
Jason Plumb 00:52:25 Yeah, it might simplify, kind of, the problem space, I think, right?
Because we're talking about, like, 5 different things at the same time.
There's, like… And maybe, maybe they're all kind of different. So, like, this thing… when I was just hacking on this, I found… one of them was just straight up not used, or not needed. I forget which one it was, like… I think it was this one.
Surbhi Agarwal 00:52:52 Yeah, this is there in all the modules, and it is not used.
Get rid of this one. It is only used for checking the phone state permission.
Jason Plumb 00:53:02 Yes, but this is not used.
In court.
Surbhi Agarwal 00:53:06 Yeah, it is, like, used in the network monitor, related classes, wherever.
Jason Plumb 00:53:13 Sure, but that's… That's not in core, that's a separate module, right?
Surbhi Agarwal 00:53:17 Yeah, yeah.
Jason Plumb 00:53:18 Yeah, yeah, so this is… this is too high of a level for this. It needs to be at the more granular… So, I will… I will just change this and just make it a one-line PR.
Yeah. And then we can address this in a different one. To Jamie's point, like, maybe we can do the things that we know are kind of, like, safe and move the ball downfield.
Surbhi Agarwal 00:53:39 Yes, that sounds.
Jason Plumb 00:53:40 The next step. Okay.
Cesar Munoz 00:53:41 Sounds good.
Surbhi Agarwal 00:53:42 Also, in my PR, there are some things that we can merge, so I'll remove the reflection change. Similar to your PR, I realized that we were depending on AndroidX preferences in the services module, just to get hold of the AndroidX fragment dependency, which is the translator.
Jason Plumb 00:54:01 I hate that. Okay, yeah, let's fix that.
Surbhi Agarwal 00:54:03 So I was able to fix that and test it out. So, I will remove the reflection part. That would be a separate PR to separate out the visible screen service.
And we can still take time to think about what to do about Core, I guess I can separate. I'll try that, and we can think about AndroidX lifecycle and… AndroidX annotation.
Annotation is, like, an easy thing to keep to a lower version, because the newer libraries would just add new annotations, right? They wouldn't remove it. They can deprecate it, but they wouldn't remove it, right?
So, pinning to a lower version might work there for annotations.
Cesar Munoz 00:54:49 Also, annotations.
It probably is worth checking what annotations are we using, because maybe some are no longer needed.
Jason Plumb 00:54:58 Are we talking about this?
Cesar Munoz 00:55:00 No, the one…
Surbhi Agarwal 00:55:02 About one first.
In the meantime.
Cesar Munoz 00:55:04 first item.
Jason Plumb 00:55:06 Mmm… which one? Oh, the AndroidX annotation.
Cesar Munoz 00:55:10 Yeah. Because… If I'm not mistaken, I think one of the annotations that we were using was non-nual, or null -level stuff.
And, you know, migrating to Kotlin, that's no longer needed, so…
Surbhi Agarwal 00:55:24 through that.
Cesar Munoz 00:55:26 Oh, there we go, keep… And, yeah, no, okay, we might need it.
Jason Plumb 00:55:30 That's in the demo app, yeah, so we're using requires API…
Surbhi Agarwal 00:55:37 Which is needed at a lot of cases.
Cesar Munoz 00:55:39 that I think requires API, it's… it's because that's how we configure our API check to look for that one, but.
Jason Plumb 00:55:50 Right.
Cesar Munoz 00:55:51 Probably just create a… Internal annotation, and get rid of that.
Jason Plumb 00:55:56 Maybe. I mean, I'd like to see what that looks like. This one should not be retained, right? This is a compile-only annotation, probably?
I hope.
Cesar Munoz 00:56:05 on Athena.
Jason Plumb 00:56:06 So that one's… that one doesn't matter. And then… I mean, I think it doesn't matter.
Cesar Munoz 00:56:14 I think it's fine to get in rid of it.
Jason Plumb 00:56:17 Yeah.
Requires API guarded by…
Cesar Munoz 00:56:24 Yeah, I mean, that's just… Good, practices.
Jason Plumb 00:56:29 Exactly, yeah.
Cesar Munoz 00:56:30 But yeah.
Well, probably we can go…
Jason Plumb 00:56:35 A lot of places.
You know.
So do we think that's a good practice here in general, is just to reduce our usages of Android X where we can? As long as it's, like, not… A ton of effort.
Yeah. Because these are really nice to have, right? Like…
Cesar Munoz 00:56:57 Yeah, but it's just that those… AndreX Labor Day bump.
minimum API version, SDK version, so that's… that's annoying for users, so…
Jason Plumb 00:57:09 But what do we do without it, right? Like, if we're not… I'm just picking one… At whim here. But if we don't have this… What's the, what's the implication?
Surbhi Agarwal 00:57:20 There is a buildconfig.sdkint, and we can check whether it is more than the required API level or not.
Right?
That is all the… And build config.
Jamie Lynch 00:57:36 It's also possible to define our own annotation like this.
Cesar Munoz 00:57:42 Yeah.
Jason Plumb 00:57:42 with an employee.
Surbhi Agarwal 00:57:43 Back to my…
Jason Plumb 00:57:44 An implementation that looks for it and does the needful.
Jamie Lynch 00:57:47 Yeah, so it really depends on how much we're using it, if it's, like.
About 10 instances throughout the project, then… Yeah, it doesn't really feel worth a dependency.
Jason Plumb 00:58:01 Yeah.
Cesar Munoz 00:58:01 I sent a link, that's the reason why we… we need it.
Jason Plumb 00:58:10 Let's see…
Cesar Munoz 00:58:11 that I'm aware of.
That's for… it's for anima sniffer. So we can… We can set any annotation here.
to replace it.
Jason Plumb 00:58:26 Oh, interesting. Okay, so we can make our own.
Cesar Munoz 00:58:29 Yeah.
Jason Plumb 00:58:30 Okay.
Oops.
Surbhi Agarwal 00:58:34 Yo.
I will create PRs for these things that we discussed, update my new… update my existing PR as well, with the changes that we are okay going forward with.
Jason Plumb 00:59:14 Yeah, sounds good.
Cesar Munoz 00:59:17 Thanks, Harvey.
Jason Plumb 00:59:18 And we are about out of time, we did not get to talk about network timing.
Surbhi Agarwal 00:59:21 Yeah, I just quickly wanted to add, I need your input, Jason. I did get a go-ahead from Cesar on one ambiguous thing that we discussed in the last Android SIG. Yeah, yeah.
added a comment and I tagged you. I will ask Hanson as well, Async. I needed his input as well. So you mentioned about complex attributes, but I think you were referring to using them if we were to stick these attributes in the span.
But do you mean to use them in the event as well?
Jason Plumb 00:59:54 I did, yeah.
Surbhi Agarwal 00:59:55 Yeah. Then, what do you think it should look like, yeah?
Jason Plumb 00:59:59 Yeah, I would have to sketch it.
I would have to maybe give an example of what it might look like instead of using complex attributes.
Surbhi Agarwal 01:00:07 Yo.
And then I can, like, work to see if that, fits this proposal, yeah.
Jason Plumb 01:00:17 Cool, yeah, I mean, I think… my instinct is that it absolutely would. The challenge is that there's, like, no… I don't think there's any great… prior art in the semantic conventions repo for events having complex attributes, even though that's the design, like, that's the intention, that's… that's the solution we arrived upon after a year of arguing about it, so I think it would be good to break some ground there as well.
Surbhi Agarwal 01:00:41 That sounds good.
Jason Plumb 01:00:43 As painful as it might be.
Surbhi Agarwal 01:00:45 Yeah, yeah. It shouldn't be, right? If the design is there, I think it should be straightforward, we'll stick to that design.
Yeah, we'll try to model it in a good way.
Jason Plumb 01:00:57 I mean, I'm also jokingly gonna say, yeah, talk to everyone's ingest team, because we know that that's probably true as well.
Surbhi Agarwal 01:01:04 Oh, yeah, that's a concern. True that.
Jason Plumb 01:01:09 Yeah.
Surbhi Agarwal 01:01:09 I think I should start with talking to my Injust team first.
Jason Plumb 01:01:13 But I'm sure it's true, like, does anybody else handle complex attributes on events yet? I… I doubt it.
Does Elastic do that, Cesar?
Cesar Munoz 01:01:23 I heard that it was a concern, maybe they were planning to flatten them, or something.
Jason Plumb 01:01:30 And that is all…
Cesar Munoz 01:01:31 Oh, so far.
Jason Plumb 01:01:31 That's a design.
Cesar Munoz 01:01:32 Already there. Yeah.
Jason Plumb 01:01:34 Cool. Well, I think we have to think about calling it.
Cesar Munoz 01:01:39 Yeah.
Jason Plumb 01:01:40 I wanted… I saw it in the chat, David, I'm sorry, there were some questions that looks like they were kind of addressed.
Sorry, it's hard for me to pay attention asynchronously to chat as well, but it looks like we made some traction.
Surbhi Agarwal 01:01:57 I think he's suggesting separate AndroidX… like, separate modules for separate AndroidX versions.
Jason Plumb 01:02:05 Yeah, it's a little intense.
Surbhi Agarwal 01:02:07 Yeah, it would become…
Jason Plumb 01:02:10 Permutations get complicated.
Surbhi Agarwal 01:02:13 through that.
Jason Plumb 01:02:15 Cool.
Alright, well, thanks for the input, everyone.
Cesar Munoz 01:02:20 Thank you.
Jason Plumb 01:02:20 Yeah, I'll… I am here next week. Okay, good, okay, cool. See you then. And it is…
Cesar Munoz 01:02:26 Yeah.
Jason Plumb 01:02:26 Those who want to join, it is… A client SIG week. We have a short meeting right after this. If you want to join and talk about client concerns.
Bye.
Cesar Munoz 01:02:37 Bye, thank you.
