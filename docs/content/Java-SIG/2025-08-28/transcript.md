SIG: Java SIG
Date: 2025-08-28
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:14 Hey, hey!
**Jason Plumb** 01:17 Hey! Zoom told me it has new floating effects on and reactions, so I had to try it.
**Trask Stalnaker** 01:22 Like, what is… what's going on, Jason?
**Jason Plumb** 01:25 I don't know, it just, like, floats up, like, this just, like, comes about… I don't know if everyone's on the same.
**Trask Stalnaker** 01:30 Yeah.
**Jason Plumb** 01:31 Yeah, yeah, I see it.
Very important new feature they're adding, day by day.
Yep.
**Trask Stalnaker** 01:48 Alright, on the count of 3.
Alright… I think we can get started.
… Gregor.
Yes, we added this in the last meeting.
To follow up, Lori… in case you had… better… Idea specifically about… … this.
So… … Currently, Instrumentation API incubator is in the Bootstrap class loader.
for, I believe for bridging purposes.
… But we're only… Ridge… Let's see… instrumentation… Nope.
Instrumentation API….
**GZ Gregor Zeitlinger** 03:56 Sorry, I was in the wrong meeting.
**Trask Stalnaker** 03:59 Oh, hey, Gregor.
We're only… bridge a couple of things from Instrumentation HPI. I actually didn't check why we have the incubator Over there, also. Probably I should do that.
Fantastic.
**Lauri Tulmin** 04:19 Not only for breaching.
The idea is that it gets shady, and … When the instrumentations use the incubating instrumentation API, they will be using the shaded classes from the bootloader.
So, anything.
**Trask Stalnaker** 04:39 Oh, dude.
**Lauri Tulmin** 04:40 Anything you want to use from the instrumentation.
**Trask Stalnaker** 04:43 Yes, of course.
That makes sense.
Okay, so maybe declarative config bridge… is… do we have any instrument… like, is it really instrumentation API? Maybe that's the… maybe that's our problem, Gregor, is that it's more of an SDK component?
Then an API component?
**GZ Gregor Zeitlinger** 05:13 The question I was asking is if it is… Incubating and declarative configuration is incubating.
**Trask Stalnaker** 05:22 Yeah, but it's like SDK is incubating in the SDK side.
**GZ Gregor Zeitlinger** 05:28 Oh, that does… okay, then I asked the wrong question.
**Trask Stalnaker** 05:33 I think… ….
**GZ Gregor Zeitlinger** 05:37 The instrumentation API is not stable?
**Trask Stalnaker** 05:42 No, no, no. Sorry, I'm not suggesting that… be an instrumentation API, and I may be… and now I'm, sorry, paging in a lot of history. The declarative config, we want it to be available to instrumentations, not… is not an SDK.
concept.
So the bridge….
**GZ Gregor Zeitlinger** 06:12 The bridge is not an SDK concept, yes.
**Trask Stalnaker** 06:15 I see, because we want….
**GZ Gregor Zeitlinger** 06:21 That's basically because….
**Trask Stalnaker** 06:22 Excuse me.
**GZ Gregor Zeitlinger** 06:22 Has not been spec'd.
**Trask Stalnaker** 06:29 Okay.
In the examples over here… So… inferred spans… Let's see, that is… it's in a span processor, right?
Where it's getting used.
**GZ Gregor Zeitlinger** 06:53 There, it's in a span processor, yes, but there are also examples where it's not in a processor, but where it's in a… Where the content is in the instrumentation part, for… GCP, authentication, I think that's the case.
**Trask Stalnaker** 07:17 That's gonna be an SDK thing also, the exporter auth.
**GZ Gregor Zeitlinger** 07:23 Well, I'm not sure which, but there was one example where it's in the instrumentation part, I have to look it up.
**Trask Stalnaker** 07:31 Okay.
**Lauri Tulmin** 07:34 Do we have instrumentations in the country, Repo?
**GZ Gregor Zeitlinger** 07:40 … The resource providers are instrumentation.
I think we call them instrumentation.
**Lauri Tulmin** 07:48 They aren't, like, instrumentations in the sense of what Trask is meaning.
**Trask Stalnaker** 07:55 So, it… The distinction I'm trying to make is SDK versus API, whether the things rely on SDK versus API.
**Lauri Tulmin** 08:08 I think what the Trask's, like, main question is, is that If placing the stuff in the instrumentation API incubator requires you to do weird things, then maybe you ought to place them into some other module.
**GZ Gregor Zeitlinger** 08:27 Hmm. Well, weird is a little bit vague. I don't know if it's weird.
**Trask Stalnaker** 08:34 But let's… yeah, let's follow up on this, Gregor.
if you can find the… an example of needing… Yet… in the API.
**Lauri Tulmin** 08:51 Actually, I think we had some other module that also had rear split.
that some of the classes were placed into Bootstrap Loader and others into the… Into the agent folder.
**Trask Stalnaker** 09:04 There's the Java Agent tooling.
**Lauri Tulmin** 09:07 Yeah, I think.
**GZ Gregor Zeitlinger** 09:14 I mean, we can always just make a new, … A module for that.
At one point, I even had that.
**Trask Stalnaker** 09:27 But I do want to, … Through, like, where… what's… so, we were considering on the SDK side, I… Yeah, we were considering… we want to have, eventually, right, a GET config provider over here.
Isn't that right, Gregor? Wasn't that the discussion with Jack?
**GZ Gregor Zeitlinger** 09:54 In the extended one, and it's only because it's incubating. Yeah, eventually we will have the config provider there. You're right.
Once it's stable.
**Trask Stalnaker** 10:06 Okay, and config… provider… … That's exposing declarative config.
**GZ Gregor Zeitlinger** 10:27 Yes.
**Trask Stalnaker** 10:31 And so, you… if you wanted in… in the instrumentation, I mean, it… It feels like for… That use case, you would… Would we even want… because we don't even have any instrumentation support today.
in API classes, like, for instrumentations that rely on API, We don't have any configuration, like, library… Instrumentations all require programmatic access, because we didn't have a solution.
And so I kind of think that over there, maybe we don't need the bridge.
We can just say, hey, for… that's an enticement for people to move to declarative config.
….
**GZ Gregor Zeitlinger** 11:23 You mean abandoned support for… The current configuration, or what do you mean by move?
**Trask Stalnaker** 11:29 No, I mean specifically for library instrumentations that rely… that aren't SDK-based.
Right? SDK instrumentations today can already get config properties.
And so it makes sense to support them to have the bridge for them.
But instrumentation… library instrumentations that don't rely on the SDK, Today, Have no config properties access.
**GZ Gregor Zeitlinger** 12:01 Okay.
**Trask Stalnaker** 12:03 And so, maybe we don't need the bridge over there, and we could make the bridge only an SDK Bing.
**GZ Gregor Zeitlinger** 12:14 And how does that translate to the… different modules.
**Trask Stalnaker** 12:21 Well, we wouldn't want it to be in the instrumentation API, then.
**GZ Gregor Zeitlinger** 12:32 Okay.
And also not in the incubator, or is incubator different? Right, right.
**Trask Stalnaker** 12:36 No, no, we wouldn't want it to be anything, like, under Instrumentation API or API incubator.
… Maybe this one? SDK Auto Configure Support?
**GZ Gregor Zeitlinger** 12:52 Yeah, I had thought about that, but, this, if you pull this in, Then, you… Get, magic stuff happening, like, it has… it changes your resources.
Because it has a customizer.
**Trask Stalnaker** 13:09 Okay.
**GZ Gregor Zeitlinger** 13:14 SDK Bridge was, … a new module I had,
**Trask Stalnaker** 13:19 Yeah.
**GZ Gregor Zeitlinger** 13:20 Before I, before I actually changed it to be in the instrumentation API, based on last week's discussion.
**Trask Stalnaker** 13:30 Yeah, maybe that makes sense.
**GZ Gregor Zeitlinger** 13:34 And I just have to, I think, revert a couple of commits and make this a new PR.
**Trask Stalnaker** 13:42 Cool, I kind of like that also because it makes it clear, like, it's an optional thing that people can opt into ringing if they need that sort of dual support.
**GZ Gregor Zeitlinger** 13:57 Yep, I… I'll do that.
**Trask Stalnaker** 14:00 Alright, thanks.
Alright, … Next. We already had an hour on declarative config before this, ….
**GZ Gregor Zeitlinger** 14:21 I was just gonna say, let's put it down.
**Trask Stalnaker** 14:25 No, it's okay.
**GZ Gregor Zeitlinger** 14:26 Time at the end.
**Trask Stalnaker** 14:27 Yeah, yeah.
… Alright, Jay.
**Jay DeLuca** 14:36 I just wanted to give a PSA for this. I noticed if you click on the… that first link, the overnight metadata job.
… So, like, for people who may not know.
We run the, the metadata updater each night, and it should pick up on either new instrumentations added, you know, changes in the telemetry.
And this morning, there was a lot of changes, and a lot of removals, and when I dug into it, it looks like after the Gradle 9 upgrade, Gradle changed the way that they, … parse tests, or, like, if you… create the… the test task. If you don't specify the classes directory, then it… it won't run anything, it just fails silently, so… It seems like all of our… like, experimental, test-stable conventions, all those, I don't think they are running as of now. And so I've… I've been… working on fixing it, we just basically have to go into all those test suites and add that test classes, dirs, equals, files, whatever. So, yeah, just a PSA. I haven't looked at core to see if we are setting up special test suites there as well, but… Yeah, just wanted to bring that up. I plan on fixing this, but for anybody who might be using… That same type of configuration elsewhere, just a PSA.
**John Watson** 15:58 I'm pretty sure in Core we have a large number of special test suites.
**Jay DeLuca** 16:03 Okay, I can take a look at those after.
**John Watson** 16:08 Although I don't know if they're declared in the same way that would be breaking here, but it's definitely worth looking at.
**Trask Stalnaker** 16:19 So, just understanding, so, this is, … If you have an other, like, if you have source… other test Java, this will work, but if you were relying on it being the source… Main Java… it won't?
**Jay DeLuca** 16:42 Can I share my screen for a sec?
**Trask Stalnaker** 16:43 Yeah, yeah.
**Jay DeLuca** 16:58 So… let's… Sorry.
Looking at some other stuff.
So if you have a… basically, like, a task where you're registering a test class. Stuff like this still works if you're registering an entire suite.
But if you're registering a test test and not specifying a class directory, then it just… basically, it runs, and it just says no source… Detected. But it doesn't fail or anything, so… ….
**Trask Stalnaker** 17:37 Should we be using testing suites instead?
**Jay DeLuca** 17:45 Oh, I understand.
**Trask Stalnaker** 17:46 I understand the difference between them.
**Jay DeLuca** 17:50 I don't either. I know the syntax is different, so I think it would require more changes, but I could certainly look into it, but I don't know off the top of my head.
If we should be using one versus the other, but… Yeah, essentially.
**Trask Stalnaker** 18:04 very… it seems very hacky, the, having to specify the test classes like that, from a Gradle perspective, which makes me wonder if they had a different Preference in mind.
**Jay DeLuca** 18:22 tentative.
These are, like, the two different ways that they say you can… do it, so if you… have a test suite, and then you… you add the targets, that… that's another way to do it.
**Trask Stalnaker** 18:44 That one looks a lot cleaner to me.
that option.
**Jay DeLuca** 18:53 Okay, yeah, I can play around with it and see if we can… we can do it that way instead. The annoying thing was, I wasn't able to find a way to just automatically identify all of them, so I think I have to literally go in to every build griddle.
**Trask Stalnaker** 19:09 Copilot won't… Copilot won't do that for you?
**Jay DeLuca** 19:12 I… I tried to get Cursor to do it, and it kept giving up, saying that there was too much to do. But yeah, there might be some automation that I can use there, but… But yeah, so I'll continue hacking on this, but I just wanted to let people know in case you guys have projects elsewhere that also use Gradle 9 might be something to look into.
**Trask Stalnaker** 19:36 I have an idea.
So, we just, … … started allowing repos to enable the, GitHub Copilot coding agent.
Because we needed to, set up co-author, verification.
Ezcla co-author verification, since the bot is the author, and so we want the co-author, the person who sent it, to be EZCLA checked.
… We And I enabled that easy CLA check here in our repo, the co-author CLA check.
And so we can… Right, oh yes, that's at the… or level.
Coding agent, let's… we can… pad… I've been wanting to try this out.
I would… I… Been using it on my fork, … But, if you, if you… Update this, or add more stuff to it?
I will be able to, I can assign it to… co-pilot now.
**Jay DeLuca** 21:23 Copilot.
**Trask Stalnaker** 21:25 And it'll go and crank for half an hour on it.
And we can see what it does. It feels like a task that Copilot could do.
**Jay DeLuca** 21:35 Yeah.
But yeah, I'll, … so we'll do that. I'll hash out the description a little bit more, and … see if I can make it robot-friendly, and then we can, … See how it goes.
**Trask Stalnaker** 21:49 Cool.
**Jay DeLuca** 21:52 But I thought it was cool that the, the metadata job kind of uncovered that.
**Trask Stalnaker** 21:55 Yeah, totally.
**Jay DeLuca** 21:56 I don't know how we would have, noticed it if that didn't….
**Trask Stalnaker** 22:02 Jason.
**Jason Plumb** 22:05 Just saying, you know, they made the choice.
**Trask Stalnaker** 22:10 Huh….
**Jason Plumb** 22:11 Yeah, I think the… that failure mode of, like, just not doing anything and just passing silently is such a bad… Approach.
**Jay DeLuca** 22:22 Yeah, I was… I was trying… yeah, I was trying to see if there was, like, a config or a flag or something that I could set for, like, a strict mode or whatever, but I haven't been able to find something just yet. They have a flag you can set if it doesn't detect any test, … files, but… I was experimenting with that, and that didn't seem to catch This particular issue, so….
**Jason Plumb** 22:43 Yeah.
Thanks for taking that on.
**Jay DeLuca** 22:47 Yeah, I promise.
**Trask Stalnaker** 22:48 Finding it, yeah.
**Jason Plumb** 22:50 That makes me want to look in Android.
**Trask Stalnaker** 22:51 Who knows how long, like, you know, with… We could have been running for, like, you know, 6 months before we noticed that.
**Jay DeLuca** 23:01 Yeah.
**Trask Stalnaker** 23:02 A third of our tests weren't running Alright, moving on!
Tyler!
**Tyler Benson** 23:15 Yeah, so, the past couple weeks I've been, working in the, … contrib area to try to make the disk buffering a little bit more efficient. I have a desire to use it for purposes of a server, not Android, but a server to have a local disk buffering for metric collection. And the server that I'm running it on, though, is fairly memory constrained, and so there's concern about the extra allocations involved in the current implementation.
So that's one reason that I implemented the optimization for when it's writing it to the disk, to use the more efficient implementation that the SDK provides.
… But when reading from disk and sending it back along the process.
it uses the standard exporter API, which effectively requires the disk buffering to deserialize, and then the exporter is going to reserialize effectively into the exact same format in most cases, I would assume.
And so… I provided this PR in effort to avoid that double, you know, reserialization process, but apparently, there's plans to change the API, that… Kind of diverges a little bit more from this. … And so, I'm just kind of curious, if people think that this is, … a common enough approach that, it's worth, sharing, or is this something I should just accept and Work privately in, in effectively my own fork.
**Jason Plumb** 25:24 I think the short answer is no. I reached out to Cesar at the beginning of this call when I saw that you had this item on here in hopes that he would show up, but he's… he's probably not around, or he's doing something else.
I think, what you're bringing up is quite important. I think the… the re-serialization and deserialization is, like, super unfortunate in the current approach. It's something that I think… I don't know, Watson, did you write the original one back in the… no? Okay. Well, some….
**John Watson** 25:53 I never, yeah, I never did anything with the disk buffering stuff.
**Jason Plumb** 25:56 Alright, well, we had a Zipkin implementation way back in the Splunk Android version, and we had intentionally avoided this. Like, we… what we stored on disk was the thing that should go on the wire, and so for exporting then, it was, like, literally just, like, read off of disk, put it in the request body.
And… it was for this exact reason. So I think this is… I think, Tyler, I appreciate that you're bringing this up. I think it's important for us to think about. And it is… the timing of this is unfortunate, too, because of the API redesign.
**GZ Gregor Zeitlinger** 26:29 Yeah, I think it's related to the API redesign, because Tyler, when he brought it up, Cesar's response was that it's not compatible with the API redesign, but I think this is approaching it from the wrong direction.
we should make the API design compatible with a use case if we agree that it is, An important one, and I would say it is an important one.
**Jason Plumb** 26:57 Yeah.
**GZ Gregor Zeitlinger** 27:01 Should we, … discuss it in the Android, or reschedule to next week, because it's quite hard, if Cesar cannot explain, Why, … the API design is in a way that is not compatible, or in other words, how we can make it compatible.
**Jason Plumb** 27:22 I haven't finished reviewing these two PRs yet, so it's hard for me to have too strong of an opinion, but I'm open… I think… I think we'd be very much open to reviewing this in the Android SIG next Tuesday, Tyler, if you can make it.
**Tyler Benson** 27:37 I'll look at my calendar and see if I can, drop in.
**Jason Plumb** 27:41 It would be… if you're on the East Coast, it would be 11 your time on Tuesday.
**Tyler Benson** 27:46 Yeah, that's always, like, the hot spot for calendar appointments.
**Jason Plumb** 27:50 I get it. I feel that pain. ….
**Tyler Benson** 27:54 I think one other thing I wanted to bring up that, would have been, like, my next step in making this more efficient is currently the, when it reads from the file, it reads the whole byte array into memory before it passes it along, and I think that's another unnecessary step.
Where… … Really, like, it should be able to, read You know, buffer at a time of sorts, directly from disk.
and pass that along through an I.O. stream.
And, so that way, if you've got a big, byte array in memory, you're able to avoid that if you take chunks of the file at a time and effectively send that all the way down to the network I.O. stream.
So, that's not covered in this PR, but, you know, if we are able to change the API to support that, that would be another extension of this same story that I would like to address, if possible.
**Jason Plumb** 29:07 Yeah, being able to get the bytes on the wire quicker while the file is still being read would be great. That doesn't… that operation doesn't span multiple input files, does it?
**Tyler Benson** 29:18 No, it's only ever one file at a time.
**Jason Plumb** 29:20 Then, yeah, I think that approach is really, really solid.
**GZ Gregor Zeitlinger** 29:24 So if, for example, there was a file stored that had, like, a thousand spans in it.
**Jason Plumb** 29:29 And we need to send those in one batch.
Oh yeah, actually, does the batching in the files match the batching on the wire? Is that… is it one-to-one there, or do we re-batch?
**Tyler Benson** 29:40 So right now, I think that it does it, in… individual spans. Like, there's some weirdness going on that I need to investigate further. Yeah, okay. I don't like the way that it's… there's some problems with the way that it's currently implemented, so I need to investigate more, but ideally, you know, it could be up to the senders to decide how big of a batch it should take.
Because I could see that, you know, maybe you collect more data on disk than you really want to send all at once.
And, you know, I think the sender should be able to determine how big of a batch it should send.
And adjust accordingly.
**Jason Plumb** 30:27 One of the challenges with that approach, though, is if that… what the sender wants is larger than files, and you have to span multiple files. That's when it gets challenging.
**Tyler Benson** 30:36 Yeah, no, I think that having it constrained to, at most, one file is fine. Okay. What I'm saying is if one file is bigger than what you want to send at once.
Got it, okay. Across multiple requests, is what I was trying to get at.
**Jason Plumb** 30:53 But then you have to kind of… I mean, we'll have to keep state of where you left off in that file, but that's also probably fine.
**GZ Gregor Zeitlinger** 31:00 That is already working, yeah.
**Jason Plumb** 31:02 Yeah. Okay.
And, Tyler, you have reviewed Cesar's, implementation.
**Tyler Benson** 31:11 Yeah, so I think one of my concerns about his implementation is, it seems like he's basically seeding ground. He's deleting a lot of the existing API and focusing on this iterator pattern.
**Jason Plumb** 31:26 Yeah. Where that….
**Tyler Benson** 31:27 Still is iterating through a collection of data objects, which means that the second you touch that iterator, it has to deserialize everything.
**Jason Plumb** 31:38 Totally.
Yeah, that's totally the new API. Yeah.
**Tyler Benson** 31:44 And so he… his argument was that, you know, I could still use… I could still touch that same class, but maybe reimplement it so that I do something differently, but I feel like that becomes very ugly and broken.
**Jason Plumb** 32:06 the… So, Tyler, in your approach, the protos that you put on the disk.
They're… are they more ready to get on the wire, or are they completely ready to go on the wire, like, in a request body?
**Tyler Benson** 32:19 They're completely ready to go. I'm using the exact same serializer that the SDK uses.
**Jason Plumb** 32:28 Got it. So if the… if the sender has an opinion about size, though, how do you handle that?
**Tyler Benson** 32:34 If the sender has… so what happens, in… I might be completely wrong about this, but, yeah, I'm a little bit naive as to how Protobuff works, but the way that it seems is that the request effectively defines a repeating field, right? So, it says, hey, we've got, you know, a repeating series of spans, or a repeating series of metric data.
That are serialized to disk. And so, the iterator goes through each of those spans individually, I believe. And, the iterator, goes through Or maybe it's a collection of spans, and so… … there must… I'm not exactly clear on this. I need to do some more research, but I thought that it was a….
**Jason Plumb** 33:29 a repeating series of spans, as opposed to a collection of spans, and so… Like 44 there, yeah.
**Tyler Benson** 33:38 Yeah, so resource spans means it's a list, right? … Yeah.
So… In that case, then, what I'm proposing is that you could potentially control the size, then, based off of how big those are that you write to disk in each batch.
**Jason Plumb** 33:58 Right, and your size.
**Tyler Benson** 33:59 Understood.
**Jason Plumb** 34:00 Your size unit, then, is not bytes, your size unit is, like, resource spans.
**Tyler Benson** 34:05 Yes.
**Jason Plumb** 34:06 Okay. Okay, that seems viable, I think.
**Trask Stalnaker** 34:10 You still have to do a little bit of magic, right? Because the… that traces data….
**Jason Plumb** 34:17 Has the size.
**Trask Stalnaker** 34:18 Yes, it has the size prefixed to it, so you gotta sum up.
**Tyler Benson** 34:25 For sure.
But that's all, you know, just byte array magic that you can manipulate the bytes, I believe, and, you know, combine consecutive ones without having to deserialize and reserialize all over again.
**Jason Plumb** 34:39 Yeah, conceptually, it should be much more lightweight than… like, dealing with the protos should be more lightweight than dealing with the objects.
Okay.
**Tyler Benson** 34:49 And I think you can still do the whole thing, streaming.
Without loading everything into disk.
**Trask Stalnaker** 34:58 Well, you need to get your size. You need to look across them all to get the size first.
**Jason Plumb** 35:05 That sucks.
**Trask Stalnaker** 35:05 Goes over the wire first.
**Jason Plumb** 35:07 Yeah.
**Trask Stalnaker** 35:09 But then you could stream.
So you could do… you could do fancy stuff.
**Jason Plumb** 35:17 But you don't know the size until you read it, right?
**Trask Stalnaker** 35:19 I mean, you can look at… You can read the first byte of each file to see the size of each one.
**Jason Plumb** 35:26 Yeah.
**Trask Stalnaker** 35:27 Prefix for the… yeah.
Anyway, just make sure there's good test case tests.
**Tyler Benson** 35:34 For sure, yeah. I think that that's definitely, implied, but… the… the thing that, I'm running into, though, is, like.
So he's saying that he's making this change to kind of support the use case of encryption and compression and… My argument is, is that there are streaming I.O. implementations for both of those, and I think that you can still work with raw bytes or raw files, even with, if you're encrypting or compressing the files.
So… I… I don't think that the significant change in the API that he's trying to do… necessarily, … is necessary to support those desires.
**Jason Plumb** 36:32 Yeah, with compression and encryption, it almost makes it more opaque. Like, you don't… you definitely then don't want to decompress or decrypt and then re-swizzle it on the wire, because that would be very expensive, right? So that approach also suggests The desire to take stuff more wholesale off of disk to put it in the request body, or stream it.
**Tyler Benson** 36:53 Yeah.
**Jason Plumb** 36:54 Yeah.
I don't… yeah, I don't fully understand the approach, so I want him to be around to defend it or talk about it.
**Tyler Benson** 37:03 Okay.
That's it for me.
**Trask Stalnaker** 37:11 Alright, … We've got… declarative config milestones.
Let's talk about it.
**GZ Gregor Zeitlinger** 37:24 Right, yeah. About 2 months ago, I started working on it, and I'm… it, turned out to be a bit bigger than I anticipated, so I'm wondering how we can split it into milestones with, the goal That we can have something that we… can put in front of users, maybe not as the recommended approach, but as a stable approach, … And… If you go to the last meeting notes, I have made, a rough… outline how we could do this. Yeah, exactly. … So, 3 milestones, ….
**Trask Stalnaker** 38:13 Can I ask one clarifying question first? You said stable.
Is that….
**GZ Gregor Zeitlinger** 38:19 No, slave is not the right word. Okay.
**Trask Stalnaker** 38:22 Good.
usable.
**GZ Gregor Zeitlinger** 38:26 Usable, yeah, that's probably a better word.
… So the, … First one does not have the Spring Starter, for example. It does not have all of the contribut components.
… But it does have documentation, obviously. It has stability around… configuration options, that's why we need to have the bridge in, and we should also be comfortable that things are not broken. That's why we have this discussion about integration tests that We have not finished yet. We talked about it a couple of weeks ago.
… Resource providers, I think, are also important.
Luckily, there is nothing big blocking it.
Distro support, I'm unsure about, this should be discussed. Yeah, any bug fixes, of course, should also be in.
Second, part is, Spring Starter, and then, things, that are, and Contrip, but that are not as common.
And, … Probably also the discussion about the extended open telemetry that we had A week or two ago. … And, then the third milestone is things that are taking a longer, time, because they involve spec work, like the authentication work, and a semantic convention. Probably also, maybe we get it faster, but this is what I'm currently thinking.
And then also work that is, like, future work, like generating, schema so that you have auto-config… autocomplete support in editors, things that we have not even really committed to, but that would be possible based on the work that we have.
Yeah, and back to the milestone one, as we write documentation, and we write a blog post, and we say now, feel free to use it. So, we should be, Comfortable with getting, bug reports that things are not working, as users expect, and then we can either point out That this is something for a future milestone, or we just fixed the bug.
**Trask Stalnaker** 41:14 Yeah, this is really the most important thing to me, the integration tests, that once we have good You know, solid integration tests across, you know, a lot of, like.
Comprehensive, you know, across all the instrumentations, hopefully, something like that.
Then… Yeah.
I'll let… have users… let users have at it.
**Jason Plumb** 41:43 The configs are so massive, how are we going to maintain this?
Like, those… the declarative config YAML alone is just, like, thousands of lines, right?
**GZ Gregor Zeitlinger** 41:53 Not a typical one. The kitchen sink example is so big because it has everything that you could possibly configure.
Or are you thinking about something else?
**Jason Plumb** 42:06 No, that's what I'm thinking of. I guess there… are there… I thought everything had to be present or explicit. Is that no longer the case?
**GZ Gregor Zeitlinger** 42:14 I don't think it ever was.
**Jason Plumb** 42:16 Oh.
**GZ Gregor Zeitlinger** 42:18 You have to.
**Trask Stalnaker** 42:19 You have a couple of things, … You have to have the OTLP, like, it doesn't default to OTLP if you don't have it present.
**Jason Plumb** 42:27 Because that's what secure the SDK. Yeah.
**Lauri Tulmin** 42:32 Don't you have to list all the resource providers and stuff like that also?
**GZ Gregor Zeitlinger** 42:37 Yeah, compared to, currently, you have to do more. I was just saying, it's not everything.
**Jason Plumb** 42:43 Okay, that's fair.
**Lauri Tulmin** 42:46 Wouldn't it be in the spirit of the Declarative convict to also list every single instrumentation that you wish to include?
**Jason Plumb** 42:53 Oh, no!
That's what I'm worried about.
It's gonna be a lot.
**GZ Gregor Zeitlinger** 43:01 No, luckily, that is in our prerogative to define what the instrumentation should do, and we have not said that you have to list everything.
**Lauri Tulmin** 43:14 Yeah, that wouldn't work out.
**GZ Gregor Zeitlinger** 43:17 Nope.
**Robert Niedziela** 43:19 Yeah, and there are multiple defaults as well, right? So….
**GZ Gregor Zeitlinger** 43:28 Yeah, if you want, we can discuss the tests. I also think that this is, … That we need a discussion about that part.
**Trask Stalnaker** 43:42 I mean, I would like to see… I… … All of the… Ideally, I would love to have that as just yet another matrix build.
Where we run everything with the declarative integration, with the declarative configuration.
Just to uncover… everything possible.
But I'm not sure how that would look.
… Or if that's reasonable… yet.
Or if that's necessary.
**GZ Gregor Zeitlinger** 44:22 Based on, what I have implemented so far, it seems a little bit excessive, because, the bridge, the declarative configuration bridge.
this, … The only, moving part, That is going to affect how instrumentations, Behave when declarative configuration is present.
Apart from anything that is, that can, of course, break if we have not tested declarative configuration at least once.
But we have a test for that since we have a component that is using declarative configuration explicitly, which is the module and instrumentation.
So, I'm thinking, that, … A couple of tests that, have, … an input file, maybe more than we currently have in the method, test, … Is reasonable, but not for every instrumentation.
**Trask Stalnaker** 45:33 So, the thing that I'm worried about, maybe it's not a… problem is… When you opt in.
to declarative configuration, you don't get any of the regular config property, like, you… the SDK doesn't… None of the… none of the normal SDK config property stuff gets configured, right?
Like, the SDK is gonna ignore properties. We're not gonna ignore properties… Because we're putting the bridge in place.
**GZ Gregor Zeitlinger** 46:11 This is only affecting the instrumentation part. If you don't configure an OTLP exporter, then the agent will not save you from that.
Or it should not save you from that.
**Trask Stalnaker** 46:27 And what, I guess would… need to look at any SDK components that we're customizing or configuring.
And making sure that those… work with declarido config.
**GZ Gregor Zeitlinger** 46:47 What?
**Trask Stalnaker** 46:48 We're adding a refund.
Like, a resource provider… The… the span… any span processors….
**GZ Gregor Zeitlinger** 47:00 But for the resource providers that we have in the agent repository.
we ought to have tests. I mean, there is a pull request, and if that pull request doesn't have a sufficient test, then we should add it right there.
**Trask Stalnaker** 47:14 With declarative config.
Yes. Like, have a YAML… Okay.
**GZ Gregor Zeitlinger** 47:18 Exactly. Yeah, that's… that's what I would expect.
**Trask Stalnaker** 47:21 Okay. Yeah, that makes sense to me.
**GZ Gregor Zeitlinger** 47:25 What is, what are other things that we have that I might not have looked at?
**Trask Stalnaker** 47:31 Span processors… I would just look at the, everything that we… in the auto… our auto-configure customizer.
I don't remember if there's… I don't think we actually do that much in the vanilla Java agent.
**GZ Gregor Zeitlinger** 47:56 The auto config… I know what you mean, I'll check that.
**Trask Stalnaker** 48:00 I know we have that thread details spam processor….
**GZ Gregor Zeitlinger** 48:05 Right, yeah, right.
Yeah, that's a good point.
**Robert Niedziela** 48:16 Resource providers are now called detectors, right? I mean… in, in….
**GZ Gregor Zeitlinger** 48:22 Declarative code.
**Robert Niedziela** 48:23 I think not….
**GZ Gregor Zeitlinger** 48:26 No, ….
**Robert Niedziela** 48:27 No, it's not.
**GZ Gregor Zeitlinger** 48:28 Maybe you are talking about entities?
So, this is not….
**Trask Stalnaker** 48:37 Other languages call… some languages call them detectors, resource detectors.
I don't know what the heck….
**GZ Gregor Zeitlinger** 48:46 We have called one of the providers detector, but this was more, like, by accident, as far as I could see from the source code.
**Robert Niedziela** 49:00 Okay, the YAML section is called Detectors, right?
There's detector model, detection model.
**GZ Gregor Zeitlinger** 49:10 Oh yeah, yeah, that could be, I have not… Looked at that part specifically.
Right, exactly.
**Trask Stalnaker** 49:18 Yeah, the spec calls them resource detectors.
**GZ Gregor Zeitlinger** 49:26 In the API service area, it's called a component provider, ….
**Robert Niedziela** 49:34 Yeah, that's… that's implemented as a… Implementation of resource provider, yeah.
**GZ Gregor Zeitlinger** 49:41 Yeah, exactly.
**Robert Niedziela** 49:42 The components provider, sorry.
**Trask Stalnaker** 49:46 Yeah, I think the… the confusion sometimes comes because sometimes in Java we call it resource provider.
… But at the spec, it's called a resource detector.
**Robert Niedziela** 49:59 In, in, … flat schema, I mean, this old approach, right, with environment variables and properties, we had something like resource customizers, and it's not expected to be working with Firebase config.
**GZ Gregor Zeitlinger** 50:21 No, … essentially, this was deemed as too confusing, and declarative configuration takes a more explicit approach. You explicitly list what detectors you want to have, and then, in addition, you can have an Include and exclude list if you want to have more, control over exactly what, Attributes you want to have.
**Robert Niedziela** 50:50 Okay.
**John Watson** 50:52 Yeah, just, I think it's called Resource Provider on the Java side, because it's an SPI, and it matches the SPI naming… naming conventions.
**GZ Gregor Zeitlinger** 51:00 Oh, okay.
**Trask Stalnaker** 51:06 This is gonna be interesting, Gregor.
But, we'll… I think we'll just have to get there when… when we… once we're… ready. I'm not sure if it's… I think each one of us Who has a distro, we'll have to… Kinda dig in and see what works and doesn't work.
And what we need to improve.
**GZ Gregor Zeitlinger** 51:31 Yeah, I, I… I have, an idea how to do it.
But, it's not in a PR yet, so for the discussion here, it's just, Do we want to have a blog post out to use it before we have our distros ready? Or, … Is that, odd, and we want to have it in the distros?
As soon as possible.
**Jason Plumb** 52:02 My opinion is that we'd at least want the distros to try it and be able to provide feedback.
Before that blog post would go out?
In case there's some very rough edges.
… That's just.
**GZ Gregor Zeitlinger** 52:18 I mean… You mean a rough edge if users try declarative configuration with the distro?
**Jason Plumb** 52:25 No, if the distro is implementing it and encounters rough edges.
**Trask Stalnaker** 52:33 It is a good source of… source of user feedback.
**Jason Plumb** 52:36 Yeah.
**Trask Stalnaker** 52:37 … I don't think it needs to be done… though, they don't need to support it. ….
**Jason Plumb** 52:46 Totally.
**Trask Stalnaker** 52:47 similar with the Spring Starter Support.
It would be nice to just kind of have a idea… some confidence that it's going to work in the future.
That we haven't, sort of, boxed ourselves into anything problematic.
**Jason Plumb** 53:06 Yeah, I think… I think moving distro support to Milestone 2 is fine, but if… we should have an item up there that's, like, distro… Integration feedback or something up there that's, like, distros trying it out and providing input.
**GZ Gregor Zeitlinger** 53:19 Yep, that's fair.
**Jason Plumb** 53:20 Okay.
**Robert Niedziela** 53:24 the roughest edge I encountered so far is the resource that is not fully configured.
and exposed to the client code, right? And yeah, I had to do some really nasty workarounds to get the resource fully configured for my code.
**GZ Gregor Zeitlinger** 53:47 Yep, that is true. There is… I think this is one of the… bug fix items, but I did not add it explicitly.
We have to get that to work, you're totally right.
I think I have delayed that because, … I really want to have Jack's input on that, because he has a strong opinion that we should not expose resource, and it's bad if we try to make a decision before he can have a say.
**Trask Stalnaker** 54:35 Cool. Yeah, I think… I mean, it looks great, thanks for putting some thought into this, Gregor.
**GZ Gregor Zeitlinger** 54:43 Yeah, thanks a lot for the feedback.
Now that looks much closer to actually seeing the light at the end of the tunnel.
**Trask Stalnaker** 54:59 Alright, we're just about on time. Any last… Topics… Then, see y'all next week!
**GZ Gregor Zeitlinger** 55:14 See you!
**Robert Niedziela** 55:14 Bill, bye.
**Jason Plumb** 55:16 I….
**Pranav Sharma** 55:18 Bye-bye.
