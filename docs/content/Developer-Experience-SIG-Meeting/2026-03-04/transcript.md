SIG: Developer Experience SIG Meeting
Date: 2026-03-04
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:12 Hello there.
**Alexander Schwartz (IBM)** 01:16 Adriano, not a book.
**Perk (Marcin Stożek) | Elastic Ingest** 01:22 Hey, folks!
**Juliano Costa | Datadog** 01:24 Good to see you. Hey, Prick.
**Perk (Marcin Stożek) | Elastic Ingest** 01:27 Hey, Alexandra, thanks for joining.
**Juliano Costa | Datadog** 01:29 Great to see you.
**Perk (Marcin Stożek) | Elastic Ingest** 01:38 You know?
**Juliano Costa | Datadog** 01:39 Oh, boy.
**Perk (Marcin Stożek) | Elastic Ingest** 01:39 tricks you down.
Last week, we had a meeting, and I remember, hey, I talked to you. How do I find you? And I was going through the Fosden website, found you on a picture.
**Alexander Schwartz (IBM)** 01:53 Very good, you know.
Nice.
Go ahead.
**Juliano Costa | Datadog** 02:04 Alexander, let me ask you one thing.
Do you want to… run, this interview now.
Or do we want to talk a little bit about it, and then we schedule another day to do?
**Alexander Schwartz (IBM)** 02:22 We can… We can schedule another thing for that, so maybe we talk about, what you're expecting? Is it, like, a written interview, a recorded interview, That kind of things. And maybe, maybe you have some list of questions that I can prepare for.
**Juliano Costa | Datadog** 02:40 So, yeah, let me… yeah, go ahead, go ahead, sorry.
**Alexander Schwartz (IBM)** 02:45 Last time, somebody was trying to do an interview, and then later a write-up of what I said. It ended up with a mess.
Because maybe I was not talking… Whoa.
**Perk (Marcin Stożek) | Elastic Ingest** 02:55 Oops.
**Alexander Schwartz (IBM)** 02:56 write-down quality, in a way. So… yeah, when you're looking for something written down, We can use this meeting to agree what you're interested in, and maybe go through the questions and come up with some candidates.
And I provide the… a write-up of that, afterwards. But maybe you're looking for something different, and then you can explain to me what you're looking for.
**Juliano Costa | Datadog** 03:21 One second, let me just add this to the… to the meeting notes, so we have, registry to others to follow.
Just discussing about the interview process.
Cool, let me… Quickly share my screen here.
And I can actually also share this doc with you.
This is our… SIG meetings, doc, and what do we have here on the left In one of the tabs is the blog post hotline.
So, basically, this is what we are looking when we are… we are looking for when we are interviewing the companies. In your case, it's a bit different, because in your case, we are interested in how the project is using hotel.
**Alexander Schwartz (IBM)** 04:23 Right.
**Juliano Costa | Datadog** 04:23 So, we wouldn't have, like, a company structure and a diagram of the how the collectors are deployed, unless you have collectors deployed, but anyways, I don't think that's the case. But we would focus on… The adoption… of… Like, how… how you guys at Key Cloth are using OTEL.
to provide observability, into key clothes, or something like that. And then we… we can… maybe… Maybe we can even… Create a different, outline for the blog here, where we explore this project.
Side of the… of the things. So… Do you allow folks that are deploying Keycloth to simply configure a hotel and then get visibility into what they're deploying?
Or do you have something that maintainers use to capture metrics and usage data, or something like that? So, what is the focus? And then maybe we can adapt a blog post on that.
**Alexander Schwartz (IBM)** 05:43 Yeah, sure. Makes sense to me, and I now understand you're looking for a blog post and less of a… Recording.
**Juliano Costa | Datadog** 05:51 But what we have done, just, for context, what we have done with the other companies that we interviewed, all of them were, live interviews, where we recorded the interview, and then we, as developer experience Seek, we wrote down the blog post, then sent And to the… to the person to review, because we know that I mean, at least for companies, we know that, they are already willing to spend their time in this interview, so we do not want to ask them to also write the blog post. So we wrote down, and then we just asked for their review and, like, approval, so now we are in the process of moving to the OpenTelem 3 IO blog.
**Perk (Marcin Stożek) | Elastic Ingest** 06:40 So then, the most important thing is, I think, this discussion. Like, you know, if we have another meeting, ideally we can record it, and then just, you know, take all of the information from that, write something, and then obviously Send it to you for, you know, approval, all the changes and whatnot.
**Alexander Schwartz (IBM)** 06:57 So is then the recording something that you would like to publish as well, or would you, in the end, publish only the blog?
What's your…
**Juliano Costa | Datadog** 07:04 oh.
**Alexander Schwartz (IBM)** 07:05 usual way of working.
**Juliano Costa | Datadog** 07:07 Cool. If we agree to do it in a separate meeting, then we would just record to ourselves, so we can refer to the recording whenever writing, but that's it.
If we record in this meeting, then this is automatically, recorded and published to the, like, all the SIG meetings are public.
**Alexander Schwartz (IBM)** 07:29 Oh, yeah.
**Juliano Costa | Datadog** 07:32 I mean, it's not on YouTube, but.
**Alexander Schwartz (IBM)** 07:35 It's there.
Yeah, that's alright. Good.
Good at America.
**Perk (Marcin Stożek) | Elastic Ingest** 07:41 Do you have a…
**Alexander Schwartz (IBM)** 07:42 Good.
**Perk (Marcin Stożek) | Elastic Ingest** 07:43 Do you have a preference, over that?
**Alexander Schwartz (IBM)** 07:46 I'm alright anyway, all of the ways. So, usually when people look at the recording, that's usually fine, but if people then try to do a write-up of a recording that I'm in… it sometimes gets difficult, that's what I… what I… Experience in the past, and Let's see how we do this.
But okay, I understood this, maybe I will make some notes, around that for the upcoming… For an upcoming, I don't know, information gathering meeting, whatever we call it.
What, yeah, what do you propose that's… that works for me?
**Juliano Costa | Datadog** 08:23 So… I think… from our perspective, we would be interested in… so, we are focused on the developer experience, so… and the folks that are actually using Hotel. So, your perspective will be kind of… new in this, process that we… that we have, so I think it's super valuable.
We would love to know, like, things that went well, things that didn't went well, what worked, what didn't work.
If you are… If you found any issues during this process, which components from hotel are you using, following semantic conventions or not?
Yeah. Things.
**Alexander Schwartz (IBM)** 09:20 Okay.
**Juliano Costa | Datadog** 09:21 You may be missing from the project.
Sorry.
**Alexander Schwartz (IBM)** 09:25 Yeah, okay, so you might be surprised what we are not doing in the end, but okay, let's… let's do that in another meeting then, that's alright.
**Perk (Marcin Stożek) | Elastic Ingest** 09:33 That would be great.
**Alexander Schwartz (IBM)** 09:35 Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 09:36 If I understand correctly, because when we were chatting during, that they're in Brussels, I think you've mentioned that you're using true way tracing?
That is the core? Do I… did I understand correctly? That you instrument the code?
**Alexander Schwartz (IBM)** 09:52 Well, so we're using Quarkus. Well, well, KCLock is a Java application. Let's start there. Well, maybe we should do an introduction, maybe… maybe after this chapter do an introduction, what we actually do.
huge ones, so… Keyclog is a Java application, and built on top of Quarkus. We had the, out the Java agent at some point. I can talk more on that when we go into the interview, but now we're doing the Quarkus instrumentation that's… well, the Quarkus Autel instrumentation that's there, which is building on top of some OTL libraries in the end, but it's not instrumenting the… not runtime instrumentation of the code, but having, like, the right pieces and… In the right places, to get, I'd say, observability, at least, for all incoming HTTP requests.
And then we added some more bits and pieces to… Yeah, for example, outgoing HTTP requests and We use some of the libraries that are there.
Because we didn't use the caucus one that was provided.
Then there were things like LDAP, where there was nothing that we could build upon. SQL databases were already there.
So I think we do… we did traces first, and then now we'll be doing, logs and metrics.
That's now coming in as a preview.
**Perk (Marcin Stożek) | Elastic Ingest** 11:17 Hmm, interesting.
**Alexander Schwartz (IBM)** 11:18 Yeah, that's where we are. But maybe another time. We might not have enough time today.
But that's the context in the end, and I now know maybe I bring one or two more people to whatever meeting we come up with.
**Perk (Marcin Stożek) | Elastic Ingest** 11:32 Oh, that would be great.
**Alexander Schwartz (IBM)** 11:33 Yeah, and either that, or… it's just me. We'll figure that out.
**Juliano Costa | Datadog** 11:40 The meeting, again, it doesn't need to be long, it's like… Half an hour, 45 minutes.
And we… if we can… so I'll… I'll put up… Outline suggestion here.
**Alexander Schwartz (IBM)** 11:59 Hmm.
**Juliano Costa | Datadog** 12:00 And… Is there a mayor that I can… or can I… do I find you on Slack?
On the CNCF Slack?
**Alexander Schwartz (IBM)** 12:09 Yeah, someone with CNCF Slack, there's also firstline.nasname at ibm.com. That would be my preferred email address for all work-related stuff.
**Juliano Costa | Datadog** 12:20 Okay.
**Alexander Schwartz (IBM)** 12:21 And, that's also a good address for invites, and, well, Slack, if I react to it directly, then it's usually… Good, if I don't react on it, I usually forget that there was a message somewhere.
Yeah. Fair enough. He's starting off my life.
Yes.
So.
**Juliano Costa | Datadog** 12:44 Perfect.
**Alexander Schwartz (IBM)** 12:44 Talking about… well, last thing about this one, then, is timelines. Is that something that you want to get done by… before KubeCon EU, end of March, or is it.
**Juliano Costa | Datadog** 12:55 And I might push it to a pro. No!
I think we have time for that. I don't know about how do you feel, Perk? Do you want to push that before Kipkon, or…
**Perk (Marcin Stożek) | Elastic Ingest** 13:09 I saw a message that we actually would like to, like, slow down a bit. Did I get that right? With the blog posts? So, I think the pipe… but the pipeline of blog posts is actually full at this moment, so before CryptCon would be, I think, hard thing to do, unless, Alex, you have, some preference.
**Alexander Schwartz (IBM)** 13:29 Oh, no.
**Perk (Marcin Stożek) | Elastic Ingest** 13:30 you don't, then… Well, I don't think that's the… that's the need here.
**Alexander Schwartz (IBM)** 13:35 So, I probably send out an invite just after Easter, or a preferred date just after Easter. So I have next week, and then I'm traveling for about 3 weeks, on business.
then, like, I will be more back to normal in April. That's my plan. And I… That gives me also the time to invite one more person, I think, to this one.
**Perk (Marcin Stożek) | Elastic Ingest** 13:56 Oh, that would be good.
And time-wise, do we want to use…
**Alexander Schwartz (IBM)** 14:02 this call?
Yeah, we could, probably. Usually… well, I have another meeting at my 10.30, or, like, in 15 minutes.
But that meeting will not be there in April, so, we can use this call, I think.
**Perk (Marcin Stożek) | Elastic Ingest** 14:18 We can also… I don't know for you guys, but we can also, like, move it back a bit.
**Alexander Schwartz (IBM)** 14:22 Figure that out, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 14:24 Okay, yeah, very good, very good.
**Juliano Costa | Datadog** 14:28 Oh, okay. No, I, I… I feel that we have a plan. I honestly feel that… it would make sense to have your story before all the other stories, because, those are two other pro- two CNCF projects.
But we are all into something, like, I have a talk to deliver at KubeCon, and busy, and I'm pretty sure you are also busy, so delivering to… and the blog post is also, like, already lined up. I saw that we have some blogs that are open, but they're not Published yet, so we would get into the queue.
So, let's not rush that, let's take the time and…
**Alexander Schwartz (IBM)** 15:16 Yeah, you let me know if you want to make it next week or a month later.
**Juliano Costa | Datadog** 15:19 No, no, no, no, no, no. Let's make… let's take the time to do it properly and do a nice story. And maybe till April, we already have the metrics and logs in.
**Alexander Schwartz (IBM)** 15:31 Alright.
**Juliano Costa | Datadog** 15:32 That would also be… be nice.
Good. Cool.
**Perk (Marcin Stożek) | Elastic Ingest** 15:36 Thank you.
**Juliano Costa | Datadog** 15:36 Yeah, appreciate your time, and you joining.
**Alexander Schwartz (IBM)** 15:41 Do we want to do an introduction, then? What are we… all of us doing, maybe?
**Perk (Marcin Stożek) | Elastic Ingest** 15:46 Sure.
**Juliano Costa | Datadog** 15:47 Sure.
**Alexander Schwartz (IBM)** 15:48 So… It's just gonna be the three of us, I'm not sure if anybody else is about to join, or is it just a small.
**Juliano Costa | Datadog** 15:54 Most pro… so, the… the developer experience, SIG is… So, I'm Giuliano, I'm a developer advocate at Datadog. I'm a contributor to the hotel for the last 5… Ish? Five and a half years.
We started the developer experience Seek myself, Tristan. Tristan is, also a long-time contributor. He is, involved in Erlang, Elixir, and, Declaration.
declarative configuration, And, Damien? Damien is from Elastic, and he… he's been away for a while. I don't know if he'll be back in the DevAX seat. Anyways, those were the three that started the… the developer experience here. We started discussing, we ran… we ran a survey back last year, and we got… So the survey went to users, and what we heard back from them was that they were… Happy with the project, but they lacked, real use cases, how people were using in production. So then we started doing those interviews, and then, Perk Matthew at Fosden, and he joined our SIG, I think.
3 weeks ago or so, and said, hey, I spoke with this guy, and I think it would be a nice story. Yeah. And said, yeah, let's bring him. So… That's me. Perk went to introduce herself.
**Perk (Marcin Stożek) | Elastic Ingest** 17:30 Thanks. Yeah, okay, so I'm a product manager at Elastic at this… at this very moment, but I'm also, like, I'm not a member of OpenTelemetry, but I… I think I should join, you know, at some point. I'm here, I am around since, like, 2019, I believe. You know, I was an engineering manager at some point at SumoLogic. We had a team of, I think, like, 7 engineers. I think, like, 5 of those people are actually, you know, contributing to OpenTelemetry right now, so… That, like, I'm around, and, I'm always… open to, like, talk to people and, you know, like, share experiences and, like, you know, blog posts and whatnot. So when you entered that, that was like, okay, yeah, we gotta do it. Personally, I'm the Kubernetes slash OpenTelemetry guy. I used to be a product manager at Canonical for Kubernetes.
He's now, product manager for OpenTelemetry, collector and friends at Elastic, so doing this kind of stuff, always.
I used to be a software developer, back in the day, not as far, you know, far away, and, well, maybe at some time I will go back, we'll see. I don't know.
**Alexander Schwartz (IBM)** 18:38 Good. Yeah, then it's probably my turn. So, I'm Alexander Schwartz, or just Alex.
I've been in the industry, like, 20, 25 years. Back in the days, yeah, you build it, you run it.
Always.
So, and all the… Tools we had back then, and tracing was expensive, and nobody did it.
But we have metrics, I don't know, maybe people know, well, Nagios, cacti, these kind of things, if you're old enough.
And then, I worked at banks, as a software engineer and IT architect, also consulting.
And, this running thing's great in production, stick with me.
It's about 4… I was using KeyCloak in, well, as part of my IT architect's role here and there.
Contributed a bit to it, and, like, 4 years ago… Fourish years ago, I then joined Red Hat.
Full-time working on the Kiklo project.
And, then worked on things like high availability, scaling.
But also, having great observability. When you want to do load tests and want to see why your things fail, you need to have some observability.
Metrics help, great logs help, but then also tracing.
I'm a big fan of exemplars.
So, how you can connect your, Yeah, your dashboard to these traces and see why there was that spike of that kind.
And, yeah, at Keyclog, I'm heading a team that used to be called an SRE team, which… well, we don't have our own production system, but we are the ones who want to make key clock.
better for those running it as an SRE and production, So we have all the things we need.
We now call ourselves Production Readiness.
Which is also a lot of things, but includes also this high availability, load testing, observability.
And, yeah, and last year.
Early last year, we added tracing, and then also an observability guide to KeyCloak.
Like, with a, like, a blueprint on how to do, SLIs, SLOs, for key cloak, to get people started with something that is hopefully good enough for most, let's say that.
Yeah, and then I have also some slides around that, about observability, how it can do things with Kickler.
**Perk (Marcin Stożek) | Elastic Ingest** 21:22 Out of curiosity, you said that you were at Red Hat, or IBM for 4 years, so you've joined after IBM acquired Red Hat, right?
**Alexander Schwartz (IBM)** 21:30 Right, that's correct, yeah. Just during or after COVID, I joined, Red Hat, and on 1st of July last year.
all the Java engineers moved over from Reddit to IBM. Basically, all the Keyclog folks were included in that, because Keyclog is based on Java.
And, Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 21:52 Yeah, yeah, yeah, fair enough. And also, IBM was always, you know, like, a heavy user of Java. I spent 5 years at IBM back in the day, back in Krakow, in Poland, so… I know the drill.
**Alexander Schwartz (IBM)** 22:05 Yeah, and then KCLock is a distributed team, as IBM is now, well.
trying to do… it's not so full remote as Red Hat was for us, at least, at the time.
But the K-Clock team is very distributed still. The Americas, Europe… Yeah, and that's, yeah, usually I'd say Europe and the Americas, that's where most of our team is distributed in.
**Perk (Marcin Stożek) | Elastic Ingest** 22:37 Would you say… would you say that the key clock is mainly, developed by folks from IBM, or do you have other companies chiming in as well?
**Alexander Schwartz (IBM)** 22:47 Yeah, well, that's something we need to fix when we want to graduate, right? We're an incubating project at the moment. I think… When you look at the commit count.
Red Hat and IBM are still doing the majority of work, but we have a lot of When you look at the maintainers, we have 3 maintainers from other companies.
As well, one from Bosch, a German company, another German self-employed.
someone went from Hitachi, yeah, but… there are a lot of users, but, not all of them are contributing. Like, there's a long tail of contributors, I would say.
**Perk (Marcin Stożek) | Elastic Ingest** 23:27 Hmm, okay.
**Alexander Schwartz (IBM)** 23:28 The scale of small contributions, but then the majority of work is done… still done by people.
Employed at IBM, though.
**Perk (Marcin Stożek) | Elastic Ingest** 23:36 And how many people are the core contributors for Kickok?
Just last question.
**Alexander Schwartz (IBM)** 23:42 Well, I wouldn't know how to count that. How would you count a core contributor, then?
**Juliano Costa | Datadog** 23:49 I have… I have this, actually. So, I don't know if you all know the Linux Foundation site.
**Alexander Schwartz (IBM)** 23:54 Yeah, I know. Yeah, yeah.
So…
**Juliano Costa | Datadog** 23:58 So you are the, in the last year, you are the top maintainer, top contributor?
**Alexander Schwartz (IBM)** 24:03 Yeah, well, but, so…
**Juliano Costa | Datadog** 24:08 Here are the… Other organizations contributing to the… to the project. Yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 24:14 Yeah, okay.
**Alexander Schwartz (IBM)** 24:15 So, when you see that 75% is done by Retta and IBM?
**Perk (Marcin Stożek) | Elastic Ingest** 24:19 Yeah.
**Alexander Schwartz (IBM)** 24:20 Mmm… that's where we are. Thomas Darwin was then also the first external maintainers, Bosch Digital… And that's the other German maintainer he touched, he doesn't show up on the list here.
Okay, yeah.
Maybe he did. No, Hitachi is there, yeah, Hitachi was there.
**Perk (Marcin Stożek) | Elastic Ingest** 24:37 Yeah, it was third, yeah.
Oh, okay, okay, basically.
**Alexander Schwartz (IBM)** 24:46 Yep, that's it.
**Juliano Costa | Datadog** 24:47 Well, no, I find this… really valuable, actually.
To see…
**Perk (Marcin Stożek) | Elastic Ingest** 24:52 It is. Yes.
**Juliano Costa | Datadog** 24:54 Yeah.
**Alexander Schwartz (IBM)** 24:55 We need to flip that at some point.
Getting, like, 25% from another company. Not sure how we want to do this, but… If you have some, I don't know, idle, full-time engineers at some point, let us know.
Security is correct.
**Perk (Marcin Stożek) | Elastic Ingest** 25:12 question. Will do.
**Alexander Schwartz (IBM)** 25:19 Alright, so that's all I have for today, I think.
**Juliano Costa | Datadog** 25:22 Yep.
**Alexander Schwartz (IBM)** 25:23 Cool, could I drop it?
**Juliano Costa | Datadog** 25:26 Thanks, Ted. Thanks for… for the nudge on the intro, because, yeah, I just… Jumped into the topic, and… Forgot to introduce ourselves.
**Alexander Schwartz (IBM)** 25:38 No, that's fine, that's fine.
looking at April, and if we want to reuse this meeting, would we then use, I don't know, April 8th or 15th? Would that be… Any preference from your side?
**Juliano Costa | Datadog** 25:54 Both of them work for me.
**Perk (Marcin Stożek) | Elastic Ingest** 26:00 Yeah, same here.
**Juliano Costa | Datadog** 26:01 Yep.
**Alexander Schwartz (IBM)** 26:03 Could you forward me these two dates, please, and that I have them on my calendar, and then I can forward it to others as well, that would be… it's usually handy, otherwise I sometimes mix up time zones.
**Perk (Marcin Stożek) | Elastic Ingest** 26:15 Sure. We can also, I think, move this meeting just, you know, like, back 30 minutes, so that we have, like, full hour.
**Alexander Schwartz (IBM)** 26:21 No, no, no, well, in April it will not be a problem.
Oh, okay, you see.
**Perk (Marcin Stożek) | Elastic Ingest** 26:25 Yeah, yeah. Very good. Okay, okay, okay.
**Alexander Schwartz (IBM)** 26:29 Alright? Then, see you on TLEC, or see you in April.
**Juliano Costa | Datadog** 26:35 CFC.
**Perk (Marcin Stożek) | Elastic Ingest** 26:35 Thanks, Alex.
**Alexander Schwartz (IBM)** 26:36 Or, maybe at Kipkon. Do we see at Kipkon?
**Perk (Marcin Stożek) | Elastic Ingest** 26:38 Oh, I… yes.
**Alexander Schwartz (IBM)** 26:40 Yes? Okay. Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 26:41 So we shop there. Awesome.
**Alexander Schwartz (IBM)** 26:43 Alright.
**Juliano Costa | Datadog** 26:44 Cool.
**Perk (Marcin Stożek) | Elastic Ingest** 26:45 Thanks, bye.
