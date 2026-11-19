SIG: GO SIG
Date: 2026-09-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:41 Hey, Brian.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 00:53 I'll unmute. I'll, I'll start again. Hi there, how are you doing?
**Tyler Yahn (Splunk)** 00:58 Doing well.
Doing well, yeah. How about yourself?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 01:02 Yeah, pretty good. I'm a little jet-lagged, I just got back from vacation.
**Tyler Yahn (Splunk)** 01:07 Oh, yeah?
Anywhere fun?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 01:11 Yeah, it was, british Columbia, west coast, so Vancouver Island, what kind of…
**Tyler Yahn (Splunk)** 01:18 Yeah, I know it well.
Yeah, what part of…
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 01:23 What's that?
**Robert Pająk (Splunk Inc.)** 01:24 I think it's pretty far for you, right, Brian, or am I wrong?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 01:27 Yes, that's why I was saying I was jet-lagged. It's a AR time difference.
**Tyler Yahn (Splunk)** 01:32 Yeah, you were in the right time zone, is what I'm saying.
Yeah.
What part? So you were in Vancouver, or…
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 01:41 Yeah, we were in the city, went to Campbell River on Vancouver Island, went from there to see bears and wildlife.
**Tyler Yahn (Splunk)** 01:50 Yeah.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 01:51 Hell yeah.
And then had a few days in Whistler at the end.
**Tyler Yahn (Splunk)** 01:56 Nice. Is it getting, colder up there yet?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 02:01 I… it was kind of threatening. I mean, it was, 24 degrees in, in metric time.
**Tyler Yahn (Splunk)** 02:10 So not so much, yeah.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 02:12 Whatever.
What is that, like, 70… 6, or something like that.
**Tyler Yahn (Splunk)** 02:16 Yeah, I think it's, yeah, 76, 78, something like that, yeah. So yeah, it's kind of up there, but… Yeah, no snow up there yet.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 02:24 Absolutely, no snow, no.
**Tyler Yahn (Splunk)** 02:26 Yeah, yeah.
Yeah, that's a… I, I remember going to Vancouver, and I was, like, really liked it, and then I went to Whistler, and I was like, dude, what? I… I'm going here every time.
This… this place is awesome, yeah.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 02:40 It's a little like Disneyland.
**Tyler Yahn (Splunk)** 02:43 Yeah, oh, 100%, yeah. And, like, especially, like, when the ski season picks up, it's even more, like, surprisingly, yeah. It's… it's pretty… it's, like, kind of nuts, but… but just, like, the water there and, like, all the climbing and mountain biking and stuff, yeah, it's just, like, if you're into the outdoors, it is straight up Disneyland, yeah.
Yeah, that's really cool.
I also like it, because you're, like, right on the edge of going into pretty much the wilderness, like… it's super, super close to, like, you are out there, like, you need to take a bush plane kind of thing. So, yeah.
That's cool. Yeah, how long were you there for? Just a week or two?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 03:19 Yeah, 10 days, yeah.
**Tyler Yahn (Splunk)** 03:21 Okay, cool, yeah.
Yeah.
Excited to be back, I'm guessing.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 03:29 That's one word, yeah.
**Tyler Yahn (Splunk)** 03:30 Yeah, that's a word, yeah.
Well, cool, we're 3 minutes in, I don't see David on the call, or, I guess Damien's not coming, it's the later one, and then I don't see Sam. But, we could probably jump in here and start. If you haven't yet… go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, go ahead and add them there as well, and I will start sharing my screen.
Okay… Cool. Robert, you wanted to start us off, talking about this next release?
**Robert Pająk (Splunk Inc.)** 04:11 Yeah, so hello folks, I think that's everything, all brokers from the MySource are kind of covered.
I created the release issues, I started creating the APR, I even created APR to contribute that bumps to, you know, to the latest commit, because there are some, you know, breaking changes in the API service, so we are replacing global get logger provider to auto logger provider, very small, but I just decided to do it beforehand, so the release will be even easier of GO Concrete.
And yeah, I'm waiting for approvals to make sure that we can release. I set up the release date for tomorrow.
We have a day off tomorrow, but I can still do everything tomorrow.
**Tyler Yahn (Splunk)** 04:56 Okay. I had a question on this one.
**Robert Pająk (Splunk Inc.)** 04:59 Yes.
**Tyler Yahn (Splunk)** 05:00 the… The 010?
**Robert Pająk (Splunk Inc.)** 05:03 Yes, this is the TraceX.
Package, which is new.
there was some, you can go to the versions of YAML, or even just…
**Tyler Yahn (Splunk)** 05:15 Yeah, I… this is… this is my confusion.
**Robert Pająk (Splunk Inc.)** 05:19 If you… yes, exactly. If you just scroll it down, it's true.
**Tyler Yahn (Splunk)** 05:24 There's nothing… there's nothing more. This is the end. I made it to the end.
**Robert Pająk (Splunk Inc.)** 05:27 Okay, so… so maybe open the file. Just open the file, you know, maybe it's just in the middle.
So there's experimental traces, line 39.
**Tyler Yahn (Splunk)** 05:44 So this hasn't been released yet, is the thing?
**Robert Pająk (Splunk Inc.)** 05:46 Yep.
You can double-check on PKG right now, maybe, just quickly, so we can just double-check.
Orders, or blame.
**Tyler Yahn (Splunk)** 05:57 Three weeks ago?
Okay.
I gotcha. Okay, yeah, doesn't look like it's there. Okay, that answers that question. Cool, alright, thanks.
Yeah, so you're just looking for reviews on these PRs, right? And then you're trying to get this done tomorrow?
**Robert Pająk (Splunk Inc.)** 06:21 Yep.
**Tyler Yahn (Splunk)** 06:22 Okay.
Yeah, any other questions on that one?
Or comments on it?
**Robert Pająk (Splunk Inc.)** 06:30 Not for my side, and it's others, to be honest.
Okay, let's go further, then, to the next topic.
**Tyler Yahn (Splunk)** 06:40 Yeah.
Cool, Penny, next up, you want to talk about the meter configurator, in this pull request.
**Puneet Singh** 06:49 Yeah, yeah, I've been sitting on this for a while to… to recollect, you know, my thoughts. There was one… annoying thing I've faced, actually. I use… Remote provision environments for testing.
and development, and I was using, E2 instances on GCP, which are, like, CPU throttled. And, And that kind of contributed a bit to the benchmark test that I was running, actually.
And that I didn't realize throughout this whole time, I think, And, I think after switching to Intuit, it started to give, like, slightly more consistent results. But, but yeah, coming back to the PR, so the question is regarding the… Performance impact?
Of this feature for non-user.
And the thing that is being introduced is an atomic variable check.
if… if the value is changing for that variable, I… I can… see it going up by, like, 10 or 20 nanoseconds, but if the value gets, like, it doesn't change, it gets cached at some point, and then I don't see the regression going beyond, like, 5 to 7 nanoseconds. That is… that is my take on this one. So for hot path, that is the… that is the impact that is going to have.
For this. So, so my question is, is that, like, worse enough that Should I consider a config-aware path for this implementation?
And also, if you have any take that, you know, whether this, I mean, this is not, like, accurate or reasonable, you know, take, or I might be missing something more on the regression side.
**Tyler Yahn (Splunk)** 09:05 Yeah, so this is… yeah.
**Puneet Singh** 09:13 Yeah, this is the… this is the one, I think, regarding the hot path.
**Robert Pająk (Splunk Inc.)** 09:16 Yep.
**Tyler Yahn (Splunk)** 09:20 Yeah, I, like, I don't see why we need this.
To be returned for… For the… the ones that are… this is just not a… like, there's no meter, configurator configured.
Like, this shouldn't change. I can see, like, this is… this is inserting something into the stable implementation, whereas you can just provide an implementation of these instruments that wrap, the stable implementation, and do this check outside of it.
So the impact literally goes to zero at that point, right?
**Puneet Singh** 09:56 I mean, yeah, that is, like, totally, running different instruments for the… for the, you know.
for the config when the feature is enabled. So that means that the take is that we should always run a different implementation if it is going to change the hot path, always? Is that… Top fair assessment?
**Tyler Yahn (Splunk)** 10:19 Yeah.
Yeah, Rick. Yeah, like, it, you're not, like… unfortunately, there's a lot of implementations of, instruments, like, for testing and for, like, the global and things, so, like, this isn't… you're not the first to do it. It is a little annoying getting, like, 9 instruments, but, like, it's not… Yeah, it is expected, so, like, in review of it, like, don't feel like it's too much kind of thing.
But yeah, I mean…
**Puneet Singh** 10:48 Sorry, yeah, go ahead.
**Tyler Yahn (Splunk)** 10:50 No, no, no, I was just saying, like, yeah, like, that… what you just described sounds… the way I would go with this, yes, correct.
**Puneet Singh** 10:57 All right. Yeah, I think that… that is the major contention then. Then I will look for a config-aware kind of approach to… to see how I can separate it. But… but, yeah, no further questions on this one.
**Tyler Yahn (Splunk)** 11:13 Cool. Yeah, that sounds good.
Yeah, honestly, I don't think there was much more that was kind of, like, the main sticking point, but otherwise… Sorry, I'm trying to remember.
Look at so many PRs. Yeah, I think that's it.
**Robert Pająk (Splunk Inc.)** 11:33 I think we can say congrat… we can congratulate Puneet for being an approver.
**Puneet Singh** 11:39 Thank you.
**Robert Pająk (Splunk Inc.)** 11:40 Yo.
**Tyler Yahn (Splunk)** 11:41 Yeah.
Yeah.
Definitely, yeah, definitely appreciated, and excited to keep it going forward, yeah.
**Robert Pająk (Splunk Inc.)** 11:51 We appreciate your help, really, we appreciate it. Maybe we do not show it, but it really helps, not only PRs, but especially also reviews. Reviews are very helpful.
**Puneet Singh** 12:00 I mean, yeah, at some point, I was, like, in between getting overwhelmed slightly.
And I was like, you know, that… I will… I will cut on some of the areas which I have, like, not yet started, and focus on things that I know well, and… and then build up from there. So that kind of, I think, solidified things a bit, actually. So… so yeah, that's the only change I did in between the whole thing. So, yeah.
**Tyler Yahn (Splunk)** 12:30 You should, you should submit what you just said as a talk to a KubeCon, like a maintainer summit or something like that. Yeah, I think that's a good… a good talk right there. How to become an approver.
My, my journey.
**Puneet Singh** 12:44 Yeah, yeah, I think… I think that was… definitely, I can talk about something, actually. Another thing is… actually, this thought came to mind that… how much work that you're doing can… can translate to… or part of it translates to a KubeCon top, for example. So, so yeah, lots of questions on… on that, so probably I can… I can, you know, talk about later on that some… on that point, yeah.
**Tyler Yahn (Splunk)** 13:15 Yeah.
Yeah, KubeCon EU, call for proposals is coming to a close in a few weeks, so… yeah, worth it.
**Puneet Singh** 13:26 I wanted to add one more point, actually.
I'll… I'm… I'll work, for maybe a month or a half.
In async or offline, because the meeting timing is slightly… Late… late for me, so, yeah. I'm expecting that, yeah, it might be… it's temporary for one or two months, so, yeah.
**Tyler Yahn (Splunk)** 13:53 No, that's fine. Yeah, we understand, that's… Yeah, like, we definitely, like, it's not, it's definitely not required to come to these meetings. Working asynchronously in the project is completely acceptable, like, almost even expected, So, yeah, like, cool, thanks for the heads up. We will love to see you come back, to the meetings, but yeah, also understand,
**Puneet Singh** 14:15 I mean, it doesn't mean that I'm going away, just that the… most of the…
**Robert Pająk (Splunk Inc.)** 14:21 You need to sleep.
**Puneet Singh** 14:21 product won't be async.
**Tyler Yahn (Splunk)** 14:23 I, I…
**Puneet Singh** 14:25 I didn't want to, you know, like, it's just a coincidence that it is happening after me being an approver, but it has nothing to do with it.
**Tyler Yahn (Splunk)** 14:34 Yeah, no, totally get it. That sounds good. Yeah.
Cool.
Well, cool. That's also the end of the written agenda. Any other topics folks have?
Things they're working on.
Yeah.
Any… I guess… I know Robert's not… is on the fence right now, but any other update on people attending KubeCon North America? I know, Bryan, you said you probably aren't ever coming to North America ever again, or not the United States, I guess you were just in North America, so, yeah.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 15:12 Yeah, just that one country.
**Tyler Yahn (Splunk)** 15:13 Yeah, we won't talk about it.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 15:18 I've got a prom con in a week and a half.
**Tyler Yahn (Splunk)** 15:23 Oh, cool.
Nice.
Are you talking at that?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 15:27 Yeah.
My talk is entitled, Working Set Lied To Me.
**Tyler Yahn (Splunk)** 15:39 you have my attention, that sounds… that sounds like a good talk. I'll be into that one, yeah.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 15:44 I hope so.
**Tyler Yahn (Splunk)** 15:45 Yeah.
Well, cool.
Yeah, if there's nothing else, y'all want to talk about, we can end the meeting here. Puneet needs to go get some rest.
But yeah, it's good seeing you all. Please take a look at Robert's PRs, otherwise, and yeah, we'll see you all in a week's time.
**Robert Pająk (Splunk Inc.)** 16:06 View.
