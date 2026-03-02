SIG: LLM Semantic Convention WG
Date: 2025-07-22
Duration: 141 minutes
Zoom Recording URL: https://zoom.us/rec/share/BkapmEi7nSA57yCzuXNZx0FBUrrUD8RJZimqm29l9OdTuQXjTmiqJ2maSoifcXnG.3Jt5wfszuplbgqgw
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:06:11 Hi! Everyone.
shiprajain 00:06:15 Hi! Lutmila! Hi! Everyone!
AB Austin Born 00:06:19 Whoa!
Liudmila Molkova 00:06:23 Okay, so let us get started.
Well, do the regular check, and please add your name to the attendees list. That's the first.st
And if you have something to discuss, please add it to the agenda.
I would like to start with our regular quick look at the project. Board.
I hope we, as we discuss the
prompts and completions, we will close most of these issues.
And let's see, we don't have anything new.
We had some progress on this one.
and I wonder if we had a chance to
bring it up until I'm a tree.
Does anybody know if we have
Otios pr up in here now.
Not yet. But I see a bunch of prs.
Sergey Sergeev 00:07:56 Oh, you mean the general tools.
Not yet. We need to move it. We were working on the design document first.st
It it will be a little bit tricky to move, because we will need to do a big rebrace.
Liudmila Molkova 00:08:14 Oh, I see!
Sergey Sergeev 00:08:15 Maybe we will start from the design document and then move to some chunks of or requests.
We will break it down to some smaller pieces.
Liudmila Molkova 00:08:28 Okay.
okay, sounds good. Thank you. I don't tend to spend ton of time on triage, because I don't think a bunch of new things have happened and the things that did.
I put them here?
Okay, I think we should move to the agenda. I would like us to
cover as much as we can on inputs and outputs Pr today, because I believe it's blocking a couple of agentic prs,
I added them here, we should talk about them.
Shipra! And I'm not sure if
did you want to put a
sometime box on this, should we? I don't know. Give it 15 min, or maybe we should tackle them together because they address a similar set of concerns right.
shiprajain 00:09:33 Sure.
Liudmila Molkova 00:09:35 Okay, let's reserve.
20 min for them.
Ratima. What is this one about?
Ridhima Satam 00:09:50 Yeah, that was just for the instrumentation. So I have approvals on that. It's just that. I think Aaron was asking for the name change confirmation. And so from, I received a response from about it that we are okay to move with the same name just we can do the different versions. So I have added a comment about it. So we're just hoping to get it approved
from the end.
Aaron Abbott 00:10:21 Oh, yeah, that's great. I'll I'll take a look at this. Pr.
Ridhima Satam 00:10:24 Okay. Great. Thanks.
Liudmila Molkova 00:10:27 Thanks. So let's do we need to talk more about it, or is it?
It's just announcement that you would like to get an approvals.
Ridhima Satam 00:10:37 Yeah, just a call out.
Liudmila Molkova 00:10:39 Okay, so let's assume we've covered it.
It seems we have 35, 40, maybe 15 min in the buffer, I would imagine.
it would take us
pretty much to the end of the meeting. If you have anything small to discuss, we could probably find time for it. Please add it at the end.
Okay, so let's start with this one.
Elastic is contributing Openai instrumentation for Javascript.
I can review it. But I'm not a Javascript developer.
and I have never used open a Javascript SDK, I really hope we can find people in this community to
take a look at this and hopefully approve.
I also believe that elastic
folks who are donating this instrumentation, they are looking for other people to share component ownership with.
So if your company is going to depend on this instrumentation, I highly recommend 1st reviewing and second, considering
being a maintainer.
The component owner for this project?
Would anybody be interested.
Sergey Sergeev 00:12:29 Yeah. 1st question is,
why should it be a separate trip, or can it be part of open telemetry? Dash? Js.
Liudmila Molkova 00:12:45 It's not. It's not a separate repo. It's part of up on telemetry. Js.
Sergey Sergeev 00:12:49 Never mind sorry I looked into a different place.
Never mind.
Liudmila Molkova 00:12:55 Yes, so they. They have this instrumentation at elastic, and they're donating it to open telemetry.
Sergey Sergeev 00:13:03 Yeah, we should have not js, approver
on our team. I'll ask to look.
Liudmila Molkova 00:13:14 Wonderful.
Sergey Sergeev 00:13:15 Walk through.
Liudmila Molkova 00:13:16 Thank you.
Okay, so let's move on to the 3rd one.
Think we have.
we had a bunch of comments. I tried working through them. There are a couple of
big discussions that I I hope we can resolve in person.
I see Alex here. That's wonderful.
I kinda want to start pushing on this more aggressively, because I see things are depending on it.
and it would be good to have some clarity and finally merge it.
Okay, so let's take a look first.st
Big discussion. Well, maybe not big. Maybe just a naming concern.
But they want to bring a bunch of things together here.
So we use genai system instructions.
I'm totally up for names, but they kinda like
the system because it's a common terminology.
We can also call it system underscore instructions
which would remove the namespacing concern.
Alex, do you have a preference? Any thoughts on this? You raised the concern.
Alex Hall 00:15:22 Yeah, I mean, I don't know exactly what words are best. It just as far as I know it, like General Guideline.
the dots. There was kind of not recommended practice like you mean the dodge.
Liudmila Molkova 00:15:39 Are for spacing. If it's 2 words that are not namespace, that would be system underscore instructions.
Alex Hall 00:15:45 Exactly. I'm just saying my. My original comment was mostly about the dots, and I think that
system underscore instructions sounds fine.
Liudmila Molkova 00:16:02 Cool. This was easy any concerns.
The other part that I think
was raised. Some questions is whether
they are considered sensitive. Let me scroll down.
Think, Samuel, of the comment.
Alex Hall 00:16:27 I think Samuel's not here. But I agree with you guys that the the instructions can contain
sensitive stuff like user dependent content.
Liudmila Molkova 00:16:46 Yeah. And whatever we are deciding on this note, it's just to know the attribute is opt in.
anyway. So it's a 2 way door. We, if we don't provide all the
warnings right away, we still have time to address it.
Alex Hall 00:17:05 Yeah, it's just a note. I don't think you need much discussion.
Liudmila Molkova 00:17:08 Okay.
R,
sorry.
It's still morning for me. I did not learn how to type yet.
Okay.
cool. The last thing I wanted to mention that I've seen
It's becoming common to have a template there and have parameters and some format.
We actually have a means to
recorded, so that the system instructions is of type any. And if we want to have the parameters, I parameterized
type inside it, we could.
The alternative would be to flatten it down and say, system instructions dot prompt system instructions dot parameters.
I don't know if it's a good idea yet
if anybody has a strong thoughts, so strong opinions. Please come forward and let's discuss.
Aaron Abbott 00:18:33 So the system instruction is just a plain. Any right? Now.
Okay.
Liudmila Molkova 00:18:40 Because you folks can have it as an array, for example, or a text.
Aaron Abbott 00:18:48 Yeah, I mean, for so for vertex, at least, it looks the same as or sorry for for Gemini models.
The Api looks the same. As for the content like
that, we're that's in the user or the response.
So I mean,
we could have some structure better than any. But are you saying like to flatten the
the text out into just directly there, and not have keep any of the structure.
Liudmila Molkova 00:19:15 I'm saying that's an alternative. I don't think I want to do this, at least until we have some evidence that it's useful.
Aaron Abbott 00:19:22 Okay.
I mean, I'll double check. But I think I think if you put those other types, it would be invalid. But maybe that's still useful to capture. So if somebody, you know, calls the Llm. With something invalid, they can understand what they did wrong.
Liudmila Molkova 00:19:37 Oh, I see what you mean. I mean not that somebody put something invalid, but that the each
model or now agent framework can decide to have their own types.
and we can go and try to unify those into something.
But I I'm not ready to go there yet. Maybe eventually.
Aaron Abbott 00:20:04 Yeah, I think that's fine. We can.
Maybe we could do like a vendor specific, you know.
like we do for for Openai and for aws, we could do a specific one that has a more specific type. Maybe.
Liudmila Molkova 00:20:24 Okay, so let's start with any. And
maybe revisit this eventually and be more specific
cool. So I think we are pretty much done with the easy part which is instructions.
The more interesting part is, what do we do with the chat history for agent?
I think last time we discussed that the chat history as we represented in this pull request.
It's it should work for all of them.
But it might also work for agents. It can work for agents, but we're would like
to make sure it. It does work for them. It's not this hard requirement, but it would be nice if the same chat history structure would apply to both
right and the difficult part there
is somewhere in the Alex's comments.
Let's see.
right here we go.
Alex Hall 00:22:02 I mean, I think you admit that the question you raise at the very end, which is not really in the discussion, is
probably the most important thing to settle first, st which is, do we even want to record anything on the agent?
It's been.
Liudmila Molkova 00:22:19 My point on this is, it's duplicative, right? If we have an agent and multiple nested alarm calls that we would record all the details and nested spans.
So
The minimum approach would be to record what was the original input to that agent and the final output from all the steps. But
if you look into, let's say, open AI
Api responses or chat completions. It returns a bunch of tool call details inside output response.
And we want to record those.
Alex Hall 00:23:02 But I would hope that those would also be recorded on the lens. Bands.
Liudmila Molkova 00:23:12 No, because you never got this Lm. Spans, because the this calls were made on the server side.
Alex Hall 00:23:22 Again.
If if I don't use an agent framework, if I just use like the Openai responses Api, and it's instrumented nicely.
I still want that to like. I only expect one span, one Llm. Span. I don't expect
2 levels of spans or anything with than anything agency.
Liudmila Molkova 00:23:48 Okay.
Alex Hall 00:23:50 And I think that somewhere in the span attributes there should be something about the tool is called
that could.
Liudmila Molkova 00:24:02 Right.
Alex Hall 00:24:03 Essentially multiple parts in an output message like to call 2 response text.
Liudmila Molkova 00:24:14 Right? So what what we have today is, let's say, when we get an output, push
tool server side tool calls, we record. It's it's currently
one of the 2 response part or
text part. Well, some other content part.
So I think we need to fix this and it can be both.
And then this to call response could be populated along with the content.
shiprajain 00:25:01 So, Lyudmila. In my Pr I have suggested something similar.
where, as part of agentic response, the possibilities is a tool response and an assistant message response. These 2 are the possibilities. And as an input to the agent could be system instructions, user instructions.
Another assistance instructions, or even tool. So
I have elaborated that a little bit more in my Pr.
Liudmila Molkova 00:25:35 Okay, let's take a look on it, says this one.
Do you remember where.
shiprajain 00:25:49 Yes, it will be an agent agent and invoke agent.
Liudmila Molkova 00:25:56 Do you remember? Which attribute.
shiprajain 00:25:59 Gen. AI. No, no, gen AI agent, invocation, input an output
queue.
Liudmila Molkova 00:26:25 Where.
shiprajain 00:26:26 Do. Do you want to go to the spans? Part spans? Yaml.
Liudmila Molkova 00:26:31 Okay, I I would have expected to then be to be on the
that would be definition. But okay.
can you guide me? Or do you wanna present or.
shiprajain 00:26:59 Let me quickly do that. Yeah.
Liudmila Molkova 00:27:04 Your present.
Yes.
shiprajain 00:27:15 Please let me know. Once you can see my screen.
Liudmila Molkova 00:27:21 I can see it now.
shiprajain 00:27:23 Yeah. So it's here. So what we're proposing as part of agent span is attributes few more attributes. 2 of them is agent invocation, input agent invocation output. I'm pretty much open to the naming convention. But the main idea is to be able to clearly capture what
comes in what goes out. And we're proposing to basically have a list of basically role in body where role can be any of these, which means the input to an agent could be a system instruction, user instruction, assistance, message or tool message.
And this is the quick example
of how multiple kind of roles and the content can flow in to an agent. Input.
Similarly, for agent 2 tools are the critical thing to saying, tools go in. The output
tool can also be an input.
And if I come down as under invocation, output here, so
usually, what we have seen is if there is a tool which has which is triggered within agents. Response, then that is folded into final assistance. Response. I can show one quick example of the trace that I had prepared
to validate this thinking.
And I mean, we can even take an opportunity. So yeah.
so if you see agent invocation, input we are talking about system and user that these are the 2 things applicable. And here assistant respond which should ideally fold in the entire response. Now, if you see in this particular span. There were a couple of tools that were triggered.
but at the end the Llm. Comes in, and it it collates all all that went in as input system, user assistant tools and all of it series of things. And then the the final output, which was assistance summary
so as assistant summary.
We are not really differentiating the the tool that got executed.
This information got folded in.
So I can also show you that, as you know, one of the.
So see
when the the last execute tool for search hotels triggered, it basically captured the tool response. But it is more, as in you know, it just keeps on getting stacked as chat history. And hence it is kind of considered as input
the output of.
Alex Hall 00:30:14 Can you show the metadata like? Oh, I don't know. Actually, the metadata shows, but I just want to see it in like Json form, and
in like a raw data format.
shiprajain 00:30:25 Like this is, is that okay?
Alex Hall 00:30:27 It's there.
shiprajain 00:30:30 So if you see the incoming events system message, user message, assistant message
tools, message. So all of these are getting considered and getting tagged as chat history and.
Alex Hall 00:30:47 Pause there for a moment. So
this is the tool message, here means the tool response. And okay, yeah, and and is the idea that these are being called.
No, these are local tools. These are just function tools, right? These are not
like open AI built in tools.
shiprajain 00:31:03 Yeah, I mean, this is the Poc that I was building to prove this particular pr, we have not used like, I mean, I can do that very, very easily, because there is one more effort which is going on where we are. Linking exactly the same thing that you mentioned using responses, AI as tool. So if if that is needed to validate we can, I mean, I can build a Poc and share. How the idea would look
so far from this whole experimentation, we understood that as an input, we may have for this
these categories system user assistant tool. But as an output it is going to be mostly assistance output, because the final Llm. That gets triggered. It kind of collates everything. And the actual output of that span is the Llm. Or assistance response which summarizes everything which has happened so naturally. The tool response is exited out of
that span, and there's a possibility that there's only one tool that got executed. But still, after that there will be an Llm span that gets triggered which captures it and responds. So it is still tagged under assistant type.
Liudmila Molkova 00:32:14 Supre. Can you help me understand? What do you record on the invoke agent, Planner? Because this it's it aligns well with what we have for Llm. Calls right for 2.
shiprajain 00:32:25 Yeah, so this is the one, this is the input.
And here one of the inputs is system, you user
in this particular case, this was actually the input that went in at the start of this pan. And then there are a couple of execution that happened. Multiple tools got triggered, which we are not capturing in the invoke agent input, because that is redundant information. We just want to see what exactly came in when this pan started. And then what was the output which is captured as invocation output, which is the.
Alex Hall 00:33:01 All of this is redundant.
shiprajain 00:33:04 Sorry.
Alex Hall 00:33:05 All of this is redundant in the sense that all of it is duplicates from the. Do you mean that you consider the intermediate messages less important.
shiprajain 00:33:13 I mean, we know. So that that's not how we were looking at it. We felt that
if we consider invoke agent as as a black box. We just want to understand what was the initial instructions of the input.
And what can be those type of instructions that an invoke agent would want would would receive, so it could be of these 4 categories, and when invoke agent output, the final output that comes out of that span invoke agent span. What type of output it would be. It is going to be an assistance output, because eventually an assist. An Llm. Runs, it summarizes, and that's the response. Now.
of course, there are all these intermediate steps which are super important. That's why we are doing this whole exercise of multi agent traceability. But the point was, should we write all that we are seeing in the final Llm. So if you see the final Llm. Captures all of this chat history exactly in the order of how it was called. You know all the tool calls as well tool messages as well. Should we just duplicate this.
which didn't seem correct to us because we can still do it. Code wise. That's not a problem. But is that the right thing to do so when we internally brainstormed, we felt that the right thing would be just to keep what went in, what went out. And if somebody really wants to double click they can look at the intermediate steps and read these intermediate intermediate steps. And and you know,
build the chat history if needed.
Simply, you know, if they just read last Llm. Span. Also, they would get this chat history. So just, you know, taking this and then also projecting it, or outputting it at invoke agent, the whole
history that seemed redundant.
The information is very much available, so one can access it.
So yeah.
Liudmila Molkova 00:35:15 I think there is a.
shiprajain 00:35:16 Thank you.
Liudmila Molkova 00:35:17 Relevant conversation in the chat Alex would, or other people. Would you mind sharing your thoughts and
the duplication and the level of details we capture on the outer
agent, span or framework span.
Alex Hall 00:35:37 Yeah, I I think that the idea of not recording the intermediate
why does it say your middle left.
Aaron Abbott 00:35:47 I think we yeah, I think we lost her.
shiprajain 00:35:57 So, Aaron, you still feel that we should capture the intermediate steps also under output.
Aaron Abbott 00:36:03 Oh!
shiprajain 00:36:04 Invocation!
Aaron Abbott 00:36:05 No, no, I I think what you showed kind of makes sense like. I I like that. It's not duplicating the telemetry. So the Lm. Calls have
all the context on that stuff. If you want to look at it.
I personally prefer that I think
the the kind of thread in the original Pr was
that the input and output aren't really good, like A,
they don't really capture the mental model of how the agent works. And I I still don't completely understand, Alex. I was wondering if that's kind of what I meant by. If you could show
an example or something of what pydantic AI is doing.
shiprajain 00:36:39 Okay, so is that is that a good thing like this example is that helping.
Alex Hall 00:36:47 The example is helping to understand the way you think about it, and I think that the way you think about it is very reasonable.
Come.
I don't know what it should be. I was initially thrown off by a wording redundant, and we also do duplication. It is still duplicating things. It is.
shiprajain 00:37:08 For sure. How much do we duplicate? I think that was the point.
Alex Hall 00:37:11 Yeah. But also I get that. There's a cement
big difference in that. All the intermediate stuff
is is more like a debugging level kind of thing you look in to see what happened.
If we view the agent like a function.
shiprajain 00:37:24 Yeah.
Alex Hall 00:37:25 You gave it these instructions, and it gave you one final result. It makes sense to record just those things on the agent span.
shiprajain 00:37:35 True. And actually, that's a very good point. I'll tell you what we also were internally doing. So
ultimately all of these are child span right, which are also linking to the parent span. So we have basically built a quick SDK internally, which reads such kind of hierarchical spans
and form the child parent relationship and say, if somebody wants to dissect what is going on in this invoke agent span, we basically went deeper, extracting the information of each of the child span and those input and output. So as part of this Pr, I have also suggested changes to execute tool, which is exactly capturing. You know, what is the output to a tool
and an input to a tool. Now, this information we want to retain in execute tool. So suppose somebody wants to really know whether this tool performed right or not. Then, with the help of that code that we are writing, we can basically use child parent relationship and extract the information from each of these pans and analyze them separately.
and with that we will also get the opportunity to go at the last most span, which is Llm. Span, and it would have the entire chat history, and the final response, and hence we can get clarity on
you know, at the White box level we can. We can get clarity on whether whatever output we received made sense or not. So
what we felt we can do is at invoke agent. We can consider it more like a black box where we keep it limited to only exactly what was in given as input, and it could be any of those 4 categories. And what came out.
you know. So as the final assistant output and maybe evaluate that. See whether that looks fine, and if it doesn't, then go deeper, dissect each span, and figure out step by step where it went wrong. So that was the idea that we had, and that's why we concluded that we would not overload the output of invoke agent and just plain keep the assistant output.
Alex Hall 00:39:52 Judmilla, do we actually have to even include anything about
these inputs and outputs on the agent spans in this? Pr, I mean, currently, I don't see anything about recording inputs and outputs of
agents. Could we not, initially like, leave this out and then add it in a follow up.
Liudmila Molkova 00:40:12 Oh, absolutely. My main goal was to make sure.
Our structure that we pick it can work for agents.
I, personally don't believe it would be useful to have Jenny Dot entered. And vacation input along with Jenai dot
input messages, or whatever we call both of them. They should have the same structure, and I want to put as much as possible into the current
definitions so that they are reusable.
shiprajain 00:40:46 Yeah. So let me have my quick. 2 cents over there, I think, from naming convention. I'm very much okay as long as they can standardize and bring those to input messages and output messages as part of invocation span from the structures structure perspective. Also, I didn't see a lot of difference, I think just the name is slightly different. Yours is more aligned with
you know you're saying parts, and I'm calling body so I think the 2 things that I would look forward to is, you know what final name we we suggest.
But then, more importantly, for an invoke agent. The proposal is that whenever an input has to be considered, it could be of these 4 types system, user assistant tool and an output, it can be of assistant type. So that's the main idea. Structuring wise. I didn't see a lot of difference just naming. And I'm very much okay to adopt what goes in your pr.
Liudmila Molkova 00:41:41 Wonderful. And
even in my Pr, we have the question of okay responses Api or chat completion. Api, that invoked some server side tools.
How do we record them? And I'm sorry I didn't notice that Ankit has has his hand raised. Do you want to go ahead, ankit.
Ankit 00:42:02 Yeah, yeah, these computers are limited. I cannot.
Liudmila Molkova 00:42:05 Oh, I wanted to go. Go into the direction of what do we do with the tool output tool? Risk.
Ankit 00:42:12 Oh, I see!
Liudmila Molkova 00:42:13 In the output. So if you want to talk about the previous topic, please go ahead.
Ankit 00:42:18 Oh, yeah, yeah. So I think one thing that comes to my mind when I like. After listening to like what Shipper had shared right? So it sounds like something very similar to how would I represent this? Invoke agent span.
including all its child, span in form of a chat history, right?
Like to kind of understand what happened
within the span like we're capturing. Okay? Assistant made a tool call. What was the tool call result right?
So and sounds like like last Llm
call in the In work agent, span the input of it would kind of give a get us there.
Right.
Liudmila Molkova 00:43:03 Usually.
Ankit 00:43:04 Yeah. However, like, in case
if it just a handoff call, I'm guessing. That would also capture these kind of in like entire chat history
like right now. Yes, here we are making a last ln call right. But in case here the last call would be, say, a handoff agent. Call right.
shiprajain 00:43:27 When you say handoff, it means one agent just handing it over to another agent. And what gets transferred.
Yeah, so that that Pr is gonna follow. We, we are gonna represent that. But in case you have a perspective, please, please share. Okay.
Ankit 00:43:40 Okay, so and like, from the perspective of whether this
like the span, should capture this entire thing of what happened within the invoke agent span. Should that show up as an show as an output?
Like messages or no, I think. Did we? Sorry, make a decision on that.
No, I think.
shiprajain 00:44:05 In. There's no decision. But I think that's that's a discussion which is going on. There are 2 point of views, one you know what we are putting up on the table, that because the whole of that information is anyway, is available in the child spans, especially in the last Llm. Span. It kind of covers the chat history exactly showing the sequence of how the assistant responded. Tools called so on and so forth. So that is available, and somebody wants they can extract from the last Llm.
Hence it is not. it's it. It may be a little duplicate for us to, you know. Take the entire last Llm's chat history and show as output to invoke agents.
Output rather, we show only the final assistant response
which was summarized. And that also is a duplicate. But it is kind of giving a meaningful conclusion on what was in inputted and what is output. So that's 1 perspective that is coming as part of my Pr, and then another perspective is, why not to
Why not so have that transparency at the agent output and have the entire chat history maybe listed.
Ankit 00:45:28 Entire chat history as the agent, invoke agent, output dot messages, attribute right as yes.
shiprajain 00:45:35 Genai agent, dot output messages. Yeah.
Ankit 00:45:39 Got it. Yeah. And I think the only caveat there was that we gonna be duplicating that
that's the only thing that we do.
shiprajain 00:45:45 Correct. Technically, we can do it. If we can do this much, we can do all of that. But whether it is okay to duplicate as much, because these are still sample pocs that we are building where the child and parent hierarchy within an invocation span is not as much what happens when this grows. So that was 1 point of view. But the another thing is we wanted to see how responses Api and chat Api does and how we can trace them. If we use this concept of, you know.
bare minimum input, and bare minimum output to an agent span.
Liudmila Molkova 00:46:18 Yeah, I'd like to call time on this discussion. I think we I think Aaron has something to say, and I would like to return back to the final things on the inputs and outputs. Pr.
Aaron, go ahead.
Aaron Abbott 00:46:35 Yeah, just real quick. I was. Gonna say, like, I feel like when we're talking about history, we're kind of getting more into the agent state conversation than the inputs and outputs.
I feel like, I mean, hopefully, we can use the same format. But there's like
some agents have actual state like structured state. And then there's also like the like, the chat history. So I I think maybe it makes sense. We can capture them on the
like. I think Alex's comment was that sometimes input and output isn't a good distinction. So hopefully for state like things, we could have a separate attribute, but reuse the same definitions.
shiprajain 00:47:08 Yeah. So, Aaron, on that. I am also working on a a quick Poc as part of my initial proposal to come up with an event as part of invoke agent span, which is genai state management. That's what I call right now, and that would that should include all of these things like the the State transfer.
Whenever a a right trigger happens, or any knowledge reference, or any context propagated. So I'll try to build that puzzle as well this one.
Liudmila Molkova 00:47:40 Let's let's let's try to focus on one thing at a time. We will talk about edge and state management.
We. We just have 18 min left, and we didn't even get to the other Pr. On the agent entities. I I would like to have some time for it before before we move on.
I want to come back to what we do on the chat history.
For Llms. I kind of feel we are we are
we? Pretty much can can decide what to do now.
So when we look into, let's say, Open AI responses Api and returns 2 calls and output.
Right? We would record 2 output messages or 2 plus one would be the chat message.
That's that has a tool call part
the tool call part, the 2 call response part and the output, the actual content output.
So maybe what I can do, I can include an example that shows it.
and we can review this example and see if we are happy with it.
But given that, it's returned as a part of output, I kind of feel that this it should be recorded on output. It would be very weird to move it from the output
wire thing over the wire thing to the input in telemetry.
Alex Hall 00:49:25 Are we talking about the agent or the Lm. Span, or both?
Liudmila Molkova 00:49:27 Let's talk about Llms. For to simplify the problem, at least, for now.
Alex Hall 00:49:32 For the Llm. Span. Anything that gets returned by the Api is output.
Liudmila Molkova 00:49:39 Right, and it's even returned as a part of output payload.
Alex Hall 00:49:43 And we're talking about built in tools, anyway, right?
Liudmila Molkova 00:49:46 Yeah.
Alex Hall 00:49:48 I think this is easily output.
for I don't know if if it would be multiple messages, it doesn't really seem like it should be.
Liudmila Molkova 00:50:00 It would be multiple parts, right?
Alex Hall 00:50:02 Yeah.
Liudmila Molkova 00:50:06 And then the input output distinction makes sense there.
And we can talk about whether it makes sense for the agents or we will need to massage it a bit more.
and it shouldn't be a blocker to this Pr. Based on the discussion we just had. Would it be.
Alex Hall 00:50:29 Right, John, like I'm thinking, more and more. We should put off the agents part.
But I don't think that built-in tools should really be an issue for Llm. Spans.
Liudmila Molkova 00:50:42 Right.
Aaron Abbott 00:50:44 Yeah, I agree.
Liudmila Molkova 00:51:18 Okay? So I think we briefly touched upon shipra's work on the tools
I want to be cognizant of time. And but essentially
folks from Cisco and Microsoft. Do you want to talk about any disagreements you have? Why do we pursue to different prs?
What can we do to not have 2 different prs.
Pavan 00:51:52 I think, the different Pr was just so that you know, the entity discussion was a bit of a tangent to what was already proposed, so I didn't want to necessarily pollute the existing Pr with some of the similar thoughts. But you know, like the idea that we had was a bit different, so I didn't know how exactly to
like sort of convey that in the pl that Shipra had raised. So I was, you know, and we were sort of going you know, like back and forth, and sort of pretty much converging on the same idea but the feedback that we received
from Sergey and others where to like. Sort of open this Pr and see you know how that goes, and bring it to the table in some sense. So our yeah, our goal was pretty much the same. With respect to, you know, figuring out how exactly we can. Let's say, you know.
ensure that within a particular agent, or with the invoke agent sort of operation, you know, that goes through
the agent could obviously have so many different internal steps which could be like a task. It could be a tool, it could be making a rag step. It could also be, you know, doing an Llm. Call. We don't necessarily want to focus on Llm. Call, because that is already pretty well defined, but we generally wanted to generalize like what sort of an operation that the agent itself will do when it sort of
it gets invoked in some sense. So the fact is that currently none of the like. So if you take a rag example, right? And if you basically give you know, like a sentence. There could be multiple different sub steps, like, you know, like a sentence splitter, or, you know, like another, you know, like which does the like m, you know.
what do you call the
yeah, like multiple steps something that doesn't come to my mind at this moment. But the fact is that a lot of the different spans the input and output that goes to it like for the internal tasks aren't necessarily captured in the right manner. So we wanted to sort of take
that idea and say that, okay for any invoke agent, you know, like trace, there could be multiple spans, and each span that gets executed could either be a a tool. In this sense it could be a internal task that the agent will perform or you know, it could be like a workflow. Because, you know, like a lot of the agent themselves are like long running, short running workflow that
tries to like, you know, sort of capture, you know, like end to end operation in some sense. So the entity output also sorry outcome is also probably not very well defined. If
it. If the status code is 200, doesn't necessarily mean that the task was a success or a failure. So we wanted to like, generalize that a little better. Hence our
idea of adding these to the invoke agent span, and you know, our initial thought was to like, sort of simplify the querying, you know, for it, because you can actually filter by the entity type and get consistent name, input, output and outcome, regardless of.
you know the different operations. It could be future, you know, extensible as well, like new entity types could be added, but the instrumentation can basically use the same attribute pattern for any entity in the chain. Hence, you know, we sort of
came up with this pr, but I think I we did get like a few comments in that Pr, which was like, you know. Very, very good questions. And happy to, you know. Answer more if needed as well.
Oh.
Liudmila Molkova 00:56:10 Yeah. So a few thoughts on this. So there is some intersection. Right? I get that. There are some additive changes that are that are adding value. So, for example, the some sort of status
I would not put it into agent entity namespace. I think it's just something more generic.
Maybe, in the Gen. AI space.
It's it's a pure additive change, the chat history or the input output. I think we need to unify those. We should have a very strong reason not to unify.
Pavan 00:56:51 Yeah, completely agreed on that.
and think we'll sort of make if we are making, you know, efforts to unify on that again. No real sort of yeah.
sort of specific. Yeah, on this particular naming convention itself, but happy to bring that, you know, sort of together in a single proposal, if needed.
Liudmila Molkova 00:57:30 Is there a specific framework that you're targeting with this.
Pavan 00:57:36 So in some of our
yeah pocs, what we have done is we have actually defined, or rather are working, on a SDK, that is actually open source that uses like multiple instrumentation. Sdks.
currently. I think we can also link that trace as well if if needed. But in general we do make use of, like some of the trace loop instrumentation sdks that they have defined for like land chain for llama Index and couple of others, and we try to unify all of that in the like sort of abstraction. SDK, that we are building
and I think, in that some of the existing attributes that we are proposing are like, sort of
being emitted without the user even needing to do any manual coding in that sense. So a lot of a lot of it is like pretty straightforward from the like decorators approach that we have. But if if that can easily be generalized to the instrumentation sdks, as well. You know. If needed through through the
yeah.
yeah. So what kind of approach.
Liudmila Molkova 00:59:05 So I feel like one of the
things that I would suggest immediately that we
should try to unify this, and it should not be
like we should have one pr, that adds those things.
So maybe we can focus on merging inputs and outputs for Llms first, st
and then we can decide what additions are necessary for the agent.
Hopeful additions, or changes, if it needs to be
and then the other things I I feel like I would like to see some code, the prototypes, or
maybe a demo that shows how useful these are.
Pavan 00:59:58 Yeah, sure. Sure, I can do that during our next meeting.
shiprajain 01:00:03 So one quick question. So I have a the the code. Pr which is the poc that I did before I propose the Pr. For changes here.
so should I just add it to the document.
Liudmila Molkova 01:00:20 So if you see, this is the the template pr template that we have.
and we recently changed it. We recently added it, so you can just add it to the Pr. Description.
That would be super useful to have it.
shiprajain 01:00:37 Okay, prototypes as in. We just need to attach the link to our Prs right? Not not really a demo recorded Demo, or something.
Liudmila Molkova 01:00:46 Yeah, just the pr, that shows the instrumentation prototype that emits those.
There is no process for the demo. It's just something useful for us here to
actually understand what's being proposed.
shiprajain 01:01:00 Awesome. Sure, I'll do that. Yeah.
Pavan 01:01:07 So I wanted to basically ask a general question, so if let's say you know, in order for any new spans or metrics to be, let's say, accepted into the semantic conventions
is the like sort of comp like the implementation complexity taken into consideration, like, you know, is it generally that? If there is a lot of work in order to
expose that particular field under the hood, either by the developer manually, you know, like setting these values? Or is the idea that the instrumentation SDK should bear most of the burden, and the developer doesn't necessarily need to worry about setting any of these fields, and like so if some of if some of the sdks don't necessarily follow that approach.
how would that sort of you know? Yeah, let's say, be useful in some sense, because we do see that a lot of the existing sdks, not talking about open telemetry, python contribut. But outside of that. They have some
like semantic convention. You know. Spans correctly. Everything. But some of the others. Aren't that great? So we just wanted to see like the effort from the developer versus the instrumentation. SDK, that handles all of this. And is there a need
for that to be like super simple.
Not sure.
Liudmila Molkova 01:02:49 So there go.
Yeah. The goal for open telemetry. It's not always possible. But to
capture things in the instrumentation. So users wouldn't need to write code or any
code that follows semantic conventions. We generally don't expect it would be nice, but we don't expect end users to follow semantic conventions.
Some will do most will won't
so I usually push back on any change that is not
possible to be on any attribute or signal that cannot be captured by auto instrumentation.
There are caveats, right? So, for example, function execution. If you're doing Llm call, maybe there is nothing that can try trace it automatically right. But if you do some framework or just your your client SDK has a nice api that automates to calling, we would recommend to capture to call there right?
So as little code instrumentation. So as little code application developer needs to write the better.
I'm not sure I answered all of your questions, but let me know.
Pavan 01:04:13 Yeah, no, it it did. Thanks.
Sergey Sergeev 01:04:18 We have 1 min left. Maybe we can quickly jump on this design, Doc, just to give highlights
in the.
Liudmila Molkova 01:04:31 Yeah.
Here, okay.
Sergey Sergeev 01:04:36 It's for offline reviewing. But overall, it just talks about the design of Gen. AI retails. Thank you, Alex, for suggesting the name. I thank you.
The proposed name, and just high level, very short with some appendixes about
different gen. A types and evaluation types which is outside of the scope of this document just for reference
to outline the thinking in the future.
and please review and provide feedback in the document. We don't have time for it.
they will be happier to answer in slack or hop on
ad hoc meetings if needed, and tradema too.
Aaron Abbott 01:05:31 That looks great. I'll take a look.
Liudmila Molkova 01:05:34 Thank you for putting it up. And would you mind dropping going on the slack channel? So people who didn't join this call would also know about it. That's wonderful.
Thank you. So we are at time. Thanks a lot everyone and see you next week.
Aaron Abbott 01:05:54 Awesome. Thank you.
Liudmila Molkova 01:05:56 Thank you.
shiprajain 01:05:56 Thank you. Everyone.
