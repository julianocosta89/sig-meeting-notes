SIG: Python SIG
Date: 2026-03-26
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/f4RCGsadOO0KaBy_SXTBGrfcuLGSg2vzJt88Hfpcc0yZCtycDU6ifyI3P1pyVJoS._8xolAsV8YcAEYo7
============================================================

## Zoom Recording Transcript

**lechen** 03:00 Hey, everyone.
**Tammy Baylis** 03:04 Hey, ladies and… Hi, everyone.
**Paulo Vital** 03:07 Hello?
**lechen** 03:13 Yeah, so, please make sure to… Add your name to the attendees list, and any topics that you want to talk about today.
I think KubeCon has been going on this week, so a lot of people are out. Aaron's not here, and Ricardo's on vacation.
I will have to be stepping out halfway through, but, yeah.
Perhaps we might have a short meeting, perhaps not, so please feel free to add your topics if you need to.
Also, Tammy, I heard that you've been kind of leading, Like, a triage session of some sort?
**Tammy Baylis** 04:12 Yeah, a little bit. Mainly, it's, we look at the board, which I'll link, and… we talk about interesting things. Usually it's turned out to be, Just identifying how many new PRs have moved to the ready-to-review column.
Got it. Yeah, but I can… I can leave that. I can't really share a screen, though.
**lechen** 04:39 I can share the screen.
**Tammy Baylis** 04:40 Okay, thank you, I'll narrate. Thank you.
**lechen** 04:44 Yeah.
**Tammy Baylis** 05:06 Cool, thank you. So, just quick state of the board, We have had, more stale PRs closed, so generally that's, shrunk numbers in all columns quite a bit, which has been really helpful.
And I've checked, most… most of the notification emails, and I can confirm that all of them are stale, that have been closed, and I've commented on others that could use a quick bump.
No status column. Most of these are just bought PRs, which I'm gonna leave in here, but if we scroll to the bottom, there are… Three more, implement processor metrics. I think that's actually ready for review. I've not… oh, and same for that map critical log level to OTEL fatal.
I haven't looked at that bottle core PR yet, but it's probably also ready for review.
But yeah, this, this is… I think really healthy now, thanks to Mike Goldsmith's actions, were out of the hundreds for… some of the columns, and just into the tens, so… I don't think you see right now.
Thank you for that, yeah.
Yeah, the…
**lechen** 06:29 the PR closing has been amazing, or the issue closing has been amazing, so…
**Tammy Baylis** 06:33 Yeah.
Comment in the chat… yeah, sorry, go on.
**Surya Teja** 06:38 Oh, sorry, that was my comment. Are you trying to, can I go ahead, or…
**Tammy Baylis** 06:43 Yeah, go ahead.
**Surya Teja** 06:45 Yeah, so that PR closing has been quite good. It's helping keep… it's helping in keeping a healthy outlook of what is left and what is there.
I wanted to see if anyone is interested in classifying the PRs or attaching tags to the PRs as co-PRs that touch logger or metrics implementation than as GenAI instrumentation PRs that touch the GenAI folder.
And other instrumentation folders, so that It helps in… Quick… reviews, even if the core reviewer is not available, someone from Gen AI can review PRs related to Gen AI and stuff like that. Will that help in closing the PRs faster?
**Tammy Baylis** 07:40 Yeah, we've been talking about this, the general topic of the Gen AI PR movement, a few times already with when Lyud Mill has been here.
Labeling… labeling might help. There have also been some auto, like, assignees have been assigned. If, say, like, a GenARPR comes in, then some, Identified contributors have been added automatically already for visibility.
a layer on top of that might help. Like, Surya, were you thinking of, like, a separate board, or, additional columns on the existing board, or just, like, PR labels, or just… Another way to slice things.
**Surya Teja** 08:28 I don't want to change the existing one because it's quite good. I was thinking of adding tags to the PRs.
so that… I usually come to the PR pull requests on GitHub.
And I try to filter… I'm not a reviewer, but I try to filter Jennai, I… PRs, and I try to review them.
And provide quick feedback so that people can, move on that one. So, if we have tags like Gen AI and stuff like that.
It's going to help.
reviewing the PR.
**Tammy Baylis** 09:07 Okay.
Yeah, thanks, Leighton. Yeah, go on.
**lechen** 09:10 We definitely have, we definitely have labels for PRs and issues, but there is not a current way to automatically do that, to automate it. I believe this can be easily done, Most likely will detect whether or not there are code changes within the generic, folder, and I think that would be sufficient enough, but yeah, we definitely.
**Surya Teja** 09:34 That's…
**lechen** 09:35 definitely we can do it, especially if, like, it's a hot topic like GenAI right now, and people are primarily interested in You know, implementing instrumentations or semantic conventions, then… I think that'll be helpful.
**Surya Teja** 09:50 Yeah, so… I raised 3 PRs in Gen AI.
all those, were not having good, naming conventions on the PRs, so I was speaking with Ricardo on the side, and he suggested me renaming the PRs, like, feature open feature, Anthropic, feature OpenAI, so that Genaya people can easily pick them and review them, so I changed the naming conventions. Even if… if you cannot do the tags, at least if we can have somewhere in the documentation that Naming convention should be followed to identify what kind of changes they're doing, that also might help us In my opinion.
The intention is just to help reviewers as well as triers to make their life easier.
**lechen** 10:47 Yeah, I'm guessing this is the… one of the examples you're talking about? Yeah.
**Surya Teja** 10:51 Yeah.
**lechen** 10:52 Yeah, definitely. We don't have a… explicit, requirement for naming conventions. Obviously, the more informative, the better. That suggestion totally works.
I think… I believe we did get, kind of, feedback that labels are the primary way that people interact with topics of their interest, especially with issues.
Yeah, naming convention helps, but definitely I feel like, automating the… The tags will be the… at least the lowest hanging fruit we can do, so…
**Surya Teja** 11:32 Yeah.
Yeah, I have been grappling with the issue of how I can make code reviews easier.
I first thought of adding, generic AI code review stuff into the PRs, but that did not go out as planned because, it is generating a lot of junk comments on my side when I was testing it, so I shelved off that plan, because I spoke 2 or 3 meetings ago on this one with Aaron and others.
So, I fell back on this plan.
And do let me know if that helps you guys in reducing the amount of PRs that we are getting.
**lechen** 12:10 Right, right. Do you feel like, you're trying to get visibility on your own personal PRs, or are you trying to kind of improve the process in general?
**Surya Teja** 12:20 improve the process, not just on my PRs.
**lechen** 12:24 Makes sense, makes sense.
Yeah, I think, I think in general, we've always been kind of, Struggling with the amount of… contributions that are made versus the kind of PR reviewers that are available. I guess any kind of ideas that we can get, or any automation, especially automation, because a lot of the things are done manually by the maintainers right now.
**Surya Teja** 12:48 Yeah.
**lechen** 12:49 Like, specifically with tagging. And a lot of these data automations are kind of… very possible, especially with, you know, workflows and GitHub Actions. So, I think those lowest hanging fruits are the easiest. If you have any ideas, feel free to create issues for them and, like, tag the maintainers, or the best way is to just, like, bring it up during the SIG, which is Like, now. If anybody has any ideas, I think that would be the… the most visible way to do it.
**Surya Teja** 13:18 Yeah, my major intention is helping reviewers and maintainers, have a simple way to review PRs.
Rather than being burdened with tons of peers coming into the queue and feeling tired to review code. So, that's the indication behind asking this question.
**lechen** 13:39 Yeah, kevin, really appreciate, you thinking about this kind of stuff.
Ultimately, yeah, it does come down to, obviously, like, community interests and personal interests for certain topics, especially if you're trying to push a certain agenda that's not, like, that's not really getting a lot of visibility. We try our best in, like, kind of outlining best practices in the contributing doc to kind of make it easier for reviewers.
for example, like, splitting your PR up into smaller incremental chunks, you know, following the correct template if you're, like, contributing instrumentations and everything.
Yeah, I can see maybe, like… adding to either contributing or making, like, a PR document or something like that for best practices, but yeah, any other ideas that you might have, always welcome, so…
**Surya Teja** 14:36 Yeah, sure. Thanks.
**lechen** 14:40 Cool.
And as usual, yeah, like, this is the best forum to, switching gears a bit, to, like, push certain PRs.
to get the most visibility and strategically push, like, reviews on things and visibility, this would be the best forum. So, yeah.
Anyways, Cool, yeah, it doesn't really seem like we have many topics today, you know, as expected.
So, if… there's no other kind of PRs or anything, that's being called out. I'll just go through the board and kind of, I think we time box it by, like, 10 minutes or so, and then, we can… If there's no other topics, we'll let everyone go, so… Okay, cool. Yeah, I'll just get started then.
So there's a lot of PRs that are ready for review right now.
This is another one for, implementing SDK metrics. I don't believe… The author's in the chat right now, but Yeah, this is, like, a suite of… contributions that relate to SDK metrics.
I believe… I'm taking a look at it right now, but if anyone else is interested, please feel free to leave your two cents. It's pretty accurate, just follows the spec. I feel like it's a pretty easy review, so… Oh, and if anyone has any comments or things they want to talk about, just feel free to speak up and interrupt me. I'm just gonna… Go through these one by one, though.
Yeah.
Oh, maybe I should go the easy-to-review merge and close first.
Some return time… oh yeah, this is pretty straightforward.
We'll just need… Maybe, like, one more set of eyes on it.
We usually have the policy of, like, needing two reviewers, at least.
From different companies, so… Yep.
Now, interestingly, we are still getting instrumentations from PhotoCore.
Does anybody have any context on this?
We haven't had a contribution for Botocor in a while, so… Very interesting, curious. Oh, just for, also, for everyone's reference, We do have higher standards now for, adding contributions and adding instrumentations in general. This is mostly because we don't want… kind of people contributing instrumentations that, like, are not super popular, or, like, a lot of people have context on them, and then just kind of leaving, and then, you know, it's up to the maintainers and approvers to kind of, like, watch everything. So, I mean, this is probably what I'm going to comment on this PR, but, Yeah, like, contributions like this, we would… we really need, like, community support and, like, context owners to kind of make a little bit of a commitment to kind of, I guess, support these for the near future, for us to consider adding them. Otherwise, we'll probably start deprecating instrumentations that haven't been touched or released in a while.
I believe this is what other language SIGs are doing as well. So, yeah, just for everyone's reference.
**Paulo Vital** 18:44 But by the way, if I may ask something, especially regarding this topic, about new instrumentation. So, Is there any process documented for that, or not?
Because we received it from IBM, we received it from a customer, the request to support, Verk Joyk.
That is what Flasky uses, as a WSGI framework, right?
And, we saw that OpenTelemetry also don't have support for that, but we want to start the implementation and contribute back to the open telemetry.
If possible. So, is this something that, open telemetry community is interesting to have, or not? Is there… is there any guidelines and process To evaluate that?
**lechen** 19:50 Yeah, that's a great question. So, in general, I would advise you to, Whatever, I guess, Functionality you're trying to create, whether if it's existing or not.
Feel free to first create an issue or bring it up here in this SIG, and then we'll… like, most of us will be able to tell you the context of whether we're working on that or if it exists or not.
In the… and specifically in terms of, like, supporting libraries, or adding functionality of, like, a new major version or something of an underlying library, we usually prefer people to the guideline for instrumentations here under Contributing.
there are certain expectations that I covered before, in terms of expectations of contributors to maintain the instrumentations.
**Paulo Vital** 20:38 As well as, you know.
**lechen** 20:39 follow Semantic Adventions, and we have all these links here. Try to extend from bass instrumenter, and yeah, you can go through this checklist yourself. It is pretty comprehensive. It might be, maybe, missing a few details that are more relevant to… the most recent, I guess, like, changes. But we have… we do have general guidelines for what you should follow. It's a pretty kind of standard template, for contribution. But the best way to actually get an idea of, like, whether you're doing the right thing, or if we're even interested is… is starting with an issue first, and then we will… Mostly the maintainers and approvers will kind of respond to it, or anyone else who's interested will respond to it, being like, hey, like, yeah, there's this desire to kind of support This new version, or, like, this new underlying library. So, that's the idea.
**Paulo Vital** 21:34 Okay, perfect. Yeah, thanks.
**lechen** 21:36 Was there specifically something you wanted to talk about?
Or you wanted to just think about it first and, like, maybe make an issue for it?
**Paulo Vital** 21:48 No, we will discuss that better, because we have a specific request from one of our clients.
Right. And then, we can write down an issue and, probably, bring to the SIG meeting, or, we can discuss over the Slack channel.
**lechen** 22:10 Yeah, definitely, yep.
More than welcome, so… Cool.
I'll just keep going right ahead, then.
Yeah, I know a lot of this is just gonna be me talking, so, You know, feel free to… either speak up, or you can just drop off. It's mostly just gonna be triaging right now, so, Entity's prototype.
Yeah, a lot of these… a lot of these old PRs are still up related to, like.
Stabilizing the log API.
I have been away for a bit from this for a while, but man, we really need to kind of close these. This is back in, like.
Oh, it does look like they responded two weeks ago, so… Yeah, I'll probably ask them to rebase, and we'll probably have to revisit this.
Hey, Hector, I see that you're in the call. Did we have… maybe, like, help me out here for timeline's sake, did we ever close on, like, the logging stability work, or is that still ongoing?
**Hector Hernandez** 23:23 It's still ongoing, but people were… I thought we were getting very close.
Maybe…
**lechen** 23:29 Yeah.
**Hector Hernandez** 23:29 This is assigned to it, right?
**lechen** 23:33 Yeah, it is part of the RSD, yes, correct.
Okay, got it. I remember there was part of some releases that'll have, like, breaking changes, and, like, we had some pretty good momentum, right?
Is that still being… kind of pushed in the SIGs, I haven't… I haven't joined in the past, or I haven't looked at logging stuff specifically in the past.
**Hector Hernandez** 23:54 Yeah, the… The ones that… there have been plenty of breaking issues, been, released, but the latest one was to remove the… the logger, instrumentation, right? To… as a separate package.
But that's also released.
**lechen** 24:11 goals.
**Hector Hernandez** 24:11 So, I think it's more like… I haven't seen the board lately, but they should be, like, small issues that need to be fixed now, as far as I can tell.
**lechen** 24:22 Got it, got it. Was that the… Was that when we moved the handler into the instrumentation, or is that just removing the instrumentation itself?
**Hector Hernandez** 24:33 Yeah, sorry, I don't know all the details, but I just have, like, the big overview of it, that was moved, not…
**lechen** 24:42 Okay, sounds good.
Yeah, I'll address these later, so… Maybe another logging one? Let's see… Map Python critical logo to a severity text. Oh, okay. I see.
Okay, yeah, I'll probably add this to the board as well.
Awesome.
I don't know where it is. Anyways, cool, I'll probably do that after.
Yeah, so I think… I guess I'll probably just be going through this… myself, then, should probably just save everyone some time.
Is there any other… oh, Tammy, looks like you had your hand up, so…
**Tammy Baylis** 25:48 Yeah, Xu Ning's added a topic to the board about our embedding PR.
**Shuning Chen** 25:56 So, yeah, I, previously, because of network issue, so I didn't add it successfully, so I just added to, bring it up. I… Got a last comment from Ricardo about the open telemetry instrumentation version.
So, I have reverted to the… Lowest version meeting the requirements, so that should be ready to merge.
**lechen** 26:26 Okay, sounds good. What was the comment specifically about instrumentation version?
**Shuning Chen** 26:33 I shouldn't see that. So, I… I… Use of version 0… 0.660… 61b0.
But, he mentioned, probably your, the previous one already.
It's a requirement, so that one should be enough, so I just reverted to… Yeah, the previous one.
**lechen** 27:02 Okay, yeah, yeah, sounds good. Yeah, as long as, We're including the min version, I think it's fine.
Cool, yeah. I'll take a look at it, and then we'll probably get this in as soon as possible. Thanks.
**Shuning Chen** 27:17 Thank you.
**Keith Decker** 27:18 Yeah, and to… to expand on that, that embedding PR is blocking two other Gen AI.
PRs, so getting this one looked at pretty quick would be… Be nice.
**lechen** 27:30 Yeah, that's good.
Awesome, okay, cool.
Are there any other topics, Before we drop off for this week. It's gonna be a short meeting.
Okay, well, if not, I'm gonna keep going through the board. Feel free to ping me on Slack if you guys need anything.
But other than that, thanks everyone for joining, and we'll see you guys next week.
**Tammy Baylis** 28:02 Thanks, Nathan. Thanks, everyone.
**Paulo Vital** 28:04 Bye.
**Shuning Chen** 28:05 Thank you.
