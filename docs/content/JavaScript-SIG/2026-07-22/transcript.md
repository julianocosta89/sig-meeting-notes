SIG: JavaScript SIG
Date: 2026-07-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 00:45 Hello!
**Trent Mick** 00:50 Hello. Great.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 00:52 Hmm? You?
**Trent Mick** 00:55 Gettin' on.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 00:56 is a one-on-one?
**Trent Mick** 00:58 Recorded one-on-one.
We are finally hitting 30 here, so feeling what the rest of the planet is feeling, I think.
Vancouver.
30 degrees, so yeah, I mean?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:28 Let's see how it is. Today was raining a lot here.
Yeah, it's 25.
**Trent Mick** 01:36 But it's humid where you are, right?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:39 Fair.
**Trent Mick** 01:40 At least I don't get that.
For me.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:46 There's not… no smoke today, so yay.
**Trent Mick** 01:51 We haven't had that yet this year.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 01:56 Yeah, my view, when, like, I would look, I would not see outside of my window was just, like.
Spoke, go ahead.
**Trent Mick** 02:10 Mark, I'm… Maybe because… well… Yes, I'm dumb, but also slow. I'm missing what the connection is on the… contrib repo release, please, thing, and that, that, the DB… instrumentation issue that you say. It's like, what's the connection? Why?
**Marc Pichler (Dynatrace)** 02:31 The… that's a second thing that didn't have the same configuration.
**Trent Mick** 02:38 Oh, only… okay, because it fits in the SimConf migration theme. It's not actively…
**Marc Pichler (Dynatrace)** 02:42 It's not…
**Trent Mick** 02:43 Thanks, yeah. Okay.
**Marc Pichler (Dynatrace)** 02:44 Yeah, we… I think we should include it in the release.
**Trent Mick** 02:49 I think it makes sense. If they release one of the things saying is, we've completed HTTPDB migration, then for sure, yeah, yeah.
And if you don't have bandwidth to work through the details, I'm happy to take that this morning.
**Marc Pichler (Dynatrace)** 03:05 I think I just pushed a commit,
**Trent Mick** 03:10 Okay.
**Marc Pichler (Dynatrace)** 03:11 just before the meeting, I might have to push another one, because I think Lint will fail.
I was a bit too… Quick on that one. Okay.
But if you can review that one, I would appreciate it. Yeah.
**Trent Mick** 03:27 Will do.
**Marc Pichler (Dynatrace)** 03:34 Let's see if… Yeah, just push the fix-up commit, because Lint was failing.
I should be.
We're good now.
Alright, I guess let's… Get into that, Trent, I guess this is your topic here.
Asking for a review on, fail fast on propagator creation.
**Trent Mick** 04:23 So, yeah, I mean, mainly with this is I'm working through all of the… create step code, so creating SDK components.
From declarative config thing, because that started a proposed thing to move, into this create from config.ts.
From most of the utilities dropped in this utils.
TS, which mixes up.
creating stuff from config and creating stuff from environment. So one thing I… that was a refactor thing that I started a while ago that I wanted to do. I'm using that move as the opportunity to go through all of the implementations for these things and change… the semantics… we'd have… we have a mix of semantics from fail fast, which is what the spec recommends, or just diag.warn and ignore in… in various cases.
There was some other issue, I can find the link where I was… proposing… we do the fail fast thing, but I hadn't had follow-up discussion on that. I'm assuming people are okay with that. So, the way it's set up is if… if… or what I'm moving towards is if… Node SDK's handling of declarative config cannot satisfy something in the declarative config, it just throws, and there's a try-catch at the top level that just returns a no-op SDK in that case.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 05:52 Yeah, I was already review… starting review of this one this morning.
**Trent Mick** 05:55 Oh, awesome.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 05:56 Yeah, so, yeah, I think I just had, like.
some thoughts about, like, just the error message of things that… some things that could be clear, but I… I'm putting the notes in. I will send it by the end of the day, just… yeah, but just nits, nothing… nothing major.
**Trent Mick** 06:10 Okay, so I've been working on the meter provider next.
Which gets interesting. I hadn't realized that the… Is the separate… I haven't even created the PR, just a local, feature branch on that one. That one, obviously, that's bigger than… The data model for propagators, but… My god.
stuff in there. Anyway, there's a whole… metrics is just big.
And like… the… the functionality in the Prometheus exporter doesn't map Exactly to what the declarative config stuff is for that, and… I hadn't really internalized that So right now, a meter provider thing in declarative config, we handle the… Which is it?
the periodic section, the data model under periodic, whatever, so… because we have a periodic metric reader. But there is not a poll metric reader, or we don't handle that side yet. There's no pull metric reader thing. The exporter is the reader, but in the declarative config data model, it reads as… or the model lays out having a pole metric reader that accepts an exporter, so it's… it's a little bit inverted there, so, kind of the pattern that I was using for building these things changes a little bit, but anyway.
I'm probably… I'll have a PR for that soonish, but I'm gonna defer some of the edge work there to separate work, because I don't want the PR to get too big.
Anyway, whatever. That's the status on that stuff.
**Marc Pichler (Dynatrace)** 07:51 Yeah, the, reason why the… Prometheus Experter is, metric reader was kind of back in the day when we were working on the metrics SDK.
We read the spec, and the spec didn't say explicitly that we need a, Pull Metric Reader and the push metric reader, so we decided to just take the easy route, and… have the Prometheus exporter, which was the only one that, It's not a push metric exporter, just have a tool.
To think, and…
**Trent Mick** 08:36 I was gonna throw my hands up and cry foul and start screaming, and then I went to look at the spec, and it has a specific section there saying you don't need to do this kind of thing, so I'm like, fine. You follow the spec, I can't complain.
**Marc Pichler (Dynatrace)** 08:47 Yeah, we… it's one of the things that I wish we decided differently, back in the day, because there's spec now written Based on that existing, and also, we are the only ones that do it this way. There's, I think, no other SDK that does the same thing. Everybody has the push and pull metric readers, so…
**Trent Mick** 09:21 Well, we've got a breaking change coming up, if you want to cancel every other holiday you had for this summer.
Try to squeeze that in.
Yeah.
**Marc Pichler (Dynatrace)** 09:32 I wonder… I wonder if it… No, I'm not gonna go there.
**Trent Mick** 09:39 go there, that's done that.
**Marc Pichler (Dynatrace)** 09:40 Okay.
It does sound intriguing, changing that, I have to say.
**Trent Mick** 09:48 Oh, sorry, another lurking thing… Sorry, I didn't even write this down. That comes to mind on the declarative config stuff is the exporter still… Handle reading environment variables unconditionally.
So… I don't know if we… want to, but I don't… I haven't… investigated to know… I'm a little bit scared of the exporters, just because there's so many, and any PR change you do there turns into a big thing, and there's still, like, legacy craft sticking around in there, and I don't know when we get to the tipping point where we want to do big changes there, but for a declarative config, I don't know how straightforward it'll be to do kind of the similar thing that we did with the SDK trace package, where we have… A code path there for creating these things that will not use the environment, which is what we want for declarative config.
Or we deal with some kind of workaround. I don't know. Had… has anyone else thought about that yet, or not?
**Marc Pichler (Dynatrace)** 10:46 I've been thinking about what to do with the, exporters, and… the next step that I was considering is to, introduce a new interface to create the exporters. That doesn't apply at the… Environment variable config stuff.
And have that be, like, the new recommended entry point for folks that want to instantiate an exporter.
And… while doing that, I would also take the opportunity to clean up a little bit the… clean up the public API of that a little bit, because One of the issues that we have right now with the, with these exporters is that… the… Options that we pass in have kind of grown, organically. It's not… Like, the naming is off, in… in many cases, and, yeah, it doesn't fit together very well. There's duplicated config, that does the same thing, but applies in a different order, and that's why, like, most of the config code is so complicated in the exporters, because we wanted to keep backwards compatibility for that. So if we don't have to do that, then it's a lot easier to… deal with in the future.
**Trent Mick** 12:27 And you think you would end up changing the… Number of packages, or which… Or… or probably not.
If we were to do that.
**Marc Pichler (Dynatrace)** 12:37 I… I would change the number of packages. I've been waiting for SDK 3.0 to do that, though, because one of the benefits that we will get from going to 3.0 is we will bump the… supported Node.js version 2.22, or… I think 22 is what we kind of settled on.
Which means that we will have, native fetch in… Node.js.
Which means we don't…
**Trent Mick** 13:08 We're talking about changing the implementation, too.
**Marc Pichler (Dynatrace)** 13:11 Yeah, we don't need to have… an HTTP transport, and, like, we don't have to have the different transports anymore. We can just consolidate everything.
Which… We…
**Trent Mick** 13:26 It's only in the browser side that we have support for different transport centers, isn't it? Like, I would assume…
**Marc Pichler (Dynatrace)** 13:32 Yeah, it used to be that we have support for different transports in browser, but now it's all patch and fetch with Keep Alive.
Okay. I think XHR and Send Beacon has been dropped.
So, everything would be fetched now.
**Trent Mick** 13:54 Are you sure you want to switch to Fetch? Like, I'd gotten the impression that… I don't know, I mean, HTP… Request as a good old trustee.
Done in my books, but, okay.
**Marc Pichler (Dynatrace)** 14:08 Yeah, if they're… I guess it would be nice to clean up a bunch of the… stuff that we're doing right now, and just switch to Fetch. It's not a requirement, though. As long as the interface that we provide to users is Stable in the end, and, doesn't apply the…
**Trent Mick** 14:36 You mean all the configuration options, I guess. Like, certainly, there… if you're.
**Marc Pichler (Dynatrace)** 14:39 Yeah.
**Trent Mick** 14:40 about what… what… Config options to expose it, certainly.
nice to want to use Fetch, because it's gonna be same across browser and whatever, and it's gone through a better standardization process and stuff, so presumably that's… yeah, I can… okay, I can understand that.
Okay, a bit of a challenge then. If I… if that's something that you wouldn't want to do until after 3.0, But if I want… want.
declarative config. Before 3.0, Can you think of a… a reasonable middle ground there? Could we use the existing packages and provide this… this… Experimental alternate path for creating exporters.
in each of those packages, so it'd be… I don't know, I guess we'd also take the chance to, instead of creating new classes, it would be, create functions for these things.
**Marc Pichler (Dynatrace)** 15:33 Inc.
**Trent Mick** 15:35 Okay.
**Marc Pichler (Dynatrace)** 15:36 Yeah, I think the middle ground would be to… do that, that was also… like, one of the thoughts that I had, on… Like, how to go forward with the exported packages, we would just, introduce a new createExporter function in each of the, exporter packages, and instead of going through the path where it merges everything together with, With the environment provider config, we just, Don't do that, and just take the config as is.
**Trent Mick** 16:21 Yep.
**Marc Pichler (Dynatrace)** 16:24 I think that's a reason that we're… middle ground.
We would market…
**Trent Mick** 16:30 Do you want that to be the interface that is kind of the experimental playground for what this final post 3.x thing would be?
So, biased towards using Fetch.
spec names for… Configuration options and things.
**Marc Pichler (Dynatrace)** 16:46 Yeah, or at least it shouldn't, depend on any… HTTP module.
Or… It shouldn't depend on the HTTP module itself, so that we expose the types.
to users that way.
**Trent Mick** 17:04 Yeah, gotcha.
**Marc Pichler (Dynatrace)** 17:06 So it's kind of agnostic to the user, what's being used in the background. You can change it later.
**Trent Mick** 17:13 Okay.
Okay, thanks.
**Marc Pichler (Dynatrace)** 17:17 True.
It's, yeah.
The whole exporter topic is… something that I would really like to see.
Done in the future at some point, but it's… It's not that much fun to work on them.
**Trent Mick** 17:36 No, it's big.
**Marc Pichler (Dynatrace)** 17:36 It's delicate.
**Trent Mick** 17:37 And that's got… Lots of scar tissue, so yeah.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 17:45 Yeah, I would work on it, but I'm busy that day, so…
**Trent Mick** 17:53 That day, you said?
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 17:54 Yeah, it's just a vague excuse that you're just like, oh, sorry, I can't, I'm busy that day.
**Trent Mick** 18:01 It's gonna take more than a day.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 18:07 Fair enough.
**Marc Pichler (Dynatrace)** 18:08 I actually wonder.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 18:09 I'm busy, I'm busy that year.
Better?
**Marc Pichler (Dynatrace)** 18:15 Yeah, I think he is… he is closer to what would actually, be the case here.
I'm actually wondering… Like, how did… So anything that we do would probably look similar to what we do for the browser here.
Which is just creating this, export delegate.
And that export delegate is actually already… In the same shape as a log record exporter, so we can just take that one directly and, return a log record exporter… return it as a log record exporter instead without running into any type issues.
There's one problem.
**Trent Mick** 19:16 delegate itself.
**Marc Pichler (Dynatrace)** 19:17 office.
**Trent Mick** 19:18 Not in that shape, is it?
**Marc Pichler (Dynatrace)** 19:20 The delegate itself is already, Like, it has all the diff… all the same functions as… or all the same methods as required by a log record export.
**Trent Mick** 19:30 Who we both see it first. Okay.
**Marc Pichler (Dynatrace)** 19:33 Yeah, so for that, it works. For metrics, it doesn't, because metrics still has some functionality in the HTTP metric exporter, Package.
that the others depend on, so that would have to be moved up into OTRP exporter base.
So that everybody can use it.
But for logs and traces, it should be fairly easy to do something Very similar to that.
I might also take some time to look into that, It's been a while since I last worked on this.
Right.
Any other topics?
I guess I would bring up that I, did open the SDK 3.0 release announcement, I just pinged that one.
So that people see it.
there's gonna be, so, what I wrote down here is that we… Start now with the… triage period for the changes that we, want to make in 3.0, so that means going through the backlog and deciding what needs to go in now, and what we can defer to later. Not… Sometimes, when thinking about an issue a bit longer, it turns out that it's actually not a braking change, or it can be done in a non-breaking way.
So, it takes some time at the end of this meeting to, Go through the issues there and discuss those, if that's fine with everybody.
Yep,
**Raphaël Thériault** 21:58 Nope.
**Trent Mick** 22:02 Another thing, I reviewed your… your context?
dot.
attach.
**Marc Pichler (Dynatrace)** 22:09 Oh, thanks.
**Trent Mick** 22:11 I think that looks good to me. I had a couple questions, like… It… Came out quite smooth, actually.
Which… which was nice with the, with using.
With the using keyword.
Yeah, I pointed out an example of a foot gun in there, which you get when you're changing the current context.
But… which is mentioned kind of deep in the node docs. I don't know if we want to surface that for people, but you already kind of have warnings that, like, you really shouldn't be using this thing unless you know what you're doing already.
It's good.
comments, let's… we've gone there. Sorry, go ahead.
**Marc Pichler (Dynatrace)** 22:56 I think it makes sense to add that warning. I will go and, add that to… the README and also the… Yes, Doc on it.
Because I think people will still start using it in the way that, I'm saying they shouldn't, but… Then it's good to have that card out somewhere.
**Trent Mick** 23:25 Yeah, and it should be, like, For people debugging other people's… hotel.js code, the first thing to look for is if they use this context.attached, then everything's… or context.
Is it attached? Sorry, I'm forgetting now.
Yeah, then all bets are off, like, that's the bug.
Anyway. So then I had another question, do you need to go back and update the… like, the utility that you'd had in the other draft PR to make sure that things are…
**Marc Pichler (Dynatrace)** 23:56 Yeah, I had a…
**Trent Mick** 23:58 him.
**Marc Pichler (Dynatrace)** 23:58 Yeah, I have a local branch that has that updated, so it does work, it… essentially does the same thing, just, this, I'm… I'm just using dispose instead of, detach, and then… everything starts working properly, so… That's actually the follow-up that I want to do, is I want to… move that utility to its own package, would be instrumentation Tracing Channel.
And… then… People can start using that instead, to… Write the instrumentations?
**Trent Mick** 24:43 Hmm, interesting. Okay. Yeah.
**Marc Pichler (Dynatrace)** 24:46 Yeah, so the reason why I want to have it in a different package is that I want to stabilize it soon, or, like, once we figure out that it works.
I would like to… Stabilize the interface and stabilize the package.
and not rely on the instrumentation package to be saber first.
**Trent Mick** 25:11 Cook.
**Marc Pichler (Dynatrace)** 25:13 So it would still provide the wrapper for… The stuff that comes out of this, Subscriber with, context management thing.
To make it the shape of an instrumentation, but, that function would be marked as experimental, even when we go stable with… with that utility package.
**Trent Mick** 25:46 Okay.
entirely follow that, but once there's code out, I'll see it. Yeah.
Yeah, having some path towards stable instrumentation, so it'd be… Of course, great.
Okay.
**Marc Pichler (Dynatrace)** 26:06 I'll have a look. Something that I, also just noticed right now… I will also change… This type here to not… come from OpenTelemetry API, because we still need to… allow people to use an older version of the API with a newer version of the context manager, and the type won't exist on older versions.
So it will fail to compile.
We ran into that in metrics in the past, and it was a bit frustrating, so…
**Trent Mick** 26:54 What's the answer?
**Marc Pichler (Dynatrace)** 26:57 The software has to copy the type to the consuming package.
And then once we bump the minimum required API version, we can drop the copy type and just use the one from API.
It's a bit clunky, but it works.
Alright… I have one more topic, maybe.
this PR here, the person that has been working on that, Yes.
opened that PR a few times.
in the past, I think, and we haven't… Really gone ahead and… done anything with it. What they're doing here is they're patching, Tesla versions so that The script can run in parallel.
I think there was a feature request on the tester versions package.
A while ago, but it hasn't moved forward.
**Trent Mick** 28:16 Did Thomas say no on that one?
**Marc Pichler (Dynatrace)** 28:19 I think it just went stale.
Let's see…
**Trent Mick** 28:44 There's an issue.
**Marc Pichler (Dynatrace)** 28:48 Maybe it was a pull request.
Oh, yeah.
Was no issue, probably.
So that is the change they propose here.
The actual code for Tesla versions is also not that, Not that huge. I wonder if instead of, Having this patch here, we could just…
**Trent Mick** 29:35 A full copy of this thing.
**Marc Pichler (Dynatrace)** 29:37 Yo.
We wouldn't need to publish it, it would just leave this, local build tooling.
I'm not too much of a fan of, like… Petching stuff this way, so… I think it would be better to copy it.
I guess the license is a pervasive one.
That's an MIT license, so… And we also don't need to bother the author with… The future that might… Only really help us a lot.
I can see that, for many other people, it wouldn't be that much of an issue, because, the… They don't have that many packages that they need to test against.
**Trent Mick** 30:54 Cool. I hadn't dug into this, Phil.
What kind of speed?
Up are we talking here?
**Marc Pichler (Dynatrace)** 31:05 Looks like this is actually not working right now, so… I'm not sure what… The issue is… seems to be timing out, probably.
**Trent Mick** 31:17 Oh, was there another one that got… There was an older pole that got closed, right?
A while ago.
**Marc Pichler (Dynatrace)** 31:24 Yeah, I think… That's the second one now that was,
**Trent Mick** 31:29 2994 was the previous one.
**Marc Pichler (Dynatrace)** 31:42 David had reviewed it.
I will, write a comment here to suggest to… Consider copying the code instead, and applying the patch.
directly here.
I just need to include the license.
While, probably the same way that we did in… the instrumentation package.
Or Shima, so…
**Trent Mick** 32:40 Right.
**Marc Pichler (Dynatrace)** 32:42 Yeah.
**Trent Mick** 32:46 Oh, this could be off in scripts, too, because it's not shipping, so… Yeah.
But same thing, yep.
**Marc Pichler (Dynatrace)** 32:55 Alright, then let's do it this way.
I don't think I have anything else to talk about, Circus.
There's no topics.
From any of you, then we can move on to bug triage.
And look at, SDK 3.0 milestone issues.
Like, no bugs in the quarry Ball, or no new ones, at least.
No new ones in the country repo. Let's check if there's… Anything that looks like a park report, but… Hasn't gone through the template.
I guess this is an internal one.
I have no way to test this.
We'd have to… find a Windows machine for it.
**Hector Hernandez** 34:13 I do have plenty of Windows machines, I can take a look at this one.
**Marc Pichler (Dynatrace)** 34:17 Thank you, Hector. Yeah, I would appreciate it, you having a look.
There's a way.
**Trent Mick** 34:28 scripts, boy, I'm not surprised. Yeah, I wouldn't be surprised if they're…
**Marc Pichler (Dynatrace)** 34:34 Yeah, there's probably a lot of,
**Trent Mick** 34:38 Can you use those slashes in there?
Okay, sorry, I have to go look at this.
This was Jen Semcoms.
Oh, no.
**Marc Pichler (Dynatrace)** 34:50 Yeah.
**Trent Mick** 35:05 Hmm.
**Marc Pichler (Dynatrace)** 35:06 Seems to be a fairly small change, though.
Alright, let's, I guess it's P4.
A feature request… And… That's it for… Contrip, let's check core as well.
Looks like there's nothing there as well, so we can move on to… I'm looking at SDK 3.2, though, Let's pick some… ECO1's first, dropping the exporter Jager package.
is, I think, something that we had already started, before 2.0 even. We deprecated the package itself.
Or at least the… the exporter that's… in the package, so… If there's no objections, then I would put that into… Milestone here, and apply the accepted labor.
**Trent Mick** 36:56 Yep.
**Marc Pichler (Dynatrace)** 37:05 Right.
Jaeger propagator is kind of similar, but, hasn't been… deprecated for that long yet. There's this, propagate-less distribution.
section in the spec, and there it says that Jager, propagator is deprecated, so I would also… Remove that one.
There's no objections.
**Trent Mick** 37:47 Yes, please.
**Marc Pichler (Dynatrace)** 37:58 Alright, then we have, dropping Instrumentation Restify.
**Trent Mick** 38:13 It's just not maintained anymore, as far as I can tell. I can't remember.
was actually… Any commits recently?
last month.
**Marc Pichler (Dynatrace)** 38:30 Yeah, seems like the last release was…
**Trent Mick** 38:35 2024, January.
Yeah.
And my memory is, unless they fix that in a later point release of 11, is that it doesn't work with Node 24.
**Marc Pichler (Dynatrace)** 38:53 Yeah, I would, be in favor of dropping that.
**Trent Mick** 38:58 Okay.
**Marc Pichler (Dynatrace)** 39:02 it's always difficult to figure out, like, how many people actually use it, because it's included in all the instrumentations node, I guess.
**Trent Mick** 39:10 Yep.
**Marc Pichler (Dynatrace)** 39:11 So, let's… Barcelona accepted.
Label on that one,
**Trent Mick** 39:25 I mean, if there's an outcry, then we can talk about reviving it, but we'd still keep it out of auto-instrumentation's node, I guess, or we could say you're welcome to take the code and…
**Marc Pichler (Dynatrace)** 39:37 Work it.
**Trent Mick** 39:38 separately.
**Marc Pichler (Dynatrace)** 39:40 We can remove it from all the instrumentations node, in 3.0, and then remove it later.
Koolers.
**Trent Mick** 39:49 You could, but I'm inclined to just go ahead and do this one. I can't remember last time there was a user.
Mention of it.
**Marc Pichler (Dynatrace)** 39:57 Hmm. Yeah, and also… we have Git, so if we want to bring it back… We can.
**Trent Mick** 40:05 kit.
**Marc Pichler (Dynatrace)** 40:08 Alright.
Dinh… Well, it's the PR, actually, so… Let's go to the issue for that.
Maybe.
Don't have one.
**Trent Mick** 40:34 What are you looking for?
**Marc Pichler (Dynatrace)** 40:35 the Open Census… shim remover.
**Trent Mick** 40:40 Oh, that was… yeah, it's there. Oh, it's draft.
Oh, because I'd created.
**Marc Pichler (Dynatrace)** 40:45 Yeah, it's okay.
**Trent Mick** 40:46 I created a PR to drop, but we decided we're waiting until 3.0, so I didn't want it to accidentally, so I've moved it to drop. So it's sitting there, it's… Yeah, okay.
**Marc Pichler (Dynatrace)** 40:57 Alright, I guess we can, just create an issue, for that, or just leave.
**Trent Mick** 41:03 Do you want an issue, or…
**Marc Pichler (Dynatrace)** 41:04 Yeah.
**Trent Mick** 41:05 I don't know if.
**Marc Pichler (Dynatrace)** 41:05 I don't… I don't necessarily need one, I think, It should be fine to just… Had the PR for it.
**Trent Mick** 41:20 I add the label to it.
**Marc Pichler (Dynatrace)** 41:23 Yeah, sure.
**Trent Mick** 41:28 Understood.
**Marc Pichler (Dynatrace)** 41:40 Alright, Then we have… Changing the… default export, are the default host to local host in the Promise exporter. Right now, it binds to all interfaces, and this is just… Making sure that somebody who is using it doesn't Accidentally expose it to… The network when they don't want to.
This is a specification… Change.
So I would be… I would say that we should include this one. The Prometheus Exporter is technically still experimental, so we could make that change out of band.
But including it with a braking change release would be… easiest to communicate, I guess.
Any objections to including it?
**Trent Mick** 42:57 No, definitely put it in.
**Marc Pichler (Dynatrace)** 42:59 Alright.
**Trent Mick** 43:08 Wasn't there… there was a… An issue that you created for a whole bunch of issues on… Was it Prometheus?
**Marc Pichler (Dynatrace)** 43:17 Yes.
**Trent Mick** 43:18 It had a whole Mmm.
**Marc Pichler (Dynatrace)** 43:19 I think…
**Trent Mick** 43:24 Where was that?
**Marc Pichler (Dynatrace)** 43:25 It's this one here.
That's what I saw you in.
**Trent Mick** 43:32 Motors on the wall.
**Marc Pichler (Dynatrace)** 43:33 Yeah, we can do it now, since we have context on it.
There's a bunch of changes that… We probably should make… We might have to… we might have to break it up, though, into smaller chunks, so that… we know which ones are actually breaking, or which ones can be done later, because I guess we'll be, We won't have that much time to… work on 3DL this time around.
Since the… Idea is to just work on it for a month, and then release.
I were… Keep the needs refinement.
label on here, and I will refine that down into smaller chunks so that We can include these in the milestone, and then I remove that one.
So that we only include the ones that are actually breaking.
I don't know, I think this person here had a comment.
**Trent Mick** 45:28 Did the dashboard thing get updated, since it looks like it.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 45:31 Oh, the…
**Trent Mick** 45:31 It was author, and now it's maintainers.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 45:34 Yeah, so there is a lot of updates on this, workflow going on.
**Marc Pichler (Dynatrace)** 45:44 But it seems to be correct now, so… I just let them know that, we'll merge this when we start working on 3.0, so… That they know what to expect for this PR here?
Great.
There's actually two issues for this one.
There's removing some of the export star from SDK node, and then there's removing all of them.
And should we close this one in favor of, like, removing oil and including that in the, Three Digital Milestone instead?
**Trent Mick** 46:56 Let me remember… What was the sum I was proposing?
**Marc Pichler (Dynatrace)** 47:01 Context-based node and tracing.
**Trent Mick** 47:09 Yeah, if 3 to those close, and we just… do it then.
Those ones, obviously, I had a stronger case for.
And then, I think for a little while, I've been proposing I can't remember if I did. I guess, anyway, yeah, you just think we should get away from doing this.
**Marc Pichler (Dynatrace)** 47:31 Yeah, the… I think the original reason for re-exporting them was that Since everything was experimental, people would just import from SDK node instead.
And they would get the minor version that was pinned in SDK node instead of the one that they would install themselves.
And then they would never run into type issues, because they would just always get the correct one, and if there was a breaking change, then they would just have to update their code.
**Trent Mick** 48:10 So that's still… that's still useful, right?
**Marc Pichler (Dynatrace)** 48:14 It would still be useful, yes, but we've… stabilized the… at least a… plugin interfaces.
Far enough that it isn't a common occurrence anymore.
So one of the issues that we've had was, for example, push.
Metric Exporter, would change.
And then you would suddenly have the wrong exporter in store. But now, since SDK Metrics is stable, and SDK Trace is stable, you don't run into any problems with these SDKs.
**Trent Mick** 48:54 Sweet!
**Marc Pichler (Dynatrace)** 48:55 Do the same with logs, and get that to a stable state, then… The issues are so… stop happening with that, and the only thing that's remaining is instrumentation, where we don't re-export the instrumentations from Contrip from this package, so it's less of an issue there.
**Trent Mick** 49:18 Okay, yeah, I gotcha. That sells it for me. Certainly, when they were 0.x, it was a pain in the butt to keep.
To update your depths.
And.
**Marc Pichler (Dynatrace)** 49:30 Yeah.
**Trent Mick** 49:30 stay compatible. So, okay, yeah, I gotcha.
Sold.
**Marc Pichler (Dynatrace)** 49:36 I'm not sure if that was, like… the main idea back then, to do it this way, because, like, also the decision was made Before my time on the project, but that's what I get out from conversations and such.
**Trent Mick** 49:51 You can also pitch it as a convenience, like, if people want to use those things in their bootstrapping setup, they only need to take one step instead of… Now they really should take… 4 plus.
Dependencies, so, but… maybe that's fine. We don't need to have that convenience for this package.
That's what the… But I hate the name, that's what auto instrumentation is noticed for, is for people that just want to have… One dependency and one entry point for getting in. Anyway, yeah.
**Marc Pichler (Dynatrace)** 50:28 I also guess the name was different for auto-instrumentations, not…
**Trent Mick** 50:32 I mean, we can change it sometime, maybe, but…
**Marc Pichler (Dynatrace)** 50:34 Yeah.
**Trent Mick** 50:35 Yeah, it's just as awful.
**Marc Pichler (Dynatrace)** 50:39 Alright, so should we go ahead and remove all of them, then?
There's also a possibility to just add them back if we need to.
if we're… Find a bunch of people that are… Wondering where that went, we can still add it back.
**Trent Mick** 50:57 So I hesitate a little bit, because there are lots of examples out there doing this, because of the convenience thing, right?
**Marc Pichler (Dynatrace)** 51:02 you're looking.
**Trent Mick** 51:03 the OpenTelemetry I.O. code, I think, was using examples of this, though it was using… The tracing re-export.
Or the Node one in some of those cases, I think. I have to go check. Maybe I… Gonna catch me in a lie here.
**Marc Pichler (Dynatrace)** 51:22 I think it was definitely there at some point. I think we since removed it, but… Might be that we missed a few.
**Trent Mick** 51:38 Oh, maybe it's the old translations, though.
Yeah, maybe not then.
some examples.
**Marc Pichler (Dynatrace)** 52:15 Oh, it actually just sends us to… own examples.
**Trent Mick** 52:20 Nope, can't find any there either.
**Marc Pichler (Dynatrace)** 52:27 present,
**Trent Mick** 52:31 There's one in OpenTelemetry.js contribut examples, but I mean, so is that my fault then?
Probably.
**Marc Pichler (Dynatrace)** 52:44 I guess we can…
**Trent Mick** 52:46 That's my fault, we can just update if that's… that's not a strong argument against this, though.
**Marc Pichler (Dynatrace)** 52:55 Yeah, it could still be that there's some examples out in the wild, though.
For what it's worth, I haven't seen, coding agents run into that, that they start importing, stuff from SDK node.
Which is surprising, because they sometimes apply weird patterns that are not that widely used.
Anymore?
You said you have.
**Trent Mick** 53:26 Have or have not seen.
**Marc Pichler (Dynatrace)** 53:27 I have not seen them do it. There's been… like, some efforts internally where people started using, Oter within the company, and they… Got started with it using, using agents.
And… the… Had some problems during setup, but it was never that they started importing importing these re-exports from SDK node. And the examples that I've seen people generate also never had that pattern, so… I feel somewhat confident in saying that, like, removing it probably wouldn't hurt people using agents that much.
**Trent Mick** 54:17 Okay.
Okay, so… You had the other issue for removing them all?
Oh, yeah, that's that old, old issue.
That we had.
So do we close the sum one, then?
in favor of… 5461.
**Marc Pichler (Dynatrace)** 54:47 Yes, I'd say so.
**Trent Mick** 54:49 Okay, I'll do that.
**Marc Pichler (Dynatrace)** 54:51 Thanks.
Gutierre… Accepted labor on this one, if nobody has any objections to it.
Right.
Maybe we can… Do one more for today.
I guess this one will… depend on… Where stuff gets moved to, in the process SIG.
Or in the browser repo.
**Trent Mick** 56:05 Yeah.
**Marc Pichler (Dynatrace)** 56:08 I probably need to refine that a bit, so… Make sure everything is… Set up for them to move it before we actually commit to removing it.
**Trent Mick** 56:24 A little bit above that, there's another one where David has a… issue for MoveUtils out of the package. That was SK TraceWeb, so… Kind of another issue for the same thing.
David's away this week, so maybe we can.
**Marc Pichler (Dynatrace)** 56:43 Bring it up.
**Trent Mick** 56:44 Again, next week.
**Marc Pichler (Dynatrace)** 56:46 Yep, that sounds good.
Let's just talk about it then.
Actually linked these together. The other one was… 58… We can easily navigate between the two.
Looks like that's also linked to… This issue here… Which is largely done now, I think.
Like, consolidating the three packages is… Done, we just need to remove the other two.
**Trent Mick** 57:47 The TraceWeb stuff is still up in the air, which is why I hadn't gone through and closed all these things.
**Marc Pichler (Dynatrace)** 57:55 Alright, that one has the accepted label on it already, but I will remove it so that we can talk about it again.
Next time. I guess, it would make sense to just… Split off smaller ones from this one, and then close… This one here, since it's already far enough along that we don't need all the context from that one to work through the stuff.
**Trent Mick** 58:19 Right. Yeah.
**Marc Pichler (Dynatrace)** 58:23 Alright, looks like we are out of time for today anyway, so… thank you everybody for joining.
Have a nice week, and see you next week.
**Trent Mick** 58:34 Thanks.
**Marylia Gutierrez (Raintank, Inc. – Grafana Labs)** 58:35 Thank you.
**Matt Wear** 58:35 Yep.
**Hector Hernandez** 58:36 Thank you.
**Marc Pichler (Dynatrace)** 58:37 Thank you, bye.
