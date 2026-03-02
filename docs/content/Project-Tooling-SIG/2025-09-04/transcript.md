SIG: Project Tooling SIG
Date: 2025-09-04
Duration: 15 minutes
Zoom Recording URL: https://zoom.us/rec/share/MYRh43oSWPXRZhjUNlaB76tP8t0hhmzEIlS_jhBBj0j42qGOU4PZw39dgF4_CdIt.8fN82fBeP2Pl1AjK
============================================================

## Zoom Recording Transcript

**Antoine Toulme** 02:12 They knew.
**Trask Stalnaker** 02:14 Hey, Anton! Long time no see.
**Antoine Toulme** 02:19 Yeah, I'm trying to see how many meetings we can have together.
Bing that.
**Trask Stalnaker** 02:24 All the meetings.
**Antoine Toulme** 02:27 Trying to get the grasp of what's what.
**Trask Stalnaker** 02:37 Yeah, we don't really have a whole lot going on in this SIG, like, actively at this time. We may kind of reboot once Austin is back, and try to refocus and work on some things, but in the meantime.
If anybody… Including yourself, has anything… did I go frozen?
**Antoine Toulme** 03:03 No, it did not.
**Trask Stalnaker** 03:04 Okay.
**Antoine Toulme** 03:06 No, yeah, maybe I have some questions, maybe, for you in a more general sense.
I'm trying to see that there are some projects onboarding AI.
The operator is one of them. It added a Gemini-type integration, but it's not finished.
And every PR on the operator seek for last week has a comment from Jim and I saying, you need to finish the setup by going to the settings of your project and clicking something.
I do not know that this has been sanctioned, or this is okay, or whether we want to do it. I can show you an example.
**Trask Stalnaker** 03:42 I'm aware there's a… there's a community issue.
**Antoine Toulme** 03:46 Okay, cool, cool, cool, alright.
**Trask Stalnaker** 03:48 but, yeah, it's actually kind of…
I may need to just uninstall it for now.
Girl, sure.
**Antoine Toulme** 04:01 I'm not fond of it.
So… I'm, don't know what to make of any of this, to be frank.
**Trask Stalnaker** 04:12 Let's see, it is…
**Antoine Toulme** 04:18 That's right, that's his name, yeah.
Oh, you've got the wrong repo.
Oh yeah, that makes sense.
Yeah, okay, okay, so he opened that, okay.
**Trask Stalnaker** 04:30 So, the problem is that I can't sign the terms of… I mean, I'm gonna have to…
It's unfortunate that they ask for us to sign Terms of Service, because that means I have to get CNCF legal involved.
**Antoine Toulme** 04:48 Maybe that's a fine response.
But I think we… in some sense, it's out of your hands, right?
**Trask Stalnaker** 04:55 Oh, yeah, yeah, yeah, I just need to…
**Antoine Toulme** 05:00 Yeah, I figured it would be something like that, and I would want CNCF Legal to really be on top of it anyway.
**Trask Stalnaker** 05:05 Yeah… I mean, it's okay, we can normally install stuff.
**Antoine Toulme** 05:14 Yeah, yeah, yeah.
**Trask Stalnaker** 05:15 But other stuff doesn't… Nuts.
**Antoine Toulme** 05:17 to the tier list.
**Trask Stalnaker** 05:18 Yes, yeah.
**Antoine Toulme** 05:18 Yeah. Yeah, yeah, I mean, completely. Like, basically, I don't think nothing is stopping Pavel from running some sort of AI-type integrations on his laptop, or from some…
client that he has, and push some comments on the PR using a GitHub document or whatever he wants that can impersonate him or do work on his behalf. So, I think there are multiple ways to integrate this. I don't know that we…
Have to have a tight integration into our repository directly.
That's… Yeah.
**Trask Stalnaker** 05:49 Yeah, also, I mean, I didn't want to, suggest, because I didn't want people… didn't want to feel I was taking a Microsoft
Bent, but, co-pilot.
**Antoine Toulme** 06:02 Yes.
**Trask Stalnaker** 06:03 is… reviews… Do the same thing, and are integrated.
better… I mean, more native… I mean, they are native in GitHub.
**Antoine Toulme** 06:13 Yeah.
That makes sense. I understand also how this is a difficult thing. So, if you want someone else to
To make the comments, or respond, or provide some context.
And you don't want this to come back to you as if you're…
**Trask Stalnaker** 06:32 Microsoft, yes.
**Antoine Toulme** 06:34 biased, let me know, and I'm happy to
I'm happy to abound in that favor.
**Trask Stalnaker** 06:42 Sure.
**Antoine Toulme** 06:44 Or maybe it's a good time to just put up a notice somewhere of a documentation saying any service that is requesting terms of services needs to go through CNCF Legal. There is no way for us to do anything. It could just be in a…
in a template for asking for GitHub repository changes, to just have a little thing that says, I cannot help you.
Like, for anything that requires some legal review, you need… please be aware that we need to go to CNCF Legal.
**Trask Stalnaker** 07:14 Yeah.
**Antoine Toulme** 07:21 Why do you make it your problem to open the CNCF legal ticket? Why don't you ask Pavel to go open that for you?
**Trask Stalnaker** 07:27 Has to be somebody from the GC.
**Antoine Toulme** 07:31 Oh, okay. So, it doesn't have to be you, it has to be somebody from the GC. There is a little bit of a timeline here. You could ask that some member of the GC becomes a sponsor for this type of initiative. It doesn't have to be you, Trask.
**Trask Stalnaker** 07:43 This is true.
**Antoine Toulme** 07:46 I mean, I'm just looking at how much time you spend on Zoom talking to strangers, like, you know?
This doesn't seem extremely healthy.
**Trask Stalnaker** 07:55 Yeah, it's, the CNCF legal tickets, they're easy to open, but, like, I had to go through… I did have to spend way too much time on a Gradle enterprise, terms of service thing that…
**Antoine Toulme** 08:15 I can see it. Yep.
**Trask Stalnaker** 08:17 It… and it didn't end up working out. We had to stop using Gradle Enterprise, because
Linux Foundation and Gradle Inc. couldn't agree on terms of service, even though, I mean, it's all free, right? Like…
But terms of service, yeah.
**Antoine Toulme** 08:37 Lawyers?
Sure. There's… so is these computations.
Okay, so… If we put that up, that's okay. What else is going on?
I wanted to tell you about my absolute lack of progress of getting any attention towards better caching.
**Trask Stalnaker** 09:01 Sure.
**Antoine Toulme** 09:03 Not that it matters all that much, but I… about a month ago, when I started to attend those meetings, I mentioned to you and others that I've been trying to understand better how we can get more
Out of the current caching situation,
And I thought that it would be a good idea to… to do better there, so I opened a couple issues, one in Actions Cache, to ask for a best practice that would actually enforce that we have some level of caching that's done only on the main branch.
And then the fork branches will just have to read that and have read-only cache only.
And I started to also open an enhancement to the GoSetup, setup action that allows us to only restore caches.
in…
**Trask Stalnaker** 09:52 That would be nice.
**Antoine Toulme** 09:53 I noticed that in the Gradle action, you actually use that in the config repository of Java.
you have your stuff mindfully being, only restoring caches for Gradle, instead of writing to.
So, already precedent has been done, at least for a different language, in a similar fashion and similar approach. So I wanted to maybe also point that out to the setup go action. I just need to find the right documentation relevance for that.
But no one came back to me. Those actions are just sitting there, and today there's a new release of the Setup Go action, and I look at the changelog, and they have not taken even a look at my PR, and…
I don't know what to make of that, besides…
Maybe I should, you know, fork this thing.
**Trask Stalnaker** 10:41 Yeah, I mean, I've seen an overall…
trend that, it is really hard to get PRs landed into these big, You know, open source…
projects, I mean, or heavily used, like, There's just not…
there's a lot of PRs, they don't get… like, in OpenTelemetry, at least, we have
I think we have a pretty… Good.
I mean, like, Maintainers who are sponsored by their work to work on stuff.
**Antoine Toulme** 11:18 Nope.
**Trask Stalnaker** 11:20 a lot of these things, like, even if it's, like, official GitHub or official Go or stuff, like.
**Antoine Toulme** 11:27 Yeah, getting PRs landed.
**Trask Stalnaker** 11:30 I've seen… That, over and over.
I'm not really sure what the… I don't know what the solution there is.
**Antoine Toulme** 11:42 No, that was… Maybe if you have a secret handshake, but if you don't, that's okay.
Sorry.
I just need to live with an imperfect reality of where we are.
there's an obvious fix, is to fork and try it out and see if it works. Because I consider it, I've tried it at length in a way that maybe I try it for real for a couple months, and then come back and say, well, this was not worth the effort, and we go back to the mainline.
I know there's going to be a little bit of anxiety, because
I've done this before, right? Even for gRPC, I had a Protop library that I forked, because I had some needs for Parquet.
And the feedback I got was, the moment we depend on you.
at the OpenTeometry level, on your personal fork of this, that means you're now load-bearing, and we cannot
We cannot just trust you. We will rather trust this random open source project
Because it's been making releases, then your stuff that you just made up on the fly from that 5-line change.
I don't have the fix for this.
**Trask Stalnaker** 12:51 Yeah.
**Antoine Toulme** 12:51 That's what it is.
**Trask Stalnaker** 12:52 Yeah, I think it… for me, it usually boils down to, how much do I really care about this?
**Antoine Toulme** 12:59 That's true.
I think I do, but I have a very specific goal in mind. The contribository is attracting a lot of attention from first-time contributors.
and has…
really been striving under a lot of load, and is, as you know, 50% of all the minutes spent in CI. So.
hiking down any of that is always going to lead to disproportionate rewards. How do we… how do we make it easy for people to find their way into the project? Seems like…
contribute as a first stop, and then they make their way, and they start to trickle down into more discussions and more interesting things as they… So we need to find ways to kind of create a channel, like, comment in.
find your way through a country repository component that you care about, because you're using Collector as a user.
Because it's very much, like, a product-y thing, where you're not a developer, you're just dumping on your
DevOps environment, a collector as a Docker image, and it doesn't do what you want, or the contains to be better, you find your way into OpenTeometry, you make it better, and then you're like, oh, but I wanted my Ruby stuff to do better. And then you start to get more involved, and you learn about semantic conventions.
It's like you… you slowly get more and more integrated into the pantometry using these type of things, and I… I see a clear path of people who come in through this.
So, half of… half the PR is going to Country Bar. I am not a Go developer.
I have no idea what I'm doing.
**Trask Stalnaker** 14:31 It seemed to compile fine.
**Antoine Toulme** 14:33 And here's…
**Trask Stalnaker** 14:34 what Copilot told me to do.
**Antoine Toulme** 14:36 Yeah, all that. We're getting more and more of those.
But, you know, I'm a Java guy trying to fix something in my Java environment, but I need this collector to do something for me, so I'm going to come and do this.
Happens a lot.
So… I think this is a big…
big channel of adoption. We should… we should continue to push.
Okay.
**Trask Stalnaker** 15:03 Cool. Well, thanks for popping by.
**Antoine Toulme** 15:06 Have a good one!
**Trask Stalnaker** 15:07 Alright, you too.
**Antoine Toulme** 15:09 Yeah.
Chef.
