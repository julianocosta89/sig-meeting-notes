SIG: Developer Experience SIG Meeting
Date: 2026-01-28
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Damien Mathieu** 01:27 Hey.
**Diana Todea** 01:30 Hello, good morning!
**tristan** 01:31 Hey, hey!
**Damien Mathieu** 01:33 For the record, I had to opt out the read.ai parts again.
**tristan** 01:39 Okay.
I saw that they were gonna complain about that, or something?
To get it.
**PL Pavol Loffay** 01:49 to be.
**tristan** 01:50 Opt in?
Good.
So, something to me.
**Damien Mathieu** 01:57 And we don't even know how it's added, so… yeah.
**tristan** 02:00 Oh, really? Okay.
Cool.
Okay.
Mmm… Pull up the agenda… Oh, rit.
I know, let's see, who's here?
Awesome.
1, 2…
Pink.
Probably everyone who's coming is here, because the… Is it Boston this week?
So I think… Juliano's not here?
We can get started.
Alright, that is great to see. We've got the Skyscanner blog post ready for review.
**Johanna Öjeling** 02:56 Don't need…
**tristan** 02:58 You know, it's approval, but… Everybody can… What's that?
**Johanna Öjeling** 03:03 Yeah, exactly. We, we don't have his email address, but he's on the CNCF Slack, so, Juliano pinged him, but yeah.
**tristan** 03:13 Boom.
**Johanna Öjeling** 03:14 He hasn't replied yet, but hopefully.
**tristan** 03:18 I thought I had his email somewhere, but… I'm sure he'll get back.
**Johanna Öjeling** 03:22 Oh, okay. Yep. Yeah, if you find the email, then yeah, you can just go into document.
**tristan** 03:30 One sec… So everybody can take a look at that and review it.
Yeah, I've got his email. Here.
Just in case you…
**Johanna Öjeling** 03:41 Nice.
**tristan** 03:42 keeps nuts.
Let me put it in the chat here…
Or I can always email them, too.
**Johanna Öjeling** 03:53 Oh, thank you.
**tristan** 04:08 No, we have.
Project issue status, language surveys… What are these?
**Johanna Öjeling** 04:16 Yeah, I had a look at the, project, or the DevEx repository, and the issues, and, there were some…
Openicious about… like, PHP Developer Experience Survey, vastgo.net Developer Experience Survey, so I wanted to check, is this… Something…
We intend to do, or should we close those issues?
Do some cleanup, or…
**tristan** 04:49 Yeah, this… that's a good point. The, we had been… basically surveying, each SIG.
To try to… Find out what…
They do different from the spec to improve the developer experience.
And… I know we… Some of them got back to us, a number of them.
Didn't, and we, ended up doing the user survey, and I think that's why this fell.
by the wayside.
I'm… yeah, I'm trying to think whether we should…
Close them, but consider, respawning that? Or keep them open, and consider respawning that.
Cause I think it's… Would be useful, because there is stuff out there, in the different SIGs of…
What they… well, it was both… it's both what they do and what their users are asking for that we were interested in, because we wanted to know…
Like, probably, like, in…
the Java SIG, there might be a lot of users asking for micrometer features for metrics, because micrometer has a lot of
ease of use features for using metrics that our metrics don't have, things like that, that we never…
never accumulated.
**Johanna Öjeling** 06:27 Mmm. Okay.
**tristan** 06:28 Yeah, we can keep them open and…
**Johanna Öjeling** 06:31 Revisit the topic.
**tristan** 06:33 Yeah, we need to revisit the topic when we're…
**Johanna Öjeling** 06:36 -
**tristan** 06:36 More prepared for it, make sure to add that for maybe the next… Meeting. We can discuss it.
does anybody else here have any thoughts on the idea?
The idea of… this… surveying…
the different SIGs to find these things out about what they do different to improve developer experience versus the spec and things that their users are asking for that we might be able to work on.
Or should we just discuss it next week?
Okay.
We'll discuss next week.
**Johanna Öjeling** 07:17 Thanks for providing the context.
**tristan** 07:23 Next up, we have… Questions regarding… Submissions of a blog post.
MCP proposal blog post?
**Diana Todea** 07:34 Yeah, hello. So, first of all, I'd like to say hi, because I never attended any of these meetings, yeah, I'm new to DevEx SIG.
I'm Dan, I'm a developer experience engineer at Victoria Metrics. I'm a member contributor of OpenTelemetry Localization 6.
or COMSIGs, whatever, for over a year, and, yeah, obviously I've been tracking the DevEx SIG as well. So I have, first of all, some questions, probably they're very fundamental, beginner style.
Like, in order to qualify to submit a blog post, for OpenTelemetry, what do we need? So, what, what will be, like, from an end-user perspective, or if you could give me some, some…
Overview about that, that would be great.
**tristan** 08:34 Oh, so… This is two different questions?
Okay, so it's not about MCP's proposal blog post?
**Diana Todea** 08:42 There are two different questions.
**tristan** 08:44 Okay.
**Diana Todea** 08:44 First, and then comma, second.
**tristan** 08:47 Okay. The…
**Diana Todea** 08:49 Sorry.
**tristan** 08:49 commas, I'm sorry. Bet. The… there's… No…
Yeah, anybody can submit a blog post to…
**Diana Todea** 09:00 Okay.
**tristan** 09:01 to do it, yeah, as part of the developer SIG? I mean, as, like, a developer SIG?
blog post, I guess it would just have to be discussed here, and reviewed through people.
**Diana Todea** 09:12 I mean, there's no official…
**tristan** 09:15 like, number of sign-offs that have to come from here or anything, but I think that's what we would…
Expect, what's the blog post you were working on, or thinking about working on?
**Diana Todea** 09:28 Right, so, well, basically, Victoria Metrics is, how can I say, we are also using OpenTelemetry, we are… have adopted it, and we are also an observable… observability vendor, so basically we are, like, at both ends. So my guess will be, like, also to… to…
Give to the community a feedback on how we implemented it, how we are using it, etc, etc, because we kind of, like, during the first time when we adopted it, through how we are consuming it right now, it has been a journey.
So that's why I was thinking about it.
**tristan** 10:04 So, actually, the, like, internally, how you're using OpenTelemetry?
**Diana Todea** 10:09 Yeah, exactly. I mean, it can be more than that, but that's why I wanted to check with you to understand the angle.
**tristan** 10:16 Well, that's actually perfect, because, that's exactly the blog post we've been working on.
For a number of companies, so adding Victoria Metrics in there is… Perfect to…
**Diana Todea** 10:29 Excellent.
**tristan** 10:30 Have another one. So yeah, we,
we've got a number of these in the works. We've interviewed, companies, Mastodon, Skyscanner, Atlassian, Adobe, Donks,
And we're… Making, new blog posts about, you know, Why they adopted the…
Their organization, how they're running the collector, how they're running… how their instrumentation is set up, things like that, and, like.
tips for other people. It's sort of to… because we ran a developer experience survey, and one of the things that we got back was that there's not real-world
Examples in the documentation?
Yep.
**Diana Todea** 11:13 Yep.
**tristan** 11:14 Having to learn these things as they go.
**Diana Todea** 11:16 Exactly.
**tristan** 11:17 And so, yeah, if you wanted… To write that from your…
**Diana Todea** 11:22 Yeah.
**tristan** 11:23 But there's no… If there's not even an interview required, that would be awesome.
**Diana Todea** 11:28 Perfect, yeah, no, exactly. So, just, just a follow-up question on this, so I'm guessing, like, everything that you, gets published is, is it published, like, on the OpenSelementary blog, right?
**tristan** 11:40 Yes.
**Diana Todea** 11:41 Okay, I'm just gonna go through that to see, like, you know, understand how it's written so I can, you know.
**tristan** 11:47 Yep, properly?
And are you… do you see the… the… Let me… grab the… we have…
a document here, I'll put it in the chat here.
That is a collection of our blog posts.
That we're in the works… work on.
**Diana Todea** 12:08 Okay…
**tristan** 12:10 If you can open that.
**Diana Todea** 12:12 Yeah, so what happened? Okay, everyone.
Let me open this… exactly, XSO, la la la…
Once we sign this afternoon else…
So, should I do viewer or editor? Because I don't want to… viewers.
**tristan** 12:29 Editor, because it would be great.
**Diana Todea** 12:31 Beautiful.
**tristan** 12:31 Add yours as another tab.
**Diana Todea** 12:34 Yep, exactly. So I requested the Rhino, my personal email.
**tristan** 12:38 Okay, I'll… Ping the owner to make sure he knows, so good.
**Diana Todea** 12:44 Yeah, so I will look through what has been published previously, and obviously, I mean, it will be nice because we have, different angles, you know, like, we are consumers, and definitely we evolved a bit, so I'll liaise with engineering to get more, like, also technical overview, etc.
But yeah, that would be great. And yeah, let's see in the future if we can help with anything else.
**tristan** 13:11 Yeah.
**Diana Todea** 13:11 Yeah, so that's why I wanted to join, because I'm really happy that we have an EMEA-friendly, like, in-the-morning, meeting.
So yeah, I'll get started with that and ping you whenever I have a draft. And about the MCP proposal, obviously I saw some information about that, and Damien, yeah, kindly pointed me to join the meeting to get more information.
So, yeah, the same. So, if I can help with anything around this proposal, or… I don't know, anything that you want to share, that would be nice. I can…
Contribute with something, that would be… that would be nice.
**tristan** 13:59 Let me…
**PL Pavol Loffay** 14:00 maybe I can chime in for this one. So we are on this… in the state of, kind of,
in the proposal state, so it hasn't been approved. There are still some concerns on the GC and TC about the proposal.
That is essentially too wide, and they are concerned with… The, kind of.
with a scope, and how it's gonna be done, the collaboration with other six, especially if they decide to build their own, kind of, MCP server, or do something on their own to support agent flow.
so this should be maybe better highlighted in the proposal, how, like, what is the overlap? Like, how it's gonna be solved, this overlap, if there will be an overlap. I will today join the GC meeting for the first 15 minutes to talk about the proposal, and…
Hopefully it will… they will get some clarity on what we are trying to achieve.
Yeah, that's essentially the state.
**Diana Todea** 15:11 Perfect. Thank you, Pavel. I just have a follow-up question. So, why is this within the DevEx, SIG?
**PL Pavol Loffay** 15:20 That's a great question, and that's the question they have as well.
So… the… like, I think our goal is to…
enable or make sure the OpenTelemetry ecosystem works well with agentic workflow, and…
we have identified a couple of gaps that usually users face. The first one is the, for instance, the collector configuration. When you are configuring the collector with LLM, it often hallucinates and produces the config that is not valid.
Because there is no, like, official schema, for instance, for the collector configuration.
Other use case that we talked about is…
the agents should understand semantic conventions and give you the correct hints about what attribute names you should use, and what values for those attributes should be when you are instrumenting an application. That's another example.
Then we talked about the instrumentation. Like, sometimes when you are using the agent to instrument your code, and you want to perform some more specific instrumentation task. So, for instance, like, enable
I don't know, Prometheus Exporter, or something like that, that is not very well documented.
Then… it's the… The college agent might fail to do that.
Because, again, there is, like, missing,
Documentation and, like, missing some… something that could be used to, kind of, for training that model.
Or the instrumentation changes, because the LLMs, they are trained on, like, on old data, and OpenTelemetry moves fast, or faster, and then the agent doesn't have the latest information. So, as you see, this is kind of cross-sig. It's many different pieces that are cross-sig.
And…
That's why… that's the reason why we think the DevEx is maybe the best place for it, because we…
Would like to handle these different pieces across the ecosystem.
But again, like, our goal is to create, like, very small interface for the AI agents to interact properly with these pieces that we already have in the ecosystem, so…
What does it mean for, let's say, for improving the instrumentation? We don't want to write, like, new content that will live in the agentic workflow repository. We want to improve the…
the docs for the instrumentation, and then provide very small shim for the agentic workflow to enable the agent to use that upstream documentation that lives within that upstream community.
So, maybe…
If the proposal is… will not be accepted in the current form, as it is right now, to kind of work across six, then…
we will…
change it, or it makes changes to… it makes sense to change it to be, like, a 6-specific, and kind of, change the scope to…
let's solve first the collector configuration as an agent tick workflow, work within the collector SIG, and then maybe
join another SIG community, let's say the instrumentation, and work with them to enable the…
the agency group flow there. But our goal is, again, it's… we want to look at this holistically and make sure that the…
The user experience.
Will be consistent for all these different
6 that we have in OpenTelemetry, which means that the installation of the MCP and maybe the skill will be consistent, there will be single kind of documentation where users can find it.
maybe we can as well think about, like, hosting an MCP server within OpenTelemetry, so you just point your agents to, you know, to some endpoint where it will get the, kind of, the latest documentation or configuration validation.
And as well, like, the most important is, like.
defining, kind of, the toolset and the content that will be served for the agent, right? Because there is a lot of overlap, and we want to make sure that
If your user enables everything, the agent will not be confused, and will get clarity on, kind of, what tools it should use to execute specific tasks.
**Diana Todea** 20:15 Yeah, no, thank you. That's very… that's a good explanation. I mean, I'm guessing at this point, because, you know, it kind of maps over, like you said, across the SIGs.
And so right now, you're looking maybe to get a clarification, on the, you know, if it goes ahead, if not, if it narrows the scope.
But I'm guessing, like, down the road, you'll also need some, like, you know, technical expertise, maybe some help from the community, you know, like, there are so many vendors, observability vendors, and not only that, you know, everybody has their own MCP server, so I'm guessing here that's also, like, something you want to
get from the community, you know, like, some best practices, what worked, what didn't, if they, you know, especially if they have some experience with OpenTelemetry.
So, yeah, I mean, I'll be… I mean, I saw the main GitHub issue for the proposal, so I think at this point, you're just waiting for, you know, the actual OpenTelemetry to define
The scope and…
you know, read some certain agreement, and then you'll move forward to maybe get some more help from the community, like, technical… on the technical side, but also on the documentation, etc.
**PL Pavol Loffay** 21:38 Yeah, yeah, exactly. We would like to get the proposal approved by the governance committee, get it merged, and then create a repository that Tristan started, so we can start building something. And any help is very valuable, and it would like to be
If you would like to be officially listed on the proposal, let me know. I can put you there. We already list a couple of people. I think that could as well help to get the proposal approved, because it shows the interest in the community. And one point, why the proposal is in the SIG,
is because… it's sort of improving developer experience, right? Like, right now.
users and developers using OpenTelemetry, they…
They go to documentation, they… or they build their own knowledge, how to configure stuff, how to instrument.
An AI agent is just a different…
It's just an additional API or additional help, what they can use to perform their tasks.
**Diana Todea** 22:44 Correct. I mean, to be honest, I would like to help, especially because, I mean, I have the expertise of Victorometrics Engineering, they also created their
on MCP server, etc. So, since we are already consumers of OpenTelemetry, definitely, from a technical perspective, we'll be able to help.
So, yeah, I can… you know, you can list me there if you want to, that's totally fine, and I'll bring it with, my team as well.
**PL Pavol Loffay** 23:16 Awesome. Maybe if you can, on the pull request for the proposal, you can comment on that section with the…
With the people that want to help and kind of put your name there, it would be probably better to do it this way.
**Diana Todea** 23:33 Sure, let me just open up again the issue…
So we are referring to, I guess, this one.
Yeah, exactly. It says here, count me down, like, I see a couple of people… On its own…
No.
So, yeah, I'll add a comment there, and I will bring it back with the engineering,
And see what they think. I'm not sure, like you said, at this point, you're looking for some, like, even clarifications, maybe questions? I think that would also be beneficial, right? No?
**PL Pavol Loffay** 24:21 But right now, we need to get the… like, your input is valuable, and .
As well, if you have some input on what I just said about the Skobot project, that's important.
**Diana Todea** 24:33 Okay.
**PL Pavol Loffay** 24:34 So you can go through the proposal, you can read it, and if there is something that you think should be clarified, or something should be added into the goals, or into the deliverables, then please make that comment, and we will, we'll talk about it.
**Diana Todea** 24:51 Perfect, will do, thank you so much.
**tristan** 24:57 Cool. Yeah, so basically it's gonna come down to the GC making a decision, hopefully soon.
Based on the meeting today.
**PL Pavol Loffay** 25:09 Yeah, yeah, but as I mentioned, like, if it doesn't go through in the current form, we will squash it and make it a bit more narrow to focus at the collector from the beginning.
**tristan** 25:22 And then kind of expands to other areas.
Dart.
Sounds good.
Alright, that was… last item on the agenda,
I guess one of the, and…
you still have a… you already wrote the blog post for the MCP server thing to post eventually once we get this accepted, right?
**PL Pavol Loffay** 25:52 I did, yeah.
**tristan** 25:53 Yeah, okay, yeah, so that's all done and ready to go. Cool.
**PL Pavol Loffay** 25:58 Yeah, the goal… well, the idea is to merge the proposal, and then have a blog post that will…
encourage the people to join the effort, and then once we build something officially in hotel, we'll have, like, a first introduction to MCP that comes, you know, from the hotel ecosystem.
**tristan** 26:20 For the end users to start using.
**PL Pavol Loffay** 26:22 So, so, if this goes through, my blog post will not be published.
So my blog post is about the MCP server that I built, right?
**tristan** 26:36 Oh, oh no, so I thought…
**PL Pavol Loffay** 26:38 And…
**tristan** 26:40 We're gonna write…
**PL Pavol Loffay** 26:41 My proposal… my blog post is about the MCP I build. If we get accepted the proposal for the MCP SIC, or MCP project.
then we will have another blog post promoting the official MCP from Rotel.
**tristan** 26:59 Okay, that one hasn't been written. Okay.
Gotcha, gotcha, gotcha. I thought you had already written that one in preparation for…
**PL Pavol Loffay** 27:05 No, no, no.
**tristan** 27:06 Okay.
**Johanna Öjeling** 27:09 But I remember seeing a draft of, like, a call for a contributors blog post.
**PL Pavol Loffay** 27:16 Yeah, this is the call for contributors for the official.
**Johanna Öjeling** 27:19 recipe.
**PL Pavol Loffay** 27:20 If the proposal gets accepted. Yes, okay.
**tristan** 27:25 Okay, cool.
Alright.
Is there anything else on MCP Server, or anything else in the developer experience we should discuss right now?
**PL Pavol Loffay** 27:39 No, for the MCP server, with,
Nico, we are having the, like, webinar today from Olive Garden, if you would like to join and so…
And listen, it's… I think it's open for anyone. I don't have the link, maybe I can find it from the link.
**Diana Todea** 27:57 Yeah.
I wanted to ask you for that. Thanks.
**tristan** 28:00 Yeah, I'll join them.
If you can't find it, you can just put it in the Slack later.
**PL Pavol Loffay** 28:10 Yep.
**tristan** 28:11 Okay.
**PL Pavol Loffay** 28:12 Yeah, we can do that.
**tristan** 28:13 That'll be neat, okay, then, we can…
call it here, if everybody can look at the Skyscanner blog post, and… Keep…
Your eyes on the MCP proposal. The webinar is now in the… Google document?
So anybody who wants to join that?
And… And next week, we can discuss, the SIG surveys, and if we want to,
We'll start… kick that off again at some point, even though we're focused on some other stuff right now, but, yep, we can discuss those, and Juliano will be there too, and he was working on those, so…
he'll be able to put his thoughts in. Alright, there's nothing else?
Thanks, everybody. We'll see you online next week.
**Diana Todea** 29:11 Thank you.
**Johanna Öjeling** 29:12 Okay, fair.
**PL Pavol Loffay** 29:13 Thank you, bye.
