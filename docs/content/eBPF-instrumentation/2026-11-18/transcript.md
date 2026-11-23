SIG: eBPF Instrumentation
Date: 2026-11-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Gregor Zeitlinger 00:01:10 Hello?
Mattia Mattia 00:01:15 No, no.
Giuseppe Ognibene (Coralogix) 00:01:17 Hello?
Roy Reshef (Kubex) 00:01:26 Hey, good, afternoon, morning, whatever it is.
Tyler Yahn (Splunk) 00:01:56 Hey!
Gregor Zeitlinger 00:01:57 Hi, Tyler!
Tyler Yahn (Splunk) 00:01:59 Hey, how's it going?
Gregor Zeitlinger 00:02:02 Good.
Tyler Yahn (Splunk) 00:02:44 Hmm… do you guys know if the Grafana folks are able to show up today?
Marc Tudurí 00:02:49 Not all of them.
Gregor Zeitlinger 00:02:50 very limited capacity, so, mark?
And…
Tyler Yahn (Splunk) 00:02:56 Oh yeah, there's Mark, yeah.
That's… Yeah, and then… yep.
Gregor Zeitlinger 00:02:59 But we have.
I hope we can still help.
Tyler Yahn (Splunk) 00:03:03 No, no, no, no, that's fine. I just wanted to know if we should wait or not. Sorry, yeah, I see you guys now, yep.
I was just looking at the attendees, Yep. Okay, cool. Yeah, well, we could probably jump in here in just a second, get started. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, go ahead and add them there as well, and yeah, I'll start sharing my screen.
Cool. Awesome.
Well, yeah, so… to start us off, Nimrod, you wanted to ask about turning off, target info, and adding configuration for it?
Nimrod Avni 00:03:53 Yeah, so… I… like, I'm working on adding OB to the semantic convention conformance repo, and I did some, like, exploring and stuff, and I saw that we emit the target info metric by default, and there's no way to turn it off right now. It's basically… For some reason, I thought it was an internal metric, but it's part of the application preset, which is… all the, like, span and met… and, like, I know HTTP metrics and stuff like that, and we have no way of turning it off.
So I'm trying to think, like, what's the best way to do it? Like, we can either have a specific Boolean under our config to turn it off, which is, like, another knob to metric selection, and we have this, like, capture metrics feature, which I think is the… Like, that's the place where we decide which kind of presets go in.
But… But there's no way to, like, say… I don't know… unless we decide to split this, like, target info into a separate feature, but then we break other, users that already emit it. So I'm… either we can do some, like, negative, you know what I'm saying, like, emit everything but target info? I don't know what the… best way to do it here, because I think a lot of users might want just… like, the application metrics, or, you know, stuff that follow OTEL semantic conventions, and this is something that, like, we kind of made up, or, you know, following a Prometheus kind of standard, but it's made it via OTEL, so… I'm not even sure a lot of people use it, so I just want to… Hear your thoughts on that.
Tyler Yahn (Splunk) 00:05:39 Yeah, I was a little confused on this as well, because I was just looking into this right before the meeting, and I thought you were just, like, talking about the Prometheus metric target info, and I was just like, oh, well… What was it?
Nimrod Avni 00:05:49 I think I… yeah, I think I talked about it with, Nicola, on, like, when we try to align the metrics between Prometheus and OTEL, and he said that it's probably still important to emit target info as an OTEL metric.
I think there's… I can't find… it's like an issue that we already closed.
I can find it… It's back…
Tyler Yahn (Splunk) 00:06:30 Yeah, it's not super critical, you can… we can find it later. I mean, I believe you, like, that it's there, and that, like, it sounds like it's there for a reason, that people may want it, so, But yeah, like… if that's the case, I was kind of just assuming that, like, okay, that's fine, like, we could do that. One of the things I was thinking is, like, because, like, features is, like, actually a list of, like, those application features, but, Man, why does it do this?
I mean, we could also just do, like, I guess it's already… And then do something like this, where it's like, you know, do, like, a Boolean there?
Does that make sense? Because then you can keep it out of here, because, like, this right… right now, right, like, target features, if I'm not mistaken, is, like,
Nimrod Avni 00:07:27 Yeah, it's like application and stats all the, like,
Tyler Yahn (Splunk) 00:07:30 Yeah.
Nimrod Avni 00:07:30 IP stats, network stats, all that stuff.
Tyler Yahn (Splunk) 00:07:34 Right, yeah, so it's like putting, like, a… you know, I guess you could do, like, applications, or… You know, without… Target info, but that.
Nimrod Avni 00:07:46 Yeah.
Tyler Yahn (Splunk) 00:07:47 that'd be awful, and then you gotta do that for, like, all these other ones, right? Like… So, I mean, I think, like, putting something here… Down, like, at the… Hmm… Like, at this, like, lower level, might… like, not… I'm sorry, not at the lower level, at the same, like, level as, like, this metrics configuration scope might make more sense, just as, like, a general Boolean.
But… It is, like you're saying, like, kind of like a one-off?
On that, I don't know if that's a good or a bad thing, though.
I mean, we would just default to true, right? Like…
Nimrod Avni 00:08:26 Yeah, yeah, to not, interfere. Not break it. Yeah, I think.
Tyler Yahn (Splunk) 00:08:30 Yeah.
Nimrod Avni 00:08:31 I think that makes sense.
Tyler Yahn (Splunk) 00:08:33 Okay.
I mean, that's…
Roy Reshef (Kubex) 00:08:36 Fit.
Tyler Yahn (Splunk) 00:08:36 as far as I came up with.
I'm just looking at it before this meeting, so I'm not 100% sure if there's a better place, but yeah.
Any other thoughts from folks?
Roy Reshef (Kubex) 00:08:50 Yeah, I can testify that someone actually uses these metrics.
I know I'm not a big fan of state metrics, and because it's a bit of abuse of the metrics model. You know, there's metrics with constant value 1, and maybe even con- not constant labels, but, like, fixed labels that don't change, but… there are… they are useful for all kind of use cases. If you have all kind of consumers that only goes to, you know, to the end storage, say, Prometheus, and needs to merge data from there.
So… It does have a value. I mean, yeah, you can add a config parameter to turn it off. If people don't care about them, that's not a problem, and I'm not the one that can tell you where it should be.
Nimrod Avni 00:09:40 Yeah, I think the, like, my main issue with… I didn't want to, like, do any major changes before that, but maybe we can think about it for, like, V2 or something, that's like… The… if you export, OTEL to the collector, and, like, the collector uses the Prometheus exporter, the Prometheus exporter will already produce this target info metric, because… I mean, because that's how, you know, you produce kind of resource attributes to Prometheus. And also, our Prometheus exporter does this, but using the OTEL exporter on OB to produce target info seemed kind of weird to me. It's something that we had from a while back, so I kept it.
And so maybe I'm not super sure of the, like, how… what's the value here, because if you… if it ends up being in Prometheus, either Obi or the collector will produce it, but any, like, hotel metric engine.
won't usually benefit from it, I think.
so that's why I… at least I want to have an option to turn it off, but maybe we can think about it, like, maybe someone, I don't know, maybe, I think Nicola.
if he… I can sync with him later, maybe he has some… You know, better opinions on that.
Tyler Yahn (Splunk) 00:11:02 Yeah, I was kind of confused. I mean, obviously, like, that's why we developed resources in Hotel, was to avoid all these kind of things, right? So, like, if I remember the conversation, which I don't really, but it was something to the effect of, like, some people aren't able to process resources or something like that, but, like.
Again, like, I think, like, even if it was a V2, it'd be, like, an opt-in feature would be a little bit… More preferable, given it's, like, not the standard, but, like.
Yeah, that's… that's fine. I did add a item in the agenda to just track an issue… track this, like, or, like, looking into removing it with the V2. Nimrod, could you create that issue?
Nimrod Avni 00:11:38 Yeah, I'll do it.
I think we can maybe even, like, I guess we need to talk about it more, like, a lot of, configs, which I think a lot of people are using, maybe we can, like, push them to be the defaults in V2, it could be… but that's a different discussion.
Tyler Yahn (Splunk) 00:11:56 Yeah, I mean, and like, even our… Like, obviously, like, the default needs to remain for backers compatibility, but, like, our examples can just show that, like, you can turn it off, and, like, by default, like, not by actual default, but just by common practice that we turn it off, yeah.
Nimrod Avni 00:12:12 Yeah. Okay, I'll open an issue for that.
Tyler Yahn (Splunk) 00:12:15 Yeah. Okay. Sounds good.
Cool. Alright, let me start sharing again.
Awesome. Alright, So, next up, Nimrod, you also wanted to ask about the 1.1, release?
Nimrod Avni 00:12:44 Yeah, wondering if, I think there were a bunch of features added since 1.0.
Maybe we can think about drafting something.
Tyler Yahn (Splunk) 00:12:55 Definitely. We're at, 309, PR is closed, so, yeah, definitely a lot of, a lot of stuff happened.
I think it's only been 3 weeks, but, like, this stuff is piling up way before the 3 weeks, so, yeah.
There are some things that I would say that we need to… take a look at.
This is a new feature.
for the config v2, not necessarily required. This, configuration definitely needs to get done, or needs to get decided to get closed. The idea here being that, we just merged recently this idea to disable the Go channels, which I think is, like, a good feature, just because, like, it was shown that, like, it can cause a lot of… issues for folks. It was added as configuration in this, like, propagation section, which seems odd to me, especially since we already have, like, this runtime go section. So, I'm moving that configuration to this section. Mattia's already reviewed it, but I'd like another review, I think, maybe before I merge, but… I mean, if not, we could probably merge this tomorrow, if nobody really cares.
Nimrod Avni 00:14:02 I'll have a look tonight.
Tyler Yahn (Splunk) 00:14:04 Okay, perfect.
To preserve the V1 Route 53 resolution behavior, this is also another one that needs, more review.
This was merged in, where… Boom, this is break… well, not breaking, this is just, like, our static configuration for V1, had changes to it, and it's been frozen, so this is just reverting that, but also preserving the ability to configure it in the V2. So yeah, this is also another one just for compatibility in our versioning policy that needs a highs.
Gregor Zeitlinger 00:14:37 A tighter?
Tyler Yahn (Splunk) 00:14:39 Yep.
Gregor Zeitlinger 00:14:40 Can you add those PRs to the document? I want to start doing some reviews, and if you put them there, then I will start there.
Tyler Yahn (Splunk) 00:14:50 Yeah, I can…
Gregor Zeitlinger 00:14:52 Thank you.
Tyler Yahn (Splunk) 00:14:54 What's, let's do that. This needs eyes as well… Yeah. Also, this was just a breaking API change. Nichola had some feedback.
on how we could use the new functions here. It's been addressed, so again, this is another one that just needs, needs some eyes on it.
I guess on that note, also, I have a issue I created to kind of, add CI to catch these things. It's still a work in progress. I've got, like, a prototype that has been working using, like, API diff. I just, yeah, right now just doing these manually, so hopefully, hopefully we catch them all. But, yeah.
I think other than that, going through this, this, I think, like I said, new feature, doesn't necessarily need to get out, this release. Try to determine the hostname for MongoDB connections. Likely can get bumps, I'm guessing?
Skip to startup open port scan with no selector uses open ports, I think as well, can also get… Bumped.
Not super important.
Support runtime metric configuration in V2, yeah, again, another feature doesn't need to go out in the 1.1.
Align the auto-read AI guidance across coding tools. Yeah, definitely still… things to work on. Same here, still working on this one.
Definitely can get bumped. Tokyo context propagation, again, also can get bumped. So yeah, I think those are the last PRs, Anything else that folks have that's sitting in the queue, maybe, that isn't tagged for… The 1.1 that we need to get Need to get fixed, something that's on main that's broken, something that we're trying to… Prevent from getting released, or… Critical features?
Mattia Mattia 00:16:49 Maybe it would be nice to, to also get in that, trace, job dispatch, trace grouping.
Tyler Yahn (Splunk) 00:16:58 The,
Nimrod Avni 00:17:01 The first one, 4-1, 4-9.
Tyler Yahn (Splunk) 00:17:05 The fir- the first one?
Nimrod Avni 00:17:07 the, like.
Mattia Mattia 00:17:08 No, it's the last one.
Tyler Yahn (Splunk) 00:17:09 Yeah, okay.
Nimrod Avni 00:17:10 from November.
Tyler Yahn (Splunk) 00:17:15 Yeah, this one, I think, looks good. Did you… I'm guessing you might have seen…
Mattia Mattia 00:17:20 So there was a comment about the config somewhere.
Yeah, I, I think, so my, my idea was to, to make this, generic for, all, Like, patterns that have this, job dispatch.
Tyler Yahn (Splunk) 00:17:39 Hmm. Okay.
Mattia Mattia 00:17:41 Bing.
I'm not sure we want the granularity for all the products, like Redis, Elasticsearch, whatever, database.
Tyler Yahn (Splunk) 00:17:52 No, I… yeah, I agree. If that's the end goal, I can… I can take another look.
I guess I didn't know exactly what we were doing here, but yeah, that makes more sense if you're trying to, like, group this at a broader thing. The, the terminology for jobs traces was a little bit, like, opaque to me. Like, I didn't really understand what it was doing without reading the docs.
and to be… to be fair, like, that just may be, like, the nature of the beast, like, I don't, like, maybe there's just no better name, but I was just trying to think of, like, a way we could try to explain this a little better to users, but, yeah, I could take another look. This is… this is.
Mattia Mattia 00:18:29 Yeah, to explain it in short, so, like, right now we get a request, an HTTP request, and we start a trace from there, for example.
This also makes, job dispatchments from queues and stuff like that.
Work, kind of the same.
But this one is only for Redis, but we should add support… support for Kafka, for databases, and… other stuff. I have a document, locally, which… Documents the gaps.
So I will open some more PRs on this.
This is just the first one.
Nimrod Avni 00:19:10 I wanted to ask if this is, like… The reason that it's behind this, like, config, knob… like config, is it because that we don't want to hurt, the existing, you know, existing traces? Because I think, like, we can say they are wrong. Like, if you take the same application and you instrument them like, via an SDK and via OB, like, one will have one trace that has, like, a Redis read, a Redis, like, pop, and then some actions below it, and then OB will have Redis pop, and then a lot of actions, like, beside it.
Unless maybe there are some edge cases where you, I don't know, that we might be wrong, or we can't, you know, infer it correctly, and we can say, you know, if this bothers you, you can turn it off on this specific… selector.
Mattia Mattia 00:20:04 Yeah, the thing is, there might be false positives, so I prefer to gate it behind the config toggle to avoid changing the behavior of the existing deployments.
Nimrod Avni 00:20:19 Yeah, makes sense, and, you know, maybe we can even… Can it be even something that, like, starts out like this, and… And some major version can be, like, a default or something.
Yeah, yeah, I agree.
Tyler Yahn (Splunk) 00:20:36 Yeah, I mean, I think the… Your point, though, Nimrod, around it being, like, the default behavior may make more sense if we do embed these?
is a good question. Like, if we can make the argument that it is a bug, that they're not showing up embedded underneath the parent span correctly.
I think that makes it, like, makes sense to then try to address it that way.
where the default behavior would be to try to embed them, and then maybe we add a configuration to avoid it, or something like that? But… Yeah, so Mattia, like, maybe I just, like, what are the edge cases, I guess, you're worried about? Are you worried about just, like, our, like, more bugs where we would introduce these things and it would, like, over… overextend, where things would get more…
Mattia Mattia 00:21:21 Well, I don't know from the top of my mind if there are edge cases that… I mean, yeah, bugs, mostly.
Tyler Yahn (Splunk) 00:21:28 Yeah, okay.
Yeah, I mean, I kind of like the idea that, like, if we can avoid adding configuration, like, it's just gonna help us in the long run.
And if we can do the thing that, like, we kind of expect, like, customers are looking for, because it's… defined correct behavior. Like, I think we should try to do that.
Obviously, the tension is, is that, like, you are, you know, we are gonna be changing existing behavior, so, like, that's already, you know, on the territory of whether that's compatible reversioning, right? Like, if you have somebody who's using this currently, and, like, they're… Workflow is finding spans in one way, like, is it possible that this could break them?
I don't think it is, Because if you're trying to find spans, like, you're probably searching for them or something like that, like, you're not using the hierarchical structure in, like… If you were… like, you would be trying to search for, like, a parent span, I guess, and, like, it would stop being a parent span, I guess is, like, the only… only concern that you're gonna see there, if I understand the feature right.
Mattia Mattia 00:22:32 Yeah, I attached the screenshot in the chat, so you can see on the left.
There is the… the new… the new thing. It's just one trace after the… the pop from Redis, for example.
And the various spans that are under it, and on the right, there is the hold behavior, the current behavior, which Which are multiple traces.
Nimrod Avni 00:22:58 I think maybe if we can… And I'm trying to think, maybe we can make it the default with, I don't know, maybe just a global off switch, like the, let's say, Go… Links or something like that, then… then it can be… I don't know, so, like, we can say… you know, we can say that this is a behavior, like, it can be turned off.
If it, for some reason, it, like, you know, you want to preserve the behavior, I don't know.
Mattia Mattia 00:23:30 Do we have, policies on behavior change? Like,
Tyler Yahn (Splunk) 00:23:35 Yeah.
Mattia Mattia 00:23:35 If it makes sense to start with the config toggle and remove the config toggle on switch 2.0.
So we can also change the behavior when, when,
Tyler Yahn (Splunk) 00:23:47 Definitely on a 2.0, like, we're not constrained across major versions, like, we can make breaking changes to API as well as to behavior.
It's just within that major version on, like, minor versions that we are, like, more… constraints around that. Definitely, we can't make, like, API breaking changes, so, like, the config can't change from one to the other. The defaults there, you can't change those, like, that doesn't make any sense. But, like, I think it's fair to say that, like, if we have invalid, like, open telemetry behavior that we can classify as a bug.
I think there's an argument to be made that, like, that behavior was never really intended, and that that's a valid change, because it's a bug fix.
you know, obviously, it's a slippery slope, because, like, it's really easy to say, like, well, I never really wanted that to be there. But, like, yeah, I think that, like, what you're describing here is, like, literally, like, invalid telemetry that's showing up as wrong traces, right? Like… So, I don't know, like, I think at the.
Mattia Mattia 00:24:45 Yeah, also, some people might be using the bug as a feature. They might get used to it.
Tyler Yahn (Splunk) 00:24:51 That's always the concern, right? Yeah, yeah, absolutely, yeah.
Yeah, so that's a good question. You know, because if they are using it in, like, this is the expected format, then, like, that's… Yeah. Having an off switch, I guess, like Nimrod's also saying, like, we could also do that, where… You know, maybe in this situation, we provide the default where it fixes it, but there's, like, an off switch to say, like, you know, give me back the bug, or give me back these disparate terraces, or something like that.
Mattia Mattia 00:25:20 Okay, so invert the behavior of the toggle, basically.
Tyler Yahn (Splunk) 00:25:24 I mean, I think that makes sense to me,
Nimrod Avni 00:25:28 Yeah, and I don't even think we need the… like, I think your even… your toggle even has, like, like, matchers. I think it might even be more simpler to have Like a globe, global toggle?
And, like, maybe…
Mattia Mattia 00:25:41 I don't think it has matches, I don't remember.
Nimrod Avni 00:25:45 Oh, no? It's just, like, one, like… Okay, if it's one flat…
Mattia Mattia 00:25:50 I mean, yeah.
Nimrod Avni 00:25:52 Yeah, if it's one flag, then, you know, either have, inverted, or just make the default, false or something, like… Right?
Mattia Mattia 00:26:01 Default on the new behavior, and
Nimrod Avni 00:26:04 I think so. Like, I think it can be classified as a… Yeah, I think a lot of… I'm also doing a lot of, like, telemetry changes, and I know we can say it's kind of breaking API, but I think if it's, going towards, like.
aligning with how Oto does it, I think it makes sense, like, because if we're doing stuff that are… like, I think a lot of people expect OB telemetry, especially the one that should be, like, imitate, you know, maybe not our custom metrics, but stuff that should be imitating The semantic conventions, we should follow them.
So I think it makes sense.
Mattia Mattia 00:26:45 Okay.
Tyler Yahn (Splunk) 00:26:46 Yeah.
Mattia Mattia 00:26:46 I'll do that.
Tyler Yahn (Splunk) 00:26:47 I agree.
Okay, cool, and I will take another look at that, after I guess, I see a push from you, and then I'll take another look. But yeah, I've added it to the milestone, as well.
Cool… Looking at your other PRs right now, Mattia, I don't think these other two… need to be in this milestone, I'm guessing, but okay.
Getting distracted.
Okay, any other issues or PRs folks had they wanted to include?
Giuseppe Ognibene (Coralogix) 00:27:25 I have one PR. I saw your comments, I just pushed the fixes.
Tyler Yahn (Splunk) 00:27:34 Oh, okay,
Giuseppe Ognibene (Coralogix) 00:27:36 Pino.
Tyler Yahn (Splunk) 00:27:38 Yeah, sorry.
I don't know.
This one, okay.
Yeah, that sounds good.
Oh, I'll add this to the milestone as well, then.
Okay, cool, yeah, this looks… like, it also needs more reviews, so folks on the call, please also take another look. I will take another look after the call.
Actually, let me add this to… for… Gregor.
Gregor Zeitlinger 00:28:13 Thank you!
Tyler Yahn (Splunk) 00:28:20 Okay.
Okay, cool.
Moving on then, Mattia, you wanted to ask about the request for the SIG-specific OTEL bot in the OTEL community?
Mattia Mattia 00:28:29 Yeah, we already, I think, discussed this a little bit on Slack. I just wanted to get a consensus from the SIG to open a request to… for a SIG-specific hotel bot.
with, Bright permissions.
So, the issue was that the renovate sometimes opens PRs that need some post-processing, which is done currently manual, but it's… the workflow is broken.
So it doesn't work.
Yeah, I wanted to automate it, more.
Tyler Yahn (Splunk) 00:29:08 Yeah, I'm all about it. I think that's a great idea.
Mattia Mattia 00:29:10 Okay, I will open a request in the community then.
Tyler Yahn (Splunk) 00:29:15 Yeah, perfect. That sounds good.
Okay, cool. On that note as well, I did wanna… Sorry, I tried to find my screen.
One of the other things that, like, we can do… I guess Marc also pointed out this is a private repo, which is a good point, maybe I won't open it right now. But essentially, right now, like, there's actually a way where, like, Gregor, I know that you were having a ton of problem with, like, the CLA bot and pushing to, like, these, like, feature branches and things. I was talking with Trask a little at, KubeCon, and, having him explain that comment that he left in Slack, because I was still a little confused about that, but the idea is that, like.
What you can do is you can, you can set a configuring, configuration in the hotel, like, Terraform, project, which is what this is, and that will update the, the CLA, like, check Exceptions to include all branches that start with an approver's name, followed by a forward slash or a dash.
Which is kind of cool, be… Yeah. So, like, if we wanted to, like, move one of those branches to… I don't know, Mr. Alias or something, or, you know, an approver prefixed one, then there wouldn't be any of those CLA checks when we tried to merge into it, so then we could actually, like, get this thing to work, and not have to do these manual pushes, which is not, like, the end of the world, but… Yeah, so that's one thing that, like, that's why he was saying, like, we can kind of avoid those problems if we do that, which I think is a positive. Another positive is, Allowing this also allows, approvers to stack PRs, so if you wanted to, you know, I don't know if you've ever seen the GitHub feature, but it's pretty sweet, where, like, you can.
Gregor Zeitlinger 00:31:02 It is gracious.
Tyler Yahn (Splunk) 00:31:04 Yeah, yeah, you know what I'm talking about, yeah.
And, like, for those that haven't, like, it's just like, you can build these, like, really, you know, big PRs, and you can break them down into small, digestible, like, reviewable things, and, like, once one reviews, it automatically, like, will not, like, the next PR will be opened, and you can see, like, the next step without it, like, being, like, these compounded, like, you know.
10,000 line PRs that you're trying to, like, manually handle that, migration, so… Yeah, another really cool feature.
It's got two approvals on it from the maintainers. This is gonna require maintainer approval. I'm gonna wait maybe a day or two, and then we'll merge it, but I think that that's kind of the goal, is to go in that direction.
Gregor Zeitlinger 00:31:41 Cool, and if I understand correctly, I also have to get a prover, so I'll do some PR reviews to… To, have a chance.
Tyler Yahn (Splunk) 00:31:51 Absolutely. I think that that's a great… that's a great task list for you. Let's get some more reviews, that sounds great.
Gregor Zeitlinger 00:31:57 Yep, thanks.
Tyler Yahn (Splunk) 00:31:58 Yep.
Okay, cool. And then, next up, I did want to talk about the roadmap, more just to kind of pause here and say, like.
Excuse me.
Kubecon was great. There was a lot of, like, interest in Obi. The 1.0, I think, has, like, kind of made people even more interested in this project. There was, like, organic talks from people that are not in Obi, people on, like, the GC, people, like, by and large in OTEL that were talking about Obi.
I think it went off really well. I know that Mike and Rafael had two really good talks, pretty well attended, around, like, the internals of Obi. I know that Nicola, in my talk that we gave, we talked a lot about, the installation of OpenTelemetry, and it was… it kind of touched on Obi, and it's a big part of that future.
But I think a lot of people are starting to, like, buy into that idea that, like.
OTEL is not necessarily just APIs and SDKs anymore.
is something that you install. So, like, OB is going to be a big part of that in the future, as well as, I think, the packaging SIG and the, you know, some operator questions as well, were kind of the two things that kind of came up.
But those are, like, the main ways that people are starting to interact with OpenTelemetry at all.
That being said, like, the next question out of most people's mouths are, what's… what's the… what's the roadmap? What's coming up next year?
And I was… I've got a lot of really excited ideas, so I was happy to share them, because I definitely have some things I wanted to work on, but I also wanted to just kind of check in, Here on our existing roadmap.
as we come to close out the year, and as we're going into the next year, I also wanted to kind of, like, give a highlight of how we can start planning for that.
I guess maybe I'll start, at the end, and then we'll work back to the beginning. So, I did create this other roadmap for the 2027 goals.
Which, did not get saved, But it is, a new label that was added.
And that, I, you know, I just added… 3 things, but there's probably, like, 4 or 5 things I've talked with other people at the conference on that they were super excited about. Mostly the, packaging SIG is, If you have met some of the personalities in the packaging SIG, you can tell they were very, excited for us to get our 1.0 out, just so that they can get the packaging stuff done, which I think is fair. Like, they… they are… very much going to be improved by having Obi.
included in, like, their OpenTelemetry package. As all of you know, like, it's a fantastic way to get, you know, broad coverage across a node, and right now, like, you know, things like Go and C++ have zero coverage for them, so, they would really like us to get this done. So that's probably top of my list. I would actually maybe try to get this done in 2026.
Just because it's been asked of us. The dynamic probe Instrumentation, another big one that people were super excited about, we were talking it up. I know that Gregor has been actively working on this one. This is definitely something that's high on the list.
These expanded W3C trace context propagations for other languages, in their frameworks, so another one people were super excited about.
But, I mean, there's a lot of other things, I think cleanup and other, other things that people would be interested in.
A lot of them aren't that, like… familiar, I think, with Obi, to the point where, like, I… I asked, you know, for most people asking what's next, the refrain was, well, can you please, like.
come let us know what you want. And so I think, like, our goal is to maybe, like, try to popularize this and get some feedback at this point. But go ahead, Gregor.
Gregor Zeitlinger 00:35:40 Yeah, once, I get more traction on the dynamic instrumentation, I want to work on the equivalent of changing code, a live patching, or I don't know what a good name is.
So this is not very well defined, but I think it has potential to fill a gap that we currently have right now. You always have to restart your service, and maybe that's just what everyone is used to, but, with OB, it doesn't need to be that way, and there's, A considerable chunk of use cases where you can live patch, and… Stop the bleeding when you have an incident before you have the time to do a proper patch.
Tyler Yahn (Splunk) 00:36:31 Yeah, I gotcha.
Can you… yeah, you're not the first on this one. I think a lot of people are really interested in this. Could you create an issue so that we can start at least identifying it, or discussing that, would be really great, and then we can even add the goal label if we want to include that as something that you plan on working on next year.
Gregor Zeitlinger 00:36:52 Yeah, for sure.
Tyler Yahn (Splunk) 00:36:55 Nimrod?
Nimrod Avni 00:36:57 Yeah, so I heard, kind of relating to the, custom captures, in a similar, space, something like… kind of, I don't say live debugging, but let's say something like even capturing, you know, the state of a function, inside, you know, a specific line, and seeing, like, what's the, the… values of certain variables, and then, I don't know, like, custom, you know, inject custom logs and stuff like that. I'm not sure if we can… do stuff like probing inside a function in a specific line, if you don't have the address, we can do it. I mean, I guess it's dependent on the language, or maybe in every language.
Gregor Zeitlinger 00:37:40 I have not figured out for each language, but we discussed it, and you can inject some instrumentation. I mean, Nikola said that I have not worked on it, so I guess I will find out once I do, but in theory, it should work.
Nimrod Avni 00:37:58 Yeah.
Tyler Yahn (Splunk) 00:37:59 Another proof of concept that Nikola was playing with, and I was playing with a little bit, it definitely can capture the parameters, or any arguments that are passed to the function, but state within the function, I guess I haven't seen that, but I don't see why we couldn't do something, as long as it's, you know… stored in an accessible location, right? Like, yeah, I think it's just discovering and finding that, and then presenting it in some way, yeah.
Nimrod Avni 00:38:21 Yeah, so I think that that's gonna be… like, if we can incorporate it into that, it'll be super cool.
Yeah.
I think that's, And there's, like, a bunch of other, I think, cool stuff that we can do, I need to… I need to think… I have some, like, other ideas I'm trying to find. Maybe Mattia remembers some.
Gregor Zeitlinger 00:38:43 Yeah, if you, if you want to collaborate, let's just, Chat, and then, there's plenty of stuff to do.
Tyler Yahn (Splunk) 00:38:54 Yeah, Mattia?
Mattia Mattia 00:38:56 Yeah, this was also related to the dynamic instrumentation.
So there are a bunch of things, cool things we… we can do, regarding that. We… we need the… Some… some fully, how do I say that? Fully updatable, at runtime config?
Or something like that. Yeah.
I… There was some other thing… Related to dynamic instrumentation, which I forgot.
What was that?
Gregor Zeitlinger 00:39:37 Maybe the… Nothing, I forgot.
Mattia Mattia 00:39:38 I had it in mind until 30 seconds ago.
Tyler Yahn (Splunk) 00:39:42 No.
Mattia Mattia 00:39:43 Which one?
Giuseppe Ognibene (Coralogix) 00:39:45 the config model.
Gregor Zeitlinger 00:39:49 Yeah, I think it is related, Such a way that you need to be able to read configuration at runtime, to have, more instrumentation at runtime, otherwise it wouldn't help. No, yeah.
Nimrod Avni 00:40:06 I think that, like, doing something with OPAM, probably be, like, we can also say that we're incorporating with, like, the hotel form… way of, you know, like, remote config management.
Mattia Mattia 00:40:21 Oh, yeah, it came back to my mind.
Gregor Zeitlinger 00:40:23 Option, yes.
Mattia Mattia 00:40:23 So we need a way to expose some kind of light data. So, in a cluster, we need to see the… so the customer needs to see the state of the current binaries, which are instrumentable.
with all the symbols, which are instrumentable. And if we want to proceed with this live patching idea, I think we also need to see the offsets which are instrumentable. So, one function can go from offset 0 to offset 150, and we can put some code in that offset, I think.
So we need to… some way to see… to be able to see all this kind of data at runtime, like… live data.
Nimrod Avni 00:41:10 Yeah, I think it's, like, not even… it's more of an API than, like, sending telemetry, because it kind of needs… like, if you're imagining some… hotel backend, and you wanna go, like, okay, I wanna instrument OB not… I'm not gonna do, like, you know, gonna edit the config map myself, I want to do it remotely, then we need some sort of, like, autocomplete mechanism, sort of, like, discovery of… Of what's even instrumentable. So maybe, either via OpAMP or some other API, maybe we can do something like that.
Lisa?
Tyler Yahn (Splunk) 00:41:42 Yeah, the…
Mattia Mattia 00:41:43 So, so you said OpPump is, if I recall correctly, is based on gRPC?
Does it support streaming?
Nimrod Avni 00:41:52 I'm pretty sure. I'm not super familiar with, like… if you're saying, like, I know the… a bit of, like, the response, like, the… you know, there's, like, two basic messages, like, one is of an agent, like, writing to a server, and one is a server writing to an agent, and I think it's, like, streamed via those, but I don't know if, like, the… payload of one message can be split, like, if you want to send metadata and it's too large, you want to split it up, I don't know.
Maybe we need to explore that.
Mattia Mattia 00:42:24 We need to do more research on that.
Gregor Zeitlinger 00:42:29 I think it's a good idea if we, Split, building the functionality, and then… adding it to OpAmp, because OpAmp, whenever I heard about it, is very complicated, so we just need to build it in a way that is flexible enough.
And I think we probably also want to have a way to do it without OpAmp, so that you can choose what works best for you.
Nimrod Avni 00:42:55 Yeah, I think it's definitely, like, you know, we can work on those either in parallel or one after another, like, even now that I think Nicola did the, like, the capture, like, the, like, selection config kind of dynamic.
Via, at least via, like, the code, the API. So, I think, like, the, like, putting, like, a config updater around that, that's, like, a different thing, but the… as long as the infrastructure allows it, we can make it, so I think we should probably do something similar.
Tyler Yahn (Splunk) 00:43:28 Yeah, when I was playing with this, I actually took… Because, like, I think his prototype was really good in, like, being able to, like, set things, but yeah, like, it's trying to get into… it's already an API, right? Like, so we already have that, but, like, you can turn that API into also a getter to handle all of these, like, other bi-directional things.
But yeah, I agree, like, I think having the API just, like, even, like, a HTTP API at first is ideal.
there's a lot. There's actually too much to talk about, honestly. I think there's a lot of really cool things here. But, I guess I would ask, like, as we're going into this planning thing, all these ideas, can you make sure that they're captured in comments or issues or sub-issues of these issues, just so that we don't lose them? Because I think, like, it's really easy to, like.
yeah, forget about them. I've got them in notes on my, like, phone right now, so I'm gonna also try to do a better job in, like, capturing them in issues.
For this upcoming year, just to, like, communicate to other people.
I do think that dynamic interpretation is going to be one of the bigger things we get out, this upcoming year, and I also think, you know.
that's a shame, because I think there's gonna be a lot of other really great features we're gonna get out as well. So, but yeah.
Please, please do that.
As well, not just dynamic interpretation, any other things that you've been thinking about in the backgrounds, or planning to work on in this upcoming year, make sure you add them. If you don't have the ability to… Add a label, let me know, and I can add a label for you as well.
Jumping back in, though, to the 2026 goals, and what we are currently at… I do see that we still have a lot in progress. I know to provide the runtime metrics with Obi. I know Mark's on the call, so I kind of wanted to pause and get a status update on this, on where we're at.
I don't know if Marc can talk. Spark… yeah. Actually, I think… Everything has been done except for this configuration task I have listed here.
I don't know if there's other… I know Marc's moved on to exceptions, as well, so maybe this is done. We just are looking for… Configuration support at this point.
Nimrod Avni 00:45:41 Yeah, I'm not super, Like, from a… maybe we can see the issue, like, is it not supported in V2?
Tyler Yahn (Splunk) 00:45:50 It's not. No.
Yeah.
Which is just a… Again, hence why we froze V1. We gotta stop adding things there. So yeah, like, just the idea is that we should be able to see a support here.
But yeah, like, I don't… this is on my thing for this milestone. I don't know if we want to block, on this. I think this might be that 1.2 configuration thing, but yeah, it's on there.
Okay, moving on. So, also on here, evaluating Trace Programs in K-Probe FastPath?
I see, Mattia, you're assigned to this. I don't know if this is still active.
Mattia Mattia 00:46:32 Yeah, I don't think we ever got into that.
But, I'm pretty sure this is not doable anymore, because we added some, some guards for cake rubs.
In order to not be preempted.
So… Even if it's doable, it's, it's… it got much harder now to do.
That conversion.
Tyler Yahn (Splunk) 00:47:03 Oh, I think…
Mattia Mattia 00:47:03 Maybe we can keep this open, like, to keep it in mind when we have some time to research it.
But, but we should maybe deprioritize it.
Tyler Yahn (Splunk) 00:47:16 Can we… can we do a research task before the end of the year, though? Given this is one of the 2026 goals?
Mattia Mattia 00:47:24 Sure, I can do that.
Tyler Yahn (Splunk) 00:47:26 Okay. Yeah, I think, like, especially if this is just gonna be, like, a… you know, ask some AI agent to give you some understanding of, like, how things have moved.
We can probably get a real quick answer of whether, like.
this is impossible, or this is hard, or this is, like, doable. And then we can either keep it open, move it to next year, or just close it, yeah.
Okay, cool. Russ, Tokyo, I.O. context propagation, I'm kind of bummed Nicola's not here, because it sounds like he… broke through on Rust, so I guess maybe… We'll just pause on this one. He might actually have some insight on this, too.
Giuseppe Ognibene (Coralogix) 00:48:08 Actually, I had a call with Nikola yesterday, because I'm working on that. Oh, cool. I have a draft PR that is failing on, Amazon kernel.
So I think that I will do a PR, and then Nicola did something else on, HTTP2 and TLS, and it will, we will try to merge both works.
Tyler Yahn (Splunk) 00:48:30 Oh, cool. Okay.
Yeah, that's great news. That sounds… that sounds like… we should get this done this year. That sounds awesome.
Thanks, Giuseppe.
The network semantic convention stuff, I don't think this is going to get done this year, still in a to-do state. I don't think there's anybody actually moving this forward.
Nimrod Avni 00:48:54 Pinot.
Tyler Yahn (Splunk) 00:48:54 Billy's at a.
Nimrod Avni 00:48:55 Isn't this the… isn't this, like, part of the network sign?
Giuseppe Ognibene (Coralogix) 00:48:58 From time to time, we talk about this, but there was the KubeCon, so people were a bit busy.
So I think that from next week, we… we should start to… to work again on that.
I think that they did something on the number 11 some time ago, but… I don't remember.
Tyler Yahn (Splunk) 00:49:20 Yeah, I think since… I think it's mostly just in the network sig is where this is coming down to.
But, I think this is something that we could probably move forward to the 2027 goals, that we can achieve there. This is one of those things that I was kind of thinking would move forward to the 2027, but… If we can get it done this year's… Yeah, yeah.
Giuseppe Ognibene (Coralogix) 00:49:39 I can… I can ask on Monday, we have the SIG meeting, so I can ask him.
Tyler Yahn (Splunk) 00:49:43 Okay, yeah, that'd be great. Just even if the answer is, like, it's gonna get, you know, moved to next year, that's fine. Or if it's gonna get done, that's great.
That'd be pretty amazing, but it'd also be pretty, incredible.
Gregor Zeitlinger 00:49:57 Incredible.
Tyler Yahn (Splunk) 00:49:59 Okay, OTEL API SDK integration? This is a big one. Most of these tasks, actually, I think, are done… not most, some of these tasks, are done.
But there's definitely a lot left, yeah.
Poof.
Yeah, there's definitely some bigger ones in here.
this is probably not gonna get done this year, but I'm just gonna say, like, it's something we could also continue to work on. I think of ours, a lot of other… APIs and SDKs that we want to keep supporting, so… This is probably definitely one that's gonna get moved.
Support for .NET, I don't know where our status is on this one. I know Raphael had been looking at it for a long time, but I don't know where we're at here.
I'm also wondering if I can get some help on this one from some of my teammates, but yeah, this one will probably get moved as well. I don't think there's gonna be any movement in the rest of the year.
Additional protocol supports, I know Marc and, Nimrod, you're looking at this.
Nimrod Avni 00:51:18 Yeah, I think most of them are, like… oh, sorry.
Tyler Yahn (Splunk) 00:51:23 No, so I… yeah, go ahead. I was just, like, I think some of these are done, right?
Nimrod Avni 00:51:30 Yeah, sorry, some noise. Yeah, I think most of them are done.
Yeah, I think that there's, like, the Mongo stuff that we have, it's, like, kind of deprioritized, Redis PubSub's still not there, and… like, all the cloud services is, like, a very wide scope, because AWS, we're already instrument.
S3, S3, and SQS and SNS.
It's more like umbrella issues of, like, we can't… like, we can say, okay, let's chase, all the semantic convention stuff and, like, implement them one by one, but they usually come on demand, like, either from… I guess from customers of each of the companies here, or from, like, external contributors. We… we can, like, open everything in, you know, in advance, but… Unless there is a… Unless there's some saying that we want to preemptive… I think most of the common stuff, like the, I don't know, the common technologies, common protocols, whatever we already have.
So I think it… maybe it should be done on, like, a… Requirement basis?
Tyler Yahn (Splunk) 00:52:46 kind of what I'm hearing is that, like, maybe this issue needs to be closed, and just call it, you know, good enough, and then when we find new protocols that we want to support, like, those can be addressed, but we're not gonna… actively tackle these right now? Or next year?
Nimrod Avni 00:52:59 Yeah, I don't think we can, like, we need to commit to, adding any protocol, I think most of the stuff that we wanted to do are… are done.
Tyler Yahn (Splunk) 00:53:13 Okay.
Okay.
I will leave a note for myself. We need to close this. It sounds good.
Then coming back here, support process declarative configuration. This is an interesting one, that's at the top of a goal. It's definitely something in the broader scheme of supporting Declarative config.
It's, possibly gonna get done.
In this upcoming year? Yeah, I think that I might be able to get this done next month, is kind of my goal.
I don't know why it's on the top level, it's kind of a small issue. But, okay.
Other than that, I think that's… All of the goals, so yeah, making a lot of progress.
I did see there was one other item, so I'm gonna… push on. Roy, you wanted to ask, is Rust the future?
Asking about an ecosystem trend?
Roy Reshef (Kubex) 00:54:09 Yeah, I showed you a LinkedIn post by Bartek, I don't know who knows if you know him. I met him… I wasn't at KubeCon this time, I was there two years ago.
And then I talked to him.
Anyway, he has benchmarked, you can read the details, some collectors, in both Go and Rust implementations, and, like, the results in terms of resource consumption are… and are almost ridiculous. I mean, it's… they're hard to believe.
And and there's also now some activity in… I have some people I know at the Prometheus community, so they're starting an activity maybe to rustify Prometheus.
And… I could see, by the way, we… at my company, we roll out Bela, not OBI directly, but we roll out Bela, which, you know, like, it's like a… a variant of OBI, you can call it, based on the same codebase.
And we did have, with quite some customers, OM kills of Bela, upon startup, and stuff like this.
I don't know, I mean, I'm just throwing it as food or dog food for thought.
Because if OBI is running on each and every node, maybe… It is worse, too.
Take a look at… porting it, and currently with AI tools, I mean, we have some exporters of our own.
Tyler Yahn (Splunk) 00:55:41 Yeah, so I just want to pause on that one for a second. So, I want to make it clear, like, that post also is not necessarily apples to apples, right? Of course not. It is exploring a collector, not only written in Rust, but also defined around the data model of OAMP, right?
So, like, it's not using OTLP anymore.
It's… it's definitely… it's a… it's… I think that's more what I would… say that that pose is kind of focusing on, is that the columnar store data model of Apache Arrow is what's actually being used under the surface, and that's, I think, where a big part of the win is.
There was another talk at KubeCon called… by Heinrich, who did a lot of benchmarking across this as well. I think that's an interesting one to also keep and look at, because one of the things that, like, maybe this isn't… showing is that that works really well, and it's a very performant system until you need to serialize and essentially, like, turn this column or store data back into a full dataset that aren't sparse.
Which… in the ecosystem of OTEL is every single jump, just because most… systems don't actually support Apache Arrow currently. So yeah, like, there's definitely some performance benefits, I think, to look at here.
I would also say that, like, there's more to talk about there, but just… just to kind of phrase that post a little bit more, I think along those lines, like, it's not really necessarily a Rust vs. Go thing, it's a data model question, I think, is what the core of that actually is looking at.
Roy Reshef (Kubex) 00:57:21 Possibly, I mean, I'm… I'm not that familiar with those details, but And again, this is a… look, I'm not a Rust expert. I'm not a rust expert either, so, in that sense, but maybe it's something in the know. And of course, this is just food for salt, it's not, I mean, currently, the entire codebase is go. And even if you decide to convert it to Rust, it will take some effort to get there, so…
Tyler Yahn (Splunk) 00:57:49 Yeah, but what I'm saying is that, like, even if you look at the Apache Arrow project, there are many projects written in Go that support Apache Arrow and show very similar performance improvements. It's the data model, I think, is the thing that is really in question here.
Another thing is, is, like, if you look at Heinrich's talk, That collector that they're… they're… evaluating here in Rust, right? It's not a feature-complete collector, and I think that that's maybe another part that you want to put into the conversation, like, even if we wanted to look into translating our data model into using the Apache Arrow.
You would need to understand that, like, that's a complete rewrite that would set the project back, right, considerably, because a lot of the features that we would need to support would not be there.
So, I think that… looking at performance evaluations and how we can speed up the project, I think are really important, but you also need to understand that, like, It is a little bit of a… a Trust Me Bro benchmark right there. Like, it's not like… I don't think I would say that it's a definitive use case to say that we should switch to a different language, different data model, different anything, honestly. I think that, like, we talked about this with people at KubeCon as well, around Obi, whether it was the limiting factor resource-wise, and it is.
Especially for people that run, like, cloud systems, it was really important for them to have the ability to run… you know, in less than 500 megabytes with, like, half a CPU, like, that's not really possible with OB running on those nodes, right? So I think, like, your point is well-founded, but I do want to, like, temper that a little bit in saying, like, there's not really a holy grail that I would say exists.
Roy Reshef (Kubex) 00:59:29 No, I didn't try to present it like this, I just… Wanted to throw it out there, and Because I did see on my feed quite a bit of reactions to this, and so on, and people are looking into it, so just… Thought it may be worse to bring it up, that's all.
Tyler Yahn (Splunk) 00:59:51 Yeah, gregor, we got 10 seconds, last up before we close it out.
Gregor Zeitlinger 00:59:57 That's very short. Just wanted to add that recently some projects have managed to convert the language while still accepting features at the same time. This is something that I have just heard a couple weeks ago, so… It's difficult, but not impossible.
Tyler Yahn (Splunk) 01:00:16 Yep, no, agreed. That sounds good. Okay, we are at the end of time. Thanks, everyone, for joining. I want to be respectful of everyone's time. We will see you all next week, and until then, bye.
Gregor Zeitlinger 01:00:27 See you!
Mattia Mattia 01:00:28 bye.
