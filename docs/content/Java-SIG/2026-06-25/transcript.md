SIG: Java SIG
Date: 2026-06-25
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Robert Niedziela** 03:43 Hello.
**John Watson** 04:16 Gask, what are you doing losing power in the summer?
**Trask** 04:20 Right? That's what I said.
**John Watson** 04:22 And on a nice, cool day, it's not even, like, super hot.
**Trask** 04:25 Hot, or windy, or…
**John Watson** 04:28 Yeah, weird.
**Trask** 04:30 Somebody probably… And the car to a… yeah, the telephone pole.
Yeah, supposedly, like, 200 houses. Also, like, not a tiny little one.
**John Watson** 04:55 Isn't 200 houses, like, your whole neighborhood, though?
**Trask** 04:59 More, yeah.
Oh, good, you should… you… you're here, Jack.
Oh, but we can't hear you.
**Jack Berg** 06:25 Just because I have the majority of the topics on the agenda, or…
**Trask** 06:29 No, because I, I have no power, and so I'm just on my phone.
**Jack Berg** 06:35 Oh, okay, so I can drive to the meeting.
**Trask** 06:36 Hoping for you to drive, yeah.
**Jack Berg** 06:39 Yeah, no problem.
Your power went out, did you have storms roll through, or something else?
**Trask** 06:46 No, no, I don't know why. It makes no sense. Just woke up and there was a power outage.
**Jack Berg** 06:54 It's too bad.
**Trask** 06:57 Shouldn't take them long this time of year, that, like, there's not, like, a backlog.
**Jack Berg** 07:33 Well, let's get started. The first item on our agenda is the Instrumentation V3 review.
That's a recurring topic.
What's the best way to talk about that? There's a project somewhere, right?
**Trask** 07:53 I usually pull up the issues milestone Filter by milestone on the issues.
**Jack Berg** 08:03 Okay.
I don't know if you can see the screen, Trask, or if you're purely on.
**Trask** 08:08 Yeah.
No, I can see, So, I mean, the main thing, I don't know if, let's see, is… the main thing to potentially discuss is the invoke dynamic Lori, there's the one… Are you… I must… I thought you were out this week.
Are you here?
**Lauri** 08:38 I was away half of the week.
**Trask** 08:40 Okay, welcome back.
The… Are you planning to take a look or think more about the… the 1PR?
The group… removing the group… Yup.
**Lauri** 08:58 I'm looking at it.
**Trask** 09:00 Okay, awesome.
Yeah, I think we're good. Then, I think once… I think that was the main… Thing to discuss here.
And we have a little bit more time with the, but, we're gonna do a 2.30 release still, in July, mid-July.
**Lauri** 09:31 Are we going, like, straight to 3.0, or are we trying to do some sort of 3.0 branch this time?
**Trask** 09:41 I was just thinking to go straight after 2.30.
to 3.0.
**Lauri** 09:48 Okay.
**Trask** 09:50 We'll… we'll keep the… 2.30 release branch that we can backport stuff to over time to patch that.
**Lauri** 10:01 I think one thing that, We got some complaints for the last time was that, For the 1X, we only produce those patch releases.
Although we probably should have been producing minor releases.
**Trask** 10:21 Oh, right, we added a feature?
what, at one point to it? Was that…
**Lauri** 10:27 It was basically because our workflows were, like… it was much more convenient for us to do it that way.
**Trask** 10:35 Yeah, but what… do you remember what the complaint was? Like, was it because they weren't true patch? We had, like, backported a feature?
**Lauri** 10:46 It could have been something like that.
**Trask** 10:50 Okay.
Because my… my hope, of course, is to only include, is to only do patches, like, security patches, things that are… critical.
**Lauri** 11:08 You know… We were thinking, I think.
**Trask** 11:12 Yeah… yeah.
**Lauri** 11:15 We'll probably have to do something more.
I don't know, like, maybe this release isn't as destructive as the previous one.
Maybe, maybe vendors and users are forced to pick it up.
Alright, coalesce issues.
**Trask** 11:34 Yeah. Yeah, I suspect that a lot of the People kind of got some processes and use to the breakage from 1 to 2.
So I'm hoping that the breakages from 2 to 3 will… B… People will be more familiar with how to approach that.
**Lauri** 12:03 Well, I suspect that the backends might have, like, something baked in with the old database semantic conventions, and they might not be ready for the geometry changes.
**Trask** 12:15 Yeah, definitely.
Cool. Well, we can keep that in mind if we're… I agree that if we do end up backporting features to 2X, then we should probably figure out a way to… Do I?
minor.
2.31, it's…
**Lauri** 12:47 Like, I think one thing that happened with the OneX release was that, At one point, we committed to the 2X, and And it actually took multiple months to get it out, I think.
**Trask** 13:07 Yeah, I'm hoping with the V3 preview flag that we've introduced now, that we've been able to basically do, all of the braking changes. I'm hoping that we've done pretty much all of the… or all of the braking changes besides API breakages, like, things that we can do in… Behind the flag.
will… need to be… I think need to be in 2.30.
So that, we don't have that long.
Delay between 2.30 and 3.0.
**Lauri** 13:49 Obviously, summertime is coming, so…
**Trask** 13:53 This is…
**Lauri** 13:53 It also complicate things.
**Trask** 13:55 Yeah, yeah.
Any…
**Lauri** 14:12 I guess we can move to the next topic.
**Trask** 14:17 Yeah, unless anybody has any questions about V3.
**Jack Berg** 14:28 Alright.
Let's move on. So, I saw a light agenda, and I have something I've been working on for a while, bound instrument support and open telemetry.
This was actually… I think a few people will remember. This was in, early metrics API prototypes, but was pulled because the spec, you know, didn't include it, and the spec was trying to de-scope just to get stable.
And, yeah, it's back in the spec now, in experimental fashion, and so trying to land it in OpenTelemetry Java. The basic idea is bound instruments can be used in cases where you know all of the series that you want to record data to ahead of time.
So, you know, just like you would initialize your instrument, maybe in your constructor, or at initialization time, you also initialize the series that you're going to record data to.
And, those… series have, you know, an API that looks sort of like a metric instrument, like a long counter or double counter, but you don't record attributes to them anymore, because attributes were configured at initialization time, and so it's sort of a simplified API that only has the record and the measurement value in context.
So, I had an older prototype PR8314 that went in a different direction. Instead of having new dedicated interfaces for the bound variants of these instruments.
I was actually reusing the existing interfaces, so, like, you know, bind would… bind… calling bind against a long counter would return another long counter, and, you know, that has less interface boilerplate and… you know, is appealing to some people in terms of ergonomics, but I ultimately ruled it out, and the reasons are explained here. So basically, so… I don't know if anybody cares. I can go into the reasons if anybody cares, but I'm just trying to give a.
**Trask** 16:43 Seems…
**Jack Berg** 16:43 see if.
**Trask** 16:44 It's… obvious to me that, like, it would be confusing… I mean, it would be confusing, right, that you can still call add with attributes?
That resulting down.
**Jack Berg** 16:59 It's confusing, and it's a foot gun, too, because, you know.
**Trask** 17:02 Yeah.
**Jack Berg** 17:02 The calling ad with the attributes is just, like, you know, you erode any of the performance benefits.
And… Yeah.
**Trask** 17:10 I think the kicker for me was…
**Jack Berg** 17:13 Okay, cool.
**Trask** 17:16 What was the kicker, though? Because that's the kicker to me, is the, the foot gun.
**Jack Berg** 17:20 The kicker to me is that bound instruments, I think, almost certainly want a close method, which is scoped to just, that series.
And, you can't add just, like, a close method to the general instrument.
for a particular… for, like, A series. So, like, the shape of what… adding clothes at the instrument level is still being debated at the spec level.
But the shape of what it looks like is different from the instrument level to a series. And so, you know, reusing that same API in both contexts would… would not make sense.
**John Watson** 18:01 Yeah, the unfortunate thing with this option is that, as you said, the interface bloat, but I think this is a better API and more… we'll get less users confused by the fact That you… once you have it bound, you can't… do anything else with it. So I think this is a good… I think it's a good option, even with the interface bloat.
**Jack Berg** 18:26 So we all agree on that.
From a performance standpoint, I have performance comparisons for our metric record benchmark. I have two different, sort of, sections here. One is like, hey, is there any change for unbound instruments from main to this PR? Like, you know, I'm adding some new machinery, I'm adjusting the internals of metric storage.
And, you know, I don't want to erode any of the performance of the existing cases as a result of that. And so, that's what this first drop-down explains. So, you know, main versus the PR for unbound instruments.
And, you know, just scrolling over these, all of the changes… this one, actually, I didn't notice this before. All of the changes I read as, like, within the bar of variance, normal variance, interrun variance, and… Now I need to go investigate this one. 37% performance protection and engaged. Maybe that was some sort of anomaly or something.
But yeah, I don't expect any performance, Regression on the unbound case.
more interestingly, for the… for the bound versus unbound case, so, like, you know, what's your… what's your reason to use bound instruments at all? And, the results here are… are… are interesting, because for cases with low contention.
there's a significant improvement. Like, you know, somewhere around, like, the 50% to 100% improvement in throughput. So, you know, drop the operations cost in terms of nanoseconds by half. So, if something took 10 nanoseconds before, it's taking 5 nanoseconds. That's how you can fit double the number of operations in.
So that's… that's a real improvement. But, for high contention cases, there's actually a, a reduction in performance.
And I was tracking this down, this was… this was a confusing result for me, and what it comes down to is that, bound instruments get rid of the map lookup.
But the map lookup is against a concurrent hash map, which is very well tuned. And, without that map lookup, all of those concurrent… all of those concurrent tasks are just, like, hammering the underlying accumulator, whether it's, like, a long adder, or, you know, for histograms, it's, like, a number of things that you have to increment together. And, so now you're seeing a performance regression.
In the long adder, the accumulator performance, as, like, you know, there's suddenly a lot more concurrency than there was before.
So…
**Trask** 21:18 Is that just a factor of the test, that you… with the… you were testing multiple time series, spreading that out across multiple time series, versus on the bound instrument, the test is… Just one time series.
**Jack Berg** 21:35 So… Add that?
That could be the case.
I have to, I have to look at the test harness now. Yeah, I see what you're saying.
**Trask** 21:50 Okay, cool.
**Jack Berg** 21:51 The test harness has to be set up, like, in a very specific way to, like.
Simulate the same thing for, like, an hour.
**Trask** 21:59 How's that?
**Jack Berg** 21:59 apples comparison.
Yeah.
**Trask** 22:03 So if you have 4 time series, yeah, you either need 4 bound instruments, or if it's just one bound instrument, then you can only test Compare against one time series in… E.
non-bound.
**Jack Berg** 22:19 I think… I think the thing for me is, like, if you have 128 series, because that's what this is, like, testing, and that's where we see this reduction, in the unbound and bound case, the measurements against those series should be, like.
Interleaved sort of randomly to simulate what you would actually expect, such that, like, it's not all four threads hammering the same series of the 128 all at the same time in the bound case.
**Trask** 22:47 Yeah. Yeah, yeah.
**Jack Berg** 22:50 Right, so, I gotta look at that, just the way that it's set up, so that's… maybe it's artificially pessimistic.
but, yeah.
**Trask** 23:01 I sit here thinking, like, how can removing one operation make it slower?
**Jack Berg** 23:06 I mean, that can happen, right? So, like, if the operation was acting as a sort of, like, I'm thinking of the things…
**Trask** 23:17 I can, but it's very, very unusual.
**Jack Berg** 23:21 Okay.
**Trask** 23:24 Yeah.
**Jack Berg** 23:25 You know what I'm saying? Like, you know, the meters that prevent cars from all going on the highway at the same time, they control the flow.
**Trask** 23:31 Yes.
**Jack Berg** 23:32 At a time versus, like, everybody just hammering the highway?
**Trask** 23:35 Totally.
**Jack Berg** 23:36 That's the analogy in my head.
**Trask** 23:38 That's your… I love your civil engineer brain goes to that example.
**Jack Berg** 23:47 Yeah, so…
**Trask** 23:49 of…
**Jack Berg** 23:51 If, there is still some opportunity, probably, to improve this, because, like, the… the hotspot for contention really moves, to this one place that Lori and I… Lori is actually, you know, he's been… he DM'd me a while back about this possible improvement. So, under the covers, for Delta metrics.
there's this one atomic integer that acts as a coordination point between record threads and collect threads. And every record thread has to increment it by 2, and every increment decremented by 2, and every collect thread has to increment decremented by 1. And this acts as, like, you know, a way to coordinate state and, you know, in a non-blocking way. And so that atomic integer is the… it is the hotspot. It controls the performance right now, because… and so if we can improve the concurrency performance of this, like this coordination task between recording and collect threads for Delta, then we… we will improve the throughput.
So, that's the critical path. Lori has a clever idea that I want to try implementing, or, like, you know, running through these performance tests. But, you know, I want to do that as, like, a follow-up step. I want to get, like, the shape of bound instruments sort of in place, and then incrementally improve it.
Just to limit this from becoming too big, because it already is a lot of code.
And that's all I have to say about that. Anybody's interested, please take a look.
I have the next topic as well. This one shouldn't take as long.
somebody opened a PR against our baggage encoder, and it's like a… it's like an innocuous thing. So, what's going on is our baggage parser, you know, reads through entries, and if any one of them is improperly encoded right now, it, like, throws out the whole batch.
And this change, which seems innocuous enough, is like, hey, if there's a single entry that's, like, improperly encoded, just throw out that entry. Just skip that entry and warn, instead of throwing out the whole batch.
And it seems okay. But… I wonder if it's actually, like, a good thing. I sort of reached a different conclusion than the other two approvers, Pranav and Gregor, who approved it. My interpretation was that, like, getting a baggage encoder correct is, like, kind of a simple task.
You know, there's lots of implementations of it. You probably shouldn't need to write your own, but if you do write your own, it's not that hard. And, like, skipping invalidly encoded baggage entries just sort of hides an error in your encoder.
In a way that I think it's, like, it's a little bit too forgiving. It's sort of like the difference between fail fast or fail gracefully. And I think, you know, where I landed on this is, like, fail fast because it's easy.
to fix it. Failing fast helps identify the problem in your encoder, and it incentivizes you to go fix that problem.
Just wanted to resolve it here.
**Trask** 27:13 Does fail fast mean, throw an exception, or does it mean, return, like, empty…
**Jack Berg** 27:24 It means return out.
**Trask** 27:25 I love it.
**Jack Berg** 27:26 On the covers, there's an exception that's thrown, but it's caught, and, like, you know, it doesn't interrupt, for example, the context extraction process, it just results in an empty.
**Trask** 27:37 And so the question is whether… To strip out invalid things… Or to return empty.
**Jack Berg** 27:50 That's right.
And both result in, like, a warning logged, like, regardless, and it's just like, you know.
I guess in my head, returning empty is sort of like a bigger red flag that causes you to have to go find that warning log.
**Trask** 28:15 Yeah, I was waiting to give my… opinion, see if anybody else, but I have very… Much the same opinion to return empty there.
**John Watson** 28:26 Renov has his hand raised.
**Trask** 28:29 Oh, sorry.
**Pranav Sharma** 28:29 No worries, yeah, I just wanted to say, I was also confused by this change as to what motivated this, and I don't think the person ever responded to that. Oh, he did.
**Jack Berg** 28:40 I reinforced your question, Pranav, and they did.
**Pranav Sharma** 28:43 Yeah.
**Jack Berg** 28:43 up with an answer. So, no specific issue, not motivated by other implementations. They were just looking through the flow and found this. And so it was purely motivated by analyzing the source code.
**Pranav Sharma** 28:57 I see. Yeah, so the current implementation in this PR was, like, similar to the other implementations in Go orjs?
So, I mean, I think that was the primary reason why I approved it.
**Jack Berg** 29:11 Mmm.
**Peter Findeisen** 29:14 I also have a remark here, because baggage is something that's not exclusively for OpenTelemetry. It's a standard that can be leveraged by applications as well.
So, the current behavior means that… An error, or maybe intentional behavior of the application.
Will… erase all the OpenTelemetry baggage entries.
So there is a potential risk here, perhaps?
some kind of attack, or… I don't know exactly what, but… Doesn't seem quite right.
**Jack Berg** 29:58 I think if I'm.
**Trask** 29:59 That's okay.
**Jack Berg** 29:59 correctly. The idea is, like, hey.
Maybe somebody can take advantage of this fact, that we throw out the baby with the bathwater. Like, if there's a single incorrect baggage entry, we throw out all of it, and, you know, maybe the default baggage encoder works as intended, it encodes entries, but somebody's able to take advantage and slip in like, an additional baggage header, right? Because you can have multiple header values, and the one that is outside of the control of the baggage encoder, you know, intentionally includes incorrect encoding.
**Peter Findeisen** 30:38 Right.
**Trask** 30:41 Jack, maybe I didn't understand, the… the current PR, does it just strip out the… invalid octet, or does it strip out the whole baggage, you know, entry, single baggage entry completely, sort of like Peter was describing?
**Jack Berg** 31:04 It throws out this… the whole bad single entry.
**Trask** 31:09 Oh, okay.
**Jack Berg** 31:12 So not just the octet, but I think what Peter was, you know, describing was, like, do you throw out all the entries, or just the one bad entry?
And, like, what we currently do is we throw out all the entries if one is bad.
**Peter Findeisen** 31:30 Right.
**John Watson** 31:33 You're saying we do that today, or this PR does that?
**Jack Berg** 31:36 We do that today. Currently, we throw out all entries if we find one that was incorrectly encoded.
**John Watson** 31:43 Okay.
**Jack Berg** 31:46 I mean, I think that's a pretty good point by Peter. I've never felt super strongly about this, and yeah, like, I can see the merit in that, like, right? So, there's no guarantee that, all the… all the bag of cheddars.
you know, are encoded using, you know, your same encoder that is correct. And so, you know, this doesn't really hurt things too much, so why not do it? It's a little bit safer.
**John Watson** 32:18 Not that we necessarily want to… leverage this, but do we know what the behavior of, the open tracing baggage was, and what the open census behaviors were?
**Jack Berg** 32:32 No.
But, Pranav mentioned that this was… The same implementation of OpenTelemetry Go and JavaScript, for what that's worth.
**Trask** 32:52 Yeah, it's definitely worth something.
**Jack Berg** 33:00 Okay, unless anyone feels strongly, I'll, you know, sort of relay the bits of this conversation that matter on the PR, and it's an approval for me, so, unless anyone plans on blocking, I'll just merge it.
Jay, you have the next topic.
**Jay DeLuca** 33:23 Yeah, just to inform, we just released a new feature in the Ecosystem Explorer. It's a very basic, right now, but it's a release comparison, so you can look at what instrumentations were added, removed, or… Configuration options that change, release to release.
A little slow right now, but Yeah, and so, like, it's very high level, and, some of the information is a little… Wonky, just because we're… we've been, like, relabeling some of the metadata and getting that all in the right format and things, but Yeah, just wanted to share this, and some of the diffs here don't account for Whether, like, the telemetry was changed underneath a configuration flag or something.
But, yeah, just making people aware that it's here, and if you have any thoughts or ideas or anything, let us know.
**Jack Berg** 34:21 It's very cool.
But it's gonna be, interesting for the 3.0 release.
**Jay DeLuca** 34:28 Yeah, and that's… that's kind of what I'm building towards. I want to make this… Much more useful by then, so that it's… it can be a… Kind of help people summarize.
I don't know if you want to also, while we're here, go to the Java agent at the top.
And go to the configuration builder.
Gregor, who's not here yet, but he also, if you click the target, you can now, Say, if you want to do a Java agent or the Spring Starter at the top middle.
Yeah, right there.
And it changes the, output format.
**Jack Berg** 35:08 Now it's nested under here.
Didn't, doesn't spring… boot, or Spring, YAML have a slightly different environment variable substitution syntax?
Maybe that's already reflected in here. It does.
**Jay DeLuca** 35:25 It is already reflected, yes. Yeah. Yeah, Gregor did a really good job.
Also, if you, because the enable-disable flags are under, like, a different node, it accounts for that, too. So, like, if you pick an individual instrumentation.
It's in the top left.
Yeah, right there. And if you, like, click on one of those and hit disabled… So it has this… it's under the spring starter node, and if you change that to the agent, it updates accordingly.
**Jack Berg** 35:56 Interesting.
Cool.
**Jay DeLuca** 35:59 And we also.
**Jack Berg** 36:00 That's a bit out of date. Gotta get our renovate set up properly to update to the latest version of the configuration schema.
**Jay DeLuca** 36:08 Well, actually, it's funny you mention that. So I, we also now have a nightly acceptance test that will use this tool to generate a configuration file, and then it runs a Spring Boot application using that application… using that file, and then asserts that some telemetry is omitted.
And so we set it up, and I real… and we had it using 1.1, but the Java agent doesn't support 1.1 yet, so it… that acceptance test crashed. So we updated it, and now it only shows 1.0.
**Jack Berg** 36:41 So, in the future, so that's fixed in OpenTelemetry Java Core, and, you know, it needs to be updated, or, you know, the next version of the Java agent needs to be released, and there was actually, like, a bug in the code that sort of hard-coded the upper limit of the, like, the 1.x version that would be accepted.
It was… it was basically too… too restrictive, and now, like, you know, in the future, if you're using a version of the Java agent compiled against config schema 1.1, And you can use file format 1.2, 1.10, 1.whatever, and so it's much more lenient, because, you know, that's how the versioning is supposed to work. You should be able to use a newer version of the file format, and the schema, and, you know, with a version of the SDK compiled against an older version of the file format, and, you know, some features won't be available, and you should get a warning, but things should just gracefully degrade instead of You know, break loudly.
**Jay DeLuca** 37:44 Yup.
Cool.
**Jack Berg** 37:48 Nice catch.
That's a cool test.
**Jay DeLuca** 37:56 But yeah, so that's it. Just wanted to let people know, and yeah, if you decide to use it, and you have any feedback.
I'd be happy to have it.
**Jack Berg** 38:05 Sweet.
I have the next topic, it's just an inform, but… so, I'm trying to work towards stabilizing the declarative config module within OpenTelemetry Java Core. And, a big part of that Or a big thing that, you know, sort of worries me is the fact that, as a part of stabilizing that, we have to stabilize the in-memory representation of the configuration model.
And, you know, we generate all of these POJOs from, from the JSON schema.
And so, you know, if you come over here and you walk into the source, we have this model package, and all of these models are generated from types that exist in the JSON schema.
And, you know, there's a lot of surface area. There's a lot of classes, a lot of methods that doesn't make me feel great. And so, what I'm doing right now is I'm systematically kind of going through the shape of these model classes, and ripping out anything that isn't explicitly needed, and making it, like, aligned with the sort of standards we hold ourselves to with our public APIs. And so, that's things like, you know, one thing you'll notice right now is they don't have a constructor, so they all have, like, an implicit public constructor. You know, maybe we want that, but we should add that explicitly, rather than just depend on the semantics of this JSON schema to POJO Gradle plugin.
They have all these, like, annotations, and, you know, previously they had, like, you know, this particular style of to-string, hash code, and equals that wasn't very good. It didn't match what we did elsewhere in the project, so I re-implemented, how those are generated to match, you know, what auto value does for two-string, hash code, and equals.
And there's, like, a number of other things, but it's all just in an effort to polish this so that, you know, we can feel comfortable stabilizing these at some later point. So, that's what I'm working towards.
And when we do stabilize it, it's going to be a massive diff in the JAPI CMP.
**John Watson** 40:24 Maybe a dumb question, but… is there a reason not to just… generate auto-value interfaces for… or abstract classes, I'm trying to remember how it works.
For these, rather than generating all the source directly?
**Jack Berg** 40:40 I asked the LLM the same question.
So, what I came back with, and, like, we can actually debate about this, and maybe we should, is… so, right now, all of these model classes, they're not immutable.
They have all of these setters, or these withers, because they're kind of this fluent format, where you can take one, and you can, you know, mutate it to change a property in it, and, you know, do that in a fluent way, where you can do it like a builder, right?
And so AutoValue doesn't really support this pattern, because all of it is, like, immutable records. So if we want to retain this type of thing, which is very convenient for testing purposes, then AutoValue is sort of out, but it might be worth doing anyways, and just, like, making the tests worse.
Just so we can, you know, stick with auto value everywhere.
**John Watson** 41:36 Because when we're actually doing the parsing into these things.
Is it… wouldn't we prefer to have things be immutable when they come out of the parser?
Like, if you're coming out of a config file.
**Jack Berg** 41:56 Yes, but there's nothing really racing against it. It's like, whether it's mutable or immutable, you, you know, you parse the YAML to this, and then very quickly after that, and on the same thread, you instantiate all of the SDK components.
So there's nothing really racing against the mutations, and I don't really envision anything that could.
**Trask** 42:20 Can you show an example of what you mean by making the tests worse?
**Jack Berg** 42:26 So yeah, let's go look at a test, and basically what we do in tests is we programmatically build up these models all over the place.
And so we take advantage of these with methods everywhere.
And I'm gonna go try to find an example of that, but.
**Trask** 42:44 Do we have… do we do builders in… auto value builders in some places?
**Jack Berg** 42:50 In some places, yeah, and that's what I was gonna get to, is like, yeah, you could replace that with, like, a builder pattern.
But… Let's… let's just, like, look at one of these, and then… Yeah, like, here's a classic example.
As this is everywhere in these tests.
And, yeah, that's the same thing as a builder, but, you know, We just don't do it right now.
Oh, hmm.
if we're gonna go with the auto value, which I can explore if that's possible, but, like, one thing that would be really nice to have, and I don't know if AutoValue does this, but, like.
Suppose you have an immutable instance. I want a way to, like, convert it back to a builder so I can mutate it again, and then create, like, a new immutable instance. I want a two-builder method on every single one of those, and I forget if AutoValue supports that out of the box.
Anyways… Yeah, so I'm not in a rush to stabilize this stuff, but, you know, this is a good conversation to have. You know, I had the same thought, can we use auto-value for everything? And so, if other people are thinking the same way, you know, that gives me more incentive to explore that.
**John Watson** 44:21 One, one tiny comment.
It looked like the with method Was… was… was doing a mutation?
which is different than the with method from Lombok, which I'm more used to, which is fully immutable and gives you a copy with the change. So, just a comment that someone who's used to Lombok might see this and assume that, and… Potential foot gun.
**Trask** 44:48 That's generally what I assume for a with method, is to return me a new copy.
**Jack Berg** 44:56 That… me as well. Like, you know, when I actually get… went and looked at these generated classes, this was surprising to me.
I mean, it's surprising and not… it's surprising that it's not consistent with Lombok. It's not surprising in that, like, doing the Lombok style takes a lot more machinery.
And so, this is just, like, the much simpler way to achieve this, if you're generating code.
**Trask** 45:19 Well, but why not just call it set, random, set?
**Jack Berg** 45:23 I don't know. Honestly, this JSON schema to POJO library, like, you know, I've customized it so much right now that I'm debating just ripping it out altogether. Like, it's just… it's not doing that much work for us, versus just, like, parsing the JSON schema and generating the types manually with some sort of, like, simple templating.
engine thing. So.
**Trask** 45:45 I see, so you're… you're having to conform the shape of this API to its expectations?
**Jack Berg** 45:52 Exactly. Like, I'm fighting… what this JSON schema to POJO library wants to do.
And sometimes it's, like, aligned with what I want to do, but often it's not.
Okay. Anyways, look out for more PRs like that, that's the… that's the intention here, is work towards stabilizing declarative config at the programmatic level.
Any other topics that folks want to talk about?
All right, y'all. Well then, I'll see you next week.
Have a good day.
**Trask** 46:44 Thanks, everyone.
Bye.
**Robert Niedziela** 46:46 Right.
