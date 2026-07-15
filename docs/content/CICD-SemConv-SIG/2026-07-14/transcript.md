SIG: CI/CD SemConv SIG
Date: 2026-07-14
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:36 Hello.
**Adriel Perkins** 00:40 Hey, good day, how are you.
**Christophe Kamphaus** 00:42 Financial.
**Adriel Perkins** 00:44 Okay, thank you.
**Christophe Kamphaus** 01:16 Okay, I will share my screen.
Not sure if you can see it, since you said you were on mobile.
**Adriel Perkins** 01:43 Yeah, I can zoom if necessary.
**Christophe Kamphaus** 01:47 Okay, I just wanted to start with some triage.
And, sir, I know that we had the… VCS span convention PR, that's still a bit stuck on the… Prototype.
And I know that,
**Adriel Perkins** 02:09 Okay.
**Christophe Kamphaus** 02:09 I don't know how you pronounce his name.
He wanted to try writing it and wrote in on Slack about it.
**Adriel Perkins** 02:29 It's about the, like, prototype itself.
**Christophe Kamphaus** 02:32 Yeah, to, to write one.
**Adriel Perkins** 02:35 Okay, thank you.
I think the preferable thing would be just a little fork of It gets CLI or something.
Or JJ Jujitsu.
But I, you know… depending… if we can figure out what the LOE on it is, then, you know, if it's, like, a really high LOE, And maybe we could, just wrap it.
**Christophe Kamphaus** 03:13 I found some prior art on it.
Not sure how difficult it would be to adapt.
Also sunset, I haven't seen… Much going on.
No report.
**Adriel Perkins** 03:44 Okay.
**Christophe Kamphaus** 03:49 So, let's come to our topics, and I think Sarah, Carlos, That's the first one.
**carlosalberto** 03:57 Yeah, hello. I was just talking to somebody about whether you consider something like, you know, like when it comes to the version control system, CEMCOM, like you always think of a monorepo situation, but what… If you want to consider two repos, let's say, because you actually did split one original repo into two and then you want to report that as the same thing, is that something that any of you have seen at all?
**Adriel Perkins** 04:30 Is that even possible?
Because they have different names, right? Like, I don't… I don't think in any VCS backend you can have two identical repository names.
**carlosalberto** 04:40 Right.
**Christophe Kamphaus** 04:42 You could report it as different.
Service names?
But that's on the level of your CICD system.
Other than that, yeah, I guess on organization level, you could report the organization name.
**carlosalberto** 05:04 -Yeah, I guess there are a few potential, so to speak, workarounds. I was just curious generally because if any of you had seen something like this already.
We could probably explore that. And basically, that's what I also wanted, to also get some prior art.
But if none of you have seen this, I will keep on digging and consider some workarounds.
Before I can try to propose something here.
**Christophe Kamphaus** 05:35 Yeah, I haven't seen anything like that.
**Adriel Perkins** 05:39 So are you thinking, like, where you have a repository that's a Git submodule of another reposit Is that kind of like…
**carlosalberto** 05:45 Not necessarily. Well, it could be probably, yes, that's the thing. Like you are, let's say you have configuration in some other repo and they're just… You know, creating a submodule?
And then, yeah, something like that, yeah.
**Adriel Perkins** 06:02 Yeah, so…
**Christophe Kamphaus** 06:03 That's.
**Adriel Perkins** 06:04 Also, that you would ever…
**Christophe Kamphaus** 06:05 We're talking about having several repositories set up.
logically belong together.
**Adriel Perkins** 06:14 Got it. Yeah, they're still separate repositories.
**carlosalberto** 06:19 Yep.
**Adriel Perkins** 06:20 But in terms of how you relate them together.
Like, I'll give you an example.
Yeah.
There's, there's a couple instances of of related like.
Like, for example, one repository is the source code for the actual service. And another repository is the deployment of that source code.
for that service.
And they are related.
Because you need both of them to get to production.
But they are different repositories. They're named different, so they have different VCS repository URL full paths. They have different repository names.
But the way that, like, well, I've grouped those, Is one by service name in that case, because they both relate to the same service.
And then another way to group them would be like a custom attribute. Like if you have like some type of organizational attribute where you have like a business application name.
You… that, like, has a bunch of services in it.
But it's really one singular application.
And spread across multiple repositories.
That's where you could use something like that as a grouper.
I guess the other potential, like.
From that perspective, if you have a… You have a service that's running production that's made up of two repositories and you want to track them back to both of them instead of just the deployment repository. I would still say like a running instance of a service should probably just only track to the deployment repository because then you can find the other one from there.
Yeah.
But, let's say that, you know, you have, You want to be able to track both of those repositories?
it might make sense where VCS repository name, VCS repository URL, could be incorporated in some type of list of VCS repositories, right, or array of VCS repositories on the service attribute, since we can do arrays and lists now, but I'm not sure how the semantic conventions would look for that.
Does that make sense?
**carlosalberto** 08:40 Yeah, that makes sense, yeah.
**Christophe Kamphaus** 08:45 Yeah, I think it's the common pattern to split the source code of your application and your infrastructure as code or deployment manifests.
**carlosalberto** 08:53 Yep.
**Dotan Horovits** 08:58 Carlos, was that with a specific use case or something that brought up this issue? I'm curious, what's the maybe scenarios that came up in that discussion and the context it came up?
**carlosalberto** 09:13 Sorry, I wasn't noticed, How you doing, guys?
Sorry, just the neighbor started doing so much noise. I was right in the window, in fact.
**Dotan Horovits** 09:49 Yeah, we can. We can get back to that another time. Just just curious if this has come up in a specific Discussion with some context, maybe this can help us understand, because we could try and imagine different Places, but if this actually came up with a specific need, maybe we can start with that.
But anyway, we can follow up on that.
Okay, so that that maps to, I guess, similar bit to the what Adrian was discussing before.
Thanks.
**Christophe Kamphaus** 10:45 So should we create an issue for that?
**Dotan Horovits** 10:54 I I feel that if we create an issue, we need to have some like someone to represent a strong need. So I don't know, Carlos, if you if you feel that the discussion you you took there.
give you enough of an incentive to drive this, or maybe loop in the relevant end users that brought it up. But otherwise, these sorts of things just… I don't know if there's no concrete driver behind them. That's my take on it.
**Christophe Kamphaus** 11:29 All right, sounds good.
Any other topics for today.
If not, then let's give it.
Let's give back some time and see you next week.
**Dotan Horovits** 11:51 Sounds good. Thanks very much, Christoph, for leading the meeting, and everyone, great seeing you.
**Adriel Perkins** 11:57 Thanks. Take care.
**Christophe Kamphaus** 11:58 Thanks. Bye bye.
