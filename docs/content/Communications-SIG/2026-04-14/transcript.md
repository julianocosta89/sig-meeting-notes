SIG: Communications SIG
Date: 2026-04-14
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/-hhs8pECbRrlXcrnpRhfOIbYbMU4vSIJEm4qKkoQcIWllEr0WlGAlm_cetkMmg0r.Um2WFUXDzs9jrJT2
============================================================

## Zoom Recording Transcript

**Patrice C (CNCF)** 02:07 Hey, how's it going?
**Vitor Vasconcellos** 02:09 Dang.
I'm going fine, and you? How's it going?
**Patrice C (CNCF)** 02:13 Good.
Are we expecting this to be a quieter meeting?
**Vitor Vasconcellos** 02:30 Beautiful, let's see.
**Patrice C (CNCF)** 02:39 Do we know, is the meeting transcription expected?
Or is that part of the… I guess it's okay.
Do we know if Severind is gonna be joining?
Hi, Jay.
**Vitor Vasconcellos** 03:46 Yup.
**Tiffany Hrabusa** 03:52 Hi, folks. I have a bit of a headache today, so I'm gonna keep my camera off so I can squint at all of you instead of smiling.
**Jay DeLuca** 04:01 I'm getting over something, too. I've been down for the count for, like, a week.
**Patrice C (CNCF)** 04:10 Well, I hope… sorry to hear that. Hope you both get better.
Even better.
Nice of you to be here. Do you… do you know if Severn is gonna join?
Who wants to lead? Anybody in a lead?
We don't seem to have anything.
**Tiffany Hrabusa** 04:28 I haven't heard from someone, so I don't know if he's pointing or not.
**Patrice C (CNCF)** 04:32 I'll… I'll assume not, given how… Busy.
Yes. It might be a really short meeting if I judge from the empty topics list.
But otherwise… Open the floor to… Questions or comments?
**Tiffany Hrabusa** 05:02 I can give a quick update on the collector docs refactoring. Super.
Made a little bit of progress, and it's been kind of serendipitous. People have been finding issues in the docs and reporting them, and hopefully they will actually be fixing them.
Sophia has put up a PR, so I've reviewed that. I had to adjust the dates for our milestones, because we blew past the Phase 2 milestone about 2 months ago.
And we're already 10 days overdue on the third milestone. So, as is typical for open source, things moved slower than anticipated. But, we are making progress, so hopefully, We can actually… Have something to show for it by the end of this year.
**Patrice C (CNCF)** 06:05 Great, thank you, and moving milestone dates is totally okay. I had been checking out the milestones, and it had noticed the dates, so I wasn't sure whether those milestones were being used or not, but… Good to know they are.
Speaking of the collector.
Vital, are you still interested, available to set a collector up so that we can use it as a target for observability of the website and whatever else Do they have one for the dem- or they must have one for the demo.
Do you… does anybody know?
Vital, maybe you could check with them to see… to see what's set up, but it would be nice to have one for us. Maybe just quickly, I can mention that I've… been looking into… Observability for the website.
With respect to… resources, because of course, we have analytics set up, and analytics works for HTML pages when they're visited, but not for other Resources, and now that we're… the website is going… is, agent-friendly.
and we're serving Markdown format for pages, then… we needed an observability… observability in terms of access to those pages. Netlify has basic observability, but that's kind of our backup. So, essentially, I set up as, some of you know, an edge function so that we can emit events. Right now, it's going to analytics just because that's convenient, and we have a public console for everybody, but I would love to be able to emit to a collector once we have that set up. So, I wanted to get a feel for If you had an idea of a timeline, maybe just confirming that Whether or not you think you can work on this, or whether you've started.
**Vitor Vasconcellos** 08:26 Yeah, I didn't know about the demo collector, I will take a look on that, but I assume I need to open an issue in the community repo? I guess.
Austin had mentioned that we can… have this collector on Cloudflare, or… Yeah, so I will open that issue, and just to… I don't know how to get access, or how we can actually… deploy the collector there, but yeah, I will… I will take a look on that.
I have some free time this afternoon, I… yeah, I… I have some free time this afternoon, so I can… I can take a look at it.
**Patrice C (CNCF)** 09:13 Great.
Okay. I mean, we've… we… I don't know if you know the history, there was a collector.
I can't remember which… whether it was… well, it was Honeycomb at some point, but prior to that.
it was… Hosted somewhere else, or, or… associated with… with the company. And then Austin left, and so that collector, we kind of lost, and then… So, it would be nice for us, for hotel comms or OTEL to have something hosted that we can use. It's been a while, so if it takes a while to set up, that's fine. If you take more time to Make sure we make the right choice in terms of infrastructure, and where we're running.
and make sure that it's easily accessible to all maintainers, I think that's worth it. So speaking to the demo folks would… would be… would be a good idea, to see what sort of experience they have. I'm kind of, curious about Cloudflare and how we can set things up there. So, if all things equal.
turn out to be equal, then maybe let's try out Cloudflare if… You also feel that as well.
**Vitor Vasconcellos** 10:36 I didn't see Cloudflare as an asset in the community repo, so I'll raise more details on that also.
**Patrice C (CNCF)** 10:44 Okay, great.
**Vitor Vasconcellos** 10:46 Is it something new.
**Jay DeLuca** 10:50 I, I'd be interested in helping out, too, eTor. Like, if you have PRs and want to add me, or… brainstorm or anything. Okay. Because I'd like to, at some point, also… Use, like, the new OpenTelemetry browser instrumentation for the Explorer site.
And so we'll need somewhere to send that as well, so… It'd be good to be able to piggyback on that.
**Vitor Vasconcellos** 11:14 Yeah, less than this.
**Patrice C (CNCF)** 11:16 Would it be worth… opening up a Markdown project file.
somewhere, maybe on hotel.io, to track… brainstorm.
and whatnot. I guess my question was, if we do track this, where do we want to track it? Is it on hotel.io?
Or community, or somewhere else.
Whatever you choose, Vital, choose something, but let us know, so… so I can keep up to date, and Jay can follow, and… Great.
Thank you.
Any, updates on the Explorer? And.
**Jay DeLuca** 12:01 Yeah, I was gonna say I could give a… Some kind of Impromptu update. Let me share my screen.
Yes, we've been making a lot of progress. I don't know, if you guys have Taken a look at the site recently, but… I've done a couple iterations of some UI touch-ups. Still, I don't… I kind of feel like maybe this feels very, like, LLM vibe theme, and I would love to get, like, other designers in to help us touch that up eventually, but… I think it works for now. But as of now, we've got, pretty much the Java agent pretty much completely mapped.
We've got, the ability to look at the… all the information, the semantic conventions that they emit.
We got the telemetry, we could see it based on different configuration options, what you get. So we got most of the… Most of the features that I had built out in the proof of concept are now, functional. We still have a few things left. I've created… A milestone.
for an MVP launch, and I've started putting some issues in there, And I also created a tracking issue, just like a meta issue as well, for launch prep or something.
MVP launch.
So yeah, my goal right now is to try and get this at a point where we can do, like, an MVP slash GA, you know… I dare to call it 1.0, but, like, an initial… push of this. I was… I was aiming to do something by the end of this month. I don't know if we'll get there or not, but that was kind of, like, my goal.
But yeah, so we're getting close. In terms of, follow-up work.
I'm also going to be creating an LFX, mentorship proposal, project proposal, to have, some work, some help on this in that space, too.
Got a couple different ideas, whether it's mapping another ecosystem, like the Gen AI ecosystem.
or helping create, like, the ecosystem onboarding guide so that other ecosystems have a kind of a well-laid path they can follow to get in. Those are just some ideas. But yeah, so that's kind of where we're at. Also, I don't know if… along with the Java agent functionality, the only other real piece of functionality that I'm hoping to incorporate into the GA is this declarative configuration builder, which basically allows someone who's using the Java agent to come in and be able to say, oh yeah, I'm using HTTP, I'm using this library, and it basically builds like a… skeleton configuration file, now that declarative configuration is, stabilized. Just gives, like, another UI builder for someone to be able to onboard and explore that. So between the declarative config builder and the Java agent, those are kind of the two functionality pieces that I'm… I'm kind of saying, like, once we get those done.
We'll kind of release it and say, like, here's the initial Explorer, and then, you know, there's a ton more work to be done from there, but… Yeah, and then the only other, kind of update I have is, Severin also put me in touch with, the guy who runs this OTEL Starter website, which is… has a lot of similar… kind of goals, I think, of its, like, it gives people a lot of information on getting started, with configuration options, things like that. So I'm not sure exactly what the… crossover will be, but we're looking at whether we can integrate, or work together, or, you know, crosslink. I don't know yet, but the main point is we're… we're looking into it, and I think that this… there's a lot of really cool stuff here, and it'll be awesome to have, kind of, as part of our… you know, revamped OpenTelemetry, dynamic, dive-deep documentation type stuff, so… Any questions on any of that?
**Patrice C (CNCF)** 16:34 Very cool. Thank you.
**Jay DeLuca** 16:37 And we've got a bunch of new contributors, too, which is awesome. Prateek, who's on the call, is one of them. So, super stoked to have other people helping out.
**Patrice C (CNCF)** 16:46 Okay. It sounds like Hotel Starter is complementary, or… that's certainly.
**Jay DeLuca** 16:52 Yeah.
**Patrice C (CNCF)** 16:53 looking at consolidating, that's great as well.
**Jay DeLuca** 16:58 Yep.
hepatic.
**Patrice C (CNCF)** 17:03 Yes, questions?
have, high… Have… have you, used analytics? Are you gaining any insights, or… if you haven't, that's okay, but I know now that they're set up, I was wondering.
**Jay DeLuca** 17:19 I did… I did, like, I have a bookmark, and I'm checking it… I'm checking it. I don't think that there's enough… I think the only… the only interesting signal right now is whether anybody, aside from me, is looking at it, and it seems like there is. Not a ton, but there are. But I think… I think it will be interesting over time, especially after we start, evangelizing it. Oh, and another update, too, is I'm also… working on a blog post. I have a draft done, Tiffany's already done a pass on it, Severin and I think Pablo took a look as well. So just kind of introducing this and telling people what it's all about, how they can get… it's mostly about how people can get involved.
And so, I'll have that out in this coming week, I think.
**Patrice C (CNCF)** 18:05 Great, great.
In terms of analytics, since I've been working in that space.
is it satisfying your needs at this point? Even though there's not a lot of traffic? I guess it's answering your basic question of, is anybody else showing up? And, Don't know if you're…
**Jay DeLuca** 18:24 I think, I don't know, because I haven't… I'm not super, deep into Google Analytics, so I don't know what I can and cannot get. I think that I have some… some wants that maybe I can get. If not, I'll circle back with you. Okay. But yeah, so, to be determined, I'll do some digging further.
**Patrice C (CNCF)** 18:42 Good.
Sounds good. Can you remind me… if… And what the plan is relative to the registry.
**Jay DeLuca** 18:54 Yep. So, we have, I have an issue in the backlog.
to do kind of a research spike on this. But yeah, essentially, like, there's… I think there's two… there's an area where the new registry works really well, and that's basically the fact that it's all automated. Like, there's no human intervention needed, it automatically updates with version… version updates. I think… you know, the… the V1 registry is entire… almost entirely human-contributed, and there's gonna be a lot of areas of the community that we're gonna need that for, so I… I think, like.
I don't have a fully fleshed-out vision so far, but I could see us basically all the automated registry scraping information can be done with the Explorer, whether it lives in the OpenTelemetry I.O, repo, or the Ecosystem Explorer repo, or another repo, I don't think it matters as much. But I think, like, what you guys are, or what exists in the V1 registry, where it's kind of… third-party friendly, non-OpenTelemetry native, or not native, but OpenTelemetry first-party stuff. Like, I see that being further invested in, in the V1 sense, Because another thing is, like, the Prometheus community has reached out, and they would love to be involved as well, and… but they don't have, like, a central repository.
**Patrice C (CNCF)** 20:24 floor, or…
**Jay DeLuca** 20:26 With the Explorer, yeah.
**Patrice C (CNCF)** 20:27 Okay.
**Jay DeLuca** 20:27 So, yeah, they were thinking… they raised it with Pablo and Severin and myself, and… we were brainstorming the idea of, like, it could be the OpenTelemetry Ecosystem Explorer, but it's not specific to the OpenTelemetry ecosystem. It's like… You know, it's just an observability ecosystem from OpenTelemetry.
And we can expand it to, like… and I think we need to limit the scope, but Prometheus feels like a potential good synergy there. But, you know, we have a lot of boundaries to set and scope to figure out over time, but at least that's my initial brain dump to your question about the registry. I don't know if that… Oops.
**Patrice C (CNCF)** 21:07 It does, thank you very much. I guess I'd like a reminder, or I'm curious, has a decision been made in terms of phasing out V1 Of the registry or not.
**Jay DeLuca** 21:20 No, not yet. I think we're… we're still pretty far away from… from something like that.
**Patrice C (CNCF)** 21:25 Okay.
What… In terms of, first official release of the Explorer.
Is there… Have you thought of a next step in terms of Cleaning out.
the registry? If they're… I don't know, is there any overlap now, or is it just not… they're just completely disjoint? I don't… I'm not familiar enough with the…
**Jay DeLuca** 21:53 there's minuscule overlap. I think the registry… the registry has the basic information for all of the instrumentation packages, but it doesn't have any of the deep dive of, like, telemetry and semantic conventions, things like that, but I think I don't know if… I thought… Vitor, I don't know if you used a script for that or something, but it seems like we have… Most of the base, bare-bones information, like the name, the repository, maybe a description.
But that's pretty much the only overlap that I've seen so far.
**Patrice C (CNCF)** 22:26 Okay, if we don't have an action item at some point, maybe that could be a first next step after the official release, would be to at least look at eliminating the delta, so that people don't… So that if they go to the V1 registry and they don't find it, we can have a pointer that says, by the way, we have this amazing explorer, please make sure you go check there for that. So I'd like to get rid of that overlap, if it makes sense, and then later on, once we have more experience, we can decide What the fate of the registry is overall.
**Jay DeLuca** 23:00 Yep.
**Patrice C (CNCF)** 23:00 Okay, good. Thanks. That gives me an idea.
**Jay DeLuca** 23:04 Yeah, no problem.
**Patrice C (CNCF)** 23:08 I don't know, Vital, did you want to… If you had an answer to that question, or…
**Vitor Vasconcellos** 23:13 No, no, I was gonna say that I haven't used any script, I just ask it to… for cloud to… to make a sync, and… remove the… I mean, not removing, because onset package from the registry is invalid, we will catch that in the half-cache update.
But I just ask it to… to sync, and… find the… The… the packages that are in the… Collector repos, but aren't in the… like, in the contrib… repos, but aren't in the registry, for example.
We don't have a script for that, as far as I know.
**Patrice C (CNCF)** 24:01 I thought we did have automation in terms of at least bumping up versions and all that, but maybe that's not what you're referring to.
**Vitor Vasconcellos** 24:08 Yeah, we, we do.
For… to bump the versions, but this script doesn't add the new… the new instrumentations, or the new… Okay.
**Patrice C (CNCF)** 24:22 Good. Thanks.
**Tiffany Hrabusa** 24:27 I have a… Oldie but goodie.
Topic. So the… Collector release happened yesterday, and yet again, there were some hiccups along the way.
Which required them to immediately release, a patch, I guess. I'm not really… it's not technically a patch, they just had to bump the tag, I guess, to a new number. Yeah. And that breaks our automation for updating the release numbers, so I don't know if anyone has it… has time in the near future to figure out if there's a way that we can… somehow… dynamically update based on what the actual tags are. It's not… it's not an easy problem to solve, for sure, but I just wanted to raise it again since it happened yesterday.
**Patrice C (CNCF)** 25:23 Thanks. We do have an issue open, right?
**Tiffany Hrabusa** 25:27 Yes, yes, there is an issue open.
**Patrice C (CNCF)** 25:29 Concerning specifically the granularity of… version bumps, I believe, as well.
**Tiffany Hrabusa** 25:37 Yep.
**Jay DeLuca** 25:37 Is the problem that it's bumping it to the… The first one, and it, like, it's not taking the patch one into account, or… Like, what didn't work about it?
**Tiffany Hrabusa** 25:47 Yeah, so we use cascading, automation on, like, the collector docs landing page, and the problem is that there are several different artifacts in every collector release.
And so, when something breaks during their release process, some of those artifacts might end up with a different release tag number than others. And so… we… it… and it's… it's never the same on the facts, so it's like… I don't know if there's a way to automate that, basically. It… it's really tricky.
**Patrice C (CNCF)** 26:20 Well, I would say, I think we can probably automate it. The source of the problem to me is that we don't have enough granularity In the way we model version numbers for components.
Would you agree with that, Tiffany?
**Tiffany Hrabusa** 26:35 Yeah, I think that's fair.
**Patrice C (CNCF)** 26:37 So, so if we refined… The way we represent the collector components and their versions.
this problem would go away. I believe that that's the solution.
Does that make sense, Jay? Do you understand the… Gist of it.
**Jay DeLuca** 26:58 Yeah, I need to look at… because the reason why I'm asking is, I have automation for the collector sync.
That works separately from all of this.
And I'm wondering if it suffers from the same problem, or if it already fixes… Is it… Because I'm updating a data file in the… it's like the data slash collector.yaml with the updates, and I'm just trying to look at how it works, If you have the issue, I can take a look at what the problem is, maybe I have some ideas.
**Tiffany Hrabusa** 27:32 Yep, I'll find it, and I'll add, I'll add links to… there were two PRs yesterday, 0.150.0 and 0.150.1.
And then I'll also link to the, the Slack thread for the release, just so you can see what kind of problems are coming up, because it happens a lot, and it's never the same. But yeah, I'll link all of them in the issue, and then I'll link the issue here.
**Patrice C (CNCF)** 28:01 Could you… could you put it in the meeting minutes? I just created a…
**Tiffany Hrabusa** 28:05 Yep, that's it.
That's what I meant.
**Patrice C (CNCF)** 28:09 Okay.
Thanks for looking into that, Jay. Any insights?
I don't think it's hard to do, it's just finding the time to do it among juggling other priorities.
Anyone else?
Any other topics?
Question, Vitor. I think at some point you had… Potentially volunteered for working Some get started material.
**Vitor Vasconcellos** 28:53 Yes…
**Patrice C (CNCF)** 28:56 Although, I guess we do volunteer for all sorts of things, and then our heritage shift, and I, Jay and anybody else on the call, if you are involved, if that's still the case, I just wanted to remind you that, we have a new version of the code excerting tool, which synchronizes… automatically synchronizes… will pull out excerpt code bits from your source codes and embed them in code blocks. It does that automatically.
The tooling is very sophisticated. You could tell it… well, you put tags in the docs, but you can also use regular expressions to say, skip the leading comment, go from here to here. Oh, by the way, unindent, remove this, replace this. There's quite a bit of capability, which is really good for getting started and, Tutorials, which is what it was partly originally built for.
or from. So, just wanted to let you know there's a new… it's an NPM package right now, so it's real easy to install. No other… funky tooling dependencies. I'd be glad to help anybody who wants to just maybe have a 15-minute coaching in terms of what they can set up, or give feedback on PRs.
So, that's why I wanted to let you know about the new tool.
Jay, I have something…
**Jay DeLuca** 30:20 I, I actually have a PR up that uses it, I think. Okay. But one of the things that I was, Gonna ask was… So the problem that I've seen with that is that, or not problem, but one of the things that comes up is you pin the tag in the git submodule.
That you then use, and then… whether it's updated automatically. I think that there's some automation that's updating specification repo, Potentially.
**Patrice C (CNCF)** 30:55 Yes.
**Jay DeLuca** 30:56 Right, and so… I'm also working on another… PR that's gonna use, the OpenTelemetry configuration package, Git submodule, and then use code excerpts and all that. But we wanted to make sure that it stays up-to-date, and so I was gonna look at either piggybacking on the specification one, or just looking at how it's done, but I was just curious, when you said that, I think you mentioned that you did work on that lately, if you have any, opinions on whether we should auto-bump those, or if we should just have it selected, and maybe we can annotate the source code or something that indicates which ones are automatically updated.
Yeah, just curious your thoughts, because that's something I was thinking about recently.
**Patrice C (CNCF)** 31:41 So we have a data-driven script that essentially… well, it doesn't matter. We have automation in place so that you can say that periodically check the freshness of any given repo, and if it's updated, then submit a PR.
We can automate it, and with… now that the tooling has been updated, and that the checks For the freshness of the code is being done, within the CI, the PR checks, then… When the repo gets updated, we can know whether the code has changed, which is great to know, and then if you're a custodian of those pages, then.
**Jay DeLuca** 32:25 You'll get added.
**Patrice C (CNCF)** 32:27 Right, so what we can't do is just fully automate the bumps and then We can't get resolution of, if the code changes, what to do with it.
**Jay DeLuca** 32:38 Right.
**Patrice C (CNCF)** 32:39 but I guess, yeah, so that's it.
**Jay DeLuca** 32:44 Does that… Okay.
**Patrice C (CNCF)** 32:45 Clarify the scope.
**Jay DeLuca** 32:47 Yeah, I think… yeah, it answers my question. I think, so, for what I was looking at, I think it makes sense to automate it, but… I don't know, that's a blanket statement across the board, necessarily, if there's, like, a particular source code that we're not going to be able to get.
validation for. I don't know if that's the case or not, but… I think you answered my question as to, like, how to think about it.
**Patrice C (CNCF)** 33:10 the.
**Jay DeLuca** 33:12 Cool.
**Patrice C (CNCF)** 33:13 extraction tool, if you don't use regular expressions to find things, you put tags in the code itself.
And the reason you embed tags in the code itself is so that whoever's updating the code will know to adjust the tags. Now, if developers do that.
then the automate… then the… it'll be trivial to review the PR once it lands, because you as the developer can just say, yes, I know, I made the changes, and The code snippets should update in the docs.
So that's kind of the workflow once you start using tags in the code.
**Jay DeLuca** 33:52 Yep.
Makes sense.
**Patrice C (CNCF)** 33:57 Sorry, Vitor, I kinda…
**Vitor Vasconcellos** 34:00 No, no, that's okay. No, I was just going to mention the getting started. I don't think I'll have time for that, but I'll be happy to add a markdown file with the prototype and raise a pull request in our repo, and… If someone wants to take that, or if this is something valuable for us, if we are willing to… To work on that.
Later… I don't know, later this year?
I can… I can write the ideas, and… my thoughts, and… We can track that.
**Patrice C (CNCF)** 34:38 Great.
I know there's ongoing effort to rework getting started overall, I have no idea what status it is.
And whether that was specifically the area you were working in, or whether you have thought about something simpler, which is the current current way that the pages are set up, but I know Severin has been Pushing for a… reorganization there.
**Vitor Vasconcellos** 35:10 There's… there's a project in the community repo, I guess.
he also shared that. I'm not sure if this is something that is already… In progress, or… Okay.
But, yeah, we can… we can… Definitely.
**Patrice C (CNCF)** 35:30 figure it out.
**Vitor Vasconcellos** 35:30 the ideas, yeah.
**Tiffany Hrabusa** 35:33 Yeah, if I remember correctly, the last… Severin had written, kind of, a blueprint for how he wanted the new Getting Started Guide to go, but then we needed… developers from each language SIG to implement the application in their language, and so that was where We kind of hit a… a roadblock.
**Patrice C (CNCF)** 36:01 And I guess it's a question, it may be of one language to be the first, get things started.
**Tiffany Hrabusa** 36:06 Yeah, yeah.
**Jay DeLuca** 36:09 I think… and we have a Java examples repo, and I think we have an issue open from Severin.
Asking us to create… An example following some… some guide.
So I think someone went out and opened issues in at least some languages asking for it to be done, but I don't know who's… Who may or may not have, actually done it.
**Patrice C (CNCF)** 36:35 So, Vital, was your work within that?
space for…
**Vitor Vasconcellos** 36:41 No, not actually. It was just a prototype and just some ideas, nothing…
**Patrice C (CNCF)** 36:48 Okay.
Maybe then speak to… if you want to catch up on the context, if you're not familiar with the context in terms of the… getting started proposal.
ask Severin, or if he's too busy. Tiffany, I think we have a document.
somewhere, or, you know, more than a document. They're… they're PRs and issues and documents. Yeah.
**Tiffany Hrabusa** 37:11 Yeah, somewhere there is… I remember reviewing it, I can dig it out.
**Patrice C (CNCF)** 37:17 I totally agree, Jay. That would be a great idea.
Are you involved with that?
Effort?
**Jay DeLuca** 37:29 No, I just saw them. I just saw talking. Was it… Devrin and Vitor, are you also involved with the Bloomberg Group?
**Vitor Vasconcellos** 37:37 Yes.
**Jay DeLuca** 37:39 I was just, yeah, I was just thinking that maybe… maybe they could help with the various getting started in each language, or… I don't know if you guys have enough… You know, stuff for them to do yet, but just an idea.
**Vitor Vasconcellos** 37:52 Yeah, that would be a great effort to start, yeah.
If we could start this in the program and keep going afterwards, we can also… have new contributors, you know?
Yeah, that would be a great idea.
**Patrice C (CNCF)** 38:09 Maybe to make things more concrete in terms of progress.
Could we choose a language? The first language? A language?
And work through that, and that would also give focus, if ever, to Bloomberg Contributors, need guidance there.
Java seems to be in the lead for quite a few things.
Do you have any idea if the Java folks might be interested there?
**Jay DeLuca** 38:45 Is… when you say interested there, do you mean in writing the examples, or kind of helping shepherd like a… a Bloomberg contributor.
Do it.
**Patrice C (CNCF)** 38:57 Cool.
both. I guess my under… I thought… I kind of got the feeling that the example existed already. So, in terms of the Bloomberg effort, it might be Making sure and refining the example, fixing… working on the example, and then… The comm… the hotel comms part is for us to Create the actual… Documentation pages that cover that example.
**Jay DeLuca** 39:23 Gotcha.
**Patrice C (CNCF)** 39:24 So… I would love to see both, if somebody can make sure that the example's ready, but of course, bringing it in to Have it documented so that it's actually used would, be helpful.
**Jay DeLuca** 39:39 Yeah, I mean, I… I… I put a link to the issue there. We can see if someone from Bloomberg is actually interested in writing the example. If not, that's something that I could either help with or find somebody in Java to help with, and then once we get that, then, you know, I could help.
Review the final or new documentation page.
**Patrice C (CNCF)** 40:01 Great.
Thank you.
Dude, but that's my document.
Any other?
**Tiffany Hrabusa** 40:18 Sorry, I linked the project document that, I think Severin created, but I feel like there was also a PR out there that I think he closed at some point, so I'm gonna dig that out too, just so you can see.
Where he was going to.
**Patrice C (CNCF)** 40:34 Right. I do vaguely remember that as well.
**Jay DeLuca** 40:39 Just as a funny aside, it looks like in September of last year, Trask asked Copilot to create this, this example, and it failed miserably.
Be interested to see Trey again.
**Patrice C (CNCF)** 40:57 I guess, I mean, that's another incentive, is if there is a… first crafted example for one language. It'll be way easier.
**Jay DeLuca** 41:07 Yes.
**Patrice C (CNCF)** 41:08 To get some agents to produce… to work on the other languages.
**Jay DeLuca** 41:14 Yeah, that's a good point.
**Patrice C (CNCF)** 41:14 merchants, yeah.
Any other topics?
I have one, but I'm… Willing to wait to see if anybody else has anything.
On the topic of AI, How's it going? What tooling are you using? Is it working? Is it not working? I mean, I've certainly been going through experimenting and seeing what… slowly getting into a figuring out what works for me and doesn't. Vitar, you were bringing in what are they called? Agent skills?
Is, is, for the website? Is that it?
Could you give me, like, a 2-minute elevator pitch for what that is and why it's helpful?
**Vitor Vasconcellos** 42:18 Yes, the skills… we can use it to automate Basically, to automate the… the work we are… I'm looking on the contributor side, I think we can also have skills like… to… Navigate through our docs, and for end users, like, they were… they are willing to, I don't know, understand how to instrument an application or to set up a collector. We can also have those skills To teach the agents through the skills to navigate in our website.
But… I'm… I've been using to… to automate my… my work anything that I can, basically. Like, I was… I was updating the drift… the drift status.
early this morning, and this is actually a skill we can… we can add to… to run the… the NPM comments, Validate the pages that have been drifted, and… push the branch and open the PR, basically.
Or, for example, also writing the internal docs. We… the maintainer docs that we… we have, like, to explain the workflows, or… Or… tasks like that, but we can… explore in… many ways.
I'm still trying to learn on, basically, why I've been using, and I've been using cloud for… most of my tasks, I'm no longer using Cursor, and one of my concerns was that Cloud has some very specific vendor-related Configurations and setup, and one of my concerns was… If we are not… creating a vendor lock-in, but then Faber mentioned that some other toolings have Are… have compatibility to… with this… this… this setup, so… Which one are you using, by the way?
**Patrice C (CNCF)** 44:41 I'm using as many as I can in rotation, but in terms of the vendor lock-in before.
I'll answer your question more specifically after. Is it because you're encoding things in a file named claw.md? And if so, could we just use agents.md?
And then, yeah, I'll let you answer.
**Vitor Vasconcellos** 45:06 No, no, it was… we're on the… I think we have some, like, the weekend… Create a set of rules for sub-agents.
Got it. But I don't see this works, for example, on Copilot.
So, I'm afraid we… we will create a skill that will ask to use a sub-agent, but Copilot won't be able to read that, for example.
**Patrice C (CNCF)** 45:35 Got it.
**Vitor Vasconcellos** 45:36 Because Copilot doesn't know what is that sub-agent.
Just… just an example of…
**Patrice C (CNCF)** 45:45 Okay, that makes sense.
**Vitor Vasconcellos** 45:48 But yeah, we also have the cloud.club folder, and the cloud.md, and all the other…
**Jay DeLuca** 46:00 I had similar thoughts.
**Patrice C (CNCF)** 46:02 Go ahead.
**Jay DeLuca** 46:03 about, like, skills, for example, like, I create them under, like, the .clawed folder, and I've wondered if… If that makes sense, or if that's too… vendor lock-in. And yeah, the co-pilot thing is a pain, that, like, if you wanted to be able to reference things, it, like, has to be in a specific… location.
but it's odd, because I would think that you would be able to tell it to reference Things elsewhere, but, like, documentation seems to be conflicting, about that, but… But yeah, just want to say I've had similar kind of brain thoughts around that, but it feels like… Claude is pretty ubiquitous in terms of what people are using Locally, at least.
a majority, maybe? But I, personally, I've been using Copilot just in the web UI. Like, before I open a PR, I guess a primary repo, I'll open it in my fork, have Copilot do a review there.
Before I open the PR proper.
**Patrice C (CNCF)** 47:08 Makes sense.
**Tiffany Hrabusa** 47:09 I've been using cursor.
With, anthropics… Opus… Llm, and I use it I'll, give it the URL of a PR, and I've created… I've created a workspace for my Grafana repos, and then I have a workspace for my OpenTelemetry repos.
And so, from within that workspace, I just say.
okay, based on the changes in this PR, what, what documentation needs to be updated? And it, like… explains to me what the PR does, and then, I tend to make it suggest before it makes changes, because I'm not really happy with how it writes things.
But it, it usually finds, areas, like, hidden corners of the documentation that I forgot existed, and it, it, It reminds me to update those, so… I don't know that it's made me all that faster, but I do think that overall, as… especially for the product I document at Grafana, which, when I first started.
It was a very small dock set, and it has grown quite a bit.
my mental model has not kept up with the growth, so I think it's definitely improved my ability to keep the docs updated, for sure.
**Patrice C (CNCF)** 48:42 Have a great… Thanks. I also use Cursor as a main environment, and it has access to the various models, but, I've tried using Copilot.
from the web, for example, to give it a prompt and say, submit a PR for this and this and that, but I find the interaction is just too difficult.
offering feedback on a PR is way slower than just jumping into the code and saying… doing immediate changes before submitting the PR from a local workspace. So I've been working locally, but I use, Codex?
On the side. So I kind of use 3 agent, three different services in a complementary fashion, but I'll do most of my development locally in cursor, and I love the tab completion and the suggestions. That kind of speeds things up a lot. And then I'll use codex on the side to say, review the changes in this PR branch. Here are my criteria. Is there self-consistency? Is test coverage good? Da-da-da-da.
And… I almost always get… good feedback.
as if it was, you know, a good review. So I feed that back into Cursor, whatever model I'm using, and say, what do you think of this feedback? So I get the back and forth between these agents, and then I'll use Copilot on… online once the PR is submitted.
I'll use Opus to do a full, full, clean context review of the PR.
And again, there, I almost always get useful feedback.
So I'll iterate a few times like that, and that seems to have improved.
quality. And in fact, that's what I did to port the code excerpting tool. I had written the original in Dart many, many, many years ago, and then gone through various revisions, but didn't want to have to work in Dart anymore.
essentially co-created a plan to port it to TypeScript.
And then had fun with the tools. And since I knew I had a mental model of what the architecture is, what the spec was, and all that.
It was way easier than just somebody who wouldn't have known.
How to guide it in the right directions, but… Yeah, that's quite been my experience, lately in it.
It's been interesting. It's certainly, I think, as most of us have here heard, It becomes orchestration, and we become the representative of domain knowledge, of what the goals are.
And, agents are great at translating Dart into TypeScript, for example.
Which is why I think it would be super if we had a getting started in Java, and we could say, okay, we'd want one in Go.
Here's an example.
Make it work and go.
And we could probably gain speed there.
And keeping the… In updating the docs.
**Jay DeLuca** 51:52 Definitely.
One other, way that I've been using… oh, go ahead, Tiffany.
**Tiffany Hrabusa** 51:57 No, I was just going to say, coming back briefly to that topic, I did find, the PR that, Severin put up, and it actually did get merged, so it's in the docs, but it's hidden from the NAP.
**Patrice C (CNCF)** 52:09 Oh, right, right.
**Tiffany Hrabusa** 52:11 So I, I linked it in our meeting notes, but yeah, it is there. It's a reference specification for the application.
**Patrice C (CNCF)** 52:19 Right, I remember now. Thank you. See, that's part of.
**Vitor Vasconcellos** 52:22 Okay.
**Patrice C (CNCF)** 52:23 The parts we forget, and then the agents tell us, oh, by the way, What was this?
The avatar, you were gonna say?
**Vitor Vasconcellos** 52:33 No, no, I was just gonna say thank you.
**Patrice C (CNCF)** 52:38 Jane?
**Jay DeLuca** 52:39 But yeah, so I was just… yeah, so the other way that I've started experimenting with it is I have, I have, like, a repo with, like, various projects where I'm keeping track of like the Ecosystem Explorer project. And for months, I've been… like, doing, like, journal entries about different work that's gone on. I have it review PRs, do issues, and have it assemble this, like, kind of knowledge base. Not just at one point in time, but it kind of has historical context. And now I've started experimenting with, like.
I've gone through and asked it, like, okay, we have the Java agent ecosystem, pretty much built out audit open issues or missing issues for the collector ecosystem, and have it go through and identify issues that might be missing context or, have outdated information. And then I have these skills that I've created, too, that will basically review all of the existing documentation, and basically… between my, like, knowledge base and the code base, and open issues and discussions, and just make sure that everything's in sync, or call out any discrepancies. So I'm just experimenting with, like, ways that I can use it to kind of Track the project as a whole, and help with, kind of, like, the… The issue curation, And things like that, which has been… it's been… a lot of times, it's very verbose, and I end up cutting most of it out, but it's pretty cool, and I think it's… it'll… it gets better over time, so… But to what you… something that you mentioned around having the different agents kind of check each other's work, I think that's almost required. It's like, if I have Claude generate anything of substance, I… well, I'll have Claude re-review it, but then I'll try other things, and it's like… it always comes up with something, but then you have to… you have to question the questions a lot of times. Like, it's… it's amazing how many poll review or pull request comments it comes up with, where if you actually dig in and look at it, it's like, no, that wouldn't… that doesn't make any sense. I would look stupid if I told this person that. So, yeah. So, trust but verify.
As much as possible.
**Patrice C (CNCF)** 54:53 Absolutely.
Oh, there's something I wanted to mention.
Okay.
Hello.
Anything else?
Time… Okay, if not…
**Tiffany Hrabusa** 55:30 Sorry, I was just gonna ask, our newcomer, Pratek, did you want to introduce yourself, or… I know that you've been working with Jay pretty closely.
**Pratik** 55:40 Okay, so, hi, my name is, myself, Pratik, and I'm from India. I'm finally a student, studying computer science, lives near Mumbai.
And I've been contributing in OpenTelemetry, from January, I guess, and… this is really a cool and fascinating thing which is… I'm writing to, and I'm really exciting and enjoying it, so I'll be… I'm going to be consistent and… So right now, from the past few weeks, I'm not really, what I can say, active, because my, because of my interviews and my, company joining, so I was really a bit busy. Sorry for that, Jacer.
**Jay DeLuca** 56:25 No worries.
**Pratik** 56:25 Right now, I have joined the company, and yeah, it's parsable, works in the observability, and I will be consistent from now.
And I'm enjoying it.
Thank you.
**Tiffany Hrabusa** 56:40 Congratulations!
**Patrice C (CNCF)** 56:42 Yeah, great, congratulations indeed.
**Tiffany Hrabusa** 56:45 Thanks for…
**Patrice C (CNCF)** 56:47 thinking of that, Tiffany, I had no idea who knew who and who'd been around for…
**Tiffany Hrabusa** 56:52 Yeah, yeah, yeah, no worries. Uzo is our LFX mentee, she's working on the Prometheus and OpenTelemetry interoperability documentation, and she's joined before, so I know that she's listening in, and Sophia's been around, she's helping me with the collector docs.
Hey, Sophia. But yeah, Pratika, I didn't think that we had heard from you, so I just wanted to give you that chance to speak up, but we are glad to have all of you here, so…
**Patrice C (CNCF)** 57:22 Absolutely.
Very much so.
Big project, lots of work to do, and it's great to see the improvements there.
Happening.
Well, it's been a great meeting.
Thank you, everybody.
There's nothing else, then… Give everybody back 3 minutes.
**Jay DeLuca** 57:46 And welcome back, Patrice. Nice to have you back.
**Tiffany Hrabusa** 57:49 So nice.
**Pratik** 57:51 Thank you.
**Vitor Vasconcellos** 57:52 No.
**Patrice C (CNCF)** 57:53 Okay, take care. See you next time.
**Vitor Vasconcellos** 57:56 Nope, not…
