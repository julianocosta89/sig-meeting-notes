SIG: LLM Semantic Convention WG
Date: 2026-04-21
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Surya Teja** 04:50 Hey, hi, folks.
**Steve Rao** 04:56 Hello?
**Surya Teja** 04:58 Hey, how is it going for everyone?
**Steve Rao** 05:00 Yeah, good.
**Surya Teja** 05:03 So, do we have an agenda that we want to discuss today?
**Steve Rao** 05:07 yeah, I guess, my colleague, my colleague, listed a topic.
**Surya Teja** 05:15 Oh, dear.
**Steve Rao** 05:16 Yeah, can you see it?
**Surya Teja** 05:19 Sure, let me quickly grab a look at it.
So, for reference, if we are not able to discuss it today, I'll take this and… present it in the SIG tomorrow, if you guys cannot join. Otherwise, you can join the SIG tomorrow.
Yeah, but let's, go forward, Let me see the topic list.
**Steve Rao** 05:49 Okay.
**Surya Teja** 06:00 Yep, the duration units, right?
**Steve Rao** 06:03 Yeah.
**Surya Teja** 06:09 Cool, yeah, let's go ahead with this.
**Steve Rao** 06:19 Yeah, do you share your screen.
**Surya Teja** 06:30 Wait a minute.
Let me join from… Another device.
Okay, just give me a minute.
**Surya Teja** 07:38 Hello?
**Steve Rao** 07:40 Yeah, yeah, I can feel you.
**Surya Teja** 07:43 Yeah, yup, yup.
**Steve Rao** 07:47 Okay, hello.
**Surya Teja** 07:50 Yeah.
It's been… I'm just joining from my computer, and I do not have… The… So, yeah, I have the… change, PR.
So… Can we go ahead and discuss it, and can everyone see my screen?
**Huxing Zhang** 08:28 Yes, we can see your screen.
**Surya Teja** 08:31 Yeah, go ahead, beautiful.
Okay, okay, okay. It's, it's, around the… Duration that we are emitting from our instrumentation, right?
**Steve Rao** 09:27 Yeah.
**Surya Teja** 09:30 Yeah.
So…
**Steve Rao** 09:36 Yeah, he wants to get some guidance.
How to, migrate from, millisecond to second?
Yeah, especially in some, production environment.
**Surya Teja** 09:50 Yeah, yeah, yeah.
This actually makes sense. We have implemented a few things in Python Contrib.
And I'm not sure how we are calculating it, for the OpenAI and Anthropic instrumentation that we're doing. I need to take a look at the code.
And, the question that I have for you guys is, do you think Or do you have any strong opinions on whether we should be Falling back to milliseconds that… Although… GenAI providers are using.
Or, should we add more documentation and discussion around what kind of metrics are needed.
**Steve Rao** 10:43 Yeah, maybe he wants to, extend the unit of duration.
Okay. Yeah, he, he has brought me up to the speed. Yeah, let me to, jump in for, for him, and, he can join the meeting, and, he, his, his question is, yeah, in, Hotel Semantic Convention, the dur… the duration union, Is there any, other options?
Except for, second, and maybe second is, another option for, developers, for, for users.
Yeah, this is, his main concern.
**Surya Teja** 11:36 Yeah, from what I believe, And the documentation suggests 80 seconds.
But I can double-check with Lydmila and folks tomorrow, and I can reply back on this question.
On what they are thinking. That's the first thing I'm going to do. The second thing that I want to ask you is.
You have given some good examples, stating that every GenAI provider, like Vertex AI or Bedrock.
are using milliseconds.
**Steve Rao** 12:09 So…
**Surya Teja** 12:11 From the instrumentation that you guys have been developing, are you… Preferring to use millisecond, or, Are you fine with choosing seconds?
**Huxing Zhang** 12:27 I think we prefer using milliseconds, because we used to use milliseconds long before GNI… on the GNI manual convention stopped, I think.
**Surya Teja** 12:40 Yeah. Yeah.
Makes sense. And, the next question that I have is, for, the semantic conventions around HTTP requests and everything.
are we capturing any duration metrics in milliseconds, or are we using seconds over there? Because… I can use those examples to build some case.
And state that we have to switch from seconds to milliseconds, and understand Why they stuck with… why they went with seconds and built case on that.
**Huxing Zhang** 13:15 I think, most of… in our case, we use milliseconds, because, you know that the microservice, they… they are shorter, the response time is shorter than, like, an AI agent. They usually… Response in sec- milliseconds.
So that's a common practice from us, I think.
**Surya Teja** 13:36 Yeah.
Yeah, that makes sense, actually. Then, I'm going to do these things. I'm going to repeat once again.
We are going to discuss this in, tomorrow's SIG meeting. I'm going to… Clarify whether seconds is the option or not, and then provide these examples that you have Jotted down here, saying that we have to swap to milliseconds.
And once, if there is consensus around, Switching back to milliseconds.
if… That is done. Can you guys work on changing the semantic conventions to milliseconds? We are going to add the notes around it, but… Then you… someone from your team can take the responsibility and change it to Milliseconds, if that happens.
**Huxing Zhang** 14:30 Yes, we also want to know the other providers, cloud providers, if they are Like, using seconds as a convention, how do they… how do they do things like that? How do they convert? How do they practice when they are… if the semantic convention defines the number of them in seconds?
**Surya Teja** 14:57 Yeah.
**Huxing Zhang** 14:59 We also want to know the practice from other providers, if they… some… Yeah, if there's some.
**Surya Teja** 16:06 So, I have two questions, guys.
Apart from these two questions, do you need any other answers that… regarding this?
**Steve Rao** 16:22 Yeah, maybe I think, they are the main concert from him.
**Surya Teja** 16:29 Pardoned?
**Steve Rao** 16:30 Yeah, I think they are the main concert.
**Surya Teja** 16:34 Yeah, yeah, yeah, yeah, yeah, yeah, sure, I would definitely, if, if Ludimilo is not on the call, I can work with her tomorrow and get answers for you on these two questions.
**Steve Rao** 16:48 Okay, thank you.
**Surya Teja** 16:49 Yeah.
Quote.
So What is the next topic in the agenda that, we… Want to discuss.
I see only one, actually, over here.
Is anything else, there in the discussion agenda?
**Huxing Zhang** 17:26 Actually, I'd like to ask, Another question is about, we… I think we have some discussion about the… how do we speed… speed up the development of this geni Semantic convention, and .
**Surya Teja** 17:46 Yeah.
**Huxing Zhang** 17:46 We'll talk about the possibility of a separate rephole, I think. Yeah.
what is the latest update from the… do you have any, Ideas of how that's that are going?
**Surya Teja** 18:01 Yeah, so right now, we are still weighing whether we can, Have a separate repository or not.
Plants are still in talks.
We haven't decided on that yet.
I believe Lydmila is going to… speak more on that. And, definitely, the plan is to engage with you guys also.
Right. Before we make a choice.
So, we are going to ensure that we join this meeting more.
And also discuss that thing over there. So, the short answer is, nothing is decided yet.
More, updates will be coming after… Tomorrow's and next week's meeting, because we are deciding on the roadmap.
on what we should focus on and stuff. And the next thing is… people in Python SIG.
Still need to respond on, Whether we should be opening a new Python repository, and a semantic convention repository for Gen AI and stuff.
that… It's still in flux.
So, did I give you the answer that you… did I answer your question, or was I missing anything?
**Huxing Zhang** 19:22 Yeah, okay, I got… so I… we need to wait, after, like, tomorrow's meeting, maybe.
We'll have, some update from that.
**Surya Teja** 19:36 Yeah, and also, here is the, our roadmap that, Litmila put together with, other folks.
So… You can take a look at this roadmap.
And can someone from your… I mean, I know it's not correct to ask, I don't know what time it is going to be tomorrow for you at, 12 PM… 12 p.m. EST, but if any one of you can join that meeting, it would be great, because, we need someone from Alibaba also to chime in on the things that we're discussing.
**Huxing Zhang** 20:20 Yeah, that's true.
**Surya Teja** 20:20 You guys cannot join.
**Huxing Zhang** 20:22 Sorry, I checked the time, it's, like, zero in the midnight, 12 o'clock in the midnight, so it's too late for us, I think.
Yeah.
**Surya Teja** 20:35 Yeah, yeah, that makes sense, that makes sense. What I can do is… For, Don't take this as something that I'm going to do, for sure, but… We are going to jot down what happened in this meeting, and in tomorrow's meeting, and we can post a short note so that you guys can be updated on the progress of things that we're doing, and on the progress of things that you guys are doing, so that we can stay in sync with each other. Does that sound good?
**Huxing Zhang** 21:11 Okay, so, let me clarify my, question, so… If, if there's a possibility, we can schedule… actually, we can schedule another meeting that's both available for you, or for the United States time, or for China time.
I'm not sure there's a possibility to schedule a separate meeting to discuss things about that.
In order to, make, you, you want communication from our… from us, I'm not sure, but because the… the… the meeting time is actually… actually is too… too late for us, so…
**Surya Teja** 21:56 Yeah, yeah.
**Huxing Zhang** 21:59 So, I would supp… I would have proposed to an… We schedule a dedicated meeting for that, if we want to discuss.
**Surya Teja** 22:10 Yeah, sure, I can take that also.
**Huxing Zhang** 22:28 So, do you know, your, the, the same meeting for the tomorrow meeting? So, what is the timeline?
for most of the attendees, are they from United States, or from, some of them are also from Europe?
Because if we're owning… folks from the United States, that will be easier for us to schedule a meeting.
He's like a… Like, 7 or 6… 5 a.m. or 6 a.m. MPT will be… A little easier for us to… to join the meeting. Yeah, we can do maybe 2 or 3 hours earlier.
So that we can have time to join.
But if there are folks from the United States and Europe and from China, I think it's… Impossible to schedule meetings for the… both… all of the three.
continents that, yeah.
Cannot be… join the meeting at the same time.
**Surya Teja** 23:33 Yeah, mostly folks are from US.
So… It will be possible, in my opinion, but I'll again check with them, and I'll get back to you. Is that fine?
**Huxing Zhang** 23:45 Right, okay.
**Surya Teja** 23:48 Yeah, but… for, the, what do you call it?
For the continuation of discussion, I'm going to post the… Meeting notes.
and PRs that need review.
in the Slack… channel, so that, you guys can review the PRs.
As well as, we can review your PRs.
And, make it faster.
To merge those.
**Huxing Zhang** 24:25 So…
**Surya Teja** 24:26 We… we definitely need reviewers Who can spend some time and, Review the peers, as well as people who can contribute… Code… In adding the instrumentation.
**Huxing Zhang** 24:43 Sure, we can definitely… to that, I think.
**Surya Teja** 24:49 Yeah.
Minghui, I… Am I pronouncing the name right? Right.
**Huxing Zhang** 24:57 That's right.
**Surya Teja** 24:58 Yeah.
Yeah. Is he in the call today, or…
**Huxing Zhang** 25:03 She, he's not in the meeting today, yeah.
**Surya Teja** 25:07 Yeah.
Yeah.
So… For sure, he reviews, he reviewed a few of my peers.
And, we can for sure, include, you and, Steve, I know, from, Java side, I actually…
**Huxing Zhang** 25:26 Yeah.
**Steve Rao** 25:27 Yeah, yeah.
**Surya Teja** 25:28 Yeah.
So for Python, if you folks are interested, I can, add you in few PRs.
Which you can take a look. We currently are implementing the GenAI utils.
And for sure, welcome you guys to take another look at FewPS. So… Zhang, right? How can I say your name?
**Huxing Zhang** 25:53 Hushing? Hushing? Who's gonna call me Hushing? Yeah.
**Surya Teja** 25:56 Yeah, Hushin, if you can ping me, or, GitHub, this thing, I can, CC you in that, PS also.
So, does that sound good, overall? I'll try to speak with them and see what works out better, and then if that doesn't work, even if that doesn't work out, I'll try to maintain some notes so that there is continuity of discussion and there's proper handoff between each other.
**Huxing Zhang** 26:27 Sure.
Sounds good.
**Surya Teja** 26:31 Yeah, cool.
Cool, guys. So, anything else to discuss?
**Steve Rao** 26:46 I don't have more questions.
**Surya Teja** 26:49 Yeah, sure, sure, Steve.
**Steve Rao** 26:52 Thank you.
**Surya Teja** 26:54 Yeah, can you guys post your GitHub, link or anything so that I can CC you in the PRs?
**Steve Rao** 27:02 Sure.
**Huxing Zhang** 27:02 Yeah, I will do it right now.
**Surya Teja** 27:20 Okay.
Great, guys. So, we are going to meet tomorrow, and I'll get you answers on the question that you asked.
And also on the timings thing. So…
**Huxing Zhang** 27:34 Okay.
**Surya Teja** 27:36 Thank you, guys.
Thanks a lot.
**Huxing Zhang** 27:38 Thank you.
**Surya Teja** 27:39 Have a great day.
**Huxing Zhang** 27:41 Have a great day, bye-bye.
