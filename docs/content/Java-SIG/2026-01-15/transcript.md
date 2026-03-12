SIG: Java SIG
Date: 2026-01-15
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Bruno Baptista 00:02:49 Hey, good afternoon.
John Watson 00:02:53 Howdy, howdy.
GZ Gregor Zeitlinger 00:03:41 Hello!
Bruno Baptista 00:03:46 Thank you, Ricker.
GZ Gregor Zeitlinger 00:03:58 Oh, I'm… am I still the only one with topics? No.
Just didn't edit in the right place.
Trask Stalnaker 00:04:34 Hey, everyone.
GZ Gregor Zeitlinger 00:04:36 Hi, Trask!
Bruno Baptista 00:04:39 Hello?
Trask Stalnaker 00:05:04 Alright… Let's give one minute for Jack…
GZ Gregor Zeitlinger 00:05:38 Laurie not here today?
Trask Stalnaker 00:05:43 Not sure.
Cool, let's dive into, Bruno's topic.
I am, In case you hadn't seen yet, Bruno, I just… tagged you on a PR. Based on the discussion last week, I realized that despite our… Around the stability question.
We actually… Though we had… adopted this new practice, starting from 2.0, not to break telemetry. We actually had never updated our official policy.
on that?
So… Like, about… Is… a very… and it's very timely also around the whole… broader open telemetry stability question, that's being raised. And, so… I… I think we should… There were… I went back and reviewed the braking changes in 2X series.
And there were a couple that we intentionally accepted, due to them being… we were… we considered them low-impact changes to lesser-used instrumentations.
But I think that… It's better just to have a clear policy.
And stick to that.
And so there's a couple of interesting things that we… discussions we can have, sort of follow-ups to that.
But… I want to… Give you time, to talk about the performance results.
Bruno Baptista 00:07:58 Okay, thanks very much. So, let me share this… Okay, So, the slideshow… well, let's do it like this.
So, yes, last week we, ended up, being here because we were discussing that the agent was mark-stable, but I was claiming that the instrumentations were not, so… well, that escalated a bit.
But the… So, going back, the setup that was prepared was to have comparable results between the Parker's extension and the agent.
So it was fair for both, and to be comparable.
Quite…
Trask Stalnaker 00:09:06 The CURCUS extension is, it's tracing and metric.
Bruno Baptista 00:09:13 and logs.
Trask Stalnaker 00:09:14 And logs. Core.
Bruno Baptista 00:09:16 Yeah, but in this… in this performance test, we deactivated logs, because we… well, they… we wanted to measure the metrics and tracing performance impacts logs. We know that always cause, Slowdowns, and we didn't want to take that into account for now.
So, the… we wanted the real-world application, so this is based in Quarkus, using REST with Jackson, OpenAPI, Hibernate, we use Panache, which is… It's not spring data, but it's something comparable. Hibernate validator, Postgres, real Postgres, and, use entities, with, entity to DTO mapping.
Like most applications would do in production. And we don't use imperative business logic, so no reactive logic on the application side.
And no logs, as I mentioned.
So, and the baseline for the performance test is… this is running on custom hardware, so real bare metal.
And for the application, we are using just two CPUs, so less than that.
we believe that, Java workloads Shouldn't be one in less than two CPUs.
well.
Trask Stalnaker 00:10:47 At least in your, like, load… at least when you're doing any kind of load testing on it.
Bruno Baptista 00:10:52 Yeah.
Trask Stalnaker 00:10:53 Yeah.
Bruno Baptista 00:10:54 We started with 1GB of RAM, but, well, it's arbitrary. We measured several, but this was the baseline.
And, we went with the default spun batch size.
And… We settle around 10% sample spans.
and, JVM defaults, and, run this, Java minus jar.
On the machine, so no containers, but for the application itself, and no native for now.
So, and we did multiple combinations of this.
So just to remember, this… this is the profile that we showed last week.
So, this is the… The graph that measures the percentiles of the response times.
Remember that the, vertical axis is, logarithm… has a logarithmic scale, so things… Grow quite quickly.
And that, for this, for this case, we are measuring, 1,500 requests per second on post, 6,000 requests on GAPT, and for this particular version of Quarkus, and just 10% of something with the G1, a garbage collector.
1GB of ROM and no, parameters on the memory. We're set. And the guests and posts are happening concurrently?
Sorry?
The gets and posts are happening concurrently? Yeah, all at the same time. So they are independently calling the get and post endpoints, but we are only measuring the gets.
just… To make it seem.
Trask Stalnaker 00:12:42 Bruno, which one… which one of those is the Quarkus extension?
Bruno Baptista 00:12:48 In here, just the extension.
But this… sorry, oh, sorry, so micrometer only, in blue, the corpus extension in red.
Trask Stalnaker 00:13:03 Mike… Does micrometer only mean only metrics?
Bruno Baptista 00:13:11 Yes, but remember that this This is not just micrometer. Is micrometer shipped through OpenTelemetry?
So, the micrometer registry is implemented with the OpenTelemetry SDK.
So, what we are measuring here is basically open telemetry metrics.
Right, but no trace.
Trask Stalnaker 00:13:31 But no tracing.
Bruno Baptista 00:13:32 Correct, correct. With, with the blue.
Trask Stalnaker 00:13:36 Oh, okay, so that, that, that explains a lot.
Bruno Baptista 00:13:39 Yeah, so the rev includes metrics plus tracing, which is the same output that the agent performs in green here.
Trask Stalnaker 00:13:49 And… and did you compare the actual, like, spans… number of spans produced per request by both the agent and the Quarkus extension?
Because, like, I know with the agent, like, we… I forget, Lori, if Hibernate is on by default.
Lauri 00:14:10 It should be on.
Trask Stalnaker 00:14:12 Yeah, so we produce… we might be producing more spans in the agent than you are in the Quarkus extension.
Bruno Baptista 00:14:20 I did that to make sure that we were doing the same work on the both sides, and actually the extension is doing a bit more, because it also… the agent doesn't produce spans when it gets a connection.
It just, has a span when… with a query that is performed on that… on the database.
Trask Stalnaker 00:14:41 Oh, the database connect… get connection.
Bruno Baptista 00:14:43 Yeah, and we are also producing on the GetConnection, which is something that I'm evaluating, because I don't think people care much about it, so I might drop it in the future.
So there's… there's that.
Trask Stalnaker 00:14:59 Cool. Did you happen to capture, like, number of spans produced?
Through both.
Bruno Baptista 00:15:05 No, I didn't. No, I didn't. But, well, the number of requests, so they are 1.8 million.
Usually per run.
And… The sampling is, 10%? So I imagine that we are producing, over 10 minutes 180,000, spans. Well, traces, with more spans inside, so double that.
Trask Stalnaker 00:15:35 Yeah, I was mostly interested in the comparison of spans produced between, the Quarkus extension and the Java agent.
Given that.
Bruno Baptista 00:15:47 As you mentioned, like.
Trask Stalnaker 00:15:48 Quarkus extension captures some that the agent doesn't, and the agent captures some that the Quarkus doesn't, just from a… because that's where, like, all the cost is, right? Like, you can kind of say the number of spans you produced is… Kind of directly proportional to the cost of the instrumentation, so that's a big factor.
Bruno Baptista 00:16:11 Yeah, but here, I can assure you that the extension is producing more spends because of the connection thing.
Trask Stalnaker 00:16:21 Cool.
Bruno Baptista 00:16:23 So, the runs. We did many.
So, we started with, 500 on PUT and, 1500 on, on GET.
And… we have actually redesigned the whole application, because first, I had two… I was getting the throughput between two services, and I was measuring things… like that, but then I dropped one of the services, and I just stick with one.
It makes things a lot simpler, because.
Trask Stalnaker 00:16:55 Very… variability on test these benchmarks is tough.
reduce the variance.
Bruno Baptista 00:17:03 Yeah, that's exactly the problem. We need to get to a state in the app That, where we are measuring the effects that we think we are measuring.
So, because sometimes we think we are measuring something, and then we profile and see, oh, this is wrong, because the application is bounded by this particular feature, and we are not measuring the performance of the telemetry, we are measuring something else. And I actually spent I was not working on these all the time, but I probably spent half a year tuning the app.
So, now I can say that a real-world application is an application that is not tuned.
So…
Trask Stalnaker 00:17:52 Yeah, I mean, when I saw your, your, initial, like, I think the average response time from your service was, like, 1 millisecond.
Like, yeah, like… The agent is gonna show some over… some overhead on, you know, very, very high-performance apps.
Bruno Baptista 00:18:16 Yeah, so, what we did… so we changed many versions of Quark, because we did many experiments with the sampling, and sampling all the… Sampling everything is a performance killer.
And we very quickly settled on 10%, because It's not low enough, that doesn't produce… That many effects, and it's not high enough that, buries the application's performance.
And the batch size… Well, I experimented a bit with it, but it doesn't have that much of an impact, or that surprising, so the default, I think it's good enough for what we… doing here. We changed a lot the memory size and the type of garbage collection, and that's where we got the most surprising effects. So, the application works quite well with slow memory, so we even tested with 256 of HIP, and it worked properly, so no worries, but the performance is degraded, of course.
Trask Stalnaker 00:19:25 What kind of difference did you see, did you capture the difference between sampling ratio 1 and 10%?
Bruno Baptista 00:19:34 I didn't, but it's dramatic. It's very big.
Trask Stalnaker 00:19:39 Because the reason I ask is… is in these… I mean, you're producing… A thousand requests per second.
Multiple thousands. 8,000 requests per second.
Producing and… What's… what would you say average spans per request?
like, 5?
Bruno Baptista 00:20:06 No, it's one for the REST endpoint, and two for the database in the case of the extension, so three per request.
Trask Stalnaker 00:20:14 3, okay.
So, I don't know if for… like, for high… generally for… I mean, people are paying.
generally by, For the amount of telemetry that they produce.
And so, there's… I tend to see people go with lower sampling rate, although I guess conversely, for people who are sending to the collector and doing tail sampling, they would be doing 100%, so that would be even worse.
Bruno Baptista 00:20:46 Yeah.
Trask Stalnaker 00:20:46 So maybe…
Bruno Baptista 00:20:48 Yeah, I agree. I think it's fair.
Yeah, I stuck with the 10% because I think it's the bare maximum that people most likely we'll use in, in, in Pro.
But… Yeah.
Trask Stalnaker 00:21:03 Cool. So…
Bruno Baptista 00:21:04 We tested more CPUs, but it's Java. More CPUs is quicker, so… We stuck with 2 because it constrains more the problem.
So, and we did a bunch of, optimizations, like, so, initially, we were too ambitious, and we were doing GMS communication and everything, but… but we dropped that. We optimized Hibernate, quite a bit.
And we streamlined the connection pools. The numbers are a bit arbitrary, but they worked well, so we stick with them.
So, things like that.
Oh, and we tweaked… so, Quarkus use… uses, Vertex and, the event loops on Vertex that actually manage the… The connections that are being accepted.
That's quite a lot of work.
And… because we only have two CPUs, I limited to just one core, so the connection pools can work on the other core, without that much contention. That improved the performance quite a bit.
And…
Trask Stalnaker 00:22:16 And I assume, as you optimized the app, the cost of telemetry, relative cost of telemetry became greater?
Bruno Baptista 00:22:25 That's the… that's the idea, yes.
So… so basically, the effects of telemetry start to float, and you see consistent results between different… different firms.
Because in the beginning, when the app is not optimized, what you see is that sometimes, with telemetry, the app gets quicker, which is… Totally.
Trask Stalnaker 00:22:45 The variances, yeah.
Bruno Baptista 00:22:47 Yeah. Pain.
And sometimes the application is bound on by I.O, Of some sort, and by interleaving some of the tracing, you actually unblock things in a way that makes the application go a bit quicker.
But sometimes it happens.
Okay, then we got some weird, problems, so, we increased the… So, I don't know if you know what's a pneumocor.
So, you have… so these machines that we are using are dual-core. Dual-core in the sense that they have two chips, each one with 16 cores.
So, each of these, hardware cores is a pneumo core.
Trask Stalnaker 00:23:38 about CPU… two physical CPUs, not two logical CPUs.
Bruno Baptista 00:23:42 Exactly. So, 2 physical CPUs, each one with 16 cores. Oh, okay. These are beefy boxes, got it. Yes, yes. I mean, not…
Trask Stalnaker 00:23:50 Yeah, semi-beefy.
Bruno Baptista 00:23:52 And we are able to, to actually put in, allocate which core, the loads that we want. So we allocate the two cores to, to the app.
Unfortunately, we didn't realize that… well, we didn't thought about it, that we are… were… assigning to different… two cores from different NUMA cores.
And when you do that, What happens is that when you… memories are distributed by the pneumocores into regions. So, if you are in one core processing something that is in the memory of the other core, gas has to go to the other core.
content… with contention with the workload that is happening in there, and then go back. So, this causes a 50% drop in performance.
Trask Stalnaker 00:24:43 Wow.
Bruno Baptista 00:24:43 Just for that.
So, when you get, Docker containers and things like that, you don't control which cores you are using, and this is actually a problem that might happen in those environments. That doesn't happen when you can't control the CPUs that you get, so you have less latency this way.
Jack Berg 00:25:06 I was doing so.
performance testing recently, Bruno, and I think I ran into some similar things, like, I was, running these concurrency-bounded, performance tests, and I noticed, like, from one run to another, and this is a very, like, kind of micro-benchmark thing, so there's not a lot of noise in this, but I was getting huge performance differences from one run to another, and in my head, I chalked it up as, like, not all cores on my machine are the same cores, and so if you, like, if the tests run, just from random chance.
to get some of the more performant cores versus some of the less performant cores, it can just make a big impact.
And, like, and so I think you're describing something similar. My solution to it was to give enough test runs and enough time running where, like, any sort of differences, discrepancies between that type of thing are sort of averaged out.
And you get, like, a, like, you know, a decent answer, you know, if that sample size is large enough.
Trask Stalnaker 00:26:07 That works great for microbenchmarks.
But these sort of, like, more macro benchmarks, like Bruno's doing, man, it is… no matter how many runs you do, it is really hard to get the variance.
Bruno Baptista 00:26:23 Yes, yes.
Jack Berg 00:26:24 Oh, and it's terrible, because the runs take so long, too, so, like, if you get… if you make a mistake in your configuration, or, you know, you just overlook something, like, it could be a day to get a new answer.
Bruno Baptista 00:26:35 Yeah, and so… and the machines are… are… are just performance, performance machines, so performance-oriented machines, so the… the operating system is tuned.
In a way that, distributes the interruptions, independent… uniformly across the course, and it has some… Well, it has a… the buffers are optimized for I.O. and things like that, and, well, and other things that, well, we could go a very long time explaining these things, but… The idea is that we have to minimize the noise as much as possible in order to understand the real effects that we are trying to measure.
And we got signal, so… consistent signal. And… And then we started to experiment with, garbage collection, and that… that got the… the performance even, higher. So…
Trask Stalnaker 00:27:38 What Java version?
Bruno Baptista 00:27:40 So, Java 21.
Trask Stalnaker 00:27:42 Anyone?
Is it? So wouldn't G1 be default?
What is the default in 21? I don't know.
Bruno Baptista 00:27:51 Should be G1, I guess.
Okay, so… Streamlining got us the… to double, even more than double the throughput.
And then… We can show things like this. So, this is, throughputs. So, from, 1,000 requests per second on put, and 4,000 on GET until the double that. So, this is the default case with 2GB of RAM, using parallel GC, parallel garbage collection.
It's the same 10%, sampling.
And this is the case without observability, so just the app running, without anything else. And we see that, as we… we talked last week, we have the inflection point where… where is… That happens when the app starts to struggle.
But in this case, it's good enough, because it's, in all the cases, the app is working okay until the 99th percentile, meaning that 99% of the requests take less than the value that's in here. So, for the worst case.
It's probably 4… between 4 and 5 milliseconds.
response time.
Then…
John Watson 00:29:17 I'm… I'm a little… I'm a little confused, Bruno. It says 10% hotel spans, but no observability. What… what does… What's that mean?
Bruno Baptista 00:29:26 Well, this, well, no observability, no observability, but when we sample things, we do it with 10%.
John Watson 00:29:34 But…
Jason Plumb 00:29:35 But that shouldn't be on this slide.
John Watson 00:29:37 But that shouldn't be on the slide, right? Yeah, I think it's true.
Bruno Baptista 00:29:40 Great.
John Watson 00:29:41 There's no spans being generated, you're not sampling anything.
Okay, cool, thanks.
Bruno Baptista 00:29:47 Okay, so in this case, we have the baseline on the left, And we have, metrics.
the extension working with the metrics, micrometer pipeline to open telemetry, and then exported with the OpenTelemetry exporter. And… In this case, we see that Well, there's a performance impact, Once we increase the throughput, as, as expected.
But the application still is able to work, more or less. It's not that bad.
So, when we are tracing.
To the extension, we see further degradation, and we start to see that things with the medium profile of throughput starts to degrade a bit as well.
And then, we have the agent.
So… The agent works… Well, on the two first profiles, and not that… that well with the… with the last performance. And… I think I know why, because… it's because it does more allocation.
Peter Findeisen 00:31:13 Excuse me, I have a question here, because you'd never mentioned that, but did you measure the CPU utilization for these tests? It looks like you are trying to get the maximum throughput at the cost of oversaturating the CPU.
But in that case, of course, the variance of the latency will be super high.
And nobody really runs their application utilizing 100% of CPU. This is… this is not…
Trask Stalnaker 00:31:45 Wise.
Bruno Baptista 00:31:46 We measured memory being used, and the CPU, and usually the CPU is below 50%, each one of the cores.
Jason Plumb 00:31:58 What about the upstairs?
Bruno Baptista 00:32:00 Yeah, because there's a lot of I.O. Each time you go to the database, well, there's not much that can be done.
So no, we are not saturating the CPU.
Jason Plumb 00:32:12 Did you have headroom on the heap as well?
Bruno Baptista 00:32:15 So… 2GB, it's probably the high… well, we experimented with 4, and 4, of course, it works better.
Actually, the extension with 4GB is a bit slower because, well, the way garbage collection works. But I think the agent would benefit if the memory was increased. But… About the agent, there's some more surprising results that we are going to see next.
So, now, let's see the garbage collection.
So, this, this case, again, something great. This is the base case, no observability, there's no… Something, of course.
So, same 2GB, but we, We are going to analyze here the intermediate sampling rate, so 1500 onput and on post, And 6, 6,000… 6,000 non-get.
And this is the baseline. There's… there's not much variance, between the different types of, garbage collections, Until we start to add the telemetry.
So, the previous case here on the left, and we start to see that with metrics.
G1 works a lot worse than parallel.
with, with tracing included, we see a further degradation, but, the parallel garbage collection, works better as well.
But it's in the agent that is quite interesting.
So… the agent over-benefits if we use parallel garbage collection, because of the… it does more allocation, so there's more garbage collection happening here. And for this type of For this amount of memory, we found that, the G1 is a lot slower than the parallel.
And that's why things…
Trask Stalnaker 00:34:44 Can you remind me what, is this… is parallel GC mean parallel, young GC?
Plus…
Bruno Baptista 00:34:54 Stop the world.
Trask Stalnaker 00:34:56 So… Old gen parallel.
Bruno Baptista 00:35:00 So it basically scans the entire memory in parallel with the execution of a program, and doesn't divide the memory in regions like the G1 does. The G1, you divide the memory in regions, and you do… You try to, to, to garbage collect those regions and, basically, minimize latency.
But with the parallel GC.
Trask Stalnaker 00:35:32 Oh, is generally for throughput?
Bruno Baptista 00:35:35 Yes.
Trask Stalnaker 00:35:35 Versus latency.
Bruno Baptista 00:35:37 Exactly.
And so this… these are kind of the… the conclusions. So what… why is that much different? So… So, with G1, we have incremental concurrent compactions of the different regions.
But, for the… the parallel GC for small heaps, which, surprisingly, nowadays is less than 8GB, It's actually faster to scan the whole thing than UG1 in managing the different regions.
Lauri 00:36:09 Actually, this shouldn't be surprising. Parallel GC should beat G1.
For patch workloads, or, like, workloads that focus on throughput.
Bruno Baptista 00:36:20 Yeah.
Lauri 00:36:21 Because it's simpler, like, the concurrent GC comes with a cost.
Bruno Baptista 00:36:26 Yeah, but the fact is that with the agent, the difference is much… it's much more, relevant.
Trask Stalnaker 00:36:34 Probably, my guess would be that we're, because we're creating more, garbage, we're leaking it out of the young gen, where things get collected fast. Under load, things are escaping young gen into old gen.
I wonder if in… with G1, if you increased the young gen size, gave it a big young gen size to prevent the… memory from escaping from young Jen as much.
Bruno Baptista 00:37:11 That's something that can be done, yes.
Trask Stalnaker 00:37:18 Interesting, yeah, yeah.
But yeah, I think what Laura… I mean, it's interesting, because G1, I always think of G1 as, like, for end-user apps that you want, but maybe I'm stuck in 10 years ago, when small… when these large… what the large heap… small heaps were 500… Megs and not 8 gigs.
Bruno Baptista 00:37:43 Yeah, the scanning speed of memory increased quite a lot, and now we… well, we have those benefits in this form. Okay.
Trask Stalnaker 00:37:52 That's cool.
Bruno Baptista 00:37:53 So, there's also the startup time, we measure that, so… Basically, the agent has a penalty in… because, well, it has to instrument the code, and there's a lot more C2 compilation, and that's… and those C2 compilations are the reason why there's higher latency spikes with the agent, because there are some requests that get stuck with these C2 compilations that take longer, so the top percentiles will be harmed by that.
Jason Plumb 00:38:32 And I'm gonna ask an obvious question, Bruno, sorry. Early in the deck is a thing about ramp-up phase. All of the main results you've been showing so far are taking place after the ramp-up phase.
Bruno Baptista 00:38:42 Yes. Okay.
Jason Plumb 00:38:43 Just asking the obvious. Okay, cool.
Bruno Baptista 00:38:45 Yeah, it's on main. Of course, in here, it's not. Yep, okay.
Jason Plumb 00:38:50 Yeah.
Bruno Baptista 00:38:52 Yeah, that's it. That's pretty much it.
Okay, some conclusions.
So, tuning the app was important to measure the impact of observability, so, and the context of the execution matters quite a lot.
So, one thing that we can say is that the micrometers, micrometer metrics and bridge, which is basically the OpenTelemetry instrumentation that we have.
in the instrumentation repo has a minimum penalty, and basically there's no reason to run a production application even with high throughput that doesn't have metrics on.
So… Opentelemetry introduces, tracing introduces a penalty, performance penalty.
But it can be mitigated if we tweak the sampling.
use ProductGC, And, But there's a catch, and that's something that I need to say. So, we have used a quite uniform type of load.
And internet plug is not uniform, it's, well… Positive person distribution is spiking.
And… the garbage… the optimal garbage collection strategy, might suffer from this, from the type of load. And it's something that I want to test, but, well, generating Poisson load is a bit tricky, so I haven't done it yet.
Yep.
Yeah, so that's it.
Trask Stalnaker 00:40:42 Cool. I think my, my only objection here would be, repla… like, replacing micrometer metrics with just metrics, or open telemetry metrics, since you're actually… you're… you're really not using micrometer metrics SDK, you're just using.
Bruno Baptista 00:41:00 the API?
Trask Stalnaker 00:41:02 So I would either call that metrics, or I would call it open telemetry metrics, since the SDK is where the majority of that overhead and performance is being done.
Bruno Baptista 00:41:14 Yes. Yes.
Any other questions?
Jason Plumb 00:41:26 Yeah, did you track error rates?
Bruno Baptista 00:41:29 There was no errors. So, each time we… I had errors, I reduced the throughput.
Jason Plumb 00:41:36 Okay, so you, in all cases, you were running with 0% error rate.
Bruno Baptista 00:41:40 Yeah, yeah.
Jason Plumb 00:41:41 Okay, okay.
Trask Stalnaker 00:41:43 Is your test app code available?
Bruno Baptista 00:41:47 Yes, it's open source. I can… I will put the links on the meeting notes in a moment.
Trask Stalnaker 00:41:53 Cool.
Lauri 00:41:54 Did you try to investigate, what could be improved in the agent?
Or in the OpenTelemetry SDK.
Bruno Baptista 00:42:02 So, I know that we are over-allocating because we are resizing hash maps quite a lot.
Jason Plumb 00:42:09 You included last time that we didn't know if you were using the low allocation exporters, right?
Bruno Baptista 00:42:15 We didn't have a purpose we were on.
Trask Stalnaker 00:42:17 I… I looked, I think they are. I think the version that they're… they were using…
Lauri 00:42:23 did already have the low allocation by default on. Okay. Just by creating spans, you are allocating more stuff.
Trask Stalnaker 00:42:31 Yeah.
Bruno Baptista 00:42:32 Yeah, but the extension doesn't use that, Well, still doesn't use it now.
Trask Stalnaker 00:42:40 Oh, the extension doesn't use the low allocation.
Bruno Baptista 00:42:44 Yes.
Trask Stalnaker 00:42:45 Yes.
Bruno Baptista 00:42:51 So… yeah, I think the biggest problem that we have, and it's not just affecting the agent, it's also affecting the extension, because it comes from the instrumentation.
is the map resizing. We do a lot of that, and we spend a lot of cycles doing resizes of maps.
Trask Stalnaker 00:43:14 Or these are attribute maps, or did you notice which specific maps they are?
Bruno Baptista 00:43:19 Yes, the attribute.
Trask Stalnaker 00:43:20 apps.
Bruno Baptista 00:43:20 Yeah, attribute maps of all kinds, yeah.
Trask Stalnaker 00:43:24 Yeah, I really, I love… somebody had proposed a long time ago, and I think it's a great idea, is… and potentially we could do it through, I think the hope was through Weaver and SEMCOM generation, generating… instead of using HashMaps, generate structs.
basically for, like, HTTP SEMCONs, we already know which attributes generally were populating, if we could make that a struct. And then, you know, you could have still an overflow attributes map.
But that… that would be nice.
Because it's not only the, Resizing of the maps that hurts, but it's the memory locality.
That hurts.
Jason Plumb 00:44:16 My takeaway from looking at that data, Bruno, and those graphs, is that, like, it's actually a pretty good outcome. I mean, most of that stuff is pushed up above the 90th percentile, so, like, you've added this agent, got pretty low impact, low-effort instrumentation out, and, like, your 90th percentile is, like, barely impacted.
Like, that's.
Bruno Baptista 00:44:37 Yes.
Jason Plumb 00:44:37 It's pretty good.
Bruno Baptista 00:44:39 Yeah.
Trask Stalnaker 00:44:40 Same for the Quarkus extension, yeah. Oh, yeah.
Jason Plumb 00:44:43 Yeah, yeah.
Bruno Baptista 00:44:44 Yeah, remember that, There's always a difference. I didn't measure in percentage the… on nominal throughput, so on nominal request response times, there's an overhead, but it's… it's… it's not that big. It's not something that you say, oh, we shouldn't use this in production. No, it's… it's… it's not that… it's not relevant, I think.
And there are not many… High-performance applications that… Need to disable these kinds of features, because they need some more cycles to do work.
Yeah.
Jason Plumb 00:45:29 Yeah, being able to do 7,500 requests on two cores and using Hibernate, that alone is a success.
I think.
Bruno Baptista 00:45:37 Yeah, and it's able to do a lot more, but… well, I need to fix a few things first.
I think it's able to do more, well, but that's ongoing work. When I have more results, I will share with you guys.
Trask Stalnaker 00:45:52 Oh, time flew.
Jason Plumb 00:45:54 Yeah, 20 minutes.
Trask Stalnaker 00:45:55 happened.
Jack Berg 00:45:57 Trask, what's your idea?
Trask Stalnaker 00:45:59 Oh yeah, go ahead.
Jack Berg 00:46:00 Had added.
Trask Stalnaker 00:46:01 Dude.
Jack Berg 00:46:01 generated, from SemComf, how does that change the memory profile?
Trask Stalnaker 00:46:08 So instead, for the attributes.
Jack Berg 00:46:12 Yep.
Trask Stalnaker 00:46:13 it would be nice if we could have, like, in our HTTP instrumentation, HTTP client instrumentation.
We could use a special variant of the attributes Object.
that is not backed by HashMap, but is a struct, so it would have, server address as a field, it would have fields directly in there.
for the common SEMCOM attributes for HTTP clients.
Jack Berg 00:46:46 Oh, okay, I see. A version of that could be, you know how the attributes implementation that is in the API that's, like, Attributes Builder, that uses, like, an array backing instead of a hash map backing?
And, you know, the semp-generated code could just directly output those attributes from the API, rather than using the HashMap-based implementation in the SDK. Because the only thing we get in the SDK implementation is, is, the attribute limits integration. That's why we have that, so we can track as entries are added, we can truncate them for length and stop adding them once we reach a certain count.
Lauri 00:47:28 Agent actually has its own implementation of the attribute that's based on a hash map.
Jack Berg 00:47:35 Oh, okay.
Interesting.
I don't think I knew that.
Anyways, okay.
Trask Stalnaker 00:47:42 Bruno, on the remaps, Do you… like, if you have any more details about that, it might be interesting, like, if it's something that should… Like, is that just the resizing from the initial… like, I forget if… I think HashMap now starts at zero, basically, and lazy at…
Bruno Baptista 00:48:05 I think the default is 16, but once you get to 75% of that, you get a resize.
And we are using the defaults, and right now, I looked at the code, and we cannot set the initial value, because if we could, we know how many elements we are going to add. We just set the right value without growing, and it will be settled, and it will be fine.
Trask Stalnaker 00:48:32 Are we adding more than 12 attributes?
Bruno Baptista 00:48:38 I think so.
Trask Stalnaker 00:48:40 Okay.
Yeah, that would be really interesting. If you gather some info and open an issue for that, that would be… Interesting to look at what we could do around either Providing a way to specify the size, or to change our default size if we think that would be beneficial across the board.
Bruno Baptista 00:49:06 Actually, I started a PR.
But, well, I will publish it in drafts, probably next week or something, and let's see… let's see what you guys think.
Lauri 00:49:20 I think.
Trask Stalnaker 00:49:20 Yeah, yeah.
Lauri 00:49:21 I had a couple of pull requests that we didn't merge that wanted to tackle this, that, I think the instrumenter made a copy of the attributes at one point.
Maybe in Dawn End or something?
Trask Stalnaker 00:49:35 Yeah, I think the Alibaba folks were looking at this.
Lauri 00:49:39 Yeah, but I think that effort didn't get anywhere.
Trask Stalnaker 00:49:43 Yeah.
Jason Plumb 00:49:43 The attributes map extends HashMap and, like, has a capacity that's passed to it, but not passed to the superclass?
Oh, man.
Trask Stalnaker 00:49:55 Let's get an issue going.
Jason Plumb 00:49:56 Yeah, let me ride.
Trask Stalnaker 00:49:56 or a draft PR.
Lauri 00:49:58 Let him go, yeah.
Trask Stalnaker 00:49:59 Yeah, I'll.
Lauri 00:50:00 You'll still require, like, some analysis, like, what exactly… Easter to improve.
Jason Plumb 00:50:06 Yeah, rabbit hole.
Trask Stalnaker 00:50:09 But yeah, we can, Bruno, once you open some… either issue or draft, whatever you want, I'll go… I can… Lori or I can go dig up links to what the Alibaba folks tried previously, and we can go from there.
Bruno Baptista 00:50:26 Okay, thanks.
Trask Stalnaker 00:50:31 All right, well, time flies when you're having fun. We've got, 8 minutes left, but, luckily not a huge Agenda, I'll just turn it over to you, Gregor, for the rest of the meeting.
GZ Gregor Zeitlinger 00:50:47 Yeah, I think we'll leave it at the first one, then roll over to the next one.
Yeah, config provider. There has been some interesting discussions, And, I would say, basically, it is about the question, what do we do, for users who… Want to continue using system properties?
Even, in the future.
Because my response was, oh, well, in the future, you are gonna have to use declarative configuration, and then Laurie said, wait, maybe that's not what we want. So I wanted to discuss what our plan is for the future.
Jack Berg 00:51:38 In a nutshell, my perspective is to keep supporting environment variables and system properties forever, but stop investing in making them better.
GZ Gregor Zeitlinger 00:51:50 So, does that mean, that we should not add support more for… for more settings than we have now? Like, in the future, we have a new, A library, and we have declarative configuration for it, and that means users would need to use declarative configuration.
for that.
Jack Berg 00:52:11 I think it's a bit nuanced. I struggle to take a hardline stance of, like, hey, we should never add any more system properties or environment variables, because, you know, I've encountered situations where, despite the specs moratorium on expanding environment variable definitions, it's just, like.
it just doesn't make sense any other way. And like, an example of this, and I think this is kind of getting to what you're asking, is We add a new instrumentation library. We have a standard for how you enable or disable instrumentation libraries using environment variables and system properties.
should we just, like, not have a new environment variable for this new instrumentation library? Should we stop following the pattern that we've been, you know, having up until this point? And I think, no. Like, that doesn't make sense.
So, like, if there's a pattern already to say, like, hey, every instrumentation library has, like, an enabled or disabled System property or an environment variable, continue to expand that pattern.
GZ Gregor Zeitlinger 00:53:16 No, that's, that's not the case where we have the argument.
Trask Stalnaker 00:53:21 Gregor, can you scope this to, like, what are we talking about? Are we talking about agent users? Are we talking about Spring Boot Starter users, or are we talking about SDK users?
GZ Gregor Zeitlinger 00:53:33 Agent, let's talk about agent. I think this is, what we discussed, and we should focus on that first. So, we have a setting, JDBC-related, where currently you can use system properties, And, when we talked Trask, we decided that, starting with 3.0, we would like to remove this. So this class is deprecated now, or I have a PR where it is deprecated now, meaning that it would be removed in 3.0. That means… Users would not be able to set… use the setting anymore.
Unless we… Find another way, like building a bridge somewhere that users can opt into using.
Trask Stalnaker 00:54:18 Doesn't our… doesn't the age… I mean, doesn't the bridge that we have now in the agent already solve that problem?
Because users can use system properties, and we… in the library instrumentations.
We can use declarative Config API to read it.
But that will get bridged by the agent, because we do… the agent does have that bridging from system properties to declarative config.
GZ Gregor Zeitlinger 00:54:49 So, out of the box, it would not work, because the instance of OpenTelemetry that we're passing in… as a library user is not controlled by us, like, by the agent. So the user would need to provide an instance that has…
Trask Stalnaker 00:55:08 talking about… You're not talking about the agent, Sam?
GZ Gregor Zeitlinger 00:55:13 Oh, sorry.
Trask Stalnaker 00:55:14 Can you, yeah, can you…
GZ Gregor Zeitlinger 00:55:18 Yeah, right. And not the SDK. Right, it's about library instrumentation, sorry.
Trask Stalnaker 00:55:25 Okay, library instrumentation.
Okay, because do we agree on the… I think we have… I feel like we agree on the agent story.
Which is that we have the bridge, We read in all our agent instrumentation, we use declarative config.
But we automatically… we will continue supporting system properties and mapping that into declarative config.
And… The system properties will work fine for all these flattenable things.
Obviously, if people want the fancy stuff now, like JMX metrics, samplers, they'll have to migrate to declarative config.
GZ Gregor Zeitlinger 00:56:14 Yeah, that's right.
Trask Stalnaker 00:56:17 So, for library instrumentation, And this is why you wanted… you were proposing this over… the bridge over here in the SDK repo.
Or in Contrib, or something.
GZ Gregor Zeitlinger 00:56:38 Right, so that it's easy to be reused. It could also be in the agent repository, but There is no need for it.
Jack Berg 00:56:48 So, I guess I have a blind spot, now that you're talking about this. If I'm adding library instrumentation.
You know, I manually add some code to my repository that, like, installs or wraps my HTTP client with the library instrumentation, or whatever the install path is. Do those library instrumentations typically automatically read system properties and environment variables to configure themselves?
Is that, like, the current design?
GZ Gregor Zeitlinger 00:57:15 Typically…
Trask Stalnaker 00:57:16 Dried non-.
GZ Gregor Zeitlinger 00:57:17 raided.
Trask Stalnaker 00:57:18 We tried not to.
Lauri 00:57:20 It's only for some, like, really special cases. It's for the cases where you can't manually configure it.
Jack Berg 00:57:30 Because it's, like, it's not accessible, like, JDBC-style things, that it's, like, you know, it's loaded via SPI or something like that.
Lauri 00:57:37 Yeah, like, the JDBC driver is loaded by something else.
And you can't easily configure it, so it reads the… System properties, which… I guess since it isn't, like, A common use case?
We could, like, consider dropping the support for system properties and the environment variables, but on the other hand, like, if we do it correctly.
then we don't need to do it. It shouldn't add, like, too much extra effort from our side.
Jack Berg 00:58:11 Can you expand on that?
What does this correctly mean in your mind?
Lauri 00:58:16 Like, how hard could it be to, like, read from the declarative configuration when the declarative configuration is available, and if it's not, then just fall back to the system properties and the environment variables as we used to?
Like, virtually 100% of the use cases are, like, simple properties that don't require any of the fancy structured stuff.
GZ Gregor Zeitlinger 00:58:42 Most of them are, yeah, that's right.
Trask Stalnaker 00:58:46 Lori, would you… I mean, I'm fine with supporting the existing ones that way, but as we… now that we have declarative Config API, that, was kind of what we were holding off on, adding lots of config support to library instrumentations.
And… Can we just lean into Declarative config for all of those.
New ones?
Or… you would prefer to…
Lauri 00:59:20 What do you mean by the new ones? Like, do you plan to implement this, like, that somebody was asking, that instead of using the programmatic configuration API, you would use declarative configuration?
Trask Stalnaker 00:59:33 Yeah, so, like, in the HTTP libraries, like, the known… setting… setting the known methods, right? We… we allow that via programmatic access, but we could now, with declarative config, start reading that from defaulting that to The declarative config value.
Jack Berg 00:59:54 I would want to have both.
GZ Gregor Zeitlinger 00:59:56 That's awesome.
Jack Berg 00:59:57 fair.
Trask Stalnaker 00:59:58 Oh yeah, of course.
Jack Berg 00:59:59 Okay, you don't get rid of the programmatic option, but you just, like, allow you to source the information from declarative convey.
Trask Stalnaker 01:00:06 We would default to the value from declarative config, and then the programmatic would override that.
Jack Berg 01:00:12 Yep.
Lauri 01:00:14 Yeah, I think for that use case, it would be fine to, like, just focus on the declarative configuration.
Trask Stalnaker 01:00:26 So it's just, Gregor, these handful of… I mean, what are we talking about, 10 or fewer?
Cases where library instrumentation today reads from system properties.
GZ Gregor Zeitlinger 01:00:39 Well, if you're using, the HTTP client builder, then you can already say that you want to use, that you pass on an OTel instance, and then it reads it from there, so… from the config provider. So that already works.
But, you would need to pass.
Trask Stalnaker 01:01:01 No, I'm asking… I'm asking about… that… we all agree on the declarative config path for library instrumentation.
The open question here that you're asking, as I understand it, is what to do with system property access.
GZ Gregor Zeitlinger 01:01:17 Yeah, that's what I meant.
You can, you can use system properties if you have a config provider that reads from system properties.
Trask Stalnaker 01:01:29 If you're using the Java agent.
But that's not library instrumentation.
Lauri 01:01:35 I think Gregory's proposing that, By default, you use the declarative configuration APIs, but you could have the declarative configuration API configured with some sort of preach that falls back to system properties and the environment variables.
Jack Berg 01:01:53 Yes.
Lauri 01:01:53 So instead of handling it inside the library instrumentation, you would somehow configure your SDK to do the right thing.
Jack Berg 01:02:03 Yeah, so where is today, the agent, has this special capability where all the properties can be configured via environment variables or declarative config using the bridge. Gregor's saying, hey, lift that up… lift that up so that library instrumentation has the same property.
GZ Gregor Zeitlinger 01:02:20 Yeah, I'm wondering if that's a good idea. Actually, that was your idea, Jack, when we talked about, is config provider actually only be meant to be read from YAML? And then you said, no, actually, that's not a constraint, and we could have a config provider as a concept that reads from other things. And I thought, okay, maybe it would be, also system properties.
It wasn't clear to me that the spec was meant to be like that, but Would be an option to do it that way.
Jack Berg 01:02:55 Well, the spec is, like, intentional about the differentiation between the API and the SDK, because, like, you know, for no other reason than the OpenTelemetry SDK should not be the only implementation. So it doesn't necessarily… like, I didn't write the spec to say that, like, with the thought in mind that config providers would be implemented with environment variables, but, like, it's possible to imagine it, and we've done it in the agent. And… like, I don't know what the answer is here. Like, on one hand, it's like, it's kind of inconsistent that library instrumentation functions diff… if library instrumentation were to function differently than the agent, like, if in the agent context you could use system properties and environment variables for just about everything using the bridging, but in library instrumentation, you couldn't.
That's kind of weird. I also feel a little bit weird about, lifting this bridge up into the OpenTelemetry Java repo. I don't know why, I haven't really quite thought about, like, why, but, like.
Trask Stalnaker 01:03:50 I find it weird… I find that weird because, I mean, it only applies to the instrumentation node anyways, and the SDK, right, is everything, so it's kind of this weird carve-out that we've made in the Java agent.
And I do think it would be inconsistent to have it. And that's why there was all this discussion initially about not supporting system properties in the configuration. I mean, not supporting flattened properties.
Yup.
Alright, thanks, Nal, this is a… Topic for next time.
GZ Gregor Zeitlinger 01:04:30 Yep.
Jack Berg 01:04:30 Yeah.
Trask Stalnaker 01:04:31 See y'all.
GZ Gregor Zeitlinger 01:04:32 True.
