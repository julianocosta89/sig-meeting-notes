SIG: LLM Semantic Convention WG
Date: 2026-05-19
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/P6Dn-sUWAqxo0rKPmkhWi_eyWo0XyHA-D2yFYUcOOkMYm1fyUsF2xbkiUPxnqbqq.qn4ZkER0fLwXcZSV
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 03:33 Hey, Huxing!
Just you, me, and the bots.
**Huxing Zhang** 03:41 Hi, hello, Jessica.
**Trask Stalnaker** 03:44 a…
**Huxing Zhang** 03:45 Can you hear me?
**Trask Stalnaker** 03:46 Yeah.
**Huxing Zhang** 03:49 Okay, Steve and Minghui may join today, I think.
**Trask Stalnaker** 03:57 Cool.
the new… Time for people, so it might take… A couple weeks for it to get into people's calendars.
**Huxing Zhang** 04:16 Yeah.
**Trask Stalnaker** 04:18 Give it a couple minutes here.
**Steve Rao** 04:30 Hi, Chaska.
**Trask Stalnaker** 04:33 Hey, Steve.
I mean, we…
**Minghui Zhang** 04:48 Hello, task.
Hello, Steve.
**Trask Stalnaker** 05:46 Oh yes, the chat part. It still has the odd term.
**Liudmila Molkova** 05:54 Hi, everyone.
Oh, it's a new, new chatbot. Botter!
**Trask Stalnaker** 06:05 Yeah, I already sent two of them away.
This one didn't seem to give us the choice.
**Liudmila Molkova** 06:13 on.
Okay.
Cool, we have some agenda…
**Trask Stalnaker** 06:26 I just coalesced them both, because it's hard to…
**Liudmila Molkova** 06:31 Yeah, you mean from both meetings.
**Trask Stalnaker** 06:34 Yeah, the agenda.
**Liudmila Molkova** 06:37 Cool.
Yeah, I don't think we should do triage here.
We'll keep doing the triage in the 9AM one.
Awesome.
So let's jump in!
Prompt tracking.
Steve, do you want to talk about it?
**Steve Rao** 07:12 Yes.
Yeah, you know, our… internal product. They want to, provide, prompt management for users.
And, in observability scenarios, they want to, Clapped.
the, JNI prompt version, information, and, yeah, I also, sought your, command last week.
And, you… I remind… Whether it's, to collect a prompt variable.
Yeah, and, I also… yeah, we also, take a look at the, documentation. We think, yeah, it's necessary to collect variable.
**Liudmila Molkova** 08:06 Is it necessary for you, or…
**Steve Rao** 08:08 I thought, for, for me.
**Liudmila Molkova** 08:09 Boom.
**Steve Rao** 08:10 bars.
And we also provide a similar ability like OpenAI for our users. Yeah, they want… they… they are going to, launch the product recently, and…
**Liudmila Molkova** 08:28 Yeah. Do you also use prompt terminology? Like, I think that the question is if it's just to providers.
Like, usually they don't align on terminology. Do you use the same terminology?
Like, do you call it prompt? Do you call it version? Do you call it… like, for example, this is ID, and we call it prompt name. I don't remember why, but there probably… there is a reason.
**Steve Rao** 08:58 But, I found, in, Hotel JNI Convention, there is a field called, name.
Yeah. And we also use the NAM.
In our… in our product.
**Liudmila Molkova** 09:18 Okay.
And there is prompt.
**Steve Rao** 09:24 Yeah.
**Liudmila Molkova** 09:29 So it seems like it's, Relatively through… oh, okay, so I… I remember somebody once created the proposal to Record prompt rendering as a… Span.
And it, it, it sounds like… Too short to be a span?
I'm curious if you want to put this on, the inference span, or agentic span, or you would… Also need some additional telemetry items to render those… oh, sorry, to stem those attributes on.
**Steve Rao** 10:12 Yeah, is there any, issue about, your question you mentioned?
Yeah, I want to take a look about that issue.
Somebody wants to, To create an individual span, it means.
**Liudmila Molkova** 10:30 Yeah, but I can find that… I think the question is, what… telemetry, you would put these attributes on, because we usually don't introduce attributes on its own. We put them… we reference them on some spans.
Or other signals.
And that question… What is…
**Trask Stalnaker** 10:51 Prompt name, captured on today.
**Liudmila Molkova** 10:56 It's the agentic… It's a…
**Trask Stalnaker** 11:02 But which span?
**Steve Rao** 11:23 Yeah, maybe it would counter search.
**Liudmila Molkova** 11:28 Oh, on MCP, currently.
Oh, it's currently for MCP.
But… .
**Minghui Zhang** 11:40 Salute. Yeah.
Just a means to, just to refer to the retrieval, prompt.
Right.
**Liudmila Molkova** 11:52 Yeah… Oops.
Okay, and in the case of MCP, there is no prompt.
Version, it seems?
But there is one for… Jeff…
**Minghui Zhang** 12:42 I mean, so, in MCP, maybe we could, retrieve the prompt by the name. So, for these spans, maybe we need to, capture the attribute named the, prompt name. So, I, I, I guess… we just use the prompt name in the MCP span, right?
**Liudmila Molkova** 13:13 Yeah, we currently do, but it doesn't make sense on the inference pens. This is OpenAI Responses API.
Where we could have attached the prompt name to it and prompt version, and if we added template variables, then we would also attach them.
**Minghui Zhang** 13:33 Yes.
**Liudmila Molkova** 13:34 Hi, Erin.
**Aaron Abbott** 13:37 Hey, morning, nice to see everyone.
**Liudmila Molkova** 13:46 We're talking about prompt, name version… And potentially other things.
**Trask Stalnaker** 13:56 Back to Lyudmila's earlier question, since it's on the… OpenAI Response API, is that where you want to capture it? You want to capture it on the inference span?
Is that the only place you want to capture it today?
Because that seems… That seems pretty straightforward, if I'm not missing something, that if it's, let me know that stuff on the OpenAI responses… There's enough different things that… Support that, or use that, that… we could… It's a pretty clear, Reference scenario for the… For both… for putting both of those, we would need to add… we would want to add both of those, prompt name and prompt version onto the inference spans.
**Steve Rao** 15:13 Hmm.
Yeah, okay, yeah, I think, yeah, maybe we can do it like you mentioned.
First.
And.
**Liudmila Molkova** 15:30 Okay, so maybe the next step could be the PR.
Okay. The semantic conventions, and There are some reference instrumentations there that would actually show what you… where you want to capture it.
**Steve Rao** 15:48 Okay.
**Liudmila Molkova** 15:50 And I'll find the issue for the… Mmm… Prompt.
Rendering span, but it's highly controversial to capture a span like this, because it's too short.
**Steve Rao** 16:05 Okay.
**Trask Stalnaker** 16:16 Alright, you've got the next… topic also, Steve.
**Steve Rao** 16:20 Yeah, yeah, yeah, this is, this, proposal we discovered, last week with, Chaska.
And currently in, yeah, Python, contribute, or in Python, hotel Python JNI, repository currently. Yeah, there is, yeah, UTM module, and, there are some, module like OpenTelemetry, Python, JNI.
But, in other, Language instrumentation, They don't, implement it.
can I… a similar, Who cares?
module.
And this is a proposal, yeah, maybe, we can… defined, how to implement, JNI, UTL module in, other language.
in OpenTelemetry.
**Trask Stalnaker** 17:44 So for… just to catch you up, because we spent a while chatting about this in the Java, meeting last week, I talked about… So this, bid… Don't love this.
The Java, they actually kind of started with, wanting to have something like Python's GenAI utils in Java.
so, kind of, we talked about in Java, we have this instrumentation API, which is… It's kind of a lot for users.
It's very nice for library instrumenters. It's got a lot of features, but it's also got a lot of knobs, and so that makes it more… Like, not the best for… End users who are… just want to layer on, and I think in Gen AI, this is more relevant now than other semantic conventions, because there's more people who… because there's not as, who need to inject some more manual stuff into their agentic workflows to… it can't quite be automatically everything captured, in as many cases.
So we've got the instrument… the Java Instrumentation API, which is a little… On the thicker side.
my direction on the… in the Java side is I'm hoping that long-term, I mean, that we will have the Weaver code gen, like, basic wrappers around the SEMCONV.
Start span, that kind of thing, add this attribute to a span, And… that's what I'm hoping will save us in the Java world, save our users from having to deal with the instrumentation API. We will still always use the instrumentation API internally for libraries.
So we've got that option. There's, as we looked, there seemed like there was some things that would need to be, like, that could cover a lot of the things, weaver generation, but there's also some things, like configuration options and things that maybe, maybe we could get Weaver to generate, but maybe there's some manual stuff. It's not a pure code gen thing.
And anyway, I directed them Here, because, I don't, want to add yet another layer in between. Like, I'm fine if they want to start code-genning pure Weaver stuff in the semantic convention Java repo, but I don't want to introduce something kind of in the middle.
Unless there's a kind of community cross-language… Spec, need defined.
**Liudmila Molkova** 21:11 Yeah.
I, I… Maybe I can show a quick demo of what we can do with Weaver.
And… We can move on from… from there. Yeah, Aaron, go ahead.
**Aaron Abbott** 21:26 Yeah, I think… I think I'm also interested in it, but I was curious, I was curious, like, the actual motivation for this question, like, I think… I think it's generally useful, but I want to make sure we're addressing the… You know, the reason you brought this up.
**Steve Rao** 21:48 You, you means my, my, my region? Yep.
**Aaron Abbott** 21:54 Yeah.
**Steve Rao** 21:55 Yeah, yeah, this, this question, comes from when we want to, implement, JNIU tier in Java instrumentation. In Java, repository, we will add, similar class in instrumentation API equator.
**Trask Stalnaker** 22:17 I think Eric's asking more, what's your customer… like, what's the customer use case list?
**Steve Rao** 22:26 Okay. Yeah, in our, internal, users, they want to, have a similar, module, like in Python, a JNIU tier from Java.
from Java, repository.
This is, The original… Requirement.
And, so we, we, we, At first, we don't know how to do it, and by some investigation, we found that if we want to do something like that, we must, Addison class in… to instrumentation API incubator in Java repository, but, we found this, if we put the GenI relative class into the, the common module, the The use case is not very similar to Python. In Python, there is an individual module for JNIU tiers.
So this is the original reason.
**Aaron Abbott** 23:49 Yeah, I can read more over the issue, but I think my… like, I think the kind of tricky parts from my perspective, that would be nice if they were the same across languages, or the parts that are still unspecified. So, like, we have these environment variables, For opting into different semantic conventions, which presumably we're gonna keep using, and the general environment variable is specified, but… the… specific values, I think, is something that we… sorry, that one is implemented, right? That one's in the spec limit mode, but the… upload, for example, there's just, like, a couple pieces which are completely unspecified, and it would be nice if they behaved across languages. So, like, from my perspective, it was… It would be nice if the… Implementations behave the same, and then maybe that's the most important part, and… like, the code reuse could come later, because… as we see more, like, Java agents, or Go agents, or whatever that need to have shared instrumentation API.
**Liudmila Molkova** 24:56 Yeah.
So, I think what we can do, and we can get pretty far with it, So, we can generate… I don't have the Genia example, I should probably create one. But, we can generate quite a bit… 4… From, just the semantic conventions and Weaver.
I just realized I don't have a code here, that's generated, but I have the usage examples that show what it… generates… So this is just the arbitrary conventions.
But you can think about them as GenAI, So here, for example, I have a, span.
storage client operation, or I have a metric storage client operation duration.
Give me one second, I'm… I'm sorry, I'm back. Okay, so, imagine, we had the… Storage client operation.
metric.
Sorry, this is the spend.
This is generated called the implementation of this method. You give it, like, it can be nicer than this, but you give it the operation name, which is typed, you give it some additional information, server address, server port.
And, this is the recording of the metric.
And again, it can be nicer, but essentially, you give it the hyped Attributes instead of a bag.
And it does what it does. So this is not the, like, the layer above, it's not do everything, like the Python generic use, but it, Generates code that helps you start spends, and spends record metrics conventionally.
And this is probably, like, 80% off.
What we can do, and maybe we can even build the common layer that's generated on top.
They're… I think what Trask, you're saying, that, This is probably the start for other languages.
And… potentially… what you're… I'm hearing, you'd rather not introduce some manual, handwritten stuff that's not… Generated at all.
**Trask Stalnaker** 28:21 I'm open. I… would… I… I think it would need to be… I'd still like it to be, like.
Almost, like, mostly the core would be auto-generated.
It would live in the semantic convention Java repo, and we could add… some… hooks, sorta. We could add some customizations on top of that.
I haven't looked at the… I'm not very familiar with the Python Gen AI utils, so sort of all the different pieces there.
But, Steve, I mean, that… that's… and, like, that would at least… that would help the discussion go forward on the Java side, to, like, prototype that.
See how much we can get.
from code generation, And if we can have a… Decent story about layering in custom Code on top of that.
**Liudmila Molkova** 29:51 I would actually start with… designing the API you want to have from code generation, forgetting about code generation for a sec.
And just imagining the thing you want to create, like, starts GenAI inference, or… Required this metric.
And then sketching out this API, and then asking the AI to do the code gen.
For this pattern.
It would be much easier.
**Huxing Zhang** 30:25 Hi, I'm Huxin, can you, can you hear me?
**Liudmila Molkova** 30:28 Yeah, hey!
**Huxing Zhang** 30:29 Yeah, I… yeah, I'm just wondering, are you suggesting that you will, have the unified solution across different language implementations?
Are you, if we are… we are investing on this, Hotel Weaver, so that will be a possible replacement… replacement for Nijing utilities, or… For Python? So next question is… I just want to make sure that we have the same implementations across different languages. So if we are invested on the hotel waiver.
So, I think, if we can replace the hotel weaver, I'm not… I have no objection on that, but, I just want to make sure that Python could follow the same approach.
If they… we have an agreement on that.
**Liudmila Molkova** 31:30 So for Python, the… This is the layer above generated code.
We can… actually replace handwritten parts of GenAIOT also was generated Weaver, but it's… Probably, if somebody wants to spend time on it, for sure, but it's not… I don't think it's super important, because Python has a better story. Maybe we can generate this layer.
As well.
But that needs to be investigated. I'm not super sure, or if that makes sense to generate this layer above.
For the layer below, like, start, Genie AI spin, or… Record that metric.
We. Can.
it's not absolutely the same across languages, because the API should be dynamic to language, right? In some cases, it will report… return, like, context, like start span. In other cases, it will return some other object that's specific to this language, but it will be… Experience, if we design it right, idiomatic to that language, and reasonably consistent, and it should have the same Produce the same telemetry.
**Huxing Zhang** 32:55 Yeah, so… I understand what you mean, but I just want to make sure that maybe we can, try to… try some experiment… experiment on, whether we can have the same approach, with the Weaver, with the Weaver and the Python gen IUTOs.
And we can see that we can implement the same approach in different languages. Currently, we have… actually, we have implement JNI UTLs for… I think Golan and Node.js.
Java is the next we want to… we want to implement, but before doing that, we just put this on… on a discussion with the community.
Yeah, sorry.
**Liudmila Molkova** 33:53 Yes, sir, finish your thought, and we're out of time, but yeah, finish your thought.
**Huxing Zhang** 33:56 I just mean that if you… the community decide to, use the hotel waiver, we… we have no objections, but we can… we can, change that. We just want to make sure that the implementation and the… keep the same… same behaviors across different languages.
**Liudmila Molkova** 34:16 Yeah, I'd like… I had a chat with GS folks, Jamie from Honeycomp, and I was going… they are interested in JavaScript, Cogen. I'll connect you on Slack.
So it would be cool if you both discussed, because I think they are working on the CodGen with Weaver version AI stuff.
**Trask Stalnaker** 34:39 Cool.
Thank you all for our inaugural, Tuesday morning, evening time slot.
**Steve Rao** 34:49 Yes.
**Liudmila Molkova** 34:49 Thank you, y'all.
**Steve Rao** 34:50 Sure.
**Huxing Zhang** 34:52 We'll go with you. Bye-bye.
**Minghui Zhang** 34:55 Hey.
