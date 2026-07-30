SIG: Developer Experience SIG Meeting
Date: 2026-07-29
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 00:24 Okay, Johanna.
**Juliano Costa | Datadog** 00:29 Hello, hello!
**Johanna Öjeling** 00:30 How's it going?
**Juliano Costa | Datadog** 00:34 Good, good. Yeah, finally the demo is out, so…
**Johanna Öjeling** 00:37 Yeah, congrats, but… Thank you most, though.
**Juliano Costa | Datadog** 00:44 Yeah, and that, Ian, that really took a while. Yeah.
**Johanna Öjeling** 00:50 Yeah.
**Juliano Costa | Datadog** 00:51 I don't know if anyone will actually join this meeting.
**Johanna Öjeling** 00:58 this one.
**Juliano Costa | Datadog** 00:58 wondering if… maybe… We should switch to… to a private meeting and discuss the talk, so we use this time.
**Johanna Öjeling** 01:12 So it's like a plan.
**Juliano Costa | Datadog** 01:13 Where's go.
Yeah. Okay.
**Johanna Öjeling** 01:16 And, I also, when I joined this meeting, now I realize also that the Zoom meeting URL change went through.
And I need to update my… you mentioned it, like, last week or two weeks ago, but the URL in the meeting docs Has been updated.
That's how I got into this room.
**Juliano Costa | Datadog** 01:39 Wait, but this is… this is actually not the new one yet.
**Johanna Öjeling** 01:45 Okay!
**Juliano Costa | Datadog** 01:46 That's weird.
I want…
**Johanna Öjeling** 01:48 I clicked the event in my calendar, and then, when I joined the meeting, it just said, like, the host has ended this meeting.
**Juliano Costa | Datadog** 02:00 Bye.
**Johanna Öjeling** 02:01 Or… Okay. And then I went to the meeting docs.
I just… maybe it's… yeah, I don't know, maybe it's actually the same URL, I don't know.
**Juliano Costa | Datadog** 02:12 Well, I was.
**Johanna Öjeling** 02:13 Okay.
**Juliano Costa | Datadog** 02:14 I was in this meeting, and nobody showed up, so I said, oh, maybe we updated the link, so I left.
**Johanna Öjeling** 02:21 Aha, okay.
**Juliano Costa | Datadog** 02:23 Mose the call, I don't know.
**Johanna Öjeling** 02:24 Okay, yeah.
Yeah, that could be the case.
**Juliano Costa | Datadog** 02:31 But, just so you know, the link's still not updated, so we are currently using Zoom.us.
And the new link will be… Zoom-lffx.platform Something Linux?
**Johanna Öjeling** 02:49 Okay.
**Juliano Costa | Datadog** 02:50 So the URL will change.
**Johanna Öjeling** 02:52 -
**Juliano Costa | Datadog** 02:53 hopefully… someone… hopefully someone from GC, We'll do this change, and then, send a message to us.
At least on the channel, saying, hey, we updated the link.
**Johanna Öjeling** 03:14 Hey, Pirate.
**Juliano Costa | Datadog** 03:15 So hello, Perk.
**Perk (Marcin Stożek) | Elastic Ingest** 03:16 Do you know when this will happen?
**Juliano Costa | Datadog** 03:18 I think they had, like, 2 weeks to do it. It should happen by the end of this week, but yeah, I don't know. Let me just check on the community repo… who is our liaison? I think it's Austin, if I'm not mistaken?
**Perk (Marcin Stożek) | Elastic Ingest** 03:46 Okay.
So, I'm going for a vacation for two weeks, so, after that… Yeah, look it up.
**Juliano Costa | Datadog** 03:54 If I'm not… Perk (Marcin Stożek) | Elastic Ingest 03:55 here in two weeks, you know, I'm looking for the Zoom link.
**Juliano Costa | Datadog** 04:00 We'll post on the… on the channel.
**Perk (Marcin Stożek) | Elastic Ingest** 04:03 Thanks.
**Juliano Costa | Datadog** 04:07 Developer Experience… I don't know who is our… liaison.
One second… Yeah, I was thinking.
**Perk (Marcin Stożek) | Elastic Ingest** 04:21 It'll be Severin? Austin. Oh, okay. Austin.
**Juliano Costa | Datadog** 04:25 So whenever he does it, We will know.
**Perk (Marcin Stożek) | Elastic Ingest** 04:30 Very well. Hopefully.
**Juliano Costa | Datadog** 04:32 Yep.
**Perk (Marcin Stożek) | Elastic Ingest** 04:39 I don't think…
**Juliano Costa | Datadog** 04:40 Go ahead.
**Perk (Marcin Stożek) | Elastic Ingest** 04:41 Oh, sorry, yeah, I just have one thing. I'll just add it to our agenda, because I read all the comments, I will add the snippet, I will ask Martin… and Alexander directly about the, like, a diagram, maybe they have one. Juliano, you, you proposed a paragraph or two there at the very beginning, somewhere.
I'm not sure I… Yeah, it's exactly what is there that you missed, so if you could suggest something…
**Juliano Costa | Datadog** 05:09 I actually replied there, The first time I read, I felt that it was missing a connection between the intro and the why they chose the Gradle. Not the Gradle, the… Quarko's approach.
**But then I suggested a paragraph, and Alex… didn't like, so he suggested modifications on the suggestion, so that we agreed on the new intro paragraph. So, I don't know if you saw, but the new… Perk (Marcin Stożek) | Elastic Ingest** 05:44 Is there, yeah.
**Juliano Costa | Datadog** 05:45 So, so the new first paragraph from the second section is different from… Perk (Marcin Stożek) | Elastic Ingest 05:50 Yes.
**Juliano Costa | Datadog** 05:51 From the initial one. So I think… I'm good with that.
**Perk (Marcin Stożek) | Elastic Ingest** 05:56 Okay, okay, okay, okay, because I only read it, the new version your comment, and then it's like, hmm, I read it, like, this looks okay.
**Juliano Costa | Datadog** 06:04 Yeah, I… I forgot to resolve it.
**Perk (Marcin Stożek) | Elastic Ingest** 06:07 No worries. Okay, okay, okay, okay. Good point. Okay, okay, okay. So, yeah, so I think it should be done, like, pretty soon, with this, except for the, maybe for the, diagram. Depends on guide, on, on the availability.
And then, other than that, I'm good on my end. So, I'll just do it, I'll ping you on the Slack, and then… because I'm off, I'm not sure how much I'll be able to, like, do anything in here, but, like, feel free to do anything.
Going forward.
**Juliano Costa | Datadog** 06:40 Give me one second, I think… aren't we good to go, actually?
On that.
**We have… Perk (Marcin Stożek) | Elastic Ingest** 06:55 Johanna suggested to add the snippet, so I'll add it, I'll add it very quick, you know?
And then maybe a diagram.
**Juliano Costa | Datadog** 07:04 Yeah, no, we… we are missing input from… from… from that, actually, so… Perk (Marcin Stożek) | Elastic Ingest 07:10 Okay.
**Juliano Costa | Datadog** 07:12 Yeah, there is no way to move on without it. Like… I think, a Jaeger trace shouldn't be difficult with, Claude.
key clothes.
**Perk (Marcin Stożek) | Elastic Ingest** 07:27 Oh, yes, yes. Yeah, yeah, yeah, correct.
**Juliano Costa | Datadog** 07:29 Like, if that was the only missing part, I could try to get one in.
And we would be ready to go.
But I think a diagram would be cool, and that's more on their end, right?
**Perk (Marcin Stożek) | Elastic Ingest** 07:44 A little bit, yeah, I'll look it up on the website. Maybe it is somewhere there, maybe somewhere on GitHub, I don't know, Because I assume if there is not there, then it isn't anywhere, you know, so I guess it's the same work, maybe they… maybe they know. But I can look it up. I'll spend, you know, like, 15 minutes looking it up.
Yeah. And then I'll ping ya. I should be able to do it today. I think I have some time for that today, so… Oh, thank you, guys.
And the other topic I wanted to say is that, I confirmed I'll be there in Prague, so I'll meet you there.
**Juliano Costa | Datadog** 08:21 Awesome.
**Johanna Öjeling** 08:21 News.
**Perk (Marcin Stożek) | Elastic Ingest** 08:23 Very well.
And congrats again, your, on your speaking.
**Johanna Öjeling** 08:28 Thank you.
**Perk (Marcin Stożek) | Elastic Ingest** 08:29 I'm going to attend your session, you know that.
**Juliano Costa | Datadog** 08:32 Yay.
**Johanna Öjeling** 08:32 Yeah, I thought there are two parallel trucks, so yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 08:35 Yes, yes.
**Juliano Costa | Datadog** 08:39 Keep on… I have one thing to talk about the key clock. Is that.
How it writes, yes.
So… the Opentelemptree.io Repo now requires, an issue for the blog.
So I created an issue, I tagged you both there, I don't know if you saw.
And severing, he came to the thread and said, hey, this is great, do you have anyone from Key Cloud side?
**Perk (Marcin Stożek) | Elastic Ingest** 09:19 to…
**Juliano Costa | Datadog** 09:20 And I said, yes, we have Martin and Alex. And he was like, hey, that would be cool to post on their blog as well, but also maybe try to race to CNCF and post on the CNCF blog, because this is kind of a cross… Cross-project thing.
Honestly speaking, I don't know which blog post has more visibility.
But, like, the CNCF blog sounds… Vince here?
**Perk (Marcin Stożek) | Elastic Ingest** 09:57 A little bit, maybe?
**Juliano Costa | Datadog** 09:58 I never posted there, so maybe we should… try to get in? I don't know. I can check. I'm a CNCF ambassador, I have a channel with the CNCF folks, I can ask.
**Perk (Marcin Stożek) | Elastic Ingest** 10:14 Well, definitely. Yeah, yeah, that sounds like a great idea. I mean, and, you know, like, to your point, it is about two CNCF projects.
Then we can… maybe, I don't know, like, do a follow-up, maybe more like a dive-in from the OpenTelemetry side, or maybe from the Quick Cloud? I can feel there's a couple more things we could do in here as well.
**Juliano Costa | Datadog** 10:37 Yeah, there is one thing, though, like… I know that for our… for… yeah, for our companies, it's good to have a blog post on the OpenTelemetry, so, like, whenever we publish something, it is, like, Perk from Elastic, Juliano from Datadog.
Johanna from now IKEA, but, like.
**Johanna Öjeling** 11:01 Yeah.
**Juliano Costa | Datadog** 11:02 It was Rafana,
**Johanna Öjeling** 11:03 Yeah, exactly.
**Juliano Costa | Datadog** 11:04 For the vendors to be there.
**Johanna Öjeling** 11:06 Meeting the word.
**Juliano Costa | Datadog** 11:07 All that stuff. On the CNCF blog, we also have that mentioned, so, as authors.
But I don't know how interesting for our companies this is.
So that's the only thing that we need to discuss and agree, because if we say, no, no, let's go for the open telemetry.io, I'll just push back on Severi and say, no, can we make it here? And then we end there. But if everyone is interested to try to raise to the CNCF blog, then I can ask around and see how that works.
**Johanna Öjeling** 11:42 I think, one, potential solution could also be… like, I think it's a good idea to publish on the CNCF blog, because it concerns two projects, but then, this, I assume, like, this will also become an OTL reference implementation, like the other Skyscanner and so on, so maybe if the, communication SIG is fine with it. We could also, like, create a blog post on the OTAL blog saying, like, oh, there is, like, a new reference implementation about Keyclode, or, like, mentioning that there is… maybe just, like, a short, introducing the topic and referring to the CSF blog post or to the hotel reference implementation.
**Perk (Marcin Stożek) | Elastic Ingest** 12:34 So which one… which one, Johanna, you propose to go with? Like, publish on the OpenTelemetry, and then… reference from the CNCF, or go the other way around. Publish on the CNCF, and then reference from the auto…
**Johanna Öjeling** 12:48 Yeah, the other way around, like, to… as Juliano mentioned, it's, like, important for the vendors to be, you know, visible, on the hotel, website. Then, if we decide to publish on the CNCF blog.
**we could still, like, highlight it some way on the OTAL blog, or or it… yeah, since it will likely also become an OTAL reference implementation, and there the… Perk (Marcin Stożek) | Elastic Ingest** 13:16 Yeah, exactly. Yeah, yeah, I agree with you. And also, it works the other way around, meaning that it works for Martin and Alex, because I'm pretty sure they have exactly the same thing, but on the key clock.
blog post.
**Johanna Öjeling** 13:30 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 13:31 So if we could reference somehow, you know, with a shorter version, or whatever, I think that would work very well.
**Johanna Öjeling** 13:39 -
**Juliano Costa | Datadog** 13:41 Yeah, I… I know they did something like that for the… graduation.
The graduation was announced on the CNCF blog, and then they released, kind of a smaller version.
On the hotel block.
I don't know how that would work, but we can try. I think we need… I think what we need to do is decide on our end first, and then we just try to go for it.
**Perk (Marcin Stożek) | Elastic Ingest** 14:14 Yeah, fair, fair, fair, fair. Yeah, so I agree with Johanna here.
And with you, Juliano, as well, but this course of action, going with the CNCF and then having a smaller version.
on OpenTelemetry, referencing the CNCF1, I think that would be even better, you know, from Elastic point of view, for example, of my employer, and probably yours as well, guys, because it's, yeah, like you said, like, more fancy.
A little bit.
So that… that… like, for my end, that is, you know.
Two birds with one stone, really.
**Juliano Costa | Datadog** 14:50 Cool. Cool, cool. Okay.
Okay, so I will add an action item to myself here.
**Perk (Marcin Stożek) | Elastic Ingest** 15:02 Thank you.
**Juliano Costa | Datadog** 15:12 dokie. And then I'll… I'll let you both know Either via the issue, or on Slack, or somewhere, or it's mobile.
**Perk (Marcin Stożek) | Elastic Ingest** 15:23 Awesome, awesome.
**Juliano Costa | Datadog** 15:24 Or a pigeon, or… Perk (Marcin Stożek) | Elastic Ingest 15:26 Yep.
That works.
**Juliano Costa | Datadog** 15:30 Whatever. Cool.
**Perk (Marcin Stożek) | Elastic Ingest** 15:32 So then, what's the next project we should reach out to?
Using OpenTelemetry.
**Juliano Costa | Datadog** 15:37 I don't know if there is already, a blog on open feature. I know that they are, using… I know because they, we have open feature on the hotel demo, and it's, It's… well, speaking hotel.
**You know, official Semitic conventions, I have contacts in there as well, so… Perk (Marcin Stożek) | Elastic Ingest** 16:01 Okay.
**Juliano Costa | Datadog** 16:01 We could try that.
Oh, definitely.
**Perk (Marcin Stożek) | Elastic Ingest** 16:05 then Kubernetes.
**Juliano Costa | Datadog** 16:07 Thus… yeah, but the problem is that Kubernetes uses Prometheus.
**Perk (Marcin Stożek) | Elastic Ingest** 16:14 Well, okay, but don't they do tracing at all?
Anywhere, you know, I would go for anyone that does OpenTelemetry anywhere in Kubernetes, so that we can get our foot in the door.
**Juliano Costa | Datadog** 16:27 I think… Some years ago, there was a project that converted, kubernetes events into traces.
And I think that was integrated into the Kubernetes project. I don't know what is the state of that, because I've been away from the Kubernetes community for some time.
But maybe we could, investigate. I think there is tracing for Kubernetes.
I'm just not sure how many folks actually use it.
**Perk (Marcin Stożek) | Elastic Ingest** 17:04 Okay.
Okay Yeah, fair enough, fair enough. So, some investigation would need to be done there.
Then, maybe they will be somewhere around for the Observability Day, or KubeCon, or whatever. You know what is the other project that we could try?
the collector.
Does it have tracing?
**Juliano Costa | Datadog** 17:24 Oh… Perk (Marcin Stożek) | Elastic Ingest 17:25 Much.
**Juliano Costa | Datadog** 17:26 the collector, and it's also tricky. I think they do have tracing now, I think… I think metrics, they are still switching from Prometheus to… to… Perk (Marcin Stożek) | Elastic Ingest 17:41 Okay.
**Juliano Costa | Datadog** 17:42 To hotel, which is funny, because, right?
Hello!
**Perk (Marcin Stożek) | Elastic Ingest** 17:46 come on! Well, it was not ready, so I think that that's fair. So maybe when they are done, then we'll do our blog post.
**Juliano Costa | Datadog** 17:54 Yup.
**I can… I can ping Pablo, he's a maintainer on the… On the collector end, Perk (Marcin Stożek) | Elastic Ingest** 18:05 Yeah, very well. Or maybe, maybe.
**Juliano Costa | Datadog** 18:07 the bar.
**Perk (Marcin Stożek) | Elastic Ingest** 18:10 they do it already. Maybe they plan to do it already anyway. Maybe they need help, or just, you know, do it by themselves. I think it's a good thing to reach out.
**Juliano Costa | Datadog** 18:19 Yeah, to be… to be honest, I don't think the collector Story would be too exciting, because it's hotel and hotel.
**Perk (Marcin Stożek) | Elastic Ingest** 18:30 Yeah, yeah. It's only funny from the organization.
**Juliano Costa | Datadog** 18:33 Now we're gonna show how Oltael uses OLTEL.
**Perk (Marcin Stożek) | Elastic Ingest** 18:36 Yeah, eventually, isn't that great?
Yeah.
**Juliano Costa | Datadog** 18:42 But if we can, You know who uses OTEL? Envoy?
**Perk (Marcin Stożek) | Elastic Ingest** 18:49 Oh.
Okay.
**Juliano Costa | Datadog** 18:51 We also have that on the demo, getting someone from Envoy into… That will be cool. Does anyone know anyone in the Envoy community?
**Perk (Marcin Stożek) | Elastic Ingest** 19:03 Not yet.
So you said Envoy, open feature… And, some… maybe some folks from Kubernetes.
Open feature… Okay.
Yeah, so I'm not sure yet. It's just a, you know, exploratory phase in my head. That was… that was pure luck that I spoke with Alex there, you know, in February.
But I guess that's a very… that's a very credible source of, you know, like, information for everybody about the adoption of auto, you know? Like, I feel that that's the job to do.
That's a good job to do.
**Juliano Costa | Datadog** 19:58 On Envoy, I know the… the guy that… So… Envoy had one implementation for OTEL, And it was kind of, it wasn't following the spec, it was kind of a workaround to produce hotel data. I know the guy that fixed that, and made it kind of hotel… The proper way.
But he's just a contributor, he's not a maintainer or anyone from the Envoy community. It would be nice to have someone from the project side.
And maybe him as well, so we do, like, Interview with them and go through, like, the… the idea, what maintainers thought, and, like, the challenges that was… that was… That they faced when they were, adopting.
**Perk (Marcin Stożek) | Elastic Ingest** 21:02 why they wrote the, like, their own implementation first, and then, like, switched. Yeah, yeah, definitely, definitely. So, the… Do you know that person? Can you… can you reach out?
**Juliano Costa | Datadog** 21:13 I know the person, but I don't know any… anyone from the Envoy community. Maybe, maybe he knows, so I'll pick him and see.
**Perk (Marcin Stożek) | Elastic Ingest** 21:23 Okay, okay.
**Juliano Costa | Datadog** 21:25 Too much to do for me, I… Perk (Marcin Stożek) | Elastic Ingest 21:29 Yes.
**Juliano Costa | Datadog** 21:29 I, I, I, I don't want, I, I, I don't want it anymore.
**Perk (Marcin Stożek) | Elastic Ingest** 21:34 Fair enough.
Initially…
**Juliano Costa | Datadog** 22:12 Did you do? Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 22:16 Yeah.
Okay, okay, okay. So, I will do that exploratory phase. I'll keep that in mind whenever I am somewhere. Maybe, maybe someone will be there on the observability day there in Prague.
Maybe we should wear a t-shirt. You use Ottawa? Talk to me.
But not as a vendor, because then nobody will talk to us.
**Juliano Costa | Datadog** 22:46 Well, hopefully on the Observability Summit, everyone will use ULTAL.
**Perk (Marcin Stożek) | Elastic Ingest** 22:50 So that's a… that's a very good point, yeah, so then they should wear their own t-shirts, and we should just pick, okay, we want this and this.
Okay.
Yeah.
**Johanna Öjeling** 23:00 I wonder how many attendees there will be.
**Juliano Costa | Datadog** 23:05 Me too, and I know that it's the first time that they are doing it in Europe.
This year, they… they didn't have much folks, but it was on, wow.
**Perk (Marcin Stożek) | Elastic Ingest** 23:21 In May, in Minneapolis?
**Juliano Costa | Datadog** 23:22 Yeah, in Minneapolis, where the whole ice thing was a mess.
during the CFP, So, during the CFP, nobody wanted to submit because ICE was striking there, so…
**Johanna Öjeling** 23:36 Wow.
**Juliano Costa | Datadog** 23:37 I don't know how many folks actually decided to not go because of, the, the location itself.
**Johanna Öjeling** 23:45 Mmm, okay, Perk (Marcin Stożek) | Elastic Ingest 23:46 Yeah, it was 100. Definitely.
**Juliano Costa | Datadog** 23:48 But it is a good event, because everyone that is there is focused on observability, so you're kind of… Meet the peers, so…
**Johanna Öjeling** 23:57 - Perk (Marcin Stożek) | Elastic Ingest 23:58 Yeah. Also, Agenta looks strong, so… Let's keep our fingers crossed.
I know I'm coming. I'll take Andre stands over me.
The auto collector maintainer.
**Johanna Öjeling** 24:13 Yeah, it will be great to meet in person.
**Perk (Marcin Stożek) | Elastic Ingest** 24:17 Definitely.
**Juliano Costa | Datadog** 24:18 Cool. Cool.
Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 24:22 I don't have any other topics, guys.
**Juliano Costa | Datadog** 24:24 Yeah, me neither.
**Perk (Marcin Stożek) | Elastic Ingest** 24:25 Just a way.
**Juliano Costa | Datadog** 24:27 You, Johanna? Do you have…
**Johanna Öjeling** 24:28 No, I don't have any topics, so I think we can close there. Juliano, do you still have time to chat separately about the talk? Yeah, then we can create another meet or a Slack huddle.
**Perk (Marcin Stożek) | Elastic Ingest** 24:43 Oh, Russell, I'll just leave you here.
**Juliano Costa | Datadog** 24:45 No, this one is actually recorded.
**Perk (Marcin Stożek) | Elastic Ingest** 24:48 Yeah, okay, fair enough.
**Johanna Öjeling** 24:49 Of course.
**Perk (Marcin Stożek) | Elastic Ingest** 24:50 Yeah, yeah, yeah, yeah, yeah, you're right, you're right.
And you… the recorded version, you want the recorded version to be from the conference, not from before the conference?
**Johanna Öjeling** 25:01 That's fair, that's fair.
**Perk (Marcin Stożek) | Elastic Ingest** 25:02 Okay, okay. Have fun, guys. Good to see ya.
**Johanna Öjeling** 25:06 Thank you.
**Juliano Costa | Datadog** 25:08 Enjoy your, holidays.
**Perk (Marcin Stożek) | Elastic Ingest** 25:09 Thank you.
**Johanna Öjeling** 25:10 Thank you.
**Perk (Marcin Stożek) | Elastic Ingest** 25:11 Thank you. I'll see you after. Thanks, bye.
