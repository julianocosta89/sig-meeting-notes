SIG: Security Governance SIG
Date: 2025-10-13
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:49 Riley!
Welcome back.
**Reiley** 00:56 Thanks, Tras. Can you hear me?
**Trask Stalnaker** 00:58 Yeah.
**Reiley** 01:00 Okay, cool.
**Trask Stalnaker** 01:07 I don't think a lot… going on… Security SIG, we did… Jeremy and I did review… Your PR?
The process, maintainer, process… Recommendations?
So, and I think we're both good with it, just there's… You know, there's a… Some comments there, just…
**Reiley** 01:39 And I'll… I'll catch up on that and resolve the comments.
**Trask Stalnaker** 01:42 Coco.
**Reiley** 01:43 Thanks for that.
**Trask Stalnaker** 01:46 Yeah, and then I think, yeah, once we merge that, then we can, Discuss that with the… in the, spec maintainers meeting, and… Kind of tried to… outline what… kind of… If we can provide more specific Like, a way for people to meet those, Especially, you know, what to do with the, renovate, or Dependabot security.
**Reiley** 02:27 Yep.
**Trask Stalnaker** 02:29 I was playing around with that a while back, the Dependabot security stuff.
But haven't followed back up on that.
**Reiley** 02:39 Yeah, I have a question about the security advisories. So, working with a couple SIGs recently, I think that's a SWIFT SIG, I… I start to feel if there's something we can help the maintainers to be more efficient. So, for example, currently, if there's a user going to GitHub and file a private security advisory on the Swift repository, the maintainers won't see that, the maintainers won't be notified.
Only people on the security rotation would be able to see that.
**Trask Stalnaker** 03:12 I thought that's what the… that bot, I remember the initial incarnation of the security SIG, Created a bot to automatically add maintainers to… as collaborators on the security stuff. Is that broken, maybe?
**Reiley** 03:33 Maybe broken, yeah, but I'm thinking, like, first, I think it makes sense if the issue is filed directly on the repo, the maintainers should be able to see that. I'm less worried about, like, people filing something on the wrong repository, that the, like, people realize, like, they are saying something sensitive, which is not related to them. So I'm less worried about that. I think it makes sense for maintainers to see that. So just want to check if that's being… So, should we bring this up, or is it just, like, the expected thing? We should just go and fix it, and make sure the maintainers can see that first time?
**Trask Stalnaker** 04:12 Yeah, we should make sure that maintainers can see it right away.
**Reiley** 04:17 We shouldn't be.
Yeah, then I'll follow up and see what happens, and see what we can do.
**Trask Stalnaker** 04:24 Yeah, I wonder if there's a better way in GitHub now, like, if you can… Because remember how we made this? We made… The security manager… Team at the org level.
I think that's at the org level, can we give… Maintainer…
**Jeremy Corley** 04:45 Yeah, I thought that was…
**Trask Stalnaker** 04:46 Have a separate…
**Jeremy Corley** 04:47 I don't have a separate… Yeah, I thought there was a security maintainers for the… Isn't there a security maintainer's… Some weird feedback. Some weird feedback. Some weird feedback. Oh, sorry, let me… let me switch…
**Reiley** 05:13 Okay.
**Jeremy Corley** 05:14 That might be better.
**Trask Stalnaker** 05:16 Cool.
**Jeremy Corley** 05:16 I think that there's a security maintainers group that automatically gets to see all advisories.
Is that… is that the same thing that you guys are talking about, or is it…
**Trask Stalnaker** 05:31 Yeah, the problem is, I think that is… Only at the org level.
**Jeremy Corley** 05:39 Hmm.
**Trask Stalnaker** 05:40 And 2…
**Reiley** 05:43 Hi.
**Trask Stalnaker** 05:43 Don't think there's a s…
**Jeremy Corley** 05:45 Right.
**Trask Stalnaker** 05:51 Let's see…
**Jeremy Corley** 05:56 Because I think by default, all maintainers get to see all advisories, and all security maintainers get to see all advisories.
**Trask Stalnaker** 06:06 all maintainers…
**Jeremy Corley** 06:12 Like, for a particular repo, all maintainers… Of that repo get to see all advisories.
**Trask Stalnaker** 06:18 I don't… that's the problem that we had before.
that that didn't… even though that seems like it should be the case, I don't think it was.
**Reiley** 06:28 Yeah, at least from what I heard from the SLIFT folks, so this is what happened. I was a security on-call, and I noticed a security advisory, which has been there for days. I notified the SLIFT maintainers, and some of them may be in Europe, so it took a day, and they came back.
Saying, how can we get notified in the first place, and how can we, like, have access to this thing by default without, like, you being… the man in the middle trying to roll things. And I… I feel it makes sense for them to, like, have immediate access when the advisory is created on their repository, and it makes sense for them to get notified instead of someone in the middle trying to Ping them.
**Trask Stalnaker** 07:15 Riley, which, which repo is this? Because I'm not seeing the advisory…
**Reiley** 07:27 I have to check.
Also, it's a little bit strange to just ping people on Slack, because, for example, like…
**Trask Stalnaker** 07:38 it is, I know.
**Reiley** 07:39 I don't even know if that's the right name, so I have to find someone who I trust, then… I'll ask, hey, can you just add the other maintainers?
**Trask Stalnaker** 07:49 Yeah, that would be… worth solving, at least the maintainers, like, I feel like we should have a central location for all maintainers, Slack.
Aliases.
**Reiley** 08:07 Even this is private, IE.
Oh… This example is from EBPIF I found.
you can see the history there, I have to add the maintainers, and then I have to go to Slack and ping them, and I only found 3 maintainers instead of 4, so I have to ask another maintainer to add the remaining one.
Oh, you should be able to add the maintainer team as a collaborator. I can. I added them, but my worry is they probably don't get notifications, so this is why I decided to pin people on… Slack. And also, I worry about, like, if I send to a team, then there's no clear accountability, so I'd rather put the individual's name there.
**Trask Stalnaker** 08:52 Okay.
I think the automation that we had, was… Adding the team.
But yeah, what happened to that automation? Why is that?
**Reiley** 09:14 Anyway, so I'll do some digging after the meeting.
**Trask Stalnaker** 09:18 Okay, I mean, I know the, it was… there was something on Zapier which I have access… .
**Reiley** 09:30 But I have a small goal that I want to see if we can avoid Slack, so, like, purely rely on GitHub workflow, because the identity on Slack could be misleading. I… sometimes I find, like, the same name being used by two different folks, and one is just fake.
**Trask Stalnaker** 09:49 Yeah.
Yeah, I've had that problem on.
Slack.
**Jeremy Corley** 10:01 the link I just put in the chat was saying that Users have to actually modify their own references, own, settings in order to… In order to, sort of, subscribe to the notifications themselves.
**Trask Stalnaker** 10:24 Subscribe to… Security Advisory notifications?
**Jeremy Corley** 10:30 Well, it's basically saying… It will notify maintainers and security managers if they're watching the repository for all activity and they have notifications enabled for the repository.
And then it has a brief little description of how to… the link in the… in the chat, I just put in the chat.
Where I'm reading it.
**Trask Stalnaker** 10:52 Okay.
So, the problem isn't so much the notif… I mean, I guess that's one issue, the notification The first issue that we have to solve is that they don't even have access And I'm looking on Zapier, that integration, the security advisory workflow integration, is turned off right now.
Let me look in the community repo issues, Probably… it's possible I did that in response to something? I don't know. Let me see… I would have created a community issue, though.
Huh.
Why was it turned off?
That makes no sense.
Okay, well… I'm gonna turn it back on, and we'll just see what happens.
I can figure out how.
There we go.
**Reiley** 13:31 So, Charles, maybe we can… Follow up offline after the meeting.
**Trask Stalnaker** 13:38 Sure, sure. Well, I just turned it on.
Okay, so it was off.
I have no idea why.
**Reiley** 13:47 Yeah, I wasn't sure whether it's related to some, like, general guidance from CNCS.
Or something, so, like.
it seems we're lacking some history here. And by the way, I also have some small things I want to achieve as part of this. For example, I noticed when I add the repo-level maintainers, they somehow Don't have access to add other collaborators.
I feel they should have the power to invite someone.
or remove someone. Like, currently they have to ask They have to ask us.
Which is very.
**Trask Stalnaker** 14:23 Yeah.
Yeah. Yeah, I don't like the whole, GitHub security advisory, permissions don't make sense to me. Like, I don't understand why maintainers would not have access to security advisors. That seems like the whole point of maintainers.
**Reiley** 14:46 Yeah.
Maybe they worry about someone fighting, for example, there's a… A widespreading issue.
And instead of filing that, like, split that on multiple repositories, just file that on one repository, then they wouldn't want that repository maintainer to know the security problem from other repositories.
Something like that, maybe.
**Trask Stalnaker** 15:09 I guess, then give us another role that we can decide, hey, we're cool with giving maintainers security advisory access.
Like they do at the org level.
**Reiley** 15:23 Yep, I agree with you.
**Trask Stalnaker** 15:26 Yeah, because it's too much built around, like, oh, there's supposed to be a central org-level security team.
And they're supposed to then, you know, triage and delegate everything, and we just don't have that. We don't want to be the bottleneck.
**Reiley** 15:41 Yep.
**Trask Stalnaker** 15:43 Okay, yeah, I'll keep an eye on the Zapier workflow, at least, to see if, because I've… I had worked on that originally with the, Wow, who was Carter, I think, originally.
So I have some background on that workflow anyways.
**Reiley** 16:05 I don'.
**Trask Stalnaker** 16:06 No idea it was not running, so… That's not great.
Alright, Let's see… Anything else?
**Jeremy Corley** 16:27 I, I had one… Yeah, I had one question. So, an email came in on our security alias about the bug bounty, and I was just going to respond back to it, letting them know that, as far as I know, the only CNCF project that has a bug bounty is Kubernetes.
But, when I went into the… the security group link, and tried to respond. It said I didn't have permissions.
To, respond, no?
And I wasn't sure of trastophy.
**Trask Stalnaker** 17:04 I had a problem on a different one of those CNCF.
Lists replying recently as well.
Riley, I think you asked that question about the bug bounty… Yeah. To the general…
**Reiley** 17:24 Yeah, so I asked, that in the governance committee channel.
And I… I think the answer is the same as what Jeremy described.
**Jeremy Corley** 17:37 Yeah, I actually talked to somebody on the security team for Kubernetes a while back, just a lot of general questions about How they handled issues and things like that, and that actually came up.
And they were saying it's actually a big… Hassle for them, because they basically get a… A chunk of funds, and then they run out of it quickly, and then they have to scramble and, ask for more funds, and it's a whole… deal,
**Reiley** 18:03 That's pretty involved. Yeah. So this is… I share a link in the chat, this is what I use to do my own search, and… I got the same result as you, and also from… from my discussion with the GC channel, I think folks confirmed the same.
So, Jeremy, I'm okay if you go ahead and reply to that email thread.
**Trask Stalnaker** 18:30 Yeah, but he can't. There's some technical… Oh, so that one is a Google group, great. So this one we can fix.
Let's see what… Problem is… oh, that's the calendar.
Group security… Wait, why can't I find… Is security at… it's security at OpenTelemetry I.O, right?
**Jeremy Corley** 19:05 Yeah.
**Reiley** 19:06 Yes.
When I came back from vacation, I saw probably 5 emails. Most of them, like, were, like, trying to sell something, or trying to do a cross-promotion for ICO, just, like, junk email.
But…
**Trask Stalnaker** 19:24 Oh yeah, I have the email, it's the group, it's the… The Google Group.
I can't find the Google group!
Doesn't make any sense.
**Reiley** 19:42 Maybe a bug. Try later today.
**Trask Stalnaker** 19:48 Yeah… J… Oh, good… Okay, well, yeah… oh! Oh, I got into it.
the group… My groups… Security… No.
That is… A… Weird one… Okay, I will work on figuring out what Where… what's the problem there, and why you can't reply? Because you should be able to.
**Jeremy Corley** 20:41 Great.
**Trask Stalnaker** 20:44 Oh, I had put something on the agenda… I'd forgotten… We had a question in the Java instrumentation repo… Asking about penetration testing… And… so I had opened a issue in, B… SIG security just for… Any kind of general guidance on… so they want to receive a comprehensive vulnerability assessment and penetration test for the OpenTelemetry Java agent and the collector. I had replied about the collector, since we have that.
But we don't have… Or the Java agent.
I… Assume is just… we're fine with just saying, no, we don't have it.
I don't know if there's any… Yeah, because as far as I understand, this requires, essentially, hiring, security… firm.
**Jeremy Corley** 22:07 Generally, that's my understanding.
**Reiley** 22:12 Yep.
I'm curious, because previously we worked with some companies in UK, I believe, to do the fast testing for a collector.
And I wonder if OpenTelemetry would be, like, as a community, we would be interested in saying, hey, if you're running a company, and you want to help us here.
then we're happy to put your name. Like, you're a third-party, independent company helping us to do this type of penetration, whatever test.
So you, like, we'll list your name, and we'll give you credit, but in return.
we have some expectation from you, like, you have to publish the results and things like that. You have to come and help.
**Trask Stalnaker** 23:00 Yeah. Yeah, it's probably worth… I can open a CNCF.
Ticket, just to see if they've got… They're aware of what people have done before.
**Reiley** 23:17 Yeah, that company from the UK, they were introduced to me by some other CNCF projects.
like, when they… when they came to OpenTele, I'm just saying, we're… we're willing to help.
the OpenTelemetry Collector Fast Testing, we have already done a similar thing for at least two other OpenCNCF projects.
**Trask Stalnaker** 23:42 Do you know if the CNCF hired them?
**Reiley** 23:48 I don't know for sure, but it seems they're doing that for free.
I guess the collaboration is they want to, like, make their product more readable.
**Trask Stalnaker** 24:01 Yeah.
**Reiley** 24:01 Everyone, and they're doing this for free, and once they find all the things, they're willing to work with us to follow the process, but in the end, we won't tell people we actually have this important product, and we identify all these issues.
**Trask Stalnaker** 24:16 Okay.
Cool.
Yeah, yeah, I'll follow up on that.
Cause… Elliot, we can point to, hey, we have user demand for such a thing, so it could be valuable.
**Reiley** 24:31 Yup.
**Trask Stalnaker** 24:34 Alright.
I think we're good, Ben. Anything else?
**Jeremy Corley** 24:44 I didn't have anything else.
**Trask Stalnaker** 24:47 Alright.
Thank y'all.
**Reiley** 24:51 Thank you, also, bye.
