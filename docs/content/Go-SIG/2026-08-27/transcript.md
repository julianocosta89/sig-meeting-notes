SIG: GO SIG
Date: 2026-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:46 Hey, Mark.
**Marc Schäfer (T&A SYSTEME)** 00:47 Hi. Hi, Tyler.
**Tyler Yahn (Splunk)** 00:49 How you doing?
**Marc Schäfer (T&A SYSTEME)** 00:50 Braden, how are you?
**Tyler Yahn (Splunk)** 00:52 Doing well.
Yeah, just, cruising along.
Where are you based out of, Marc?
**Marc Schäfer (T&A SYSTEME)** 01:04 Germany.
**Tyler Yahn (Splunk)** 01:05 Oh, nice. At what part?
**Marc Schäfer (T&A SYSTEME)** 01:07 And close to Cologne de Sidoff.
**Tyler Yahn (Splunk)** 01:10 Oh, cool, nice, yeah.
**Marc Schäfer (T&A SYSTEME)** 01:12 So, in the middle.
Oh, yeah, in the most populated area, let's call it that way.
**Tyler Yahn (Splunk)** 01:18 Yeah, that's a good way to put it, yeah. Yeah, I've had a few colleagues, who've worked there, or in that area, the Cologne… Always close.
**Marc Schäfer (T&A SYSTEME)** 01:26 Traffic, always traffic.
**Tyler Yahn (Splunk)** 01:27 Yeah. Yeah, I can see that. Do you have pretty good public transit, though? Like, trains and things?
**Marc Schäfer (T&A SYSTEME)** 01:33 Trains, especially in Germany, is a special topic, because they are always canceled or delayed, and you can't rely on them. So if you have an important meeting or appointment.
don't use public transport. It will most likely… either you need to be, like, to schedule arriving 2 hours earlier than your appointment is, or not using public transport, yeah.
**Tyler Yahn (Splunk)** 02:00 Yeah, yeah, that kind of stinks, yeah. At least the traffic is a known constant, right? You're like, well, it's always.
**Marc Schäfer (T&A SYSTEME)** 02:06 Funny thing is, like, about 8 years back.
like, end grade, last level of school class, I was in. I had a driver license, and it took me 25 minutes with the car to get to school, and one and a half hours with the bus.
**Tyler Yahn (Splunk)** 02:27 Oh, wow. Yeah, that's a… that's a motivating factor to drive, yeah.
**Marc Schäfer (T&A SYSTEME)** 02:32 Yeah.
**Tyler Yahn (Splunk)** 02:33 Yeah, that's a lot of time. Oh, man. I don't know if I could do that.
Especially if you need to do transfers.
**Marc Schäfer (T&A SYSTEME)** 02:40 Yeah, and you need that twice… twice a day, so, like, going to school and then from school off, so, it's a lot of time wasted in the bus. You can do many stuff in the bus, like doing homework and other stuff, but not as good.
**Tyler Yahn (Splunk)** 02:54 No, absolutely, right? Yeah, it's… yeah. You could also just get home and just start working.
Yeah.
Yeah.
Wow, there's David… hey, Brian. Hey, Puneet. I don't think Robert's gonna make it today.
So we're probably actually at Quorum, so we could probably get started here in just a second. I see, David had added some things, we want to talk about, but if folks have other agenda items they wanted to talk about.
go ahead and add them there as well. And, if you haven't yet had your name to the attendees list, which I think everyone's, Marc, I think, may be the only one on there, but yeah.
I'll start sharing my screen, we can jump in here.
Cool.
Awesome. Alright, so David, you wanted to start us off talking about exemplar timestamps?
**David Ashpole (Google LLC)** 03:50 Yeah, we can get back to this. I think last time.
We had maybe walked through some of the options.
And… One of the requests was, like, what are other SIGs doing about this?
And so I did go look into… the other SIGs, and most of them actually just kind of accept the bug.
So… Java, Python, and C++ all just allow this to happen.
I mean, we could go ask them if it was intentional. I… I kind of suspect, given the spec language, is should.
That that was, like… like, it sort of makes sense that we would have put it as, like.
The exem… the exemplar should be before the end time, so that this isn't, like, a… a hard constraint on implementations.NET does do… The fourth option, which is just to move the end time to the end of collection.
So there is one… sort of piece of precedence. Nobody does the… triple buffered… Hot swap reservoir, and merge.
That I prototyped.
So yeah, I'm kind of fine with either switching it to be the end time.
For cumulative, we would keep the same behavior for delta.
Or… Leaving it as is, and accepting that occasionally you'll get an exemplar that's You know, just past your end time.
Yeah.
**Tyler Yahn (Splunk)** 05:31 How has Python do this if… I thought they were also single-threaded as well.
Like, if they're not, runs outside the aggregation lock.
Maybe my understanding of Python is out of date, but, like, I thought there was the GIL, and, like.
Wouldn't also have the same restrictions that JavaScript does?
**David Ashpole (Google LLC)** 06:08 That's a good point. That makes sense. I can double-check that.
**Tyler Yahn (Splunk)** 06:14 Yeah, well…
**David Ashpole (Google LLC)** 06:15 Python.
**Tyler Yahn (Splunk)** 06:16 Anyways, I guess maybe that's just, like, a tangent, because it's not really relevant, we don't have a GIL. So, like… Yeah, like, maybe that's just not, yeah, okay, so… Understanding the way it is, like, outside of, like, the language restrictions imposing it, like… And when you say .NET is no, it's no for cumulative, like, Delta is also, like, the same problem, right?
**David Ashpole (Google LLC)** 06:43 So Delta is different, right? Because Delta… you simply… you've… you can… Delta, it's much easier to have two reservoirs.
be… or… Yeah, Delta is much easier to have two reservoirs, because you're… clearing… After the thing, so there's no, like… like, the hard part with cumulatives is the whole, like, exemplars persist across collection intervals if they're not overwritten.
**Tyler Yahn (Splunk)** 07:12 Oh, okay, I'm saying.
**David Ashpole (Google LLC)** 07:13 Like, that's what makes this hard.
**Tyler Yahn (Splunk)** 07:16 For cumulative. So for Delta, it's correct, though, is what you're saying?
**David Ashpole (Google LLC)** 07:19 For deltas, it is perfect, right, it is correct. There's still, like, the tiny… race where…
**Tyler Yahn (Splunk)** 07:25 during that, like, switch of the reservoir route.
**David Ashpole (Google LLC)** 07:29 timestamp, but that, I think, is just worth ignoring for this.
**Tyler Yahn (Splunk)** 07:33 Okay.
**David Ashpole (Google LLC)** 07:34 issue, yeah.
**Tyler Yahn (Splunk)** 07:36 Yeah, I kind of feel like… With that understanding, like, seeing other languages.
being comfortable with this, and this is only for cumulative, like, if you're already doing cumulative, like, isn't it kind of implicit that, like, your backend is gonna, like.
Eventually see the next collection cycle that that exemplar is… belongs to.
It's just that, like… I guess maybe it's more of a question of, like, how it shows up on the backend, right? Like, if… You get the exemplar, and it's showing up in some sort of graph, and it's tied specifically to that collection cycle, and you have some bad collection cycles, like… that are maybe, like, a few minutes? Like, would it not show correctly into the next collection cycle? I think it would, right? Because, like, the exemplar still has a timestamp.
**David Ashpole (Google LLC)** 08:26 Yeah, I think the ingestion would likely be fine, and then I'll let Brian… Give his take as well. But… I would think that… I think the actual issue is, like, the timestamp is slightly… like, the end timestamp is sort of slightly off from It's not that the exemplar and the measurement ended up split, it's that… the timestamp.
That we're reporting isn't actually the timestamp when We stopped collecting measurements for the thing, right?
**Tyler Yahn (Splunk)** 08:59 Yeah, but the exemplar timestamp is correct.
**David Ashpole (Google LLC)** 09:04 Yes, the exemplar's timestamp is correct.
**Tyler Yahn (Splunk)** 09:06 Yeah, okay.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 09:09 Right. I wanted to suggest that the spec chose the word should.
Very intentionally, with the intent that you not worry too much about it.
**Tyler Yahn (Splunk)** 09:25 I mean, I don't know, like, I wrote the spec.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 09:28 Oh!
**Tyler Yahn (Splunk)** 09:29 Excellent. Yeah, like, I definitely think that, like… My intention was that, like, we want to try to get it correct, but, like, for languages that are literally, it's impossible to, like, we don't want to, obviously, have it be non-compliant.
But, yeah, to your point that, like, I think, like, us doing our best effort is something that, like, maybe is just, like, an edge case, And that we shouldn't worry too much about it, but yeah.
Yeah, I mean, I'm…
**David Ashpole (Google LLC)** 10:04 Let's see a witness.
**Tyler Yahn (Splunk)** 10:06 What's that?
**David Ashpole (Google LLC)** 10:07 I didn't realize you'd written the exemplar spec, or, like, this part of it.
**Tyler Yahn (Splunk)** 10:12 Yeah.
Yeah,
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 10:16 I think it's a good call-out, but Having done all this investigation, it definitely seems like the easiest way to go is to So, we'll just not worry.
**Tyler Yahn (Splunk)** 10:29 I kind of agree. I think that that's probably the right way to go, is just to say that, like, you know, we'll do our best. Obviously, like.
If the collection's… take a, you know, exceptional long amount of time, like, this could become a problem, but then I think we just wait for a user to complain, and I don't know if we will see that, and I think maybe let's just not have it be a problem until a user tells us it's a problem.
Like, in Prometheus, is this also something that is an issue?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 10:59 So, the… the… normal path, the time of the sample is assigned at the beginning of the HGB call, so… It's… it is… the same problem can occur.
And, I mean, I don't… I don't think anyone's checking. I… I have a… Quite a strong memory of, we used to have… we used to sort of log streams and streams of things saying out-of-order exemplars.
So we used to get upset with people Who somehow contrived to send exemplars in their… Where the time of a later one was before an earlier one, and we got upset about that because the data structure didn't fit.
And I… I think the code was modified to stop logging those.
Because they're… Yeah, I just… I mean, it sort of turns out in the wild that people will contrive to send you all manner of shit, and It's… it's pretty hard to… or it generally doesn't work out so well to try and reject things… Based on it being outside the rules, you have to try and be… Generous in what you accept.
**Tyler Yahn (Splunk)** 12:28 Yeah, I think…
**David Ashpole (Google LLC)** 12:28 Prometheus, because it's, like, the timestamp is… The server's timestamp, and the exemplar timestamp is the client's.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 12:36 Yeah, that's the default case. I mean, the… The exporter can supply a timestamp.
But the default case is it's… it's the server, and… It's kind of the time when the server intended to start collecting the data. You know, it's not even necessarily the time when it actually collected the data.
**Tyler Yahn (Splunk)** 12:56 Okay.
Well, I think if that's the case, there's even more stronger support to just say, like, this is a little bit of a fuzzy boundary at this point, and let's just move on.
Yeah, that makes sense to me.
does that kind of resolve this issue, you think, then, David?
**David Ashpole (Google LLC)** 13:19 Yep, I'm happy with that. I think that means… That we don't change what we're doing for histograms or sums.
**Tyler Yahn (Splunk)** 13:26 Yeah, yeah.
**David Ashpole (Google LLC)** 13:28 And I think we can unblock this other pull request. So I can, I'll leave a comment, and I'll close the issue, and then I'll reopen the… or mark this ready for review again.
**Tyler Yahn (Splunk)** 13:39 Okay.
Yeah, perfect.
Cool, awesome. Thanks for the work on that, David. Yeah, really appreciate it.
Okay, next up, Experimental Metrics API Surface. Yeah.
Cool.
I don't know if you wanted to jump in on this one.
**David Ashpole (Google LLC)** 14:05 Yeah, yeah, so…
**Tyler Yahn (Splunk)** 14:06 your work.
**David Ashpole (Google LLC)** 14:08 I'll just summarize by saying… Bound instruments are exciting, we've been talking about them for years now.
There is an experimental spec for it.
And… I think there's a few things about it.
One is that it's still experimental, so… Like… it's gonna be a large amount of code changes, potentially, in the SDK to support it.
If we do want to support it before it goes stable, and that means, like, just if things get updated or something, churn, and if the… if it never moves out of experimental, then it means, like, we've got, like.
You know.
I don't know, it feels like maybe even a quarter of the, like, aggregator would be kind of dead code, right? So, there's a pretty significant amount of complexity that comes along with this.
There's also… the spec is written today with flexibility in the API design, so unlike most of the APIs that say, like.
It must return, you know, foo method must return bar. Like, this one says, like, oh, it can return Either… A special bound instrument interface, or it can return the standard instrument interface.
So there's a good amount of flexibility in the API design.
Which means that even if the… even if it goes stable as is, we might get feedback from our users and decide, like, oh, hey, we want this other API design, so that Like, we can… Like, Still have that flexibility, right?
The other thing that I'll say is, currently, our contributor guidelines say that We will not support experimental API interfaces. So, when I originally wrote that, you know, 4 or 5 months ago.
It wasn't something that we had, like, spec'd out, basically, like, how we would even go about supporting something like this.
So right now it says, just, we will not support it. So if we did want to… try and support this with the existing SDK. I think we should at least document the… Like, duck typing, or whatever it's called. Basically, this pattern where… We define interfaces in a package that's experimental.
And then have… Our stable types, implement them in a way that doesn't That, if we were to change them, wouldn't break, goes… backwards compatibility.
Versioning schemes, right?
So, I think the… And then, Tyler, I don't know if you want to jump in and say, like.
So I think one path forward that I had originally planned was, like.
we would have these interfaces live in an X directory so that people could use them.
And the SDK would implement them, but it wouldn't necessarily be bound, like, required to keep that implementation. So we would be able to change it at the cost of breaking users that are doing, interface assertions on the stuff in the X package.
**Tyler Yahn (Splunk)** 17:25 Yeah, I'm guessing… You're asking me to jump in. So,
**David Ashpole (Google LLC)** 17:29 Yeah, yeah.
**Tyler Yahn (Splunk)** 17:30 Yeah, I mean, I, I… so… So first off, thanks on doing this work. Like, I think that that's… it's great. I think also there's a little bit of an echo chamber in here, because I probably suggested exactly what you just described, and then… I think you gave me the same critique that I'm giving you now, so it's a little bit of a reversal, which is… I think is hilarious, but yeah, it's just, Anyways, so the only thing is, is that, like, after sitting with this for a little while, and I've been thinking about this, is that, like, you know, you're gonna see things like this in the use of our SDK, and This counter is supposed to be stable, and, you know, there is no guarantee that this interface is stable, so this satisfaction may change in a minor version bump.
So, like, that's… that would cause a panic, right? Or, I guess, this technically wouldn't cause a panic. Yeah, that would handle it, but it could, is kind of the idea.
And so… the… the question I had is, like, is there a… is there… is there a way we can do this without doing, or introducing this instability?
And I think there is, it's just, a lot of work, is kind of the trade-off, obviously, but, like, the idea is, like, similar to, like, what you have is… this experimental X package, like, keep having those interfaces defined there. I think that's… I think that's fine. I think that's great. It's a great place to put it. I think there's nothing stopping us from doing that. It's just that then the implementation, I think, also needs to live in itself in the X package, so, I was actually super excited about this, because, I think this also gives us the ability to do, like, the remove method, which would be really sweet, and something.
**David Ashpole (Google LLC)** 19:21 Yeah, yeah.
**Tyler Yahn (Splunk)** 19:22 very much need in Obi, right now, but, or have needed, so much that we wrote our own.
So, yeah, I mean, I think this is an interesting idea, but essentially, it takes the implementation of our pipeline, and it moves… most of it's internal, but, like, it really puts, like, the core I don't know what else needs to go live in the core, to be perfectly honest. I think that, like, it's just, in theory, like, the core GO lives entirely internal. And then we expose certain parts of it in the metrics.
stable package that, you know, preserves that compatibility, and then in the X package, we, you know, essentially open up those, those features. So essentially, you have two different imports. If you import, like, the metrics package, like, that's a guarantee that it's gonna be stable. If you start using, like, the X package, under SDK metrics.
that's essentially a facade, but it opens up all these experimental features, which loses those guarantees. Obviously, we want to try to document, make that clear to users, not break things if we can, but, like, that's kind of the idea.
So, I think that that makes a lot of sense. And then… as we stabilize these things, or as they get stabilized in the specification, we obviously are going to have a lot of ability to use these, so we have a lot of, you know, trust that these are going to be available. And so, essentially, moving these into this package is, you know, it's a code shuffle to try to just open these up, essentially, in that other package.
Obviously, like, The big downside is the complexity here. I don't know of too many other downsides, honestly.
But it's more just, like, you know, how do things get shared across this? How do we make sure that, like, we restrict so that we don't open things up? And then, like.
Making sure that, like, you know, I think this stays… you know, somewhat manageable. The other option, obviously, is, like, you could just literally copy what's in the SDK metrics into, like, this X… I don't want to do that, like, that seems like a bad idea. It would definitely, I think, maybe even, like, use our templating system, which I think is, again, like, there's just already all sorts of problems with that, but yeah.
**David Ashpole (Google LLC)** 21:27 I was gonna say, I feel like we almost have to do that. At least, like… I feel like we would have to template the internal directory… So that we don't have the cross-module… Internal dependencies.
**Tyler Yahn (Splunk)** 21:41 Otherwise, the internal.
**David Ashpole (Google LLC)** 21:44 package becomes, like, a stable interface?
**Tyler Yahn (Splunk)** 21:47 It would… these are two different modules, is the.
**David Ashpole (Google LLC)** 21:51 They have to be, because we want one at zero dot.
**Tyler Yahn (Splunk)** 21:55 Yeah, you're right, yeah.
Okay, well then, I guess that's even more complexity, right? So there's gonna be some templating involved.
Yeah, I mean…
**David Ashpole (Google LLC)** 22:09 I was wondering if we could…
**Tyler Yahn (Splunk)** 22:11 So, so, but isn't that… So I think, Hmm.
Yeah, you're right, that would be a cross-module dependency. Okay, never mind, sorry, that's a half thought. Go ahead.
**David Ashpole (Google LLC)** 22:30 I was… I was wondering if… If we could… Like, alias all of the public?
things in SDK Metric X.
And then just… reimplement, like, Bind, I think, is an interesting use case, because… we could implement the code path entirely separately to support Bind.
Maybe. I'd…
**Tyler Yahn (Splunk)** 22:55 A road.
**David Ashpole (Google LLC)** 22:56 Not quite sure about that. Cool.
**Tyler Yahn (Splunk)** 23:00 Because you can kind of just, like, well, I… you can't entirely just wrap it around our existing methods, right, because there's optimizations we wanted?
**David Ashpole (Google LLC)** 23:07 No. So, it… We… we could… we could copy, yeah, it… We might be able to… Yeah, we would have to at least template the aggregators.
And then we would have to do some, like, collection time merging.
the outputs of 2, right? So, like, we could implement it like that.
It's very specific to the bind.
API. I don't think remove… like, remove wouldn't be able to be implemented that way.
**Tyler Yahn (Splunk)** 23:36 No, right, yeah.
Yeah, I think you're right. I think there definitely would have to be some… Like, I mean, even if… Yeah, I just don't think you're able to get around, like, the stable module.
dependency.
Like, I think you could definitely write it so that, like, the X would depend on the stable SDK metrics, but then internal, obviously, then just becomes unstable, because we're going to be changing experimental features in there that we would expose in the other one. So, like, that's not really… Yeah.
Okay.
Yeah, the only thing, I just really don't like that templating system, because, like, all of our tooling for GO really doesn't work on it, and it's pretty annoying. Obviously, like, you can write it in, like, GO and then copy-paste it into the template, but, like.
It's annoying, yeah.
**David Ashpole (Google LLC)** 24:34 It's like, I don't know if it would be worth it to me. It's like, maybe for this feature in particular, because I would like to see bound insurance happen, but, like, for experimental features generally, like, I wouldn't be willing to carry this burden.
**Tyler Yahn (Splunk)** 24:50 I… I… I'm kind of willing to carry it for this and the remove feature.
there's so many bugs in Obi's SDK pipeline that I'm fixing that we've already fixed here, that it just, like, bothers me that, like, we don't… views.
**David Ashpole (Google LLC)** 25:06 Oh, yeah.
**Tyler Yahn (Splunk)** 25:07 This right now.
So, like… Having that feature would save me a lot of development effort.
But… Yeah, I also get… why it's not… I mean… Yeah, maybe… so…
**David Ashpole (Google LLC)** 25:30 Can we go back to the top of the issue, actually? So, like, Am I understanding correctly that Am I reading into this that you would like to use this in OB as soon as it's released in the X package?
**Tyler Yahn (Splunk)** 25:43 Yeah.
**David Ashpole (Google LLC)** 25:44 Okay, cool, like, that makes more sense, because I was like… It's kind of like, well, who cares, you know? The only other thought Right. Well, I was like, who cares if this is just for people to play around with, right? It's in the X, you know, like, use it if you want, might break.
**Tyler Yahn (Splunk)** 26:02 Yeah.
**David Ashpole (Google LLC)** 26:03 If it's just to get it out there so that we can show, like, hey, you know, we reviewed this, and we like it, and we want the spec to go stable so we can put it in the regular thing.
Yeah. If we're gonna use it in OB, then yeah, I would feel less… Okay about making it silently stop recording your metrics.
**Tyler Yahn (Splunk)** 26:19 Well, I do have… I guess I gotta qualify that. I would use it immediately if we also include the remove. Like, I can't use it unless there's a remove, because, like, we do need that, so if you just add binds, then yeah, it would kind of be in that category of just, like, it's just a prototype, but yeah.
**David Ashpole (Google LLC)** 26:33 I'd be down to implement remove. It's not in the spec yet, unfortunately, but…
**Tyler Yahn (Splunk)** 26:37 Yeah, it's not even experimental.
**David Ashpole (Google LLC)** 26:39 Maybe we could… I don't know, maybe we can be brave and go beyond the spec a little bit.
But then we're kind of tied to something.
to support OB, that… any, anyways.
**Tyler Yahn (Splunk)** 26:50 But Hobie's, like, like… I'm more comfortable adopting experimental features in that metrics pipeline, given I control Obi, and the upgrade path is something I can handle. Like, that's not too scary to me. As long as, like.
I don't know, I don't get hit by a bus, maybe? Even then, like, I think other maintainers there can come here and fix things, so, like, it's not… that doesn't bother me too much, yeah.
**David Ashpole (Google LLC)** 27:17 Well, it just means, like.
Like, I feel like once you rip out your custom SDK in OB, you're not gonna, like, wanna go back.
**Tyler Yahn (Splunk)** 27:25 Oh, definitely not, no.
**David Ashpole (Google LLC)** 27:27 It's like, I kind of… once it's in the X package, I feel like we're, like, we own these things forever.
**Tyler Yahn (Splunk)** 27:33 Yeah, but I mean, like, I, like, literally, we've already forked it once, like, we could just fork the X packages as well, so, like, it's not, like, the end of the world, but yeah.
**David Ashpole (Google LLC)** 27:40 Well, if the SDK removed the actual… like…
**Tyler Yahn (Splunk)** 27:46 Like, if… If we went with…
**David Ashpole (Google LLC)** 27:47 the initial proposal where the logic is actually in the SDK, and you're, like, essentially.
**Tyler Yahn (Splunk)** 27:51 Yo!
Yeah, yeah.
**David Ashpole (Google LLC)** 27:53 I don't remember what Ben, like.
**Tyler Yahn (Splunk)** 27:54 That would be… yes, actually, that would be way more problematic, because then, yeah, version upgrades could really cause issues from an external standpoint, yeah.
Actually, version upgrades could still cause a problem on the other one.
Yeah.
That's okay, though. I'm not too concerned. Like, our compatibility guarantees on the OB package are not specifically around it being a module, it's more about it being a distributed object. So, yeah, I think that that's… that's actually fine for me, but… I guess it wouldn't really matter if I… either way.
I'm sorry, you got your hand up? Sorry.
**David Ashpole (Google LLC)** 28:37 Jump, jump in, yeah, yeah.
**Puneet Singh** 28:39 Yeah, I just had a small question for this thing that, when you're… Implementing experimental features, Is there a general criteria on when you want to push beyond what Currently, SPAC is a scope 2.
And when you want to restrict, you know, like, within the scope and get the PR Shipped, and then worry about the extended features.
**Tyler Yahn (Splunk)** 29:10 Yeah, I mean, like, definitely… so in this case, I think it's a good one, is, like, sometimes the spec does include experimental features, and this is one of those experimental features. So we want to try to provide some way to validate that, because the spec… it's like a little bit of a chicken and an egg problem.
The spec requires prototypes for experimental features to become stable, even to be accepted sometimes. And you can't really have that without a language trying it out.
and GO is usually a problem child, like, we usually find edge cases that other languages, like, are like, oh, that's not really an issue, and we're like, actually, that's a really big issue.
So, like, having us being able to do that is kind of one of the big priorities. And, like, we have… most of the times, like, we're able to do that. Like, this is one of the first cases where, like, it's digging deep enough into the systems and, like, the SDKs where we have stability guarantees that are getting in the way of this.
that, like, this is starting… this is, like, the first time where we have, like, these kinds of problems. You can look, there's a bunch of other X packages that are, like.
new features, where essentially you just turn them on, and, like, they're not really, like, you know, there's no API surface, essentially, that comes out of it, so it's a lot easier to actually get this to work or not.
Other things like this remove method, I think it's, like, that's definitely way more of a gray area, Because it's something… it's something that there's, like, real use cases on, like, obviously Obi's using it, Obi's implemented it, and, like, it's been in the spec, there's an open issue in the spec for a few years now, so, like.
Yeah, I think that's probably worth talking about. Like, there's no guarantee that, like, we should accept it. Like, the… having these features, obviously, is gonna have a developmental burden on… so, like, the maintainers… on the project are the ultimate people who are going to be responsible for maintaining that, and I think that that's really where I would say that's the line of, like, yeah, these are… these are gonna be owned by us, so, like, if we're willing to support it or not, is kind of like… it has to get motivated. Yeah.
**Puneet Singh** 31:04 Right, I mean, like, one has to take or understand that it might be possible that this becomes part of a spec, but it's also possible that it get reverted because it doesn't find enough adoption. In either case, you have responsibility to make sure you end up on the clean side, whether it means dropping the entire feature or otherwise.
**Tyler Yahn (Splunk)** 31:26 Yeah, exactly, exactly.
So, I don't anticipate bind, but yeah, that's… that's the worry here. Like, say, you know, the spec goes, like, actually, bind's a horrible idea for some reason, and they're like, let's make sure that, like, we don't define it, like… then we have a choice of whether or not we're gonna go beyond the spec, or we're gonna literally drop it, and if we have an interface satisfaction that we're saying, like, now the SDK no longer satisfies this interface, like, that's… that can be very problematic. So, yeah.
But I think, I think the buying one's more of a concern of, like.
in the evolution of it, they come back and say, to stabilize, we want to, like, harden up this API interface, and, like, we're gonna require it be in a particular form, and we don't have it in that form, so to stabilize it, we have to put it into that form, is kind of, like, the problem, and that's… that's also problematic for GO, hence why we're, like, the problem child, yeah.
**Puneet Singh** 32:16 Got it.
**David Ashpole (Google LLC)** 32:17 Tyler, I was wondering if there's… is there any way to do, like… Compile time, or… Similar assertions on… whether the… Types match.
Like, it would be… It would be easier if I could, like.
add in, like, in OB, you know, above my usage, just say, like, you know, underscore… X.int64Counterbinder.
is implemented by… you know, I guess you can't just, like, get the SDK type.
Maybe, but if there was some way for, like.
**Tyler Yahn (Splunk)** 32:59 Like, to guard it, you mean?
**David Ashpole (Google LLC)** 33:02 Like, to guard it at compile time would be…
**Tyler Yahn (Splunk)** 33:05 Yeah, yeah, you can do that. I mean, like, we definitely do that in, like.
**David Ashpole (Google LLC)** 33:07 Try and do a version bump, and it just doesn't compile unless you bump them together, kind of thing.
**Tyler Yahn (Splunk)** 33:12 Yeah. The only… the only problem there, though, is that, like.
It's… it's the… the user who has to put that guarantee in.
And so… so we can't, like, require it turn into, like, a compile time error. We can only.
**David Ashpole (Google LLC)** 33:26 Yeah.
**Tyler Yahn (Splunk)** 33:26 Expose it in a way.
So there's always gonna be, like, like, the… pathological case where somebody's gonna be like, well, I didn't do that, and now my code's panicking at runtime because I didn't do that. Like… you're like, well, you should have done that, and you're like, well, the GO compatibility guidelines say that I shouldn't have to do that either, so, yeah, that's the thing.
**David Ashpole (Google LLC)** 33:52 Do you mean that, like… Just to be clear, do you think that having it Exposed on a method.
This should be a question we can actually, like, get to the bottom of.
from your understanding of the GO compatibility guarantees, if I expose… like, if I have an unexported type, like.
N64 counter.
that I return that implements, like, the counter API, right?
And I add a method on it, bind, that's public.
Is that part of my… if I break that method, is that breaking my… compatibility guarantees… according to, like, GO versioning? Do you know…
**Tyler Yahn (Splunk)** 34:38 Yeah, so, yeah, like, I think… I don't think it's exactly said this way, but, like, the gist from some of the maintainers and the authors of GO are, like, if it compiles in one version, it needs to compile in the next. Like, that's actually their guarantee, it's not actually a runtime thing.
Hence why 127. Anyways, but like… So, yeah, like, that… and we can't guarantee that at that point, right? Because you can set it up exactly like you're saying, like, you can build these compile time assertions that, like, an interface is satisfied, and it would not compile as you go through an upgrade. And so, yeah, that would violate that.
**David Ashpole (Google LLC)** 35:13 I was trying to f- I don't even know if you could… it's like it would be useful if you could do that, but I don't know if you can write that compile time assertion, because… So we actually do…
**Tyler Yahn (Splunk)** 35:24 We have an example of this in our, like, API… What do we call it? The,
**David Ashpole (Google LLC)** 35:36 Essentially, tapes.
**Tyler Yahn (Splunk)** 35:37 Yeah, yeah, yeah, sorry, the embedded types, yeah. Like, because we include, like, this private method thing in there, that's kind of actually implicitly doing it, so users can come in and say, like, I want to turn this into a compile time error, I want to turn this into a runtime error, I want to turn this into a no-op, and so, like.
Yeah, that is one way to do it. Like, you can look and see, like, how we do it there. But essentially, like, you could then re-implement the wheel for all these other methods, that you wanted to sort, you know.
Define that on.
I definitely think it's a breaking change for the SDK in, like.
**David Ashpole (Google LLC)** 36:10 You do, okay.
**Tyler Yahn (Splunk)** 36:11 Yeah, like, that… I definitely think that that, like, it can be considered, and I think that that's valid, like, I think somebody can come to us and say, like, you violated this, and we'd be like, yeah, that's pretty true, yeah.
**David Ashpole (Google LLC)** 36:25 Would it?
would it ever actually panic? I guess… is… there's the function signature where you, like, get the thing back.
And…
**Tyler Yahn (Splunk)** 36:33 Well, it can panic, or… yeah, I mean, it… yeah, there's always these pathological cases. Like, take out that okay in that if statement that you had, and then…
**David Ashpole (Google LLC)** 36:40 You can't do it without that. It'll panic, it won't return nil?
**Tyler Yahn (Splunk)** 36:44 Oh no, it'll panic. Yeah, which is why they say you should probably always do this, but yeah.
Yeah, and then you can turn it into a compile time error as well, but, like.
again, like, kind of pathological cases, and it's not really defensive code, but, like, that doesn't really matter. Like, it's a part of the GO language, and, like, that's supported, structure and syntax that we want to try to support, yeah.
So… like, David, maybe it's worth, like… I'm guessing you're looking for some help on maybe prototyping this?
**David Ashpole (Google LLC)** 37:26 I… I think… I think it would be helpful just to make sure that we can assemble all of our options. I…
**Tyler Yahn (Splunk)** 37:39 Right.
**David Ashpole (Google LLC)** 37:41 I'm… I'm still, like, kind of iffy on whether I consider it breaking, so I want to go… look into that a little bit more. But yeah, I'd appreciate any help, especially if you want to dig more into… or anyone else, obviously, wants to dig more into, like.
What we could do.
to provide… Like, an SDKX package.
But… has, like, I assume the full surface area of… Right. Or… it would have to have the full surface area of the SDK, but then support experimental API features. Like.
figure out if we did do that, what would it look like? I feel like maybe we sketched it out here, that there would be some sort of… Some amount of, like, templating of… portions of the SDK.
Yeah, figuring out what our alternatives are. And then… I guess the only final thing is, like.
The other thing we could do is stick with just prototypes.
And… Way Bronco Stable.
Yeah. I… right, I'm also happy with the branch. I feel like… The hard part about This is that the feature is so complex that it… it's like… I feel like the exercise of reviewing it.
You know, and having, like, multiple people go over it, and, like… ironing out all the issues, because I'm sure, like.
Even though I've worked on it for a while, I'm sure it's not, like, perfect.
Would give a way better signal that it's actually, like.
That this act… like, if this all hinges on, like, the compiler optimizing something away, and… The implementation's broken, and it wouldn't… you know, like, those sorts of things, like… I feel like until we get this merged in a more, like.
Or merged, or, like, put somewhere in a more official way, where it's been reviewed, and, like… tested and stuff. I don't feel like I trust… I don't feel like it's enough of a signal for this spec.
I don't know.
**Tyler Yahn (Splunk)** 39:40 Yeah, and this is, I think, where I really wanted it to be, like, in a nice package, because it could not only be, like, there and reviewed, but also used.
Like, that, I think, is gonna be a better signal, is, like, you know, we start using it in Obi, or, you know, we have users downstream using it, and they're reporting bugs against it, like, that's, like, oh, that's actually, like, oh, there's a memory leak or something, right? Like, that would be really helpful, yeah.
But… I… yeah.
I think it's also one of those things where you put it in a branch.
We're getting a lot of, like, updates to the metrics pipeline currently, and, like, fixes and things, like, it's pretty quickly gonna be out of date, I think is also the other side of the equation.
**David Ashpole (Google LLC)** 40:22 Right. Which… If the goal is just to prove that it… Right, if the goal is to get it actually used, and… you know, get that kind of feedback, then I think it… that's not good enough.
if it's just to, like, get it… Reviewed and hosted somewhere.
So people can try it out, then maybe it's okay?
**Tyler Yahn (Splunk)** 40:44 Yeah.
Yeah, I'm also, like… one of my other goals is, like, I'd love to have the bind and the remove method, right? And if you put it in a branch, like, you're probably just gonna have one or the other. So, you can't really do both, yeah.
**David Ashpole (Google LLC)** 40:58 We're gonna end up building, like, a second.
**Tyler Yahn (Splunk)** 41:01 Yeah, or 3rd, and then fourth, yeah, exactly, yeah.
Yeah, so I… okay, I can think more on this.
And probably try to get a prototype, maybe today or tomorrow, working on that. So, yeah.
Yeah, that sounds good.
**David Ashpole (Google LLC)** 41:20 Cool, thanks.
**Tyler Yahn (Splunk)** 41:21 Okay.
Cool.
Cool, that's the end of the written agenda.
Any other topics folks had? Things they're working on?
Top of mind?
**Puneet Singh** 41:34 I have one more doubt, actually, regarding, implementing experimental features.
And I'm still… consider myself, like, somewhat fresh to go and trying to figure out stuff.
So… because of this restriction of… Not able to add experimental methods on the stable package.
One race.
**Tyler Yahn (Splunk)** 41:59 SDK package, by the way.
**Puneet Singh** 42:00 Sorry, yup. One thought I had was that, why can't I have, like, an experimental package for, meter provider, because it is big, and it has a lot of private, you know, like, functionality which is not exposed, so you won't be able to, reuse those. But is there a challenge against, making them visible so they can be reused, or you end up replacing with the components you want to override. One downside I could say is that you will end up making a lot of stuff public, which is not ideal for the surface area of the API, but I just wanted to understand that if there are any other issues with this approach.
**Tyler Yahn (Splunk)** 42:50 I think I'd have to see some of the specifics you're talking about, like… If there's, like, use cases for… So the meter… the… meter provider, did you say? Or, I'm sorry, did you just… or the reader?
**Puneet Singh** 43:07 So, I'm working on this meter configurator thing, which needs a new method on the meter provider, but… Because it's a stable, package.
I cannot add that directly, and I, Add it as an option in the experimental package.
And… one thought I had was that if I could have an experimental package for the meter provider itself.
Or I could create one. I could add the method on… on the, experiment… experimental version, but I cannot do that because, meter provider has, like, a lot of stuff inside.
And a lot of things is, like, not visible, outside, and because of that, it's just not… possible to create one, or it's a huge endeavor to create a, you know, like, experimental version of meter provider, actually. That's my feeling on this, but… I haven't tried it, I'm just… I was just thinking that, it would be better.
**Tyler Yahn (Splunk)** 44:18 Yeah, that's actually true.
**Puneet Singh** 44:19 Yeah.
**Tyler Yahn (Splunk)** 44:19 That's actually, I think, what we're talking about, is what you're describing, is that, like, we would have an experimental meter provider, and then that would give you access, or you could plum in the access that you needed into that.
In the experimental package, but… Yeah, that's actually kind of the plan that David and I are proposing.
**Puneet Singh** 44:39 Got it. I mean, yeah, I was like… maybe I was thinking, like, too basic, and, you know, maybe this, I mean, there might be some other approach compared to this, but… but yeah, then it's okay. I'll spend some more time on thinking about this, yeah.
**Tyler Yahn (Splunk)** 44:54 Yeah, I mean, and that's… I would also say that, like.
if you can get away with not doing this, and not, like, partitioning and putting experimental features in this other type, and you can use, like, a flag, I would do the flag option to keep it in, like, the stable package, because One… it's really… annoying for users to have to switch imports to get this to, like, you know, upgrade. And also, like, any sort of other experimental features, you don't have any, like, an on-off switch anymore. It's like… you would have the experimental meter provider configuration, plus the remove method, plus the bind method, and, like, maybe, like, there's bugs in one or the other, and, like, that would cause, I think, issues for folks, so… if you can do the option pattern that you're already doing, I would probably say we stick with that, but… If there's, like, blocking issues like this with the bind thing, then maybe we'd think about it, differently.
Yeah, but again, like, I… maybe if there's more details, on what you're thinking, I could…
**Puneet Singh** 45:57 I mean, yeah, it's still just, you know.
thought, you know, it's still yet to… in order to be a conclusive argument, it has to, like, supplement it by some concrete experiments, so, yeah.
**Tyler Yahn (Splunk)** 46:11 Yeah, yeah.
Yeah, absolutely.
Okay.
Well, cool.
Any other topics folks, have?
Things we're working on.
If not, we can end the meeting here. Yeah, thanks everyone for, joining all the conversation, and yeah, we will see y'all in a week's time.
Or asynchronously. Till then.
Right? Bye.
