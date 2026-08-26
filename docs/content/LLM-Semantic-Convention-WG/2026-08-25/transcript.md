SIG: LLM Semantic Convention WG
Date: 2026-08-25
Duration: 8 minutes
============================================================

## Zoom Recording Transcript

**neil yashinsky** 02:31 Good afternoon. It's Annie, right? How's it going?
**Anirudha Jadhav** 02:37 Hello, hey, how are you?
**neil yashinsky** 02:39 Good. I feel like we've chatted just once or twice. I could be wrong. Yeah.
**Anirudha Jadhav** 02:43 Yes, yes, yes.
**neil yashinsky** 02:45 Okay, good.
**Anirudha Jadhav** 02:45 Yeah, early on in some of the meetings, and then afterwards, I had to drop for a couple of months, and now back again.
**neil yashinsky** 02:52 Oh, same B.
**Anirudha Jadhav** 02:53 We do a lot of work. We do a lot of work in between and did a lot of releases, but we never got to talk about it, so I was just, like, waiting and thinking how things are going.
**neil yashinsky** 03:02 You know, I personally, my own kind of personal release philosophy is, I guess you could say kind of akin to, agile. So, sometimes things slip, sometimes things shift. But.
**Anirudha Jadhav** 03:17 I don't know how many people join this regularly now or what's going on, so I was just trying to wait and watch and see. Yeah, yeah. I can share some links.
They've been kind of open sourcing all of these updates.
And we also open-source a GenAI normalizer in the OpenTelemetry community to sort of get through some of the changes in the upstream core, too. But yeah, I'm sharing some links here. Yeah.
All the eval workflows are also generalized.
And all of these things moved into hotels, Trans started supporting them.
Did a lot of work.
**neil yashinsky** 03:56 Hmm.
Interesting.
And scoring, too. Look at that. And benchmarking. Wow. There's, some very interesting, what I like to call evolutionary convergence.
with, what I've been working on with you, and what you've been working on, it seems like, and that's exciting for me, because, I knew…
**Anirudha Jadhav** 04:21 This is the final link. This is where all the ingestion pieces of the GenAI Semantics got normalized and went upstream to OTEL.
So now we can effectively move, like, Telemetry from… various platforms.
into the Gen AI Semantics.
**neil yashinsky** 04:42 laughs Wow, this is, terrific, yeah, and, in some ways, even more overlapping, I think, with an entirely different, perspective, if I'm seeing it right, because I'm just looking at it, for the first time, so forgive me, I don't want to draw any, I don't want to draw any premature assumptions. Do you mind, saying, like, walking me a little bit through how this works?
**Anirudha Jadhav** 05:05 So effectively, the problem was we had many other platforms, LLMetry, Open Inference.
having different semantics.
This normalizes everything into OTel GenAI semantics and it also covers evals. Evals and traces are both combined and now both can be done via normalization processors and evals can also have direct auto instrumentation evals from popular frameworks.
Or manual instrumentation evals.
**neil yashinsky** 05:39 Interesting. And what is the… what are the instrumentation evals, like.
Eval, I guess?
**Anirudha Jadhav** 05:45 So you use, effectively frameworks like Strands Eval, or PyTest, LangML Flow, any eval platform you use, now you can start just instrumenting them and moving them to OpenSearch. And the GenAI normalizer can move them to anywhere.
**neil yashinsky** 06:01 Interesting. Yeah. Yeah. That's very cool.
That's very cool.
Yeah, so, it's kind of like, two sides of the same coin.
Which is great, and it's why, like, this is, like, in some ways perfect, like, if we were doing the exact same thing, it would be worse, I guess, if I'm being honest. I'd be like, ugh, you know? But I think we're actually, from what I can tell, this is, like, basically, for lack of a better word, like, server-side instrumentation, yeah? And, like, providing details around, like, within… The operating LLMs themselves?
**Anirudha Jadhav** 06:36 Yep.
**neil yashinsky** 06:37 Yeah? Yeah. Yep. And so, basically, what I've been doing is building, if you will, the client side of that, and, like, for a business that has all these agents that are doing all these things, like, how do you keep track of them?
you know, and the applications that they themselves are building, rather than what I'm seeing this as, is like.
Them building the applica… like, this is their internal mechanics that you're instrumenting.
**Anirudha Jadhav** 07:03 Yeah. Yeah.
I might need to drop over here, honestly. Sure. I was, I can, like, most of these issues are closed.
But part of the OpenSearch, AI observability or eval frameworks, we are continuing to add more support for GenAI Semantics in OTEL, empowering them all over.
Hotel Gen AI Semantics. like, I can join… I'll be joining next few meetings, if we have more attendance over there, we can talk, or…
**neil yashinsky** 07:36 Yeah.
**Anirudha Jadhav** 07:37 Talked with… Just GitHub issues, and we'll continue to move forward.
**neil yashinsky** 07:41 Yeah, that sounds great. I've seen, like, a couple of the other ones that I've been at lately have been sparsely attended, and I think it's just, like, the summer, you know.
What's happening, yeah. Yeah, so one last thing, if you're okay, do you mind sharing your email address with me? And I'll just, like, offline, I'll send you a few details of, like, the great thing is, like I said, is, like, non-over… I mean, I'm sure there's obviously.
**Anirudha Jadhav** 08:04 I shared on Slack.
**neil yashinsky** 08:05 Yeah. Oh, okay, great. And, yeah, I mean… I will… oh, that's right, I could have found you on, on Slack as well. I didn't even think about that, I forgot. Is that what you were saying? Or do you mean the meeting?
**Anirudha Jadhav** 08:19 I put it in the Zoom meeting, but Slack is also okay, both are okay.
**neil yashinsky** 08:23 Oh, perfect. Okay, great, great. Well, I'll let you go, give you some, great catching up with you. Congrats, this looks really, really exciting stuff. I'm eager to follow along at home, and I'll talk to you soon.
**Anirudha Jadhav** 08:33 Take care, take care, bye.
**neil yashinsky** 08:34 Take care, bye.
