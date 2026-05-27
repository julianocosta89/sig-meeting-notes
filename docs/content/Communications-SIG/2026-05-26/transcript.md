SIG: Communications SIG
Date: 2026-05-26
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/LDmQxcjUwXKTWLQRWQXu2VbWi2TG6Orcz8dkakuFPXZjDUHPh__VDzGGEs7neQZ8.nrP-nuCm6mFqx8cv
============================================================

## Zoom Recording Transcript

**Pratik** 05:14 Bye.
**Tiffany Hrabusa** 05:21 Hi, Bertita, how are you?
**Pratik** 05:24 I'm good, Agun. How are you?
**Tiffany Hrabusa** 05:26 I'm good, thank you.
Jay and Vitor have both said they won't be able to make it today.
And I know that, Severin is on vacation.
So, we may not have, much to talk about today, but we'll give it a few minutes and see if anybody else comes.
**Pratik** 05:46 Okay, sure.
What about Jay? Is he coming?
**Tiffany Hrabusa** 06:51 Sorry.
**Pratik** 06:53 What about Jay? Jay, he's coming?
**Tiffany Hrabusa** 06:56 No, Jay is not coming. He said he had something, very important he needed to take care of, so, he did, send an update to the… internal comms channel, I can… Okay, so he said, The Explorer project is progressing well.
He and Vitor are working on implementing some new guardrails to help new contributors, figure out the best ways to contribute.
And, he's working on a few other docs for declarative configuration, and then he's also starting an LFX mentorship, that will help with, the information display of, the Explorer.
So that was the update he typed in our channel, but, he said that he would not be able to make it, so… Did you have anything that you wanted to talk about today?
**Pratik** 08:05 Actually not, I'm not, too much active right now, because, I'm, like, in the next, 15 to 20 days, I'm planning to relocate, because, my job is too far, like.
almost a kilometer away, so all… I'm, like, very messed up, like, what to pack, how to go, what to…
**Tiffany Hrabusa** 08:25 Understood, understood. That's a very exciting thing, though. But yeah, I think right now we are all very, very busy with Lots of things that are, unfortunately, not open telemetry, so… It's understandable. Well, in that… in that sense, if you don't have anything and I don't have anything, it's about 4 past the hour here, so I'm going to say that we just adjourn, for today, and, we'll… Come back in 2 weeks, and hopefully more people will be here.
**Pratik** 09:00 Okay, sure, sure. just one advice, like, I have to start contributing on a collector, so, like, I don't have much, knowledge about the collector. Means, I do have, I have views, but, internally, how the collector is returned, so I don't have, but, I want to be a part of Collector. How should I start contributing?
What could be the…
**Tiffany Hrabusa** 09:21 Yeah.
**Pratik** 09:22 onboarding process.
**Tiffany Hrabusa** 09:24 The collector SIG is one of the biggest SIGs.
And their meetings are, large. They have a lot of attendees. So, My recommendation would be to, attend a few of their meetings. They have, because they have so many people, they actually stagger their meetings. So, each week, it's at a different time.
This week… sorry, this week, I think it's, It's actually, today, I guess it might be tomorrow your time.
It's at 5 p.m, U.S. Pacific time.
**Pratik** 10:14 Okay, yeah. Which is Morning.
**Tiffany Hrabusa** 10:16 minus 7, so yeah, it's your morning, so you could join that one. That one is probably the least attended, just because there are fewer people in, the… those time zones.
But that might actually be good. You can kind of just chat with them.
when the meeting is bigger, it's harder to just have a conversation like this, because there's usually a really long agenda, right? Like, people have things that they… that they need to talk about. So, if you get a chance, in your morning, maybe you would want to try, attending that.
As far as what their priorities are right now, they're working on, stabilizing a few specific components.
Do you have access to their notes document?
for their meetings, let me see if I can find the link. I can send it to you.
**Pratik** 11:12 Actually, like, I wanted to go into, like, SDK assign a collector for contribution, because, yeah, I just wanted to explore, but, you know, like, blindly going and contributing to any report doesn't make a sense, yeah, like.
Being a specific part of a particular repo really helps a lot to understand a particular repo as well.
**Tiffany Hrabusa** 11:32 Yeah, yeah, and the collector has multiple repos, so they have the core repository.
Which has the… the core binary for the collector, and just a handful of the components that they package in the core distribution. And then there's the, contrib.
Repository, which has all of the other components.
there's, you know, 100 or more components. So those live in the contrib repo, and then they also have The collector also manages the operator repo, they have a releases repo.
And There might be one other one. But let me… Like, I…
**Pratik** 12:21 Are you active in Collective?
**Tiffany Hrabusa** 12:24 I am. I mean, I don't… I don't contribute directly to them, but because I work so heavily on the collector documentation, I attend their meetings when I can, and I try to pay attention to what's going on, but it's a busy SIG. There's a lot going on there. So I just put in chat the link to their meeting docs.
And you can get a sense of, first of all, just recognizing the people's names. You'll get to know, like, who…
**Pratik** 12:54 B.
**Tiffany Hrabusa** 12:55 Who's kind of running the show?
And then they usually… you can see the first item in the meeting agenda is usually going through the priority issues for stability. So you could even check that out and see if there's anything there that, you would be willing to contribute to.
Or able to contribute to.
And then I would also just review it to get a sense of, like.
The issues that people are working on right now, and, what kind of… Like, how they frame their questions, and that kind of thing.
That would be my recommendation. If you have lots of time, you could also watch a few recordings, from the SIG meetings, because these meetings are always recorded. So, you can go back and get a sense there. But I know that the top priority right now is stability.
So yeah, I would… that would be my recommendation to start.
**Pratik** 13:50 Okay, okay. Thank you, thank you so much.
**Tiffany Hrabusa** 13:53 Yeah, no problem. Hi, Mike, welcome!
**Mike Blum** 13:55 Hi, Tiffany. Yeah, I just wanted to introduce myself. I used to work with Jay DeLuca at, Toast.
**Tiffany Hrabusa** 14:02 Hell yeah!
**Mike Blum** 14:03 working the Golang side of the hotel, Explorer, and so I just wanted to, like, dip in and kind of see how the communication SIG works, because I've never really interacted with any OCIG except, like, the GoSig, basically. So, hi.
**Tiffany Hrabusa** 14:17 Yeah, yeah. Hello, welcome. Yeah, Jay couldn't make it today. He had.
**Mike Blum** 14:21 100%.
**Tiffany Hrabusa** 14:21 Something more pressing that he needed to take care of.
Prateek and I were just talking, actually, about, how to get started in the collector SAG, so that was… you didn't miss much in the conversation, because we weren't really talking comms stuff.
**Mike Blum** 14:37 Good.
**Tiffany Hrabusa** 14:38 Yeah, to be honest, the communication sync is stretched extremely thin right now.
**Mike Blum** 14:45 But, yeah.
**Tiffany Hrabusa** 14:45 We are…
**Mike Blum** 14:47 Congratulations. Graduated.
**Tiffany Hrabusa** 14:49 Yeah, it is… I mean, congratulations to everybody. It is definitely an achievement that's owned by the entire community.
So… Yeah, it's, we're heading into, Northern Hemisphere summer, and so that will naturally mean less availability, but also.
All of the maintainers and approvers are also, dealing with some stuff, like, life stuff that's going on outside of OpenTelemetry, so… Availability is… very stretched right now.
If you are interested in helping out, feel free to take a look at any open issue. We… comms does not, have any gatekeeping, as far as who can review things, who can, contribute things.
The only… the only time you might get a little bit of pushback is on infra stuff, like, for, like, the website build and repository infrastructure, because we do like to keep just a little bit tighter controls on that. But otherwise, documentation, blogs, registry.
We also have the Ecosystem Explorer, which I'm sure Jay has told you about, and Prateek has been… has been working on that as well. So, yeah.
Yeah, so anything, anything you see, feel free to, pick up. If you… have questions about, contributing, the… the website, OpenTelemetry website, does have a contributing section that is actually specific to the communications sake. It's not project-wide.
So there's, a bunch of information there, and we're, always on Slack. You can always ask us any questions, but…
**Mike Blum** 16:42 Better.
**Tiffany Hrabusa** 16:43 Yeah, we don't have much of an agenda today, because, there's not much to talk about. Prateek, do you have anything to add?
**Pratik** 16:51 No, no, no, not. And actually, I see the ecosystem is really growing very well. I see the contributors, like.
pinging up on the Slack, and… Yeah, it's taking a really good peak right now.
**Tiffany Hrabusa** 17:07 Yeah.
**Mike Blum** 17:08 Progress.
**Pratik** 17:09 most of the seniors have also messaged me that, like, how to start contributing. I'm just pointing out to them on our Explorer report, just go there, like, contribute, I really need them.
Yeah, it's… Yeah.
**Tiffany Hrabusa** 17:24 It's one of the, if not the.
fastest growing sub-projects within OpenTelemetry right now, and Personally, I think it's because it has a front-end component, so it's really fun to develop.
instrumentation, let's be honest, can be kind of boring. So, yeah, I think, I think it, it, it has that excitement factor, so it's definitely, it's definitely been thrilling to watch.
Do you have any other questions, Mike?
**Mike Blum** 17:56 No, I just wanted to… I've got my, the PR I've been chewing on, it's just research so far, and I was just, like, surfacing it, if anyone had any commentary, because I think this is, unfortunately, as far as I can tell from reading all the comments and everything, and tell me if I'm wildly off-base here.
We have Java Agent. Java Agent's basically, like, in prod, more or less.
But then hot behind it now, we have JavaScript, Golang, and Python all trying to kind of be integrated into the ecosystem Explorer, kind of basically simultaneously. And all three of those languages and the ecosystems around them are, like, dearly departed from, like, the Gradle Java agent.
Maven way of, like, versioning and doing things. And so, unfortunately, this research topic I have is, like, a little bit more existential than I was really… than I was really signing up for, because it's just like, oh, like, in Go, you can, like, pin different versions of things, and there's no really, like, omnibus version of, well, anything. Like, Go itself, I suppose, but, like.
that's it. And then you have, like, toolchains and things like that. So what I wanted to, like, surface this topic, because I think it's gonna affect, like, Python is the same problem, JavaScript is the same problem. I wanted to kind of surface this issue to be, like, make sure I'm on the right track before I, like, go off on the deep end and, like, you know.
figure out the instrumentation story for all of Golang, like, and then… but we come back and we're like, oh wait, no, we want to, like, reimagine how we're doing, like, the metadata YAML files and stuff like that.
**Tiffany Hrabusa** 19:20 Yeah, first, thank you, because I know, that this research is absolutely necessary, and I know that, Jay… No, it really is, like, to be able to, obviously.
Jay started with Java because it was what he knew, and so that made sense, but he also… our grand vision is that this ecosystem explorer can map the entire world of OpenTelemetry, so… We need experts like you who can come in and do that.
I don't have enough knowledge. Maybe Pratik can take a look at your issue. He has worked on the Explorer a little bit.
what I would recommend, if you… if you expect that, the go… trajectory is going to line up more closely with Python, or… I don't know, anyone else? Maybe… jumping into the Otel Python Slack channel, and just saying.
Is there anyone who would be willing to kind of just brainstorm with me about how this could look so that we don't… we don't… Go in the wrong direction, or end up.
**Mike Blum** 20:36 Yeah, I'm kind of worried, like, all three of us… all three streams are gonna basically reinvent wheel here, is my concern.
**Tiffany Hrabusa** 20:41 Exactly, yeah. So, I think it would be… I think it would be a great idea if you want to take it on, to, to put it into Slack, in those channels for the different language SIGs, and just say that, you know, I've started jotting down some ideas, but I think that this is going to overlap with your implementations in the Explorer, so if we could… maybe flesh out all of the different edge cases and figure out how we can make this work for everyone. That would be a good way to go.
If you need specific advice from the Ecosystem Explorer developers, that Slack channel is probably the book.
**Mike Blum** 21:27 Yeah, I'm in that.
**Tiffany Hrabusa** 21:28 as well.
**Mike Blum** 21:28 Yeah, I'm active in that one. I think… What I was wondering is, very early, back in October, November, I went to the GoSig with a very early rendition of what this is, like, back before we knew about Weaver, before we knew about a lot of things.
And I'm wondering if I should, like, go back to the SIG and be like, okay, that was in the fall, here's kind of where we're headed, does this pass the sniff test for you all? Because I think the thing that I'm the most, like, a little hesitant about is, in the Java world, the Java SIG, like, put the metadata YAML files in the actual, like, upstream Java agent.
contrib… repos.
I don't know how that'll work in the Go world, or the other languages, as an example.
It would be good to get, like, buy-in, I guess, from the SIGs earlier, sooner rather than later, I guess, on, like, do we need to operate as, like, a standalone thing where we're just gonna hoover up the repositories and package definitions and build the metadata yAMLs ourselves and track them?
ourselves? Or is there some, like, path, paved road here where the SIGs slowly adopt metadata yAMls on their own?
I don't know if you've all, like, prosecuted that question yet or not.
**Tiffany Hrabusa** 22:38 So, I know that, the collector's SIG.
has… because the Ecosystem Explorer is meant to, map the massive number of collector components and all of that kind of stuff.
**Mike Blum** 22:55 There are many.
**Tiffany Hrabusa** 22:56 Those components had some form of metadata already, but not, not enough to… fully power the Ecosystem Explorer. So, I know that, Jay has been working with Pablo to modify, the, the metadata that exists. So… I do think, at some point, the idea would be to go to a more, metadata-based Repository setup that… that we could draw from directly.
I don't know how that would be implemented in Go, but I do know that they have… whereas Java kind of started with the metadata.
**Mike Blum** 23:42 Right.
**Tiffany Hrabusa** 23:43 On the collector side of things, they have been… modifying and augmenting what's there. So it has been, a manual process that they've been just trying to set up that in the new metadata YAML files that exist, they need to have, like, there are now new required fields that have to exist for each component.
So, yeah, I think, I think finding a champion in, the Python SIG who can kind of be your, Your partner in crime, as far as…
**Mike Blum** 24:22 Yeah.
**Tiffany Hrabusa** 24:23 Yeah, yeah, would be, would be a good start.
And then, it absolutely can't hurt to go back to the GoSig with it. And if you knew…
**Mike Blum** 24:32 very nice people. I just want to make sure I, you know, when I bring it down the mountain, I want to make sure I'm, like, saying the right things, and don't just, like, hand them something, and they're like, well, this is a nice idea, and then we try to implement it, and then, you know…
**Tiffany Hrabusa** 24:43 Yeah, yeah, I totally get that, yeah. Yeah, I would start, besides Python, I feel like you told me another language thing, I can't.
**Mike Blum** 24:52 The JavaScript one is the one I've been seeing chatter about, and, like, so Jay made this one issue, let me go find it, And it is supposed to kind of draw together the three… competing is the wrong word here, the three… This one… Go Manavir Docs… Oh, it is right here, this guy here.
this dude. So this guy here is, I think, trying to attempt to collate all the research and consolidate what… because we're solving, like.
eerily similar… I think there's gonna be, like, a bit of an uncanny valley here at one point, where it's just like, oh, you can pin different versions of a module under a larger semconf, like, that is something that all the languages have that problem. Even Gradle has this problem.
So I think we're trying to… consolidate what the mapping is going to look like, but I also want the weigh-in of the SIGs, because it depends on where these metadata files live, in my opinion. Like, if they… if the SIGs have to merge the Yamadata… the Yamadata files, wow, under-caffeinated this morning.
**Tiffany Hrabusa** 26:06 We're making up words.
**Mike Blum** 26:08 Right, words! What are they? Why do we use them?
So I think that's where I've just… it's given me pause as I'm, like, digging into this, because I at one point, hit this going way too hard at it, way too deep. I was, like, messing with the Weaver config in GoContrib, and, like, pushing updates to their branches, and I was like, wait a second, this is… I need to, like, take a step back and make sure we don't… you know.
go a little overboard here. But yeah.
**Tiffany Hrabusa** 26:35 Okay, so JavaScript… Marillia, Gutierrez, who is one of the, POMS approvers, she is a maintainer for JavaScript. So, I am sure that she would be able to answer questions, and would almost certainly be willing. I've just volunteered her for this, but she… she is very familiar with Ecosystem Explorer, and.
**Mike Blum** 27:04 Great.
**Tiffany Hrabusa** 27:05 JavaScript. So from that side of things, I think she would be, a great person to approach.
And then, I'm not super familiar with Python, like the folks who manage the Python SIG, but, let me… you know what? I'll just take a look and see if there's anybody that I've seen pop up in, the… commsig for docs frequently from the Python side of things. Let me just see.
**Mike Blum** 27:32 Yeah, and I don't mean to, like, take on 3 different languages, I'm just trying to find, like, what is the common ground between the three of them, so we don't, like, chase our tails.
**Tiffany Hrabusa** 27:41 Absolutely, yeah.
Absolutely. Okay, let's see who's here.
Ludmila Mokova.
is an approver. Let me see who the maintainers are.
And, Ricardo… I'm not gonna get this right. Maglio Cheti?
Xrmx is his GitHub handle. I've… Ricardo, I've seen, frequently respond to Python-related docs issues, so… he might be a good choice. I've not, interacted with him much, so I can't say for sure. Ludmila is not a maintainer, she's an approver for Python, But I think she might be, if she has time, might be willing to help as well. So, those might be two… Oh, amidionito is another one. E-M-D-N-E-T-O.
our GitHub handle.
is another one I've seen in, docs PRs for Python, so… .
**Mike Blum** 29:08 Thank you.
**Tiffany Hrabusa** 29:10 Lumila's, GitHub is L-M-O-L-K-O-V-A.
**Mike Blum** 29:19 She's on the JavaScript side.
**Tiffany Hrabusa** 29:21 Not Python.
So, Lyudmila and Midio, or Ricardo? I don't… I don't have as much familiar with the Python side of things, so…
**Mike Blum** 29:31 Got it.
**Tiffany Hrabusa** 29:32 But I… those are people that I have seen pop up in docs.
issues and things related to Python, so… That tells me that they're interested in that side of things, and making sure that, But the project is well documented, so… That would be my best guess.
Yeah, I agree, you should not take it on for all languages, but having conversations…
**Mike Blum** 29:58 Yeah.
**Tiffany Hrabusa** 29:58 Having conversations to make sure that you're not recreating the wheel for each one is smart.
**Mike Blum** 30:03 Right. Yeah, I think that's where my head is, and then once we have, like, a rough template, I think then we, like… I think I might take… I want to talk to Jay about this before I go to the SIG, but, like, I think once Jay weighs in on this, I'll go to the SIG and get their input on what they want to do, and then we'll go from there, I think.
**Tiffany Hrabusa** 30:18 Okay, that sounds good.
We still have a half an hour to go. Does anybody have anything else, you want to talk about?
Do you have our… a link to our, meeting notes, Mike?
**Mike Blum** 30:34 Yeah, it's on the Google… Invite…
**Tiffany Hrabusa** 30:37 Yeah.
**Mike Blum** 30:37 Thing… calendar invite thingy.
What's nice is the communication SIG doesn't, run up against the Java and Go Sig ones, because those happen, like, simultaneously.
So it's always…
**Tiffany Hrabusa** 30:47 Oh. Oh.
**Mike Blum** 30:48 I always have to pick which one I need to be in it for.
**Tiffany Hrabusa** 30:52 Yeah.
**Mike Blum** 30:54 doing stuff. But yeah, it was… it took me a while to figure out the… it's always hard to get that calendar subscription thing to work, and then it magically works, and I'm like, okay, it works this time. I don't know why this is so hard. Every time I add it, try to join a new one, it's a bit of a touch-and-go exercise.
It might spin.
**Tiffany Hrabusa** 31:09 Same. Yeah, and trying to share a link from the calendar is really difficult.
**Mike Blum** 31:15 Yeah, I accidentally…
**Tiffany Hrabusa** 31:16 Share the whole calendar, and then…
**Mike Blum** 31:18 Right. At one point, I accidentally subscribed to all Sigs, and I was like, my calendar just went blew, and I was like, oh, this is… no, no, no, this cannot stand.
**Tiffany Hrabusa** 31:26 Absolutely.
**Mike Blum** 31:27 Absolutely not.
**Tiffany Hrabusa** 31:28 Too much open telemetry. Too much.
**Mike Blum** 31:30 I mean, I love OpenTelemetry, don't get me wrong, but I think my day job would be annoyed at me if I was like, you know what, I'm gonna devote every waking hour, and also the hours I'm supposed to be asleep, to OpenTelemetry.
**Tiffany Hrabusa** 31:44 Alright, I do not have anything else. Prateek, did you get the information you needed for getting started with CollectorSig?
Okay. Sure. And… Mike, If you have any other questions, feel free to speak up. Otherwise, I think you have, Some things to get started on.
And hopefully, hopefully next meeting we'll have, a few more people joining.
**Mike Blum** 32:12 Cool. I'll single to Jay, and yeah, we'll get this party going.
**Tiffany Hrabusa** 32:17 Okay.
It was nice seeing you both, and see you later.
**Mike Blum** 32:22 Thank you.
**Pratik** 32:22 Good day. Goodbye.
