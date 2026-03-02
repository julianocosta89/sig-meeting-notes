SIG: Rust SIG
Date: 2025-11-04
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Sayali Sawool** 01:01 Right. Almost…
**Prasad Sawool** 01:41 Then…
**Cijo Thomas (Microsoft)** 01:46 Hello, can you hold hear me?
**BA Björn Antonsson** 01:49 Yep.
**Cijo Thomas (Microsoft)** 01:50 Okay, thank you. Let me share my screen.
Hopefully, it should be visible now.
Yeah, please feel free to add to the agenda. We can get started in maybe another minute.
Also, please add your name to the attendees list, if you're okay with that.
Okay, I think we can get started. I'm not sure if anyone else joins, typically.
It's been a while since I joined myself, so I'll assume these are the… all the people, so we can get started.
Hey, Prasad, it looks like you are new, if you want, like, if you're comfortable, like, feel free to…
Introduce yourself. Just want to say hello to everyone.
**Prasad Sawool** 03:58 Hello, everyone. I'm new to the OpenTelemeter community, and…
Yeah, I just want to learn more about, Rust and its SDK.
**Cijo Thomas (Microsoft)** 04:10 Okay, welcome.
Yeah, feel free to, like, reach out to me. It's like, if you are looking to get some help getting started or trying to find issues to help, like, feel free to reach out to any of the maintainers or approvers.
**Prasad Sawool** 04:24 Yeah, sure.
**Cijo Thomas (Microsoft)** 04:27 Okay, yeah, we have, like, one issue. Hey, Bjorn, nice to meet you after I ride.
Good weather.
Yeah, okay, 3190, let me open that.
Okay, we did have a brief discussion a while ago, but I don't think we…
concluded anything. Bjorn, can you…
**BA Björn Antonsson** 05:00 Well, to me, I would like to move this into the contrib directory.
To ensure that there are no
as I said, I mean, it's being used in… this…
appender is being used in examples, inside the core repository, and as soon as I change anything, if it has any dependency on this crate.
Which I think it might want to have in the future as well, to do other things. I mean, just if, like, as a fallback.
mechanism. If you don't find anything in the current context, there are other ways to sort of, like, traverse
the… Tokyo idea of span hierarchy, because filtering might remove something.
So we don't activate things in the way we would assume, but I'm not sure. I mean, you can have different filters for different
things. Like, you can have… A more fine, granular, filter for… the, the, the…
the log events than you can for the spans, as far as I know.
So, I'm not sure. I just want to make sure that we don't really…
preclude that. Or the other thing would be to just, remove that, but I think we still have a circular dependency right now, where I can't clean up.
the, the… I can't clean up hotel.
the hotel span builder, because… as soon as I try to do that, this build will pull in the…
the dependency from OpenTelemetry, or tracing OpenTelemetry, which is using fields that are not available anymore, etc, etc. So it's…
**Cijo Thomas (Microsoft)** 07:27 Can we, like, remove this feature flag completely now? Like, do we… what's the… because we added this as a temporary solution for people to create.
**BA Björn Antonsson** 07:36 Yes.
**Cijo Thomas (Microsoft)** 07:38 What's preventing us from removing this feature?
**BA Björn Antonsson** 07:41 The only thing that I said was that you might want to traverse the tracing idea of span hierarchy to find, like, the root.
The service entry span, or what you would like to call it.
Because that might not be… Available, if… if you don't…
If you ha- if you have…
threads that are executing on a… on a, like, inside Tokyo, in a multi-threaded environment, and… and you do filtering, I am not sure that all the spans you would expect will be activated, but the log event will still happen within
A context of a span that has not been, like, activated and deactivated.
**Cijo Thomas (Microsoft)** 08:34 But is that something which we want to solve in, like, this report? Because this part, I'm not very sure.
This was timbered.
**BA Björn Antonsson** 08:41 Yeah, I mean, yeah, yeah, but I mean, it's sort of like, okay, you have to kind of do it somewhere, or we would just say, that…
This other feature is good enough, and we haven't really tried it. But, of course, we can… we can rule it out.
**Cijo Thomas (Microsoft)** 08:57 Yeah, because if some user does filter out the span itself, but not the log, then they would find that that log is not paralleled to the right thing, which is normal even in OpenTelementary, like, even if, like, you look at other languages and people filter out
spans using whatever mechanism, they'll, find that the logs are not… Okay, okay, fine, I'll, I'll, stop move… I'll stop moving this to contrib, and just, and just remove the features. That part, like, yeah, like, moving it to Contrib is something which I think we…
Probably mentioned.
on day one, like, when we started, like, we thought, okay, we'll just start here, we'll move it, when the time, is, like, apt for it. But what I'm responding to was, like, we don't have to
move it just because of an issue with the subtler dependency. That should be, like, a problem which we need to solve, like, nevertheless, like, we cannot have this…
experimental tracing support anymore. It was started, like, with the explicit understanding that it's a temporary thing. So we'll need to get rid of that, like, irrespective of whether it's in the main report or in the contrary report.
**BA Björn Antonsson** 10:04 Okay, okay, fine, fine, I'll just do that then, so, that will probably unblock me from doing the cleanup then.
**Cijo Thomas (Microsoft)** 10:12 So this… this… once we remove this one, like, I… hopefully, like, you should get unplugged, but if you still find, like, there are, like, much more, work which is, like, getting in your way, then I think that's a valid argument. Let's move it, to the contrary and unblock your work. But I want to, like, first see, like, can we clean it up, and then…
get ourselves unblocked. If not, yeah, I'm, like, okay to, like, completely move it off to the contrib.
Both… both the lower appender and the tracing one both can be, like, lifted at that point.
Was that the only thing which we… like, or, like, maybe, like, once you try it out, like, we'll know, like, whether there are anything else, but based on my understanding, this is the only reason why we have that weird, like, dependency thing, and our releases are, like, done in, like, lockstep way with tracing open elementary.
**BA Björn Antonsson** 11:05 Yeah.
**Cijo Thomas (Microsoft)** 11:05 release.
**BA Björn Antonsson** 11:06 Yeah, as far as I… no, that's… that's the thing.
**Cijo Thomas (Microsoft)** 11:09 Okay, thanks. Yeah,
Is that something which you want to tackle, like, removing this, like, feature from the appender itself, and just showing the work?
**BA Björn Antonsson** 11:21 Absolutely, I can do that. I mean, I'm still… I have all the things set up anyway, in a circular way to try out my changes in tracing open telemetry, how they work. So, yes.
**Cijo Thomas (Microsoft)** 11:35 Yeah, thanks for that. I have a very similar topic, which we discussed, like, a few times in the past, but I finally got some time to
Create an issue for tracking that, which is, this is not for…
span being converted as OpenTelemetry span, but there are other use cases where the tracing span is simply used as a enricher, or a context enricher for the logs.
So this feature do not exist, anywhere today, because if you use tracing OpenTelemetry, the span becomes a full-blown span in OpenTelemetry world.
But what we are after is, if someone creates span, maybe not just one, like, there could be any nested amount of span, all the attributes from those will become attributes in the corresponding logs. I used a simple example to demonstrate. So this
log statement, currently, it only has, like, a single attribute, like, status. But what we want is it should have, everything from the log statement, and plus
Anything from the…
a parent span, so in this case, user-ready and endpoint. So this is something which, I think we had even a PR to do it, like, a few months ago, but we never, merged it.
But a lot of people are asking for this feature, because if… I mean, otherwise we are pretty much, like, ignoring the… all the contacts which the user has provided.
So I did add, like, some, like…
notes here, which is, basically, we don't want to do it by default. It should be a explicit obtain feature, so users can decide whether they want
span macros to act as a log enricher, or they want to use the tracing open elementary and treat it as…
full-blown, span. And then there are, like, few design, like, detailed, things, which I don't know the correct answer, like, for example.
What do we do with the span name itself? Like, in this case, it's request.
We don't have any such notion in log, so it has to be an attribute, which brings the question, like, what would be the name of the attribute we would use.
And then something about depth control.
should be… Trace all the parent spans, or should we stop at… some depth.
I don't know the answer again. It could be that we had to go all the way, to all the… like, till we reached the route.
And then there is also a question of, like, what would happen if there is a collision, because there could be…
Duplicate attributes coming from parent span, or the further parent span.
So someone has to determine, like, what circulation behavior.
I lifted, like, few options here. Again, we don't have to solve all of them in one short.
And again, the capability to,
Determine whether all attributes become an attribute on the log, or whether a subset of that becomes,
Depending on the time, I might send a small pair to do a very basic version, which will be just opt-in, but does not include any of these things.
And we'll see whether that's useful enough for users, because many people have asked for it, like, in the past, so we'll see if that's useful, and depending on how it goes, we can incrementally add all these other things.
I might actually wait for Bjorn to, like, I'll wait for you to finish that cleanup first before I do, maybe, otherwise we may have some corrections, but it shouldn't be.
**BA Björn Antonsson** 15:07 That would be great. I'll try to get it done tomorrow. Shouldn't be too big.
**Cijo Thomas (Microsoft)** 15:14 Yeah. I think I'll try to mimic what is done by the tracings format subscriber, which currently has the behavior. There is no… not much control.
pretty much, what happens is every event inherits all the attributes from all the parent spans. That's what the format subscriber is doing as of today. So we could mimic that to begin with, and if there are
Any issues, then only we need to worry about, like, providing all the advanced features.
But yeah, I'll go with that as the initial implementation. And in case anyone remember, like, there was a…
PR, which I opened a few
Months ago, with the guideline, because we want to, like, give a guideline to inducers, like, what should…
If they're starting new, like, what should they do? What APA they should use for spans, what for logs? And if they're not starting new, like, they have some legacy system, then how do they bridge them properly?
And even this one calls for a…
feature, which I just described earlier. So that feature is, like, a prerequisite even before we can make some…
Guidelines like this, so… yeah.
Yeah, so those are the things which I believe we had in the… Meeting notes.
**BA Björn Antonsson** 16:37 I just, added one more thing, I think.
**Cijo Thomas (Microsoft)** 16:42 Did I know.
**BA Björn Antonsson** 16:42 not.
**Cijo Thomas (Microsoft)** 16:43 Okay, now I can see it, yep.
Pills are failing, yeah. I think Scott mentioned this in the…
**BA Björn Antonsson** 16:50 Yeah, into Slack. So, there's someone who…
Who knows about these things need to… Sort out.
**Cijo Thomas (Microsoft)** 16:59 Okay, it's only used in the integration test.
And… yeah, which forces us a bump to the MSRV. Lilith, maybe, like, you probably know more about this. If not, we can take a look offline.
Yeah, it looks like… yeah. So the issue is, like, we are using a version of,
a library which is containing a CBE.
But that's only used in the integration test. We use a… something called dev containers. Sorry, test containers to spin up Docker images or things.
So that's the, like, gist of the issue thing.
The easiest way would be to bump the version and do the MSRV bump only for the test itself. I don't know whether it's feasible, do you know if it's feasible to do…
a higher MSRV, or higher Rust version for the integration test alone.
**lalit** 17:58 I don't think we can do it. We don't have a separate
It's not a separate creation.
**Cijo Thomas (Microsoft)** 18:06 Yeah.
**lalit** 18:06 Don't do that.
For the integration test, so… We may have to look for…
In that issue, it's mentioned, right?
The alternative was…
**Cijo Thomas (Microsoft)** 18:18 There is… no, I don't know whether there is any… Alternate here…
**lalit** 18:23 to use Astral… Oh, that… oh, that means…
**Cijo Thomas (Microsoft)** 18:28 That's so amazing.
**lalit** 18:28 You need bumping the… okay, oh, sorry.
**Cijo Thomas (Microsoft)** 18:31 Yeah, I was hoping that, like, if we just pump the version here, this should not affect anything else. This should be…
**lalit** 18:39 Good evening, huh?
Thank you.
**Cijo Thomas (Microsoft)** 18:43 Yeah, I mean, as of now, like, builds are failing, and we just kind of ignore that, because we know it's in the test, so we just merge the PR, even if, it's failing.
That's what we've been doing for the last few days. Yeah, this one fails, but that might mask any other real issues.
Yeah, do you have some bandwidth to, like.
**lalit** 19:03 I can do that, yeah, I can replace you.
**Cijo Thomas (Microsoft)** 19:06 Yeah.
There were, like, few other, like, security issues which got opened up.
But most of them were in the test area, so I…
I think I dismissed some of them.
But yeah, we still have, like, 3 of them. I think, like, the maintenance can look at it offline. We are not supposed to look at it in a live call, so… yeah, let's look at it offline. I think, same for Contribu, we have some, issues popped up there.
Any other… sorry, I lost the meeting notes tab.
Yeah, anything else which folks want to bring?
Yes, quote asked for, like, some, like, plans for, like, next release and all, because we did a…
bunch of features to OTLP to, like, retry compression and all. I don't think we did a release after that.
But, like, I would…
I don't think we have anything critical which requires a release, but I'm hoping that once we add more features to tracing, like including the cleanup, which Bjorn talked about earlier, and the feature which I talked about.
That would be a good time for us to do the release. I don't have any ETA, but as soon as we have some.
Like, enough bandwidth of… or enough payload of features, then we can cut out the new release.
If anyone needs to do a release earlier than that, like, feel free to reach out and we can figure out something.
Nothing else in the agenda, so maybe we can keep…
**lalit** 20:43 Sorry, I mean, like, in case we are closing, I think there were some discussions on…
Making the timings alternate,
I mean, I just waited to change anything, just for the daylight things to be done at both the time zones, but I think probably
If there's something which has to be done, we can discuss those?
**Cijo Thomas (Microsoft)** 21:05 Yeah, was it already concluded that we'll alternate between Tuesday and Wednesdays?
**lalit** 21:11 There was some discussion, I think people gave some thumbs up, and probably… but I think it was not finally decided, actually. I mean.
**Cijo Thomas (Microsoft)** 21:18 Because he probably did the poll, so he should know the actual number.
Yeah, if, like, we have a reasonable, like, majority voting, then I think we can totally shift to Wednesday, 8am, alternating.
Yeah, as long as this float is not taken by, like, yeah, Wednesday AM, I don't think any other project is taking that. Maybe, like, some airline or something, but usually there aren't much… there aren't much common people attending them, so it should be fine.
Yeah, let me ping Scott and find out the actual result, and I don't know whether I have the permission to change it, but I'll figure it out. Yeah, thanks for the remainder, I'll…
talk to Scott and figure out how to change to alternates.
We can quickly look at the open PRs. This one had reviews. Oh, this might be worth, discussing. I think this was a…
Like, huge change to the way we were doing internal… error handling.
Oh, sorry, that was in the issue, not the PR. The PR itself is now small.
I think Laditha and myself, we have responded already,
So if… I don't have anything to discuss, like, right now, but it might be…
Worth looking at if you have, like, some bandwidth.
The basic idea being proposed is, like, instead of
Like, especially for, like, background tasks, instead of simply…
doing internal loads, we should have a way for people to programmatically respond to it. Because right now, if something goes wrong in, say, the batch processor.
All we do is do an internal log, which happens to use the tracing rate, so technically, people can set up a tracing subscriber, look for the event, and then do something about it, but that's not really what we want.
So the ASCI is, like, quite genuine, like, people want to have a way to programmatically respond to certain things.
The thing which is not clear to me is, like, how much we should go in that aspect. Like, it's… it's possible to, like, redesign the entire thing by firing a callback.
Whenever something goes wrong in our operations where we cannot, like, return anything.
And then the question is, like, should we go and do it across the report? Because the person who opened the issue, he had a very concrete scenario where…
the… SDK, sorry, the OTLP exporter, was failing because of…
new cert not being picked up, so he wants the ability to, like, pick it up and programmatically reactivate by forcing a refresh or something. That was the original issue, which he reported. So we could just solve that problem, like, by providing some ability in the free tray module, which we very recently added.
So users can execute something, in the retry. Or, like, we can just solve it ourselves, like, just make sure, like, if the failure is due to a certain thing, we'll try to reload or something.
So that is my main comment I left here, like, should we just try to solve that particular problem, or should we try to rethink the entire way we are doing internal logging?
If anyone has, like, thoughts on it, like, please do take a look. There is a PR, which initially was quite significant change, but since then, it made to a very small scope.
Again, I left some comment there, so if anyone has more thoughts, please feel free to look at it.
There is one other pier, this one is also quite interesting. It looks like… It's trying to do…
So…
I mean, in the parent sampler, which is supposed to delegate to… sorry, in the parent-based sampler, it's supposed to delegate sampling decisions to inner sampler based on some condition. It's trying to bring a new flag.
To that decision matrix.
Unfortunately, that is not a spec-out flag, there is no spec about deferred.
trace flag, but then the person who opened the PR pointed correctly that, many places within the repo, we are, like, using such flag.
So, we are… we have to, like, find a way to, like, address this one. Like, we should probably get rid of all the unofficial things. This is not a aspect-out thing, it's just our own invention. I don't know whether there was any history or discussion behind it.
So as of now, I'm inclined to not accept anything which introduces, or which spreads the unofficial thing to even more places, because as of now, it's,
it's mostly restricted to, like, Zipkin and Jaeger propagator, which are, like, separate crates, but what this PR is doing is it's going to make it part of the mainstream SDK, like, the main sampler itself. We are trying to…
Figure out whether…
the parent span is having this flag set, which is an… this is the unofficial or undocumented parent flag. So my default inclination is not to spread more of the problem to the core of the SDK.
That's what I'll be replying, but if anyone has, like, more…
context on, or information on sampling, please feel free to chime in. Like, beyond maybe, like, you probably know about.
This one, if you have time.
Please take a look, and see if we can offer some input there.
**BA Björn Antonsson** 27:00 Yep. I will… I'll try to take a look at it.
**Cijo Thomas (Microsoft)** 27:04 Yeah, thanks. This one is, like, a follow-up from Skold. I did review it, so it shouldn't require any new…
Comment on the rose away.
Pierre, again, to retrieve.
So, sourced by GetRef. I did ask for some clarification, which I got.
in the original issue, which means I don't have any concerns.
Yeah, I think Scott replied.
Yes, Corden, poorly.
Wanted, this for some transformation being done.
So I'll remove my… oh, I didn't request for a change. Maybe I just need to approve and merge it in. Yeah, I'll unblock the PR.
I think everything else is a bit old, I don't think we need to look at any of them.
Oh, there is this one, Pione, is it something which I forgot, like, whether this is something we…
Discussed… Yeah, I don't recollect discussing this one. Any… anything beyond? Do you want to discuss this one?
**BA Björn Antonsson** 28:10 No, I mean, so, I think…
We might have come to the conclusion that we…
can work around it without doing that, but I need to double check and think about it some more.
A lot of these things have been sort of, like, swapped out from my brain. It was quite a while ago.
**Cijo Thomas (Microsoft)** 28:34 replicate it.
**BA Björn Antonsson** 28:35 with them.
You can, you can, you can change it, or maybe I should change it to, like,
draft PR or something, so it's not…
**Cijo Thomas (Microsoft)** 28:45 The only thing which I remember was, like, if at all we are doing something for…
Tracer, you should probably need it for metrics and logs to maintain consistency.
**BA Björn Antonsson** 28:55 Yeah, I mean, metrics and logs don't do this either right now, so there is really no,
I mean, we… since it's come up… the reason it comes… has come up for tracing is that we are building things around tracing. Tracing logs go through, like, the normal OTLP pipeline for us.
**Cijo Thomas (Microsoft)** 29:22 Yeah, okay, yeah, it's just that, like, you encode it in tracing, yeah, that's got it. No worries, yeah, I will, move to issues, open issues, this one, I…
Went through the first and second.
This one is probably… it's a bug, I trashed it as a bug. We knew about this, we fixed it for observable glitch. Counters and up-down counters still have this bug,
I don't think I'll have time to look at it anytime soon, so if anyone has the bandwidth.
Feel free to take a look. It's not super straightforward, I remember, like, we did look at it.
A few months ago, and it was easy to fix for Gwage, but it was not easy to fix for…
absorbable counters and up-down counters. That's why we didn't fix it. It triggers, like, some more re-architecting to fix it.
Yeah, I'll currently accept it as a bug and wait for someone.
Pick it up based on bandwidth.
There is an issue about this environment variable, but I believe we don't have any plan to do it right now, because
Yeah, we don't have any Uber package right now, so it's not sufficient for
Environment variable to be there, we'll need to enable features.
So as of now, we don't think we can do it. I think I already replied to that. Oh, no, I didn't reply.
Oh, this is… Protocol code 1, okay.
Interesting, yeah, I…
Maybe I'll ask, like, Scott Weather here some time to look at it as part of OTLP exporter stabilization.
Yeah, that's probably the best bet.
There is an issue from the spec team about new consistent samplers. Again, this should be, like.
Pretty much additive changes, we are adding, like, new samplers and spec.
What's with that.
should be, like, just a deep change, we don't need to do anything immediately.
This one we already discussed. I believe this one is assigned to someone. Yep, this one we covered.
I think, like, yeah, Rustar, like, pretty old issues, I will… Ignore them for now.
That's the end of all items from the meeting agenda and open issues. If anything is still pending, like, I can discuss it now, but other ways we can meet next week. I generally… I was kind of away, but I'll be away once more for next week. Next week is KubeCon, so I'll be attending that full week.
But after that, we expect to be, like, spending some more time, too.
look at open issues, trying to get tracing towards table. But meanwhile, if anything comes up, yeah, feel free to reach out.
Okay, if there is nothing else, we can end.
Few minutes early.
Thank you, everyone. Bye-bye.
**BA Björn Antonsson** 32:16 Bye.
**lalit** 32:17 Thank you. Bye.
