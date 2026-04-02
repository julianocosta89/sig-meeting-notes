SIG: JavaScript SIG
Date: 2026-04-01
Duration: 56 minutes
Zoom Recording URL: https://zoom.us/rec/share/b_8Z1GZpfgtvo1w7gFNpAzRNrQ-bbMKpLWGY_rJjGfU2gHexEtSJaZ8mXLbbG7hq.EBcEtE1fFSujoxlk
============================================================

## Zoom Recording Transcript

**Trent Mick** 01:38 Nope.
**Hector Hernandez** 01:41 Hello.
**abhinama** 01:44 You know.
**Trent Mick** 01:45 Sorry, I'm slow, I said I'd do this one, and I just got the agenda set up.
6 seconds ago.
And I'd say, I guess we could get going, but there are no agenda items, so… We go straight to boring triage.
**Marylia Gutierrez** 02:56 I was just gonna… For a review of a PR, it was… it's not my PR, but I just wanted to get an opinion, and I'll try to find a PR, so this one I'm taking a while. It's the one that the person messaged on the Slack channel.
Let me find…
**Trent Mick** 03:13 JS or JSDev?
**Marylia Gutierrez** 03:15 Jsk funded, let me put it…
**Trent Mick** 03:23 Sure.
**Marylia Gutierrez** 03:27 Is the one about…
**Trent Mick** 03:31 This one?
**Marylia Gutierrez** 03:32 Yeah, this one, so… I just wanted to get an opinion on this one.
I'm not sure if I… If… if the solution's getting too complicated, but…
**Maxime David** 03:46 Hi, by the way, I'm the author of this pull request, I just joined, sorry about that.
**Marylia Gutierrez** 03:51 Cool.
Because, yeah, I just got back, because I was out.
So I'm just… I'm just looking today, so, yeah, because my, my idea was… For the issue itself, I was trying to see if we can use something for… that would work for both the… when you config from the file and from the environment variable, and this one is very focused on the environment variable.
But at the same time, we have Mike that is changing how it's done on the file, so I don't know if they're gonna conflict. So I'm just trying, like, something that we can have, like, the default values for everything.
**Maxime David** 04:33 Yeah, I see. I've done that because at first I was just trying to add just warning, everywhere, and it got pretty messy, so I was like, maybe there is a better solution to, to just have a list of what's… Available for each one of the options, and if it's not here, well, we auto-log something, So… but yeah, obviously, open to any suggestion.
**Marylia Gutierrez** 05:00 Yeah, I like the idea of, like, having all of the, like, the default, like, the first file that has… you can see in one place everything, so I like that idea, but I'm trying to see if there's any way that we can combine it, because this is only going to work if you're setting up from environment variable, not from the file. So this is what I was saying, like, is there anything that we can do to… Have the default, Or… bold, so yeah.
So, just looking for anyone has any ideas as well.
**Maxime David** 05:34 Yeah, I can try to think about a solution which fits the two.
Yep.
**Trent Mick** 05:46 I've been too long away from config stuff to have a strong opinion there.
**Marylia Gutierrez** 05:50 Just to give, like, an update, so now the… the way that is being parsed, the file, because we are now able to generate the schema, so the PR that is up, is basically now we don't have to go thing by thing, just gonna parse the file and put it The… basically the… The config model.
**Trent Mick** 06:12 one.
**Marylia Gutierrez** 06:12 Yes.
So, what the trick about this one is… If we have a default value, then we have to, like, merge after for the things that don't have. So this is why this one's gonna have a function that is… yeah, it's called a merge something.
So the… so this is what I'm thinking, like, is anything that we can, like, the… the… the… basically the list that you created for the environment variables be the name of the parameter or something, and then the file can call this one to the default of the file, and the environment variable can also call this, but I don't know if that starts to get too complex or not.
**Trent Mick** 07:02 Okay.
**Maxime David** 07:07 And the logic is first pass the file, then check the environment variable and perform the override if needed.
**Marylia Gutierrez** 07:16 No, so from the, like, configuration, you only… only you use environment variable, or you only use file?
But the… yeah, you can have an environment variable on your file, then it's gonna use, but if you don't have it, it's only one or the other. But the way that the… works on the environment variable is, like, okay, you read the environment. If there is no value there, you use the default.
So you are going, like, on that file, it's going caves by case, because you have to check for the right name, whatever, but on the file, it's because the… basically the format of the YAML is the same of the config model, we can just call a function that is just sparse, and it just do all of them.
But what that means is that now, if there is a default for something, you have to then add it after, because otherwise it would get replaced.
So that's why I was thinking, if there is a single place that we could add anything that is a default, like, after, so this way is… doesn't matter which one you're using, it would get a line.
**Maxime David** 08:24 Yeah, I definitely agree with the vision, and I'm pretty new to this package, I'm more familiar with the AWS Lambda, the OpenTelemetry Lambda one, but, yeah, I don't know if you want me to have a look at a more… a bigger solution, or if it's fine to merge this, and then reuse this logic into the file reading, or if we want to have one, full solution on the first draft. It's really up to you. I'm fine with both options.
**Marylia Gutierrez** 08:57 You know, I'm gonna take another look in more detail, just because I mentioned, like, I am back, kind of, like, today. And if anyone else also wants to take a look to give an opinion, and then I can put any comments on the PR itself.
**Maxime David** 09:09 Sure. Also, feel free to… I don't know which channel are you using, is it the HotelGS channel?
**Marylia Gutierrez** 09:17 Oh, so yeah, we have, like, two channels. So, hotel.js, we use more for, like, questions of people that want to use the SDK, so, like, oh, how do I use? And we have one that is hotel.js dev, so that is for people that are, like, contributors, so we talk about more, like, PRs on that one. So, yeah, feel free to join that one as well.
**Maxime David** 09:34 Sure, yeah, I'll be super active on this channel, because, yeah, just a quick spoiler alert, this is the first PR, but I suspect that we are going… I'm from AWS, by the way. We are going to push a bit more pull requests, maybe to adjust the performance issue if there are some. We are doing some internal benchmarks, so I might be more active in this community on the following weeks, so…
**Marylia Gutierrez** 10:00 I'll always have.
**Trent Mick** 10:01 Oh, that'd.
**Marylia Gutierrez** 10:01 have new people.
**Maxime David** 10:02 Yeah.
**Trent Mick** 10:03 That'd be great.
**Maxime David** 10:05 Cool.
**Trent Mick** 10:05 Especially if you're able to publish any of those benchmarks. I know sometimes you can't always, but I'd love to see some of those, yeah.
**Maxime David** 10:11 Definitely, yeah, thanks.
**Trent Mick** 10:16 Alright, next, Jamie, did anyone chat? Welcome back.
**Jamie Danielson** 10:23 Hi, I know, it's been a while. So I've been, working with the LLM Symante Convention SIG, and one of the things that we were talking about recently is creating a separate repo for Gen AI instrumentations. Basically, the idea would help us to, like, iterate faster on things without having to worry about affecting stability or, you know, kind of just doing things differently in a separate repo, and it's almost definitely going to happen for Python.
Because that's, you know, probably the top language for Gen AI stuff, and, has some issues that they're trying to sort out. One of the questions that came up was.
when we create this other repo, do we want it to be specifically Python and maybe just Gen AI semantic conventions, or do we want it to be.
potentially a monorepo or multiple repos for things like, you know, JavaScript or TypeScript instrumentation, and Java and a couple of others. So it's still sort of an open question, and so we were checking in with everyone of what their preference was. Now, for Python, it's of course a lot easier, because when they use their, you know, bundled auto-instrumentations agent thing, they're pretty easily able to bring in instrumentations from third parties, but our auto instrumentations node does not work that well, or does not work that way to be able to bring in third-party instrumentation. So I guess the question I had was.
As a general thought, how do we feel about… doing… moving GenAI instrumentation stuff into this separate repo, both as a general thing, but also knowing that That would mean we can't today… someone can't use our auto instrumentations agent with one of these other instrumentations, at least not like the one-liner, easy, startup.
So yeah, I guess I wanted to get… opinions. I sort of have… the thought of where it might just be too difficult, and we've been okay with what we have in Contrib, and it might be hard to split brain to another place, but… curious to see what people think. I guess especially, maintainers and approvers, which seems to be most of who's here anyway.
**Trent Mick** 12:37 So the only one that would be impacted currently would be the OpenAI one.
That I'm.
**Jamie Danielson** 12:42 Yeah, that's.
**Trent Mick** 12:42 a maintainer on. I am fine either way, so… no blockers if you feel like it's gonna… help unblock work going on there, then I'd be cool with moving it out.
**Hector Hernandez** 12:54 There's also a line chain that is in progress.
**Jamie Danielson** 12:58 It's just not in the agent yet, yeah.
Yeah.
**Trent Mick** 13:04 You were… Hector, were you working on that? I saw you added your name as a maintainer, so I'm not sure what the Langchain story was, but…
**Hector Hernandez** 13:11 Yeah, someone else, I think it was Amazon people were trying to add this, so we're definitely interested in having this instrumentation, so if there's not a lot of traction, we will start adding code there very soon.
**Jamie Danielson** 13:27 Yeah, like, one of the… one of the things generally is, like, you know, obviously everything in… anything related to AI, LLMs, whatever, is moving super fast, and, there's definitely, you know, some… interest in helping things move fast in SimConf and everything, but there's different stars that have to align to help it move fast. So there's, you know, I guess one of the questions I have, especially because I've been away for a little bit, is, like, have we run into any issues currently with like, our instrumentations right now in Contrib? Like, is it… I don't remember exactly how experimental it was. When I saw the OpenAI instrumentation was in the agent, that's sort of what made me think twice about potentially moving it out. And also, it might not necessarily happen now, it could be, like, we start with Python now, and if we see it's working well and moving quickly, then we move the JS stuff over.
**Trent Mick** 14:25 Yeah, the… I mean, the… I, the main difference from Python, as I gather, is exactly what you said, is whether it's included by default in auto-instrumentations node.
**Jamie Danielson** 14:39 Not just default, but, like, we can't… like… I guess by default, you're saying just in the package. Yeah. Yeah.
**Trent Mick** 14:47 Well, there's that, and I guess the second thing is the specific… getting the right versions of dependencies, like the instrumentation package.
can matter, and can matter because things will subtly break if it doesn't. So if you have two different versions of import in the middle, then ESM instrumentation stuff's surprisingly not going to work in some cases.
So that's… that's maybe a bigger one, too. I don't know, like, we have to solve that problem, but it's not gonna happen right away.
Similarly, the… maybe, I don't know, the vaporware idea that I'd had for the… including third-party instrumentations was having something like Hotel Java's extensions, But that's… that's not gonna happen quickly, either.
Yeah, I don't know. I don't know how… I know what the… this isn't answering your question, it's just throwing more fuel on the fire. The… Browser guys care about… breaking some of the dependency on the instrumentation package as well. So, like, instrumentation Base has got a whole bunch of stuff in there that the browser instrumentations don't really need, and I'm not sure what the progress is on that kind of thing, so I don't know if… this would be another avenue for doing that kind of thing. I don't know.
**Jamie Danielson** 16:04 Yeah, I was thinking the same thing and kind of mentioned that, like, we have a similar… a different scenario, but a sort of similar scenario with browser, of what gets split, when it gets split, things like that.
So, and so there could also just be… we can… you… we… just focus on Python for now, keep it as an open… like, it's good to know. I didn't know if I would mention it, and there would be sort of, like.
oh, dear God, absolutely not, you know, burn it with fire. If we don't have strong objections, but don't feel strongly in terms of trying to start it up right away. It could be a… let's see how browser things go if they start figuring out how they want to split things off, see if we get any inspiration for that, or people working on splitting those things.
And if it turns out to be painful, then… Yeah. We move it higher on the priority list?
**Trent Mick** 16:56 I mean, all these things are still experimental packages, so we can do a breaking change on auto-instrumentation's node, yeah.
Hector, you and your guys with usage, would it be a killer if the Langchain one was not part of Auto Instrumentation's node? So it's not part of the default set?
**Hector Hernandez** 17:13 No, we do not use that package, actually, because it comes with so many instrumentations.
**Trent Mick** 17:18 Yeah, yeah, yeah, okay, good, so that… that case doesn't… isn't a blocker for… I don't have a read at all on users of the OpenAI instrumentation.
The history behind that one is we… we built that, I was part of the JS one at Elastic, and then we… we donated upstreamed, but it hasn't seen any dev really on it since.
There are a couple open issues, so… Yeah, I don't know. I think anything to free up, if you… like, you're gonna be spending time on this, so anything to free up making that… those things move faster. And I guess maybe on the… The optimistic side, this could be a thing that pushes us to deal with the problems that we have with not having an extension system or a better story with the instrumentation package dependencies and stuff, so… Maybe it's positive.
**Jamie Danielson** 18:09 True.
Okay.
Alright, I think that's useful, I guess. I haven't seen anyone else come off mute, but if you do have thoughts, I guess… Let me know, otherwise… I'll have this as a… Solid maybe, and kind of put together some notes and see what some other folks think, and… Go from there.
**Trent Mick** 18:36 Am I wrong that the discussion in the LLM site was probably mostly around Python, right? Because that's where most of the discussion.
**Jamie Danielson** 18:40 Python is the sort of thing that's, like, definite. The question is… one of the… One of the several reasons of why we're also thinking about it is with a lot of these semantic inventions and instrumentations, we have some input in various ways from AI folks, and less in certain areas, and some from hotel folks in certain areas, and we want to get as many voices involved, not to overwhelm perspective, but more of… you know, does this work for this AI provider? Does this work for this tool? Because otherwise there's, you know, we're making decisions that we don't really know the difference of, and if it means that having multiple languages means we have more… companies involved, then maybe that's a good thing, but it might not be necessary because Python is so ubiquitous, really. Python's number one.
In terms of needing to have this other place to work.
**Trent Mick** 19:40 Yep.
**Jamie Danielson** 19:43 Okay. Okay.
**Trent Mick** 19:46 X.
repeating what Mark says, if while we're doing triage, people have other things, please add them to the agenda, and we'll come back and look at them, so… Let's look at… And triage bugs.
Yay, none.
Okay…
**Marylia Gutierrez** 20:16 Oh, this… this one, yeah, could probably mark as trash. Already found someone that… who can fix that, and… basically now the… after there was, like, an update, instead of, like, when there is no GCP, it's actually Instead of just, like, quietly saying, like, there's nothing for me to detect, it's actually creating those errors, and it just…
**Trent Mick** 20:40 Yeah, I noticed that recently, yeah. Did you… do you happen to know if that was in a Gaxios update, or in GCP metadata itself?
Looks like…
**Marylia Gutierrez** 20:48 So the… because I know that they just, who's, created the issue was Nikolai, and they just got the latest auto-instrumentation, and after that is when he started to see this error message. So whatever was added on the latest auto-instrumentation.
And since I saw that Aaron was the one who added the package, I messaged him, and so he's gonna take a look.
**Trent Mick** 21:11 Okay, great. So, we put that as a… Dan, are you here? You know my priorities.
**Daniel Dyla (Dynatrace)** 21:24 I am here, sorry I was distracted. Resource detectors print scary messages in the logs. Yeah.
**Trent Mick** 21:29 You just get warnings. I don't know, is it a.
**Daniel Dyla (Dynatrace)** 21:31 I'd say that's a 4.
I mean… I could also see the argument For 3?
Yeah.
**Trent Mick** 21:43 et cetera.
**Marylia Gutierrez** 21:44 Yeah, I would… I would say… I would say 3, because it's actually showing, like, error message, which is not an actual error, so if people are, like, looking for errors, might trigger, like.
Alerts or whatever, and it's not really an error.
**Trent Mick** 21:59 Yeah, okay.
And that's enough to get off the list, yeah. Okay, so… do I want to assign this to Erin, or…
**Marylia Gutierrez** 22:08 So I don't know if he was gonna be the one looking, because he said that he was gonna look at his team, so, like, whenever someone… it is working, let me know. So I don't know if it necessarily is him, so I left without an assign.
**Trent Mick** 22:21 Okay, cool. I'll throw that on my list to take a look at later.
Better follow-up on next week.
**abhinama** 22:30 Is that something I can, also volunteer to take a look?
**Trent Mick** 22:35 On that one?
**abhinama** 22:36 Oh, yeah.
**Trent Mick** 22:38 Sure, definitely. Did you… Well, why don't you take a look, and you can assign yourself if, or…
**abhinama** 22:43 Okay.
**Trent Mick** 22:44 Or I don't know what the…
**Jamie Danielson** 22:47 I think you have to comment on it for someone to be able to assign you to it anyway, so maybe if you take a look and it seems like something you want to grab, just comment that you want to grab it, and then we can assign it.
**Trent Mick** 22:57 That one of us can send you.
Great, thanks.
Okay, so there is… we've had this… A couple of times before I was looking, there were a couple older issues. One was an instrumentation PG.
Oh, maybe he'd gone and found the same ones, too.
Yeah, looks like.
I just asked a little while ago to see if he can give us the full stack trace, so it might help track it down a little bit.
Interestingly, that last one that was in Instrumentation PG was also a Nest application, I think.
This one's using Nest.js.
So… I wouldn't… There have… no, actually, I don't know if there's been an instrumentation PT change recently, so I don't know.
We'll see.
If I've asked for feedback, what are the appropriate labels for this? I'm new to this.
**Jamie Danielson** 23:55 I don't always put one on there, but there, I think, is a, like, needs feedback or needs author.
**Daniel Dyla (Dynatrace)** 24:01 Something? Yeah.
I think it's in…
**Trent Mick** 24:03 It's…
**Daniel Dyla (Dynatrace)** 24:03 outweight.
**Trent Mick** 24:06 Needs author response.
And then, good enough for now. It'll show up next week.
**Jamie Danielson** 24:11 I don't remember if we're…
**Daniel Dyla (Dynatrace)** 24:14 Also, you have, like, stale bodies.
**Jamie Danielson** 24:15 add on.
But yeah, it needs a repro.
**Trent Mick** 24:18 also needs… oh.
Green…
**Daniel Dyla (Dynatrace)** 24:21 Sorry to just hawk over you.
**Jamie Danielson** 24:24 No, you're good. I was just gonna say, like, I know Mark and I had updated Stalebot at some point to, like, close out certain issues if they had, like, bugs if it had needs author response and was open for 30 or 60 days or something, so that's why I think it's useful to put that on there, too.
Because otherwise, bugs don't close with Stalebot.
**Trent Mick** 24:46 There we go.
**Jamie Danielson** 24:52 I don't know.
Yeah, so, like, 39… Line 39 has, like, exempt issue labels as bug.
So maybe… oh, it might be the other one. The, The other repo, the core repo.
**Trent Mick** 25:17 Oh, what am I doing?
Hash, of course.
**Jamie Danielson** 25:19 of the idea.
**Trent Mick** 25:20 Or it's the core package.
**Jamie Danielson** 25:22 Yeah, the idea is, like, if it's a bug, we generally probably want to fix it, but if it's labeled as a bug, but is, I wonder if we got rid.
**Trent Mick** 25:32 We did.
**Jamie Danielson** 25:34 If it's labeled as a bug, but is, you know, needs response or something, then the idea was that it would still close, even if it was labeled as a bug.
I don't know. It's been a while.
**Trent Mick** 25:49 Okay… Cool. It'll…
**Jamie Danielson** 25:53 At least it's useful looking at it. It'll turn up next.
**Trent Mick** 25:55 Okay, we'll take a look next week then, too, at least.
Okay, before jumping into old issues… Let's go to… Ding… Focus topic milestone.
So, I think, the logger.enabled one just merged the other day, yesterday, two days ago?
So we're getting close on this, so… just a reminder, poke to anyone if you have cycles and want to pick up a bug. The sooner we get this off the list, the sooner we can pick some other focus stuff, like, I know a lot of people are keen on the declarative config work, too, so that'd be good to be able to put that on.
It's one of the focus things.
And then, another reminder for… June-ish, when no… 20 is dropped.
We wanted to do JS SDKv3, this summer sometime. If you're coming across issue work and you notice that there are things where we've said what we're gonna wait until a breaking change to do whatever, or if there are things that we should do before that, please bring them up and add them to this milestone or discuss.
Bringing that up.
And we'll have to start working through some of these.
brick things, yeah.
Cool.
Okay… I think Core might actually have more, but we've done Core the last couple of times, started there, haven't we?
I know, it's close.
47, I'll do this one.
Or is this the one that we've been doing all the time?
Okay, this one, I want to kick the can down the road again until… unless anyone's heard it, has there been movement on finalizing the RPC schematic conventions? Anyone know?
Oh, don't know.
Just gonna wait until that goes… Stable, then we can… To have a clear path forward there.
**Jamie Danielson** 28:18 Do we want to put something like needs spec on there? Like, it's not specifically spec, but kind of? Like, it's waiting on semantic conventions? That's why it hasn't been updated?
Does that help at a glance?
**Trent Mick** 28:33 Well, so, my memory was that Mark had started that issue for the… The opt-in environment variable, what was that one?
**Jamie Danielson** 28:45 Oh, yeah.
**Trent Mick** 28:53 This thing.
And that hasn't moved at all soon.
**Jamie Danielson** 28:59 Love that.
**Trent Mick** 29:01 Come on.
Mark said he could work on this, but two closed… What was this?
That was so many conventions, did Stalebot kill that one?
Yeah.
**Jamie Danielson** 29:13 Oh, there's something I linked, it should be linked in here, I think.
Because… like, in this particular PR, maybe. Does it have a link to another SEMCOMF PR issue in the history in here?
**Trent Mick** 29:27 In this one.
**Jamie Danielson** 29:29 Yeah, that one, guidance for… that one. I haven't looked at this in a bit, but I think this is where we're, like.
It gets funky, like, this was if, I think this drops… A particular attribute?
**Trent Mick** 29:46 Excuse me.
**Jamie Danielson** 29:49 Oh, things get weird with the latest experimental… We'll be in a situation where someone wants both stable conventions When available, and they want the latest experimental, we're not yet stable.
**Trent Mick** 30:14 I admit to not being super well-read on… The issues around this one, but… A couple of things I'd seen in some of the Java instrumentation was… Specific one-off configuration options for… assuming stable is a starting point, I want this extra thing, I want this extra thing, and so… they were somewhat akin to, like, the particular config bars that we have in some instrumentations for. I want to turn this thing on, but it's off by default.
Basically, targeted opt-ins instead of one big… monster opt-in. I kind of wonder if that's a… clear path, but I don't know, I haven't thought it all the way through.
**Jamie Danielson** 30:56 Yeah, I haven't looked at it since whenever this… whenever this happened, a few months ago, but it's one of those, like, you could really go pretty deep down a rabbit hole of How particular you want to be, and that's probably why it's been… Sitting for a little bit.
**Trent Mick** 31:12 And then there was that separate… I don't know if it was more than a blog post, if it was OTEP and spec work for stable only by default.
This is… Wrapped up in efforts to get… OpenTelemetry.
what, along the next stage in CNCF approval or something like that? I don't know… Yeah, what the hopes and dreams are there. Given that all of our instrumentation is unstable, and our exporters are still experimental, it's like… Forget the small stuff, we have bigger fish to fry that we want to get stuff stable so we can be part of that boat. So, yeah, I don't know.
This is why I keep kicking that can down the road.
birth.
Particular ones, like…
**Jamie Danielson** 31:55 Yeah.
**Marylia Gutierrez** 31:56 Yeah, the hope is to have a lot of things market-stable, just help with graduation.
**Trent Mick** 32:02 Graduation, there you go, that's the…
**Daniel Dyla (Dynatrace)** 32:05 Given.
**Jamie Danielson** 32:05 Instrumentations are probably a lower priority. Sorry.
**Daniel Dyla (Dynatrace)** 32:10 Given that we're doing, like, regular… Major version.
Bumps at this point.
do we know what's holding back the exporters from being stable? Because I know Mark's done a lot of work on them, and there's some things that He still wants to do, but if it's okay to… Wait until the next major version bump for braking changes.
Was holding us back from… from saying those are stable.
**Jamie Danielson** 32:45 I think it might be listed… I'm looking in, like, the focus topic.
To see…
**Trent Mick** 32:50 It was discussed there, wasn't it?
**Jamie Danielson** 32:53 Yeah, there's, like, a tracking issue and milestone, because I think it was… related to… I mean, part of it might even be related to the config file, honestly, where we wanted to see how that landed, or how, you know, we wanted to put those things sort of together.
Because he wanted to change how these things are done.
So maybe go into, yeah, tracking issue, and maybe even the milestone might give us more…
**Trent Mick** 33:19 Get a milestone for this.
**Daniel Dyla (Dynatrace)** 33:23 Yeah, I think the biggest problem with the OTLP exporter is that it depends on the logs.
**Jamie Danielson** 33:31 Oh.
**Daniel Dyla (Dynatrace)** 33:31 Maybe, which is not…
**Trent Mick** 33:32 Okay, so hence, stabilized logs first would solve some of the issues there.
**Daniel Dyla (Dynatrace)** 33:37 I think so.
**Trent Mick** 33:38 It's all tied in together. There's, I mean, there's a fair amount of craft in there. There's, like, create legacy whatever is the only thing that's whatever wrapper function calls, so, like, presumably there's some cleanup stuff that could be done there. I don't know if that was necessarily on its plan.
To me, another… pickup.
Currently, it's the renewed effort on the browser side stuff, and just… Not in issues, but discussing with Mark on the side. I wonder if it makes sense to have a… just a node… path for exporters and a browser path for exporters, and not try to have this unified base for them, because I think it just adds it's potential that it adds more work than it helps solve problems. I'm not sure if… the hope was to wrap all of that kind of stuff up before we stabilize. Don't know.
But certainly that's one point, and then instrumentation base stuff is another thing to stabilize.
At some point.
And then I think we're, like, basically good, right? And then we can start… Those are all the core… those are the core pieces. Exporters and instrumentation, is there something I'm missing?
**Jamie Danielson** 34:49 own logs.
**Trent Mick** 34:51 Oh, well, true.
Yeah.
**Jamie Danielson** 34:54 But… Yeah.
And then config file.
To quickly.
**Trent Mick** 34:59 That feels like that's a new thing coming afterwards, like, the old stuff that we're catching up on is…
**Jamie Danielson** 35:05 Hmm.
**Trent Mick** 35:05 Yeah, that's free.
**Jamie Danielson** 35:06 Yeah, we need those in order for declarative config to become stable anyway. We need the other underlying pieces to be stable.
**Trent Mick** 35:13 Correct.
**Jamie Danielson** 35:14 Right. Yeah.
**Trent Mick** 35:16 I'm kind of assuming, without having said it, that after we get logs and stuff stabled, that one of the likely focus objects is going to be declarative config.
work.
**Jamie Danielson** 35:25 Yeah.
**Trent Mick** 35:26 Not like… Not, like, not being a focus stops other people from working on it anyway, so… Yeah.
Okay, where were we?
Okay, the reason I wanna… Mentioned this one as… Maxine, are you… you're still here?
**Maxime David** 35:51 I am…
**Trent Mick** 35:54 Yeah, you said you're at AWS and you mentioned Lambda, so this old one kicking around for a long time sure seems like a likely candidate to poke you with, if you had some cycles that you wanted to take a look at at some point.
**Maxime David** 36:06 Yeah, definitely, yeah, I can sync with the author, because he's also on the OpenTelemetry Lambda SIG, so yeah, I can definitely have a look at that.
**Trent Mick** 36:17 Okay, yeah, that'd be great to… I don't remember what the current state of this is, but…
**Jamie Danielson** 36:22 Yes, I checked, yeah, they have to update SEMCOMF with… these things.
**Trent Mick** 36:27 So it's pushing to get SEMConf to… It's the SEMConf for FAS for Lambda that was not caught up to changes that have been made in general messaging SEMConv.
And…
**Jamie Danielson** 36:40 Yeah.
**Trent Mick** 36:40 Once that's clarified, then we can change the… the Lambda instrumentation.
Yeah. Which is potentially, arguably, a breaking change for people, I don't know.
So anyway, having someone engage on that would be… Would be nice. Definitely not a requirement. It's sat there for a while already, so…
**Maxime David** 36:57 Can you assign it to me, or do I need to comment, and then you will assign it to me, or…
**Trent Mick** 37:02 What's your GitHub handle? Max Day? Yeah. Yeah, you'd have to comment on that issue, so… I'll put it in.
Chat here.
Thanks.
**Marylia Gutierrez** 37:13 Yeah, just to clarify, this is a PR, not an issue, so ask us to help with the review of the PR.
**Trent Mick** 37:22 So maybe, yeah.
**Marylia Gutierrez** 37:24 Because, yeah, you can just go and review, you don't get… you need to be assigned to review up here.
**Maxime David** 37:30 Okay, I get it, yeah.
**Trent Mick** 37:33 Thank you.
You weren't correct.
This is just needing reviewers.
Iowa readiness work.
Okay, here's a meta-issue. I think, actually, hold on.
So, Amir is the maintainer for a few packages?
Has anyone spoken with Amir in a while?
I think we'd had the issue about moving some contributors to emeritus status.
I don't know if it's time to move on that one. And then do we…
**Marylia Gutierrez** 38:17 I messaged him to see if he was still gonna be alive, like, like, active, and then he just didn't reply, and that was, like.
Over a month ago?
**Trent Mick** 38:30 Okay, so I mean, unfortunately, he doesn't have the time for it, but so be it.
**Jamie Danielson** 38:38 Yeah, I know Mark has the script already in there for, like, regular approvers and maintainers, but I don't know if we've applied it to… code owners specifically, that might be a manual process still, since sometimes packages sit there and just don't have any updates, and I know that's something, Marilla, you were looking at with your script upstream, too, where it gets tricky with code owners and things for things that don't get updated that often.
**Trent Mick** 39:04 Do we not have an open issue for them?
Alex, here we go. It's in the J… in the core repo.
So basically, we're just waiting to merge this, but we talked… pushed off discussion of it, I guess.
**Jamie Danielson** 39:21 Oh.
I think… Yeah, this might be where someone had reached out, like, personally, again, on Slack for this one, too.
Amir… oh, a mirror dropped from maintainer to approver, I guess.
So it's like, I knew he had done the… Yeah, I knew he had done the one change, but I couldn't remember which one.
**Trent Mick** 39:47 I mean… I could just merge this one, it doesn't change the question of… Put over and change the contemporary part.
**Jamie Danielson** 39:54 Yeah. Yeah.
**Marylia Gutierrez** 39:55 Because this changed, but it still manually needs to be removed from the team, like the JavaScript approver, that process is still manual.
**Trent Mick** 40:05 I see, okay. Okay, I'm gonna leave this open for now, then, because someone has to follow up.
Immediately after.
Okay.
**Jamie Danielson** 40:17 So yeah, I guess, like, with your meta issue, I guess at some point, maybe we go through again, we do the same process that we did, I don't know, several months ago, of… Code owners checking in on people, seeing if they're still around, and… Updating for no… no maintainer.
Just for setting expectations.
**Trent Mick** 40:36 Yep.
And for anyone who's on and is keen for the Redis and our Redis package, there are a few older PRs poking around.
If people have cycles for… here's another one.
Down here.
And there's a rediswand.
That one's just for tests, I think.
Okay.
Sorry, I know that you will have to follow and click through on all these ones and have some, but I don't feel like I'm going to be able to provide any forward motion on many of these things, other than some general discussion. There's an OpenAI one, Jamie, if you'd like to take…
**Jamie Danielson** 41:12 I know, I just saw that, I should probably take a look.
You can also take a look, if you'd like. You can both take a look.
**Trent Mick** 41:18 Yeah, well, I'm technically a maintainer, or a co-owner of… That's what we have cycles for.
**Jamie Danielson** 41:31 Can't remember if this is the one where there's not SEMCOM for the things yet.
**Trent Mick** 41:39 Is there still not?
Respond… okay, I don't know, there's so many APIs, right?
Yeah, I'm putting together…
**Jamie Danielson** 41:47 yeah, I'm putting together a list, actually, this week of all the things that are there, and that are still… need to get worked on, so I'll know for sure in a day.
**Trent Mick** 41:56 Okay.
**Jamie Danielson** 41:57 If that's the case, but yeah, I'll put this on my radar.
**Hector Hernandez** 41:59 Yeah, this PR, the author, just… Had not replied for a while, I think that's the issue with this one. But, yeah, he created this, like… Seven months ago, so semantic conventions keep changing, so it's obviously not.
**Jamie Danielson** 42:13 Yeah.
**Trent Mick** 42:15 Okay.
Are you… Hector, I'm curious, you were talking about… Being more involved in some of the the GenAI instrumentations from JS side, I'm assuming, at least partially.
**Hector Hernandez** 42:35 Also from Python.
**Trent Mick** 42:37 Well, I'm…
**Hector Hernandez** 42:38 It's just very hot everywhere, right? Gen AI things.
**Trent Mick** 42:44 Okay.
**Hector Hernandez** 42:45 Oh, yeah.
**Trent Mick** 42:46 If you want to take ownership.
Of this one. I mean, I know these things are sometimes, especially when they get old, it's like, well, you're 17 versions of semantic conventions behind on this one, and…
**Jamie Danielson** 42:55 I was gonna say, you might… this one, too, you might want to hold off for a minute, because, like, it has… omitting the messages as inference details, and there's an open PR from Trask right now getting rid of inference attributes that I asked the question about, so I would hold off on this for… At least a day, I don't know, I don't know if he…
**Trent Mick** 43:14 I had this… I had the GenAI semantic state in my head at one point, and then it was… Yeah. It was events, then it was spam, then it was events again, or something like that, anyway. Or log, yeah, still.
**Jamie Danielson** 43:28 a lot.
**Trent Mick** 43:32 It's hot.
Okay, DependBot, or renovate… Innovate this one. Mark was gonna follow up at some point. Thompson… Renovate, renovate… Another iRitis one.
My vague memory is that the two I wrote us once were… Probably reasonable, they're just adding features to get more coverage.
So, if someone's…
**Jamie Danielson** 44:06 I think, like, we just didn't have a chance, like, if someone could try it out and see, or if someone's more knowledgeable of it.
**Trent Mick** 44:13 Yeah.
Was that the one that we'd already discussed?
**Jamie Danielson** 44:30 Yeah.
**Trent Mick** 44:32 Alright, so…
**Jamie Danielson** 44:33 What if we… I guess one thing to look at, too, if we wanted to limit how many we look at, is if we wanted to look at fixes, more specifically. Like, right now, we're kind of going through just old open things, but the reason a lot of the features usually aren't implemented is because they're a lower priority to fixes or current focus areas, so… I wonder if it's… More useful for us to… try to target fixes first before… as opposed to looking at all of them, which kind of goes to your earlier question.
**Trent Mick** 45:04 Think in title list?
**Jamie Danielson** 45:05 Does that work?
Aww.
**Trent Mick** 45:08 There used to be, isn't there?
**Jamie Danielson** 45:12 Advanced search syntax.
I don't know, teach me.
**Trent Mick** 45:24 What? Where did I see Entitle before?
Oh, sorry, that's Gino.
Nevermind.
**Jamie Danielson** 45:31 Oh.
**Trent Mick** 45:36 Yeah, no, that's not gonna work.
**Jamie Danielson** 45:39 Manual look, Ctrl-F, or Command-F.
**Trent Mick** 45:42 So, yeah.
I'm a sucker for log stuff, I should probably look at these.
Okay, the pain I'm feeling right now in driving this is because I feel like I'm wasting everyone's time, but I think the pain is partially intentional, and that we should look at the older issues so they don't sit around forever, but I'm feeling pain.
**Hector Hernandez** 46:18 Yeah, they say no pain, no gain. Right, so…
**Trent Mick** 46:21 Whatever.
**Jamie Danielson** 46:23 I mean, we could also time box it if it becomes too, like… too much, but that's also, again, the reason that we did add it is because we were hoping that by feeling the pain together, then maybe we get some of these looked at. But it is hard to review PRs with Bunch of people.
**Trent Mick** 46:48 Yeah, I certainly feel like my IQ drops when I'm on a call.
So I find it harder to…
**Jamie Danielson** 46:53 It's a lot of eyes watching.
**Daniel Dyla (Dynatrace)** 46:55 Usually, it's, like, the last 15 minutes of a call, too. Today, it's been the whole call.
Mostly.
**Trent Mick** 47:03 Alright, so I'm calling it, I'm gonna go to the repo and look at recent stuff.
I don't even get opinions from people.
So, latest issues… If anyone's keen on sampler stuff, there's sampler things happening.
I didn't realize that the trace ID ratio-based sampler was… Deprecated in favor of a probability sampler, which is a Anyone… Well, okay, if you don't know what… I mean, when I say composite sampler and the composable samplers, then… I guess he could stop reading, but… There's a whole lot of sampler.
Stuff in the spec.
Some of which we could catch up on. Most of the composable sampler stuff we have implemented now, but the probability sampler is a new thing that was added.
Basically promoting the better… sampling algorithms up to the non-composable stuff, with the idea, I guess, of… and some of this will come from… this is, in a way, declarative config was… Partially motivated by being able to express these complex samplers, right?
In config without being able to do them very well, so… Yeah, someone picking up on those would be… okay.
This is up for grabs if someone wants to, to do the work to make sure that our exporters don't… read a 7GB response from, a bad-acting OTLP collector.
**Jamie Danielson** 48:54 Should we… is it… we haven't done it, really, in a while. Is it useful for us to add some labels, like… Up for grabs?
It's, like, implied, probably, but… Know that something is well-scoped.
**Trent Mick** 49:09 No, I have a couple of times, and it's been useful. I think some people have picked up stuff when I've… scope them well.
**Jamie Danielson** 49:17 It can be intimidating to have 187 open issues and not sure… Where to start, but if something is well-scoped, then it seems like a good one to…
**Trent Mick** 49:25 This one is kind of well-scoped, but I wasn't sure on this one is, or maybe people have opinions on this one, so… the probability sampler was added to the spec.
As it's kind of easier to see in the table of contents.
as an alternative to the trace ID ratio-based one, this one's in status development.
Currently, our s- our… Our approved samplers live in, in stable packages.
I don't know what… so my question is, if we wanted to provide this, what package would we provide it in? Because right now, SDK Trace Base, I think, has the samplers. Other than the composable ones, the composable ones, their composite sampler got added to a separate package that's experimental.
**Jamie Danielson** 50:22 I mean, would it be…
**Trent Mick** 50:26 Go ahead.
**Jamie Danielson** 50:28 I couldn't remember if that was one of the packages that we wanted to get rid of eventually, or if I'm confusing that with… Something else.
So ignore me for a sec.
like, do we have, like, an experimental… we have an experimental entry point, at least, I guess, on… JS, but do we want to put it there, or is that too heavy-handed?
**Trent Mick** 50:59 Yeah, I don't know. I mean, one of the reasons I'm asking, too, is because the easiest way to implement this probability sampler is to use the existing implementation of, say.
of the composable version of that, which we do have implemented. But you can't take a dependency on an experimental package.
SKTrace base can't depend on one of the experimental packages, can it?
**Jamie Danielson** 51:21 I don't think so.
**Trent Mick** 51:25 Yeah, anyway, cannot track. We're discussing with everyone here.
**Jamie Danielson** 51:34 I mean, so we have…
**Trent Mick** 51:36 Sorry, I lost my spot now.
**Jamie Danielson** 51:42 Sampler composite was added in September as its own separate package, experimental implementation of composite sampling spec.
So… I wonder if… and I wonder if something like that would be how we would want to do it?
It's just its own package inside of Yeah, with the idea of eventually moving it in, because that's what we did with logs, right? Or that's what we're doing with logs, I don't remember where we're at right now.
**Trent Mick** 52:12 I guess, and then…
**Jamie Danielson** 52:13 It's own experimental.
**Trent Mick** 52:14 away.
**Jamie Danielson** 52:15 Yeah.
**Trent Mick** 52:16 Yeah.
**Jamie Danielson** 52:17 That way we can have experimental stuff that we can work on without affecting stable things.
**Trent Mick** 52:24 Excellent.
**Jamie Danielson** 52:58 Yeah.
**Trent Mick** 52:59 And I can put, perhaps… Make some ticker out.
Some progress.
So, these two issues came out of the discussion on this one. There was someone who came along and said, hey, the… node implementation of the TraceAdia Eurishia-based sampler isn't the same as the other languages, and then if you go look in the spec, the spec's like, yeah, we didn't specify how it works, it's gonna differ between languages, so…
**Jamie Danielson** 53:31 Oh.
**Trent Mick** 53:32 Do you want good first issue, Nellan? I don't know if it is a good first issue, you gotta understand.
**Jamie Danielson** 53:36 I don't think it's a good first issue. Yeah, it seems more like a hotel funkiness, maybe a good first issue for someone who knows some of the stuff a little bit already.
**Trent Mick** 53:45 Please.
**Jamie Danielson** 53:46 That's what I just put in the chat, is it's hard to… sometimes good first issues are good because they're scoped or clear, and sometimes… It's still…
**Trent Mick** 53:57 This one is.
**Marylia Gutierrez** 53:57 Basically, we need a label for good first issue, if this is not really your first issue.
**Jamie Danielson** 54:02 Right? Good second.
**Trent Mick** 54:04 conditioning?
**Jamie Danielson** 54:06 Good second issue.
**Trent Mick** 54:09 I'm gonna set us up for grabs if someone wants it.
I think this one should be fairly straightforward. There are a couple implementations in other languages, and… There's an open… PR on the… Protobuff to recommend what the size limitation should be, so it's fairly well scoped.
**Jamie Danielson** 54:32 you know.
Nice.
**Trent Mick** 54:40 And then, Marilla, if people want to get started on the declarative config stuff, where do they start?
Because there are a lot of open issues, right?
**Marylia Gutierrez** 54:47 Yeah, I have the project boards that I have the columns for… Okay, let me get you the link.
**Trent Mick** 54:56 No, I gotcha.
**Marylia Gutierrez** 54:58 Yeah, this one, I have, yeah, the column for backlog, like, don't pick up now, the ones that are, like, people can pick up if they want, yeah, in progress, and then… so everything that is on the pickup, can somebody grab it?
**Trent Mick** 55:10 I had my boss independently notice this one, because he's all over GitHub projects. He's like, whoa! There's a project in here, should we be working on?
I'm picking through those ones for that.
**Jamie Danielson** 55:19 Yes.
**Trent Mick** 55:21 The management hat's happy when you have this kicking around.
This is a lot.
**Jamie Danielson** 55:26 Right?
**Trent Mick** 55:28 Yeah.
Okay, I'm not gonna beat this anymore.
Is there anything anyone else wanted to bring up? Otherwise, I'll get 5 minutes back.
I can't take the pain.
Basically.
**Jamie Danielson** 55:42 Appreciate your sacrifice.
**Trent Mick** 55:44 Yeah, yeah, someone else can do this next one.
But… okay.
If that's it, then. Thank you all.
Thanks, Alan. I'll see you next time.
**Hector Hernandez** 55:54 Thank you.
**Marylia Gutierrez** 55:55 Mute.
