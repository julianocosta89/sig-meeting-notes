SIG: JavaScript SIG
Date: 2026-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trent Mick** 00:56 Hello?
**Marc Pichler (Dynatrace)** 00:57 something.
Okay.
Isn't it… didn't you say it was a holiday for you today, Trent?
**Trent Mick** 01:06 It is, but OTEL's just so exciting, I have to…
**Marc Pichler (Dynatrace)** 01:09 Oof.
**Trent Mick** 01:10 Do it, or with my morning coffee.
Plus, I don't know, I don't wanna… Miss something and arbitrarily make this whole release take a week longer, so…
**Marc Pichler (Dynatrace)** 01:21 It's.
**Trent Mick** 01:22 and.
**Marc Pichler (Dynatrace)** 01:23 I think we might have to take.
Some more time anyway, and it's…
**Trent Mick** 01:28 Oh yeah, for sure we're going to take more time. I don't want to go even more, but yeah, yeah.
**Marc Pichler (Dynatrace)** 01:34 Mostly, okay.
Oh.
**Trent Mick** 01:38 We're not going to release today.
Interesting.
**Marc Pichler (Dynatrace)** 01:41 No.
**Trent Mick** 01:42 Yes.
**Marc Pichler (Dynatrace)** 01:43 The whole 3.0 work was a bit unfortunate because I had a scheduling conflict at work, so I didn't have a lot of… Time to dedicate to Otter, unfortunately.
You've probably noticed that I wasn't around as much as I usually am during these things, so… Just wanted to say I'm sorry about that, it's…
**Trent Mick** 02:05 This is… You don't have to apologize, but yeah, all good.
Good to know.
Is that work thing cleared up now, or you're still working on?
**Marc Pichler (Dynatrace)** 02:15 I'm still working on it. I'm hoping to get it done sometime next week, but… Umm.
**Trent Mick** 02:21 Okay.
**Marc Pichler (Dynatrace)** 02:22 Yep.
**Trent Mick** 02:25 I think we'll see if, whatever, I mean, we'll look at the… What's remaining on the milestones?
We'll see if Jared joins. He's had a bunch of PRs I've been trying to get through. He's… like… a bunch of small PRs working on the last main thing that he had.
**Marc Pichler (Dynatrace)** 02:45 Yeah, I saw some of, some of them are already open as draft.
Oh, oh.
Hopefully have some time tomorrow afternoon to look at those as well.
I guess we can kick it off with the topics for today. I think this is already reserved.
**Pranav Sharma (Google LLC)** 03:09 Yes.
**Marc Pichler (Dynatrace)** 03:10 Yeah.
**Pranav Sharma (Google LLC)** 03:11 Thank you for that.
**Marc Pichler (Dynatrace)** 03:12 Sure.
Alright, then the next thing, something that we already talked about briefly just now.
delaying the SDK 3.0 release to finish up the remaining work.
I… I'm going to comment on the announcement issue and let everybody know that we are delaying that or Sometime, yeah.
Not sure how much time we would actually need, I'm… I've been meaning to, Target October 15th.
That would give us 15 more days to work through that.
Does that sound okay to everybody?
**Trent Mick** 04:10 Yeah, I think so. Having a set target helps.
**Marc Pichler (Dynatrace)** 04:12 Yeah. Then I will… Update the announcement, and I wrote, as opposed to the other Js channel on slack, so that everybody's on the same page.
**Carlos Alberto Cortez (Dash0)** 04:24 Out of curiosity, are you planning to do some logging?
Part of, logging part of this, or not yet?
**Trent Mick** 04:34 So, well, opinions may vary. My hope is for us to do the logs.
GA milestone as part of this.
There are… Right now, I think just mechanics to… Remaining on the open issues and the milestones, so moving… Changing the versioning and setting experimental… whatever, and moving the API logs package into the blessed API package. That PR is being reviewed right now. But then, the open question that I have is I'm… this is my… is my first rodeo for adding stuff to the API package and stabilizing something. I'm not sure what we need for TC approval, or what the… what the rules are there.
I know that you'd spent some time looking, but I don't know.
**Carlos Alberto Cortez (Dash0)** 05:24 Yeah, so you can ask for a review, and this was kind of an informal review from my side.
It's up to the maintainers in case you want to get like second pair of eyes.
But it's up to you, mostly.
**Trent Mick** 05:39 I see. Okay, so there's no hard requirement in the…
**Carlos Alberto Cortez (Dash0)** 05:43 No, I can check. But yeah, as far as I know.
Some SIGs just went ahead, you know?
without this.
**Marc Pichler (Dynatrace)** 05:55 Are there is precedent to six going ahead without the TC review on stabilizing SDKs?
**Carlos Alberto Cortez (Dash0)** 06:03 Yeah, that's what I remember. I don't remember which one. I can double confirm if that's, but that's… I can… yeah, sure. Actually, let's continue with this, and we'll do this Well, as we are having the call, so in 2 or 10 minutes, I should have the full answer.
**Marc Pichler (Dynatrace)** 06:21 Thank you.
**Trent Mick** 06:26 I think I missed the gist. They were saying that there… there is… what is there precedent for?
**Marc Pichler (Dynatrace)** 06:33 It seems like there is, I think Carlos said that he's going to have a look and see.
**Carlos Alberto Cortez (Dash0)** 06:39 I remember that, yeah, yeah, we're saying that, I remember that some SIG went stable with some part of the API without the DC actually doing a review.
So that's the question, like, which SIG did that, and for what component, yeah.
So yeah, I'm checking now the historical records.
**Trent Mick** 07:01 Okay.
So I think, conceivably.
We could have… A pre-release of the API with those things mark stable in the next couple of days, and then, given that we're giving ourselves another two weeks, we could ask for a TC review. If it doesn't come within those two weeks, then we can make a judgment call whether we want to go ahead then or wait.
**Marc Pichler (Dynatrace)** 07:29 That sounds good.
**Carlos Alberto Cortez (Dash0)** 07:31 Okay, I will follow up with historical records, but I just located the docs now, and it says, yeah, it's not a hard requirement. It's like language implementation maintainers may request a TC review prior.
to etc, you know. So it's not a hard requirement. Yeah.
**Trent Mick** 07:46 Can you post the link?
**Carlos Alberto Cortez (Dash0)** 07:47 Yeah, of course. Oh yeah, sorry, I forgot to do it. Yes.
**Trent Mick** 07:51 Thanks.
**Carlos Alberto Cortez (Dash0)** 07:52 Here we are.
**Marc Pichler (Dynatrace)** 08:12 So I guess we can talk about this a little bit more, When we're going to the review three-level milestone and blocks GA milestone issues.
But yeah, in any case, it's good to know that it's not a hard requirement. I think we are With the informal review, we already, are very close to spec compliance there.
So… Yep.
Let's move on to the next one. There's… a request for review on the, OpenAI agents instrumentation.
Looks like Jackson approved this one.
Already, I will have a look at this PR.
To make sure that… Like, everything is… Okay, in terms of structure and… Config and whatnot, to make sure we don't… Release that before, stuff is ready, but, it's probably gonna look good. So, since Jackson already did the review, I… would assume that this would be a fairly quick one.
And this year is the same.
Just needs a maintainer to have a look.
Because it's a new package.
So… Ever.
Do that.
Alright, moving on to the next one.
**Trent Mick** 10:19 On those ones that we discussed, they're generally are fine with These ones being added to auto instrumentations node.
Not sure if we have a position. I don't have a strong opinion either way.
**Marc Pichler (Dynatrace)** 10:31 I'm not sure if… Oh, yeah.
**Surya Teja** 10:37 Thanks.
**Marc Pichler (Dynatrace)** 10:37 you Yes.
We can hear you.
**Surya Teja** 10:40 Can you… Sorry, am I audible?
**Trent Mick** 10:47 Yes, we can hear you.
**Marc Pichler (Dynatrace)** 10:55 Now we might not be able to hear you anymore.
I think there's a message in chat that I have to… Look for the Windows role.
They said I have no idea.
**Trent Mick** 11:12 I'll shoot.
**Marc Pichler (Dynatrace)** 11:13 should Oh.
I guess for auto-instrumentation's note, the question that you just had, Trent.
I would prefer actually it not being in auto instrumentations node immediately and having a release with it.
Out of that.
And then including it later, once we have found that it's stable enough to be included.
I don't assume that there's gonna be any big issue, but I would like to have.
people opt into it first by just manually installing it, and then we see that there's no issues reported for a month or so, we can add it to Auto Instrumentation's node.
**Surya Teja** 12:07 Yeah, hey, can you guys hear me now?
**Marc Pichler (Dynatrace)** 12:09 Yes, we can hear you.
**Surya Teja** 12:12 Cool.
Yeah, sorry, I missed the initial beginning part, so… If anyone can recap, what I missed.
for this PR.
**Marc Pichler (Dynatrace)** 12:23 stay.
**Surya Teja** 12:23 That would be quite helpful.
**Marc Pichler (Dynatrace)** 12:25 Yeah, so the one thing I mentioned was that I am going to have a look at the package structure and make sure we can merge that one. It seems that Jackson had already reviewed the contents of it.
So, I will just give it a quick look.
And see if the package package structure and dependencies and Read me as an order.
And then we should be able to merge that in. Trent had a question about it being included in Altery instrumentation's node, and if we had discussed whether we're okay with that or not.
And I just said that I would generally prefer if we could.
Leave it out of Auto Instrumentation's node for now. Just merge the package.
**Surya Teja** 13:14 Yes.
**Marc Pichler (Dynatrace)** 13:15 So that people can opt into it first, and… Report issues, if they have any, to avoid breaking folks that.
Don't expect telemetry yet, and are using that package so that we kind of have a… Like, a stage rollout of the whole thing.
**Surya Teja** 13:39 Yeah, I agree. So let me quickly rip off auto instrumentation to keep.
The whole thing safe.
That is fine with you guys.
**Marc Pichler (Dynatrace)** 13:49 Yeah, that sounds good. Thank you.
**Surya Teja** 13:52 Yeah, bye.
**Marc Pichler (Dynatrace)** 13:54 And once we have the first release out, I would say, let's just wait for a month or so.
work through any issues, if there are any. If there are none, then we should be fine with adding it to our instrumentations node.
That's my opinion, I'm not sure if anybody else has.
Other ideas about this?
**Surya Teja** 14:18 No, I do agree with you, Mark. That's a good call out because, we just want to see how Things are lining up with users, and then if… There are no issues, we can enable this.
in auto-instrumentation, and then we can take it forward. I agree with you, and I probably would think that one and a half month or two months, not just one month, but I want to give more time, because these are new instrumentations, and the GenAI space is evolving rapidly, so there might be some breaking, underlying SDK changes, so just look everything is good or not, and then I will enable… I'll create issues to enable the auto-instrumentation after 2 months, if that sounds good with you.
**Marc Pichler (Dynatrace)** 15:04 That's good. Yeah.
Trent, I'm not sure if you have… Any additional thoughts on that?
**Trent Mick** 15:13 No, I'm good. I have a chance, I'll take a look, but…
**Marc Pichler (Dynatrace)** 15:16 Okay, not sure. Yeah.
**Surya Teja** 15:20 Thanks, Chris.
**Trent Mick** 15:21 Oh, another one, this… there was the whole… sorry, There was the larger meta issue of the donated.
Instrumentations, Gen AI-related ones for JavaScript, from… open inference? Is that… am I getting that right? Is this related to those ones, or not?
**Surya Teja** 15:44 Yeah, this is related to those ones, Trent.
**Trent Mick** 15:49 Okay, did I miss a link in the description?
**Marc Pichler (Dynatrace)** 15:55 I think there's no link in the description here.
**Trent Mick** 15:58 Can you update the description then and have a link back to that meta issue? It would help.
**Surya Teja** 16:03 Oh yeah, sure. a question, quick question, if I link… That issue with this, 1.
Once if I merge that package, is it going to auto close this issue?
**Trent Mick** 16:18 Don't… don't say closes, or you just say, like.
Just do some prose in a sentence saying, hey, this is related.
**Surya Teja** 16:25 Yeah.
**Trent Mick** 16:27 Just as long as you don't use the, like, fixes colon or closes colon issue, then.
And you won't have that association.
**Surya Teja** 16:35 Yep, cool, got it.
**Marc Pichler (Dynatrace)** 16:45 I mean… And I will have a look at the package structure, get the descriptions updated, and the… Diff on auto instrumentation's node removed, and then, We should be closer to getting these merged.
Brent, you added an issue here.
**Trent Mick** 17:18 Yeah, I wanted… I had a question for you, Mark, on this. This is a request to change the component owner.
at instrumentation.
I wasn't even sure where this checklist came from, but Kuhe, or however you pronounce his handle.
Mmm.
is not a member of the OTEL org.
Because I guess they would have to go through, like, having made contributions and get added as a member. Is that a requirement for us for component owners?
Or will it effectively be a requirement, because we can't assign anything?
To put that kind of…
**Marc Pichler (Dynatrace)** 17:54 Yeah, exactly, that's, so I… added this… Lists of requirements at some point in…
**Trent Mick** 18:05 This is a special.
**Marc Pichler (Dynatrace)** 18:06 Template.
**Trent Mick** 18:07 Template, yeah, gotcha.
**Marc Pichler (Dynatrace)** 18:08 Yeah.
The reason why I added it was exactly what you said, that we cannot assign them anything. Auto-assign won't work from the GitHub action.
And, it's generally a bit more difficult to get a hold of people that are not.
Members of the organization, and we also assign triage permissions to component owners so that they can deal with any issues that come up and labor things accordingly.
**Trent Mick** 18:42 Okay, well, I can reply to them. I think it's not onerous for them to become a member, but I'll… I'll… talk to them on this issue about doing that. There is at least one issue open on this instrumentation. I could just ask them to do a review of it, and that's gonna… basically, quickly, they'll have met the minimum requirements required to become a member, and then they can submit the PR to ask to be a member, and you and I can approve it, and we can go forward. Okay, cool. I'll follow up.
**Marc Pichler (Dynatrace)** 19:11 Good. Yeah. If.
They opened the PR, then, yeah.
Good.
Feel free to also tell them that I would, sponsor them so that they have to folks to get added to the org, and then we should be good.
**Trent Mick** 19:30 Great.
**Marc Pichler (Dynatrace)** 19:31 Thank you.
**Trent Mick** 19:39 The review stuff can maybe move down to other people's.
After other people's things, yeah.
**Marc Pichler (Dynatrace)** 19:47 next one is… Matt, about the support for instrumentation slash development, I haven't gotten around to looking at that, unfortunately.
**Matthew Wear (Dash0)** 20:06 I was just pinging Zach.
**Trent Mick** 20:07 That's on me.
Still, but…
**Matthew Wear (Dash0)** 20:09 Yeah.
You could use another pass whenever anybody has time, but Just wanted to bring that up.
**Trent Mick** 20:17 Yeah, definitely. That's on me. Sorry I haven't been distracted by the… 3.0 release stuff.
There are some merge conflicts, I don't know if those are difficult to deal with, or… it's probably not going to impact me reviewing them, but it means that… Ci won't be running.
Amen.
**Matthew Wear (Dash0)** 20:36 Yeah, I'll… If it's cool, I'll just address those on the next round of feedback, or…
**Trent Mick** 20:41 Yeah, that's fair. Yeah, that's totally fair.
**Matthew Wear (Dash0)** 20:43 I need to address them now again, so…
**Marc Pichler (Dynatrace)** 20:53 Yeah, sorry for us and not getting to this one.
Also somewhat carried away with the other things, but this one is important, and we… I'm hoping to get that in soon.
Right, then I guess we can go to the review of the milestones.
Let's do SDK 3.0 first.
The publishing the 3.0 release is still assigned to me. I will do a pre-release.
Or, like… set up a Pr to do a pre-release for the current state that we have, since we've changed quite a few things. And we'll also include the Api changes with that, so that we can.
test these out.
and then we can do another pre-release. Once we have the logs. Api changes also included there.
some… Okay.
And the next ones, I guess these three are… The remaining work is all the same, right? It's our OpenTelemetry.io updates.
Trent, you're muted.
**Trent Mick** 22:43 Thanks.
I almost said thanks, Mom, for unmuting me anyway, sorry.
I guess I said it. Yeah, OpenSlimJIO, I started PR for that. There was another PR on… there's a… There's a tracing.js, so I guess there's… the browser instrumentation stuff is being set up for the deployment of OpenTelemetry.io, but I'm not sure how to test that. I have to go… I opened a PR, update that, and then was asking… I have to follow up to ask questions on how I can actually test that. That's okay, and then, anyway, whatever. Yes, OpenTelemetry.io is the only thing remaining there.
Doc updates.
A thing that there isn't an issue there, I need to do another pass on the, the migration doc.
That we have for 3.x, and add a few things, like discussing the logs.
Stabilization and the any values.
In addition for complex types of stuff.
But yeah.
Thanks to stocks.
And then the last big one, I think, is Jared's.
work on the browser field, which I haven't really grokked yet, but I've been helping review some of the smaller issues for that.
**Marc Pichler (Dynatrace)** 24:00 Yeah, I also haven't had a look at this one, but I will also try to have a look at that.
I guess one last thing that is also remaining here is… this issue…
**Trent Mick** 24:24 Yeah, that'll be straightforward to do whenever, when we're ready.
**Marc Pichler (Dynatrace)** 24:31 All right. And I guess any one of us can do this one.
on… We are okay with deprecating all versions, right?
I… Was just thinking about, like, what the best course of action would be, and that just, mentioned here that we should probably do it for all of them, because if people npm install, it's not entirely clear if it will be published again if we just deprecate the latest one.
Is everybody okay with that?
Brilliant.
**Trent Mick** 25:15 Yeah, I'm trying to think of the use case of someone who's gonna stick on 2.x, and we're still… For a year, we're gonna do security releases.
Is it a pain in the ass for them to have that deprecated message? I don't know. That's fine. We've been dealing with a thousand deprecated messages for Glob for years, I think we're fine.
Yes.
**Marc Pichler (Dynatrace)** 25:37 I guess we can still undeprecate if it's really annoying to…
**Trent Mick** 25:44 I'm not sure.
Not sure if you can.
**Marc Pichler (Dynatrace)** 25:49 I would double check.
**Trent Mick** 25:50 Makes sense. Yeah.
**Marc Pichler (Dynatrace)** 25:52 Yeah.
**Trent Mick** 25:53 Still, I think it's fine to deprecate. We know, moving forward, that they're deprecated, these ones, so…
**Marc Pichler (Dynatrace)** 25:59 Yeah, and I guess for SDK Trace.
One can migrate within the 2.something range.
**Trent Mick** 26:10 For that one, for all of them except SDK Trace Web.
So I don't know if we want to do a… 2.x release of… both SDK Trace and Web Common, which would be required to get the last pieces so that people can move off SDK Trace Web now.
rather than 3 dot XI don't know how painful that would be.
**Marc Pichler (Dynatrace)** 26:36 I wanted to try out the… release workflow for backports anyway. So this might be a good A good case to trade it.
**Trent Mick** 26:52 Okay, I could…
**Marc Pichler (Dynatrace)** 26:52 I…
**Trent Mick** 26:53 Maybe you and I could work together on that. You know the release mechanics, and I know which PRs need to be backported.
Okay.
**Marc Pichler (Dynatrace)** 26:59 Yeah.
I think we can do that. Let's look into that, Later this week, and then, try that out.
Maybe we'll do the release on Monday, just to avoid any issues over the weekend.
Suggest something, then.
**Trent Mick** 27:23 Christian.
**Marc Pichler (Dynatrace)** 27:25 work for that.
**Trent Mick** 27:27 Okay, sounds good. Yeah, let's do that.
Jamie just showed how to unduplicate.
**Marc Pichler (Dynatrace)** 27:31 Oh, perfect.
So… There are options. If it's too annoying, we can undo the deprecation thing.
**Trent Mick** 27:41 Okay.
**Marc Pichler (Dynatrace)** 27:43 Sounds good. Alright.
I think that's all for… SDK 3.0.
Oh, yeah.
And then we also have the… Logs, API, SDK, GA, Milestone, There we have taking SDK logs out of experimental, integrating the API logs package into the API package.
**Trent Mick** 28:28 Yeah, so Hector has revived his old PR for that, I've been reviewing that, or… We're going rounds on that. Next is on me to do another round of review.
adding to API is not a small deal, so having another… Maintainer, take a look at it, would be… Worthwhile, I think.
Taking out TSPR.
Yeah, so then I added the issue to move over.
STK logs as well. I think that's just mechanics, it's changing the version and moving it to the other directory.
**Marc Pichler (Dynatrace)** 29:02 Exactly.
**Trent Mick** 29:04 Yeah.
Thanks, Carlos.
And then on the the middle one that stands old.
issue I'd had a… can we open that one? Go to the bottom.
**Marc Pichler (Dynatrace)** 29:15 Yeah.
**Trent Mick** 29:17 Dan didn't have a reply. I think we can close this one, yeah?
**Marc Pichler (Dynatrace)** 29:20 Yeah, I think.
**Trent Mick** 29:21 You basically answered it.
**Marc Pichler (Dynatrace)** 29:23 I think we discussed this in the SIG meeting a while ago, and Oh, yeah, I commented here, anyway.
Okay, to keep it as is, So… I'm gonna close this as… Won't do.
**Trent Mick** 29:45 Basically, as planned, we did do it.
**Jamie Danielson** 29:47 I was gonna say.
**Trent Mick** 29:48 Yeah.
**Jamie Danielson** 29:49 Completed, yeah, because not planned seems like, no, we don't want to audit it, but you kind of Did and just said we're not gonna change anything.
**Marc Pichler (Dynatrace)** 29:56 Mmm.
I guess the comment is sufficient anyway already, so let's just close it as… Completed then.
Yeah, we do.
**Trent Mick** 30:11 Option 2, basically.
Yep.
**Marc Pichler (Dynatrace)** 30:17 Exactly.
Grant.
And that milestone also seems fairly close to completion now.
**Trent Mick** 30:29 Yep.
**Marc Pichler (Dynatrace)** 30:33 All right.
Any questions, comments about… Logs, or… Read it all.
But let's move on to the next one.
the release preparation PR. I haven't updated this one yet. I'll do so right after the meeting, so that.
We are in this.
**Trent Mick** 31:06 Is… so my naive question was, can I just… use the… the CI workflow, and it'll update it properly, or is this a special case because you had, like, that.
**Marc Pichler (Dynatrace)** 31:19 Yeah, this is… This is a special case because of the override that's needed.
I will run the workflow again, and then I'll just cherry pick that commit onto the onto the Pr that's created from that. And then it should be okay again.
**Trent Mick** 31:42 Okay, cool.
**Marc Pichler (Dynatrace)** 31:51 Yeah, and then the actual release, Like, once it's merged.
is… Taking the, where is it now? It's taking the suffix to determine Whether to use the canary or latest tech. So, There's nothing to like. Once the data identifier is correct.
It will use the correct tag as well to publish it.
It's really just the release PR creation that, might be a bit difficult to get right first, and then it's R.
Set already.
**Trent Mick** 32:52 This is just an FYI to people, I haven't reviewed this yet, but, Instrumentation base is painful, especially to browser people, and heads up, there are potential changes coming there.
**Marc Pichler (Dynatrace)** 33:06 I did have a brief look into… the proposed structure, and I think that, it.
Still implementing the instrumentation interfaces, the… Most important part to keep compatibility, I think.
a different instrumentation base from a different package should be fine, in my opinion. Not sure if there's any other… opinions out there.
**Trent Mick** 33:40 Yeah, no, I agree, but I think the thing that's not quite Clear from just the interfaces what the… like, what the contract is, who calls what methods, and what order. And, like, the order's all messed up right now, mainly because the… at least the node instrumentation base Calls enabled during the constructor, and also dot init in the constructor, and all of that's basically a mess, so… I think this is a… Maybe a bit heavy solution to try to make sure anything works there, because it handles any of these things coming in out of order, but So, anyway, just a heads up, I don't have a good answer for it, whether we can, like, have a simplifying assumption there, so things don't need to be quite as complex, but… Anyway, basically I agree with what you're saying. You shouldn't have to depend on the instrumentation package, as long as you're just following the existing interface. Then it can be passed in, and registered instrumentations is pretty straightforward in what it does, so it should be fine.
Yeah.
**Marc Pichler (Dynatrace)** 34:47 Yeah, thanks for bringing it up.
A word.
I'll give this some time, have a look at that. From what I gathered, from the Slack message, it seemed that this was not super urgent, but.
Jared was looking for early feedback, so I will… just put a comment on there saying that as long as the instrumentation interface is there, I think this should be okay, so that we can… Go ahead, if… He's looking to get that merged soon.
And then you can iterate on that later.
Not sure if that's at all helpful.
**Trent Mick** 35:42 Bye.
Or any old post.
Because there's some disagreement between maintainers having another maintainer review, and that would be helpful.
David added a review as well.
**Marc Pichler (Dynatrace)** 36:00 and Yeah.
**Trent Mick** 36:05 It takes some time to get into this one, though, so yeah, we don't have to discuss it now.
**Marc Pichler (Dynatrace)** 36:11 Yep.
I wish I could review all the PRs.
**Trent Mick** 36:17 Yeah.
**Marc Pichler (Dynatrace)** 36:18 I'm sorry for not getting to all of these.
Okay.
They're stacking up now.
I think that is… No, does anybody have any more topics to discuss?
If not, then we can have a quick look at… On triage box.
Looks like there's nothing in core, nothing… One thing in CONTRIP, Invalid OpenTelemetry span names.
Yeah, that is definitely a bug, and that causes… All spans to be dropped, I think.
So I'm putting P. 2 on there.
I think we have since updated, the core repo as well to make sure that this doesn't happen.
I'm not sure we've released that yet.
So… Or have a look.
But also, I think, span name like that should not be produced, so… I think it's fine to have that also be a bug for instrumentation.
clicks That's it for the contrib repo.
I'm gonna… propose skipping the old PR triage and give everybody some time back.
**Trent Mick** 38:50 Sounds good to me.
**Marc Pichler (Dynatrace)** 38:54 Brian.
more topics.
Then, thank you, everybody, for joining.
Have a nice week, and see you next week.
**Jackson Weber** 39:03 Have a good one, Ollie. Bye.
**Pranav Sharma (Google LLC)** 39:05 Thanks, James. Thank you.
**David Luna Bistuer** 39:07 Bye-bye.
