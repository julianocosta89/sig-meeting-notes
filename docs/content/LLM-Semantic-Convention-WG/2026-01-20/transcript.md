SIG: LLM Semantic Convention WG
Date: 2026-01-20
Duration: 112 minutes
Zoom Recording URL: https://zoom.us/rec/share/BDO23iYmVb1V21zA2K6DLPn5-aEPdAQl16D_WI9z7PfLQHjhTKUdtJU_ICXruc2V.0xs7U9yM3HEXWdZ5
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 03:00 Everyone, they're gone.
**Keith Decker** 03:13 What's going on? How are you doing? How's your weekend?
**Aaron Abbott** 03:17 Yeah, pretty good, can't complain. I had a long weekend.
Okay, I don't know if Glutenola's gonna join, I actually kind of…
And she might, but we can get started.
Anyway…
Cool, yeah, please add any items to, like, the agenda, or we can do the,
The kind of structured part of the meeting, so the triage, and then…
Looks like we've got some new people today, so we'll leave a little time for intros.
Can… I'm sharing, right?
Yeah, okay.
Cool.
New issues…
I'm not sure, Alex, if you're around and want to talk to this one. I don't think so.
It looks like this is from…
February? I'm not sure why this is in the new issues. Invocation specifically, change usage… Okay,
It sounds like this is kind of, like, just a bug in our conventions.
But not actually a new issue, so…
That looks like the only one we had. Okay, cool.
It's easy, alright, does anybody want to say hi? Anybody new to the SIG? Totally optional, but
If you're around and want to introduce yourself, feel free to.
**Jeff** 05:52 Sure, I can, okay, can you hear me?
**Aaron Abbott** 05:56 Hey, Jeff.
**Jeff** 05:57 Okay, hi, yeah, nice to meet you all. I'm, Jeff from, Google. I, worked with, Aaron briefly, at Google before, and, yeah, just joined this meeting.
Yeah, see whatever… see what other people are talking about, about the, OpenTelements many conventions, because I personally am super interested in, into this domain. So, yeah, nice to meet everyone here.
**Neil** 06:24 Yeah, boom.
**John McBride** 06:25 Cool, I can go.
Yeah, go ahead, Neil.
**Neil** 06:28 No, no, please.
**John McBride** 06:30 Sure. John McBride, I'm coming from a new company I'm starting, actually, called the Paper Compute Company, and we're exploring agentic telemetry, so I'm mostly trying to figure out the landscape, and I know that this is a great working group talking through OpenTelemetry for
Agents, so… fly on the wall.
**Aaron Abbott** 06:52 Cool, nice to meet you.
**Neil** 06:55 Anyone else?
Hi. I guess, kind of similar, my name is Neil Ishinsky. I am working on a new project called Context Core. I am of, recently, of Grafana Labs, where I did a lot of…
AI development around, starting with dashboards, and it kind of,
Through this process, I realized kind of two problems, that I might be looking to solve.
One is that, it can be really hard to maintain, like, what you're working on with the agents, you know, what was fixed, what other agents did, etc, and markdown files don't really leave a lot to… or leave a lot to be desired, pardon me.
And also, this kind of, realization, if you will, that we have all the data structures we need in time series-based databases to do project management without
having a whole other tool, really. And so Context Core is kind of… was conceived to be a single, metadata language that you could use from, you know, project initiation or design development through deployment.
and operation, and even, optimization. In theory, it's out of scope now. But like I said, I think for this group, it would be interesting to hear if there's relevance or ways I can contribute, because Context Core also uses
OpenTelemetry as a model to…
You know, do project management, which means both agents and people can use the same data, and we get kind of the benefit of query languages, et cetera, in order to…
you know, it's very efficient. You don't have to worry about, you know, blowing up your contact size, for example, with, you know, if you've got a lot of information that you want to use as part of your prompts. And this way, both, kind of, the context and…
The capabilities are more discoverable
With your, you know, with my… with your… with your infrastructure, with your environments, because keeping agents up to date about what's available, too, became a problem. And so, like I said, context core.
uses telemetry, you know, open telemetry-based data modeling or whatever to create machine-readable and human-readable versions of the same project management data, among other things.
So, it's nice to meet with you.
Happy to chat more about anything you want, or, you know, I'm eager to, like, if there are good things for, you know, new level contributors to, you know, work on, by all means, let me know. Happy to jump in. I can help.
Thanks.
**Aaron Abbott** 09:46 Cool.
Nice to meet you.
Anybody else?
**Jamie Danielson** 09:51 Yeah, sure, hi. I'm Jamie, I know a couple people here. I work at Honeycomb. I've been working in OpenTelemetry for about 4 or 4 and a half years, maintainer in JavaScript, and
at Honeycomb, we're, you know, doing a lot of things with AI and LLM observability, and so just want to kind of be involved and make sure to help move things forward and keep a pulse on what's going on.
That's me.
**Sujay Solomon** 10:15 I'll go, since there's lots of new folks. So, hi everyone, I'm Sujay, I've been, participating in this SIG for about a year now. I work at Google Cloud on observability of AI, kind of cross-cutting across things like Gemini Enterprise, Vertex, ADK, and so on.
I actually have a question, like, on… I see on the doc that there's, like, an AI Agents track now. Can somebody share what that's about?
**Liudmila Molkova** 10:47 Is there a gate here?
**Aaron Abbott** 10:50 I don't think so.
**Liudmila Molkova** 10:52 Yeah, so, does anybody want to participate, so want to talk about it more?
**Sujay Solomon** 10:59 No, I'm just curious about, like, what the… it looks like we have a separate series of meetings on Mondays on, like, the AI agents track. Like, how is that different from this one?
**Liudmila Molkova** 11:09 Yeah, so how it started. There were different groups of people who were interested in, like, the… yet another layer for the agents.
workflows, the… what… what else was there? The orchestration. And, we didn't have enough time in this call, and there were some groups from Cisco, from Microsoft, and we… they started meeting at a certain time.
Then we made it official. I haven't been there. They should have meeting notes in the same call as this one. And essentially, this is a sub-working group where people discuss, like, complicated
scenarios around DEGINS, and the hope is that they come up with the consensus, some proposals there, and then we discuss them here in this group after they are formed.
It's… In the hotel calendar.
And I… we can't go through the notes, but I think it's been quiet for a bit.
**Sujay Solomon** 12:17 Okay. Okay, thank you.
**Liudmila Molkova** 12:23 So, I see some notes, there is a discussion on guardrails, there is some draft pull request, but I think it's not… it's in the draft.
And I don't believe there is a consensus there.
**Sujay Solomon** 12:41 Yeah, maybe… I don't know if we've updated, like, our GitHub READMEs and stuff on different tracks. If we're introducing, sort of, like, different tracks within this SIG, we should probably just educate people on
Like, topics that we're tackling in different tracks.
**Aaron Abbott** 13:02 I did actually just update the, like, the Gen AI…
I can share a link here for… because there's so many new people today, but the, like, the times and stuff, I think it mentions…
But yeah, I agree, like, there's not a lot of info on what the tracks mean, just has kind of the meeting times.
Yeah.
We could… we could do a few more intros, like, there's a lot of new people today, more than usual, so I, I think, Alex, if you want to go.
Otherwise, it's fine, Dory.
**Alex Boten** 13:35 Yeah, I mean, I kind of just did mine in the chat. I've been around with help for a while. Hi, I'm Alex. I'm just here to listen to what's happening with SEMConf in the land of…
AI and LLM, and happy to help.
**Aaron Abbott** 13:55 Cool.
Well, it's good to see a lot of new faces and familiar faces, so…
Alright, should we get into the agenda?
Alright.
Yep, Unkit, europe, do you want to share your screen, or just talk through this?
**anksing** 14:17 Sure. Let me… again… Oh yeah, actually, since you've already opened it, so if you can…
Now we get to this, comment that I added.
System… Yeah.
just a bit deeper.
Oh, sorry, go on.
**Aaron Abbott** 14:39 Oh, yeah, yeah.
**anksing** 14:41 I think it's called Passive, that's fine.
Okay, there we go. Yeah.
So, okay. So, just a quick intro, like, why this PR is for, and why I started on this. So, I was looking into, like, adding tracing for open, OpenAI Responses API. However, like, one thing that I found was missing was
built-in tools were not represented yet in Genesomatic convention, so this PR is basically to fill that gap.
For the built-in tools.
So on December 16th last year, we had the meeting, and one of the feedback items came up was, can we look at some of the competition, like OpenAI, Google, Anthropic, like, all the providers, and see how the
Built-in tools, requests and responses are represented.
And, that can help us decide whether we should break it down into two parts, like request and response, or just one part.
Or just one, like, kind of an object which has both informations.
So, I did some research, and I put them, in a doc, where the link of the doc is, right there in the hyperlink.
So, and this talks about, like,
all three, OpenAI, Google, and Anthropic, and gives a recommendation. So, the recommendation that I gave, based on the research that I did, is it's easy and nice, and it's more consistent if you break them down to tool call and tool response for built-in tools as well.
Yeah.
**Liudmila Molkova** 16:26 And kid.
**anksing** 16:26 But, yeah.
**Liudmila Molkova** 16:27 Oh, go ahead. Go ahead, Erin.
**Aaron Abbott** 16:29 Oh, I was gonna say, yeah, this is super useful, and the executive decision is also really appreciated, so…
**anksing** 16:36 Thank you.
**Aaron Abbott** 16:37 It sounds like we just need, kind of, feedback and, final approvals here.
**anksing** 16:42 Yes. Like, so this is one, decision that had to be made, and there is one more, so I can come to that,
Lima, if you have any questions before that.
**Liudmila Molkova** 16:54 Yeah, my main question, so, like, I checked the PR tomorrow, maybe you updated it since, but, it seems we are…
**anksing** 17:03 Now defining the…
**Liudmila Molkova** 17:06 Code interpreter tool definition, but are we…
Is the goal to define a generic one?
**anksing** 17:16 Yeah, actually, I'm gonna update that PR, sorry, I haven't gone to that, because I was, like, like, first, let's make the decision, and then I'll do the, update of the PR, just once. So, the aim of this PR is, like, not to define the generic… any, like, any of the generic,
built-in tools like Code Interpreter, which is available, like, across providers right now, at this point. But just to come up with the…
Like, come up with a design on how the tool calls for the built-in tools would be represented, and…
Yeah, so I think that code interpreter was just an example I added initially, but probably I'll update that and won't include that.
**Liudmila Molkova** 17:56 I see, so the principle you're suggesting that the, like, the… there is still the request and response in some shape, the toll call part and to-response part, right?
And then, for any built-in tool.
**anksing** 18:10 Yes, exactly, exactly, because, like, it was really hard to come up with a generic, like… because every, provider has its own way of representing things, so…
Yeah, so I don't think, like, at this point, it was really straightforward to say, okay, this is what would work for everybody, right?
**Liudmila Molkova** 18:30 Nice, thanks.
**anksing** 18:32 That's go.
Okay, so,
Yeah, please let me know and share any feedback on, like, this decision about, like, representing built-in tool calls and tool responses separately as two different objects.
And then the second decision that we had to make was, and I think there was a comment by you, Aaron, as well.
Should we extend the existing tool call part and tool response part that exists, or should we have a separate
new part defined just for server tools call and server tool response.
So…
I think I'm open to both, because both of them helps me achieve the same thing, in a way.
So I was not really…
biased towards one solution versus the other, so I can go either way on that.
Yeah, and, Aaron, I would like to get your feedback on that, since,
You had a specific comment about that, so I just wanted to make sure we cover that part, and…
Can make a decision.
**Aaron Abbott** 19:44 Yeah.
I think I kind of shared what I was thinking there,
I don't know if there's any counterpoints, but it seems…
Like, it's relatively inconsequential, but it might make things a little bit more ergonomic for,
People using the schema.
That was my main motivation, at least.
**anksing** 20:05 Got it. Okay. No, I think that's, Indefinitely.
And, okay, let me also…
So, since you're talking about that, I want to… I'll quickly,
share my screen. There's one doc that I've put together of these two options, and I want to just talk through them, and hopefully we can make a decision today on that, too.
Okay… is my screen visible now?
**Aaron Abbott** 20:43 Yep, I can see it.
**anksing** 20:47 Okay.
So, so,
Yes, our tool call representation. So, these two proposed representations, one was extending the tool call pattern
And the tool response path, so I think we just discussed that.
And the second one option was having a new part called server tool call and server tool response. And…
This is how the server tool…
call would be represented, and this is just a sample for a code interpreter, but the thing that I want to highlight here is this is kind of a polymorphic object, where
The part type is server tool call.
And then there is a property called server tool call, which can be polymorphic, based on which
built-in tool or server tool you're representing, whether it's code interpreter, file search, web search, right, things like this.
So that it kind of makes it more… schematized.
And, and I think there was some feedback from
There was one more comment about, like, Can we also have a…
free flow any, which can capture, kind of, any tools which we don't know how to represent yet fully, or…
So, I think that's something I want to cover as a part of this as well, where server tool call could be any specific schema based on the tool.
Plus, like, a generic… like, we have a generic part, like, very similar to that.
**Neil** 22:24 Since they're fucked.
**anksing** 22:25 See? Wait.
**Neil** 22:27 I was just gonna say, if, you know, admittedly very new question, but might be instructive, if I may?
**anksing** 22:35 Sure, sure, please go ahead.
**Neil** 22:36 Thank you. So I was curious, like, you clearly have some good data, like, descriptions or data model, like, set up here, and, if I'm correct, are you suggesting, like, you're proposing this separate from the persistence layer, for lack of a better word? You're, like, trying to, identify the elements, or is there…
I guess that's the one thing that I'm wondering is, like, how these are represented in, either relational, I guess for lack of a better word, or, maybe to use a better hotel word, like,
What's the, semantically, as part of the same…
is that what the third one is?
**anksing** 23:19 a single…
Yeah, yeah, so this one, like, was the option where, like, if you want to represent all of them as one
Cool call, but then,
Still, you would want to, like, kind of break it down to tool call and tool response, because that makes a lot of sense, and most of the providers, they do break it down in some form or the other, so…
So this one is not too different than the option 2.
And option 2 kind of makes it consistent with the function tool calling as well, so it's kind of easy to follow and understand.
**Neil** 23:48 And then you persist this where? Is that… are you… are you at that point yet, or is this still protocol, or whatever specification that doesn't get into the details of persistence?
**anksing** 23:59 So these will be, like, right now, for JNA apps, for example, if I pick a span called Invoke Agent Span.
the messages, like, which is basically your conversation history, can be represented as genai.inputs and outputs messages, and I think Lumila did a great job getting that out, the part of the hotel. So, this is basically kind of a,
Defining how you would represent.
The tool call and tool response for…
built-in tools from providers like Anthropic, OpenAI, Gemini.
For example, like, code interpreting, which runs behind a service, right? So all you get is your call and the response.
**Neil** 24:41 Thank you so much, that was… I hope that wasn't, too, low-level of a question to be asked, but…
**anksing** 24:47 No, no, no. Oh, and thank you for, I really appreciate, actually, you clarifying those things, so…
Appreciate that.
**Neil** 24:57 Yeah, good. I mean, I don't want to take up too much time, but I was wondering if there's some,
some amount of overlap. It is admittedly very self-serving, in a sense, but, like, I was kind of looking at a similar challenge in representing
Agent communications as, traces and parents and spans. So I can talk more about
Yeah, yeah. So, thank you for that. I appreciate that. Like, I… because there's a JSON layer, and then there's, like, the persistence as well, and I wasn't as… I have to double-check, like, the JSON layer in case you don't persist it. I don't even recall off the top of my head what I used for…
this specific thing, but I… it feels like there's overlap. I could be wrong, again, I'm super new, so forgive me if I am.
**Liudmila Molkova** 25:50 Yeah, there, there is some overlap with the agent communication, it's just we… this is the attributes we capture. These attributes can, in theory, show up
on the agent spans, but more realistically, they are part of your communication with the model directly, right? So,
That this is how, when we capture the two calls.
Like, there are function 2 calls that happen on your box, right, and then it makes total sense to…
record them as input and output, and then when you talk to, let's say, OpenAI Responses, you give it a list of tools that can include tools that model loads, right? Model calls it.
**Neil** 26:33 Right, right.
**Liudmila Molkova** 26:34 Including code interpreter, and then when you… that agent, like, the model, the agent, it's blurry, invokes this tool on the backend site, it would return some objects saying how it went.
**Neil** 26:47 And we need to wait to record it, and we record it on the…
**Liudmila Molkova** 26:51 Attributes, and this is the schema we are discussing of the… of how we record the stuff on the attributes for the spans or logs.
**Neil** 27:00 Inside the model's perspective, or what have you.
Well…
**Liudmila Molkova** 27:06 Like.
**Neil** 27:07 Sorry, go ahead.
**Liudmila Molkova** 27:09 Model, in a sense that this is the data type we defined, not that it's a large language model or something.
**Neil** 27:16 Right, but I guess what I'm saying is, like, this is… and maybe… I forget if I don't want to go too deep, but, like, this is the… the representation…
Across the models to be represented to… presented to the users, you know, in a client-server, almost, sense, or if that's not too passe or whatnot.
And so this is…
**Liudmila Molkova** 27:38 Yeah, so what we are trying to do is to build some layer that is common across different providers, and this is somewhat tricky, and we always have this balance of, like, how much do we want to
formalize and unify, and this space is not…
great, we try to stay sane. It sounds like some things, and we need a way to define how those server two calls are captured in general, and maybe we will have a few specific
Models for, let's say, code interpreter, because it's common, or maybe file search, and, like, there should be a limited list of things we will formally define in some generic way.
we have.
**Neil** 28:23 Yeah, great, because I was just wondering, like, this is great, and then how would you… my question was, like, how would one query this data? But it sounds like we're on a little early there, but it's, like, where we're… that's where the direction is. We're skating towards the puck is going to be, not where it is. Thank you so much for all patience.
**Liudmila Molkova** 28:40 Yeah, thank you.
**anksing** 28:43 Thank you. Appreciate your questions.
Okay, so…
**John McBride** 28:49 I had a quick question on, MCP tool calls. If you would envision the generic
semantics capturing MCP, or, you know, any, like, future use, I guess, of those tools?
**anksing** 29:02 Yeah, so, for the scope of this PR, I'm just limiting it to the server-side tools right now, but for MCP, like, I think I have ideas, but I don't… didn't want to add them at this PR to make it too big. Yeah, fair enough. But then, definitely, I have some ideas, if you'd like to discuss, I can, definitely, we can discuss it over Slack as well.
And come up with a PR.
**Aaron Abbott** 29:25 Yeah, I think, John, did you mean, like, server-side MCP calls, where… the server.
**John McBride** 29:30 Yeah… Yeah, because from my experience, they're…
they're kind of two separate, same-ish things, like, you can have these clients that are calling MCP tools from, like, an MCP client, but then Anthropic, OpenAI, they have MCP servers they can connect to on their side from the providers. And they generally have the shape of this with
the tool name, the JSON schema, the, like, blob of arguments or whatever.
So it could fit in this generic thing, it's just, I guess, a choice in, like, how specific you want it to be.
**Aaron Abbott** 30:04 Yeah, I think as long as we think it can fit in here, it should be enough, like, to move forward with this PR, and then it would be a really good follow-up, territory, because I know a lot of providers do support that.
**John McBride** 30:14 Yeah, plus one.
**anksing** 30:19 Thank you. Thanks, Tom.
**Liudmila Molkova** 30:21 In the sense, it kind of makes sense to separate, like, the client-side tolls and the server-side toecalls, because, well, it's hand-wavy, but they are, like, different enough to deserve different
type hierarchy.
I can't see, like, the argument for it, and I don't think we can, like… we know for sure what would be the best.
**anksing** 30:52 Agree, and yeah, thanks, Aaron, for adding that comment as well, which made me think and kind of come up with the option to kind of separate them all, so appreciate that.
Okay, so, looks like, we are in agreement with the option to, have a server tool called and server tool called Respond, so I'm gonna update the PR with this information.
I think these are the two major discussion points.
That I had. And the third one was,
and which I think was a little bit of lower priority, was about, providing a way for providers to define their own server, we'll call and pull-response schemas as they evolve, as new tools get added, right?
And, yeah. And then we can look into if there is a way for some of these tools to have a generic, tool called ProResponse Pack.
Like, I had it, like, yeah, initially for Code Interpreter.
But I think that can come later.
And a follow-up here.
Okay So… Thanks, we're kind of…
Yeah, and I think from my side, I feel like…
We're kind of closed on those two decisions that I wanted to. So, thanks for…
Thanks for the feedback, and I'll update the PR and share the update to PR soon.
**Aaron Abbott** 32:16 Awesome. Thank you, and, I owe you a review as well.
So, thanks, Adam, appreciate it.
**Aaron Abbott** 32:29 Sorry, I deleted myself from the meeting.
One other thing I was gonna mention was, good, great discussion. Like, I think, one area we're really needing contributions, and somebody asked, was reviews. So even if you don't have, you know, like, green checkmark, you all are familiar with this space, so getting some reviews on these PRs is,
Super important in perspective, because…
Yeah, you all know a lot about LLMs and all that stuff, so…
All right, Pavan, do you want to take it over? And actually, we might… we have a pretty full agenda, so if folks want to add, like, a time box estimate to each agenda item, it would help with, just making sure we get through all the topics.
**Pavan** 33:19 Yeah, sure. I think I won't take more than a few minutes.
Okay. So…
Continuing the last week's discussion, I think, you know, I was basically pointed to the hotel browser SIG, just to, like, sort of go over and sort of, you know, present this idea to them, just so that, you know, we wouldn't necessarily be stepping on their shoes, because we have
explicitly and clearly defined, you know, like, who creates the session IDs, how it propagates, and they all are already using, you know, session.id, within their, sort of.
you know, instrumentation, so to speak. So, when I sort of presented, like, where we are coming
from, in the, sort of Gen AI, you know, space, I think they sort of largely agreed, that, you know, reusing the same
attribute is probably not an issue, as long as it's sort of, like, user-initiated task, which I think, you know, that's the premise that we are actually going with. And, like, they also did sort of say, with respect to the instrumentation, that, you know, like, as long as
SDK, you know, instrumentation doesn't necessarily translate baggage into semantic attributes automatically, it should be fine. And I think the key takeaway is that
the session ID, you know, needs to be set by the application or the agent runtime. And, you know, baggage could be used to, like, let's say, propagate it, either through, like, agency protocols or, you know, through, like, manual approach.
Or HTTP, you know, which could be, sort of, like, like, one of the options that the application could choose to, sort of, you know, work with. So…
those were, like, some of the key takeaways that I, sort of, you know,
came with, or rather, you know, went away with after the last week's, you know, browser sick call. I don't know if that sort of helps, with respect to the discussion that we were sort of having.
And if it sort of narrows the scope for the… Like, you know.
with respect to seeing if this would make sense, and if I can sort of start a PR if needed. Again, it would be, like, completely optional. There wouldn't be any, sort of.
explicit
requirements for the application or for the instrumentations to carry with, but if it's available, then, you know, the instrumentations would sort of
Like, you know, use, or rather, you know, use that in order to, sort of,
Set it in, in, in, in their spans.
So…
**Liudmila Molkova** 36:25 by seeing available. So, like, let's say we are… we have a handful of instrumentations in the Python Country Prepot.
what would they do? Like, nothing?
But where would they get session ID from?
**Pavan** 36:45 So, like, you know, you meant to say, like, who sets the session ID, or rather, like, how would…
the session IDB propagated in some sense.
**Liudmila Molkova** 36:57 A more pragmatic question. There is an instrumentation like the Eclip and AI or LinkChain.
What should it do as regard to Session 8?
**Pavan** 37:08 So, as long as, like, let's say the, user-initiated task, you know, let's say, like, whichever
you know, agent or component is rather interfacing with the user, that would sort of set the session ID, or rather, you know, the user-initiated task, right? The session ID would be set there, and through agentic protocols, let's say.
the session ID would get, you know, like, let's say, propagated through baggage, and it'll be set in the… or rather, it'll be present in the hotel context of the other agent, so to speak. So, unless
there is, like, an existing attribute called session ID within the baggage, then those
OpenAI instrumentations wouldn't necessarily set it within their spans. So it's mostly, like, if and only if it's present, then the instrumentations will sort of know that it needs to check within the context, and if it's available, it'll just maybe
Use it and propagate it along, like, the entire, end-to-end
Flow, of, of that user-defined task.
**Liudmila Molkova** 38:26 So, if I understand correctly, then OpenEI Instrumentation, or any other one, would check the baggage, and if there is a session ID key there, it would stamp it as an attribute.
Is this the… the proposal?
**Pavan** 38:41 Yeah, yeah, yeah.
Oh, that's… that's how I'm mostly thinking about it, but… Yeah,
We could sort of maybe define other ways that, you know, the instrumentations would first
check before even looking at the baggage, for example, or the open telemetry context that it has access to, to see if there is a presence of a session ID key, and if that is set, and, you know.
If the, if there is a, you know, associated, you know, string value, then it'll probably use it, but if not, it won't do anything.
But the responsibility of propagating and everything wouldn't necessarily lie with the instrumentations themselves.
**Liudmila Molkova** 39:34 Right So then…
what gives me pause is that, like, I mean, it makes sense, and we talked about it, it makes sense. What gives me pause is that none of the instrumentations do this so far.
**Pavan** 39:49 Yeah, yeah.
**Liudmila Molkova** 39:51 I can try.
It's just an unconventional thing to do, uncommon in our world.
But nothing about baggage is common.
**Pavan** 40:07 Agree. Baggage, you know, in itself is sort of, like, you know,
the probably default way to propagate, like, anything between, like, multiple hotel, you know, contexts, right? But, I think one of the ways that we were thinking about is that, you know, if…
there is a presence of, like, a manual context propagation approach, which, again, is what is suggested in the hotel docs. And going forwards, I think what we could also do is maybe bring in some
protocol-related auto-instrumentation as well, for example, A2A instrumentation or, you know, MCP instrumentation. I know there is some MCP instrumentation already, but if we, let's say, you know, do… if two agents are, for example, communicating with
8-way, you know, protocol, then the, suppose, you know, quote-unquote, send and receive methods of two different agents could be monkey batched by those instrumentations.
library, and using that, we could automatically check the presence of these, you know, like, session ID fields and propagate it and set it in the destination agent context. In that sense, again, it would probably be somewhat of a…
addition, or rather, you know, a change that the instrumentations would need to make, but if they had access to such, you know, protocol-level auto-instrumentation, then the OpenAI or ADK or any other
The instrumentation libraries wouldn't necessarily need to change,
any, let's say, code, because the protocol instrumentation would be sort of a separate thing. I don't know if it… if what I'm saying is making sense, but that's how…
**Liudmila Molkova** 42:07 Yeah, so what… how OpenTelemetry does it usually… the bag… the baggage is propagated through a protocol. Protocol is agnostic to the instrumentation. Instrumentations can access the baggage from the context.
What happens usually is that there is a processor.
Like, people who want to stamp things from the baggage on the telemetry usually enable the processor that stamps them from the baggage to the telemetry.
Yeah, baggage spend processors, things, Jimmy. It's available in some languages, sometimes you implement it yourself, sometimes there is a component that does it for you, but this is the typical way.
So all you are saying makes sense, and it's the only unconventional thing that instrumentation would actually participate in this, at least by default. And I'm super sorry, Aaron, I think I jumped in front of you. Go ahead.
**Aaron Abbott** 42:58 No, you're fine. I was gonna say something similar, like, usually the baggage is propagated kind of out of the box, so I was curious what you meant, Pavum, like.
Did you mean…
it's put inside of, like, an A to A request, or did you mean something else? Because usually it would go in, like, the HTTP header automatically, right?
**Pavan** 43:17 Exactly. So, within the header itself. So, within the header, we would automatically, you know, create a new key value and propagate it automatically as long as, you know, it's sort of using A2A by default for agent-to-agent communication. So.
**Aaron Abbott** 43:35 But, like, this already works, right? Like,
you shouldn't need any changes specific to A to A or anything like that, right?
**Pavan** 43:45 Right. I might need to…
take a look as to, like, how exactly it sort of works out of the box today, but I think those were along, like, in the similar lines that I was also thinking about.
But yeah, I think… That's a good… that's a good point.
**Aaron Abbott** 44:09 Okay.
Gotcha. And then with Milo, like, just to make sure I understand, you're… you're given pause because…
It would be done in instrumentation instead of a processor, which we usually do.
**Liudmila Molkova** 44:21 Right, yeah.
**Aaron Abbott** 44:23 Okay.
**Liudmila Molkova** 44:24 And Dan… For semantic, like, for instrumentations, it's important to understand, or for semantic conventions, it essentially means that
If we put session ID on the attributes in GenAI spends, then it would be instrumentation responsibility, not the processor responsibility.
And all the parts with the processor should work?
As long as propagation works already.
If somebody set session 80 in the baggage, it would be… and users processor?
All spans would have Session 80 already. No change needed anywhere.
**Pavan** 45:08 Got it.
**Aaron Abbott** 45:12 Okay, I mean, it sounds interesting and feasible to me, like, I understand it's different than what we usually do, but,
I… it doesn't seem, like, hacky or bad, necessarily. It seems maybe a little inevitable, honestly.
But.
**Neil** 45:29 There's a little pattern, dare I say.
**Aaron Abbott** 45:33 Yeah.
**Neil** 45:34 Sorry.
**Aaron Abbott** 45:36 No, no, you're fine. No, that's all I was gonna say.
Anything else on this one, Juan? You just… like, next step is kind of writing down the results of the discussion we had here.
**Pavan** 45:49 Oh, yeah. And I'll try to address, like, the processor, you know,
trade-off as well, or rather, you know, the different, approach that Ludmila had mentioned, and see
You know, if we could also…
Sort of take that into consideration.
**Aaron Abbott** 46:12 Okay. Lumila, do you feel like we're ready for that? Do we need more, kind of, design here? What do you think?
**Liudmila Molkova** 46:19 I mean… while the purchase has pros and cons, I, considering, like, the baggage.
is rarely formally used in OpenTelemetry.
And I, I hate…
I'm interested what would happen if we actually try leveraging session 80 in an explicit way.
I would like to try that. I don't know where we end up with, how much problems we'll…
Have… because of it.
But I, I…
let's just try if there are no objections. Like, if you want to add session ideas up to an attributes.
on… GenAI's pants.
And, you would, we can implement a prototype for it in one of the instrumentation libraries.
These two things together.
I think would be enough, and we… let's not design it, we've been designing it for, like, months.
**Aaron Abbott** 47:24 Yep. Agreed, sounds good to me.
**Pavan** 47:27 Would that be sort of a precursor before
there is an explicit PR to add it to the spans, do you think, Rudmela? Like, the POC, or…
**Liudmila Molkova** 47:39 It would be great to… to have it in one of the… Yeah, sure. Or maybe in GenAIOT also, actually.
**Pavan** 47:48 Okay.
**Liudmila Molkova** 47:54 Thank you.
**Aaron Abbott** 47:55 Okay.
Thank you.
Josh, I think you just… your next year, you just wanted some additional reviews here. Looks like we've got two approvals, Leighton approved.
Yeah, any… do we need more, Ludmilla? What do you think?
**Liudmila Molkova** 48:17 I can hit merge if everybody's comfortable. If you folks want to take a look and just need more time, let me know.
Does anybody would take a look if we keep it open for another few days?
**Aaron Abbott** 48:33 Not me, no.
**Liudmila Molkova** 48:35 Okay, and I'm just going to hit merge.
**Aaron Abbott** 48:39 Cool.
Alright, and last one, Redima, you're on?
**Ridhima Satam** 48:52 Yes, so there are two, I got some initial reviews on those, just want to ask if anything else is concerning there, or people can take a look at, again, who has… I have resolved some comments there, so…
Yeah.
**Aaron Abbott** 49:12 Yeah, I… I can take a look and merge. I think Keith took a look at this one. Sorry, this one.
the, instrumentation PR.
This one… this is, yeah, submit to conventions to add the workflow operation name to Agent Spin.
Yeah, I'd… I would like to take a look.
has anything changed, kind of, since the last discussion we had, or just called for reviews?
**Ridhima Satam** 49:44 Yeah, just call for reviews, and if anything else, so in this new… are any other attributes of required, like, we can do a follow-up, but just in case, if anything is absolutely necessary to go in this, additionally, in this PR, people can point that out.
But yeah, just take a look. And I think it's a minor thing, I think some maintainer has to, or someone has to trigger that, or test, or… yeah.
The pending checks, yeah.
On the PR.
**Aaron Abbott** 50:18 Ankit, do you wanna jump in?
**Ankit** 50:24 Yeah, I had one question, though, might not be related to the exact PR, but was there any, thing discussed about, like, conditional loans, or loans that make flow?
**Liudmila Molkova** 50:39 Can you repeat your breaking?
**Aaron Abbott** 50:52 I'm having a hard time… some network issues on Git?
**Ankit** 50:57 Am I audible?
**Liudmila Molkova** 50:59 Now, yes.
**Ankit** 51:00 Oh, okay. Sorry about that. Yeah, I wanted to check if there was any discussions about, like, conditional nodes, which are, like, decision-making nodes on how to represent them.
What kind of attributes or things we need to capture?
Nope.
If not, that's okay, but just wanted to know.
Did not affect the sphere, though.
**Ridhima Satam** 51:27 Is it related to this peer you're saying?
**Ankit** 51:30 Yeah, basically mostly related to workflows, like…
**Ridhima Satam** 51:36 Okay, yeah, no, we didn't discuss anything like that, but if you have any comment, like, you can just add, and then… your voice is still breaking for me, but if you can add a comment, we can see if anything is required there.
**Liudmila Molkova** 51:53 I, I have a question. It's probably… it can be a follow-up.
We have been talking that workflows would have different
like, when I look at the dashboard, I would separate workflows from just regular LLM calls, because they would have, I don't know, different expectations, different times, and everything.
and… here, we're writing a span.
And the workflow metric would be essentially part of the GenAI client operation duration.
Is it what we want? I think this is not what we wanted. We wanted to have a separate thing.
**Ridhima Satam** 52:42 So in the JNAI utils, you're saying that,
Sorry, so there is… right now, there is no workflow invocation there.
But eventually, that's what was the thought process that we'll have in workflow invocation, which would also have the metric
Oh.
Initialized there, so… we will have, like, a start of a workflow and end of a workflow.
And the duration for that. Is that where you're going with your question?
**Liudmila Molkova** 53:15 Yeah, I mean, like, today with your PR here. You're writing the operation name and the new span definition. That makes sense.
But we are not adding a unique metric for this.
**Ridhima Satam** 53:30 Oh, yeah, in this, right. In this PR, I'm not adding the metric here.
But that could… I thought, like, it can add it in the follow-up year. That's okay, if that's okay.
**Liudmila Molkova** 53:44 I… It would probably be okay to me. What would we…
For tenant, the workflow name would be there.
The attributes, I mean, or type.
Maybe some other stuff, but essentially, it's a very small metric.
In terms of attributes, yeah. Maybe,
I'll leave a comment, and it would be great to create an issue for this so we don't forget, because, like, this is the design decision we're making. It's important because it has different… significantly different duration.
**Ridhima Satam** 54:22 Okay.
**Aaron Abbott** 54:24 Yeah, sounds good for a follow-up to me, too.
And yeah, adding… adding some more… not just having this grab bag metric with, like, everything under the sun would be good.
**Liudmila Molkova** 54:36 Should we break down that metric? Like, I don't know, maybe invoke agent should be a separate metric as well?
**Aaron Abbott** 54:43 Yeah. Yeah, I've been thinking that,
For sure, like, we talked about…
It's hard to target this with views, it's difficult to, you have, like, the histograms.
All using the same boundaries, unless you add additional views, so…
I think that would make sense, and yeah.
**Liudmila Molkova** 55:05 Yeah.
**Ridhima Satam** 55:08 So, we are saying that we'll have, like, say, a duration metric with the name as workflow.duration, not the one what right now we are using, right? The client duration, and then we change the operation name. But we would have, like, a specific separate workflow duration, and then invocation duration metric, right? That's what we want.
**Aaron Abbott** 55:28 Yep.
**Liudmila Molkova** 55:29 I should stop somewhere, because at some point, like, should we move execute tool to a separate metric? Maybe. What about create agent?
like, what about chat versus generate content? Yeah, I don't think we can solve it right now, but I mean, we… we should maybe start thinking about how we…
have, how we… Guru does different operations in a way that
The metric… combined metric for them makes sense.
But for you, Redeema, the only ask would be to…
To start with the workflow, because it kind of makes sense. I would imagine we would have workflow usage metrics versus the, like, the from tokens perspective. Maybe if you can report them, it would be cool, but yeah.
That's the future.
**Ridhima Satam** 56:32 Sure, yeah.
**Aaron Abbott** 56:36 Okay.
And concretely here, the ask is just to file an issue for this PR, right?
**Liudmila Molkova** 56:42 Yeah, I'll leave a comment right now.
**Aaron Abbott** 56:45 Bye.
Cool.
Any last thoughts on this one?
**Neil** 56:54 No, looks good to me.
Good thinking.
Thanks.
**Aaron Abbott** 56:58 Cool.
Alright, that's the end of the agenda, everyone.
It's nice to meet all the new folks, and yeah, see you all next week.
**Neil** 57:09 Yeah, thanks for being welcoming. Have a great day.
**Aaron Abbott** 57:12 Of course.
**Liudmila Molkova** 57:13 Thank you.
**Neil** 57:13 Bye.
**Ankit** 57:14 Yeah, good.
