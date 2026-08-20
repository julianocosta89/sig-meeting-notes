SIG: JavaScript SIG
Date: 2026-08-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:57 Hello?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:00 Boom.
**Marc Pichler (Dynatrace)** 01:09 Just us today.
I think Trent is also out today, and Janie is out too, so…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:21 A lot of vacations.
**Marc Pichler (Dynatrace)** 01:24 Yeah.
I came back this week, so I'm well rested.
**Matthew Wear** 01:33 Whoa.
**Marc Pichler (Dynatrace)** 01:34 Hello.
Alright, I didn't… figure out what to do with my Zoom window. It always keeps blocking everything I wanna… use.
on screen. Alright.
So, let's get started.
The first topic here on the agenda today is from Marylia.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 02:25 Yeah, so this one… so I know that Trent is not here, and I think, like, he should be part of this conversation, but I think, like, there's a lot to read before having this conversation, so I want to, like, already give, like, a overview of what is happening, so probably we can discuss next week when Trent is back.
Because… so I created one thing, and he's changing a lot on the behavior.
So now, I don't know if I agree with that or not. So, to give context. So the… I created that new package that was for, basically, configuration.
So, my idea with that package, that that would be the package that would handle all configurations. So, if you're using, like, config file, or if you're using the environment variable, doesn't matter, because it's, like, all contained in a single package, and this way, whoever is importing, like, importing this and using would just get the objects, like, config, and use however they want. So… The… all the logic about, like, setting up and deciding all of that would be on this particular package. The pros of this is, well, as I mentioned, it's all contained in a single place, so if you want to add a new config or stuff, you just have to check on that package, and that's it.
The cons of this, there are, like, some things that… only exists on environment variable, like the… he mentions here things a little bit, like the node, like, the resources and stuff like that, so there might be some, like, mismatches if you're using from file or from environment variable. And I think, like.
Those were the main things. So, when I was creating this, I actually looked at other languages, how they were doing, and Java was not doing this way. They created a package that is just for configuration of the file, and whenever they were importing, they were like, or we import this, or we still need to have all the functions for the other stuff.
So, actually, I went… like, and I see others that were, like, doing something similar, and I kind of asked them, like.
why it was being done this way, and I share my idea, and they actually say, like, oh, we regret not making the way that you did, because it created, like, some burden for maintenance for them, and they wish they had done the way that I did it. So I was like, okay, so I saw that as, like, a positive from people that had the experience of It should be in a single place.
So yeah, this is how I created… what Trent is doing in this PR is changing that behavior. So he is making the configuration package only handles the config, and returning, like, the file.
and then whoever is important now has two functions, or, like, call that configuration, or now all the… creating, like, the config objects from environment now is handled by whoever is using. So, for example, here he's changing the SDK node, so now the SDK node instead of just doing, like, give me the config, it's doing, give me the config from the file, or give me the config from pharma, so all of those functions of setting up.
are now on the SDK nodes.
The pros of this is that, for example, now the configuration package is lighter, because it only handles the file parts, not the environment. The mismatch of environment and the file. You don't have to really think about it on the configuration.
But then the cons is now your configuration is all over the place, because right now we're… he's doing this for, like, this part of the code, but I'm assuming now the next step is to update this on every other packages that use config, so now you're gonna have the repetition of code.
on every single package, which was… I was trying to avoid. So yeah, Trent is putting, like, his case here on how I think that is the best approach, but I was like, I think still the other is the best approach, so we need more eyes on this, pretty much.
So, because it's a long PR and a long thread, I don't think we will be able to, like, discuss this now.
But I want to just, like, give the heads up. People take some time to, like, look at this, have their own, like, opinions, and then we can discuss next week when he's back.
Unless somebody already has an idea now, of course, I'm always happy to hear.
**Marc Pichler (Dynatrace)** 06:51 Yeah, I don't, have an idea yet, because I didn't look too much into it. Yeah.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 06:56 Is a big one.
**Marc Pichler (Dynatrace)** 06:57 So, Yeah, I will definitely have a look, and I think discussing next week is a good idea then.
this PR is currently, what's the status here? It's not approved yet.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 07:16 No, no.
**Marc Pichler (Dynatrace)** 07:16 So… Just making sure that we don't merge it,
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 07:21 Excellent.
**Marc Pichler (Dynatrace)** 07:22 accidentally. Alright.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 07:23 Yeah, so he put in, like, all his description, and I put, like, a couple of comments describing, kind of like this, what I said, like, what I feel like are a few pros and cons of each approach, so, yeah.
**Marc Pichler (Dynatrace)** 07:37 Right, I will have a look at this.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 07:39 Yeah, the code itself is, like, fine. There's, like, if that is the approach, like, you would be, like, good to merge. The code itself is fine. It's just a decision of, like, if that is the approach.
**Marc Pichler (Dynatrace)** 07:53 Do you know what sparked this change?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 07:57 Oh, no, I was kind of, like, surprised by it. He gave me the heads up. He's like, I'm creating this, and I think you want to look at this. I was like, yeah, I definitely want to look at this. But he, like, sent me, and then I was like, and then I'm going on vacation, so he… I'm just joking, he dropped a bomb, then left.
So, yeah, I don't know the motivations, but… I'm assuming it was because he was working a lot on the resource detector changes, and that is the one that is kind of like… Weird, if you compare it with the file versus the environment variable, so maybe that was the thing that sparked his… decision, but I don't think that is enough, argument to change the whole thing.
**Marc Pichler (Dynatrace)** 08:38 I think the way that resource detectors work, they don't really have a spec, right? So, it's kind of different for all of them, and making it work with declarative config is a bit of a pain.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 08:50 Yeah, one of my SIG.
**Marc Pichler (Dynatrace)** 08:52 D.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 08:52 Yeah.
My suggestions at the end, I put out, like, one, like, alternative is having, like, the configuration, like, not deal with the resource detector, and it's kind of like, whoever's using can, like, augment the config, like, objects to add those extra stuff.
So this way, still everything else is, like, contained on the config package, but people that want to use still have the ability to add more stuff that makes sense only for that package, or whatever.
**Marc Pichler (Dynatrace)** 09:24 Nope.
Alright, I will have a look and try also to figure out, the underlying… Issue that it's trying to fix, and maybe we can find some middle ground here, as well to make it work with the resource detectors without Like, ripping out all the things from the configuration package and moving it around.
I'm sure we'll figure something out, so… Yeah, let's discuss next week. I encourage everybody to have a look.
At this, inform an opinion about it, and then we can… jump into that topic next week.
Yeah, Marylia, feel free to, add another section here, and, for next week, and just put that as the first topic, so that… We can make sure that we have enough time for it.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 10:29 Yep, sounds good.
**Marc Pichler (Dynatrace)** 10:31 Okay, thank you.
Then, moving on, pranav, you have a topic about, GenAI Util package.
**Pranav Sharma (Google LLC)** 10:49 Yeah, yeah, I think… I was unable to join the meeting, last week. I think Surya presented that we were gonna do the… open inference, donation that we had, for various Gen AI instrumentation packages, so this is just a PR to, like, have a utils package, which ensures that, you know, there's SEMCON compliant and, like, consistent instrumentation for all these instrumentation libraries that are related to Gen AI frameworks.
So, I just wanted to make the community aware of this, PR, and hopefully try to get some reviews on it.
I'm mostly modeling this after the Python one, which is why, like, it has gotten a little bit big, because I think that library was, implemented incrementally, and we are just, porting over all the features at once that that utils package has. So… Yeah.
**Marc Pichler (Dynatrace)** 11:46 So, just to get a feeling of how this is supposed to be used. Is this supposed to be used internally by, the packages that are being donated, or is this supposed to be used by… End users as well.
-Oh.
**Pranav Sharma (Google LLC)** 12:03 mostly used for the… supposed to be used by the instrumentation library authors to make sure that, you know, the instrumentation libraries are, somewhat consistent in their use of semantic conventions, and Yeah.
**Marc Pichler (Dynatrace)** 12:20 Would it, be possible to… Start with one of the instrumentation libraries first, and add stuff to the utils package.
as it's needed to avoid having, stuff possibly in the Gutierrez package that's part of the public API that we might not need.
**Pranav Sharma (Google LLC)** 12:46 So, So there's already, I think, there's one instrumentation that was, that's also in a PR state for Gen AI-specific instruments.
**Marc Pichler (Dynatrace)** 12:57 innovation.
**Pranav Sharma (Google LLC)** 12:58 I think it was OpenAI one. So, this library, the user's library, is supposed to be used by that instrumentation, so, I mean, this needs to be there, Before the instrumentation is added.
Are you suggesting that, we should first get an instrumentation, GenAI instrumentation in, and then refactor it.
**Marc Pichler (Dynatrace)** 13:28 I use the…
**Pranav Sharma (Google LLC)** 13:28 library?
**Marc Pichler (Dynatrace)** 13:30 Yeah, what we can do is we can, have a PR that just adds the GenAI YouTube package.
without actually containing any code, so it wouldn't have any code yet, and then once there's changes made to the OpenAI instrumentation, or, like, instrumentation is donated, we add these functions as they're needed.
So that we don't end up with more than we actually need.
**Pranav Sharma (Google LLC)** 14:01 One of the… Would it make sense to, like, like.
would it make sense to, like, make all the… like, we… whatever code we have in this PR right now, we leave it as is, but, like, we don't export everything at once, so that it's all, like, package private, so to speak. Like, we don't export it out, and then, the instrumentation authors can just, Modify this library to, like, keep exporting the code that they need.
Would that make more sense?
**Marc Pichler (Dynatrace)** 14:32 That could also work, yeah. What… one of the issues that we have had before with packages, and that's also the reason why I'm suggesting doing, an approach where we only add stuff that we need is, We had a bunch of… Things exported that, weren't really necessary to be exported, and that made it super difficult to actually stabilize packages.
**Pranav Sharma (Google LLC)** 14:59 No, I…
**Marc Pichler (Dynatrace)** 15:00 I understand that. So your approach… Helps out with that. But then it's, I think it might add some friction to getting the PR merged, because, there's a question of… like, you have to ask the question, do we actually need this?
For each one of the functions that are being added.
And for each one of the types that are being added, and when we… already see where it's used, then that question is answered automatically.
And we don't need to… Wonder if we are building the right thing here.
**Pranav Sharma (Google LLC)** 15:40 I see. I understand that concerns, but, would it help alleviate that concerns that, the instrumentations that we are planning to add, the GenAI framework instrumentations that we are planning to add in JS were already added in Python, and you know, the library is using almost similar functions as they are being used in the Python one. So, like, we have the Python one as a proof of concept for what functions would mostly be required.
I mean, Python community has already done the legwork for us in this regard, so…
**Marc Pichler (Dynatrace)** 16:27 I have to… say I don't have enough insight into these, packages that are being instrumented to be able to say whether, modeling it on top of the Pythonuters package make sense or not?
Because I don't know how the packages are structured internally. So I can't answer that question right now.
if it would alleviate it or not. I would say that depends a lot on, like, how the instrumented packages Deviate from each other.
Or not deviate from each other.
**Pranav Sharma (Google LLC)** 17:07 Okay.
Since they were all ported from the same donation, like, open inferences, I know there must be some language-specific differences between Python and TypeScript, but, I imagine the… the… public API, would remain largely the same.
But, I do like the idea of, like, not exporting anything by default, and then, as in when we keep adding the instrumentation libraries, we export packages, we export the functionality out of this utils package.
That seems very much acceptable to me.
And I will be working on the instrumentations next.
like, porting over those instrumentations next, so, like, I will be actively working on this, thing.
**Marc Pichler (Dynatrace)** 17:59 That sounds good. Then let's go with the non-exported thing first, just to make sure that we don't end up with a large package that… People might start depending on.
**Pranav Sharma (Google LLC)** 18:13 That sounds… that sounds very reasonable. Thank you.
**Marc Pichler (Dynatrace)** 18:17 Alright, thanks.
Does anybody else have any, questions, comments?
He's blocked. Then, let's go ahead to the next topic.
This is the instrumentation development… Support… That we were talking about as a car for review, right? I guess nothing much has changed. There is… Just needs to be… looked into.
**David Luna Bistuer** 19:07 Yeah, Matt, Trent and I were discussing about this last week, so… but he's leaving that review, so I'll prefer to wait for him to… That gets hit background, but it looks good, so… But, we are on the right path, here.
**Marc Pichler (Dynatrace)** 19:31 I unfortunately won't have time to look into this, but if Trent is back, then,
**David Luna Bistuer** 19:37 Yeah, goodbye.
**Marc Pichler (Dynatrace)** 19:41 Alright.
I guess we don't have any, thoughts, or… things that we would like to discuss about this yet, but… encourage everybody to also have a look at this, and form an opinion about it, so that, we can have discussions, next week in the SIG meeting, or on the PR, async.
Alright, it looks like we are at the end of the topics for today. Does anybody have… Anything else you would like to talk about?
If not, then, I…
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 20:41 I'm just gonna bring one topic, in case people are not on the Hotel Maintainers channel, take a look or share a message there. I know we are having a lot of… Basically.
maintainers or contributors talk about a lot of AI contribution that has a lot low quality, or just overwhelming amounts that people have to basically review. So we are trying to find ways to, like, improve this experience for everybody. So I share a message there with, some ideas, but we also have an issue if people want to share, like, feedback or discuss about it. So, yeah, please do so.
**Marc Pichler (Dynatrace)** 21:25 Thank you. I haven't read it yet, but I will have a look at it.
I've seen a lot of AI contributions, too, and… there's some… Definitely some that are helpful, and some that are less helpful. So it's… Sometimes difficult to sort through those.
So yeah, thank you for… I'm writing that up.
I have a look at that, precinct later.
Our copy app is so… triage section, if there's no… topics that you would like to discuss, then I'll just go real quick, and… let everybody know that the SDK 3.0 work is coming up, so if there's anything that you would like to see, being added to the milestone.
please feel free to comment on the issues, or bring them up, bring them up in the SIG meeting here.
And then we can add it to the milestone, or have a discussion if we can, possibly push that after SDK 3.0. The timeline for that is we wanna release on September 30th.
So, the timeframe in which we would do the 3.0 work is a lot shorter than what we had last time around with 2.0.
So… yeah.
Just wanted to let everybody know that this is happening soon.
And… There's no… Questions or comments, then we can move on to bug triage.
Looks like there's actually quite a few of them here. A lot of them already have… PRs… Which is good. The first one here is in fetch transport.
Seems that… There is… Causes… Export requests to fail.
And the PR here… Already has one. Uber.
Looks like the lead step is failing. I might have had a look at this, and Did see the… Response here, and try to rerun it before.
Let's see if another rerun does trick. I think there's a PR open to actually, defer the link check to only run once a week, on a scheduled run, which… I think I would prefer, because we run into this here a lot,
**Matthew Wear** 25:06 I think that lint is failing on one of my PRs as well, for unrelated reasons, I think.
Yeah, that is… you know, Temporarily unreachable, or it's dead.
**Marc Pichler (Dynatrace)** 25:19 Yeah, there's quite a few of those. It doesn't always fail on the same, same link, it's just that there's so many that, one of them is bound to fail, and, now we are getting rate limited by… I think it was one of the Slack links or something.
So, yeah, I will actually… look for that PR and assign it to me so that we can… get that done a bit more quickly, because it's actually blocking quite a few PRs.
So I'm just to myself.
If anybody else gets to this PR first, please feel free to review it, and if you have reviewed it, merge it in, so that we can unblock the others. I haven't looked into the contents of that PR yet, but… If it does what I outlined in the issue, then it should serve the problem.
Alright, going back to the bug, it looks like this is at least a P2 issue to me, because telemetry is not arriving where it should.
And I'll put the OTRP exporter base… Labor on it.
And we can continue with review on the PR.
And once the check passes, then we can also merge that in.
Perfect.
Back to… On triage box, we have… back production builds for SDK node.
Breaking… Seems like this was decent.
change, starts failing in 2.20.
as it worked before and is now failing on build, I would mark this as a P1 bug.
And this is affecting SDK node.
So I put that label on here as well.
Might have to dig a bit more into what the actual issue is. Might be related to the… Recent move of… the SDK trace code to the new SDK trace package, and… Changes that… We're necessary to make that happen.
This is awful.
Try to review this PR.
Looks like the reproducers were, so… Should be… Fairly easy to check if that actually serves the problem.
All right.
Moving on to… I'm here. Opentelemetry trace and log providers can skip a processor that was registered when Shut down or force flush begin.
Okay, so that seems to be one issue, and… That's a mechanism in which that breaks stuff.
That also looks like P2 to me. Seems that there's… It ends up in a state that it shouldn't end up in, and then skips a bunch of stuff, which isn't great.
So… I actually wonder if that also affects the… No, it wouldn't affect the metrics SDK, because the way that it's structured internally is way different from what traces and logs do. So, I will put SDK logs and SDK trace… for this issue.
Yeah, drop telemetry is definitely… at least P2.
I think there was some requirement for that, too.
the role, I'm not sure if there's… Some spec that says that, The processors should never throw, but, still worth… fixing, I think.
Alright.
So that should be it for the core repo, and for counter repo, we seem to have no new bugs reported, which is great.
Alright.
So, that is it for backtriage.
Does anybody have any topics you would like to do?
Discuss… Bring up.
If not, then, Come on, if we can end the meeting here. I'll take some time myself to look at PRs after this.
And encourage others to also do the same. We have quite a few.
PRs.
in the ContraPend Core repo to review right now. So, investing some time is definitely a good idea, I think.
Alright.
Then, thank you, everybody, for joining.
Have a nice week, and see you online, or next week.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 33:08 Thank you.
**Daniel Dyla (Dynatrace LLC)** 33:09 Thanks, Mark.
**Marc Pichler (Dynatrace)** 33:10 Thank you, bye.
