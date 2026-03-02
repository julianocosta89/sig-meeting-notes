SIG: Semantic Convention SIG
Date: 2026-01-26
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/S3EJlQkt18CIP7khtazgpdOfG4I3Z7KBaHLgk7iTL8eUP6nog-6ylV-Uy_sGmpY.u9WhQIaZ-Ie2v9_x
============================================================

## Zoom Recording Transcript

Sven Cowart 00:00:19 Check, check.
Liudmila Molkova 00:02:22 Hi, everyone.
Christophe Kamphaus 00:02:27 gloom.
Kai Levin (Ericsson ADP) 00:02:27 Hello.
Donal O'Sullivan 00:02:31 Smooth.
Liudmila Molkova 00:02:31 We might turn to run the call?
Okay,
So, we are going to discuss a few topics today. Please add things to the agenda if you want to discuss something
I don't know, fast, feel free to bring it before the topic I left here.
what's… Take a quick look at our PR board.
Okay, there is nothing that's ready to be merged. There are a couple of things that are blocked.
So… This one is still in discussion. There's some… Yeah, no update.
This one introduces terminology for PC protocol and framework.
There is a discussion… So, no update.
Okay, is there anything that we can move forward?
Need some more approvals…
So, oh, okay, so this is kind of interesting. It's probably the first precedent of people using stability…
beyond development, RC, and… Stable.
It's promoted to better.
I don't have any objections, it's just, A new president.
But it sounds like it's approved by the SIG, and it would be cool if somebody…
From the core crew also approved.
Christophe Kamphaus 00:04:46 Is it defined what beta means?
In terms of stability.
Liudmila Molkova 00:04:52 Yep, it's part of the specification.
So, like, every document has a…
Documents, data is a very normative document.
So it's… it's here.
Trask Stalnaker 00:05:08 Do you know what the motivation is for marking it beta?
Liudmila Molkova 00:05:14 I don't know.
Here, Christoph.
Christophe Kamphaus 00:05:19 Right?
Liudmila Molkova 00:05:22 Let's see… Is anyone from the Kubernetes SIG here?
Advertise the intention toward having those attributes as early as candidates soon.
Trask Stalnaker 00:05:42 I mean, I don't object to… it, I just kind of…
Curious the practicality of, what it means to move it to beta.
And maybe also, a worry that, That…
me, that says something about all of the other STEMCOM not being at beta quality that we have, as…
What do we call it? Development.
Liudmila Molkova 00:06:25 So… from the practical perspective, we would rather say, okay, go straight to RC.
Anything under that that doesn't say much?
Trask Stalnaker 00:06:41 I mean, it's certainly been the practice in this repo.
Liudmila Molkova 00:06:51 He, let's…
Trask Stalnaker 00:06:56 Let me see when they meet, maybe on…
Liudmila Molkova 00:07:04 I mean, we can bust in the chat, but yeah.
Trask Stalnaker 00:07:09 I can, yeah, I'll take that action item.
Liudmila Molkova 00:07:13 Thank you.
Trask Stalnaker 00:07:14 Yacht.
Liudmila Molkova 00:07:20 Bye.
Sorry, I've lost the…
I've lost the PR. I hope you remember.
Trask Stalnaker 00:07:29 Oh, I… Yeah, yeah, yeah.
Liudmila Molkova 00:07:30 Here it is.
Awesome, thanks. Okay, let's see, there is…
Yes, I think, Trask, you would also need to take a look at some point,
Trask Stalnaker 00:08:00 Exception recording…
Liudmila Molkova 00:08:02 Yeah, this is still on, I think, more in the… Logs sake plate for now.
Trask Stalnaker 00:08:12 Yeah, yeah. Well, I'll… we'll chat about it tomorrow.
Liudmila Molkova 00:08:17 Yeah, and if somebody can take a quick look at this trivial PR, please do, it's, Copilot.
And it just adds some metric section, and it's just pure, pure, corrections and beautifications.
Okay, thanks. I think we can move on to the main agenda.
Daniel Dyla (Dynatrace) 00:08:43 There was one more in the need approvals that I had hoped to talk about.
The, deprecation of the error.message.
Liudmila Molkova 00:08:51 Oh, right.
Daniel Dyla (Dynatrace) 00:08:53 Yeah, I guess the… the…
mostly I'm asking where that came from, because I was looking at the history of the issue and other PRs that attempted to resolve it. It looked like…
the issue to… or the PR to document the difference between error message and exception message was closed because it was stale, but I didn't see anything
any open discussion that seemed like it was going to be blocking or unresolvable in there, so I was wondering…
How… how the discussion changed to, deprecating this, as opposed to just documenting the difference.
Liudmila Molkova 00:09:38 Yeah, so, I'm sorry we didn't have this question and the issues. It came from the log-seq, where we are
Trying to deprecate span events and figure out what to do with exception attributes from this point.
And we've been trying to,
Like, map the difference between error message and exception message.
And, there are… quite a few confusions there. Let me find that.
discussion.
So… A few things that…
Let's say you report the log was error message.
Is… is error message different than the log body?
Where if you… report.
You don't report error message transpens, you don't report it on metrics. The only place you would report it is
Logs our events.
And, it's just, yeah, there is… it's not a blocking to document the difference, but this difference
It's subtle, and it's hard to document it, it's confusing.
It was hard for me.
Trask Stalnaker 00:11:01 And so we, on logs, we have severity error, and so the thought is that, well, generally your error message
Is… you log it at severity error, and then the thing that you log is that error message, generally.
Daniel Dyla (Dynatrace) 00:11:21 Right, okay.
I guess the reason it came up, I was talking with Michael Beamer, who is the… He's on the open feature side and helped with a lot of this work with the… when the SIG was still active.
And… we originally had feature flag error message, and we were told…
Trask Stalnaker 00:11:41 by me.
Daniel Dyla (Dynatrace) 00:11:42 generic one.
Trask Stalnaker 00:11:43 Sorry.
Daniel Dyla (Dynatrace) 00:11:43 We switched to that, and, like, it caused a lot of headaches because that had already been released by Open Feature, and now this is obviously… the new version has obviously been in use for, like, I think a year at this point.
The feature flag SEMConf has been marked as, I think, release candidate for something like 8 or 10 months, and…
The only reason I think it's not released as stable is because nobody got around to it.
So…
Yeah, I guess it's just unfortunate to have to… that the open feature community was frustrated when… when we brought this to their attention.
Trask Stalnaker 00:12:33 Yeah.
Daniel Dyla (Dynatrace) 00:12:34 So I guess my feedback is, is we can do this, like, if there's a good reason for it, then fine, but maybe we should mark feature flag as stable after this, because I think if we do this too many times, they're just gonna say, well, we're gonna go our own way and not follow the…
OpenTelemetry semantic convention.
There was already a little bit of discussion about that.
So, I'm already kind of in damage control mode over there.
Trask Stalnaker 00:13:07 So, we can definitely… I mean, I was checking… I thought we had marked… What is future lags?
So it's R… is it RC… okay. It's RC… except that error.messageO is…
Daniel Dyla (Dynatrace) 00:13:31 cylinder.
Oh, yeah, it was a… it was a development attribute, but the…
The overall, like, the feature flag
Document is a release candidate document.
Trask Stalnaker 00:13:47 Right.
To the point of them going their own way, I mean, that's…
not necessarily a bad, option in terms of, you know, we are trying to decentralize semantic conventions, so, I mean…
If they want to host the semantic conventions, I know, that'll be a topic later from Lyudmila's, kind of, 2026 planning.
But, I mean, we do want, actually, to decentralize, and feature flags could be a good thing for them to host, if that helps them feel like they have more control of it.
Daniel Dyla (Dynatrace) 00:14:32 Okay.
I guess as far as this change goes, is this… my… the core of my question is, is this actually… is this resolving real problems, or is it just…
easier to do this than documenting what we already have? Like, is there some reason that error message
actually doesn't work? Or is it just that it was difficult to document?
Liudmila Molkova 00:15:04 It's difficult to document because the head's a very difficult definition, and this is the problem on its own.
That it's… it's effectively impossible to explain the difference between exception message… well, it's possible, but it's… it's impossible to… to deliver the… the explanation. Between exception message, error message, and log error body.
So this is, from my perspective, it's a… design concern, and…
I'd like to fix it.
Daniel Dyla (Dynatrace) 00:15:43 Okay.
Trask Stalnaker 00:15:48 Yeah, we… we already… we have a lot of problems, when there's, like.
Two different… multiple different ways of doing something and modeling something in semantic conventions.
And so the more that at least the core semantic conventions can prescribe a common pattern.
We think the better.
Daniel Dyla (Dynatrace) 00:16:16 Okay.
Liudmila Molkova 00:16:21 And sorry for the headache we caused in the Future Flag community.
My impression that was that we didn't go stable at the time exactly because of this attribute.
It was the only one new.
And I… at least in my head, I kept it as a blocker.
Trask Stalnaker 00:16:41 Yeah, looking at the feature flags, I mean, that one is the only non-RC attribute, it's kind of clearly the blocker for stability, so, I mean, you could…
Maybe you could try to sell this as, hey, we're finally resolving that blocker, and you will be able to go stable after that.
Daniel Dyla (Dynatrace) 00:17:03 Yeah.
Okay.
Liudmila Molkova 00:17:08 And actually, if the folks feel comfortable, just send the PR.
Or, to, to mark everything stable.
Daniel Dyla (Dynatrace) 00:17:19 Okay, sounds good.
Liudmila Molkova 00:17:34 Okay.
Anything else on this topic?
Okay. So, I think there are, Sven, I think your topic is also, not a short one.
Like me here.
Sure. Suggest maybe 15 minutes.
Sven Cowart 00:17:54 Okay.
Liudmila Molkova 00:17:54 X.
Hi, how much time do you think your topic will take?
Sven Cowart 00:17:58 15 minutes is probably fine here. I doubt we'll get into the weeds of things in this call, so… should be fine. And nice to meet you, by the way.
Liudmila Molkova 00:18:06 Nice to meet you.
is Kai here?
Kai Levin (Ericsson ADP) 00:18:11 Yes, I'm here, hello. Nice to meet you all.
Liudmila Molkova 00:18:14 Nice to meet you. How much time do you think your topic would take? How much time we should reserve?
Kai Levin (Ericsson ADP) 00:18:19 But I would say, it will be a pretty short one, it's 5 to 10 minutes. It's mainly just to understand the current direction of this mental convention for the teleco alarm standards.
It's something that is a little bit ethical-specific, but I hope this is the right place to ask.
By the way, my name is Kai, I'm from an organization called ADP in Eriksen, and here we work with Commonwealth Microservices upon Kubernetes, and I'm working with the company engagement for our requirement of observability.
Where we are currently working on our journey towards open telemetry.
For our observability layer. I think I met many of you in QConn America this year, or last year, and…
Liudmila Molkova 00:19:04 Yeah.
Kai Levin (Ericsson ADP) 00:19:05 Really nice to see you all here again.
Liudmila Molkova 00:19:10 Thanks for coming.
Yeah, so then we… it seems we have right enough time for the, sorry, topics, and I'll, keep an eye on the time.
So I wanted to chat about Semantic Convention's roadmap, and it's nice to have a direction for all of us, and see what we are ready to commit to, and what we are not ready, and maybe it's the way to provide some focus around things, so that we can make progress on them.
So, I have a list with the help of some of you, with ideas of what we can, like.
Try to achieve in, 2026?
And, like, 2026 means probably, usually means KubeCon, the autumn edition, because after that, things go slow. So, we have, like, I don't know, maybe 8 to 9 months, to execute on this.
And, one of the suggestions I have is that, we try to stabilize whatever we are ready to stabilize.
And this is the list of things that I think that are feasible. I don't know about others.
So, it's not that if I… if it's not in this list, I don't see the opportunities, just I don't… maybe don't… didn't think about it.
So, and I would be, I sent some, Slack messages in the subconf channel I found for the SIGs to…
comment on… And provide their, there…
A few bullet points for the roadmap. Yes, Sama already replied, so let me paste it in the chat.
And, the goal is to, like, combine the goals from different SIGs and have, the full roadmap documented.
So some other things, that might belong in the specific SIGs, like deprecating span events, I think this would be,
I would propose it for the log's sake.
And, we have some other stuff that are,
That is interesting, and it's… it's… it could be important. I don't want to get into the details of what we should target, I just want you folks to think about what your… the SIGs you participate in would be interested to, have.
From the central, career, it seems we are actively working on the federated semantic conventions, the new schema, ability for everybody to define and publish their own semantic conventions, and for us to improve the publishing process.
So, I'm looking for the feedback, for the additional things from SIGS.
And, well, move forward. Is any, any, are there any, any thoughts here?
Okay, dan,
If you're a member of the SIG, please set it to the agenda of your team call, of your SIG call, and
please come back. Hopefully, maybe in a couple of weeks, we can collect the inputs and…
publish something.
Cool. Then, moving on to the next topic, Sven, network-specific semantic conventions. Do you want to present?
Sven Cowart 00:23:09 Yeah, that'd be great, actually.
Let me… Let me shrink my window down.
Give me one moment.
Okay.
Hey, everyone. So…
I mean, I think it probably makes sense to give a little bit of a context and history of what… why I'm bringing this up, and
Where we want to take it.
So I'm co-founder of a company called Lassiflow. We specialize in, helping NetOps people, in their…
need to observe their networks and infrastructure, and primarily in things like, traditional NetFlow and, S&P and TRAP.
So… One of the things that… One of the problems that…
we started, our users were asking us about is, it's great that I can see all this NetFlow traffic and, SMMP-related metrics, but we really also want to see what's happening within our Kubernetes clusters and see the traffic there and observe it there. And…
It quickly became obvious to us that, specifically in the open telemetry and,
I would say larger Kubernetes ecosystem, there isn't a lot of great tooling to instrument the network layer within something like Kubernetes, beyond some basic byte counters that you get, or CNI-specific,
implementations, like, that you would get out of Cilium.
So, what we started working on was, alright, if we wanted to, in an open manner,
instrument the network layer inside of Kubernetes clusters, how do we do that? And we ended up creating a project called Mermin, and it's an open source project, and inside of that.
What we were trying to do was align it with OpenTelemetry, and
So, we went through the work of
Taking our background and knowing how to,
utilize NetFlow data very, intimately, and applying it to OpenTelemetry and seeing, like, what is kind of the thing that we can
create an open telemetry that would make sense as a broader ecosystem. So… The idea is… pretty…
decently documented in the repo itself, I've linked to it.
there's a detail here I don't think that's appropriate to… probably just a sidebar conversation about why we decided to do it this way and not another way, as far as this… which signal we decided to use, which is that we went with
trying to expose NetFlow data as a trace instead of a log or something else, and the reason for that is that, it… a trace naturally fits into the definition of, what it is, which is, something that has a temporal
Aspect to it, meaning that there's a start and end time to it, whereas a log is usually just a singular point in time.
But I think the thing that matters here to this SIG the most is what are the semantic conventions that… or the attributes that we want to use to represent a lot of the data that is typically communicated about,
flow.
And… So with that, the idea is that we would introduce a new namespace, just called Flow,
Particularly, that's important, because it… it seems like, based on when we…
did a research into the network namespace and the systems namespace. Those typically describe
Things that, describe a singular entity that something is running on.
not this entity of… that exists, which is just a network conversation or a network connection, right? And so the flow namespace in OpenTelemetry would be
Attributes that describe the… the actual network connection, network conversation.
And this is largely based on and inspired by the existing
IP fix spec from IANA. So you'll see there's… in the definitions, we've called out which ones are borrowed from those, and
And kind of just made a little bit more modernized, I would say, and more clear, because some of the definitions, even in IENA, don't clearly describe the intent of a certain field.
So this is kind of the body of work here that we're talking about in the first part of it.
I… Lumel, I don't know if you want me to go into specifics here, on… on this, or…
Liudmila Molkova 00:28:28 Yeah, before we do this, I think the first question we usually,
try to answer is, does it belong in the central repo, or is it some component-specific thing?
And I… I would be looking at you to answer this question, but I want to share what the other…
That there is interest across the community in
network-level conventions. It's like, I've heard from, security people, especially during KubeCon, we had some discussions with people from Cisco who wanted to have some network-level metrics, for,
security reasons. And they might be slightly different, but maybe the attributes are the same, or the concepts are the same.
There's also a need from OBI community. They focus on network metrics, and they have some conventions on their own, and it would be
again, maybe it's not the same, but something similar, and it would be nice to find the common piece. So, we are discussing the roadmap, and, like, I think this project, at least some parts of it, belong in semantic conventions.
It's probably a big one, and it would need collaboration from a few SIGs.
Yeah, sorry for interrupting, but I'm curious if other people have… want to Dive deeper in any parts.
Trask Stalnaker 00:30:07 I… I tend to agree that the… like, for…
core networking stuff, that our story today is weak and, would, I think would belong in the core semantic convention repo.
I'm not… There's a… yeah, at least that part.
Maybe, yeah, there's a lot in here.
Is there… generally, how we move forward with something like this is creating a, semantic convention SIG?
Around making a proposal in the community repo.
And sort of… Outlining, you know, with something this big, maybe
If there's a way to even break it into, like, a Phase 1, Phase 2, Phase 3 kind of thing.
Sven Cowart 00:31:10 That's…
Ludmila suggested that, and that's what I'm gonna try to do here, is to break it into numerous phases. Particularly, like, this flow one is… it's probably not that big in its first phase. I mean, there's, like, vendor-specific attributes on flow records, too, that you could extract, but that…
then becomes a much larger project, I believe. So this would just be trying to identify what are the core central ones that are the most important, and start there.
There's also a very… another very large body of work, that just revolves around S&P,
values and trap values that, and Rob's on the call here with me, he's also the other co-founder of Velociflow, and, he… he's been trying to sort through our…
I mean, I don't know how many thousands of attributes that you're going through, Rob, and MIBs to…
RC Robert Cowart 00:32:05 The word cry is unfair.
What the.
Sven Cowart 00:32:09 I would say it this way, in my…
RC Robert Cowart 00:32:12 25-plus years of doing network observability. Our current schema is the third one I've built. They get better and better over time. But our opinion now is that, you know, we'd like to take that work and use it as a foundation of
bringing it into something like OpenTelemetry, because quite frankly, over my… what 25 years have told me, the…
Partially the bane of our existence is the fact that there are no standards around,
You know, around it, something as simple as.
network interface bytes in and out, you know, you can get that from flow records, you can get that from S-Flow countersamples, from SNMP, from streaming telemetry, all three versions of Cisco streaming telemetry, F5s, Juniper JTI, blah blah blah blah, etc, right? Like, so having, you know, needing to normalize, but give you an idea, like.
Our MPLS schema is based on over 130 different sources from 26 different vendors.
To come up with, like, what are the metrics for a label distribution path?
Right? And so, I think we have a really strong starting point, although, you know, of course, there's probably some things, decisions we've made in the past that we've already seen, there's probably a few tweaks worth making.
I think a lot of our concepts have been similar, despite, you know… I always think when people come up with similar idea from two diff… you know, totally independent, it usually means it's a good idea, like…
for example, you have some concepts around what are the more important metrics versus what are the outliers. We had a concept we called Core, Common, and Custom, which very much maps to that same philosophy. So, I feel like we have a strong starting point, especially for a lot of the stuff that would be in a metric signal for network.
That, you know, could serve as a foundation around which we can have some conversation and… and…
I may be naive in saying this, but I'm at least somewhat optimistic that there'd be an opportunity, you know, in the next 6 months or so to… to solidify around some stuff, so…
Trask Stalnaker 00:34:23 And so… Oh, good.
Sven Cowart 00:34:25 Oh, sorry, Trust.
Trask Stalnaker 00:34:26 Right.
Sven Cowart 00:34:27 what I was gonna say is just, thinking about how to break the work up, I mean, I was thinking about doing it in, like, alright, flow, comment.
Core or central.
attributes, right? And then you have these application-specific metrics, which I'm working with the OBI SIG to figure out, okay, how do they need to communicate the things that were in this project originally, because their intention is to take the OpenTelemetry
metrics project here, and specifically these metrics, and expose them inside of OBI. But these, to me, these are all describing something that is about an application, and not a network conversation.
And… and so… but they're clearly related, and…
So how can we structure these in a way that it makes sense to also…
relate them back to the actual network conversation, so I'll be working with them to figure that out, but there might be some things that, like, just some recommendations or ideas that come out of that work itself. That should also be smaller in scope. And then there's the SNMP and the TRAP work, which are probably
two different… potentially two different projects all on itself. But I imagine they will not require a new namespace, but will just be, new attributes probably within the network and the system namespaces.
I could be wrong, especially about traps, but.
RC Robert Cowart 00:35:55 I would personally say, if you… if your solution handles traps the way it should, it's a log. There's… I don't even know that there's any necessary extra conventions needed for a trap, per se.
But the S&MP would be the other… the, like, polling of metrics and stuff would be the one that's more…
Or streaming telemetry fits in that, but, you know, the metrics is the one that has a lot of need for…
To give you an idea, I think our total number of fields right now out of the network space is somewhere around 3,000-something.
So, you know, there's just a lot of…
A lot of detail, a lot of protocols, a lot of, you know, very network-y specific stuff, so…
Liudmila Molkova 00:36:41 Maybe the way… Go ahead, Trisc.
Sven Cowart 00:36:44 What I was just gonna ask is the best way to go about this, then, to create one of these, which you shared? Something like this, a project for Flow, and then I can document
all the… the initial phase one of flow, like you were saying, Thrask, and in here, and then that's the first step, or is there some better or other way that we should go about that?
Trask Stalnaker 00:37:08 Yeah, that would be my recommendation, because the… the hard… generally the hardest part of getting new semantic conventions off the ground is building a community around it that
cares, and that can cross-check each other's work. Like, if it's only you and your, you know, company coming and wanting to do it, that's not going to be approved as a project.
So, really need to find other people who are…
Domain, you know, have the domain knowledge to participate in those discussions and help to drive and own that part of the specification.
Sven Cowart 00:37:55 Okay.
Liudmila Molkova 00:37:58 I was going to suggest that maybe, the principle we can use, here to…
To break down it into phases that face…
During Phase 1, we address the things that are common across SIGs.
It's like, EBPF folks need something.
And can we identify what we need, what they need, and how we can help them there? Plus, system conventions have something, can we address that?
And this would also solve the problem of finding the community.
I don't.
Trask Stalnaker 00:38:41 And finding… and finding prototypes, producing prototypes.
Because that's another kind of blocker if we generally like to see prototypes in the OpenTelemetry community for these things, whether it's a collector, you know, receiver, whatever.
As opposed to just saying, oh, the vendors can implement this.
Sven Cowart 00:39:07 That makes sense, yeah. So, just so you guys are aware, this project, Mermin, is a EBPF…
agent and its entire intent is to try to, instrument the network layer. And, our intention is to donate this to the CNCF
We're just not there yet, as far as, requirements, or the requirements to…
go towards donating, which is, I think, 300 stars. So, I'm trying to grow this to reach 300 stars and then donate it to CNCF. And it's just… and it would be implementing whatever spec that we arrive at for as far as flow goes.
But that makes a lot of sense, so, what I'll do is I'll try to figure out, besides OBI, who are the other people that are interested in this, and,
Yeah.
That might be.
Trask Stalnaker 00:39:59 And they're…
Sven Cowart 00:40:00 you guys know other people, that would also be good, just knowing, like, new to this community and space, and so…
Josh Suereth 00:40:06 Actually, I… you should talk to me. There are folks at Google who do networking who are actually super interested in having, like… like, our mesh team was interested in having, like, mesh capabilities and things. So anything that, like.
Has to deal with from and to.
Okay. Whereas most of ours, from is assumed, and to is the span, you know, like, but when you have to deal with both, you're reporting, yeah. That, there's a group… anyway, reach out to me, I can try to connect you with those folks.
Sven Cowart 00:40:35 Okay, sweet, will do. You're in Slack, I'm assuming.
CNCF will give up on you.
Trask Stalnaker 00:40:44 And there may be… there may be some point at which, you know, there's the core things that would go into the core SEMCOM repo, and then at some point, like, with your, project, if you're doing, like, a
like, you said something like 3,000 metrics. Like, I'm not sure if we would take 3,000 metrics into the semantic convention repo.
But that kind of comes into this decentralization effort, where we are,
Where we want to support
a decentralization of semantic conventions where we can have the core things in the core repo, but then other people can extend those and define those, and it'll be discoverable and all of that, good stuff. So there may be… just kind of keep that in mind with your
Overall plan, that there may be some… a place where you could cut that and spin off the rest into an external community.
RC Robert Cowart 00:41:46 I mean, I think that makes a ton of sense, actually, for some of the network stuff, although there is a lot of core things, just because of the number of protocols, but, you know, it's always, the issue…
the network vendors have to differentiate themselves in the marketplace, right? So it's like, yeah, we have link aggregation, and then Cisco has 3 versions of their own link aggregation, plus Arista has some specialized ver- and they all have metrics with it that don't cross vendors, and…
I think those could be, certainly.
sliced out into something in the model you just said, that makes a lot of sense, yeah.
Liudmila Molkova 00:42:26 Yeah, I would be… I'm not sure how much time I can,
spend on this in general, but I would be interested to support this effort. They can provide, like, the semantic conventions perspective on things. You would probably need me… you'd need to teach me some networking stuff,
But I hope we can find some middle ground. That's… feel free to ping me on any specific, like, questions, or if you need to connect to people. I think system and process, system group is also interested in some part of networking.
Okay. And there is security semantic conventions, they are based on, I think they, they are the people who work on Elastic Common Schema.
And…
in the past, we've been checking, okay, if there is something in the semantic common schema as one of the input points to how we… we can define conventions, and if… if there is something in common. We can ping… I don't think anybody from Elastic is here to talk about it.
But, we can ping them, and we can ping the security chat. I hope they can provide some perspective, but let's see.
RC Robert Cowart 00:43:45 We know that team extremely well, so…
Liudmila Molkova 00:43:48 Nice.
That's awesome.
Cool, then thanks a lot for coming, looking forward to the collaboration.
Sven Cowart 00:43:56 I have… I have one more question, real quick. One thing that… and,
This is my point, let me, or you can have it up here. That prefixing flow attributes, this is just something that, when you're talking about an entity that's a connection, it's… you need to oftentimes describe the source and the destination of that attribute, and there's not really great
guidance around how to do that. There's that one guideline hidden somewhere deep down that talks about prefixing client source, and how to do that.
And it suggests that you use the pattern of namespace.client slash source.attribute, or the rest of the attribute name. So it's splicing the attribute name by namespace, and then whatever follows, and that's about it.
quite frankly, I find that
kind of confusing when you're talking about something that is a connection, because you think of it as in, okay, what is the source and what's the stuff in the destination? So I don't know how to go about
This probably needs to go with the flow project and proposal, but suggesting some type of guideline around how to
decorate these other attributes with source and destination as a prefix to use as a standard prefix, or if it's not the first prefix and we want to keep following the client-server guideline, that's fine too. But I think we just need to take a little bit more of a definitive stance on that.
aspect of it.
RC Robert Cowart 00:45:34 Let me just add one thing to that real quick, Sven. I think part of where the challenge comes in is some of the recommendations are written in a way, assuming you're using the perspective of a network endpoint.
Liudmila Molkova 00:45:48 But if you're a router in the middle of the network carrying that particular flow, then…
RC Robert Cowart 00:45:54 you're not either one. Both ends of it are remote to you, you're just the forwarder. And sometimes those recommendations don't always apply the same way, because it's a different perspective, if you will, you know?
Liudmila Molkova 00:46:10 Yeah, our conventions are frequently modeled around either just client or just server communication, and we… there is a lot of guidance we can improve, for sure.
But if you can send a link, I asked in the chat, or create an issue, it would be a great feedback.
Sven Cowart 00:46:30 I can do that. Where would I create the issue for something like that? Which rich repo? Is it the community repo, or something else?
Liudmila Molkova 00:46:36 Semantic conventions? If it's about semantic conventions.
Sven Cowart 00:46:40 Will do.
Trask Stalnaker 00:46:41 Community repo is just for the project proposals.
Sven Cowart 00:46:45 Got it. Alright.
Liudmila Molkova 00:46:49 Cool, then thanks a lot. Anything else on this?
Awesome.
Sven Cowart 00:46:57 Hi.
Liudmila Molkova 00:46:58 Do you want to talk about, telco alarm and TLS semantic conventions? Do you want to present, or…
Kai Levin (Ericsson ADP) 00:47:04 Right, I can present it, actually, but you can continue to show the screen, just as a reference.
Great, yes, thank you so much, I appreciate that.
Yes, so the last 10 minutes, I have two questions from Ericsson's side. It's regarding the alarm handling and also the TRS logging, so let's start with the first one.
So, in our product, we have a very common use case for telecom, that is alarm history logs for classic fall management, storing and curing the historic of alarms, and this data is stored in a search engine behind the front-end dashboard.
And the alarm handling follows telecom standards, like the ITU-TX.733. We already have a microservice that implement this standard today.
But since now we are looking at how to map this into OpenTelementary as part of our OpenTementry journey.
We would like to…
Avoid inventing error from specific naming if there is a better shared approach in the semantic convention.
And we see that in the auto docs, the guidance is that company-specific attributes go under, com.vendor.
namespace, but in our case, the parameters come directly from the telecom standard and not Ericsson-specific. So today, we prefixed many of these fields with X733 dot in our own schema.
So, the question would be that does OpenTelemetry have, or plan to have, semantic convention for alarm handling that align with the technical standards, like the ITU?
dash tx.733 or 3GPP, and if not, what would be the recommended way for us to propose a such domain-specific set of conventions, or they are not just…
So they are not just, Comp.Erickson does something, but something other technical companies can also reuse for technical use cases.
Yes, that was the first question.
Trask Stalnaker 00:49:22 My first…
Thought is, that this sounds like, one of those domains that would work well as a kind of a decentralized effort.
Hosted somewhere else.
I don't know if there is, an…
Any kind of open source… existing open source… Org around telco… That.
Would be a good place to host it?
You could also… host it as Ericsson, but generalize things to telco,
But my, my first thought is this is,
feels like one of those things… pieces, domain-specific things that we would want to decentralize and not necessarily host in the OpenTelemetry Core semantic convention repo.
Kai Levin (Ericsson ADP) 00:50:30 I see, I understand. Yes.
And, if we would like to, like, propose as such to miss a specific set of conventions for, let's say, the telco companies or the telco users, what are the ways for us to do it? Since it will not be a part of the semantic convention for open telemetry, but how…
How would the process look like?
Trask Stalnaker 00:50:57 Ludmila, do you wanna… do you probably know more about the decentralization, effort status?
Liudmila Molkova 00:51:03 Yeah, so there is a technical aspect, right, and you would be able to… You can have.
you would create a repository of some sort. It can be open source, closed source, doesn't matter. You would describe the conventions there. You can take dependency on up and telemetry conventions, if you want to, from that repository. This is, like.
a little bit still work in progress, but we should have some good examples and everything pretty soon, if I'm not mistaken, looking at Josh now.
But essentially, you would host them on a separate repository, you can publish your conventions, and you can provide a thing called schema URL. It's, it's, part of the telemetry payload. It goes with instrumentation scope, and it says where your conventions are hosted.
And at the schema URL, it tells people, okay, this is not up in telemetry, but let's say it's Ericsson or Telco.
And then you would have your own governance around this project, which is actually good for a year, because you can make progress as far as you
As fast as you can. You can,
you would have experts there, right? So, like, you're the only expert on this topic, in this group, probably. I'm sorry if I'm mistaken, but there are very few people who know this stuff.
And we would not be able to provide any meaningful contribution to this topic. But you would have your own experts working on the thing, and you will be able to stabilize at your own pace and publish them.
On your own.
Kai Levin (Ericsson ADP) 00:52:48 I see, I understand. Yes, thank you so much for so detailed information. And just one quick question, so this thing that you… or the space that you are mentioning, is this some kind of… does it have some kind of connection to OTL semantic convention? Like, how do people find that?
This space that you mentioned?
Liudmila Molkova 00:53:09 the… the space?
Kai Levin (Ericsson ADP) 00:53:11 Yes.
Trask Stalnaker 00:53:12 The discovery mechanism of decentralized semantic conventions, is that…
Kai Levin (Ericsson ADP) 00:53:19 Yeah, so that people know that we are working on such effort, and… because we want to be as close to the open source community as possible, and also, of course, to the open elementary community.
Liudmila Molkova 00:53:32 We can definitely, start…
a document in… well, I'm saying definitely, but that's my point… opinion. We could have a document in semantic conventions that, like, some sort of a registry that points to other
Conventions, other registries, or we can make it part of Autel are your registry.
Oh.
Kai Levin (Ericsson ADP) 00:54:00 asking.
Liudmila Molkova 00:54:01 So, let's see, there is a registry here.
All the time.
Trask Stalnaker 00:54:09 So I think this is a good way to…
For users to know about it.
I think another option is, like, you're kind of also… part of your question, I think, is about…
Getting… finding contributors in the, to build this.
Which… I… I think…
would… we would probably support a blog post from the OpenTelemetry blog, have to…
Confirm that with the, the blog folks.
But I know from semantic conventions, we do want to support this.
Kind of decentralization, so… And I think that is a common concern that people have around decentralization, is
Lack of discoverability and community… building community.
So if you have suggestions, you know, of things you would like support from the OpenTelemetry, like being able to post, you know, a blog post, things like that.
feel free to reach out. I can… I'm on the governance committee, I can interface with the blog folks, if there's any, you know, to confirm that kind of thing.
RC Robert Cowart 00:55:35 Kai, I will also speak…
I will also put my hand up and say the downside of being… doing this network stuff so long is, like.
I knew exactly what you meant when you said X733, and I'm happy to also, you know, contribute to whatever your effort is, just to have, you know, some other external source that's involved in it, you know.
It's scary how much of it, actually, I remembered when hearing that, so… Yeah.
Kai Levin (Ericsson ADP) 00:56:07 Thank you so much, Robert, and thank you so much, Drask, for the inputs.
That'd be really helpful.
Yes.
Great. I think I got a very good answer on the first question, so we have 4 minutes left. I will jump on the second topic. It's quite connected to all of the discussion we just had regarding the network-specific semantic conventions. It's related to the security aspect, so…
We have another study where we try to map our TRAS-related log fields, for example, the TRAS handshake failures and certificate issues to the public hotels and other conventions, and we noticed that there were a few attributes we care about are not actually present in the current hotel model.
We know that with the ECS, the Elastic Common Schema, they seem to cover more of these tier S
parameters, or the, yeah, the details related to TES.
And, I know that there was an announcement a couple years ago that ECS would cut coverage into all the elementary semantic conventions, and…
We know that Elastic has provided a lot of input here, and our impression today is that ECS seems to still have a broader coverage in some of the TRS areas than Autel.
So the question is…
what is the current thinking in the SICK group on closing these gaps for TRAS and certificated related logging?
Is there an active plan to reach priority with ECS in this area, and what is the…
Preferred way for our Yeah, like, users from us, for example, to…
Feed concrete missing attribute proposals into This kind of conversation.
Trask Stalnaker 00:58:00 So, we have a, semantic invention security SIG, which… is… Part of their, project.
I think covers these TLS,
Attributes, and I know, was part of Elasticsearch… it's Elasticsearch wanting to bring more of the security-focused things from, ECS into OpenTelemetry.
Unfortunately, that SIG is… has kind of, dissolved, isn't meeting anymore, and so need…
Basically, need new energy, new people who want to, help to drive that work.
But there… I think… it…
is work that we would support within OpenTelemetry. We've sort of already said that, yes, this is something that we want to…
Under the OpenTelemetry Community umbrella.
Kai Levin (Ericsson ADP) 00:59:20 Yes. Yep.
Sven Cowart 00:59:22 There seems to.
Kai Levin (Ericsson ADP) 00:59:22 Thank you so much, Chris.
Sven Cowart 00:59:23 Thrask, are you saying the security SIG is the one that went dormant?
Trask Stalnaker 00:59:28 So the… yeah, it's confusing. We have a security SIG, and we have a semantic invention security sig.
Sven Cowart 00:59:35 Okay.
Trask Stalnaker 00:59:36 Yeah, so Security SIG is around, like, supply chain security, the CVEs for open telemetry software.
Sven Cowart 00:59:46 I see.
Trask Stalnaker 00:59:47 that we create. The SEMConv is about capturing security stuff via SEMConv.
Sven Cowart 00:59:57 It seems like there's gonna be a lot of overlap between that and
What we'll be working on with the network.
semantic conventions. I just, I wonder if it makes sense to…
start up something new again. I know the OBI team discouraged me last time around trying to restart the network SIG group, because apparently it's pretty dormant and has been abandoned, too. But maybe it makes sense to do something around that, where it's like, this is network and network security SIG.
to… I'm not sure, but…
It seems like there needs to be a place for that if we're gonna pursue these things.
Liudmila Molkova 01:00:38 Yeah, and it would make total sense to either restart it,
if there is, like, if there are other people, if it's beneficial, right? It doesn't really matter which repo you're hosted in, or the name of the SIG.
The one idea could be that, okay, there are central conventions that live in semantic conventions repo, and maybe Kai would also be interested in some of them.
And maybe the network, repo would host other conventions that are less, specific to… less… less common.
And maybe OBI would host them, or all of them.
Josh Suereth 01:01:18 I also want to call out, there's a networking set of instrumentation that was done with eBPF that was donated to OpenTelemetry, and that is mostly… from my understanding, there's not a lot of activity there.
And so, I think you could revive networking semantic conventions, and networking instrumentation in general, like Libmila's saying, without that repo. Like, when OBIs, like, don't revive networking, I think they mean that specific repo and that implementation.
Sven Cowart 01:01:44 Oh, I see what you mean. They were saying…
Josh Suereth 01:01:46 Okay. Yeah.
Sven Cowart 01:01:47 Because.
Josh Suereth 01:01:47 Yeah, so let's not confuse those two, because I think… Yeah, go ahead.
Sven Cowart 01:01:52 So you're saying the… the SIG, the network SIG, was tied to that… that network project? Okay.
Sorry, I didn't mean to cut you off.
Liudmila Molkova 01:02:05 We are out of time. Yeah, sorry.
Thank you all. Let's talk on Slack if we need to.
Trask Stalnaker 01:02:11 Thanks, everyone.
Liudmila Molkova 01:02:12 Thank you.
Kai Levin (Ericsson ADP) 01:02:13 So much. Thank you. Have a nice day.
