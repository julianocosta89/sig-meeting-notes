SIG: Java SIG
Date: 2025-09-18
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/LHM-P3dUzf5G-cOdqexEAAYYJ5XL1l1g-vg5RbmAHob7s3EZqH23S5yEApdTz_QL.vEJInkPJlOQ21lHB
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:31 -Oh.
**John Watson** 00:39 Good evening!
Gregor, what part of the world are you in? You're in Europe somewhere, right?
**GZ Gregor Zeitlinger** 00:46 Berlin.
**John Watson** 00:47 Well, Berlin!
Fancy.
Do you like Berlin?
**GZ Gregor Zeitlinger** 00:56 Lived here all my life, it's, it's not the fancy city for me, it's just the normal city.
**John Watson** 01:06 My wife, visited Berlin right after… The wall came down.
She was in Germany during high school.
Said it was… she said it was quite, quite an experience.
**GZ Gregor Zeitlinger** 01:23 She picked a great time, I guess.
**John Watson** 01:27 So it was still, like, still checkpoints, though, still difficult to get across the city, still felt a little uncomfortable, but…
It was, definitely a time.
**GZ Gregor Zeitlinger** 01:38 Yeah, these days, it's more the public transport that is giving us a hard time.
**Trask Stalnaker** 02:27 Alright, just getting my topics in, let's start.
Jay, do you want to share?
**Jay DeLuca** 02:36 Yes, please. Yeah, I'll keep this kind of quick. A lot of this is just inform-type stuff.
So, starting with… I…
created this README within the project, just so we have kind of a source of truth for the way that we expect instrumentations to be documented. And I'll talk about why this is important later, but… So yeah, so if you're creating a new instrumentation, there's some guidelines here that you can follow, or some hints to
guide you in the structure for that. And, I also…
That's a bad link. But, I moved the… or I copied the supported libraries list
From within the repo to the documentation site, so we now…
have a… it's a little stripped down compared to the one within the repo, but, I put this here. Ecrofana, we had heard from some
customers and support people that, the README wasn't being indexed by Google, and so it was kind of hard to find, and so…
That drove me to move that there. I also…
created a, we had a nightly job that I was using to diff…
the documentation from our site to let us know when it's in sync, and so I updated it for that, too. So, when new instrumentations are added, an issue will be opened automatically to tell us to update the documentation site.
And I've been working through adding READMEs to any standalone library instrumentations that don't have them. And what I've done is, in this Proof of Concept Instrumentation Explorer, I'm now pulling in those READMEs and rendering them. So, like, for our Miria, if you come in, you can see, like, the standard
details that we had before, but now you can go in and get that kind of quick start for standalone library documentation, and I'm also linking to the Java docs. At some point, maybe we can move the Java docs in here, too, if we want.
And then, yeah, I'm working on a community project, document for this instrumentation Explorer and moving it into the OpenTelemetry docs, officially. And so I'll share that when it's done. I'm hoping to have it done by tomorrow.
And now, so that's all the informs. Now I kind of wanted to talk about two different things, fairly quickly. One is this notion of stability. We've had a couple questions come up recently, whether they're in issues or slack about the stability of certain instrumentations, and…
I know that we… we think about it mostly in terms of the semantic convention stability and how that maps, but I'm curious if this is something that we think we should start including in this… this metadata, and if so.
how would we want to think about it? Is it… do we want to say that…
Instrumentations that only emit
semantic conventions, or the latest semantic conventions, are stable, or… Yeah, just curious if people have thoughts about that.
Start that conversation.
**Jason Plumb** 05:48 Like, declaring stability for those instrumentations is just hard in general, because as soon as the library that's being instrumented releases a new version.
We might break.
We have guardrails, but…
**Jay DeLuca** 06:08 Yeah, that's a good.
**Trask Stalnaker** 06:09 That would be,
Stability, to me, means when people consume the next version of our artifact without changing anything else in their system.
That nothing breaks.
**Jack Shirazi** 06:29 What's the benefit of declaring an instrumentation stable?
**Lauri Tulmin** 06:37 If it's a library instrumentation, then,
By declaring it stable, we will be saying that the API is stable.
And for other instrumentations, we say that the telemetry is stable.
That we aren't going to change stuff around.
In backwards, incompatible ways anymore.
**Trask Stalnaker** 07:06 the other… Aspect that comes up, Is whether something is production, Ready?
We got a little…
decent number of questions about, you know, they see that it's alpha-tagged, and they're like, oh, I… does that… that means I can't put it into production, and…
That's not… has not been our stance on the… at least on most of the Java stuff.
**Lauri Tulmin** 07:36 Here's your.
**Trask Stalnaker** 07:36 We're willing to accept the… API breakages.
**Lauri Tulmin** 07:41 I think it's kind of unfortunate, because we aren't doing the API breakages anyway, I think.
Or at least we try pretty hard not to do them.
**GZ Gregor Zeitlinger** 07:54 I think we have it just for the semester.
**Lauri Tulmin** 07:57 It just sounds so bad.
**Trask Stalnaker** 08:00 It does. Yeah.
**Jack Shirazi** 08:03 nature of… it's going back to what Jason said, the nature of instrumentations means that you can never guarantee they're stable, right? Unless we say that any breaking change, we have to actually create a new instrumentation for that
Change, and leave the old one as it is, and then it becomes really maintenance burden.
**Trask Stalnaker** 08:25 So, that has… we've kind of…
That is kind of our strategy, though.
for better and worse. That's why we have encoded the base version
for library instrumentation, specifically, into the artifact name and package names.
So that… If there is a breaking change that we need that will cause us
to break our API or some other contract that we can…
We can do that, at least.
**Lauri Tulmin** 09:05 Yeah, but it also means that…
If we are going to rename the… like, if you are going to change the version and change the package name, then everybody who depends on that instrumentation will be completely broken.
**Trask Stalnaker** 09:21 Can you explain that again?
**Lauri Tulmin** 09:24 Like, because we changed the package name, like, anybody who depends on the old package name won't compile anymore.
**Trask Stalnaker** 09:35 Oh, yeah, the… If they update their library version.
I mean, the… the underlying… instrumented library.
**Lauri Tulmin** 09:47 Obviously, one thing is that As far… I think we currently don't have any stable instrumentations.
**Jason Plumb** 09:53 Yeah, I was gonna ask that, like, do we make a declaration of stability at all on any? And I think, yeah, I think Lori just answered that.
**Jack Shirazi** 10:02 I mean, Moving to a different point of view, Jay is asking, because of the documentation he's doing.
But we… a few of us have distributions that we are providing customers.
And we are supporting those directly. And have we had any feedback from customers saying, we can't use this because the instrumentation isn't stable? I know that we haven't had that.
So… I don't know if you guys have had that.
**Trask Stalnaker** 10:32 tends to be less of a problem for the Java agent.
And more of a prob questions come up for people who are using library instrumentations, because they see that big alpha tag on the library instrumentation dependencies.
And that scares them.
So I would say almost exclusively, it's…
Questions from people using library instrumentation?
**Lauri Tulmin** 11:02 If, instead of alpha, we used any other word, like apple or carrot.
Everybody would complain.
**Jason Plumb** 11:07 Yeah.
**Trask Stalnaker** 11:08 Yeah.
**Jason Plumb** 11:08 Agent?
**Trask Stalnaker** 11:09 Beta would be so much better.
Maybe even Gamma.
**Jason Plumb** 11:16 I mean, and Trask knows this, but we're also getting beat up in Android right now, and so there's a concerted effort to move that forward, because people see the…
the semver leading zero on the semantic version, and they get scared, and then there's also the alpha suffix, so it's the combination there.
**Jack Shirazi** 11:33 Yeah, but that's at the agent level, not the instrumentation level. We have the same concern. Yeah. So it's, you know, one… you go one… one point something, and you say it's…
It's production ready, and then that's fine. And I don't think anybody cares about the, like, the internals.
They don't need the internals, it's like, as Trask says, I think it's…
It's the library users, and maybe we should just declare those stable as… on an as-needed basis by whoever is asking for something particularly to be stable.
**Lauri Tulmin** 12:13 Usually.
**Trask Stalnaker** 12:14 So…
**Lauri Tulmin** 12:14 Like, declaring anything stable is a… It's a lot of effort.
somebody needs to review the APIs and make sure that everything is backwards compatible, or, like.
That everything is evolvable in the future, and everything makes sense.
But usually nobody's willing to… Undertake that effort, so everything will probably remain.
On stage.
**Trask Stalnaker** 12:40 Also… Yeah, we're also hamstrung by, OpenTelemetry Wide says that, Instrumentation that we publish.
via OpenTelemetry.
Can only be marked stable if the semantic conventions are stable.
**Lauri Tulmin** 13:06 Is there also something with the schema, sir?
**Trask Stalnaker** 13:10 Yeah, but that's… I would… That didn't really… that failed.
That was a failed experiment, and they're working on schema V2 now.
**Jason Plumb** 13:21 So, Trask, to your point about the telemetry, the semantic conventions being stable, is necessary for the telemetry to be stable, if that's true, and we were to bring something stable, and it uses only stable semantic conventions, does that exclude us from using new semantic conventions?
Like, not a change, but, like, a new one that's now unstable or experimental.
**Trask Stalnaker** 13:46 It would need to be opt-in.
**Jason Plumb** 13:47 Opt in, okay.
**Lauri Tulmin** 13:49 Yeah, I think we have solved this, by using flags.
**Jason Plumb** 13:53 That's unfortunate.
**Lauri Tulmin** 13:56 Yeah, but the new… new Semitic convention that's in the…
That's under development can also be stabilized.
**Jay DeLuca** 14:10 I think from the, the gist of this, it sounds like it's probably…
**Trask Stalnaker** 14:14 Is that a rabbit hole that you expect?
**Jay DeLuca** 14:17 Well, I think this… this… so I haven't been focusing on it, and I think that maybe it makes sense to leave it out, for now. Maybe…
Maybe for libraries, standalone libraries, it would make sense, but it sounds like we should probably avoid…
Trying to add that verbiage, at least for now, into just, like, the general agent instrumentations.
Anybody disagree with that?
So, I'll kind of… and we can revisit this, but for now, I'll just kind of… I won't incorporate stability as one of the metadata kind of fields and part of the documentation.
**GZ Gregor Zeitlinger** 14:57 But you could, use something different, like production-ready.
Which is a commitment that we are providing bug fixes.
And also, like, semantic convention stability, so something that is more concrete,
That, I think would scare users less.
**Jay DeLuca** 15:24 Yeah, so the semantic… okay.
**GZ Gregor Zeitlinger** 15:28 If we, say API stability.
Yes or no. This also does not sound scary, because then you can decide, am I interested in API stability or not?
**Jay DeLuca** 15:44 Yeah, and that… so this one, I do plan on incorporating kind of a semantic convention scorecard, and so that could be translated into, like, a…
Semantic invention stability type thing, so…
I think that does make sense.
Cool, and then I had one other thing, but in the… I've already been talking for 15 minutes, so I want to give time to others, but I have one other kind of metadata…
field around kind of describing the functionality of instrumentations. I have an issue that kind of lays it out, and I'll have an implementation soon, but if anybody has thoughts on that, and whether it's useful, and whether the functionalities that I added make sense, open to any feedback there, but…
I will, stop there.
**Jack Shirazi** 16:30 Oh, just a quick question on that one,
you've got a context propagator. Are you already publishing whether context propagation is provided by a particular library or instrumentation?
**Jay DeLuca** 16:44 No. That's what this aims. Like, we have some instrumentations that only do context propagation, and then some that do it along with other things. And so the idea was that I would… we would tag those so that, you know, if someone goes and they're thinking, oh, what is this… is this instrumentation going to generate, you know, metrics?
they have a little bit more insight. Is that what you were asking?
**Jack Shirazi** 17:07 No, no, no, I was just, I mean, I see that there's the context propagator, because you're saying that that's only for ones that don't emit spans and metrics, it just propagates context, but it's actually quite useful to know…
In general, if an instrumentation propagates context.
**Jay DeLuca** 17:23 Yeah, and it wouldn't be an exclusive list, so, like, if there's an instrumentation that does emit telemetry or do the other functions, and it does context propagation, then we could list both of those.
**Jack Shirazi** 17:32 Right, gotcha. Okay, nice.
**Jay DeLuca** 17:35 So yeah, so the idea would be to tag all the instrumentations that do that.
**Trask Stalnaker** 17:42 Yeah, I like it also. you're kind of moving from, an exclusive…
Like, pick one to, like, More descriptive, pick multiple.
**Jay DeLuca** 17:55 Yeah, sort of like tags that we can then, you know, filter and reason about the… yeah.
Cool. Thanks, everybody, for your input, appreciate it.
**Trask Stalnaker** 18:10 Alright, gregor… patch.
Question…
**GZ Gregor Zeitlinger** 18:20 Yeah, this is, a bug discovered in the SDK,
And this is in the Prometheus Exporter, and in addition, it's also in
In an exposition format, that is not the default. So by default, you get a text format or open metrics.
To be exact, and if you say that you want to have protobuf, then you get protobuf, unless you have
The era that we have now.
And women.
**Trask Stalnaker** 18:56 Was… when did the regression happen?
**GZ Gregor Zeitlinger** 19:00 And the current release.
**Trask Stalnaker** 19:01 Just in the latest release.
**GZ Gregor Zeitlinger** 19:03 Exactly.
**Trask Stalnaker** 19:06 And this is, this is coverage For regression coverage going forward.
**GZ Gregor Zeitlinger** 19:14 It is, yeah. I also have, some ideas to make this more bulletproof, because,
there is a test dependency, and if you add that, then you don't see the error. So maybe I'll make a smoke test out of it or something, but that can all be done later. Right now, I'm…
Wondering, first, if, we should do a patch release when our policy is.
**Trask Stalnaker** 19:40 Yeah, and…
**GZ Gregor Zeitlinger** 19:41 I'll receive.
**Trask Stalnaker** 19:43 is… and I'll just confirm it's the same in this repo. I know in the… I know what it is in the instrumentation repo.
Maybe we don't.
have it in this repo. Let's look in the instrumentation repo.
I know we talk about… Oh, it's under the releasing MD.
So… It definitely falls under… our qualification…
for patch release? Let's just confirm, do we have the same regression? Yeah, same language over here.
**John Watson** 20:31 So the question really is… How… we don't guarantee patch releases for regression.
Is this… significant enough.
And people who are… are people… like, if people had to wait 3 weeks for this fix.
Is it going to be…
**Trask Stalnaker** 20:52 how many people are going to be harmed? Like, if they really need to… if they need to wait a couple weeks to get the fix?
**John Watson** 20:58 Just because patch releases are kind of a pain to manage.
And someone will have to actually shepherd it through.
**GZ Gregor Zeitlinger** 21:05 Huh.
**John Watson** 21:06 So, I'm not opposed to it, but we… generally, it needs to be something that's pretty urgent and breaking…
Enough people that…
And that enough people are going to… like, have we got any reports outside of you, Gregor? I guess is the real question.
**GZ Gregor Zeitlinger** 21:23 The bug report is not from me, I just created the fix.
**John Watson** 21:28 So where was the bug report from, and do we… can we ask that person how critical it is that they get a fix immediately?
**Trask Stalnaker** 21:36 So, John, to the question about the, patch… I mean, the patch release process… Is…
I mean, it's pretty… Easy, as long as it doesn't fail.
**John Watson** 21:51 Huh,
**Trask Stalnaker** 21:53 So, and if it fails, it's because I've messed up the, automation, and I need to fix it anyways.
So, I volunteer as a, you know, I don't mind making batch releases for.
**John Watson** 22:06 So maybe… so given that, maybe it would be good just to exercise the patch release process
Just to exercise it at this point.
**Trask Stalnaker** 22:14 I'm… Not opposed to that.
**Jason Plumb** 22:16 And then are we gonna chase patches in all the dependencies, like instrumentation and elsewhere?
Yeah, sounds like yeah.
**Lauri Tulmin** 22:27 Yeah, it's not the first time we have done it.
**Jason Plumb** 22:30 No, I know.
**Lauri Tulmin** 22:31 Just as usual.
**Jason Plumb** 22:32 I just want that to be a consideration when we decide to do one, like, it's not just this one.
**Trask Stalnaker** 22:39 Yeah, I mean, my feeling is patch releases need to be simple enough that we…
**Jason Plumb** 22:45 can just…
**Trask Stalnaker** 22:46 do them…
**John Watson** 22:47 We can do them, yeah, and we aren't gonna… we aren't gonna get good at them unless we do them, so…
**Jason Plumb** 22:51 relay.
But, like, we're not gonna patch Android for Prometheus.
**John Watson** 22:56 No? You don't expose Prometheus on your Android device?
That would be a thing.
**Trask Stalnaker** 23:08 Cool. So, Gregor, why don't you just, follow up on… with Jack on getting this finished out and merged, and then, I will, kick off the back port and release… patch release.
**GZ Gregor Zeitlinger** 23:24 Okay, thanks.
**John Watson** 23:26 So that patch release will end up having a few other miscellaneous things in it.
just… Unless you're going to branch specifically off, and only cherry-pick in the one
Commit, you're gonna do that? Okay.
**Trask Stalnaker** 23:42 That's how, that is how our, patch release… Automation works.
So that's one of the reasons why…
All of our releases are off of release branches.
And so what we do is we have an automation, so once that's merged, I'll just come in here to Backboard.
pick… this, and put in the PR number.
And it'll backport it to that branch.
And then I will, go to… release, prepare, patch release.
and pick… That branch and run it, and that will, bump the patch number on that branch.
Cool. So yeah, it's pretty… it's pretty straightforward. I've… I've run them a bunch.
a decent number of times over the years. But I do continue to modify things and break things, so…
**John Watson** 24:52 Yeah, okay, cool. Well, I'll be around if you need any approvals and stuff, so…
**Trask Stalnaker** 25:00 Cool.
Patrick.
**patrickpok** 25:08 Yes, can you guys hear me?
**Trask Stalnaker** 25:10 Yeah.
**patrickpok** 25:11 Yes, so, finally, it's my first ever PR in this repo. Thank you guys for really, like, thank you guys for bringing me here, like, just for the journey, like, if not anything.
Really, thank you, Laurie, thank you, Trask, and thank you, Jay. Now more on the technical side, yes, I've written in the PR as much information as possible, so that when people come and look into it, they have enough background. Just for this group is that, as of right now, the Spark, like, Apache Spark.
For when it is consuming from Kafka, like, the traces are not being, like, propagated, continued, and I would really, like, just like to help on that. Mainly, like, following Laurie's, advice. Again, thank you, Laurie. I came up with this PR.
And just wanted to speak with the… yes, so this is, like, the problem statement. This is the manual implementation. This is what I would like to achieve, like, in the screenshot.
Which is having to consume when the producer… the producer and the consumer are seeing both the traces.
And I believe, and hopefully that, fingers crossed, this is the solution. What I would like to…
to do, like, in terms of the next step is, like, I'm going to build, like, some kind of test jar, and then run with, the end-to-end test to, to see if it is, and I'm going to publish the test result in this, in this pull request.
So if it is a negative, so it is not fixing the issue, then I'm going to go back and continue fixing the issue. And if it is, then, like, Julia, I would like to ask you guys for, like, what will be the, like, the process, because it's my first time doing this, so…
**Trask Stalnaker** 26:50 So the most important thing is gonna be to add a test here.
So it's fine to test it manually, but we will want to see a test
Here, that, shows that failed before and passes now with this.
**patrickpok** 27:13 instrumentation.
Okay.
Very clear. So, I know what to do next then.
And if you guys can just, like, eyeball through it, like, I take feedback very well, like, positive or negative, and I'm learning in the process, so it's fun. If you guys just… if you have some time, and if… just have a look at the PR while I'm building, like, the test, both, like, manually and inside, like, the code, that would be great.
Thank you guys for the help.
**Lauri Tulmin** 27:43 Hey, one thing I wanted to point out is that,
this pull request doesn't anything… hasn't anything to do with Spark, so the test doesn't also need to have anything to do with the Spark.
I believe we already have, like, Kafka tests that use the regular iterator method. You could pretty much build a new test based on those tests that use the list iterator method instead.
**patrickpok** 28:09 Yes, okay.
**Lauri Tulmin** 28:10 And that would verify that… The list iterator works.
**patrickpok** 28:16 Understood, let me do that.
**Lauri Tulmin** 28:17 And this, this really doesn't even, like,
This… if that method… like, if that test works, the pull request would be good, even if it doesn't fix anything for Spark.
**patrickpok** 28:27 Agree, I agree. So, let me work on that.
**Lauri Tulmin** 28:30 And as far as I understood, you had some problem building the HNCHR file.
**patrickpok** 28:34 Yes, yes, I reached out to the Slack channel. I think it's, like, a me problem, I don't know. I'm in JDK21, I have this great old thing, and I literally pull, like, a fresh image, like, fresh Ubuntu.
I'm just trying to build, and I'm… and I'm hitting this… like, I pasted insights, like, and I'm sorry I cannot share, but it's pretty much… I don't know… and I'm a Maven guy, so it's really hard for me.
But yeah, I'm googling, I'm asking AIs, and hopefully I will be able to fork… I mean, at least build, like, a version for myself to test it.
**Lauri Tulmin** 29:11 Well, I can't help you with that, but I.
**patrickpok** 29:13 Yeah, yeah, no, no problem, no problem.
**Lauri Tulmin** 29:15 The pull request that you made.
It, it publishes the OpenTelemetry… like, it publishes the agent char file that's built from the pull request, so if you just need the char file, you can find it from the pull request artifact.
**patrickpok** 29:30 Okay, okay, okay.
Like, can you guys show me where, so that I can, like, just download this one thing? Like, actually, that would be super helpful, so that I don't need to build it locally.
**Trask Stalnaker** 29:42 Yeah, so just go to the… did you see how I got here?
**patrickpok** 29:46 Okay, just this, like, was it from my… the PR itself?
**Trask Stalnaker** 29:52 Yeah, so I, looked at the checks.
And I grabbed any of these,
Let's go for any of these, it shows you here, and then you go up to the summary.
And then scroll to the… Bottom… Okay. And there it is.
**patrickpok** 30:13 Okay, okay, okay.
Understood. Thank you.
**Trask Stalnaker** 30:18 And just to make sure that you're doing assemble… Yes. Okay, not build, because build is going to run the tests, and that's a whole other thing that you don't want to do locally.
**patrickpok** 30:28 I made sure, like, the Java version, it's, like, 21. I even asked, like, if it is, like, a very specific 21 that you guys are expecting. I'm using the normal OpenJDK, so I think that box is checked, and then I'm doing the exact command as this one here, but unfortunately, I'm having, like, 100% of the time this error.
So, yeah, this is probably me, but at least I have a workaround, like, I will be able to test it in parallel, so thank you guys.
Great. That's it for me, and if nothing else, really, thank you for the journey. Like, it's my first ever… hopefully, it will be emerge, like, contribution to this report, and I'm quite happy about it. So, thank you, guys. That's it for me.
**Trask Stalnaker** 31:07 Awesome, thank you.
Alright, Robert.
**Robert Niedziela** 31:19 Yes, so… If you, if you could click, yeah, on, on the files.
So, basically, my question is related to, again, metrics naming.
And let's go to Hadoop YAML, for example, or Hadoop MD, that doesn't matter much.
We have the case where,
Two… there are two metric names.
Hadoop.dfscapacity and DFS capacity used. And the question is if it is okay to, yeah, basically, the metric name be a prefix for another metric.
Or we should, do it differently. I mean, add some suffix to capacity.
In first line, so there is no confusion. I haven't found any recommendations regarding this.
Hmm, but maybe… It makes sense.
**Trask Stalnaker** 32:23 Yeah, in general, we've tried to avoid that. I don't think we've exactly…
encoded that rule into semantic conventions, but it's probably worth avoiding, either just
capacity? Like, what's the… I mean, what's the difference between raw and used here?
**Robert Niedziela** 32:49 Row is total, but we cannot use total as well. And the current row capacity, actually, it's taken from Hadoop documentation as well.
So that… but then their name is different, it's just description, so maybe we could add .row suffix here.
as Sylvan recommends.
**Peter Findeisen** 33:14 In some cases, we use MAX, and this is a recommended, name for maximum capacity in this case.
**Robert Niedziela** 33:25 Makes sense, as well.
Yeah, so do we have, written… no, we don't have written this recommendation, right? And maybe it would be worth adding if it's not written anywhere.
Dude…
**Trask Stalnaker** 33:41 Is that a… yeah, is… so is total… this is a limit?
**Peter Findeisen** 33:47 Oh, limit.
**Robert Niedziela** 33:47 Wow. As well, yeah.
**Peter Findeisen** 33:49 We've seen limit.
**Robert Niedziela** 33:53 But the limit, to me, is something that you have influence on. I mean, you can configure it somehow, and you establish a limit.
For this, but this is not the case here, right? It's the maximum
Capacity, because the cluster is configured in some way.
**Trask Stalnaker** 34:15 I think Limit could still…
I mean, even if it's not configurable.
**Robert Niedziela** 34:22 okay.
**Trask Stalnaker** 34:24 Let's see, there's…
That matched way too many. Oh, general naming, here we go.
Let's see what the example is here…
Limit, measures the constant known total amount of something.
**Robert Niedziela** 34:59 Okay?
Yeah.
**Trask Stalnaker** 35:04 So, if that fits, I would go with that.
**Robert Niedziela** 35:07 It… Yeah, in the light of what you showed here, yes, it fits.
**Trask Stalnaker** 35:12 Okay, awesome.
I'll drop this link in.
**Jason Plumb** 35:17 It does read a little weird to have capacity.limit.
**Robert Niedziela** 35:23 To me, it sounds a little bit…
**Jason Plumb** 35:25 It's not the worst, but it's weird.
**Jay DeLuca** 35:28 Or should they be attributes instead of separate metrics?
**Jason Plumb** 35:34 Good question. Yeah, capacity with two different…
Attributes, one for used and one for limit or max, yeah.
**Trask Stalnaker** 35:42 It'd be Hearts Personality…
**John Watson** 35:45 Yeah, the cardinality on that would be bonkers. You don't want.
**Jason Plumb** 35:47 Yeah.
Yep.
**Trask Stalnaker** 35:54 is capacity… capacity… capacity… Yeah, I mean, I guess it…
Doesn't hurt to just kind of lean into their naming, and just kind of combine, even if they're naming with our naming, and…
Do limit there.
**Robert Niedziela** 36:16 So…
I lost that. Along with their naming means capacity.total, we cannot use, right?
**Trask Stalnaker** 36:25 Yeah, yeah.
I think this is… A decent compromise.
**Jason Plumb** 36:32 Yep, agreed.
**Robert Niedziela** 36:32 Capacity limits is okay, yeah. Okay, cool.
Thanks.
**Trask Stalnaker** 36:43 Alright, I've got a few topics,
One is the, unsafe, Java 26…
Apparently it's going to throw an error on unsafe usage.
I… don't know if it's already. I did download a 26EA, and…
Anyway, it would be nice if there was a way to… I don't know if anybody has…
Experience knows if there's a way to…
get this behavior already from the JVM, so that we could add it to our, standard…
Test matrix.
**Peter Findeisen** 37:38 As far as I noticed, this is thrown… well, the warning is emitted by, by the body.
Not directly by our code.
**Lauri Tulmin** 37:50 Yeah, but I think it's because we use whitebody in a way that brings in unsafe, which we probably shouldn't be doing.
**Trask Stalnaker** 38:00 So that would be on the Java agent side.
**John Watson** 38:05 Yeah, we use… we have a couple uses of unsafe in the SDK itself, though, right?
**Lauri Tulmin** 38:10 Yeah, but the thing…
**Jason Plumb** 38:11 Some string stuff.
**Lauri Tulmin** 38:12 I mean, in SDK, I think, the unsafe was optional.
Already, wasn't it?
**Trask Stalnaker** 38:20 for, the string stuff, it is actually…
**Lauri Tulmin** 38:24 Definitely disabled for newer versions.
**Trask Stalnaker** 38:28 Yeah, but there's… I couldn't tell the JC Tools stuff how that works.
what would happen?
**Lauri Tulmin** 38:36 I'm thinking even for that, like, there were alternative queues.
**Trask Stalnaker** 38:41 Yeah, I saw in the code, there's a fallback. I just couldn't figure out how to test it with,
to see… I wanted to say, hey, this is already done, I want to check the box.
But I don't know how, other than…
And it feels like there should be a better way than just… Eyeballing the code.
**John Watson** 39:07 I thought there was a way to enable this failure on 25, but I don't… that's just something tickling the back of my head, not… I don't remember how it would… what it would be.
**Lauri Tulmin** 39:19 I think… I'm pretty sure there is, like,
They used to have, like, switches that were, like,
Either warn, or fail completely, or don't complain.
**Trask Stalnaker** 39:32 There… I found a thing of illegal access equal deny, But that, hi, Jonathan, thank you.
But that was removed in 17. Let's see, what's this?
Any memory access method, issue a warning.
Okay…
**Jonathan Halliday (IBM)** 39:59 Scroll down, there's a section on how to identify the uses.
**Trask Stalnaker** 40:08 What are the uses. Okay.
Deny, okay.
Similar… okay, yes, so I had found this, but it was added and then removed in Java 17.
Okay, perfect.
So, if we do deny…
Okay.
Fantastic.
**Jason Plumb** 40:41 So is this a good time to revisit why we're using unsafe at all?
**Trask Stalnaker** 40:47 ES.
But the first thing I want to do is make sure it's not tested, that we have fallbacks in place.
**Lauri Tulmin** 40:57 But I'm pretty sure we don't.
And, HR25 was also released a couple of days ago.
Probably should, update our test metrics for that.
**Trask Stalnaker** 41:10 Yeah, I was waiting for…
So I had tested this in Contrib.
**Lauri Tulmin** 41:21 You were waiting for this automatic pull request?
**Trask Stalnaker** 41:23 Yeah…
**Jack Shirazi** 41:28 I mean, don't we use unsafe…
Because we're Java 8 compatible, and…
It's gonna be really hard to not use it without a lot of…
Checking which version we're running on.
**Lauri Tulmin** 41:45 Well, I think that's a… That's how it's supposed to be used, like…
That, on newer JDKs, you will need to use a different method.
But I think, like, currently, like, probably one of the issues
that we need to solve is that we want to define classes in the bootstrap loader.
And the unsafe Define class works fine for that.
**Jason Plumb** 42:15 Yeah, I'm only considering the usages in core right now. It's what I'm focused on.
It's a much bigger, much bigger can of worms to think about our use in instrumentation.
**Trask Stalnaker** 42:28 But we do, yeah.
**Jason Plumb** 42:30 Yeah.
**Trask Stalnaker** 42:31 so we should add that to… Add… to test matrix…
Try.
Cool. Yeah.
I had gone down the rabbit hole of, so your, Lori, your string optimization. I went down the rabbit hole of
Trying to convert them to VAR handle.
Only to find out at the end that var handle respects the Java module system.
And so, it won't give you access to string internals without the ad opens.
Which sucks.
**Lauri Tulmin** 43:29 Yeah.
**Trask Stalnaker** 43:35 Okay.
**Lauri Tulmin** 43:36 Like, the thing is that,
In the core repository, like,
You can't do that kind of magic, but if we wanted inside the agent, we could create.
**Trask Stalnaker** 43:49 We can add opens.
**Lauri Tulmin** 43:51 Yeah, we couldn't, like, create the necessary preconditions for this to work.
**Trask Stalnaker** 43:56 Yeah.
Good point.
So it might be worth… my, my work for supporting VAR handles might be, worthwhile, after all.
If… even if only we use it in the Java agent.
Oh yeah, this is what I… I don't know when Renovate is… Renovate's supposed to update us.
I did notice that, like, the, microsoft…
Hasn't published 25 yet…
**Lauri Tulmin** 44:45 Yeah, I think, like, I don't know which distribution we use.
Like, it's… it may be, like, the distribution we are using, hasn't published it yet.
**Jason Plumb** 44:54 Is Renovate… is Renovate Distribution Aware?
Like, it has to probably just pick one, right?
**Lauri Tulmin** 45:01 like, in the setup Java task, we are using Tamarin.
**Jason Plumb** 45:05 Yeah.
**John Watson** 45:10 What,
Are we… do we basically only run LTSs and the most recent release in the Matrix? Is that our…
Is that the goal? Okay.
**Trask Stalnaker** 45:21 Yep. That's what… that's what I was hoping.
**John Watson** 45:24 So once 25 is out, we should drop 24.
And go with 25.
**Lauri Tulmin** 45:31 For us, there was a large partner at the top of the page that said 25 in progress.
**Trask Stalnaker** 45:37 Thank you.
Pardon me.
Yep.
**John Watson** 45:45 What is the next planned LTS?
released version.
**Trask Stalnaker** 45:49 25.
**Peter Findeisen** 45:49 Until fine.
**John Watson** 45:50 25 is gonna be LTS. Oh, cool.
**Peter Findeisen** 45:52 Yes.
**Trask Stalnaker** 45:53 It's now every 4 years. They just keep changing it.
**John Watson** 45:58 I can't keep track anymore.
I mean, heck, most of Cloudera is still running Java 8, so…
**Jonathan Halliday (IBM)** 46:04 2 years, 4 releases.
**Trask Stalnaker** 46:07 2 years, 4 releases.
**Jonathan Halliday (IBM)** 46:09 Oh, yeah.
**Trask Stalnaker** 46:11 I guess that then has been consistent since 17, 21, 25.
I can math.
**Jason Plumb** 46:22 Not incredibly sustainable to do that and then leave 8 around forever.
**John Watson** 46:28 I mean, 8's not supported anymore, right? You have to.
**Jason Plumb** 46:30 It is.
**John Watson** 46:31 You have to pay…
**Jason Plumb** 46:31 By some vendors, yeah.
**John Watson** 46:33 You have to pay Oracle if you want to get 8 support, but…
**Jason Plumb** 46:35 For IBM.
**Jonathan Halliday (IBM)** 46:36 You can pay us instead if you like,
**Jason Plumb** 46:38 Yeah, exactly.
**John Watson** 46:39 OpenJDK doesn't support it, though.
**Jason Plumb** 46:42 No.
**Trask Stalnaker** 46:48 Alright, next, while we're talking… Java, internals.
There is a spec PR, out to,
Make the disabled config, so this is, Right now… We have…
Let me show you the code we have today… in SDK logger…
So this enabled flag that we can update via…
op-amp. The goal is to be able to update that dynamically at runtime.
We intentionally didn't make it volatile,
So that it doesn't trigger volatile reads on access.
And just saying, hey, you know.
It will probably eventually be visible to other threads.
This, spec PR language I think…
Means that we would need to change that.
I played around with various
Options of trying to, like, only do a volatile read, like, every hundred accesses, but…
Even that the low… writing to a local counter, non-volatile counter, just…
Was the overwhelming performance bottleneck there, so that didn't work out at all.
**Jack Shirazi** 48:38 I… I don't understand. Eventually consistent means eventually that could be… Just before the…
the JVM terminates, or just after the JVM terminates, I mean, it's… That… that's… that's nonsense language.
**Trask Stalnaker** 48:58 So, that is a good question, what does eventually mean? Does eventually mean after restart?
That's… that is eventually.
**Jason Plumb** 49:07 Just before the heat death of the universe?
**John Watson** 49:12 I mean, the Java memory model doesn't guarantee, if it's non-volatile, it'll ever be done, though, right?
**Jason Plumb** 49:18 Exactly.
**Trask Stalnaker** 49:19 Until after restarting the JVM.
**John Watson** 49:21 Yes, yes. Although, I mean, in practice.
Unless you're in a very unusual situation, it gets synchronized pretty quickly.
Like, in practice, it generally will get synchronized across threads, even if you don't… even if it's non-volatile, but there's no guarantee.
**Jason Plumb** 49:41 So I think the way to think about this…
the way I think about this is that the volatile hit, or a lock, is going to be considerably less expensive than the string concatenation.
Or the string template building for a logging statement. Like, that's the whole reason that exists, right? Is to be able to not build strings.
And so, I think relative to that, you know, taking the volatile hit seems like it's probably fine.
I understand the instinct not to want to.
**Trask Stalnaker** 50:14 So I did some research, where did I post?
what I posted here. I looked at both Log4J and LogBack.
And log back was not doing a volatile check. A volatile read, log for J2 is doing a volatile read.
So… It may not be… The worst?
I did do some benchmarking, and I'll… I'll push… Benchmark.
Cool. At some point.
**Jason Plumb** 50:54 Yeah, that's good.
**Trask Stalnaker** 50:56 The only way I could get it to really kind of show up.
**Jason Plumb** 50:59 Was even just volatile versus non-volatile.
**Trask Stalnaker** 51:03 was, looping. Like, because for non-volatile in a loop.
It can just… it only… it doesn't have to access memory each time. It can cache that, whereas with the volatile inside of that loop, it has to actually physically check memory every time.
**Jason Plumb** 51:28 Yep.
**Jack Shirazi** 51:31 Every time one of these things come up, my answer's exactly the same. Any app that… for which it matters is not using OpenTelemetry.
**Trask Stalnaker** 51:41 Fair.
**John Watson** 51:43 Yeah, that's kind of where I was headed, too. Like, it's only gonna be… it's only going to really matter under extremely high… high throughput situations, right?
And they're probably not using OpenTelemetry anyway.
**Trask Stalnaker** 52:01 Alright, my last topic, is complex attributes are coming.
And so, I threw out a couple of… Options…
And… or adding… for bringing them into the Java SDK.
And just wanted to share briefly, I kind of put in here the,
Pros, cons for both of these two.
But you can kind of see, so…
We would be adding byte array support.
Value array, which is basically a heterogeneous array.
So before, we only had,
homogenous arrays, so long array, string array, but now we would support
These… these are kind of useless, in my personal opinion, but it's part of the spec, so we would support it.
And maps. So this is the big one, nested maps.
Trust Corvet.
**Jason Plumb** 53:21 Value array… value array is an array of objects, or an array of other attributes, is that…
**Trask Stalnaker** 53:26 It's an array of any value.
**Jason Plumb** 53:28 Okay, perfect.
**Trask Stalnaker** 53:30 So in this, Product in this, idea.
We would reuse the value. We already have an AnyValue object in the SDK for body value.
So we would reuse this.
**Jason Plumb** 53:52 Yep.
**Trask Stalnaker** 53:53 Which… So the… the downside, the value…
Is… is not terribly performant.
Because it ends up… we end up wrapping everything, extra.
Versus our attributes.
is highly optimized.
But… That doesn't really bother me for the value array, just because that's a pretty limited use case.
**John Watson** 54:23 Yeah, my… I mean, I understand we need to support this because the spec says we need to support this, but…
like, I don't think we should try to optimize these cases at all. Like, is any instrumentation… is any… are any semantic conventions gonna use this nonsense?
**Trask Stalnaker** 54:40 This nonsense, or this?
**John Watson** 54:43 Either.
**Jason Plumb** 54:45 Yeah, definitely.
**Trask Stalnaker** 54:46 Ultimately, they're gonna use this.
**Jason Plumb** 54:48 Yes, absolutely.
**John Watson** 54:50 Well, that's a shame.
Only because, you know, the open source backends aren't going to do anything with that data, right? It's just going to get in a JSON array or something, JSON object.
**Jason Plumb** 55:05 Yep.
**John Watson** 55:06 And it's not gonna be useful
in that way, to anything except just being able to see a bunch of… a blob of stuff in your UI?
**Jason Plumb** 55:15 I'm not equal yet.
**Trask Stalnaker** 55:17 Yeah, not yet.
**Jason Plumb** 55:22 That's a good point.
**John Watson** 55:23 I mean, the heat death of the universe did come up earlier, right? So…
**Trask Stalnaker** 55:29 So in this one, because we see… because this one is going to be used by semantic conventions.
We have the option of taking our attributes map and basically just nesting it in itself.
And so the benefits are… it's a… we already… people are already familiar with that API.
And it's already optimized.
The potential downside there is it kind of mixes this concept of attributes and nested maps.
So, like, it can… some people have argued in spec language for, like, these are kind of different. You have attributes that go on your spans, metrics, logs.
And then you have, kind of, these nested maps.
So, not sure how I'm… I mean, I think we can make our own call in Java.
And then this other one is kind of leaning into the… Just using…
Not using nested attributes, but… This is how our…
existing value API expresses maps as a list of key-value pairs.
So this is already built into the value.
object, it's… again, the downside here is…
The… probably not as performant, maybe we could… Deal with that.
I think maps having this list of key values is a little confusing, but… It's… manageable.
So… Yeah, any… we've got only 3 minutes left,
So, mostly wanted to share, But any immediate… Thoughts would be welcome.
**Jason Plumb** 57:58 Nothing immediate, but I'll try and take a look.
**Trask Stalnaker** 58:07 Cool. And then, Gregor, FYI, smoke tests…
Yay! Our final groovy… this is our final groovy remnant, right? Other than the tests, we actually have some Groovy that actually tests Groovy, so those will remain kind of like.
**Lauri Tulmin** 58:26 I think we might still have some Groovy tests in.
**Jay DeLuca** 58:30 Cooling?
**Lauri Tulmin** 58:31 Yeah.
Some crew we test that are not the instrumentation tests.
**GZ Gregor Zeitlinger** 58:36 Some muzzle tests, I think. There's a groovy test hiding.
**Trask Stalnaker** 58:44 Yeah, we went groovy crazy.
Alright, folks!
We are past our cutoff, so… Enjoy… And see you next time.
**Peter Findeisen** 59:03 time.
