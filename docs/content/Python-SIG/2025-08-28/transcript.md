SIG: Python SIG
Date: 2025-08-28
Duration: 69 minutes
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:04:33 Hello, everyone.
Shuwen Pan 00:04:38 I don't know.
John Scancella 00:05:17 Hello!
tammy.baylis 00:05:24 Hello, John.
Liudmila Molkova 00:05:48 Hi, everyone.
Riccardo Magliocchetti 00:05:53 Finally.
So, welcome, everyone, to this week's Python Seek call. We'll wait just…
A few more minutes for more people to join.
And in the meantime, please add yourself as an attendee to the sign notes.
And… also, please add any last-minute topics you want to discuss?
Thank you.
Okay, I think we can start.
So, the first topic for today is…
from Tammin, about the new leveler.
tammy.baylis 00:08:18 Yeah, thanks, Ricardo. So this is something I talked about, I think, two meetings ago, where I wanted to introduce a new
utility to let us add custom attributes to, metrics, specifically HTTP server metrics is what I'm interested in. So, at requests two meetings ago, I created this new issue.
I looked up the semconv, and this should not conflict with anything explicitly stated in the semconv, and I did check to see if
Custom attribute writing would be possible with baggage, and…
I… I think technically it could be, but it seems to be more complicated with baggage than with adding a new utility.
So, yeah, this is… this is the new issue with all those things I looked up, and …
I have a PR out. It was my draft prototype before.
But now, now I think it's ready for review, but I do realize it's a little big. So it's 1,500 lines, but most of it is test…
adding unit tests, the label… and it can be divided into, I guess.
six main changes. One is adding the labeler utility that uses context bars, and the other five changes are, support for the labeler in five instrumenters. And we have a lot of topics today, so I don't want to…
go through the whole thing with everybody right now, but, like, I'm wondering, especially for more, I guess, senior approvers and maintainers, does this look like it's reasonable to review, or would you like me to split it up?
Riccardo Magliocchetti 00:10:30 I think I need to take a look before giving you an answer.
But, like, if the implementation is straightforward, Let's, like, give me, like…
Sometimes to take a look before, like, Give me.
Like… Like, I don't think, spitting would be required, but…
I should take a look before giving you a definitive answer.
tammy.baylis 00:10:56 Yeah.
Yeah, that's totally fair, and I appreciate it.
Yeah, it's, … it feels big, but it's not… I don't know. I'll leave this… I've marked it as ready for review. I should put it on one of the project boards, actually, for the PRs. But yeah, please take a look, let me know what you think. Thank you.
Riccardo Magliocchetti 00:11:19 Thank you, Tammy.
Any other comments?
Help.
Liudmila Molkova 00:11:31 A quick comment on this. I've just been in Java declarative config call, and we were discussing a very similar thing, but for the other side, the client side.
Where you would label, metrics or any other things.
…
on the client side was, let's say, if the IP address was 123, then we would set the peer name
Sorry, service.peer.
To something, and would populate it on the client metrics.
I'm not saying anything needs to change for this PR, but see, it seems there's a generic problem of how to add
arbitrary… Attributes to metrics before they are reported, not after.
tammy.baylis 00:12:28 Oh, thank you. Yeah, I was aware that, Go had something like this, like, very generally, but I didn't know about the Java client metric, so I'll be sure to take a look at that.
Liudmila Molkova 00:12:40 I'll post the pull request. It's actually in semantic conventions, I'll post it in the, docs, in the meeting notes.
tammy.baylis 00:12:51 Sorry, which meeting notes? The,
Liudmila Molkova 00:12:53 This one. I mean, right here. I will find the link, and I'll post it in the meeting notes here.
tammy.baylis 00:13:00 Oh, oh, right. Thank you.
Liudmila Molkova 00:13:03 Of course.
Riccardo Magliocchetti 00:13:10 Okay, thank you.
Next topic is from, Ridima.
Ridhima Satam 00:13:19 Yes, hi. So this is the PR for the line chain, LLM span invocation, and yeah, that's the… in the description, you see what you get on the span.
I have this comment, yeah, from Ricardo. I want to talk about that. If you go down, there is this comment.
Actually, two comments, but the first one is…
… there was this test I added, and I… first part I did, move it to fixture, so that we can use, different types of models. So, right now, when I tested it for the first time, before this comment was with OpenAI.
And then, when I tried with the Bedrock or Gemini models, what I see that…
Some of the attributes are different.
So, like, when you fetch it in the lang chain.
The attributes could be… I have given an example, so it could be in the… for OpenAI,
It is, like, model underscore name.
or for AWS Bedrock, it could be model underscore ID, so that is not supported, in this current implementation to fetch that attribute, and Gemini could be model. So if we… if we use these models, the model… request model would be empty, like, there won't be anything in that.
So my question would be here, like, why this inconsistency is there, and how do we fix it? Is this the responsibility of the… of… of…
People, like, who are supporting the instrumentation.
To accommodate all of these models, because it's going to be random, like, everyone will come up and add their attributes in the library.
they have, like, the… the Langchin…
Google Age and AI, or the bedrock.
They are not consistent, so either we should ask them, push it to them, that that should be consistent.
So that we can support it. What do we think? What do you think?
Riccardo Magliocchetti 00:15:24 I can tell you that when implemented, instrumentation for the…
Bedrock APIs in the Botoko instrumentation.
Since it's just a thin wrap, over the… …
model providers' APIs. Like, every models have different attributes and API.
parameters?
So, yeah, I had to add quite a bit of, … Ifs and conditionals around, …
Staff in order to support, like.
To precisely support, what they expect.
And not, you know, I have issues with modest, …
I didn't know about, or stuff like that.
So probably, like, on our side there, we can just say…
if it's not, an OPI model, just don't do…
The instrumentation and stuff like that.
But, like, I asked to, like, generalize the finger to avoid that… …
not that I want to… we should support every model available, but just to test that we don't crash if we get another…
a different implementation, but it's not OpenAI, so it's fine.
To not instrument.
But it's also, like, kind of required to not crash.
If it's not OpenAI.
I don't know if it answers.
Ridhima Satam 00:17:07 Okay, so for now, do you think it's a good idea that we skip for now? Because I have tried two providers, I haven't tried others, so how do we want to go about this exercise? Do we first just skip it, unless it is OpenAI?
And I thought.
in this PR itself, and then be safe about it. Is that a good way to do?
Riccardo Magliocchetti 00:17:29 I don't raise the right. I don't….
Aaron Abbott 00:17:32 Yeah, just to make sure I understand, it sounds like… the…
instrumentation introduced here for the prompt and response logging, …
sorry for the prompt or response capturing would kind of be dependent on it using OpenAI, so it's… like…
It sounds like this lane change instrumentation is a little bit coupled to that, is that right?
Ridhima Satam 00:17:55 looks like, looks like, because for, like I said, right, AWS, Bedrock, and Gemini, when I tried, the parameters from where the model ID, model request model fetch could be different for other providers. So either I have to add, like, if else, if this is the model, if that is the model.
I mean, sorry, provider, then fetch the model from this. And it could be for other para… other attributes as well, you know?
Aaron Abbott 00:18:21 Yeah, yeah. I mean, it seems like we might end up duplicating some of the effort that's already in those instrumentations, so, like.
I know, for example, that if I use the OpenTelemetry Instrumentation Vertex AI package with Langchain, it already does do the capturing, but it does it at a lower level, so that…
this stuff kind of just works, but, like, I know we've been back and forth on, if it's useful to have it captured in the orchestration layer, like in link chain like this.
… Yeah, I don't want to block it, but it also seems like
Kind of the abstraction is leaking a little bit, right?
Ridhima Satam 00:19:00 Yeah, so what would be the good way to do, like, like, right now, just skip other providers, if we find it's other than OpenAI for this PR?
And move on.
Aaron Abbott 00:19:15 I mean, what's… what's, like, your long-term plan for this instrumentation? Like, do you… do you want to support many of them? I mean, it seems, …
like, what would be the follow-up here if we just did OpenAI?
Ridhima Satam 00:19:30 We can have, like, follow-ups for the other providers, and try some multiple providers after this PR part, like, if we can open a ticket for that.
And try to see some, like, a bunch of providers if community agrees on, and then we can, then support, like, maybe the few or whatever we have agreed on.
For this land chain.
Aaron Abbott 00:19:56 Yeah.
Ridhima Satam 00:19:57 That's what should be fine, right?
Aaron Abbott 00:19:59 Yeah, I mean, I feel like…
I feel like, for me, I would probably prefer to just do the underlying client library instrumentation, and then not even capture it at all in Langchain, because it seems like it's…
not, generalized enough that it's providing much value. At least that's what I'm kind of hearing here, but…
….
Sergey Sergeev 00:20:25 Yeah, I would make it probably opt-in.
When you can opt in, enabling these additional attributes,
If you want to, maybe disable it by default.
Aaron Abbott 00:20:43 Yeah, Lamila, you wanna jump in?
Liudmila Molkova 00:20:46 Yeah, I want to echo, Aaron, your, your question.
Why are we doing this instrumentation at all? If we need to implement every provider one by one, what is the goal that you're pursuing? Why do you want it and not just tell people to use instrumentation for the underlying library?
Sergey Sergeev 00:21:07 Yeah, LAMChain basically will provide a link chain view, so you will see the framework when we add support for all of the LAMP chain constructs, like workflow, tasks, and etc.
and OpenAI course, you will see it, all from the… … framework.
View, and you will see it in the framework concepts.
So… the idea, if you…
have just OpenAI, codes from OpenAI instrumentation, then it won't be connected in that execution, graph.
What was it?
Liudmila Molkova 00:21:52 Absolutely. So if we want a different layer, like the workflows and tasks, let's go for it. But this, this is the low, low level, right? This is just the LLM level. Do we care to instrument it in link chain?
Sergey Sergeev 00:22:08 Yeah, we do, and specifically it can be not only OpenAI, it can be, something else,
like, bedrock and so on, native library, so, I…
Think we may have no proper instrumentation for.
The client side, … like OpenAI. So, I think it still has value.
….
Liudmila Molkova 00:22:41 There is a trade-off, right? There is, you would effectively duplicate the work for every instrumentation you want to support, and then you're effectively committing to supporting more, like, all the instrumentations we have plus more.
Is it something that you're ready to do?
Sergey Sergeev 00:23:03 Yeah, we will see as we go, I think, if it will be more demand, if,
if it will be just OpenAI, Bedrock, and so on, if it will be something else, and if we can have those libraries, I think it should be
customizable by the end user.
That you can opt in, to have the view of one chain, one graph, especially if you have
specific… types of telemetry for one graph, if you want to troubleshoot just what was happening in your framework.
And then you may, want to have some out-of-the-box dashboards for OpenAI specifically, so it will be in just a different size. It's more a question, does it make sense,
to have that TOM and vacation out of the box. Go ahead, Aaron. Sorry.
Aaron Abbott 00:24:06 Yeah, I was gonna ask, is there, like, a general set of things that we can always rely on to look the same, regardless of which model provider you're using? So, you know, something that we could…
Capture is still at the link chain level, but doesn't require hardcoding a bunch of extra cases for different model providers.
Sergey Sergeev 00:24:28 Yeah, probably we need to document, what's specific to Lankchain. Do we see in AOM invocation?
In their abstraction.
Which makes sense.
Aaron Abbott 00:24:42 Yeah, like, I think… I feel like we're running into friction because the abstraction levels were… we're trying to…
… Capture stuff from a lower level at a higher level.
But if we… if we work with what's available, we know it's gonna be there, I wonder if we could get kind of the thing that you're saying, but…
I still think it would be duplicative, like Nilo was saying, But, …
Yeah, it just… it feels like a lot to have special cases.
for… for each provider, because I know, for example, like.
It goes pretty deep. For Gemini, I think you can have…
like, arbitrary extra fields, so, like, the safety ratings that it returns in the model response, there's just, like, an any or whatever in the langchain data model where it's gonna show up, so…
Yeah.
And one other question was, what does the open elementary one do? Does it have special cases, or does it, …
Work at a, like, more general level.
Sergey Sergeev 00:25:40 Yeah, let's make it an action item to see in details. Sorry, Edima, do you want to say?
Ridhima Satam 00:25:46 Yeah, for L Elementary, OpenL Elementary, I just saw for OpenAI support. I didn't see any FL cases, unless anything… just, they updated recently, but…
Nothing that I could see.
Aaron Abbott 00:26:00 Okay, … Yeah, so then to move… to move this PR forward… oh yeah, Ricardo, please.
Riccardo Magliocchetti 00:26:08 Oh, no, please go ahead.
Aaron Abbott 00:26:10 No, I… I was gonna go on to the next step, so why don't you go ahead?
Riccardo Magliocchetti 00:26:15 Yeah, I was, like, proposing maybe…
Let's just maybe discuss on what this finance should look like.
And maybe try to understand if the current semantic already provides what we need to… To have, like, …
Higher level view of.
this LLM, LLM interactions? I don't know.
Ridhima Satam 00:26:51 Okay, so to summarize, like, can anybody summarize, like, what's next for the PR? Like, how when… how can we unblock this?
Aaron Abbott 00:27:05 Yeah, it sounds… it sounds like we kind of just have to decide if we want to just support OpenAI here, or if we can… if we're going to be a little more opinionated and pushback.
I'd say people should just instrument at the model level.
…
I mean, I think that would kind of be my preference, to tell people to instrument at the model level, and then just capture the orchestration level stuff within Langchain, but…
I mean, I'm assuming you're bringing this because you have a, like, a specific use case for this, right?
Or, or it's… it's, like, super important.
….
Ridhima Satam 00:27:38 Yeah, true. How much….
Aaron Abbott 00:27:40 Yeah, go ahead, please.
Ridhima Satam 00:27:41 I was just saying, like, we are just trying to support line chain, and we can… instrumentation, right? And we can add up on that, like, how… how we want it.
Right now, it's just LLM invocation. We would add different tools and chains and other features of Langchain as well, and along that, like, we can add more as the requests come for other providers also. Is that a good plan?
Aaron Abbott 00:28:14 Little, were you gonna say something?
Liudmila Molkova 00:28:16 Yeah, I was, like, there are two reactions I have. The first one, it seems the value, the largest value is not in the LLMs, like, the link chain instrumentation. So it might make sense to start on this higher level, and then you would get way more
Understanding from this, if the lower level is needed.
I don't want to, block the lower, lower level.
…
I have very little confidence that it's useful. If we want to implement it, and the Python maintainers are on board with this, then I think the plan forward could be that
We start by supporting OpenAI. We have tests, unit tests, whatever tests, to validate that it does not
Fail does not explode with other providers.
we intentionally don't put the way… we intentionally put something into the parameters that are… don't follow up an AI API, and then we test that it doesn't fail, that's it.
We should look into how TraceLoop does it, and …
If they have, or open insurance, and if they have some safeguards in place, if they have some good approach.
We can try… doing the same.
it sounds like it addresses the Ricardo's concern on the PR.
The main question is, why do we see value in doing this, and are we ready to do it every time for every provider?
Aaron Abbott 00:30:07 Yep, I just want to echo that, like, I… for me, I don't personally see the value, but I'm sure that we're bringing this for a reason, so if you can help under… help us understand that, I think we can
either move the PR forward, or decide that it's not important, and just focus on the orchestration stuff.
Sergey Sergeev 00:30:27 Okay, sounds good. So I think we can show, basically, how, LM anniversation brings more value for more than just OpenAI, maybe OpenAI AWS Bedor.
And have unit tests, to show
how it works, and second, what happens when we have OpenAI, instrumentation installed, to make sure that we
Do not fail that, test, right? Or….
Liudmila Molkova 00:30:58 Oh, no, so what I meant is the link chain instrumentation should not fail if link chain is used with
Bedrock, or something on Tropic.
Sergey Sergeev 00:31:10 We can definitely do it.
Liudmila Molkova 00:31:12 Yeah, the… it will definitely be duplicative with OpenAI or Bedrock. We have instrumentations for both, right, or vertex.
It will… it will be duplication, people will hate it. So the reason to do this would be that, okay, people can just install link chain instrumentation.
And then they don't need to know about OpenAI. But they inevitably will get a
less observability with Langchain, because it's the higher level, you cannot possibly know everything that OpenEI SDK does. And you would run into the issues. People will tell you, okay, we have duplication now, how do we disable yours?
But we want to keep orchestration. We want to disable just the LLM layer.
…
So, you should be ready to these concerns, and I think that this layer should be, even if we do it, it should be either opt-in or opt-out.
It should be possible to disable it without disabling the important parts.
Sergey Sergeev 00:32:17 Sounds good. So, let's focus on trying to provide, basically, two different, providers, like AWS Bedrock and OpenAI, to show how it provides the same telemetry, and second, provide some opt-in, probably.
Option to enable it, …
So we don't duplicate if our level instrumentation exists, and third, provide some ideas on how we try to
do it automatically, and on the value, right? So, why it may be… Needed at all.
Liudmila Molkova 00:32:58 That, that's… the last one is the most interesting to me, yeah.
Sergey Sergeev 00:33:02 Yep.
Okay, it sounds good.
Ready, man, do you have any… Feedback from usage.
Ridhima Satam 00:33:14 No, so the opt-in, one thing is, like, the opt-in is, like, do we have to add, like, a flag or something? If anyone wants to opt out from the LLM or instrumentation, they can just opt out?
just the LLM invocation part.
Right?
Is this how we can provide it?
Liudmila Molkova 00:33:33 This is one way, checking, there is a generic way to do it, I'm not sure if it's implemented in Python yet. Maybe Python maintainers can help me. Is there a tracer enabled? Is… oh, there is no declarative config, and there are probably no tracer-enabled thing, right?
Okay, so then, …
My personal opinion, I would wait with this flag. You don't have an orchestration layer yet, but when you add an orchestration layer, that would become
A good question on how we let people use one layer or another.
Riccardo Magliocchetti 00:34:26 Okay, thank you. Any other comments?
And also, please double-check the notes, because… It's this complicated discussion.
Liudmila Molkova 00:34:40 Thank you for capturing them.
Riccardo Magliocchetti 00:34:50 Okay, also thank you to… You're the person updating that?
Okay, then we can move to the next topic from John.
John Scancella 00:35:01 Hey, y'all, just, trying to continue to be, helpful and learn at the same time, so, I was thinking I would just run through all of the documentation that we have and read the docs and, you know.
See if there's anything that needs to be fixed, and if so, try and work on it, but just generally wondering, is there… is there any area that, like, you guys already know, hey, this… this is kind of, like, messy and could use some help, or…
No, just, you know, take a look and make sure it all looks good and is understandable.
Aaron Abbott 00:35:40 So, were we talking on Slack before, or am I thinking of something else?
John Scancella 00:35:46 Maybe? I, I know I was talking, with, …
sorry, with, … with Tammy earlier on Slack about… I was having issues with, getting the dock stuff to work, but that was a different, merge request.
tammy.baylis 00:36:08 Yeah, yeah, we talked before. Sorry, go ahead, Erin.
Aaron Abbott 00:36:12 Oh, no, no, no. Yeah, I was thinking of somebody else, I think, but…
So Tammy made some improvements to, kind of, the explanation of how to deal with forking in OpenTelemetry. I think that's a big area where we had, like, a lot of open bugs.
Some existing documentation, and some of the, kind of, just institutional knowledge was on the bugs, instead of written down nicely in the docs.
…
So, so there's also, like, some of the docs live on the OpenTelemetry.io website versus the actual docs in the, …
sorry, first the actual docs on the Read the Docs page, which are more like API docs from… taken from the source code and stuff. …
So, John, were you, ….
John Scancella 00:37:01 Yeah, I'm open, right? Like, I'm just kind of looking to give back and, you know, improve things, so if, again, kind of, if there's something you want me to work on, I can be helpful, like, I'm more than happy to work on whatever.
tammy.baylis 00:37:17 Yeah, John, I'm gonna, add some more links to the meeting notes we're all looking at right now. Yeah, Aaron already mentioned that, the otel.io, docs could really use some improvements, especially around troubleshooting Python, so that's one link. And, …
If you'd rather touch, like, the read the docs docs specific to the Python repos, there are open issues in both the OTEL
OTel Python repo, and the OTel Python Contra repo, which is more specific to instrumentation, so… …
Yeah, if, if there's, like, a relatively… we… we don't, sorry, disclaimer, we don't have enough resources to do too much ticket triage and organization, so, it's gonna be multiple links that I share, but yeah, if you see, like, a relatively recent….
John Scancella 00:38:18 based on that.
tammy.baylis 00:38:19 Okay, thank you. Any issue you're interested in, … any… anything helps, really, but yeah, I'll… I'll paste more links in the notes here.
John Scancella 00:38:29 Okay, cool, yeah, and feel free, you know, if you think of something in the future, you know, either ping me or, you know, whatever. I'm flexible.
tammy.baylis 00:38:39 Yeah, thank you so much for joining us.
John Scancella 00:38:44 Thanks for having me.
Riccardo Magliocchetti 00:38:50 Okay… My next topic is from Lydumila.
Generic change is config.
Liudmila Molkova 00:39:01 Yeah, so I wanted to chat about, some upcoming PRs. Dylan… I'm sorry, I'm not sure if I pronounced your name right. Dylan, or Dylan?
Dylan, yeah. Dylan, oh, thank you, appreciate it. So, you're working on the vertex, and I'm working on OpenAI. There are a couple of config approaches I want to…
To socialize. I don't know if we need a discussion on this, so we'll probably talk more about it in the coming weeks. So, maybe we can start with, your…
PR, Dylan, it's the least controversial … … So… I think that….
Dylan Russell 00:39:54 This PR, or one of the other ones?
Liudmila Molkova 00:39:57 Oh, the other, the other one that, the latest experimental.
Dylan Russell 00:40:03 Yeah, that one, I think, yeah. Okay.
Yeah, I can… yeah, so this one…
we… first, we add this GenAI latest experimental thing to the semantic convention stability flag, which, like, already exists.
….
Riccardo Magliocchetti 00:40:27 Huh, do you want to share, by the way?
Dylan Russell 00:40:30 … I can try to share…
Okay, can you see that?
Riccardo Magliocchetti 00:40:56 Yes.
Dylan Russell 00:40:57 Okay, nice.
Liudmila Molkova 00:41:03 Oh, I didn't notice you have a PR for Bose, I'm sorry, that's awesome.
Dylan Russell 00:41:09 Yeah … So this just adds the GenAI latest experimental thing.
to this existing… Flag.
And if they set, like, Gen AI latest, then they get… …
the semantic conventions that are… been added after 1.36, I guess?
It's That's where the big change was just made.
And… That's where we're, like, updating all the instrumentations to… To, you know… use.
And then the other change is… We add this, like, Content Capturing Mode Enum.
To say, You can choose between whether you want to capture, like, the…
the input messages and output messages from the LLM.
in spans, events, Both, neither.
And the plan is to use this existing environment variable, which before just…
Was to say, do you want message?
content.
from the LLM.
Or not, just like a Boolean.
… to be, basically, we're saying, if you… if you opted into the GenAI Latest.
Then, yeah, you choose between this enum now.
…
Yeah, so any questions about this… this change?
her thoughts.
And it's all in this GenAI Utils thing that just got added.
Sergey Sergeev 00:43:17 This is exciting for me, personally, because it's the approach we wanted to have to avoid duplication of this logic in instrumentation aware, and I really appreciate that you
Doing this work.
Dylan Russell 00:43:36 Yeah, thanks for adding the utils folder.
… Alright, so the other small thing that I did was… … just added… like… Data class types…
For… like, we have these defined in, like, the JSON schema.
for Gen AI semantic conventions, and now I'm just…
Adding them as Python data classes.
There's probably a lot of ways you could, like, do this. … But this seems like…
Okay to start with, perhaps?
…
Yeah, there is, like, a JSON schema Python library, which I was looking at this morning, but I couldn't, like, quite figure out how to use.
I don't know if anyone's used that, but….
Liudmila Molkova 00:44:59 What would you use it for?
Dylan Russell 00:45:02 Because you have the schema defined as JSON.
Liudmila Molkova 00:45:08 Mmm.
Dylan Russell 00:45:08 So….
Liudmila Molkova 00:45:08 I see. You would want to generate this from the JSON schema.
Dylan Russell 00:45:12 Yes, exactly.
Sergey Sergeev 00:45:16 Yeah, the whole idea was that, we, Try to separate… the actual telemetry from…
Basically, instrumentation-reported data, and the key idea was that here we will have some named attributes which we defined already in semantic convention.
So it's an internal representation, but also we can pass, some dictionary, whatever information we get from a call, for example, we can just dump it, in…
A dictionary which, other…
telemetry formats can use, even before we agree on how it will be named in semantic conventions.
That's the whole idea of these, data types.
Coas, … So, and so you wanted to… use, basically, JSON schema, … To create telemetry, right?
Dylan Russell 00:46:28 ….
Sergey Sergeev 00:46:29 Well, it's more how to convert the request and the response you got.
Dylan Russell 00:46:36 Yes. Exactly.
con… you would convert the request into, like, a Python object that you could, like.
Yeah, then type check using the JSON schema somehow.
Sergey Sergeev 00:46:53 Yeah.
Liudmila Molkova 00:46:55 And we can… In theory, I type checked, I'm using JSON schema.
And from… it seems it's still useful to have a common…
Python code that… you don't have to use it, you can use dictionaries instead, you can use something else, right? We don't care how it's internally represented.
But it's useful to have it, it's easier to… …
Use it in one instrumentation, and it also forces us to unify and avoid stupid mistakes when we do it in different instrumentations.
Dylan Russell 00:47:33 Right.
Liudmila Molkova 00:47:35 We… we might have…
Well, it's… like, the code that would create those would probably be specific to instrumentation still, because it needs to understand the original
Message.
Dylan Russell 00:47:52 Yeah.
Yeah, the conversion logic from… like… Whatever it.
The request and the response specific to the instrumentation to the…
To the format that we want.
….
Sergey Sergeev 00:48:11 Damn, … So, kid, Kid Daycare also,
did a similar, similar, POC… Change in our development branch.
Where we have that end-to-end, …
Link, so he shared the link, …
How he used the data courses.
Maybe we can interview session honestly.
Yeah, we definitely need to review this pull request, and we will do it and provide comments, so if you have an idea how you would prefer to do it, and if you can just
document it on the pull request, it will be helpful.
Liudmila Molkova 00:48:57 So one thing to understand about this, this is literally what we have in semantic conventions now.
So this is just the Python representation of what we already have defined. There are definitely maybe 10 different ways to
represent it, have serialization logic, I don't know, and stuff like this. But essentially, it will boil down to the same stuff.
Sergey Sergeev 00:49:22 Yim.
Yeah, it…
It will be a sum of the things for vector databases, for example, which we haven't defined yet, which have, … which we are defined in TraceWoop, for example.
So, instrumentation definitely has those attributes we can…
Leave them, unnamed dictionary for now.
And then….
Liudmila Molkova 00:49:47 I think we need to document them in semantic conventions, right? And then how to represent them
It's up to instrumentation.
Sergey Sergeev 00:49:55 And it's, it's unambiguous on what.
Liudmila Molkova 00:49:59 … almost unambiguous on what Python code you would write to represent them.
Sergey Sergeev 00:50:06 Yeah, but it will be still a lot of discussions, like, where do you put a response from
documents fetched, from a vector database and so on. I think it will be… LOMSIC will be always
We're getting some behind the actual implementation, for some of the providers, like TraceWhoop.
And the challenge, if we don't have a way to use this data…
Before we define semantic conventions, then a tracebook will never migrate to… vanilla OpenTelemet instrumentation.
That was the whole idea for this Python representation of the data.
….
Liudmila Molkova 00:51:00 So what you're saying is that, in some cases, you would like to define Python representation first, use it in the instrumentation, and then bring it to semantic conventions. Right, right. And by having single implementation in Python.
the single data type defined in Python and shared across instrumentations, we achieve some level of consistency.
Sergey Sergeev 00:51:22 Yeah, so the Python object will be shared across instrumentation,
when you report your telemetry to Gen AI OTS, you basically…
make a call, and all the named attributes can be the ones which are already defined. All the names, will be
just a dictionary, and, … We will have semantic convention, compatible, Telemati.
And we can version it, by the way, which is also…
A big thing, so we can have spanning matrix, telemetry of…
That semantic conversion version, and we can have some more experimental
span and metrics, for example, telemedic.
provider, I… I'm trying to… not to use a word.
Experture, because it conflicts with other OpenTelemetry concepts we need.
To find out how we name it. Again, I think it will be a more evolving discussion as we go. So, for this pull request, I think we will try to review it urgently today, tomorrow.
And just to provide feedback and share ideas how we did it.
… Devon, Devon, do you have any specific…
open questions except, how you map, your request to DataQuest, or…?
Dylan Russell 00:53:04 … I was able to update the Vertex AI instrumentation using these data classes.
… So I think the only thing is just, is there, like, a…
Yeah, is there a better way than… than this? …
Or is there some way so that when we update the JSON schema, like, we don't forget to update the…
the Python type.
Or some better way to, like, map between the JSON schema and the actual Python type.
But it seems… I mean, it works fine for…
what I have now, so maybe it's just fine.
Sergey Sergeev 00:53:52 Let us review it. Aaron, you have… Yeah.
Aaron Abbott 00:53:58 Yeah, I was gonna say, yeah, I think we need probably more tooling to generate these.
But that would probably be eventually something in scope, so, like, we already generate, obviously, constants for… from the semantic conventions, but this is the first kind of JSON schema thing we're including, but it would be great if these data classes could be generated directly.
But I think as a stopgap, just doing it how you did it is perfectly fine, or we could just add, like, a…
a script if you said you found a program that can generate the data classes from the JSON schema. …
I just… just listening to the conversation, I want to make sure
The… using data classes here and kind of having strong typing is not controversial to anybody, right? Or…
I wasn't completely sure on that point.
Okay.
Cool. And then it sounds like there's a good amount of duplication in this effort, like, between Keith
…
Dylan, etc. So, it sounds like the plan is to review the PR, and then work out how to deduplicate the effort? Is that right?
Sergey Sergeev 00:55:08 Yeah, yeah, it will be, yeah, it will be best. I'm glad that there are two people working on the same thing. It will bulletproof it from both sides, so we will make sure that
It serves… To both instrumentation side and, to the original design.
I think it's great.
Aaron Abbott 00:55:32 Okay, me too. Sounds good, thank you.
Dylan Russell 00:55:41 Alright.
Riccardo Magliocchetti 00:55:43 Okay, thank you.
Well, last topic is from Sergei.
True.
Sergey Sergeev 00:55:51 Yeah, this topic is more,
About telemetry sampling for asynchronous evaluation, and just brainstorming, wanted to get any ideas.
I think, first of all, do we have any telemetry sampling on the agent instrumentation side, approaches? Like, if you want to sample every 100th trace.
I know there is something on the Open Telemedic Collector.
In Golank…
Is this just, like, a general question about… Yeah.
Aaron Abbott 00:56:40 Pretty simply, yeah.
Sergey Sergeev 00:56:41 We'll start from general question, and then go deeper.
Aaron Abbott 00:56:45 Yeah, I mean, so, so OTEL has, like, you know, typically recommends doing a deep sampling, so, you know, there's this parent-based sampler,
So that's the default, is parent-based always-on, meaning that if there's no…
Sampling decision in the propagated context, it would… it would default to be on.
And then more likely, in practice, you would want to use this trace ID ratio one, so basically, you would set
You can't… you can't do every hundredth, but you could do, like, a, …
A probability-based sampling, and then… That decision will be propagated to all the children to sample the whole trace.
So that's kind of the main way it works, but then, yes, in the collector, if you want to do tell-based sampling, it's possible, with some big caveats, which is that
You typically need the whole trace to be sent to the same collector, so that you can do the tail-based sampling.
Sergey Sergeev 00:57:41 And collector means, go and, open telemet collector, right?
Aaron Abbott 00:57:49 Yeah, yeah, that's right.
Sergey Sergeev 00:57:51 So I'm… I'm just trained to…
think about, so, what if we want to do some sampling in the Python?
instrumentation, stack.
So… Let's even say we can deterministically select some same trace ID across RPC boundaries.
… let's say we have some hash in OG, so we select, one every 100…
Same trace idea across all the instrumented, … services.
And, let's say V…
try to evaluate, basically, we have some windowed aggregation of spans in the same trace ID.
So we can do, … Coordinated… coordinated evaluation of all the spans in this space.
Or probably we even… we probably don't even have to wait.
For a taste to assemble, and suggest…
Evaluate ever spent on the same trace idea.
Do you think it's… It's a good idea at all in instrumentation level.
Liudmila Molkova 00:59:26 I don't think it's a good idea to block your telemetry pipeline on evaluation.
Ed.
I mean, it would work on the toy application for demo purposes, but I don't believe it would work in the real life. I think you should do it asynchronously. You cannot let… wait for spans to… like, you cannot hold spans back while you're evaluating them.
Sergey Sergeev 00:59:50 Yeah, what are some of our friends in the market doing? They basically, in the agent, they select some of the spends and enqueue it for asynchronous evaluation.
Liudmila Molkova 01:00:04 That sounds great.
Sergey Sergeev 01:00:08 It's, it's more on the… Sampling strategy. Wanted to brainstorm with this group.
How can we do it?
So we select, I, I understand how we deterministically select, every…
100th trace ID, for example, using some predefined fashion. If trace ID is random, we will probably get roughly every 100th trace ID and all the springs in it sampled across
All the services, but… let's say we want only GenAI operation name, equal chat.
Anybody can think of, any approach.
How to sample every 100th of this.
Typically across IRPC boundaries.
Liudmila Molkova 01:01:04 I think if… if there… if you're doing evaluations based on the telemetry, then something independent, samples it, right? So it does not… it cannot really pay attention to GenAI operation name, because sampling usually happens on the incoming request, right? And if… but on the incoming request.
your application decided to sample it out, then it doesn't matter if there was an GenAI stuff under, right? You can, in theory, try to do very advanced sampling configuration that would ignore the parent.
And it would sample on the starting on the client span if it starts with GenAI, and it probably means very complicated sampling configuration for your users.
It's something to explore, but it's kind of hard.
Yeah, Erin, go ahead.
Aaron Abbott 01:01:58 Yeah, yeah, and just to echo that, like, this is… this was the kind of conversation that led us to having both events and spans to capture these chat events, was because the… you kind of want two axes… two axes of sampling, so, you know, even if your trace isn't sampled, you could still emit logs,
And it's not dependent on kind of the incoming request or anything like that. So for eval purposes, if you want to do this, it's easier, like, to do it in a flat kind of logging, logging sampler, right?
Liudmila Molkova 01:02:32 That's a great point.
Sergey Sergeev 01:02:33 Yeah, it's, one of those ideas, of course, it's, …
Just trying to think through with this group, if anybody has an idea.
on how to do it. And, the reason to do it, basically, let's say we want to evaluate all the LM and vacations,
In the same trace.
Across all the RPC boundaries.
In this case, the challenge is, it can be even not on the same OpenTelematic collector.
And it may be… Again, if we support both span attributes and, events for this type of,
GenAI invocation, …
the question is, if in instrumentation framework, in Gen AI, which use, with support of Evaluator, we can somehow select every 100
Threes.
And to evaluate every gen AI.
… Oh, I'm on vacation.
type, for example, or GenA, operation name chat.
I think we are approaching the end of time, or we are at the time.
I already did. Yeah.
Aaron Abbott 01:03:58 I would just say there's a sampling SIG, I think, Lamila, keep me honest, I think it's still going on, yeah, our sampling working group.
Sergey Sergeev 01:04:06 Oh, no.
Liudmila Molkova 01:04:08 I think, yeah, …
Yeah, I think they are going on, I'm not sure if they have a call, I'm checking really quick.
One thing you might be interested is, first, baggage, and second, trace date, but your application would need to say, okay, there was an AI operation in this call. From now on, either sample it in or, run evaluations based on this.
… But, yeah, let me see sampling.
Thursday at 8 AM, it was an hour ago.
Aaron Abbott 01:04:45 Yep.
Liudmila Molkova 01:04:46 Two hours ago.
Sergey Sergeev 01:04:49 Okay?
Yeah, this is really nice. Thank you so much.
Liudmila Molkova 01:04:56 Thank you.
Aaron Abbott 01:04:58 We made it through the agenda, so good job, everyone.
Riccardo Magliocchetti 01:05:03 Okay.
Dylan Russell 01:05:04 Alright.
Riccardo Magliocchetti 01:05:05 Okay.
Aaron Abbott 01:05:07 Alright, I'll see y'all next week. Later.
Riccardo Magliocchetti 01:05:08 Bye. See you. Bye, thank you.
John Scancella 01:05:12 Bye, everybody.
