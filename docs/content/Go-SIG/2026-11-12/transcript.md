SIG: Go SIG
Date: 2026-11-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Damien Mathieu (Elastic)** 00:17 Hey, folks!
**Robert Pająk (Splunk Inc.)** 00:21 Hello, hello, how are you?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 00:24 Huh?
**Damien Mathieu (Elastic)** 00:25 Happy not attending KubeCon.
**Robert Pająk (Splunk Inc.)** 00:32 It's pretty dark here. It will be not that dark in Salt Lake right now.
**Damien Mathieu (Elastic)** 00:37 Hari, what did you say?
**Robert Pająk (Splunk Inc.)** 00:39 I said that it's dark here, it wouldn't be that dark at Salt Lake City.
It would be a lot warmer as well, I guess.
Okay… I will add you, Bryan, to the… To the attendees list, adding myself.
Okay.
I'm not sure if anyone else will join.
So, I'll stop sharing my screen.
If you have anything that you want to discuss today, feel free to add items to the Agenta notes. Personally, I added just things to discuss for upcoming release.
I think these are the most important topics, but if there's anything else that you want to discuss, then please… Add topics here.
Alright, so maybe let's start?
And if anyone joins, then we'll just, we'll just expand the agenda. Damien, are you here? Or do you have to leave?
**Damien Mathieu (Elastic)** 02:09 No, no, I'm here.
**Robert Pająk (Splunk Inc.)** 02:12 Okay, so I created this, Soap.
I added the current milestones.
For… that are… contains issues or PRs that, in my opinion, are broken the release. The… the ones which I think are currently the most blocking one are the one related to the SEMConf upgrades. So, this is one. There's also a separate one, which is related, to a… to a bump.
Because right now, the new semantic conventions for duration, they recommend, like, one bucket.
for the dur… for the duration instrumentations, instruments. So, right now, so this is a backflix related to it.
It would be good if David also reviewed this PR later.
For… for the Go contribute.
**Damien Mathieu (Elastic)** 03:07 Sorry, I just want to stop on go.
I think it's important to note that there are multiple CVEs that need to ship with this And we need to synchronize this properly to ship everything when we do the workbooks.
**Robert Pająk (Splunk Inc.)** 03:26 Yep.
Correct.
So the purposes we do usually, we just, you know, ship the… we… we do the… we… we kind of merge these private, private fixes on the day of the release, just before.
But first, we need to have this one resolved.
So, and for GoConstrip, it's not GoConstrip… This is a GoCon sweep. We have also, bump usage.
And we have also a few leftovers.
I thought that, some of them I think we could also, this one has a related PR, which I can also add to the microphone, and I just reviewed it a second ago, and I added a comment, but… I'll give you the chance.
But I don't think it should be blocking. This is not a critical error, this is just that.
**Damien Mathieu (Elastic)** 04:26 Yeah, I don't see that as blocking.
**Robert Pająk (Splunk Inc.)** 04:30 So I… for now, I prefer keeping this, and And, I prefer keeping this.
But I think the only one which is currently blocking is this one. I saw also one issue, Damien, which looks important.
to me, I'll just try to find it quickly.
You can just remember how we use the gold.
No. YAML?
**Damien Mathieu (Elastic)** 04:58 you're in PRs.
**Robert Pająk (Splunk Inc.)** 05:01 Yes, I want to be in PRs, or maybe… because I have not… Was it this one? No.
This was for auto cons.
Of course, maybe I'll find it.
us through here.
I just do not remember where was the window when I was reviewing it, like, a half an hour ago, or something like that.
Yeah, this one.
So this one… I have not reviewed it, I just read the description, But the thing we should…
**Damien Mathieu (Elastic)** 05:36 Even remember viewing this one.
**Robert Pająk (Splunk Inc.)** 05:39 Ain't been there.
**Damien Mathieu (Elastic)** 05:41 There's been so much noise recently that, yeah, I don't remember… I don't even remember this one.
**Robert Pająk (Splunk Inc.)** 05:46 Yeah, so this one is about, about parsing the YAML, and if I remember cor… if I understand correctly, this PR is about fixing potential YAML, injection.
It's a very HPAC, but what I thought when I saw this is I would probably just to double-check how it's implemented in the collector.
Because I have a feeling that this, this environment substitution may… may be, I'm not sure if it is, I'm not sure if it's not adapted from the column metal collector implementation. So, because I know that you're Damien approver or maintainer, the collector.
**Damien Mathieu (Elastic)** 06:26 Yeah, approver, approver, but I have no idea.
Okay. The collector is a huge codebase.
**Robert Pająk (Splunk Inc.)** 06:34 I know.
you know.
Okay, but, if you, Damien, will have any opinions about.
**Damien Mathieu (Elastic)** 06:43 I can, look into it.
**Robert Pająk (Splunk Inc.)** 06:46 Yeah, not now, you know, tomorrow, or… because, yeah.
**Damien Mathieu (Elastic)** 06:50 Yes, it's not gonna be today.
**Robert Pająk (Splunk Inc.)** 06:53 Yes, it's already late.
I'll just add it to the notes, maybe, so it'll be easier.
**Damien Mathieu (Elastic)** 07:03 Yeah, I'm… I'm pinging myself up so.
**Robert Pająk (Splunk Inc.)** 07:06 Okay.
And I can handle it releasing next week, hopefully.
Opinions history.
**Damien Mathieu (Elastic)** 07:20 Just one thing, there is one PR that is not frightening, but, has a potential rather big impact. It's the unending I think it would be good, like, if this PR was split into two steps, I think it would be good to not ship the unending one until the next release, just to, like, split things.
**Robert Pająk (Splunk Inc.)** 07:49 Okay, so the on-ending, which you opened, I think, today, you opened?
**Damien Mathieu (Elastic)** 07:52 I moved out of draft today. I think it's better if we don't ship it before the next release.
**Robert Pająk (Splunk Inc.)** 08:01 Don't… okay. We don't ship it…
**Damien Mathieu (Elastic)** 08:03 Before the next sweetie's.
**Robert Pająk (Splunk Inc.)** 08:05 Okay, so…
**Puneet Singh** 08:07 Does that mean that it cannot be merged before the release can go? Yes.
**Damien Mathieu (Elastic)** 08:13 Exactly, yes.
**Robert Pająk (Splunk Inc.)** 08:15 I will just find it and maybe explicitly set the milestone.
**Damien Mathieu (Elastic)** 08:19 Yes, we can save attest, basically. It's just, like, out of, being safe.
**Robert Pająk (Splunk Inc.)** 08:25 This one, download it like that.
**Damien Mathieu (Elastic)** 08:27 it has, like, performance impact and everything, so yeah, I'd rather… Doing it slow.
**Robert Pająk (Splunk Inc.)** 08:35 I will do it like that.
**Damien Mathieu (Elastic)** 08:42 Just, yeah.
there will be time before the next one, but just, like, since you're requesting changes, just make sure that it's not because the PR is bad, but yeah.
**Robert Pająk (Splunk Inc.)** 08:58 Yeah, I can…
**Damien Mathieu (Elastic)** 09:10 I would say we want to give it some time to… for… for the original PR, maybe.
Yeah, your comment is fine, but it's not, for… in my opinion, it's not more review than just, like.
getting the first PR in the world, and then… then ensuring that the next one can ship.
**Robert Pająk (Splunk Inc.)** 09:44 Okay.
Do you want me to edit it, or is it good for now?
**Damien Mathieu (Elastic)** 09:48 No worries. Okay. If someone is asking around, I can give more information.
**Robert Pająk (Splunk Inc.)** 09:55 Okay.
Hello, Puneet. Okay, you had just a few. Is there anything you want to discuss?
We were discussing only release preparations.
Yeah,
**Puneet Singh** 10:08 I wanted to ask two questions, actually. So one is related to the activities when we do… when we are trying to make a module, V1 stable. So… I mean, when we are doing the audit, does it mean that by that time, the spec has to be very stable? Because… what… I have, like, in my understanding, the U2 audit, implementation audit, based on what the specification says. So, there should be no friction, or tension, or any sort of conflict in the spec language.
By the time we arrive at the audit. Is that the case?
**Robert Pająk (Splunk Inc.)** 10:53 Yes, indeed.
**Puneet Singh** 10:56 Okay, next question is about… it's a smaller.
**Robert Pająk (Splunk Inc.)** 11:02 Okay.
**Puneet Singh** 11:02 I'm sorry.
**Robert Pająk (Splunk Inc.)** 11:03 So, I guess, just… because I'm not sure if… so, just double checking. So, we… we check with the stable parts of the spec, this is a must-have.
We also try to address development, but depending, you know, of the For instance, if there's a component, which is development.
then we do not add it as part of, you know, of the… of the stabilized API, because this is something that we should maybe change.
But if there are some types of little development sections which just clarify.
some behavior which do not, you know, cause, I don't know, any backwards compatibility changes, then they can be also kind of reviewed, etc. But usually, we just review the stable parts of the specification.
**Puneet Singh** 11:51 Okay.
Yeah, I think that, that helps more, you know, the, the… Clarification on what's… Being considered stable versus what's being considered development, actually.
But yeah, I think I'll learn more as I follow up, so I'm just looking at different modules which are undergoing, you know.
moving towards V1, and… and the one, if… I need to work in future, what needs to be, like, how this needs to be scoped as a problem, that's what I was trying to look at.
**Damien Mathieu (Elastic)** 12:29 I'm…
**Robert Pająk (Splunk Inc.)** 12:29 Oh, you must… Are you mentioning local exporter, or something different?
**Puneet Singh** 12:35 No, I think, I haven't, like, focused on any specific module, but it's just, most recently, I think what Robert was working on related to modules in the log, SDK log, and and also, I think David has recently started working in Prometheus-related areas, so that is also… You know, just, just looking at an example that what goes on, and… yeah, just, just acknowledging… acknowledging that I might, need to work at some point in this kind of problem, so… so, yeah.
**Damien Mathieu (Elastic)** 13:14 I think one important thing is to remember that, marking V1 means that for the middle long term, we do not want to change anything, make breaking changes, like, not change anything, but make braking changes. We can definitely release a V2. Some SDKs have a V3 already. I think Go is particularly cautious regarding that.
But, what I mean is, to me, V1 means that we are really confident But we are happy with what we are shipping, and it's not going to change substantially. It may change in the future, but it's going to be a lot harder to make those changes.
So it's, it's basically a question of being, confident enough that… We do not want to change so many things at the same time in the near middle future.
Does that make sense?
**Puneet Singh** 14:15 Yep, yep.
Yeah, I think it's useful, and thanks for, you know, following up on the answer, actually.
Just, just a small… Question, actually, that has anything come up that kind of signals that we might… start to look towards V2. Not in soon, but some distant future, maybe, like, by mid or end of next year.
**Robert Pająk (Splunk Inc.)** 14:43 There are two modules which I wanted to make a video, and there was a pre, pre, like, approval for the OTLP export… trace exporters, because right now their design is, like, that when you're using the HTTP exporter, then you're also importing the… all the proto… your… yes, when you keep the HTTP exporter, you also have the dependencies of the gRPC, and a lot of… a lot of people were just complaining that we are importing those, these modules, and because of that, the binaries are, like, I don't know, a few megabytes or even bigger.
than without this gRPC, modules, so… dependencies, so that's the only one which I think.
may be V2.
Because it requires changing the, the structure in the APIs, because right now, there is something in the API which is tightly coupled to the… to some gRPC endpoints, if I remember correctly.
**Puneet Singh** 15:53 Yeah.
**Robert Pająk (Splunk Inc.)** 15:54 So that's the only one.
**Puneet Singh** 15:56 Sounds… I mean… Yeah, it would be interesting follow-up, actually, just to… see the… what V2 API will look like, but… but I think it's in… not… not anytime soon, so we'll see.
But yeah, thanks for… Providing your perspective on this.
**Robert Pająk (Splunk Inc.)** 16:17 So the idea is that the idea is that the trace exporter, the API for the trace exporters, OTMP trace exporters, will look similarly to the metric and lock exporters.
Because this has different… like, the AP… if you look at the exported API for all the OTLP exporters, the trays are different than matrix and logs.
**Puneet Singh** 16:44 Yeah, I think that part is definitely… I'm not much familiar with. I mean, I haven't looked at, like, long enough or multiple times that… Metrics API is the one that I'm most familiar with.
Because of the… the most work that has gone there.
All right. I'll follow it up, I think there are some useful… references that has come out of this answer, actually, mostly to look at the trace API and Exporters API.
Okay, I think, yeah, there's… another question is a small one, is regarding when we make the SEMCON release for the… the… when we create the Go package, for the respective SEMCON release.
I mean, the change log of a SEMCOM for release can be very long, but when we create a GOP package.
What… consider when… Preparing the migration notes, that what needs to be included versus what that can be, you know.
Like, there's a long tail of changes, but not everything needs to be part of the migration notes. But still, when we prepare the release, the Go package, what we consider including in the migration notes.
**Damien Mathieu (Elastic)** 18:10 I mean, if you… yeah, I guess it depends, kind of, the stability of the package, but if a SEM kind of migration has breaking changes, then it needs to go through a migration anyway. If it doesn't, it's a trivial change.
If we do need to do a migration, then it takes a couple releases.
We've done that for hotel HTTP, for example.
I'm not sure we would need to do that for any of our instrumentation at the moment. Do you have a specific one in mind?
**Puneet Singh** 18:47 I, I know, I'm, I'm… I don't have any ex… you know, like, anything specific, but it's just that I was looking at the… the Go SEMConf release of the recent PR that Robert has created, and I was looking at migration notes that how they are getting generated, so… the file that it gets created from seems like that is, like, manually written, so… Some thoughts must have gone in that what needs to be, perhaps, like.
trying to include that, that, from the perspective that how it will affect the downstream consumers, but it doesn't need to include everything that what new SEMCOF attributes got added, or… or… or… or so.
But more, like, important.
Behavioral changes, maybe.
I'm not sure.
**Robert Pająk (Splunk Inc.)** 19:51 Let's just try to find the PR which you're… which you are discussing, but I think both Damien and you have… I think you both reviews, if I remember correctly.
**Puneet Singh** 20:00 Yeah.
**Damien Mathieu (Elastic)** 20:03 I mean, San…
**Puneet Singh** 20:04 I was…
**Damien Mathieu (Elastic)** 20:04 Sameconf PR should have nothing manually generated.
**Robert Pająk (Splunk Inc.)** 20:09 There's the little pe… there's the little part, which is…
**Puneet Singh** 20:13 I think there is this md.inc file, yeah?
**Robert Pająk (Splunk Inc.)** 20:19 Mmm… yep.
Yeah, this one.
**Puneet Singh** 20:25 Yes.
**Robert Pająk (Splunk Inc.)** 20:29 Yeah, so this one is kind of manually, or semi-manually generated, because, you know, I use AI to help me out.
But, yeah, but because some part is… is here, is right, generated, is generated separately, and some of the things here is taken from this file. So, for instance, if I remember correctly, this kind of part, like, here.
It's not in the migration nodes. You can see that it's not here.
So, some parts which are, like, you know, these re… have been removed, these have been added, these are, like, generated separately, and this is just a template that this… this part, I do not remember. I think it was, kind of, this part is added from the file, I think this is the part, like, from here to here.
So, this one tries to be, like, more, you know, not fully auto-generated, but, you know, it's just based on the description. If something, you know, if there are some more behavioral changes, like you say, or, you know, something is more sophisticated, then, yeah.
Let me try to add it here in this Inc. included, include it.
**Puneet Singh** 21:40 Okay, so more like a general guideline, that's something which has, like, a broader impact, or, you know, should be just not… worthy, then… And it gets mentioned.
Quickly.
**Robert Pająk (Splunk Inc.)** 21:58 your connection is breaking, but in general, we try not to assess which is important or not. If something can be problematic for the end user, we just try to document it to make the migration path as easy as possible.
So, we cannot assume that, you know, that some people are using this, this. Whenever we have something, we just try to have the migration notes for everything, if it's, you know, if we just find out for this information based on the release notes from the semantic conversions.
**Puneet Singh** 22:35 Yeah, I think that makes sense.
Yeah, I think I'm on a very remote connection, so yeah, that's why my voice might break up once in a while.
Yeah, I think, I think that's it from my side.
**Robert Pająk (Splunk Inc.)** 22:55 Bryan? Damien, anything from you?
**Damien Mathieu (Elastic)** 22:57 I don't think I have anything else.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 23:01 No, I'm good.
**Robert Pająk (Splunk Inc.)** 23:04 Okay So it's nice to see you.
Have a nice day, and see you next time.
**Puneet Singh** 23:09 2…
