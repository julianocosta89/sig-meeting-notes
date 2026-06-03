SIG: Android SIG
Date: 2026-06-02
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 02:14 Good morning.
**Hanson Ho** 02:18 Yeah, hello!
**JM Jason Morris** 02:20 I am.
**Jason Plumb** 02:21 Hello.
**Cesar Munoz** 02:43 Good morning.
**Jason Plumb** 02:46 Good morning.
Shouted, dude.
**Hanson Ho** 03:00 Just felt like doing that early in the morning.
But only if my first name.
**Jason Plumb** 03:29 Well, given how this got merged, I think the answer's yes.
**Hanson Ho** 03:39 The fact that there… The fact that they're based on the same YAML, and it's not bringing in additional API references.
Yeah, I think it's… it's a matter of taste, almost, so I think I like it.
**Jason Plumb** 03:54 Yeah, so Cesar and Jason, I think, weren't in the Kotlin meeting yesterday, so I'll just say it so they've heard it.
I had some concerns around… the packaging over in Kotlin, and maybe the fact that the incubating aren't in an incubating package, and they don't have incubating in the class names.
But I am starting to like the annotation, the incubating API annotation over there, and it seems a little more, Kotlin-ish, I guess?
And, you know, we will break… if we end up repackaging stuff in the Kotlin repo, then we will have to make changes in Android, but I think that's also fine. I don't think that those are… I don't think it's a huge deal to have to repackage. There's only, like.
I mean, you saw the PR was… I changed every semantic conventions reference in the project, and it, like, wasn't that big of a PR, so… Yeah.
**Hanson Ho** 04:48 Which in and of itself is not a great thing, but, you know, it is what it is.
**Jason Plumb** 04:52 The other one… so I'm going out of order here, but now I… you got me wondering, did… what happened with the semantic conventions?
**Hanson Ho** 04:59 Still not… are you talking about the…
**Jason Plumb** 05:01 So, I'm trying to get this through as well, because none of our events are using semantic conventions yet.
They all just have string constants.
So… and no one's looked at this yet. I'm gonna have to probably force this issue a little bit, but… So it's using Weaver to create these semantic convention events files, so, like… Oh, I don'.
**Hanson Ho** 05:26 Oh!
**Jason Plumb** 05:27 I don't know what a good one is.
succession, right? So…
**Hanson Ho** 05:30 These… these don't exist?
**Jason Plumb** 05:32 They don't. We have the string hard-coded in Android.
**Hanson Ho** 05:38 Oh.
Oh, no, sorry, what I mean is, those events are not bubbled up in a referenceable artifact.
**Jason Plumb** 05:47 Not anything we can consume yet. So, I was adding it to Java.
if this gets merged, then it's weird, right? Because we don't… now, after yesterday, we don't take… a dependency on semantic conventions Java anymore, so we'll need to do the equivalent in Kotlin.
In fact…
**Hanson Ho** 06:06 Yes.
**Jason Plumb** 06:06 This is unrelated to Android, but let me take an action item on this.
**Hanson Ho** 06:15 But… That's strange.
To me, actually, the fact that they are… exposed.
Until you're a PR. It feels weird.
**Jason Plumb** 06:27 I think it's kind of worse than that, because, you know, events can have attributes and stuff, and… what I think… where I think we went ahead, and for a long time, Weaver couldn't even understand the event syntax in YAML. Like, it just straight up could not understand it.
This is a step in that direction, but it's just a bunch of string constants, right?
**Hanson Ho** 06:50 Yeah, good.
**Jason Plumb** 06:50 What I'm also contemplating is maybe doing, Instead of just, like, using a template that creates a class like this, maybe creating a template that actually has methods for all of the attributes, especially required attributes, so that when you create an event, it's like an actual object that has first-class methods for all the stuff that's kind of required.
Or, like, a builder pattern, or some… I don't know, but there's… I think there's room to create, like, a very strongly typed, you know, data object with Weaver.
**Hanson Ho** 07:24 Yeah, there's no way to validate that the required attributes are there, or even reference them directly, right? You kind of have to, like, look in the YAML and know which ones to use, and then use them, right?
**Jason Plumb** 07:37 Yep.
**Hanson Ho** 07:38 Dude.
So it just seems events are not really supported in YAML, or in Weaver.
**Jason Plumb** 07:47 Yeah.
It just depends on what you want to do with the templates, I think. How fancy you want to get.
And, I mean, there are… there's maybe some limitations there also.
But this is… this is kind of nice, like, this is the way that you can filter out for events.
Took me a while to sort of stumble on that.
**Cesar Munoz** 08:06 I didn't even know about this syntax, so…
**Jason Plumb** 08:10 Yeah.
Yeah, you can do… you can do all kinds of crazy stuff with Weaver.
Alright, let's talk about the network change detection limitations. Let's see… I don't remember what this is.
Oh, I think it was… I think this fell out when I was doing… the semantic conventions change, and I was looking at… this class Right, we have the network detector.
which is an implementation of the interface, the interface method being detect current network, and it struck me that While this is nice, and it's worked fine for a few years.
It's a little misplaced, because phones aren't really just on one network.
That was the point I was making, was just that, You know, you can be on… a VPN on Wi-Fi while also being on 5G? Like, that's a very valid, common use case.
So I opened this issue for us to think about it, and just… I don't know, we don't have to necessarily hash it out on this call, but I think we… I think there's room to rework this to show better what networks, plural.
the thing is on, and I don't think we can stabilize this instrumentation. I don't want to stabilize this instrumentation until we figure that out, so… I open an issue.
**Cesar Munoz** 09:44 No, no, that… I think that's… that's fair, and I… I… It's been ages since I read the docs on networks… Android networks.
But I do remember the same that you mentioned, that the device can have Can be connected to multiple networks at once.
Now, what I… what I… Also, I do remember that there was, there was always a default network.
like, there was always… like, even though it's connected to both, you know, mobile cellular data and Wi-Fi.
the OS automatically chooses which one to use for all of the requests.
And… and… and that's the one that I think we're… We're capturing here.
I remember reading that it's not… it's not impossible to choose another network when you are making requests.
From your device, but it's, like, it's manual work, like, you're… You'll have to write some code to bypass the default network that the OS has chosen, so… It's a valid point, but I'm not sure how… How much of an issue it is right now.
You know?
**Jason Plumb** 11:06 I hear you. I'm not convinced that much… and I'm not aware of any thought that went into the ordering of this… Block right here.
And because we're only picking one, we seem to favor like, we seem to favor cellular over Wi-Fi, right? Because the first one wins here, in the win.
Right, because this has transport, I think it's probably just checking, like, a bit mask or something?
And so, if it has cellular, then we just return build cellular, and we don't continue, right? Because this is a win.
**Hanson Ho** 11:41 And it's very hard.
**Cesar Munoz** 11:42 Yeah, I haven't.
**Jason Plumb** 11:43 If they are on a VPN, and they're on Wi-Fi, we're certainly going to report Wi-Fi and not VPN. So we're kind of hiding the fact that they're on VPN, maybe, or we're hiding the fact that they're tethered, or whatever.
**Hanson Ho** 11:53 So, so… there being one network is probably okay, because that's the active connection, that the active network API is reporting. I don't think it aggregates all the connections it's got. Oh, okay. So, but… I think what it reports is actually one underlying network connection, and capabilities… so that code is weird, because it's looking for bit masks that are not mutually exclusive. So… you could be on a VPN while on Wi-Fi and on cellular. So, I… Unless Build Network… What, what does Build Network… Due. Oh, it's returning, okay. So…
**Jason Plumb** 12:42 Yeah.
**Hanson Ho** 12:43 I think there's… I think the logic is… I think the VPN logic is wrong. I don't think you can have a case where you get both cellular and Wi-Fi.
**Jason Plumb** 12:56 on the platform.
**Hanson Ho** 12:57 Yeah, so I don't think that's possible.
if you look at the active network, API, it's… it is… it is the current network, basically the one that… I think it's the same symbol as you would have, like, on your top of your phone.
**JM Jason Morris** 13:14 I believe it's the active network as potentially bound to the process, because there's also that whole side of things.
**Hanson Ho** 13:23 Yep.
**Cesar Munoz** 13:25 Which is kind of, like, chosen as a default one.
But it's like… The device, it's always, like.
My understanding is that it has those Radio's active still, it's just that it chooses which one to use.
For… by default, for requests, so… That's… I mean, you can technically… hack your way in into picking another network for your request, but it's a lot of work. I never had to do it before, so I don't think it's a common thing.
**JM Jason Morris** 14:03 There's also.
**Cesar Munoz** 14:04 I agree.
**JM Jason Morris** 14:04 fact that VPNs can define sub-IP ranges that they actually act on.
**Jason Plumb** 14:11 Oh, yeah.
**JM Jason Morris** 14:12 So they don't necessarily route all traffic, they may only route specific traffic over a VPN.
**Cesar Munoz** 14:20 True.
I, I also, I do, I do agree that having… VPN as a network.
option, like, distinct from, you know, Wi-Fi and cellular, it's kind of weird, because it's like… They're not, they're not exclusive, but… But yeah, at least when it comes to Wi-Fi and cellular, They do, it's something that the OS chooses, and there are actually two of them, or… you know, available. But the OS decides which one to use.
That should be the one that we… Get that imagery.
**Hanson Ho** 15:06 So perhaps there's… there's a, there's a matter of documentation and cleanup about what that actually means.
**Jason Plumb** 15:14 Yeah, documentation might be enough.
**Hanson Ho** 15:19 And frankly, the VPN thing is kind of weird.
**Cesar Munoz** 15:25 Yep.
**Hanson Ho** 15:26 VPN is orthogonal to the underlying… Connection that you have.
Yeah, it's like, it's like metered and non-metered and all that stuff. It's, it's…
**Jason Plumb** 15:39 Yeah.
**Hanson Ho** 15:44 there's a lot of stuff if you really, really want to get down to it, and most of it is not that useful, and may not even be correct, to be honest, on all OEMs.
Trying to be too fine-grained is…
**JM Jason Morris** 15:56 Yeah, I would say trying to be too fine-grained is a bit crazy, because… How do you deal with situations where the phone is actually on a tethered network to another cell phone that's actually on a cellular network? What network are you on now?
**Hanson Ho** 16:13 Exactly.
**Jason Plumb** 16:17 Okay, I feel like I've beat that dead horse a little bit.
**Cesar Munoz** 16:20 Is it fair to say that at least For, for starters.
Because I guess it all boils down to what's useful to know.
for our users. So, is it fair to say that, as a starting point, it's just fine to report either cellular or Wi-Fi.
And that's it.
**Hanson Ho** 16:47 Or no network.
**DavidGrath** 16:49 Yeah, I mean.
**Jason Plumb** 16:50 It would be interesting to note If and when we've ever gotten to this part of the win, I'm suspecting almost never.
Right? Like, you're almost always either on nothing, or cellular or Wi-Fi.
**Cesar Munoz** 17:06 Alright, in India.
**Jason Plumb** 17:07 If you're on those, then you're here.
**Cesar Munoz** 17:08 to add some things.
Alright, David?
**DavidGrath** 17:13 I'm not just about a peculiar case. I don't know if it actually counts, but It could be the case that your Wi-Fi could have internet issues, and then it will say it's connected to the Wi-Fi, but it's prioritized your cellular instead. I don't know if that's actually… I don't know.
**JM Jason Morris** 17:31 That is absolutely a thing, and it happens to me all the time.
**Hanson Ho** 17:36 Yeah, you have captive portals, basically, so you're on Wi-Fi, but you're not actually connected to the internet, but you also have an LTE connection or something like that. But if what you're saying is my internet connection is my Wi-Fi connection, you'll be connected to Wi-Fi, not connected to the internet, even though you have an LTE connection in the background. So.
**JM Jason Morris** 17:58 I personally have one extended on that. If my wired internet goes down, my phone stays on Wi-Fi, but routes… and routes all the internal traffic to the Wi-Fi network correctly, and all the external traffic goes over cellular.
So I can same time.
**Jason Plumb** 18:17 That happens… that happens to me with, like, public access points. Like, if you're out somewhere and you connect to an access point, and they haven't restarted their router in, like, 3 weeks, like, you can still connect to it, but they have no actual internet.
Yeah, that happens all the time.
**Hanson Ho** 18:32 What does the current network report, then, if you have, like, internal traffic being routed to one connection, and your external traffic routed to another connection?
**JM Jason Morris** 18:39 So for me, I get it as both Wi-Fi and cellular alongside each other on the icon bar. What it does, technically, I have never actually bothered to look.
**Hanson Ho** 18:51 Both on the icon bar. Interesting! I've… wow, but I think… I've only…
**Cesar Munoz** 18:57 There's a default… there's an API from Android that I… I don't remember the details, because it's been ages since I looked at it, that returns you what's the default network. And my understanding is that the OS will automatically decide to switch from you know, Wi-Fi, Wi-Fi for… to LTE, If it finds that the Wi-Fi doesn't have actual internet connectivity.
and you don't have to turn your Wi-Fi off or anything like that, but the OS will do that automatically, and then My understanding is that this callback that tells you which one is the default network should, you know.
she'll mirror that. She'll tell you, okay, well, yes, you have these connections active, but this is the one that I'm actually using. In that case, the LTE 1.
That's my understanding.
Unless I missed something.
**Hanson Ho** 19:52 So, with the new network connectivity callbacks, what you get is when a connection is established, you get a callback, and when it's connected to the internet, you get a callback.
So, in that case, maybe… I'm trying to figure out… because through the API, there's really no way of… Like, do you get, like, SSID or something that identifies the actual connection, through the current network API, or the active network API?
I mean, I don't want to rat hole on this, but, this… this is, This is interesting, in terms of, like, the corner case behavior of the simultaneous connections, and especially if packets are being routed two different ways depending on what process is calling it. Like, if it is bound to the process, I wonder if it has to be switched at that level, that… Even though some network is… some data is going through one, and some is going the other, at a process level, it's still bound to one.
**Jason Plumb** 21:07 Yeah, I was just tracking this down, but we do use those callbacks, right? I forget where they're set up, but it's probably in the network instrumentation.
**Hanson Ho** 21:16 Yeah.
**Jason Plumb** 21:17 Yeah.
**Cesar Munoz** 21:18 Yeah.
**Jason Plumb** 21:21 Alright, well, David wanted to talk about ViewClick. I think this is a good question. Are we done with this one?
**Hanson Ho** 21:27 Do we have an action item? What do we want to do with this?
**Cesar Munoz** 21:31 I think it opened.
**Jason Plumb** 21:32 I have the open issue, we can add some comments to it.
**Hanson Ho** 21:35 Okay.
**Cesar Munoz** 21:36 Yeah, I don't It's a great topic.
**Jason Plumb** 21:41 Yeah, like, complicated. Like, you just think about it, you're like, oh, a network, no big deal. It's pretty complicated.
**Cesar Munoz** 21:47 Yeah.
**Jason Plumb** 21:49 And there's no semantic conventions for any of that stuff, of course.
**Hanson Ho** 21:54 Would you have a quick report network connection? Your backend always knows what network it's connected to.
**Jason Plumb** 21:58 That's one in there.
**Hanson Ho** 21:59 goes down.
**Jason Plumb** 22:01 That's right.
**Hanson Ho** 22:02 And what do you import that as? Change events? That's probably actually correct, but, you know…
**Jason Plumb** 22:12 So the question is, do we want to keep this as view-click, right? Because a lot of this is maybe no longer clicking on a view?
Is that the main question, David?
**DavidGrath** 22:28 Yes, that's my question.
**Jason Plumb** 22:30 Okay.
**Cesar Munoz** 22:33 I think that's fair to rename it.
Makes sense.
And it's not stable yet, so…
**Hanson Ho** 22:40 Are we using any semantic conventions?
**Jason Plumb** 22:46 I don't know that view is in the name anywhere, but let's find out.
In the… I don't think it's in the semantic conventions, but let's see…
**Hanson Ho** 22:52 Because remember there's a tap.
**Jason Plumb** 22:58 Click… Yeah. Widget click. Screen click, widget click.
And then, you know, for double-click, it's the… it's the pointer, number of pointer clicks, We should maybe have…
**Hanson Ho** 23:16 Whoa.
**Jason Plumb** 23:17 We should maybe have, the types for these on the documentation, but I guess… maybe it's overkill, because we… it's one click to get to here.
**Hanson Ho** 23:27 I thought apps… yeah, yeah, these are… so AppScreen is semantic conventions, so that's fine. The HW pointerClicks, I don't… I don't recognize that at all. That's… that's not semantic engines.
**Jason Plumb** 23:40 I don't think so.
**DavidGrath** 23:45 Oh, yeah, that was something suggestion.
**Hanson Ho** 23:51 Yeah, I'm trying to figure out what does H… there's no HW…
**Jason Plumb** 23:58 Yeah, I'm guessing that's hardware. Hardware?
**Hanson Ho** 24:02 Sure, but there's no namespace for that.
**Jason Plumb** 24:04 Yeah, no, not yet, yeah.
**DavidGrath** 24:08 Okay, so the question is, yeah.
**Jason Plumb** 24:12 The question would be, if it's not… if we want to rename it to ViewClick.
We should probably do that as a separate PR, like, let's do your PR first, and then rename it separately.
So we're not kind of confusing two different work units there. And the rename is just gonna be… it's gonna touch a lot of code. But the question in my brain, then, is if it's not ViewClick, then what is it? Like, what do we want to call it?
**Cesar Munoz** 24:39 I think also David mentioned the, another option as, which is to… Move that code to its own, module.
If I understand correctly.
So it's about gestures.
**Hanson Ho** 24:59 Like, is the scroll, data or instrumentation in that same package?
Is that… is that what the flings and scrolls are in the same package as Click?
**DavidGrath** 25:14 Yes, I did them both at the same time, since they're similar.
**Hanson Ho** 25:18 Okay.
**Jason Plumb** 25:28 I like the idea of having a new instrumentation package called Gesture.
That's… I'm… I'm kind of favorable to that one.
**Cesar Munoz** 25:39 But is it specific for, scrolling?
gestures, if I understand correctly, right?
So maybe scroll? Scrolling?
**Jason Plumb** 25:51 A fling? Is a fling where you do, like, that long… that kind of quick let go thing? That's a fling?
**Hanson Ho** 25:56 Yeah.
To shorten.
**Jason Plumb** 25:58 Scrolling, yeah, versus scrolling.
I like the gesture encapsulates both of those.
**Cesar Munoz** 26:10 It's just that gesture is a little bit broader. Like, you can also call, I don't know, the pinching and things like that, gestures.
**Jason Plumb** 26:18 We don't have instrumentation for that yet, and that could be… when we do, putting those in ViewClick would definitely be wrong.
Putting those in gesture makes sense.
**Hanson Ho** 26:28 I mean, call… making… keeping view click means it's one specific, you know, gesture, versus if renaming its gesture, we could put, you know, all of them in there, if we want. So the idea is then, do we want one module per gesture, or one module for all the gestures?
And I feel like, given there are probably 5 or 6… Eventually, we may actually want renaming this thing, one module, and then having instrumentation, perhaps separately loaded, that defines each of them.
Seems… fine.
**Cesar Munoz** 27:08 Yeah, I think it makes sense to have a module only for gestures, that it's also open to new gestures in the future. I was trying to come up with a… With an example of why somebody won't want Wouldn't like to have Different kind of gestures instrumented with, you know, at the same time.
And, I just figured that it's just not possible for me to know that until somebody actually complains, so I think it makes sense.
To have a whole gesture generic package, then where we'll add more gestures in the future.
**Hanson Ho** 27:48 I think having one module makes sense, but each of them probably should be configurable, because you're basically adding, overhead. If you attach all of them and you don't really care. You generate data that you may not want, and you also, are listening for events and processing them that, that you eventually don't do anything with. So I think, in the instrumentation and configuration level, they should all be, Disablable or enablable, if default all disabled.
**Jason Plumb** 28:17 And we can add configuration for that later.
**Hanson Ho** 28:19 Yeah, in terms of packaging, I think it all makes sense in one. Like, I don't want to… have each gesture be included or excluded in the SPI, simply because, that's convenient to do it like that.
**Jason Plumb** 28:36 So, it might be… so, I guess the idea is that we would leave view click alone, and these new things, which are about scrolling and swiping and flinging.
we would put those in a new package. Presumably, there is some shared code that they will need to have, like, it looks like this is… Piggybacking off of some existing code, so we may need an internal common package for gesture-related stuff.
But I think that's what I'm hearing, is that we leave view click alone.
We make a new package called Gestures, or Gesture.
I don't know if plural is better.
I'd follow whatever pattern we have over there.
**Cesar Munoz** 29:16 I'm fine with whatever native English speaker people are comfortable.
**Jason Plumb** 29:19 I mean, fragment, singular, crash, singular, sessions, plural.
**Cesar Munoz** 29:24 Well…
**Jason Plumb** 29:25 There's no.
**Hanson Ho** 29:25 Gesture.
**Jason Plumb** 29:26 B.
Gesture. Yeah, I think gesture… Yep. And then, there may need to com- there may need to be an internal common module.
**Hanson Ho** 29:36 We may already have an instrumentation common.
Like, unless… unless that adds a whole bunch of dependencies that we don't want, having, like.
UI-common is okay too, I suppose, but…
**Jason Plumb** 29:52 We only have the common API, we don't have, like, a specific instrumentation common.
**Hanson Ho** 29:56 Really? Yeah. Okay.
**Cesar Munoz** 30:01 It's… it's another topic, but just to double check, that view click… instrumentation, it's only for views, or also… composable liquid.
**Jason Plumb** 30:11 Compose is a separate instrumentation.
**Cesar Munoz** 30:12 Oh, okay.
Got it.
**Hanson Ho** 30:15 The Compose thing looks at the… hooks into the Compose… thing. So it identifies composable, I think.
or the closest composable, or something like that, versus, I think, the view click is just whatever's on screen, tries to find the latest coordinate, and… Yeah, it's different.
**Jason Plumb** 30:34 Yep.
**Cesar Munoz** 30:37 Okay, I think we can leave that name then. Makes sense.
**Jason Plumb** 30:39 Okay, David, does that help you? I know we talked about, kind of, a bunch of different things, but hopefully that helps with that PR.
**DavidGrath** 30:47 Yes, it does, thanks. So I guess we'll do it after this one gets married.
**Jason Plumb** 30:54 Say that one more time.
**DavidGrath** 30:56 So, yes, it helps. So I guess we'll take care of the separation afterwards.
**Jason Plumb** 31:01 Awesome, yeah, sounds good.
And once again, thanks for adding these instrumentations, this is awesome, it's good to see these start to come together.
**Cesar Munoz** 31:10 Yeah.
**DavidGrath** 31:12 You're welcome.
**Jason Plumb** 31:17 Cool.
Is there anything else that folks want to talk about? And if not, we can do a quick cruise through the open issues and… See if there's anything new.
And I don't see any blue lines over here, so it looks like I've seen all of these.
**Hanson Ho** 31:37 Good job catching up.
**Jason Plumb** 31:39 Yeah.
Yeah, this would be nice to have. This got me down another rabbit hole as well, because I looked into what this might take.
And I did want… I think I called out in this comment just the difference between having an exporter that throws data away versus not generating the data at all.
And that led me to create this PR, which I think will maybe not get merged, I'm not sure, let's see.
So in core, in Java Core at least, we have these no-op exporters, but there's no direct way to get to it. You have to work around it by doing this.
You're like, compose me a span exporter of no exporters, and that will fall through to the no-op, or it'll effectively give you a no-op, and I'm like, that's silly. We should just be able to expose the no-op.
**Hanson Ho** 32:34 Correct.
**Jason Plumb** 32:34 what I tried to do, but I don't know if this will get merged.
We'll see.
We'll see.
**Hanson Ho** 32:41 in Kotlin, you try to configure a composite with no, we throw an ex… we error out.
Because you're like, what the fuck are you doing?
**Jason Plumb** 32:50 I mean, the effect should be no-op, probably.
**Hanson Ho** 32:52 Yeah.
**Jason Plumb** 32:53 Yeah.
**Hanson Ho** 32:55 The intention is weird, though.
**Jason Plumb** 32:57 Totally.
**Hanson Ho** 32:57 Especially if we can expose an OAP one, which seems perfectly reasonable, well, the intention becomes obvious.
**Jason Plumb** 33:05 Did we?
**Cesar Munoz** 33:06 Now, based on… Go ahead.
Well, I just was gonna add on then, I like the idea of having that no op.
Method.
It's just that I remember reading your, your comment, and… Well, I was just wondering.
Which, to me, is fine, it's just that having a no-op exporter still… I mean, it doesn't… It doesn't, I mean, it still does the stuff that you mentioned there, which is to…
**Jason Plumb** 33:40 Oh, yeah.
**Cesar Munoz** 33:41 Prior to that, it's still done, so…
**Jason Plumb** 33:43 You still get all the overhead and none of the data.
**Cesar Munoz** 33:46 Yeah, I… It's… I think it's fine, at least initially. To be honest, I haven't checked.
What could be a better option?
Maybe making… having no-up processors, which is a bit… Prior to that, but… But yeah, it's.
**Jason Plumb** 34:10 Yeah, it'd be, like, the tracer provider… I think you'd want, like, a no-op tracer provider, I think, and I think you'd want a no-op logger provider, and those would provide no-op instances of the tracer, no-op instances of the logger.
**Cesar Munoz** 34:25 Yeah.
**Hanson Ho** 34:28 So, this person is… has instrumentation that does these things, but they don't want that data.
**Jason Plumb** 34:36 This is what I was asking him, like, what component was even generating metrics in the first place? Because I'm not aware of any. They were like, yeah, we just want spans, we don't want any… or they just want logs.
**Cesar Munoz** 34:47 This one locks, yeah.
**Hanson Ho** 34:49 She'd be… yeah.
**DavidGrath** 34:50 I… Yeah, sorry, I think that OKHTTP generates client span duration, but I might be mistaken, I'm not too sure.
**Jason Plumb** 34:59 Okay.
**Hanson Ho** 35:00 I know, I know Servi has a PR that if you manually turn things on, it can generate metrics. But I think when we reviewed it, we were like.
We don't know if anybody would want this on Android, because it… yeah, you're talking about a whole fleet, and there's no way to disambiguate between devices. So maybe this person's turned it on.
**Cesar Munoz** 35:25 No, but I think it's a good point, because that instrumentation comes from upstream, and they do… they do like metrics, so it's probably the case… I haven't taken a look in a while, but it's probably… we're just reusing their… their SDK. So probably, if they added metrics, they're… I mean, they're there, and we… Haven't noticed.
**Hanson Ho** 35:47 But yeah, setting a no-op meter and a no-op logger meter provider, logger provider and trace provider seems like the correct thing. You just basically step it out, so you don't even go through the overhead of creating and storing all this stuff, just to dev null it, so…
**Jason Plumb** 36:05 Yep.
**Cesar Munoz** 36:08 So, are we fine with, like, if… Someone can find a way to provide no-op providers.
to… to then go ahead with that config option in the DSL. I guess that's the, Action item here.
**Jason Plumb** 36:25 Yes, and that seems like the best idea. There's not a direct path there today, but, like, if you use the… the old builder…
**Hanson Ho** 36:36 I'm surprised we create a default.
meter to begin with.
**Jason Plumb** 36:41 I know.
So if you use the builder, you can get… you can… you can get in enough to provide a tracer provider customizer, which can, you know, override any tracer, same with logar meter.
And once you get in there, you can just return no-op versions.
And then the telemetry just wouldn't be created at all.
And then it doesn't matter what exporters you have wired up, because they do nothing.
**Hanson Ho** 37:07 Is this the public API that they can have access to? Is this… or is this the…
**Jason Plumb** 37:12 Well, I mean, that comes back to the question.
**Hanson Ho** 37:13 How public…
**Jason Plumb** 37:14 do we want core to be, and do we really want people to be using this?
**Cesar Munoz** 37:19 It currently is… is public.
**Jason Plumb** 37:22 Yes.
But it's internal. We discovered that last time, remember?
**Hanson Ho** 37:28 I suppose what I mean is that the happy path that we suggest direct people to is this a configuration that's on it? Because if it's not, it probably should be, and we should probably create an issue for that.
**Cesar Munoz** 37:41 No, I mean, I think they were asking for adding scan of config options to the DSL.
Which is the agent's graphic.
**Hanson Ho** 37:48 Okay.
**Cesar Munoz** 37:49 Yeah.
**Jason Plumb** 37:50 Yep.
They were.
**Hanson Ho** 37:52 Okay.
But they wanted, export or configuration, right? But we're saying that we're going to offer a differing configuration that effectively does what they want.
**Jason Plumb** 38:04 Yeah, they were just saying, I don't want… like, they have… they're seeing failures in the exporter, because they don't have it configured. So it's trying to export metrics and traces, and it's just failing repeatedly, and they're like, how do I turn that on?
**Hanson Ho** 38:14 That, yeah, that feels like something that we should handle.
**Jason Plumb** 38:19 Agreed.
**Cesar Munoz** 38:21 Yeah, they just don't want that… those signals, so… the implementation details, I think it's fine, it's up to us. Okay. And I think that the providers are the best place, too.
**Jason Plumb** 38:36 Cool. Well, I think that's it for today, unless anybody has anything else they would like to bring up.
**Hanson Ho** 38:42 We are perhaps getting traction on the Google stuff again. I'm gonna ping Severin today. And hopefully, like, I don't know what the deal was, I don't know if they were in the middle of changing processes, but he got an email back from them saying, hey, we can do this now.
I'm like, cool, it's just been how many months now?
**Jason Plumb** 39:02 Yeah, do you have anything to show yet for that? Like, how are we gonna be able to see it?
**Hanson Ho** 39:06 It hasn't been done yet. Severn has to re-contact them, so.
**Jason Plumb** 39:10 Do we think that there's data, though?
**Hanson Ho** 39:13 I don't know. Okay. If nothing else, it'll be listed. It'll be listed somewhere. Whether we get data, I don't know. I… for… for Embrace… we've gotten a few crash predi… whatchamacallit, reports, but they're not new and insightful.
**Jason Plumb** 39:36 Okay.
**Hanson Ho** 39:36 But it is listed, so that side of it is good. It's not us getting data, it's them seeing, oh, it's in the Google Play, you know, verified SDKs or whatever, so…
**Jason Plumb** 39:47 Cool.
**Cesar Munoz** 39:48 Google is taking longer than semantic convention PRs.
**Hanson Ho** 39:52 I don't know, I don't know, I mean, I started that, like, a year and a half ago, and…
**Jason Plumb** 39:57 Where is that damn thing? Oh my god, I haven't looked in a couple of days.
**Hanson Ho** 40:02 It's been approved by 4 people, including, including, Oh, who was it? Somebody.
**Jason Plumb** 40:13 Lunmilla… I thought…
**Hanson Ho** 40:17 More?
**Jason Plumb** 40:17 wonderful.
**Hanson Ho** 40:19 Okay, there's probably more now, okay.
**Jason Plumb** 40:20 Yeah, this is new, okay, 16 hours ago, yeah, this is new.
**Hanson Ho** 40:23 Take a look.
**Jason Plumb** 40:24 She did approve it, though.
**Hanson Ho** 40:26 Yep.
**Jason Plumb** 40:27 Okay.
**Hanson Ho** 40:27 had approved it, but I'll take a look at this and…
**Jason Plumb** 40:31 These look all small, these are just, like, notes to brief changes.
**Hanson Ho** 40:34 Okay. Cool.
**Jason Plumb** 40:37 And…
**Hanson Ho** 40:37 Yeah.
**Jason Plumb** 40:37 They're all just, like, recommendations, but it… yeah, go through those, because I think it's very close.
**Hanson Ho** 40:42 Oh, never been closer!
**Jason Plumb** 40:44 A development crash.
**Hanson Ho** 40:47 And then I have to do another one, which was the actual interesting one, and then async as well, probably as a third one.
But that's… that's… that's, for the future. Maybe in 2028, we'll… we'll get it, so we'll see.
**Jason Plumb** 40:59 I really do want us to be thinking about semantic conventions across all of these, because we have a ton that are still bespoke.
**Hanson Ho** 41:08 100%.
**Jason Plumb** 41:09 Yeah, there's… I mean, there's just too many, like, I'm just gonna pick Fragment as an example, right? Like… We create a span with these names, like, really? We're still doing that? Yes, we are. Yes, we are.
**Hanson Ho** 41:21 Honestly, the problem is I don't… I think if you look at some of these, we would not want them to be shaped the way they are, and that will imply changing the instrumentation, as well as doing the semantic conventions, which, It's easier now, like, I think when I was starting this, like, getting the YAML, I had to, like.
hop… yeah, I have to, like, do a bunch of copy and pasting and stuff like that. Now, at least, it's easy.
So, one by one, this could probably be validated and then sent. But first, validation is… is… because obviously the… I would say the view instrumentation, or the view life… or, sorry, activity lifecycle instrumentation stuff, I don't… know if we want them to be as it is, proposes semantic conventions.
**Jason Plumb** 42:09 Okay, I think… but I also think we're fine changing it, if there's ways to make it better. Yeah, definitely.
**Hanson Ho** 42:14 Yeah. For sure, for sure.
**Cesar Munoz** 42:16 Also, for the ones that we are sure about, I think it's fine to open semantic conventions PR at the same time, given that, you know, just with one, it's taking this long, so just… just for those to run in parallel.
**Hanson Ho** 42:33 Like, there's a bunch of stuff, probably, that is relatively low-hanging fruit, like… all, like, the network change events, and, like, you know, screen orientation change events, a lot of things that Android effectively fires a callback.
those probably map decently to just events that are pretty simple. So, getting it in is a matter of, hey, does iOS have something similar? And if they do, what is the shape and all that stuff, but we can certainly start off with creating it.
With very simple, attributes in mind, and then adding to it, similar to the crash stuff.
But, of course, it… just takes time to find time to do it, and then have everybody kind of align on it, so…
**Jason Plumb** 43:20 Yup.
**Hanson Ho** 43:22 It's like I have 2 hours. What do I spend it on? Do I spend it on looking at the network stuff? Do I spend it.
**Jason Plumb** 43:28 Two hours! Oh, what a luxury.
**Hanson Ho** 43:30 If, if, if. Or, like, getting the DSL for adding no-op implementations to, to meter, well, to everything for configuration. Like, it's… it's, yeah.
**Cesar Munoz** 43:44 But I mean… It's also, like, any, any of us.
Like, she'll be able to create these, right?
**Hanson Ho** 43:51 Oh, for sure, definitely.
**Cesar Munoz** 43:52 If you… if you have, like… now, if somebody has a specific, recent… Not to go with one of those.
Then, it's probably, you know, worth… flagging it in the, I don't know, the Slack group, so that nobody creates a… PR for that one, specifically.
But for the rest of them, I think we can… like, anybody can just take a look at.
those PRs.
**Hanson Ho** 44:20 Yeah, definitely.
**Jason Plumb** 44:23 What's up with this lately? I haven't checked in on this in forever, but it looks like… Seems like it's probably still doing stuff.
**Hanson Ho** 44:30 Yep.
It's happening.
**Jason Plumb** 44:32 Okay.
They're releasing, they're at 2 already.
**Hanson Ho** 44:39 They're a bit different, though.
Because they're both an SDK and… they're, like, the language SDK and instrumentation. All rolled in one, so it's a bit… Yeah.
**Cesar Munoz** 44:50 Yeah.
I just wanted to mention that next week, I won't be able to join.
There's, there's an elastic off-site.
So…
**Jason Plumb** 45:00 Anywhere fun?
**Cesar Munoz** 45:02 It's in Madrid.
Yeah, it's fun.
And so yeah.
If, look, I mean, for you, Jason, who's also I know you work with other people from Elastic, so none of us probably will be able to join anything next week, so…
**Jason Plumb** 45:19 Okay, that's cool. Is it just Europe? I mean, you guys are mostly in Europe anyway.
**Cesar Munoz** 45:25 Is it… Tariq? Am I?
**Jason Plumb** 45:26 Is it in Europe?
Like, it's just… from Europe.
Yeah.
**Cesar Munoz** 45:33 It's in… it's in Madrid, yeah.
**Jason Plumb** 45:35 But is it everyone from Europe coming there?
**Cesar Munoz** 45:38 Oh, no, everyone from anywhere.
**Jason Plumb** 45:40 Oh, okay, cool.
Cool, cool.
**Hanson Ho** 45:44 Nice.
**Jason Plumb** 45:45 Alrighty.
Well, thanks for the heads up, and thanks for joining, y'all. We'll see you soon.
**Cesar Munoz** 45:50 Thank you. Bye. Bye.
**JM Jason Morris** 45:52 Bye.
