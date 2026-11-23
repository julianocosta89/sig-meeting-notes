SIG: Community Demo App SIG
Date: 2026-11-18
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Shenoy Pratik** 00:43 iPhone.
Wait, yo.
Voice is a bit muffled, I'm not sure.
If it is my issue or something else.
**Som Banerjee** 01:00 So, am I too quiet?
**Shenoy Pratik** 01:04 No, it feels like a microphone is way away from your, like,
**Som Banerjee** 01:09 Alright, okay.
**Shenoy Pratik** 01:10 Yeah.
**Som Banerjee** 01:10 That makes sense, so maybe… Okay, how about now?
**Shenoy Pratik** 01:26 Oh, it's much better. Clear.
**Som Banerjee** 01:28 So, for some reason, it was latched to the computer microphone, I think.
Yeah, yeah, I, I, I, I, I just, happened to… Take a look at the demo app last month.
And, I think it's a really cool app.
It's, very close to my use case. I'm actually developing an Agentic, search for a little CVC e-commerce company.
Who basically know how to search, but want to make it agentic. And, what I realized when I broke into their code is, they've got very little by way of telemetry.
And, personally, I hadn't really dealt with, setting up telemetry a lot, so I'm… I was never the guy that, you know.
Took the decisions about the telemetry backend.
But yeah, I kind of, had to start digging into it, and then I found, Hotel Demo Repo, and I think it's a beautiful app, and it's kind of… I'm also very delighted that it's so well adopted.
That everybody speaks on those terms, you know, even, let's say, a company like Datadog, who, I think, traditionally been unaligned.
So yeah, I'm, so I, I, I actually tried out your Agentic, layer, and, I thought I found a few bugs there. I, I raised, some issues, and I saw that they haven't been attended to in a month. Now, you know, I could just be wrong in terms of, you know, maybe I'm doing something incorrectly?
But I thought maybe, you know, I'm just gonna, check with you guys,
**Shenoy Pratik** 03:45 I see. So, is your GitHub handle super slow?
**Som Banerjee** 03:48 That is correct.
**Shenoy Pratik** 03:50 Okay, yeah, I didn't get time to look into these.
We're running low on maintainers right now. The other maintainer is out here, not well.
**Som Banerjee** 04:00 Hmm.
**Shenoy Pratik** 04:01 I discovered it to a man.
I see, Antonin is here. Hi.
So for this particular.
**Antonin Bruneau (Tsuga)** 04:09 Blue.
**Shenoy Pratik** 04:09 issue, yeah. Yeah, and just to give a brief on what we are discussing, Zoom has some… Issues raised for, the agent Telemetry example that we have in the demo.
And let me share the three issues.
Let me know, Sam, if you have more issues.
I just got.
**Som Banerjee** 04:33 No, no, I just, you know, wanted to… so, like I was telling, Shenoy, I… I recently found this demo. I found it really cool that it's a common language, kind of, all, telemetry backends.
speaking, so I dug into it, and I… tried it out, I… I think I found a few.
Loose ends between services.
Now, I might just have set it up all wrong, but, yeah, I thought I'll… Check in with you guys.
**Shenoy Pratik** 05:11 Yeah, I'm just looking through it. It's, get cart sends user session ID, so card looks empty.
Oh, I see it's missing some parameters, is it?
**Som Banerjee** 05:28 I think it's a… it's, it's, you know, the service expects, one parameter, and the request has a different one.
The request seems to have user ID, and the service expects session ID, or is it the other way around?
So it's a pretty easy test, and an even easier fix, actually. I mean…
**Shenoy Pratik** 05:54 Yeah, the SIG would be even easier, to be honest. But I think if you have the bandwidth, feel free to put out PRs, otherwise I can look…
**Som Banerjee** 06:06 I didn't do that.
**Shenoy Pratik** 06:06 And then get it done before next week as well.
**Som Banerjee** 06:10 Oh, I'm… I'm running a little fix already. I mean, you know, all the three fixes are really little, so I, you know, I just didn't want to raise a PR and, Sort of, consume more bandwidth in you trying to convince me that that's not the right thing to do.
**Shenoy Pratik** 06:29 And this time, we are more happy to have PRs in.
Along with the issues, because that's what people are doing. Okay.
That's what, we have seen, like, after the Agentic stuff boomed. We have a lot more PRs coming in.
**Som Banerjee** 06:47 I know.
**Shenoy Pratik** 06:47 It's difficult for us to also, like, keep up with the pace and everything, because.
**Som Banerjee** 06:53 I know.
**Shenoy Pratik** 06:53 Everyone has their own thing going on in parallel. So…
**Som Banerjee** 06:56 Yeah, I'm sure.
**Shenoy Pratik** 06:57 I…
**Som Banerjee** 06:57 Dealing with a lot of slop there.
**Shenoy Pratik** 06:59 Yeah, exactly. So it's very difficult to differentiate between an actual PR and the swab.
**Som Banerjee** 07:04 And that's kind of the reason why I wanted to show my human face.
**Shenoy Pratik** 07:09 Yeah, that would be amazing. Yeah, if you have some PRs, I can review them before the next meeting.
**Som Banerjee** 07:17 I do, I do. I will send it in in a couple of days, and probably even ping the Slack channel.
**Shenoy Pratik** 07:27 Also, I had some questions around, The other part that you mentioned about, the e-commerce part and the retrieval part itself.
In the demo, first of all, in the current demo that we have with Agent Telemetry, do you see anything missing in terms of retrieval on your e-commerce project that you're working on already?
The setup that you're working on. Can we add something in the demo?
That can help your use case.
So, we don't want to add a lot of use cases that are not Showing observability, or, like… Helping others learn about observability of agents.
**Som Banerjee** 08:14 I know, yeah.
**Shenoy Pratik** 08:15 But anything that is, like, way out of what we have, but needs to be there for us to understand how agent telemetry works for retrieval, rag-based searches, and other pieces, will be helpful to have.
So, if you have some thoughts on it, we can discuss it. Otherwise, feel free to put…
**Som Banerjee** 08:33 Yeah, yeah, I was… I was just about to jump in with something, and then I realized, you know, that might be a little too narrow, and, you know, I… I think that demo app, the beauty of it is how… Carefully little it does in terms of being an e-commerce app, and you know, being a telemetry app, so I think it's important to protect that, that, minimalism. Yes. So, so, so let me, let me take a look. I have to say, you know, I'm not a, sort of agent telemetry, stalwart, so… so let me also, run it by a few guys I, know make more sense than I do.
And, I will definitely keep an eye for it.
**Shenoy Pratik** 09:23 Correct.
Yeah, I'm just thinking, like, what could be done from my thought process right now, just with discussing and the things that you brought up. In the current agent itself, it does search of products and other pieces. Maybe if we can add a retrieval layer, a minor layer.
As a supplemental thing on top of this.
enhance the existing agent. We don't need a new rack search or something with a different agent altogether.
We just need to have that retrieval operation name inside the current agent.
To see if that can be matched somewhere. And that can again become an example for anyone who is trying to… Build observability platform, or doing an instrumentation for their retrieval engine.
**Som Banerjee** 10:11 Gimme, gimme, something real quick, don't you already have… so, since you have a search, I expected you have some kind of, Embedding store, do you not?
**Shenoy Pratik** 10:27 No, we don't have.
**Som Banerjee** 10:28 So it's a pure keyword-based search.
**Shenoy Pratik** 10:31 Yeah, yeah, it's a dumb search. It's not even, like, a BM25 or TF IDF thing, so…
**Som Banerjee** 10:38 Okay, all right, okay. It's just the word matching, sir. Okay.
**Shenoy Pratik** 10:41 It's just… Okay.
**Som Banerjee** 10:43 Okay, I will definitely, I will definitely, take a look at that.
**Shenoy Pratik** 10:47 Yes.
Thank you. Yeah.
And yeah, apart from these three, if you have any more issues, feel free to… create, the issues. If we have bandwidth, we'll pick it up.
If not yet, it'll just stay in queue for some time until some of our approvers and maintainers get some bandwidth to go ahead and then, work on them. So it's better to have PR as well, and if you think an issue, like, one issue that you find is, like, very minuscule to even raise an issue for, just create a PR, that should be still fine with us, yeah.
**Som Banerjee** 11:23 Sounds good, sounds good. I might just come up on integrating one backend to it, which I'm evaluating, which is, Oodle. I think you have it, you have their blog linked, and I… I believe they've done some internal tests.
But I would really like to sort of, make a repo with, sort of make a fork off the hotel demo with, Oodle, handles on it.
So… so if I get around to doing that, I will, Try to post the link as well.
**Shenoy Pratik** 12:09 Got it. So I think the Oodle, link goes to a blog.
**Som Banerjee** 12:16 Correct.
**Shenoy Pratik** 12:17 And then, have you been in touch with any of those folks?
**Som Banerjee** 12:22 Yes.
**Shenoy Pratik** 12:23 Yes. I see.
**Som Banerjee** 12:24 So, I think that was an internal test they did.
It's not really an open-source demo that people can try out. It's kind of on their backend.
So if… if it's possible to, you know, because I will be evaluating them, I hope I will be evaluating them for a project, so if I get around to doing that, I will definitely set up my own hotel demo.
So if I do that, I will definitely share that, and we can probably discuss if it makes sense to link it.
**Shenoy Pratik** 13:07 Yeah. Adding back-ins, people are very sensitive, and I'll put it that way. Adding more backends, yeah. But what we have seen is if.
**Som Banerjee** 13:16 Oh, no, I wasn't talking about adding more backends, I was talking about integrating Hotel Demo with another telemetry backend.
So, you know, feeding to a different, so through the hotel collector, feeding to a different exporter.
**Shenoy Pratik** 13:34 Yeah, so do you… like, are you suggesting to add Oodle into this upstream demo, GitHub repository, or do you want to just keep it in your fork?
**Som Banerjee** 13:46 I'll keep it in my fork, and probably add a link to the fork.
**Shenoy Pratik** 13:51 I see. So, to add a link to the fork, I would, like, highly recommend… talking to the Woodle guys themselves, and they have a GitHub repo, so if you create a fork, and it works out of the box for Woodle, just talk to them, and then they'll be more than happy to create a repository for you there, and then we can link it.
So that's why.
**Som Banerjee** 14:13 Yes.
**Shenoy Pratik** 14:14 I think every vendor is doing today, so…
**Som Banerjee** 14:16 Yeah, yeah.
**Shenoy Pratik** 14:16 You will get an official repository that way, and then it will be also helpful for those guys.
**Som Banerjee** 14:23 Absolutely, absolutely.
**Shenoy Pratik** 14:24 You're not associated with Oodel, or not, right?
**Som Banerjee** 14:27 I am just evaluating.
**Shenoy Pratik** 14:28 Oh, good.
**Som Banerjee** 14:29 as a customer.
**Shenoy Pratik** 14:31 Okay. Yeah.
Thanks.
**Som Banerjee** 14:35 Yeah, but… but this is… this is the… this is the channel that works perfect.
**Shenoy Pratik** 14:40 Yeah, and if you get the official repo, again, a PR is good enough, we can update that link from a blog to your particular demo.
**Som Banerjee** 14:49 Correct.
Correct.
**Shenoy Pratik** 14:52 Cool.
Yep. Antonin, did you have any agenda items for today? Anything you wanted to discuss?
**Antonin Bruneau (Tsuga)** 15:04 I just raised, PR, not a PR, an issue, to see if I should open a PR for it.
So, in our… because we used this Demo Environment, in our… to demo our product, the Tsuka platform. What we did is, with the ad service.
We… Changed it a little bit, so, To be a bit more representative of how an ad auction would, take place on a… Real… e-commerce websites.
With 3 fakes… beaters.
And it serves two purposes. The first one is… So those betas are not observed, so… or they are observed indirectly, so it's showing how you can monitor third-party services that you query.
But it's also a good way for us to demonstrate more business-oriented use case.
Which is, So you… for a bidder, you need to compute the profile of the user to share with the bidder, so they decide if they make the auction or not.
And that costs you in terms of CPU. And then you have… the beta that responds with an offer, and you need to evaluate if the offer is, worth your money or not. So I combined the information from profiling of the ad service that generates the profile with the value of the bid that the bid has proposed.
And just have a dashboard where I can, compare different kinds of profiles with different revenue. It's all fake data, but it showcased the use cases.
But the question is… Is this something you want to integrate in, the official Reaper, as it adds a new service, which is the BIDER?
service. It modifies how the ad, service works.
So, I wanted to have, some feedback before pushing up here. It's already running in our fork of the The repo, but, yeah, wanted to have, your feedbacks, or the feedbacks of the community before, making the PR to the official repo.
**Shenoy Pratik** 17:52 Yeah, this is interesting, To be honest, yeah. I didn't think of any service like this before, so… It's really nice. One question that I have is, what is the value add that you are giving? I understand the business metrics part.
Where you have a separate type of orthogonal thing coming out. But, By adding this service, is there anything new that the community is learning?
**Antonin Bruneau (Tsuga)** 18:23 So, it shows how to… so it allows you to demonstrate how you can observe an external service that you don't own, and you can't enter.
Through, external traces you make to APM.
So, I can show you…
**Shenoy Pratik** 18:39 It's more like just using client spans, and then creating a dashboard on top.
**Antonin Bruneau (Tsuga)** 18:45 No… well, so this one is the kind of view we provide, where you can see external services being called. It's just spans that, get submitted to external services.
**Shenoy Pratik** 18:57 Yeah.
**Antonin Bruneau (Tsuga)** 18:58 and… So he had those.
**Shenoy Pratik** 19:02 Bidder service is not getting instrumented, but the request you are getting, the request count that you are getting is from the ad service, sending client spans to the bidder external endpoint.
**Antonin Bruneau (Tsuga)** 19:13 Yes.
**Shenoy Pratik** 19:14 I see.
**Antonin Bruneau (Tsuga)** 19:15 And you can check how many requests you make, and how… what's the latency of the bidders.
**Shenoy Pratik** 19:20 So…
**Antonin Bruneau (Tsuga)** 19:20 I also have a feature flag where, one bidder gets low to respond, or times out, and you can alert on that.
**Shenoy Pratik** 19:32 For… we on the open search side, internally, have been doing a similar flow for external dependencies, but what we used was the external LLM API call to showcase.
So, because in the agent itself, we have, the OpenAI endpoint that can come up as an external service.
And that's good enough for the demo, where we showcase the requests going from the, the Python agent.
to OpenAI endpoint, and that OpenAI endpoint is an external service which is uninstrumented.
**Antonin Bruneau (Tsuga)** 20:15 Yep.
**Shenoy Pratik** 20:16 And, We can… we can add a feature flag service to that as well, to mimic something that is similar to this.
Oh, this is just…
**Antonin Bruneau (Tsuga)** 20:26 Okay.
**Shenoy Pratik** 20:27 One of the things that we are doing, we haven't added it into the upstream demo yet, because we are testing few things on the agent side itself.
The agent itself needs a lot of telemetry improvement at this point, to be honest. But, yeah, that's… that's one of the things, that we can do a similar… Showcase without adding a new service with.
What do you think about it? Like, people… are already… Not happy with the demo being so huge right now.
**Antonin Bruneau (Tsuga)** 21:02 No, okay.
**Shenoy Pratik** 21:03 multiple microservices. But, I will share it with all other… look, two questions for you. One is, do you think that the LLM external endpoint is a similar Demo Showcase?
And the second point is, I'll ping all the other maintainers and approvers. Let's get all the feedback from everyone.
It's just my personal opinion right now.
**Antonin Bruneau (Tsuga)** 21:28 Okay.
**Shenoy Pratik** 21:30 So, did you guys tie the, external LLM endpoint before.
**Antonin Bruneau (Tsuga)** 21:38 No, we just use the fake responses that, meetings.
**Shenoy Pratik** 21:42 Yeah, even with fake responses, we can create a similar scenario.
Yep. Yeah. Yeah.
It's just my thinking, but I like the idea. To be honest, like, if you have a lot of space and nobody's… nobody in the community is complaining about it, I'm fine with adding as many services, because we need… multiple things to showcase. Like, it's not easy. Just starting a service and then doing it is also easy to maintain for us as maintainers, rather than having, like, two, three feature flags on one particular service, which is… which can cause some problems.
**Antonin Bruneau (Tsuga)** 22:16 Because the idea was also to show how you can drive business information out of technical data,
**Shenoy Pratik** 22:25 Yeah, that part, I don't think, could be there in the LLM side of pieces.
So that's another additional add-on.
bar.
To have this, business metrics or, like, business data being used.
In sync with the telemetry and other pieces.
**Antonin Bruneau (Tsuga)** 22:43 It's the… what I find interesting in it also is because it, do a cross-analysis across multiple signals. So you have part of the information in profiling, part of the information in spans.
So it's also interesting to… to do the… the… Yeah, the… the NS is based on two types of telemetry.
**Shenoy Pratik** 23:09 Do you have any, like, in the current UI that you showed, on how we use the profiling information?
Because that is not there today in the demo, on how you can correlate something with profiles.
So.
**Antonin Bruneau (Tsuga)** 23:23 Yes, so… For us, profiles comes as metrics, so we can just query… so no, that's the spans.
profile compute cost. So we can just… Compute the profile sample add, that's the name of the function that, computes the profile.
Proof of… that's the… No, that's the metric, that's the profile builder, that's the function that gets called.
And I just add a weight on, A random weight to convert it to dollars, basically.
And, and so you can draft The two lines where you have the beta's revenue, so this is a span information, and you have the qualified cost.
**Shenoy Pratik** 24:20 Gordon.
Yeah, this is… this is something very new, so… It's not there in the demo, I don't see any alternative right now on this.
**Antonin Bruneau (Tsuga)** 24:31 And the ad service generates different kinds of different levels of complexity of profiles.
So you can then compare which one, generates most revenue.
The beta will respond differently depending on the complexity of the profile, but it costs more to generate the profile, so where is the balance between the two?
**Shenoy Pratik** 24:56 Good morning.
Lord.
It's pretty, pretty interesting, take.
Yeah. This particular part of, like, using profiling and then using the span information together, I think is another major value add.
**Antonin Bruneau (Tsuga)** 25:17 About hearing it more.
**Shenoy Pratik** 25:20 Yeah. Do you mind, like, adding these differentiation parts inside the GitHub issue?
**Antonin Bruneau (Tsuga)** 25:27 Saria, I lost your sound for a minute.
**Shenoy Pratik** 25:30 Okay, yeah, what I'm saying is this, using the profile information and the spans data together.
**Antonin Bruneau (Tsuga)** 25:38 Yep.
**Shenoy Pratik** 25:39 Is a value add, and then, adding this external endpoint.
can also be a value add. Maybe you can call out these two details explicitly.
And also third part, like, we are matching business data now, and doing more analytics on top with this new dashboard.
So if you add these 3 major parts that you are adding that can help Demo, it will be also something that… Other maintainers will weigh on when deciding, like, do we need this in or not?
So, yeah, just another comment, or just updating this would be really helpful.
**Antonin Bruneau (Tsuga)** 26:20 Yep. Okay.
**Shenoy Pratik** 26:21 Yeah.
**Antonin Bruneau (Tsuga)** 26:22 Is it okay if I add, two or three screenshots, too, so it's more.
**Shenoy Pratik** 26:26 Yeah, use your dashboards as well, like, you don't need Grafana or something that is in the demo. For the showcase, we just show the value-add with your existing flow, and then we'll see.
Yeah.
**Antonin Bruneau (Tsuga)** 26:38 Okay.
**Shenoy Pratik** 26:39 I am happy, for that business data being correlated with span information. That's my value-add, personally.
But yes, there will be questions on, can we use external… existing external services to do the same thing with new feature flags or some additional information on top.
So, yep.
It would be good to see how others respond.
Awesome. But yeah, this… this is a cool addition, yeah.
It's fine. Do you have it in any of your forks or something, where I can take a look?
**Antonin Bruneau (Tsuga)** 27:15 Yes, it's in our… open, give you the link,
**Shenoy Pratik** 27:26 I'm looking at the Suga… OpenTelemetry Demo.
Is it the main branch, or some…
**Antonin Bruneau (Tsuga)** 27:35 No, it's on, yeah, on the main, on the big branch.
**Shenoy Pratik** 27:39 Oh, I see your last comment there. Okay, perfect.
Yes, I think that should be… For me to look into it, yeah.
You can also drop the link along with screenshots, so people…
**Antonin Bruneau (Tsuga)** 27:53 Oh, yeah?
**Shenoy Pratik** 27:55 And see the usage and stuff here.
I'm just taking some notes, One second.
Got it. I think we are on time as well.
Anything else that either of you guys had?
For the agenda.
Okay.
And then, I'll just wait for your comment, and then ask the reviewers and other maintenance processes, Danosil, Donalo, for their opinions, and then we can go… Perfect.
**Antonin Bruneau (Tsuga)** 28:49 Thank you.
**Shenoy Pratik** 28:49 This is the cool, cool addition.
**Antonin Bruneau (Tsuga)** 28:52 Good to you.
**Shenoy Pratik** 28:54 Thank you so much, folks.
**Som Banerjee** 28:55 Awesome. Thank you, Ben.
**Antonin Bruneau (Tsuga)** 28:56 Bye.
