SIG: Developer Experience SIG Meeting
Date: 2026-03-18
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/SMsZmQzlTbVdlbT_dtE0cPvSZZPWFPR1jtleG3pKPvMRsJJJoCBHaOAhqkT3LJCl.NWZDeFUTP6u2wMC4
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:05 Hello, hello!
**Johanna Öjeling** 01:11 Hey, Leno!
**Juliano Costa | Datadog** 01:13 Morning.
**Johanna Öjeling** 01:14 Morning, how are you, Drew?
**Juliano Costa | Datadog** 01:16 Good, good. Yourself?
**Johanna Öjeling** 01:19 Yeah, I'm alright. I think I'm, catching a cold, so yeah.
**Juliano Costa | Datadog** 01:25 Sorry.
**Johanna Öjeling** 01:25 A cup of tea, and yeah.
We'll just hope it will kind of pass quickly.
**But, yeah, how… Juliano Costa | Datadog** 01:34 Beautiful.
**Johanna Öjeling** 01:34 about KubeCon next week, and we go Bye.
**Juliano Costa | Datadog** 01:39 Excited? Yeah, I need to send the slides till today. They are… Johanna Öjeling 01:44 Okay, today.
**Juliano Costa | Datadog** 01:46 They're almost there, I would say, like, 80ish percent.
But yeah, you know when you miss the final touch to make the story, like, really tied together? So, I'm doing some, I'm revisiting it and going through all over and checking how this story flows.
Yeah. So, yeah.
**Johanna Öjeling** 02:10 Nice.
And your talk will be about… like, the cost of auto-instrumentation, right? And, like, yeah.
**Juliano Costa | Datadog** 02:19 Yeah.
**You know, how… Johanna Öjeling** 02:21 Take home.
**Juliano Costa | Datadog** 02:22 Huh.
Basically, comparing metal and alto instrumentation.
**Johanna Öjeling** 02:26 - Juliano Costa | Datadog 02:27 Cool, yeah.
**Johanna Öjeling** 02:28 I think that's a really relevant topic, so I look forward to watching the recording afterwards.
**Juliano Costa | Datadog** 02:34 Cool, thank you. Yeah, there are a lot of, benchmarks, talks there. Like, previous KupeCons, FOSDEM, There are many, but we take a different approach, and we talk about the data that we collect.
**Johanna Öjeling** 02:50 So… Juliano Costa | Datadog 02:51 We touch, of course, the CPU and memory consumption, but the focus of the talk is, like.
Size of this bin, attributes that… People are collecting by default.
**Johanna Öjeling** 03:04 Mmm, Juliano Costa | Datadog 03:05 Oh, this… All this, like, fire… fire and fire and forget issues, you know?
**Johanna Öjeling** 03:12 Yeah, - Juliano Costa | Datadog 03:13 Let me auto-instrument this and never look at it again. No, you actually should, go and, Clean up the data, instrument the things that you think are useful, add attributes where you think they are useful, remove attributes that you don't think it's useful, because all of that, in the end is cost on Storage, yes, but also, like, your application is producing this there's… This data is collecting this data, so… it can be minimal, but when you add Like, when we start adding, you see that in the end, it is a big impact, and yeah, that's… Johanna Öjeling 04:01 Yeah.
Yeah, I think it's, yeah, it's important for people to be aware of the trade-offs. Like, it's an easy setup, so it doesn't require much effort, but then, yeah, you will see the costs, like, yeah, when scaling in, yeah, in the long term.
**Juliano Costa | Datadog** 04:20 Yeah, and we are also tackling two things that people usually do, which is sampling.
And filtering out stuff. So, like, when you do on the collector.
This is good, because it will solve the issue of, storage, but, on the other hand, your application is producing that… Collecting all those data, all this data, so… you are basically paying for the infra to collect all of that, and then paying to the infra of the collector to prune all of that. So, if you don't need… don't even collect, then you already… you start already saving on the collection side, and then… You also say… of course, you can still do, assembling, because, yeah, that… that… It's good, you don't need all the data that you get, like, you don't get… you don't need all the, successful path, requests that went through, but yeah.
So yeah, that's it. And every time I talk a little bit, I… I remember that I forgot something on the presentation.
**Johanna Öjeling** 05:31 Okay.
**Juliano Costa | Datadog** 05:33 Hey, Chip.
**Johanna Öjeling** 05:34 That's good. Viewing the talk from many angles.
**Juliano Costa | Datadog** 05:40 Yeah.
On the… on the SIG itself, I think we have, the two blog posts already lined up. One of them will be published today.
**Johanna Öjeling** 05:53 Yeah.
**Juliano Costa | Datadog** 05:54 everything right. And then the second one after Qubicon, if I got it right.
**Johanna Öjeling** 06:01 Yeah, exactly, the week starting on the 30th of March. So yeah, that should be the week after Yukon. So yeah, I think that's great, and also, for the Skyscanner post, Neil came back and said that now the PR department has approved it, but he wanted to Double-check with, the architecture diagrams.
So he, like, pasted, some pictures, but he wanted to check with the Kubernetes team to see that it's accurate, and then I'll… once he has confirmed and, like, updated, then I'll draw them with ExcalDraw. So, yeah, it's consistent with the rest.
But yeah, then, I think, yeah, Skyscanner posts.
Should be ready quite soon, too.
So maybe, like, one or two weeks after Adobe.
**Juliano Costa | Datadog** 07:00 and Skyscanner.
Waiting… Then set date.
**Just, updating the… Johanna Öjeling** 07:14 Oh yeah, nice.
I'll paste, please.
**Juliano Costa | Datadog** 07:20 On the submitting notes. Cool.
Yeah, so… then I think that's it. We don't… we don't have much, and I know Tristan is being away for… for some time.
**But I feel that we have… some things to… to do already. So, like, the… the blog posts are already lined up, we have drafts, and I think even the one from Tristan is already at, Use Boy State, so we just need to… Johanna Öjeling** 08:01 Sounds scarier, yeah, Juliano Costa | Datadog 08:04 And then… after KubeCon, where… when we're gonna start?
opening the PRs, we will also have the meeting with Alexander from… from Key Club?
And… Yup.
Yeah, I think that will also be a nice interview to have, because this is how projects are using OTEL, so this is pretty cool.
**Johanna Öjeling** 08:32 - yeah, I'm excited about that one. I'll have a look at the questions.
All services.
To see if there's anything.
**Juliano Costa | Datadog** 08:42 Yup.
**Johanna Öjeling** 08:42 No, but… Juliano Costa | Datadog 08:43 I… Johanna Öjeling 08:44 So far.
**Juliano Costa | Datadog** 08:44 I added to the… in the blog post outline, there is, like, a tab. Not a tab, but, like, a… a second… view, where you have, like, interview, for the interview with Key Club.
It doesn't change much, but I think there are some things that are… that they are not using, so I just dropped.
**Johanna Öjeling** 09:08 Okay, okay.
**Juliano Costa | Datadog** 09:09 If you feel that there is anything that it would be nice to add, feel free to add.
**Johanna Öjeling** 09:15 - Juliano Costa | Datadog 09:17 Because then we… during the interview, we go through and see if we cover everything. I feel that having an outline is better to guide us during the interview.
**Johanna Öjeling** 09:28 Yeah.
Yeah, I think these questions are great. Maybe I'll add one.
In the… like, around… maybe after question 6, or, like, a sub-question, if… like, if there was anything they wished they had when getting started, if… yeah, if they can recall, like, if… yeah, is there anything that would have made it easier?
On board onto the top.
**Juliano Costa | Datadog** 09:58 Awesome.
Awesome. Yeah.
I don't know if you, just to share with you, I don't know if you are aware, but there is also another project, that is being started by the end user seek that is called Hotel Blueprints.
**Johanna Öjeling** 10:16 Yeah, I heard of it, but I'm not… Juliano Costa | Datadog 10:18 Okay.
**Johanna Öjeling** 10:19 I don't know exactly what the status is right now, yeah.
**Juliano Costa | Datadog** 10:22 Cool, so the idea is to have, like.
Blueprints of how companies are using, or how companies are deploying their, how companies are using hotel in their environment.
Why they want that?
So… Basically, to serve as a guideline for newcomers, and it's basically the same goal that we have with the blog post, but the main point is that the blog posts we usually do not update.
**Johanna Öjeling** 10:57 We have a.
**Juliano Costa | Datadog** 10:57 Policy that once the blog post is published, we don't touch it.
But, On the other hand, for the blueprints, they want to make it as a live document, so whenever something changes in that recommendation or that blueprint, then they go and update, so keep that up-to-date with the… The latest things that companies are using and have proven in production.
I'm really short on time, so I'm not involved too much in the discussions. I know that Danielle, Danielle, Gomez Blanco from New Relic, Dan.
is leading that. He pinged me on, one issue, and… on Slack.
But I just replied to him and said, hey, to KubeCon, I cannot commit any minute with anything, but we will have another sync. And I think Damien said the same.
Damien has been away, he's been away from this SIG as well, so I don't know what… what's gonna be the future of this SIG whenever the blueprints, Starts… I know that Tristan has other things that he wants… he planned to… to tackle with the developer experience here, but we will keep that… that discussion going. And of course.
The blog post will go, like we started, we're gonna finish this, publish everything, and then, we… we decide, as a group, what we're gonna do with the SEEK.
**Johanna Öjeling** 12:39 Yeah, - yeah, sounds good, so that's, yeah, probably a good topic to tackle. Yeah, the week after KubeCon is the interview, but then, yeah, perhaps the week after that. Then we'll also have published a couple of blog posts already, and yeah.
**Juliano Costa | Datadog** 12:56 Cool.
So… I don't know what to write here, but like.
**Johanna Öjeling** 13:22 Do you know… what some of those other initiatives are that Tristan has in mind?
**Juliano Costa | Datadog** 13:29 When we started, he… he wanted to focus on the SDK.
**Johanna Öjeling** 13:36 - Juliano Costa | Datadog 13:37 Like, setting up a hotel, and really… Like, on the… the developer itself.
But… From the survey, we saw the need of having some educational content on how people are using the collector.
So, then we shifted a bit to the collector story. We're gonna present that as a… result, and then maybe Tristan wants to revisit the SDK and maybe do a more opinionated survey.
Because the survey was like, hey, when, starting with hotel, did you have any issues? And, like.
People could answer yes or no, and there were also open text fields.
But maybe now we can run another survey, like, hey, on the SDK configuration, what do you think about this? What do you think about that?
**Johanna Öjeling** 14:42 Yeah, - Juliano Costa | Datadog 14:43 What would make your life easier when configuring this?
Again, also don't know if he's still interested on that, because now we have the configuration file.
that… will make way easier to configure the SDK.
**Johanna Öjeling** 15:00 Oh, the declarative config. Yeah.
**Juliano Costa | Datadog** 15:03 Yeah, please.
Yeah, but… Wow.
**Still, so… Johanna Öjeling** 15:10 Yeah, but that could also be good to evaluate among those early users, like, what, yeah, how's it working, and… Yeah, any pain points, or… yeah.
**Juliano Costa | Datadog** 15:22 Yeah, totally.
Yeah, well, I feel that with Java, everything is easy, and the more you go to other languages, you'll feel like, okay, yeah, why is that… why do I need to write that much in Java?
**Johanna Öjeling** 15:39 I was just like… Juliano Costa | Datadog 15:39 I'm invaribo, and… And it's not.
**Johanna Öjeling** 15:43 Are you changing the OCL demo, the Java services to use declarative config, or do you have plans to do so?
**Juliano Costa | Datadog** 15:52 No, we have added two product, product catalog, I think it's Go.
We have added to… to a goal service, Alex, Bolton from Honeycomb, he… We send a PR replacing… reconfiguring both goal services to use the clarity configuration, and I said, hey, maybe we can keep one service using the clarity configuration approach, and another service using the manual, because the goal of the demo is to demonstrate how to use.
**Johanna Öjeling** 16:27 - Juliano Costa | Datadog 16:28 And we have, like, both different scenarios there.
But I feel that the more we move.
towards having the config as the default, then I think in the demo, we'll just go for the config, because that will make our life way easier as well.
**Johanna Öjeling** 16:47 Okay, Juliano Costa | Datadog 16:48 Have one central config file, and then all applications pointing to that.
**Johanna Öjeling** 16:54 Yeah.
Cool.
**Juliano Costa | Datadog** 16:59 Cool.
Yeah, let's see. The future is bright.
**Johanna Öjeling** 17:05 Yes.
**Juliano Costa | Datadog** 17:07 There's a lot going on, but yeah, I feel that we are in a nice path here as a project.
**Johanna Öjeling** 17:16 - yeah, I agree. Yeah, I'm excited to also, talk after KubeCon about upcoming initiatives.
But then I guess next week, this meeting will probably be council, because you'll be at QCon, and Eric will be there too, I think. And then, yeah, Tristan and Damien haven't been here for a while, so I'm not sure.
**Juliano Costa | Datadog** 17:39 Yeah, I think Damon will also be at KubeCon.
Tristan, I don't think he will be, but I'll text on the… on our chat, so we can officially.
**Johanna Öjeling** 17:49 Oh, okay.
**Juliano Costa | Datadog** 17:50 next week.
**Johanna Öjeling** 17:51 - Then, yeah.
**Juliano Costa | Datadog** 17:55 in the basis.
**Johanna Öjeling** 17:56 all the best for QtCon. Thank you. I think as well.
**Juliano Costa | Datadog** 18:02 I appreciate it.
**Johanna Öjeling** 18:04 It'll be amazing.
**Juliano Costa | Datadog** 18:06 Thank you.
Well, then see you in 2 weeks.
**Johanna Öjeling** 18:11 Yes, see you then. Cool, have a good day.
**Juliano Costa | Datadog** 18:14 You too, bye.
