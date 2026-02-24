SIG: Collector SIG
Date: 2026-02-04
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/QrZq2dIeMxW1XxHcPs5mc1t4k4N-F7KLIMyu8PKrCrQ4_DFwcWDbOtDwn23snI8M.SpqvgCwfkCZTta4d
============================================================

## Zoom Recording Transcript

**Blake Rouse** 03:56 Hey, how's it going?
**Andrzej Stencel** 04:01 It's good.
How's it going on to your side?
**Blake Rouse** 04:10 Really cold, a lot of snow.
**Mikołaj Świątek** 04:16 Really cold? How cold is that?
**Blake Rouse** 04:21 I gotta get to eat in Celsius, soda.
Negative 18.
**Andrzej Stencel** 04:30 Celsius?
**Blake Rouse** 04:32 Yes.
**Andrzej Stencel** 04:33 Hmm.
**Mikołaj Świątek** 04:35 That's properly cold.
**Blake Rouse** 04:37 Yeah.
**Andrzej Stencel** 04:40 My side of Poland, it's minus 7. Mikawaii, how about you?
**Mikołaj Świątek** 04:44 In theory, it's minus 5, but it feels much colder when you go out. It's very windy and kind of a little bit humid.
**Andrzej Stencel** 05:43 I can see someone added…
Link to the pull request in this first slot. Anybody want to talk about this?
**Pablo Baeyens** 05:55 I can… talk about it, so… This is… let me…
We're also running on the Zoom chat…
This is a PR for a template to mark components as, stable. The Prometheus receiver,
Folks mentioned that.
it was close to being stable, and I suggested we do this on Arthur Ha's
open this. The idea is to have some sort of checklist out,
An approver or maintainer, can…
Go through to make sure that, the component is stable.
Before we actually do the thing and market.
So… Yeah, I think it shouldn't be controversial, most of it…
was already on the component stability document, but yeah, I would appreciate reviews. I will review it myself.
This week.
And also, I didn't…
the link, let me add it now. There was some discussion on the issue I just linked…
I think would be good to have more.
more feedback on, so one of the requirements for stable components is that,
Component owners, will work on… Bugs and performance problems,
And that there will be 3 active cod owners.
we… Do you not have a documented…
Process for that, in terms of, like, what does it mean to be active, or what,
What does it mean for code owners to work on them? We have the triage document, but that's…
Maybe not sufficiently detailed.
Yeah, we've had some discussion here about, like, do we want to have some sort of SLO,
the… but maybe not call it an SLO to avoid, like.
The expectation that we are a company or so, it would be great if we have opinions from more people on that issue.
**Mark S (Smart Pension)** 08:46 Apologies, I'm new here. Where would the best place to put those comments and feedback?
**Pablo Baeyens** 08:54 I linked the issue on the meeting notes, let me also…
put it on the Zoom chat. This issue is specific to… oh, it's the last one I sent on the Zoom chat. The issue that I linked is specific to the Prometheus receiver, but, I mean, if you have thoughts in general about the Prometheus receiver, or…
about how this should work in general.
It's a good place to put them. It's the first component we are working on, so we are going to have some
General things to solve.
Alright, I think we can move on to the next one.
**Israel Blancas** 09:50 Hi, all. So, well, the things that I have done here that have been reviewed, I retain Ryan, has been there for a while, mark as maybe to be merged, right, but never was merged. So please, you can take a look,
well, if you have any kind of concerns or something about it, just let me know, right, and I will be more than happy to address them.
No, we can do something to have it merge.
Great.
**Pablo Baeyens** 10:27 Okay, yeah,
I haven't taken a look at this PR, but…
I can…
No. I can do so.
**Israel Blancas** 10:49 Thank you.
**Blake Rouse** 10:59 Okay, I think I'm next.
on the list.
This is a feature request,
For enabling, it's that first issue there, for enabling partial reload.
For, the collector, specifically in the graph.
At the moment, it, tears down everything and brings it back, any change? And… you know.
At Elastic, we would like to improve that flow, you know, the full restart results in
Events and flow being lost, and downtown windows, things like that, with simple changes, like adding a new pipeline, or just adding a new receiver.
And so that's the motivation, for this proposal.
It is something that…
we would use right away, as soon as, well, this is something that would be behind a feature flag. We would be… we would want to do it in a way, as an always try for… as a collector strap and go for stability. This would affect no current flow at all. It would be feature flag gated.
And, it would result in…
When that feature flags on.
The support of rolling through the partial reload path instead of the full reload path that it uses today.
And we would use it, right away. Like, as soon as this was merged, and available, we would enable this feature flag.
And actively support it and maintain any bugs or anything like that.
So I just wanted to bring it up in the call, and
I don't know, see if anyone had any opinions on it, see if it would be something that you all would be okay with accepting. Obviously doing, like, a rollout plan.
And then at the bottom of it, in the other two issues, I did kind of, like.
To prove that it works.
The first issue is, you know, like, kind of a phase one only, and then the second issue kind of shows that the whole thing.
can work. So, to get it merged, it'd probably be more of taking that last issue, or that last PR, and splitting it up into the different phases, and slowly getting them merged.
**Jade Guiton** 13:21 I'm… A little bit concerned about the complexity of the change, to be honest, and…
Like, complexity is fine as long as there's a very clear win.
To me, it's not entirely clear, because… Even if we only reload.
Like, first of all, it seems from the proposal that if an exporter's config is changed, it would still be reloading the entire pipeline.
So, it sounds to me like it would only reduce downtime windows in some cases.
But it would not eliminate them.
And it also doesn't seem like it would…
prevent lost events. Like, one thing to be clear is that
The collector's shutdown process is supposed, in principle, To avoid lost data.
By shutting down receivers first, and then…
processors and then exporters. In principle, they're supposed to flush their data in the process.
So if there are bugs with that, it seems to me like partial reload would not solve them.
So, I guess I'm… I'm trying to wonder… I'm kind of wondering… Does this actually… Address the fundamental problems.
**Blake Rouse** 14:42 It does for us and our use of the collector. We have a lot of receivers that come and go, often. The exporter does not change
often. And the whole restart of the whole pipeline, every time a receiver comes and goes, is a big problem. It provides basically no window of time for the collector to stay running.
And for events to be sent, because we're just adding a receiver, and it's causing the whole, pipeline
To be completely restarted.
So, it does have that on us. It could be limited to just supporting receivers, which is what our main need is.
But my goal, obviously, was just to provide an implementation that
Worked across the board for all
All pieces, in the, in the collector.
I don't think you're wrong on the regards to if you change an exporter, the whole pipeline gets restarted. It does, and would work that way. But things like adding a new pipeline wouldn't…
affect another pipeline at all.
You know, so there's some real benefits there, like.
You know, no need to restart another pipeline that's completely unaffected by…
A new pipeline, or you have two pipelines and you only change one pipeline, why are we restarting both pipelines?
So there's a lot of… of benefits there, I think, in… Just those flows.
**Jade Guiton** 16:24 Hmm, fair enough.
I don't fully understand the use case, I'm not sure how many…
Users are constantly changing their configuration, but at least for receivers, it is pretty compelling.
Although, yeah, it's just to me that…
The fact that it doesn't actually address downtime for the receivers that are being
Configured, to me, feels like the…
The real solution is, you know, using load balancing and gradually rolling out changes.
But… It does sound interesting. Yeah. Mikolai?
**Mikołaj Świątek** 17:04 Something… something worth noting is that there's some overlap with Receiver Creator.
And…
because receiver creator, in principle, is supposed to kind of address this idea of spawning things dynamically based on some event from the environment. Unfortunately for us, that doesn't really work, because what we're actually trying to do is we're trying to
replace the, replace most of our stack with the auto… a lot of our stack with the auto collector underneath, and we have, like, an existing templating language.
And mapping that to receiver creator is very difficult. We don't want to go into the receiver creator and just, try and…
shoehorn a bunch of stuff in there that it doesn't necessarily need, which is why we're… we want to do it in the collector proper. A, yes, there is a complexity, but this is an improvement for all users. Ultimately, it's going to be an improvement, and it makes… in particular, it makes a pretty big… er…
these are the things that I recall also earlier coming up with some regularity when it comes to remote management and opam, where in a remote… kind of in a remote managed collector, you'll often get a situation where you have, like, only maybe one or two exporters, and then you're kind of moving around your input, let's call it. So you're adding, or…
Removing receivers, sometimes whole pipelines, but which usually terminate at the same exporter.
And especially if you're trying to do something like multi-tenancy in a single collector, so in some respects, maybe your pipelines are owned by different users, then you also don't want things to cross-effect
each other. And that is, like, a somewhat niche use case, but if we could support it without bringing pain to anyone else, I think it would be quite nice. And in general, this is just, like, a performance improvement.
The fact that you can,
You can just, keep things running that could be running.
**Blake Rouse** 19:32 I'm kind of new to these calls, I don't know how something like this Goes about, you know…
Obviously, I'm looking to work on this, but, you know.
Wanted to see, you know, everyone else's… Feedback on it, and…
You know, so… so what do we do from this call standpoint? Do we… do we…
I don't know, someone let me know, because I really don't know.
**Mikołaj Świątek** 20:00 You, like, you show up to the next one in a week as well, and do the same thing, so all the audiences can hear your pitch, and then you wait for comments on your PR if there's, like, no yelling during the actual SIG meeting.
**Blake Rouse** 20:18 Alright, sounds good.
**Dhruv Shah** 20:22 Yeah, I guess, I'm the next person, I think. So I've raised one, feature request in Routing Connector.
So I got one comment from Bogdanrutu, but I haven't heard anything, post my clarification to his comment.
So, this is regarding the new, copy and move configuration, array to routing config… Routing connector.
So, according to the latest, configuration changes.
If you use, copy action.
The data stays in the default pipeline, but we have a use case where, if there is any condition matched under the routing table entry.
Then we don't want data to be sent to a default pipeline, but that is not possible under this new configuration.
So I proposed a change in configuration that we add a third option that says that, copy to non-default. That is, if data is sent to any non-default pipeline.
We should not send it to the default pipeline.
I'm gonna… Any comments, any suggestions or ideas?
**Edmo Vamerlatti** 21:45 Yeah, sorry, I tried to understand this issue, because I didn't… I didn't see this feature before.
He's pretty new, I think it was, didn't.
**Dhruv Shah** 21:55 Yeah, yeah, it was recently, probably a week or two ago.
**Edmo Vamerlatti** 21:59 Yeah, but I think the behavior is still the same, but the action is just moving or copying the data, right?
**Dhruv Shah** 22:06 Yes, that is correct.
**Edmo Vamerlatti** 22:07 Oh, you need.
**Dhruv Shah** 22:08 data to…
**Edmo Vamerlatti** 22:09 Okay, so…
So what you need is to cop the data, but just… but not for the default pipeline, correct?
**Dhruv Shah** 22:16 Yeah, yeah, in case if there is any match with the conditions under routing table, then do not send it to the default pipeline.
**Edmo Vamerlatti** 22:24 Okay, but in that case, you want to copy because that data will match another condition, or just because you…
**Dhruv Shah** 22:32 Yeah, yeah, I want to copy because data is matching in the other condition. And mainly, I mean, this copy feature was introduced because
Due to using multi-layer routing connector, right, we were copying a lot of data here and there.
So they wanted to create a single layer of routing connector, so that, you know, we don't have to copy data to multiple connectors.
**Edmo Vamerlatti** 22:54 Okay, I see.
**Dhruv Shah** 22:55 Yeah.
**Edmo Vamerlatti** 22:56 Okay, okay, I'm gonna take a look on the issue and try to answer there then, because I'm not aware of this feature very much, to be honest, but I'm gonna take a look and answer on the issue, if that's fine for you.
**Dhruv Shah** 23:09 Sure, sure, sure. Yeah, I really appreciate that, Eddie. Thank you.
**Edmo Vamerlatti** 23:13 Take care.
You can go ahead, Berkel, and…
**Perk (Marcin Stożek) | Elastic Ingest** 23:56 Yeah, hey, I'm looking for a good word, thanks.
Hey folks, I'm Perk, and yesterday I had a very, very interesting discussion with Andre here. We spent, like.
couple of hours, to say the least, going back from the, auto unplugged, that was, that was on Monday.
And we've discussed in particular about the collector API, meaning the configuration API, and, you know, the naming that we use for different components, different input, sorry, receivers, and exporters.
And I wanted to ask you if that's only us that feel that sometimes the API that we use for our configuration is not in the best shape it could be.
And by that, I mean that…
We have multiple components named after… sometimes the feature that they… that they do, sometimes after the…
protocol that they use. Sometimes we have receivers and exporters, disconnected, like, we have, Andre Pitch called me through here, I believe, like, we have one receiver for OTLP and two different exporters, and we have additional one other receiver for OTLP JSON file.
Right? And when you take a look at all of this, it feels like, it… like, there could be a little bit more care attached to all this.
Anyone else feels the same? Thanks.
**Jade Guiton** 25:39 I think that when we're dealing with something like Contrib, where everyone is contributing their own component, it's a bit inevitable that there's going to be some…
Redundancy or inconsistency in the naming?
The OTLP receiver and exporter, I do kind of agree.
That it is a little bit confusing.
But I guess, you know, one difference is that
Having one receiver being able to receive from multiple things.
Isn't as problematic as having an exporter that would export to two different places, but…
I guess the bigger problem is that we can't really change things.
At such a high level at this point. Like, renaming components is doable, but…
Splitting up, I think the OTLP exporter would be a lot more difficult. Oh, sorry, the OTLP receiver.
**Perk (Marcin Stożek) | Elastic Ingest** 26:39 Yeah, yeah, so one thing that comes to my mind is that, if you have projects that are very long
long-running ones, you know, for multiple years. At some point, you do have breaking changes, and you do redesign things, and this is not something that I propose right now to do right now, like, I think that these things should stay as they are right now, but going forward, maybe we should come up with a plan to just clean it up.
That's all I'm saying. Yesterday, we, for example, took a look at how Vector does this.
And it feels much more coherent, to be honest. Much, much more coherent.
So, just a food for thought, Andre?
**Andrzej Stencel** 27:27 We have this, notion of encodings.
So, for example, the file exporter currently exports OTLP in either JSON or Protopath.
But maybe we could… Use some other encoding.
Actually, it does already support any encoding you specify. If you have an encoding extension that does something else than OTLP,
then that would support it. But to import that data from the… exported by the file exporter.
I don't think we have a corresponding component other than the LTLP JSON receiver, which imports OTLP JSON online.
That feels inconsistent.
And yeah, it's true, it's contrived, and things come in a specific shape. Maybe we as maintainers, including me, of course.
Could do a better job at, Shaping this.
And maybe using more, of the encoding, Architecture.
**Pablo Baeyens** 28:33 Apart from the encoding thing, do you have any other, like.
Suggestions on… on what to do about this?
like, in… to, do you want to write guidelines, or,
enforce it automatically, somehow, I don't… I don't know how that would work, but… Maybe there is some
Something to be done.
**Perk (Marcin Stożek) | Elastic Ingest** 29:01 Yeah, having guidance seems like a very good start, at least, right?
Because I don't think there is anything like that at this moment, about the overall architecture of the configuration, and how components are being named.
And use, and what's architecture underneath, really?
what's the user feel? Like, when they use this configuration, when they want to configure their collector, like, you know, how do they think about
things, right? Whether they think in, I don't know, transport protocols, and then the payload that is coming, or they think about the OTLP as both of those functions, you know? So, I'm definitely for the guidelines, at the very least, right now.
**Andrzej Stencel** 29:47 Yeah, as Perk mentioned, we looked at different project vector specifically, and it seems to keep
This split that a component
is about a specific source or destination, for example, a file, HTTP endpoint, or S3 bucket, and then you can have encoding
which… specifies whether we actually want to export things in OTLP,
sort of format, or maybe just plain text, lines, or something else, Avro, or something else, right?
**Jade Guiton** 30:29 I think… It seems like… Oh, sorry.
I wanted to say, I think the distinction between where you're putting the data and what encoding it has makes sense for some exporters and receivers.
But I think a lot of the time it's kind of intrinsically linked.
like, for example, like, how would you split up the OTLP exporter between… The encoding and the protocol.
like, I don't… I think there's a limit to how, like, for a lot of…
Exporters, they could be flexible in this way, and, you know, allow you to combine any two options.
But I think that's maybe too much to ask for from every single exporter, if that makes sense.
Like, I don't know, the Datadog exporter, like, you can't, like…
send it under Prometheus format, it's not gonna make any sense.
**Andrzej Stencel** 31:31 Of course, of course. And also, OTLP is probably special in terms of OpenTelemetry collector and an OpenTelemetry project. We probably want to make it easy to import-export OTLP, and having an OTLP exporter and importer probably makes a lot of sense.
And yeah, as I say, not every encoding makes sense for every destination or source.
Just, yeah, as Park said, it's just cruise for not any specific, like, action items to take now.
**Jade Guiton** 32:02 Yeah, I think, like, maybe filing an issue about the different things that You think don't make sense?
And so they could be addressed
like, on a case-by-case basis, I think could make sense.
**Andrzej Stencel** 32:20 Yeah, makes sense. Makes sense to me, thanks.
Anybody have anything else?
**Pablo Baeyens** 33:02 I guess at some point we'll share the discussions we had on… unplug on Monday,
There are some meeting notes, but I need to… Check with,
the organizers, with Ted on… Rafana, in general, to see…
How do I want to share this, but, we had some discussions about
maintaining contribib about the OCV, un…
well, some other more general topics that are not only about the collector, but there were a few…
collector end users that provided feedback about this, and I think it's… It's worth reading.
Thanks, Brian.
Think we can… call it a day?
**Blake Rouse** 34:12 There, by everyone.
**Evan Bradley** 34:13 Thanks, everyone.
**Perk (Marcin Stożek) | Elastic Ingest** 34:14 Thanks, Al.
**Israel Blancas** 34:15 Give her day.
**Mark S (Smart Pension)** 34:17 Bye, folks.
