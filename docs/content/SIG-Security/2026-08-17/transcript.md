SIG: SIG Security
Date: 2026-08-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 00:57 Hey, Gunther.
**Jonathon Klobucar** 01:01 Good morning, Riley, how are you?
Good! I, I should be able to join these now that I'm not, traveling. I was at, Well, you're on vacation, but, I was at, DEF CON, and then, I was at, our company's off-site last week, so…
**Reiley Yang (Microsoft Corporation)** 01:21 Hey, awesome.
**Jonathon Klobucar** 01:23 Yeah.
But I'm here now.
**Reiley Yang (Microsoft Corporation)** 01:27 Yeah.
This is great, and I also, heard, like, a couple more names that I… I'm reaching out to, so sounds like we have a party here. Hey, Trask!
**Trask Stalnaker (Microsoft Corporation)** 01:39 Hey, Reiley.
Hey, Jonathon, nice to meet you.
**Jonathon Klobucar** 01:43 Nice to meet you as well!
Von, I can, let's great, just a sec here. Yeah, nice to meet you, You get me on my phone at the moment, so enjoy. But… Yeah, so, Did any introductions stated? Like, I… did Reiley told you about me at all, or…
**Trask Stalnaker (Microsoft Corporation)** 02:07 I think so, but I might be misaligning names and what Reiley has told me, so… Maybe a recap would help.
**Jonathon Klobucar** 02:17 Yeah, no worries. Alright, so my name is, Jonathon Klobucar.
Oops, sorry.
I have been, a, like… in security for a few years. I used to do SRE stuff, and then, you know, that's been a lot of my career, but most of my SRE stuff was very security-focused. I'm currently… I was at Sublime Security for a year, and now I'm at Socket, which is Also deals, you know, primarily with supply chain, right? And I'm… they're, like.
product security engineer. I've done other open source stuff and, you know, got interested in trying to help out when I saw Austin Parker was like, can someone in a different community, he's like, can someone, like, go help them out? They could use a hand. And I was like, yeah, let me talk, so… That's… that's me. I'm based in San Francisco, And, yeah, like, not too much, huh? There's stuff.
**Trask Stalnaker (Microsoft Corporation)** 03:12 Cool.
Awesome, welcome.
**Jonathon Klobucar** 03:15 Yeah, thank you.
**Reiley Yang (Microsoft Corporation)** 03:20 Okay, so, I have a couple of topics. I have some, like, local changes. I plan to push a PR later today or tomorrow, to change the README file. So currently, if you look at the SIG security report, the README file doesn't seem to give people a clear view, like, what's the most important thing we want to focus on, and I want to, change that a bit to, more, like, focusing on the supply chain security for now. I know security is a big scope, and there are many other things, but I think the supply chain is the most, interesting thing to folks, and definitely something we need to improve. So expect a PR from me. And another thing, I have to talk to Charlie, I… I'm not sure, like, if he can join this meeting, the security researcher on the NPM side. He's been giving us a lot of, like, suggestions and ideas on how to do a better job there. So, so based on that, I want to work on some article, and hopefully we can publish either on the security SIG, or ideally, I would hope, a blog post, just to Like, socialize with the… The rest of the world, how we want… people from the security side to come and help. So, Yeah, so these are two, like, heads up, I'm going to send some, like, draft, talks and PRs.
Today or tomorrow. Any questions?
Okay.
**Trask Stalnaker (Microsoft Corporation)** 04:57 Hopefully, hopefully GitHub will be back up, and…
**Reiley Yang (Microsoft Corporation)** 05:00 Oh, it's dumb.
**Trask Stalnaker (Microsoft Corporation)** 05:01 actually.
**Jonathon Klobucar** 05:01 It's hard down, oh yeah.
No day.
**Reiley Yang (Microsoft Corporation)** 05:06 Yeah, yeah, so, in the past week, I… I was, helping on 8, security advisories that people reported, and one… one thing I noticed, like, I have permission to add whoever, like, to the… to the security advisory, and for that particular case, I won't be able to share all the internals, because it's still a secret thing.
But the… the problem is somewhere between open telemetry and Jaeger. So, initially, when someone reported that security advisory, it got automatically assigned to the repo.
owners. Like, the repo maintainers, 5 of them, they got there, then I tried to ping them, reach out to them. Then, one thing they… they asked me is, hey, like, can you add the Jager maintainers? This is from a different product, also under CNCF. And then I just realized the… they were added there, but they don't seem to have permission to add others. So, the first thing is, I think it makes sense, if you're already added to the security advisory, as a, like, owner of the repository, like, basically, you own the follow-up, then I think you should have the power to add others.
Any, like, questions or objections?
I think it makes sense, and it doesn't seem they have the permission, so I have to see, like, what we can do. And I think, ideally, we want GitHub to be able to allow this, but it doesn't seem so, like, GitHub security workflow seems to give us all these troubles. So then, if not, I hope we have a mechanism, like a bot or something, so they can just say, like, I request someone to be added there, then they can… they can at least, like, help themselves. Or, the worst case, they can tag whoever, is, like, on the TC on-call rotation, because they have the org admin. Like, the problem is, I added them, but then I finished my TC on-call week.
Then I was doing something else, then when I went back home, I saw someone ping me, and I assume it's urgent, so I caused, like, about, like, one day delay, because after my on-call week, I was not checking all this, like, security advisories every day.
Yeah, and I feel like if it's… it turned out to be a really urgent issue. I don't want myself to be the one-day delay problem. So, yeah, I feel there's something we need to do here.
**Trask Stalnaker (Microsoft Corporation)** 07:40 And is this primarily the difference between admin and maintainer permission repo?
**Reiley Yang (Microsoft Corporation)** 07:46 I have to check, but in order to check, I have to create another GitHub. I think Trasky, you've done that before, right?
**Trask Stalnaker (Microsoft Corporation)** 07:52 Yeah, yeah.
Okay, yeah, because I… I mean, if… That's the other option to consider, given the problems we've had with Maintainers having, with security, access to do things in the security Advisories is just to make everybody admins again.
**Reiley Yang (Microsoft Corporation)** 08:16 Yeah, so I can't… can you see the… the black window I shared?
**Trask Stalnaker (Microsoft Corporation)** 08:21 Yeah, yeah.
**Reiley Yang (Microsoft Corporation)** 08:21 I see here, like, they have to tag me, they have to add people here. Yeah. Then there… there are a lot of, like, pings, because people don't know what's the right way, so some of them ping me on Slack, then I just realized that at very late night, so… This is why it seems like it's taking time.
**Trask Stalnaker (Microsoft Corporation)** 08:39 Yeah, but I think it… Oh, go ahead.
**jonathon klobucar** 08:42 Oh, no, I was just gonna say, I think one thing is, like, that I'm seeing in this is that the communication path for when there's security advisories may not be, like, as crisp as it should be, of, like, I need to… like, it, in essence, needs, like, a… like, I wouldn't quite say, like, an instant commander from the SRA, but it needs someone that's, like, yeah, sort of corralling it, and it looks like, like, after on-call week, like, it's just sort of… So far, like, who corrals it, like, after the on-call handoff? Does it just, like, kind of flow to the next person, or, like, how does that sort of work? Because I think that's part of the shift, right?
**Reiley Yang (Microsoft Corporation)** 09:16 Yeah, okay, so let me explain. So, like.
this is what I would hope. I would hope for each repository, the maintainers would have some mechanism to handle it well. Like, whether they want an on-call, or they're going to say, like, we'll just throw random dice, but if you got the… if you got the phone call, you should do it immediately. Like, it's their freedom. I… I'm not there to… force them to follow a certain process, although I have my opinions. Then, the technical committee is, like, the catch-all. So we're saying, if there's security advisories, and nobody is taking care of that, then the technical committee have an on-call rotation every week. If you're on call during that week.
all the newly, created security advisories should be handled by you, and we expect, like, a daily triage, and then you should work with the right side of folks. Sorry, my… my screen just went black, I have no idea why.
Okay, now I recovered. Yeah, so… so you as a TC member, we don't expect you to know everything, like, if you come and say, but I don't know this particular, like, JavaScript repository, that's fine. We expect you to go and rally the right side of folks, because you're supposed to, like, know these folks, and when they see you're coming from a technical committee.
they trust you, like, after verification, like, they know where you're coming from, they trust you, so you're going to help do the… coordination. And the second part is if we have the, like, folks who, just reach out with some, like, very tricky issue, like, they see a security problem across many different language, SDKs.
then, like, do they create individual ones for every repo, or they just, like, talk to someone? So, in some cases, people don't know what's the right thing to do. They should just reach out to the primary on-call, like, technical committee member, but… The problem is the technical committee member is more like rallying folks, rather than they go and fix every single issue. In case there's a debate, like, if the people who report the issue had a fight with the maintainers, saying, I disagree, the maintainers, like, have a different position, I think the TC members, sometimes I also select Trask.
They're trying to help, so we're trying to… Like, provide, feedback there, and find a reasonable balance, and keep the communication going on.
So that's what the TC is doing. And the problem today, I've seen, is many of the security advisors, they come here, and they automatically tag, for example, like, 5 maintainers of the repo. But there's no established power site, so the maintainers simply, quote-unquote, forgot about those. Like, nobody's looking at this.
Then, as a TC member, like, if I'm primary on call, I don't try to pin them immediately, because I assume they will come and do the work. Then, I post something on my reminder, so after, like, 24 hours, if I don't see any response there, then I'll chime in, and I'll work with them.
So I don't even try to be the first one who responds to the security advisor, even saying, thank you, I don't want to do it, because I think it's their job, I want them to do it.
And then, if I don't see any action there, like, even if I tag them individually, I'm the security advisor, I don't see any of that, then I'll start a conversation, like, whether on Slack or email, like, I'll just reach out and see who's handling that. And I won't have a warm handoff, so someone come and say, okay, I'm going to take care of this.
Then I'll say, okay, so I'll leave it to you, and if you need some help.
please get back to me. There are cases where the maintainers could have some position, and when I look at their response, like, I remember one thing from Trask. So it could be, like, people report the issue, then the maintainers think, oh, it's not an issue, then I was trying to I share my opinion there to find a reasonable balance. So that… that's what I'm… I'm doing, and I… I think my goal is… I… I don't want TC to kick… kick in and handle every single divider. The maintainers should do it by default. And if the maintainers are not doing that, then their SIG have a problem. We should flag it, and they need to have some action.
Yeah, and the TC should be only helping there if someone explicitly requires them to help, or there's no clear accountability.
Yeah, so basically, like, I want to decentralize the thing. The current situation, like, why we have a centralized, like, TC rotation is because we don't have a better process.
**jonathon klobucar** 13:49 Yeah, no, that totally makes sense, like… like, this, yeah, I agree with you. The TC thing feels like it's a stopgap when it's, like, the… the repo should be able to, like, discern this and then, like, shuffle it upwards and outwards correctly, right? Like, the maintainer.
**Reiley Yang (Microsoft Corporation)** 14:05 Yeah, and I have some idea I'm gonna put in my proposal, so this is what I'm thinking, just to give you… some, like, prior, like, read on my mind, and let me know if I'm crazy. So I, like, I want every repo to have some status, like, whether it's, like, alpha, or it's, like, preview, or, like, stable. I think that's what we have, but In addition to that, I also want them to see what's the promise in terms of the supply chain security and the security advisories. And by default, they all start by, I have no promise. Like, I have the lowest bar.
And then I want this group to write, like, if you want to turn the status to have this certain promise.
Then these are the things you have to do, and you have to come and read it, you have to agree with it, and if you think, for example, we're saying you agree that any security advisories will get an active response.
Within a business state. And if you agree with that, we're moving you to a higher state, and you can put that thing in your repo readme file. So… so by default, all the repo readme files have a red flag saying this repo.
generate the artifact that has no promise. Like, there could be a security issue that has been running forever, and nobody would take care of that.
And also, if you report any security advisory there, you should expect that nobody will reach back to you. And then, if you want to fix that problem, you have to come and read and agree, and then you have to do it, and I also want to measure that.
**jonathon klobucar** 15:45 Awesome. Yeah, that's, like, a good start. That also shows the transparency, like, when people want more providence in their builds and, like, assertions, then, like, we can… We can work towards that.
And there's certain things that we can look into to, like, try to help streamline that.
You know, products or whatever that… that we can get our hands on.
**Reiley Yang (Microsoft Corporation)** 16:30 Yeah, so in this way, like, we don't force people to do it, but we ask them to reflect the current state for their product, and just, like, give the transparency. I think that's a reasonable thing. It's not a corporate, like, enforcement.
**jonathon klobucar** 16:44 No, it's like a nutrition label, right? Like, for supply chain. If you're gonna… if you're thinking of how to frame this in, like, a blog post, be like, we're trying to roll out, like, supply chain nutrition labels on, like, the hotel projects, so that you know that, like, which ones are… You know, Like, the security nutrition label of just, like, what it's… like, where we think it's at.
And where they need to improve.
**Reiley Yang (Microsoft Corporation)** 17:15 Okay, so that's pretty much it.
a lot of things I need to follow up. And, meanwhile, like Jonathon, I… I'm not sure, like, what's your immediate goal here? I know you've been trying to help, and of course, like, I'll involve you in those PRs.
To try to become an approver.
soon? Like, how can we help you? I mean, you're helping us, I want to help you as well.
**jonathon klobucar** 17:42 Yeah, I mean… I think shadowing either… some sort of… advisory that you're shepherding through, or some other stuff, I can try to help with that. Like, that's all up to you and how much you want to, like, involve me.
That's a good way to do it.
Sorry, I'll try my… if we have a repo that's, like, lower stakes, but, like… Could use, like, you know, us to test drive, like.
supply chain process improvements, I can take a crack there, like, If it's also just, like, can you just go take your… your clod and go fable a repo and see if, like, anything, like, what looks like some priorities, I can, you know, stuff like that, too, can happen.
**Reiley Yang (Microsoft Corporation)** 18:31 Okay, so… so one… one… one challenge I… I can see here, Trask, I… I need some of your thought, is when we try to grow people in the SIG security, we have, like, different levels. There's, like, people just come and help, then we move them to become an open telemetry member. I think that's where Jonathon is.
**jonathon klobucar** 18:49 Yeah, that's where I'm at now. I got you and Watson that approved me for there.
**Reiley Yang (Microsoft Corporation)** 18:52 And then we move them to approver, which gives them the power to approve the PRs, and those PRs are just, like, process and document. It's not a real security.
issues. And then, once we agree to move them to maintainers, it gives them a lot of power. Like, maintainers can see the email. Approvers cannot, I guess.
So, do we want to open up some of them? I mean, there's a balance, right? You don't want someone like a hiker to come and say, I just made my first PR, let me move them to maintainer, give them access to everything. That's too scary, but how do we do it? So my thinking is that supply chain security is a pretty public thing, right?
Like, if you depend on something, you don't need someone else to come and tell you. Everyone should be able to just… like, run a scanner and say, hey, you depend on this protoboth library, and that protobuf depends on some, like, arbitrary library that has a security vulnerability. So, that thing seems to be given by default, and I think this is where people can help.
And then they can prove themselves before they move them to a higher, like, stage. Then for security advisories, I think that's where we're struggling. I don't think we can just open up the security advisories for For people, unless, like, they've been working in this area for, like, maybe, like, 12 months, and have this consistency.
track record or something, so…
**jonathon klobucar** 20:20 I agree with all that, so I don't… I'm not asking for you to open up a bunch of stuff. Like, I think, one, earning trust is very important if you're gonna be on, like, the SIG security side, so, like.
like, I'm not… I'm definitely not asking to be like, just… just let me… just let me in, bro. It's more like, let me… let me find ways, this is what I'm talking about, let me find ways to, like.
give contributions, so it's, like, just a natural, like, oh yeah, you've, like, been poking around and adding good stuff. Like, now it's, like, for the community, it's, like, very easy to be, like, you know, in whatever, 6 months or whatever, 12 months, like, okay, like, we can… we can up your access, like, you're… you're… you've… you've proven yourself. So, like, that's what I'm looking for is, like, what little things can I do to help You know, that are guided, that it can prove, you know, my prominence.
In this world.
Versus just, like, hey, this guy volunteered, and then, like, here's just, like, a bunch of free rein, right? So, you know, that's where I was like, either lower risk stuff or, you know, there's certain supply chain things I definitely can go look for. It does help that I work for a company that does support open source supply chain, like, very publicly, to be like, I just ran, like… I just ran the SBOM for OTLJS through our product, and like… I found… I found, like, some things that we should probably figure out, right? Where the scores are low or something, and I can definitely do stuff like that.
And… and very… and also, yeah, find some other, you know, security bugs, whether that's, like, GitHub Actions that aren't Zizmoard, or, like, you know, it'd be really easy to add, like, you know, some actual, like, ODIC to this workflow or other stuff that they're missing.
So that's what I meant by, like, I can do some public looking. The thing I'm gonna ask is, like.
how do I best communicate that stuff? Should I, like… send that kind of stuff to you, Riley? Or should I open, like, a PR on their repo? Or if I find security stuff, should I go to, like, the… I think I found a minor security bug, let me report it as an advisory, like, what… what… what makes your life easier to see all of this?
**Reiley Yang (Microsoft Corporation)** 22:22 Okay, so if you have a proposal, I think these discussions in this meeting, or sending PR, like, both are fine. And PR, I think I've been looking at the PRs every day, as long as I'm not on vacation. If security advisory, I think that's… something, like, I don't want to treat, like, especially for this sake. I think anyone, when you see, like, those security advisories, you should go and file that directly, and you should receive the credit as a reporter for each,
**jonathon klobucar** 22:52 Yeah, I might have found a very low, almost informational one in the OpenTelemetry.js that I'll… that Claude, I think, vetted, and I'll try to open it and see what I can get.
**Reiley Yang (Microsoft Corporation)** 23:03 So how you work on that should be totally independent of whether, like, if you don't even know me, if you don't even come to the SIG security, you should still be able to do the same, but…
**jonathon klobucar** 23:13 You can also test the process from an.
**Reiley Yang (Microsoft Corporation)** 23:15 Exactly, yeah, exactly, but if you go through the process, you see the problem, you want to improve the process, I think this is where we can leverage your help, and also you can leverage us to be able to move things forward.
**jonathon klobucar** 23:27 Yeah.
**Reiley Yang (Microsoft Corporation)** 23:28 Which ones?
**Trask Stalnaker (Microsoft Corporation)** 23:30 Yeah, I was…
**jonathon klobucar** 23:31 I'm sorry, go ahead.
**Trask Stalnaker (Microsoft Corporation)** 23:33 This SIG is, more about the process. Yeah. But certainly, like, like Reiley was saying, testing out the process, by submitting things is a good way to find what's working, what's documented.
It's not that sort of thing.
**jonathon klobucar** 23:50 And I'm down with that, with this being, like, that's what I… that's what I envisioned this SIG is, is, like, it's the… it's the way to do good security by, like, helping inform the rest of them, not doing the security for God knows how many hotel repos, right? So, like, that's why I was, like, doing some stuff where I can, like, figure out what this process is, and, like.
my personal reflections on if it's where it's, like, holding up and where it's not, I think is, yeah.
It's good.
**Trask Stalnaker (Microsoft Corporation)** 24:14 Cool. And, Reiley, to your question, about… access… I could definitely see us separating, maintainer, from access to the CVEs.
like, maintainer of SIG security, Would be about maintaining the process.
Not… doesn't necessarily have to correlate to… the CVE access and helping with individual CVEs.
**Reiley Yang (Microsoft Corporation)** 24:52 Yep.
Yeah, I… I'm not worried.
**Trask Stalnaker (Microsoft Corporation)** 24:57 That would allow us to not block, sort of, that… Track on, you know, community worries about Bringing, you know, bringing people along, giving people too much access.
**jonathon klobucar** 25:33 Sorry. I was also gonna say, Something else, that as you do your, your pull request stuff, if you want to tag me in your drafts for any of the procedure, policy changes, or blog posts, or docs, like, I'll shoot you my email if it's the Google Doc stuff, but if, you can just tag me right on GitHub, and I should see it within, you know, 24 hours.
**Reiley Yang (Microsoft Corporation)** 25:57 Right.
**jonathon klobucar** 25:58 I'll be on the… I'll add some filters to be able to, like, see it.
**Reiley Yang (Microsoft Corporation)** 26:02 Yeah. Awesome.
**Trask Stalnaker (Microsoft Corporation)** 26:03 Probably worth watching the SIG security repo.
Yeah. It's not a… it's not a high-volume repo.
**jonathon klobucar** 26:11 Yeah, for sure, let me go do that right now, that's a good idea.
**Reiley Yang (Microsoft Corporation)** 26:15 Yeah, and Jonathon, please give Trask and me feedback about, like.
your motivation level, because I think Trask and I have seen this before. So we see people coming, and they express some interest, we're trying to help them, and we move them to approver, and once they become approver, they never come to this meeting again.
**jonathon klobucar** 26:36 Oh, yeah.
**Reiley Yang (Microsoft Corporation)** 26:37 For some people, the motivation might be, I just want to get a status, like, approver, maintainer. For some people, it's like, I have a particular thing I want to solve now. Once I solve that issue, I'll be gone. I, like… as a product maintainer and sponsor for this SIG, my goal is I want to have a better motivation system so people would feel this interest, or if we couldn't figure that out, I better be honest and say there's no way to establish a long-term SIG like this, but I… I don't believe that's the case.
**jonathon klobucar** 27:08 No, there's definitely a way. Part of it also, so I did, when I switched my employers.
like, this is on my work calendar that this is a thing that I attend. So, like, this is… I've made time for this professionally. I can see where people either join, and they're like, I want to do this, and then it's too much work, and, like, nope out, or, like, they just want their one thing fixed, and, like, it's not effective, but, like.
You know, I, you know.
my case was being a more conscious decision, but I definitely know what you're talking about, where people, like, get really interested, and then, like, when they… they aren't getting movement, or it's not what they thought it was, they just sort of, like.
just go radio silent, you're like, I don't know what to do with this, I thought we were working on this, and not, like, they just, you know, went back into the ether.
**Reiley Yang (Microsoft Corporation)** 27:52 Yeah, I can give you one example. Like, this, when this SIG started, I… at that time, I… I was also running a couple, like, SDK 6.
And in one SIG, I was having the trouble, how do I sign the binary? Of course, I cannot use a Microsoft certificate and ask other companies to all follow that, right? We need some, like, open source, like, open way.
But there's no such standard. At that time, I think SIG store was just at the very initial state, so… Yeah. So my focus when I joined those discussions were just, I… I need a way to sign my binaries on behalf of OpenTelemetry.
And once that problem solved, I just disappeared from this discussion for almost a year. Then I started to say, oh, Microsoft, internally, we have a lot of supply chain security issues, and if I don't solve the problem in the open source repository.
I have to do it again inside Microsoft, exactly the same amount of work, then it wouldn't make sense for me to do it in private, so I want to work with the community to find a better solution. So this is why I'm driving the SIG right now.
Yeah. And once that problem is solved, I, like, I'm, like.
I'll have the question again, like, what's my motivation? So, I think you have… you have similar challenges as me, trust, like, we all have limited amount of time, and we spend the time here because we want to achieve something, right? So I want to better understand, like, what we don't have to discuss it now, but I want to receive your constant feedback about your motivation and what motivates you, because this helps me, as long as I'm in charge here. I want to understand how I can do a better job to motivate more people to come and contribute.
**jonathon klobucar** 29:33 I mean… I mean, my motivation is primarily, like, this product is used everywhere, and it needs, like, you know, to… to rethink, security in some aspects, but, like, really the big part is, like, I'm very interested in supply chain stuff, so, like, a lot of the work I would be doing up front would be, like.
making sure that, like, you know, direct dependencies or transitive dependencies of open telemetry are, like, generally, like, pretty well locked down and, like, other stuff, and I think that that's just, like.
You know… table stakes at this point, but trying to get a pretty big movement on it is gonna be hard. And it's gonna be an interesting challenge, and it's gonna be… like… It's gonna be something to write about, for sure.
**Reiley Yang (Microsoft Corporation)** 30:18 Yeah, and for both of you, do you know if there's some… some, like, existing system that can track when a security advisor was first discovered by someone? Like, how people work through that, and then they have a published one? Then how would the… the… the… the entire, like, dependency tree eventually, like, pick them and propagate the fix across the entire thing, and then how that got deployed. You can imagine it's some… something like a discrete tracing. There's a, like, Gantt chart, so from the discovery to, like, fix, to the upstream, like, pick up the… dependency, and then another one for dependency component have to pick that up again. So the entire time that's taken, and you can slice that down by each individual step.
and ask the question, like, why would this step take this time? And it could be, like, communication, it could be, like, we need tests, or it could be just, we don't have an established process.
Like, it requires, like, many pings until people realize the issue, so… so is there a way to, like, visualize this across many… across, like, all the existing CVEs to understand, like, how much time it takes for it to fix and see the trend. I think that'll be pretty interesting.
**jonathon klobucar** 31:32 It is, yeah.
**Reiley Yang (Microsoft Corporation)** 31:32 That's like…
**jonathon klobucar** 31:34 Yeah, that's like figuring out, like, a vulnerability management program for OpenTelemetry, right? Like, I've had to use it a couple of jobs where it's like, I see my downstreams, I have to push them to my upstreams, which are, like, customers, or some customers are running my software, or whatever, and, like, that's a… that's a thing that we… we should think about, how to do. I don't think that there's… there's a tool that just, like, does it for you, but I do think there's ways that, especially in this, age of AI gen-made software, there's a way that we could… we could find something that, like.
helps us with the reporting and, like, tracking better.
like, we can go look for tools, too, like, someone might… might be like, oh, I'm definitely… we'll offer you OpenTelemetry, like, I'll donate this, like, licenses to this tool, or whatever, but we can also… we can see what exists, I've had… I mean, not to… most places I've worked until they get sufficiently large, I've basically used a Google Sheet in the past to do, like, tracking, which is not great. Sometimes you use things like linear or GitHub issues or whatever, but yeah, if you're trying to actually also get, like, metrics on, like, time to, like.
fix and pull into upstream and, like, track, like, that's a… yeah. I feel there's… there's probably some… some tool that we'll have to look at to… to fit our needs specifically here.
Sorry, I have to hear my dog barking in the background, she, she heard, something outside.
**Reiley Yang (Microsoft Corporation)** 33:00 Okay, I, I, I think, That's all the topics I have.
Okay, so if there's no other topic, we can… we can give the time back.
**jonathon klobucar** 33:12 Yeah, I wanted to say…
**Reiley Yang (Microsoft Corporation)** 33:13 Adams.
**jonathon klobucar** 33:14 Thanks for meeting, I'll… Put this on my calendar to be here, and we can kind of see how we're going.
**Reiley Yang (Microsoft Corporation)** 33:21 Yeah, I hope in two weeks we can have the banner for the repost, and start to have a conversation with the maintainers.
**jonathon klobucar** 33:31 Yeah, absolutely. And I've watched the open… the SIG security repo, so… and you can just tag me in any PRs, and I'll make sure I see them.
**Reiley Yang (Microsoft Corporation)** 33:41 I will.
**jonathon klobucar** 33:42 Awesome.
**Reiley Yang (Microsoft Corporation)** 33:44 Have a good one. Bye.
**Trask Stalnaker (Microsoft Corporation)** 33:45 Bye.
