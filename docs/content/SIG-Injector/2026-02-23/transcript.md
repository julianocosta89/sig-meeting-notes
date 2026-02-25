SIG: SIG Injector
Date: 2026-02-23
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/5fdH2eJd03Zk4UGnBh4lzV6vbgUbGQzuhaXnbXkgqRYCwDmo50QOeMAO5SW4tCjV.1xyGZ0GA6aF0k3J4
============================================================

## Zoom Recording Transcript

Bastian Krol 00:00:58 Amen.
How's it going?
atoulme 00:01:01 Hey.
How are you?
Bastian Krol 00:01:04 I'm fine.
atoulme 00:01:07 I'm okay.
22… Yeah.
It's like we're… What's the agenda today?
Bastian Krol 00:01:19 A lot of ellipses so far.
atoulme 00:01:24 Okay.
Oh yeah, I can see it.
Yep.
Hey, everybody.
Okay, so… Let's dive in.
Nikola, you want to start?
Isn't even?
Wow, Nikola's not here. Okay, and you can just go to PR Open, I can share my screen.
Okay, so, what is this issue?
240…
Bastian Krol 00:02:22 No, that's… So…
atoulme 00:02:24 Oh yeah, okay.
Bastian Krol 00:02:28 I think the issue,
combines a couple of things into one. It should probably be more two or three issues. Nikola worked on one. Actually, I'm not sure…
why I didn't merge it? Because this PR has 3 approving reviews. What more can you… can you want from a… from a PR?
atoulme 00:02:57 D?
Bastian Krol 00:02:59 I can…
atoulme 00:03:01 He… maybe, he's waiting for me to approve.
Bastian Krol 00:03:07 Yeah, that's actually a good segue into, I mean, we can just merge it. Apparently, she wants to merge it, so we can just do that. But that leads me a little bit into my next question already. I mean, you can also take a look and review it and approve it later if you want to.
What is our consensus on when we merge
PRs, especially merged by PRs from maintainers, so I usually look for one or maybe two reviews, and then I just merge my own PRs. Other people seem to wait for
I don't know. Other maintainers to merge and not merge their own PRs? Is there some… how do you folks usually…
handle that, because every project, I feel, does that a little different.
atoulme 00:04:04 Yep.
Do we have a policy?
jea 00:04:06 We're good.
atoulme 00:04:08 Sorry, yep, that's it. That's what I had.
jea 00:04:12 I was gonna say, like, for operator, it's usually dependency updates, one maintainer.
For code changes, we aim for two, if it's, like, more than a few…
files, like, if it's anything close to interesting, but if it's… like, over the weekend, we had a mass… a huge amount of,
just, like, linter fixes. And for those, it's just, like, you know…
Doesn't really matter. That's one main thing, but kind of anything more, I think, makes sense for two.
Just to be safe. I don't know if we've been waiting on it. I try not to… I try not to merge other people's PRs if it's, like, a maintainer making it, though, but that's more my own,
Bastian Krol 00:04:57 It's also how I feel that people merge their own PRs, except if it's a contributor that cannot merge, of course, that's different, but… yeah, so…
That sounds good to me. Nicola, we were just, discussing… you asked for whether we can merge your latest PR, I think it…
is so ready to merge since… since days. And my question around that was, just to summarize, because you… a couple people joined later, how do we handle
merges… how many approvals do we want, and do people usually merge their own PRs, or do other people merge their PRs? Just to summarize that question.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:39 Yeah, but I don't have merge rights, so…
Bastian Krol 00:05:41 You don't… we, what, you maintain… became maintainer recently, you don't… still don't have merch rights?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:48 I'm only on the approver list, so I couldn't hit the button.
atoulme 00:05:51 Oh…
Bastian Krol 00:05:51 Oh, I thought you were waiting for something, and…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:56 No.
Bastian Krol 00:05:57 Good that we talked about it!
atoulme 00:05:59 Okay, let me see what we can do there.
Bastian Krol 00:06:01 But, I mean, Jack as well as Nikola became maintainer, or should have become maintainers, that at least was what we…
Michele Mancioppi 00:06:10 The most IPR.
atoulme 00:06:11 it by hand.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:06:13 Yeah, but I would, yeah, we didn't get the…
I assume that it was discussed maybe somewhere else that we are not getting merged right? So, yeah.
Jack Berg 00:06:22 No, no.
The standard for maintainers is merge rights, so that's not like a repo-level decision. That's a project organization decision.
Bastian Krol 00:06:30 Yeah, we probably just…
jea 00:06:32 Yeah, we need to update the admin repo.
Bastian Krol 00:06:35 Yeah, we need to update the team in that Terraform… Things?
atoulme 00:06:39 The tofoil.
Bastian Krol 00:06:40 I said, oh, how does that work?
atoulme 00:06:43 Wait, is that telephone now, or is it, you, you got me…
Bastian Krol 00:06:48 Or is it, is it just.
Jack Berg 00:06:53 Yeah, I don't think Terraform member, manages team membership. I think that that is managed by whoever the maintainers are for the maintainer team.
Bastian Krol 00:07:03 Oh, everyone is… is maintainer of the team, except for me. Did we… we had that same discussion with the other… I see we had that discussion before with the maintainer… team maintainer role.
atoulme 00:07:19 Dinner now, sorry.
Bastian Krol 00:07:21 No, that's fine, I just had a deja vu, I thought we…
atoulme 00:07:26 It's…
Bastian Krol 00:07:26 discussed that before, and also edit maintainers there? Am I…
Michele Mancioppi 00:07:30 I don't have…
I also do not have the possibility to change team stuff in the project. What's going on?
Bastian Krol 00:07:37 You are a teaming…
atoulme 00:07:40 Let me share my screen so we can see the same thing together, right? So, we're looking at this particular under…
Bastian Krol 00:07:45 Yeah.
atoulme 00:07:46 Between you have teams, injector approvers, injector maintainers.
Bastian Krol 00:07:49 I think so. I didn't realize that maintainers is a child team of approvers, because I think we had the very same discussion for the parent team of what we are looking at right now, the injector approvers. If you click one level up, there everybody is there, and we probably confused that with…
atoulme 00:08:08 Oh, because of the maintainer little button here? Yeah.
Bastian Krol 00:08:10 Yeah, we probably thought, okay, that is enough to add Nikola and.
atoulme 00:08:16 Jack, to the maintainers, but we actually only added you to approve us.
Hopefully that helps.
And also, I'll make Nikola.
jea 00:08:26 I can add Jack right now.
atoulme 00:08:29 Oh yeah, fair enough.
Sorry.
jea 00:08:33 Yeah, we had, when we were doing the, like, info work to bring over all the stuff into Terraform Management, we were considering doing all of the team membership there, but we realized that it would actually become…
way more annoying to do it in, Terraform than it would have been to do it just in, like, GitHub, because then otherwise you have, like, a bunch of people that need to press a bunch of buttons and get PRs merged, which is really frustrating for doing membership stuff.
atoulme 00:09:01 Cool.
Jack Berg 00:09:03 There's another bit, so there's, like, a link I posted in the chat, which is, like, instructions on how to set up new repos, and it just gives some… some guidance, or not guidance, these are instructions about, like, team memberships. And so, like, one of the things that I think, that I remember being sort of unintuitive is that even though the maintainer team is a child team of improvers.
You still have to explicitly add every maintainer to both maintainers and approvers, so that's, like, kind of a snag to be aware of. And same thing with triagers as well, so,
Yeah, just be aware of that.
Bastian Krol 00:09:37 I guess if you're in the child team, you're automatically also in the parent team, but not the other way around. Isn't that how GitHub teams work? But… maybe I'm misremembering that.
Jack Berg 00:09:48 There's some sort of… there's some sort of gotcha in there, where you have to, like, even though you're an approver through your membership and maintainers, you're supposed to be added to both.
Bastian Krol 00:09:57 Hmm.
Jack Berg 00:09:58 Maybe it's something like, like, because if you transition from a maintainer to an approver.
It's like, you'll lose that maintainer role, and then you'll also lose approver role, so maybe it's just, like, a sort of belts and suspenders approach to make sure that we're less error-prone.
I don't know.
Bastian Krol 00:10:17 Yeah, thanks for that link.
Okay, that clears up a lot of, confusion.
atoulme 00:10:25 Yeah, sorry about that.
Jack Berg 00:10:28 It just, you know, while we're on this topic of merging PRs, I think all of us are, you know, maintainers in different repos around this organization. Each repo develops its own sort of culture, its own habits. In the Java repos that I'm part of, we don't have enough maintainers to, like.
get two approvals on everything, things would just, like, sit stagnant forever. So we… we sort of have an informal policy that is, like, what everybody would expect, where it's, like, you, you… you have, like, a sort of waiting period and a scrutiny level that is proportional to, like, the impact and the risk of the PR. So if you're making, changes to the public API surface area that are one-way doors.
You know, we let those sit for longer so that people that may not see them have a longer window to object. And if you're doing something particularly impactful, you know, one thing you can do is just, like, you can explicitly call out the approvers and be like, hey, like, my plan is to merge this on date N in the future. If you want to object, please, please say something before then.
So, just like, those are a couple of strategies that I've seen work. But yeah, I think we kind of have to
There's nothing to pose.
Michele Mancioppi 00:11:42 Say now, or hold your peace forever.
Jack Berg 00:11:45 Something like that, but, like, with a couple of days, right? And that kind of works in the spec repo as well. Like, you know, there's a lot of balls in flight, everybody doesn't see everything, and, you know, we want to assume the best intentions, but we also want to keep things moving along, so different things that we have to balance.
Michele Mancioppi 00:12:02 No, I feel that so far, I mean, we're not having an issue with the speed of getting stuff reviewed.
Jack Berg 00:12:10 Yeah.
atoulme 00:12:12 It's been good, I mean, I have no complaints whatsoever on this project, and if… I know you're not shy about pushing, on Slack if you need something reviewed, so continue to do that. Yeah. If you need to. Yeah.
In some cases, for the collector, maybe one thing we do is that in the PR description, we actually set the expectation of how many people we want to review a PR, if it's going to be contentious.
But all of this is just destroyed.
Bastian Krol 00:12:37 That's good.
atoulme 00:12:37 There's… so if you want to have a hard and fast rules about, like, okay, you know, an approach we can take, which will happen maybe down the road if we start to have too much stuff to review, is you can have code owners or some portion of the code that are going to be assigned to maybe a subset of people.
And these are people who need to kind of be the gatekeepers of that code, and we do that in the collector around some of the contrib components.
Bastian Krol 00:13:03 Hmm, but it's so much bigger.
atoulme 00:13:05 Yeah, I mean, and for that one, for example, to pick an example, like, anything related to log collection is so complex, and so much domain on its own, and we have a set of people who have, like, have volunteered to be responsible for that.
hopefully nothing like that happens. Maybe down the road we could make some of the .NET teams also approvers, reviewers of some of the changes for .NET, and same for Python and whatnot, but you're…
We're not there.
Michele Mancioppi 00:13:33 Speaking of that, I think I'm a bit slow in setting up the system packages thing, because that is actually what should happen there with,
With a sake for that.
Because…
atoulme 00:13:46 To be right. Yeah.
That is the better one for it.
Michele Mancioppi 00:13:50 I just have not had the time to set it up yet.
atoulme 00:13:54 Yep.
Michele Mancioppi 00:13:56 By the way, Ted, I'm sure I have you here.
Where do we stand in terms…
of the project for the system packages. I mean, there is to find the liaisons for the languages, yes.
Is there any other… thing that is blocking the, let's say…
Ted Young 00:14:15 I think just staffing, like, I can hook us up with, you know, language liaisons, but there has to be people committing to actually doing the.
Michele Mancioppi 00:14:24 We have a bunch of them.
Ted Young 00:14:25 Okay, just getting that… getting the project file updated to who's agreeing to do what.
Michele Mancioppi 00:14:31 It has… it has been with that, but people literally signed themselves up to that. I was just merging the commits and the.
Ted Young 00:14:37 I feel like I just looked at it, and I didn't see that section filled out, but I'll look again.
Michele Mancioppi 00:14:43 Let me, let me check it live.
Ted Young 00:14:48 But at any rate, if we've got people, ready to… to go to work, I think we can just make it happen.
We have to get a TC sponsor, but I think that's sort of…
Michele Mancioppi 00:15:02 Here.
Ted Young 00:15:05 Okay, great.
Michele Mancioppi 00:15:10 There's also a nice representation across multiple vendors.
It's better than I thought.
Ted Young 00:15:15 Yeah.
Jack Berg 00:15:16 It's still a little bit light on the instrumentation side. There's.
Michele Mancioppi 00:15:20 Yeah, that is where we need the liaisons, yes.
Ted Young 00:15:23 Yep.
Jack Berg 00:15:26 Yeah, so just to kind of clue you in, or key you all in on some of these conversations that are emerging or happening in the TC and in GC, somewhat together, somewhat different. Sometimes we talk to each other, but, like, they're different groups that have their own opinions. And so, at the TC level, there's this idea of
for each project, like, a sponsorship level, and so there's 3 levels of sponsorship, of increasing engagement. There's escalating, which is the lowest, which is just like, hey, go do your thing and let us know if you have any problems. And then there's, like, guiding, which is, you know.
playing a bigger role, but still relying on other people to do most of the work. And then, the highest level of engagement is leading, where you're actively leading the project.
So, like, I would… just to, like, you know, I'm in a leading capacity for the configuration SIG, and I'm in an escalating capacity for, like, the Android SIG.
For example.
And, you know, there's limits in place on how many, guiding and leading sponsorships a TC member can have at the same time, because that's just what we found. There's practical limits on where people can actually be effective, and if they spread themselves too thin, they're not actually doing the job.
And so, the TC is having conversations about, like, hey, what level of, engagement, what level of sponsorship do we think is necessary for SIG-like packages to be successful?
And that's sort of a subjective conversation. But, you know, based on that answer, is there anybody available that has that type of capacity?
Given what… given what they're working on already. So, it's… there haven't been any comments on this PR in the community repo related to, like, like, people stepping up and volunteering, but there are a lot of conversations happening in the background about, like, you know, just what level of sponsorship is required, and who might… who might have capacity.
Michele Mancioppi 00:17:31 Oh, the answer is we don't know yet who has capacity, right?
That's… that's my takeaway is this sponsorship is not closer.
Or did I misunderstand?
Jack Berg 00:17:45 So…
Yeah, we don't know who has capacity. It's like a combination of capacity and interest, because you can't force people to do things. So, those are the two factors.
Ted Young 00:17:59 Yep.
I mean, I think there's a parallel conversation that has to happen around
OpenTelemetry getting a little more organized at the top, in that we have kind of a new set of goals we're running at, and we haven't quite figured out.
how to communicate them all, and I feel like…
what the work we're doing here is kind of in the middle of that, right? We're trying to say, like, hey, across all of the languages, the new goals are to, like, be configurable, and, like, be installable through these new system packages, and also, like, be stable, and have all of your instrumentation and stuff updated.
we haven't quite figured out how to organize all of that new stuff across OpenTelemetry, so I think that's the other thing.
Right. There's, like, how, you know, how much attention does this SIG need from the TC? I would say the answer is little, because it's a very strong SIG, but how much should the TC be paying attention to this stuff as part of, like, we're trying to be organized about rolling this stuff out, and so, like…
the TC should probably be involved and, like, aware of what's going on over here.
Michele Mancioppi 00:19:11 I truly would argue that, despite, I mean, it's nice to hear that
The sake is good for good, but it has such wide-reaching implications for the rest of the ecosystem that it deserves, actually.
Exactly. And to liaison to the outside, and pushing it, and make sure that it's aligned everywhere, so yeah.
Ted Young 00:19:34 Yeah. There's, like, what…
Jack Berg 00:19:36 Those seem to be where the TC conversations are going as well, Mikael, is that, like, yeah, this does not just require an escalating level of sponsorship from the TC. It's probably guiding…
Probably guiding. I don't know. Maybe leading, but probably guiding.
Ted Young 00:19:51 There's, like, what we can get away.
Michele Mancioppi 00:19:52 Do you manage to ship something nice, or is it…
Ted Young 00:19:54 what would be a good idea? And I think we could get away with a low level of involvement, but that would not be a good idea. It would be a good idea to be…
very coherent about this rollout, and do a lot of messaging to a lot of SIGs about it.
Jack Berg 00:20:10 And to integrate with, like, all the different pieces of the ecosystem, not just, like, have this be something that's being developed without, you know, in a vacuum, right? So we want all the pieces to work together, so we need to coordinate.
Ted Young 00:20:23 Yep.
Michele Mancioppi 00:20:25 But then I, I am a,
guilt feelings about being reticent and doing so many things because I was on vacation doing other stuff, they're gone.
It's all stuck on me, right?
Ted Young 00:20:39 Cool.
Well, we're gonna definitely get.
Michele Mancioppi 00:20:42 Next question. Next question.
It is completely obscure to me what happens very often in TC and GC.
To the extent where I was entirely unaware if and how this was being discussed until you spoke about it.
How can I fix my ignorance?
Ted Young 00:20:59 There's.
Jack Berg 00:21:00 Go ahead, Ted.
Ted Young 00:21:03 Well, I was gonna say, this is on us to improve. This is, again, just getting into, like, TCGC biz. I feel like…
we have projects, right? And we've been working on, like, how those should work, and I'm pretty happy with, like.
Like, how they should work, but in terms of the actual process of…
setting up process projects and also taking donations, I feel like, on our side, we are not vocal and proactive enough
When people show up about, kind of.
right there in the moment, explaining what the process is, what the next step is. We tend to, I think, under-communicate.
And that leaves the people who are, like, trying to start the project, or trying to get the donation done, feeling a little bit like, unless I, like.
poke somebody that I happen to know, it's hard to… to know what the…
next step is, or, like, where this thing is in some process. I think that's actually something we have to improve.
result.
Michele Mancioppi 00:22:14 Does that mean that, when the TC figures out the sponsorship, then,
I get pinged on SenseiFlack, or how does it work?
Ted Young 00:22:26 We would want that all to continue through GitHub, ideally, right? But I think there should be more communication going on on that project PR from us, saying… saying these things.
Right. Like, we're telling you these things in the SIG meeting, because you're talking with us, and we're kind of involved.
But it feels like that's… that's a little bit like happenstance, right? Like… like, when people aren't totally connected up, then it becomes even more of a vacuum. So I think this is just… we don't have enough of a process in place around…
You know, explaining this to people.
On the PRs.
Jack, you might have a different take on it.
Jack Berg 00:23:09 Just, just two additions. So one, there's,
the TC used to have private meetings. Its meetings are public now, so, you can always go watch the recording and look at the notes. That wasn't available in the past, so there is a little bit of transparency. It takes, like, it takes more effort to consume, but you can at least know what conversations are happening.
And then the other thing is that, like, on the upfront communications,
a point that I've been making, and I don't necessarily speak for, like, the whole GTC right now, this is just my opinion, is that, like, we need to do a better job of managing expectations.
people come in and open an issue to, like, start a new project, or to, like, donate some big chunk of code, and, you know, are, like, left, like, wondering what the status is. Well, the status is, is that everybody has a lot of work that they're working on, and stealing their attention for 20 hours is, like, a big ask, and so, like, I think, like, one thing in the case of, like, a donation, in the case of, like, going to sponsor a new SIG, it could either be, like, less than 20
hours, or, like.
a lot more. So, there's, like, like a people kind of temporal coordination problem that's happening, and,
My, my two cents is, like,
We should kind of go into these types of things with, like, lower expectations around how fast they'll… they'll kind of,
reach… Reach, like, a decision.
So…
Yeah, like, you know, we talk about sometimes whether we should build things inside of OpenTelemetry or outside of OpenTelemetry, and when or why one is appropriate, and like, you know.
Just, like, as an anecdote, I like building things outside of OpenTelemetry because you don't have to deal with this governance.
But, like, you know, this packaging type of work is the type of thing that, you know, it'd be nice to go fast outside of the governance, but it really is, like, fundamentally a coordination between different groups that are within the governance model, so it kind of has to be within OTEL.
So… We pay the governance tax.
Ted Young 00:25:20 Yeah.
Michele Mancioppi 00:25:22 I mean, despite all the bureaucracy and how slow it works, I think this project
Needs to be done in the most official, sanctioned way, with as much
Driving power and influence on the other six, because…
It's a linchpin project. Without that, it doesn't work.
Jack Berg 00:25:43 Yep.
Ted Young 00:25:45 And it's a… it's an integrated project. I think when people tell us to go faster by letting people be more independent, they tend to be looking at it like it's the CNCF or something. Someone can just start a SIG and…
they're… the work they're doing is, like, totally independent from what everyone else is doing. But we find that usually, when we go into a new domain, the experts there aren't used to thinking about
you know, how does, like, browser observability integrate with tracing so that it can integrate with server-side observability? Like…
it…
you want to have some high touch, especially when you're standing these projects up. Like, like, they just thrive a lot more if we're giving them tender, loving care when they get started, versus just being like, go off and have fun.
I think it's that integrated nature that makes it important.
But we've just kind of… we're just at a stage where we've run out of, like, our original roadmap was, like, tracing metrics logs, and so we're kind of, like, at the end of that roadmap. So we just need to reboot a little bit around, like.
How do we…
if we do a list of, like, what is OpenTelemetry up to, it's, like, 40 things. That's, like, you can't be like, here's the 40 things we're up to. There needs to be a way to, like.
have a more concentrated set of focus. And the stuff we're doing in this SIG is, like, really related to that effort.
So…
Hopefully, we'll have something stood up that feels better, but we definitely want feedback from you all the time about
does that messaging feel like it's landing? Do these processes feel like…
Whether they're fast or slow, do they at least feel like they make sense, and you're being told about what state they're in?
Michele Mancioppi 00:27:35 I can tell you that if you had not been holding me in writing project files and stuff, I would have never figured it out.
Ted Young 00:27:42 Exactly. So… Getting that stood up, I think that's something…
I want to see the GC and TC kind of work on over the next couple of months.
Jack Berg 00:28:09 Back to the… Meeting agenda?
Bastian Krol 00:28:12 Yeah, we can.
I have just one quick update, we…
fiddled around a lot with the release, lately, and just wants to give a quick update where we stand with that. So,
I think we need… so we… the last thing that I tried to do was… was using this,
Autobot GitHub application to do the one step of the release that needs to be done by something with more permissions than the normal token. The Autobot app does not have permissions to push tags, so,
That's why we need, an app with more permissions, there's a process for that. I opened the PR,
Around that, just posted it to the… to the chat here, and I guess we'll just need to wait, until we get a response.
there, there are, like, it's a community repo, so there are a lot of open PRs, so I assume it will take a while until some poor soul gets… gets to that and… and can…
set this up. But, yeah, we don't have a…
release plan immediately. I mean, we… now that Nikola merged this PR, we could make a release, if it's release-worthy, but yeah, I guess in the meantime, we have a workaround, we just need to push to that… push the tag manually, and so we are good on that front.
Jack Berg 00:29:57 just trying to remember what we do in the Java repo with this, like,
I guess, what, what repo did you look at, as, like, prior art?
Bastian Krol 00:30:09 I… don't know. I took the release process that Antoine had set up initially, I think, and then just extended it with a bit more automation without taking any specific existing repository as
as a blueprint, I just thought at the time it was a good idea to create the tag automatically that would then also trigger the rest of the release process. If somebody has other ideas that do not require,
these… or us jumping through these dupes, that's also fine. I'm… I'm not…
Emotionally married to that specific release process.
Jack Berg 00:30:54 Right, right. I'm just asking because, so, like, what are the fundamental things we have to do during the release? We probably have to, push some commits and open PRs against them, maybe to update, like, versions in README or something like that.
Bastian Krol 00:31:07 Yeah, so there's one GitHub action that triggers the changelog update, which is automated via Chlogin, or how the tool is pronounced.
And, that needs to be approved by a human, and then from there, it should all be… be hap… should all be happening automatically. It doesn't because of this technical…
issues with the tech creation, that, that. And I think somebody, I think it was Antoine who mentioned that in the collector or collector country repo, the tech is pushed by a human…
atoulme 00:31:44 being, so that's where… where that's different. So with Go, you have to push…
Not just one tag, but one tag per folder per module. So you just end up machine 200 and some tags from your machine.
That's, that's what it is.
Bastian Krol 00:32:00 It doesn't sound like a good argument to make it on a local machine and not automated, but that's not me.
atoulme 00:32:06 You're right there.
there's…
Bastian Krol 00:32:10 Yeah, but it is what it is.
atoulme 00:32:11 Another strong stance, I think the release should be a button, right? It needs to be as simple as it gets.
Due.
Bastian Krol 00:32:19 Yeah, yeah.
atoulme 00:32:22 Yeah, I don't have any strong… like, I pretty much copied what we had in the collector for this, so that we could prepare the release at first.
Then we talked about having the artifacts being generated by the release, that was a separate function that we did, and now trying to make all of this work in one step seems to be having permission issues. So if you have an open issue for that, let's start with Trask and see where we go.
Bastian Krol 00:32:45 Yeah, I think… I think it's fine. I really don't want to be pushy on that community repo, because they are… I think they have a lot off their plate, so I just opened the issue for now, and…
Let it sit for a while, and then maybe…
You know, in 2 or 3 weeks, we can… we can ask nicely.
If somebody can take care of that.
atoulme 00:33:08 Yeah.
Jack Berg 00:33:09 So, just… so we have to do all the same types of things in this repo. We have to create the actual release artifacts, we have to, create tags, we have to push commits and open PRs against those commits, and in the OpenTelemetry Java repos.
Bastian Krol 00:33:25 Yeah.
Jack Berg 00:33:26 of them, and I don't think that we have
A special user to do an.
Bastian Krol 00:33:31 I think… I think you have, if I'm… so I looked through the community repo for a blueprint for that issue to have a, special, GitHub app, and I…
Deem to remember that…
There's one for Java as well, because I saw that, but I could be misremembering that.
Jack Berg 00:33:50 I'm just…
Bastian Krol 00:33:51 What's for pushing.
Jack Berg 00:33:53 I'm just looking through, like, the build, the GitHub Action, you know, YAML files right now, and the secrets, and I just don't see any secrets.
atoulme 00:34:02 It's not that hotel boot itself has an application scope or something.
Bastian Krol 00:34:08 You are looking through the, Java repo, or through our repo?
Jack Berg 00:34:13 the Java repos, and I'm looking for, like, some sign that we're using a different account, a different secret, something like that.
Bastian Krol 00:34:22 Yeah, I think it is a specific, let me look that up, it is a specific GitHub action that,
connect everything to that GitHub app?
It would be the Create GitHub App Token… let me share my screen, actually.
Jack Berg 00:34:43 Yeah, yeah, yeah, I'm looking at that right now, yeah.
Bastian Krol 00:34:50 Oh, that's cool.
I don't know if it's… So, if you have something like… like this, in the Java…
Jack Berg 00:35:05 Yeah, yeah, yeah.
Bastian Krol 00:35:06 Positive.
Jack Berg 00:35:06 exact thing.
Bastian Krol 00:35:07 Yeah, and there is… I don't know then, there's probably an Autobot app ID, and that could be either the standard organization-wide ID, or the specific one for
for Java, I guess.
Jack Berg 00:35:23 Yeah, I see.
Bastian Krol 00:35:26 Okay.
I mean, the other… the other option would probably be to give the… to give that organization-wide app, permissions to push text, but there's probably a good reason for why that app is quite restricted.
So, that's not my call.
I also didn't want to make that into a longer discussion, I just wanted to update you folks where we stand, and…
It's currently on hold.
That was the last official agenda item, at least from the Google Docs.
Any… anything else?
atoulme 00:36:18 No.
Can we merge that first PR that we started the meeting with, so we'd be done?
Is there any reason not? Oh, it's merged. It's good. Alright.
Michele Mancioppi 00:36:27 I have a question, Basti, the,
Basically, we are running, we have integrated Python?
Bastian Krol 00:36:37 Oh, good point.
Hmm.
Michele Mancioppi 00:36:39 And, we had some interesting learnings about Otelify and Python instrumentations that have not been upstreamed yet.
Maybe you want to share what you found?
Bastian Krol 00:36:51 Yeah, that's a good point. I forgot about that. I mean, I talked about that before. We are doing that over in the Zero repository, just because we can move a little bit faster there and iterate a little bit.
faster there, so I… basically, what we put together is very similar to what the opera… the OpenTelemetry operator is doing, so we have a list of Python packages that… that we bundle
Together with the other instrumentation agents, the small plot twist that we added is a user customized.
script, which was, inspired by something that Michaela did a few years back.
And, I extended that and updated it to two more recent Python versions, which…
checks for a couple of things. So it first checks, is he…
Python version doesn't have the right Python version, so very old versions we don't instrument, because it would break. Second thing we check is, is a specific…
auto… OTLP protocol set, there's an environment variable for that, and Python…
can either export gRPC or protograph over HGP, and we check if it's gRPC, then we stand down and do not instrument that one.
if someone explicitly said gRPC already, because we know then that there is a gRPC exporter in it, and that would not work together with what we do.
And the most interesting thing is probably we check for double instrumentation, so is there already some OpenTelemetry packages in the… in the Python sites?
Are those installed? Or do we have any dependency conflicts across the whole dependency tree? So, if V, for example.
Import protobuf 6, and the app wants protobuf port 4.
For whatever reason, then we also stand down, so it's…
should be pretty safe. What we have failed to do so far is to entice any of our customers to give it a try. It's currently opt-in. Most of our other stuff is opt-out, so it's just all enabled by default, but Python, we were a little bit cowards and went for
Off by default.
Michele Mancioppi 00:39:29 It's not covered in his common sense to be rightfully afraid of pipes.
Bastian Krol 00:39:33 What's, what's a,
Bit of a joke, yeah. And so, we are using it internally for one Python workflow, so that's not a…
large sample size, unfortunately, and we are looking for people to want to give it a try. That's where we are a little bit blocked now, because, yeah.
no one.
Michele Mancioppi 00:39:56 And raise the hands of.
Bastian Krol 00:39:57 pop.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:58 Bye, buddy.
Michele Mancioppi 00:39:58 Do we have any statistics about how often
Do the current packages we have get installed?
atoulme 00:40:07 Oh.
Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:09 I had a question, if you don't mind.
Bastian Krol 00:40:12 Go ahead.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:13 And you mentioned user customize,
I thought there was another on-site customizer.
Bastian Krol 00:40:19 So there's also side customers, and I don't know the difference, but maybe Michaela does.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:25 I do, and I think we should use Sitecups anyways, but…
Okay, let me…
Bastian Krol 00:40:30 about it.
Michele Mancioppi 00:40:31 when I did it the first time.
I don't know if site customize was a thing.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:37 Okay. Okay.
Michele Mancioppi 00:40:39 That was a few years back, and I never reconsidered.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:43 Right, so the reason why is that user customized does not work if anybody does buy and
So, if they enter an environment, user customized will not get picked up. There's a switch in the… in the Python inter… Oh, they're doing their own thing, no, I won't touch this. It won't pull it up. So… but site customers, they'll respect it. There is a…
If you read the spec on… I don't remember the terms, but if you read this carefully, there says, if this option is on, then site user customize does not work, and you trigger that by, say, pyenv enter environment, and that's off.
Bastian Krol 00:41:21 That is so interesting, because, I… so I, of course, also have a good bunch of tests with different Python versions, and one thing that is quite annoying is when I build one container image.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:34 all.
Bastian Krol 00:41:34 the different test cases, their dependencies get mixed up, because they all installed into the same
Python library folder, and I said, okay, I can just use, virtual ends, to separate the test cases, but then nothing, or everything stopped working, and now… now I know why, because we are using a user-customized script.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:57 Yeah, yeah, switch to site customize, and then we'll be fine.
Bastian Krol 00:42:00 Oh, that is, that is so cool, yeah, I will definitely try that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:04 And one more other thing, I also know that the Python SDK, by default, if you don't specify protocol, it will use gRPC. So, empty needs to be checked as well.
Bastian Krol 00:42:15 Yeah, we're checking for empty as well. We are in the lucky situation, our operator, that we always
Specify protocol and endpoint for the…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:25 Okay.
Bastian Krol 00:42:25 For the… that… that is…
Michele Mancioppi 00:42:27 lucky. There are painful reasons why we had to do it, Busty.
Bastian Krol 00:42:31 Yeah, yeah, but for Python specifically, that means in our…
site customized, user customized script. If we don't see the values that we know that our operator sets, we can stand down.
That is probably…
going to be a bit more complicated in the injector, because there is no operator externally that we can rely on that sets it, not always, like, but yeah, that needs to be figured out when we are.
Michele Mancioppi 00:42:59 Technically, we can do that in the site customize as well.
Bastian Krol 00:43:03 No, that's where we checked… It's…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:06 F, right? Yeah, okay.
Bastian Krol 00:43:08 And we check it by taking a look at these two environment variables, and if they are the values that we know that our own operator sets, then we continue, and if not, we stand down. So the question is, who is the one that sets them always to the same value? That's a little bit…
Michele Mancioppi 00:43:27 Budgets?
Bastian Krol 00:43:28 Maybe, maybe for later.
Michele Mancioppi 00:43:29 We are not going to have that facility to enforce the protocol at the level of the system packages.
Bastian Krol 00:43:38 Yeah, I do. That's what I'm…
Michele Mancioppi 00:43:39 You should either, because the way to configure which protocol, which endpoint, Should be the declarative format.
So, it would be perfectly fine to have Java that talks to your PC, and Python that talks HP.json in the blessed time that PR actually lands. It should be perfectly.
Bastian Krol 00:44:01 Yeah.
Michele Mancioppi 00:44:01 It's a problem.
Bastian Krol 00:44:01 The only thing that we need is we cannot allow gRPC or MT for Python, that's probably the same.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:09 Which you can check in the customized script, yeah.
Bastian Krol 00:44:12 Yeah, yeah, yeah. Yeah, maybe I'm hallucinating problems.
Michele Mancioppi 00:44:15 I mean, those exporters are separate packages. If they are there, you can find them. If they're not there, the value is invalid.
Bastian Krol 00:44:24 Something like that, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:27 I had another question, sorry, this Python's interesting, but…
because I… I was thinking about this, this is why I posted that message, like, what happens if the instrumentation is already on, and, like, if there's an SDK and whatever? But…
I thought of it harder, and…
Then I'm… I was thinking, should we just be checking to see if the exporter package is there? Because, I mean, one of the advantages of using the SDK is that I, as an end user, can go add manual spans. Like, I want to augment my application with…
like, additional stuff. All this instrumentation will just work. It will just wrap those pants, and I can actually add my business logic into the application with minimal effort as an engineer.
Michele Mancioppi 00:45:11 the SDK for that?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:45:13 Yeah, but then if I use the SDK, then when you think about it, I need to set up my exporter. I need to set up what my endpoints are, I need to do all these things, and I'm already setting it up externally, let's say, through some operator, and I've already configured that, now I have to teach my application developers how to configure those exporters.
I would like just to use the SDK to add manual spans. We did this in Go.
Michele Mancioppi 00:45:37 You don't need to use the SDK for that. You use the API package.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:45:41 Right, right, but I'm… hotel SDK API package, whatever, right? I'm considering the Python Bear API, the SDK for the API, but not the exporter. So, if we check for any open telemetry dependency, that may be too restrictive.
Bastian Krol 00:45:56 Yeah, that's… that's… that's true, and… but that very much depends on the runtime in question. So from my…
time of doing a lot of custom Java instrumentation, but that was before OpenTelemetry, I remember. So, in Node, it works very differently. Each module can have their own dependencies, and you can have the same dependency a lot of times, and then you need to be very careful that you don't have two separate instances of the OpenTelemetry API. So you maybe write your custom spans to one, but that's not the one that is connected to
an exporter, and so there are a lot of tricky bits to keep in mind.
But that, ideally, you can combine the two, like, have, auto instrumentation, setting up all the plumbing, and still allow custom
instrumentation. I don't think that really works for Python. We tried that a little bit with some of our own workloads that have custom instrumentation. We didn't get it to work, but yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:01 Bless you.
Bastian Krol 00:47:02 I agree that this is a worthwhile goal, for sure.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:06 Yeah, for Go, it worked, because I know, because OpenTelemetry Go, even the other instrumentation and in OB, we added specifically support that if you start using the SDK or the API to add manual spans, we can register this global tracer, and then it just picks it up from there.
Bastian Krol 00:47:24 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:25 Okay, fair enough.
Bastian Krol 00:47:26 I still…
Michele Mancioppi 00:47:27 And also, Python, in my experience, is pretty fiddly. The moment you start mixing release trains.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:34 I see.
Michele Mancioppi 00:47:34 SDK that is way younger, or older as a package, an instrumentation.
Bastian Krol 00:47:40 That's one of the reasons we thought it's probably too risky, because if you mix outer instrumentation, custom instrumentation from two different sizes, you are probably locked, so the application needs to have the same compatible version, or it will break in weird ways, so that's…
Michele Mancioppi 00:47:59 Which is why I ultimately had that knee-jerker facts of, no, no, you don't have the SDK, you have the API, because that is the only thing that actually is…
Nothing down safe to do.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:10 Yeah, yeah. But the API could also be wrong, version.
Michele Mancioppi 00:48:14 Yeah, but the nice thing is… yes, but the API of OpenTermetry is seldom… I don't actually remember an actual breaking change.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:22 Mmm.
Michele Mancioppi 00:48:23 In, in… Recent memory.
Bastian Krol 00:48:26 So… my mango.
Michele Mancioppi 00:48:28 Just don't expose some methods. That's why.
Bastian Krol 00:48:31 I make a forecast, like, I think this topic of double instrumentation and combining that will
need a couple of iterations, I think that's very.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:42 It's popular, for sure. Yeah.
Bastian Krol 00:48:45 You know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:47 In orderly, we do the same approach as you are proposing, which is, if we see instrumentation in the application, we just let it go. We just say, no, we're not touching that.
Bastian Krol 00:48:59 I mean, even if that…
would work, you end up with duplicated spans, even if you don't crash the application, so that's… that's another thing. I recently, added this, this kind of, is this already instrumented check to our own, Node.js distribution? So, for historical reasons, we have a dash zero Node.js hotel distribution. In Node.js, the check is really easy,
And I think I would like to upstream that at one point to the…
node auto-instrumentation package, or the Node SDK that needs to be seen.
So that this also works, if… if the injector's node instrumentation finds the Node.js app that is already instrumented, we should also be able to detect that, and I think that's something that needs to be in the runtime packages, so in the Node and Python packages, etc.
If possible.
Michele Mancioppi 00:49:58 There is, there is a bunch of these kind of things to sort out.
In the language… language 6, because…
SDKs like Java and Node are pretty safe to inject.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:12 Yeah. And…
Michele Mancioppi 00:50:13 some are… Effectively claymore mines that you put under your ass.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:20 So, I talked to Jack here internally, when I… before I asked the question, I was asking all the SDK people that work in Grafana, I was like, what… how does this, double instrumentation work? And Jack convinced me that in Java, it's just gonna do the right thing, even if you double inject it, which is really… which is really good, in my opinion, because then there's one we don't have to worry, and as I said, like, Node.js and Python, it's probably easier to add with these sort of scripts that get
picked up, and then you can check. The only one that remains is .NET, which is why I proposed that since we already read the maps.
Michele Mancioppi 00:50:56 NET is actually not a problematic one.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:58 Well, because there's only one guy on the profiler, but I think they say if you, like, the guys told me internally, it's unsupported behavior. If you have your own instrumentation and the auto tries to do something, it's just like…
You're on your own.
Michele Mancioppi 00:51:14 Wait, what?
Bastian Krol 00:51:15 Does that work? Because you can only set one profile, and then the.
Michele Mancioppi 00:51:18 You cannot activate the truth.
Bastian Krol 00:51:21 How can you get double instrumentation to even be a thing in .NET?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:25 But can we… do we check to see if the profiler is on? We do?
Bastian Krol 00:51:29 We just override it. We very boldly just override it, which is maybe also not the best thing to do, because there is already a profiler, then we just kill it and kick it out. Right. But that's the status quo.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:43 But, so what I was thinking about is that for .NET, there will be binaries, so they will be compiled. Since we're already reading the proc maps, why don't we just check
for the core CLR.
Sorry, not…
Bastian Krol 00:51:55 Wouldn't… wouldn't we just check the environment variable?
Michele Mancioppi 00:52:00 Can we take a step back. I still have not understood in which situation would trigger double instrumentation here.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:06 It's not just double instrumentation, my worry was that something will break. Let's say I have a customer, I have instrumented my .NET application using the .NET SDK from OTEL, and I'm happy running. Then I'm adding the injector globally in Kubernetes. Let's say through the operator, and it just starts instrumenting everything.
Okay. This application, and somehow leaks the instrumentation.
Bastian Krol 00:52:29 That's it, so you say the .NET binary is already built with OpenTelemetry baked inside, is that…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:36 Exactly.
Bastian Krol 00:52:37 Yeah, yeah, yeah, that makes sense.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:39 And it's binary, so it's easy to check. We can already find it in the shared libraries, so it's just a list of the frog maps.
Michele Mancioppi 00:52:48 Yeah, we could, we could check that.
Yeah, that's… There is no not about the name of the binaries.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:55 I mean, we could… I think it will be, like, DLL, OpenTelemetry DLL something, it will be there, I'm sure. I don't know.
Michele Mancioppi 00:53:01 That is, it's going to be file names, and, I do not remember if in the bundling,
of .NET, you actually get the names to be scrambled or not, so I would not bet money right now that you can look at the proc maps and know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:21 I don't think they can statically link it.
Michele Mancioppi 00:53:24 Not statically linking, is that they can be renamed?
You could call it food.bar.dl.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:31 Yeah, sure. Okay, yeah, I mean, nothing is bulletproof, right? I mean, at the end of the day, most people will just import it, and it will be open telemetry in the maps.
Michele Mancioppi 00:53:41 However… I believe that with the fact that we have the DL, the DL SIM.
We could actually…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:52 But you need to parse that, because you want to parse the symbols.
Michele Mancioppi 00:53:56 No, we already do that. So, what happens is that when, what the injector does is…
It first uses the proc maps to locate ellipse C.
It goes, reads the ELF symbols of the mapped memory region to find the ELF sim.
And then through that, it finds, MVRO, and it finds SATAMP.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:17 Okay, yeah.
Michele Mancioppi 00:54:18 Technically, we could do the same, looking for some distinctive .NET thing.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:23 Yeah, the OpenTelarchy.net. Yeah, okay, that's a good.
Michele Mancioppi 00:54:26 actually very cheap, because there is no allocations going on. It's literally a bunch of pointer magic back and forth.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:34 Yeah, okay, that could work. That could work better then, yeah.
If that works, then it's better than definitely reading the Brock maps.
Michele Mancioppi 00:54:43 It's, it's actually a two-step thing. First, you read the proc maps to find out which memory regions you have mapped.
Then, region by region, you go and use the DLSIM of the libc to go and say, hey.
That's so.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:57 Yeah, is there a symbol in there that looks like on that auto something?
Bastian Krol 00:55:08 Yeah, sounds good.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:10 So then we come, oh, these are 4.
Michele Mancioppi 00:55:13 Something that I do not believe is viable, however, is to be able to detect, upfront what type of process this is.
Is it Node? Is it .NET?
We could have some heuristics, but we are going to find corner cases of somebody
doing something profoundly depraved in the way they built their Node.js runtime until the heat death of the universe.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:35 Yeah, we… we do have that in OB. It does work to some extent. Most are… like.NET is easy, so is Java, right? If you see libcore CLR in there, it's .NET. If you see Java, libjvm.so loaded in the maps, that is Java.
Python and .NET, I… they're a little bit more complex, but libpython will be there if it's Python.
It'll be one of them, I'll just loaded.
Michele Mancioppi 00:56:04 Copy.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:05 And Node, unfortunately, just vendors everything, so there's very little external dependencies, the Node.js runtime, it's,
One big blog binary.
You don't do that?
Michele Mancioppi 00:56:18 Okay, there should be, there should be local objects.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:22 Yeah, you can look into the symbols, you'll find them, yeah. Yeah, there's specific symbols if you want to determine for sure that it's known.js, yeah.
Michele Mancioppi 00:56:31 So, there's multiple approaches.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:34 We do, like, we try to avoid the symbol reading, because for us it's an external read, so you just open the binary and walk the symbols.
Which is more memory-intensive than checking crop maps, but, yeah, definitely doable.
Michele Mancioppi 00:56:54 Why is it's memory intensive?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:56 Reading the… remembering CPU, right? Either way, you gotta open the file, and you gotta process it, and…
you want to instrument OB, you can throw it at.
Michele Mancioppi 00:57:05 Oh, yeah, because we do not… we are not inside.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:57:08 One is another person, right? For us, it's external.
So, I mean, one particularly bad one is Click House. It's massive. So, you try opening that and walking it, it's, it's a lot of…
Michele Mancioppi 00:57:22 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:57:28 Cool, this is good. Okay, I'm actually feeling good about this.
Personally, about the… the ability to detect and not break the apps. This would be awesome.
Bastian Krol 00:57:40 Yeah, we should probably, at some point…
write these ideas down somewhere to some extent, but for now, I guess we are not tackling them tomorrow, so that's fine.
Michele Mancioppi 00:57:52 The change to go from user customized to site customized is something we do.
Indeed.
operator, because…
Bastian Krol 00:57:59 Yeah, that's something we can just try, easily.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:03 Try it, see if it works. I think it should work better, yeah.
Bastian Krol 00:58:06 double up.
Michele Mancioppi 00:58:07 Do we open, an issue on the rad proof for, double… avoiding double instrumentation at .NET?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:15 Yeah.
Yeah.
Let's discuss that there. Yeah, let's open an issue and let's find a way.
I'm a little bit busy at the beginning of this week, but maybe I'll give it a shot if nobody else does in the meantime, by the end of the week, see how it goes.
Bastian Krol 00:58:48 Oh, by the way, Nicola, I, intend to call dips on that other part of the,
issue for the other to just merge, the one where we want to disable individual runtimes, or all the runtimes that… that was kind of all mixed up in one issue, but it's… I think it's a separate environment variable and a separate thing, so…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:11 Yeah, sure, go ahead, please.
Yeah, I'm particularly…
like, worried about .NET, which is why I think it's important, because my understanding is from the folks at Grafana that work on .NET, auto instrumentation.
The auto instrumentation can oftentimes not work properly.
And… People often resort to…
Implementing, like, three lines of code or something that adds it to their source, because they'll hit.
Bastian Krol 00:59:56 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:57 And it would be bad if we just reverted that.
Yeah.
Bastian Krol 01:00:00 Yeah, for some reason, for .NET, I was only always thinking about the way to attach via the core CLR profile environment, but of course, you can just put these dependencies directly in your app, and then…
That, for sure, will, crash.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:18 Yeah.
Michele Mancioppi 01:00:21 I think technically we… something that I'm wondering is…
Maybe we can do it in the .NET startup hook?
Because we would register a startup book.
But then, I am not sure if that happens before or after the CDR provider is bound.
That's something that, that, we could test.
Because, doing it with a .NET primitive, But…
Rob… No, wait a second, we need to… we need to, the hook from the SDK.
So unless we wrap that, we cannot… no, never mind. We do it, we do it at the simplest level.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:01:13 Nuh.
Very cool.
Bastian Krol 01:01:21 Very nice.
Michele Mancioppi 01:01:22 fun.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:01:24 That's gonna be fun.
Bastian Krol 01:01:28 Good! We are out of time, so…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:01:32 Any of you folks going to the CubeCon EU?
Yeah?
No? Okay, Michaela, I guess I'll see you there.
Michele Mancioppi 01:01:43 Hi, folks.
Jack Berg 01:01:44 Yeah.
Bastian Krol 01:01:44 Bye-bye.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:01:45 Right.
