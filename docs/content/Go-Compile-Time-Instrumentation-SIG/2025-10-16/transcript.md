SIG: Go Compile Time Instrumentation SIG
Date: 2025-10-16
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Przemyslaw Delewski** 00:03 Hello?
**Kemal Akkoyun** 02:03 Hello.
**Przemyslaw Delewski** 02:06 Hi.
**Kemal Akkoyun** 02:08 Hey, how have you been?
**Przemyslaw Delewski** 02:11 So, last week, I had a varicose vein removal surgery.
**Kemal Akkoyun** 02:20 And now you're feeling better?
**Przemyslaw Delewski** 02:21 Yeah, I'm feeling, good now, so I started work this week.
**Kemal Akkoyun** 02:28 Awesome.
Glad that you're feeling better.
**Przemyslaw Delewski** 02:33 Thank you.
**Kemal Akkoyun** 02:34 just that… I think one of the things keep… I think there's a thread, in Slack, the compile time check-in.
And I think, Jurassi pinged a couple of times, just in case you haven't seen that.
**Przemyslaw Delewski** 02:54 So, I haven't seen that. Maybe he was… because, you know, there is a problem that I have two accounts on Slack.
And there is…
**Kemal Akkoyun** 03:03 Oh.
**Przemyslaw Delewski** 03:04 my old account, and maybe he was pinking the old account, so I haven't received any message from him.
**Kemal Akkoyun** 03:13 Oh, okay, so you own, yeah… You are in here, but I don't know if this is an old account or no. It's a private channel.
So you have new icons?
**Przemyslaw Delewski** 03:26 Yes, yeah, I have a new account.
**Kemal Akkoyun** 03:28 Oh, yeah, you have different… Okay.
Maybe you should… Fair.
**Przemyslaw Delewski** 03:35 different image, I think I have.
**Kemal Akkoyun** 03:38 Yeah, maybe you should, like, write, I don't know, like, an old account or something, so that it won't… Yeah, confused. Now I'm adding your Neva account to this channel, so that you can see…
**Przemyslaw Delewski** 03:53 Because, you know, I don't have access to the old one, and I don't know how to…
**Kemal Akkoyun** 03:58 Okay.
**Przemyslaw Delewski** 03:58 You know, remove it or do something with it, so… That, that, duh.
**Kemal Akkoyun** 04:03 Pardon?
**Przemyslaw Delewski** 04:04 No problem.
**Kemal Akkoyun** 04:06 Okay…
**Huxing Zhang** 04:09 And maybe you can change your name of the new account.
**Kemal Akkoyun** 04:13 Yeah, maybe this is the new one. Yeah, that's a great idea.
**Przemyslaw Delewski** 04:18 Hmm.
**Kemal Akkoyun** 04:19 because, like, I'm not an admin, Boom.
Okay, let me write to the channel.
**Huxing Zhang** 04:51 So, I saw the difference of the two accounts, and then, the picture.
They're different.
**Przemyslaw Delewski** 04:59 That, that's true.
**Huxing Zhang** 05:01 I really suggest you can put something in your new account name that can differentiate from the old one.
**Przemyslaw Delewski** 05:10 Okay.
**Kemal Akkoyun** 05:12 Yes.
We were under the impression of, like, you are not responding to the thread, whatnot, and yeah.
Yeah, you've seen the thread, probably, you can check it out later.
**Przemyslaw Delewski** 05:23 Yes, yes.
**Kemal Akkoyun** 05:27 All right, so let me open the doc. I don't know who is the… Facilitator this week.
**Huxing Zhang** 05:36 I think it's your turn, Kimu.
**Kemal Akkoyun** 05:38 Oh, it's my turn. Alright.
Okay, that would be easier.
I can put my name… Yes.
I guess, we have only one topic to discuss.
Right? And it is what to do with the next steps.
Thanks, Ford.
putting that in.
So, thanks to Yi Yang, he's been doing a great job, but we need to step our game as the other maintainers and contributors, and I guess, the main problem for me right now, we even have the issue, but… an umbrella issue to describe all the next steps, but maybe it's, like, super clear how these all tied up to our end goal, but it's not, like, super clear to me, and I'm having some hard time to just, like, get into the project, right? So… And maybe, and, like, how I see that, I think we should, as soon as possible, put something for, NetHTP and gRPC, an example.
And this already, but there are also tools, like, if you haven't seen that, I think you have seen this.
**Huxing Zhang** 07:12 Eric, can you share the screen?
**Kemal Akkoyun** 07:15 Yep. I will also share this. Okay.
That is easy. Let's share the screen.
Can you see it now?
**Huxing Zhang** 07:28 Hmm.
**Kemal Akkoyun** 07:29 So…
**Yi Yang** 07:31 Yeah.
**Kemal Akkoyun** 07:31 I think there were… there have been discussed a couple of things in here. This is one of the posts that, I think, Premchik, you did, or, like, one of, your, comp… company? Yeah, this is… Probably your, like, company account. But there are a lot of discussions in here, right? The people asking… one of the things that people ask is, like, examples, right? So, I think we should prioritize to have an HTTP and gRPC example, how they can use, and then, like, maybe create another post for that.
So yeah, like, so maybe we can prioritize the… tasks in here, like, what is missing to… what is blocking for us to add the netHTP?
and GRPC, and maybe just, like, assign some of the tasks among us right now.
So that, like, we can help hold people accountable for delivery. What do you think?
**Huxing Zhang** 08:37 Yeah, I read the blog post as well, and I saw what I'm, have, learned from that post is, there are quite a lot of folks that, have pain, developing, like, have, developing in manual instrumentations, and they really want.
automation tools like us, like our project provides. So I think this may be very useful for them, and they just, have and know about our project, and another thing I want to address is we… can provide more documentations. I saw something… some people asking about the… how the, how, the project has been, work… has worked under the hood. Maybe we can add some documentations, or, including the explanations of how we… how it… how does it work, and, How to use, and, providing examples, something like that, yeah.
**Kemal Akkoyun** 09:51 Yeah, I think we did… you already gave a talk about it, and you talk, In detail, maybe we can link that YouTube recording of the talk.
some areas, documentation on the README so people can watch, but definitely, I agree, we need to do better, like.
documentation work, and maybe we can record the demo, but let's focus on first, like, adding the NetHTP and gRPC stuff.
And then maybe for those regions, I don't know.
record a demo, create some documentation, because that makes it useful, right? People, if they have, like, online services, they can just start using this one.
**Huxing Zhang** 10:32 Yes.
**Kemal Akkoyun** 10:35 Cool. So… from this list, I think this is, yes, Yi Yang, actually, maintaining this one, like, what is the blocker for us, to add net HTTP.
**Yi Yang** 10:51 Actually, I don't have a very, very detailed development plans. I think about the high… but the blocking thing is that we need to refactor the demo.
application to use a little GP or GPC tools, for example, to send a request and receive reset response. After the refactory, it could be, we can run it, and then we… I think we should write some instrumentation rules for them.
after that, the application sh… should, is expected to not work, I think. And the ongoing, the.
The next development plans is to make them work.
I'm not sure if I, if I described,
**Kemal Akkoyun** 11:55 I mean, if you can put something as a comment to this PR, about, like, the plan in your head, and maybe to update these tasks, that would, like.
That would be easier for us to understand, right? Also, for you to, like, clearly state the plan in your head.
And, like, we can pick a task. Like, I really want to get my hands dirty as soon as possible, so, like, don't, like, hesitate to assign a task to me, so… But let's, like, focus on… we have a lot of things here for, like, I don't know, quality of life improvements, maybe some refactoring things for the project in the longevity. Let's also, like, do that, but let's also focus on providing a value. I mean, the KubeCon is around the corner, and if we can I don't know, create something useful, some examples, maybe some recording, and we can ask people to like, I think we already talked about this with Jurassi, and we can create a update slide or recording, something, and they can share, right? And if we can get into that stage, and just, like, share that, what we have already done so far, that would be a huge win for us, and… The KubeCon is 10th of November, I think.
So it's plenty of time, right?
**Huxing Zhang** 13:19 Oh, you mean, Cook Carnos America?
**Kemal Akkoyun** 13:22 Yeah, North America. None of us going to attend, but we can still create an update post a YouTube recording, whatever, and we can't ask OpenTelemetry governance to maybe… there is a place for them. We already talked about this, right, in one of the private channels with… JRASI, I think, if I'm not mistaken, and there is a section for projects to give updates, like 5-minute recordings, whatnot, so maybe you can do that.
**Huxing Zhang** 13:50 Oh, that's a good idea. So we can provide some slides, you mean?
Yes.
**Kemal Akkoyun** 13:55 some slides… let's… I will talk about that. I will find that thread and write to Rasia about that. What is the form of that update? Is it some slides, or is it just a recording of a video, or whatnot? Let's understand what is the medium.
And then, like, implement the HTTP and gRPC instrumentation with a demo, and, like, send that to the KubeCore North America.
**Huxing Zhang** 14:18 That's… that's a really good idea. I think we… we should target for him. It's a big chance for us to expose this project, I think.
**Przemyslaw Delewski** 14:27 And, one question, regarding this demo, or… Some documentation… Do you think about them from the user perspective, or from the developer's perspective?
I mean… But, yeah.
**Kemal Akkoyun** 14:44 our users are developers, like, what do you mean? Like, do you want to have… demo something for contributors?
**Przemyslaw Delewski** 14:51 Yeah, so I'm think… yeah, I'm thinking about… I'm distinguishing these, two, you know, roles. So, first one is a developer, of course, that uses our tool, but the second one might be a contributor that is interested in internals of the tool.
**Kemal Akkoyun** 15:11 let's, like, focus on the end user, how people can use it, and if they use it, probably they are developers, and if they want to contribute, I think that's… that would serve the same purpose, right? If we get into the, like, nitty-gritty details of how this thing works, I think we opt out a lot of people, because most of the people, they don't want to know the details, right?
So, let's focus on the broader audience, like, who would… Like, the platform engineers that would use this.
**Przemyslaw Delewski** 15:40 Okay.
**Huxing Zhang** 15:40 Yeah, I agree with that.
**Kemal Akkoyun** 15:45 Okay, so I'm… I will create some action items, and I realize that we haven't checked the previous action items, and we will do that in a minute, so… Variable, pink… Someone from the government, governance committee?
to learn about, like, how can we give updates in KubeCon.
Alright, assign this to me… Cool.
And, yeah, just update the plan?
crafted… For, like, demo delivery.
I am going to assign this to Yi Yang. I don't know if you have… I don't know how… What is your email?
**Huxing Zhang** 16:58 Just, type the name?
**Kemal Akkoyun** 17:01 Yeah, it's not here.
the un… No?
Adipapa, maybe? Nope, I think my auto-completion doesn't work, I need to…
**Huxing Zhang** 17:11 On Sunday.
**Kemal Akkoyun** 17:12 in…
**Huxing Zhang** 17:13 Take, taking the name, name, right.
**Kemal Akkoyun** 17:18 Okay, we can figure that out, or you can assign that to yourself, Yiyan, like, I think you already have the… Okay, so about the previous action items, Do we… do you want to add anything about this one? Like, do we need to discuss any further?
**Huxing Zhang** 17:39 Yeah, I think we can, check out, check this issue again about… What else… what is the current status, and is there any update to the… Items that we can check it out, and anything to do next.
**Kemal Akkoyun** 18:00 Yes, I think, for example, the critical question is, do we need to implement any other rules than struct and function type to be able to deliver net HTTP and gRPC, functionality.
Does anything come to mind?
**Huxing Zhang** 18:21 Holding it.
**Yi Yang** 18:25 I think there are… they are necessary steps to, to accomplish, to accomplish the goal, to make a demo application runnerable.
**Kemal Akkoyun** 18:38 Exactly, but do we have… do we need any other instrumentation rule besides that, too?
**Yi Yang** 18:46 Oh, okay. I… I already sent, submitted a PR tool and, two, two new kind of, rules to, to let it work. Yeah, I think they are, they, they, they are necessary stuff.
**Kemal Akkoyun** 19:03 Okay, what are those? Like, are they in here?
**Yi Yang** 19:07 There are no, there are no update, up-to-date. I will, I will update it later.
**Kemal Akkoyun** 19:13 Okay, cool. Then maybe you can assign one of them to me, and I can help with that.
**Yi Yang** 19:20 Okay, okay. I think I'm not familiar with OpenTelementary and actual usage of the OpenTelementary, so I think, you can help to refactor the data application to to, to, yeah, to use, use data tree as GRPC.
**Kemal Akkoyun** 19:40 Okay, yeah, that's… that I can do as well.
But, like, if… like, what I'm… yeah, let's… let's see, I will try to do that, and if we miss any rules.
Then I will try to, like, talk to you about that and maybe add them, so… Okay.
Let's start with NetHTP.
So… I'm still, like, I… I don't know.
This… I hate that.
Okay, Dan, you will… Update… That one… And I will think, yeah, I think this is good for until our next meeting, either next week, or the week after that.
So… I will be out in the last week of October, but, like, we still have next week.
So, before we call it done, let's check the previous action items.
Yeah, I failed on this, I don't know if you have submitted something for KubeCon?
**Przemyslaw Delewski** 21:23 No, not from my side.
**Kemal Akkoyun** 21:26 Yeah, I dropped the ball on.
**Huxing Zhang** 21:28 I have some in the one, but this is not related to this project.
**Kemal Akkoyun** 21:34 Okay.
**Huxing Zhang** 21:35 But I'm still thinking there's a chance for the main conference, and we can do the co-located event.
**Kemal Akkoyun** 21:45 Yes, let's do that.
I was gonna suggest that it's until, I think, 2nd of November is CFP deadline for co-located events, and we have two candidates, actually. One is the Platform Engineering Day.
Observability Day. I think we have a high chance getting accepted in Observability Day, to be honest, but we can also try the Platform Engineering Day.
So, yeah, I was… I will do that. This time, I'm… I promise I will do that.
Okay.
So, I think there's this action item to share a documentation on instrumenting AI ML agents. I think this was… Your idea to create a tall Where we use… where we use this… our tool with AIML workloads, that was about that, I think… did you happen to do that?
**Huxing Zhang** 22:52 Not yet, I… I have to try to reach out to the contributor of this project, but… I think there's still… For me… for him, for the contributors to… gave a, like, English version of that, and maybe she… he has some… materials, like, in Chinese, I will try to push it forward.
**Kemal Akkoyun** 23:23 Okay.
**Huxing Zhang** 23:26 So my question is, do you have any… Candidate topics that you would like to submit?
**Kemal Akkoyun** 23:36 I just want to talk about the, like, I don't want to make it, like, complicated or… anything. I just want to talk about our tool, like, and how it could help, others to, like, easily instrument their application, right?
**Huxing Zhang** 23:50 And I assume that we will have a more fully-fledged tool.
**Kemal Akkoyun** 23:53 by March for KubeCon EU, let's just talk about that patterns, right? Like, what this tool can achieve. We already, like, instrumented several tools, whatnot.
I think we can even go ahead and find some CNCF tools and try to build them with our tooling, with our rules and whatnot, and showcase that people are gonna love those sort of things, whatnot.
And we can craft that proposal in that sense, right? Like, how it's easy to write these tools and instrument any application.
**Huxing Zhang** 24:27 Okay.
**Kemal Akkoyun** 24:30 So, nothing, nothing fancy.
**Huxing Zhang** 24:32 Okay.
**Kemal Akkoyun** 24:34 I think this enable CI test action, this is done, right?
**Huxing Zhang** 24:40 Yes, I think so.
**Kemal Akkoyun** 24:42 Okay.
Cool. So we carry over some tasks.
Mmm… More or less the same thing, I think this is the most important.
is to… Are the most important ones.
Let's highlight them.
**Huxing Zhang** 24:58 protocol.
Okay. First, the action item I want to add the one more thing. Do you… I want to reach out to the governance committee about whether we could use the maintainer… To submit proposals.
**Kemal Akkoyun** 25:23 There was a… there was a slot, we talk about that. I'm gonna try to… Yeah, I think… Slack is just… Deleting them.
But I will just do that, and ask Jirassi.
Mmm… And then, like, yeah, we talk about this, there's a way to actually share some updates.
Yeah, I pinged them, in the private channel, so you can also see, and, like, we will see, like.
What can we do, according to the response?
I hope it's a recording, then that would be awesome for us. We can just, like, record a screen and show that, how it works, whatnot. We can set up a, I don't know, a demo application.
some Kubernetes cluster install Jager and OpenTelemetry collector whatsoever, and we can show how end-to-end we actually collects, an instrument, whatnot.
**Huxing Zhang** 26:46 What I mean is, we can reach out to them to check if we can use maintainer to submit a proposal for KubeCon EU, I think.
**Kemal Akkoyun** 27:00 EU, that's another thing.
**Huxing Zhang** 27:02 being new.
**Kemal Akkoyun** 27:02 Okay, now we can talk about that.
I'm not sure about this one, because, like.
We are a small part of a huge project, and I don't think they would give us a whole slot about that, but let's ask.
**Huxing Zhang** 27:27 Fair.
**Kemal Akkoyun** 27:36 Do you wanna do this, maybe?
**Huxing Zhang** 27:39 Yes, I can, I can, I can do this. I, I can, yeah.
**Kemal Akkoyun** 27:45 I have already too many tasks, let's not… Overwhelmed.
Cool.
And yeah, yeah, like, let's… this is mentioned a couple of times, before we close it. I can stop sharing the screen, I think.
We could definitely, try to contribute, more.
Because, like, most of the contributions are coming from, right now, from Alibaba, and it's not fair. We are doing all this together, so Keishma and Datadog should do a better job.
And I already told that on the Slack channel, this is mostly on me. On our side, I am the one, like, supposed to do this, but yeah, other priorities came into way. But this quarter, like, this is my, like, P0, and this will be my focus.
So, yeah Sorry about the pest, but we will try to fix that.
**Przemyslaw Delewski** 28:54 Okay, I don't want to commit to that, but maybe I will spend some time trying to, you know, look at the gRPC instrumentation.
And, and maybe I'll share… what I did, so… I will try to find some time to do that.
**Kemal Akkoyun** 29:16 Sounds good!
Do you want us to create an action item for that, or… Do you want… you don't want to commit that yet?
**Przemyslaw Delewski** 29:27 I don't want to commit to that yet, because it might be hard for me to find this time, but I will try, so…
**Kemal Akkoyun** 29:36 Okay.
**Przemyslaw Delewski** 29:40 Just to, you know, at least to know what… what's… is… what is needed to… in order to… to do that.
Because there might be… Yeah, there might be some, you know, missing points and so on, so…
**Kemal Akkoyun** 29:54 Yeah, I wouldn't surprise, so let's, let's try to do that.
Cool! That's it.
From my side, are there any other topics that you would like to bring up?
**Huxing Zhang** 30:10 I just want to remind it that the Kukan North America is, like, November the 10th. It may be less than one month.
So, we need to… maybe we need to… Hurry to comf… to confirm that what we can do in Coop County, North America.
**Kemal Akkoyun** 30:34 I've already sent the message on the private Slack channel, where we have this check-in with the governance committee, and I think they should… they would answer, like, quite, fast.
Done. Accordingly, then, that we can make a plan.
**Huxing Zhang** 30:52 Okay.
**Kemal Akkoyun** 31:00 Muslim.
Fits that, of, yeah, we can finish early, which is better for everyone's time.
**Huxing Zhang** 31:13 Oh, okay.
**Kemal Akkoyun** 31:17 Cool.
See you, everyone, in the next meeting, I hope, and this time, let's try to finish some tasks.
**Huxing Zhang** 31:27 Bye-bye.
**Przemyslaw Delewski** 31:27 Thank you, buddy.
