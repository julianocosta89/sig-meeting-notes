SIG: Governance Committee
Date: 2025-10-01
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Austin Parker 00:00:25 Mmm…
Trask Stalnaker 00:00:30 Can you hear me now?
Good morning.
Austin Parker 00:00:35 Good morning.
Alolita Sharma 00:02:23 Hey everyone, good morning, good morning.
Trask Stalnaker 00:02:28 Ayy.
Alolita Sharma 00:02:33 Hey, Severin, are you coming to Atlanta?
Severin Neumann 00:02:37 Yeah, I will. Yeah.
Alolita Sharma 00:02:38 Okay, okay, cool. Very good.
I know the rest of us are in the US, so, you know…
Severin Neumann 00:02:47 It'll be… it will be my first KubeCore North America, so, yeah.
Alolita Sharma 00:02:50 Cool. Ted, are you coming?
Ted Young 00:02:53 No, I think I have to skip this one, unfortunately.
Alolita Sharma 00:02:56 Oh, my gosh.
Ted Young 00:02:57 But, yeah.
Alolita Sharma 00:02:59 Are you just traveling, or…
Ted Young 00:03:02 Yeah, it's like, I've got OBSCON and, like, an off-site this week, and then, like, or this in October, and then in November, like, another off-site, and then it was, like, KubeCon in A.
Alolita Sharma 00:03:16 And I've got, like, a…
Ted Young 00:03:18 Yeah, my arms busted, and I've got this cat, I'm trying to take care of it. It was, like, too much stuff, and I was like, I can't be worried.
Alolita Sharma 00:03:27 way too…
Ted Young 00:03:28 Out of… out of 8 in a row.
Alolita Sharma 00:03:31 Yep, I agree, I understand.
Ted Young 00:03:35 well, I guess.
Alolita Sharma 00:03:36 Sometimes, yeah, sometimes it's just too many things going on at the same time.
Ted Young 00:03:41 Yeah. Back-to-back. I actually… I couldn't join the meeting yet last week, because I was…
Alolita Sharma 00:03:47 I was in Seattle all last week, so I was like, gosh.
Ted Young 00:03:53 I'm interested in getting a big push going around, like, an OTEL installer.
Alolita Sharma 00:03:59 Oh, very cool! Thank you.
Ted Young 00:04:01 SIG I've been paying a lot more attention to now, and I think the injector's just a tool. We need to get, like, a package management SIG or something going where we… We kind of take the same approach we did to building the SDKs, where we say, okay, there's all these package managers out there, like, what kind of, like, installation experience can we give an operator?
where they can just, like, install OTEL on this machine, and then that thing will have a scanner that will use LD preload and all these other tricks to just, like.
Austin Parker 00:04:37 Do you know what the injector does, though?
Ted Young 00:04:39 The injector is, like, just the mechanism, right?
Alolita Sharma 00:04:42 Yeah, it's not, it's not…
Ted Young 00:04:44 You have to wrap it up into some kind of big.
Alolita Sharma 00:04:47 It's not the manager, necessarily.
Ted Young 00:04:50 SIG doesn't want to be the everything Sig.
Austin Parker 00:04:53 They're like…
Ted Young 00:04:54 We'd like this SIG to just focus on ZIG and the injector stuff, because that's this really specialized, like, engineering task, and then we can spin up another SIG that can focus on how do we take the operator and everything else and, like, package this up into something.
Alolita Sharma 00:05:12 Actually, that's something that, you know.
For large, large scale, you know, like, we do that.
Ted Young 00:05:21 For management anyway, so we can definitely contribute.
Austin Parker 00:05:26 Can you talk to Alex Bowen about this, Ted?
Ted Young 00:05:30 I haven't talked to Alex Bowden specifically about it.
I've been more talking to, like, the Dash Zero and Stana people and Splunk people.
Because they care a lot more about APM, and… and this is much more, like, table stakes in the APM.
Austin Parker 00:05:49 Yeah.
Ted Young 00:05:50 the infrastructure metrics game, like, if you look at.
Austin Parker 00:05:53 Yeah, I would ping…
Ted Young 00:05:54 They all have an LD preload installer thingy, and.
Alolita Sharma 00:05:58 Yeah, yeah, that's true, that's very true.
Ted Young 00:06:00 We tried to go to compete with OTEL, and they're like, where's your thingy? And we're like, we don't have one. They're like, like… So…
Austin Parker 00:06:08 Yeah, ping Alex, because I know we've talked about this a little bit.
Hugh had some thoughts.
Alolita Sharma 00:06:15 I mean, it's come up even in the past on the collector, in terms of how do you actually manage, you know.
Austin Parker 00:06:21 Yeah.
Alolita Sharma 00:06:22 collector pools and configurations for scaling, right? So, definitely big use cases there.
Severin Neumann 00:06:30 I mean, kids, don't they have, like, sick releases or something like that, and they really make sure that, like, every… every few months they… they push something out that is, like, coherent? Maybe that's also part of that. I mean…
Austin Parker 00:06:44 Well, Kate has…
Severin Neumann 00:06:46 more than packaging, but this whole thing of, like, I mean, I would definitely see that as very valuable to also have somewhere people chase people for docs, and say, like, hey, if you want to release something, those are the things you should be doing. But that's maybe much more than.
Austin Parker 00:07:02 Subtle difference, but Chate's does have… did have an installer. I don't think it's installer SIG, but I know that they had a SIG at one point that built.
Improvements to, like, cube admin, and I guess Cluster API is kind of also this. Like, there is… there are people that work on this on the Kate side.
Ted Young 00:07:26 We have config, right, we have config files now, we have op amp.
Yeah. And so, this is more about, on the one hand, just making an infographic of, like, here's all the telemetry sources, and here's the thing in OTEL that matches that source.
Because there's often more than one thing you could use in some situations. You want to get host metrics? It's like a couple things could grab that for you, but we're saying, like, here's the thing.
Austin Parker 00:07:54 And I don't think we're…
Ted Young 00:07:55 This installer, there's this one piece that's some mechanism for using op-amp to get the configuration for all these things, and do the management layer for… Flipping it on and off and stuff for all of this stuff.
Austin Parker 00:08:08 Nope.
Ted Young 00:08:09 Right, so it's like, it's like we have all the LEGO pieces, and now we're ready to build.
a bit of, like, a product experience around it for, like, IT operator people, and…
Austin Parker 00:08:19 Yeah.
Juraci Paixão Kröhling 00:08:20 And we… Catch the agenda, please.
Ted Young 00:08:23 Yeah.
Let's do it.
Alolita Sharma 00:08:27 Yeah, yeah, that's a good point, though, read. Definitely a valid use case.
Ted Young 00:08:33 Yeah, you'll be hearing plenty more from me.
Austin Parker 00:08:35 Do you want to do the private topic at the end, I guess?
Trask Stalnaker 00:08:39 Yep.
Alolita Sharma 00:08:40 Sure.
Severin Neumann 00:08:44 Do we want any of the review topics that we have? So, taking a look, since we have it there, like, looking into our board.
I don't see a lot of things there. I can show my screen, if you like, real quick.
Alolita Sharma 00:09:01 Yeah, sure. Yeah, sure, 7.
Austin Parker 00:09:03 The other topics are also you.
Severin Neumann 00:09:06 Yeah, most of the topics I put there, I mean, it's also… most of them are not, like, super long, but… Here's the board.
I mean, the only thing that is coming in is, like, at a document that explains to the review process. I'm not sure if we need to do anything with that.
Alolita Sharma 00:09:32 Is that just documentation, Sarah?
I think Josh was gonna… Josh didn't…
Severin Neumann 00:09:39 that the TC needs to do, right?
Alolita Sharma 00:09:41 Yeah, yeah.
Severin Neumann 00:09:42 And document their review process, so this is like… Outstanding for… for a while.
I said, I don't know if there's anything that we can do on that beyond… like, reminding NetTC from time to time that they should be doing something around that, so… Yeah, I don't know.
Any thoughts?
Alolita Sharma 00:10:09 I think that last time, Several Josh Sureth had mentioned that, he would remind the TC, so… when we had the last TC discussion.
Severin Neumann 00:10:22 Okay, yeah, yeah.
Yeah, I see that Morgan asked him here in July, so…
Alolita Sharma 00:10:28 Yeah.
Severin Neumann 00:10:29 Okay.
Anything that's in progress that stands out where we need to… Take a look into, or anything in the waiting for others that has… changed. I mean, I have opened another thread on the whole… Donations and projects and everything, we can talk about them as well, but… Anything?
Alolita Sharma 00:10:56 Severin, what do you… what, are you just asking for conclusion on these open proposals?
Severin Neumann 00:11:02 Yeah, no, is there anything, like, where anybody says, like, hey, let's click into that, or move it from state to state?
Alolita Sharma 00:11:08 From one straight to the other.
Severin Neumann 00:11:10 If there's anything we can move around, but…
Alolita Sharma 00:11:13 Prask on the Kotlin, discussion, I think we had added all our comments on the issue itself, I don't think we've heard anything after that.
Are you on mute, Trask? At least you can't hear you.
Trask Stalnaker 00:11:35 How about now?
Alolita Sharma 00:11:36 Yeah, that's good.
Trask Stalnaker 00:11:38 Yeah, understood.
Alolita Sharma 00:11:40 There has been activity on…
Trask Stalnaker 00:11:42 dot.
They've gotten more people to chime in as… Contributors, which was the concern that we expressed, the most.
I don't know if they answered your specific question.
Alolita Sharma 00:12:02 I didn't see anything, but, Yeah, they kind of responded here in this…
Severin Neumann 00:12:17 I think you might need to go back and review that and see, like, if that.
Alolita Sharma 00:12:20 No.
Severin Neumann 00:12:20 Questions, so… Yep.
Alolita Sharma 00:12:22 Under that.
Severin Neumann 00:12:23 Yeah.
So I think the additional contributors, it looks like it correlates with, like, the call for contributors that we did on the blog, and by that on social media.
So it looks like that's working.
Alolita Sharma 00:12:37 That was very useful.
Severin Neumann 00:12:39 Yeah.
Ted Young 00:12:39 Also, Android taking off, which is the main use for this.
Severin Neumann 00:12:43 Yeah. Right. I think they also have, like, we have a blog post in the pipe as well for Android, I think it will come out today or tomorrow. I think tomorrow, because today we had the TC announcement.
Yeah, busy, busy month with all the blog posts.
Alolita Sharma 00:13:00 Yeah, it was a great post, though, Severin, the ATC announcement.
Severin Neumann 00:13:04 Yeah, we are right now a sick blog post review, and not sick comp or sick talk, so… But, yeah, I mean, it's happening every year in October with, like, GC elections, KubeCon coming up, and a few other things that… for whatever reasons happened… happened at the time of the year.
Yeah, I don't know, like, should we, like, Like, what's the next step here on that, on that, donation proposal. Should we, like, vote on it, and… then give it to the TC review, or… Should we give everybody some time to…
Alolita Sharma 00:13:43 on Kotlin?
Severin Neumann 00:13:45 Yeah.
Alolita Sharma 00:13:46 I think the, last time, at least, what we discussed was that we'd review and ask the questions on the thread. Once, once they have… folks had responded back, then we would actually review once more. I think as far as things were… votes were concerned, the DC had already voted positively in the last discussion, but I think we were just awaiting some clarification before it switched to the TC for in-depth review.
That's what I recall.
But.
Severin Neumann 00:14:21 I think last time we voted on, like, hey, this is, in general, in sense of our project.
Alolita Sharma 00:14:27 Yes, yes, yes.
Severin Neumann 00:14:29 called for contributors, but if I remember correctly, we had the numbers of contributors missing, like, I think that's right.
And I think, like, like, we, we probably, So, so maybe… Do we need another week to review that, and then come back next week and make a vote on it, or…
Alolita Sharma 00:14:50 Sure, sure, we can vote on it next week, so that books are aware.
Okay. Should we just list that as, vote next week?
Trask Stalnaker 00:15:04 I'm good. I'm good with that. I think it's encouraging to… I know we have interest already from existing OpenTelemetry folks, so bringing in the Embrace folks who want to do this, I mean, who are also already contributing.
And a couple more people, makes me feel good about.
Alolita Sharma 00:15:25 Yeah.
Trask Stalnaker 00:15:26 it on to the TC.
Alolita Sharma 00:15:28 I'm just reading through it.
Severin Neumann 00:15:31 I mean, if I see it correctly, mode.
He's contributed to OTEL in the past, apparently.
But yeah, I mean, it's always, always an opportunity to recruit new contributors.
So yeah, but as I said, let's, let's, Let's take another look at it, and then… Circle back to it.
Cool. Since we're at that already, I can also, like… Oh, sorry, with that topic, one below, that one.
on the Ecosystem Explorer. I'm not sure if anybody's aware of that one.
Let me… No, it's a pull request.
Actual laxity.
Project proposal.
so Jay created this tool, that you can use to explore the Java instrumentations.
Which is very, very powerful, so you can go into those and… I think get even some, like, what metrics does it support, what traces? I think you can even do version comparison and things like that.
And he brought this back to comms a few weeks back, and I said, like, hey, from my point of view, this is a potential replacement for what we have in the registry right now.
Because this is, like, at least from what I understood in the conversations that we had in the last few years, this is more what we envisioned, or what I think was envisioned in open tracing for, like, what the registry should look like. And that's why I told him, like, hey, maybe you bring this as a proposal to the community.
And I think… what I would do once again is, like, if we all agree that, like, yeah, this is something… we should work on that, I also tell him, like, hey, let's do a call for contributors on the blog, on social media, because I want to add this as a cadence to all the project proposals, and see, like, okay, how much do people react on that? At least for Kotlin, it worked, right? We had two people show up and say, like, I'm excited about that.
I also told Jay to reach out to Backstage Artifact Hub.
So yeah, there's some… some ongoing discussion on that. So it's less about, like, let's do this, and more around, like, hey, if this is in line with our project, let's provide some support and reach out to people.
Ted Young 00:18:16 I'm also fine with looser oversight for projects like this, because this is.
Austin Parker 00:18:21 Yeah, I don't…
Ted Young 00:18:22 He gets pulled into production, you know what I mean? Right? Like… if… They make decisions, like, we can just change them, so…
Austin Parker 00:18:32 Like, the registry is popular as it is, but I think that, you know, an… It's not, like… Load-bearing?
Ted Young 00:18:43 Yeah, yeah, we're not yet to a point where we have a bunch of users who are dependent upon some format that Think produces.
Sorry, Trask, you have.
Trask Stalnaker 00:18:52 Oh, yeah. I think the advantage that I see to going through this Process is the, the advertising of it.
Because while it's freaking awesome, it's also having been… maintainer in the repo where Jay has been doing all of this work. It is a freaking lot of work. He's put a lot of, not the UI of it, but of the, actually.
organizing and… Documenting what all the instrumentations capture, and instrumenting our tests so that they, you know, automatically capture what telemetry and correlate that, and… it's a lot of work, and so for it to be successful, we need… more than just J. I mean, to be successful across languages, we need.
Austin Parker 00:19:52 Yeah, I guess, well… If that's the case, does it seem like… Does it seem… If it does require a bunch of additional work, I don't necessarily know if it's going to be something that, like… I guess it depends on, like, the type of work, right? Like, is this something that… You know, it's a one-off change, and then it works forever, and other maintainers don't have, you know, don't get their cheese moved.
Or is it something that's gonna require, like, an additional burden, so to speak, for… every other SIG in perpetuity?
Like, if that's the case… you know… I guess my question is fundamentally, like, this seems like a comms project, right? Like, this seems like something that the comms shig Because they're the ones that ultimately own the registry and the website.
Trask Stalnaker 00:21:01 Driven… driven by comms.
Austin Parker 00:21:04 Yeah, and if it's something that's, like, is bespoke, and it works in Java for X, Y, and Z reasons, and it would take a bunch of additional work, then maybe the play should be like, okay, well, let's make it for Java.
And integrate it into the site, and then say, here it is, and then if… you know, just think about sequencing, I guess, right? Like, I don't… I don't think it's good for us to have… Projects like this that are… okay, I did it for X, and now I need to boil the ocean to get it everywhere.
Like, we should be delivering incremental value.
Draw a seal.
Juraci Paixão Kröhling 00:21:47 Yeah, can we perhaps have a subdomain for this one under Opentelemetry.io? Like, what is it called? Something.opentelemetry.io, and then see if it gets traction there.
If it does, then we replace the registry, and perhaps we can add a banner to the registry, saying, try it out, try this new UI, and give feedback, and contribute. Make it good.
And see if it sticks. If it does, if there is traction, we replace it.
Otherwise, just kill it. It's a subdomain, it's not official.
Austin Parker 00:22:26 Yeah, I mean, it doesn't even have to be a subdomain, it could be a separate, like… browser.
Juraci Paixão Kröhling 00:22:31 A subdomain… I feel like a subdomain gives a… a less of an official kind of vibe, like, it's not part of the official website, so removing doesn't mean removing from the whole website, like, it's not… doesn't… is on a band-aid, that you have to remove it from the website and cause pain to people.
It's just a separate repository where Netflix can be pointed to, and, you know.
Austin Parker 00:22:58 Yeah.
Juraci Paixão Kröhling 00:22:58 And if it doesn't work…
Austin Parker 00:22:59 At this point, it's easy to make just… it is easy to make subdomains, so…
Juraci Paixão Kröhling 00:23:03 Yeah.
Yeah.
Alolita Sharma 00:23:06 Yeah, that's a good suggestion, to Rasi.
Definitely.
Juraci Paixão Kröhling 00:23:12 Todd?
Alolita Sharma 00:23:13 Dead, go ahead.
Ted Young 00:23:15 Yeah, the main thing I would want to look at with this is just, like, the part where we're doing this analysis and generating the results, it would be great for that to have some long-term thought into it. Like, I know we're using Weaver for a lot of this stuff.
And for, like, schema generation and schema detection.
And so I would kind of want the rest of this infrastructure around schema, OTEL semantic convention, tooling, and schema stuff to… to at least be coherent with what's going on in that semantic convention tooling sig, so… you know, people were mentioning this is maybe a comms project, but I'm also pointing out maybe this is more like a semantic convention tooling project.
Severin Neumann 00:24:03 Yeah. Now, a few comments on that. So, first of all, I agree with what Trask said about, like, this is advertising, right? We need more people on that, right? This is not something.
Ted Young 00:24:13 Yeah, yeah, yeah.
Severin Neumann 00:24:14 And I remember that Pablo, back in the day, said, like, hey, we do something similar in the collector, so it would be good, like, to rally people around it. That's the one thing. Personally, if… if this is spinning out of comms at some point, and we have a SIG registry, or a SIG ecosystem explorer, or whatever, I would not be sad, right? Because, like, all these things comms is doing right now, I mean… We are lacking resources all over the places, and in my experience, like, keeping those things too long within comms also adds… like, why should we do that, right?
Alolita Sharma 00:24:49 Yeah.
Severin Neumann 00:24:50 I'm with curiosity that, like, let's put it on a dedicated domain, and then at some point, like, I talked with Jay about this already. On the registry, we can do a banner and say, like, hey, try out the new Ecosystem explorer.
give us your feedback, whatever, and if over time we figure out, like, hey, this is the thing to do, then we can get rid of the registry, and I'm more than happy to have other people take care of that, right?
and I said, the main purpose for me is, like, not oversight, but more, like, really people around it. I told… I said, Jay as well, like, reach out to Backstage and Artifact Hub to see, like, other projects within CNCF, if they're interested in seeing, like, how can they make use out of that.
Yeah, it's just evolving, and at the end, I think, like all the other projects, it lives and dies with more contributors.
Ted Young 00:25:44 I think Weaver, in general, like, this is kind of, like, new hotness in OpenTelemetry, right? Like, we've matured enough that now there's this second layer of stuff getting built on top of OTEL, and… And we're doing a lot of exciting things with Weaver and looking at it around schema detection and analysis and stuff like this. So I would… that would be my one request, is to work with that thing, just to make sure if there's some part of this that we have to roll out to all of the contrib repositories, that that thing is… is just lined up with the rest of the schema.
Severin Neumann 00:26:17 Yeah, yeah, yeah, no, that's a good point. I will let him know that, like, Weaver is, is, definitely a SIG that, or a group of people that should look into this as well. I think that totally makes sense, yeah.
Looking at time, we have… 3 minutes before we have, like, the private meeting.
Trask Stalnaker 00:26:35 our private…
Juraci Paixão Kröhling 00:26:36 We're not having that.
Trask Stalnaker 00:26:38 move till next week. Sorry, I posted in the GC chat.
Severin Neumann 00:26:41 Sorry, I did not… I did not see that. Okay.
back time. But just to confirm on that, like, I can go ahead with Jay and maybe even do, like, a call for contributors on the blog and social media and see, like, who is interested in contributing to that.
Ted Young 00:26:56 Yeah.
Severin Neumann 00:27:02 Do we want to stay on, like, do a quick review on the other donations and project proposals as well, or jump to any of the other topics?
Trask Stalnaker 00:27:15 The quick review of the donation proposals is… I think, just to make sure we aren't dropping any…
Severin Neumann 00:27:22 Yeah. What do we have? Elastic, the PHP one, it's moving, did something, so… at the back of things, the C++IC was also, like, looking at it, and did an analysis on, like.
Hey, can they migrate off their custom implementation to what the community has already, and yeah, there's some things going on on the back of it.
Yeah, I… I don't know what else is missing, if we also need more people that are… willing to contribute to it, but my understanding is that the PHP seg is super eager to have that.
added to the project, so… yeah. I don't know if… if there's anything blocking, or if we also… Want to find some time, as of this week or next week, to vote on it and say, like, yeah, it's going to happen.
Alolita Sharma 00:28:17 I think, Severin, probably we should just give guidance on the GC channel to… for everyone to make sure they've read through the… you know, the open issues on each of these donations, and then let's do a vote on all of them next week. Okay. Like, so that it all gets, you know, kind of at least addressed.
Because, otherwise, you know, it just is open-ended, and…
Severin Neumann 00:28:44 Yeah, I…
Trask Stalnaker 00:28:44 Okay.
Severin Neumann 00:28:45 Prepare a little bit on that, and then we can…
Alolita Sharma 00:28:48 Yeah, just, just, you know, because we have a nice list here, and most folks have, you know, should read through it.
Because I think, as you said, the Elastic PHP one is actually quite well known, so…
Trask Stalnaker 00:29:03 And that, that one has already gone through due diligence.
Severin Neumann 00:29:07 Exactly.
Trask Stalnaker 00:29:08 Just waiting for us to… Rubber stamp it.
Severin Neumann 00:29:12 Yeah, yeah, I think there's some, the requirements.
But it's more like… and that's maybe something I need to reach out to the Elastic people to confirm that, like, yes, what the TC and PHP Sig and C++IC are requesting, we are going to do that. We understand.
like those requirements, and we are going to implement them. I think that's maybe missing as well, but I can circle back to them.
Trask Stalnaker 00:29:40 Okay. Yeah, because it looks like Pablo last moved this to waiting on others, which makes me think it's not ready for a vote.
Severin Neumann 00:29:50 Oh, I think that was before the… Oh, when did he move that?
Trask Stalnaker 00:29:54 The very bottom.
Severin Neumann 00:29:56 Okay, yeah, okay, okay, okay, okay, okay, okay. Yeah, yeah, there it is, yeah. And I will circle back on them and see, like, that, like, when, whenever someone reviews it, that it's clear, like, yeah, they're committed to do that.
Awesome.
Trask Stalnaker 00:30:10 Cool.
Alolita Sharma 00:30:11 Cool, cool, thanks.
Severin Neumann 00:30:13 What else? The Dart one?
I think last action here was that I also… added a comment and said, like, hey, Michael, you can go ahead and write a blog post to rally people around it, because again, I think the blocker is having more people, right? That was my main understanding, like, they want to donate some code, but right now.
There's no clear understanding who's going to contribute to that.
Ted Young 00:30:47 Yeah.
It's too small. It's just, like, one person.
Alolita Sharma 00:30:52 Yeah.
Severin Neumann 00:30:54 The… I think there was another one, the Audit Sick, or something like that.
Versus.
Ted Young 00:31:04 It's like OpenLeetry.
Severin Neumann 00:31:07 Yeah, I spell, right.
Ted Young 00:31:09 Oh yeah, we talk about the donations, the other one is a project proposal.
Severin Neumann 00:31:13 Yeah.
Alolita Sharma 00:31:14 Yeah, these are donations.
Ted Young 00:31:16 But this is just… just the… the LLM SIG trucking.
Alolita Sharma 00:31:21 Yeah, yeah.
Ted Young 00:31:22 Let me ping, Lyudmila on this.
Severin Neumann 00:31:28 Sorry, so what's, like, can we close that, or should, like, should we circle back to Ludmos?
Ted Young 00:31:34 Let me… let me ping Lyudmila on this, because this was mostly about just getting them to… less about getting, Traceloop to do all the work, and more about allowing the LLM SIG to move forwards.
Alolita Sharma 00:31:49 Yes,
Ted Young 00:31:50 If, like, that's all unblocked now, and people are happy, we could probably close this.
If there's still weirdness around pulling these things in.
Trask Stalnaker 00:31:59 I'd like for… I… I would like for this to be, like… a little bow tied in it, that they are donating it, so that we have, from an IP perspective, we know that we can copy that in without Retaining the copyright notices?
Ted Young 00:32:19 Okay.
Austin Parker 00:32:21 Don't we need something more than just… The checkmark for that, though… Do I need, like, a letter?
If they're actually… er… I hope you're as a trademark.
Ted Young 00:32:37 not suing us when we're adding this… we're not… the reason… we're not doing a, a repo move, to be clear.
Austin Parker 00:32:48 Okay, okay.
Ted Young 00:32:49 repo and then, like, moving it over. We're building all new instrumentation, and for each piece, if it already exists, in OpenLeetry, we're just taking that code and moving it over.
Yeah.
Austin Parker 00:33:04 Yes.
Ted Young 00:33:04 It's all piecemeal, and so really what we need is for them to not sue us when some code shows up that's, like, exactly matching some code.
Austin Parker 00:33:14 Right, but my question is, like, is… this separate… Like, we're not taking any trademarks.
Ted Young 00:33:23 Where we really need access, we're taking copyright, and we're, taking over, the Python, PyPi… Register.
Alolita Sharma 00:33:36 Good stuff.
Ted Young 00:33:38 Like, a V1 in PyPi that's, like, the open LL imagery, and then V2.
Austin Parker 00:33:42 Right.
If it's copyright, I think that's fine. If it's trademark, I think we have to have lawyers, but if it's just copyright, then I think a checkmark will work here.
Trask Stalnaker 00:33:55 I feel like, a blog… just a blog post…
Austin Parker 00:33:59 Yeah, there needs to be something where they… there needs to be a public thing where they say, yes, we are doing this, that… it's… again, copyright you can sign by just…
Alolita Sharma 00:34:08 Right, yeah.
Austin Parker 00:34:09 That you assign it.
Alolita Sharma 00:34:10 Yeah, yeah, you're correct, Austin. I think a blog post would be ideal, because it's.
Ted Young 00:34:15 There is no trademark. Yeah, I should be clear about that. I don't think there's any trademarks.
Austin Parker 00:34:19 Okay.
Ted Young 00:34:20 Holding on to OpenLeetry as a trademark, or any kind.
Austin Parker 00:34:23 Right, yeah, again, I asked because you have it in your… in the post, in the thing there, and I didn't see an answer to it.
Ted Young 00:34:30 Yeah.
Austin Parker 00:34:31 So yeah, as long as we can just, like, clearly state what exactly is being done, then I think a blog post is fine, and we can close it out.
Ted Young 00:34:39 Great.
Alolita Sharma 00:34:40 Yeah, agreed.
Severin Neumann 00:34:45 Yeah, I think donation-wise, we're… Through the list, right?
Yeah. Anyone?
For the audit logging sake, I think I sent a message the other day on that and, like, wanted to know where they are with that.
Yeah.
That's… just something that stalled, so I would just wait for them to come back to us.
Cool. Anything else on the donation and project proposals?
Nope.
Alolita Sharma 00:35:19 No, I think we covered all of these, right?
Severin Neumann 00:35:22 For an FYI, I raised a blog post PR.
Alolita Sharma 00:35:27 Looked at it, 7.
Severin Neumann 00:35:29 I think I wanted to publish it next Monday.
Alolita Sharma 00:35:34 Yeah.
Severin Neumann 00:35:34 Gives people roughly a month.
to… .
Alolita Sharma 00:35:40 apply, and…
Severin Neumann 00:35:41 plot, or nominate people.
Alolita Sharma 00:35:43 Nominate, yeah.
Severin Neumann 00:35:44 So again, I picked, like, four or five days before KubeCon North America to close it out. I don't think we need that much time to probably create the slides or anything for KubeCon, but anyways.
I'm not sure, I think we… we gave people some awards last year, or something like that, or…
Austin Parker 00:36:03 I did.
Severin Neumann 00:36:05 Is this something we want to do again? Is this something…
Austin Parker 00:36:09 Yeah, I figure I'll just have some awards made again.
Severin Neumann 00:36:13 Okay.
Austin Parker 00:36:17 Last year, I just had them made locally. I'll probably do that again, just…
Severin Neumann 00:36:25 That's probably…
Austin Parker 00:36:25 Little loved some local biz.
Are we gonna do… 5?
Depending on the amount of people, but that's what we did last year, right?
I think we did 5 last year, yeah.
Severin Neumann 00:36:44 Oh.
Austin Parker 00:36:45 Er…
Alolita Sharma 00:36:47 Yeah, we did 5.
Austin Parker 00:36:48 Okay.
Alolita Sharma 00:36:49 Yes.
Austin Parker 00:36:55 Awesome. If we're doing 5, then I can go ahead and start looking up looking up things?
Anyone got any fun… Theme idea?
Juraci Paixão Kröhling 00:37:11 Who… who won last year? Do you remember? Do we have a list?
Alolita Sharma 00:37:15 Yeah, there was a list. We did a blog post on it also.
Austin Parker 00:37:19 Yeah, it was… Adriana? And…
Alolita Sharma 00:37:26 Anusha.
Austin Parker 00:37:28 Yo?
Alolita Sharma 00:37:30 For my team. And then, three other folks.
Severin Neumann 00:37:35 Think… how is it… sitcom?
Austin Parker 00:37:37 Alex?
Severin Neumann 00:37:38 the… yeah, Alex.
Alolita Sharma 00:37:39 Alex. Yeah.
Juraci Paixão Kröhling 00:37:40 I had Alex in mind, yeah.
Austin Parker 00:37:42 Yeah, Alex won, and someone else.
Severin Neumann 00:37:45 Yeah, Con, or… what is his name like from the Lambda?
Austin Parker 00:37:49 Yeah, Lambda, Lambda guy.
Severin Neumann 00:37:52 get the most votes, if I remember correctly.
Austin Parker 00:37:55 He did, he had quite a few. Let me see, I can… Improve.
Juraci Paixão Kröhling 00:38:00 Any lessons learned from last year?
that we should apply this year. I thought there was, like, this… .
Austin Parker 00:38:10 Maybe…
Juraci Paixão Kröhling 00:38:12 Could add some limits, like… Yeah.
Severin Neumann 00:38:15 And a third limit to the nominations. So if you go into the form, if we have a few seconds, we can quickly glance over it.
What I did is, like, I sent here, like, yeah, you have a max of 281 characters.
Austin Parker 00:38:31 Yeah.
Severin Neumann 00:38:32 And then keep it short and impactful, I just added it here. And only the first nomination is mandatory.
So, yeah.
Austin Parker 00:38:42 Yeah.
Alolita Sharma 00:38:43 7… 75281.
Huh? Specifically, Y281 characters.
Severin Neumann 00:38:51 I, I think I asked… Like, a suggestion, and it said, like, yeah, tweet length.
Austin Parker 00:38:57 If anyone, that's fine.
Juraci Paixão Kröhling 00:38:58 I was trying not to ask this question, Alvita. I was… I was… I… I hurt myself.
Austin Parker 00:39:04 One… the only, the one thing that, like…
Juraci Paixão Kröhling 00:39:07 281.
Austin Parker 00:39:09 I guess if there was one… one thing that I… I don't know about…
Alolita Sharma 00:39:19 Like, one part of me says, like, oh, we should do nominations, and then…
Austin Parker 00:39:24 Voting?
Juraci Paixão Kröhling 00:39:27 I mean.
Austin Parker 00:39:28 But I feel like we just, like, there's a sort of vote overload this time of year.
Juraci Paixão Kröhling 00:39:36 I mean, it would not be too much of a problem to upload the same voter roll to Helios, Helios, and then ask the community to vote. The only thing that we would need is, like, who are the nominees?
Alolita Sharma 00:39:52 Yeah.
Juraci Paixão Kröhling 00:39:52 This form comes into that.
Austin Parker 00:39:54 So the problem, or the thing with that, though, is that… This is supposed to get more people than just…
Juraci Paixão Kröhling 00:40:03 Yeah, yeah, yeah, just…
Austin Parker 00:40:04 the contributors. And, like, that was… I think that was the thing that kind of, like.
Severin Neumann 00:40:10 winners last year who were, like, more end users, or people that adopted OpenTeller?
Austin Parker 00:40:15 Right, which is good, that's the point.
Severin Neumann 00:40:17 Yeah, exactly. Like, if someone says, like, hey, within my company, there's this person that's, like, the OpenTelemetry champion, and I want, like, 10 people to nominate them. And that's maybe also something what we should advertise and tell people, like.
Austin Parker 00:40:29 Yeah.
Severin Neumann 00:40:30 computers.
Austin Parker 00:40:31 I think let's just advertise it more. Let's just, like… .
Severin Neumann 00:40:38 I think the good thing is, like, that's at least my feeling, that, like, our social media channels get a little bit more attention.
Alolita Sharma 00:40:46 I mean, what happened with the Kotlin thing, right? I mean, we had two people.
Severin Neumann 00:40:50 Jumping on it, like, immediately when we published that blog post.
And we're much better in using our social media right now.
Austin Parker 00:40:58 Yeah. I will point out, last year, we only ran the nominations for, like, a week.
Severin Neumann 00:41:06 Yeah, because we figured out.
Austin Parker 00:41:08 Because we did this very last minute, so yeah, let's roll with it for, like, a month, and see, like, having it out there a month or whatever, maybe this problem will fix itself.
Severin Neumann 00:41:18 Yeah.
And maybe that's also something you can reach out to maintain, since they're like, hey, bring this.
Austin Parker 00:41:24 Yeah, bring this up in your signings, yeah, so let's just publicize it more.
Severin Neumann 00:41:28 Yeah.
Awesome.
Austin Parker 00:41:41 I have just a question.
For the… the group.
So, over in… the… Maintainers… Circle… Every now and then, like, over the past, like, year or so, there's… every now and then, a maintainer for another project will come up, will pipe up and be like, hey, we're having, like.
AI slot PR problems?
And I've been pointing people to our guide… the guidance we published last year about AIPRs, and… They're like, this is great!
And now, like, Jorge or George is kind of, like.
seems like there's, like, some interest, like, oh, maybe we should have, like, a CNCF-level guidance here. So my question is, like, I actually haven't heard anything negative about our policy. Has anyone from their SIGs, or just in general, heard any, like, feedback about this policy? Is it working? Is it not working?
Severin Neumann 00:42:54 I just used it twice this week. So, I have not used it for, like, since we created it, and just this week, I had, like, two situations where I could… I think I told Vitor to use it, I used it myself, where I said to a contributor, hey, thank you for contributing, but… please be aware about this Gen AI policy, and what you have created here is clearly using that, and I think one of them retracted their PRs because they were, like, just not good, and the other one was like, yeah, I will pay attention to that, so… It works.
That's at least my feedback.
Austin Parker 00:43:33 Anyone else?
Trask Stalnaker 00:43:36 I don't think we have needed to use it in any of the Java repos yet.
But I have heard in the… just the hotel maintainers channel, a couple of maintainers… Who didn't know it existed, and asked if we have any such thing, and I pointed them to that, and they were like, yeah, that was what we wanted.
Alolita Sharma 00:43:58 Should we do a blog post on this? Because I think that it would be nice for.
Austin Parker 00:44:03 Mr. Fuck.
Alolita Sharma 00:44:04 Criticize this policy for the project.
You know, and just saying that it's worked well for us.
Austin Parker 00:44:10 Did we already do one on it?
Severin Neumann 00:44:13 I thought…
Alolita Sharma 00:44:13 I think.
Austin Parker 00:44:14 Number one.
Severin Neumann 00:44:17 I think back when we created it, there were a lot of maintainers that said, like, yeah, why do we even need something like that?
Alolita Sharma 00:44:22 Yeah.
Severin Neumann 00:44:23 Yeah, just for the case, but I think… at least… I think… how long do we have it now? Is it a year?
Austin Parker 00:44:29 About a year, that's why.
Alolita Sharma 00:44:30 Almost a year, yeah.
Austin Parker 00:44:31 It was about a year ago. I mean, if you… take it from, like, when we started working on it, I think it's been about literally a year.
Severin Neumann 00:44:39 Yeah, you pushed the first version, like, 11 months ago.
Austin Parker 00:44:43 Yeah.
Alolita Sharma 00:44:43 Yeah.
Severin Neumann 00:44:44 And the only thing right, is that I added that… that piece around human…
Austin Parker 00:44:50 Yeah.
I can, if… If we want, I can take an item to write, like, a quick blog on it.
Alolita Sharma 00:44:59 Yeah, that would be awesome.
Austin Parker 00:45:02 But, okay, I'll also ask next week at the spec meeting, just if there's any other maintainers that have any feedback on it. Okay.
Alolita Sharma 00:45:10 Sounds good, yeah, that's a good, good idea.
But definitely, Austin, do write a short post.
Austin Parker 00:45:16 It's good for us to kind of publicize it. It's been pretty successful for us.
Alolita Sharma 00:45:21 I haven't heard anything negative, actually.
Austin Parker 00:45:25 That's good.
Alolita Sharma 00:45:31 And oh gosh, I know 7. That's a good thing.
Severin Neumann 00:45:34 We have 15 blog posts on Skipping.
Alolita Sharma 00:45:36 Oh, gosh.
Severin Neumann 00:45:38 I mean, a bunch of them have been published, I think 4 or 5, but, like, yeah, we…
Austin Parker 00:45:42 Why do we have so many?
Severin Neumann 00:45:43 Gc election alone is, like, 3 of them.
Kubecon is one.
And then, like, with this, Community Awards, this one, TC election.
Alolita Sharma 00:45:53 DC's one, yeah.
Severin Neumann 00:45:55 And we had a bunch of people, including myself, that came to us and said, like, hey, let's… can I… can I publish some… some blog posts? So, yeah. I don't know why it's always in October. Maybe, like, everybody's like, oh, KubeCon is coming, let's… let's put.
Alolita Sharma 00:46:08 I think it's probably the election and coupon, yeah.
Ted Young 00:46:12 I'm gonna blast you with another one today or tomorrow for Hotel Unplugged.
Alolita Sharma 00:46:18 Oh, cool.
Severin Neumann 00:46:18 I mean, I'm more than happy that we have that.
Austin Parker 00:46:22 What did it.
Severin Neumann 00:46:23 That's a good problem to have. The only thing I want to call out is, like, we need to, like, find out a cadence, so that means, like, if we think about publishing a blog post today, it could take a few days a week to… Yeah, that's actually a good idea, Seven, because you could say that we could do a publishing schedule or something, then get it… Yeah, no, we have one internally, we will not share that with everybody.
Alolita Sharma 00:46:46 Okay.
Severin Neumann 00:46:47 Anybody who's curious about that, I can… I can give some guidance on that, but Tiffany is taking good care of that, so yeah.
Ted Young 00:46:54 M.
Alolita Sharma 00:46:59 And lots, lots of people joining our OpenTelemetry announcement lists.
Ted Young 00:47:04 Oh, cool.
Severin Neumann 00:47:06 We're not use… I'm not using that, maybe we are…
Alolita Sharma 00:47:09 We should, but I'll probably…
Austin Parker 00:47:11 You should, yeah.
Alolita Sharma 00:47:12 of publications, for sure.
Severin Neumann 00:47:15 the other side.
Yeah.
Ted Young 00:47:18 Yeah. Can we automate that? Like, is GitHub able to send out emails? Anyways?
Austin Parker 00:47:24 Github's not, but we could… Oh shit, fucking… If we wanted our own… well, we have… it's a listserv, right? So we should be able to, like, do something where we push… to something.
Alolita Sharma 00:47:43 It's a listserv, yes.
Austin Parker 00:47:44 Yeah, we should be able to, like, have something, like a webhook or whatever, that when… Something happens, it goes and sends an email.
Ted Young 00:47:55 Or, like, compiles a set of things into one email.
Austin Parker 00:47:59 Well, that's… I mean, that… that… Is what you… you would do one email for each, and then, if someone sets their list to digest mode, then they'll get, like…
Alolita Sharma 00:48:09 on an email.
Austin Parker 00:48:10 One email.
Alolita Sharma 00:48:11 Yeah.
Austin Parker 00:48:12 I feel like, you know… I feel like email should make a comeback.
Severin Neumann 00:48:19 I mean, 2003, right? I did some research on the topic once. I wanted to find the first blog post where someone said, like, email is dead, and it's like… 20 years ago, so yeah, I'm all in for Moe's.
Austin Parker 00:48:33 Yeah, no, I think… I think we need… I think it's time for email to come back. Like, we're cooking ourselves with short form, with video, with… with… with… 280, 300 character posts, all this shit. No, it's… Slack.
It's time for us to send letters again.
Trask Stalnaker 00:48:52 I will say that email is coming back among the kids because of their locking their phones in schools now, so they don't have access to their phones, so they can't… but they have laptops, the school, you know.
Austin Parker 00:49:06 books, so…
Trask Stalnaker 00:49:07 They email now during the day.
Austin Parker 00:49:10 Oh, cool. There you go.
I'm down, I'm… I'm… Alright, I have my next quixotic crusade. Bring back email… 2026, the year of email.
Alolita Sharma 00:49:25 Maybe we can give it a cooler name, or something.
Austin Parker 00:49:29 AI mail.
Alolita Sharma 00:49:31 Exactly.
Severin Neumann 00:49:32 It's a year of mail.
Austin Parker 00:49:34 You can't spell AI without… you can't spell email without some of the letters in AI.
Ted Young 00:49:38 I feel like it can't just be email, it's gotta be, like, a pine client on, like, a Razer flip phone or something.
Alolita Sharma 00:49:45 Yes, exactly.
Austin Parker 00:49:46 Mail. Mail talk. E-talk.
Severin Neumann 00:49:51 God.
Alolita Sharma 00:49:51 This is awesome. A male. A male.
Austin Parker 00:49:55 Yeah.
Alolita Sharma 00:49:55 Amyo.
Ted Young 00:49:58 I, yeah, yeah. Excellent.
Austin Parker 00:50:01 AI, AI, AI.
Ted Young 00:50:05 I think.
Alolita Sharma 00:50:05 This meeting has officially crashed. Yes, exactly. We run out of topics.
But I think… I think there was one topic for the GCTC in-person meeting, was… Severin? What was the follow-up on that? You had the first item there.
Severin Neumann 00:50:27 No, that's… I think that's just a copy and paste.
Alolita Sharma 00:50:30 Oh, that's just a copy, okay, okay.
Severin Neumann 00:50:32 Yeah, what's remaining, it's like, that is postponed, it's like your update on KubeCon. Or are we done with Stitch Gen AI, I think? Sorry, Austin.
Austin Parker 00:50:40 Yeah, yeah, no, that was… that was all. I just wanted to, like, get… before George asked me questions, I wanted to have answers.
Alolita Sharma 00:50:53 Okay, cool. And my update was just that I'm… I got the template, I'm working on integrating the sections, and I'll just share it on the GC channel. That's all.
That was just my update, because I'd taken an action item on it.
Yeah.
And then everyone can add to it.
Okay, that's it. I think we are done.
And, Ted, was there any updates on, OTEL Unplugged, in terms of just progress?
Ted Young 00:51:29 Right, so we've got the prospectus, I'd like to circulate that more, but the main thing is just getting a blog post up, for the registration page. So we've got the registration page almost finished.
Alolita Sharma 00:51:42 Okay, very cool.
Juraci Paixão Kröhling 00:51:44 any…
Ted Young 00:51:46 Very much like how we did it for the last Hotel Unplugged, it's just a blog post that has a link to the registration page that's like… Explaining the basics of the whole thing, and also a link to the prospectus.
If people still wanna, sponsor it.
Alolita Sharma 00:52:01 Sponsor, okay, cool.
Juraci Paixão Kröhling 00:52:03 Any constraints for the sponsors? I knew you had some reservations in the past about, you know, one of the only people who…
Ted Young 00:52:09 I was just getting cranky with you, because you were, like… I was just trying to get, like, a head count of how many people would sponsor, and I felt like… like, things were getting complicated, and then I was like, I don't give a shit about those guys, never mind. There's no actual, like…
Juraci Paixão Kröhling 00:52:23 You do now, though.
Ted Young 00:52:24 I don't, I don't, yeah, I've already sent "-0, to the perspective, by the way.
Juraci Paixão Kröhling 00:52:30 Okay, I sent them as well, so after you sent that message.
them as well.
Ted Young 00:52:34 I've never… I was just, like, in the moment, just being cranky, because I was like, how many people want to sponsor? Like, maybe I'll set up a meeting if you jump through some hoops. I'm like, I don't… I didn't care that much.
Click.
Juraci Paixão Kröhling 00:52:45 Alright, so I'm gonna send to a couple of other companies that I have in mind. Great. But, I'm happy to… But yeah, yeah, far and wide, like, if newcomers want to sponsor this, this is totally cool.
Ted Young 00:52:54 You know.
For sure. We tried to keep the sponsorships… Like, costs low, so that… It wasn't just… Splunk.
Juraci Paixão Kröhling 00:53:05 Bodyguardian is officially sponsoring, so I'm happy.
Ted Young 00:53:08 I saw that.
Alolita Sharma 00:53:09 Oh, cool, very cool.
Ted Young 00:53:12 But yeah, that's the next thing, and then just getting the word out, and hopefully getting people to come and attend.
For sure.
Juraci Paixão Kröhling 00:53:24 Cool.
Alolita Sharma 00:53:25 Yeah, do we have new stickers for this year, or something? Like, cool stickers for our tents?
Ted Young 00:53:30 stickers for Hotel Unplugged.
Yeah, I mean, we had that cool, like, old, like, MTV logo.
Alolita Sharma 00:53:39 Yes.
Austin Parker 00:53:39 I think we should do… yeah, bring back the MTV logo. I thought that was great.
Ted Young 00:53:44 It's a joke.
Austin Parker 00:53:45 I didn't.
Ted Young 00:53:46 I have no problem with the… the graphic design.
Austin Parker 00:53:49 I have no… yeah, I have no clue where the originals are anymore, because that was a job ago, but…
Ted Young 00:53:56 Yeah.
At any rate, I liked how we did it last time, I don't…
Austin Parker 00:54:01 Yeah.
Ted Young 00:54:02 Yeah.
Austin Parker 00:54:04 I was… I was hoping Morgan would be here, because I wanted to ask about, the observatory.
art, but… independent of that, I guess since I'm making the shirts… Should I just go… should we just keep… should I… should I go with the baseball theme for Atlanta?
Alolita Sharma 00:54:24 I thought we decided, and…
Austin Parker 00:54:27 Well, we're doing the baseball shirts, but, like, for stickers and accoutrements.
Alolita Sharma 00:54:32 Oh, that's not a bad idea. Why not?
Juraci Paixão Kröhling 00:54:35 Are we gonna get graduated by Atlanta?
Alolita Sharma 00:54:40 I think they're almost on their last, part.
Austin Parker 00:54:44 Let me shake my magic 8-ball.
Outlook hazy.
Juraci Paixão Kröhling 00:54:49 Okay.
Austin Parker 00:54:49 I mean, I think it's… I don't… I do not… I… I have… I ha- I know no more than I have told you, which is… They are trying to do these adopter interviews and get them approved, and…
Alolita Sharma 00:55:02 Yeah, there.
waiting on two, from what I've.
Austin Parker 00:55:06 Right, and the process is, is that the adopter interviews get done and submitted and approved, and then those Go up as part of, like, the graduation… packet, I guess, and then there's a public comment period, and then they vote.
Alolita Sharma 00:55:23 Yes, that's right.
Austin Parker 00:55:25 So that's typically very fast, and they can actually do that in October, but it's really cutting it close. Yes, like, it's cutting it very close.
Alolita Sharma 00:55:34 Yes, because if they have to make announcements and, you know, in the keynotes and call out the project, they have to actually organize that stuff, so…
Austin Parker 00:55:43 Maybe I can, would you like me to actually ping.
Alolita Sharma 00:55:47 The CNCF…
Austin Parker 00:55:49 I mean, I'll ping Emily again and be like… We would love to have some visibility into this, if you wanna…
Alolita Sharma 00:55:57 I can ask too, because I think it.
Austin Parker 00:56:00 Yeah.
Alolita Sharma 00:56:00 be nice to announce at KubeCon.
That's… you know, it would be a big deal, instead of not announcing at KubeCon and missing the window.
Austin Parker 00:56:12 Yeah, well, I mean, I mean… I… surely, like, we would… they would just push it, the keynote, to, Europe, and… No, I think it's a partnership.
Alolita Sharma 00:56:26 To have leverage it, don't you think?
Austin Parker 00:56:28 Yeah, like, I think, I mean, I… Arguably, like.
Arguably, Europe's a bigger stage anyway, but I would rather just be done with this shit.
Juraci Paixão Kröhling 00:56:42 I didn't.
Alolita Sharma 00:56:43 It's important to do it sooner than later.
Juraci Paixão Kröhling 00:56:46 Yeah, no, the only question that I had was, I mean, if we were, then perhaps the t-shirt could feature, like, the mascot.
Alolita Sharma 00:56:52 Yes.
Austin Parker 00:56:53 Well, the mascot is…
Juraci Paixão Kröhling 00:56:55 The mascot will probably end up being a Europe thing anyway. We have not…
Austin Parker 00:56:59 Yet, begun to talk about the mascot.
Alolita Sharma 00:57:02 But.
Severin Neumann 00:57:03 Like, a year ago, right?
Austin Parker 00:57:05 Okay, let me rephrase this. We, the people on this call, have talked about the mascot. I have not talked to anyone involved in Fippi and Friends about actually getting our official.
Severin Neumann 00:57:17 Yeah, probably they then have some rules, and like, all of our great ideas are gone, and we are stuck with… I don't know.
Austin Parker 00:57:23 I think we… I'm pretty sure we get to pick what we want, but I…
Alolita Sharma 00:57:26 No, we can pick what we want.
Austin Parker 00:57:28 There's a process.
Alolita Sharma 00:57:29 Yes, but let's pick it anyway and start the buzz there.
Austin Parker 00:57:35 Yeah, no, I think I'll just probably go with the… I'll just go with the baseball thing, because we'll go find someone to do some logos.
Alolita Sharma 00:57:42 Sounds good.
Austin Parker 00:57:43 to be fun.
Alolita Sharma 00:57:44 step at a time. I'll go and poke around for what's happening on the…
Austin Parker 00:57:48 Last fall. Oh… Yeah, yeah, I'll ping Emily.
Alolita Sharma 00:57:55 Yeah, because I thought that they said that they would… they need to reach out to number 5 if 3 and 4 don't complete in time.
On the adopter interviews. So that's where my understanding… is… Okay, cool. We have a plan. We'll follow up and come back.
Austin Parker 00:58:19 Yeah.
I was also gonna ask if people wanted to go to medieval Times in Atlanta.
Alolita Sharma 00:58:26 What is that?
Austin Parker 00:58:28 You've never heard of Medieval Times? No. It's been on a show.
It's like, am I the only person that has heard of Medieval Times?
Trask Stalnaker 00:58:38 One in Southern California, so I know what it is.
Austin Parker 00:58:41 You know what it is, at least. It's… it's a… Dinner, it's like a restaurant, but it's also, like…
Alolita Sharma 00:58:49 Oh, good.
Austin Parker 00:58:51 But it's also jousting!
Oh, cool!
And you can… and it's like, you get the big turkey leg…
Ted Young 00:58:59 Not the same way, Monster Truck is a pizza parlor.
Alolita Sharma 00:59:04 Oh, I see.
Austin Parker 00:59:05 I mean, it involves, like, okay, you don't go to a monster truck rally for the food. I don't necessarily know if you go to Medieval Times for the food either, but at least the ostensible point of Medieval Times is that it is a dinner and a show.
Alolita Sharma 00:59:19 Jousting horsemanship.
Austin Parker 00:59:21 Yeah, it's like, it's a medieval… People, the servers are in character or whatever?
Severin Neumann 00:59:29 Are they even allowed to call it like that? I mean…
Ted Young 00:59:35 Amazing.
Severin Neumann 00:59:35 Well, this champagne needs to come from… and there was no…
Austin Parker 00:59:42 My only point is that they do have a show… there is a showing on the… on Sunday, which is the Maintainer's Summit Day, and it's at 4pm, so we would all have to leave the Maintainer's Summit to go there, and it's half an hour away.
Severin Neumann 00:59:56 Okay.
Austin Parker 00:59:58 But… Think about it.
We could also do something completely normal, but…
Alolita Sharma 01:00:08 Pretty interesting.
Austin Parker 01:00:10 We could go to the Koch Museum.
Alolita Sharma 01:00:13 Cool, as if… I think the medieval times, like.
Austin Parker 01:00:18 There's all sorts of fun things to do in Atlanta.
Okay, we'll figure it out by next time.
I gotta go.
Alolita Sharma 01:00:29 Good suggestions. Bye. Take care.
