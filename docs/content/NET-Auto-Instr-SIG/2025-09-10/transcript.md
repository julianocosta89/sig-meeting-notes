SIG: .NET Auto-Instr SIG
Date: 2025-09-10
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/Dg-i1y7x3rVhW7sqRbHRWqyDbfwQwmCJzR8tf0Gpul8ZtFJCZdBKw8zTjSJBoUbp.EU2COi0p2pHbSD3Z
============================================================

## Zoom Recording Transcript

**Zach Montoya** 02:00 Hi, everyone!
**Rasmus Kuusmann** 02:03 B.
**Zach Montoya** 02:23 Let's give it another moment, we can let some people trickle in.
Well, let's, we can get started, that way we use everyone's time wisely here. So I will go ahead and share my screen.
And, okay, so I don't see any, other agenda items, separate from our regular agenda, so I'll just… Get started on going through these links.
Alright, so, open pull requests.
We have one for N-Log instrumentation.
This one has been open for a little while. I'll watch… I'll go back and… see if there's updates. I had left some comments about some changes, for them to, push that through. And then we have one open Dependabot one. We can… I think this one should be pretty simple. Oh, it's not an SDK, okay, this will require an update, so we'll have to manually update that.
Otherwise, these look good. There's some other draft ones.
Is there anybody… anybody here have any… or need anything from us to… Advance the draft ones.
Alright, gonna go with a no.
Alright, so new issues… Okay, so we have a bunch of issues. I think these all, many of these ones here with the file-based one are… yeah, these are all, sub-issues, so we're just tracking that progress there.
And I do believe the… the YAML deserializer implementation was added, and then there's… there's additional tasks to follow up on that.
And then the other one is… this one with the naming of ASP.NET resources.
Rasmus, looks like this is actually… it's very related to what you were, bringing up with the, semantic conventions recently. Were you… have you taken a look yet?
Yeah, it's basically the same one, so now we've managed to connect different links, so they're all over.
It's so sad.
**Rasmus Kuusmann** 05:10 Issues.
**Zach Montoya** 05:12 Did you reach any conclusions? I know that you were talking with Lenmilla about… Are you at least having a conversation there.
**Rasmus Kuusmann** 05:19 So, basically, we need to understand what we want, and then… after final implementation, we need to double-check if it's… everything's fine with the Semcon.
**Zach Montoya** 05:33 Okay. So does that involve, like, just a POC then? Is that the next step? Or are there still some, like.
**Rasmus Kuusmann** 05:40 Yeah, I guess… We probably need to.
At least the first part is definitely fine. We need to replace ActionController There is, probably.
Similar stuff.
**Zach Montoya** 05:57 Okay.
**Rajkumar Rangaraj** 05:59 Sorry, I joined slightly late. Just wanna, as we are speaking on this topic, I wanna understand why this change should be part of this repo and not in the SDK.
**Rasmus Kuusmann** 06:12 Yeah, definitely the issue is in the wrong place, so… It's nothing to do with the auto-instrumentation, actually.
**Zach Montoya** 06:21 Yeah, like, I think this one actually looks correct. Like, this one, it should be over here. So we can… So anyway… Let me just close this one and suggest that it goes over here, although we need to make sure that their feedback or what they're looking for, is also captured there.
**Rajkumar Rangaraj** 06:40 The reason why I'm saying that is there is a mission to remove the instrumentation library at some point in time. So, only if we drive it as a part of the SDK, we can also drive… go back to the .NET team and say, hey, this is what we needed. It's a spec called compliant on everything, and when the like, span gets emitted itself, it should have the appropriate information instead of we going and doing some work on top of it. That was the end goal, that's why, from a .NET perspective, also SDK perspective, also, there is no… more traction in that space. But if there is a… like, also not many users did a thumbs up on that. Right now, we are getting the users. Probably it's the time to revisit the other part in the SDK area.
**Zach Montoya** 07:28 Got it, okay.
Yeah, it seems like that would benefit, at least, like, that discussion could use, like, a POC of, like, showing, here's what that would look like, you know, just using the Ace.NET contrib, package as, like, just a way to demonstrate it, but, yeah, I mean, this definitely doesn't belong in this repo, this belongs over here in contribib, and then we can… like you're saying, see if we can upstream that to the .NET team.
So, are you guys okay with, with closing this and just redirecting to, To this contribrib topic?
**Rasmus Kuusmann** 08:14 Or maybe we can just keep it open if anybody else is looking for it.
It is duplicate, but… I don't know. Informational duplicate.
**Chris Ventura** 08:24 Well, the issue will still be around, and so if we just simply have a note saying closed, I mean, it's already pointing to the other ticket, so… It's discoverable.
**Rasmus Kuusmann** 08:42 Yeah, definitely.
Maybe, might… You have a wrong intent that's… It's done there.
**Chris Ventura** 08:51 Well, if we make it clear that we're closing it because it's a duplicate, For… for the issue in the other repo.
**Zach Montoya** 09:12 Oops, my bad there.
Actually, I'll just grab that URL, okay.
Yeah, I think that's fine. We're just redirecting it.
Alright, I'll just go ahead and do that.
And then, aside from that one, I don't think there's any other new ones. These ones were all the, file-based configuration.
So, I think we can move on.
Discussions… Is there anything?
Okay, cool. Seems like there's nothing we need to follow up on there.
Issues that should be assigned to board.
Okay.
So, shutdown refactor… Yeah, I suppose we can put this one… Actually, does anyone have a background on what the… This is… Oh, okay.
**Chris Ventura** 10:12 It's a follow-up, based on feedback on a previous PR.
So, I think we talked about it during the last SIG meeting, where it's a nice-to-have to get done, but not required.
**Zach Montoya** 10:32 Okay.
So we already have this as the 1.13.
do we need to trap this on the project board if it's… Just a sort of nice-to-have backlog.
**Piotr Kiełkowicz** 10:44 Materos is on third PTR, he should be kind of… One or two weeks from now, and he promised to look into this.
Cool.
Probably yes.
**Zach Montoya** 10:56 Okay, so I'll do that. I will put that on the projects, which are reflected in a second, and then it's currently… We can put it as… committed if Natish said he was gonna take a look at this, and then we can always change it after that.
**Piotr Kiełkowicz** 11:18 But I would not consider it as a blocker for the next release, as it is kind of…
**Zach Montoya** 11:24 Got it.
**Piotr Kiełkowicz** 11:24 It's not a reflective.
**Zach Montoya** 11:26 Okay.
Yeah, that makes sense.
Alright, that's all of those issues.
And then the project board… Added… we just added this one a second ago.
the Lawsburg is still committed for just the general logging libraries.
One in progress regarding net effects. Is this still being… have to be looked at?
**Chris Ventura** 12:04 Oh, yeah, so…
**Igor Kiselev** 12:09 I'm still trying to address that also in my bigger change, how we would, which assemblies we would provide in different Ugh.
net-specific runtime folders, so I believe all… not all cases, but a lot of cases comes that we provide .NET, for, for 6 assemblies, for 6 two assemblies for, old runtimes, and probably some of cases of that issue may be solved with it. Some other cases probably would not be solved It's not possible to solve at all. So, still investigating, still looking and trade.
Hope to get some progress.
Maybe next month.
**Zach Montoya** 12:59 Okay.
Yeah, that sounds good, and then, with whatever progress you achieve, we can document which ones, which cases that covers, and then which ones are still left uncovered.
Is there anything that we can help with to, with your, like, in progress or with your investigation?
**Igor Kiselev** 13:20 Let me think about it, and I will try to provide some updates here.
what I can do, so… I'm not sure if you need to come on Tennesaw right now.
**Zach Montoya** 13:34 Okay.
Sounds good.
Alright, I don't really see anything else that we need to actively track.
I guess one thing we could do is we could also move… There's a whole bunch of the, file-based configuration stuff, we could add that to this committed, because it seems like we're just working on all the subtasks.
That's the only thing I can think of that we would change here.
**Chris Ventura** 14:08 I don't know if that's something that's neces… well, maybe, Piotr, you… you have more visibility. Is it something that we think will get done for, one… our… basically our next release? Or are we thinking that…
**Piotr Kiełkowicz** 14:28 Which one?
**Chris Ventura** 14:29 The file base… file-based configuration?
**Piotr Kiełkowicz** 14:32 I hope.
**Chris Ventura** 14:34 Okay.
**Piotr Kiełkowicz** 14:37 I have a plan to… put next chunk of this giant PR from New Guinea to review.
I'm not sure if current architecture is fully functional, so I will try to extract, let's say.
the resource configuration.
from this, PR and, Check once more time what… what can be improved.
I think resources are pretty simple, and there will be no discussions related to this domain, so it is a good playground to… To start with.
**Zach Montoya** 15:27 Are you opposed to me putting this… this larger issue, like, on the milestone project, or just do it on a smaller level?
**Piotr Kiełkowicz** 15:35 I think the big one.
**Zach Montoya** 15:44 So we'll do that… And we'll just say, we'll say this one's in progress.
Okay, cool. Yeah, so from here we can see the link to all the small, subtasks.
Alrighty, any other changes?
Which is, out here.
**Piotr Kiełkowicz** 16:09 There will be issue… there is an issue with .NET10 support, and I think it is also missing.
**Zach Montoya** 16:16 Oh, yes, I… I don't have a link. Do you… do you have that?
**Piotr Kiełkowicz** 16:21 I will check, and I will add it.
**Zach Montoya** 16:33 Yeah, this one, right?
**Piotr Kiełkowicz** 16:38 It is in the .NET. But yes, it is pretty important.
There is some functional changes in the activity sampling functionality.
So, worth to read.
At least.
**Zach Montoya** 16:53 Okay.
Alrighty?
Let's just put this in our notes.
Right, it's… So I think that…
**Piotr Kiełkowicz** 17:29 And I sent a link.
**Zach Montoya** 17:32 Oh yeah, I knew I saw. Okay, cool.
Score for .10… Okay.
Awesome.
So, for .NET 10, when is that releasing? That's in… is that in November?
Okay.
**Piotr Kiełkowicz** 17:53 Yes.
**Zach Montoya** 17:55 Alright, so maybe in… in October… well, I guess, is there anything that, you guys are worried that we need to start working on right now?
Or can we, you know, start tracking some stuff, like, in a few meetings from now?
**Piotr Kiełkowicz** 18:13 I think we mostly rely on SDK, and there is tons of job to do on Rush and Alan's side, to be honest.
Martin from Grafana, team, is… created already PR, and… Basically, it is… it should be pretty straightforward when it is merged.
Let's steal a couple of… Library updates is needed, and then we need to follow up with country repository.
And then here. For now, RC1 is not building on my local environment, and also on… CI.
there is some issue with detecting .NET, but I do not have time to investigate it yet. But RC was released yesterday, so… Maybe I need to raise an issue on the… .NET repository site.
**Zach Montoya** 19:13 Okay.
Alright, so for now… I guess, not much yet on this.
**Piotr Kiełkowicz** 19:19 It was for… In other words, it was working locally on my Windows machine with Preview 7, without any problems.
**Zach Montoya** 19:29 Okay.
So I don't have any other topics, does anybody else have things they wanted to discuss?
Alright… Looks like we're good for today. Oh, thank you everyone.
And, catch you next time.
Right.
