SIG: Developer Experience SIG Meeting
Date: 2026-07-08
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Perk (Marcin Stożek) | Elastic Ingest** 02:07 Hey, hey.
**Fabrizia Rossano** 02:09 Hi.
**Perk (Marcin Stożek) | Elastic Ingest** 02:10 Good to see you.
I think we've met, like, a month ago?
**Fabrizia Rossano** 02:16 Yes.
Then I was here a couple of weeks ago, but there was no one.
And last week I was off.
So I'm back.
**Perk (Marcin Stożek) | Elastic Ingest** 02:33 Okay. Nice to meet you. Where are you coming from? Where do you work? What do you do?
**Fabrizia Rossano** 02:37 I work in Grafana. I'm a product manager and I work on developer experience.
Inside Grafana. Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 02:46 Oh, nice. Okay, so I'm Perk. I work at Elastic and I'm a product manager for Ingest, really. Everything Ingest, so OpenTelemetry and everything else.
**Fabrizia Rossano** 02:56 Nice. To product manager.
**Perk (Marcin Stożek) | Elastic Ingest** 03:00 Yes, yes, yes, yes, yes. I think we're going to work on getting the word out.
**Fabrizia Rossano** 03:06 Yeah, sure.
**Perk (Marcin Stożek) | Elastic Ingest** 03:07 People for people to to.
To know how to use OpenTelemetry and, like, what it provides and what.
**Fabrizia Rossano** 03:15 Yeah, I was looking actually at the proposal.
of… Things that we could do?
They're really interesting. I have another one that I wanted to add.
That is, I tried to instrument, like, to work on the demo.
**Perk (Marcin Stożek) | Elastic Ingest** 03:35 Mmh.
**Fabrizia Rossano** 03:35 without using LLMs.
And it's been.
**Perk (Marcin Stożek) | Elastic Ingest** 03:40 What does it mean?
**Fabrizia Rossano** 03:42 Like, you know, you could do the hotel demo and ask an LLM to help you instrument and check.
**Perk (Marcin Stożek) | Elastic Ingest** 03:47 Oh, nice.
**Fabrizia Rossano** 03:48 Prerequisite, right? So I tried without, and then I tried with. And one thing that I know this could help would be some sort of checklist of all the things you need to have installed locally.
like, Python, and Go, and this, and this, and this, because if you don't have that, it tries, and then it's a blocker, and then you need to install.
**Perk (Marcin Stożek) | Elastic Ingest** 04:12 Oh.
**Fabrizia Rossano** 04:12 Sure. And I was thinking, if we have a sort of script or something that could like just help check your PC if all the.
**Perk (Marcin Stożek) | Elastic Ingest** 04:24 Mmh.
**Fabrizia Rossano** 04:25 Are there?
I'm like, people would try the demo much more.
**Perk (Marcin Stożek) | Elastic Ingest** 04:31 Probably. Yeah, yeah, yeah, yeah, yeah. I'm with you. I'm with you. Well, definitely.
**Fabrizia Rossano** 04:37 It fits in the developer experience, because I'm a developer, I want to try this, and then it takes me 4 hours, and I'm never gonna do this. Yeah. But if it takes me half an hour.
I'm gonna do it.
**Perk (Marcin Stożek) | Elastic Ingest** 04:50 Yeah, yeah, yeah, yeah, yeah, definitely. Well, yeah, the only problem is that with those prerequisites, ideally you install them as well, but you never know, you know, what is the environment that is going to use, right?
**Fabrizia Rossano** 05:03 Maybe… maybe they… It just checks your environment.
Flex your environment, checks what's missing against these prerequisites, and then.
Those are all the things you need to install. If you're on a Mac, you can brew them. If you're on a Linux, you can do this. If you're this.
**Perk (Marcin Stożek) | Elastic Ingest** 05:18 Oh, yeah, yeah, yeah. Like with the copy and paste commands. Yeah, yeah, yeah. I think that will work. Defin.
**Fabrizia Rossano** 05:24 So that's on my list. What this is a proposal in the proposal of things we could do as this group.
**Perk (Marcin Stożek) | Elastic Ingest** 05:32 Is it somewhere,
**Fabrizia Rossano** 05:34 I don't.
**Perk (Marcin Stożek) | Elastic Ingest** 05:34 It'.
**Fabrizia Rossano** 05:35 in this. Here's the document. That's this one.
That's the meeting notes.
And I haven't documented it yet, but I see there are some… proposals for things we could do.
To improve the developer experience.
**Perk (Marcin Stożek) | Elastic Ingest** 05:55 Hmm.
**Fabrizia Rossano** 05:57 I like the trace verbosity level one that's been put in here. Do you want me to share the screen or are you seeing?
**Perk (Marcin Stożek) | Elastic Ingest** 06:04 Yes, please do. Yeah, yeah, yeah, yeah. Yeah!
That will be easier, I think.
**Fabrizia Rossano** 06:10 Yeah, so.
**Perk (Marcin Stożek) | Elastic Ingest** 06:12 Is anyone… Watches the recording afterwards.
**Fabrizia Rossano** 06:16 Yep.
So, there are two proposals now, that is, the documentation templates.
and the trace verbosity.
I really like the trace verbosity. I need to add another proposal here. for what I just said, like making it easier to onboard.
On the… OpenTelemetry dem Like, how can we reduce The time to run?
**Perk (Marcin Stożek) | Elastic Ingest** 06:50 Mmh.
**Fabrizia Rossano** 06:50 Telemetry demo to the bare minimum, like, 30 minutes.
**Perk (Marcin Stożek) | Elastic Ingest** 06:53 Yeah, yeah.
**Fabrizia Rossano** 06:54 One hour. Okay.
Something that people can time box.
**Perk (Marcin Stożek) | Elastic Ingest** 06:58 Definitely. Okay. So, so the idea is that you will add it in here as a, as a, as a, as a tab for review. Yeah.
**Fabrizia Rossano** 07:05 We can discuss it next week, maybe.
**Perk (Marcin Stożek) | Elastic Ingest** 07:08 Cool. Yeah, I will.
**Fabrizia Rossano** 07:09 Two more people.
**Perk (Marcin Stożek) | Elastic Ingest** 07:11 I also just posted the, we did the interview with Keycloak, maintainers.
**Fabrizia Rossano** 07:16 Peace.
**Perk (Marcin Stożek) | Elastic Ingest** 07:17 I think back in April, and I have a draft of the blog post.
Now, I just posted it on Slack.
**Fabrizia Rossano** 07:27 So… Perk (Marcin Stożek) | Elastic Ingest 07:27 If you would like, if you would like to review it as well, that would be great, and I would need to add you.
Because I do it by email.
**Fabrizia Rossano** 07:38 Yes, you do it by email. My mail is from… fabrizia.rosano at grafana.com. It should be in the calendar event.
**Perk (Marcin Stożek) | Elastic Ingest** 07:48 Maybe let's put it here. I put it like that.
And…
**Fabrizia Rossano** 07:52 I'm gonna add mine.
**Perk (Marcin Stożek) | Elastic Ingest** 07:54 Oh, that would be helpful, yeah.
**Fabrizia Rossano** 07:57 Oops.
Sorry.
**Perk (Marcin Stożek) | Elastic Ingest** 08:01 Auto demo… Alright, alright, please.
**Fabrizia Rossano** 08:12 Okay.
I have a question on the blog post, because a few Weeks ago… We talked about the fact that, There's also a blueprint effort that's been done by a different Sikh.
Yeah. That overlaps with the blog post, and they are using some of the blog posts to create blueprints.
I don't think you were in this call, but apparently, like, apparently, like, there was a discussion on the fact that let me find the blueprints.
I think it wasn't happening here.
8:27, I think.
Yes, on May 27. So there is this one.
That's the reference implementation.
And, see, the Skyscanner one, I think, was taken from the Skyscanner blog post.
But it's different, because It.
explain the implementation.
**Perk (Marcin Stożek) | Elastic Ingest** 09:45 Mmhm.
**Fabrizia Rossano** 09:46 But I don't think it's much different from the blog post. So Joanna.
Suggested.
To get in contact.
with the hotel blueprints group, and see if we could collaborate into transforming more blog posts into blueprints.
**Perk (Marcin Stożek) | Elastic Ingest** 10:07 Oh, okay, with the transpiling.
I…
**Fabrizia Rossano** 10:11 Don't know how.
**Perk (Marcin Stożek) | Elastic Ingest** 10:12 Well, because… okay, okay, okay, that makes sense.
Maybe we should discuss that next week.
**Fabrizia Rossano** 10:19 Yeah, ma'.
**Perk (Marcin Stożek) | Elastic Ingest** 10:19 Are they the same? I feel they are a little bit different.
**Fabrizia Rossano** 10:23 They are a little bit safe.
**Perk (Marcin Stożek) | Elastic Ingest** 10:24 Sure, shorter.
**Fabrizia Rossano** 10:26 They are a little bit different, but a lot of what they put in the blueprints. It's kind of a subset of the things that we have in the blog post.
But they are a quicker reference if you just want to look at implementation.
**Perk (Marcin Stożek) | Elastic Ingest** 10:44 Yeah, yeah, for me, you know, like, Blueprint doesn't have a narrative and anything.
**Fabrizia Rossano** 10:50 No, I know I know I'm not saying it's the same. What I'm saying is, they've been using the blog post.
to then extract blueprints.
**Perk (Marcin Stożek) | Elastic Ingest** 11:03 Mmhm I think, yeah, I think that might work.
**Fabrizia Rossano** 11:06 Okay.
**So, if we are… Perk (Marcin Stożek) | Elastic Ingest** 11:09 Yeah, for some. That depends who are we talking with, because, for example, like.
Maybe this could, like for the Keycloak specifically, we discussed how another open source project can use OpenTelemetry. So maybe we could have a blueprint for another open source project. Well, okay, fair enough.
Fair enough. But then every opens… like, technically speaking, those projects will be so different that I'm not sure whether that will work for everybody, you know?
**Fabrizia Rossano** 11:37 Yeah, I know, but maybe there's some sort of over… like, we can investigate where there is an overlap, so… Perk (Marcin Stożek) | Elastic Ingest 11:45 Oh, definitely.
**Fabrizia Rossano** 11:46 They already have, like we could give them some materials to speed up.
the blueprint projects, and they don't have to go and re-interview or recheck those things.
**Perk (Marcin Stożek) | Elastic Ingest** 11:57 Yeah, yeah, yeah, yeah, yeah.
Okay, okay, yeah, that sounds good. Okay, I think we… So I propose to discuss this next week.
**Fabrizia Rossano** 12:08 Yeah, okay, I'll put it here.
discussions.
Okay, cool. I review the blog post. If you don't have a much to discuss. Since I have this hour set for hotel, I can do it now.
if you want, like, we close this call, and I'll go and read the blog post.
**Perk (Marcin Stożek) | Elastic Ingest** 12:52 Yeah, yeah, yeah, yeah. And this is just a first, first draft. So, you know, like.
**Fabrizia Rossano** 12:57 No.
**Perk (Marcin Stożek) | Elastic Ingest** 12:57 Whatever you have any comments with regarding to, you know, this flow and how it reads and the wording and everything, like I'm open to that. Great. That would be helpful. Thank you very much. Thanks. Awesome.
**Fabrizia Rossano** 13:09 Thank you very much. Talk soon and see you next week. Bye.
