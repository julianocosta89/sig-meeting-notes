SIG: Java SIG
Date: 2026-04-02
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/niCBal4H-OcsrqFOdgP1sBSBROTX_WgKXOIk6lAL2DMGIPIa0RHSe490tnRO9jIO.MT6Tb9UEx8kUXh0z
============================================================

## Zoom Recording Transcript

**Jack Berg** 01:18 Hello.
**Trask Stalnaker** 01:23 Hey, folks.
**Jason Plumb** 01:27 Hello.
**Trask Stalnaker** 01:33 Looks like my office just got trashed.
**Jack Berg** 01:40 What happened to your office?
Are you in a different room?
**Trask Stalnaker** 01:44 No, it just… oh, they… my video came up, it was, like, sideways. I was looking at random, I don't know, whatever was randomly stacked on my desk. On my desk.
**Jack Berg** 01:57 Raided your office?
**Trask Stalnaker** 01:59 Yeah, my desk is not clean.
**Jason Plumb** 02:01 To go back through the recording and look over that frame by frame there, Trask.
**Trask Stalnaker** 02:06 Yeah, right.
**Jason Plumb** 02:09 The risk of having everything recorded all of the time.
Terrible.
**Trask Stalnaker** 02:16 Yeah, right? Don't leave your… any, like, password papers.
Out on your desk.
**Jack Berg** 02:23 Blur your background.
**Jason Plumb** 02:24 Yeah, here's my important one.
**Jack Berg** 02:27 IMG.
Alright, we've got a light agenda today, so if you have any topics, please add them. I suppose I have a topic. We got the… the Java release… no, that's next week! Okay, good. I don't have to have that topic then.
I was actually… I was kind of nervous about that.
Because there's a PR I wanted to get in beforehand, I thought.
It needed more attention.
**Jason Plumb** 03:28 I've heard very little fanfare… About the excitement of last week, which is a good thing, I suppose.
**Trask Stalnaker** 03:36 Excitement.
**Jason Plumb** 03:37 that we patched. I just hadn't… I expected more, kind of.
**Trask Stalnaker** 03:43 Oh.
**Jason Plumb** 03:44 chatter about that topic, and I haven't heard a lot of chatter about that topic, so I take that as a good thing.
**Trask Stalnaker** 03:53 Probably means not that many people were exposing RMI farts publicly.
**Jason Plumb** 04:00 Seems like a good idea in general.
**Jack Berg** 04:06 Does that reflect in the scoring?
**Trask Stalnaker** 04:09 It doesn't.
**Jason Plumb** 04:10 Hmm.
**Trask Stalnaker** 04:12 Which is…
**Jack Berg** 04:13 Seems like it ought to.
**Trask Stalnaker** 04:14 Right, I know.
I mean, yeah, I remember looking at that.
And there was one… area where it… Slightly could have affected, but for the most part.
It was, like, it was just about… If you… Like, yeah.
I don't… I don't remember. That CVS scoring is.
Trixie.
**Jack Berg** 05:12 Am I sharing my screen?
**Jason Plumb** 05:14 No.
**Jack Berg** 05:15 Okay.
Sorry about that.
**Jason Plumb** 05:17 There you are.
**Jack Berg** 05:21 Okay.
Let's get started. We haven't done Stock Overflow review in a while. Is Stack Overflow still a thing? Sorry.
**Jason Plumb** 05:43 Oh, look at this, yeah.
**Jack Berg** 05:45 Oh my gosh.
I think I'm gonna not do this just because of… I'm not gonna train the AI.
I refuse.
**Jason Plumb** 05:57 I mean, we understand how ironic this situation is, right?
**Jack Berg** 06:00 Yeah. Yeah.
If somebody else wants to do that, they can… You know, the irony is that, like.
I'm clicking from a Google Doc, where I have a Google account with multiple you know, identities associated with it. And I go over here, and this reCAPTCHA, this is… this is a Google, this is a Google product.
And… I'm… would be amazed if there wasn't a cookie that was accessible to those that indicated that I was signed into my Google accounts.
**Trask Stalnaker** 06:38 Or you could have faked that cookie.
**Jack Berg** 06:41 And… and clicking pictures of trucks.
Let's not change that.
Can't be picked, yeah.
**Jason Plumb** 06:50 I mean, the irony is that you're training the AI by clicking the CAPTCHAs. The CAPTCHAs are in place to block the AIs that are scraping Stack Overflow.
**Jack Berg** 06:58 Yeah.
**Jason Plumb** 06:59 Yeah.
**Jack Berg** 07:01 Jay, you got the first topic. You wanna take it away?
**Jay DeLuca** 07:04 Sure, yeah, it's just a quick inform, Marillia, is gathering some questions that SIGS might want included in the end-user survey that they do every once in a while. I think they're preparing to do one in a couple months, so… I just put that example, I guess that's one of the things that they're doing in JavaScript, is, like, they're trying to understand what versions of Node they need to support, things like that.
But yeah, just wasn't sure if we had any ideas for things that we'd want included in that.
**Jason Plumb** 07:43 Is it better to have, like, multiple choice, true-false versus open-ended? Do we know?
**Jay DeLuca** 07:52 I don't know. I don't remember what the last one looked like.
**Jack Berg** 08:08 I'm writing some ideas down here.
things that I… if I… if I… if I had a crystal ball, I would like to know.
**Jay DeLuca** 08:18 What about, like, what exporter or, protocol is used?
**Jack Berg** 08:24 Yep.
**Trask Stalnaker** 08:35 Jack, you were asking for feedback about event… API…
**Jack Berg** 08:45 Yeah, you know, is there interest in using a user-facing log API? Log event API? I don't… what are we calling that thing? Did we call it the log API? Did we call it the event API?
Like, do we call it the log event IPL?
**Trask Stalnaker** 08:58 API. It's the Logs API.
I think in the spec.
**Jack Berg** 09:17 Does this capture, the idea, you think, Trask? If we had a user-facing log API with routing to SLF4J, would you use it?
**Trask Stalnaker** 09:28 Yep.
**Jack Berg** 09:34 This one, are you using ZipKit?
Exporter, specifically, because that's the thing that we're… we've deprecated in our planning on.
Not deleting, but stopping publishing.
**Trask Stalnaker** 09:55 What's the difference?
**Jack Berg** 09:57 So, we've kind of… If we continue to publish, like, a new artifact, but we rip code out of that artifact.
That is considered, like, a breaking change that we're not allowed to do.
But we are allowed to stop publishing artifacts altogether.
And it seems like a cheat.
But somehow, we've… we've done that in the past, and we… You know… We've had the conversation.
**Trask Stalnaker** 10:31 What I mean is, would you not delete it from the repository?
Like, what does delete even mean?
In that… Also, what is the alternative of stopping publishing? What is…
**Jack Berg** 10:45 Well, we could continue publishing it with all the code in that artifact being deprecated for a longer period of time.
I think that would be the only alternative to stopping publishing the module and deleting the code from the repository.
Oh, here's a good one.
Are you using declarative configuration?
**Jason Plumb** 11:21 Yeah, I kinda said the same thing above, but it's a good one.
I think.
I said, are you planning to? But yeah, same question, basically. And then, if not, why not? And if so, why do you like it? Or why did you switch?
**Trask Stalnaker** 11:40 Might be worth scoping that to… Also, whether you're using the Java agent or not.
It's not really stable, since it's not stable in the Java agent.
**Jack Berg** 12:25 You could snap your fingers and solve one problem with the hotel Java ecosystem.
What would it be?
**Jason Plumb** 12:32 And I want to ask every single person this question every day.
**Jack Berg** 12:44 Anybody else have thoughts on this topic?
We can linger, because there's not a packed agenda.
**Jason Plumb** 13:02 I'll share you this, sticker that Honeycomb had at KubeCon.
Oh, there we go.
I thought that was pretty good.
**Jack Berg** 13:17 Oh, no, buddy.
**Jason Plumb** 13:19 Yeah.
**Jack Berg** 13:22 At least we're self-aware.
Okay.
Next topic, just because we have a light agenda.
I've linked to a couple PRs that could use some attention.
One of them, as an approval from Jay, it's about, reflecting spec changes about Metric time series start times.
The key thing here is that, currently, in the Metrics SDK, we, For delta metrics, we're always setting the start time to be the time of the last collection.
And if it's… If there has been no collection yet, then it's, like, the start time of the SDK.
And for cumulative, we're always setting the start time to be the start time of the SDK.
And the spec has changed. Before, this was, like, an open-ended part of the spec. There was, like, very little guidance on what you should do for the start time. And in order to solve… unblock this problem of, like, we want to add a method to finish instruments, to close time series.
We need to have, you know, we need to be more detailed about the start time. And essentially, the thing that we're trying to embody with this start time change is that the start time should be, the… What's the language that it uses? Let's see if I can… Pull it up.
the timestamp which best represents the first possible moment a measurement could have been recorded.
So, if you kind of think about what that means, and you try to the different, the different scenarios we encounter, and the scenarios are, I lay them out here. It's like, you know, delta versus cumulative, and synchronous versus asynchronous for each of those. Those are kind of the dimensions you need to think about, like, what your rules should be for start time.
And yeah, the rules are now kind of codified in the spec, and, you know, follow that line of thinking of, like, what's the first possible moment that a measurement could have been recorded?
And so this embodies that, and… For reasons, it ends up being, you know, a PR that touches lots of code.
It's been a couple of weeks since I wrote it, so… I forget some of the details on why it touches so many files. I imagine there's, like.
It's a lot of test files, but… Oh, and it looks like GitHub is having problems again, so…
**Jason Plumb** 16:13 Impossible.
**Jack Berg** 16:18 What's the, their uptime? They're approaching single 9. Single 9 of uptime, that's the joke. Or maybe not the joke.
**Trask Stalnaker** 16:28 I think the joke is that they're almost not even at 1-9.
**Jason Plumb** 16:32 Oh, man.
**John Watson** 16:32 I think they're shooting for 5 eighths.
**Jason Plumb** 16:34 Bye, babe.
It's a pretty good poker hand.
**Jack Berg** 16:40 Bye there.
**John Watson** 16:41 Not as good as Five9's, though.
**Jason Plumb** 16:43 It's true.
**Jack Berg** 16:47 Well, I'm gonna struggle to talk about this if I can't pull up the code, so, Anyways, it's… it's a bit tricky to talk about, but, yeah, like, the reason why this matters more than anything else is it paves the way for this other spec issue, which is, to add a finish method to our synchronous APIs, our synchronous metric instruments, so… yeah, you'd be able to, for a given histogram or counter or up-down counter, say, like, hey, finish these series. And, and yeah, this contributes to that. So, take a look if you're interested and able.
And then the other one, now I'm, suspicious of whether this will load at all. Oh, okay, so the… Okay, so GitHub is, you know, I managed to get a connection to one of the servers that isn't Flapping, so that's good.
But yeah, this is a, I opened this PR back on January 8th, and it's, it's the first step in adding OSGI support.
And I guess the interesting bit is we've had collaboration from some OSGI experts, I'm not familiar with these people personally, but you know, based on what I can tell about them, they know a little bit about OSGI. And, you know.
the key bit in here is OSGI ends up being sort of like Graal native.
And in the sense of, like, for Grawl, we have these, we have these integration tests, and we, like, we say, hey, we're gonna test.
We're gonna test Graal, that, like, it works with our, that we have properly configured our artifacts to work with GraalVM, but the thing you don't really know is, like.
This is sort of a, like, a smoke test level test, in the sense of, like, it… We add, you know, all of our dependencies, like our, you know, most of our dependencies that we publish, and, and then we verify that things work.
But it's… there's less confidence that if you add, like, different combinations of dependencies, that everything works, because maybe… maybe, like, in the absence of, of OTLP, an SPI isn't there, and it causes, like, it causes the, you know, the growl to fail in some novel way. And OSGI is a similar type of thing, where, you know, what I've done here is I've added support, and I've added an integration test here.
That has… like, what are the dependencies that I've done? So, you know, I've added one sort of test suite that has all the SDK all, that's, like, the dependency, and I do, like, a sort of smoke test with SDK all.
But if you tried to use this with other combinations of dependencies, like with auto-configure, with OTLP, with file configuration, I am sure that, we would run into, issues where, like, the SPI information isn't properly encoded into these… into the manifest, and OSGI would fail. And so those are, like, follow-up steps that are coming, is, like.
you know, coming up with additional test suites that reflect the different combinations of dependencies that are popular, and verifying that those work, and that the right metadata is included in the headers to allow those to work. But, you know, OSGI has been an open issue since As long as I've been around this process.
**Jason Plumb** 20:28 2020, yeah.
**Jack Berg** 20:30 2020, so it's like, let's get something, and let's… and then let's work from there. So that's kind of my goal here.
So, I think it's pretty safe to do. If you care to go deep into OSGI and give it, like, a thorough review, that's, like, fine. But, you know, Yeah, I'll probably merge it if we can get a, a green check.
That's all I have to say about that.
Anybody else have topics? Lori, Trask? Anything on the instrumentation side?
**Jason Plumb** 21:11 That OSGI issue, I'm just jumping in. That OSGI issue has this label on it, which is release after GA.
And I was looking at what is in there, that's a fun list.
**Jack Berg** 21:27 Yeah, yeah, these are the things that we were just gonna do the month after GA, just in the 1.1 release.
**Jason Plumb** 21:36 Metrics for drop spans, that's pretty fun.
**Jack Berg** 21:41 Hey, we have this! This is solved.
**Jason Plumb** 21:43 Close it.
**Jack Berg** 21:51 Let's see… Should I actually reference the issue?
Or just close it.
Or take up the PR that solved it.
**Jason Plumb** 22:00 It was a reference, yeah, it was, like, 8.98 or something.
**John Watson** 22:03 disclosure.
**Jason Plumb** 22:04 889.
**Jack Berg** 22:14 Oh, now I have to actually pull it up now. It was by Honorock. Honorock did this.
**John Watson** 22:19 No, I think I did it.
**Jack Berg** 22:21 Okay, well…
**John Watson** 22:22 I mean, I put the original implementation in. You can see that on… that pull request for 889, but I mean, it wasn't… it was just, you know, with the old, made-up Names for the counters and stuff.
**Jack Berg** 22:37 Right.
**John Watson** 22:41 I don't remember the… I don't remember the later one where we actually have, I have semantic conventions for it.
**Jack Berg** 22:49 Yeah, now I'm being just a little loose. I don't… I don't care.
**John Watson** 22:52 I mean, it's my issue, close it. I don't care. It's fine. It's all good.
**Jack Berg** 22:56 Alright.
Oh, there was this interesting thing that happened the other day, just because there's nothing on the agenda. So, somebody reported this, like a test flake, or just like this. It's actually not a failure in the build, but it's just verbose logs, because I made a change that didn't clean up a managed channel, and managed channel really wants to let you know when it's not cleaned up.
so… that was interesting, but then somebody added this thing here.
like, hey, there's this one task that's failing in Ubuntu and RHEL, and they go and they reference a specific build, and if you go in here, everything's green. All the tasks passed. But if you go down to the build in here.
And you go get this test that they were claiming failed.
Let me do a Ctrl-F on it.
You can see that there's a… This is a logged a standard error, but there's a… failure. It's… there's a test failure, so despite a test failure, the build succeeded.
I have not seen that before.
**Lauri** 24:14 Maybe you have, retries enabled.
**Trask Stalnaker** 24:20 Yeah.
**Lauri** 24:20 Sorry about that.
There was once, then it retries it.
**Trask Stalnaker** 24:23 in my comment, Jack?
**Jack Berg** 24:25 Okay. My bad comment.
**Trask Stalnaker** 24:28 I know, I realized today when I saw the follow-up that my comment was horribly terse.
**Lauri** 24:35 You could try and see if you have the build scan link.
**Jack Berg** 24:42 That would be at the bottom, I assume.
Oh my gosh, look at these verbose logs. This is… I opened a PR to fix these just a couple of days ago, but… It's crazy, we're just logging out all this spam now.
Or we were.
Is that in the end of the build?
the velocity… That's the cache entry.
**Trask Stalnaker** 25:11 Yeah.
**Lauri** 25:11 And it should…
**Trask Stalnaker** 25:11 Very loud.
**Lauri** 25:12 out.
**Trask Stalnaker** 25:12 line.
**Lauri** 25:13 I think.
**Jack Berg** 25:15 I'm…
**Lauri** 25:15 Excuse me.
**Jack Berg** 25:16 use it.
**Lauri** 25:16 Road at the bottom, I think, the bottom part appears faster, so…
**Trask Stalnaker** 25:21 We have really long, build logs in instrumentation repos, so we actually copied the scan link to another step so that we can get it without having to download the log.
There you go.
**Jack Berg** 25:38 Let's scan.
**Trask Stalnaker** 25:39 Two lines down, yeah.
**Jack Berg** 25:58 So I don't… so the… okay, so the flaky, is this a reflection that… It succeeded after a retry?
**Trask Stalnaker** 26:05 Yeah.
**Jack Berg** 26:06 Execution 2 of 2.
That… Is… you were exactly right.
**Trask Stalnaker** 26:31 Yeah, don't give me any credit for my horrible comment.
**Jack Berg** 26:35 Just gonna figure out how to write a correct sentence.
**Trask Stalnaker** 26:38 No. No.
**Jack Berg** 26:56 Let's see if this is… oh, nice. I mean, that's even a good permalink, so that works.
So, I should be able to close that.
**Lauri** 27:03 Well, sometimes there are issues where the test always fails the first time.
**Jack Berg** 27:14 Do you think this is one of them, or…
**Lauri** 27:17 I don't know. What's your context there? In, In velocity, you can actually exceed flaky test.
Somehow.
**Jack Berg** 27:31 I'm not gonna go into that right now, unless you really want to.
**Trask Stalnaker** 27:36 No, but we… we… we've seen that in the instrumentation repo. Sometimes, there's certain conditions where it… because it'll… when it runs… when it retries, it retries the single test in isolation.
And so, in some cases, that… Is enough for it to pass, whereas it always fails when it's run In the group with all the tests.
**Jack Berg** 28:02 Right, some other test pollutes the.
**Trask Stalnaker** 28:04 Yeah.
**Jack Berg** 28:05 In some way.
**Trask Stalnaker** 28:05 Yeah.
**Jack Berg** 28:08 So, I guess, like, the… Lori, is your point then that, like, we should check to see if this is one of those types of tests that always succeeds the second time?
Just as, like, a sort of double check.
**Lauri** 28:23 Well, I guess you could always try running it on your own machine also.
**Jack Berg** 28:27 Yeah, the build passes locally for me all the time, so that's why I suspect Not the case.
**Lauri** 28:32 I'm just wondering why that person pointed out that this test is failing.
**Jack Berg** 28:45 I don't know.
Trying to figure out the source of this, This spammy log message in the build, which… but, you know, it was already solved.
Let's see… I can track down the PR, but I already opened a PR to fix this, to close this… this resource.
Anyways, that's enough time on… Something that isn't that important.
Any other topics before we end early?
**Jason Plumb** 29:27 Not for me.
**Jack Berg** 29:29 Alright, well then… I'll see you next week, and on Slack.
**Trask Stalnaker** 29:35 We're driving.
**Jack Berg** 29:35 See ya.
**Trask Stalnaker** 29:37 Wait.
**Pranav Sharma** 29:38 See ya, guys!
