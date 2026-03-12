SIG: LLM Semantic Convention WG
Date: 2025-12-15
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/3X8gAjgENCe3y0mTqNC97-tDxfLATGdxyxUvukd_S90eEQYiedJJjznNo4A-ihTn.WeSsZMwI7OWza0Re
============================================================

## Zoom Recording Transcript

**Sergey Sergeev** 01:32 Hey, Sharon.
Hey folks, let's wait a few minutes if more people join. Unfortunately, I couldn't set up the reminder Ahead of time, so it may be just us.
So for today, we can… Just go over, some of the topics we have, For identic semantic conventions.
Let's wait a few more minutes if more folks load in.
Yeah, please add yourself into attendees.
If you have any topic, if you have any pull requests, specifically for AI agents.
Simantic Convention, instrumentation, and so on, please edit here.
**Pradeep Nair** 07:14 M.
We've got no pull request yet, but, based on the last SEG meeting, Pavan, Ridimo, and I, we were, like, thinking to combine the… the agent, types and the session ID proposal, into one proposal.
I think, but when there's a draft, we gotta review it.
Not sure when it will be, ready, but, just an update on… The session, and.
**Sergey Sergeev** 07:53 This one?
**Pradeep Nair** 07:54 Workflow proposal. Yeah, session and workflow, the proposal just above it, that Vadhima is working on, we have combined that.
into a single proposal, because, there was some questions around workflow and session ID, you know, like.
What seemed… seem to be, Very similar, so it was a better idea to combine them and have them both together in one proposal.
**Sergey Sergeev** 08:30 Yeah, and, surya, are you from, first of all, have I spelled your name properly?
Are you… maybe you want to do some intra… so most of us here are from Cisco Splunk.
So, the only name I do not recognize.
Is yours?
Do you want to do a quick intro?
Okay.
Yeah.
Anytime, if you want, to do an intra… Go ahead.
But otherwise, we will roll with the agenda.
This is, a first… Meeting covers a series for… Conventions and instrumentations for agents.
So, in today's meeting, we have just 20 minutes left, so, we will try at least review, the roadmap, kind of, what we know we need to do for identification conventions and instrumentation, and Probably it will be… overhelman, Lesplanque, and Cisco.
Requirements, but eventually we will add more work to it.
So, Pradeep, this is for the session, right? The ticket.
**Pradeep Nair** 10:26 Yeah, that's for the session, and the other one above it, by Vidhima is for the workflow and, step. So, basically, we will be probably closing, or just, you know, not updating these two, issues anymore, rather working on a new, issue, well, with the new proposal.
New proposals.
**Sergey Sergeev** 11:02 U.S.
**Pradeep Nair** 11:02 combines, both the issues and, like, wherever possible, it makes, clear, distinction between a session ID and a workflow ID, and why, or use cases where you might need both.
**Sergey Sergeev** 11:24 Yeah, wondering why we need the new one.
**Pradeep Nair** 11:29 So, like, in this, in the workflow, the… In the workflow, there is a span, not a span, what's that thing? A step, step type introduced, which was, again, like, you know, challenged in the last SEG meeting, like, it's probably, it's probably redundant, So, basically, the new proposal just makes… very clear distinction between workflow and session ID with clear examples, because workflow and session ID being in two different workflows and, sorry, two different proposals and workflow being mentioned in the session ID proposal, just caused a lot of confusion. So this is just to… You know, explain, those concepts better.
So, the new proposal, Pravan just shared it, like a draft version of it. It's not… it's not on GitHub yet, so we have to review that proposal, and create a issue.
**Sergey Sergeev** 12:41 This is a new proposal for both workforce and for session, right?
**Pradeep Nair** 12:45 Yeah.
**Sergey Sergeev** 12:54 And we can update, basically, the existing… Tickets.
This one, do we need… This one will be removed, right?
**Pradeep Nair** 13:19 Yeah.
**Sergey Sergeev** 13:20 One of the challenges with this proposal that, It's hard to comment on it.
**Pradeep Nair** 13:29 Yeah, I think, Parvan is probably going to just create a new proposal altogether.
**Sergey Sergeev** 14:14 Josh, sean, from your side, do you have any specific, You might see conventions, You need to… To purpose in the form of, formal.
Issues, or maybe a design document.
**shuwpan** 14:42 No, not from my side. Mine is like OpenAI, pretty well defined.
**Sergey Sergeev** 14:49 It's the instrumentation, right?
And for upstream work, not for angsta.
**shuwpan** 15:19 Upstream, I'm waiting for Keith, you two, to merge, and then… I would go from death.
**Sergey Sergeev** 15:33 Yeah, I'm just wondering, what is the current state, Keith, if you are on the call, so for the types… Where we give the type support in Gen AO2s.
What we see was JNA.
**Keith Decker** 15:50 We have inference.
So, L on invocation, we have metrics and spans for those. There is a PR out there for events that is being worked on in the Python contribute.
**Sergey Sergeev** 16:03 This is for AOM and vacation available.
**Keith Decker** 16:06 Yeah, so, and friend's comments.
We don't have any other types, and… Upstream, yeah.
**Sergey Sergeev** 16:16 And right now, we have only spine support, right?
**Keith Decker** 16:21 We have span and metric.
**Sergey Sergeev** 16:27 magic…
**Keith Decker** 16:29 And then events is in progress.
**Sergey Sergeev** 16:43 Yeah, if you can add, pull requests, so, or… Agent, specifically, agent invocation, and… Or invoke agent and create agent, right?
**Keith Decker** 17:00 Yeah, we don't have those in Upstream yet.
I don't think we have a PR out for those, either.
No, no, tools would be another one, right? Invoke tool and…
**shuwpan** 17:24 Or about embeddings?
**Sergey Sergeev** 17:33 Yeah, also not started tights.
for workflow, we also need.
So we have, basically semantic conventions, as an operation, GenAI operation.
type for InvokeTool, Invoke Agent, Create Agent.
And by Jenko, I think the only mission is workflow.
List for suspense.
Yeah, I think, step and workflow are missing.
Yin.
The spend, so basically what we need to do Let me see… End step, anybody started, one step.
operation for the Mandy Convention.
Yeah, I think, those types are needed, basically, before we can… really switch, any app, Steam.
Agent took… instrumentation… To using, this, which is Gen EA.
Types.
So probably we need to pull in internally if we can contribute to it.
And, probably we need to… To create, upstream, tickets on GitHub for those.
To make it the proposal.
Yeah, for instrumentation.
Right now, for agentic stuff, it's just, Linkchain and OpenAI agents with you. Has anybody reviewed, The coverage of those… Maybe we need to create automatic, if it… Ugh.
Basically, to take the coverage.
And probably we need to add a LAMA index and, Oh my god, what is the second one we are working on? It's a spoongeister.
**Surya Teja** 22:43 So, hey, hi, second.
**Sergey Sergeev** 22:45 Yay.
**Surya Teja** 22:46 I was also planning on adding Anthropic's agent SDK after I finish up with the Anthropic SDK. I don't know if you guys are covering that or not, but I don't know the appetite for adding it.
So…
**Sergey Sergeev** 23:02 But let me guess, are you from Antropica?
**Surya Teja** 23:05 No, no, I'm not from Anthropic, I've just… I've been using that, so…
**Sergey Sergeev** 23:08 Excuse me.
**Surya Teja** 23:09 Yeah, I wanted to do something for anthropic side, as we don't have any coverage, so trying to add that.
But I can, go in and work with the SDK team on the GitHub team to see if they can come to these meetings and contribute over there, because they also have been doing a lot of work in tracing and stuff in Anthropic side.
**Sergey Sergeev** 23:44 Can you probably add, to this? Yeah, ideally, we need to create, so we… didn't track well, I think, a different framework, instrumentation in GitHub, tickets. Maybe it's time for us to do it more formally. So, right now, there are some issues. Let's search for Anthropic, if there is already a one.
If I can on less power, it's always a challenge.
**Surya Teja** 24:15 Yeah.
**Sergey Sergeev** 24:18 Okay.
Opened last month.
Yeah, please review this one, if… Yeah, please circle back on this ticket reviewed, and…
**Surya Teja** 24:51 Yeah.
**Sergey Sergeev** 24:51 See if it's… A good one.
**Surya Teja** 25:27 So, that PR only covers only for Anthropic SDK.
It doesn't cover the anthropic agents, so they released a new SDK, they had an old SDK called as Cloud Code SDK, and they change that to Cloud Agents SDK.
So, after I complete the current one, I'm planning on contributing to Claude Agents also.
So, it will take a little bit of time, a couple of months, for getting to the agent stuff on cloud side.
**Sergey Sergeev** 26:09 Yeah, so if you could, just create that, gitHub issue with the.
**Surya Teja** 26:18 Yeah.
**Sergey Sergeev** 26:18 It will be great.
**Surya Teja** 26:20 Yeah, sure, sure, Sergei.
**Sergey Sergeev** 26:30 I guess, yeah, everybody's just releasing new waivers.
This is quite crazy and generative AI.
Maybe in Korea.
Okay, so, yeah, we have just 5 minutes, left, probably we will… Let's see if we have something, for Lama Index already.
And for Curie… So, Cisco Splunk team, maybe somebody can take an action, to create a GitHub ticket.
With, work description for those instrumentations.
Okay, my MBLT connection.
An action to do it.
Nice hose in.
Sri, and, which company are you from?
**Surya Teja** 28:13 I'm from Principal Financial Group, I'm not from any of the… what do you call it? Trace… tracing companies or anything.
**Sergey Sergeev** 28:23 Oh, yeah, got it. I, I didn't get, the name. Is it…
**Surya Teja** 28:29 Surya.
**Sergey Sergeev** 28:32 Okay, maybe you can add to this doc. Yeah, sure.
Okay, we have just a few minutes, left, probably OS, make this call, let's wrap up this call.
To prepare for the next meeting, if anybody has it.
Yeah, probably I will also update, He entered more details to the document, asynchronously after the meeting.
Yeah, thank you all, happy Monday.
**shuwpan** 29:19 Thank you.
**Erdenesaikhan Tserendavga** 29:21 Thank you.
