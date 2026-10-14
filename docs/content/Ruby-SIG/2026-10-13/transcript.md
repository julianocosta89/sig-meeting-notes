SIG: Ruby SIG
Date: 2026-10-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle (New Relic, Inc.)** 01:06 Hello.
**Robb Kidd (he/him)** 01:16 Morning.
**Kayla Reopelle (New Relic, Inc.)** 01:18 Good morning.
We might… one more minute.
Good evening. Good day.
Okay, I think we can go ahead and get started. I'll share my screen.
And then, if you want to add anything to the agenda… Oops, what's going on?
There it is.
To start off with the SPEC SIG today… Not really much that pertains to us. There were some presentations about the collector and a lot of the issues related to the collector.
The one thing that could be interesting is that Excuse me, I gotta sneeze. I have some kind of cold I think I'm fighting.
Is that the software bill of materials.
seems to be gaining some traction. I'm not sure what that looks like.
For us, if we are participating in this packaged version of OpenTelemetry.
But, that may come up more in the future.
Yeah, I think that's the only thing that really feels relevant for this group.
at some point, eventually, we may be asked to provide a SIG update, and… the specification SIG meeting I'm hoping we can hold off onto that until we're maybe ready to put forth, like, a metric stability proposal to encourage more eyes on it.
But we'll see what is asked of us.
Anything on this agenda that people want to take a look at more closely and talk about?
Okay.
And, let's see, we have some things… I guess I jumped the list.
So… One question I have is whether… We need to keep metrics and logs pinned at 3 places in the SDK.
Actually, you know what, let's… let's table that for later.
So, a different, Question? This was… I'm not sure who added this. This was here… This morning… There's a question about the structure of the semantic conventions, Jim, so how can we structure it to support generating… these things without conflict. Oh, it looks like James opened it. So here's this PR.
Aha.
So how can we generate event names without having any… Constant conflicts would be my guess, is what he's asking.
Don't think that's something…
**Robb Kidd (he/him)** 04:49 Is there an example in that PR?
Of… the conflict?
**Kayla Reopelle (New Relic, Inc.)** 04:56 And… Yeah, that's a good question. Maybe… Trying to think what could… Exception, possibly?
I don't know. But that would be a great follow-up question, is what would the conflict look like? I can't think of… looking.
**Robb Kidd (he/him)** 05:24 And.
**Kayla Reopelle (New Relic, Inc.)** 05:25 list, yeah.
**Robb Kidd (he/him)** 05:26 The point of the incubating, the only… the… Places where I recall potential conflicts would be if.
A metric and an attribute name matched, which… What, a year or two ago, we were told that it was highly unlikely, so we.
**Kayla Reopelle (New Relic, Inc.)** 05:46 Yeah.
**Robb Kidd (he/him)** 05:46 We ran with that as a… probably won't happen.
And then the… and then the incubating namespace was supposed to, like.
Cordon off.
The stuff that was not stable. Like, incubating sort of the superset of all names, and then the not incubating are the stable names, and incubating is there to, prevent.
Matching things that are stable and present in incubating don't.
conflict because they're under incubating.
**Kayla Reopelle (New Relic, Inc.)** 06:19 So yeah.
**Robb Kidd (he/him)** 06:20 I'd be curious about what conflicts there are, if any.
And I will ask that question on the PR.
**Kayla Reopelle (New Relic, Inc.)** 06:26 Okay, sounds good. Just leave that, and then… There.
Yeah, that sounds great.
I know there's… were some questions.
related to the metrics PR that I'll get to later about, like.
Should we be generating metrics from semantic conventions? Questions like that.
That I don't know if I have answers for yet.
**Robb Kidd (he/him)** 06:57 I think that's the promised land.
**Kayla Reopelle (New Relic, Inc.)** 07:00 Hello?
**Robb Kidd (he/him)** 07:01 Weaver of… But yeah, I don't, we're only just getting metrics, much less automated.
**Kayla Reopelle (New Relic, Inc.)** 07:10 Yeah.
**Robb Kidd (he/him)** 07:11 So…
**Kayla Reopelle (New Relic, Inc.)** 07:11 Yeah.
Possibly getting a manual solution in place before… Trying to automate everything.
**Robb Kidd (he/him)** 07:20 It's generally been my philosophy, is to do it manually before you automate it, to make sure you do.
**Kayla Reopelle (New Relic, Inc.)** 07:26 Yeah.
Okay, cool. Any other points on the semantic conventions or questions?
**Robb Kidd (he/him)** 07:35 No, I think that's the… I hadn't seen this prior to the meeting, so I'll review and ask the question about.
What conflicts are there?
**Hannah Ramadan** 07:46 It does look like James added two comments on the PR.
on conflicts from not splitting based on type. Not exactly sure what that means. It's in the comments of the, summary conversation page.
**Robb Kidd (he/him)** 08:10 Oh, this is a… this is a pretty old PR, I see. So it's…
**Kayla Reopelle (New Relic, Inc.)** 08:13 Yeah.
**Robb Kidd (he/him)** 08:21 A namespace module.
per root namespace.
trying to remember if we had considered that.
It rings bells.
**Kayla Reopelle (New Relic, Inc.)** 08:40 Yeah, I feel like we had…
**Robb Kidd (he/him)** 08:43 I think we had, and we were like, why? Why is the.
**Kayla Reopelle (New Relic, Inc.)** 08:45 Yeah. And then the constant names were just getting to be very, very long and so.
**Robb Kidd (he/him)** 08:51 thousand.
**Kayla Reopelle (New Relic, Inc.)** 08:52 Big risk of conflicts.
Then it didn't quite… Makes sense, but…
**Robb Kidd (he/him)** 09:00 Yeah, the in use in code, it just was… They'd become…
**Hannah Ramadan** 09:05 So long.
**Robb Kidd (he/him)** 09:06 Yeah.
**Hannah Ramadan** 09:07 Yeah.
**Robb Kidd (he/him)** 09:10 Do we care?
I cared then.
**Kayla Reopelle (New Relic, Inc.)** 09:14 Yeah, yeah.
Good question.
Because I also don't think we're often using the constants in our instrumentation. We have, like, mixed support for whether we're using the constants or just strings.
Which… At some point, maybe we should… Decide about.
**Robb Kidd (he/him)** 09:36 I continue to think that with the turmoil that the semantic conventions gem causes.
that other languages don't have the dependency problem of you may only have one version of a gem in some.
**Kayla Reopelle (New Relic, Inc.)** 09:51 Hmm.
**Robb Kidd (he/him)** 09:52 Dependency graph.
**Kayla Reopelle (New Relic, Inc.)** 09:53 There's.
**Robb Kidd (he/him)** 09:54 There's a, I don't know, the anarchist in me says that the Semantic Conventions gem in Ruby should be a test gem, a gem that you.
**Kayla Reopelle (New Relic, Inc.)** 10:02 using.
**Robb Kidd (he/him)** 10:02 test environment.
To assert that you are using the correct strings at runtime.
And so in runtime, you could have bare strings, you could have your own constants.
But.
don't depend on the semantic conventions, gems, constants in runtime. If you, if you want to avoid dependency conflicts at some point in the future where two different instrumentations use a different version of the semantic conventions gem that are somehow incompatible.
**Kayla Reopelle (New Relic, Inc.)** 10:38 Yeah.
**Robb Kidd (he/him)** 10:39 It also, a philosophy of that would also sidestep all of the, do the semantic conventions, Jen, need to be backwards compatible? Because it's really hard.
**Kayla Reopelle (New Relic, Inc.)** 10:49 everybody.
**Robb Kidd (he/him)** 10:49 Then it's backwards compatible.
You just never delete them. That's how you make constants.
Right, right. So it just becomes a junk drawer of constants of past attempts at naming things.
**Kayla Reopelle (New Relic, Inc.)** 11:03 And by loading things just kind of by whatever module you're using, having a giant gem with all of the constants in it isn't as cumbersome, but… I'd be curious for any end users if they've been using the semantic conventions gem, and if they have any thoughts about this.
**Robb Kidd (he/him)** 11:22 That is, yes. I think we were channeling the end user in looking at the very long namespace of.
multiple modules of would the end user that we can imagine want to type all of this or even tab complete all of this?
**Kayla Reopelle (New Relic, Inc.)** 11:40 what.
**Robb Kidd (he/him)** 11:41 What kind of wreckage does it make in the code? And the readability of a code that's trying to just, it's just a string.
**Kayla Reopelle (New Relic, Inc.)** 11:47 Yeah. Yep.
So maybe, maybe it's a conversation, too, that we bring into the Slack channel. I know Bart has used this term, because he had a recommendation for changing the way that we require things.
Okay.
So we could tag him, and just see if anyone else responds to… Cool.
Any other thoughts on this one?
**Robb Kidd (he/him)** 12:35 We'll comment. I don't know about the module namespacing, but I think, Hannah, thank you for pointing out that latest comment. I think that is…
**Kayla Reopelle (New Relic, Inc.)** 12:44 Yeah.
**Robb Kidd (he/him)** 12:45 James was talking about with the module namespacing.
lowering the… Possibility of name conflicts.
Hmm.
**Kayla Reopelle (New Relic, Inc.)** 12:59 Okay, so for this one, You know, James has been doing some work towards consolidating The proto and common gems. Let's see if there's any.
No other comments at the moment, so… Centralized encoding… We'll be in the next release.
It's looking for implementation feedback.
on the common HTTP client.
I guess we could just Pause here for a moment.
So I think historically, there was… An experiment to break?
the exporters into HTTP and GRPC But it wasn't fully tested, and so it was just kind of around, but that has been confusing for some people who think that there is a GRP expert, but it hasn't actually been.
released.
now that we have started to make some structural changes to our OTLP exporters, and I think we also have Far more exporters than we did when the last time that was drafted.
I'm wondering if things are becoming more… complicated. It looks like this is… adding… like, a common gem, maybe just for HTTP stuff, but is it adding anything else as well?
Okay, and then it's also… Adding an OTLP HTTP gem.
that… Only emits traces.
And then it looks like it's just updating the logs and the metrics to use the new common… file… Yeah, okay, so… More gems, more abstraction.
What do folks think about this?
**Robb Kidd (he/him)** 15:22 is There's more gems… The thing that… We've decided we want.
To solve a problem?
Because I see that this PR is linked to the issue 2070, opened by Xuan.
And so the James's Pr. Is says that it is in service to this.
So I guess it's… does this PR… Address this thing, or progress.
Towards a solution for this thing.
**Kayla Reopelle (New Relic, Inc.)** 16:00 Yeah, Sean, my understanding of this initially was just to… Make it so we didn't have multiple proto-dependencies in different gems that were causing conflicts.
And just try to have the protos in one spot, but I feel like it's getting… Expanded upon, and I'm not sure more gems is going to make things easier to maintain, or necessarily a better interface for users.
But I could be.
missing something, xuan, do you think this still aligns with your initial goal, or what do you… Think about this proposal.
**Xuan Cao** 16:38 Alright, oh, yeah, I think my initial… Our request is just, not having separate portal.
To have one… Although I don't know what kind of approach we should take to make that happen.
Having a single… place like a gem or bring to the common headed portal and then all other exporter to use that as dependency.
was my, initial, thought, but, I haven't looked at, his PR Particular for this… Issue, so I don't know what… He down so far.
**Robb Kidd (he/him)** 17:25 I will say that other languages do have a lot of different exporter packages.
**Kayla Reopelle (New Relic, Inc.)** 17:30 not.
**Robb Kidd (he/him)** 17:31 not prior art.
thank you.
**Kayla Reopelle (New Relic, Inc.)** 17:39 Yeah.
**Robb Kidd (he/him)** 17:39 I keep coming back to the perennial question of what problem are we solving?
**Kayla Reopelle (New Relic, Inc.)** 17:44 Yeah, I think the centralized encoding is… is one… Problem to solve that it seems like we might be making some progress on?
But I'm not sure… Maybe I'm missing… Why we need to rename all these gems and add some new ones.
I guess this is the other open proposal for GRPC, if we're going to think about… Expanding that.
I'm just… I'm not sure we're ready for this level of bundling, since metrics and logs are still… in development. I don't know if this is adding… But it's also not my focus, so maybe I'm missing something.
**Robb Kidd (he/him)** 18:41 Yeah, and this is the first time I've been looking at this, so I don't have a… well-informed… I don't have an opinion, much less a well-informed opinion.
**Kayla Reopelle (New Relic, Inc.)** 18:54 Yeah, I haven't looked at this one yet either.
Well, I don't think… I think these are pretty big questions that we don't necessarily have the answers to right now, so, maybe the goal this week is just to take a look at those PRs, and… Yeah. Some comments on the issue?
Okay, cool.
Before we move forward out of core, any other… points, Yes, we do have a bunch of… Gems that are getting ready to release.
We've had, like, all of these awesome PRs open for spec compliance, so thank you for that. I think Some of them have comments that are waiting feedback, so… Take a look if you can. The… the question that I had added initially was, something that I think I'll just chat with Matt.
Offline about. But, basically we locked… the metrics.
API and logs packages to three decimal places because of… Some of the breaking changes we introduced to allow meters and tracers to be in instrumentation base and solve a problem that we had with proxy meters and loggers.
But I'm not sure if we need all three places. It'll just make things a little stickier with releases, which isn't necessarily a bad thing. It's just… Something I didn't… fully comprehend until… That release PR opened.
All right.
Yeah, so… We chatted a little bit about metrics and instrumentation last week, and… I looked at the last.
few metrics… implementations that we've had. I think we have this PR open, or, you know, something to add this metric open in a few different places.
But now that we have the meter actually.
like, distributed from base, I thought I would try it again.
So, this is more just, like, a request for review.
With a quick overview of some things that could potentially.
B design questions to contemplate. Looking at a lot of other instrumentation, it does seem like metrics and spans are pretty well integrated into the same pieces of code, and not usually separated too much, so that's.
The step that's taken here,
**Robb Kidd (he/him)** 22:18 Like, the metrics code path is not a totally separate code path.
**Kayla Reopelle (New Relic, Inc.)** 22:21 Exactly, yeah. Like, it wouldn't be in its own module that's just for metrics, like, usually in metrics and logs.
Seem to be assigned in the same place.
Even though, you know, it is calculating its own direction. Go ahead.
**Robb Kidd (he/him)** 22:37 Well, and which makes… to defend that, it makes a certain amount of sense, certainly, in our instrumentation, which has a whole lot of, like, we're gonna go put hooks and things.
Monkey patching, or prepending, and… Having different things in the gem.
Put its patches in, depending on whether you're doing Yeah, I agree. Especially if what happens in there is, like, a no-op, if you don't have metrics installed.
or if we're calculating roughly the same. I'm thinking in my case, with the queue latency recorded.
**Kayla Reopelle (New Relic, Inc.)** 23:14 either.
**Robb Kidd (he/him)** 23:14 attribute on a span or as a metric. Well, you're going to do the math anyway, so do the math and then condition.
**Kayla Reopelle (New Relic, Inc.)** 23:20 Yeah.
**Robb Kidd (he/him)** 23:21 Do the other stuff. So, sure. Yep. Yes.
**Kayla Reopelle (New Relic, Inc.)** 23:24 So, you know…
**Robb Kidd (he/him)** 23:25 Long way of agreeing, yes, mixing together.
**Kayla Reopelle (New Relic, Inc.)** 23:28 That's great. Yeah, I guess, like, you know, if we're gonna nitpick, like, this process clock get time assignment is not going to be applied in span land. There are things we should add to spans, like capturing, I think? I forget what it was, there was some kind of error… Attribute that we were missing, but.
So there's a few assignments that aren't necessarily SPAN-related, but I think it's all small enough that it shouldn't be a problem for SPAN users.
who aren't also metrics users.
**Robb Kidd (he/him)** 24:01 Yeah.
**Kayla Reopelle (New Relic, Inc.)** 24:01 Yeah, and then tried to… bring some things into the shared HTTP helper module.
To keep stuff directly out of the patch as much as possible, so just… Basically, creating the metrics attribute hash, which is similar to what we're doing for Span attributes as well.
And metrics also cares about the success range, so moving that into…
**Robb Kidd (he/him)** 24:31 Sure, yeah.
**Kayla Reopelle (New Relic, Inc.)** 24:32 That makes sense.
Let's see, what else?
Yeah, bucket, like, actually just defining the metric, whatever the metric is, in the instrumentation RB.
File as an instance.
variable, with a reader that can be called on in the instrumentation, so… We can just kind of see… The metrics and any of their advisory parameters in that same place where we think about, like, installing and initiating instrumentation.
So that's the gist. There's also some tests that… you know, make sure it's not running in cases where it shouldn't. So, this is making the assertion that we should only be adding the metrics to the stable instrumentation, and not to duper old.
And… stable conventions, that is. So, yeah, and then adding a special appraisal to make sure that metrics is installed and things work with metrics when it's present.
But not forcing that to be in all cases yet.
Hmm.
**Robb Kidd (he/him)** 25:38 Okay.
**Kayla Reopelle (New Relic, Inc.)** 25:39 So yeah, so those are some of the ideas. And so…
**Robb Kidd (he/him)** 25:42 And so this was… that was the, comment on, is this how we want to… Yeah. Bring metrics into instrumentation.
**Kayla Reopelle (New Relic, Inc.)** 25:51 Yes, because I would love for us to just decide on a pattern and a process so that we can start getting metrics out in more places. So it's not a question, like, for your Sidekiq implementation. Where do we define the metric? How do we define the metric? Does it live with spans? Does it not live with spans? Those are all questions that have come up in the past when we've tried to add metrics to instrumentation, so… Okay.
**Robb Kidd (he/him)** 26:13 I'll review that. That all makes sense in the skim that we just did, but I'll look at it more closely.
**Kayla Reopelle (New Relic, Inc.)** 26:19 Thanks.
Well, let's see… All right.
**Robb Kidd (he/him)** 26:28 But then I snuck my sidekick.
**Kayla Reopelle (New Relic, Inc.)** 26:29 Yeah.
Go for it.
**Robb Kidd (he/him)** 26:32 Well, so you and James had both commented, I think.
Yes, I accept, several of James's comments.
The proposal… we've been asked for this forever, since, like, 2021. Could… could… Two things. Could the timestamps That we record as span events. When a job gets created, when a job gets pushed onto the queue.
We record them as span events, because that's what the spec says we do with things that happen in a point in time. But span events cause trouble for some back ends.
And most of the time, people just want to do the math on how long something sat in a queue, rather than know the very specific time that it was in queued at. It's like.
Knowing when a job was created and when it was enqueued are, like, the ingredients to compute a latency queue time.
Or, queue latency, duration.
So, this is my pitch to, like, yes, after, what, 5 years of saying no to people, let's say yes. And do it conditionally, so the proposal's two new options.
The option names are sort of awkward, but I think would read semi-fluently in a… in… in a… config, times… job timestamps as events, or as attributes, or as both. That one reads a little awkward, but if somebody's got better names for the options, I'm open. I'm not wedded to these things, but… The first option is about how do you want the timestamps for the job creation and job being enqueued. Events is the current behavior. You could choose to do attributes instead, and we would not create the span events, or you could get both if… if you want the… All you can eat plan.
And then the second option is We're right there. We're a… we are a subtraction operation away from computing the job latency for you. So some backend doesn't have to do it, some passing these spans through a collector for the collector to do the math doesn't do it.
So, proposing to just compute the job latency right there, which is another feature that we've thought about and said no to in the past, but at this point, I got another request from two other Honeycomb customers for this, and I think it just makes sense to let people do this.
Especially since there's a prior art session. There's been interest for a while, is my little… Survey of the history of it, this feature being asked for, and then other instrumentations do it.
We've been a stickler about the spec, saying we shouldn't record timestamps as attributes, those are point in times, there should be span events, and… metric… metrics should be recorded as a metric, not a span attribute, and I'm like, you know what, other job… other instrumentations do it, so why don't we? It… it solves a problem for people.
I'm game to, with… Gosh.
I was gonna say I'm game to make the… Job latency.
option default to the metric, except that then it's a no op unless you install the metric gem.
Because I agree with Ariel's point in the past when the latency metric as an attribute has been brought up is that metrics should be metrics. And I agree with that as written by the spec.
So I guess I could attempt. I guess I could attempt. I could also do this in different phases, where part 1 and part 2 on this proposal don't have to happen in the same PR.
if we want the default to be metric.
And adding metrics is… complicated right now.
Part 2 could wait.
Which sort of makes me sad, because it's really… the number's right there, but if I implement it today, the default would probably be attribute, and then if we change the default in the future, we'd surprise people.
**Kayla Reopelle (New Relic, Inc.)** 30:35 Which, which could be done as, like, you know.
Whatever point in time we get.
stability for this instrumentation, you know, when metrics is stable, or emitting only the stable convention, something like that.
I guess both could be… is both a weird default, because you're really only getting attributes unless you install the metric.
I don't know.
**Robb Kidd (he/him)** 31:00 Well, we can make the default metric.
We can make the… in thinking out loud, we can make the default metric If I implement this as modeled off of what we had just talked about with the HTTP instrumentation and adding a metric.
**Kayla Reopelle (New Relic, Inc.)** 31:15 The.
**Robb Kidd (he/him)** 31:15 Default could be metric, but it's no op unless you add the metric gem. And maybe that's okay?
Because then there'll be a future at some point where maybe the metric gem is present by default? Is that a future?
**Kayla Reopelle (New Relic, Inc.)** 31:31 Yeah, so, I mean, a possible future is that once metrics and logs are stapled… stable, the, OTLP… not the OTLP, the metrics… OpenTelemetry SDK gem includes all of the signals.
And we…
**Robb Kidd (he/him)** 31:48 And then it's on the operator to decide which ones are on or off.
**Kayla Reopelle (New Relic, Inc.)** 31:52 Yes, yeah, that's something that the metrics-enabled method, I believe, controls. That's the preferred pathway in declarative configuration, and I think also programmatic configuration, is that you, like, disable the meter when you don't want it, rather than turning off metrics altogether.
**Robb Kidd (he/him)** 32:14 Well, I'm game to, I can update this proposal to say that the default for the latency metric is a metric.
And…
**Kayla Reopelle (New Relic, Inc.)** 32:22 and.
**Robb Kidd (he/him)** 32:22 Note that… It will be no op unless you add the metric for the foreseeable future, the metric gem for the foreseeable future.
**Kayla Reopelle (New Relic, Inc.)** 32:30 Yeah.
I think that makes sense.
**Robb Kidd (he/him)** 32:34 Also, Okay.
**Kayla Reopelle (New Relic, Inc.)** 32:36 Oh, go ahead.
**Robb Kidd (he/him)** 32:37 I was going to go into the open questions.
**Kayla Reopelle (New Relic, Inc.)** 32:40 Yeah, yeah.
**Robb Kidd (he/him)** 32:41 One comment, actually, if you scroll up a little bit to the job latency, the attribute and the metric, James raised the good point that the job latency For the metric is a second.
I put milliseconds, because I think, actually, in queue times and milliseconds, so my bias came out in my proposal for the attribute, and saying milliseconds, which I acknowledge is an inconsistency, because.
I said that I'm going to do job latency as a histogram in seconds, but if you ask for the attribute, milliseconds. James appropriately went, maybe it should be seconds.
So I will change that so that the job latency will be seconds, but as a float rather than an integer.
And then the names for the attribute and metric. I think you and James both said, how about we drop the messaging.
the namespace messaging and just call it Sidekiq and… And, and exist under the, What was it? Vendor specific naming conventions.
**Kayla Reopelle (New Relic, Inc.)** 33:43 you Yeah.
**Robb Kidd (he/him)** 33:45 does mean that some of the attributes coming out of this… if I add these attributes as sidekick. and not messaging sidekick, it will differ from all the other attributes that this instrumentation currently emits.
**Kayla Reopelle (New Relic, Inc.)** 33:58 Right.
**Robb Kidd (he/him)** 33:59 Now we have, like, a migration thing of… What do we do about… all.
**Kayla Reopelle (New Relic, Inc.)** 34:07 Yeah, yeah.
**Robb Kidd (he/him)** 34:08 We currently put out.
**Kayla Reopelle (New Relic, Inc.)** 34:10 Because I think we could argue that the semantic conventions we currently have for Sidekiq instrumentation are perhaps different from what a stable convention would recommend.
I, because Sidekick falls into this weird, like, middle ground where the.
**Robb Kidd (he/him)** 34:27 SIG.
**Kayla Reopelle (New Relic, Inc.)** 34:28 Conventions don't seem to want to accept it, so it's, like, in this… It's.
**Robb Kidd (he/him)** 34:33 Messaging SIG doesn't want to accept job processing names, so…
**Kayla Reopelle (New Relic, Inc.)** 34:37 Yeah.
**Robb Kidd (he/him)** 34:38 They keep punting on, like, nope, that's not messaging, so…
**Kayla Reopelle (New Relic, Inc.)** 34:42 you.
**Robb Kidd (he/him)** 34:42 All of us people trying to instrument.
background job work.
Are on our own.
**Kayla Reopelle (New Relic, Inc.)** 34:51 Yeah.
**Robb Kidd (he/him)** 34:52 So we keep bunting.
**Kayla Reopelle (New Relic, Inc.)** 34:53 Yeah.
**Robb Kidd (he/him)** 34:53 specific stuff.
**Kayla Reopelle (New Relic, Inc.)** 34:55 So… I mean, we could consider adding this as a part of an OTEL SEMCOM stability opt-in endeavor, where if we're gonna call some of these things just Sidekick, they only exist on whatever stable future we're marching towards. But that would require some extra documentation, where we make a choice about what those attribute names look like, and what semantic conventions bucket they're gonna live in. And… just have that documented somewhere. Since it seems like the greater SEMCOM SIG is kind of, like, raising their hands up with this type of a thing.
We do have a Ruby namespace now in Semcomp, so we could define things there, or… open up some kind of vendor-specific documentation. But again, it's like, is it… I've noticed that when we have a prerequisite to try to get something defined in semantic conventions, things usually fizzle out and die, and so I would like to make sure that this can be seen through, And we could potentially take an… implement an undocumented approach instead? I… I don't know, but that's… that's another… just concern about…
**Robb Kidd (he/him)** 36:15 I guess it's… would this group… would this group want to go to sidekick.job as the namespace that we put Sidekick.
Attributes and and and metrics under.
And then, like, the implication there is, like, ActiveJob would have active job or rails.active job, which I know is another PR that's open. I think I linked to it.
I think I linked to it in the open questions.
**Kayla Reopelle (New Relic, Inc.)** 36:46 Okay.
Yeah, this one.
**Robb Kidd (he/him)** 36:55 So this was James's, sort of.
So naming… normalization proposal back in May, about Getting out of messaging and just putting it under rails.
Sidekiq isn't Rails.
**Kayla Reopelle (New Relic, Inc.)** 37:13 So.
**Robb Kidd (he/him)** 37:13 So, in aligning the two, Job Runner tools that we're attempting to instrument.
Rails Active Job makes sense for Active Job, and I think just Sidekick makes sense for Sidekick?
Unless we wanted to put it under ruby.sidekick?
**Kayla Reopelle (New Relic, Inc.)** 37:34 Yeah, which I think feels a little weird for some reason. I mean, like, Sidekiq… I think Sidekiq has implementations in languages that aren't Ruby.
**Robb Kidd (he/him)** 37:46 Yeah.
**Kayla Reopelle (New Relic, Inc.)** 37:47 I know it's, like, primarily… or I believe it's primarily used by Ruby, so…
**Robb Kidd (he/him)** 37:52 Reach out to Mike Purim and say, what would you like?
**Kayla Reopelle (New Relic, Inc.)** 37:54 You were.
**Robb Kidd (he/him)** 37:55 Semantic convention names to be, and he's like, what?
**Kayla Reopelle (New Relic, Inc.)** 37:57 Yeah, yeah. I mean, he's aware of us, so we could… yeah, I think that could be an interesting… The side quest.
**Robb Kidd (he/him)** 38:08 Joseph, you want to reach out to Mike? Say, like, we're gonna try and come up with semi-official names for describing things.
I'd even be okay if his response is, well, look at the Sidekick metric stuff that already exists.
**Kayla Reopelle (New Relic, Inc.)** 38:24 Useless.
**Robb Kidd (he/him)** 38:29 alright, so I think the blocker here is deciding what we want to name things.
**Kayla Reopelle (New Relic, Inc.)** 38:35 we're.
**Robb Kidd (he/him)** 38:35 I think I could still put up a PR and have within the insurance.
I could, oh God, I could do so many things in this. I could demonstrate what an instrumentation owning its attribute names as constants within the instrumentation gem itself looks like.
**Kayla Reopelle (New Relic, Inc.)** 38:52 Whew!
**Robb Kidd (he/him)** 38:54 Since none of these are semantic conventions, like, it's…
**Kayla Reopelle (New Relic, Inc.)** 38:58 you.
**Robb Kidd (he/him)** 38:59 There's no constant from SEMCOMS to use here.
It's kind of our problem.
I could… I could say, here's what an instrumentation that wants to, like, own its destiny, and not be beholden to constants from outside.
Looks like.
And then when we… and then it's draft until we decide, like, with some input from Mike, and… Looking at both the active job update and the sidekick update, what kind of internal conventions do we want to follow?
I can do that. If the rest of this seems to hang together, I can do that.
**Kayla Reopelle (New Relic, Inc.)** 39:36 I think so, I think there's enough people who have wanted it and especially now that there is.
you know, ex… Other…
**Robb Kidd (he/him)** 39:44 else's.
**Kayla Reopelle (New Relic, Inc.)** 39:44 instrumentations. Everybody else is doing it. I mean, that's often our excuse. Like we are very much the followers peer pressure.
**Robb Kidd (he/him)** 39:52 What are conventions, but what everybody else is doing?
**Kayla Reopelle (New Relic, Inc.)** 39:55 Yeah, yeah, so I think… I think it's time, and we are also… having a pathway for metrics now, so I, you know, I think we can even answer that question.
Cool.
**Robb Kidd (he/him)** 40:10 So I think what I'll take away from this, and I'll update the proposal afterwards, because I type slow, because I have a new keyboard.
I'm gonna update, like James had said, I'm gonna update the units for the job latency time to be consistent with seconds. It'll be recorded as a float. I will, let's see what it looks like to make the default for the job latency Come as a metric.
And we'll document.
To get that, you're going to need the metric gem, like so.
But then there's the attribute path or both paths available.
And… And I will, make constants for whatever the attribute and metric names will be, so that we can easily update them when we decide what they ought to be.
**Kayla Reopelle (New Relic, Inc.)** 40:53 haha.
**Robb Kidd (he/him)** 40:55 Okay.
**Kayla Reopelle (New Relic, Inc.)** 40:55 Sounds good. I think the only other thing I would add… this is something I haven't investigated, but I saw James commented on it, is to make sure that these options make sense in a declarative config context. I think we're gonna have to do, like, a decent revamp of our.
**Robb Kidd (he/him)** 41:12 Oh, like that.
**Kayla Reopelle (New Relic, Inc.)** 41:14 and.
**Robb Kidd (he/him)** 41:14 Yeah, okay.
**Kayla Reopelle (New Relic, Inc.)** 41:16 Yeah.
**Robb Kidd (he/him)** 41:16 How would you declare these options in declarative config?
**Kayla Reopelle (New Relic, Inc.)** 41:20 Yeah.
**Robb Kidd (he/him)** 41:21 what do they look like there, too? Okay. Exactly.
**Kayla Reopelle (New Relic, Inc.)** 41:23 Yep.
**Robb Kidd (he/him)** 41:24 I guess I didn't understand what… his comment, what change I should make to address that comment.
**Kayla Reopelle (New Relic, Inc.)** 41:30 Yeah, let's look again.
**Robb Kidd (he/him)** 41:34 So… If we instead had options to opt in to adding the attributes to the span, and had a separate option to enable the metric, which… I thought…
**Kayla Reopelle (New Relic, Inc.)** 41:44 Yeah.
**Robb Kidd (he/him)** 41:45 There are two options. One is to add attributes to the span, and the other is.
**Kayla Reopelle (New Relic, Inc.)** 41:50 I think… Oh, that's right, it's not in their repo anymore.
My… my vague recollection right now, without looking anything up, this is the wrong one, is that declarative config might scope Configs and instrumentation by signal.
**Robb Kidd (he/him)** 42:11 Oh.
**Kayla Reopelle (New Relic, Inc.)** 42:12 Maybe that it's, like… Sidekicks, fans, do this thing, sidekicks.
**Robb Kidd (he/him)** 42:17 I will go…
**Kayla Reopelle (New Relic, Inc.)** 42:17 do this thing.
**Robb Kidd (he/him)** 42:18 I will go, I will go and catch myself up on Instrumentation declarative config, and… adjust accordingly.
**Kayla Reopelle (New Relic, Inc.)** 42:28 Okay, great, thanks.
**Robb Kidd (he/him)** 42:30 Cool. I should write this down.
**Kayla Reopelle (New Relic, Inc.)** 42:33 I think… I think we got a… probably a robot transcription, I don't know at this point.
**Robb Kidd (he/him)** 42:39 Okay, great, thanks very much.
**Kayla Reopelle (New Relic, Inc.)** 42:40 Yeah.
Okay, cool. That takes care of everything, since I'm going to take that one on Slack.
For anyone who's here today, anything else you want to add on the agenda?
All right.
Feel like there are enough.
issues and PRs open right now that we could probably spend the 15 minutes looking at those.
So… Yeah, I think that's… that's gonna be my preference, unless… anyone wants to talk about anything, I'll give a moment of silence for you to chime in.
Great. Okay. Well, thank you everyone for coming today, and yeah, please, please take a look at the things in the agenda if you have some time.
And regardless, I will see you all next week!
**Robb Kidd (he/him)** 43:52 Okay, thanks so much. See you, everyone.
**Kayla Reopelle (New Relic, Inc.)** 43:54 Bye.
