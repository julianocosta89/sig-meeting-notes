SIG: .NET Auto-Instr SIG
Date: 2026-05-13
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 07:20 Hello, everyone.
I think the most folks are… looks like most folks are oof this week.
And I'm also driving.
present or drive the meeting today. Probably we can wait for, one or two minutes and see if anyone joins. If not, we could drop and join next week for the updates.
I think it's already 5 minutes over, I think we could drop off.
Instead of wasting our time here. Thanks, everyone.
**Matthew Hensley / Grafana Labs** 08:46 Thanks.
**Zach Montoya** 08:58 Hey, sorry for being late.
**Rajkumar Rangaraj** 09:05 Hey, Jack, I just was speaking and saying, like, there is no other maintenance, and I'm also driving.
That's why I said I couldn't share and drive things out. We were about to drop, and you join. I don't know whether you want to drive today's session, or… Or we can just check if there is an agenda.
We can just try to cover that, too.
**Zach Montoya** 09:30 I mean, I'm happy to have fewer meetings today. I've got so many, so…
**Rajkumar Rangaraj** 09:35 Okay, cool, then I think we'll call off this meeting and then meet next week.
**Zach Montoya** 09:41 Okay.
**ikisel** 09:41 There is… there is one small thing that I'd really like to… Took a boat.
So, we have one, pull… so the one trivial pull request that I identified previous week, we have a bug, that just to clean up something, we get a pull request.
Maybe I'm over-suspicious, but… I don't like something in the pattern, because there is a lot of push in a pull… in a bug that, please assign it to me, then a pull request, please do a review, then after it, please do a review again, then some, strange answer to my commands that, please do a review again, and… I looked in the profile of a user.
And I see there are tons of, trivial pull requests.
all in different repositories, so it doesn't match for me any… so it may be… I'm maybe over-suspicious, but I'm a little bit worried, maybe it's some, type of attack that a user tried to get a first trivial pull request, and then get an access, to automatic CI, something like that, so I'd really like, somebody to make sure that we are talking with a real and what it is behind. Maybe just some university course, and it is expected that they know how to do pull requests in open source repository, and that's why they do it.
So… It's once again, right now, just a gut feeling, but…
**Zach Montoya** 11:17 Which…
**ikisel** 11:19 which pool…
**Zach Montoya** 11:20 Where are you?
**ikisel** 11:21 It is, 5061.
**Zach Montoya** 11:26 That was successful.
**ikisel** 11:28 Cloud Architect Emma.
**Zach Montoya** 11:33 Cloud Architect Emma, this very much sounds like an agent persona.
**ikisel** 11:38 Yeah, but the agent personas that have a biography, resume on the side, but everything looks very template-based, so it really sounds… it really, for me, it right now feels as AI person that tried to mock a real person.
And when I see something like that, I'd like to flag it, and we already have some pull requests in other hotel repositories already approved, so I'd really like us to do something with it, or maybe I'm over-suspicious.
**Zach Montoya** 12:12 Hmm. Yeah, no, I think your suspicion is warranted, for sure.
**ikisel** 12:19 So, mass and bet right now with a pair. PR is good, it can be approved, but…
**Zach Montoya** 12:31 Yeah, I think we can be just… Vigilant on just… Making sure that we… carefully review the PRs. I mean, if this one about the NuGet version suffix, if that is legitimate, then… I don't see reason to not, but…
**ikisel** 12:56 For example, right now, the last comment was, you see, a discussion with me was, what's the reason for this change?
issue with single quote. The response, totally irrelevant. Okay, can you explain the response? How the change, re-released was accidental. I've reverted it. It's not reverted. Yet.
**Zach Montoya** 13:20 Yeah.
**ikisel** 13:21 So, it's not much prefer, so… Right now, my advice would be, for now, to… I don't know what to do with, but…
**Zach Montoya** 13:37 Okay.
**ikisel** 13:44 Steven.
**Zach Montoya** 13:46 Yeah, that's really odd.
Hmm.
Well, I can look into this further, but yeah, I guess… Yeah, it's probably good to just, We'll keep an eye on this.
**ikisel** 14:08 The same I looked into the other thing, because there is, in another, repository, something like, there is a removal of one, end of one end of line, there was double end of line in docs, and reference that, it will help for that ticket, and also of original tickets. No, it would not help.
But it was merged, so that's why… Right.
**Zach Montoya** 14:34 They submitted a PR to remove one blank line in open telemetry CPP. That's really funny.
**ikisel** 14:42 Yes, yes, yes.
**Zach Montoya** 14:45 Interesting. Okay.
**Rhynier** 14:48 Yeah, no, to me that… from some of the articles I've read about actual attacks that have happened in the last few years, supply chain attacks, that sounds very suspicious. It's like they're trying to build a resume.
And so somewhere in 6 months from now, they submit a big PR, and the person looking sees, oh, this person is very, very active. They've got a lot of PRs that got merged. Not realizing that they're all small little ones that That we all wondered why were they doing those things. But then comes the bigger ones.
**ikisel** 15:30 Nope.
Probably, in that case, we should just be a little bit more formal, and the requirements for hotel contribution is that the person should be registered in Slack.
We try to op… connect with them in Slack, and advise to talk with… in pull requests that we'd like to speak with a person on Slack to understand what's the reason behind the pattern, so why so many different pull requests, or if there is any negative thing or not.
Because it's in our rules that every person contributing should be on.
like…
**Zach Montoya** 16:15 Yeah, that might be… a good way forward. What do we have in our… Contributing… Conduents… We reference the Edwin Sanitary Code of Conduct… Oh, no.
Yeah, I haven't encountered this before, so I'm actually… I'm not sure either about what the… What we should do about this one.
**ikisel** 16:51 contribute.
**Zach Montoya** 16:54 Yeah, we have some additional maintainers, maybe we can… Chat about this morning's week.
**ikisel** 16:59 Yes, there is… please read OpenTelemetry new contributor guides and code of conduct, and OpenTelemetry is the prerequisite. Before you submit a code, you'll need to have a few things up. Create a GitHub account, sign a SLA, Code of Conduct Community.
Maybe not.
I'm not sure about.
I believe I have seen somewhere, that's why I'm on Slack.
**Zach Montoya** 17:34 Yeah, I think I'm happy to get some other input, so this… we could talk about this next week when we have some more… more voices in here.
**ikisel** 17:49 So… That's all on my side. Critical on my side, finished tip. I still would like somebody to take a look on Trump Alliance thing, but it's less critical and can wait.
**Zach Montoya** 18:10 Oh, the trampoline, yeah, yeah.
**ikisel** 18:11 Once again, not a review right now, but just, I have not done a full review myself, but just an idea-level thing, if it's something that can work or not.
**Zach Montoya** 18:23 Gotcha. Okay.
I can take a look later this week.
Cool. Anything else to chat about today?
**ikisel** 18:40 And last thing, there was, lots of bugs, previously that talked about, assembly redirection not work, with a failure to load assembly, so per my test, per my investigation, we finally resolved after all that after changing to different .NET versions, after changing to a secondary app domain workaround, I believe we finally resolved all of them. I commented on all of them that I believe they can be closed, and I referenced my ones that I created and closed. So I have not closed them, but Probably we should.
Or at least say that we believe that it is closed, and if it is not, please reopen it.
**Zach Montoya** 19:32 Yeah, yeah, what we can do on those is, if they, Yeah, you've already commented on them, and then after, like, if it goes stale, then we can just close, and then…
**ikisel** 19:43 Probably in a week.
**Zach Montoya** 19:45 Yeah.
Boom.
**ikisel** 19:53 Because, like…
**Zach Montoya** 19:55 Alright, well, that's everyone. I'll see you guys next week.
