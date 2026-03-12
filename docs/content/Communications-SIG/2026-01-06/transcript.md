SIG: Communications SIG
Date: 2026-01-06
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Vitor Vasconcellos** 01:46 Hello? Hello?
**Patrice CNCF** 01:51 Hello! Happy New Year!
**Vitor Vasconcellos** 01:54 Javier. Hey, Patrice. Hey, Tiffany.
**Tiffany Hrabusa** 02:04 It's been a meeting marathon this morning.
I'm jumping from one thing to the next.
**Patrice CNCF** 02:14 Same, same.
Seems like we might have a quieter meeting today as compared to the last two.
**Tiffany Hrabusa** 02:27 Yeah, oof.
if you all don't have anything pressing, I can just launch into my question. Maybe we can cut out early then.
So, phase one of the collector docs refactoring is almost done. There's a few PRs that are still outstanding, but they're… they're pretty close to done.
I took over.
all of those PRs and just finished them myself, I don't like doing that, but with the collector issues, like, we're on a timeline here, like, we need to make progress on this for hotel graduation, so I can't, you know, just kind of let things sit.
Hi, Leandro. So… I'm about ready to embark on Phase 2, which is, Phase 1 was kind of the warm-up. It was… Working with pages that don't necessarily need new content to make sense, like, if we restructure them or copy-edit them, they're mostly already, complete.
Phase 2 is going to be much more in-depth. It's still gonna be, re-architecting pages and copy editing.
But there are going to be new pages added, lots of new content included, and I'm going to work… have to work with the collector, SIG on getting that new content in, and I plan to meet with them tomorrow.
My question is, I learned from the Phase 1 process that if I create a slew of issues at the start of the phase, then I get a slew of PRs immediately. And that is… it's not ideal for me from a review perspective. So… Do any of you have suggestions about, like.
Can I… should I create issues and just assign all of them to myself until I'm ready for them to be kind of implemented, and then open them up to the community? Should I just not create the issues until I'm ready to have the work done?
what do you recommend? Like, I should say, from my own planning perspective, I would love to just create all of the issues now, so I can see the landscape of Phase 2 in its entirety, but I'm afraid. I'm really afraid if I do that, that I'm gonna end up with, like.
40 PRs, like, within a matter of days, and then I'm gonna be… you know, conflicts, like, merge conflicts come up because things… it just spirals. So, anyway, opening it up to you all.
**Patrice CNCF** 05:36 I think you have, Clarified what your preference is, and proposed a solution that makes sense to me within that context, is open all issues so that you can have the full landscape.
And, yes, if things are unassigned, then they get picked up. So assigning them to yourself, and even marking them blocked.
**Tiffany Hrabusa** 06:00 Blocked? Okay.
**Patrice CNCF** 06:02 Whatever makes you feel the most comfortable in… Avoids you wasting time telling people, no, no, have you noticed this is a sign to me?
I think that's a great strategy. It's also good for us because we can see the landscape as well.
So, it's a matter for a… us to agree to the convention that if it… well, we already have it, but if it's assigned to somebody, that we enforce that.
As a comment, if anybody comes up, I don't know if there's a new period of… Mentorships coming up, but we know that we get extra pings, can you assign this to me, type of thing, but…
**Tiffany Hrabusa** 06:44 Okay. Yeah, alright, that's, that's how I think I'll go about it then. So I'm gonna spend some time, this week and next week creating all of the issues, and I will assign them to myself and block them initially, and then, as… as the work needs to be done, I can unassign, I can add the help wanted tags and, like.
open things up, as I'm ready for that to happen.
Okay.
I think he…
**Patrice CNCF** 07:12 You usually… you usually have a meta tag, a meta issue for that, so maybe you can have a separate comment in that meta issue that explains just in a couple lines, what you're saying now, which is you've laid out all issues, but you're blocking them until you're ready to work on them. And that way you can cross, or any of us can cross-reference that particular comment.
If, if, people not cognizant of our process comment on an issue that's not available.
**Tiffany Hrabusa** 07:43 Okay, that's a good.
**Patrice CNCF** 07:44 How does that sound?
**Tiffany Hrabusa** 07:45 Yeah, that sounds good. I will do that. Thank you.
**Vitor Vasconcellos** 07:54 Yes, I just added another item. It's the workflow, the AI-generated content detection workflow.
I have some concerns regarding the security, if we are using the pull request started correctly in the workflow.
And there's, Here, that is still pending.
I think the most important part is we need the organization-level token to access the Copilot features. We can't just… there's no GitHub action for Copilot or anything else. We… we can use the… Copilot CLI, I think.
But we… still need that token, and I think I have an issue in the… it's in the community repo.
Just let me grab this link and add it to the document, but… Yes, here it is. From… from everything I could test, personal repos, it works… Okay, it sounds good, and this most likely it will help us in the future when… We start receiving this… these tons of PRs that people just grab some random issues and contribute, just like happened to the collector.
Yes, there it is, the… But I think this is something, if we… we can get that token, I think this is something we can… Start using in the next days.
**Tiffany Hrabusa** 10:02 I'm… I'm all.
So…
**Patrice CNCF** 10:06 I have a question about usability. I… And maybe a question about whether anything has changed in the past 4 or 5 weeks, since I've been away.
when I looked at the, I think this is based on what is… or was used in Hugo, is that correct?
Or inspired from it.
Okay.
**Vitor Vasconcellos** 10:33 Actually, it's not the same action, it was inspired because we need to use the Copilot CLI, and in Yugo, it's, A single GitHub action, yeah, it's not the same action.
**Patrice CNCF** 10:48 Got it.
I guess my question, as I looked at how that… I think, Hugo feature was working. It seemed quite verbose, and I… Wasn't sure how much value we got out of it.
we would get out of it. I'm certainly willing to see this enabled and give it a try in our repo. I think, in the end.
the, we're using AI to help us gate a kind of a go-no-go, we accept this, we don't. Is that where we're… we're heading?
Or is it more to be informative towards the community so that, essentially, we're going to be redirecting them to our AI policy, which is It's fine to submit stuff.
If you're using AI as assistance, but you're in the driver's seat as a human.
does that sound right as a… goal?
high-level goal.
**Tiffany Hrabusa** 12:03 For me, I struggle with… pushing back on people. Like, I feel bad doing that. I don't want to discourage contributors who would… Potentially stick around in the community.
So… it would be helpful to have something concrete that I can point to, like, if they don't check the AI box on the PR.
And then this tool says, yeah, but 80% of this was created with AI, and it's… It's… slop, or bordering on slop.
then I don't have to feel bad about saying.
here's our AI policy. This PR was… evidently used creating AI, and it doesn't… solve all of the problems that need to be addressed, so please Take another look, and this time use, your own judgment and tools and skills in addition to AI.
I feel… maybe that's just a me problem. That I… I feel bad saying that without something backing me up. Like, it was pretty obvious that a lot of the PRs that we got with the phase one of the collector refactoring were AI-generated.
But I still didn't have proof of that, and so saying that to someone… I don't know. That's, for me, high level, that's what I would like to see it for.
**Patrice CNCF** 13:33 Okay.
I agree, and I think as, approvers and maintainers, I share that struggle as well.
We want to be as welcoming as we can in the community, but also be able to filter out. Okay.
Regarding that fine-grain token, have you been in touch with Has anybody gotten back to you? I see there's nothing on the issue, but…
**Vitor Vasconcellos** 14:02 Yes. Do you see it.
**Patrice CNCF** 14:03 Any roadblocks?
**Vitor Vasconcellos** 14:04 Shop.
**Patrice CNCF** 14:05 And… and what is it that… Is in the fine-grain access that we don't have now.
**Vitor Vasconcellos** 14:15 I think this is something that must be configured through the hotel bot app, I'm not sure. I had this issue initially in the admin repo, and… they asked me to… to move it to the community repo, so… but I'm not sure what needs to be set up to have it.
**Patrice CNCF** 14:35 Okay. Well, I'm seeing that there seems to be, like, an option for co-pilot requests that needs to be specifically turned on, is that it?
**Vitor Vasconcellos** 14:44 For our co-pilot interactions?
**Patrice CNCF** 14:48 It…
**Vitor Vasconcellos** 14:49 Huh?
I'm not sure…
**Patrice CNCF** 14:54 Okay. No worries.
**Vitor Vasconcellos** 14:57 Yeah, yeah, I can confirm that.
I'm not sure.
Oh, yeah, yeah, yeah, it's the… that setting is to… to access the… so we can connect on the CLI using that… that token, that's basically for…
**Patrice CNCF** 15:18 Okay.
**Vitor Vasconcellos** 15:19 Right, yeah.
**Patrice CNCF** 15:20 To me, that kind of explains why we need that extra option in the… fine-grain access as compared to what we have already. Sometimes what I do is I ping, Trask?
on… such shoes, although if… He was involved in the admin… if you say this was in the admin repo before… Maybe you don't need to, but if not, You can just tag him.
**Vitor Vasconcellos** 15:52 Yeah, I think it was stress that replied to the issue initially.
**Patrice CNCF** 15:58 Got it.
**Vitor Vasconcellos** 16:01 Yes, that it was stress, that's right.
And… We also have some settings we can decide in the future if we want to fail the workflow on detection, if we… We want to add some labels, or… add some comments, or even if we just wanted to leave it as an Easter egg and dry run, and if we are… looking into seeing the results, we can just go to the actions, the workflow history, and see the output. It's… we can… Configured, all of that, so…
**Patrice CNCF** 16:47 Could… eventually adding labels is probably something we'll want to do.
Soon, but, just testing it out.
With training wheels, still on its training wheels, makes sense, initially.
Good.
I'm just back, haven't caught up on issues. Tiffany, I did see your comment when you're back, can you take a look? I haven't yet. This is my first hotel, activities.
**Tiffany Hrabusa** 17:24 I do have one other, just kind of an announcement. So, I… Arthur Silva Senz, who is a maintainer with Prometheus, and, Victoria Enduca, who has been active in both Prometheus and OpenTelemetry. Actually, I think Arthur's in the collector's sake and OpenTelemetry as well.
And myself are going to serve as mentors for an LFX mentorship.
For documentation in this upcoming cohort.
The idea is to improve the, interoperability documentation between Prometheus and OpenTelemetry.
I think primarily the issue and the work will be done in Prometheus, but there may be some corresponding work that's done in the OpenTelemetry docs to kind of bridge the gap between the two.
Victoria was actually a mentee last year, and she conducted, a user research study.
To identify, the mental models that Prometheus users have about hotel resource attributes and the labeling.
And so it was… it was identified that there's… that there are actually ways to map the two, but people don't know about it because it's not well documented.
So, you may see, Arthur, Victoria, me, or our mentee pop in, In the next… 4 months or so.
Just an update.
**Patrice CNCF** 19:05 Well, first of all, thank you very much for doing that. I think that's awesome. Could… would it make sense to open an issue over hotel to just kind of… Kind of as a placeholder landing… issue to say that there may be such activity, and to give a link to the LFX proposal, so we can get the broader context, because this is pan… it spans both projects, and so to somehow be able to cross-reference and get to the whole Scope of the work.
**Tiffany Hrabusa** 19:45 Absolutely. Yeah, we, we haven't actually… so the, the project submission and, like, creating the application, or job description, this is the first time I've done it, so… is happening this week. So, Arthur and Victoria and I are still working on that. We haven't even created the upstream issue in Prometheus yet, so… Once all of that happens, I can absolutely create an epic in OTEL that we can just kind of… Use to track what's going on there.
**Patrice CNCF** 20:15 Sorry, I wasn't sure about what the dates were. I thought it was all settled and done, and you had your mentee, and…
**Tiffany Hrabusa** 20:21 Oh, no, not yet. In fact, we haven't even settled on the exact scope of the mentorship yet, so yeah.
the, application opens, I think, at the end of January, and the selection happens mid-February.
And so I think the official start date is beginning of March.
**Patrice CNCF** 20:43 So this is term 2.
**Tiffany Hrabusa** 20:46 I'm sorry.
**Patrice CNCF** 20:47 term. Which term is it? LFX has four terms, I believe.
**Tiffany Hrabusa** 20:52 It's the first one of the year, I think.
**Patrice CNCF** 20:55 Okay.
**Tiffany Hrabusa** 20:56 But it goes from March, April, May, I think is the actual mentorship, so it's…
**Patrice CNCF** 21:03 Maybe we have 3. Okay, if it's the first one.
**Tiffany Hrabusa** 21:07 Yeah.
So… Arthur is an expert mentor. He's done a lot of LFX mentorship, so I'm gonna lean on him a bit to figure out how it all works. And then Victoria has gone through it as a mentee, so we actually have, I think a really solid team, and hopefully we'll get a good mentee for this.
**Patrice CNCF** 21:27 Yeah, that sounds great. Well, if it's not up and open yet, then probably hold off creating an issue in a hotel until it's finalized. Otherwise, you'll probably get a, please pick me, please pick me type of comment on the issue.
**Tiffany Hrabusa** 21:44 Yep.
**Patrice CNCF** 21:45 But I would… if you just want to drop me a link to your proposal whenever it's ready, I'd be glad to take a peek. But if you've got an LFX expert already, that's awesome.
**Tiffany Hrabusa** 21:58 I mean, I don't know if I would call him an expert, but he's done it, I think, at least.
**Patrice CNCF** 22:01 Seriously.
**Tiffany Hrabusa** 22:02 he mentorships. So, yeah, he's… he's… he knows, I think, what to look for, because I think he's… he's had the experience where he's picked a mentee, and they just kind of disappeared.
But then Victoria was phenomenal, like, she did an amazing job, and she stuck around in both communities, to help out, so… yeah.
I'm hopeful. Great.
**Patrice CNCF** 22:28 Great.
Anything else on the hotel side, in terms of, as I mentioned, I'm probably going to be clearing my notification cache and starting afresh.
Based on Philip's wisdom.
**Vitor Vasconcellos** 22:42 Yay!
**Patrice CNCF** 22:42 Which I used to not do, but now it's like…
**Vitor Vasconcellos** 22:46 How about the, I'm doing the thing when I'm back at work. Okay.
**Patrice CNCF** 22:51 Cool. How about the, specification integrations? Have those gone smoothly?
Have you maybe not had the need?
**Vitor Vasconcellos** 23:02 I just added another item to the document. We have, Google Document… I think two documents, actually, that were set to private, and those documents are linked in the specs. I raised an issue to them, but didn't have any answers so far.
I'm currently setting the… manually… manually setting this… The ref caching results to… To pass the workflow, and… avoid failing, but those are two documents related to logs, I think.
And…
**Patrice CNCF** 23:43 how, if you can help me understand the timeline.
did the…
**Vitor Vasconcellos** 23:50 Oh, sorry.
**Patrice CNCF** 23:50 original PR get merged if the link was failing, or did they change the access to the document after, type of thing?
**Vitor Vasconcellos** 23:59 I think… I think they changed the access after. It's, it's, A page that… a document that was less updated on… It's been a while since it was less updated.
At least a month, or… Or more, and…
**Patrice CNCF** 24:31 Got it. That makes sense. And it happens, and since you've been active in, updating the ref cache, you're kind of getting a feeling for what sort of… how… Links can go stale, and… This is one of the use cases.
**Vitor Vasconcellos** 24:50 Great. And we… we had a release also, and it was… okay, nothing… no issues on the release from… I think it was a release from the specs, too, not from the semantic conventions.
**Patrice CNCF** 25:06 Okay.
**Vitor Vasconcellos** 25:07 I'm glad to know that went.
**Patrice CNCF** 25:08 smoothly.
**Vitor Vasconcellos** 25:10 Windsor, please.
**Patrice CNCF** 25:14 In terms of the document, that particular link in the Google Doc.
Being private, do we want to keep a link to a private Google Doc, or…
**Vitor Vasconcellos** 25:31 Yes, I'm… I'm not sure if this is an important document. I… I mean, if we… we don't have access… if any… no one has access to that document.
I think we should just remove it, it would be easier.
**Patrice CNCF** 25:52 Okay, so I'll take a look, and I was just wondering if anybody here had an opinion already in terms of what the link was, and whether we should keep it.
If it's become private.
If it does stay private, and we do want to keep the link for whatever reason, it might be better to Create an exception rule.
Then to modify the cache, because otherwise we'll hit it again.
Thanks for bringing that up.
**Tiffany Hrabusa** 26:24 One quick question. I didn't pay attention to where the link is showing up in the docs, but is there at least… should we add something? I guess if it's… is it spec?
So it's auto-generated, but can we indicate that this is a private document so people don't, like, click on it thinking that they're gonna have access to it?
If we do keep it.
**Patrice CNCF** 26:50 be taught?
I don't know what the context is yet, I will take a look. We've had a similar situation in the past, and I remember us deciding to just remove the link and not keep A link to a private document. That's the issue.
**Vitor Vasconcellos** 27:08 Yeah, the title says, Discussion of Severity Field.
From the logs data model, and the other one is… Okay, they are both… There are different documents, but both relates to logs and logs data model, so…
**Patrice CNCF** 27:31 Seeing that… oh, one in the OTEP, okay.
**Vitor Vasconcellos** 27:35 Yes, the old club.
**Patrice CNCF** 27:39 Which we don't publish, so that's not an issue. That shouldn't be an issue for us.
But the data model… Okay, maybe we'll just want… it might be preferable to keep the link in the OTEP.
Because it… those are historical.
But in the live specification, since the discussion is over, and the OTEP, I assume, is approved, or not, whatever, there's a final status on that, we should remove it from the… The spec, but… that would… so that would, imply submitting a PR to the spec.
And maybe referencing the OTEP instead of referencing the Google Doc that is referenced in the OTEP. How does that sound, Vital?
And Tiffany.
**Tiffany Hrabusa** 28:34 I think that's a better user experience, for sure.
I would imagine somebody coming into the dock and wanting to read it, and then clicking on it and finding that it's locked.
If they at least have the context of the OTEP.
**Patrice CNCF** 28:51 Right. They're gonna have the same questions as we do, which is, what's the context? And the context is the OTEP. It seems.
You will need to submit a PR to the spec?
You want me to do that?
You can think about it. Let me know.
**Tiffany Hrabusa** 29:10 Kinda neat.
**Patrice CNCF** 29:12 No, sorry, Vitor.
**Tiffany Hrabusa** 29:14 Wait a sec.
**Patrice CNCF** 29:15 How are you, Tiffany?
**Vitor Vasconcellos** 29:18 No, I can, I can submit. I think you have a lot of things. I can… can do that. That's okay.
**Patrice CNCF** 29:25 Great, thank you.
Anything… Else?
Any fires in the past month or so? Anything that… No, that seemed… kind of quiet, maybe? Or more quiet than… Our busier months.
**Tiffany Hrabusa** 29:54 Good.
Do we want to talk about the year in review blog post? I don't know where we stand on that.
**Patrice CNCF** 30:04 Has that gone out?
**Tiffany Hrabusa** 30:05 It has…
**Vitor Vasconcellos** 30:06 Like, I… I have the draft, but it's not… We… we haven't published yet. I had this read somewhere here, too.
**Patrice CNCF** 30:18 Okay, either.
**Vitor Vasconcellos** 30:19 It's a nice one that I was going to mention was…
**Patrice CNCF** 30:23 Is it a PR or a Google Doc? I remember we were juggling.
**Vitor Vasconcellos** 30:26 Yeah, for Google Doc, I'm… He's still blue.
Right? Here.
That's this one.
I also have some images that we could use. I shared these images somewhere in the Slack. I will add to the document as well.
I'm not sure if this is something that… We could use something like this one.
I'll just add it to our… Notes document.
This is a script that I was working on, also, to… To gather some… some numbers for internal presentation at the company, and… I can also publish this script to… To our repo, and we can use it whenever we… I feel like…
**Patrice CNCF** 31:58 Okay.
Tangential question, I see a notice that this meeting is being transcribed. I remember. Did one of us turn this on? Does this turn on by default?
**Vitor Vasconcellos** 32:13 Anybody know? I think it… I think this is by default.
**Tiffany Hrabusa** 32:18 Yeah, when I joined, it just said the meeting was being recorded.
**Vitor Vasconcellos** 32:22 Same.
**Patrice CNCF** 32:25 And Leandro joined, a little… I'm not saying you triggered anything, I'm just saying I noticed after you joined, I saw that.
Transcription notice come up.
Okay.
Regarding the blog, how… I find that… my experience and why I've participated in year-in-review blogs in the past, they're really fun to look at, but it's not necessarily something readers will spend a lot of time on. So I want us to be judicious in our use of time in putting it out. If we have 80% of the content we want, I would want to push it out sooner than later, and then we can get on with… other… more important things.
I see two things in these blog posts. I'm… maybe I'm a data nerd, I like to see the data, and it's fun, but it's also useful I guess from a managerial point of view, to get an overview and key insights. So if we can get both of those in the document, and it doesn't have to be deep, profound insights, but at least a handful would be nice.
Highlights in terms of what And I think, the, multilingual.
Gross.
is something to mention. The growth in the team, I think, is also… worth highlighting.
**Tiffany Hrabusa** 34:04 Yeah, I agree. We should talk about the growth in the team, and then I noticed, Fabrizio did the December release, and we've reached 1,000 contributors, so that's something else that we can, announce in the blog post as well.
**Patrice CNCF** 34:19 Great.
So, Vitor, are you… are you championing this blog post?
And if not, that's fine, I just want to know who's gonna… Who's gonna lead?
**Tiffany Hrabusa** 34:34 Vitor, if you think that most of your data is already in there, I can flesh things out from, like, the contributor and team perspective, and add the conclusion, and then we can just get it published. But if you have more that you want to add from your… from your scripting and data.
**Vitor Vasconcellos** 34:52 Sure.
**Tiffany Hrabusa** 34:53 If there's anything else you think we can also.
**Vitor Vasconcellos** 34:58 get from the script, and Ed can work on that too.
**Tiffany Hrabusa** 35:04 I mean, I agree with Patrice, I think we should just move forward with what we have, unless there was something specific that you knew that you wanted to add. I'll… I'll just, Add a couple lines about the growth of the team, the growth of the docs community, And then a conclusion, and we'll call… we'll call it a year.
**Patrice CNCF** 35:22 Call it a year, I love that. So, Tiffany, you're taking… leadership for.
**Tiffany Hrabusa** 35:27 I'll take it.
**Patrice CNCF** 35:28 Or the, passing the baton, great.
Another thing that is coming to mind Do we want to talk about upcoming graduation, and how some things have… been worked on in 2025, including the collector docs, or… or not? We wait till 2026.
**Tiffany Hrabusa** 35:47 So I did think about that, We've mentioned the Ecosystem Explorer, which I think is… the most interesting part of the collector docs refactoring right now. The rest of what's been done in 2025 is mostly just copy editing and moving some pages. So, I think, next year sometime, I plan to do a blog post about the refactoring itself and, like, how the process worked, and then we can maybe mention that in 2026's year in review.
**Patrice CNCF** 36:21 Okay, so for 2025, I like to have a bit of a launch pad for the end of it, so maybe this could… How about weaving prose along the following lines, which is… Maybe mention graduation is upcoming, or if we talk about the collector docs to say what you just said now.
what the main work has been done, and I want to look forward, I guess in that sense, to say we're looking forward to graduation in 2026, and more exciting Additions to the collector docs, or something like that, to end on a… An excited note of what is coming, or to let people know what's coming.
**Tiffany Hrabusa** 37:06 No pressure, though, right?
**Patrice CNCF** 37:07 No, no pressure whatsoever.
**Tiffany Hrabusa** 37:11 Okay, no problem, I can do that.
**Patrice CNCF** 37:14 Actually, in that context, given the grant, is… Work on the collector docs, a graduation requirement.
**Tiffany Hrabusa** 37:24 It is. Yeah.
It is.
**Patrice CNCF** 37:29 Probably not. That's what I thought, but I wasn't…
**Tiffany Hrabusa** 37:31 Yeah, probably not to the extent that I'm taking it, but I'm like, if we're gonna do this work, we might as well do it all. Like… The docs… most of those pages haven't been touched in a very long time.
**Patrice CNCF** 37:43 So…
**Tiffany Hrabusa** 37:44 Yeah, the biggest thing they want to see is what the Ecosystem Explorer is doing, the… bringing the component documentation into the official documentation. And there's still lots of work to be done there, but we've started, and that's, that's what I'm most excited about, but yeah.
**Patrice CNCF** 38:04 Great. That sounds like a great thing to mention in the… What's coming in 2026, type of thing.
**Tiffany Hrabusa** 38:11 Okay.
I.
**Patrice CNCF** 38:13 If you agree, I mean, that's…
**Tiffany Hrabusa** 38:16 Oh, I definitely agree. I mean, I think it's… It's… there's… there's a lot still to do. I kind of baby-stepped my way in with Phase 1, but, yeah. I would like to get the bulk of it done.
before KubeCon, but I think that that's, like… Which one?
Yeah.
Eu. But at least, like, Phase 2… That's great. …done by then.
But that's soon, right?
March, yeah.
I mean, phase one, I started in November and mostly finished by the end of December. I think without the holidays, it definitely would have been finished, but .
**Patrice CNCF** 39:03 Okay.
**Tiffany Hrabusa** 39:04 Phase 2 is, reworking pages and adding content. Phase 3 is a gap analysis, so figuring out from what we have there what is missing, what, what is no longer accurate, like, what's out of date, that kind of stuff.
And I'll be using some AI tools and… Slack messages and things like that to kind of… assess that, or to perform that gap analysis. And then stage 4 is… Did we succeed?
did it work? Are the docs better? Which, I have some ideas about that, but that can be post… definitely post-CubeCon, but I'm hoping to get at least Phase 2 done before… Before CookCon, so we'll see. So I… I agree with you, it's a big deal. We need to mention it, at the end as, like, something to look forward to.
**Patrice CNCF** 39:57 Excellent.
And I'll see whether we can get this Cross-posted if we feel that we want to get a bit more visibility.
**Tiffany Hrabusa** 40:07 Okay, I will, we have… Jurassi's post is going up tomorrow.
There's another, post from Lukash that might go up Thursday, but maybe we could get this one up on Friday.
If that sounds…
**Patrice CNCF** 40:24 You mean the year in review by Friday?
**Tiffany Hrabusa** 40:26 Yeah.
**Patrice CNCF** 40:27 Okay, sure. I was thinking next week, but…
**Tiffany Hrabusa** 40:30 I'll aim for Friday, and we'll see where things pan out. It's been… I like that. Other than meetings, it's been relatively quiet on the work side of things, so maybe I'll have time, but no promises.
**Patrice CNCF** 40:42 Okay.
Sounds good.
I like that.
**Tiffany Hrabusa** 40:46 Leandro, did you have anything that you wanted to discuss?
**Leandro Caracciolo** 40:50 I'm a good wrestler.
No, just kidding. So, I'm helping Fabrizio with the landing page. I'm creating some illustration for it.
But I don't have nothing to show now, but I think I'm gonna end it at the end of the week, so soon I can show you something.
**Tiffany Hrabusa** 41:10 That'd be great. Patrice, I don't know if you saw that. Yeah, sorry, just filling Patrice in. One of the projects that Fabricio was working on in December was redesigning the homepage of OpenTelemetry, and… he was basing it, I think, kind of on Kubernetes homepage, and I think there was another, like, template that he was kind of working off of.
But we found that we needed some more images, or, like, Icons, or things like that.
**Patrice CNCF** 41:39 cups.
**Tiffany Hrabusa** 41:40 Yeah, things that, instead of just text, there would be, like, an image, as well. And so, Leandro is a designer, so he's been working, to, create some images for that. If you saw any of the OTEL Unplugged images that have been floating around, Leandro created those, so… Yes.
**Patrice CNCF** 42:00 I think that was talked about in this meeting before I left, so I remember that part.
**Tiffany Hrabusa** 42:05 Okay.
Thanks, I didn't know about the…
**Patrice CNCF** 42:09 To what degree is the homepage being redesigned? Is it just adding more images, or is it an actual redesign in… Will there be mock-ups before that, or…
**Tiffany Hrabusa** 42:20 Yeah, Fabrica sent the structure.
**Leandro Caracciolo** 42:23 And I will work on the illustration for it, and also I will try to improve something that I found is interesting to…
**Patrice CNCF** 42:33 Thanks for the link. Vitor, is that the link to the preview?
**Vitor Vasconcellos** 42:39 Yes.
**Patrice CNCF** 42:40 Okay, thanks.
**Vitor Vasconcellos** 42:40 That's the preview.
**Patrice CNCF** 42:44 Hmm, interesting.
Okay.
**Tiffany Hrabusa** 42:50 So it's… I think it's just, It's lengthening the page, so it kind of falls more in line with some of the other, CNCF project pages that have, kind of, You know, little snippets of text with, like, the capabilities of the… of the tool, so… I… Fabrizio has all the knowledge here. I don't actually know what his methods were, so… but you can see there are some blanks for, Just kind of images, and…
**Patrice CNCF** 43:20 Yes, yes.
Cool.
Thank you.
Anything else?
Any developments in terms of AI tools used internally by the… Any surprises, hopes?
Not, opposite of hopes, despairs. Disappointments.
**Tiffany Hrabusa** 44:03 I mean, I've noticed a lot… I mean, a lot of the PRs that are coming in are, Gen AI-assisted. But, I find that if the… creators willing to at least engage and, like, work back and forth with it, then it's not as problematic as some of the ones that I was seeing earlier in December, where they just kind of, like.
dumped a massive PR and then disappeared.
So, I have not felt… Immense despair recently.
No other updates, as far as I know.
**Patrice CNCF** 44:55 Thank you to the note.
Take care of this.
If there's nothing else… Call it a meeting.
**Tiffany Hrabusa** 45:35 Sounds good to me.
**Patrice CNCF** 45:36 See you online, and on Slack.
**Tiffany Hrabusa** 45:40 Thanks, everybody.
**Leandro Caracciolo** 45:41 Thank you. See you.
Bye-bye.
