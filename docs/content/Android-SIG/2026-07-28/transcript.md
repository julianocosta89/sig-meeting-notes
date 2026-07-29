SIG: Android SIG
Date: 2026-07-28
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Cesar Munoz** 02:28 Hello.
Morning, afternoon.
**Jason Plumb** 02:31 Hey folks, sorry I'm running a little bit late this morning.
**Cesar Munoz** 02:38 It's okay, no worries.
**Jason Plumb** 02:57 How do I use computers?
**Hanson Ho** 03:01 It's too early. Computers can't be used this early.
**Jason Plumb** 03:11 There's a very real chance that sometime during this call, I might have to step away, because someone might be coming over.
So if that happens, I apologize. Please continue without me for the short time that I'm away, hopefully.
I had… At least one item on the agenda here.
Please feel free to add any others that you want to talk about. Looks like some are coming in.
So, the first one here is that there is… some new development in Open Telemetry, some new excitement around… Client-side semantic conventions, and… Hanson is floating an idea of, bootstrapping a new SIG with a new repo, and that, would include contributions from all of the client SIGs, presumably, and there's also an additional interest from the group at large, the community at large, to sort of get more regular updates from maintainers. Unfortunately, this meeting, in its current position here at 8 AM Pacific on Tuesday, is squarely at the same time as the spec meeting, which is combined… has been combined a while ago.
With the maintainer meeting. So, the maintainer and spec meeting is at the same time, so I'm floating the idea for us to try and move this meeting.
I know it's hard with the momentum, we've been at the same slot for more than 2 years, so… I'm curious what folks think.
My proposal right now is Thursday at the same time, so 2 days later than it currently is.
**Jamie Lynch** 05:06 What, to me?
**Jason Plumb** 05:09 I got two thumbs up, I got Cesar grumping, maybe? Let's see.
**Cesar Munoz** 05:14 I was just checking, but it actually works for me, too, so…
**Jason Plumb** 05:18 Okay, okay.
**Hanson Ho** 05:20 Works for me!
**Jason Plumb** 05:22 Looks like we're at 5 out of 5, David.
**Hanson Ho** 05:33 Yeah.
**Jason Plumb** 05:34 Alright, okay, so I will… I will take an action item to follow that up. Oops.
**Hanson Ho** 05:44 Jason AI, whoa.
**Jason Plumb** 05:47 Yeah, okay, fine.
**Hanson Ho** 05:54 We want the real one.
**Jason Plumb** 05:57 Yeah, and I mean, I just put this on here because it's, like.
even when I'm scheduling stuff outside of work, scheduling is impossible these days. I feel like there, like, during COVID, scheduling was so easy, no one had anything going on, and now it's just impossible again, so… Cool. That was the easiest scheduling I've done in a very long time.
Alright, Ben, let's talk about ComposeNav. I think your PR is still at that rate.
**Ben Joseph** 06:25 Yes,
**Jason Plumb** 06:26 it.
**Ben Joseph** 06:27 I think we have a couple of approvers, maybe good to merge.
**Jason Plumb** 06:33 This one.
**Ben Joseph** 06:34 Yeah.
**Hanson Ho** 06:37 The first one has the reduced scope of, of basically just, hooking up the, everything, and, and, and, and… And I think, Ben, I just got up, so I didn't check if you've, added to the other, PR with the, with the event shape. But,
**Ben Joseph** 06:59 No, that… so the event shape is what I wanted to discuss today.
**Hanson Ho** 07:02 Okay.
**Ben Joseph** 07:03 Yeah, so I'm looking for feedback on how this should be done. As you pointed out, like, there is challenge with, yeah, so we already have this visible screen tracker. So, let me first explain why I want to do this. Like, so at this point, like, we do not have any sort of visibility into Compose-based apps, like, what screen they are on. So, the basic goal is to get some sort of, you know, navigation tracking, even if it's a Compose app, like, a single activity Compose app.
So what can we do in that scenario? So there are, like, two things that I'm thinking of, like, one is the navigation itself, like, moving from one screen to a new screen. So, we… this… it might be tricky to have, like, a previous screen and the current screen, but at least the current screen showed, that is something I'm hoping for. Also, for, Just like what we have today. So this is already covered by activity lifecycle. When we move from one activity to another, we send an event, like, navigation event.
I mean, like, cycle event. Also, we have the current visible screen tracker, which stamps every telemetry with, the currently visible screen. So these two items, I would ideally like to bring to Compose as well.
And, and, so the question is, how do we want to do that? When… When we have Compose and activity competing for the same attribute, there is definitely a challenge there.
So what I've seen is, like, I think some SDKs, they either let you select one.
Of this, either activity or compose.
And the other option is to have separate, attributes for activity and, Compose Space Screen.
Or… You can have both, but what, So then, then basically it means, like, you will have certain allow list or block list for activities. So, say you have multiple activities, only a few of them use Compose navigation, and, like, both others are, like, just activities, plain activities. In that case, you can include those activities.
But when it comes to an activity that hosts Compose, you basically ignore that from any sort of disabled screen tracking or navigation events. For those activities, we will only consider what's happening within that activity, which would be the Compose part of it.
So, these are the, kind of, three, high-level approaches we can take.
And, like, I'm open to more ideas, like, this is what I could come up with. So, in these, like, what would be your suggestion? Like, what is the preferred approach?
**Hanson Ho** 10:04 So, I think the original, the current implementation.
with screen tracking is a bit overstating what it's actually doing. It is basically just an activity lifecycle, tracking, and I believe it doesn't do open spans, or does it create events?
But whatever it does, it is not screen tracking, it is activity and fragment tracking, so that's part number one.
the Compose, destination lifecycle kind of lives embedded within the activity lifecycle, because, you know, a Compose component has to live within, you know, an activity, so it always kind of fires. The problem is that the lifecycle events are kind of, they don't… Get processed along in the same way. So they're kind of similar, but kind of parallel.
So, there's a couple of ways of solving this. One is basically making those two life cycles for the instrumentation, just reporting those events from those life cycles. So they can be interspersed, they can kind of mix. So we have, basically, an activity lifecycle event reporter, and then we have, like, a jetpack navigation destination load.
reporter.
Those can fire and report events when they happen, so they can coexist.
So that's kind of one way of doing it.
We could basically make each event, very specific about what it's doing.
And then those can be laid on top of each other. And if you just want to have, kind of, you know, events and signals for when those things happen.
that… That is good.
If you want to track, times between those, it's a bit trickier.
So, so that's… if you want to do that, that almost might be, like, a second step.
Now, the existing implementation is about… the existing semantic is screen, which is… Probably wrong.
So we could consider… Deprecating the…
**Jason Plumb** 12:16 So, Hanson, tell me more about that, because I believe in… RUM product, like a RUM interface, the user who's looking at, you… A user that's looking at an end user flow is concerned with what screen the user is on at a given time.
**Hanson Ho** 12:31 Yes.
So, the activity, life cycle doesn't tell you what screen you're on, because…
**Jason Plumb** 12:38 Yeah.
**Hanson Ho** 12:39 And.
**Jason Plumb** 12:40 Especially within the context of Compose.
**Hanson Ho** 12:42 Exactly.
**Jason Plumb** 12:43 But if you have, like, a classic app where you're just doing activity stuff.
**Hanson Ho** 12:47 Yep.
**Jason Plumb** 12:48 you know, that's… that's… that's what that was built on originally, was the idea that, like, oh, yeah, you have activities in your app, we can give those a screen name, and… Yes. How's your uncle.
**Hanson Ho** 12:59 And, and… so it makes sense, like, activity mapping to a screen for certain Android apps makes sense. And you can actually derive the name of the screen from the activity. You know, that all kind of makes sense. So in Compose in there, you… you have destinations that live within a screen, and you can look at the destinations as… the nav destinations as a screen, and that makes sense in total.
But what happens when you have those two things laid on top of each other? Because for Compose, you have to have activity. For an app, you can have multiple activities. Some have Compose, and some don't have Compose. So… You could always say both of those are screens, but then if you have an activity screen quickly overridden by a navigation screen, you know, how do you… how do you… how do you reconcile that?
And especially if you have other screens in your app that are actually activities. So, you would have to do the configuration that Ben was talking about, where you let some of these use activity, and you let some of these… like, you can do through annotations and say, hey, if you have this annotation there, you know, or like, if you have Compose, then… your activity navigation doesn't, like, fire off the screen, so… Having both life cycles be aware of each other is the only way to basically avoid the duplication.
So… that is one way of doing it. So, what I described, basically, was everything separate is one way.
And then basically using suppression and annotations to make sure they don't duplicate. That's one way. The other way is to kind of have a unified lifecycle.
and a unified processor that makes it aware of both life cycles, and to say, hey, for this given, activity I'm loading, should I show activity, or should I show, compose?
And then… and then deal with it that way. Both of those, we can call screen.
And, and move on.
**Jason Plumb** 15:01 I like that latter one. I mean, let activity and compose live side by side. As long as the ordering is kind of correct, right? As long as the compose stuff, which is, in my brain, at least the more granular thing, like, activity is kind of like a container. Within an activity, you typically have composed composables. Letting those show up after, I think, I think is actually fine. If you get… A span that says… this screen is active, or an event that says this screen is active, and then, like, shortly thereafter, you get the composed version, and maybe the names aren't the same. I don't think that's super confusing. And then in the worst case scenario, you disable the activity.
**Hanson Ho** 15:42 The problem is the order is not guaranteed, so, on resume is where I think the existing instrumentation fires activities loaded, but the callback for destination load could actually happen before.
**Jason Plumb** 15:55 The controller.
**Hanson Ho** 15:55 We've created.
**Jason Plumb** 15:56 Okay, so the ordering is hard to get right, is what you're saying.
**Hanson Ho** 15:58 Yeah, potentially is a race condition.
**Jason Plumb** 16:01 Okay.
**Cesar Munoz** 16:03 What are we capturing?
out of activities, because I don't remember what… is it spans, or just events?
**Jason Plumb** 16:11 Yeah, I pulled it up, so… maybe we ought to do something about this nonsense. Apps start being part of activity, whatever. Please fix that. But the, activity change, has a span.
And I think the reason it was chosen as a span is because, like, the sub-lifecycle stuff is also exposed through span events.
**Hanson Ho** 16:39 So… the… The argument for… Separating the two sets of, Telemetry logged is that we could basically start the new one, and then leave the existing one as it is, and then refactor it after.
If we want to kind of, like, bolt this on to that, that instrumentation has to change. Otherwise, we'd have basically two… two instruments… like, two instrumentation writing to the same, and… and you're gonna have this issue. I think the first thing that needs to happen, like, similar to what Ben has done, in the… in the Compose, you know, hook.
is… is basically firing something, notifying something when something happens. So that's almost like step one.
Figuring out what that event would look like, and then getting that in there. The second step is how do we reconcile this with what's existing? One way is just deprecate that, make something new that supersedes both, and is aware of both, and do it like that.
Or…
**Ben Joseph** 17:54 Nope.
**Hanson Ho** 17:55 change the activity one to be… sorry, change the existing one to be more narrow in scope.
And then, basically keep both.
**Cesar Munoz** 18:06 That's something I was… so based on what we're discussing, it looks like… Really, the only problem, apart from the upstart.
Stuff from the existing activity.
instrumentation. It sounds like a lot of the issues will go away if we just remove the two last attributes.
Because those are the ones that kind of make us assume that the… Intent of that activity is to be a screen.
Where, you know, which might or might not be correct, depending on the app. So… Would it… what if, like, just as a thought experiment, if we remove these two attributes, then this will just end the application starting. Then it will just remain… this will just remain as an activity lifecycle instrumentation that gives… Lifecycle awareness.
Of activities, and then we can then have screen transition events.
For… for both activities and composables, then maybe, you know.
Different instrumentations, but this will just not be anything related to a screen, it's just an activity lifecycle.
Instrumentation, and that will be it.
**Hanson Ho** 19:32 Are the existing, attributes we use part of the semantic convention?
**Jason Plumb** 19:39 I don't think so…
**Cesar Munoz** 19:43 Me neither.
**Ben Joseph** 19:44 No, I think. No, I think.
**Hanson Ho** 19:46 So this is where we could maybe get a bit… More granular about how we either report this, or allow some sort of configuration to say, I want one of this one or the other. Without… that's… that's assuming we don't want, like, a unifying one that's aware of both life cycles.
**Jason Plumb** 20:08 What it sounds like I'm hearing, though, is that, The importance or value of having a screen, and knowing which screen you came from.
is not as important to people. Is that what I'm hearing? Like, just losing or not caring about the notion of screen, even though that is, like, a higher level construct than all of this activity, fragment, composables… like, there's this… the idea… the intent was to be able to convey what's… what screen you're looking at. Like, what screen the user's looking at when stuff happened, right?
It sounds like if we remove these, though, that people… if… like, the idea of removing these kind of implies to me that it's not as important.
**Hanson Ho** 20:53 So, I think it's important. I think it's actually not… we should… it's not… I don't think we should remove it. I think we should either report both.
Basically, you can figure out what screen is based on what the last destination is, or what the last activity is.
Because when… when you're… if you're using activity lifecycle to map to a screen, you're basically saying what the last activity is anyway, or I think they use the word… may use the word screen because some of them are fragments. So, whatever the existence partition is, the last big piece of UI that was loaded successfully.
This, the Compose stuff adds, like, another layer to it. So… We could use the same attribute.
if we could manage the life cycles to make sure that the last writer is whatever is appropriate. So I think… I think it's… it's… it's… it's not that bad to have, like, activity load, and then… and then the compose destination load. So if you can have, basically, and the activity, when you start, you figure out whether you have a nav controller, present.
And then on resume, you fire the, activity if there's a little nav controller. And then if there's a nav controller, then you fire… you let the destination instrumentation, you know, fire the last one.
So, that's how you would commingle those But that… that piece of… Code would have to be aware of both.
So…
**Jason Plumb** 22:22 Yeah, I'd love to not have that interaction or awareness, that coupling between these instrumentations. Like, I don't think there's any prior art for that yet, and… Yeah.
**Hanson Ho** 22:30 So what we've done in Embrace is, we've basically created, you know, our own events. So, what those instrumentation will do is fire events into a common queue.
And that thing processes and understands what's going on. So those two instrumentations are not coupled, but there's a third component that basically is aware of those events that they're firing. And I think without that third component, you're basically… you basically have to… your instrumentation has to work independently.
And if you work independently, then by definition, you don't want to have that coupling.
So…
**Jason Morris** 23:05 I… I just have two key to contribute here and say, Jason asked the question earlier, isn't this a higher level concept? Like, isn't… are we maybe not conflating mechanism with intention a little bit? And we're talking about the lifecycle ordering of Compose and navigation, jetpack navigation, and fragments, and activities, and so on.
Where, really, what we actually want is, like, a formal definition of what screens are, or at least this idea that screens are not any of these things.
But they… they can be implemented by those things.
And does that maybe not take away a lot of the, well, how does it order, how does it couple, etc, if you have a formal, what is this… what screen am I on, what screen was I on, concept, and just decouple it from the rest of the implementation for now.
**Hanson Ho** 24:03 I was…
**Cesar Munoz** 24:04 Yeah, I agree, and it… oh, sorry, Hanson.
**Hanson Ho** 24:07 Oh, I was just gonna say… I was gonna say, I was… I was trying not to, like, boil the ocean and bring that up, because yes, that's ultimately the right thing to do. And we haven't even brought over, like, the render piece as well, which, you know, there's a PR about DTID and things like that. There's a third life cycle that we're gonna introduce into this fray. But yeah, that is… if we want to kind of, like, just step back and kind of do it from scratch.
that's where we should, you know, what is a screen?
**Cesar Munoz** 24:34 My opinion… my opinion is, regarding your question, Jason, I think it is useful to have the screen name.
It's just that… as I say it, maybe I don't remember stuff that's important, but, the activity lifecycle, to me, it's… it's that. It's an activity lifecycle. And… and it's… it's its own thing, and we… we could try to put a name to it, and say that it, you know, it might also give us a hint of which screen it is, and the screen in some cases, but it's just that I think for that instrumentation, it seems to me that we're adding an extra responsibility that probably shouldn't be there, so maybe we should keep the screen, it's just that it's its own thing. Maybe it's an event that it's created, somewhere else.
But I think it's also important to have this in… this… Activity lifecycle stuff, depending on what you look for.
So, I think we need both, it's just that it seems like putting the screen there seems to add Some responsibility that maybe doesn't belong there, and maybe it could be easier to have like, an event, just an idea, it doesn't have to be like this, but maybe if we had an event that tells you when a screen has been loaded.
For example, you… we probably could reuse that for each… type of… screen that users could use in their application. Maybe if they go all with activities, or even fragments, or Compose, then there could be a way for them to get a screen event out of Each of those, and then users can probably pick and choose which one they want to Collect screen names from.
Maybe that's… Kind of like an idiot.
**Ben Joseph** 26:31 Just, just want to add two pieces of information that made me relevant. So, first of all, the activity, related spans, they are reported under the lifecycle scope.
And the other piece is that the screen name. So this is, it's not strictly speaking part of the scope, the light cycle span, I think. It's… For any telemetry that we send, like, we, attach the screen.name from the current visible tracking, like, visible screen tracker.
So… so that's… that's where it's coming from. It's not strictly, tied to the, COP.
**Jason Plumb** 27:08 And this is the way it behaves today, right?
**Ben Joseph** 27:10 Yes.
**Jason Plumb** 27:11 Yeah, okay.
**Cesar Munoz** 27:14 So just to understand, the idea would be to add the screen name.
like, a global attribute to… like, a session ID attribute. It is right now.
oh, I see.
**Ben Joseph** 27:27 Yeah, we have these span processors and lock process that Add these additional attributes on.
**Cesar Munoz** 27:34 Right, so in that case, we definitely must… Big one.
That's… that's, I guess, that's the prime, yeah.
**Jason Plumb** 27:42 Yeah.
**Ben Joseph** 27:43 So, which… which makes a case for, you know, screen can be a separate entity unrelated to the activity lifecycle.
It can be its own independent thing.
But, like, how we update the visible screen tracker would be the challenge, like, based on the, Callbacks, or, like, the risk condition.
**Jason Plumb** 28:07 I think it's gonna require some reworking. I mean, I think there's some stuff here that's, like, missing, and I think this work is highlighting the shortcomings of all of this stuff.
I suggested that maybe this is suggesting that we have some kind of screen API that instrumentations, or even user code might leverage to indicate, like, what the current screen is, or, like, when a screen is starting and when a screen is ending.
I think having some duration, like, having, like, leveraging a span so that you can have child stuff associated with that context, that open Telemetry context.
And a duration, because… I believe that in Rum products, people will often ask the question, well, how long were they on that screen? Or, like, how, you know, how long were they looking at the cart before they submitted the cart? Like, that kind of stuff. So having a duration for a given screen, I think, is often very helpful in a RUM product.
But I…
**Cesar Munoz** 29:03 I like… I like the idea you said about an API that uses.
**Jason Plumb** 29:07 It's been cold.
**Cesar Munoz** 29:07 Cool.
And… and probably… That could be a good start. They will have to manually say which screen they… they are.
And we'll track that as a global, you know.
Idea of a screen for each.
Telemetry that is sent.
And then maybe… Later, we could… at a… an upper layer to that that does this automatically only for one technology that we choose, which might be composables, and that would be it. And so, users who are only using composables.
Then, navigations with composables, then they will get this free screen right away, and users will want to do something else and will have to manually call the API.
Maybe, like, prove your way?
**Hanson Ho** 30:00 So, the reason I asked about semantic conventions is that if what the screen tracking, thing we have right now isn't part of semantic conventions, we can effectively start a new one.
that will have an attribute that's in the semantic conventions, and that's where we define what a screen would be. So we basically would have something that supersedes this, but writes a different attribute that is gonna be part of semantic conventions. So, what we have right now could then be deprecated and said, hey, previously you used this non-semantic invention attribute to define what last green is. This is a new one. And with that new implementation, that's when we can fold in this new concept.
have… have basically, an API internal to… to the instrumentations that fires events, and then something else that… you know, visible screen tracker V2 that listens to these events, and then depending on configuration, or if you don't want configuration, depending on just the events coming in, decide what that last screen is.
And set that attribute.
**Cesar Munoz** 31:04 If I understood correctly, you're saying that we should first define something In the semantic conventions, before we can… Add anything here?
like an API, or…
**Hanson Ho** 31:18 No, we can have the API right now. it's attaching the, new attribute.
To the Telemetry, like we do currently for the visible stream tracker.
That's a part where we don't even have to get it approved, per se, just, like, we'll use a string that we're gonna say, hey, we're likely gonna use this, and if it changes, it changes. We'll change it afterwards. So basically, consider the old thing deprecated, and make a new thing that… does what the old thing does, but a little bit better. And bound to an API that we create internally for the project. So, activity, lifecycle events will report.
something that this new thing listens to, and compose destination will do. Nav3 backtrack mutation, backstack mutation will fire off something like that. And hell, customers could even, like, implement their own custom one, although… They can really fuck things up by, by introducing their, hey, my cool screen, and it's like, you know, kills all the auto ones, but… If we want.
**Jason Plumb** 32:22 The libraries, I mean, the thing that's gonna happen is the libraries are gonna screw it up, but whatever, like… I… I think a lot of this discussion is good, I also think it's kind of forward-looking, and I'm a little concerned that this might be pulling Ben a little bit far afield from his original questions, so let's circle back and see if this is at all helpful.
Ben, is this the discussion you wanted to have?
**Ben Joseph** 32:47 It's certainly in the right direction. So, I mean, I understand, like, we need to, you know, probably… You know, re… like, revisit the idea of screen and, like.
go from there. But, again, Given, given the current, like, I'm looking for, like, immediate direction. Like, if this is something we wanna, you know, nail before we, you know, take the next step, I'm happy to, you know, wait for that. But, like, if you think, like, we can… I can, you know, make some immediate progress on any of these aspects, I… I can go ahead and do that as well. So I'm, honestly looking for some direction, like, what should be my next steps in terms of, this.
**Jason Plumb** 33:36 And are you also asking within the context of this PR?
**Ben Joseph** 33:39 So I think that kind of, has, is mature, and, like, it's an independent piece. This does not change any existing behavior. It's just, like, as, Hanson mentioned, it's a step one.
It doesn't do anything yet, so that's what it should do is what I'm looking forward to, like,
**Jason Plumb** 34:00 So for the next step, you're looking for, like, a follow-on to this one. Okay, just want to spell this out, yeah.
**Ben Joseph** 34:05 Yeah.
**Hanson Ho** 34:08 The most basic thing is to fire a semantically conventioned, event.
**Jason Plumb** 34:14 It's just, I think an event… I also am inclined to say event, so I'm agreeing with Hanson, like, even in the short term, like, having an event that indicates this screen is now active, or this screen started, is a step in the right direction. We may circle back when we do some of this larger work.
And say, oh yeah, that event's not helpful, we have start and end times, like, I don't… You know, that's, like, down the road, but having events now would be great.
**Ben Joseph** 34:39 Okay, so, so currently we have activities within the lifecycle scope, so, I'm hoping, like, for Compose, we can have a, navigation scoped, event, that, that fires on, on, based on this navigation destination change.
Does that sound good?
**Jason Plumb** 34:57 It does to me, I would want to just… I want to make sure that it's not firing too much, like, it needs to… it needs to be something that constrains it to, like.
hopefully some form of grouping within an app, or a screen. Like, I don't… those terms are nebulous, but, like, within… within some kind of structure, like, every composable cannot fire an event. Like, that's absurd, right?
**Hanson Ho** 35:18 The thing about this is, actually, it's bound to the Jetpack navigation library that actually could not have.
**Jason Plumb** 35:24 Okay.
**Hanson Ho** 35:25 still have it. So these are, like, literally the, navigation library saying a navigation event has happened, has succeeded. So these, these, these should be effectively, someone going or perceiving that they've gone somewhere else. So these are analogous to…
**Jason Plumb** 35:44 That seems like a great fit to me.
**Hanson Ho** 35:45 It is.
And in my, in my sample of semantic conventions, I declared, actually, an app navigation complete event, which… something like that could… could be done, could be used. So, yeah.
**Ben Joseph** 36:05 Yeah. So, the only other, problem I want to, check on here is, like, for any event, we kind of overwrite the screen.name at this point.
with the activity name. So should… should that be, like, as I'm working on this event, that… that might, like, Is that… is it okay to maintain that behavior?
Along with the navigation destination. So this would be a destination.
Yeah.
**Cesar Munoz** 36:34 I'm a bit confused, because I don't see how that will clash with the activity. So, my understanding about the existing activity screen name.
Is that it's just an attribute for that span.
So it shouldn't, like… How… so how do you think it will… like, an event will be just one… one log event?
With that.
**Ben Joseph** 36:55 So…
**Cesar Munoz** 36:56 Composable screening, right?
**Ben Joseph** 36:58 So, within the… within this Compose instrumentation, if I fire a log event for, you know, destination change, then, before the event is sent, we add additional attributes.
Which… one of which is the screen.name.
So I'd say it's a kind of a processor.
**Jason Plumb** 37:16 Yeah, what component does that again? I forget.
**Ben Joseph** 37:20 Span, span lock processor, sorry, yeah, Sorry, it's a span processor, I don't remember exactly what it…
**Hanson Ho** 37:30 That's not the same thing as the last, the last screen act, the visible screen tracker. I thought that was what was writing, I thought the.
**Ben Joseph** 37:39 Easy.
**Hanson Ho** 37:40 would be that, in that event, there will be an attribute called screen.name, which is the activity name, and then the event would be navigation destination complete.
**Ben Joseph** 37:50 Oh, sorry.
**Cesar Munoz** 37:51 Is that one.
**Hanson Ho** 37:52 That last screen tracker basically has hijacked the screen concept for itself, and using it to report activity.
Yeah. That, that is…
**Jason Plumb** 38:06 That's not fair, Hanson, I'm sorry. It's through the visible screen tracker, like, that's the reason why this abstraction exists, is it's not activity tracker, it's visible screen tracker.
**Hanson Ho** 38:15 Right, but what it actually does is it takes the last activity and puts it on as a screen, is what I'm saying.
**Jason Plumb** 38:20 Something else does that. It's not… it's so…
**Hanson Ho** 38:22 It's not that?
**Jason Plumb** 38:24 The visible screen tracker doesn't know anything about activities, as far as I know.
**Hanson Ho** 38:27 Okay, alright, then, then, okay.
Alright, then I don't know what is hooking it, then. So, cool. If that is… if the visible screen tracker is agnostic, so there is then some event that fires.
**Jason Plumb** 38:41 Aw, shit, it knows all about activities and fragments.
**Hanson Ho** 38:44 Yeah, that's… that's what we thought.
**Jason Plumb** 38:46 Kill it with fire. Kill it with fire. Okay.
**Hanson Ho** 38:49 That, that.
**Cesar Munoz** 38:50 Right.
**Hanson Ho** 38:51 That's the original problem, so it's… Which is fine for what it was, but now we're adding another concept that is modern.
**Jason Plumb** 38:59 on my screen.
**Hanson Ho** 39:00 So…
**Jason Plumb** 39:00 These are… oh man, this API. Okay, so these map sort of into these concepts. The end goal should just be these two, maybe, or whatever. That was the thing that stands out for me, is it should be these two.
the fact that the API kind of has knowledge of fragments and activities is a little bit of a bummer, but I think it was trying to hide that. I didn't realize it was even an interface.
But cool, okay.
My bad.
Yeah, so…
**Hanson Ho** 39:27 Oh, by the way, are you sharing your screen?
**Jason Plumb** 39:30 Yep.
**Hanson Ho** 39:30 Okay, alright. Yeah.
**Cesar Munoz** 39:32 I see.
**Hanson Ho** 39:33 Okay, cool, I'm just not… oh, I see it, never mind. There's two tabs. Forget it. Never mind.
**Jason Plumb** 39:39 I've done that same thing, Hanson, it's super confusing in Zoom. I agree. Yeah.
**Hanson Ho** 39:43 Nope, it's just too early for me.
**Cesar Munoz** 39:45 So, now I understand properly, Ben. So, of course, if you use the same name, then it will be… it will just override, or get overridden, I guess, whatever happens first. So…
**Jason Plumb** 39:56 Yes, yeah.
**Hanson Ho** 39:58 So, I don't think we would use a same name, because the current name is not semantic inventions. I think the confusion is that we have a navigation event. We'll have a semantic invention name, app.screen, or, like, whatever it is, and we'll have an addition, additional thing that says, hey, screen.name, not semantic invention. You're like, what the hell's going on?
**Cesar Munoz** 40:20 Maybe the…
**Jason Plumb** 40:21 Go ahead.
**Cesar Munoz** 40:23 maybe in the future, this visible screen tracker could be, like, the source of this API that we were mentioning, so it could The manual thing that users will reach.
And maybe instrumentations like the one Ben is working on will… it will automatically call that API.
But it will… like, the… I guess what… what it should be done, definitely, at some point, is to remove the, the activity and fragment awareness of it. So… But probably, this is what Hanson was mentioning about deprecating stuff.
**Hanson Ho** 41:04 So I think… I think for now, as long as the event we're firing doesn't talk about screen and talks about navigation, then those things can coexist. So for the context of this, this, this, for Open DevelopG Android, currently, screen maps through activity. And… It's not right, but that's what it is.
**Jason Plumb** 41:24 Amen.
**Hanson Ho** 41:25 Yeah, and fragment. And fragment. And then… and then it's… when we go V2, is that we redefine the concept of screen.
And that's when, we could modify what Visible Screen Tracker does. And then, at that point, it could also consume, events from, Compose.
and use that as the screen. So in that case, then those things will be congruent, using the same attribute name, so that, yeah, they might overwrite each other, depending on order, but if it's the same value, well, we can… Or we clean it up later, it doesn't really matter, at least for the first thing, and go from there. So… I think that would be the easiest.
**Cesar Munoz** 42:07 That sounds good to me.
**Hanson Ho** 42:08 For right now.
**Cesar Munoz** 42:10 Sounds good to me. So, I think the last step, then, we're almost there. It's, which will be the name?
of this attribute, I guess.
**Ben Joseph** 42:19 Oh.
**Cesar Munoz** 42:20 Something like navigation… Yeah. …completed? Yeah.
Target?
**Hanson Ho** 42:25 app.navigation.complete. I, I had.
**Jason Plumb** 42:28 Are you talking about the event name?
**Ben Joseph** 42:30 Yeah. Yes.
**Cesar Munoz** 42:30 Know that… Okay. Yeah.
Whoa.
**Hanson Ho** 42:33 there should be an event name and also a screen name. I think app.screen.name or something like that would… would… would… Yeah.
**Jason Plumb** 42:45 So what do we… what do we like for the event name?
**Ben Joseph** 42:48 Should it be a route or a destination?
**Hanson Ho** 42:55 I would even… the event itself could just be navigation complete, and basically not tie it to Compose.
And then within that, we can… we could… we could… we could report attributes a bit more, granular, like screen, or… or destination, or whatever it is. Or you could make it, restrict it strictly to compose, and basically say, compose destination loaded, or something like that.
So, it's, it's how… it's, again.
So, semantics, it's how narrow you want to be, and how specific, or how specific you want it. Those are the same thing. How general you want to be, or how specific you want to be.
**Ben Joseph** 43:35 Right.
**Cesar Munoz** 43:35 I like… I like Navigation Complete as an event name.
AppScream name, I think we cannot use it, because.
**Hanson Ho** 43:42 AppDot. AppDot. We have to use app.
**Cesar Munoz** 43:45 Right.
Now, for the screen attribute, I don't think we can use that one, because that would be the one for the visible screen tracker right now.
**Jason Plumb** 43:53 No, I think it just says screen name.
**Hanson Ho** 43:55 I think it's just screen name.
**Jason Plumb** 43:56 Yeah, I thought I had that.
**Ben Joseph** 43:58 I think we recently changed that.
**Jason Plumb** 44:01 Did we?
**Hanson Ho** 44:02 Oh.
**Ben Joseph** 44:03 Yeah, they have to add app.
**Hanson Ho** 44:06 Oh, did we? Did we release it?
**Ben Joseph** 44:08 It's in that, I think it's along with the app.crash, like, device.
**Hanson Ho** 44:16 Last.
**Jason Plumb** 44:16 Is it in Upstream?
**Ben Joseph** 44:19 Maybe I'm confusing with iOS. Somewhere I saw it recently, Jake, sorry, my bad.
**Jason Plumb** 44:26 It's almost like we need a central repository for this stuff.
**Ben Joseph** 44:28 This is…
**Cesar Munoz** 44:30 This is… the one that we're using comes from Kotlin.
Same comp.
**Jason Plumb** 44:35 Is it?
**Cesar Munoz** 44:35 And I'm looking at the IDE, it looks like it's.
**Hanson Ho** 44:38 Then it's upstream.
**Jason Plumb** 44:40 Yeah. Okay. Well, that's… So that's the one that the appender is putting on all the Telemetry currents.
**Hanson Ho** 44:47 Oh, so, so the…
**Jason Plumb** 44:48 We want to use a different one.
**Hanson Ho** 44:49 So, so there is a syn… so… so… so they have… It is a semantic invention.
One, then. Somebody in a smart convention.
**Jason Plumb** 44:59 So, what.
**Cesar Munoz** 45:00 Yeah.
**Jason Plumb** 45:00 This is… this highlights a different problem, then. What is this being used for?
**Hanson Ho** 45:08 Is it used to… is it even used?
**Jason Plumb** 45:10 It's gotta be, and we've probably got a mismatch then. Like, we should remove… we should pro… almost certainly, we should remove this from our locally federated SEMCOM.
Because we should be using app.screen.name. So I will take an action item to track that crap down.
**Cesar Munoz** 45:29 Thank you. It's probably just a leftover of it.
**Jason Plumb** 45:32 Yeah, I hope so.
**Cesar Munoz** 45:33 Maybe we're… maybe we're not against…
**Hanson Ho** 45:35 So, again, if we don't report a screen name, then that's fine. We can report an aviation destination. And then, basically.
We never want to chi… Will the instrumentation be that?
**Cesar Munoz** 45:47 destination name?
Is that what you're saying?
**Hanson Ho** 45:51 Yeah, app.or…
**Ben Joseph** 45:53 Navigation.
**Hanson Ho** 45:53 Greg.
We can figure out the specifics later, but, like, it'll just not be… we're not gonna try to, like.
we're not gonna try to, in this event, take over the concept of screen. Screen just remains what it is. We're just gonna say…
**Jason Plumb** 46:07 That's approach.
Yeah. Yeah. Yeah.
**Cesar Munoz** 46:10 Yeah, I was trying to report something… Because I think this is, like, this is actually the… the… the… the main blocker for Ben. So, that's what I was saying, what name… I think app.destination's a name.
In the meantime, while we figure out the other.
**Hanson Ho** 46:28 Let's, let's put app.navigation.destination.
**Jason Plumb** 46:31 Dunname.
**Hanson Ho** 46:33 So all of that… well, we don't need the .name, I think.
But, you know…
**Jason Plumb** 46:39 Everything in a hotel has name on it.
Because there's gonna be, like, a type later, there's gonna be a namespace, you know.
**Hanson Ho** 46:46 Well, this is our namespace, but… Whatever, it's fine.
**Jason Plumb** 46:54 Which one do we like better?
**Hanson Ho** 46:59 I like destination, because we're implying that it's a name, because we're defining it, and we're not defining a subdomain, or, yeah, subdomain. Domain is what they use, right? Or… namespace, subnamespace.
**Jason Plumb** 47:17 I was gonna put in a string, I think we should put name.
**Hanson Ho** 47:19 Sure.
Ben?
**Cesar Munoz** 47:23 I agree, maybe it's better, but it's quite long. But yeah, I guess it's more… Correct.
Yeah.
**Ben Joseph** 47:34 If that's the pattern, let's follow that, I guess.
**Jason Plumb** 47:38 Yeah, okay, so let's do that, and then for the event, do we agree that this is… this is something we like?
**Hanson Ho** 47:44 Yep.
**Ben Joseph** 47:45 Yeah.
**Cesar Munoz** 47:45 Sounds good to me.
**Ben Joseph** 47:47 Yep.
**Jason Plumb** 47:47 Okay.
Okay.
Cool. That was a nice discussion. I want to give a little extra… so we've got about… generally 8 minutes left if we end 5 minutes before, which we try to. Let's move on to these other PRs that I think have not gotten some love recently. Let's talk about this one first.
Yeah, so… I haven't come back to this… I know that there was some work done, and I just haven't had a chance to digest it yet, I'm sorry. I can… if y'all are happy with it, I will remove that, but it looks like… it looks like the concerns I had were acknowledged, it looks like there was some follow-up work, and it got two other maintainer approvals, so I can remove this. I'm fine with that.
I just don't remember how to do it.
It's in here.
I think it's… Yeah.
This one?
Oh, I don't remember. I don't do this very often.
**Cesar Munoz** 48:55 A near review.
**Jason Plumb** 48:57 Wait.
How'd you get.
**Ben Joseph** 49:01 Things I'm good.
**Jason Plumb** 49:02 Yeah.
Let's try that.
**Hanson Ho** 49:10 reason.
**Jason Plumb** 49:11 Okay, good. I was worried it was gonna remove this, but no, GitHub's good about leaving context, so that's great. So, if you all are happy with this, I think it's fine. And let's look at the other one.
**Ben Joseph** 49:23 That's mine, Compose.
**Jason Plumb** 49:26 And I'm, yeah, okay, it's the same one. So I'm sorry to be the blocker on that one, I just, especially since it, you know, was native code, I wanted us to be very careful about it.
**Vishwan aranha** 49:34 We just don't have the merge access, so if you guys can merge the two, that would be great.
**Jason Plumb** 49:39 No, I know we have to, yeah, that's, that's part of the job here, so… Okay, cool. I haven't had context on this one either, so I apologize. Again, similar situation, we've got the approvals. Cesar, have you looked at this one?
**Cesar Munoz** 49:56 I think so, yeah.
**Ben Joseph** 49:57 Yes. Okay, thanks.
Okay, good.
**Jason Plumb** 50:01 Yeah, I don't… it seems like we're ready to merge both of those.
**Ben Joseph** 50:06 That was all.
**Cesar Munoz** 50:07 for me.
**Jason Plumb** 50:11 Okay, cool.
I think that was… I think that was easy. That was… that was faster than… it was 2 minutes instead of 8, so…
**Ben Joseph** 50:20 God.
**Jason Plumb** 50:21 faster than I thought.
Alright, Cesar, you push the button on this one, I'll push the button on this one, and we don't have to do it on the call, but yeah, we'll get those merged, and they'll be in the next release, which I think we need to do, actually.
So, that got me thinking about release 3 weeks ago. Upstream released last week, I believe, and Upstream being instrumentation. That's our main dependency, right?
Yeah, this is, like, Friday, I think.
Monday. So, we should do a release.
**Hanson Ho** 50:58 Did we merge the thing with the semantic conventions, where we detach ourselves from Kotlin and just build from scratch?
**Jason Plumb** 51:08 No, but that would be nice to have, wouldn't it?
**Cesar Munoz** 51:12 Yeah, but the one that.
**Jason Plumb** 51:14 They're creating.
**Cesar Munoz** 51:14 Hanson?
**Jason Plumb** 51:15 Yeah, it's one of these.
**Hanson Ho** 51:17 I was waiting… yeah, there's one that's, like, ready to be merged, or something like that, and I was waiting.
**Jason Plumb** 51:21 on…
**Cesar Munoz** 51:22 I didn't approve that one, I was just… I just asked a question because I think this only… cover at the jank, if I understand correctly.
I was wondering if we'll add the rest of stuff that we use from Austrian, you know?
**Hanson Ho** 51:38 Yes, so I think I was waiting for… Actually, the one that takes, that takes away OTel Kotlin and regenerates everything, I don't think is this PR. I might not have created it. I think it might still be in draft.
**Jason Plumb** 51:53 I think it's Do Not Merge, I think it's this one.
**Hanson Ho** 51:55 Okay, I could, I could…
**Jason Plumb** 51:56 this one.
**Hanson Ho** 51:59 Yeah, no, no, I think, I think this one is using the, the fake, one, but, This might… it might be a subset of this one, I might need to, like.
**Jason Plumb** 52:08 Okay.
**Hanson Ho** 52:09 start a new one. Because that do not merge is Do Not Merge that points to the fake, federated, client SEMConf, but…
**Jason Plumb** 52:18 Okay, it sounds like we can get this one in. I like this idea, I think we can do this, so…
**Cesar Munoz** 52:26 Yeah, sounds good for me, too. So it sounds like this will be, like, a first step, and then you'll add the, like, the rest of…
**Hanson Ho** 52:33 Yeah, forever.
**Cesar Munoz** 52:33 later, it's…
**Hanson Ho** 52:35 the registry… so what will need to happen… well, I mean, actually, two separate things. One is, don't take semantic convention constants from Kotlin, and basically build it all on Android, like we have for these custom ones.
And then basically ensure that all the events that, we do record, defined upstream are built. One way is to manually say each one we use, we import, or we use a wildcard and say, bring them all in. But I think just selecting each one for now is probably the safest thing to do. And that's… it's pretty mechanical to do that. So I can put two PRs on top of each other. Have this org been approved for using stack changes?
Yeah? You know, that's fine. Those should be unrelated, so I will… or I will resolve them if it's a problem. So I'll send two PRs, for this.
**Jason Plumb** 53:29 Okay.
I… I think this is great, I think this can go in. I think those other two that Ben brought up, I think we should get those in the release, but I don't think that semantic conventions should gate the release. It's like… that's not anything functional or user-facing, that's kind of internal housekeeping stuff, so… I don't think it should gate it, but, having the crash… native crash stuff in there would be great to have in the release, so I think that should go in, and then the Compose as well. At least the framework for Compose.
Cool. So, let's do that. I… did you do the release last time, Cesar, I think? Maybe I was out, so I'll do this one, if that's helpful.
**Cesar Munoz** 54:07 I forgot, but if you wanna do it.
**Jason Plumb** 54:08 I forgot to, man.
**Cesar Munoz** 54:10 Go ahead.
**Hanson Ho** 54:11 So, Jamie's in the process of, or has already, released Kotlin 6, 0.6, so, I don't know if we wanna, if we're gonna do it today, if we wanna, like, you know, up that, or, or not.
**Jason Plumb** 54:27 That would be nice. Jamie, when's that coming? You think today?
**Jamie Lynch** 54:30 Possibly today, or tomorrow.
**Jason Plumb** 54:35 Okay.
**Jamie Lynch** 54:36 Yeah, I actually need to talk to you about that, the workflow's failing.
**Jason Plumb** 54:40 Oh, shit.
Damn it.
**Jamie Lynch** 54:43 Sometimes.
**Cesar Munoz** 54:43 Maybe, maybe, maybe I can do it, I can start it tomorrow.
If, you know, the content release is ready then.
**Jason Plumb** 54:53 I don't know that we should gate it on that, because it's just through semantic conventions, and I don't think there's… I'm not aware of anything that's important enough in there to block a release.
**Cesar Munoz** 55:02 Oh, okay.
**Hanson Ho** 55:07 Just release as it is. If it's not. I thought it might have been out already, but if it's not, then, like, yeah, don't worry about it.
**Jason Plumb** 55:12 Okay.
Okay, I… I mean, I can start it today, Cesar.
**Cesar Munoz** 55:19 Cool. Thank you.
**Jason Plumb** 55:23 I don't know if I'll finish it today, but I'll start it for sure.
**Hanson Ho** 55:26 If the workflow works.
**Jason Plumb** 55:28 Okay.
It will. Worked last time. I think I did Android… The weird secret thing I think I did for Android first.
So I'm bummed to hear it didn't work for Colin.
But that process is also tedious, so it's not super surprising to me.
Alright, I think it was a good discussion, everyone. Thanks, thanks for being here. Thanks for reviewing PRs. I appreciate the help. It's awesome.
**Ben Joseph** 55:57 Yeah, thank you, guys.
**Cesar Munoz** 55:58 Nope.
**Vishwan aranha** 55:59 Thank you, Grace.
**Cesar Munoz** 55:59 Thanks.
**Hanson Ho** 56:00 type.
**Jason Plumb** 56:00 Yep, bye.
