SIG: LLM Semantic Convention WG
Date: 2026-07-21
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:31 Hello, Trask. Hello, bots.
**Trask Stalnaker** 01:35 Good morning.
**Liudmila Molkova** 01:40 I hate when I join and there are only bots there.
**Trask Stalnaker** 01:44 Yes, I already kicked the one out that let me.
**Liudmila Molkova** 01:49 Yeah.
**Trask Stalnaker** 01:54 Yeah, I don't think… I guess it probably won't be any better with the new, when we move to the CNCF Zoom stuff.
Have you seen that happening?
**Liudmila Molkova** 02:08 Yeah, the one that needs you to log in first.
**Trask Stalnaker** 02:12 Okay, so it does, so maybe that'll fix our bot problem.
**Liudmila Molkova** 02:16 Maybe, but I would imagine some of them are coming from services like this Otter AI.
So, I would imagine it… figuring out how to create a Zoom account, or link your existing one, or something.
But it's… I guess it's a good, like, I don't know.
gate, in a sense, how do you care enough to even bother?
**Trask Stalnaker** 02:42 Yeah.
**Steve Rao** 02:43 Hello?
**Liudmila Molkova** 02:44 Hey, Steve. Oh, sorry.
**Trask Stalnaker** 02:46 Hey, Huxing.
**Steve Rao** 02:47 Yeah, hi, folks.
**Huxing Zhang** 02:48 Trask and Liudmila.
**Liudmila Molkova** 02:52 Okay… No, let's… Get started… See a couple of topics… Great. R.
maybe I will add one more topic. Huxing, I want to talk about your Block post draft.
It's awesome, but I want to figure out what we do with the Trask conformance test there.
**Huxing Zhang** 03:37 Yeah, I was planning to talk about that also.
**Liudmila Molkova** 03:42 Awesome.
Cool. Any other topics?
Okay, then let's dive into… The first one.
**Steve Rao** 04:08 Oh, yeah.
Yeah, there is a PR to support.
Real-time audio token.
**Trask Stalnaker** 04:17 Yeah, I dropped this in there, because I just discussed this with Ankit, yesterday.
Hmm.
And so, wondering if this is related… if this is related or helps your… Question.
**Steve Rao** 04:35 Yeah, yeah. We have a similar, yeah, use case. Yeah, they want to, achieve… Capture audio or video, and they want to, see the audio or video in a span attribute.
being… Yeah, you know, our… A plan for.
**Trask Stalnaker** 05:04 Yeah. Oh, go ahead.
**Steve Rao** 05:06 Yeah, and the sun… I think, yeah, maybe in China, there are some companies, they want to, do some intelligent glasses.
And, something like, they ask a question, to the glasses, and the glasses can, understand, use the model to understand the question.
of people, and to give the answer, like, STTT to LLM, like, TDS, like, something like that, this.
**Trask Stalnaker** 05:44 So, I think that's similar… I think Anket also has, wants to capture, well, he specifically is interested in, audio.
At this point, but also wants to capture the audio.
Files… In the responses, on the span.
**Steve Rao** 06:10 Yeah.
Yeah, okay.
**Trask Stalnaker** 06:14 sure, I haven't looked at his PR yet, so I don't know if he split.
things out, and what exactly is in this PR.
**Steve Rao** 06:24 Hmm.
Okay, yeah, I can, check it out, later, and, if I have any questions, I can, leave my comment, yeah.
**Trask Stalnaker** 06:37 Yeah, I think he's going to join the, the… the next meeting in an hour to… Potentially just give an overview of this, and so if you want to watch the recording later, That might help also.
**Steve Rao** 06:56 Okay, thank you.
**Trask Stalnaker** 06:57 I know he's… wants to just kind of… Get people interested in the topic. So it's great to hear that you also are Interested, so reviewing that would be really helpful.
**Steve Rao** 07:11 Okay.
**Liudmila Molkova** 07:15 Oh, okay, there is a new… Span. That's awesome. I think that… Text to speech.
Yeah, I think the real-time API is not, well… Aligned with our inference plans.
**Trask Stalnaker** 07:34 Yeah, we talked about that, I… I think at this point, my, Recommendation was, like, so rea… with the real-time… with… basically with streaming.
But the streaming could be either… Voice or text, and we don't really support text streaming anyway. Like, we're not capturing the individual events, but we still capture everything on the span at the end.
**Liudmila Molkova** 08:14 But it's… it wouldn't… Would it even work?
like… Oh.
Nice long spot.
So… Or hysteria.
Time… Create a translation, create a speech… text-to-speech, right?
Okay, so this one… ish.
Fine. I remember seeing maybe it was some deprecated API that you essentially give a chunk To the request, then it… uploads the… sorry, it… It… Yeah, maybe this one.
File. Okay, file is good.
No, okay, then it makes sense. I was kind of worried that if it's a ton of small fragments.
then… Our inference wouldn't work.
Right, it should be fine.
**Trask Stalnaker** 09:51 API he showed me, and, we're gonna get into it more when he's on, hopefully on the call, the next call, was still… Just a one request.
being sent, and then streaming, you know, like, chunks, basically, for the response, and then the response ends. So it didn't… seemed like… like, because I was worried when he was first describing that it was, like, we had to deal with bi-directional streaming, and… complicated stuff.
But it felt like we could keep it simple.
**Liudmila Molkova** 10:29 Okay, yeah.
Cool, thanks. I'm kinda… the one thing I'm worried, and we should probably talk with Zankit about it, that… We kind of… have the inference. We're starting to use inference.
Maybe.
We should separate, even… Further, and if this, this is a different span.
Then we should maybe call it… Something else?
Chunky… oh, chunking strategy.
Oh, this is, like, the bi-directional streaming. It probably happens inside, and we just don't want to expose it to users, right?
Okay, it has a unique set of parameters that… Inference would not normally have a unique set of response formats.
It returns a different thing.
It's a different span, but it's also an inference bit of a different sort.
**Steve Rao** 11:56 Okay, yeah, yeah, but for our requirement, yeah, we also start from inference band.
To, support multiple… a multi, model.
Information for our users.
**Trask Stalnaker** 12:15 Ludmila, if you go back to the API you were looking at.
So these are specific APIs… I think the one that, at least Anko was looking at was more the… was the real-time audio… Where it's, you know, more open-ended than just, like, hey, give me a transcript of this, or give me a translation of this.
**Liudmila Molkova** 12:50 Oh, I… okay.
And then this is the… And it's a layer, right? It's the protocol.
Level.
**Trask Stalnaker** 13:02 Yeah, it's a…
**Liudmila Molkova** 13:11 Oh my goodness, you start the call with OpenAI.
You have a tool called OverTranslation.
Yeah.
Well, that's a big new area.
**Trask Stalnaker** 13:44 Yeah, I'm not sure it's this either, we'll have to… Let's see, from, on Kit, because it was… the API looked different, it was like, you create a connection.
sending… your initial… piece of it. It looked very… the API he was framing me looked very much… very similar to the inference stuff.
As opposed to, like, this call stuff where you're, like… the call was what I was worried about, of, like, this true bi-directional… this, although maybe… yeah. Sorry, I'm probably just gonna add more confusion than… Useful.
Input.
**Liudmila Molkova** 14:32 Okay, so then, let's talk with Ankit about it. Steve, do you have any particular, like, questions or thoughts on this?
**Steve Rao** 14:44 Mmm… yeah, no, maybe I need to, yeah, check out the PR.
Sorry, I have another question as the second, the second problem.
Yeah, for the first question, I need to check out the PR is out later, and the… The second question is, what kind of spends need to have a JNI conversation ID?
I, I found, in our, Semantic conventions, in inference span, and, invoke agent span.
It… content, JNI conversation ID.
Yeah, I have a question. Why in, workflow span.
it doesn't have… it doesn't contain the JNI conversation ID.
In… Yeah, why I, bring this question, recently we… We want to, achieve, evaluation, for SPAM.
And, I found in inference span, in Work Agent Span, and Workflow span, they contempt, input message, output message.
**Liudmila Molkova** 16:08 Yes.
**Steve Rao** 16:10 But, in invoke flow span, it doesn't contain the conversation ID. If we want to, correlate the, span to the session or conversation ID, we can achieve it. So, this is my, question, the background.
**Liudmila Molkova** 16:33 Yeah, so, we have… I think Korea, or maybe a… Maybe a little bit more frameworks that emit workflow span.
This is the up in the eye… adjuncts?
There is, indicator is… Length chain… Andreas… oh.
Yeah, yeah, maybe Cruelier.
These are the four that can emit it, and… I think only 80K?
has, something like this. They call it session, of course.
there is nothing for LinkChain or QueryI, and I don't remember OpenAI agents if they have it, so the reason is not that it's not useful, there isn't… it's not… really capturable in general case. I have no objections about editing it and saying that it should be populated whenever The instrumentation has this notion.
Or we can, At some point, leverage context sculpt attributes and say that if the users, like, the callers of the framework can push it into context, then we would then stamp it.
But… I… I think that the core part that we are missing is defining what conversation is.
**Trask Stalnaker** 18:16 And right now, some of the inference APIs have their own conversation ID, is that right?
**Steve Rao** 18:26 Mmm, yeah, yeah, maybe, in some scenarios, a user, they can, pass the conversation ID.
When they, invoke the LLM API.
For example, a user, they can use the JNIU tier.
to, instrument their application, and they can, pass the conversation ID by themselves.
**Trask Stalnaker** 19:01 And does that have to be, if you're passing it back into the… inference, the LLM, does it have to be a conversation ID that the LLM originally gave you?
Or is it just…
**Steve Rao** 19:18 No, yeah, maybe this, this, field, should, store by, application.
the AIM.
According to my knowledge, it doesn't respond to a conversation ID, something like this.
**Trask Stalnaker** 19:50 I see what you're… so, Ludmila, you're… Maybe it's… maybe I'm overstating that the inference clause Because that would be nice, because that was my worry, like, is I thought that if inference calls had their own, like, conversation ID that meant something to the… LLM itself.
then I was worried how we would…
**Liudmila Molkova** 20:14 Mmm.
**Trask Stalnaker** 20:16 Like, if we… Create or propagate our own… How does that… does that cause conflicts there?
**Liudmila Molkova** 20:26 I see, okay, so the responses still have it.
I'm just checking, because I, at some point, I thought that maybe nobody does.
Let's check another one.
Cryout.
I'll check later, I can never find reference.
I'm here.
So then… There is a conflict, So if we… okay, so there is no semantic conflict between using the same attribute for conversation AD, for… Client-side agents, or inference agents, and, like, internal agents?
But there is a problem with… Making it a context scoped attribute.
And letting users set it.
**Trask Stalnaker** 21:50 Well, even… I mean, so you would… potentially have a conversation ID on an invoke agent span, or some parent span.
And the child LLM call would have a different conversation ID.
**Liudmila Molkova** 22:09 And that's fine.
So, like, if you stamp your conversation ID only on your spense, right? About your… So I had this conversation, AD, but you Trask did some other work, and you had a different conversation, Edie?
**Steve Rao** 22:33 Yeah.
**Trask Stalnaker** 22:46 A little confusing, but yeah, it makes sense.
Yeah, I guess that same thing applies to, like, session IDs.
**Liudmila Molkova** 23:07 If they are any different from conversation, it is. I still… I'm still, yeah.
**Trask Stalnaker** 23:12 Yeah, but I was thinking more in terms of, like, just not Gen AI, but session IDs and.
**Liudmila Molkova** 23:17 Hmm.
**Trask Stalnaker** 23:18 General apps where, I mean… I often think of session ID being, like, applying to the whole request.
But you could have session IDs for outgoing calls that were different.
**Steve Rao** 23:42 Okay, yeah. Yeah, you meant, yeah, just, because, the… the sub-agent may all have its own conversation ID, so in workflow, it doesn't contain this attribute.
**Liudmila Molkova** 24:01 Yeah.
**Steve Rao** 24:02 Okay.
**Liudmila Molkova** 24:08 We could, in theory, find ways around it, but I'm… I don't want… Like, if the only way it's used is by users, stamping it.
It's not ideal.
But… but we have enough examples to… Added to workflows, fun!
With caveat when available, when framework supports it.
This… this is non-controversial.
**Steve Rao** 24:44 Hmm… Okay.
Hmm.
But, yeah, but, I… my question is, yeah, in some scenarios, yeah, if we want to evaluate the span.
Yeah, in, workflow span, it, contems the input message and output message, and we use the, LLM as a judge to eva- evaluate the, the span.
without the conversation ID, yeah, some, some, sometimes it's, We can't… Finished the, session type evaluation.
Yeah, something like, there are different, there, there are some, traits.
And, each trace, it has its own workflow span, and we want, they have the, same conversation ID, and we want to evaluate the all workflow span.
Yeah, we want to solve the problem like this.
But, yeah, in these scenarios, if we don't contain the conversation ID in workflow span, we can't do it.
We can't do it.
**Liudmila Molkova** 26:23 So maybe the next… the good next step would be to… Like, there is a scenario how you want to consume, what you want to have in the telemetry.
**Steve Rao** 26:32 Right?
**Liudmila Molkova** 26:33 It's… Yeah, it's great to know, and there is a question of how you put it in.
And this is the trickiest question.
We model conventions based on what we can collect.
Hmm. Usually, right?
**Steve Rao** 26:49 Mmm, yeah, maybe in some scenarios, yeah, this, value, provided by user side.
for example, if a user used the JNI, UTIR to instrument their, application, something like, recently we found a, case like, intelligent glasses. They, if a user, close their, glasses, and they will, create a new conversation ID.
they can pass the conversation ID to, Yeah, to the instrumentation.
**Liudmila Molkova** 27:34 Yeah, so I just want to spend a couple… at least a couple of minutes on Huxing's blog post, but I think if you can write down how… It can be stamped by other applications without breaking something else.
**Steve Rao** 27:48 Hmm.
**Liudmila Molkova** 27:49 That would be you?
A good next step.
**Steve Rao** 27:53 Okay, okay.
Thank you.
**Liudmila Molkova** 27:55 Awesome, thanks.
Okay, the blog post. As I mentioned, it all looks great, with the caveat that I love this.
project?
**Trask Stalnaker** 28:11 Oh.
**Liudmila Molkova** 28:12 But I don't know how… if it's a good idea to publish it in a blog post.
**Trask Stalnaker** 28:21 We need to get it in… Now, do you want to… Do you want to include it in the blog post, but get it into Open Telemetry, or…
**Liudmila Molkova** 28:37 Yeah. So…
**Trask Stalnaker** 28:39 What's the ideal? What's your ideal?
**Huxing Zhang** 28:42 I see so… I think we should move that project to hotel. That would be better.
**Liudmila Molkova** 28:58 Would you be interested in helping out with this?
**Trask Stalnaker** 29:04 So there's… a… Rep… slight repl… I mean, there's also the… for, let me find… There's the generalized one.
Semantic conventions, conformance… in… Oh, put it in the dock.
This one… which generalized it to be, like, HTTP… Gen AI.
**Liudmila Molkova** 29:56 Nice.
**Huxing Zhang** 30:07 Yeah, I think…
**Trask Stalnaker** 30:09 Nope.
**Huxing Zhang** 30:09 LiDope.
**Trask Stalnaker** 30:10 One thing I was… was hesitating to pull the trigger was the idea that, of… what you were doing in the Python GenAI repo of, kind of, doing the conformance testing in… the conformance testing living with the code itself?
Which… I also… I mean, I mean, has… Yeah, so anyway, there's a little bit of a conflict there that I'm not quite sure what's the best.
Wait to go forward.
**Liudmila Molkova** 30:51 Well, we need to end soon, but my thinking was that, ideally.
Since we will run confirmance tests.
in that repo. Maybe we even have a place to put conformance tests around native instrumentations, or third-party instrumentations, and then we can probably feed to this Central conformance source with the results on conformance testing.
from this rituals.
And ideally, we would have… well, probably the checks with the code are more strict.
And they are, like, CI-breaking, but this is more like, I don't know, like a coverage… Service, the test coverage, that's where you publish the results, and it shows you.
**Trask Stalnaker** 31:45 Yeah, maybe we can chat.
Somewhere about it, because that also relates a little bit to, like, CJS benchmarking.
Repo, which is sort of this… Uber, like, there are… yeah. Anyway, we do gotta go.
**Liudmila Molkova** 32:02 Yeah.
Yeah, so, sorry, Huxink, we didn't get to it properly. Let's try to identify some… something we can do, At least to get you unlocked.
Cool, I really need to drop. Thank you.
**Huxing Zhang** 32:19 Okay.
**Trask Stalnaker** 32:20 Chew.
**Huxing Zhang** 32:21 Please comment on the doc, if you want.
Okay.
**Trask Stalnaker** 32:25 Okay.
Bye.
**Steve Rao** 32:27 Right.
