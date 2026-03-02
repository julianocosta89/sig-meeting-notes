SIG: Java SIG
Date: 2025-07-03
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:01 You have a meeting? No sled.
Hi, Julie!
Hello!
**Jean Bisutti** 01:53 Hello! Everyone.
**GZ Gregor Zeitlinger** 02:00 So Trust said he's out.
let's see.
Wants to take over.
Maybe Laurie.
**Jack Shirazi** 02:26 Thank you for volunteering. Gregor.
**GZ Gregor Zeitlinger** 02:29 I can also do it. Sure
trust does have an agenda item. So maybe.
if not, consider that I'll bump it.
**Jack Berg** 03:29 Has anyone heard from trust?
**GZ Gregor Zeitlinger** 03:31 He said. He's on vacation this week.
Hi, Jack!
**Jack Berg** 03:35 Hello!
**GZ Gregor Zeitlinger** 03:37 You're also on vacation, isn't it?
**Jack Berg** 03:39 Not yet. If you're talking about my parental leave, and I don't know not really a vacation.
**GZ Gregor Zeitlinger** 03:47 I know what you're talking about.
**Jack Berg** 03:51 I have more anxiety about it than I have about work.
**GZ Gregor Zeitlinger** 03:56 I think congratulations are in order. Nevertheless.
**Jack Berg** 04:00 Yeah, definitely, thanks.
**GZ Gregor Zeitlinger** 04:02 Is it your first.st
**Jack Berg** 04:05 No, it's my 3.rd
**GZ Gregor Zeitlinger** 04:08 But you're still anxious.
**Jack Berg** 04:10 I'm still anxious.
I'm anxious about the sleepless nights like sleeping in 1 h increments for like 2 months. I just, I'm gonna I'm gonna feel awful, and I'm not looking forward to it.
**GZ Gregor Zeitlinger** 04:30 Problem.
Yeah, that part. I'm not jealous about.
**Jack Berg** 04:40 Okay, I'm sharing my screen where you got a light agenda today.
should we just dive into it?
**GZ Gregor Zeitlinger** 04:50 Yeah, I mean, if we have more time, we can also talk more about declarative configuration.
Think there are many topics that are worth exploring. If we have time.
**Jack Berg** 05:03 Yeah, let's go for it.
yeah, that's that's the that's the 1st items on the agenda. So.
**GZ Gregor Zeitlinger** 05:14 Let's check if someone has something else, and we can just pull that up front, I guess.
**Jack Berg** 05:20 Okay.
**Jason Plumb** 05:21 Yeah. So I I've never done the contribut release. It seems pretty straightforward. But I I wanted to go ahead and run with that. We need it in Android. And there's some dangling prs, that we want to get merged.
but I think that should happen today or tomorrow. Well, probably today. And yeah, is there anything that anybody needs from contrib
in this release?
That's that's the reason I bring it up. Or if anybody's like, no, Jason, don't do the release I want. I want this to be a chance to do that. But
I don't think that's gonna happen. We're like 3 months overdue.
**Jack Berg** 05:57 Yeah.
**Jack Shirazi** 05:58 I mean there was. There was a thread on the channel
which involved tasks. Somebody was desperate for the country release, but I don't remember.
**Jason Plumb** 06:09 It might have been me.
No.
**Jack Shirazi** 06:13 Wasn't you or somebody else.
**Jason Plumb** 06:14 Okay. Okay. Good.
**Jack Berg** 06:17 Yeah. Now, somebody was asking for this. Where is it?
Trask was involved, so I can look for his little icon.
**Jason Plumb** 06:30 I like that strategy.
Yeah, okay.
**Jack Berg** 06:36 Yeah, so you know, we're overdue. And I mean, thanks for volunteering Jason. I have.
**Jason Plumb** 06:42 Sure.
**Jack Berg** 06:42 Maintainer permissions for this. So if you come across any issues, and we need to update tooling or work through anything, I can be on standby to approve things.
**Jason Plumb** 06:54 Cool. I I think
I don't know how it works in Contrib. Maybe it's different. Or maybe this is some weird edge case. But I also have maintainer in contrib. I believe.
**Jack Berg** 07:05 Well, cool. That's that's even better.
**Jason Plumb** 07:10 Okay.
**Jack Berg** 07:11 But if you need to make a Pr. You still normally need an an approval to to merge it. So.
**Jason Plumb** 07:15 Yeah, totally. So I'll reach out to you if I need that. Yeah.
Trask
Trask did the change log? Pr, but it needs to be rebased because of all the link checking Snafu.
Let's see.
Yeah, that one.
**Jack Shirazi** 07:36 Wasn't there an issue with publishing to Maven? Has that been resolved.
**Jason Plumb** 07:41 That's been resolved.
**Jack Shirazi** 07:42 Okay.
**Jack Berg** 07:44 Did you? So that was for the instrumentation repo. And so, I guess. Do you know anything about the resolution of that? I know Trask and Laurie aren't here.
**Jason Plumb** 07:52 Dang it! No, I think I think it was on Sonotypes end.
**Jack Berg** 07:57 So there's the sonotype thing. And then we were talking about using a different gradle tool.
**Jason Plumb** 08:04 J releaser.
**Jack Berg** 08:05 J releaser, yeah.
**Jason Plumb** 08:06 Yeah, I don't think that went in.
I looked for it, but we should maybe look again. I'll I'll do that.
**Jack Berg** 08:12 I I guess it doesn't matter for the purposes of the contribute lease. I think you know, if we did go with different tooling, though. You know, as a follow up to the contribute lease, we should probably think about normalizing all of our our builds again. So.
**Jason Plumb** 08:28 Yeah, I totally agree. And I've been. I've been chasing that on the link checker and trying to get them consistent. And it was like the worst time to take on that work
because of this, like sonotype breaking snapshots. And yeah, funge
so I think it was. J. Releaser is the thing that Lori linked to. And I
oh, there's a
there's an open pr in instrumentation that has not been merged yet. It's a 1, 4, 1, 4 6,
so that mentions J. Releaser. And I don't think it's been merged yet, so I don't. I don't think we're yet inconsistent.
**Jack Berg** 09:24 So is this blocking their 2 dot 18 release? It seems like it.
And do we want to? Are we trying to wait for 2 dot. 18 to release contrib, or are we just, you know, overdue, and, you know, catching up with contrib.
**Jason Plumb** 09:41 I think we're overdue, and we need to catch up.
**Jack Berg** 09:44 Okay? And then we can release a subsequent release of Contrib. Once 2 dot, 18 is available.
**Jason Plumb** 09:50 Right? Yeah.
So Android is blocked on. We we want contribu and android. We're also behind in Android. But there's disk buffering changes that we want to bring in.
So we're we're the android release.
**Jack Berg** 10:05 So so what's the issue with?
I I think you should be good to resolve any issues in this Pr, and then merge it. If you want, you know, as a as a maintainer, you have the ability to push to other contributors.
**Jason Plumb** 10:17 Yeah, okay,
I guess I could do the rebase, or I could just merge it. Because what's it? It doesn't conflict. It's just that link check is failing this branch, but we fixed the link check link check in main. So I'm I'm happy to merge that.
**Jack Berg** 10:33 Yeah, that's fine.
**Jason Plumb** 10:34 Okay, cool. This is.
**Jack Berg** 10:35 This isn't a check that blocks merging, anyway. So.
**Jason Plumb** 10:39 Okay, sounds good.
But from the Pr list no one on this call at least, has any pet Prs that they want to see, get in there
other than other than 1 9, 9, 1 which I'm actively working on.
**Jack Berg** 11:02 X integration test.
So if we're not going to merge this Pr to upgrade the version of instrumentation.
**Jason Plumb** 11:12 We need to know that needs to get in there.
**Jack Berg** 11:14 Okay, so this, this is blocking as well.
**Jason Plumb** 11:17 Yeah, I'm that's part of what I'm working on.
**Jack Berg** 11:20 Okay.
**Jason Plumb** 11:21 Yeah.
**Jack Berg** 11:22 Cause that that was gonna be my other comment, because without this, then contributes effectively targeting 2 dot 16, not 2.
**Jason Plumb** 11:28 That's a good deal.
**Jack Berg** 11:29 So it's like 2 behind.
**Jason Plumb** 11:30 Yep.
Yep.
**Jack Berg** 11:41 Okay, there's no additional comments. Then.
Thanks for being a volunteer, Jason.
**Jason Plumb** 11:49 Sure thing
do a lot of companies just take this week off. I heard I heard from some other people that, like a lot of companies are just closed this week in the Us.
**Jack Berg** 12:01 Not mine.
**Jason Plumb** 12:02 Yeah, not mine.
It's just it's been weirdly quiet.
**Jack Berg** 12:08 Yeah sad.
It's a good week to take off. It's Peak summer, and you probably as a Us. Company, we we have a day or 2 off already, so.
**Jason Plumb** 12:19 Yeah.
**Jack Berg** 12:22 Okay, thanks, Jason.
Gregor. I know we we punted this from last week. And so we could take this in a lot of different directions. I've been trying to follow along a lot of the work you've been doing, and just kind of provide comments and stay out of your way. if where do you want to take this? What? What are the most urgent things to discuss.
**GZ Gregor Zeitlinger** 12:47 Actually, it's the Pr that I already have feedback on. But since it's like the most critical one, it's good to have another round of feedback like from everyone. If this looks good, so what it is is, I have a mapping from old to new properties.
**Jack Berg** 13:08 And this is this is the Pr right or no.
**GZ Gregor Zeitlinger** 13:11 Exactly.
It's it's not a big Pr, because it does not do any code changes.
**Jack Berg** 13:19 So is this meant to be a demonstration? Only. I noticed there's no tests in here that sort of verify that that'd be like a nice to have that, you know, somehow verify that the mapping is doing what we think that it's doing. We're sort of asserting it in this file, but.
**GZ Gregor Zeitlinger** 13:36 It is not because this is a specification.
**Jack Berg** 13:40 Oh, okay.
**GZ Gregor Zeitlinger** 13:43 So so will be a breaking change for some things like the
the mapping of some instrumentation which is currently different. But we said that
declarative configuration in Java agent I can still do breaking changes. This is my understanding.
Like, if we do disable. Yeah, let's take disable. The most basic one. The this pr proposes that we disable on the same flag
as the SDK. Currently, it's doing something else. So in the future, if you are using Hotel Java agent disabled in the
A configuration file so it would be under
instrumentation development, Java agent enabled. It won't do anything.
That's why I didn't put it here.
but this is what the automatic mapping would do.
**Jack Berg** 14:46 And I don't.
Bad.
Well, I'm I'm trying to remember. I can't. I can't quite
off the top of my head. I can't remember if it was. If it's possible, in the current release version of the Java agent to actually set this flag via declarative config.
And you, you're saying it is possible to do this. That would you said it would map to instrumentation development.
**GZ Gregor Zeitlinger** 15:13 Well, I all of them
that that was a little bit exaggerated. You could put it there, but it actually would not work, because it is evaluated at an earlier time.
It wouldn't work for that reason, so I would have to pick a different example.
**Jack Berg** 15:29 Okay?
yeah. So there was no. This wasn't actually practically available to set via declarative config before. So we don't have to worry about breaking anybody for that.
The same thing with this log level as well.
Yep. And so what would.
**GZ Gregor Zeitlinger** 15:53 But this like exclude class loaders. And there are several other properties that I didn't put here. Actually, I don't know if they are also in the early list.
So yeah.
**Jack Berg** 16:08 And this seems fine to me we're taking an opinion on this. We took a 1st pass to make things work before, and if anybody did figure out how to get these properties to work. They were sleuthing pretty deep in the code because we didn't actively advertise it anywhere, and we didn't show any examples of these types of things. So you had to dig deep to know that this feature existed.
So I think we're well within our ability to to make a change now, and the sooner that we get opinionated about this the better.
**GZ Gregor Zeitlinger** 16:46 Right.
I'm also saying that this configuration can be used for early loading like this disabled. And the way we do this is that we load the configuration file before the SDK. So we have to
do it a two-phase step. But I think this is what users would expect.
and the only prerequisite is that you set this system property that you want to have the configuration file. So this is the 1st thing that we will check, for then read the configuration file and take it from there.
**Jack Berg** 17:28 Yep.
**GZ Gregor Zeitlinger** 17:34 All right.
**Jack Berg** 17:35 If this, if this is just a specification, and you know that that implies that there would be, you know, subsequent work to sort of incorporate this and
and tested and all those things. So I'm happy to approve it in its current form.
**GZ Gregor Zeitlinger** 17:47 Or what that's worth.
I think you made a suggestion about this application logging.
which is not incorporated, but I kind of liked it because it is more consistent with how the SDK is doing things.
**Jack Berg** 18:11 Right.
**GZ Gregor Zeitlinger** 18:12 Can you explain that again, so that everyone can have an impression on that.
**Jack Berg** 18:20 Yeah. So this down here is
a bit of what I would call like a a smell in that, you know. You have this kind of coupling between properties which are at different levels of this of the data structure, the config data model. So you know, we have.
you know, logging application. And when that logging it, when we say that we're going to log
agent logs to the applications logger, we have this property that says how many we're going to buffer. We're going to buffer 1,000. But this property is only applicable, if you know, in a separate property, in a different level of the hierarchy, you set the type to be application.
And so the alternative to this, which is like a pattern that we've adopted in in declarative config would be something like this, where, you know.
when you're we're specifying the you know, the config for the agents logging and the thing that we want to specify is how we're going to output them and output has 2 options, application or simple.
and you know, output. The the child of this output is always going to have exactly one entry, one key value pair, and you know it will either be application or simple. But to specify both would be invalid.
and you know application has some nested properties underneath it. Simple might at some point in the future. But it doesn't today. And so you know, you can by structuring it this way, you can ensure that you don't have this sort of
this sort of loose coupling, and the only time you can actually specify this property, which is specific to when you want to log to the application logger is, you know, when you've opted into the applications logger. So
it's sort of like by the design of the schema. It sort of makes it more
less brittle.
**GZ Gregor Zeitlinger** 20:31 Yep, I like it.
**Jason Plumb** 20:35 And then the idea is like, if you, if you're testing or want to be able to toggle between one and the other, you just leave a block commented out for the other one, like, if you have simple in there with its own configuration sub configuration, then you could just, I guess, commented out. I'm thinking of, like the collector collector configs where you have like, I have a bunch of receivers, a bunch of exporters, and then I can pick and choose which ones to use. And just just because they're they're configured and they're defined doesn't mean that they're actually used.
That's kind of convenient as a user. But I like that. This kind of enforces the
the intent a little stronger.
**Jack Berg** 21:13 Yeah,
and so that type of structure, the collector has this pattern which happens all over the place. You know. You define your library of processors, exporters, receivers, connectors that you might want to reference. And then you have this separate pipeline section where you organize them.
**Jason Plumb** 21:34 Yeah.
**Jack Berg** 21:34 And
yeah. So we we went in an explicitly different direction with declarative config than that we we could have gone in that way and I guess, like, 1st of all, I don't remember all the reasons why we didn't but we did discuss.
**Jason Plumb** 21:53 Years ago, 5 years ago.
**Jack Berg** 21:54 Yeah, 2 years ago, maybe. But yeah, at some point we decided to to deviate from that pattern. You know. And you can kind of see why, like, you know, as you're
as you're interpreting declarative config with this type of structure, you know.
you never need to like reference. Another part of the hierarchy, like at any particular place in the hierarchy, when you're trying to interpret it and do something like create a batch processor. All the information that you need to create that Batch processor is nested underneath it. You never need like to be able to reference things from, you know, a different place in the yaml, which is the case with the collector's design. So that's a nice sort of benefit.
**Jason Plumb** 22:39 Cool.
**GZ Gregor Zeitlinger** 22:50 I just see that we have
a property that uses a dash, and this is the one common default enabled. I did not list it here, but it's in the ticket.
and I'm wondering if that needs to be more a nesting level.
It's not here. It's only in the ticket. I just noticed that.
**Jack Berg** 23:25 Default enabled.
So in declarative config, we have a convention for using snake case instead of kebab case.
So you know, underscores to separate words. You know, and then that reserves dots if you want to like, imply like in short form notation, you know a child like walking down the hierarchy
**GZ Gregor Zeitlinger** 23:58 So I.
**Jack Berg** 24:00 I guess, like, you know, you could structure this in a 2 different ways. You could say that you have a property called Default underscore enabled.
or you could have default, and then a child property within that called enabled. And you know, it's just a matter, I think, of whether you imagine having other peers of enabled like, if do you want to have a block that's called default, and you know, enabled is just one property. But you imagine other default properties as well.
That would kind of encourage you to go in the direction of
**GZ Gregor Zeitlinger** 24:35 Even if not, we have this enabled column and a couple of places.
So maybe this is like even the line below.
And Id enabled. So maybe this is a smell that we want to clean up
while we have the opportunity.
**Jack Berg** 25:00 Right. That's a nice convention to standardize on like that. You know. You, you'd like, Yeah.
you're always going to have for each instrumentation module, a property called enabled. And you know users get used to that type of ergonomic, and they they come to expect it, and it just like it matches. Their intuition, and, you know, default, underscore, enabled, would deviate from that.
**GZ Gregor Zeitlinger** 25:27 Yeah, okay, I'll make a note to change that.
I also noticed that the SDK. Uses disabled instead of enabled.
But I don't know if we can do anything about that.
**Jack Berg** 25:39 Oh, that's that you know. There's a longstanding debate about that at the spec level.
So you know, there was a
there's this long debate about whether Boolean properties should be named such that, like by default they are false.
right? So we want the SDK to be enabled by default. And so we don't want you to have to explicitly like Set.
you know, enabled is true. And so you know. So we named the Boolean properties, such that like, you know, it's
it's clear that whether it's omitted or explicitly set to false that aligns with what we want the defaults to be. And so that was the argument that was made, you know, years ago for this convention around naming Boolean properties. And then there's been a bunch of people that be like, no, that that sucks. We don't like that like, even though that like, that's an okay argument. Just having our properties called disabled
is unintuitive. And you know, doesn't match what we do with things like, you know, the the agent and the collector, and you know it causes you to have a variety of properties called like disabled and enabled, disabled, enabled, based on what the defaults are for each of those properties? And wouldn't it be better if we just had a convention where everything was enabled.
And so that's kind of like both sides of this argument. Don't want to
argue about it myself, but other people have been pretty passionate about this.
**GZ Gregor Zeitlinger** 27:19 Well, I guess the question. I see the question a little bit different. The question is for me, do we want to have a consistent feel in the entire configuration like that. Booleans are always false by default, and if we do, then we would need to flip some. I just checked that dB statement sanitizer is enabled by default.
**Jack Berg** 27:48 Yeah. So I think Trask has been one of these people that has chimed into this conversation in the past at the spec level and has, you know, taken the point of view that for the Java agent all of our properties are named enabled, whether or not they're they're disabled or enabled by default. And and you know he's made a pretty compelling argument that that's like the most intuitive thing for the users is to name everything enabled.
And so I think that Drask would probably be like opposed to changing that, at least for all the Java agent properties. And so you know.
that means that sort of at the declarative config level. We have this top level property called disabled, which is going to look weird. It's it's gonna be in conflict with the rest of the you know the Java agent properties, and so something's got to give, or it's.
you know, either the Java agent needs to adjust its stance or declarative config needs to adjust its stance, or we need to accept the inconsistency. Those are the 3 options.
**Jack Shirazi** 28:56 Yeah. The. Your disabled also has the
semantic overhead. You have to go disable full. So hang on that. That's too negative. So yeah, okay, it's actually enabled.
**Jack Berg** 29:08 Exactly like the double negatives. Then the cognitive load.
**Jason Plumb** 29:15 There is also an inclusivity argument about the word disabled. It's not, it's not widely used, but people kind of discourage the use of disabled, if, if, when possible.
**Jack Berg** 29:28 Well, so if
If one of you is brave enough, you could open an issue on declarative config, and request that we rename disabled to enabled
and.
**Bruno Baptista** 29:42 Oh, forget! It.
**Jack Berg** 29:46 Oh, Bruno!
**Bruno Baptista** 29:47 We spend. Bruno's been.
**Jack Berg** 29:48 In this conversation too.
**Bruno Baptista** 29:51 Yeah, I was the guy that created the spec. Actually, the it took one month. And yeah, disabled is good.
**Jack Berg** 30:01 Yeah.
like, I said, like other people have been passionate about this. I am not interested in arguing about this.
**Bruno Baptista** 30:10 They have actually good reasons for the disabled.
**GZ Gregor Zeitlinger** 30:18 And I would propose we leave it as it is, and have enabled for Java agent stuff.
**Jack Berg** 30:28 That doesn't seem like the worst thing to me. You know. There there is. Exactly.
Well, maybe maybe there's exactly one Boolean property that is, you know, well known in in declarative config. And that's this top level disabled one.
There's a few more, but they're kind of they're esoteric. They don't actually show up.
**Bruno Baptista** 30:53 Just just one question. So this agent disabled
will it even load something when the application starts?
**GZ Gregor Zeitlinger** 31:06 It will only load the file. That is the goal.
**Bruno Baptista** 31:11 Okay, and it will. It will stop there.
**GZ Gregor Zeitlinger** 31:14 Right.
**Bruno Baptista** 31:16 Okay.
**GZ Gregor Zeitlinger** 31:25 Hey? Should we go to the next one? Then I I'm I'm happy about the feedback. I got.
**Jack Berg** 31:32 Okay, do you have any other topics within this? You know, declarative config combo, or cause I I think that's all for the agenda.
**GZ Gregor Zeitlinger** 31:41 We already scratched on it this dash versus underscore. I think that is also good to discuss
where? Okay? Just the next one.
**Jack Berg** 31:52 Jason's topic.
**GZ Gregor Zeitlinger** 31:56 No.
**Jack Berg** 31:58 No.
**GZ Gregor Zeitlinger** 32:02 Dash versus underscore and mapped properties right? So
I proposed that we change to underscore for all properties, and then I think Jack was wondering if we should support both, and Trask was saying, No, let's be strict.
and I am also leaning towards strictness.
Just wanted to see if there's
any other feedback. If someone has a good argument one way or the other.
**Jack Berg** 32:37 I like this perspective. You know. I didn't want to be too presumptuous about the you know the the agent, because I'm not a Maintainer in it. But if Trask's on board with being strict, it's always easier to to loosen the policy later. But it's strict is a good place to start.
**GZ Gregor Zeitlinger** 32:56 Okay, yeah, those are the most important ones we can. I have another topic if we have more time. But let's see if there's anything else.
**Jack Berg** 33:08 Anyone else have topics that are not on the agenda.
Alright, I guess that means we have more time, Gregor.
**GZ Gregor Zeitlinger** 33:24 All right. Yeah. How to test this? We already
stretched on this couple meetings back, and there is a ticket on how to do. Matrix tests.
And Jay, I think you have already
taking a look at it.
**Jay DeLuca** 33:51 Yeah, I haven't done much, but I've I've started thinking about it, but I I think it would be good to talk about it. In terms of like what our goals are in terms of what things we would want to verify versus. Do we just wanna run things and make sure nothing breaks or
and and which which test do we want to run with this enabled? Do we want to do everything or.
**GZ Gregor Zeitlinger** 34:15 Exactly. That's also why I think it's good to talk about it, because it could potentially be a very
big item to work on.
I put it in the agenda now.
**Jack Berg** 34:27 Okay.
**GZ Gregor Zeitlinger** 34:31 It's the 3rd one.
So what I'm thinking is that we take the system properties that we have, and we write them to a file.
The system properly.
**Jack Berg** 34:52 That we have, where.
**GZ Gregor Zeitlinger** 34:54 We have them in Gradle that add the system properties to the Jvm. Arcs, and
when starting the test, you should be able to read them out, but I have not tried it out yet.
**Jay DeLuca** 35:13 So you're talking about like the set of global properties. Are you talking like? So a lot of our tests will have specific like overrides and and Jvm properties enabled for different test suites.
**GZ Gregor Zeitlinger** 35:27 That's what I'm thinking about.
**Jay DeLuca** 35:32 So would the idea be that we would basically convert all of those to use declarative config.
or those would.
because as soon as we implement declarative config. I guess all those are would not be evaluated right if we, if we try and.
**GZ Gregor Zeitlinger** 35:49 So you would have to have a mapping so that you know where in the file they would be written to, and then you can create the file like this is one way, or we could say, No, this is like too hard to maintain, and we want to have a configuration file that you
put somewhere, maybe in the gradle file, maybe just in the same folder as a convention, and if this file exists, then you read this file instead. This would also be possible.
**Jay DeLuca** 36:28 And and I. And so in terms of what we want to test like, I imagine we want to test like the parsing and make sure that nothing breaks. But are we thinking that we'd actually want to test that the the configurations do certain things
or just parody.
**GZ Gregor Zeitlinger** 36:47 The parity that is important part, so that we gain confidence that users are not losing any feature when they switch to declarative configuration.
**Jack Berg** 37:01 Does everything in the Java agent use
a common abstraction to read configuration out.
**GZ Gregor Zeitlinger** 37:10 I mean, yes, it's used in most places. Not everywhere. Most places use the instrumentation config interface.
Which is implemented by both the Java agent and the spring starter. But there are, or where still some places that read system properties directly. Those would not
benefit from the declarative configuration, but they would also not break. You would still be obliged to use system properties for those.
I think it was used for stable convention switching and Http, and maybe it still is for databases.
Least. Last time I looked.
**Jack Berg** 37:57 Well, so if everything uses this common abstraction, then
then a good way to, you know. Sort of test parity without having to, you know. Do this matrix test, where you kind of rerun every test in every situation with a declarative config equivalent would be to enumerate all of the properties that exist in system, properties and environment variables, that flat schema
and and then provide the equivalent in declarative config
and have a test that you know in both cases resolves an instance of instrumentation config that represents those those sources, and do some sort of a quality like test reading out every single one of those properties and that and and confirm that you you get the same output from like an Api standpoint.
**GZ Gregor Zeitlinger** 38:56 Right, Jay, do we have a list of all properties with the work that you've done so far.
**Jay DeLuca** 39:05 Not yet. I am going through
and creating them, but I think we only have, like 15% of the modules covered so far.
But but we are working towards that.
**GZ Gregor Zeitlinger** 39:17 In general, I like Jack's idea because it sounds to be
an easier to maintain approach if we can get that done.
**Jack Berg** 39:28 Yeah. And and also like the
you know, there's a there's a sort of nice quality to it that you have like one test somewhere that enumerates
all of the config properties in both. You know, config stories, declarative config and system properties. So you know, we can kind of work out exactly how that test harness would work and where it sources those properties from. But that one test would have to have access to you know or know about the complete configuration schema.
and that's that's nice.
**Jay DeLuca** 40:03 Yeah, I think that that makes a lot more sense to me than trying to go and replicate all the configurations in each
module, and individually.
**GZ Gregor Zeitlinger** 40:28 Oh, and what I've
I forgot help on this topic would also be welcome. Now that we have a general idea how this is working would be great to have more
people helping. The board has a
number of tickets that are ready, or that, I think are ready.
and can now be worked on.
I'll put the board again into the document project. Sorry not board.
**Jack Berg** 41:10 Okay, I'll kind of sort of enumerate, or, you know, list out kind of this, this rough idea. For, like a a test on how we could. You know validate this type of thing in in Github?
I'll do that asynchronously, just because I need to think about the right words, and I'm bad at typing and talking.
**Jay DeLuca** 41:32 Appreciate that, Jack. Thank you.
**Jack Berg** 41:34 You know.
**GZ Gregor Zeitlinger** 41:35 Yeah, thanks a lot.
I still have a question for you, Jack, or are you thinking about it right now?
**Jack Berg** 41:42 It. Let's let's talk. Yeah, no, I think I I you know, articulated something very loose and hand wavy. So
**GZ Gregor Zeitlinger** 41:51 There is one ticket that I created for the SDK. Were you planning to work on that? Or is that up for grabs? That is about the internal state of telemetry that is, using global open telemetry.
**Jack Berg** 42:07 Internal state of telemetry that is, using.
**GZ Gregor Zeitlinger** 42:09 Good.
That's 1.
**Jack Berg** 42:18 Yeah, this is a
This is a good question.
if if you want to work on this, by all means take it. I've got my hands full right now. I'll I like like all things I I can. I think that I'll get to them eventually.
but it's hard to say exactly when.
**GZ Gregor Zeitlinger** 42:45 I am probably busy with the spring starter stuff, because I think that is the part that I know most about. But
anyone else just like for the other tickets. Just wanted to ask if you have that
like already figured out, and it only takes you 5 min or something like that.
**Jack Berg** 43:09 I think I have a rough plan for it, right? So like because, we already have to do this for auto configuration today for the system property or the let's call it the flat environment, the flat config schema you know, that has to be able to set up internal telemetry, correctly regardless of whether global open telemetry is or isn't used. And so I think it's like a matter of copy paste modifying
with that approach.
And I don't know. Maybe I can take a look at this, because I'm really familiar with that. I'll take a look. And you know, if it's really easy, I'll I'll you know, send the Pr. For it, and it might. It very well could be that. It's it's pretty easy to do.
**GZ Gregor Zeitlinger** 43:56 Hey? Thanks. Yeah, that was it. Like the most important ones.
**Jack Berg** 44:05 Cool thanks for the discussion.
Alright! So that's all. The agenda last. Call for anybody to
bring up topics that are not on the agenda, or else we'll give everyone 20 min back.
Alright nice to see you all see you next time.
**GZ Gregor Zeitlinger** 44:29 See you.
**Bruno Baptista** 44:30 Bye, bye.
