SIG: GenAI SIG (APAC)
Date: 2026-09-22
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:20 Yeah, hi, folks.
**Trask Stalnaker (Microsoft Corporation)** 01:23 Hey.
**Emil F** 01:27 Hello.
**Nida Hasan (Salesforce)** 01:31 Hey, guys.
**Trask Stalnaker (Microsoft Corporation)** 01:54 Alright, we… don't have Lynn Miller this week.
I think maybe next week also, I'm not sure.
So, but we've got… Agenda topics. Cool.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 02:18 Yes.
Yeah, this is, this is, about, a skill-related, semantic convention PR, and I also… provide similar issue, and this, yeah, this guy, he, provide a PR, and, he, implement, a similar thing I want to do, and, I want to ask a question. Is there anything.
He needed you, before Merge.
merging this PR, and if there are anything I can do, I'm also, interested in involving this PR, and.
**Trask Stalnaker (Microsoft Corporation)** 03:08 Yeah, I know, Lamila raised this before, and she has approved it. So definitely, always, your reviews and approvals on PRs Help to move things forwards.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 03:26 Okay, okay.
Yeah, I think with this…
**Trask Stalnaker (Microsoft Corporation)** 03:42 Guessed it in… the last week General meeting, if you want to check the… recording… Steve Rao (Alibaba Cloud (Singapore) Private LTD) 03:56 Yeah.
And, I watched the recording, and I found, Someone think it's not, suitable to.
to, design skill-related cinematic convention, so I… I… I don't do it, but I'm not sure.
Why he, why this also.
create this PR, and Ludmila agreed to accept this PR.
**Trask Stalnaker (Microsoft Corporation)** 04:34 Yeah, did you listen to last week's… Meeting… Steve Rao (Alibaba Cloud (Singapore) Private LTD) 04:40 No.
**Trask Stalnaker (Microsoft Corporation)** 04:42 Okay, last week's meeting is when we discussed this PR, and I raised that, with Ludmilla that previously it had been discussed in the meeting.
Hmm.
And what I… I think, was discussed previously in the meeting, or at least maybe was misunderstood previously in the meeting.
Was capturing a span for when the skill actually runs.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 05:12 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 05:13 Because that's not… Generally how they work, or that's generally not capturable, because the skill just gets added… it gets loaded into the context.
**And then… Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 05:29 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 05:30 The LLM, you know, from then on, it's kind of freeform. It's not like you run a skill, you load a skill into the context.
And I think that was… Maybe the confusion when we discussed it before, Or… Yeah.
So, this one is not about Running a skill, there's load skill.
Low skill resource, and this run skill script, she, explained, is a narrow… it's not, again, running a skill, it's running a script associated with the skill. I… I forget the.
But yeah, that… That's why it doesn't align with the previous discussion we had.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:21 Okay, okay, makes sense.
**Trask Stalnaker (Microsoft Corporation)** 06:33 Cool. Anything else?
That anyone wanted to chat about in this meeting?
Otherwise, we can keep it short.
Thank you all.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:54 Thank you.
**Nida Hasan (Salesforce)** 06:58 Thanks, Arun.
