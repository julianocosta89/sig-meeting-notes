SIG: Service and Deployment SemConv
Date: 2025-12-04
Duration: 47 minutes
Zoom Recording URL: https://zoom.us/rec/share/aLPCSNJWf9IXkZTN5-KbYwsJrivRIyscFDIXp6AnJn513S6vfoTpKpaoxBrIhr-D.Caangz6XqJlPdwlb
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 02:27 Hey, Josh.
**Josh Suereth** 02:30 Hey, how's it going?
**Trask Stalnaker** 02:33 So far, so good.
You?
**Josh Suereth** 02:39 She's had more time. Finish everything up before holidays and vacation.
I have a two-week timer here, and I, am counting down.
the vacation, but I have so much to do before then, you know?
**Trask Stalnaker** 02:53 Ugh.
**Josh Suereth** 02:54 Yeah.
It is what it is, and I'm completely distracted by Weaver v2 schema, so…
We're very, very close to having, the, like, release candidate ready.
**Trask Stalnaker** 03:11 Nice!
**Josh Suereth** 03:13 Yeah, I have to solve some of, Lyudmila's issues with, attribute refs, though. We, hmm… Anyway…
I can get into details of the shenanigans of how we model data, but it's probably not that exciting for most people.
**Janhvi** 03:34 Hey, guys.
**Trask Stalnaker** 03:36 Hey, John V.
**Janhvi** 03:37 Hello.
How do I remove the note-taker? I think that's something you mentioned last time, right?
**Trask Stalnaker** 03:49 you need access to the, a doc that has the, owner codes. I have, honestly, I've given up removing it, because it takes, like, 3 minutes every time in every meeting, and it just…
**Janhvi** 04:07 I see. Yeah.
**Trask Stalnaker** 04:09 So…
**Janhvi** 04:09 Can you share that doc with me? I'll look at it.
**Trask Stalnaker** 04:13 But you won't have access…
**Janhvi** 04:15 A lot of the access. Oh, okay.
**Trask Stalnaker** 04:18 Let me see, I think as a SIG…
Yeah, I think I can give you access, and actually, that will also give you access to update the calendar.
**Janhvi** 04:35 Okay, got it.
**Trask Stalnaker** 04:37 On your own. So yeah, let me… I'll get you the instructions, and I'll…
ping you on Slack.
**Janhvi** 04:44 Sounds good.
Thank you. Yeah, we anyways have to change the time slot for the other meeting that we have with the Asia-friendly time. I'll then do that.
**Trask Stalnaker** 04:55 Yeah.
**Janhvi** 05:03 You guys have not gone on holidays. I thought most of the US folks have gone out.
Not yet.
**Josh Suereth** 05:10 We're just back from holidays, actually.
**Janhvi** 05:12 Oh, I see.
**Josh Suereth** 05:18 I was just commenting how I have, so much to get done before… I'm taking a long holiday over Christmas, and so I'm leaving about, leaving mid-December.
And so I have, I think, 2 weeks to get everything done, and I keep seeing that time getting closer, with not a lot getting done, you know?
**Janhvi** 05:38 Yep, yep.
So, during that time, I think after 15 December or so, I'm assuming most of the folks are going to be out, right? Should we then skip the sick meeting during those two weeks, the last two weeks of December?
**Josh Suereth** 05:52 Give your address.
**Trask Stalnaker** 05:54 Yeah, we… Can't… we already canceled… OpenTelemetry takes a two-week holiday.
And so we already canceled all the meetings, for those last two
weeks. So the 25th and the 1st.
Are both canceled for this meeting.
**Janhvi** 06:17 Do the same thing here.
**Trask Stalnaker** 06:21 Yeah, yeah, they're already canceled, so, we just need to not show up to those.
But we can choose to,
you know, take the 18th off, for example, if folks are gonna be out. Sounds like, Josh, you're gonna be out, that week.
**Josh Suereth** 06:45 Yeah, so I'm trying to figure out how to do the, claim host thing.
**Trask Stalnaker** 06:51 Sorry.
**Josh Suereth** 06:52 Do you know what, what,
Do you know what? How do I find out what account ID this one's made with, by the way?
**Trask Stalnaker** 06:58 Yeah. Oh, you go to the… click on the meeting security, shield icon at the top of the meeting.
And… why does it… it used to…
**Josh Suereth** 07:12 There's a shield at the top of it?
Oh, I see, got it.
**Trask Stalnaker** 07:20 It says host open telemetry.
Okay, so the other way is to go to the calendar, And, open the calendar.
**Josh Suereth** 07:33 Introduce.
Okay.
**Trask Stalnaker** 07:35 It's number 4.
**Josh Suereth** 07:39 Okay, alright, I can… I'll claim ownership of the meeting temporarily and do all this. Okay.
Yeah, I got it. Sorry.
Sorry for the distraction.
**Janhvi** 07:50 No worries.
Should we get started? I'm not sure if anyone else is going to join.
**Trask Stalnaker** 07:59 Yeah.
**Janhvi** 08:01 You guys can see my screen, right?
**Trask Stalnaker** 08:05 Yes.
**Janhvi** 08:06 Okay.
Cool, I've added the agenda, feel free to modify slash add if you have more things to discuss.
First, I've added the criticality PR, which we had discussed last time. I see there's a demo that's already attached to the PR.
And I think there are some approvals on the PR, but I wanted to check how do we move forward with this one.
I'll quickly open it.
Yeah, I think Josh has already approved.
Trask, if you have some time, can you also take a look at this one? There's a demo attached, at the end.
**Trask Stalnaker** 09:05 Yeah, yeah, and also, I mean, your approval is meaningful.
Even though.
**Janhvi** 09:12 So it's.
**Trask Stalnaker** 09:13 green…
**Janhvi** 09:14 Yeah, I'll take a look.
I think one more thing that we tried to do, and Ayushi's also here from my team, I think last time we discussed, right, we wanted to see how is criticality used in other observability, places, Kubernetes or stuff like that. Ayushi, do you quickly want to go through the doc that you have, where you found, how is criticality and similar attributes being used?
**Ayushi Asthana** 09:41 Yeah, sure, I think, so…
**Janhvi** 09:46 I'll just quickly.
**Ayushi Asthana** 09:47 Yeah, yeah, after I went through the PR that, Josh had shared, I kind of…
stopped working towards a demo, because, I'm assuming this is already under the works, and this will get approved in the next 1-2 weeks at max, right? So…
Yeah.
**Trask Stalnaker** 10:08 The… the PR?
**Janhvi** 10:11 Yeah, yeah, the PR.
**Trask Stalnaker** 10:13 I mean, I think that the understanding how this interplays with existing systems will help the PR to get merged.
**Ayushi Asthana** 10:24 Okay.
So if you go to the observability section, it's at the bottom. So right now, so this is, like, sort of an analysis of how, the cloud providers are exposing criticality as an attribute right now.
And then some analysis of, what different observability platforms are doing with that criticality, attribute.
So, there is some analysis of how Datadog processes criticality. For example, they have, special, filtering on dashboards by criticality, so we can probably create, like, a small demo with observability.
like, plugging in, maybe, like, a Kubernetes, cluster, and generating some metrics, and plugging it into Datadog or Splunk.
**Trask Stalnaker** 11:18 So, I don't… I don't think you need to…
Do go that far as actually
implement, you know, show it in Datadog, but if you can add links to their documentation, is what would be helpful.
**Ayushi Asthana** 11:36 Okay.
**Janhvi** 11:38 Even links to how Grafana Radiadog, uses these, attributes, right?
**Trask Stalnaker** 11:44 Yeah, yeah, links to their documentation about these is what would be helpful.
**Ayushi Asthana** 11:50 Okay.
**Janhvi** 11:52 Got it.
**Ayushi Asthana** 11:53 I can do that. Let me just take a note on this.
**Janhvi** 12:00 Yeah, and I think other than that, I usually also saw that, even in cloud, all the other clouds are also using it, maybe in different formats. There are attributes like this, right? You want to talk about that?
**Ayushi Asthana** 12:13 Yeah, so right now, I think… so, in Kubernetes, there is a couple of different ways that this plays out.
You can go to Kubernetes, right? It has different ways that it exposes criticality, in terms of scheduling and storage classification, but these more or less have, like, the same meaning as criticality, they are named differently.
Similar to, I think AWS, how AWS does it and how GCP does it, they both have, criticality in security use cases, as well as, like, user tagging.
So, for these as well, I think the same thing goes, that we might… it might be helpful to attach, some doc links
And, I think forums where these things are discussed.
Oh… Janvi, can I share my screen? It'd be helpful.
**Janhvi** 13:15 Joshua, go ahead.
**Ayushi Asthana** 13:22 Do I have access to shares?
Yep.
Okay.
So, in GCP, right now, criticality is mostly relevant in AppHub, which is in development, I think.
And in Security Command Center, where criticality is, like, explicitly exposed, and the naming is also similar to, I think, what we are proposing, critical, high, medium, low.
For AWS, this use case is similar. Security Hub exposes criticality as an attribute for their findings, and this is, like, both system-generated and user-defined.
So Alibaba has one, like, new use case that I saw where they also allow classification of backups according to criticality.
And they allow users to tag their backups as critical, important, or general, which has the same semantics.
In K8, it's mostly, it's around scheduling, so users can classify their workloads as critical.
There is some classification semantics for storage and volume provisioning.
Where, again, this… the…
