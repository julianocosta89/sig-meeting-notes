SIG: Semantic Convention SIG
Date: 2026-07-20
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:00 This meeting is being recorded.
**Trask Stalnaker** 00:23 Hey, folks.
**Sven Cowart** 00:25 Hi.
**Christophe Kamphaus** 00:27 Hello?
**Josh Suereth** 00:51 Hey, how we all doing?
Finally got my audio working.
**Sven Cowart** 00:58 Hey, good, how are you?
**Josh Suereth** 01:00 Bye.
Every time we change zoom, it wants to connect to my in-laptop camera when I'm docked.
And my in-laptop audio when I'm docked.
So, apparently we changed Zoom.
Since the last time I joined.
**Trask Stalnaker** 01:14 Change to Zoom…
**Josh Suereth** 01:16 Did we? Is this a different thing?
**Trask Stalnaker** 01:19 No, it's going… we're going to change it right in the next, bill.
**Josh Suereth** 01:26 I see, it must have been I rebooted, and Zoom forgot everything. One of the two. Anyway.
Who wants to lead the meeting today from the SemComp Maintainer folks?
**Trask Stalnaker** 01:48 Not it.
**Josh Suereth** 01:50 Okay.
I can take a crack if no one else wants to.
I don't remember the last time I had led one of these.
**Armin (Dynatrace)** 01:58 You have to motivate people today to put some stuff on the agenda.
**Josh Suereth** 02:03 Yeah.
We do need to do a little bit of triage.
So, I'm gonna copy and paste our, standard topics.
Okay.
We're about 3 minutes in, so why don't we do a little bit of triage, and then we'll… Go from there.
Oh, come on, computer.
And… share… There we go.
Alright, so I think things have mostly been moving pretty well here.
Useful past commands, that looks like that's ready to merge. Needs more approval. Performed excellent corrections.
No, this one seems pretty simple. If folks have a chance to… I didn't have a chance to do SEMConv reviews today, I was in a bunch of other repositories.
**Trask Stalnaker** 03:03 Which one?
**Josh Suereth** 03:05 This, this, oh, sorry. Perform text link corrections.
this one here, it's just, like, changing ID to ID.
CPU to CPU and that sort of thing, so it's just another linter.
And then, the myriad of files that are linted.
**Trask Stalnaker** 03:23 Yes, yes.
**Josh Suereth** 03:24 So it looks huge, but it's not actually super big. I think… If I recall correctly, this one.
There's update table, get rid of you. Yeah, so you can actually see what it changes here.
If you wanted to, like, validate. But these are the… this is… this is the real meat of it, is what we allow and what… what we don't allow from TextLint.
Cool. And then terms that we recognize inside of stuff. It looks pretty configurable.
There are a few rules that are more… fun.
But, yeah. Okay.
Cool.
**Trask Stalnaker** 04:05 testing a, a final co-pilot review on it, and if it comes back clean, I'll scan it and approve it.
**Josh Suereth** 04:16 Interesting.
Can I, can I see… how did you request a co-pilot review?
**Trask Stalnaker** 04:23 The… on the… where the reviewers are, if you scroll up.
**Josh Suereth** 04:28 Yeah.
**Trask Stalnaker** 04:29 So it's not there right now because it's in process, but, like, Ludmila… see Ludmila's review at the top? There's the recycle, the re-request review button.
**Josh Suereth** 04:39 Oh…
**Trask Stalnaker** 04:40 Yeah.
**Josh Suereth** 04:40 Put a pilot one up there, normally? Okay.
**Trask Stalnaker** 04:42 Yeah, yeah, and you just click it.
And since we…
**Armin (Dynatrace)** 04:47 Yeah, it's there if it was there already, but you can also, like, manually, add a review, and then just type Copilot, or it will show up in your auto suggestions as well.
**Josh Suereth** 04:59 Do we…
**Trask Stalnaker** 05:00 Right, but I…
**Josh Suereth** 05:01 Have co-pilot instructions?
**Trask Stalnaker** 05:05 I think we do. Yep.
**Armin (Dynatrace)** 05:07 from the bottom.
**Josh Suereth** 05:09 Oh, sweet!
Okay.
**Armin (Dynatrace)** 05:14 I think Ludmila added them a couple of months ago already.
**Josh Suereth** 05:18 Yeah, I feel like I might have even approved this PR that added them, now that I look at it.
At least Reddit at the time, yeah. Okay.
**Trask Stalnaker** 05:26 and…
**Josh Suereth** 05:26 We have…
**Trask Stalnaker** 05:26 We have automated code, we have it, The setting enabled to auto… co-pilot review all PRs, so it's always going to be there in the reviewers, and what's nice about that is also authors can click the… can re-request co-pilot reviews for themselves, and it doesn't go onto their bill, it goes onto the CNCF's bill.
**Josh Suereth** 05:52 Oh, really? So this is not using my co-pilot, this is using CNCF?
**Trask Stalnaker** 05:56 Yep.
**Josh Suereth** 05:57 Oh, man, so I can look at as much as I want, is what you're saying.
**Trask Stalnaker** 05:59 Yep.
**Josh Suereth** 06:03 That's cool.
**Liudmila Molkova** 06:05 I think, by the way, instructions, I added them so long ago, and they're probably in the wrong spot.
I don't know if they are applied.
And I can take a look and see if it still works with the… Modern AI.
**Josh Suereth** 06:24 I'm not gonna lie, I keep looking for a .agents directory, and then a clod.md with the little at symbols everywhere, because that's what I'm used to seeing everywhere now.
**Liudmila Molkova** 06:35 We should add AgentsMD.
**Josh Suereth** 06:38 Yeah.
**Armin (Dynatrace)** 06:41 Actually, make fun.github slash copilot dash instructions.md is what GitHub has in their docs, and they're usually up to date.
**Josh Suereth** 06:52 Okay, so, but if it's instructions.md.
then I think we might need to update the file name, that's all.
Okay.
Alright, so with these, should we take a look at any of the block things? I don't know… Trask, I don't know, do you… did we want to install your PR dashboard? Because that might make this a little bit easier.
Or is it not built for purpose for this, for us?
**Trask Stalnaker** 07:21 Yeah, we should. Let's, I will… I'll do that, I'm landing a bunch of… PRs to the PR dashboard, today.
**Josh Suereth** 07:33 Yeah.
**Trask Stalnaker** 07:34 And so I will enable after that.
**Josh Suereth** 07:37 I'm just gonna show folks, in case you haven't seen it, We installed it in Weaver, in Proto, it's in Java, it's in a bunch of other places, but you end up with this pull request dashboard, which is a… issue.
And in the issue, it tells you if it's waiting on a reviewer, if it's waiting on the author to respond to comments, and what's in draft. It'll also say, like, ready to merge, and that sort of thing. So this, this is kind of replaced, like, a PR, triage workflow for us. It's actually pretty powerful. I would recommend everyone, like, if we add it, everyone use this, because it'll tell you if we're waiting on you. Like, it infers that based on the comments, the open comments, last review time, that kind of stuff, and it'll tell you, like, who's reviewed it, whether or not they have a green checkmark, all that kind of junk.
**Trask Stalnaker** 08:25 Gosh, if you go into one of those that's waiting on author.
And there's a live… Any of them.
**Josh Suereth** 08:36 Thanks.
**Trask Stalnaker** 08:38 Oh, pick one that has… oh, this one, yeah, sure, go to LIA, scroll down, there's there, this pull request dashboard status.
**Josh Suereth** 08:48 Yeah. I should have mentioned this. Yeah, I saw this today, and this is amazing. I love it.
**Trask Stalnaker** 08:52 showed up, yeah.
**Josh Suereth** 08:53 Yeah.
Right, because I think, the one thing.
**Trask Stalnaker** 08:58 It wasn't always clear to authors what…
**Josh Suereth** 09:00 What was going on?
Yeah, I was… I was doing something in here, and it was interesting, because I was having a back and forth with someone.
And it's basically like we're playing tag, where is it? Yeah, so now it's on me again, right?
Even though it says…
**Trask Stalnaker** 09:18 Oh, yeah.
You're the opposite.
**Josh Suereth** 09:20 Yeah, I'm the author. Even though that says, I'll keep digging. And so, I kind of, like, I started using it to play tag, where I'll just make a comment so that it's on him instead of me.
Anyway, kind of funny.
**Trask Stalnaker** 09:31 Yeah, there were also… there were also a few places where it got things wrong, and there was one proto, oh no, it wasn't that one, it was the SELinux proto.
Yeah, so anyway, yeah, sometimes at the… I'm still making improvements to,
**Josh Suereth** 09:52 It's cool.
This is also awesome, by the way, because it gives you a link to the thread to click on, because when you get PRs that are big and gnarly, it's kind of hard to remember where particular things are.
Right? Anyway, so that's just a demo of that for folks, not necessarily, like, what we should be spending our triage time on, but I will say that, like, that has been phenomenal, the pull request dashboard.
So, thank you for writing that.
**Trask Stalnaker** 10:23 Yay! Awesome.
**Christophe Kamphaus** 10:25 Quick question, how does it work?
**Trask Stalnaker** 10:28 In… I'll give you the link to the, shared workflows.
Have you seen the Shared Workflows repo?
**Christophe Kamphaus** 10:42 Yes.
**Trask Stalnaker** 10:43 Okay, so, here's the doc.
easier than it would take a while to explain it. But go ahead and check out the docs, and if you have questions, let me know.
**Christophe Kamphaus** 11:00 Will do. Thanks.
**Josh Suereth** 11:04 Yeah, it's very cool. The only thing I'll… for the TLDR, in the GitHub directory, under Shared Workflows, there's a JSON file you add yourself.
So that's pretty easy.
Alright.
We're well over our time for triaging. We have a bunch of untriage. I'm just gonna look at the latest things that came in.
So we have a fast one in refactor messaging into V2 spans and span refinements instead of attribute groups. This is related to, the second one here.
the messaging one. This is related to moving to Weaver V2 syntax, right?
**Liudmila Molkova** 11:42 Yeah.
I have them on the agenda. We can…
**Josh Suereth** 11:46 Okay, so we'll discuss it then.
And then this FAST one, do… we do have an active FAST group, so should I move that to waiting for code owners?
**Liudmila Molkova** 11:56 Yeah, let's do this.
**Josh Suereth** 12:01 Cool! Oh, this one looks like it came into… oh, so this is all the V2 stuff you're working on, right, Liudmila?
**Liudmila Molkova** 12:07 Right, yes.
**Josh Suereth** 12:08 Right. And, hotel SDK component shutdown self-observability event. Do we have a self-observability group that I should move this to code owners, or is this still an untraged?
Cause we need to make sure it doesn't get auto-shut.
**Liudmila Molkova** 12:23 I think we have, self-observability co-owners. Let's move it there, but also, I'll add it to the agenda because I want to chat about it a little bit.
**Josh Suereth** 12:35 Okay.
Alright, I'll slide it over, and then add it to the agenda. Awesome. Let's move on to the agenda, since I took a little too long for triage. I ended up taking, like, 10 minutes, so apologies. Let's go to… Sven, you want to talk about the Network SIG proposal?
**Sven Cowart** 12:55 That was on mute, sorry. Yeah, so that is, pushing more changes based on the feedback that's come in.
But it feels like it's in a good state now, so I'm just wondering what the next steps are from here. I still think we're… trying to identify a TC, or get a firm commitment on a TC, and otherwise it's, Should be good to go.
And there…
**Liudmila Molkova** 13:23 Oh, I'm your TC member that I should be able to sponsor it as long as Braydon is… will be there to help with some kind of stuff. I'm just waiting for you to reply to their comments.
**Sven Cowart** 13:37 Oh, I already did them all.
**Liudmila Molkova** 13:39 Oh, awesome, thank you, sorry I didn't notice.
**Sven Cowart** 13:41 No, you're good. So I'll add you there then, and then I think this is good, and I know your main comment was around stability and affiliations. I've added in the notes about stability.
And then the affiliations I've listed here, there was a kind of a question of, like.
Some of us are not maintainers of these SIGs, and, like, for example, I listed myself at Semcom.
I know I'm not a maintainer, but I plan to attend very regularly now that we're doing this SIG, and we need to be in close loops, so I hope that's acceptable as enough of an affiliate.
And the same thing with Rob, he's not an official maintainer, but he's already starting to… bet himself into that SIG with, with the work that we're doing. So hope that's acceptable, and I think the same is true of some of these OBI members down below. Like, I think Mario's a maintainer, but the other two are not.
So, yeah, that was the only question, like, is that okay? I, I… unless somebody here wants to volunteer to regularly participate in the network stage, which I doubt it, because I think you guys are all busy, it's probably better for me to join as a non-member and say I'm affiliated to SemCom, because I regularly attend.
**Liudmila Molkova** 15:02 Oh, yeah, absolutely. I was just… I was asking you to add this, because I was curious where people from which SIGs are participating. Okay. And I think it's a… it's a healthy combination.
**Sven Cowart** 15:16 Okay.
So then, as far as next steps go, what… how does it look from here?
**Liudmila Molkova** 15:26 So I think the next step for me is to come back and review and approve, and then I think GC will need to approve the project first.
Trask is great.
And then, given that, yeah, do you have GC liaison? GC sponsor?
**Sven Cowart** 15:46 Yeah, you can scroll down.
It's, Ted, yeah.
**Trask Stalnaker** 15:53 Cool, so just…
**Liudmila Molkova** 15:53 that.
**Trask Stalnaker** 15:54 Yeah, ping him, kind of bug him to get, GC approvals on it.
**Sven Cowart** 15:59 Got it.
**Josh Suereth** 16:01 Also, one thing that can help speed it up is if you get folks who are going to be participating to approve, to say, like, yes, I've read that, I approve, I'm going to participate, that once there's a ton of check marks, even if they're not the green ones, it accelerates the green one.
**Sven Cowart** 16:17 Got it, yeah, they… a ton… a ton of people already have approved, but… They're… they would likely need to re-review.
Because I push changes, but yeah.
And there are spell check errors, but I don't know… some of the CI things are not related to this change, so just something that seems to be broken.
But there's spellcheck errors in my file, but it's just it not recognizing terms like IP fix and NetFlow and things like that.
**Liudmila Molkova** 16:48 You should be able to add them to the…
**Sven Cowart** 16:51 Oh, okay.
**Liudmila Molkova** 16:51 solution this year.
**Sven Cowart** 16:53 I just pushed before, because I've never seen changes, so you're not gonna see it, but, okay, I'll add them.
**Liudmila Molkova** 17:01 Awesome. What are your thoughts on the stability?
**Sven Cowart** 17:05 what is what?
**Liudmila Molkova** 17:07 Like, I've been asking, on the PR, how do we get to stability? Yeah, I'm curious what your…
**Sven Cowart** 17:16 So what we want to really focus on is, the… the way we're approaching it is we want to focus on, like, an entities-driven approach to defining these attributes, and then In addition to focusing on core ones that could be Utilized across the board. So we're gonna focus on driving towards stability on both sets of those attributes, particularly, like, the core ones need to be stabilized, and that would be things like The source and destination and those… those areas that already exist that are used widely across the board, and then Stabilize the ones that are… Very common across entities that we're gonna, define.
So, it's a little bit… Open-ended right now, because we don't know exactly what those will be, but that's the little…
**Liudmila Molkova** 18:11 Awesome.
Cool.
I'll read through, I'll ping you if I have any questions.
**Sven Cowart** 18:17 Awesome, thank you, Ludmil.
**Liudmila Molkova** 18:19 Thank you.
**Sven Cowart** 18:22 And then… This… I got the next one, too. This came up this morning, about the… someone… Pointed out that the, Josh, you're in the… Hearing.
We get switching tabs.
There we go, thank you. Yeah, these… Network metrics exist in the hardware area.
And… Some of these are the same metrics that people are trying to define in system right now, and that we will be defining in network. And, So the question was, Braydon was under the impression that These are not… there's con… there's uncertainty around how they're being maintained, and if they're actively being maintained.
And… How should we proceed with the work that we're doing?
Would it be best to try to… Deprecate these and… and replace them with the things that we are going to be proposing.
Or… Have them… Continue to exist as this exists, and we'll just focus on what we're doing, and… Go… go that way.
Or they're more like split efforts.
**Josh Suereth** 19:42 I'd say if you're making something that basically is the same semantic, and you decide to use a different namespace, then I would deprecate for the new namespace, if that's what we decide. We have precedence where we've done that in the past.
I actually don't know… where these are used today, I… I think that these might have been around the, like, energy consumption metrics, and these were, like, one of the aspects of that, but I could be wrong.
I… in my head, when I see hardware, I just kind of remember, like, those coming in around the same time, but that could also be me rewriting history in my head. I'd have to go look at the details. But if it's… if it's still in stability development, that does mean that we have not stabilized, and if there's no… Semantic Invention Group behind it, there is no path to stability because no one's actively working on them, right? So, at a minimum, what I would say is when you see that in Semcov, if there's no active group driving it towards stability, and again, you've been mentioning that on your project proposal bunch, right? We want to get these.
**Sven Cowart** 20:49 Yes.
**Josh Suereth** 20:50 stable as quickly as possible. So, we have two options. One is we treat it as de facto stable, and just mark it stable, and assume that what's there is good enough, because it's been used for a long time. Or, if you're doing active work where, like, you're redefining this in a more holistic way.
You can take over the attributes and basically deprecate these for what you provide.
**Sven Cowart** 21:12 Okay.
**Josh Suereth** 21:13 Yeah, but we prefer having active groups and active maintainers.
**Sven Cowart** 21:17 Okay, great, yeah. Yeah, Braydon said there was a specific group prior to Semantic Convention SIGs existing and entities were.
And the… and… This doesn't really… For him, it's, doesn't fit into the new paradigm of the direction that cement conventions are going.
And, so it probably makes sense to… replace these.
**Josh Suereth** 21:46 Cool.
**Sven Cowart** 21:46 Thank you.
**Josh Suereth** 21:48 Alright, let's come back to… Kathie?
Azure Container App Replica Name PR.
**Kathie Huang** 21:59 Yeah, hi, I came to the last, SIM meeting, but my PR is still closed. I addressed all the comments. This is a PR to add Semantic Conventions for Azure Container Apps, for the replica name and revision.
But I just wanted to bump this PR again since, I made some changes, but they're not showing up on the PR because it's closed.
But I responded to all the comments, so it's just a waiting review.
**Josh Suereth** 22:32 Trask, you remember…
**Trask Stalnaker** 22:33 I'm hitting reopen. Yeah, I'm hitting reopen on that.
**Josh Suereth** 22:37 Okay.
**Kathie Huang** 22:38 Okay, appreciate it. Thank you.
**Trask Stalnaker** 22:40 So yes, yes, I… I can help, just, it may be a week or two, but yes, I… I will. You can, also, are you on the CNCF Slack?
**Kathie Huang** 22:54 Yeah.
**Trask Stalnaker** 22:55 Okay, great. Yeah, feel free to DM me there, for anything, or if it doesn't get attention.
**Kathie Huang** 23:04 Gotcha. Okay, sweet, thank you. Appreciate it.
**Trask Stalnaker** 23:06 Yeah.
**Kathie Huang** 23:08 That's all I had.
**Josh Suereth** 23:12 Alright, Ludmila, take it away, V2.
**Liudmila Molkova** 23:15 Yeah, so I've done a bunch of migrations to V2.
For… individual areas for definition only, and to unblock the templates, because these are the things that would not be able to exist in V2.
So this is probably the biggest and the hardest one.
a lot of changes. So, the reason is that we only had attribute groups. We didn't really have spans.
I have a span for… 5 or 6 different spend types.
And… Now, we have… Spans for the 6 different types.
And we have refinements for some of them.
The tricky part is that Originally, since we have all attributes in one attribute group.
And separating them into this different… Span types, was tricky.
It was AI-assisted with a lot of reviews.
So I'm, like, 90% confident in that it did the right thing.
But I'm pretty sure there are some 10% that that's wrong.
Given it's not stable, and given that this group will come back and stabilize, I'm kind of okay with some of this being not 100% right.
But if folks can take a look, I would appreciate it. I'll ping Zhao, because he was part of the core messaging, and he would have probably the most context.
**Josh Suereth** 25:10 Cool.
I was… about how you're dealing with the V2 in, Here, this looks like this is working as desired, though, right?
**Liudmila Molkova** 25:21 Yeah!
**Josh Suereth** 25:23 Cool.
**Liudmila Molkova** 25:24 It's like… I… I don't know how Claude does it.
**Josh Suereth** 25:30 Anytime you depend on something that I considered kind of a hack when I wrote it, I'm happy that it's not broken. That's all I'm saying.
Okay.
**Liudmila Molkova** 25:38 It works perfectly, yeah.
**Josh Suereth** 25:40 Alright, that's good.
Did you want to say something, Trask?
**Trask Stalnaker** 25:44 Oh, only that, I've been looking… working on the Java instrumentation, updating that to the latest messaging Semcon for our 3.0 release.
So this interests me, and I will try to, look at it.
**Liudmila Molkova** 26:05 Oh, cool! And you have a bunch of semantic convention… oh, sorry, migration PRs, right?
**Trask Stalnaker** 26:12 Yeah, I'll just link them in, chat.
**Liudmila Molkova** 26:17 Cool, I will ask, I will check… them against… This new version, and see if we agree on how things separate across different spends.
**Trask Stalnaker** 26:31 Cool.
**Liudmila Molkova** 26:33 Yeah.
The, the fast…
**Josh Suereth** 26:37 Yeah, yeah, the first one made sense. This is… this is the next one, right? So, FAS…
**Liudmila Molkova** 26:42 Yeah, and this is much easier because there was a group of common attributes shared the CRSL server spends.
And it's just a… refactoring it in V2, and moving this group to be part of that… this… that spans.
So there is some MDDV, because the attributes that didn't appear… Unindividual spans now do appear.
There is one tricky… Problem there.
So, in FAS, we define surreal response. The… well, yeah, three. The… just the server, the generic one, one for timer trigger, and one for data source trigger.
And for HTTP, we just say that It confirms with HTTP, or whatever.
And initially, I thought the timer trigger and data source trigger should be refinements of the generic server.
But then I thought that, okay, we will do, refinements for AWS Lambda, Azure Functions, GCP, Cloud Run, and then… they would refine the individual things, like the timer trigger.
And we should not allow her to refine refinements.
So I made them the core things, and maybe server… like, generic server should be not a span, but attribute group, but also you can have a generic thing that's not actually any specific trigger for some corner cases.
So, I'm kinda, what I've done is that they are all top-level spans, and that you can refine them.
And I'm using the Hawk from… YAML that they didn't know about until recently, that allows you to, Avoid duplicating things.
**Josh Suereth** 28:55 Where's… where does this show up with the ampersand thing?
In the file. I would have expected it earlier, right? Or is it at the bottom?
**Liudmila Molkova** 29:03 Yeah, it must be earlier, so if you search for it, you will find it. Oh, line 35.
**Josh Suereth** 29:09 Oh, here, I see. And this is where you name the block and then reuse it, got it.
**Liudmila Molkova** 29:14 Right.
**Josh Suereth** 29:15 Okay.
This is… this is also, if you ever write a YAML parser, this is why it's really a pain in the butt.
**Liudmila Molkova** 29:27 Yeah.
**Josh Suereth** 29:29 Okay.
Interesting.
So… The refinement thing is an interesting discussion. I think what you did is a good compromise, but it does… Make you wonder.
Because the only difference…
**Liudmila Molkova** 29:51 That'll refine.
**Josh Suereth** 29:53 Yeah, between refined… well, this is… this goes into one of the things I think you had mentioned before. So, the difference between a server and a data source server is what? There is something that's locked down?
**Liudmila Molkova** 30:08 Right, the trigger has a specific value.
And actually, there are a bunch of new attributes that are describing the data source.
**Josh Suereth** 30:18 I see, so it's, it's… wait, you called it a discriminator before?
Right? So basically, they're all the same kind of spend, but there's a discriminator.
That leads to certain attributes coming after it.
I wonder if we need a better way to model this in the long run.
You know, it goes into, like, what you guys did with Database, where you have, like, MySQL, you have Postgres, you have, you know, SQL Server, and then there's a refinement for all of those that has a discriminator, and then the extra things.
Can you have a discriminator on a discriminator? You know what I mean?
that might make sense for a subset of things, so, like, a GCP… attribute, having the discriminator that says it's a data source, and having a discriminator that says it's GCP.
I don't know.
**Liudmila Molkova** 31:16 discriminators.
More than.
**Josh Suereth** 31:18 You have for different pieces, though, right?
Yeah, it gets… I, like, it gets weird. Okay, anyway, this seems like a good compromise, I just… this is making me think we need something more first-class for this here.
**Liudmila Molkova** 31:39 For this, yeah, and like… We, we should, we should think about discriminators.
It's just that you will need another, then, a way to say that that this span, not just the refinement, but this span.
is… Another spend.
It's also another spend, so it is a refinement.
**Josh Suereth** 32:01 It is, yeah.
Yeah, I'm just… so, like, this is the thing I think it probably needs a first-class support of… You could reference something as… that happens to be a discriminator, and then we should call out, well, the value Has to be data source, right?
**Liudmila Molkova** 32:17 Yeah.
**Josh Suereth** 32:18 So instead of writing a note that it must be data source, we just know because it's a discriminator with a particular value, we would automatically generate the docs to say this must be data source for this type.
And then we have it in code, so if we did, like, code generation.
For this particular span type, it would be hard-coded as a data a data source.
**Liudmila Molkova** 32:42 Yep.
**Josh Suereth** 32:43 Okay.
Interesting.
Alright, well, this looks good. We have some code review to do here. There's one more, I don't know if you want me to show that, which was message… wait, did we already look at messaging? We already did.
What?
**Liudmila Molkova** 32:59 The hardware.
**Josh Suereth** 33:01 Hardware.
**Liudmila Molkova** 33:01 What's the…
**Josh Suereth** 33:02 Here it is.
**Liudmila Molkova** 33:02 03, yeah.
**Josh Suereth** 33:04 Yeah.
**Liudmila Molkova** 33:05 So, this is probably the easiest of all.
So for hardware, we… similarly to VAS, we had a group of common attributes that was not included on all the metrics in the file, And… We are including this group on all of them, and… There is a special metric, like, CPU state or something.
And a bunch of them, actually, or hardware state, yeah, hardware state, that has a refinement for each of this group. There is a special hardware state for CPU, special hardware state for GPU. They are refinements, it worked perfectly fine.
And… Yeah, this prints.
And now we have… Both of them.
Nicely defined for… Yeah.
This was a refinement.
**Josh Suereth** 34:17 Gotcha.
**Liudmila Molkova** 34:18 So there is a lot of stuff here, but it's mechanical, it follows the same pattern everywhere.
**Josh Suereth** 34:27 Yeah, that's cool.
I guess this gets into that networking question, and this is why, if I recall correctly, these were somewhat related, because I think these were the metrics that were used for, the energy consumption.
And now that I look at this, yeah, I think they all came in around the same time, right?
Talks about fans, CPUs, CPU…
**Liudmila Molkova** 34:52 Yeah.
**Josh Suereth** 34:53 Temperature and voltage, yeah.
Cool.
This is looking good. I… I am liking the V2 syntax, but I'm 100% biased, so I am curious… if you take away the diff, how folks feel like this is readability-wise compared to our existing format. I'm hoping it's more readable, because it literally tells you what the thing is up here, instead of you have group and then type.
And the names line up better, but the, like… I'm happy with how easy this is to read, Ludmila.
So, I don't know how much of that is you, and how much is the syntax that you defined as well, but…
**Liudmila Molkova** 35:39 Yeah. You also define the syntax quite, quite a lot.
**Josh Suereth** 35:44 Anyway.
Cool. Let's, let's move on unless folks have questions.
**Liudmila Molkova** 35:52 I have a question to you, Josh.
**Josh Suereth** 35:54 Okay.
**Liudmila Molkova** 35:55 So there is a change in Makefile.
And to use VQU syntax, I have to remove future.
Maybe if I should… Not. Maybe we should allow to keep future and use video syntax at the same time.
Because it's… it's really annoying, to… For AI to not understand that the future… it's okay to remove future and things will start working.
**Josh Suereth** 36:30 That's absolutely correct.
**Liudmila Molkova** 36:31 Kinda lose the strictness of the checks, just because we have a mixed situation.
**Josh Suereth** 36:38 That's because future is… doesn't allow any warnings, right?
**Liudmila Molkova** 36:43 Yeah, and it comes as a warning. Maybe it should either come as… just an info log, or wording log, but also… I think it's just the info log.
**Josh Suereth** 36:56 It is an infoglog, but I also think it's warning you that V2 isn't stable.
We could just… say that we're gonna mark V2 stable, and then remove the warning completely when you pass V2, because there's no need to warn you anymore.
Future is about compatibility, right? So, like, it's doing its job today. If you use V2, and we were to break the format, it's giving you a warning, but I think we're at the point we're not going to break the format, so we might as well just remove the warning completely, and mark the V2 output as stable.
**Liudmila Molkova** 37:31 Maybe we should mark V2 input as stable first, before we.
**Josh Suereth** 37:36 Oh, butter.
**Liudmila Molkova** 37:36 pushing something.
**Josh Suereth** 37:38 Sure, one of the two, yeah, yeah, agreed.
**Liudmila Molkova** 37:41 Cool, yeah, so let's finish the migration for SemConf.
And after that, we will become more comfortable. I'm almost comfortable with… Definition part.
**Josh Suereth** 37:55 Maybe we add a quick flag that says, ignore V2's future warnings?
It just removes that specific warning, yeah.
Okay.
But yeah, it's working as intended right now, it's just that is awkward as hell.
Cool.
Riger.
**Ruediger Schulze (IBM)** 38:19 Yeah, hey there. Actually, to the discussion of V2, and I have to say, I haven't paid too much attention yet to it, but as we get into the mainframe semantic conventions, and I was looking actually on metric definitions, and we have, I think, also a number of refinements there.
So, from your perspective, is V2 ready to go from a, you know, if we have our federated repository? I understand what you just said about, you know, there's a couple of things that may generate warnings, but… I suppose it's actually ready to go, right?
**Josh Suereth** 38:58 Yeah, the only thing we're anticipating changing, potentially, is publishing, and I think with the latest, like, with the next Weaver release, I actually don't think we're gonna need to make any changes to publishing.
The only thing coming is we're gonna have a non-breaking change to templates, where you will have access to your dependencies in the template. For Semantic Convention Core, it doesn't change anything, but for you, like, you would actually have the ability to actually look through all of the Semantic Conventions you depend on, and your local repository. That is, like, you know.
So you can see them both in Forge. That's the only thing we're looking at adding, and we wanted to make sure we did it in a non-breaking way, so there's still a warning about, you know, things might break on some of these outputs now.
But again, yeah, with the, with the, With the latest PRs that got submitted and some of the things we have, we think we can do all this with non-breaking ways. So, I'm pretty pumped about that.
So, we meet Wednesday. Oh, the V2 definition syntax? I don't think we need to make any breaking changes to that at all. We even plan to add, like, Liudmila has a couple PRs that actually improve our ability to add features without breaking.
So, I think from definition syntax, you're fine. It's the output that we're working on stabilizing next.
But they're both the same flag, is the pro- is the problem.
So…
**Ruediger Schulze (IBM)** 40:30 Okay, good, thank you.
**Josh Suereth** 40:35 Cool. Do you want me to open this one up, or do you want to talk about self-observability with Mom?
**Liudmila Molkova** 40:40 And let's talk about self-observability first, because I think it's more interesting.
You're not sharing, yeah.
So, SIGO is adding the surf observability for shutdown.
And there is an interesting discussion there. It's been a while, so I might forget some details, but they should be documented here. So… as a part of this event, I believe he measures the duration Of the shutdown.
And, if any errors has happened.
And… Justification for this not being a span.
is kind of interesting, and if you scroll down, I don't… oh, sorry, it's part of the, PR description. I don't want… it's in the PR description.
Why not, an event?
So… What is interesting is that the tracing pipeline ess… Something that's shut down first.
And the login pipeline is something that's most reliable, because we can usually have non-autel Logging story that applications do.
And… M… The shutdown being an event, Makes total sense to me.
But it goes against… Our typical guidance of Spence.
For something that has a duration.
And I wanted to check if anybody has concerns with it.
**Josh Suereth** 42:34 I have concerns in general with this feature, which is just, like… We… we can't… getting… getting… Dealing with crashes and getting data off process while the process is actively shutting down.
Hugely problematic.
if the component is being shut down, like, from a safe aspect, cool, but, like, what if that shutdown's caused by an out-of-memory, right? There's a whole bunch of things when you design that system where… You want to make sure, for example, you pre-allocate all your arrays and stuff, and you have something that you can fire data out, where you don't actually need to turn anything on, or, like.
create a network call, for example, because you're shutting down and you don't know if the network is shut down yet or not. So, generally, my thinking was we should come up with an alternative way of exporting data at shutdown or at crash from the SDK. Like, this type of self-observability should have a different way to get off process if possible.
I agree that using a log makes sense, if let's get an event fired out somewhere in the most stable, reliable thing that we have during a crash of, I might already have a, you know, file handle for standard out. I can just dump bytes to it, and the OS will take those bytes and actually get them into the file. I'm not doing anything as a process. That makes sense to me, but I… I… if we're talking about putting this into any OTLP pipeline, I am nervous about that. I think that that is hugely problematic, specifically you know, the… anyway, I think that's problematic. I have a protocol I proposed that I can plug right now, but it's basically because I'm worried about this concept, so there's a JSRED OTLPMAP, GitHub that you can take a look at if you're curious. It's a full working implementation, but basically, it gives the SDK a file that it can dump events onto.
You could have those events be spans. All of the memory is pre-allocated and hot, and so you can actually push to this while you're getting shut down or destroyed, because the memory's owned by the operating system, not you. But it only works, when you actually have a file system and a operating system in the middle that you can do this communication with, so it works in containers, but it would not work in, say, like, a fast deployment, right? So… I need to look at the proposal. I think writing to an event makes sense. I think having something's better than nothing, but I also think we should be more diligent with how we look at, like, shutdown observability, or crash observability. Like, it's almost its own signal type.
**Liudmila Molkova** 45:25 This makes sense. Perhaps.
**Christophe Kamphaus** 45:26 There have been proposals for… Client-side crash events.
**Liudmila Molkova** 45:38 Yeah, for that one.
I think they are even saying that the backend SDK would be needed.
Because it would detect a crash somehow, or the… oh, so the next instance that will… come back on the same device. Well, notice there was a crash and reported at start time.
But that, probably not possible on backends.
I kind of think if we're… had the… event that says, okay, I'm down, and if it's possible to export it.
It's interesting, right? Combining it to a start event.
And you can compare the number of ones versus another is of itself an interesting characteristic.
**Josh Suereth** 46:38 Yeah, I mean, the other thing is, in case you can't get data out.
You could actually do, like, a black box recording, right? Where we just try to get the crash shutdown data written somewhere, and then on next startup, we read it and send it out.
like, that's… that's one of the techniques that, like, client-side can do, for example, if they crash and reboot, is you can try to get the data back after you reboot, in case you're not able to get it down before things shut down. So, you know.
If you, are trying to write how long it takes to shut down. Obviously, this cannot tell you how long it takes to shut down the logger, if you're using the logger to write the log.
But, if I have a separate component.
Right? That is considered the last thing to shut down, and this only writes events about everything else.
then when I start back up, I would say, cool, I have events about the last time I crashed, let me fire them out, that's an option. This is all getting into design, though.
I… I feel like this probably needs a bit more of a, I don't know who… where this is being driven, if there's, like, a SIG around it or something, where there could be OTEPs or, you know, thinking about this holistically, but I'd love… I'd love this not to just be a, here's an event for SemConv, I'd love to have a, here's how we think about dealing with self-observability during shutdown overall.
As a design, that you could read through that whole thing, and then figure out, okay, does this event make sense in that Space, right?
**Liudmila Molkova** 48:08 Yeah. Would you mind leaving a comment?
**Josh Suereth** 48:12 No, no, I would not mind, I will… I will do that.
**Liudmila Molkova** 48:15 Awesome, thank you.
**Josh Suereth** 48:17 Okay.
Cool.
Alright, and then… Anyone have any other thoughts around that?
Okay, let's look at shared templates.
**Liudmila Molkova** 48:38 Yeah, we've talked about it.
sometime ago, the feedback was to… make it more configurable, and I did. Probably not everything is possible until the new weaver comes out.
Like, there is the… Okay, so the tricky part… Was, we want to be able to render registries.
And markdown snippets. But we want to be able for repositories to pick which one they want.
So, there is a branch, if you want to look at the examples, there is a branch, in Semcon Gen AI that, follows the new syntax. It's down below the end-to-end demo.
Here, and maybe you don't want to look at the div, but just open one of the files and then explore the repo.
**Josh Suereth** 49:40 Come on.
**Liudmila Molkova** 49:45 Yeah, so the… this is the same as it used to be, but the registry's, docs registry.
Yeah.
So here we have a red mean that points to all the namespaces, and then things are grouped by namespaces.
And here we have, events, metrics, spans, if entities were there, we would also have entities.
And then we have a list of signals, the table that just lists signals. You can click and go to that specific metric definition or event definition.
And… This is the same table as we're under today, nothing special.
Oh, I should add metric requirement level.
R.
And finally… In the big README file, there is a… Then there is a list of attributes.
Oh, sorry, in the previous one.
Yeah.
Yeah, so there are just a few attributes defined for MCP, but these are all… all attributes that come from MCP namespace.
So, summary post… adding… Both registry for everything and markdown snippets, maybe not the right time.
So you can turn off… a rendering for… Individual registries, you can turn off all of them, you can turn off per signal registries, however you want.
It's done with a new Weaver feature that I think is not released yet.
But once it is, it will start working.
Maybe I should bring it back to draft, because… Yeah, I'm… yeah, because if we… if we have it, I will need to update it again to, Yeah, so these are… there are the configuration options.
Oh, probably I rendered with local weaver, not the… or with the weaver on main. But anyway, so you can turn off these registries independently.
And you provide a bunch of, Links you want to use.
Most of them are… Like, to our naming guidance, or recording errors, and in theory, you can customize them.
But the last two are the most interesting ones. Here, this is where you say.
Who is your upstream? For now, the single upstream?
And then which is the past and the format of your linked to attributes.
And you can customize acronyms as well.
I think through parameters. Oh, I need to remember how, but I believe you should be able to.
**Josh Suereth** 52:53 Yeah.
Cool. Braydon?
**Braydon Kains (Google LLC)** 52:59 I might have missed if you mentioned it earlier, but is… The intention that other federated repos.
would introduce their own Jinja templates like this one does, or will there be, like, a built-in one that we can start from?
**Liudmila Molkova** 53:14 This is the built-in one that I'm proposing for everybody to use and add it to the agenda, because Ruediger brought up mainframes, and I think I don't want everybody who starts with Directed Semconf to invent their Ginger templates.
Unless they really want to, but, like, they should probably all start here.
**Braydon Kains (Google LLC)** 53:37 Okay. So, so I didn't realize we were looking… this is Weaver. Okay, this is not… I thought, for some reason, I thought we were looking at Gen AI Semconf here, and you had to write your own Jinja templates. I was a bit worried about needing to do that when there… we could probably just work with a shared one on our federated SEMCOM that's coming up.
So if there's a shared template, we would definitely use it, I think.
**Josh Suereth** 53:57 For context, this whole repository, if you didn't know it existed, is meant for sharing.
So, like, we've already moved the policies for Semantic conventions into this, so you can actually do all the checks that we do in SemConf, for your distributed repos, and then Ludmila is working on a template that we can use for semantic conventions.
If you want to contribute things for sharing here, this is where… would highly recommend folks do that and, you know, take some time. Like, we… for templates, we'd love to have full code gen. So, like, Java, Go, JavaScript, TypeScript, whatever, like.
added in. But this… this is… Liudmila's PR is the proposal for the thing that we can all share and use.
Cool?
**Liudmila Molkova** 54:54 then I'm looking for reviews.
I'll make a quick chat.
And let me leave a comment that, actually, it all works with released Weaver, or I won't need any changes.
**Josh Suereth** 55:07 We… we should probably cut a… we have a release this week, too, because I think we landed.
**Liudmila Molkova** 55:11 Yeah.
**Josh Suereth** 55:12 we landed enough that we can start stabilizing some things.
You have a Python code gen draft? I'm excited about that.
**Sven Cowart** 55:20 Quick question, Liudmila.
just because it's relevant to what we're doing with Network SIG, Is there a way to… for me to try this out?
You can…
**Liudmila Molkova** 55:33 Like, yes.
**Sven Cowart** 55:34 No? Okay, okay.
**Liudmila Molkova** 55:36 Yep.
Well… I'll send you a link.
**Sven Cowart** 55:44 Okay, sounds good.
I'll figure it out, I just need to know if there was a way to do it before a release is cut or something, that way.
**Liudmila Molkova** 55:54 Yeah, so this is how you would do it. There are a couple of bugs or missing features in Weaver that prevent it from doing it easily, so… If it's the next release, it should all be really trivial, but I'll… I'll… If you look into the Semantic Conventions GenAI, the… my branch, it would show how to run it, but,
**Sven Cowart** 56:20 Okay.
**Liudmila Molkova** 56:21 I'd rather for you to wait for me to send you a link, because there are too many… Rough edges for now.
**Sven Cowart** 56:28 Sounds good.
**Liudmila Molkova** 56:29 Tail Veril is a new weaver.
**Josh Suereth** 56:31 Oh, this is the parameter override thing you added, right?
Or is there something else that I'm missing?
**Liudmila Molkova** 56:38 The parameter override.
**Josh Suereth** 56:43 Like, this piece is what's coming out in the next release, right?
**Liudmila Molkova** 56:48 Oh, no, the parameter override has been there, so what was missing is the one thing in templates, so that you can turn off specific template.
And the other piece…
**Josh Suereth** 57:04 Oh, the wins and ifs, gotcha, yeah.
**Liudmila Molkova** 57:06 Right, and this is the main one. Other… everything else comes through params or Weaver Config?
I think I added acronyms and something else to the river Tomo.
So that you do the syntamil once, and then… Yeah, you get everything, If you search for TOML, there probably should be an example. Yeah, here is the TOML. So you provide acronyms, you can customize text maps.
And, the params are still coming from either command line or yeah, from Comment Line.
But I think we can add them to TOML as well. I just didn't add them because it's not the hard blocker.
**Josh Suereth** 57:53 Okay.
Cool.
Awesome. I look forward to this.
And yeah, we should… we should cut that release of Weaver so we can use this.
Alright, let me just make a note.
set of features, okay?
**Liudmila Molkova** 58:18 Oh, by the way, it's easy to try, because we were on Docker, because we push main, Josh.
And, like, everything, all those new features should work with just the Docker one.
**Josh Suereth** 58:31 So instead of using Weaver colon latest, you would use… or Weaver colon version, use Weaver colon main, and you get all the latest features, so you can… that's so we can debug and try things out before we cut releases across the whole ecosystem.
**Liudmila Molkova** 58:47 Cool, so I'll send a comment to Sven, and thanks a lot. I appreciate reviews.
**Josh Suereth** 58:54 Awesome. We had a packed agenda today after not seeing a lot, so that's… that's great.
We will see y'all next week.
Bye. Have a good week.
**Braydon Kains (Google LLC)** 59:02 Thanks, everyone.
**Christophe Kamphaus** 59:03 steal.
**Armin (Dynatrace)** 59:03 Bye.
