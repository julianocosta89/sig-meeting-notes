SIG: Arrow SIG
Date: 2026-09-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Albert Lockett 00:00:27 Hey, good morning.
Pierre Mariani 00:00:30 Hello, good morning.
Drew Relmas 00:01:49 Hello, everyone.
Pierre Mariani 00:01:54 Good morning.
Albert Lockett 00:01:56 Good morning.
Joshua MacDonald (Microsoft) 00:01:59 Do we have a problem with the Zoom link?
I noticed that there's a… oh, there's two Zoom links, and I was just clicking the wrong one. Ha! Never mind. We have two Zoom links, and they're both in the notes.
Good morning.
Afternoon, whatever.
While we're, here waiting, we can enter our names in the agenda document, notes document. I'll paste that just in case.
And, I know that… I think F5 may have been having an off-site this week, So we may be short on F5 folks. I'm not sure whether Laurent will be here today.
But we can just start.
Okay, here's my… Nope.
Here's my screen.
Cool, alright.
Well, it's been another week.
Weird, okay. And here we are.
Does that work?
Can't tell what y'all are seeing.
Drew Relmas 00:03:17 I see the Google Doc right now.
Joshua MacDonald (Microsoft) 00:03:19 Okay, good. Yeah, let's just go through the usual motions. It's a small group today, but that's good. Feel free to speak up if you want. So we're looking at the ones that need discussion.
I'm going to… Start at the bottom, going backwards in time. I still haven't asked CJO about this one at the bottom. We're gonna keep skipping over that one because, I need to ask him to fill in some more information. We've also been skipping over Phase 3 for now, that's fine.
I think, there's more to do there. So let's start at the bottom with, receiver plugins. I know Aaron can't be here today, but let's take a look anyway.
And… This is one… I've read this now that I… now that I see it. It's… it's certainly lengthy. This is a detailed proposal for several modes of interaction. Wow, look at how long this is. I say I read it, but did I read it all?
So, this is, Aaron's plan for WASM receiver plugins, which are given access to, either a host-framing mechanism or a guest-driven receiver. That's an alternate that gives you the ability, I think, to do stuff like WebSocket, whereas host-framed would be, like, for HTTP.
I certainly think we want to accept this. This… idea has been lingering for a while. It came up when the database folks began talking about custom receivers and how we'd like to be able to be a little bit more modular, and have components that are built outside of our repository. Only plan so far is for WebAssembly, so… I think we can accept this one. Any comments?
Drew Relmas 00:05:18 No, sounds good. I know it'll be a long road, it's a long issue.
Joshua MacDonald (Microsoft) 00:05:22 Yeah, that's a big one. But I think it was well written. I did read… did read the text, and the diagrams.
All right.
Okay, so now, this is one… That's… Old, but has been updated.
Okay, looks like…
Drew Relmas 00:05:47 re-edit it?
Joshua MacDonald (Microsoft) 00:05:49 Yeah, okay, so it got stale, no one ever, responded to this. I'll describe what I was thinking back when, is basically that we have a lot of, like.
the component, the node is trying to send an ACK or a NAC, and it itself could fail, because… delivery of the AC or the NAC failed. And I felt like back in March, when I first wrote this issue, there was a lot of code that was being written to handle the error of handling the error. And, like, that can keep going forever if you're not careful, so I wanted to, like, set up some sort of, like.
framework so that, like, just most of those call sites where we have to deal with an Akronac send failure, like, have a standard treatment and a helper or something like that.
I think that summarizes the issue.
And I suppose… There was some… earlier discussion in this issue. Any comments on this topic?
I would… this is one I would like to hear Laurent's feelings on. I've always felt a little bit vague and uncertain about this topic of When you are a, let's say, processor, And you receive some data, You say, this data has an error It is not appropriate to return an error to the engine. That is a… that is a very serious condition. That is saying, I am failing.
there's a difference between I am failing and this data has failed. And we want to be able to fail the data and never return errors to the engine unless there's something catastrophically wrong. And I think what happens is you see this… What I… what I'm afraid of, and this is my uncertainty, is that you see code like this, and that's gonna return an error to the engine when a NAC send fails, and that's gonna, like, abort something, I think.
And I don't like that.
And that is the major reason that I wanted this issue filed.
Was just the uncertainty over, I'm going to break the engine when I can't handle a knack or a knack.
So, at least we should remove the stale. We did. So, Tom removed the stale by putting back to needs discussion.
I'm inclined to accept it again. Oh, hey, Laurent has joined us. Good morning, Laurent.
Laurent Quérel 00:08:09 Hello, sorry to be late.
Joshua MacDonald (Microsoft) 00:08:11 Yeah, so we were just going through some stale and or re-discussing issues. This is one I was just describing how my anxiety is that when we fail a request, it may end up propagating back to the engine, and we don't want that. We want a nice way to handle these moments where you're trying to send an ACK, and this… this question mark is going to cause the engine to fail if it… if the… send channel fails for some reason.
So it's a pattern that I keep seeing that makes me uneasy every time, and that was why I felt this issue. But it was back in March, so… My inclination is to return it to accepted, but I don't have a solution in mind.
Laurent Quérel 00:08:59 Yeah, I think we need to… to study exactly why that would fail.
I didn't notice recently any issue in this,
Joshua MacDonald (Microsoft) 00:09:08 Maybe we could make Notify Act infallible. That would actually… that would actually improve my, feeling.
Yeah.
Laurent Quérel 00:09:16 Yeah.
Joshua MacDonald (Microsoft) 00:09:16 Because what I remember was very early, our code was sort of like, well, I'm gonna try and send this Akronack, and if I fail, then I'm gonna do something else to handle the error, and I just don't like seeing error handling on top of error handling on top of error handling, you know? Like, it makes me feel uneasy and undisciplined.
Laurent Quérel 00:09:34 Maybe the… the only event, that, can make sense for me for that will be a shutdown.
Both should then.
Yes, something like that.
Because otherwise, we have to wait till the… if the channel is full, because there is too much, act like message.
We should not return an error, we should wait.
Except if the research is done.
Joshua MacDonald (Microsoft) 00:10:14 block unless there is a shutdown ending, in which case error is appropriate, I think.
Laurent Quérel 00:10:23 Yeah, we have to double-check if it's the best approach, but… At least, for now, that makes sense for me.
Joshua MacDonald (Microsoft) 00:10:31 Sounds good. All right, we're down to, 5 more of these, and it's… it looks like we've mixed our stales and our needs discussion, so this is another old one.
I'm willing to say that Drew has mostly addressed this one. This was really just a,
Drew Relmas 00:10:48 Yeah, I think we can consider this one closed, we're tracking it with other work.
Joshua MacDonald (Microsoft) 00:10:57 Alright.
Drew Relmas 00:10:58 Still not done, but we're getting a lot closer.
Joshua MacDonald (Microsoft) 00:11:01 there's more issues filed for what's left, so I'm happy that the mission was accomplished, or substantially accomplished.
I remember this one. I know Karsh couldn't be here today, The morning meetings are hard for people.
This was a sort of wish list to get Tokyo sort of swapped out, and I know that… or at least swappable, and I know that this is a tremendously difficult one. I see us adding more Tokyo mutexes and things here and there.
So, I think this remains a nice idea. I'm not sure that we have much to discuss about it.
Drew Relmas 00:11:38 Yeah, the only thing I'll say is technically it was a child issue of release on crates.io. I think Ukarsh's position was he's fine that we released less than, 1.0, but I think, from his perspective, this is a prereq for a 1.0 crate release, so…
Laurent Quérel 00:12:04 And, do you still have this project, internally, with, a thread per core, in runtime?
Joshua MacDonald (Microsoft) 00:12:11 Yeah, that's the project called Oxidizer, and we do have it, and I haven't checked in with them for a while.
Laurent Quérel 00:12:18 Okay.
Joshua MacDonald (Microsoft) 00:12:19 That's a good question for Ukarsh.
I'm going to leave it open.
Huh.
Laurent Quérel 00:12:24 I'll be curious to see if there is any kind of benchmark.
comparing the oxidizer versus Tokyo, and Yeah, maybe at some point, if you can organize a presentation of where they are, to see if that makes sense for us to make… to put some effort.
Joshua MacDonald (Microsoft) 00:12:44 I'll check in on them. I have a fear that they realized the magnitude of their task and scoped back a lot and are not going to be ready for us, which is kind of what I heard a year ago, but, I should check in with them. They still exist.
Or ask someone else on our team, too.
Alright. I… think I removed the nice labels and accepted this again. Okay. Oh, I found this one. So, option to propagate transport headers from authorized data. This is… Already… Oh, this was brand new. So this is just a feature request, on top of the work this week done by Maxat on my team, who's not, here.
But this was… we've introduced authorized data fields into the context at this point. I wanted to sort of tease a feature out of it, at least something simple.
Which is something my old company would have wanted. So this is, like, the ability to take something from the auth on the inbound side and just slap it onto a header on the outbound side. This is the assumption that, like, you have a SaaS environment where this is the gatekeeper does off, and then everything inside my SaaS is trusted, so I'm going to hand a header around instead of doing some sort of strict auth.
And this is what it would look like to use the selector type of authorized data instead of whatever else you put for headers, which I can't actually remember.
I don't think this is a super common feature request, but it's also a very minor one that fits in with existing header propagation.
Any objections?
Laurent Quérel 00:14:31 Hello?
Joshua MacDonald (Microsoft) 00:14:32 I hear none. Cool.
Let's see.
Alright, we're into new stuff.
Albert Lockett 00:14:40 I can speak to this one.
Yeah, so I'm working on adding, support for processing metric data points in the OTAB query engine.
that work is underway. I have, one PR up that had simple support for filtering, and working on adding, like, the ability to assign metrics, change the value, and things like that this week. So, I basically opened, yeah, the issue that we just clicked away from.
Is the one to remind me to go back and update the user guide documentation when this work is implemented.
Joshua MacDonald (Microsoft) 00:15:14 Cool, and there's also a PR, I just found it here, which I have approved, I read through it, thank you. Drew has his hand up.
Drew Relmas 00:15:21 Yeah, Albert, I was just gonna say that I know we at Microsoft have some internal use cases, we're interested in using Transform Processor to manipulate metric data points. I know Prateish, who I don't think is in the call today.
on our side was interested in looking at this. So if you have… the only thing I was gonna say is if you have, some minor work or things you want to potentially delegate, I think he'd be happy to… Step in and, pick up a little bit of it.
Albert Lockett 00:15:54 Sure.
Laurent Quérel 00:15:55 for Usluid.
Albert Lockett 00:15:59 No, go ahead. All I was gonna say was that I saw that he posted on the issue, asking about some things that we're planning to support, which the answer was yes, we plan to do that.
So, but yeah, I can, Yeah, once I've got, like, the work needed a little bit more stabilized, if there's anything I can carve off, I can, get him to help with it.
Laurent, you had a question?
Laurent Quérel 00:16:23 Yeah, a question for the Microsoft folks.
to, try to… we are looking for use case regarding the metrics, and Trying to figure out what will be the priority for the next, because it's, like, not an endless, but, definitely a huge, huge work to… to integrate metrics properly into OPL. So it will be, I think, interesting to have some, List of, use cases or requirements, things that you'd like to see.
for the ITS, or for regular, I was thinking, initially focusing on things that we can achieve in… for the ITS, where we have a specific context, a single thread, blah blah blah, so, where we can do much more, in fact.
Easily. But, yeah, I would be super interested by having, some, some document describing that.
Drew Relmas 00:17:18 Yeah, yeah, I can expand on this just a little bit. I think we're aligned on folk caring more about the ITS world. For full transparency.
you know, I think the use case we're targeting internally, is today there's some, usage of a GoCollector transform processor to manipulate metrics in some way using OTTL.
So, essentially, what we're looking for is, it would be great if Hotel Arrow ITS allowed us to do the same breadth of manipulations, so we can stop taking our dependency on the GoCollector transform processor. A lot of it is simple.
metric, like, attribute, data point attribute renames, or reads, or simple stuff like that. The one complex one is, that I know of is scale metric.
So, you know, we've… it's somewhat related to duration as well as, like, CPU percentage metrics that we're emitting from the engine.
for duration, you know, we made the call that we should try to use seconds throughout, but what happens when we have… we need to report milliseconds, or for CPU, we want to report it as a percentage, so we want to scale it by 100.
So things like that, which isn't necessarily metric data point, it's more… well, it is metric data point, but it's on the value, not the attributes.
Laurent Quérel 00:18:48 Yeah, yeah. Yeah, that… I think that's, that's something we were targeting anyway. What Albert is doing is, right, so these are fully…
Joshua MacDonald (Microsoft) 00:19:01 these are point operations, not aggregations, and they're very useful. I also know that there's, like, convert histogram, which sounds terrible, One I've seen is, like, converting units, so I have something measured in atmospheric pressure, and I want to change it to PSI or something like that. Something dumb, but, you know, just multiply by a constant floating point value, and so on.
Laurent Quérel 00:19:25 Yep. Great. Cool.
Joshua MacDonald (Microsoft) 00:19:28 Very good. Accepted.
And this… this… I'm gonna put a… put a flag on 4068. We're gonna come back to talking about code review, because I feel… like, what I heard just there is that Pratish should be helping with code review for Albert.
But that's just my agenda to talk about how we get more code reviewers. So… We're almost one more. Okay, Drew has filed one. Want to talk about it?
Drew Relmas 00:19:58 This was way back when, when we were doing.
Joshua MacDonald (Microsoft) 00:20:00 Oh, right.
Drew Relmas 00:20:01 nodes. If you scroll down, I think it got marked as stale, and then Tom moved it back to meet its discussion. I still want to do some organization in the OTAP crate.
Specifically, I really want to organize the OTLP HTTP gRPC shared stuff a little better.
However, I don't think we're in the huge rush to get rid of the OTAP crate. Laurent and I discussed when we were doing crate publishing, and I added something to the OTAP crate README, saying, for all intents and purposes, this is our common, crate, so I think it's going to continue being that, but we can still look at organizing it a bit better.
Joshua MacDonald (Microsoft) 00:20:45 We just don't call it common, so it doesn't look like another common crate.
Laurent Quérel 00:20:50 In this, in this area, we also had, I don't know if you read my comment, to… The ability to add some feature flag Pearl, Pearl knows…
Drew Relmas 00:21:03 So we… I actually, I added an agenda item to talk about feature flags later.
Laurent Quérel 00:21:08 Okay, perfect.
Joshua MacDonald (Microsoft) 00:21:11 Okay, maybe we can move through staleness quickly here.
So, gosh, does everybody remember what we were doing 6 months ago? I'm… you can see what I was doing 6 months ago.
Laurent Quérel 00:21:24 It's fault.
Joshua MacDonald (Microsoft) 00:21:25 That's true. So, let's see, some of these are probably, I think we have a continuous benchmark on Windows.
I… these two here, like, I was thinking about memory limits in the middle of the night, so this is, like, still pressing, I think. We… we have a lot of work to do on memory… memory governance, so I would say that these two that I wrote here are worth keeping open. Let me just kind of do this in bulk.
So those are two tests about low memory use. I have… this is a blanket issue about profiles. I think this is still super important and super interesting. For the group here, there was some… discussion about Memalloc profiling in the last, couple weeks, and I have an email from the Memalek author, this morning or last night, basically saying he made a bunch of progress. He's implemented PPROF.
Laurent Quérel 00:22:20 Oh, fantastic.
Joshua MacDonald (Microsoft) 00:22:22 And I also spent a few days learning Memalek so that I could help him if necessary. So I have also come up to speed a little bit on Memalek's implementation, and I looked into our own memory issues there. So, So that's sort of two issues. Profiles, I think, were… this… this year… the year ahead, 2027, is going to be the year where we talk about profiles for OTAP, and then there's still some research to do.
I… gosh, OneCollect is still part of that same research for me, as I'm trying to get another meeting with OneCollect and really understand the ideal architecture from their perspective for our profiling needs.
So, let's just move past that.
I think we had a lot of missing docs, and I think we maybe can… I think they're gone. Does anybody agree?
Laurent Quérel 00:23:17 Yes.
Drew Relmas 00:23:18 We wouldn't know until we remove it.
Joshua MacDonald (Microsoft) 00:23:22 Okay, I'm gonna call it fixed.
So this… I feel like we talked about one similar last week, or on last Tuesday, which was receive when false does not detect, and I think there's a related issue.
And now it's not here. This is… but we talked about receive when in last meeting as well.
Laurent Quérel 00:23:54 Yeah, I agree.
Joshua MacDonald (Microsoft) 00:23:54 There was a revisit this, and I closed it. So here's the other issue that we were talking about revisiting.
Laurent Quérel 00:24:05 Maybe…
Joshua MacDonald (Microsoft) 00:24:05 I haven't heard any problems of this nature recently, and I need to look at it again.
Laurent Quérel 00:24:10 Maybe, ask Lalit, we could add a comment, asking Lalit what you think about this one.
Joshua MacDonald (Microsoft) 00:24:25 Yes, and do I automatically remove stale by doing that? No.
Okay.
Fly log receiver. Well, that is actually underway. I'm gonna mark all these unstale at the end of this. Validation framework validation framework updates from February.
Maybe we could mark this one done. Oh, here's a list.
Laurent Quérel 00:24:54 For the injection… You can remove the style, because there are still a few things there that we, we'd like to,
Joshua MacDonald (Microsoft) 00:25:04 Okay.
Laurent Quérel 00:25:05 not.
Joshua MacDonald (Microsoft) 00:25:05 I'm gonna bulk remove stale. So let's see, engine, replace… Unbounded Events Channel.
With bounded design. I think we actually have done this now.
Laurent Quérel 00:25:15 I think, I hope.
Joshua MacDonald (Microsoft) 00:25:17 Yeah,
Laurent Quérel 00:25:19 I'm not aware of any unburned thing in the project.
Joshua MacDonald (Microsoft) 00:25:22 Right, because…
Laurent Quérel 00:25:24 But maybe if there is one, we need to work on that. Use a dedicated channel for engine.
Joshua MacDonald (Microsoft) 00:25:29 Yeah, I'm trying to remember…
Laurent Quérel 00:25:33 The prevents started failing.
Joshua MacDonald (Microsoft) 00:25:37 I kind of remember that we added something Unbounded, as a, like, we gotta get something fixed for now.
I'm gonna open up this… Oh, that was me. No, I merged it. Lalit wrote it, okay.
Yeah, Let's see what you wrote.
Alright.
Oh, I do remember this conversation.
Sorry, I want to skim forward, but I feel like people are reading.
Laurent Quérel 00:26:39 Maybe we can, read that, offline.
Joshua MacDonald (Microsoft) 00:26:43 Yeah, okay, well, this is still interesting, I'm gonna… I'm gonna add that, like, follow, needed.
That's… that's not what I wanted. Okay, We're gonna remove stale from that.
And… syslog load generator MAC issues… two days ago… two days ago. Oh, okay.
Windows networking.
Okay, so we're having load problems with our tests on macOS.
I'm gonna say… Cool.
I think that works. Okay.
Cool. We made it through that list as well. We'll keep… keep coming back to it, I'm sure.
Okay, so now we're on the agenda.
And I wrote something here, so since I'm first, I guess I'll just go for it. I don't have a document to share, and I did want to just… we meet once a week.
Throw out some… some conversation.
So I feel that we are struggling to keep up with code reviews, and there's a dynamic that I'm seeing that I don't like, and it's one I want to try and figure out intentionally how to avoid. So the dynamic is that, you know, we all need code reviewers, and we also need approvers and maintainers.
We need approvers and maintainers to get the work merged.
But there are a limited number of approvers and maintainers, and the amount of code is just, like, massive right now.
And so I was starting to think about ways to kind of, like, manage that problem. And the one principle that I like, that I've… sort of thought about my whole career in this type of work is that there is a reader and writer problem. We learn about distributed systems, and we learn that when you are blocked on rights, you should go serve your reads.
You should serve your reads before you serve your rights, in fact, because that is a principle by which you avoid distributed deadlocks.
I find that there is a… the dynamic is that you end up with one person doing all the code reviews and one person writing all the code, and what I want to do is try and figure out a better way to share. And I don't think that we can ask the approvers and maintainers to do more code reviews.
Reasonably. So we started adding code ownership recently, and that was mainly to try and make sure that the owners who care about code aren't left, like, surprised by changes that are happening. So it's sort of a, like, I want to protect the code that I own.
I want to talk about using code owners to share the load of code review, as well. So, to say that, for example, before you get… before you ask an approver or a maintainer to do some code review.
make sure that the code owners have approved. And this… some… of course, some of the code owners are going to also be maintainers and approvers, and that's their problem. But this is a model that works in the Go collect or contribute repository. It's such a massive repository that you basically… no approver or maintainer's going to look at your PR until you have a code owner approval on it.
And what I'm trying to get to is that, like.
as you know, there's this large piece of work involving database receivers that we've got, and as a team that's sort of adjacent to us, they know and cared about all that stuff. I want them to do their own code reviews.
Before we do, basically.
And that's, potentially something that we could automate, like, at the repository level. And I'm going to pass to Drew.
Drew Relmas 00:30:33 Yeah, well, I just have one question here. When we talk about code owners, there's, like, the official GitHub code owners versus kind of the implicit, like, documented in a README or YAML file. Like, I'm fairly certain we can't have people in the actual code owner's file, unless they have right access on the repo as, like, actually part of the approvers group. So, what we're talking about here is more of the informal model.
Joshua MacDonald (Microsoft) 00:31:01 Right, I think what… I don't mean it to be informal, but I see your point, so… so maybe it's the, a separate mechanism that is somewhat formal.
Drew Relmas 00:31:11 I think the way it works in the Go Collector is they have those YAML files with code owners to find, and then when the PR is opened.
I'm pretty sure that those code owners are added as reviewers, or pinged in some way, so that's more than what we're talking about.
Joshua MacDonald (Microsoft) 00:31:27 Yeah, and it's… there's… right. And so, when the PR gets opened, somehow, and I don't quite know, automation kicks in and will automatically assign the code owners listed in the metadata.yaml file.
And… then… It's still a manual process for the approvers and maintainers.
to go look at the PR and say, this has some code owners approving, so I'm going to now approve or merge. And… The signaling mechanism is a ready-to-merge, so when the code owners are happy, they put ready to merge on it, and then the approvers and maintainers can see that it's got approvals already from code owners, and it's basically, like, you're the second approver at that point, and that's what I'm trying to get to, is where the frontline review has been done by someone else.
Drew Relmas 00:32:19 Got it. Yeah, that makes sense, and we can definitely, you know, look at the automation they have in that repo. I do want to open up the floor, I saw Gokhan hand up. The one final thing I want to say is.
We can also work with Trask on the PR dashboard. Maybe we can improve things a little bit there. I know, like, I've been using that a lot for the, like, waiting on maintainer, or waiting on, approver, or waiting on review, whatever the section is. So we can try and customize that further to our specific needs.
But anyone else, like, anyone from F5, other maintainers, Gokhan, you wanna chime in?
Gokhan Uslu 00:33:03 Just… I just wanted to… spoke about… you know, my own experience a little bit. Because I worked on the extensions, and I like to be able to Review as many pull requests that relate to extensions and capabilities as possible.
But I'm also very busy at the same time nowadays, so I'm not able to keep up with it.
Like, nowadays, it's not usually the case. And I was wondering, And I sometimes miss, for example, which pull requests have issues related to it, etc. So, how could we use, to make it easier?
For specific code owners to be able to have the visibility.
Of the pull request that they need to… Pay attention to. Not just the… having code owners, but… Stuff like that, yeah.
Drew Relmas 00:34:06 I do have one suggestion, which is going back to our labels system. So you could imagine having a label for area extension or area capability, and that would give you a one-click filter for everything related to that.
Joshua MacDonald (Microsoft) 00:34:24 And that is automatic, too.
Right.
Drew Relmas 00:34:28 Right now, it's automatic based on code path touch.
Joshua MacDonald (Microsoft) 00:34:32 So I'm just thinking of, like, the… I'm looking at CollectorContrib now, and you'll notice that these PRs all get these, like, this is a SQL receiver, and it has this label, and I'm pretty sure that was automatically applied. Yeah, so…
Drew Relmas 00:34:46 Today, we have area exporter, area processor, Area Receiver. We don't have per-node ones.
Like, we can, but it's just… that's also a scalability problem. The more nodes we add, the more label maintenance that has to happen, etc. So… I think some combination of the informal code owners as well as you know, if there's an area someone's interested in, like Gokhan with topics and exten- or sorry, with extensions and capabilities.
I think that deserves a label, and we should think about how to automatically label code.
With it.
Joshua MacDonald (Microsoft) 00:35:27 I would… I guess I was going a slightly different direction to say that there should be a code ownership, and that Gokan should be required to review those PRs before anything else happens, so that he becomes… on the, kind of, the path. And I… and I acknowledge what Gokhan just said, which is, I think, part of the problem I'm trying to fix here, which is that We're all busy, and there's someone, like.
I know that somebody has to sit there and merge PRs, and, like, look through the PRs that are pending, and this dashboard is helpful, but when it comes to, like.
I know that this PR needs to merge. It's like, either I do the work of reviewing it quickly and just merge it, or I ping Gokan and say, Gokan, I want you to review this, and, like, wait 2 days or whatever.
And that's fine, to wait 2 days, as long as I don't have to be involved in the beginning of, like, looking for code reviewers here, and either I do it myself, or I push… pester somebody about it. I want some automatic system to, like, pester people, so that, So that, because go… because… because what's happening is… I'm looking at the PR, and I'm thinking, I could just merge this, or I could wait for another code owner, because I want to build up more review knowledge, and I want to build more awareness and skill, and, like, all the… all of the breadth of the organization here. So, there's this tension where I know it could move faster if I just do it.
And it would be nice if I could ship this out, but that adds to this latency that I don't want to add, and it's just like… Easier to do it myself, which is not the good solution.
Gokhan Uslu 00:37:07 Yeah, I think, yeah, that notifying someone, like, not you having to do it, but maybe some, you know, pipeline work or something like that, that would be very helpful for me, because I want to spare the time, I want to do it, but I realize that I'm missing them. Like, I even built this AI skill locally to scan the PRs daily. The skill misses it. And I realized, oh, this PR was there, you know, Josh sent me, why did my AI skill not recover?
Anyways, there's that, and also, the other thing is, sometimes code touches capability and extension-related stuff, lightly.
And it still requires attention, but then it is much harder to detect. How could an automation detect that to, you know, ask for my input? In any case, I guess we can, you know, not find a solution to everything, but those are the problems that I wanted to raise.
Joshua MacDonald (Microsoft) 00:38:05 Yep.
Thank you.
That was the discussion I wanted. Any ideas, if you have them over the next week or two, just, you know, feel free to bring them up in the Slack.
And with that, I think we can move on.
To Drew.
Drew Relmas 00:38:23 Yeah. So… Laurent, this is going back to the topic you had. So, I went down this rabbit hole where Riley, on our side, asked me to take a look Excuse me, at… the repo's security policy and how we handle vulnerabilities, and I saw we had one really stale, like, 2-month-old medium level about a crate called Thrift, which led me down this huge rabbit hole. Josh, if you want to open 4085, it's probably the one to look at first.
Joshua MacDonald (Microsoft) 00:38:54 So, sorry, I just went the wrong direction.
Drew Relmas 00:38:59 Oh, you're.
Joshua MacDonald (Microsoft) 00:38:59 I was gonna show us the,
Drew Relmas 00:39:03 The actual alerts.
Joshua MacDonald (Microsoft) 00:39:04 security dashboard.
Drew Relmas 00:39:06 So, I first started, okay, how do I… how do I treat this thrift, vulnerability? And the answer was with an Arrow and Parquet upgrade, which also pulls in a Data Fusion upgrade.
However, there's one blocker, which is, when we upgrade Arrow to 59, That's not compatible with a minor dependency that the ClickHouse exporter has, which still requires Arrow 58.
So this led me down a whole rabbit hole of.
I, as, you know, as a for our Microsoft, use cases, we don't currently use the ClickHouse exporter. So, I was like, okay, I can introduce you know, it's in the core, it's in contribib nodes, so I can get… I can avoid it with feature management. And then this led to a conversation in the maintainer's Slack chat about… Should we have per-node features to allow any consumer to really minimize their dependency supply chain surface as much as possible. So that led me to the other PR you have on the tab to the left.
Which I have been iterating on this morning, which essentially adds a feature for every single node in core nodes and contribib nodes, as well as, per Laurent's recommendation.
some aliases, like, if you feature… if you say feature OTLP or Kafka, that probably means you want both pairs, like the receiver export. If you say OTLP, we'll give you OTLP receiver and both OTLP exporters, things like that.
So… I think this is a smart thing. It doesn't solve the thrift issue, like, that's a separate conversation we're… that Albert and I, I think, are gonna have with the Click House, maintainers.
But, I think this is a good step forward for all parties. The only downside is it's, you know, as we add more nodes, you know, there's more features going on. The other risk is… And this is something I found… Laurent, I see your hand up, we'll come to you in a second.
was OTLP HTTP exporter actually had a code dependency on OTLP gRPC exporter. There was some… code that was in gRPC that should, in this PR, I'm moving it down to that common OTAP crate we were talking about.
We want to make sure that every… individual node builds independently. So I opened a follow-up issue for the prepare-release workflow. I think in there, we sh… like, it doesn't have to happen in every PR, because that'd be, you know, a lot of time spent just rebuilding. But when we talk about prepare release, that feels like the right time to make sure that our feature management story all makes sense, and we're not shipping a broken node, accidentally. So I opened a follow-up issue, I linked it at the… I commented on that PR.
That one, validate independent cargo feature builds.
During release preparation.
Joshua MacDonald (Microsoft) 00:42:37 Got it.
Drew Relmas 00:42:37 So that's my spiel. Laurent, go ahead.
Laurent Quérel 00:42:42 I think in the spirit of minimizing the number of features, macon was, Do we really need to have a feature per node, or do… or can we… Have a feature per capability.
And a capability, for example, for receiver-exporter, when you have a pair like OTLP receiver or TLP exporter.
the capability will be OTLP support.
And I… I don't see a lot of scenarios.
where if you have OTLP receiver, that doesn't make sense to have the OTLP exporter. So, for me, it's not really an alias, it's more directly the feature, and there is no way we… the drawback of that is there is no way to just… Construct a binary with only the receiver or only the exporter.
But I don't think it's a big deal, because usually they share also the same kind of libraries.
for Kafka, that's the case. For RTLP, that's the case. For RTAB, that's the case. So… and sometimes we have only one direction, syslog receiver, for example.
And if at some point we have the sysplug exporter, if sometimes that happens, I don't think it will be a problem too. You just enable the sysplug capability, and automatically you generate the exporter, if we have one at some point.
Drew Relmas 00:44:11 That's a very, very good point. As you've been talking, I think your, comment finally clicked in my head, and I understand exactly where you were going now. Yes, I think… If someone only needs OTLP receiver and not OTLP exporter.
like, adding… having the OTLP export still available doesn't increase the supply chain surface that much.
It only… I mean, we can talk about how it affects binary size, but that's gonna be almost negligible, I think.
Laurent Quérel 00:44:42 Yeah, because we are already already granular with that, so it's, Yeah. And that will reduce significantly, in fact, that will reduce by, too, the number of picture flags in more or less.
Drew Relmas 00:44:55 That makes sense, and it, yeah, it just gives us a cleaner public surface. Okay, I think I can refactor, like, I'm gonna take another stab at this and talk about going that direction. There is one funny comment I'll make, which is, as Albert and I were discussing, we said, are we getting to the point where we need, a builder, like the Go Collector has.
Because that's how they solve this problem, right? Is a builder config file that tells exactly what components you want to include or not.
so, I'm not saying I have to do that immediately, but it's.
Joshua MacDonald (Microsoft) 00:45:33 I have proposed in the past that we, like, actually adopt the same builder and build in Rust support for it. That would be one direction. By the way, I pulled up, just so we can see where we're heading, this is the collector contribib rep repository, which is, like, one of the biggest security surfaces in OpenTelemetry, and I've got security and quality opened, and Code scanning, we all have these pinned dependencies alerts, both repositories do. I don't quite understand them, but we should get rid of them. The reason why this is coming up is that there's a push to make a much more higher… much higher security policy for OpenTelemetry, in terms of response time, and Riley is trying to set some levels That we could potentially, like, advertise, and… We… this is what it's gonna look like for us when we have 300 components. Like, we've got… you know, there's so many of these, and most of them get closed as, like, we are not gonna fix this, but we have to stay on top of these, or else someone's gonna think we're insecure. And the one about thrift had me thinking, because Thrift is a terrible old dependency. I'm sure it's still very active and alive in the world, but does anybody remember Thrift? I mean…
Laurent Quérel 00:46:46 I remember Omen, so yeah.
Joshua MacDonald (Microsoft) 00:46:47 Right? It's so old.
Laurent Quérel 00:46:49 And you can filter these things on the content.
Joshua MacDonald (Microsoft) 00:46:51 So what I'm reminded of is that what we get in this type of repository is, like, open source just kind of proliferates, and sometimes it stops being maintained.
And so Click House has a dependency on Thrift, and it's… we are stuck with this, like, transitive dependency until something happens. And what I'm worried about, Drew, is that even remove… even if we have feature flags.
that say how you build the code, the code scanners that we use don't know about the feature flags we're building with. So the code scanner will still see the bad dependency and still raise the flag, and Riley will still be, like, looking at us, like, what's going on?
Drew Relmas 00:47:29 We can't do anything, our hands are tied.
Joshua MacDonald (Microsoft) 00:47:31 And I don't know what to do about that problem. I'm seeing the same exact problem right now in the Collector Contrib. I could have pulled it up, but Prometheus has this one… Prometheus is one that we will not escape here. Prometheus has a huge importance, and it has 25 discovery plugins. I'm making that number up, but it's, like, dozens of Discovery plugins, and each one of those Discovery plugins is a dependency risk.
And what the collector contrib does is build Prometheus Receiver, which does a blanket wildcard import of every single discovery agent in Prometheus. So then.
Well, it turns out there's one discovery agent in Prometheus that has a stale dependency on an old AWS SDK. You know this story, Drew, but the point is, we have no control over the Prometheus receiver, which brings in 25 sets of dependencies.
and gives you feature flags, roughly speaking, the Go equivalent of a feature flag, but I don't think it's going to help us with our code scanner problem.
And it gives us a need to, like… if I could change how the collector contrib does it, I would say, let's break up Prometheus Receiver into… narrow Prometheus receiver instances. There's a Prometheus receiver for Kubernetes, there's a Prometheus receiver for Azure, there's a Prometheus receiver for whatever this thing called outscale is, is the bad dependency right now, and I don't know what outscale is, and I don't want it, but it's part of my build right now. So I think we're going to have to worry about this problem as we grow.
Drew Relmas 00:48:57 Yeah.
Joshua MacDonald (Microsoft) 00:48:58 There's no easy.
Laurent Quérel 00:48:58 So this…
Drew Relmas 00:49:00 Besides being, like, trying to limit our dependency surface, but that's kind of a losing battle.
Laurent Quérel 00:49:08 Maybe we also have some kind of default posture.
For… if I'm taking this, specific example with the Clucose, dependency.
Based on the discussion between Drew and Albert yesterday.
My understanding is… we could fork, because it's a small, it's a small repo. Yeah, it's a small repo, there is no real value there.
So, in my opinion, the posture could be… when we are in such situation.
Let's fork, or let's integrate directly the code, or whatever we do.
Just in order to minimize, Possible complicated dependency to a strict minimum, and not trying to, To systematically, onboard things that could be problematic.
When they are small, why we are just, adding this kind of situation for us, I don't think it's necessarily the right way to go.
Drew Relmas 00:50:15 Pierre, I think your hand is up.
Pierre Mariani 00:50:18 Yeah, just a left-field question. Would it… would it be an option to… Split some of the contribib nodes that, have dependencies that we cannot control as a separate repo, and build a separate, dynamic library, and then, You know, connect them at runtime.
Joshua MacDonald (Microsoft) 00:50:41 Yeah, that is the appropriate solution, Pierre, and it's one that the collector contribo has struggled with. It's, like, so much nicer to have one central build managing all the stuff, but then you end up with this kitchen sink with every dependency in the world, and even if you disable them by feature flags, you still have a complaining security scanner.
This has been one of the long-standing wishes for the Collector Contrib, is not to have 300 components in one repo, but to make it possible to have your own publicly hosted repo.
And why isn't that? There's a bunch of reasons. It has a lot to do with stability of the libraries themselves. It's like, breaking changes are very hard on external repositories, and much easier when you control 300 of, you know, in one place.
Pierre Mariani 00:51:30 Got it, got it, thank you, yeah. Maybe that's something also, once the library becomes more stable, it becomes more feasible, and…
Joshua MacDonald (Microsoft) 00:51:37 Right, once you have the 1.0, like, stability guarantee, then you can kick things out into their own repositories, in theory. But I think we will also come back to this OCB question of whether we need a builder that can then assemble binaries, you know, with the main function that has all… and that shouldn't be that hard, because we have the static linking stuff, the linkme.
crate doing a lot of the heavy lifting, so maybe we… it's easier and go, even.
Pierre Mariani 00:52:06 Thank you.
Gokhan Uslu 00:52:07 About the OCB stuff, I wanted to mention the OCB, the official one. The version of it is coupled with the OpenTel Go-based collector's version.
So I'm not sure if that's very usable with that regard, but…
Joshua MacDonald (Microsoft) 00:52:22 It might be one of the major problems.
Laurent Quérel 00:52:24 Whoa.
Joshua MacDonald (Microsoft) 00:52:24 It generates a main file that's totally dependent on the current library versions.
Gokhan Uslu 00:52:30 But talk… Yeah, go ahead, sir.
Laurent Quérel 00:52:34 And I'm not sure that we… I mean… for us, in the situation where we are, I mean, it's not so much to do, To recreate a binary, even if we split in multiple repo.
I mean, it's just basically nothing. So do we really need to inherit this OCB stuff?
In our case, I'm not sure.
I don't see the real value.
Personally, I mean, today, we can do that just with the cargo build, dash dash feature, and done. So there is no need for a CV to pay. In other words, if we have a multi-repo staff.
Yes, I agree, we need to have, To update, basically, the dependency dynamically, based on the selection of what the end user wants to achieve.
But again, it doesn't look like a big rock.
Joshua MacDonald (Microsoft) 00:53:32 Alright, I think we can leave that question open, anyone wants to think about it.
And now I want to… so the follow-up needed was me making notes. Let's move on. Gokhan, has a point here about the operator, and actually, I'm gonna ask questions about op-amp while we do.
Gokhan Uslu 00:53:52 So, I realize that we mentioned, oh, what if we do put it into OCB, the RAS collector support? I'm like, okay, if you are that mature, maybe OpenTelemetry operator is also in question.
At least in our company, I saw that at Microsoft, there's at least one internal customer that depends on it, and if you want them to, say, onboard to Rust instead of Go.
they would, still need that operator, but to support Rust Collector as well.
And I wonder, like, if it is a good opportunity for us to… for people, like, when people are using Operator, and then say, like, oh, you go use Rust Collector instead, and very easy way for them to be exposed to Rust Collector, and can also help Our use case internal.
Joshua MacDonald (Microsoft) 00:54:51 I think we're gonna end up talking about this in about 9 months, my question… my guess.
Currently, the hotel operator targets the Go collector, but it's… the coupling is through configuration syntax only, as far as I.
Gokhan Uslu 00:55:06 Yeah.
Joshua MacDonald (Microsoft) 00:55:07 So, one of those touchy topics is whether we ever implement compatibility for GoCollector, which… or Kupeg, which I sort of don't want to, but… but would we ever consider a driver for the OpenTelemetry operator that just knows about Rust collectors instead of Go collectors, maybe.
I noticed that we've started saying Rust Collector, but, So, so I think this is a good question I don't have an answer to. Anybody else?
And… Does anybody for… have a minute to talk about the current state of our op-amp support?
Albert Lockett 00:55:55 Yeah, I can… I can speak to it. Did you have any specific questions, or did you just want me to, kind of.
Joshua MacDonald (Microsoft) 00:56:01 I was fielding questions internally, and I realized I didn't quite understand it well enough, but, one of the… so, my understanding of OpAmp is it can be used in a bunch of different ways. You could use it just to, like, establish a Like, an observability pipe to your vendor, for example, just to, like, know which… which collectors are running, for example.
But also, I've seen configurations where, like, the configuration is empty, except to say, talk to my op-amp, and I'm gonna get my configuration from op-amp.
And, the question was sort of, like, how do we make that reliable? Is that a reliable path where, like, if I want to have a collector that just has an op-amp configuration to get its configuration, so dynamic control plane completely, is that feasible?
And then the question was really about reliability. Like, I don't… I want to make sure that I can start my collector, and then what if the op-amp service goes down? Could I use my stale configuration from the last time I got one?
that's the sort of question I was fielding, and I didn't have good answers. I was just saying, I know we have OPAM, but I don't know exactly how complete or how, capable it is.
Albert Lockett 00:57:14 Yup. So, Yeah, so currently, like, what we've implemented is we have this controller… so, I guess the short answer is, like, yes, you can start your, your data flow engine with just, like, the controller extension, to tell it, like, go talk to the op-amp server, and then, what it expects to do is it will send, like… it only works over WebSocket, to be fair, that's another thing, so we don't have HTTP support yet.
So it will go talk to the op-amp server and say, hey, like, I'm here, here's my current config, and it expects the, the op-amp server to send it a server-to-agent message, basically with, like, the config of its… of it, the engine config, basically, all its pipeline configurations, and then it just does, like, the same live reconfiguration that you would do through, like, the… the admin API, and then it sends its… The configuration is applied back as the… as the server to agent message.
And so… but, like, the… you know, there's some stuff in, like, the off-amp protocol about, like, how you configure, like, like, self-telemetry, like, like, where does… where does that go, and, like, configuring OTLP endpoints and, like, cert management, like, we don't have any of that implemented yet, And I guess, like, to answer your other question, do we… yeah, so, in terms of, like, do we just basically, like, keep reusing the old config until we can fetch a new one? Effectively, effectively, yes. Yeah, so, like, it'll… your engine starts up, it's got its config.
the controller extension is trying to talk to the op-amp server and say, hey, like, what's my… what's my latest config? Or, like, waiting for a new config to come back to it, but if nothing's coming, then there's no configuration update, and it just continues to keep reusing the same configuration that it has.
Laurent Quérel 00:59:03 And to comment on that, the reconcil… reconciler system that we have inability.
Into the system.
When we receive a configuration that is strictly equivalent to the existing one.
It's a no event, or no up.
So in the case where we start, we get the previous version, and the controller finally gave us a configuration which is exactly the same.
Does that mention?
Joshua MacDonald (Microsoft) 00:59:34 Cool, this is what I was looking for. I think the… there's sort of… the concern I was address… was being asked about was really about how reliable is this from, like, when the op-amp server is missing could I then start with my last known configuration? It was just a feature request, really. And thank you, I have now learned.
Laurent Quérel 00:59:55 Just for information, at F5, we rely on that. It's not saying that we… there is no bug, but definitely, that's something we built, because we want to use it.
Joshua MacDonald (Microsoft) 01:00:11 I think we do.
Albert Lockett 01:00:12 One comment I would say with the last known configuration, though, would just be, like, if your process goes away, then it doesn't start up with the last known configuration. It'll start up with, like, whatever it has as the dash dash config argument.
So, like, that, you know, just to be aware, like, that's what would happen if the process was, like, killed, necessarily.
Joshua MacDonald (Microsoft) 01:00:30 Yeah, that's kind of what I was… that's what was being asked, really, and I was imagining, like, a… like a… an op-amp proxy that would just say, I… I am returning what I had stale, or something like that. But, we can… we can take this offline. It's just a question for the… fault tolerance, I guess.
But thank you very much. It sounds, good, and also good to know that you are relying on it.
We have reached the end of an hour.
As we always do.
Thank you all.
Thank you. Enjoy your day. See you next week. Cheers.
Laurent Quérel 01:01:08 Okay.
Drew Relmas 01:01:09 Bye, everyone.
