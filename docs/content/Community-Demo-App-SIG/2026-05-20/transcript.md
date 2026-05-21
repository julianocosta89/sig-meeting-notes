SIG: Community Demo App SIG
Date: 2026-05-20
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/CNpNQJSYsERAQ7jDD5x_5-AosL3Mv9ZFOYorRzZuaD7H-zRWjg-d_Kmo38E9csu1.6zgGLNDC-HdP3wMi
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:38 Hello, hello.
**Donal O'Sullivan** 00:45 Hello.
**Juliano Costa | Datadog** 00:48 You are… There you go.
**Donal O'Sullivan** 00:51 Always defaults to the long camera.
Agreed.
**Juliano Costa | Datadog** 00:57 Kid, kid. How are ya?
**Donal O'Sullivan** 01:02 All good, all good.
**Juliano Costa | Datadog** 01:04 Hey, Phoenix.
**FELIX GEORGE** 01:06 Hi.
**Juliano Costa | Datadog** 01:07 I'm happy that you joined, actually.
I have questions.
So… We are, we got a user sending a bunch of PRs to us, renaming… Renaming, our attributes.
We usually use app, or we… We used to use app.something, then, count, or… Whatever. And that was always the pattern for the demo.
But app became a reserved key, so now we are migrating off everything to demo.whatever.
And this user is sending a bunch of PRs. So that will break a bunch of integrations that we have, for instance, with Grafana and all that stuff, and if we have, vendors showcasing dashboards with the demo.
That's all great.
**FELIX GEORGE** 02:16 Yeah.
**Juliano Costa | Datadog** 02:16 So, that… Debt… There is that. We're also adding FirePit. It's already part of the demo.
**FELIX GEORGE** 02:27 Yeah, I, I saw that.
**Juliano Costa | Datadog** 02:29 The profiling one.
We have, Pierre, PR from Pierre that, changes the way that we deploy the demo with the layered, Docker Compose file.
So, all of that to say that whenever we finish the rewriting of the attributes, we are planning a major release, so, like, demo 3.0.
And my question to you is, should we consider adding the agentic demo?
Also, to this… I, I think… on a time perspective, I think it would fit, and also we could make some noise out of it, so, like, working on a blog post, sharing what we are adding to the demo, why we decided to do a a bump and everything, so I think that would kind of shed some light into the demo back again.
But yeah, I wanna hear your opinion on the, on the work.
**FELIX GEORGE** 03:31 I… I would love to, do that if, that's possible, because… so this… we were internally using this for a while now, I mean, more than around 6 months, to be honest, right?
Like, for, for trace collection, and we were, working on, some, papers and all, for anomaly detection on the generated traces.
Like, our own mechanisms, and… So, we have been working on, using this for some time right now.
And, yeah, right now we are also, some of… also trying out some other agents, like Miro agent, or, like, you know.
So, but to start with, I think this will be very helpful for anyone to get into the agentic phrases and, you know, someone. But, to have, for example, so right now I have, I haven't added to the repo, but I… I did a share with Shinoy.
like, GPT-4 and Claude, Opus 4.7 caches. So, if we add… if you can add caches, users can use it even without an LLM.
like, given that the queries probably won't change, and tool responses won't change, you can add the caches. People can… you see it without an LLM, I think that's a very good feature, given the cost of the tokens are really high.
So the third part is, to have a local LLM where the users can run their own So, so by default, the small models, which you can fit in your laptop, for example, I'm using this, Apple Silicon, laptop. Okay, so, I was able to run, models which are below 3 million.
locally, I mean, natively using MilLM, but you can also use Olama to run even, you know, slightly larger models. I think GPT OS is also something you can run with OLAMA.
But, yeah, so consider it about… I was trying to fine-tune a very small model, so we can run it on Docker systems and something, right? So, somewhat, to some extent, you know, we should have some custom parses. If we have that, I think Jama 2 billion model will be a good choice. I just… kind of made it, you know, it was kind of possible to work with it. Quen was not working for me, I don't know. Maybe I was doing something, yeah.
I don't have much clarity on that part, on having a local LLM, but I think we will reach there soon, but yeah.
So this is my conclusion, and I hope the PR looks in a good shape. I have tried to resolve all the All the changes that were requested.
So, and, please, if you guys get a chance or time, I know everybody needs to spend my time. If you get a chance, please try it out, and you can send me the feedback, I will try to make appropriate changes. I would love to go. It could go with this timeline.
**Juliano Costa | Datadog** 06:40 Cool. Okay. Just to… to get Shenoi on… on… on the… on the topic. So, Shanoi, we are having a bunch of, changes on the demo lately, and whenever we have the… all the attributes renamed to demo.something.
We are planning… to have a major release, so like a demo 3.0.
And I was asking Felix if, it would make sense to also add the iGenTech Demo to… to that release, because then we can… also announce and make some noise out of it. So, I think… timing… thinking about timing, I think, would make sense. I just know, the state of the PR, because to be honest, I haven't looked at it. I know that you have reviewed, so I left it to you, and you guys are still talking, so I said, okay, yeah, I'll leave to Shanai to… to… to take care of it. But I can, of course, take a look and see, how it is and stuff, but… Yeah. That's it.
**Shenoy Pratik Gurudatt** 07:52 Yeah, I took a couple of passes. Just last week, I was not able to take the look at VCR and the cache file that Felix sent over.
I didn't get time. Let me take a look this week again. What's the, timeline, probable timeline for the release that you're thinking of?
**Juliano Costa | Datadog** 08:09 We still have a bunch of app. attributes all over the place, and I'm happy that the contributor that is sending the PRs is, going through, like.
a subset of… per time, so it's not a major PR, changing everything all at… all at once. It's changing, like, Not one by one, but, like, group by group, so that's making the review process really easy.
But, yeah, if he stops sending the PRs, I think we can take care of it, but I… if he continues sending me, I'll just, keep merging and getting through, so, like.
**Shenoy Pratik Gurudatt** 08:56 Yep.
**Juliano Costa | Datadog** 08:56 I don't have, a deadline for that. I just knew that the amount of commits that we have, and the amount of breaking changes that we have, we should have a release soon, because… Yeah.
**Shenoy Pratik Gurudatt** 09:12 Yeah, I saw the last one was in Jan, so…
**Juliano Costa | Datadog** 09:15 Big glass.
For instance, I really want to talk about Firepeit, but it's not available on Helm yet, so, like… It's the new kid on the block we should talk about. And then, of course, the Gen AI stuff, so…
**Shenoy Pratik Gurudatt** 09:29 Yes.
**Juliano Costa | Datadog** 09:30 We add all of that, then, like, we have, a full… A fuer now.
**Shenoy Pratik Gurudatt** 09:38 Okay.
**Juliano Costa | Datadog** 09:38 To, to do.
**Shenoy Pratik Gurudatt** 09:40 Yeah, I think, I… with the current state of the… PR, I think the main thing is the cache one that we already discussed. I didn't test it out yet. But I was also thinking, if we have some hard-coded prompts there in the VCR file, is that good enough? Because in the previous, LLM thing that we have for recommendation service, irrespective of whatever is the prompt, it just starts putting out recommendations from cache, whereas here, in VCR, you need to put the exact prompt.
And only then you'll get the response. Felix, correct me if I'm… Wrong day.
**FELIX GEORGE** 10:15 So, earlier, the key difference is, it's a multi-hope completion, right? So, for example, get me all the products, and get me the cheapest product, identify the cheapest product, okay? So, suppose this was the case. First, the LLM model should decide what tools to call here.
So, that's the first step. So, one LLM call is already completed, okay? So, based on the response here, then only we can you know, call the second… second, tool, or, you know, generate the response based on the response of the tool, right? So, earlier, it was just, get me… it was very simple, right? Get me the reviews, or, you know, something product.
**Shenoy Pratik Gurudatt** 10:56 More like question and answer?
**FELIX GEORGE** 10:57 We're just gonna…
**Shenoy Pratik Gurudatt** 10:58 Sequential chain, so you cannot chain… yeah.
The first thing.
I'm just thinking, so in that case, can we just make a minor modification in the chat UI, where if you don't have an LLM model connected.
you have some set of questions that are already there from the VCS.
**FELIX GEORGE** 11:16 That's already there, that's already.
**Shenoy Pratik Gurudatt** 11:17 Okay.
Like, I can just click on the question from the VCR cache, is it? And then, rather than typing, because the problem is, if I type, it will not do anything.
**FELIX GEORGE** 11:27 Yeah.
**Shenoy Pratik Gurudatt** 11:28 Instead of typing, we can just give them 3 blobs, maybe, of… some prompts, and you just can click it and view it. I'm just thinking, like, from an easy usage point of view, because it goes in 3.0, people will start using it a lot, and we don't want things to just not work.
**FELIX GEORGE** 11:46 So, what I think… so, I created a curated set of prompts.
I think it's, it's… like, there are some prompts, internationally curated to break the system as well. I mean.
everything shouldn't work, give you the characteristics, right? So, there are some prompts which might confuse the LLM, and it should fail, is what I thought, to generate a, you know… So, you can check out the prompts file that I have said.
So I had created it, using Cloud and GPT, iteratively, I have run it again and again, and, so, so it was a, bit tedious process, but I think the prompts are… give you a complete set, kind of, you know? It is able to activate all the tools, or all the tools exhaustively.
And, yeah, so I will select few prompts, which will always give you the same response, irrespective… from the cache. So, I'll do that. So, we already have few sample queries in the UI, I will add to that.
**Shenoy Pratik Gurudatt** 12:51 Okay, got it. Yeah, even in the chat UI, if you can… if you don't have a model connected.
If you can just give preloaded questions.
That users can select from. That's the best thing. You just… you don't need to give the free from chatting.
You just give the preloaded questions that you have, couple of them which will work end-to-end, couple of them which will fail. That is fine.
**Juliano Costa | Datadog** 13:11 I think… I think it's kind of what we have now with the question and answer, like… We have preloaded questions that the user can just click, or we have the text field where they can type.
If there is no OLLM, if they type something, Like, if you don't provide your key, and you type something, then nothing happens, but if you click on the questions.
It will happen all the time.
**FELIX GEORGE** 13:42 Yeah, yeah, okay.
So…
**Shenoy Pratik Gurudatt** 13:44 with the minor feedback, and what I'm thinking is, maybe this week we can do I can look into it deeper, and we can get it to a state that we can ask, Donal or Giuliano to do a second review as well.
on it.
**FELIX GEORGE** 13:59 Yeah.
**Juliano Costa | Datadog** 13:59 That will be cool.
**Shenoy Pratik Gurudatt** 14:00 Yeah, we can just get it to a stable state, is what I'm thinking. I'll have some bandwidth this week to get this done.
**Juliano Costa | Datadog** 14:07 Awesome.
**FELIX GEORGE** 14:08 thing.
**Juliano Costa | Datadog** 14:10 So, this was one thing.
Great that we… agreed.
Let me just fill in the… The attendees here on the… on the… on the agenda. And Felix?
George?
Honeybee.
Did it?
Okay.
Pierre had sent me a message saying that he wouldn't be able to join today, but he… he said that the… the layered, compose file, the layered Compose deployment PR should be ready.
So I'm traveling tomorrow, but I think I'll have some time to take a look. I know that Donal already, reviewed, and provided some feedback. Donal, would you be able to take a second look there?
**Donal O'Sullivan** 15:15 I'm actually off the next 2 days, but I can definitely look it up on Monday.
**Juliano Costa | Datadog** 15:18 Yeah, no, if you're off, then, don't worry, I'll check that.
**Donal O'Sullivan** 15:24 I probably can't review anymore, though, because I have pushed changes as well, so maybe it's better if someone else.
**Shenoy Pratik Gurudatt** 15:31 Yeah, happy to review it again.
**Donal O'Sullivan** 15:33 Oh yeah, excellent.
**Shenoy Pratik Gurudatt** 15:34 Yeah, I took a stab, I think I found some issues. It clear already changed, so let me take up that as well.
**Juliano Costa | Datadog** 15:43 Awesome.
And another thing that I have on the list here was a PR that came in from Citel, today.
And it's, so it adds… a Prometheus Java library to the ad service.
And then exports, slash metrics, and add a custom counter to… to the ad service. I have the link of the PR on the SIG meeting notes, if you want to take a look.
The thing is, I'm not a Prometheus guy, this is the OpenTelemetry demo.
I… I was… I really wanted to hear your opinions on that, but I actually pinged Seville, and he gave me his perspective, so I want to read what he said to me, and then we can… I want to hear your opinions. So… I told him, hey, I'm a hotel person.
I don't like Prometheus.
And he's like, yeah, I understand, but all this work is to help people migrate off Prometheus. You introduce the hotel pipeline, scraped Prometheus Exporter with the hotel collector in the most backward-compatible manner possible to move fast.
Then you incrementally replace Prometheus exporters with hotel native solutions, and then you replace the Prometheus exporter, by the collector native receivers, and, replace the Prometheus client libraries with custom metrics by Autel SDKs itself. So it's like a process, and then adding that to the demo would just showcase a part of that, and also showcase the integration with Prometheus and Autel.
So, there is advantage of that, and we know that the community uses a lot Prometheus, so maybe it's a good addition, and yeah, I'll open the stage. I talk too much.
**Shenoy Pratik Gurudatt** 18:07 I like the effort here. It makes sense, interoperability between Prometheus and Rotal Collector. You have a receiver. People have their application metrics sent over to Prometheus via slipping endpoints today. If you just put total collector, you can send it to any other backend now.
Okay. I think the user's fair there, yeah.
**Donal O'Sullivan** 18:35 Yeah, no, I'm… yeah, I'm of the same opinion. Like, it… it sounds good, like, it's a way of demonstrating how you can kind of migrate off of, like, legacy ways of doing things to, like, pure hotel, so, makes sense.
**Juliano Costa | Datadog** 18:47 Oh, I think some folks from, from the Prometia side would be mad if they hear the legacy.
**Donal O'Sullivan** 18:55 It's been around a while, so…
**Juliano Costa | Datadog** 19:01 Okay, cool. Yeah, nice, okay.
And then I see that we have a new item here, adding host CPU metadata to upstream Collector, and show… via Grafana dashboards, we can update resource detector processor. I don't know who I did that?
**Donal O'Sullivan** 19:21 I… I… I added that one. It's only a… it's a very small change, it's just something we've done, at Elastic in our fork, so it's just showing, host metadata and CPU metadata on a dashboard, and I was hoping not to have to update the upstream collector But it's something I had to do, just to get that data to populate dashboards. It's very straightforward, it's just showing, like, host information, like, what OS you're running, that kind of thing. And then there's also, like, CPU metadata, so, like, the make and model, that kind of thing. And you can just show it on your… on your dashboard, so… We've done that.
downstream, I guess, on the Elastic Fork, and we're just showing that on our Elastic dashboard, so I was just wondering, is that something we'd like to do?
Upstream. It's quite a simple change, it's quite small. Now, it will be showing it… I've already done it locally, and it requires just a small config update to the hotel collector, and also a small change to the Grafana dashboards, but… Nothing big.
**Juliano Costa | Datadog** 20:26 Bob.
Sounds good to me, yeah.
**Donal O'Sullivan** 20:31 Cool. I can open an issue and show, like, just pictures, and you guys can kind of decide from there if that probably makes more sense.
**Shenoy Pratik Gurudatt** 20:39 Yep.
**Donal O'Sullivan** 20:41 Thanks.
**Juliano Costa | Datadog** 20:42 Cool. Hi, Pierre.
**Pierre Tessier** 20:50 Hello, sorry I'm impossibly late, but, this will be the last time, because we had a… had a customer conflict office hours that… brand, weekly.
I appreciate my open source contributions, but I still need to make a living.
**Juliano Costa | Datadog** 21:07 Cool. Yeah, we, we, I already, brought to, to Donal and Shanoi, the thing about the, the layered Docker Compose files, and, Shanoy said that he, he will take a look later.
**Pierre Tessier** 21:22 Awesome.
I think all the changes are in there.
please let me know. One thing I did play around with, I noticed testing does not work well.
there was some problems around MakeTest. If you run, like, the run test, whatever it is.
I think we're also talking about redoing the whole testing framework.
So, I don't know if we want to fix that or not, or if we want to fix it with the testing framework, we do.
**Juliano Costa | Datadog** 21:52 Can I…
**Shenoy Pratik Gurudatt** 21:53 I think we're good.
**Juliano Costa | Datadog** 21:53 Right there, I know.
**Shenoy Pratik Gurudatt** 21:54 ignore that older test funnel.
Study a language.
**Juliano Costa | Datadog** 21:57 No, no, go ahead. I just wanted to say that you open a PR sending a test proposal there.
**Shenoy Pratik Gurudatt** 22:04 beep.
**Pierre Tessier** 22:05 Yeah, I've seen. That's why I'm like, I don't really want to fix testing on this new Docker Compose Layer thing, because we're ripping it out anyways, and we're replacing it, so…
**Shenoy Pratik Gurudatt** 22:17 Yeah, I agree. I wanted to not update it in my PR as well. I'll just remove it in one PR that cleans up the older tests and everything that are stale objects there in the compose.
And then make files.
**Pierre Tessier** 22:32 Okay.
**Shenoy Pratik Gurudatt** 22:34 I also want to get your PR in as soon as possible, because Felix has a big PR that has some services, and then my inventory test depends on these. It's better if you can just move your stuff in now, and then we can replace all of it.
**Pierre Tessier** 22:49 Yes, please, because the merge conflicts are getting annoying.
**Juliano Costa | Datadog** 22:56 Well, one.
**Pierre Tessier** 22:58 I'll be around, Chanoi, if you have any problems with it, tag me in Slack as well. GitHub notifications don't really hit me as quick.
**Shenoy Pratik Gurudatt** 23:04 Okay, yeah.
**Pierre Tessier** 23:05 send me in Slack and be like, hey, Pierre, I've noticed this, and I'll get on it. I do want to get this wrapped up and finished as well, so we can… Get onto a better way.
**Juliano Costa | Datadog** 23:16 One thing that I… that I want to ask as we are here, so… Felix is, adding this agent deck AI thingy. Should we… Remove the recommendation? Not the review, the product reviews?
Service as a whole.
**Pierre Tessier** 23:43 Kind of redundant now, isn't it?
**Juliano Costa | Datadog** 23:45 Yes?
**Pierre Tessier** 23:47 I like red diffs.
**Juliano Costa | Datadog** 23:51 Yeah, that would change the UI as well, the front end. Oh, man, I don't want to touch the next game.
**Pierre Tessier** 24:00 It's all delete code, though, for what it's worth. Everything's a delete.
**Juliano Costa | Datadog** 24:06 But…
**Pierre Tessier** 24:07 Yeah, it would be… we should have a follow-up PR to remove product reviews.
**Juliano Costa | Datadog** 24:13 Okay, but then first we get, Felix Piara in. I mean, first, first we get the, the Compose file, in, and then, Felix… And then, yeah.
**Pierre Tessier** 24:29 And then we could talk about removing product reviews. Did you talk about cutting a 3L?
**Juliano Costa | Datadog** 24:36 Yep.
Okay. So, then in Trio, we can announce the Agentech demo, we can announce, profiling.
we can announce the big renaming and the addition of Weaver as well. So, I think.
**Pierre Tessier** 24:50 Lots of changes.
**Juliano Costa | Datadog** 24:51 Yeah, I think it… kind of demands at 3.0. It's a lot of breaking changes.
**Pierre Tessier** 24:59 Yes, yes, I agree. Yes, braking changes is true.
Awesome.
Awesome. Good to see that.
We still have a lot of variable renames to do, right? Or variable, attribute renames to do, right?
**Juliano Costa | Datadog** 25:15 Yep.
**Pierre Tessier** 25:16 Did anybody from Bloomberg join this call?
**Juliano Costa | Datadog** 25:18 I'd… I don't think so…
**Pierre Tessier** 25:21 They are gnawing at the bit to work on those, so I'm encouraging them in their mentorship program to work on those PRs. They feel, like, pretty… Fairly trivial, and it gets them their contribution experience.
**Juliano Costa | Datadog** 25:36 Yeah.
So, it's a guy… Florian?
**Pierre Tessier** 25:40 for you? Yep.
**Juliano Costa | Datadog** 25:42 I don't know from where he is.
**Pierre Tessier** 25:44 He's from Bloomberg.
**Juliano Costa | Datadog** 25:45 It's good.
**Pierre Tessier** 25:46 Internally, they're gaming who gets the most contributions, I think. I'm not sure, but he's definitely winning that.
**Juliano Costa | Datadog** 25:54 That's great.
**Pierre Tessier** 25:55 Oh.
**Juliano Costa | Datadog** 25:55 This is good. So, if he is from Bloomberg, I'm happy that this is actually working.
**Pierre Tessier** 26:02 Yes, yes. We… were you on that call, Juliana, where we demoed OpenTelemetry to them?
**Juliano Costa | Datadog** 26:08 Yeah, yeah.
**Pierre Tessier** 26:09 Yes, it was very well received.
**Juliano Costa | Datadog** 26:12 Awesome.
**Pierre Tessier** 26:13 thereafter has been fantastic, so I'm… I'm now looking at the OpenTelemetry demo as a good way to get people into OSS contribution as a whole.
Right? There's a lot of low-hanging fruit.
There's not a lot of complicated code to do.
Necessarily. It's a great spot for people to get their feet wet.
dope.
**Juliano Costa | Datadog** 26:32 And once they are in the project with easy CLA signed, they know the flow, they know the people, starting contributing to other repos is…
**Pierre Tessier** 26:44 And sometimes, like, you fix something in hotel demo, and it turns out it's an upstream SDK problem, right? We run into those often enough, and so then you get the experience of going upstream.
So I think it's a great launching board, and we should probably… I don't know.
when this program is over, we should probably think about maybe making a blog post about it, or maybe even just documenting it. Like, hey, look, if you're looking to OTEL as a way to get into OSS contributions, here's a great SIG to get started with.
**Juliano Costa | Datadog** 27:12 Huh.
**Pierre Tessier** 27:13 You know what I mean?
**Juliano Costa | Datadog** 27:14 Yep.
**Pierre Tessier** 27:15 Not sure, but that's been my feedback on that so far. There's a lot of celebration going on in that channel.
**Juliano Costa | Datadog** 27:22 Awesome.
Yeah, I agree.
Cool. Yeah, I think we… we went through, the things.
**Shenoy Pratik Gurudatt** 27:34 Juliana or Donor, do you want to take another stab at the telemetry test sphere?
to review it.
**Pierre Tessier** 27:43 I can review it as well.
**Shenoy Pratik Gurudatt** 27:45 Yeah, if you… if you have some changes, for sure.
**Pierre Tessier** 27:49 I'm getting the cycles. By the way, my AI finally just finished on the, the dependent bot PRs. Two of them failed.
3382 and 3378 failed. So, that'll require deeper investigation.
**Juliano Costa | Datadog** 28:02 Yeah, I… I… I mentioned last… on our last sync.
the Rust release. So we got dependable bumping all dependencies, but Rust released just for core, and there was… we used a contrib, dependency as well, and the contrib was relying on the old SDK, so we had a SDK conflict.
So, I liked the demo because of that. Then I went to the guys from Rust and said, hey, can you guys cut a release here? Like, please?
So, yeah, I'm the annoying one.
**Pierre Tessier** 28:42 I… anyhow, I will… I'll get the other four approved, I'll tag the other two, I'll make comments on it, we'll see if we can figure out what they are.
whatever. It's… a testing framework will make this way better, because the testing framework will catch these for us.
Yep. Right?
**Juliano Costa | Datadog** 28:58 And then we can…
**Pierre Tessier** 28:59 It's working inside the PR.
Yep. So, Chanoy, I want to stop using this AI thing, which pissed me off last night.
For what it's worth, it was gonna run all 6 PRs last night, but I was using that session. I said, no, don't, right? I know we've got one minute left, so I said, run us later. And it's scheduled to run it later, at 4 AM, which is fine.
Except it ran it in Claude's Cloud, which is also kind of fine, I guess, but Claude's Cloud, when a session ends, it deletes all its temp files, and it wrote its output into the temp folder.
And I was like, what the fuck did you… why would you do that? I woke up this morning, I'm gonna have a report and start merging PRs? No, I woke up this morning to an empty report. It was great.
**Juliano Costa | Datadog** 29:47 God, awesome.
**Pierre Tessier** 29:49 Yeah, man.
**Juliano Costa | Datadog** 29:50 So, thanks everyone for joining. Yeah, so, see you all in the next one.
**Pierre Tessier** 29:57 Awesome. See you next week.
**Juliano Costa | Datadog** 29:59 I'm curious.
**Donal O'Sullivan** 29:59 Guys.
**Shenoy Pratik Gurudatt** 30:00 Okay.
