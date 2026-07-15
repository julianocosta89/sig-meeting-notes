SIG: LLM Semantic Convention WG
Date: 2026-07-14
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao** 01:20 Yeah, hi, Traska.
Hi, Traska.
**Trask** 01:28 Hey, Steve.
**Steve Rao** 01:29 Yes.
**Trask** 04:42 Looks like it might be only us today.
**Steve Rao** 04:46 Yeah, yeah, maybe.
**Trask** 04:50 I, I'm.
It's going to be a couple more minutes before I make it to my desk. Is there anything you wanted to chat about or you could share the screen and we could chat about a couple of things?
**Steve Rao** 05:06 Okay.
Okay, yeah, can you see my screen?
**Trask** 05:19 Yeah.
**Steve Rao** 05:20 Oh.
Okay, and yeah, I left a agenda. Yeah, on today.
Meeting.
yeah, I have a I have a question just like describe here.
Yeah, recently, we want to distinguish multi-turn conversation.
And we want to achieve multi-term conversation evaluation.
And how to… Yeah, tag, Several trace to, multi-turn conversation.
Yeah, this is the first question, and the second question is, Yeah, maybe. How to collect the identifiers.
in multi-conversation, in different framework.
I want to hear the comments from community. Is there any Use case or idea to share.
And I also found in community issue. There are some similar issue. They want to achieve similar. They have similar Popular.
And yeah, this is, yeah, I guess this is latest one.
And yeah, just like.
Describe on the screen.
**Trask** 07:31 Yes.
Now, Do we… are we capturing conversation ID for any of the frameworks already?
**Steve Rao** 07:49 Yeah, in AI coding framework, I think it's not so hard to capture the conversation ID.
in AI coding a framework. Maybe we can assign the session id to the Gen. I conversation id to To achieve this target.
**Trask** 08:21 I see. Is Conversation ID… Something that gets past… To the, the LLMs?
Or that it's only retained by the… At the agent level.
**Steve Rao** 08:43 Okay.
And yeah, I have a small question. I also discussed with Ludmila last time. How do you see the session and conversation?
means, such as, and.
Mode key… Term… Conversation… Equal session or not.
Yeah, maybe.
**Trask** 09:23 I feel like session would be something.
Broader…
**Steve Rao** 09:31 Mmm.
**Trask** 09:32 I mean, what, what's the.
Purpose of capturing the same thing in both places.
**Steve Rao** 09:40 Hmm.
Yeah, you mean this concept, mail come from brochure?
**Trask** 09:53 I'm not really sure what… yeah, I… I'm not sure what session… represent in… Gen AI.
In, in Gen AI semantic conventions.
**Steve Rao** 10:11 Hmmm.
**Trask** 10:14 It feels like mostly we care about conversation.
**Steve Rao** 10:20 Hmm, yeah.
**Trask** 10:23 Yeah, I.
So, I guess I would… And we have the… Conversation ID, I guess I would… Probably… Focus on that.
over… Session.
**Steve Rao** 10:41 Okay.
Okay.
makes sense. Yeah.
so in Jni semantic convention, we provide attribute, yeah, Gen. I. Yeah, check.
Gni conversation id to capture the identified.
**Trask** 11:16 conversation.
Do we, can you check the, our reference scenario?
And.
To see if we are capturing conversation ID in any of the reference scenarios.
**Steve Rao** 11:35 Mmm.
You mean the description of conversation ID?
**Trask** 11:46 No, go to the reference scenarios.
**Steve Rao** 11:52 a reference scenario.
**Trask** 11:55 Go to the top of the repo route.
**Steve Rao** 12:00 oh.
That is the issue, or…
**Trask** 12:09 No, I go to code.
**Steve Rao** 12:12 I'll go to the code.
Okay.
**Trask** 12:18 And then go to reference directory.
**Steve Rao** 12:22 Reference.
Okay.
**Trask** 12:30 And yeah, scenarios.
And scroll down… is this… oh no, go back up a directory?
**Steve Rao** 12:40 Hmmm…
**Trask** 12:44 Go back up.
a directory.
**Steve Rao** 12:51 A directory.
**Trask** 12:54 Go back to reference.
**Steve Rao** 12:56 Okay.
Preference.
Oh.
**Trask** 13:01 parent directory.
**Steve Rao** 13:03 Clear reference.
**Trask** 13:04 Yeah, yeah. And scroll down.
For… yeah, for the spans, let's see… Maybe, where would we see… Conversation ID… Is it on… It's on inference spans.
**Steve Rao** 13:29 Inference span here.
**Trask** 13:33 I don't know, I'm asking you, is this where… I don't remember where.
conversation ideas captured, I'm guessing.
**Steve Rao** 13:48 Yeah, conversation.
**Trask** 13:49 There. So, we do have two reference scenarios.
In case this helps you.
**Steve Rao** 14:04 Mission lighting.
Oh.
But I'm not sure why I can search this Use case.
Okay.
Okay.
In… Google Apps.
Adk.
It's provider session. Id.
**Trask** 14:47 So they call it session ID in ADK, I guess.
**Steve Rao** 14:53 Yeah, society.
Yeah, and I also, sat at in… In some, coding agent, such as OpenCode or something like that, and it also provides, session… Concept.
**Trask** 15:17 And, is session… is there a session concept the same as conversation?
**Steve Rao** 15:23 Yeah, yeah, I think.
Yeah, you can.
**Trask** 15:28 Yeah.
**Steve Rao** 15:28 That's new session, something like that.
**Trask** 15:32 I mean, it's a good question, then, I mean, if it is the same thing as session, I'm not… Sure.
**Steve Rao** 15:42 Mmhm Yeah, okay, yeah, I, I, I understand the first question, and, yeah, another question is.
How to achieve this, this goal, yeah, maybe, Yeah, from my knowledge, yeah, I found, yeah, maybe in AI coding scenarios, it's not so hard to capture, the identified, and we can store this identified to the conversation. Id. And in some other scenarios.
other framework, such as long chain, long graph, or something like that.
Yeah, how to… yeah, how to… yeah, maybe it's not so easy to get the, identified and, How to achieve a multi-turn conversation evaluation is a problem.
I'm not sure, do you come across a similar question, or is there any… Wong. Ask a similar question. In community.
**Trask** 17:09 Being able to link the evaluation event back to the conversation.
**Steve Rao** 17:16 Yes.
**Trask** 17:30 Yeah, no, I don't know, It does seem like… something very useful.
**Steve Rao** 17:42 Hmm, okay.
**Trask** 17:44 Yeah, I guess for kind of for both of these, like.
Probably what I would recommend is, you know.
Start with sort of instrumentate, you know, take.
Some of the frameworks, and some of the existing instrumentation, and See, you know, like kind of you have to dive into it to see if these.
Things are even capturable.
If there's, if the frameworks, you know, provide that, if they provide something Correlatable.
Yeah.
**Steve Rao** 18:30 Okay, yeah, you mean, yeah, maybe, we need to, solve this problem case by case, and, You found it.
**Trask** 18:39 Well, at least prototype a couple, like, to see, you know, what kind of… Like, if you're trying to make… if we're trying to make changes to these scientific conventions, we need to kind of see if there's… Support for that in a couple of frameworks, at least.
Hmm.
Yeah.
**Steve Rao** 19:02 Okay, yeah.
**Trask** 19:04 That's kind of why those reference scenarios exist in the repository.
is to… Encourage us to… Kind of take a… Practical.
perspective on what is what we can capture or not.
And we'd like to see at least, you know, two frameworks where… something as possible before we… Encode it into the semantic conventions.
**Steve Rao** 19:45 Okay, makes sense. Thank you.
**Trask** 19:48 Yeah, sure.
**Steve Rao** 19:51 Yeah, I don't have more questions. I'm not sure. Is there anyone want to talk about something?
Hi, Tom Yoo.
**Trask** 20:03 Hi, Tom.
**Tom Yu** 20:04 Yeah, I… Yeah, hi. Hi, it's me.
Strasque?
**Trask** 20:10 Yes.
**Tom Yu** 20:11 Yes.
Yeah, I… I think I don't have new topic today, I… I proposed 3… Pull requests, last week.
And, I… I just want to follow up.
Hmm, okay.
To see how.
How it would pro-process… proceed.
Yeah, and, last week, I think that's.
Medicova, is on the meeting, right? And, He, he said the Finnish, yeah, the Finnish, Finnish reason proposal is Is quite reasonable and he she she would.
She will, check.
why Finnish reason is double recorded in both messages and And us.
and a specific field. Hmm, I am.
And, about… Another PR is about the input message delta attribute.
And proposed… And a field to record.
the new message.
And the request rather than the whole conversation and the and the request to compress.
And, spend size.
**Trask** 21:59 Right.
**Tom Yu** 22:02 Yeah, and I think there are some discussed under the pull request now, and I just wait to see… And.
Will there be more comments here?
**Trask** 22:22 Okay, cool. I do both of these… PRs have the reference scenarios.
I'm seeing, it looks like the… our… I don't… I'm not noticing the… our standard PR template here.
which has some… Yeah.
**Tom Yu** 22:58 So, what do you mean? You don't understand the template, or what?
**Trask** 23:03 No, we have a PR template that we ask all people to fill out, and it looks like When you opened this pull request…
**Steve Rao** 23:15 You know.
**Trask** 23:19 No.
Oh, look for, go to the .github repo.
**Steve Rao** 23:25 Github.
Got it.
**Trask** 23:28 GitHub. Go to code.
**Steve Rao** 23:31 Okay.
**Trask** 23:32 No, you're in the right place, just go to code.
**Steve Rao** 23:36 Oh, yeah, okay.
**Trask** 23:38 Yes.
And that GitHub?
**Steve Rao** 23:42 Here? Directly.
**Trask** 23:45 No, I click on the first directory.
**Steve Rao** 23:49 first to derived.
**Trask** 23:53 Yeah, that one.
dot.
GitHub.
**Steve Rao** 23:58 Okay. Okay, okay.
**Trask** 24:03 And then pull request template.
**Steve Rao** 24:09 Okay.
**Trask** 24:10 Yeah.
This is and if you go to raw.
Click the raw view.
R. A. W.
**Steve Rao** 24:31 Umm.
**Trask** 24:32 Raw.
In the right… Upper right.
Sure.
**Steve Rao** 24:38 You you mean to let me type a word.
**Trask** 24:42 R A W.
Yeah, click that.
**Tom Yu** 24:46 Okay.
**Steve Rao** 24:47 Okay, okay, you mean here.
**Trask** 24:53 So this is our DR template, Tom.
**Steve Rao** 24:57 Mmm.
**Tom Yu** 24:58 I understand.
**Trask** 25:00 Yeah, if you could fill this out, that would be helpful.
**Tom Yu** 25:05 Okay, I will adopt the messages.
to this template.
**Trask** 25:12 Cool.
Yeah, importantly, this calls out the reference scenarios.
And that's what I was asking. And apologies, I'm not at my… Desk yet this morning, so this is why it's a little… Harder for me to provide more.
Feedback.
**Tom Yu** 25:42 Okay Right.
**Steve Rao** 25:48 Okay, yeah.
Yeah, if we don't have more comment or question.
Oh.
Yeah, okay.
Yeah. Thank you, Chaska.
**Trask** 25:58 All right.
Thanks, Steve. Thanks, Tom.
**Steve Rao** 26:01 Mmhm.
**Trask** 26:02 Bye.
**Tom Yu** 26:03 Thanks.
**Steve Rao** 26:03 You're next.
