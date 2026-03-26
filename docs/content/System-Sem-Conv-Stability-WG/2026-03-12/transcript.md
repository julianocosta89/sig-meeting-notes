SIG: System Sem Conv Stability WG
Date: 2026-03-12
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/l1xsqYTvAStFihab0DSrPmVXzehu067ehiXiXdf-az6pmQ9jM4o5x4aj9az8BAZ3.9f70y4T_blFJc1y1
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:02 Anyways… What's this note-taker? James Fellow's notetaker.
**Braydon Kains (Google)** 01:23 Probably one of those auto-sync Zoom… AI bots.
**Donal O'Sullivan** 01:33 Quite invasive, isn't it?
**Braydon Kains (Google)** 01:36 Oh, yeah.
like… I mean, these are public meetings, so it's not like… where we, like, we've already consented to being recorded by CNCF, but not by random people's AI bots.
**neil yashinsky** 01:52 Hey, Braden, hey, Donald. How's it going? Yeah, I've been on a few, and I gotta say, it's almost like every other meeting, there's some random record-o-bot or whatever. Trying to record, I should say. Not attempting.
**Braydon Kains (Google)** 02:04 My theory is that people, like, have, for work, there's just some note-taker attached to their account, so when they sync the hotel calendar.
It goes to the whole thing.
**neil yashinsky** 02:16 I think so, too. That's exactly what I think. It's kind of like accidentally consenting to this, or unaccidentally consenting to this, I'm not sure exactly which one it is, but yeah.
**Braydon Kains (Google)** 02:24 There is one where, like, if you type opt-out in the chat, it goes away. I tried that, it did not work.
**neil yashinsky** 02:31 Oh.
**Donal O'Sullivan** 02:38 I assume the individual is a… Is that the… is that the actual person, James Fellow, I wonder?
**Braydon Kains (Google)** 02:44 No, I think this is, somewhat… because… Fellow… fellow note-taker is probably… And yeah, it's fellow.ai, it's… it's a…
**Donal O'Sullivan** 02:55 Hmm…
**Braydon Kains (Google)** 02:56 Natural, like, startup. So…
**Donal O'Sullivan** 02:58 Okay.
**Braydon Kains (Google)** 02:59 The person's name is James, but there's a few…
**Donal O'Sullivan** 03:01 there's a.
**Braydon Kains (Google)** 03:02 Hugh James's.
**Donal O'Sullivan** 03:04 Yep.
**Braydon Kains (Google)** 03:04 So, I don't know who we're gonna… who we… who we talked to.
Okay, good.
**Christos Markou** 03:20 I just kicked that out.
**Braydon Kains (Google)** 03:24 I was about to whisper the bot to fuck off, so… It's probably… it's good that we kicked off.
**Donal O'Sullivan** 03:29 You never know when that recording can end up haunting you. Good call.
**Christos Markou** 03:59 Do we know if Pablo, will join?
**Braydon Kains (Google)** 04:27 I haven't heard from Pablo today.
**Dmitrii Anoshin** 04:34 I've heard he is busy this week, I don't remember specifics, but Albert.
So I guess we can start without you.
**Braydon Kains (Google)** 04:43 Church.
I forgot to put it on the… schedule, but I… I'm getting that requirement level PR reopened.
That's pretty much the only update I have.
**Donal O'Sullivan** 05:12 I, I merged the, the other PR for updating the, process resource attributes, requirement levels.
And I opened another… pull a request for… I know that there was some.
**Braydon Kains (Google)** 05:26 for executable?
**Donal O'Sullivan** 05:29 Yeah, exactly, yeah, spot on, yeah, yeah. I can put it in the doc if that helps.
**Braydon Kains (Google)** 05:33 I took a quick look at it, too. I'll write a response, too, but I think… the best path forward is actually for us to start looking into introducing, like, general file semantic conventions, like, just, like, attributes about files, because they're useful in multiple ways, and it would still address all the stuff that Process Executable wants.
So probably that's the, like, Quote-unquote, right thing to do.
And actually, there is another thing that came up recently that kind of needs that, which is, semantic conventions for… Like, log attributes?
Like, right now, the file log receiver, attaches, like, log file path and file name and stuff, and it just sort of, like, invented those attributes the way they are, but, like.
If we had file conventions, they could… they could attach themselves to those pretty easily.
So, yeah, multiple… There's multiple things that would benefit from us introducing file conventions, so that's probably the next step.
**Donal O'Sullivan** 06:41 Okay, interesting. So does that mean we won't be adding process executable as a separate entity then, right? It would be…
**Braydon Kains (Google)** 06:47 We would… so we would still be adding it as an entity, but… Its attributes would come from a registry of, like, general file information, because, like.
**Donal O'Sullivan** 06:57 Hmm.
**Braydon Kains (Google)** 06:57 So some stuff about the executable might be specific, but most of the stuff that they want to know about process executable is just, like, what's the file's path and file's name, and, like.
**Donal O'Sullivan** 07:08 It's sort of.
**Braydon Kains (Google)** 07:09 thing. A lot of that stuff is just, like, information, general information about any file, like, it doesn't matter if it's an executable specifically or not, so probably it would be, like, the executable entity is an entity, but it uses attributes from the file registry.
**Donal O'Sullivan** 07:24 Okay.
Yeah, makes sense, makes sense.
**Braydon Kains (Google)** 07:27 I say all this as someone without ample time to, like, try and introduce it, but I will, open an issue to get the discussion started, and maybe we can talk about it at KubeCon for those of us who are there.
**Christos Markou** 07:42 Yeah, I was about to raise this, yeah, I was chatting with a few folks, and also mentioned that to Pablo.
I guess… Bridon, you are going. Dimitri, you will be there as well. I know Roger, Pablo will be there, so maybe we can, find a time for us to, like, meet and discuss things, if you agree.
**Braydon Kains (Google)** 08:06 Yep.
**Christos Markou** 08:07 It's not yet sure, because this time we will not have the observatory. It's a bit complicated. There will be a booth, in the pavilion area, a smaller booth, like the other CNCF projects have.
So either we'll need to have something centrally to get some, to see what community managers will… from what they will, tell us, or maybe we can self-organize and find a place to, you know, go and discuss.
**Dmitrii Anoshin** 08:38 I heard that we missed the deadline to submit a request for the booth, and we probably won't have anything.
**Braydon Kains (Google)** 08:44 Is that… is that what happened? Okay, I was wondering. That's a huge loss to not have that.
**Christos Markou** 08:50 I… so, Observatory will not happen, usually that was paid by Splunk, Dimitri, right?
**Dmitrii Anoshin** 08:56 Yeah, I mean, the observatory, no, but even the booth, we lost.
**Christos Markou** 09:00 who lost the deadline, but they managed to secure one for one day, I think, something like that.
**Dmitrii Anoshin** 09:06 Oh, okay.
**Christos Markou** 09:06 So, yeah, we will have something only for one day, but in our case, yeah, we can find the time and, you know, make some…
**Braydon Kains (Google)** 09:14 So we only… we only even have, like, in the CNCF pavilion, we only have a booth for one day.
**Christos Markou** 09:18 For one day, yeah. Wow. That's… That's…
**Braydon Kains (Google)** 09:23 That's gonna be interesting, because, like, the observatory was really popular with people, like, just coming and asking general questions about the project, and, like, it's… probably one of the most popular CNCF projects that people would want to come and talk about, so that's going to be interesting.
**Christos Markou** 09:40 We can occupy always a table at the lunch area or something, and put some hotel, yeah, brand stuff there.
**Braydon Kains (Google)** 09:49 Buy some, like, some craft materials from a dollar store, and, like.
cut out… cut out open telemetry on a Bristol board or something.
**Christos Markou** 09:59 Yeah.
Anyways, yeah, I will, post later, maybe next week, so as we can coordinate once we know more and see what time is preferable for every one of us, so we can, schedule it then.
**Braydon Kains (Google)** 10:16 Sounds good.
And I think last time, I missed… I missed last week's, we had mentioned that, like, that requirement level on the… on the attributes was sort of the last thing we wanted for, cutting a process release candidate. Was that… Is that right?
**Christos Markou** 10:36 So I think last… yeah, there was a one PR from Donald, and that was merged. That was the requirement level on… On the…
**Braydon Kains (Google)** 10:45 the entity.
**Christos Markou** 10:46 On the entity attributes, yes. And then there is the requirement level on the metrics, the PR that you're trying to reopen, and Donald also sent an issue in the PR, I think, to, introduce the process executable, entity, so I think these two are the leftovers, and, maybe after this, we can consider the, the RC, I guess.
If we can do it this week or next week, that would be great. If not, yeah, no worries.
**Braydon Kains (Google)** 11:19 Yeah. It would be… it would be good to be able to do it before Roger's talk.
**Christos Markou** 11:24 Yeah, yeah, sure.
We can even, like, yeah, we don't have permission to merge, but if we had, that would be cool to merge it, like, live, maybe, during the…
**Braydon Kains (Google)** 11:35 Yeah, that would be… that would be funny.
**Christos Markou** 11:36 Prometus folks do it, usually.
**Braydon Kains (Google)** 11:39 Yeah.
**Christos Markou** 11:39 Yeah, anyways.
**Braydon Kains (Google)** 11:41 The… there was… in the… I'm just trying to get the PR reopened, so once the PR is reopened, my updates should show up, and there was one… one spot where I… Was questioning a little bit.
Just a little, like, Piddly thing, but the… For a page fault, the page fault metric, I marked the fault type metric, as recommended.
Because… It might be useful to some… like, someone might care To aggregate over that attribute.
To get the sum of major and minor.
So I figured making it recommended was the right call, but if anybody disagrees… like, the general… the thought process I took was, like.
Basically, if the metric is useless without the attribute.
like, if… or, I shouldn't even say that. Like, there are some aggregations that technically make sense, even though I think they're useless. If the… if the aggregation literally makes zero sense, then I make the attribute required.
So, like, for CPU mode on the CPU time metric, we discussed, and I made… I decided to make it required, because, like, if you sum over CPU… all the CPU modes, it's just the elapsed time, like, that's not actually… A usable metric that anybody cares about.
And, like, things like for network I.O. direction.
the… summing over in and out does not make any sense either, so I didn't. But for major and minor page faults, you might want to get a sum of all the page faults, so I made that one recommended.
If anybody disagrees on that, we can… we can discuss, or we can just merge it that way.
**neil yashinsky** 13:37 Sounds, sounds like, you know, good defaults or whatever. Doesn't sound anything questionable to me.
**Dmitrii Anoshin** 13:46 I can potentially see if, like, users aggregate everything.
And the CPU time, I'd want to… Get, like, number of… course.
That would be the value right. Number of course… number of cores, times elapsed.
**Braydon Kains (Google)** 14:07 The last time, yeah.
**Dmitrii Anoshin** 14:09 So, like…
**Braydon Kains (Google)** 14:11 I think we do provide a core count metric, though, right?
**Dmitrii Anoshin** 14:14 Yeah, we do provide it, but, for example… I mean, it's just… we need to maybe clarify what's meaningful here, and if there is a meaning, we can find the meaning for that. I can even argue that we can find the meaning for the direction as well.
someone can… Like, just worry about… Overall traffic over the particular… Particular host, for example, and don't care whether it's egress or ingress.
**Braydon Kains (Google)** 14:48 Hmm.
**Dmitrii Anoshin** 14:49 And, they would maybe potentially do some more average.
I mean, it's useless, In practical way, But in technical… Way, it's kind of… can be considered as meaningful? So, I'm not sure where we draw the line.
It probably…
**Braydon Kains (Google)** 15:10 Yeah.
**Dmitrii Anoshin** 15:11 We do have it somewhere referencing Prometheus guidelines, when they say.
Aggregation must be, like, meaningful. But what meaningful is, it's also questionable.
So, I'm just… my point is that, yeah, it's not ideal, like, it doesn't make a lot of sense, but do we have to restrict users? Like, will the data that's… Produced by the… by the aggregation.
Or completely incorrect or wrong.
That's.
**Braydon Kains (Google)** 15:52 There's… there was one case, which was that for the CPU mode, Like, if… if you, if you aggregated over it.
Or, like, if you didn't include the CPU mode, the fact that there's, like, Multiple possibilities for states.
Means that there's no way to classify whether you've actually summed all the states, or if you've just, like, chosen some to… like, some people will do aggregations of, like.
All the non-idle time, so any state that isn't idle, and then produce that as a metric.
and, like, it becomes ambiguous what they mean if the attribute isn't there. But that is still a question of, like, whether that's our job to enforce, like.
In fact, does required mean that, like.
an aggregation would violate our conventions. Is that how that would work?
**Dmitrii Anoshin** 16:55 Aggregation would violate the conventions, but what…
**Braydon Kains (Google)** 16:59 I'm just… I'm just thinking, like.
in a future, like, there's talks of people, like, implementing Weaver on the server side.
To, like, validate that data coming in adheres to whatever semantic conventions registry, and, like.
if someone sent in… like, let's say CPU.mode is a required attribute, and someone sent data to the back end, and Weaver tried to validate it.
I guess that would fail, because it's missing the CPU mode?
**Dmitrii Anoshin** 17:32 If it's required.
**Braydon Kains (Google)** 17:33 Yeah, if it's required, then…
**Dmitrii Anoshin** 17:35 But here we're talking about whether making is required or not in semantic conventions. I don't… I'm not saying that we should violate whatever is defined in semantic conventions.
And now we are discussing semantic conventions, right?
**Braydon Kains (Google)** 17:49 Yeah, right, well, this… that's what I mean, like, if we consider…
**Dmitrii Anoshin** 17:55 Like, if it's useful to have it required specifically for the validation of the backend in that case.
**Braydon Kains (Google)** 18:05 Yeah, I'm just trying to… I'm trying to make sure I don't, like.
paint us in a corn… paint users in a corner by making a decision like this. So, like, if we… if we mark… It will, in that case, should we mark any attribute as truly required? Because we don't want to restrict them from being able to do Aggregations that they feel like doing.
like… I think we're trying to only introduce attributes that, like, are… Are summable or aggregatable in some way.
And so, if they decide to do those aggregations at collection time, and then send to a backend that's validating semantic conventions, and all of a sudden they're violating semantic conventions just because they decided to do some kind of calculation on it that we're now saying, like.
don't aggregate. Ever.
on some… on some specific attributes, like, maybe that's… like, maybe we should just call them all recommended, or, like, recommend… recommended if we think they should be there, but, like, should… is… I… I'm now struggling to think if there's a case we should ever call anything required.
**Dmitrii Anoshin** 19:10 I see what you mean. So, your point is that required, Potential purpose of required is the use case when they want to use it for validation of particular metrics.
So…
**Braydon Kains (Google)** 19:27 We've even been talking about it at Google, the possibility of, like, implementing Weaver in a backend to recognize when something is valid semconf before routing it somewhere.
**Dmitrii Anoshin** 19:37 Yeah. I mean, okay, to… counter-argument, like, against what you originally said, if they don't have a full set of labels, and they aggregate a full set of states, and they aggregate over some of them, they will be having run metric. It's applicable to any recommended attribute, essentially. If we only aggregate over a set of CPU cores, it's gonna be incorrect metric. So, I think here we… let's just… don't bring that, at least. Here, we're thinking about aggregation over all all MTSs.
we are not talking about subset. So, I guess that thing we should not consider. But, required to Using the required as a, like, extra validation, and on the backend.
and, like, providing the best practices from our side, from OpenTelemetry, semantic conventions, I think that kind of makes sense.
I'm not 100%… still, like, convinced, but yeah, I guess it's probably… better for us, because otherwise, if we… as you said, we can potentially mark everything as deprecated, and we… if we draw the line about… meaningfulness.
To be, like, too wide?
It would, not be good from our side.
Like, saying, hey, like, there are some attributes that are… Clearly good for aggregation, core, and some of them which are not ideal for aggregation, like state. And if we don't… don't separate that in any way in semantic conventions, it's kinda… maybe… Makes it unclear.
**Braydon Kains (Google)** 21:40 Yeah. Like, the best we'd be able to do would be just, like, in our, like, documentation, to say, like.
you… you can do… you can do aggregation on this attribute, but we don't think it's gonna give you a good value, so we recommend you don't. But, like, that's not a… that's not a very… Aye.
It's not a sh… not a strict enforcement.
**Dmitrii Anoshin** 22:01 Okay. But…
**Braydon Kains (Google)** 22:02 Like, the… but the… the… the straw man I'm thinking of is this… this… there's been this theoretical pitch I've heard of, like, you know, using Weaver to recognize something coming in as semantic conventions, and then automatically, like, populating dashboards or something based on that.
And, like, if someone has done aggregation on a required attribute, and then that attribute no longer goes there, and then that breaks Weaver's validation, it's like, okay, this is not semantic conventions, I'm not going to automatically populate this to some dashboard.
**Dmitrii Anoshin** 22:36 No, I'm not saying that we should allow aggregation of the required attributes.
we should… we should stick to the conventions, and we should not allow… and currently, M-DataGen doesn't allow you to… Right. If you… I made something from the attributes list. Amid something required, it'll give you an error. So I…
**Braydon Kains (Google)** 23:00 I think that means, like, any time we're… any time we think someone could reasonably aggregate over something, we should just say recommended, even if our recommendation is to not aggregate.
It's like… Technically speaking, someone still could do… still could aggregate.
**Dmitrii Anoshin** 23:22 Yeah, but at the same time, the validation part on the viewer, you…
**Braydon Kains (Google)** 23:27 And so it's like, to counteract that, we just always say recommended, basically.
**Dmitrii Anoshin** 23:33 No, no, I mean, I think we should… clearly identify which one… which attributes are, like, good for aggregation, which are not. So, yeah, probably, I would, I think we can go with more strict definitions of the required. So, for example, yeah, as you mentioned.
Direction and state can be required just… not… just because Let's say, reaggregation over them.
Provide some meaningful, Data, but we don't believe that data is useful.
So, like, we can be more opinionated here, and I think it's fine.
So, I'm just… my point is that let's maybe update our guidelines, and not use word meaningful from Prometheus, but… Something like, useful, from OpenTelemetry perspective, or something like that.
Does make sense?
**Braydon Kains (Google)** 24:41 Yeah, I think so.
**Dmitrii Anoshin** 24:42 Okay, cool. And anyway, they potentially can just, whoever wants to violate that and aggregate over… CPU states, for example, they can just add another processor if they want to.
**Braydon Kains (Google)** 24:56 Yep.
**Dmitrii Anoshin** 25:00 Cool.
**Braydon Kains (Google)** 25:01 Okay.
That car will be hopefully reopened soon, once a maintainer sees it.
**Christos Markou** 25:13 Anything else, folks?
**Braydon Kains (Google)** 25:17 Not that I can think of.
**neil yashinsky** 25:20 for me.
**Christos Markou** 25:20 Sounds good.
Okay, cool. Thank you, Ronan. See ya.
**neil yashinsky** 25:24 Thanks, have a good one. Bye.
**Dmitrii Anoshin** 25:26 Thank you, folks, bye.
**Donal O'Sullivan** 25:26 You guys.
