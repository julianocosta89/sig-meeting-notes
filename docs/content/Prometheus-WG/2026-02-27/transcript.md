SIG: Prometheus WG
Date: 2026-02-27
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Jonathan Santos** 00:14 Zero.
**Arthur Silva Sens** 03:34 Hello!
**Jonathan Santos** 03:37 Hey, hello?
**Arve Knudsen** 03:40 Hello!
**Arthur Silva Sens** 04:16 Is anybody else joining today? So… So, empty.
I guess we wait for, like, 2 more minutes?
If nobody joins, then we just do it.
**Jonathan Santos** 05:20 Okay.
**Arthur Silva Sens** 06:25 Maybe we can start with your topic, Jonathan.
**Jonathan Santos** 06:30 Thank you, yeah.
**Arthur Silva Sens** 06:31 headquarters.
**Jonathan Santos** 06:34 It's about the… replace?
of Appender V1 to Appender v2.
I thought that the Appender V2 was just a testing thing, but I noticed that
It will be used, in production.
Like, the default.
And for this reason, I think that we don't need to put a feature flag on the hotel code.
We can just replace and test. But my doubity is…
We don't have benchmarks on the code, and maybe this replacement could be bad for the codebase.
And don't know… If we need to leave to the users, choose which is better.
Which append is better, or we just replace it and that's it.
**Arthur Silva Sens** 07:23 Like, if you look, not sure if you saw, but I… I built a quick PR,
Like, I don't know, almost 2 months ago? 1 month ago, I don't know.
And in that PR, I adjusted the benchmarks so we can compare the two.
But… like, this means that I keep the V1 implementation, and I keep the V2 implementation.
And then I… that's the only way I can benchmark.
Since we are trying to delete V1, Yeah.
Not sure if we can keep the code there.
I… There is a… there is this work that you… I see you…
adding the note that you want to work on this? Like, there is…
The Ubunta Limited Collector has a benchmark suit.
**Jonathan Santos** 08:25 If you want, you can solve this one first, like, add or benchmark to the test suit.
**Arthur Silva Sens** 08:30 Bloody Brandt for a few… for a few commits, I don't know, one week, two weeks, and we'd gather…
Benchmark results for a few weeks, then we…
switch to V2 and see if the results are better?
**Jonathan Santos** 08:48 But, for example, if we prove that the results are worse.
the Prometheus will keep the V2.
they will not, roll back to V1, right?
**Arthur Silva Sens** 08:59 I doubt… I doubt the results will be worse. Like, the interface is so much better for a hotel. Like, it would… it was designed to…
to make it better for Rotel.
Like, okay, if the results are bad, we should reach out to Bartek again?
**Jonathan Santos** 09:17 Explaining, but, like, I think it's not gonna happen.
What is most important for the repository? Have the most… recent version of Rometheus.
Or have benchmarks before… Validates that the appender is better.
**Arthur Silva Sens** 09:36 What do you mean by, oh.
Should I focus on replace the… the offender, or should I focus on…
**Jonathan Santos** 09:44 Have benchmarks to validate that a trend there is better.
**Arthur Silva Sens** 09:48 The benchmark PR is… it's very quick. I don't think it's going to be very complicated. Like, if you are using some AI tooling, they will nail very quickly.
So I think it's easier to lend the benchmark PR than the Panda V2.
**Jonathan Santos** 10:07 Okay.
Okay. Can you send to me the PR that you work?
**Arthur Silva Sens** 10:13 About the Panda V2?
**Jonathan Santos** 10:15 No, about the benchmark?
**Arthur Silva Sens** 10:17 I did not… I mean… I have a benchmark on my Pandor V2, PR.
**Jonathan Santos** 10:26 Okay, okay. You ready?
**Arthur Silva Sens** 10:28 But the benchmark I'm talking about is, like, the benchmark that I wrote in my appended V2PR is a micro benchmark.
And we need a macro benchmark.
that's related to the testbed, but I… let me pick it up.
the links.
**Jonathan Santos** 11:06 If I create a end-to-end, Test that will benchmark the whole code?
Is it enough?
Like, not test, individual functions, or…
The heaviest ones, but end-to-end implementation.
**Arthur Silva Sens** 11:26 Yeah, it's like, it's a… this testbed will spin up an OpenTelemith collector.
we'll have it configured with a Prometheus receiver.
we need to find a way to provide some data to this receiver. This, I have no idea how to do it, but we need to think about it.
And then it will run for a few, I don't know, 1 minute, 2 minutes, and it will keep scraping this app.
While it is scraping, we are benchmarking the… the results.
**Jonathan Santos** 11:59 It's very similar to PromBench.
**Arthur Silva Sens** 12:03 Probably not as sophisticated, but it's very similar.
The link for the PR is there.
But again, this is a micro benchmark, not a macro.
It would be very cool if we get this done before the switch, because the results are published in the hotel website.
And we'll be able to compare how much better It's gonna be.
**Jonathan Santos** 13:09 When the switch will happen.
**Arthur Silva Sens** 13:14 I mean, I mean, the switch from V1 to V2. It will happen once we finish the PR.
**Jonathan Santos** 13:20 Okay.
**Arthur Silva Sens** 13:31 Is that all the information you needed, Jonathan?
**Jonathan Santos** 13:35 Yes.
**Arthur Silva Sens** 13:38 Okay.
Okay, so the topics I… yeah, oh wait, let's get Kyle's topic on top.
Go for it, Kyle.
**Kyle Eckhart** 13:59 Oh, yeah. As I was looking at some series ref things, I was kind of questioning how the receiver handles the series refs plus staleness, and I think, you know, Arthur… Arthur jammed in a little bit, but I'm more looking holistically, because it…
There's a lot of awkward things there. There is one fix that definitely needs to be made, but there might be more.
And I can open issues for these, but I just was…
Kind of looking for a little bit of a… if anybody has
some knowledge enough to say, yeah, that makes sense as a problem, or if I should do some more digging, which is fine.
**Arthur Silva Sens** 14:42 I, honestly don't know enough.
Yeah, I don't know, something… something happened today, not very… not that many people were able to join. I'm pretty sure that Cryo knows this. He is the one that implemented this thing in Prometheus.
So he has a lot of knowledge.
**Kyle Eckhart** 15:05 Yeah.
My knowledge comes from similar, but an alloy, where that was why, when I was looking at it, I was like, this doesn't seem right.
Okay.
**Arthur Silva Sens** 15:16 Yeah, if you have experience, like.
**Kyle Eckhart** 15:19 Yeah.
**Arthur Silva Sens** 15:20 Like, just do what we think is right, and we'll look at the test and tell you if it makes sense or not.
**Kyle Eckhart** 15:27 I can go down that.
I just have to make time for it.
**Arthur Silva Sens** 15:31 Cool. But I'll ping Cryo.
Make sure he's on the loop.
Okay, so for my topics, not sure if you are aware, OpenTelemetry has several other special interest groups.
One of them is focused on the end user experience, and they… what they usually do is run
User surveys, they create content dedicated for end users.
And they reached out to me asking if we want to do a follow-up survey from a… from another survey we did 2 years ago.
And I've… yeah, I wanted David's input. He's not here, but I'll ping on Slack.
Like, the survey we did 2 years ago, it was mostly about…
UTF-8, if people like underscores, if they like dots, if they like unit suffixes or not, etc, etc.
So I'm not sure if, like.
If there's anything to follow up there.
But we could do other things if we want to.
anything immediately comes to mind? Like, something that you really, really want to know.
how end users are perceiving Prometes and hotel compatibility.
**Kyle Eckhart** 17:17 Would it be interesting to find out how many are struggling with the whole, like, to use it… use exporters in the hotel collector? I have to run all of those exporters, like, as a.
**Arthur Silva Sens** 17:30 Oh, boy.
**Kyle Eckhart** 17:31 Like, deployment?
It's a small I don't know if it's worth, like, another survey or not, but, like, it'd be interesting.
**Arthur Silva Sens** 17:40 Yeah, like, I… I think the survey that they did, it was, like, a 10 minutes long survey.
So we definitely would need more questions.
But we can start… Like, compiling a list, and…
Of, like, things we want to answer, and they will come up with the questions.
**Kyle Eckhart** 18:10 Because I think I'm going down a bit of that, path
Regarding… and, like, compatibility is kind of an interesting thing, where it's just, like, how many people would like to see hotel receivers for things that have exporters, and, like, you know, the feature gap between them, like, would people prefer
a native hotel receiver versus, like, a Prometheus exporter. Those are things that kind of come to mind.
But yeah.
Kind of noting stuff and seeing if we have enough for our survey makes sense.
**Arthur Silva Sens** 18:48 Hey, let me write this down.
**Kyle Eckhart** 19:17 And I guess even thinking out loud further, like, one of the things that we do know, which is why there is effort towards stabilizing Prometheus Receiver, it is one of the most used components.
And it'd be interesting to understand, like, why? Why is it one of the most used components? Is it because of immaturity of?
Like, hotel receivers? Is it…
the perception of, like, Prometheus receivers versus, or, sorry, Prometheus exporters versus the hotel receivers.
Yeah.
**Arthur Silva Sens** 19:58 Yeah, I mean, if they are running Prometheus exporters, that's the only way they collect metrics, if they're running the collector, right?
**Kyle Eckhart** 20:07 Yeah, which makes sense, right? Like, it's kind of an interesting thing of, like, like, Greenfield versus Brownfield. Like, if somebody's just, like, doing observability from the ground up, would they want to start with hotel receivers versus, like, where a lot of people are today, where they might already be rerunning from atheist exporters?
So it makes sense for them to just, like, keep using those, but through the hotel pipelines.
But as a long-term, like, would they rather see them as native hotel? Like, through… see those same things through a native hotel experience?
**Arthur Silva Sens** 20:45 Other thing that comes to mind is the SDK experience.
if they write their instrumentation with hotel or a Prometes SDK, and why they choose… H1?
What else?
I cannot think of anything.
Okay, I think that's a good…
In our first list, we can continue to iterate.
Mmm… Yeah, FYI, Prometheus 3.10 is out. We need to bump the… the dependency…
I'm… yeah, I'm not… If anybody has the time, just do it. If not, eventually I'll do it.
then for the Prometheus receiver, I think we are almost done, honestly. Like… Let me share my screen.
There is this… issue we just talked about, Jonathan, about the benchmarks?
There is one slightly complicated PR, Which is, like, Today, the way we build… Scope.
a hotel?
is that we look for a metric called… or telescope info.
And all the labels on this metric, we…
We transform into, scope attributes.
The spec has changed.
I don't know how many months ago, and this is not the way Scope is transformed to Prometheus anymore.
now… the scope… or telescope infometric doesn't exist.
And the scope attributes are directly built into the metric itself.
for example, if we have an HTTP…
request total. There will be labels.
called Autel Scope, and the name of the attribute.
If there are other metrics with different scopes, they are all like this as well?
So we need to switch the way we parse a telescope. Like, we need to stop looking for a telescope infometric, and we need to look at telescope labels instead.
Yeah, it's been hanging around for I don't know how many months. We need to… we need to implement this.
Yeah, Kai?
**Kyle Eckhart** 24:31 Oh, I was just gonna ask, is it something that has to be done in a backwards compatible way? Like, or is it just, like, we only care about the current spec version, and we can drop support for it?
**Arthur Silva Sens** 24:41 Since we are a beta component, we cannot just switch things out of the blue.
we need to add a feature gate, and then, I don't know, 2, 4 releases we switch completely.
So this is gonna be, like, one month
transition, I guess? One month, one month and a half.
Again, if nobody do it,
I have Hackathon week next week, and I'm not doing anything, so I'll probably just… Goal…
Pick up all the harder issues in the board.
But yeah, that's… that's it, actually. And then this is spec work, which is not really writing code, it's just reviewing the spec and make… adjusting wording.
**Kyle Eckhart** 25:48 And that one, like, the last one that you talked about is kind of the longest. Like, do we have to have it done and fully migrated for, like, us to be considered stable? Like, would that last time?
Yeah, got it.
**Arthur Silva Sens** 26:03 Like, once we get this implemented with the feature gates.
**Kyle Eckhart** 26:07 Yeah.
**Arthur Silva Sens** 26:07 It's just easy work, just, oh, now I'll switch to better, now switch to stable.
**Kyle Eckhart** 26:14 It's baby.
**Arthur Silva Sens** 26:15 Yeah.
**Kyle Eckhart** 26:15 As opposed to complicated.
**Arthur Silva Sens** 26:17 Yeah, yeah. Like, since we are so far ahead of all the other components, like, like, we can just chill.
And, if we have the time, it would be also nice if we can start helping other components
graduate, and then we release Collector V1.
But yeah, I have another meeting in 7 minutes.
Anything else you want to discuss?
Alright.
Then… See you online.
Bye-bye.
**Jonathan Santos** 27:00 I love this.
