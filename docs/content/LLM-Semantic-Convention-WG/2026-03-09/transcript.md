SIG: LLM Semantic Convention WG
Date: 2026-03-09
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/3FKXabnV-1kEEUMeawQA8BXmNHpBFjGRS8SmScQL4YTGnCxUEFhzyg4-tLK7Ci40.GLZBxqEm6m9kvX6r
============================================================

## Zoom Recording Transcript

**Sergey Sergeev** 01:37 Hey. Happy Monday.
How's everybody doing?
**Wolfgang Therrien** 01:44 Hello, happy Monday.
Doing alright.
How about yourself?
**Sergey Sergeev** 01:55 Good, just too much stuff.
to get reset after the weekend.
**Wolfgang Therrien** 02:02 For sure, for sure.
**Sergey Sergeev** 02:20 Yeah, I am researching… Just adding a new record for the meeting agenda. So, today is a track, half an hour track for Mostly focusing on agentic, multi-agentic, semantic conventions.
And, what it means, more… More focus, towards, What we can define.
for… Multiple agent communications, and so on.
I'm just adding some… A placeholder, please put your name, if you… If you attend in here, just didn't attend this section.
Yeah, if you have any topics, please add it to agenda section over there.
Let me share the screen.
Oh, my… That was unexpected.
Yeah, and, the next topics, This is a good section for just keeping track of all the items, For all the meetings, so if you have anything for today, Or March 9th.
You can put it, right here in that… Agenda section.
Below, so I see a wall gun. You are hidden.
Something to overall topics.
I… don't see as a Microsoft folks, specifically, And kids to ask, So, looks like there is a proposal for invoke agent service plan.
And there are some standing topics which are probably for tomorrow's meeting, so tomorrow is more generic, generated for AI.
Semantic convention sync.
So, here in this call, I see… Some of us from Cisco Splunk, so… Erdan, Keith, Radeep… Shonian and Edima are actually from Cisco Splunk, and, do you want to introduce yourself, Volgang, or… Cam and, Victor.
Sorry if I misspote, and Mirk Krishna, sorry if I misspoke your names.
Bogdan, do you want to introduce yourself?
**Wolfgang Therrien** 06:56 Sure, sure. Hello, I'm, I'm Wolf King. I'm a tech lead for Agentic Observability over at Honeycomb, trying to come to these meetings on the regular to just see how we can help, and what we can move forward together.
**Sergey Sergeev** 07:11 Oh, this is cool, exciting, and exciting to see some of the proposal on the agenda.
So…
**Victor Lu** 07:23 Yeah, yeah.
**Sergey Sergeev** 07:24 Yes.
**Victor Lu** 07:25 independent… I was here before, I believe. Yeah, yeah, yeah. The reason I'm back here is I'm a generalist, so there is a other community I participate in, in particular one called COSI, Coalition for Secure AI.
where we discussed about telemetry, for AI, so, we agree there is some need to.
add some specific, matrix to both, OpenTelemetry as well as OCSF, which is for a different kind of purpose. I just wonder, the reason I'm, asking this question is.
the… the type of telemetry added, ideally will be mapped to a MITRE… DFAN, which is the ontology that's used extensively in the security industry.
So, at this point, my belief, OpenTelemetry is not… in any way mapped to those, standard ontology. Is that correct?
**Sergey Sergeev** 08:26 Yeah, I… I think it was mentioned, at least in the past, about the standard side. DTA is not here today, but he worked from our site, Viv.
Vivnag about this Gardeo security proposal, I think it was mentioned in that context, so, if you can, check the security spec.
From the Gumor…
**Victor Lu** 08:58 Yeah, I guess my question is, if that community, COSI, decided to continue with that mapping, are you open to, I guess, listen to what's been suggested from that community?
How to map it to, meet the requirement need for, security, and kind of correlated with OCSS. OCSF is for high-volume, analytics, so it's kind of a different purpose for, compared with OpenTelemetry, but the two can really be.
Kind of, synced up in a logical way, so that, Yeah, so that's something that's being discussed in that community.
So, is that… Is that something that can be discussed here in the future?
**Sergey Sergeev** 09:45 Yeah, I think, Nakumar probably has some magical, note-taker, which brought him here once we mentioned security, so… Agumara, do you remember the conversation about OCSF, basically related to security as a standards?
**nagkumar** 10:07 Yes, so I had a PR for the security guardian, I'm gonna paste the link, and that's the first opportunity.
**Sergey Sergeev** 10:15 That's right, right?
**nagkumar** 10:15 just… Yeah, it's… that's… that's that one. There was one comment about, someone from, this group who joined recently, was, like, all the way in the bottom. But OCSF has still not commented on it.
They also have meetings on Tuesday mornings at 9 o'clock, so it's kind of hard to get in.
**Sergey Sergeev** 10:42 Looks like Victor, was in that, meeting, and probably…
**Victor Lu** 10:48 Yeah, actually this was a different meeting, but I also, going… I'm a generalist, so I don't have to go into a lot of details. So, what's happening, there's another community called COSI, Coalition for Secure AI, where, we discuss about how to put AI, related to matrix.
And it was determined… you already identified that, really, the matrix needs to be in both, OpenTelemetry as well as OCFSF for different reasons, different, use cases. So… so that's why… so it will be… there will be some discussion in COSI on how to do that. So what happens… will happen next, we'll probably do some mapping there, and then propose to both here, for OpenTelemetry as well.
as OCSF to, to see whether to be all in sync.
**nagkumar** 11:37 Okay, that sounds good. Are they discuss… do you know when they're going to discuss this?
**Victor Lu** 11:42 Yeah, we have a weekly meeting, I forgot which day it's called, it's a telemetry meeting.
I think it's Wednesday. So yeah, so we'll, this has just been raised last week, so it will… it's still early, so once we have a proposal, we'll bring it here and share and see whether that's something you agree on.
**Sergey Sergeev** 12:03 Yeah.
**nagkumar** 12:04 That would be great. Like, we can branch off of this, whatever I have done, see what is kind of important to you, and plug those parts in.
Because my… my version is still, like, you know, we need some more feedback on it. The part where I have been stuck on is, like.
building some, prototypes. So, we know that Agentix, like, frameworks don't do this security by default, so there is no hook that I can, grab onto to generate these security events and traces and spans and all those that I've proposed.
So, that has been a limiting factor for me to understand if this is practical or not.
But of course, we are security where folks can kind of chime in and say, hey, here we have, like.
these five locations where we can send all these traces from, and the traces events, or whatever we propose. Like, if you find a practical spot to send those events from, then we can obviously take that proposal in.
**Victor Lu** 13:12 Awesome. We'll, we'll get back to you, should be in a couple weeks.
**nagkumar** 13:18 Yeah, feel free to, like, DM me on Slack, yeah, I have a pretty unique name, so you'll not find anyone else with my name. And yeah, you can get me in, and I'm happy to join the call and explain what I have done, and how I have come up with all those attributes.
**Victor Lu** 13:40 Awesome.
**Keith Decker** 14:19 You're muted, sir.
**Pradeep Nair** 14:35 Sergey, you're muted.
**Sergey Sergeev** 14:40 Oh my god, I was talking for a while. So, yeah, Sorry, I, I, I think, you guys should, basically collaborate, to basically to… to present, ideally for a Tuesday meeting with a bigger group, what are OCSF, metrics and attributes, and how to integrate it into OpenCelematics, so I think it will be, really helpful.
I just wanted to make sure that we also go over all the topics and all the people.
whom I didn't see on the call. Cam, do you have any… items to discuss, or just tuning in? Do you want to introduce?
**Kam Chehresa** 15:28 No, I'm just my first time meeting. I'm new to OpenTelemetry, but I just joined a new company that does GenAI observability and evaluation, so I see a lot of our customers sort of struggling with hotel and some of the vendors, and the disparity between the attributes, so I just wanted to learn more and hopefully contribute in the future. Thank you.
**Sergey Sergeev** 15:54 Sounds great. Congrats.
join the company, and wogan, do you want to bring up Eurotropic?
**Wolfgang Therrien** 16:05 Sure. So there's, if you just click through to that issue, this is just sort of, radiating some information here. I think this aligns with the kind of work we're trying to do here.
And, I'm not quite sure if this maps to maybe one of our existing or planned, semantic conventions, but I just wanted to put this here to give… for folks to maybe have a read of it, and if there's, something that, connects with, something that we, have on the roadmap. Maybe we can call it out, in the comments here, or you can shoot me a DM, and I can, you know, I can respond here. But I just wanted to make sure that folks saw this, because I know a lot of folks trying to manage that complexity are, are reaching for, for things like, agent trace.
**Sergey Sergeev** 16:57 Yeah, so what we, have right now in semantic convention, we have, GenAI, basically a GenAI namespace, and we have, invoke, Agent Span.
Which covers a lot of operations, So I'm wondering, if, this… How is this different? Maybe you can provide more, background?
**Wolfgang Therrien** 17:25 Yeah, I think, you know, when I was reading through, sort of, the GenAI stuff, maybe, maybe it wasn't, quite as clean a mapping, but I will give it a, a closer look, and maybe I'll follow up on Slack.
**Sergey Sergeev** 17:41 Okay. Yeah, sounds good. V…
**Wolfgang Therrien** 17:44 But yeah, I think there… I think there is probably an existing mapping. I just wanted to see if other folks, Had one, that jumped out to them.
Thank you.
**Sergey Sergeev** 17:58 I have, if… if we don't have any other topic at this moment, so I also, have, a little bit, of an open-ended question, Nakumar, or probably anybody else, Do you see some, Agents using, human interruption, or basically interruption and resumption of workflows.
So when, when an agent needs, for example, human feedback, human approval, and etc.
How do you represent, this telemet in semantic kernel… in AutoJN, or semantic kernel, or Microsoft, agentic framework?
**nagkumar** 18:55 We usually do it as a chat span.
Like, with… You know, user-generated chat spam?
**Sergey Sergeev** 19:06 User-generated chat spans, so, Basically, when an agent decides to interrupt execution of a workflow and request human For additional feedback, what type of span is it?
**nagkumar** 19:28 Oh, so that action is not captured.
Sergey, so the following action, like, let's say the agent decides, you know, human interaction is needed, the human interaction is captured as a chat span. Like, whatever the human says is then sent as a chat span, so until what the human says, I don't think we are capturing anything there.
**Sergey Sergeev** 19:52 Yeah, I, I, I, I, I did some AI research, On it, I can probably, share, and, the reason it was, brought up by some team who are doing it in WangGraph, WenChain, so… and, specifically.
the way it's implemented in a WNGraph, so when there is a user interruption.
Basically, a Wang graph throws an exception.
**nagkumar** 20:30 Yep.
**Sergey Sergeev** 20:31 It doesn't show… which doesn't do work really well.
And, specifically the challenge with, this, that, basically, if… User doesn't provide feedback or approval instantly, so it might take way more than the trade span, so if you If you try to keep that workflow On the same trace.
So it may be just 2-1 coffee window.
So it looks natural to use, Conversation ID to stitch together different traces, but, I'm wondering if, there are some ways to to provide, additional… Additional, metadata… Veach.
Which step in the workflow, basically.
requested.
User feedback, how to represent that user feedback, And if it's a new trace, How can we track, basically, the span which requested user feedback?
I think, Yeah, it's… again, sorry, I think it's a, it's an ask, for Microsoft Agent Framework team. Yep. Because they were trying to use, spend links, to show better, message and communication, I think it may be, Fitting the same.
Buttern.
**nagkumar** 22:31 Makes sense, yeah. I messaged it all.
**Sergey Sergeev** 22:35 Oh.
**nagkumar** 22:37 Yeah, Tao was the agent framework person, I think he was here last week.
**Sergey Sergeev** 22:42 Yeah, yeah.
Yeah, especially, it's a mix also of, client-side agents, which run in your environment and, server-side agents, like OpenAI.
Okay, I was wondering… I will bring it up in tomorrow's meeting as well.
**nagkumar** 23:29 Okay.
**Sergey Sergeev** 23:29 But I'll, share this research.
True.
Otherwise, do we have any other topics, right now?
Hey, if nothing else, yeah, we can probably take a few minutes back.
And they have this meeting.
Early.
**Wolfgang Therrien** 24:26 Thank you much.
**Sergey Sergeev** 24:28 Thank you.
**Erdenesaikhan Tserendavga** 24:29 Thank you.
