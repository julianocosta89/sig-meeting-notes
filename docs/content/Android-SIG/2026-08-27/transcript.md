SIG: Android SIG
Date: 2026-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:28 Hey, good morning.
**Jamie Lynch** 01:32 Yeah.
**Vishwan aranha** 01:32 Morning, guys.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:34 Mine does.
**Jason Plumb** 01:49 It's 8 AM, it's everyone's favorite time of day.
**Cesar** 01:56 Good morning.
**Jason Plumb** 01:58 Hey, good morning. I'm getting set up here.
Cool, light agenda today. Please add any agenda items that you have to the doc.
Let's give it one more minute.
**Hanson Ho** 02:47 Hello.
**Jason Plumb** 02:51 Hey, Hanson.
**Cesar** 02:52 8.
**Jason Plumb** 03:07 So before we get started, Ben, did you see my comment about that… super stupid Tomil escaping thing that you commented on?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:17 Yeah, I saw that. Oh, man.
**Jason Plumb** 03:20 This is the time where you can say told you so.
Anyway, glad we got that worked out.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:30 I think co-pilot.
**Jason Plumb** 03:32 Yeah, we'll call my… Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:34 on the second PR also, Copilot was insisting that you, you know, add their skates.
**Jason Plumb** 03:39 I know. I'm like, whatever.
**Hanson Ho** 03:46 Was there a PR that this manifested in that… Provides hilarity.
**Jason Plumb** 03:52 It was simply, like, adding a URL to the Lychee exclusions, so that that doesn't fail.
And Copilot's like, oh, these dots in the URL, like, in the host name.
It's a regex, so those will, like, match any character, you should probably escape them, and I'm like, fine. And it's… I think it even suggested the escaping.
Which then breaks because it's supposed to be, like, a double slash instead of a single slash, so it… it made it worse.
Good time.
But more to the point, Ben was like, I don't think we need that. And I'm like, Copilot says we need it, and I think we should just do it. And then it broke, because it made it worse.
Alright.
Visible Stream Tracker.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:44 Yeah, I just put this on the agenda because, like, I think earlier we decided we'll go back to this. We were debating the concept of What a screen is. How do we want to update the attribute based on the navigation instrumentation that we did?
So we added separate events board.
desk, like.
navigation complete, and then we would, add the attribute, navigationDestination.name, I think. So that… Now, these are two parallel, different things. One is tied to the activity of the fragment, which files on lifecycle events, and then you have independent, composed navigation, or, like, navigation in general, right?
And somebody, I think, I did not update the issue after that. We were gonna discuss it.
And I think somebody picked it up, and, like, I just wanted to give them the right direction, if they are working on it, and, like, I think it would be a good time to, you know, revisit that discussion on how we want to proceed here.
**Jason Plumb** 05:53 Is it this issue? This 1920?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 05:56 Yeah, I think that's the original issue where I did the work on Compose navigation.
So… so there we added the new event, which is in the unreleased version, I think.
Right. Yeah.
So now we have a new, event, which is tied to the navigation scope.
Right. Firing independently of the lifecycle scope, and so, say if you were to track navigation, a user navigating through the app.
you have two different kinds of events. And then… to top it all, like, there is this, visible screen tracker, span processor, and log processor, which would add this additional attribute, current screen, to every log and span, based on, just on the activity lifecycle. So it… even if you have a single activity app.
You would have, like, different events fired for the navigation, but you'd still see the current screen as the main activity, or the only activity.
So, do we want to update that behavior?
how should we do that? Like, can we type both of these navigation, or, you know, the combo screen versus activity? Do we want to keep those separate?
Should we maybe add an additional attribute to the visible screen tracker, saying this is the screen, this is the activity?
Yeah, because these are currently… Duplicated, sort of.
**Jason Plumb** 07:31 Yep.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:32 I think Hanson had, like, pretty strong opinions on that.
**Hanson Ho** 07:37 Yeah, so I think… there are two things that we need to be considerate of, doing what's correct and not breaking existing behavior. I think the existing screen tracker stuff, basically conflates activity and fragment with screen.
And given what we have for Compose, and other navigation, Compose 2, NAV2, and NAV3 destinations, the conflation becomes a problem, because you're basically gonna have one activity navigation, one visible screen update, and nothing else if you're doing pure composed navigation.
So I think the old, implementation is, should be deprecated and replaced by one that is aware of, something higher level, than simply activity and fragment loading, which includes the composed navigation events.
I think luck… luckily, I don't know what, attribute names are used by the destination… by the… the attribute, by the, the SPAT… was it… do we put it in the span processor, in the log processor? Is that the mechanism for getting, the activity, or the… Yes. Okay, so I don't know what attribute names they use.
I'm hoping they…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:06 Screen.name,
**Hanson Ho** 09:08 Perfect, perfect. Because that's not going to be the new, semantic convention name. It's probably going to be app.screen.whatever.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:16 I think we, yeah, sorry, screen.name was the older one. I think we migrated it to app.screen.name.
**Hanson Ho** 09:22 Oh, did we? Fuck.
So…
**Jason Plumb** 09:29 So let me respond to the… this idea. So, only because I know a little bit of the history. Absolutely, the activity and fragment instrumentation conflate the notion of screen, and they… Had no awareness of Compose at all.
like, when it was first written, Compose was not even a target for… this kind of stuff. I still think there's merit in tracking what activity you're on, what fragment you're on.
But we shouldn't call those screen. I would suggest… I would like to see us, rather than just deprecating those instrumentations, just let them do what's printed on the tin, and that is track the current activity, track the current fragment.
And have those be available through events.
Optionally with some sort of tracker that's putting it on, every… Spanner log, I suppose that's also possible, I don't know how desirable it is.
But they shouldn't necessarily be responsible for… Tracking the screen.
But I think it's also pretty complicated, because there are some simple apps that just, like.
Have a couple of fragments and a couple of activities, and that's it, right?
And that's enough for some users to determine what their screen is, but I agree that there needs to be a high-level abstraction that Compose feeds into, that Activities and Fragments can feed into, that maybe even has, like, user overloads, so some sort of API that both instrumentations and users Can leverage to… Set or check the current… current screen.
**Hanson Ho** 11:12 So… to modify the existing instrumentation to do what it actually does, which is record activity, current activity and current fragment. That is probably going to involve changing the, attribute names again. I think doing that will basically leave that as… as what it is, and then we could basically build the screen stuff, alongside that, so folks could choose to, to, to use one, or use the other, or use both, and get… and get effectively both things.
Does that sound reasonable?
**Jason Plumb** 11:49 It does. I'm wondering if the intent of the visible screen tracker was kind of supposed to be this abstraction.
And it's just not in the correct shape for us yet.
**Hanson Ho** 12:01 Well, yeah, that… I mean, that's why I… That's why I kind of want… So, you could make a visible screen tracker that does both, respect activity lifecycle and, the composed navigation destinations. Then we have to basically create an abstraction that says these are navigation events, and then, you know.
handle them as they are, and if you don't get any, you know, destination firing, the activities, moving about the activities should create enough vents to basically allow you to track the screen.
But that would mean deprecation says this is… this is the one end-all be-all, or, you know, the single tracker that does everything.
That single tracker should do everything, but, I think you're not wrong to just rename the existing one and have it as, like, a simpler instrumentation, that, you know, does this… tracking, but does what it actually does, which is tracks activities and fragments, and uses attributes like that. And then they can live side by side, if they want, if people want, even though the utility isn't, you know, Is it really there to use both, if you already have the eventual screen tracker that respects destinations?
**Cesar** 13:22 I remember we discussed this a couple of SIG meetings ago.
And I think we're kind of… we're landing on a similar conclusion, and… One of the things that I remember from then was… is that I think Visible Screen Tracker might be a nice… place.
to… put a manual API for users to define where When they have a screen.
It's just that right now, visible screen tracker.
is aware, as far as I remember, I haven't checked today, but… I think it's aware of… activity and fragment lifecycle stuff, so… If we remove that, Stuff.
And probably just leave the two strings and some setters.
When something changes, I think it would be a nice first API. I mean, users can call manually.
And then we can have, in each instrumentation.
Whatever tracker is needed, either an activity tracker or fragment tracker for, you know, those specific new events that we're talking about.
That's an idea.
**Hanson Ho** 14:51 Yeah, right now, this is directly implementing the, lifecycle services, right? Or life cycle, activity lifecycle, or, sorry, not activity, the life cycle, events. So, it is explicitly tied to resume and…
**Cesar** 15:11 Yeah.
**Jason Plumb** 15:13 It is, yeah.
**Hanson Ho** 15:15 So… I think changing the name of this… Is the easiest way of preserving existing implementation, and then start from scratch, where we do have a more nuanced and different, you know, system-aware screen tracker, that actually is… visible screen rather than, you know, life cycle.
**Jason Plumb** 15:45 Yeah.
**Hanson Ho** 15:46 Owners.
**Jason Plumb** 15:47 Unfortunately, it is internal, so we can change it.
Right? Like, users should not be depending on this class.
**Cesar** 15:56 Oh, which is… which is even better, right?
**Jason Plumb** 15:58 Yeah.
**Hanson Ho** 15:59 And the… and the API is actually quite tricky here, because it… the API makes it… makes the onus on the app developer, and whenever that happens, things could be incorrect. The magic of this is that it just works automatically as the app navigates. So, if we were to kind of bust things out into a real, like, you know, visible screen tracker 2 interface, how the automatic interacts with the manual should be very carefully, configured. If not.
having the manual simply be an event firear, and have the guts that do the update, do the processing.
So…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 16:58 Why do you think we need a manual API? Is that… is that, can we not, you know, tie this to the, instrumentation that we have built today? Say, for wire it into Compose Navigation, for example, and then not… not let the user manage that. I think that, yeah, that can lead to more no, unpredictable… transitions, then, like, it would actually help. They would have to… take care of it in every screen. There might be something that's left over from a previous screen and, like, not updated. So I… my preference is to update this ourselves, like, as an SDK, rather than Let the user do the work, which… which would be more, like, I think we.
**Cesar** 17:47 Error a problem.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 17:48 has… yeah, airplan, definitely. We have the, you know, option to do something here, so if so, then why would we want to put that responsibility on the user?
**Cesar** 18:02 I think it's a good question, and I… I have an opinion on that.
Which is that… There is no single way in Android apps to define a screen.
So… There is no bulletproof way that we can ensure that we know What a user will call a screen.
So because of that, I mean, we can create an automatic instrumentation that Probably covers, what you say, something like… Compose navigation events, and trade that as, screen transition.
And… That instrumentation might… Be nice for a lot of people.
But… For those who are not using that mechanism, then it doesn't work.
And… or maybe if they have a mixture of composed screens and then some old activities, things like that also can happen.
So… I, I… it is a risk of user… Error-prong stuff.
But in the end, I think with things like this that we cannot 100% be sure about, I think they need an FBI so that We don't have to at least initially cover them all.
And we can just tell the users, okay, well, if you don't… if it doesn't… if this… I mean, we can provide both. Let's say… and the automatic one can call the manual one.
So it will be all a single flow, still.
And then we can tell users, well, if this automatic one doesn't work for you, it's fine, you still have the manual API, and that can help you cover the other cases. So that would be… My reasoning behind it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 19:57 That, that makes sense, but, so how do you see this implemented? Like, my concern is, like, if it's manual, can… can that, say, somebody navigates to a… A navigation destination, and then we update it in the screen tracker.
And then, like, within that screen, maybe they are, you know, with that Compose destination, they are changing something, and they want to call this in a sec… like, as a separate screen, and they call the manual API. But then when they navigate back from that old destination to a different destination.
can the auto-instrumentation, update the screen, rather than having to rely on the user again updating the screen? So, if it works in conjunction, like, say, okay, you already arrived at the screen, and then you, the user manually wants to update the screen as, like, okay, within this station, I navigated to something else.
But, like, we can also, track the auto-instrumentation so that, like, rest of the things come free.
Anything that's not covered under activity lifecycle or Navigation, navigational instrumentation, just that the user has to manually instrument. Does that… Does that model work?
**Cesar** 21:07 Yeah, I think especially if the automatic instrumentation also uses the manual API, you know.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 21:14 Oh, Yeah, in that sense, I definitely agree, like, a manual API. My concern is that, like.
I don't want a user implementing this to have to manually, you know, register the screen.
in each of the scenarios, like, if for certain users, all of this can come, out of the box for free, that's a great way to, you know, get them to instrument using this. If they have to manually do it, I think that's, like, additional work.
**Hanson Ho** 21:47 I think… I think there are valid manual use cases. If the UI, you know, like, Jason talked about, there's one, you know, activity that loads a web view, and the web view, depending on what the web view does, it… it may or may not be considered a screen.
I think the trick is having the auto work in conjunction with the manual, because the auto has to do a lot of things to make sure things are correct, like coming back from background, like, the navigation between activities and compose, and making sure, you know.
the correct thing is being surfaced. When you have a manual in there that says, hey, I'm actually this, and making sure the user does everything correctly, to respect and be integrated in the lifecycle, that's where the hard part comes. So it's almost like… The manual should work, but only with either no auto or a limited amount of auto. Once you're doing stuff like, trying to balance, you know, activity navigation and composed destination loading, and background foregrounding, it becomes tricky if you introduce, like, a a randomness in there, that you can't really draw a state machine and be like, doo-do-do-do, this is where the arrows go.
So… I almost think, conceptually, there needs to be a manual way, but how deeply does it integrate with the auto? That is the part that we need to be really careful about. It's almost like, if you use manual, you are taking on a lot of responsibility. If you screw up.
You better know what you're doing.
And have that very clear about where the boundaries of manual and auto come, because it's just not… if you just toss manual randomly, it's going to make auto really, really difficult to deal with the edge cases. But if we can have a sticker that says, hey, if you do manual, you're going to be, you know, limited to this with auto, or whatever.
**Cesar** 23:55 Yeah.
**Hanson Ho** 23:56 manual's almost like a harder use case. It's almost like we should do the auto first, get that completely working, and then on top of it, think about how we could integrate some sort of manual, whether it's annotations, whether it's manual API calls, whatever, to basically allow an aspect of override.
**Cesar** 24:18 When I talk about manual, I talk about API.
And that can translate to anything, like, that can translate to an automatic instrumentation using that API.
And then also an annotation processor using that API as well.
So, for me, the manual, it's… it's really the one Source of truth.
And then… We can decide what to do with it next.
And users, you know, We can probably put a warning there. Can also use it as well.
I've never been, like… Like, I know we have to make things as easy as possible and as correct by default as possible.
But I'm also… I also don't like the other stream where we have to babysit users.
Like, if they make a mistake, Like, it's on them.
If we provide them with automatic instrumentations that already covered the most common use cases, let's say that we think that everybody should be using composables and compose transition… transactions… transitions, sorry.
And… and they don't… because they don't want to, or because, you know, they can't.
I mean, that's… that's… that's up to them. It's like… Maybe in the future, if enough, demand.
Arises, you know, saying.
Things like… well, I also… that, like, my app mostly uses fragments for, for screens, and I want them to… to be represented, like, maybe with annotations in the fragment, and I don't want the composed transaction stuff. Maybe we can, in that case, create an annotation for those cases, or maybe an automatic instrumentation that Covers Fragments out of the box, which probably won't work.
But… I will say that, you know, What you say makes sense.
Well, it seems like you're describing an issue that we still don't have, so… so I wouldn't… Like, over-optimize it yet.
And, probably we'll just skip things like, you know, there's a manual API, and there's this instrumentation that we believe is what everybody should be using, that uses that manual API.
Let's see what happens.
**Jason Plumb** 26:58 So, I want to try and summarize. We're about halfway through the meeting today. I want to try and summarize what we've covered for this topic.
I think none of us love the way that screen… screen handling is happening today. I think that's what I'm hearing.
we're burdened a little bit by some history here. We think that we have an opportunity to make that much better. And by better, meaning… handle Compose, like, provide an API or a way for ComposeNav not to just generate the events, but also to participate in this concept of the current screen.
We probably will need a new component, or several.
maybe it's simply called Screen Tracker, and we deprecate the old one, but we're gonna need something new. And we will probably… Change the behavior, or at least the telemetry created by the activity and fragment instrumentations.
Who may also participate in… Tracking of whatever screen is active.
But we'll probably not, we'll probably be tailored more toward their lifecycle stuff, which is what they do anyway. So… Hopefully, I… did I miss anything in the summary there?
Okay, if I didn't… if I did chime in, if I didn't… then let's talk about these two things, because I think these are relevant, right? So it… when it comes to Compose.
There was one idea here about… Oh, I have to take this phone call, sorry. Talk amongst yourselves.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 28:37 Yeah.
**Hanson Ho** 28:37 That was an example.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 28:39 Yeah, I think, Embrace, or… I was looking at some other implementations, I think you guys have it, like, This is the approach I saw, like, so my original idea was to, like, conflate, like, activity, prepman, and compose into one, single screen attribute, and how we can, like, Hanson mentioned, like, there are, like, cycle complexities, like the race conditions.
Amongst, different lifecycle callbacks, that would be problematic, but I was thinking.
If it's for the same activity or fragment, and then, like, we always have a clear winner, where if we have certain whitelists, like… So, for this activity, we always prefer the activity as the, screen attribute, but if it's within a, you know, some main activity that usually has a bunch of compose, transitions or navigations, then in that case, we would, like, we could maintain two different, you know, components, like one for the activity environment, or the other for, Compose, and we pick and choose the winner based on, what Based on a whitelist, or a blacklist, or something like that.
That, that was the idea, if that makes sense, like… if we… again, I think this comes back to, do we want to maintain one single attribute? I think that's one thing we first need to discuss, like, are we okay to modify the existing attribute's behavior to include composed?
if we… if we want to create something new, do we want to include Activity and fragment into that? And then, then I think rest of the… how we do it can be answered, I think.
**Hanson Ho** 30:22 So one easy way of solving this is not to use the word screen, and just report what we're actually doing, which is, a composed destination is loaded, an activity, the current activity has loaded, and basically have, you know, a set of different, implementation-dependent notions of what's on, quote-unquote, the screen. Hanson…
**Jason Plumb** 30:46 The problem I have with this, I totally hear where you're coming from, the problem I have with it, though, is you can't tell that to a product manager who's looking at a RUM screen. Like, they want to know… they want to know what screen the user was on when something happened, right?
**Hanson Ho** 30:58 I, I, I completely agree, so that… I'm setting that up by saying, you know, a straw man that basically, this is what we can do. But then the implication is that, like, so what's my screen? And it depends on your implementation. You use this if you… no PM's gonna buy it. Right. So having that difference under the hood, I think, is necessary for everything to work together, but ultimately.
We need to bubble one thing up, and that is… what thing am I looking at?
And, whether it's an automatic API, manual API, there is only one, unfortunately, concept, whether we call it screen, whether we call it whatever. And don't even start when we're talking about multiple activities on the same screen, which is possible for cars and… tablets and things like that. So the notion of screen is an abstraction. How you produce that screen is implementation-specific. So I strongly believe that eventually we need to bubble up one thing. Call it a screen, call it a page, call it whatever, but it is the single concept.
**Cesar** 32:08 Yeah, I agree.
And, and it's why I think manual API is needed.
Because we can't ensure that we can bubble up Always the right thing.
Automatically, so… Although we can provide an automatic, you know, convenience instrumentation, just for… Composables, because let's say that's the official current way of defining screens.
So…
**Jason Plumb** 32:41 Okay, I put another line item here, which is just, like, I think whatever we end up coming up with, I think we just need to, take care not to break the existing behavior, unfortunately, until we hit 2.0. So we're gonna have to have… Some amount of compatibility there.
**Cesar** 32:58 will…
**Jason Plumb** 32:59 Instrumentation is not stable, I respect that.
**Cesar** 33:01 It's not stable.
**Jason Plumb** 33:03 But…
**Cesar** 33:03 say that. You're right, you wrote my mind.
**Jason Plumb** 33:06 Right now.
**Cesar** 33:07 We've worked together.
**Jason Plumb** 33:08 there for a couple of years now, Cesar.
**Cesar** 33:11 Yeah.
**Jason Plumb** 33:13 But we should do our best not to break users, so… If there's a path to allow the current stuff to behave like it wants to, at least until we hit 2.0, Which I think will happen this year.
I think we should probably do that this year.
I think we should try not to break the existing.
And this is in keeping with OpenTelemetry's stable by default, which… You know, is… Probably intended to be… bent. That rule's intended to be bent sometimes, but… We want to do our best. We want to be good citizens, we don't want to have a ton of thrash.
And users that are currently expecting the visible screen tracker to be putting their activity stuff in every span?
Should be able to continue getting that without too much effort.
Until we… Right. Until we made your bump.
**Cesar** 34:11 But, like… This is probably a separate topic, which is probably related to what Jamie Jamie added, but… but… like… to me, if I use an artifact that is marked as alpha.
I don't expect… like, I'm fine if it breaks, like… I'm expecting that. I'm expecting that, unless… there is something in the README or something that mentions that it's… that that's not gonna change, but… That's… I mean, I understand your point, that these instrumentations have been there for a while, so there's probably somebody using them.
So, it wouldn't be nice to break that. But, but then…
**Jason Plumb** 34:57 Also…
**Cesar** 34:57 concern.
**Jason Plumb** 34:59 I just want to say that.
**Cesar** 34:59 California.
**Jason Plumb** 35:00 Those are hidden when you use the agent, because the agent includes those alpha artifacts, right? By default.
And so that's… the fact that you're using alpha is a little bit hidden.
To some users.
**Cesar** 35:11 Oh, I forgot.
I forgot we were… oh, yeah, then that's… that's… then… then there's no… yeah, then you're right. It's… it's not… In this case, yeah, because we added as part of a stable stuff, yeah.
**Jason Plumb** 35:25 We have that same challenge in OpenTelemetry Java instrumentation, because I think virtually none of the instrumentations are stable, but everyone's using the agent, right? And so you're just… you're getting…
**Cesar** 35:38 Ryan.
**Jason Plumb** 35:39 Tons of alpha, like, artifacts that are not declared stable.
**Cesar** 35:45 Got it.
**Hanson Ho** 35:46 So, how do we do the… I mean, if we want to move on from, from,
**Jason Plumb** 35:50 I think we need to, but… Okay, yep.
So, Ben, good discussion. I don't know that we left you with, like, concrete takeaways for this. Maybe more uncertainty than when we started, but at least, I think.
**Hanson Ho** 36:03 We can continue on the, on the, on the, on the, on the GitHub issue, I think.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 36:09 Okay, just… I'll take 30 seconds to summarize. So we… we would like to have, something that tells us what the user is looking at. So that's, I think, agreed upon. We don't want to break the existing, whatever, attribute and what its behavior is.
We would like to have a manual API, to, you know, fit this, whatever we are looking at, because the auto-instrumentation probably cannot do a good job. I think this much is an agreement. I think, like, next is, like, how we… do this, I think, like, that we can probably discuss, in the thread, but just want to make sure.
This is how I understood it.
**Jason Plumb** 36:49 I think I'm aligned with that. There's still a little contention around the manual API, but I think it's… I think it's good.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 36:55 Okay, sounds good. Thanks.
**Jason Plumb** 36:57 Yeah.
Okay, next topic. Jamie.
**Jamie Lynch** 37:02 Yeah, continue on with stabilization stuff. Yeah. So… Yeah, I think… I can't remember where we left off with this, but it feels like it's been a while since we've discussed it, so… Yeah, I just wondered what folks think, like, should those modules be our next target? Do we need to… Go into more detail about what needs to be done for them.
**Jason Plumb** 37:37 We do.
**Cesar** 37:38 the tree that…
**Jason Plumb** 37:40 Yeah.
**Cesar** 37:40 I'm home in court.
**Jason Plumb** 37:41 Common Core and Services, and what's not on here is the individual instrumentations, right?
**Jamie Lynch** 37:46 Jesus.
**Jason Plumb** 37:47 Whole other category.
But these three are really… I think these are the next targets, do we agree?
**Cesar** 37:54 Yeah, well, kind of… the thing is I common… we've been trying to clean it up, and I think… Ideally, for some point, we should get rid of it.
And at the end of the day, it's really just an internal tool.
So… I'm not… I'm not… comfortable about stabilizing internal tools.
You can run.
**Jason Plumb** 38:23 So, even though this is mostly internal, there's one thing that's not internal, and that's constants.
Which is only the logging tag, which… really, users shouldn't need, right?
So everything else in this module is internal, then?
If we gloss over that… And… helpers… Some network stuff… And what's in here? Not much. So yeah, we've cleaned this up a lot.
I don't have a good mental model of what… what's left on maybe continuing to shrink common.
But that's a target that people could work on for sure.
**Cesar** 39:15 I think we had an issue for that.
**Jason Plumb** 39:17 for common.
**Cesar** 39:21 Probably not well redacted or titled, but yeah.
**Jason Plumb** 39:26 one, yeah.
**Jamie Lynch** 39:39 I'm pretty happy to, like, create more issues for, like, these individual modules, and… kind of flesh them out a bit with ideas of what we could do.
I think that feels like it would be a good first step, although we can spend time looking at them.
Now, if people wanted to.
**Cesar** 40:04 Sounds cute, maybe we can have a single label for all of them.
like… stabilization.
**Jason Plumb** 40:14 Like this one.
**Cesar** 40:17 Oh, there you go.
**Jason Plumb** 40:20 I love labels, I make labels, I use them.
They're handy.
Yeah, I think the consensus on Common is maybe we can shrink it and it goes away.
Core, let's… Push that on the stack for a second and talk about services.
So, if I remember correctly, services is intended to be An additional abstraction between… Our instrumentation and the hardware.
So that we don't… like, the.
**Cesar** 40:55 Yeah, well, the Andre SDK, yeah.
**Jason Plumb** 40:57 Yeah, the platform.
So… Right, so stuff like… It's so funny, there's all that network stuff that's in common as well.
**Jamie Lynch** 41:10 Yeah, I think… from… From what I remember, when I worked on this module last, we were breaking it apart, because, it was… Mainly only used from, like, one or two instrumentation modules.
**Jason Plumb** 41:26 Right.
**Jamie Lynch** 41:26 So… I figure that might be the case for some of the other stuff, like, if there's loads of network code in here.
I probably… Belongs in the network instrumentation.
**Jason Plumb** 41:39 Yeah, we have this tag interface, I mean, it's almost a tag interface, closable tag interface, that is… Yeah, this has also shrunk quite a bit from, like, 2 years ago, right?
And this is where the visible screen tracker lives. Oh, interesting.
It's also a hodgepodge.
**Cesar** 42:17 I also don't know if all of these are needed Across many modules, you know? So maybe, yeah.
**Jason Plumb** 42:25 I think there's some analysis that has to be done there. If, yeah, Jamie, if you want to create an issue for that kind of stuff.
I think that's… I think that's super helpful. I don't think there is one.
**Jamie Lynch** 42:36 Yeah, I can take a look at that point.
**Jason Plumb** 42:38 Cool.
And then that leaves us with Kor, our good friend Cor.
Which has a lot of code in it.
Like, this API file makes me a little sad. But we all… we know this, like, this is not a huge surprise, but, Built by…
**Cesar** 43:07 2.0, We remove it.
And, you know, the stuff that's there.
Because I think we've gotten to a point where Hopefully, a lot of people don't need to use Core.
Right?
Well, at least one.
**Jason Plumb** 43:26 That's the goal, yeah, that's the desire.
Yeah, there's a lot of code in here. So, you think… interesting idea, though, By 2.0, we removed core.
**Hanson Ho** 43:50 I think to do that, we have to… Have a clear audit of what it actually does, what ought to be internal, and what ought to be something we should stabilize.
there… because you look at that API file, and you're like, oh boy, it's the kitchen sink in here. So, until we do that.
We don't know…
**Cesar** 44:10 Yeah.
**Hanson Ho** 44:11 Yeah.
**Jason Plumb** 44:12 Yeah, it's probably… I mean, we probably just need to start picking through this stuff, but it's sometimes, at least for me.
I have a hard time, like, okay, instrumentation, that might have a home somewhere, but, like.
like, the resource. Where should that live? Like, the resource, hugely important, we need it to identify the telemetry that's coming in. Where does this live, then, if it doesn't live in core?
10 minutes that I just…
**Cesar** 44:42 there will be…
**Jason Plumb** 44:44 Go ahead.
**Cesar** 44:44 move the parts, because Core right now, to me, feels like a backend for the agent module, so maybe we can move… stuff to… the agent.
Now the… the… the one issue… the… the one thing that I… that I… think people might need core for is to set things up in Java.
Because the agent, it's all Kotlin, so… They build the API, so…
**Jason Plumb** 45:17 Interesting, yeah.
**Cesar** 45:18 something.
**Hanson Ho** 45:21 So, so the concept of core isn't necessarily bad.
if we scoped it to what it really should be. If there are things that are effectively APIs that are on the agent, like for setting things are… that are, you know, on the STA instance, that should be an API on the agent.
So, core… we just need Core not to be something that customers who use the STA have to use.
It becomes truly internal, truly core. And everything that… Core… all the functionality Core provides.
that ought to be public, should be exposed as an interface in the correct module. That, to me, would be the, the, equivalent of getting rid of Core, making Core completely private, locked down.
So we can still have this kitchen sink. It's just that nobody has access to it, unless you're developing within the SDK and the package itself. Everything else is in the API.
and API.
**Cesar** 46:28 Hello, good.
**Jason Plumb** 46:34 Yeah, I just… every one of these, I'd stumble on it. When I look at it, I'm just like, where would that live? But I think it's just gonna take some iterative… Figuring out here…
**Hanson Ho** 46:45 I mean, that stuff could live here. Like, we do need an OTEL Android clock, it's just nobody, no customer should be, like, instantiating explicitly that instance.
**Jason Plumb** 46:54 Right.
**Hanson Ho** 46:55 So…
**Jason Plumb** 46:55 Yeah, and it's not even internal, yeah. That's a good point.
**Cesar** 47:06 There's, of course, stuff that we should remove, like the, I think pre-configure ROM Builder, that should… that should go.
**Jason Plumb** 47:15 Oh, man.
**Cesar** 47:16 Happy New.
**Jason Plumb** 47:16 That's everything, though.
So…
**Cesar** 47:21 is it? It's really where the ROM builder gets its config.
like… converted into the, ROM object, but… like, I know that the reason… I mean, that functionality could be moved to the builder.
But the reason it's here is so that users can provide their own hotel.
**Jason Plumb** 47:48 Yeah.
**Cesar** 47:48 Yeah.
**Jason Plumb** 47:49 for this, yeah, yeah. So if they want to do all of the nitty-gritty creation of their own SDK, and customize every little less bit of it, they can.
**Cesar** 48:01 But that's even… even lower level, the builder.
**Jason Plumb** 48:06 It is, it's the lowest.
**Cesar** 48:07 That's… that is what we… Tell users to use today.
From core, as well.
**Jason Plumb** 48:16 Yup.
And that's for those… that's for those weird edge cases that some user has something they have to do very special with the SDK that we don't yet have.
API surface for.
They can always fall back and use this one.
Yeah. Is it possible?
**Cesar** 48:36 public.
I…
**Jason Plumb** 48:41 Oh, internal constructor, is there a builder method?
Oh, maybe we've… maybe… Andrew?
**Cesar** 48:51 It's not even possible to use.
Right now.
**Jason Plumb** 48:54 Yeah, I forget when this happened, but this is starting to ring a bell.
Huh.
**Cesar** 49:04 Okay, so what…
**Jason Plumb** 49:06 Yeah, go ahead.
**Cesar** 49:07 What if we create an issue and start adding a list of things that we think should get removed from core, or moved?
And then we can review that list.
offline.
Or, I don't know, I'm just trying to think about that, because it seems like it's gonna be a long… running… Task.
So, just to keep track of… Because I think we talked about this briefly as… well, Jamie mentioned it yet. We have actually talked about this briefly, but we don't keep, like, log.
produce.
**Jamie Lynch** 49:48 Yeah, that sounds good. I think it's gonna be a mixture of removing some stuff that's no longer needed, and maybe just Documenting that folks should not use this module directly.
Yeah. That'd be probably 2.0.
**Cesar** 50:09 Okay, we can create that… that issue.
**Jason Plumb** 50:14 We do have one more topic, but on the top… but on the subject of stabilization and… The roadmap… I've been chipping away at this a little bit, I don't know if that's been obvious, but, like, now that we have this federation… I've kind of been going back through the registry and trying to identify stuff that's, like.
like, blaringly, glaringly non-hotel looking, and I still think there's a few more in there, but at least it's getting better. And so, I think… before we declare it stable, let's make it good, right? That's… that's the dumb guy approach that I'm taking, is like, I don't want to declare something stable while, like, it's bad, so let's make it at least somewhat good. This will also then overlap with some of the, the new repo that's hopefully going to be stood up soon, right, Hanson?
**Hanson Ho** 51:06 Repo has been stood up.
**Jason Plumb** 51:08 Oh, cool.
**Hanson Ho** 51:09 Yeah, I don't know what's inside, so Trash created it yesterday? Cool, I knew it.
**Jason Plumb** 51:16 I know it's getting close, that's great.
**Hanson Ho** 51:18 Yeah, I was, I needed to go to… I was gonna go to this SIG meeting before, to actually talk about it, but I've been either on PTO or on holiday, you know, the public holiday, or something else that's prevented me from actually attending that meeting, so… Yeah. That's been created.
**Jason Plumb** 51:36 Awesome, it's this thing, yeah, cool.
**Hanson Ho** 51:38 Nope.
**Jason Plumb** 51:44 Alright, let's move on to Cesar's issue.
**Cesar** 51:48 Just a quick one. It's based on what you mentioned a couple of days.
**Jason Plumb** 51:52 Oh, yeah, yeah.
**Cesar** 51:53 Yo.
I have an idea.
Okay. But it… it might… so I'm taking a look at it.
**Jason Plumb** 52:01 Awesome.
**Cesar** 52:02 buddy of mine.
it might… Have to be done in several… PRs, because it's gonna touch… a lot of the code, so… but essentially the idea, and if somebody Has, you know, an opinion on that, or a better… Options.
Essentially, the idea is to, Use a single… but right now, we're having the tests we have… we use, a ROM in-memory… Exporter things, where we check.
what are the attributes and events and stuff that was… that were created by the instrumentation? Yep. Essentially, it would be like to… Collect that in-memory data, and then store it In… in disk, and then dedu… deduplicated.
Per module, and then that… we'll get… turn into this YAML file that… it's probably not going to have the same structure that the one that you mentioned from upstream.
**Jason Plumb** 53:12 I think that's fine, there's no schema for it yet, really. Not really.
**Cesar** 53:17 Got it. And then, on the release, that file… It'll be read by… something during the release to generate a README.
with that… that data. So… That's the idea, high level. Okay. And as I mentioned in the comment there, it relies on our instrumentation test to actually create everything that they create, like, to test everything that they create, so… which I think is good.
**Jason Plumb** 53:51 Yeah.
**Cesar** 53:51 They should do so, so… Yeah, that's the idea.
**Jason Plumb** 53:56 Very cool. Okay.
It sounds tricky, but I think it's a very cool idea, because then you're generating it from the actual generated telemetry.
But as long as the coverage is good, it should be accurate, yeah. You got me thinking about… a change I made in instrumentation to allow the smoke test server component thing to support HTTP. If we remember the smoke tests that we have right now.
As of, like, a week ago.
Are awesome, but they run stuff, They run stuff on… like, they run this… Server on the device, instead of the server being on the host.
And… had that other PR that kind of did this, but it requires a collector, only because the smoke test server that exists in upstream had not yet supported GR… it only supported gRPC.
Which meant we had to run a collector in between to translate, because we only want to export HTTP.
But I got a PR… I got a PR through an upstream to add HTTP support, to that server, so the next release, we can leverage that. Is… I don't… is there an issue for that?
This one, yeah.
So… yeah, PR has been merged. Okay, so this thing.
**Cesar** 55:28 Boom.
**Jason Plumb** 55:28 Yeah.
So now we have… now we can export HTTP to this fake backend, we won't need a collector, and then that'll clean up our smoke test quite a bit, I think.
And that's… that's gonna be awesome to be able to run stuff.
on an emulated device, and then get the telemetry off the device, and then make assertions about it, like, that's… that's killer. I love it.
And having this little app is great.
**Cesar** 55:56 here, we'll… It will create everything… yeah, okay, right. Will be the whole app.
**Jason Plumb** 56:04 Yep.
**Cesar** 56:05 Got it. Yep.
Sounds really cool.
**Jason Plumb** 56:09 Alright, well, we are basically at time.
Sorry, I didn't see what was happening in the comments.
**Cesar** 56:17 Was there… I saw a link… Below my e- my topic.
Overall, it was just bad formatted.
**Jason Plumb** 56:29 Oh, no, that was something I… that was something I added in, just about the, client-side SEMCOM frequent being created.
**Cesar** 56:35 Got it. Got it.
So no, no topics there.
**Jason Plumb** 56:39 No. We made it.
**Cesar** 56:42 Cool.
**Jason Plumb** 56:43 Alright, time for the Java SIG.
Take care, everyone.
**Cesar** 56:50 Yep. Thanks. Bye.
