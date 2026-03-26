SIG: Java SIG
Date: 2026-03-19
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:24 Hey there.
**Jay DeLuca** 01:26 Hello.
**Gregor Zeitlinger** 01:28 Hello!
**Trask Stalnaker** 02:19 Alright, we have got a short agenda.
So let's go!
Jay, I saw the issue closed!
Congrats!
**Jay DeLuca** 02:44 Yeah, I think we… I think we started about a year ago.
Populating those, so… Yeah, not bad. But yeah, pretty exciting. And yeah, so my topics are basically… now that we have all this information, I've been playing around with some of the different ways that we can… we can start to use it.
**Trask Stalnaker** 03:05 Do you want to share?
**Jay DeLuca** 03:05 So, yeah.
So there's two… two things. So one is, for anybody who might not be aware, we have started, another project within OpenTelemetry.
called the Ecosystem Explorer. This was… Built off of the proof of concept, that I had built, Late last year, using the metadata, but we've now Moved it into an official project, and we're slowly, piece by piece.
productionizing it, and building it up. So it doesn't have full parity yet, but one of the things that I wanted to show was, I've been experimenting with, like, a UI builder for declarative configuration.
And so, like, you can… This is all hooked up to the schema, so we have all the different options, you can come in, you can change the different values.
Could make different samplers, all that.
And it will basically populate and build the schema for you, and then… With the instrumentation, we could say, like, add all to give us, like, a… Basically, a kitchen sink of all the existing configuration options, including their default values, so if we wanted to just Basically, have a starting point with all the… Everything mapped in, we could do that, or… you could just say, like, oh, I just want… the values for, like, the AWS… Instrumentations, or… Something like that. But yeah, just still playing with it, but if people have ideas of… Like, what this type of experience might benefit from.
Feel free to let me know.
So I'll pause on that one before I show the second thing that I've been doing, but…
**Trask Stalnaker** 05:07 Any ideas, when the registry stuff would be on the website?
**Jay DeLuca** 05:16 So, it… it… It is available now, sort of.
**Trask Stalnaker** 05:22 Huh.
**Jay DeLuca** 05:22 like, this subdomain, explore.opentelemetry.io, like, this is live. It just doesn't have… it just doesn't have the fully populated, like, I'm still working through the detail page.
**Trask Stalnaker** 05:36 Oh, okay, so of which, yeah, because I've wanted to go and check before… looking forward to being able to see… look at the… all the attributes that are emitted by certain telemetry.
**Jay DeLuca** 05:50 Yes.
**Trask Stalnaker** 05:50 instrumentation.
**Jay DeLuca** 05:52 Yep, so that… that's… that will be there. So, like, yeah, we have that basically in the POC. That just needs to be ported over.
But I think my second project might, touch on some of that too, but Jack, you have your hand up?
**Jack Berg** 06:08 Yeah, can you go back to the config?
**Jay DeLuca** 06:13 This is experience.
**Jack Berg** 06:14 And it's… Can you refresh the page?
Like, I want to see what it looks like.
Okay, so, one thought is, like, to… have the, you know, the default config that you add to reflect the default config, or the getting started config from the OpenTelemetry configuration repo. There's a couple things in there that are… that are good to have as… and, like, you know, might be potential snags if they're not included by default, so the hotel getting started.
So, resource detectors, so referencing the standards that are resource detector, service host process container, and then the attribute list, so resource.attribute list up there, where it, references the standard environment variable. I think those are going to be, like, you know, common pitfalls, and people will be surprised if they're not included.
**Jay DeLuca** 07:13 Good call.
Great, yeah, that's great feedback. I'll… I can make this the starting point, essentially, for all the SDK components.
**Jack Berg** 07:23 And I think your starting point had at least one thing that I don't see in here. If you scroll down back to that, get started.
I don't think there's a sampler. Oh, okay, no, it's the sampler, it's the parent-based, always on. Okay, so that… that reflects the, you know, the default of the, of the SDK, if you use environment variables, so I guess that's why that was chosen. I think yours, I think, used the… did it use the parent base with the root set to trace ID? No, no, no, okay, no, they're in sync, sorry.
No comments there, then.
**Jay DeLuca** 07:57 Cool. Thanks for that feedback.
**Trask Stalnaker** 08:01 How is the collector, Data being gathered.
Is it the same, JSON file structure?
the Java agent has…
**Jay DeLuca** 08:20 It's a little different. So, within the collector, they already have, like.
metadata, files per component. And so what we've done is, on a nightly basis, this basically goes and aggregates all of them into these different So we have, for each version, we'll have a different folder of the different schema files.
Now, we… and then for the actual use on the registry, we do convert that into a JSON Like, content address database that we then… I'm gonna load up into, like, a… Index DB on the front end, but, But yeah, so basically we're just scraping the metadata files directly from the repos.
**Trask Stalnaker** 09:11 So the… the reason I ask is, actually, I am… I've been… Looking at all the different… telemetry emitted by all the different Gen AI instrumentations.
And so I was… Thinking about this… project, and, like, I was considering adding, like, where you have Java Agent and Collector in the top right, adding, like, a GenAI, something that I could… Pull stuff in there.
What… do you… has there been any discussion of… What would be the right approach for extending this beyond Java agent and collector.
**Jay DeLuca** 10:01 So, there's… there's no standard yet, but basically we have issues open for some of the other languages, like .NET, Python, and JavaScript, to basically go out, identify what data sources are there, what it would take to… fill in any gaps, and then, ingest them, basically, to do whatever. But what… what is… when you're… when you say Gen AI, like, what do you foresee, actually, like, the user experience being? Like, what would I be looking at on that page?
**Trask Stalnaker** 10:36 Yeah, so, let's say, just within the Python Gen AI, there's, like, there's… there's OpenTelemetry Python Contrib, there's OpenLelemetry, there's Open Inference.
there's, like, a… not just within OpenChurch, but externally also, and… They all sort of… have a very different, telemetry that they're emitting. What I want to do is kind of be able to view… How well things are… Conforming to the semantic conventions, or what additional things they emit, so that we can kind of… Start to try to… Encourage people to normalize.
**Jay DeLuca** 11:30 Yup.
And that is… mostly in Python, or cross-language?
**Trask Stalnaker** 11:38 It's… Across language, but mostly, mostly in… I mean, I'd be happy to only start in Python.
**Jay DeLuca** 11:47 Yeah, I think that's… that seems like a reasonable… like, a reasonable use case for this, like, that… that is, like, an ecosystem component, and… I think it has a lot of similar characteristics, I can create an issue, and we can start… I can look into that a little bit, and see what that might look like.
**Trask Stalnaker** 12:08 Yeah, are you thinking… I mean, I know with the Java instrumentation, you're capturing the telemetry from the tests themselves to create that. Yes.
The… is the collector doing that, or the collector is just a manually curated…
**Jay DeLuca** 12:29 The collector, yeah… They have, I don't know if it's Weaver specifically, but they use, like, a lot of the Weaver format to document.
**Trask Stalnaker** 12:41 Oh… They generate… they auto-generate some code from that.
**Jay DeLuca** 12:45 Yeah, so that's what… so I'm scraping their… their Weaver information, essentially.
**Trask Stalnaker** 12:51 Nice.
**Jay DeLuca** 12:52 But, yeah, we would probably need to look at those other… the Gen AI projects and see if there's… a source, or if we would need to infer them in some way. That's really the challenge. This took us a year to do Java, so…
**Trask Stalnaker** 13:06 Cool, cool Thanks.
**Jay DeLuca** 13:09 Yeah, but so on that topic, this other thing that I've done, was I've taken all of the metadata, and I've built a system that transforms it into a Weaver-compliant format, and then runs the Weaver Live Check against each module, and then gives us, basically, any of the outputs, whether it's, like, an info or a violation.
And then One thing that I'm… I'm still working on this, this is mostly a data quality issue, it's not necessarily this, but I'm trying to track the compliance against Semcov with So, like, if we look at the telemetry just with the SEMCOM opt-in enabled.
just to make sure, you know, that we're not emitting other things. Like, these ones are still failing just because I don't think that we have the test cases annotated correctly, so I need to go back and, continue to kind of Massage those, but just gives us a way to kind of have a report card of… you can even switch between, like, different versions.
But obviously, a lot of these misses are just data quality issues right now, but the idea being, as we get closer to 3.0, we might be able to use this to just double-check, make sure everything is what we expect, and then maybe have… after we release 3.0, maybe we have this run in CI or something, and give us some kind of heads up if something gets added that isn't, stable, but… Yeah, just kind of a toy that I've been playing with, but… Just wanted to share.
**Trask Stalnaker** 14:43 Nice.
Cool, let me share back and see if our agenda has indeed grown a little bit.
Gregor, speeding up the builds.
**Gregor Zeitlinger** 15:04 But before we get to that, I realized that I wanted to add something But, traders, told about, because we also talked about it.
And, I have added, a pull request for, Autel IO, where I have, First documented, the… Spring Boot, because I think now it's the first time that it's actually usable. And then, on top, that was Jay's idea, I have added an automatic converter for where you can plug in your environment variables, and then you get out the declarative configuration.
And, this is, split into two PRs, and this is… the second one, and I just thought about it, when, I think, Jack, you mentioned that there is something about, Sampler or something that I probably forgot about, and… That is in here. I wanted to show it, but you can actually…
**Trask Stalnaker** 16:08 Oh, yeah, yeah, you wanna share?
**Gregor Zeitlinger** 16:10 No, if you have it running, even better. I didn't think about that option. That's great. It's in the zero instrumentation, I think you're in the wrong… a path… Yeah, it has two new sections in the agent and in the Spring Boot Starter, and if you go to declarative Configuration.
Then you should have, below the getting started, a way where you can do the Right, the conversion.
And, the conversion is interesting for, two things. First, it has all those nitty-gritty rules.
That are hard to get right, and then it also has, something that is not dependent on what you put in, which is the getting started configuration. And this is where I'm probably forgetting about some things, so this is where it needs particularly good review. So I have added the propagators.
Already, but I have forgotten about the samplers, and I think that's because it's also missing in the getting started above.
Yep, I think that's…
**Trask Stalnaker** 17:23 Nice, nice.
**Jack Berg** 17:24 You and Janie to go to the spec meeting and show this stuff off, this is… This is very cool, like, an automatic translating mechanism for environment variables to declarative config, and I know there's a bunch of Java-specific stuff based on the agent conventions, but there's for sure things that are just related to the standard environment variables as well that would be Language independent.
**Gregor Zeitlinger** 17:49 Yeah, it is, it is. Yeah, good idea. I'm on vacation next week, but, either you can take it there, or I can do it.
The week after.
**Trask Stalnaker** 17:59 Next week is KubeCon, no… there will be no spec meeting.
**Gregor Zeitlinger** 18:03 Okay, yeah, then, then let's do it. So, it has also a section for a Spring Starter, but that's very similar. It just is this YAML format that you have in Spring.
**Jack Berg** 18:18 Hey, two quick comments on this, Gregor. So one, up at the top of this… document, there's a warning that declarative configuration is experimental. I think it's worth, adding some additional color to that at this point, considering that the data model is stable, and that there's bits within the Java agent which are probably… which are still experimental, but other bits are quite reliable.
**Gregor Zeitlinger** 18:49 Okay, what's a good framing for this point in time?
**Jack Berg** 18:58 So, I feel sort of out of the loop with what the state is in the agent itself, but, you know, all the stuff in the SDK, where the code is located could be shifted around, but, like, the semantics and the schema, I think, are going to be… are going to be reliable, are going to be stable, unless, like, you know, you're using a property that explicitly has the development suffix.
And so, I guess, I just wanna… not scare off users. And, like, you know, it's basically, it's stable unless… unless otherwise stated. And, like, you know, how do we otherwise state?
And, like, you know, the development suffix is one place where you can… where it's clear that, you know, the thing is still experimental. But, is there anything else in the Java agent which is, like, sort of structural? Structurally experimental?
**Gregor Zeitlinger** 19:55 So, this, big, dashboard of all the tickets, that, I wanted to, land is in a pretty good shape now. So this development suffix is probably one thing to call out.
task. Do you have anything in mind? You also spend a lot of brain cycles on that?
**Trask Stalnaker** 20:18 Yeah, I mean, so, in the latest version… Right, we support the OTel config file Without the experimental… word in it anymore, and so that essentially makes it kind of de facto stable for the Java agent.
For anything that, you know, again.
Yeah, it doesn't have the slash development suffix.
The… the key being that, Basically, every single Java agent property that basically only applies to the SDK.
being stable SDK config, because every single Java agent configuration, even if we Even if it's stable for us, it's still under the instrumentation slash development node at the root.
So it is technically not stable.
**Gregor Zeitlinger** 21:22 Right, technically, but I mean, what is the message that we want to send to users? Because we have already said that we treat each individual setting on its own. If it has development, then it is unstable, but not just because it's under the instrumentation. That's what I remember.
**Trask Stalnaker** 21:43 It cascades down, so if you have logger provider slash development, that means everything under it is development.
**Gregor Zeitlinger** 21:53 Right, but not just, because it's under, instrumentation slash development.
**Trask Stalnaker** 21:59 Why not?
**Gregor Zeitlinger** 22:01 That's what you said last time!
No? No.
**Trask Stalnaker** 22:06 That's why I've been pressing Jack. I'm like, don't forget about the instrumentation node with stability. I mean, I'm like, this is awesome that the SDK configuration is stable, but it honestly doesn't do a whole lot for us in the instrumentation repo.
**Gregor Zeitlinger** 22:27 Well, to sum it up, it sounds like what we currently have on there is pretty close to what we want to convey.
**Trask Stalnaker** 22:45 I mean, I'd be fine with saying that the SDK Configuration… you know, we could nuance it with slash development, but yeah, I mean…
**Gregor Zeitlinger** 22:57 and one sentence. I want to really shrink it down to one sentence.
**Trask Stalnaker** 23:06 Yeah, I mean, it's gonna be hard from the Java agent perspective to say that declarative config Is stable until we have the instrumentation node is stable.
**Jack Berg** 23:20 So, yeah, I agree with that. And, like, yeah, so basically, you know, something to the effect of, like, look for the presence of the slash development suffix. Anything with that is not stable, and, you know, you can specifically call out that at least all the core SDK configuration is stable. That's something.
**Gregor Zeitlinger** 23:41 Okay, then I'm…
**Trask Stalnaker** 23:42 Two sentences.
**Gregor Zeitlinger** 23:46 then I will make, like, another… a bit longer version, yeah. Okay.
**Trask Stalnaker** 23:51 Give it a try, and tag… tag me and Jack on it, on your… on this… The change once you make it, and we'll… Look at that.
**Gregor Zeitlinger** 24:03 Okay, I'll make a specific PR just for that, so that it's not intertwined with the other changes.
**Trask Stalnaker** 24:09 Oh, goodness.
**Jack Berg** 24:10 You know what? You know what, yeah, that's a good idea. I owe the core Java docs an update, now that declarative config has changed. I want to, like, change how we frame declarative config up in, you know, docs languages, Java, and then there's, like, a dedicated configuration page, and so I can do a pass on this as well. So, like, everywhere we talk about declarative config and stability and experimental, we do it in a consistent voice.
**Gregor Zeitlinger** 24:37 I like that, yeah, I'll take it, thanks.
**Jack Berg** 24:40 Okay.
And I had a second comment, too, which is, can you scroll down real quick on this page?
So, no, no, up to the, like, oh, no, this… I think somewhere you gave a demonstration output, so you had, like, a…
**Trask Stalnaker** 24:56 This guy?
**Jack Berg** 24:59 Yeah, where were we talking… yeah, is… Where is this source from? Like, what… Do you just have a, oh yeah, this is what I was talking about, this getting started here. So, what I was gonna say is I was gonna suggest adding a submodule to Opentelemetry.io, pointing at the OpenTelemetry configuration repository, so you can directly embed the, the… the snippet for the… Getting Started example file, rather than having to keep them in sync, you know, by convention and manually.
**Gregor Zeitlinger** 25:35 I think this is gonna work for, what we see right here, but for the other one, which is in JavaScript, it's a little bit harder to do. Yeah. Maybe not impossible, but at least a bit harder.
**Jack Berg** 25:47 Definitely, definitely harder.
**Gregor Zeitlinger** 25:50 Okay, yeah, I'll make a note of that, thanks.
**Jack Berg** 25:59 Yeah, I like the idea of just, like, having a sort of standard resource that we consistently point to across the ecosystem as, like, a good getting started point for declarative config.
**Gregor Zeitlinger** 26:09 Yep.
Good idea.
**Trask Stalnaker** 26:12 Yeah, that would likely be pulled into other languages, docs as well.
Alright, speeding up builds… trigger…
**Gregor Zeitlinger** 26:27 Yeah, this, was an idea I had, and it seemed like a good idea, but then, Laurie pointed out that we should discuss if it's really worth the complexity. I thought, yeah, that's a good point before I continue on that. Let's discuss that first.
Is that really the right link? I think it has a link where I have… the interesting data, the impact that I'm estimating to see.
If we, should, pay the complexity tax, or if we should just, Forget about this idea.
**Trask Stalnaker** 27:14 So, I mean, I have… my, I still have, trauma from… dealing with Gradle dependency, not understanding all the implicate… all the up-to-date checks.
Not being… Correct before, in the past.
And it's so easy to then, like, a test doesn't run that should have run, and you end up merging stuff, and then it fails, later on, and you have to track that back.
Hmm. So… I will just say that's… that's where I'm coming from, in that Just the whole idea makes me nervous.
But I… have not really… I haven't looked… At it, sort of, because the whole idea scares me.
**Gregor Zeitlinger** 28:14 I totally get that, yeah. It makes it more complicated.
**Trask Stalnaker** 28:21 And we're trying to… I feel like the Gradle is supposed to… I mean, you were mentioning… I think I asked you this in chat, how this is better than the Gradle up-to-date.
Stuff.
**Gregor Zeitlinger** 28:45 Yeah, that just catches more cases, like, smoke tests, that is, more complicated. That also makes the script logic more complicated, because the smoke test does not need to run for every, change. If you change an instrumentation that is not covered by the smoke test.
then I would argue that you shouldn't run the smoke test.
**Trask Stalnaker** 29:17 Is that something that could be encoded into the Gradle up-to-date checks?
Or, like… the smoke tests?
**Gregor Zeitlinger** 29:28 I don't know how that works, so I cannot answer you that.
I, just add it as a comment, then I, And check it out.
**Lauri** 29:40 The problem is that sometimes it's difficult to tell whether… Changing some module actually affects any smoke tests.
**Gregor Zeitlinger** 29:51 In the dependency graph, Would not tell you?
**Trask Stalnaker** 29:58 Well, if the dependency graph told you, then Gradle would know. I think with smoke tests, the problem is that it depends on the bundled Java agent. So therefore, it depends on…
**Lauri** 30:09 I was actually thinking that maybe the easiest way to speed up the smoke tests would just be run… would just to be… run less smoke tests.
We run smoke tests on a ton of different versions, a ton of different JVMs.
I'm pretty sure we could, at least for pull request builds.
Come up with a smaller set of smoke tests to run.
**Gregor Zeitlinger** 30:34 That's also a possibility, yeah?
**Trask Stalnaker** 30:39 Yeah, we've done that, I think, in a couple cases before. Like, I think with Windows, I think we don't run the smoke… the Windows smoke tests on PRs, but we do… on Merge Domain.
Or in the daily build.
Yeah, I mean, that makes a lot of sense. It's… I would say it's pretty rare that yeah.
that one specific Tomcat version fails, but not another.
And we would catch that still in the daily.
**Gregor Zeitlinger** 31:24 But… I think the test should be way faster. That's where I'm coming from.
So in other projects, 5 minutes is already very slow, and, We don't have that, of course, but, That's what I would like to have.
**Lauri** 31:52 What is currently the slowest step?
Or, like, What is the step that needs to be always run? Like, what's the minimum amount of time that the pull request can take?
Is it CodeQL?
**Jay DeLuca** 32:07 I think I have…
**Lauri** 32:08 Like, 15 minutes?
**Jay DeLuca** 32:11 I have a dashboard that shows this.
**Trask Stalnaker** 32:17 Let's see, we've got… Because…
**Jay DeLuca** 32:21 the Grail VM.
**Trask Stalnaker** 32:27 Yeah, the smoke tests are pretty long there, definitely.
Most of the others… let's see, we've got some…
**Gregor Zeitlinger** 32:36 But, some of them, could be, made faster if you have more buckets that run in parallel. GraalVM is a candidate where it really, could hit a limit, because you have to do all those steps in sequence.
Right. Can I share my screen for a second?
**Trask Stalnaker** 32:59 Oh, yeah.
**Lauri** 33:01 I was actually meaning, like, what's the minimum amount of time that we could, like, Get the bills, too.
like, if you always run the CodeQL step, then… It took 17 minutes from the pull request that Trask showed.
**Jay DeLuca** 33:19 But here I have…
**Lauri** 33:20 Any step that takes less time than that probably isn't going to affect the total time.
**Jay DeLuca** 33:29 This is the list of jobs by average duration.
**Trask Stalnaker** 33:34 Oh, that's nice.
**Gregor Zeitlinger** 33:37 Like, GrowVM does not always run, so I think, We should ignore that for this purpose.
**Trask Stalnaker** 33:47 So yeah, I mean, it looks like Test 1 probably maybe needs to get Split out or rebalanced?
And the smoke tests… You know.
as Lori suggested, run a… run against… have a different profile to run against, maybe only run against the latest ones in PRs.
**Gregor Zeitlinger** 34:17 What would also be interesting to know is, how effective the different test categories are, I mean, like.
Have we ever found a bug that Only occurred in one of the… observers…
**Trask Stalnaker** 34:37 That's why Lori is suggesting just, you know, we could reduce the number of App server versions that we run against.
**Lauri** 34:46 Well, even not necessarily the app server versions, but, like, the app server and JDK combinations.
Like, if you run something on JDK 8, 11, 17, and 21, Then we probably could just… Run it only on one of the versions.
**Gregor Zeitlinger** 35:08 On one of the JDK versions.
**Lauri** 35:12 Yes.
**Gregor Zeitlinger** 35:15 So, like, have one on Tomcat, one on, Jetty, and… so, like, one on each app server.
**Lauri** 35:24 Oh, whatever is clever.
**Gregor Zeitlinger** 35:27 Yeah, I think that's… that's something that we could try.
Definitely easier than, what I had.
In the beginning.
Yep, I'll try that out.
**Trask Stalnaker** 35:43 Cool.
**Lauri** 35:44 Well, if you want to work on the build stuff, like, I'm sure there is, like, plenty of other things that could be considered.
Like, one thing that might help us in some situations, would be to… to cache the Docker images.
Currently, occasionally, bills fail because, Downloading a Docker image times out.
**Gregor Zeitlinger** 36:15 Don't we already have the Docker images cached? I thought so.
**Lauri** 36:20 I don't think so.
**Trask Stalnaker** 36:21 I don't think so. I think intentionally, though, just because they tend to be big, and… The… the… our cache is limited.
**Lauri** 36:36 And also, like, the cache setup, Probably could also be improved.
I think the problem is that, like.
The setup currently plugin caches all, like, precious things.
And to avoid that, it… so, like, it would compute, like, a different key for each, like, workflow, somehow.
And to avoid caching too much, we have, like, set some of the executions to use read-only cache.
I think, actually, we probably only need, like, one job that, Like, if the main build job, Could be, like, the only one that actually updates the caches.
**Trask Stalnaker** 37:34 Isn't that the case?
**Lauri** 37:38 I suspect that we might have missed, like, some places where the… Cradle setup is used.
And I think we also saw… Maybe enabled it for one of the test jobs, but it probably isn't necessary What might complicate things is that We have, like, some jobs that aren't, like, Strictly related to our main job.
Like, the… Like, the overhead benchmark and stuff like that.
Those could also end up messing with the caches, because I think that the setup Gradle plugin, it just, like, if it doesn't find, like, an exact key, it just uses some random one, or, like.
**Trask Stalnaker** 38:31 There's some complicated, yeah, logic there that I agree that there's… I know we spent a lot of time trying with Nikita long ago, and then I made another pass after that at some point. Trying to improve the situation, but… It is…
**Lauri** 38:52 When Nikita was working on it, we still… we were still using, like, the… The other plugin, like, the one that… where we had to manually manage the caching.
But yeah, like, photographer images, I think there was, like, an… a GitHub Actions plugin that did it, but the problem was that it was written by some random dude.
So, I'm not sure whether you would agree with using it.
**Gregor Zeitlinger** 39:26 Well, maybe there is something new. If we haven't looked at it in a time, then maybe there's an easy win.
**Trask Stalnaker** 39:37 Yeah, just, you have to evaluate the trade-offs, right? Github has been… finally started enforcing the cache limit size.
So we are limited to 10 gigs in the cache.
So storing… Docker images is gonna overflow, you know, could impact our Gradle caches, and… probably, you know, it's more… it's better to have all those Gradle artifacts downloaded, or build caches downloaded, then a Docker in a big Docker image, which can be… downloaded.
faster.
**Gregor Zeitlinger** 40:21 Oh, that's why…
**Trask Stalnaker** 40:22 miscellaneous files.
**Gregor Zeitlinger** 40:24 That's right, does it matter where the Docker image is stored?
Maybe we are not using, one of the fast.
Registries?
**Trask Stalnaker** 40:42 I mean, I'll… You'll need to dig into that. I mean, a lot of the stuff, the Docker stuff, we store local… we store in GitHub Action… I mean, in GitHub packages, the actual smoke test Docker images that we use, so that's gonna be pretty… Fast.
**Lauri** 41:00 I think the smallest Docker images aren't the issue. The issue is with the Docker images that we use in the normal tests.
**Trask Stalnaker** 41:07 Mmm, the test containers.
**Lauri** 41:09 Hmm.
I'm pretty sure that the guys from Docker Hub hate the people who always download the images for every build.
**Gregor Zeitlinger** 41:21 So those should also be repackaged, like the smoke chests?
Would that be the idea?
**Lauri** 41:27 That probably is too much effort.
**Trask Stalnaker** 41:37 Gregor, I don't think there's any easy answers in… down this road. I mean, it's a very fruit… potentially fruitful area, but it's… you're gonna have to spend a lot of time on it.
Anytime that I've dug into this stuff, I've spent, you know, weeks trying to make small improvements.
**Gregor Zeitlinger** 41:58 Okay, yeah, that's also very good feedback. At least I've tried.
Alright, let's go to the next topic.
**Trask Stalnaker** 42:10 Cool. Alright, let me share back… And… Jack…
**Jack Berg** 42:28 Yeah.
**Trask Stalnaker** 42:29 on pretty print to logging OTLP exporters.
Alright.
**Jack Berg** 42:37 Yeah, so a little bit of context, we have this, these long-existing exporters that are called, like, what are they called? OTLP JSON logging, span exporter, things like that, OTLP, JSON logging, metric exporter, and you know, we've had those for as long as I can remember, and maybe a year or two ago, somebody introduced a standard out exporter at the spec level, a standard out OTLP exporter, which was kind of standardizing the concept that we have long had, but used a different name.
And so we have this internal, OTLP standard out.
log record exporter, OTLP standard out, span exporter. And, this person, wants to add a new Pretty Print configuration option to these, which is… a reasonable thing to ask. It's really hard to read, these, like, long, dense JSON strings without copying and pasting them into your JSON formatter. And so, like, if you're debugging, why not just have, like, a pretty print option that you can turn on?
For your local machine. And, you know, they added that, and it works. And then they were talking about, okay, how do I actually enable this? Like, how do I flip this on?
And we're declarative config first now, and so we don't want to add, you know, system properties or environment variables, and we definitely don't want to add them if there's no declarative config equivalent, and we definitely don't want to add them for deprecated components, like the OTLP JSON logging exporters.
Or, you know, components, they're not deprecated yet, but, like, you know, the intent is for these standard-out versions to supersede them.
And so, you know, also, this option doesn't exist in the spec yet. And so, what I'm trying to figure out is, like, you know, is the… can we establish a precedent for how we, how we represent Java-specific declarative config options?
For, you know, otherwise built-in components, things, you know, types that are part of the declarative config schema.
And what… what would that convention look like? Here, I've kind of proposed that, you know, if you're going to add an option like this, you add the development suffix, but you also add, underscore language suffix to development, so you can indicate that this is an option that is in development, and it's specific to Java.
But we don't have a precedent for this yet.
**Gregor Zeitlinger** 45:14 Why is it specific to Java? Would other languages not be able to do the same?
**Jack Berg** 45:20 I, so I opened a spec issue to add a new property at the spec level for the standard out OTLP exporter that would, like, you know, standardize a pretty print option, but, like, you know, it's still… gathering steam. And so, like, hopefully, there is a general-purpose pretty print option that applies across all languages, but, you know, you know.
Do we want to block on that, essentially? Or do we want to provide a capability sooner?
And I think I'm inclined to provide a capability sooner.
**Gregor Zeitlinger** 45:56 Sounds like this would be the POC implementation.
And in other POC implementations?
We also don't have an indicator that the POC was in a particular language.
**Jack Berg** 46:10 We don't have… I don't know of any instances where the built-in exporters or the built-in components we have, whether it be, like.
batch span processor, or batch log processor, or the OTLP exporters, or Zipkin exporter, or any of the samplers. I don't know of any instances where we have an additional Java-specific configuration property for those, which lives outside the… which is outside the declarative config schema. So that's what's new about those.
**Gregor Zeitlinger** 46:39 quote about the schema, not that you have created a spec PR that is still and development.
It sounds a little bit like it's just this artifact that we have this schema that is making it more difficult. Not the process itself, but we're proposing something and trying it out in one language first.
**Jack Berg** 47:05 Well, it might never land at the spec.
Like, and, you know, if it doesn't land at this back then, you know, I think it's still a good feature to have for our users.
**Gregor Zeitlinger** 47:15 But isn't that inherent to all the things, development, that you don't know if it's gonna be stable, and… Therefore, you want to have More flexibility to try it out in some languages first.
**Jack Berg** 47:33 And I guess that the risk of just… maybe I think what you're saying is that, like, do you really need this underscore Java? Can you just, like, have slash development?
**Gregor Zeitlinger** 47:42 Exactly.
**Jack Berg** 47:44 what, what… I have a sentence here in my comment, so, you know, this should help confusion if users try to take this Java feature and use it in other languages. So, like.
if you don't have the Java, the underscore Java suffix, you know, do you have some expectation that you could pick this up and use this in Go, and it's just, like, a matter of Go not having implemented this yet?
**Gregor Zeitlinger** 48:07 So, the corollary would be that, currently, you can expect that all languages provide all the development features.
That's not, like…
**Jack Berg** 48:19 you can expect, like, it's a reasonable ask for them all to implement the development features. Where if I went and asked, you know, go, hey, what's the status on this pretty print feature? They would say, what pretty print feature? That's not even in development in the schema.
**Gregor Zeitlinger** 48:36 Oh, so we have, like, more… 3 different, forms. We have stable development, and something… More development, experimental development, or whatever?
**Jack Berg** 48:49 Language-specific development.
That's how I'm framing it, because, like, I can only add properties to the schema, development properties to the schema, if there's a development property in the spec. So what do you do if you want to introduce something that's, like, even in excess of that, that hasn't even landed in the spec in development yet?
**Gregor Zeitlinger** 49:08 Sounds like overcomplicating it.
**Jack Berg** 49:12 So you would say block them until there's a feature in the spec.
**Gregor Zeitlinger** 49:16 No, I would say development should not promise that it's available in all languages.
But…
**Jack Berg** 49:23 Okay.
**Gregor Zeitlinger** 49:23 That's… I don't know if that's too harsh, if we currently have a pretty good coverage of all the development things.
**Jack Berg** 49:33 We do. We do, in Java, and… you know, Some languages more than others.
**Gregor Zeitlinger** 49:41 Okay, so it's a tough decision, I get it.
**Trask Stalnaker** 49:46 I have a question, Jack. You… would you take this… Bor, would you ever stabilize this without it being… Stabilized in the spec.
**Jack Berg** 50:03 I don't know, that's uncharted waters. We have examples of Java-specific environment variables and system properties that we stabilized.
And, you know, there is actually a naming convention for language-specific environment variables, right? There's a spec piece that says, like, hey, add, you know, underscore your language underscore in a particular place. I think it's, like, hotel underscore Java underscore, and then whatever your environment variable is.
And so, like, stabilizing this property without it landing in the spec would be some sort of analog to that. So, I don't think it's out of the question, but we haven't done it before, and I haven't…
**Trask Stalnaker** 50:43 So, yeah, where I'm getting with that question is that the underscore Java, like, if it's… if we're gonna do underscore Java, it seems like… This part should be the underscore Java.
**Jack Berg** 50:57 Right.
**Trask Stalnaker** 50:57 There's not really any… path to… I mean, if we're saying that this could be stabilized, You would then drop this.
**Jack Berg** 51:10 That's a good point. So, Java underscore prettyprint, if, you know, to… something to that effect, or prettyprint underscore Java.
**Trask Stalnaker** 51:20 It also helped, I think it's one less rule about slash development.
**Jack Berg** 51:27 Yeah.
**Trask Stalnaker** 51:29 Like, we have… we have some… we have some special rules in our bridging about slash development mapping to experimental.
**Jack Berg** 51:39 Yeah.
**Gregor Zeitlinger** 51:40 Yet another… yet another, possibility would be to have a Java node. So under, the exporter, you would have a Java node, and then Pretty Print. This would be, like, more analog to the environment variable.
**Jack Berg** 52:00 Yeah… And more cumbersome a bit.
**Peter Findeisen** 52:08 I have yet another question. So, what if some other SDKs will pick up this feature?
And the user will have a mixed environment with different languages, and some of these languages will have this pretty print, and some will not.
But they want to share, the configuration as much as possible.
How would we handle that?
**Jack Berg** 52:36 Yeah, so, that… that underscores the importance of not just, like, leaning on language-specific properties. Like, in a healthy ecosystem, everybody is making a good faith effort to upstream these properties and have a standardized schema.
In the event that they don't.
And that, like, you know, you're copying and pasting this config from Java, where it is supported, to Go where this, you know, they have no knowledge of this property.
I would hope that it's, well, and it should be. It should be a graceful degradation, and, you know, the absence of this property just means that they don't have the logs pretty printed.
**Trask Stalnaker** 53:21 Jack, do, the schema… is… does the schema allow a… arbitrary additions? Like, if this was present and Go loaded the SDK, would they emit a warning to users that said something like, your schema doesn't There's a mismatch.
**Jack Berg** 53:42 So the answer is, it depends, and we actually have, so there's this, this… JSON schema keyword called Additional Properties.
And, by default, additional properties is set to false, which means that if you add additional unrecognized properties, the consumer should fail.
But we have a schema modeling rule somewhere that basically says, like, hey, the default should be false, the default should be, like, fail if you see unrecognized properties, but, like.
If… if there's… if a maintainer of an implementation knows about, like, language-specific properties or something that needs to be modeled outside of this schema, tell us, and we can switch to additional properties as true for that specific type.
And I'll try to dig up a little bit of that.
**Trask Stalnaker** 54:31 This would require… Updating the schema, updating that additional properties to true.
In the schema.
**Jack Berg** 54:41 If it's not already set, and I would have to look into that specifically.
So, here's the… Schema modeling guidance.
Yeah, okay. This is… this has given me… like, so where I thought this would go is, like.
you know, kind of, like, the declarative config is sort of underspecified right now in how to model language-specific properties for these types of components, and so I was going to use this as a jumping-off point to actually add more, more language to that effect, so that this is Whatever precedent we set here is, you know, is… applies to other languages as well, and they don't have to repeat this argument, or discussion, let's say.
So yeah, lots of good thoughts here. I like the… I liked, you know, Having just a slash development suffix instead of including the language in the suffix.
I like, like, you know, reinforcing that You know, you should make a good faith effort to model these upstream in the specification and in the schema, rather than leaning on language-specific properties too much.
**Trask Stalnaker** 56:09 Yeah, I mean, my… not… I mean, it seems… reasonable to block on… block this for, like, a month to see if the… I mean, we get steam of the upstream Let's see, you have this… Requested… Oh, we've got… yeah, there, we've got two thumbs ups.
**Jack Berg** 56:36 Alright.
**Trask Stalnaker** 56:37 I'll approve, I'll approve your PR.
**Jack Berg** 56:41 And you know what? If, if this person's PR is, you know… they can actually still achieve what they want without landing this Java-specific property, because they can, like, rip that out, and they can still programmatically configure it using the exporter customizer features that we landed.
There's an SPI mechanism where you can customize exporters programmatically, so it is cumbersome. It's not friendly UX, but it is possible.
And, you know, if this drags on too long at the spec level, that's probably what I would recommend, rather than having them wait indefinitely.
**Trask Stalnaker** 57:26 Cool!
**Jack Berg** 57:29 Thanks for the chat.
**Trask Stalnaker** 57:33 Anything, any… oh, no, we are out of time. Alright.
Great to see y'all.
**Gregor Zeitlinger** 57:40 See you.
**Trask Stalnaker** 57:41 Next time. Oh, we… I would say we probably won't meet next week, because it's KubeCon. I mean, I guess I'm not gonna be at KubeCon. Jack, what… are you going?
Nope. No.
Alright, so maybe we will meet next week.
**Jack Berg** 58:00 We can now.
**Trask Stalnaker** 58:01 I'll leave it on the calendar.
**Jack Berg** 58:01 in the Slack channel and see if folks are gonna be sticking around.
**Trask Stalnaker** 58:06 Alrighty.
**Jack Berg** 58:08 See ya.
**Trask Stalnaker** 58:08 Bail out.
