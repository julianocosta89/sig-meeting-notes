SIG: End-User SIG
Date: 2026-04-23
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Reese Lee** 01:08 Hello?
Hey, Andre.
**Alexandre Ferreira** 01:16 I'm trying to see, I have a sidecar now.
**Andrej Kiripolsky** 01:21 Nice.
Nice, nice, nice.
**Reese Lee** 01:29 Huh?
**Andrej Kiripolsky** 01:30 How old is…
**Alexandre Ferreira** 01:32 She was born.
She's… it's… it's a girl?
She's not…
**Andrej Kiripolsky** 01:39 Okay, nice.
**Alexandre Ferreira** 01:40 she was born in January, but she's… she was premature of, like, 7 months?
So, like, her corrected age would be, like, 40 days, or something, yeah.
**Andrej Kiripolsky** 01:53 Okay.
**Reese Lee** 01:53 Doriano.
**Andrej Kiripolsky** 01:54 really tiny.
**Alexandre Ferreira** 01:55 Yeah.
**Andrej Kiripolsky** 01:56 Wonderful. So congrats here.
**Alexandre Ferreira** 01:59 Yeah, thank you. It's been quite some time in ECU, and we've… Brought her home a few months ago, and now she's getting heavier, and my back is hurting a little bit, but…
**Andrej Kiripolsky** 02:11 Legion.
I was just about to ask, like, this is so difficult with… is it your first child, I guess, right?
**Alexandre Ferreira** 02:17 Yes.
**Andrej Kiripolsky** 02:18 Yeah, that's the first child problem, like, when… when your back… like, you can… the kid can be, like, 3 kilograms, but already, like, when you carry it for a long time, it… it'll hurt. It really hurts.
**Alexandre Ferreira** 02:36 So, Rhys, I don't think we've met before, and, Andres, did we meet before me going to FAT leave? I don't think so, right?
**Andrej Kiripolsky** 02:47 I don't think so, actually, I don't think so. So we can do the intros first.
**Alexandre Ferreira** 02:52 Alright, so, I'm Alex, you can call me Alex, and I work at Grafana as a observability architect.
And, a few months ago, we joined a… the end user, sit, and most… actually the Blueprints project, and, I ended up volunteering to do the Cates, Kubernetes platform, Blueprint.
But then, I… I didn't have much time to work until now on it, so I was just picking up the… picking up the bass again, and… I updated the template, and I'm just… I just need to fork an OpenAPR on that.
And that's me.
**Reese Lee** 03:48 Oh, right on!
Well, nice to meet you, Alex, and congratulations on the little baby. I'm Reece. I have been with the end-user SIG since the beginning.
And I am also still, now newly one of the hotel community managers as well, along with Adriana.
And Julia?
And yeah, I don't have any quite exciting news as you to share.
But I'm really happy to be here, and… yeah, it sounds like you've been working on the blueprints?
Stuff? Awesome. Okay.
And, Andre, it sounds like maybe you two have already…
**Andrej Kiripolsky** 04:41 No, we actually haven't, we haven't met, so… Shay, can I go, or do you have anything else?
**Reese Lee** 04:48 Oh.
Please.
**Andrej Kiripolsky** 04:51 Maurice has a wonderful cat.
That she uses in her presentations.
That's an important piece of information. And, I'm Andre.
I am, user researcher at Grafana Labs. We never met with Alex, or as far as I know, and I'm based in the Czech Republic, I've been with End User Sikh for… One year and a few months.
And, yeah, it's been a lot of fun.
And, I work mostly on things that… well, I work mostly on surveys. I think that's… that's the best way how to… how to put it.
There are other things, like Blueprints, for example. I occasionally approve Dan's PRs, but that's about it when it comes to Blueprints from my side. And then there is a lot of work that Rhys and Adriana and other folks are doing on videos.
But that's also something that… I'm a little shy, so I am kind of avoiding it, and Yeah, that's… that's about me. And yeah, Ernest, before you joined, we just decided we would do intros, because we haven't met with Alex before, so Ernest, do you want to go next?
**Ernest Owojori** 06:13 Oh, yeah, so… Hi, Alex, and hi, everyone.
I'm finished, and I joined the MD6 through the NAS Foundation Mentorship.
you know, where I designed the, survey analytics templates, you know, the guidelines to how we should analyze surveys, and since then, I've been involved with analyzing surveys so far. I think it has been fun, and beyond that.
I have my research interest in the understanding collaboration dynamics in peer production communities, which a very good example of that is open source communities, which is why most of my work, or let me say most of my future work.
From now to the next 5 or 10 years will be around understanding how communities are evolving in terms of collaboration.
Through all different fronts, you know.
So that's pretty much me.
And.
**Alexandre Ferreira** 07:08 Thanks. Very nice to meet you, Ernest, and… Everyone else. And I forgot to mention where I'm based. I'm in Brazil.
And yeah.
**Reese Lee** 07:20 Oh, yes.
I… I am based in Portland, Oregon.
**Ernest Owojori** 07:27 I'm currently in Nigeria.
**Alexandre Ferreira** 07:35 Alright then, so, I don't know, like… Before me leaving, we were discussing the Blueprints project.
Almost exclusively, but it seems that This was merging… merged into the… End user SIG.
So now we have, like, more stuff to talk about, but I'm really not up to speed with, what should we do in this meeting today, so… I'll be mostly listening, and if you want, I can share what we've been doing in the… Kate's blueprint, but that's it, yeah.
**Reese Lee** 08:18 Thank you. I… I did message Dan to see if he has… if he's able to hop on, since you're here.
Since he is our main Blueprints person.
And…
**Andrej Kiripolsky** 08:32 Like, currently, we have two meetings, like, they're… the blueprints are part of EndUser 6, but… there's still kind of, like, a separate working group, perhaps? So we have two meetings, bi-weekly. On one week, there is, like, this usual end-user SIG meeting as we had before, and then on the other week, there is, there is, like, a Blueprints-focused meeting. So there was one Blueprints-focused last week, and we usually… well, if there are some Blueprints-related topics, we are, of course, happy to discuss them, and if there is anything we can help with, we are happy to, but we might not have that good of an overview of the Blueprints project, so… Yeah. Is there… is there anything that you would like to discuss, Alex?
**Alexandre Ferreira** 09:34 Nothing that you couldn't wait for the next meeting, the next Blueprints-focused meeting.
So, yeah.
I mean, unless we have… we don't have any other topics.
**Reese Lee** 09:53 I just wanted to chat about… Some blog stuff, so…
**Andrej Kiripolsky** 10:15 Also, Alex, you mentioned that you have to run after the first half?
**Alexandre Ferreira** 10:20 Yep, yes.
**Andrej Kiripolsky** 10:23 Yeah, Rhys, is it okay if we discuss the blog stuff in the second half?
**Reese Lee** 10:28 Oh, of course!
**Andrej Kiripolsky** 10:29 Okay. Ninia, Alex, like… If you… you said that it can wait, but if we have time, we can talk about the blueprints, so yeah.
Go ahead, if you have anything to share, yeah, please.
**Alexandre Ferreira** 10:44 So, first, I've been to this doc right here, but then I noticed that we have the template, and I should fork the OpenTelemetry.io repo, and open PR, and all that. So, I'll be doing this, Today, still.
But the gist of it is that I'm using this template to provide the summary and background, so… My thought process on monitoring Kubernetes is that there is two, main things that we should monitor. First are the workloads themselves, the services running in Kubernetes.
And this is usually monitored using the OpenTelemetry SDK, secondary traces, metrics, and logs, but also And I think this usually… I think people miss this part right here, where you have to monitor Kubernetes itself, so it's like a metamonitoring of the components, the critical components within Kubernetes, like coordinas and all that.
So, this is the summary, what, we can achieve out of this.
And then, as the template, specifies, we should put the common challenges here. And the gist of it is that, like, the first challenge, If you don't monitor the Kubernetes components, you could see, like, the application failing, but missed to notice that this probably is a DNS issue, or anything else, really.
By default, you will want to monitor those core components, like Core DNS, CADA, PGDA, and ingress controllers.
And I won't go into much, much, much detail, but we have this consideration here that I would like to discuss with, the Blueprints folks.
Perhaps in the channel, that, we have this double standard of Prometheus format versus OTLP, so if you use, like, QBSA metrics, this will usually come with the pod and score name, which is the Prometheus format, but OpenTelemetry actually expects this, right?
So this is stated here, and then a bunch of guidelines to address each challenge.
And… I know that Baby wants to chime in, but not now, okay?
So here, I proposed some guidelines to, to scrape workloads from those core components.
Use the OpenTelemetry operator instead of deploying and managing the collector life cycles on your own.
Metadata enrichment should be done via the Kids Attributes Processor.
And then self-monitor the… the components themselves, like… CubeSig metrics goes down, you will only notice that the other metrics, like CPU usage, has no data, right? So, you should monitor if the KSM bot are running a node exporter.
And then this probably will be the one that will open the discussion. I mean, we'll discuss mostly about this in the blueprints.
because of the difference between Prometheus and OpenTelemetry. So here I'm proposing that, like, if you're monitoring those core components, that exposes Prometheus natively.
You should keep this on Prometheus and use OpenTelemetry for the applications, the SDKs, right?
And then we should provide the reference architectures, to which I'm not doing right now here. And then a bunch of steps to implement all of this.
And… here… like… to deploy keepsake metrics, node exporter, and all of that. I'm doing that separately from… The… collector chart.
We'll have to discuss if we'll go this route, or if we'll recommend having the OpenTelemetry collector chart deploy those components, like I said metrics.
porting a nest… traffic, and then, some alerts, like monitoring, dipstick metrics itself, node exporter.
the self-monitoring of OpenTelemetry Collector, and here's an appendix with useful dashboards and alerts from the Grafana community.
And I… Asked AI to help with this, right?
I will only need to check if, like, this keepsometrics dashboard is the most up-to-date one. And that's basically it.
Oh, and then the reference architecture stack, you'll have to pull those up.
That's it, I think.
**Reese Lee** 16:12 Dang, that's very cool.
**Alexandre Ferreira** 16:16 And like, don't mind the… the 1,000 tabs I'll… I just forked the repo, I'll open the PR, and And do it, following the contributing guidelines, and I should send this today still.
**Reese Lee** 16:37 Sounds good, yeah. I mean, this was my first time seeing, like, one of the Blueprint docs.
So, it looks great to me!
**Alexandre Ferreira** 16:49 Minimum.
I like that.
So I guess this is, what I have to share today, and then, the next, Blueprints-focused meeting, is it next week?
**Reese Lee** 17:02 Yes.
**Alexandre Ferreira** 17:05 NISC, so I'll be there as well.
It's like…
**Andrej Kiripolsky** 17:09 From my side, it looks… it's also the first time for me, so… It was very interesting. It was actually, like, I was surprised how… I knew that it would be long.
and, like, very detailed, and, like, a lot of information, but it's, like, when you actually see it, it's… it's… it is slightly overwhelming. But that's not a bad thing. I think that was kind of expected, so I think that's… that's… that's okay. Two things… There were a lot of Prometheus stuff mentioned there.
And, I know, like, folks recent, like.
I know that there are some updates around Prometheus and, like, recommended usage of Prometheus, that there was, like, recently a new page on OpenTelemetry.io created about this.
Not sure if you are aware, but might be interesting to check it out. Let me… let me paste it.
To the… to the agenda.
Again, I'm not saying that it's… Yeah, I actually… I don't know to what extent this… helps or not, but I think it… Yeah, it's good to be aware of.
And, Agenda.
**Alexandre Ferreira** 18:44 Oh, interesting.
Yeah, and… To your point.
**Andrej Kiripolsky** 18:49 It's, it's…
**Alexandre Ferreira** 18:51 No, go ahead, go ahead, sorry, I'll, I'll… Simpler.
**Andrej Kiripolsky** 18:56 So, so that was, that was one thing, and, another thing… You had those links to… Grafana community.
And, I'm trying to… like, one thing that I really admire about everyone here is that folks are super strict about the vendor neutrality.
And while I'm also from Grafana, I think this is something that we should… we should, be careful about. I don't know what are the… what are the expectations about vendor neutrality on the Blueprint side. Maybe it's totally okay. I guess that also for the reference architecture, it might be totally fine to mention the vendors. I just want to flag it that, it might be worth discussing this in more detail with… with, the Blueprint folk. I'm sure that they will be able to give you more… more… more guidance on that.
**Alexandre Ferreira** 19:59 That's super helpful.
**Andrej Kiripolsky** 20:00 And that's it.
**Reese Lee** 20:03 Yeah, thanks for bringing that up, Andre. I wasn't sure how… since this was my first… first one that I'm seeing, I don't know what the standard is for… How you want to show those dashboards and stuff.
**Andrej Kiripolsky** 20:20 Yeah, yeah, me neither, me neither. And this is, like, really a very specific, specific project. I know, like, we kind of have this… I'm feeling already quite… Like, we figured it out for the live streams, and for surveys, and these kind of things.
about, like, what is okay or what is not okay to share from this vendor neutrality perspective, but I don't know how it works with Blueprints, and I think it's, like, very specific, specific thing, so it might be a little different.
**Alexandre Ferreira** 20:50 Yeah. I refrain myself from mentioning, like, Alloy and all that, because, like, even though Alloy uses OpenTelemetry, I get that, we have to be vendor neutral, more vendor-neutral as possible.
And to your first point on… at a first glance, this being very overwhelming, it really is, and I will try to discuss in the Blueprints project how we can cut this down as much as possible, to be more digestible, right? So, I'll probably even remove the code snippets and all of that. I'll just say, hey, here's the case attributes processor, and go there and do your stuff.
But, I'll discuss this in the Blueprints meeting as well.
And…
**Andrej Kiripolsky** 21:39 Yeah, and by the way, it was not necessarily even a feedback, it was just, like, my first time looking at it, and it's more than… if it would be a feedback, it's more of a feedback to, like, the blueprints template than to, like, what you did, because I think you just followed it, so I think we did a great job, it looks amazing.
**Alexandre Ferreira** 21:59 Thank you.
That's right.
**Andrej Kiripolsky** 22:03 Alright.
So, if that's it, we can go to the next topic.
**Reese Lee** 22:10 Thank you, Alex, and thank you, Andre.
Yeah, so blog contributions, so the way this came about was I was looking at the OTEL blog, to… I don't know, I was searching, I was researching something.
And I noticed that if you go to the 2026, you know, just like that first page.
Something that stood out to me was there were 3 blog posts by the Developer Experience SIG, you know, as part of their work with user… end-user organizations. So there's one from Skyscanner.
There's another one from… sorry, talking to Adobe.
and also Mastodon.
And… you know, I was like, oh, this is fantastic. But also, you know, we do similar things, and we have so much valuable content, and I know our focus has been on video, But, you know, I think there's a mix of people who watch videos.
Versus, like, reading blog posts and… Overall, I think, you know, we have… we produce a lot of valuable content for the community, and I think we could share it wider if we… Convert some of those into blog posts for the… For the blog site?
So one idea was just to do that. I know we've done the blog post from survey results, which is also extremely valuable.
But yeah.
I don't have, like… a strict plan to do this or anything. I just wanted to… Bring it up and see what… everyone else thought. I know it hasn't… it's not, like, super easy… well, it hasn't been super easy in the past to… Turned videos into a blog post, but… you know, I think we have more tools now that can… Help with that?
I know we've talked about, you know.
Maybe we can publish the transcripts, which is one thing, and that would obviously be, you know, kind of… It's very simple to do, But I think we could go a step further and, you know, take the transcript and then… Make it more into, like, a blog post style?
So I just wanted to… Get your thoughts, and feel free to think about it.
Yeah.
**Sophia Solomon** 24:47 Which, videos do you want to aim for, like, first, Reese? Like, is there one that you had in mind at all?
**Reese Lee** 24:55 I think our hotel and practice, video.
**Sophia Solomon** 24:59 Mmm.
**Reese Lee** 25:00 would be good, and of course, there's also, you know, if our… Guests wanted to… write up, you know, something themselves. Like, that would, of course.
be more than welcome. And then we've also done interviews, although I think we haven't done one in… Sometime.
I can't remember the last one that we did, because I know we've focused more on, like, hotel and practice.
Versus the interview ones.
Yeah, and I'll have to check the calendar to see what we have coming up.
**Sophia Solomon** 25:38 Hmm.
Yeah, because I think that would be… good… because I feel like if maybe if there's someone from the end-user SIG working with the person who was interviewed for hotel and practice, we could grab, you know, like, screenshots from their own, like, instances where they have it, and then kind of integrate all of that into a blog. I think that, like… I feel like Josh would be, like, perfect… a perfect guinea pig for this, honestly.
**Reese Lee** 26:09 Yeah, and, you know, I know some of our video content is… You know, we have some from, like.
the last 6 months that I know we've, like, had planned to convert into blog posts that, I mean, I'm also guilty of saying, oh, I'm gonna do this, and then, like, not actually being able to do it. But yeah, I… Obviously, would love to help out with this, And also would love other help. More help!
Also, Sophia, I love the color of your headphones.
**Alexandre Ferreira** 26:52 Oh my god.
**Sophia Solomon** 26:53 Gosh, thank you. They're plum, and I named my headphones Fi5o Plum.
So, yeah.
Nice.
**Andrej Kiripolsky** 27:07 I wanted to add, it's something we haven't discussed publicly.
**Reese Lee** 27:10 Thank you, Alex!
**Alexandre Ferreira** 27:12 Thank you, see ya.
**Andrej Kiripolsky** 27:13 So just want to mention, bye-bye!
dead… CommunicationSig mentioned… folks, Tiffany from CommunicationSeq mentioned that they now have a… Schedule for when they publish posts.
So it… so if we want to publish something, it might not get out right away, but, it's… But they are always welcoming any blog posts and contributions, so it's not something we should get discouraged by.
And we should still write, write them.
Yeah, by the way, regarding the blog post, one, Ernest's blog post about, Japanese survey will be going out next week.
And, Tiffany mentioned that I can do a blog post announcing the Prometheus and hotel survey, intergurability survey, so yeah, there'll be more blog posts for… I think it's… it's, like, the developer experience, I think it's more of a coincidence, because the project where they were talking to Skyscanner and these folks, it's something that they were doing since last summer.
And it… I think it just, like, happened that they… they finalized the vocals, like, in, like, a short cadence, and they were putting them out quickly, so… Yeah, but yeah, I totally agree, I think it would be great to have more of them out.
And also agree that it would be great to get help, and now I shut up tomorrow.
**Reese Lee** 28:47 Oh, no, that's great. Yeah, I was just saying, you know, like, when I went on the blog, and I was like, oh, the DevEx SIG, the DevEx SIG, the DevX… I was like, oh, they've been really busy!
Yeah, that was it. I'll look through, oh, sorry, Ernest.
I was just gonna say, I'll look through, like, our most recent videos, and also, I need to look at our calendar.
Because I know there's… we… you know, it's, like, kind of casual, so we'll be like, oh, we have this person and that person who said they'd be interested, but we need to, like.
Full up and get them.
on the books.
Yeah, that was it. Go ahead, Ernest.
**Ernest Owojori** 29:38 Yeah, he just, like, you know, had an… added an agenda there that I wanted to know, because there is a kind of studies that I would like to do. If you remember when, Amy came to our study last time.
I, you know, I was intrigued by the… Context of the research that they did about newcomers' experience.
And I took a step further.
I don't know if I can shortly present the, plan that I currently have.
My aim is to understand what SIG… is it okay to talk about those… the progress of those kind of work in this SIG?
You know, because I believe this SIG is working with every single SIG, Aww… We should just take it to the sick days.
conducting the studies. So let me… I don't know if we have time, I will try to… Talk through everything under, like, 5 minutes.
So that, I don't eat too much into our time.
Oh, yeah.
So, if you remember from… from Amy's presentation, if you, however, if you've probably checked the slide that she had.
on the interviews that they conducted, they had some findings that I, because I have a very strong and very good background.
you know, empire stores, the… The level at which you can trust interviews.
I have this opinion that there is little to what users can tell you compared to what you can find out by seeing their behavior on an improved level.
So I said, I wanted to take that studies into… The next level, which is… actually finding a way to craft out an umbilical hypothesis around the current result that they have, treating them as. Let's go find out if this is true.
So one of those ways to do that is to say, you know.
you know, does, issue quality, response latency, and augmentation reliability actually predict contribution of success? But I'm going to cut through all these stories and just go through the hypothesis.
that I have drafted. One of them is to find out if how detailed or how… good your issue description, actually predicts whether they could attempt to, you know, work on it, which I have described how to define that.
And, what are there ways to say, okay.
The rate… the time at which people respond, does it actually predict if someone will submit a pull request?
And the last one, which is, like, how detailed your contribution guide is, does it predicts, you know, the… margin of the pull request. These are crafted based on the findings that Amy's contributions he had on their interviews. So now.
I don't want to go into exact detail of… okay, let me just do just one to get a sense of, to get a sense of what I'm trying to say.
So, you know, brute force issues, you know, issues that are labeled brute force issues with eye distribution regions, I want to know whether they have a significant higher rate of newcomer attempts or not.
And, you know, Referencing the studies, one of the things that they said was.
you know, one of the participants said they found good force issues, but could not act on them, because his decision has assumed the prior knowledge of open telemetry. That is just one person. Is it the same for all cases? That is all the kind of studies that I want to do. We found out, and I said, I'm going to define Issue description as, you know, compositing.
Number of word count for a body of text of your usual. Then, how many code blocks are there, then number of links to source files are there, are there checklists in the usual description?
Then, you know, and set up on terms of sentences, do we have something that says install, run, you know, things like that. I will composite it into a… into a variable and call it issue description richness.
There is a whole body of knowledge that is doing this kind of research, but the thing is, a lot of people are not doing it on open telemetry.
And I see it as an opportunity for, you know.
me to do that kind of work. That is my research interest, and I see that opportunity for me to do that kind of work beyond doing surveys. If we want to do this by surveys, yeah, we draft questions, you know, and in a way, we still believe surveys also don't… There are randomness that we cannot control in service.
But when users have actually used GitHub to do some things. We can empirically say that this is not a fact.
you know, there's a lot in this document. If anyone is interested, maybe, Andre, I can share this with you, you know.
And then, you'll see how it goes, but the reason I'm presenting this is to know I want to do this kind of work in OpenTelemetry. Who are we interested to discuss that? I know that a lot of end-user people are not necessarily empirical, they are just engineers, developer advocates.
I know.
So, I wanted to know… who might want to listen to this? In terms of weekly presentations, bi-weekly presentations, or no?
Oh my god, you… Did I… did I invest it all?
**Reese Lee** 35:27 Oh, no, no.
It was just… my face was on your screen, and so it was just funny. I was making a… making a funny face.
**Ernest Owojori** 35:37 Yeah, so I want to do those kind of work.
why I'll be around service as well. I want to know what I'm, like, which is, like, which SIG or 6… Who want to listen to this.
Yeah, that's essentially my question.
**Andrej Kiripolsky** 35:59 To me, it looked super interesting. So, basically, it's analysis of data from GitHub. Basically, it would be… would be… taking data from GitHub and,
**Ernest Owojori** 36:10 Huh.
**Andrej Kiripolsky** 36:11 processing it, and then making conclusions based on that. To me, that looks super cool, and I think it would be awesome to see, like, what could you find there. It might be, to some extent, even, like, easier than surveys, because, like, there is a whole lot of… as you said, like, there's… like, people might respond, might not respond. It's not that easy to get those… get those answers. So, in this sense, like, the data is more available, and if you are able to do the analysis, then I… like, that's the only thing that you have to do, assuming that you have access to that… to those GitHub.
GitHub stats, but… yeah, to me, that looks… that looks super cool. And just one thing, I'm, by the way, very much confused about The difference between… To begin the user.
Or it's not, like, super clear, right? And it's not confused, but it's, like, it's not totally clear. Second user, contributor experience, and developer experience. These three six, like, my understanding is that we are taking more from, like, a… Process perspective, and perspective of… serving the other six and providing them with tools and helping through some of the parts of the work. But… Then there… and then there are, like, when… then there are contributory experience and developer experience who are taking care of, like, specific topics.
And they are less about… less focused on, like, standardizing, or, like, having… providing some kind of a process and tools, but where they… they're more… more creative about how they approach things. So… Yeah, and I think, like, it's… Regardless of how you want to approach it, I think there will be a lot of people interested in it, and interested in helping you, or, like, supporting you.
In both, end user seek and contributor experience. I know that Amy and Marilia are Going to try to, like, make some noise about contributor experiencing, because it was very… Like, there are not many people attending and doing… things, so it's mostly two of them right now, so if you'd like to… like, you can do it as part of second user, I guess? But I'm sure that if you'd like to hang out with them and contribute to experience as well, I'm sure that they would be happy about it as well.
**Ernest Owojori** 39:00 Yeah, thank you. I think I will try to reach out to Himi as to…
**Reese Lee** 39:08 I mean, I agree, I think it's interesting. I would like to see the results.
of that.
**Ernest Owojori** 39:15 Yeah, and I wanted to say that, generally, it actually takes time to complete those kind of findings, maybe an average of 3 months.
You know, but it's always very, very exciting, because at the end, you want to publish it in a knowledge base.
Maybe in a paper, but that should take longer time, but you communicate your findings to the immediate You don't really… yeah, magic, bad.
**Reese Lee** 39:38 Alright.
Arza's like, and I'm done.
Alright, looks like we have… One more topic? Elsell Prometheus?
**Andrej Kiripolsky** 39:59 Yes, and that's mine, and that's just an update, because I was talking about it last time.
So, last time, I said I will, publish the survey and do everything, and yeah, here we are, two weeks later.
And, I just want to let you know that, like, I finished the update of the survey, and I started doing some things around publishing. Just so you know, I… I asked to publish a banner.
on the communications, and I have almost ready, like, socials post.
And I'm coordinating with Jack Berg, who is posting something, actually, about OpenTelemetry and Prometheus interoperability as well, so we are considering, like, to combine that message. Not sure if it's a good idea, because it's, like, one message with four links, so I think things can get lost there, but… At the same time.
it might be better to post one message than have multiple messages about the same topic, I don't know. So… yeah, just FY, this is… this is where we are. I can actually show you how the message looks at the moment.
**Reese Lee** 41:13 Oh, yeah.
**Andrej Kiripolsky** 41:14 And I'd love to hear your feedback.
Pasting it into the entity agenda.
Something like this. So if you can take a look.
And again, like, not me, nor Jake. I use… social media expert, as… I guess, like, I don't want to talk… or, like, respond for Jack, I don't know, maybe he is, but I for sure am not.
But… Yeah, I think we can make it shorter.
But… Yeah. What do you think, folks?
**Sophia Solomon** 42:09 Hmm.
**Reese Lee** 42:30 Yeah, well… I do see Prometheus as mentioned, like, 6 times, So we could probably… it could probably bring that down a little bit.
But I do think it, I mean…
**Ernest Owojori** 43:04 So this is just going to be, like, a single or two paragraph on the… blog page.
**Andrej Kiripolsky** 43:13 Sorry, I'.
**Ernest Owojori** 43:13 I believe you want to put… I believe you want to post this as a blog.
To announce the survey?
**Andrej Kiripolsky** 43:19 Good question. No, actually, I wanted to post it as, on a social, so LinkedIn and, And, Blue Sky and Mastodon.
**Ernest Owojori** 43:31 So what's… what's going to be the difference in the blog that you said, Tiffany said, Mentioned that you could.
**Andrej Kiripolsky** 43:37 Oh…
**Ernest Owojori** 43:37 unknowns.
**Andrej Kiripolsky** 43:39 Yeah, in the blog, I wanted to announce just the survey, and explain the… the… Rationale behind why we are doing this survey, and what kind of stuff we want to learn.
That was the… that's the idea about the blog post. But… Again, very open to any feedback.
**Sophia Solomon** 44:05 Yeah, I think I just agree with Reese about… Mentioning Prometheus so many times.
But… I think it's really good.
I like, I like the copy.
**Ernest Owojori** 44:18 Yeah, the copy is nice for socials.
**Sophia Solomon** 44:23 It's not too long.
Maybe the middle paragraph is, but…
**Andrej Kiripolsky** 44:31 By the way, like… Total newbie question, can you do bold in LinkedIn posts?
Alright, no.
**Sophia Solomon** 44:40 You can't through LinkedIn, but you can, like, use a LinkedIn side editor.
like, on another site, and put bold in. It might be, like, a slightly different font, though, than the LinkedIn, locked-in font.
I've, I've…
**Andrej Kiripolsky** 44:57 Okay. Like…
**Sophia Solomon** 44:58 mess around with, like, italics and everything. It looked kind of weird, but it's fun.
**Andrej Kiripolsky** 45:04 Okay, okay, okay.
Cool. So… You did it.
Anonymous hedgehog is… making some changes, so I really appreciate that, thank you.
And.
**Reese Lee** 45:28 When… so, when it says new page, which… Is it referring to the… First doc? The first link?
the.
**Andrej Kiripolsky** 45:43 Yeah.
**Reese Lee** 45:44 This and open metrics compatibility.
**Andrej Kiripolsky** 45:52 I think it's referring to that new Prometheus and OpenTelemetry Client Libraries comparison page.
**Reese Lee** 45:57 Okay.
So… I'm also trying to do a… edit. I'm feeling on some… On a comfortable night.
Let me put both tools.
**Andrej Kiripolsky** 46:54 I don't want to… Interrupt.
Please, so I'll just shut up. I really appreciate that you are taking time to tweak it, so… And do you all feel that, like, 4 links is okay for a post?
**Reese Lee** 47:13 You know what, they could figure it out.
**Sophia Solomon** 47:14 like.
**Andrej Kiripolsky** 47:15 Okay.
**Sophia Solomon** 47:15 What…
**Andrej Kiripolsky** 47:15 Cool.
**Sophia Solomon** 47:16 Adding in links for, like, on LinkedIn, or…
**Andrej Kiripolsky** 47:20 Yes.
**Sophia Solomon** 47:24 Yeah.
**Ernest Owojori** 47:27 But wait, are you able to hyperlink a part of… a part of a LinkedIn post to an external link?
Oh, okay.
**Andrej Kiripolsky** 47:39 There's actually another question, yeah.
But Sophia was nodding, so I hope it's possible.
**Reese Lee** 47:46 You should…
**Sophia Solomon** 47:48 Jude!
Well, hmm… You can add in links for sure, but not… I don't know if you can hyperlink like you're trying to…
**Reese Lee** 47:59 Yeah, for LinkedIn, you can't… You can't hyperlink on LinkedIn, which is, like, stupid.
**Sophia Solomon** 48:05 Stupid.
Yeah, let me assume.
**Reese Lee** 48:11 I'm not sure about mass… I'm not sure about the other ones either, actually.
**Sophia Solomon** 48:16 I don't know anything about Mastodon.
**Reese Lee** 48:21 Okay, my suggestion is on the bottom.
Wonderful thing.
**Andrej Kiripolsky** 48:26 Thank you so much.
**Reese Lee** 48:27 Oh, no problem.
I just try to organize it a little bit.
butter.
**Andrej Kiripolsky** 48:37 Huh.
**Sophia Solomon** 48:43 A place called LinkedIn. It uses links so bad.
**Reese Lee** 48:46 It still says Prometheus a lot, but… Please check out.
Mmm… I think that's fine, you can also not stimulation up.
**Andrej Kiripolsky** 49:11 Gee.
Cool, so I just wanted to mention this. Thank you all so much for… for… Feedbacking, and, yeah.
**Reese Lee** 49:21 Hopefully it's helpful.
**Andrej Kiripolsky** 49:23 I was always… I was just, like, pushing it, like, okay, I'll do it next time, I'll do it next week, I'll do it next week. We have… we have a SIG meeting next week, and then I was starting working on it, actually, yesterday.
And I realized it… Like, except for just, like, asking for feedback, there is not that much.
that I was, like, supposed to be waiting for. I could just… I could have just done it, yeah, so…
**Reese Lee** 49:48 Oh, yeah.
**Andrej Kiripolsky** 49:49 Work, work, work.
**Reese Lee** 49:53 Yep.
**Andrej Kiripolsky** 49:55 Alrighty.
We don't have anything else, so… as Reece already mentioned, like, folks, if you, by any chance, want to pick any I mean… work any issue that is open in the repo, feel free to.
And, Other than that, do we have anything else to mention, please? Or Sophia, Ernest, anything else you would like to discuss in the next 10 minutes?
**Sophia Solomon** 50:25 I don't have anything.
**Reese Lee** 50:29 I think I'm…
**Ernest Owojori** 50:30 Nothing.
**Reese Lee** 50:30 I'm good.
**Ernest Owojori** 50:33 Yeah, it's funny, too.
Not anymore.
**Andrej Kiripolsky** 50:36 In that case, In that case, I guess we can wrap up, and Have a wonderful rest of your day, and… Upcoming weekend, and see you in two weeks.
**Reese Lee** 50:49 Yes, you all too! Good to see you all!
**Sophia Solomon** 50:52 Hi, guys.
**Ernest Owojori** 50:54 Yeah.
**Andrej Kiripolsky** 50:54 Right.
