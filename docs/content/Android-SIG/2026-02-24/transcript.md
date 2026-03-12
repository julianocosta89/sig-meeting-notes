SIG: Android SIG
Date: 2026-02-24
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/glcVZqCO7_XOmj1AqvnY3t-sw4EaZ-NjCnZD2pWYDo5WjRUur1cLawrvYbjzySM.294fqUjYCgBQmchm
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:09 Hey, good morning.
**Jamie Lynch** 01:13 How's it going?
**Jason Plumb** 01:16 I haven't been awake very long.
It's going fine, though.
**Cesar Munoz** 01:26 Good morning, afternoon.
**Jason Plumb** 01:30 Hello, Cesar.
**Cesar Munoz** 01:33 a…
**Jason Plumb** 01:36 Mr. Like the Salad.
Which at least…
**Cesar Munoz** 01:41 like that, yeah.
**Jason Plumb** 01:42 which, at least in the States, we would say, Caesar.
**Cesar Munoz** 01:46 That's true.
That's what I… That's how I pronounce it in English as well, so it's fine.
**Jason Plumb** 01:55 Yeah.
**Cesar Munoz** 01:56 Still doesn't seem to be a common name in English, though, so that's why I had to follow with, like, the salad. Otherwise, people will… We don't get it quickly.
**Jason Plumb** 02:08 I know another Cesar here.
He's Mexican, but I, I mean, still…
**Cesar Munoz** 02:13 Yeah, that's it.
**Jason Plumb** 02:18 Alright, I can share… Seems like a good window.
Yeah. Okay, so I've front-loaded some topics. Please feel free to add stuff on there.
If you have stuff you want to talk about, Yeah, so this idea… the first thing to talk about this morning is this idea that came up originally Someone who wants… the… Android analog of the global OpenTelemetry instance, right? They're like, hey, I really just want to be able to grab the instance globally and do stuff with it.
And through some discussion, kind of presumably it's because they're building library instrumentation… sorry, they're building libraries that do their own instrumentation, or are OTEL native, right? They want to be able to do Android stuff, generate events, whatever, from these libraries.
And… I think our response was kind of like, well, you know, global's kind of an anti-pattern, putting… just sticking stuff willy-nilly and… static instances and poking at it later is maybe not the best approach to building software, but it's often convenient. You'd be better served by doing some dependency injection, and then I think after all of this.
I kind of floated this idea of a callback, or, like, a listener that you could register, and maybe we could use, like, the service locator pattern. We could, like, do… a service lookup of all the classes that implement this interface, and when the OpenTelemetry Rum instance is initialized, we could then pass that instance to any of these listeners.
So, if you were building a library, and you needed OpenTelemetry, you could have, you know.
you can have an implementation of some interface that would get called back, so… In Core Java, they have this thing called the… auto-configure… after auto-configure listener, it's not actually what it's called, but it's, you know, this was, like, floated a long time ago. And I think it's just called… Open… I think it's called OpenTelemetry Listener, or Auto Configure Listener? Let's see.
Yeah, this thing. So, auto-configure listener, and… if you're writing software and you need to get a handle on that, you can implement one of these, and like, if you're using the agent, it'll, you know, it'll do all that for you, and you'll get an instance. The… I guess one downside of this that I can think of right now is, immediately, is that if we want to support shutdown and reinitialization, you know, there's some stateful stuff that has to happen, and we… I don't know, do we… have to have the equivalent, like, shutdown side of this to let people know that they should no longer use that instance, or… you know, it adds some complexity that we haven't… I haven't thought through at all. So I'm just curious what people think about this idea.
**Cesar Munoz** 05:24 just to make sure I understand, is to provide a listener with the, with the hotel.
Instance that we created.
**Jason Plumb** 05:33 With the OpenTelemetry Rum instance, yes.
**Cesar Munoz** 05:36 Okay, the ROM… got it, it's not the, okay, I got confused, because the one that's in the example is the SDK implementation. Okay. Right. It will be the ROM, got it.
But isn't that something we already do? I think we had a listener.
**Jason Plumb** 05:54 We do, yeah, but it's not exposed in the agent, and it's something slightly different.
**Cesar Munoz** 06:02 Okay.
**Jason Plumb** 06:02 Let me find it. It's called… Oh, there's so many listeners, let's see.
I think it's on the OpenTelemetry Rum Builder, so I can go there, probably.
Oh yeah, so in thinking about this, this is what got me to, to do the PR recently that made this change.
to deprecate the SDK realistic, because the… we exposed the… Yeah, so this does not… the listener that we currently have, and what people are using, exposes the OpenTelemetry SDK and not the interface, so I deprecated that, went to the interface, but you still cannot get the OpenTelemetry RUM instance, which is the convenience kind of like our convenience API, which only really provides emit events right now, but we could add stuff to it later.
**Cesar Munoz** 07:07 Got it.
I think… I think this top… it's interesting, because I think this topic touches on other topics that we have for later.
In the agenda.
**Jason Plumb** 07:18 Yeah, I saw.
Yeah.
**Cesar Munoz** 07:20 So, regarding, okay, Especially the one regarding agent API, which is where we have the ROM interface.
**Jason Plumb** 07:31 Yeah.
**Cesar Munoz** 07:31 In the… in an issue that I created a while ago, and that I haven't been able to To go back to, which is this one, we were talking about, you know, how to enhance and, you know, avoid workarounds in the instrumentation API. And because of that, we ended up talking about what's needed in the ROM interface, And what's not needed there.
And… My general, like, to summarize it, my idea is that We probably don't want to add any kind of Ability for instrumentations to flush anything.
You know, directly, and also to shut things down.
So, actually, I think Hanson created a… a POC.
where… I think he removed the shutdown.
method from the… from the interface. So… If, I guess, we… agree on that, then the… probably the issue that you mentioned wouldn't be an issue, you know, because it's like.
unless I misunderstood, but I… if I understood correctly, one of the concerns is that if we provide them with this instance, they could shut it down.
And then that will kind of break everything else, or…
**Jason Plumb** 09:04 I don't think there's a sh… is there a shutdown on OpenTelemetry Roam?
I think there is. Let's find out. Let's find out.
**Cesar Munoz** 09:16 Yeah.
**Jason Plumb** 09:25 Yeah, that'd be nice to have that be internal, wouldn't it?
**Cesar Munoz** 09:36 I wouldn't be opposed to it.
**Jason Plumb** 09:37 Yeah, I mean, there hasn't.
**Cesar Munoz** 09:38 I didn't…
**Jason Plumb** 09:40 There has to be some entry point for shutting the thing down. I just… it's where does that live, and who should have access to it?
That… the concern I brought up earlier was not specifically about anyone who has an instance of this calling this, although that's a… that is maybe also a concern.
I was just more worried about listeners getting this instance and then holding onto it, right? Storing a reference of it.
creating and passing it to dependencies, and then after it's shut down, they have this old… this old version that they need to do something with, right? Or not. They need to… Yeah.
**Cesar Munoz** 10:16 Yeah.
Okay.
**Jason Plumb** 10:21 But one way to mitigate that is to… is to pass a wrapper, like a shutdownable wrapper, that then is just… when it's shut down, it just delegates to no ops, and, like, nothing happens. But then, you have to deal with this crap, you know?
Like, what do you do in that case?
This is an easy no-op, this is an easy no-op, but then if someone's getting the session ID, I guess we just… we have some default invalid session ID or something?
**Cesar Munoz** 10:50 I guess another, approach… Which, it's probably not gonna be popular.
But it's… it's an approach. Will be to provide some sort of… not necessarily specifically the Java-specific, you know, optional API, but something that kind of resembles that, so that when you called the getter to get the ROM instance.
You might get a null if it's already shut down.
Maybe that cooled.
But, you know, that's… I think it's kind of on the verge of… Been to be hacky, maybe?
So, I'm not sure about it.
Just throwing some… Ideas.
**Jason Plumb** 11:37 Yeah…
**Jamie Lynch** 11:39 It feels like, for a regular app.
I would expect… someone to basically take care of this by dependency injection. I think that would be the best approach.
So… you'd be using, like, a dependency injection framework, or something like… like, AndroidX startup library, which kind of… Deals with all of this and allows you to retrieve it from a central location later.
But I think you mentioned this was specifically for instrumenting a library?
**Jason Plumb** 12:16 I don't think that they were super clear on what their use case was, but I kind of assumed that that was… What they were looking for.
Like, you know, big companies have…
**Jamie Lynch** 12:28 Hmm.
**Jason Plumb** 12:29 internal teams that write reusable libraries, and if they want to be able to emit events or whatever across several different apps, then… Making it a requirement to pass the already created and initialized OpenTelemetry instance to the library upon library creation is kind of a big ask.
I think it is. Like, telling every library that wants to do OpenTelemetry instrumentation on Android that they need to take a dependency on OpenTelemetry, it's a little bit heavy-handed, I feel like.
**Jamie Lynch** 13:01 Yeah, bad.
**Jason Plumb** 13:04 Now, by dependency, I mean, like, a literal constructor dependency. I don't mean, like, a… like a Maven dependency.
But there's trade-offs, like everything. I don't know.
Okay, well, I think that we can probably kick this can down the road. I don't… I mean… We don't have a lot of… auto-configure to try and reuse the pattern that's in Java. We don't really have a lot of auto-configure It's all very manual right now, through the initializer or the OpenTelemetry Run Builder.
So I'm okay not… Going down that path right now.
**Cesar Munoz** 13:55 Yeah, probably we can wait until more.
I don't know, use cases?
**Jason Plumb** 14:00 I think so, I mean, there's no…
**Cesar Munoz** 14:02 It's complicated, because not only… Like, you will have to wrap it.
If that's an approach. But it's like, people can also store instant… store stuff that is inside the SDK, so they can store a trace Builder.
And then… It's inside the, you know, and then still has a… holds a reference, so… Even if it's swapped.
the OpenTelemetry instance, then you still have this, you know… it's quite messy.
to control that.
**Jason Plumb** 14:42 Yeah, it's almost like you're starting out.
Yeah, it's almost like there should be two methods, one that's like, here's your ready instance, and there's another method that's like, now your instance is invalid.
**Cesar Munoz** 14:52 Yeah, but it's… It doesn't sound right.
**Jason Plumb** 14:59 Yeah.
**Cesar Munoz** 14:59 Now, bear in mind that I think most of the issue that we have The potential issues with this is that it can be shut down.
the ROM instance.
Which, I think there is… there is value, and… It's been a while since we added it. I don't remember the use case, but I think somebody asked for it.
**Jason Plumb** 15:22 Yeah, I think it was Mustafa.
**Cesar Munoz** 15:26 I don't remember, but yeah, I think somebody asked for it, and I know… I think we added it because it's also present in the, in the Java… SDK implementation, so…
**Jason Plumb** 15:41 Well, we should revisit this damn thing. I forgot. Okay.
But I… yeah, I'm trying to find the original ask, let's see… Yeah, it was Mustafa. Okay, so this, this is the original ask.
So, in some cases, they just want to be able to shut it down.
Specifically, they have a span processor… That they want to reinitialize.
**Cesar Munoz** 16:11 So maybe, maybe we need a…
**Jason Plumb** 16:12 Yeah.
**Cesar Munoz** 16:13 Maybe we need an extra API layer, you know? It's like, the one with the shutdown is the one returned.
In the initializer, but then the one that we passed To instrumentations or other stuff, it doesn't have the shutdown.
Function available, things… maybe something like that.
**Jason Plumb** 16:32 Yeah, so you said that Hansen proposed this idea that shutdown should not be available to instrumentations?
Is that…
**Cesar Munoz** 16:39 I think that's what I remember, let me check the PR.
**Jason Plumb** 16:42 Okay.
**Jamie Lynch** 16:47 That feels reasonable from the perspective of someone who's, like, writing instrumentation, because I think… That kind of aligns with the behavior and the spec.
**Cesar Munoz** 16:58 Yeah, it's here.
**Jason Plumb** 17:00 But the app itself should be able to?
**Jamie Lynch** 17:07 Yeah.
**Cesar Munoz** 17:08 Whatever.
**Jamie Lynch** 17:09 But I think that…
**Cesar Munoz** 17:11 Based on what we already do, With the instrumentation context, Hmm… If we provide there only the plain OpenTelemetry API.
then probably we shouldn't worry about users, at least instrumentations, you know, calling shutdown.
**Jason Plumb** 17:41 Yeah.
Yeah, if the main thing that the agent is providing is a way to get the OpenTelemetry instance.
then you have to ask how much value the agent is providing. It's really only initializing the SDK And wiring up instrumentations.
which is maybe fine, but then there's… then there's kind of, like, no API surface. Because right now, the only real thing that it's providing is a way to get the SDK and to emit an event, and I guess also to shut it down.
**Cesar Munoz** 18:19 Yeah.
**Jason Plumb** 18:19 Yeah.
**Cesar Munoz** 18:24 Okay, that's fine. Regarding instrumentation, I was planning to continue That work this week.
I've been a bit busy the past couple of weeks, but… I'm gonna try to, gather all the information from the threads in… And, and this… PRs, example PRs, and see, you know, What ticks all the toxics?
All the boxes.
**Jason Plumb** 18:56 Okay, cool.
Yeah, I think as part of this is… I think I added this, like, immediately after. I was just thinking, like, I saw that, and I was like, you know, this is, like… This is the thing that people touch, that the users touch, and… It is something that is the main thing that's returned by the agent, and so we have this stable agent, but it's returning an unstable API.
So I think we should prioritize getting this in shape. Like, maybe… prioritizing this over the… I know it's related to, but maybe prioritizing stabilizing that before the instrumentation API?
**Cesar Munoz** 19:34 I think it's fine. One of the… I think Jamie mentioned something like this a while ago in Slack.
And… I commented there that, you know, because of the suggestions, To change the… ROM interface based on the instrumentation API thread.
I was wondering if we should wait until that's sorted before stabilizing these?
But… It's… well, it was mostly because I was thinking that maybe we will add like, a way for instrumentations to manually flush the data. But then, I think, based on the threat, I think that idea is discarded.
In favor of… Somehow making the, the ROM Builder, Make sure that, you know, when there's a crash or something, it will flush all the data.
So that instrumentation don't have to care about that.
And I think that makes a lot of sense, so I don't see any potential changes to the RAM API regarding the instrumentation API, so… I'm… I'm… I'm good too.
You know, stabilize it.
So…
**Jason Plumb** 20:54 Okay.
Go ahead.
**Jamie Lynch** 20:57 It's fine from my perspective as well. I think it's just one interface in that module.
**Jason Plumb** 21:08 And we think that we probably want to remove shutdown.
From that interface.
**Jamie Lynch** 21:16 Probably.
**Cesar Munoz** 21:17 at least I'm sure that We probably won't… don't want to pass it to instrumentations.
You know, the open sentiments are drum, instance.
At least on that… on that context, the shutdown here wouldn't be a problem.
You know, in the sense that, you know, an instrumentation will shut it down.
But then, if we are going to pass it somewhere else, then, yeah, the problem remains.
**Jason Plumb** 21:48 But is that… is that the… is that the only concern about passing this to instrumentation?
Is the shutdown method?
**Cesar Munoz** 22:00 That's my understanding.
**Jason Plumb** 22:02 Okay.
Because I think right now the… let me just revisit this, because it's not fresh in my brain, but the install… the… Isn't it called…
**Cesar Munoz** 22:13 Solution, yeah.
**Jason Plumb** 22:14 Yeah.
Okay, so this does not have the RUM, but doesn't the install method… where is that damn install method?
It's, like, in the… this one, maybe.
No I'm very much awake.
in here, right? Install?
Okay, the only thing it takes is the context. Okay, so then, right now, today, the OpenTelemetry ROM… Instance is not exposed to instrumentation already.
**Cesar Munoz** 22:49 Yeah, I think that's true. So, we wouldn't add it.
And… I think what we… yeah.
**Jason Plumb** 22:55 So, instrumentations today cannot call shutdown.
Which I think is fun.
I think there's a need for that.
**Cesar Munoz** 23:02 I think that the idea came… came up because of the threat in the instrumentation API changes.
That, you know, one of the ideas was to, you know, add more stuff here so that instrumentation will have more options from this instance.
But now that's scratched, so…
**Jason Plumb** 23:22 Okay.
**Cesar Munoz** 23:23 Yeah.
**Jason Plumb** 23:31 Okay, then maybe we can stabilize this, then. Like, if we're thinking about stabilizing this, is there any reason, I guess, not to?
Or is there additional work that we think would be impacted if we stick… let's say… can we stabilize this today? That's a hypothetical.
**Cesar Munoz** 23:50 I think we can. The only…
**Jamie Lynch** 23:52 Now that I look at it, the only thing…
**Cesar Munoz** 23:56 that I see is, Do you remember why we have a get prompt session ID that returns the current session and not Instead of providing the session, provider, right away.
**Jason Plumb** 24:15 So the value instead of the thing that provides the value?
**Cesar Munoz** 24:19 Yeah, I think… I'm saying this because probably one benefit of Providing the provider is that… Maybe a user will… will want to know when the session changes.
And that could be one way to get to that information via the provider.
**Jason Plumb** 24:39 There's a listener for that, for sure.
**Cesar Munoz** 24:42 Yeah, but they won't be able to get it just from the string, so…
**Jason Plumb** 24:47 If they poll this, like, if they call getRum session ID and it changes, they'll get the new ID. I'm not following your…
**Cesar Munoz** 24:55 Yeah, but, you know, they won't get notified when it changes. They will have to keep on…
**Jason Plumb** 25:01 pulling the value. Right, which is the purpose for the listener? Like, if there's… are you saying if instrumentation needs to be notified?
**Cesar Munoz** 25:09 No, the user. I mean, how will they attach to the listener? We have a listener, but how will they attach to it from the OpenTelemetry room?
I mean, we… because in my idea, this is all we… Give.
to our users. An instance of this.
**Jason Plumb** 25:27 So they can register… Session change listeners, I believe, when the agent is being created.
**Cesar Munoz** 25:36 Oh, you mean via the DSL?
**Jason Plumb** 25:38 I think so.
**Cesar Munoz** 25:39 Got it.
**Jason Plumb** 25:40 I mean, definitely, definitely via the builder, but I think it made it to the DSL.
It's not on the top of my head.
**Cesar Munoz** 25:47 Brawloop.
**Jason Plumb** 25:48 Yeah.
**Cesar Munoz** 25:50 Okay, yeah, no, that could be… I mean, as long as it's possible, I think it's fine.
**Jason Plumb** 25:59 But if not, it's also something that we can add, right? Even if it's not the.
**Cesar Munoz** 26:03 Yeah, true.
**Jason Plumb** 26:04 Yeah.
**Cesar Munoz** 26:05 Okay, so yeah.
**Jason Plumb** 26:07 People definitely care about this session… changing… I think I'm in the wrong place.
That's not what I meant to do.
I hate this double thing. Okay.
Yeah, maybe we don't have it exposed yet, but…
**Cesar Munoz** 26:39 No, but it's… it makes sense, we can add it.
**Jason Plumb** 26:41 Yeah.
**Cesar Munoz** 26:42 You know, anytime. So, yeah, that's another way to provide it.
Okay, cool.
Yeah, I don't have… Any objections?
**Jason Plumb** 26:54 Okay.
Jamie, stabilize… stabilize this interface?
**Jamie Lynch** 27:00 Let's do it.
**Jason Plumb** 27:02 Cool, okay.
That's an impossible word to spell about this.
Okay.
Sweet. So… pardon, I asked Hanson about this yesterday, so our last release that we did contains that, I think I'm missing a word from this. It's the Play Console or Play Services Console?
**Jamie Lynch** 27:30 Google Play.
**Cesar Munoz** 27:31 Google Play phone.
**Jamie Lynch** 27:32 so-and-so.
**Jason Plumb** 27:33 Jesus. Okay, Google…
**Cesar Munoz** 27:35 Every player console.
**Jamie Lynch** 27:36 play a console.
**Jason Plumb** 27:37 It's, it's Google Play Console.
**Jamie Lynch** 27:40 Google Play SDK console.
**Jason Plumb** 27:42 Oh my gosh, okay.
**Jamie Lynch** 27:43 to sync from Google Play Console.
**Jason Plumb** 27:46 Awesome. So we had support for that in our last release.
I asked… Hansen said he couldn't make it in the… when we were in the Kotlin SIG yesterday, he said he was gonna miss today, so I asked him, and he's like, yeah, it takes, like, at least a week for stuff… like, the account, I think, that they registered takes, like, a week to get set up, and it depends on the artifact being available for some amount of time.
So I think it's still in the cook-in, the bake-in phase, and we haven't really seen any… I don't think there's any data yet, is my point. But it'd be cool to, like, see one data point in there would be… Kinda cool.
Let's revisit this next one.
Okay, this is a good question and a good topic, because I feel like we should probably add this… maybe to contributing or something, but I think that we, like, at least the three of us, are probably not aligned on this topic.
**Cesar Munoz** 28:45 Yeah, it's a good point.
Jamie and I quickly… Discuss it.
Earlier today. Well, we just… You know, we're sharing some ideas, but yeah, nothing… So… what I was mentioning is that maybe… Maybe we could start with some rules based on the scope of the changes, so… If it's a version bump, Then, just any approval from anybody?
It's fine to merge it.
But if it's an API surface change.
And probably two maintainers' approvals, at least, should be needed.
And then the rest in between, we can… we can discuss.
**Jason Plumb** 29:34 Yeah.
**Cesar Munoz** 29:35 tips.
**Jason Plumb** 29:44 So, that's kind of where I'm coming from, is, like, a… a huge change, even if it has, like, a couple of approvals, I want to at least cook a little bit longer, allow other people to see it. Like, the… The only thing I try and be a little bit cautious about is, like, getting stuff in too fast before, like, especially with a large change, before other people have had a chance to comment on it.
**Jamie Lynch** 30:09 Huh.
**Jason Plumb** 30:15 Yeah, some sort.
**Jamie Lynch** 30:15 Oh, sorry, go on.
**Jason Plumb** 30:17 Yeah, I was gonna say that it's certainly not, a case where the person that submitted it is the one that needs to merge it. Like, any of us three can merge PRs, and I don't think it matters. Like, if I submit a PR, it's totally fine for you to merge it, and I think that's also true, like, if either of you have submitted a PR, and it's pretty chunky, but we've, like, talked about it and figured it out, I'm happy to merge it if it has the approvals, and no blocks.
**Jamie Lynch** 30:42 Hmm,
**Jason Plumb** 30:43 I think… I'm of the mind that anything that is… contentious. We should… Put a red, you know, change required on, because that sends a strong signal.
That we need to keep talking about it, but anything that has green checks… and no blocks, I think, is fair game to merge, but… there's this unstated, and I think that's what you're asking for in this, Jamie, is, like, the unstated, like, how long or when should we let stuff cook?
And… I mean, it's a good question. We… I know that some other repos in OpenTelemetry require two approvals.
And that kind of forces more eyes and more discussion.
But it also, like, very intentionally slows simple stuff down. So…
**Cesar Munoz** 31:29 Definitely. Yeah, I think two approvals for things like bumping versions is too much.
**Jason Plumb** 31:34 Yeah.
**Jamie Lynch** 31:35 Agreed.
**Cesar Munoz** 31:37 Maybe when you talk about alert… when you talk about alert changes, Large changes, sorry.
You mean large in the sense of… API surface-level changes that are big, or… you know.
changing a Java code to Kotlin, which might seem large.
In surface, you know.
**Jason Plumb** 32:02 Yeah, I mostly mean… I mostly don't mean lines of code, I mostly mean impact, and potential…
**Cesar Munoz** 32:09 Yeah, totally.
**Jason Plumb** 32:09 Potential for mistakes, or potential for problems being introduced?
**Cesar Munoz** 32:16 So maybe we can define some… Tier levels of changes.
And I will say… and we can… you know.
Iterate on the… on those, you know, as needed.
I mean, it probably doesn't have to be perfect right off the gate.
But I will say that the top-level tier of importance for changes will be an API surface change.
Which, maybe we can say, okay, for the top-level tier.
We require 2 approvals, and at least 48 hours.
They are open, just in case.
**Jason Plumb** 33:02 When you're saying top level, do you mean specifically the agent?
**Cesar Munoz** 33:06 No, I mean, the… The, the, the, the priority level.
**Jason Plumb** 33:13 Okay.
**Cesar Munoz** 33:13 Which is based on the impact of the change, which To me, right now, the only top impactful change will be the API surface.
**Jason Plumb** 33:27 the stable API surface.
Or any of it. Probably any of it, right? Because we want to be.
**Cesar Munoz** 33:33 stable.
**Jason Plumb** 33:33 by default?
**Cesar Munoz** 33:36 Yeah.
**Jason Plumb** 33:37 Yeah.
Yeah, I wish I'm not awake enough yet to have a good way to phrase this. Like, I feel like we should have it written down, and I feel like this will come up again.
If we don't write it down…
**Jamie Lynch** 34:00 Yeah, I'd be happy to try and summarize this and put it in the README or Contributing file somewhere, and… Yeah, I'm also happy to keep it a little ambiguous until we need to revisit it, I think.
If it changes.
Fairly complicated, then it makes sense to wait a couple of days, even if it's got a couple of reviews.
**Jason Plumb** 34:28 Yeah. Okay, I mean, I appreciate you offering to do that. I think, I want to just look at, like, for instance, because I know that there's a couple out here that are fairly big, that were just, like… like, I think… this one, I think, is a good example of this. So, it's relatively large, it doesn't touch very many files, it's clearly just a, you know, augmented Kotlin switchover, and it's been approved 4 days ago, so clear, like.
like, Jamie wants to push the merge button on this, right? Like, I assume that that's the case. He's like, I did the stupid Kotlin refactor, it got approved, someone else has looked at it. I think… I personally think that this is fair game to merge, right? Because Cesar's looked at it. So, two maintainers worked on this.
you did the work, Cesar approved it, I think it's good to go. I haven't had a chance to look at it yet. I'm also not… super inclined to go… like, when I see an approval, me, as a maintainer, if I see an approval from another maintainer, I'm just gonna give it a quick look. I'm probably not gonna go line by line.
**Cesar Munoz** 35:35 And it's also not changing the API surface, so…
**Jason Plumb** 35:40 Right. You know, it's kind of like… Exactly. It's down in the instrumentation, that's fine.
**Jamie Lynch** 35:45 But is there another one that maybe…
**Jason Plumb** 35:49 Is a different example of this, like… Is there a… can you do it by reviews? Can you do it approved? Yeah.
So, like, here's one. It's been out here for a minute. It's approved, right? So this bumps the minimum support, but does it build? Is it broken?
**Jamie Lynch** 36:18 Yeah, not quite yet, I think.
That's waiting on… CodeQL to release an update.
**Jason Plumb** 36:26 Oh yeah, okay, so this one is not… well, it's broken down anyway, but it is mergeable because we have an approval on it.
Right? So this is where… this is where it gets complicated. Like, I think the three of us look at this and know… probably don't want to click this button, and I mean, it won't merge, because we're waiting a code QL.
But this is fairly, also, like, fairly impactful, I think, right?
**Jamie Lynch** 36:51 Hmm.
**Jason Plumb** 36:54 I don't know how to… I don't know how to summarize that.
In an eloquent way right now, but… Yeah, there's only these that are approved anyway, but, like, maybe this one?
**Jamie Lynch** 37:08 Yeah, that's probably a good example, because it touches the instrumentation API.
**Jason Plumb** 37:14 Yeah, so the loader is being moved out of the instrumentation. I don't even think I've looked at this, to be honest, have I? Oh, I have. Okay, it's just been weeks. Okay.
But it's approved.
So, and I know.
**Cesar Munoz** 37:29 Yeah, I agree.
**Jason Plumb** 37:30 And I didn't put a block on it, right?
**Cesar Munoz** 37:33 if… if I remember correctly, this does change the, public service API. API surface. So… I think it's been a couple of weeks since I took a look at it, but…
**Jason Plumb** 37:50 It impacts.
**Cesar Munoz** 37:50 That's people right.
**Jason Plumb** 37:51 Writing instrumentation, doesn't it?
**Cesar Munoz** 37:56 I think so… It's been a while.
**Jason Plumb** 37:59 This… this… oh, that's the impulse. Wait, where's the… This is the public interface for instrumentation.
And… that's not a change.
**Jamie Lynch** 38:15 Yeah, I think initially there was a change on this. So… I guess.
Using that as an initial example, it would have been good.
to… Wait, poor.
Approval from everyone, basically.
**Jason Plumb** 38:34 Yeah, or at least to have some additional eyes on it, because it's an interface change, yeah. I think that's… I think that's good.
Did Cesar, or did I catch that one, or did we talk about it? I honestly don't remember.
**Jamie Lynch** 38:52 I think it's got, like, one approval, and then there's one comment left over. Yeah. Yeah.
**Jason Plumb** 39:02 Okay, I can, I can take the hint.
**Jamie Lynch** 39:07 Thank you.
**Jason Plumb** 39:08 Yeah, no, it's a, it's… this is a good example, though.
Yeah, cool. I think… I think the fact that I looked at it and commented on it after the comment, it's worth me coming back and also putting a green check on.
So… Cool.
David, what are you working on?
You got any… you got anything fun Android-related that's happening in your world?
**DavidGrath** 39:41 No, that's obvious.
There you go, Vince.
**Jason Plumb** 39:48 That sounded completely garbled to me, and I couldn't make sense of any of it, I apologize.
**DavidGrath** 39:53 Okay, let me try and change audio sources.
**Jason Plumb** 39:58 Still pretty muffled. I couldn't get it.
But it's cool. I didn't mean to call you out, I'm not, like… I'm just…
**DavidGrath** 40:07 Because he's go for it.
**Jason Plumb** 40:11 Cool. Anyway, if you have anything, feel free to add it to the agenda. I think we're about out of topics, and I just wanted to give you an opportunity to bring anything up if you wanted to.
**DavidGrath** 40:23 Oh, no.
Yeah, I don't know.
**Jason Plumb** 40:29 Cool.
**Cesar Munoz** 40:31 So, just to… before we move on, just to make sure, then, I think we agree we should add something to the repo, mentioning this.
What we should do in each case.
if I understood correctly, Jamie, you wanted to take a look… okay, got it. That's fine, I just wanted to confirm, otherwise I was gonna… I was gonna do something, but it… but it's better if… If you… if you take a look. Thank you.
Okay.
**Jason Plumb** 41:08 Cool.
Alright, well, that's exciting stuff, and, I can probably do a PR for this.
And that'll be an incremental step forward.
On stability, at least.
Cool.
**Cesar Munoz** 41:33 Nice.
**Jason Plumb** 41:34 Well, we ended a little bit early.
Which is not always the case.
**Cesar Munoz** 41:41 Yeah, but it's good. Yeah. From time to time.
**Jason Plumb** 41:44 It is.
Have a great rest of your day.
**Cesar Munoz** 41:48 You too. Thank you.
**Jason Plumb** 41:49 Yeah.
**Cesar Munoz** 41:50 Talk to you later.
**Jason Plumb** 41:51 Bye.
