SIG: Java SIG
Date: 2026-08-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:15 Hey, early birds.
**John Watson** 01:22 I like to think of it as on-time birds.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 01:29 Speaking of early birds, Trask, I feel like I've been seeing you operating in a different time zone recently.
**Trask Stalnaker (Microsoft Corporation)** 01:35 Yeah… I've not been… I've been waking up too early.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 01:42 Wasn't sure if it was, automated Trask.
**Trask Stalnaker (Microsoft Corporation)** 01:46 The ones in the middle of the night, like, there definitely has been some of the automation still going.
Overnight, I've noticed they've been… Still doing stuff. But yeah, the human version.
Has been… Awake too early lately.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:07 Yeah, okay, I joined late, but, you know, sometimes I see notifications at times that makes me worry, and I was hoping that AI would be involved, so I'm glad to hear that.
Glad to hear you sleep sometimes.
**Trask Stalnaker (Microsoft Corporation)** 02:23 Yeah, I'll, well, Lauri, sorry for the mess I've made of our repository.
Lately, with this messaging, work is… Kind of spiraling a little bit.
**Lauri Tulmin** 02:44 Yeah, there is quite a bit of pull requests.
**Trask Stalnaker (Microsoft Corporation)** 02:50 Yeah, yeah, I'm trying to keep… there's way too many in draft, I know, but, like, I mean, and I notice you review some that are in draft, and thank you for… That, but, yeah… this…
**Lauri Tulmin** 03:06 If you have some sort of preferred order.
That I should be reviewing, I mean, let me know.
**Trask Stalnaker (Microsoft Corporation)** 03:14 No, the ones that are not in draft are, the ones that are my preferred order. But there's actually not… you've… you've caught up on… All of those, pretty much.
Yeah, I'm reworking the messaging stuff right now based on your feedback, Lauri, about the, receive telemetry.
Thought about that some more, and I agree, with… yeah, I have forgotten all the nuances of the messaging spans.
But I like the idea of keeping it… keeping the receive span stuff essentially the same as… what it is today. I left a comment, With, sort of, outlining The… the small changes that, I'm gonna make there.
**Lauri Tulmin** 04:15 Yeah, I think I saw that comment, but it was kind of weird, because… I got, like, the email notification, but for some reason GitHub didn't show your comment.
**Trask Stalnaker (Microsoft Corporation)** 04:24 That was because my agent made a comment without my permission, and I deleted it.
**Lauri Tulmin** 04:31 And it was a.
**Trask Stalnaker (Microsoft Corporation)** 04:32 It was a dumb comment, and I deleted it, and I posted a real comment afterwards.
**Jason Plumb** 04:44 And hopefully you scolded it and rubbed its nose in it.
**Trask Stalnaker (Microsoft Corporation)** 04:49 Yeah, I have an instruction somewhere that tells it not to open… not to write comments without, like, my explicit approval.
of… But… I think it's… circumvented me, somehow.
Alright.
Let's talk briefly about 3.0… What do we have?
Okay, this is… the messy one, but, hopefully by your tomorrow, Lauri, I'll have this the received telemetry stuff reworked, and I think that cascaded into a bunch of other places, like metrics and things, so hopefully I'll have A bunch of things ready, for another look tomorrow.
Probably a need to, I mean, certainly, we'll… well, I guess we've got two options from a release perspective.
I'm not sure if we're gonna… I'll need to look and see if everything can be in, like, next week.
Whether that's realistic or not.
Otherwise, we might need… Another month, still.
And I know I keep picking up some other things, here, like stabilizing some of the, instrumentation libraries, but… actually pretty happy with where… I like the include-exclude stuff, that… landed, and I feel like that resolves some of the… Questions, both in the stabilizing our existing library instrumentations, as well as, kind of.
pairs into a couple of discussions that have been going on with some other features that people had wanted to be added around include exclude for MDC, include-exclude for, like, micrometer metrics, metrics bridges.
**Lauri Tulmin** 07:30 I think, for micrometer at least, for library instrumentation.
It is actually possible, I think, to register some sort of filter that excludes, or, like… Excludes the metrics, even, even now.
Because it… I think it's set directly on the… On this meter registry.
So…
**Trask Stalnaker (Microsoft Corporation)** 08:00 So that would be, like, for this kind of thing?
**Lauri Tulmin** 08:06 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 08:10 would that work for the Java agent, or that would be a programmatic…
**Lauri Tulmin** 08:17 That would be programmatic, but for the Java agent, then… I guess it would be the metric views.
I think for micrometer, it might be more useful if, We had, like, some sort of, like, defaults.
like that… I think what we need isn't, like, that much maybe for micrometer, but more for, like, Spring Boot.
So that, you could exclude the metrics that conflict with the built-in OTL metrics.
**Trask Stalnaker (Microsoft Corporation)** 09:00 Yeah, so if we used our knowledge of that… Or figured that list out instead of,
**Lauri Tulmin** 09:09 That could be something that the users actually want.
So they could get, like, whatever the, like, all the metrics that the Springput can produce, minus the ones that UTL already has.
Without running into some, like, I guess maybe, like, the… the worst case is, like, the JVM metrics, how, like, the metrics with the same name.
So, you start to get warnings.
That, some metrics was reported twice in the same cycle.
**Trask Stalnaker (Microsoft Corporation)** 09:47 Jay, I think you were doing some investigation at one point about the overlap?
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 09:55 Yeah, I have, like, a… a repository, I just put a link in the chat, where I did kind of what I've been doing in the agent repo, where I set up some test harnesses and ran some applications and intercepted the metrics And then I was trying to do some comparisons between What we emit versus what they do, find the overlapping ones, and then see the deltas.
And I was able to come up with, like, the… I have an example view config that does drop all the ones with, like, the conflicts, or… it wasn't just, like, names, some of them have different units and types, too.
But all that to say, like, I do have this information. If we have, an idea of how we want to solve it, I could… I could probably work on that.
**Trask Stalnaker (Microsoft Corporation)** 10:43 Yeah, I think it… Makes sense. I mean, long-term, I would… love to be able to, like, see what we… what users want that's out of micrometer, or have, sort of, all of those natively in, OpenTelemetry.
Via, maybe JAMX metrics, other things.
But, yeah, I think Laura has a good point that You know, that… short-term… what users… What would probably make users happy is if we could filter And that would be a good thing to do in… 3-0, since it would… or to put behind the V3 preview flag.
Since… I guess we could certainly call that a bug fix, but it might be easier… we might be able to be a little bit more aggressive if we call it a breaking change.
So the… I guess… it would… Lauri, you're thinking it would apply… By default, to the micrometer… bridge, regardless of whether it was in the Java agent, or the starter, or library.
**Lauri Tulmin** 12:13 Honestly, I don't know, like, what the best solution is.
Like, this was just an idea, like, how we could make, the micrometer instrumentation better.
**Trask Stalnaker (Microsoft Corporation)** 12:27 Yeah, so Jay, maybe, you could propose something, and we can… See how it feels, what it looks like.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 12:38 Yeah.
I'll, I'll put something together.
A little Bonsai initiative.
**Lauri Tulmin** 12:45 Maybe it is, like, that we need some sort of includes and excludes.
And some sort of, like, default set of excludes.
That would make, it's easier for users to… Get using both micrometer and ultral metrics.
Something that would, like, satisfy most of the users.
**Trask Stalnaker (Microsoft Corporation)** 13:11 Yeah, so with the include-excludes, we can have a default of excluding certain ones.
If we want to go… if we want to add the includes-excludes as a user configurable.
The one awkward thing is that if you do want to Exclude a few more.
Question… we have to decide whether the new… When there's a configuration, generally that overrides the default, so you would need to resupply all of the excludes that were in our default.
But… So… But if we decided to not tie the list of duplicates to the include-exclude feature.
Then we could sort of just be like, hey, we just always exclude these metrics.
from micrometer.
if somebody… Complains about it, we could add a toggle just for that or something.
**Lauri Tulmin** 14:25 Yeah, that makes sense.
**Trask Stalnaker (Microsoft Corporation)** 14:32 Cool.
Anything… any other questions?
discussion topics around the V3 staff.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 14:46 So, I'm in the background, I'm preparing, like, the… I'm gonna have some… a blog post come out, and social media posts announcing the RC.
And then followed up with that with, like, a more in-depth one for the actual 3.0 release.
So I think between the time where I drafted it initially and now, we've done a bunch of messaging stuff, so I'll update it to include, kind of, the current state of affairs for that. Are there… Is there anything else that you wanted to call out in the RC for people to, like.
Validate or pay close attention to.
**Lauri Tulmin** 15:22 I guess messaging, maybe.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 15:25 Right, yeah, that one I'll add, like, a… I think that's the biggest one.
At this point.
**Trask Stalnaker (Microsoft Corporation)** 15:32 Yeah, and I forget, but I would just, maybe look through… The PRs for anything else that's hidden behind the V3 preview flag.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 15:43 Okay.
**Trask Stalnaker (Microsoft Corporation)** 15:45 I think that's a pretty reliable indicator now.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 15:51 Cool.
Alright, cool, yeah, so I'll do another round of that, and then I'll ping you guys when it's ready for another review. I mean, if we're gonna do it, you know, next week or whatever, otherwise we'll have some time, but…
**Trask Stalnaker (Microsoft Corporation)** 16:03 Yeah.
Alright.
Let's… moving on, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:15 Just a call for reviews on this PR.
I'm taking another crack at improving the performance of, explicit histograms when there's contention.
Yeah, there's a… there's a lot of content in this PR description, a lot of… data to consider. And so, I can answer questions here if anybody has one, but the gist of it is that, there's no way to improve the contented performance without regressing the uncontended performance.
I've thoroughly explored this problem space.
That's just not gonna happen. And so our options are, you know, accept the trade-off.
And try to minimize the trade-off, try to minimize the regression.
And… or… provide an option to the explicit bucket histogram aggregation, where users can express a preference of whether they want an implementation that is optimized for uncontended performance or contended Performance. And so there's this, we have this new, sort of, builder pattern and options for what… that we pass to Explicit histogram called explicit Bucket histogram options, and it has things like, you know, your bucket boundaries and whether to capture min-max, and so we could add a new parameter to that that was an expression of, like, whether you… what type of performance profile you want to optimize for.
So that would be sort of the escape hatch if the regression is too much to… to… Accept.
**Trask Stalnaker (Microsoft Corporation)** 18:03 This… this looks, a lot better than what I remember the numbers were before. Am I misremembering?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:13 I think they were before on the order of, like, maybe 20 to 30%, so they might be a little bit better, because I found an op… an optimization in here that I'm bundling in with this change to make it more palatable. The optimization is basically, like.
Hey, when you're, When you record a measurement, and you don't include an explicit context, so you're using the implicit context.
We always, currently, look up the current context.
Even though we only use it in select situations. And so, basically, I made the implementation smarter, and I say, only look up the current implicit context if you need to, and that offsets some of the regression.
And also improves everything across the board, and I know it could be considered as a separate change, and I'm politely bundling these together to make the overall picture seem a little bit better.
So… Yeah, anyways.
There's a details expansion, if you want to actually go see the before and after of.
**Trask Stalnaker (Microsoft Corporation)** 19:33 Oh, okay.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:34 every case that matters. It's just, you know, I don't want to overwhelm people with information. And if you scroll to the right, you actually see the diff.
**Trask Stalnaker (Microsoft Corporation)** 19:43 Okay, so what are… So, minuses are bad, or pluses are bad?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:49 Minuses are bad.
Okay. So, yeah, that's, like, the entry… yeah, that one's one of the higher ends.
higher end regressions.
And on the positive side, we get up to 1200% improvement for contended performance, so…
**Trask Stalnaker (Microsoft Corporation)** 20:33 I think it's good.
Myself.
Trying to think, like, uncontend… like, how often is this the… Bottleneck for an application, especially if they are… in the uncontended case, that means that there… Not hammering the metrics.
Anyways, which… means I wouldn't… they… I would suspect that they're generally not bottlenecked on metrics.
So this is not going to… Change their, sort of, overall… application… profile.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:23 Yeah, so trying to prioritize the uncontended case, like, The argument for it is… and I think back to Bruno, his performance benchmarks he showed a few months back, where he was trying to measure for, like, realistic applications what the overhead was of the Java agent and the SDK compared to other instrumentation systems.
And, you know, for almost any realistic workload, your instrumentation is not the critical path.
There's just… there's so much else going on, but you still… you still care about any measurable change in the latency, in the allocations, that adding that instrumentation provides. So, you know, that… that to me is the case for minimizing the… Or improving the uncontended performance.
Right? Because, you know, even if the metrics aren't on your critical path, you still want to avoid unnecessary work to keep your overall, latency down, but… You know, trade-offs.
**Trask Stalnaker (Microsoft Corporation)** 22:40 John, any thoughts?
**John Watson** 22:44 No, I mean, my main thought is that this is a lot of theater.
Like, I think for the very cases we… I mean, the very reasons we just said, like, the number of cases that this actually ends up impacting realistically is small, but it's probably important theater, because Any, any, FUD.
that a competitor instrumentation library can throw out, the easier we can refute it, the better.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 23:21 That's where my head is at. I don't want there to be any opportunity for a narrative to emerge or continue that says, like, you know, open telemetry just has bad performance.
So…
**Trask Stalnaker (Microsoft Corporation)** 23:40 Whoa.
**John Watson** 23:41 I feel like the… I feel like most of the times when we've… in the past few years, when we've seen Complaints about… Performance has always been memory.
Or someone just, like, running benchmarks, which don't end up meaning anything in the real world.
So… but this is fine, I don't have a problem with this at all. Do we know if this has any memory impact?
Any allocation impact?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:06 All of our metrics allocate zero on the record path, and allocate Basically nothing on the collect path as well, so we're quite proud of that.
**John Watson** 24:18 And this doesn't change… this doesn't change any of that.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:21 No.
**John Watson** 24:22 Cool.
**Trask Stalnaker (Microsoft Corporation)** 24:32 Cool, thanks for sticking with this one, Jack. It seems like a good… spot. Seems like it's in a good spot from the numbers, at least.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:43 Well, I'll be happy to put it to rest.
**Trask Stalnaker (Microsoft Corporation)** 24:53 Alright, speaking of micrometer…
**Jason Plumb** 24:58 Yeah, only because we… we were talking about it earlier, and it sparked this thought about this issue, which goes way back.
**Trask Stalnaker (Microsoft Corporation)** 25:05 Yeah.
**Jason Plumb** 25:06 And it's the third most popular issue.
So other metric systems, which will go unnamed, have these annotations that you can slap on stuff to get… telemetry.
And so, I took a stab at counted.
I have a couple of questions about it, you know, this is… like, I've been going back and forth with Copilot on this, but, like, there was something that was brought up about, bridging that I couldn't reproduce, and… maybe experts can help me understand how that works, or if it's a real problem. And then I also had a question about using reflection, I think.
**Trask Stalnaker (Microsoft Corporation)** 25:55 Yeah, this didn't… I think it might have been off.
off on this, I don't really understand it, but I think I had… yeah.
**Jason Plumb** 26:05 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 26:12 And you, you've… Certainly seen and looked over the PR that,
**Jason Plumb** 26:23 A long time ago, right? The closed one?
**Trask Stalnaker (Microsoft Corporation)** 26:26 Yeah…
**Jason Plumb** 26:27 Yeah… I mean, I… yeah, not thoroughly, but yes.
**Trask Stalnaker (Microsoft Corporation)** 26:32 Okay. Yeah, take a look at that one, because, We had… I don't know which one it is, but… Because we had spent a… Decent… not this one,
**Jason Plumb** 26:49 And just for some additional context, like, this was very much user-driven, like, we have users that want to measure internal areas without creating traces for it, or spans.
So…
**Trask Stalnaker (Microsoft Corporation)** 27:02 Oh yeah, it's a good feature. Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:06 That's an overdue feature.
**Jason Plumb** 27:08 Yup.
**Trask Stalnaker (Microsoft Corporation)** 27:09 Here, this one, 177 hidden items. So we had a quite… I had quite a lot of discussion on this PR…
**Jason Plumb** 27:18 Okay.
**Trask Stalnaker (Microsoft Corporation)** 27:19 So just… I haven't looked at your PR yet, Probably won't get to it until after. I know. I know. Yeah.
**Jason Plumb** 27:32 The next.
I only brought it up because micrometer was mentioned earlier, and it got me thinking about it, but yeah. If anyone has cycles, and I understand, like, there's plenty of other stuff going on right now, so…
**Trask Stalnaker (Microsoft Corporation)** 27:45 Yeah, but thanks for looking at it, because it really is, I agree, it's an overdue feature.
**Jason Plumb** 27:54 Cool.
**Trask Stalnaker (Microsoft Corporation)** 27:59 Sylvain…
**Sylvain Juge (Elastic)** 28:02 Yes.
Okay, so… In parallel also, I started adding, like, weather validation for JMX metrics, and one of the goals was to say, by default, all stable metrics should be enabled and captured.
So, for example, once we officially mark the Tomcat JMix metrics as stable, they should be automatically captured by default by the agent, or by, like, JMIX scraper.
And in order to, like, allow this, I decided to maybe take a shortcut. So instead of trying to complicate the… YAML definition, and to add a stability in it, which would duplicate the, what we have in the weather registry format. I decided to just split the YAML in two parts.
And, only load all the defaults, That have, like, this stable suffix.
And, this is a multi-steps process, because we have, it's being used in Jameel Scraper, so this part is only implementing, like, parts of the feature, and then later it will, like, enable it by default.
And so, this is mostly, like, a request for comments on this Pierre and for the general approach, and I was wondering, like, given the, like, recent discussion about, like, include and exclude.
If it would be maybe simpler to have, instead of splitting the files and doing some complex stuff, having a list of, like, list of metrics to include by default and to exclude by default.
**Trask Stalnaker (Microsoft Corporation)** 29:50 So, if we did, would that be a list… Would that be per GEMX module?
**Sylvain Juge (Elastic)** 30:03 Maybe, yes. So, yeah, so ideally, so in the registry format, we can define stability on each metric, and ideally, we should be able to do the same for every metric.
**Trask Stalnaker (Microsoft Corporation)** 30:17 Oh… Yeah, check what I ended up with for the JFR.
Cause I… I think it might be a little bit similar to this, and so I had kind of struggled with how to… Handle the JFR metrics, which are… off.
By default… Yeah, and we had other mechanisms, but I did end up liking that include, exclude It still is off by default, but you can… You don't have to… I guess you don't have to enable the module itself, and maybe that's where that could be leveraged for JMX, is that some of the modules just… their default is none, and some of them can have default all.
And then users could opt in by doing included star… I don't know.
**Sylvain Juge (Elastic)** 31:37 Because, like, the challenge here is, like, if we, like, get all the… even just metrics for Tomcats, we maybe have a dozen, which means the list will get very long very quickly. So, it means asking users to deal with such a very long configuration option could be tricky.
**Trask Stalnaker (Microsoft Corporation)** 32:00 Why… Why not just all on or all off? All on for stable and all off for… Experimental.
**Sylvain Juge (Elastic)** 32:10 Yes, that's more or less what I suggest, is just have a Boolean option, where We, like, by default, all stable metrics should be enabled.
And always produced.
And then we toggle only the unstable ones.
**Trask Stalnaker (Microsoft Corporation)** 32:56 Alright, anyone else have thoughts about this one?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 33:00 So… I was… I was listening a little bit, but I… I guess I might have missed a bit about, is this filter happening at the individual metric level, or at, like, sort of the system level?
**Sylvain Juge (Elastic)** 33:14 No, in fact, like, right now, we have, like, a single YAML file per system.
And so, it would require, like, to split each YAML file between, like, the stable and unstable metrics. And so, when you select… you enable the unstable matrix, you just load the two files, and when you only get the stable ones, you only get the first one.
But when you enable… so currently, for example, if in JMixcraper you enable JVM metrics.
you will have, like, both stable and unstable. So, when you enable by system.
it means you will get both stable and unstable metrics, but when you use this auto feature, and, with only stable metrics, you will only get the stable JVM matrix.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 34:01 And do… can users easily modify the contents of those YAML files themselves, or are those sort of, like, pre-canned and bundled and…
**Sylvain Juge (Elastic)** 34:10 They are bundled in the agent, but they can easily, like, duplicate and build their own.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 34:16 Yeah.
Yeah, I think this sounds like an attempt to make the common case easier.
Which is… which is a good thing to do.
Make the common case easy, make the uncommon case possible.
**Trask Stalnaker (Microsoft Corporation)** 34:52 Cool, I'll try to do it some… But, Sylvain, I agree, it's a kind of tricky modeling, after being lost in the include-exclude for the JFR for a while.
**Sylvain Juge (Elastic)** 35:08 Yeah, thanks.
**Trask Stalnaker (Microsoft Corporation)** 35:12 And it's tough when there's, like, a split default that we want, kind of similar to that micrometer.
Discussion earlier, where we would like to exclude A fixed set, by default.
But then still, maybe give people, users, Easy ways to enable…
**Sylvain Juge (Elastic)** 35:39 So, once the feature is complete, like in JME Scraper, for example, it means you could get rid of the target system and just capture stable metrics, or even opt in for unstable metrics, and whatever metric is available, you would get it.
**Trask Stalnaker (Microsoft Corporation)** 35:54 Yeah, and I did end up, like… some… one thing I liked about this, which I think could carry over there, is the include-excludes being based on the metric names themselves.
Compared to, like, inventing module names for them.
Like, it seems very natural for users to see what metrics are omitted, and… It… Kinda allows them to group maybe more… Fine-grained than, like, at the whole module.
With, like, CPU ones…
**Sylvain Juge (Elastic)** 36:34 Yes, and especially because, like, those metrics should be namespaced, so… It's more or less the same as the target system.
**Trask Stalnaker (Microsoft Corporation)** 36:41 Yeah.
Cool.
J…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 36:54 Yeah, just… this is quick, but a while back, I had raised the idea of having kind of a kitchen sink generation of the declarative config. If you go into the files change and open up the… Yeah, that one right there.
So it's generating… basically, it goes through, takes all the metadata, and it assembles it into a single tree, and it… if it has a default value, it will display the default value. If you go down to, like, the pier.
We have, like, some of them are structured properties, And so we render out the example as well, so people can see what the format should look like. And then I hooked this up into a smoke test to… to basically validate that the structure is correct. And I actually found two issues with some of the the stuff we were doing, so I have a separate PR, with that as well, but yeah, essentially, we were using the, the sanitize query parameters. We had, like, a development suffix to it, and that causes the, The file to not be used, because it doesn't parse it correctly.
**Trask Stalnaker (Microsoft Corporation)** 38:19 So, yeah, what I… Oh, good, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 38:22 On the development suffix, everything that the agent does with this is working through, like, declarative config properties, right?
So if we… so if we can make the lookup smart enough to recognize the presence or lack of presence of the suffixes, then that would kind of solve that problem seamlessly, right?
**Trask Stalnaker (Microsoft Corporation)** 38:50 My first question, Jay, which one is correct?
Is it true?
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 38:55 Yeah, so this one's incorrect. So right now, this… this is… this requires the other one to be merged first, and then this will be correct. So in the other PR, I'm actually fixing it, because it was a little bit more, like, we actually have it outside of the metadata files, too. Like, if you look at the files changed there.
**Trask Stalnaker (Microsoft Corporation)** 39:13 So, sensitive query parameters is not a development property?
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 39:19 Right, it's under the experimental instrumentation Leaf.
Or a branch, but it's not… it doesn't have a development suffix.
**Trask Stalnaker (Microsoft Corporation)** 39:29 Okay, okay.
And so, then to Jack's question… To Jack's question, I think, Jack, yeah, so this would… With the… with your proposal.
I think this would not have… this would have worked.
The slash development would have automatically fallen… back to… Non-development, or fallen forward to non-development.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:04 Yeah.
So that seems like a good thing to do.
Although, I think there continues to be some questions about whether these suffixes are a good idea at all. Like we talked about in the last Java SIG meeting, I think they're a good idea, and you know, Diego from the Python group, you know, reached out to me again and was like, can we talk about this? I really don't think we should do this.
And I was like, well, I do, so, we need more opinions.
**Trask Stalnaker (Microsoft Corporation)** 40:39 Yeah, yeah, sorry, I never, replied on that. It might be a good spec meeting topic.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:46 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 40:48 To get… Right.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:50 What I was thinking about is, like, if it's too inconvenient for you as a language to sort of accommodate these suffixes, just because the tooling for generating code from JSON schema is too impractical to, like, you know, hand roll or customize or however you would need to do it. It could be an option to… for a language to not support experimental or development properties at all.
And that wouldn't be such a bad thing. Like, say if Python says, hey, we support declarative config and only stable properties. Then, you know, essentially that is a further incentive or forcing function to drive things towards stability, which is what we want.
So… That might be part of my argument. Hey, if it's too inconvenient, don't do it, and Let's stabilize these properties sooner.
**Trask Stalnaker (Microsoft Corporation)** 41:52 Jay, while we're on… this. What happened here? What's this?
What did I do?
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 42:02 I think we… We changed it at some point, and I think it was just in the declarative config metadata.
Like, the declarative name.
So, I don't think there's any actual… Code implications here, it's just a metadata fix.
I think.
**Trask Stalnaker (Microsoft Corporation)** 42:21 Okay…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 42:23 Actually, no, actually, because I did have to add something to the bridge, too.
**Trask Stalnaker (Microsoft Corporation)** 42:27 Because I think this is the… I thought this was the standard… SemComp… oh, I see.
But… yeah… Oh, I see, and we're mapping it back, so we're saying this is what we have in declarative config.
But this, it maps to this, like, system property or environment variable.
Because I think that is the official…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 43:08 To drive it backwards.
**Trask Stalnaker (Microsoft Corporation)** 43:11 Well, so this is the official semantic invention environment variable.
But I think you're right, when we did the declarative config, in declarative Config.
we had to find a place for it, and I think we did… this.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:39 E… yes.
General… I'm just double-checking the name of that, yeah.
That's correct.
**Trask Stalnaker (Microsoft Corporation)** 43:52 Directly under General.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:54 Yeah, I'll send the link over.
**Trask Stalnaker (Microsoft Corporation)** 43:56 to build.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:57 the option.
**Trask Stalnaker (Microsoft Corporation)** 43:57 list. Okay.
So it's not… So it's not scoped to semantic conventions.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:08 Everything under general instrumentation is scoped to semantic conventions. The second link that I sent over. Sorry, I sent over, too.
So, there's a property in here, stability opt-in list.
**Trask Stalnaker (Microsoft Corporation)** 44:24 Okay, and this was sort of the backwards compatibility with… That guy.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 44:31 Right. The declarative config version of this is, like, you specify your preference at a per-domain level, and this is, like, you know, for compatibility with that environment variable.
**Trask Stalnaker (Microsoft Corporation)** 44:57 So… in the… I don't know how we deal with that, Jay, the, the mappings… Because this is still… we don't want to deprecate… that… from an… Environmental… environment variable perspective.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 45:21 Red, I don't think we do…
**Trask Stalnaker (Microsoft Corporation)** 45:24 Okay.
Oh, I see, we just don't… we just don't dock it in the metadata… Because the metadata is… Documenting just the declarative config name.
Which is fine.
I mean, makes sense.
Deprecated declarative names…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 45:53 This is just a… I have, like, a test that runs through all of them, and so this was just catching so we could… so I could update them all.
**Trask Stalnaker (Microsoft Corporation)** 46:12 Okay, okay. Makes sense to me now.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 46:21 So it is showing the right one, we do want it to be the general.stability opt-in list.
**Trask Stalnaker (Microsoft Corporation)** 46:28 Yeah.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 46:28 The documented way.
**Trask Stalnaker (Microsoft Corporation)** 46:30 Well, the declarative config way.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 46:34 Right, yeah, that's what I mean, yes.
**Trask Stalnaker (Microsoft Corporation)** 46:35 Yeah. Yeah.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 46:37 Yeah, so the name there, this allows us to kind of have the same configuration with differing names and types, but still kind of be considered the same thing. So the name being the otel.sumconstability.optin, that's still referring to the environment variable.
Definition.
**Trask Stalnaker (Microsoft Corporation)** 46:58 Yeah, and so do you reverse map that in the… maybe, like, in the Explorer, or somewhere?
Reverse map this back to the environment variable.
That you would set?
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 47:12 This… this maps it. This… option here.
Maybe I'm misunderstanding what you're asking.
**Trask Stalnaker (Microsoft Corporation)** 47:19 Oh, the name…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 47:21 Yes.
**Trask Stalnaker (Microsoft Corporation)** 47:21 this is… oh, I missed this.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 47:24 Yeah, that should be more explicit, like, maybe we should call it, you know, property name or something, but, we had introduced that before we introduced the declarative kind of fork for the.
**Trask Stalnaker (Microsoft Corporation)** 47:34 Right.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 47:34 Okay.
**Trask Stalnaker (Microsoft Corporation)** 47:35 So this is the flat name.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 47:37 Exactly, yup, that's the… yeah.
**Trask Stalnaker (Microsoft Corporation)** 47:41 Got it.
Cool, thanks.
Alright, anything else anyone wants to chat about?
Cool, then!
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:07 Alright, nice to see everyone.
Deal. Take care.
**Pranav Sharma (Google LLC)** 48:11 That's…
