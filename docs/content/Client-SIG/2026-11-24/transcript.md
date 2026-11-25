SIG: Client SIG
Date: 2026-11-24
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (Palo Alto Networks)** 01:13 Hey, Jason.
**Jason Plumb (Splunk Inc.)** 01:16 Hey, what's happening?
**Jared Freeze (Palo Alto Networks)** 01:18 Not sure where Hanson is.
**Jason Plumb (Splunk Inc.)** 01:29 Well, it's impossible to see in this lighting I have going on here, but let me try something, let's see.
**Jared Freeze (Palo Alto Networks)** 01:35 He just posted, we're canceling.
**Jason Plumb (Splunk Inc.)** 01:38 Okay. What's up?
**Jared Freeze (Palo Alto Networks)** 01:39 No one has anything urgent.
**Jason Plumb (Splunk Inc.)** 01:40 We've got the color scheme, but my team will never have that fancy thing on the side that yours has.
**Jared Freeze (Palo Alto Networks)** 01:48 That's not true.
**Jason Plumb (Splunk Inc.)** 01:50 It is true.
**Jared Freeze (Palo Alto Networks)** 01:53 You know what's funny about this, is when I was at the… when I was at Dodger Stadium, I went with a friend, and it was the last hat they had, and it was on sale, which is why I got it. It was, like, 20 bucks, so…
**Jason Plumb (Splunk Inc.)** 02:06 You're like, you're like, that's the best hat, and it's on sale, that's great. Yeah.
**Jared Freeze (Palo Alto Networks)** 02:11 So, I was pretty pumped about that, but
**Jason Plumb (Splunk Inc.)** 02:14 They have, I think they also have a Black on Black Mariners that has the, like, upside-on trident for M, like, it looks like an M, but it's the Trident.
**Jared Freeze (Palo Alto Networks)** 02:22 That's cool.
**Jason Plumb (Splunk Inc.)** 02:24 I probably need one of those, too. I didn't make it to a single game this year.
**Jared Freeze (Palo Alto Networks)** 02:28 No?
**Jason Plumb (Splunk Inc.)** 02:29 I mean, it's a trek, you know? I gotta… Gotta go up to Seattle.
**Jared Freeze (Palo Alto Networks)** 02:33 Oh, yeah, you're in Portland?
**Jason Plumb (Splunk Inc.)** 02:34 Yeah.
**Jared Freeze (Palo Alto Networks)** 02:36 Yeah, right, right.
Well, it's funny, I just got back from Perf now. Do you know what that is?
**Jason Plumb (Splunk Inc.)** 02:43 No.
**Jared Freeze (Palo Alto Networks)** 02:43 It's Performance.now, right? Which is the API for web to do, high-resolution time.
And it's a conference that's, like, all the web perf people.
And I was kind of the hotel guy.
**Jason Plumb (Splunk Inc.)** 02:59 Cool.
**Jared Freeze (Palo Alto Networks)** 02:59 For what it's worth.
**Jason Plumb (Splunk Inc.)** 03:00 Yeah.
**Jared Freeze (Palo Alto Networks)** 03:00 And so, they are now obsessed. So, I talked to…
**Jason Plumb (Splunk Inc.)** 03:04 That's great.
**Jared Freeze (Palo Alto Networks)** 03:04 Firefox, Chromium, Google Chrome Teams.
about moving OTEL up a level into the browser itself.
**Jason Plumb (Splunk Inc.)** 03:15 Awesome.
**Jared Freeze (Palo Alto Networks)** 03:16 as an export, there's something called the Reporting API, which you basically hand it a URL and a header, and it just fires off stuff.
Now, what it fires off currently is just errors that happen before a navigation, or, like, basically before an interaction. Okay. So it's kind of like an abandonment signal, which is, like, the one thing you can't get.
Because you need your JavaScript to be loaded to sort of act, right? And so, that was… that's the problem they were trying to solve, but I was saying, like, hey, you have this performance timeline with all this stuff on it, you should just send me everything I allow.
like, I'll give you a list of the types, and then whatever. And then that led to a conversation about, well, let's put everything on the performance timeline. Like, not everything in the browser is on the timeline.
you guys figure out memory, I'll do… I'll just start handing you stuff, you know, or whatever.
**Jason Plumb (Splunk Inc.)** 04:09 Super interesting, yeah.
**Jared Freeze (Palo Alto Networks)** 04:11 So what if there were no JavaScripts?
Like, none at all.
**Jason Plumb (Splunk Inc.)** 04:14 Yeah.
**Jared Freeze (Palo Alto Networks)** 04:16 Interesting idea. Cool. Yeah, OTLP at the browser, in the browser.
**Jason Plumb (Splunk Inc.)** 04:21 What's up?
**Jared Freeze (Palo Alto Networks)** 04:22 I don't know how updates and stuff would happen, but it makes this SIG, like, THE SIG, basically, for us.
**Jason Plumb (Splunk Inc.)** 04:30 It's cool to, like, to see them, like, getting more directly engaged, too, from those teams.
I don't know what the… there is still this separate, kind of, like, web SIG that I assume you also attend, right?
**Jared Freeze (Palo Alto Networks)** 04:43 For… for us, or for… for them, for W3C?
**Jason Plumb (Splunk Inc.)** 04:49 For open telemetry, like, there's still the web SIG.
**Jared Freeze (Palo Alto Networks)** 04:53 Yeah, yeah, I'm a browser maintainer.
**Jason Plumb (Splunk Inc.)** 04:55 Yeah, okay, so you still go to the… like, there's a… there's a browser SIG still.
**Jared Freeze (Palo Alto Networks)** 04:59 Yes, absolutely.
**Jason Plumb (Splunk Inc.)** 05:01 Okay.
**Jared Freeze (Palo Alto Networks)** 05:02 But the long-term plan is to… potentially not have one at all. Right. I mean, you'd still need something to collect clicks and things, but as far as the sort of auto-magic things we do with network and errors and all that stuff, that potentially would be just collected, you know, by default. And then… you know, my understanding of OTEL is admittedly not, like, deep, deep on context and things, but my understanding is that, you know, OTEL wants discrete data.
Like, not, like, partial updates and things. So that… that presents a bit of a challenge, depending on what you consider a session span.
Because, like, on the back end, you can sort of do whatever you want, and then close it, or leave it open for 10 hours, or whatever. On the web, you can't do that, right? Like, people leave all the time, they're switching tabs, they're coming and going. So, knowing when someone leaves and trying to get stuff out the door is actually a hard problem.
**Jason Plumb (Splunk Inc.)** 06:02 Yep.
**Jared Freeze (Palo Alto Networks)** 06:03 And so, yeah. Anyways, I'm trying to solve that as well, so, like.
what's good enough? You know, if you go idle for 3 seconds, can we just dump what we've got, you know? Or… you know, can that just be an ID that gets passed through instead of, like, a proper span? Like, can you just send the spans you've got, sort of thing.
**Jason Plumb (Splunk Inc.)** 06:24 Yeah, so I think you're speaking directly to some of the things we would want to solve with a session SIG. We need to have, like, a formal definition of what a session is, what its data model is, and the semantics, and how it… It's lifecycle, all of that stuff, and you know, I think at Embrace, you guys all model it as a span, like a long-running span.
At least I think I've heard that from Hanson and others, but…
**Jared Freeze (Palo Alto Networks)** 06:49 On the mobile side, yes.
**Jason Plumb (Splunk Inc.)** 06:50 Yeah.
**Jared Freeze (Palo Alto Networks)** 06:50 On the web, we actually do something closer to this, which is the session ID, and then we let the spans not have a parent, necessarily. Yeah.
**Jason Plumb (Splunk Inc.)** 06:59 It's interesting, so there, there is a spec proposal right now, because the spec meeting is, like.
before this one, and I've been… I've been going to that now that we've moved the Kotlin, or the Android meeting, rather, to Thursdays.
There is a s… back from, like, a week ago, I believe, if you review the meeting notes.
Someone has a proposal to send events at the beginning, and the beginning of a span, and then in that thing, it links back to some prior work about being able to send span, kind of life cycle updates for long-running stuff, because, you know, spans are not very well suited to long-running operations.
**Jared Freeze (Palo Alto Networks)** 07:38 Okay.
**Jason Plumb (Splunk Inc.)** 07:39 speaks to that, right? You could at least get an event that a span has started, and if it never ends, then you could maybe time it out in the back end. At least you got some indication that it had started, whereas The current operational model for OTEL is, like, you don't get the span until it's finished.
**Jared Freeze (Palo Alto Networks)** 07:53 Right, right.
**Jason Plumb (Splunk Inc.)** 07:54 So that poses certain challenges. Anyway, just mentioning that, because I know it's out there, and it… if and when I can ever find time to help bootstrap a session SIG, you know, it's been probably 3 or 4 years now in the making, but…
**Jared Freeze (Palo Alto Networks)** 08:08 Okay.
**Jason Plumb (Splunk Inc.)** 08:08 of time…
**Jared Freeze (Palo Alto Networks)** 08:10 Yeah, I think we're gonna need it pretty quick, because… we're… we solved this by… Sort of stitching later.
So, for web, at least, if you're visible, you have… you're… you basically have a session, we call it a part, that's a span, and it's… You know, discrete, like, in that it, like, collects… logs and has children and stuff, but every time you switch tabs, it closes itself and sends it out, and then at the end, so we have a session ID that gets, like, pushed through, but at the end.
you know, you may not get the last span, and we sort of call it good, because we're hoping we have, like, all this other data to just sort of, like, understand, like, what a person's intent is, but you're not really always seeing the whole picture, like, on mobile, right? Because on mobile, you have something, like, installed. Like, you have another opportunity, even after… do you guys call it A&R? Like, whatever the crash is.
you know, when they come back, you can sort of, like, tidy things up and send it out later in that sort of update. Like, I think we would want the same sort of thing, so not just, like, an on-start event.
But something that's, like, I'm holding this in memory, I send it later.
But I… I have some idea of, like, what that timestamp might be. I just didn't have time to do the networking.
Because on the web, you have to compress… And then send, and you only get one frame to do that. And the compression is a single frame, and then it exits.
**Jason Plumb (Splunk Inc.)** 09:45 Yeah, we had a… we had a contributor, from Webb, like, a couple years ago who's no longer involved in this project, but they were very, very, focused on reducing, like, payload sizes, and, like, not putting OTLP JSON on the wire for telemetry, because, like, it's too big, and these protobufs are too big, and… You know, having… a more, like, stateful, compact representation like Arrow is starting to afford might be an option, but that was definitely a point of contention. We on the mobile side, are a little bit fortunate, because we have local storage that we write telemetry to, and in the event of a crash, we just… It depends on the type of crash. I think best effort, we try and send it, but if we can't, there's this natural disk, like, through-disk buffering situation that happens, and so on next app start, we then siphon that data off.
**Jared Freeze (Palo Alto Networks)** 10:36 Okay, that's cool.
Yeah, I'm not Chiquita.
I'm not sure what the… what the sort of timing implications are, because I think our backend will accept stuff later, but…
**Jason Plumb (Splunk Inc.)** 10:48 There's probably a limit.
**Jared Freeze (Palo Alto Networks)** 10:49 Yeah, it's like… Do you care about a person that really… went to bed.
**Jason Plumb (Splunk Inc.)** 10:55 Yeah.
**Jared Freeze (Palo Alto Networks)** 10:55 And then came back, you know, or is that.
**Jason Plumb (Splunk Inc.)** 10:57 A boring session at that point, yeah.
**Jared Freeze (Palo Alto Networks)** 10:59 Yeah, so it's like…
**Jason Plumb (Splunk Inc.)** 11:00 crashes, I mean, that's interesting, right? Because, like, I feel like most people, if the app straight up crashes, they're gonna launch it again.
**Jared Freeze (Palo Alto Networks)** 11:07 Yes.
**Jason Plumb (Splunk Inc.)** 11:07 And so hopefully you get that data. This meeting's been canceled, by the way, we're just chatting.
Yeah.
**João Oliveira** 11:13 Hi, I didn't want to interrupt.
**Jason Plumb (Splunk Inc.)** 11:16 No, it's all good.
**Jared Freeze (Palo Alto Networks)** 11:17 No, it's really…
**Jason Plumb (Splunk Inc.)** 11:18 social and casual.
**Jared Freeze (Palo Alto Networks)** 11:20 Yeah, talking about sessions, but But yeah, I would love to see… oh, I saw the other thing, too, that span.type.
Got put through, that's pretty nice, because we are also… have an obstruction for that.
Cool. Yeah, so knowing the schema, I think that was actually one of the things that came up at the conference, was, like.
is this arbitrary? Like, how big is it? You know, what is it supposed to be? And the idea is that, well, if it's stable.
you know, hopefully, you know, you should be able to just say, this is the schema, and if it doesn't match, you toss it out, or whatever. But again, that makes it really important, right? Like, if Firefox publishes something.
you know, they can't be breaking, like, ever. Like, we have to really commit to the protobuf style of, like, you only move forward. Yeah. And so we have to be super careful. Like, it's… there is no experimental for them, so… I mean, they have gated flags, but then it's effectively, like, non-existent. Like, it would just be sort of…
**Jason Plumb (Splunk Inc.)** 12:18 Yes, exactly.
**Jared Freeze (Palo Alto Networks)** 12:20 So…
**Jason Plumb (Splunk Inc.)** 12:20 throughout.
**Jared Freeze (Palo Alto Networks)** 12:21 It's, it's the sort of import of your decisions, like, go way up, so…
**Jason Plumb (Splunk Inc.)** 12:26 Yeah.
I hear the…
**Jared Freeze (Palo Alto Networks)** 12:30 Yeah.
**Jason Plumb (Splunk Inc.)** 12:31 Alright, well, I'm gonna go hack on some non-related stuff.
Cool. It was good chatting with you. Yeah, have a good Thanksgiving.
**Jared Freeze (Palo Alto Networks)** 12:38 Yeah, you too. See ya.
**Jason Plumb (Splunk Inc.)** 12:39 Right.
**João Oliveira** 12:40 Exceeding this. Yep.
**Jason Plumb (Splunk Inc.)** 12:41 Yeah, take care.
Bye.
