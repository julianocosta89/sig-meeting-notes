SIG: Browser SIG
Date: 2026-02-26
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/0wK3_-nt6-CFCCnVTwb0HL_5ajXirrTQLm-4e39BrNq0B9KI1tTjIDc9kUQMMJhb.y9_zIKcb3WcTXjdh
============================================================

## Zoom Recording Transcript

**Jared Freeze** 02:09 Dude, what's up?
**Martin Kuba** 02:13 Hey. Hey, Jared.
**Jared Freeze** 02:18 Thanks for all your help this week. I feel like we're really moving, so… Yeah, yeah, same.
**Martin Kuba** 02:27 Oh, yeah.
**Jared Freeze** 02:27 And walk out for the reviews.
**Martin Kuba** 02:35 Yeah, I don't want to.
Like, we've made a lot of progress, I think we just… it's… we just need to get it to a place where it's available to people.
So…
**Jared Freeze** 02:44 Yeah, absolutely.
Actually, to that point, the web vitals, the decision I made.
Was just to rip out all attribution?
So we're not dealing with semantic conventions or anything like that. There's 6 keys we need to agree to, which I think is…
**Martin Kuba** 02:59 Nice.
**Jared Freeze** 03:00 already in the conventions, right? Which is browser.webvital. I think we call it good. And then attribution
Actually, this is a question I had for Ted, was when you loop through keys that are programmatic.
Is that okay?
as Google adds keys to this third-party library, or do we need to have, like, explicit
names for particular keys, right? So they say, like.
delay time. And then they add delay time… Deferred, right, later.
And we don't have a semantic convention for it. Like, as you loop through the library, it would maybe automatically get picked up? Like, is that code that would be acceptable?
**Tedsuo** 03:49 I feel like I'm missing the context a little bit. What are…
What kind of keys and values are we talking about? I just joined in.
**Jared Freeze** 03:56 Oh, yeah, no, just, like, a general question of, like, third-party library, like, exposes, like, a list of just attributes.
Would it be okay to just loop through them and blindly add them to…
Like, a given list, or do we need to, like, be on top of every version of that library and add them as they… as they come in?
**Tedsuo** 04:18 I think we've discussed this in two ways. There's… and this kind of gets back to when we used to debate whether we used the body field or not in logs. But, there's, like, we're constructing our own stuff versus, this…
thing, this object, is like a system object. It's defined by the browser of this other system, and we just splat it in here, and that is, like, the definition of what you find in here in the semantic convention.
We've proposed that in the past for not
Wanting to have to do all of this work on the client side.
But I don't know if that was, like, back when we were maybe being more obsessive about efficiency over, like.
Being straightforward, potentially.
the advantage of thinking it through is that you're saying, these are the keys that you're gonna find in here, and, like, these are the dashboards. We added this information here so that you can use it in this way over there.
I think in general, we should… I would suggest we take that approach with the client.
Given our resource constraints and stuff like that.
But That's… that's just kind of, like, my shoot from the hip.
opinion.
**Jared Freeze** 05:40 Okay, yeah, I'll put up a proposal, because it's constantly changing, but, you know, again, you're relying on a third party to, like, not to delete anything. Right. I can't guarantee that, right?
**Tedsuo** 05:51 It's sort of like… I feel like when we record data, there's, like… I feel like I'm just… maybe it's just in the zeitgeist right now. I'm hearing a lot of, you know, about just, like, the cost and weight of, like, all the extra data that we record, just, like, in general, and, like, do nothing with.
And I kind of feel like when we're saying, hey, we're gonna record this information for observability purposes, we should always be like, why is someone going to look at this?
And if your answer is, like, this thing is changing all the time, it's some systems splat, we wouldn't use it for metrics or aggregates, but, like, yes, we look at this damn data all the time. It's important to have this in your hand.
Well, then that's the reason. It's like, yeah, you want all this data, it's in a log, it's just whatever the system splats out, we can't really control it, we're not going to try to track it, because we're not trying to use metrics, you just want to read it as a log.
If that's, like, worth the cost of sending that thing out, then sure.
**Jared Freeze** 06:52 Okay, cool. Yeah, a bunch of these are just, like, 4 keys that add up to the total you actually care about, and I'm like, do we really want to send all 4? But that's what we're supposed to decide, right? So…
**Tedsuo** 07:03 I kind of… yeah, I… my instinct is, like, we should favor sending things that we think are valuable, and, like, letting people bug us for the million little extra pieces they may or may not need, but…
Yeah.
**Martin Kuba** 07:18 And we also talked about in the past, about, like, if you had a use case like this, like, when you had… you just, like, take…
take something from the API, like, it's a huge, like, JSON or something, like.
For those use cases, you could just, like, dump the whole thing in the body of the log.
Right? So, like, the individual attributes that you want to aggregate on, or index on.
Like, we need to discuss those as attributes in semantic conventions, but you could…
say, like, for this API, like, we can dump everything in the body as well.
**Jared Freeze** 07:50 That's actually what I have right now, uncommitted, which is just, like, add raw body as a config, and then it just, like, literally jams in the entire attribution object that you get from Google.
So…
**Tedsuo** 08:03 Yeah.
**Jared Freeze** 08:03 Well, I appreciate the info, because I was sort of like.
**Tedsuo** 08:08 I feel like the body field in logs feels like an appendix for our purposes, right? Like, it's there because, like, other logging systems have this concept, and so we want to be able to, like, have an obvious place for them to put their stuff. But then, like, we've…
Feel like… it's always felt to me like we have a body field, and then we are trying to find creative reasons to…
To use it or justify its existence in, like, our spec world.
I do think it's reasonable to be like.
we put heavy stuff in the body, and you can just… if you want to turn a switch that just drops the body field, like, that's fine, like, we designed it so that you could do that. Like, I'm kind of tempted to say that's what it's for, the low-round.
**Jared Freeze** 08:51 Okay.
**Tedsuo** 08:51 stuff that you could leave behind, you didn't want it.
**Jared Freeze** 08:54 I mean, that's exactly what this is. It's extended metadata, so…
Okay, perfect. I will propose that. So, thank you very much.
**Martin Kuba** 09:09 Okay, I do have a couple things on the agenda. Let me share my screen.
There you go.
Okay, so I… we had a discussion, we've been having a discussion on this issue…
This one, for the versioning, trying to get to a place where we, can do a release.
There's been a bunch of discussion here, and…
Joaquin, like, you, like, raised the question about…
If we put all the instrumentations in… And… a single… Package…
then, tree shaking of third-party modules, would that work? I just… you know, I'm pretty sure it would, but I… so I… just to make it concrete, I created this… I put together this prototype.
Partially for this reason.
Let me see… yes. So…
This is in my fork. I did basically consolidate all the instrumentations that we have into this instrumentation browser package.
And then I also created, this… Bundler… bundler tests…
harness that… that, like, tries to bundle different combinations of instrumentations in the SDK, and checks that, like, things get tree-shaken, so it… they do. You can take a look if you want.
So that was part of the reason that I put together this prototype, and I also wanted to, just make it…
More concrete for people to look at, how the structure would look like, and…
Test if you want to test it.
With that, I would like to…
I think… I think I would like to, like.
Drive, like, to make a decision on this soon.
I think the… it seems to me like we're, in general, in agreement that we want to minimize the number of packages.
Maybe, like, the remaining question is, like, what they should be named, and…
That was my second related topic here.
Which is, we had two proposals, one…
was, browser, like, prefix browser-SDK package and browser-instrumentations package.
The other…
proposal, maybe this is minor, but, was to use the other way, so have… follow kind of the pattern in OTelJS, which is SGK. browser, instrumentation-browser.
In my opinion, like, one just makes it kind of groups packages for the browser. This, this kind of…
This naming kind of makes sense in the JS ecosystem.
But I'm not, like, really… I don't have a strong opinion either way, to be honest. I think, Jared, you had a third…
Option that you were proposing.
Which is… Just have a single…
just hotel browser package, that's the SDK.
And put the instrumentations in a separate package, but this…
That would be essentially just, like, a single browser package, yeah?
**Jared Freeze** 12:42 Well, I'm proposing two, so yes, the instrumentation package, and then, yeah, browser would be the SDK. I decided not to just add a suffix to it, because…
It really is the only other thing that I could see.
Now, the… I think the thing that would have to be decided is whether or not we do want to export instrumentation from that package. My proposal is to take just the stable and export them.
It does lead us down a road of, like.
what happens when navigation instrumentation goes from 1.0 to 2.0? Do we bump the SDK from, you know, 4 to 5?
I think it's a compromise. I would say maybe that's okay, you know, because you are actually saying, like, yes, something changed fundamentally in how navigation instrumentation works.
Did the SDK have a major bump? Technically, no, but, you know, if you want to have this convenience, I just want to make sure the entry point is super easy.
for adoption, I just want to minimize, like, how confusing it might be. But all the instrumentation playing together, I think, was good, and I think they're all
the problems.
All the peers are gonna work together.
I just… that was what I always think, just say browser.
And it'll be everything. Maybe, you know, you don't include instrumentation, it solves some of those problems, but you're not gonna know necessarily what instrumentation works with it.
So, I feel like having that instrumentation package alone is sort of like advanced users, like, that want to pick and choose, maybe within their own SDK for vendors, etc. For people that want to go pure hotel, I think they probably would not use that, I think.
they would just use slash browser. That was sort of my intent, though. Again, this major version issue I haven't really solved, but…
It's a comp… it feels like a major compromise.
**Martin Kuba** 14:49 So the one thought that I had about this proposal is whether it breaks the
the… the separation of API and SDK that's in the spec.
And I wanted to check with Ted, like, if you had any thoughts on this.
We… I know that the Android SDK actually does have a separate package or separate module for API.
Were they exposed by getting a session?
Like, if you wanted to, like, make it possible for users to, you know, have, like, a browser-specific API that they put in their code, and that they can replace the SDK behind the scenes if they want to.
like, you know, having, like, a single browser package, I think it…
May not make it possible, but…
**Tedsuo** 15:38 So, I feel like this sounds like something that's trickier in client in general, and in the Swift SIG, they decided to do this because of the way Coco works.
to just have one package that has the SDK and the API in it. And when you ship it, if you aren't using the SDK, it shakes out, but it does mean in, like, your CI and everything else, it's really heavy.
Because it pulls all that stuff in, and I know at least one vendor, Datadog, has been very frustrated with them, because they want to use the API separately, from the SDK, like, actively do that, and having it all mixed together,
creates trouble for them. It certainly creates a lot of bloat for them.
And so that was a… a dust-up in that SIG, because we've got it written as a sign on the wall that we would do this for people and let them have the API separate from the SDK.
So… So I would consider that that actually happened in the Swift SIG.
**Jared Freeze** 16:39 Well, I don't think… I mean, it's still gonna have the larger install size, but having a subpath for SDK should solve that problem.
where it's, hotel slash browser slash SDK, which, that endpoint only contains the SDK, and the API comes from core.
I think that would be fine, or even if we re-exported it with a compatible ver- like, whatever version we decide on for browser, like, slash API at the end.
**Tedsuo** 17:09 I feel like the package management, this part of JS changes so rapidly, I feel like an old man. And I… like, I don't feel like I have a great intuition to offer you guys, personally. All I can say is, like.
when we glued everything together in Coco, like, that created trouble, but that could be very different from this situation.
**Jared Freeze** 17:32 Well, I will say, one of the things that's different about, like, the JavaScript ecosystem and NPM in particular is that there's two main concerns. One is, like.
download size, where you, like, get everything, and then there's sort of… well, three things. Then there's, like, what gets pulled in and compiled. Then there's static analysis. So the big problem with core for web is the static analysis part, because all of this stuff
that goes with Node gets tree shaken, but a bunch of bundlers get really mad that it exists. Right. So, having the subpack import is really important. Once we do that, it solves a lot of the problems. So, like, the JSON serializer, for instance.
this… all of these proposals provide for that, so that way, if you do have a bundler that is a little quirky or doesn't do the right thing, you still have a set path import that's not going to pull everything else. So I think that's sort of a solved problem.
**Tedsuo** 18:24 It sounds fine to me. I… that's what… that's all I'm saying, is, like, I feel like the same thing with the Coco Swift discussion. It was all nuance about how, like, the details. It was not about…
someone being right or wrong in some, like, broad sense. It was just, like, who… whose toe is getting rolled over in the trade-offs we're trying to make? So, I don't know. This kind of feels like the kind of thing we'd want outside input
On, or maybe be prepared when we demo this thing to people, that This is something…
that people complain about, but, like, we should… we should just pick what you think is best, I think, and try to roll with it.
**Jared Freeze** 19:03 Okay. I mean, yeah, we can just…
**Tedsuo** 19:05 This seems like one of those things where you kind of want some practical feedback from the interop that has to go on with this thing, and just find out.
If… if someone's gonna have a problem with these choices.
**Joaquín Díaz** 19:19 I mean…
Ultimately, we are building this for users, and we want to do this the way that it's easier for people to implement it, so if we feel like there is only… that only one package is enough for everyone, and then you can just pull this package in.
and use all the options invitation that if that's enough for them, they don't have to worry or even care if there's an API. And then if they want to do its implementation, they can import the API from the same package.
I think that's the best for an end user, so…
**Tedsuo** 19:49 Yeah.
**Martin Kuba** 19:59 Okay.
I guess I wanted to…
Just, like, resolve it in my mind.
Whether, like, the spec about… the API is… applies specifically only, like, to the… signal APIs, like the…
You know, like, the trace, log, and metrics.
Or, like, if we…
like, we should be, like, thinking forward, and see, like, if we want to have some layer on top of those for API.
should be, like, prepared for that now. But it sounds like, even with this approach, we can introduce an API later and have it
You know, tree-shaken, so…
**Jared Freeze** 20:48 Just as a smaller detail, I think we've sort of been talking about, like, metrics not existing.
in the… On web, because it wasn't really a good use case, since it's, like, one user, one…
Session 1 library.
And the size, I think, was a major concern for everyone involved.
So I think it would just be the other two if we're gonna discuss it specifically.
**Martin Kuba** 21:16 Okay.
**Trent Mick** 21:19 Not totally unrelated thing that happened this week is there's a proposal being heavily discussed. It's early stages for having an OTel module and Node Core.
And the initial proof of concept there was just doing the tracing signal, and there were some comments about how all the signals are intertwined in the current JS node libraries, and how it would potentially have been helpful, at least for that initial effort, if
it was easier to just pull in the trace signal or do whatever, so, kind of related. Not… it shouldn't make any decisions here, but I thought that was interesting.
**Tedsuo** 21:58 I'm a little surprised that that happened. In the spec, we tried to keep them.
Totally clean from each other.
**Trent Mick** 22:05 Yeah, well, they kinda are, but life happens, so… yeah.
they pull in, like, they want some SDK package, and the SDK package is a convenience that sets up all three, so they take dependencies on all three, and… sort of… but mostly the API. The API that we've… that…
sorry, the JSOTEL API right now has… you pull in the API, and then it has .trace.metrics.
logs, I can't remember what the things are. Instead of being separate entry points, which is maybe, I think, what is being discussed here, that… I think the way it's right now is difficult for tree shakers to… to deal with, so…
Yeah, I think it's just… it wasn't thought about at the time, so that's not the way the API was designed, and if we were to do it again, it might be slightly different.
to separate.
**Tedsuo** 22:54 Yeah, we were… thought about ensuring that you could plug… you could use it piecemeal.
Not to the level, probably, of, like, tree shakers.
Being able to just complete.
**Trent Mick** 23:06 And I think exactly that. Like, API-wise, you can definitely use just one or the other, but I think now you're talking tree shakers, or… yeah, yeah.
**Tedsuo** 23:13 That's… that's tough. That's a tough.
**Trent Mick** 23:15 Or even installing, if you don't want to feel the size of it, because that discussion got a little bit off-tangent, talking about the bloat of, and they wanted a simpler version of, and like, well, okay, the bloat's there because… different use case, but yeah, okay.
**Martin Kuba** 23:38 Okay, so I think the next step here is…
If you have any more comments, please, please comment today or tomorrow, and I think the next step would be next week.
maybe I can… I can start open a PR to reorganize the packages, and we can, you know, someone can also
Start working on the, on the release, workflows.
Publishing workbook.
Okay, jared.
**Jared Freeze** 24:14 Yeah, so Fetchulator support, this got, proposed
I went pretty deep on it, as far as I could, on what it actually does. So, it's closer to a replacement for SendBeacon than Fetch with Keep Alive. So, Fetch with Keep Alive is the source code that underlies SendBeacon now.
Fetchulator is a little different. So, if you do not pass,
there's a new option, I think it's called Advance After. If you don't pass anything, it waits until page unload by default.
for everything you feed it. So, you call fetch later, it just waits. That's how it works. So, it's not quite…
like, an asynchronous, out-of-the-way, idle callback thing. Now, you can give it that value, and it'll say, wait till…
whatever value you say, 3 seconds, you know, 60 seconds, or page load, that's how that… that's how that value works. But it delays things quite a lot, and it sets you up for failure, in my opinion, which is that
you know, you're gonna queue a bunch of stuff, especially on a SaaS app with a lot of traffic, and then it's not gonna make it out the door.
Right? By default. So, you'd have to pick a value, all the… blah blah blah blah blah. The other problem is that it's fire and forget, the way Symbicin was, where it only tells you if it queues, it doesn't tell you if it's successful. Fetch with Keep a lot does do this, and is retryable. Fetch later, by nature, is not retryable, which I feel like kills it.
for how much you care about data integrity in OTEL, generally. So, I think it would be interesting to have it
on-page exit, because the queue size has doubled, that was one of the things that I think was a point of contention, is that everyone's fighting over 64K on page unload. This increases that, and also lets
The site itself set limits per origin, which is cool. And also, there's a much higher total limit.
But the not retry nature means it's really only suited, again, for page exit. If that's the case, you'd have to redo quite a… quite a lot of the code that's in there, so it's not just, let's drop this in, it's safer and sort of lens than it's idle.
Which I think maybe… I don't know if this author knows that or not. I certainly did not.
So, my… I'm saying no, basically. I think it's a huge refactor, and it kind of…
has a gap that I'm not really comfortable with.
**Trent Mick** 27:18 Well, if you could add those thoughts to that issue, that would probably help. On the note side, then we can decide that we're probably just gonna defer that, or say no thank you right now, yeah.
**Carlos Alberto Cortez** 27:28 Yeah, correct. That's what I wanted to say. Even if the group doesn't have an opinion, putting your own, you know, what you think about these, it would be great, you know?
**Jared Freeze** 27:41 Yeah, for sure. I don't know if anyone else is gonna respond, I just wanted to make sure I'm not, like, speaking on behalf of anybody, I just wanted to make sure it was, like, an opinion of…
You know.
It seems like there's a data loss
problem here that I don't think can be solved easily with the way the code's written currently.
**Martin Kuba** 28:06 But I think there is, like, a… maybe, like, a bigger question here. It's, like, how…
like, which kind of APIs we're okay with supporting?
In… in the browser SDK?
**Jared Freeze** 28:18 That's the other issue, is, like, we had talked about, like, baseline widely available was what I had put forward. That means it's in at least two browsers, and it has major market penetration. Fetchulator is Chromium only. The tickets have been filed for the other two majors, and they have not been picked up or discussed, so…
It's 80% of global traffic, right, Chrome?
I… you know, but it's, like, 50% in the US, because there's a lot of iPhones.
It doesn't seem good enough for me, but also, a lot of people are just like.
We had talked about Web Vitals, right? Web Vitals is specifically Chromium in the extended metadata, and it's so useful that I think we should make an exception, but we haven't really had rules around that, so… definitely a longer conversation. We clearly don't have time, but…
That was my two cents, is like, because it's chromium only, and it also has these issues, it would be really unstable in that
your expectations of what happens on page unload is, like, you have to know what browser you're in as well. Like, it's not really… you can't say this happens. You can say, this happens in this case, and it's biased towards this browser with this tool, which I felt like was a bridge to fail. Like, Web Vitals was missing with, like, certain numbers, and some get left out.
it's a little different, I think, than the fundamental nature of how the network transports open.
So, one of my two cents.
**Martin Kuba** 29:44 Yeah, I guess my feeling on this is that, like, the API hasn't been around that long.
That we don't… I don't know, like, if there's enough…
Kind of feedback on, like, if it's buggy or if it's working well.
**Jared Freeze** 30:01 It's not even newly available, which is in at least two browsers and under 30 months. It's still marked experimental. So basically, if something's in one browser, it is marked experimental by
MDN and W3C, and that's just the state of it, so I think at the very… at the minimum, we should say no experimental APIs as marked on MDN, like, easy to check.
I think that'd be a good starting place, and we can talk about newly available and widely available.
Literally.
**Martin Kuba** 30:29 Okay.
Alright, we are at time,
Tary, you have this session update, session entity update.
**Tedsuo** 30:40 Oh, it's just a question, yeah.
**Martin Kuba** 30:44 I've been, I've been looking at this, I don't have anything to share quite yet,
But I'm… I think I'm… I'm gonna attend the session… the entity SIG next week.
I have some open questions about… About this,
I think the one… the main thing to figure out is…
For me, from my perspective, is how instrumentations get… get notified… notified of… Entities being swapped, and…
How that works, like, with the global provider registration.
From my planet, yeah, so…
**Tedsuo** 31:20 Cool. I was gonna say, you know, our first, our, you know, our first order of bigness is we want to give feedback to the entity, SIG, because if we approve this design and we're happy with it, then they're gonna approve it.
But it does seem like this… we're heading towards a good moment to kind of, like, stand up a demo.
Of the whole thing.
Because I think that would probably also help the discussion around some of the things you just mentioned.
If people can just see it all.
**Martin Kuba** 31:50 Yeah.
**Tedsuo** 31:51 To the degree to which we've got instrumentation and everything, just starting to figure out what the right little demo environment is.
Food.
**Martin Kuba** 31:59 Yeah.
Yeah, so I have that exact thing in progress, and I can share that next week.
**Tedsuo** 32:05 Awesome. I'm excited.
**Martin Kuba** 32:10 Alright, we're at time, and… Thank you.
**Jared Freeze** 32:14 I think that'.
**Martin Kuba** 32:14 See you later.
