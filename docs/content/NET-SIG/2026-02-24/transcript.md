SIG: .NET SIG
Date: 2026-02-24
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Matthew Hensley / Grafana Labs** 02:55 Hello, just gonna wait a few more minutes and see if anyone else is going to join us this week.
**Vanshika Navya** 03:01 Bye.
**Matthew Hensley / Grafana Labs** 03:01 Hi, Matthew.
There we go, Alvin just joined.
**Alan West** 03:10 Hey, friends.
How are you?
**Matthew Hensley / Grafana Labs** 03:12 Hello.
**Alan West** 03:16 Well, let's just wait another couple minutes or so. I haven't heard…
from Raj to indicate that he's not gonna be here, so…
**Matthew Hensley / Grafana Labs** 03:38 And Martin's out of office this week.
Which I'm… Pretty sure it was covered last time, just in case.
**Alan West** 03:45 Gotcha.
Well, it might be a small meeting, so…
I suppose I can share my screen, but… I don't… Personally have any agenda.
For today, and Sheika, you, I think you're new here, or have you attended this meeting before?
**Vanshika Navya** 05:36 Yeah, I attended last week, and I'm quite new, I've just started contributing.
**Alan West** 05:41 Oh, okay, great, welcome.
I can add your name to the,
Who are you with, or which company do you work for?
**Vanshika Navya** 06:02 I work for latex.
**Alan West** 06:07 Latex?
**Vanshika Navya** 06:09 Yeah.
**Alan West** 06:11 Gotcha.
What do they do?
**Vanshika Navya** 06:13 Okay, so it's a video telemetics solution company.
**Alan West** 06:20 Gotcha.
Cool. And what brings you to Opentelemetry.net?
**Vanshika Navya** 06:27 Yeah, so I work with .NET, and I just wanted to explore open source. And, yeah, I was quite bored at work.
And I wanted to, like, see how frameworks are developed.
**Alan West** 06:42 Oh, okay.
**Vanshika Navya** 06:43 Yeah.
**Alan West** 06:44 Cool.
That's great.
Do either of you have anything that you'd like to discuss today, agenda-wise?
**Vanshika Navya** 06:54 I just wanted to, since I've just started contributing, and I have only one PR merged, I would like to know how to, like, prioritize the kind of work, like, what, issue should I
pickup.
Any priorities that you are… you guys have?
**Alan West** 07:16 I am not,
super in tune with what, various open issues we have, but that's where I would start if I were you.
You know, we…
**Vanshika Navya** 07:35 Yeah, I went through the open issues, but I wanted to know, like, I went through the issues that are labeled Help Wanted.
**Alan West** 07:43 Dammit.
**Vanshika Navya** 07:44 picked up a few, so right now I'm working on expanding test coverage of baggage encoding. But then, like, CJO said that we are, like, you guys are planning to…
remove propagator-related code from the repository. So I just wanted to know, like, is there any area that you guys are focusing on right now? Like, the areas that are a priority right now, so that I can pick up issues that are related to those areas and work on them?
**Alan West** 08:16 In the main repo here, we don't have,
any big areas that we're tackling right now. We're gonna start looking at logs here soon, but that really requires a lot of planning first before we have any sense of, like, you know.
we've not broken it down into, you know, work and so on. If you wanted to begin familiarizing yourself with our log support and whatnot.
That wouldn't be a bad thing to do. But…
The other potential for contribution is,
the contrib repository, are you familiar with that?
**Vanshika Navya** 08:56 No. I'm not explored yet.
**Alan West** 08:59 Yeah, so we also have this contribrib repository here, which essentially has all the instrumentation of it.
The community has developed.
I would look over issues here as well, to see, whether there are things that, you want to tackle.
I mean… I've not been tracking the issues super closely, but…
There are a number that have been…
opened in the recent few weeks. Like, if you… just even, even…
Digging into the issues and identifying whether they're actual legit bugs, you know, that type of work is very helpful to us as well.
Here's a bug I actually opened up a couple of weeks back, that, I haven't had the time to address yet.
But, would like to see fixed.
of… So, there's… things like that.
coding.
What's that?
**Vanshika Navya** 10:05 Yeah, the bug that you mentioned right now, what is the issue number?
**Alan West** 10:12 3862.
**Vanshika Navya** 10:14 Okay, 3862, right? I'll have a look.
**Alan West** 10:17 Yep.
Yeah, you're welcome to take a look at that one. But, you know, as you see, there's… there's things that are marked Help Wanted, in this repository as well, so you might take a look over.
Those.
2.
**Vanshika Navya** 10:36 And in case I need any help, like, can I, drop a message in the group, or shall I reach out personally, or shall I communicate through the comments, PR comments?
**Alan West** 10:48 Yeah, PR, opening a PR, and, and…
Working that way is always good, and we can just…
go back and forth on the PR itself. If you have any other questions, kind of beyond the PR, you're welcome to
Hit us up in the Opentelemetry.net Slack channel.
**Vanshika Navya** 11:10 Yeah, okay, I have shown that one.
**Alan West** 11:12 Yeah.
So…
But yeah, if you have code or whatever that you… even if you just open up a draft PR, you know, sometimes that's the…
Easiest way to have a conversation, if you…
Have done a little bit of work, but you don't quite know
where to go, you know, opening a PR, opening a draft PR, or whatever, however you want to do it.
Is a good way to… for us to collaborate as well.
**Vanshika Navya** 11:42 Okay.
**Alan West** 11:50 Cool.
**Matthew Hensley / Grafana Labs** 11:56 I don't really have anything, besides… it's actually kind of a similar question about priorities. Didn't know if we wanted to contribute anything to the hotel roadmap.
It's being collected for 2026.
**Alan West** 12:14 Well, as…
as a group here, I mean, I guess there's a few things in 2026. Actually, I probably should have mentioned that the RPC instrumentation needs some attention, right? Those… those semantic conventions are…
In, Release Candidate now.
**Matthew Hensley / Grafana Labs** 12:36 Yep.
**Alan West** 12:37 And we've… Not… I don't know if anybody has picked up that yet, do you?
**Matthew Hensley / Grafana Labs** 12:44 Yeah, I'm working on WCF.
**Alan West** 12:47 Oh, okay, WCF, and then, of course, there's, the GRPC instrumentation as well.
So…
That's a big thing that's happened in 2026, right? The stabilization of those conventions.
What else might you be thinking?
**Matthew Hensley / Grafana Labs** 13:06 Declarative config. I know the zero code group has an implementation
And has been trying to upstream changes to the YAML.NET library and such.
But, obviously, that needs to come to the full SDK at some point.
**Alan West** 13:24 Yeah, I was kind of hoping that the work that they were doing there would ultimately B.
Incorporated into the SDK.
Have you been following that work much?
**Matthew Hensley / Grafana Labs** 13:35 Yeah, it's kinda… Yeah, it's… Fairly done for some… It has, like.
basic coverage of declarative config stuff, but I… Don't think it integrates,
In a way that would be really easy for us right now.
So, I think there's probably something to be figured out there, and they've had to vendor YAML.net
Because it turns out that's not fully Net Framework compatible.
So there's… it's a whole thing to…
I think really get it done.
**Alan West** 14:15 Gotcha. Are there… is that something you're going to be working on, or are you looking to work on?
**Matthew Hensley / Grafana Labs** 14:19 No, it's just…
Coming up, I don't have any plans to work on it in the next few months.
**Alan West** 14:27 But it's…
**Matthew Hensley / Grafana Labs** 14:29 obviously something that's… I think, might end up with .NET behind on, declarative config. I think it's… implementations are progressing a little bit quicker for the other runtimes.
**Alan West** 14:42 Yeah. Yeah, short of actual people, like, you know, that have the bandwidth to pick up these things, I can't really comment on, you know, what this community's gonna do with respect to…
you know, those types of things that are kind of, like, on the… in the forefront of the community's mind for 2026. Until we kind of get people the bandwidth to do that, I guess I'd probably say, like, I don't know. I don't know if we're gonna get there or not.
**Matthew Hensley / Grafana Labs** 15:09 I think, I had the same concern, and I have not…
Done too much as far as pushing for a roadmap.
I didn't know if we might want to go the other direction and just have the high-level list of things that we know need doing, and whether or not there's people for it. So if someone wanted to come along and pick up something.
Like, logs is very complex and requires a lot of design.
But just knowing that that's even on the table.
Might be interesting to mark down.
**Alan West** 15:42 Would something like that help, someone like you justify Spending time.
**Matthew Hensley / Grafana Labs** 15:50 Oh, yeah. No, it's kind of knowing the… what initiatives there are, and…
You know, things to implement, basically, at a high level, and that makes it easier for me to put it down on work for a quarter, for sure.
**Alan West** 16:08 Okay.
Yeah, I mean, I don't disagree, yeah. Those are good ideas.
**Matthew Hensley / Grafana Labs** 16:22 Let's just put it on the agenda for next meeting, and see how many people we get, and can start figuring out if anyone else is interested in that, even.
**Alan West** 16:33 Sure, yeah.
get a sense for people's bandwidth. Yeah, that's one thing I just don't have a great sense of, is, you know, who we got, and who has the bandwidth to kind of move some of these things forward.
So with more people, that would be…
That would be helpful. My impression is, is that,
Martin and, some of the folks from Splunk, Peter, and some… some of the other folks working on the no-code stuff.
Have had more bandwidth, so we can kind of get a sense for what they're thinking.
And, yeah, maybe, maybe get some interest.
**Matthew Hensley / Grafana Labs** 17:19 Well, I'll just add it to the agenda for next time, and…
Martin, I think we'll be back for the next meeting, and maybe we even have a Raj.
**Alan West** 17:29 Yeah, sounds good.
Alright, y'all.
**Matthew Hensley / Grafana Labs** 17:32 What?
**Alan West** 17:33 Thanks. Okay, thanks for the chat.
See you soon.
**Matthew Hensley / Grafana Labs** 17:39 See ya.
