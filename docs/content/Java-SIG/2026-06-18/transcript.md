SIG: Java SIG
Date: 2026-06-18
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 03:48 Good day, y'all.
**Jay DeLuca** 03:52 Blue.
**Gregor Zeitlinger** 03:54 Oh.
**Jason Plumb** 03:55 Nape.
**Trask Stalnaker** 05:45 Sorry, just populating… some… Stuff in the agenda here. Please go ahead if you have anything else to add.
Alright, let's… kick it off. So, okay, so… Yes, still no 2.29 release.
The, I would… let's see, so the… Finalizing the database semantic convention stability work, Okay, the last thing that I was… Working on was looking over all the Handling… how we handle batches.
Across all the different database instrumentations.
And… improving the test coverage there, and… Ran into a couple of edge cases that, actually ended up, Opening a… Semantic invention… clarification, PR… Let's see here… two things here that, oh, I guess I commented them here.
One part here is, what is a batch operation?
It was actually in, like, when you're thinking SQL, it's obvious.
But in some cases, it's not so obvious, like, is a multi-get… Operation a batch or not.
So… tried to clarify that.
And then the other clarification is a weird… degenerate case of… a lot of APIs, actually, you can send batches of zero elements.
And that was… not… Clear how to handle that.
So, what resulted was this massive, PR here, with all these test… tests across all the different, database instrumentations and, that have batch coverage.
So, this is actually passing, but is not reviewable, because it's… too enormous. So, I just finished, got this passing this morning, and just started the work of extracting out PRs that can be actually reviewed.
The… One that, would be the most… helpful is this one. Let me bold it.
Cause this is… kind of the core behavioral change in the instrumentation API incubator package.
Of changing how the batch zero is handled, and a little bit of… about, how batches are handled for this case where there's a single… we have one case, Cassandra, where It actually is a query, but it does guarantee you can only have a single operation name or a single collection name in a given query, and so there's some other rules around that.
So this, all the other stuff then, I will stack on top of this, but if, we can get this reviewed… And then I can merge that and not need to stack quite so much.
So I should be able to get all of… I think it shouldn't be that hard, it's kind of mechanical at this point to extract things into reviewable PRs.
And honestly, most of those are test… most of it's test coverage.
There are a couple of… places where There's one place where I decided what I had added some batch instrumentation for.
Shouldn't be considered a batch.
And then there's some new batch coverage for, like, Redis and some Redis variants that I hadn't instrumented for batching before.
So I should have all of those PRs up and reviewable by end of today, and then, so I think probably should give a couple days there for review, and then… Hopefully we can get out the release on… Monday or Tuesday of next week.
**Lauri** 11:40 I can already say that it's… Most likely going to turn out to be Monday or Tuesday, the week of the next week.
**Trask Stalnaker** 11:51 Just in terms of the reviewing the complexity of the reviews.
**Lauri** 11:56 Well, I won't be available for reviews, I think.
**Trask Stalnaker** 12:00 Oh, okay.
**Lauri** 12:01 big.
**Trask Stalnaker** 12:02 Okay.
Is anybody else available for reviews, or do we… I'm actually out the week after next.
So… Yeah, it's…
**Gregor Zeitlinger** 12:22 Ask me for reviews.
**Trask Stalnaker** 12:26 Okay.
And, Laurie, do… If you have a chance just to kind of get a sense of whether you are good with the general direction.
Or not, if… if the… if you think… if you have some concerns… Then… probably, we can just cut the release… I could just cut the release tomorrow with what we have.
And… This stuff can land in the next release.
**Lauri** 12:58 I'm sure you… whatever you came up with makes sense.
But nevertheless, like, it might… Makes more sense to just cut the release, because… We have already slipped for a week, and And cutting these into the release probably isn't all that important.
**Gregor Zeitlinger** 13:20 So, is the next one 3.0, or are we extending by one?
**Trask Stalnaker** 13:27 Well, that would be the difference, because, so I… what I… I realized that we can't… the reason I was pushing to get all the database stuff into… all the database stuff needs to be into the release before 3.0, whatever that is.
Because of the way we have the stability opt-in flag, Where people on… We're gonna drop the duplicate emission in 3.0.
And so people who want to be able to migrate do the whole duplicate, emit both old and new SEMCOM at the same time.
the final 2.X release.
Needs to be fully database.
Ready.
**Gregor Zeitlinger** 14:17 So we're targeting in 2 months for 3.0, basically.
**Trask Stalnaker** 14:23 That would be the difference if we do cut the release tomorrow.
Without this, then yes, we would need to push it.
Or…
**Lauri** 14:34 If we want, we can do, like, another 2X release whenever this thing is ready.
We don't have to follow the schedule, I think.
If we want.
**Trask Stalnaker** 14:48 That's true also.
**Gregor Zeitlinger** 14:54 I would make it dependent on how many tasks are left. I checked this week, and there are still a couple tasks, so in 2 months.
does not feel too early, but, I mean, we can check the board now.
**Trask Stalnaker** 15:10 Yeah, let's check the board. I thought I… I thought, we had wrapped up everything that we… could… Except for this one, which is what those are depending on ignoring the… I mean, I think the invoke dynamic stuff is, Most likely going to slip out of 3.0.
And… the other… oops.
The other ones, we can't… my understanding is we can't do… Prior to 3-0 anyways, these three?
**Gregor Zeitlinger** 15:48 That's right, yeah, that's right. Okay, if invoke dynamic is out of the picture, then, yeah, I think having an in-between release is a good idea.
**Lauri** 15:57 Actually, I think most of the hook dynamic is, like, quite ready, Daryl, and the API promotions… Most of them aren't really important, also.
**Trask Stalnaker** 16:13 Okay, I haven't been… I mean, I guess… Somebody needs to drive that.
**Lauri** 16:21 Yeah, the big problem is that there isn't anybody who's driving it, I think.
There is, like, there's this, pull request that removes this, getModuleGroup method.
Which… I guess it isn't important, but it sort of is, because, like, currently.
All, like, all the instrumentations are isolated from each other.
the way this PR solves it is it… It, It basically makes so that, on the agent side, all the instrumentations also share a class loader.
Which makes it kind of similar to our… Existing injecting instrumentation that That instrumentations can share code.
But the problem is, like, like… But, for extensions.
it still… it uses a different class loader. Like, I guess it's a decision point, like, do we want to isolate all the classes, or do we want to share them?
Like, the sharing makes, maybe makes some things more simple, like, if somebody wants to extend our instrumentations, then, They at least have a chance for doing it.
**Trask Stalnaker** 17:50 Let me pull up that PR here.
So I guess the, So is there… there's a decision here that you're saying that we need to make?
**Lauri** 18:36 Well, yeah, the instance, like, Oh, we want those instrumentations to behave, like, like… Previously, all the helper classes were injected into the application class loader, so they were, like, implicitly shared.
But now, when each of the… Instrumentation released in a separate class loader. We currently use this getModuleGroup hack to force them into the same group.
What this pull request does is that it basically places all the instrumentations into a single group.
With the exception of, Of extensions.
It's basically, like, the extension's handled, separately because, For extensions, the parent class loader of the instrumentation class loader will be the extension class loader, otherwise it will be the agent class loader.
**Trask Stalnaker** 19:34 Hmm.
**Lauri** 19:34 But probably that one also could be circumvented. We could, like, consider setting the parent class loader to… To the class loader that can see all the extensions.
Of course, Ken, then the question would be, like.
That, what if the extensions, like, contain classes with the same name, but I think, we currently don't handle that anyway.
**Trask Stalnaker** 20:03 So this is, this is moving in the direction that… Already of… Sharing across everything, so it's only the… whether the extensions… Is that the only decision point at this point, or…
**Lauri** 20:22 Yeah, like, also the question, like, whether we want to share, like, everything. Another option would be to share nothing, and write the instrumentations in a way, like, when they need to share, then they explicitly have to… Place a class in… class somewhere that both instrumentations can share.
Perhaps into the agent class loader somehow.
**Trask Stalnaker** 20:50 I guess what would… we need somebody who can, like, write up, sort of, you know, pros, cons to… Those different decision points.
**Lauri** 21:02 I guess, like, the major colony is that… That, you can move from, like, a more restrictive approach to a more lax approach, but moving vice versa would be… Again, like, breaking change.
**Trask Stalnaker** 21:31 We… our current, I mean, the non-Indy Approach is shared everything already.
**Lauri** 21:39 Yes.
**Trask Stalnaker** 21:45 So what, what do we think the advantage to, isolating… is…
**Lauri** 21:58 Well, it could be that if you have, like, some sort of conflicting instrumentations that contain classes with the same name, or stuff like that.
Then maybe that would help, or…
**Trask Stalnaker** 22:13 I feel like the distra, like, not so much a problem for distros, I would expect distros to… handle that.
Themselves via shading or whatever, it's a whole package, the conflicts they can work out.
It seems like the only… the advantage to isolation would be more around extensions, People…
**Lauri** 22:40 Well, I guess one question is also, like, If you, like, share things, then, For extension authors, it might be possible to, like, write extensions that take advantage of existing instrumentations, like, they could write an extension that somehow relies on the native instrumentation, but if we don't share the things.
Then, this might be tricky.
**Jack Shirazi** 23:10 But if they do that, that it's relying on internal… Implementation that's not stable.
And that's also… Tricky.
**Trask Stalnaker** 23:34 So with the, Yeah, with the extensions, I guess one nice thing with it being isolated is, like, if you wanted to replace, like, in an extension that… Copied.
the… neti… Was a duplicate.
I mean, ideally, an extension should shade that and have their own package names anyways.
But… Yeah, I mean, that… it's a good point about, ideally, the extensions.
should only… be interacting with our public APIs.
I mean, I guess we could potentially, in the future, declare some Java agent instrumentation APIs to be public, sort of.
Extensible.
**Lauri** 24:33 Well, I don't know if that's, like, even, like, real concern for now, like… But the people are actually, like, taking advantage of stuff like that.
**Trask Stalnaker** 24:47 So, I mean, this doesn't seem like a… I mean, this seems like a reasonable… Option… To share everything in the… Distro, but have the extension… be isolated.
I don't have real strong opinions here, if you have anything that you would prefer.
**Lauri** 25:19 I need to think a bit more about this.
**Trask Stalnaker** 25:26 Okay.
**Lauri** 25:29 That's for other stuff that's… That, like, There are a couple of promotions.
our basic… This should be easy to handle, and even if you don't promote them, well, we could do this later.
**Trask Stalnaker** 25:50 I see, so these are just pretty straightforward…
**Lauri** 25:54 The injected… injected class names is, is easy, and the JPMS module's still open. We probably don't want to do that at all, at least First, because… They're only, like, a couple of instrumentations that rely on it.
And if this really turns out to be an issue, then I guess it could be solved in some complaint-driven way.
I think even for existing instrumentations, it is, like, something that… Like, nobody has asked for it this far, so it can't be that important.
**Trask Stalnaker** 26:33 So, it would… if we… Did these things… would we… are we… good to enable it by default, make it the default in 3.0.
**Lauri** 26:46 I think so, but, like… Another big part, probably there, will be documentation.
And I don't know who's going to do that.
**Trask Stalnaker** 27:06 There was… I mean, I thought that a bunch of the docs were… Updated already that there was a good amount of doc about the invoke dynamic?
Let's see if I'm misremembering…
**Jack Shirazi** 27:25 Yeah, they… they… There should be quite a bit.
But we can… We can commit to doing documentation.
If there's more needed.
**Trask Stalnaker** 27:42 Trying to see what… Okay, yeah, so…
**Lauri** 27:56 first thing that would need to happen is that, I think.
all the mentions of Indy would need to go away.
And some other kind of terminology would need to be invented.
Either, like, inlining and non-inlining.
**Trask Stalnaker** 28:21 Cool, so it sounds like the main kind of sticky point is… What to do with this one.
Is that… Fair, Laurie.
**Lauri** 28:35 Well, this is, like, one step.
like, we could leave it as it is and keep using Ticket Module Group, but ideally, we… We would… Have some sort of, like, an idea how these instrumentation should be worked, and how would they behave for the users?
**Trask Stalnaker** 28:57 I mean, I like the… I like the idea of removing it, only from the perspective of it has been… Right, it's, it has been confusing, like, when you're… working with instrumentations, and there are cross-module dependencies, it's a non-obvious solution.
That if we just don't need that, then… That simplifies things.
**Lauri** 29:32 Yeah, I think it thinks so, too, that it just simplifies things.
Although, like, one issue is that, like, If you have instrumentations that, that are different libraries.
For all the sharing to work, it kind of assumes that these instrumentations are in the same class loader.
Which, is a… is an assumption that isn't necessarily true.
But we have the same issue with our injecting instrumentations anyway.
**Trask Stalnaker** 30:16 Yeah, yeah.
**Lauri** 30:18 There are ways to work on it, and probably, like, with Indy, there are better ways to do it than with the injecting instrumentation.
But it's… It's something that, again, like.
If users are not complaining, then maybe we can pretend that it isn't a real issue.
**Trask Stalnaker** 30:42 That's what we've done so far.
**Lauri** 30:44 Yeah.
**Trask Stalnaker** 30:45 Complaint-driven, yeah, I mean, we've had some of those with Spring being loaded in different class loaders.
**Lauri** 30:52 Luckily, OSGI isn't that popular.
**Trask Stalnaker** 31:01 Okay, so, Sylvain, hopefully you're listening to this.
or reading, reading the transcript. Maybe I'll, summarize the transcript, for him, and because I know he was asking in Slack.
Sort of about this topic anyways, so… Cool, alright, so hope's alive for Indy making it to 3-0.
That's That's cool. I think that would be, you know, great. It was a lot of work to come together for that, so it would be really nice to be able to enable that in 3.0.
I will… ponder… maybe I'll make a decision, tomorrow about… tomorrow morning about whether to cut the release, depending on how the… my last set of, database PRs look, and if, after… hopefully I get them in and good today, and Gregor has a chance to look at them.
Tomorrow.
Alright, anything else about… 2.29 or 3.0.
Before we move on to the blog post about 3.0.
**Lauri** 32:46 I have one thing that… This may be, like, a bit related to 3.0.
I was thinking, like, whether we could improve our integration with micrometer somehow.
But currently, we are disabling the micrometer and Spring Boot Actuator instrumentations by default.
I guess one of the reasons was that they emit metrics with the same name as we do.
**Gregor Zeitlinger** 33:23 Not only same name, also sometimes a different name, but for the same thing.
**Lauri** 33:29 I think the metrics with the same name were, like, more annoying, because it started spamming with warnings, and it was unclear, like, what was going on with it.
**Gregor Zeitlinger** 33:39 But both are at least confusing if you look at the output Of a single application.
At least this is what motivated me initially to disable it by default.
And of course, that it's creating costs that is quite unnecessary.
**Lauri** 34:08 But nevertheless, they have, like, some more metrics than we do.
**Gregor Zeitlinger** 34:14 Yes, and that's a very good point.
**Lauri** 34:16 I think, like, maybe we shouldn't, like, concentrate on, like, that much on enabling it by default, but just making, like, enabling it less painful.
like, what would the user need to do, like, for now? Like, would they need to, like, somehow write declarative configuration to drop the… Micrometer metrics that they don't want.
**Gregor Zeitlinger** 34:41 I think so, yes.
That would be necessary.
And it's quite complicated.
**Lauri** 34:48 could we improve the situation somehow? Like, I don't know.
Maybe by default, like, by default excluding some metrics, like, Micrometer has this, meter filter function that, Basically, you can add a meter filter to the metrics registry that will either rename the metrics or exclude some of them.
**Gregor Zeitlinger** 35:13 Yeah, that's possible. I've done that already for the Grafana distribution.
**Trask Stalnaker** 35:22 Laurie, do you, or to anyone, do you know what metrics, are useful, like, what metrics people want out of micrometer, that they're getting out of Micrometer.
Because we do have the JMX metrics now that… make, like, I mean, those were some of the key metrics at… that I know we were missing before, like the Tomcat Jetty, metrics… What else? Because that's another option.
We could look at improving our default set of, or our metric offerings.
**Lauri** 36:06 That is definitely an option.
**Gregor Zeitlinger** 36:10 It's been a while that I've taken a close look, so it's not fresh, but I remember that when I did look, it had some useful metrics around database pools, and I don't know if we are on par in that area yet.
**Trask Stalnaker** 36:35 I think that's the… that would be the first thing I would, you know, I would like to see if somebody wants to tackle this, is… Sort of, what's the list of, metrics?
Coming from micrometer that are useful, that people are looking for.
And seeing if we can… add those… enhance our… the JMX metrics, for example, to include those.
If it's kind of… If it's… if that's not the issue, if there's sort of… Well, a lot of people have I mean, certainly enabling micrometer should be simpler. Like, a lot of users have instrumented their applications with micrometer.
And it should be easy for us.
To let people enable that, the bridging for that.
So it's more the… Enabling micrometer, I think, is… should be easier. It's the spring actuator stuff that is more… overlapping, right? That's the actual… Code that's emitting telemetry.
**Lauri** 37:58 There is also, like, the JVM metrics that are built into the micrometer. In fact, those have the same names that are metrics.
**Trask Stalnaker** 38:08 I thought those… came from Spring Actuator. Like, I didn't… I thought micrometer was just pure SDK.
**Jay DeLuca** 38:19 They have…
**Lauri** 38:20 have some metrics.
**Jay DeLuca** 38:22 Yeah, they have, like, libraries for… you have to enable it, it's not by default, so if you just use micrometer to instrument your application and don't turn that on.
You won't get those.
**Trask Stalnaker** 38:32 Oh, okay, okay.
**Lauri** 38:36 Probably the actuator just turns them on.
**Trask Stalnaker** 38:39 Yeah.
Makes sense.
**Lauri** 38:43 I don't know, like, exactly, like, what metrics people are missing, but we have had, like, a couple of issues where people are asking, like, why aren't… why don't I get some metrics? Or, like, they expect to get some metrics, like, I haven't figured out, like, why they expect them, like, maybe they previously used micrometer, and…
**Gregor Zeitlinger** 39:07 Yeah, I think mostly because they… they don't technically know the difference.
**Lauri** 39:14 Yeah, because, like, actually… We don't have, like.
we have, like, quite a few metrics that we emit by default, like the JVM ones and the HTTP ones, I guess.
That's pretty much it.
Okay, maybe the connection pool ones also.
**Trask Stalnaker** 39:36 Yeah, I wonder if we should consider, at some point, enabling some of those JMX metric Modules by default.
**Lauri** 39:46 Well, as Gregor pointed out, that's a double-edged sport, because Because of the cost concerns.
**Trask Stalnaker** 40:00 So, did we… is this off?
By default, default enabled… Okay, so into… Oh, we had already turned that off, okay.
**Gregor Zeitlinger** 40:21 We also, have to… Answer if we want to, Rename the metrics if we are Enabling them selectively.
Not… typographic.
**Trask Stalnaker** 40:43 Like, and then, like, having, like, a prefix for the micrometer metric?
**Gregor Zeitlinger** 40:49 No, not a prefix, if we want to mangle them to conform to semantic conventions, if available.
**Trask Stalnaker** 40:57 I don't think so. I think for bridging, when we're bridging from other systems, it's pretty… it gets gnarly trying to do that. We've kind of gone down that path before with, like, Kafka and other metrics, and… I think we've landed in the past on just bridges should just be bridges and straight mappings.
**Gregor Zeitlinger** 41:23 Okay.
**Trask Stalnaker** 41:33 Okay, Jay, tell us about… blog post?
**Jay DeLuca** 41:39 So…
**Trask Stalnaker** 41:40 ideas.
**Jay DeLuca** 41:42 Yeah, I was thinking of, getting something out just to cover, kind of, the 3.0 release, and… Give, users some ideas of what impact it might have on, like, their queries, as well as to potentially pitch some stuff, so, like, we can… although declarative configuration is not being out by default, like, if people are… Going through this upgrade, maybe it's a good chance for them to try it out, So yeah, so I have, some of the high-level stuff here, but I wanted to see if, like, I cover the database, stuff, the… Code, semantic conventions, some of the RPC… Values changed, things like that, just so people kind of have a… A centralized changelog, And then, also just, giving some people some information on how they can do the duplicate, emitting, so that they can try it out ahead of time.
So yeah, I just wanted to see if anybody else had any other ideas of things that might be useful to include.
**Gregor Zeitlinger** 42:53 I have more question, The Spring Boot Starter also supports declarative configuration for a couple releases now, and I'm wondering if that is something for a dedicated blog post, or if it naturally belongs here.
Because… Of the timing.
Mainly.
**Jay DeLuca** 43:17 I don't know that I would include it here. I think this should be more scoped to just the primary differences in the release. We could certainly call it out as, like, a in the declarative configuration spot, but I think that would probably be better to have a separate Post 4.
That's my opinion, anyway.
**Jack Shirazi** 43:38 Yeah, I've got a question, also.
given that the CENCOMF changes… not declared… the CENCOMF changes are… Technically not breaking, because they're going from experimental to stable, so a name change on an experimental is technically not a breaking change.
**Trask Stalnaker** 44:00 No, they are… they are breaking. It's only acceptable because we are doing a major version bump in the Java agent.
**Jack Shirazi** 44:11 But they're going from experimental to… to… to something non-experimental. Isn't that technically not a breaking change?
**Trask Stalnaker** 44:20 So, we've, we tried to argue that at one point.
But the… Experimental ones are so widely adopted that we ended up calling them de facto stable.
**Jack Shirazi** 44:36 Okay.
**Trask Stalnaker** 44:37 Colloquially.
**Jack Shirazi** 44:39 Okay, let me rephrase my question. Are there any braking changes apart from the SEMCOMF changes?
**Trask Stalnaker** 44:46 Oh god, I'm… I'm not looking forward to writing the, release notes for 3.0. There are… gonna be a lot of… I'm sure there's gonna be a laundry list.
You can look right now, basically, if you search the codebase for everything hidden behind the V3 preview flag.
Those are essentially all breaking changes that we could not make yet, until doing a major version bump. So, essentially, that's our list. That's gonna be my list of breaking changes in 3.0, is… I'm gonna strip out all of those V3 preview flags.
And enable all of those things by default, and… Include those in the release notes as breaking changes.
**Jack Shirazi** 45:39 Cool, that's useful.
**Gregor Zeitlinger** 45:41 And on top, we have a common comment pattern for things that will be changed. There's an issue for it, so you can look for this comment pattern as well.
**Trask Stalnaker** 46:05 Yeah, this guy.
**Gregor Zeitlinger** 46:07 Right.
**Trask Stalnaker** 46:24 Yeah, definitely.
We should do a blog post.
**Jay DeLuca** 46:34 Maybe when, maybe when you start working on that changelog, I can come back and… refresh it with what else, in case other things I missed. It probably doesn't make sense to include everything, but we can point it to the changelog and just highlight the… The important parts that we think people will need to take action on.
**Jason Plumb** 46:55 Jay, is your intent to drop this before the release, or, like, right around the time of the release?
**Jay DeLuca** 47:01 I was… I don't know. I…
**Jason Plumb** 47:04 Okay.
**Jay DeLuca** 47:04 I guess it depends on how quickly we can get everything in order.
**Jason Plumb** 47:08 Yeah.
**Jay DeLuca** 47:09 are confident about the 3.0, and then there's also the… the OpenTelemetry I.O. blog backlog is a little tricky, too, so I'm gonna need to coordinate That as well, but I was thinking a close… close to release, if not sooner, but… Yeah, it's subject to change.
**Jason Plumb** 47:29 Cool.
**Trask Stalnaker** 47:36 Yeah, that's an interesting idea, since we have doing it… I would have assumed doing it with the release.
But… Especially since we have the V3 preview flag.
It's kind of an interesting idea to… promote that.
As a way for people to… Get a sense ahead of time.
Maybe a, maybe a… Quickie, I don't know how the blog posts… Backlog works with, like.
Or if they even want, like, short things.
like, how do we advertise that there's the V3? I think with the… whatever release is right before V3, It makes sense to try to… to have some kind of push of, like, letting people know that the next release is gonna be V3, you can try it out now with the V3 preview.
Even if it's just social media.
**Jay DeLuca** 48:43 Yeah, it's a good idea. I can, once we figure that out, the cadence of what we think will be the next one before that, I can help Put something together and get that out quicker, and then… We can save the longer, more in-depth post for, when we actually are there, ready for the release.
**Gregor Zeitlinger** 49:01 But why wait? I mean, we can drop a message in the Slack channel right now.
**Jay DeLuca** 49:09 We don't know.
**Trask Stalnaker** 49:09 Bye.
there's still… Breaking changes coming.
**Gregor Zeitlinger** 49:16 Yeah, but we already have quite a lot of things. We can say that we have most of the stuff, but maybe there is more coming, and then we can update the… Thread.
Or is there substantial things that are not yet covered in the preview flag?
**Trask Stalnaker** 49:36 No, but just sort of more like a… Like, it's one… Trying to make one push.
That is like, hey, this is the final release, you know, the final release is out before 3.0.
you can try it now. This is essentially, like, we could almost even consider it a release candidate for 3.0 with the V3 preview flag.
**Gregor Zeitlinger** 50:04 Yes, I understand that, but right now it's summertime, people may be on vacation, so if we say it a little bit earlier, then maybe they have a chance to actually take a look.
**Jay DeLuca** 50:17 Right, that's the idea. As soon as we figure out what the… 3-0, like, if it's Monday, then I'll start working on it to get it out.
You know, that week, hopefully.
But we just gotta figure out, like, what… whether it's gonna be this month or next month, essentially.
**Gregor Zeitlinger** 50:33 Okay, so as long as we still have, like, months ahead for people to read it, then I think it's good.
**Trask Stalnaker** 50:39 Yeah, yeah.
All right.
**Jay DeLuca** 50:47 Damn.
**Trask Stalnaker** 50:48 Any… anything else?
About releases, or any other topics.
**Jack Shirazi** 51:02 Yeah, I just had a quick look at the search for V3 underscore preview. There isn't that much.
Oh, I use V3 underscore preview, okay.
**Trask Stalnaker** 51:28 So, I think what you want to look for is… I think most of it calls SEMCOM Stability V3 Preview.
So, V3 preview… Yeah, this'll get you a better list.
I think.
**Jack Shirazi** 51:51 Thanks.
**Trask Stalnaker** 51:52 Yeah.
Even…
**Jason Plumb** 52:11 The width span constructor thing is breaking. That's one that I… know of.
Right. I mean, probably no one's using it.
**Trask Stalnaker** 52:22 I think that actually turned out to be non-breaking.
**Jason Plumb** 52:24 Really?
**Trask Stalnaker** 52:26 Because I think I discovered that it never worked.
**Jason Plumb** 52:29 Sick.
**Trask Stalnaker** 52:33 Yeah, let's see the history there… with… Span… .
**Jason Plumb** 52:47 Constructured that third one? No, that's document.
**Trask Stalnaker** 52:50 Yes, yeah.
But this was the idea. Turns out constructors aren't supported by… with the mid-span instrumentation anyways. So, yeah, we were able to resolve that in a non-breaking way.
Thanks, by the way.
**Jason Plumb** 53:06 I must be breaking. Yeah. Okay.
**Trask Stalnaker** 53:13 Love, love when a bug, goes in your favor.
**Jason Plumb** 53:20 Yup.
**Trask Stalnaker** 53:25 Alright, folks.
Yeah, I will, I will try to post… I'll keep the, since there's a broad group here interested in the 3-0 schedule. I'll post in the general Java Slack channel tomorrow.
With an update.
Sounds great. Thanks, all!
Bye.
**Jay DeLuca** 53:53 loader.
**Gregor Zeitlinger** 53:54 So you're…
