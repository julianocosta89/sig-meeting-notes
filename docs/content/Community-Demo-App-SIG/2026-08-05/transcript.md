SIG: Community Demo App SIG
Date: 2026-08-05
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:00 Hello, hello!
**Felix Felix (IBM India Pvt Ltd)** 01:08 Hello.
Hi.
**Shenoy Pratik** 01:12 Felix Juliano.
**Felix Felix (IBM India Pvt Ltd)** 01:14 Thank you.
**Juliano Costa | Datadog** 01:15 Hello, hello?
How's everyone?
**Felix Felix (IBM India Pvt Ltd)** 01:19 Yeah.
**Shenoy Pratik** 01:20 Good.
I'm rocking the new beard.
Inspired for.
**Juliano Costa | Datadog** 01:27 Oh my god.
If I, if I let, if I leave my mustache, yeah, my, my wife, would pick me out. So, I'm allowed only in November.
**Shenoy Pratik** 01:41 That's me.
**Juliano Costa | Datadog** 01:43 That's the month I let my massage grow, but yeah, other than that.
And my father has a mustache, so she keeps saying that, huh, now you look like her father.
So, yeah.
Wow.
Cool.
Or not cool.
Oh, where… where are you guys based? I'm melting down here.
**Shenoy Pratik** 02:19 It's pretty hard in here as well.
Seattle area.
But our heart… the hot here is, like, 20s or 30s.
**Felix Felix (IBM India Pvt Ltd)** 02:33 In Bangalore, it's, normal temperature, it's raining.
**Juliano Costa | Datadog** 02:38 Oh.
I, I, I wish we had a break.
So… Okay, let's, let's stop business.
Peter came to me with a K6 issue that I typed Shenoy there.
where K6 has a different licensing, so hopefully we won't go to jail, but, yeah.
In theory, we are breaking the license, because we are redistributing K6.
So, I opened an issue on the CNCF repo to raise that, and I think the Grafana folks are already aware of it, so let's… Let's wait to see what… what CNCF will, do whenever they… because the… I just create the issue, so they are not even aware of it.
The Grafana folks are aware, because I think, Matt, that was the Grafana guy that opened the case here.
And he was like, yeah, I'll loop everyone in, so they are already aware, but we need to wait CNCF action, so I think… I think we are good there, and I don't think it will be a problem.
But… Just so… just so everyone is aware.
Other than that, for the agenda, I think we need to discuss one thing that, Felix briefly mentioned to me, on Slack. I don't know if he, I don't know if you discussed with Shenoy also.
**Felix Felix (IBM India Pvt Ltd)** 04:41 Yeah, I discussed with him as well, I messaged him as well, so I created a PR after his… a draft PR after, he suggested to do the same. Yeah, if you want, I can demo how it happens, and I have… something working. If you guys are okay, I can show it.
Wow.
**Shenoy Pratik** 05:04 Yeah, that would be great.
**Juliano Costa | Datadog** 05:06 Okay.
**Felix Felix (IBM India Pvt Ltd)** 05:07 Soon.
Are you guys able to see my screen?
**Juliano Costa | Datadog** 05:13 Yes.
**Felix Felix (IBM India Pvt Ltd)** 05:14 Okay, so, yeah, the same master mishap. I added, you know, more requests, so we can see what exactly, you know, for different type of requests.
what kind of response we are getting, okay? So, this is the first one. Okay, here, the response is as expected. Sometimes, I have seen it behave immediately. For example, let me execute the request again.
Okay, it's exactly us there yet, okay. So, let's try another one. Okay, so the binoculars also… I'm getting, so this is an actual LLM, which is running, like, it's a very small, large language model, which is trained using the cache data we have created in the earlier PR. So it's exactly… I think it's only 5 million parameters, it's 6 layers of attention stacked.
With some residual connections and all.
It… very small model, with 2048 is the context window. I mean, it… okay, so I'll get to there. So, because of the smaller context window, so I'm… now I have executed the query, show me all available products, okay?
In the store, okay? So here, because the tool core of the catalog Right? It's big. Because of that, when the context window is higher, when the… whenever the product catalog service is being called, it kind of loses itself, okay? Because 2048, it will easily reach that context window, okay?
For other requests, you can see it was, you know, pretty, okay-ish.
behavior.
But, with a 5 million model, I don't expect much. But anyway, I'm still trying to, you know, get maximum out of it. And if you are… if anybody wants to train it, it only takes 6GB of RAM. For inferencing, it costs similar to 1GB. So, I think it can be a very light LLM model, okay, anybody can run it in their laptop.
So, and the inferencing is also not taking a long time. Like, for example, if you run a Lama model, Llama 3 billion or 7 billion, in your laptop, it's gonna take a long time for the inferencing.
Yeah, so these are some queries that, you know, I have tested with almost all the queries, around, some 1,900 plus queries.
You know, some queries it works, some queries it kinda, you know, because it loses the context, it kinda… but for the shorter queries, you know, it kinda does what it is being asked to. For example, you know.
empty the cart, okay. After this one, I can try this. This is, you know, a medium-sized query.
With some, you know, some, different actions that I am asking it to do.
Some cases, it kind of works okay-ish. So, yeah, this is what I have.
Okay.
So, it kind of works, but… not very… Okay, so in this… some scenarios, it kinda, you know, empty the cart, and… You know, some basic instructions.
Oh.
So, it's not technically, responding a jargon, I'm surprised by that itself, because, I never expected a 5 million model to do that, but yeah. If you guys think it might be a good addition, so… I'm very new to model training and, you know, this kind of measure of work, so I'm learning in between ascertain, so… It was a nice, nice thing, yeah.
**Shenoy Pratik** 09:13 I have a couple of questions, like, are we solving the fuzzy matching problem that we had with cache with this? Is that the only reason we are adding this model?
**Felix Felix (IBM India Pvt Ltd)** 09:23 Yes, also, kind of, yeah.
And if you see any follow-up request, right, you won't hit the error, right, if the request doesn't match with the cache. So you will get a response for any request.
Might be… might not be 100% correct, but you will get a response from an LLM.
And we can also get metrics related to LLM inferencing, like, you know, token, time to decode, pre-fill, token throughput, or, you know, those kind of tricks.
**Shenoy Pratik** 09:58 Yeah. I just want to know, like, the ROI of adding a new service versus is it… just worth it to use cache, and then we also give model endpoints for live usage. Is that enough for the hotel Demo or not?
Because this is coming into the territory where it seems to be a good-to-have solution.
But not a necessary one.
That's where I'm coming at. But I like the custom model part.
If we can… if we can train a custom, like, we can, retrain some base model, which is, like, a small LLM or something.
**Felix Felix (IBM India Pvt Ltd)** 10:40 I tried, I tried. The small LLMs are all about… I think the smallest one was 0.5 billion, which…
**Shenoy Pratik** 10:48 Hmm.
**Felix Felix (IBM India Pvt Ltd)** 10:48 which will… I mean, it's at least 100 times bigger than what we have now. I made it small only because… so, I tried to use JAMA 4 billion and Quinn 3 billion. There was catastrophic forgetting was kicking in, and half the response was English, half of it was a different language, I couldn't understand what it was.
It was some Chinese or Korean, I don't know, or Japanese scripts. So, because of the catastrophic forgetting, I tried DPO and many things, it didn't… it was not just working, maybe I was doing something wrong.
So, what I did was, I built a custom tokenizer. So, this model only sees astronomy shop tokens.
Okay, it's only, for example, a GPT-2, which was a simple model back, you know, looking now, it had 50,000 plus tokens.
Now, this particular one only sees Astronomy Shop tokens, so it is only 2,048, distinct tokens are there, okay? And the tokens can be long, also. For example, I can share, I have a detailed report, like, I mean, there was, you know, these keywords in the Astronomy Shop, those, like, large product names, right? Those are even a single token.
And most of it is, like, tuned for JSON.
**Shenoy Pratik** 12:04 Oh, nice. Hmm.
**Felix Felix (IBM India Pvt Ltd)** 12:05 So, it's, so we can accommodate 2,000… that's why even with 2,000 for, rate, we are getting decent responses, right? Otherwise, we need 4,000 or, you know, about, like, 10,000 context window, because some tools have large responses.
So, yeah, so this… and that's why the model… the model size is 21MB, like, the file, model file size, and… it's… I think it's pretty small. The training… training with the 3 million data points took 6 hours… No, sorry, one and a half hours, with 6GB of RAM.
So I think if anybody wants to get into training or those kind of things, they can experiment with it, I don't know. Yeah.
**Juliano Costa | Datadog** 12:53 I have, I have two, two concerns on, on that.
One is the… the memory consumption, so we… have just reduced a bit the memory consumption with K6, like, 1 giga, basically.
And if we introduce that, we are… we're gonna be, like, 500 megas plus.
So, like, we are adding 1 plus 500 tones.
So we are back where we were. I know that we have the deployment models, so people would only deploy if they choose to, but this is a concern, and something that people actually care. This was something that the community raised multiple times, like, hey, the Demo is not runnable on my machine anymore, because it grew… So much.
**Felix Felix (IBM India Pvt Ltd)** 13:52 I completely understand, but so, like, still it's configurable. If you provide an API key for any update.
**Juliano Costa | Datadog** 14:00 Demo.
**Felix Felix (IBM India Pvt Ltd)** 14:00 You can still use those models, okay? This is just, I think we can have some configuration to, you know, make it, like, if the user really needs it.
For example, in… like, recently my company, you know, they started giving us the API keys and all, but before that, I wouldn't have paid myself for… to get started with all these things, right? If some… for example, if a user is there, like, who has to generate, you know, some kind of Agentic trajectories, Agentic load, okay? They can start with a simple project where they have to experiment.
when they… when they have a complete flow, they can actually start using a bigger model also. But to get into something, I thought it might be a nice addition from… because when I started on last year, we were working on a paper, to detect cycles in the Agentic trajectories. So at that time, I think we didn't have the API subscription, and we were using the open source models.
Like, trying to run them in the laptop, and it was a little bit painful. So if you have a complete system, like, where you can, you know, mock this, that's all.
**Juliano Costa | Datadog** 15:14 Matt?
**Felix Felix (IBM India Pvt Ltd)** 15:18 You know what I mean?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 15:19 So, I was gonna say that it's… it's an optional… Feature anyway, right?
So it's… it's… you have to run make-start Agentic to get the Agentic stuff in when you build it. It's still there, so I think your point's still valid, that it's adding memory usage when it's run, like, in its entirety.
But I guess my question is more like.
how, like, are we okay adding these extra things in that people can opt into? Because they could get bigger and bigger, but they do add more functionality.
I don't know.
**Juliano Costa | Datadog** 15:50 Yeah, but, I think just… Coming, circling back, back on that, like, I think that goes… that goes well with, what Shenoy posted on Asijo's, PR.
By adding that to the demo, are we adding a new scenario, something that we will show, something new for the OpenTelemetry folks, or just those three questions already enough to show how the AI traces and spins are created, how different tools are called, and how is the structure of the trace on those scenarios. So, like, adding more and more stuff.
Are we adding more scenarios that we are covering, or we're just increasing the size of the demo?
So, I think this is something that we need to keep in mind.
And another thing that I… that I want to… to bring to the group for discussion is the instrumentation, because unless you actually train your own model, I think most of the people do not do that nowadays.
But unless you do.
you do not have instrumentation on your LLM, so you just call an API and, like,
**Felix Felix (IBM India Pvt Ltd)** 17:11 L.
**Juliano Costa | Datadog** 17:11 I don't know, let's say, you call, OpenAI, and OpenAI may have instrumentation that you can also point to, to your backend, but the instrumentation that we are adding to the LLM service, I think it's too much detail, when you're adding custom stuff. So, it is cool, but, like, is that actually representing a real-life scenario?
So those are my two points. Like, yeah.
**Felix Felix (IBM India Pvt Ltd)** 17:47 Yeah, yeah.
**Juliano Costa | Datadog** 17:53 But I mean, we are a group, and whatever we decide, we go. Like, I'm just sharing the concerns, and if we merge and people say that it was a mistake, it's no problem, like, reverting and going back to what we had.
So, like…
**Felix Felix (IBM India Pvt Ltd)** 18:16 Yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 18:16 Is the instrumentation for, like, Agentic observability something that we want to add? Like, that would be the ad, right? Where we're actually observing a running LLM.
with OpenTelemetry.
**Felix Felix (IBM India Pvt Ltd)** 18:33 Juliano was saying that it's not someone a normal user would need, because they will just be called OpenAI servers.
we would never see the VLLM or, you know, the inference engine metrics from there, yeah.
Yeah. It's a lot of fun.
**Shenoy Pratik** 18:53 We can also think it the other way, like Matt said, like, we can go back and check if there is any extra telemetry that we can get, and that actually justifies the custom tokenizer work and the custom model work.
And if we can get some additional telemetry out, which is actually useful for real life and production cases, then we can probably for sure add this one. I see. Like, that will add more value to the users of the demo.
I know there are a lot of, Custom training organizations.
Which are niche and specific in their areas, like.
biomedical engineering and other pieces, which do not use the general LLMs. And there, they might want to… they today probably use something like MLflow or something for their training and inference telemetry, which is, like, very specific to ML models. Like, if we can get something from that domain here. That would be a real value add, and that's, like.
Something that we couldn't do with our existing setup.
So, maybe we can take some time and check back on that.
**Felix Felix (IBM India Pvt Ltd)** 20:01 So, like, I'm fam… like, a few of my friends work on Project LLMD, Which is, like, a router, like, it routes the same request to the same GPU, it makes sure, so that the KV cache will have a, you know, maximum hit rate. So, if we have the Kubernetes version, like, do you guys think if, like, if somebody's building their custom model, In that case, like, we have an application, okay, the successive request.
are going, you know, being routed via LLMD or something, and it gets hit on the same KV cache. Right now, our model, it doesn't need a GPU, the CPU is more than enough, but, like, you know, I'm thinking of a very niche scenario that, like, Shenoy just said, right?
If it might be useful.
**Shenoy Pratik** 20:52 Yeah, I'm looking at liability. Cool.
**Felix Felix (IBM India Pvt Ltd)** 20:55 Yeah.
**Shenoy Pratik** 20:56 Oh.
Yeah, people do track KV caches, and that's the thing that they use even for the large language actual training models.
**Felix Felix (IBM India Pvt Ltd)** 21:06 And one other thing…
**Shenoy Pratik** 21:07 tree.
**Felix Felix (IBM India Pvt Ltd)** 21:08 I was working on was, like, scheduling of requests, like, with… if you have different users, like, like, different tires of users, how do you… how do you design a scheduling algorithm so that the tire… highest tire user, will have the lower latency?
suppose that all the requests will be coming to the GPU in a queue, and you will always do some kind of batching in the GPU, right? So, we're working on scheduling algorithms. At that time also, we… we really never had an application, real application, where we could test it out.
like, how a user will send requests. If OpenTelemetry Demo has such a feature where we have a load generator, natural language load generator, which will trigger the agent.
And, you know, the NL request will, you know, get to some LLM calls. If that can be, like, with some request, right, or something, right?
**Shenoy Pratik** 22:04 I remember, like, you were planning to add load gen anyway, right?
**Felix Felix (IBM India Pvt Ltd)** 22:08 Yeah, well, that's, that's when I stumbled upon…
**Shenoy Pratik** 22:12 handle it.
**Felix Felix (IBM India Pvt Ltd)** 22:12 cash issue,
**Shenoy Pratik** 22:14 Hmm.
**Felix Felix (IBM India Pvt Ltd)** 22:15 Yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 22:18 So, one general question, I think, related to this is, do we know the profile of the average user? Like, obviously, people complain they couldn't run it on their laptops, but I would imagine there's a good amount of users that do run this in, like, a larger Kubernetes environment that could allocate extra memory towards it. Just a general question, maybe for Juliano and Shenoy, like, do we know what our average user profile is like for this app?
**Juliano Costa | Datadog** 22:43 So, this is actually a… this is actually a problem of not tracking users, right? One thing that I know is that vendors use it, because whenever you go to conferences, you see the demo running.
So, they use, in big Kubernetes clusters. When Pierre was at CONICOM, I know that he had a demo running for, like, months.
So they have a live demo running all the time. I think Jaeger has a version of the demo also running, so if you go to jaegertracing.io, you can navigate to the hotel demo and see the data.
But those are, like, projects and vendors. And the problem is that we never talk much with, Yeah. So, Charles just said that they also have Incortex. So, the thing is that we do not… almost never talk with the end users.
Or, like, people that are not representing vendors?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 23:55 Yeah.
**Juliano Costa | Datadog** 23:57 One… so, I was writing the Delta Demo 3.0 release, and then I went to the forks of the demo, and there is one fork of the demo.
The, the one that, with most stars, is from a guy that, that, forked the demo and created a course on top of it.
So he uses the hotel Demo, on a course. I don't know exactly what he's teaching and what is the course about, but his REPL has, a lot of stars, so it's the most starred, starred, project forked from the, from the demo.
So, like, I think people are using the Demo in different ways.
Won't be able to actually know.
**Felix Felix (IBM India Pvt Ltd)** 24:48 in IBM, Instana… of, Instana is, it's like, you know.
Datadog of IBM. So, they… they… they use it to show the loads and all that. They have one more application called Robot Shop, which is kind of similar to Astronomy Shop.
Instead of astronomy things, they buy robots. Okay, so that's the only difference, but it's very similar. Yeah, they have these two applications to show the customers their features.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 25:21 Yeah, I've just always… Church, yeah.
**Shenoy Pratik** 25:24 Also, we have seen the extremes, right? We have the initial users who are not from big vendors or projects, but also want to try it out.
So, that's where the memory issues have come up.
On the other hand, like.
If you go to the vendors part, I believe that most of them will have an API key to some, LLM from APIs.
**Juliano Costa | Datadog** 25:49 I… Honestly, I don't know if everyone would deploy the demo on an event like KubeCon that is a week.
And let the login hit the API key over and over,
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 26:05 That's a good point. Just a demo.
**Juliano Costa | Datadog** 26:07 Yeah, I think they would use, like, the data set for a specific time and just showcase.
I like the idea. I like the idea of having an LLM. I think it shows a new use case.
I'm just… my only concern is memory usage, but again, we have the option to deploy either the demo or the Agentic demo, so…
**Felix Felix (IBM India Pvt Ltd)** 26:37 Yeah, and I would like all of you guys to test it out if there is time, and give me any feedback that I can work on.
Well, yeah.
I'm having a lot of interest in it now, trying out different things, so yeah, I can try it.
**Juliano Costa | Datadog** 26:56 I have a… I have a suggestion.
What do you… what do you all think about… possibility of disabling, fraud detection, accounting, and Kafka whenever we deploy the Agent Inc.
Are we… Using those services in the Agentic… Agentic flow, alright?
that… that reduces some… some usage there. Kafka is huge.
How much is Kafka on the demo currently?
I don't remember.
620… M.
But, like, it's 600 from Kafka, 300 from fraud detection, and 160 from accounting.
Boom.
Yup.
**Shenoy Pratik** 28:05 Oh, that's cool.
**Juliano Costa | Datadog** 28:06 Got it.
**Shenoy Pratik** 28:07 introduces.
But also, like, another point of view, thinking about this full, full compose, right?
**Juliano Costa | Datadog** 28:15 Yeah, yeah. We never released the full, full one.
**Shenoy Pratik** 28:19 Yeah, yeah, man.
**Juliano Costa | Datadog** 28:21 Currently, there is no way… Go ahead, Charles.
**Charles** 28:25 Can we run the inference without, you know, with the model, without, you know, running the training? Because inference only takes one gig.
should be something that runs all the time, right? And then you only need to train once.
**Felix Felix (IBM India Pvt Ltd)** 28:39 Yeah.
So, right now, like, I have loaded a trained model. It's only inference that we are doing.
I was just saying that if you have the data for someone who wants to retrain it with an additional data or something, it only takes 6 GB. For running the inference, it only takes, you know, 1000MB.
**Charles** 29:02 Oh, oh, oh, okay, wow, okay, so it's not too much then.
**Felix Felix (IBM India Pvt Ltd)** 29:07 Yeah, it's a pretty small model, it's only 5.2 million parameters.
**Charles** 29:15 Yeah, sounds like what Julia, Juliano is proposing is good. We can adjust it. I mean, for people who are running it in Kubernetes, we can put, like, 20GB A memory there, for sure.
**Juliano Costa | Datadog** 29:29 Yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 29:32 Yeah, it's just having the flags to enable, disable stuff.
**Charles** 29:38 Cool.
**Juliano Costa | Datadog** 29:39 Yeah, I… I would vote for that. So, what… what if… For… at least for Docker.
for the, make start image intake.
We run the… Make start minimal.
Agentic.
And then, for that, we… We drop Kafka… Accounting and fraud.
and spin up the LLM with, I like that, yeah.
Okay, let me add that to the meeting notes. I can't talk and write at the same time.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 30:43 I had a question, Juliano, if we have another minute.
**Juliano Costa | Datadog** 30:47 Yep.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 30:48 Have we ever considered something like Chaos Monkey, like a feature to randomly introduce? Because we already have failure scenarios in the app.
Have we ever thought about putting something in to just kind of loop through those and turn them on and off?
**Juliano Costa | Datadog** 31:04 One thing that, forgot his name. From the docs.
Jesus.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 31:16 We haven't we have…
**Juliano Costa | Datadog** 31:18 No, no, I forgot.
Anyways, severing. Okay, sorry. One issue that we have from severing opened, kind of… tries to bring that. He wanted to have, like, a timer on the… on the feature flag.
So let's say, enable add failure for 30 minutes, and then just for 30 minutes, you have a failure on that service, and then things like that.
The guy that contributed the flag BUI, which is implemented in, Elixir, and, like, nobody in the world, programs in that language.
He contributed and did one or two PRs and then, disappeared.
Wicked.
what happens, like, people change priorities, it's fine, but we never had a chance to… to implement it, so… now that we have AI, maybe, Cloud or codecs can… can influence such a thing?
It wouldn't be the same as a Chaos Monkey thingy, but, I think it would help a bit. Or maybe we can even… we could even, introduce, like, enable randomly thing, like, something like that.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 32:40 I like the timer thing, because I've done demos where I just need to show, like, some error spike.
And I'll, you know, you forget to turn it off and whatever, it's no big deal, but then you go back and you have, you know, 2 days of 100% error rate. What… do you know what issue number that was, or maybe you could send it to me offline?
**Juliano Costa | Datadog** 32:58 Yeah, I'll… I'll look through and I'll send it to you.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 33:03 Cool.
**Juliano Costa | Datadog** 33:05 Cool.
Thanks, everyone.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 33:07 books.
**Juliano Costa | Datadog** 33:09 And the ducks right.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 33:09 No, no, on the docs front, do you think it makes sense to take the best of all those PRs and combine them?
**Juliano Costa | Datadog** 33:17 Yeah, one thing that I didn't want to do… so, you and two other users, opened the PR to, for instance, fix the Docker Compose commands.
Yep. The two other users are new… new contributors, so I didn't want to actually close their PRs. We need more contributors.
So I was… I'm holding off yours. That… actually, yours is ready to go, but, like, the guy opened before, so I would rather have him, like, circling through, going, addressing the PRS, so, like, he gets used to and comfortable in contributing.
And then we have… but I did that. I think I mentioned that on the PR, saying that, hey, we have this other PR, if the user doesn't come back in a week, we go on with yours.
Just so we have more… more people involved.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 34:10 Yeah, I don't mind that at all. I'm not… I don't, I'm not keeping track of my PRs and stuff and getting an ego about it, don't worry. That'd be great.
**Juliano Costa | Datadog** 34:19 Cool. Cool. Appreciate it.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 34:22 Yeah, of course.
**Juliano Costa | Datadog** 34:24 Awesome. Ben, yeah, see you all next week.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 34:30 Thanks.
**Juliano Costa | Datadog** 34:31 Cheers.
**Shenoy Pratik** 34:32 Ex…
