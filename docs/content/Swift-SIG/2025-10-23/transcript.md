SIG: Swift SIG
Date: 2025-10-23
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 00:19 Hey, Martin.
**Martin Holman** 00:22 glue.
**Vinod Vydier** 00:25 Hey, hey.
**Bryce Buchanan** 00:27 If not, Mary.
Nacho said he wasn't going to be here today, so we can get started here pretty shortly.
**Ariel Demarco** 01:45 Hello?
**Bryce Buchanan** 01:55 Now, if you have any topics, please add them to the meeting notes.
I'm sharing my screen here… Come on…
Okie dokie, why don't we get started? So topics from last week,
App crashes when… or in test flight build,
Oh, interesting.
Yeah, so it looks like this was an unrelated issue, but, I still want to document this issue. I haven't had a chance to do that yet. But yeah, so that's still on my plate. Nacho created a nightly build.
for, for, the…
core and main repo interactions. I had some feedback for it. I'm not sure if he's… doesn't look like he's made the changes.
for that yet, but I might just merge this, for the time being, and allow the, the…
This, this to actually, like, or the, the change…
that I asked him to make, which is, you know, running this against the head of the core repo, rather than the latest release.
Yeah.
Okay.
CocoaPods issue in Slack?
-Oh.
Why is it doing that?
Praying out loud.
Can anybody summarize this?
**Martin Holman** 04:38 Looks like they said,
Hey folks, looks like these two pods were left behind in the 2.2.0 update, could you release them? It looks like they are…
It's just… They linked to this run.
Yeah, a GitHub action run. I haven't clicked on it yet, though.
But I put it in the Zoom chat.
**Bryce Buchanan** 05:07 Here we go, okay.
**Martin Holman** 05:14 Hopefully that says which two, because they said these two pods were left behind, but their screenshot lists three pods.
Oh, I see, so OpenTelemetry Swift Protocol Exporter Common, and OpenTelemetry Swift Protocol Exporter HTTP,
Are still at 210, and the persistence exporter is at 220.
**Bryce Buchanan** 05:38 I think that is because those are managed by the core repo now.
**Ariel Demarco** 05:48 Yep, they are.
**Bryce Buchanan** 05:53 Yeah, so HTTP… Common. So is this, let's look at this. So… 220…
So that was the last one.
Right?
Yeah, we're at 220.
**Martin Holman** 06:17 Pix.
**Bryce Buchanan** 06:30 So we just… we just need to remove that pod from this, from this job, right?
Because it's handled… it's handled here now.
**Martin Holman** 06:43 So they don't need to be released then?
**Bryce Buchanan** 06:45 They don't need to be released with the main repo, because they're released with the,
the core repo.
**Martin Holman** 06:54 Oh, okay.
**Bryce Buchanan** 06:56 So… Come on.
**Vinod Vydier** 07:02 So the main report, yeah, it doesn't have… the API and SDK is in the core, right? So…
That's all you need in the pod.
Is that…
**Bryce Buchanan** 07:10 Yeah.
**Vinod Vydier** 07:11 Good.
**Bryce Buchanan** 07:12 Although common, comment in HTTP.
Is common?
**Martin Holman** 07:22 I feel we didn't have any of the exporters in the core one. I thought that was the whole point of it.
**Bryce Buchanan** 07:26 Well, yeah, we had to make some,
trade-offs here, because, there… there are…
dependencies in the… in these… I'm not sure exactly… I can't remember exactly where, but there are dependency issues where the exporter needs to be with, the…
the, API and SDK.
**Martin Holman** 07:52 Right.
**Bryce Buchanan** 07:54 Although, that's interesting that the, exporter common… Is not in here.
Hmm…
That's weird.
**Ariel Demarco** 08:30 But does… does the standard output supporter depend on common?
**Bryce Buchanan** 08:39 No, I don't think it does.
doesn't… yeah, I mean, it doesn't appear to depend on it, because this is… this is mostly for the,
Protobuff stuff.
Mmm… So it's interesting that those two are failing.
So why is this one failing?
**Martin Holman** 09:10 Well, because it's looking for common at 220 when it's at 210.
**Bryce Buchanan** 09:16 Right, right, but, common is,
So this… I mean, maybe it's an order issue? Is that… could that be what it is? Because this…
**Martin Holman** 09:31 Then why did Common fail?
**Bryce Buchanan** 09:33 Yeah, that's what I'm… that's what I'm curious about.
Hmm…
**Martin Holman** 09:46 I think it was at the bottom of this, I saw something.
The.
**Bryce Buchanan** 10:01 Oh, is… is it because… oh, I see. Is it… it's looking for…
the HTTP exporter, or no? Is that… hmm… Hmm…
**Martin Holman** 10:26 Is this… this is the… oh.
And that's confusing.
**Bryce Buchanan** 10:40 Yeah, that's… that's rather odd.
I'm kidding.
Oh, this is Cornell.
Let me look at the job again.
Tag and release, yeah.
Okay, so…
**Ariel Demarco** 11:10 Okay, so seems that the command is failing because of a compilation issue.
Regarding the value type of 3 double record… 3-double log record.
If you see the, their… the error in the release?
go to line, 286.
**Bryce Buchanan** 11:37 Oh.
Oh, interesting.
Curious?
**Martin Holman** 11:47 But our other CI test didn't pick this up?
**Bryce Buchanan** 11:52 Yeah, how did that?
**Ariel Demarco** 11:52 So… as that is not compiling in CocoBots.
HTTP is not compiling, too, because it depends on it. So, it's just fixing that compilation issue.
**Billy Zhou** 12:07 Oh.
**Bryce Buchanan** 12:14 Well then, alright.
Hmm.
I wonder how that snuck by him.
Alright, so,
Does anybody want to take a look at that? Otherwise, I can… I can take a look at it after this meeting.
**Billy Zhou** 12:34 Okay. I broke… seemed like I broke something.
**Bryce Buchanan** 12:50 Alright, thanks, Ari.
**Ariel Demarco** 13:03 Shall I do opportunities, too?
**Bryce Buchanan** 13:06 Yes, yeah, if… I mean, if that's… that's really curious that we were able to…
release the… release the product, you know, release the, SDK with that, or the, the…
You know, the whole library with that error.
**Ariel Demarco** 13:26 Yeah, I don't know why SPM didn't complain and Cocopots did, so I'll take a look. But, regardless…
I have to… probably I have to do some code changes, so…
I would… I wouldn't want to target as 2.2.0.
**Martin Holman** 13:44 I let them know on Slack that, someone's looking into it now.
**Bryce Buchanan** 13:50 Alright, so the next topic, deploy OS version.
Adjust platform deployment targets to match Xcode 16.
**Ariel Demarco** 14:09 I did that for a week.
**alexcohen** 14:10 Feed a dog.
**Bryce Buchanan** 14:11 Oh, interesting.
**alexcohen** 14:12 I think that guy works at Datadog.
They asked… they asked for this before.
Right.
Obviously, he says he's happy to help. I gave it a try last night just to see any compatibility problems or anything. Only the concurrency stuff has a couple of things where we need availabilities in there, but other than that, everything seems to work perfectly fine.
I personally don't have any issue
going backwards like that, and I don't think it would cause any issues to… to anyone, really, anywhere. But it's worth bringing up, and if we can address it, addressing it quickly.
**Bryce Buchanan** 14:50 Yeah, I thought that there was something that we were using in our… in the metrics, maybe, that requires, OS 13, but if that's not the case, then there's no… no issue doing this.
**alexcohen** 15:04 So are the metrics in the core, or are they in, the non-core?
**Bryce Buchanan** 15:09 Those are in core, yeah.
**alexcohen** 15:11 Oh, okay. Yeah, I… I didn't put the branch up, because I didn't want to intrude too much on… on what this guy was… this guy was helping and stuff, but I just gave it a try, and it was only the concurrency stuff that had any issues. Everything compiled fine, all the tests ran fine.
**Bryce Buchanan** 15:30 Cool, yeah.
Do you want to, open a, like, a… push your branch up and open a, draft PR, and then we can start working off that for, fixing the…
concurrency issues.
**alexcohen** 15:46 Yeah, well, actually, my branch has the concurrency issues fixed, it's just availability,
**Bryce Buchanan** 15:52 Okay.
**alexcohen** 15:52 abilities here or there. Now… That's okay.
question… question is, should we instead ask them to participate? I don't know, I don't know if he's here. I don't know.
I don't know what N is… stands for, what his real name is, Max or something, maybe.
But, I guess we're only 6 here, so I don't think…
**Bryce Buchanan** 16:13 Yeah, it doesn't look like it.
**alexcohen** 16:15 Maybe we can just say yes, it would be great if you could put a PR up for us.
**Bryce Buchanan** 16:20 Yeah.
**alexcohen** 16:20 To get their input.
I mean, I can do it, but it might be good to get them participating.
**Bryce Buchanan** 16:27 Sure, yeah, I agree. I think that's a fine idea.
I'll just leave a little message.
Oh, that's you.
In Create. There we go.
**alexcohen** 16:48 I think one thing I didn't try is the Swift Linking 2, core.
Because they're not asking for this… for… well, not SWIFT, but whatever the main… main repo's name is, linking it against… with this, but I don't think that'll be… I don't think that'll be a problem. But they're not asking for that one to have this support, they're just asking for this one, so…
**Bryce Buchanan** 17:13 Yeah, yeah.
Cool. Did you, Andrew, or Alex, did you add that… you added that to the, the topics here?
Yes, I did.
I just wanted to clarify that. Cool, alright. Let's see, any other issues for us to look at? Billy, do you want to… is there anything to summarize in the issue department?
**Billy Zhou** 18:29 Close to a handful of, like, tasks that were stale, and then I saw the documentation update for,
So I put out some small PRs for that.
**Bryce Buchanan** 18:43 In the, in the info.
**Billy Zhou** 18:50 Yeah, I think I put one up for both of them,
Let's just what the, the SPM release, documentation did the two, and then I guess CocoPods doesn't need it, because you guys, pointed the pods to the old, the new directory.
It seems like most of our issues are, like, review issues,
And then there's this new story of, like, the metrics, exporter,
So there's that, and then, I was planning on pushing some, more of the instrumentation, like, for, like, app launches, like, crash reporters, whatever, in the next, like.
a couple weeks, probably in the next week or so.
yeah, maybe I'll, like, yeah, I was just hoping to share that, fairly soon.
**Bryce Buchanan** 19:46 Cool. Look forward to it. That sounds great.
**Billy Zhou** 19:53 But yeah, so there's nothing really that big, for issues so far.
**Bryce Buchanan** 19:56 Okay, cool.
I'll just make a quick summary.
Are you gonna, do a specific crash reporter, or,
Or make it a generic option, or what's your plan with that?
**Billy Zhou** 20:25 Yeah, I guess I was wondering, like, what sort of, dependencies you guys would be interested in taking on for upstream,
I saw that, there's, like, different types of crash reporters, so, like, for instance, like.
Microsoft, like, PL crash reporters are really good for the live reports, and, like, I'm using that for hangs, for instance, like, it seemed like it was, like, really performant, and
But then for, like, crash recovery, like, I saw people, like, you know, prefer to KS crash and things like that, and I also tested those,
So, from my perspective, if we want to get, like, stack traces for hangs,
Then we probably need PL crash, and then, because you only want one crash reporter, typically, like, you could al- I could also put that as the crash reporter,
I don't know, that was kind of what I was thinking.
**Bryce Buchanan** 21:21 Hmm, yeah.
Yeah, that's kind of what I suspected. It might be interesting to see some, you know, optionability, you know, like, let whoever's using the SDK decide which crash reporter they want to use, and maybe make, like,
Some sort of, you know, instrumentation for each of them to… to translate them to,
You know, hotel events or something like that.
**Billy Zhou** 21:51 I see. Yeah, I can make a, like, an agnostic, like, crash provider thing that they can supply.
**Bryce Buchanan** 21:56 Yeah, yeah.
**Billy Zhou** 21:58 And then, yeah, I guess, like, and then,
Like, there's also the thing about Metricit,
What do you guys think about MetricKit in general? Like, we have…
Like, at least, like, from when my team was investigating it, we kind of have, like, some, mixed opinions on it.
**Bryce Buchanan** 22:18 That's where it gives you, like, a daily summary of things?
**Billy Zhou** 22:25 Yeah, like, I think a lot of the docs advertise that, like, with the new update, all the data's reported in real time, but, like, we didn't really see that to be the case for a lot of them.
**alexcohen** 22:38 Metric kit is a tough one, just because the diagnostics are sampled, and we don't know what sampling they have.
And from… they started out iOS 13, I think, where they were every 24 hours, you got a batch of them. Now, from iOS 15 or 18 and up, I think, they're, they're live, so the next… next launch is when you get them. But it's, like, you can't really…
Totally trust that, and you can't really associate.
any of the diagnostics with any type of other set of data. Like, there's no way to make that association, except if you're… you want to have some heuristics over the timestamp range. So, dealing with metrics.
**Billy Zhou** 23:25 You don't have the real start and end times of anything, right, from what it seems like.
**alexcohen** 23:30 What's that?
**Billy Zhou** 23:31 It didn't seem like you have, like, the real, like, start and end time of anything, so it's kind of hard to report as, like, a span.
**alexcohen** 23:39 Yeah, exactly, and… but on top of that, like, figuring out where it goes in your… whatever, however you call… whatever you call a session, like, what session it might have ended, what that di… or what diet… what session it was part of,
So because of the time, the time is totally, you know, feels very random. Or actually, it's the time that it was sent to you, I think, most recently. Not the time that it happened, but the time that it was sent to you, so…
**Bee Klimt** 24:05 So, the metric kit reports actually have the… they have both times, the time it's sent, but they also tell you the time it's recorded over. But anecdotally, we've always seen it say that the record… the recording period is…
From midnight to midnight the previous day in the user's local time.
Which makes it even more difficult to, like, correlate with anything, to your point.
**Bryce Buchanan** 24:30 Yeah, it's definitely more of just, like, a summary of
Yeah, it doesn't seem like a good idea to attribute a session to that, but yeah, that would be kind of hard to…
you know, prevent that from happening with, like, the session automation, I guess just the way that it applies session information, but…
**alexcohen** 24:53 All that being said, though, if you… if we move over to… also, like, there… some of them are profiles, some of the payload diagnostics are actually profiles, so we would have to jump into the… the whole part about profiling, which we don't really have anything on the Swift side for that yet.
So I think hangs and crashes are actual stack traces, and the other ones are… all the other ones are profiles. But there's the whole other side about the actual metrics of them, which do actually come in, like, within a 24-hour timest with…
It's aggregated over a day, so it might be interesting to be able to push those through our metric system, the hotel metric system.
I would… I would start there with Metric Kit, if I were to do anything with Metric Kit and OTEL, much more than diagnostics, especially because those are, unsampled. The metrics are not sampled, the diagnostics are sampled.
So, and we have a time range that's in real time range and stuff like that, so that… that could be interesting around the metric side.
**Bee Klimt** 25:56 Aren't a lot of the metrics bucketed into histograms? Because I tried to…
I mean, I've tried some things with representing it with hotel metrics, but the histogram buckets didn't line up, and I didn't think… at least at the time I tried it, we didn't have APIs to set the buckets to be the same as what MetricKit was reporting, so it was not a good match.
**Bryce Buchanan** 26:18 Oh yeah, we should have a bucket, bucket in the builder. You should be able to set the buckets now.
I've… I've been… I have, like, an open project where I'm trying to translate the metric kit, histograms into a… into a…
hotel metric histogram by just, like, recreating the averages and, like, just implement… you know, adding them one by one.
**alexcohen** 26:47 But, I haven't been able to complete that yet to see how well it works.
I wanted to go back to the… to the actual crash reporters that we were talking about a second ago. One thing that I would really like in whatever implementation we have is for it to be in its own target.
And its own, well, pro- what is it, packaged? No, not packaged, not packaged. Product, I guess. So that… I basically, don't want it to be automatic, because if it's automatic, it's gonna cause problems, like, for everyone, because everyone has their own crash reporter.
And if we just add a crash reporter directly into, say, core, or even the non-core part, it's gonna break a lot of things for everyone. Everyone's gonna all of a sudden have two crash reporters. So I would make it extremely explicit that you have to add
An actual product or target to your, like, depend on that target, in order for it to end up in your app.
Or whatever it's using, hotel.
**Billy Zhou** 27:51 Yeah, we can make it opt-in also for, like, binary size and stuff like that, yeah. Good.
**alexcohen** 27:57 And I would, I would say KS Crash, is the best out there. PL Crash Reporter is good.
But Chaos Crash is, by far, at least in my opinion, by far, the top that's available.
Today.
**Billy Zhou** 28:12 Yeah, sorry, go ahead, Bryce.
**Bryce Buchanan** 28:16 No, I was just… I was just… You know.
I just said, cool, that's all.
**Billy Zhou** 28:25 Oh, yeah,
Yeah, I was just wondering, Alex, like, like, one, what makes you say, KS Crash? Like, what, which qualities would you say makes KS Crash the best reporter, and two, like, like, how would you propose getting, like, live crash, stack traces,
If, we're on the… if,
like, if you only want to use KS Crash, for example.
**alexcohen** 28:53 Sorry, what's the question? How would I propose getting a little chaos crash is a basic crash reporter that reports Mako events, or events. It reports crash…
logs for Mako events and signals, and does some other stuff as well. I would ignore all the other stuff, because we're talking about real crashes here, and not everything else. And all the other stuff is already collected by a lot of different pieces within OpenTelemetry. But KS Crash, there are multiple reasons why I like Chaos Crash. First of all, it's the one we use at Embrace.
Second of all, I sort of know the… the person that's been working on it, has been working on it for a very long time. It is used in some of the… most of the largest, observability platforms out there, like Sentry, and, and, the…
Can't think of the names that are escaping me. I know Datadog doesn't use it, Datadog uses PLCrash Reporter.
Thank you.
**Ariel Demarco** 29:52 Bugsnag, I think they're using, too.
**alexcohen** 29:54 Yes, Bugsnag. Well, the guy, the guy used to work at Bugsnag. Bitdrift, I guess. But yeah, so KS Crash, to me, is the biggest one. I'm also, I also push a lot of stuff to KS Crash.
So that, that helps for me liking it, I guess.
But I found it to be the one that is the easiest to use and gives us the best output and the best performance overall. Now, that definitely doesn't mean we shouldn't be able to also connect BL Crash Reporter or any other system out there, so I really like the idea that you were saying earlier that
we can have some sort of protocol or interface or something, and it can be, you know, we can have one for KS crash, one for a PL crash report, and whatever anyone wants to use, they just act the same.
**Bryce Buchanan** 30:43 Yep, yep, that's what I'd like to see, yeah.
**alexcohen** 30:46 But even more important is I know that, someone's, at some point, started the semantic conventions for crash… for crashes, but I don't think there's actually any, current convention.
So, it would be good to figure out what, what those conventions would be for, for crash reporting within OpenTelemetry.
**Martin Holman** 31:09 I think there are, they're just pretty vague.
**Billy Zhou** 31:12 I've been using exceptions, just, like, there's, like, exception at type, message, and stack trace,
I figured that covered most of it, but I guess there's things specific to Crash that we might want to add.
**alexcohen** 31:25 Yeah, well, I mean, that's even better. If there's something specific to crash, and there's also something specific to exceptions, at some point, they become very, very similar, and an exception is just one type of crash, sort of, or the other way around, a crash is a type of exception.
**Billy Zhou** 31:40 So…
**alexcohen** 31:41 It would be good to figure that out before, and sort of get that accepted, I think, by the community, before we actually put in anything too, too concrete, as far as crashes go.
**Bee Klimt** 31:55 Exception is pretty close. I think the biggest difference I saw was that with a crash report, you have multiple threads, and the exception semantic convention is very much about having one stack trace instead of multiple, so we'd have to figure out how to represent that.
**alexcohen** 32:10 Yep.
**Billy Zhou** 32:11 Yeah, and then there's the call stack tree that ElementaryKit uses.
That's so different.
**alexcohen** 32:18 Yeah, what's… well, the call stack tree is… they did that because… to support profiles and to… basically to support spin dumps and things like that, but it's really, like, you never have, like, more than one child down one… more than one node that leads to another node that leads to another node. So, yeah, it is really interesting.
But I do think that the exceptions here… so, oftentimes, what you'll see is exceptions have, like, you have one sort of stack trace for what led up to the exception, and then after that, you'll have all of the threads.
Right? So, we could expand on exception, possibly, and add, like, threads, or found the exception.threads.
Or exception.threadstack Traces, which would contain the actual stack traces for each thread. So there might be an option to expand on exception instead of creating something new.
**Bryce Buchanan** 33:12 So, the semantic conventions is pretty open-ended on what the stack trace is defined as, so each language has its own representation, so we can just add
Our, expectation to this, to this representation here?
**alexcohen** 33:30 Yeah, and that becomes rough as well, like, is it symbolicated? Is it not symbolicated? Usually when you're pushing up a stack trace from a client, it's not going to be symbolicated, especially on mobile.
**Bryce Buchanan** 33:41 Yeah.
Yeah, I mean, we can just specify that the Apple standard format is on here, which, you know, has both symbolicated and unsymbolicated formatting.
**Vinod Vydier** 33:52 Hey, hey Bryce, I think there was some effort in the…
in the client side for Android as well, so I think maybe there's some…
**Bryce Buchanan** 34:02 I think that Android just uses Java, and the,
I'm not sure if the, the de-offuscation in there is… is needing to be specified in,
in the semantic luins.
**alexcohen** 34:19 There was a proposal, I think, from… I think his name is BitOfEvil on Git, on GitHub.
Hanson. He works for Embrace as well, he's on the Android side.
**Bryce Buchanan** 34:30 Yeah.
**alexcohen** 34:31 he started putting together, I think, something around crashes that's a lot more detailed.
So I haven't really looked through it, but, like, regardless of all that, I sort of feel that we should, we should definitely
join in on whatever is going on there and make sure that it fits.
**Bryce Buchanan** 34:51 Is that in OTEPs, or is it in the semantic convention issues here?
**alexcohen** 34:56 I do not know.
**Bryce Buchanan** 34:58 Maybe this document? I think the…
**Ariel Demarco** 35:00 He first pushed that into the…
client-side SEC, and then he went to the OpenTelemetry semantic convention SIG.
**Bryce Buchanan** 35:08 Okay.
**Ariel Demarco** 35:09 To push it up.
**Bryce Buchanan** 35:12 Well, I'll try to find that and add that to our meeting notes, and you can take a look at that, Billy, and decide whether or not you want to
just follow the existing semantic conventions for exceptions, and… and I would, if you do that, I would, use the log events rather than the spans. I think spans have pretty much been,
What's the word, deprecated, and I was.
**Billy Zhou** 35:43 So.
**Bryce Buchanan** 35:43 My brain was wanting to say dilapidated, but…
Yeah, I think span events are deprecated at this point, so.
**alexcohen** 35:52 Really?
**Bryce Buchanan** 35:53 Yeah, I'm pretty… I'm pretty sure, yeah, like.
**Martin Holman** 35:56 Yeah, I think it'll be a long time, but I'm… I feel like.
**Bryce Buchanan** 35:58 Yeah, it's…
**Martin Holman** 35:59 In the air is the…
**Bryce Buchanan** 36:01 I recommended this to start using log events rather than span events, and using span links if you want to associate those log events with a span.
But if you want to take a look at that, the… what Hanson's working on, and implement that, I think that would probably be okay, too, as long as it's not too crazy, but maybe we can take a look at it, next week or the week after.
**Billy Zhou** 36:25 Sounds good. Could you send that link? I think I missed whatever…
**Bryce Buchanan** 36:28 Yeah, I'm not sure where it is, but I'll try to track it down. I might just message Hanson and ask him about it directly. So,
Crash reporting…
**Billy Zhou** 36:40 Okay.
**Bryce Buchanan** 36:47 I don't know how to spell his name.
**Ariel Demarco** 36:49 I can ping him too, no problem.
**Bryce Buchanan** 36:51 Oh, right on. Yeah.
**alexcohen** 36:55 Okay. And, crash…
**Bryce Buchanan** 36:58 hoarding, Discussion from, Client SIG here.
Okay.
**alexcohen** 37:11 And Billy, if you need any help with this in any way or anything, I'm… I very much enjoy working on crashes, and
That area, so you can feel free to ping me if you want to talk it over or anything like that.
**Billy Zhou** 37:25 Thanks, Alex. I… yeah, really appreciate it.
**Bryce Buchanan** 37:28 Cool.
Okay, yeah, so next release date.
**alexcohen** 37:36 Yeah, so that's… I put that up there. I just know that we've landed a bunch of things since the last,
Since the last release, so I was just… I was just curious. There is…
There has been one bug fix that we put in there around, the document attributes that I feel should get out there sooner than later, because it is a threading issue that could show up for others as well. Or, worst case, a crash.
Best case memory corruption, and stuff like that.
**Martin Holman** 38:07 The next release is likely to be very soon, right? Because 220 is broken.
**Bryce Buchanan** 38:11 Yeah, yeah, exactly. So, I think, I think, yep, that's what I was gonna say, is I, Ari's gonna look into that, that, build issue, get it fixed, and then we'll do a, you know, 221 or 230.
Depending on, the… Amalgamation of, of, additions.
**alexcohen** 38:35 country.
**Bryce Buchanan** 38:36 Ari make that choice.
Yeah, it's ASAPing.
Alright, oh yeah, so I'm gonna be out next week.
So, hopefully, either Nacho or Ari will be here to run the meeting.
Alright, any other topics that we want to discuss?
Huh?
Let's get, 20 minutes back then.
Everybody have a good weekend.
**Vinod Vydier** 39:17 Have a good weekend.
**Ariel Demarco** 39:18 You know.
**alexcohen** 39:18 Yeah.
**Ariel Demarco** 39:19 Bye-bye.
**Bryce Buchanan** 39:19 But…
**Billy Zhou** 39:21 Bye.
