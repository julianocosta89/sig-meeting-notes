SIG: Go SIG
Date: 2026-04-09
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:32 Hey.
**David Ashpole** 00:39 Hey, Tyler?
**Tyler** 00:40 How's it going?
**David Ashpole** 00:41 It's going well.
**Tyler** 00:43 Nice.
Are you in the office today?
**David Ashpole** 00:47 Yep.
Just a green room today.
**Tyler** 00:51 Oh, nice.
Is today the 9th? Okay, interesting. It is upon us. Hey, Paula, and Arthur, and Brian, and everyone.
**Arthur Silva Sens** 01:31 Hello!
**Tyler** 01:33 Y'all doing?
**Pellared** 01:34 Oh, Mr. Sue.
**Arthur Silva Sens** 01:39 Good, how are you?
**Bryan Boreham** 01:40 Good, thanks.
**David Ashpole** 02:09 Go ahead and add yourselves to the attendees list, if you can.
**Tyler** 02:14 Yeah, we could probably get started here in just a second, sorry, just, loading up my computer. But yeah, yeah, if you can, please go ahead and add attendees, stuff to the attendees list. I have added an agenda item to talk about Prometheus here in the beginning.
If I remember correctly, that's what most of the people are here for. And so, I can start sharing my screen here in just a second, we can jump in.
Cool. Alright, yeah, welcome everybody. So, yeah, I, admit I'm a little bit behind on this, but, if I remember correctly from conversations at KubeCon.
And David, I don't know how up-to-date you are on this one, but there's a talk of… This is where I'm gonna step out of turn, but, integration with Prometheus and the OTEL Metrics SDK, and trying to do some sort of replacement, trying to do some… something along those lines. Performance is a concern there, and I think that there is a need for a discussion on this, that I'm guessing a lot of people on the call are here for.
So, I could probably hand it over to someone who can speak more to this topic. I don't know if that would be Pablo, Brian, Arthur.
David? I don't think David, because I don't know if you've been in the conversation, but yeah.
**David Ashpole** 03:36 Yup.
**Pablo Baeyens** 03:39 I think it would be interesting to hear from Brian and David, and even if David hasn't been in the conversation, you are the one that did a bunch of performance improvements, on… or… Yeah.
**David Ashpole** 03:52 About how much more.
**Tyler** 03:54 Maybe it's more about, like, the background, though. So, just… Brian, I know you were in the conversation, and you… There was a meeting at KubeCon, and it was around, the Prometheus, I think, update… don't quote me on this, and I'm hearing this secondhand. But the idea is that, like, the Prometheus world was looking to use, or maybe even replace with the Metrics SDK. The Metrics SDK has performance limitations, and the API has performance limitations.
That were blocking or causing concern?
**Bryan Boreham** 04:24 Yeah, I would… I would say the uncomfortable situation is that… that we have a… We have a world where… where… there's a declared standard, open telemetry, and a kind of a de facto standard, Prometheus.
And people… look around and say, well, what does that mean? What am I supposed to do?
And the answer is, well, do you want it to be standard, or do you want it to be fast?
And, you know, that's one of the choices, which is very, very clear.
From… from everything that we've tried, everything that we've done, and… Then there's a… there's a related point, which is, do you… do you want it to be standard, and really, really flexible, and have a particular data, you know, complicated data model, or… do you want, quite a simple data model in the API, which is… which is more… more the Prometheus case?
So there's those, there's those two… axes of choice.
and… I certainly find it uncomfortable to just, sort of, leave the choice with the rest of the universe. Well, I suppose… most of the people… most of the people who are, like, on the customer side who I do talk to, or hear about.
they say, well, I think I'd rather have a standard.
And then that… that kind of makes me sad, because that means that stuff is just gonna run slow for the rest of time.
**David Ashpole** 06:05 Oh, hey, Jack. Welcome.
I mean, are people interested in, like, Just me covering what… the current state is? Like, what's been done?
Yeah, okay, I got a thumbs up from… One… two nods. Okay, so… I think Julius wrote a blog a while back, while I was on leave, maybe last summer.
comparing the two, and I think the differences he found were somewhere on the order of, like, 50X?
In terms of how expensive it was to increment a counter, in OpenTelemetry versus… 4X at best.
I think that may be more recent.
Basically, it was a lot worse.
Back mid-last year, and we made some improvements. So, one of the things we did is we started hashing the labels as they come in.
Instead of using… our big struct as, keys. And that… that addressed some of the worst-case scenarios, because if you had a really, really massive list of attributes, then Go would take a really long time to, like, perfectly Hash that and do lookups for it.
And the other thing I was able to address without any API changes has been… the way locking works? Yeah, so there's the blog. The other thing I've been working on is… improving how locking works in the metrics SDK, so… Previously, we had just, like, a global lock per instrument.
And so if you did a lot of concurrent Rights to the instrument, you would get really high contention, and it would be really slow.
So now we've adopted, I think, most of the optimizations that the Prometheus Libraries have made.
Using atomics, using, either read-write locks or sync.maps.
For attribute lookup, and so that aspect of it is now On par, more or less, between the two libraries.
I think the biggest… the biggest differences… Are… mostly come down to… Oh, what's the thing called?
bound… bound… like, Prometheus has bound instruments, so if you pre-bind a counter.
You can do counter updates in a couple nanoseconds.
Really quickly, without any attributes.
But in OpenTelemetry, even though You can pre-make your… like, attribute option, and store that, and not have any allocations, you still end up doing the map lookup each time. So, instead of it being, like, 7 nanoseconds, it ends up being closer to, like.
60.
In my testing. So, it's a big difference, but they're both not… Not, like, huge numbers. So that's one gap that currently exists today, is in the, like, the prebound instrument, Section.
Arthur?
**Arthur Silva Sens** 09:23 just… just clarify what you said about a few nanoseconds, and it's not a big difference?
Sorry, sorry.
**David Ashpole** 09:33 the absolute values aren't… aren't huge, but I… the… You're right, it is a big difference if you need that.
**Arthur Silva Sens** 09:42 Yeah.
**David Ashpole** 09:43 There's some cases, I understand.
**Arthur Silva Sens** 09:44 when working at the Go SDK in Prometheus, like, when we do, like, a few nanoseconds.
regression, we get 5 issues open immediately, right after the release, because, like, this is a big difference for instrumentation.
**David Ashpole** 10:01 Right, and yeah, I guess OTEL probably hasn't seen that, because the users who need a You know, 3 to 7 nanosecond counter increment probably aren't using our library.
So that's one difference, is if you… if you have We don't have bound instruments. We could introduce that and meet those needs.
The other difference is mostly, we… It's difficult to explain succinctly.
But, essentially, when you pass attributes to us today.
We copy the attributes no matter what.
And Prometheus, when you pass attributes, it's able to first do a hash of them.
And then do the lookup just with the hash.
And then only do the copy if the attribute set doesn't already exist.
So… That's another big change, but that, we've discussed, would require some changes to our API.
We had discussed maybe doing, like, an unsafe version of it that I think might be able to avoid this.
And then there are some other smaller differences. But those, I think, are the two big ones.
**Tyler** 11:20 A caveat on that one, though, that's only for dynamic attributes, too. Yes.
**David Ashpole** 11:24 only for dynamic attributes.
**Tyler** 11:26 So if you have, like, a predefined set of attributes, like, there are ways to avoid all of this, like, performance overhead. But yeah, for the dynamic attribute, we have looked at this, and we have looked at, like.
updating our APIs on these options as well to just reuse those allocations, to avoid this in the API, but yeah.
But other than that, like, I don't… I think, David, that's pretty comprehensive about, like, all of the performance differences that you found in between these two, right? And, like, we are still actively working to address these.
**David Ashpole** 11:54 Yeah, I mean… We, we are. I think, Yeah, Bound Instruments, it sounds like Jack is, interested in kicking this off at the spec level.
That would be… I think a larger change, and then we're looking at some smaller changes that we could make.
To make this possible.
I don't think we will quite get to the level for dynamic attributes, I don't think we'll quite get to where Prometheus is.
But we could get, like, within 2X.
Which may be close enough for some users. Like, we could get close. I think… Like, this time last year, we certainly weren't.
anywhere near. And, it feels like we're… We're making improvements over time.
is all I'll say.
**Tyler** 12:45 So, I guess I kind of want to, like, back up and ask the question of, like.
We're doing a lot of performance improvements here, but we're doing it kind of because we think that, like, our users will benefit from it, but I'm kind of confused about what the end goal of Prometheus is in this conversation, like… Are you looking for something from us? Like, I… like, we… we like performance improvements for performance improvement's sake, but, like, it sounds like there's maybe a blocker that you guys are waiting on us from?
**Arthur Silva Sens** 13:14 I think the problem is the way the two communities are communicating.
where Prometheus is communicating, hey, we are the most performant ones, you should be using ours, and then it'll tell… Are also saying you should be using ours, but for different reasons, and it's not clear for the final user.
What those reasons are.
**Bryan Boreham** 13:43 I think there was another, thing discussed, which is… Given… given the enormous amount of code using the Prometheus SDKs that has grown up over, whatever it is, 14 years.
Could we, could we… could we kind of bring that into the envelope of, hotel? And… and I think, you know, we discussed that pretty rigorously at the meeting in Amsterdam, and… and… mostly that seemed… well, down at the SDK level, that was a flat no. Up at the exporter level, that was, let's see what we can do. And then it kind of comes back to the performance point, because you… you don't really want kind of the same thing, but slower?
So… Yeah, okay.
**Tyler** 14:42 Yep.
**Bryan Boreham** 14:42 Yeah, there, there was, there was that, that… you know, I think… I think that's an answer to your question. There was this whole other conversation that was like, well, can we… Can we solve this whole thing by… taking the Prometheus code and doing something kind of legalistic with it, and that… you know, we talked, we had a good discussion about that. It was a no.
So we don't need to go back over that.
**Tyler** 15:12 Was the… was this meeting recorded, by chance?
**Arthur Silva Sens** 15:16 No…
**Tyler** 15:18 Okay.
**Pablo Baeyens** 15:19 I think…
**Tyler** 15:20 Yeah, go ahead, sorry.
**Pablo Baeyens** 15:22 Now we're working on… on some nodes on, those.
meetings, there's no recording, but there will be notes. It's gonna be to finish writing some of them before we can release it.
But I think that that second conversation, if I recall correctly, was more focused on integrating these exporters with the collector, so maybe a conversation that we can have on the collector's SIG. But if there's some overlap with the GoSig that I missed, then it's worth discussing here, I guess.
**Arthur Silva Sens** 15:54 Another question that I had is, There is a, like, a bridge from the… Prometheus SDK to the hotel SDK, So, somebody could just use the Prometes SDK to do all the… All the metrics, creation and… and incre… Increasing?
And then there's a performance cost to transform back to OTLP.
But would that be enough? Like… Like, don't use OTLP to increment your counters, but you… you'll need to do this transformation later.
**David Ashpole** 16:35 I mean, it… I wouldn't be too worried about the… Transformation cost during collection, because it's… Like, it's not on your hot path. It… like, it does matter, but… Not as much… like, for performance-sensitive applications that are incrementing counters a lot, or something, like, the cost of translating it from the Prometheus data model to the OTLP one at collect time is not nearly as, like.
I doubt that that's the crux of the issue.
I think that totally could and does work.
For people who want OTLP export with Prometheus Client Libraries.
I suspect a lot of people use the hotel libraries because they're interested in having the OpenTeometry conventions as well.
But…
**Tyler** 17:29 Yeah, maybe… I'm still not quite understanding, like, the user journeys here. Like, it sounds like Brian and you guys were talking about some sort of, like.
as you called it, a legalistic thing, I'm not exactly sure what that meant, but, like, Like, what… So, like, we're happy to continue supporting the OTEL users. I didn't realize that there's OTEL folks trying to position us as a replacement for Prometheus. Like, I'm not trying to do that. I didn't realize that was the case. But, like, I'm also, like, it sounds like maybe you guys have understanding of some sort of user story that, like, is kind of motivating the discussion. I'm kind of, like, I'm not a… A point of ignorance here, like, I'm just wondering if, like, you can fill me in on that one.
**Bryan Boreham** 18:15 So users, there's lots of different categories of users, like… Someone… I don't even know what's a good example, but maybe the Postgres exporter is a good example. Somebody wants to collect Postgres metrics, and… there's a… there's a Prometheus Postgres exporter.
And so the gap between that and a hotel solution is in the semantic conventions, is in… Well, possibly nothing else.
I'm not sure. But, you know, whatever that gap is.
Or… so there's… there's a journey where we kind of work to… make all that stuff work together. And then there's a journey where, effectively, the Postgres exporter gets rewritten using hotel libraries.
And I'm… I'm definitely… it's a personal… Prejudice of mine is to try and avoid doing the second one for, you know, 200 times over.
because it… it just seems like such a lot of work.
So that's… I don't know if I'm kind of painting the entire picture. That's.
**Tyler** 19:47 So, if I understand you correctly, you have, like, this is maybe what I'm understanding, like, the users are out there right now, there's a very rich ecosystem of Prometheus exporters, which, thank you as well, by the way, I used to be a very avid user, still am in certain areas, but, like.
the users there are saying, like, well, why can't this be replaced with some sort of OTEL component, is the idea?
**Bryan Boreham** 20:09 Well, no, how do I… how does this fit into my… I've decided to standardize on hotel, right? That's a definite… that's a phrase that we hear.
**Tyler** 20:16 Yeah, okay.
**Bryan Boreham** 20:17 And to some extent, we then have to interpret what they might have meant by that, because usually we're hearing it from someone You know, in, L… L9 in the.
**Tyler** 20:32 They may not even know exactly what that means. Yeah, I…
**Bryan Boreham** 20:34 That's okay.
**Tyler** 20:34 I see what you're saying, yeah.
**Bryan Boreham** 20:36 So, yeah, sorry, the, the, they're, Yeah, so if we interpret that to mean, that it should conform to the OTEL data model and semantic conventions.
you know, it should… so, yeah, so now that's… that's what I was trying to describe, that we then have these… these two choices of trying to start with postgres exporter that exists, and do stuff to that.
To make it fit that requirement. Or start from scratch, you know, start from the… Postgres API.
**Tyler** 21:21 Oh, okay.
**Bryan Boreham** 21:22 API.
**Tyler** 21:23 So, in this specific case for Postgres, like, I don't remember, but maybe it doesn't support OTEL semantic conventions and what it actually exports, and so what the idea is, is, like.
could you turn on a flag, or could you tune this some way to be hotel semantic conventions? And then your question is, like, well, do we do that, or we just say, like, go use hotel instrumentation if you want hotel semantic conventions? But you can't say that if the performance is…
**Bryan Boreham** 21:49 Yeah, and who's doing that work? I mean, you know, there's two gaps. There's the coding gap and the performance gap.
**Tyler** 21:57 Okay.
I see.
**Pellared** 22:00 could be a collector.
Doing the transformation, yeah, plenty of ways.
**Tyler** 22:07 Yeah, I mean, I think… I definitely think the… yeah, there's a great story around, like, the collector here, right? But, like, at the end of the day, like, the Postgres exporter isn't supporting even the collection of data that we need for semantic conventions, or… or it's collecting it in a way that cannot be transformed, then I think you're at a loss, is what Brian's user story is kind of the point.
Because, yeah, I mean, I think from David's point as well, like, if performance is super critical, and you already have Prometheus exporters in place, like, the collection pipeline can handle that, like, asynchronously, which makes a lot of sense to me. So, like, this HotPath stuff becomes, like.
a pretty easy story, saying, like, just keep that, and, like, use the collector. But, I think it's more about, like, semantic meaning and, like, data forms coming upstream, and, like, maybe that's more where the users are like, I need a solution there, if I'm hearing you right, right, Brian?
**Bryan Boreham** 23:02 Yeah. Like, what are… what is the story? We, you know, what is the, holistic.
story.
I mean, I guess we also feel it, or, you know, I can point you at ads from our competitors bashing the fact that if you use Grafana, you have to bolt the pieces together yourself. That's the kind of… What is the holistic solution?
and I don't even know what the competitors are proposing to monitor Postgres.
So, yeah.
**Tyler** 23:36 Sounds like noise to me. I really hope it wasn't coming from us, but yeah, that sounds like noise to me.
But, yeah, okay.
**David Ashpole** 23:45 I will also just… if I can jump in for 10 seconds, I… I think the performance issue is very much a problem for applications that are instrumented with hotel.
If we're mostly talking about, like, things that in hotel land would be collector receivers.
then, like, that has a very different API and doesn't have any of the performance like, there's… there's no aggregation in the collector either, so you can't, like… like, there are no histogram instruments to be optimized. You just… you know, produce histogram data, if that makes sense. But there's, like.
I don't think… I think maybe the trade-offs are different if we're talking about collector-receivers, or things of that nature.
Which is usually what I hear Prometheus exporters being compared to.
**Bryan Boreham** 24:37 God, maybe…
**Tyler** 24:39 Did you want to jump in there?
**Jack Berg** 24:40 I don't want to jump in there. I kind of want to just share my experience about, you know, performance and comparing Prometheus and OpenTelemetry from a Java perspective, because there's some parallels, but there's also some differences, but I want to let this conversation sort of run its course.
**Bryan Boreham** 25:00 We can go there. I mean, some of this is just my ignorance, that, that I, I, Just on the point that David was saying, like, in the collector-receiver… I mean, ultimately, you start… you start from the… in my example, you start from the Postgres API. You've got… you've got some data about… I don't know, page caches inside Postgres or something like that, and you're gonna… you're gonna make some metrics, maybe they're histograms or something like that. So you are gonna call an OTAL API to do that, right?
And so I could accept the argument that you don't do this enough to worry about the performance, so that may well be true, but I… I'm not getting why it's fundamentally not a concern.
**David Ashpole** 25:55 I guess, when we've had previous discussions, we've talked about Or, most of the Prometheus exporters I've seen that get rewritten into OTEL end up getting rewritten as collector receivers.
There may be cases where the exporter Is actually, like, receiving a stream of inputs and needs to aggregate those into instruments?
But a lot of the time, it's actually just calling some API And getting some data that's already Pre-aggregated, or like… gets somehow transformed into, like, directly into metrics. Doesn't get, like, Put into instrument structs and…
**Bryan Boreham** 26:40 And stuff like that. In that center, too.
**David Ashpole** 26:42 In that sense, like… you would just take that data and map it right into PData.
**Bryan Boreham** 26:47 Oh, okay.
**David Ashpole** 26:48 And so, maybe the… one of the AIs is, like, we should explore writing a… bridge from… the Prometheus registry to…
**Bryan Boreham** 26:59 the P data.
**David Ashpole** 27:00 P data, not the Prometheus registry to… maybe, Arthur, you've said this a billion times, so…
**Arthur Silva Sens** 27:05 I, yeah, I have something working already, I just…
**David Ashpole** 27:08 Great, wow.
**Arthur Silva Sens** 27:08 Heads.
**Bryan Boreham** 27:11 Yeah, sorry, that's a useful clarification for me. Okay, we can move on.
**Jack Berg** 27:20 Alright, so I'm gonna jump in then. So, you know, I'm reading this blog post from… from Julius. I haven't seen this before, but there's… there's, like, the reason 5. It says, OTEL SDKs are complex and can be very slow. And it says SDK is plural, and then there's an immediate caveat that says we're talking about the Go SDK.
I take some issue with that framing, because it, like, it groups together hotel SDKs, like, you know, they're one uniform thing, and each one is a very different story, different context, and so… You know, I do think that nuance matters when we're having these conversations. Like, you know, which SDK are we talking about? And, like, what are their very specific problems? And so, I wrote this blog post that I'm going to share in the chat.
two years ago, and, you know, I set out to try to do a comparison between the metric systems and the Java ecosystem. The major ones are Micrometer, Prometheus, and OpenTelemetry. And, you know, I did my best to be unbiased, and and, you know, my conclusion at the end was, like, hey, these are all, like, really serious metric systems. They all meet the criteria of, like, on the hot path.
there's zero allocations, and, you know, for the cases that I tested, the performance is, like, you know, relatively consistent. And And then, you know, I joined… I joined Grafana recently, in 2025, and there was, you know, I found out that there's just, like, a lot of people still thinking about this, and, like, you know, and there's, there's this… there's this thought that, like, even within Java, where I had done a lot of research, that the Prometheus Client Java was, like, much better. And so I went digging for, like, what is the actual benchmark they're referencing? And I found it. In the Prometheus Client Java library, there's a benchmark, and when you run this benchmark, like, Prometheus just, like.
kicks OpenTelemetry's ass, it's not even close.
And so, you know, that was a blind spot when I was doing my performance benchmarks. And the specific blind spot was that, like, in this Prometheus benchmark, they were really concerned about a high concurrency situation and a bound instrument.
And so, like, you know, being that from an hotel world, we don't support bound instruments, and one, and two, bound instruments, I would argue, are only applicable in something like 5-10% of instrumentation cases. More often than not, you have to complete… Compute your attribute set or your labels, within the context of when you're recording a measurement.
But so that was a blind spot. But, so, I still took it to heart, and I started digging into, you know, what are the actual differences? Like, what is this Prometheus benchmark measuring? And, like, this is a real problem. Like, OTEL is seriously slower when there's high contention. And, you know, also I want to solve the bound instrument piece, but I have to kind of put that off to the side, because that's a spec-level issue. So, how can we solve this contention issue?
And, like, you know, basically what I found, staring at the Prometheus code for a long time, and making some improvements to the Prometheus code, and making even more improvements to the Java code, was that, like, the systems really converge.
They're not, like, you know, you have to get nuanced in these conversations because the systems are so convergent in terms of the code paths and, like, what they're doing to optimize that, like, there's very little opportunity for differences. And so you kind of have to zoom in on the very specific thing that you want to improve.
To call that out. And so… what's the takeaway? So, like, one of the things that I found that I think hasn't been mentioned here is Prometheus Client Java benefited from only having to support cumulative temporality.
Like, so, when you have to support delta temporality, you have to do this sort of, like, extra state management to make sure there's no missed like, lost rights. It's like you have to do additional tracking to ensure you have no lost rights, and in Prometheus, lost rights aren't a problem, because they'll always be picked up in the next collection.
Right? Because it's cumulative. And so, like, one material thing I did to improve the performance of OpenTelemetry Java was I decoupled the, like, the cumulative from the delta path.
And now the cumulative path is, like, identical to what Prometheus is doing under the covers, and it benefited a lot in terms of concurrency performance.
And so, like, you know, there may be some structural things in terms of the Go Metrics API that is, like, forcing certain things, but… and maybe there's, like, maybe we should put together, like, a plan to.
evolve or, like, add, like, a new API that sort of fixes any structural issues that exist? I don't know the details, I'm not a Go developer, but if any such things exist, like, a long-term plan to resolve them could be a good idea. And, like.
you know, I think… if… like, we go, Java, OpenTelemetry, Go Java, and all these implementations should try to be as performant as possible. If Prometheus has techniques.
that, like, makes it more performant and makes it a better candidate, then we should learn from those techniques and incorporate them into, you know, our implementations. And, at least in the case of Java, I have benefited from reading the Prometheus, like, code and incorporating those ideas. And, you know, if you play that out over a long time, the implementations look remarkably similar.
there's always going to be, like, this difference of, like, Prometheus libraries don't have this notion of scope, so they don't have to deal with, like, this, like, you know, you start with a meter provider, then you walk down to a meter, and then you walk down to instruments. That's, That, I think, is a… like, an ergonomics thing we can't easily, like, resolve, because that's, you know, what… how OpenTelemetry is designed at the spec level, but implementation-wise, we can and should set a target to be as performant as Prometheus is.
**David Ashpole** 33:31 I agree. I want to call out, like, one difference, maybe, between the Go and the Java, and Tyler, keep me honest here.
OTEL implementations is, I think, for us, in the dynamic attributes case, where you haven't pre-computed them.
Even if you do pooling and some other, Go best practices, you still have an allocation on the hot path.
So I think that's one of the, like, maybe, like… little warts that we still have from our API design that we're thinking of.
I'm trying to figure out how to remove.
**Tyler** 34:03 Yeah, and I want to say, like, that's not insurmountable, as David's pointing out. Like, that's definitely something that we have solutions, right now, bad solutions, we're trying to find the best of the bad solutions, maybe, is the way to say it, but, like, yeah, like, there's… structurally, Jack, from your… I just want to say, like.
David has done, like, an immense amount of really great work here. We originally designed the Metrics SDK with, like, a, like, this works, like, sort of thing. Like, we'll come back and touch the performance, later.
And David's come back and he's touched the performance. All of the things that you've said are very accurate. He's worked in both Prometheus World and Otel World, and he's taken a lot of you know, phenomenal, you know, changes to try to, like, make this improve. He's still in that path, though. I want to say, like, there's still some, like, there's still work there. There's no… outside of that structural change in the API that David's talking about, like, there's really nothing limiting us from optimizations in this… in this particular space, and, like.
The only thing I would say, like, is it's still a work in progress, And that's… that's the only thing that, like, you know, if you want to evaluate the SDK performance.
give us a little bit. You're welcome to do whatever you want, but, like, if you want to actually, like, apples to apples this thing, like, I think that… I think we're still a little bit of ways, from that. But I… I… I did want to, like, kind of progress the conversation from here, but I didn't know if there's, like, more, David, you wanted to add to that.
**Jack Berg** 35:25 Can I just jump in with, like, one, I guess, follow-up to what you said? So, in Julius's article, there's, like, one of the headers is, hotel SDKs are complex. And, like, the implication there is that some complexity in the data model is a, you know, a fundamental bottleneck in terms of what you can achieve in terms of performance.
And I don't find that to be the case at all.
So I think that, like, there's, at least in Java, and I imagine in Go, based on what you said, that there is nothing stopping the OTEL APIs from… or the OTEL metrics implementations from being every bit as performant as Prometheus counterparts, you know, given that we still have some problems to solve, like bound instruments, and maybe some other things that are implementation-specific, but, like, it's not like the APIs are, you know, structured so differently that, like, OpenTelemetry will never be able to achieve that performance.
**David Ashpole** 36:19 I think some features have a performance cost.
Just the fact that exemplars are, like.
kind of always plugged in, adds a small amount of overhead for us. Attribute filters.
being a thing that we have to take into consideration, and sometimes being, like, a default case is something that adds small amounts… like, there are features that have performance costs, and if you use them in the API, but you're right that I think we can get to If we're doing the same thing as Prometheus, you can get close to the same performance.
**Jack Berg** 36:52 Exactly. If you have… if you're doing, like, a like-for-like comparison, like, you know, the same behavior on exemplars, maybe turning off attribute processing, the code paths should be able to benefit from turning those features off and achieve, like, blazing fast performance.
**Tyler** 37:08 Yeah, and so, just to… yeah, again, like, I think an apples-to-apples comparison, I think, is helpful. We're not there yet, we're working towards that. Like, I honestly… there are unknown unknowns, I'm sure, and so, like, if we do find things, like, it'd be great to identify them. Like, David's already kind of pointing out, like, there are feature sets that you want to keep in mind. But I, like, I… So, so, I think to that effect, like, if you want to evaluate the performance here, give us a little bit, we're working on it.
that doesn't really, there seems to be an underlying issue, though, that, like, I wanted to, like… why we're having this meeting, it seems like. Like, it seems like there's, like, a concern about the long-term… story about the compatibility, about the… how these things are gonna live alongside each other. Like, I think it's commendable, and I think it's great, like, you're having this competition in the sense that, like, we're, you know, this performance improvement is probably getting ported over here, and then this one's getting ported over here. Like, there's great, like, I think that's making the world better.
But, I also really want to make sure that these two communities are not, like, adversarial. And I think that's, I think, more important here than… Then I think the performance of the SDK. Like, I want to make sure that, like, that we in the hotel community are not saying, like.
don't use Prometheus, it's blank, and then, you know, I can't speak for the Prometheus community, but I didn't, like, talking with Brian and Arthur and these people, like, I don't… I don't see these adversarial personalities, so I just want to make sure that, like.
whatever that story is, like, we as, like, the TC, with the TC members here, at the GC level, are aligned in the Prometheus world. Like, I've talked to other people in the Prometheus world as well, and, like.
by and large, I don't find an adversarial, like, ethos. I do… I actually find a collaborative ethos. I know there are personalities that don't see it that way, but, like.
whatever that is, I think that maybe I'm more concerned about that than I am about the performance here, and I just want to maybe, like, take a step back, like, if there's problems, if we could surface those and address those.
**Arthur Silva Sens** 39:10 Speaking for myself, yeah, of course, not an adversary at all.
There are a few people who might be skeptical.
But I don't see nobody, like, saying… Well, tau sucks, and you shouldn't use it.
Definitely nobody like that.
**Tyler** 39:38 Well, cool, alright, maybe, maybe it's just, yeah, I…
**Bryan Boreham** 39:41 On the, on the, on the keynote stage of the observability Day a couple of weeks ago, somebody said that I think they put up the XKCD cartoon about, now we have 15 standards, and they said, well, this didn't happen with the hotel, it squashed all the other standards.
And I felt that was not a… That was not a community-minded, collaborative thing to say.
**Tyler** 40:08 Yeah, I think that's fair. I think you're right. I don't think Prometheus has itself been squashed.
**Arthur Silva Sens** 40:15 Yeah.
**Tyler** 40:15 I don't know, I apologize, I don't know who said that, but I can remember who's on stage, so maybe the people who are on the TC can maybe take that back as some feedback? Community guidelines here, around, like, trying to be A little bit more… Receptive to that?
**Arthur Silva Sens** 40:34 I can share the name offline if you want, like…
**Bryan Boreham** 40:37 I, yeah, I chew…
**Tyler** 40:38 Personally, I don't want it, but maybe Pablo.
**Arthur Silva Sens** 40:41 I can't.
**Tyler** 40:41 David would be interested, although I'm guessing they already know who we're talking about, yeah.
**Bryan Boreham** 40:45 Oh, it's funny.
**Pablo Baeyens** 40:45 Simply conversation offline, yep.
**Jack Berg** 40:47 Offline place, yeah, definitely interested.
**Bryan Boreham** 40:50 The, oh, sorry, I lost my thread. I think, I feel that the Prometheus is treated as a vendor.
like, Datadog is a vendor, Spunk is a vendor, you know, in this, In this world, and that… that feels unfair.
Because nobody's going to be a billionaire.
off Prometheus.
**Jack Berg** 41:20 Prometheus?
**Tyler** 41:21 I wish…
**Jack Berg** 41:22 has a special spot in OpenTelemetry.
There's Prometheus and PPROF, which are, you know, two standards that are, like, sort of above the rest, in terms of, like, there's parts of the spec that say, you know, as a part of designing the metrics data model API, like, we commit to full compatibility with Prometheus.
As a part of the profiling specification, we commit to having full compatibility with PProve.
So, like, there's nothing else that has, like, that level of guarantee.
Now, nothing in logs, nothing in tracing. Zipkin and Jaeger, we try to play nice with, but, like, you know, there's… there's latent issues in the exporters that are never fully resolved with how, like, the data models are transformed. So… I mean, as a TC member and a maintainer, I definitely, like, hold Prometheus well above, you know, the status of any vendor.
**Pablo Baeyens** 42:25 Yeah, I'd say to put another example, if you compare the support for StatsD compatibility with the support for Prometheus compatibility within OpenTeometry, Prometheus is clearly, much more well integrated.
**Tyler** 42:41 To be… You know, to validate you, Brian, though, like, I do… would love… personally, I don't know if the TC's interested, but, like, I'd love to get, like.
like, why you think this, like, not like… obviously, just perception is… is reality, right? So, like, if this is the case, that is… that is what you're feeling, like, I'm not saying that, like, that's invalid. I'd love to know, like, what are some things that we could do better here? Like, I do think that, like, Pablo and Jack are bringing up, like, will you try? I know David is… I mean, I see him every week, and he's working really hard about this compatibility stuff, as well as Arthur. Like, they're very, very active in the spec world on this, so, like, I know that they're trying. If that's just not visible, I think that that's a problem. If there are things that, like, aren't being done, I'd love to know things that we could do better here.
like, this sounds like you have really great feedback, is what I'm trying to get at, and I'd love if we can, like, maybe capture that feedback and actually take it as action items, to try to make sure that that isn't… the case. Maybe it's just standing up on stage at Observability Day, holding hands, and saying, like.
We don't hate each other, but yeah, I don't know.
**Jack Berg** 43:46 One concrete thing that, you know, we're working on currently is, you know, there's a new section on OpenTelemetry.io in the docs called Compatibility.
And I'm working on, like, the first page, which is, you know, a document comparing, you know, the client libraries, OpenTelemetry and Prometheus client libraries, in terms of, like, what are the conceptual differences. But I think there's going to be other Prometheus compatibility content that just, like, you know, really digs into everything you need to know as someone who's part of the Prometheus ecosystem, and, like, how Prometheus and OpenTelemetry interact.
operate.
Like, at the collector level, at the client level, you know, potentially instrumentation, things like that. There's a… isn't there… I think there's an LFX mentorship that's committed to doing this, so…
**Arthur Silva Sens** 44:36 Yeah, I'm mentoring someone, but, she is very, very, very, very junior.
I don't think we'll be able to get something very advanced out there.
Hopefully she stays on the community and eventually starts contributing there, but in reality, right now, it's a little bit too far.
**Jack Berg** 45:00 well, then, you know, yourself, myself, David can, you know, pick up the torch and carry that forward. But, you know, I guess the point is, is that if, you know, maybe we can help some of these… these issues by just being more public-facing about, like, our commitment to interoperability with Prometheus.
**Tyler** 45:25 Yeah, and say it's not a vendor. Yeah.
Cool. Brian, I don't know if maybe we can, like.
I also don't think that your voice alone is, like, the sole voice in this community, so, like, if you have other people that are, like, feeling these things, like, if you could reach out to them, Jack and maybe David, I don't know if there's a touchpoint that you guys can all sync up with, and Pablo as well, with the cohort in the Prometheus world, I… I want to keep progressing in the Go topics on this meeting, so I wanted to move forward, because I know Robert has some.
**Pablo Baeyens** 46:00 Yeah, ideally, I think some of these topics would be more on, like.
either the Prometheus interoperability sig, or just, like, TC and GC.
**Bryan Boreham** 46:12 Yeah, and I… maybe in closing, I feel huge strides have been made. You know, historically, there would be events around KubeCon, and the Prometheus people and the hotel people would be in separate buildings.
So, so I was… I was… I've pushed hard myself, and we got it done. We got ev- we got not everybody, but we got a lot of people, like, 50 people in the same room.
So… so huge step forward. So, thanks to everyone who helped.
With that, and yeah, let's… let's keep working.
**Tyler** 46:49 Awesome. That's good. Yeah. Let's, let's, let's keep it going on that and that good end note. So, yeah, appreciate it.
Okay, moving on to the agenda, Robert, you wanted to ask about, breaking changes on a particular PR. I can start, sharing my screen here again.
Yeah, go ahead, Robert. I think you can see my screen, yep.
**Pellared** 47:11 Okay, so, I created right now CTRs, like, recently we created this, string method for the attributes value type, so, which conforms to the non-OTLP string representation.
And I discovered that we have some encoder, attribute encoder, which uses the emit, which was not following basic… which was not following any, you know, kind of specification.
And, I tried to point out in the description what are the differences, you know, how… what will be the result. That, for instance, the array of, of, the slice of booleans, does it have commas, I think it didn't have also, Yeah, there are a few, like, you know, encoding differences between emit and strange.
And the question is if we want to make this change, if we want our encoder to be more, kind of, spec compliant, or do we Preferred to keep it as it was.
To not break some existing users, which… May have been… Depending on this, on this, behavior.
I try to put some examples how my people use it.
I think the biggest, I think it can be from testing, you know, some logging stuff.
But, yeah, I saw that David, yeah, so maybe someone was using golden files or things like that for testing, you know, capturing, like, output of some telemetry, you know, encoded, and then comparing. I see David is smiling, yeah. So, this is my biggest worry.
And the question, if you are scared about that, then I prefer keeping a meet.
Asia.
That's…
**David Ashpole** 49:14 I was smiling at Brian's comment in the chat.
**Pellared** 49:18 Okay, I can't see it. I'm not able to speak at the same time.
**David Ashpole** 49:21 Hiram is going to… is going to come find us all.
**Pellared** 49:30 Oops.
**Tyler** 49:31 So, yeah, I think David's concern here about, like, stability here is probably important. This has been the way it is.
fortunately or unfortunately, for quite a long time. And so, like, I think it, like, maybe just leaving it, I think, makes a lot of sense. I do think, though, that, like.
we always made the encoder extendable with whatever encoding you wanted, so I actually think that maybe providing, like.
something other than this, like, default encoder. I don't know what a good name is.
**Pellared** 50:05 It's easier.
**Tyler** 50:06 But, yeah.
**Pellared** 50:08 I agree, I agree, a difficulty, or an option, or anything. Yep.
**Tyler** 50:12 Yeah, because, I mean, a user has always been able to provide, like, its own encoder, and then, like.
There's nothing stopping us from just saying, like, well, here's an additional encoder that we support as well, and they can switch it if they want.
**Pellared** 50:25 Okay.
**Tyler** 50:27 Does that make sense?
**Pellared** 50:29 Yes, it makes sense.
**Tyler** 50:31 Gotcha.
David, how about you?
**David Ashpole** 50:37 Yeah, I just… I didn't have a good sense of, like.
what this is used for, which is why I left the comment. Like, it seems like something… Someone could totally be… relying on.
Unlike some… I think there's another change here, which was just about, like, how we log something.
**Pellared** 50:58 If I remember correctly.
**David Ashpole** 50:59 partial log, and for me, like, that change feels like, oh, you know, like, we changed a log message or something, you know, like… Seems like…
**Pellared** 51:08 I'm also more concerned about the encoding. Yeah.
**David Ashpole** 51:11 seem… But I… that's where I fell, was I was okay with the log change, and not… not as comfortable with the encoder, because, I don't know, it sounds production-y to have an encoder, and people are probably doing dumb things with it.
**Tyler** 51:30 Yeah, I go back to the fact that I really… This is, like, my least heard package we ever exported.
But anyways… Okay, cool. Robert, so we have a path forward on this one?
**Pellared** 51:40 Yes, of course.
**Tyler** 51:43 Okay, cool.
Alright, going back to the agenda, I had a roadmap check-in, so these are things that we've, like, identified at the beginning of the year. We've got, 7 minutes to go through this, so… definitely not enough time.
Maybe we can just call out anything that you are working on that, like, is not accurate in its, state, or needs to be updated, or you have an update on it. I do know… that optimized metric SDK is what we just talked a lot about, so, I'm guessing, like, we don't need to talk too much about this. We just got kind of an update that David is still actively working on this. The, hotel HTTP stuff is coming up, maybe we can kind of maybe just touch base on that, because I know Damien is about to go out on, paternity leave for… French time, so, 3 months, I think it was, something? I can't remember. Quite a long time, and so, or maybe even more. So yeah, we might want to see if we can find another owner for this, if we're going to try to get this done this year, I think is an important thing.
To consider.
I think this enable method… Robert, is this done?
**David Ashpole** 53:03 No, it's not. I, I just opened two more PRs in Contrib to fix the last two little… instances of it. And there was one note that I didn't look into about, like, Templating… updating SEMCOM based on a template.
That I didn't have context on, but is the last remaining item after.
The two, one for hotel gRPC and one for runtime metrics.
**Tyler** 53:31 Oh, yeah, I see it now. Okay. Alright, yeah, so we're actually pretty close, but we still have a little bit more on that one.
**David Ashpole** 53:37 I looked at the SDK self-observability ones as well. There's 4 open issues, all 4 have PRs, but some of them haven't been touched since October, November. I did do reviews of 3 of them.
**Tyler** 53:51 Yeah, doing a great job, man.
Yeah, cool, okay, then, yeah, then I think… we… maybe… maybe we wanna, on your opinion on those remaining ones, is it worth reopening PRs for those, or, do you think that we should give it a little bit of time to see if folks are gonna respond?
**David Ashpole** 54:10 I think Robert just pinged one of them.
asking, like, hey, are you still… no, it was, like, at the beginning of March or something?
Maybe. So, I think maybe we can have someone pick… pick up.
I think we should consider unassigning people and closing people.
**Tyler** 54:30 Yeah, okay, that sounds good. Then, I think, maintainers on the call, like, if you are… have some free time and you want to start working on these things, Go ahead and start unassigning and picking things up, or reassigning.
Two of the other big ones, I'd love to get, like, just a 4-minute status update, Robert, on is, like, the, complex attributes edition, how that's going. I know we're working a lot on the bytes, and maybe just scope it to that, because I'm guessing that's a precursor to the log stuff.
**Pellared** 55:04 Like, all of the complex attributes, right?
**Tyler** 55:07 Yeah, correct, yeah.
**Pellared** 55:09 Yep, yep, I'm focusing on that. Actually, like, I think there are 4 open PRs, like, right now for the context, at least. I found also another few, you know, leftovers after the previous PR. I approved yours, if I remember correctly, regarding the pin.
And I started creating a PR for the slices.
**Tyler** 55:32 Okay, this is just generic slices, that you can do, like, the heterogeneous, yeah.
**Pellared** 55:38 Yes. Okay. Exactly.
**Tyler** 55:40 And then, so we have slices and then maps are the last two, right?
**Pellared** 55:45 Yes, absolutely, last one, probably not the release that is going to happen now. I propose to, you know, postpone to the next release, because I think even the slides will have a little more PRs, and I do not want, you know, postpone the release, or, I don't know, revert the… reverse the commits in OPRs.
Unless you want to…
**Tyler** 56:07 The bytes haven't been released yet, have they?
**Pellared** 56:11 They have not.
**Tyler** 56:12 Okay. So, this next release is going to include the byte support, and then the release after that is slices?
**Pellared** 56:18 I will try to have slices as well for this one.
**Tyler** 56:22 Okay.
Right, cool, yeah. And then, so then those are kind of blocking the restructure of the logs API, because, like, literally that was the last item, right? Or are there… okay, yeah.
Awesome.
**Pellared** 56:36 They may have been more, which may… because there were also some changes in the specification, but I don't think there's any… this is the most… these are the biggest changes.
**Tyler** 56:47 Yeah, right.
Cool.
Awesome. Well, I think maybe with that, we can pause here. Any other topics people wanted to… oh, I got a topic. The KubeCon… North America CFP opened, just a heads up on that one.
if you have topics, it's the end of May that it closes, so you got plenty of time at this point, but yeah, just kind of maybe start thinking about talks, In this… in the space. So, yeah, just kind of wanted to mention that.
I don't know if it's other… other topics, or cool ideas, or fun things people are working on?
**David Ashpole** 57:31 I, I will… If there's nobody else, I will say, I am still working on the… Lockless exponential histogram. I tried to bite off a chunk.
But it turned into a PR that's… Probably still too big and complex to review.
For anyone who's interested, one of the issues is that… It's really hard to… We did this thing where we have, like, a hot histogram and a cold one, right? And we can read the cold one and then merge it back into the hot one.
But exponential histograms are really annoying because measurements can underflow if you only have to… Two things in your exponential histogram, so… It makes the histogram thing that we did not work very well.
So I… I'm working on a new approach, but… it's big and ugly, and I don't like it yet. So, that's… that's where that's at.
**Jack Berg** 58:29 I feel like I need to follow that along. That is one area I was not able to get lock-free.
**David Ashpole** 58:35 No, it's… Is it lock-free? It's lock-free unless you have to downscale.
So it's always going to have a lock when you downscale, but it'll be lock-free unless.
**Jack Berg** 58:47 We'll see by time.
**David Ashpole** 58:48 Yeah.
**Jack Berg** 58:48 Yep.
**David Ashpole** 58:50 But… Yeah, it's… it's still… I still can't… I need to figure out how to get it into bite-sized pieces so people can actually review.
**Tyler** 59:00 When we say not bite-sized, what are we talking about, like, 1,000 or 10,000?
**David Ashpole** 59:04 Right now, the… I have a draft PR open that's 600-ish lines, but… it's… it's also kind of complex. I don't know, I wouldn't probably be able to review it myself.
Okay.
**Tyler** 59:18 Yeah, I'm happy to take a look at a little bit more complexity for these kinds of things, but if you think you can split it into smaller, simpler ones, I'm also really happy to.
**David Ashpole** 59:27 I hope that happens. I think I can, so I will… I will try, yep.
**Tyler** 59:30 Perfect.
Okay, we are right at the time. I want to be real respectful of people's time. It's good seeing you all, thank you all for joining. Most of you all will see you in a week's time, or asynchronously. Bye.
**Pellared** 59:41 Thanks a lot. Bye.
