SIG: OpenTelemetry C/C++ SIG
Date: 2025-12-01
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/972hyo2pKKNJen2gDwC2LgBzNd8WPDxs7XAHRYX2nxhw1q9FQjuwmVJXULKfQITT.X6kisM1d5_aS9JwJ
============================================================

## Zoom Recording Transcript

Doug Barker 00:01:57 Hey, Tom.
Tom Tan 00:02:00 Hi, Doc, good afternoon.
Doug Barker 00:02:02 Good afternoon.
Tom Tan 00:02:07 I haven't seen any notes from Mark, not sure he will join or not, and later, I'm also not sure he…
Who are joined or not today?
Doug Barker 00:02:20 Yeah, maybe we can hang out for a few minutes, see if they join. There's Mark.
Tom Tan 00:02:24 Ma, hi.
malff 00:02:27 Hi, everyone.
Doug Barker 00:02:30 Hey, Mark.
malff 00:02:34 So, I guess you're back from Thanksgiving.
Doug Barker 00:02:40 Yep.
Tom Tan 00:02:41 Yes.
Ehsan 00:03:17 Hi, everyone.
malff 00:03:19 Hi, son.
Doug Barker 00:03:22 Excellent.
Tom Tan 00:03:23 Hi, yes, I'm…
malff 00:03:30 So I'll just share my screen, do you all see it?
Doug Barker 00:03:38 Yep.
malff 00:03:42 Great.
I have a few topics for today, I don't know if you have any, anything special as well.
So, the first one is the… the spec,
in the spec, in the trace context, there is a PR to
Mark the trace context level 2 as required.
And actually, we have an issue for that.
Which is this one.
So, so far, we are only using the trace context level 1 in propagation, so we need to adjust to level 2.
And probably review if everything is okay or not, and also see if
If we have any enough coverage in tests, or things like that, so…
Some… some work to come, coming from the spec, just to be aware of it.
And apart from that, my main topic is the ceiling tidy cleanup PR from Doog, which I think is great, so…
We need to discuss, how to proceed with that,
We need to… there's a lot of cleanup to do, obviously, and especially a lot of cleanup to do in the API itself.
So, I wanted to discuss with you how you see things going for that.
Doug Barker 00:05:31 Yeah, sounds good. So I think with that.
the header files, run through Clink Tidy and upgrade to Clink Tidy20, it's gonna bring in… or it's gonna expose, I think, over 600 warnings. So, like Mark said, there's,
maybe some… some coordination around when we want to turn that on. In order to help facilitate the cleanup, I had to output a markdown report, so it's a little bit easier to see where the warnings are coming from by file and by, Clank Tidy check.
So, that might be, you know, one way to organize around how we clean them up, is to either pick a file, or pick a… pick a check, and just start creating the PRs to address them.
malff 00:06:25 And I looked at the… at the summary before, it's quite nice, because it's well organized.
So, earlier, we've, included what you use or things like that, it was just a huge.
Log file, and… We had to…
Parse it and see different errors there, but in this case, everything is nicely presented.
So we know that File by file, what is going on, and so it's much easier.
Find issues to fix.
So, thanks, Du, for the report, because it's,
It makes it much easier to work with.
Doug Barker 00:07:08 Yeah, no worries.
malff 00:07:09 And also.
Doug Barker 00:07:09 And if you scroll all the way down, there's a section that breaks it down by a claim tidy check, so…
malff 00:07:15 Yes, yes.
So… If we… if we fix,
Check by check, say, fix all the signing issues, and fix all these things like that, yes, then we can find all the warnings for a given error number.
So, quite nice.
And the sad thing, once we are done with the cleanup, then that report will be empty, so…
Doug Barker 00:07:45 Well, there's always more checks to enable.
malff 00:07:47 Yes, that's true, that's true.
So yeah, so my…
My concern mostly… well, everything which is in SDK we can fix. The concern is for things which are in the API.
Just picking one randomly.
If we… if we need to clean that up.
It may break the ABR itself.
So… For ABI V1, we cannot touch it, so we might have to…
Add some, some special comments.
And otherwise, so…
Yeah, this one, if a copy constructor is missing, we can add it, that should be okay, but there are other things which are likely to be breaking changes, so either we'll need to provide some special comments to silence the warning.
And, otherwise, we may still want to clean that up, so maybe we will have…
a cleanup, but only in ABI V2, then.
I guess we need to… to see that on…
on each fixes, but I'm expecting that, if we really want to clean that up in,
we might as well have a very clean ABI V2, to work with.
Any comments on that?
Okay, well, I guess we can see that when we have the different PRs, with fixes coming.
Just so you know, I had some very old tooling to actually check ABI.
Which I updated recently.
So it's in, it's not in the CPP repo, it's in,
It's in my own repo with, OpenTelemetry, CPP, ABI, I think.
Which are some scripts to, to compare to APIs automatically.
Ehsan 00:10:22 Do you have a link for that?
malff 00:10:24 Let's me, let me find one.
It's this one.
So, my own repo and, CPPA BI.
Basically, you need to install a couple developers, and then,
Run a script that will generate a report comparing every single version we've made.
Tom Tan 00:11:12 Is there a plan to bring this tool to the official report?
malff 00:11:16 Yes, it's, it's basically using the official repo as Git submodule to pull from it.
And to compile with, every single,
version that we shipped. Let me show you…
It has submodules for every single release, so I just update it to the latest one, 24.
So, what it does is it takes a simple,
simple code, which is using the trace API to write a tracer.
And compiling that against, version 1, version 2, version 3, and so forth.
And… Using some tooling to compare the binary to see
between API version this or a API version that, if anything changed.
The best is to start with a README, if you're interested, to see how it works.
Tom Tan 00:12:21 Okay.
malff 00:12:31 No, this one.
Yeah, so we have it.
Another topic I wanted to discuss, quickly, the meeting dates for December. As you know,
There is Christmas, and so on, so I'm expecting that nobody will be here for the last two weeks of Christmas… of December.
And… Just to have a…
just to know, do you plan to be around for early December, like, December 10 or 15?
To know if we can maintain the meetings or not.
Ehsan 00:13:36 That won't be available December 10th.
malff 00:13:48 Okay, so otherwise, for the next two meetings, we can… I guess we should have enough people then.
And last thing, so, I don't know if you… if you are aware, but, in the spec repo.
The compliant matrix used to be this huge MD file with a fancy syntax and an HTML table that was very difficult to maintain.
So this has changed with a YAML file instead.
And… Earlier, the file had one… one line for every single,
Every single language for a specific item.
So… it was causing some chaos with mergers, because, say, the Java team says they have won
one feature in one line, then it could cause a merge issue with another team, like PHP says they have the same feature, things like that.
So now we have a dedicated file for C++.
So, if Java clicks… checks some flags in the matrix, it will be…
no longer generating much conflicts with other languages. So each team has… each language has its own file.
And we have… what we have is…
just a YAML file to the
To provide all the input from the matrix.
So this has been changed a while ago. Now, one thing I noticed is that, well, especially someone…
someone was asking in the spec in an issue, well, how come this feature is not implemented? Because no one has reported it in the matrix, and in fact, we forgot to do it. So, in some cases, we have features we try in CPP,
But we forgot to update the matrix there, so the matrix is…
In some cases, way out of date. So we probably should take a look to fill the gaps there.
And when doing so, we need to upgrade the… update the YAML file and not the… not the MD file.
That's it for me,
We can, of course, go through the issues and PRs, but do you have any general topics to discuss?
Tom Tan 00:16:42 No, on my part.
malff 00:16:44 Okay.
One thing, though, which is, showing up again in issues…
there is still this problem with, Windows and, and single tons.
So I'm assuming there are some reports of saying that things don't work on Windows, and I'm guessing that this could be related to the issue with Windows singletons.
this is… this has been there for a long time, but it's really blocking for Windows, and so I wonder if anyone has any idea of how to address that and what we should do about it.
This is really too… boozy shoes.
So, a while ago, we started the discussion to see what we can do.
But I guess we have to…
To take a look at that and try to fix it one way or another.
from… Technically, I think the simplest solution is to do that.
So… possibly ship a small API library that only contains the single tons.
Because we cannot make it, head-only, obviously.
So, we need to…
We need to discuss that to see how to plan it and how to do it.
Doof.
Any comments on that overall? Because if you do, you are muted.
Ehsan 00:19:43 What would be the consequence for…
Giving up on the header only.
malff 00:19:50 Well, typically an application,
Built with, instrumented with OpenTelemetry, we'll have to link.
With one library?
So, it's annoying because people need to change their makefile.
But that will be only for one platform.
And not on… not for all of them.
So the fact that you link with the library which is instrumented now shows, because when you consume the library, you also have to have the OpenTelemetry singletons.
I think there's a wave with pragmas
to… inside the header file, to tell the linker in Windows that, hey, by the way, you should use this library as well. So we might have a way to work around that, but I don't know enough the details of how this works.
Doug Barker 00:20:51 How does this relate to the single DLL that we create now and include in the package?
malff 00:20:56 It's, it's a different issue.
The single DLL is to ship all the SDK and exporters.
But this one, this is related to the singletons for the tracer provider, metric provider, and related things.
that the API is head-only, so when you compile some instrumented application against the API, the API uses the tracer singleton, for example, to look at it and then to invoke
To start a tracer.
And the problem is that this singleton,
It's working on other platforms, because we have a way to tell the linker that all the code resolves to the same thing, but on Windows, this does not work. My understanding is that this is mostly because the
The binary format on Windows does not support that concept, so that…
Relinker can not resolve everything at once.
Tom Tan 00:22:04 And what is the first option? The title?
malff 00:22:10 Where to fix it, but… But,
I mean, if you remember, I've tried 4 years ago, and it went nowhere.
Tom Tan 00:22:24 Okay, I see.
malff 00:22:33 So, Tom, one thing what I don't get is,
I'm assuming that at Microsoft, you are using OpenTelemetry in a couple of places.
How come this is not an issue important for for Microsoft.
Tom Tan 00:22:53 I think for… for now, the team I work with is…
We use starting a library, and
Only maybe used for… for their component, or, like, we don't use it to… To do the…
Cross module… context propagation a lot, so this is not an issue I have seen.
malff 00:23:21 Okay.
Tom Tan 00:23:28 Yeah.
malff 00:23:31 Yeah, and Doug, thanks for mentioning this. There is also a lot of work to do on the single DLL as well.
Especially the way we export things, there are a lot of symbols missing, so…
people cannot link properly when using the single DLL, but it's a totally separate issue.
Tom Tan 00:23:50 a deal or studio has problems, like, we wish, like Jude, I think we should not,
release the DL itself, right? Maybe we can provide the DL build.
Fully released DO, then… We need a…
secure way to sign it. I think currently there's no such way for us.
And, yeah.
And also, for deer out, like…
If different components depend on different versions, like OpenConnecture version, That can be some… some…
someone comes from another deal, which depends on our different deal version, I think that could be a problem.
Like, you have two components.
depend on slide, two different OpenTelemetry DLs, Then…
I think that the original idea for, I think, at least from the beginning…
of working on DL is for, like, for some… some… oop.
We released some common… deal, OpenTomach deal, like, we released that in the…
OS, or somehow our common package, but I think it will… And then, after the initial
Start, make it the initial networking, we…
We're not pushing to that target.
So I think the versioning will also be a problem.
Yeah, I mentioned this because for the signing thing, mention the signing, because for .NET, for the OpenTemperature .NET, we…
we have… we got some issue on the signing, because for .NET, I think signing…
In most, production environment, that's… that's required. And, we made some internal solution, like, we did some internal
Signing that with our… Certificate, and for that part, we don't publish that to the public.
I think for… for… that will apply to… to the open territory material here, right, for option two.
malff 00:26:12 Okay.
Tom Tan 00:26:13 Yeah.
malff 00:26:14 So you're saying that if we make a… A library for that.
Yeah, resolve the signing issues, and… What it creates, okay.
Tom Tan 00:26:29 Yeah. If we release a deal, the binary form in, like, in our release, package our release, we should consider signing, but then…
I think for native binary, especially on Windows, there will be a trust issue, like, which certificate to use. Maybe there are some open source certificates, like for OpenTelemetry, maybe you can use one, but usually that's not trusted by Windows.
Hmm, not that useful, yeah.
malff 00:26:58 Okay.
Tom Tan 00:27:08 Yeah, maybe… yeah, I'm not sure, I…
Or maybe I forgot some details about Option 1. Maybe we should do some more exploration.
malff 00:27:20 Well, I remember some special compiling flags.
But, we, we never got… Got it to work.
Tom Tan 00:27:30 Okay.
Also, if we… header only… give up header only, will that break our, like, API, right, or…
malff 00:27:48 I don't see why, but there is also the risk there.
Tom Tan 00:27:59 Okay.
malff 00:28:07 So, in any case, this is something that,
we already need to resolve at some point, because more and more people are complaining on Windows itself.
Tom Tan 00:28:17 I see.
Force duplicate copies in each library to be resolved by the linker.
Is this for static linking, right? Or static library?
I mean, we… What's the scenario?
And.
malff 00:28:37 Well, I'll say not free, but I don't think it's really feasible, because this… this involves a lot of code, and on top of that, it will have to do… to be done header only.
Which is even more complicated.
Tom Tan 00:28:52 Okay.
But even, I think, for… for the DLL build, we faced the similar problem, right? Like, the header file can be used by as many application or users code, and all the
Singletons should resolve to the one from the DL.
I just think maybe the same should work for static linking, too?
malff 00:29:20 No idea, we need to see the details, but .
Tom Tan 00:29:26 Yeah, oh, yeah.
malff 00:29:29 But this… my point is, this needs to be investigated.
Tom Tan 00:29:32 Yeah, I remember that, yeah, but I can't just…
Get… get all the details on that.
malff 00:29:39 Okay.
Tom Tan 00:29:54 Or is there anyone from your side who can… Drive this, like, investigation, like…
malff 00:30:07 You, you mean, at Oracle? No, because we don't use Oracle. We don't use Windows, mostly.
Tom Tan 00:30:14 Okay.
malff 00:30:15 This is only affecting, basically, people are using the MySQL connector when talking to the database.
Tom Tan 00:30:24 So… Okay.
malff 00:30:26 a client might be using a GDPC connector, things like that.
And… When this is instrumented, we see this issue, but otherwise, on the server side, we don't use that.
Tom Tan 00:30:38 Excellent.
Okay.
Okay.
malff 00:31:02 I don't have any other general topics,
Want to take a look at, issues and PRs really quick.
Oh, I remember I had another topic also.
For some reason, so this is because someone just noticed, where is it?
So, I remember that Lalit used to export as a script to export all of the…
Brief documentation generated from the code to some, some website.
But this has been,
That… that was exporting the doc until version 1.11 or something like that, and it has been,
Not updated since.
Tom Tan 00:32:27 Is that a random manager? That tool? Yeah.
malff 00:32:34 this thing, read the docs.io.
Tom Tan 00:32:37 Updated manually, right? Or…
malff 00:32:41 Well, I don't know how it was updated, but the thing is, it's no longer edited, this is for sure, so…
Tom Tan 00:32:48 Yeah.
malff 00:32:48 We're looking at… Where is it?
Tom Tan 00:32:54 Wonderful.
malff 00:32:56 there is a revision somewhere, so I looked at this commit ID, and it was, like, version 1.11.
We are at version 1.24 today.
Tom Tan 00:33:07 So this is way out of date.
And the copyright year, is correct, right? So the last update was 2021.
malff 00:33:22 Possibly… I don't know where this comes from. I don't know if it comes from the script itself, running that, or if it comes from the source.
Because we don't change the UR in our copyright as well, so…
That could be why it's lagging behind.
What is my CMake?
Sometime when we have a copyright year, it's always very old.
Anyway… So, yeah, this dog is way out of date.
So…
The first question is, well, do we try to keep it up to date or not? And we have to see with Vlad how this worked, because I think he had some, some tooling there.
And if we don't maintain that, then we need to see with, the official,
doc repository where to place this, this generated content.
Tom Tan 00:34:31 Okay.
malff 00:34:34 So I guess, we have to see that with, Servin Neumann, and…
Tom Tan 00:34:38 Okay, I'll ping Nalid on this.
malff 00:34:42 Okay.
So yeah, back to issues,
Oh… Someone had a crash, in one-time context, but it's…
It seems to be related to the order in which things are initialized in this application.
But we don't have… Not of details, Bill.
So those two Windows things, I don't quite know what to do with it.
So…
Yeah, the complaint is that one of our own examples is not even working.
And I suspect that this is because of this singleton thing.
But even before the singleton, okay.
Tom Tan 00:35:58 Hmm.
malff 00:35:59 This, this person has also reported that they had a lot of issues with a single DLL, that they had to change the way…
The symbols are exported, to make sure that it links. So we have multiple issues to fix.
The singleton issue is one, But we also have a single DLL to fix.
Tom Tan 00:36:21 Okay, so he's using the DL build, and it doesn't work.
malff 00:36:26 Well, he is, but he has a lot of issues with that.
Like, this magic file that says, which symbol is exported here to fix it.
Tom Tan 00:36:39 I see.
Okay.
Maybe you'll send this to me. Usually, I run metric sample locally, it runs fine.
malff 00:36:54 Okay.
Tom Tan 00:36:55 Yeah, maybe some beauty issue, I think.
malff 00:37:02 Thanks.
Doug Barker 00:37:03 We do have the test for that one disabled in CI, because it was flaky, and it would sometimes crash, so maybe there is another issue.
Tom Tan 00:37:11 Oh.
malff 00:37:13 It could be, yes.
Or is it the metric sample test that was, failing?
Doug Barker 00:37:19 I believe so.
malff 00:37:23 Yeah, good point. Could be unrated.
So there's that, and also someone complaining about the single DLL as well.
And so… Yeah.
When we build the single DLL, I think we put everything from the SDK itself.
Well, everything. We tried to put everything from the SDK, but this is… Possibly missing some symbols.
But on top of that, I don't think we… we add the libraries for the different exporters.
So, in this case, he's compiling with gRPC, and expects the gRPC exporter to be part of that single DID, and it's not.
Tom Tan 00:38:22 Okay. Oh, does it cook and leaves our tail, or building?
Beautiful.
Oh yeah, maybe you need to take a model.
malff 00:38:33 Okay, can you take a look at?
Yeah.
Tom Tan 00:38:36 Okay, yeah.
malff 00:39:06 So, the remaining things… so this is… About metrics?
I don't even know I call…
Between the synchronous and asynchronous metrics, and between counter-good,
And all the things that we have, like Eastlogram, and there is another one I forgot.
I think not everything is implemented.
Tom Tan 00:39:33 So I don't know…
malff 00:39:35 I don't remember if… This should be implemented or not, like, it goes in asynchronous?
Tom Tan 00:39:44 Oops.
malff 00:39:46 And on top of that, the… I think the reporter is using
Labels, but… well, they are adding attributes to a metric.
But somehow, the attributes they are adding are not just dimension, it's… Noise, which is causing,
The metric storage to grow forever.
Do you know if latitud is around these days?
Tom Tan 00:40:30 Yeah, hey, Hay is better today, I think.
3 of the AV of A, ticks.
malff 00:40:37 Okay.
Tom Tan 00:40:37 Yeah.
malff 00:40:39 Because he's, he's the person who knows the best this part of the code.
Okay.
Tom Tan 00:40:48 You can assign it to me, too, you know, I'll sync with him.
malff 00:40:52 Okay.
Thanks.
Tom Tan 00:40:56 No problem.
malff 00:41:44 So this one, I guess we can take it and investigate.
I think I can look at it.
And the last one… this has been opened a while ago.
For some reason, there is some global memory which is used by the Portobuf library itself.
And…
There is, in his application, there is a memory leak at the end, because that library is not cleaned up.
But the thing is, so yeah, so this is the magic thing that needs to be done. However, this is a global cleanup.
So the problem becomes, when you have multiple libraries in the same application.
When multiple libraries are each of them using protoburf.
If one library issue shouldn't put a buff, it just kills the others. So, obviously, we should not do that.
But on the other hand.
In this case, well, he's saying, I don't know if I'm using Portobf or not, because I'm using OpenTelemetry.
And OpenTelemetry is using, what if I does.
So, he's…
The question is, this cleanup needs to be done at some point, but it's unclear who should do it and where.
So…
Doug Barker 00:44:01 We… do we have a, a memory check test in CI? Because I'm wondering if we're…
Not seeing this.
NCI for what reason, because I don't recall that we were calling this shutdown anywhere.
malff 00:44:14 So we are not calling this shutdown, this is for sure.
Unless we are calling it indirectly, if we call it another API that does this inventory, I don't know.
In CI, we have some Valgruent builds, but I've never seen them saying anything, so I wonder…
I'm not even sure if we properly detect leaks, or if magically we have no leaks at all whatsoever.
So, maybe that would explain why we've never seen things in CI.
Also, in CI, the only place where we actually use portal buff is the functional tests for the HTTP exporter.
Because everything else is running unit tests, mocking things.
So, there is only… there are only a few, very few places where we actually talk to a real,
What'll be back-end.
And…
Doug Barker 00:45:21 That makes sense.
malff 00:45:22 Yeah, so maybe those tests… those tests are much likely not executed on… under Valgrain, so if we have a leak there, we will not notice.
Doug Barker 00:45:36 Makes sense. I think we have an example that runs the HTTP exporter, maybe we can run that under Valgrun and see if it reports anything.
malff 00:45:45 Yep.
So… detecting it in CI is one thing, but in any case, I don't think we should,
Advert call, because… It's really touching a global resource for the entire Portable Buff Library, so…
That should most likely come from the main application itself.
So I guess it becomes a matter of documenting and tell people that they should do that.
I guess we can take it because it's a valid issue.
Most likely, it will be… Something to document.
Okay, so I think that's it for…
new issues, I haven't seen anything else change recently.
Doug Barker 00:47:08 There are a few, topics that came through, Mark, on the discussions panel.
malff 00:47:13 Oh, yeah.
So, shame on me, I never go there, because the way the UI works in GitHub, I mean, if I know the numbers change, I go there. If I don't see anything there, I never click there, so…
Okay, so some question on latency…
I think the main issue first is to decide whether this is synchronous or asynchronous.
If I'm using synchronous counter and flooding them, then that's,
it's not likely to scale, I mean…
Incrementing a single counter means emitting a metric in no TLP.
You do that a thousand times, you have a thousand events right away.
Doug Barker 00:48:22 I don't know if it was the same person, but there's also a question that came through on Slack related to finding the bottleneck in the spin lock, so it seems like a.
malff 00:48:32 Yeah, it seems, seems very related, yes.
Yeah, I noticed that one on Slack and forgot to reply, but yes, it's,
Same issue, really, whether to use synchronous or asynchronous metrics to start with. And then, depending on how many metrics you have, then…
But all the way of force.
Depend on that.
Okay, so I guess… Yeah, we can reply that the first recommended way is to use asynchronous metrics.
Especially if it's, if it's high frequency.
Doug Barker 00:49:14 Makes sense.
malff 00:49:21 Okay.
So for PR's recent things, so, someone wants to…
The badge… where is it?
some… Some badge that says that, we are maintained, and
We are looking good, things like that, okay, why not?
So, earlier approved it, please take a… take a look if you want to, and
I will… if no one has any comment on that, then I will merge it.
The second one is from Ovent. This is to address a failure that we have in unit tests sometimes.
edge conditions, some… some tests can fail, in CI.
And when that happens, it's typically a test that, exports two spans.
So there's a parent and a child span and the test to make sure that they are related and whatnot.
But, the test uses, batch… Span Exporter.
And it just happened that the batch exporter triggers when only the first span is available. So there is one exporter with one span.
And then a second export with a second span.
In some cases, while most of the time, the export export to, the two spans at, in the single, same export.
So this changed the test output and the test condition, that fails.
So… This was fixed for another issue in Zipkin, and
by a new contributor, and now Owen also looked at that for the HTTP exporter tests.
I haven't looked in detail yet, but this is… So, yeah.
We export the… we expect the exporter to be cooled once, while this is, inv…
This is the typical case, but what can really happen is that the exporter can be invoked multiple times.
So the test is accounting for that.
And in any case, this is only touching the test code, it's not touching the SDK or export of themselves.
So I think it would be, fairly, trivial to,
To merge, and low risk to merge anyway, because it's only touching the test.
loaded.
Try to take a look at that one in detail.
If you… if someone was suck at it also, that would be great.
Then, do we have a sedentary, thing, so…
Great PR, especially for the… for the report, which is quite nice.
One thing, I noted is,
We have a file that contains all the ceiling tidy settings, so I was wondering if this part can actually move inside that .ceiling tidy file instead.
Doug Barker 00:52:54 Yeah, it, it,
is supported, so I just need to figure out what the right syntax is to get that regex to work, so I was struggling with a…
malff 00:53:03 That a little bit, but it is.
Doug Barker 00:53:06 Something that's supported should work.
malff 00:53:08 Okay.
And apart from that, I don't have any other comments, so…
I think the… what we should do is first merge this one, so that we can see the…
the CI failures, and the cylinder report.
And then, as many PRs as needed to fix things,
Piece by piece, to just decrease the number of issues.
the same thing, the same way we have done that with, serum tidy in the past, or include what you use, and those sort of things.
Doug Barker 00:53:53 Sounds good.
malff 00:53:55 Okay.
So yeah, thanks for… thanks for the PR.
It's still drafts, but I'm assuming it should be very close.
Doug Barker 00:54:15 Yeah, I'll try to finish it up, if I get some time, maybe this, coming Sunday.
malff 00:54:20 Okay.
Tom, I saw that you also fixed an issue in baggage, so, this thing…
Looking… there's no link, but looking at the baggage spec, this thing is actually legal, and a couple of other factors are legal.
Tom Tan 00:54:46 Yep.
malff 00:54:47 So… Where is it?
Yeah, so I saw a way to fix that.
the PR looked okay to me, so, what?
I don't see anything else needed, so I don't know why…
is still in draft? Were you waiting for CI to complete, or things, something like that?
Tom Tan 00:55:14 I was trying to, like, to look more into that spec, but I think it is mostly, I think, okay, yeah. I will publish it soon.
malff 00:55:22 Okay, so, yeah, I will review it.
The only thing we may add is just a comment and the URL pointing to the spec, so it's easier to review the code itself.
Okay. When having the spec on… Oh, horrible.
But otherwise, yeah, it's, I first… I took a quick look earlier, and it looked okay to me.
Tom Tan 00:55:48 Okay, thanks.
malff 00:55:59 And then, this is ordered already,
Steel draft, and routine detail and learn.
So this is… so he's a new contributor, looking at a lot of things at once.
In this case, so…
There is an issue in general, I think, in the CPP code, is that we claim nor accept in many cases.
But there are still in tidy issues detected on that, because sometimes we claim no except, and yet still have code that can have an exception.
So… Overall, my gut feeling is that we need to do some…
Overall, some review of No Exception all over the place, and decide what to do with it.
Or, in some cases, it may not even be feasible to claim no exception, given that we use unique pointers and shared pointers.
But themselves do need to allocate memory anyway.
So, it's a, it's a bigger issue. I haven't looked at this, this fix yet.
And, other things are quite old. So this…
Where was it? Okay, so this is from our aunt, getting older, also.
But, it's mostly some build issue with CMEC, and
scripts related to that, I think.
So, I… I don't know… well…
I usually don't do things like this with CMake, so I don't know exactly what's going on there.
Duke, could you take a look at that, if you… Beautiful.
If that sounds like something you can… Can't comment on?
Doug Barker 00:58:23 Yeah, I left some comments. I think… I don't know if you guys had a chance to discuss it, but I think it's worth discussing. Do we want to try to support? Given all the challenges with Windows DLLs, is this a build configuration that we want to invest in and support?
Because like I said, in one of my comments, I don't even know if we're able to test this, or are currently testing, you know, building, like, gRPC as a shared library, because that's something that, that,
for Windows, they explicitly call out and saying, like, it may result in undefined behavior, and they, A, support it as a best effort.
malff 00:59:02 Oh, gRPC itself is saying that?
Doug Barker 00:59:04 Yes.
malff 00:59:06 Oh, okay, good enough.
Doug Barker 00:59:14 Yeah, so I made a comment on this one with the.
malff 00:59:16 wins.
Doug Barker 00:59:16 to that, that, comment on GRPC. So I think, I think part of this,
PR was to also support building GRPC and linking it as a DLO, but I think
Owen mentioned that he could remove that, so we don't do that on Windows, but I think the reason that GRPC is saying that is probably because they're also running into similar issues, like what we've run into, and then, you know, I don't know if the protobuf,
Maintainers are… are… Making similar,
comments, or if they're fully supporting, you know, shared libraries on Windows.
malff 00:59:54 Oh, that's that?
Doug Barker 00:59:54 may be one of the challenges why the GRPC team has kind of decided, you know, they're not going to do that.
malff 01:00:01 Okay, yeah, good to know, then.
And yeah, well, the other thing is, before looking at shared libraries with JRPC and things like that.
We have so much cleanup to do up front with the OpenTelemetry CPP DLL itself.
But we may want to start with our own library first.
Okay.
Doug Barker 01:00:31 Yeah, that was… that was my feeling as well, so I think, you know, I could add some more comments here, but I think there's a lot… this type of change makes kind of a commitment, you know, to supporting
this particular build configuration, and one, I don't know if we're testing it fully in CI, and two, you know, I don't know if it's something that, if we are able to test, that we'll be able to make any kind of guarantees about, given that all the other libraries are not guaranteeing support for this.
malff 01:00:57 Okay, yeah, good point.
Okay, I will take a look at the comments and the details, but yes, it's…
Once, as usual, even when we say, hey, don't use that, it's unstable, or whatever, people use it anyway, and then complain that it's not working right away.
Like, some people are complaining that ABIV2
I don't remember where I saw that, but someone was actually, oh.
Building a shared library with ABI V2, And… when it's…
not recommended, because by definition, ABI V2 can't change.
And once you have a shared library that changes, then what's the point to have a shared library? They're going to blow anyway.
But, yeah, once… the bottom line is, once we do something, just people take it for granted and run with it without even questioning.
Or without looking at the fine print, saying.
It's experimental, it will take some time to stabilize, don't use it yet.
So it could be one of those. If we… if we claim that we are
Supporting this bill, then people will, will try it and Possibly get into more issues.
Okay.
So, yeah, this is some, cleanup which is related to selling tidy in the API, I think.
So that guy, identified some… some places where we could be more efficient.
Unfortunately, this is in the API, and that can break the API itself.
So, the… the proper way is to…
do that only in ABI V2, and do the cleanup in ABI V2, because that one we can change.
And… So, that PR was written before the upgrade to Silent ID, but it just happened that,
the items which are fixed in that PR are exactly the same one as complaints from ceiling tidy in context, saying, well, you should not pass a parameter by value, try a const reference, things like that.
So this is the… exactly the same thing he fixed.
So… If we commit to clean up, everything ceiling tidy reports,
We will have some changes there, and…
So I think we can start and do them.
And varsity's, older with no…
No recent changes, so…
Any specific PR issues you want to discuss? And I see it's getting late already, so…
Tom Tan 01:04:26 No, for my part.
malff 01:04:28 Oh.
Boom.
Looks like we… we lost two, so, okay.
Okay, well, it's getting late, so we can… we can finish the call now. Thanks, everyone, for joining, and
See you soon, Vin.
Bye now.
Tom Tan 01:04:48 Later.
Yeah. Bye.
Ehsan 01:04:51 Thank you, bye.
malff 01:04:53 But…
