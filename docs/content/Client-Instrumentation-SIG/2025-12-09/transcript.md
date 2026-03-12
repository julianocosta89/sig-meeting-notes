SIG: Client Instrumentation SIG
Date: 2025-12-09
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/yrhso7Jv0jAtmSPG4RbliJ7cOGkD720U2bJCPz3QM3UQIkfHihHmA3rtnumsXsA6.3hSSsg6Tw_FpjP-n
============================================================

## Zoom Recording Transcript

**JP Jason Plumb** 00:53 Well, it's pretty quiet around these parts.
**Maciek Grzybowski** 00:57 Hey, Jason.
**JP Jason Plumb** 00:59 How's it going?
**Maciek Grzybowski** 01:01 Good, how are you?
**JP Jason Plumb** 01:03 Good, I think a lot of people are winding down for the holidays, starting to, at least.
It's pretty quiet.
**Maciek Grzybowski** 01:09 That's this part of the year.
**JP Jason Plumb** 01:13 Yup.
Haven't heard from Martin, who often runs this meeting.
Let me just double check.
We'll pull up the… agenda to see if there's anything on there, but I… I have low expectations.
**Maciek Grzybowski** 01:59 it's empty to what I see.
**JP Jason Plumb** 02:01 Okay.
Well, we'll just make a note that we tried.
**Maciek Grzybowski** 02:14 Maybe one question that… I have to… is… this SIG versus Android SIG.
If I want to stay up to date with Android from SDK development, perhaps Android 6 is the one where most things are going on, right?
**JP Jason Plumb** 02:32 Yes.
**Maciek Grzybowski** 02:34 Because I saw the past meeting some of the context being pulled to here, like, discussing some, like, high-level elements, the GA strategy, etc, for the Android SDK, although not much on the details.
What's your… what's your perception of this SIG client's instrumentation SIG versus the Android SIG?
**JP Jason Plumb** 02:55 Yeah, that's a fair question.
if Android stuff spills over into this, it's just because the agenda's light, and we want to keep people, who are interested in cross-cutting client concerns abreast of what Android's doing. If you want Android specifics, come to the Android SIG, for sure.
**Maciek Grzybowski** 03:13 It's true.
**JP Jason Plumb** 03:13 It's the one hour right before this, and it's every week.
we will… we definitely get into way more detail, and it's very Android-specific. This meeting is supposed to be kind of a coming together of people from Swift iOS, and from the web, and JS, and Android coming together, to talk about any of the, like, kind of common… Sorry, I'm getting… there's… Sorry, I'm getting notifications, and it's a flood. But I'm going to ignore them.
It's still happening. I don't know if you can hear it on your end.
**Maciek Grzybowski** 03:50 No, I don't hear it, no problem.
**JP Jason Plumb** 03:52 Okay, good. It's really obnoxious.
Hi, Wolfkong!
**Wolfgang Therrien** 03:59 Hello, hello.
**JP Jason Plumb** 04:00 How's it going?
**Wolfgang Therrien** 04:02 I'm doing well. I'm, subbing in for B today.
**JP Jason Plumb** 04:06 Okay, cool, cool.
**Wolfgang Therrien** 04:08 So…
**JP Jason Plumb** 04:09 We have a very light agenda. We're mostly just kind of discussing the relationship between this SIG meeting and some of the other, kind of more, area-specific or language ecosystem-specific.
**Wolfgang Therrien** 04:22 SIGs or groups, like the iOS Swift, the Android, and the web. They call it Browser now, browser SIGs. Yep.
**JP Jason Plumb** 04:30 And this is really supposed to be a place for us to just touch base every couple of weeks to see if there's activity in one area that might Support or conflict with, stuff happening in other areas.
**Wolfgang Therrien** 04:45 Yep.
**JP Jason Plumb** 04:46 Yeah.
**Maciek Grzybowski** 04:47 So, I think I found one, like, that there was a discussion started from us, from Databoc. I just put it into the edge, and it's about so-called events background.
out.
It's on… the screen ID, something is, basically, so it's clearly… It's clearly a common topic, I believe, between browser and… And Android. Also, I guess, SwiftSeq, I mean, not sure if any representative of SwiftSeq is joining here, but I think this could be something covering all, Client platforms, let's call it this way.
**JP Jason Plumb** 05:31 Yeah, so it's like, it's… so the intent here, I had not yet seen this, this is in the browser. That's interesting, so not… it's not really… Around semantic conventions per se, it's just, in browser.
They want… Something that's smaller in scope than session, yeah, that's what they want.
So we have some similar ideas happening in… Semantic conventions… wrong repo.
I think we have some screen stuff, so yeah, here's one idea.
**Maciek Grzybowski** 06:14 Hmm. And then here's a… what is it?
**JP Jason Plumb** 06:18 Those are not quite the same.
This is also not quite the same.
But this ask has come up before, I haven't seen it framed as breadcrumbs, but that kind of makes sense. In Android, we do have this thing called, Activity And it's kind of like a grouping of behaviors in, like, a topical area of an application.
So, like, if you imagine, like, you open your banking app, first thing you're staring at is, like, the login… activity, and if you get through that, then you're maybe staring at your account summary activity. And if you dive into one of your accounts, maybe you're seeing transaction activity, like, you know, that sort of flow.
there has been a request for something kind of like this, and we have something kind of like this on Android, but this is way more kind of specific.
**Maciek Grzybowski** 07:09 So, the activity thing, I think I saw it, because I played recently a lot with Android SDK implementation. I saw those funds that basically, like, highlight the activity lifecycle things, like on the resume, created, destroyed, etc.
And this, indeed, like, it's more like the ask to add common attributes across all telemetry that could be both signals, logs, and spawns.
So we can identify the instance of particular screen, meaning that… So we have, I mean…
**JP Jason Plumb** 07:39 You have to be able to make that differentiation from session ID, though, right? Because we have session, that's… that's something that gets tagged on all this data and allows you to tie it all together.
**Maciek Grzybowski** 07:48 Yes.
**JP Jason Plumb** 07:49 intent of session. But they want something more granular than session. They want something…
**Maciek Grzybowski** 07:53 Exactly.
Yeah.
**JP Jason Plumb** 08:01 Yeah, that's interesting. I didn't know that this was there. It's cool, though, and it would… that would be something, if this got adopted, it would be something that I think I think Android people would want this as well. We would want to make it… we'd want to figure out the difference between that and some other grouping mechanism. Like, we have this idea of… what I was trying to find is, like, some screen stuff, so we… We have a way to sort of determine what screen you're on, and there is some prior art in, In semantic conventions around screen, the idea being that… But maybe, I mean, this breadcrumb idea could span multiple screens, too, so breadcrumbs maybe is a little more generic.
**Maciek Grzybowski** 08:48 The way I see it… yeah, the way I see it, we have a screen name in Android, and that clearly identifies that the user is on, let's say, profile screen. But if the user visits profile screen twice, you can't differentiate between the first visit and the other visit.
So the breadcrum idea here is to be able to identify that those two screen names contribute… are coming from a different instance of the view, like, of the activity, let's say.
**JP Jason Plumb** 09:18 And then is it completely up to the application developer to decide when a breadcrumb is over? Like, when that trail stops?
**Maciek Grzybowski** 09:27 No, that would be… according to our idea, and this is, again, inspired by what we have in .com, that would be part of the instrumentation. So the instrumentation itself not only tags the, like, the event with the screen name, which is, like, great that it should stay.
But it also adds some sort of, like, identifier for this screen visit.
**JP Jason Plumb** 09:51 Yeah, so this is kind of touching on what I was getting at. Yeah, so it's already standardized, there is already a screen ID.
**Maciek Grzybowski** 09:57 Yeah. But I think they're thinking about supplementing it with some other stuff.
I think the call here for the upscreen ID is basically to adopt it in browser SDK. I think it's not adopted in Android.
SDK, I haven't seen that in the telemetry that I was inspecting.
So, solution here, like, quite common one, would be to adopt this on both platforms, and That would be… Nice, I would say, right?
**JP Jason Plumb** 10:30 But, like, something like browser.navID would not make sense on Android, though, right?
**Maciek Grzybowski** 10:35 Yeah, like… or we go with Android Navigation ID, but then we need to create a special type of event that indicates that the screen was… activity was presented, which is basically what we have with spans right now.
**JP Jason Plumb** 10:49 Right.
Yeah, it's definitely interesting and complicated. I don't necessarily have… solution for it. But I like this idea of breadcrumbs, I just don't know… Like, if it is… if it's intended to be pretty generic, then… I don't know when the instrumentation decides that a new breadcrumb begins, and if it's on… if it's when a screen changes, and I'm using that screen term generically.
**Wolfgang Therrien** 11:17 If that starts a new breadcrumb trail…
**JP Jason Plumb** 11:20 Is that really what everyone wants?
Because some people probably want a different breadcrumb trail.
And if it's not what people want, then isn't screen just enough? Like, if they want to be able to span across multiple screens with their breadcrumb trail.
then this would do that, but then how do you end it? Like, when does it stop?
**Maciek Grzybowski** 11:44 Yeah, well, one problem with current approach of having just a screen name is that we can't differentiate that this is another screen. Imagine this situation being on one screen, then entering another screen, but nothing happens on the screen, meaning we have no signal, no telemetry with different screen name, and then user comes back and does something yet again on the previous screen.
So, we clearly missed a screen visit in this… in this sense.
**JP Jason Plumb** 12:11 I'm not sure that I'm following you, can you… okay, so, I'm on screen 1, I navigate.
**Maciek Grzybowski** 12:16 industry.
**JP Jason Plumb** 12:16 there should be events that show those two things happening, right? Or at least the new screen appearing.
**Maciek Grzybowski** 12:23 Okay, okay, indeed, because the view instrumentation… send spawns, so we can see that some other screen was visited.
**JP Jason Plumb** 12:35 It should, and then if you go back, you should get a new event.
I think that's currently, at least on Android, I think that's part of our, activity instrumentation, is kind of what we expect.
We don't have, and, like, a big shortcoming is around Compose, which is an Android-specific technology for building UIs. It's really similar to React.
And, the definition of a screen, then, much like in React, like, what is a screen anymore? I have no idea. It's the same in Android, like, you're just swapping out elements all the time, and…
**Wolfgang Therrien** 13:13 Yo.
**JP Jason Plumb** 13:14 The very definition of a screen is weird.
**Wolfgang Therrien** 13:17 I… I think there's also maybe a little bit of an interesting nuance here for web, where, like, you can have the same web tab open multiple times.
And if you're rehydrating that session ID from, say, local storage or a cookie or something, like, all of those tabs will have the same session, but how do you differentiate between those individual tabs, right?
**JP Jason Plumb** 13:40 Yeah.
**Wolfgang Therrien** 13:40 You can't rely on session, and you can't rely on URL.
And so how do you… like, what is the semantic convention for doing that? I don't know that mobile might not have that same construct.
**JP Jason Plumb** 13:54 Yeah, I don't… I don't know much about iOS, but I can tell you on Android, I don't think you can run an app more than, like, multiple concurrently… I don't think… I don't think you can, and if you can, it's definitely an exception. Whereas, like, in the browser, of course, you're gonna tab all day long.
**Wolfgang Therrien** 14:13 And so that might be where it makes sense to diverge a little bit, and something like a document ID or a navigation ID for the browser namespace could… could make sense, since the concepts don't translate between platforms.
**JP Jason Plumb** 14:27 Yeah.
Yeah.
**Maciek Grzybowski** 14:37 One particular distinction on iOS, for example, is all these, splits… okay, split screen is one, like, one scenario, but I don't know if… if using app on split screen, is it running two instances of the entire process? Meaning, like, two different sessions ideas or whatever? But there are also all this concept of, like, master detail type of UIs, where you have some view controller on the left panel, let's say this is the menu with some, like, you know, hamburger, like, button, etc, and on the other side, you have details. Should this be… seen as one screen under one common screen name, or maybe a user wants to track two screens, one for the one vController, and one for the other vController. So, it's maybe a question also of how much granularity we want.
Between a screen. What we see on the screen, on the mobile screen, should it be under one screen name, or we want to enable users to go deeper into this? If we want to go deeper, then we have a similar problem to having multiple tabs on browser, right?
**JP Jason Plumb** 15:45 It's true, I'm kind of… I'm kind of classic in that I would, can I even do this? Like, if I, How do you do this?
You can make this pretend to be a phone, right? Like this thing? Oh yeah, here we go.
Oh, wait, I lost it, dang it.
I don't do this very often.
Okay, I'll just do that and pretend it's what I wanted. Right, so I'm gonna call this… I'm gonna say that I'm kind of old school in that, like, pretend this is an Android app and not a browser, but, like.
what I'm on now is, like, the issues screen, right? Like, screen… you have… like, if we're not talking about the actual… physical display on the device, then we're talking about something that's more abstract. And screen is abstract, but my… my concept of what a screen is, is right now I'm looking at the single-issue screen, right?
**Maciek Grzybowski** 16:43 Like, a user experience, so you're more.
**JP Jason Plumb** 16:45 Totally.
**Maciek Grzybowski** 16:46 the experience of the user rather than the technical detail under… yeah.
**JP Jason Plumb** 16:49 Totally, and the users of these RUM tools are often UX people, right? They want to better understand the user's flow and their journey through an app. And if I click this button here, no longer will I be on the single issue screen, I will be on the issues… the open issues list screen.
Or maybe just the issues list screen filtered to open. You know, there's two different ways of approaching that.
I don't even know how to go back anymore. I guess I used that back button. My point being, there's, like, you know, you could… even though I'm, like, adding a comment now, that doesn't mean that I've entered a different screen.
And there's some other operations, like, that might even put a modal on top of this, but I'm still on the same screen, and at some point, that, abstraction starts to break down, right? At some point, you can do enough on a screen that it no longer is the same screen. And that's just… that's where it gets complicated, but I think… For most apps, there's a logical kind of flow to different areas, and that's what a screen is.
**Maciek Grzybowski** 17:59 And if you open a menu, the side menu I saw on the top, you have this Hamper group button.
**JP Jason Plumb** 18:05 Oh, yeah.
**Maciek Grzybowski** 18:06 -Oh.
**JP Jason Plumb** 18:08 Yeah, I haven't left the screen, right? I've just opened the menu on that same screen.
I mean, that's the way I think about it. I think that's not… Too far-fetched.
But there could be UX people that disagree with that, and I don't actually know. I'm not… I'm not… that's not… I'm not an expert in UX.
**Maciek Grzybowski** 18:32 I get your point, and it's a pretty solid point, so I totally understand.
**JP Jason Plumb** 18:44 Well, it's good to know about this. I didn't… I hadn't seen this, because I don't follow this… this, repo, but it's good to know that this is happening, because if… if browser comes to some conclusion over here, we might consider something like that. I think… I'm trying to think if there's… I'm trying to think if there's an issue on Android that is, like, basically the same request, but with different words. Go ahead.
**Wolfgang Therrien** 19:05 Yeah. Is there something we'd like to bring back to the browser SIG? Because I generally go to the browser SIG, in terms of guidance.
**JP Jason Plumb** 19:17 I mean, I guess I have open questions, and that is, does… Does this, breadcrumb allow you to cross multiple screens?
And I think the answer's gonna be, what the hell is a screen?
I think. And if the answer is no, then I think you can just use screen. If the answer is yes, then my follow-up question is, when does this breadcrumb trail end? Right? If you're allowed to… if this breadcrumb trail continues across multiple screens and activities, or whatever we want to call it.
When does it end?
**Wolfgang Therrien** 19:48 Yep. I think there's probably two cases for that. Like, in the context of, I think, what Benoit, is talking about here, it's like a single document load or a single navigation. There can be lots of events in there, and grouping all of those together to be like, hey, this is your logical unit here, like, the instrumentation could know whether… when that starts and ends, and all of the activities that sort of are being tracked in there. I think if we're talking about it in terms of, like, a user journey, which is a very similarly shaped problem, obviously, auto instrumentation isn't going to know that answer, but I think for here, it is basically being able to differentiate, sort of, multiple tabs, and so that we don't conflate activities from different tabs in the same session, right? And so that we can also, so that we can scope those more appropriately. So I don't think it's about necessarily saying, navigate multiple subsequent navigations. I think session ID covers that. I think it's about differentiating, between Essentially, the browser being able to do concurrent emissions in the same session.
**JP Jason Plumb** 21:04 Yeah. Okay.
**Maciek Grzybowski** 21:10 That's…
**JP Jason Plumb** 21:11 I think you said that very eloquently, and I don't have a good way to, like, summarize it here, but if you want to, you may. I think it would be helpful.
**Wolfgang Therrien** 21:19 Okay.
**Maciek Grzybowski** 21:21 Jason, could you, could you link the, like, the, the, the similar thing that you found, in SAMConf record? Could you link it… Yeah, could you link it in a doc? I want to have a look.
**JP Jason Plumb** 21:31 That's true.
I'll just link these two.
**Maciek Grzybowski** 21:36 Yeah, of course. I don't remember which one.
**JP Jason Plumb** 21:37 you want, but…
**Maciek Grzybowski** 21:38 S.
**JP Jason Plumb** 21:41 Yeah.
And I think we… I think we might also have one in the Android.
And in case you haven't seen this, this new, Chrome feature that I stumbled upon accidentally, I was talking about this in the last meeting, I sometimes, while I'm reading, I'm like, I probably want to visit this, and I start clicking.
And then I realize, oh, I don't actually want to follow that, and if I release my mouse button now that it's pressed down, I'm gonna navigate to it, and the way to avoid that previously is to move your mouse cursor off of the link before letting go, but now in Chrome, if you do that, it starts dragging, and if you… if you're not careful, like.
It seems like it might have actually gotten better, but there's this thing where it, like, splits the tab now. Have you seen this?
**Wolfgang Therrien** 22:37 Oh, no, I haven't seen that.
It's wild.
**JP Jason Plumb** 22:39 It's not gonna do… oh, there it goes, yeah, look at this.
It splits the tabs. Like, it's still two tabs, but they're now, like, split screen with grouping?
**Wolfgang Therrien** 22:50 Oh, interesting.
**JP Jason Plumb** 22:52 I don't want to…
**Maciek Grzybowski** 22:53 think about the screen ID right now.
**Wolfgang Therrien** 22:56 Yeah, what is…
**JP Jason Plumb** 22:57 Exactly.
**Wolfgang Therrien** 23:00 My goodness.
**JP Jason Plumb** 23:02 Yeah, and I've only ever done that by accident, I don't think I ever want this. I mean, I guess it allows you to keep context here while reading, and if you have a really wide display, like, that's… maybe that's helpful, but… I usually just use Windows for that, you know? I just tear off a tab to a new window and put them physically side by side, and I guess people don't do that anymore.
Anyway. Also, which… is it… like, which one of these has focus? Can I tell?
**Wolfgang Therrien** 23:33 Oh, I guess that little icon tells you whether it's the left or the right side?
**JP Jason Plumb** 23:38 This little thing, yeah.
**Wolfgang Therrien** 23:39 Yeah, that's fine. What does that do?
**Maciek Grzybowski** 23:42 Can you… can you do more? Like, add more vertically, or…
**JP Jason Plumb** 23:46 I bet you can. Let's find out, I don't know.
**Maciek Grzybowski** 23:49 Yeah, I wonder on the icon, then.
**JP Jason Plumb** 23:56 No, it just clicked.
**Maciek Grzybowski** 23:57 Maybe 2 is the limit.
**JP Jason Plumb** 23:59 Yeah.
I mean, two's more than enough.
Anyway…
**Maciek Grzybowski** 24:07 Okay, so now you have windows, then you have tabs, and between tabs, you have, like… Talking more.
**JP Jason Plumb** 24:13 tabs, or…
**Maciek Grzybowski** 24:14 Good.
**Wolfgang Therrien** 24:15 Tap pane, tap group.
hands.
Yeah. It's like a journey.
Okay.
**JP Jason Plumb** 24:22 Anyway, cool, good discussion.
Light agenda, light attendance, if you have anything that you think about in the next two weeks.
Which I think butts pretty close to the holidays at this point, doesn't it?
**Wolfgang Therrien** 24:38 Yeah, I think it takes… 2 weeks will take, you're right to the 30th?
**JP Jason Plumb** 24:43 The 23rd. The 23rd, yep, nope, can't read a calendar.
But… I don't know if we're gonna be meeting then or not.
I assume it's on, and it will be about like this, so…
**Wolfgang Therrien** 24:55 Alright.
**JP Jason Plumb** 24:55 Yeah.
**Wolfgang Therrien** 24:56 Sounds good.
**JP Jason Plumb** 24:57 Cool.
**Wolfgang Therrien** 24:58 Alright.
**JP Jason Plumb** 25:00 Hey, well, it's good to see you. Thanks for the discussion.
**Wolfgang Therrien** 25:01 Yeah.
**JP Jason Plumb** 25:02 Feels good?
**Wolfgang Therrien** 25:03 Yeah, likewise.
**JP Jason Plumb** 25:04 Alright, take care.
**Wolfgang Therrien** 25:05 Fair.
