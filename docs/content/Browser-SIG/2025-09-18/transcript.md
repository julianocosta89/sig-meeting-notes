SIG: Browser SIG
Date: 2025-09-18
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 02:13 Come on.
**Martin Kuba** 02:14 Hi there.
Okay, I don't think, I don't think, ted is joining today, so…
But if we can just get started.
I'll just go down the line,
Santosh, you have the first topic.
Santo's not here.
**Santosh Kumar Cheler** 04:06 I'm here, yeah. Okay.
Yeah, I think I,
asked this question on Slack, too, in the Total Browser channel, and only you responded, Martin. Basically, I'm looking for any…
Feedback, from those who have used this instrumentation.
In our experience, we have observed that,
The long task events, sometimes on pages that are not,
you know, built very efficiently. I think we have noticed too many, events coming from the same page.
And when I say too many, think in terms of, like, hundreds of thousands.
Over the, you know, Duration of, let's say, an hour.
If somebody is just hitting on that page. So it is really, bad.
So I'm wondering, and the other thing to note is this long task events, although they have
Theoretically speaking, you know, they do have attribution information, but it has not been very helpful.
It only talks about whether… The issuers from the… First party or third party?
But not exactly, you know, which…
Function is slow, which task is slow.
There aren't… there isn't much, you know, helpful detail to address the issue of long task itself. Like, why is the task taking long, and which task is taking a long time?
It seems to be useful, as a… a way to…
As a causation for the web vitals, like, hey, too many long tasks is probably…
Affecting the web vitals, so it seems to be useful from a…
Secondary perspective, but not, to really determine what tasks are slow.
So with that, I'm wondering, if we should instead model the long task events using a metric.
Which will maybe compute,
an aggregate over, let's say, you know, every minute, and emit, you know, only once a minute.
You could attach the attribution maybe as exemplar on the metric.
If needed, but otherwise, it will… have…
A count of how many occurrences, how many instances have occurred in that minute, and also a histogram of the long task duration.
The challenge is, just a few weeks ago in the client seg.
I had mentioned that as a guiding principle for client instrumentations, maybe we should… Put a guideline
That client instrumentation should not emit metrics
metrics is a server-side concern. There were a few reasons we talked.
it hasn't, made it to the official… it's not, like, a set in stone that we should not emit as a metric, but I still feel that using a metrics API is an overkill on the… in the… in the client-side instrumentation, so…
The next question is, you know, does it make sense to simulate the metric using an event? Now, you just
You know, model your event.
To, to include a count and, the histogram.
So, just wanted to get thoughts. I don't know if, there is anyone that has, I mean, anyone in this group that has used this instrumentation, and what their experiences are, and what they think of this proposal.
**Benoît Zugmeyer** 08:16 I have some feedbacks, so…
In our SDK, we were collecting long tasks as individual events, And,
Since the beginning of the year, we migrated to long animation frames.
So, if they are supported by the browser,
We don't collect long tasks anymore, we just focus on long animation time, which is about the same volume, but…
They are much more valuable, because the attribution is way more detailed.
And… And so… I guess?
Just sending a matrix will… will…
a bit too bad, because we would lose lots of information in this case.
Let's… What we could do to limit the volume is to filter
Long task or long animation frame, by duration.
So… because the minimum threshold is 50 milliseconds, but…
If we say, okay, let's just focus on the long tests that are more than 200 milliseconds, we should have way more,
**Santosh Kumar Cheler** 09:37 Vita.
**Benoît Zugmeyer** 09:38 Way less data, sorry.
**Santosh Kumar Cheler** 09:40 Okay, okay.
Okay, so in short, you're saying that there is an alternate to long animation frames. I have heard about it, I have not looked into it in detail, but…
You think that the concern with volume will remain the same, and you're suggesting to increase the threshold to reduce the volume?
**Benoît Zugmeyer** 10:05 Yeah.
**Santosh Kumar Cheler** 10:08 Yeah, okay, that… okay.
**Benoît Zugmeyer** 10:17 And yeah, I don't… I don't really know the status of the long task, because, as far as I know, it's only implemented in Chromium browsers, and
So, I think it's kind of superseded by long animation frames, and that's why we kind of…
Removed support for it, but…
**Santosh Kumar Cheler** 10:42 Yeah, I think,
We have to see how, by filtering on the threshold, on a higher threshold, how useful that data is going to be to attribute for…
the… as a causal detail for the web vitals, I think we will need to analyze that.
Hmm… Okay.
But any… any general thoughts on…
Modeling, you know, this data as a metric.
**Martin Kuba** 11:20 I was… Sintosh, I was wondering, like, how would you even model it
If you send… if you send a metric.
That you, like, collect in a single client, but then you would aggregate that together across all clients?
**Santosh Kumar Cheler** 11:40 Yeah, I think at least in our product, it depends on how each of us is going to make use of this data.
Renewer product, but at least in our case.
We show that, hey, on a given page.
For a given page, you know, this is the…
This is the number of long tasks, you know, seen in this minute, and then this is the histogram of the durations.
And then show the corresponding web vital, and then…
you know, make a connection. So something like that.
So, yeah, so at the end, you know, you do aggregate the data, and, and if we,
You can aggregate… you can compute that aggregate looking at all the individual events.
Or in this case, you know, you would be completing the aggregate based on the aggregated metric per user, per instance.
Which is effectively the same.
**Jared Freeze (embrace)** 12:48 So you said before, it's how it, affects web vitals, right? So…
If you care about what happens between
like, document load and, like, LCP, right? Long tasks that hold that up.
Yeah, I mean, it seems like you can just collect them. You can just count it, right? Like, you don't need a, like, a timer to run, say, like, every minute or something.
if you're trying to figure out if the UI locks up between navigation, like, while they're working, like, without a URL change.
I think that's a tougher question. Are you talking about, like, just before… like, where blocking resources and long processes take before LCP?
**Santosh Kumar Cheler** 13:34 Yeah, frankly, I have not, like, I'm not super familiar with, the web vitals themselves.
So yeah, I have not looked into, you know, this detail, but…
If you are suggesting that
LCP is emitted only once, when the page is fully loaded, right? I think in that case.
In that case, these long tasks events… but the long task events could occur anytime, right? Even afterwards.
So, are you suggesting that they are not? They may not be useful?
for LCP, once the LCP is emitted.
**Jared Freeze (embrace)** 14:17 No. No, I think it's useful to, like, figure out, because I think you're saying, like, the long animation frame is, like, the UI being unresponsive, right? Is that correct?
**Santosh Kumar Cheler** 14:29 Positive, yeah, I think so.
**Jared Freeze (embrace)** 14:32 Yeah, I mean, I guess collecting… I mean, if hundreds of thousands is crazy, right? So, I don't know. It seems like the right thing to do, just count them, you know, put it on an interval.
you know, potentially between… yeah, I mean, I would collect it, like, between the URL changes.
Right, it's start and stop the timer if you have a SPA.
Huh.
**Santosh Kumar Cheler** 14:57 Correct.
And the other concern is… Should, should the client,
Like, the browser instrumentations, we're using a metrics API.
Which we have stayed away from so far.
**Jared Freeze (embrace)** 15:16 I don't think so. I think the… we… we talked internally, and I think across the group, it was like, it doesn't make sense.
Generally, this… this, I think, is actually a pretty good use case for, like, you don't… you don't want to report every single one, right?
But the library itself was the blocker here for web. We just can't include another library. I think we had talked about…
just very briefly, I talked with Mark about just creating completely new libraries.
That have the right interface?
I still don't think we should probably include metrics. As it stands today, we couldn't, I think, for file size.
So, like, the actual, like, package.
**Santosh Kumar Cheler** 16:07 Yeah, and, and I know we stay away from talking, anything outside the client concerns, but…
as in the… I do…
I think, this puts the requirements on the receivers, too, to have a metrics endpoint.
That also is a consideration.
Because in our… in our legacy EE products, all the data, you know, was sent as events, but now traces, events, and metrics, you know, they go to different endpoints, which is also…
extra operational… Hustle. Overhead.
So yeah, I'm not, too inclined to,
use the metrics API, but just the thought that should we still
Collect the information as a metric and put that in the event.
**Jared Freeze (embrace)** 17:12 Not sure on that. I don't know.
**Dan Gomez Blanco** 17:16 that.
**Jared Freeze (embrace)** 17:18 Just to answer Dan's question, yeah, there's a cap, right? Like, the resource… the resources cap at $2.50, and then it starts throwing them out.
So you have to flush, right? Or 200?
**Dan Gomez Blanco** 17:30 It's 2… I think it's 204 long tasks. It's infinite for, like, marks and measures and all that.
But, yeah, it does count. So I do wonder if, like, you know, if that is the way…
If, you know, that's another way to handle it, right? So after…
**Jared Freeze (embrace)** 17:45 Oh, yeah, that's a good point. Yeah, just flush it at, like, 200 or 190 or something.
**Dan Gomez Blanco** 17:52 And after that, yeah.
Mmm…
**Jared Freeze (embrace)** 17:58 And then just try to flush it before navigation.
I think that makes sense.
**Dan Gomez Blanco** 18:08 But the threshold as well. Is it… is the threshold, like, is it 50 milliseconds by default?
And is that something that can be…
I guess that's what, Bernard was saying.
Borth looking into as well.
On the metric side, I just… I'm not sure about how one would represent, like.
Without having a metric, something like an exponential histogram, within… an event, I think that might be…
You know.
**Santosh Kumar Cheler** 18:45 Yeah.
**Dan Gomez Blanco** 18:46 quite complex, I guess, you know, to…
**Santosh Kumar Cheler** 18:48 To do that without the, without the.
**Dan Gomez Blanco** 18:51 The rest of the metrics.
Metrics SDK, I guess.
**Santosh Kumar Cheler** 19:00 Yeah. One question on this link that you shared, on the buffer sizes. Is that the limit the browsers need to…
Use, when the clients are not, consuming the entries?
But if they are, then this limit doesn't, you know, help so much. Is that correct?
**Dan Gomez Blanco** 19:24 I think, yeah, I think you can increase the limit, but by default, that would be the…
the buffer size, and I'm not sure…
At what point they are cleared, or…
flushed, let's say. I'm pretty sure that…
It doesn't… does it do it automatically? I'm not… I don't know enough about this, if it does it.
Automatically, or if it just stops.
Add to new stuff, I think, Carlos, you've got your hand raised.
**Carlos Alberto Cortez** 19:52 Yeah, so, for the sake of time, probably it could be good to discuss other items. I saw there are 3 or 4 more items after this one.
So, and by the way, something that we do at SPEC is that we try to put an estimated time that we think we can leave. That's always useful, so we try to
our very best to cover all the items. And by the way, Santos, it would be nice if you could have some notes, even though this is a reporter, it would be nice in case people want to take a quick stop at the dog, you know? It would be super nice.
**Dan Gomez Blanco** 20:23 But we can follow up in the discussion on… on Slack, maybe, as well.
**Carlos Alberto Cortez** 20:27 Yep.
**Santosh Kumar Cheler** 20:29 Thank you.
**Carlos Alberto Cortez** 20:35 So, Joaquin, maybe you want… yeah, Joey.
**Joaquín Díaz** 20:37 games.
**Carlos Alberto Cortez** 20:37 Fucky.
**Joaquín Díaz** 20:39 Yeah, I don't think we need to discuss this here. I just want to say, like, thank you for commenting on that. I updated this morning after your comments. I think I changed my original approach was to have this basis, but…
to me, they make sense at the beginning, but now I think it's more confusing, so I just remove everything and stripped down into a list of events, and I'm trying to map them one-on-one to browser events, so there is no confusion, and we don't have to…
have opinions on how they're being used. It's just, this is what's happening on the browser, and how we emit it.
So yeah, if you wanna take another look, that would be great. My goal will be…
If we agree on those initial events, we can focus then on the semantic obsession of PRs and instrumentation PRs that are already there.
And try to get them… To the finish line, and start underneath the ones that don't have anything.
But we don't need to discuss it here, just as a reminder.
**Martin Kuba** 21:49 Okay, so I think I have the next topic, Mine is,
Also, we don't have to discuss right now, I just wanted to let people know that I opened an issue, the last, about page view, the page view event, and semantic.
Conventions for that.
We have discussed this last few meetings. There's a…
there's a PR for the semantic conventions, but we've… I've heard a number of different opinions on this, so I wanted to capture it in an issue that
And continue the discussion there. I just wanted to let people know that that exists.
**Joaquín Díaz** 22:29 Yeah, I have a feeling that we've been talking about this for, like, a month, and, I think we should try to.
Get to a point where we are.
Happy about the first iteration, and that is…
good enough, and we can iterate it, later.
Okay, I think I left my comment there, I think.
Regardless of… we can call it navigation, that's fine, but I still think, like, we want…
find an event that will capture every single way of navigating in the browser. There are, like, so many ways of navigating.
So I will focus on defining the…
What a navigation is, which is…
changing the page, however you do it, and then we can… I feel the approach will be having multiple instrumentations.
that may meet that event differently, depending on how the user needs to be met. Like, for example.
one that emits when the page loads, like, from scratch, then one, maybe just changing the URL is good enough for you to know that there was a navigation, or eventually we can hook up to the new, how it's called, like, the soft navigation heuristics, that'd also be good, but we don't have it right now.
So I think…
For now, we'll focus on defining what a navigation is, and then we can focus on how we instrument it.
**Martin Kuba** 24:01 Yeah, that sounds good to me.
**Jared Freeze (embrace)** 24:06 Cool. So I was just gonna put up a PR, just, like, a default NX install with some tooling, try to get away from ESLint, just look at different options.
And then we can talk about it, so that way there's not…
you know, it's always nice to have code to look at. So, like I said, I'll just do the packages folder and just put that up.
For next week.
**Dan Gomez Blanco** 24:39 Cool.
Is it me?
Yeah, so this is something that we discussed in the client-side, the general client-side, SIG on Tuesday.
And we've got the project definition from the original client side, still as an active project. I would like to mark that as discontinued, and then, close the project board that wasn't that, and then basically
signal to the community that this has started as, for browser-specific issues. The client-side SIG still
Meets every couple of weeks to discuss cross-cutting aspects.
And the next step there will be to try to,
Yeah, come up with a… with a… with a tighter scope project for something that is cross-cutting, like, sessions, for example.
Stabilization of sessions, and so on.
So, it won't deal… it's not going to deal with instrumentation, perhaps an instrumentation or anything like that.
Does that.
I mean.
any concerns on just closing that project, or moving it? It's basically moving the document in the community repo
From the active projects to the…
completed projects, because I want to have a better name.
But then adding a note saying that
Yeah, the deliverables were not all completed, but the progenesis continued, and continued with the browser, with the browser project.
Cool.
**Jared Freeze (embrace)** 26:14 Seems good.
**Dan Gomez Blanco** 26:15 That's good.
I'll do that then.
**Jared Freeze (embrace)** 26:20 I would be curious, who from here is going to Client SIG, or has in the past?
Yeah.
**Dan Gomez Blanco** 26:28 Yep.
**Jared Freeze (embrace)** 26:29 Cool.
**Dan Gomez Blanco** 26:30 I think, yeah, it's good to get that.
cross-pollination here as well, right? If we at least talk about those common concepts.
**Jared Freeze (embrace)** 26:42 Agreed.
**Martin Kuba** 26:49 We've got a few more minutes left, does anyone else?
Have anything else to talk about?
**Jared Freeze (embrace)** 26:57 I was just… I was just gonna say that, I saw one of your notes that, URL changes are definitely hard to track.
or you said complex, right? Which… which is true. I think…
I'd be curious to see how we eventually hook into, like, the major routers, because I think that's gonna be pretty essential, so literally just looking for Angular in the window. Like, looking for a rack router in the window, because those…
I believe they all have interfaces that attach to the window that emit events. And I just think it's a little… it's a little strange, I think, to, like, have, like, specific vendors, but it's also, like, the reality that that's what everyone is using, so…
I'll be curious to see how we interact with those specific things, and, like, how they version, and all that good stuff, like, you know, there's major differences between, like, you know, 7 and 8, and so…
How that might work.
**Martin Kuba** 27:55 Yeah, when I was, when I was, I was referring to the, specifically to the soft navigation heuristics.
Which is, like, which is, like, a generic…
general approach to… to, like, tracking these… these route changes, so you wouldn't need, like, to know about a specific framework in that case. But yeah, I mean, it's…
If, you know, that, like, generic instrumentation Could potentially be complex,
But yeah, maybe we might still want to, like, Use… do some special…
Like a framework instrumentation, too, that's possible.
**Joaquín Díaz** 28:34 That's… that's what I'm saying, it's like, if we define what a navigation is, then we can have
Whatever number of instrumentation that will hook up to whatever library or way of Instrument or way of navigating.
That is why I don't think we should.
Try to think of an event that should cover everything, because there are so many ways of doing it.
I think it's perfectly fine if we have, like, an instrumentation for a router, or whatever it uses, like, individual instrumentations for each library.
Anything we should have one imitation, of course, because that will be very hard to do, and hard to maintain.
**Jared Freeze (embrace)** 29:13 Yeah, agreed. I mean, the… like, you know, a good… a good default is… is…
You know, gonna be recommended, and then, you know, if you wanna deviate, sure.
**Abinet Debele** 29:24 Just here, I think for…
the common frameworks like Angular and React.
the history change itself, captures the route changes, and I think it's common across, this framework, so…
That's… that's already what we try to implement.
But I don't know if there is specific,
logic in the frameworks. If there is something different that changes a route, makes, that results in a route change, but…
the industry change usually tries to capture that one, and I think that's enough for those scenarios, but… for…
Things like bug navigation and other things, maybe we need to have some more events, some more triggers, probably.
**Jared Freeze (embrace)** 30:14 Yeah, I think so.
It'd be nice, too, to have, like, look at, you know, as the new APIs are coming, to be able to integrate those, you know, check for the new navigation API.
Because Chrome releases every two weeks, right? So, it'd be nice to pick that up as it comes.
**Abinet Debele** 30:36 Yeah.
**Benoît Zugmeyer** 30:40 But at the same time, like, he… if,
We want, probably, to support other browsers, so… If the soft navigation becomes like…
A key event.
it might be too bad for the other, or maybe it could be polyfields, but I don't know.
**Jared Freeze (embrace)** 31:12 Yeah, I don't know the recommendation status or anything like that, but for the evergreen browsers, I don't know.
**Martin Kuba** 31:22 You know, I would actually be very interested in hearing from… if you have good representation of different vendors here, like, how… how everyone is handling this kind of… this kind of thing, as far as, like, generic
self-navigation instrumentation, because I think there are a lot of implementations out there, and I think for the most part, like, the…
you know, like, the community has kind of converged on similar solutions. And I think what the Chrome team, or, like, what the incubation group is trying to solve is make it the standard, but… but I think
it's been solved out there, so I'd be curious, like, to how…
Different people have. What they have, yeah, what would they recommend?
**Benoît Zugmeyer** 32:06 Basically, for us, we do the same as, dragging…
commented on your issue, like…
We, instrument, root, Upstate.
And, push date and stuff like this.
And we create a new view every time the URL changed, but not the parameters.
Thing like this.
If the hash is changing, but it's not matching any element, so we consider it as a root change also.
Things like this.
It's pretty straightforward.
**Joaquín Díaz** 32:51 Yeah, we…
Sorry, you probably were able to say this, yeah. But we have React instrumentation directly, like, we have instrumented React router V5, V6, and both, like, the data
Way of, you know, the new data navigation.
Because we, for us, it was important to also know the path, not the URL itself, but the actual, like, route that the developer defines, and also, like, send that over the instrumentation.
And I think the only way of doing it is actually hooking into the instrumentation itself, the library itself, so we did that.
**Benoît Zugmeyer** 33:33 Yeah, same here. We have a reattrooter integration.
**Jared Freeze (embrace)** 33:39 So, were you saying you also check for DOM changes? Like, you have a threshold for DOM changes?
On the hash, is that what you were saying?
**Benoît Zugmeyer** 33:48 No, no, you know…
In the past, when the router were working with the hash, and so the root was in the hash.
So, to distinguish between, like, a link that targets an element on the page, and the root.
We just do a getElementByID, or something like this, to check if the element exists or not.
You see? And if there is no element, then we deduce that it's probably a root.
**Jared Freeze (embrace)** 34:28 Okay, that's interesting.
**Martin Kuba** 34:32 So we're out of time, we're over time, so maybe you should continue this discussion in Slack or on an issue?
Or next time.
Okay.
**Jared Freeze (embrace)** 34:45 Thanks.
**Joaquín Díaz** 34:47 See you, everyone.
**Benoît Zugmeyer** 34:48 June.
**Dan Gomez Blanco** 34:49 Yep.
