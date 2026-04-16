SIG: Technical Committee
Date: 2026-04-15
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Reiley 00:02:25 Hello, Carlos, Tigran.
Carlos Alberto Cortez 00:02:28 Hey!
Tigran Najaryan 00:02:30 Hey, guys.
Josh Suereth 00:02:51 Hey, folks.
Sorry, the, previous meeting ran a little long.
Reiley 00:03:00 Hey, Josh, how are you?
Josh Suereth 00:03:02 I'm bad, how you doing?
Reiley 00:03:05 Yeah.
I was on vacation last week, and just, like.
But I'm trying to catch up.
Josh Suereth 00:03:15 Yeah.
I feel your pain. Tain's stinked, and… Let's do triage quick.
Oh my god, I suck at this. That's 11.
Did anyone take a look at the… Our inbox yet?
Reiley 00:03:45 Not here.
Josh Suereth 00:03:46 D.
Community inbox… Also empty.
Unassigned open spec PRs, we want to assign TC members here, right?
Let's do a little bit of this while we wait for people to show up. Do we… were we starting at the bottom or starting at the top with this? I don't remember, sorry.
For assigning spec PRs.
Carlos Alberto Cortez 00:04:12 I think of the old ones.
Josh Suereth 00:04:14 Old ones? Okay.
Carlos Alberto Cortez 00:04:16 If I remember correctly, yeah.
Josh Suereth 00:04:18 Alright, hey, stable by default.
I… I'm amazed.
Tigran Najaryan 00:04:25 I think we… I think we said we… we don't assign OTEPs? Am I misremembering?
Reiley 00:04:31 You're right.
Carlos Alberto Cortez 00:04:32 Yeah, I think OTEPs can be assigned, but that's only if we really feel like that. But yeah, usually OTEPs are not covered.
Josh Suereth 00:04:40 I'm gonna add this to the agenda, because the fact this isn't merged, and the fact that we're, like, calling this our number one priority, there's a problem.
jmacdonald 00:04:49 Yeah.
Josh Suereth 00:04:49 We need to talk about it.
I'll add it to the back of the agenda.
Okay, I think it might be good to assign one of us to help make this make progress, because it's not, somehow.
Carlos Alberto Cortez 00:05:05 Yeah, that's what…
Josh Suereth 00:05:06 Good.
Carlos Alberto Cortez 00:05:08 Yeah, because It has enough reviews. It has enough reviews. There are some last details that somebody has to drive.
That's the important part.
Josh Suereth 00:05:18 I think we need to make a decision of… with… so basically, this has me nervous here.
And then, some of the feedback that we've seen from some of the maintainers also has me a little nervous, but we could make a decision of, like, maybe this is something that the TC and GC decides and pushes through.
you know, before we said, like, hey, this is blocked because we want to see more maintainer approvers, and immediately after we said that, one of the maintainers marked it as, as request changes, right?
Liudmila Molkova 00:05:50 To be, precise.
this is the… Robert's manner to express things. I believe from his comments, it's not a directional disagreement, it's… there are some, specifics that, needs to be discussed. It's not a directional disagreement, but yeah.
Josh Suereth 00:06:11 Yeah, that's fair, that's fair, and I think, The other thing is, I saw some confusion from reading here and misinterpreting details, because this has a lot of details in it.
there was a discussion on another thread, on another OTEP, I think it was with Anthony Marabel and I, where he was basically reading this and saying, hey, I don't think what you're saying lines up with this at all for the, like, federated SEMCOM working group.
I'm like, oh, well, it should. So, anyway, we can talk through details later. I… Well, it's timebox, I'm getting derailed.
Liudmila Molkova 00:06:47 I think if you want to assign somebody, I would be happy to assist in getting this resolved. Also, I think we discussed that we will dedicate some time on every spec call for this, 20 minutes.
Josh Suereth 00:07:02 Yep, okay, so I… Ludmila, thank you. I'll assign this. I think we need to figure out what, I'd like to get this merged, but I also want to make sure that the Way that, folks are interpreting it is not, is actually aligned with what we want to do, and, like, that does make me nervous, is like, is this phrased in a way that people will interpret it wrong? And that could still be true. That was the whole problem with it to begin with. Okay.
Cool.
So we're skipping OTEX?
Hey, speaking of the devil, that's the OTEP that was commenting on this OTEP, if you look at the latest activity. So, hey, alright, anyway, we'll move up.
Prometheus Update Resource Translation.
David, since you sent this, do you want to own this?
Tigran Najaryan 00:07:56 It's the same there, right, Josh? We distrust that if it's submitted by a TC member, it doesn't require assignment. Whoever submitted it already owns it.
Josh Suereth 00:08:06 Alright, I think we should just add the assignment so it doesn't show up in this filter then.
David Ashpole 00:08:11 Just sign it to myself.
jmacdonald 00:08:12 I'm happy to keep approving all those Prometheus PRs. I started yesterday.
Josh Suereth 00:08:18 Cool.
What about… what about this one? Stabilized Prometheus Labels, OTLP Instrumentation Scope? That feels like Prometheus-related.
David Ashpole 00:08:26 Yes, definitely.
Josh Suereth 00:08:27 Okay.
Oh, and you guys already approved, awesome.
Okay.
Alright.
One more minute.
Maybe one more. That was Arthur. Add event to span event bridge.
I think this one actually has enough to merge now.
But we can add this, Sony. Good.
Liudmila Molkova 00:08:54 Feel free to assign me, my goal was to manage it by the end of the week, unless there is any feedback, and… I've posted in the spec channel.
So, just giving people a few days.
Josh Suereth 00:09:07 Okay.
Then… alright, well, I want to do one more, then. Stabilize SDK Exporter temporality.
Who… I'll just offer David or Riley, either of you interested in making sure this one makes it through?
Yep, David, was.
David Ashpole 00:09:24 Yep.
Josh Suereth 00:09:26 Gotcha.
Awesome.
David Ashpole 00:09:27 This is like, make sure the Prometheus exporter asks for cumulative metrics, essentially. It would not work.
Josh Suereth 00:09:36 Cool. We're at, we're at, like, almost 10 minutes after, so let's get into the agenda.
Jack?
Security Advisories.
Jack Berg 00:09:47 Yeah, so, I want to pick up the conversation that we were having last week. We've made some progress since then.
And just for context, last week we were talking about this uptick in security advisories, and, you know, it's definitely due to AI. Researchers and more casual contribution… contributors now have this ability to, you know, ask You know.
very simplistic prompts to these AIs, and potentially find vulnerabilities that have gone undetected for a long time, and that's even setting aside, you know, this stuff about Anthropic's mythos and Project Glasswing. You can still find reasonable vulnerabilities with the existing open source, generally available models and tools.
And so, you know, there's a couple of questions that I have. So, like, some are tactical, which is like, hey, we have this TC on-call, and one of your on-call responsibilities is to review and sort of shepherd along all the vulnerabilities.
There's a lot more vulnerabilities, and they're not getting resolved over the course of a week, and so there's a lot more carryover, from week to week.
And so, one of the things that I think we need to do has been somewhat addressed. We need to get the tooling to do the advisory tracking with the Grafana and that tooling that Armin built back functional. And that's back functional, that's great. So now we can all log into this Grafana dashboard, see a list of all the open security advisories.
And do things like sort by how long they've been open for, and prioritize ones that are… have been open long, or, you know, follow up with them to shepherd them to conclusion.
So that's one thing.
And if anybody has anything to say about that, we can pause and make comments. But then, like, you know.
it also has implications on what it means to be on call. So before, you know, you'd just kind of casually check for new advisories. There might be, like, one a week. You'd ping some people, it would get, you know, it would mostly reach a conclusion with a reasonable level of intervention. That time commitment changes a lot.
So, what are we gonna do about that? Like… Are we gonna do anything about that, or are we all just gonna, like, internalize that being on call means a lot more than it did before?
Tigran Najaryan 00:12:18 How many more, Jack, how many more are we getting? Like, last time I was on call a few weeks ago, 3 weeks ago?
I think I only got one.
Maybe new one?
I mean, it does not open, but…
Armin (Dynatrace) 00:12:32 Yeah, this big kid has been 10 as well.
Jack Berg 00:12:34 I got, like, 10 the 2 weeks that I've been on call in the last, like, month or two.
10 Punch Week.
David Ashpole 00:12:40 about age.
jmacdonald 00:12:40 There's two in my week, in February.
Reiley 00:12:44 I've been looking into this for a longer time. I can share my observations. So, it used to be much lower, but now I see a trend, and it seems it's not going back. And I think the trend is coming from two factors.
One is OpenTelemetry is getting more and more adoption, which is great. With more adoption, that means people care about security more. There's a general, risk of, like.
raising level of awareness about security. And the second one is thanks to AI. Like, I… I've seen that in a lot of OpenTelemetry repos. People are just, like, sending, like, more than 10 PRs a day. They're saying, like, we use this codecs or cloud. We just ask, like, go and scan the code, what are the issues?
And although, like, our maintainers and community members can do that, there's third-party folks who can do this, and we actually work with some companies from UK to do the AI-based, fast testing by simulating different kind of input. So, with AI, I expect the number of PRs, not the number of security advisors, all of them would increase significantly.
And I guess this is why we're seeing more and more recently.
Jack Berg 00:13:57 Yeah, and, like, one thing… so there's a number of people from Grafana that work on OpenTelemetry, and internally, we've been having conversations about this. One thing the maintainers from Grafana have been doing is preemptive scans of the repositories that they're owners of.
So, like, you know, that seems like a good thing to do. And, like, all of our maintainers could do that.
And maybe they should do that. So, like, you know, you gotta stay ahead of the attackers, and, like, you know, now we have tools that allow you to do that in a relatively straightforward manner.
So, you know, one tactical thing that we could do, as the TC, and we could get the GC involved with this as well, is make recommendations to the maintainers to do preemptive scans, so that they don't come to… you know, their fixes and PRs instead of security advisories. That reduces the overall amount of effort and coordination needed to fix these things, and they're fixed sooner than they would have otherwise.
Reiley 00:14:56 Yeah, I know Trask and Jeremy, they had some discussions about this, and there's a conversation about consistency, I've got some, approval from cloud. We can use their latest, like, tools to do the security scan. I think they have a general interest in helping open source, and to, like, advocate for their tools. And I also shared a link here, you can see this is similar. This one, I… I don't think it's coming from Grafana, but the maintainer is from Grafana, and the developer, I believe, is from Splunk. But anyways, this is a general trend, like, people have good intention, they run the tools to detect the potential problems.
And definitely, I see a lack of guidance there, because AI is coming faster than we thought.
Jack Berg 00:15:50 So… Another aspect of this topic is the source of where these advisories are coming from. You know, the elephant in the room is that, you know, most of them come from the collector, and collector contrib.
those projects have huge surface area. Those projects represent, you know, the portions of our collective open telemetry surface area that are actual servers responding to requests, and so they're the natural candidates for exploits. It's, I think, you know, categorically more difficult to have, like, an exploit in a client library than it is, like, a server.
And so, it's natural that that's where the vulnerabilities, the advisories are gonna, like, tend towards. So, Pablo opened this conversation in the GCTC channel. It's a private channel, I don't think you should open the link, but, like, you know, I could, you know, take the comment and bring it here, but I just didn't want to do that. But essentially, what Pablo suggests is, looking at the security posture.
of other open source projects that have, like, a similar type of purpose as the collector, and seeing how they think about scoring and classification of advisories on whether they're actual vulnerabilities or bugs. Like, is it… it's the classic thing, like, is this a vulnerability, or is this just, like, a bug in the code?
And the answer to that matters. And so, Pablo is looking at prior art like Postgres, he's looking at prior art like Prometheus and the stance that they have, and, you know, essentially saying, like, hey, if we come up with a set of recommended configs for the collector.
And, and those configs include things like, hey, you don't have full, unauthenticated network access to a collector. This isn't something that's open to just, like, the public internet. Then, this scoring.
changes dramatically, and the scoring changes and what gets classified as a vulnerability versus a bug changes, because you can say, like, a prerequisite for something being, like, a vulnerability is that it's done within the bounds of your expected reasonable default config.
So, you know, Pablo explicitly asked for TC input on this, on the collector, because, like, Pablo's a collector-maintainer, but, you know, he views this as a point that is a big enough discussion that I think he wants the blessing of the TC. So, yeah, our point of view would be appreciated.
Josh Suereth 00:18:29 I really like the direction that's going. When I was on call last, I think I had a back and forth with a submitter of a vulnerability, saying, I don't think your score is correct, and this would have helped to, like, fix that, because they wanted something to be marked vulnerable, and I think they have a financial incentive to do so, by the way.
To report critical vulnerabilities, so I think us fixing that is good. What I would suggest is I really think we want to make it so that we have these recommended, you know, how to do open telemetry securely, but also we need to make sure our defaults are secure, if you will, in some fashion. If we say, hey, this is where… this is what we consider vulnerability tracking, this is, like, standard config, and if you've configured to, like, open up security in some way, like, allowing unauthenticated access.
then that's on you. You've taken on that risk, that is… that's not, like… But this goes a little bit to, like, packaging and defaults, of… I think if we provide that guidance, we also need to have guidance of our default should actually be the safe way to use OTEL. Is that fair?
Jack Berg 00:19:42 Yes.
And Pablo has some good quotes here in his message, you know, from the Postgres, from their stance.
You know, Postgres does not consider denial of service on PostgreSQL from an authenticated, valid SQL statement to be a security vulnerability. Like, if you're an authenticated client and you submit a query that is extremely expensive, and it ultimately provides denial of service, that's not a vulnerability. That's the feature. And, you know, you're just misusing the product.
Right? So that's a good one. Another one that I like, and this is from the scoring guidelines for CVSS, is, you know, unreasonable configurations are those that deliberately place the target in a vulnerable state by disabling security features Or that conflict with documented configuration guidance, right? So we can… we can cherry-pick some of these bits, into the collector's policy.
When we're crafting that, so… I see a lot of heads shaking, I've seen a lot of, like, thumbs up, so I think the TC is generally aligned with Pablo on this.
So, you know, how can we move forward? We have a couple of TC members that are, you know, deeply engaged with the collector project. You know, do we want to give the thumbs up to Pablo and just, like, you know, ask him to, you know, craft a policy that makes sense?
For the collector, and, you know, loop in the TC, when they do so.
Reiley 00:21:18 I, I suggest we ask Pablo to… put some proposal and try to merge a PR in the security repository, and instead of doing that specifically for Collector, describe that in a general way. Of course, like, with the mind that it must help Collector, but it… like, I don't see there's anything specific to collector in this case.
It's like, if you ship a binary artifact with configuration, this is what you should do. If you ship a binary artifact without any configuration, without any exposed, like, surface, you're just like a client, without listening or anything, this is what you should do.
then this is, like, a reasonable balance that would be good for a collector, and also will help to guide the other ICKs.
Jack Berg 00:22:08 Do you agree?
Tigran Najaryan 00:22:10 Yeah, I think the policy, having that policy is useful. The other bit that we'll need to solve is the process. I think our process today requires that the TC members somehow Are the entry point for these reports.
And I think we're an unnecessary middleman here. If the vulnerability is in the collector, we're not fixing it. The collector maintainers are fixing it anyway. So, what's the purpose of us being there between the reporter and the collector? It's not entirely clear to me. Especially because you're saying we're getting 10 new, and maybe it will increase even more each week.
Are we helping? Are we useful there by being a middleman? I am not sure about that.
Reiley 00:22:59 I can share some context there. I think the intention is not to have TC micromanaging every single thing, but the TC is held accountable for it. I think the expectation is the TC.
Tigran Najaryan 00:23:11 Why is Lotusi okay?
Reiley 00:23:13 Okay, let me.
Tigran Najaryan 00:23:14 Using the collector.
Reiley 00:23:15 So, it's like you're a manager of a thing. You don't write all the code, but you're accountable. You have to delegate. You have to define who should work on that, and make sure you work with relevant folks to have the execution. So, in this way, I think TC is more like the leaders of this group.
Initially, we were held accountable for security, and the expectation is through that we drive the process improvement and clarity, and we grow up the maintainers so they can do more.
But I still think there's a last line of defense. For example, if there's a common pattern across all the OpenTelemetry, like, 6, or, like.
across multiple projects. I think one recent thing is, if you send some OTLP request to an endpoint, and they give you a response, which… with unbounded, like, size. They just give you 1GB of the OTLP response. What do you do? And then we realize, oh, we need some limit, and we got to do this. This time, it seems like, like, a fairly low severity thing, so we end up, like, patching the spec, work with the maintainers to fix it.
But imagine, if there's a… a, like, very severe security issue across multiple repositories. Who's going to do it? I don't think TC can just wave hands and say, oh, like, let each maintainer figure out themselves.
Tigran Najaryan 00:24:34 No, I get it, I get it. If it's cross-companying across many repos, Riley, I understand it, but if it's clearly in a single repository, if it's a particular receiver in the collector.
which is vulnerable and needs a fix. What is the role of the TC there? And I'm not absorbing us of the responsibility. Yes, we are ultimately responsible, but what we should be responsible for, in my mind, is for setting the bar, for a quality bar.
Reiley 00:25:01 We've done it, yes.
Tigran Najaryan 00:25:01 expectation there, right?
Reiley 00:25:03 delegate.
Tigran Najaryan 00:25:04 Managing individual… yeah, I'm saying managing individual reports of vulnerabilities, I don't think we're useful there, really. We should immediately connect the porter to the person who will fix it.
Josh Suereth 00:25:17 I'm gonna disagree. I'm gonna disagree. And here's why.
I think we need to at least be an escalation path here on all of these. In practice, when you're on call, you give it to the maintainer, you ping the maintainer and say, hey, do you need any help? And they'll be like, hey, this vulnerability doesn't seem right to me, and you're there to help with judgment.
Right?
Tigran Najaryan 00:25:39 Sure, absolutely, we can do that, if that involvement is necessary, but is it always necessary?
Josh Suereth 00:25:44 It's not always necessary, but when it's not necessary, the only thing you do is assign it to the maintainer. It's not a huge lift.
But then the maintainer knows who you are, right? And they know that you're there, they know you're ready, and yeah, it's like, it's not a big deal, but it's like, at work, when we have on-call, there's always a secondary, but there's also always a technical lead, and you escalate to your technical lead when something's off. That's our role here, for the maintainers.
Of, cool, if something seems weird, you escalate to us, and we're there, and you're, like, we need to make it not tedious, we need to make sure we're not in the way.
But, like, our goal is to just make sure it's assigned to the right people, and to give them a path of escalation, and to help follow up with, like, weird off questions, right? It should not be a significant burden.
Except now, like, to the point that we all have, is a lot of the things coming in, I read the vulnerability, and it's like, I don't think this is filled out correctly, or this is abusing our config.
I think that's the thing we need to address, right? They're like, I configured the collector to be completely insecure, and I want this to be a high vulnerability. And you're like, no, that… your configuration's the problem. Like, you shouldn't run the collector that way.
Right?
Tigran Najaryan 00:26:58 I hear you, Josh. Does it have to be a TC member who makes that call that the vulnerability against the collector ease… Doesn't contain the necessary details, or is not legit, or… Are we in a better position than the collector maintainer can be to make that call?
I'm there to help if necessary. I'm not sure it's necessary all the time, so… could… could there be a process where, initially, that report lends into the inbox of collector maintainers, and we're there to help if we're needed? I don't know if we're needed all the time, or…
Reiley 00:27:40 alright?
Tigran Najaryan 00:27:41 Whether it helps if we're a gate between the report and the maintainer, or just upping the delay.
Reiley 00:27:47 like, if there's… if someone reported a security vulnerability using the advisory on GitHub to open telemetry, let's say Java.
I would expect all the Java maintainers would get that advisory, and I would wait for a day, unless it's super critical, then I probably would ping them. If it's, like.
I'll do a quick glance, and then I'll wait for a day. If the maintainers are not doing that, I'll send them a friendly ping. If they don't do this, like, in 3 days, I'll keep pinging them every day. Then I'll chime in and make sure they follow up. And they don't follow up, then I have something to follow up with the GC. And the process…
Tigran Najaryan 00:28:20 I may be missing something here. When they are… when the reports are open, when we go and look at them, are they already visible by maintainers?
Josh Suereth 00:28:28 Usually, yes.
Tigran Najaryan 00:28:30 Wow.
Okay.
Josh Suereth 00:28:31 Yeah.
Tigran Najaryan 00:28:32 Okay, then I… I somehow misunderstood, I… thought that unless we tag them, they are not going to see that. Oh, no. Okay.
Reiley 00:28:41 No, we're not doing stupid things here.
Tigran Najaryan 00:28:43 Okay, so they're never… but then the question to me… for me, would be then, every time I go and look at the newly opened vulnerabilities, the maintainers are never engaged immediately. Like, we're the first to be engaged there, which is a bit weird to me, because they… they… they are the ones that should be the… in my mind, should be the… okay, sure, I can go and say, oh, hello, I'm a TC member, I'm here to help, but why isn't the maintainer already on top of it?
Reiley 00:29:09 Maybe you're the victim, but… but… that's not always all the case, maybe you're just an unlucky one.
Tigran Najaryan 00:29:17 Maybe.
Reiley 00:29:17 It's a combination. It's related to which repository we're talking about, and I think in general, if a repository is owned by, like, two or three maintainers, then they normally have very clear accountability, but you have a repository owned by, like, 10 10 maintainers, and the issue with tag 10 maintainers, everyone would assume someone else's problem, because they haven't established an on-call thing.
Similar to what the TC has been, like, 5 years ago, right? We established the on-call recently, we started driver accountability, so that's something I think the maintainers can improve, and TC can give the suggestion. We can work with the GC to define some process. I think eventually we have to do it, but we're not there yet.
Tigran Najaryan 00:30:02 Okay, okay, it seems like we're doing…
Josh Suereth 00:30:03 Yes, no.
Tigran Najaryan 00:30:04 the on-call for all the SIGs in this case.
Reiley 00:30:06 And it's also related to some individuals. Like, I've seen the case where couple, like, I kind of gained the experience. I know in some repositories, there are maintainers who can I, like, I can reach out to, and they'll respond, and there are maintainers who never… like, never follow up with me. I can ping them on email, on GitHub, on whatever, like, Slack. They just ignored me completely, and I even have questions, like, why the other maintainers allow this maintainer to exist for such a long time? But this is, like… Some say I have to observe more before I bring this out to the TC.
Josh Suereth 00:30:42 So, I think Josh had a good point in chat I want to bring up, which is just, we have a rotation and a Slack reminder to check.
should we encourage these, these, like, the SIGs and the groups that have large maintainers to actually set up a security rotation across maintainers, and to share the load the same way we have? Should we make that like, maybe we can make that a repeatable process that all of these can have. Because, Tigran, to your point, one reason you're probably catching ahead of time is you have a responsibility One week out of every, what, 11 or 13 to, like, go look at it, and you do!
Which is good, that's what we want. Maybe we need for these… and we did that because in the TC, we had the tragedy of the commons, right? There's so many of us that I think, for a while, it was Armin doing all of them. And that's why we set up the rotation. We need to apply that same principle to everyone else.
Right? I think that…
Tigran Najaryan 00:31:38 I think so, yes. That may be the takeaway, because the process for us, the on-call process, seems to be working.
we may… it may be a good idea to roll out something like that for all of the SIGs who have any responsibility to deal with the… with the… with the reports, vulnerability reports, right? So maybe that's the… that's the takeaway.
Jack Berg 00:32:08 So…
Josh Suereth 00:32:09 Next steps, then, Jack.
Jack Berg 00:32:11 Yeah, so I followed up with Pablo, and just on the collector-specific thing, and, you know, he gave me a thumbs up to my response already, so I think he's going to make a proposal to SIG Security for an adjusted security stance, posture that reflects these types of ideas that he's thrown out there. You know, these other things that we're talking about, which is a recommendation for maintainers to have, you know, notifications, reminders.
call rotations.
How do we act on that?
Reiley 00:32:41 I have a question. So, I think individually, as a member of the community, I can give, like, personal recommendation, but do you think TC is in the place to define the process for maintainers, or… we can give recommendations and pieces. For example, like, we never said in the community repository, maintainers should define some rotation or something. We're just saying.
you have to be accountable for all the security things, but if they don't do this, we don't have a policy saying, if the maintainers are not doing this, we got all of them fired, right? So the TC, they worked on this process for the TC itself, but should the TC dictate the process for each individual repository containers? I don't think the TC has the power. Of course, we can give friendly recommendations.
Tigran Najaryan 00:33:29 I think there's two parts to that, Riley. Oh, sorry, I'm jumping the queue, Josh. Go ahead.
Josh Suereth 00:33:35 Yeah, you might be saying the same thing I'm about to say, which is, I think, there is a maintainer responsibility list of what maintainers respond with. So I think the next step here would be we actually make a proposal with the G… we talk to the GC about it, and we make a proposal to the maintainer responsibilities about some wording here. I think the on-call thing should be a recommendation. As long as maintainers are responsive and owning security vulnerabilities, they don't need an on-call, but we could provide a, hey, here's how we do it, here's the thing we set up, feel free to take the tech and use it however you want, right?
Reiley 00:34:10 Yeah, but one key outcome of that is we hold people accountable. This is the recommendation how to do it. We don't define process for you, but if you fail to be accountable there.
there will be a consequence. Like, there's always, like, what if you don't do it?
And GC should help on that part, I think.
Tigran Najaryan 00:34:29 Yes, interrupt me, I totally agree with what you guys are saying. I think there can be a hard requirement That you must deal.
with the vulnerability reports, it's your responsibility, it's not a recommendation, it's a hard requirement for maintainers.
the process can be a recommendation. We can say, we tried this, and it works well for us, we recommend you use something similar, but they may find a different process that works well for them, as long as it achieves the goal, as long as they are being responsible, I think that's fine.
Jack Berg 00:35:14 Okay, do we have a volunteer to make that proposal to the community repo?
Tigran Najaryan 00:35:25 It's not just that, though, Jack. I think we need to go talk to the maintainers. There's a bit more socializing necessary here.
Jack Berg 00:35:33 I mean, isn't the best way to socialize it? Like a PR against community?
Tigran Najaryan 00:35:37 But it's not enough, I think. There's more needed there.
Somebody needs and… Yeah, being the call, explain what we're doing, but it's a bit more needed here.
Jack Berg 00:35:49 I agree. So, like, in my head, it's like a PR that you advertise on the spec call, and you solicit, you know, feedback, you know, in a synchronous context.
Reiley 00:36:01 Yeah.
I agree with Jack.
So I think before the PRN community, there will be a heads up for the GC.
Yep.
Josh Suereth 00:36:29 Alright, so who signs up to do it?
Reiley 00:36:33 I can't do it, but I need one thing, like, from you, just want to see whether it makes sense. In the current community repo, we kind of define what's the role and responsibility.
where do we want to put those recommendations? I know in the SPAC, we have this supplementary guidance document.
Josh Suereth 00:36:51 So there's a role and responsibility in Community Repo.
Reiley 00:36:55 I don't know, but that doc doesn't define the process or any recommendation. Like, we just say, like, you must do this, you're expected to do this. If I'm going to add a section saying this is how you might want to do it, or this is the TC's recommendation, because we've seen success, I think that document would be super long, I just need somewhere else, like, maybe just a supplementary guideline, but I… I think that English term is… is very bad for… for this purpose, so… so… when it's in the PR, I don't feel I just add a long section in the role responsibility part. I need to have a separate place, and in the role responsibility, we can say, here's a link how we recommend you to achieve this.
We hope that's helpful. So, how should I do this?
Jack Berg 00:37:39 There's, there's an open-ended docs directory within community, which is docs about all sorts of odd things, like, how to use GitHub extensions, how to set up a new Slack channel, things like that. We could have a document that's like, yeah, like, you know, an example, Some guidelines. Guidelines, exactly.
Reiley 00:37:59 Okay, so I'll… I'll put a doc there, and I'll put a link in the role responsibility definition.
as a recommendation.
Tigran Najaryan 00:38:10 Yeah, one more thing.
Josh Suereth 00:38:12 Sorry.
Tigran Najaryan 00:38:13 I'm gonna show you…
Josh Suereth 00:38:13 Context, security vulnerabilities does not show up here.
I mean, health of the project does, but specifically security vulnerabilities is not called out.
For… for a maintainer, right now.
Reiley 00:38:26 Overall health is covering everything.
Josh Suereth 00:38:29 Right, right, but I think we should explicitly call out.
Tigran Najaryan 00:38:32 We need to be explicit, yes. I think we need to be explicit. One additional thing I would do here is we want to make sure that the maintainers act on this.
it's not just that they see the PR, and then in two days they forget about it, right? I would suggest that we file issues against every repository, that they came up with a process They are null .
whether they have an old talk or whatever, right? They came up with a process to make sure that they are dealing with the security issues as they appear, and have some sort of a summary with a checklist in the community repo, where once the SIG is done their part, we mark it as complete.
So that we can see the progress and make sure that we're actually covering all of the hotels.
Otherwise, it's just going to be forgotten in a couple weeks.
Reiley 00:39:32 Yeah, the definition of health is where things are getting interesting. For example, like, I can't imagine if we start to define something, like, you must respond within 48 hours or something. Then we're… we're getting into all the red holes and details.
So I probably will start with the intention, give some recommendation, and hopefully we can see some improvements there. Then, if the improvements are not big enough, we start to define some, like, more rigid rules, instead of trying to be very rigid upfront.
Tigran Najaryan 00:40:07 Sounds good.
Reiley 00:40:08 Thank you.
Josh Suereth 00:40:09 Alright, we only have 20-ish minutes left. Lyudmila, how long do you want for set stand status? Just to check to see if we can get to all of these. I might cut the stable by default, we already talked about it a little bit.
In terms of just making sure we have time to talk.
Liudmila Molkova 00:40:28 Just 5 minutes for this one.
Josh Suereth 00:40:30 Okay, let's jump in.
Jack Berg 00:40:32 Just on the stable by default, like, so we added it as a recurring item to the spec agenda for 20 minutes each and every week. That's… and many of us, most of us, I would say, attend the spec meeting. And so, I think that's the right venue to talk about this, and I think we're giving it the priority that it needs now that we've made it a recurring topic.
Tigran Najaryan 00:40:56 Agreed. I am… I'm not sure it's good enough, though. I would set up a separate, dedicated call, longer call.
To make sure we're making progress there. It's good for socializing, raising awareness. I don't think we're solving the issues there in that call, in the spec call.
Josh Suereth 00:41:14 Yeah, I know.
Carlos Alberto Cortez 00:41:15 Yeah, anything that… go ahead.
Yeah, I think that we need somebody to actually become responsible for this, so, you know, we can drive that conversation. Otherwise, we are, like, talking about the details, which is great, but then we are not making decisions, you know.
Josh Suereth 00:41:32 I was gonna… Carlos said, 100%.
Liudmila Molkova 00:41:36 Yeah, I think Josh assigned me to be responsible for this table by default. I think we need the discussion in the spec call just to identify individuals who would be in that other big call if we need it. Otherwise, we cannot invite the whole community to the call.
Tigran Najaryan 00:41:50 Yeah, I didn't mean we shouldn't discuss it in the spec. Definitely, I think it's important. I'm saying it's probably not enough, but there's probably a need to do, like, it's sort of a mini-C in a way, right? So, run it with its own calls, with proper duration, like, 20 minutes.
A week is probably not going to be enough to make progress.
Jack Berg 00:42:13 Yeah, I agree with you, and it's just the problem is that, like, the spec has the best attendance.
And, so, like, while we do need more time, you know, we're in conflict. We'd have a smaller group at that meeting with more time, and so, you know, we'd have to take those ideas and the outcomes and then socialize them back with a wider group. So, we're in a bit of a bind.
Liudmila Molkova 00:42:41 Cool, yeah, so then we'll discuss in the spec call, we'll find people who are for specific discussions, and I'm happy to set up individual ad hoc meetings for… for these individual topics with these, people.
Josh Suereth 00:42:56 Alright, let's call time on that, setSpan status triage.
Liudmila Molkova 00:43:01 Yeah, this didn't hit our trash yet, but it will, probably next week, and I wanted to get it, check the temperature. So, this spin-off from logs work, and switching from span events to logs, but essentially, the problem today is that when we, record an error, we have, semantic conventions guidance for this.
And it's not a trivial operation on how to do it right. And every SDK does it in a slightly different manner.
Even with SPEN events, so… Forget the exception part, but let's just say how we set an error.
There are 3 components.
As I mentioned, everybody does it inconsistently, so the proposal here is to introduce a helper method.
For the set error status, or something? Yeah, set error status, to combine these three things, and there will still be… it will still be flexible, it's just the default behavior, a sugar convenience method.
Just wanted to get your thoughts if, anybody would be against this.
Carlos Alberto Cortez 00:44:18 Just to be clear, this is, like, the equivalent of the record reception for spans, right?
Liudmila Molkova 00:44:24 It would not record exception, it would record the status code to error, it would populate the message, the status description consistently for everybody.
And it would also record error type attribute, which is what we need in semantic conventions to be consistent across pens, metrics, logs, and whatnot.
Tigran Najaryan 00:44:52 I think it makes sense to me, particularly for forego, I would use the second approach that Robert has there.
Because you'd… you'd still want, anyway, to have the differ span end there.
And… I don't think you need to have different end path there.
So I would just… I think it's set error status, or whatever we call that, makes sense to me as a concept.
Liudmila Molkova 00:45:23 Cool.
Can we mark it as triage, then?
Unless somebody wants to, I'm checked.
Tigran Najaryan 00:45:38 We want to… Do we want to explain that this is… Sort of a helper.
And… Do we want to have… helpers marked as optional. We don't have anything like that today in the API, really. Everything we have in the API Is a requirement, essentially, right?
Liudmila Molkova 00:45:59 Record exception is one, on tapos at events.
Tigran Najaryan 00:46:01 Is it optional?
Liudmila Molkova 00:46:03 Yeah.
Tigran Najaryan 00:46:03 Okay, okay.
Would this be optional as well?
Liudmila Molkova 00:46:07 I would imagine. It's a sugar, right?
Tigran Najaryan 00:46:10 Yeah, yeah.
I think it's fine, yes, as an optional, especially, if it's just a helper that is marked as optional.
Makes sense to me.
Liudmila Molkova 00:46:23 Thank you.
Yeah, I added this item for packaging. I think we had a bunch of discussions, on Slack.
And… the proposal… if I remember correctly, is to… Limit the scope to the current packages and their boundaries, and not break it for the sake of packaging sake.
But… We're then stability by default.
we will have a different, potentially, definition of what stability means, what pack… how packaging should be done in general, and the packaging SIG would need to… support this, but… What we're also being discussing, that essentially the principles of the packaging, this would be an OTAB that packaging SIG would start.
And as a community, we would review the OTAB, we would agree with principles, if we agree with principles, and then they would implement them for Linux.
The same principles would apply for other packaging efforts. They may change along with stable by default.
But, the OTAP is probably the key deliverable, and it's the first one.
And then the question is, If this is the reasonable scope.
Then, the sponsorship level changes, probably, to escalating, that's at least.
how I think about it.
And then, if that's the case, then the ask is, can somebody sponsor it?
I don't have… I think we should do this, but I have no expertise in packaging on Linux, and I'm not the right person to provide escalating sponsorship there.
Josh Suereth 00:48:36 So…
Tigran Najaryan 00:48:36 Are we happy with escalating? Maybe the… I guess the… We need to make a call.
Do we think that's good enough?
Josh Suereth 00:48:44 I'm gonna throw out that I think for specifically making Linux packages, escalating sponsorship's probably fine.
I really think we need to have an OpenTelemetry the package workstream that is lead and driven, and my fear is that by just, like, trying to de-scope this, we might make Linux packages, but miss, like, the thing we need.
You know, that's… that's my fear. That's… so, I understand why we want to go to just escalating sponsorship. I understand that, like, I… I… I literally cannot sign up for another thing because I'm overloaded on sponsorships, right? Like, we made a limit to make sure that we don't fail things. So, what… what we could do… Is if we wanted to basically stop the entity's work.
or SEMCOMF, which are the two I'm sponsoring, at a leading or guiding level, I would step in to do one of these, because I think it's actually really important we figure out the packaging.
And… and we can have that discussion, but otherwise, someone else needs to step up. If we de-scope it, it's fine, but I just want to call it what I think is the elephant of, I think, figuring out an OTEL distribution and treating us as a product is the next phase of OTEL.
That's the feedback we're getting from the technical advisory group in CNCF. If we as the technical committee can't step up and do it.
That's a problem.
I'm happy to turn off something to pick this up, but I really think we should not be turning this into escalating sponsorship. I think we should be taking that objective of making a package, somehow. And I know that everybody's doing hard work here, and I know that, like, what is it, the squeeze, right? Open source is, we all have to fight for time, we all have to fight with employers to get stuff, I get it. I just… I think that, you know.
I want to call out the importance of that mission, I don't think changes, and I'm worried that we're unable to put time on that mission.
Liudmila Molkova 00:50:48 I don't think…
Tigran Najaryan 00:50:49 you should stop the entities or the SAMCOM, Josh, just… that's my opinion. I think you should keep going there. I'd rather Yeah, sorry, go ahead.
Liudmila Molkova 00:50:59 what we, I agree that we need to find the Proper resources to… for the packaging overall, right?
So… If somebody on this call wants to volunteer the higher sponsorship level.
Let's do this. At the same time, it didn't happen so far, And it's kinda… Sad that we cannot sponsor something that important right now.
But one of the things this group can do for us, the Linux packaging, is that they can write this OTAP, and this OTAP would be a good indicator if we can even start writing this policy, and the OTAP is an actual deliverable.
I think that the Linux packaging after that, like, well, what, what, it's just a small technical job, what else it is.
Jack Berg 00:51:54 Good, Mela, can you repeat the reduced scope?
Liudmila Molkova 00:51:59 So, the problem as I understand it.
there is the Uber package we need to create, and there are the mechanics of how to create it for Linux. There are questions like, do we ship one distro stable, or one distro, experimental, or it's the same one with opt-in stuff, right?
This is one of the core principles we should have in Autel. Then there is a question of, okay, there is some existing understanding. For example, Java Agent. There is a stable distribution of Java Agent, there is an unstable distribution of collector.
Let's not break them down, but let's have the super package, including only the stable things by default, and having some mechanism to bring the unstable things on demand.
Let's figure out the default config.
The reduced scope here is, let's not change existing distributions.
Let's take whatever they consider to be stable.
Let's have a mechanism that will allow to take new major versions of these distributions going forward, and let's promise some cadence.
And let's outline the principles behind those choices. How do we package things into distribution without changing the principles how the… let's say, Java Agent is built.
Yet.
Tigran Najaryan 00:53:25 I think that the point of reduced scope here is also that it significantly eliminates the the extra work for maintainers in the… in the language 6, right? So we package whatever already exists, mostly.
And we… we come up with the requirements of… what… what needs to be there for the language or for the, let's say, collector component to be included in the stable package, but the work that is necessary to get there is phase two now, right? It's not in the phase one anymore.
Liudmila Molkova 00:54:01 So…
Tigran Najaryan 00:54:02 So phase one is figuring out the requirements and packaging what already meets the requirements, but not necessarily making sure everything else also meets the requirements.
That's… that's the difference, essentially, I believe.
Jack Berg 00:54:19 Can you cut the Uber package?
Liudmila Molkova 00:54:24 Sorry?
Jack Berg 00:54:25 Can we cut the Uber package from scope?
Tigran Najaryan 00:54:29 Then what remains there if you cut that?
Jack Berg 00:54:32 the individual packages that comprise the Uber package, collector, and each of the instrumentations?
Liudmila Molkova 00:54:39 Are you installed.
Tigran Najaryan 00:54:39 them separately? Like, what's the… how do you envision? What's the end result?
Jack Berg 00:54:44 So, the Uber package would take dependencies on the subpackages, the instrumentations and the collector, and the point that I've made a couple of times now is that it's still valuable to publish those subpackages, because the injector needs those. The operator needs those.
And so, we hash out the, like, the sort of, we develop, like, the muscle to figure out how we should do packages, the principles for how we should do packages without going all the way to the Uber package.
And, like, in the process of doing that, that takes time, and we finish up other work that allows our attention to shift towards the Uber package in Phase 2.
Liudmila Molkova 00:55:28 This is the opposite, essentially.
the two different… what… It's not a reduced scope, though, Jack, right? Or is it reduced scope in a sense that we specify which things we want to package today?
Jack Berg 00:55:46 It's a reduced scope in the sense that you do not have to decide and make decisions… you don't have to make decisions about how all of the subpackages work together, to form an overall open telemetry experience.
That's what you have to do as soon as you say that you want to build an Uber package.
You have to say what the collector's gonna do, and how it will play nice with the SDKs, and how OBI will, like, play a role next to the SDKs, and when it instruments things, and when the SDKs instrument things.
Tigran Najaryan 00:56:20 right, Jack? If they don't do that, then what's the… what they do, even, right?
Jack Berg 00:56:25 Well, the…
Tigran Najaryan 00:56:26 point.
Jack Berg 00:56:26 The, the, the, the… The line I'm trying to walk is that we don't have the time to do the important bit right now, because we're focused on a bunch of other things.
And so, if we can focus on the more trivial matters of packaging, finish up the work that we have in flight right now, then when it comes to do the more important bit of packaging, we'll have the attention.
Josh Suereth 00:56:48 Yeah, that goes to my overall thing, is like, I think if we cut the scope here to the point it only needs escalating sponsorship and doesn't involve any Cross-collaboration, the ecosystem and making hard decisions.
Like that, then are we… is this really a useful project?
But I agree with Jack, like, that's a… that would be the kind of scope that I'd be comfortable with, because, you know, just foundationally, we have an Uber package, we have to pick a versioning scheme. That versioning scheme's gonna be OTEL's versioning scheme.
And we're saying we only need escalating sponsorship for that? We don't want to be involved in that decision and participate, you know?
Liudmila Molkova 00:57:24 We will be through that app.
Josh Suereth 00:57:26 Exa… well, sure.
But then it's not really escalating anymore, is it, right? Like, we're actually, like, participating.
I think, I think we should be active in that discussion.
Yeah.
Tigran Najaryan 00:57:46 I guess the difference there is if it's through the OTAP, if decisions are made in the OTEP and they are executing that OTAP diligently.
then you don't need a single TC member to be leading in that particular seat. It will be community-driven, spec-sponsored-driven TC, the whole TC will be driving it through the LTEP, right, if we agree on the LTEP.
I think that's the difference in what Ludmila is proposing here.
Liudmila Molkova 00:58:16 So the driver… okay, so we don't have a driver at the TC.
And, leads, proposed leads, have the energy to drive.
The decisions made will need to be signed up by everyone, essentially, in the TC.
Well, through the hotel, because it's the foundation of the hotel.
Someone needs to drive the OTAP. Can… can they, I don't know, run the auto… sorry, write the OTAP before the project? Like, they don't need a project to… to create an OTAP.
And document the decisions, at least we can start working on this.
Tigran Najaryan 00:58:58 I think the question here is, can all the important decisions be made up front and agreed on?
using the OTEP, or there is an ongoing need for decisions to be made all the time, which would require, then, a TC member to be there continuously. It's not clear to me if it's possible to do that work in advance, like, without requiring an ongoing discovery and design.
Liudmila Molkova 00:59:26 I would imagine this needs to happen every week in a spec call, because it needs buy-in from maintainers as well.
And this, this effort, this enormous effort across all etel.
jmacdonald 00:59:40 My question is whether there's a, like, is there a technical figure in the community that's not here in the, like, in this group that we feel comfortable, like.
assigning the responsibility. Like, if there's an escalating sponsor, there has to be a trusted technical leader that's not us, and I don't see that person, or I don't know who it is, because… or who's volunteering to do this work.
And I kind of agree, like, this is gonna come up… this is gonna produce questions all the time.
Are we going to review them in the spec call every week? I was basically just saying what Tigray said.
Josh Suereth 01:00:21 Alright, we're… we're out of time. I do have a hard stop, apologies, so I can't continue to run. I'm gonna real quick, briefly say, Carlos, thank you for raising that JS Login API SDK. We'll have a stabilization review. We do have the, we do have a rotation for that, but, folks think about who could sign up to do that. Thank you for calling that out, Carlos.
Carlos Alberto Cortez 01:00:43 Yeah, let's continue that offline, because there are some details that we don't have time to discuss here, because I'm escalating one, so I will do a pre… a preview, or a pre-review. Anyway, let's talk in Slack, yeah.
Josh Suereth 01:00:56 Awesome, thank you. Yeah, so let's follow up on Slack, let's also follow up on Slack on system packaging. I think we need to do some more discussion, and probably high bandwidth in Slack, if we can.
Okay, thanks. See y'all.
Armin (Dynatrace) 01:01:09 Right?
