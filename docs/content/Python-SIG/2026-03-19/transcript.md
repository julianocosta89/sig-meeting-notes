SIG: Python SIG
Date: 2026-03-19
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:04:30 Hello, everyone.
jayesh 00:04:39 Blue.
Erdenesaikhan Tserendavga 00:04:43 Hello, everyone.
jayesh 00:04:57 Good evening, everyone.
Aaron Abbott 00:05:26 bleh.
Riccardo Magliocchetti 00:06:26 Welcome, everyone, to this week.
Python security… In the meantime, we wait a few more minutes for more people to join. Please add yourself as an attendee.
to the notes. And also feel free to add any topic you want to discuss.
Benjamin Kawecki 00:07:09 Hello, I've got a topic I want to discuss, if that's okay?
Riccardo Magliocchetti 00:07:15 Cool. Please add it to the… Notes?
Benjamin Kawecki 00:07:19 Sure.
Riccardo Magliocchetti 00:07:35 I think we can start.
The touchboard.
Anyone?
Wants to triage.
What? And do it then?
Aaron Abbott 00:08:00 I don't know if… Tammy Baylis 00:08:01 Sorry, I, I'm not quite back up to speed yet, so, yeah, if you could drive today, Ricardo, I appreciate it, thank you.
Riccardo Magliocchetti 00:08:10 True.
Okay, so we have, I think, a bunch of… Dependable?
PRs?
Yeah?
Like, usually we don't merge them, but… We can take a look.
Nothing important, I guess?
And then… We have this one… Okay.
I should probably take a look at it as well. This is for implementing more SDK metrics.
Or monologue?
So, I guess this is ready for review.
Yeah, if one is interested, like, Anorag is working around being, all the SDK metrics, what are the semantic conversion.
lechen 00:09:13 Yeah, I'm taking a look at that right now.
Riccardo Magliocchetti 00:09:15 Thanks.
And Ben, we have… Instructor from Josh.
Oh, it's expanding.
And I think this is, like, the same… as the longing Andrew, we have for the standard link, but for struct log.
lechen 00:09:50 Hey, did we wind up moving the logging handler into the instrumentation, or no?
Riccardo Magliocchetti 00:09:56 you know, we have a copy inside the instrumentation logging, and the one in the SDK is deprecated.
lechen 00:10:04 Oh, nice, nice.
Riccardo Magliocchetti 00:10:09 I think this is… ID4 renewal, as well.
What?
Josh, if you are here… Please fix, sophie, yeah.
Josh Winerman 00:10:27 Sorry, will do, Ricardo. Been sort of out of touch with this one for a second.
Riccardo Magliocchetti 00:10:33 Not a problem.
Some Gen AI stuff… Okay, opener espos extractas… Okay, so… We'll move this as well to the default review.
And then… Again, dependable stuff, automated stuff… And these are more interesting. Okay, you ever seen this one?
This is a fix for a default we have, in the… I think it's, yeah, it's much longer to process our default, schedule delay.
It has already been approved by Pablo.
So… Yeah, if anyone wants to take a second look.
And I do as well. But by the way, while you're here, we started to get some automated reviews from this thing, I think it's a bot, the Mavic.
I'm not sure they're helpful, but… Yeah, just… For your information.
When we have another… OpenAI, I think… no, this is for Anthropic. Yeah, just, by the way, like.
GenA people doing PRs, please add the… also, like, everyone doing a PR for a specific instrumentation would be helpful if you… say for which instrumentation it is the PR.
Because this one is quite genetic.
But, yeah, again… Okay, this is unrelated, so I think this is ready for review as well.
With… Where it is, so this one?
Okay, okay, so the Mavic wasn't about, maybe? Or maybe it is?
I don't know.
But, yeah, this is me missing, silly signs, so… We have to wait before taking a look, I guess.
Slow.
Swing fixes.
Yeah.
I think I merged a bunch of approved TRs early this week.
I probably need to… to go… To take another look at.
What we have left here.
Anyone want to discuss something specific?
Between the board.
Okay.
By now, 5… 5 minutes timebox, is gone.
And so let's move on to the next topic.
I read here with Mike.
We'll be around in 5 minutes, so maybe we can skip, His topics, while he joins.
And when the first one is from Arum.
KubeCon? You're coming to Amsterdam?
Aaron Abbott 00:14:18 Yeah, yeah, I actually am. I will be there, so, I wanted to ask if anybody's going, Yeah. Are you gonna be there, Ricardo?
Riccardo Magliocchetti 00:14:29 Nope.
Bye.
Aaron Abbott 00:14:35 Yeah, so, you know, you don't have to stay here, but I just wanted to, I guess, let people know I'll be there. There's nothing, like, planned for… Python?
if there's a lot of people coming, I guess we could try to plan, like, an office hours or something like that. We do have office hours for GenAI, semantic convention SIG.
I'm gonna copy what Lyubmila said.
I think we… we have the time, it's in Slack, but, you know, if folks are around, and You wanna talk about… LLM stuff.
There's gonna be office hours for that, so… Yeah, and then the only other thing was, like, I guess if folks aren't going, then the SIG next week, you know, please do it without me.
Liudmila Molkova 00:15:30 And it was… Oh, sorry.
Riccardo Magliocchetti 00:15:33 That op is great.
Liudmila Molkova 00:15:35 There was quite a few folks at last KubeCon from Splunk. Sergei, do you know if anybody's coming?
Sergey Sergeev 00:15:46 Yeah, I'll double-check. We have a broader open telemetic group, which may come Not anybody from the US, because of the… Siskaspoenk, policy right now, on travel.
Liudmila Molkova 00:16:04 Oh, okay.
Thanks.
Aaron Abbott 00:16:08 Yup.
Okay. Well, I hope to see some of you there, I guess just mostly an FYI then.
Riccardo Magliocchetti 00:16:20 Thanks, and enjoy your cubicle.
Okay, next topic… from… Syria?
I think this may be, yeah, the very same PRs that I showed before.
Yep.
Surya Teja 00:16:42 Yeah, I just posted this just to get some reviews, because I am doing some stuff to normalize things by using Pydantic, and extractors, so that's it, nothing more. I guess this can be skipped because we discussed it, but if people want to take a look, they can take a look and let me know their feedback.
Riccardo Magliocchetti 00:17:10 Alright, thanks.
Okay, my next topic is from Xuning.
Shuning Chen 00:17:36 Yeah, this is about a comment, for my, PR that Lyudmila previously left, so… She suggested removing the, star stop And fail type.
methods, I tried to remove them all, but then I found that the current, launching, Anthropic, and, instrumentation packages already have these methods applied, so if I remove them, it will cause the braking changes.
And, Similarly, for embedding, I, followed the same pattern, creating the start embedding, stop embedding, fail embedding methods.
So, after some, internal discussion, we still prefer to, keep these methods. For now, if we want to remove them all later, we can create a separate ticket.
What do you think?
Liudmila Molkova 00:18:42 Thanks, I understand that removing stop LLM and fail LLM is problematic, yeah, sorry, but I don't think we should introduce new methods like this. They don't seem to be helpful.
Shuning Chen 00:19:00 Yeah, I, so before this, PR, the start, LLM, and LLM methods already, exist, so.
Liudmila Molkova 00:19:11 Yeah, let's keep that. What I'm saying, let's not add… New ones like this for embedding.
Shuning Chen 00:19:18 Okay, okay, now makes sense, yeah.
Liudmila Molkova 00:19:23 It seems you don't have them, right?
in your PR.
Shuning Chen 00:19:29 Right now, I have them, I can remove them.
Liudmila Molkova 00:19:39 Okay, I, I, I would like that. Sorry, I interrupted somebody.
Sergey Sergeev 00:19:44 Sorry, it was me interrupting you. I wanted to check, Just high level, is it, the idea to have just, standard start-stop, fail methods, and basically… in court, the different actions based on invocation type?
Yeah? Is it… Basically, check the invocation type, and basically… Then, do different actions, right?
Liudmila Molkova 00:20:18 We already do this, it's just the stop embedding, fail embedding is the wrapper on top of that method, and it does not… Do anything at all.
And, like, maybe in the future, I, like, from the API design perspective, it would be cool if we did, let's say, start LLM, and we provided not the invocation object, but the required properties of the invocation, LLM invocation, and we returned LLM invocation object.
back. It would be nicer, but it's not related to this PR at all.
Shuning Chen 00:21:02 Okay, okay, sure. I will remove the, yeah, these embedding methods, and please take one more look, yeah.
Thank you.
Liudmila Molkova 00:21:10 Thank you.
Riccardo Magliocchetti 00:21:13 Thank you.
And then… Next topic is from Lucas.
Lukas Hering 00:21:25 Yeah, Ricardo, I know, I think we discussed this a little bit.
Just for context, this is for implementing, Part of the configurator changes, specifically for meters.
What I want to just… what we want to discuss is kind of what approach we want to take for actually applying the… Configuration updates.
So, I think the approach in Ricardo's initial implementation It was decided to kind of just… Call the configurator, to get the configuration every time we access Any property on the configuration, which for now is just the enabled flag.
But… The approach that I went for for metrics was, I guess, Mercado's original implementation, which is to sort of Lazily update the configurations only when The user actually updates the meter configurator, I'm not sure if that's… I'm not sure if I'm making a whole lot of sense here. I know, I think, Aaron, you were… You're kind of up to speed on this, maybe?
Goodbye.
Chime in here.
Aaron Abbott 00:22:49 Yeah, it sounds vaguely familiar, I remember talking about this on the Tracer one with the week set, and I think… so, Ricardo, you're saying that we already have the week set in metrics because of some other check?
Riccardo Magliocchetti 00:23:03 Nope, we have a plain dict.
But… Yeah, we already have a cache of the… the meters.
Aaron Abbott 00:23:13 Okay.
Lukas Hering 00:23:14 So, yeah, what was the objection with adding the weak set here?
Aaron Abbott 00:23:21 I think… I think the reason I left this comment was that it was just a little more complicated, So, like, instead of having weak set, you could just have the reference backward, but then, I think, Ricardo, you raised a point. It was either something about walking, or… You have to… you have to know when to reread it, or re-read it every time, is that right?
Lukas Hering 00:23:46 Yeah, you would need to read it. If you just store a reference to the configurator, you have to call it every single time you access anything on it.
Aaron Abbott 00:23:54 Right, right, so it's not just a Boolean flag, it's like a predicate function.
Lukas Hering 00:23:58 returning an object. I mean, right now, it's just a billing flag, but I mean, thinking, like.
Long term, there'll probably be more… more attributes being added to it.
There's also the question of… I think you raised the question, like, is this expected to be a peer function?
Because if we only update when we set the configurator, it might not work as expected if the functions are not pure, but actually reading the spec, if you read the spec, I'm pretty sure… it doesn't explicitly say it, but it implies that these are pure functions. The configurators are expected to be pure functions. It even kind of hints that the… fix the… The natural implementation is to actually Cache the configs, and then only update them when the user updates their configurator.
So… That's my diet list, yeah, so… Aaron Abbott 00:24:57 At which implementation was that? You mean it would be the one where we keep the week set and then update it?
Lukas Hering 00:25:03 Right, yeah. If you click on, I added in the doc just a link to, the section in the spec.
It even kind of explicitly says, like.
When the user updates the configuration, or the configurator, update the configuration for each meter, only when the… Yeah, it should be… The function is called when the meter is first created, and for each outstanding meter when a meter provider's meter configurator is updated.
Okay. So… Aaron Abbott 00:25:35 Yeah. Yeah.
Lukas Hering 00:25:38 Yeah, I agree, it's more… it's a little bit more complicated. I think it's only the tracing that needs… that we need to add the week set for.
And maybe the logging, but, I think also performance-wise in the future, it'll be advantageous to do this.
Aaron Abbott 00:25:54 Yeah, yeah, I think sometimes the spec kind of implies implementation, and then there's definitely somewhere in here that it says… I don't remember if it's here, if it's tracing, where it says it's not defined whether or not the same meter is returned every time.
Which… kind of implies, like, you would be churning a week set all the time if you had an instrumentation that was calling, like, getMeter. I think it says you can call getMeter each time, and basically it's undefined, If you would get the same reference back. So, like.
Lukas Hering 00:26:23 Oh, interesting.
Aaron Abbott 00:26:24 Yeah, I think… I think we always return… What do we do? I think we return the same one, so… Yeah, I… honestly, I'm not too… like, the implementation is pretty much internal, besides that peer function thing, like, that seems like the… The main difference that people would see if they're… depending on the implementation.
Lukas Hering 00:26:46 Yeah, I can't see any scenario where you wouldn't want it to be a pure function, but… Aaron Abbott 00:26:51 Well, yeah, like, I mean, maybe an example is we have Jaeger Remote Sampler. I don't remember what the status of that is, or if it's integrated with Meter Configurator, but, like, you would have… basically some function that pulls this eager remote sampling endpoint, and then it says, it might say, like, you know, stop… stop sampling, and you could turn it off for the whole meter. I think right now, it's… it's much… it's not that granular, it's more focused on, like, the actual sampler interface, but just an example, like, some kind of control plane thing, or op-amp. I guess the idea is you would change the configurator instead of having the function, call out, right?
Lukas Hering 00:27:33 Yeah, I think that's kind of what the spec expects you to do, though, but, is to actually… you have to update the configurator if you want the effects to be observable, but… Aaron Abbott 00:27:42 Yeah.
Lukas Hering 00:27:43 Yeah.
Okay.
Aaron Abbott 00:27:45 Yeah, maybe we could just… Yeah, we should just, like… I think… Whichever implementation makes the most sense with the assumptions here, and then maybe we could document that this should be a pure function And leave it open, we could always revisit.
Lukas Hering 00:28:06 Yeah, I think… yeah, so we should probably bring this to the… the SMCOV.
Senkov people, then, to maybe make this a little more clear.
Probably add something, like… If you want, you know, your changes visible, you must update the configurator.
Aaron Abbott 00:28:25 Yeah, we could, we could leave a… We could open a bug.
I mean, it's a kind of a mix, because also, if it's a pure function, and the… Function pointer is the same.
then there's no reason to, like, recall it. So, I don't know, you could… I feel like you could implement it either way, but we should just document the assumptions about the… The user interface. And then we can go from there.
Lukas Hering 00:28:49 Okay, yeah. And then, I guess, yeah, either Ricardo or… I can do it as well, but we… I would be in favor of just modifying the original Tracer PR to switch to using the weak set after we do the… Metrics and logs implementations.
Aaron Abbott 00:29:11 Okay. Yeah, and if we could add, like, benchmarks, honestly, that would be… I don't… I don't know if we have any memory benchmarks right now, there's… there's, like, a little bit of a way you can set up some, you know, like, CPU time benchmarks, but… Lukas Hering 00:29:22 Yeah, I did set up some… I believe I set up some PyTest benchmarks. Yeah.
So… Aaron Abbott 00:29:30 Awesome. Cool, does that… is that good? You're… you're… Yeah.
Lukas Hering 00:29:34 I think we have a clear path forward. Thanks.
Aaron Abbott 00:29:38 Thank you.
Riccardo Magliocchetti 00:29:40 Thank you.
By the way, like, as I already written, I think, like, I'm open to revisit the implementation, and we also have already benchmarks for the Tracer configurator stuff.
And also, like, earlier today, I was working on… on using, the address reconfigurator for remote updates.
And so, yeah. So, like, I may have other things to revisit in the SDK implementation after, like… Having a real user for this stuff.
Lukas Hering 00:30:21 Alright, thanks, Ricardo.
Riccardo Magliocchetti 00:30:23 Thank you.
And then, next topic… From Sergey?
Sergey Sergeev 00:30:35 B.
Yeah, so… quick, overview, I checked it with Aaron, some time ago, maybe a couple weeks ago. So, high level, the problem, summary. So, it's what a lot of third-party generative AI instrumentation libraries are doing.
So they, provide some APIs.
to easily propagate, generate a conversation ID, or some… custom association properties for every GN AI span.
on the trace, so, a user of this API can set, basically.
some properties, and they will be stamped on every span, every child span. Or at least, they can use those APIs to stamp it on the first span in GenA, Trie.
So, the proposal, we have already OpenClement AOTU, GenAI library, which is a helper for… Those specific instrumentations, and, the proposal is, if you click on that, on the left, on, item 4.
Oh, sorry, item 5, proposed API in Python.
So the proposal is to create some APIs as part of this, OpenTelemet OTL GenAI library, where, customer can set either GenA context, to use the V construct, to basically to… To add that specific Pentext, Throughout the course, within the schools, or… to, Just to make this call, and expect, That context to be propagated, or… To add support for instrumentation aware, specifically a one-chain, one graph supports, for example.
custom metadata configuration, or thread ID configuration, which a lot of instrumentation libraries use in.
as a source for that GenAA conversation idea.
So, This is high-level overview, so there are a lot of questions. Let me… sorry, I see you.
end up… Liudmila Molkova 00:33:15 Yeah, that's awesome. There is something that happens in Open Telemetry right now around this that's not genera… that's not specific to Gen AI.
There is an OTAB, this is the spec proposal to support it, just in general, and there are some API considerations Dear, would it be possible to, try implementing Prototyping.
the proposal made in DataTub.
And it's good.
Sergey Sergeev 00:33:49 I don't.
Liudmila Molkova 00:33:49 tremendously helped this OTEP to move forward, but also it would serve our purposes.
Sergey Sergeev 00:33:56 Yeah, sounds great. If we can limit the scope of the spans, the… The one to up away, the specific, context, so I think it may work.
Liudmila Molkova 00:34:13 Yeah, so, I left a link to the ATAB.
Sergey Sergeev 00:34:19 Yeah, yeah.
Liudmila Molkova 00:34:19 In the chat and also in the doc.
walk through it and see… it probably is very similar to what you're already suggesting.
It's just the more generic API.
Sergey Sergeev 00:34:34 Yeah, I will be very happy to review it.
Liudmila Molkova 00:34:38 Yeah, nice. Thank you.
Sergey Sergeev 00:34:39 Yeah. And, yeah, we also need, probably, as part of this API, to, to be able to configure, so, using environment variables or explicit API, parameters if we want to set this context just on the span, if we want to propagate it to the child span, and how we propagate across RPC boundaries, so… Aaron, you have a question?
Aaron Abbott 00:35:16 Yeah, I think… I was gonna kind of maybe, like, generalize this to the Python SIG audience?
Sergey Sergeev 00:35:24 so appreciative.
Aaron Abbott 00:35:25 Yeah, I think, So, I wanted to call out, I think with Mill, you mentioned in Java, they have this kind of generic Semconf mechanism, right, where it generates context keys for certain spans.
Give me honest here, though.
Liudmila Molkova 00:35:40 Yeah, yeah, so they would have something like, this is the HTTP client span.
On the context.
Aaron Abbott 00:35:52 And there's nothing, as far as I know, there's nothing really in the spec about this. This is kind of, like.
An instrumentation-specific implementation detail, right?
Liudmila Molkova 00:36:01 Right, yeah.
Aaron Abbott 00:36:04 Yeah. So at the expense of overgeneralizing, like, do we… do we think we should… maybe raise this, because I think the main decision is kind of like… I left a comment here in this doc, but… Do you… Like, first of all, there's the question of stamping.
Stamping the same attributes on, like, child spans automatically.
I'm not… I'm not sure if I'm 100% sold on that.
And there's nothing in the spec as far as I know about it. And then the other kind of question is.
Whether you send the, like, the span downstream, or whether you, Actually, if you… Sergey, can you expand that comment on the right, where it says show more?
Sergey Sergeev 00:36:43 It's not me, Sharon, so I can take over and public.
Yeah, if you can explain Aaron's comment, that's right.
Aaron Abbott 00:36:54 Yeah, that one, yeah.
Yeah, like, context key targets the attribute keys, context key targets the spin.
Or the context, stores the actual spin. So… I'm not sure what Java does, but… yeah, I think the design space is kind of there, and I'm… I'm also not sure about the automatic attribute propagation.
like, automatically being stamped. So I don't know if we need to bring this to the spec.
To get some more clarity.
Liudmila Molkova 00:37:24 This is what already happens with the Carlos and the context scoped attributes. If you're familiar with something like MDC or, like, login scope, you say, okay, everything under the scope is going to have this attribute stamped.
Baggage, I think what Carlos is proposing, taking it separately for now, at least, not propagated through RPC.
This… seemed… it was the topic in Open Telemetry for, like, since the beginning, and it never happened, and everybody wants it. So I think it will happen in one way or another, but this ATAP is the great place to bring these concerns, and it's very hard to have, like, targeted injection, right? We can do this with uploadho, by the way.
it can be used for targeted injection of attributes. But I… Sergey Sergeev 00:38:24 I can, I can provide some, ideas, how we, on SDOT, Sponge Dist, implemented it for first MCP. Basically, there are environment variables for.
The client instrumentation and the server instrumentation, which controls, which attributes should be propagated, and… On the client side, and on the server side, which attributes should be inferred.
On the server side, so it gives controls, To both the client and the server, and by default, no propagation happens.
Because, just send in something like, customer session ID.
Maybe a huge security risk.
So if we… we can generalize it, for… Not necessarily to be specific to a particular protocol.
Liudmila Molkova 00:39:28 Yeah, so, like, I… yeah, it would be great. What I'm saying, that let's try to provide the feedback on that app.
And this is… then it will be… cross… I tell.
Thing.
Aaron Abbott 00:39:45 Yeah, Ricardo, do you mind?
Sergey Sergeev 00:39:45 It's… Aaron Abbott 00:39:46 Do you mind opening the OTAP? I kind of missed that part at first. It's in the meeting notes.
Yeah.
Yeah, this is great. I didn't even know this was here. It's good timing.
Liudmila Molkova 00:40:00 Yeah, and it's been out there for maybe 5 years. Just, yeah.
Finally, somebody that takes care of it.
And this is a little bit orthogonal to what Java does, because they are saying, okay, these are HTTP client spans. These two things… the only thing common between them is that there are some keys on the context.
Sergey Sergeev 00:40:28 Yeah, the good news, I'm pretty sure I know what I want from the GenAI.
site, so I can.
And now it will be just a matter.
Generalizing it and figuring out if we can make it, Just generic enough.
Aaron Abbott 00:40:51 Cool. So it sounds like maybe we'll just start by reviewing this OTEP and bring some of the discussion there.
Sergey Sergeev 00:40:57 Yeah, it can do it.
Aaron Abbott 00:41:00 Awesome.
Liudmila Molkova 00:41:00 Careful.
Sergey Sergeev 00:41:08 Again, if anybody's interested to review, the document I shared, I will appreciate any comments, any feedback, etc.
Riccardo Magliocchetti 00:41:25 Okay, thank you.
Okay, next topic is from Ben.
Benjamin Kawecki 00:41:37 Hey, how's it going? It's my first time in this meeting, so if I get anything out of turn or anything like that, let me know, and then, yeah, nice to meet you guys.
This was from something I've kind of noticed when interacting specifically with, the OpenAI client in streaming and its use of the logs API in, like, the newer versions. In the original OTEP that deprecated span events.
It talked about creating, like, bridges where possible. I think it, like, linked a Java bridge implementation.
To effectively allow people who still depended on having a single protobuf export of both spans and the events relevant to those spans, or logs relevant to those spans.
as, like, a backwards bridge until it was fully deprecated. One thing I've noticed is that, with OpenAI using the Logs API directly, there's no way in streaming use cases to capture the output event.
onto the span.
And this kind of has to do with there's not really a good API interface. When the active span, so the OpenAI streaming span in this case, is out of context, or it's typically out of context when that event.emit, or log.emit.
is called, and so there's no way, because it has the span context, so it has trace ID, span ID, but it doesn't have a reference to the actual span itself.
So there's no way to… and you can't get the current span because getActive span doesn't return the same span. There's no way to attach it back.
This isn't an issue with, like, unary operations, but it is an issue with streaming. And I know, like, this backwards compatibility isn't, like, the main reason, and there's a lot of reasons why people are moving to log records. I just wanted to highlight this, because I don't think there's a viable path forward on this, at least from looking, like, through all the APIs.
Liudmila Molkova 00:43:37 Can, can you, elaborate what this… Why do we need a span itself, in case of… in any case, when we use logs API, we don't need a span?
Benjamin Kawecki 00:43:52 Yeah, so using the logs API is… or sorry, my understanding in reading through the OTEPs is that span events were deprecated in favor of log records, and that instrumentation libraries were encouraged to move over to log records, and if they wanted backwards compatibility, they could call the There's two things. One is there was a proposal that they could just call span.add event, which would keep the backwards compatibility. And then also there was the introduction of a, effectively a, like, a concrete logger provider that would be a bridge and effectively call that span.add event on behalf. So, like, for example, let's say the user still wants to have their, events on the same protobuf as their spans, because they're, I don't know, doing some back… like, some processing, and they haven't migrated to fully using, like, a separate stream of spans and logs yet.
That was the, I guess, the motivation behind this.
Liudmila Molkova 00:44:51 Okay, so you want to capture something as span event rather than log record.
Benjamin Kawecki 00:44:57 Correct. Until, until, you know, we can build out, like, internal support for, you know, being able to join those together on the backend, You know, previously we were just ingesting, like, a span event, or the stream of spans, and then using the fact that the events were on that same protobuf.
If… I can link the recap and what it talks about.
Liudmila Molkova 00:45:17 Yeah, that, the… The latest version of Gen AI instrumentation, the OpenAI Instrumentation, does not even meet Well, let me log records, but it's an alternative to spend. You can have this attribute… the chat history as attributes on SPANs.
So, I'm curious, why do you even want to… Spend event at all.
Benjamin Kawecki 00:45:46 I believe the attributes on spans were part of the 1.37 set of features, is that correct? I think the 1.36 SEMCOM had them being span events, and then 1.37… or had them being events, and then 1.37 is where the support for, The data or content being part of attributes was introduced.
Aaron Abbott 00:46:11 Actually, Ricardo, if you can scroll down a little in the thread.
To my response, I think.
Yeah, at the bottom, below.
Yeah, that… Yes.
Does that, does that sound right? It's pretty much what I mentioned there, right?
Benjamin Kawecki 00:46:33 Correct.
That is correct.
Aaron Abbott 00:46:35 Yeah, so I'm also curious about Lamilla's question, like, are the attributes not good?
Benjamin Kawecki 00:46:41 It's more that, like, we have to build our… like, we didn't have support for the more complicated attributes. We were, like, doing the 1.37 migration on our backend, to be able to handle that. Like, our data model, it was kind of a bigger change for, like, our internal data models, and so we were trying to keep the 1.36 behavior as long as possible.
Aaron Abbott 00:47:05 Gotcha.
And, my other question then was, like, the… I don't know if the OpenAI V2 was doing this, but I don't think we ever had them set as span events, right?
Benjamin Kawecki 00:47:19 No, but we had a, we had implemented our own log processor that was able to do this, per, like, the OTEP on keeping functionality, or, like, keeping the backwards functionality.
Aaron Abbott 00:47:31 Okay, so, like, when you saw a… so you had a processor or something, and when it saw a… A regular log event, it would convert it to a spend event?
Benjamin Kawecki 00:47:40 Correct.
Aaron Abbott 00:47:41 Let's see.
So that still works if you, if you don't set the experimental flag, right?
Benjamin Kawecki 00:47:48 No, it does not work any longer.
It has to do with how the… the… In order for that, like, backwards compatibility mode to work.
The span that is… or the log record, span context must equal the active span span context.
And if you look at the Java implementation of this, they do, like, an explicit check.
But due to streaming, right, like, we don't want to have the active span in the span context for a long period of time, so when the span leaves the active span context, it's, like, no longer possible to attach it via this backwards compatibility method.
Liudmila Molkova 00:48:38 I agree, yeah, I agree with this conclusion that it's not possible.
it… It could be possible to add a duct tape that makes the span current, too.
allow this, but I… I think this is the… the past.
And… It's… Solves a narrow issue for something that we don't want to support going forward.
Yep.
Benjamin Kawecki 00:49:12 That makes sense. I just wanted to bring this up. It seems like the only… the paths out are to move to the 1.37 plus semconvin attributes for supporting spans, or span-only transport, I guess? Is that correct?
Liudmila Molkova 00:49:26 I would recommend that, yes.
Benjamin Kawecki 00:49:28 Okay.
Aaron Abbott 00:49:28 Yeah.
Yeah, plus one to that. I think… I would also, like, you know, if you could file a bug in the instrumentation, I feel like, even if they're not the pre-1.37 events, like, if there's some streaming happening, it would be nice if the, the span… excuse me, if the span was still in the context so that any logs do get attached, like, you know, regular logs, if it's like, You know, info logs or whatever.
It could be impossible, I guess, because of the asynchronous Nature of it, but… .
Benjamin Kawecki 00:50:03 I think it's the async generator side. It's like, if you reactivate the span on entering next, then you don't… you can get some really wonky behavior on changing, like, especially if the user's, like, interleaving streaming calls or doing something weird like that, you can get some really weird behavior.
Aaron Abbott 00:50:19 Yeah, so async generators are kind of just broken with Python context right now, but I think we could… Benjamin Kawecki 00:50:24 Yes.
Aaron Abbott 00:50:24 If it's just, like, a simple… if there's a bug, we could discuss, you know, maybe fixing it, and it could help you, but I would also recommend just moving to the post 1.37 one, also.
Benjamin Kawecki 00:50:34 Okay, awesome.
Aaron Abbott 00:50:37 Yeah.
Aditya?
aditya (cisco/splunk) 00:50:42 Yeah, so this thing, right, that you guys were discussing, I was a bit distracted, but I think this 1.37 plus 1, right? So, I'm right now working on the telemetry handler in the GenAI utils.
And the GenAI utils is right now, using, I think, 137.
And there was a customer that we had… which were using, like, a SEMCON version, like, 1.39. The SEMCON version, I think, was 0.6.
Like, 0.60.
And I think… it will break for them, right? If they upgrade it to that.
So if you upgraded the telemetry handler to the latest SEMCONS, correct?
If we are emitting the events from there.
Like, the Gen AI events that we have.
Liudmila Molkova 00:51:41 We… this is the opt-in flag user set.
If they don't set it, there is a default behavior, at least in OpenAI, that doesn't use, telemetry handler and Gen AI tools.
And things will stay for them as they are. If they opt in, yes, this will be breaking.
aditya (cisco/splunk) 00:51:59 Yeah, so, okay, yeah, I'll take a look at my PR closely. I'll try to test it out with the latest changes, because they have, like, some of the things that they were using.
From the hotel world, it had… Latest, change the latest versions.
And… but for now, I just asked them to… Use a, like, an older version, and it worked fine for them, but… Yeah, currently I have a PR in the… work, so I'll take a look and… So then, probably, we'll have to change the GenAI utils if it is using any tech… because I'm also seeing, like, some errors related to the SDK log record being deprecated, and we have to start using something else.
That's another deprecation that I'm seeing in the newer versions, right?
So, where we get an error that… SDK log record is deprecated.
Something like that.
Aaron Abbott 00:53:07 Yeah, I, I think… we should probably wrap up on this. There's just, like, a couple more, but then if you wanna… no, I mean, feel free, if you want to respond, we can just wrap this one up.
aditya (cisco/splunk) 00:53:17 Yeah, yeah, yeah, that sounds good.
Benjamin Kawecki 00:53:19 Nope, no other… no other responses for me. I have some, like, other things, but I'll… I don't want to derail stuff too much.
Aaron Abbott 00:53:27 Yeah, yeah, I just want to make sure we get to the other topics.
But thank you, and thanks for coming, Ben. Always nice to see new people.
Riccardo Magliocchetti 00:53:38 Okay, thank you. Since I see that Mike joined the call, we should probably… Go for the first two topics here, Mike?
Mike Goldsmith 00:53:57 Here we are. Hello, everyone. The, the first one was, something that I shared in Slack, is that I've noticed in our commit history, we always use the commit list as the list of things that, goes into the merge squash commit. That can be a little bit… unusable, it doesn't really say a lot of information. So this was just a suggestion to change our repost merge settings to use the PR title. It's an easy change, but then it just means that the commits that go into the main branch are a little bit more readable, and then they still have the PR issue ID, so it's easy to reference to go back to the GitHub if you need to.
I think there's a few people that thumbed it up, so I just wanted to raise it here to make that change.
And… I think… does anybody disagree with doing that?
Aaron Abbott 00:54:45 No.
Mike Goldsmith 00:54:47 Okay.
Great. The second one is, I've been doing some work on declarative config this week, the… There's four PRs open right now. The resource and propagator one, is, one that is marked ready for review. I've had a couple of more… some feedback on it, I think that's just about ready. And then the other three, which adds the tracer meter… the tracer, the meter, and the logger providers are all set, dependent on that, but then are ready for review, because they are all just additive, so… Once that's done, then we can start looking at making, like.
making the final changes to make the API public so people can actually interact with it, so I think we're getting close to that being done, too. So it's just… they're all ready for review.
Riccardo Magliocchetti 00:55:31 Thank you.
Aaron Abbott 00:55:32 Awesome.
Thank you.
Riccardo Magliocchetti 00:55:40 Okay, and then… I think the next one is this one. Keef, looking for reviews.
Keith Decker 00:55:51 Yep, it's just adding tool call types to GenAI Utils. I'm watching the other PRs for embedding and, agents closely for the tool call implementations to follow. Already gotten a few reviews and approvals on this, so just looking for… Some more.
Oh, Luma just approved, so… we're good.
Riccardo Magliocchetti 00:56:14 Thanks.
And then we have Erdin.
Erdenesaikhan Tserendavga 00:56:22 Yeah, hi, Odon.
Aaron Abbott 00:56:28 Bill?
Erdenesaikhan Tserendavga 00:56:29 I am.
Editor, demo application, which is using the, which takes, instrumentation from the Google, and… or create agent spend type for the, generities. It is creating the, remote agent using the vertex, AI agent in Jain, and also I have, included the demo of the instrumentation in this PR.
Also, same demo application, In working that, remote agent, and creating the, instrumentation.
From the remote teaching, and, also provided the application And, I'll… Okay.
collector.
Yeah, I'm asking the review on that.
Both Pierre, please.
Liudmila Molkova 00:57:27 How much do I care about attention creation? And invocation, yeah, definitely, but, like… Do we actually have any instrumentations that need Create Agent?
Sergey Sergeev 00:57:42 Yeah, I… I think I also was wondering what is the practical… practicality of create agent, and I wanted to check here, maybe it's a better fit for Gen AI Isig, but if anybody trying to capture the agent graph.
In CreateAgent.
So when you compile, for example, one graph.
You have that, graph definition, which may be… Used, which may be captured in… When you compile the graph.
So you can put it into agent description.
Of the create agent, and use it for… Basically, visualizing of, Agent Graph or something like that.
Wondering if anybody is using it.
Liudmila Molkova 00:58:37 This guy is specifically for server-side agents, so, like, OpenAI systems.
And there are, I think, Bedrock, who has this API as well, to create an agent on the server.
Not for the local agents.
Erdenesaikhan Tserendavga 00:58:56 Yes, that's true.
Sergey Sergeev 00:59:00 So, same question.
Anybody can choice, the remote agent, description, or… Definition, and use it anyway.
Maybe for the future.
Liudmila Molkova 00:59:18 And it's useful if you create agents remotely. If you create them in process, you can report just the metadata on the Invoke agent span.
The operation itself is not interesting.
Sergey Sergeev 00:59:30 I think, I think, capturing, basically, when you create an agent, and when it's, Maybe you want to capture something like a prompt, maybe you want to capture some specific, Configuration or structure of the agent.
And this is, when you can use it.
Liudmila Molkova 00:59:57 Well, let's discuss it in the Gen AI SIG, probably, because we will need a different definition for this agent creation operation, then.
Sergey Sergeev 01:00:09 Yes, sounds good.
Riccardo Magliocchetti 01:00:10 Yep.
Thanks.
Erdenesaikhan Tserendavga 01:00:13 Thank you.
Riccardo Magliocchetti 01:00:17 So, Aaron, you have an empty topic?
Aaron Abbott 01:00:22 Yeah, I… we could just keep going. I was gonna bring up the, The one about the log context, but it seems like there was some good progress on the issue, so… can skip.
Riccardo Magliocchetti 01:00:33 Okay.
Man, you didn't meet up?
Liudmila Molkova 01:00:36 Yeah, we don't have time to discuss it, really, but what I wanted to bring up is that, with all the changes, amazing changes we have in Gen AI tools and in instrumentation libraries, it's essentially impossible to have, a compatible list of instrumentations, for GenAI in one application.
and we've been discussing that we can't release them together, what I'm actually proposing, that maybe we should release them along with the rest of libraries, plus have means to release them independently.
I've gone through the releases in the past 6 plus months, and it seems we are releasing GenAI leaps no more frequently than once a month, and would actually benefit from Putting them in the common bundle.
And we probably won't even need to.
Release more frequently, but it's good to have the possibility to do this.
Aaron Abbott 01:01:38 Yeah. Yeah, I think we should chat in the you know, GenAI Sig, too. I… I feel like the… it was a good idea, but in practice, it's… you know, some of them are maybe being released less frequently, so… I'll leave a reply on here, maybe we can chat next… or the following Tuesday?
Liudmila Molkova 01:01:55 Yep.
Aaron Abbott 01:01:56 Indeed.
Thanks for looking at it.
Liudmila Molkova 01:01:58 Yeah, thank you.
Riccardo Magliocchetti 01:02:01 Thanks. We have one minute left. I think we already seen this one before.
Nope, another one.
Josh?
Josh Winerman 01:02:17 Yeah, just, asking for more review on this. Thanks, Mike and Pablo, if you're both here, for the approval, but just looking for more eyes.
Riccardo Magliocchetti 01:02:26 Thanks.
And… Yeah, I think the same for Redeemer.
Ridhima Satam 01:02:36 Yes, so this is just adding the support for workflow in the GenAI handler, and It has the same pattern that the start workflow, stop workflow. I get the comment from Ludmila on Schooning's PR, so maybe after Shuning peers get merged, we can follow the same pattern, but just, want some review, other comments, any… If anyone has.
Riccardo Magliocchetti 01:03:02 Thanks… And another one from Mali.
Yazdankhah, Mani 01:03:09 Yeah, so Aaron has already reviewed and approved this, but he asked some additional tests to be added. I added those. I think he had a few questions for other maintainers, which have not been addressed. I've kept them open.
If, if yet.
I'm not sure how to proceed with getting this merged.
Riccardo Magliocchetti 01:03:31 Since this is me, I think I'll need to take a look there. Sorry.
Yazdankhah, Mani 01:03:36 No problem.
Riccardo Magliocchetti 01:03:45 Okay, and I think we don't have.
Lukas Hering 01:03:50 We can… we can skip that, it's… It's not super important.
Riccardo Magliocchetti 01:03:58 Okay.
And then… thank you, everyone.
Yeah.
See you next week, maybe?
Bye.
Liudmila Molkova 01:04:11 Thank you.
Ridhima Satam 01:04:11 Right, thank you.
Keith Decker 01:04:12 Bye, everyone.
