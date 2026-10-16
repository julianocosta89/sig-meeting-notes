SIG: Python SIG
Date: 2026-10-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Emídio Neto** 01:26 Hey, Tammy.
**Tammy Baylis** 01:30 Hey Emilio, how you doing?
**Emídio Neto** 01:33 Great, great, and you? Feeling better?
**Tammy Baylis** 01:36 Mostly. Yeah. Thanks for asking. That one. That one cold flu hit me really hard. It was pretty early, I guess, for around here. Usually flu season is.
It's later, yeah.
**Emídio Neto** 01:52 We got the flu as well, like, 2 weeks ago.
**Tammy Baylis** 01:56 No…
**Emídio Neto** 01:58 Yeah.
But I'm not feeling better now.
**Tammy Baylis** 02:02 Okay, good. I it wasn't too long to recover, was it?
**Emídio Neto** 02:08 7 days.
**Tammy Baylis** 02:10 Oh.
Yeah.
Well, glad glad you eventually recovered.
**Emídio Neto** 02:19 Yeah, yeah.
**Tammy Baylis** 02:35 Oh, I was sharing for a moment, and now… Now it's gone, let's try again. There we go.
**Riccardo Magliocchetti** 02:45 Hello.
**Tammy Baylis** 02:47 Hey Ricardo.
**Emídio Neto** 02:50 Hey.
**Tammy Baylis** 02:59 We'll wait one more minute or so.
Okay, might as well… get started.
Small.
Turn out of familiar faces today. Welcome back to the Yotel Python SIG meeting. The meeting notes you see on screen are shared in the chat.
**And we'll start with a bit of triage till** 9:10 today.
Yeah, there's a lot in Contrib from the last… Week, two weeks or so, so maybe we'll start there.
We are looking at the… Katie Reilly, Bot maintained dashboard for pull requests for Contrib, and we're looking at the… Waiting on reviews… sorry, still getting over this cold. Waiting on reviews, section… eric hansen: bottom up so we can look at some most recent ones first.
This one, updated recently… khurd: Three weeks ago, Lukas, to update the CI, I think that's a great idea.
Yeah, Emilio gives the old thumbs up there.
**Emídio Neto** 06:11 Yeah, I'll discuss with Lukas about this one.
It's good to reduce the footprint, but I asked him to at least we keep the PiPi jobs.
I know we have a lot of issues with them, so it would be nice to have… At least those running.
But I'm fine with the CPython.
Testing against the Python oldest and latest version.
**Tammy Baylis** 06:39 Yeah.
Oh, hey Lukas.
**Lukas Hering** 06:43 Half the jobs, almost half.
On PRs.
**Emídio Neto** 06:47 Yeah.
**Lukas Hering** 06:49 So I think it's… And, for… if we apply this.
The note I added, if we apply this in the main repo, we can also just exclude, like, have SDK run everything. Because that's more of a… No sense.
**Emídio Neto** 07:03 Yeah, it's more critical. Yeah, I agree, yeah. It would be nice to run against other version.
Can you scroll down a bit to the…
**Tammy Baylis** 07:15 Oh, yeah, sorry.
**Emídio Neto** 07:17 No, I mean, to see how many jobs. I'll skip it.
**Tammy Baylis** 07:24 And.
**Lukas Hering** 07:26 CRT.
**Emídio Neto** 07:28 Church 103, yeah. It's nice.
Yeah, good improvement.
**Tammy Baylis** 07:35 Yeah, Ricardo.
**Riccardo Magliocchetti** 07:37 Yeah, question, is this only for the PR test, right? So on the merge queue?
All the… Python will be tested, correct?
**Emídio Neto** 07:48 Yeah.
Exactly.
**Riccardo Magliocchetti** 07:54 Well, sounds great.
**Emídio Neto** 08:00 Cool. Yeah, I will approve the PR Lukas and we can merge.
**Tammy Baylis** 08:05 Dope.
Thank you, guys.
Good call.
Open client.
Which, to be fair, I… Sorry, I still don't know much about, but I know a couple people here do.
Oh.
**Riccardo Magliocchetti** 08:26 Yeah, I think that both me and… Pablo took a look already, so I guess we can skip this one.
**Tammy Baylis** 08:33 Yeah, thank you very much.
Okay… Bottle core test.
Huh.
Sounds nice. One file change… Hmm.
There's no issue linked, but it is just adding a test.
I approve to run.
Might be good to… Visit again, no reviewers assigned. That's interesting.
Hotel process context OTEP 4719.
Evpf.
Oh… We've had some… People flagged already.
Yeah, we need to review this.
Thanks, Lucas.
Oh, add Oracle DB. Yeah, I think we've talked about this before. Pablo's approved it.
Okay, yeah.
It'd be good to get a couple more views on this also. Please take a look.
Fix for Flask. Keep server span open.
Until streaming response fully sent.
I think I've seen this before, but… Hmm.
Okay, yeah, we should look at this one.
Let's just do… One more same reporter Emidios had a look. Thank you.
Take the readme.
Yeah, okay.
Let's let's leave triage at that for now. It's 9 11 my time.
And… we'll move… On to the rest of the agenda.
What people are working on, thank you for filling this in. Ricardo's reviewing PRs. Lukas, log stabilization, thank you. And Emidio PRs and security advisories, thank you.
Topics, Lucas, log benchmarks. Take it away, Lucas.
**Lukas Hering** 12:23 Yeah, I think, so Last week, I submitted the PRs for the log stabilization. I think, Aaron commented that maybe we want to Add some more benchmarks for the disabled path.
So, yeah, I did that. Notice, like.
a one like a few performance improvements we can make.
I guess the question is, is there anything else that we see needing to change here before the logs.
stabilization.
**Aaron Abbott (Google LLC)** 13:05 Hey.
Yeah, sorry, I'm taking a look now. I… it looks like this is all SDK benchmarks for disabled. I didn't see anything for… testing the no-op API, or maybe we already had some benchmarks.
**Lukas Hering** 13:21 the… Sorry, the… this, you mean, like, when… No, no loggers… logger provider is… is initialized?
**Aaron Abbott (Google LLC)** 13:34 Yeah, no SDK.
**Lukas Hering** 13:36 I think that, yeah, this should be included.
Or maybe I didn't double check.
**Tammy Baylis** 13:42 Sorry, my connection was really slow. There we go. Sorry.
**Lukas Hering** 13:47 Ahem.
If you, like, if you look at the PR description, the last two are, API proxy, no ops.
Is that what you were referring to?
**Aaron Abbott (Google LLC)** 14:07 Yeah, I guess also, excuse me.
Also, just like the no op without the proxy.
But I guess this is the default state anyways, the proxy, right?
**Lukas Hering** 14:19 Yeah.
**Aaron Abbott (Google LLC)** 14:22 Okay, no, I think… That's good, sorry, I'll take a closer look. Do we have anything in the benchmarks for, like, memory or GC pressure.
**Lukas Hering** 14:38 From what I could tell, no. It seems like they're pretty basic.
**Aaron Abbott (Google LLC)** 14:42 Yeah.
**Lukas Hering** 14:42 I guess, like… So the… the concern is, though, generally that I guess, like, what would… In my mind, I'm not sure…
**Aaron Abbott (Google LLC)** 14:55 Yeah.
So, like, I think we have two variants.
Sorry.
**Lukas Hering** 15:00 Go ahead, sorry.
**Aaron Abbott (Google LLC)** 15:01 My bad. I was gonna say, I think we have two variants of the API. We have one where you pass a log record, which is the original one, and then we added, later on, one where you can pass, Like all the fields directly without having to box them in a data class.
Which I think probably covers the concern.
Because I was worried that if we forced people to churn through these LogRecord boxes without a… without the SDK.
It's just kind of, gonna create a lot of GC churn.
**Lukas Hering** 15:37 Right, yeah. And I think, Well, we also have the enabled API, so… I mean, it's not, like, pretty, but… if you guard, right? I mean, if you're… if you're guarding everything with that enabled check.
But it's another way to prevent the creation of those objects in the first place.
**Aaron Abbott (Google LLC)** 16:03 Ian.
Okay, cool. I'll review this one, and Yeah, sorry for the delay, Lukas.
**Lukas Hering** 16:12 Oh, yeah, no worries, just wanted to make sure. Yeah, so, I mean… Yeah, I can look into adding some memory stuff.
memory benchmarks here.
The one… I guess, potential flag that we might want to add that would be a breaking Api change would be doing like lazy formatting similar to the Python logger.
Since, like, currently the body is just an any value, that's, you know, greedily evaluated.
We don't have any, like… formatting or templating option.
Do we… does anyone see that as being, like… Something we want to add.
Like, right now?
**Aaron Abbott (Google LLC)** 17:03 When you say body is eagerly formatted, do you mean the user has to pass the formatted string directly?
**Lukas Hering** 17:11 Right, like, with the Python logger, right, you can just do, like, a format string, where the R… the… the actual… the formatting will only occur when the logger is enabled.
Whereas… You know, here, you just pass in the body as a string, so you'd have to… You know, your only option for doing that lazy evaluation would be to add an is-enabled guard.
if I'm… I'm not sure if, like…
**Aaron Abbott (Google LLC)** 17:48 Yeah, I don't know if I totally… Got it. I, I, what you said about the lazy guard, but I, I see what you're saying about the format.
**Lukas Hering** 17:58 the.
**Aaron Abbott (Google LLC)** 17:59 Yeah.
**Lukas Hering** 18:00 Like I just put it in Zoom chat. So like with the Python logger, you can do this, right?
Actually, yeah, this is just what.
ChatGPT gave me, but, right, so, like, that string will only be constructed, right, when the locker is enabled. We don't really have an option for doing that right now.
I'm not sure if we do want to add it, because… I mean, the other thing I pointed out is, like, I'm pretty sure almost everyone in Python will be using the Python logger for the most part. I'm not sure.
What… what your thought is on that, but…
**Aaron Abbott (Google LLC)** 18:39 Yeah.
Why don't we… is there an issue for this already, Lukas? Maybe we can discuss it there.
**Lukas Hering** 18:45 For adding…
**Aaron Abbott (Google LLC)** 18:48 Yeah, the template.
**Lukas Hering** 18:49 Formatting, okay. Yeah, I don't… I don't… there isn't… I didn't see one, but I mean, I can add one.
**Aaron Abbott (Google LLC)** 18:56 Yeah.
I mean, I think, like.
Because it's basically just variadic arguments, I feel like we could probably design the API so we can open this possibility up later.
Or use, like… I don't know if the T-strings help, or the user could also just do, like, their own custom, support string class or something like that, which we could provide them as a wrapper or something like that. So maybe just make sure the API is open enough to allow this later on if we decide to add it.
**Lukas Hering** 19:31 Okay, yeah.
Yeah, I can create an issue for that. I yeah, I just I mean, if it's not something we need, then Like, we could also just kind of skip it for now.
Yeah, that's… that's all I have here, so…
**Tammy Baylis** 19:59 Cool, thanks for… Yeah, taking notes and continuing discussion.
And last topic right now, also from Lukas, declarative config end-to-end tests.
**Lukas Hering** 20:16 Yeah, just wanted, I guess maybe some, some eyes or thoughts on this. So, I've added this… Tests, suite, harness, thing, that… We'll basically go through a bunch of different scenarios, load a declarative config, With the collector config.
And, you know, test everything works end-to-end.
It was adding like three minutes of CI time because it would do everything sequentially.
But I was actually able to parallelize it, at least running on Linux.
Which is what CI does, so… yeah, just, yeah, I don't know if people have, like, ideas on better ways to do this. Basically, what ends up happening is that each scenario actually spins up its own Hotel collector.
And Python process.
So everything's, like, very isolated, Since with, like, a global, collector, if you… If you have a bunch of listings enabled, it could end up sending us the wrong one, so… Yeah, if we're good with this, I can… we can merge it, or, like, if there's ideas for improvements here.
I had one other item that… oh, yeah, the, so this is, I actually realized this is kind of general enough to to the point where we can maybe even just like replace the old docker tests.
So, I was also wondering, like, do we think we want to just do that, and just, like, kind of make this our standard for doing our, like, integration tests for the SDK, since this uncovers everything that that does, and it's also more parallelizable? So, yeah, that's all I have. Aaron?
**Aaron Abbott (Google LLC)** 22:14 Yeah, I haven't looked at this one yet, but I… I guess for… What does it have to do with declarative config, like the Docker testing and all that? Like, is it, I didn't understand the connection, because the declarative config is just, like, the YAML format, right?
**Lukas Hering** 22:32 Yeah, so, I mean, this just kind of tested, like, everything completely end-to-end, I guess, like… So, you can see each scenario defines a declarative config, and the test runner will just Execute that run.py script with that config.
And then in the scenario file, you just kinda say, like, okay. I want these I mean, I need to make sure that these spans with these attributes are present or whatever.
**Aaron Abbott (Google LLC)** 22:59 Oh, I see, I see.
Mmm.
**Lukas Hering** 23:01 So, like, I mean… It just, yeah, it just, I mean, it literally tests everything end-to-end, including the declarative config from, like, process initialization all the way to, like, exporting.
**Aaron Abbott (Google LLC)** 23:15 I see.
Yeah, I mean, this seems like a good replacement for the general Docker tests.
I guess… One, can you go to one of the configs, Tammy?
Yeah.
Okay, so we inject… Oh, we have a single port, though.
Yeah, exactly.
**Lukas Hering** 23:37 I.
**Aaron Abbott (Google LLC)** 23:38 Yeah.
**Lukas Hering** 23:39 I managed to, with the help of Claude, just use like virtual Docker networks. So like.
**Aaron Abbott (Google LLC)** 23:47 Yeah, yeah.
**Lukas Hering** 23:48 Yeah. Everything yeah. I have the test runner running, like, sixteen parallelism, and it completes in, like, around thirty to forty seconds now versus three minutes.
**Aaron Abbott (Google LLC)** 23:59 Gotcha.
Yeah, this seems super cool. I know, also, I think Riccardo was working on, and Ludmilla were working on, like, Weaver tests, and… it looks like the nice part about this is for… for stuff that's not semantic conventions, you don't have to write… you can just write some Python assertions, and also it's kind of nice if you don't want to do, Rigo?
but there seems to be some overlap there, right?
**Lukas Hering** 24:28 Yeah, that's… so I don't know if we want to, like, create some, like, mega framework and unify everything.
There actually, like, isn't too much manual, like, everything is kind of ran through that, like, scenario.yaml.
But it just kind of… You know, you just kind of… Describe what what telemetry you expect to see.
**Aaron Abbott (Google LLC)** 24:55 Yep.
Okay, well, I'm just… I wasn't working on that one, I was just… I guess, Ricardo, if you're on board with this one, too, maybe you approved it already. Seems just like some overlap, I would kind of call out, that's it.
**Dylan Russell** 25:10 What's the purpose of, like, the collector here? Like, could you have this… All set up without the collector.
**Lukas Hering** 25:20 I mean, we want to test the actual, like, if I'm using a gRPC exporter.
We want to test it, like, fully end-to-end.
So.
**Dylan Russell** 25:31 Do we need the collector for that? Like, can't we, like, just… Have it export to… like, something else.
Like…
**Lukas Hering** 25:43 Yeah, we could spin up our own, like, gRPC server. I guess the idea here is that, like, in production, you know.
like, most people are going to be running this behind a collector. So, We'd wanna, you know, it… we'd want to… we want to test as closely as what our users are using in production, is kind of the idea here.
Are, like, what is the concern, just, like, the overhead with spinning a bunch of those containers, or…
**Dylan Russell** 26:11 Yeah, it just seems like… Could get rid of that completely.
And just simplify it, but… Yeah.
**Emídio Neto** 26:22 I'm more in favor to keep the collector, because you can send both gRPC and HHP.
And you can… if I'm not wrong, you are using, OTLP Sync. Right? Which only receives HTTP, so… The collector is good at that point.
**Lukas Hering** 26:40 Sorry, we're using what?
**Emídio Neto** 26:43 The… Hotel P Sync.
I'm seeing you are exporting to… other PC can point.
Right.
**Lukas Hering** 26:53 Oh, yeah, so, like, the way this works is, like, the actual Python process will export to Collector, and then Collector will send it back to the PyTest process.
**Emídio Neto** 27:02 Yeah.
**Lukas Hering** 27:02 I'll be the…
**Emídio Neto** 27:03 Yeah.
And you are sending through Http.
So it does make sense to me to keep the collector.
**Lukas Hering** 27:12 I mean, this is… I guess, I mean, we can remove the collector, but… really… like, we want to see, I guess, I mean, the reason that the… I think the main reason that the collector is there is to see that this actually integrates with the collector, right? If there was somehow some sort of specific interaction with the collector there.
Right. I mean, the other thing is, like, so this does… I mean, it tests every single exporter that we support, so this is including, like, Prometheus, Prometheus scrapers as well. So we'd have to basically, like, update the, like, our test sync to, like, accept every single format.
Which is kind of a pain.
like, for me, this kind of, like, having this run, like, gives me, like, really high degree of confidence that our SDK is working, because, like.
like, in production, you know, my Python app's sending it to my collector, which then sends it somewhere else, right? So, versus, like, I mean, there could be, like, specific bugs in our sync implementation that, like, you know.
It's unlikely, but yeah, I mean, that's the kind of idea.
Yeah, Aaron.
**Aaron Abbott (Google LLC)** 28:37 Yeah, I was gonna say, if we have, like, do we configure the collector at all? Is there an option to configure it? Because I can imagine some, like, testing it with some processors, and I think there was discussion of, like.
Integrating Weaver or the Rego stuff with the collector, so it might… I'm just throwing things out there, but, like, there's… rebatching in the collector and stuff like that, and we can make sure it plays nice with Python.
**Lukas Hering** 29:02 Yeah. So there's, like, that collector config there is the default one, so each scenario will use that by default, but you can override the collector that's used.
So… let me see if I… do I even overwrite any of them? I think I just left it basic for now, but yeah, you could imagine we could do… Stuff where we have, like, you know, different pipelines doing different things and stuff.
**Aaron Abbott (Google LLC)** 29:29 Yeah.
**Lukas Hering** 29:30 Or, like, just straight up add the, can we add, like… is there, like, a schema validator processor that we can just add in here?
Like, that would be one way to do, like, semantic conventions checks.
**Aaron Abbott (Google LLC)** 29:44 Yeah, I think there's some work on it, but it kind of overlaps with Weaver and it might just wrap Weaver. I think Ricardo, maybe you know more about that.
**Riccardo Magliocchetti** 29:55 Yeah, like, I was going to ask two questions. The first one is… Do you think we can also move the current docker test to this scenario around now.
And does it make sense for you?
And the second one is, do you think we can swap Eventually, like, we can configure this thing to run Weaver instead of the collector.
**Lukas Hering** 30:26 Yeah. Yeah. The first point yeah. That's what that was one of the points I was making. So, like, we can like, this should I need to make sure we cover everything, but, like, this already has all the coverage that the other Docker tests have, so we can probably remove the old ones or just, like, rename this.
And then the second point.
Yeah, I just didn't want to, like, you know.
create some, like, behemoth PR that has, like.
20 moving parts. So like, yeah, there's definitely room to expand this to incorporate Weaver for the actual semantic conventions validation. This is more just.
**Riccardo Magliocchetti** 31:01 Like, I didn't mean… like, in BSPR, I mean, we can extend the… The finger… Okay, thanks.
**Lukas Hering** 31:11 Yeah. Yeah. Totally. Totally. For sure. Yeah.
Okay, yeah, I guess the last… I guess, do we think… Having the collector in this process, like.
In my mind, it's valuable for the… for validation purposes.
Do we want to do everything we want to remove it, or.
**Emídio Neto** 31:49 I'm favor to keep because you already have collector in the existing Docker tests.
So, I don't think it's… It won't add overhead in this CI, in my opinion.
**Aaron Abbott (Google LLC)** 32:05 Out of curiosity, which collector image do we use?
**Lukas Hering** 32:10 I think it's the contrib one.
Okay. Let me double check. You can look in the…
**Aaron Abbott (Google LLC)** 32:18 Yeah, yeah, I was just asking, because I know it's, like, an enormous, typical, like, static Go binary, so if, with the parallelism, the, like, resource overhead is a concern, we could probably… Some… some things down.
**Lukas Hering** 32:35 Yeah, we could build our own, I guess. Actually, I need to double check. I'm not sure if we use the contrib or the default.
**Aaron Abbott (Google LLC)** 32:41 Yeah, I think the — yeah, just because the contrib is — I want to say it's like 100 megabyte binary, so.
**Lukas Hering** 32:49 Yeah, at least I think it should be caching it. Are you worried it's just like memory usage or like?
**Aaron Abbott (Google LLC)** 32:54 Yeah, yeah, yeah.
**Lukas Hering** 32:56 Okay, yeah.
Okay, yeah, we can probably… can… yeah, this is all I have here, just… just wanted some… Thoughts on what people had, so… Yeah, we can.
Wrong.
**Tammy Baylis** 33:17 Awesome, thank you.
No more listed topics, but is there anything anyone else wanted to talk about?
Okay, I think we can end early today then. Thank you everyone.
See you next time.
**Aaron Abbott (Google LLC)** 33:45 Thank you for running it, Tammy.
**Tammy Baylis** 33:46 That's really cool.
**Emídio Neto** 33:48 There it is.
**Lukas Hering** 33:50 Thanks.
