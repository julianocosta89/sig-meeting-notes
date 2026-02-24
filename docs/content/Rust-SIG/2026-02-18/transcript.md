SIG: Rust SIG
Date: 2026-02-18
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/5E8qtDN6Zj4t4Ecxr8F63kNrs9cfc5C0st7-m92LN9ja-5EwZTgWF5Ah7kNhWU2o.50jjbQcZX__EJ0f6
============================================================

## Zoom Recording Transcript

**Alex** 00:17 Hello!
**Yadi Abdalhalim** 00:19 Alright. Hey, hey, how's it going there?
**Alex** 00:22 Doing alright, pleasure to meet you, Yadi, is that right?
**Yadi Abdalhalim** 00:25 Yeah, yeah, yeah, yachting, yeah.
**Alex** 00:27 Got it. I'm Alex, so, pleasure to meet you. I'm obviously new to the hotel community, but I thought I'd jump onto one of these, SIG meetings.
**Yadi Abdalhalim** 00:35 Well, I'm also new too, so I get excited about this one as well, so hoping to meet others.
**Alex** 00:41 Nice.
Yeah, me and, Brett, who just joined, are from a company called Elastiflow, so,
No, I would not recognize familiar faces from old, because I'm new here, so…
**Yadi Abdalhalim** 00:54 Hell yeah.
And I'm from a startup called MUX, and we do video processing, so…
**Alex** 01:02 Oh, nice. Mux, you said?
**Yadi Abdalhalim** 01:03 earmarks, yeah.
**Alex** 01:04 Nice.
**Franco Posa** 01:18 If everyone else was gone, I hopped on a little late here. I'm Franco, I'm from Grafana.
I've just mostly got involved through, like, donated, like, a metrics…
middleware, to the contribib library, and I've been sort of hanging around, helping out ever since.
**Alex** 01:38 Nice.
**Franco Posa** 03:25 Sorry, do we have any, like, agenda items or, things that people are looking to discuss?
**Brett Mitchell** 03:36 Well, from…
Elastiflow's perspective, we have sort of a general discussion topic, nothing that's specific to, like, an issue or a PR that's open in the repo right now.
So if there's anything else to take care of, we should probably go through That stuff first.
Oh.
**Franco Posa** 03:56 I don't think there's anything on the menu, so go ahead.
**Brett Mitchell** 03:59 All right. Yeah, so we're exploring the concept of a no-tel collector written in Rust.
We were pointed in the direction of the OTEL Dataflow project in the OTEL Arrow repository, and we're going to be coordinating with that group, but we're also interested in the Rust SDK's position on the Rust collector landscape.
So we're kind of wondering, like, what level of coordination and support has been discussed or put in place between the Rust SDK and the Otel Arrow project?
And there might be another point of contact that I could go pursue to find out the answer to that question.
**Franco Posa** 04:41 Yeah, I don't know if we have any, like, of the more experienced, like, higher level maintainers of the Rust.
repos on this call. I usually interface with CJO, who's listed here in some of these notes,
And… Actually, Bjorn might have some more context. He's been around a lot longer than I have, I think.
But, yeah, the Slack might be the place to start.
**Brett Mitchell** 05:09 Yeah.
Okay. Well, I mean, I can move the, conversation over there, if you think that would work better.
Bjorn, I don't know if you have, topics that you wanted to go into, but we were just, talking about kind of a general question that Elastiflow has.
Basically, we're trying to figure out
We're interested in, investigating the concept of a collector written in Rust.
We were pointed towards the hotel Aero project, with the Hotel Dataflow
Rust sub-project, and we're kinda… we're trying to figure out what is the relationship between the Rust SDK and the Arrow group.
**Björn Antonsson** 05:56 I'm most definitely not the right person to ask. I've been contributing to the tracing side, I have really no idea about the history of the project, and yeah.
Gotcha. So, yeah.
**Brett Mitchell** 06:12 Well, I think what Franco suggested is a good idea. I'll move the conversation over to the Slack in the CNCF space.
**Björn Antonsson** 06:19 Boop.
**Brett Mitchell** 06:21 Awesome. Thanks.
**Franco Posa** 07:49 Is that all we've got. I'll just mark down everyone's names here. I think I missed everyone's, you know, company association at the beginning. Brett, I assume you're with Elastiflo.
Yachty, and Alex.
**Yadi Abdalhalim** 08:07 My name's Yanni, I work at MUX, software… software engineer on a data platform, so we use OpenTelemetry pretty extensively.
**Franco Posa** 08:21 And… Alex?
**Brett Mitchell** 08:27 I don't know if you can get to the microphone.
**Alex** 08:28 Alright, I had to step out for a call. Just got done.
Alex Bird, a, engineering manager at Elastiflow. So don't know if Bird introduced himself yet, but Elastiflow, dealing with, like, network observability and going into hotel space now.
**Franco Posa** 08:46 Awesome. Well, I don't think…
We have any more agenda items. I don't normally lead these things, but I guess I've just been going at least as long as anyone else here, so,
Yeah, we'll see you in the Rust Hotel Slack, I assume. And nice meeting you all.
**Brett Mitchell** 09:05 Sounds good. Thanks, all.
**Franco Posa** 09:07 Right, cheers.
