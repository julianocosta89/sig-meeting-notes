SIG: Communications SIG
Date: 2026-04-28
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/8A3bmQWs8NsE4wDswg0Pf7p1Kb52zpTaNudzu4522j67P5RLaUOSauVJz8cY4Rao.ZISLfPAgubMIcDzm
============================================================

## Zoom Recording Transcript

**Vitor Vasconcellos** 00:52 Yay.
Oh my god.
**Patrice C (CNCF)** 00:59 I am good, how are you?
**Vitor Vasconcellos** 01:01 I'm good. Hi, Tiffany, that's it.
**Patrice C (CNCF)** 01:08 Hello, everybody.
**Tiffany Hrabusa** 01:11 Hello.
While we're filling the agenda. Prateek, how is your new job going?
**Pratik** 02:02 Actually, yeah, I'm going with the onboarding process and a lot of fast pace, because of its startup India and startup working in observability.
Actually, they are, the company is something related to, like, a log… about a log section of the observability, like, a user can query using a SQL query, and… to collect the logs from their injection and collector.
So, something like a user can use a natural language to collect the recent logs using the natural language and SQL queries as well for the SREs and Yeah, the DevOps engineer.
And actually, it's a startup right now. It's growing seed stage. I just got funded last year. So, actually, they are very fast-paced.
So, a lot of work.
responsibilities. So, actually, I wasn't able to get much of time for contributing in hotel from last one to two weeks. I was a bit busy about this onboarding process, and… new work culture. So this is my first job, I was a bit overwhelmed.
Yeah.
**Tiffany Hrabusa** 03:12 Yeah.
**Pratik** 03:12 It's going well.
**Tiffany Hrabusa** 03:14 Completely understandable, and we will welcome you back as a contributor as soon as you have time.
**Pratik** 03:23 Yeah, sure, I will.
**Patrice C (CNCF)** 03:32 I guess we can get started?
Feel free, anybody, if you wanna, there you go, add some items.
Let me kick off this party.
And maybe just invite feedback on the agent skills that we've been setting up. Actually, maybe let me start with you, Vitor. You have a visible PR in the queue.
And I've been keeping you busy with Feedback.
that, agents have been generating kindly for me. I'm passing on to you, but how's that? Is there… Do you think it's close to be done?
**Vitor Vasconcellos** 04:23 Yes, it is. I was just taking a look at the last… reveals.
with an S at the end. And I think I'm gonna… I'm gonna ask Claude for another round of reviews, but I will push the commit and… We can… Okay.
Can take another look, but it is close to… I can get this done in the next couple hours.
**Patrice C (CNCF)** 04:52 Yeah, I've been doing that as well, to use one, top model to review the works of another.
My main question, which, as I have been writing Skills was to avoid the… To keep our documentation dry.
And so, in the references section, I don't know if you read… read… Through the… yeah, okay. So… what's the answer there? Do you know? Can we avoid the repetition? Or I think you might even have said that There is no repetition.
**Vitor Vasconcellos** 05:31 Yeah, we… there… there are some repetitions we… we could avoid. I'm trying to… to set a… Source of truth.
But I don't know if we can have it living outside the skills directory.
And… If we can, which would be great, we can… Move some of those instructions to our… Slash site section, and we can just… Add the references on the skills to read from the slash site section.
But I don't know if we can do that, or if that will work with Copilot or Cursor, for example, with other… other agents.
I will give it a try on this… on this branch I'm using, and if we can do that, we… we can… Avoid repeating it, some… some of those instructions or rules.
**Patrice C (CNCF)** 06:32 That would definitely be my preference. I think… what's nice about the official Claude skills is that you can slash command, you type slash, and it lists the skills that are available.
Under VS Code as well.
I… from my research of the official documentation, they kind of say don't do that, but I think if we have an absolute… Url to our site.
Documentation page, a specific link.
I would hope that it would be able to traverse that, and thanks for experimenting, or give it a try, and… I'm eager to see it.
**Vitor Vasconcellos** 07:15 Thank you.
**Patrice C (CNCF)** 07:16 If it works.
**Vitor Vasconcellos** 07:17 I'll let you know how this goes, but… This is looking good so far. I have used that skill, especially the triage skill, to find some issues for the Bloomberg, the mentorship program, and I think… I think I can say 90% of the issues, the results were accurate, actually, so…
**Patrice C (CNCF)** 07:43 Good.
Good, sounds good.
**Vitor Vasconcellos** 07:46 They save us a lot of time, and…
**Patrice C (CNCF)** 07:49 triaging.
**Vitor Vasconcellos** 07:51 Yep.
**Patrice C (CNCF)** 07:53 Yeah.
Good, thanks.
I've been experimenting with what I've called maintainer skills, which is pretty much maintainer documentation for us, but… hey, why not call it a skill? But… it's also aimed at having the agent do the work, and I've been experimenting with two of these maintainer skills For resolving issues with the ref cache.
as you know, this is something that just happens every day. And, so far, I've been successful at asking Cursor to, Execute a maintainer skill.
And it's been doing it… I don't think I've reached 90% success rate yet, because as you know, rough cache updates are… can be a bit tricky. You get… Servers going down, like.
**Vitor Vasconcellos** 08:50 Yeah.
**Patrice C (CNCF)** 08:51 javadoc.io that is returning 500.
errors. But anyways, it's, it's, hopeful. It's… it seems like it's… it's… Gonna be beneficial for… us as maintainers, and useful to… ask agents to do.
**Vitor Vasconcellos** 09:16 Yes. No, this, I've seen some updates in the ref cache workflow, but… I'm still not up to date with that yet. I still haven't caught all the… all the updates, and… No problem. But it is looking… it is looking good.
**Patrice C (CNCF)** 09:36 Anybody else?
Wanna comment on the skills, whether you've tried, not tried?
**Tiffany Hrabusa** 09:45 I haven't had a chance yet to try them out, but, your Slack post is a save for later item, but I keep staring at the little green notification, so… I will try them out soon.
**Sophia Solomon** 09:59 Yeah, same here. I want to try them out, but yeah, I've been so busy. Is this, like, conference season? Like, what's going on? But I want to try it out, but yeah.
**Marylia Gutierrez** 10:14 To give a different answer. I don't want to use it, I refuse to use it, because everybody wants to use it, so I just feel like somebody has to do the opposite. Like, no, I just refuse.
Okay.
**Patrice C (CNCF)** 10:25 Thank you. Add a bit of diversity.
**Marylia Gutierrez** 10:28 Yes, it was…
**Patrice C (CNCF)** 10:33 Okay, move on to the next, item.
as some of you are aware, I brought up a topic of a possible showcase page. I haven't… I don't have any… more feedback to provide, so… I mean, that's all I guess I'm gonna say for now. Once I get more details.
Which hopefully is just going to be a confirmation that we can go ahead with that.
then I'll… I'll publish on our… approvers Slack first, and Probably the Seagan user folks are gonna… Be involved, as well.
**Vitor Vasconcellos** 11:18 Yeah.
**Patrice C (CNCF)** 11:19 That one's.
**Vitor Vasconcellos** 11:21 Oh, no, no, go ahead.
**Patrice C (CNCF)** 11:23 No, I was just saying, next. Go ahead.
**Vitor Vasconcellos** 11:27 But it's… Marilla was going to talk about this same topic, or is it another one?
**Marylia Gutierrez** 11:35 No, no, keep the same software. Yeah, go ahead.
**Vitor Vasconcellos** 11:38 Yeah, I was just wondering if we could have, like, a plan B. I don't know how… Much effort the… That… that is going to take on the… On the showcase.
I know, I got, I get your point on… and I would like to have something that we could… use it to… so that people can see, hey, this is what you can do with OpenTelemetry.
But as long as we can't tie, or… at least can tie it with any… any vendor. I was wondering if we could have something neutral like, we had? Is… Proposo… a couple months ago, I think, of someone who was trying to donate this project that is intended to be… Okay, this one that is intended to be, like.
A front end for development proposed… proposed.
I was wondering if we could have something like that, and… because… We also… We also want to have a place where we can see.
the signals from… from our documentation, or from the explorer, and the collector we are setting up, so… I was wondering if we could have… Yes, yes, Sophia, like… our, our… Our tooling to visualize the data, and… Perhaps… get started with that. I don't know if this is, like, this could be a Plan B, or this could be something Neutral, as neutral as possible.
**Marylia Gutierrez** 13:29 So yeah, that was one point that, like, whenever people usually… want to donate visualizations usually gets rejected, because that is not the proposal of OTEL, so having, like, an official visualizer that's not gonna happen. I don't know if it was this one in particular, but I remember one of the donations, if you look at the actual code, is pretty much just AI, and we don't want to accept something, because if somebody is donating, actually.
The technical review has to read all the code, the due diligence, so we are not going to spend time doing all of this in a project that's The person is not even they committing the time itself, because then we have to find people to be liaison, we have to be people for maintain, and things like that.
So, having this group, that is, like, a requirement, to approve, and also because that is not a part of hotel, I don't think there is any plan to have any, like, official, like, visualization of those, and I don't think that is something that the GC or DTC will accept any time soon.
if you have, like, things to visualize, because one thing that I'm thinking about to showcase, it is which direction it might take, because, for example, we do have the hotel demo that is showing people how you can visualize data, that's exactly what the demo is about.
and the demo is, like, sending a lot of data, and then you can connect to, like, Jaeger, or take, like, Grafana, or you can, like.
I don't know, so pick other vendors, so there is already a way to do this, I think they are… might be working. There is one people that people ask a lot, I have, like, a live version of the demo, so maybe this project could be a collaboration with the demo. If it is just about explaining how to actually do the architecture, then could be a… Project combined with the blueprints, because then you can show, like, how to actually set it up and everything, and then use the demo to collect.
Because I… I don't want to, like, someone here dedicate a lot of time to this.
And it's just, like, rep… like, repetition of work. If we were, I have a whole SIG focus on, like, showcasing, how a hotel works.
**Sophia Solomon** 15:40 Okay, yeah, that makes sense. Thank you.
**Patrice C (CNCF)** 15:48 Pico, did you wanna… were you gonna add something else?
**Vitor Vasconcellos** 15:52 Nope, nope, I was just…
**Patrice C (CNCF)** 15:53 Okay.
**Vitor Vasconcellos** 15:53 Agreeing.
**Patrice C (CNCF)** 15:56 So the idea of the showcase is a bit… is… Well, prior to your answer, Marilla, I was going to say, well, if there's… if there are open source dashboards out there and backends and visualize… visualizers, fine, they could be in the showcase. And the whole point about the showcase is not to give SIG comms.
or any… SIG under OTEL more work to do, it's to have a showcase page.
Where others, including vendors, So, the area where… and again, this is just my understanding as I'm… Learning what other projects have done.
This is not the official position of the CNCF yet, until I confirm.
But the idea is, to showcase… All vendors who wish to participate in this As opposed to necessarily being selective. So it's… it's a showcase page which is open. In that sense, it's vendor neutral, because we're not choosing to bias any particular vendor.
And the idea was to have Something that is live.
And if multiple vendors can get… can buy into this, then it's nice because it offers An incentive for vendors to have a functional version of, dashboard into the demo.
But of course, that means somebody has to run the demo somewhere under some circumstances. Who should do that? Should it be vendorized? Should it be a collective?
Those are all good questions.
So, yeah, that's my thought so far.
**Marylia Gutierrez** 18:00 Yeah, so I think, like, the idea is good, but I'm just thinking about if we actually have vendors that have time to do this. Because, for example, the demo. I don't see a lot of vendors just going in and putting the connection to their backend. They can do this today, but they are not really doing, so I feel like it would be a similar situation.
On here, that people might not necessarily join.
**Patrice C (CNCF)** 18:28 Agreed, I don't know.
It may be a question of putting up the page, seeing who…
**Marylia Gutierrez** 18:33 Yeah, same through.
**Patrice C (CNCF)** 18:34 And if there's no interest, will you take it down?
**Marylia Gutierrez** 18:37 Yeah, there's…
**Patrice C (CNCF)** 18:39 Tiffany?
**Tiffany Hrabusa** 18:42 I'm not sure that I fully understand.
The loop process that you described?
So… For the demo part, that would be… like… showing some kind of telemetry and some kind of incident using the hotel demo, and then the idea would be the vendors use their own dashboards to visualize the data that came in from that incident.
Is that how I'm… Yes. …understanding this? Okay. And so then… The idea is that somehow there's… of… is it a video of the demo running on a loop? I'm just not clear on what would be the central part, and then how are the dash… like, are we just writing about the The… the scenario, the incident, and then the dashboards visualize.
**Patrice C (CNCF)** 19:39 So… The A-plus version of what I'm envisioning is live. It is not a video. It is not a write-up.
having a write-up with screenshots is probably better than nothing, but the idea was to have something live.
And that, to me, was inspired in part by, the demo we had?
Michael's?
Is that his name? Who put together a demo that runs on AWS, and what's nice about his is that it's interactive, and you can say, well, simulate this Failure. Simulate this failure.
Which is nice if you're running things on your own, and we can have a link to that.
For users who want to run it locally and see… see that sort of thing.
I don't think it's feasible for something that's available online that anybody… that you can have live feeds into.
There, I think we should have a loop where it cycles through scenarios.
Or people can queue up scenarios, and then we could… we just have a queue of scenarios that people might want to see.
And then the dashboards are live.
**Tiffany Hrabusa** 20:56 Okay.
**Patrice C (CNCF)** 20:56 And…
**Tiffany Hrabusa** 20:57 When you say.
**Patrice C (CNCF)** 20:58 another reason.
**Tiffany Hrabusa** 20:58 scenarios, that's, like.
we're showing, like, the demo website, like, the shopping website, and some, like, some… I'm just not sure what I'm… what is actually looping and what we're showing. That… that's my brain, not computing, so…
**Patrice C (CNCF)** 21:15 So, whether there is a website somewhere of the demo that is accessible or not, to me, is secondary. It's as if there is that service somewhere that's running, and then the loop is of scenarios of 3 buyers logging in.
Somebody doing something with their cart.
There's a back-end failure.
So that's what would be… looping and live. And potentially, we as maintainers or whoever of us want to interact with it. There may be ways of interacting with it, but… Does that make sense? So it's not necessarily a live storefront that people can go and do things, it's… the simulation of it. So, the demo, but that's being driven By us, by our script, by…
**Tiffany Hrabusa** 22:11 But would we show any of that on the showcase?
Or would it just be the dashboards that are reflecting?
**Patrice C (CNCF)** 22:18 I was thinking just the dashboards.
**Tiffany Hrabusa** 22:20 Okay, that's… that's where my brain was not going. Like, what… what are people seeing on the showcase page? Okay, that makes sense. Okay.
Thank you.
**Marylia Gutierrez** 22:29 I think…
**Patrice C (CNCF)** 22:30 to the showcase.
**Marylia Gutierrez** 22:30 One way that you can do is just, like, as a, like, proof of concept, is, like, okay, getting the demo, then right now can send to both, like, Giger and Grafana, and have this running somewhere, and then that page would be, like, see in Jager, see in Grafana, and whenever the person clicked, they would see that particular dashboard.
So, this is a way that, first of all, if whoever's working on this from here doesn't have to create everything from scratch, but you have to basically Since you already have the demo, have that running, and just to see if it works, see if people are interested, see if other vendors want to add their stuff, and then if yes, then you can… I don't know, Go from there, pretty much.
**Tiffany Hrabusa** 23:15 Okay, thank you for taking up more time.
**Patrice C (CNCF)** 23:17 No, it's fine. Actually, I'm glad we're fleshing this out, because it's clear in my mind, but if it's not clear in yours, then we're talking… at Crossroads, let me, show you… Where am I going?
Have you… did you check out the Flutter showcase?
Why am I not finding this?
**Tiffany Hrabusa** 23:52 I did take a look at it, yeah.
**Patrice C (CNCF)** 23:54 Okay, so… Admittedly, it's not exact… not exactly the same thing, but… Since we'd be having a live element.
Okay.
Anymore?
Questions or comments?
Thank you for the discussion.
So, Vitor, if ever we do get… access to surfers somewhere. This might be one of the uses, in addition to get… getting our own collector.
**Vitor Vasconcellos** 24:33 I'm still waiting on the… on the response to… to get access to Cloudflare, so… So far, I have no updates on that now, so…
**Patrice C (CNCF)** 24:44 Thank you.
Marillia.
**Marylia Gutierrez** 24:49 Well, this one is the one that I started the… on the thread. I was like, well, since we're actually gonna meet in person, might as well just ask them. Yeah, it's because, like, from yesterday… I think, yes, when that PR got merged, I deleted the tools folder. Now it's just the links on the community repo that is just… Giving that error.
So I was like, does that mean, like, the tools don't exist anymore? So I just, like, remove that sentence completely, or do I point people to, like, the package? I was just like, what… I wanted to fix that error, but I don't know to what.
**Patrice C (CNCF)** 25:23 And your question is understandable, because we don't… I even had trouble finding a reasonable link other than the code excerpt homepage. So, as I mentioned, if… if you… If you're kind of in a hurry and you want to fix it right away, use that homepage. Otherwise, what I'd like to do is find a suitable place under our slash site.
documentation.
which I had started looking just before this.
But I'm…
**Marylia Gutierrez** 25:57 The thing is that, because if you tell me that it's something like, oh, I'm gonna have it done, like, in a couple of days, I don't mind waiting, because people are, like, noticing that it's not a real error for the PR and emerging right away, but if you're telling me, like, oh, it might take a couple of weeks, then I would just put that other link.
**Patrice C (CNCF)** 26:13 If… if you're willing to wait a few days, I'm… I can… Find a suitable home.
**Marylia Gutierrez** 26:20 Okay, cool.
Awesome, yeah.
Then, yeah, happy to wait, and then whenever you have, I can update that.
page.
**Patrice C (CNCF)** 26:28 Okay.
Do you… could you open up an issue?
For that, if there isn't already an.
**Marylia Gutierrez** 26:35 Yeah, I can open, yeah.
**Patrice C (CNCF)** 26:36 over the, hotel.io repo.
**Marylia Gutierrez** 26:41 Oh, on the Hotel de Rio? Okay.
**Patrice C (CNCF)** 26:43 Well, because the ask is to find a suitable Boom for… Can you lie?
**Marylia Gutierrez** 26:50 Yeah, yeah, got it.
**Patrice C (CNCF)** 26:51 On our website, that's why.
**Marylia Gutierrez** 26:53 Yep, perfect.
**Patrice C (CNCF)** 26:59 Anybody else?
**Tiffany Hrabusa** 27:09 I just had an FYI there that I'm out Friday and next week.
That is relevant because I'm going to postpone any blogs until I get back.
There are two more drafts still waiting to be reviewed.
And I may or may not get to them this week. I have a lot of other stuff to… accomplish before… before Friday. So, I'm just gonna postpone everything, so there won't be any social media, that you have to do, Vitor, or, any merging of blog posts next week.
**Patrice C (CNCF)** 27:49 Thank you. Heads up.
Anything else?
If not, have a great rest of your week.
We'll see you online, or at the next meeting.
**Tiffany Hrabusa** 28:16 Bye!
**Vitor Vasconcellos** 28:16 you.
**Patrice C (CNCF)** 28:17 Take care, everybody.
