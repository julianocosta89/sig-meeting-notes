SIG: Prometheus WG
Date: 2025-11-05
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Arthur Silva Sens** 00:18 Hello!
**Arve Knudsen** 00:19 Hello, Arthur, how are you doing?
**Arthur Silva Sens** 00:22 Pretty good.
How are you?
**Arve Knudsen** 00:25 Goods.
Spacey?
**Arthur Silva Sens** 00:31 I'm not sure if anybody's gonna join today, because there was some confusion… oh, cryo's here. Some confusion about changing the times.
**Arve Knudsen** 00:40 Hello, crime.
**krajo Krajcsovits** 00:41 Hey, hay.
**Arthur Silva Sens** 00:44 No.
**krajo Krajcsovits** 00:52 My calendar isn't that crowded, so I didn't really look at that discussion. I'll just adopt whatever.
**Arthur Silva Sens** 01:02 I have a feeling… That people are slowly…
putting me in a manager position, because, like, I'm in so many meetings, I have almost no time to do any coding.
**krajo Krajcsovits** 01:21 I mean, as long as you enjoy it.
**Arthur Silva Sens** 01:24 Yeah, true.
I'm still deciding, I guess.
I… a magic advice.
What's it again?
One second, guys.
**krajo Krajcsovits** 01:49 I did look at the open telemetry.
calendar, the public calendar, and it's full of meetings all week, so if you want to go to meetings, then
Open Tarot is a great place.
**Arthur Silva Sens** 02:02 Yes.
That's where you, like, I don't know, 2 more minutes. If nobody shows up, we just start.
**krajo Krajcsovits** 02:11 Yep.
Did you guys see the V-Log from Raj?
**Arthur Silva Sens** 02:28 Yes, I did.
That is awesome.
**krajo Krajcsovits** 02:32 Yeah.
**Arve Knudsen** 02:34 I don't think I'm aware of this.
**krajo Krajcsovits** 02:37 Just going to general.
**Arve Knudsen** 02:39 Okay. I'm never there. That's why I don't mind.
**krajo Krajcsovits** 02:42 You should be here this time.
**Arve Knudsen** 02:46 Just find it.
**Arthur Silva Sens** 02:48 Just remember, we are being recorded.
**krajo Krajcsovits** 02:50 Yeah, yeah, I think, yeah.
Don't say anything.
It's just a suggestion.
**Arve Knudsen** 02:57 Alright, thanks for making me aware.
**krajo Krajcsovits** 03:00 Yep.
So, yeah, I, I started…
This is not about Prometus, but I did start to look at the… Oh, somebody joined, okay.
**Arthur Silva Sens** 03:21 Hello, Adam.
**Adam Bernot** 03:25 Lou?
**Arthur Silva Sens** 03:29 Adam, do you know if David is joining? Probably not, right?
**Adam Bernot** 03:35 I'm not sure.
**Arthur Silva Sens** 03:48 Okay, I guess we… Looks like he has…
**Adam Bernot** 03:51 Looks like David has 4 meetings on his calendar for this time slot, so I'm not sure which one he's going to.
**Arthur Silva Sens** 03:58 How many? Four?
**Adam Bernot** 03:59 Yeah.
**Arthur Silva Sens** 04:01 Oh, damn.
**krajo Krajcsovits** 04:05 Obviously, this is the most important, I don't get it.
**Arthur Silva Sens** 04:09 Like, he… he recently joined the hotel technical committee.
**krajo Krajcsovits** 04:14 Oh, yeah, that's the same time.
**Arthur Silva Sens** 04:16 Yeah. Oh, he's a big guy now.
Okay, I guess we can start with… with us. Let me write this down. RF… Bye.
Okay, first topic is something that I've been…
sharing with Cryo already for a few… few weeks.
OpenTelemetry tried… to apply to graduation status in CNCF.
They failed, there's a lot of feedback. One of the feedbacks is that OpenTelemeter contrib is a mess.
Too many components, too many unmaintained components, upgrading versions.
Most often break some random thing.
And, the collector SIG needs to…
To come up with a better strategy.
Something… some stuff that we… some ideas that we discussed is we will select the most important components in collector contrib, and move it to CollectorCore.
And stop advertising Contrip at all. Just tell people to use Core and not use Contrip.
And the Collector SIG, we… we collected information from several vendors about the components that those vendors' customers most use.
And the Prometheus receiver is by far the most used.
By, like, everybody. Everybody's using Prometus Receiver.
So that makes Prometus Receiver the most important component in the collector, and we need to work on stabilizing.
I honestly… it's too much work. It's too much work for a very small group.
I don't know exactly how we'll do it.
I think a first good step is…
Coming up with some kind of epic, or…
A big issue describing step-by-step what needs to be done.
And we advertise it, we call for help.
And we guide people to implement what we need to implement.
But first step would be, yeah, creating this epic… But…
Yeah, let me stop there. Any comments on this so far?
**krajo Krajcsovits** 06:48 Or can I raise my hand? Wait.
Yes.
**Arthur Silva Sens** 06:51 There you go.
**krajo Krajcsovits** 06:52 So, you said there's a lot of things to do. Is that… are you referring to there's a lot of issues, or you know something you don't?
**Arthur Silva Sens** 07:01 There is, let me see if I can share my screen.
Oh my god.
There is a document.
Describing what needs to be done for… Declare something stable.
And it's over here.
We need to go over this document, and review if we meet all those requirements.
It's a very big list.
I haven't gone through it, so I don't know how much work. It's, like, a good feeling. It's a good feeling that it's gonna be a lot of work.
Let me…
I can do this work.
what I… yeah, like I said at the beginning.
I have a feeling that I'm switching to a manager.
And I don't have time to code.
Maybe… maybe we can discuss more after we have this epic? Like, we have this list of things that needs to be done?
**krajo Krajcsovits** 08:59 Yeah, for sure, I'm more, you know, prepared to… Discuss concrete things.
But also, Yeah, we need to go back to our managers and see how much time we get.
**Arthur Silva Sens** 09:15 Like, imagine a word… like, we are the co-owners, Cryo. You, myself, and David.
Imagine we are in a world where none of us have the time. So we… we became… we become blockers.
What is our plan?
If… if that's the… the reality.
Do we just let the collector maintainers do whatever they want?
**krajo Krajcsovits** 09:56 You mean the people that are maintaining the OpenTromatic collector that is going to copy the stuff?
**Arthur Silva Sens** 10:03 Yeah.
**krajo Krajcsovits** 10:03 Cool.
**Arthur Silva Sens** 10:04 I, the… Open Telemetry Collector has maintainers, approvers, and code owners.
**krajo Krajcsovits** 10:10 Yeah. And regular contributors. We are code owners. We're very low…
**Arthur Silva Sens** 10:15 in hierarchy, like, very low, but we are lower than maintainers and approvers. If they want to.
they can just open PRs and merge as they like, because they… they are…
That are the people that are actually on the code and have push access.
They are gonna… if we, we, if we block, if we don't review this stuff, they will do it.
But do we want to put up a fight and tell them, hey, Don't do this.
without our consent, or we just let them. Like, what I can imagine is, like.
You, myself, and David, we are the Code Islanders because we have Prometra's expertise.
They… they do not.
they are focused on OpenTelemetry, so they definitely understand less than we do when it comes to Prometheus.
**krajo Krajcsovits** 11:06 But if we don't reveal their stuff.
**Arthur Silva Sens** 11:09 Like, they will just do it, whatever.
**krajo Krajcsovits** 11:12 Yeah, yeah, I mean, sure. I don't see what the problem is there. I mean, they will… either it will work, or people… since you said that it's being used a lot, people will slap them in the face if it's too bad. Like, I… Yeah, I mean…
For me.
again, the… my time is kind of restricted to triaging and looking at PRs at this moment.
Like, I did a bunch of small PRs recently, and then I'm reviewing something regarding the…
Created time?
theories… And… Yeah, it's just something I need to… discussed with Maya?
miniature.
**Arthur Silva Sens** 12:06 Alright.
The next meeting is in 2 weeks.
Do you think you… we can discuss this?
Batter, I guess, in 2 weeks?
**krajo Krajcsovits** 12:17 Yeah, yeah, yeah.
Also, in the meantime, if you have the… if you create the list and, you know, I can look at small items, I mean, that's… that's fine, but, like, if there's a major thing that's a project.
Then that's, you know, tricky.
Because I'm also a Prometus maintainer, which is another 100% time, sometimes.
**Arthur Silva Sens** 12:41 Alright, sounds good.
S…
Okay, next topic is, yeah, kind of similar to the… Contributes a mess.
A lot of receivers are drive-by contributions.
to something that already exists, but it's in a Prometus exporter format.
like… the… There is an issue open. Let me see… let me see if I can find…
Okay, this is not well formatted, but, like, We are rethinking.
our strategy for accepting new components. One of the ideas is rejecting everything.
Shifting towards building Outside of the… collector, Before donating?
And the other… It's not really… I… I… Requiring more code owners.
They're like… Three of, the three…
Strategies are about making this more strict.
Oh, drive-by contributions are probably… Disappearing, or… At least… decreasing?
And I see, like, we talked about this during PromCon, Cryo and I. We see this as an opportunity to promote the Prometus Exporters more, and Prometus Exporters have been around for years. They are mostly stable.
and we could help the collector's sick by giving them an escape. Like, somebody wants to contribute,
A receiver for a random infrastructure, tool.
the…
CollectorSig has a strategy, like, hey, there is a previous exporter for that already, why don't you just build your own collector with this exporter instead?
I did a… I did some… POCs?
Thank God.
I was able to implement the receiver interfaces in Exporter Toolkit, and Experter Toolkit is like a… an adapter.
That receives,
Receives, like, it's a… it's kind of a scrape loop.
Let me see if I can find a config.
It has a scrape interval, it mimics the Prometus behavior. Let's say every 30 seconds we scrape
client calling registry.
And with transform, we have an adapter that converts this registry to OpenTelemetry.
I do just… just gauseous for now.
But I was able to…
to add… I created a PR node exporter that implements the exporter toolkit interface that I created, and I was able to build a collector
with the node exporter.
and I run this collector, node exporter was running inside the collector, this adapter was switching the registry to Pmetrics.
And then it's just the regular collector pipeline, whatever comes after.
It just works.
So we… this is something doable, and it honestly doesn't look too hard.
**krajo Krajcsovits** 17:22 Oh.
**Arthur Silva Sens** 17:24 we could… Yeah, go ahead.
**krajo Krajcsovits** 17:27 Oh, sorry, finish.
**Arthur Silva Sens** 17:29 I was just saying, like, if we implement this in Exposure Toolkit.
every Go exporter could also implement this interface.
It will be automatically embeddable in the collector.
We could even have, like, a Prometheus collector distribution.
With all the exporters, and… Whatever we want.
Do we want to do this?
**krajo Krajcsovits** 18:01 Hmm.
I think this sounds very tempting for… for a first MVP.
the… I think the… Question is, you know, this doesn't give you OpenTeametry semantic conventions, right?
Yes, exactly. Yeah, that's the… that's the main issue.
So… And to give you those 70 conventions.
You would need to do something else in the…
In the exporter itself, or have a mapping?
**Arthur Silva Sens** 18:51 Yeah.
I wouldn't require the exporters to follow the semantic con… the telsemantic conventions.
I could see a slow transition towards it, if desired by the maintainer, but I wouldn't see that as a requirement.
**krajo Krajcsovits** 19:12 So, potentially, we could add the mapping in this… thing that…
That would just do the mapping, right?
**Arthur Silva Sens** 19:22 But then this thing would need to know the mapping for all conventions?
**krajo Krajcsovits** 19:28 No, the exporter would need an extra file or something that… that would be loaded, or something like that. I mean, you would define the mapping
I don't know if it makes sense, but I would define it per exporter.
So people working on the core exporter don't have to worry about it, but… someone could… Add the mapping.
Yeah, I don't know, I…
This is the first time I see this, but this sounds pretty cool, for sure.
**Arthur Silva Sens** 20:00 There is a… a component in the collector contrib called schemaProcessor.
That do the translations of schemas.
So if… Data comes in this format.
The schema processor will transform the metrics to the following.
schemas. It's kinda… one step in between that do the translations. We could… Make the exporters.
Use schemas.
Just declare the schemas that they want, but, like, we don't do any transformation to the metrics in that site.
And we have something that, like, translates their schema to the semantic convention schemas.
**krajo Krajcsovits** 20:50 Yeah, yeah, yeah, I guess I shouldn't have talked about implementation, just… Just on high level.
you know, You wouldn't want to alienate people working on exporters.
And keep them efficient.
It would make sense to do the mapping outside, yeah, I agree.
**Arthur Silva Sens** 21:14 I think it's fine to discuss implementation. Like, we have time, we don't have any other topics in the agenda.
**krajo Krajcsovits** 21:20 Yeah, that's true.
So… Yeah, I… Yeah, sorry.
**Arthur Silva Sens** 21:27 I was gonna say that…
To commit to something like this, we also need to wait until next week, because you don't know what you're gonna work on.
**krajo Krajcsovits** 21:37 Yeah, that's true.
**Arthur Silva Sens** 21:39 Cool.
**krajo Krajcsovits** 21:41 I mean, I know what I'm going to work on in the next quarter, and
This is not on that list at the moment, but next… next week I can maybe… have…
A better idea.
Cool. If I can change that.
**Arthur Silva Sens** 21:55 Well, is that…
So, you know what you're gonna work on next quarter. Is there anything that this group could help?
Like, what are you working on that is related to Attal and Prometheus?
**krajo Krajcsovits** 22:08 The Open Matrix tool.
is my second priority. First priority is native historical custom buckets migration.
But that's… you cannot happen that. And I'm pushing OpenMetrics.
2?
Yeah, we'll… we'll see.
it might be that the NHCB migration is more an advisor role, which I'm trying to do.
So then… then I will… will have time. But I… again, I… I can't commit, because I…
Like, I need to… speak to somebody next week. But this is interesting, for sure.
So, how it would look like from an end-user perspective?
I don't imagine… The exporters, even though they are, like, some of them are super stable.
I don't imagine they would get into OpenTeametry Collector, right? The core.
**Arthur Silva Sens** 23:06 we… with… I haven't discussed.
I expect not.
But we never know.
I… but I… I can definitely see… Up.
I can definitely see a distribution.
Made by Prometheus.
Where we declare… declare…
what we want. Like, for example, I'm adding my node exporter receiver, I'm adding a Prometus remote write exporter, and Prometus has its own distribution.
This can, like, this is easily…
To be very easy to convince people.
But… Yeah, but then people would need to switch from OpenTelemetry Core to Prometheus.
Collector.
And I'm not sure how that will play out, if that's something that is seen with good eyes.
**krajo Krajcsovits** 24:14 I mean, do people use the core only? I mean, they cannot…
Right now, you said a lot of people use Prometus, so they cannot use score, because they need to build…
**Arthur Silva Sens** 24:22 True.
Today, they don't… almost nobody uses a car. Like, the… the… switching…
Components to Core is the main reason… the main goal is to advertise Core.
**krajo Krajcsovits** 24:36 Yeah.
**Arthur Silva Sens** 24:43 We can discuss. Pablo is… Is very open to ideas.
I'm very open to accepting ideas as well.
We… we could discuss with Pablo.
**krajo Krajcsovits** 25:02 And who would use it? That's the question. Because people that are currently running exporters and run Prometus Receiver, they will be even more incentivized to do it if it gets into core.
So the… so the target audience is… People that want to…
People that don't want to run.
Prometous exporters, basically.
**Arthur Silva Sens** 25:27 It's people who want to replace 100 exporters once with one single binary.
Like, one single agent that collects all metrics from all infrastructure.
**krajo Krajcsovits** 25:40 Yeah, I assume they will run it per host, because otherwise it's going to blow up in their face, but yeah.
**Arthur Silva Sens** 25:45 Yeah, yeah, that's a demon set, I guess.
**krajo Krajcsovits** 25:47 Yep.
**Arthur Silva Sens** 25:50 Which is very common.
**krajo Krajcsovits** 25:52 Yeah, yeah, that's what I'm thinking, that that's very common, and also fits well with… you have a local thing running, scrape what it needs to do locally, receives what it needs to locally.
And it's one thing that you have to run everywhere. Yeah, that sounds pretty… Cool, yeah.
Yeah, I can see that.
And because it's one per host, it doesn't matter if it's a bit bigger.
Because it handles everything. Although, like, there's usually no such thing as, you know, one size fits all, so… I'm sure this… people will find weird use cases, but it doesn't apply, but…
**Arthur Silva Sens** 26:32 I… I can definitely see drawbacks. Like, the binary will… it's gonna be huge.
**krajo Krajcsovits** 26:37 Yeah.
**Arthur Silva Sens** 26:39 Like, the amount of… network spent to… to download the Docker images, it's just gonna be… Yeah, crazy.
**krajo Krajcsovits** 26:51 It's so strange that… Google has zero support for dynamic loading. Like, that's…
Because in most… on most of the hosts, like, how many times are you running MySQL? Like, you know.
couple of nodes, or I don't know, like, but not all of them.
So it's going to be weird to run this whole… thing everywhere.
**Arthur Silva Sens** 27:15 But they're running the contrib.
Yeah, that's true. They were running the collector-contrib already, so I guess they don't care.
**krajo Krajcsovits** 27:23 Yeah, it's… it's weird.
At least to me. I mean, but they can…
If… if all the exporters are separate, Things, then they can just…
Compile the thing that they need.
So you can optimize this if you want to.
**Arthur Silva Sens** 27:42 I mean, the…
**krajo Krajcsovits** 27:43 The binary.
**Arthur Silva Sens** 27:45 Yeah.
**krajo Krajcsovits** 27:47 Beautiful.
**Arthur Silva Sens** 27:47 We could… yeah, we could, like, build a builder as a service, I guess.
So you only build what is necessary for one specific host, and that's it.
**krajo Krajcsovits** 28:00 Yeah, yeah.
**Arthur Silva Sens** 28:02 That sounds complicated.
But useful.
**krajo Krajcsovits** 28:09 I don't know, to me it seems like…
for sure, the bigger, higher priority is the stability of the parameters receiver. Out of these two that you are talking about, or we are talking about, and I guess you agree.
higher priority is the stability of the Blumentus receiver, right? That seems more useful, at least.
**Arthur Silva Sens** 28:27 Yes, it is, but it is also the hardest.
Actually, I'm not gonna say it's the hardest. I haven't done the work of reviewing what needs to be done.
**krajo Krajcsovits** 28:37 Hmm.
**Arthur Silva Sens** 28:38 I'll do it, that's an action item for me, and then we can discuss how hard it is.
**krajo Krajcsovits** 28:46 Okay.
**Arthur Silva Sens** 28:48 One thing that I see happening a lot is Prometheus codebase.
Changing.
And that reflects when we upgrade the dependency.
Like, if we switch the behavior of the script manager.
Then it's gonna switch the behavior in the collector.
Yeah, we can discuss that when we get to that.
**krajo Krajcsovits** 29:15 Are you saying that because I merged the PR that changes the behavior of the script manager, or…
**Arthur Silva Sens** 29:21 I… I don't have a single PR in mind.
**krajo Krajcsovits** 29:23 Oh, okay.
**Arthur Silva Sens** 29:24 I just feel like this happens with a certain frequency.
**krajo Krajcsovits** 29:30 Right.
**Arthur Silva Sens** 29:35 Okay, any other topics?
**krajo Krajcsovits** 29:42 I just wanted to let you know that I'm looking at the… there's a PR on the receiver, for…
underscore created.
Metrics, so created timestamp versus open metrics counters.
So, yeah.
You don't have to deal with it if you don't want to. Although it's… it's superb.
complicated.
How, also.
Yeah, I'm not actually sure, bought a good solution.
There is… if there's a good solution.
Also, the… the… the… Like, the feature that they are trying to use is a feature flag
feature gate called Use CreatedMetric.
So you turn off created timestamp, or the created time in Prometus, in the script.
Which means that it… it simply gives you the underscore created metrics, right?
as a… and, so you get them in… in… in the… In the Prometheus receiver.
And there's logic in the parentheses receiver to turn that into start time.
**Arthur Silva Sens** 30:59 Yes.
**krajo Krajcsovits** 31:00 I think it's super weird, because…
There's no grouping, or, or like…
I don't think it's possible to actually tell if an underscore created metric belongs to something, and it was meant as a
start time or credit time in the receiver, but, like, best effort, I guess. So, who cares?
Oh.
**Arthur Silva Sens** 31:25 The whole point of open metrics too, right?
**krajo Krajcsovits** 31:28 Yeah, yeah, yeah, that's the whole point, that we put it on a single line, and now we got it.
Which also means that in Open… with OpenX2, this feature has, like, zero relevance for… for paramedics 2.
But, then the problem is that…
When, so it works mostly, except for counters.
Because the… the contour…
Name of the country has the underscore total, but the metadata doesn't have the underscore total, and there's some
Complication there, so we basically lose
the… the created timestamp. And it doesn't work.
And I think at least I know I… like, it took me half a day to even understand the problem.
And
The person gave a solution, but there's a lot of test failures, so I have no idea if it's right or not, or even if it's the right direction.
Anyway, yep.
**Arthur Silva Sens** 32:35 like… Since… Yeah.
on Prometheus side, we already discussed this underscore created
And we also came to the conclusion that we cannot reliably parse it.
**krajo Krajcsovits** 32:51 Yep.
**Arthur Silva Sens** 32:51 Can we just… recognize that the problem is the same. Like, we cannot do it.
And we need open metrics, too.
**krajo Krajcsovits** 33:02 I mean… -Oh.
The problem is that it kind of works for histogram summaries.
So, it's like… It's half… half… it's half there, so…
maybe we should just get rid of it before we make the feature stable, but I don't know how it would impact people.
It seems like this person is probably expecting it to work, and probably depends on it, so…
You cannot easily get rid of it, that's the problem.
Anyway, I will hack away at it, just letting you know that, unless you have a lot of time, please don't have to look at it.
**Arthur Silva Sens** 33:41 I… it was on my list to look at it.
But I have the same… feeling of overwhelm when I look at very complicated
PR, and I just assume it's gonna take too long.
But I'll try to help, no promises, but I'll try to help.
**krajo Krajcsovits** 33:59 Okay, fair enough.
You'll be bored.
**Arthur Silva Sens** 34:03 Yeah, thank you.
Alright, any other topics?
And I guess we can stop for today, and see you in two weeks.
**Arve Knudsen** 34:22 But…
