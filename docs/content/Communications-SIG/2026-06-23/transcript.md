SIG: Communications SIG
Date: 2026-06-23
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Vitor Vasconcellos** 01:30 Hello?
**Marylia Gutierrez** 01:31 Hello.
Recognize the t-shirt.
You see?
I thought just the top, whereas…
**Vitor Vasconcellos** 01:46 Yeah.
It's a good one. I also have the socks I'm not wearing today, but…
**Marylia Gutierrez** 01:58 Oh, I have so many socks here. We are doing an event next week, so they send me a bunch of swag. I have, like, 30 socks right now.
**Vitor Vasconcellos** 02:07 I'm gonna ask for another one, and I'll see you again there.
Hey, Prateek. Hey, Jared.
**Jared Lewis** 02:19 Hi, good to meet you, Vitor. Thanks for the response in the Slack.
**Vitor Vasconcellos** 02:24 Robin, thank you for… Hello, cool.
Saturday might be going sometime soon. I think the first item… Home released is… Can you add in?
**Marylia Gutierrez** 04:47 We can probably start with your topic, Rita.
**Vitor Vasconcellos** 04:51 Yep.
It doesn't let me clear my screen?
Oh, what… Yeah, okay, I think I'll need to… to redrawing.
Can… can you share?
Please, I… I need to rejoin and… Let's set the permissions here, but… Okay, we can… we can move to the next one, the… pick the second item.
Alright, alright. So, just to give you some context also, it's… oh, let me share the document.
If you will, also. Yep.
So… We… we got the idea to implement a pull request dashboard, and there's an example from the Java repo.
And it's a GitHub action that actually integrates with Copilot and generates this dashboard.
And… breaks it into some categories and gives some extra visibility, I think.
It… it was Jack's idea, actually, but I think it gives us some extra visibility on… the currents… Taros, or… How can I say a thing?
It's gonna be helpful for us, since we… we've been dealing with so many open PRs lately, and… It's been… at least for myself, it's been… I'm heavy a little bit.
Hard times to… to… to review and to… to… to get an overview of all of them.
And… Yeah, I just added this guidance to the list to get some extra thoughts and see how various he is. I think it's also a good way to… So, I mean, I think it's also going to be useful for… Locale maintainers and approvers also, not only for The repo maintainers and operators, but also the locale, so… Yeah, it does make some space to go hit some parts.
**Marylia Gutierrez** 07:18 Yeah, so I was thinking, for example, the… I was just comparing the amount of PRs, yeah, we are, like, close to 100 right now, hoping, like, 90-something, so definitely a lot to keep track. On the… JavaScript, seg, one thing we did was just, like, as part of the actual weekly, at the end, we always go, like.
open issues, mostly, like, bugs, just to, like, triage, and then we also do, like, PRs on the call. Not actually reviewing, but just making sure somebody's assigned to… to review.
But we, yeah, we started, like, several pages of PRs, and lately we're just, like, at one, two pages. That… but that took, like, a few months to actually get to this place, because we had to, like, keep doing this every single week. But I think, like, yeah, for this one.
Sounds like a good idea, creating this. Well, since Jay is here, and Jay is also working on the Java, any feedback from how this is being used? Like, anything you think we should adjust? Or, like, has this been actually working for the maintainers?
**Jay DeLuca** 08:26 Yeah, I think Trask… Trask is the one who created this originally, and so it's… it's been in use in the instrumentation repo for… I want to say, like, maybe over a month or two, and it's gone through several.
**Marylia Gutierrez** 08:38 It looks like 3 weeks. Looks like 3 weeks from now.
**Jay DeLuca** 08:41 Well, this… this is the… this is the core, so this was… this was adopted after the instrumentation repo.
So, like, after Trask kind of workshopped it there, then we moved it over to Java, too, so, Yeah, I think it's… it works really well, So I would recommend us doing it. It doesn't take much.
Like, it's very… There's no downside, as far as I can see.
Unless we run into some issue with the co-pilot, credits, but… I'm just assuming that that gets… Build to the.
**Vitor Vasconcellos** 09:18 CNC.
**Jay DeLuca** 09:19 No.
**Vitor Vasconcellos** 09:20 Where does the token come from? Because I was trying to do some things with Copilot a few months ago, and I didn't… couldn't get the token. Is it, like, a coupon token, or is it an organization-wide token?
**Jay DeLuca** 09:38 I don't know. I know this… this is actually… This uses, like, the… GitHub, Copilot Framework or something, or Agent Framework?
I forget what it's called.
But I don't… yeah, I don't actually know how the token… is configured for it. I just assumed that it was a CNCF thing, but… And I would assume it would be per project.
But I don't know.
**Marylia Gutierrez** 10:10 I'm trying to remember, because I remember there was a conversation on one that says, like.
asking this question, and I think it was, like, a mix, like, some things is, like, the CNSAP one, but if you are requesting a review, it is your own token, so I don't know… Which token would be for this?
One here in particular.
But I don't.
**Jay DeLuca** 10:38 though.
**Marylia Gutierrez** 10:39 Yeah, but I don't see why not.
try it out? Sounds like a good idea. Like, worst case is, like, it doesn't work, so we disable.
**Vitor Vasconcellos** 10:49 Yep.
Alright, we can, I think it will try. There's also… One other thing you mentioned, the assignment on reviews. I'm just curious, how was it assigned, and is it… random, or someone picked the PR?
**Jay DeLuca** 11:15 Oh, you mean for in Java?
**Vitor Vasconcellos** 11:17 Yeah, it was actually in JavaScript, but if you do that in Java also, None.
**Jay DeLuca** 11:23 No, we… yeah, I wasn't sure if you were talking… we… I don't… the… it's just maintainers and approvers just kind of use the dashboard at will. There… there's no, like… we didn't, use it together or, like, on a schedule.
**Marylia Gutierrez** 11:37 Yeah, for the JavaScript, it was just, like, during the call, it was like, if you see something, you're kind of like, oh yeah, I know this area, I can take a look. It was mostly like this, and you would assign that person to your review.
**Jay DeLuca** 11:55 We do often, I feel like, have some time in this meeting, so it probably wouldn't hurt to spend a few minutes at least going through some.
**Marylia Gutierrez** 12:07 Yeah, we can try, like… so, are you planning on creating this action yourself, or…
**Vitor Vasconcellos** 12:17 Sorry. Yeah, I can, I can pick this one, or…
**Marylia Gutierrez** 12:22 So then we can, like, start from, like, a following week, like, taking a look at this and seeing if there's anything that is, like, no one touched, like, at all, and then we can, like, use the code to assign people.
**Vitor Vasconcellos** 12:35 Unless someone wants to, to, to give it a try and pick this, but yeah, I can also… Can also take a look.
**Marylia Gutierrez** 13:03 I guess we can now go back these efforts.
**Severin Neumann** 13:06 Sorry for being late. Hey, everybody. I was, like, 5 minutes before the meeting, I started something, and then it was 8 minutes after the meeting. Anyways, thank you, thank you for sending me a reminder, Vitor.
Yeah, this is a thing I just wanted to quickly chat about, because, like, I think we had a conversation of that in the check-ins channel, right? So… And, and we had a thing, like, a few weeks ago, where… especially Tiffany sent out a message into the comms channel where we said, like, hey.
We are currently out of capacity for blog posts.
And my feeling is this will go on for a while, right? We are right now a little bit… Low in bandwidth, especially on the maintainer side.
And also after feeling that, like, right now.
So there's things how OpenTelemetry is now… perceived in the world, and then how things are going, I think we can approach the block slightly different, right?
And the things I wanted to quickly chat about and propose is that, like.
If you go into the… right now, like, the requirements for a blog post, there are two things I'd like to change.
The one thing is that I think, like, until recently, the… sponsorship by a SIG slash maintainers.
was… Optional.
And we said, like, hey, and by the way, we help you to find someone, and I want to flip this around entirely and say, like, hey, if you want to publish a blog post, you must have a sponsor, And you must… yourself go to a Sikh.
That might find this blog post relevant.
And, tag them then accordingly, and say, like, hey, this and that person from this and that SIG said they're going to sponsor this blog post, and sponsoring also means, like, they will provide the first step of reviews on it, right?
And the second thing is, like.
A lot of the blog posts that we get is, and especially those that make a lot of work, are the ones that are hands-on and tutorials.
And while on the one hand I like them, and I like writing them myself, the big problem is, like, they, as I said, take a lot of effort.
they take away attention from docs, because some of them should be docs, right? And the other thing is, like, they're very… temporary, right? So someone writes them, we put them on the blog, and a year later, like, I said they're outdated, or nobody cares about them anymore, so the… the time and effort, or the effort to outcome relationship is broken, I think, for those blog posts. I don't think we should, let's say, not allow them forever again, but… but right now, maybe still, like, hey, this is something we are not able to… to handle right now, so… so we will focus on project updates and things related to… to the work of Specific SIGs, but we're not… no longer open to… to accept any any… any blog posts that are more like, hey, here's how you do X, Y, and Z with OpenTelemetry, right?
So yeah, I'm curious what people think. I also think there's a lot of drawbacks of doing that, but yeah, I just wanted to talk this through.
**Marylia Gutierrez** 16:38 I think there might be, like, some… Pushback from people if we just, like, say, okay, we're not doing, like, the… that type of blog post, but… I guess if we make the requirements of getting, like, a sponsor, like, case required, actually, like, mandatory. And if you have somebody from ASIC that is willing to, like, review.
The, like, this type of a blog, and then just, like, a copy edit from our side.
maybe we can try, like, kind of, like, do by phases, for example. We do this as required, and see if that improves anything. If it still doesn't improve, we might, like, limit the type of blog post, so it's not, like, a one-time, like.
basically, like, limitation of a lot of things at once. I don't know, maybe it's an option.
**Severin Neumann** 17:36 I mean, it makes sense to me, right? I mean, at the end, the goal is to, like.
take away some load from the maintainers, like, from the docs maintainers. And actually, we… we want… to have most of our blog posts coming from SIGS themselves, right? Which, like, has no issues with sponsorship, right?
whatever language SIG or CollectorSig says, like, hey, we want to put a blog post out.
I don't know, we changed some mechanics in the collector, and sure, we are documenting that, but here's also, like, a tutorial how to make right, or something like that. And it's still a hands-on blog post, right? So, yeah, that makes sense, so that we focus maybe on the… on the, on the… on the first part.
Did we make it a little bit more… more restrictive, and then if things are not changing… I think the moratorium on, like, those kinds of blog posts… this was a little bit more because, as I said, like, we… we're a little bit slow, and… Low on, on, on, on maintainer, capacities right now, but if this is changing things already, then yeah, I mean, I'm totally fine with just doing that first thing.
**Vitor Vasconcellos** 18:55 I was just looking at the document, because I remember we discussed it, and it was back in October.
Having a second blog for contributor posts.
And… Not now, but maybe… Some months in the future, we could… Like, prepare some… some kind of… Of changes, and having a separate blog.
For those kind of polls, and for now, just… Just… just make those… those changes and have stricter rules for…
**Severin Neumann** 19:43 Yeah, I think that the advantage of what I propose here, it's very low effort on our end, right? I mean, we just changed the contribution guidelines. And the other one, I'm with you, like, there's ways how to, let's say, address this even structurally. I mean, we… a few years ago, we even had, like, an open discussion, and I think it's still open, around, like, hey, do we want to have a tutorial section, and a section which is a little bit more like keeping those hands-on things, more… more long-lived, right? That if someone says, like, hey, here's how you, I don't know, do X, Y, and Z with the collector.
That… that we could… that we could host that specifically, but… but that also means, like, someone would need to… to run and maintain that, and I think that's why… why this… this never got traction, but… Yeah, so I think what I hear right now is, like, let's… let's make… let's flip on the sponsorship, and then see how things improve from there.
**Marylia Gutierrez** 20:47 And we can also tell people, like, oh, if you really want to, like, show, like, how to use this, like, a good scenario, we can basically point them to blueprints, like.
Oh, we have this project that is about, like, how you choose, and this is another way to get more contributors on that project as well.
**Severin Neumann** 21:03 Yeah, that's a good call-out. Blueprints is actually a good example for that, yeah.
Cool.
I still face the challenge that, like, I have to figure out my CLA myself right now, so I hope that I can create a pull request maybe next week or something like that, but if not, I mean, if anybody else is open to revert.
our contribution guidelines and OpenDPR, please help me with that. I said, I still have to sort a few things out.
**Marylia Gutierrez** 21:40 I can take this one, too.
**Severin Neumann** 21:42 Yeah, that would be great, thank you.
**Marylia Gutierrez** 21:44 Yeah, I see the amount of, like, closed PR and, like, open PR.
**Severin Neumann** 21:48 protestable.
**Marylia Gutierrez** 21:49 I just keep getting notification. Open code.
**Severin Neumann** 21:53 Actually, actually, this PR, like.
like, like, right now, ECCLA is saying, like, oh, you're fine, just go on contributing, but actually I want it to turn red, so that way I can, let's say.
kick off the whole… the whole process again. Just give me a second.
**Vitor Vasconcellos** 22:10 But… if you… oh, sorry, yeah.
I was going… just going to mention that I went… I had to go back to my first PR, my very first PR, and click on the same link. I clicked it, like, 2 years ago to kick off the process all over again.
**Severin Neumann** 22:29 Yeah.
Sorry, I was just distracted for a minute.
Can you repeat?
**Vitor Vasconcellos** 22:36 Yeah, when I… the last time I had to change my CLA and sign… sign everything once again, I… I went back to my very first PR and clicked on that link.
And I managed to… to start the process all over again. I'm not sure if this…
**Severin Neumann** 22:57 Yeah, no, the thing is, like, We need to go through the whole process as a company to sign the CLI, which is…
**Vitor Vasconcellos** 23:06 Oh, okay.
**Severin Neumann** 23:07 And I'm probably the person that will lead that, so I have some experience with that already, but it's just some… some work that needs to be done, so… and I appreciate it, or apprehend already that, like, this takes some time to… to get this over the finish line from Linux Foundation's side and our side and everything, so yeah.
Anyways…
**Vitor Vasconcellos** 23:29 Perfect.
**Marylia Gutierrez** 23:33 Yeah, because from… next item, I can take over the updates, and yeah. I guess next item on the agenda, Diana?
**Diana Todea** 23:43 Yeah, no, it's just, I saw the backlog, and so I started, like, chipping in and reviewing a few PRs, like, PRs, obviously in sync with the sponsor's PR reviews, but yeah, some of them still the maintainer's approval. I saw that some of them got approved, but still there are a couple of them that still need somebody to… properly schedule them and, everything like that. Should I still keep doing that, or… Hmm.
**Severin Neumann** 24:16 Yeah, please, and can you… can you send us the, maybe, reminders about which… which PRs you reviewed, so maybe drop in the comms channel. Perfect. I saw, I think I looked into them last week, and then…
**Diana Todea** 24:29 Yup.
**Severin Neumann** 24:30 There was something that distracted me, so I'm not sure if Vitor can help with that, or anybody else from… From maintainers, so… but yeah, just…
**Diana Todea** 24:38 Sure.
**Severin Neumann** 24:39 Send us the links again, and we can take a look.
**Diana Todea** 24:42 No problem, thank you.
**Marylia Gutierrez** 24:49 Yes, any other topics from anyone?
Yeah, so for the… in two weeks, that would be the time that we will go over the dashboard and assign stuff to people, so yeah.
**Severin Neumann** 25:13 I'm really, like, we tried to establish a triage process a few times, and then hopefully this is really going to help with that.
And I'm also, hopefully, a little bit more back on track with everything, so filling the, again, agenda a little bit more. So, yeah, thank you, everybody.
**Diana Todea** 25:30 So, yeah, I just got another question, sorry, because you reminded me, Severin, about the docs, Localization.
**Severin Neumann** 25:40 Yeah.
**Diana Todea** 25:40 So, I don't know, if you wanted some help, or I don't know, you said there's some, like, updates coming, or you wanted to do some updates, but anyway.
**Severin Neumann** 25:50 No, no, okay, I think I know what you're referring to.
**Diana Todea** 25:55 Is that it?
**Severin Neumann** 25:56 I was, like, I still need to review the answers that all the localization approvers gave me on my… on my… on my questions, and I just need to review the ad and see, like, hey, what kind of actions should we as maintainers take on that?
That's… that's definitely something that's… that's pending, yeah, yeah.
**Diana Todea** 26:16 Okay, no problem, perfect, yep.
**Severin Neumann** 26:17 Yeah, thank you.
**Diana Todea** 26:18 Fair.
**Marylia Gutierrez** 26:34 Looks like… No more topics, and you can have 35 minutes back.
**Severin Neumann** 26:41 Amazing. Yeah. Thank you, everybody.
**Diana Todea** 26:44 Thank you, bye bye.
**Vitor Vasconcellos** 26:46 Thank you, sir.
