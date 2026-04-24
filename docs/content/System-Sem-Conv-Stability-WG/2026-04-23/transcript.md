SIG: System Sem Conv Stability WG
Date: 2026-04-23
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:26 Hey, Braden, how are you?
**Sailor Moon (ca-wat-brt3)** 02:13 Oops, I was muted.
Tried to tell the bot to fuck off again, it didn't work.
Oh well. Guess that was a one-time thing.
**Donal O'Sullivan** 02:25 I typed stop and nothing happens. I don't know what you're… I think Kristos booted the last time, I'm sure.
Okay.
Are you guys back in the office a lot, or…
**Sailor Moon (ca-wat-brt3)** 02:58 It's… I'm sort of, going in… Twice a week right now?
That's technically how much I'm supposed to be coming in, that's, like, the mandate.
**Donal O'Sullivan** 03:13 Yeah.
**Sailor Moon (ca-wat-brt3)** 03:13 I… I just kind of come in more often, because I don't live far, and so if it's not, like, snowing, I'm fine to go out, or if it's not raining, because I do have to park, like, a 10-minute walk from the office and walk over, so if it's raining, I'm like, I'm staying home.
**Donal O'Sullivan** 03:31 Yeah, yeah, yeah.
Where, where are you based? Are you Canada, you are?
**Sailor Moon (ca-wat-brt3)** 03:38 Yeah. Okay. Yeah, about an hour out from Toronto.
**Donal O'Sullivan** 03:41 Okay, cool.
Oh yeah, so you probably get crazy winters.
**Sailor Moon (ca-wat-brt3)** 03:46 Yeah, they can get pretty bad. Not as bad as… the northern parts, it's more in line with… the type of winter you see in, like, northern U.S, like New York or Ohio, or that sort of thing, but…
**Donal O'Sullivan** 04:01 Yeah.
**Sailor Moon (ca-wat-brt3)** 04:01 it's still… it still gets pretty bad. It was… it was really cold this year.
**Christos Markou** 04:27 Okay, the boat is shout, no.
**Sailor Moon (ca-wat-brt3)** 04:37 Goodbye, note-taker.
Not sure if we are waiting on Pablo today, I assume still no Roger.
**Donal O'Sullivan** 05:20 Oh, Roger's down under still, so…
**Sailor Moon (ca-wat-brt3)** 05:23 Yup.
**Donal O'Sullivan** 05:23 Yep.
**Sailor Moon (ca-wat-brt3)** 05:49 We can probably get started for now, then. We'll see if Pablo ends up joining.
**Donal O'Sullivan** 05:58 Cool.
Do you want to talk about, my thing first, or yours? I don't know mine.
**Sailor Moon (ca-wat-brt3)** 06:05 Yeah, you can get… you can start with yours.
**Donal O'Sullivan** 06:08 So, yeah, so I, I, replied to the, to the issue for multiple… Metadata, metadata schema configs, I know Roger's taken the multiple schema approach.
I, I took the, diversion metric approach, and… From what I can see, it seems to work pretty good. I can share my screen if you guys want, but basically… There's, let's see, where's my share button?
kind of… Minimal code changes required, if we can share the race.
Yeah, so… So I did a little write-up of it here, we can see in… just running… Running Grafana locally, actually.
we look at metrics here, so we can… so basically, I, just to start, I suppose, I have, Am I in the right place here.
Maybe it's better if I show it this way.
So basically, the configuration, so for CPU scraper, there's just two metrics here.
So this is the schema in Host Metrics Receiver. We have this metric, the existing one, the legacy one, I just changed some description just to have legacy. We have our new versions metric, which is just the same metric.
We have V1, we have this name override field, Which we're using To actually keep the metric name, and then we've changed the unit from seconds to milliseconds.
And essentially… there's a small update to mdataGen and Collector Core to just support this name… this kind of name overwrite field, and what that allows us to do is it just allows us to generate, the code using… using this name, so the new generated code for this… for this versioned metric will have V1 in it, but it allows us to keep the same name, if that makes sense.
Yeah.
And then the user configuration just stays the same, so, like, they have their CPU scraper enabled, and there… I have a feature gate. We can use two feature gates, I just have one for the new metric, but you could just create another one for the legacy as well, just to make it easy to turn stuff off and on.
Then, in terms of the host metrics… the host metric receiver code.
it… the big code change is just the generator code, but the actual custom logic required outside the generator code is quite small, so there's just one to, like, handle the feature gate, so just checking, is it enabled? If it is enabled, then emit the new, the new metric information, and then just, like, in this example, I just added a, function for CPU… in CPU Scraper Linux, which was recording the new… the new, Metric, which is in milliseconds instead of seconds.
And that's it. And then, that metric just gets emitted, just with the new… unit, and you can emit both at the same time. There's… there's no issue there, as I showed in… Grafana, it works fine, we can look at the metric here, it's been omitted.
That's… this is… everything so far, and then mdatogen, there's just a… so, basically, there's a small update. I don't know what's going on there. Can you still see my screen? My screen, yeah.
**Sailor Moon (ca-wat-brt3)** 09:46 Yep.
**Donal O'Sullivan** 09:47 Cool. So just the name that agenda was just a small update to the metadata schema, just adding this name field, and then in the template, we just check, is that populated? If it is.
We use that name instead of the actual metric name, and you can end up with, like, your generator code then in your… wherever you're generating it, you can have your metrics info.
So you'll have, like, two fields, System CPU time and system CPU time. This one just… I think I just had V2 in the example, but, you have the same name, if that makes sense.
It's… quite a small code change in mDataGen, it's just basically… the schema, and then there's some, like, templating updates, and I think a small update in the loader.
And then, yeah, that's it. Do you guys want to see more? Do you have questions, or…
**Dmitrii Anoshin** 10:36 It sounds pretty good to me. I think, Yeah, we discussed this approach, and approach-wise, it looks… it looks good, I agree with this. The one thing I'm concerned about is that, is it really we switched to milliseconds? I completely missed that change.
**Donal O'Sullivan** 10:57 Maybe, I think so, so I'm just, I'm just doing it manually, so I'm multiplying the time by a thousand.
**Dmitrii Anoshin** 11:04 No, no, no, I'm saying, like, did we change semantic conventions for.
**Donal O'Sullivan** 11:09 Oh, yeah, yeah, no, no, no, no, no, no, this is just, like, a very crude example.
**Dmitrii Anoshin** 11:13 Oh, I was scared.
**Sailor Moon (ca-wat-brt3)** 11:14 I was just for a demo.
**Donal O'Sullivan** 11:15 Yeah, yeah, no, no, don't worry, it's… it's just a very…
**Dmitrii Anoshin** 11:20 Let's not change that to milliseconds, I was like… I was pretty scared about it.
**Sailor Moon (ca-wat-brt3)** 11:24 Yeah, I don't think that would have been a good idea.
**Dmitrii Anoshin** 11:27 Okay, okay, cool. Yeah, and I'm relieved now. I was like… I was concerned during the whole presentation.
**Donal O'Sullivan** 11:35 Yeah, that's actually in production, Dimitri. Yeah, it's just a crude example.
**Dmitrii Anoshin** 11:44 Okay, okay, makes sense. Yeah, otherwise this looks pretty good. Thank you. I think we…
**Sailor Moon (ca-wat-brt3)** 11:48 I like it. The only thing I wonder is… so I guess slash is technically an allowed character in a metric name?
But part of me wonders if we should just, like, instead of forcing… the user to remember to put the name field, like, we just discard everything after the slash, but I think slash is an allowed character, so maybe we can't do that.
**Dmitrii Anoshin** 12:11 It's a loud character, but I don't believe it's used everywhere, and there is no semantic conventions that ever mentions this slash, so maybe we just don't allow it for now in the gen. At least there is a, like, specific use case. But by not allowing, I mean that if we see a slash in the metric name in the validation, we just, Mmm… Break it and say, hey, put a name instead.
Put name field, you forgot the name field, something like that.
**Sailor Moon (ca-wat-brt3)** 12:44 Yeah, I guess we could just validate that they have to set the name field if they say Gosh, yeah, that's probably fine.
**Donal O'Sullivan** 12:51 This is a good point, so I actually think I had to update mdataGen slightly around the slash. I think I have to add it to linting, if I remember correctly.
Just to handle it, because… so what I do in mdataGen is I strip everything off after the slash to just use that as well, so… but maybe that's slightly different, but I… I would agree with what you guys were saying. If there is a slash set, just use the name overwrite.
**Dmitrii Anoshin** 13:15 Yeah, and… Probably… we can technically… Use simplified approach and do not have name field at all, just strip and slash, and I think that's also fine. From my perspective, I just would like to either set, like, strict validation, for example, slash, if slash is there, we require a name, and Potentially, we require name to be the same as first part of the metric name before the slash.
Or we just don't introduce name and say whatever.
Before the slash is the metric name.
**Sailor Moon (ca-wat-brt3)** 14:01 Yeah, I think… thinking about it more, I'm actually more on the side of validation anyway. For mDataGen specifically, I'm not too concerned about, like, a convenient config experience, because it's for selector developers, not for, like, general users. So, like.
like, forcing the name field and having the strict validation seems fine to me. Like, if it was a user-facing config, I might say we should come up with something more convenient, but it's for developers. Like, I think it's fine for us to… to do it like that. The only other question I have is, we had talked about, in other contexts, like, versioning component configs and stuff like that, and using an at symbol was one of the things tossed around.
Should we consider Making the at symbol a standard, and following along with that, and using that as the versioning instead of the slash.
**Dmitrii Anoshin** 14:57 That's a good point.
If we say that we're only using that suffix for… versioning only, I think it makes sense.
Otherwise, if we use it, like, let's say, for adding some aliases, For any other use cases.
**Sailor Moon (ca-wat-brt3)** 15:17 Yep.
**Dmitrii Anoshin** 15:17 In that case, slash works better because it's kind of similar to the configuration when you specify the components, right? You can make components different.
But, yeah, if we… if we're only thinking that it's gonna be a useful version, I think ad symbol is… should be good. And add symbol is not supported anywhere in the… In the metric name, right?
**Sailor Moon (ca-wat-brt3)** 15:41 I… don't remember what the restriction on the metric name is, because, like, thinking back, my initial thought of, like, was slash character supported? I should have remembered that obviously it is, because, like, we rename our Google Cloud metrics to do that, like, within the pipeline for a lot of our stuff. So, like, obviously that is supported. I don't know about, like.
arbitrary Unicode characters like that? I don't know if it's specified anywhere what the protocol allows.
**Dmitrii Anoshin** 16:09 It should be something in the spec. Protocol doesn't care, but in the spec, it should be naming convention, guidelines, something like that. And if it's not allowed, I think it would be good to use add character. In that case, we don't even need name field anymore.
**Donal O'Sullivan** 16:27 Okay.
Yeah, that makes sense. So you guys are saying, don't use slash, use at, and then no name field, and we can… we can just get the metric name from anything after the at, I guess. Is that the…
**Sailor Moon (ca-wat-brt3)** 16:39 Everything before the at, yeah. Like, discard everything after the at, and just take the metric name there.
**Donal O'Sullivan** 16:46 Yep.
**Sailor Moon (ca-wat-brt3)** 16:47 Especially because the only time that we're… that we'd need to apply that version Might… would probably be if there's a name Clash?
**Donal O'Sullivan** 16:57 Yep.
**Sailor Moon (ca-wat-brt3)** 16:58 I guess that is kind of a question, like, that is kind of the only time we need to apply that version, right? We're not gonna, like, apply versions to names that have changed… metric names that have changed.
**Dmitrii Anoshin** 17:09 Right.
**Sailor Moon (ca-wat-brt3)** 17:11 So, so I think discarding everything after the at.
It's also fine.
If we do… if we do the at. I wonder if it's worth maybe… Because the talks about versioning configs and stuff is still… kind of nascent, like it's… we've talked about using an at symbol before and thrown that around, but we haven't made an official decision.
I wonder if it's worth an RFC to, like.
support that in ConfMap, and then mdataGen just kind of follows along.
**Donal O'Sullivan** 17:49 Yeah.
**Dmitrii Anoshin** 17:51 Yeah, maybe we're… Expanding the scope.
Too much. In that case, it might block us.
That's the only concern at all.
**Sailor Moon (ca-wat-brt3)** 18:01 Yeah, it would… it would be.
We could also just say that, like, whatever… whatever the collector decides to do, we like the at symbol, so we'll take the at symbol.
**Dmitrii Anoshin** 18:10 Yeah, makes sense. We can do that.
**Sailor Moon (ca-wat-brt3)** 18:12 Yeah.
**Dmitrii Anoshin** 18:12 And it's also not, like, really user configuration interface, it's just confab, and I'm not sure that it… that support of version will be implemented at the confab level. It might be implemented somewhere a higher level. So, in that case, there is no, like.
There is no reuse of the logic in the… if we…
**Sailor Moon (ca-wat-brt3)** 18:33 Right.
Makes sense.
**Donal O'Sullivan** 18:36 Hmm.
**Sailor Moon (ca-wat-brt3)** 18:37 Okay.
I like the at symbol, then. Everything else about the proof of concept seems pretty good to me.
I'd still want to give Roger the chance to… Yeah. …to give his side, too.
**Donal O'Sullivan** 18:51 True.
**Sailor Moon (ca-wat-brt3)** 18:51 So we should check where he's at with it, or if maybe he just likes to… the alternative that you've proposed? I'm not sure.
**Donal O'Sullivan** 19:01 Yeah, no, good question. I was just… I was going to mention it there, so I was talking to him earlier today, and, he was saying his POC that he's shown previously in the issue thread.
Is where he's at, and… like, he likes that approach, I guess. I don't know, do you… with the interest of time, do we have time to talk about that now, or I know you've got our topics, Brayden, so…
**Sailor Moon (ca-wat-brt3)** 19:23 Yeah, good.
I don't… I don't remember what that one looked like, so… I think maybe I will…
**Donal O'Sullivan** 19:35 I can…
**Sailor Moon (ca-wat-brt3)** 19:36 open.
**Donal O'Sullivan** 19:36 a Slack message in the CNCF channel, and maybe we can… Async, we can both… we can all kind of look at it, maybe, if that works, or…
**Sailor Moon (ca-wat-brt3)** 19:44 Sure.
**Donal O'Sullivan** 19:56 But his approach was the two different schemas, and you end up… At kind of a similar place, but there's just more custom code required within the receiver, and you end up with more generated… you've, like, you've generated code for your legacy schema, and then generated code for your… Semantic conversion schema, so… It works fine, it's just that I suppose you end up with more code overall.
But, yeah.
**Sailor Moon (ca-wat-brt3)** 20:26 Yeah, his… his proof of concept is… The summary is very similar to, like, the initial the initial idea I had come up with way back when.
And I think the… the… the concern was mainly that there was just… there was a lot of generated code. Like, all of the mdata gen stuff is generated essentially twice, with differences, but essentially… there's two M-data Gen packages, and that's quite cumbersome.
**Dmitrii Anoshin** 21:00 Yeah, it's harder for users to follow when we have, like, this separation.
**Donal O'Sullivan** 21:09 I think as well, with all the custom unmartial logic.
You can… you can end up with bugs there, just quirks, because there's a lot of different… It's not as straightforward as just having, like, you know, on this feature get you this, like, there's a…
**Sailor Moon (ca-wat-brt3)** 21:24 Yeah, yeah.
Yeah, like, you could configure something, and then a feature gate could cause a config load breakage, which is a bit odd.
**Donal O'Sullivan** 21:33 I mean, hmm.
Yeah.
**Sailor Moon (ca-wat-brt3)** 21:39 with, with the, with the, the versioned config version, I, I suppose, if you, if you… configured a V1 metric, and then… it… If you configured a V1 metric, and then the thing to emit V1 That feature gate was turned off.
**Donal O'Sullivan** 22:00 Not.
**Sailor Moon (ca-wat-brt3)** 22:00 probably would, like, fail to load the config, or they just wouldn't get emitted at all.
**Donal O'Sullivan** 22:05 It just doesn't get emitted. The way it's currently done, it's just like a simple if statement, if it's not… If it's not… if the feature gate's not enabled, you'll just get… It just won't be emitted, like, yeah.
**Dmitrii Anoshin** 22:17 Don't we want to support, like, some more granular… like, configuration capabilities here. So, for example, I want, I want the V1 metrics and disable V0, but I want just one metric from V0. In that case.
I would potentially… turn on the next feature gate, and disable the previous feature gate, and just enable one metric from the old one in config, if that makes sense.
That's…
**Sailor Moon (ca-wat-brt3)** 22:51 Dude.
**Dmitrii Anoshin** 22:52 still not gonna be possible, right? If we have metric conflicts, like, same metric name by different… behavior.
**Christos Markou** 23:03 But the old metric, has a new equivalent, or no, it just remains there, or it's just deprecated?
**Dmitrii Anoshin** 23:14 The new method has new equivalent.
What do they mean?
**Christos Markou** 23:17 the metric from V1 that I still want to enable, does it… will this… does it… does it have an equivalent metric in V1?
**Dmitrii Anoshin** 23:29 Yeah, I guess, for example, it's easier for metrics that don't collide, but for metrics that do collide.
Like… Even… for example, even if I want to enable… so, let's put it this way. If I enable both feature gates.
give me… all metrics, from V0 and V1.
**Donal O'Sullivan** 23:59 Hmm.
**Dmitrii Anoshin** 24:00 If I… if metric name collides.
And if I disable that metric in my config, in user config, what happens in that case? Which one is getting disabled?
**Donal O'Sullivan** 24:13 Oh, yeah, yeah. So, the way I have it currently done is you don't have to touch the user config, it's just controlled at feature gates when you run the collector. So, like.
Yeah, you can't… you could disable… the metric, but I guess you'd be… you'd be disabling the entire metric, you know.
**Dmitrii Anoshin** 24:33 Both of them.
**Donal O'Sullivan** 24:34 Yeah, yeah, so you'd have to use… you'd have to do that through feature gates, the way it's done currently. So, like, the way I have it done, you don't have to specify the new version metrics in the user config, it's just you put in whatever the… whatever they… they had current, like… Currently in their config, and you just enable the new one through a feature gate.
If that makes sense.
**Sailor Moon (ca-wat-brt3)** 24:55 So, if both feature gates were on and they wanted to double right.
Just enable… just having the systemcpu.time entry and the user config would write both.
**Donal O'Sullivan** 25:04 Yeah, yeah, that's what I showed you there in the Grafana dashboard, that's writing both at the same time.
**Sailor Moon (ca-wat-brt3)** 25:09 Okay, and it's just configured once in the user config, and that may have already been pasted there, and I just missed that part.
**Donal O'Sullivan** 25:16 Yeah, yeah.
**Dmitrii Anoshin** 25:17 In Grafana, you have this translation when you put units in the metric name and everything. How is that done? Is it part of a transform processor or Grafana?
**Donal O'Sullivan** 25:29 Good question. I didn't do anything, Dimitri, so I just… I'm just emitting the metric, and Grafana's just picking it up.
**Dmitrii Anoshin** 25:36 Yeah, I think it's…
**Sailor Moon (ca-wat-brt3)** 25:37 Yeah, I think it's a… that's part of the OTLP to Prometheus, like, where it… It takes the unit, and then adds underscore total, because it's a counter.
**Dmitrii Anoshin** 25:47 Right, right. So it's probably ingest of Grafana in that case.
Okay, so for Grafana, for example, it works pretty well, but for other backends, so for example, for Splunk observability, that's not gonna work. We don't do any special treatment between different names. So if user enables both feature gates, it'll be… It'll be re-aggregated, essentially.
So, in your, like, example with milliseconds, we would add milliseconds. We would sum them up with the seconds. Not ideal, but…
**Donal O'Sullivan** 26:17 Man, this is hot.
**Dmitrii Anoshin** 26:18 was it gonna work. So, we need something.
Yeah. To be able to have that control as well.
So, like, enable… enabling those feature gates, and potentially, somehow, say that.
Only the last one, like, if metrics collide, we only need one of them to be… Potentially, this can be done in the transform processor somewhere, I guess.
**Christos Markou** 26:47 We added diacems for this, no?
Sorry, what? I think you added the guidance, you updated the RFC.
for this, use case, I… or it was something else.
**Dmitrii Anoshin** 26:59 Oh, I think in RFC we said that only one of them will be enabled.
**Christos Markou** 27:03 Yeah, you amended the RFC to include something like this, but I don't remember.
**Dmitrii Anoshin** 27:08 Oh, right, I forgot about it. Oh, okay, in that case, we shouldn't emit both, essentially.
**Donal O'Sullivan** 27:14 Okay.
**Christos Markou** 27:14 Yeah, I can find it and send it to you.
**Donal O'Sullivan** 27:19 So I think we'd have a similar problem in Elasticsearch, well, in Cabana, but we can have, like, versions.
Dashboards, but yeah.
I just went with the, Prometheus Grafana approach to keep it, you know, open source, well, yeah, if that makes sense, just… Yeah, that makes sense.
**Dmitrii Anoshin** 27:40 Yes.
**Donal O'Sullivan** 27:40 Something we can automatically.
**Dmitrii Anoshin** 27:42 We can potentially support both… both use cases, just somehow need to figure it out, figure this out, how to do it. The problematic part is with enabling both and providing granular… granular configuration interface for the users, I think we… if we… if we… Imagine both, we need to provide users a way to disable old one and renew one. And that one, that's where it becomes complicated, because we are attaching user configuration interface now.
And we are introducing new options for the user interface that are… will be short-lived, like, for the transition period only. So… If we want to do that, it's fine, we just need to, like, properly design it.
Or we don't… we just don't emit it, and in that case, it will not work as… as clean, as smoothly for a Grafana use case.
Yeah.
**Sailor Moon (ca-wat-brt3)** 28:52 Yeah, I'm not sure. I'm kind of of two minds about it, where I want to be able to support people double writing, but when the name doesn't change across schemas, most backends will… will screw it up. I'm pretty sure… I'm pretty sure GCP will screw it up.
Huh.
Good question.
**Donal O'Sullivan** 29:20 I could take it as a… It was an action item to investigate that a bit more on the versioned approach.
Maybe you're…
**Dmitrii Anoshin** 29:30 The general version approach seems pretty good, and, like.
pretty easy to understand for the end users and developers. So I would like to stick with that one, but we need to figure out that edge case.
**Sailor Moon (ca-wat-brt3)** 29:49 I can write, a summary comment on the issue.
With the feedback.
That we talked about here.
**Dmitrii Anoshin** 29:57 Cool, thank you.
**Donal O'Sullivan** 29:58 Thanks, Braden.
**Sailor Moon (ca-wat-brt3)** 30:01 We're… we're over time, but the only thing I was… that I should mention is the, the hotel arrow issue I posted. They're currently, like, designing a host metrics receiver for their Rust.
Version of the collector.
And… a lot of their design approach is pretty nice and stuff. I would have… I would… we probably… like, if we were making the host metrics over again today from first principles, we probably would come to a lot of the same conclusions they did. And they're going to be supporting our conventions from, like, from the get-go, which is… Exciting, but also means that we'll need to, you know, help them Help them out a little bit.
Take a look at the issue and provide comments if you have time.
**Dmitrii Anoshin** 30:49 I'll be leaving some feedback, too.
**Sailor Moon (ca-wat-brt3)** 30:53 Alright, thanks everyone.
**Dmitrii Anoshin** 30:55 Thanks, folks.
**Donal O'Sullivan** 30:57 Thanks, guys. Bye.
