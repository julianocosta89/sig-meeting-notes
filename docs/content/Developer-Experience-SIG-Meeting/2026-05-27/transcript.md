SIG: Developer Experience SIG Meeting
Date: 2026-05-27
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Dhruv Ahuja** 00:17 Hello.
**Fabrizia Rossano** 00:19 Hello!
**Johanna Öjeling** 00:28 Yay!
**Dhruv Ahuja** 00:31 Hi, hello.
**Johanna Öjeling** 00:33 Bye! Nice to meet you.
**Dhruv Ahuja** 00:36 Yeah, nice to meet you on.
**Juliano Costa | Datadog** 00:45 Should we… get started?
**Fabrizia Rossano** 00:51 Yeah.
**Juliano Costa | Datadog** 00:52 Cool.
**Fabrizia Rossano** 00:53 This is the first time I joined, so I'm gonna be mostly listening shadowing. I've talked with Joanna, because I work with her, and because I'm interested in the whole DevEx. My name is Fabrizia, I'm a product manager at Grafana.
So, just to set the scene of me being here for the first time.
**Juliano Costa | Datadog** 01:18 Great to have you.
**Johanna Öjeling** 01:19 Sure enough.
**Juliano Costa | Datadog** 01:20 Yep, and welcome to the SIG meeting. Thank you.
Hope to see you more, more, often here.
**Fabrizia Rossano** 01:30 That's my intention. I had something to close up.
For the Grafana 13 release and follow up, but, now I've cleared my schedule, so I can join this meeting every week.
**Juliano Costa | Datadog** 01:46 Awesome.
And, so let me, let me introduce myself. I think you know Johanna, and then we can maybe… Johanna, maybe you can say hi also to, Will I pronounce your name correctly, Dhruv?
**Dhruv Ahuja** 02:05 Yeah, poof, yeah.
**Juliano Costa | Datadog** 02:07 Okay, awesome. So, hi, I'm Giuliano, I am a developer advocate at Datadog.
A maintainer on the OpenTelem3 demo.
And I've been involved in the developer experience SIG since the beginning of it.
With Tristan and Damien. Damien actually left this… this SIG, to focus on other parts of the project, and then, Johanna was also onboarded to, to the project, so, Johanna, myself, and Tristan, that is not feeling well today, are the… kind of maintainers of this project to run and discuss what we're gonna do next.
And… yeah.
Yep.
**Fabrizia Rossano** 02:55 Thanks.
**Juliano Costa | Datadog** 02:56 That's me.
**Johanna Öjeling** 02:58 Thanks, Juliano. Yeah, hi, I'm Liana. I'm a Senior Software Engineer at Grafana Labs.
And I joined this SIG about 6 months ago, I think, and I've been working mostly on the blog post series so far.
And within hotel, I'm also familiar with Opband, and worked on the collector on Trib. Yeah, I actually posted an update to the agenda, because I'm changing jobs.
And my last day at Grafana will be next Friday, and then I take something to do, and I join IKEA in July.
But yeah, I'll try to still make it to this meeting, if I'm on video, but I might miss some occasion, in June, so yeah, I'll keep you posted.
**Perk (Marcin Stożek) | Elastic Ingest** 03:52 Congratulations, Johanavan.
**Johanna Öjeling** 03:53 Oh, cute.
Thanks.
**Juliano Costa | Datadog** 03:57 is, is IKEA using OpenTelemetry?
**Johanna Öjeling** 04:03 They are, they have said that they would like to explore it. They're not big until users today, and different departments and different, like, companies of IKEA have different setups. But yeah, for sure, the people I've spoken to, they, they like, hotel, So yeah, let's see if, if I get to introduce it, though.
**Perk (Marcin Stożek) | Elastic Ingest** 04:32 But they will know, not what you're saying.
**Johanna Öjeling** 04:34 Yeah, yeah. Exactly.
**Juliano Costa | Datadog** 04:38 Awesome.
**Dhruv Ahuja** 04:41 Yeah, so…
**Juliano Costa | Datadog** 04:41 And…
**Dhruv Ahuja** 04:42 I'll introduce myself as well.
Yeah, so hi everyone, I'm Dhruv. I'm currently working as a DevRel at Cygnos, an up-and-coming hotel vendor.
Yeah, so I mainly transitioned to DevRel about 6 or so months back.
And, yeah, I might not be able to join this meeting frequently. I would definitely love to, because this falls, this is 2.30 for me, so working hours.
So, yeah, and today I have a topic to discuss so specifically, but I would definitely try to join meetings when and where possible. And I only recently started attending the SIG meetings.
So, I've been working, on OTEL6 for about one and a half weeks, mainly on the contributor experience side, and somewhat on the end-user SIG as well.
Yeah, glad to make an acquaintance.
**Juliano Costa | Datadog** 05:36 Awesome.
Awesome. Yeah, so, I don't know if everyone saw, but, Dhruv has, shared a message on, on Slack.
Saying that he, had an idea of a blog post on… or a potential blog post involving GenAI libraries.
And, I briefly invited him to join the call and, yeah, share that with us.
Before we… Before we actually jump to that, let me just take… I… But if you just… Update one thing here on the… on the… On the meeting notes, and get some updates on the ongoing work.
Or the blog post that we have.
I… Johanna, did you hear back from, Vidya? Would you… I don't know if she shared… she… if she shared something with you?
**Johanna Öjeling** 06:48 No, and I actually emailed them again yesterday to follow up, because, yeah, I'm waiting.
For them to either approve or, yeah, so, no update on Croc.
**Juliano Costa | Datadog** 07:05 Okay, so that's Grok. Grok… No fake.
**Johanna Öjeling** 07:08 Yeah, or a Grok NVIDIA, it's… yeah.
**Juliano Costa | Datadog** 07:12 And, no, what I mean is, the name of the person, from the Atlassian blog.
**Johanna Öjeling** 07:20 -
**Juliano Costa | Datadog** 07:21 I think… yeah, I'm not sure, again, how to pronounce the name, but…
**Johanna Öjeling** 07:26 Yeah, you're permanent.
**Juliano Costa | Datadog** 07:27 She… she shared a Google Doc with you?
Because if you're going on PTO, maybe you could, include myself, Bar.
Trust me.
**Johanna Öjeling** 07:38 Yeah, no, she didn't, I shared the Google Doc with her.
**Juliano Costa | Datadog** 07:43 Okay.
**Johanna Öjeling** 07:44 the common one. So she has started to write in the Atlassian tab.
But yeah, she hasn't shared anything else with me, so…
**Juliano Costa | Datadog** 07:58 I see, I see, okay. So, there it is here. Okay, I see the… The blog post now.
I will… Fabrizia, do you mind, sending me your email on Slack, or the CNCI?
**Fabrizia Rossano** 08:16 I'll send it.
**Juliano Costa | Datadog** 08:16 Or… or here, yeah.
**Fabrizia Rossano** 08:18 No, no.
**Juliano Costa | Datadog** 08:20 And I can invite you to the… to the dock.
**Fabrizia Rossano** 08:24 Great.
**Juliano Costa | Datadog** 08:25 We… just so you know, we have interviewed a couple of folks and a couple of companies. That's how we started this series of blog posts that Johanna mentioned before.
These stories… And the blog posts are not in a public doc, because it… sometimes they need to remove things that they are, that we are, mentioning on the doc, so we decided to move into a private doc, have a draft, then they approve or not, and then we move to the, to GitHub, and then to the official process of publishing it.
Oops.
Just so you know.
**Fabrizia Rossano** 09:06 Okay, and if you need any help reviewing the docs, or… like, just add me to the docs, and I can go in, make edits, like, help with that. I've, collaborated to… like, I write a lot of blog posts.
for the Grafana, so I kind of know how the process works. I'm also pretty familiar with using GitHub or anything, so… I'm a product manager, but I can use all the tools without any problem.
**Johanna Öjeling** 09:40 That's great. Cool. Take care.
**Juliano Costa | Datadog** 09:42 And then, Perek, do you have any updates on the Kiko? .
**Perk (Marcin Stożek) | Elastic Ingest** 09:50 the only update I have so far is that I've started writing this. I have a sketch, that I don't like, unfortunately, I have to write it once again, you know, but it's… it's there, it's happening, I… like, I'm still, you know, like, on top of it. Just nothing to share, unfortunately, just yet.
**Juliano Costa | Datadog** 10:09 Okay.
**Perk (Marcin Stożek) | Elastic Ingest** 10:11 Time-wise, time-wise, yeah, fair, fair, fair enough. Time-wise, I just want to ask you, because, I have a quite, what to say, like, packed… packed timing right now, you know? Like, company-wise and whatnot, lots of things are happening.
Is there any timeline in your heads, guys? Or is it okay for me to say that, you know, like, mid, like, second half of the June, to share something, and then, you know, we can go forward? Is that fair to ask for that?
**Juliano Costa | Datadog** 10:40 I… I don't have any stress on that, Johanna, do you have…
**Johanna Öjeling** 10:44 No, yeah, please, do it whenever you have capacity, but yeah.
the stress.
**Perk (Marcin Stożek) | Elastic Ingest** 10:50 There it is. Okay, thank you. So, just wanted to…
**Juliano Costa | Datadog** 10:53 Yeah, I know No, don't worry, and even if you, like, have for tomorrow, we can't publish… we don't choose the timeline on the blog post from OTAL itself.
Because they have a schedule, so no rush on that. Take care.
And it's, okay.
**Perk (Marcin Stożek) | Elastic Ingest** 11:11 Sure, sure, sure. That's fair enough. I just wanted to make sure that we are on the same page, because I totally understand that, you know, writing things and agreeing on a blog post is one thing, and then publishing is, like, yet another monster.
**Juliano Costa | Datadog** 11:25 Yep.
Cool. And, okay… So… Ruth, do you wanna share with us your, idea?
**Dhruv Ahuja** 11:46 Yeah, sure.
So, I was going through the, concept of open telemetry and LLM integration, right? And the kind of topics that are already there, and I noticed that we have an official blog post, which is from 2024.
So, I wanted to kind of write an update on that, which goes more into what is a more actionable item for a user. For example.
How do you… how does a span actually look like? Because, I noticed that the blog actually does not go deep into implementation detail as such. So, I wanted to make a demo application which uses OpenAI SDK, or the Agent's SDK.
instrument the application, and it… and I don't want it to be just a trivial application where we have a single endpoint, but more of a… maybe showcase how you can build maybe a markdown or something out of it by calling an API, and then maybe even query it. So I'm still finalizing the implementation and the ideas myself.
But I… I saw that it's 2026, the blog post was from 2024, so I definitely feel that a follow-up would be good for the community.
And then show.
**Juliano Costa | Datadog** 12:53 I assume.
**Dhruv Ahuja** 12:54 what that… what those details actually look like in TraceView, and what the user… any user who is coming today to observe their open telemetry, observe their LLM-based applications, what they should expect from OpenTelemetry.
But the concern that I have is, I had started on that, but the concern I have is that the agent's SDK, right, I believe we are in the middle of migration to a dedicated repository.
And as part of that, the, for example, the OpenAI Agents SDK, which has, I think, 20,000 plus GitHub stars, so it has a lot of traction.
But the SDK was last published in 2025, the version 0.1, so it has not yet been updated until thus far, so it still works fine, but there are a couple of spans that have unknown as the name.
But a lot of the details are fine, and I think that can be a good starting point for any developer as well, because everyone knows that GenAI is a developing space, right? And that things are underway, things are progressing.
So, but the unknown might be a bit jarring for a reader who is reading an official OpenTelemetry blog. So, I then tried out the OpenAI SDK, which is the OpenAI Python library, the more commonly known one.
But there as well, I noticed that we currently only support the chat completion API, which OpenAI is kind of phasing out in favor of the Responses API. So, the instrumentation for Responses API has been merged, but that is not live yet.
So, and responses, and the concern with the chat completion API is that you have to dedicate… you have to switch to a dedicated model for something like a web search API call.
Which is somewhat of a blocker, because I wanted to gather info from the internet and showcase how the SDK can make a report for you, and then you can follow up with questions on that.
So, kind of like a real-life use case, so the user can actually see what kind of an impact total has on their real-life application.
So, I wanted to know whether I should park it for now and wait for the implementation to mature a bit, and then work on it?
**Juliano Costa | Datadog** 15:11 I believe, so, like, when I say, I believe, I think it's clear that it's my opinion.
**Dhruv Ahuja** 15:24 Yeah.
**Juliano Costa | Datadog** 15:24 I believe that this would be better if we discussed with the GenAI folks. So there are two channels that I would point you to. One is the hotel GenAI instrumentation.
And the other one is the hotel, Python.
So those… those are the two ones that I would, try to join the SIG and discuss this same idea that you shared with them, and then, like, how to move on, and even do a blog post, because then you can, I would say, you can collaborate with the folks that are Responsible for the implementation.
In the… DevEx, what we try to do is to… focus on pain points of, users of OTEL.
So, I don't… I don't believe… I mean, it… in the end, everything fits the developer experience, but I don't think this specific one would be, I don't think anyone here is the SME for that, and if you discuss that with the folks that are working on the implementation, I think the result and the quality of your blog post would be better.
And…
**Dhruv Ahuja** 16:45 Right, makes…
**Juliano Costa | Datadog** 16:46 With then, you would also have a better timing on, when to… to release, and when new release will come up, and everything, so…
**Dhruv Ahuja** 16:56 Got it. Yeah, I had actually posted in the, GenAI channel, and one person, I believe, had replied as well, but nothing from the, I believe, the core developer team, so I'll try reposting the same message in OTLPython as well, and see where that goes. Yeah, I should have actually mentioned that initially.
Maybe that would help set the context more initially, yeah.
**Johanna Öjeling** 17:19 Did you, could you also share a link to the blog post you found from 2024? Sure. So you have an idea of what's already out there, and how you want to… Yeah. Improve it for the next one.
**Dhruv Ahuja** 17:33 chat.
I believe we have 3 total blog posts, covering this, the topic of LLM observability, Gen AI, and… such things.
I believe two were in 2024, and one was recently published in 2025 around the evolving standards.
Of genre.
**Juliano Costa | Datadog** 17:59 I'm actually, bumping a lot… I bumped a couple of times the Python folks.
To have a new release on the… on the GenAI Python instrumentation for OpenAI, because at the moment, they do not use the latest semantic conventions. So, all the semantic conventions that they are using are prior to 1.37, And, if you try to capture the messages and everything, like, from a chat, it doesn't work.
It is implemented, it's missing some parts, so I… I actually discussed, with some folks from Rafana, Lil Demila, I think she's involved with that, and Yeah, we still don't have the package released, so yeah.
**Dhruv Ahuja** 18:54 Yeah.
**Juliano Costa | Datadog** 18:55 And…
**Dhruv Ahuja** 18:55 And…
**Juliano Costa | Datadog** 18:56 Go ahead.
**Dhruv Ahuja** 18:56 Yeah, actually, funnily, the… so, I tried out the OpenAI Normal SDK as a workaround, right? And then I realized that Responses API can actually let you build kind of, like, an agent without a lot of, scaffolding required around it.
And finally, the release was on May 1, 2026, for the V2 version, and then they, I believe they started the migration onto a dedicated repository just for GenAI instrumentation libraries.
rather than the OpenTelemetry Python contrib path.
repo path, and the response is API instrumentation was merged on 13th May. So, even if that gets a patch release or something, I think that would just unblock me totally, because then I can just use that SDK instead of the agent's SDK.
So yeah, I'll definitely try pinging them. And it's a bit confusing as well, since the standards are changing, so it's like I'm just taking help of AI to guide me on what needs to be done, and then putting my own brain behind it.
**Juliano Costa | Datadog** 19:59 Yeah.
And of the other.
It's tricky because, like, if you want your agent to be Up-to-date, you usually point to the REPL, and then the agent can understand everything.
But then, the agent will reply to you, like, hey, it's simple, use this.
And then you use it, and it doesn't work, and then you check again with the agent, and he's like, yeah, actually, there was no release for that.
the code is there, but there was no release, so then you can't use whatever is on the REPU. And if you don't point to the REPU, then it's not even aware of those configs. So it's, yeah, I totally get your pain there.
**Dhruv Ahuja** 20:46 Yeah, and I think that's why this kind of a blog post becomes even more important, because I had read a customer or two saying something like that, and then I got the idea that, okay, maybe this is something… Which might be worth exploring, because I was a bit out of touch with it, and then when I… from the surface level, it seems that things might work. But you start the implementation, and you immediately… it's like you're working on eggshells, just because The space is developing, OpenTelemetry itself is evolving to better manage this, and we are bang in the middle of it right now.
**Juliano Costa | Datadog** 21:19 I will, I'll share with you something.
Sorry. I'll share with you something that is happening on the OpenTelemary demo at the same time, so maybe you can take a look.
Sorry.
There is a… Thank you. There is a PR that is currently on draft, it's… been open since March, and it's a long, ongoing discussion here.
But they are the, some folks… some folks from IBM, they are adding, agentic.
workflow to the OpenTelementary demo.
And… the… the… the… the changes that they have done is super cool, so basically you interact with an agent to do your shopping. I don't know if you have ever used a demo like this.
**Dhruv Ahuja** 22:26 shop.
**Juliano Costa | Datadog** 22:28 Yeah, so it's e-commerce, you go, click, click, click, done. But with the agentic workflow, you actually interact with the agent and say, hey, I want to buy, like, a telescope, whatever. And then the agent do the tool calls and everything, and then, adds the things to… like.
It does the shopping for you.
They presented that in a SIG meeting back in March, and then they started with this work. This is not merged yet, will be part of the demo eventually.
I just wanted to make you all aware of it, because then you may not even need to build the demo.
to showcase what you want to showcase, you could just use the hotel demo, and then talk about it, and how we do the instrumentation there, and everything.
**Dhruv Ahuja** 23:27 Yeah, makes sense, yeah.
**Juliano Costa | Datadog** 23:32 Cool.
Anything else?
**Dhruv Ahuja** 23:48 Yeah, I'm all good, yeah.
**Perk (Marcin Stożek) | Elastic Ingest** 23:55 I just wanted to give you a heads up on the… on the key lock, so that's why I joined today. So I'm good as well, thanks.
**Johanna Öjeling** 24:02 Almost a good…
**Juliano Costa | Datadog** 24:05 Awesome. So… Yeah, we had a to-do item for… From the previous call, about addressing the proposals on… That was it.
**Johanna Öjeling** 24:26 Yeah, the new idea.
**Juliano Costa | Datadog** 24:28 telemetry level and interview 6. I… yeah, I know that I… I was meant to talk about the telemetry level, but I… yeah, I didn't. So, yeah, I'll take that as a homework to me.
**Johanna Öjeling** 24:42 Yeah, and I will, I've been out on video also, so I'll continue with the documentation thing, and Tristan also wrote that he would try to… get the proposal for the SIG interviews done, and present next week. So, yeah, hopefully next meeting we can discuss the new initiatives.
**Juliano Costa | Datadog** 25:03 Awesome. Awesome.
**Fabrizia Rossano** 25:05 I'm at an off-site next week, so I'm not gonna be here, but I'm gonna read this. I'm particularly interested in the interviews.
So… that's something I'm pretty happy to run, if you need help with that, but.
**Juliano Costa | Datadog** 25:23 Yeah, so just to… to give you an update, Fabrizia, So, when we started the SEEK, we kind of, Set the goals of the… of what we wanted to do, and then we ran… End-user inter… end-user survey.
To kind of find out their pain points.
from the survey.
We were expecting one thing, like pain points on configuring SDK and interacting with the hotel API or whatever, but actually the… The 120 folks that replied, their main pain points were, like, Having real-life examples within the docs.
So, they said, hey, the docs are good to get started, but they lack, things like, how do I run a hotel collector in production? Or, like, how do I configure sampling and that stuff.
And then… We decided to do… to run those interviews with, different company sizes.
And then share those stories in the, in the hotel page as a blog post.
At the same time, they, the end user seeing started a project called What's it called, Johanna?
**Johanna Öjeling** 26:50 Yeah, the blueprint.
**Juliano Costa | Datadog** 26:50 blueprint.
**Johanna Öjeling** 26:51 Yes?
**Juliano Costa | Datadog** 26:52 Thank you.
So they started the hotel blueprint, which is kind of the same.
The difference is that we… In Deltaware space, we do not update blog posts, so once the blog post is published, I think we can fix minor stuff, but there are no major updates on it.
On the other hand, the Blueprints is meant to be a live document, where whenever there is a change, the company can come back to it and update, and then have that as a reference to users. So.
I think we're gonna talk with the companies that we interviewed to migrate their stories into the Blueprint format.
Or…
**Johanna Öjeling** 27:38 It has already… yeah, it has already been done, so they are added as reference implementation, so there are two parts. One is the blueprints, which is the, like, best practices and the living documents, and then We have the reference implementations, where company, organization, stories will be added.
And, so they just, like, copied the blog posts and reformatted the, like, intro and outro a bit, So, yeah, actually, our blog posts that we have published, they became the first reference implementation, so hopefully more will be added.
**Fabrizia Rossano** 28:21 Where can I find the link to this blueprint?
**Johanna Öjeling** 28:24 Yeah, that's fine.
**Fabrizia Rossano** 28:26 and…
**Johanna Öjeling** 28:26 Bing.
**Fabrizia Rossano** 28:27 treat them.
**Johanna Öjeling** 28:39 Okay, I'll post in the chat.
Okay, so I've seen the PR for the first blueprint, but it hasn't been… published yet. But yeah, there are 3 reference implementations.
Adobe, Mastodon, and Skyscanner.
**Fabrizia Rossano** 29:09 Just to give you context, I'm interested because I've, worked on several projects in different companies on making docs into actionable workflows for users, so I'm really keen to read it. If you don't mind, I might add some comments on it, because one thing I found really useful or we got feedback from users that was really useful, is having, and maybe it's already there, so I haven't seen it, having something at the beginning that explains who is the target user for that blueprint. So, like.
Read this blueprint if you are a medium-sized company with this setup that wants to achieve this goal.
And that avoids… People going through and midway realizing it's not for them.
And then, Start another one.
So… Maybe it's already there, but I'll give you the.
**Juliano Costa | Datadog** 30:17 I don't think so.
**Fabrizia Rossano** 30:19 Okay, I look at the code.
I think there will be a GitHub issue somewhere for this, so I'll, Possibly have a look and, introduce myself.
**Juliano Costa | Datadog** 30:33 Yeah, I think that would be a nice, suggestion to raise to the Hotel Blueprint folks. I think Danielle Gomez-Blanco is kind of the… the… the main person there. There are other folks in the SIG, but I think he was the one, like, driving, and… Trying to get this, rolling, so… I can… I'll actually share his name with you, honestly.
Okay.
**Fabrizia Rossano** 31:05 Thanks.
I'll join the channel, introduce myself, then, have a look.
**Juliano Costa | Datadog** 31:15 Cool.
**Fabrizia Rossano** 31:17 Thank you so much.
**Juliano Costa | Datadog** 31:18 Yeah, no worries, and also the… I sent to you Dan Gomez Blanco.
And, the channel, Hotel Blueprint.
And, so all of that to say that we kind of ended the interviews.
So, we won't run, at least as of now, we won't run any new interviews.
And we are… A couple of meetings back, we were discussing what we should do next, and then we, we came up with three… Proposals that we're gonna try to drive and see… What will actually be chosen or accepted, and then we just move on from there.
**Fabrizia Rossano** 32:12 Thank you for the update.
**Juliano Costa | Datadog** 32:18 Cool.
then, yeah, I think we can, wrap up. Johanna, is that your last one? So you're going on PTO for a while?
**Johanna Öjeling** 32:27 No, I work next week as well, yeah.
**Juliano Costa | Datadog** 32:31 Okay.
Cool.
So then, see you all next week.
**Perk (Marcin Stożek) | Elastic Ingest** 32:38 Yeah, next week.
**Fabrizia Rossano** 32:39 Okay.
**Johanna Öjeling** 32:40 Have a good day. Bye, bye.
**Fabrizia Rossano** 32:41 Thanks.
**Juliano Costa | Datadog** 32:41 Bye.
**Perk (Marcin Stożek) | Elastic Ingest** 32:42 Right?
