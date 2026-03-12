SIG: Developer Experience SIG Meeting
Date: 2025-12-17
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZNR1fhIgcw6qs3VrHrBOTrmlyRjGG4UxoV7xaBiI4orxvRMHtfqNKuTfmdy13LwV.PcKIHLSTk7aDj9Cz
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 00:36 Hello?
**Juliano Costa | Datadog** 00:40 Hello there.
**Johanna Öjeling** 00:41 Hi! How are you? Nice to meet you. I'm good, thanks. How are you?
**Juliano Costa | Datadog** 00:44 Git, good.
Welcome! I think I wasn't here on the previous meeting, and you were, so…
**Johanna Öjeling** 00:52 Exactly. Hi! Nice to meet you.
**Damien Mathieu** 00:54 Hi! Good morning.
**tristan** 00:56 Morning.
**Juliano Costa | Datadog** 00:58 40?
**tristan** 01:03 Can we wait a couple minutes, I'll be good.
More people joining.
**Nicolas Wörner** 01:07 Bing.
**Juliano Costa | Datadog** 01:09 Indeed.
**tristan** 01:33 There's Petal. Okay.
I think we can… So that's about get started.
Alright, thanks everyone.
Before we get to the agenda, I am almost done with the Donks, blog post.
Juliana, I wanted to ask if… Could you give out write permission to your blog, so we can just make it, each one, like, a document in there, or whatever that tab, or whatever they call it?
**Juliano Costa | Datadog** 02:09 Yes, you, you mean on the… on the master download?
**tristan** 02:13 Yeah, so they can all be in that one… Document.
**Juliano Costa | Datadog** 02:17 Yeah, sounds good.
**tristan** 02:20 I'm guessing you haven't heard anything new.
**Juliano Costa | Datadog** 02:24 No, tristan, you were already editor? Have you tried any…
**tristan** 02:30 Oh, am I? Oh, okay. I thought I was just a commenter, sorry.
**Juliano Costa | Datadog** 02:34 Okay. No, no worries. I actually pinged Heno, on… on Slack, but haven't heard back from him, so…
**tristan** 02:45 Oh, yep, made a tab, okay.
**Juliano Costa | Datadog** 02:48 So, I think we will actually have to open the blog post with them, or to reinforce them, and just, like, go through with everything with them, and maybe that will be easier.
**tristan** 03:04 Yeah, you're going the fast then?
**Juliano Costa | Datadog** 03:06 I'm going for the Hotel Unplugged, which will be one day after, but I'll be at Clausden like, around Fosden, so I don't know, maybe I can just…
**Damien Mathieu** 03:18 crack them down.
**Juliano Costa | Datadog** 03:20 Yeah.
**Damien Mathieu** 03:20 We, we should, go with them together, maybe if it's two of us, that's more, more weight.
**Juliano Costa | Datadog** 03:28 Or intimidating.
**tristan** 03:30 Yeah, what?
Hmm.
**Juliano Costa | Datadog** 03:35 the.
**tristan** 03:36 Get them in an alley on their way, you're okay.
**Juliano Costa | Datadog** 03:39 Awesome.
**tristan** 03:41 Alright, perfect. Wait, when is Fostom? I forget. It's coming up soon.
**Damien Mathieu** 03:45 Last weekend of January? Between January and February.
**tristan** 03:52 Okay.
Yeah. Yeah, I came up with some question, additional questions I have for Doncs, so I'm gonna send those out to them, and hopefully we'll see how long it takes to get a response from them, because of the holidays, but There's a couple things I want, like, examples for, because, like, the… they have… libraries internal, for making OTEL easier to use. I think those are important, especially to this SIG, to understand. I'm curious to know if some of it's just, you know, will be easier with the declarative config.
Once that's available, but it'll be… I want… I'm hoping they can get some example code of what it looks like to set up their hotel, so that gives them, you know, look at… How they're actually doing it, versus, using the… you know, the standard SDK.
Okay, And there are a couple other things I gotta ask them. But, yeah, we can move on to the… The first item on the agenda, which is… Pretty cool.
the MCP server… So, the collector configuration use case?
Pebble.
**PL Pavol Loffay** 05:19 Yeah, hello, everyone.
Yeah, I would like to start the conversation on the MCP, but maybe before we jump into the specifics.
there is… the proposal… the project proposal is still open, and I'm not sure why it hasn't been merged. I wonder if you have any kind of information on that, or if there's anything I should do.
**tristan** 05:47 Those things just take time.
I don't know exactly about the community.
Repo, but if it's anything like the spec repo, even once it has enough sign-offs, people just sit on it for a while. I don't know if there's a… there's not… what is the appropriate place to go to? Because they're not, like, a community SIG.
To, like, raise that.
**PL Pavol Loffay** 06:17 Yeah, I think it has been discussed in the, like, the GC call, but I'm not sure who…
**tristan** 06:23 I can…
**PL Pavol Loffay** 06:23 Maybe… I can ping our GC liaison.
**tristan** 06:29 So, I'll ping… I think… wait, is that… that's Austin or Ted? Is Ted still on the GC? But, Yeah, I'll ping Aston.
**Juliano Costa | Datadog** 06:39 And I think one thing that could help is, at least the… someone from the… this SIG approving the… the PR.
Oh, wow.
**tristan** 06:49 Yeah, I guess since even though… even if we don't have, yeah… Yeah, we don't have… it won't be a green checkmark, but… It'll be a checkmark.
**Juliano Costa | Datadog** 06:58 Yep.
**tristan** 06:59 Alright, I'll go do that, too.
Anyway, I'll ping Austin this morning, once heats up.
But then, yeah.
Maybe it'll get done this week, hopefully, but it could be…
**PL Pavol Loffay** 07:16 I think it's just the formality of the all- To have this content here, but it would be nice to get it merged and then have the… blog post for the…
**tristan** 07:27 this, yeah.
**PL Pavol Loffay** 07:27 according to the conditions.
Okay, thank you. So let's then talk about the… the MCP, finally. So, I think I would like to understand what are your ideas, Nicholas and others, not sure if there's anyone else.
to discuss the MCP, but I think… where we could start is the configuration use cases for the collector, because I think those are straightforward, to do, and… as well, like, most of these MCP servers, they already look at this use case and try to solve it, so I think it's a good candidate to get started.
I started… Doing some work in the… In the collector.
to… Improve the… the schema.
I'll just post here the pull request.
So I have this pull request that essentially adds the JSON schema to the collector.
There are two pull requests. One is… that I shared here is adding the schema generation to MDGen.
Which means that each component We'll have to… we can enable it by default, but the idea is that we make it optional from the beginning, and the component owners can switch on the schema generation in the metadata config.
And… Then… we could consume this schema in the MCP server by kind of getting it from the Git repository, essentially.
It could be as well useful for the docs people, we could get the tag of the repository and download the schemas.
That's one approach. The second approach is via the collector builder, so at the build time.
The… the collector manifest contains all the components, and then the builder has, A flag that will enable the schema generation for all the components defined in the… the build manifest.
It uses the same implementation, essentially, it's just a different way how to, How to hook it up to the… to the process.
I wonder what's your thoughts on this, if this will be sufficient, or…
**Nicolas Wörner** 10:21 Could you share the links to the PRs, or to the…
**PL Pavol Loffay** 10:27 Yeah, just funny.
**tristan** 10:29 In the Google Docs.
**PL Pavol Loffay** 10:29 linked up.
Yeah, yeah.
**tristan** 10:31 I'll put it in the chat, too.
**PL Pavol Loffay** 10:34 I'll just…
**Juliano Costa | Datadog** 10:35 Here, the doc on the chat, if you want to take a look.
**Nicolas Wörner** 10:43 So I will… I will take a look in more detail into the PRs, and I think I can give a better answer, Pavel. But, one thing which I wanted to mention in terms of the MCP server, which I think it's a good idea to start with the MCP server for the configuration use case, and I personally, I think it's a good idea to avoid spinning up too many different MCP servers right from the beginning on.
So we should focus on, okay, how can we bring the MCP server, collector configuration, in a state that it's, like, very nice to use, that people out there start using it, that we maybe even bring it to our official OTEL repo, and that once we have the baseline and learnings from building that first MCP server, we then can also think about, like, other MCP servers. So I would advocate for Starting with that, and then from there, we can use the learnings to, focus on other MCP use cases as well.
That's the first thing which I wanted to mention.
And, in terms of the use case for the MCP, I think the ones which you already listed as tools, are they all already present there? So in the tools MD, are they already working, or is there still some work left which needs to be done?
**PL Pavol Loffay** 12:04 I'm not sure I understand the last question.
**Nicolas Wörner** 12:08 So, in your OpenTelemetry MCP Server repository, you have, like, this ToolsMD file.
And there you list on all the available tools, which…
**PL Pavol Loffay** 12:18 Yep.
**Nicolas Wörner** 12:18 Are all of those already working?
**PL Pavol Loffay** 12:21 Yes.
**Nicolas Wörner** 12:22 Oh, cool.
**PL Pavol Loffay** 12:26 Yeah, so the… maybe I can give a brief overview of the MCD play build. I think there are, like, two main capabilities. The first one is the… Collector component schema, so it exposes collector schema per component and per component version, which is cool because you can ask a diff between the collector version.
It can validate the configuration based on the schema.
And then the other tools… expose the README files and changelog.
**Juliano Costa | Datadog** 13:08 Pavel, just one thing. I think it's related, but not directly related to the MCP. But you shared two different approaches there. One, that you have the schema within the collector, and the second one, that you would generate the schema during build time with the OCB.
My question to you is, if we have the schema already on the collector, wouldn't that also help whoever is, like.
configuring a collector manually, so to say, because it would allow, like, autocompletion and, like, things like that in the IDE, so to say. And the other one wouldn't benefit, right?
**PL Pavol Loffay** 13:51 I think, like, both of them all output the same schema, it's just the schema will be hosted in different repositories, in different places. That's the only difference.
So even if we had the schema in the collector builder, we could still build an integration with the autocompletion in the IDE or whatever.
Yeah, I think it's kind of… I like more the… schema being part of the collector repository, because that's where people already go and look for the config, and it's gonna be, I think, easier for end users, and easier as well for maintainers, contributors, to directly jump into the schema and see what has changed.
And I guess as well for, like, maintainers of the… of the components, if there is a pull request that adds a new configuration, then we'll see it in the… In the schema JSON.
**Juliano Costa | Datadog** 14:50 Totally, yeah, I agree with you.
**tristan** 14:53 Have you spoke to the… Collector SIG, about… This way of generating the schema?
**PL Pavol Loffay** 15:00 Yeah, I was talking about it, I think, 2 weeks ago, I was submitting, The… They were interested, because there's a lot of issues open in those repositories for the schema.
**tristan** 15:16 Right.
**PL Pavol Loffay** 15:16 And… What's his name?
Okay, I forgot his name, but someone will take a look and…
**tristan** 15:29 living.
**PL Pavol Loffay** 15:30 interview.
**tristan** 15:32 Yeah, my understanding was they wanted a… declarative configuration for a while. They've, been working with the… config sig to be, you know, kind of… to be equivalent, so they wouldn't diverge from each other, in how they describe similar things, and so it was… yeah, my concern was that they've wanted this for so long, but they haven't done it, and I was worried there was some, like, major booby traps somewhere in there.
**PL Pavol Loffay** 15:58 Yeah, Pablo mentioned to take a look, but he's on vacation until January 7th.
**tristan** 16:04 Maybe it's just that nobody's ever gotten around to it, so that'd be great if we get that done.
**PL Pavol Loffay** 16:14 But anyways, so yeah, please take a look.
**Nicolas Wörner** 16:16 Yep.
**PL Pavol Loffay** 16:17 And… I think this is, like, kind of the underlying piece that we'll need to solve for the config use case, but anyways, we can start with, the actual MCP anyways, even though we hack something that is maybe not… Directly consumed from the collector repository.
**tristan** 16:40 Yeah.
**Nicolas Wörner** 16:41 Any thoughts? Do you have any thoughts, Pavel, about exposing, like, a public or a hosted MCP server out of the box? So right now, the way… how I see it, you need to spin up the MCP server locally.
And I think it would be cool if maybe we could host somewhere, maybe I can check if we could host it, so that it's easier to hook the MCP server into your agent.
Have you already thought about that, or any plans to… To do something in that direction.
**PL Pavol Loffay** 17:14 Like, do you mean there would be, like… OpenTelemetry hosted GapsCP server that anyone could use.
**Nicolas Wörner** 17:21 Yep.
**PL Pavol Loffay** 17:22 I think for the configuration use cases, it'd be awesome.
Yep.
**Nicolas Wörner** 17:27 Because you probably wouldn't send any sensitive data to that if you just want to connect.
**PL Pavol Loffay** 17:31 Right.
**Nicolas Wörner** 17:31 Okay.
**tristan** 17:34 Is it…
**PL Pavol Loffay** 17:35 Comp, I understand what commands…
**tristan** 17:38 And stuff always… existed on… locally, and so I thought MCP servers did, too. Is that not… is it common to have them hosted? Is there someone who even… that provides that kind of service as well that we could work off of, or is it just so simple, just… you just use, you know, any service provider to host them?
**Nicolas Wörner** 18:00 I, I think, it really depends on MCP. Some you would run locally, some you use the remote ones, and what I like about the remote ones is that it's very user-friendly to use them. So usually, you just run, like, a short command, and then it's automatically hooked into your agent, and you're done.
You don't need to spin up a local server and then, yeah, hook that into, but at the end of the day, of course, it's just… a small user experience improvement. Both will work, but if there is a way, I can also check if my company would be open to host it. It would be pretty cool if it's, yeah, easier for the users just to run the command, and then they're ready and can use that.
**tristan** 18:47 Yeah, that would be neat.
Has there been any thought to, since there already is a schema for SDK configuration, to… start there, or… I mean, maybe we could… if the… And you've talked about… focusing on one MCP server to start, but, I mean, we have… a number of people here interested in building MCP servers, if we could do… Two, one for the configuration schema, one for the collector schema.
Since the configuration schema's already built and almost right at being 1.0.
**PL Pavol Loffay** 19:27 Yeah, I agree, if there is schema, let's do it.
**tristan** 19:32 Okay. Maybe as… we should as well probably discuss, like.
**PL Pavol Loffay** 19:36 Mmm… Some, like, admin stuff, like… Do we have a repo? Like, in which repository we're gonna work, like, and where we want to create issues and stuff like that?
**tristan** 19:50 Yeah, I get the… Yeah, we'll need a… we'll need a repo. Would it… does it make sense to have a single repo for all MCP servers?
**PL Pavol Loffay** 20:02 I would prefer to start with the monorepo from the beginning, and then if it's, like, hard to maintain, then split it.
**Nicolas Wörner** 20:09 A crew.
**tristan** 20:10 Makes sense. Alright, so I guess, yeah, we can… So the… doesn't the… community PR, does that… Don't I have a question, like… What repos do you need, or anything like that, or does it not?
**PL Pavol Loffay** 20:29 -Oh.
Maybe I mentioned the already existing DevEx repo? There is one.
Pay phones.
But maybe I can, No, it doesn't mention it. Doesn't mention that?
**tristan** 20:54 Okay. Well, I can… Bring it up with… GC, when I pinged them about getting this merged, mmm.
what would we want it named, I guess? Would… hotel MCP servers or something?
**Nicolas Wörner** 21:14 Yes, something like that.
**tristan** 21:17 Okay.
**Johanna Öjeling** 21:20 I wonder if we can also create a project for it, or maybe some milestones or issues, but I think that could also help with attracting contributors, or yeah, if we issue that.
I think probably you heard some calls for contributors?
Mmm.
Yeah, it could be easier for people to know how to engage, if we have time.
**Nicolas Wörner** 21:45 I already like the idea, because I see two advantages. First of all, it's easier for us to coordinate, like.
who's working on what, what's the open items which are ready to be picked up. And also, I think a question which I hear from other people who are not too much involved into OTEL, but still interested in it.
what is happening in the world of open telemetry in terms of MCP servers, in terms of AI. So they could go to the project board, and they get, like, an insight what's currently worked on, and that's the other advantage to bring some visibility into that. So, I really like the idea.
**Johanna Öjeling** 22:18 Yeah, that's a good point, and then we can also show that this is the priority first, with the collector configuration, and then…
**Nicolas Wörner** 22:27 Yep.
**Johanna Öjeling** 22:33 Is that something you have access to create for STEM within the… Developer experience, free flow work.
**tristan** 22:40 Yep, I can get started on that as well, so I'll make a note, must don't… And I'll… Figure out adding more people to that.
the… so I'm not the only… well, I know Giuliano and Damien have access to that, but… We'll get more people.
And I'll… Create other issues just for… the… Things we need done, like, the repo, just to keep track of all that.
**Juliano Costa | Datadog** 23:20 Sorry, I think I missed something. So, we are having that on our repo, or our new MCP repo?
**PL Pavol Loffay** 23:30 I'll try to rephrase, maybe, because it's alright.
**tristan** 23:33 I think it's on our…
**PL Pavol Loffay** 23:34 triggered.
**Juliano Costa | Datadog** 23:35 Okay, okay, yeah, okay, so, we'll…
**tristan** 23:38 We can get started.
**Juliano Costa | Datadog** 23:39 to do. Yep, sounds good. No, no, makes sense.
**PL Pavol Loffay** 23:44 So we'll start in the Deluxe repo, and then in the meantime, Tristan will ask GC to create a separate MCP.
**tristan** 23:53 Goodbye.
**PL Pavol Loffay** 23:53 Okay.
**Juliano Costa | Datadog** 23:56 So we do have the to-do for Tristan.
**tristan** 24:14 Oop.
Anything else on MCP servers we should discuss?
Right now… We got… some things to get started on, and…
**PL Pavol Loffay** 24:35 Like, do we want to start building it, actually? Or we want to first… Kind of outline the… maybe the architecture, like, been set up in, like, an issue, and have a little discussion there, and then… Someone opens a first initial pull request for the initial implementation.
**tristan** 24:57 Yeah, I don't know enough about them to say how much architecture discussion has to happen, but, that would be great also just to learn to… if there… if we did do it that way, so I like that… that we can… And we can even start in the developer experience repo, saying, what's our… first MCP server gonna look like, once we have the repo, and… Start the discussion.
**Nicolas Wörner** 25:24 Yeah.
**PL Pavol Loffay** 25:24 We need to, like, pick the language, the framework, and this.
Dope and stuff.
**tristan** 25:31 So there's different frameworks for building these things?
**PL Pavol Loffay** 25:34 Yep.
**tristan** 25:34 Okay.
**Nicolas Wörner** 25:36 I think it's a good idea. So, I already looked a bit into the code of your MCP server, Pavel, but I think it would be great simply to get everybody on the same page to align, and then we can start with something. I mean, it doesn't need to be perfect from the first day on, but simply that Everybody's aligned, and we have a common agreement what we want to use, how we want to use it, how it should look like.
And then we can actually start from building there.
Maybe we can open the issue and discuss there.
**Juliano Costa | Datadog** 26:11 Awesome.
Sounds like a plan.
I think we have one extra item here on the agenda, which is the holiday break.
I think…
**tristan** 26:24 Yep.
**Juliano Costa | Datadog** 26:25 Next… next week, nobody will be, online during the meeting, so… hopefully?
**tristan** 26:35 And then…
**Juliano Costa | Datadog** 26:37 I would say that the next… the following one also not, so…
**tristan** 26:40 Good.
**Juliano Costa | Datadog** 26:41 I would say we skipped two.
**tristan** 26:43 Yeah, the first meeting will be January 7th, because the hotel has an official, like, two-week meeting break.
We come back on January 5th, I think, so the 7th will be our first next meeting, first meeting of the new year.
Lots to… lots to do.
Mute.
There's nothing else, and we can… Break for the holidays.
**Juliano Costa | Datadog** 27:15 Happy holidays, everyone, and hope to see some of you at Auto Unplugged in… Well, we will be back, before that, so…
**Nicolas Wörner** 27:28 Happy holidays, Bryce. See you.
**PL Pavol Loffay** 27:31 It gives you a little bit.
