SIG: Browser SIG
Date: 2026-06-11
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 00:46 Jared.
**Jared Freeze** 01:16 Hey, what's up?
I can screen share and stuff today, Martin, if you like.
**Martin Kuba** 01:37 Okay, thank you.
At all again.
**Cleo Schneider** 01:57 Hello!
**Jared Freeze** 02:01 New faces, I'm pumped. Do you guys work with Martin?
Just hello again.
**Cleo Schneider** 02:08 We came to the client side, SIG earlier this week, so, I'm happy to give an intro, and I'm sure Brian is too.
If we're ready for that thing.
**Martin Kuba** 02:24 Sure.
**Jared Freeze** 02:24 Yep.
**Cleo Schneider** 02:27 Sweet. I'm Cleo, I work on Firebase at Google, and we are just getting our… our toes wet, in the hotel space, and we're… we're coming to some SIGs, we're gonna start, looking at some… some PRs and proposals, and… Hopefully… hopefully help, contribute.
So…
**Jared Freeze** 02:54 Very cool. That's awesome.
Always looking for more!
Amazing.
**Cleo Schneider** 03:02 Brian, I didn't know if you wanted to chime in, just so folks can hear your voice, too.
**Bryan Atkinson** 03:06 Yeah, my… this is my voice. I actually have, I actually have a topic now as well, but I can just throw it on the meeting, on the agenda.
**Jared Freeze** 03:19 Yeah, that's fine.
You know, link to the Google Doc, or are you good?
**Bryan Atkinson** 03:25 Yeah, I got it on there. Thanks.
**Jared Freeze** 03:28 Okay, cool.
David said he can't make it. Okay, we can get started.
Okay.
There we go.
Joaquin, are you ready?
**Joaquín Díaz** 04:12 Yeah, I can't use my camera today, I have to use the charging port for something else.
But yeah, I just wanted to ask you to take a look at this issue when you have some time.
This is after the discussion we had last week about sharing context within network and resource assignment instrumentation.
With the idea that on the new network instrumentations, we don't emit resource timing, since we already have a resource timing instrumentation.
And how we can solve the issue of, the resource type instrumentation not knowing about the network spans that we create, from Petch and XHR.
So, my approach was to… no, do anything new with the instrumentations, in the sense that I didn't want them to be, like, dependent on each other, or have, yeah, high correlation between them, so I just added a couple of callbacks.
And, like, that we have other instrumentations where we can change something when it's emitted.
And a callback to get the network spawn.
And what I did create is, like, a manager that works in between.
That just holds the network span context, and it has a function to get the current span based on the URL.
So yeah, my idea is to keep it simple. It's not really… hotel E, in the sense of, like, this manager doesn't follow any… like, current conventions or anything, but I think it's good enough for the SDK package that we are building.
Hopefully we can also export it to anyone just using the instrumentations on their own, but yeah.
Open to have a discussion there.
**Jared Freeze** 06:16 Yeah, Martin.
**Martin Kuba** 06:17 Yeah, Joaquin, I wonder, like, is this, Like, the resource timing events are emitted Usually after the span ends.
Does this, does this handle that?
**Joaquín Díaz** 06:34 Yeah, because… The first thing we do is we store the spawn We may do it as we create it, or as we end it, the network spawn.
And then there is a callback that runs on the resource instrumentation.
Right before we emit this bond.
And at the point, we should have this network span created, so we should have that in the context store to get the actual span and the URL.
So yeah, you should handle it. Yep.
**Martin Kuba** 07:06 Okay.
Do you happen to have a… do you happen to have this prototyped?
**Joaquín Díaz** 07:13 No, since we don't actually have a fetch instrumentation merged.
**Martin Kuba** 07:20 Oh, yeah.
**Joaquín Díaz** 07:20 But I can… I guess I can do something like a mock fetch instrumentation that creates spawns.
But, no.
I have some calling the issue, just sample, but I can't create a prototype based on some mock fetch instrumentation, I guess.
**Martin Kuba** 07:44 Yeah, I think that would be useful, just to, yep. Is that working, yeah.
**Joaquín Díaz** 07:49 Yeah, the…
**Jared Freeze** 07:51 Okay.
Awesome.
Alright, let's see.
Yeah, Martin, you have, network timing?
**Martin Kuba** 08:00 Yeah, so this is just on behalf of Serbi, who's been working on this for a long time. She has an updated PR.
In semantic conventions for this, I took a brief look.
I guess I'm trying to still figure out if this would… if this is something that we would want to use for resource timing, and so I would appreciate, you know, others in this… in this group to take a look at this, and And I think this probably will get merged, I just, like, the main question for me is whether we would want to use this for resource timing.
There… there's missing… so… so Serbi defined an event, so if you look at the… At the bottom, the events, on the model events.
So there is, Proposal to add this, network timing event.
I think we would need to… I think we would still need to… Yeah, no worries.
**Jared Freeze** 09:12 There we go.
**Martin Kuba** 09:14 Yeah, this… I think… I think we would still want to… Or we would need to still use our own event.
Because we have more attributes that we need to put on this.
But I guess the question is, could we reuse some of these attributes instead of what we have right now?
And would we want to?
**Jared Freeze** 09:45 Haven't really seen a suffix before. Is that… unusual?
**Martin Kuba** 09:51 Yeah, I have not seen this before either, I think.
I think it's… Was probably requested by… someone… from the Semantic Conventions group, because… to make it clear that these… Measurements are relative to… To the start of the, to the, event's timestamp.
So…
**Jared Freeze** 10:19 Okay, yeah, I think I followed up.
Gotcha. Okay, let's take a look at that.
**Martin Kuba** 10:26 Yep.
**Jared Freeze** 10:32 Cool. Yeah, Brian, you wanna…
**Bryan Atkinson** 10:35 Yeah, I was just wondering, so, and maybe, I don't… stop me if this isn't the right SIG to discuss this.
But, so there's this app crash event, and I'm wondering… If there is, is this an appropriate Type of event to write from a browser.
In the event of, like, an uncaught browser exception?
I think probably not, given that this is, like, talking about an actual app crash, but what I'm thinking, though, is that is there a need for there to be a browser error event that's modeled very similar to something like this to capture just an arbitrary browser error, uncut browser error?
Like, I know I found there's that in the instrumentation JS.
repository, I found there's, like, that.
Instrumentation web exception, handling.
Which looks like it's just writing… It's following, like, the exception semantic convention.
But to me, it seems like, from a browser perspective, there's a whole bunch of additional things, like, similar to what's shown in here for the app crash event.
That we'd probably want some common Convention to, to, to model.
And so, like, I'm wondering, Is this appropriate, if we're talking about, like, a web app?
or… Should we create some… browser error… event type.
In this, in this same, In the same vein as this PR.
**Jared Freeze** 12:17 So beyond, name, stack trace, message.
And I think, like, ID, do you foresee something… Something else that the browser would have that's not here?
**Bryan Atkinson** 12:29 Yeah, I think… well, I mean, basically all the browser attributes, so, like, the user agent, browser, session… and an app ID. Like, that is kind of one of the things that I've been wondering, sort of, outside of even the browser.
Spec here is that, like, there's an app resource type.
without any… ID associated with it?
**Martin Kuba** 13:03 So, so, we have, all the things that you described, like the, the… Browser attributes, like the user agent attributes, those are, also defined as resource attributes right now.
And they're sent as resource attributes.
The app ID, I'm not sure if it applies here, like, we do send service name, service name and service version.
I'm not sure what app ID would be here in this case, compare.
**Bryan Atkinson** 13:34 Okay, no, that actually answers my question. If service name is considered, yeah, but that's perfect.
But what I, what I… is… so, these browser resources exist?
But if we… if it's not encoded in a convention around, like, a specific, like, a browser error event type, and it's just being shown up as an ex… like, we have a convention for an exception event, and we have conventions, or, like, these browser attributes.
Is it considered following the hotel convention if every time, you know, a browser exception is… an uncaught browser exception is caught and, you know.
Sent up to the server.
Like, should it have… like, do we need to encode that it must have the browser resource attributes on it?
So…
**Martin Kuba** 14:28 Yeah, I mean, it's… it's not, it's not, like, required. It's… but, like, in the browser.
In the browser SDK that we're building, those will be default, default resource attributes that we add, and they apply to all of the telemetry, not just, not just errors.
Yeah, I think if you forgot to send those with the resource, that would be… obviously, incomplete telemetry, but that's not… I don't think that's… that's something that should be resolved on… On each of the individual, events, sorry, the, you know… signals.
**Bryan Atkinson** 15:12 Okay, so it sounds like there's… there is probably not the need for a browser error convention.
**Martin Kuba** 15:21 So my understanding here, the difference is that, the crash… is called, like, how Hansen was… Explaining the crash was being collected.
you know, with a different instance of the SDK than where it happened.
So, like, those… those attributes must be, I guess, added to the… to the event specifically?
Which is something that's exactly what Hansen is trying to… to address with this.
I don't think that it's… We don't have such a case or use case, like, where… there would be an error that would be collected later on.
I might be wrong, maybe there's some, like, experimental feature in Chrome, that, you know, for Observing crashes, like the browser actually crashing, or, like, the page crashing.
Not the browser, I guess the page would crash, or stop responding.
But that's not something we handle right now.
**Jared Freeze** 16:26 Yeah. So, yeah, Joaquin and I actually work with Hanson. We talked about this a lot when this came up. So, Crash… We had considered maybe, like.
you know, React render error, where the page goes blank, and we consider that crash. If the SDK's still available, try to use it.
That… it's not great, because… they're… the way they're using crashes, like, the process died, but they also, on mobile, have a container that does this. The only equivalent we could find on web is in browser extensions. Extensions can still observe the page.
that doesn't help us at all, right? Not… you know, that's fine for extension developers, but it doesn't mean anything to most people.
So that's why we just avoided the word graph, or exception. Also, the app namespace is… still TBD in general.
like, app for web app for SaaS versus browser. Which is really what we've committed to for, like, a lot of the things related to the document. So, like, browser.document.url.full, so url.full is kind of the convention, and we sort of tacked on this to differentiate between, like, the URL of, you know, a fetched resource versus the page itself.
So, we're kind of moving in that direction. Yeah, app is so overloaded. The other name they use is Widget, so this… we should probably settle this, like, sooner than later, to figure out which direction we want to go, but app.crash, I think, is not relevant to us, so… You know, I agree in a lot of ways.
**Bryan Atkinson** 18:02 Perfect, okay, thank you very much.
**Jared Freeze** 18:05 Yeah, I mean, and again, you know, if anyone can think of Crash.
In some other kind of way that's super relevant to the… You know, some customer that you have or something, just let us know, cause… We just didn't have anything we could think of, really.
Beyond the React area, so I think.
**Bryan Atkinson** 18:22 Right.
**Jared Freeze** 18:26 Okay, cool. Let's see, Martin, on behalf of David.
**Martin Kuba** 18:32 Yeah, so as, as, as… You know, David's been working on this SDK package, we've been discussing it.
I have added a review and asked for a few changes, and I think David addressed those.
So, yeah, if you have… if you can please take a look one more time, give it a stamp if you think this… it's… it's ready to go.
But I think we can probably merge it soon.
One thing that I wanted to point out is that it's… right now, it's being merged into a feature branch.
Because I think, we kind of anticipated that, there would be some… The review would take longer, and we would want to… collaborate on this, but if you feel like it's in a good state as is, then we could just ask David to merge it into main directly. I was wondering what you think.
**Jared Freeze** 19:31 Yeah, so I… just as a sort of experiment, added the SDK package as well, like the scaffolding, so package.json, the release, please, all that good stuff.
I was finding that if we do use this namespace for browser.sdk as the package name, and this is where the exporters are gonna live. We're gonna need way more folders than this. Like, I think just leaving, like, logs at the top is probably not the move.
I can put up my branch. I'm thinking now maybe what we do is fully scaffold it.
take it to main, maybe not in this PR, because there's quite a lot of code here. Take that to main, do not put it in any of the YAML files so it doesn't actually release, like, don't put it in CI and whatever, and then we'll just rebase this into that folder, and then people can start working out of this folder to start adding other things.
What do you think about that?
**Martin Kuba** 20:31 Yeah, that sounds good to me.
**Jared Freeze** 20:33 Okay, that way we just have a place to put stuff right away, that's…
**Martin Kuba** 20:36 Yeah.
**Jared Freeze** 20:37 basically empty.
So… Okay, I'll make sure and put that up, probably tomorrow?
I'll just pull out the exporter that I was experimenting with, and then we can go from there.
**Martin Kuba** 20:51 Okay, so, like, I'm gonna ask David to, to change the… to go to Maine.
And, yeah, if you can, if you can just, Approve, so we can merge it.
Or do the same.
**Jared Freeze** 21:11 So, are you saying, sorry, you want to merge this first if we get this approved? 2 main? This one?
**Martin Kuba** 21:17 Yeah, there's no… sorry, maybe I misunderstood.
**Jared Freeze** 21:21 Yeah, I'm just saying, we probably need to move all these files up a level, because they're not… namespace the way we had talked about using the SDK package itself. So, if we want to add a folder here, that's cool. If we don't.
We're probably gonna turn around and make another PR just to move this stuff.
I'm fine with… I'm fine with that, too. That's fine.
**Martin Kuba** 21:38 Yeah, I think a follow-up… follow-up PR is fine, too.
So…
**Jared Freeze** 21:42 Yeah, if it's not published, either way.
Okay, and then… yeah, Maxine?
**Maxime Quentin** 21:52 Yes, so I just wanted to, to know if, We would have more inputs about, mutable entities, and, If there were some tasks on it, like, that I could help.
Because the following, idea I had in mind was to work a bit on the browser URL, that full, browser.ur… the document.ura, that full, instrumentation.
And, I wanted to experiment a bit, on top of NGTs, so I wanted to know if… We would have some… Walk to do here.
Or if it's too early in the description.
**Martin Kuba** 22:43 Yeah, I think the latest is that, We were thinking about having the document being an entity, but we felt like the… The URL was… was not the right identifier for… For the entity, correct? So… I think we just need to… Make a decision here, like, what, What would be, like, if you want to… Introduce this as a… entity in the semantic conventions, like, what would be the identifying attributes for that entity?
**Joaquín Díaz** 23:19 Can we start by setting up?
like, the APIs to set the entities.
First, and then we can discuss how do we define the page view entity.
Like, I think the API that is proposed here works fine for sessions, so we can start with that.
And then, like, I don't think we should mix these problems, like, I think in here you are proposing an API, and I think the API is fine.
We can figure out later how we define the page view entity, which I think will take a lot of discussion.
**Maxime Quentin** 23:55 I agree.
Yeah, so I totally agree with that. I think the page view entity is a bit more complex, so maybe we should focus on session ID.
And as an entity, kind of… Third, and then we move to the next topic.
And for that, do you have a plan in mind, or… How could we… Start.
**Martin Kuba** 24:33 So, so, so one thing that, as, as far as sessions.
There is, implementation of session management in… in, JS Core.
That it needs to be moved to this repo.
But I think where it belongs to it, where it probably should belong to, is the SDK, so it's a little bit dependent on… that SDK package to be added.
Once that's… once that it is… once the session management is here… well, I guess you can, Yeah, then… Then, Bronito… Bronito, I guess, I think, I think all that work is probably gonna be in the SDK, to be honest, but, I might be wrong.
**Jared Freeze** 25:37 I mean, that's… that's where we have it. I mean, if… we would consider upstreaming some of our code. Yeah, it all lives there because of the… life cycle, like, we call it a manager. I think that… Might be a decent way to go, but, Yeah, definitely open to what others are doing as well.
**Joaquín Díaz** 26:01 So I guess what's… what's… do we need to, to, merge the SDK?
Package.
Or the SDK repo? Sorry, PR.
**Jared Freeze** 26:16 Yeah.
Thank you.
**Joaquín Díaz** 26:19 That'll wait up.
**Jared Freeze** 26:33 Okay.
Anything else?
I had, I had two other things open, they're still in drop, I'll bring them up in the next meeting, but I was still kind of hung up on instrumentation bass.
And I was thinking we could start moving exporters over, the console exporter, so I'll make an issue for that, but nonetheless, hopefully.
But yeah, the comment that's at the top of every single one of the instrumentations, it's like, hey, be really careful about instantiation. It's just kind of annoying, so if we're gonna redo it in this repo, I thought that might be a good time to do it before we get to any more instrumentations.
Okay, anything else? Anybody?
**Maxime Quentin** 27:24 All good.
**Jared Freeze** 27:26 Okay, sweet, we can wrap up there, then.
See ya.
**Maxime Quentin** 27:29 Thank you, bye-bye.
