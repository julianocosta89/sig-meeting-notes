SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-11
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:18 Hello!
**Siri Varma** 00:20 Hello.
**Trask Stalnaker (Microsoft Corporation)** 01:13 Hello.
Am I audible?
**Liudmila Molkova** 01:17 You are…
**Trask Stalnaker (Microsoft Corporation)** 01:18 Meaning… I am, but it's going to the wrong… Not the headset.
**Liudmila Molkova** 01:31 Now you're… Sound like you.
**Trask Stalnaker (Microsoft Corporation)** 01:33 Okay, that's better, yes.
**Liudmila Molkova** 01:39 Hey, welcome to the stabilization effort, again.
**Trask Stalnaker (Microsoft Corporation)** 01:44 Yang!
Just posting my homework.
**Liudmila Molkova** 01:54 Nice.
Let's go through your homework, and then let's see how it aligns with my homework.
**Trask Stalnaker (Microsoft Corporation)** 02:02 Alright.
**Liudmila Molkova** 02:04 Do you want to present to…
**Trask Stalnaker (Microsoft Corporation)** 02:06 Yeah, sure. Yeah, mine is pretty straightforward.
Yeah, so, one minute ago, tracking issue for stabilizing, inference and Core Agentic execution… Semantic Conventions. So I tried to basically very minimal scope, so execution meaning not, like, create agent, delete, not the, Control plane stuff.
And all of this, I just tried to come up with the very most minimal, and then, of course, we can discuss more.
Spans, inference, invoke agent, execute tool.
I think MCP we can talk about it, whether we want it in or out. I don't… I think at least there's a clean boundary of it not being in, but it's also been around for a while, and probably would… would be… odd.
Could be manageable if there's interest.
For metrics, then… Again, just the core metrics around inference, Invoke agent, duration, execute tool duration, the… I… Kept these in, it could… it could come or go, I don't know how important… They are.
And this is, you know, kind of the key one that we've been discussing, token usage on Inference bands.
I did not include… Token usage on agent spans, or number of tool calls on agent spans, or number of inference calls on agent spans.
And events, obviously the exception event. I didn't include the details event, but, you know, again, I was just… as a first cut, I wanted to be aggressive of what's the absolute minimum scope that Would be useful in the world.
**Liudmila Molkova** 04:53 What do you feel about embeddings?
Any particular reason they're out?
**Trask Stalnaker (Microsoft Corporation)** 04:58 No, I… No, I guess the… I didn't… at least in the… maybe, probably just, I'm not as familiar with the workflows that use them,
**Liudmila Molkova** 05:27 Yeah, they have every 2024.
**Trask Stalnaker (Microsoft Corporation)** 05:29 They don't feel core to me in my workflows, but… No, no objection if we want to include them.
**Liudmila Molkova** 05:44 Only reason I think it might be useful to have them is… To demonstrate that they have individual metric name.
An individual span type, but we can do this with… Without marking them stable.
And we can mark them stable at any moment later, they are not controversial… I don't think they are controversial, at least.
**Aaron Abbott (Google LLC)** 06:16 Much the same as the inference ones, right? It's, like, very similar.
**Liudmila Molkova** 06:21 But easier, right? There is no output.
**Aaron Abbott (Google LLC)** 06:24 Yep.
**Dylan Russell** 06:31 Seems like if we have the inference span, we should have the inference event.
Just there, like… Pretty much the same, right?
**Trask Stalnaker (Microsoft Corporation)** 06:43 I… yeah, maybe you… you all can fill me in, sort of, of the, when… I wasn't clear when we used the event versus the span.
**Dylan Russell** 07:00 I think we… I think we should be using both.
And there's a flag that controls whether the event gets enabled.
And there's some discussion over what the default of that flag should be.
**Trask Stalnaker (Microsoft Corporation)** 07:22 Right, but why? I guess the question is why, like, why do people… need.
An event versus a span.
**Liudmila Molkova** 07:32 The complex attributes, the input, out-of-put messages that Or somewhat more acceptable in logs, then?
Spence.
**Trask Stalnaker (Microsoft Corporation)** 07:46 But we finally got complex attributes on spans.
**Liudmila Molkova** 07:50 Yeah, it's not… it's about the storage, the backend.
So, the backends are still more open to having large ends.
complex data there.
**Aaron Abbott (Google LLC)** 08:06 Yep.
That was… there was one other point as well, and that was that we heard… from some customers, there's the EU AI Act, and maybe somebody can Keep me honest here, but there was… a question of whether, like, it's important to capture the prompt responses separate from the sampling events, sorry, separate from the sampling rates of spans. So, like, capturing 100%.
Of the prompt responses was important for compliance purposes, and having an event lets you decouple from the span sampling decisions.
**Trask Stalnaker (Microsoft Corporation)** 08:44 That one, I'm a little… Curious about, because, I mean, is it just that you… I mean, you could… Have a sampling rule that says always capture 100% of my inference spans.
**Aaron Abbott (Google LLC)** 09:04 With, like, with no parent, kind of thing?
**Trask Stalnaker (Microsoft Corporation)** 09:06 Yeah.
**Aaron Abbott (Google LLC)** 09:09 Yeah.
**Liudmila Molkova** 09:10 You could, but it would mean you capture everything under wraps.
Well, it's… it's difficult to configure a sampling for that… that's… Not a tree-based.
**Trask Stalnaker (Microsoft Corporation)** 09:27 Yeah.
Yeah.
**Liudmila Molkova** 09:38 Well, I think it's just important, it's just something that Google depends on, and I… it's kind of important for Google, I don't know if there are other companies that it is important for, but I'm here, I'm advocating for myself.
**Aaron Abbott (Google LLC)** 09:55 We've got some hands, too. I don't know who is first here.
**Trask Stalnaker (Microsoft Corporation)** 09:59 Yeah, Neil.
**Neil Yashinsky** 10:00 Ankit can go first. I think we went Zymo. Ankit? Ankit, you wanna ask?
Maybe while he's going off mute, I'll just say, like, I feel like those are separate things, like the inference event and the telemetry, if I'm… I came just a few minutes late, so forgive me if I'm conflating things, but it sounds like those are separate concerns, which have overlap, but, You know, deserve… Consideration as their own entities.
Thanks.
**Trask Stalnaker (Microsoft Corporation)** 10:35 Okay.
**Ankit Singhal** 10:38 I think, I had one more, data point, and this is around, like, Customers also asking for, better, like, access controls on the sensitive data.
And then, roughly, I think… If they are, like, stored as, or, like, the sensitive, the attributes which have sensitive data are stored separately, as events, right, in a way. I think that kind of helps achieve that, too.
**Aaron Abbott (Google LLC)** 11:17 Yeah, that probably brings us to the REF discussion as well.
The, like, starting in customer-managed blob storage kind of thing.
**Trask Stalnaker (Microsoft Corporation)** 11:35 Okay, so what I'm hearing is definitely inference event is in.
Sounds good.
**Ankit Singhal** 11:45 Yeah, and probably the rev storage as well, which I think, Aaron also brought up.
So that there could be, more restricted access.
On the sensitive parts of the data.
**Trask Stalnaker (Microsoft Corporation)** 12:05 Are you saying that ref… I mean, do we… Yes.
**Ankit Singhal** 12:10 Tiffer story.
**Trask Stalnaker (Microsoft Corporation)** 12:10 Which sounds like a lot to… for, I mean, for a feature that we don't have yet to… Make that a blocker on stability.
**Liudmila Molkova** 12:24 I have mixed… I have mixed feelings about making it stable, but I don't think it's big.
I'm going to bring it up, like, the principle on the SemConf call on Monday, but I think what it implies is that we define attributes for, like, a handful of attributes that are already big and complex, that we define them as additional things for them as refs, and say that instrumentations or pipelines may put the content there. But the details of how.
Is out of the scope.
**Aaron Abbott (Google LLC)** 13:06 Yeah, I was… I was gonna also mention we do have it's not, like, attributes, but we have the wording around hooks in the SemConv.
Like, when Instrumentation should call them, and roughly what the API should look like for them. It's… I guess it's kind of non-normative right now, but… There is some stuff there already, we should… We could also poke around. I think Alibaba also depends on this… the hook mechanism.
We could check with them.
**Liudmila Molkova** 13:37 Yeah, I don't think we have to stabilize this wording, but I think I would like us to… Have clarity on the ref attributes, like, stable or not.
**Trask Stalnaker (Microsoft Corporation)** 14:10 And for the hook, is that… something that… we just need in Python instrumentation? Like, is that a Python-specific instrumentation hook, or is that something in Semantic Conventions that we want to… do we have something in Semantic Conventions describing hooks already?
**Liudmila Molkova** 14:31 Yep.
**Aaron Abbott (Google LLC)** 14:32 Yeah, I put the link right there.
**Trask Stalnaker (Microsoft Corporation)** 14:34 Oh, thanks.
Is our hooks related to… Sensitivity?
**Aaron Abbott (Google LLC)** 14:47 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 14:51 They're… they're for scrubbing?
**Liudmila Molkova** 14:54 Oh, no, they're for upload. So, like, you can…
**Trask Stalnaker (Microsoft Corporation)** 14:58 Even without the graph.
**Liudmila Molkova** 15:01 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 15:01 Gotcha.
Cool.
**Liudmila Molkova** 15:25 Yeah, question about the agent versus workflow. I think you, you mentioned that it's, it's to be resolved.
But, assuming queer.
Keep the current state of affairs, that Agent and workflow are different things.
I think that workflow should be in.
**Trask Stalnaker (Microsoft Corporation)** 15:46 Yeah, yeah, I had, I agree.
I'll make notes.
**Liudmila Molkova** 16:01 I think it's fine, I think your, your, like, the length of the issue covers it.
**Trask Stalnaker (Microsoft Corporation)** 16:06 Yeah, I think it could be clearer. AdWorkflow.
Surya.
**Surya Teja** 16:27 Yeah, the question is around, Retrables plan. Is it also considered for stabilization?
**Trask Stalnaker (Microsoft Corporation)** 16:34 Which spin?
**Surya Teja** 16:36 The retrieve or retrieval span.
**Trask Stalnaker (Microsoft Corporation)** 16:41 I left that out also, similar to embeddings, but, it was definitely, it was definitely… an option that feels like it's been similar to embeddings, has been around long enough that We could stabilize it.
**Surya Teja** 16:59 I have another question on the same lines. A2A is still not published, and it's in PR state.
I believe the plan is to first, stabilize these in A2A, and NGB and others can be considered after the standardization effort. Is that a submission right?
**Liudmila Molkova** 17:19 What did… I didn't hear what exactly you were talking about.
**Surya Teja** 17:22 It's about A2A protocol, let people laugh.
I have been working on it, and the question is, should we… is it also part of standardization, or… Is it, not considered for standardization?
**Trask Stalnaker (Microsoft Corporation)** 17:41 My initial feeling is that, We should only tackle things which are already in semantic mentions and already in instrumentations that we feel that, you know, we know fairly well, that there's good evidence that we can stabilize, and so new stuff. You know, we should definitely continue working on it in the weekly meeting, and progressing, and hopefully, you know.
Given the amount of interest in this group, I mean, this is, like.
Four times as many people as we've had in prior stabilization efforts.
Hopefully there will be interest for the next wave, you know, kicking off the next wave.
Not that far beyond… And maybe, you know, we can just kind of do these rolling stabilization efforts, would be cool.
**Surya Teja** 18:33 Cool. Thanks, Trask.
**Trask Stalnaker (Microsoft Corporation)** 18:42 Alright, what else? Did I miss anything? Anybody else's favorite features?
**Liudmila Molkova** 18:49 I think… From the spans and metrics, I'm an events… It's good. There are also… The new creatures, we need to consider the parts, the… Schemas for the complex attributes.
And there, yeah, there are some… we probably need to draw a line somewhere on how detailed we want to be, because I think Dylan has a great issue describing all the parts that we're missing.
And we need to decide if it's okay to stabilize without them.
Or if it's just some of them.
Ankit?
**Ankit Singhal** 19:37 Sorry, coming back to the events a little bit, do we also have evaluation results in the list, or…
**Trask Stalnaker (Microsoft Corporation)** 19:47 I didn't include it.
**Ankit Singhal** 19:49 Okay.
**Trask Stalnaker (Microsoft Corporation)** 19:50 I know it's a super important event, super interesting, I just don't know if there's… Enough, instrumentation yet?
**Ankit Singhal** 20:04 I see. I can, pull up, like, the libraries which already do instrumentation using that.
If that helps.
**Liudmila Molkova** 20:12 Oh, that would be nice.
**Trask Stalnaker (Microsoft Corporation)** 20:13 Yeah.
**Ankit Singhal** 20:14 Yeah, yeah, I think I did come across some of them which already do,
**Liudmila Molkova** 20:21 Would you be interested in adding them to the conformance suite? Because we have the native instrumentations there in third-party.
**Ankit Singhal** 20:31 Hmm, I see. Okay. Yeah, I think I can, check on that on how to do that, but yeah, let me first find the list of the Instrumenting libraries, or libraries which already instrument that.
**Liudmila Molkova** 20:44 Yeah, and just tell your AI to bring them to performance repo. We will test the quality of our instructions there.
**Ankit Singhal** 20:52 Yeah, yeah, not the… Okay, yeah, I'll take that as an action item.
**Trask Stalnaker (Microsoft Corporation)** 20:59 Cool, and I'll add a comment, or add this to these… to the issue that these are sort of… Sort of, the next tier that we haven't decided one way or another on yet.
**Ankit Singhal** 21:14 No, yeah, that makes sense. I think, definitely. I think tier approach is good, because you can definitely make sure that we make good progress on tier ones, which we are 100% sure about, right? Yeah, definitely, makes sense.
**Dylan Russell** 21:31 So, one thing on parts… So, I think I'll probably go through and figure out, like, what are all the parts that are missing?
Where we just fall back to, like, generic part.
But maybe we also want to say something like, Don't rely on generic parts.
Like, that may become, like, some standardized part in the future.
Like, any… anything we don't have a schema for, we're gonna, like… Fall back to a generic part.
And then, I think there's other weird stuff we do in parts, like we, like, sometimes, like, Base64 encoding.
Text… So there's some weird stuff to look at with parts.
**Liudmila Molkova** 22:22 Yeah. Also, like, I would feel… conflicted about stabilizing video parts for… if we have… oh, we don't have video parts, we have blob. Okay, so this makes things better.
**Dylan Russell** 22:38 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 22:40 Aaron.
**Aaron Abbott (Google LLC)** 22:43 Yeah, also on the JSON schema, If you… if you, like.
try to work with it with the way the generic blob is defined right now, it ends up just allowing literally anything.
So the… the fallback… Makes it so that you can put anything with a type.
String in there, so… I guess the question is, like.
schema evolution's pretty well defined for something like protobuf, but for JSON schema, it'd be good to get it into a state where we can evolve it without making and breaking changes, if that makes sense.
**Liudmila Molkova** 23:19 Yeah, we need to define them in the way that… Would accept future… yeah.
**Trask Stalnaker (Microsoft Corporation)** 23:31 So these, Dylan, anything, or, like, this would be great to just… spam issues, like, for all of these efforts, for all of the stabilization effort, as we find… think of things that should be in, in the effort, create issues for, and we'll get it on the board, and tracking.
**Dylan Russell** 23:56 Okay, that sounds good.
**Trask Stalnaker (Microsoft Corporation)** 23:59 Which, maybe we want to spend a few minutes, Ludmila, you can show us the board, and we can kind of… think about… Next steps there.
**Liudmila Molkova** 24:12 Yeah, okay, so let's take a look at the board now… So, there are… Quite a few things here, and… probably mostly aligned, I'm just thinking how we approach it.
**Trask Stalnaker (Microsoft Corporation)** 24:45 One thought is, I mean, given our time constraint, if you want to call out maybe, like.
2 or 3… high-priority ones that we should all look at by Monday.
**Liudmila Molkova** 25:00 Oh, yeah.
So… Yeah.
Let's look into the to-do.
Let me think for a sec.
I mean, I would appreciate reviews on the, token usage.
And… So, I think that the core parts that we need to do, the renames for the metrics.
And, token usage.
And the agent versus workflow. These are the most hairy areas. Maybe we should start with something smaller.
**Trask Stalnaker (Microsoft Corporation)** 25:53 I mean, I vote for Duckling those, because they kind of… then things start to filter.
**Liudmila Molkova** 26:02 Okay, so maybe we should do this, because this is 3VL?
And this just needs alignment. And there is the… Good issue for this.
So… There is a proposal.
And maybe by the next call, we can… Go through the proposal.
and capture… Anything that we learned since it's been made, so we can start working on this.
how do people feel?
**Neil Yashinsky** 26:44 Makes sense to me.
**Trask Stalnaker (Microsoft Corporation)** 26:47 Yeah, we dropped that in chat, and then also… Drop the… drop the metric… usage… PR… Should we…
**Liudmila Molkova** 27:04 Yeah.
So… Let me paste them in the notes as well…
**Trask Stalnaker (Microsoft Corporation)** 27:12 Yeah, thanks, that's even better.
**Liudmila Molkova** 27:38 Okay.
And, well, if we finish with them on Monday, I… I think I thought we would be lucky, so let's start.
**Trask Stalnaker (Microsoft Corporation)** 27:48 Oh, yeah.
**Liudmila Molkova** 27:48 Agent work versus workflow.
Next.
**Trask Stalnaker (Microsoft Corporation)** 27:54 And then, I mean, in parallel, if anybody wants to, you know, look through the board, kind of, from, Just triaging perspective.
If you see any small chain… any small things that you can send, you know, PRs for that, you know, we can handle asynchronously, that's great, too.
**Liudmila Molkova** 28:19 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:27 But I think that that could be something we kind of do in parallel, asynchronously over the next couple weeks while we tackle some of the big ones in these meetings.
**Liudmila Molkova** 28:39 Yeah, and I think we are pretty much aligned, with your proposal and the issue, Trask on what goes where.
It's just there is a lot of noise here, and… but, and I think areas like MCP, I left somewhere in the no status, until we, like, call it, but we can move them around anyway.
Okay, that's it for the day.
Thank you all.
**Trask Stalnaker (Microsoft Corporation)** 29:12 Awesome. Thank you.
Have a good weekend.
**Neil Yashinsky** 29:15 Thanks for, your leadership. Have a good one. Bye.
**Liudmila Molkova** 29:18 Bye.
