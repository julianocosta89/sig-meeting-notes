SIG: Android SIG
Date: 2026-03-10
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:38 Good morning.
**Hanson** 00:39 Hello!
**Jason Plumb** 00:44 Let's get this first cup of coffee going.
**Hanson** 00:48 It's technically 7 o'clock, so…
**Jason Plumb** 00:54 Yeah, is that what it says on your phone?
**Hanson** 00:58 Not my phone, I adjusted all my clocks, but my body…
**Jason Plumb** 01:01 Yeah.
**Hanson** 01:02 My body is feeling it.
**Jason Plumb** 01:03 Yeah.
**Hanson** 01:06 I get up at, 6.45, so it was extra hard the last couple days getting up, because I was like, ugh, oh yeah, it's actually 5.45, so…
**Jason Plumb** 01:16 I know, I know. I get up around the same time, a little earlier, but I snooze. Like, I know I'm gonna snooze, so I buffer a little bit.
**Hanson** 01:24 I used… I used to do that. Now… now the easiest thing to do is just, like, when it rings, just get the fuck up, or else I might… I might… Yeah. Yeah.
**Jason Plumb** 01:33 Yeah, I get it.
You got discipline. Hi, Cesar.
**Cesar Munoz** 01:39 Hey, Jamie.
**Hanson** 01:41 It's gonna be super confusing, when it comes to fall, when everybody changes time again, and we don't in British Columbia. So, I don't know how to deal with this, like, you know, switching time nonsense, but…
I'll have to deal with the nonsense, so…
**Jason Plumb** 02:00 Yeah, it's rough. Okay, I can share my screen. Yeah, it's, struggle's real.
That window? Okay.
Phew.
Cool, I added, just a couple of really quick things, and we can… we can talk about a couple of,
I think there's an open PR we should also probably talk about.
**Hanson** 02:33 So good at keeping up with my hotel notifications up until Tuesday.
And then… It falls apart.
**Jason Plumb** 02:44 Yeah, I mean, I'm in decent shape if I can get around 200.
**Hanson** 02:50 I wouldn't clear…
**Jason Plumb** 02:51 Yeah, I just need to clear it out.
declared bankruptcy, Start over.
Yeah.
**Hanson** 03:00 I partially did that last week, or was it the week before? No, it was last week.
So I cleared up my… so if you see replies from me about things, like, in November, or something like that, that's what I was doing.
**Jason Plumb** 03:12 Yeah.
I get it. Here's mine.
Here's mine.
I'm at 205.
**Hanson** 03:23 how you picked a very random number at 200, you're like,
Functionally, I can only get it down.
**Jason Plumb** 03:29 I had it in the, like, the mid-100s, I think, earlier.
In the week, or late last week, and yeah, this does, yeah, like, you know…
I have some stuff I should just not follow.
Anyway, cool, let's get started. So…
I, saw this issue the other day, only because I got a notification for it, because
it was flagged as stale again. It's been flagged stale a bunch, and I've reopened it once, because I thought it was worth, you know, talking about first. So let's talk about it first. This goes way back to 2023, if you can believe that.
**Hanson** 04:08 Ow.
**Jason Plumb** 04:09 how time flies.
And the idea was to be able to use time from an NTP server. You know, we do have this relatively new clock implementation, which apparently handles, you know, the…
Going in and out of sleep, or low power modes, and readjusting the clock.
By using the underlying Android clock.
Now, I know that these are separate, like, maybe solutions, but if they're the same underlying problem, the question I'm posing to you all is, do we still need this issue? Do we still want to do this?
**Cesar Munoz** 04:42 I think we should, yeah.
**Jason Plumb** 04:44 Yeah?
**Cesar Munoz** 04:46 I mean, this is… I guess it depends on the use case that
Our customers… well, customers, these users would like to… to go with.
I think this is key if we want to provide support for distributed tracing.
**Jason Plumb** 05:06 Which we do.
**Cesar Munoz** 05:08 So then, yeah, we… we need it.
**Jason Plumb** 05:10 So, let me ask you why or what this solves, because it's… I thought, naively, that mobile phones, mobile devices would get their time from
Gps.
GPS has time embedded in it, right? So they usually sync their time with GPS.
Like, for example, we had daylight savings time here.
Is it pl- I never know if it's plural, is it savings or saving?
I know one of them is wrong, and it upsets people when you say it the wrong way, so I want to know which way is wrong, so I can hire it that way.
**Hanson** 05:46 I think it's saving daylight, so I think.
**Jason Plumb** 05:48 Yes.
**Hanson** 05:48 savings. No, they like savings.
**Jason Plumb** 05:51 you know, your phone switches over, and it's not because some Android programmer put that into the OS, I think it just gets the time, like, it knows what time zone you're in.
And it knows… What time it is.
I don't know, maybe that's a bad example, I'm not awake yet, but, like, I think it just…
Syncs time by default.
**Cesar Munoz** 06:11 Well, yeah, that's my understanding as well. I'm not sure if it uses GPS, though.
But yeah, I think the OS has ways to get the proper time.
I remember reading once in the Android docs that
I think the OS uses an NTP server itself.
an Android NTP server, so… My… what if… now?
what I can tell you from experience is that
Oftentimes is not synchronized well enough, at least not for distributed tracing use cases.
Now, the reason why might be different ones, like, I don't know, maybe the sync that the OS
you know.
Performance is not… is not done as… as… as frequent as it should for this use case to work.
Or maybe, maybe… Yeah, maybe it's just that, it's just not done as frequent as needed.
But, it's usually a matter of…
maybe… because I think it's also not needed to be done as frequent as we need it for observability, because
For an end user.
The, the, the, the outcome is… is…
it's, like, they won't tell, you know? It's usually a matter of a second off, or something like that, or maybe at most 2 seconds, or something like that. So, regular users won't notice.
But, you know, 2 seconds in a, you know, HTTP endpoint call where you
Want to see, compare what's going on in the backend service versus in the client.
it's a lot, so that's why I think it's still needed.
**Jason Plumb** 08:04 So you've observed a drift up to, like, 1 second?
**Cesar Munoz** 08:08 Actually, an emulator, I remember once seeing a 10-second
Three? Bob, between the nades, right.
**Jason Plumb** 08:15 Between the time, sorry, between the time on the OS and the actual time?
**Cesar Munoz** 08:21 Yeah.
**Jason Plumb** 08:21 10 seconds, it's miserable.
**Cesar Munoz** 08:24 But it's an emulator, so maybe, you know, it's not that good. But even in real devices, it's about 1, 2 seconds, that's what I've observed.
**Jason Plumb** 08:33 Yeah, and even NTP, I mean, you're not continuously polling or constantly getting, it's just something you do once in a while to adjust your clock. Your local clock, like your OS clock, is like…
getting nudging closer, like, it doesn't immediately just set the time, it, like, it's… it's pretty fancy, right? Like, the way it works. And you can imagine that
minor adjustments toward correctness could be interrupted by low power modes and sleep modes and whatever else you do with your phone. So doing that adjustment gets more challenging when you don't have a consistent local clock.
If I make… if I'm making sense.
**Cesar Munoz** 09:10 I think I see what you mean. The… I think the ideal scenario
Is to fetch it once, cache it, And then, calculated diff.
Between what you got and the internal block of the device that's not tied to the To the actual…
You know, it's like an internal chronometer, it's not a clock, actually, it's just something that's running from the moment the device, was booted. Booted?
**Jason Plumb** 09:40 Yes.
**Cesar Munoz** 09:40 the right way to start. Yeah.
So, there are ways to make it work. I don't remember reading through the, spec for the SNTV.
Which is a simple NTP, stop.
That I'm using in Elastic, and…
They say that they recommend that the most frequent
You know, polling to be at least a minute, every minute, something like that.
Not… not shorter than that.
And I think the reason is because…
Like, you can cache it, and then you can use the internal chronometer of the device.
But that won't work in case there is a lip second.
Which is not common, so it's not like it's gonna happen every day, but if it happens, then apparently it can go a second forward, or even a second backwards.
In a minute.
And depending on the server that you're using, your NTP server, That might happen right away.
Or, sometimes that second is kind of scattered across like…
multiple minutes, which I think is what the Android NTP does.
So, ideally, in that case.
you should keep track of the NTP server more frequently, otherwise, you know, you might get tenths of seconds
off in a couple of hours. So things like that, it's like…
I don't know exactly what's the right… Cadence, but the, the point is that
For a use case that requires, you know, distributed tracing, maybe you do want to
Try to pull that information.
As much as possible.
**Hanson** 11:38 So, there's a couple of, I think, things to clarify. The interface for Android, the one that we typically use, is about the system clock. And the system clock is set by, various means. So a user can override,
It's usually synced up with the, I think, carrier. So what it… what you're getting is what the system, what the Android device is saying.
Now, that device might be lying for various reasons, explicitly because a user set the time wrong, or there's a drift. But it is what
the clock appears on the device sets, and that's the one we're using.
There's also, interfaces, on, so Jamie pointed to one, get current network time clock, as well as the GNSS clock, which looks at the, the, the, GPS, which is…
slightly different.
But at the end of the day, it is… well, first of all, they don't work for all API versions, so there's that. But they will be different than what the user will see in their, in their, in their UI, which we may or may not care about.
in the issue, Jamie pointed out… pointed to the, the clock interface thing that, that I proposed for the spec, which is, the last time I checked, people say it's a good idea, but they want a spec sponsor, so that's kind of being hung up.
If we have a clock, interface.
That'll be much easier for SDK users, or even ourselves, to provide an implementation. That is different, depending on what folks want.
So, we already do a clock lock.
I think for the Java SDK, when a span starts. So a span will never…
look at two different instances of clocks, or a clock adjustment during a span won't alter that span. Embrace does the locking, when the SDK starts, so all the time within the instance of the SDK is, consistent with each other.
So, if the… if what we want to deal with is internal consistency and clock blocking, we don't necessarily have to go with the fancier network implementation, just do that.
But if we want the time to be precise and exact according to the network or the GPS,
We could also do that, depending on, you know, versions. But the downside of that would be… that would be…
that may not be what the customer or the user is seeing. So…
I think it's one of those cases where, Choice is good.
And… Forcing one on customers, or rather changing what we…
force on customer… on our users.
requires the new alternative to be definitely better, and I don't know if the new alternative is definitely better. I think if we want to have that as our default, we should still have a way of allowing folks to go back to the other one, which goes into the interface thing.
If we have that, I think customers can provide their own implementation of the clock that they want.
As well. So…
**Jamie Lynch** 15:20 Yeah, I think one other thing to…
bring up is quite a lot of those interfaces.
Don't guarantee that you'll actually get a time back.
Like, the current network time clock.
Doesn't guarantee it. Same with GNSS clock, and you can have, like, GPS.
Like… But you don't always have access to GPS for various reasons. So…
I guess if we did use those, we need to fall back.
**Hanson** 15:53 Because those clocks are not guaranteed to do what?
**Jamie Lynch** 15:57 But you might not have.
**Hanson** 16:00 Like…
**Jamie Lynch** 16:01 any GPS data, for instance. So, like, you might not be able to get a lock on a.
**Jason Plumb** 16:06 Got it.
**Jamie Lynch** 16:06 of NIV spoofing going on in an extreme case.
**Hanson** 16:11 And also for lower APIs. So, basically, if, like, in 23, we can't get one of the clocks, we have to fall back to the other clock. So, the time that we're showing varies…
it depends on a number of, factors. So if you see a timestamp, you don't actually really know,
what it is.
**Jason Plumb** 16:35 So, I wanna… so, the root cause here, right, let me make sure I understand this correctly, Cesar, when this was filed originally, what we were thinking about is that if you have an Android device roaming around in the world, and you do something, and it either initiates or takes part in a distributed trace, for whatever reason.
It's possible that when you're looking at the trace in a observability product, an observability product, that you could see that the service that was invoked
the start time of its span is before the start of the client span. Like, if you were off by a second.
**Cesar Munoz** 17:12 Yeah. You looked at a waterfall, tracing waterfall.
**Jason Plumb** 17:15 you could see that the span started before it was invoked. That's the… that's the main thing we're trying to solve here.
**Cesar Munoz** 17:22 Yeah, that can happen, and the opposite as well. Kinda looks like it started way after.
The client's found or something.
**Jason Plumb** 17:30 Yeah, there could be a gap, yeah.
**Cesar Munoz** 17:31 So, making it look as though the servers took forever, or something.
Or maybe this is a workaround. I think I… yeah.
**Jason Plumb** 17:41 Yeah. This kind of confusion can happen with trace waterfalls.
Yam.
**Hanson** 17:46 I think… I think it'll be difficult
For mobile devices, just by the very nature, to be…
to participate, in a distributed trace other than, like, the parent. I think it could be… if it generates a network request to a server, and basically that kicks off a distributed trace, I think that's a reasonable scenario.
Going the other way, with a mobile device being just, you know, a node and then going back.
I think that the… the…
It'll be difficult for that span to get to the network, get through the network to the collector in time, and…
The, the, the, the sync will be… Much less…
trustworthy, because of, you know, all the issues that we talked about. So…
I think we can improve, certainly, from where we are right now, but to get to the point where
There is no drift, or the drift is insignificant, will take a lot of work.
And I… I'm not sure if people are…
clamoring for it. They're almost… like, I would think that if you have a mobile piece, or, like, an user-facing app piece as part of a distributed trace, you almost think that data is somehow untrustworthy in some ways.
So… if… What we want to do is to kind of…
figure out whether the data is trustworthy or not, we could do certain things like get, like, the network time, or the GNSS time, and slap it on the telemetry as, you know.
So we can… offsets can be calculated, from what the time we think it is, so internally it's consistent, and then we have, like, another timestamp here that says, hey, if you compare these two timestamps, it should be the same timestamp, but their drift is off by 2 seconds, and you could do some math to kind of do the calculation.
Kind of one off.
But it'll be possible. But I think solving the distributed Trace case is gonna be…
it's gonna be really involved with, I don't know, with… Low utility, relatively.
**Cesar Munoz** 20:08 Low utility.
**Jamie Lynch** 20:10 I think… I think a reasonable step here might be to… Default to using…
One of these two clock implementations to get the initial start time, and then locking that against the,
what's it called? The elapsed time in milliseconds, the monotonic clock.
Because then you don't have to deal with the complexity of
the, like, GPS not being available.
And it's unlikely to drift a large amount over like.
**Jason Plumb** 20:45 So…
**Jamie Lynch** 20:45 On a client app.
**Jason Plumb** 20:46 Are you… sorry, are you suggesting that we just replace this with a different clock to compute our baseline?
**Jamie Lynch** 20:54 Yeah, basically. Or you could default to that if we're not able to get a time from one of the other
Saul says.
**Jason Plumb** 21:03 Sure, but so, that implies that whatever source we're hitting
is available and accurate. I guess if it's NTP, right, you could, like, say NTP server.giveme the current time millis or whatever, and the client is fancy enough to account for network offsets or whatever, and we get a pretty good baseline then. And then…
Does this… does this call also account for drift?
**Cesar Munoz** 21:30 Nope.
**Jason Plumb** 21:31 Like, if your operating system is drifting and it's correcting itself over time, does this not account for that?
**Cesar Munoz** 21:37 No, that's just a chronometer.
Put, like, a timer to start it when the device boots.
**Hanson** 21:43 And I don't think we could… I hope we don't expect drift within the SDK instance, like, that short amount of time. Like, if anything, it'd be an explicit change from the user, saying, oh, I've connected to a new network now, and the new carrier's saying, my time is this. So that change is more likely.
But if it was…
**Cesar Munoz** 22:03 It's not… you don't get the time from the network, you get it from the NTP server.
So that's… that's… that's a single thing. It's like, it's not relying on which network you're connected to.
**Hanson** 22:17 Right, so I…
what I'm saying, what's happening here, with current time is based on the device time, and that device time is based on, usually, the carrier. So it's an indirect update, I suppose. But if we swap this out and say, you know, we explicitly hit a server, that tells me the time.
Which we could do with both the GNS clock as well as the network time.
We'll be able to get a more accurate time, sometimes. But that will be different than what the time the user sees.
**Jason Plumb** 22:52 It's also more accurate in terms of, like, reality on a wall clock. Like, if we go hit an NTP server, and we set our clock based on that, and we're doing that, say, once a minute. Like, if the guidance says that hitting NTP once a minute is enough to sort of keep your clock…
Carefully adjusted, even in power savings mode, sleep mode, whatever.
Great, but we have to also account for any drift that comes back from… that NTP server, right?
If we're hitting it once a minute, sometimes we're gonna be hitting it and thinking it's 61 seconds, and sometimes we're gonna be thinking we hit it in 59 seconds, if we're changing our clock based on the results of that NTP call.
that drift, whatever change there is between what our clock currently has, before we made the NTP call, and the time that we get after the NTP call, any delta in that, or unexpected delta.
is going to play into the duration of any span that might be active. Because if we started under one clock baseline and we end under a different clock baseline, then the span duration is not accurate.
We might be more wall accurate, but we've changed the clock under the span. I think that's the… I think that's a problem.
**Hanson** 24:11 So, I…
**Cesar Munoz** 24:12 That's a problem… that's a problem when there's a… when there's a leap second.
And.
**Jason Plumb** 24:18 I think it's a problem all the time.
**Hanson** 24:19 If we adjust the baseline, we could change the duration of the span, if the baseline is adjusted during the course of a span having started, which is why,
the SDK locks the clock, and the Embrace SDK locks the entire SDK clock. It's more important to us that it's internally consistent than it is consistent with, like.
real life.
So if we do choose a different hidden NTP server or use one of these APIs, I think we should still lock it at the beginning, at the very least beginning of a span.
But probably, at the beginning of the SDK too, because the internal consistency, I value much, much higher than consistency with the rest of the world, given there's already, like, you know, a fungible, you know, gray area of drift.
**Cesar Munoz** 25:10 That's fair enough. I mean, internal consistency, and that's why I mentioned at the beginning of the meeting that it depends on what we want to provide.
Of course, internal consistency is all you need if you don't care about distributed tracing.
Because it's like, you're just trying to find out what's happening in a single device.
As if it were in a vacuum, or something like that.
But then, you know, when you involve HTTP calls and stuff like that, I know that
for a lot of people, it's just gonna be confusing to see, you know, I'm seeing this trace waterfall.
And it sounds like, it seems like, you know, my backend service is taking 2 seconds, or 2,000 milliseconds.
Which is usually what you see in these trace UIs.
To… to provide a response, or something like that. And it's not that, but it's just that the…
time from the client was 2 seconds off, or something like that, so…
I would say, I mean, if that's an important use case, then that's why I think it would be nice to have more accuracy in the time.
The, it's not an easy task, for sure, and definitely there will be cases where there's no way to get the more accurate time.
And for those cases, I think it's fine to fall back to something like we have right now.
But I think the times where it's not possible to get the accurate time, especially if you're involved in an NTP request, which requires internet.
Which you should anyway have in order to export your telemetry data.
I don't… I don't think it's gonna be that… you know, Common for it to fail.
So, I mean…
Yeah, it will be our best effort in a still, but I think it's worth it if we want to provide
Distributed tracing use cases.
**Hanson** 27:16 I think if you want to look at duration.
doing diffs of two timestamps generated from two different places is gonna be,
Especially when you don't have to, because we actually have the start and end time of the span from the client perspective, and we also have the server traces. So, if we want to compute a delta of, like, you know, this is how long from the client's perspective it took, and this is how long from the server's perspective.
there's internal timestamps for us to calculate, too. So, I don't… I don't think we'll ever want to, like.
look at the start timestamp of the client trace, and then look at the end timestamp of, you know, of the backend, and then do a diff. I mean, I think if we want to do it.
We could, but we should probably…
make it very well known, what we're doing, and allow customers or users to override this. If we have a clock interface there, if you… Jason, go back to the implementation.
**Jason Plumb** 28:23 Yeah.
**Hanson** 28:24 If we're not doing system.currentTime, it basically says, you know, hotelClock.currentTime.
And then otoclock.elapse time, or whatever.
then,
we could provide that implementation, whether it's this, NTP-based clock, whether it's a GNSS-based clock, whether it's one that falls back, then we can configure it at that level.
Instead of having it hard-coded in here.
So…
**Cesar Munoz** 28:59 That sounds… that's an option.
**Hanson** 29:00 We could do it. Like, I mean, one thing to do, I mean, if you want to do this right now, is to create a clock instance based on the Java clock instance, or interface.
Because there is an OTel clock interface, it just happens to be in the SDK, package. And implement it, like, that way within the Android SDK. And, you know.
do this, because we can probably still do this without the interface, it'll just be… it'll just be, something internal to the SDK. But then we can internally provide the original one, which is system, or this alternate implementation, and kind of shove it down here.
Which would be fine.
**Jason Plumb** 29:42 Cool, so coming back to my original question, like, do we still need this issue? It sounds like yes, it sounds like we're not ready to close this, so let's keep it open. I will…
I don't think we have a better means of, like, not auto-closing stuff that we think is worth keeping around, other than unticking stale on it after a while.
**Hanson** 30:01 It's good, because it forces us to have this discussion. So…
**Jason Plumb** 30:05 Yeah, I mean…
**Cesar Munoz** 30:07 food.
**Jason Plumb** 30:08 We could… we could consider…
another label that's, like, not stale, and then the bot just ignores it, but we, you know, we'd have to build that. I don't know how important it is.
**Hanson** 30:19 That… but the not stale can also become stale.
you know, like, this, this, this went stale, is… the bot did the job, I think.
**Jason Plumb** 30:28 It did, yeah, yeah, but if we decide that an issue or a PR is sticky enough that we want it to not go away, which is… I don't know if we've concluded that here, but, like, if one were to conclude that, then we don't have a means of doing that, that I'm aware of. We could build it.
But, I don't think we have it yet.
**Hanson** 30:46 You say, bump.
**Jason Plumb** 30:48 Yeah. Okay, sounds like we… sounds like we do want to continue talking about it, and…
Okay.
I did want to also leave time to talk about Cesar's PR.
In a slightly… Higher speed… Back and forth. This one, right?
**Cesar Munoz** 31:13 Yeah.
**Jason Plumb** 31:14 So we've had some good discussion on this,
I read your comment at the end of the day yesterday and have not digested it yet, but let's see, so…
Right, this is about installation context and the instrumentation API, which we're working toward, slowly toward, stabilizing.
Right.
**Cesar Munoz** 31:35 Yeah.
**Jason Plumb** 31:37 And the current state of affairs, like today, if a user builds their own instrumentation,
There's currently no way for them to install that using the agent, am I correct?
**Cesar Munoz** 31:53 Well, you… no, no, yeah, correct.
I mean, it's possible to install it, but it won't be… Aligned with the agent.
Context.
**Jason Plumb** 32:04 So making an instance of installation context today, which is required in order to call install.
Is that possible from the user's perspective? Like, is this class available to make?
**Cesar Munoz** 32:19 Yes. It's public.
**Jason Plumb** 32:22 But the fields that go in there are not necessarily available.
**Cesar Munoz** 32:28 I don't expose those from the agent, no.
Well, only open telemetry.
**Jason Plumb** 32:35 Right. And presumably they have the context, because they're the app, right?
**Cesar Munoz** 32:40 Yeah, they should be able to get it.
**Jason Plumb** 32:41 Okay, so ignoring these two, they would have to figure out the clock and the session provider.
The session provider is not exposed. The clock… they…
could maybe create their own instance and use the same one, but whatever, that's, like, unnecessarily complicated. Okay.
So, I just wanna… I'm talking through this issue out loud so that we're… I'm making sure…
on a different page. Okay, so to solve this problem of a custom user instrumentation class not being installable.
is solved in one way by this PR. There's a couple of different ways to go about this, but in this case, we add… wait, I think it was just there. Yeah, we add an install method on OpenTelemetry Rum.
**Cesar Munoz** 33:33 Yeah.
**Jason Plumb** 33:34 And that…
takes a new instrumentation and calls install on it with a context that it has created, because it has all these parts available to it. And then it has to…
Added to a list of… mutable list of instrumentations that it tracks.
So that it can shut them down at shutdown time.
So far, so good, we're aligned. That's what the.
**Cesar Munoz** 34:00 Yeah.
**Jason Plumb** 34:01 suggesting.
**Cesar Munoz** 34:02 The most important part of this approach is line 50, where we will create installation context
On behalf of the user, so that they don't have to.
**Jason Plumb** 34:14 Yep.
And then the implication that I think I called out was that this install method now in OpenTelemetry Rum, OpenTelemetry Rum being the main thing that users care about, right? They call… they call build or build, or in our case, they call agent initialize, and what they get back is an instance of this, OpenTelemetry Rum impulse.
Covered by an interface.
**Cesar Munoz** 34:38 Yeah.
**Jason Plumb** 34:38 Now that they have that, they can pass that to their dependencies, they can do all kinds of, like, manual tracing, manual stuff.
And they can also now call install sometime later, potentially hours later, they could call install on new instrumentation of their own design, or from third-party packages, or whatever, right?
**Cesar Munoz** 35:00 Yeah, that's possible. The API allows it.
**Jason Plumb** 35:02 Yeah, yeah.
So, I guess one of the questions I raised, and I don't think we have a good answer for yet, is, is that something that we want users to be able to do? Should they be able to, at any time.
Install instrumentation.
Or is it something that we want pinned at agent initialization or SDK startup?
**Cesar Munoz** 35:29 I think it's something we haven't discussed.
**Jason Plumb** 35:32 But right now…
**Cesar Munoz** 35:33 The way it is, is the former. Like, they can already…
do so. So, if we decide…
**Jason Plumb** 35:40 Well, kind of, right? But they can't create one of these.
**Cesar Munoz** 35:44 They can create it, it's just, it won't be the same data.
**Jason Plumb** 35:48 From here.
**Cesar Munoz** 35:50 from the agent, so probably they will get…
Yeah, it'll work, badly, but it will work.
**Jason Plumb** 36:00 Yeah, I mean, they could build their own implementation of these two things if they don't care about them, and then ignore them in their install method, right? Like, okay.
**Cesar Munoz** 36:07 Yeah, they will get, like, another session ID that's not the one that the agent uses, and another time that's not the one that the.
**Jason Plumb** 36:12 But maybe they don't care about the session or the time, and they just ignore those fields, right? Maybe…
Yeah. So…
**Cesar Munoz** 36:18 Maybe, yeah.
**Jason Plumb** 36:19 Yeah.
The reason why we have… so, backtracking a little bit, the reason why we have the context at all was to bundle up some classes and give us a little flexibility in this API.
And being able to add features… like, being able to add or remove classes from the instrument installation context without breaking this call. That was the whole idea. Because it used to be… it used to… install used to have, like, this, basically, inside of it.
**Cesar Munoz** 36:47 Yeah.
**Jason Plumb** 36:48 And that's because some instrumentations need some of these things, right? Some instrumentations might care about the session, some might care about the clock.
Some need to do callback hooky stuff with the app, right?
**Cesar Munoz** 37:01 Yeah.
**Jason Plumb** 37:02 They need to register listeners or whatever. That's why we have it.
Okay.
**Hanson** 37:09 So, if someone wants to install instrumentation, and they don't care about session, or the clock.
Why do they even have to go through the SDK?
they just want instrumentation. They could… they could load instrumentation however they want.
basically.
**Jason Plumb** 37:28 Sure, yeah, I mean, they can just build… yeah, they can build their own thing that sits outside and just might use the OpenTelemetry instance. Totally, yeah, that's… that's completely valid.
**Cesar Munoz** 37:36 That's true.
**Hanson** 37:36 So if they ignore… the value you provide is the stuff they can't just get from the application or the SDK.
So… I think we should allow this.
Because… with caveat, like, you know, things are not gonna work before they're uninstalled, or before they're installed, etc, etc.
But… Like, otherwise, they wouldn't need… they would need it to be…
an instrumentation the way this, SDK calls it instrumentation.
So… That's true.
**Cesar Munoz** 38:18 I think it's, I understand the value that we saw with the installation context object.
But yeah, it definitely is… it doesn't make any sense to have some objects there that are only used by a handful of instrumentations. So, the fact that you will have to provide a no-up in most of the cases.
for session provider and clock, it's…
It's, it's, it's, it's probably a sign that the, that, that maybe this is not a good…
Approach, you know, to have installation context.
The other approach…
**Hanson** 38:58 Boop.
**Cesar Munoz** 38:59 Which is… Yeah.
**Hanson** 39:01 Sorry, go ahead, sorry.
**Cesar Munoz** 39:04 There were two approaches that we discussed in the thread.
The other one was just to get rid of installation context, which I think is also something that Jason
mention.
And just fast, open telemetry drum.
And then, ideally, open telemetrodome should have getters.
For the stuff that it initialized.
So that people can get those and use them if needed. So I should have a getter for the clock.
And… and things like that.
The problem with that approach, if I remember correctly… I mean, I love that approach, because it will…
Allow us to… train the API surface.
A little bit.
And it will also probably solve the issue that you mentioned, Hanson, where…
you know, right now, users will… will be able to just install whatever they want, regardless of whether they have an OpenTelemetry ROM instance or not.
So it doesn't seem, like, tied, like a single thing, like…
You know, like a part of the signal system.
In this case, they will have to provide an OpenTelemetry ROM instance.
Which has the stuff that's needed there inside.
But the problem that I remember we discussed about that approach was that OpenTelemetry ROM allows
To shut down the agent, because it has a shutdown method.
And I remember we thought that that was gonna be ended.
super important issue, you know, that instrumentations could shut down the agent, that this is how good, and I agree with that.
That's… that's bad.
But that's why I think one of the latest stuff that I mentioned was that I mean…
Maybe both options have trade-offs.
And in the case of that option, maybe the trade-off of having to check that none of the instrumentations that we provide
in this repo, called shutdown, I think I will be fine with that.
Because that will solve a lot of other issues. But yeah, those are the two options.
So far.
**Jason Plumb** 41:15 Yeah, what I was thinking about, and I think I also proposed and probably described it terribly, was that we could enhance the DSL…
And say, if you have… we could… there's probably some programmatic ways that we could, like.
dial it in a little bit, but we could certainly, through documentation, encourage users to not ever call install themselves. That if you write instrumentation, you should pass it to the agent before the agent is initialized.
And then we handle it for you, and it shouldn't be a problem.
**Hanson** 41:52 That would be useful.
**Cesar Munoz** 41:53 Sourish people from installing stuff after the agent has been initialized?
**Jason Plumb** 41:58 Right, and if they have use cases for that, then just build your own thing. It's not OpenTelemetry instrumentation at that point, it's whatever you're doing, right? Which is totally valid. It's just, if you want to play in the OpenTelemetry ecosystem and have instrumentation that does stuff.
and uses the OpenTelemetry facilities at your disposal.
You need to pass your instrumentation to the agent before it's initialized.
That seems… I don't know, I mean, that's… I think that's a little more… Consistent.
Like, it allows the state to kind of be set up in advance, and…
Yeah, I mean, it would be a virtual…
**Cesar Munoz** 42:38 It would be a virtual constraint, though. I mean, technically, they still can, Call install whenever they want.
So… If we go with that route.
**Jason Plumb** 42:48 which I think it's also fine, because…
**Cesar Munoz** 42:50 frankly, a lot of the stuff that I want from any kind of change that we add
into public APIs is the ability to
keep it maintainable, you know, without it becoming, you know… Painful for us.
That, that will be in line with that as well. It's just that…
I think we will have to be very clear in that if they choose to call install after the agent is initialized.
we wouldn't provide support for those use cases. So it's like, they're on their own.
Right. In that case.
**Hanson** 43:30 Right now, do we use SPI to discover instrumentation, or is there a hard-coded list?
**Cesar Munoz** 43:36 Who uses the app?
**Jason Plumb** 43:37 And there's both. We do both.
**Hanson** 43:40 So if it's SPI.
**Cesar Munoz** 43:41 Oh, yeah.
**Hanson** 43:42 and it's on the class path, shouldn't it just be discovered?
**Jason Plumb** 43:47 Well… We, we find stuff.
**Cesar Munoz** 43:49 stuff on the glass.
**Jason Plumb** 43:50 They believe.
**Hanson** 43:52 Right.
So, get all…
**Cesar Munoz** 43:56 Know if you created it in your app.
**Hanson** 44:02 Right, but when… when this is in votes, the class path is the apps class path, right?
**Cesar Munoz** 44:09 Yes, but for the SPI to get this discovery, you have to…
Like, it has to be… there has to be a meta file.
That points at your implementation.
**Hanson** 44:26 Right, so…
**Cesar Munoz** 44:27 Which is usually what we add in the libraries, but if you create an implementation within your app.
and want to install it, then that won't… that won't be part of the benta Inf directory. So it won't be discoverable.
**Hanson** 44:41 The meta-inf directory, is it in the module, or is it in the SDK,
Because if folks create a meta-inf file, then it could be all discovered.
**Cesar Munoz** 44:52 Yeah.
True.
**Hanson** 44:55 And then… then that would… That would just load things up automatically.
**Cesar Munoz** 45:03 Yeah, I mean, it's more work. You will have to make… you're… Local implementation, discoverable.
Maybe using… yeah, probably they could use something like auto… Out of service or something.
Well, no, other savers, no, because that doesn't work with KSP.
**Hanson** 45:24 So, so if, if…
So I think we could put enough metadata for this to be auto-discovered. We probably have to document it and say, hey, this is… which then becomes an implicit API. If we don't want to go that route, we can just basically, as what Jason said.
pass this object in, and we will load it. So, instead of auto-discovery, just shove me a set of Android instrumentation, and we will load it for you. And then… and then everything is taken care of.
And that would be…
**Cesar Munoz** 45:54 do that.
in the builder.
the ROM Builder.
**Hanson** 46:00 I feel like that's the easiest way of not having an explicit programmatic way to call install. It just makes it an instrumentation.
Rage is the easiest.
**Cesar Munoz** 46:13 Based on how the class path discoverability works.
You know, it's… it will still, you know, the interface will still need the install method.
So that's what I'm saying, that it's not technically impossible to call the install method at any point you would like.
So… We just…
**Hanson** 46:32 We can say it's unsupported.
**Cesar Munoz** 46:34 Yeah, that's what I was mentioning. We can just say it's unsupported. If you go these route and find trouble, then you're on your own. We won't… we won't help.
That's something I'm fine with.
But we haven't done so, so…
**Hanson** 46:48 If we're worried about exposing our SPI internal as an API, then I think doing what Jason said, and say, hey, provide me a list of Android instrumentation, and we will install it for you. Have an API that does that.
on Run Builder, or not Run Builder, on whatever gets called before we start the SDK. That seems reasonable. Or, hell, have it as an optional parameter you can pass in when you start the SDK.
Start with these additional instrumentation.
**Cesar Munoz** 47:18 Yeah.
**Jason Plumb** 47:21 The only reason I'm clicking around in the Java instrumentation is to just remind us that we have this kind of… in Java, we have this separation between library and Java agent. Library is what we might expect people to…
take a dependency on if they manually want to use what already exists in OpenTelemetry without the agent.
Right, they still have to create their SDK, they still have to do all of that auto-configure stuff, but then they can use this library, right? And here's, like…
a quick start on how you might do that. You have to import the library classes and then wire them up to your instance of OKHTTP client. Just as one example, like, there's… I don't know, there's a dozen that have library instrumentation, there's not nearly enough, we want more.
But then the separation is, that's cool, you can do the hard work of just using the library, or if… but if you're using the agent, the agent has to kind of know how to wire up the library instrumentation to the rest of the agent.
And… this is where it gets kind of fancy, right? Like, these are the…
this is the breakdown of how instrumentation is written in the agent. The module is kind of the top-level construct, and it's loaded by the service loader.
Alright, it's found based on its interface, and then the methods on it are pretty… like, we can… we could even jump over here.
One of these is correct, yeah, this one, maybe. Can I jump there?
Yeah, so the…
So when you implement one of these, sorry, you extend through inheritance one of these, and then there's a few things that you tend to override, which are like, give me the list of instrumentations that you produce.
And then, this is, like, a sort of a newer way of loading instrumentation, but are you invoke dynamic ready? Yes. And that's all that this has to provide, except it hides the fact that there's a pile of code in here.
Right?
I guess what I'm saying is, like, there's a separation, and if you wanted to build agent instrumentation, you can do that. I mean, you can build an instrumentation module and totally do that through an extension.
And, you get access to then to all kinds of stuff, I think, through that base class.
Like.
**Cesar Munoz** 49:49 Yeah, and in this case, the agent depends on the library, so…
**Jason Plumb** 49:52 I clicked the wrong thing.
**Cesar Munoz** 49:53 In our lives.
**Jason Plumb** 49:54 So, yeah, yeah. It took… yeah, so…
**Cesar Munoz** 49:55 I'll, like…
The same stuff that you will do manually is just done by the agent when you add the agent.
**Hanson** 50:01 It's their instrumentation API, but.
**Jason Plumb** 50:04 It is.
Yeah.
**Hanson** 50:06 And I think right now we're saying the API is this Android instrumentation class, and we're just basically saying, how do we wire this up? And we can build a bunch of infrastructure to auto-discover if we don't want to use an existing one. Or we can just, for simplicity's sake, have a method.
which I think…
accomplishes all that we want right now. May not be as flexible, may be programmatic instead of auto-discovered, but…
Until we have 10 of these.
**Jason Plumb** 50:39 Yeah.
**Cesar Munoz** 50:40 Yeah, but that's the thing, it's like…
One of the reasons for this change is that we're looking… my understanding was we're looking to stabilize this API.
**Jason Plumb** 50:50 Yeah.
**Cesar Munoz** 50:50 So… That's why, you know, At least the use cases that are possible today.
they should be, you know… I hope we can go get them to a point where… get the API to a point where we…
John…
Feel like we're gonna have to, you know, backtrack in the future, or, you know, introduce braking changes because we didn't think stuff through.
**Jason Plumb** 51:16 Totally. That's what I'm trying to get at here.
**Cesar Munoz** 51:19 The.
**Hanson** 51:19 Yup.
**Cesar Munoz** 51:22 Just wanted to say, the instrumentation, so… It seems like we are… gearing towards…
The option of not supporting
Some use cases that are technically possible.
It's just that we will document them, we'll say, this is not supported, you can do it.
But we won't… or maybe we won't even mention that it's possible. If people find out that it's possible, it's, you know, we're still gonna just add support for the stuff that… the path that we support.
Now, the… I think that that's a valid argument in most of… in most of…
Most of the changes that that will require will be documentation.
So that's fine.
Now, regarding the installation context object.
It's still something that users will have to deal with if they create an instrumentation.
And it won't be the users installing instrumentations, but the ones creating it will have to deal with it.
**Jason Plumb** 52:26 Because it's on the public interface at that point, yeah.
Like, if we keep this interface the same.
then they have to deal with, and that is part of our API service.
**Cesar Munoz** 52:37 I do like the idea.
**Jason Plumb** 52:40 of passing just a RAM instance.
**Cesar Munoz** 52:42 And that users should be able to get what they need from the RAM instance. Because this installation context, to me, is like adding an extra layer.
that… it's an extra layer that we'll have to support, so I'm not sure… You know…
I would like to get rid of it, to be honest.
**Jason Plumb** 53:02 Yeah, it'd be cool to at least see, like, even if it's hacky, how that might look like. I agree, I would like to see what that feels like, to have installed just take the OpenTelemetry instance, and then have getters for at least these two, maybe all three. I don't know about context, whatever, but at least these two.
Because they're just, they're just, they're.
**Cesar Munoz** 53:25 They're immutable.
**Jason Plumb** 53:25 Yeah, they're immutable, they just do their thing.
And having… the one hesitation is that we have balked previously at having session be stable. So a session provider is not a public stable interface yet, and that comes from the session module, right? Like, it comes from… which…
we decided we weren't ready to stabilize until maybe some more semantic invention stuff happens? I don't know.
**Cesar Munoz** 53:55 I mean, it is public, but…
**Jason Plumb** 53:58 Really, the only thing it provides is a session ID, right?
**Cesar Munoz** 54:01 So, you think that will change?
**Hanson** 54:04 So, so, like, Cesar's change is totally fine. Like, if we want to support ad hoc installation outside startup.
**Jason Plumb** 54:15 I don't want to.
**Hanson** 54:16 You don't want… So, so, so there, so that's… that's the question. It's whether we want to do that, because it's not… it's not, it's not what gets passed down and what gets to the API, is do we want to support ad hoc installation?
Cause I think we could have…
We can… we could hide all the installation context details.
with both ad hoc installation and no ad hoc installation. And we could expose it for both.
So that is almost irrelevant. It's whether we want this install method to be run ad hoc. So we should just talk about that. And we might… we're probably out of time today, but…
**Cesar Munoz** 54:53 No, but I think… I think we settle on that, that use case. We don't want ad hoc installation, so we will document that we don't support it.
**Jason Plumb** 55:00 Yeah.
**Cesar Munoz** 55:00 But aside from that, the issue of having this extra layer called installation context, it's a separate issue, that's the one I was mentioning. But yeah.
**Jason Plumb** 55:10 Yeah, I would like to see a mock-up or, like, even a draft PR that, like, does part of what we're describing. I think it'd be interesting, especially if we can include the DSL portion to which people can add their own instrumentations to be installed, because I think that is a gap currently. If you have custom instrumentation that you want the agent to install for you.
That… that's currently a gap. The other thing I just wanted to call out, I think I did a reasonable job of this, was that the… one of the main things I don't like about this PR, and I'm sorry if that sounds mean, I'm not trying to be super hypercritical, but
the fact that makes the OpenTelemetry instance mutable. Like, it introduces mutable state into the OpenTelemetry instance was the thing I was, like, kind of like, I don't know.
feels wrong.
**Cesar Munoz** 55:55 Yeah.
**Jason Plumb** 55:55 Oh, so that's why having all of the instrumentations known up front is nice.
**Cesar Munoz** 56:00 I'm glad to get that feedback, so don't worry about it.
**Jason Plumb** 56:03 Okay, cool.
**Cesar Munoz** 56:03 I'll, I'll…
**Jason Plumb** 56:04 Fist bump.
**Cesar Munoz** 56:05 I'll try to… I'll try to, come up with something more on the line that we discuss in this meeting, of what we discussed here, so…
**Jason Plumb** 56:15 Cool, that'd be great. Before we run out of time, Hanson, did you have something else?
**Hanson** 56:20 No, I will rat-hole into this discussion in whatever issue or PR we discuss.
I don't think it's switching on effects that fast, it's just a wrapper around things are already public, so…
**Jason Plumb** 56:31 Yeah, it's a relatively small surface.
I just wanted to point out that I cannot run this meeting for the next two sessions. Next Tuesday, I'm gonna be traveling, and the session after that is… or the, yeah, the meeting after that is during KubeCon.
I think… So…
**Cesar Munoz** 56:49 handle it.
**Jason Plumb** 56:50 Are you UTC?
Okay, plus one.
**Cesar Munoz** 56:54 I… well, I… it changes. I'm not sure what is it right now.
But, yeah.
**Jason Plumb** 57:04 I was just curious, so it's evening time for you, right? It's like 5pm or something?
**Cesar Munoz** 57:09 Right now, it's… it's… almost 5PM, but I think it's gonna change next week, or…
**Jason Plumb** 57:15 Great.
**Cesar Munoz** 57:15 After. It's somewhere in the 5 to 6.
I have this meeting.
**Jason Plumb** 57:20 Okay.
There's a chance I could join.
But it does seem unlikely.
So if you could run it, that would be killer, and I'm sorry I won't be here to provide…
Any help at all?
**Cesar Munoz** 57:35 Oh, yeah, that's fine. Probably for those… the week that you're gonna be at QCOM, I'm wondering if…
They usually cancel that meeting for…
For that week in Alto Java, don't they?
**Jason Plumb** 57:47 That's true, we might consider canceling the one…
for Android the week of KubeCon, I'd be fine with that.
**Cesar Munoz** 57:55 Yeah, man, me too.
**Jason Plumb** 57:57 I haven't remember.
**Cesar Munoz** 57:58 Have everybody.
**Jason Plumb** 57:59 Yeah, I haven't heard in the last couple of weeks, but I think…
Trask might not be going, and so he might just be like, whatever, I'm just gonna run it, because I'm not going, but…
**Cesar Munoz** 58:08 Yeah, I mean, if it's not canceled, I'll take care of it.
**Hanson** 58:12 I'll be around, I won't be going to KuCon this year.
**Jamie Lynch** 58:16 I'll get into KubeCon, but I won't be around.
**Jason Plumb** 58:18 Alright. Bummer.
Just to hop across the pond for you, too, Jamie.
**Jamie Lynch** 58:23 I know.
Maybe that's, yeah.
**Jason Plumb** 58:26 Yeah, cool, cool.
Alright, it's good to see everyone.
**Cesar Munoz** 58:30 Thank you.
**Jason Plumb** 58:30 Have a rest of your week.
**Hanson** 58:32 Right?
**Cesar Munoz** 58:32 You too. Bye.
