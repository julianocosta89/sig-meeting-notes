SIG: Prometheus WG
Date: 2025-12-05
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/AUh8C09OgCbVsfKupoPKKcltZE70mIMNOc-0VafShJV7iETZsgXzZwpITZlKjTDc.9LyD0EpOeePruMxc
============================================================

## Zoom Recording Transcript

**krajo** 00:39 Hey, Hayden.
**David Ashpole (dashpole)** 00:47 I was muted. Hey.
**krajo** 00:49 Bye.
Notice.
**Arthur Silva Sens** 01:20 Bloke.
Not sure if anybody else is joining.
I added Prometheus receiver stuff, at the backlog.
But, I don't know, it doesn't need to be first. What people want to talk about first.
**krajo** 02:42 Could you take my… points, because I have to leave in about half an hour.
**Arthur Silva Sens** 02:48 Yeah, yeah, sure.
**krajo** 02:50 Okay, so… Yeah.
Right, I remember that,
So, first option, or first question is, does anyone know if somebody's working on the… Making the…
the conversion code.
you know, Promatus to OTA, OTA to Prometus.
put into some common library. Because I remember Yurai said that he might try that, but I don't think he did, so…
I guess that's not… Not happening anywhere, right? Or we don't know about it.
**David Ashpole (dashpole)** 03:25 There's the Prometheus Translator Library.
It's in Prometheus.
Or not in Prometheus, Prometheus, but, like…
**krajo** 03:35 Yeah, that's an idea. I don't know if that's a good idea, but yeah, that's certainly a place that's kind of natural for it.
**Arthur Silva Sens** 03:44 a TLP translator, it translates names, but you mean about the Go objects, right?
**David Ashpole (dashpole)** 03:54 co-op.
**Owen Williams (he/she)** 03:56 Yeah, I'm not aware of anything. Do we have, like, multiple implementations of it?
**krajo** 04:02 I mean… The question came up because of the second one, is that…
I have a new colleague, a fairly new colleague, Lauren, who's looking into
you know, issues around open telemetry, and he's going… he started to contribute.
stuff. Not to the Prometus receiver yet, but I think it's probably coming.
And we noticed that if you use the Promatous remote write exporter.
It never sends any CBs.
So, native histogram custom buckets. It always converts the open territory histograms into classic Prometus histograms, which is… may not be what you want. You might want to send, you know, the native histograms, which are more atomic and have some nice qualities.
**David Ashpole (dashpole)** 04:50 And I would like to…
**krajo** 04:53 Sorry?
**David Ashpole (dashpole)** 04:54 Is this… do you know if this was remote, right? 2.0 or 1.0?
**krajo** 04:57 It can only be 2.0.
**David Ashpole (dashpole)** 05:02 I told Jirai to do this. I thought… I thought we did, but maybe… maybe it's still doing the old thing.
**krajo** 05:08 No, he tested it, and also in the code, it does the conversion to the…
So anyway, I think I can write an issue for it, but then the question becomes, like, okay, but we do that already, that kind of conversion.
in the…
what is it called? In the auto receiver in Prometheus, which is converting from OTA to Prometheus.
And then we do it in the…
I'm blanking on the other place.
But I'm sure there's another place where we already do this, so it would make it, like, 3 places where we do this. So anytime you are converting from the OTAL model to Prometus model in some way.
We're doing the same things.
**Owen Williams (he/she)** 05:55 That could go in OTLP Translator, I think, because it's got the same purpose, so that would seem to be a fine home for that.
Depending on what things need to be imported, though.
**Arthur Silva Sens** 06:09 Yeah, I think the problem is that it's… Prometheus can be several stuff. It could be client model, it could be Prometheus remote, right?
And I think the multiple places that you're seeing, they are different from Itus.
logo objects. It is not the same everywhere.
**krajo** 06:35 Yeah.
Still, it's kind of weird to have the same logic different places.
Okay, well, I… If you have…
time for this… I'll create the issue for this to happen, and then somebody can implement it right there in the remote flight exporter, that's fine, and then we can iterate on
How we can, you know…
**Arthur Silva Sens** 07:07 Yeah.
**krajo** 07:08 i.e.
**Arthur Silva Sens** 07:11 Yeah, but we need to find a list of places that translates OTLP to the same Prometheus thing.
If it's… several places to remote ride, then I think that makes sense, but if it's only one
I don't see why.
**krajo** 07:27 yeah, that's fair.
Yeah, you're right, we don't translate to remote fight anymore in Prometus. In fact, David and I rewrote that, so yeah. Yes.
Yeah.
Okay.
That answers my question.
Let me make some notes…
But not here, but… Here…
Okay.
And then, the other thing that…
I wanted to bring up is a PR.
That's about… Info metrics.
So… Oh yeah, David, you already replied on it, I didn't have time to look at that.
Was there any conclusion already that I'm not aware of?
**David Ashpole (dashpole)** 08:41 I mean, I just shared what the spec was. Like, I shared the current state. I think it's all debatable, you know, as to what we should be doing.
Right now, we say that the OpenTelemetry metric name is always the… Prometheus metric family name.
Right?
Yeah. And for open metrics, across the board, that means that we
generally don't include suffixes. So for counters, you'll be missing the total suffix.
that is on the individual underscore total actual series, and for infometrics.
You'll be missing the info suffix.
This is the first time I've seen anyone use an infotyped metric, though, so…
I'm not surprised that they were… Surprised, I just…
Yeah, Owen?
**Owen Williams (he/she)** 09:33 Didn't we just talk about this in the,
open metrics meeting, where we said that infometrics are special, they're specific to Prometheus, and they shall always end in underscore info.
Which is… The reason being, it's not the same as I did… Declared a metric in…
OpenTelemetry, and then the name is getting changed, because there is no equivalent in OpenTelemetry, so this is a different thing. I don't love it, but that seemed to be… that was the conclusion that was drawn two days ago.
**David Ashpole (dashpole)** 10:08 Yeah, I, but that's…
I think that's a slightly different question. I'll say… I'll be quick, and then Arthur, I'll let you go. I think the question here is…
Should we use the sample… for Open Metrics 1.0, should we be using the sample name or the metric family name?
And then for OpenMetrics 2.0, Should we be…
should we be requiring a suffix, or should we be more relaxed? And I think what we said was, we can require a suffix, because this is a Prometheus-specific concept.
But I… I think the question of whether we sh… like, OpenMetrics 1.0, in theory, could have added, like.
an info-created series, right, where it doesn't have the info suffix, and it has a different one, and, you know, like…
I don't know. I think they were trying… I see the idea, but…
Yeah, I mean, this is also confusing for counters, but it's still something we at least currently decide to do. We could undo that now that we
I don't know, are thinking of going stable, and just say that for counters and… Info-type metrics.
We use the sample name, because there's only one sample.
Maybe that's helpful.
Arthur.
**Arthur Silva Sens** 11:29 Prometheus doesn't parse infometrics, where… Or are they using this form?
**David Ashpole (dashpole)** 11:36 What do you mean by it doesn't parse? Does the parser literally not know what the info type is?
**Arthur Silva Sens** 11:41 Yeah, it does nothing. It doesn't store.
**krajo** 11:46 I mean, I would guess that they…
just want to use the metric as is, in whatever query, and I suspect that the info function would… would use the suffix, right? Or… or does it… or doesn't that care either?
**Arthur Silva Sens** 12:00 What I meant is, if the metric has type info, Prometus doesn't ingest.
**David Ashpole (dashpole)** 12:07 Really?
**Arthur Silva Sens** 12:09 It ingests as gauseous, And no, that's what people usually do, they…
they export info metrics as gauges, because that's what Prometus.
**krajo** 12:21 Oh, I see what you mean.
**Arthur Silva Sens** 12:22 chest.
**krajo** 12:23 Well, the thing is that if you look at the code in the receiver, it doesn't care about the type. It just cuts any suffix that it thinks is cuttable. So, the code, I think, is really done.
And… The fix that Christiane provided is to actually look at the type, and if it's info.
Then not do the cutting.
Okay, okay.
**Arthur Silva Sens** 12:51 So, the Prometus receiver…
can ingest infometrics, and will send it to some… someplace else that is not Prometheus, probably.
**krajo** 13:03 No, I think he sent it to Prometus, but he's missing the suffix, because the receiver…
you know, the receiver removes the suffix, so it gets rid of the info, but because the OpenTermetry model doesn't have an info.
Type, it's a gauge, which means that when you export it, there's no way to add back the info suffix, since you lost the type.
So if we lose I kind of agree with Christian that we shouldn't remove the suffix if we
Lost the time.
**Arthur Silva Sens** 13:36 Yeah.
**David Ashpole (dashpole)** 13:37 Hmm, okay.
**Arthur Silva Sens** 13:38 I can see that, I agree.
**krajo** 13:44 But of course, I don't know who would be break… like, who we would break with this.
If anybody out there is depending on…
losing the info now, like, I don't know.
**David Ashpole (dashpole)** 13:54 I mean, we can feature gate it and do the usual… Stuff to handle breaking changes.
**Arthur Silva Sens** 14:03 While it's not stable.
**David Ashpole (dashpole)** 14:07 Can we not do…
I mean, I guess we just need to… is it that we have to have a higher bar for breaking changes, or that we…
Can't do them at all.
**Arthur Silva Sens** 14:16 I… I think there are rules for…
for metrics, for stable components, I think we cannot change.
**David Ashpole (dashpole)** 14:25 But I don't understand it fully, to be honest.
**krajo** 14:34 I mean, iffy… We can sleep on this one, but if we agree that
We shouldn't remove the suffix. We could do the opposite.
we, you know, accept this PR, but also add the feature gate to
If somebody relied on this for some reason, turn it back on, turn back the… Info removal.
So, basically, make it a feature, What's the default now?
And break things while they are not stable.
**David Ashpole (dashpole)** 15:11 Well, it'll still be a feature gate, though, right?
**krajo** 15:14 Yes.
**David Ashpole (dashpole)** 15:14 Yeah.
**krajo** 15:15 the opposite.
**Arthur Silva Sens** 15:18 If it's a feature gate.
that means we are… we intend to make it stable somewhere, some… at some point, right? And once it's stable…
What do we do?
**David Ashpole (dashpole)** 15:33 I mean, you can… Strip or add suffixes.
Based on the Prometheus metadata type. I have done this myself. So it's, like, we could provide a transform processor to work around it.
My, my bigger thing is… I would almost want to revisit Counternaming?
If we're gonna do this… That, to me.
This is just, like, an outgrowth of…
What we decided to do for open metrics counters, where we don't include the total suffix.
But, like, I'm surprised that that isn't the more confusing part, right?
**krajo** 16:10 Wait, but but if you look at the PR,
It's adding the condition right next to the special Hendrick for counters.
Where we don't remove total, as far as I understand.
**David Ashpole (dashpole)** 16:22 If that's the case, then… then I agree with the change, but I… I missed that.
Like I said…
**krajo** 16:29 literally adding an OR.
**Arthur Silva Sens** 16:36 Like, wouldn't it be best to just follow this pack?
like, OpenMetric says it removes that remove, and OpenMetric 2 says don't remove.
we don't remove.
**krajo** 16:52 But then… You're depending on the…
input format, somehow? I don't know, that's… that seems fishy, but.
**Arthur Silva Sens** 17:00 And the… Yeah, we… people could work with what David said and with the metrics… metric transformer.
And we continue to add the metadata that the original type was info.
I mean, we don't do that, huh?
**David Ashpole (dashpole)** 17:20 Yeah, we store it in metric metadata.
Under the key Prometheus.type.
**krajo** 17:28 Oh, okay.
**Arthur Silva Sens** 17:30 this part here, like, we add permitous type to the metadata.
**krajo** 17:35 Okay.
**Arthur Silva Sens** 17:36 Yeah, that could be done.
**David Ashpole (dashpole)** 17:41 Yeah, we do… Google does some fancy handling of unknown metrics.
Which is why I originally added this.
So I think the better case to make here is that we already break the rule of using metric family for counters.
I think… if that's already what we do for counters, I think we should do it for all
for info and state set. I don't think we should do it for histograms, obviously, because I would like.
**krajo** 18:12 Yep.
**David Ashpole (dashpole)** 18:13 But… maybe it's okay to be inconsistent, knowing that in future versions of open metrics.
We're almost certainly not going to have this problem anymore, where…
Counters will simply usually have the total suffix.
Yeah, right, and that will be that.
I think the weirder part, so I don't know how…
Closely, people here are following Bartek's new appender interface PR.
but…
The nice thing about that new appender interface is that it's going to directly provide us the metric family name.
But in this funny case, for, that's actually…
maybe we can still have this type of special handling, like, if… If the metric family name
And the sample name?
differ?
then we use the sample name for counter types and for info types. I guess we can still have that.
I don't know if anybody's following.
**krajo** 19:19 I, I, I feel like…
I, like, at least in Mimir, when I look at metadata, I see the total suffix in the metadata for
For counters already. So, there's some magic happening already somewhere. I don't know where.
**David Ashpole (dashpole)** 19:35 Are these open metric metrics, or are these just regular?
**krajo** 19:39 All politics one.
So I don't know where the magic happens. It's a… I think… Yeah, the problem is that
It seems like this evolved… it wasn't really designed, it evolved as people got annoyed with certain things, and then there are some exceptions everywhere.
And I don't know if what I see in Mimir is coming from, like.
Romitus Agent, or Alloy, or what the hell.
So I'm… I'm… I cannot say… Where it's actually coming from.
Anyway, we can, we can take this offline into that, PR.
To decide what we want to do. I just wanted to raise it because I thought it was a non-trivial, interesting question.
**David Ashpole (dashpole)** 20:38 Yeah, it is.
**Arthur Silva Sens** 20:43 Good to me.
Should we go for… Receiver stuff, then?
**David Ashpole (dashpole)** 20:53 Yep.
**Arthur Silva Sens** 21:14 we have two PRs, For the test coverage, this should be done very soon.
I saw that Lauren opened a PR to deprecate this two… configurations?
Here it is.
It is… Literally just adding a deprecated comment.
It's not really doing anything.
How… but, David, you started work, to remove those configurations already?
**David Ashpole (dashpole)** 21:55 So there's already a feature gate that, like, disables the target, or the, start time adjustment?
And we… how long… how many releases ago was that added? I think I changed it to beta, like.
A release or two ago, so it's not been there, like, forever.
**Arthur Silva Sens** 22:15 But we can… we are allowed to change every two releases.
**David Ashpole (dashpole)** 22:21 Every two weeks.
**Arthur Silva Sens** 22:21 So it's… Yeah, if I'm not mistaken.
**David Ashpole (dashpole)** 22:25 And I think we're good to go.
**Arthur Silva Sens** 22:29 I can't go after this info.
**David Ashpole (dashpole)** 22:47 I just have to check. It might have been two releases already.
That would feel so good.
Rip out all of that.
**Arthur Silva Sens** 23:25 It's been a while.
**David Ashpole (dashpole)** 23:28 Yeah.
**Arthur Silva Sens** 23:30 Understood.
Okay, diprecate, report, extra metrics.
Somebody already opened a PR to move this to a feature flag, feature gate?
But then we need to remove… the… Remove the configuration option.
And there is… I have a PR somewhere.
Or is it?
I have a PR in Prometheus.
To stabilize the feature flag.
**David Ashpole (dashpole)** 24:19 Oh, well, then we won't need a feature flag.
**Arthur Silva Sens** 24:21 Yeah, exactly. Like, that's the plan. Like, we shouldn't have feature flags that just stay there forever.
**David Ashpole (dashpole)** 24:27 Okay.
**krajo** 24:28 I think I even re-reviewed that, didn't I?
**Arthur Silva Sens** 24:32 Yeah.
I'm not fighting.
Oh, there we go.
I'm adding this to the config file instead.
But I… I feel like people are not opinionated about this. Like, nobody said yes or no.
So I don't know, should I just go ahead?
**krajo** 25:00 I was a little bit…
Hesitant, because it works differently than the…
than the script native Instagram versus the… Feature flag it has.
Which is that you cannot override.
**David Ashpole (dashpole)** 25:21 one with the other, it's an OR.
**krajo** 25:23 Which is fine, but I think my comment was to make it more clear in the documentation, and then I can approve.
**Arthur Silva Sens** 25:31 Okay, yeah, I saw that, and I agree with you. What I meant by people are not being opinionated.
It's like, people don't care much about this feature, seems like it.
**David Ashpole (dashpole)** 25:47 But anyway, I'll just, yeah, I'll address your comment.
**Arthur Silva Sens** 25:51 And put it back to reveal.
And then, at some point, we can, yeah, stabilize the feature flag.
**David Ashpole (dashpole)** 25:58 Does Prometheus have a notion of feature flags that are enabled by default?
**krajo** 26:03 Nope.
**David Ashpole (dashpole)** 26:04 Okay.
**Arthur Silva Sens** 26:04 drove.
**David Ashpole (dashpole)** 26:05 So it doesn't really… yeah.
**krajo** 26:08 Also, I'm not a general maintainer in Prometus, so I can approve and
Generally, how it works is that if nobody cares for, like, 2 weeks, then we'll just merge it.
But I will not… I will not be able to, like, merge it right away, because I'm…
Only maintainer in native programs.
**David Ashpole (dashpole)** 26:28 Do we have, it might be good to look and see who, like, implemented it initially.
And who reviewed it initially, and like.
See if they've been using it, or have feedback, or… I don't know.
**krajo** 26:43 You can… Arthur, you're on the Prometus team as well, you can ping in the Prometus team.
Slack.
**Arthur Silva Sens** 26:50 If somebody wants to review my PR?
**David Ashpole (dashpole)** 26:55 Or just available.
**Arthur Silva Sens** 26:55 Sorry, I didn't understand… I didn't understand, really.
**David Ashpole (dashpole)** 26:58 Excellent.
The question was more like, does anyone have opinions?
I don't want it to merge just because, like, we don't want to have a feature gate in the collector. Like, that shouldn't be the reason. So…
It's just like, find someone with an opinion who has thought about it, or cares, and then…
If we've gotten any feedback, or, like, just something, yeah.
**krajo** 27:28 Yeah, I think Arthur's reasoning that this has been there for years is good enough, like…
We don't… we don't even need to mention OTA, but of course, that's a trigger for making it happen.
**David Ashpole (dashpole)** 27:39 Like, has anyone used it? I guess is the question.
Cause this is gonna be… A decent chunk of extra stuff stored everywhere for everyone?
**Arthur Silva Sens** 27:51 Yeah, that's why I'm putting false as default.
**David Ashpole (dashpole)** 27:55 Oh, it's… wait, there's a config option now?
**Arthur Silva Sens** 27:57 Yeah, I'm switching from feature flag to configuration option.
**David Ashpole (dashpole)** 28:01 Okay, then that… then that's totally fine. Yeah, yeah. But…
Cool. Sorry, I missed that. I thought we were just turning them on.
**Arthur Silva Sens** 28:11 No, no.
Oh, the last call, we were talking about these two things.
Eliminate time dependency.
I opened a PR with, the idea of using the clock… clock injection.
But, ayubi… mentioned that Prometes is already using SyncTest.
And… it would be… Kind of wasted effort to use both sync tests and clock injection.
But I don't know if we can use sync tasks in OTEL. Do you have any idea, David?
**David Ashpole (dashpole)** 28:54 I… would hope so. So I think…
**Arthur Silva Sens** 28:58 Is Go 126 out yet?
No, it's not until February or March, I think.
**David Ashpole (dashpole)** 29:04 Okay. So, I mean… it's just a test dependency, right? So you just have to, like.
when you open the PR, you'll have to update our…
I guess there's two questions, like, if it… if you run a test that uses sync test, in 1.24.
Does it fail, or does it just pretend the test doesn't exist?
But more likely, we can just update CI and set the environment variable to opt-in.
I would think.
We might run… we might have to… or you can add maybe a skip if the Go version is 124, or, like, a build tag. I don't know, some way…
**Arthur Silva Sens** 29:44 tag, probably.
**David Ashpole (dashpole)** 29:46 It's like, I would hate to not…
Or to, like, implement some poor test, because we don't want to change the CI.
Not an environment variable or something, but… Yeah, I…
I was reading… I read the blog, and I actually think it's a really amazing feature, and wish I had this many, many years ago, because I've written… I've done clock injection, you know, many, many times, and it's always a pain in the butt.
**Arthur Silva Sens** 30:14 Right?
**krajo** 30:17 Yeah, I fully agree that we should be using it. I'm looking forward to using it in Promatus as well.
But the reason why I raised my hand is that I… soon I have to go, so let me just disrupt a little bit and say that on the other issue regarding the…
Separating the service discoveries, I had no time to work on it yet.
I'm gu- like, I'm working on an NHCP migration, and also BartTech is…
Pestering me about, you know, the…
start time and open their V2 and stuff, so I haven't had time to start it.
But I do…
**Arthur Silva Sens** 30:55 What do you…
**krajo** 30:57 Yeah?
**Arthur Silva Sens** 30:58 I was gonna say, what do you think about suggesting that to Laura?
**krajo** 31:02 To what?
**Arthur Silva Sens** 31:04 Laurent?
**krajo** 31:05 Oh yeah, that's why I kind of recruited him and suggested him look… he look at the hotel stabilization work, so I think…
You know, if push comes to shove, we can use it.
So
Especially if I have to, like, do even more stuff related to the data and remote write to Meta and stuff like that.
So I think that's probably a good idea.
**David Ashpole (dashpole)** 31:31 Boop.
**krajo** 31:33 Cool, but I have to go, sorry, and…
No problems. Have a great weekend.
**Arthur Silva Sens** 31:39 Bye-bye.
I'm looking… I look for sync test and collector contrib, and there is one component that is using it already.
And it's also controlling that by, by Builtech.
If GoExperimentSyncTask is set, then it runs, I guess.
**David Ashpole (dashpole)** 32:03 Awesome.
**Arthur Silva Sens** 32:07 Okay, then, I guess I'm gonna close my PR in Prometheus, remove the clock injection.
And start working on sync testing in the collector.
**David Ashpole (dashpole)** 32:22 Nice.
**Arthur Silva Sens** 32:25 Gonna put this as workable.
Anything specific people want to cover today, here?
**David Ashpole (dashpole)** 32:47 Don't think so, I've… I haven't had time yet to go update all the spec-related things.
**Arthur Silva Sens** 32:56 Okay.
There are two things in the discussion needed that I think we already discussed.
the Prometheus config, I think we brought this topic to the…
Collectors seek leads, and they said that it's okay to not test this.
Right? Yep.
I'm gonna close…
**David Ashpole (dashpole)** 33:42 Is that enough to close the issue? Do we need to, like…
**Arthur Silva Sens** 33:46 I was gonna close.
**David Ashpole (dashpole)** 33:49 stabilize Prometheus config, so we're happy with the whole config.
**Arthur Silva Sens** 33:53 I'm… I'm saying just… Just this part of the config.
Like, the config is…
**David Ashpole (dashpole)** 34:01 I see, I see.
**Arthur Silva Sens** 34:02 Good in that, then.
**David Ashpole (dashpole)** 34:03 Okay.
Yep.
**Arthur Silva Sens** 34:28 And about that commit… commit duration? You have any news, David?
**David Ashpole (dashpole)** 34:36 That some college student signed up to work on it.
A little bit nervous.
But, it's… it should be fine. Yeah, if you open the issue.
Someone asked to be assigned. I don't know if we can assign them.
**Arthur Silva Sens** 34:58 I have… I have a hard time assigning
issues to people I never saw before.
They often do that and don't open a PR, and then nobody picks the issue anymore.
**David Ashpole (dashpole)** 35:15 Yep.
**Arthur Silva Sens** 35:26 But, like, is his understanding correct?
**David Ashpole (dashpole)** 35:30 We're just adding…
Prometheus scraped to commit duration seconds. I don't know if you have opinions on the name, but…
I think… I don't know if you have opinions on whether scrape duration seconds should exclude
Append in the future?
But I think we could tackle that separately.
Not obviously important for the stabilization.
**Arthur Silva Sens** 35:56 Like, and this will be one… one metric per target, right? The target will be the… the label. Like, how is that different from the X-ray script metrics, in terms of cardinality?
**David Ashpole (dashpole)** 36:11 It's… I was imagining that this would be potentially part of extra scrape Metrics.
But this would give you the end-to-end.
Scrape to commit duration, and not just the scrape duration.
If that makes sense.
**Arthur Silva Sens** 36:26 Okay, so this is behind the feature flag or config option that we have.
**David Ashpole (dashpole)** 36:33 Right, it… the only weird thing about this is that it's not actually part of the scrape metrics.
**Arthur Silva Sens** 36:39 Yeah.
**David Ashpole (dashpole)** 36:42 Because it can't be, right?
**Arthur Silva Sens** 36:44 Yeah, yeah.
**David Ashpole (dashpole)** 36:45 So maybe that doesn't make sense.
Like, I mean, I'm okay with that. It's… it's more…
Yeah, it's more I'm not sure, like, who…
I feel like there must be other people who would care if we doubled the cardinality of scrape commit.
Duration. Duration.
Maybe it needs to have a feature flag? I don't know. Feels like a feature flag for a single metric.
**Arthur Silva Sens** 37:17 Yeah, sounds a little bit.
banana, sir.
It's gonna sound like I really don't want a sign.
But… but then beyond issues to people all the time.
**David Ashpole (dashpole)** 37:43 I would just assign them, and we… we'll just have to, like…
I think the main… we shouldn't assign unless we actually are certain that this is the right thing to do.
That's my only concern, was like.
**Arthur Silva Sens** 38:05 Okay, let's…
**David Ashpole (dashpole)** 38:08 Yeah.
**Arthur Silva Sens** 38:08 let's wait, like, I'm gonna sign and give him, like, a week or two.
If he doesn't open a PR, I'll just take it, I guess.
**David Ashpole (dashpole)** 38:18 But, like, is it… do you feel like this is fully specified? Like, is it gonna be behind a feature flag? Is it…
Is it on the endpoint? I guess we're okay with that, right?
**Arthur Silva Sens** 38:32 Yeah, my, like, my preference was not… no feature flag.
just… Just implement it.
**David Ashpole (dashpole)** 38:40 Yep, then let's do that, and see if we get any pushback.
That does bring up a good question. Do we have, like, idea of timeline?
For when we expect to be done with everything?
Or, like, when the rest of the collector expects us to be done with everything?
**Arthur Silva Sens** 40:20 Like, if I'm comparing with the other components that need to be stable, we are very far ahead of everybody.
**David Ashpole (dashpole)** 40:28 Okay.
Well, that's… some… Consolation.
**Arthur Silva Sens** 40:37 I… mostly because, like.
Some of those components don't have very active code owners, so maintainers need to go there, understand the code base.
Then start creating issues.
H.
Yay.
Is this good enough for this week? Or should we also cover the others?
**David Ashpole (dashpole)** 42:13 I feel like we have plenty to do.
**Arthur Silva Sens** 42:14 Yeah, yeah.
**David Ashpole (dashpole)** 42:16 I could use some time to get things done.
**Arthur Silva Sens** 42:20 Yeah, sounds good.
**David Ashpole (dashpole)** 42:24 Cool. Alright.
I'll see you guys.
**Arthur Silva Sens** 42:29 Tia. Bye-bye.
**David Ashpole (dashpole)** 42:30 Bye.
