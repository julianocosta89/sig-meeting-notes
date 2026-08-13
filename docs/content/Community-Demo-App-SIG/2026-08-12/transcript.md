SIG: Community Demo App SIG
Date: 2026-08-12
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Felix Felix (IBM India Pvt Ltd)** 04:01 I… I don't know.
**Donal O'Sullivan** 04:06 Hey, Felix, how are you?
**Felix Felix (IBM India Pvt Ltd)** 04:09 All right.
I like it.
**Donal O'Sullivan** 04:18 I don't think, Giuliano's gonna join…
**Felix Felix (IBM India Pvt Ltd)** 04:23 Okay.
**Donal O'Sullivan** 05:07 I don't have anything to discuss. Did you have anything, Felix?
**Felix Felix (IBM India Pvt Ltd)** 05:13 Yeah, I… I had a draft PR, which I opened, okay, so…
**Donal O'Sullivan** 05:20 Yeah.
**Felix Felix (IBM India Pvt Ltd)** 05:21 Like, I think you were there in last meeting, right? Where, trying to show a demo LLM.
**Donal O'Sullivan** 05:29 I'm not sure. I wasn't there last… was it last week?
**Felix Felix (IBM India Pvt Ltd)** 05:32 Yeah, yeah, yes.
**Donal O'Sullivan** 05:34 Oh, I wasn't there.
**Felix Felix (IBM India Pvt Ltd)** 05:35 Okay, so I'll give you some, context. So here, so in the initial agent, to help the users who doesn't have an LLM subscription, we were, we were creating, the cache files.
Which will contain the request and response, okay?
So, we will match the request with any similar request, not exactly. Like, we have a threshold of 85%. If two requests are 85, like, it's a sentence sequence matcher.
if, the sequences of the request, like, the string similarity, it matches, like, 85%, we will send out a recorded response, okay? This is to, eliminate some, you know, few, you know, brackets if it is missing, or some characters if it is newly added by MCP.
To match the strings, that's why we added the matching.
So, the string matching is of N-square complexity, and You have to search for each request in each file, each item, right?
So, in… whenever… when I added load generator, this became really complicated, because you will have… it will send tons of requests, you want… you just don't want them all to fail, right? You want them to succeed.
So, I created a list of prompts, like, it's 143 unique prompts.
But it will involve… each will involve multiple LLM calls. So there were around 400 to… nearly 500 unique LLM calls, which is happening in this… yeah, so the cache becomes really huge, and so I created a PR, which, Giuliano said, because the number of, so… I cache, so I hashed the request.
And I used a file, for… to store the response of that particular request. So the lookup will be faster. I can just… search for the hash of the request, right? If the file exists, then I can just send the response.
So, but this created a lot of files. So to prevent it, like, anyway, if I'm uploading files, it will be too many, too many new lines. So, to prevent it, I thought I will just train a custom LLM, And that is what is included in the PR. Last week, I was demoing that.
So, you can run a… so it's a very small LLM. You can say it's memorizing everything, it's not, actually learning anything. For example, if you ask the price of any one quantity, and the price of Y quantity, it won't… it won't understand the difference. It will just give you the price of one quantity as the… Okay, so it doesn't really understand stuff, it just memorizes from the training data. So it's a 5.2 million parameter. I was… so the concern was, we were trying to reduce memory by moving from locus to K6, around 1GB was saved, but if you are adding new services, it will cost more memory.
So, I… benchmark this, this, new LLM against, different memory sizes in my local machine, like 500MB, 1GB, with 1GB of RAM.
And, along with the agent, MCP, and chatbot. So, I think they hold pretty well under… even under 500MP.
like, the Demo LLM. So, the additional memory requirement will be 500MB for LLM, and the agent and MCP and chatbot, agent has been reduced from 500MB to 300MB.
then MCP is reduced from 500 to 200, also chat… also chat port, okay? So MCP and chat port is reduced from 500 to 200MB.
And, another 200 MB is reduced in the, agent also. Okay, so now, I think… With this, we can comfortably serve up to 40 requests per minute with 1GB of Demo LLM, and around 20 requests per minute for Not 20, around, yeah, nearly 20 requests per minute for, 20 requests per minute.
Sorry.
**Donal O'Sullivan** 09:56 Yeah, but… so what's the total resource usage, then, when you're running the whole, like, astronomy shop on your machine? Because… Like, I'd imagine running the demo and then running an LLM on top of that is gonna still take up quite a lot… like, that's gonna…
**Felix Felix (IBM India Pvt Ltd)** 10:11 No, additionally, with, you know, compared to the Agentic, Demo Agent Dick, you know, start Agent DIC, we consume 500 MB more.
**Donal O'Sullivan** 10:22 So it's gonna add another 500MB to running the astronomy shop in Agentic mode.
**Felix Felix (IBM India Pvt Ltd)** 10:26 Yeah.
**Donal O'Sullivan** 10:27 of… of REM. And what about the CPU pressure? Because I know running the demo can.
**Felix Felix (IBM India Pvt Ltd)** 10:35 Yeah, CPU usage is pretty high, yeah.
**Donal O'Sullivan** 10:37 Yeah.
**Felix Felix (IBM India Pvt Ltd)** 10:38 TP usage is pretty high, because, it's our matrix multiplication since I don't belongs.
**Donal O'Sullivan** 10:44 Yeah, yeah, yeah. Like, my concern here would be when I run the… the hotel demo locally on my laptop, it's already kind of maxing out, and, like, I've got 32GB of RAM and 12 cores.
Okay.
**Felix Felix (IBM India Pvt Ltd)** 10:59 I'm also using a similar setup.
But, yeah, it didn't turn on my fan, so I didn't check the complete usage, but in the… if I… I have pasted the link in the chat, you can check the CPU usage and…
**Donal O'Sullivan** 11:15 What, what, what laptop are you using?
**Felix Felix (IBM India Pvt Ltd)** 11:17 Yeah, yes.
**Donal O'Sullivan** 11:19 I use… see, I'm using a Linux machine, I have a ThinkPad, so…
**Felix Felix (IBM India Pvt Ltd)** 11:23 Is it possible, can you test it out and know…
**Donal O'Sullivan** 11:26 Yeah, yeah, for sure, yeah, I can. I'm just… so just looking at the code there, like, where exactly is the LLM? So you have LLM.
**Felix Felix (IBM India Pvt Ltd)** 11:32 There is a new service called Demo LLM.
So, it, it's under, so, it's a new, new service itself, SRC…
**Donal O'Sullivan** 11:42 Okay, so it's… so the model… it's model… so the… it's model.pT is the actual…
**Felix Felix (IBM India Pvt Ltd)** 11:47 Yes, at weights.
**Donal O'Sullivan** 11:48 language model, yeah.
**Felix Felix (IBM India Pvt Ltd)** 11:49 Yep.
**Donal O'Sullivan** 11:50 Okay.
**Felix Felix (IBM India Pvt Ltd)** 11:51 So, instead of having a lot of cache files, we just have one file, and
**Donal O'Sullivan** 11:56 Yeah, yeah, no, I'm excited, too.
**Felix Felix (IBM India Pvt Ltd)** 11:58 Wonderful responses, but it's giving occasion responses.
**Donal O'Sullivan** 12:04 Yeah, okay, yeah, yeah, like, I can definitely take a look at this, and I will review it, for sure. What's the advantage to doing this over the way it's currently done?
**Felix Felix (IBM India Pvt Ltd)** 12:16 So the advantage is any user will get at least some LLM-generated response, so that's one advantage, for any request. Otherwise, you will only get responses for requests which are already in cache, so even if you change the request a little bit, like, even if you change the words used to some kind of, you know.
**Donal O'Sullivan** 12:35 Nice point.
**Felix Felix (IBM India Pvt Ltd)** 12:36 you will… it will be a failure, but you will get a response here. The… another advantage.
**Donal O'Sullivan** 12:40 Yeah, yeah, exactly, yeah. So, like, with the cached one, you have to have the exact…
**Felix Felix (IBM India Pvt Ltd)** 12:44 Thanks.
**Donal O'Sullivan** 12:45 like, yeah, but this way, it's because it's… yeah, you're still using an LLM, you can just kind of send something somewhat…
**Felix Felix (IBM India Pvt Ltd)** 12:51 Yeah, this is using a custom tokenizer. So, for example, a GPT-2 tokenizer, which is really primitive. It had around 50,000 tokens. So the lookup table, each token will be some 256 IS embedding, right? And so the lookup table itself becomes two… 2, you know, 50,000 into 256, that many, right? Yeah.
But here, I used Astronomy shop-specific keywords. So, even large words in the astronomy shop is just one token. So, there is only 2,000 tokens. That's why the model size is really small. It's only 5… 5 million in parameter. So… that's the reason why it is fitting into a smaller model. And I have used the already collected cache as training data, so I had it handy because… so it was pretty, straightforward approach.
But, yeah, Another approach is you could get, these LLM-specific metrics, like, you know, time to generate first token, token to inter-token latency, then the, you know, pre-fill decode, time, those kind of metrics, which are LLM-specific, I'm not… so we had a discussion around, does it serve the astronomy shop Demo? But yeah, it might be an addition we could have, but yeah, we could get those metrics.
**Donal O'Sullivan** 14:18 Yeah. As in, like, it, like, so instrument the actual LM itself, right?
**Felix Felix (IBM India Pvt Ltd)** 14:23 Yeah, like, whatever you get in BLLM, like, inference engine, LLM inference engine, we could have the same, same metrics here.
**Donal O'Sullivan** 14:31 Yeah, that, like, yeah, yeah, for sure, that, I think, like, my only concern would be that the… this will tip the demo over, like, like, the resource usage will be quite severe, but it's still using the separate make target, like, isn't it? Yes, it's…
**Felix Felix (IBM India Pvt Ltd)** 14:47 Yeah, start Agenting.
**Donal O'Sullivan** 14:49 Yeah, yeah, yeah. Yeah, cool. No, like, yeah, yeah, sounds good. I can definitely, I can definitely take a look at it anyway.
**Felix Felix (IBM India Pvt Ltd)** 14:55 Yeah, so I can give you some heads up on what kind of errors you might expect. Like, when the tool response is too large, for example, list tools have a very large response.
And, sometimes it… the LLM gives you expected output, but sometimes it gives you not technically jargon, but, not correct output. But it will give you some kind of output.
**Donal O'Sullivan** 15:17 Yeah, because it's, yeah, it's a non-deterministic, so it's just going to give you…
**Felix Felix (IBM India Pvt Ltd)** 15:22 Yeah.
Yeah, because I'm using temperature as 0.7, so you… if you use temperature as 0, like, absolutely zero, you will get the deterministic output, but I'm using temperature as 0.7 by default, so it will give you some kind of variance in the output.
And the second issue is, it's not trained for a follow-up request. Like, you just give a request, it will give you a complete answer. If you ask a follow-up question, on top of the current response, it will mostly give you an empty response, because in training, we haven't seen that data.
model just hasn't seen that. But I hope in the future I can work on that, yeah.
**Donal O'Sullivan** 15:58 Yeah, okay, cool. Yeah, yeah, no, it definitely sounds interesting, like, the benefit is you don't have to have, like, all the cached responses, and it's a bit more… reliable from a user perspective to use the actual, the chat interface, I guess, isn't… is that the idea?
**Felix Felix (IBM India Pvt Ltd)** 16:17 So for any user to… for example, one other thing that we were working on was anomaly detection from the Agentic traces. Like, so the Agentic applications have a diverse set of anomalies, not exactly similar to microservice, where an error is either 0 or 1, right? You get an error.
Definitely. So here, the error can be partial as well. Like, it didn't complete, maybe the output is partially correct, not exactly completely wrong.
So, so those kind of scenarios are very specific to H&D applications. So, if someone who wants to test out their LLM more, you know, LLM in actual tool core scenario, they can plug in their LLM and use the Astronomy Shop application instead of the… our Demo LLM. They can test… so those… those are some kind of other, you know.
use cases, it might, help people.
**Donal O'Sullivan** 17:08 Yeah, yeah, to kind of, yeah, debug what they're trying to do. No, that's cool. Can you update the PR just with, like, the information you gave me around, like, the errors? I don't know, is it in the actual PR?
**Felix Felix (IBM India Pvt Ltd)** 17:17 Okay, so I… I have written a file, I have shared it with Juliano, and I'll share the same file with you in the Slack, is it… is it okay, or should I just update?
**Donal O'Sullivan** 17:27 I would just update the PR, because it just gives anyone who's, like, reviewing it a quick glance, they can see, like, maybe just have it, like, testing steps and, like, known issues or errors or something like that, just to make it easier. It's all in the one place, at a quick glance, you can see what, you know, what the steps are, if that makes sense.
**Felix Felix (IBM India Pvt Ltd)** 17:45 Okay, yeah, I'll add it.
**Donal O'Sullivan** 17:47 Cool. No, thanks, thanks, Felix. It sounds very interesting, so I'll… yeah, I'll… I won't get to it today, but I will… I will get to it tomorrow, I'd imagine. I can definitely run it and just kind of look through it.
So, But just all through diffs and stuff like that.
Cool.
I don't have anything myself, there was a few PRs that I reviewed, and I think I approved them. I think Juliana wanted me to look at some… stuff in the demo docs. Do you still have a PR and Demo? I think that was merged, was it?
**Felix Felix (IBM India Pvt Ltd)** 18:23 Yeah, it's not merged yet, so it was the documentation related to the Agent MCP and chatbot.
**Donal O'Sullivan** 18:31 Okay. Oh, yeah, yeah, yeah. So I think… you have approvals on that, though, don't you?
**Felix Felix (IBM India Pvt Ltd)** 18:36 I have approval from Juliano, but
**Donal O'Sullivan** 18:39 Oh, you might be waiting on the maintainers of the docks, I guess.
Yeah, hmm… Yeah, might be worth reaching out to them.
I think there should be a Slack channel.
Cool.
**Felix Felix (IBM India Pvt Ltd)** 18:57 Yeah, thank you, thank you.
**Donal O'Sullivan** 18:59 Alright, I have nothing anyway, so,
**Felix Felix (IBM India Pvt Ltd)** 19:04 Yeah, I'll really appreciate your feedback. I'll just,
**Donal O'Sullivan** 19:07 No worries.
**Felix Felix (IBM India Pvt Ltd)** 19:07 paste my design docs, as well as some, you know, about the LLM that I have used.
**Donal O'Sullivan** 19:13 Oh, yeah, yeah, perfect, yeah, great, great, Felix, thanks, I appreciate that.
Looking forward to reviewing it. It sounds quite interesting, so… nice.
**Felix Felix (IBM India Pvt Ltd)** 19:23 I was also learning, in the process, I'm not an expert in this, so I was just curious to, you know, it was really interesting to do this.
I was surprised that it worked.
**Donal O'Sullivan** 19:34 Yeah, yeah, nice, yeah, no, it's, yeah, it's kind of cool to run an actual LM in…
**Felix Felix (IBM India Pvt Ltd)** 19:40 Yeah, I mean, the small size, right, like, it is similar to any big iffels condition code, but… Somehow the model learned some, you know, correct grammar and all.
**Donal O'Sullivan** 19:53 Yeah, yeah, gotcha.
**Felix Felix (IBM India Pvt Ltd)** 19:54 I… earlier, I trained a simple, small LLM, like, QUEN3 billion, to, work in this astronomy shop. That's what I tried first. But the Q3 billion, it takes so much memory and all. I thought it will work, but it didn't. I tried to fine-tune it, but it didn't work because It, there is something called, catastrophic forgetting, where you'd retrain the LLM with some new data, it will forget everything that it has learned so far.
So it… it was not able to even, you know, predict the same language from end to end. So it was predicting English in the initial few words, then it was predicting some other languages, so…
**Donal O'Sullivan** 20:39 Weird. Yeah, yeah.
**Felix Felix (IBM India Pvt Ltd)** 20:40 Yeah, it was a huge failure, but maybe because I don't have enough data.
Yeah. But yeah, but this worked, I was really surprised.
**Donal O'Sullivan** 20:51 Nice. Cool. Yeah, looking forward to it anyway. I… I… I got a drop, so, I will… I will take a look at that anyway, ASAP, so…
**Felix Felix (IBM India Pvt Ltd)** 21:00 Okay, thank you.
**Donal O'Sullivan** 21:02 See you, Felix.
Have a good one.
