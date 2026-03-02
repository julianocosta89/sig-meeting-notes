SIG: LLM Semantic Convention WG
Date: 2025-07-15
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/cIwiiOeSkvt8PycLNbKlgr63xEMLS9VjJ8XjRNVp_-jgbY1rI27iLvwz35kzFmQ.uff5fLeJS5IfjfcG
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:42 Hello, Hi, everyone!
Let's give people a few minutes to join, and in the meantime
feel free to add topics to the agenda.
I will share. Start sharing in a second.
Okay, while we are waiting for other folks to join. Let's take a look at our Project board. We don't have new issues. We have a bunch of things in progress.
And I'm just checking. If there is anything immediate we can make progress on.
Let me. This one got stalled.
By the way, while we, since we're here, does it? Anybody know if in practice they mentioned, Count
could have high cardinality like in theory, it's just a number.
But in practice it has very few values that people actually use.
Okay, anyway, if you have thoughts feel free to jump onto this port request.
It's definitely still in progress. We're going to talk about this one quite a bit.
This is the embedding instrumentation from the rule. Let's take a look if there is any anything here.
Yeah, I think it's waiting for the semantic conventions for request.
Ding this one got!
Don't
we have, Aaron.
No, we don't.
I am going to reopen it.
Okay,
and
we still have this one. It seems there are a lot of people who would be interested in the common materials, and
I don't believe there is any recent progress on this one just wanted to check.
Okay,
let's move to the agenda. I think we have a lot of things to discuss, and we can
make progress there.
Okay, so a few small updates before we move to the substantial part. The 1st one is that we now have a pack time meeting.
On Tuesday.
It's 10 am. Think in the
one of the pack time, zones. It's Monday, 7 Pm. Here, where I am in the Pacific time.
so it gives the opportunity for folks in Asia to connect
some of the folks in Asia to connect with us folks. Unfortunately it completely excludes Europe.
But unfortunately ours is not flat, so we have to.
We cannot have
meetings that work for everyone. This is very unfortunate. The other thing I wanted to call out.
we have the
specification change or top. It's still a proposal. It's not the actual, the spec itself, but it's a proposal to spec about the complex attributes and spans.
We are going to merge it today unless something urgent happens.
We depend on it quite a bit. And the Jenny, I see, because we we are one of the main drivers for this change
time to celebrate. It unblocks some things for us.
Yes, Emil.
Samuel Colvin (Pydantic) 00:06:37 So sorry. That's the one on on the new attribute. Sorry this is is that the is that allowing complex attributes? Or is that your Pr. For the new schema.
Liudmila Molkova 00:06:46 Oh, yeah, it's the allowing complex attributes.
Samuel Colvin (Pydantic) 00:06:48 Oh, wonderful! That's very good. Sorry! I thought it was your one, in which case I had some comments, but that that's great.
Liudmila Molkova 00:06:53 Oh, yes.
I'm aware of your comments. Thanks for leaving them. I'm not going to merge anything with that. With this open discussions.
Samuel Colvin (Pydantic) 00:06:59 Sort of sort of checking. Great. Thank you.
Liudmila Molkova 00:07:01 Yeah, okay?
And with this, let's move on to the agenda.
should prat. Do you want to talk about the Pr.
shiprajain 00:07:17 Yes, would you like to share, or should I share my screen.
Liudmila Molkova 00:07:22 Do you want to share whatever you prefer?
shiprajain 00:07:25 I think I can share quickly.
Liudmila Molkova 00:07:27 Yeah.
while you're saying, would you mind sending it against semantic conventions? It's it's currently against my fork. And I didn't even notice it.
shiprajain 00:07:37 Okay, I I did it on purpose. I can do that tomorrow again. So I can explain that.
Let me quickly share my screen.
Liudmila Molkova 00:07:48 Yeah.
shiprajain 00:07:59 Okay, so this Pr is basically about so in the process or in the journey of defining the proposal for multi agent
observability, which I from Ms and so we from Ms and Cisco's team, we are working together internally. We realize that there are enhancements that we will have to also start proposing for new. You know the single agent spans like a tool execute tool span Llm span
invoke in span.
Again. This is all deriving from my very 1st proposal document, that is, for multi Agent tech. So I took the suggestion and I started off creating the Pr
For the smallest Mvp. Possible. This is the Pr that I've created only to cover the enhancements that we're suggesting for execute tool span and some enhancements to llm span in nutshell. It covers these changes
we are proposing to bring in you know, version control at each level. So for the tool right now, we don't have any way to capture the version of the tool.
This is one generic
attribute which we wanted to propose. When it is present in the execute tool span, then the value would be tool similarly, for other relevant span, the value would be assisting the user as team correct.
then we are in, we are suggesting to include genie tool type. So we understand that there can be different kind of different types of tools which can be triggered by an agent. So far in hotel, we describe more about function based here. I have listed more such tool types.
because depending upon the kind of tool, though the input and output schema which I'm explaining below won't change. A schema would change. But the types won't right, but it is necessary for us to be aware what can be the possible enums. So nevertheless, we should capture tool type
and then the other 2 things that I included were for each of these pans like execute tool. We wanted to capture very clearly what goes in what comes out
for now I mean, all of this information is kind of present in different capacity, not in complete capacity, but in a certain capacity in existing events like genai choice genai assistant message. Gen. AI tool message inputs can be through Gen. AI system and Gen. AI user.
But that's where I fell back upon the open Pr from Durdmila. This is basically done in order to show that I take reference from this. However, in my proposal, I'm not keeping any common attributes, so, in short, we want to propose parameters to capture input and output or not parameters. Sorry attributes to capture input and output. For input let me quickly go now at the
a little deeper level.
Okay? So if you see here, we are talking about introducing tool call argument. And
I'm proposing to basically bring it like a nested dictionary with 2
keys parameter schema and runtime arguments. The naming, of course, I'm hoping to get more feedback, but the idea is to clearly capture. What are the what is the parameter schema for that tool? What kind of incoming arguments can be passed with a clarity on the type, the description, so on and so forth.
Alex Hall 00:12:18 I think, in general, there's quite a lot of desire to capture parameter schema.
But in general, as in you know, whenever there's a request.
capture all of the tools that could be called, so that we
you can confirm that this was available, and the agent chose not to call it
so I think that we would. We would already be capturing this somewhere, and it wouldn't be tied to the tool actually being called. I mean, I suppose we could still have this here, and maybe it'll be useful to have it
directly on the same span. But at this point it's a lot less useful, you know, you can really see that the actual data, a description of the structure, is less useful.
shiprajain 00:12:58 So 2 things. That's what the actual data I'm covering under runtime argument. The reason to keep these 2 was again from our experimentation where the incoming parameters there can be many different parameters, and that's what I'm also capturing as part of this field like required. So this shows us what are the acceptable
arguments to that tool. And in the runtime arguments, the actual parameters which were utilized. And what was the value?
And that's where we can do a lot of evaluation with respect to tool calls efficiently made or not. So this is something which we were internally doing like a custom implementation. But to basically capture these 2 things separately was to make sure that the right arguments are called.
We're retaining the information about the types. And then during runtime, what were the what was called actually, and the value of it in examples actually down below, you would see more clearer. So, for example, this is the parameter schema.
you know. Query this thing, that thing, and in runtime the the actual value, the actual argument, and the value of it.
So.
But yes, please.
Liudmila Molkova 00:14:17 Said that the we should have 2 definitions.
As a part of the span.
so the agent span should have an attribute
defining all the tools and the the argument. Schema should be there.
But also simple types are actually part of the
payload. So when you send, let's say, string attribute or a string value.
All the consumers of this telemetry know it's a string. It's part of the protocol.
So it does not make sense to actually write, what is it that is a string?
The description comes from the 2 definitions, and if we duplicate it on 1st 2 definition, then also in each time this tool is called. Then we are bloating telemetry a lot and we should try to avoid it.
It makes evaluations life harder. You need to join some telemetry.
shiprajain 00:15:28 But it.
Liudmila Molkova 00:15:30 It's the trade off between user pays a lot of money for telemetry and complaints a lot versus those who do evaluation need to be a bit more clever.
shiprajain 00:15:41 Okay, I agree on this one for the type. So to one thing I didn't understand is whether there is a feedback on also not including type.
Liudmila Molkova 00:15:55 And then the definitely the simple types are.
it does not make sense to include them. They are part of the value.
shiprajain 00:16:07 Okay.
okay? And how about? So if if we get rid of these 2, and we still want to retain what were the list of arguments acceptable, and whether they were required or not.
what is the team's perspective over these 2.
Liudmila Molkova 00:16:25 So we will have a 2 definition recorded as an attribute.
You can take the 2 definition and find the 2
you can join by the name. You can query this data right? You have it recorded on the telemetry. You can find what this argument.
Means in this span, based on the 2 definitions provided
this way, you, you know, if it's required or not, because you have 2 definition as well.
shiprajain 00:16:56 Got it, and tool definition becomes a part of what span.
Liudmila Molkova 00:17:01 The agent span Jenai span
right the any any span that deals that sends 2 definitions to the model or to the agent.
shiprajain 00:17:14 Okay. And right now we don't have that available right? Lunla.
Liudmila Molkova 00:17:19 We? We don't. I've seen it. I've heard somebody else talking.
Ankit 00:17:23 Yes, ankit, I guess. Hey, ankit.
hey? Hi, yeah. Yeah. Sorry. I just wanted to suggest, like, if you can also add, like.
I know this proposal doesn't have it, but could be like an announcement where we could also capture the tool definitions
because most of the agent tech framework they allow now overriding the tools
during an agent invocation. So and
so that kind of helps capture it at the place where actually they are being used
because you can create an.
shiprajain 00:17:53 The reason. Yeah.
So so what I'm hearing, if I understood you correctly. So I mean in my invoke agent span, I was including 2 definitions already. I have not created the Pr. For that it is Wip. But at that moment I felt it's kind of redundant that I'm also including 2 definition for agents. And then I'm adding over here. This was mostly done for the reason that Anka explained where, in case
customer decides to skip tool definition as part of agent invocation, at least at the root where that particular tool is called. We have all enough information present, so that is one way to think the other way. I the other thought process I had was, maybe we can skip
tool definitions as part of agent as well as execute tool span, and we let it be available as a rag information. Which again, we don't have any parameter as of now, but like a rag. We have 2 definitions. We have agent
definitions, all available at one place, and that is shared across spans. So that is another thought I had. I don't have a proposal on that yet. I wanted to brainstorm here.
Liudmila Molkova 00:19:13 So I think there is a good discussion in the chat that A, when you make an Llm. Call not the any of the agents may be as well, but when you make an Llm. Call, it's important to record all the tool definitions, not just for evaluations, but for all other reasons, but for evaluations as well, you need to know all the tools that were available, and whether the the Llm. Pick the good one right.
shiprajain 00:19:40 Yeah. So what I was thinking, in my invoke agent span. I wanted to keep it simple as you know. Give the list of registered tools or for an agent if they're calling sub agents, then give the list of registered agents. But if somebody wants to double click on what that tool entails, or what that agent entails. Then they can go deeper into each of those spans, and from there, from the span, it can be digged so
Liudmila Molkova 00:20:10 That you?
That's how I was thinking
you would want the full definitions, right? Because this is the debug level info about the Llm. Call
what were all the tools that were provided, and there you would record everything. Why wouldn't you record
all you know about the tool definition.
shiprajain 00:20:33 Okay,
I I think I understand the point. So maybe what I'll do, Lydmila, is I'll also in the same Pr add the proposal I have for invoke agent. The current thinking that I have, and with that, if if I can get some offline comments on what is the right place that we think we should have
the entire tool definition covered at the rootest level, like the execute spans, or at the tool invocation agent invocation. you know, currently, we can take a decision.
Liudmila Molkova 00:21:10 Yeah, it's some comments as well. The the executive span doesn't know about the definition. Really, in practice.
you don't even have this information. There.
shiprajain 00:21:27 Is that the re, the the way each framework writes because I implemented this thing in semantic kernel.
and I didn't have to do a lot of changes to extract this information was already available.
And
yeah, so does it. I mean, what I can only think of is it? Does it depend upon agent framework to framework
whether the tool definition for that particular tool is available to them.
Liudmila Molkova 00:22:03 Can I see, Aaron? Has your hand raised.
Aaron Abbott 00:22:06 Yeah, yeah, I I think I'm I'm also a little concerned about like we have 3 different levels. Potentially, we have, you know, like
the code. There's a function that gets called for the tool, and it has its own parameters, and and potentially it has its own schema. So it might be like a Python type. Definition, right?
We also have, like whatever the Llm. Expects the schema to be, which is probably Json Schema. And then I often see, like agent frameworks, have their own definition of of what these things look like, and it will probably convert or take it from the source code. So I think it's just important that these things kind of line up. And we know which abstraction layer. And I think that's kind of the crux of the problem. Maybe that's also what you were getting at. Shipra.
shiprajain 00:22:48 Yes.
and if if I could request comments directly on the Pr. Also. That will really help me to keep a track of all the feedbacks, and
I can interest him.
Liudmila Molkova 00:23:04 Yeah, sure 1. 1 question this pr does not do does not
write semantic conventions in the format where we write them in semantic conventions.
Do you need any guidance or help on how to convert it into the the proper format?
shiprajain 00:23:28 Yes.
Liudmila Molkova 00:23:31 Cool. I'll
I'll send you the instructions.
Aaron Abbott 00:23:44 Well while we're here. Oh, sorry! I'll get.
Ankit 00:23:48 Thanks, Aaron. I think I saw a really interesting comment in the
chat as well about like tool definition. Should it be on the tool span or the tool Llm. Invocation span, or it should be at the
agent. Invocation span or agent execute spam, so it'll be kind of nice to close on that. And I have some thoughts, and I can kind of put those answers there like any comments in the Pr. Where I believe it should be on the invocating span rather than the tool invocations, and I can list out the like the reasons for it.
so it'll be nice to kind of have a discussion regarding that.
Liudmila Molkova 00:24:27 And that's why it would be useful to have this Pr. Against semantic conventions, so that.
You don't discuss it on my fork. I mean, I'm
I'm just a human. I'm not the organization, open telemetries, organization.
shiprajain 00:24:42 Sure. Sure. Yeah, I mean, like I explained right. The reason to fork it on your Pr was just to maintain the history that we want to get rid of events and propose as attributes, but I can easily do it directly on the main branch.
and Alex for this one. I have an example. I'll just put it over here.
Why, we were suggesting tool name versus tool call name.
Alex Hall 00:25:14 What I'm saying is that there is a semantic convention for execute tool spans.
For the tool name like this part exists, and you're proposing changing the convention.
shiprajain 00:25:27 No, these are additions to that. I have already listed in my so if yeah, I think I
I'll just check if I have. No, it is in enhancement to whatever we have.
We are not proposing to change anything existing.
I'll add that as well.
Alex Hall 00:25:47 Saying that there is a execute tool span in the semantic conventions.
shiprajain 00:25:59 Correct, and this is the proposal to enhance attributes to that span to add new attributes.
Alex Hall 00:26:05 One of those attributes is the tool name.
shiprajain 00:26:08 Correct, so I can give an example on what I was intending to capture differently for tool call name versus tool name.
I'll add it in my Pr.
Liudmila Molkova 00:26:21 It it like
definitely it. It would be great to understand like having 2 attributes which are pretty much the same is usually
But then we don't.
We try to come up with one name, and we expand the original definition of the attribute. If it works or we decide what to do with the other attribute.
It seems like a collusion and a concern.
We need to either have a good reason, or we definitely need to understand why. Why would be the case.
shiprajain 00:26:55 Yeah.
Liudmila Molkova 00:26:59 I saw Tao has his hand raised for a while. Sorry, Tao, go ahead.
Tao Chen 00:27:03 Yeah, no worries. one of the questions I have is regarding the run arguments
shiprajain 00:27:13 Runtime argument, yes.
Tao Chen 00:27:14 Time. Argument attributes since is an attribute to a span, and because that
runtime arguments may contain sensitive information.
What's the recommended way for frameworks to do with.
That's like a flag.
On turning this on and off, or
a separate flag or existing flags on, you know, turning off sensitive information.
Should we specify the recommendation here, as well.
shiprajain 00:28:02 Is that question to me? I think I don't have that.
Tao Chen 00:28:04 Yeah, yeah, or or to the group.
Liudmila Molkova 00:28:15 Sorry you didn't. I didn't capture the question. Can you summarize it for me? I'm sorry.
Tao Chen 00:28:20 Oh, yeah, so so the random arguments may contain sensitive information.
Liudmila Molkova 00:28:25 Oh, alright. Yeah.
Tao Chen 00:28:26 And and since it's it's it's it's going to be an attribute on the span. So
should we put some recommendation here? For frameworks on how to actually enable or disable.
you know, part of the certain attributes on a span, but not disabling the entire span.
Liudmila Molkova 00:28:52 Yeah. So I think this is the same story. As for everything else that we have, we have the the opt in the content, opt in flag right?
And I would imagine we will need something smarter than that eventually. But they would just start with the
this feature flag controlling this content as well.
Tao Chen 00:29:14 So it's it's sort of like in what we currently have
with the events. The messages, right? So most framework will have a flag to turn on, you know. Turn on and off capturing those messages to the
yeah, should we recommend using the same flag or a separate one?
The same one.
Okay, okay, yeah. That answers my question.
Thank you.
shiprajain 00:29:46 I think I'll get back to Alex's question. So, Alex, this particular one basically comes as I was dissecting Jenny choice event under that if we remember, there is a tool called parameter, which has, you know, function name. Now, because we understand that tools can do different types. That's why I gave a generic
name to it as tool call and name over here is supposed to be the actual method, the technical method name which gets called behind the scene. Now, tool name
I understood usually is used something generic. Not the exact technical name.
However, I understand it's up to the user how they can feed this information. And why not? To very well use tool name itself to capture the technical method name. I think that's the feedback that I'm hearing from you. But the reason why I had this separately was to basically dissect the tool call section engineer choice event I, you know, mentioned the type of the tool that is getting called, and then the the actual method within it.
Liudmila Molkova 00:30:59 Yeah, we would need to merge those attributes together.
and having 2 attributes with different names about the same thing is doesn't
make much sense from semantic conventions, perspective.
shiprajain 00:31:13 Okay, okay. So the I think the action items.
Liudmila Molkova 00:31:17 Maybe. I will share the details on how to write semantic conventions in hotel right.
Yes, where we'll need to.
I will make a pass. But I would actually recommend just taking the branch you have and just sending it against semantic conventions.
shiprajain 00:31:39 I'll do that.
Liudmila Molkova 00:31:40 Time.
It doesn't matter which. Your your tip like which which branch which branch you branched off it. It matters is that it's visible.
and that people can provide feedback and discover this pull request, even if they were not in this call.
Okay?
And then we will make some few rounds of the feedback on this one, probably
and feel free to reach out if you need any any help with the tooling. It might be
some learning curve to learn how to use it. But it's actually your friend, not not your enemy.
shiprajain 00:32:24 Sure, cool. Yeah, that's all from my side. Thank you.
Liudmila Molkova 00:32:28 Thank you. For bringing it up. Give me a second. I'll start preparing.
I have a comment in the chat, Alex. It's intended for you.
Okay, so let me share my screen.
And let's see what we have. We have something from Redema. Do you wanna go ahead and
talk about your pull request before we move forward to the large discussion.
Ridhima Satam 00:33:17 Yeah, sure, I can share my screen.
Liudmila Molkova 00:33:19 Oh, sure!
Ridhima Satam 00:33:31 Yes, so I think before earlier, Sergey, from Cisco Splunk, mentioned about a Gen. AI. SDK. Which will have
semantically semantic conventions, compatible telemetry. So. So I would just want to showcase like what we have. We have done some poc around it. And can you see my screen right now?
Aaron Abbott 00:33:55 No.
Sergey Sergeev 00:33:55 Not yet.
Ridhima Satam 00:33:57 Okay.
No.
Aaron Abbott 00:34:06 Thank you.
Ridhima Satam 00:34:06 Okay, thank you. Yes. So basically. Right? Right, we know right that we will be contributing from Cisco for the Langchain instrumentation. And we did some Poc regarding that. So we have here what Llm invocation telemetry which we are
supporting here. So basically here in the Langchain instrumentation under the Jenny. We have this callback handlers, where we are actually looking at the span, we are creating the spans and the metrics or the events from this. So, for example, here we have this Llm. Start, and then we are creating the spans here.
or emit any log here. And
similarly, at the end of the
invocation we are generating. We are adding the attributes to the span, and also we are creating some metrics here.
So what we did with the SDK. Is. We moved all this creation, logic of the span and metrics and events to this SDK, where we can have everything semantic conventions, compatible telemetry in one place. So here, if you see, this is another Poc we made.
So this is basically just a heads up how we can use this SDK in future.
So under under the instrumentation, Jenny, we have created this Jenya SDK, where we have added certain exporter here
and in that exporter.
Sergey Sergeev 00:35:54 I think it needs to be open, because it's lots of different.
Ridhima Satam 00:36:01 Thank you.
So basically, what we did this exporter we have created. So there will be 2 types of exporter right now, we have just defined, like span metric event, or just span metric span metric will not have the event in case we don't have. We want events, but in that case we are planning to put all the event data on the span itself. So this is where we are actually collecting everything
inside this exporter and the part of where the exporter is getting called from. So here it's exporter where we'll be adding all the spans and metrics and
its events, and what we'll do, we'll have an Api
where this this Api can be called from actually the instrumentation namespace like Langchain, can use this Api to call that exporter. So for what we'll do in in the In between, we'll create an Llm invocation. So we have different types of invocations. We can define here, like Llm. Invocation or tool invocation or certain types of invocation. So what we do is basically where we had earlier the creation logic of the span
from the callback handler of the lang chain. What we will do is we'll just call that Api. Pass all the attributes in this Api and convert it into a certain type of these types like Llm. Invocation, we convert it, and in the exporter, what we'll do is we'll export all those in semantic conventions, compatible telemetry.
So this is what we have proposed earlier, and this is just a Poc demonstrating the same. So we just collected everything in just one place in the SDK.
Liudmila Molkova 00:37:45 I'm I'm a bit lost. Why, it's the SDK level thing.
Ridhima Satam 00:37:51 What is at the SDK level thing.
Liudmila Molkova 00:37:53 Yeah. So all the instrumentations would only yes, api to instrument things.
And I'm a bit lost. Why do we need any SDK concepts here like, why would this thing export anything.
Ridhima Satam 00:38:10 Yeah, so we just yeah, go ahead.
Aaron Abbott 00:38:13 Yeah, I was just gonna say, so. I mean, this was one feedback I had. But I think we're overloading the word SDK here. So this is an instrumentation. Api, which we're calling just Gen. AI SDK
with most. So I think. And the same thing with exporter. But that's right. Is that right?
Ridhima Satam 00:38:30 Yeah. So this is, yeah. This is like, we are just calling the Api of the from the SDK
to export the the semantically convention compatible telemetry.
Sergey Sergeev 00:38:42 Yeah, it's Gen. AI, specifically, where?
So the the way it's different from open telemetry, Api, SDK, and etc. That it provides some a convenience
methods to define gnaa types, gnaa Apis and Gnaa exports here the difference
why we want to do it because we probably want to support at least 2 different flavors of telemetry.
One is when you export spans and metrics
and put everything on the span attribute. And second, when you have span metrics and events.
So this is kind of boil up weight
which we can solve by introducing 2 different genai exporters.
Vichio use this type of telemetry.
Liudmila Molkova 00:39:41 So the exporter from up until lunch is the component that sends your telemetry to certain destination.
This exporter is not the exporter. It's something.
Sergey Sergeev 00:39:53 It's converter, it's adapter you can name it. We we need to define the names. It's good.
Liudmila Molkova 00:40:00 So we should try to avoid mixing things like sdks and exporters. If it's just a pure instrumentation
layer theme, and we shouldn't call them that.
Sergey Sergeev 00:40:14 Which materialize a genie type, which is a python structure into some telemetry.
I.
Liudmila Molkova 00:40:26 Yeah. So we should use some open telemetry. Api related terminology, or
some terminology that does not create this confusion, because what what they see here tells me you have your own open telemetry distro specific to geni. And it's not that if I understood correctly.
Sergey Sergeev 00:40:48 That's a great feedback. I yeah. So probably we can
for gna Api. So when you report something like oem and vacation, what can this thing be.
is it? Yeah, just let's work one by one. So we named it Api. But
yeah, please, Aaron, go ahead.
Aaron Abbott 00:41:17 Well, I mean, I can make suggestions offline. But I think, like Sergey when we discussed this in the Hotel Python Sig, I think the
when. When I when we talked about some of this, it was just like this, is a proof of concept. Let's talk about the actual
high level design kind of thing, and and then we'll tweak it for the actual Prs. Is that right?
Sergey Sergeev 00:41:37 Yeah, this is just again, it's a convenience
way to show how it integrates end to end.
Yeah, we we will be working on the design, Doc. Probably next, before we continue
this change, where you can comment on this Poc. If it's helpful, let me know what you want to do next we can put it in the design. Unfortunately, I wasn't able to
do it yet.
Aaron Abbott 00:42:09 That's okay. Yeah. I think some of some of the naming is a little
like confusing, just for hotel people. So if we could just tweak a couple of them for the Poc. I think it would be a good start for kind of getting feedback on it. But
yeah, it's okay, there's no like design, Doc. I think
I I get the general idea. But we could. If there's any like specific call outs. You wanted feedback on
that I think that would be good. And and also I'm sorry I jumped in front of you on Kit. If you had something to say.
Ankit 00:42:38 Oh, thanks, Aaron, no worries. This is my 4th call. So I'm just kidding.
So I want you to understand
one aspect. So this can like this piece of code, or this piece is converting
line chain. Llm. Spans, or, like Langchain spans to Jenny. Convention like is that the conversion that's happening here.
or is it more about like, we'll give you some helper methods you give us the information what it needs, and it can
generate an Gen. AI compatible span and give you that
like, is it the 1st or the other? Because the second one I can see it's very helpful in a way like where not everybody has to kind of write them if you are writing your own
like converters and per se, right. But then, if you're doing the 1st one, then I would.
Then I had some other feedback. Whether what should be the right place for it.
Ridhima Satam 00:43:39 Yeah, I think we are trying to do the second part like, but we are demonstrating no way Langchain could use it.
Ankit 00:43:46 Got it. Okay? I think, yeah, definitely. I think that's a nice idea. I like it.
Thank you.
Ridhima Satam 00:43:58 Yeah, that's that's all I had to show.
Thanks.
Liudmila Molkova 00:44:02 That's actually wonderful. Thank you for working on this.
Sergey Sergeev 00:44:07 Yeah, please, Redima, also post this pull request to the swap channel. So I know I have to do my due diligence to post this document. I have already
creatures of the design and the diagram, but
I think we can even start commenting on it
earlier, like on Newman. And it said.
Liudmila Molkova 00:44:36 Is there again the same question as to is there any reason? It's not against open telemetry.
Sergey Sergeev 00:44:46 Say it again, not again.
Liudmila Molkova 00:44:48 Could you send the Pr against the pantolemetry?
So it's more discoverable. Right? We, we can definitely comment on this. It's just. There will be more people who are aware of this work.
Sergey Sergeev 00:45:01 Yeah, let me
put some sketches of the design in a Google Doc and connect it to the pull Request description, and we will redirect it to the upstream.
Liudmila Molkova 00:45:16 Yeah, thank you. Sorry. I jumped ahead of you. You had your hand raised.
Aaron Abbott 00:45:20 That's what I was. Gonna say.
Liudmila Molkova 00:45:23 Sorry.
Aaron Abbott 00:45:24 No, no, you're good.
Liudmila Molkova 00:45:31 I. I have not been doing my note taking
duty. And I'm trying to catch up.
okay. So moving on to some discussions, open discussions we have on the attributes and events for requests.
I really appreciate folks who took a look. And Alex and Samuel left a bunch of
comments are, so
I'm not going to dismiss any of them. But I would like us to focus on a few.
and the 1st one I outlined is the skeleton right?
So here, I think, Alex, you're asking whether we can
keep the skeleton without the content when content is disabled.
Alex Hall 00:46:46 I'm not necessarily saying we need to. I'm just saying it. It. They felt like
this needed to be clarified because a it was a change that hadn't actually been
noted as a change. And B, because this Json Schema made it seem like some parts were optional
in a way that felt like it vaguely hinted at this.
Liudmila Molkova 00:47:10 I see. I understand there was a change. It was not described on this.
This is a good
idea to describe it. My position here is I. I intentionally made this change. I don't think the skeleton in this shape
and form is particularly useful. It's still huge, though.
Alex Hall 00:47:38 I mean, am I right that you know
at this point there's no need for the spec to even make a decision like
if if some instrumentations decide to record a skeleton
that's up to them like, is it?
Backends have a decent chance of understanding them, but if they don't, they don't.
It's not like it's it's worse than not recording it at all.
Bye.
Liudmila Molkova 00:48:10 So my my main concern is the default. Right? Let's say I'm just enabling Jenny instrumentation by default.
And now, even though I didn't enable content.
I get tons of data that doesn't contain that contain the data.
The interesting data.
Alex Hall 00:48:31 Alright. So I guess you're saying that like instrumentations should, as a hold.
prefer to not record the skeleton, because
the same instrumentation might be pointed at different backends, and some backends will
deal with this worse, or charge users more for it, or whatever.
Liudmila Molkova 00:48:50 Right. And I think there is a value in skeleton, but maybe a slightly different one.
and I don't have the good format for it in mind.
and it's something that we can always tackle incrementally.
Alex Hall 00:49:18 Okay.
Aaron Abbott 00:49:22 Alex. It sounds like the pydantic instrumentation would like, you want to continue doing. This is could you talk a little bit about the use case, or you're not that opinionated about it.
Alex Hall 00:49:33 We currently record a skeleton we don't have a different way of.
you know, showing that it called, at least not within the
particular Llm. Request in Agent one spans. We don't have a way of showing the tools called. You'd have to like. Look at the
the spend themselves. Which maybe is enough.
Liudmila Molkova 00:50:04 2 courses where it contains something useful.
but you should also have the execute tools spent, at least sometimes.
Alex Hall 00:50:14 Yeah.
maybe there just isn't enough reason.
But it's again, I'm not saying that we we absolutely need to have this.
It just seemed like a notable change.
And then, if if you know, we're going to go for
not having a skeleton, that it seems like the Json schema probably shouldn't be marking the arguments and responses as optional.
so I don't know why there would be.
Liudmila Molkova 00:50:49 I see what you mean, because they you can have either message or do call.
But I guess yeah, we we could make another pass on them.
Alex Hall 00:51:03 Well, the pots already. Take care of this, don't they?
Liudmila Molkova 00:51:08 The parts are distinct. So yeah, but you're saying within the parts the thing should be required.
Alex Hall 00:51:16 Yep, like there's a tool call part, and it has arguments optional, nothing else. There is optional.
Aaron Abbott 00:51:26 So the only thing I would say is, if we market like, if we want to do this incrementally, and we market required to start. It makes it much harder to evolve to not have it, because the people producing the telemetry need to to update it right
or sorry consumers would would expect it to always be there, but producers would stop sending it.
Alex Hall 00:51:51 The other way is also not
a very smooth evolution. If you suddenly start requiring it.
Aaron Abbott 00:51:58 Yeah.
Liudmila Molkova 00:52:08 Think we will end up in some form of some middle ground.
and it might be a different
I don't know. Maybe even different attribute.
Is, people wanted to have a distribution of tokens. For example, when tokens arrive
you can record it as a metric. But if you kinda want to know. Okay, for this span.
There was a huge pause in the middle between tokens.
There were ideas to report. I don't know. Obfuscated content or empty 5 or something.
And there were a lot of ideas. I like them all.
I feel like we are not ready to make a decision on this one.
and we I would like us to leave the room for evolution.
And my soft preference is to
say, Okay, we just don't record it, and then come back to the attend, perhaps define
either a different default or
yet another opt in mechanism. To opt in. Into this level of details, right. The
the opt-in can tell you more than okay, nothing or everything. It can tell you something in the middle collect summary.
Alex Hall 00:53:38 Okay.
Liudmila Molkova 00:53:48 Yeah, thanks, Aaron, for typing it.
Okay?
So I will follow up. I agree we need to call it out. And I I will do my best on this.
Alex Hall 00:54:12 I think the other big thing there was the
input and output messages on agent spans.
Liudmila Molkova 00:54:20 Yeah, yeah, thanks for bringing it up. We've been chatting with ankit yesterday about the same one. And I agree that input and output is not the great
terminology, because you have, like the 3, the trivial example is, let's even use open AI responses api.
or assistance it
in the response in the output. It gives you information about which tools it called on the service side, like code interpreter file search.
It's an technically an input, but it's some intermediary steps that resulted in this output. And that's just their way of letting you know it happened.
And we would like to record this information.
But it would technically be part of the
input or output. It's not clear.
So
the suggestions Alex, you left it seems you would rather see inputs and outputs merged together in one giant
list. Is it the case.
Alex Hall 00:55:36 I I that's what we do for Agent Walk. That is what we do in general.
in the sense that we take.
We emit events in the current spec, but actually by default, we take those events and bundle them into a single array as a span attribute.
It feels like something like that makes sense, especially for the agent, run where they are intervened
like actual input messages from the user or something
alternating with output messages from the model. Just one messages away, feels right.
What you're saying about the
like remote tool calls does also feel like it supports that as well. A little bit
like, what? What is the separation even for? Is it? Is it to make it just slightly easier to like?
Get the output one is like
as in if it was all within one attribute, you'd formally still usually be able to just get the last message. But I guess if there were multiple
things like tool. Remote talks happening. Then you would want that separation.
Liudmila Molkova 00:57:09 Yeah, I see some hand raised. I would like Iron house first.st
Aaron Abbott 00:57:13 Yeah, I I'm I'm not gonna respond to Alex. Because it I wanna I just wanna make sure we're scoping this like, is the conversation specifically for agent history? Or is this applying to the inference, spends as well.
Liudmila Molkova 00:57:28 I would like us to have the same attributes. It would be very unfortunate if we had different.
Alex Hall 00:57:34 It applies to the influence guys as well.
Aaron Abbott 00:57:38 I mean the like. There are inference Apis, where the that look pretty much exactly like the format we proposed right like
I thought I thought the feedback was that the agent may do multiple calls. So it's input and output
would actually be different from the like perspective of the caller. Right?
Alex Hall 00:58:02 I do think that in the inference case, if, like the 8, if the model is calling, you know code interpreter, or something
internally, remotely.
That's still all part of output. The the Gen. AI system as a whole, like the open AI back end
is doing these things and producing these results. They're not coming from the user or client
like the inputs to the model in some in some cases. But the outputs of the back end as a whole
of the server of Openai, or Provider.
Aaron Abbott 00:58:46 I guess I was thinking more of like the so even like a 1 shot kind of use case like the I like that. The format proposed works for both
one shot or like conversational. But
yeah, it would be nice if they were the same. I agree.
Liudmila Molkova 00:59:07 Yeah. Ankit. Do you wanna go next.
Ankit 00:59:10 Yeah. And I think, touching on what Alex and Aaron said, like
the tool calls that an agent make is something. Yes, the agent produces.
And are those things that we show to the user as an output, or they are just considered as an internal working of the agent to give you a
a response at an output right? Something like going from that angle like where we lean towards.
I don't know if that can help make decision. And the I think the other thing that
yesterday was around.
if you do that, then are we duplicating that information both on inputs and outputs. And then, as the tool executes, it's gonna generate those plans as well. Right?
so how do we kind of
possibly not duplicate that, because and I think you educated me. That duplication is a real concern as well. Right
because of cost.
So it's just like large amount of telemetry.
Liudmila Molkova 01:00:25 Have we? We are at time.
Alex. Do you want to make the final point? And then we will need to keep discussing it, and they will keep thinking about it.
Alex Hall 01:00:36 I was just thinking that you could argue that even in.
even if, like, everything is happening locally on an agent run.
you could say that the 1st message is the input and everything after that is output. If, like the agent, if the AI is just like going in a loop of
quoting tools until until the final thing, all of those
calls and so on, could be classified as output
in the same way that when there's a remote agent, and it uses a code interpreter or web search
that could be considered output by the backend.
Liudmila Molkova 01:01:09 Yeah.
We need to stop here.
I keep thinking that input and output just wrong words. We need to find better ones.
let's talk about it. Next time I'll try to come up with some proposals. Thank you all for the feedback. I really appreciate it.
Aaron Abbott 01:01:32 Thank you. Later.
Liudmila Molkova 01:01:33 Thank you.
Ankit 01:01:35 Thank you. Bye.
