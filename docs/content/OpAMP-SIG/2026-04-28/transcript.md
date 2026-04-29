SIG: OpAMP SIG
Date: 2026-04-28
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Evan Bradley** 02:44 Hi, everyone.
**Andy Keller** 02:49 Hey, And how are you?
**Evan Bradley** 02:51 Doing alright, how are you?
**Andy Keller** 02:53 Dude.
Now, should we get started?
**Evan Bradley** 05:14 Let's do it.
**Andy Keller** 05:16 Dakota, the first thing on the agenda?
**Dakota Paasman** 05:18 Yeah, Yeah, so, just thinking a couple of PRs here, that I have open against the supervisor.
They're in need of… some review. Evan, I think you probably… You reviewed both of them once before.
I think they're ready for… Your look again?
But if anyone else wants to take a look at them as well.
Hmm… Yeah, that's all I had.
**Evan Bradley** 05:51 Yeah, I'll take a… I'll try and take a look, hopefully later this week. I'm a little swamped, and a lot of the op-amp stuff has kinda fallen a little bit down on my to-do list.
**Dakota Paasman** 06:00 That's fair.
Yeah, whenever you, yeah, whenever you take a look.
Greatly appreciate it. But that's all I had.
**Michel Laterman** 06:15 Alright, so I've got the next one, my Pure just changes how… Connection setting statuses are applied.
My initial implementation was… Trying to use the, op-map code library to do everything automatically, but I forgot that.
We use asynchronous calls, so… it pretty much broke immediately, and this is a PR to correct that, and it's… Now, something that changes the behavior of… How they're gonna be used, so… Having a few other people review it would be, good.
**Andy Keller** 07:03 Okay.
Great, thanks for mentioning it, I haven't…
**Michel Laterman** 07:06 Nope.
**Andy Keller** 07:07 I missed this, but I'll, we'll take a look.
**Evan Bradley** 07:15 I'll try and include this in my PR, sweep that I'll hopefully do, within a week here as well.
I see that you pinged me on this.
**Andy Keller** 07:29 Okay, I have the next one. I really just… mentioning that… We created a new exporter, Called the op-amp exporter.
And, it solves a… use case, I don't know how common it is, or how interested other people would be in upstreaming this, but that's partly why I wanted to raise awareness.
And see if there's interest. Basically, what this exporter allows you to do is send OTLP data via custom messages.
up the op-amp connection, so that if you… want to collect telemetry from the agents via OpAMP, you can do so using the existing WebSocket connection without creating a second, OTLP you know, previously we were using the LTLP exporter.
And then had an OTPL endpoint in our platform, and so if we wanted to send some data, we would send it over OTLP, but that requires An extra connection, To the back end. We already have the op-amp connections, this allows us to reuse the op-amp connection.
It's really simple, it just grabs the… Custom message registry from the op-amp.
Extension.
And then sends… whatever OTP… OTLP data.
Comes in the pipeline up, up over a custom message.
It's not intended to be used for routing, you know, real telemetry.
You know, I wouldn't suggest using this with… High throughput pipelines.
Our use case is more for… scraping local Prometheus metrics, very targeted, and, things like CPU and memory and… exporting those.
Up the op-amp connection, so… Think of, like, you know, either telemetry about your telemetry, You know, self-telemetry, our own telemetry.
Or, you know, very targeted pipeline for… collecting data Happy to answer any questions.
Just curious, if anybody… Has any interest in this, or a use case?
**Evan Bradley** 10:01 Looks good to me, nothing from my end, Looks like a good implementation. I think the key motivator, from my perspective anyway, is reusing that connection, which it sounds like is the same for you, right?
**Andy Keller** 10:14 Yeah.
**Evan Bradley** 10:14 So, I guess if we take that upstream, I think that'll be the… just the important piece.
**Andy Keller** 10:21 Yeah, yeah.
clear intentions on why we should do it. There was talk, and I wish Tegan were here, to get his input, but of potentially… Adding… An OTLP payload to the agent-to-server message.
We never did that.
Still could do it, but that was also before we had custom messages.
This exporter actually allows you to specify what the custom message capability and message type are, so… In theory, if you had multiple exporters, they could have multiple Capabilities, or multiple types, and it's really kind of… Up to the implementation, how that data is used, and how you would… Segment it.
but… But yeah, so there isn't… I don't… I don't think it necessarily needs to be built into the protocol.
but… I do know that the topic came up, there may even be an open issue.
From years ago, discussing it.
**Evan Bradley** 11:39 I don't know, I'd have to think about that. I mean, for now, I think custom messages are a great way to do it.
I guess I'd want to see from Splunk, probably, whether that's… or any other, any other provider, whether that's something that's, like, a common use case, or… If it's just, you know, kind of a one-off here.
**Andy Keller** 12:00 Yeah.
Cool.
**Evan Bradley** 12:11 Douglas.
**Andy Keller** 12:12 silence.
**Douglas Camata** 12:15 Yeah, so I'm also just, wanting to, to put, two, two PRs in evidence that I have pending and need reviews.
the startup fallback config one, which has been… is already having the new name. I heard, you, Evan, that you're gonna do a review spree soon, so… I'm, I am, waiting for that.
But, yeah, I understand it takes time, because… There's a lot of stuff going on. The second one is a new one, which is related to some of the things that we discussed in KubeCon EU in person, which is… a change so that the supervisor, when it fails to apply a remote configuration, it just restarts and keeps running with the previous working configuration that it had. So I do a little… a little tracking of when… when the collector reports to the supervisor that it is healthy via their own internal open communication, I persist that, the… the last applied remote configuration as a kind of known-to-be-working remote configuration.
And then, in case a new remote config comes and fails to apply, I just restart the collector with that.
With that working configuration, and as you will find in the description of the PR, I intentionally do not report any Config status for that remote configuration.
That was a decision that I made based on what I understood from the OPAM spec, that the status should be reported for the last received remote configuration, but let me know if you disagree with that, because that was just a decision that I had to make, and…
**Andy Keller** 14:16 Sounds reasonable.
**Douglas Camata** 14:18 Okay, okay. Yeah, I'm also fine if, you know, someone disagrees and we come to the conclusion that we should report an applied again for that configuration, but… It would be the responsibility of the open backend for now to realize that that config failed, and it should not send it again, maybe without changes, or without maybe trying a restart, or… Up to the… to… to the implementation of the backend.
So yeah, waiting for reviews on this too, and that's… that's, all from my side.
**Andy Keller** 14:58 Are you, are you persisting… persisting that remote?
previous remote config.
So that it survives restarts and things.
**Douglas Camata** 15:08 It will survive restarts, yes, yes, if you… if you are, for example, in an EC2 host, or any other virtual machine, it will survive restarts, right? And then if you are in Kubernetes, you would have to Have some kind of… shared volume there for each pod, so that's more complicated, but for more simple scenarios, like VMs, it will persist across restarts. And if… so if the… And if the supervisor restarts, it will… when it starts again, it will see, like, hey, I… there is this file with the… last… Working remote config, and it might also have the effective one.
Right? It will try first the effective.
if I recall correctly from my PR, I think, I think I must have written something there about it.
If I didn't, I will probably recheck and make it clear, but it should… It should use the… You should use the last working, right? It doesn't make sense to start with a failed again, or it might make sense to start with a failed again, because, right, in case… Potentially in.
**Andy Keller** 16:32 Okay, zoo.
**Douglas Camata** 16:33 Get a restart command.
But that would restart only the collector, right?
So…
**Andy Keller** 16:40 I guess it really depends… I think it depends on how… you know, what's triggering that restart? I mean, it could be an upgrade, for example, and the upgrade could be the thing that fixes the configuration.
**Douglas Camata** 16:51 Yeah, yeah, I will double-check this one, because I think that's a good point, and I would say that… A restart of the… if the supervisor is alive and restarts the collector, it should restart It should be… that's a good… maybe if the collector restarts, it should restart from the last working?
But if the supervisor restarts, it should potentially restart from the less effective.
That's a good…
**Andy Keller** 17:26 Yeah, I think it's… I don't know, maybe, Dakota, if you've… If you've got some time, if you could review this and also compare it to our implementation.
We do this in our our collector and our op-amp implementation. I remember at KubeCon, I was convinced that we also did this in the superfinder.
**Douglas Camata** 17:44 I remember this from our conversation. I also put this feature behind a small configuration option, so that we can… We can… we could merge it if we are all happy with the… the initial implementation and the behavior, and the… I am interested in using that as soon as possible, and if others are, and we discover by user feedback that, oh, it's better to change the behavior, maybe we could document it as experimental, and we leave the flag there off by default.
And, eventually, this would give us some freedom to change behavior if we realize that a change is needed.
**Dakota Paasman** 18:32 Yeah, I can definitely take a look at the PR, and not to hold up this PR for merging in the event that, you know, we all like it and approve it. One of the extension PRs I'm working on is adding the idea of feature gates to the supervisor, and I think… Instead of a config flag using a feature date for this behavior would be pretty cool.
**Douglas Camata** 18:57 Yeah, yeah, because I think it keeps it safer in terms of being experimental, maybe less.
**Dakota Paasman** 19:03 Yeah.
**Douglas Camata** 19:04 So we'll… we'll try it out, and not… not expecting there to potentially be breaking changes in… in… in behavior, especially.
**Dakota Paasman** 19:14 Yeah.
**Evan Bradley** 19:16 At a minimum.
**Dakota Paasman** 19:16 Yeah.
**Evan Bradley** 19:17 Oh, I was just gonna say, at a minimum, it's kind of making them sign a waiver. That's typically how we treat it, is you have to opt in, and if it breaks, that's on you.
**Dakota Paasman** 19:28 Yeah, so this might be… it'd be cool to get the feature gate stuff in, and then you can… Switch this over to the future date on top of it.
But…
**Andy Keller** 19:38 Is it the, extension capability that has the feature gate?
**Dakota Paasman** 19:43 Yeah.
That introduces it.
But that shouldn't…
**Andy Keller** 19:49 It might make sense if for some reason that seems like that's gonna take a while to get in, it might make sense to… Factor out the feature… feature gate.
Implementation… And then build both of them on top of it.
But if we're pretty close to merging, then… It's probably good to just merge it and… And then rebase, who needs a feature date.
**Dakota Paasman** 20:11 Sure.
**Andy Keller** 20:13 since you?
**Evan Bradley** 20:14 We were… I think we were close… ish.
I'd have to see what other people say, but yeah, I agree, if, I need to take another look at it, but… I think if we're… If we're not close, then it should be fairly easy to extract.
And get in.
**Dakota Paasman** 20:32 Yeah.
**Andy Keller** 20:34 Okay.
**Evan Bradley** 20:34 I'll take a look, and anybody can feel free to review any of these PRs, it would help me before I click the final merge button on them.
**Andy Keller** 20:53 Okay, anything else?
Thanks, Douglas.
**Evan Bradley** 21:13 Nothing for me.
**Andy Keller** 21:14 Alright, great.
Huh?
See you next time!
Have a great rest of the week.
**Evan Bradley** 21:21 See, everyone.
**Douglas Camata** 21:22 See ya, bye-bye.
