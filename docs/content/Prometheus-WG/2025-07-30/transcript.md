SIG: Prometheus WG
Date: 2025-07-30
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Juraj Michalek** 01:17 Maybe.
**krajo Krajcsovits** 01:41 All right.
**Arthur Silva Sens** 02:48 Hello!
**Juraj Michalek** 02:54 Hey!
**Arthur Silva Sens** 03:03 Is David joining today? Probably not right?
**Juraj Michalek** 03:06 Is he already out again, or.
**Arthur Silva Sens** 03:09 Yeah, he's on Pto, I think.
**Owen Williams (he/she)** 03:11 His own Pto. But he keeps popping up in threads anyway.
**Arthur Silva Sens** 03:15 Yeah, there's Google folks like Partek as well on Pto, and always online.
**Juraj Michalek** 03:24 Well, sometimes you need the break from the kids, I guess.
**Arthur Silva Sens** 03:29 Yes, alright, I'll I'll start anyway.
So there is a
within the collector, Sig. There is a group that is working on stabilizing the collector like doing a release
called one dot 0. And there is a set of things that they they want to promise that won't break in the future.
And one of those things are the metrics that the collector emits.
They've given me some feedback that
metrics are changing all the time.
Sometimes it is kind of of our fault. The things we're doing in the translate Otlp translator package. But it's not only on us to be honest. There are some random Prs
from some random, like 1st time contributor that
accidentally changes the metric name, and nobody notices.
So one thing that they want to have before calling the collector. One dot 0 is some kind of testing platform that asserts that
a Pr doesn't change a metric name.
How to build this platform. How this platform looks like that's open to us.
We can come up with whatever we feel like it as long as it meets the requirements
the issue is there in the meeting agenda? We have tons of ideas.
but if they are all very blurry, and I don't really know how to
get all these ideas into like a concrete project?
Does anyone want to take a look, read a little bit more, share some opinions.
**Jonathan (jojo)** 05:35 What is this? The collector that you're talking about?
**Arthur Silva Sens** 05:41 The open telemetry. Collect the the binary, either the the tool that collects
matrix transforms into something else and exports.
I know you worked in a in a receiver, right
receiver is a component that receives metrics in a certain format.
The collector is this pipeline that bundles together.
**Jonathan (jojo)** 06:08 Okay.
**Arthur Silva Sens** 06:09 And exporters.
**Jonathan (jojo)** 06:11 But it's just related to the version one.
**Arthur Silva Sens** 06:15 Oh, the version version one is not
I. We are not in version one yet. We are 0 dot something.
But to release something called one dot 0. We want the metric names to be stable.
**Juraj Michalek** 06:31 I would like that very much. Pretty. Please.
**Arthur Silva Sens** 06:34 Yes, air crier.
**krajo Krajcsovits** 06:39 So this issue is all about, you know, updating Prometheus.
and I guess the client go long.
But I'm trying to understand
which which metrics are we talking about the metrics that
Tangolang, or the promitous receiver image, or or the collector in in general? Because the the
the metrics that the collector itself defines
will depend on this versioning for sure. But, like the promise receiver, isn't that Beta?
Something like.
**Arthur Silva Sens** 07:17 Yeah, it's not the metrics that the collector ingest is the metrics that the collector itself exposes.
**krajo Krajcsovits** 07:24 I, I know, but but which which ones like you can have metrics.
So yeah, I'm trying to understand the scope a little better.
**Arthur Silva Sens** 07:35 Okay. So imagine.
imagine a collector that has a Otlp receiver and Otlp exporter. The Prometus components are not even there.
So the Ltlp data comes in. Ltlp, data goes out and there are metrics that measures data throughput data and ingestion rate CPU usage, memory usage.
Those are metrics that aren't about the collector itself.
and they are instrumented using the the hotel. Go SDK,
this go SDK uses its own premise exporter module, so it exposes in the premise format.
and from version to version those those metrics are are changing like there are new suffixes. There are things getting duplicated.
and these are the methods that they cannot change.
**krajo Krajcsovits** 08:29 I, see.
**Owen Williams (he/she)** 08:33 So is the request that the
hotel metrics not change? Or is the request that the Prometheus translated metrics don't change.
**Arthur Silva Sens** 08:45 The metrics emitted by the collector.
**Owen Williams (he/she)** 08:49 The but.
**Arthur Silva Sens** 08:52 Is the open telemetry. Metrics have not ever broken the things that have been breaking is the Prometheus translations of those metrics, so.
**Owen Williams (he/she)** 09:02 Is this a chicken and egg thing, where they think everything's changed because everything's going through the Prometheus exporter.
**Arthur Silva Sens** 09:10 But that's not actually.
**Owen Williams (he/she)** 09:12 Like it's it drinking?
They're.
**Arthur Silva Sens** 09:15 Actually, we, we are receiving reports that some dashboards
are getting empty after they update a collector version.
**Juraj Michalek** 09:25 Yeah. But part of that was probably at least one in my experience. At least one of those breakages was exactly the auto to the beauty of migration where the default?
Yeah.
right? And so suddenly, you like, I don't remember which change was it? But it was basically with the suffixes. Suddenly you got them or didn't. So yeah, your panel is empty, but it's it's just the suffix changed and.
**Arthur Silva Sens** 09:48 Yeah.
**Juraj Michalek** 09:48 Yeah, that change for the metric name.
**Arthur Silva Sens** 09:50 I I, the Ltlp translator migration could can be a cause, but they are more worried about the symptom like they. They care how the metrics look like whatever we are we are doing on the behind the curtains. They don't really care.
**Owen Williams (he/she)** 10:05 Right. And that. And that's my point, though, is that they're talking about. It's the Prometheus translation stuff they're talking about. It's not the like the hotel metrics have not changed like, Oh, you know, it's still got dots in it, and it's still got type in unit metadata in the struct that it's making. What they're talking about is the stability of the translation to Prometheus metrics that is unstable.
I just wanna make sure.
**Arthur Silva Sens** 10:28 Yeah, the the how it looks like in the slash metrics endpoint. You're correct. Yeah.
**Owen Williams (he/she)** 10:32 Exactly. Yeah, yeah, okay, cause like, it's because those are different. Yeah, those are different things. Like, yeah, if we if we test, you know you go through all the code, and you find all the places that metrics are created. And you can say, is this stable? And that's fine.
If if the issue, though, is that? And so that's that's 1 thing. But then, if the issue is that the translation is unstable
that should be solvable just with unit tests. And we just need to make sure our test coverage is complete. And we have been adding as we've been having problems. But it should be impossible to. You know it should be impossible to have a metric that, when translated to Prometheus is unstable. If our unit test is good, there's no need for an end to end test. It's just is our unit test coverage complete.
**Arthur Silva Sens** 11:23 It happened in in the past as well that somebody thought it was good good idea to change a metric name, because
I don't know it was not clear to them.
**Owen Williams (he/she)** 11:34 So that's a separate problem. And this and that, I totally.
**Arthur Silva Sens** 11:37 They also, they also want to fight this.
**Owen Williams (he/she)** 11:39 Yeah. So okay, so then, this is where we have the issue where the collector exposes a metric. That is something dot seconds with the type seconds. And so when you go through the code path of translation, you end up with a doubled seconds, underscore seconds, because they already put the unit name in the metric name, despite that being against the semantic convention. So now that's talking about.
you know, they they do want the stability of the Otel metrics, in which case Prometheus is not even a part of that
but you don't even need to worry about the 3.
**Arthur Silva Sens** 12:15 Can solve both in the same project. I think.
**Owen Williams (he/she)** 12:21 Yeah, I just I. It feels like 2 separate issues that are being mashed together. So the and this is why we now have. David and I were talking about this. We have this workaround code to detect
if the suffix already exists, and therefore don't append it. And so we had to write this extra code.
and that's not a matter of the Promethe of Otlp. Translator being unstable. It's a matter of somebody wrote a metric counter to the semantic convention. So we're being asked kind of this impossible thing, which is, we want your output to be perfect, perfectly
unchanging, which I don't want to say stable. But we want unchanged output, even if you're actually writing things that conform just to the semantic convention in the spec
that would would produce a different output. So I think it's a very, that's a very hard thing to be asked to do.
And that's that's 1 reason why this is such a complicated issue, because if it was as simple as
the name, translation is wrong, well, then, that's easy. More unit tests. And if it was as simple as the metric names need to not change in Otel. Well, then, that's a simple test. But no, it's this, it's this, we want everything to be just the same, even if it's wrong, and that's what's harder.
**Arthur Silva Sens** 13:42 Yeah. But I, I think we like this group has a much better knowledge to build this kind of automation to them, even though
we are not really the
the culprits here, like they, they are not following their own spec, but we can help them follow like we have. We can. If we create an end to end test, we can
updates the art translator to not do this suffix the duplication anymore. And while we roll out
this this bump we can adjust their metrics to comply to the semantics.
and the end-to-end task will will show that making the changes to the metric while we bump the Otlp translator.
The metrics names won't change, and there's a safe, a safe upgrade to do.
**Juraj Michalek** 14:33 If- if
nothing else, like a very naive implementation, I guess, would be just running the collector directly with some configuration.
push some data through it, and then just do
rerun the same with the upgraded version. And then just do basically a prompt kill query in a Prometheus. That's like list. All the metric names from version a list, all the metrics name from version B, and if, like, if some are missing from the older version in your new version, like.
yeah, something with rogue.
**Arthur Silva Sens** 15:04 They? They have a a Pr almost ready with something very similar. They implemented
somebody just run a collector. They he copied the text that he got.
**Juraj Michalek** 15:17 And then put that text in the.
**Arthur Silva Sens** 15:20 And end-to-end test.
But I I think this is very fragile as well, and doesn't scale.
**Juraj Michalek** 15:29 I think the crux is like.
are we talking collector or collector contribut right? I think collector at least doesn't have that many components. But if if the scope is even collector contribut.
then anything that involves like running it and expecting these metrics to come
have fun with couple 100 components trying to like push data through them. So they actually expose all the metrics. Right?
So that's that's, I guess. My question, like, what what is the scope of this is this just open telemetry collector, or this is also open telemetry, collector, contribut.
**Arthur Silva Sens** 16:02 It's all components that are declared stable.
**Juraj Michalek** 16:07 Any idea how many there are.
**Arthur Silva Sens** 16:10 No, it doesn't really matter. Like we, the automation should be intelligent enough to look at the components, look at the stability.
and then add this, this this component to the to the framework.
**krajo Krajcsovits** 16:27 But
some metrics could be having dynamic labels. So unless you do something specific, they never show up. So I wonder if
I kind of agree with Owen on this, that
we should have the right unit testing Prometheus itself, or or client go along more like
to ensure this, because otherwise you're like the way to do this to me would be to write the unit test, basically in open territory collector
that has a a good list of kind of metrics that they use and then
write. You know one, observe one value into each in the test, and then do
collect the output, not even that's text, but
more like the Dto or or Protobuff, or whatever to be complete, and then compare
with the with the golden record.
because I feel like trying to
trigger all the possible metrics in the end of that's going to be very hard like. I mean, it could give you a pretty good coverage. So I'm not saying it's it's useless, but
I don't know if you want to go that route.
**Juraj Michalek** 17:41 Yeah, I mean, my worry is exactly the same right? Like some of these components, like some of these metrics, will not show up unless you actually like, use the use the processor right?
**Arthur Silva Sens** 17:54 I I totally agree. This is not a easy project it will take a few months to complete.
I don't know. I I know that some Grafana folks want to increase their
their impact in the in open telemetry.
That could be one of one of the opportunities. But if you feel it doesn't align with your objective, that's also fine.
I'll try to look for other people as well. Maybe I maybe I'll do it. I don't know.
Yeah. But I don't see the collector group doing this because they they lack knowledge.
That's we. We lack time. They lack knowledge.
This hard to balance. Yeah.
**krajo Krajcsovits** 18:52 Yeah. By the way, I mean, I used to do.
did I? Or somebody else? I don't know. I I remember in the stuff that in a previous life we did static analysis on things like this, or or very similar things in C, plus plus where you would
take a tool that can give you access to the syntax tree of the
of the compiled thing, and you could do rules on it and detect like bad patterns, was our our
think
cause. It was like, you know, mission critical or like critical system. And and they made sure that some design factors just didn't happen because we code them in in the code by static analysis.
And you could. I don't know if that's possible with go, but you could potentially find all the calls to, you know, new
histogram deck and histogram and stuff like that, and and
and and just parse out the the information that way that would give you possibly a better
coverage than than trying to run the thing.
**Owen Williams (he/she)** 20:04 rewinding back to the act the the specific ask, Which is Collector Sig is asking for the stability of metric names generated by the hotel. Go. SDK,
if we just take that
as the specific request, then it's a much smaller issue. It has nothing to do with the collector or collector contribut.
Then it's just a we need to make sure that the otop translator is stable and correct, which we're rapidly getting to like. I think that's going to be a non issue shortly. And then the second thing is all the metrics that the hotel go SDK exposes itself. We need to make sure are stable. That's a much smaller problem than trying to figure out how to make sure every metric generated by the collector is unchanging. That's a separate.
Again, I feel like they're they're
rewinding. Even further, they're mad that their metrics broke and they're breaking for multiple reasons. One of those reasons was instability in Otlp translator. We're fixing that.
And then the other is people messing about with metrics in components. And I feel like that's not our
problem like that's, I feel like we have to fix one thing at a time.
**Arthur Silva Sens** 21:20 This is not the words that they use. It's just the words that I use to write this down like they are not asking specifically for the goal. SDK,
stability.
I they are not. They are not really mad. They understand that we are all making. We we all have different problems to solve.
They are just asking for help because they want to release Collector one dot 0. And they can't with without some kind of testing.
There's nobody mad with anyone like. It's just people asking for help.
**Owen Williams (he/she)** 21:58 Okay, that's that's helpful.
yeah. And certainly I would.
I don't want to keep breaking people's names. And again, with this issue with
we have to implement the configuration options in the go SDK asap. And so cause that's gonna
break things again. What is it? Do they have a timeframe for 1 point. Oh, that they want like yes.
**Arthur Silva Sens** 22:32 It's
It was supposed to be released in 2023.
They are 2 years delayed already.
**Juraj Michalek** 22:44 What's 1 way you're gonna change it.
**krajo Krajcsovits** 22:47 And, by the way, is there a defined or written down somewhere, like what translation they want? Or is it just the current? That's it, like, you know, underscore translation or
no underscores suffixes whatever.
**Arthur Silva Sens** 23:01 I don't think there is something like this written down.
**krajo Krajcsovits** 23:04 Okay, so basically the current, okay.
**Owen Williams (he/she)** 23:06 Opinions differ.
Go ahead.
**Juraj Michalek** 23:09 Personally think. One of the origins of the whole issue is basically what happened was like people upgraded auto collector. And then their dashboards and metrics, for it just stopped working because they broke things.
And then, yeah, we we like had to debug this. Personally, we don't know times. And it took us a while to even figure out like why, it broke.
**Arthur Silva Sens** 23:30 I think they
they are okay with us, breaking a few more times until we get to 1 1 dot 0. But once it's 1 dot 0. They absolutely cannot change anymore. And and if they do, then it's this needs to be blocked by Ci, somehow.
**Owen Williams (he/she)** 23:49 Got it.
So for what it's worth. My proposal for the default is by default. The Prometheus exporter should output metrics in Prometheus format, which is underscores with suffixes. And then, if people want the native version, they can update to native
David actually disagrees and thinks like, Oh, we should just be using Utfa by default. And I don't think that's practical, especially not without typing unit metadata. So I think, for now it makes sense that the thing that, says Prometheus on the tin should do Prometheus by default, and you give people the option to do otherwise.
That's not the default now, so it will break again. Yeah.
**Juraj Michalek** 24:31 Yeah.
**Owen Williams (he/she)** 24:33 1 1 other way to do this is to start with having a little E to E thing in the
SDK,
because that's a smaller surface area, and then see if that type of pattern because the collector doesn't it?
The modules are so weird, like the go module. Each folder has its own. Go. Module, you know. Go, MoD, file, and it's like it's very complicated. It's a humongous, sprawling repo.
I can imagine requiring people to. If you have a if you have a stable component, you need to add some
dummy code to the top of you know every you know when you declare a metric that you do something that somehow registers it with our test, and if you don't register it with the test, then you're not stable or something like that like I think you could. I think you could have some requirements to make it easier rather than trying to like.
spin up and hope for the best.
**Arthur Silva Sens** 25:38 I'm not sure if we if it's productive discussing this any more today.
But I think we got some ideas.
I'll I'll come back to them. I share what we what we, what we think.
I'll see if we can.
if can, spin something up, or if if we just tell them, hey? We cannot do this, or I don't know how many time, how much time.
and see how they respond.
**Juraj Michalek** 26:06 Is there last question for me? Is there also, like an estimate when they want to do now the release
**Arthur Silva Sens** 26:14 I. They want to do asap. But like
asap without a date is just.
they don't have a they don't have a date anymore.
**Owen Williams (he/she)** 26:32 Okay, I just, I rewrote your initial. Ask to try to make it more accurate to my understanding. Do you? Does this look right? Cause. I wanna make sure we're agreeing what the problem is. And so.
**Arthur Silva Sens** 26:46 Yeah.
**Owen Williams (he/she)** 26:46 They're asking for this.
**Arthur Silva Sens** 26:47 Correct.
**Owen Williams (he/she)** 26:48 Yeah, because it's the stability of the Prometheus. Translated names generated by all hotel collector components.
because once they release 1.0, they cannot have names change.
**Arthur Silva Sens** 27:02 Looks great. Thank you.
**Owen Williams (he/she)** 27:04 Okay. Yep.
Cool.
**Arthur Silva Sens** 27:10 Alright. Next topic is more of a Fyi
Prometheus, release 3 dot 5 renovate. Open a Pr.
And it doesn't pass like
just letting people know if somebody has the time to just take a look at the Ci failure and fix.
That would be nice.
**krajo Krajcsovits** 27:35 Next week I should have time, because I'm finishing up a big
Pr. In in promitives, and I'm going to send it for review, so either
Friday or or early next week I can. I can take a look.
**Arthur Silva Sens** 27:51 Thank you. Looks good.
You right?
**Juraj Michalek** 27:57 And I guess then there's my topic. So
the remote way to support in the Prometheus remote exporter is
getting into a decent position right now. I guess there's there's
We're like, I'm missing support for one metric type. I have a draft pair for that. There's another Pr from Jonathan. I would like to get merged before we ask end users to start tested.
And there's still a bunch of things I want to eventually do in the to do so I guess it's it's sort of like asking for feedback like from this group, like, what are the things that you think are necessary. We need to have before we ask people to test it. One of that would be a question like, Okay, do we absolutely need to have exemplar support, for example, in the remote right. V. 2. Before we ask people to just test it.
That would be one of them. Another one would be, which I also have, like a very
draft Pr, that I don't think even the pipeline passed on it. And I will definitely need some outside view on that was also adding the config option for the translation
of the normal histograms into the native histograms with custom buckets
and potentially name billing by that by default.
I think like I'm perfectly fine going asking people to test it without the where the headlock support.
1st like one reason that was broken for years, and nobody seems to like some people ask about it. Nobody really complained that much.
And the other one it's that's gonna be also take a while to implement.
So just like, sort of, yeah, I guess to ask, is general feedback, on which of these things do you feel like are necessary before we ask people to test it.
No.
**krajo Krajcsovits** 29:53 That that was a that was a lot. I I lost a little bit of the thing, but you mentioned exempliers, and I always think that exempliers are kind of best effort in primitives, and you know how much memory you have, and in general, so
you could ask people to use it and say that exemplars are not supported, and they will be like, not mad
at you. So part is one thing that you can. You can skip on on the 1st step for sure
that you mentioned.
Missing metric type, which? What was that.
**Juraj Michalek** 30:27 So I have a draft. Pr, that's
adding the translation logic. For where this is issues turning really big.
where is it? Exponential histograms. And I definitely want to get that one merged before
before I ask people to test it. But
the yeah. So that one I definitely want to get merged. There's also one link that Jonathan was working on handle the conflicts in metrics. So those 2 are must for me before I ask anybody to test this. The rest of it is like I am willing to start like
I don't know, begging my friends in my ex companies like, hey, could you please test this for me in production? Because I changed jobs. And I now don't really have a environment with larger scale where I could test this
**krajo Krajcsovits** 31:26 Yeah. Yeah, exponential histograms. I definitely would want it, because we
said explicitly that especially the custom bucket stuff, is in remote right? 2 only. So you would want that
and the will. This
you mentioned the, you know, maybe defaulting to converting the classic histograms to native programs with custom buckets.
That would be very helpful for my testing as well. But I'm like.
**Juraj Michalek** 32:03 That's that's the thing right, like I know in Prometheus. It's not enabled by default in the hotel Endpoint. But I feel like
we. That's that's a discussion. We sort of need to finish right? We were discussing this in another Pr and decide in in the Pr. Where I added support for at least like the old way of dealing with that.
And and I guess the question is right, like.
well, one perspective is, this is like nobody's using this right now. Right? So like, if the default is different, we're not breaking anything for anybody. But then the the other thing is right, like we're coupling to migrations. We're coupling migration from Rv. One to Rv. 2. And at the same time, we're also like changing your metrics under your your feet. So it's definitely good for driving adaptation.
Not necessarily the most end user. Friendly thing. I also just wonder.
Yeah, well, like.
I have seen some data around the usage of Rv. 2 out in the wild, and they are not encouraging. So I also just wonder, like what are. And
another thing I should mention, I guess? I asked this. You have probably seen the message right? I asked this in the Cnc channel like, do we have any data on like remote right. V, 2 usage out there in general. And that ended up with basically me agreeing with Martech and one other person from the Thanos team doing an Lfx. Mentorship
in in autumn to like, finish up some of the work around Rv. 2, and hopefully drive a bit more adaptation for that.
I.
**Arthur Silva Sens** 33:37 I will like. I I'm not understanding, because I feel like you're walking around several different.
**Juraj Michalek** 33:45 Yes.
**Arthur Silva Sens** 33:45 At once.
But going back a little bit, to what do you need to release the V 2 in the collector.
**Juraj Michalek** 33:54 Sort of like the main point is to get feedback on, because I have bunch of other things in the to do list. Which of these. I guess this group feels like as must before we ask people to test it.
**Arthur Silva Sens** 34:07 Bye, implementing all the existing types counter gauge
**Juraj Michalek** 34:14 Yes, no, for that. We're just missing exponential histograms, and I have a trust. Pr. Of that.
**Arthur Silva Sens** 34:20 And the conflicts that Jonathan is doing, and I think that's that's good enough for our Alpha release. Right like this is behind a feature flag, I assume.
**Juraj Michalek** 34:30 Yes, it is.
**Arthur Silva Sens** 34:31 Okay.
**krajo Krajcsovits** 34:33 Yeah, I would also add that I wouldn't make any Cb conversion default on unless
you can also, at the same time, convert to classic historm as well.
because that's a way to to start the migration.
So you would need.
you know, options to keep the classic histograms and convert to an Hcb. At the same time for migration. So just don't don't do it. Default. Yeah.
**Juraj Michalek** 35:04 Yeah, I I can add the option for that. It's just.
I don't know, like it's it's sort of it's not doubling the data exactly. But it's definitely
increase for a time of period. You're you're sending a lot more data than you will after you like.
**krajo Krajcsovits** 35:21 So.
Oh, I I see. Yeah, I guess the other way to deal with it would be to require the server to be able to
do both, and Hcb. And also turn it back into classic as well for time.
**Juraj Michalek** 35:38 I'll
I'll I'll raise the Pr. Where I added the config option to like enable the translation. And that's a conversation we can have in that. Pr, yeah, like, how how we want to handle it.
**Arthur Silva Sens** 35:50 Hey? Since since this this exporter handles both v. 1 and v. 2. What do you think of having like a config? Option
to that only is only about V. 2, like something like.
**Juraj Michalek** 36:06 Oh, yeah.
**Arthur Silva Sens** 36:06 R. 2, our W. 2 options, and it's a like a struct has
enables custom buckets conversion enable. I don't know what else.
**Juraj Michalek** 36:19 It. It doesn't have to be its own script, because we already, for example, have the precedent of like enable sending metadata right is in every one, and in Rv. 2 it doesn't do anything, because it will always send the metadata and I don't necessarily think there's gonna be. I hope there's not gonna be. If it becomes too many config options. I'll I'll make it. And it's it's a separate script. But definitely the the plan was to call out, like the native histogram buckets that would only affect Rv. 2. And there would be a call out about that in the readme.
**Arthur Silva Sens** 36:48 We. We could also have a a block for only v. 1. Config options.
**Juraj Michalek** 36:54 That's the cracks right like the moment you like.
add a separate book. That's like we run, unless you keep supporting the existing configuration. It's a breaking change, and I think we can avoid those ideally so.
**Arthur Silva Sens** 37:07 But yeah, yeah, I I totally agree. We can avoid, if like, let's avoid, if we can. But if not like, we are still allowed to do making changes. The component is not stable.
**Juraj Michalek** 37:18 Yeah, yeah, I know that I just prefer not to. And I don't think I don't think at least, for now it's necessary.
**Arthur Silva Sens** 37:25 Alright. So for Alpha you have, you have. What do you want? Right? Implement explanation conflicts, and we can announce that this is ready for like.
**Juraj Michalek** 37:36 Usage in very yeah for testing, not production.
And see if anybody actually does test it. And if not, then I can go around and ask some people if they're willing to test it for me.
That's it for me. Thanks.
**Arthur Silva Sens** 37:54 Alright I just wanted to share another thing Bartek and Jonathan they are doing.
They will also do a Lfx mentorship. Jonathan is going from ment to mentored.
and they will work on native summaries.
This is like literally this, a very similar project from classic Instagrams to native Instagrams. But now for swimmers.
I don't.
Being very honest, Jonathan. I don't think we'll in 3 months you'll be able to do something very complete.
But you can definitely write a very good proposal.
and I think that's good enough.
**Juraj Michalek** 38:36 Yeah, I think at least like in in my experience, is like.
it's not the end of the world. Right? Like, I started the Rv. Work last last of them, and I'm still not finished with it.
**Arthur Silva Sens** 38:48 Yeah, yeah, that's all. Okay.
**Jonathan (jojo)** 38:52 Bartek is doing the whole hard job. I'm just in trying to help.
**Juraj Michalek** 38:58 He's he's doing 2 of them. So that's gonna be also interesting for him.
But he likes to have a lot on his plate. I guess.
**Arthur Silva Sens** 39:07 Yeah.
Our once native summaries gets more concrete, they'll probably
put that in a remote right to be 2 dot 1, 2 dot 2. I don't know.
This will also probably affect queries storage, etc.
**krajo Krajcsovits** 39:29 Wait! That's what I was going to ask. Is this about the collector side and remote right only? Or is this Prometus as well.
**Arthur Silva Sens** 39:35 This is a Prometus project that affects opentelemetry, but it is. It is a Prometus project.
**krajo Krajcsovits** 39:42 Huh?
Cause. Yeah, i i i agree that it would be nice to get to design Doc.
in such a project at first, st because
the current latest program code is like.
just for a little bit of historical perspective. You know, the 1st idea of that in in protonators was that? Oh, we are going to use like interfaces and and dynamic types
to handle, you know, float versus native program, and everything will be very nice and easy to maintain.
and that, and then go interfaces. And and that kind of type
what is it called? I'm I'm blanking on the name. So like, basically, those dynamic
pipes turn out to be so slow that they destroyed the float performance. So that's why you have in permitives
in like most of the code looks like
that. You have a switch where you deal with floats in one branch, and then integer histograms in another branch, and then the the 3rd branch is the float date histograms.
and that's
like it would be very good to refactor that to be a bit simpler, you know, still keep the float performance, but like not have so many branches before adding new types.
So I will try to find the issue. I know that there's a
we just copy this issue about the type handling in general.
In Prometus, which is that
the reality is even worse, that you have a bunch of branches. But there's also those are the optimization, memory optimization. And that made everything even more complicated. And it would be nice to refactor and put these things into order before adding a new type. Ideally.
**Arthur Silva Sens** 41:55 Like the the mentorship process already kicked off
so it will start like next month.
Not sure if this is something that they can work on in one month. But that's why I'm saying that this project will probably the outcome of the mentorship will probably be a design, Doc, and not really
code contribution.
And yeah, if the design, Doc.
like this what you just shared is probably something that they need to take in into account or take our notes, Jonathan.
but I don't think they will actually refactor that.
**Jonathan (jojo)** 42:36 I don't know if under, if I understand a hundred percent, Carlo.
But the problem is
the performance. The performance is affected because we have multiple branches to deal with with different types is that the problem.
**krajo Krajcsovits** 42:53 No, the problem is that we have multiple branches. And the code looks like crap. So it's really hard to maintain, because it's it looks. There's a lot of branching. And you would think that you could just write, you know.
code using interfaces and and dynamic types. And then it would be simpler because you would call, for example, Ed and Ed would figure out what to do, based on the types. But no, we need to do
lots of branching, because the dynamic types are just too slow in go
and you can't have nice things, basically. And the.
But there, there should be some kind of way to make this nicer, because the last thing we want is add, you know, a 4th or 5th branch everywhere on top of float integer histogram data, histogram.
It would be good to have like float. And then.
you know, complex types somehow deal with it that way.
Did that make sense.
**Jonathan (jojo)** 44:03 Yeah, yeah.
**Arthur Silva Sens** 44:10 You. You remember, Jonathan, when you were working on the native scrums in the collector that you have.
if histogram is float, and then you have another. If if it's not.
I think this is what he's talking about.
**krajo Krajcsovits** 44:24 Yeah, exactly exactly exact.
I put the link to the issue that
is about like in general handling of samples in in promiss. I did put it into the notes.
**Jonathan (jojo)** 44:38 Nice things.
**Arthur Silva Sens** 44:56 Alright any other topics.
Okay, and see you in 2 weeks.
Bye-bye.
**krajo Krajcsovits** 45:12 Oh, man!
