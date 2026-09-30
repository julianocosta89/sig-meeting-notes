SIG: .NET SDK SIG
Date: 2026-09-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:18 Hey, Matt.
**Matthew Hensley** 03:21 Hello.
didn't have a slack going. So, Mr.
Notification.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:33 Oh, for the meeting.
**Matthew Hensley** 03:35 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:36 For a minute I was like, oh, I've closed Slack, what have I missed?
So I have Chrome do the native notifications for me.
**Matthew Hensley** 03:46 I've been closing as much as possible to reclaim some RAM.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:50 Fair enough.
So it might be a short meeting today.
**Navya Sharma (HealthStream)** 04:05 Hello.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:07 I know, Janet.
Give me 2 seconds.
And…
**Alan West** 04:30 Hey, how are you? Sorry I'm late again.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:36 No problem. I think everyone pretty much all just turned up anyway.
**Alan West** 04:42 Bill.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:49 Let me share my screen.
There's… excuse me, so there's currently nothing dedicated on the agenda other than issue and PR triage. Is there anything anyone wants to talk about specifically that's not in the agenda?
**Alan West** 05:27 Got a newcomer.
Oh, sorry, I interrupted somebody.
**Navya Sharma (HealthStream)** 05:35 Very good. I was gonna say I wanted to review my PR on Metrics SDK, but I think that's not been reviewed yet, so I might leave that alone for now.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:49 Which one exactly was it? Was it the one that we're waiting for CJO to look at?
**Navya Sharma (HealthStream)** 05:53 Yeah, yeah, exactly.
7557.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:58 Yeah, I did re-request his review on it just now.
Because I saw you repaste it, but yeah.
That one, there's not much we can do other than poke CJ with a virtual stick.
**Navya Sharma (HealthStream)** 06:13 Gotcha. Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:22 PR dashboard. So, we don't have to look at this now, but… whoops. If, people can have a look at it over the next couple of days. I've added… I say I did. I asked… I asked an AI to do it. It's AI all the way down. I've added some… Copilot review instructions.
to both the main repo and the contrib repo.
To try and make.
Copilot a bit smarter if we ask it to do reviews on things, and also… try and give a bit more instruction to people who are doing AI, agent PRs to the repos.
Steve's had a look at one of them. They're basically both the same, but I used… the… skills they have in the .NET Runtime repo.
that I happened to see when I did a PR there the other week, as the.
the source of inspiration to write them, which I asked Claude to do, so… But yeah, if everyone's happy with the, the approach and the instructions those have, then there, we can merge those.
Okay.
That's Navy's PR, that's waiting on CJO.
Piotr.
**Alan West** 07:45 Oh, that's what it's about, changing aggregation type for all instruments. Yeah, that's a… That's a spec thing, right?
**Navya Sharma (HealthStream)** 07:55 My one? Yeah.
**Alan West** 07:58 It's something we don't currently support from the spec, but it is something that… Yeah. It's backed, right?
**Navya Sharma (HealthStream)** 08:07 Yeah, it's a huge change, so I don't blame anyone who hasn't been able to review it, so…
**Alan West** 08:11 Yeah, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:16 Yeah, yeah, I think on this one, if we get some steer from CJO, as, like, Raj was saying last week or the week before, like, CJO wrote a lot of this code originally.
And then from there, if needed, it can pivot off into the spec.
To actually get some… Agreement on what it should do.
**Alan West** 08:44 Oh, is there a spec question on that one? The spec allows for changing the aggregation type, I think at least between.
Some things.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:58 I figured.
**Navya Sharma (HealthStream)** 08:58 I'm not really asking that question.
Yeah, there's not really a spec question, it's just that I have some questions on what changes I should make versus… Maybe I should, probably… I just want everyone to, like, kind of discuss the changes I made before I make those changes permanent.
So public API changes. Yeah.
**Alan West** 09:19 you.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:25 There's a couple of… non-urgent PRs for me to do some performance stuff.
There's also some questions in this PR. This is changes to add schema URLs to logs.
It'd be good if people could have a… take a look at the new API suggestions this makes.
And see if there's any suggestion… suggestions to change It will improve it.
But those have to be done now. It's just that that's the main bit that I'm waiting for feedback on that one, because we might need to do some changes.
I'll chase Piotr about that PR because it's been sat around for a while.
Oh no, sorry, no, my bad, that's I'm thinking of a different PR.
This… Oh, no, yeah, this one, there was a performance change someone made last week.
And then this sort of… I think this is something Codex found.
off the back of it that wasn't actually introduced by the PR, but the effect is that it undoes the performance improvement.
But, the author's waiting for feedback from the author of the original.
FPO on that one.
That's another one.
Wing on CJ4.
**Navya Sharma (HealthStream)** 11:01 This one is a spec question.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:05 Okay.
Maybe I'd mixed up the two.
Do things to Pokemon there.
There's Steve's PR to change the self-diagnostics. I know Raj.
is partway through looking at that, and wants to double-check some internal Microsoft stuff, but if anyone else wants to have a… take a look at it, and if they have any concerns.
The idea being is basically it's a rewrite of the internal self-diagnostics based on some stuff from the Elastic.
Destroy.
And the eventual idea is that it will just have a compatibility shim in it, so that the old way of turning it on works with the new way. The new way looks a lot better, but it's… it's a lot of code.
And… what else we got?
Don't think there's anything in… Or an open that isn't, Just needs reviews.
And I think a lot of these have got conflicts as well.
**Alan West** 12:34 Hmm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:35 There was an issue there, muscle aches.
Steve's working on that. There's an issue Steve created.
About directive configuration.
which is soliciting feedback on. I've given my feedback on that, but if anyone else wants to chime in.
on that app.
Good is quite long, so I don't think… go through it now.
I don't need that to be wrong.
And then literally one minute ago, someone's… open two issues asking for various parts of the SPAN API to be made public.
I've put a comment on one of them, asking to provide some examples of what they're actually doing.
to try and Put some justification on why we should change things.
But, I feel they're probably not things you want to actually do.
**Alan West** 13:43 Yeah, that's with respect to the Shim API.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:47 Cemetery span, and… yeah, they're both cemetery span. Like, one of them I just immediately put a… it's… it would be a breaking change to do.
I don't think there's any real reason to discuss it until we reach such time that we're considering doing a major version.
So it could just sit in the backlog until then.
Unless there was like an obvious reason to just not do it at all.
**Alan West** 14:13 I mean, honestly, I… I'd be interested in having the conversation of just retiring this thing. I mean, obviously, it seems like we have users, but I wonder how large that user base Is for this.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:27 It might overlap with, yeah, the question I put on this one, this person is basically, can you make these things public so I can unit test them?
Oh, thank you.
**Alan West** 14:37 have.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:37 replied.
They were using Jaeger, which itself is deprecated.
**Alan West** 14:43 Yeah, right, right, right. Just kind of like, just use diagnostic source.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:48 But, I'll read that properly later, but yeah, I just suggested they give some motivation.
information.
What's that?
That's… Yeah, that's everything in the main SDK repo. Contrib… There's a new W3C state.
Ask that one of the country is added to the extensions.
If anyone has… wants to take a look at that and see what they think.
There's PR… This is one of these PRs to do with, like, the suppressing the instrumentation.
Stuff that remember we talked about a while ago.
On face value, it looks okay to me.
But I don't use gRPC often, so… if someone who uses gRPC in anger and stuff wants to take a look at it, see if it makes it… actually makes sense, that'd be good, because it might… I don't know if it would break something.
**Matthew Hensley** 15:59 Yeah, I was already looking at that, trying to figure out what the unintended consequences might be of.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:07 Okay, cool.
And… then… Oh yeah, as an update, we just started… had the discussion the other week about XUnit V3.
Those changes have been merged now.
And… Now that's been done, I'm trying to migrate this onto the new testing platform instead of the old VSTest one.
But.
There's some bits and pieces that make it non non mega trivial because how MTP works under the hood is quite different to the S test.
But if we can get it done, we might be able to shrink the CI legs, so that we don't have to test every TFM separately. Because MTP, by default, tests TFMs in parallel.
So we might be able to make this CI a bit less resource-intensive.
Once that's happened. But, there's a few bits and pieces that make it a bit… awkward to migrate, rather than just turning on a few toggles. And also.
coupled with the XUnit V3 upgrade, it made… Lots of fun, flaky test flakes appear because the threading model that.
Both of them uses different, so there's lots of async fun.
Bleeding state that broke a load of tests, but they should be all fixed now.
Right.
**Alan West** 17:44 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:45 And then… Might be someone you know, Alec?
**Alan West** 17:52 Yeah, yeah, yeah, he's, he's at New Relic.
He's based out of India.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:58 Right, okay.
Because, they've opened a PR to like make some changes to do logging and meter flushing.
But the Lambda instrumentation only just traces.
So, I'm not 100% convinced.
We should add these changes, but… so I'd be interested to… See what other people's opinions on this are.
I'm also not 100% convinced he's actually Writing the keystrokes himself, and it's an agent replying on his behalf.
**Alan West** 18:36 Gotcha. I can reach out to this guy. This is… not work that I've… Looked at her.
That he's spoken with me about, so… Yeah, I would be… Curious what he's trying to achieve here.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:55 Because I… reading between the lines, I think… They've been trying to get all the signals working in a Lambda.
And sort of, like, hitting some difficulties Lambda itself creates.
But then… Trying to push all of those fixes down into the instrumentation.
Because I remember last… I've got a Lambda for, like, a hobby project that I tried to put metrics into last year, and it… really made it slower. It, like, it had a massive overhead on it that meant I ended up removing it completely.
Because it just tanked the performance, so… It makes me wary of putting metric special casing into this.
Because it might affect all the users, even if they don't use metrics.
**Alan West** 19:44 Yeah, totally. And it's for the reasons that, like, you've already encountered that I believe… the Lambda instrumentation, I think, for just about all the languages have not really… Umm.
Strive to support metrics.
And it's also just strange, right? Like, to… like, lambdas are these ephemeral, like, short-running things.
If you're recording metrics, you… would not get much benefit from any aggregation, right? Because The runtime might be very short-lived.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:26 you Yeah, I think I think when I was playing with it, I was basically trying to do custom metrics.
Rather than, you know, like, HTTP duration and stuff like that. It's just gonna be, like, basic counters.
**Alan West** 20:41 Yeah.
Anyways, yeah, I can follow up with this guy and get a sense for… What's on his mind?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:57 Yeah, sure, because, yeah, this was one of those ones where it was all… the issue… you get the issue, and then you get the PR straight away.
Hmm. Sort of one, so there wasn't really the time to, like, have the, do we want to do anything about this?
**Alan West** 21:14 the.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:15 That just happened straight away after.
**Alan West** 21:17 Hmm.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:20 But yeah, I think if we did want to add this, we… Probably want to see some… use of it in a real Lambda.
Before merging.
Because I think I'd certainly try a CI build of it in my own Lambda if we did want to take this change.
Because I'm not going to dig it out now, but I remember in the… in the… I found it, like, last week, and it was, like, you know, it, like, doubled the execution time on my Lambda.
From doing the flushing.
**Alan West** 21:57 Yeah, got it. I can believe it for sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:02 So that's all the PRs, and then… it's the… There's the one we just talked about, and then… Selling for the op amp.
Owners to look at.
I don't think anything, there's been anything else popped up in the last… 7 days of interest in contract. We did deprecate the elastic Instrumentation since last week.
After we discussed that. So that one's gone now.
**Alan West** 22:44 Oh, cool.
Good deal. Yeah, so there was no pushback on that, huh?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:50 Not that we saw.
**Alan West** 22:55 Cool.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:57 Save.
That's Everything that's currently open.
Anything else anyone wants to chat about?
**Matthew Hensley** 23:12 I dropped a link to those, SDK benchmarks.
Anyone's curious?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:20 Oh, yes.
Yeah, did you see this, Alan?
**Alan West** 23:33 No, I didn't hear.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:35 is.
**Alan West** 23:36 Who is this? Who's publishing this?
**Matthew Hensley** 23:38 Oh, we…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:39 Bill… You go ahead, Matt.
**Matthew Hensley** 23:43 Yeah, so it's just, one of the vendors.
Did all these… they've been involved in OTEL for a bit. If we'll go back to the dock and open up the… All languages link.
Might be easier to look at.
That's to start with.
So they just made a simple app, they described the methodology of what was done here, but this is the overhead for the contrived application they put together.
And it's fun because .NET has its own write-up, and it's basically unmeasurable, as you can see here, for a couple of reasons, but one of them being that the CPU overhead is very low.
Generally speaking, but also a quirk of the vertice instrumentation means they can't run the tests they do on the rest of them, so…
**Alan West** 24:34 Hmm.
**Matthew Hensley** 24:39 But the actual .NET results page has.
some graphs on it, but there's stuff in there, it's like, wait, the async await engine.
It seems to be consuming more CPU than the actual OTEL SDK.
**Alan West** 24:59 Interesting.
**Matthew Hensley** 25:00 So yeah, that block there.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:07 Yeah, I mean, tomorrow I'm gonna, Take a look at… the benchmarks of my own, and try and get it to synthesize the overhead, because, like.
For anyone who hasn't seen this.
I got my own unofficial benchmark thing.
**Alan West** 25:29 Nice.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:34 Wife retired.
There's sort of tracks in the mirror scenarios, and I have, like, sort of, let me search for it like this, just for the sake of comparison.
Oh, there it is. So, I have, like, baseline… that's not the right one.
Baseline, and then logs, metrics, traces, so… I can't easily overlay, like, the baseline versus adding logs on, so I need to do some number crunching.
But in theory, I should be able to get some… what's the overhead numbers of these? Because that was what I was originally trying to measure with this.
In the first place.
It does find some interesting things now and again, like, SQL client.
They fixed a performance regression, so that's why there's a massive drop-off in allocation.
**Alan West** 26:32 Yeah, not that long ago.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 26:35 And then… This one, there was a… there was a regression in the AWS SDK.
That, made it go really slow.
**Alan West** 26:47 Cool, and you got it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 26:48 To be fair, it was only for when you override what the URL of AWS is.
Which the tests have to do for mocking purposes.
**Alan West** 26:58 Oh, I see.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 26:58 It wasn't like a massive, just general problem in the SDK, but It showed up as Big Spike.
On the, the graph, so… Reported an issue, and the folks there fixed it.
Yeah, unfortunately, because a lot of the PRs I've been doing recently are all on… in the OTLP exporter.
Because this is the user code path, they don't show up.
So I've yet they've yet to do a performance PR where it's had a big dip like this.
But, but yeah, I've got some num… I've been tracking my own numbers for the SDK. At some point, I want to get, continuous benchmarking set up in the repo, but it's been in my to-do list for a very long time.
**Alan West** 27:53 Totally, but that's pretty cool.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 27:57 I saw on, LinkedIn.
Earlier, CJ tagged me on a post.
from the person who originally shared this link at Koru.
asking them to engage with the hotel benchmarks repo.
To try and extend the scenarios there.
Because, yeah, ideally, this would be something OTEL would measure for ourselves, rather than.
Random vendors going and doing the numbers.
**Alan West** 28:35 Sorry, so you said CJ already reached out to that person, and…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 28:39 Yes.
**Alan West** 28:40 Connect them. Yeah, yeah, that would be great.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 28:43 I think, I think from our…
**Alan West** 28:44 work.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 28:45 Hmm. I think from our point of view, it's just unfortunate that they happen to pick the Redis instrumentation because it's like the one of the instrumentations we have that works differently to all the others.
**Alan West** 28:57 Oh, yeah, yeah.
That, so their, their benchmark across all the languages focuses on Redis instrumentation?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 29:06 I think it's I think they use Valkey, but yeah, I think they just picked like an arbitrary database to measure.
And because we've got the weird quirks of how the Redis instrumentation works, is it doesn't lend itself To be measured by their benchmark.
**Matthew Hensley** 29:28 the.
**Alan West** 29:28 Yeah.
**Matthew Hensley** 29:29 Benchmark app is some HTTP server, a minimal one, kind of like the Roadice examples in the docs, effectively, but it… pokes at a Redis-compatible database, trying to do some end-to-end things, and because of how the Redis instrumentation works.
the The benchmark just kind of… Absolutely slams this endpoint.
And because the Redis instrumentation flushes periodically, it actually ends up discarding a ton of the spans in the exporter because it exceeds the buffer, like, immediately.
So.
**Alan West** 30:05 Oh, funny.
**Matthew Hensley** 30:07 Yeah, I'm working on some tweaks, but not gonna put a ton of time into making that possible since we're working.
To hopefully move the instrumentation into the driver.
So…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 30:22 Do you have the link to that to hand, Matt, so I don't have to search for it and I'll just pull it up?
**Matthew Hensley** 30:27 Yes, I do.
Let me find this tab.
I'll say I have it, and then… Yes.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 30:51 Thank you.
I can't remember if we talked about this last week or not.
But yeah, Mark, who's one of the maintainers of the Stack Exchange Redis, I poked him on… This issue that's been lying around… for ages.
Because there was a update to the Redis driver that broke our, reflection.
So, we were like, could you just… Provide us a way to not have to do reflection.
And it seems enough has happened in .NET.
Metrics and traces over the last 5 years.
Or however long. that their… their knee-jerk… oh, it'll make it slow.
A reason to not do it has sort of gone away.
So he spun up something with Copilot.
that me and Matt have commented on.
Although nothing's happened on his side since then, that they might actually build metrics and tracing into the Stack Exchange Redis library directly.
**Alan West** 32:10 That'd be great.
I… I actually was never… up on the conversations with them. They… so they had performance concerns back in the day about using, what, like, diagnostic source for tracing and all that.
And metrics.
**Matthew Hensley** 32:32 Yeah.
there's long-standing issue. If you go dig through the ones referenced here, there's… Giant sets of comments, been talked about for years, and there's… concerns about what was… I think… Somewhere there's an issue about using event source.
There's ones about using activity.
But I think this recent, issue with renaming some private fields. It didn't just break the hotel instrumentation.
Broke a few vendors.
So.
Looks like we're gonna meet in the middle. Oh, go ahead.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 33:10 I was gonna say, yeah, I think it was, like, an earlier release broke… some Datadog instrumentation.
Then 3.2 broke.
our instrumentation, and then 3.3 broke the zero code instrumentation.
So it's, like, in the space of, like, 4 months.
They've broken 3 different instrumentation solutions with internal refactoring.
**Alan West** 33:37 Gotcha.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 33:42 But they seem open to, at least.
revisiting the topic, but nothing's actually happened yet.
But yeah, we might end up with something more performant.
more… In keeping with all the other instrumentation, and also with one less component to maintain.
**Alan West** 34:05 Totally. Yeah, that's the dream, right?
Cool, yeah, that's fun.
**Matthew Hensley** 34:18 In the spirit of potentially winding down the instrumentation, I'm Doing some quality of life things, like fixing up the docks, and… Some things like that, in case we're going to deprecate it.
Just make sure it's in the best state it… Can reasonably be without actually.
Fixing everything that's outstanding.
**Alan West** 34:40 Yeah, and if I recall, the Redis conventions Are not actually stable yet.
**Matthew Hensley** 34:48 Yeah, the Redis specific stuff is not stable, but the general database Spanometric conventions are.
But there's not really been a request to stabilize the Redis one, so this will be a good opportunity to see if we can… Get some of those in there, especially since we'll be working with, One of the driver maintainers, so presumably they know what would make sense.
**Alan West** 35:15 Yeah, that's kind of what was on my mind. Might be a good opportunity to, I mean, if he has bandwidth.
I have not studied the state of the Redis database conventions very closely, but… so I don't know what is actually holding them back from becoming stable, but if that can be identified, then yeah, maybe… maybe this is a good opportunity to work with a… Special matter expert on Redis.
**Matthew Hensley** 35:41 I think that's why they're not been marked stable. No one's asked.
**Alan West** 35:46 Yeah.
**Matthew Hensley** 35:46 put the time into it, so… I'm more than happy to work with Mark or whoever on implementing this.
And… Yeah, hopefully that'll give them some time to… Be able to guide us as to what would be stable, and we can get those checked off.
**Alan West** 36:09 Right on.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 36:13 Anything anyone else wants to chat about?
**Alan West** 36:18 Not for my end.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 36:26 Okay, cool.
With a lid for today. See you all next week.
**Alan West** 36:31 Yep, talk to y'all later.
**Navya Sharma (HealthStream)** 36:33 See ya. Bye-bye.
