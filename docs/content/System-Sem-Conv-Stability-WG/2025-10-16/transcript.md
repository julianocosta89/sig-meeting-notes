SIG: System Sem Conv Stability WG
Date: 2025-10-16
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/mclNMKDxehfIX712ShhmxuTu1os_N7zWCx0QgsxNUWGIBkpsQ2KgMa9fujh1HGot.aTLcYB1r_2wmacfa
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin** 01:32 Hi, folks.
I'm not sure if anyone was gonna join.
Vibrate them.
**Fraggle Rock (ca-wat-brt3)** 03:10 Hello, sorry, I was in the washroom.
**Dmitrii Anoshin** 03:15 I was like, who's the flat fragile rock?
**Fraggle Rock (ca-wat-brt3)** 03:18 If it's a silly meeting room name, it's always me.
**Dmitrii Anoshin** 03:30 Cool, I wasn't able to join last few times, but I'll be available going forward.
Do we have anything to discuss today?
**Fraggle Rock (ca-wat-brt3)** 03:48 Maybe the only thing… Worth mentioning.
Is that one of… we've had This… this thing with… Briefs, people trying to commit, like, the… the briefs for every single thing in… in system, and… And, in process.
there was a PR that got merged, I don't think… The system group actually ended up approving it, but the maintainer did and merged it.
**Dmitrii Anoshin** 04:24 Uncle's that?
**Fraggle Rock (ca-wat-brt3)** 04:25 I'll find the PR. It wasn't… It wasn't enum members, so the… The briefs were… were fine.
I didn't have, like.
any specific hangups with the PR looking at it after the fact, but I thought I should bring up that one did get merged without Our group's involvement.
**Dmitrii Anoshin** 04:47 Is it collected or awesome at your conventions?
**Fraggle Rock (ca-wat-brt3)** 04:50 It was semantic conventions.
There it is.
Oh, that's some huge font.
It's not… Doesn't need to be this big.
Here we go.
So if… we have any issue with these briefs. I mean, to be fair, I don't think any of these were, like.
Enum member briefs?
Enum member briefs are the thing that really bug me, because it's really hard to… Write a detailed description for what The… the enum values mean.
But briefs for actual metrics is probably fine.
And None of the briefs seem… Wrong.
**Dmitrii Anoshin** 06:13 Yeah.
Makes sense.
**Fraggle Rock (ca-wat-brt3)** 06:16 So, I just wanted to… Bring it to people's attentions, has this been… In the front of our minds, recently.
**Dmitrii Anoshin** 06:22 Thank you. I'm not sure if percentage is the right word, that's the only thing I can think of, because we use one, so it's more like…
**Fraggle Rock (ca-wat-brt3)** 06:32 Oh, yeah, it's a… It's a fraction. One of them says fraction, one of them says percentage, so actually, yeah.
Yeah, we should clarify that. I'll… I'll submit a PR to… to clarify that.
**Dmitrii Anoshin** 06:45 Awesome, thank you.
Yeah, otherwise it looks good.
**Fraggle Rock (ca-wat-brt3)** 07:03 I've been too distracted with other stuff to do much… Of this… the stuff for this group, anyway.
**Dmitrii Anoshin** 07:12 Yeah, from my side, I've been, I'm working on entity stuff, which potentially would lead to… not potentially, but eventually would lead to… lead to modeling of the system as well, and resolving the issues that are… I'm assigned to.
So, that's pretty much it. And I'm… I've been trying to help the person who is, Moving the PR… To be able to re-aggregate metrics on the collector, and, like, I had some discussion about… I actually can post it here, so for visibility, because it's pretty much related.
Let me find it… So, yeah, this PR… This is actually… Did I put something else?
Yeah.
So, we want to… there is that, like, this optional field.
in, in metadata YAML, it means that you want to… it's possible that this… this attribute will be able, but it's not… it cannot… may not be available as well, based on some conditions, not necessarily related to the user. And also, we want to, with the aggregation, we want to introduce, like.
Field that can be enabled, disabled.
So I decided to combine them together, and made this availability field, which, like, would be a conditional, default.
or opt-in. And then, Christos came in and, said that, yeah, there is a requirement level. I was like… I looked into that, and apparently in the semantic convention.
requirement levels are, like, the bigger set of them, so we can potentially adopt them, but I was thinking that not all… not all of the levels are needed for the collector, so I decided… I went… initially went with the availability with 3 options, but apparently, in semantic conventions, there is a required level for attributes, even for Metric and span attribute.
which would say that this attribute cannot be disabled. And I, like, I had this additional semantic convention issue about that, and I was told that, hey, we need to keep that really required, and not be able to disable those kind of attributes, which is very, very little set of them, so probably we will never have anything like that on the collector. But anyway, for the completeness, I believe we… and for consistency with OpenTelemetry, semantic convention, and specification, we would just probably adopt require requirement level for the attributes in, metadata YAML, and allow all of the fields.
And based on… whether it's… Recommended, conditional, or opt-in, we would make it available for the reaggregation.
That makes sense.
Another thing I wanted to talk right now, we decided… it's, like, kind of related to that. We decided that we want… do not want to emit, CPU utilization, CPU time with the CPU attribute as a… with the CPU attribute by default. We want to make it top 10, right?
**Fraggle Rock (ca-wat-brt3)** 11:15 Right.
**Dmitrii Anoshin** 11:16 And but if we adopt And, like, we need to adopt semantic conventions anyway, and in semantic convention, that attribute is actually recommended.
So, I'm thinking we should change that. We should make a CPU attribute opt-in. What do you think?
**Fraggle Rock (ca-wat-brt3)** 11:36 Yeah, I would agree with that. I… I remember us talking about doing that. I guess it just kind of fell under the radar, but I think That is… Probably, probably right.
Because for, like, this is… for the system CPU time.
Or, sorry, this is the utilization metric, sorry, but…
**Dmitrii Anoshin** 11:58 It doesn't matter. CPU time and energy utilization will be applied.
**Fraggle Rock (ca-wat-brt3)** 12:01 Yeah, same thing, like, the default experience we want is actually for the whole system, regardless of individual cores, so…
**Dmitrii Anoshin** 12:11 Yeah, we won…
**Fraggle Rock (ca-wat-brt3)** 12:12 I can do that, too.
**Dmitrii Anoshin** 12:14 I, I, I… Like, yeah, I can do it as well, so if you have some stuff to your plate, so I'm, like, just… something that I brought, and I'll submit a PR, and if you can approve, so we can merge it. It's, like, to show that there's a consensus in our… Cool. Thank you.
**Roger Coll** 12:35 But the attribute recommendation level is per metric, or is per attribute by itself?
**Dmitrii Anoshin** 12:43 it's per attribute by itself, actually, so if we make it opt-in, it will be applied to all attributes, which… which kind of makes sense, I believe, because… Yeah, it's pretty much.
**Roger Coll** 12:56 Yeah, yeah, yeah. If there is one metric that it's… it's opt-in, yes, it should be the one. Okay, thank you.
**Fraggle Rock (ca-wat-brt3)** 13:28 not exactly a group topic, but I am curious. I'm working on… getting funding to go to KubeCon Europe.
I'm wondering if anybody in this group Is thinking of… of going to that.
**Dmitrii Anoshin** 13:43 And I would like to.
Okay, nice.
I would like to, but yeah, I won't… I don't think I can… I can do it. Because it's for US… like, residents, it's… we can do funding for US KubeCon, but it's harder. It's mostly impossible to do for Europe. Unless you have a talk, but I didn't submit anything.
**Fraggle Rock (ca-wat-brt3)** 14:10 I'm… I didn't submit anything to the main KubeCon, but I'm gonna submit something to the observability Day, and… Hopefully get, get funding for it.
**Dmitrii Anoshin** 14:18 When's the deadline for observability?
**Fraggle Rock (ca-wat-brt3)** 14:22 I think a couple… couple weeks from now, if I remember correctly.
**Roger Coll** 14:28 Yeah, I think the 30 of those.
**Dmitrii Anoshin** 14:32 Yeah.
**Roger Coll** 14:35 And for us, the same. In Europe, for Christos and I, we will probably get that funding, so… At least we expected?
**Dmitrii Anoshin** 14:46 Yeah.
**Fraggle Rock (ca-wat-brt3)** 14:48 Sunday, 2nd of November is the end of CFP.
**Dmitrii Anoshin** 14:50 Okay.
**Fraggle Rock (ca-wat-brt3)** 14:54 I'm probably going to resubmit the talk that got accepted to NA, but I didn't get funding to go.
**Dmitrii Anoshin** 15:00 Oh, really? You got dog accepted, but you didn't go?
**Fraggle Rock (ca-wat-brt3)** 15:03 Yeah, yeah, I got a… I… It's… it was, like, a weird… midpoint in, like, our policy change about applying for travel, and I screwed something up when I was applying, and so I couldn't get it approved, and I was… I submitted to CNCF, but in the end, when I realized how few folks from the collector project were going, and basically, almost nobody from this group, I think just Roger and Christos were going.
So, sorry, that's not almost nobody from this group, but, like, very few OpenTelemetry people.
We're going. I decided to just cancel the application.
**Dmitrii Anoshin** 15:40 See, what was the topic?
**Fraggle Rock (ca-wat-brt3)** 15:44 It was, I think I called the… I called the talk, How to Actually Use System CPU Utilization, How to Actually Use Utilization… CPU utilization metrics, something like that.
**Dmitrii Anoshin** 15:56 Yes.
**Fraggle Rock (ca-wat-brt3)** 15:57 Kind of an incendiary title, but… It was… it was basically going to be about the… the thing we've been… we've been fighting with about, like.
people want the utilization metric, but they don't realize it's a bad metric, and that they should use time, or things like that. So that's what the content of the talk was. I'm probably just going to resubmit that.
**Dmitrii Anoshin** 16:17 Interesting.
**Roger Coll** 16:18 Yeah, that's a great one. And it was accepted in the.
**Fraggle Rock (ca-wat-brt3)** 16:22 was…
**Roger Coll** 16:22 Yeah.
Hold on.
**Fraggle Rock (ca-wat-brt3)** 16:29 We'll do that something… I will submit one other topic, I'm not sure what yet.
**Dmitrii Anoshin** 16:50 Oof, wow.
So, I guess that's it. That's it for today.
**Fraggle Rock (ca-wat-brt3)** 16:57 Yep.
**Roger Coll** 16:58 Yep.
**Fraggle Rock (ca-wat-brt3)** 16:58 I guess if anybody wants to submit, like, a joint talk for EU, I've got one other spot open, so let me know.
**Dmitrii Anoshin** 17:04 I'm always open for that. So, let me give you some brief history.
initially, like, when I tried it myself and run it, I, like, I tried it with Bogdan, with some other people, I, like.
I did all the work, like, coming up with ideas, suggesting people, and, like, doing the discrete, and was rejected.
Both couple times, but both times I got rejected, and after that, I was like, okay, I'm not gonna do any work if someone… invites me to do a talk? I would always agree.
**Fraggle Rock (ca-wat-brt3)** 17:38 Yeah, makes sense.
**Dmitrii Anoshin** 17:39 And then, after that, a couple talks were submitted by, Christos with me, and they also got rejected, so probably I'm not the best person.
To do the giant talk. They didn't like me for service.
**Fraggle Rock (ca-wat-brt3)** 17:55 Well, if I can think of anything else, I'll let you know.
**Dmitrii Anoshin** 17:58 Okay, thank you.
Okay, cool. Thank you, folks.
**Roger Coll** 18:04 Thank you.
**Fraggle Rock (ca-wat-brt3)** 18:05 run.
**Dmitrii Anoshin** 18:05 Right.
**Pablo Baeyens** 18:06 You…
