SIG: eBPF instrumentation
Date: 2025-09-03
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Mattia Meleleo** 01:10 No, no.
**Tyler Yahn** 01:11 Morning.
**Mattia Meleleo** 01:13 Good morning.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:16 Great.
**Mike Dame** 01:17 Hello.
**Nimrod Avni** 01:20 Hello!
So…
**MM Mario Macias** 01:45 Good morning, good afternoon.
**Tyler Yahn** 01:48 Morning. How you doing?
**MM Mario Macias** 01:51 Good, good.
**Tyler Yahn** 01:53 Nice.
Yeah, so we could probably get started here in just a second. Looks like we have a lot of people on the call. I'm looking at the agenda doc as I get my Zoom setup set up. I've only got one thing on there, that's to review some PRs.
So maybe we can just wait a little bit. If you have topics you wanted to discuss, go ahead and add them there, otherwise we can jump in in just a second.
Awesome. Okay, well, welcome, everyone.
I think this might be the first one we're having where some people from vacation are coming back. I think, Nicola, it's good to see you again. Yeah. So, yeah, happy to have you all back.
If you haven't yet, go ahead and add your name to the attendees list, I also forgot to mention that, and we can jump in here and just, just do a little review of the open issues and see if we can't make sure we're making some progress. Looks like there's… Quite a few. Okay.
So, start us off, this Kafka 2.8, 4.0 integration testing. This is something we talked about last week and the week before. It does look like it has a review at this point.
5 days ago…
**Mattia Meleleo** 03:36 I think it has been proved, though, that there is just one test failing, but I think it's just flaky.
**Tyler Yahn** 03:43 Okay, it just needs to be run again?
**Mattia Meleleo** 03:45 Yeah.
**Tyler Yahn** 03:56 Okay, cool, alright, well, we'll rerun that, and then, hopefully this clears it up. Have you, Synced with Maine.
Mattia?
**Mattia Meleleo** 04:08 Probably did, but I don't know when.
**Tyler Yahn** 04:12 Yeah.
**MM Mario Macias** 04:12 I think if you resync again with main, you will get much quicker integration tests, because Stefan Para split the integration tests in multiple test cases, so now it.
**Mattia Meleleo** 04:26 Yeah, yeah, yeah, I saw.
**MM Mario Macias** 04:27 10, 15.
**Mattia Meleleo** 04:28 I'll, rebase them.
**MM Mario Macias** 04:30 Okay.
**Tyler Yahn** 04:30 Okay.
But yeah, otherwise this looks ready to go, it just looks like it needs to get merged. Okay.
Thanks. Alright, next up, trace export internal metrics, BPF and internal metrics. This is something, from Nimrod. You had looked at this I think we looked at this last week, yeah, 2 weeks ago.
**Nimrod Avni** 04:49 Yeah, I think, I don't remember, I think there was some test, I didn't manage to see if it's, like, some flaky test, or actually something failing. And I didn't get a chance to look at that, and I saw… Rafael left a comment, and I commented just, like, a couple of hours ago.
I don't know if that's one of the… I don't remember which ones are, like, the flaky ones.
But yeah, we just discussed about, like, the self-instrumentation thing, that it's… Whatever written there. But I'll try to… Yeah, I'll also rebate so we can run the integration test quicker.
**Rafael Roquetto** 05:33 So…
**Tyler Yahn** 05:34 Yeah.
**Rafael Roquetto** 05:34 like… Sorry, go ahead, Tyler.
**Tyler Yahn** 05:37 No, go ahead.
**Rafael Roquetto** 05:38 I was gonna say, so do you wanna enable that exporter traces after all?
**Nimrod Avni** 05:46 it's not for… it's not for traces, I mean, it's for… Yeah, it basically counts the amount of traces OB sent as a metric. That's what, I think we were missing until now. There was, like, in the internal metrics, we described a metric that counts, total traces exported and total trace export errors, but we just never reported it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:09 Hmm.
**Nimrod Avni** 06:10 So it's a metric. It's a metric that just relies on the traces we export?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:15 Yeah, one thing to note is, I'm not sure if it's happening still, I haven't looked… I'm sorry, I haven't caught up at all. I was just going through my email and messages, but, The internal exporter… For internal metrics for the exporter, would also send spans, so just make sure that that's disabled, because it does make these silly spans, so you get, like, a span for exporting the traces, so you fill up your tracing database with junk, essentially. Which is why…
**Nimrod Avni** 06:49 Hmm. I can look at it, because there's, like… Basically, there's, like, the normal path of, like, how we export metrics and traces, and that's done, like, you know, and that's exactly what this, attribute, like, filters out all the self-instrumentation stuff. But there's, like, the internal metrics, which are, like, reported I think there's, like, either through Prometheus or through, OpenTelemetry, and it's, like, a different exporter pipeline, and then the export… like, specific metrics regarding how much OB… I don't know how many, like, processes there are, and, like, sent metrics and traces. I also added, like, the BPF stuff, like, BPF size and BPF events.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:33 Nice. No, no, I totally get it, yeah, I know what you're trying to do, and I think that's a good thing to do. I was just, In the hotel… If you enable the… the… I haven't looked at the PR, I have to do it, but we disabled it. We used to have it initially, but then we disabled it because The instrumentation that was… if you say, enable internal metrics for the traces exporter.
It also produces spans that tell you each time you've exported trace, so then you actually end up reporting OB as a service that exists in your cluster.
And all it does is reports how long it took for individual, export to happen. Each time it does an export of traces, it produces this Trey Spann.
That goes out, which is… we want… didn't… I mean, it… it looks kind of confusing to customers from what we got as a feedback.
They're like, what's this service? I don't know, like, who's producing this, and stuff like that. So, if there's a way to enable just the metric side, and not actually cause it to send traces, that would be awesome. That's one thing that…
**Nimrod Avni** 08:47 I can… I can check. I think that's what I… like, in the code, basically, I just… when I took, like, the normal, like, exporter, and, like, I said, like, before you export, like, report the metric, and, like, if there's an error.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:01 report the error, it's a thing, it's traces.go or something?
Just like a very…
**Nimrod Avni** 09:08 And basically, yeah, like…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:13 Yeah, that's what we did. Yeah, that's what it used to do. So you would do this instrument that trace is exported. We just need to double-check that it's not going to generate these pants. I'm sure there is an option to say what you want. I think our initial implementation was doing this exact thing.
But, I, yeah.
**Nimrod Avni** 09:31 I'll check that again, I think you can look at the Instrumented Traces Exporter. It's also, like, a class we…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:38 Yeah.
**Nimrod Avni** 09:39 down, and I think it just does basically report metric, and yeah, I'll make sure to test it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:43 Just make sure, if you have, like, if you're exporting both traces and metrics, just make sure that you don't see, like, these single spans that are just essentially telling you, all this token to the collector, and… and it just gives you individual export time for each time it did push traces.
I mean, it might be useful to some people, I don't know. Like, you were debugging OB export to collector, if it error out, but I don't know if we collect enough information.
**Nimrod Avni** 10:12 we can just, like, remove the filtering out of OB, and because it's, like, gRPC, we can.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:19 Yeah.
**Nimrod Avni** 10:19 View it as a span, a normal span.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:22 Okay, okay, just, yeah.
**Nimrod Avni** 10:26 I'm a cool… I'll check that out.
**Tyler Yahn** 10:29 Okay, cool, that sounds good. One of the things I was also gonna say is, I would… double check, Nimrod, if you're able to… In those integration tests, just download the actual log files and look at them, because usually having 3 fail altogether is, just talking statistically, it's pretty rare. So, like, I would see there's maybe something actually going on here, So, just a heads up, yeah, you go here, in the summary is where I've been able to find it, although…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:00 This is the top, left corner.
**Tyler Yahn** 11:03 There's a specific summary, yeah, and then Tesla. Okay, yeah.
**Nimrod Avni** 11:07 But, okay.
**Tyler Yahn** 11:07 Download test logs, yeah. And then you have to unzip them, but, yeah. You figure that part out, yeah.
So yeah, that's where I take a look. I know… I don't know if Steven's on… We had talked again, Nicola, about flattening those into the logs themselves, but we haven't actually seen any progress on that, but yeah.
Okay, alright, moving on, fixed Prometheus metrics export is missing the SDK version in target info.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:36 Okay.
**Tyler Yahn** 11:37 Yeah, I think… We talked about this as well…
**MM Mario Macias** 11:43 He is.
**Tyler Yahn** 11:43 That's true.
**MM Mario Macias** 11:43 provided… I provided some feedback and some guidance, but I… I haven't seen any… Any new commit for that?
**Tyler Yahn** 11:55 Righty, okay.
Alright, so it looks like we're just waiting on, feedback from the original author on that one.
Yeah, similar here. Okay.
Okay, feature improving Kafa parsing. This is something I think we also talked about last time we were gonna split up. This is also based on, Mattia's PR, so this is something we're still waiting on, on that one, right?
**Nimrod Avni** 12:18 waited until Matias PRB merged, and then see if it's still too much, and if it's still, like, split it up to them.
OPRs.
**Tyler Yahn** 12:27 Yep.
Okay.
Awesome. Well, looks like the TSPR is about to merge, so, sorry about the delay on that one, so, yeah.
Okay, next up is the fix, Docker RM requires at least one argument.
This is from Steven. We talked about this last time.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:48 Yeah, Steven is at another SIG. I believe he joins the Kubernetes SIG, so…
**Tyler Yahn** 12:54 Yeah. So he's… he might join a bit later, so maybe we can…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:59 Delayed talking about this until he's back.
**Tyler Yahn** 13:02 Yeah, it looks good. I don't know why Mario's review is getting… Oh, it's probably because he re-asked for it.
Because he changed his approach. We're not actually doing the shell commands anymore.
Okay.
Yeah, I'd have to check this… This is… this is, I think, a problem between, the Linux and, BSD-based make command is what's going on here.
Okay, I should probably… get to reviewing this. I've been out for a little bit, so I haven't got to doing this, but okay, yeah, this just needs review, I think is what's going on here.
Mario, are you on a Mac, by chance?
**MM Mario Macias** 13:48 Yes, I am.
**Tyler Yahn** 13:50 Could you double-check this? He's pushed some new things, I think, like, actually, maybe, maybe it's more on me, because it's about… I want to make sure this actually works on all environments, but I'm guessing, because Steven's on a Mac, he probably already tested it, so maybe just ignore that. I probably just need to test it on a, like, a Linux environment.
**MM Mario Macias** 14:06 I will… I will anyway give a… give a… have a look, yeah. Okay. Yeah, yeah, more eyes on it is always good, so…
**Tyler Yahn** 14:16 Okay, another WIPM, so work in progress, so something we talked about, we'll wait on this one.
Next up, Nimrod, do you want to allow filtering on the Kate's, container name?
**Nimrod Avni** 14:29 Yeah, we had, some client who asked for it because, that's, like, didn't have a, like, a legit way of… like, they wanted to filter out a specific container, not, like, by pod name or whatever, so I just added it wherever all the other metadata is, and I… Thought it could be cool.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:50 Cool.
**MM Mario Macias** 14:51 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:52 Yeah?
Sounds good.
**Tyler Yahn** 14:54 Great.
Yeah, it looks like it's already got one review, looks like it's ready to merge.
**Nimrod Avni** 15:01 I think there's also integration tests, probably… Yeah, this one… Leave it.
**MM Mario Macias** 15:07 Yesterday, I uploaded a new attempt to fix this multiprocess flaggy test.
So, yeah, I don't know if that was the reason of the failure, but if you can try to also rebase or update domain and… And see if they passed.
**Nimrod Avni** 15:28 I already ran it, but if it happens again, then I'll rebase and try again.
**Tyler Yahn** 15:35 Yeah.
**MM Mario Macias** 15:36 If not, we can have a… if not, ping us, ping me if you want in the… in the Slack channel, and we can have a look together to see if something has… what else might be missing.
**Nimrod Avni** 15:51 Cool.
**Tyler Yahn** 15:55 Okay.
Waiting on Sioc for that one.
Next up, fixed CI codecove action input is files? Yeah, not files, what?
It definitely is. I ran into this as well.
That's… oh, that's right. I ran into this and it does silently just fail, so that's probably why I haven't been noticed, but yes. Cool.
Yeah, this looks great. Let's get this merged.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:26 We probably need to re… I guess there's some unit test that's flaky?
Alrighty.
**Tyler Yahn** 16:31 No, so this is for the CI, so this is GitHub Actions, and so it's the… this is the last step where you're gonna upload the code coverage report.
And, if this fails, it'll be in all the, CI jobs, but it literally is just a log line, it doesn't fail the step itself.
Actually, where was that being run?
Take a look at the example integration…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:00 Let's see, I failed in the test.
**Tyler Yahn** 17:02 Yeah… or Flintish. It's… it's… But I imagine it's failing for something else, Guess that these are still working.
Maybe we can take this.
Yeah, it's coming up.
So it'd be this, report coverage. This… this part will… it'll, like, it'll succeed, in the… in the sense that, like, it won't, like… cause any problems, but the log message says that it will actually… it was malformed, and it will…
**MM Mario Macias** 17:37 It should…
**Tyler Yahn** 17:37 Fix.
But yeah, that is kind of interesting. I did just notice that we had a Maybe… Just take a look at this, sorry.
Get a little nerd sniped.
Huh.
Okay.
That doesn't look like a temporary failure. Probably need to take a look at this, okay.
Okay, I will keep this tab open, try to take a look at this after the meeting. I don't know what would have changed, but… Okay, next up, yeah, same thing. Restore coverage, report is failing.
Apparently, the CodeCub supports automatic merging reports.
Yes.
**MM Mario Macias** 18:32 Yeah, this is because when Stefan, split the integration tests, he… he removed the coverage.
Stuff. So, it is just restoring it.
**Tyler Yahn** 18:51 Okay.
Yeah, alright, that sounds good to me, yeah.
Okay, also from Steven, see, I shard both Kate's and non-Kates integration tests. This looks like a draft, so it's a work in progress.
So, I… no reason to review just yet, if you haven't. Yeah, looks like it's still… Dealing with some… CI issues and also trying to get this to work. So, yeah, we'll keep an eye on this one.
Okay, and then, last up, Mario, limit cardinality of spam metrics.
**MM Mario Macias** 19:41 Yes, we found that for span metrics, the trace name, could lead to cardinality explosions in customers with many, many routes.
This is fine for traces, but for span… for spam metrics, this is a problem. So, we enabled a configuration option that led Keep track of the different routes for every service, and then when the routes for a given service surpasses the given maximum number, it will start reporting the spam names as aggregated. Only for the spam metrics. For the traces, it will remain.
unchanged.
**Tyler Yahn** 20:34 Okay. Yeah.
**Nimrod Avni** 20:35 That's… that's, like, per, OB pod, right? So, like, theoretically, it can be… I don't know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:44 Yeah, that's.
**Nimrod Avni** 20:44 I think if I give it, like, a different paw, it, like, depends.
**MM Mario Macias** 20:47 Yes.
**Nimrod Avni** 20:48 If it's really high cardinality, where there's, like, no matching.
**MM Mario Macias** 20:53 Yes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:55 Yeah, the heuristic is imperfect in a sense that it looks for… words, right? So if it sounds like a word, it will… it will actually let the path go through, so if you have, like, an API like GitHub.
Where every part of the path is actually a reasonable name, you will end up with high cardinality.
**Nimrod Avni** 21:18 Yeah, that's interesting, trying to think.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:21 Maybe there's a better way for us to do this, but…
**Nimrod Avni** 21:26 I think there's, like, an experiment of, like, doing this in the collector or something, but that will require… Like, a central… like, a central collector.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:36 Collector, yeah.
**Nimrod Avni** 21:37 So I don't know if that's.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:40 Yeah, they're actually using… yeah, they're using the same code that we have, right?
**Nimrod Avni** 21:46 Yeah, for the route, like, temp… the detector… I think they extracted it to a processor.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:52 Yeah, yeah.
That's right, yeah, so they're building a processor based on the same code that we have. The… however, it will be susceptible to the same problem, like, if you have API that's, like… if you look at our GitHub API for this issue, it's like… GitHub, OpenTelemetry, OpenTelemetry, maybe eBPF will trip it over, but if it's anything other than that, like any reasonable name, those… all those routes look normal. So if you're, like, browsing subpaths and folders into GitHub.
It could easily be, like, extremely high cardinality.
Yeah.
We have the other modes, but the other modes are just way too bad. They just, eat up all the roots and make them into…
**Nimrod Avni** 22:43 Maybe, like, the solution is, like, you know, using this and, like, combining it with… you know, like, predefined routes, like github.com slash star, like, I don't know, but then, like, you need some manual configuration thing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:58 Yeah, so it almost… like, if Bobby had storage, you would almost sound like we should… you know, kind of detect them on the fly, and then produce a low cardinality root out of it, right? Something like a pattern. Keep it in some sort of, like, a local storage. Next time you boot, you kind of read them back on, and… but… yeah.
**Nimrod Avni** 23:21 Huh?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:22 Has this being a demon set being restarted and redeployed, and I don't know if it's… Any way possible to do something like that.
**Tyler Yahn** 23:32 Do we use the patterns in the, like, the HTTP libraries?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:39 No, we don't. So that's an interesting one, right? So if it's a Go application, we could technically read the information from the APIs, right? Is that what you mean?
**Tyler Yahn** 23:48 Yeah, like, modern, like, Go has ways that you can have, like, templatized, like, path names, right? Yeah. And so, if it's a templatized path name that does the pattern matching in, like, the Go library, like, you can get that from the Go, but I know it's, like.
Mux and Jin and a few others also do this. So there's, like, it's based on libraries, though, like, it would be specific to that library.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:11 Yeah, but Go applications might be doable, yeah.
**MM Mario Macias** 24:15 Yeah, I think we can even read all the strings in executable, and anything that looks like a pattern, a standard pattern, maybe… maybe we can get that. I think it's more problematic in…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:32 Exciting.
But it helps.
**MM Mario Macias** 24:34 in Ruby or Python, in which you will need to read the files, and if they are in a container, probably there's no easy way to access the files.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:44 Yeah, so the GitHub is a Rails app, right? So, can we read that somehow?
Maybe, I don't know, maybe there's a way, like, if… if it's a well-structured app, we kind of scan the code and… I mean, we have access to the roots of the… Of these… of the running process, so we can tap into their file system and scan for patterns and…
**MM Mario Macias** 25:12 Maybe.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:14 Maybe it's something we should start looking into, you know, honestly.
**Tyler Yahn** 25:19 I think this is a good start, at least. You know, maybe.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:21 Yeah.
**Tyler Yahn** 25:22 Perfect in all the ways you describe it, but… Yeah, I think… I mean, I definitely think that you'd… I would, you know… I'd much rather get back the pattern that I put into the system, in my span names, if we could do that, but, like, I think this is, like, better than having my backend blow up, right? Like, that's… that's more what this is trying to solve, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:43 It's sort of like a fallback. Okay, something is weird is going on. It's not perfect, right? You restart Obi, next time you make a different combination of roots you see until you get the aggregator, right?
But, still better than exploding.
Permanently, right.
**Tyler Yahn** 26:01 Yeah, yeah, and I think that's kind of more… it's the same with, what we do with metrics in general for cardinality limit, with attributes, so, like, if you have the cardinality limit set for attributes, it'll automatically, like, do exactly this. It'll truncate, to some sort of, like, thing after youhip.
like, 2,000 unique ones by default.
So… It's not… it's not consistent, but it's also an error case, so it's like… it kind of is more just a… prevent… Worstick things from happening than being correct, I guess is the way to say it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:35 Yeah.
Yeah.
**Tyler Yahn** 26:37 So, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:38 Yeah.
**Tyler Yahn** 26:39 Looks like it has a review. I'm sure more review would be great. It's been open for an hour, so, looks like we're working on CI as well, but…
**MM Mario Macias** 26:47 Yeah, something… something has broken in the integration test. I will… I will have a look what has been broken.
**Tyler Yahn** 26:55 Yeah, okay.
Okay, cool. Alright, that's the end of the, open pull requests.
I'm gonna pause here.
Matia opened up an umbrella issue for flaky tests. I don't know how long ago you put that in chat, but I'm just seeing it now. Thanks for… thanks for doing that.
Any other topics people want to talk about? Things that aren't on the agenda?
Okay, well, I guess just a reminder, KubeCon's coming up for those that are coming. I think, I think I mentioned this last time?
Sorry if I'm a broken record, but you should try to come to the Maintainer Summit as well, if at all possible. I know a lot of people are gonna be there. We're gonna have a little bit of a group meeting for OTEL, which would be great to see.
I… I don't know exactly if, So it's for maintainers, but I think if you're a part of this project, we can get you in. I'm happy to help you, whatever sort of sponsorship that is required. So, yeah, we'd love to see more people there, so if you're on the call, or you're coming in later, yeah.
**MM Mario Macias** 28:11 I'll be there.
**Tyler Yahn** 28:12 Awesome. Well, I'm looking forward to seeing you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:15 I still haven't booked my flight, so maybe I'll change my mind about missing the…
**Tyler Yahn** 28:20 Yeah, I also understand, like, life outside of work is also important, so, but yeah, I, yeah, I haven't booked either, but I'm planning on being there, so…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:29 Yeah, unfortunately, I have 3 other trips before it, so it's really putting a little stress on my family. I'm at home, you know? Just, I'm out every week in October and beginning of November, so…
**Tyler Yahn** 28:42 Oh, wow, yeah. Yeah, that is a lot.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:44 Yeah.
**Tyler Yahn** 28:46 Well, cool. I see Steven just joined, unfortunately, right at the end here, but, yeah, maybe… Steven, I don't know if you wanted to talk about something in specific. We looked at a bunch of your PRs, looks like some of them are just blocked on CI and that kind of thing, so we're waiting on that to merge, but anything… That comes to mind that you wanted to talk about before we end it?
**Stephen Lang** 29:05 No, no, I don't want to hold things up. I was just wanting to drop in in case anybody had any questions about the PRs. I don't have the ability to rerun the checks, so I keep having to push new commits.
So I can continue trying to get the, the green check.
**Tyler Yahn** 29:21 That is annoying. I forget about that sometimes. Okay, well, we'll try to stay on top of that and, and get these through.
Cool.
Alright, everyone, well, it's good seeing you, thanks for joining, we'll see you all in a week's time, or aspicuously till then.
**MM Mario Macias** 29:33 But I…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:35 Wow.
