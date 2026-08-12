SIG: GenAI SIG
Date: 2026-08-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:01:55 Hey folks, we'll give another minute or two for… People to join up.
In the meantime… Feel free to add your name to the attendees.
Our… and add any topics you want to the agenda.
Liudmila Molkova 00:03:08 Hi, everyone.
Trask Stalnaker 00:03:11 Hey, hey.
Pranav Sharma 00:03:13 Hello?
Josh Bonczkowski 00:03:16 Hello.
Trask Stalnaker 00:03:30 Let's see, so we don't have, Ankit yet, so let us… Why don't we bump up your… topics, Ludmila, and start with you.
Liudmila Molkova 00:03:44 Yeah, so it's been maybe even a little bit longer than a month since we released the first version of Python GenAI leaps, time flies.
And it's time to release the next one.
Before doing this, I want to check how people feel about aligning versions. They are slightly misaligned today.
And some new libraries will start are marked as 100.
And I'd like to align them, and it'll be a little bit awkward that they start at 1.1.
But overall, I kind of feel… not strongly, but it would be nice to have all libraries at the same version instead of having a wild zoo.
Unless we actually have to.
Like, probably because of major version bumps or other things like that.
So probably send a PR to align, and maybe add some checks so they don't get misaligned.
And I would like to do a release sometimes this week. Or, if somebody else wants to do the release, it's also relatively easy.
So… If anybody wants to volunteer, go for it.
Aaron Abbott 00:05:06 Yeah, I'm happy to give it a shot and see how the process is.
Liudmila Molkova 00:05:10 Oh, nice.
Thanks.
Aaron Abbott 00:05:13 Yeah, and I don't… I don't really have a strong opinion on the, the version alignment? Do you mean it's misaligned relative to each other, or relative to, like, the Python repo?
Liudmila Molkova 00:05:23 Oh, to each other. Some of them 1.1… some of them will be 1.1, and some of them will be 1.0, and I'd like all of them to be 1.1, even though The new ones never had 1.0 release.
Josh Bonczkowski 00:05:38 I kind of like having them aligned. It just makes things easier long-term.
For most use cases.
The fact that it doesn't have a 1.0 release, no one's gonna remember 6 months from now.
Liudmila Molkova 00:05:50 Yep.
Trask Stalnaker 00:05:53 I'm a big fan of aligned versions. As you know, in the Java instrumentation repo, we've got hundreds of instrumentations, all… Get the same tag.
The only difference is whether it's dash alpha or stable.
Liudmila Molkova 00:06:11 Yeah, and I feel we probably should at some point have a release We do have a release for all of them anyway, so we… it's just maybe we don't need to have a per-package version, or it should hide it somehow, so it's just hard to break.
Anyway, I think we're on the same page, then we'll… I'll send a PR to Align, I'll ping you, Aaron, and you can try the release once we're in And… Moving on to the next topic. Cool.
Trask Stalnaker 00:06:46 Yeah.
Liudmila Molkova 00:06:47 Yeah, we have a couple of attempts of giant PRs to clarify the metrics for usage.
And, it's kind of hard, and there is some alignment, needs… that needs to happen, some explanations on the histograms versus counters, it's hard. This part doesn't seem to be controversial.
We need to record individual usage attributes for modalities and phases on spans and events, right?
And it can be extracted from the giant PR.
and, apply it independently of metrics. Whatever we come up with, the counters versus histograms, this will stay in the same way.
I think that the… a couple of slightly controversial, like, things we can discuss, the worst discussion is the, like, order of… names in the pattern, so it's, like, modality, then… Input tokens, or modality than phase, or some other breakdown.
whatever. I… if somebody has a strong opinion, throw it into the PR, and no… no… no super strong opinions here, except the consistency.
The more interesting questions is video.
There is no video here.
And no document. Document is a modality that, Gemini has.
It's not that because I think we shouldn't have them. It's more that it's… the availability is very limited.
And… I wanna try and see if we downtown them, if somebody will come and notice and suggest before we actually… Ed.
And I remember, Trask, you found some research that for video, it's, like, the provider's bill on, the time, rather than tokens.
Or some other characteristics.
Trask Stalnaker 00:08:57 I don't remember.
Liudmila Molkova 00:09:00 Yeah.
Trask Stalnaker 00:09:02 But yeah, good idea. I like, that's a good idea to extract out the attributes and land those. These all look good to me, and I agree that… This feels uncontroversial.
Liudmila Molkova 00:09:19 Then, I would appreciate reviews.
That's it.
Trask Stalnaker 00:09:29 Alright, next up… Ankit.
Do you want to share, or do you want me to drag?
Ankit Singhal 00:09:39 Yeah, I think I should just share a link of another, like, small Google Doc, the second one. This is, like… so, I went through the doc, Limila, that you had put in together, so, thank you for doing that. I think that is, a lot of great information, and, I think… had some discussion as well internally, and looks like, I think, definitely, Voice agents, especially the real-time, is slightly different, in modeling, from… like, the text, agents. So I think I've got down to, at least, to start with, like, a few open, questions, So, sorry, actually, if you could open the other doc, there's one more in the link. Yeah, open questions, just under there.
Trask Stalnaker 00:10:26 Yeah.
-Oh.
Do you want to share?
Ankit Singhal 00:10:30 Oh, sure, I can… Oh, sorry, my… I don't… Okay.
So I'm just… okay, no worries.
Okay.
So, is this document the one which says open questions?
Trask Stalnaker 00:11:10 Yeah.
Ankit Singhal 00:11:11 Okay, awesome.
Okay, so I think I went through the doc, and it brings up a few very good points. One is around… Like, turn detection is not so straightforward, right?
And then, for capturing, I think… I was making one assumption, which I think is not fully valid in case of voice agencies.
Like, there's a WebSocket open, and then the user input gets streamed. It's not like you buffer it and then send it, and I think… So, that's another assumption that I was making, so, thanks for, bringing that up, Limila. Appreciate that.
And then, And then, so considering that, and then there was some suggestion about the possible span structure, the trace structure as well, and I've put them down here, and please do let me know if my understanding is correct, versus this is something, or if I missed something.
So, if I understand correctly, the trace structure that's being proposed in the doc is… capture user input, right? And if it's possible, do that.
And then for any generation from the model, would go under, say, a span called GenerateLiveContent. We can discuss on the naming, obviously.
And… Depending upon the provider, like, generate live content.
I can have child spans, for execution of tools, because I know Gemini only provides, like, one generation which has all the tool calls as well, whereas OpenAI ends the response if it has to make a tool call, right, and then user makes a tool call if it's a client-side function calling, and then another generation, like we have it in text models, right?
So, this is how the trace structure would look like, yeah.
As per that proposal, right?
And then the document also suggests, we can have, like, a turn span as well, but that's optional, or it could be just something that we kind of heuristically put in so that we can kind of make that distinction, right?
And if you do that, this is how this would look like, where you have a turnspan, same… exact same thing for first one.
And then turn to where you have user, and then the generation from the model, right? So, definitely, I think that makes sense.
So I had two major… And actually, before I go, those two questions that I also wanted to bring up. So, I looked up a few more, like, voice agent providers, like Pipcat and Elevenlabs. I think they're pretty popular as well. This is, like, open source, so you can play around with that, and 11 Labs is another one. So here.
they do kind of, model, like, conversation as a root span, and then have turns within that. And similar thing shows up in 11 Labs as well.
And Arise right now does not do that. Arise only shows the turns. They don't have, like, an Uber conversation level span.
So, I had two major questions to start with. One was… Should we group, like, these generations, as a… uber conversation span, or can we link the conversation just via conversation ID, like we do for text ones?
Liudmila Molkova 00:14:34 I think maybe, like, it's, it's a good question.
But maybe we should start from the bottom?
Like, from the… generate live content is, if we agree how it's represented on the inference.
like, the, the higher levels may be easier. I have done, like.
On the PipeCAT and 11 labs, It sounds like they… Are… not… they're either relying on the underlying leaps, like the OpenAI or Gemini to do the life, or they… Do the speech-to-text.
And then inference with text, and then text back, and text-to-speech. And then it's, like, just a regular inference, there is nothing specific, we already covered.
Great.
Ankit Singhal 00:15:34 Yeah. Yeah.
That totally agree, yes, I think that's the cascade style, they call it, and that's what they use on it, yeah.
Liudmila Molkova 00:15:42 Right, and then… Would you… the case you want to address, is it more like the casket style, or the… the end-to-end… life thing.
Ankit Singhal 00:15:56 So, I think, so, in both the cases, like, whether you go with real-time models, they have a long-running session, and they also have a conversation, right? Which is… model manages that, like, customer doesn't have to manage that.
Right, and even in voice agents, like, these providers also give you the same flexibility, right? Where you create a session and they manage the, your, like.
conversation, right?
So, that thing possibly applies to both, like, whether it's just agents or just an inference model.
Liudmila Molkova 00:16:29 I think we should have, some events, like, sessions started. Like, not the session that is conversation, the session which is WebSocket session. I hate the session. Yeah, yeah.
Ankit Singhal 00:16:41 Yeah, so I think my question was more about, like, like, for the conversation, how do we kind of pass that information if we are not… So, like, some of these providers, they create a conversation span, and then say, okay, this is your entire conversation, right? And any child span that show up is for this conversation, and different turns.
Liudmila Molkova 00:17:00 I think what they mean here is… Maybe set. But, like, maybe, again, this is the outer layer for a couple specific providers.
Maybe we should… I kind of want to start with the lower level.
With the voice, if that's what you want to address.
Ankit Singhal 00:17:21 Okay, yeah, I think then we can probably apply this question just to, inference span for, like, for GPT Real Time or Gemini Live, right?
Do we capture the conversation, and how do we capture that?
Liudmila Molkova 00:17:37 It's the part of the availability, right? So for, I think, none of the providers, I'm not sure, maybe you know better about the Gemini doesn't… have any idea about the conversation ID on those APIs?
It's like, you have a session, but this is a WebSocket session, it has nothing to do with conversation.
Ankit Singhal 00:18:00 Hmm, I see.
But Gemini Live does manage the conversation, right, like, over that WebSocket. Like, if I ask a follow-up question, it would still know the context of my previous questions, right?
Liudmila Molkova 00:18:13 Good question.
I don't know how.
Ankit Singhal 00:18:16 Yeah.
And I think so far, like, what I looked up, Gemini, like, for a short time of window, they also give you a, like, resumption.
Of the same conversation, if your connection gets disrupted. And… the conversation gets replayed, and it knows that context. So, there is definitely something happening on the Gemini side where it manages that.
Liudmila Molkova 00:18:40 Yeah, so if there is information, Google captured. I think that the key question for me, whether this life's inference is the same span as Non-life inference.
And my thoughts are that it's not, because it's based on events, it's not the operation that we kind of instrument.
It's only, like, the stream duration, like, if we… I think you asked, I didn't reply on the doc, that how does it relate to the streaming case for text? It is essentially the streaming part, not the initial request, not time to first chunk, but time after first chunk. That's what we can get… reliably get.
And it makes things slightly different, and I would like to have a different pen for it.
just because it's so synthetic, and I'm not even completely sure that we should have a spend for it. It's convenient.
But, like, it's a little bit synthetic.
Ankit Singhal 00:19:39 Yeah, I think I'm totally, on board with, like, those two cases are different, and, like, after digging some more, and after I… like, I was also chatting with Trask yesterday, just to get more idea on how, like, other Lungs with Rakuten.
things are modeled, so I think I'm totally on board, because I do see there are major differences there, and for those reasons, like, I think it definitely makes sense, no doubt about that.
So… Okay. And then, Okay, so for this question again, like, sorry, coming to the conversation, so this is something that we can just… link or identify, like we have in text models using a conversation ID or something, but I know, like, both of these providers, they don't provide you a way to get that conversation, like, if you want to, like… in case of text models, you have some API where you can say, okay, this is the previous response, and then you can build that conversation, right?
Liudmila Molkova 00:20:40 Yeah.
Ankit Singhal 00:20:41 our list conversation, they are APIs, but, like, for real-time models, I didn't see any APIs from any of the providers. It's just within that session, and once it's there, done, like, it's handled on the model side. The customer doesn't get to… Like, tinker with it, in the sense, like.
Can I get that conversation later on, once my session has ended?
Liudmila Molkova 00:21:01 It doesn't change the fact that we cannot have a conversation span, right? Because it's not the conversation, it's the session that we can scope down to a specific client.
The conversation can last across multiple sessions, however it's managed.
And it's the WebCircuit session.
That we could have a span for?
I don't know if I should, it's… Probably minutes, but it is…
Ankit Singhal 00:21:31 Oh, it can be out.
Liudmila Molkova 00:21:32 That makes sense. It could be ours, like, but for this, yeah.
Trask Stalnaker 00:21:40 That's a good point about, not… Confusing the WebSocket session With the convert… with the conversation.
Ankit Singhal 00:21:56 Go ahead. Yes.
Yeah, no, no, definitely. I think,
Trask Stalnaker 00:22:00 model.
Ankit Singhal 00:22:00 Yeah, like…
Trask Stalnaker 00:22:02 if there's… we can model the WebSocket session, possibly.
or if there's… the APIs give us something to do the conversation, But we… can't really make up something for the conversation if it's not given to us by, I think, outside of the API.
Ankit Singhal 00:22:26 So, for the WebSocket, I know, like, the proposal suggests having events, right, when the session starts and session ends.
And…
Liudmila Molkova 00:22:35 You know, this seems to be uncontroversial, at least, that it's a long-running thing.
Yeah. And if we could record that it has started?
It's useful. Its duration is somewhat interesting, Craig, because, like, if your sessions are interrupted, with an error, we would want to record it, so the metric for the session duration is useful. It feels like the… the Spanish nature, it's just that Like, if it lasts for hours, It's problematic.
Ankit Singhal 00:23:08 Yeah, yeah, no, definitely.
Trask Stalnaker 00:23:09 What did we do for GRPC? Don't… don't we… Have a span for the whole session?
Liudmila Molkova 00:23:19 Yeah, great that you asked. I've been thinking about that that's exactly the gRPC. So, I kind of have this mental model. It doesn't fit what we have in gRPC right now.
Yeah, Aaron is also checking, that maybe the baseline, if you know that something is very long, you start, like, the default experience is event-based.
Then… On top of that.
You can also have spans, but they are more like opt-in.
The gRPC case is more complicated because there is, like, domain-specific thing, there is no extra knowledge.
But I was thinking that maybe life instrumentations are better done by the calling framework, because the web sockets are so hard, but usually it's, like, the agent framework that calls them.
And it can get extra meaning. And, for example, ADK knows whether you start, like, the translation, which is completely asynchronous, there is no turns, there is no back and forth, it's just completely stream in and stream out with no boundaries.
Then it knows that you use this kind of a model, and then you just don't create spans for it.
And then when you know the use case is more, like, shorter, then you add spends.
Trask Stalnaker 00:24:44 I see, so the translation is just a client layer on top of the same real-time voice, where it just streams it all in one direction and streams it all back in one… response. Yeah.
Liudmila Molkova 00:25:00 Yeah.
Ankit Singhal 00:25:06 So, we definitely know, like, these sessions can go an hour long. I know OpenAI does that.
It says, like, 60 minutes is your, like, the time window, which is pretty long for a span to be open.
And opening it, right? So… would it be safe to say we can start with, like, events or sessions? Because these are pretty long, right? And then spans, I think, we can come back and see if it's really needed.
Okay, sounds good.
Okay. And then for the conversation, Should we just link it via, like, conversation ID on the span, so that we know this is what this…
Trask Stalnaker 00:25:48 I think the question is, do we have a conversation ID?
Ankit Singhal 00:25:51 Yeah, so I think for GPT real-time, yes, it does provide a conversation ID, but there are no APIs later on for you to fetch that conversation.
It's just within that session after that, that's… yeah, okay.
Liudmila Molkova 00:26:07 And then we would stamp the attribute when we have it.
But there is no means we can do anything. We don't know when the conversation started, really. Where we don't, we cannot record the conversation as a Spanish.
Trask Stalnaker 00:26:25 And we don't gen… like, in the, text inference, we don't capture a span for conversation either, we just stamp the attribute.
Ankit Singhal 00:26:40 Okay, that's awesome. Yeah, and then my second question was, Like, for example, in this trace, right?
It's very… not so straightforward for me to tell that all these things happen because of, like, a user input, right?
Or it could be multiple tool calls as well, if that happens, right?
So, for those reasons, like, just to make these traceable, like, more readable, rather than, like, putting that onus on customer to figure those out.
Having that logical grouping of turns, does that make sense? And… And I think that doc clearly states how, like, it's not always possible for all the providers, and there's some places we have to just play with heuristics on, okay, this is where we think it would have started, right? And that might not be entirely accurate, but at least it gives you… puts you in that ballpark area, and gives you at least a more… Workable view of those traces, right?
Liudmila Molkova 00:27:38 Yeah, I… Like, I… I tried… inferring turns bad, and it sounds like it's possible, but I always end up in some weird case, and it's super synthetic. Like, super synthetic, like.
The live content is based on two start and end events, but this guy is, like, completely, you choose what constitutes a start and, what constitutes an end.
I… I'm not opposed to saying, okay, if you can't detect it, do it.
But more like, are there actual cases where we will implement it?
In instrumentations. And if you want to try, and like, I think the good next step would be like, once… I still want to get, like, finish the live content, and then after, like, we land this, maybe, to have a prototype for the turn, like, more, like, like the one I'd like to play, and I found that, like, when I talked to Edge and interrupted it.
create some random turns. So, like, if we can end up with some somewhat reasonable, detection, and we can document its best effort, I would not be opposed to it at all.
Trask Stalnaker 00:28:56 So sort of the having two layers, I think, is what you're describing, Ludmila. One is kind of this low-level… Close to the protocol, layer, event-based.
And sort of, that's what we know we can instrument And then… If there is an abstraction layer on top of that, like.
Translation, or some other use case.
Then we could… you could build in… grouping spans.
Liudmila Molkova 00:29:33 Oh, more, more like… for the translation case, we would not create any of it, because this can last for hours, even the lifespan. We would create events, but maybe we can special case the translation and say.
I don't know, don't.
Yet. And then for the models where it's, like, conversational model, then we would, create the live content spend from… from the… the protocol-level events.
And the turn, it's not even the abstraction that exists in the SDK. It's just us inferring from different events in the stream some higher level grouping. Okay, user spoke, moderator replied.
It's totally best effort. We don't know the sexual boundary.
Trask Stalnaker 00:30:28 That makes me nervous.
Liudmila Molkova 00:30:29 Hmm.
Trask Stalnaker 00:30:30 I mean, like, I'd rather, like, just have a… Clear answer to, like, that we just instrument, like.
I don't know. I guess we'd have to see how that worked out, but that feels like something that… higher level, API, if it knew, or your application knew, you could create your own, sort of.
turn spans…
Liudmila Molkova 00:31:05 Yeah, so they give the… the framework on top wants to add this. It can add it.
It can be framework-specific. In practice, it might mean that they would Added based on events.
Anyway, because that's the best that they have.
Ankit Singhal 00:31:27 Yeah.
Trask Stalnaker 00:31:30 I guess it would be an opt-in, I mean, in the low-level instrumentation, as long as it was, like, an opt-in, like, a best-effort thing is opt-in.
Seems… Reasonable.
Ankit Singhal 00:31:49 Awesome. Actually, this is great discussion. And, okay, so it's possible we'll do some, like, groundwork on how well we can detect turns, at least with two of the known Like, hey, here, this one.
Aaron Abbott 00:32:10 Sorry, did you… did you say Mi Ankit?
Ankit Singhal 00:32:13 Yeah, I'm seeing your hand up.
Aaron Abbott 00:32:15 Yeah, I didn't mean to interrupt, I have a separate question from what you're saying.
Ankit Singhal 00:32:20 Oh, I see. Okay, so I think for now, let's… so, like.
It's fair to say we can make a decision on, like, this being an opt-in.
And then providers can decide on making that,
Trask Stalnaker 00:32:36 Yeah, we still have to give… okay, we still have to figure out if we can give reasonable guidance on what best effort means.
Ankit Singhal 00:32:43 Yes, yes.
Trask Stalnaker 00:32:44 But if you come up with something that seems compelling, best effort, that we can define sort of semi-concretely, then it could potentially be an opt-in feature.
Ankit Singhal 00:33:03 Yeah.
Aaron Abbott 00:33:04 Yeah, I was gonna ask, so if we don't have a parent spin.
and say we don't even do, like, the conversation detection, I think we still need spans for, like, tool calls and such, right? Because those have a fixed amount of time, so… I was gonna ask, do we have semantic conventions for WebSocket already? And I guess there's some intersection with HTTP, so… yeah.
So once the HTTP, like, initialization handshake happens, I assume there would be, like, a closed HTTP spin?
And maybe we could use that as the parent? I don't know, just throwing things out there.
Trask Stalnaker 00:33:39 Our HTTP instrumentation is very much request-response-based, not WebSocket-based.
I think the closest we have today is the GRPC streaming… Which… Is… has its own issues.
Aaron Abbott 00:34:00 Okay. I think it might be worth trying out in Python to see, depending which, like, just to see what happens with the actual instrumentation we have.
I think it might give you at least, a really short spin, and then look like a SSC kind of case where the spin ends after the initial response, and then… I guess it upgrades to, like, a TCP kind of connection after that for WebSockets.
Liudmila Molkova 00:34:29 Yeah, I… I can try the… the Google GenAI and see if I can leverage it. There… if there is a gRPC span, that would be the nature of convers… like, the session, where the… There is anything from HTTP we can leverage, but I would imagine it's… it happens on there. We have no access to it from the… Google GenAI, where OpenAI real-time API service.
Aaron Abbott 00:35:03 Okay, well, sounds good.
Ankit Singhal 00:35:07 And one more question. So, I was also… like, once I was thinking about this, one thing that comes to my mind about the grouping as well, when it comes to, say, voice agents.
I know it probably might not be… discussing everything about voice agents, but just from the uber, trade structure point of view.
So, like, in, text models, we have this invoke agent span, which kind of shows you that unit of agent invocation, right?
I was trying to see if that makes sense as well for the voice agents, where this is… I just gave it the name Agent Life Generation, but this is that agent spend once the user inputs is committed.
And then it uses real-time models under the hood, and… This becomes, like, similar to… In a way, somewhat similar to, text agents, where… An agent uses a live model, like GPTL time or Geminer Live, and then… Gives you a response back.
Liudmila Molkova 00:36:12 what I've seen in ADK, and maybe it's also the case for OpenAI agents, let me know, new colleague Agent Run.
It actually corresponds to a session, the WebSocket session, and it would recreate sessions underneath.
But it includes multiple…
Ankit Singhal 00:36:34 But for every run, it'll create a session.
Liudmila Molkova 00:36:37 Yes, when you call run, it'll create a session, not conversation, web circuit session.
Ankit Singhal 00:36:42 Yeah, yeah.
Liudmila Molkova 00:36:42 Then it will keep it open, probably, retry, reconnect, whatever.
Ankit Singhal 00:36:48 Hmm, I see.
Liudmila Molkova 00:36:48 But then… It's… Essentially, it's multiple runs or turns.
So, like, in the text case, or, like, the traditional, the, like, OpenAI Responses or Gemini Interactions API, It's like… you give a set of inputs, right? The chat history, and it gives you an output, or multiple outputs.
And it's a… this is one run, or one turn, and in this case, at least an ADK when you call run on live agent, it's multiple runs or turns within it. You keep talking to it, and it keeps coming back. So I think it's wrong to model it as an invoke agent.
But it's okay to model it in some other way.
Ankit Singhal 00:37:36 Oh, yeah, yeah, so actually, who's not… suggesting using an invoke agent, but I was just suggesting from the trace structure point of view, like, here we are using, like, say, for example, GenerateLive Content, which is a new span, or probably will be a new span, or something similar, right? So, something similar for agent invocation, because we know it's not exactly… Because here, also, it's gonna have the same differences as you would have for a real-time model, right?
Liudmila Molkova 00:38:04 I just… I don't think that, at least in ADK, you can create this span. This is the same problem as turn span. This is the turn span, which we have no… no known boundaries for.
Ankit Singhal 00:38:14 Oh, I see.
Okay.
Trask Stalnaker 00:38:19 I'm gonna cop time on this here.
So that we can get to the next couple of topics.
But thank you, that was really great. Discussion.
Ankit Singhal 00:38:36 Thank you. Thanks, Trask. Thanks for the, yeah, and thanks, Lilmila, and, for the discussion, appreciate it.
Trask Stalnaker 00:38:44 Yeah, if you can stop sharing, then I can take back control. Thanks.
Pranav… You've got the next topic.
Pranav Sharma 00:38:57 Hey, hi. Yeah, I just wanted to, share this, document, like, Open Inference, donated some of their instrumentation, to the OpenTelemetry project, and, I was just trying… thinking of starting the work on.
the JSTS instrumentations, porting them over to the contrib repo there, and I just wanted to, ask the community here, like, if there are any concerns or objections about this. I'm going to present this to the JS SIG tomorrow as well, but just wanted to let people know that I'm planning to work on it, and if there's anything I should be concerned about.
Or take care of, special care of, while doing this work.
Trask Stalnaker 00:39:43 Awesome.
Liudmila Molkova 00:39:47 Yeah, it is. Unfortunately, we don't have Jamie here today. Don't think we have anyone from JavaScript saved.
Correct me.
It sounds awesome, and thanks for doing this.
Pranav Sharma 00:40:00 Alright, sounds good.
Trask Stalnaker 00:40:02 Yeah, if you've seen the, you've seen the Python-ish tracking issue? Yes, so something, like, similar like that in JS.
Pranav Sharma 00:40:12 I think I mentioned that in the, later down in the doc, that we need to create that issue. Yeah, Broad said the very first one.
Trask Stalnaker 00:40:21 Yeah, I see. Yes.
Alright, sounds like you're on it.
Pranav Sharma 00:40:26 Alright. Thanks, Vogue.
Liudmila Molkova 00:40:27 And I also think it's part of your dog that Pretty much the only way we can make it repeatable, scalable, is to have a lot of core things, like the GenAIOTs we have in Python.
And this helps tremendously.
without it, I don't know how we can… we could… Review all the instrumentations.
And another part is the confirmance testing, that we can validate the telemetry… we produce against semantic conventions. It helped find a lot of issues in Python instrumentations.
And it would be useful to have it from the get-go, so, like, whenever we port and instrumentation, we also generate the conformance tests, and it gives us, like.
More than 50% of, confidence that we actually follow semantic conventions there.
Right?
Pranav Sharma 00:41:28 That sounds good. So, when I port over the first one, I'll make sure that we have the conformance tests along with it.
Thanks, Ludmila. Yeah.
Liudmila Molkova 00:41:38 Damn.
Pranav Sharma 00:41:39 Thank you.
Aaron Abbott 00:41:41 I was just gonna ask, is anybody interested? Oh, I see, Surya, you just… just when I said that, you said something in the chat. Yeah, I was gonna ask if anybody's interested, besides Pranavan working on the JS instrumentations.
Yeah, go ahead.
Surya Teja 00:41:54 Yeah, I was actually working on OpenAI agents and, Anthropic.
The question that I had was, how are we pulling the semantic conventions in JS? Because I saw that in 1.42, we deprecated as we moved to a new repository, and there was a… Open issue from… honeycomb folks to create something for JavaScript ecosystem.
Aaron Abbott 00:42:27 I think that maybe would be a question for Jamie.
Surya Teja 00:42:32 Yeah, no, thanks, thanks.
Liudmila Molkova 00:42:35 I think that there, if I remember correctly.
The conclusion Jamie and Volvgen came to is that we want to generate a separate artifact for semantic conventions in JS, but maybe it should be part of the Sutil package, at least in Python.
I would generate them directly into GenAI 2.
Surya Teja 00:42:57 Okay. Yeah, Ludmila, if you are free sometime, I would like to pair up with you and see how I can generate them both in Java and in JavaScript.
Liudmila Molkova 00:43:08 In Java, it's better to talk to Trask about it.
Surya Teja 00:43:11 Yup.
Liudmila Molkova 00:43:11 In JavaScript, Yeah, I… okay, so we had an internal discussion between Pranav and Arrow, and I was going to write, like, a one-pager on the call generation. Maybe I just do it in public, and I created the one in public space, and share it with you, Surya and everybody else who's interested.
Surya Teja 00:43:32 Yeah, that sounds awesome, actually.
Liudmila Molkova 00:43:35 Sounds good.
Trask, do you have thoughts on the Java GenAI conventions?
Trask Stalnaker 00:43:44 We're… Oh, didn't… wasn't that from you, Surya?
We've got GenAI… we've got, sort of, the GenAI semantic conventions in our instrumentation API package, and there's some…
Surya Teja 00:44:03 Yes, that was from me. Yeah, we have a copy, but… Yeah.
Yeah, the second one.
Trask Stalnaker 00:44:13 Yeah.
But it doesn't today match… yeah, it doesn't today match the, kind of, the Python GenAI utils. And I know we actually had a request from the Alibaba folks to have, kind of, this consistent GenAI Utils, or have something like that in Java, also?
So… I'm open.
Interested to see what your, would be happy to follow along with other languages.
Surya Teja 00:44:49 I was actually gunning for going to… in that direction, but I just wanted to get this sorted out before I put that in place.
In Java.
Trask Stalnaker 00:45:03 I think there's… Probably worth commenting also on this.
Issue.
Or cross-referencing it.
Because that's basically what I told the Alibaba folks, was for Java, that, I wanted to see, like, a cross-language consensus. Since we have our own, sort of, instrumentation API already, even though it's not as convenient and has got some, I don't want to create yet another abstraction, unless there's, like, a cross-language effort, and then we can say, oh, okay, we're aligning with that.
Surya Teja 00:45:55 Yeah, that sounds good, Trask. I'll drop something over there and see.
Trask Stalnaker 00:46:02 All right, Nikhil, do you want to share?
Nikhil, you there?
Nikhil Chitlur Navakiran 00:46:16 You… Yes.
I can share, let me…
Trask Stalnaker 00:46:23 Oh, okay.
Nikhil Chitlur Navakiran 00:46:24 I've linked it, if it is easier.
Trask Stalnaker 00:46:28 Whatever you prefer.
Nikhil Chitlur Navakiran 00:46:31 Okay, just please, please pull it up, that's fine.
Trask Stalnaker 00:46:34 Yeah, sure.
Nikhil Chitlur Navakiran 00:46:40 So, I think a couple of weeks ago, we spoke about, how we could unify Multi-agent tracing across, different, You know, like, the different approaches used in… Used by, like, the… used by different platforms today, right? So, I went ahead and, I did some research on that, and… I can present the executive summary, and… and then we can go down. So, most… So the two types… Essentially is, there is an… tool-based handoffs or delegations happen when the control is transferred from the parent or agent A to Agent B.
And, some of those are, like, agent-directed, right? So, like, you get, like, NLM, Saying that, hey, you need to call Agent B. So… so that, is recorded, and then… so some of those can be recorded as tools, so, like, a few platforms, including, Google and, And, Amazon, record them as, tool calls.
And there are some other platforms where they… they are just recorded as, non-hotel spans. So, for example, OpenAI, records one such interaction as a span.
So the… the proposal is… So to… So when it is modeled… when the hand… when the transfer of control is modeled as a tool, then we continue using execute tool, and when the transferred is modeled as an, as an agent-to-agent.
Agent-to-agent transfer, then, let's reuse the invoke agent span, rather than introducing a new span to capture that, that transfer.
So, in, the tool-mediated handoff, there is, like, the caller execution happens, and then, yeah, that line specifically, then there's an execute tool, and then there is a target execution. So, essentially, there's, like, a invoke agent at the caller.
Then there's an execute tool, which records, which says that, hey, there is a… the… the, you know, the control is going to be transferred to a different agent, and then on the target agent, you always… you additionally get an invoke agent as well.
In the non-tool handoffs, so you have a… you have the caller, like, the initial agent, so, like, the agent exec… you'll have an invoke agent at the agent… at the caller agent, then another invoke agent, which denotes the, transfer.
So this will be a caller-owned Invoke Agent span that… That I'm proposing to record, and then the target agent also has an invoke agent.
That it… that it records.
So, the, the caller-owned invocation section, so that is where we… to ensure that there, like, the invoke agents Are not repeated, so there are specific properties that we can Add or look for to, make sure that it is this invoke agent technically is more like a client, and it is… it is meant to denote a transfer, right? So, there's additional terminology and stuff that you can go through, and I've also documented the current approaches.
But yeah, I would like to go to the recommended trace shapes, so it might be easier to understand.
So, the first two examples are of, tool-mediated handoffs. So, the first share is, okay, there's an invoke agent orchestrator. The orchestrator agent is the caller in this situation. So, the… So there's some interaction, and it, decides to, you know, it decides to, transfer to.
agent, the research specialist agent, right? So here, I am, I'm calling out, delegation versus handoff, right, as two, as, two distinct types.
So, delegation, I'm, defining it as, like, it is… the… the control, or the… yeah, the control comes back to the orchestrator agent at some point, like, after the… after the research agent has been, has run. But in a handoff, we don't expect that the, like, the… Like, the control goes back to the parent agent, during that handoff.
Right, so… Today, like, Google and, ADK and the Bedrock, instrumentation, as execute, records, these transfers using executeTool.
And they, what I'm posing is to make it more of an, hotel standard.
And, where we also add certain properties, like agent name and agent interaction type, to, on the executeTool span to, make sure that we are You know, this sort of, Transfers are cap- are captured.
Ludmila, you have a question?
Liudmila Molkova 00:53:11 Yeah, I'm thinking… What you're suggesting is that we have a special type of the toll call span, right, that records, To executing Agent as a tool.
Right.
And it becomes special by either The name, the operation name, or the attributes that are there.
the… Assuming we just record that it is the invoking another agent.
Would we need Like, the interaction type.
Do we need to qualify it? Because… If I say, okay, it's a transfer.
do Agent, or Agent as a tool execution.
And then there is a name of the current agent.
And the agent to be invoked.
Then it kind of implies certain… Hi, Poss.
delegation.
Sorry, I'm nitpicking, I, I, I'm with you. Yeah, conceptually, I agree, there are some details we probably should polish.
For the sake of time, I think.
Nikhil Chitlur Navakiran 00:54:29 Yeah, yeah.
Yeah, absolutely open to, like, all the feedback. So just to understand better, so, are you… so… so the reason why the delegation type, or the interaction type came in.
Was… there is this certain notion that an execute… whenever an execute tool happens, that you… It's a tool call, right, technically, so that the control comes back to the the main agent.
So… with… with that… so, but with the handoff scenario, like, it is just fire and forget sort of a thing, so that never happens. So in order to capture that distinction, it was introduced, so that that is… Like, from users of ExecuteTool who maybe expect that the control, comes back are not I'm not surprised by it.
Liudmila Molkova 00:55:41 I see, so for the same… for the two calls.
And still with two different ways. The first way is that the outer agent is blocked until the inner agent does the thing. In another case, we unblock immediately, and then the other agent continues independently, right?
Nikhil Chitlur Navakiran 00:56:04 Yes, so in the handoff scenario specifically, the… it's the… it would become the responsibility of the target agent to… to respond back to the user.
That's… That's the idea.
Liudmila Molkova 00:56:20 Jay, thank you.
Nikhil Chitlur Navakiran 00:56:23 Hey, Aaron, you have your hand up.
Aaron Abbott 00:56:25 Hey, hey, yeah. So I, I was wondering if… So, like, executeTool is kind of specific. I feel like pretty much all inference providers support tools, and they mean the same thing at this point.
So I… I'm wondering if… this is capturing the fact that, like, the LLM is actually… like, the sub-agent is put into the available tools when you do the inference call. And if not, I'm just a little worried, because I think it's pretty unambiguous right now. Like, the execute tool is a decision by the LLM from the thing that the LLMs recognize as tools.
Is that… is that kind of the case here? Are we overloading?
the spin.
Nikhil Chitlur Navakiran 00:57:07 So, I think the definition is still the same, where we say that a tool is registered with the LLM and then it is invoked. That's… that's still the case, but… But the registered tool itself can, invoke an agent.
Aaron Abbott 00:57:29 Yeah, right. So, so I mean… Yeah, like, what I would imagine is most times the agent framework would give a tool, like, start subagent, and then it would have, like, subagent name.
and in the description, it would list the sub-agents, yeah.
Which is a little bit different, because, sorry, go ahead.
Nikhil Chitlur Navakiran 00:57:50 Yeah, no, that's essentially what we're trying to capture, as well. So, like, the… today, the execute tool, like, when you say, hey, go, like, you know, start the sub-agent or whatever, right? Like, the execute tool doesn't have… The, attributes to denote what, sub-agent is being, started, or, you know, anything, like, what context is being passed, maybe we could… I think what I'm proposing we use… we reuse the call arguments, but Yeah, it doesn't have anyth- any… attributes related to the sub-agent that is being captured on ExecuteTool.
Awesome.
Trask Stalnaker 00:58:39 We are almost out of time, Anything else we can cover in a minute?
Nikhil Chitlur Navakiran 00:58:50 Yeah, so the, mostly, yeah, just please have a look at the in-process, non, non-tool delegation as well, so that is mostly, if you scroll down, so there is, like.
How this… how this interaction is supposed to happen.
And maybe I can, talk about it in the next, in the next meeting. It's primarily… So there are, like, platforms out there that are, using custom spans, like OpenAI is using a handoff span, and even, even Langchain uses, like, some sort of a chain span to.
denote, non-tool, non-tool transfers of agent. So, this, I'm proposing that we can all circle that, or tie that back into Invoke Agent, so that's what this section would cover. But yeah, happy to present. I also have a initial PR on it, if, Folks were, folks can take a look.
Liudmila Molkova 00:59:54 Nice. Do you have reference instrumentation, too?
Like the…
Nikhil Chitlur Navakiran 01:00:00 Yes, and…
Liudmila Molkova 01:00:05 It's usually… we're out of time, but usually the problem is that it's not the telemetry we want to collect, it's what we can.
And, I would be first looking probably into the… the instrumentation, the reference instrumentations to see how and what we can, learn about.
Nikhil Chitlur Navakiran 01:00:28 Perfect. Is that… So, I have the scenario section, so would… is that the reference implementation? Okay.
Liudmila Molkova 01:00:36 Yeah, that's the one, thank you.
Nikhil Chitlur Navakiran 01:00:38 Yeah, so yeah, so I added some, like, on how it can be captured. So mostly, like, it's… yeah, so we can, we can have a discussion on that.
Liudmila Molkova 01:00:49 Thanks.
Trask Stalnaker 01:00:50 Sorry, we're out of time, but yeah, let's, thanks for getting the PR up, and, yeah, let's discuss on the PR, if we can.
Thanks, everyone.
Nikhil Chitlur Navakiran 01:01:03 That'd be great.
Liudmila Molkova 01:01:04 Thank you.
Nikhil Chitlur Navakiran 01:01:05 Thanks, folks.
Trask Stalnaker 01:01:06 I…
