SIG: .NET Auto-Instr SIG
Date: 2025-08-20
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/W32ViZKJFgu0DyGxPJQEXOW-vAao5OvAV1IEFCVsO_aMQdAmsqoXYX-a_Zgs7E2F.swf8Pa5jUVEBnBJp
============================================================

## Zoom Recording Transcript

**Zach Montoya** 01:35 Hello, welcome back.
**Piotr Kiełkowicz** 01:39 Not sure, I wasn't here last week. Maybe you're back last week. Hey, Zach, yeah, I'm back here.
On Monday, to be honest, to work.
**Zach Montoya** 01:49 Nice.
**Piotr Kiełkowicz** 01:52 Too short.
As always.
**Zach Montoya** 01:57 As always, yeah.
How long were you, … how long were you out? It was, like, 2 weeks?
**Piotr Kiełkowicz** 02:03 Two weeks, yes.
**Zach Montoya** 02:04 Got it.
**Piotr Kiełkowicz** 02:05 But it is kind of second longer break in this year, so it's not bad.
**Zach Montoya** 02:12 I've got a… plan a…
Two-week vacation at the end of the year for me, so I'm looking forward to that.
**Piotr Kiełkowicz** 02:19 Nice. But Rash, have much longer vacation than me.
**Rajkumar Rangaraj** 02:25 True, true.
So I haven't traveled or taken a longer vacation for the last 3-4 years. So this is the first time I took it. So I thought, like, let me try, and yes, I'm not even taken a vacation, which is more than 2 weeks. So that's why I went ahead and
Taking the bigger one, yeah.
**Piotr Kiełkowicz** 02:52 Nice.
**Zach Montoya** 02:53 Yeah, that's nice.
**Rajkumar Rangaraj** 03:00 Yeah, I think something has changed, beer… follow us!
Moved to a… like, I'm out of the maintenance status, if I understand correctly, when I wasn't there.
**Piotr Kiełkowicz** 03:13 Yes, Paolo internally inspired Paolo NUF to collect our team, end of a year ago?
**Rajkumar Rangaraj** 03:19 Okay.
**Piotr Kiełkowicz** 03:21 And…
he doesn't have enough time to work on .NET stuff, but if we need some advice from him, he's always welcome to help, but he's very limited in time.
**Rajkumar Rangaraj** 03:35 Okay, got it, yeah, the collector should keep them busy, like….
**Piotr Kiełkowicz** 03:40 Yep.
courage plus se… present, because I need to drop, kind of, within 15 minutes, probably.
**Rajkumar Rangaraj** 03:57 Sure, Let me see… Just… give me a second here. I was not prepared for it, like…
Hope I'm sharing the light.
window.
**Zach Montoya** 04:20 Yep. Yeah, I see the agenda.
**Rajkumar Rangaraj** 04:22 Hmm.
So, Pietro, I see you have, … Like, two topics for discussion.
**Piotr Kiełkowicz** 04:31 Yeah, so we need to finally, …
decide what to do with SQL Client Library, the legacy one.
there are….
**Rajkumar Rangaraj** 04:40 Okay.
**Piotr Kiełkowicz** 04:41 two or three solutions on the type, and we need to recommend something to Gordon.
I think.
To… to proceed.
The first option was to….
**Rajkumar Rangaraj** 04:57 Oh, Pietro.
**Piotr Kiełkowicz** 04:58 before….
**Rajkumar Rangaraj** 04:59 Just before you go, can… I was just… being two months out, like, lost most of the knowledge. Can you just fill in why this is an issue, and then speak about a solution for it?
**Piotr Kiełkowicz** 05:10 Okay, the… what is the issue? Old SQL client included into .NET Framework basically does not share
The… in the event details, information about the…
query. It is intentionally, in the code.
Checked if it is kind of standard text query and replaced by string empty.
And due to this, we are not able to… create… Good Span name.
And we are not able to populate dbQuery text.
or DB statement in older semantic conventions. And it leads, for at least Splunk and the Elastic to problems with presenting correct data on the UI, and our customers are complaining.
**Rajkumar Rangaraj** 06:06 This is a much bigger issue, so…
I remember the SDK side, the classic application inside SDK, we had taken care of it, so I don't recall how and, …
how it's been done. I need to take a look. So, looks like earlier it was not a part of the .NET Framework. I think recently it got into .NET Framework, is that correct?
**Piotr Kiełkowicz** 06:33 It was….
**Rajkumar Rangaraj** 06:34 It was.
**Piotr Kiełkowicz** 06:35 And I think it was.
**Rajkumar Rangaraj** 06:37 Okay.
And do they have any….
**Piotr Kiełkowicz** 06:41 Or actually, there are three versions of a square client, and one is kind of legacy, I'm not sure if it is included in framework. I suppose yes, but I…
I can… I have some room here.
**Rajkumar Rangaraj** 06:56 Any information available.
**Piotr Kiełkowicz** 06:58 But…
One of them is problematic in this case, as I've described. The source code is even linked in the longer description.
And we have, free solo… free potential solution.
One of them is purely bytecode instrumentation, and we'll… and we will drop a dependency on the SQL client.
It is bad because we need to maintain similar, or more or less the same instrumentation in two places.
The second part is to keep existing SQL client instrumentation for most cases, but for the problematic library instrumentation, we could use, kind of, bytecode instrumentation and create spans on our own. It is kind of…
I'm not sure if it is better than the previous case. And the last, not but least, is to modify the ill code for
the… for this library, as Zach proposed.
In this comment, and just remove The sanitization of… DBQuery.
content.
**Rajkumar Rangaraj** 08:17 How does that happen, the standardization? Is there an environment variable or something at the framework level to get that done?
**Zach Montoya** 08:26 No, so, from here, you can actually see where those replace arrows are. Essentially, in those branches, it'll just, …
it does a simple if-else, and if, in the case where, it's a normal statement, it'll just pass in string empty, so we don't see any contents. But otherwise, if it's a stored procedure, it'll pass in that statement, and so we would just…
pass in that command text. So, like, I guess a couple lines after that is where we… it already does get command text, so we would just replace the string empty with getting command text, and that would be… give us, the statement that we need.
**Rajkumar Rangaraj** 09:06 Got it.
**Piotr Kiełkowicz** 09:08 I think it should be kind of feature-flagged.
**Zach Montoya** 09:11 Hidden by the feature flat.
**Piotr Kiełkowicz** 09:13 Because we can expose the sensitive data for other listeners. It is unlikely But it's possible.
But it is the cheapest option for the long-term… from the long-term maintenance perspective.
**Zach Montoya** 09:34 Yeah.
It's, … For me, it's… I… that's my preferred approach, just because it's, …
Yeah, it's only maintained in one place by us, and it's very… it's a very small, targeted change. It does have the effect of it will pass that information to any listeners, but as long as we have that feature flag,
It, you know, all the logic to maintain that will just be in one place.
It should be pretty minor, just, swapping some of the instructions.
**Rajkumar Rangaraj** 10:09 I acknowledge that, fact. Like, I think this… the… this is the option which will make it simpler. The other things is that we… we need to take care of so many other things in the first two approaches, so this may be simpler. Peter, what do you think about that?
**Piotr Kiełkowicz** 10:26 Yeah, I agree. I've thought… I… I think one… about one other option is to kind of
Create bytecode instrumentation to fetch this… …
DB statement, and try to inject into…
Instrumentation package, but it can be hard, because it is kind of…
async method, and there is no easy possibility to…
to merge them together. Chris mentioned that we could leverage concurrent dictionary, but…
For sure, we can expect some… issues.
In such cases.
So, yes, I agree that the solution proposed by Zach is the best option.
**Rajkumar Rangaraj** 11:24 Cool, then.
Do you plan to drive it? Like, the changes?
**Piotr Kiełkowicz** 11:31 Steve… Steve, ….
**Rajkumar Rangaraj** 11:35 Okay, Steve.
**Piotr Kiełkowicz** 11:36 Steve is going to drive, but he needs the recommendation.
**Rajkumar Rangaraj** 11:41 Got it. Which way….
**Piotr Kiełkowicz** 11:43 You should implement it.
**Rajkumar Rangaraj** 11:45 Okay.
**Piotr Kiełkowicz** 11:47 So, I will make a note probably tomorrow morning, and share that we agreed on….
**Rajkumar Rangaraj** 11:52 I don't have the context… yeah, I don't have the context to summarize and put a sign note here, so I wanted your help here, just to summarize and help with a sign note, yeah.
**Piotr Kiełkowicz** 12:08 And the second one, some time ago, Yevgeny opened an NPR related to file-based configuration.
We have discussed a lot of…
things, including contribution to the OpenTelemetry SDK, but for us, it is kind of…
Time-sensitive, and we have tight schedule to deliver something like this.
And our proposal is to create just file-based configuration in auto-instrumentation right now.
maintain it for a while, and when the SDK will be ready, we can just switch our implementation and bring everything from the upstream.
The PR is huge right now, so my proposal is to split it into smaller chunks.
The first one should be vendorICRM.net, … Parser, or something like this?
And include into our beat pipeline.
Because otherwise, we'll be kind of in this nightmare dependency hull, and…
it is the best option I see.
**Rajkumar Rangaraj** 13:20 I did not take a look at the previous PR. Is that a precedence that we have sorted out already on this?
File-based and the environment variable, all that.
Stuff.
**Piotr Kiełkowicz** 13:33 High-based configuration is a new feature developed on the OpenTelemetry level. It is on the beta state, or something like this.
So, we can create…
I think we have agreed some time ago about the environmental names to leverage the antennabis. So, we should be able to implement it in the beta stage, for now.
**Rajkumar Rangaraj** 14:00 But… So, …
if I understand, what's the plan for the release on this one? So you don't plan to include it as a part of the stable version? Because you said we will keep it for some.
**Piotr Kiełkowicz** 14:15 No, we have a lot of non-stable features in stable releases, so we have just need a clear description that it is a better feature, and
In the future, you can expect changes in the schema file, or something like this.
**Rajkumar Rangaraj** 14:34 Makes sense.
**Piotr Kiełkowicz** 14:38 Cool. So, as if Guinea is on PTR, couple next weeks, I will be probably working on to…
Push it towards two mergers.
**Rajkumar Rangaraj** 14:48 Cool.
So…
The third topic is from my side. I just opened this, like, 10-15 minutes before the SIG. So, the out-of-process forwarder is ready now.
So we can do the first beta version of it, and try to integrate… start the integration with the .NET Monitor, and start adding, the few codes to the .NET Monitor also.NET Monitor does not need… we don't need to add a lot of code there, because a lot of things… the logic relies in this SDK itself.
As we know.
So, I'm planning to create the package. We already have the pipeline and everything set up, so the remaining stuff are the changelog and the versioning part, which I… we need to take care and publish it to NuGet. If I have a thumbs up from both of you, I can start working on this one.
**Piotr Kiełkowicz** 15:50 I would go with alpha version, … Instead of beta?
At least for the first round.
**Rajkumar Rangaraj** 15:57 The only issue is that the .NET monitor will not accept the alpha version.
**Piotr Kiełkowicz** 16:04 So… Understood, so go with beta.
**Rajkumar Rangaraj** 16:07 Yeah.
So, anyways, like, there is no customers at this point. Even if we release, it's going to be for the consumption of the .NET Monitor. At some point in time, we can think about if we need to rely upon .NET Monitor, or we can make this complete in-house
best solution and everything. So, but we have the forwarder ready for us.
So, so I don't know that .NET… there is a big change in the Microsoft recently. I don't know what's the story for the .NET monitor with that change, so I have to just see, what… how that has impacted, the changes before I left.
**Piotr Kiełkowicz** 16:49 So, I would suggest just to release OX version, not 1-0.
**Rajkumar Rangaraj** 16:54 What is that solution?
**Piotr Kiełkowicz** 16:56 0.1 or 0.omething, not going to 1 0.
**Rajkumar Rangaraj** 17:01 Hmm….
**Piotr Kiełkowicz** 17:02 Immediately, if it is possible from the .NET perspective.
**Rajkumar Rangaraj** 17:08 Yeah, that makes sense. So, I'll have a conversation with the .NET monitors team if they are ready to accept that. That would be the safest approach over here.
Cool. So I've done, but just to give you a slight background about this, I've done the complete testing with the out-of-process and the telemetry flows, and in the Ashwa dashboard and the other, the OTLP-based service, we could see every correlation and everything is working with this one.
So, it's not a, …
like, and completely covered by tests now. I think we have, like, 90 plus percentage of test coverage. The only thing that's missing is now the integration test. So unless I add some… we add something to the .NET monitor part, it's very difficult to have the integration test completed over here. So, that's why
we have to guess everything, what's going to happen in .NET Monitor and write an integration test, so that's why that part is missing at this point, for us.
**Zach Montoya** 18:15 And what's the, plan for the GitHub release part? Will we just have an independent tag?
an independent, like, release, like, right now we only have just, like, V1.12, V1.11.
What are you thinking for the GitHub release part?
**Rajkumar Rangaraj** 18:34 You… do you mean, like, adding a release label over here?
**Zach Montoya** 18:39 Yeah, I'm wondering if… are you planning to add… No, but….
**Rajkumar Rangaraj** 18:42 And ….
**Zach Montoya** 18:42 Yes or.
**Rajkumar Rangaraj** 18:43 say it's not for a direct customer consumption at this point in time. Like, don't want to advertise too much also about it at the same point. So, probably want to keep it very simple and take the bits out of it for the consumption.
**Piotr Kiełkowicz** 19:01 rush. The question is if you should tag. I think you should create tags, On your branch?
**Zach Montoya** 19:07 release.
**Piotr Kiełkowicz** 19:08 Without releases, and maybe out of process dash something, as we have on contribute repository.
**Rajkumar Rangaraj** 19:17 That's a very good call. Yeah, we should maintain the tag.
**Zach Montoya** 19:29 How's it done in the, SDK repo?
**Rajkumar Rangaraj** 19:33 It's there in the contrib repo, yeah. SDK repo also… SDK repo works completely different, even if you need to release OTLP exporter, you will release all the packages together. So, that way, we wanted to reduce the maintenance burden in the SDK, and all the pipelines have been set up like that.
**Piotr Kiełkowicz** 19:54 And the contract repository, you can create, really, each package, or set of packages, more or less independently. There are kind of…
which… there is a couple of them which needs to be released together, like ISPNet and ISPNet IIS module, or whatever it is called, and they are tightly coupled by the same prefix on the tag.
**Zach Montoya** 20:22 Got it. Yeah, I see that now. I see that there's basically a tag for the package name and then the version. Okay.
Cool, yeah, no other questions on that one.
**Rajkumar Rangaraj** 20:37 ….
**Piotr Kiełkowicz** 20:39 Sorry, guys, I need to drop right now to another meeting.
Thank you.
**Rajkumar Rangaraj** 20:46 Thanks, man. Yeah.
Jacques, I don't know how much it would help, like, we both going through this one, because the work has been done by Pyotr, like, and his team, because I see a lot of issues being created in, the… related to the file-based configuration over here.
**Zach Montoya** 21:14 Yeah, I think… yeah, I think all of that is an effort to break down the work.
of… because the file base contains a bunch of them. Oh yeah, I see. Yeah. So there's, one file base, implement file base configuration, which is number of.
**Rajkumar Rangaraj** 21:30 Oh yeah, this.
**Zach Montoya** 21:31 And all those are sub-issues. So, yeah, I think those are fine, and we can just monitor those.
**Rajkumar Rangaraj** 21:38 Yeah, and every other issue is rolled, and we had a discussion about this one also.
**Zach Montoya** 21:44 Yeah.
**Rajkumar Rangaraj** 21:45 I might need to create a milestone for the out-of-process here, and slightly arrange it, because right now it won't fit in anywhere.
we won't be able to move it out, so I'll try and see what can be done, and how well can be managed.
**Zach Montoya** 22:02 Okay.
**Rajkumar Rangaraj** 22:03 So, I don't think we have anything else apart from that. It looks good, everything else here.
**Zach Montoya** 22:11 Yeah, yeah, I think we're… I think we're probably good for today. I'll take a look at some of those PRs, …
Over the rest of the week.
**Rajkumar Rangaraj** 22:21 I think this is one of the things. Yesterday, I saw you in the SDK, like, SIGO, so….
**Zach Montoya** 22:29 Yeah, I'm trying to stay up-to-date on the SDK and see if there's anywhere for me to… To help.
I haven't historically had a lot of engineering time, but I'm trying to
trying to build the case to get more time to work on input telemetry, so I'm just trying to see if there's some good opportunities for me to contribute.
**Rajkumar Rangaraj** 22:49 Sure.
So this is something I'm…
kind of, like, serious discussion, it ties up to that. If there is a log bridge API, we don't need to do anything over here.
**Zach Montoya** 22:58 Yeah, exactly.
**Rajkumar Rangaraj** 23:00 Yeah, so that's what I need to do, some groundwork for this week to see
Because the earlier I had a conflict with the, the,
the current features that have been added as an experimental in the SDK, the, …
conflict is, like, every API comes from the .NET. Why do we need to,
kind of bridge API to the SDK instead of taking that to the .NET layer itself, because managing another new API is a maintenance burden in that repo. So, just trying to keep less maintenance stuff, and if something is a native part of .NET, it makes it also easier, like.
people can integrate easily and rely upon SDKs just to export things. So that's what I have it in mind, but I don't know whether .NET team will be very much interested in converting the… some other vendor's log to the… or providing a contract for that, because they already have a contract of
iLogger, so I don't know how much interest they are going to show it in that space. So that's where it's pending upon.
**Zach Montoya** 24:10 Yeah… Yeah, that's true. I…
Yeah, I wonder what that'll look like, because I know that other libraries, like, it's very easy to just add an iLogger dependency, so…
Ideally, we wouldn't need to add any more dependencies, but for something like serialog or N log, where they… those are supposed to go back to OpenSometry, …
Yeah, I guess that's for the .NET team to determine if there's gonna be a new API or something there.
**Rajkumar Rangaraj** 24:37 Yeah.
Let's see how it moves, like… Okay, that's all I have at, here.
Thanks, Jack. See you. Bye.
**Zach Montoya** 24:46 See you later. Bye.
