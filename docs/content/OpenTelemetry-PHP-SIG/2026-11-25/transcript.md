SIG: OpenTelemetry PHP SIG
Date: 2026-11-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Brett McBride** 02:19 Hey, team. Sorry I'm a bit late.
**Chris Lightfoot-Wild** 02:24 That's hilar.
**Michele Mancioppi** 02:24 Ghost.
**Brett McBride** 02:27 Hey, Chris. Hello, Michele?
**Michele Mancioppi** 02:30 Michaela.
**Brett McBride** 02:31 Michele
**Michele Mancioppi** 02:33 SIG.
**Brett McBride** 02:35 I… I recognize your name now.
**Michele Mancioppi** 02:38 Oh, nice.
**Brett McBride** 02:39 Okay.
Tobias, hello.
I'll try and drive this meeting. Just give me a minute.
**Paweł (Elastic)** 03:35 Hey, guys.
**Brett McBride** 03:37 Hey, Pawel, how are you?
**Paweł (Elastic)** 03:39 I'm good, thank you.
How are you?
**Brett McBride** 03:43 Good.
Are we happy to get started? Tobias, are you online yet, or are we waiting?
**Tobias Bachert** 03:52 Yeah, I'm here now.
**Brett McBride** 03:54 Hello.
**Tobias Bachert** 03:55 meeting, so No, I'm ready.
**Brett McBride** 03:57 macaron.
Thank you for coming, it's lovely to have you here.
Alright, let's get started.
Sure. Alright, well, let's fly through it. First of all, welcome to our, Michele, I don't remember you being at any SIGs, but I've also not been to many myself for…
**Michele Mancioppi** 04:32 Yeah.
**Brett McBride** 04:33 while.
**Michele Mancioppi** 04:35 This is the first time I attend the PHP one, because… I, Would like to enlist some help in getting the support of the injector for the PHP distro over the finish line.
**Brett McBride** 04:52 Excellent. And again, welcome to our… our new maintainer, Tobias, who's, been a contributor for Forever for OpenTelemetry PHP, and has taken up a maintainer position with us.
So, if we just fly through the agenda, everyone can see my screen that I'm sharing here.
Thumbs up!
So, speaking of the… distro of OpenTelemetry. I had a couple of pull requests in, to… generate a Docker image, just to simplify the setup. So, that actually got… something got tagged last night, and it all worked as expected.
So I think the short version of that is that, instead of using a package manager to install a RPM, or a DEB, or an APK, we can just, copy the distro out of a Docker image with a copy from… and I tested that out in my day job today, and it worked Worked really well.
**Michele Mancioppi** 06:05 Speaking of this, I, I am also one of the maintainers of the packaging SIG.
The, we are doing DEB and RPM packages for auto-instrumentations.
So, effectively, the, the Deb and RPM packages you're doing for the distro, they could be.
Merged upstream with the rest.
We're organizing packaging repositories where you can actually do APM install OpenTelemetry and DNF install OpenTelemetry, and it works. And we're gearing up for, shipping container images.
So, effectively, the delivery of the PHP distraught that you got working is something that we could move into the packaging SIG.
**Paweł (Elastic)** 06:52 Great. So, please correct me if I'm wrong. So, we have some package registry, so you can just add a registry to your system, and then it will be able to update it, right?
**Michele Mancioppi** 07:05 Yes, the, we are building the system packages with OBS.
from, from OpenSouza.
assigning them, doing all the… all the important ceremonies, and then we deploy them… well, we will soon deploy them, because we're still waiting for a couple of settings, on a Cloudflare R2 bucket.
And, we have put… we are putting, the, OpenTelemTry.io Netlify in front of it.
So, the URL that the users will actually put in their APT sources is gonna be packages.opentry.io slash something.
Which is gonna be, it's gonna look very official.
Additionally, at KubeCon, we learned that The CNCF is, setting up a, artifact registry.
Where, we want them to publish the images.
And the same, for example, what you did with the Docker image for the PHP distro, that is effectively upstream of what the OpenTelemetry operator does.
with injection. So, we actually want to publish equivalent Docker images for Java, for… the Apache mode instrumentation, everything else, in the same, CNCF, image registry.
We would love if somebody from this SIG would join us in the packaging one to… To get the stuff, done properly.
**Brett McBride** 08:48 Who's the… I suppose that's Powell or… or myself?
The most likely people.
I don't know a lot about packaging, though.
**Michele Mancioppi** 09:03 Don't worry, it's, it's more like the work that you did.
Deb and RPM is, is largely portable.
If anything, we… there is stuff that we can, we have problems we've already solved, like man pages and the like.
So… moving it over is not going to be difficult. We are in a… in a bit of a bootstrapping phase on a couple of things. The infrastructure is not 100% there yet, and we're waiting since a month.
We're actually ready with code and everything since way before KubeCon.
Now it's mostly external dependencies, because in 2026, creating a CNAM is difficult, apparently.
**Paweł (Elastic)** 09:48 You suck.
**Brett McBride** 09:49 Yeah, so you, you mentioned the, the operator, so is this, is this the, Because we've got… we've got two different… two different ways. I think Pawel's trying to explain this to me.
Last week, where, we can install OpenTelemetry into a running Kubernetes application via the operator, but… Separately from that.
we can install it into a non-Kubernetes OS?
**Michele Mancioppi** 10:22 Yes. On, well, we're talking mostly Linux here.
The, there are… Pavel is absolutely right. There are two ways of, of triggering the injection of PHP. They both go over the PHP dot, PHP underscore, ini scannier, or Skandirini, environment variable.
The, the way that I would like to integrate the injector is the one with the additional extension, the additional SO file.
that then loads with a DL open, the OpenTelemetry.so.
for PHP. That is, It's… the discussion of how the injector is going to work is going to be a bit technical, but ultimately, what the injector needs as a contract with an automatic instrumentation distro is an agreement on which steps to perform to activate the distro.
with your, extension, especially the moment that you start supporting ZTS as well?
It is as easy for us as to make sure that the files are there, which is what, for example, the OpenTelemetry operator does by adding the instrumentation image and the volume mounts and the pod.
what the packages do by copying the files of the distro to slash opt slash OpenTelemetry, whatever.
And then what the injector does, its job, is to ensure that the process that we want to inject is the correct one. So, for example.
Check the PHP version.
And then, modify the process environment to add the PHP scanDir folder.
And then the PHP distro would take over.
**Paweł (Elastic)** 12:14 So, there is also other solutions to inject the process. I'm not sure if Convid has to be enabled during the compilation of the PHP, I'm not sure if it works on every PHP.
version.
But there's also option to patch the fopen function.
**Michele Mancioppi** 12:34 Yeah, that I would not do. It's, it's fraught with issues. You need to go, and it gets very complicated when you are in containers, and you do not know which version, which flavor of libc you're running.
**Paweł (Elastic)** 12:50 Hmm.
**Michele Mancioppi** 12:50 Instead, the, effectively, the… the injector can figure out at runtime, and already knows how to figure out which flavor of Lib C, so GNU lip C or Massel C, and then could load a different… Loader extension.
Because those need to be compiled.
**Paweł (Elastic)** 13:12 Yes, exactly.
**Michele Mancioppi** 13:12 I guess the food.
**Paweł (Elastic)** 13:13 But I'm trying to say that there's other ways, if you encounter any issues with the not working environment variable.
then you can use the patching of the fopen function, because PHP is opening the PHP i9 file, right?
So you can patch it and create the file on the site in the temp folder, and add the extension line there, and let PHP open this file from.
**Michele Mancioppi** 13:44 Yeah, I hear what you're saying. I advise against patching if open.
It's, it is… The more you patch of libc, the more bugs are going to find.
**Paweł (Elastic)** 13:55 Of course.
**Michele Mancioppi** 13:56 Moreover, the patching of FOPEN injector should do when it first loads, and that should pass F-Open on every process.
And I don't think we should be doing that.
The, the extension in between, I think is the best way, but ultimately, I mean, the contract, in air quotes, is… I mean, the injector implements what the PHP SIG tells it to in order to support automatic instrumentation.
**Paweł (Elastic)** 14:27 Hmm.
**Michele Mancioppi** 14:29 I've done a lot of work in preparation of this together with Jerry from SolarWinds.
And, I would like to sit to somebody and sort out the details.
Is that going to be you, Pawel?
**Paweł (Elastic)** 14:45 Yes.
**Michele Mancioppi** 14:46 Nice.
then, I will, we'll talk in DMs.
To figure out when to catch up and make a proposal.
Thank you.
**Paweł (Elastic)** 14:58 Thank you, too.
It's… thank you for doing that, so it's really too great to have it working for the PHP.
**Michele Mancioppi** 15:06 We, I think both the PHP SIG and the ejector SIG, we share a passion for stuff that just works, and it's easy for users to install, so… It's natural to work together like this.
**Brett McBride** 15:28 We're happy to move on.
So the only… well, the other notable one from me is, so I've been working away for a couple of weeks on, just… getting… automating our releases, at least in Core and Contrib, initially, as much as possible.
Just to make it… make it easier for, sort of, the limited number of maintainers that we have.
So, I think the final piece was merged.
sort of yesterday. So… I… the next time we need to sort of release something in core, I hope to be able to sort of do it all.
from… From GitHub, and not… not require us to… Sorry, not require a second… a second person, because the problem that we run into is… you need… you can't commit your own code, so you need someone else to… to review it.
So… So I'm hoping that the next, next batch of releases for Core, I can sort of, attempt to do solo.
Because I can.
can, approve bot PRs.
That's it, firm.
For me, well, every… the other bits can wait to the end if we've got time.
Chris, you've got the next agenda item. Did you want to talk about that?
**Chris Lightfoot-Wild** 17:03 Yeah, I linked it there, because I was going to bring it up here, but then it looks like, it beat me to merging it in first.
Some more… the contribution to come along and… added 1.45, dependencies for the SimConf packaging.
And Pawl, you'd initially said, a comment about bumping all the version on the telemetry that was being emitted.
Maybe I'm, against the grain here, so I guess looking for clarity, but… Felt like we shouldn't do that until we know… We are, like, compliant with the spec at that version.
But the… the package version can bump, because that's got… Like, the constants in it to be able to use newer versions, etc, and the way we use the constants in general.
So the names have changed, but, like, the underlying… Value is perhaps the same.
In places?
**Brett McBride** 18:02 Right.
**Chris Lightfoot-Wild** 18:04 Cool. Toy.
**Brett McBride** 18:05 Yeah, so, so, is the concern that… Because the attributes themselves must be there, because we've upgraded to the latest SimCon, and it's… it's not failing.
But… is it that the… The values of the attributes may… have changed.
**Chris Lightfoot-Wild** 18:26 It was as I understood it, like, if you're saying, I'm emitting telemetry at this, Agreed upon version.
You at least match the spec for that version that you're omitting.
Versus we jump from, like, 1.24 to 1.45.
And there might have been other changes in there that were not included.
But we're saying we're compliant with 145 now.
I'm not saying… maybe that was just fine, but… I remember at least one instance where, I think with the messaging attributes, like, the order flipped between the value and the… The two values in one of the… Things had flipped around.
Can't remember the exact, thing, but it's kind of per flew in my head.
So…
**Brett McBride** 19:12 Yep.
**Chris Lightfoot-Wild** 19:13 I don't know if there's a process, then, for us to… more regularly be able to update these, and maybe Weaver's able to be used in some way. I'm not that familiar with it, but to highlight where we're lacking agreement.
**Michele Mancioppi** 19:28 Are you familiar with, Trask's and Lyudmilos?
Conformance repository for semantic conventions.
**Chris Lightfoot-Wild** 19:37 I'd seen it roughly linked very recently.
**Michele Mancioppi** 19:41 It is absolutely worth… To invest in, Checking the conformance of our instrumentations and reporting the results over there.
Like, 100%.
And, something else that, it's not, if I recall correctly, in the conformance repo yet.
But it makes a difference between a good experience for end users and not, are the conformance of the resource detectors.
That tends to be one of the aspects of quality of metadata in OpenTelemetry that is the most undervalued by end users and maintainers alike.
So having both, analyzed for, conformance systematic conventions and reporting the results.
I, I promise it's worth your time.
**Brett McBride** 20:37 That sounds like something we should look into. Do you… do you know, Michele whether people tend to integrate it into CI and their GitHub Action Pipelines, or…
**Michele Mancioppi** 20:49 The one that can check quickly, I… the word… the word talks about that. I think the PHP SIG is one of the more further ahead there, so let me… At least recalling from memory, let me check very quickly what they do there.
And if I don't find an answer… I mean, continue the discussion, if I don't find an answer in the next few minutes, then I'll give you one in Slack.
**Brett McBride** 21:17 Thank you.
So it sounds like, Chris, at the very least, like, that that's worth investigating, but also, we should probably do a scan or a check over… contribute.
**Chris Lightfoot-Wild** 21:31 I mean, is my understanding off? Did it make sense what I was saying, or… I might have misunderstood from what I'd read previously in the spec, but, I don't know if there's a… By looking it up here, we might have had different interpretations?
So what?
If it's a 2 to 1, I'm in the wrong one, that's fine.
**Brett McBride** 21:51 I mean, I mean, we could be wrong either way as well.
I think… I think it's more correct to bump the… the SEMCOM version that we're reporting as.
**Chris Lightfoot-Wild** 22:08 Do you have to…
**Brett McBride** 22:09 Because we're sort of mixed mode at the moment, I think, is… is… what… what you're…
**Paweł (Elastic)** 22:14 But on the other hand, you know, we should report the lowest number we are compatible with, right?
So… I think that there are different… Different approaches here.
because if we just bump the… we are… let's say we are meeting the 1.23, right? It was 1.23, and now we are meeting 1.45, but none of the… of the strings changed, I mean, none of the constants, right?
the keys, so… On the other… on the other hand, so we are… Compatible with the lower version.
And I think that the problem here is that in some packages, and the real problem is that we can report lower version than we are actually reporting, so we are using the newer version of the SEMCOM, But reporting the older version, and it should be scant. As Brett, you said.
Without any scanner, we are… we will just lose… lost there.
Because there will be a lot of bugs on the backends, of the vendor backends, with the conversion, and adapting all of, you know, matching all of those versions, and all of those messes.
But… bumping?
Let's say it's more… we are more on the safe side, right, with the bumping of the version, and…
**Brett McBride** 23:46 I think we are, particularly given these ones where we have… we have started using new New attributes that do not exist in 1.24.
Yeah, we… at least by… by bumping it, we… We are confident that all of the attributes that we're using do exist in that version of.
**Chris Lightfoot-Wild** 24:12 Are you talking about bumping the package, though, there, specifically, or the telemetry that's emitted from it, from the instrumentation?
**Brett McBride** 24:20 The telemetry version that's emitted.
**Michele Mancioppi** 24:24 Do you mean the schema URL?
**Paweł (Elastic)** 24:27 Yes.
**Brett McBride** 24:27 scan a URL, yeah.
**Michele Mancioppi** 24:28 The schema URL is, problematic. There is some chatter.
in the, maintainer circles, especially with, the development of, Josh.
from the GC.
to kind of nuke it. So, might be worth for, for, some of you to go to the, Symante Convention SIG on Mondays.
And, and ask, your questions there.
I don't have the answer from the top of my head, despite… attending most of those meetings. This particular detail of whether it's the ceiling or the floor.
I don't know, Pawel's… sounds more plausible, having the floor. Ideally, it would be more consistent.
And speaking of deformance, I have found an example where In the semantic conformance repo.
Trask was actually reporting on the compliance of the HTTP PHP instrumentations.
And, it seems to me, that the workflow is still kind of manual, the bridging of the PHP contrib and the performance repo is done ad hoc at the moment.
**Brett McBride** 25:49 That sounds like something we could automate. If, if half of what we're after is already there, that's… that's well worth…
**Michele Mancioppi** 25:55 Yeah, I think so.
**Brett McBride** 26:04 What'd you say? Manually breached, manually something…
**Michele Mancioppi** 26:08 Yeah, kind of a dock. Like, you… if there is a change in the instrumentations, you go and open a PR to… to… to change the records about the instrumentations and the conformance.
**Brett McBride** 26:22 Okay, I think I understand. I have enough to go on with.
Possibly also related to, to that, PR, Chris was, that I do have a fix waiting.
Can't remember if it was linked from here or not.
Let's in colder, so… So… Weaver, so… semconf do not remove attributes, not ever now, and they are marked as deprecated, so, there's a full request, which I don't think had been reviewed yet.
**Chris Lightfoot-Wild** 27:09 Well, it brings back the ones we dropped.
**Brett McBride** 27:11 It brings back all the deprecated ones, yes.
**Chris Lightfoot-Wild** 27:14 Nice.
**Brett McBride** 27:15 Yes. So, changes the script, yeah, so the deprecated stays.
Forever? Always?
And I think it also adds a check that we don't ever drop anything.
Which we would have to… Yeah, the build should fail if we drop, if we drop an attribute that previously existed.
So if someone could have a look at that, that would… that would also fix that… that pull request, and possibly some other things, that are referencing deprecated.
attributes.
There's possibly some of those that are in… No. No, I was going to say they remain, but haven't been tagged, but the problem goes the other way.
Yep, so that's… that's… that's a fix, which should… Keep working. And, and… Stop those types of issues.
over again.
**Chris Lightfoot-Wild** 28:15 Cool, yeah, I'll have a look at that. I wasn't trying to be difficult, sorry, I hope I didn't come across that way, because there's another PR where someone… Someone claimed that… Like, existing instrumentation was broken, because it was on a… emitting a specific version, and like… whatever backend now wants this new attribute, and I guess my opinion on that was that it wasn't broken when it was written.
it might have changed in SimConf, but we're not omitting that version, and just bumping it might bring other side effects that… We've not checked, and we don't have, like, some kind of cadence to… regular check these at the moment. And it's obviously a time commitment from any of us to just… every time there's a new version released, just make sure everything is compliant.
So I guess any automation would really help with that.
**Brett McBride** 29:03 Automation's great. I think the question is, What? What should we check?
We can automate it if we understand.
what it is that we're looking for. And in the example you gave.
Was that specific to A backend? Because we do sometimes have issues with… Sort of third party, not OpenTelemetry.
processing of, of semantic conventions and, or just the, the OTEL, sort of, protocol.
Because they're not… Quite compliant.
**Chris Lightfoot-Wild** 29:40 I don't remember if it was… it might have been a messaging SIG thing, but then, looking in their Slack channel, they seem to be… Largely… defunct?
Or prior to shifted elsewhere, so… Couldn't actually get an answer out of.
That SIG.
But just… it's fine. It's just… Yeah, that was… it wasn't super obvious, just reading it.
To me, at least.
**Brett McBride** 30:07 I'm sorry.
We should say… One troop… Good automation. Does that cover it as a high-level.
**Chris Lightfoot-Wild** 30:24 Yeah.
I guess it seems like one of this sort of similar cat and mouse things, to where we're bumping package versions across the place, and then someone says the new version broke, because we didn't constrain the upper bounds on it, and… It's just… An extra way of being painful.
**Brett McBride** 30:42 Yep.
Yep.
**Chris Lightfoot-Wild** 30:46 But I like those changes you put in that other PR, to keep them around.
**Brett McBride** 30:52 Yeah, I think that that's the biggest one. That's the one that continually Gets us.
Or has on multiple occasions. So, I think that… That's resolved, but…
**Chris Lightfoot-Wild** 31:04 One of the other things… the thing I said last week about this, and now Tobias is here, my, Have some kind of thought on it as well, perhaps.
From your hotel packages that I've seen, Tobias, you're not actually using the constants, you're just, like, hard-coding the strings in? Yeah.
**Tobias Bachert** 31:24 Yeah, to avoid this exact dependency, when some conflicts bumped in, we lose some So, yeah.
And, I also remember checking, limited attributes using Weaver, so it definitely works, but it was a one-time action, nothing automated in the pipeline.
But, there are the tools.
To check it.
**Chris Lightfoot-Wild** 31:50 Okay. So it's obviously… it's useful when the constant's there, and when you're first developing it, but obviously, if there's any risk that it moves, or is removed, or whatever.
But just using a hard-coated string is the safest way, but…
**Tobias Bachert** 32:02 And when I bumped the, scheme, well, I, yeah, change the strings, or add two boots.
It's… no.
It's more typing effort, but… Yeah, it needs to be validated once, but then it stays fixed and safe.
**Chris Lightfoot-Wild** 32:23 I guess by that, Brett, you look like you were maybe sort of on the opposite side of that. Obviously, it seems a bit cold-smelly, perhaps, to move away from a constant, is that what you're…
**Brett McBride** 32:35 Yeah, I suppose.
Yeah, I'm just turning it over in my mind, though, I don't… I don't have a straw.
opinion either way. I… I'd probably… lean towards Constance. Breaking them.
**Chris Lightfoot-Wild** 32:55 Yeah, I suppose it's less constant if it's… We move it.
**Brett McBride** 33:02 That's true. That's true. And we've talked about other solutions as well in the past, like, should… So Simcov keep growing where we have, actually, you know, directories for every version, and the bundle just adds a new version as it goes, so that So that people can… Reference, you know, specific versions, and… and they will stay.
Stay as they were.
**Chris Lightfoot-Wild** 33:36 I guess I'd feel… it's not strongly opinionated… Sorry, go on.
**Tobias Bachert** 33:40 No, you're first.
**Chris Lightfoot-Wild** 33:44 Cool.
**Tobias Bachert** 33:46 We could also publish a package pair version, but this would lead to many packages, but would resolve this entirely.
I'm not sure if he, can do the same.
And it will lead to quite a lot of classes installed into a vendor that are… Not necessarily used.
So, yeah.
**Brett McBride** 34:12 I feel like… Fixing it.
Understanding the problem and fixing the problem.
Properly is… is the… the best.
The best route, and the… hopefully the least work, and the least maintenance.
Yeah, yeah, I think it's something we just need to… I need to understand, like, what are all of the things that go wrong?
what should… what should we do? Is that… is that written down in… the same con for, sort of spec, or in the OpenTelemetry spec.
Is it well defined?
What does Java do as a… As a fallback.
Lacking anything more official.
**Chris Lightfoot-Wild** 35:10 So you can mull it over, but perhaps,
**Brett McBride** 35:14 Yeah.
**Chris Lightfoot-Wild** 35:14 Do you want any issues? Like, should we raise an issue or something to discuss it further? I'll come back with our thoughts.
**Brett McBride** 35:20 it's probably… it wouldn't be a bad idea to raise, like, a meta-issue for it, Chris, if you've… if you can… locate.
These are the sorts of things that we've broken in the past.
through SimConf.
I just, just… Sort of collate them.
We'll just go through.
**Chris Lightfoot-Wild** 35:40 Horrible.
**Brett McBride** 35:41 tag them with something so that we can find them, it doesn't… I don't… I don't mind how, but, yeah, what are all the complaints people have had? What have we… what have we broken?
And… What should we have done, or what should we do in the future to… To avoid that.
**Chris Lightfoot-Wild** 36:03 Cool, thank you.
I did have one other thing, and again, sorry, it was because… I've put it in the past about spam suppression, and… Tobias, this might be one that I've seen you comment on other people's PRs previously.
But it seemed quite… we've had some other issues pop up with, like, Laravel instrumentation in the past, where people are saying there's, like, long-running jobs and, like.
Memory issues with the child spans of the, sort of, parent trace being left around, hanging about.
so, and I might be butchering the explanation here, but… kind of… what I hoped for was to, like, encapsulate a unit of work that Livo was doing, so either a request or a job being processed.
And it would start… I guess, turn on span suppression at that point. Sorry.
drops my inspiration so that everything is captured and emitted, and then everything that happens outside of that start and stop point Just gets dropped, or not emitted, or… Because… Like, with, with Laravel, there's a process where it's checking if it can pick up the next job, From a queue.
and it actually hits Redis in case it's… some other code has triggered it, to start shutting down, so it checks if it can still be running.
and someone at some point added a Redis hook, so that actually… Like, emits a spam.
That is not part of that trace parent.
And I don't want to do that. I don't… sorry, I've probably not fully understood it, and it's a poor explanation, but… Ideally, I wanted to start and stop point where I could say, right, from now, I'm interested… I want to, like, own being able to… Emit any spam.
At this point, and then turn it off again.
And is there a mechanism to do that? Am I thinking span expression is the… thing for that, or I've got it totally wrong.
**Tobias Bachert** 38:15 But, it is about Charles Penston only, or… Or new traces entirely.
Everything in one dress.
Because I'm thinking that this should be… I think this would be a case for the, for a sampler.
for a rule-based center, I would say.
Unless I missed something, no?
**Brett McBride** 38:39 Mmm.
**Tobias Bachert** 38:41 For group base sampler, you should be able to, select… Pretty precisely which span should be sampled.
If you care about entire traces and some traces, not at all.
**Chris Lightfoot-Wild** 38:56 Who controls that, then? Sorry, would it be the instrumentation?
Itself, or someone just configuring.
**Tobias Bachert** 39:03 the configuration.
**Chris Lightfoot-Wild** 39:05 Right.
Okay.
**Brett McBride** 39:07 So we'd have to document it. But so the problem, if I understood it correctly, is… A process is running that's polling for, is there work to do?
And a side effect of auto-instrumentation is that creates a whole lot of orphaned or single Or very small, frequent, Spans that you're not interested in.
**Chris Lightfoot-Wild** 39:30 Yeah, because I suppose.
**Brett McBride** 39:31 Occasionally.
Sorry, occasionally, that's also the origin of a unit of work, which you are, or they're always separate, but the unit of work you did want to trace.
A self-contained correct trace.
**Chris Lightfoot-Wild** 39:47 I think that one, like, there's the unit of work is trying to establish its own trace.
But some other operation… Was hooked first, and decided they didn't have a parent Trace already, so it starts one.
And everything else that happens… Around that is attributed to that, but it never ends, because it's a long-running process, and they keep building up and building up.
But then when the unit of work is captured and emitted, I don't care about the other bits outside of that.
Maybe I should try and find an example to… Highlight, but there's been a few people asking about this and trying to… change it, I don't know… How… don't know the direction it should be going in.
But if it's just a configuration thing, then…
**Brett McBride** 40:37 I feel like a reproduction would be… would be good, if you could spin up a… a baby application that… that does… does that.
Then… yeah, then I think we could look at it and… Like, work out which of the tools that we have.
can do that, and actually just see what What spans are coming out, and which traces are coming out, and… which ones we do and don't want. And I'm probably also interested in is the traces that you don't want. So you said Redis, so let's just say they're all Redis.
is Redis, as well as being these single Spans that just keep happening every… Pulse. Is that also then the parent of the thing that you really did want to trace, so that it's mis-parented?
What… what should have been a… an… you know.
The starting point of the unit of work should have been the start of the trace, but it was actually a child of… the pulse, or the check, the Redis check, that… Discovered that there was a unit of work to do.
**Chris Lightfoot-Wild** 41:50 I'll see if I can try and put something together to… Demo, I suppose.
**Brett McBride** 41:55 Mmm, I think that.
**Chris Lightfoot-Wild** 41:56 I'll reproduce it.
**Brett McBride** 41:57 Yeah.
**Chris Lightfoot-Wild** 42:02 Thank you.
**Brett McBride** 42:03 Let's zero.
Tobias, now that you're here as a maintainer, just, I've just been thinking about how to, sort of, organize work, so I've been… For a few months, sort of.
working on core, sort of in isolation, so I've got, like, extensive plans that I've written for myself on, you know, the sequence of things and how to break them up.
And I'm wondering whether we need to sort of share those, or document them, or spin them up into issues, I am starting to see, you know.
If we create issues for things with the help wanted, we are actually occasionally getting Contributors coming in, and… and… you know, try to fix those problems or address those issues for us.
Yeah, but I think… I think I need to tackle, like, the visibility of… what I… what I've got as the roadmap anyway, and you've probably got some ideas yourself.
Bour.
the roadmap for OpenTelemetry.
**Tobias Bachert** 43:19 Listen, never.
We should definitely share what we have right now.
Just to get an overview, and yeah.
I don't think we should put everything into issues at once, because…
**Brett McBride** 43:37 No, it's too much, no.
**Tobias Bachert** 43:39 Yeah.
**Brett McBride** 43:41 But maybe, I don't know.
**Tobias Bachert** 43:41 iPads.
**Brett McBride** 43:42 epics and sprints, to use the terminology. So what I do have, I was actually working on it today. Most of my plans are AI-generated, but they are extensive and self-linking, and they're all in Markdown.
And I just reorganized them a bit today so that they are backed up to… my personal GitHub.
that's a… that's a place for now. You can read them and look at them, and there's nothing… There's nothing sensitive in there.
So I'm happy to, sort of, open that up to individuals. Also, they're marked down, so we do have a wiki in the OpenTelemetry PHP repo. I can throw them all in there. They're a bit more public, they might get some… some visibility. Yeah, so I'm happy to do that. It's just… it's not… it's not a one-shot thing, but I do… I do actively sort of maintain them, you know, they… also, as well as planning the work, I'm keeping track of what's done, and… Which commit that was in, and which pull request that was in, and So, I do tend to update them. Well, no, I'm frequently updating them as they go, but I do want I do want to have some visa… give some visibility.
To them, for… a high-level review and, you know, is this a good direction to go? But also, it would be great if you know, Once we decide on Let's tackle this bit of work.
If we can, spit it out into… Sort of units of work, and distribute them amongst developers, then that would be… That would be fabulous, because I would like… more.
more contributors.
If possible.
**Chris Lightfoot-Wild** 45:35 That'd be really cool as well, because quite a lot of contributors just seem to spawn issues.
Of their own making, which is fine, obviously, but then, unexpected.
And then you need to review it when you don't have any context.
Versus having a roadmap with, like, this is what we're heading toward, and this doesn't quite fit our… Can come later, but… but we're doing these other things as a priority.
**Brett McBride** 46:00 Well, how about as step one, I'll just open up what I've got in my personal GitHub now. You can just go and have a look and tell me what you think, whether it makes sense.
And then we can… we sort of assess from there.
What to do with this information? What to do, what to do next, because it's… yeah, I think I've personally got too many Not trying to do too many things at once.
And… Having a plan helps me to not get lost while I'm doing that, but… I think I probably need to… I or we need to focus on just, like.
chunks of deliverables, so… and I mean, at a high level, it's declarative config, I want it to get done and stable, and then it's sort of get version 1.x.
Ultimately, it's to get SDK 2 out, but… but a whole lot of that isn't breaking, so it can come forward to SDK 1, you know, our current mainline.
Yeah.
I don't know, there's probably 6 or 8 different… high level.
Streams of work of differing sizes, and they do need to be… some of them need to be sequenced, and some don't.
**Chris Lightfoot-Wild** 47:24 Is the SDK2 goal still, like, all in on SPI for…
**Brett McBride** 47:28 Yes.
**Chris Lightfoot-Wild** 47:28 able to, you know…
**Brett McBride** 47:30 Yes, yeah, yeah, it solves… it solves lots of problems.
that we have.
**Chris Lightfoot-Wild** 47:35 I like it, I really like it. Yeah.
**Brett McBride** 47:37 Yeah.
yeah, I just… I really thought I'd have it done a lot sooner than now. I just keep inventing new and different work to do before I do that.
Sure. Yeah.
Yes.
Yeah, I'm getting distracted.
**Chris Lightfoot-Wild** 47:53 I feel like once… once we get to that stage where all the existing instrumentation is using SPI, I don't know how far away that is, but you can start having dependencies between each other.
Because at the moment, obviously, the ordering of Putin is… Outside of our control.
Yay.
**Brett McBride** 48:09 Yeah, and look, I think… I think I'd have to go back and look at my plans. I think I decided that we… that doesn't have to wait on SDK2 either. We could use SPI now. So if we… if we just decide… That's a priority.
Let's make it a priority, and…
**Chris Lightfoot-Wild** 48:30 Well, I changed my mind on what you said the other week with what Severin had raised about the CNCF, Claude Mac subscription for a 6-month period. I thought I might as well jump on it and understand it more and play around with it for 6 months for free.
at least I can, you know, not commit to it after that, whereas… That we could probably, in that amount of time.
Automate quite a lot of things, and move it forward quite a bit.
I know you've already… you're doing that massively, but I'm… I'm not. Yeah. Obviously, I'm moving at a snail's pace in comparison.
**Brett McBride** 49:07 Yeah.
Yeah.
**Chris Lightfoot-Wild** 49:11 I've not heard back on… from Severin, I don't know if you have, but I don't know if it's worth us chasing up on that, just in case.
We miss out on the 3,000.
Participants in that program.
**Brett McBride** 49:22 Yeah, it probably is worth chasing up, it's been a week, at least just to say, did you submit that?
For us yet.
Yeah, Poland, Tobias, OCMU saw that that was available.
And… Have an alternative, or are not interested, which is… which is fine.
Alright, well, let me put down as a, action item on myself, love share,
**Paweł (Elastic)** 50:07 you can also organize this document with the bullets, then you can easily convert the bullets into any issues. So if you will put this in one issue, in OpenTelemetry PHP repository, then you can easily just convert the bullets into the issues.
Yeah, and I didn't…
**Brett McBride** 50:25 think of that. And look, yeah, absolutely, happy to take any advice on how to reorganise it, but I did consider that. Can I just say?
Yeah, because I've… I have been.
Letting it make a couple of, sort of, issue responses on my behalf.
As I get more confident in it. Yes, it could absolutely just spit up… spit out, you know, 300 issues. I probably don't want it to do… To do that all in one hit, but… but yes. Yes, we could create… create issues, and the… the plans can be quite… Some of them are quite detailed on what needs to happen.
Yeah, alright, well, I'll go and do that, right after this meeting.
That's an easy one.
Does anyone else have anything else they wanted to raise or talk about?
Today, before you all get back to work, and I… Wind up for the day.
**Paweł (Elastic)** 51:29 I just wanted to let you know that I will start work on the PHP 8.6 support in the distro.
And, and I try to add the thread-safe mode into the distro, so… but it's… it will be a bit long-running process.
So I have to get some time to do that, make some planning, and share with other tasks I have.
So, yeah, but that's my plan for the upcoming Upcoming days, and maybe 2-3 weeks.
**Brett McBride** 52:05 Sounds great. That just reminded me, has… I can't remember if we've… Apart from… I think we run CI through 8.6 for OpenTelemetry PHP, but… possibly a couple of other things we need to do, like the, maybe… I can't remember if we've added the polyfills yet for… We're probably not using any PHP 8.6 isms yet, but I'm sure we will.
That's probably worth chasing up.
**Paweł (Elastic)** 52:36 I also reviewed the original extension.
Because I'm a bit concerned about the globals, I mean, the process globals, so I'm not sure if they are protected with some… Mutex, or rather, locking mechanism.
I'm not sure if it's totally thread safe, so I will take a look into that and check the Regina extension, so, yeah.
A few weeks ago, I just… I just took a look into that, and I wasn't sure that he… if… I think that maybe we are a bit lucky.
Right now. Yeah, I have to be sure that it's stable.
everything… I mentioned the thread safe is… the reason is that I read somewhere that in the PHP 9, they want to drop the support for non-thread safe, so they will switch to the thread-safe mode.
So, yeah. Huh.
I'm not sure if it will gonna happen or not, but I read it somewhere, so… something is… is… it triggered me to put more effort into that, and one of the biggest triggers was that they dropped support for the… in the Docker registry, so… now the… the 8.6 images for the CLI, they are… all of them are thread-safe now.
So, if we have something in… in our CI, and we are going to… if you are testing the, let's say, non-thread safe mode against the thread safe, then it's… it will… it will require a bit of changes from our side, but I don't… I think we don't have anything related to the trade safe or not trade safe in our test base, right?
So we are just seasoning.
**Brett McBride** 54:36 I think so.
**Paweł (Elastic)** 54:37 Damn.
But if, if something will start to, to fail.
Then the reason might be it's… it's… it's trade safe, so… Yeah.
**Brett McBride** 54:47 Yeah, that's fascinating, I didn't know that. I can only assume it's because of all the CVEs that have been… Popping up in the past couple of months.
**Paweł (Elastic)** 55:00 Yeah.
**Brett McBride** 55:06 Okay, well, it seems like we might be done. Got one other item, which is that my… my workflow didn't fire in Slack to tell us about the meeting. It's time zones. It was a real pain to set up, so… I'll go and have another play with it.
But if we're done, then I will… Take care of the… my to-dos from here, right now, so… Keep an eye out, and I'll let you know on Slack.
So, thank you for your time, everyone.
And I'll see you next week if you can make it.
**Paweł (Elastic)** 55:46 Take this way.
**Chris Lightfoot-Wild** 55:47 Northern Ire.
**Brett McBride** 55:48 Alright, goodbye.
**Chris Lightfoot-Wild** 55:49 Cheers, boy.
