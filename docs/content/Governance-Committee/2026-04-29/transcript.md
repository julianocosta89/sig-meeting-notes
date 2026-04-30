SIG: Governance Committee
Date: 2026-04-29
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Marylia Gutierrez 00:01:25 Hello.
Austin Parker 00:01:27 Blue…
Trask Stalnaker 00:02:01 Good morning.
Austin Parker 00:02:06 Hello?
Marylia Gutierrez 00:02:36 Hmm, trust.
Any chance that the token that we are using to, like, run scripts cannot create PRs?
Trask Stalnaker 00:02:49 Give me the link… link to the run.
Marylia Gutierrez 00:02:53 Cause I keep getting, like, 401.
So, at least now, with my latest PR that got merge, it doesn't expire.
But it's running for… it's running for, like, 20 minutes, and it, like, ran everything.
Trask Stalnaker 00:03:06 Oh, yes, you cause… This is an actual PR, not an issue, so you have to be able to push to the… Branch on the repo itself.
Marylia Gutierrez 00:03:18 Yes.
Trask Stalnaker 00:03:19 That's the problem.
Marylia Gutierrez 00:03:22 So I finally, like, was able to run in 20 minutes, and it just ran, and now, like, I'm creating the PR, and then it just shows 401. I was like.
Trask Stalnaker 00:03:30 Yeah, it's the… it's the… not the PR creation, it's the pushing to the branch that's failing, I assume.
Marylia Gutierrez 00:03:38 Yeah, so I didn't put any… extra message to help me out, so I just get, like, a 401 unauthorized.
I didn't put, like, steps on which part.
Trask Stalnaker 00:03:49 Yeah, can you drop me a link to the… CI run?
Marylia Gutierrez 00:03:53 Yeah, I just put it here on the… on Zoom.
Trask Stalnaker 00:03:56 Oh, cool. Thanks.
Marylia Gutierrez 00:04:02 Yeah, look at this step, check activity and create PRs.
Trask Stalnaker 00:04:24 I'll look… I'll look at the script.
Marylia Gutierrez 00:04:26 Inc.
And thank you for the patience for everybody that is approving those PRs. Like, it's annoying because I do things, like, local, everything works, and finish in, like, 5 minutes, and every time that I put it there, it's like, 90 minutes run! It was like, ugh, oh yeah.
Trask Stalnaker 00:04:44 GitHub Actions is always that way for me. Like, I literally never know if it's gonna work until I actually… like, I can do as much testing and… as I want. Even I test stuff in my fork… GitHub Actions in my forks a lot.
But until I actually merge it and run it, Yep.
Marylia Gutierrez 00:05:02 There's one that doesn't even make sense. I keep getting one that apparently is like, oh, the hash is no longer valid. I was like, there is no commit between when I started the script and when I'm running, so why you're talking about a hash changing? Doesn't make sense at all. But I put in the fix, at least I didn't get that error this time, but yeah, still… I'm annoyed.
Alolita Sharma 00:05:38 Hi, everyone.
Marilla, don't.
Keep going… come and carry on.
Marylia Gutierrez 00:05:49 Just gonna go bang my hand on the wall and be right back.
Alolita Sharma 00:05:53 No, no, no.
the Google Nexus one.
We even got called out as a project in the keynote.
Trask Stalnaker 00:06:12 Nice.
Alolita Sharma 00:06:13 Very cool. Hotels, semantic conventions, observability.
Trask Stalnaker 00:06:18 Mmm.
Alolita Sharma 00:06:19 Gen AI instrumentation, so that was very cool.
Ted Young 00:06:25 Did they spell her name right?
Alolita Sharma 00:06:27 Yes, they didn't say it, they didn't spell on you right. And Ted, they didn't call you a flounder or anything. Bastard. No.
Ted Young 00:06:48 Do people have, agenda topics? I put a couple of things on there.
But…
Trask Stalnaker 00:06:58 Fire away.
Marylia Gutierrez 00:06:59 Yeah, my topic was just frustration. I already put that out, now we can move on.
Ted Young 00:07:05 Yeah.
Okay, so two topics. One is just, trying to get stabilization, you know, over the finish line. We discussed in the spec meeting, I'm gonna try to to take that over to… to drive it, because when… just getting into the weeds, some of this stuff is harder than it looks. The area in particular that I'm most concerned around is stabilizing all of the instrumentation.
that is kind of an unfunded mandate, right? Like, we've had a model up till now that Contrib is community-managed, and if people want something to work or be better, they can come in and… and update it. But… and then the other model is, like, one day we will move this stuff upstream into native instrumentation, but… for either of those things to work, I think we need to come up with, like, a… just, like, a different approach to how we… we manage those packages, specifically the instrumentation packages.
I think… something that involves using, better tools. Weaver seems to be just about ready, so I want to investigate how we can use, Weaver plus, like, testing tools to constrain the problem really hard, and then potentially allow AI tools to help us improve it. And the same tools would also be what would help, you know, move these things upstream into a native Native instrumentation model, but… It's… it's kind of like a different way of doing it, and I don't really see how we get over the finish line of stability, for all of that stuff, unless we come up with something new. So, I'm gonna put my proposal out there and be wrong on the internet, and people can… can tear it apart, but… but I'm curious what other people think, if other people have been thinking about, you know, the contribrib management problem at all, and if they have… Any insights they want to throw out at this time?
Trask Stalnaker 00:09:24 So, I have… Then, on the conformant side of, you know, the… because you brought that up as one way to drive this stuff.
So this has come up, heavily in the Gen AI work of, you know, trying to take different people's instrumentations and sort of benchmark them, show, what's happening, and drive. I totally agree, like, with that. I think that's a really effective feedback cycle, to drive changes. I… There's still a whole other hurdle of… declaring stability. That's partly also just mental.
And… Accepting that there will be future major version bumps.
But, yeah, so I did HTTP to kind of see what this would… look like. So these are all just Hotel Contrib, and so, like.
You know, it's looking pretty good. Some… the asterisks are, you still have to opt… do the opt-in.
But, you know, I know a lot of those languages are moving in that direction.
Anyway, that's all. I know the problem's way bigger than that, but .
Ted Young 00:10:59 But…
Trask Stalnaker 00:11:00 So, the goal here is, we do want to bring this over into semantic convention, well, as a new repo.
owned by the Semantic Convention folks.
It may be a temporary-ish landing spot, in terms of, kind of ideally, this conformance testing would belong in the repos themselves.
So… I don't know, there's… I wasn't gonna land the HTTP stuff to begin with, but I did kind of… The Gen AI stuff is what we want to land initially.
But I wanted to kind of… Explore how we could extend that if we wanted to, to make it, you know, a general… Or general… general, or… Peace.
Ted Young 00:12:01 Nice.
Austin, got your hand up?
Austin Parker 00:12:05 Yeah, I was wondering… I mean, kind of along… Excuse me, gosh.
Along what Trask was saying, and what you were saying about Weaver, like, is there a… I mean, what's the appetite for, sort of, the blunt force trauma approach of just saying, instrumentation, like.
If you want instrumentation that is official, then it has to be attached to a SEMConv.
Ted Young 00:12:48 I think it's just a labor shortage, right? Like, we're seeing two things here. One is, Maintaining this stuff is maybe… could be made a lot easier, right?
some tools that could automate a lot of it, and kind of almost reduce it to, like, someone just has to review the PRs, which would be great, but then someone still has to review the PRs.
Austin Parker 00:13:14 Yeah.
Ted Young 00:13:15 I'm noticing this, like, growing tragedy of the commons with OpenTelemetry, and I think… you know, like, the first… the first thing to dry out is, like, contribib, but it's, like, as OpenTelemetry becomes more perceived as stable, the less interested the various vendors and people are in, like, contributing labor, and I heard a lot of this from… people are like, well, if someone wants that to work, they should deal with it. I'm like, we want it to work.
Alolita Sharma 00:13:42 In fact.
Morgan McLean 00:13:43 Yeah, I think that's.
Ted Young 00:13:44 No industry's useless without this stuff, so…
Morgan McLean 00:13:47 That's actually true for instrumentation, right? Like, people want to contribute.
Ted Young 00:13:51 Tiny things. Yeah.
Austin Parker 00:13:53 That's 100% true. I mean, I think, like… Putting on my… Yep.
Alright, he's putting my big boy pants for a second, like… I'm… I think there's utility in saying, like, okay… where you need to start taking toys out of the box until you take care of the ones you already have, type of stuff, right? Like, I agree, like.
We have these multiple…
Trask Stalnaker 00:14:29 mean in practice, though, like…
Austin Parker 00:14:31 Practically, it means that, like, okay, here's the, like, contrib now becomes the… the wasteland, and, like, if your instrumentation, like.
we have the split already, right? We have contribib versus non-contrib. We simply say, okay, if this instrumentation has, like, a active slash stable semconv, that means we can promote it to core. And if it's in core, here's the guarantees. And if it's in contribib, then Like, contrib becomes sort of the load… like, we load shed away from contribib.
Right?
Now… I think there are, like.
I think a thing that we could do is we could provide, you know, to your point, like, people don't want to contribute as much time. Okay, like, are there interesting things we can do about saying, like, well, hey, maybe you can't contribute people, but you can contribute tokens to the cause?
Ted Young 00:15:32 Yeah. Pablo, you've had your hand up for a while.
Pablo Baeyens 00:15:37 Yeah, I was just going to mention briefly a couple of documents from, the collector, which I guess it's a… has enough similarities that could serve as inspiration. So there's the component stability guidelines, and then We've done some work, although not a lot yet, on automation that I think could be useful here. I… I really like the… having the metadata files for every component, which I think Java also has, is really useful for ensuring… A baseline level of… Features or quality, and then, like, auto-generating from that metadata file certain… things, including documentation, and I… I don't know if that is the more realistic approach for every language, but I think it is… It has proven really useful for us, so… Maybe that is a way that we could…
Ted Young 00:16:41 I have been looking at what you all have been doing over there, and I think there is a lot of inspirational work that we can apply to the other contribibs. It… but there is, like, even something that just got mentioned of, like, oh, we could, like.
move some things into core. It's like, that's specifically what the existing maintainers are like. When I was like, just the things that are de facto stable, just mark them 1.0. The instant feedback we got is, like, if I touch that and mark it 1.0, then I own it now.
And there'll be some expectation that I maintain it as a maintainer, and since I… do not want to do that. It's like… It's like the opposite of cheese. It's like the stinkiest of cheese. We thought we were giving people cheese, and we were giving them… mold, from their perspective. Like, they don't… like, they're like, we don't have time to do this. So it's like, there is this genuine labor shortage, and… and, like, I think we can have a good process that will make it more obvious how… People can contribute labor to this, but then we also have to figure out where… where we get the labor from, and, like, what… what we can offer, you know, vendors and other, you know, community organizations in exchange for that labor.
Pablo Baeyens 00:17:56 would it make sense to, instead of focusing on whatever you think is stable, back to stable, figure out what things are the most used, and focusing on improving those? We've done that to some extent on.
the collector. Maybe we have more data than other people, but, like, I think that could be a… it has proven, like, a motivating factor for people to say, like, hey, yes, I'll work on the Prometheus receiver, I'll work on the Kubernetes attributes processor, and… I don't know.
you would…
Ted Young 00:18:25 I think it's helpful, but what we're hearing from the maintainers right now, the existing SIG maintainers, is, like, they don't have the capacity, even if we were like, so just these 12 things, they'd be like, right? So I do think…
Pablo Baeyens 00:18:38 Three.
Ted Young 00:18:39 But the thing about instrumentation is the long tail actually matters to people.
Right? Like, what happens is everyone uses a core of the same stuff, but the thing is, like, everyone's system is, like, core plus one, you know? And so… At any rate…
Pablo Baeyens 00:18:59 I'm sure it has been useful to focus on just a few components, even if there is a long tail, because focusing on improving those components kind of Helps all the others, because we build common automation.
Ted Young 00:19:12 I like the idea of starting with just a subset, right? Like, just HTTP, and just the important HTTP libraries and every, like.
Like, we don't try to eat the whole elephant all at once, but I think we also need to come up with… with a more comprehensive approach to how we do it. So it's kind of both. But yeah, I agree with you, the more we make it one big, giant effort, the scarier it is to everybody, and we have to find a way to chop this up into bite-sized pieces, or we're never gonna get there.
Trask Stalnaker 00:19:54 Just, from a sort of resource… factor… Like, if we look at contribib repos… Over the last 2 years.
You know, there's definitely been… A lot, like, that has been a place where people have been pulling away from Yeah, python contribib.
Surprising, given the Gen AI.
Interest that this hasn't.
been up, but that's something that we're working on in the GenAI SIG.
net… It's good, oh, that's, JSContrib.
Marylia Gutierrez 00:20:45 Yeah, so for JS, we even… One thing that we did was, for the package, nobody was actually touching, and the code owners kind of, like, disappeared. We are marking them as, like, we are not accepting any PRs on them.
Only if the person wants to become a code owner, then they can approve. If it is, like, a more serious, like, bug fix, you can have one of the maintainers be kind of like a sponsor for that PR, and then get in. And this was a way for us not to just get drowned on stuff. Now we are seeing a couple of ticks, just because, like, AI and people just, like, finding old issues and opening them up, but we are trying to, yeah, look into that as well.
Ted Young 00:21:29 Yep.
Trask Stalnaker 00:21:32 Yeah, but, like, the… any… Amount of ideas we have for… I mean, it… it… I really do see it as a fundamentally a, A resource shortage, like, that, And so I'm not sure what we can do short of, you know, like, We can create… Yeah, like, all of these problems, these are not necessarily that hard of problems, but they require… They do require a good amount of work.
Austin Parker 00:22:12 Yeah, I mean, I think that… I think a lot of it's just gonna be scoping, right? Like, we… We do fewer things… Or are we… We try to… Focus the community on fewer things, even if maybe they're less high impact.
But, like… I don't know, just give…
Ted Young 00:22:47 So, I… yeah, that… I feel like that's a good segue into the… the next topic that I have, which is that… how we do project management. But, I see you have your hand up, Jirassi, but what I wanted to say is I feel like it's actually almost two different pools of labor. There's, like.
you know, how do we design and implement the next cool thing, and, like, do spec work and stuff like that? And, like, that's sort of one pool of… People and stuff. But then there's, like.
you know, building and maintaining all of the implementations that we have. And that… that feels like… those don't necessarily feel like the same labor pool, and that if we, like, say we're not gonna work on, like, Stefanero or anything like that, that wouldn't solve our, like, contrib… problem thing.
I think the natural course of what would happen is we don't work on this stuff.
contrib all catches on fire, it becomes public, the vendors are like, what are you doing in there? And we're like, we gotta come at, right, like, and then eventually… and then through that mechanism, we would get labor, but I don't want to go through that. So we need…
Morgan McLean 00:23:59 There's also a credibility risk with that, right?
Alolita Sharma 00:24:03 Exactly. We have seen some of that in the past.
Morgan McLean 00:24:07 at another project, certainly, yeah.
Ted Young 00:24:09 So how do we get, the… how do we avoid this tragedy of the commons and get vendors and cloud providers and other people to lean into the boring work, right, that we have to do?
Jurassi, got your hand up.
Juraci Paixão Kröhling 00:24:25 Yeah, and sorry, I joined a bit late, so I might have missed a few… a few parts of the conversation there.
But, I… there's so many, so many things to talk about there.
Ted Young 00:24:37 One…
Juraci Paixão Kröhling 00:24:40 the reason that I raised my hand was basically to call out on your favorite topic, Tad, which is project management, right? So, I do think that maintainers, we have… We know here, in this circle, but we need to, make it clearer that maintainers, they are the project managers of their SIGs. Like, they are the ones that are responsible for for the healthiness of the SIG and so on, like, they are the ones dictating or assuring the direction of the SIG, of the project, of the things that they maintain.
Nowadays.
at least from where I'm standing, the coding part is not the one part that is taking the most work nowadays. It is really determining what to do, and… steering the direction. So, the work that maintainers did last year, even.
but, I don't know, 2 years ago, is way different than what would be expected from maintainers nowadays.
I guess one question that I would have is, are maintainers Do maintainers share this vision, or do we still see… open source work as the highly rewarding stuff that we do as a hobby, because we want to, you know, exercise our brains, or is it… is it a project that is trying to solve problems for people yesterday?
I don't know, like, I think… I would love to see what is the vision of maintainers in general, not only our opinions, but what they think their work is in 2026, in April 2026, to be more precise.
one thing that I… towards the end of what you were saying, Ted, reminded me of a situation that I saw, like, yesterday. So yesterday, a company called Warped.dev, they open-sourced their terminal, their AI terminal, AI Asian terminal, or whatever they call it. And I… one thing that I found interesting was they're open sourcing, but they don't expect anybody to open PRs, not even them. Like, they expect people to open issues, and then have a discussion, and then have a coding agent to pick up from there and open a pull request, and then they just merge, like… Like… Yeah.
I don't know, is that the future? I don't know. I think I'd like us to have a conversation about that, because if the boring work Well, I mean, we can talk about tokens.
Ted Young 00:27:15 Palm OS was also trying this model.
Austin Parker 00:27:17 Yeah, so is… I think Ghosty? There's a few other projects, or…
Juraci Paixão Kröhling 00:27:22 Yeah, good.
Austin Parker 00:27:23 honesty.
Juraci Paixão Kröhling 00:27:23 I don't know, so that one was warped up now, so I… I stopped using one.
Austin Parker 00:27:28 It was a new thing.
Juraci Paixão Kröhling 00:27:29 Okay. So, but I think the, Why am I saying that? Because boring work is the perfect candidate for that kind of work, like, for that workflow.
I don't think that there is a disconnect between from maintainers not wanting to maintain Contrib, and the expectation that contrib is alive.
Pablo can probably, talk about the newest conversations there around country, but I think Last year, or 2 years ago, the discussion there was.
we are gonna kill Contrib, because it's so much work, and we expect people to build their own distributions of the collector. We just don't need… we just don't have the tooling around to make it easy for people to build their distributions. And if we make the build your own distribution the common path, then that problem goes away.
I don't think we aren't there yet, I think with the tooling of 2026, like, we can definitely build guides for people to build their tools without having to know the internal details of OCB and collector releases and whatevers, right? So I think it is doable to just get rid of contribib.
and I'm assuming that we are talking about contribib distributions here from the collector, not contribute in general.
But anyway, so…
Ted Young 00:28:50 No, but we're talking about all the content.
Austin Parker 00:28:53 instrumentation.
Ted Young 00:28:53 instrumentation.
Alolita Sharma 00:28:55 Instrumentation.
Ted Young 00:28:58 And that's, like, the part of the problem is some of the pushback is, like, if people want this shit to work, they can just deal with it, and we're like, we… we want it to work. Yeah.
Morgan McLean 00:29:08 Yeah, the project value evaporated.
Austin Parker 00:29:11 I mean, so… spitballing something, like… well, okay.
Yeah, spitballing something. Like… What if we invert the problem statement a little bit? If the problem is, like, oh my god, we have all this bespoke instrumentation that isn't in these upstream releases.
why not have, like, if we're going to throw the infinite, token machine… assume we have an infinite token machine. If we're gonna throw the infinite token machine at the problem, why… Why would we throw it at, we want to maintain our own forks of this, versus We will use our token budget to upstream these.
Ted Young 00:29:56 100%. I think it's, figuring out the tooling for making this all work opens both doors. Opens the door for us to be able to maintain this stuff ourselves, but it also makes it easier to upstream and maintain it there. But we have to figure out the toolchain first.
Austin Parker 00:30:15 M.
Ted Young 00:30:16 And maybe figuring out the toolchain is the interesting problem. I think figuring out how to leverage AI in an open source project like us, you know, like… you know, can we… can we constrain the problem enough that we don't need to use God-Emperor-level AI to manage it?
Alolita Sharma 00:30:35 Yeah, exactly.
Ted Young 00:30:36 and open LLM, to manage it. Can, you know, can companies that are invested in OpenTelemetry, like Microsoft, have, like, you know, co-pilot and things like that that they are interested in seeing people use. Like, I think there's ways to figure this out, and maybe those are, like, interesting problems for people to work on, so that makes the problem interesting again, which is.
Austin Parker 00:30:59 I do want to say, like, even, like, assuming that this… assuming that plan works, right? Like, we still have the problem of… Just because we get… you know… whatever version of whatever upstream library to… it's like, hey, now we're native hotel, and da-da-da-da-da, great, like, we will still need instrumentation for the people who are not updated, right? Like, so…
Morgan McLean 00:31:27 Or close first things.
Austin Parker 00:31:28 Yeah. Right, right, like, there's…
Morgan McLean 00:31:31 But we'll need a lot less.
Austin Parker 00:31:33 Well, yeah, over time, we'll certainly need less. Yeah.
Ted Young 00:31:36 We'll still need people to review the PRs, so there's still this late.
Austin Parker 00:31:40 Yeah.
Ted Young 00:31:40 and getting back to what was brought up about maintainers earlier, and, like, their motivations, I feel like, there needs to be more agency in terms of, like, maybe the direction of the… maybe tying, you know, contributing labor leads to more control over the destiny of the project in a way that's a little more explicit. I think we've been constrained on that, because we still haven't… we've got this final lump of stuff to get to graduation, right? Where we need to finish our original mandate, tracing metrics and logs in all the major languages and the clients, like, stable and managed and done, and we graduate.
and I kind of feel like once we get to the other side of that, it's a little more open-ended about, like, what's… What should we work on? What's interesting? What's the most important thing?
But that's kind of, like, when I think about the tragedy of the commons, I think part of it is, is figuring out how to tie those two things together more than we have. And I think our current model with, like, the GCTC kind of tightly controlling and running everything is not a model that… that… Works well with… with that approach, so… so that's an area where I would love some creativity from people about how How do we avoid the tragedy of the commons with the boring stuff, in particular? The boring but important stuff?
Don't need an answer right now, but that's… I think that's… that's the hard… that's one of the hard things. I think we can get people excited about building AI Weaver toolchain, blah blah blah blah.
Austin Parker 00:33:27 Yeah.
Alolita Sharma 00:33:28 Agree, then.
Ted Young 00:33:29 Who looks at the PRs this thing generates when it generates 50 fucking PRs across, you know, Python contribib, when we push the button?
Austin Parker 00:33:39 Yeah, the problem comes back to focus, right? Like… We can't… I mean, I think the problem comes back into focus, and it comes back to focus in the sense that, like.
Without doing something to constrain the scope of… which we already have, right? Like, we already have a… I feel like we have implicit statements about, oh, these are the things that we actually care about, but we need to be more explicit about it in terms of instrumentation, right? Like… And we need to do what needs to be done in order to make that real, like, I think…
Ted Young 00:34:30 Yeah.
Austin Parker 00:34:31 you know, I don't exactly know what that is, but until we have, like, a more firm stance, like, until we draw a… I think if we go out and say, hey, cool, here's… Here is the… Like… the direction, right? Like, here is the official ring fence around, like, this is the OpenTelemetry aura of responsibility, these are the things that we will commit to do for our users, and here are the… and then here's the things we think you should do, and here's how we're enabling you to do those. So, like, with the Weaver stuff.
For things that are, like, in Contrib, that are unspec'd, or things that are, like, these aren't really… this isn't really instrumentation that we think we should be responsible for.
here's how you, other person, would take that and do that using Weaver, using these prompts, using whatever framework we build, right?
But, like… having a really crisp way to say no, right? Having a really crisp way to say, this is in scope, this is out of scope, and here's what you should do about it, like… Would at least give maintainers slightly more confidence that they're not signing up, or that we're not signing them up for infinite spiraling, you know, complexity and scope creep.
Ted Young 00:35:53 I think we can do that. Right now, they don't want to sign up for one thing, right? Like, being like.
Just eat one of them. They're like, - nope, not even one. So… so… But at any rate, I would love… This is something I'm gonna try to work on, I would love to hear proposals for other people, because I think… I think we need to get a game plan together for this quickly, or we're never gonna graduate, because this… like, the other stuff, when I look at our graduation, like, what do we have to stabilize, how do we deal with the collector and other things, like, those are things that… You know, it's work, but we're working on it, it's just like…
Austin Parker 00:36:32 Well…
Ted Young 00:36:33 path to get there. This is the one where I… it's still kind of like a question mark of how we… how we actually do it, right? Like, we don't have a plan… concrete plan yet.
Austin Parker 00:36:44 I do want to point out, like, Just to… Make sure we're on the same page.
Like… accomplishing this stuff is not necessarily a blocker for graduation. Being able to show, like, hey, we have a plan, we're actually, like.
like, we're listening and learning and doing stuff, like, that is the, you know, thing that needs to happen. Like, we don't need to… I don't think we should rush into a suboptimal decision or whatever, simply because we think, like, oh, we need to do this right now. Like, we do need to…
Ted Young 00:37:19 Sweet!
Austin Parker 00:37:20 We need to figure out what we need to do to get that OTEP merged.
Yeah. But, like.
Ted Young 00:37:24 This is that, right? Right, like, I think it's… We want things to be stable by default, and the one big chunk of that is, that we don't have a plan for right now is instrumentation, because one thing I tried to do is, like, let's just go through and mark the de facto stuff as stable, and even that was, like… like, maintainers don't even want to do that without a plan for how it's gonna be handled. So we just need to come up with some kind of plan for how we're gonna deal with instrumentation contribib. I agree with you, like, we don't need to be at the end of that journey, but I don't see how we… we move forward with stable by default without a plan for this. It seems like the next step, I guess. Just telling people, like, go take it over or something, that's not working. There needs to be a more coherent plan for how we're gonna lower the labor costs in dealing with this.
Alolita Sharma 00:38:23 Is it the TED-only labor costs, or is it also that, as you said, you know, there is no clear blueprint for what stability, you know, actually means for… because if we make it simpler, right, it's much easier for maintainers to grok also.
Ted Young 00:38:41 So, we did make it clear we want to separate code stability from, you know, semantic convention stability, right? Like, that was a thing where we just, to some degree, missed the mark as far as, like, perception, right? Like, people perceive… the sub 1.0 as a sign that they should not run it in production.
Alolita Sharma 00:39:06 Right.
Ted Young 00:39:07 Right, and that's not necessarily what we're saying with a lot of the stuff that's in Contrib. People have been running that in production for years.
Alolita Sharma 00:39:14 Absolutely.
Ted Young 00:39:15 So why not just go through and mark all that stuff as 1.0, and then we hop to 2.0, you know…
Alolita Sharma 00:39:22 Exactly.
Ted Young 00:39:23 we bumped the semantic conventions up. And the pushback we got from maintainers is, like, who's marking this 1.0, right? Like, who's doing that? Who's on the hook? Because there's a perception on our side, if I go and mark that as stable, I am now saying I'm going to be responsible.
Alolita Sharma 00:39:42 Indeed.
Ted Young 00:39:42 maintaining.
Alolita Sharma 00:39:43 Yeah, maintaining that compatibility.
Ted Young 00:39:45 Most of these things are getting used in production, but the reality is they're, like, used couches that somebody threw on the street, right?
Alolita Sharma 00:39:52 Yep.
Ted Young 00:39:52 how much of this was, like, Datadog instrumentation that LightStep schlepped over for Datadog because they didn't want to bother, and then, like, we did it, and now, like, LightStep is gone, and, like, you know, so who's… who's doing any of this, right? So that's… that's why I see it as just kind of like a labor shortage. If we literally had people who were like, yeah, I'm fine bumping these things to 1.0, and… and paying attention to them, I think.
I would be less worried about the timeline on the tooling and everything else.
But it feels to me like if we come up with a plan around tooling to make it all simpler, that would… That would help.
Solve the labor problem.
Right? Because we aren't just telling maintainers, hey, just go… Take over this stuff.
Without any help from us, or a plan.
That's my field. I could be wrong about some of this stuff if other people have, like, other perceptions and other proposals, I'd love to hear them.
But to me, it feels like… like, let's… let's start moving fast on the stuff we've been.
Alolita Sharma 00:41:00 Yeah, I agree.
Ted Young 00:41:01 for a while, around Weaver and AI and these other things, like, it feels like those things have matured enough. Like, semantic convention tooling has matured enough.
That… that, you know, we could… We could bring it into play, and that would maybe… But the other part is, like, how do we go back to vendors and be like, hey, like… Like, if we have a more coherent plan for how we manage instrumentation as a group.
I think it'll be, like, easier to go get more people assigned to dealing with it. Because asking the community to do it because it's fun, or interesting, or, like, my hobby project, like, that… that doesn't actually align with with what we need to see here. It's literally, like, the most boring part of OpenTelemetry, and it's critical to those of us who are consuming the data and have customers, but it's not the kind of thing that's, like, fun for some, like, 23-year-old JavaScript engineer to… to do as a hobby thing.
So… Figuring out what kind of cheese, to… to bring the vendors back in would be helpful, and figuring out a more coherent plan for how we manage it collectively would be helpful. So I'd love… I love people's ideas.
Jossie?
Juraci Paixão Kröhling 00:42:26 So, what is the one thing that we see at every KubeCon that, At every single vendor booth there, like.
We support OpenTelemetry, we are OpenTelemetry Native, we support, like, we integrate with… we are OpenTelemetry native, and so on and so forth.
Ted Young 00:42:44 set that you can win if I scan.
Juraci Paixão Kröhling 00:42:47 Like, this one.
Ted Young 00:42:49 Yeah.
Juraci Paixão Kröhling 00:42:51 So…
Ted Young 00:42:53 Everyone wa- everyone says they support it.
Juraci Paixão Kröhling 00:42:56 Yep.
Ted Young 00:42:57 But…
Juraci Paixão Kröhling 00:42:57 So I think… Right, so how about we take the statistics, like, from code, from the dev stats, and we create, like, a… a seal of approval, like, a… a… I don't know, like, this is a good company in the ecosystem, like, we, OpenTelemetry, we are telling you, like, those companies, they actually help instrument the world, like, instrument… doing good instrumentation.
So, a seal, like, an official seal that we can have at the booths, and companies can have that if they get into those, specific, scenarios.
It's gonna be tricky, right? But I think it is a good incentive.
So that… and then we can tell people there, like, oh, look for… for that symbol, like, those are the true OpenTelemetry good citizens, that it should be… you should be considering in your hotel journey.
Ted Young 00:43:55 I do like that, and we could even have multiple Fancy hats that we hand out for the different kinds of work.
Morgan McLean 00:44:04 Diamond, gold, silver, platinum.
Juraci Paixão Kröhling 00:44:07 Cred the badges to companies, why not?
Ted Young 00:44:10 Yeah, no, I mean, it's… it sounds… but that's actually a great idea, Jirassi, because we need something to motivate. It can't all be just through altruism or through, like.
Alolita Sharma 00:44:19 Right, right.
Ted Young 00:44:20 Fall apart if you don't do it or something.
Alolita Sharma 00:44:21 That doesn't motivate everybody. Yeah. For sure.
Juraci Paixão Kröhling 00:44:24 And I mean, blog posts, they're fine, they're nice, they help the ecosystem as a whole, but they… it doesn't help, like, with the thing that we actually need help with, which is engineering work.
Ted Young 00:44:34 You can be the founder this year.
Juraci Paixão Kröhling 00:44:40 I want to be the king.
Ted Young 00:44:41 You're good.
Juraci Paixão Kröhling 00:44:41 And how are you?
Alolita Sharma 00:44:42 Come on, Father.
Ted Young 00:44:43 dead. I'm just staying over here.
Alolita Sharma 00:44:44 I think that word, girasi, doesn't work.
The flounders are…
Ted Young 00:44:52 We could have a flounder, like a gold flounder.
Juraci Paixão Kröhling 00:44:55 Are you?
Morgan McLean 00:44:55 It could be a.
Alolita Sharma 00:44:56 flock of flounders.
Juraci Paixão Kröhling 00:44:59 Yes. Oh, we are being recorded, so I would make a very bad joke right now.
Ted Young 00:45:03 No!
Alolita Sharma 00:45:04 Hold it back.
Austin Parker 00:45:06 I'll… I will… point out that… We will have an additional lever here with certification.
Yep. Boom.
I don't necessarily… I mean, I think there's two, like, there's… there's… So there's, like, legal levers, there's contractual levers, and then there's sort of, like… Fancy hat levers.
And one thing that we could think about is, you know, Pushing on the… like… Community awards stuff, pushing on the, like… you know, Fancy hats for vendors.
Right? Now, I think some of that does require us to be significant. I think that will require us to be a little more, like… Lever… use that sort of contractual leverage a little more.
Right? To… like, when someone says, company name OBI, To have the response be a very… exciting letter from LF Legal about…
Ted Young 00:46:25 Yes.
Austin Parker 00:46:26 I don't think you can do that! Star Fox?
Ted Young 00:46:29 I would love to get more guidance from them about that stuff, but anyways, like, let's… let's… I'm interested in what kind of hats, and badges we can hand out. I think that's a good next step. Severin, you had your hand up?
Severin Neumann 00:46:45 Now I'm muted. Awesome. I just wanted to second what Torasi said, that, like, having those kinds of batches, and I mean, the website could be a good starting point, right? We have this… very not-optimized vendors page and integrations pages, and something like that, where we definitely could… could put the ones that are good citizens at the top, and the other ones a little bit below. And so, like, here's, like… I don't know, in 2026, those companies contributed the most, or something like that.
I think the only thing I want to call out, the problem is, of course, this is a lot of marketing value, right? This is… The much harder thing to figure out is, like.
How can we encourage companies to… they're like, hey.
we contribute for very selfish reasons, right? We… we are… I don't know, picking up Python, whatever libraries, because, like, they're super important to us, like… it's really this thing, I'm not sure about how we… how we can… how… because everybody… I have the feeling everybody's right now, OTEL is good enough, right? OTEL is just… yeah, it works, right? So… and that's a problem that we have right now, right? We hit that bar where everybody's just satisfied with it, but yet everybody's complaining that, like, hey, it's not stable, it's not… whatever, and, and, and yeah, I'm, I, I'm… I'm asking the same question, right? How can we get product managers, engineers to a point where they say, like, oh, upstream contributions are in our best interest, so I don't have a good answer for that.
Juraci Paixão Kröhling 00:48:26 I think the selfish reason is actually a good reason, like, being selfish about my contributions is actually good, because then I have a… something that is important to me, and I have a business value out of that. So, we should encourage selfish contributions.
If, a specific language, a specific SIG, doesn't have a company or a selfish reason for somebody to contribute to.
Perhaps it doesn't.
deserve to leave, I don't know. I mean, let… let it just… Be run by the people who care about that.
I don't think we have… we should… Encourage companies to do things that are not selfish to them, like, let them be selfish. Right.
I do think that we can, like, I know that a lot of companies care about placing their placing OpenTelemetry at their KubeCon booths. Like, if… if what we need to… if the selfish reason is, I want to have a badge just like those guys up there, then that's a good reason for me, and it's a good way for us to use our levers, like, as Ted was saying, like, I don't see… and that could be the one way to make Ruby interesting to other companies for selfish reasons. Like, the selfish reason is I can make my contributions to Ruby, because that's where they need help with, and that's where… I mean, I can get more Java developers, but Java is already Overstepped. I'm not saying jolly's overstepped.
But yeah, anyway.
Ted Young 00:50:04 Okay, winding down, Alita, and then…
Alolita Sharma 00:50:07 Yeah, very quickly, I wanted to reiterate that, you know, from an end-user perspective, and I've been, you know, I talk to a lot of different end users, it's just that, I think there is a trade-off, Ted, as, you know, you also called out, Jurassi called out, is that where, There is a labor, you know, kind of crunch on the project, but at the same time, there's also this… anxiousness on the end users that, why does a hotel just be brave and declare these things stable, right? Because they've been used forever, and just do it. And then, if there is pushback in terms of areas that need more work.
then that is an opportunity for, you know, everybody to come in and help. And they're more than happy to help, but at least, you know, they can go and say, hey, everything is stable.
Right? So, maybe even taking a approach of shortlisting, you know, the core areas and just driving, saying, hey, we are stable, and then kind of going after the, labor retraction, you know, slash badging, etc. process may work in parallel. But pushing to stable is super important, because we are, right? I mean, we have run in, on hundreds of thousands of, you know, infrastructure clusters all over the planet, and… everybody uses OTEL, and it's just that… it is stable for most features. So how do we… how do we, you know, kind of just flip the switch in many of those areas and just say that, hey, you know, if there are concerns here, then, you know, please work with us and get those addressed.
Ted Young 00:51:59 No.
Alolita Sharma 00:52:00 I mean, I just want to make that point, because from a user perspective, it's so important. It's already, you know, the de facto standard, but we are not… in one sense, the project is very conscientious, but, you know, still, it doesn't necessarily reflect… it shows up as hesitation, more so than, you know, a lack of… Lack of, conscientiousness.
Ted Young 00:52:21 But the hesitation is there's no one to push that button marking.
Alolita Sharma 00:52:25 Yes, yes. But, I mean, maybe as the GC and TC, we can take that bold step, and then You know, face the consequences, but be also okay with facing it.
Ted Young 00:52:38 So you're gonna make the PRs, is what you're saying?
Alolita Sharma 00:52:40 Yes, I can definitely deploy some folks to make these cars.
Ted Young 00:52:44 That would… that's all we need.
Alolita Sharma 00:52:48 I've actually already been adding folks to the different segs, so people are, for sure, participating.
Marilla, if you're next.
Marylia Gutierrez 00:53:00 So on the recognition, I was actually thinking, like, the categories of recognition, so I can think, like, 3 different areas. One is, for example, end users of hotel. So they might not be the one contributing, but they're using, they are providing feedback, and that is something that we really value, so there is an area that we can kind of, like.
recognize. Second one is… like, projects, they already have OTEL on their projects.
So this helps us, because we don't have to instrument. It's already, like, they are dealing with that, and that gives us less work. So we also have a badge of, like, really, like, compatible, already, like, emitting, hotel, and stuff like that. So, also a way to, like.
remove a little of the burden for us on some of those things that people are really asking. And then the third one is for actual, like, contributors. And that one, yeah, can have, like, tiers or something, because there is no… we have to be prepared, like, if we say, like, oh, you're gonna get a badge, we might be prepared for a bunch of people just hoping, like, fixing a typo, because that counts as a contribution, and I want to have the badge. So that also should have the level of, like, okay, you had something, but, like, oh no, you were a maintainer, or you're, like, always joining the SIGs, so it should be also, like, be prepared for this The… the level of just, like, farming a badge as well.
Ted Young 00:54:29 Yeah.
I like it.
Trask Stalnaker 00:54:32 On the topic of bad, like, kind of badges, fancy hats, like, we… We kinda already have I mean, our… the main one that vendors have used in… To date, has been having approvers and maintainers on repos.
Right, like, that… that has been, I know, the main driving reason, one of the big driving reasons for, like, Microsoft and Splunk and others to, you know, is to be present as maintainers and approvers.
there's a couple problems with that today, one of which, Marillia's, work is, working towards, but that's, you know, that's still a pretty min-bar, of activity.
We… for… I've been thinking about this in the context of we are splitting out the GenAI SEMCOM, from the SEMCOM repo to its own repo.
So we're kind of rebooting that and gonna, you know, rebooting approvers and, over there.
And so I put in chat, kind of, the… and, you know, luckily, you know, in that space, we have a lot of people who want to Be involved and want to contribute, and so, you know, but still, or at least who want those badges, those hats, and so, you know, kind of put together.
You know, some more explicit guidance of what that means to continue, in that role.
Austin Parker 00:56:20 Oh…
Trask Stalnaker 00:56:21 just as a… there's the dev stat, I think both of those are good, like.
angles for, company badges. One is just kind of pure DevStatsy involvement. One is sort of we have… You know, active maintainers, approvers.
Austin Parker 00:56:41 One thing I wanted to add to what Maria and Trask said, that I don't know how much we should and or could… I don't know if I like this idea. I want to preface this idea by saying I'm not sure I like this idea, but…
Trask Stalnaker 00:57:02 Worms. Yeah, there's a lot of dragons.
Austin Parker 00:57:05 Well… So one thing that's, kind of annoying to me, actually, is that The… if people aren't aware, LF adopted the MCP, the Model Context Protocol project into the foundation, and one of the fun little tricks they're doing is they're saying, we have these working groups. Would you like to be on a working group? You need to be a member first.
Alolita Sharma 00:57:29 Yep. Yep. Whoa!
Morgan McLean 00:57:31 No…
Alolita Sharma 00:57:32 A-I-F.
Trask Stalnaker 00:57:33 I guess W3C is doing that, yeah.
Morgan McLean 00:57:36 W3C and IETF are similar, right?
Alolita Sharma 00:57:39 Yeah, but…
Austin Parker 00:57:40 Yeah, but you don't actually have to pay anyone.
Alolita Sharma 00:57:42 To do, to sit, to…
Austin Parker 00:57:43 do an IETF thing, crucially. I know.
I do not necessarily… well… I think for certain… I think if you want to be on the board?
Morgan McLean 00:57:53 W3C, you've got to pay to show up, like, I had to… when I put Google, I had to check out.
Austin Parker 00:57:58 IETF, if you want to sit on a board or run a working group, I think, you have to actually, like, be a member, but if you want to submit a propo- if you want to, like.
Alolita Sharma 00:58:06 Right.
Morgan McLean 00:58:07 tribute.
Austin Parker 00:58:08 Well, if you want to contribute, or you want to, like, get into the process, like, I think it's, like, it's not the… it's…
Morgan McLean 00:58:14 I don't… yeah, still. I'm not comfortable with.
Austin Parker 00:58:17 A lot of… right, like…
Morgan McLean 00:58:18 Yeah.
Austin Parker 00:58:18 Again, I do not know if I care for this, but… I think there is a, like… And we arguably… Arguably have some level of a sense… like, you have to be a member of… hotel to, you know, be on the GCTZ, but I do think there is maybe a… like, if we really wanted to, kind of.
do some fancy hatting. Like, we could go and say, like, okay, here's the, like… you know, start tying some of this stuff to it, like, start basically saying, like, hey, you know, you have to be, like, a CNCF member.
Right? To be, like, here's… the releases working group, or the production readiness working group, or I don't fucking know, right? Like, I don't, you know, pick, pick something, but say, like, put a very clear, like, hey.
You're paying for this, and if we attach, like, it to the financial incentives that they're already… like… people are already essentially paying for this, then, like, by kind of, like… it's the whole, like, why you don't just give away free tickets, right? Like, you charge a nominal amount for the ticket to your free event, because… but, like, people then have a stake in it, and they're more likely to show up, even if it's just, like, 10 or 20 bucks.
It's that kind of, like, mental thing of saying, like, well, hey, yeah, you've, you've, you've… You've paid for a mission, so… Take the ride.
Ted Young 00:59:59 Yep.
Austin Parker 01:00:00 And I get that we need time, but by attaching… so by… but that… using the kind of money that they're already paying as the carrot, then, like, it helps… it's… it changes the conversation a little bit, right? Like, it's more of, look, you're… here is your benefit.
And you need to invest time in your benefit to actually, like, Get something out of it, Right?
Yeah. And… You know, I don't know, again, spitballing.
Juraci Paixão Kröhling 01:00:31 I have no idea what spitballing means. I'm really gonna Google that later, I suppose. Askball.
Morgan McLean 01:00:37 Brainstorming.
Juraci Paixão Kröhling 01:00:39 Okay. Growing space.
Ted Young 01:00:41 spaghetti against the wall. It's like…
Alolita Sharma 01:00:43 It's like…
Juraci Paixão Kröhling 01:00:44 I had to imagine…
Alolita Sharma 01:00:45 Yeah.
Juraci Paixão Kröhling 01:00:45 I had a picture of a cat, spitting…
Morgan McLean 01:00:49 air quality.
Alolita Sharma 01:00:49 Airballing.
Juraci Paixão Kröhling 01:00:51 No, that's what I had in mind.
Alolita Sharma 01:00:52 I see.
Ted Young 01:00:53 You're not.
Juraci Paixão Kröhling 01:00:54 But anyway… Okay. But I think, on incentives, I do feel like they are paying… so companies are paying, the salaries of the engineers working on instrumentation already, and we don't have to make it complicated. We only have to create one badge for one thing only. And the one thing that we started a discussion with was we need people to care about instrumentation. All right, so let's take a list of SIGs, let's look at which SIGs we want people to be… are attracted to, and then we create a badge for contributions on those. We need a badge for Like, a low… a higher level badge, perhaps as well, like, the top 10 companies get a special badge, or the companies with more than 1,000 contributions, so that we don't have a limit on the number of badges.
Then, those get a… those get the right to have a badge at, at KubeCon, or marketing materials for one year, or whatever. Like, let's make it simple for one badge and two badges, just to get the initial contributions and see what it… where it works.
no legal requirements, I mean, let's, just if you quote somebody from the other call, let's get shit done, only, like.
One thing small, and then we iterate.
Alolita Sharma 01:02:10 But you can generate a thousand… AI-based PRs.
Juraci Paixão Kröhling 01:02:16 I mean, it's hard to get them merged, I suppose.
Marylia Gutierrez 01:02:19 Yeah, more than PR is not open.
Austin Parker 01:02:22 I gotta bounce, folks, so…
Alolita Sharma 01:02:24 Yes, yes. Take care, take care. Thank you all. Bye.
