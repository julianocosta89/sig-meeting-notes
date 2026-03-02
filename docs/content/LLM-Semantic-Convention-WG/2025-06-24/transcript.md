SIG: LLM Semantic Convention WG
Date: 2025-06-24
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/s_pGKn1fkuBX59jc9W0i7UTWAv-jloSQBBFqYhi8TqKTTSmayix7hpePTuS-CI_D._gqK-wrnc5QYVWCf
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 04:10 Hello! Everyone.
**Bruno Baptista** 04:13 Hello!
Sorry! I don't know if you are talking, but you are muted. We cannot hear anything.
**Liudmila Molkova** 04:33 Oh, so nobody heard me saying anything yet.
**Bruno Baptista** 04:37 I think so.
**Liudmila Molkova** 04:38 Okay, that's fine. That's why everybody was so quiet. Okay, now I get it.
yeah. Do you see my screen.
**Bruno Baptista** 04:50 Yes.
**Liudmila Molkova** 04:51 Awesome, wonderful.
Give me a sec.
Okay, so let's get back. So I was talking
like, please add your name to the attendees list. If you have a topic, please add it to the agenda.
Let's see how much we can cover today.
While people are still joining. Let's spend a few minutes on the backlog.
We don't do a great job maintaining it but hopefully, we can get
through some items today.
So I see one new issue.
I think there was a Pr. On this.
And the proposal is to add urgent pattern.
Do we have the author or Gwanya on this call.
No, we don't.
Okay, anyway. If you're interested I'm going to move it to the to do a
so there is a pull request. If anybody
has any thoughts on this, you're welcome to chime in. I left my comments.
There, essentially, it suggests a pattern to
add some information about the agent.
I have a lot of questions, and I think we need to talk about it.
It's the only new issue that we had.
We have a bunch of Prs in progress. So let's move on to the main agenda. So we can spend more time on them.
Okay, there are a bunch of topics from me
before we get started. Does anybody have something they want to bring up?
Okay?
So the 1st topic is, we are doing some open telemetry, wide planning roadmap stuff, and we would like to get some feedback from every seed on what they're working on what they're the plans. And if there are any areas
that we want General Gc, governance Committee, Technical Committee help on.
So maybe we can spend a few minutes thinking about the first, st what our big achievements during the past 12 months.
and just answer these questions, and I'll try to polish them.
So I think one of the big achievements are that we have some of the instrumentation libraries. Open. AI vertex
great
bedrock.
There was one more from Google. Is it called Gemini, or.
**Aaron Abbott** 08:46 Google, Gen. AI.
**Liudmila Molkova** 08:47 Oh, Google, Jenea.
this is from the instrumentation side, I think, from semantic convention site. We have added basic support for agents.
Hold on.
and well, it's still in progress. But we have the groundwork
or a better chat history representation.
Let's call it this way.
Does anybody wants to call out anything else in the achievements.
**Aaron Abbott** 09:52 I mean, maybe on the instrumentation side. I think we've had of
some adoption in open source from other things, not in contrip, right. So like. I know pydantic supports
the semantic conventions we have right now for inference bands.
I think crew AI probably supports the somebody. Keep me honest here, but I think it supports the
agent. Semantic conventions, etc.
**Liudmila Molkova** 10:17 Nice
cool.
Anything else.
**Bruno Baptista** 10:36 I think long Chain 4 J. Also has tried to align with these conventions.
**Liudmila Molkova** 10:43 They don't use a pencillometry right?
**Bruno Baptista** 10:47 Who luncheon for Jay.
**Liudmila Molkova** 10:50 Oh, Link, change for JI see.
and maybe spring AI as well, at least partially.
Oh.
okay. Anything else.
Okay, let's talk about the plans. Actually, I wanted to spend a little bit more time on the project planning, but it will be a good segue to the project planning discussion.
So what are our plans are?
I'm going to start first.st I think we need to finish the chat history work for sure. And it it. It holds us back
what do you think we should
do like? Bring their thoughts? We will prioritize and polish them.
**Sergey Sergeev** 12:29 Yeah, I thank you.
I have in terms of points. Unfortunately, we could not accomplish what we wanted to do in shorter terms. But I think it's extremely important to have that
Apis decay, or whatever for python, at least to be able
to to avoid repetition in instrumenters.
and to provide some library for other integrations like Om, different adapters and etc, which will
simplify new instrumentations. Development, and which will control what type of telemetry is emitted? Is it Meta and span mass type of same convention, semi-convention, telemetry? Or is it just spans and metics or just spans? In some cases? I think it's crucial to do.
It's early, so we can have more telemetry.
more open source projects emitting telemetry and simite convention.
**Liudmila Molkova** 13:47 Can. Can you help me understand? What what would the common, what would be in the common package? How would.
**Sergey Sergeev** 13:54 Yeah. Right now, for example, Openai instrumentation. Or let's say, one chain we are working on creates all the telemetry directly in the library. Let's say you
received one Llm. Start. You want to create a span, a metric end to end, a measurement end to end. So
and same happens for
length chain, or for other instrumentations. I think it's important to create that base class which will be
emits and telemetry, and provide some standard Apis to other instrumentation libraries.
So in your openai you just call on Lm. Start and provide all the parameters needed.
But that base class can control which type of telemetry it emits. Let's say you set up
you. You want to add works or events, or request response from the model
that by squad should control it, and the.
We should not repeat it in every instrumentation library.
Oh, this.
**Liudmila Molkova** 15:12 Okay.
**Sergey Sergeev** 15:13 And so.
**Liudmila Molkova** 15:14 It's more of an go ahead.
**Sergey Sergeev** 15:16 And second, so let's say we have 3rd party projects like white oem proxy.
Or let's say we have Ranksmith.
and it collects everything in internal telemetry.
but then, if we want to convert it to open selemnity, we should use this library.
So it provides a way to integrate more frameworks, beef, adapter style.
conversation, conversation, and even for tracewoop
it can emit telemetry. We just need to provide the library built and provide the library, which will simplify
those adapters to convert to semantic convention telemetry.
and we'll support all the forevers.
as we define. So in semantic convention.
**Liudmila Molkova** 16:10 So if I if I if I can summarize that, we would
like to have a simpler way of writing instrumentations less repetitive.
**Sergey Sergeev** 16:20 A simple way of writing instrumentations and a way to control which types of telemetry we need, because the reality is that some some providers will require
just spans and metrics, and some providers will require span metric and event telemetry.
**Liudmila Molkova** 16:43 Yeah. Yeah.
Well, we we can talk about it.
I would call your second point as a configuration. There, there is a big, open telemetry, configuration, effort, and essentially it allows users to configure their SDK. And what signals they need. It's not the instrumentation concern. It's more of an application concern.
Okay. Cool.
**Sergey Sergeev** 17:26 And one more, if I may sorry for taking so much time.
**Liudmila Molkova** 17:31 No no go ahead.
**Sergey Sergeev** 17:32 I think we need some standardized way to
to to design instrumentations that we can add some gen AI evaluators for telemetry in Runtime.
But
**Liudmila Molkova** 17:52 I think evaluations is a big topic. So we first, st we need
semantic conventions to record evaluation results right.
The second part is.
**Sergey Sergeev** 18:07 That's fun!
**Liudmila Molkova** 18:08 Alright, maybe running a vows on top of telemetry.
**Sergey Sergeev** 18:13 Yeah, yeah, basically.
And again, in order to do it, we don't want to code that elevator for specific attributes of telemetry.
We want something in between which will represent Lm. Conversation before the
translated to specific telemetry, and most probably that telemetry needs to be mutated. To add, for example, conversation, score or bias score to the event itself.
**Liudmila Molkova** 18:51 Yeah, I'm I'm adding it here realistically. I think it should be done in the collector. It should be done in one language. And collector, if you want to especially mutate the telemetry and offload the the work. But yeah, let's talk about it. Let's just list the
things we kind of want to work on and think we should prioritize. And then talk about details.
**Sergey Sergeev** 19:16 Later.
**Liudmila Molkova** 19:18 Anybody wants to add anything.
**Giovanna Carofiglio, Cisco** 19:20 Yeah, I would like to add the multi agent or agent to agent. observability. So there.
yeah, agent to agent, not not necessarily as as the Google proposal, but in general as agentic protocols and multi agent conventions. Yes, so there we would like to just mentioning this. But we. We have launched an open source initiative in Cisco. That
traceloop and and and pedantic and Long Chain Lama Index, I mean, many other partners have joined is is not an alternative forum for these discussions. So we're gonna come here and and propose. But we have started some work, and and and that we would like to start presenting, maybe next week on the
instrumentation, on a proposed extension for multi agent metrics on a connector for a gentic protocol instrumentation. And all of this will be releasing on a translator. So maybe I can share a few words about what our roadmap, and then we can go more in detail about what we released 2 weeks ago on the SDK.
But just mentioning, we know that this is a long term topic, and we're just getting started. There was Microsoft proposal last week. So it's just to to mention it. I think it's gonna be a
an important topic.
**Liudmila Molkova** 20:56 Wonderful. Thank you.
Yeah. Aaron.
**Aaron Abbott** 21:03 Yeah, I was also, I mean, I think we discussed last week with Microsoft about the A to a stuff as well, or just multi agent semantic convention. So
just plus one to that.
I also wanted to plus one what Sergey said. Like, I think right now, there's there's too much boilerplate for these instrumentations. So yeah, like making
making instrumentation easier and easier to be uniform, having some kind of.
you know, strongly typed wrapper. And then it also makes it much easier for us to evolve the conventions when they're shared. Code.
I did also want to say, add one of my own.
I think, in this, Doc. In the Doc you shared libel. You already have multimodal content.
I think it's a pretty natural extension of the chat refactoring that we're doing. It's pretty much hopefully, just adding a
specific new thing to the Json schema like it should be pretty much
no changes. I think there's there's obviously like the
the streaming protocols for multi multimodal, but just kind of the traditional.
you know, one shot calls to the Llm. I think we can can extend that pretty easily.
**Liudmila Molkova** 22:19 Yeah, that's a great point.
Cray.
**Pavan** 22:29 Is there any plans to actually expand the semantic convention for a single agent? I mean, right now, there is a notion of like the agent id, and so on, and so forth. But I think there could be a lot of other metadata that we can actually store that would be very useful. For example, what sort of
tools is the you know agent working with and you know, like many others so there is like some work that we are doing. But I was just wondering if, like expanding the scope of a single agent convention would be useful, because
it would slowly catch up very quickly.
I'm sorry. Yeah.
**Liudmila Molkova** 23:15 Yeah. So it.
I mean, we we can. We can plan it. It's it's at the same time it's a trivial feature that if somebody can put some leg work and
design it and bring it up. Implement. Do the prototype or something, and we'll we'll we'll take it
alright. So I I don't see why. Why not? But
at the same time, like the exercise I want to do after that.
is to actually ask people what they will work on right because somebody needs to bring things up
for them to materialize.
Okay.
So let's add this to call 2 definitions right
and
cool, so we'll talk about who wants to work on what
in a second let's spend a little bit of time on the last part.
I'm in the word spot. I am the CC member
so I'm biased. I kinda wanna hear from you. If you
think we need any support from General the Tc. Or Gc, like, what do we lock
here? And how we do? We need to any help from the community.
**Sergey Sergeev** 25:11 Yeah, I have 2 questions, and sorry we have a lot of interest on Cisco site on splunk site to contribute to open source project to this project. But we are new to the project. So we will need some help. 2 topics I have on top of my mind is vector database, semantic conventions? Is it falling into database? Or this group?
And second, is basically, do we have
for conversation support? Is it going
for for chat for chat. Sorry session, support, is it? Another
group? Or can we define some attribute which will represent jet session?
**Liudmila Molkova** 26:13 Good questions, the the the vector, the database group
is dissolved. Now we reached the stability. We will not,
do any database work. But if you bring up a pull request
for vector, databases that actually makes sense, then
I can review it, or we can
find other people to review it. I think we we
can't tackle it in the scope of general semantic conventions.
The rope, the chat sessions, I think, is directly in the scope of this group.
**Sergey Sergeev** 26:58 I. I think the idea was that it's basically something like a user session, and we
should keep it aside. But maybe I'm missing. Sorry if
I missed some conversations about it.
**Liudmila Molkova** 27:16 There is a general like RAM real user monitoring part where you have user id and session. Id.
I would imagine the conversation is a separate thing.
**Sergey Sergeev** 27:30 Okay. It's it's great to be.
**Liudmila Molkova** 27:34 Similar, yeah.
**Sergey Sergeev** 27:35 Okay.
**Liudmila Molkova** 27:35 But yeah, we probably we, we definitely will need to work with the browser and client folks to separate those. Well.
**Sergey Sergeev** 28:01 Oh!
**Liudmila Molkova** 28:04 The 1st point you mentioned is that you kind of want some onboarding either crash course or a body that would help you
contribute to the Python instrumentation.
**Sergey Sergeev** 28:17 We even in splunk. We have some maintainer. I think we have a Maintainer and even a server on Cisco
spoon converter team.
It's more Vfc. Mindy conventions. It will be great to understand, because Giovanna's team they worked on that agency project and we just connected internally a couple weeks ago. So we
trying to align our internal plan how we can make as much progress as possible. And how can we translate the agency
schemas.
They developed as part of that group to Lms Lm. Semantic conventions in this group. Maybe we need additional meetings or something with you, and probably aren't as the most active
participants in the group to help us understand what we need to focus and how to
what? What's already in simite convention. What's missing? What can be borrowed from agency.
**Liudmila Molkova** 29:33 Yeah, definitely, I would. I would recommend to take a look at the semantic conventions first, st right? And just do
just go through the docs here. They are structured. Right? So, for example, I don't know, Jenny, ice here databases. Or here you can
see how we normally structure stuff right, that we have some markdown files. We actually describe everything in Yaml
it should all be in the contributing guide. So I would recommend starting there, and maybe come up with some very early draft and then bring it on.
i. There is a lot of kind of art in the semantic conventions. There are some naming policies and whatnot. They are
like, 80% documented, 20% not documented. And I, definitely, I'm definitely happy to help. We have general semantic conventions all on Monday, 8 Am. Pacific.
We can definitely do one off sessions to go through some specific details. It's more like I would prefer to do it in public, so other people would learn
2 right.
**Sergey Sergeev** 30:49 Okay. Sounds good.
**Liudmila Molkova** 30:56 Wonderful
cool.
Anything else on the side them any help? Big
things we want to bring up.
**Aaron Abbott** 31:13 Yeah.
Oh, sorry
I I was just gonna ask. I know. I know you said you're biased and don't feel like you can.
You know.
I guess my question is like, what is the kind of stuff that Gc. Or Tc. Would help with? It seems like it would be.
you know, like prioritization, or, like, you know.
conflicts like either in the group or with other projects and stuff like that like?
What kind of problems would they be solving.
**Liudmila Molkova** 31:47 Well, if
my list would probably be that if we didn't figure out the complex support for complex attributes in the spec, if it wasn't on the way, it would be the technical concern I would bring to the
Tc.
From the Gc. I think we we should ask to finish the donation stuff.
the open elementary donation for lob.
**Aaron Abbott** 32:22 Yeah, I agree on that one.
**Sergey Sergeev** 32:24 Yeah, and we've open elementary. So the exercise we did for link chain. We just realized that we need that boilerplate library
basically to simplify conversion. We cannot. We cannot just do the donation
in as is so unless we accept that there are some attributes named like, trace, whoop, and so on. Yeah.
**Liudmila Molkova** 32:54 Oh, we! We were never going to do it as is right. We were never going to take it without modification.
**Sergey Sergeev** 33:01 But if we do the modification, it makes sense to do the boilerplate library first, st so we don't have to
to to repeat the same boilerplate. In each instrumentation we transfer.
**Liudmila Molkova** 33:24 Yeah.
And the other thing I think we can ask from the Gc. And Tc. Is the
help us with, not with the industry outreach. But what I think I see will be brutally honest that
while we are working on the up and telemetry is Jenny. I story. It is slow. It's inevitably going to be slow, because we need to be behind to create something common.
And it means to some extent that startups and companies that evolve quickly cannot fully rely on semantic conventions.
and it means that there are a lot of things out there that don't follow us or don't use up in telemetry.
And we, maybe it's more like a a question and feedback to this group that
we have different interests.
Some want to move fast and semantic conventions to cover everything.
There's like we are more conservative, and if maybe there is some
conflict within us, but we don't understand. We don't talk it through. It could be a community problem. So I'm curious if you feel this way. Yes, I'm.
**Samuel Colvin (Pydantic)** 34:56 I'm with you on as someone in a startup. I would rather that the conventions went slowly and were right than that they tried to go quickly and made the mistakes that are inevitable. Almost nothing requires like semantic conventions. So, in my opinion, there's quite a lot of stuff going on from startups and from big enterprise that really should be
like shouldn't be semantic conventions yet. I would much rather people came back and were like we've been doing this for 6 months. And we know this thing works. And we found all these problems, and we fixed them than like before we started doing anything. Here is the semantic convention. I know I made that point quite forcefully on the
buckets by, you know, big file upload stuff, and I felt that last week on some of the stuff Microsoft were proposing on interagent communications. Almost nothing like requires a semantic convention to get going right. You can go, and that's the whole point in the end. It's like.
you know, no schema dict that you can put whatever you like in. I mean, ignoring the like complex attributes. But you get the idea. And so I think, personally, I'm a fan of like being somewhat cautious about adding semantic conventions until you're sure they're right.
I kind of think the default answer should be, have you been using it in production for 6 months?
If so, then we can have a conversation about a semantic convention.
**Aaron Abbott** 36:23 Yeah.
Oh, sorry I was. Gonna ask like, what's what is the value of the conventions like, I think.
like, Sam, you're saying we don't need them to do anything. But I I suppose, in terms of having shared instrumentation like, if the ultimate goal is for every vendor to have their own set of instrumentations that implement their own conventions.
Then that's not. There's no point in having a standard right? So like, if we do want interoperability, and I'm not disagreeing with your points. I'm just trying to suss out the details of like, what are we doing here? What's the high level goal.
**Samuel Colvin (Pydantic)** 36:57 Yeah, I get that. And obviously we don't want different ones for everyone. But I think there is value in writing semantic conventions around the things that have settled, as in the fundamental, like
whatever you want to call it. Chat messages.
like protocol has been, is stable enough that we can have some anti conventions, and
I would, you know, push us to get them right, and and do the technical stuff to make them possible complex attributes, etc.
I'm not sure yet that anyone really knows about, like multi agent communications. And like whether or not we're doing like handoff or delegation and all that stuff. I think that stuff is still being figured out as a pattern in a way that, like structured outputs are not being figured out. We have things that we know work.
**Aaron Abbott** 37:45 Yeah, I agree. And I think, like working on the chat completions. The inference level stuff that we're doing now, like like you asked, has it been in production for 6 months, like, I think we have a good feeling on. This is our second iteration of it. I think we have good feeling on this, but agents are maybe a little bit further out like you said.
**Samuel Colvin (Pydantic)** 38:00 Yeah, some of the the like, at the risk of being critical, some of the like. Here are some semantic conventions. It looks kind of like physicists trying to work out the like
difference between a muon and a quark like rather than people using something that has been in like prod for 6 months. It's like exploring stuff in the form of semantic conventions doesn't seem
like a good solution.
**Sergey Sergeev** 38:25 Yeah, I I wanted to add my 5 cents to this. And the idea of instrumentation. SDK, based instrumentation. SDK, because this Api. So we know, for example, what python Pydantic or trace whoop.
instrumentation
is doing so. We know that there are some parameters you provide for every element vacation, for example, and sometimes we don't have semantic conventions yet.
And we can have multiple implementation of telemetry. We emit from that. SDK, so this way, we can go a little bit faster than semantic convention by developing those Apis control, and the version of those Apis and etc, add an optional
parameters to Lm invocation object, for example. And then we can emit, for example, pydantic telemetry style.
So this way you can develop Apis a little bit faster.
Then the Simite convention, and then you will have very specific example of
whatever the parameters I needed to create that vacation.
Sorry. And then you can basically catch up with semantic conventions.
Again, we need to prove this theory, but I think we can separate semantic conventions
from this python Apis, and so support different styles of telemetry.
Whatever kind of AI observability focused platforms developed over time.
**Samuel Colvin (Pydantic)** 40:26 Yeah, I mean, I I know that we're not like both us and trace loop claim to be following semantic conventions. And we're not entirely because there was some blurred.
I you know uncertainty about what you do when you can't have a complex attribute. Lots of other people do this like
normalization of like key dot key dot key. We do like Json Blobs.
that kind of stuff. It's it's totally, you know, we have enough information about what people are doing to fix fix that stuff.
And you know there's no real excuse for us and trace group to all be doing different things apart from waiting for complex attributes. Like, I say, the agent stuff is much less defined.
**Sergey Sergeev** 41:06 And yeah, yeah, go.
**Liudmila Molkova** 41:09 Yeah, thanks. So if we want to support different output formats, you can always do it in the processor or in the elector.
If the data is the same right? And then you don't need to implement it. Hmm! Like
complex hierarchies and all. All the post-processing stuff is already there for you to rename attributes.
**Sergey Sergeev** 41:32 The the challenge is that we know that request or response from Lm and vacation include that many values. So it's that much data you can extract, but we probably missing some of semantic conventions
for some of the telemetry here. But the key is that if we have that
SDK or library Api, which accepts all the possible parameters. It doesn't have to
to set all of them in simite convention, approved Format.
But we can have other telemetry like, we know that vector database has some attributes which are not defined in semantic convention yet, but we know they exist because pydantic or trace will make sense of them. They put it as a span attribute.
but semantic conventions have to catch up with time because it takes time to standardize. But if you have that library with Api. At least we we have a place to
integrate with other
Telemetry providers like Pydensic, and etc. And now we have a chance to get it adopted by broader group. Because if you have that boilerplate somewhere.
if we provide provide some benefits for 3rd party instrumentation developers.
if we make it easier than maintaining your own boilerplate.
Then we have a chance to broader adoption of semantic conventions.
**Aaron Abbott** 43:24 Is this a pattern that we've seen in opentelemetry yet? Because
I'm not like we've had, you know, a couple of utils and stuff. But I'm not sure if we've seen this kind of thing where
we enable people to emit different conventions really easily by giving them kind of
you know, like hook hook points and stuff like that, like I I think we should write it down like it doesn't seem I don't have anything against it. I'm just seems very new, right?
**Liudmila Molkova** 43:49 So the way the pattern? No, it's not the pattern. It's actually one thing somebody did a talk on. It's actually your colleague, Aaron Bartek Plotka, who is a Prometheus Maintainer. So Prometheus has a different format for metrics. Different semantic. Well, they don't have conventions, but they use different Format.
and sometimes. There is a metric that in output telemetry is called this way in in Prometheus it's called differently.
So we are working on the tooling
that should be able to translate one schema to another. It's also can be used by the backends to update the version of your semantic convention, like the the schema transformation. If you're familiar with it, you can update from version X to version x plus one.
And there's also enough metadata in the semantic conventions for you to do this. Well, sometimes there is enough
but essentially the the pro problems like taking some data and translating it from up in telemetry to something else. I would be thinking about something in the collector.
because it makes it. You implement it once.
and you made up in telemetry schema by default, but then you can translate it into other formats. And yes, it could be loose. Lossy.
**Sergey Sergeev** 45:15 To that the the biggest benefit of having it in Python, where? So we can
also block something which is not coded for specific
convention. Let's say you emit optional events as a request and response events, or you can put it on a span attribute. So now let's say you implement evaluator, runtime, evaluator
Library, which tries to evaluate those requests and responses in the runtime.
Now you have to support both telling me the types
instead of just expecting to have an object with some Apis, where you will have request and response.
like a field of an object instance which you can use before it turns into one flavor of telemetry.
**Liudmila Molkova** 46:16 Yeah, I think we can. We can discuss different ways of doing this. I kind of want to return to the project, planning a little bit and 1st
I think we were well into this discussion as well. So
one thing we're missing is, we
talk a lot a lot about what semantic conventions and Gen. A instrumentation should have. We don't talk about who will do it?
And I. People to sign with their blood to commit to some work, if that this is the good way to see if they really want it, or
it's just nice to have right so I'm
I'll be happy to put my name here.
So, Sergey, you're very excited about this one. Would you be interested.
**Sergey Sergeev** 47:21 Yeah, of course. Yes, and I think Aaron is
I I will be happy to F. Aaron as a body for this work.
If you have any availability to do that.
**Aaron Abbott** 47:44 Yeah, you can. You can put my name there, too.
Sounds good.
**Liudmila Molkova** 47:52 I feel the configuration part is related.
Yeah.
**Sergey Sergeev** 47:58 You can.
**Liudmila Molkova** 48:00 Aaron. Do you know if somebody is working? I think there is the prototype in Python, but it was created by Diego, and it's been a while.
**Aaron Abbott** 48:07 Yeah, it's very outdated. So this seems like the like. Python's a concern.
I think I would. I would probably raise it there, and you know, maybe we should put this in the we have the same discussion in the Python group, and maybe we should have it more publicly like this, but I think
maybe this is one I bring there. Does that sound
reasonable? Or do you think there's a specific gen AI stance on it?
**Liudmila Molkova** 48:28 No specific. Jenea.
Okay, thanks.
I'll go.
**Aaron Abbott** 48:32 I'll put in the agenda. There.
**Liudmila Molkova** 48:34 Wonderful. Thanks.
Okay, so under evaluations, I want to separate the semantic conventions from how evaluations are done.
I think there are a lot of folks in Microsoft toy interested. I don't know if I should put my name here. I'll I'll check with some Microsoft
**Samuel Colvin (Pydantic)** 49:01 I can volunteer someone to review that work. I'm not gonna be able to get someone to do it or do it myself. But someone from Pedantic will
be volunteered by me to review it.
**Sergey Sergeev** 49:14 Yeah, and we will have an engineer on Cisco's blank side also.
No, but it's in.
**Liudmila Molkova** 49:25 Would they be interested in working on the on on this? Or just reviewing.
**Sergey Sergeev** 49:35 Yeah, I've been working.
Yeah, they should be able to dedicate enough time.
**Liudmila Molkova** 49:46 Okay?
For this one. Is anybody going to work on this.
**Sergey Sergeev** 49:56 No, Cisco, they'll be working again. We will put more names. It's
now. Even 2 teams are interested and just connected. Who are working on it.
Giovannis and my.
**Samuel Colvin (Pydantic)** 50:13 What do we need to do within within hotel for that.
**Sergey Sergeev** 50:17 Make sure that we have a way to call evaluator with some instrumentation language types instead of specific telemetry. I think there are benefits of doing it.
Basically, we need to review different designs of how evaluators can be plugged into instrumentation. Stack.
**Samuel Colvin (Pydantic)** 50:42 If I'm.
**Liudmila Molkova** 50:43 Go ahead!
**Samuel Colvin (Pydantic)** 50:44 If I'm understanding correctly, maybe I'm not. Pydantic. Evals has support for judges that basically get access to spans and can then go and judge based on, for example, whether a tool was called using the spans within that Eval. I don't know if that's part of that. I can send you a link
format for sending that data to hotel.
**Sergey Sergeev** 51:08 Yeah, maybe I'm missing something. I don't appreciate any ideas.
**Samuel Colvin (Pydantic)** 51:12 I'm not saying. I mean, it's half baked is perhaps a little rude, but like it's not, it's not like incredibly complete. But I just sent you the link
and there's a bit on open telemetry integration. There.
**Giovanna Carofiglio, Cisco** 51:31 I think we are referring here to runtime evaluation rather than offline.
**Samuel Colvin (Pydantic)** 51:37 No, yeah. I mean, we can use that, for we basically co-opt hotel to send the data about offline evals as in. If you go and run a like batch job to to run evals. Then we send that data to log fire as hotel.
**Giovanna Carofiglio, Cisco** 51:52 No, no, I was. I was. I was mentioning
Sergey's point when we added this ranivals was probably related to one time. But yeah, you can go beyond that. Yeah.
**Sergey Sergeev** 52:02 Yeah, we will be bothering you guys from pandemic.
**Samuel Colvin (Pydantic)** 52:06 Okay, we're here happy to happy to talk.
**Liudmila Molkova** 52:13 Okay, cool. So from Multi Agent side, I think we have Microsoft and Cisco who are interested at the same time. I kind of share Sam's concern that it's
somewhat far from our main agenda, I think, like what I personally miss is the actual prototypes of the instrumentation.
And the conventions are easy to write. But yeah.
**Giovanna Carofiglio, Cisco** 52:45 I think that is more long term topic, and that's fine. When I propose it, I propose it as agency, so I mean, there are more partners, pedantic included, so we will try to have discussion and come with proposal. But we can also have discussion directly in this forum. So it's not just a Cisco. But yeah, otherwise we can prioritize instrumentation.
**Liudmila Molkova** 53:18 Oh, and I'm going to
**Giovanna Carofiglio, Cisco** 53:22 And you wrote just this thing you wrote multi agent. I think it also includes the agentic protocol instrumentation.
**Samuel Colvin (Pydantic)** 53:36 That was presented last week on.
**Giovanna Carofiglio, Cisco** 53:39 I mean, yeah, that was proposed by Microsoft. I was saying that we have released a few things in open source. We would like to also present from our side. But there is some aspects related to a multi-agent communication collaboration, and the observability of that. But there are some others which are probably even shorter term about agentic protocol observability, which you can have also with an Llm. Talking to an Mcp. Server, and
so just mentioning that that when we call it multi-agent. There is also that.
**Samuel Colvin (Pydantic)** 54:12 Yep.
**Liudmila Molkova** 54:13 Let's put it here right? So we.
**Don B** 54:17 So a quick question. Cause like I've been thinking about this, and I wouldn't mind helping it out, but be impossible to tackle on
one zone, but it's the aspect of it's like the standard telemetry open telemetry standard has their demo environment.
This sort of in terms of multi agent and multi agent with Mcp type scenario takes more. So a good business use case. So if the travel planner use case is something that people have already sort of
created the sort of you know. They're coming out with a docker toolkit now. But you know the dockerized ability, the ability to generate. You know the the base or the original Json Rpc. Message that we kick things off for various scenarios.
If that has been done, even if it isn't a semantic Convention, Llm perspective. I think that would help significantly in standardizing the scenarios and the messages that we're trying to.
Does that make sense? I see there's huge value in this, but I've been looking at it, and haven't been able to sort of distill that yet.
**Liudmila Molkova** 55:39 Yes, I think the key piece that we will need to focus in the protocol level is the context propagation. And even in the lack of semantic conventions. You kind of need to
propagate whatever workflow id task. Id. However, you call it.
**Don B** 55:54 Exactly so. I think it's been done like I don't know. In blockchain there was a convention. I don't know if that was sort of the aspect of you know, how do you generate data? How do you track it through? An end to end flow? So
anyway, I think it's maybe been solved, but just not external to sort of what we're focusing on.
If you can leverage other people's work that's always help.
**Liudmila Molkova** 56:27 Yes, Sam. Go ahead.
**Samuel Colvin (Pydantic)** 56:29 I wanted to talk about something completely different, just very quickly, because I have to drop like on the hour. I've got a call, but I don't wanna like distract from this conversation. So
no, go ahead. We have just a few minutes left. Go ahead.
Okay. I'll just say very quickly. We talked very a bit last week about pricing for Llms. We've started a project to basically
have have prices for Llms. We would love collaboration. It's not ready yet, but hopefully it will be quite soon. We have most models in there now
in Yaml. And then, if you look providers, there's basically if you look in providers. I'm just letting everyone know hopefully, it's in a better state in future.
But like we're doing the work, so most models will now have.
Prices in there. And yeah, we're gonna work on it. So
I'll make more noise about it. But just letting everyone know.
**Liudmila Molkova** 57:25 Nice.
**Samuel Colvin (Pydantic)** 57:27 I looked around at the references you you gave, and not not be critical of you, but none of them were none of like. We've sucked all this data from all the existing sources, but none of them do it right? So we'll do it. How we want it. So that's why we're doing it our way.
**Aaron Abbott** 57:40 Yeah, sounds good.
**Samuel Colvin (Pydantic)** 57:43 Cool.
Thanks. Everyone. Sorry to.
**Liudmila Molkova** 57:44 Nice.
**Samuel Colvin (Pydantic)** 57:45 Be late and leave early. Bye, bye.
**Liudmila Molkova** 57:47 No, thank you. Okay, we are out of time. I think we should continue. We didn't
really talk about what? And who is interested in doing this stuff. So maybe let's put the cut line.
Here!
And
We didn't cover any of the poor request reviews. I think
that I want to call out 2 of them.
This is getting ready till
go. So if you want to. If you have any thoughts or concerns. Please take a look, and I'll probably ping you to discuss the
final details.
And I didn't get much updates on the monster.
I understand it's it's it's too big. But I think we need to go through
and discuss it in details. I don't know how we will find time for this, but let's try.
**Aaron Abbott** 59:04 Yeah, I agree, sounds good.
**Liudmila Molkova** 59:09 Cool. Then thanks a lot for your time, and have a great week.
**Aaron Abbott** 59:16 Yeah, you, too. Thank you. Everyone.
**Liudmila Molkova** 59:17 Thank you.
