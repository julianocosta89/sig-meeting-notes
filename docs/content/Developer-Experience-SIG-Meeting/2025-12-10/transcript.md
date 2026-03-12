SIG: Developer Experience SIG Meeting
Date: 2025-12-10
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Damien Mathieu** 00:17 Good morning.
**PL Pavol Loffay** 00:22 Hello, good morning, everyone.
**Nicolas Wörner** 00:51 Hey guys, good morning. Nice to meet you all.
**tristan** 01:06 Right.
Good to see new faces.
One second, who… Maybe we should do a little… Introduction. We can wait one more minute.
See if anybody else joins, expecting at least one more person.
Alright, we'll just get started, maybe he's not coming. So I can kick off.
Zoom.
who I am. We can go around. I'm Tristan, been working with OpenTelemetry from almost the beginning, mostly with the Erlang and Elixir API and SDK, but also involved in the specifications SIG, and now, of course, the Developer Experience SIG, where… which we started, earlier this year or something, and the main thing we've done is the… Developer Survey, which we got a lot of feedback from… about, and… One of the things that stuck out was Usability for… in the documentation, in real-world usage, collectors.
Especially, so that's what kicked off what we've been working on most recently, which is blog posts after interviews with, companies about their real-world experience and setup and how they use it, day to day. So we've been working through those, and… That's been the main work, but those are kind of coming to… Ahead with, we're just working on the blog post now, interviews are done, so we'll be looking to take on a new task, in the near future.
I guess we can go… To my right, which is, Nicholas.
**Nicolas Wörner** 03:34 Yeah, hey guys, nice to meet you all. I'm Nicholas, I work at Ollie Garden, and previously I contributed to the auto collector, so I built the GitLab receiver and the contrapt distribution over there. Not sure if you've seen that. It's basically a component which allows you to create traces for your CISD pipelines.
And yeah, independently of that, I'm, like, very passionate about AI and MCP service in general. And then I saw this proposal from Pubble about, integrating, or about a new SIG.
And I understand that it might be a good first start to add it to the DevExSig as a starting point, so I thought that a pretty interesting topic, that's why I'm here today.
And yeah, nice to meet you all.
**Johanna Öjeling** 04:23 Cool, and I'll go next. Hi, I'm Johanna, nice to meet you all. I work at Grafana Labs in the Open Telemetry team, and I work mostly with OpAMP and the collector so far. But yeah, I'm interested in learning what you're working on in the DevEx lick, and how it can help.
Needs to be here.
**tristan** 04:47 Thanks.
Damien?
**Damien Mathieu** 04:49 Yes, I'm Damien. I've been involved in this thing since the beginning, like Tristan. I am a maintainer of EcoSDK, and I'm involved in the collector. Yeah, so I've been, like Tristan, working on the interviews.
And, the subject I have for today is, that I, we are also kickstarting the Hotel Blueprints projects.
And, We would like to be able to reference every interview we've done so far, and I don't have every contact of the person we've interviewed, and I need to reach out to them to ensure they are okay being referenced.
**tristan** 05:34 Alright, cool. Yeah, put that on the agenda. I can get you that stuff for most of them, I think.
Pavel? Is that right?
**PL Pavol Loffay** 05:46 Yeah, that's right. Good morning. Hello, everyone. Yeah, I work for Red Hat. I've been with the hotel pretty much since the beginning. I am as well a maintainer of Jaeger, and used to be maintainer of Open Tracing back then. Now I work mostly on the operator, but as well One couple of collector components I used to contribute as well to the Java ecosystem in OTEL.
And yeah, now I'm interested in the MCP server, And I created a proposal that is in the community repo and a blog post as well.
And… Yeah, I would like to code this, this work in the… some of the 6.
**tristan** 06:36 And… Andre, are you there?
**Andrei Raiu** 06:40 Yeah. Hi, everyone.
Good morning. Yeah, I'm with Adobe. We are pretty heavily users of OpenTelemnity, at least the collector and the operator. I think you had an interview with Bogdan?
For your blog post.
For now, I'm interested on the MCP, and I'm trying to help as much as I can, with the limited time that I have.
To contribute to the whole project.
And, yeah, came here to see if there's any, any area I could help.
**tristan** 07:18 Alright, sounds like MCP has brought a lot of attention to this thing, that's cool.
But… Bing.
kickoff, in the agenda. It's gonna go through, just updates on the blog post, then we can talk about blueprints, and then the MCP, which will probably be the longest conversation.
blog posts, I don't think there's much of an update there. I've been starting on the… One, the dunks.
Good.
blog post. The company does, like, energy swapping in Germany and Europe.
And, I'm definitely gonna have the draft by next Wednesday. Been going through some stuff recently, but the… Delaying it, but, definitely by next… Wednesday gonna have a draft, and that'll be… I'd like to get… hopefully we can get at least one out before Christmas. It's been a while we've been working on these, so… Mastodon is kind of stalled, but… Hopefully we can get one of the other… Draft's done. We have a draft for a Mastodon blog post, but we've been waiting for approval from Mastodon themselves to move forward with publishing it, so that's what's been kind of delaying that.
But we have some others in the pipeline that should be in the… near completion soon, I'm hoping.
Damon, do you have any other update?
I can't remember which one you're gonna be working at.
**Damien Mathieu** 08:55 Yes, I don't have any… any updates, sorry.
**tristan** 08:59 Beautiful.
Alright.
**Johanna Öjeling** 09:02 Were the blog posts based on interviews that have already been conducted, or…
**tristan** 09:08 Yes. And they're… Most of them are recordings in the… That are in the meeting recordings for Developer Experience Sig on that spreadsheet.
Good.
We can… we should… Consolidate those.
Because it's not clear which ones are which, so you… unless you look through the… you can look through the agenda and figure it out, because we label it in there, and then go to the right one, but yeah, all the interviews have been conducted, I think it's, like, 5… 5 interviews, One blog post is done, the one from Mastodon, just waiting on their approval, and then the four others are in the process.
And so… Damien, for blueprints, I know I… for Grok, I talked, talked to them, and they were, supportive of that, but I'll definitely get you, talk to him again, get him to get his… make sure he wants to be the contact for it, because I know they're… Marketing department's involved, too.
**Damien Mathieu** 10:17 I mean, I think if you have email addresses that I could reach out to, that would probably make things easier.
**tristan** 10:24 Yeah.
**Damien Mathieu** 10:24 but, also for team of Mastodon, Skyscanner, and everyone.
**tristan** 10:30 Yeah, I gotta look at… I know I have Atlassian, Doncs, Brooke.
I have to figure out Skyscanner… oh, wait, no, I should have Skyscanner.
I don't have Macedon, that'll be…
**Damien Mathieu** 10:45 Juliano must have messed it up, I'd ask her.
**tristan** 10:49 Okay, yeah, I will get those.
Is there any update… any other update on blueprints? I don't know if they need… I know they asked for, like, volunteers, and you volunteered. I didn't know if they wanted anybody else to throw in their hat.
**Damien Mathieu** 11:06 I…
**tristan** 11:07 I'm also just, you know.
**Damien Mathieu** 11:08 I don't know. I mean, I think there would be open to any of us joining. I think, there are other people who also volunteered who are not in this sick, so, yeah.
**tristan** 11:19 Yeah, it didn't look like they, you know, needed a bunch, so I wasn't sure if they just wanted one contact from our SIG to be involved, and that'd be fine with me. So, we can stick with that for now, and if, yeah, see how it goes, if there's more help needed, happy to jump in there.
Alright.
Can you give, A little bit on what blueprints are for everybody else.
**Damien Mathieu** 11:42 Yes, basically, we, like, in Visig, we have been conducting interviews, because what we, like, when we started the Sig, the idea was to, improve the experience of developers using OpenTelemetry, so the idea was to, like.
possibly do some spec changes for things that would be currently bad experience. The thing we actually realized from our poll that we conducted last year is that the main problem that we saw was kind of lack of documentation and, understanding of how folks are using OpenTelemetry to see how folks can use OpenTelemetry.
That's why we have been conducting interviews instead, rather than changing the spec and making code improvements, to better communicate on how small and large enterprises are, Using hotel.
And the end user, SIG has been planning something rather similar, which is the hotel blueprints. The idea is to have a registry of Blueprints, like, reference configurations of how people are using OpenTelemetry.
on their orgs, and so the idea is to… like, we never intended to have these interviews be something that we do long-term, anyway. The idea was to pass that on to another Sikh that would conduct that more frequently, which the end-user SIG is really appropriate for that.
And so, basically, the Hotel Blueprints, project is passing on, those interviews.
For long-term, documentation and FAT registry.
**tristan** 13:29 And this is… partially the… due to CNCF graduation, to be able to graduate in the CNCF, is to have these things that other CNCF projects have, right?
Yep.
I mean, Kubernetes has blueprints, and… I don't know what other projects do, but yeah.
**Damien Mathieu** 13:50 Yeah, I'm not sure it's a requirement for the graduation, but at least it's, anyway, a… A good step for people to better understand the project when they are getting started.
**tristan** 14:03 Okay.
Alright, so yeah, that's the other thing that this group is partially going to be involved in, but won't be the sole focus of the group, of the SIG.
So next… we can talk about the MCP, which… I know… very high level, what an MCP is.
So, we could maybe start there with, what it is, and then what is there now? Like, is there a repo? And what… what would it look like for this SIG to be, I guess maintaining it would be the… yeah.
Because they can eat.
**PL Pavol Loffay** 14:51 I can start. Yeah, so the MCP is called… it's an abbreviation for Model Context Protocol. It's a protocol how an agent can… Kind of… Talk to other tools, and then execute some actions in those tools.
what's… does it mean maybe for OpenTelemetry is… the AI agent can… Talk MCP server to… Let's say, configure the collector, or validate collector configuration.
So, essentially, the MCP server can… can give AI agent all the necessary information, to then… to enable the AI agent to execute some action, or the MCP server can execute that action directly. So, for instance, the OpenTelemetry Collector can have MCP server, AI agent would call this MCP server that runs in the collector to, for instance, like, enable additional components on the collector, or disable it, or change configuration, or ask collector which components are available in the build of collector, or what is the configuration for that specific collector component?
No.
And then AI agent can, you know, call these tools and get the final result that, user requested.
in the prompt, let's say, configure the collector with… for log collection in Kubernetes.
Right, and then there can be, like, series of calls to the MCP server to… To implement this use case, essentially.
**tristan** 16:47 Okay, so it's…
**Nicolas Wörner** 16:50 Yeah, so… One thing I wanted to add, the way how I think about MCP, or I think if you really break it down at the end of the day, what it is.
The, the, the way, or… the AI agents, it's all about the context, right? So, what you feed to their context window, and based on that, they will do something.
And, those MCP servers, they really help to kind of guide the agents, or the LLM, to return better results for whatever you prompted to do something. And that's in the end, or at the end of the day.
what the MCP servers are about, to give the AI agents better capabilities to return better results.
**tristan** 17:34 Okay, and it's mainly about expo… like.
The data it exposes is more the collector configuration than… and what's in the Collector image.
**PL Pavol Loffay** 17:46 Listen.
**tristan** 17:46 It is, like, any telemetry.
**PL Pavol Loffay** 17:49 I think it's… it's… it's two things. It's… it's about this context, what Nicholas mentioned, that, the MCP returns, like, text information that will help AI agents to do something.
or MCP Server can execute that action directly. So it's like an API for AI agents to directly interact with the tool. In our context, the tool is the collector, or it can be OAMP server.
what else? Instrumentation, probably not, but, yeah. So what it can as well do, like, if we build an MCP server on the collector.
it can as well return, like, live data for the AI agents to understand what is being collected, and then use this information to, you know, to change config as well, or do some other action in different tools, for instance.
**Nicolas Wörner** 18:45 Or another quite simple example could be, so when we think about the semantic conventions, if you would give all the different definitions about the semantic conventions which are out there to the LLM, and to kind of tell the LLM, read all those definitions, it would, like, explode the context window, but if you would have an MCP server who is optimized for guiding the LLM, how to retrieve the relevant semantic conventions for the use case the LLM is working on, then you would work with the semantic conventions much, much more context-deficient.
So, yeah, it's kind of really, like Pavel said, two things. On one side, the, context optimization, and on the other side also that we can pair it with some deterministic actions to kind of like an API, where the LLM then can execute those actions.
**tristan** 19:33 So the semantic convention example might be there would be a component in the collector that tracks what versions of the semantic conventions has been seen in the telemetry.
And then, if it's asked for it, it's able to say, these are the… what I've seen.
**Nicolas Wörner** 19:49 I would see the semantic convention example more as part of, like, the development workflow, so imagine you're kind of doing some manual instrumentation in your code, and you're thinking, hmm, what semantic conventions could apply to that certain part which I'm instrumenting right now?
And then you would basically use the MCP server to get the relevant semantic conventions, which are up-to-date for whatever you're trying to instrument.
**tristan** 20:12 I got you. So, separate from the collector, this is…
**Nicolas Wörner** 20:15 Yes, it's, like, different use cases.
**tristan** 20:17 Okay, so the MCP server, it's gonna span, okay.
And because OpenTelemetry doesn't have, like, a… storage format. There isn't any… thought of the… like, Honeycomb has an MCP server that, lets you talk about the data, the telemetry that you've collected, like… There isn't any of that gonna be going on, because we don't have a file storage format.
**PL Pavol Loffay** 20:45 Maybe, maybe we could build some cash on the collector to support some of the common use cases.
**Nicolas Wörner** 20:53 Don't good.
And I think one big challenge, or the problem we're seeing right now, is there are those use cases we just talked about, like the semantic conventions, the collector, and I'm sure there are other cool use cases out there which could also be beneficial.
But right now, there is not really a common place where we can talk about those topics, where we can also maybe streamline the way how we develop those servers.
which will then also, of course, result in different user or developer experiences, which means, you have different setup steps, you have different configuration requirements, you will also have different quality, in those MCP server implementations if there is no alignment, and really the thing what Pavel and myself are looking for is, like, that common place where we can talk about those topics and align the implementation and just exchange.
**PL Pavol Loffay** 21:46 Yeah, and anyone can come here and kind of contribute their use cases and what they would like to achieve.
**Nicolas Wörner** 21:52 Nope.
**PL Pavol Loffay** 21:52 And I think the, kind of, the topics that are being discussed in this SIG are very relevant to MCP. Like, MCP is… kind of… an alternative approach, how people can… how end users can get stuff done, right? Instead of studying documentation manually, they can just prompt AI agent, and it will make things happen, essentially, if everything works right, and… but that is a problem, like… Right now, the things don't work. We need to make… we need to do some work in the core Autel components to make it work nicely with agent workflow.
**tristan** 22:31 Cool, I see there's a blog post, I'll give this a read, too. The… so there is…
**PL Pavol Loffay** 22:39 So, there are… yeah, I wrote this blog post, I wrote one MCP server. In the open source, there are maybe, like, 3 or 4 more, maybe 5.
They… all overlap, I would say. They all look at… or they try to simplify the collector management, like the configuration.
Well, that's one… kind of set of use cases, and the other set of use cases is around the… I call it data profiling. Essentially, you want to ask questions about what data is being collected by the collector.
**tristan** 23:14 This is what Niklas as well mentioned. It's a bit more difficult use case, because we don't have store in OpenTelemetry.
**PL Pavol Loffay** 23:21 But we could definitely… support some of these use cases in the collector by building some… API layer that would expose some of the live data.
**tristan** 23:36 Okay. Yeah, see, maybe.
**PL Pavol Loffay** 23:40 I can maybe talk about the, kind of, examples that I, put in the blog post.
the…
**tristan** 23:48 Yep, that'd be great.
**PL Pavol Loffay** 23:50 The interesting one was, for me, is, like, in the MCP that I built, I can… my AI agent has access to Kubernetes cluster, and in my cluster, I have a couple of collectors running, and there is new OpenTrometry Collector version that is released, and I want to upgrade, but I'm not sure if… has anything changed, you know, in the upstream? So I can ask the MCP server, like, hey, I'm running OpenTelemetry.
Could you please check if I'm running If I need to update anything for the upgrades.
And it will get the collectors that are in the cluster, it will get the version, then it will ask MCP Server for the… For the changelog of the next version.
On top of that, it will ask the… the configuration schema for all components that I have in the cluster, and it will compare if there is any, you know, deprecated fields, and it will give me a summary of what I need to change to properly upgrade.
Right, so it can list, like, okay, you are running these deprecated fields in this component, and you should migrate it to a new configuration.
And things like that.
**tristan** 25:15 Nice.
**PL Pavol Loffay** 25:16 then other use case, like, I want to collect logs on Kubernetes. Like, I don't know what is the configuration for it. I can ask MTP Server to create me the collector config for this use case.
And then again, it will… it will get the, kind of the README files, so it understands which components need to be enabled, then it will get JSON schema for those components, and configure those, and produce valid configuration. I think that's important. Without the MCP server, it often happens that It will hallucinate, it will create a configuration that is not really valid.
That's… that's very problematic, and, in Autel, like, in the collector's SIG in general, there is no… collector component schema, right? So it's… this very fundamental piece that we need, it's not there, for instance, so… I think when we will start building the MCP0, we will need to kind of build this, pieces, to support these use cases.
**tristan** 26:27 As in, like, per contrib component schemas?
**PL Pavol Loffay** 26:32 For instance, yeah, I just started working on the… config schemas, there is a draft PR open on the collector.
So one idea is that we can extend the collector builder, and the collector builder at the build time would analyze the source code and would create the JSON schemas for components, and then we can use this in the documentation, but we can as well use this in the MCP we could as well maybe put this into the collector component that would serve this at the runtime. There's many things we can do with that information.
**tristan** 27:12 Yeah, and if it's able to work with JSON schema, now that we have a file format for configuring SDKs as well, it could be used there. So, another use case is configuring your actual SDK and talking about it.
How do I… Properly configure this, because that's not easy itself.
Nice.
And I see there's… So, in the repo.
Link to in the blog post, that there… it links to… What is it?
4 other MCP servers? Is there any… I take it… the idea is sort of to have one of these get donated to OpenTelemetry and become the Standard.
**PL Pavol Loffay** 27:55 Dude.
**tristan** 27:56 Kind of merging.
**PL Pavol Loffay** 27:58 I think… to create MCP server, it was not that difficult, I would say, but we should definitely, Kind of take the learnings, that we had from those, and… talk about the use cases we want to solve, and start designing the… the MCP capabilities that we want to build.
And then it's gonna be pretty straightforward, I think. Gotcha. What is important is this, these authors that created the MCP series, they're all, I think.
I'm happy to… to help and contribute, in this… in this common effort.
**tristan** 28:43 Okay.
**Nicolas Wörner** 28:49 No, so I think… at least right now, how I feel about it is that we will probably end up with multiple different MCP servers.
Maybe we'll find a way to put everything into one, but based on my experience, it's better to kind of split based on what the MCP server is supposed to do, because otherwise you will end up uploading stuff into your context window, which you don't actually need. So if you have like, I don't know, the collector MCP, what Pavel talked about, and then you have, like, a completely different MCP. If you combine that, you end up with the risk that you only need a small portion of that MCP server.
So, I'm not sure how the exact future or the exact implementation of all those servers might look like, but that's one thing to keep in mind, that we likely or eventually would have multiple different MCP servers with different use cases.
**tristan** 29:43 Okay.
So, like, the SDK configuration might have their own MCP server. Right.
**Nicolas Wörner** 29:49 Right, right.
**tristan** 29:50 Okay.
**PL Pavol Loffay** 29:51 Yeah, and maybe, like, there as well this, like, Cloud Code has these, plugins, that have, that have skills, and, Is it tool? No, it's not tool.
comments, right? So maybe some of these could be actually, implemented not as MCP, but as kind of other approaches that the common agents will understand.
**Nicolas Wörner** 30:17 Yep.
**tristan** 30:18 Okay.
**Nicolas Wörner** 30:19 And another thing, I think is… I've seen an issue about that somewhere already, in our documentation, in the OpenTelemetry documentation right now, we don't have a way to just view the plain markdown format of the documentation, and that's also something which is super useful for those agents. So if you would have, like, the options to maybe add an LLMs.txt at the end of the URL, And then you get the markdown format of the documentation, or, like, a button you can click, and then it opens a new tab where you have the option to copy.
the whole contents of the documentation is marked down. That's also something which you will find in a lot of documentations out there, what more and more, like, frameworks or documentations are adding, which makes it, again, easier for agents or kind of LLMs to interact with that knowledge or that, Yeah, information which is encoded in the documentation.
And that wouldn't be, like, a MCP server, but still something which I think the auto developer experience or the ecosystem would benefit from.
**tristan** 31:22 Yep.
Okay.
Good note of that.
So what would the next step look like, if we were to… Take on this project.
**PL Pavol Loffay** 31:58 Yeah, probably… I think what we want at this point is… A place where we could meet and…
**tristan** 32:10 Discuss the… the agenda, and…
**PL Pavol Loffay** 32:13 Based… On the outcome of those discussions, we will start working, As it was probably mentioned, like, we will need to make changes in the collector, maybe in the docs, and then… as well, produce some MCP server that will be maybe standalone, maybe will be part of the collector. We don't know yet, but we need to start talking about these use cases that we want to solve, and… So, yeah, have a place, and then do some… Announcements, so other people that are interested could join as well, and contribute.
**tristan** 32:50 Nice. When is this, MCP blog post gonna go out?
**PL Pavol Loffay** 32:56 So, this MCP blog post is blocked at the moment on the decision that we… on the… on the Sikh decision, essentially.
**tristan** 33:05 Okay.
**PL Pavol Loffay** 33:06 So it could be a place where it's announced.
Maybe, yeah, or maybe we establish, kind of, the sub-sig, and then we have another blog post that announces the… the subseq, and for people to know that they can join and contribute.
And then maybe we don't even publish the blog post, and we create something else, and we publish that. But, the whole idea with the blog post for me was to… get people interested, in the MCP server.
**tristan** 33:42 Yes, okay, that makes sense.
Alright.
Well, yeah, next steps sound good, we decide if this is the right place, and… Get more people in who are interested, discuss use cases, and then we can architect from there, based on the use cases.
Figure out what this… Things gonna look like.
Okay.
I don't know what the process should be to… Decide.
If this is the place MCP servers should live, I know.
Juliano is missing.
Today.
**Damien Mathieu** 34:29 I mean, Pavel was here last week, so, and we, while chatting last week, we determined that it was better to, for more folks to be here to have a project presented. But last week, Giuliano was, I think, not against,
**tristan** 34:48 Oh, okay.
**Damien Mathieu** 34:48 of, having VMCP join us.
**tristan** 34:53 Yeah, I think, I mean, I don't… C… I see it as a… dev experience thing, so it makes sense. The… the… and… maybe eventually it would need to spin off into its own SIG, but since we're… Open to, you know.
new work and new projects, I think it makes sense to start here instead of all the work of creating a new SIG, and then if that… if it becomes something that needs to be spun off, it always can be. That's something… It's open in the future, so it's not like a… There's a reason that… That's more said in the beginning.
**Damien Mathieu** 35:36 I also think the DevExig with, our projects, has been a bit struggling, with, participation, and maybe, getting the MCP, with us will help.
**tristan** 35:50 Exactly.
**Damien Mathieu** 35:51 Show that developer experience is important.
**tristan** 35:54 Gotta ride the wave.
to where the… Where the people are.
Yeah, I like it. So I'm in favor.
I don't know if there's… If that's enough, with… the three of us who have been the main people of this SIG.
For quite a while now.
like… That should be enough, to say that this could be the home for the MCP server for the foreseeable future, I'd say.
**Damien Mathieu** 36:27 I mean, I don't think we have to fret too much about it. If we say we are fine, let's… Kickstart things, if we realize it doesn't work for reasons.
Then things can change.
**tristan** 36:41 Yep. Always spin it up.
Alright, yeah.
sort of…
**Damien Mathieu** 36:46 I mean, it's… sorry, I have a bad joke, it's not Erlang, things are mutable.
**tristan** 36:53 I won't allow it.
the… So yeah, we can, get started then. I think it sounds like the next, step is the, you know, get the word out, however best that is done. A blog post would be nice to… and get more people…
**Damien Mathieu** 37:19 We lost Tristan.
**tristan** 37:21 We could see, I don't know how fast we could get something out. What's up?
**Damien Mathieu** 37:24 We lost you for a couple seconds.
**tristan** 37:27 Oh, yeah, says my internet's bad.
But yeah, no, I was just saying that I'm wondering how fast we could get a blog post out about this, announcing the Developer Experience SIG is gonna host this, so that people will start joining us, and we might have to start I might have to start attending the North American meeting again, because there'll probably be people that don't want to get up at this time of day who want to be involved, so, glad we… Never got around to getting that off the calendar. That'll be important to mention in the.
**Damien Mathieu** 37:57 any blog post, that we have two meetings. And to that, I want to say that, I mean, if needed, because that's better for contributions, we can also move this meeting, like, there are, between Europe and the US, there are overlaps, in times.
It's, so, yeah, we could do it end of the EU and, start of the US, but…
**tristan** 38:21 Yeah, I think the issue with that was PST was… Really, really early.
It'd be, like, 7 AM.
**Damien Mathieu** 38:28 Yes, and then it's, late for, EU, but yeah.
**tristan** 38:32 Right. Yeah. Yeah, maybe it'll work, so… But yeah, we can consider that as well. I guess we can find out who… Joins and stays around, so we can start it by saying, you can join either of these times, and we'll see who, and discuss, you know, if we need to pick a new time.
So was… bevel…
**PL Pavol Loffay** 38:56 Yep.
**tristan** 38:56 Volunteering to write this blog post.
**PL Pavol Loffay** 38:58 Yeah, I think first that we should update the, the proposal on the community repo, and market, like, we will host this in Visig. Get it merged, and yeah, I can then work on the… Announcement blog post.
**tristan** 39:18 Okay, let me see… Okay.
Project proposal… So, you're gonna update the text of the project proposal, and… Yeah, I can ping in there that we are… in favor of this project joining the DevExSig, and then we should be good on that end.
Cool.
And… Well… Is there anything else on that, or another topic we should discuss now? Otherwise, I'll get, posts into that community PR, that'll get updated, and… Maybe, Nick.
Wednesday, we can discuss the… draft of the blog post, or, I mean, if you got it sooner, then we can try to get it out, just post it in the DevX, channel on… Slack, and we can review it and get that out as soon as possible, so we can get people who are interested and involved, so we can really start hashing out use cases and architecture.
**PL Pavol Loffay** 40:43 Okay, well, COVID.
**tristan** 40:45 Cool.
Alright.
Anything else from anybody?
Otherwise, we can call it here.
Thank you, everybody, for joining. It's great to see lots of new faces.
Hope to see you even more.
**Nicolas Wörner** 41:05 Right, thank you guys. Bye-bye.
