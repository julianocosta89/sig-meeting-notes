SIG: Developer Experience SIG Meeting
Date: 2026-05-06
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 00:21 Hey, Irviano.
**Juliano Costa | Datadog** 00:23 Yo.
How are ya?
**Johanna Öjeling** 00:31 I'm good, thank you. How are you?
**Juliano Costa | Datadog** 00:35 Git, git?
**Johanna Öjeling** 00:38 Let's response.
**tristan** 00:39 Yay!
**Juliano Costa | Datadog** 00:40 Good morning.
**tristan** 00:41 Morning.
Contact's messed up, one second.
Hmm.
**Johanna Öjeling** 00:49 So, did you start a new job, Krista?
**tristan** 00:52 Yeah, it just started a couple weeks ago.
place called Serv… Robotics.
**Johanna Öjeling** 00:58 Congrats!
**Juliano Costa | Datadog** 00:59 Do they do hotel?
**tristan** 01:01 They don't yet, that's what I'm partially there for.
**Juliano Costa | Datadog** 01:05 Oh, cool.
**tristan** 01:06 it's an Elixir Erlang backend, and then they want to get into OTEL for all types… they have robots and stuff, and they want those doing hotel, they want the backends doing hotel, and all that, so… I'm doing… both parts?
Back-end work and hotel work.
**Johanna Öjeling** 01:25 Nice.
**Juliano Costa | Datadog** 01:26 And you have IoT devices and stuff, like, it's robots, I guess, you have.
**tristan** 01:32 Those delivery robots?
**Juliano Costa | Datadog** 01:35 Awesome.
**tristan** 01:37 Like, cruise around the streets, yeah.
**Juliano Costa | Datadog** 01:42 I think that would be a nice story to tell, just saying.
**tristan** 01:48 Yeah, once we're up and going, it will be. The… Slowly working with the infra team to actually get the collector deployed, but… Once we get that up and running and the service is, instrumented, I think it will be a good one to put up.
**Johanna Öjeling** 02:06 Do you work in, like, a platform team, or…
**tristan** 02:10 Yeah, I'm technically on, what we call the… delivery… delivery platform? Delivery something platform, but yeah, so… because I'm technically on the, like, backend team for, like, controlling the robots, but the… because of the hotel experience, I'm kind of straddling, so I'm, like, working with, Multiple other teams on getting both the collector out and instrumented to the different components, so… Kind of all over the place.
**Johanna Öjeling** 02:46 Park.
**Perk (Marcin Stożek) | Elastic Ingest** 02:49 Hey, folks.
**Juliano Costa | Datadog** 02:50 you know.
**tristan** 02:51 Nope.
Let's see…
**Juliano Costa | Datadog** 02:58 Tristan, we… we had a nice chat last week.
with, Aubrey.
From the docs team.
**tristan** 03:10 Oh, yeah?
**Juliano Costa | Datadog** 03:11 Yes.
Let me just open the notes here.
And, So, we started the discussion on the things that we found out on our survey, and, like, our next steps.
And then, part of the discussion, we went to… Fabry mentioning the lack of agnostic, or vendor-agnostic way of showcasing hotel in the docs.
And then we kind of started discussing Aspire, and the open search observability stack, just to… try to demo observability within the docs to kind of show the value of hotel to newcomers and stuff, but I don't know if that would be something that we on the developer experience would tackle.
One thing that we, that we discussed that could be something that we can, handle.
is… Some sort of proposal where we… present to GC, something like, I think we already discussed that.
Every SIG would have kind of a rule to follow where they need to document their… their components and their stuff in, some sort of template within their repos.
And then, to mark anything as stable and GA, this.
doc, or this template, need, Must be there. And then, the docs would fetch that and render in some way.
Ada docs. This is something that I have in my mind. I'm not sure if we actually discussed that with Fabri last week. I think, I briefly touched, but then the discussion went to the, to the, hotel backend.
So, I'm not sure what is the opinion from the docs team on that.
**tristan** 05:44 So you're saying the… the docs that get generated on the website would come… live in the individual repos?
Or they just submit it based on that template, you know?
**Juliano Costa | Datadog** 05:55 Yeah, I… So, from… From maintaining the devil.
So, from my experience as a maintainer on the demo, I know that it's… It's difficult to ask to every maintainer to maintain their repos, plus keep the docs up to date.
**tristan** 06:17 Yeah.
**Juliano Costa | Datadog** 06:18 Because it's two different working groups, two different repos, the cadence and the flow, they're different.
if we have a structured way where the project says, hey, this is the template that you need to follow, and this is what you need to do within your REPL, then we can enforce within every repo, like, whenever there is a change on component X, you need to update this doc, otherwise the GitHub action fails, so then the PR cannot get merged, and we only merge the PR whenever the changelog is changed, for instance. But, instead of the changelog, this doc template Because with that, then we do not increase the burden on the maintainers, but we ensure that the docs will be up-to-date.
**tristan** 07:13 Yep.
**Juliano Costa | Datadog** 07:15 And I know it's tricky because we have different… this is… I think this was one thing that we discussed with Fabric. It's difficult to map the personas that are accessing the docs.
we have folks that are fine in navigating to GitHub and checking the code on how to use a component, and even going to… let's say I want to use a component on the collector, I go to the Go code and check the implementation of that, and that's fine for some folks.
But for other folks, they just, check the yellow file on the docs, copy-paste, adjust for their needs, and that's it. And they do not have the goal knowledge to go to the GitHub code and actually see how that was implemented. And they do not even need that.
So, we have different personas. This is difficult to map, from the doc's perspective, because I don't think we have Like, I don't think there is a way to… To know that. So yeah, this was a thing that we… discussed a bit, last week. So, yeah, just…
**Johanna Öjeling** 08:25 Yeah, and I really like that idea, because it's, yeah, today, like, you have to go to the GitHub repost to read the readmiss to actually, like, learn how to do things, and… And, like, for… in some cases, I remember the… hotel operator. The documentation of the website is… mostly what's in the README, but then, like, people update the README, but forget about the OpenTele Micro I.O, so it's outdated, but this way, we would have, like, one single source of truth, and as you mentioned, Juliana, it won't increase the burden. Rather, on the contrary, it will reduce it, because You only need to update documentation in one place, and it will be reflected.
**Perk (Marcin Stożek) | Elastic Ingest** 09:15 there's one thing to take into account as well, which is, translation, which I think it's a people problem, because you cannot have people translating their website go to every Apple and translate their stuff.
That being said, I think you could say that, hey, English version is the master one, and that lives in the project projects, different projects repositories.
And then the translations are in the, in the main docs, for example.
**Johanna Öjeling** 09:42 Do you know how it works for… I'm thinking of, like, the specs, and, because… on OpenTelemetry I.O, it kind of refers to the specs repository, and that's where the, like, truth is, and, the OpenTelemacro I.O. uses Git submodules, I think, too. So I wonder how translations are managed there.
**Perk (Marcin Stożek) | Elastic Ingest** 10:14 I don't know for spec, I only know for the website, unfortunately.
**Juliano Costa | Datadog** 10:18 That works out.
**Johanna Öjeling** 10:20 For example, the op-amp spec, it's in a repository, and then the OpenTelemetry I.O, it, like, refers to the Git sub module.
**Perk (Marcin Stożek) | Elastic Ingest** 10:33 So that's a good point, because I am part of the translating team for Polish. We will get to that part, so I'll learn about it.
**Johanna Öjeling** 10:43 Mmm, okay.
**Perk (Marcin Stożek) | Elastic Ingest** 10:45 But if I look at the markdown… Yeah, it is in the spec.
That's true.
**Juliano Costa | Datadog** 10:53 Oh, I… Perk (Marcin Stożek) | Elastic Ingest 10:54 Page size is in the spec.
**Juliano Costa | Datadog** 10:56 I was checking the Portuguese one, but yeah, I cannot do that. Like, okay, now I found the spec, let me switch to… So, in the spec, when I go to the dropdown on languages, I just have… Perk (Marcin Stożek) | Elastic Ingest 11:12 English.
**Juliano Costa | Datadog** 11:13 Japanese and Chinese, I think? And English, of course. But, like, all the others are grayed out.
**Perk (Marcin Stożek) | Elastic Ingest** 11:22 Oh, interesting. Let me share my screen. So, that is what I see.
For the OPAM specifically, I can see only English.
So you said that… which one has Japanese?
**Juliano Costa | Datadog** 11:34 I think the, the root specs, so if you click on the, on the specs, on the drop-down itself, yeah, there you go.
**Perk (Marcin Stożek) | Elastic Ingest** 11:42 Yeah, okay, so this one will be translation for that page.
**Juliano Costa | Datadog** 11:45 Yeah, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 11:46 Specifically, and then you go to the specific spec, the status probably… yeah, it's easy to translate. This one doesn't have it.
Also, it changed from here.
This one… yeah, doesn't have it. Opam doesn't have it.
Yeah. Also, this one changed again.
Oh, so I, okay, and this is here. So I'm not sure, how this is done for specs. It seems like it's not.
**Juliano Costa | Datadog** 12:21 Yeah, I'm not… not sure.
But again, I'd want to… to start with this discussion, because I know that this goes a bit… out of the initial scope of this thing.
I think the plan was to typo SDKs and APIs. So, again, just bringing that back to you, Tristan. So, I want to hear your opinion on that, and, what is your idea? Because I think you had to leave, when we were starting to discuss that, so I want to hear what you have to say. So, yeah, go for it.
**tristan** 13:01 About what we can do next?
**Juliano Costa | Datadog** 13:03 Yep.
**tristan** 13:04 Yeah.
Yeah, I keep coming back, in my head, to needing to… ask, around the SIGs.
And then the developers.
don't want to do that again already, but maybe later in the year, where we have another survey, but more focused on the API and SDK, and… possibly get back to trying to query the SIGs about what they do different from the spec, so those are the things that we could, try to, formalize.
Where… where they, where they, diverge from the spec, and anything they add that could be useful.
But I do like the idea of only having to maintain one place for docs. One thing I was thinking was, what if the docs became an automated pull request into the OpenTelemetry I.O?
repo. Only problem there is then they technically still… versus a submodule, they technically still could diverge, because somebody could make a pull request that changes them in the I.O. repo.
But translations could live there, but translations should probably live in each, repo as well, though it makes it harder for people to translate, and so I can't… I'm not sure there, but yeah, if English is the main one, then you could have them live in .io. But yeah, for what to work on next, I kept coming back thinking on my own of, just… needing to do that outreach again, to get now what to work on next. Not sure if that's the best path forward, because I like some of these other ideas, but yeah, that's what I kept.
having to… As I tried to figure it out, I was like, I'm not sure. Better to ask.
**Juliano Costa | Datadog** 15:07 On the SDK experience, I feel that, config file.
**tristan** 15:15 Hmm.
**Juliano Costa | Datadog** 15:16 We'll improve things a lot.
But they… yeah.
But I don't… I don't know, maybe we could take a look at the… Or… kind of go back to the… to the… to the Sikhs, and also ask around, like, what they are doing differently as well.
Fuck.
That's true.
**tristan** 15:45 Ian, there is some stuff that came up in the… in the interviews of what companies are doing to make it easier for teams to use it, for their developer… the developers at their companies, that's possible to build on in some community-led way of, they make wrapper libraries to make it easier, or Docker images to make it easier, things like that, so… there's some things to pick at there, I think, as well.
**Juliano Costa | Datadog** 16:17 Yeah, the… the thing that Skyscanner does, it's pretty cool that they already shipped the… the agent within the…
**tristan** 16:26 Hmm. They had me.
**Juliano Costa | Datadog** 16:26 Everyone has an agent when we release a new service.
But the agent is… Has everything suppressed, so people just enable what they want.
Which is I think a nice approach, because once you already have the thing.
enabling one or two feature flag… one or two, like, I want this library and that library is way easier than configuring the whole thing from scratch.
Nope.
But… Java.NET, They are way more mature than the others.
**tristan** 17:06 Yeah.
**Juliano Costa | Datadog** 17:08 Oh.
Not sure.
Do you all think it would be nice to, kind of, work on this?
proposal for the docs, or should we maybe join a comms, SEC meeting and pitch to them first?
**Johanna Öjeling** 17:44 Yeah, I think it's a good idea to, gather their input also.
And… Yeah, see whether they think it's a good idea, or if they also have some concerns.
And about the translation matter.
**Perk (Marcin Stożek) | Elastic Ingest** 18:04 And it's a good, good thing that there is already this, part that is not being translated, which is, like you said, that lives in the other repositories, which is, for example, OpamSpec, so that's a good precedence, I think. I wonder if it would be a good idea to, maybe for me to ping Fabry to make sure that he has this on his radar, because I'm not sure, you know, given our discussion last week.
If he was, like, fully on board, you know?
**Juliano Costa | Datadog** 18:34 suspended.
**Perk (Marcin Stożek) | Elastic Ingest** 18:34 the discussion redirected so much that I'm not sure that's the case. But definitely, I think feedback first is a good idea, you know, to just pitch the idea, learn, like, do you like it at all?
If yes, then we can draft a doc.
So, I'll do it, I'll talk to Fabri, about it, and then, yeah, definitely let's go to the ComSec.
**Juliano Costa | Datadog** 19:02 And I know that… Johanna also, you pinged, where is it?
**Johanna Öjeling** 19:10 Yeah, I think Patrice, as probably suggested for the Kappa AI data, but he's out of office, but Vitor replied. I think Victor is part of the Yeah, maintainer OpenTelemetry I.O. So he mentioned, so my question was, like, if we could get some data, what users ask the AI assistant to figure out, like, where are the gaps?
He didn't provide that, but on the other hand, he mentioned three, ongoing initiatives, or initiatives that, will start soon. One that he mentioned was the Ecosystem Explorer.
Which is, like, an interactive, guide, where it currently has Java, configuration, but… and apparently collector configuration is, in progress.
But it needs to be extended also with other languages than Java.
And then he mentioned a project to redesign the Getting Started section.
And have, like, your wizard, Yeah, and I don't think that project has started yet. And then he mentioned the live OpenTelemetry demo. Patrice suggested this, and Fabry mentioned it last week also.
And I saw you had commented on that PR, Juliana, but now it seems like he will hold off with that initiative, but Instead, providing a dashboard showing real-time telemetry from OpenTelemetry I.O.
could be a simpler solution. I don't know if that kind of ties into the back end a bit, maybe?
**Juliano Costa | Datadog** 21:19 Yeah, I think… I think the Explorer is a good idea. I'm not sure how the Explorer will work, but I think… for folks looking for documentation for specific components on… or how to configure the Java SDK, I think the Explorer will be a nice landing page.
**Johanna Öjeling** 21:38 -
**Juliano Costa | Datadog** 21:39 And… Yeah, so there is only the instrumentation libraries for now, but yeah.
It is something.
**Johanna Öjeling** 21:51 Yeah.
**Juliano Costa | Datadog** 22:09 And, regarding the… the live hotel demo, this is where our discussion, last week Went out, and on the vendor discussion.
So, this… The survey on the… so the OpenTelemptry Getting Started survey, Said that 65% of folks Asked for more… implementations reference, so… But showing what the instrumentation produces.
And not how to instrument stuff.
So this is a bit different from what I had in mind.
But maybe because I'm… I'm always late, Onboarding new stuff, and struggling to get started with, then, actually.
validating what I'm getting. I don't know, yeah, I'm just, like… Yeah, I don't pay for my telemetry that I sent to Datadog, so… This is not a concern on my end. I talk about it, but it's not a concern that I have.
**tristan** 24:08 Yeah, that is one of my recent concerns.
limiting it. I gotta look into the… latest in the configuration file, because I know it's got… some general stuff around, like, HTTP, at least, of… Like, I just wanna… trace one particular path to start with.
Which is… if you just turn on instrumentation library for your HTTP server, you get… everything. And then… then what do you do? And it's like… Well, you can write a custom sampler, and that's a pain to… do when you say, oh, I want a particular path, but I think the configuration file now has something that you can specific to… HTTP say you only want to trace particular pass, but languages then have to support that.
Not just the configuration file, but the per… Per type of… Request filtering.
Good.
But I know that's a place I'd always get questions on, is limiting telemetry.
**Juliano Costa | Datadog** 25:21 One thing that I… that I raised, during Hotel and Plut, the beginning of the year, was… Having some sort of… Flag to… find the telemetry level on the… on the traces. So, like, traces telemetry level, such as we have with logs. So, like.
the bug, error, warning, info. So, like, the bug, you would have everything, but then info, you just get, like, the basic stuff, and… In the tracing, we could have, like.
levels such as, like, boundaries, or I.O, and then you just get the incoming request, outgoing request.
Oh, no, I want, I don't know, I don't know, I want, like, internal response as well. Okay, so you set internal level, and then you get I.O. plus internal.
I got a little bit of pushback from Austin and Ted.
But the… some folks actually, understood my idea, in Ludmila, she said… that we see in a lot of languages the verbosity, which is, like, too high. Like, in JavaScript is a mess. Like, the amount of data that we have, because We have instrumentation libraries for almost everything in JavaScript, so if you just drop in the auto instrumentation and do not look at the data, you would just get a lot of spends for a single, like, Hello World app.
**tristan** 27:01 Yep.
**Juliano Costa | Datadog** 27:02 And, she mentioned something like, maybe… the default should be the I.O.
So instead of having the… this… this environment variable that would configure, we ship everything as the… the default should be, like, just the basic telemetry, and then if the user wants to get more, then they go and change the configuration to say, hey, I want everything.
they're kind of related, but I think implementation-wise is a bit different, but I would be happy with either… either approach. I don't know, though, if that would be something that we would discuss as a developer experience seed, or this is a spec?
Or if we should race to spec.
Sorry, I have to get a couple seconds.
**tristan** 28:02 Yeah, I think there are things we could do around… the spec.
We should raise to them instead of… Delegating.
Yeah, when he comes back.
Can you ask me more about that, because… Yeah.
See, that is useful.
**Johanna Öjeling** 28:22 That's perfect.
About the ideas.
Now I wanted to check, Perk, if… what are your thoughts about the initiatives and ideas we have mentioned so far?
**tristan** 28:35 Yep.
the… I really like… the docs one, Because I've found that to be a pain.
I still don't know how it's gonna work the… I'd like to learn more from… What you were, Trying to get from… Kappa? Is that it?
**Johanna Öjeling** 29:05 Oh, yeah, - Yeah, it would be good to have that data.
**tristan** 29:10 Yeah, learning more there. Especially if… because one thing I've always felt was lacking compared to existing instrumentation, Is metrics, where ours is very low level.
So I've wondered… I'd wonder for people searching for how to do things in OpenTelemetry, particularly if they're struggling with metrics and what they're looking for, because the developer experience there, I think, is lacking. This is very low level, and people have to rebuild a lot of things that they get from existing stuff, like micrometer, or… Prometheus libraries that exist, or… individual vendor metrics libraries.
So yeah, I'd be curious if… people are searching for, like, well, how do I… measure a duration with open telemetry metrics and things like that, because we don't… have anything built in for that, it's very low level, and I think the developer experience could be a lot better there for when people are… trying to… move to OpenTelemetry metrics, because I especially, I think… We have such a better story around naming things and attributing things. Everybody else is putting Application names and stuff in the metric name and things like that, and we have instrumentation libraries, and… So you get the same metric name throughout, The company for things that are the same.
So, like, moving people to OpenTelemetry would be great, but the metrics is just so low level, I see it as a hard thing to sell places.
I don't… I'd be interested in, yeah, their data.
**Perk (Marcin Stożek) | Elastic Ingest** 31:02 There's also one more thing I'd like to add, and I think that that relates to both what Tristan said and what you, Juliana said before.
I wonder what's our story, because I just honestly don't know, right, that, at this very moment, what is our story for the, I saw traces, but I think metrics… metrics is the same. When you instrument… When you use a library that is instrumented, and then you get your spawns, your traces for… staff.
And it really depends whether you are a developer that works on the library, you're interested in different stuff than the developer that is using the library, right? The developer that is using the framework, so you're rather interested in the business side of things, so not I.O, But your business domain logic that is represented in this, you know, library or framework.
So… when you said I.O, that is interesting, but that is tech, and, you know, what about business? What about the domain?
**tristan** 32:10 I really like the I.O. idea, because as I'm instrumenting stuff that I don't know… I don't yet know the details of the code, the first thing I want is just the I.O, because I'm like, well, I know that is going to have, some duration to it versus, certain function calls, and, like, those could be… nanoseconds, but the… I know I want EIO calls. That's what I want. And especially… When we start getting more… Which, you know, I gotta check what we have at this point, because it's been months of… but the profiling… more support for that, is that… People could use profiling.
Rather than tracing when they want that individual function that's going on, versus tracing… putting a span in every function, like people often do, and they end up with a bloated trace versus a… the business logic and the I.O, which is really what, traces, I think, are meant for, in my opinion, but the… Yeah, how to actually get business logic.
Spanned, automatically.
Yeah, tough one.
**Perk (Marcin Stożek) | Elastic Ingest** 33:28 Yeah, yeah, it's… I think it's up for the, like, framework creators, mostly, like, that they know how the stuff is being used.
Naruto.
But then there is a bias again. Like, if you create a framework, you would like to have the traces for yourself, and those are not the traces that your users want.
**Juliano Costa | Datadog** 33:47 Yeah, but then if we have some sort of configuration, it's totally fine to have different tracing levels.
**Right. Because the… Perk (Marcin Stożek) | Elastic Ingest** 33:57 Anything.
**Juliano Costa | Datadog** 33:57 Again, I think that brings us back to the docs discussion. The personas are different, so what they are interested in seeing is different, so… We shouldn't have… TCP and DNS connect, on every I.O. call, because TCP and DNS connect are, like.
instrumented, so… Nope.
**if you are the framework for TCP and DNS, like… Perk (Marcin Stożek) | Elastic Ingest** 34:28 Yeah, yeah, exactly.
**Juliano Costa | Datadog** 34:28 If you are the owner, then you want to work on that. This is the… what you're doing, but… Yep.
So… But again, we are… What?
We are discussing, but I would love to have, I don't know, like, the next steps, or…
**tristan** 34:51 Right.
**Johanna Öjeling** 34:52 Yeah, I'm… I summarized in the meeting notes the, like, ideas we have talked about. I probably have missed on something, so feel free to add it, but I feel, based on the discussions, it feels like the documentation is.
what people, find most important. I get that sentiment. Or… Do you all agree, or… Is this what?
**tristan** 35:24 do that.
**Johanna Öjeling** 35:25 Should we, like, as a next step?
maybe… you mentioned Juliana speaking with the commsig, but should we first maybe, like, write down a pitch, or to align within the SIG what we actually want to achieve, and what the problem is?
**Juliano Costa | Datadog** 35:43 I think we, we discussed… A couple of ideas, right? So, The doc is one about having the templates living on there, on the individual sinks.
And also the telemetry level thingy.
And then Tristan brought up the… the… the point of us going back to the… to the SIGs, and check with them what they are doing different from the spec, and why they're doing different, and things that we can learn from each language, and then have something that we can Eventually.
push back to SPAC, and then… like, let's say that PHP is doing something that is totally different from the spec, but it's good because of XYZ. Then we could maybe pitch to SPAC, and then have all the other languages adopting this.
pattern that is different, because it's better for XYZ, or whatever. So, this is something that I do see value. I think in our initial survey on the 6, we didn't get anything that was, like, super different, did we, Tristan?
**tristan** 37:07 the, the per SIG surveys?
**Juliano Costa | Datadog** 37:11 Yeah, the one that we went to the 6 and messed around.
**tristan** 37:15 I feel like we didn't also get many… as many responses as… Would have, shown us that.
I gotta go back through them, because we… we have them in GitHub.
**Juliano Costa | Datadog** 37:27 Yep.
**Johanna Öjeling** 37:29 So this was a survey run, yeah, for the Sikh members. Okay.
**Juliano Costa | Datadog** 37:36 Yeah, so we had a couple of questions, and then we, we asked around on the SIGS itself. That was before our, external survey.
**Johanna Öjeling** 37:48 Mmm, okay.
**Juliano Costa | Datadog** 37:54 Like, when we started, started.
So those are the, the, I think the three… Points that we… we raised today.
Should we?
Should we draft a doc on, like, those three proposals, or just one, or just two, or just… All of the above.
And… and see what we… we do.
**Perk (Marcin Stożek) | Elastic Ingest** 38:31 like, at least, like, a pitch, so that it's not only, like, you know, like, a couple of words, but, you know, like, a pitch idea. I think, I think that would be good, yeah.
Definitely.
**Juliano Costa | Datadog** 38:42 Okay.
Okay, so adhere a to-do.
**tristan** 39:04 I wonder if we shouldn't also… ping the GC or TC, since they have their hands in all the SIGs, see if they have any feedback on what… Developer experience could focus on.
Just cause they might have… Might know of where people are struggling.
I don't know.
**Juliano Costa | Datadog** 39:57 I… I think there are a couple of things to consider here, Tristan, to actually answer your… your point. It's about the… who are we interested in? Are we interested in people that are already mature on their observability, or that they already have collectors and services instrumented?
What are their pain points, or are we interested in the folks that are arriving to the project today?
and, how they add hotel, and how they get started with hotel. Those are two totally different personas, and I… I don't know what we should focus, I'm just shedding some light to the problem.
**tristan** 40:44 Yep.
**Johanna Öjeling** 41:05 When this, like, started, or it was you who started it, Tristan, or… Could you Or you were involved. Could you share some context on, like, why it was started, and what they were… Ideal for the chili.
**tristan** 41:25 I started… pinging around… so, the SIG… It had an incarnation before this, I can't remember what we… what it was called before, but the… then… died out, and… I… Started looking at, Bringing it back with the idea that the… a number of things in the spec had stabilized, but there wasn't… There had never been that focus on, Not necessarily a layer on top, but at least something in the spec that, eases developer usage, because it was always, especially metrics, was seen as a… sort of low-level APIs that people might build libraries on top of, and so I felt there was a need for to improve, especially from what I was seeing, and usage and questions I was getting with the Erlang Elixir SIG, or at companies I was working at, of usage of these libraries, and the the API and the SDK was just how complicated it was.
So, my focus in wanting to… bring back the developer experience, Sig, was that… focus on, both the API and usage of the SDK, and how that could be improved. The… Then when we started it, we came to the idea that we needed… we should go… Ask, and so there was the… parallel, asking the SIGs, and doing the community survey.
And the… yeah, asking the SIGs was difficult. There wasn't always the feedback, we wanted, like, we weren't getting feedback. And, yeah, the community outreach, we got that… the feedback that, it was complicated just getting started and using how to productionize your collector and your, how companies were actually doing this, so that's the direction we went for the time being.
**Johanna Öjeling** 43:38 Here.
**Juliano Costa | Datadog** 43:52 I… I was here on the first CBT, but, I know that the discussion started before with some TEDS idea discussion, and that's why we have the EU meeting and the North America meeting, but I think the North America one is kind of…
**tristan** 44:14 defunct, yeah.
**Juliano Costa | Datadog** 44:16 Dead, at the moment.
**tristan** 44:17 Mmm.
**Juliano Costa | Datadog** 44:18 Oh.
**tristan** 44:22 Yeah, we should probably… yeah, I never got around to dropping that, did I?
I don'.
**Perk (Marcin Stożek) | Elastic Ingest** 44:31 I will ask you, Teresa, what's the time for you, by the way?
**tristan** 44:33 It's 540 right now. 5.40?
**Perk (Marcin Stożek) | Elastic Ingest** 44:37 Okay, oh man, okay.
**Johanna Öjeling** 44:39 Does the time work for you, or…
**tristan** 44:42 Oh, yeah, yeah, I get up really early. I gotta get up before the kids get up, and they get up super early, so…
**Johanna Öjeling** 44:47 Okay.
**tristan** 44:48 They get up at, like, 6, so, yeah, meeting at 5 is fine.
**Juliano Costa | Datadog** 44:53 I'm totally fine in moving this to later, by the way, so…
**tristan** 44:57 Yeah, if we did it any later, the kids would be up, so it would have to be way later, and then it would… then it gets… Perk (Marcin Stożek) | Elastic Ingest 45:04 Okay, yeah.
**Johanna Öjeling** 45:06 Yeah, I mean, we could also do… I think the collector's say?
us, like, every 3 weeks, North America friendly, every 3 weeks.
you're friendly, and then, like, Aisha, so if you wanted to have this, like, every two weeks in your time, and… the other week, U.S. time.
**tristan** 45:30 Yeah, I think if… yeah, if we get some… more people involved, that… that would help. I think we definitely should do something like that, but… Until then, yeah.
Or until the time changes again, maybe we'll have to switch it up, but as long as it's 5 for me, that's… Perfectly good.
**Juliano Costa | Datadog** 45:52 Oof.
Okay, so, just on the side note, I will open the PR, adding the roles to the… to the main README.
Then we can mention the meritous ones.
What else?
Back.
I think there was an accident on my streak.
Yup.
Couple of cars passing by.
**Perk (Marcin Stożek) | Elastic Ingest** 46:34 Oh, hello.
**tristan** 46:38 Nigga, the… So, pitches, I can do the…
**Juliano Costa | Datadog** 46:43 That's a land con.
**tristan** 46:51 Nice.
I got a kid, too.
I can do the… the interview Sigs pitch, Then we got the docs and telemetry level pitch.
**Juliano Costa | Datadog** 47:16 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 47:16 Yeah.
**Juliano Costa | Datadog** 47:17 Yeah, I… I can do the telemetry level, I think.
**tristan** 47:21 boom.
**Juliano Costa | Datadog** 47:21 Yeah, I… I have some context there, also from the… From the hotel unplugged.
**tristan** 47:30 Great.
Yeah, I like that one.
**Johanna Öjeling** 47:33 then I can give it a go with the documentation. And then, yeah, Juliana, I think the idea originally came from you, so feel free to add to the proposal.
**Juliano Costa | Datadog** 47:48 House.
**Perk (Marcin Stożek) | Elastic Ingest** 47:49 Yeah, and who can create a doc?
So we can put those pictures there.
**tristan** 47:56 Mmm.
**Juliano Costa | Datadog** 47:57 We can start… we can start as a tab here, but I don't think there's anything that is secret on those, so… Perk (Marcin Stożek) | Elastic Ingest 48:05 Sure.
Okay.
**tristan** 48:06 you know.
**Juliano Costa | Datadog** 48:07 Just before we wrap up, I see that there are blog posts on the agenda here.
**Johanna Öjeling** 48:16 Yes, I wanted to give a brief update about the ongoing one. So, for Grok, we finally got in touch with Kelly, the legal person from Grok, so… Now, also a person called Erin from NVIDIA is involved, so I asked Kelly again to review the Google Doc, and let's see if… yeah, hopefully she'll be able to do that, and we'll be able to go ahead with publishing it.
And then, Atlassian, Vida community member who offered to write it, she has started to work on it in the Google Doc.
**tristan** 48:57 Yes.
**Johanna Öjeling** 48:58 And then perk.
**Perk (Marcin Stożek) | Elastic Ingest** 49:00 Yeah, for me, I've secured the recording, and I'm unblocked right now.
Like I said before, so I will start working on draft and share with you guys.
**Johanna Öjeling** 49:11 Oops.
**tristan** 49:12 Awesome.
**Juliano Costa | Datadog** 49:14 Awesome.
Quote.
**Perk (Marcin Stożek) | Elastic Ingest** 49:18 in a row.
**Juliano Costa | Datadog** 49:19 Yeah, have a great rest of Wednesday, and see you all next week.
**Johanna Öjeling** 49:25 We're.
**Juliano Costa | Datadog** 49:26 token.
**Johanna Öjeling** 49:26 You're true.
**tristan** 49:28 Yep.
**Perk (Marcin Stożek) | Elastic Ingest** 49:28 See ya.
**Juliano Costa | Datadog** 49:30 Joe.
