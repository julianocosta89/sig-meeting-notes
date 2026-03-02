SIG: Governance Committee
Date: 2026-01-28
Duration: 69 minutes
Zoom Recording URL: https://zoom.us/rec/share/io8q2T_gPJpuhHyORVa7inxyZmfI7BT8Xi92qATHUsf8c2xFzhttH2XyC0hL62px.qX7cEuGdMSdk8IhM
============================================================

## Zoom Recording Transcript

ploffay 00:00:14 Hello. Hi, Seren.
Severin Neumann 00:00:17 Hey, Pamel, good evening.
ploffay 00:00:20 Good evening.
Severin Neumann 00:00:23 It draws.
Trask Stalnaker 00:00:23 Have a…
ploffay 00:00:26 So, right there.
Juraci Paixão Kröhling 00:00:37 Hello, hello.
Severin Neumann 00:00:38 Hey, Urasi. Hey, Pablo.
I forgot to let Lydmilla know where we are. She also wanted to join us for the MCP discussion we have in the beginning. Let's give her a second.
Alolita Sharma 00:02:37 Did you pay her, Simon?
Severin Neumann 00:02:39 No, she pinged me and said, like, hey, can you give me the Zoom link?
Alolita Sharma 00:02:42 Okay, okay, I see.
Good cook. Hi, everyone. Good morning.
Morning, good evening.
Yeah, I'm hoping everybody… most folks are going to Fostom. I'm sorry I can't make it. I love Fostum. I've been there many times.
Severin Neumann 00:03:04 I think we have a good quorum of GC and TC people coming.
Alolita Sharma 00:03:08 Yeah, it'll be fun. It's… Boston is a great conference. Yeah.
Severin Neumann 00:03:12 Yeah, looking forward to it.
I think we should get started with, like, our…
Topic with guests, so we can get into the rest of the agenda.
Alolita Sharma 00:03:24 Yes, absolutely.
Severin Neumann 00:03:25 I tried to timebox it to 15 minutes.
I don't know, what else do we have in the agenda if we… If we need any longer.
I think we have 10…
Yeah, maybe we can do 20 minutes, depending on the time, but yeah, as I said, let's get started, maybe.
Alolita Sharma 00:03:45 Yeah.
Severin Neumann 00:03:49 Exactly. So I asked Pavel, or Pavel and I were chatting about the MCP proposal, and I was like, yeah, maybe… maybe it's best to… to have everybody on a call to quickly chat about it. So the proposal is out now for 3 months, and there were…
let's say a few discussions back and forth, and I think what's… like, there's… overall, I think, one big blocker, and that's more or less like, okay, how does this project relate to…
to all the other six, to all the other work that other six are doing, right? Like…
If this project is building,
MCP server, or instructions for a MCP server for the collector, what does this mean for the collector's sake, etc, etc. But maybe, Pavel, you can explain it better, and let Mila as well, maybe you can… you shared something today already in a chat. Maybe you can kick it off from here.
ploffay 00:04:45 Yeah, absolutely. Thank you, Severin, for the time that I can be here. Yeah, so our goal is to build… it's not necessarily to build the MCP server, but to enable open telemetry with agent inquiry flows.
we want to make sure that if someone, a user, is using AI agents, that agent is able to use OpenTelemetry effectively, right? So it will not hallucinate, it will produce, good
configuration results or good decisions that a user asks about the OpenTelemetry stack.
We kind of recognize that OpenTelemetry is a wide ecosystem. There is a lot of components that are created separately, independently. They often are not compatible with each other.
And this poses an issue for end users, and our goal is to solve this with agent group flow, because agent can have access to
Much more information than a human, and can understand the wide ecosystem much better than a human.
So our goal is to, kind of, make the OpenTelemetry…
Knowledge, which means, like, documentation, code, and configuration, available to…
to agentic workflow. We don't want to, kind of, build, kind of.
competing documentation, or competing configuration, or anything kind of duplicate. We want to work with the individual 6, and kind of enrich their,
what they have, which is, like, documentation, or the way how they produce the configuration examples, or whatever it is, and then just take it, maybe repackage it, but somehow expose it for an AI agent so it can use, that information to…
to solve user queries, for the open telemetry.
this interface is usually the MCP server, but it can be as well the skill, the agenting skill. We don't know…
which…
one we will use for which use case. We'll probably use the one that makes the most sense, and…
And that probably needs, as well, a lot of experiments, and a lot of user input.
But the goal is to kind of enrich what we already have, kind of increase the stability of the project, don't create any duplicates, just enable users to use
the latest and greatest bits from OpenTelemetry with agentic workflows. So I was, like, experimenting with the cloud code and trying to configure the collector, and I realized that many times the agent will produce incorrect configuration, and it's…
it's very clear that it produces incorrect configuration because we don't have official schema of the configuration in the collector, right? So, even I, as I work on OpenTelemetry from the beginning.
I sometimes fail to produce valid configuration, because there is so many components, there is no schema, there is… the documentation should be, improved a lot.
That's one example. The other example is there's a lot of
even other documentation of OpenTelemetry out there. For instance, at Redhead, we have lots of hotel docs, and as OpenTelemetry kind of,
goes forward, a lot of this configuration becomes obsolete, because the configuration changes, and it's hard to maintain it. It's, again, like, something that AI Agent can effectively help with to maintain. And I think end users have these, problems as well, like…
They maintain the collectors in the… with GitOps. There's large configuration files, the…
The configuration evolves, and they need to make good decisions on how to migrate it.
Liudmila Molkova 00:09:11 Yeah, thanks, Pavel, for the context, and I… I love the goals of the project. I think what you're saying makes total sense.
To explain where my concerns are coming from.
So, I don't know Collector enough, I would let Pablo and other people who work on this, comment. When we, let's say, start talking about instrumentations or semantic conventions, there is a lot of prior art.
And there are a lot of things we are planning to do there.
And, like, if you…
let's say the collector phase of this project is done, and you move over to, let's say, Weaver or semantic conventions. What we would expect, that you come and work with the existing SIG,
Because we… we have code generation, we have schemas, we, like, would love you, to…
tell us how to do things, and what we are missing, and we will fix it in the product itself, right? So I think, like, 90% of problems already in the product, like the lack of the schema or lack of the documentation, they are about what the Sikh produces.
more than it's about the MCP wrapper or skills around it. It's my impression, I'm not sure if I'm right or wrong, but this is my feeling, and
the… I feel like you… if… if we were talking about Weaver, or semantic conventions, or instrumentations, you would be much more successful with it if it's a sub-project within the SIG.
Not a thing on the side, at least in each particular phase.
And I don't want to talk over the collector, folks, but my impression is that this collector, he might be more successful as
part of the collector SIG, a sub-project in the collector SIG, and they know what you do. Because the risk is that, okay, you build something on the site, and they don't know.
ploffay 00:11:10 No, no, no, no, no, we want to exactly avoid the situation, like, we don't want to build something…
I think each Sikh is, like, the domain expert in that area, and we… our goal is to collaborate with them, on creating
that core functionality directly in DeadSig. And our goal is to just bring the expertise of how users
think about using agent equipals across the six, because that's very important. If you do something for, let's say, Java, but it's missing for Golang, or there is missing or competing
kind of tools that will confuse the AI agent for a different sake, then the whole experience will… will not be there, right? And I think
There's this whole opportunity that if we start from the beginning building this.
Across the six, we will have much better success of achieving some coherent behavior.
Liudmila Molkova 00:12:17 Yeah, it makes sense. I see some hands raised, I'm curious what other people think.
ploffay 00:12:23 I can as well maybe give you one example about the collector. We already worked with Pablo about the schema.
So it's just one example that,
It's not about rebuilding something, it's about enriching what we have, and then just repackaging that.
So that it can be used in the, agentic workflow.
Severin Neumann 00:12:47 Graci.
Juraci Paixão Kröhling 00:12:48 Okay, I… Zoom always plays tricks on me, so I never know when it's my turn. So, I have… I have a few comments there, and I think there are good reasons, good arguments on both sides. I guess one is.
I would certainly defer to the collector folks to tell
AI agents, what is good in terms of the collector, so I can see that.
On the other hand, I also would not like us to apply Conway's Law here. Like, we should not be shipping our organogram to our users. So we should not be having, like, one MCP or one SKU or whatever per SIG.
people who are using OpenTelemetry, they should be able to consume one thing, or perhaps, I don't know.
two things based on the roles that they have, like for platform engineers, and perhaps one for containing collector plus Helm charts plus operator plus whatever.
OTTL, and then another one being instrumentation-specific. But then I think it's more like an organization for…
Like, how do we ship this thing, this thing here, instead of breaking on a per-seq basis?
So I guess my point would be, we should be having two separate discussions, perhaps. One is, how do we organize the context, how do we organize the knowledge base that we want to give our users? And the second one is, how do we ship that, to the users? Like, how do we, like.
how do we entice Ruby, Rust, and so on, folks, to create their context, and then how do we consume those at top level?
kind of user-facing… deliverables.
Ted Young 00:14:32 Yeah, this was, helpful to hear, directly from you. Just realizing, like, I think one of the confusions I had was around, like.
Is the point to try to build a canonical MCP server and say, everyone using OTEL, all the vendors, everyone, you know, like.
base your MCP server off of this thing we're building, or something like that.
But it seems like that's not really… the point is more to create the raw material.
for an MCP server, or any other AI use.
And a lot of that raw material, I think there's some ways to do it that would be, like, just for AI, but there's, like, plenty of examples. I certainly, when I think of Weaver and stuff like that.
Where it's just things like, semantic APIs, right? Like, taking the Java model of an instrumenter, an HTTP instrumenter, trying to use Weaver to…
To generate, you know, more code objects, and that would naturally make
You know, agentic coding work better?
But if that's the approach you're taking, I feel like one… like, a big project file that's, like, all the kind of MCP stuff we're trying to do, I think that approach might be confusing.
to the community.
It's almost like… if we're gonna… I would encourage you to sep… more firmly separate
building a server at all, or why we're building it? Are we building it just to test, to make sure the other stuff we're doing is just working, and it's just…
A proof of concept.
Like, making that clear, and then maybe breaking it down from one project to these, like, different projects in these different domains where you're gonna go try to improve this source of information, improve that source of information.
Because, like, what other people are saying is, like, a lot of that work sounds like it's more like…
you're going into other SIGs and into other places, but you have, like, a unified goal.
And we haven't thought about making projects, like, from that perspective before, using our projects, but it seems like a natural next step to me.
To say… and we've already had SIGs show up and be like, we want to create a project, but we don't want to create a new SIG.
So, to a certain degree, this feels like trying to figure that… that stuff out.
Because, and part of the reason I say that is I'm conscious of, like, if we're like, yeah, go get them, you know, AI MCP crew, but what this really means is, like, that crew's about to, like, dogpile on the collector SIG with a bunch of PRs and stuff.
It's, like, part of us trying to manage
things is just, like, seeing that and being like, well, let's check in with the collector SIG first, since we know you can't make progress without them.
just trying to catch those things ahead of time. That's a lot of what we're trying to do with the projects.
So I think, maybe…
my advice would be maybe after this, coming back with, like, actually breaking it down into smaller, separate projects, based on who else didn't open telemetry, you're gonna need besides the people interested in AI stuff.
To work with you.
Because you can probably separate it based on different groups, and if you separate it that way, then we can see which groups are super busy versus might have some time right now, and then…
Figuring out how to make progress might be easier.
Anyways, that's my piece.
Pablo Baeyens 00:18:23 I'm just going to briefly mention the experience with the collector, so,
for the collector schema, this is… the configuration schema, this is something that we've wanted to do for a while, and there were various initiatives. I think,
Pavel help, like…
using the momentum of the MCP stuff to… to get this moving, and, like, it was done within the collector's stake, it was…
I think so far, a pretty positive thing for the collector, something that we wanted to do, and this helped us do it. And…
Then the other thought that I had is…
we do have examples of SIGs, like the security SIG, that are, like, more cross-cutting. I don't…
feel like we are the best at making that work, but we do have the example of SIGs that collaborate on different SIGs, or try to get things done on a more cross-cutting way.
Liudmila Molkova 00:19:35 So, it sounds like, we don't… we share the… we understand the goal, and we share it. It's just, it's the phased approach, and maybe the first phase is to… the first phase is to identify
the SIG, and then we would need some sponsorship from the SIG.
ploffay 00:19:56 I think…
just… let me jump real quick. I think finding liaison in the Individual 6 makes sense, but at the same time.
for instance, in the collector, we know that we need to do some groundwork to build the schemas, but for, let's say, the declarative configuration, there is already a schema, which we can directly take a rig package, and maybe there is zero work that will be needed done in that SIG, right? So.
It's hard to…
figure out what will be the needed work to be done in those individual six. And we will figure it out once we will start building the actual stuff.
Liudmila Molkova 00:20:43 Benjamin, maybe…
ploffay 00:20:43 We know that we want to… we know that we want to start with the collector, but there's as well some low-hanging fruit that we can…
Implement pretty easily.
Liudmila Molkova 00:20:54 Sarah, Alolita, go ahead, I didn't mean to cut you off.
Alolita Sharma 00:20:56 No, no, no, no worries, Ludnula, did you finish what you were asking?
Because…
I had… I had a couple of, questions. I mean, obviously, Powell, I'm very excited about the, you know, I think everyone's looking forward to having an MCP server, you know, attached to a hotel, but to Ted's point, again, I think the scope of where, you know, you start is very important, because obviously the collector config is a great
you know, focus area, and that would help everyone who's using the collector everywhere. I can tell you, you know, exactly what you described in terms of having very long config files, you know, which we end up maintaining, downstream, is a big, huge challenge all the time, and, you know, GitOps is not ideal.
for maintaining configs, for example, which are so, so long. For the collectors, obviously, the collector health as well as the collector config are very, you know,
Nice areas that could actually be…
be assisted by an MCP, you know, player. That said, to Ted's point again, I think it's…
you know, instrumentation and, being able to support the instrumentation and language SIGs is different from supporting the collector, features, right? Well, and…
Having a scope would be useful, because, obviously there are very many complexities within the instrumentation. Like, yesterday I was having a detailed conversation about,
How, you know, models could be…
instrumented, you know, in a standardized way for every language. You know, and of course, the semantic conventions have been very useful, but still, you know, it's like, that's a whole area of work where an MCP could greatly help, right? Because you could have automated instrumentation that an MCP can provide, and a user, end user can use out of the box. So there are, you know, obviously very
diverging areas in OTEL, where, you know, the knowledge as well as the visibility from an MCP server can help. So I really want to understand better, you know, where
some of these use cases fit in, because, it… that will make or break Odell's MCP implementation in one sense.
So anyway, that was my two cents, but I, I mean, you know, again, very excited about this. So, thank you.
It's dead.
Ted Young 00:23:49 Yeah, I just wanted to reiterate that I'm still a little confused about whether or not we're providing an MCP server, like, is OpenTelemetry providing one?
And if we are, what is the purpose of that one?
Like, is it a reference? Is it, no, literally, you should use it?
Because probably… we're gonna… this strikes me as something that, like, vendors and lots of other people are gonna be building their own versions of, because it's gonna have to mix capabilities across…
Multiple systems and contexts.
So, getting that story straight will probably be very helpful for everyone who doesn't really understand the details about these things, trying to make sense of what the SIG is up to.
ploffay 00:24:40 Our goal is to build something that users can use directly, right? So, there will be an MCP server in Auto, or agentic skills, or a set of skills that people can enable in their agent as, like, the final package that will
enable agent workflows with OpenTelemetry. That said, the…
I'm not sure if you build MCP Server or skill, it's fairly…
Ted Young 00:25:08 small API.
ploffay 00:25:11 That exposes some… knowledge that has already been built, right? So, if a vendor wants to, kind of.
provide the same functionality in their MCP server, they will be able to do that, and kind of copy what we already built in OpenTelemetry.
Well, it's to have, yeah, is to have something official in the ecosystem, like, point users to one place, one kind of documentation where they could configure the agent and use OpenTermetry.
Ted Young 00:25:43 A line you might want to consider drawing is development versus production.
I think that the moment we start saying there's, like, this MCP server is gonna be out there in production, and OTEL end users are expecting it.
to be working in production in some way, that needs to coordinate a lot. If that's gonna happen, that needs to coordinate with…
with things like OB and the injector and the operator and other things. I would recommend maybe…
again, I don't know all of the use cases clearly, but you might wanna…
Stay away from that at the beginning.
And I would certainly recommend…
being very cautious, they're just not building anything that looks like an API or some way of driving things. Like, however this thing is trying to drive stuff, it should just be driving it the same way a human.
Is driving it.
And I only bring that up because when I read at least one of these drafts, it wasn't really clear to me whether or not that was part of the scope, that you… the intent of this group was to, like, add new APIs to the collector or something so that some agentic system could… could drive it in a way it couldn't drive it today.
Liudmila Molkova 00:27:02 I need to go, sorry, but thanks for… for the opportunity to talk about that. Thanks, Pavel, for joining.
Severin Neumann 00:27:09 Thank you, bye-bye.
Juraci Paixão Kröhling 00:27:11 Yeah, I have a question on the last topic that Ted mentioned, like, can you clarify what I mean by the production use case there? I'm not very clear what you mean there.
Ted Young 00:27:25 I just mean, like, if people want this stuff to be working in production versus
in development. Again, I don't really know, like, people spitball all kinds of stuff with AI these days, and I don't totally know…
How… which ideas are the ones that are gonna stick versus not.
Juraci Paixão Kröhling 00:27:47 Yo.
Ted Young 00:27:48 In this case, this feels like… like, I don't know, like,
what are examples of, like, using this MCP server to actually, like, drive things? Because a lot of it seems like setting things up and installing things and doing stuff like that, and configuring things, right?
doing that, like, in development versus something more like what the operator and the injector and OB are trying to do in production, where you've got, like, a control plane that's trying to live manage everything in production. We've got several SIGs who are trying to figure out
how to drive all that stuff through OpAmp right now. So I guess I'm just saying, like, if you start to get into that space, like, I would say, like.
That feels like a hairball, because we're still trying to figure out…
The human programmatic way of doing all of that stuff.
Or the non-AI way of doing all that stuff. So, that just… that's just, like, a lot of balls in the air when you start talking about
Overlapping with the operator and things like that.
Juraci Paixão Kröhling 00:28:59 Okay, yeah, bubble.
ploffay 00:29:02 It's not about overlapping, it's kind of…
It's about enabling human to be… to have more knowledge at hand to configure stuff.
Ted Young 00:29:11 Yeah. But it's…
ploffay 00:29:13 the MCP server will not kind of invent a new way how to deploy a collector in a Kubernetes cluster, right? It will just learn how the collector CR looks like, so it can create the correct schema, like a human would do, right?
Ted Young 00:29:31 Yeah, that's… that's helpful. I just… when I read some of your stuff earlier, it sounded a little bit like maybe this SIG was…
sort of reinventing some facilities we were in the process of inventing in other SIGs.
ploffay 00:29:44 No, no, not at all. No, this is… no. You're like…
Ted Young 00:29:47 You know, that's.
ploffay 00:29:49 As I mentioned at the beginning, we don't want to reinvent wheel, we don't want to create duplicate documentation or duplicate configuration, anything like that. We want to work with individual 6 if something is missing.
If nothing is missing, all great, we will just package what is out there, create the MCP server. It's a very small API layer for AI agents to invoke.
And make it accessible to end users.
Of OpenTelemetry. That is our goal, to have a single place where they can go configure their… their AI agent, and… and start using OpenTelemetry. It's, like…
Juraci Paixão Kröhling 00:30:32 So, but the original reason that I raised my hand was to talk about something else, and that was…
I think going back to the goals of OpenTelemetry, one of the concerns that I have, and that I'm seeing happening is every other company out there is now having their own MCPs, and that includes support for OpenTelemetry.
And I think one of the things that Pavel mentioned resonates a lot, like, we… we should really be providing the building blocks
So if people want to build their custom MCP servers and whatnot, that's okay, as long as our users are not confused, and they have an option to not be locked in by those, specific solutions.
Alright, so if I, if I have a knowledge about the specific open telemetry aspect, then I can encode that as a skill, and then as… and that skill can be used in other… other things.
So this is one thing. The second thing that I really like about OTEL is we have this…
The idea of things being,
pluggable, or I've been able to use individual pieces that we want, so I could perhaps want to use only the knowledge part with my new coding agent that doesn't know anything about, I don't know, cloud commands.
But knows about whatever. So I could, use a new… that knowledge base that we are building as part of new things.
So I think that is the…
the one aspect of OpenTelemetry that we could leverage here as well, like,
Having the building blocks separate from the things that we are shipping.
And then, the other thing is the things that we ship, like the Better Together story. Like, we have all of those small pieces that you can use individually, but we also give you, like, the package that you can consume as a whole.
Just like we have collector components that you can probably build on your own collector, but we also give you the collector binary that you can run in production if you want.
I think the same applies here. And the one thing
just to, you know, viewed on top of what Ted said.
using OpenTelemetry's philosophy, I would not go into the query language side of things. Like, we should not expect the MCP to be able to understand OTLP and query Grafana databases using OTLP data model, like, it doesn't make sense, right? So this is, like, the line that I would draw is.
Whatever OpenTelemetry is set to do is what the MCP could be helping people to do, and not far from, like, not too much…
After that.
Right, so of course, we should definitely have a skill or a specific knowledge base section about semantic conventions, and perhaps for each individual semantic convention, so that when we get data from a backend, we can understand what it is, but not necessarily
like, not going there, like, not… I don't know if it makes sense at all, but, like, what is part of open telemetry should be in scope for MCP, but not what is not as part of our scope. Like, we should not be using
MCP to define SLOs.
Severin Neumann 00:33:51 I just wanted to check in, like, that we may be used to next
5 to 6 minutes to wrap this up and, like, come up with, like… I think, Pavel, your goal was, like, to… what's blocking this proposal, right? So if we can spend the next five to six minutes based on the discussion that we had, like, okay, what's missing? Like, what do we need that everybody can get started?
And, like, GC can approve that thing.
Yeah, I said that we may be at…
Have another 20 minutes for the other topics, then.
Ted Young 00:34:27 Yeah.
So, coming back to that.
if I could reiterate my first suggestion, it seems like there is a SIG, which is, you do want to build an MCP server. So there is a group of people who are like, we literally want to hack on an MCP server, and that's the SIG that you're proposing setting up.
that SIG should have a charter that's basically, like, the project is, like, what's our first stab at, you know, building this MCP server? From, like, what direction are we gonna tackle it?
But then you have this other work that people in this SIG are gonna do, but it's more like, in order for this SIG to make any progress, step one is you're blocked
in, like, lots of places, because… or you're like, this isn't great because the information or how we're getting it isn't great right now. So we want to go into the collector SIG, or this other SIG, and help improve this source of information so that the MCP server can work better.
And I feel like those are the things, if they're big enough things, those are things that should be getting their own projects.
So it's sort of like one project about, like, what's the first version of this MCP server we're gonna build?
What can you guys build without having to go in?
to… to other places? Right, like, maybe you could build it, and you're, like, just proving that this data isn't as good as it could be.
Right? But I would encourage you to find ways to, like, be able to, like, keep making progress, even if you get blocked.
interacting with this SIG or that SIG.
Because…
ploffay 00:36:06 Yeah, and this is exactly what we did for the… that I did for the collector MCP that I already built. There is no official schema, so my tool was able to generate a schema from the goal line configs, right? But the long-term goal should be
improve this in the collector sig itself, right? And there is already proposals for it, there is already people working on it.
Right.
Ted Young 00:36:28 But I think having all those proposals in one big MCP project
proposal is, I think, part of why that proposal is getting blocked.
Basically.
Like, that's what… that's my suggestion for getting unblocked, is to talk about, here's our SIG, here's how we can keep making prog… even if we get blocked interacting with all the other SIGs, we could… that doesn't mean the SIG has to disband, here's how we're gonna keep making progress.
And, like, here's a project for how we want to engage with the collector SIG, so we can talk to them about that. Here's a project for how we want to engage with the SDK SIGs, so we can talk about that.
Just so you have a way of, like, talking to the different groups of maintainers.
And getting their buy-in for… For being able to work on this stuff.
I think that will help you get unblocked.
Because a lot of what we're trying to do is just make sure, like, if you're gonna need to rope in people from another SIG, they've at least consented and been like, yeah, we can work with you on this.
Does that, does that make sense? Is that helpful?
ploffay 00:37:36 It sounds like a lot of…
admin work to get started, to be honest. Because we don't know what we will need in, let's say, the instrumentation, see.
Until we start.
Ted Young 00:37:49 Well, maybe the first version, then, is, like, you just need to build it without…
Without adding any special things, and then.
ploffay 00:37:56 Exactly.
Ted Young 00:37:58 The first version is just to come up with a list of all the stuff that sucks.
Right?
We're like, we're gonna go ahead and try and do it, but, like, point out all the things that you're gonna want to improve.
That… that doesn't sound like a hairball to me. That… that… if I saw a project like that, I'd be like, okay, great. I can see how they can make progress without bothering people, and then…
We're gonna have something to play with.
And they're gonna have recommendations for how we could improve it if we can work with these other SIGs.
If the collector sig's, like, ready to go on it.
great. Then make a second… just make a second project. It's like, here's all the stuff we're gonna do in the Collector SIG.
So hopefully it's not, like, a lot of admin, it's more I'm just saying, like, put them in… separate…
Separate project files.
Maybe the project…
ploffay 00:38:51 Essentially, essentially, like, improving the collector schema in the collector, it's like an implementation detail of the MCP.
Right? And, like, it's our goodwill to make it right in the collector's sake, right? And I don't know what we will need to change in the docs, or the instrumentation, or schematic conventions, until I start building and I will realize that it doesn't work, and…
Yeah, but now, like, creating… all this…
projects beforehand that I actually start building MCP seems like…
Yeah, just additional work that I'm not sure it will have value for me at the moment.
Like, there's people that want to start building it, and…
Blocking them on the fact that we…
We need to create a project for something that we don't know at the moment.
Ted Young 00:39:52 I don't know, man. I mean, if you're saying, like, some of these things are just, like, really small, they're just not big enough to be worthy of project, I'm not worried about that stuff.
I guess some of these things, at least the way you presented them in the past, sounded like…
it was gonna be a situation where, like, if the collector SIG said, we're just working on stability, we're not working on this.
Then, maybe you guys would…
Severin Neumann 00:40:17 Be blocked, or something.
Ted Young 00:40:19 So that's more what I was trying to suggest. If you're trying to, like, actually build something in another SIG that would need a lot of that.
ploffay 00:40:27 No, I think the biggest thing that will require a lot of work is the collector conflict that is already in progress.
Severin Neumann 00:40:37 Yeah, I don't know, like, we might need to wrap this up, but I have the feeling, like, this is not sorted yet, so I don't know if we maybe find…
So, Pavel, you said, like, you will not be on Unplugged, but maybe we can find some time to follow up on this.
maybe we scale… should we, like, continue next week, or schedule a one-off meeting? And… because I said, like, I think the big goal is, like, okay, how can… as Pavel said, like, how can we make people progress and start building something?
Versus, like, running in circles with this proposal. But as I said, we have a few other topics that we should be talking about.
Alolita Sharma 00:41:17 Severin, I propose that we have a separate session, and actually allocate an hour to, you know, work it out.
But because then it really, you know, kind of gives a little bit of time to Pavel also to, you know, I mean, he has a pretty clear scope in mind, I think, with the collector, and starting from there is a win.
Because I think, you know, even if we, as I said, could put it in collector contribib for now, and then move the, you know, project as it grows bigger and has more contributors.
But again, let's trash out the details in a specific session.
Severin Neumann 00:41:57 Okay, then let's… then let's find some time for that, and… Yeah.
maybe in the GC channel, we coordinate who…
wants to and has to be in the meeting, and who says, like, hey, I agree with whatever you come up with, right? Yeah. So maybe not everybody has a,
has a strong opinion, but… but I get Pavel's point that, like, this is going now for a few months, and… and we should… we should get… get something out there.
Alolita Sharma 00:42:24 Yeah, yeah, definitely, because, I mean, again, the area is moving so fast that if you don't provide it, then, you know, it really causes a lot of…
ploffay 00:42:32 To that point, I think there won't be a lot of work required in those individual six. I think just the collector was the problematic one, because how it was done in the past, but, like, repackaging semantic conventions is pretty easy. Doing something with instrumentation is probably as well.
Straightforward. And that's actually the entire scope of the proposal, if you look at it.
Your concern is the collector, and already there are people working on the config. There is a proposal, and it's moving forward.
Severin Neumann 00:43:07 Okay. Okay, then let's figure out some additional time for that, so that we can jump into the other topics. So, Pavel, thank you for…
For joining us today.
Yeah, thank you. Let's make sure that we quickly follow up on that, because I think right now this is not 100% satisfying for you. Yeah, I will follow up in the GC channel on that, so we can…
Talk about that. Thank you.
ploffay 00:43:34 Thank you very much, Anna. Have a nice day. Thanks, Paul. Bye.
Alolita Sharma 00:43:43 Cool. I think this was a very good discussion, though. It's a good start.
Severin Neumann 00:43:48 Yeah.
Pablo, do you want to…
Pablo Baeyens 00:43:52 next.
Severin Neumann 00:43:53 jump into C-Advisor.
Pablo Baeyens 00:43:56 Yep.
Yep, so,
the… I put the link on the Zoom chat, and it's also on the Slack channel, and on the agenda.
Basically, Google wants to…
in some ways, sunset C Advisor and move it to, other places.
The idea is that a part of it would be transitioned to the collector in some sort of…
receiver way?
And… yeah, I have two asks. The first one is whether this is something that should go through this body, or whether you think the collector should handle it… the collector's seek should handle it on its own?
And the second one is, if you think,
it should go through this body, should we meet with circa.
Alolita Sharma 00:45:02 I think, Pablo, we should definitely look at the proposal, because, C-Advisor is such a core part of the KATS infra metrics, and, you know, infra data that,
It would be useful to understand what, you know, that,
Layer is going through, unless they already have a well-written technical proposal that we can look at.
Severin Neumann 00:45:34 Yeah, but I don't think, like, this is really something that TC should be involved in. Yeah, the TC can look at it. I mean, I recommend that everybody of us looks at it, but…
My feeling is, like, the collector SIG should be more than capable of handling this. Yes, indeed. And if there's anything going outside of the collector, and then, like, touching into a lot of other topics, then maybe, yeah, let's revisit it, but, like, I don't know what we should…
do beyond, like, having an eye on it, and maybe review the proposal. That's my few cents on that.
Alolita Sharma 00:46:08 I think we should get the, you know, the recommendation from the collector SIG maintainers, right? So, they should definitely be looking at it in detail.
Pablo Baeyens 00:46:20 Okay, we can start with the collector and see how the conversation goes. Note as well there's a similar question on the GCTC tunnel about a different donation.
I… Don't think we need to discuss it right now, don't we?
Do subscribe, or take a look, because… I think…
the TC is going to have opinions, about this, and we probably need to… Talk, buddy.
Trask Stalnaker 00:46:50 My understanding of… The donation process is… historically, at least, has been… we've only… we haven't…
Used it if a donation is going straight into an existing repository.
Yeah, that's my understanding.
Ted Young 00:47:11 Yeah.
Trask Stalnaker 00:47:11 With following that.
Pablo Baeyens 00:47:18 Alright, let's… Move on to the next topic, then.
Jurassic.
Juraci Paixão Kröhling 00:47:27 Mine is quite simple, it's just a…
a request for people to look into this specific issue, so this was requested by Fabricio to me. We have a new design for the website, and one thing that I mentioned to him while reviewing the new design was, we also deserve new hero sections, like new taglines, new text.
And, and he…
very correctly decided to do that, one step at a time. Like, so, first the new design, and then new copies.
And this is the issue for the new copies. So if you have opinions, if you have ideas.
On how things should be…
done, or how… what is… what it should look like in the future. Leave a message there, comment.
And, and yeah, that's pretty much it.
Alolita Sharma 00:48:29 You're asking, where do we see the new design? Is that the link here?
Juraci Paixão Kröhling 00:48:33 OpenTelemetry.io, it's default already.
Alolita Sharma 00:48:36 Oh, okay, okay, okay. Fine, fine.
I see. I was just thinking it's a sandbox kind of a…
Juraci Paixão Kröhling 00:48:44 No, no, what is under discussion is, the new copies. So, what should we be having as the hero copy? I think, like.
it's… it's too long, perhaps, right now. Like, it is correct. It's quite long, yeah.
Alolita Sharma 00:49:00 But it's good.
Juraci Paixão Kröhling 00:49:02 Yeah, but it can be a little bit shorter, it can be a little bit more…
I don't know, it can be simpler.
punchier, perhaps, I don't know.
So that's the call-up, like, so give your suggestions, see what it should be doing.
Severin Neumann 00:49:17 But not only the hero, right, but, like, everything…
Juraci Paixão Kröhling 00:49:20 I'm not only the hero.
Severin Neumann 00:49:21 Not only, like, quality, ubiquitous, whatever, but also, like, OpenTelemetry is vendor neutral, unified, run anywhere.
Juraci Paixão Kröhling 00:49:31 Exactly.
Severin Neumann 00:49:32 features.
Juraci Paixão Kröhling 00:49:34 Yeah, I think the hero is the part that I have the biggest opinion, perhaps, like, I think it is, like, high-quality ubiquitous, like, those… I mean, we can probably…
get away from those words, and portable telemetry, I like it. But anyway, this is not for us to have a discussion here, it's just really.
Alolita Sharma 00:49:54 Yeah.
Juraci Paixão Kröhling 00:49:54 Share your opinions on the issue, and, engage on the discussion there.
Alolita Sharma 00:50:01 Absolutely.
Very cool.
Severin Neumann 00:50:08 Okay, looks like we went through the rest of the agenda really quick. Yeah.
Let me quickly give you, like, maybe you saw it in the maintainer's channel already, but I can give you a quick update on the…
on the… on the Bloomberg, mentorship program. So just as a reminder, Bloomberg approached CNCF and said, like, hey, we ran this with the Pandas project successfully a few times, and what we want to do, we want to encourage,
Internal employees to contribute to…
a CNCF project that you find a good fit, and they said, like, hey, OpenTelemetry is actually a good idea,
So, I, I was, speaking back and forth with them, the one thing is, like.
Overall, the legal agreement is…
almost done, so I was told, like, yeah, we can also now start talking publicly about it, that, like, Bloomberg wants to do this. What they want to do is, like, sometimes April, June, do a 10-weeks program where they're, like.
have a bunch of their engineers show up and contribute to our project, right? And what I'm recruiting right now is a few ZIGs, a few maintainers that say, like, hey.
we can…
create some buckets of work that those engineers can work on. And a very specific goal of them is that, like, this is going to be sustainable, so they don't want to…
Like, of course they don't expect, like, all of those 30, 45 people to contribute forever, but they hope, like, to get out, like.
5 or 10 people that will continue contributing to OpenTelemetry beyond that, right? And it looks like with the… with the Pandas project, they were very successful with that, and then now they offer that to OpenTelemetry as well. I'm very excited about that, because, like, hopefully…
We get a few experienced engineers that just start contributing, and…
Hopefully, also, they're more on the end user side, right? So what I hear them talking about with the Pandas project is, like, they, of course, contribute the stuff that they need, because they're heavy users of that, and they also want to be heavy users of OpenTelemetry at some point.
So yeah, that's more or less a status update. If you have any questions, if you have any…
things you want to be involved in, then let me know. Yeah.
Alolita Sharma 00:52:32 Okay, cool, cool.
Let's… so, Severin, what's… I mean, creating this bucket of work, from the different projects is probably just asking the maintainers to…
Severin Neumann 00:52:44 Yeah, exactly. So our idea was, like, they have internal maintainers, so they have.
Alolita Sharma 00:52:48 Yes.
Severin Neumann 00:52:49 experienced open source contributors that say, like, hey, we help you with, like, the baby steps, but of course what they need from us is, like, maintainers that say, like, oh.
I'm a pipe maintainer, and we care about stability, and here's, like.
the good first issues, the help wanted you can work on, or maybe I spend some time with you on an office hour. So they said, like, if we can find a few people that can spend 2 hours per week
during that period, that would be really good, and as you can imagine, they have a big footprint in C++, they said Go, they said Python. I would love to have the C++ stick on board, but as you all know, like, they're…
very, very thin staffed and… and, trying to figure out how to do it. So… so I will see how to… how to enable that, because I think having…
having more people on C++ would be, like, extremely valuable. So if you have any ideas also in that direction, like, how we can… how we can make that happen, that… that would also be something I appreciate.
Alolita Sharma 00:53:50 Did they specify these specific languages that they.
Severin Neumann 00:53:53 No, it was more like, hey, we as company, that's the languages our people code in, right? I see.
Alolita Sharma 00:53:59 I see.
Severin Neumann 00:53:59 They just are a big C++ house.
just if you think about what Bloomberg is doing, and how long this company is around, and they also do a lot of Python, and the other language they do a lot is Go, so that's how it came up as Scope.
Alolita Sharma 00:54:15 Okay.
Juraci Paixão Kröhling 00:54:16 So, perhaps one request that I would have, Severalin, is… so I committed to helping there, but one difficulty I'm having right now is, and it might be my impression, but the communication seems to be mostly during the calls on Fridays.
not so much asynchronously, and I'd appreciate if it is more asynchronous than, you know, meetings, because I.
Severin Neumann 00:54:38 Yeah. On Fridays, it's very hard for me to join. Yeah, no, no, I think we had one call so far, and I used, like, I was in New York earlier this year, and that's why I said, like, hey, let's meet in person just to build this relationship, but yeah, I also think that we should figure out how to do the communication. Also more of it public, right? I mean, a lot of it was, like.
Happening on the side, because, like, there were still some debates on the background, but
more and more is happening, and I want to also push this out, like, people need to learn to work and speak in public, so yeah, that's part of.
Alolita Sharma 00:55:11 Maybe, maybe a Slack channel that.
Severin Neumann 00:55:13 Yeah, yeah.
Alolita Sharma 00:55:14 You know, it's for this specific program, but it's.
Severin Neumann 00:55:16 Yeah. Public. Yeah.
Alolita Sharma 00:55:20 Awesome. That's, that's cool.
Ted Young 00:55:25 there's no time left in this meeting, but something related to what you're saying, Severin, is just… you're saying we want to get more contributors, and this is a great way to do it, but I've been thinking a lot about how we change or improve
You know, the way we promote people to triager, approver, maintainer.
I'm having this interesting experience of, like, moving from LightStep to Grafana, where LightStep
came… LightStep came up through OpenTelemetry, right?
Alolita Sharma 00:55:58 Yes, yes.
Ted Young 00:55:59 We… LightStep…
was not a situation where we had a bunch of open source devs sitting around, and they all want to, like, get involved in telemetry, and then find out, how do I get involved in this existing, big, giant thing, right? So I didn't have that experience last time, but I'm having a lot more of that now that I've switched companies.
And trying to navigate…
how that should work, and I don't think open telemetry is, like, particularly bad, but I am feeling that, like, open telemetry is not particularly bad for open source, but open source is particularly bad.
Around being a little exclusive and reluctant, and thinking about, you know, giving people a hat
As being related to seniority, or how long you've been around?
Severin Neumann 00:56:54 Yeah, yeah. I mean, this is maybe a great topic to talk about in Unplug, I mean, like, collect some feedback from outsiders, and say, like, hey.
As a non-contributor, how do you.
Ted Young 00:57:07 Yeah.
Severin Neumann 00:57:07 getting in, right? But I'm with you on that side. I mean, technically, we have a contributor experience sick. Pablo and I tried to establish that, but, like, yeah, and Marilio, of course, you helped us a lot here. But it stalled very much, right? And we have Amy from Profana.
Marylia Gutierrez 00:57:24 So actually, like, me… yeah, me, Amy, and Kayla, we still meet regularly.
Severin Neumann 00:57:29 Yeah.
Marylia Gutierrez 00:57:29 We do have plans, we did, like, interviews, we are getting, like, feedback on things that we want to change, and my plan is also on Onto Unplug, one of the topics be about the contributor experience as well.
Severin Neumann 00:57:40 Yeah, yeah, yeah, and I think that's definitely something we should tackle more and talk about, but yeah, maybe Unplugged is a great place also for us to chat about that.
Ted Young 00:57:52 Yep. How do we communicate priorities to SIGs, and then how do we encourage SIGs to promote people?
And…
Just feeling like we need to maybe take a more rattle rethinking about what it means to have earned trust.
And can we come up with, like, a way of thinking about that that's a little bit different from, like, longevity or seniority or something like that?
Alolita Sharma 00:58:18 So, Ted, if I may…
Ted Young 00:58:20 Seeing that we were…
Alolita Sharma 00:58:23 No, no, I just wanted to understand the context of what you're saying, because,
Are you saying that, you know, when… like, when you made the comparison between, you know, the DNA in LightStep versus, you know, a larger ecosystem like Grafana or other companies, are… do you see folks,
finding it harder to contribute to… and getting involved in a project like Hotel, or is it just that they don't see a path in terms of getting promoted? I mean, because they're two separate issues, right?
Ted Young 00:59:00 Three things. I see three things. And they're all totally normal open source things that I don't think we do especially bad. One is trying to get started with a gigantic
open source project that's been around for a long time and has a lot of velocity, it's just hard, right? Yes. Doesn't matter what the open source project is. When you try to get involved for the first time as a contributor, it's totally confusing until you just kind of do it for a while and you figure it out. That's, like, all open source.
OpenTelemetry fits that way, but can we do better?
Alolita Sharma 00:59:37 But it's… large projects always have that issue. Yes, you're right.
Ted Young 00:59:40 Right, but, but, like, docs, everything else, our answer is, like, can we move the… can we raise the bar? Can we, like, let's not just be like, well, we're normal, like, let's do better. The second thing is, like, people get involved, and then they're like, cool, so I've been making all these contrib… contributions and stuff.
like, when… when do I become an approver, or when do I become a maintainer? And people start to form their own opinions about whether or not they've, quote, done enough.
I'd be out of step with what the maintainers…
feel. And then they'd come to me, and they're like.
when is this gonna happen, or why? And I'm like…
You know? And… but, like, there maybe can be a way to be a little more objective. One of the feedback is, like, yeah, you're doing work, but are you just doing work for you, or for the company you work for, or are you doing work in a way that feels like you're kind of holding things down for other people?
Right? That's a subtle distinction that's come out when I've been looking into stuff, right? In terms of, like, perceptions of maintainers, of whether this person's done enough, right? That's something that comes out.
Yeah, this person's done a lot, but it's always self-directed, and they just want to work on their thing.
So I'm not really thinking about them as a maintainer.
Alolita Sharma 01:01:04 Right?
Ted Young 01:01:05 Versus this other person hasn't been around as long, but they… I feel like they're just doing… they're working on everybody's stuff. They're seeing what everyone else is trying to do, and they're, like, pushing on that. And so I'm… as a maintainer, I'm, like, liking that person a lot more.
But…
we're a big federated thing, so everyone's opinions are different. And then the third thing is, like, how do we communicate priorities, right? We've decided config and stability are, like, super important, and then we've got, like.
Marillia here, just as, like, an example, like, she's, like, a JS approver, she's on the GC, she's been involved for a long time. We know that config is important. JS is, like, in a place where they could do it. She's got, like, config PRs, and they're, like, stalled.
Because that SIG is sort of like…
Our opinion of where config is in our backlog is…
actually, like, pretty different from where the GT thinks maybe it should be.
You know, and why is that? Well, we don't, like, coordinate heavily with the JS SIG, so… it's not surprising.
So that's, like, the third part, where it's, like.
If we could improve that part, then maybe it's more obvious
how to make contributions in a way that aren't just, I'm working for my vendor, but I'm also, like, working for this SIG. Because…
the SIGs communicated its priorities, so now I can show that I'm working on those priorities, or something like that.
I don't really have answers to any of these things, I'm just, like, I'm noticing it a lot more now that I've switched jobs, because I'm just interacting with a lot more devs, where…
you know, I'm like, oh, I bet this is, like, wider spread, it's just the devs who don't work at Grafana aren't gonna be coming to me, like, asking, what do I do, right? It just so happens it's the Grafana people talking to me today.
Alolita Sharma 01:03:04 No, I think, Ted, they're all good points, because I think, as you know, we have discussed some of these areas earlier before also, because promotion of, you know, and recognition of contribution has always been a kind of a…
subjective process in OTEL, and as you said, it's dependent on each SIG, dependent on the maintainers, what they see as valuable versus not. But having a clearly documented guideline, at least, would be useful.
Ted Young 01:03:40 Yeah.
Alolita Sharma 01:03:41 maybe that's what we could help, the maintainers with. The other part is that, again, we've also discussed the GC meeting with the maintainers, you know, maybe on the specsig or wherever, you know, once…
every quarter, or whatever, may… might be useful, so that priorities are at least, you know, communicated, so… but this is a longer discussion.
Ted Young 01:04:06 Yeah, it's a longer discussion. One thing I can offer, my boss, Merle Krantz, who, Jurassi, you know Merle.
Alolita Sharma 01:04:15 Oh, yeah, yeah, I'm Martin Salsa.
Ted Young 01:04:16 Yeah, she's… she's been involved with the Apache Foundation.
Alolita Sharma 01:04:22 Yep, 20 years.
Ted Young 01:04:23 Really long time. And we've talked a lot about this, and she's expressed, like, this is a common thing there.
So I can pick this up in Slack or somewhere else, but one thing I proposed to her, she'd be willing to come talk to the GC at some point about the Apache Foundation's history.
Around noticing this stuff.
and doing work to break it up when they see, because they found this to be a very common pattern in Apache projects, where maintainers start to become a little exclusive.
And you have this situation where the maintainers feel like there's enough maintainers, but the people trying to, like, get stuff pushed.
Alolita Sharma 01:05:05 Yes.
Ted Young 01:05:06 enough containers.
Alolita Sharma 01:05:07 Yes, yes. Apache PMCs are notorious. So, totally. Good, good suggestion.
Ted Young 01:05:14 Anyways, we don't have to solve it all.
Alolita Sharma 01:05:16 Yes.
Ted Young 01:05:18 But, yeah.
Alolita Sharma 01:05:20 Yeah, let's talk on the channel. Thank you, Ted.
Thanks, everyone. Take care. Bye.
