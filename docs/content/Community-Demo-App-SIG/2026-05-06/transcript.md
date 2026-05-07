SIG: Community Demo App SIG
Date: 2026-05-06
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 02:56 Hello, Barry.
**FELIX GEORGE** 02:59 Hi.
**Juliano Costa | Datadog** 03:01 How you doing, Felix?
**FELIX GEORGE** 03:02 I'm good, how are you?
**Juliano Costa | Datadog** 03:04 Good, good.
Is that your first time on the… Sick, on the sick, or…
**FELIX GEORGE** 03:21 No, no. I mean, I've been… I have attended, I think, 26 before.
**Juliano Costa | Datadog** 03:27 You, So you are, with the IBM team? Yeah. Okay, cool.
Nice.
I'll add Donal here, and myself.
**Donal O'Sullivan** 03:48 Hey guys, how are you?
**FELIX GEORGE** 03:50 I…
**Juliano Costa | Datadog** 03:57 So, I actually… I think I have added here to the meeting notes the… the PR.
To discuss. Yes, I did.
So, you are basically here to discuss the ad agent astronomy Shop, the MCP server, right? Yeah, okay. Yeah, I added here to the… to the… to the agenda, because I was going through the… the open PRs that we have, and we have a couple of ones that are Ode, so to say.
that I would love to… give authors a, a feedback.
**FELIX GEORGE** 04:44 Yeah, sure. Actually, Shinoy shared some feedback today, and I have, I have addressed, addressed them.
at least try to… I mean, I hope it's fine with him, the way I have addressed the PR. I mean… Okay, so I'm waiting for the comments, for the more comments.
**Juliano Costa | Datadog** 05:06 Okay.
**FELIX GEORGE** 05:07 But I think last meeting, there were… I couldn't attend because I was traveling for a conference, but last meeting, there was some discussion on… actually, right now, we are caching the response, if the user want. There is a feature flag there, NVMN variable, which they can toggle to Catch the request and response.
So when the exact same request comes in the future, the call won't go to the LLM, it will just, you know, send a cache response again.
So, that's something that we have added, because I felt like, you know, for people who doesn't have an LLM, I can share this cache with them. You know, we can have a few versions, a few open model, you know, caches, I mean, like, Gwen or, like, you know, GBD OSes or something.
model caches… caches, which we can share with the people, so they… if… for the people who doesn't have access to the model, they can still, you know, try out the OpenTelemetry demo, with the Agent framework. So, but there was a request to actually use a smaller model, if possible.
So, I was trying to do some kind of fine-tuning office more of a Quen 3.5, 2 billion, to be exact, because you can actually run it on a laptop, locally.
So, that's what I was trying out, and still… still, it's not giving me correct responses still, but I'm trying DPO right now to, you know, make it better suited for the tool calling that we have in astronomy show application.
Yeah, so that's what's something that I'm trying out right now.
But I'll give… I'll share the updates if it… if it is good enough for…
**Juliano Costa | Datadog** 06:53 Cool.
Nice. Yeah, I think the way that we are, working on Actually planning on, deploying the demo In the future, in a near future, will actually help a little bit on that, because then we can… simply deploy the demo, just the core services, the whole demo, or, now Donald has an OpenPR that chips profiles.
**FELIX GEORGE** 07:27 So, you.
**Juliano Costa | Datadog** 07:27 We can run the demo with profiles, run the demo, the live mode, just the demo, or then we would have an extra one for the agentic demo.
I think that helps a bit.
Regarding the cache that you said that you can share.
How does that work? I'm a newbie here.
**FELIX GEORGE** 07:51 Okay, it's dead.
**Juliano Costa | Datadog** 07:52 Would that be part of the Docker image, for instance, or not?
**FELIX GEORGE** 07:55 Yeah, yeah, it can be, it can be. It's just a YAML file right now, so whenever it sees a new request, it will just add the request and respond to the YAML file.
Like, it will append to the same file again and again.
So, for… I was thinking, like, so we can have a file with the prefix of the model name. For example, if it's GPT-40, like, you know, cache… some… some, you know, prefix and, GPT-4-0.
Like, if it is Claude, Claude 4.7 Oppos, you know, like, we can have different models if people want to try it out.
That's… that's the idea of having the cash, but Yeah. But, but the problem with the cache is the response is immediate, okay? Actually, in all the agent link flows, the around 90% of the trace time of the complete trace of the application, of one execution, that's actually consumed by the LLM calls. But if you use cache, the responses are, like, you know, immediate.
Which kind of doesn't give you the, you know, complete picture.
But, but there's… Yeah, I understand. Yeah, in the cache itself, you can kind of add some kind of sleep time.
To simulate the latency of the request. Yeah, but, yeah.
**Juliano Costa | Datadog** 09:24 Yeah, but I… is live time.
Would be an interesting approach, but Yeah, okay, well, let's see, do you have any… So, I know that you mentioned that Shanoy, took a, gave you some tips. Do you want to ask him anything, as he just joined?
**FELIX GEORGE** 09:52 You know, thank you for your comments in the PR. I mean, I tried to address them all, but, there was one concern that I felt was, the shipping core tool, it… for me, the GET request is working, and the post request is not working. I mean.
the GET request.
**Shenoy Pratik Gurudatt** 10:09 I can…
**FELIX GEORGE** 10:10 They're giving me valid response, and the post is.
**Shenoy Pratik Gurudatt** 10:12 Yeah, I can check if the API is RPC or not, the one that I was suggesting. I can look at the code and then verify once again.
**FELIX GEORGE** 10:19 Huck.
**Shenoy Pratik Gurudatt** 10:19 So if it works, that should be good. Either API is good from front-end or the service directory.
I had some concerns on the, chat UI not being exposed on the right port.
**FELIX GEORGE** 10:34 I have a…
**Shenoy Pratik Gurudatt** 10:35 the front-end proxy.
**FELIX GEORGE** 10:36 I have exposed it right now, so it will be, like, localhost 8080 slash chatbot.
**Shenoy Pratik Gurudatt** 10:43 Understood. And then, the other concern was, if, for example, today in our LLM recommendation service, we don't explicitly need one LL model running behind, it can use some hard-coded values to go to and fro.
**FELIX GEORGE** 10:56 Yeah, I saw… it's kind of similar to what I'm doing, but without the request, like, you give the hardcore…
**Shenoy Pratik Gurudatt** 11:03 with the VCR?
**FELIX GEORGE** 11:05 Yeah, with the VCI.
**Shenoy Pratik Gurudatt** 11:06 So, in that case, Can you make sure that the demo works with some dummy VCR file already there, attached? And then, when users load it, it should just work out of the box, irrespective if they have LLM or not. We can just test it out end-to-end, I can also do that.
**FELIX GEORGE** 11:24 Okay, so…
**Shenoy Pratik Gurudatt** 11:25 Damn.
**FELIX GEORGE** 11:26 I can share a VCR file if you want to test it out.
**Shenoy Pratik Gurudatt** 11:31 You can also put it in the PR itself, so that I can pull it from there, and we can merge that in a.
**FELIX GEORGE** 11:38 I was a little bit concerned because I was using GPT-4.0, Which is a proprietary model, and if I upload it, they will raise some legal issues or something. I was not sure, that's why I didn't upload it in the PR.
**Shenoy Pratik Gurudatt** 11:54 I see. Do you want to use any open source model? Give me…
**FELIX GEORGE** 11:58 I can try, I can try with, some social media.
**Shenoy Pratik Gurudatt** 12:01 Yeah, that would be fine.
I don't think the sponsors… have any issue, but it's better to go with an open source model. And also, we can write some mini README for users to onboard their own model. So if I have Claude, via some other endpoint, like Bedrock, can I onboard it to the same, environment, and then what is the procedure. So, we can write a short readme on that, how to bring your own LLM model.
Each of the services today have a README. We can follow the same template and add it in.
**FELIX GEORGE** 12:40 I'm not sure about, for example, if someone is bringing cloud, cloud models, and, I'm using Chat OpenAI for calling the LLMs.
So… or cloud, if they are using the cloud endpoint, but if they are using lighter endpoint, anyway, it shouldn't be a concern, you know.
**Shenoy Pratik Gurudatt** 12:59 Yeah. But can we have a genetic wrapper, is what I'm thinking.
**FELIX GEORGE** 13:03 Hmm.
Yeah, we can have a generic wrapper, like, to identify the model from the model name, or .
**Shenoy Pratik Gurudatt** 13:10 Yeah.
**FELIX GEORGE** 13:10 And the call, yeah.
Maybe, can I…
**Shenoy Pratik Gurudatt** 13:13 That's… try that, because that would be more easier to, like, more easy to maintain in the long term, I feel.
Okay, yep, rested all good.
**Juliano Costa | Datadog** 13:28 Yeah.
**Shenoy Pratik Gurudatt** 13:29 The major thing that's important.
**Juliano Costa | Datadog** 13:31 You got my attention when you said, easier to maintain.
**Donal O'Sullivan** 13:39 I, I had…
**Juliano Costa | Datadog** 13:40 I'm back to you.
**Donal O'Sullivan** 13:41 So, I haven't had a look to… had a chance to look at the PR yet, Felix, but so, are we following the OpenTelemetry for, like, generative AI? So, are we instrumenting all the AI parts of it with, like, the old telespec?
Essentially.
Is that… is that the idea here? To, like, demonstrate, like, instrumenting LLMs, you know, AI calls, like, tooling.
Following the, OTEL AI guidance.
**FELIX GEORGE** 14:07 Oh, okay.
**Donal O'Sullivan** 14:07 Just wondering there.
**Juliano Costa | Datadog** 14:08 I think, I think to answer that, Donna, I think it would be nice to maybe go back to one of the recordings, I can point you to that.
**Donal O'Sullivan** 14:19 Yeah, I think it was because they actually… Yeah, yeah.
**Juliano Costa | Datadog** 14:22 They actually presented, the… the project.
They have a whole new… flow for the… for the demo.
Are you… Buy the stuff, but by talking with an agent, and then they have, like.
**Donal O'Sullivan** 14:39 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 14:40 this whole new approach. It's… it's nice, it's different, and I… I feel that this is the way that the world will be in a couple of, Months, maybe?
**Donal O'Sullivan** 14:51 Yeah.
Yeah, no, no, so I was actually… I was in the call, but, I know.
**Juliano Costa | Datadog** 14:57 Wow, can…
**Donal O'Sullivan** 14:58 So, in OpenTelemetry, we do have instrumentation for generative AI, though, right? So to instrument all that.
I'm just wondering, are we following those standards, like the…
**FELIX GEORGE** 15:06 So, I'm using TraceLoop, for instrumenting the application.
But it's… so it's… all the spans are auto-generated, I'm not generating, spans or adding any attributes, but Shinoy pointed out there is a… there is a… way that… there's a plugin for Autel Collector which can convert the trace loop spans into Autel Collector spans. I haven't tried it out yet, sorry for that, but yeah.
**Shenoy Pratik Gurudatt** 15:32 We were finding sponsors, and it took some time. I think, finally, we have one. So, it is an open PR. I think one of my colleagues, Kyle, is working on it.
**Donal O'Sullivan** 15:45 Cool.
**Shenoy Pratik Gurudatt** 15:46 that, and then once we have that in, we can just attach it as a processor. So we convert everything from Tracelube into just Gen AI conventions.
**Juliano Costa | Datadog** 15:55 I'm really concerned about this, then.
Because I know that ServiceNow acquired TraceLoop, right?
**FELIX GEORGE** 16:02 Yeah.
**Juliano Costa | Datadog** 16:03 So the OpenLM3 project, we don't know how it's gonna… What's the future of it?
But anyways, I think daily and length views are the most mature ones, right? Like, Hotel is a bit behind on that.
**FELIX GEORGE** 16:22 Yeah.
**Juliano Costa | Datadog** 16:24 Yeah.
**FELIX GEORGE** 16:24 So, I actually have, I was the one who added the OpenTel Elementary MCP instrumentation, but during that time, we reached out to OpenTele Elementary as well to support, you know.
native support for, because, yeah, the MCP doesn't have any callbacks or, you know.
for V2, you know, monkey patch the functions to add observable, sorry, spans and, you know, span attributes. It doesn't support that, but we, we raised a PR in our MCP servers, but they… nobody… they didn't respond, actually.
There were some activity after that also, but people were not really, you know, willing to… Do that.
So, yeah.
So it will be difficult to add native, telemetry support for MCP, but yeah.
**Donal O'Sullivan** 17:20 And, sorry, what repository was the pull request in?
**FELIX GEORGE** 17:24 MCP… okay, MCP plug… Sorry, the MCP Python SDK, that purpose.
**Donal O'Sullivan** 17:30 it for… for Oto.
**FELIX GEORGE** 17:32 Yeah, no, no, no.
**Donal O'Sullivan** 17:33 Oh, okay.
**FELIX GEORGE** 17:34 Yeah, so, yeah.
Not…
**Donal O'Sullivan** 17:37 Not for auto.
**FELIX GEORGE** 17:38 Not the OTEL one, but the MCP Python SDK, right? MCP has, like, Go SDK, Python SDK, and I think JavaScript, hybrid, for MC.
**Donal O'Sullivan** 17:48 There's probably… there's probably an OTEL SDK for Python, though, right?
So you can instrument your Python MCP server.
with… with hotel?
**FELIX GEORGE** 18:00 No, but I don't think it will work natively, because, because, for example, when you are… when you're running Py, MCP, the communication between server and, The server and client, okay? So there is, you know, one server and a client, and it happens in one queue, okay? And the communication from client to server That happens in a completely different queue. So these… both processes are detached. So the native hotel, this context propagation won't work there. You will get, detached spans.
Okay. So your request will be one independence plan, and the response will… which comes, back, that will be completely… it will… both won't have the parent… the same parent race ID.
They will have.
**Juliano Costa | Datadog** 18:51 Aren't they… Are they using spanned links, or not even that? Do you know?
**FELIX GEORGE** 18:57 I'm not very expert in it, how to solve this, but when we tried it, we were seeing this issue, and we tried to import… get the context, get the current context, but both are in a completely different, you know, both are different ports, to be honest, right? MCP is one port, which is the server, and your agent is a different port, which is the client.
So… both will have different contexts, so I'm not sure how to… how can we link these two.
**Donal O'Sullivan** 19:32 Might be worthwhile. Yeah, yeah.
Go ahead.
**Juliano Costa | Datadog** 19:36 No, what I wanted to say is that the Python instrumentation for GenAI is way behind, I think it's on semantics 136?
I've been asking on the… on the Slack channel, like, hey, can we get a release with the new semantics?
And, yeah, it's been… it's been a while, so… I know, I mean, we need to work with what we have.
I think… Okay, so from my end, prior to the meeting, I also added this… integration tests in the CI PR, PR3194.
which basically… kind of brings… the, the trace test back. We have been discussing that in the prior SIGs.
I'm not sure if we should have that, or not, or if we should focus on, some sort of, Automated way that we can… Validate that the demo is running, and spins are being created, spins are properly connected, metrics are being generated, and logs are flowing through.
It is, like, 3 different things.
I don't know… What we should do, but either way, we should, give an answer or take some action here for key lag on the PR.
I think I discussed with him on Slack, so he's not actually worried about… it's just me, like, after removing a couple of times the stale, tag from the… from the PR. I would love to… Have some… some action here.
Opinions?
**Donal O'Sullivan** 22:01 Nope, yeah.
**Shenoy Pratik Gurudatt** 22:02 Through this, but it looks good.
**Juliano Costa | Datadog** 22:07 So, the thing is, it works.
For a small set of stuff.
And it's validating traces, because it's the trace test.
So, for traces… we… Actually, to validate just traces, we actually don't need the whole… Trace test, suit.
we could rely on Jager, because we can… let's say, if we run the demo.
send traces to Jaeger, we can… within the pipeline, within the CI, we can query Jaeger and get the JSON.
from… from the trace, and then we just do the checks there, like, hey, is service A connected with service B? Like, yeah, I know that, it's not easy if we would do manually, but, with, AI nowadays, it's actually pretty simple, like.
Like, what… once we… explain the case, I think that that is doable. The thing is that this would only validate traces. I think even Pierre has something that he's been using for some time already.
He called, Trace Validator.
But the problem was when I added, like, when I brought up to him, like, what about metrics and logs?
So… I don't know, we could have 3 different pipelines, and we start with something?
Having something is better than having nothing.
**Shenoy Pratik Gurudatt** 23:53 Yep, this also checks individual attributes, right?
In the traces.
Do we need to go… This also checks the attributes in the traces, isn't it?
**Juliano Costa | Datadog** 24:05 Yep.
**Shenoy Pratik Gurudatt** 24:06 Do we need to go in that detail? Because you just mentioned, you just mentioned to check if you want to see a connection between Service A and Service B.
**Juliano Costa | Datadog** 24:15 Yeah, I… I think…
**Shenoy Pratik Gurudatt** 24:19 Cooliff.
**Juliano Costa | Datadog** 24:20 We could eventually have Weaver doing a live check later.
to validate the attributes, we don't need the trace validator to… to actually do this… do the attribute validation.
**Shenoy Pratik Gurudatt** 24:36 Yeah.
And Dead, I mean… Yeah.
**Juliano Costa | Datadog** 24:42 You can also showcase Weaver Live Check. Yeah, go ahead, sorry.
**Shenoy Pratik Gurudatt** 24:44 Just to give some… we have the observability stack up, which is having a similar CI test. What we do is we just run it in our GitHub CI. There's a bash script. Bash script goes and checks the Docker logs.
And make sure the things that are emitted out have the trace context there. And it also pings OpenSearch, queries OpenSearch, queries Prometheus, and then fetches some data to make sure it is in some sanity.
It doesn't check exactly if service A is scoring service B, but we can go into that detail, but that's another way, That's what I was thinking to, put in peer's trace validator.
I'm just thinking right now, should I just… Start on it, or… We can get this merged in, and then I can build on this.
That's what I'm thinking.
Hmm.
**Juliano Costa | Datadog** 25:39 Yeah, I think we just need to loop Pierre and maybe see. Maybe we can start the discussion on Slack and see.
If he wants to start with the trace validator, or if you can bring What do you already have, and…
**Shenoy Pratik Gurudatt** 25:55 Okay.
Let me do that, let me create a PR this week, and then we can…
**Juliano Costa | Datadog** 26:01 Thanks for joining, Felix.
**Shenoy Pratik Gurudatt** 26:02 Thanks, Alex.
Yeah.
let me, get that PR out this week, and it will test everything locked spaces and metrics, but on a higher level, it's not… it will not be at an attribute level that we are doing. Also, I feel attribute level checking is difficult to maintain without Weaver. If code drifts, then… fail.
**Juliano Costa | Datadog** 26:25 No, no.
**Shenoy Pratik Gurudatt** 26:25 Even if the stack upgrades, it will fail.
**Juliano Costa | Datadog** 26:28 Yep.
**Shenoy Pratik Gurudatt** 26:29 Yeah.
**Juliano Costa | Datadog** 26:30 No, I think with Weaver, we'll be… we'll be way better. And we also take the chance to showcase Weaver.
**Shenoy Pratik Gurudatt** 26:38 Yep, yep, yep, exactly.
Yeah, so let me take a stab. I also looked at Pyotr's PR. I didn't have a chance to look at it before. That's a good thing. We have something up.
It just gets locked between all the dependency PR that comes in.
**Juliano Costa | Datadog** 27:00 Yeah, I think we, we, we have changed, Dependabot, Schedule, so now it only opens once a week, which is great.
For our sanity.
**Shenoy Pratik Gurudatt** 27:14 Yeah.
**Juliano Costa | Datadog** 27:17 But still, it would be nice to have something that is automated. So, whenever we have an approval, we are sure that the things are running.
**Donal O'Sullivan** 27:28 Yeah.
And then, like, auto-merge the dependable up here.
**Juliano Costa | Datadog** 27:33 Oh, that would be awesome, yes.
**Shenoy Pratik Gurudatt** 27:35 After we get the testing in.
**Donal O'Sullivan** 27:37 Yeah, of course, yeah, yeah, 100%. Otherwise, it'd be interesting.
I… I just had a… so I remember attempting to run the… Tests locally in my machine, and they didn't work.
This was a while ago, though. I guess, Kila is probably… he's… looks like he's addressed a lot of the issues, maybe? I haven't… I haven't got a chance to look through the full PR.
Have you guys had similar experiences, or…
**Juliano Costa | Datadog** 28:13 Sorry, coming in.
**Donal O'Sullivan** 28:15 So just running… just running them locally, I know… I think there… wasn't there a make target to run these tests locally on your machine? So, like, versus… NCI.
I can't remember.
**Juliano Costa | Datadog** 28:28 Love.
**Donal O'Sullivan** 28:30 We'll double check.
**Juliano Costa | Datadog** 28:31 I know that TraceTest was runnable locally, faster than, wireless CI, to be fair.
**Donal O'Sullivan** 28:40 Yep.
**Juliano Costa | Datadog** 28:41 But the problem with, The reason why we disabled trace tests was that it was, flaky on our CI.
**Donal O'Sullivan** 28:50 Hmm.
**Juliano Costa | Datadog** 28:50 So sometimes it took 15 minutes, failed, we just restarted, and it went through.
**Donal O'Sullivan** 28:57 Yeah, yeah.
**Juliano Costa | Datadog** 28:57 twice.
**Donal O'Sullivan** 28:58 Yeah.
**Juliano Costa | Datadog** 28:59 We decided to drop.
**Donal O'Sullivan** 29:03 Okay. Yeah. Cool.
I can, yeah, I can review that PR anyway, and have a look.
In, in 3 times.
**Shenoy Pratik Gurudatt** 29:17 One question.
**Donal O'Sullivan** 29:20 Oh.
Nice.
**Juliano Costa | Datadog** 29:24 I can'.
**Shenoy Pratik Gurudatt** 29:25 turn that pager off, but I just like to not miss any page.
**Donal O'Sullivan** 29:33 Mute.
**Juliano Costa | Datadog** 29:36 What is… what is this PR that… I just saw it now, like, the… the… the middleware?
**Donal O'Sullivan** 29:48 dear.
**Juliano Costa | Datadog** 29:49 I saw the… once.
**Donal O'Sullivan** 29:51 What's going on over here?
**Juliano Costa | Datadog** 29:51 like… Bye.
**Donal O'Sullivan** 29:53 I'm not sure…
**Juliano Costa | Datadog** 29:54 I…
**Donal O'Sullivan** 29:55 Yeah. I was… I was trying to explain, I was like… if you fork the demo, you can put, like, a link of your fork here, and I think they were trying to, like, link to a demo of their… service, but it's behind the paywall. Yeah.
Anyway, I don't know. I guess we can close it now, I think? They said they don't have open source code, so I guess…
**Juliano Costa | Datadog** 30:24 I mean, I don't mind, they don't have any open source code, but can they point to, like, instruction on how to send NOTAL data to their closed source code?
But anyways, I think that the main issue here is that we shouldn't invest that much time on PRs that do not have the easy CLI signed.
So, like, that should be the first thing. Hey, hey, to us, to even spend time here discussing with you, please find the CLA, and then we… we… we discuss. Yeah, this is, like, yeah.
I was just, it was just interesting to see. Before we wrap up, I want to discuss one thing about Firepeat.
Yep.
I… I've been… Well, I set up PR to Florian, adding, what's it called?
Jesus, I forgot.
adding a base path comment to FirePit. So then we can use FirePit behind Envoy, so then whoever deploys the demo can simply expose Envoy, so the front-end proxy, which is… how we recommend, to expose. So I have everything on my… on my machine, I'll… I'll push, I'll… I'll push.
To your PR, Donald, if you don't mind?
**Donal O'Sullivan** 31:58 Yeah, sure, yeah, of course.
**Juliano Costa | Datadog** 31:59 one… I'm currently building it, to test it out. I want to ask your opinion on this.
I just don't know which one it is, so… Give me a second.
Okay, I have only one.
Error? Okay.
So… I saw that we are… we were doing, resource attributes… Getting the container name and asserting to service name.
Yep.
But I think in the… let me just check here the change… Yeah, I…
**Donal O'Sullivan** 32:46 I don't think it actually works.
**Juliano Costa | Datadog** 32:48 Yeah, the thing is that we… we were not even adding to the processor.
**Donal O'Sullivan** 32:54 Okay.
**Juliano Costa | Datadog** 32:55 I added it, but the problem is that a container name is an optional resource attribute on Docker.
So we actually need to add this. But I'm testing… I'm testing it now, and I can send to you.
**Donal O'Sullivan** 33:11 Yeah.
**Juliano Costa | Datadog** 33:12 And…
**Donal O'Sullivan** 33:13 That, that worked with, with, with, what was the other one called? Pyro something. So they… they had a recommendation, but yeah, a Pyroscope data recommendation that you change… that you use service name just for filtering and being able to view profiles, and I… I forked off of my other PR, so there's probably, like.
**Juliano Costa | Datadog** 33:33 Okay.
**Donal O'Sullivan** 33:35 Yeah.
**Juliano Costa | Datadog** 33:35 Cool.
A couple of things that I'm doing here. So, I have a bunch of changes here, to be honest.
One thing that I'm doing, and maybe I shouldn't, is that I'm already taking the chance to update the The… the names with the new… Underscore…
**Donal O'Sullivan** 33:58 Yeah.
**Juliano Costa | Datadog** 33:59 And I also… I'm also adding a transform to send task profiles and remove process executable path.
And I think… so, like, I'm still investigating, because when we go to the… to the profiles, we have a whole list of all the container IDs, and all the… container IDs… Process Executable path and process executable name.
if we get the container name, then all of that is, we can drop it, so I think it's easier to navigate the profiles when we go to FirePit. Otherwise, it's just a list of a lot of stuff, so I'll test it out.
And then I have the profiles here, and then, of course, we need to add this… FirePit host and port, and that's what I'm doing here on the… On the nth.
And any objections on bumping to 151?
**Donal O'Sullivan** 35:09 That's just the base collector, though, is it?
**Juliano Costa | Datadog** 35:12 Yes, and I, I, I also bumped the one from… From the profiling.
**Donal O'Sullivan** 35:20 Okay.
Cause the… that… yeah, that's just the… that's just a collector distro for profiling, right? But I assume.
**Juliano Costa | Datadog** 35:28 Yeah, that's pretty… that's.
**Donal O'Sullivan** 35:29 It'll be fine, I guess. Yeah, yeah, yeah, should be cool.
**Juliano Costa | Datadog** 35:33 And now that we have the GitHub images.
I am removing this bill.
**Donal O'Sullivan** 35:43 Yeah, yeah.
**Juliano Costa | Datadog** 35:44 we need.
**Donal O'Sullivan** 35:46 No, I don't think so. I think I had, yeah, I was experimenting with both, and I think I had.
**Juliano Costa | Datadog** 35:51 Yeah.
**Donal O'Sullivan** 35:52 Yeah, we don't need to build. Yeah, that's funny.
**Juliano Costa | Datadog** 35:55 Okay.
**Donal O'Sullivan** 35:55 Cool.
Just with the, with the, process executable path, so does… does the… does the flame graph change then when you run it? So what do you see then in the flame graph?
**Juliano Costa | Datadog** 36:09 So the thing is not the… the… It's not about the… Jeez, it's not about the… the flame graph itself, it's about… The options that we get on the drop-down, because.
**Donal O'Sullivan** 36:26 Okay.
**Juliano Costa | Datadog** 36:27 you receive all the profiles, and then the profiles, I think they are listed by their resource attributes.
Yeah, yeah. So then we have all the container IDs, then we have host, we have OS, And we have, all the process executable path, and all the process executable name. If we get just the container name, then we are good, and maybe we can have, like, other stuff?
That is running… I don't know. Do we, like… when I'm… when I run, I get, Chrome and some other stuff that I have running on my laptop. Do we want that or not? Because then I can… we can also drop that and get just the demo profiling. I don't know.
**Donal O'Sullivan** 37:19 Yeah, yeah.
Yeah, I mean, like, that's the thing about eBPF profiling, it's just gonna get everything.
**Juliano Costa | Datadog** 37:27 Yep.
**Donal O'Sullivan** 37:28 Yeah, I thought, yeah, how difficult is it to filter that out?
just have to add some settings to the collector to process it, I suppose.
Yeah.
I don't really mind. Yeah, Florian, like, I'm not actively on the profiling side at Elastic, like, that's very much Florian is, like, the expert there, but… I think it might be tricky to, like, filter it out.
**Juliano Costa | Datadog** 38:06 No, not, yeah, I'm actually good in keeping. The only thing that I'm trying to clean is the… if I underst… if I understood what… what… what we get correctly.
We get one item in the list per resource attribute.
So if, for instance, the same, for instance, we have the container ID.
**Donal O'Sullivan** 38:40 Hmm.
**Juliano Costa | Datadog** 38:41 And we have the process executable path.
for the same container. So we have two entries for the same profile.
That's what I'm dropping in the collector.
**Donal O'Sullivan** 38:55 Yeah. So, like.
**Juliano Costa | Datadog** 38:57 good in having all the other stuff that eBPF gets, because that's the way it is, but .
**Donal O'Sullivan** 39:03 Yeah, the thing is, though, you can have two processes that are using the same executable.
If that makes sense. So the path to the executable can be the same, but it can be two different processes running.
So if you filter it out, do you lose that granularity? It's probably fine. It's… this is actually something we're talking about in system… in, like, system namespace and spancy conventions at the minute, but Yeah, it's probably fine. Leave it with me, I can think about it for a bit.
So you're essentially removing process executable path.
**Juliano Costa | Datadog** 39:41 Well, give me a second, it's… I don't know if you all have other meetings. I'm just, starting it, and I'll show what I mean in a second.
**Donal O'Sullivan** 39:54 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 39:55 It just takes a while, because I'm on the call, and the demo is huge.
And I did a pruned right before the call.
**Donal O'Sullivan** 40:05 Nice.
**Juliano Costa | Datadog** 40:06 Great idea, huh?
**Donal O'Sullivan** 40:13 You're on Mac as well, Juliano, are you? Yep. Okay, cool.
**Juliano Costa | Datadog** 40:24 For some reason, the… the… hotel.io page, and the hotel.io page, there is this Ask AI, and I was chatting with it about the… the Docker Resource Detector… Docker Resource Detection.
And it kept saying to me that it doesn't work with Mac.
But I'm… I've been using for ages. I don't know from where this is coming from, but anyways… Interesting.
**Donal O'Sullivan** 40:56 soon.
**Juliano Costa | Datadog** 40:56 Thanks. Thanks, Pranathi.
**Donal O'Sullivan** 41:00 Is that in… is that in the collector? You're… so, like, the hotel collector, Docker resource?
**Juliano Costa | Datadog** 41:11 Sorry, oh, come on.
Sorry, I don't know what happened here. I'm just… Yeah, every time you need to show something to someone, things… Brady, so…
**Shenoy Pratik Gurudatt** 42:01 We call it the curse of the demo.
Yes.
**Juliano Costa | Datadog** 42:05 I… you know, I ran the demo on stage at KubeCon, so, like, I… I was on stage, and I just, like, make start.
Of course it was every… yeah, yeah, but it was, like, I tested right before, and I didn't need to Pull any image, or whatever, so… I knew it would work, but, yeah.
**Shenoy Pratik Gurudatt** 42:29 I just keep on… keep it running before the presentation. That's it.
**Juliano Costa | Datadog** 42:34 Yeah, for some reason, the… their profile's UI is not loading now.
So, I don't know what happened.
I'm getting a no healthy upstream.
**Donal O'Sullivan** 42:53 Oh.
**Juliano Costa | Datadog** 42:54 Oh, 503.
Yeah, that's the message from… From my boy. Okay, yeah, I… we can continue the discussion, offline.
Thanks, Far.
**Donal O'Sullivan** 43:12 Yeah, no worries.
**Juliano Costa | Datadog** 43:13 pristine.
**Donal O'Sullivan** 43:16 No worries at all.
**Juliano Costa | Datadog** 43:18 Cool.
**Donal O'Sullivan** 43:18 See you later, guys.
**Juliano Costa | Datadog** 43:20 See ya.
Cheers.
