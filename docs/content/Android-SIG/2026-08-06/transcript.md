SIG: Android SIG
Date: 2026-08-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:06 Hi, Jamie.
putting a link to the new, Zoom invite, Zoom meeting, into the channel, just in case people have the old one, as many of us did.
**Jamie Lynch** 01:34 This is the… this is the first one we've done on a Thursday as well, isn't it?
**Jason Plumb** 01:38 It's true.
**Jamie Lynch** 01:39 Let me…
**Jason Plumb** 01:40 Yeah, we'll see what shows up. I mean, we all voted yes on this time slot, but people get busy, and I get it. It's the middle of summer as well, so…
**Jamie Lynch** 01:48 Yep.
I know that Hansen's out, he's a company thing.
**Jason Plumb** 01:53 Okay.
Was the… is… is the Embrace headquarters in… Like… Vancouver?
**Jamie Lynch** 02:05 I guess… We don't really have a HQ, but probably the most folks are based in LA. So, yeah, basically a lot of people are in LA right now.
Just for a meet-up thing.
**Jason Plumb** 02:20 Cool.
That's a bit of a far trip for you.
**Jamie Lynch** 02:28 Low bet, yeah.
**Jason Plumb** 02:30 And you've got a baby!
Well, let's give it another minute or two, even though we're… we're well into it. Hey, morning.
**João Oliveira** 02:39 Redhawks.
**Jason Plumb** 02:40 Abe.
**Jamie Lynch** 02:41 Nope.
**Jason Plumb** 02:49 Yeah, there's a couple of items front-loaded into the agenda.
Yeah, Ben's joining a little bit later, it sounded like David was also gonna be late.
But we can probably jump in on this one, so… I looked at this one recently, like, yesterday, I think, or maybe the day before, I forget.
Yeah, so I think he probably has some input to give on this, but… just in general, when I was looking at it, I was like, man, there's a bunch of Copilot stuff that's still just open, and even if it's outdated, I guess probably just resolve it, you know?
And…
**Jamie Lynch** 03:29 Those are the first item on the agenda.
**Jason Plumb** 03:32 It is. Yeah.
**Jamie Lynch** 03:34 I don't think there's a screenshot, FYI.
**Jason Plumb** 03:37 Oh, my bad, yeah, whoops.
I'm just talking… talkin' like you can see it.
There we go. Hi, Cesar!
**Cesar** 03:46 A…
**Jason Plumb** 03:47 Welcome to Thursday. Thursday's here.
**Cesar** 03:51 Yeah.
**Jason Plumb** 03:56 Anyway, yeah, the… so this is the one that… I think David said he was gonna be late, but Yeah, maybe, you know, maybe it's worth updating some of the contributing docs to just say that we have Copilot reviews now, and that we want those to be resolved.
Like, resolving co-pilot reviews is a strong signal to other maintainers, actual human maintainers, that they should look at it, so I'll take an action item on that one.
**Cesar** 04:25 They have been, surprisingly… Useful.
Lately, the, co-pilot reviews, so… Yeah, I like when those are resolved.
**Jason Plumb** 04:37 Yep.
**Cesar** 04:49 By the way, did you guys get, like, a Linux Foundation page?
when clicking on the Zoom… to join…
**Jamie Lynch** 04:58 Yeah.
Boo.
**Jason Plumb** 04:59 Yeah.
**Cesar** 05:00 Last time I say that, so that was a bit odd.
**Jason Plumb** 05:03 Yeah, so I'm sure… hopefully you can see my history here, but yeah, I think it lands you… And then, like, forwards, but yeah, if you're not logged in, I think it forwards.
I think you do have to… I think you do have to have an account, I think you do have to be logged in. Or maybe there's a link to join as guest. I think someone on the client SIG.
joined as guest, and they were like, can I just join as guest forever? And I was like, that's fine by me.
**Cesar** 05:27 I confirmed that I think we can join as guests, because that's.
**João Oliveira** 05:31 Just today.
**Cesar** 05:33 I do probably have an account that I don't remember.
Need to check them.
**Jason Plumb** 05:39 Okay.
Yeah, I think I had to create one. Or no, I tried to create one that said I already had one, probably from… I don't know, KubeCon or something else.
Okay, well, the other folks are also joining late, maybe, looks like.
Cesar, I think you did the most thorough review on this one. Do you still have some hangups on it?
**Cesar** 06:09 I was waiting for the co-pilot, yeah.
**Jason Plumb** 06:13 Okay.
**Cesar** 06:13 stuff to get resolved, but I… I think the only comment that I had was that the, the… the… I think the… the changes that David added after my comments were to flatten Three, instrumentation modules, All as part of the same instrumentation folder.
**Jason Plumb** 06:39 Yeah.
**Cesar** 06:40 And it's slightly different from the one I suggested, which was to have the tree… Related modules within a single view.
folder.
**Jason Plumb** 06:53 Right, so you want to see… you want to see instrumentation view… Is that right?
**Cesar** 07:00 I mean, yeah, that was my suggestion. I'm just curious why he went with the, flattened… way, which… It's probably fine, too,
**Jason Plumb** 07:10 I thought you had a diagram of this, too.
**Cesar** 07:14 I, I did.
**Jason Plumb** 07:15 Yeah.
**Cesar** 07:16 Somewhere in these comments, yeah.
**Jason Plumb** 07:19 I think I'm with you on that, though. I think… here it is, yeah. Yeah, I like this. It'd be cool to understand… Hopefully he'll join, and we can understand why he didn't go that way.
The thing that I thought I saw… Is that… is it common that it doesn't have the publish?
One of them… One of them doesn't publish.
Wait, I thought it was in the gradle here.
Yeah, so…
**Cesar** 07:52 Yeah, yeah.
**Jason Plumb** 07:52 The Common doesn't publish, so… If you consume one of the other two, then you don't get common, and that's a problem, right?
**Cesar** 08:01 Yeah.
**Jason Plumb** 08:02 Yeah.
So I'll just make a quick note here, too.
**Cesar** 08:11 I thought you mentioned that, or maybe I'm…
**Jason Plumb** 08:14 I mentioned it, but I'll just put it on the exact line, that way it's really clear.
Okay, anything else to talk about on that one? Probably, if David shows up, there'll be more, but…
**Cesar** 08:50 No, for now.
**Jason Plumb** 08:51 Alright, let's… let's run ahead on Ben's.
So, he wanted to talk about schemas a little bit. Yeah, this came up earlier in the week.
I think right now, we don't set any sort of schema versions, and the… the goal with these is to… if you're… if you're a backend getting… data from… hundreds or hundreds of thousands of telephones, then it might be nice to tell what version of the data you're getting, not just, like, what version of the app is running, but, like, how the data are formed, you know, once they hit your ingest, so… The schema's intended to be… A hint, or at least a strong idea of what version of the schema you're on, and I think we don't set it at all. I think I even created an issue for this.
**Cesar** 09:48 I think I saw… yeah, sometimes it's discussing the clients, was it?
**Jason Plumb** 09:53 Yeah, so I created this one, let me just link to it, he might have already linked to it.
Whoa, that got bold.
Okay, well, we can hold off on that, because, I mean, I think this is important for them. It's probably important to other vendors as well, to… to have that stuff in there. My understanding is that the Java SDK doesn't… Currently set it.
So we're probably getting no schemas. So schema… the schema version URL lives in two places. It lives on the resource.
But specifically, it lives on the resource spans, resource logs, and resource metrics.
And then it lives also on the instrumentation scope.
So the instrumentation scope can also have a schema version, and… I don't… I'm not entirely clear on why you need both, because they're kind of like… They're different layers of the onion.
Onion skin, onion wrapper, but… I don't know why both are helpful, or which one's better, and… Are they the same schema version? Are they different? I don't know what to put in there, but something.
**Cesar** 11:15 But I think it's great that we… talk about this, because I noticed… There seemed to be some movement around pay more attention to this schema version stuff, and it's probably related to An issue that we had with the, the same comps that we are generating in Auto Android.
that I think Jamie fixed, where they introduced a new, mandatory thing that you have to define the schema URL or something.
So that it can work, so that Weaver, Waiver, Weaver can work properly. So… I… I don't know where… Are we supposed to send that?
From, you know, in the telemetry.
I don't know if it's… that's… that's one thing I… I don't have clear.
You mentioned in the, in the scope.
As in… Because I know scope has name and version.
Or maybe I'm… Confused.
No, that's another thing, versioning. Yeah.
Yeah, no, I don't know about it.
**Jason Plumb** 12:41 So I think there's instrumentation… Go… Does that have… yeah, so instrumentation scope… so every piece of telemetry has an instrumentation scope that has created it, and that has a schema URL.
Yeah. So that's… and at least, I mean, that's probably part of the spec.
But that's what Java has, the ability to set. I bet you we only ever call it with this. Like, I think… I think any time we make an instrumentation scope, or we get a tracer, or whatever, we only do this, and then it passes null.
**Cesar** 13:19 Yeah.
**Jason Plumb** 13:20 Which is fine.
**Cesar** 13:21 I think so.
**Jason Plumb** 13:21 just, like, we just are not setting it, and I think that's pretty common in the instrumentation as well. And then the other place is, like, resource… there's something like resource… Yeah.
Resource… the Java.
I think this has a schema on it.
Yeah, so when you… same situation here, like, when you create one, you have the ability to pass in what resource you're creating it for.
What version?
**Cesar** 13:59 I see.
**Jason Plumb** 13:59 And I'm sure we're only calling it like this.
So those are the two places that I know of from the spec where that kind of happens.
**Cesar** 14:11 So maybe for the instrumentation, it's… if… In case it's adding some… Just regular attributes that may be different from the ones in the resource.
You know, there's the schema.
Which is kind of strange, then, I guess. A server will have to… Take a look at two broadly different schemas for a single… Events or something.
**Jason Plumb** 14:39 Right, so that's, like, I also don't know what the right thing to do is, and also, if we have… Like, should we be using our, like, our version, because our version has a declared dependency on other versions, and that gives you everything?
Yeah.
I don't know, actually.
Are we supposed to be using the version of the spec?
Because it's not just semantic con… it's not like semantic conventions URL, it's like schema URL, which kind of, to me, speaks more about the shape of the data, like the protobufs, right? Like… But I don't know the answer, that's probably a good spec question.
Or maybe just, like, do some homework. I also am not thoroughly familiar with that portion of the spec, but maybe Ben's done some homework.
**Cesar** 15:30 Since we're, Creating the CENCOM stuff in Auto Android.
**Jason Plumb** 15:37 Holy…
**Cesar** 15:37 At least at the… at first, we can just reuse the same schema across the whole autoantry stuff, and that's until somebody complains, probably, but I wouldn't see why.
**Jason Plumb** 15:52 Yeah, as a starting point, maybe that's better than nothing.
**Cesar** 15:57 Yeah.
**Jason Plumb** 16:16 Okay, well, I'm gonna jump ahead… in case people show up, and I'm just gonna mention a few, kind of, quick things. The first one being that, I did get an Android-related… I hope the schedule's out, I think it was supposed to be out today. They said don't say anything until the schedule's out, but I think they said today. I did get an Android-related talk accepted into KubeCon North America.
And it's kind of mostly talking about, like, what the project is, but also, like, how to use the DSL, like, from the agent. That's kind of the focus of it, is, like.
hey, we have this fancy new DSL, and we even marked it stable, and here's cool stuff you can do with it, so… That's happening in November, if anyone's gonna be there.
I, I…
**Cesar** 17:04 It won't, but it's nice.
That somebody will? From Andre.
**Jason Plumb** 17:10 We're gonna have to get you to the States at some point, Cesar. I know it's… I know it's a hard sell right now, given… given what's going on in this damn country, but Yeah.
Alright, the other thing I wanted to talk about, or one of the other things I wanted to talk about was… This nightly job, this thing… And it worked! Okay, cool.
The first time it didn't, and then it had a fix, so this should… Update the semantic conventions version that we're depending on?
And it should do that by a PR. Does anybody know if that PR got created?
Because I think we were at least one behind. Okay.
Do you know if I got merged?
**Cesar** 17:55 Yeah, I think it worked.
I think it's the second one.
**Jamie Lynch** 18:00 Yes, I got one done.
**Jason Plumb** 18:02 Cool. Okay.
And does the build pass? Look at this! Awesome!
Great.
And Jamie, you're gonna adopt this for Kotlin, you said, right?
**Jamie Lynch** 18:15 Yeah, yeah, I think I can just take what's hair.
**Jason Plumb** 18:20 Cool.
It's a little bit complicated, but… It's fine.
I guess. Until it's not… until it breaks. Okay. Well, thanks for looking at that one and talking that through with me, and then the other thing I've been doing incrementally that you've seen already is, trying to get us basically caught up on all of the new way we're doing semantic conventions, and at the end of the effort, we will no longer have a dependency on the Kotlin conventions, because we're generating them all locally.
So… I think this one is the last one in the chain, but it doesn't finish the work. There's more that need to follow this one.
But I've been kind of doing these. So yeah, this one needs to come out of… I need to rebase this one and then come out of draft, but they're all basically doing the same thing, right? They're… they're just, dropping the dependency on this, and then depending on the SimConv module.
And so we get the events and the constants in our own… in our own module from Weaver.
So that's still a work in progress. I think there's a few more places that still use Kotlin, or a few more places that don't have correct event generation, but I'm hunting those down, and we're close.
**Cesar** 19:40 Thanks. I haven't taken a look at this one, because I usually just ignore drafts.
**Jason Plumb** 19:45 Yeah, exactly, that's fine. It just needs to be rebased, and then it will be smaller. So I'm trying to keep these small, you know. I'm trying not to do it all in one go.
**Cesar** 19:53 Thanks.
**Jason Plumb** 19:55 the pros and cons of that, right? The pros are it's, like, easier for people to review, and the con is I have to, like, do it piecemeal and do rebases, and they have this, like, stacked PR thing now, and have you seen this? They have this stacked PR feature in GitHub.
But when your first PR… when your first PR is from a fork, then it, like, screws up the whole stack. Like, it only works if you're working in one repo.
And I'm like, what?
**Cesar** 20:23 Okay, well, it's not enough for us, but…
**Jason Plumb** 20:26 No.
**Cesar** 20:26 Cool.
**Jason Plumb** 20:27 Mvp is what it seems like that they shipped, and maybe they'll fix it, I don't know.
But… Okay, those are my three.
Since we have a light agenda, I'll just see if this thing's on the schedule so I can link to it.
I think they… I think the schedule's up.
Yeah.
Probably observability?
Okay.
But they don't… Is it… Can I get a permalink? Oh, yes, okay.
Cool. Let's look at Vishwan's PR bump.
And without looking, I'm guessing this is about native crashes.
No. Okay, but it's related to that, because I think this fell out of that native crash work.
I haven't looked at this yet.
**Cesar** 21:40 Yeah, it's just about adding Android tests to the PR checks.
**Jason Plumb** 21:47 This is gonna make them even slower, isn't it?
**Cesar** 21:51 That's true.
I remember we used to have them, and we were… I think we removed them, or we moved them to a… to a nightly… Check or something?
**Jason Plumb** 22:04 That sounds.
**Cesar** 22:04 But, I… I don't, like… I will… I don't think it's that… I mean, have you seen the instrumentation… Java instrumentation tests?
Like, we are checks.
**Jason Plumb** 22:18 I have.
**Cesar** 22:18 I don't… I don't think it's as bad as that one, and… and I… I do believe it does provide Good benefits, so…
**Jason Plumb** 22:29 Yeah, it definitely does.
How… how bad… Sorry, how slow is it currently?
And I'm just looking at the main PR checks, right?
So, 19 minutes.
It's not the worst thing in the world.
**Cesar** 22:52 I think it's fine.
**Jason Plumb** 22:53 Oh, and actually, I don't… hmm… If this adds those… I think it wouldn't run on this PR. Is that true?
**Cesar** 23:03 Did it…
**Jason Plumb** 23:04 Do we know?
If it ran as part of this…
**Jamie Lynch** 23:08 Is it the Android Instrumented tests check.
**Jason Plumb** 23:12 Was it in… oh, was that one of the checks?
**Jamie Lynch** 23:15 Yeah, I think it's a separate check.
**Jason Plumb** 23:19 This one.
**Jamie Lynch** 23:21 Yeah.
I just assume so.
**Jason Plumb** 23:24 And that one took 8 minutes. Yeah, that's not too bad. That will grow as we build more of these, right? But that's cool.
Okay, and concept seems like a good idea.
Alright, it's got two approvals, I'm gonna merge it without reviewing it, because you all are very trustworthy.
So hopefully there wasn't anything where he was gonna say, don't merge it, I found a mistake!
So…
**Cesar** 24:03 We can always review it, but…
**Jason Plumb** 24:05 That's true.
**Cesar** 24:06 For now, I think it's fine, but…
**Jason Plumb** 24:08 Alright, so they wanted to know about the next release that contains… this stuff. Oh, this is part of crashed stuff. So, the last release… It was last week, so… it'll just be in our regular monthly, is the answer.
Inc.
A downstream Grafana retest is waiting on it. Well, do we… I think we still publish snapshots, right?
**Cesar** 24:36 But I haven't checked.
**Jason Plumb** 24:40 I think we do.
Do I have a tool that allows you to browse those? You know, they broke browsing of snapshots in Sonotype.
Let me see if I have this tool that I wrote one time, and by wrote, I mean… Use AI to code.
**Cesar** 25:00 That's fine, I think AI is pretty cool for CI stuff.
**Jason Plumb** 25:08 Let's see… Yeah, this thing. So, do we have Android?
No, but let's try it.
Is that the coordinate? No, that's… It would be here, maybe?
Maybe?
No?
Okay, fine.
I know.
Android Inc.
**Cesar** 25:44 Although, yeah, it was right then.
**Jason Plumb** 25:46 Yeah, do we not publish… do we not publish snapshots?
Or is my tool just a piece of crap? So… This should resolve, but it doesn't.
I.O, OpenTelemetry, Android, Android Agent.
What about another… module, like, not the agent. What about… 12 men is a bad one. Session. How about session?
I'm just gonna double check.
Yeah, that's fine.
Maybe my tool is just broken, or maybe we don't publish snapshots.
So, like, the last build… On Main, that passed.
Publish snapshot.
Well, clearly my, artificially intelligent garbage app is not working correctly, and I'll have to investigate, but it looks like it does publish snapshots.
**Cesar** 27:01 But there was… there was an issue that you couldn't see snapshots via HTTP.
Right.
**Jason Plumb** 27:09 Well, the, the, yeah, the browser, like, the browsing application, the hosted thing is broken, but all of the metadata files should still be accessible if you know where to look for them.
**Cesar** 27:20 Okay, got it, so your tool checks it as Cradle does.
**Jason Plumb** 27:25 Exactly, so it kind of crafts these URLs that conform to the pattern, and that should be the way to resolve them, but, you know, we're getting 404s here.
But it looks like the snapshots should be working, so if we track those down, I think the answer to this question is, Can you use a snapshot?
And it will be next month.
Because I don't… I don't see a reason to do, like, a rushed release of that crash reporting. It's like an enhance… it's an enhancement, right? So I don't think… It's not like a bug fix or a regression or anything, so…
**Cesar** 28:13 Okay. Do we mention how to use snapshots? Because I know people have to do some setup.
**Jason Plumb** 28:24 I doubt it.
I doubt it, but it's… yeah, it's in the… I think it's in the, here, but it's in… the dependencies, you can put that Maven snapshot call instead of Maven.
But I don't think we do, let's see.
**Cesar** 28:45 Oh, I can take a… a look.
The next action item.
**Jason Plumb** 28:50 It's not…
**Cesar** 28:50 there.
**Jason Plumb** 28:52 Look at this, snapshot builds.
We mention it, but then what's this?
Yeah, this is the… this is the thing they broke more than a year ago that they refused to fix.
Yeah, it's this…
**Cesar** 29:11 Fine, it's probably… I'll just add something to the docs.
**Jason Plumb** 29:14 Cool, that sounds good.
**Cesar** 29:15 Or, to show how to use snapshots.
**Jason Plumb** 29:18 Yeah, and if I can track down what the latest snapshot is, or, like, at least how to get to the metadata file again, I will… I will fill that in.
**Cesar** 29:29 Thanks.
**Jason Plumb** 29:30 Yeah.
Then there's a question about this one… Yeah, it's related to the other one, right?
Did you have more context on this one, Jamie?
**Jamie Lynch** 29:49 Yeah, so… basically… I figured it'd be useful to have some sort of… early warning system that basically tells us if the SDK is, like, catastrophically broken on a real Android app.
yeah, I guess it's just to catch classes of problems that we might be missing today. So, for example, like.
we don't run tests on, like, minified code, as far as I'm aware, so if we're relying on reflection, that could potentially break stuff, and we'd be messing up.
**Jason Plumb** 30:30 Okay. Yeah, that seems like a good idea.
So, I don't know how to answer this question, it seems like a good idea. I don't know about most, but… I think it's a good idea.
**Cesar** 30:47 Sounds good. Would it be like… like having a, dummy project, Android project that runs with… Minify enabled.
And… and see if it… If it sends data, it's still…
**Jamie Lynch** 31:06 Yeah, I think I'll… Yeah, that sort of general idea. So I think we'd want an instrumented test for launches the SDK, And… potentially… Bye.
yeah, potentially, like, wraps it in a bit of a test harness. So, like, what we do at Embrace, the context is we have a mock web server using OKHTTP, Or that's what we've done in the past, that's probably what we do here.
And you can route the telemetry through to that, and then see if, like, we're getting, like, a basic login span.
**Jason Plumb** 31:49 There are some.
**Cesar** 31:50 Sounds good.
**Jason Plumb** 31:51 There are components in Java instrumentation that we can use for that, right? I think there's a… I think there's a mock… collector that gets spun up in the smoke tests over there, or the… some of the integration tests, and you can… it'll send data to it, and then you can just fetch them back. So I think that exists.
**Cesar** 32:14 There's one from… from the, the same OKHTTP family, which I'm guessing is the one.
that Jamie was mentioning, probably.
**Jason Plumb** 32:26 Yeah.
Hey, Ben and David, we've, talked about your issues, so let's circle back, and maybe we can summarize. So, David first, this… PR is great. We have kind of two things that we talked about in the context of this PR. The first one is probably not obvious, because we haven't done a great job of explaining how we as maintainers look at or treat co-pilot reviews, but as a maintainer coming in and looking at this, the first thing I see is there's a bunch of outdated, but they're still open.
So Copilot made some comments on the PR, and whether they're good or bad or worth responding to or whatever, I think we at least want to have those responded to and resolved, but we don't have that in any of the contributing docs, so it's not easy for someone to know that.
So, I have taken an action item to add that to the contributing docs, so that's a little clearer to people submitting reviews that, it helps to have these cleared out. So, as a maintainer scrolling through this list, just like, man, there's a lot of stuff that he's still working on or needs to respond to.
even if they're outdated, please close them out. So that's what I will add to the contributing. That was the first thing. The second thing we talked about was a question around the project structure.
So I'll let Cesar take over that.
**Cesar** 34:06 Yeah, well, it's basically that I… Thanks for the changes, David. It's just that I saw that The… the structure of the folders is flattened right below instrumentation, like view, dash, click, and dash scroll and dash common.
So I was wondering if… if you consider this, other structure.
Or, if you haven't checked it, or if you did, but it had some problems.
**DavidGrath** 34:35 Fair.
**Cesar** 34:36 Curious about it.
**DavidGrath** 34:38 Oh, yeah, the issue was that I… what was the issue again? I'm coming.
Oh yeah, I couldn't get view comment to sync or something like that, I can't remember. It's on Slack, I'll try and look up my old notes and comment.
But I couldn't get it to sync properly, basically, that was the issue when I tried this structure.
**Cesar** 34:59 Okay.
Okay, probably that have something to do with the, smart… way that we… instrumentation modules in the Gradle settings file, probably.
**Jason Plumb** 35:21 Oh.
**Cesar** 35:21 Yeah, no.
**Jason Plumb** 35:22 Yeah, yeah, that's a good…
**Cesar** 35:25 Which will be on me, to be honest. But I can have a look.
**Jason Plumb** 35:30 Yeah, this thing.
**Cesar** 35:33 Yeah.
**Jason Plumb** 35:34 Yeah, okay.
You think that having view, and then… or view common might not be compatible with this. Okay. That's a valid response, I think.
**Cesar** 35:49 Well, it… it could… Probably if we increase the max depth, That it… that it checks…
**Jason Plumb** 35:56 Oh, yeah.
**Cesar** 35:57 owners.
**Jason Plumb** 35:58 Okay.
**Cesar** 35:58 But, I mean, also, we can just get rid of this and have everything.
Manually added.
In any case, I mean, both styles work. I mean, the subfolders, or the dash separated folders, prefix folders.
Yeah, I think it's a… it's a matter of style and… And, so it's fine, I mean… Whichever we… we find useful.
In fairness, though, we do have the OKHTTP main one in WebSocket, like, the flattened way, so…
**Jason Plumb** 36:46 Yeah, these don't share any code, though, they're so different.
And some of the Vue stuff probably shares code, so… I don't know, it makes sense… makes… I think it makes sense to keep modules that have that shared instrumentation code kind of nested.
But I think we don't have a good… Prior art for that.
**Cesar** 37:08 Yeah.
Yeah, what you're trying to do, David, I think it's the very first time we Find an issue like this.
So you're saying, Jason, that when there's a common module.
It might be better to have everything in a single folder.
**Jason Plumb** 37:29 That's what I'm thinking.
And I think that follows the pattern of upstream, is probably where I'm getting at. So, like, I'm trying to think of a good example, like, I think… Upstream has stuff like… I don't know, Servlet, maybe?
Right, so there's all these different Servlet versions, but they share code in Servlet Common.
**Cesar** 37:56 Got it.
**Jason Plumb** 37:57 So I think following that same pattern makes sense to me.
**Cesar** 38:03 Okay, so I need to fix the Gradle stuff.
Meh.
**Jason Plumb** 38:09 Or we can just… for that… for the purposes of this PR, though, maybe we can just try the max depth, like, 5, and hope it works, or max depth 4, and see what works, and if it works, then we can kick that can down the road a little bit.
**Cesar** 38:21 True.
**Jason Plumb** 38:24 Okay.
Does that help, David?
**DavidGrath** 38:31 Okay, yeah, I remember correctly. I don't know if you could check Slack right now, but it was specifically with the demo app. Yeah, that was…
**Jason Plumb** 38:37 No.
**DavidGrath** 38:37 The issue specifically. Yeah.
**Jason Plumb** 38:40 Okay, yeah, so one thing… yeah, the demo app, so… this makes me insane. So, the fact that the demo app is a separate Gradle project causes problems for us sometimes. And I will show you this stupid hack that you have to… to do.
Demo app.
in the Gradle for… the demo app is some mappings. I think they're in the settings, maybe.
**DavidGrath** 39:08 settings.
**Jason Plumb** 39:10 Yeah, this.
**DavidGrath** 39:11 So… Sorry.
This is a hack that allows us to use the live source code project.
And declare dependencies.
**Jason Plumb** 39:23 locally, that would normally be resolved through Maven, so that we can have the local changes reflected in in the project, like, when you fire up the demo app, you want to see those changes reflected immediately. And this stupid thing allows us to do that, so anything that we rely on from the demo app, from the local repository needs to be in here, and so I think that's probably what you bumped up against, is this thing.
So when you've restructured, does that sound right?
**DavidGrath** 39:51 Yeah, but I kept on trying to, how do I put it now, add it in different ways. I think I remember… changing it to view-click, I tried changing it to view colon click as well, and it was still the same, resolve issues. Okay. I didn't like it.
Yeah.
**Jason Plumb** 40:05 Well, give it another try. Like, do the thing with the depth, and the thing that I also mentioned elsewhere about needing the published conventions for common.
Because those were also missing, that could be part of it, too.
**DavidGrath** 40:21 Alright.
**Cesar** 40:22 Also, I would like to… odd.
I mean, if it's too much trouble.
**DavidGrath** 40:28 Probably we can just leave it as is, and then we, you know, tackle the, the reorganization issue with the single folder, like, later, if… because I don't know, I don't want, you know… to add.
all this extra work on David.
**Jason Plumb** 40:47 Yeah.
**DavidGrath** 40:48 If it's too much, likely. Like, if it's easy, fine, but if it's not, then…
**Cesar** 40:52 Wouldn't like to block.
Yeah, don't…
**Jason Plumb** 40:56 Always sleep over it.
**DavidGrath** 40:58 Yeah, because at least, at least it helps a lot to at least have this new common module.
**Cesar** 41:03 That's reused by the other two.
**DavidGrath** 41:05 Let's go.
Yeah, okay then. I think I should try it out if it's not too much trouble, but I'll get my feedback.
**Jason Plumb** 41:13 Cool.
**Cesar** 41:15 Thanks, David.
**Jason Plumb** 41:18 Alright, let's go on to Ben's thing, let's see, so, yeah, there's discussion about schemas. I think you want these.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 41:25 Yeah, I think these are… Pretty important if you want to build a consumer.
When we have, like, Persian bombs and, you know, different, label names come in.
If you want to build something that's, can be used in production, it's pretty particular, so that's why.
**Jason Plumb** 41:46 Yep, so I opened this issue, I think, after our discussion earlier in the week, I don't know if you saw that.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 41:53 Yeah, yeah, I…
**Jason Plumb** 41:54 Yeah.
it hasn't had any comments yet on it, so we can also continue discussing it there. I think what we decided… what it sounded like to me on this call is, like, none of us are experts on this, and we're a little bit unclear on what URL to use and where to put it. So, we know that there are two places that accept a schema URL, One of them is the resource, and one of them is the instrumentation scope.
which sometimes I just call scope, and that's incorrect, it's the instrumentation scope. And… Cesar suggested that maybe we just use the URL from our semantic conventions declaration, but we don't rev that, right? We have, like, it's 0.1.0 right now, just because We're hacking on stuff.
And as we add more semantic conventions in there, or make breaking changes, like, how… like, do we have a way to rev that version reliably? Because if we don't, then the… like, having a URL with a version number in it that is wrong or outdated is maybe worse than having nothing.
So… I think what we concluded is, like, none of us are experts on this. I think we all agree it's a good idea, but we're not entirely sure how to execute on it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 43:12 Yeah, I did some primitive research on this, so what I found is that, like, okay, yeah, we can… I'm not sure about whether to add within scope or resource, mostly I found resource, I think, and Yeah, I think that the best thing to do is, from the schema, from the manifest, like, we can pull… that should be the, source of truth for the schema URL. And I think the most important thing is, like, first of all, we have to publish something where the schema URL points to, right? So today, it doesn't point to anything. It's not a valid, I think it gives a 404 or something.
So we have to figure out how to get publish something there. So that part, I am… I'm not sure. I think Hotel has a process, defined.
Yeah, and… and what… what I found is, like, so, when we, when we do… Any, any sort of version bump.
we have to, you know, probably use… I think Weaver already provides some, generate diff kind of, option that can help you… help you build the schema. So it will analyze, okay, what is the previous version, what has changed, and that can, using that tooling, you can generate the… the schema. So, schema basically holds the dip, right? Like, what renames should be done? That's the main, Component of the schema file.
And… but the other, other tricky part is that, we… if we have to go with one schema URL, that would cover both, the upstream conventions and, whatever federated we use, so… this should be in a single, schema file. We can… there's no inheritance or, like, importing from an upstream convention. So, even if something upstream changes, that has to be part of our schema. Even if… within our federated conventions also, that also needs to be published. But I think Weaver handles that.
**Jason Plumb** 45:24 Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 45:25 Yeah, I… I can, like, I can add some research notes onto the issue that you opened, and then probably we can continue the discussion there. Some aspects, I'm not sure, I'll ask for help on that, on the ticket.
**Jason Plumb** 45:39 Okay, that sounds great to me. I think that's helpful. I still don't have a good mental model at 8.45 in the morning on how this all fits together, but… I'm starting to.
There's little… there's breadcrumbs here, so that's… that's helpful.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 45:56 Yeah, sure.
**Jason Plumb** 45:58 Okay, and then, I think… did we look at this one? Which one was this?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 46:03 It's the event generation for the navigation, composed navigation.
**Jason Plumb** 46:07 Okay, we didn't look at this one.
On this call today.
But there has been some traction on it. I have not looked at this one.
Looks like Jamie likes it.
Yeah, I just… this needs more review, but I think it looks… like, it's pretty manageable, so I will try and look at that today.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 46:32 Thank you.
**Jason Plumb** 46:36 Throw that into my list.
My ever-growing list.
Okay, cool.
And we did run through Vishwan's stuff, assuming he won't be here today.
**Vishwan aranha** 46:50 I'm here.
**Jason Plumb** 46:51 Oh, you are here, okay.
**Vishwan aranha** 46:52 I joined along with Ben.
**Jason Plumb** 46:52 Yeah, no, you're… yeah, sorry about that. I… it… It was scrolled off the bottom of my attendee list, sorry, no offense.
We like this… Yeah, we already merged it, it's great.
So the timeline for the… I know you want this feature really badly. We're gonna just do it as part of our regular monthly release.
**Vishwan aranha** 47:16 Okay, that's fine, yeah.
**Jason Plumb** 47:18 I know that there's downstream stuff that's waiting on it, but I think… I think it doesn't warrant us rushing a release out.
**Vishwan aranha** 47:25 Yeah. Yeah, I was just curious, like, if it's gonna be soon, so… it's fine, we can probably wait till the end of the month.
**Jason Plumb** 47:31 Yeah, it's probably… so it's when… we release normally when Upstream releases, because we do depend on instrumentation from Upstream.
And… that's when we'll… it'll probably be a month. It'll probably be 3 weeks.
**Vishwan aranha** 47:44 Sounds good.
**Jason Plumb** 47:44 Okay.
And, one… one thought was, and I don't know if, like, if you're just looking to make sure the tests pass versus, like, a CI problem, we were like, can you just use the snapshot builds? Because we do publish snapshots, and you should be able to use them. We don't have any clear documentation on how to do that, so Cesar's gonna add it.
**Vishwan aranha** 48:04 Sounds good. I can use it if… I'll talk to my team members and ask if that's something we should look into, or we can wait till the next release.
**Jason Plumb** 48:11 Okay.
Cool, Yeah, we talked a little bit about this thing, too. I kind of tried to take some notes, We like the idea of it. I was a little concerned that maybe it was gonna add some… length to our already lengthy builds for PRs, but it's not that bad. The PR builds about 20 minutes already. This'll add about 8.
So, for a percentage increase, it's, like, not small, but I think it's worth do… I think we all agree it's worth doing.
And so, we're into it. Part of that smoke test, we think, can or should use some form of mock server that spins up an actual collector-style receiver to get telemetry that you can then fetch out and do asserts on.
That's that.
**Vishwan aranha** 49:02 Sounds good, like, if you guys have any, like… I saw that you guys added some recommendations, so I can probably look at that and open a draft and, like, run it by you guys.
**Jason Plumb** 49:10 Sounds great.
Yeah, I think, Yeah, there's some prior art in the Java instrumentation around the way they do smoke tests, and some assertions around, like, fake… not fake, but data fetched from a server, like a locally running mock server.
Cool.
And then I mentioned a couple of things, but, nothing too crazy. Going back to the schema conversation, we do have this nightly job that will update what version of the upstream schema we use.
when it… when they rev, we'll get a PR, and then if it is clear, we can merge it, and if not, we'll have to fix breaking changes, so that's really good to have automation around.
That's it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 49:53 Yeah, and so that was added most recently.
**Jason Plumb** 49:56 Okay.
We've reached the bottom of the agenda. Is there anything else that folks might want to chat about or look at?
Going once.
Cool. Well, let's… let's call that a SIG meeting.
Nice. Nice to see everyone, I'm glad you found the new meeting invite and the new meeting time, and let's do it again in a week.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:26 Thank you, guys.
**Jason Plumb** 50:26 Cheers.
**Cesar** 50:27 Bye. Right.
**Vishwan aranha** 50:28 See you guys.
