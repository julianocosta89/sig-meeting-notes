SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-05-13
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Ruediger Schulze (IBM) 00:04:44 Hey, Antoine.
atoulme 00:04:48 There you go to meet.
Find a way to remove that guy.
Ruediger Schulze (IBM) 00:04:52 Yeah, what is Fireflies?
atoulme 00:04:55 I'm not interested in that.
Hmm… Oh.
Here you go.
You continue to, FF leave? Okay, yes, I can do that.
Much better.
Ruediger Schulze (IBM) 00:05:31 Okay, very good.
atoulme 00:05:32 Oh, man.
I just don't like those things, I don't think they're very valuable.
Alright. Bye.
So… Lots happened last week, I just wanted to make sure… you, you caught up already, that's great, thank you.
Ruediger Schulze (IBM) 00:05:47 Yeah, I think I'm up to speed to the discussion.
atoulme 00:05:52 So we had a topic specifically for you, so that I can talk about right this moment, about the fact that this time is not really working for you.
Ruediger Schulze (IBM) 00:06:02 Yeah, And this is two different reasons. I was also traveling a lot, that might become a little bit better.
Maybe this… so, previously, we had this meeting one hour later, that seemed actually to work better Wednesday still, but, one hour later.
Maybe that's one proposal that we could put for vote, a different day… .
atoulme 00:06:31 We moved it earlier for someone, right? I think it was Katrina?
Ruediger Schulze (IBM) 00:06:35 I think it… yeah, it was for… Angela.
atoulme 00:06:44 Angela, sorry, not Angela.
But she's not showing up these days.
Ruediger Schulze (IBM) 00:06:50 Yeah, right.
atoulme 00:06:52 Anyway.
Ruediger Schulze (IBM) 00:06:53 Well.
atoulme 00:06:55 Okay, so let me share… Here, the duck, and we're gonna get started. Here is the dock.
If you'd like to bring…
Ruediger Schulze (IBM) 00:07:05 Also, to go there. Choose it.
atoulme 00:07:11 Okay.
Alright, so we're… We started with an AI boat, we kicked it out, we're good now.
Please put your information in the attendees, if you'd like.
the, our agenda today, so we discussed last week.
Can follow up on that.
So, let's start first with Undmila, because she's giving her, you know, she's giving her time away to discuss with us, if that…
Ruediger Schulze (IBM) 00:07:43 Yeah, I appreciate this very much, you know.
Ludmila Molkova 00:07:46 Yeah, I appreciate you being interested, and I think this is a very well spent time. So, I can give you an overview of the split we are doing in GenAI, and walk you through the steps of how it happened, and we can talk about any specific Questions. Okay, cool, so I'm going to share my screen.
Okay, so… What do we have done?
And the reason why we've done it is because we want to move at a different pace in Gen AI space. We want to maybe version differently.
We still are under up on telemetry governance.
In case of mainframes, I don't know, maybe you want to be under IBM governance. It's totally possible, it doesn't matter.
How things look like, We still depend on the open telemetry semantic conventions, and we express it through a manifest.
That says, okay, there are some hacks here, we're working on fixing that, but essentially, we're saying we have dependencies, the… this is our, Dependency on the core repo.
We have a thing called schema URL.
If you… feel free to interrupt me whenever…
Ruediger Schulze (IBM) 00:09:22 Yeah, actually, just first question, and as we are in the space of, So mainframe is actually strong on virtualization. I know we don't have virtualization yet.
And the semantic conventions being represented, but let's assume we move ahead with mainframe-specific semantic conventions. We may have a point of view on virtualization.
what would be actually your proposal to represent this? Because somehow they go together, but virtualization is its own domain, right? It's an own domain space. Would this be a separate repository? And if so, how would we represent that we maybe depend on the base, but we also depend on virtualization as a… as a concept.
Ludmila Molkova 00:10:14 So… You would like to have virtualization as a separate entity from the core semantic conventions.
Potentially.
Ruediger Schulze (IBM) 00:10:23 Yeah, potentially, because, you know, we discussed this last year on the semantic convention SIC call at some point, right? There are some proposals, but, I think, you know, they are not yet as part of the base semantic conventions available.
Obviously, from a mainframe point of view, we have certain concepts of representing virtualizations. We also would like to get this generalized across the industry. It's a general concept, obviously.
So we could potentially kick this off as a separate… repository, semantic conventions for virtualization. But then also the question comes of.
How would we… how would we include this again as a base for… for mainframe definitions that, you know, are higher in the stack, for instance?
Ludmila Molkova 00:11:16 Yeah, so let's assume it's done as a separate repo.
So this is the way to express. You can… currently, you only have one dependency. We are actively working on making more than one. So there would be a core repo, there would be a virtualization repo that may depend on the core one, up until.
Ruediger Schulze (IBM) 00:11:38 Right.
Ludmila Molkova 00:11:39 And then there could be a mainstream repo or component within the virtualization repo that depends on both.
Like, you can, like, think about these things as libraries. You can just.
Ruediger Schulze (IBM) 00:11:53 Come by.
Ludmila Molkova 00:11:53 them together.
Ruediger Schulze (IBM) 00:11:55 Okay, okay, good.
And… Yeah, so… obviously, why we want to represent virtualization concepts of the mainframe that's all specific to the mainframe, I think we want to keep, you know, virtualization as our own domain, yeah. Okay, good.
Ludmila Molkova 00:12:18 Cool, I'm going to dive a little bit more in the tooling part. Is it the right thing to do?
Ruediger Schulze (IBM) 00:12:25 I think so, yes, yeah, yeah.
Ludmila Molkova 00:12:27 Awesome.
Cool, so then, okay, there is this manifest. It says, okay, I'm in development, there is this schema URL, this is what you would attach to the telemetry so people know where to find it.
As a part of the thing.
Sorry, what happens during… when we release it?
We're… I'm going to show you something… If GitHub cooperates. So let's imagine I'm releasing this repository.
as a part of the release process, it would produce two things. First, the manifest, Let's open it up. This is what, would be published on the schema URL, so when users hit the schema URL, They would see this file.
It contains the link to… The full schema?
And, this is the other file we published during the release process. And it contains everything, like, everything you define, like, for example, if you do the Uber package for virtualization and mainframes, it probably would contain both.
And consumers can use it to… for many reasons. You know, when you, write your query, this could be available to your, I don't know, agent that writes the query, or you can hover over some attribute name, and your UI on the backend would be able to show you the brief. So, this becomes, like, the living documentation attached next to the telemetry.
And the cool part is that currently it works mostly for the core repo.
Because everybody… every vendor has some understanding of semantic conventions, whereas the schema URL and vendors may be hopefully supporting the schema URLs They can pull this file up.
Cache it, of course, and then use it as a leaving documentation for your specific telemetry.
Most of these things are… automated. So I've shown you the manifest, there is a bunch of tooling, that works with semantic conventions.
So, let's, let's take a few, We have some things to help you write conventions. For example, we can run Weaver Registry Check. Weaver is the tool that works with semantic conventions, allows to model them, check them, and whatnot.
So, it allows you to, Run certain policies, and it's hard to see here, but these policies actually come from from this repo, it's the common repo, you can just include them from their mode.
And it has backward compatibility policy, like naming conventions, stability, and it's the default checks you would run If you want to… Follow same principles as behind the semantic conventions.
There's more.
you can generate docs in the same way as we generate them in semantic conventions. There is a little bit of ongoing work, so for example, here we use local templates. We will have a generic template here as well, so you don't need to write this Jinja unless you… you want to. So this is the templates behind the documentation.
I'm sorry if I… if I'm going too deep. Should I stop?
Ruediger Schulze (IBM) 00:16:42 No, actually, appreciate that, because it makes more clear on what happens behind the scene, and I think we also have a few folks on the call who haven't seen us yet, so appreciate that, thanks. Thanks a lot, Mila.
Ludmila Molkova 00:16:57 Yeah, duh.
Other parts are pretty much repetitive, right? We can, package, generate, and so on. Essentially, it's something you can try today. The process is not well documented. If you… have any specific date in mind where, like, you would like to start playing with it, I can prioritize, like, writing the queue steps down and making sure we… We can.
Ruediger Schulze (IBM) 00:17:31 Yeah, so here's what I… wanted to suggest, or also what I want to do. Obviously, Antoine, you made the request for the semantic conventions mainframe repro. I assume this to go through in a couple of days.
And actually, I just wanted to… so from a mainframe point of view, we have the HMC that has a… it actually already has quite some rich telemetry, but I think it would be a good starting point to somehow play with this approach of having semantic conventions being defined for the… from a mainframe platform perspective. So… just, you know, trying to, on the basis of the GenAI, to put a, you know, populate this new repository. That would be also one of my questions. If I would, you know, take GenAI as a basis.
Maybe there's, you know, certain artifacts that, you know, are most reasonable to copy over, then, if you have some thoughts on that, that would be great. And, I'm… I would say I'm more or less familiar with how the semantic conventions process works from, you know, these previous activities.
And, Then it's essentially, you know, getting it to run, and then at some point, it would probably be good if, maybe you or somebody else from the semantic convention essentially could look over, assuming that all the tooling already works, but could look over if we are kind of, like, what we are doing is reasonable.
And then we… I think we can go off on our own.
Ludmila Molkova 00:19:11 Yeah, that sounds great. So, from the process of doing the Gen AI stuff, we identified a few issues that are, it would be better to… for us to fix. There are some workarounds for them in January, but if you copy it over, you would also copy over all the hockey solutions for it. It might take us a little bit of time, but we are actually working on it.
And, Still I would love to understand the timeline you have, so that we can…
Ruediger Schulze (IBM) 00:19:49 So, if things go… okay.
I have a little bit of time in the end… end of… end of May, beginning of June, obviously, some vacation time.
Which may allow for digging into this topic more, and then it's probably more on the go, through June, July timeframe, right?
Ludmila Molkova 00:20:16 Okay, so then, what… I can do… is I can… Right.
So, if I understand correctly, you don't… you won't get to it till June.
Ruediger Schulze (IBM) 00:20:30 Yeah, yeah. And, you know, if you write something, you know, maybe this doesn't need to be very extensive in the beginning, but maybe the key points that, just to, you know, maybe if you know about pitfalls.
Then, you know, maybe avoid this or that, or do that and that.
Ludmila Molkova 00:20:48 Yes, totally. I will write it down. There will probably be, so, in terms of artifacts, right, you need… you mentioned that, what you can reuse. Ideally, everything reusable, we would put here.
Ruediger Schulze (IBM) 00:21:00 Yeah, yeah.
Ludmila Molkova 00:21:01 And then, it just didn't happen yet. This would also be a good opportunity for me to list down those things that should be there.
And maybe follow up on at least some of them.
So, Let's do this, yeah, I write it down, I'll leave a follow-up, so I will follow up on them, for real, and I'm… I'm relatively… I have a high, high… I'm confident that you will find some new issues, and I will definitely be there to help you fix them.
Ruediger Schulze (IBM) 00:21:41 Okay, yeah, you know, we have been in contact previously, yeah, so I appreciate that, Lyudmila. I'm sure we will find ways to solve that.
I have a couple of questions, just more on the process. Obviously, from a mainframe perspective, there's not much there yet in the base. Also, this needs to be reworked. I think the way I understand it from a… From a GenAI perspective, we would deprecate in the base the mainframe namespace, we would do the same with the COS namespace.
And then for the PR for the transaction processing system, which has been open for quite a while, I think my… at least my current view is we will integrate this into the mainframe, repo… Then, as we move forward… So, obviously, this would then also imply, as we go through the process, to, you know, pull over the namespaces into the new… repository.
Ludmila Molkova 00:22:49 Yeah, if that's what you want. This is one of the bumpy places.
Ruediger Schulze (IBM) 00:22:52 Yeah. So far.
Ludmila Molkova 00:22:53 Okay, there is just one attribute here.
Which makes it much easier, and…
Ruediger Schulze (IBM) 00:23:01 It's not so much, and it's… I think, the way I… how I understand the process, you move these fingers over, and then, you know, everything is then maintained in one place, obviously.
Ludmila Molkova 00:23:17 Yeah.
Yeah, this, this would make sense. So, yes, you would have some dependency on the… the core repo, and, you would deprecate this thing specific here. So, and there are… actually, those are… attribute groups. One thing you probably should know about is that we have a new syntax that's a little bit more friendly than this one, I'll share some docs, and we even have an AI skill that converts the old syntax into a new syntax.
So you can get some help. Given that you have essentially one entity and a bunch of attribute groups, and a couple of attributes that should be trivial.
Yeah. It's just… you don't have to convert, but at some point, we will pull the trigger on V1, maybe in, like.
Year.
And so it's… it makes more sense to start writing in V2 syntax.
Earlier, once you have just a few things, and it's easy to convert them later.
Ruediger Schulze (IBM) 00:24:28 Okay, sounds good.
Ludmila Molkova 00:24:31 Yeah, so you would deprecate, you would move things to the new repo. There are some bumpy things for this right now, but we are solving them for GenAI, so hopefully by the time this happens, we would have a good solution for you. It's workaroundable, so it's not the end of the world.
And there are still parts that we are, going through in GenAI, for example, the release process and publishing the schemas.
Well, I'll… Be ahead of you there, and you will… we will stay in touch and just share what we came up with.
Ruediger Schulze (IBM) 00:25:14 Okay, so… I'm just thinking through the process. So, these repos, they have their own actions, they have their own build workflows, obviously, so the GenAI one has its own build workflows.
This is something we need to take over.
And, you know, adopt accordingly.
And… Yeah.
Okay.
Ludmila Molkova 00:25:40 Yeah, so what? I'm thinking how we can help. We can, in theory, have a template.
So the, the… Trask, who set up this repo, he knows all the process. I think we should involve him at some point, and, like, probably he replies to you on the mainframe repo request.
Ruediger Schulze (IBM) 00:26:01 Okay.
Ludmila Molkova 00:26:05 But he would know the process, what's important. Maybe as a part of this writing, I can create a list of things that R… important, so, for example, the checks and the… some kind of specific CICD checks, but there are… there is more, there is, like, I don't know, dependency and supply chain attack detection and whatnot, security and stuff.
Ruediger Schulze (IBM) 00:26:29 Okay, okay, yeah.
Ludmila Molkova 00:26:31 rainbot.
Ruediger Schulze (IBM) 00:26:33 Yeah, that's obviously important to get all in.
Right.
Ludmila Molkova 00:26:38 You don't need to do it right away, right? So this is the, it's an ongoing process.
Ruediger Schulze (IBM) 00:26:45 Okay, good.
Maybe to the audience on the call, maybe Jim or Richard, Any, any other questions?
Richard Nikula 00:27:00 I don't have anything.
Other than, why is Greg here? I'm pretty sure he said he wasn't going to be here today.
But, on that note.
Jim Porell 00:27:10 And I was trying to talk over mute, so, No, it looks good. We want to, you know, we're trying to more expeditiously make progress on some of these, you know, conventions, so I think this is, a big help. One question I had, and I think you kind of said it, but that Weaver, that's looking for name conflicts, if I'm not mistaken, that we're not using the same names for something different that somebody else is using, okay? And that can also help us, I would assume, because we would embrace or adopt some of that naming, too, where, like, as Rudiger pointed out, virtualization for us is gonna be common 80% of the time, and maybe we have small extensions, but… We should reuse the existing versus reinventing it, so…
Ludmila Molkova 00:28:00 Yeah, so the weaver would not, like, block you from reinventing things.
Jim Porell 00:28:05 I agree with that, yeah, yeah, yeah, yeah.
Ludmila Molkova 00:28:08 Yeah, but… It would provide the tools to check, and the backward compatibility check is another one, because we consistently, Constantly remove things and forget about.
They absolutely need some, checks for this. The other part Weaver can do, it can… you can run it as a conformance test. It has live checks, so you can give it the telemetry, and it will, Assert that it follows semantic conventions.
Jim Porell 00:28:42 Huh?
Ruediger Schulze (IBM) 00:28:47 Okay, very good. So, thanks, thanks a lot, Milai.
Jim Porell 00:28:50 Yeah, thanks a lot.
Ruediger Schulze (IBM) 00:28:51 I don't have any other questions right now, but I suppose the minute I start with this, or we start with this, then we will have lots of questions to come.
Ludmila Molkova 00:29:01 Yeah, totally fine, and feel free to come to SunCon if you already come in, feel free to come to Weaver if you think we need some deep discussion on mainframes, I'm happy to join this call, and we will… Figure it out.
Cool, then, I owe you the follow-up with the documentation on how to do this, The brief one, and we'll get from there.
Ruediger Schulze (IBM) 00:29:26 Okay, yeah.
Jim Porell 00:29:27 Antoine, thank you. Antoine, thank you for, generating this. That was really helpful.
atoulme 00:29:32 It's all, you know, frankly, like, she… so she brought up this… this point, because this has been directional for some of the conventions for, like, at least 6 months, right? She… she's been working really, like, hard to, kind of, work on this delegation model, and I think it's, I just… so, I don't think mainframe is actually special here. Collector is also probably going to be going through that, there's… so, it's also, like, very reassuring that you're not just, going to have to do all sorts of discovery by yourself, like, when… when she mentions you're going to find bugs, I think collector will find bugs too, and others as well. So, this is a big maturation, and yeah, we can… We can definitely call onto Lumila to help. I, I… yeah, the administrative part of this, of just getting the repository, did not go as well as I would have hoped. It's just taking me longer than I like to get things done on that.
And some of it is just completely me, right? So I tried to… and this is an update I wanted to give you all. I tried to unarchive the existing repository you already had.
And then they're like, oh, can you unarchive it, but also change its name? Well, if I do that, then we will delete the archive at the same time, and we actually might lose the contents of the old repository.
So I stopped everything, I put it back to them as an action item for the GC to build the repository, which they do in a different way. So that's going to take just… Maybe a couple days, like Rudiger said. So, as soon as that's done, I think we're clear to engage on working with the Semantic Convention's litigation.
We might need a… Yeah, we can talk about, like, some of the elements of what goes in that repository, like… Changelog, and… all those things, like, really did not think that through.
I don't know how organized we want to be about it, or we just, like, start just putting a bunch of issues in there, and just pine on as fast as we can some… some things, we did not discuss any of the actual collaboration of building those submitting conventions. I know it's been a lot of rigor in the past, right?
there was a discussion last week about some of the different things. So Jim had a list, very quick list, of, here are the different things that a mainframe is going to care about.
Right? So, maybe we could also… When we go about it, just find an issue per area.
So, dbido database, the parallel sysplex discussion, the clustering as part of that.
Virtualization concepts, we already are going to be based off that, so anything we need to extend.
Message queuing, anything that we need to extend from there. Transaction processing with some KICS, extension.
and IMS extensions, right? So… A lot of what we're going to do, I think, is also going to be between core and extensions, from what I discussed with you all.
And that might, That might feel like we're blocked sometimes, because we have to kind of go back to the transaction.
Some of the conventions, fix something minute.
And then build on top of it.
So… But if we have some sort of a framework to attack this, with, like, being able to also parallelize some of the work, it would be interesting in my view.
A thing that can help with, like, anything related to IBM MQ, which I built for this. We could try to bring it over on top of the transaction, or message, or… I'm not sure which place this would make more sense.
And, anything that we can get for free there, that would be great, I guess.
Ruediger Schulze (IBM) 00:33:15 Yeah, so, it's actually interesting.
Before I, you know, comment on messaging and databases, just, so the way I was looking at initial content for this repo, obviously we have still, you know, some of the span information from TPS to go in here.
atoulme 00:33:34 Yep.
Ruediger Schulze (IBM) 00:33:35 Same what I said, I would see value to start from… from an HMC point of view, to have a couple of resource definition or entity definition, being… being taken over.
atoulme 00:33:47 Okay.
Ruediger Schulze (IBM) 00:33:48 will be added. Messaging is actually… and also database… I think messaging sick is currently paused, right? Database, I'm not sure what the status is. But, We also had discussions around that. Would be interesting if this lands down here, or would that be actually a separate domain, a separate repository? It's probably something we want to explore.
And also, you know, just on… in terms of, Virtualization, I think we had previously discussions on the semantic convention SIG call, so maybe this is essentially something where, based on what was discussed last year there, which we, you know.
Would materialize into conventions, and probably we need to discuss this as a separate repository to start with.
Separate from mainframe, or is this… Part of the mainframe.
atoulme 00:34:56 Oh, I see.
Ruediger Schulze (IBM) 00:34:57 Yeah, right. But let's get started. I think this is, as we just said earlier, Craig and I, we discussed this when this came up. I think this is really, you know, helping us to accelerate on these definitions for the mainframe domain. So, really, really right step to move forward with.
atoulme 00:35:18 Awesome.
Ludmila Molkova 00:35:21 Awesome, thank you! I'm glad you're interested and happy to help. If you don't need me, then I'll drop off and leave you to important mainframe topics.
Ruediger Schulze (IBM) 00:35:32 Yeah.
atoulme 00:35:33 Yep, no, thanks.
Jim Porell 00:35:34 Thanks again.
Ludmila Molkova 00:35:35 Good to meet you.
Ruediger Schulze (IBM) 00:35:36 Thank you, thank you, Ludmila. And Antoine, I just… maybe just two topics. One is, I mean, we discussed this offline, it's more for awareness for the others.
on the Linux S390.
atoulme 00:35:50 Nope.
Ruediger Schulze (IBM) 00:35:52 self-hosted JitHub Action Runners, obviously, we… We need to, to, go, go back to… I forgot the name of the person from the CNCF, but obviously, kind of, like, moved this discussion forward.
And the other one is probably more for information for you, but from an OMP perspective, and as I look at the gentleman on the call, I think it's the same crew who will be looking at.
Jim Porell 00:36:20 It is.
Ruediger Schulze (IBM) 00:36:21 That's a…
Jim Porell 00:36:23 We didn't invite Greg, I don't know, we should have invited Greg.
Richard Nikula 00:36:26 They said they didn't have time, so that's fine, but anyway.
Ruediger Schulze (IBM) 00:36:29 So, there is an initial discussion to bring the Open Telemetry Collectible to COS, which essentially is COS Unic System Services, at least that would be my initial understanding. Yes.
just, this is FYI, we will see how quickly and how fast this will be evolving. There's an initial kickoff meeting, I think now next Monday. Obviously, we had some initial testing being done, it's… it's probably now a year ago, a year or two years ago, there is, you can compile the… the collector on C or SEONX system services, but there is no way to do a cross-compile like you do… like we do, for instance, for Linux on C.
We need to do this on the platform, there is.
or there was a dependency on a specific function from the Go compiler, which I need to go back to check.
That's something, okay, let me find out the status for that. And then, obviously, you know, things like… host metric receiver, this doesn't work at all, obviously, because it's a different flavor of Unix system services. This is then also an interesting, or a discussion to have, what to include in a similar type of receiver from a CS point of view.
the build, obviously, and to have an initial run without any kind of, like, plugins, receivers, or a large use of contrib, that seems to work, at least it worked at that time.
But, there's obviously more to be done to make this really a deliverable from… for the platform, but, that's essentially where things… you know, stand.
Richard Nikula 00:38:25 There'll be certainly topics to discuss come Monday, so…
Ruediger Schulze (IBM) 00:38:28 Yeah, yeah, right, definitely. So, but just to… to… to give an update on that.
Richard Nikula 00:38:35 Let's get it moving.
atoulme 00:38:39 Please return, go.
Okay, so I did some digging on my own. I wanted to ask you about this. I don't think the host metric receiver is particularly useful on the OS.
4. It's just not the same concepts.
looks like, right? I'm just generalizing, I was like, I think it would be a waste of time to try to just map out everything that is in the OS over to Linux concepts, it's just not the same thing.
Instead, what seems to be the best approach is to embrace the work that has been done by IBM to organize infrastructure metrics for the Z-type systems, and specifically look at ZHMC as the preferred solution to get host metrics.
Am I right here?
Am I missing something?
Ruediger Schulze (IBM) 00:39:31 It's a very infrastructure-centric view.
atoulme 00:39:34 Okay.
Ruediger Schulze (IBM) 00:39:35 And, and.
Jim Porell 00:39:39 Operationally, I don't see it.
Ruediger Schulze (IBM) 00:39:41 Yeah, it's a starting point. There's some use cases, but it's actually, like Jim just said, right, it's operational, it's not actually the layout to… To look at, right?
Jim Porell 00:39:56 The HMC is a protected resource that controls way too much, and I think customers would be very risk-averse.
To use that as a collector, if you'd like.
atoulme 00:40:10 Oh, I see what you're saying. Right. So, so, I mean, my digging brought me to the Golang ZHMC client, and I also saw that there is a Prometheus exporter for ZHMC.
that is defining a lot of metrics. So, to me, that tickled me a little bit, like, I was interested to find out Some of those metrics are defined. Most of them are just a combination of factors, like, you combine a resource to a unit, and you send a lot of information. Like, it's just a lot.
And there's no semantic conventions behind the metrics that are defined for that Prometheus exporter, so I was interested to find out, like, if there is… A team there, or is this in some sort of, like, is this… is this where we should be?
Ruediger Schulze (IBM) 00:40:59 So…
atoulme 00:41:00 invalid.
Ruediger Schulze (IBM) 00:41:01 So, that's what I touched on earlier. So, that actually has a… if you look at the HMC… data that has a couple of resources or entities that are generally interested… interesting from a hardware platform perspective, and In order to kind of, like, define this common language to represent the mainframe platform.
I think there's a couple of things in there that, you know, we want to look at from a… from a… you know, how can we express these metrics, for instance? And that's why I was bringing this as an example, to kind of, like, start populating these semantic conventions.
Repo for the mainframe. Historically, the promiso is receiver, or exporter in this… in this moment.
that was… one of the use cases was, and it's actually still, I think, as part of a managed offering for essentially in the cloud environment, if you have a cloud-like environment to manage access to the HMC, Or to monitor the, you know, hardware resources. That was one of the use cases how this, Kind of, like, was created and then contributed as just, or made available as open source.
The… The chronolarity is really if you are at a level where you would manage Or wanna… wanna monitor, certain… infrastructure metric information from a… from a… lowest level of the platform, but the… the interesting parts from an operational perspective, they, in fact, then reside in the CUS as an operating system. Interesting. So, I'm looking, you know.
I'm looking at the… at the example of the HMC as a way to kind of like, you know, we talk about certain concepts here, right? We talk about, CPC, we talk about LPOS, and so on. So… we talk about CPU types, you know, we… I mean, we have been discussing this for a while, but, you know, let's agree on what… how we… how we define the CPU type, and how we express an utilization on the CPU type… on a particular type of CPU, and that actually becomes… Then, you know… can be used also at the COS level, and there are similar things, probably, to look at.
Jim Porell 00:43:52 I like to use analogies to show, because when you say HMC, that sounds like a unique Thing to the mainframe.
In some respects, It's kind of like a VM control monitor.
Control center, you know, that you're defining how you're gonna break up the virtualization of the mainframe.
And… and you can set workload limits.
by partition, if you'd like. Yeah. But it's… but it… so it's very similar to Virtualization Manager, you know, in terms of what it's doing. So I think that, you know, I think.
atoulme 00:44:28 Yeah.
Jim Porell 00:44:29 Going back to… what you, Rudiger said before is this virtualization concepts, there's a… there's a lot of synergy here.
Okay. And then you get inside the containers.
you know, now you're seeing the operating systems pop up, like ZOS, VSC, another VM. It happens to be multiple, multiple levels of virtualization on the mainframe, but…
atoulme 00:44:57 I see.
Not bad.
Jim Porell 00:44:58 I think… I think if you start with that concept, that they're similar, then it'll make a lot more sense.
atoulme 00:45:04 Yeah, I figured that HMCA wasn't going to be it. When I looked at it, and I saw that some of the metrics were related to the wattage of power cords, like, this is very low level.
I just don't know if we have customers who would be interested in that type of detail at the hardware level, or if that's actually overkill. Like, this integration was built And do… should it… should it be… but I… okay, let's take that offline. I… I know I understand better, it's not in scope, it's actually not that useful. Another use case I have… which I'm discussing with different teams, is a way to also correlate better trace data.
Going through a mainframe.
With the metrics.
Jim Porell 00:45:49 What are you talking?
atoulme 00:45:51 And this is… this has been actually very painful. So, for example.
I'm not seeing the LPAR being populated on the APM traces.
So that makes it really difficult for me to then offer a better authoritative way for people who have, let's say, LPAR in staging and L power in… in pod, I want them to make it super clear which particular part of the data is coming from, and that's a big miss. That's just the start, right? We're just, like, not seeing that in the trace data.
And I would like it so that we have even more of this type of trace data, so that we can really correlate better to some of the elements of ZOS, and specifically the services running in ZOS, like Kix, right? Just make sure we do a better job there.
Ruediger Schulze (IBM) 00:46:35 Yeah, so where this is leading is actually, there needs… and this goes into the semantic conventions, obviously. This really goes about the resource or entity definitions.
I mean, we… we… we… And that's why I said, right, we somehow got stuck on this TPS, PR for various reasons, but, you know, I think now is the time to really take this over. But along with this, there's obviously going the… The entity definition, if you have a… just by example, right? You have a kicks region, so what's the… what's the attribute that you want to have on a KICS region, and how does it relate? Also, what's the operating system, what's the LPAR name, or what's the LPAR information, sysplay information? Some of this we have been discussing earlier here.
I think, you know, especially now that we also moved from resources to entity and the semantic conventions.
we need to take, kind of like, also the next leap to be very clear on what are the identifying attributes versus what is being descriptive attributes. We… let's say we are aware of this discussion, but we didn't have that here in this forum yet, so this is really where… where we need to get into to… to clear that out.
atoulme 00:47:56 Okay, I'm gonna look up that TPS PR you mentioned. I am actually not up to speed on that.
So, I want to… Right? But…
Jim Porell 00:48:06 Is there a vision of inheritance here? Because…
atoulme 00:48:11 when.
Jim Porell 00:48:12 So, like, you want to do this trace, so… and I'm… and to me, that is the number one customer issue, that people are looking for here, with OpenTelemetry.
You make a connection from the outside, you know, mobile, ATM, whatever, you know, some app comes into the mainframe, it goes to a Kix region.
Now… the span, the trace ID is all being captured as part of that context coming into that instance, but that instance resides within a broader view, like, That's a KICS application, so I need to know that.
That's running within a KICS application-owning region.
That's running inside a KICS transaction processing server that's running inside a ZOS image that's running inside a particular LPAR. Now.
I don't want to share all that crap. I want to be able to inherit that information so that you know, It all becomes consumable, and that's kind of the thoughts of how do we get all that, you know, that's where we started defining what's a host, which got us into an LPAR, and all those kind of things, and into an individual process, if you'd like.
atoulme 00:49:31 I think that's beautiful. Let's do it this way, through entities in that case. We used to do it through metrics, which is kind of the poor man's definition of this type of parentality.
It would stitch together things by using those dimensions to kind of go around, like… the case of Kubernetes, to give you something that's… is roughly equivalent, it's not as deep, but you would have a container would be part of a pod, which would be part of a deployment, and that thing is inside a namespace, that namespace is inside a cluster, right? So you… You would go by going through the UIDs of all those things to kind of, you know, go back and forth.
Jim Porell 00:50:07 We can…
atoulme 00:50:07 that, and that would be our identifiable attributes, that's what Riddigger is talking about. And then on top of this, if we define those relationships between those entities, then it makes it really easy to just diagram those things and represent them so people can catch those concepts.
And then, yes, I will be able to, looking at I might be a bit presumptuous, but I think what I could then do is start to do this type of weaving together, where I say, this pan went to that particular service.
and then based off that, go back and say, okay, that service is in that L-bar, and what's going on? The problem I'm having is, we were having a discussion about that, like, just looking at the chart that we were getting from our APN spans, is that, our chart would say things like.
I'm talking to, to… Kicks DD1B.
That's my service name.
And now I have questions about that. I was like, DD1B, where? Like, how many DD1Bs do you have? I'm like, oh, you can have multiple.
Alright, that's a red flag.
No, you're no longer talking to Unique Service.
So what is… it felt like on the ZAPM side of things, When we look at the spend we're able to collect.
We just need more identifiable attributes on there. I'm not asking that we change anything that we're doing, it's just… ServiceName is not enough, or it needs to be more… comprehensive, so we can derive from it identifiable attributes, like, did D1 be in which LPAR? Did D1 be in which case region? Right? What… how do I cross-correlate? It's not… the identifiers were not unique enough. I think if we put this on paper, and we built exactly what you just said, first time I hear.
I'm new to this, right? So, bear with me. The five different levels here.
then we can build these entities and we can go from there. I'm still catching up on… everything, right? So this TPS PR, for example, I need to go read that.
But that's good.
Jim Porell 00:52:03 Richard… Richard, Greg, do you agree with kind of that observation? I think that helps.
Richard Nikula 00:52:10 Well, the one thought that I had is that There's only so much that we can do from a… Open telemetry point of view.
And then there's other systems that have to come into play, right? So these systems have some forms of discovery that's going on, that's figuring out things, right? And the key is that when the kicks… When this kicks thing records that it's a kicks thing.
it has to record it in such a way that all of the rest of the systems now know what that is, right? So that, you know, you don't… it obviously can't say what LPAR it's on, that's… it's way below its… way above its… level of information. It's simply saying, hey, I'm a Kix region, I'm running this thing.
Right? And so now, we now say, well, what's that Kix region? Well, that Kix region exists within you know, a CMDB somewhere, or something that now has to figure out that, okay, that's the relationships, and then somehow that has to get into observability to figure out what the heck everything else is, right? It can't… it's got to kind of be a multi-tiered Piece of things running to make it all fit together.
atoulme 00:53:28 Yeah, that's fair.
And this is good feedback, this is what we need, like, if we… I don't think we can call it all of it all the time, but I think also what we… if we build a semantic convention, then… It becomes the blueprint on which those implementation teams can exist.
Richard Nikula 00:53:45 Exactly.
atoulme 00:53:46 What I got.
Jim Porell 00:53:47 Right, that's where I was going, yeah.
atoulme 00:53:50 the feeling I got talking to them is that they were lost. I was like, but everything is fine, was the answer. And then we started to show them, I was like, I cannot tell you that I can correlate those metrics coming from that Kix subsystem to this particular span, I'm not sure we're talking about the same Kicks region, or the same Keeks server.
I need you to be very precise about how you send this, because my customers will go leeviate at me, or they will be alerted on their own kicks.
all hell breaks loose, right? It's just no way to work. We cannot do that. So, close, is what I'm feeling here, because we would be able to do that, and then kind of come back to the implementation teams, and kind of work in harmony on… on delivering this. The good thing about semantic convention is what is there, you can validate against it too.
So, we can very easily go to any direction, like any vendor discussions than that, and be like, okay, here are the set of attributes we expect to see on the span.
And we can use Weaver to just life check that the data that is coming out of this particular thing is in check with those things, and that becomes a test.
So, before you release next version, can you please run this as part of your testing framework?
And then it's a very easy comparison, and we are going to have a good time supporting this whole thing. We can even version it, you know, are you familiar… are you working with version 1 of mainframe SIG conventions, or… V2 and whatnot, and we can take our time to transition people, but at least have some sort of a stamp on it. It's like, here's where it is, here's the spec, and here is where you can come back and know how to correlate those signals together.
The entities are absolutely paramount to get first.
Jim Porell 00:55:33 Yeah, I think part of the issue is… and rude, I'm thinking of your charts, you know, where you show all the W3C connectors in between components, It's… I don't think we transmit.
via OpenTelemetry today.
all those inherited things, and so I do think it goes back to what Antoine's saying about discovery, you know, that there has to… it's almost like a secondary means has to also exist for that context.
Not positive on that, but… Think it out loud here.
Ruediger Schulze (IBM) 00:56:11 Yeah, I mean, our… From a propagation point of view, you actually don't want to, you know, propagate, you know.
Information about the previous servers, it's actually that you want to emit this information to your observability backend. And, the propagation is really limited to you know, the W3C trace parent, trace state, and then, you know, baggage is obviously a topic on its own. Also, you know, when it comes to Maybe transmitting additional correlators.
I think where, where really the, The enhancements are needed is really in the space of what was just discussed, and have a commonly agreed, entity model And also, you know, once we get there, once the… I think the relationships, I think, are still in work from a specification point of view, but once we get them.
To also make use of, relationships as part of the data that would be sent out, so that there's a clear understanding, like you described it, Jim, okay, this, you know, KICS region is running on this LPOR, and we have a… Not all this information being just attached on the.
Jim Porell 00:57:32 Yeah, I can't.
Ruediger Schulze (IBM) 00:57:32 with suspension, right? So this is… This is definitely something to explore moving forward.
atoulme 00:57:43 Alright.
It looks like. So… We got about 200 orders to just get first, so get this repository going, file… feel free to file as being issues, anything you can think of that we need to do in there. I don't think we need to be particularly… Don't, don't… Don't… torture yourself trying to make sure that we're being very… good about coordination yet, because we can coordinate those issues over the code, if there's an overlap or anything like that, right? And then we should take, probably, the TPS, and this is really good, probably want to do that, to take the existing PR for TPS.
Ruediger Schulze (IBM) 00:58:21 Right, right.
atoulme 00:58:22 entities, we start from there, that's our identifiable attributes, everything flows from there and becomes very easy for us to kind of work our way through the different components of virtualization, messaging, production.
From there on.
Ruediger Schulze (IBM) 00:58:34 So let me ask one question, a last-minute question. So TPI is kind of like we started, and this is for KICS and IMS.
atoulme 00:58:44 Okay.
Ruediger Schulze (IBM) 00:58:45 There's also, for databases, Span, and also for DB2 in this case, and also for… for MQ.
Which brings me back to what we touched on earlier, right? So, where would this live? Do we… would we want to have this live originally, or… not originally, but for the time being in the mainframe repository to give it a start?
atoulme 00:59:09 So, funny story is that when I built the MQ, IBM MQ, specifically Metrics.
I built them with the PCF approach, which allows you to query from the outside an IBM MQ system and get some information about its behavior and its health.
And then, I used this waiver… I built a waiver model first. I used it to generate the code and the documentation of that.
Especially in Java, so I could kind of make it a bit more maintainable.
So, we currently have the Weaver model for this already in OpenTeometry Java country.
It's maybe a bit harder to discover than it should be, and maybe it could be derived or defined better if it was in the mainframe SIG, but that's up to us to decide.
Ruediger Schulze (IBM) 00:59:53 Looking back.
atoulme 00:59:53 open a PR, and move this Weaver model over to the mainframe SIG, and instead have a reference to that model in contribib.
going forward, Which might make things, interesting, so that we can maybe cross-correlate or do more work.
But, when I opened that PR, I expect that you folks will have some feedback on this. It's like, is this useful for mainframe? Is it too specific to IBM MQ? Do I care for this to be in mainframe? And then we can have a… good conversation about that. We don't need to have We don't need to come to a conclusion right now, but I would like to have that conversation with you all.
In… in contrast, and after having time to review some of the concepts in.
Ruediger Schulze (IBM) 01:00:37 Yeah, and I think when I… when I remember this right, Antoine, this was actually for the MQ Distributed when you did the implementation against the REST API there, right? Yes.
atoulme 01:00:47 PCF.
Ruediger Schulze (IBM) 01:00:48 Yeah.
atoulme 01:00:48 of a recipe eyes.
Ruediger Schulze (IBM) 01:00:49 Yeah, yeah.
atoulme 01:00:50 M.
Richard Nikula 01:00:50 I mean, MQ is a good example of something that's Identical, or near identical, Mainframe distributed, really doesn't matter.
atoulme 01:00:58 Indeed.
Richard Nikula 01:00:59 Yeah, there's some uniqueness on each of them, but… they're very similar. It's very strange to say it was an MQ thing, right? Or, I mean, a mainframe thing.
Something like Kix is a little less obvious, although it's not much different than an application server, but it is sort of more unique.
But, you know, MQ is MQ, and it's virtually the same as any queuing system as well, so it's even more confusing, because you could then compare it to active MQ and say, oh yeah, pretty much all You know, this set of objects are the same, yep, and there's a set that are different, but yep.
Jim Porell 01:01:36 What are the complications?
And what I like, though, is I think we're starting to define our own destiny, because if we can put a stake in the ground, you know, are we a follower or a leader? I think we've been a follower somewhat, and now we can kind of leapfrog into a leadership. So, if MQ SIG is, you know.
They're, they're parked, not active.
We can do what we need to, and then maybe push them to go adopt our way of thinking, you know, or extend toward our way of thinking, if it makes sense to them.
But at least we'll have made progress.
Which I think is where we're lacking right now.
atoulme 01:02:18 Yep.
That's… perfect.
Ruediger Schulze (IBM) 01:02:22 Yeah, there's… a good closure, Jim, for this today.
Jim Porell 01:02:26 Excuse me.
Sounds good to me.
Ruediger Schulze (IBM) 01:02:31 Okay, I have to say I'm traveling next week, but, you know, whatever, Antoine, you know, if the April comes live, as I said, I would, you know, later than take a look at this, and… Okay.
atoulme 01:02:47 If it's simple mechanical stuff, like moving some files for the TPSPR over to mainframe, so we can kick off the review process, I am happy to be of help, right? And I'll… anyway, whatever I do, I'll make sure to bring it to Slack.
So you know what's happening.
Ruediger Schulze (IBM) 01:03:05 Okay, sounds good.
So, thank you.
Jim Porell 01:03:07 And Ruder, are you gonna be at the EOTC?
Ruediger Schulze (IBM) 01:03:10 Yes, on the EOT, but this is in June, right? Yeah, it will be.
Jim Porell 01:03:14 Right, I will be there, so that's an opportunity. I'll talk to you separately about that.
Ruediger Schulze (IBM) 01:03:19 Yeah, okay, good, yeah.
atoulme 01:03:20 Awesome.
Ruediger Schulze (IBM) 01:03:22 Okay.
atoulme 01:03:22 What's going on?
Ruediger Schulze (IBM) 01:03:23 Yep, but…
Jim Porell 01:03:25 Alright, bye.
