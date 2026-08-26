SIG: GenAI SIG (APAC)
Date: 2026-08-25
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:40 Hello, good morning.
**Trask Stalnaker (Microsoft Corporation)** 03:43 Hey! Good morning.
I think good morning to Iwa as well. Your Pacific time?
**Iwa Wong** 03:53 Yes, and Pacific time. Thank you. Good morning to you all.
And, good evening to… afternoon to whoever.
Around the world as well.
And thank you for standing my PR.
**Trask Stalnaker (Microsoft Corporation)** 04:08 Oh, yeah, yeah.
Thanks for sending that.
**Liudmila Molkova** 04:15 Can you folks see my camera… see me?
**Trask Stalnaker (Microsoft Corporation)** 04:18 We can, yes. Okay.
**Liudmila Molkova** 04:20 Okay.
**Trask Stalnaker (Microsoft Corporation)** 04:21 We also see a second Liudmila,
**Liudmila Molkova** 04:25 Oh… Okay, she'll go away at some point.
Gay… Or do… it's probably my turn, because I was neglectful of my duties last week.
**Neil Yashinsky** 04:49 I won't tell anyone if you don't.
**Liudmila Molkova** 04:55 People would know. There will be signs.
**Neil Yashinsky** 05:08 We can just call it…
**Trask Stalnaker (Microsoft Corporation)** 05:09 Do you like the all-caps announcement.
I am here.
**Liudmila Molkova** 05:16 Finally.
Okay, our agenda is empty, but I don't think it's the real… data thinks.
to maybe… We can see what we can prioritize from our pull requests.
Let's see… I think this one is interesting, but I don't think there is anything to discuss. It's more of a question if people have any strong objections.
on, this, so I'm going to… Pass, unless once somebody wants to add,
**Neil Yashinsky** 06:08 Could you just… Liudmila, sorry, could you just make your screen just a little bit bigger?
**Liudmila Molkova** 06:12 Sure.
**Neil Yashinsky** 06:14 And which one were speaking about?
**Liudmila Molkova** 06:17 This one, the one that's waiting for maintainers.
**Neil Yashinsky** 06:20 Got it, thanks.
**Liudmila Molkova** 06:21 We can merge it, it formally has the approvals, and I approved it. I just want to see if people have had a chance to review.
And share their thoughts.
Okay, under everything else is waiting for… others, But I think we've made some progress on the… Different parts… For example… I don't see a life… Here.
**Trask Stalnaker (Microsoft Corporation)** 07:08 Which one?
**Liudmila Molkova** 07:10 Oh, here we go.
okay, there are a bunch of open.
Duck pilot, okay.
Cool.
Okay, we have something on the agenda… But also, I wanted to talk about Instrumentations?
**Trask Stalnaker (Microsoft Corporation)** 07:50 And I suspect Victor's, Agenda item is for the next meeting.
**Liudmila Molkova** 07:58 Okay.
Because she's not here.
**Trask Stalnaker (Microsoft Corporation)** 08:02 Yeah.
**Iwa Wong** 08:05 She was letting me know that he couldn't make it, so I'm not sure if, Arthur, her mother is going to be here, so he wanted to make sure that, like, that was an agenda item on there to discuss, save it to our next meeting as well.
**Liudmila Molkova** 08:24 Which one.
**Iwa Wong** 08:25 Vector, and…
**Liudmila Molkova** 08:28 Oh.
**Iwa Wong** 08:30 Yeah, Victor told me that he wouldn't be able to make it.
**Liudmila Molkova** 08:36 Okay.
**Iwa Wong** 08:37 So he wanted me to actually make sure that, the group here has the link to, the spec and the slide for review.
**Liudmila Molkova** 08:49 Okay, sounds good.
Do we have anybody in this call who wants to talk about anything specific?
**Neil Yashinsky** 09:06 Oh, sorry, go ahead.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 09:09 Yeah, I, I just, yeah, Huxin, create, a blog, PR, In… yeah, I share. And, he let me, to… yeah, I sent a hyperlink.
**Liudmila Molkova** 09:29 Am Ice.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 09:31 Yeah, he don't have time to, join today's call. Let me… Happy to, share this, PR, and if, anyone have comments, yeah, please, left your comments on it, and I see Ludmila, you have left some comments. Thank you.
**Liudmila Molkova** 09:55 Yeah, thank you, for… and thanks, Hu Xing, for writing this.
There are some minor, like, technical caveats and some style, suggestions, but it looks good.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 10:08 Okay.
Okay, thank you.
**Liudmila Molkova** 10:13 Cool.
**Neil Yashinsky** 10:16 I was gonna… I'd like to speak to the group, but next week, I'd like to introduce something that I've been working on. It's great, really cool to see you're building Agent Harness, not quite, there's a little bit of overlap, even, Steve, with what I'm building, so it's a new benchmark for AI development, only tangentially related, of course, to the AI semantic dimensions, but I think it could be of interest to people if there's time for it next week, to talk about Kit.
**Liudmila Molkova** 10:48 Okay, sounds great. Should I put you on the next?
**Neil Yashinsky** 10:51 Yeah, let's do it.
**Liudmila Molkova** 10:52 Any announcement on this? Like, harness?
**Neil Yashinsky** 11:00 Sagan?
**Liudmila Molkova** 11:01 Do you want to put any announcement around it? Some harness instrumentation or something?
**Neil Yashinsky** 11:07 Oh, well, the similarities are more of… well, I… let me think about that… I mean, next week, definitely.
I don't know if I'd have, like, enough content to, like, put together an announcement quite yet.
**Liudmila Molkova** 11:20 Yeah, I mean, I mean, just for the, sake of this line, what should we put here? And feel free to go ahead and…
**Neil Yashinsky** 11:28 Sorry, yes, of course. Here, why don't I put something, to save you from typing my words? That's great. Yes, I will definitely use it.
**Liudmila Molkova** 11:35 Yeah, thank you, appreciate it.
**Neil Yashinsky** 11:37 Yeah, feel free to correct it or whatever, format it as you see fit afterwards, yeah.
**Liudmila Molkova** 11:44 Yeah, do we have Jan here?
It seems it's also for the next meeting.
Okay, so maybe we'll spend this time, then looking into the instrumentation. So we are mostly talking about Celante conventions in this meeting. Maybe we'll take a look at the Instrumentations and different parts of the implementation journey.
Okay, so… I'm not… updating it, like, quickly, but I'm updating it every once in a while.
And, where… I think what we miss, and as, A tracking issue is the… Like, the status of… What's left?
And if anybody would be interested, it would be cool to… I don't know, contribute a skill that analyzes the status of instrumentation between two different, Libraries, like Open Inference and OpenTelemetry.
And, we would then know what's left.
Because looking here, it seems pretty solid.
But I think there are parts that are still… missing.
**Neil Yashinsky** 13:28 No.
Which… Is that a specific, pull request you're looking at? What's the view you're looking at? Sorry?
**Liudmila Molkova** 13:35 So this is.
**Neil Yashinsky** 13:35 One for one?
**Liudmila Molkova** 13:36 In a shoe.
**Neil Yashinsky** 13:37 Oh, okay, great.
Yeah, I'll take a look. I won't have any time, till a little bit later, but I'd be happy to peek at that, in the afternoon feature.
**Liudmila Molkova** 13:52 Yeah So… We, this is the tracking issue that, where we monitor the migration of open inference instrumentation to open telemetry.
And, while… We know that people are working on some parts, we don't know what's left.
And what I'm suggesting is to maybe start documenting it more precisely than on the individual library's level.
And I'm just taking a look to see what we have and what we need to tackle.
Next.
So we have a decent number of things for Langchain, OpenAI, for Paydantic, the… there is native instrumentation, and we now have conformance tests. They are not merged yet for the native instrumentations. So, what I'm thinking, maybe I replace this link with the link to conformance tests, and then add some indication of whether How close it is.
maybe I'll just use some t-shirt sizing, but, like, Very far, pretty close, or… Conformant or something.
Then… But this one is pretty good.
the Anthropic, I think, Surya told that it's… very… Closer, done.
This one, I think we're postponing, because… We are… We heard the rumors that maybe Antropic will have native instrumentation?
**Trask Stalnaker (Microsoft Corporation)** 15:54 Someone joined last week, when you were out from Anthropic.
**Liudmila Molkova** 16:03 Okay.
Our Aaron told me where they… Were they interested in instrumentations at all, or, like, native parts?
**Trask Stalnaker (Microsoft Corporation)** 16:13 They definitely were interested in, you know, what they could capture. I mean, they didn't raise… That's any topics on their own, but they, participated in the conversations as far as, like, what kinds of things they could and couldn't capture.
So, promising.
**Liudmila Molkova** 16:35 Yeah, awesome.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 16:40 Yeah, yeah, for… for this issue, I, I guess maybe Zooming also, is interesting in migration, something like that, and, he also, sent some PR, in, this library to provide some, instrumentation from Alibaba, and, I can talk to him, and, if, if He's interested in it, and yeah, he maybe can, join this.
**Liudmila Molkova** 17:17 Okay.
Sounds good. It would be… I think there is a tracking issue somewhere here.
So, it would be… Nice to see… Oh, you're the priorities.
It would be nice to see where there is an intersection, and maybe… if you folks can analyze, like, where we have an instrumentation for this, what's in the OpenTelemetry instrumentation that's What is not there that you folks have?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:12 Hmm.
**Liudmila Molkova** 18:28 Yeah, I wanted to look here to understand where we are, mostly, and to have some common idea.
And… It would be nice to just format this issue in a similar way and remove duplications.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:53 Okay, okay, yeah, I… I can talk to Jimin later.
So…
**Liudmila Molkova** 19:02 Yeah.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 19:03 So, what's this issue?
**Liudmila Molkova** 19:08 Sorry?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 19:09 Yeah, I, I will talk also of this issue.
**Liudmila Molkova** 19:15 Okay.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 19:16 Zooming, yeah.
**Liudmila Molkova** 19:18 Sounds good.
Okay, so… Yeah.
I think what we miss is… like, what people think, how we should drag this.
I personally, I miss knowing what's left.
**Neil Yashinsky** 20:09 I'm not ignoring you, I just don't have any ideas.
**Liudmila Molkova** 20:12 Okay, I see.
Okay, so then, we have 10 minutes left, and I see two people who, it seems, want to introduce themselves.
Maybe we should do this now?
I don't want to call you out, but if you want to introduce yourself, go ahead.
**Jeremiah Ross** 20:34 Oh, yeah, hi, sorry, I know it's kind of weird, because… I just showed up out of nowhere.
**Trask Stalnaker (Microsoft Corporation)** 20:40 Not weird at all. Okay. Welcome.
**Jeremiah Ross** 20:43 Basically, you know, I've been… I've been sucking off of the, open source ecosystem for years, and I appreciate it, and so I'm looking for ways to give back and get involved, and since I'm in, you know, the observability space.
hotel makes a lot of sense, so I'm just, like, checking out the different groups, trying to figure out which ones, you know.
makes sense that I can contribute to, and that's it. So, I'm listening in this week.
And learning. My name is Jeremiah Ross, by the way.
I'm in San Francisco. San Francisco Bay Area.
**Neil Yashinsky** 21:17 Nice.
**Trask Stalnaker (Microsoft Corporation)** 21:19 Welcome!
**Jeremiah Ross** 21:20 Thank you.
**Iwa Wong** 21:25 Hi, I guess I can go next. I'm Iwa. I am based in, Wetman in Washington.
I've been previously with, big tech companies, including AWS, I have been focusing on my career entirely focusing on, security, in particularly, observability pipelines.
I previously drove down, DDoS mitigation, that was end-to-end on the computing platform from 30 minutes to time to 3 minutes, because of the, simplifications and re-architecture that I did, with, the whole observability pipelines.
But I think, it is time for me to, contribute to the open source community, and, very recently, I've been, getting myself My hands dirty on the agent side of things, and realized a few gaps.
on.
how do we, observe the two calls, executions, and the intent of these agents, and all in the same telemetry? And I realized that, like, there is a really, good industry, standard. Maybe there is one, that this group is forming.
I have no idea, but yeah, hope to, start my journey, if not too late, on open source, and really.
Help the industry to define some.
Center, and be part of the journey.
**Neil Yashinsky** 22:58 Thanks!
Yeah.
Welcome, you know, Iwa and Jeremiah, and someone who's not exactly new, but somewhat new to Hotel for just a few months, you know, I really will compliment, Liila and Trask. I mean, they do a great job of running a volunteer organization, but like all volunteer organizations, you know, it's basically as good as the output of all of its volunteers together, and so that's, you know, it's a double-edged sword, but it's a great one in my opinion, and Third, you know, in my opinion, you gotta kind of… spend a little bit of time just listening and getting to know things, but then you'll, you know… it'll just emerge, I think, when you find good opportunities to collaborate, or a SIG that connects with you, or maybe you, like, gotta do your own thing, and you're like, this is what's missing here, and I feel like, people are very supportive.
In steering people in the right way that's not, like, structurally harmful or whatever, you know? And that's kind of the good thing. It's like, if you have a really good idea, they'll tell you so, and if you have a really bad idea, they'll also maybe tell you so, or provide the right perspective of, like, hey, this is a large community of group, and so your great idea could still be great, and just not necessarily be right for hotel, or as it's… Whatever, I don't want to overgeneralize, but… Like I was saying, I think it's a really supportive community, and you know, lives up to its goals, unlike a lot of organizations that I think, you know.
I'll struggle with that. But, yeah, that's just me. Welcome.
**Trask Stalnaker (Microsoft Corporation)** 24:26 Yeah, and Iwa, thanks for your Java PR. I would say… I will say for both Jeremiah and Iwa, it is easier to get involved initially on the coding side, the instrumentation side.
The spec side, semantic conventions and specification side is… Thorny, even for us, and we… we do look for those, like, if you are wanting to drive spec issues, it really helps to sort of First, understand the instrumentations, and then build out prototypes of those spec issues in the instrumentations. Kind of try to push the instrumentations forward as sort of support.
Glad, for these spec issues.
**Iwa Wong** 25:23 Yep, sounds good. Yeah, we'll take a look at the instrumentation, and oh yeah, definitely.
**Trask Stalnaker (Microsoft Corporation)** 25:30 look, if you haven't looked at the Python GenAI repo, that's a great one right now.
A lot of stuff going on there, and very, of course, relevant to this SIG.
**Iwa Wong** 25:42 Okay, sounds good.
**Liudmila Molkova** 25:48 Yeah, welcome, both of you. There is another effort that I think is… is awesome.
that, especially if you're new, it's kind of easy. Trask, what do you think about People adding, let's say, Java.NET, Go instrumentations to our conformance.
a repo.
**Trask Stalnaker (Microsoft Corporation)** 26:13 Yeah, yeah, definitely.
Especially if there's something that you are particularly, interested, like, if you have, you know, background in Ruby, the… currently, the conformance repo.
So there's going to be, like, 10 or 11 different languages in there, and, Ludmila and I are starting to populate them with, various instruments.
But we only know so many of those languages, so the rest of the languages are… our PRs are… entirely vibe-coded. Well, I mean, I guess they all are, but at least I can… then I can verify the, a couple of the languages make sense. Liudmila can verify a lot more of the languages, but we're still missing, many.
expertise.
**Iwa Wong** 27:11 Yeah, I'm definitely a Java developer here, as you can see.
Yeah, Python is something that I picked up for the past 8 months. I wouldn't say… I wouldn't say that I know the language, I'm still trying to write Python, not like a Java developer, so… So a lot to learn here. I can take some steps, And…
**Trask Stalnaker (Microsoft Corporation)** 27:42 God.
Yeah, if you're interest… if you're interested in this, you could look at, the conformance repo we have. I've just merged the Java HTTP libraries conformance tests.
But we haven't done the AI. Java does have a few AI GenAI instrumentations that we would want to land there.
ping me on Slack if you happen to start working on, that, so that… because I might… Prompt something at some point, but that's not on my… current list.
**Iwa Wong** 28:25 Yeah, sounds good. I'll sync you off, Slack.
**Liudmila Molkova** 28:35 Okay, awesome. Oh, by the way, Steve, the blog, mentions… The… that you folks have your own confirmments repo?
**Would you… Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 28:52 No. Yeah, we don't have our… We don't public our own, conformance, report.
So far.
**Liudmila Molkova** 29:03 Okay. Would you be interested in contributing your… the conformance for your instrumentations here?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 29:11 Yeah, sure, sure, maybe I can discard with a folk who is doing something in this field, and I will discard with him later.
Yeah, maybe Zhiming is responsible for this part, yeah. He also created an issue to contribute some long suite instrumentation to, Python GenI repository.
**Liudmila Molkova** 29:41 Yeah, I think that we have now… we have merged this one, and even released it last week, and I think there are a couple more on the way, so, it's just, like, for those that are not yet… you didn't contribute to OpenTelemetry yet, it would be nice to see them here, because For Lopania, let's say we have pretty… quite a few instrumentations here, and, like, the long suit could be another one of them, and actually, this is maybe how we decide if instrumentation is… like, we can detect the gaps based on just the… the coverage reporting.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 30:20 Okay, yeah.
**Liudmila Molkova** 30:25 Awesome. So, Dan, that's… we're at the time for our first morning call.
If you're joining in hour and a half, see you there… sorry, in an hour. See you… see you there.
If not, see you next week, and around in the community. Thanks for coming, great to meet you, Eva and Jeremy.
**Neil Yashinsky** 30:46 Same. Yeah, thanks. Bye.
**Iwa Wong** 30:48 Yeah, buddy.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 30:49 Do you?
