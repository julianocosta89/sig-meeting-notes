SIG: Go Compile Time Instrumentation SIG
Date: 2026-03-19
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/rPmz09MFB_7MnrXIVno4wQ2sGu63F4hhzUuDGKGoebG4TVGEDmgMZbrEA7rPqek.H0qsr8vDLslwONRV
============================================================

## Zoom Recording Transcript

**Marc Schäfer** 03:00 Hi.
**Przemek Delewski** 03:01 Oh.
**Marc Schäfer** 03:47 Will there be anyone else coming, or…
**Przemek Delewski** 03:51 I'm not sure, I'm just looking at the channel, and it seems that no one will join, probably.
And the meeting will be canceled, I think.
Okay… I haven't spoken.
**Marc Schäfer** 04:07 I'm… I'm new.
So it's my first time, it's my first time joining this kind of meeting.
**Przemek Delewski** 04:15 Yes, I know, because I haven't seen you before.
But it seems that, there will be only two of us.
Okay. Okay, so… Where are you based?
**Marc Schäfer** 04:33 I'm based in Germany.
**Przemek Delewski** 04:35 Okay.
**Marc Schäfer** 04:53 And what about the, meeting later this day? The Go one? The GoSig one?
**Przemek Delewski** 05:01 Yeah, I'm not sure, because I'm not attending this… the next meeting.
**Marc Schäfer** 05:05 Okay.
**Przemek Delewski** 05:06 I'm usually attending only this one.
So probably the Go one will be, you know, normally.
**Marc Schäfer** 05:16 Okay.
Normally, this one takes also… Normally plays, and it's not cancer at all.
**Przemek Delewski** 05:26 Yes, but we haven't had, this, Sikh meeting for a few weeks, I think, now. Oh, okay. Because there was no, Let's say, important, topics for the discussion. So, they were canceled.
But I was hoping that today will be, you know, we will have it normally.
Because there was a plan to make this meeting before the KubeCon.
And nobody joined, so… Yeah.
So, maybe… We can briefly discuss, we can talk a bit, what are we doing? So… Do you… are you a Go? Go developer?
**Marc Schäfer** 06:27 Yes, normally I'm a system administrator, but I started in IT with programming or developing code, but nowadays I'm at work, in my full-time job, I'm a system DevOps engineer.
**Przemek Delewski** 06:45 Okay.
**Marc Schäfer** 06:45 But I wanted to do more programming again, or going back to programming again, so I'm capable of Java and Go.
**Przemek Delewski** 06:55 Okay. And are you…
**Marc Schäfer** 06:57 So, yeah.
**Przemek Delewski** 06:58 Are you interested in this specific topic, due to your personal, I don't know, preference, or, you are also…
**Marc Schäfer** 07:07 both.
**Przemek Delewski** 07:08 Oh, okay.
**Marc Schäfer** 07:09 so I'm interested in open telemetry in general, because of personal projects, but also, open source projects I'm part of. For example, Pangolin, you maybe have heard of that.
And, also at work. So at work, we do use open telemetry quite heavily.
we don't have any Go application at work, we have only Java-based, Spring Boot, all that kind of stuff application, so nothing Go-related.
Besides… besides Kubernetes and all those applications that are run on, or, are written in Go, but, no self-developed applications that are written in Go. But, yeah.
**Przemek Delewski** 07:53 Okay, okay.
So this sick is about, you know, compile-time instrumentation, so basically we have a tool where we are injecting, you know, additional code, OpenTelemetry code, during the compilation, and this is based on some rules that we defined in YAML files. So, in YAML 5, for instance, you define that you would like to inject in this, and this function, for instance.
nth.
There are some other… Additional properties for that, and we also have, let's say, Instrumentations that will be then used, when you inject this code.
**Marc Schäfer** 08:35 Okay.
**Przemek Delewski** 08:35 to the application. And there is also another, you know, Go Auto Instrumentation Seek, which is based on eBPF instrumentation.
**Marc Schäfer** 08:45 Oh, okay.
**Przemek Delewski** 08:47 So, I was also… because at the beginning, I was… co-founder of… let's say both 6, because the one that was EBPF, in fact, it contained at the beginning these both kinds of instrumentations, so… But most people were interested at the time in eBPF, and there was, in fact, only maybe me and two, maybe, other people interested in compile time instrumentation at the time. And then the… last year, at the beginning of last year, this Sika was created.
So that's the new thing, and here all people, you know, are interested in compile time.
Instrumentation.
So, basically, that's… that's the history of… of the… Of the second… tooling around Go. But there are, you know, as you mentioned, there are also other 6, Go-related, but this is mostly, I think, about SDK, so… OpenTelemetry SDK for Go.
**Marc Schäfer** 10:04 Good to know. I did already some minor contributions, some cleanup, in a few of the OpenTelemetry projects.
some in the Java one, and recently some in the Go one, so…
**Przemek Delewski** 10:21 Oh, okay, okay.
**Marc Schäfer** 10:23 But not… not much, maybe total of… 300, 400 lines, few, few pull… well, I think total 3 pull requests or so, cleaning some, some, or closing some, or letting the maintainer, know that some of them can be closed.
Yep.
**Przemek Delewski** 10:43 Yeah, that's… that's great.
So, are you already a member of OpenTelemetry organization?
**Marc Schäfer** 10:50 Not a member, but a contributor.
So, not a member of the organization or so, yeah.
**Przemek Delewski** 10:58 Okay, okay.
Because I think, to become a member, you have to do some work, and as you mentioned, you already did some, you know, pull requests, so I think that's enough to become a member, also, and then… If you do more work, you can be promoted to, you know, something like a… Approver, or that there are… there are a few roles that… in the organization.
**Marc Schäfer** 11:29 Yeah, I'm happy to work my way up there, yeah?
Is there any documentation or specific steps? Because I looked at all the… the markdown files, the contribution guidelines, README and other stuff, there was no… cleared, maybe that's on purpose, but there was no clear way which steps needs to be done to become or to get more involved into the project than just creating pull requests and that stuff.
**Przemek Delewski** 12:12 Yeah, to be honest, I don't know if there is more documentation, but are you talking about this specific project, or in general?
**Marc Schäfer** 12:23 more… more… maybe more in general, because right now I don't even know which repository, or depends how they are connected to each other, that I want to work on or work with. That also depends on where it's possible for me to get in.
It's easier to get… it doesn't need to be easy, but not like taking 3 years or so.
to get, get involved, with, with every day, two hours of activity or so, because I'm doing that, privately, part-time, or besides my full-time work, so additionally on my 40 hours, of work per week, I'm doing that, so I have, like, 1 hour per day I could… Spent on a few… GitHub, or maybe 2 hours per day on a few GitHub projects, and one of them is then OpenTelemetry, or would be OpenTelemetry, and then the different projects or repositories for OpenTelemetry.
**Przemek Delewski** 13:26 Yeah, so, as I said, I'm not sure if there is some kind of documentation. Maybe there is, but you can also, there is a channel, Slack channel, Autel Maintainer, or something like that.
And, yeah, auto maintainers, and probably you can ask these questions there.
Okay.
**Marc Schäfer** 13:48 I still need to join Slack. I'm… maybe it's because of my work, but I'm not that used with Slack. It will be my first time with Slack.
So, at work, we don't use Slack, so until now, I have not come away, or at all in connection with Slack, or have touched Slack at all. So, that is on my to-do list. I just.
**Przemek Delewski** 14:12 Yeah.
**Marc Schäfer** 14:13 I just joined, I think I just joined, yes, no, not… Tuesday. Tuesday or Monday, I think it was Tuesday I joined, the, the Google groups and got invited into this, into the SIC calls here.
Yeah.
**Przemek Delewski** 14:29 Yeah, so, you know, the… all discussions around the open telemetry is… are in Slack, so probably… Yeah, yeah, for sure. I will join. Yep.
**Marc Schäfer** 14:42 It's just on my to-do list, and then I'm not, got to that point yet.
**Przemek Delewski** 14:48 Yep.
**Marc Schäfer** 14:48 So, I will do that today or tomorrow, so… and then I can… can ask that in the… Auto… how did you call that? Auto? What was the name?
**Przemek Delewski** 14:59 Auto instrumentation.
**Marc Schäfer** 15:00 or to, so the channel where I should write the…
**Przemek Delewski** 15:03 Sorry, the one about documentation.
**Marc Schäfer** 15:08 Yep.
**Przemek Delewski** 15:08 So, so it is, sorry. Hotel, auto maintainers, but there is, I don't know, this sign between these two words, how to…
**Marc Schäfer** 15:26 Yeah, I know what you mean. Okay, okay, yep.
**Przemek Delewski** 15:28 Disconnector, but I, I… I don't know how to say that in English.
**Marc Schäfer** 15:33 Me either, me either, but I know what you mean. So, yeah, okay.
Good, good to know. Okay, then I'll… we'll try that.
**Przemek Delewski** 15:45 Maybe, someone will join.
Because I see… That they are writing something on the channel.
Because I'm… I mentioned that, I joined, and you are also here.
By Hu Xingq.
Do you hear me, guys?
**Marc Schäfer** 18:47 Yep, I can hear you.
**Przemek Delewski** 18:50 Yeah… I know that you hear me, but I'm just.
**Marc Schäfer** 18:56 Checking with the other ones.
**Przemek Delewski** 18:57 Yeah, yeah, yeah, yeah.
**Huxing Zhang** 18:58 Yeah, I can't hear you.
**Przemek Delewski** 19:00 Okay. Hi, Kimmo.
**Kemal Akkoyun** 19:01 Hello, sorry for being late.
**Przemek Delewski** 19:05 I wasn't sure if we have this meeting today, but I joined, and we have a new person, Mark.
Who joined, and he's interested in participating in this SIG.
**Kemal Akkoyun** 19:17 Okay.
Oh, yeah.
**Huxing Zhang** 19:20 We haven't been met for a couple of weeks, and I think we can meet.
**Przemek Delewski** 19:25 Yeah.
**Huxing Zhang** 19:25 have a specific topic, I think.
**Kemal Akkoyun** 19:28 Yeah, we haven't met, but we also, like, figured out the way working efficiently, asynchronously, so I think… I can't complain. For the past few weeks, we are creating PRs, people reviewing PRs, and yeah, we have a good momentum.
**Przemek Delewski** 19:47 Yeah, unfortunately, the problem for me is that I'm very busy recently, and I couldn't participate as I… as I would like to.
So…
**Kemal Akkoyun** 19:58 No worries, this is open source work, right? So, best effort.
Cool. So, do we have any particular, like, topic for today? I guess I have one. Apparently, I put it here.
Besides that… Anyone else? Any… Any topics?
**Przemek Delewski** 20:24 I think that I don't have… Topics.
**Kemal Akkoyun** 20:29 Okay.
**Huxing Zhang** 20:29 I, I, I, well, I was wondering, to… I… I'm planning to go to the KubeCon EU, and I'm planning to meet with the… hotel sick maintainers, maybe others with other SIGs, so… or we… what… if there is anything that we can share with others, they maybe connect with them, or maybe good for us, I think.
That's what I'm going to do, and to… maybe we can do… some brief introduction to our SEC, and let the folks know what we are doing, and what is the latest status, right now, and maybe can, like, future cooperation, maybe, or… and, yeah.
**Przemek Delewski** 21:29 Yes, I think that maybe not all people know that this SIG exists, so it would be good, you know.
To… to talk with people.
**Kemal Akkoyun** 21:41 Yep.
Definitely. We had… I think, like, at least Open Telemetry Committee knows about us. He had a lot of, like, discussions in the hotel unplugged, which was adjacent to the four stem.
But yeah, let's, like, spread the news.
We will be releasing… the V1 by the time of the next KubeCon.
Yeah, I think we should aim for really putting, like, getting a talk in for KubeCon North America, and, like, I don't know, if it's not in the main track, maybe in an observability day, let's talk with the OpenTelemetry, like, governance committee, like.
Because we will have our, like, big moment of, like, stable release for the next KubeCode.
And let's try to have… A dedicated time to talk about it.
**Przemek Delewski** 22:39 Are you, Kemal, also attending this KubeCon in Amsterdam?
**Kemal Akkoyun** 22:44 Of this one.
**Przemek Delewski** 22:45 Okay.
**Kemal Akkoyun** 22:46 try to attend the next one in North America, just because, to talk about our, like, project, right? Because we will be GA by then.
Okay, Cool. I think we can just, like, socialize the project, try to recruit people, there is no harm to that.
More is merrier, so… Definitely, let's go for it.
I am trying to also take some notes.
But I don't know what to add for this one.
Okay, so I actually have one topic. Maybe I could just, like, jump onto that. Can I also share my screen?
Okay.
So, yeah.
Let's begin to talk about this.
So, one request, so we always had this, like, silent agreement on the PRs that we don't merge.
before, like, the other parties approved, right? So if I'm, like, from… coming from Datadog and creating a PR, if I only have… an approval from Dario, I wouldn't merge that PR, right? I would wait for Primajek, or, like, Yi Yang.
So, I saw that, like, we merged, like, two PRs, For the integrations, and… I… It's no biggie, but, like, we should still respect this rule, I guess, right? If the PR is created by Alibaba, I should… I think we should at least wait for someone from other parties to review that and give an AC before merging it.
And these PRs are, like, quite sizable.
I think if it's, like, sizable, definitely we should abide this rule. But if it's a small thing, I don't worry about it, right? If it's a fix, if it's a small thing, we can merge it. But otherwise, let's wait for some consensus.
What do you think?
**Huxing Zhang** 25:02 I think that's a good program. I agree.
Yeah.
**Kemal Akkoyun** 25:10 I'm glad that no one objects that, so, yeah.
**Przemek Delewski** 25:14 I was thinking about, you know, discussing that on the Slack channel, but… I'm not sure.
I mean, when there is a PR, just mention it on Slack channel, and maybe wait for some time before merging it, something like that.
**Kemal Akkoyun** 25:31 Yeah.
Yes, I think that should be the way to go, like, ping people on the… select channels, I don't know, like… Everything can wait, but again, like, if… no one responds in, like, I don't know, a week? We still have the meeting, right?
**Przemek Delewski** 25:50 Maybe not even a week, maybe that would be, I don't know, two days, and we can then merge it if no one, you know, responds, and you have approval already from, let's say, the same organization, we can merge it, something like that.
**Kemal Akkoyun** 26:08 Two days is not enough for certain PRs. Let's stick with a week. Like, some PRs are huge, and, like, sometimes you want to… at least that's for me. I want to carve out some time to actually review in depth. And these PRs were waiting for that, right? Okay, these are… Like, BPRs, I need my, like, concentration, but then I wasn't, like, fast enough.
**Przemek Delewski** 26:32 But I was thinking about the small ones, so… but… Yeah, okay.
**Kemal Akkoyun** 26:37 Small ones… small ones are, like, if it's, like, I don't know, it's 10 lines of change, and it's fixing something, just go and merge it. I mean, you are… you are the maintainers, like, the small things shouldn't matter, but if it's changing something substantial, you should definitely wait for other parties to review.
**Przemek Delewski** 26:55 Yeah, that's for sure.
**Kemal Akkoyun** 27:09 Okay.
**Yi Yang** 27:13 Yeah, for two projects, I think we can… we can merge immediately, but for some substantial purchases, such as… And the instrumentation plugin, or, modifying the tool, we should… we could, at least merge… at least wait for two approvals.
**Kemal Akkoyun** 27:34 Yes.
Totally agreed. Totally agreed.
And I think we have enough reviewers, right? And enough different representation, right? We have Avier, we have Premierk, we have Datalog people, we have Alibaba people, like, we have four parties, and we just need an additional one party in this case, and I think that's… Shouldn't be a problem.
We have other approvers that we recently onboard to the project, but I guess they also disappeared after getting the approval rights.
I guess this is the life of an open source project, nothing to do about it.
I'm checking recently, we merge a lot of PRs.
Yes I mean… Yeah, we are on a good trajectory.
Anything else?
People want to add?
Cool.
We have some PRs, like, in, like, adding Kafka implementation. I think this is a huge PR.
And then the OpenAI Go SDK implementation, which is a… could be a really cool one.
Yeah, I'm… I will try to spare some time to review those, but if anyone also has some, like, spare time, that would be nice.
and we have, like, this log, like, S-Log and the Zap logging instrumentation. It's been also waiting for a while now. It's since last month. It's… it's been a month. I think this is not good that this one sits here. And it's from an outside contributor, and it's kind of discouraging.
So we should also, like, focus on that one as well.
**Przemek Delewski** 29:44 Yes, right.
**Kemal Akkoyun** 29:49 So yeah, like, if you have any spare time, for reviewing PRs, please go ahead.
Any other topics, or, like, Mark, do you want to, like, say something?
If you have any questions.
**Marc Schäfer** 30:12 Until now, not.
**Kemal Akkoyun** 30:15 Okay.
We are glad that you are here. We are still looking for, like, outside contributors, really.
**Marc Schäfer** 30:22 I'm always happy to help.
I want to… I always… I already, pulled.
Sorry if I pronounced your name wrong. I told him already that I'm more… well, nowadays, I'm more of a… DevOps system engineer, but I started in IT, with… within school. Maybe sounds, like, low, but I did many, many, applications and stuff for the school, like, a whole, school, plan.
Where every student can view their exams and upcoming lessons and all that stuff.
On mobile phone and also on web. I did that during school.
And… but then I joined, my current company. And got into more into the system administrator role, and since then, or about 2 or 3 years, I've almost coded nothing, only, like, maybe private side projects, but now I really want to get back into coding, and yeah, that's why I started,
**Kemal Akkoyun** 31:30 I'm super happy that you picked us. Yeah, this is the kind of a cool project, and, like, it's nice that…
**Marc Schäfer** 31:37 Definitely is.
**Kemal Akkoyun** 31:37 unbelievable.
**Marc Schäfer** 31:38 Different issues.
I did, so I did some, some, some PRs, already on the, Go repository of OM telemetry, but not on the compile instrument station yet.
The big, the big yet.
**Kemal Akkoyun** 31:56 We have a lot of things to work on, like, you can check our issues,
**Marc Schäfer** 32:01 Yep.
**Kemal Akkoyun** 32:02 Too many things to take care of.
**Marc Schäfer** 32:04 I did already just a few seconds ago, so…
**Kemal Akkoyun** 32:07 Yeah, some of them are, like, super, like, low-hanging fruit, so you can… I actually done this.
**Marc Schäfer** 32:17 Did I? Okay.
**Kemal Akkoyun** 32:19 I should assign this myself. I thought I created a release MD file, and I don't know if I cover everything. So yeah, I checked the issues, and it should be, That would be a lot of, like, things to work on.
But always, like, before starting, ping us, ask for more context, or whether, like, we actually done it, whatnot. Some of the issues can be stale.
**Marc Schäfer** 32:43 Yeah, definitely. I did some cleanup in the… Go repository, go home telemetry one, I think I got to close, or not myself, but I got the maintainers to close about 11 issues, and 3 or 4 stale PRs.
**Kemal Akkoyun** 33:01 Awesome.
**Marc Schäfer** 33:01 did two or three APRs of my own already, so…
**Kemal Akkoyun** 33:06 Awesome, awesome, great, great, great help.
**Marc Schäfer** 33:11 There are much more issues and much more stable ones than you have in your repository.
**Kemal Akkoyun** 33:17 DV, we are right now smaller.
**Marc Schäfer** 33:19 Yeah, smaller, smaller one, definitely can't compare to the main GoAM telemetry repository, so…
**Kemal Akkoyun** 33:26 We want to change that, though, so you want to be one of the popular protein.
**Marc Schäfer** 33:30 Definitely, definitely.
I can understand why.
**Kemal Akkoyun** 33:33 Yes.
Cool, we have another topic. Do you want to talk about it, Gwen?
**Huxing Zhang** 33:40 Yep.
I just, on my notes, I, I, as I mentioned in… earlier in the Slack channel, and, we are working on some sort, something about the… Jingai UTLs, that, which is the… right now, one of the focus of our… our team. And, actually, we first, start doing this in Python.
Python instrumentation, that be… a lot of use there, and as long as we are working with the semantic convention, we are adding some semantic convention for the AI agent, and this is a kind of UTLs SDK, Like, we can wrap the things that an agent can generate, and you don't bother with the detail of the… how to add the two different itches, of the semantic convention things, so you can simply grab the data and call this SDK, and it will automatically create the, format that can follow and can follow the latest semantic conventions, something like that. This is just a prototype.
So, Usually, when we're doing some instrumentation, we have to handle things, like, we want to add a geni input message, like a span, a span, attribute, or something like that, or you need to focus, you need to understand the, a lot of, Span attributes and a spam hand.
But, if you are using this, JNI UTL SDK, it will be a lot of easier for, a developer to, like, to, add a new instrumentation to the AI agent. That's what we do… we are doing in the Python, Python, country, and, we are also migrating this to different languages, like Java and Go, we are still start doing things like that, and we… We'd like to see if the committee's interested in this one, and we can maybe contribute to the… to this, gold repo. Yeah, that's what I mean.
8.
**Kemal Akkoyun** 36:10 I'm checking these PRs, and I think, like, this is… this, the OpenAI, PR that we are… That is opened by the community member, and they are doing similar stuff, and they're adding this, like, GenAI convention package whatnot. I guess this util package does similar stuff.
And… Maybe if you want to contribute this to the repo, maybe this is the time?
before we measure the OpenAI PR, and we can say that, okay, like, we had plans, that's why, like, we would like to first integrate this gen utils through the compile time, and we want you to maybe rewrite your OpenAI PR, or vice versa, like… I leave the… so, for me, it's okay to have this, and apparently you have invested a lot of time onto this, and you have the knowledge, and that would be super nice to have Gen AI conventions within the repo now, because it's pipe, and then start adding, like, the integrations like OpenAI.
So… I mean… if someone from, like, someone has an expertise on this utils can have a look at the OpenAI PR, and maybe open a PR to move, like, contribute the spec to the OpenTelemetry compile time.
Am I okay with that.
I think we should do it.
**Przemek Delewski** 37:40 Good point.
**Kemal Akkoyun** 37:45 But if you want to keep things clean, If you believe this util thing is, like, clean.
cleaner than this OpenAI thing, we should merge that one first, and, like, rewrite the OpenAI one.
**Przemek Delewski** 37:59 Probably, it would be simpler to do that this way.
**Kemal Akkoyun** 38:04 Yeah, would be.
Is this one of the…
**Huxing Zhang** 38:10 Sorry.
**Kemal Akkoyun** 38:11 Sorry, Miles, like…
**Huxing Zhang** 38:15 I'm just saying that, according to our past experience, we… on Python, we write a lot of, instrumentations by our own self before this, general YouTube has, come out. But, We found it are very difficult, because different developers, they might not be aware of a lot of details of this.
**Kemal Akkoyun** 38:40 they.
**Huxing Zhang** 38:41 I've made mistakes, or they're missing something. But if we use this, this is, like, tool, a standard, standard tool, they can avoid things like that, and we have already migrated our, past implementation, tool this.
new sort of UTLs, you know, using this new one, and that makes us more… it's easier for us to, keep up with the semantic conventions, yeah.
**Kemal Akkoyun** 39:14 Yeah, let's have it. Let's have it in the instrumentation package, yeah, like, sooner than later. I don't know if they can directly… probably he's working for Ali?
**Huxing Zhang** 39:27 Yeah, yeah, he's from my team, and he will send an issue or create a proposal first. I'll let him, but he's not in this meeting today.
**Kemal Akkoyun** 39:40 Yeah, an issue and, like, a PR would be nice. Yeah. And then we can tag the OpenAI person that we want to merge this one first.
And they can, like… yeah, we can speed this thing up as well. I don't… I don't think this… it would take a lot of time to integrate this package to our tool, because, like, the conventions that we have is quite similar still, so should be really fast.
**Huxing Zhang** 40:09 Okay.
**Kemal Akkoyun** 40:10 Awesome.
Okay.
Any other topics?
Dario and I, we will be working exclusively on this, the issues that we are trying to, handle for, call site instrumentation, like this OP31, OP5, and OP4 for this week and the next.
So, we would really appreciate the reviews.
Yeah.
Then we will start, like, the, next quarter. We will start, like, migrating our, things from Orchestrian to this tool.
And see that, like, we will benchmark that, so that eventually we can decommission the orchestrium From our tool stack.
Oh, yeah.
**Przemek Delewski** 41:26 You mean migrating some instrumentations, or maybe some generic stuff?
**Kemal Akkoyun** 41:33 No, no, we have our instrumentations within our repo, right? That is how we use, Orchestrian, but we, like, for our, like, own library, right?
And… Say that, like, but we don't wanna… keep maintaining two tools, right? That's why we wanted to have the donation. So our goal is the next quarter is, like, these YAML files that we have for Orchestrian. We will write equivalent OpenTelemetry compile time versions of it that injects our library.
then, yeah, then we plan to eventually decommission the orchestrian and use everything from upstream. So, we really appreciate your reviews, so that we can have all the features.
Yeah, I don't know how Alibaba feels about it. I don't know if your… what is your plan for the long-suit, agent? Like, at least for the compile time version, we don't want to keep maintaining orchestrian, so…
**Huxing Zhang** 42:35 Yeah, we just have a short discussion about that before this meeting, and we actually are planning on that to migrate to the upstream one to, we, to, to migrate our internal repo from this, upstream one in IP next, semantic, maybe. I think in the late this year, I think we, we are.
about that, and, we don't want to maintain this too, and we will, post a plan about the what we're gonna do next. And I think this community effort really helped us a lot, because we have a lot of more features that we didn't expect before, and we can't do it by ourself.
But we, through this community effort, we can get a lot of features, for example, the co-site instrumentation and, other, very, very good, features. This is very useful for us, and we will, continue to invest on this project and, make it upstream to our of our repo, right? Yeah.
**Kemal Akkoyun** 43:57 Awesome. I'm glad to hear that, like, and SIG is actually working, so we, like, we haven't bailed yet, and we will produce a state-of-art tool. I also believe that as well, especially when it comes to integrations and different type of instrumentations that you can have from community.
I don't think we can keep up with all these, like, new tools, open source things happening, but people, the library authors, maybe the application authors, we will just, like, put them here, and that will be super awesome.
Yeah, let's focus on that, cool.
Any other topics?
going once.
Twice?
All right.
Alright, it was great to meet again. Let's keep up the good work.
And see each other in a few weeks.
**Przemek Delewski** 45:00 Thank you.
**Huxing Zhang** 45:01 Mommy, I… Bye-bye.
