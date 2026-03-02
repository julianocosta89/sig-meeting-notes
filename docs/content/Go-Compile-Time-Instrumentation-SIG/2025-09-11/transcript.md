SIG: Go Compile Time Instrumentation SIG
Date: 2025-09-11
Duration: 76 minutes
Zoom Recording URL: https://zoom.us/rec/share/puI8utikqcC5suoFlaJGp1tDwZKH34a9xQ0FPgjLDyYIK1ZvIofnpebRzYk4H8_2.CHYiN9FXFQi0GQHX
============================================================

## Zoom Recording Transcript

**Przemyslaw Delewski** 00:04 Best.
**Kemal Akkoyun** 02:39 Hello?
**Przemyslaw Delewski** 02:40 Hi, Camel.
**Kemal Akkoyun** 02:43 Long time no see. How are you?
**Przemyslaw Delewski** 02:46 Good, thank you.
And you?
**Kemal Akkoyun** 02:50 Who knows?
**Przemyslaw Delewski** 02:51 So you recently have been on this golferCon, right?
**Kemal Akkoyun** 02:55 Oh, yes, I talked about… This, basically, whatever we do in here as well.
Okay. Yeah, it was great.
**Przemyslaw Delewski** 03:05 And you presented, this, or… I don't remember the name of your tool in Datadog.
But do you present this tool, or maybe something from OpenTelemetry already?
**Kemal Akkoyun** 03:21 the tool called Orchestrion, but, like, the talk was all about, like, how we come to be writing Orchestrian, right? And then, like, the call to action and the feature was about OpenTelemetry compile time instrumentation, so this thing.
And people were already interested in.
They talk, like, they ask questions about, like, all… like, how they even start using it. There is a company that they are, like, already using Orchestrian, and they're a paying customer for Datadog, but they want to use, like, OpenTelemetry for other stuff, and they're, like, super interested in the result of this work, so…
You will immediately have a customer, and they're a bank, whatnot, so…
Okay. So, good signals, so we need to build it, so…
**Przemyslaw Delewski** 04:15 Yes.
**Kemal Akkoyun** 04:23 Who is the facilitator of this?
**Przemyslaw Delewski** 04:25 I think that today is my turn.
**Kemal Akkoyun** 04:28 ruled.
**Przemyslaw Delewski** 04:39 Maybe let's wait, 2 more minutes, and then I can share the screen.
**Kemal Akkoyun** 04:46 Nope.
**Huxing Zhang** 04:47 Hi, sorry, I'm licked.
Nice to meet you.
**Kemal Akkoyun** 04:57 Finally, right? It's been a month.
**Przemyslaw Delewski** 04:59 Yo…
So please add your name if it's not there to the document, and if you have something on the agenda.
Please add it as well.
**Huxing Zhang** 05:18 Okay.
**Przemyslaw Delewski** 05:31 Okay, maybe I will share the screen.
**Kemal Akkoyun** 05:40 Oh, I already added that. Nice.
I'm sorry.
Oh, that reminded me.
I can't kiss.
Open.
We do.
Filter, right.
**Przemyslaw Delewski** 07:37 Okay, can we start?
**Kemal Akkoyun** 07:40 Yeah, sorry, invite me.
**Przemyslaw Delewski** 07:42 Okay, so, the first topic that I added on the list is about CI workflow and…
Unit test coverage, so…
At some point, we disabled all our tests, unit tests and test coverage. As you can see here, this is temporarily disabled.
Which means that these actions, of course, are not executed on the CI for now. And, so I wanted to fix that. I can take care of that thing, so I can add this as an action point.
But, yeah, so that's the thing. I think that it's time to enable this test, because we now have a more or less complete framework.
When we will merge, of course, the last PR, we will have it, and then we can start work on, on, probably on, on instrumentation for…
additional libraries, and also we will probably work on framework itself, but it's… I think it's a good time to enable all these tests, all these actions here.
The second thing is that I would like to also extend our unit test coverage.
Because we don't have, we have only, I think, one or two tests now, and it would be good to have more tests, and also to extend this,
developer experience, to, to, to have a test where we can go and test, step-by-step what
What, our tool is doing.
So, basically, that, that's, that's, that was my goal, that, that is my goal.
And any comments on that?
**Kemal Akkoyun** 09:45 Biting is fine by me, let's have it.
**Huxing Zhang** 09:48 Yeah, agree.
**Przemyslaw Delewski** 09:57 I don't know how to edit this thing.
Okay.
**Kemal Akkoyun** 10:05 What do you want to do?
**Przemyslaw Delewski** 10:07 It's… it works now, so…
**Kemal Akkoyun** 10:11 Okay.
**Przemyslaw Delewski** 10:18 Okay, so…
Yeah, I think we can then, if we don't have any further comments on that, or questions, we can go to the next
Next topic, which is from Camel.
**Kemal Akkoyun** 10:33 Yep.
I think, since we have the Hello World application right now, let's, like, decide the scope of MVP, or, like, beta release, or initial release, not even beta, this is… should be, like, the initial release.
And, and let's call it, like, 0.1, and…
doesn't need to be, like, super fully-fledged whatnot, just, like, try to inject open telemetry SDK for HTP and GRPC.
And I think we can achieve that in a couple of weeks, so that's my proposal. So, your thoughts? Do you think this is feasible, or what are the blockers?
**Przemyslaw Delewski** 11:17 Yeah, I think that it's feasible. First, we have to, of course, merge this PR from Eonc.
Yes. That is about finishing the end-to-end framework, but then I think we are ready to start working on these topics.
**Kemal Akkoyun** 11:36 Any objections?
**Huxing Zhang** 11:39 Yeah, I also agree on we… yeah, we should do releases, even if it's not,
very complete, or they have some issues, yeah, we should do that, yeah.
**Kemal Akkoyun** 11:54 Yeah.
So, like, what I… what I have in mind, we don't need to, like, care about the configuration layer at all. Like, this could be manual and whatnot, so… at this stage. So, just, like, to be able to have those, like, middle layers, like, injected,
for, like, refold configuration, whatnot. So,
Wherever we can cut corners, let's cut corners, but, like, let's have something that's presentable, like, this is an HTTP application, and this is a gRPC application, and you run this, and boom, it's instrumented.
**Przemyslaw Delewski** 12:31 Do you think that we should have some, I don't know, basic HTTP or gRPC examples to instrument, or we should use something that exists already?
**Kemal Akkoyun** 12:47 We can try, like, we can try it on a demo application, but, like, we can also try in a complicated case as whatnot, so…
But it should be fine, I think.
Depending on the example, and how far we can go.
**Przemyslaw Delewski** 13:04 Yeah, so we can start from something very, very minimal, I think.
**Kemal Akkoyun** 13:08 Yes, minimal, like, maybe a very common standard pattern that we can hook into and just support that case, but, like, show that it stuck working, then we can build something more flexible.
Okay, so do we have any agreement?
**Przemyslaw Delewski** 13:42 Yeah, I think so.
**Kemal Akkoyun** 13:44 Alright, let's aim for it.
**Przemyslaw Delewski** 14:00 And regarding, because, I think you mentioned something about configuration.
But we already have a configuration where we can describe what we would like to…
And where we would like to inject Okay.
Okay, so that's something that you meant, right?
**Kemal Akkoyun** 14:22 like, that configuration… what I meant, like, we shouldn't…
Focused on the nitty-gritty details of the configuration layer.
it's endless, right? So, not focus on that. Maybe configuration is not finalized, because that's the user-facing API, and I think it will…
We need to discuss a lot of things about that, so I want to skip that part.
assume there's a basic configuration, maybe even without configuration, make it work.
**Przemyslaw Delewski** 14:52 Yeah, so, as you said, this probably will evolve, but at least we have something that we can use, I think, for now, so we have a basic, you know, configuration that works.
**Kemal Akkoyun** 15:06 Book.
Okay.
It's fine.
**Przemyslaw Delewski** 15:30 Okay,
We can go then to the next stopping.
**Kemal Akkoyun** 15:50 Okay.
So, the next topic is,
about the feature, have you ever heard about this project called Weaver? It's part of OpenTelemetry.
**Huxing Zhang** 16:03 Yeah, sure.
**Kemal Akkoyun** 16:05 Yeah, so if you know about it, so I… what I envision is Weaver is, so you basically write your semantic convention and, like, generate, code for those semantic conventions.
And, like, we should have examples or a way to support this directly, for our application. That would be super cool, right? Like, you can generate your semantic convention code with Go, and get the generated call.
go code and use the compile time instrumentation, and inject over the…
Basically over the board, whatever applications that we have.
So if you haven't checked it out, I, like, highly encourage. It seems like a perfect fit with our tool.
**Przemyslaw Delewski** 16:55 Okay, so I haven't heard about this tool.
So I have to read about it. And so your,
Suggestion is to use our tool to instrument it, or what…
**Kemal Akkoyun** 17:10 No, no. So, if you go to the, like, if, like, this… what this tool does is…
there is a configuration layer, and that, from that configuration layer, it generates code, right?
**Przemyslaw Delewski** 17:22 Okay.
**Kemal Akkoyun** 17:23 you can use the same code, for example, Goal, Rust, Python, JavaScript, whatever, like, in your company.
and, like, these instrumentation SDKs are already… can be used to instrument your code, right? And then you would manually import these packages into your code, and then you would instrument your application, right? So instead of doing that, we can support a mode
And… Like, whatever you generated with the Weaver, you can just inject it in the compile time.
This could be just an example, right? We don't need to do maybe something magical, but maybe we can also, like, offer some, like.
convention of over-configuration type of, like, integration with the Weaver, with a configuration file, so we can say that if you have Weaver-generated SDK, like, then we can just inject that.
**Przemyslaw Delewski** 18:21 Okay.
Thank you.
**Huxing Zhang** 18:27 I want to add something to that, because we, what I, to my understanding, what another
Another point of this tool is to, like.
We build… build based on the hotel con… semantic conventions, but sometimes we would like to know whether we…
completely follow these, conventions or not. We can use this tool to check
If we have something that's different in our implementation.
**Kemal Akkoyun** 19:04 Yeah. Yeah, that's also a cool point, yes.
**Huxing Zhang** 19:08 Yeah, that's what we did in our company. Well, we are…
Facing this challenge is that sometimes we make mistakes. What we have implemented is not the same as the
convention has defined. So we use something… we want to use something to automatically check.
For that. I think this tool can…
have a… can do things like that, and we… maybe we should check it out. We are planning to adopt this tool in our company as well, yeah, but, yeah, I think it's definitely… we can try, something we can try.
**Kemal Akkoyun** 19:53 Yeah, I already found what you meant, it's here.
**Przemyslaw Delewski** 20:00 So, first point was about, like.
**Kemal Akkoyun** 20:04 Support…
**Przemyslaw Delewski** 20:06 Okay.
**Kemal Akkoyun** 20:07 Automatically… Injecting.
Output, or, like, generated code.
Using our tool.
The other point is basically using this functionality, and probably defining our, like, yes, let's say, defining… semantic,
On mentions, or… our instrumentation.
And choosing… So check it.
Yeah, this could be a part of CI.
**Huxing Zhang** 20:46 Right.
**Kemal Akkoyun** 20:49 Thanks for that.
Yep. Why not? Like, that would also help us to understand this tool and support the use cases.
Because we always say that, okay, like, the…
target audience of this tool is platform engineers, and so that they can just change their, I don't know, like, Docker files, or how they build their application, and they can automatically inject their instrumentation, right? And this tool also targets those audience. So you configure your semantic conventions.
And then, make sure that everything abides or, like, follows those conventions over the board. So…
Same logic.
We will just make this easier for everyone.
**Przemyslaw Delewski** 21:38 Okay.
**Kemal Akkoyun** 21:45 Oh, that's it for this topic, if you don't have anything else to add.
**Przemyslaw Delewski** 21:51 Not from my side.
**Huxing Zhang** 21:54 What we do… is there any actions for this… Topic?
Fast to take.
**Kemal Akkoyun** 22:01 I think not right now, but, like, we can say that…
First, we need to add the SDK in the, into the application, right? So that's why, like, there's no immediate action, but we can say that, like, Adam…
CI action,
Sore… But after… We have the… or Taylor CK.
instrumentation in place.
Or, like, with semantic conventions.
Bye, Chen.
Okay, this one, but this is not urgent, but let's… let's add the action item. We can carry it over. That being said, did we have… oh, right, we don't have any remaining action items. Okay.
**Przemyslaw Delewski** 23:07 Okay.
So now I think we can go to the next one.
**Huxing Zhang** 23:15 It's the, we are actually, yeah, holding the KCD Hangzhou, and together with the Open Infra,
foundations, this, co-located event, and this is in Chinese, but
Actually, we are calling for proposals, and I'm being one of the organizers, so actually, I'd like to, like to…
To call… call it out, and maybe we can, like, to apply for… submit a proposal for our… for this event? Yeah.
And, I think the deadline is, about 10 days…
from today, and we still have time, and yeah, I think we should, have tried it out, yeah.
**Przemyslaw Delewski** 24:11 So, do you plan to present in English or in Chinese?
**Huxing Zhang** 24:17 I think, in Chinese it's better, because the…
**Przemyslaw Delewski** 24:21 Attendee.
**Huxing Zhang** 24:21 It's almost in Chinese, so I think one of our, folks may…
Submit a topic to that, just a… Not to bring it out.
**Kemal Akkoyun** 24:38 Sounds good.
**Przemyslaw Delewski** 24:44 Okay, anything, sir, for this topic?
**Huxing Zhang** 24:46 Nope.
**Przemyslaw Delewski** 24:47 Okay.
So, the next one is Kamal about KubeCon.
**Kemal Akkoyun** 24:52 Same thing, actually. We did it a couple of times. I think we need to, like.
Write yet another proposal, and try to submit.
to KubeCon, and maybe, probably, maybe a co-located event, like Observability Day, whatnot, which I think they haven't opened that yet.
But let's try it again. This one… for, like.
Most of us from Datadog site, we're all based in Europe.
And this would be easier for us to attend.
**Przemyslaw Delewski** 25:30 But let's do a joint talk.
**Kemal Akkoyun** 25:34 As always, it's always better, so…
So, I think the first action item, who would like to
volunteer to give the talk for the CFP.
**Przemyslaw Delewski** 25:49 So where this cube con will be located?
**Kemal Akkoyun** 25:53 This one is in Amsterdam, if I… steak.
**Huxing Zhang** 25:57 Yeah.
**Przemyslaw Delewski** 25:57 Okay, okay.
**Kemal Akkoyun** 25:58 Yeah.
**Przemyslaw Delewski** 25:59 So, I can participate in that.
**Kemal Akkoyun** 26:04 Same here, so… maybe we can have someone from Ayuba as well, so…
**Huxing Zhang** 26:10 Okay.
**Kemal Akkoyun** 26:14 Cool. Three people, yeah, let's initialize one.
Gosh.
**Huxing Zhang** 26:22 Actually, in order to increase the acceptor rate of our talk, I… I'm thinking of, whether we should add some.
elements.
About, like, AI-related things, stuff.
Shoot, shoot, shit.
**Przemyslaw Delewski** 26:38 Hmm.
**Huxing Zhang** 26:39 proposals, because you know that, all the conferences are talking about AI, or every conference I have attended this year, that they are talking about AI.
**Przemyslaw Delewski** 26:49 That might be.
**Kemal Akkoyun** 26:50 Yeah.
**Przemyslaw Delewski** 26:50 point.
**Kemal Akkoyun** 26:52 hub, like, do this?
**Huxing Zhang** 26:54 Yeah.
**Kemal Akkoyun** 26:55 I find it super forceful.
**Huxing Zhang** 26:57 Actually, I am thinking about, like, to… like, we'd add some introduction, or to the AI…
related frameworks to add the observability instrumentation. Like, what I've done here is we, in China, we have several, like, AI agent frameworks that are written in Golan, Goland.
And, we also have some popular, popular, frameworks, platforms that build in… Golan, and we can…
As something that we can add some observability… observability of that… AI agent frameworks.
our AI platforms that are written in Gonan, so that we can connect our observability and the AI. That's what I'm thinking about.
**Przemyslaw Delewski** 27:54 Yeah, that's…
**Kemal Akkoyun** 27:55 Yes, that's actually super cool. Like, there's the… there's an official MCP SDK from GoTeam as well, and I think there's another one, like, the MCP implementation
coming from the original creators of the MCP, and we can just showcase instrumenting those things, build some agents using one of those, and, like, instrument that.
But yeah, this can be an example, and we can include that in the description, that we're gonna show some how to, like, instrument some agentic applications.
It'd be interesting to try.
**Huxing Zhang** 28:38 Actually, in our repo, we have some contributors that are doing this and that.
And we can…
like, draft something, or we can, we can have… first… at least we can have a documentation of how we can do things like that. I think,
There's already something working on that, happening in our… Red Pole.
And we can initiate that.
**Kemal Akkoyun** 29:06 So, share a documentation.
Excuse me to think.
AI ML agents.
Can I assign this to you?
**Przemyslaw Delewski** 29:21 I was also… I was also thinking about something simpler, you know, to… to use AI?
in the case where AI is using, or LLM is using our tool, in order to prepare configuration to instrument, you know, specific libraries. So we can, for instance, provide some MCP, model context protocol, some component, and provide
some tools,
And then, user can use this MCP in order to, you know… user as a developer can use it in order to prepare this kind of configuration, this YAML file.
That will be generated automatically, for instance.
**Kemal Akkoyun** 30:11 this could eventually can happen, but we don't even have a, like, a stable YAML configuration, and from my experience, if
Like, these models…
doesn't work super nice with the newer stuff, so… because this will be a new thing, and recent, and there… there aren't…
a lot of examples to that. Outcome would be suboptimal, but we can try, of course.
**Przemyslaw Delewski** 30:40 Yes, that's true, that this configuration is not stable for now, but…
That's just an idea, I don't know.
**Kemal Akkoyun** 30:49 Yeah. Yeah, definitely. Maybe not for… not this KubeCon, but eventually we should have something like that.
**Huxing Zhang** 30:58 Music contract.
**Kemal Akkoyun** 30:59 I'm afraid it's hard to make it work, yeah.
**Huxing Zhang** 31:02 Right.
I think we can draft multiple proposals and, before submission to the…
**Przemyslaw Delewski** 31:10 Yeah.
That might be a good point, so to… at some point, to match… to take the best, you know, things from all proposals and match them, somehow.
**Huxing Zhang** 31:21 Submit, two or maybe three net nets.
**Przemyslaw Delewski** 31:27 So your idea is to… just to submit more than one, right?
**Huxing Zhang** 31:32 Yeah, yeah, yeah.
**Przemyslaw Delewski** 31:34 Okay.
**Kemal Akkoyun** 31:35 I am…
in for this as well, like, we should… we can, I think, submit up to 3 proposals, as speakers and co-speakers, and we can do this.
**Huxing Zhang** 31:47 Yes.
**Kemal Akkoyun** 31:49 Also, like, there are other tracks that we can submit, yeah, let's try. We… at some point, we also ask, to the OpenTelemetry governing community, that committee that, like, whether we can have an update, like, slot.
Because they have this in KubeCones, you know, as part of OpenTeleMH, and they said that, like, they would be happy to help for that as well. So…
In the end, if our proposal's all rejected, let's try to aim for, like, preparing an update for KubeCon.
Like, I don't know, maybe we can ask to be…
present for that. Also, one last thing, we can also have lightning talks. Lightning talks are the easiest,
Barrier of entry, and, like, and they… probably we… we could… we would get some acceptance, and we can demo that, like, whatever we built by then.
**Huxing Zhang** 32:49 Yes, there's another channel, it's called the Maintainer Summit. That's dedicated for the project maintainers of the CNCF projects.
**Kemal Akkoyun** 33:03 Yes.
for…
the maintainers, they, can have meetings, but I don't know if they would have, like, say that, okay, as a SIG, you can have this, and…
**Huxing Zhang** 33:19 I don't know.
**Kemal Akkoyun** 33:20 ask.
**Huxing Zhang** 33:20 Let's ask. It's a maintainer track, I think it's called a maintainer track.
**Kemal Akkoyun** 33:27 if… but it's… it's in the project level, the maintainer track. If you are, like, a CNCF project, then you can have it, but then the OpenTelemetry is a huge project. I don't know if they allow us to, like, as a SIG, we would like to meet in the maintainer stage. Maybe they would allow. I never, like, no.
**Huxing Zhang** 33:44 Totally.
**Kemal Akkoyun** 33:44 tried this as part of OpenTelemetry, and then maybe we can have some tickets and, like, go KubeCon and, like, have the meeting and, like, talk with the community, because, like, people can
joined those meetings. I did that as part of Prometheus and Thanos several times, but not with OpenTelemetry.
**Przemyslaw Delewski** 34:05 Okay.
**Huxing Zhang** 34:06 Okay.
**Kemal Akkoyun** 34:22 Oof!
That's it, I think, for this topic.
**Przemyslaw Delewski** 34:26 Yes.
So I think the next one… you can go to the next one, which is about…
Head over showcase.
So I will stop sharing.
I don't know.
**Yi Yang** 34:42 Okay, let me share the screen.
Can you see my screen?
**Przemyslaw Delewski** 34:52 Yes.
**Yi Yang** 34:54 I have finished the very, very early, PR for this project, and I'm trying to show the example.
We can… we can run the… the… the demo, we can run…
We can run it by using MakeDemo to show it.
Yeah, as you see, it, it firstly builds the instrumentation tool, and then builds the demo with the instrumentation, and then running, running the demo.
Like this.
how the world is… how the world is instrumented, and, and I'm… I'm digging it more, yeah. This… this is, this is the example program, and, our instrumentation code is located in…
PKT is super in the other word.
Is there?
Anna.
the main function course example, and… and we want to ins… we want to inject, instrumentation code in… at the beginning of the example, and the… and the… and… and the function… function X side.
Okay.
by injecting these two functions, my hook before and my hook after, it looks something like this.
My hawker beef… my hawker… Before.
And, infer my hook after moves something like this.
Damn.
**Kemal Akkoyun** 36:41 I agree.
**Yi Yang** 36:41 Hmm…
So, how can we… how can we tell the hotel tool we want to… what we want to inject, and what we… and where we can find our information code? The… the registration… the registration…
Configuration is located in there.
In this, in this, in this file.
When… when the point card field specifies, we, we want to inject the hook of the two
to example functions.
And,
What, and, advice, advice, advice field specifies, we want to instrument my hook before, and my hook after, into the mail, respectively.
And, the path, specifies where we can find my hook, and then my before. It, it…
It is located in, in this, in this model, PKG instrument hardware, as, as you know.
Okay, yeah, fair.
And this is the base… this is the basic flow, and
And if you're interested in the instrumenting the code, we can… we can…
We can inspect the hotel builder.
And, debug. Is it there?
Great content.
Oh, nice.
Yeah, we can give them the… the internal… we can… we can say it internally.
You can see here, we instrument the if, the if… we insert the if statement as the example, at the function entry.
And, the… and the hook, coarse, coarse, or trampled function. In trampled function,
it accomplishes many things. Firstly, it catch up all exceptions from there.
And, it prepares the hook context, then it finally jumps… it finally jumps into my hook before… my hook before. In my hook before, we can use our hook context to… to… to, for example.
To fetch, to… to do seed data?
And, we, we, we can also, to get data, get data from, from, from, from the context.
And also, we can, we can gate, gate parameters.
Or get the… or see the… see the return values.
Basically, in this.
So, so it, so, even if our, our, we, we are in very early stage, but, it, look, it does work, it does work, yeah. And, I, I think, we can set a goal.
For our first, first initial version. As we mentioned in, at the end of October.
And for… for… I think… I think we can… we… I think our goal could be, for example.
make… make HTTP work, or gRPC work.
As the final… as the initial… the goal of the initial version.
And after our… after this… after the patch is merged.
The follow-up work could be, could be done perinatally.
I don't have a very detailed, list, but I could… but, I could break it down into, into some… some stuff… some stuff in my mind. For example, we can…
We… I think the most of… we can… we should enable the test.
this, I think this is the most, most high priority.
Yeah, in this, I think… In this… in this space? Okay, yeah.
**Kemal Akkoyun** 41:17 Yeah.
**Yi Yang** 41:18 And, and, we, we should, and, now, and all… we… and we should, we should also support the, support the instrumenting the struct.
Yeah, I think… I… yes, I think this… this stuff's, in most priorities.
**Kemal Akkoyun** 41:42 So, good.
**Przemyslaw Delewski** 41:44 Instrumenting strucks, you mean, right?
**Yi Yang** 41:48 Yeah, yeah, yeah. Yeah, okay.
**Przemyslaw Delewski** 41:50 Yeah, that's definitely something that we will need.
**Yi Yang** 41:55 Okay.
And I… I wonder if you have any other high priority, since we can… we can be done parallelally?
At least from my mind, at least from my side, the most high priority stuff is, first, enabling the test and, and the instrument the struct.
Yes.
**Przemyslaw Delewski** 42:20 Yeah.
**Yi Yang** 42:20 achieved our goal, and… Instrument of the net as you did it.
**Kemal Akkoyun** 42:26 Yeah, first of all, the Yi Yang, thanks for…
the work, this looks amazing. You basically did this single-handedly, thanks for that. And we will try to review the PR.
as soon as possible. So, let's get it merged, and as you said, like, start iterating on the next phases, next tasks.
**Przemyslaw Delewski** 42:55 So… Let me share the screen again.
There is one thing that I was thinking about, because currently.
I think that it's hard to,
unit test this kind of things, because, for instance, we have this tool exec function, but inside this call, we have also, running another processes, so it's hard to, you know.
unit test this, so I… I made a simple refactoring here, so I extracted from this tool exec function something that is another function called compile command, and there is the whole process of this,
the whole flow of this instrumentation here. And now I can use it easily from the unit test.
So, I prepared arcs here.
some, artificial arcs, but, you know, they mimics the real… the real arcs. And now I can, I can invoke that, and this… then we can, you know, go through this code step by step, step by step. I don't know if you have any other,
maybe, options, or do you have any other ideas how we can better unit test that?
**Yi Yang** 44:23 Yeah, very great work. We… we haven't… we haven't did this. We, we, we have… previously, we, we always build the program and run the program to check the output, to…
**Przemyslaw Delewski** 44:38 Okay.
**Yi Yang** 44:39 as a taster, but your, your, your refactor is very, very, very useful. Yeah.
**Przemyslaw Delewski** 44:46 Okay, so… so, you know, my plan is to enable these actions, as I said, but also I would like to prepare a pool request with this small refactoring and to add more unit tests to our project.
So, yeah, as… and as I mentioned, we can… if I rerun it, we can now go
Through this step-by-step, so… We can go,
To the instrument face and everything.
You can check what the code is doing here very easily.
So… That's… that's basically the idea.
Okay.
**Yi Yang** 45:31 Thanks, thanks.
**Przemyslaw Delewski** 45:33 So now we can go to the next topic.
**Huxing Zhang** 45:40 Yeah.
**Przemyslaw Delewski** 45:41 She's from Hushing?
**Huxing Zhang** 45:42 Yeah, I'm thinking of, as I have mentioned in the Slack, and I'm suggesting of using AI like GitHub Copilot to help you do the code review, or something like that.
And I wonder if you, have
do it already, and you have checked the results that Copilot has feedback. I think the quality is relatively good, and it's helpful sometimes, and I wonder if anyone that…
Could, have some comments on this, for enabling this, like, competitor to help us do code-to-code review.
**Kemal Akkoyun** 46:31 I never tried this, but I would be happy to try it. How do we enable it?
**Huxing Zhang** 46:36 It's very easy. When you review some, PRs, you just assign the assignee to the GitHub compilers, add, add one…
to the… to the… add GitHub Copilot as the… one of the reviewers, and it will automatically activate that and do it for you, and it will leave the comments there, and you can choose whether to accept or not.
**Kemal Akkoyun** 47:06 Okay, I'm just trying that in the open PR from Yi Yang, so let's see how it behaves.
**Przemyslaw Delewski** 47:17 Okay.
**Kemal Akkoyun** 47:19 Yeah, I'm okay… with, like, trying all the AI tools, if it helps us.
I don't see any problems with that. We just need to be conscious about, like, what to accept.
Because, like, you cannot… held accountable an AI tool.
So we have to hold accountable ourselves.
Sorry.
**Huxing Zhang** 47:40 Yes.
I think we just want everyone to evaluate the
Quality of the comments that it left.
Yeah, so we have… so that we can, like.
Have some, basically have some trust on that tools, yeah.
**Przemyslaw Delewski** 48:03 Yeah, so we, in fact, enabled this kind of agent for one of our projects, and what it provided for us is very basic, you know, comments about the code. But still, it might be useful, of course.
**Huxing Zhang** 48:20 Yeah.
I think sometimes we will, for some cases, like typos, something like that, and the stuff that will be…
Yeah, very good for the AI to…
To capture the… something like that. But,
what we can do, about the deeper things, like, like very high-level bugs, then maybe we'll not be able to identify, but it's not very… I think it's worth to have a try, yes.
**Kemal Akkoyun** 49:01 Yeah, let's try it.
**Huxing Zhang** 49:03 Yeah.
**Kemal Akkoyun** 49:05 Yeah, it already left a comment on the PR.
**Huxing Zhang** 49:11 Yeah.
**Przemyslaw Delewski** 49:11 Thank you.
**Huxing Zhang** 49:12 At least the advantage is that they will never take a rest.
**Kemal Akkoyun** 49:18 Yes.
But nowadays, it's thousands of AI tools nowadays.
Pretty cool.
**Przemyslaw Delewski** 49:30 Okay, I think we are good.
And if he goes…
**Kemal Akkoyun** 49:36 Nope, I think we should… let's aim for reviewing the open PR, and try to merge it maybe this week, at the very latest, beginning of the next week.
**Przemyslaw Delewski** 49:47 Yes, yes.
**Huxing Zhang** 49:50 Okay.
**Kemal Akkoyun** 49:52 Awesome.
**Przemyslaw Delewski** 49:54 Okay, so then… If we don't have any other topics, I think we can…
Stop the meeting, and… So, thank you very much for attending.
And see you next, next time.
Bye.
**Kemal Akkoyun** 50:10 Alright.
**Huxing Zhang** 50:10 fine.
**Yi Yang** 50:11 Alright, see you.
