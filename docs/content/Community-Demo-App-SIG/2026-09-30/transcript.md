SIG: Community Demo App SIG
Date: 2026-09-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Tobias Oka** 00:36 Hello.
**Shenoy Pratik** 00:38 Yes.
**Tobias Oka** 00:41 Is Shenoy your first name or Pratika? I'm not entirely sure.
**Shenoy Pratik** 00:45 In commission.
**Tobias Oka** 00:47 Okay, so now.
**Shenoy Pratik** 00:48 Yeah.
**Tobias Oka** 00:51 How are you doing?
**Shenoy Pratik** 00:53 Doing good. Let me take a second… Start the meeting notes on Doc.
And wait for a couple of minutes, or start on any agenda if you have one.
Maybe.
**Tobias Oka** 01:09 Yeah, I didn't have… I didn't have a lot to say today, I just wanted to listen in, and To see if, if, yeah, what, what people are working on.
**Shenoy Pratik** 01:27 Check.
See some other folks are out.
Today… Not sure. Juliana, is it joining?
Yep. I don't think, oh yeah, Felix is here. Hey, Felix.
**Tobias Oka** 02:14 Hi Felix.
**Felix Felix (IBM India Pvt Ltd)** 02:15 Bye. Christian, what?
I thought yes.
**Tobias Oka** 02:19 Nice to meet you.
**Felix Felix (IBM India Pvt Ltd)** 02:21 Yeah, I.
**Shenoy Pratik** 02:26 Yeah, we don't have anything specific on the agenda.
So… We usually go through the pending PRs. If you have any feature requests, you can go through them. If you want to contribute to anything, or something is bugging you in the demo, we can also go through them.
But that reminds me… Felix, we had this, Pr from Matt.
It was around agent MCP and chatbot services.
**Felix Felix (IBM India Pvt Ltd)** 02:55 metrics, right? So, he added few metrics with respect to the enough tokens, and… So, yeah, I think he will… I recently saw a commit from him.
And it keeps on getting, you know, timed out, like, without still activity, the PR just, you know.
And then, after the stale activity, he will push some commit, and… actually, I have verified, and I was able to see the metrics in Grafana.
I tested the metrics out, and I could see all the metrics that he, he claims in the, this, you know, PER summary. But I don't know why it is still not approved.
Yeah.
**Shenoy Pratik** 03:40 You see, Donald tried to work with it, and his local setup didn't show anything on the Grafana dashboard.
**Felix Felix (IBM India Pvt Ltd)** 03:48 care.
**Shenoy Pratik** 03:49 Okay, that could be the reason, but
**Felix Felix (IBM India Pvt Ltd)** 03:52 No, it's all right.
**Shenoy Pratik** 03:53 Try it out also.
**Felix Felix (IBM India Pvt Ltd)** 03:55 Okay, yeah.
**Shenoy Pratik** 03:58 That's all… it also comes down to what setup are you using. I know Donald uses Podman for a lot of things. Can cause some issues here and there at times.
But, Let me recheck this once.
And… I'm just trying to see. I see Matt also added some more comments.
If you can help review that, and then put your tick there, just so that, you know, you have verified it. I can also take a deeper look today.
**Felix Felix (IBM India Pvt Ltd)** 04:30 Yeah, I'll also test the recent version.
I can add my comments in the same PR.
**Shenoy Pratik** 04:41 Okay.
**Tobias Oka** 04:43 So, so one thing, that I have on my mind, is Some time ago, I… Contributed this thing here, basically… Do a… call it proof of concept, if you will, to show that a service can be changed in such a way that the Operator can be used to inject the SDK at runtime in Kubernetes.
And my idea is To take the same approach on.
All of the other services in languages that support runtime instrumentation.
And, so, yeah, I mean, I'm not sure how much time I will have, but probably this or next week, there will… There should be some PRs.
**Shenoy Pratik** 05:44 Correct.
**Tobias Oka** 05:45 the other services, but like Python and I'm not entirely sure if… Like, what I will do with Java yet… Hmm.
For, for, for Node.js, and yeah.
**Shenoy Pratik** 06:03 Yeah, I just want to understand one thing. Do we want to leave out one example on how it is done with packages, or auto-instrumentation, or do you want to convert everything into operator code?
**Tobias Oka** 06:17 Because sometimes.
**Shenoy Pratik** 06:18 Sometimes people use this as a showcase and learning things on how to.
**Tobias Oka** 06:22 Yeah.
**Shenoy Pratik** 06:23 They're not using the operator for some.
**Tobias Oka** 06:25 Yeah.
then… Yeah, I mean, so basically, that's a… I think that's a very good point, right? And… .
The change is, in the end, pretty small, because I do not actually remove like the manual spans that are added, or anything like that, because we live in the OTEL API, right? So all of the custom instrumentation is there.
The only difference is… That's… that it's all just written against the API, not against the SDK, and then the SDK Gets loaded in, in this case, into… the Docker file, And… Because it is loaded via the Docker file.
environment variable, you can very easily replace it. So, in a way, it is actually still there, and you can use this if you want to do manual instrumentation yourself.
It's just not part of, like.
you know, package JSON, or, you know, what be it.
Yeah. Like, I think it's a bit of a… question of how we want this to work. Like, my view is that in most scenarios.
I probably wouldn't necessarily want to hardbake the SDK, into my package if I don't have to.
but… like, I don't know, what's your… what's your view on this?
**Shenoy Pratik** 08:11 My, my opinion is the same as you. EKS is the default, like standard now to.
**Tobias Oka** 08:15 Yeah.
**Shenoy Pratik** 08:16 Published services, and then… If that's the case, then I don't want to pollute my service packages.
with other OTEL-related things. I don't know if it is an actual CV coming from something that I have added in, or something that OTEL is inheriting from its transitive dependencies. So, that way… I agree.
I'm just thinking, do we want to spin up an issue before we do it for all services?
Just forget…
**Tobias Oka** 08:44 you.
**Shenoy Pratik** 08:45 other containers view and… before you start on anything. So, it's easy to know if everyone is aligned.
I'm pretty much there. Maybe we can leave out one service as an example on how to do it.
Yeah, but it's only that some maintainers might think, that OTEL Demo is used for, learning and as an example showcase on how to do it easily.
**Tobias Oka** 09:11 Yeah.
**Shenoy Pratik** 09:11 In that case, I think…
**Tobias Oka** 09:13 case, I think the question is also then for what… for what languages would we… would we want to have it, right? So we would almost need… for each language, at least two services, one where it's done one way, one where it's done the other way, because otherwise, what we still will always have left is we will have services that don't have runtime instrumentation anyway. There, you will anyway have it all.
Done. Yeah.
**Shenoy Pratik** 09:38 And also, some of them have runtime instrumentation, some of them have manual instrumentation. There's also this variation, but I do remember, I think there are many services in… 500.
Okay, maybe wrong there.
**Tobias Oka** 09:52 Yeah, Python has lots of them, like, especially also the new AI stuff, I think, has… I found the other.
**Shenoy Pratik** 10:01 Okay.
So, that's the case, we can look at the languages, where it is redundant, where it has, Different ways of instrumentation, and then we can pick a few of them to start with.
**Tobias Oka** 10:16 Yeah.
**Shenoy Pratik** 10:18 I added the link which says, like, the multiple services.
Having different languages in there.
**Tobias Oka** 10:26 By the way, regarding the issue, There… is actually… 1 It's not by me, and it's also a bit old, but…
**Shenoy Pratik** 10:42 you Nice. I think we can double down on this. You can ask a question for all approvers, and then we can start a discussion.
**Tobias Oka** 10:53 Sounds good.
**Shenoy Pratik** 11:07 I'm just taking the notes.
So this is… called instrumentation injection.
Cool. That makes sense.
Mmm.
Do you have anything else, Tobias?
If not, I have some questions for Felix. Felix, thanks for joining in again after a few weeks. I had some things running in my mind for agents, but didn't get time to implement.
Maybe you can get some of your thoughts.
If you have bandwidth, you can also pick it up. Agent evaluations have been picking up a lot right now in the hotel world.
And we have the evaluation spec for agent spans and events.
So whenever there is an evaluation done on a benchmark, people store it with the A.
events, telemetry, and then they have it stored inside their backend, and they use Grafana or any dashboarding to view these evaluation runs, to see what is the average score for the evaluations run from yesterday, something like that.
So, do you have any experience, there?
And is there any recommendation from you? You're on mute, by the way.
**Felix Felix (IBM India Pvt Ltd)** 12:47 Sorry. So I have seen evaluations where people were using an JETS LLM.
**Shenoy Pratik** 12:54 Yeah, online is one part of it, but also there's the offline part.
So…
**Felix Felix (IBM India Pvt Ltd)** 12:59 Okay. Do you have any benchmark which uses offline? I can probably…
**Shenoy Pratik** 13:05 Yeah, so I don't think, like, for our agent that we have, the support agent that you have added in, we don't need a benchmark or a data set, right? We can just create our own data set and run some evals on top, and then store it in…
**Felix Felix (IBM India Pvt Ltd)** 13:22 So, I'm, so I'm a little bit confused. So, with respect to quality, it's not gonna change over time, because we are using a fixed Set of responses, again and again.
with respect to latency also, it won't be changing, because it's just coming from… so, the score will be invariant of anything, right? We will be just keeping a… number, which will be perfect score every time, because if I'm comparing, for example, if I'm taking path A to reach an answer, it will always take path A, and the response time also won't be having any variancy or, you know, with each other.
So, irrespective of the score, it will be a perfect score, I assume, right?
**Shenoy Pratik** 14:05 Yeah, for what for that? I was imagining that we use feature flags.
So we enable something in feature flag for agent, and even if it is a VCR, it switches to some other VCR which has errors.
And then you see in the evaluation run something that goes down.
So, maybe latency has gone up. In the VCR, it just takes time. Or, the VCR is running into errors, and that's why the evaluation is not completing or giving wrong results.
**Felix Felix (IBM India Pvt Ltd)** 14:33 So this will be, like, something like a, you know, fault injection kind of stuff that…
**Shenoy Pratik** 14:37 Fault injection, yeah. But in pair with some Grafana dashboard, which will show evaluation result. Yeah.
**Felix Felix (IBM India Pvt Ltd)** 14:43 Okay. So evaluation will be tied to the trace ID somehow, or…
**Shenoy Pratik** 14:48 Yes, so evaluation, in the semantic convention, GitHub repo, I moved to GitHub right now, for… Agent.
observability.
Let me pull it out. There is.
There is a recommendation to use events. Events are nothing but logs stored in OpenSearch.
So they mentioned that that's the way to go ahead.
So we can store logs in OpenSearch, and the Grafana dashboard can pull logs, use VPL to create these visualizations.
**Felix Felix (IBM India Pvt Ltd)** 15:22 Okay, okay.
**Shenoy Pratik** 15:23 that.
**Felix Felix (IBM India Pvt Ltd)** 15:23 That, that, I'll check it out. If you have, what is the convention of Sending out this. So… okay, so logs… okay. Basically, we will send the trace context in the log as well.
And Grafana can somehow link these events.
**Shenoy Pratik** 15:42 Yeah. We have trace-to-lock correlation, right? So if you log has trace ID, so it uses the same thing. It doesn't invent anything there.
Yeah.
Let's share this, I got the link… This is domain branch.
This is the one.
**Felix Felix (IBM India Pvt Ltd)** 16:01 Okay.
**Shenoy Pratik** 16:02 Does, like, evaluation spec in detail?
Hmm.
Click on… something… Azure one, or DPVAL one, has some examples as well.
**Felix Felix (IBM India Pvt Ltd)** 16:14 Okay, yeah.
**Shenoy Pratik** 16:21 Okay, I'll send some more links, just so that we can brainstorm.
Later.
But something that…
**Felix Felix (IBM India Pvt Ltd)** 16:30 Slack, right? You'll be sending on Slack, right?
**Shenoy Pratik** 16:32 Yeah, Slack, yeah, okay.
**Felix Felix (IBM India Pvt Ltd)** 16:37 This is… this is cool. I never saw this before, because we have our own evaluation, internal, you know, evaluation stuff going on, and we were trying to create a root span.
To the trace ID, which contains the evaluation results. Now, I…
**Shenoy Pratik** 16:56 That's another thing, like, even with our SDK, the OpenSearch SDK, we have been trying that way out, where we create, test spans.
for evaluations, because that's what people do with Jenkins today.
So if you have a Jenkins RAM that will run some integration test, people have the CIDCD spans, which have test ID and everything. Yeah, but there's a different way of how the semantic convention is treating that. So we can try this way first and see if it works.
**Felix Felix (IBM India Pvt Ltd)** 17:27 make.
**Shenoy Pratik** 17:27 Makes sense to put it in the demo.
Yeah.
Let me know if you have some time, we can discuss.
**Felix Felix (IBM India Pvt Ltd)** 17:36 Wow.
Thanks for the suggestion, I'll go through it.
**Shenoy Pratik** 17:46 So we can get some open PRs.
If you need any.
To review it out as well.
I think we are good here.
More or less, yes.
These are good.
Tobias, do you have any experience with Java instrumentation?
**Tobias Oka** 18:14 A bit. I mean, Java is the language I have worked with the most in my career, I guess, but lately a bit less, so… depends.
**Shenoy Pratik** 18:25 Yeah, lately I think it's less with every language for me.
**Tobias Oka** 18:29 Yes, exactly! Lately, lately, the language that I use most is natural language when I talk to Claude.
True, yeah.
**Shenoy Pratik** 18:43 There is this PR that came in, where they are adding Spring Boot In one of the services, and using that for instrumentation.
We have a question, like, Spring Boot recommends their own API called Micrometer for OTEL instrumentation. And then there is the OTEL recommendation itself from our documentation, which uses the Spring Boot starter.
So, if you have any… opinion based on your experience that will be helpful if you can just comment out on the last pr I shared the last comment on it.
**Tobias Oka** 19:22 Okay, I'll have a look.
And read through it.
**Shenoy Pratik** 19:25 Okay.
Yeah, so, like, for our, we discussed this PR last, time within the maintainers, and then, like, we don't have any hard opinions, so we'll ask the Java.
approver folks, the Ava instrumentation approver folks. They mentioned to use the starter, but if you are a practitioner, I would also like to know your opinion before we tilt towards one.
**Tobias Oka** 19:49 Yeah, happy, happy to have a look, and… Yeah.
Give… give my opinion. Up to… I will have to look into it a bit more, because.
**Shenoy Pratik** 19:57 Yeah, yeah.
**Tobias Oka** 19:57 You can take.
**Shenoy Pratik** 19:58 Take your time and just put an async comment on the thread.
**Tobias Oka** 20:01 Yeah, exactly.
**Shenoy Pratik** 20:07 Cool.
I think that's what I had for this meeting. Do you guys have anything else to discuss?
If not, I think we're good for today.
**Felix Felix (IBM India Pvt Ltd)** 20:25 Yeah.
**Shenoy Pratik** 20:26 Thanks everyone for joining.
**Felix Felix (IBM India Pvt Ltd)** 20:28 Bye-bye.
**Shenoy Pratik** 20:28 Thanks, Sophia.
**Tobias Oka** 20:29 2.
**Shenoy Pratik** 20:30 Bye-bye.
