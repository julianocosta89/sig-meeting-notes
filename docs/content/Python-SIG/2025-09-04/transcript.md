SIG: Python SIG
Date: 2025-09-04
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/q2dyS0USWbZzOsQ_i_khrjWQWi1_puVkXf_-kQKTNrp-4pjI-QdmfBQM0jKYpkaN.Fbk3MNl-xQgk5z9V
============================================================

## Zoom Recording Transcript

**John Scancella** 10:27 Hello!
**Pablo Collins** 10:30 Anybody know if we have any, maintainers, that are gonna be Attending today?
There's nothing on the agenda… oh, there's alert, okay.
Hey, Aaron.
**Aaron Abbott** 10:48 Oh, hey, sorry I'm late. Looks like we haven't gotten started yet.
No? Okay. So, looks like the agenda is empty.
Do you folks have anything to discuss?
No.
**Pablo Collins** 11:19 Looks like Redima's got something cooking here.
**Aaron Abbott** 11:23 Okay, great.
Yeah, in the meantime, folks, can you please add your names to the attendees list? And yeah, if anybody has any additional topics, you know, don't be shy, feel free to add them to the list here.
Alright, oops.
-Oh.
Oops.
Right, there we go.
Radima, do you wanna…
take over, or I can… I can share my screen if you want to just talk through this.
**Ridhima Satam** 12:24 Yes, you can share.
I'm not going to go through the PR. I see that you have some comments over there, and take a look at that as well. Here, I'm going to talk about the action items we have on us since our last conversation.
And I have added some points on it, I have some questions, and I want to see if we are on the right path, what we discussed last time. So the first, if you see, so this is about, the LLM invocation.
Instrumentation in the line chain.
And earlier supported just the OpenAI,
the chat open AI in that. So, the first two points in here is explain value of the LLM invocation in Langchain versus the client instrumentation, and the second is adding
unit test showing both OpenAI and Bedrock. So for the both of the points, I think we have… we are adding the AWS Bedrock, support as well in this PR.
And just to show the value of it is, like, because right now we don't have the AWS Bedrock instrumentation separately, we will be covering in the instrumentation, you know, in the Langchin instrumentation itself.
So, that is what I have covered there.
And then the next two points is about, finding out how Traceloop is handling the duplicate, spans and our long-term strategy to avoid a telemetry duplication. So if you go below in the second page, for the Traceloop, what I have… the findings I have is.
TraceLoop, I see that you have to just install this TraceLoop SDK, so now TraceLoop has both
Langchain instrumentation and OpenAI instrumentation in place. So you just add this library, and then you initiate in a traceloop.init. So the first piece of code is, like, actually sending it to the backend of Traceloop, and there I saw there was just one span.
Which actually showed me a span of a langchain instrumentation. It was not the open-air instrumentation span, because it had the vendor lanchain, all those details. Second, what I tried was, adding the telemetry, moving it to just the local collector, where I actually saw the span. If, I thought, like, maybe backend is handling the multiple spans, but when I saw it on the local collector.
which was collecting the telemetry, I could see only one span that was Langchain. So, what I deducted from that is, maybe it's in the instrumentation side, where Tracelope Open Elementary is handling,
handling, the… the… how to pick the one, the one over other, the span is… is what I… I think.
So, that's one thing. And then, with the Python contrib, right, when I was, so the second point here, right?
So, in the zero code, unless you actually… the user installs, like, the pip install OpenAI V2,
you will see only one span, that will be a flank chain. If you install it, then you'll see two spans. Also, in the second, or manual instrumentation, you have to explicitly add this, telemetry, like, instrument. So, my point is.
Here in the… in the Python contrib, user is adding intentionally
or loading intentionally the OpenAI v2, so is… is there a concern still, and maybe I missed a point last time, why we are thinking about that? I mean, this could be, like, a user-side issue, like, they have to handle on the backend, or it's intentional.
So that is my point, in the second one.
**Aaron Abbott** 16:05 Yeah. I just… Yeah, well, on the second one, if I could jump in, it's just, like.
the thing is, Langchain is like an agent framework, and we have these agent invocation spans, right? So, I feel if they have to choose between either OpenAI and Langchain, and they can't have both, then there's no way that they could have the agent invocation and the inference spans without duplication, right?
**Ridhima Satam** 16:29 Yes, but they are choosing… the user is choosing to do that, right? I mean, they want both of the spans, that's why they are installing both, like, they have langchain as well, and then they have OpenAIV2 as well.
**Aaron Abbott** 16:43 Okay. But, like, unless…
**Ridhima Satam** 16:46 So, sorry, I mean, unless they install it, you will see only one, the Langchain one.
Unless they install the OpenAI, They will just see the line chain span.
**Aaron Abbott** 16:58 No, I understand. So you're basically saying that the lane chain
instrumentation conflicts with the OpenAI instrumentation, is that right?
**Ridhima Satam** 17:08 I mean, there was a point brought up last time, right? There would be a duplicate telemetry if, if there are… both instrumentations are in place.
Right? If there is a langchain instrumentation,
And then there's OpenAI, so we will get two spans, showing mostly common data, or common attributes, right?
**Aaron Abbott** 17:29 Yep.
**Ridhima Satam** 17:30 And then that would maybe interfere with usage, or tokens, or count of that. But,
But langchain would additionally have a framework, like what we also spoke about briefly last time, like, we will be adding genaiframework.langchain. I mean, sorry, genai framework, which could be langchain. So, that could be a differentiation factor of the span, but here what I'm saying is.
a user is intentionally doing it, right? So, as a… as a… as a…
as we are supporting the Langchen instrumentation, should we even think about the strategy? Like, if you see the action items in that, that we have to think about the strategy to avoid duplicate telemetry. So, is this responsibility on us?
**Aaron Abbott** 18:16 Yeah, I understand.
I mean, my feeling is, first of all, the OpenAI one is a bit more detailed.
it also, like, there's use cases where people still use the OpenAI client without LaneChain, so I've seen that, for example, with, like, if they use LaneGraph and they want to have sub-agents, which are written in a different framework, which uses the OpenAI client library directly, right? So, like, I feel like this works as a short-term thing, it's a little bit fragile because
the user has to be really careful about the dependencies they install, but also, I just don't… I don't love the idea of having two of our contribut instrumentations almost be, like, conflicting, or…
the user have to do this. So, I'm only saying that in the context that I think there's a relatively easy way to work around this, and that's if you do…
You know, if we can work on setting a context key.
to say, hey, this spend has already been captured, and then have kind of, like, a cooperation between the two frameworks. It's not great, because then still the… if OpenAI is going to be emitting more detailed information, and LinkChain's already emitted stuff, to avoid the duplication, it would kind of suppress the OpenAI one, right? So, I mean.
That's… that's kind of my… my feeling on this, but I… I still…
Like, it seems wrong for these to have to conflict, or for the user to have to deduplicate these, right?
**Ridhima Satam** 19:37 Okay, so, do we want to discuss more on this, maybe in the next meeting where we have more attendance? Because there were a couple of other people who were also adding to this point, and I want to get an idea how important is this in the first PR to even,
take an effort to think about this right now. Does it… I mean, is it required for the first VR?
**Aaron Abbott** 20:05 I mean, I can only speak for myself there, I guess. I know there's a lot of other reviews on here from,
Like, from, ricardo, for example, I think…
I don't want to say that it's blocking, and I know this is mostly, like, a translation of the OpenLometry one, so for me, I don't…
I don't think it's super blocking, but I still don't completely understand the value. I think maybe we can,
maybe we can move this discussion to the PR directly, like, we can have,
Kind of record of what other people think, and we can…
**Ridhima Satam** 20:46 Okay.
**Aaron Abbott** 20:47 decision there.
**Ridhima Satam** 20:48 add this to the Slack as well, and, like, a couple of people who are interested in this, so if they want to have any comments on this, I'll just add this document as well there, so I can get their view as well.
**Aaron Abbott** 21:01 Okay, if I could ask one other question, it was, like, the…
The current PR… here, let me just share it.
So currently, this PR doesn't handle any of the prompt response capturing, it just emits the span of the labels, is that right?
**Ridhima Satam** 21:23 Sorry, Kai, can you say it again?
**Aaron Abbott** 21:25 Yeah, so this, this pull request, like, it doesn't, it doesn't actually include the completion details, it just has the SPAN attributes, right?
**Ridhima Satam** 21:33 Yeah, you're right.
**Aaron Abbott** 21:35 Okay.
I mean, that seems…
That seems pretty reasonable to me, because, you know, the amount of duplicated data is pretty low, so…
But maybe, like.
It would be… it would be useful if we had, kind of, like, a couple of issues, or even, like, a root issue with, like, a checklist in it to explain what, the scope that you're planning to implement here.
Is kind of, like, what the end state, and also so we could link issues to the pull requests in the series.
**Ridhima Satam** 22:06 Okay, okay, I'll do that.
Yeah.
And I think there is one more point, if you're done with your questions, but there is one other point in that document.
Oh…
**Aaron Abbott** 22:20 What was it, sorry.
**Ridhima Satam** 22:23 Yeah, the last point, or the action item, about adding more LLM testing and models, that point, and it's kind of work in progress, but I also want to understand, like.
again, I can put this on channel, but do we have to even do this in the first PR? Like, we can…
We can build it up, like,
Right? Right now, like I said, I have supported AWS and OpenAI, but if there are other models, we can just first do the first PR and then build it on top of that.
**Aaron Abbott** 22:58 Yeah, that makes sense. I mean, I think the main ask was just to make sure that it doesn't crash, so have some kind of test, like.
For example, if there was an unknown
Chat provider, like, you could inject Some fake, right?
Just to make sure that the instrumentation doesn't…
try to find model ID, not find it, and crash.
**Ridhima Satam** 23:20 Okay, so, okay, that test… that sounds reasonable.
**Aaron Abbott** 23:24 Yep.
Yep.
**Ridhima Satam** 23:26 Yeah, that's all the questions. I'll take a look at your comments, and then I'll just publish it and let you know that if we are ready for the review again.
**Aaron Abbott** 23:35 Okay.
**Ridhima Satam** 23:36 So I'll be taking a look at that.
**Aaron Abbott** 23:39 Alright.
Any other thoughts on that?
**Pablo Collins** 23:47 Maybe this is throwing a monkey wrench into the conversation, but…
I was wondering, it might be… well, something that I would like to do is, in the next couple of days, investigate whether or not it's possible to, instead of instrumenting a particular provider's chat wrapper.
Just instrument somehow, the bass class, or all of them all at once.
Yeah, I just wanted to mention that, as a significant possibility.
**Aaron Abbott** 24:22 Yeah, I mean, were you hoping to do that, like, before?
merging this PR.
**Pablo Collins** 24:28 Yeah, yes, yeah, as a… Yeah, I will do that.
**Aaron Abbott** 24:33 Okay, cool. Yeah, that sounds good. I also noticed there's, like, this linkchain 1.0, release candidate.
And this maybe is more for the follow-up, where we have,
Let me see if I can find it.
This is maybe more for the follow-up when we actually do the prompt response capturing, but they've…
Oh, this is JavaScript, hold on.
They added this thing called content blocks,
Share this in the meeting notes.
And basically, my understanding of this thing is that the… When you use the,
Sorry, the LinkedIn org. Okay, here we go.
So, if you call, like.content blocks on the messages, it will parse the content into a standardized type-safe representation, so it kind of solves
some of the problem with the model providers having different formats, so the example here is, like, if you have Anthropic and OpenAI and
One of them uses thinking, one of them uses reasoning.
If you call .contentBlocks, it will be parsed into this reasoning content block type.
That link didn't work. So, obviously, I think this is only available in this kind of release candidate alpha thing, but if we can, you know, focus on just newer versions and don't need to support older versions, this would probably alleviate a lot of that pain.
Okay.
Great, keith, do you wanna go your run?
**Keith Decker** 26:27 Yeah, just bringing up the Gen AI utils as our initial PR for this, looking to start getting some feedback on it before we…
That's further down the pipe, so…
**Aaron Abbott** 26:36 Just wanna bring it up.
Court, do you want to…
Talk to it a little more, like.
**Keith Decker** 26:47 So, the initial PR, it's kind of big at 1200, but a lot of that is just structure.
But we are bringing in handler and generators in order to generate some standard SumConf stuff around LLM invocations. We have
Spans, metrics, and events so far?
**Aaron Abbott** 27:10 Hi. Awesome, good.
Yeah, I was gonna… Dylan, are you around? I think,
You were working on something pretty similar, or at least you had some boilerplate?
**Dylan Russell** 27:23 Yeah.
**Aaron Abbott** 27:26 Stuff right now.
**Dylan Russell** 27:27 Can you hear me?
Nice.
Yeah, I think… I mean, I haven't looked at this yet, it looks like the types that you're adding are kind of similar to the types I was adding.
In my PR.
**Aaron Abbott** 27:48 This one, right?
**Dylan Russell** 27:50 Yeah.
**Keith Decker** 27:51 To, to merge those two together, kind of thing.
**Dylan Russell** 27:56 Yeah, definitely…
**Keith Decker** 27:58 We don't have as many in ours, because I was focusing mostly on… Just the inference type.
**Aaron Abbott** 28:05 God.
**Dylan Russell** 28:05 Sure.
Yeah, let me know if you see anything in mine that… I guess…
conflicts with yours, or if you just think it looks good, then… Can probably just merge mine.
**Keith Decker** 28:20 Okay.
**Aaron Abbott** 28:22 Yeah.
This is great that everybody's working on the same thing. We definitely want to deduplicate, like, the effort,
So yeah, I think, like, I noticed…
this is a bit different between the two of them, so… I think, Dylan, we were kind of relying on the…
data classes, to dict, or as dict, or whatever function, so… Do you…
**Dylan Russell** 28:49 Yeah.
**Aaron Abbott** 28:50 Was this one, Keith, was this one something that didn't work with the built-in data classes serialization?
**Keith Decker** 28:56 It didn't match the JSON structure that's laid out in that link.
So this was just a 2JSON.
Kind of bridge for me.
I'm happy to explore a different…
Durham method if we need to.
**Aaron Abbott** 29:13 Funny.
Yeah, I mean, based on, like, this, it looks like it's making some assumptions, like, the content
Like, this is a flatter representation.
Assuming that there's only one part, which I think, at least… at least for, like, Gemini, I can say that that's not always the case.
So yeah, I… maybe… if…
Yeah, if you two could get together and work it out, I can also take a review pass at this, but…
Does that make sense?
**Keith Decker** 29:51 Yeah, makes sense.
**Aaron Abbott** 29:52 Dylan, I'll look at yours, and then maybe we can take conversation into the Slack.
**Dylan Russell** 29:58 Okay. Sounds good.
**Aaron Abbott** 30:03 Okay.
Was there anything else you wanted to mention on here, Keith? I guess I should just read the description.
**Keith Decker** 30:09 No, like I said, I just wanted to initialize and start getting more feedback that, you know, for stuff we didn't necessarily think of.
**Aaron Abbott** 30:17 Okay.
Great. This is awesome.
Alright, that's the end of the agenda.
Does anybody else, have any topics, or should we call it there a little bit early?
**Jackson Weber** 30:34 Yeah, I just wanted to call a quick attention to a link I dropped in the chat. I had some initial engagement on this PR, but yeah, like I said, just really intended to get some further eyes on it, some implementation of the synthetic source, semantic conventions. This has been implemented in the JS
repo already, so I'm just bringing it over, to Python.
**Aaron Abbott** 30:59 Cool. Sorry, you'll have to forgive me, I don't… I'm not too familiar with Synthetic source, could you.
**Jackson Weber** 31:07 Yeah, sure.
So this is a function to be able to allow
telemetry to be marked as created by a synthetic source. So, if you have something like, some bot
That goes and, you know, accesses a website, creates, synthetic traffic. This allows us to mark, using a semantic attribute, that telemetry as synthetic.
That way it can be filtered on whatever, backend the customer's using to,
**Dylan Russell** 31:38 Filter out or filter in.
**Jackson Weber** 31:40 Certain synthetic telemetry.
**Aaron Abbott** 31:44 I see, so this is, like, for synthetic monitoring use cases.
**Jackson Weber** 31:47 Exactly, yep.
**Aaron Abbott** 31:49 And, is this… so is this already in the cemente Conventions, or is this just another prototype to move that along?
**Jackson Weber** 31:55 So, it is in the semantic conventions, it is experimental at the moment.
**Aaron Abbott** 31:59 Okay.
Cool. So this is just a call for more reviews, basically.
**Jackson Weber** 32:05 Yeah, exactly. I had some initial reviews, From… let's see…
From Ricardo, which I did address, I…
Haven't gotten follow-ups on those, it's been in about a week.
**Aaron Abbott** 32:19 So I just wanted to, call attention.
Yeah, Ricardo's not here today, I don't know if he's,
out of office, or maybe I missed a message on Slack.
He's usually pretty, pretty good at getting back to stuff,
Yeah, in the meantime, if if you want to drop, like, a…
comment in Slack, it's usually a good way to get more eyes on stuff, too.
**Jackson Weber** 32:43 Sure, yep.
**Aaron Abbott** 32:46 Alright.
Anything else on this one?
**Jackson Weber** 32:51 So for me…
**Dylan Russell** 32:54 Cool.
**Aaron Abbott** 33:01 Alright, so, on our last call, anybody have any topics, or we can end it a little early?
All right. Cool. Well, thanks, everyone. See you all next week, and this is a pretty light agenda for a change, which is nice. Thanks for joining.
**Jackson Weber** 33:23 Yep.
**Pablo Collins** 33:23 Bye-bye.
**Dylan Russell** 33:24 Bye.
**Hector Hernandez** 33:25 care.
**John Scancella** 33:27 Thank you.
