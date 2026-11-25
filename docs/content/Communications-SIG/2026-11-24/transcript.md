SIG: Communications SIG
Date: 2026-11-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Virginia-Diana Todea (VictoriaMetrics)** 02:21 Hello, good afternoon, Laura, good morning.
**Reese Lee (New Relic, Inc.)** 03:29 Hello?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:30 Little Mermini.
**Virginia-Diana Todea (VictoriaMetrics)** 03:36 Hello!
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:47 Okay.
**Severin Neumann (Bronto)** 03:53 Hello? Can you hear me?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:56 Okay.
**Severin Neumann (Bronto)** 03:58 My… my earpods just do not work. Maybe the battery is empty, I don't know. Hey everybody, how are you doing today?
**Reese Lee (New Relic, Inc.)** 04:06 Dang, y'all gonna make me go on camera.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 04:10 It's alright, I'm, like, wearing a blanket, basically. Is it cold?
**Reese Lee (New Relic, Inc.)** 04:15 A cat.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 04:16 You know what?
Aww.
**Virginia-Diana Todea (VictoriaMetrics)** 04:18 Oh, that's a nice white blanket!
**Reese Lee (New Relic, Inc.)** 04:23 Yes, actually.
**Severin Neumann (Bronto)** 04:28 It feels like a proper winter this year, right? At least where I live, like…
**Reese Lee (New Relic, Inc.)** 04:34 No, it does. It was… warm for a while, and actually, I was in New York City the first week of November, and it was 70 degrees.
I think that's… like, maybe 22 Celsius? It was warm.
**Severin Neumann (Bronto)** 04:55 It's really warm, yeah, yeah. It shouldn't be that warm.
**Reese Lee (New Relic, Inc.)** 04:59 No. It was nice, but weird.
**Severin Neumann (Bronto)** 05:02 Yeah, that feels weird. Yeah, we now have, like, zero Celsius, so, like, it's getting freezing. Like, they promised snow, so I'm still hoping for that to happen this week, so…
**Reese Lee (New Relic, Inc.)** 05:14 Damn.
**Severin Neumann (Bronto)** 05:16 Hadn't had snow in a while, but let's see.
**Reese Lee (New Relic, Inc.)** 05:20 Oh, like, the past few years?
**Severin Neumann (Bronto)** 05:22 Not a lot, right? Last year, nothing. I think 2 years ago, a little bit.
I don't know, it was just too warm, but yeah, would be great to have some snow from time to time.
**Reese Lee (New Relic, Inc.)** 05:36 Okay.
**Severin Neumann (Bronto)** 05:36 Oh, Lots of people joining us today.
I feel a little bit…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 05:43 Joe, nice to see you.
**Severin Neumann (Bronto)** 05:44 Yeah.
Now I feel a little bit guilty for not being super well prepared. So, Tiffany, Indiana, thank you for filling the agenda.
I'm… I'm very behind in a lot of things right now, so… If anybody else has anything for the agenda, wants to add something, please do.
I think we can get started, right?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:14 Yes.
**Severin Neumann (Bronto)** 06:14 Let me… should I share the agenda? Any… Anybody else?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:19 Please do.
**Severin Neumann (Bronto)** 06:21 Do that? Okay…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:25 Maybe… Before we get started, since we have a bunch of new people in the meeting, We can just kind of… Say who we are and why we're here.
**Severin Neumann (Bronto)** 06:36 Oh yeah, that's a good idea. Many lots of good new faces, so yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:40 I'm Tiffany, I'm a maintainer.
in the Com SIG, and happy to see some new faces.
Who are not new to me.
But are new to this meeting.
**Severin Neumann (Bronto)** 06:54 Yeah, then I go next, so I'm Severin. I'm also one of the comms maintainers and part of the governance committee. Yeah, I'm also happy to see some new faces, and don't feel pressured to… to… to say or contribute anything, so we're always happy to have people also listen in.
But yeah, even better if you want to… Say something, or are interested in specific areas, we definitely can… Spend some time on diving in any topic you're interested in.
**Reese Lee (New Relic, Inc.)** 07:26 Hey everyone, I'm Reese. I am one of the community managers for Ocel, and I just thought I'd drop in and see what's going on and see if there's anything I can help with.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:38 That's awesome.
**Virginia-Diana Todea (VictoriaMetrics)** 07:40 Hi everyone, I'm Dana, I'm a docs approver here for comms and a Romanian localization maintainer. How are you guys?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:56 Okay,
**Heather Cloward (Raintank, Inc. – Grafana Labs)** 07:58 I'm… I'm Heather, I work with Tiffany at Nirvana Labs, and I just stopped by because she said there were some things that maybe the dogs didn't use, so it's my dealers, and I'm happy to… Jump in, I just don't know where yet, so…
**Reese Lee (New Relic, Inc.)** 08:13 Very nice.
**Severin Neumann (Bronto)** 08:14 And let's maybe add something to the attendance. Sorry, I didn't want to interrupt.
**Clayton Cornell** 08:18 Nope, go ahead.
I'm Clayton, I also work with Tiffany and with Heather at Grafana, and I'm also here to basically start trying to help out with documentation on the hotel side of things.
And I spend a lot of time doing hotel-related stuff for Grafana Labs, so it's kind of my wheelhouse, or starting to be more… That way, so hopefully I can lend a hand and we can work together.
**Reese Lee (New Relic, Inc.)** 08:45 Nice! Dang, Tiffany, you got all these people.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 08:47 I know, I… I put in… I put in a hard press in our last team meeting. I was like.
I need help.
**Reese Lee (New Relic, Inc.)** 08:55 Yeah, that's awesome.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 08:56 Oh, I'm… and I promise that I didn't bribe them. They are here of their own accord, but I'm really happy to see that Heather and Clayton are here.
And, Leandro, I don't know if you feel like speaking up, but Leandro is our… design…
**Leandro Caracciolo** 09:09 I'm a designer. Thanks. I'm a designer and design founder on Olive Garden. I work with Caraco College, and… Well, I, I tried to, to, to… to develop some, some screens, some, some solutions in UX and Y.
Trying to explain… Observability to, to, to, to, to… Sure, sure, some common dollars.
Not special people, so… So that's it, and if you need something related to the science, I'm good.
**Severin Neumann (Bronto)** 09:49 Awesome.
**Reese Lee (New Relic, Inc.)** 09:50 Thank you, Leandro.
**Leandro Caracciolo** 09:52 Broke.
**Reese Lee (New Relic, Inc.)** 09:52 I've definitely used your designs in our hotel stuff.
**Leandro Caracciolo** 09:56 Stop.
**Reese Lee (New Relic, Inc.)** 09:57 For, yeah, for the end user's sake.
**Leandro Caracciolo** 09:58 Allow.
**Severin Neumann (Bronto)** 10:04 Cool, I think we have everybody, so, yeah.
I'm… I… I'm, I, I'm… how to… again, like, I… I feel bad for being not well prepared today, but we will get there, we will get there, don't worry. We have a few topics, so Tiffany and Deanna, you put in a few things, maybe we can go over that first, to get this out of the way, to do the… The… the normal, hey, here's a few things we should talk about, and then maybe towards the end we can spend more time on really talking about, like, hey, where do we need help?
What, what, what are the things where… Heather, Clayton, you… you can help us?
So yeah, maybe we start with the… Mermaide diagrams? Is there anything… yeah, go ahead.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:52 Yeah, so, the Blueprints project, which has now been fully bootstrapped, we have 3 published blueprints and 3 published reference implementations.
And, so now we're heading into, like, normal operating mode. What has come to light during the bootstrapping process is that the diagrams are a very critical part of, the blueprints.
And… The, the current way the website works is that you have to use the default formatting for a mermaid diagram in order for the diagram to shift properly.
Between light mode and dark mode on the website.
The default formatting of mermaid diagrams is ugly. But it's also limiting, to some extent, with the complexity of the diagrams that we want to create. So… this came up a little, like, a year and a half ago, I think, and at the time, we just decided, okay, we'll use the default formatting and just go from there.
**Severin Neumann (Bronto)** 12:03 Yeah, yeah, yeah. Remember that.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:04 I wanted to find out… where I need to press the issue, if we wanted to make it Possible to use dark mode on the website with the… with customized formatting.
I don't know where that happens. Is that a doxy thing? Is it, a Hugo thing? I don't… I don't know… is it a mermaid thing? I don't think it's a mermaid thing, but I don't know. Maybe it is?
Just wanted to see if anyone has thoughts or ideas.
**Severin Neumann (Bronto)** 12:42 Patrice probably would have an opinion on that. I think he's still… he's still out of office, right?
I think step one would be that we open an issue for that, definitely.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:54 Okay. In our repo.
**Severin Neumann (Bronto)** 12:56 Yeah, in our repo. I don't think it's, is it a doxy thing?
I don't know, I don't think so. I think at the end, it's maybe something we can fix with CSS.
I would also need to look into that. I mean, I can… I can see if I can find some cycles to… to look into that.
Because, like, I think the situation right now is that, like, most of the time people try to edit it directly in the Mermaid, but that's breaking a lot of things, so we might need to do some research on, like, also what's the best practice for Mermaid's side, and then also, like.
That's maybe also something where you can help Leandro with, like, how can we make it pretty at the end of the day, right? I mean, the one thing is, of course, like, we have the hotel colors, and we have our… range in our… What is it?
very kind blue, but… but I think there's… yeah, I don't think we have a really good… how you say it is, like, because what my feeling is with those mermaide diagrams is, like, it's not only about colors, it's also what the colors communicate, if this makes any sense. Yes. Like, what kind of red are we choosing, what kind of… green are we choosing if we want to highlight certain things? So I think there's two tasks, right? The one thing is how do we set it up, and the other part is where… where we can definitely help… get some designer help, or need some designer help, is, like, more on the… design language.
That could be… yeah. If you raise an issue, maybe you can… Do that, and we can maybe follow up from there.
**Leandro Caracciolo** 14:41 Sure, I can do some color studies on it to see what fits better. Yeah. Just to see what kind of file is it, and where is it?
**Severin Neumann (Bronto)** 14:52 Let.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 14:52 Oh, yeah.
**Severin Neumann (Bronto)** 14:54 Or, Tiffany, do you have a link?
Then I can maybe open it up.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 14:59 Oh, yeah.
**Severin Neumann (Bronto)** 14:59 Otherwise, I quickly…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 15:02 I'm doing probably what you would do, but yeah. The one that has the most complex… Yeah, go to the, kubernetes cluster observability.
**Severin Neumann (Bronto)** 15:15 This one.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 15:16 Yeah, there's a fairly complex diagram in that.
**Severin Neumann (Bronto)** 15:20 This one?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 15:22 Yes.
**Severin Neumann (Bronto)** 15:22 What are the other ones?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 15:23 So they… No, that's the right one.
**Severin Neumann (Bronto)** 15:26 Yeah.
And we actually…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 15:31 It is, right? He did a really great job with it, and it was actually even prettier before.
Well, no, sorry, if you… If you see, like, in dark mode, it doesn't switch to dark mode, right?
**Severin Neumann (Bronto)** 15:44 Oh, yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 15:45 So… It… that's… it's, like, completely incompatible because he changed the default formatting.
Now, if you go to, let's do collector… Architecture, I think.
Yeah, if you go to the… this page, Saren, where's my chat?
**Severin Neumann (Bronto)** 16:07 Architecture, this one?
Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 16:10 Yeah, and you switch to dark mode, you'll see… That… the diagrams… convert.
**Severin Neumann (Bronto)** 16:20 Yeah, but they lose color entirely, right? Instead of, like…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 16:24 Yes, yeah, there's a lot of limitations there, so… basically, diagrams have always been important to technical documentation, but what we've noticed, especially within Blueprints, that it's becoming especially limiting, so we just wanted to maybe raise the issue again and see if we can make progress. So I'll… I'll actually raise an issue.
Yeah. In the comms repo, and then we can see.
**Severin Neumann (Bronto)** 16:50 just to add this for context, Leandro especially, like, this is Mermaid, so mermaid.js.org, this is, like, what we use under the hood. So if you go into the page source.
what people… Right, normally. Oh, I think GitHub is rendering it.
So if we go into the code, this is what people write, right? So they say, like, here's a pipeline, whatever.
And then Mermaid turns it into something, and I think one task is really finding out, like, hey.
here's, like, how you do layouts, where do we put that is maybe then something I can… figure out, or Patrice can help with that.
But I think it's a lot of, like, What can we do and what can we not do to make it, like.
look like hotel, and maybe have some… some language that communicates something, right? Maybe there's some standard languages for pipelines, there's maybe some… standard colors for receivers. Like, there's a lot of things we could do. Maybe let's not try to boil the ocean and start with something, like, basic, where we say, like, hey, this is, like, how it should look like in light mode and in dark mode, and then maybe we can… we can evolve it from there, too. But you will find a bunch of them, right? There's also, like, I think, I think, is it in management, or in… no, in deployments?
There was another one where we had a bunch of, like, diagrams, right? So… and that's the other one, right? Those are not mermaid diagrams, they're, like, SVGs.
And I think today, They're a lot prettier.
But I think I would lean today towards turning them into mermaid.
Because I assume that an LLM understands Mermaid much better than that.
So if we give it to an agent and say, like, hey, explain this page to me, they can make more sense out of the mermaid thing than, like.
the… the SVG that's probably, Not even… it's just text, I don't know. But yeah, okay. But yeah, I think, Tiffany, if you… if you open the issue, and then, like, we can… we can talk about that.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 19:11 Perfect, yep, I'll do that.
it appears that Grafana may have encountered an issue similar to this with our own mermaid diagram, so, I can… I can check with our platform folks as well, to see if that, is… a solution that we can port to OTAL.
**Severin Neumann (Bronto)** 19:41 Perfect.
**Leandro Caracciolo** 19:43 Awesome. I'll take a look at it.
**Severin Neumann (Bronto)** 19:46 Cool.
Okay.
Anything else on that topic?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 19:54 Nope, over to Deanna.
**Virginia-Diana Todea (VictoriaMetrics)** 19:59 Yeah, awesome. So yeah, for the remaining localization, things are looking good with the new approver that we… that we had joined several weeks back. So from my point of view, everything is fine. We have been able to approve stuff, and everything is working correctly.
So, as you wish, if you want to stay longer as… in the… in the list.
or the SIG, to overview, but from my side, so far there have been no issues.
So, just wanted to give you this, this update.
And we also have.
**Severin Neumann (Bronto)** 20:35 Here, yup.
**Virginia-Diana Todea (VictoriaMetrics)** 20:36 Yep, and we also had, like, in the last couple of weeks, new joiners, because we kind of, like, spoke with each other, so we kind of, like, asked for more help.
And we have more people right now, hopefully tomorrow we can onboard, but they're already passing some… They have passed some PRs in the Romanian localization, and also in the main documentation repo. Tiffany was, I think, handling a couple of those. So that's… that's pretty good, it's picking up.
**Severin Neumann (Bronto)** 21:05 Okay, so that means, like, we could… Remove… Marylia and myself from the Docs Approvers Group. I mean, the good thing is, like, you can add us back, or we can add ourselves back anytime we need to. I have not looked into any Romanian localization PR for a few weeks now, so… but by then, I assume it's really working. So yeah, I think that's totally fine, I can just… drop ourselves, and I mean, if you ever have the feeling like, hey, we need… we need assistance with that again, and like… You're good, yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 21:41 Yep, perfect, thank you. Sure, so I will go to the next one. So this one is an issue that I opened several months back. So basically, it's a proposal to do a dashboard, so let me check if I can share this.
Just once.
Yeah, you have it already there, Sorry, I guess he just, yeah, yeah, that's the issue.
And basically, the, yeah, that's… basically, I made the screenshots of… of whatever is happening there. That's the prototype.
and the raw data, so I gave, Marylia, Vitor, and Patrice access to the dashboard and the raw data, but obviously anybody can ask for the access they want, so I just didn't make it public to, like, everyone, because, you know, I think… From the beginning, we just wanted to have, like, a look-see, you know, to see if this prototype works.
And then, obviously, test it out with localizations. But this is, like, the… my proposal. So, basically, we can have, like, a nice, dashboard inside, Looker, or whatever the name is right now.
And we have, like, total PRs, merged PRs, open PRs, unique contributors, and select the locale, so we can see there the drop-down menu, we can select the correct localization.
type of contribution and project status. So, it's a very minimal, basic type of dashboard, but it's good for, I don't know, localization, or maintainers for localization, or even us from the doc side to just view what's the current status, take a look at it.
And yeah, just, just basically habits, something like that. Obviously.
We need to take a look at the road data, see if everything is correct, if, you know, from all the guidelines, you know, whatever regulations there are around that.
My dad.
If you have any time to review this at some point, just… just let me know.
**Severin Neumann (Bronto)** 24:09 I mean, if you can… do I have access to it?
**Virginia-Diana Todea (VictoriaMetrics)** 24:13 That's true.
Yeah, can you ping me your email address, and I'll give you on the spot?
**Severin Neumann (Bronto)** 24:20 Okay, yeah.
**Virginia-Diana Todea (VictoriaMetrics)** 24:21 Nope.
**Severin Neumann (Bronto)** 24:21 I can request it here.
**Virginia-Diana Todea (VictoriaMetrics)** 24:23 Yeah, exactly.
**Severin Neumann (Bronto)** 24:24 I request now with my work account, I think that's not really making any difference.
So how… how… how much… my feeling is there's not a lot of maintenance effort on that one, right? So my feeling is, like, the moment you have this up and running.
It kind of just works.
**Virginia-Diana Todea (VictoriaMetrics)** 24:42 me.
**Severin Neumann (Bronto)** 24:43 Except we change anything, or if you want to add a feature. But right now, it's more like… You did it once, and it works.
Kind of forever thing.
**Virginia-Diana Todea (VictoriaMetrics)** 24:54 Yeah, exactly. Yeah, exactly, so I explained, like, in the issue how, it was done, but obviously I can test it further if, yeah, if there's any further maintenance required. First of all, I wanted to check the data itself.
If… if we agree that everything is fine there, you know, we are not breaking any rules or… or whatever, And, yeah. Basically, I think this one is connected. It was a bit long time ago, but it was connected for the last thing, as you can see, it was in October, and I will check, how we can get more, fresh data and stuff like that. I still need to go back to it, obviously.
I already forgot what was happening after one month. But yeah, so that's the gist.
So I gave you access to it. Severin, let me also give you access to the raw data.
You can take a look at that whenever you have.
**Severin Neumann (Bronto)** 26:01 And what would be the next steps from there? Like, if we say, like, hey, we want to kind of make this official, like, would you… would we need to link this from somewhere, or… Can you, like… or have you lined us out in the… in the issue.
**Virginia-Diana Todea (VictoriaMetrics)** 26:17 Yeah, yeah, so as Patrice said, and that's a good point, I mean, I don't have any, whatever, publication rights on Looker.
Yeah. Or, I don't know, elevated permission. So this was, for me, let's say, more, more or less like a local project. Okay. And let's say, if we share that with… so if… first of all, you guys like maintainers, you like this idea, everything is fine. We can share with the localization team, see, like, if we can make it better, or if it's… the idea is to have something also quite basic and easy to use.
**Severin Neumann (Bronto)** 26:51 If they…
**Virginia-Diana Todea (VictoriaMetrics)** 26:51 like it, and we want to use it, then we could go ahead and actually publish it, because right now it's… basically local for me, but I think Patrice and whoever has access, we can actually publish it on Looker, and, like, whatever dashboards we have at the moment in Looker for OpenSelemetry will be there, existing with the rest of the others.
**Severin Neumann (Bronto)** 27:14 Okay, yeah, I will… I will also take a look, and then we can maybe see how we… how we… how we establish that.
**Virginia-Diana Todea (VictoriaMetrics)** 27:19 Okay.
**Severin Neumann (Bronto)** 27:20 Makes sense.
Cool.
**Virginia-Diana Todea (VictoriaMetrics)** 27:22 Coco, yeah, and… Let me just give you… access. Anyway, once I find it, right, and this… the second one was about, the other issues, so basically how I'm trying to… I received the final permission.
**Severin Neumann (Bronto)** 27:44 Okay, the collector's thing.
**Virginia-Diana Todea (VictoriaMetrics)** 27:47 Yeah, I received, validation from the collector, so Tiffany was helpful, so, provided me some context how we can start next, maybe create, like, Start from a performance… route there, or manage collector in production. I just wanted to validate before I start to open PRs or whatever, if everybody agrees, if we should do like that, or…
**Severin Neumann (Bronto)** 28:21 I mean, my main point with that topic is, like, I mean, if the collector SIG Is in favor of it.
And Tiffany, you have the best overview of that, so I also think, like, if you're happy with, like, what I just opened up here, Let's start with the first piece of it, and then go from there, right?
Yeah, sure.
**Virginia-Diana Todea (VictoriaMetrics)** 28:46 Josper.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 28:48 I think, I think Deanna did a good job of getting… Input from quite a few people, and it seems like, There's definite interest in having something like this.
I do know that it can be a, a touchy subject in the collector's SIG, so, We might have some… some… Hurdles to… to overcome as we work on it, but… so just… that's just kind of a heads up to be open to all the feedback you're gonna get, because there will be thoughts.
The Manage Your Collector in Production section doesn't exist yet.
So, that was… Yeah.
This snapshot was part of a refactor that I was unfortunately not able to execute as quickly as I had planned, but that's part of why I'm hoping that Clayton and Heather will will join our, our project, and we can make actual progress on that. So I think I put in the comment where you can put it for now.
And then we'll move it, we'll refactor it, once we get to that stage.
**Virginia-Diana Todea (VictoriaMetrics)** 30:03 Okay, so basically just create a top-level page, performance, or something like this, and go from there, right?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 30:11 Yep.
**Virginia-Diana Todea (VictoriaMetrics)** 30:11 Okay, cool. We're gonna contribute to that. Yeah, yeah.
Yeah, no, that sounds good. Anyway, I will start working on the first PR, get a sense, with the Sea Collector, if that's okay with them, before, like, going full… into… into other stuff. Also, I saw, because that… that for me was pretty interesting, the… the hotel Arrow involvement, so they gave some, interesting feedback, and they said they're interested in that, about the benchmarks and whatever, so they also gave… and I saw that, there is an interest, although… okay, I'm not sure how, Arrow overlaps with collector, but I know it overlaps, and this is not the first time I've seen them, kind of, like, as soon as somebody, wants to add something about a collector, they're interested in it. I mean, that's pretty great, but I just wanted to know, like, if that's a… Like a valid, A comment, like, a valid reply from their side.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 31:20 I think it touches on a bit of the… touchiness that I referred to,
**Virginia-Diana Todea (VictoriaMetrics)** 31:26 Yep.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 31:26 the… the Hotel Arrow project is attempting to basically create I might misstate this, but a more performative version of the collection.
And so, for specific, very specific circumstances. So it's a little… it's a little tricky there. We're gonna have to navigate that.
But I think overall, what you want to add is valuable. It's just… We're gonna have to… yeah, there's gonna be a lot of opinions. I'm trying to be diplomatic about how I say it, but there are going to be a lot of opinions here, so, we'll just have to… have to work around those and work with them as well. One other note is I highly recommend doing small PRs.
**Virginia-Diana Todea (VictoriaMetrics)** 32:18 you know, even.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 32:19 Even if it means that you're just adding a couple paragraphs at a time, it's… you're gonna get Much faster reviews, and, things will… You'll… your progress will be better than if you attempt to put up larger PRs, so…
**Virginia-Diana Todea (VictoriaMetrics)** 32:37 Yeah, no, that's very sound advice, and I know, because, like you said, there are going to be a lot of, feedback, so yeah, better to be safe with a small PRs.
Awesome.
Okay, yeah, that's it from my side, so I think we have half an hour to discuss maybe other things. Thank you.
**Severin Neumann (Bronto)** 33:00 Okay, thank you, Deanna. I think that's a really good thing, and also seeing a little bit more progress again on the collector docs.
in that regards, it's really good. I think the benchmarks have been a topic forever.
Yes. That's good, it's good that something is happening there. Awesome.
Yeah, I think then we have a little bit of time left for talking about, like.
where we need help, and how people can jump into these things that need the most attention right now. Tiffany, I don't know if you have any things in mind already?
Aye.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 33:39 Turn…
**Severin Neumann (Bronto)** 33:40 but I'm more than happy to hear anybody's else first, so… yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 33:44 Yeah, I think, Clayton, especially, Clayton works, on our alloy docks, so he's very familiar with how the hotel collector works, and so… I'm hoping that, his interest and time will permit him to help me with the, the refactoring that I had basically abandoned earlier this year, for valid reasons, but I would like to actually fix the collector documentation.
It desperately needs it.
as far as more general needs, I do think that… reviews, like, helps with… help with reviews, whether those are blog posts or docs or anything, would be where we need the most help at this point, I think.
And, you know, Heather… Coming into it with maybe not a lot of hotel knowledge.
the reviews that you can help with most are literally copy edits. Now, I will say that Copy edits have… like, your… the need for copy edits has shrunk now that more people are using generative AI to create the docs. Like, there aren't as many typos or… Incomplete sentences, or that kind of thing.
But it actually… Means that the copy editing is harder, because now you're reading for clarity.
like, I read a PR, or started to read a PR yesterday that was AI-generated, and All of the words… I knew what they meant.
But once they got put into sentences and paragraphs, I literally could not grok it. Like, it was not coming together, and… And I… at that point, I just pushed back a little bit on the author and said, can you give this another shot? Like, it's… It's just not really readable in its current form.
That's the kind of stuff that we're encountering a lot more, these days, is… Just trying to… B-A-I, if I… the, the… the tone of… of the documentation that's getting created.
That's… Severin, feel free to jump in there.
**Severin Neumann (Bronto)** 36:17 No, I think that's, I think at the end, my question would have been, like, where people see their own expertise, and would they… What they… what they can help with, and… Collector definitely needs help. For me, the other part is always, like.
and we technically have a few people that wanted to look into that, but the whole, like, how do people get started with OpenTelemetry, right? That's like… if I would have all the time in the universe, that would be, like, the one area I would put the most time and energy into, because this is, like… it's like, when I was back at Cisco, a colleague of mine told me, like, hey, getting from 5 to 10 with OpenTelemetry is easy, but getting from 0 to 1 is a nightmare.
this has not changed a lot. I mean, AI made a lot of those things easier. If you don't care about OTEL at all, and you can just tell your agent, like, instrument me that thing, and then you don't care about it, but the moment you say, like, hey, I want to understand what's going on there, and then what's happening here, and maybe go through it step by step, that part is still not solved, so if anybody feels very, very interested in that… I mean, Lisa is making progress on the videos.
That's… that's really good. So, you still need to figure out how to… how do we keep the videos and the docs in sync?
But yeah, that's maybe another topic, but…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 37:46 Yeah, and I know that, Julia has a lot of interest in that.
**Severin Neumann (Bronto)** 37:51 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 37:52 And she, I think, the synchronous meetings, just… we've… I think she and you, Severin, have been crossing paths, because I think, you have some ideas about how you'd like to see that progress. So, yeah, that is definitely a good idea. There's… There's also, from, like, a tech writer's perspective, a lot of things that can be fixed in this documentation. There's consistency issues.
there's… Like, TOC and, information architecture sprawl. Like, things have little organization in some places, So, I would say, Yes, your interests and abilities are obviously number one, but… You can pick pretty much anything, and it will be a huge help to us at this point.
**Reese Lee (New Relic, Inc.)** 38:52 Do you have, like, a list of, you know, pages or areas in the docs that Should maybe be looked at first?
For that kind of stuff, or kind of just start anywhere?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 39:07 I'm not aware of a list, docs-wide. There is, an analysis that I did of the collector docs, and that is in the projects folder in the comms repo.
It has a copy of the proposed architecture that I, the architecture I proposed, and then it has, like, analysis that I did of, like, what's missing.
pretty out of date now, because I did it, like, a year and a half ago.
But… I… like, yesterday, that same PR where I had trouble just reading it.
identified that we are missing, A section for, like.
How do you do good instrumentation?
at a language-agnostic level. Like, what are those best practices?
Now, we have the blueprints and the reference implementations, and there might be a good spot for that there, but, There are definitely some, like.
Best practices or, like, key ideas that we want to impart to people trying this out on their own, and there's not a good spot for that right now.
So, it's… It's a vast docset.
And… No one has done an analysis Of the entire thing?
So, no. The very long answer to your question is no. There's no list.
**Reese Lee (New Relic, Inc.)** 40:48 Got it, okay.
**Clayton Cornell** 40:49 Coming at this from what I hear, just to join in on that, is this discussion, finally.
Since I haven't said anything yet, There's two places in the Ally Hotel documentation that are always a pain point, and that is that 0 to 1 step that you mentioned, Severin. That's a really, really… hard to fill that gap, and that's the same problem we have in the OTEL documentation. I see it there. The other spot that the developers complain about, into my ears, is always the reference documentation is scattered.
And it's not always formatted the same way, so they get expected to be one way, and then they change two pages further on, and it's presented differently. So if somebody's looking for a place to jump in, those two areas are always the first two places I go and look.
Is that zero-to-one step, can we get people onto the product, and understanding the core concepts really well? And once they're there, can they find those bit and critical pieces they're looking for?
**Severin Neumann (Bronto)** 41:53 Yeah.
I think that's also… what you're pointing out is also a little bit of a problem that we had in the past with the information architecture, that we, like, mixed all of that into one big mess. Java is, I think, the only language that tried, really, to resolve that.
Because I think what we technically would need, but as I said, this is more like a… This is more something where… where we need someone who… pushes forward and really is like, hey, I want to lead this effort, is really figure out, like.
okay, this zero to one, how should this look like in 2026, right? I have ideas about that for years, but implementing them is really, really hard.
And then the other part is like, okay, and if we have that part.
Like, and maybe it's language agnostic, maybe it's focusing on a few key languages, maybe it's… So we also tried to… the one thing we tried a few times, and I'm not really sure… like, we tried to have one getting started across all their languages, and then, like, you can say, like, oh, I'm a Java guy, I'm a Rust guy, and then here's now the same story across all languages.
I'm not sure if this really works.
Yeah, at the end of the day, I think we need something where we tell people, like, hey, this is how you get started with open telemetry at a very broad sense.
and then what you said, like, and then we need reference documentation. If someone says, like, hey, now I get it, and now I want to dive deeper into… into this and that topic. So, I think the closest to that right now is really, like, the thing that, that Lisa is working on, and more in a… more in a video way.
And I must admit, like, I'm… I'm trying to help her with that, but she's, let's say, doing a one-man show on that for a long time now. That also means, like, she has not put out a video for a long, long time.
But I think something like that is maybe more meaningful for a beginner's journey, if you say, like, okay, we do it in JavaScript.
just, we pick one language, we do it in that language, and then give it out. But I really don't know, and they said, like, my problem is really, like, attention for that, so if people care about that, this would be really, really helpful.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 44:19 I think you touched on a really important point here, which is… There are lots of little things that need to be done, but some of the some of the things are much bigger. They're going to require more buy-in from different parts of the project. They're going to require moving pages around, which is always tricky in this particular website. It… And it's going to require a lot of planning and thinking. Those projects, we need someone to, like, take them on as a leader.
Like, the maintainers, while we know that they need to be done, we don't have… The… the… the hours, the time, the brainpower to… Be the leader on those projects at this… Maybe someday. Maybe someday. But right now, that's… that's where we're at.
**Reese Lee (New Relic, Inc.)** 45:22 Okay, that's helpful.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 45:27 Heather or Clayton, do you have any questions?
Like, anything… beyond where you could get started, is there anything that we can answer for you? You've got… you've got some very knowledgeable people on this call, so… Any questions? Now's a good time.
Yeah, Leandro.
**Leandro Caracciolo** 45:50 I'm just, just… What you need, basically, is there something more visual to explain this stuff to the developers that are beginners on it?
Something like infographics or animation, something like that could help in it.
Or a better, better… Better architecture.
Of the elements to explain it for the beginners.
**Severin Neumann (Bronto)** 46:21 Definitely. I… yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 46:23 Yes.
**Leandro Caracciolo** 46:23 Hey, I mean…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 46:27 the… the balancing factor of that is, though, we do need the text to be digestible as well, because most people are pointing their agents at our docs, right? So, it's… I… yes, the visual component is, either lacking or very out of date, I would say.
So yes, there's definitely a need.
But yeah, we also… the text, we also need to… to make things more findable and digestible, I would say.
**Reese Lee (New Relic, Inc.)** 47:06 On the, like, document architecture piece, is there… so, I think you mentioned Java.
That's probably… the… Where they get the most, a FERT, I guess, Is that… would the Java, like, docs kind of be the… you know, the… I guess I'm trying to ask, is there any language or component, that has, like, an ideal, or the most ideal, like.
architecture.
That we can, like, follow.
**Severin Neumann (Bronto)** 47:44 I would say Java, yes. I mean, it also is now… like that for a long time. I'm not sure if it's still… But the idea was really, like.
And this goes back to Clayton's point.
the idea was really, like, to turn it more into a reference documentation.
Versus, like, reference documentation that's mixed up with the Getting Started Guide.
Right, and the structure that… so this structure was mainly suggested by Jack, who I would say is one of the people who knows best, like, how to… how open telemetry is structured, so this structure also follows, kind of.
the… how do you say, like, architecture of OpenTelemetry, right? Did we say, like, If we ignore the… the intro and the getting started, but then we say, like, hey, here's the API, here's the SDK, here's the configuration, and then here's, like, everything that builds on top of that.
And in that particular case, exclusively for code-based instrumentation, and then everything else, like the Java agent and whatever, is living somewhere else, so that was a little bit the idea of that.
So yeah, I would say, like, for any language that anybody would want to update, so if someone says, like, hey, I want to go after Go.
that could be a re-architecture, but together with the SIG, right? I mean, one thing is definitely to see, like, hey, does the Go SIG do a buy-in here. For example, the .NET SIG, they have their own architecture, I would say.
And this is more about, like, syncing with them.
But, but there we go in a more complex, discussion.
Maybe a less technical thing, especially for Heather and Clayton. Are you already in the OpenTelemetry or in the CNCF Slack? So are you signed up with that one already?
So, because that would be the… best place to… to chat with us, so we have the hotel comms channel.
That would be the place, like, if you have any questions, if you want to follow up async.
Or want to send any of us a direct message, that's definitely the best place to To… to chat.
**Heather Cloward (Raintank, Inc. – Grafana Labs)** 50:28 I mean, I'm… I don't have a lot of experience with OTEL in particular. I work for Grafana Labs, which does observability, so I have that.
Kind of background, at least. And I'm, you know, I'm happy to take a look at the beginner stuff, but that, again, like you were saying, will take some time, and I don't know, like… I guess I would create an issue, and… or is there already an issue, maybe? I don't know.
**Severin Neumann (Bronto)** 50:56 I mean, create issues, and if we find duplicates, or see, like, hey, this exists already, then we link it back.
There's no issue with that. I think at the end, what I always say for people joining that are new, to OTEL especially, this helps, right? Because, like, what you talked about, the zero to one, I mean, if you don't know anything about OpenTelemetry and have the Grafana background, and you read some of our docs, and they're like.
I don't understand what this sentence means, then you're probably not the only person having that question, right? So this is definitely helping.
So, yeah.
**Heather Cloward (Raintank, Inc. – Grafana Labs)** 51:37 Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 51:37 Mmm.
**Heather Cloward (Raintank, Inc. – Grafana Labs)** 51:38 Thanks.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 51:39 Another… another kind of easy… way to go in. I mentioned that new PRs need… Less of, like, the kind of basic copy editing.
But our existing docs were written by humans, and by many different humans. So, there are absolutely, you could go in and just, like, pick a page.
And, I mean, even just reading through the page, like, you're gonna… learn and ingest, but like Severin said, you're also going to figure out what doesn't make sense. And then you're also gonna find all the typos, and the bad grammar, and the style inconsistencies, and… it… it hurts me sometimes to look at some of the pages in our docs. It… it's… it's painful. So that's kind of, like, low-hanging fruit, like, just… Pick a page and go in and edit it, like…
**Severin Neumann (Bronto)** 52:41 Yeah, absolutely, yeah, yeah.
**Reese Lee (New Relic, Inc.)** 52:45 Tiffany, I know exactly what you mean, because I've, like, come across a lot of those.
But now it's like, aww, I know a real human wrote this, you know what I mean?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 52:55 Right?
Yeah, it's, there's definitely, like, a before and after, for sure. But yeah, it's… Lots of… yeah, there's lots to be done.
Sorry.
**Reese Lee (New Relic, Inc.)** 53:13 And then I'm guessing, like, each page you would prefer, like, one PR per page.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 53:20 Or even a section. Some of these pages are monumentally long.
And that's something we could look at, even breaking them up, if it makes sense.
But from… like, if you're going purely for low-hanging fruit, just go in, find a chunk of things to edit. I mean, you… we've all worked with the engineers and the SMEs who are going to be reviewing this, right? So, we know Kind of what their tolerance is for… for a single PR review. So kind of just use your best judgment on how much to put in there.
Because…
**Reese Lee (New Relic, Inc.)** 53:58 Got it.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 53:59 It's… yeah.
If you want to get eyes on it, yeah, keep it small.
**Severin Neumann (Bronto)** 54:13 Awesome.
Any… any more questions, any more thoughts?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:26 I guess, to Leandro's point, like, if… you, Reese, Heather, Clayton, whoever is seeing this and decides to go in and edit a page.
If you think that an infographic, some kind of diagram, if something could improve that page.
then reach out to Leandro in Slack. Leandro, are you in CMCF Slack? Yeah.
**Leandro Caracciolo** 54:51 Yeah, yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 54:53 Because I… there's definitely a gap there. And so, a lot of… a lot of those docs pages were built incrementally as the feature was built, and so the holistic view of, like.
What should we be telling users on this page is missing, and so an infographic or diagram or something could help.
**Leandro Caracciolo** 55:14 Okay, I'll check it out. I'll take a look on the documentation pages, and… I will propose some visual solutions for it.
And I'll show it on Slack, and we can discuss.
What… what can work or not, and… Unless that's the way, to explore new one, you know.
New visual solution.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 55:37 That's.
**Leandro Caracciolo** 55:37 group.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 55:39 Yep, and some of our contributors may come to you and say, I'm working on this page, and I think it needs something.
**Leandro Caracciolo** 55:48 Okay,
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 55:50 But I think, I think, I think that would be great.
**Leandro Caracciolo** 55:54 Good call.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 55:55 collaboration.
**Leandro Caracciolo** 55:58 Awesome, awesome.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 56:03 That was my last thought, Severin. I know I've talked a lot, so…
**Severin Neumann (Bronto)** 56:06 No, no.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 56:07 I didn't know that.
**Severin Neumann (Bronto)** 56:08 The brain is empty now.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 56:10 So…
**Severin Neumann (Bronto)** 56:11 You get all the time talking, you, you, you deserve it. You brought two more people.
So I'm excited. So, yeah, all I have to, to, to say is, like, I'm… I'm… I'm looking forward to… to see you all help us. This is really urgently needed right now.
And if there's anything I can help with, then Slack is, as I said, the best place to reach out.
just ping me on the hotel comms channel. I mean, as always, let's keep as many conversations as possible public.
But if it feels like something you'd like to discuss in private, then yeah, we have… We have DMs and everything for that.
And yeah.
If there's nothing else I said, thank you, and… And we're talking in two weeks from now.
**Reese Lee (New Relic, Inc.)** 57:01 Thank you, everybody!
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 57:03 Thanks, Al.
**Leandro Caracciolo** 57:03 Right?
**Severin Neumann (Bronto)** 57:04 Thank you. Bye-bye. Thank you.
**Virginia-Diana Todea (VictoriaMetrics)** 57:05 Am I ain'.
**Heather Cloward (Raintank, Inc. – Grafana Labs)** 57:06 So… Bye.
