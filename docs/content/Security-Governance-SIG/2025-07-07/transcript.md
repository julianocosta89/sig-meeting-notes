SIG: Security Governance SIG
Date: 2025-07-07
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang** 00:11 Hello, Jeremy!
**Jeremy Corley** 00:14 Hello, Riley!
**Reiley Yang** 00:18 Hey!
**Jeremy Corley** 00:29 Hey? Yeah, let's see.
So we can wait one more minute. See if the ask anyone else to join.
**Reiley Yang** 02:00 Yes, we can start.
**Jeremy Corley** 02:03 Okay.
yeah. The the 1st issue that I had in the agenda there. I I guess it's handled. Now that was The issue where?
It sounds like, you know, they're going through the whole graduation process. And they, you know, found the remains of our our discussion about a security response committee. And I think we've got all those closed And so and it mostly was gonna see if if Trask was going to be here if there was anything else he heard that was hanging over from that. But I think I think we've got everything handled there now.
**Reiley Yang** 02:51 Yeah.
**Jeremy Corley** 02:53 So think that one's done.
**Reiley Yang** 02:57 So I'm I'm curious about how you think like moving forward. Do you? Do you still want a separate group handling this, following the Kubernetes model.
**Jeremy Corley** 03:10 Not for now I mean it. It's If if everybody's quote unquote, happy with with the way things are working. Now then, then. There's kind of not necessarily a reason to change it.
You know UN, unless, you know, there's we start seeing things like, you know, dropping through the cracks where, you know, either maintainers are struggling to deal with their own vulnerabilities, and we need to have that manage more centrally. Then then there's not necessarily a reason to do it differently in in my opinions.
Let's just have to say.
**Trask Stalnaker** 03:50 Hey folks.
**Reiley Yang** 03:52 Hey! Trust.
**Jeremy Corley** 03:52 So.
**Reiley Yang** 03:56 Yeah. So we were just checking about the the Security Response Committee that community issue related. So so Jeremy temporarily remove the the.
**Trask Stalnaker** 04:09 Was there anything more anything since we merged those Prs.
No, okay.
**Jeremy Corley** 04:19 I haven't seen anything else, so I was just curious. If you had heard anything where people were.
you know, found anything else, or or if there was any other discussion.
**Trask Stalnaker** 04:30 I haven't heard anything.
Hey? Assume that's good.
**Jeremy Corley** 04:36 Yeah, okay.
**Reiley Yang** 04:43 Is there like a like a security bar from Cncf regarding the graduation? I'll give example, like, if there's a dependency on a critical security, vulnerability? Is there expectation that the the fix and the new package should be released in certain number of days, or just every product they can define? It.
**Trask Stalnaker** 05:06 Oh, I see. So like once we're graduated. Is there a bar?
Not that I have heard.
I think they're partly the looking at the secure our security policies to see what we say, if anything about that.
But yeah, all I've heard, I mean, you know, there was the required audit, which happened like a year ago.
and so yeah, no, I haven't heard anything more.
**Reiley Yang** 05:57 Yeah, just I'm I'm thinking about some some of the the challenges. I'll I'll give one example. The the current collector has a dependency on the on the go to chain and the go to chain. If you look at the release history, it seems like they have a they have a bi weekly release. Every 2 weeks they release a new version, and some old version might have security vulnerability. So so, in order for the collector to the production ready and up to date. Number one thing is, if the collector has dependency on some gold packages that has known vulnerability, then the version needs to be bumped to the latest one that has a fix. Number 2 is, it needs to use the latest version of the compiler if the previous one has a known vulnerability. But when you look at the history, it seems people are doing that in the ad hoc way, so they will get someone pinging them, saying, Hey, there's a security vulnerability. It has been there for 6 months, and they will say, like oops. We didn't even know it.
and we don't have a detection, but they're willing to take the fix. So then fix the issue. Then, couple weeks later the similar issue would happen again.
So so my my gut feeling is many. 6 are in that situation, so the maintainers are willing to like, have people reporting those vulnerability and bump the version, or do whatever necessary, but they don't seem to have the right tools and procedure to make sure it's up to date. So normally, it's like after the fact.
And and maybe that that's okay for now. But how do you think about like improving that or like, is this something that Cncf would expect from opentelemetry? Or it's like per project. Maintainer's definition.
**Trask Stalnaker** 07:49 Yeah, I mean, I the Cncf is doesn't define a lot of that stuff. I wish they would. I I when I chatted with the security.
the security tag at the Cncf. I mentioned that like that it would be nice to get more guidance from them. At this point we get very little to none. Guidance from them.
The things that I would like that I think we can drive that makes sense to drive from this group.
One is I I would like to.
I mean, all the repos should have depend about our renovate and be updating dependencies regularly.
So I think we can do some checks on that.
A. To make sure that every but he has at least one of those tools and be that they're actually merging those Prs.
so some kind of automation, I think that would would be good. What I don't really want to do is go like to a particular repo like collector, and to say, Hey, you're not merging these like I I would want it to be from a automation across all repos. I don't want them to feel like we're picking on just that repo.
**Reiley Yang** 09:27 Yeah, so automation is one part. The other part is, how do we measure? Or we're okay with people leaving those Prs.
**Trask Stalnaker** 09:38 Yeah. So I think we can check that. We can do some automation to check that. There's no that those Prs are being merged.
But the second thing that I think would be good for us to look at is what kind of stuff Github has?
Cause we've got a lot of security stuff that I haven't really looked into, but they will.
Flag stuff depending on. Let's see. So these are coming from Scorecard.
Let's see, I feel like somebody has set up more scorecard. Depend a bot alerts.
It's like, Where is oh, yeah, so like secret protection.
Let me go to a Java repo just in case I do something bad.
Secret protection.
You know, we could enable code security code. Ql, I'd like to make sure that all the repos have that still doesn't quite address your depend about so.
**Reiley Yang** 11:52 Yeah, so currently, this tool seems like, we give people some recommendation. We're saying, this is cool. It helps you. And you decide whether you want to enable or not, and if you enable it, whether you handle things in a timely manner or not, it's up to your choice.
But I I feel as part of this group like like we want to reach the overall security. So it's better to give some tracking and some overall guidance, and maybe at some point, when we see most of the maintainers are ready, we can make a requirement there.
So which means, if the Maintainers are not putting enough attention to security, then we would rather them to spend more time there, instead of taking more and more features.
**Trask Stalnaker** 12:39 Yeah, I agree.
What I don't know is what kind of to like. I feel like there should be tooling, whether it's I know we we have Sncc, have had mixed results when I tried to use that, but something that would actually it feels like that should be like something an easy thing to have some automated tool that scans all our repos and flags. If there's known vulnerabilities.
**Reiley Yang** 13:14 It is actually hard from. I think the dependencies can come from either the package level dependency, then it's per language so dependable and renovate the the SIM to handle most languages reasonably well.
The the second part is, if you have any like tools that you use as part of generating the final artifacts. Like the compilers, the build tool, or even like test cases, they could potentially manipulate something and not including the code generation. But I know several like repositories. They have certain level of code generation, or they just copy some generated thing from another repository.
So so anything from the tooling part can be also considered as like dependency, like supply chain thing. And the 3rd part is the use of a a build environment. So some some folks they are using the the default. Github containers. There are also, like dedicated machines that people use for performance test, and some people might have access to those machines. So which means, if they got attacked.
whoever got the privilege, they can install additional things there.
So so I I feel like dependable and renovate. Probably cover most of the package level dependency and the Cicd container dependency or the action Github Action Dependency. But still their their gaps, and specifically like the example, could be the goal compiler it. It seems like like none of the existing boss, have the understanding. There.
**Trask Stalnaker** 15:05 Yeah, that's it's just surprising to me, had given the I know there's a lot of at least, I mean, now, it's not the new hotness anymore. Obviously. But security was 5, 10 years ago. Kind of a lot of people were investing into that security detection.
So yeah, I mean, I would like to look at, I think, if this group.
you know, if we can look at what automations, what tools are available already?
If there is a way to get Sncc to be helpful.
I think checking on the depend about or renovate automatically like is something we could do just to ensure that those those are happening and getting merged.
but it would still be nice to have something that's doing like a baseline scanning of all the repos.
**Reiley Yang** 16:32 And and another thing I notice is most of this boss. They don't seem to understand deprecated packages. I I know in rust there's a tool.
but it's not covered by a bot. So the bot will typically see if you use a package and you use an older version, and it has a known vulnerability. And the later version, fix that problem so it'll send you a Pr to update the package.
But it won't tell you you're using a package that has been there without any maintenance for 9 years, and what you should do.
**Trask Stalnaker** 17:08 Yeah, I ran into one of those recently. There was. What was the is it the mark? Oh, the Trc generation.
Markdown toc.
**Reiley Yang** 17:31 Oh, yeah.
**Trask Stalnaker** 17:31 Always last released.
Yeah, in 2017.
Yeah, that would be another.
I wonder if how to check that.
**Reiley Yang** 17:52 Yeah. So my my gut feeling is, we probably don't have enough manpower here. And I I feel what we should do is first, st we should establish some process if we identify a new type of issue like trust. You notice, hey? We we depend on a legacy package that has been there without any maintenance, then we should think about, hey.
this is not a single issue. Like we're we expect that there will be similar type of issue. Then we, we need to 1st let people know these are the potential issues. Then we let people know which part has been reasonably covered, which part is like a blind spot when we should seek for help. So so, understanding what's the what's the challenge? And what's the priority seems important. My main concern here is, it seems we're willing to fix the issue based on what we learn, and once we learn the issue, we'll go and fix it. But we don't seem to have the habit of hey? How do we systematically solve this? So we'll just solve the immediate issue and then believe everything is done. Then later we come back and see the similar issue again from another repository. We just keep learning from this.
**Trask Stalnaker** 19:02 Yeah, it's it's hard because of the how distributed our community is. To get everybody to and how underman, some of the repos are to get people to really invest time into it.
I'd like to 1st see what we can find from a tooling support like existing tooling out there.
Cause the more that we can provide tool lean. And you know, automate automated checks that then tell the you know, flag. These things for the maintainers, you know, create issues for them that the Maintainers can just go through.
I think the more successful that will be because, even like that outdated packages like I've seen in the in that step. Security dashboard.
One of the things they did was flag hack github actions that 3rd party github actions that have like 2 stars kind of a thing like kind of unreliable github actions.
yeah, there's a lot for this. There's a lot there. I mean, you know, I think it's okay. If it takes time, just keep chipping away at it. But I would love to feels like tooling should exist.
I don't know, Jeremy. You looked at Sncc a bit right.
Did you bring it back?
Did we get.
**Jeremy Corley** 21:18 Not in any depth.
**Trask Stalnaker** 21:20 Okay.
**Jeremy Corley** 21:20 Yeah, yeah, I I. And and mostly I'm just seeing, you know sort of the things that it's flagging. But I haven't. I haven't I? I didn't go too deep into it.
**Trask Stalnaker** 21:46 Only because I mean, it makes sense to start here, since the Cncf.
Has provides it.
But like we're not even running these collector.
What does?
Why can't I click on? Go? MoD 5.
Critical. Let's look at critical.
So maybe that's what maybe that's the 1st thing we could spend some more time on Sncc. See what we can cause this sort of. I don't know if this is related to what you were talking about Riley, of the go like.
**Reiley Yang** 23:26 Yeah.
**Trask Stalnaker** 23:27 Vulnerabilities being brought in via go itself.
**Reiley Yang** 23:31 Yeah. So I, I got some some email on the Tc Channel people reporting like one issue here, another issue on a separate repo. I think that's the dogs repo. And every time it, it seems to me like the Tc. Members are trying to just reach out to the Maintainer of that certain repo, and and then make sure, like they actually follow up. But as part of that thing like, when I work with multiple Maintainers, I start to see some pattern, and I start to feel, oh, like, if this thing keep happening today is on this report. Tomorrow, it's on a different report. But in the end it's just like 7 questions like you as the owner of this repository. Do you have a tool to check? You have package, level dependency and make sure you update them. Do you have a tool to check if you use that?
And like a deprecated package, or something that hasn't been maintained for years. And do you have the latest version of the compiler? And how do you update that? So so I start to form this like list of questions, and I feel if there like, if I know there's a good place I want to pull that like those things in the place, so I can share with others, and then we can keep improving that. And I would imagine that list won't be very long. It's just like 7 to 8 questions, and at some point the answer will be very different, depending on which project you work on like some project. They will say we don't even release a binary artifact. So we don't have compiler. We just like share the code. And we're done right. Then some some component might say, we we actually build the artifact, and we need to go through some signing process, and we need to publish it to a official registry or something. Then they will even care about who has access to the to the private key or password, or something.
So so everything will be different. And and currently my model like, when I think about this is this group should list out the the top level items, for like that would generally apply for all the projects in open telemetry, then we probably need to establish a contract. So every maintainer of a repository they need to give a reasonable answer to each of the question and the fact. They don't have an answer, for some question is already showing us. This is something they have to do, and because each language is different. If we have a general system that can cover all automatically, like depend about or renovate. That's great. But there are cases where we won't be able to like do too much here, because every like, for example, like, How do you actually push the package to your registry? Then the answer will be, for Java is central or something for Donnet. It'll be new guys. Everything will be different. And I don't expect this group to have the domain expertise for all of that. But we should be able to ask a very reasonable generic question from security perspective, like, when you build a package.
which machine are you eating? What tool are you using? And how do you publish? And how do you sign the thing? And how would people verify if the package, the artifact they download is actually the same as what you try to publish. And how do you communicate? If you've already published an older version of the package, and that thing now has a known security, vulnerability. Do you communicate? Do you even have a system? Tag it, or nobody would know, or your expectation is, as long as I have the latest version, you should always use the latest version. So this seems to be very generic to me, and my gut feeling is a lot of maintainers. They're not aware of this until they actually hit the problem.
**Trask Stalnaker** 27:15 Cool. So what do you? You wanna start an issue to where we start documenting these things.
**Reiley Yang** 27:24 I can't start a dog just capture, like what I already see, and we can probably add new things when we learn more and like, where where should that dog live? I think it should be in the security repo. But which dog? I'll just find a reasonable place to start.
And yeah, we can figure out what's the best place. But my, my question for this group is, once I have an initial list. What do we do like? We already know. Hey, we've seen this in a lot of projects that people publish a new package, and they don't seem to mark the previous package as deprecated, either because they don't even know about this, and then never thought about it. Or maybe the the registry system they use, like pi, or whatever that thing. Don't have this ability to allow you to mark a package as deprecated.
**Trask Stalnaker** 28:16 I've only even heard I've only ever heard of.net new get supporting that.
**Reiley Yang** 28:21 Oh, there's some convention about containers that can be published into docker hub, then there. But this is a problem. Right? Then the answer could be. Oh, we verified with the registry owner. There's no such way. Then we have some alternative way. Maybe we'll just like.
put that in our readme file or recommendation is as long as there's a new version, you always use that. But we we need to think about it, and how we, how we like, raise the bar there, that's my gut feeling, or you can. You can like, if both of you are saying we don't need to do that. Then I'm I'm fine. I'm just saying this this pattern over and over again.
**Trask Stalnaker** 29:00 Yeah, no. So I agree that there's a list of things I'd we may disagree on what belongs in that list. So I think we should just start creating that list, and we can talk about individual items in that list, and how we would communicate those to maintainers.
For now I would try. I would just keep it internal in this group. I mean, it can be a public issue. But the Maintainers get as you've seen, Riley. They get very easily panicked when the people tried to force things on them top down. So we just have to be kinda careful on how we push those kinds of things out.
**Reiley Yang** 29:53 Yeah.
**Jeremy Corley** 29:57 Yeah, yeah. And I see it as finding finding both the specific examples. And then seeing, does that bubble up to something generic like like, yes, we start collecting this list. We can. We can go both directions right? Because there can be oh, here was a specific example we had, you know. How do we genericize that? Is there a tool that already can help us do something with it?
You know, we can sort of go that direction or or yeah, from a high level going? Oh, you know.
Yeah, deprecation. Is that something you know that that, you know? Is there something. Can we get more granular with that? Is, is there a tool that helps us with that on on.
you know, various languages? So yeah, I think I think, starting the list in in in an issue on our side, and seeing what we can do about each item is is a good idea.
**Trask Stalnaker** 30:56 Cool. I'll I'll add snick to my explore list at some point. I will try to hook up. Maybe. Ja! I had hooked up Java at 1 point.
But it's not.
Maybe that's just like expired. Oh, no, it says tested 9 days ago, 19 days ago, 4 days ago.
So this can't really mean that there's 0 issues. I don't believe that it's just not. Hmm.
yeah. But I, Riley, I agree with the like, I don't want this group to have to be rest or.net, or Java or python like expert like, that's yeah. That's total completely out of scope for this group.
Cool? Maybe we let's see. I don't.
I know. Pablo was tagging the Sig group.
I'm trying to keep this group out of again deploying like these org level things. Because again, I know that there's people get have a lot of feelings about kind of org level changes. And so, if I can isolate, just make it responsibility of the Github admins to sort of roll these changes out on the Sig security, just making recommendations.
So I'll look through this today and try to.
I mean, I I don't really agree with some of it. The some of the premise. But I do agree with the overall, like I think it does. It will make people feel better to have kind of a rollout.
Some basic policy around that that we can point to Riley. Since we're both here, let's see what did happen here.
do you know, if there's been any more discussion on the in the C, plus plus.
Let's see, I think that it. I think it saw that Mark and Lalit were discussing.
Let's see, okay.
**Reiley Yang** 34:31 Yeah. So I have some contacts here. So initially, I discussed this with Ccntc saying, there's a preview feature of the coding agent. And and I want want to have couple repositories. Give a choice. I kind of like, ask around. Then I got several people reach out to me, saying they want to enable that. And because we already communicated. And this is a preview, feature doesn't seem to have been like impact. So I just like enable that per the Maintainer request, and for some of the repositories I just replied in their slack channel, saying, Hey! Like we enable that and give a try, give us feedback, and I probably missed one or 2 repositories. So I just let the Maintainer know. Hey, you already? See, I I made the announcement here, so I just enable this for you, and you can just copy paste what I have there. So I shared what the known issue, and some like workaround like the Edcla, and you have to add, like branch policy there. For this specific thing. I think there might be people who have concerns, because not all the Maintainers are notified or not. All the maintainers agree.
and some maintainers might have worry about this. So the like. The the ask. My understanding is that they won't have a more like a careful approach before any Pr actually got merged, because they they worry about. Maybe there's some like license or copyright issue.
**Trask Stalnaker** 36:03 Okay, so do you think we should?
I mean, we can't really use it right now, anyways, because of the easy Cla.
**Reiley Yang** 36:17 Oh, we can. Because if you, if you read the license and those things like the essentially saying, if you review and you want to merge the request then, like Github copied, and own that intellectual property so.
**Trask Stalnaker** 36:31 No, no, I mean from a I mean from a Cncf automation. The easy Cla check.
**Reiley Yang** 36:37 Oh, that part! It's possible that the Maintainer can just force, push, and rewrite the history if they really want, I think, ask co-pilot, go and update all the deprecated version to the latest version, and if they're happy with that they're blocked by either. Cla, they can just like pull the latest change, and rewrite the commit history, and then.
**Trask Stalnaker** 36:57 Okay.
**Reiley Yang** 36:57 Then they converse the Pr.
**Trask Stalnaker** 36:59 Gotcha.
**Reiley Yang** 37:00 That's 1 option. And I shared with a with a like couple folks on the slack channel so essentially like, let let them decide. But I like, I'm I'm not too concerned about like maintainers are trying to do any evil thing there.
So it's more about, hey? People notice this. They they just want to have a better process like like no maintainers, would want to get shocked if, like some maintainers want that to be enabled. But the other maintainers do not, and this was not even discussed publicly. So so that's the concern, I think.
**Trask Stalnaker** 37:44 Okay? So I mean, I think there's 2 pieces to this. One is the writing up?
well, there's a few pieces to this one is the part that I'm going to take on is writing up a policy for github admin org level changes to cover all org level changes like that basically requiring us to go through community issues and tagging people. And you know that kind of thing.
A second question here is what to do with this specific repo with this specific maintainer who's asking for it to be rolled back?
And the 3rd issue or question is sort of getting the probably the Governance committee to like officially. Bless copilot usage in open telemetry.
Given.
I think there will give. Let's see?
Yeah, given like this kind of basically just saying.
yes, it's okay to use copilot specifically in open telemetry. If you want.
**Reiley Yang** 39:35 So my gotcha is, we shouldn't talk about co-pilot specific thing. It's more about like using any generative AI or like AI assisted coding and in the community repository. We already have a Doc. I think Morgan or someone help on this because I met similar problem maybe a year ago. So so we already have a doc. And in that, doc, we also link to the Linux Foundation. Doc, I want us to maybe discuss, like among the Gc. And Tc. To see.
Is there anything we should improve in a Doc.
And that, Doc, I believe it shouldn't be co-pilot specific. What if co-pilots just gotten renamed? Or there's another thing that can do similar job here, then, like I feel the the the doc we have in open time tree should not be tied to any specific bot.
**Trask Stalnaker** 40:32 Yeah, yeah, makes sense.
**Reiley Yang** 40:37 Have you seen the yeah, the the Gen. AI, one. Yeah.
**Trask Stalnaker** 40:41 Yeah.
**Reiley Yang** 40:43 So we probably need to understand specifically what are the gaps or concerns. And how should we improve this stock.
**Trask Stalnaker** 40:53 Yeah, cool, I will. Maybe. Since I haven't been as kind of a 3rd party. I'll comment on this and ask Mark if he has any. If there's any part of this, the open telemetry, Gen. AI cause, I mean. It certainly was the intention that can I help.
you know? Can I use Llms? I mean, it's all the idea, is it? Was all yes, you can.
and just don't spam us with nonsense things.
Was the intent of this when it was written.
Because we had had we were. We had started to get spammed. A couple of repos were getting spammed by low quality. Llm, generated Prs.
okay, yeah, let me. I'll reply to Mark, and then let's see if he's still as concern and is pushing to roll that back or not. Cause. Yeah, I think you're right. Given. I don't feel like we need to take this to the Gc.
Given. It seems to fit into this policy already.
but we'll see what Mark comes back with.
**Reiley Yang** 42:46 Yeah, and for the for the rollback. Do do you think like we should do the rollback or my Varro.
**Trask Stalnaker** 42:51 Let me!
**Reiley Yang** 42:52 We'll just surprise the other maintainers who want. So so we can either just like, like, do this based on who's asking for a rollback, or we'll just proactively communicate to all the repository maintainers. Here, I can do that. I just want to see. What do you think.
**Trask Stalnaker** 43:13 I don't think we need. I think we could tag everybody and ask if there's anybody else who wants it rolled back.
I don't think we need to roll that back on Repos that don't have any objection.
**Reiley Yang** 43:29 Yes, I I chatted with last week. So 1 1 thing I could see is there. There's a trap here.
We have never clarified if we want to make a change at the repo level or the all level. But it's going to affect the repo. Then do we need all the Maintainers to agree. Or we need majority of the Maintainers to agree. Or we need just one of the Maintainer to agree. Previously, I was just like one Maintainer, because I don't feel this is like adding anything severe, and I also check the AI docs. I think it already covered what I want. Then I kind of took the the low bar. As long as there's 1 Maintainer confirmed they want to give a try. Then I'll just enable it for them to try with the understanding that I want them to give feedback. Then I can put up a more formal proposal.
But now.
**Trask Stalnaker** 44:19 Yeah.
**Reiley Yang** 44:19 We want all the Maintainers to agree.
**Trask Stalnaker** 44:22 I disagree with that. I agree with your approach of, and that's what I'm going to try to like. Write in the policy which is, I'd prefer for us to be able to move fast and roll back if we need. If, after that like, I'd rather optimistically assume that it's all good and move fast and not wait around for you know, waiting around for all maintainers to approve. Something is takes too long.
But that's also why I don't mind rolling things back if somebody does object so like I don't mind rolling this back for this one repo but let me ask mark if he has any, if he really wants it. Given that, I think that it fits in the Jen AI policy. But then I will tell him that we'll roll it back if he wants us to.
Given that. Yeah.
**Reiley Yang** 45:38 Okay. Thanks.
**Trask Stalnaker** 45:41 Yeah.
see, Jeremy, what you get to avoid by not having the the power, the the org level powers. It's like, not my problem.
**Jeremy Corley** 45:57 Yes, yes, with great power comes great responsibility. Yes.
**Trask Stalnaker** 46:09 Cool anything else we should chat about.
**Reiley Yang** 46:18 Oh! From my side!
**Jeremy Corley** 46:19 You have anything else.
**Trask Stalnaker** 46:21 All right.
See? Y'all.
**Reiley Yang** 46:25 Thank you both. Bye.
**Jeremy Corley** 46:26 Right. This is.
