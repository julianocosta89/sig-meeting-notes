SIG: Swift SIG
Date: 2025-12-18
Duration: 44 minutes
Zoom Recording URL: https://zoom.us/rec/share/owk9MdhtuDETsn6tgxj6Jz-s0vKSHahbiRmtQe9db7zAHDe9DVtOuMKkiFVBlWUN.cPmAKY9zf6b7eWse
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 00:48 Hey, Billy.
**Billy Zhou** 00:51 Hey, Bryce.
**Bryce Buchanan** 00:53 How you doing?
**Billy Zhou** 00:56 Okay, how are you?
**Bryce Buchanan** 01:00 Not bad.
**Billy Zhou** 01:01 Fair.
Dara, are you doing anything for the holidays?
**Bryce Buchanan** 01:06 Oh, just staying home.
**Billy Zhou** 01:11 Those are kind of the best plans.
**Bryce Buchanan** 01:12 Yeah.
Yeah, we're trying to…
We're trying to keep it, low-key, because every time, like, the last, like, 2 or 3 years in a row, we've gone and visited my,
My, brother and his kids, and we always come back with a cold.
And my wife's, Pregnant. She's due in February, and she really doesn't want to be sick.
Sick. Like, for the last, like, couple months of her pregnancy.
**Billy Zhou** 01:46 Yeah, definitely not. Like, also for the baby, too. Congratulations. That's, that's really.
**Bryce Buchanan** 01:50 Yeah. I think… Thank you.
Look, that's new topics.
Yeah, if you have any topics for today, just add them to the, new topics section on the meeting notes.
Well, it looks like Nacho's not gonna be here today.
Okie dokie, let's get started.
Let me share my screen.
Nice… There we go.
Everybody see that?
Alright.
Okay.
So, I guess Ari's not here, let's just see if there's been any updates on this.
Looks like there's a PR that's been issued.
So we'll take a look at that when we have a chance.
Moving on… I don't know if there's any… if anybody has any comments on that, if anybody's had a chance to take a look at it.
But if not, I guess we can move on. So, it's the monotonic… monotonic… monotonic… Clock, there we go.
**Vinod Vydier** 04:17 It is, it is something like the…
When you try to say internationalization, right, it's a…
**Bryce Buchanan** 04:23 Yeah, it just gets hung up. All right, so we got… got a PR out for this,
That's interesting, yeah, why is it skipping?
Sources here…
Oh, you know, I think I know what the problem is, so… the,
I think that I made changes to the, the build job.
OBS, but I did not… there are some issues with it, and I updated on the, Swift main, repo, but I don't think that those got pushed here, so I'll have to double-check that.
So there may need to be a,
You might need to do a, do a, poll from that.
**Bee Klimt** 05:40 Other than that, there's nothing about the PR that's different from what we talked about last week.
**Bryce Buchanan** 05:46 Cool. So I'll get… I'll take a look at that.
And, maybe, hopefully we can get that merged this week.
That'd be good.
And please, anybody else who has time, take a look at that as well, that'd be nice.
Alright. Swift 6 upgrades…
**Billy Zhou** 06:13 Yeah, for this, I tested this one against, V5 main, and then Core 6. Yeah, I put the setup here.
Yeah, I did a demo app with 5.9, and Swift.
5.9 and Core 6.0, and then I put it on a,
A demo app that I released to Tesla.
And… I bought, like…
4 devices or something for work, and so I tested it on, like, at least 2 or 3 of them. Seems… seems fine.
Like, so yeah, this will have to get released on its own at some point,
But we can also wait until, I, finish testing, main 6.0 against Core 6.0 as well. I hope that you guys…
**Bryce Buchanan** 07:08 Okay, cool.
There it is, okay.
Oh, this.
No.
I'll just… we'll just remove that there.
Alright.
**Billy Zhou** 07:43 I'm never supposed to update, like…
Or, I thought, like, we…
**Bryce Buchanan** 07:47 Yeah, it doesn't…
It doesn't do anything valuable for us, and yeah, it's just… it just causes issues.
**Billy Zhou** 07:58 Okay.
**Bryce Buchanan** 07:58 Because, like, if… if there's a diff… if there's a diff in it, and you're trying to, like, do, you know, Git commands, then it causes problems, because, like, Xcode's open, it'll… it'll…
you know, you'll be like, oh, like, check that out, I don't want to mess with it, and then it'll,
It'll update…
**Billy Zhou** 08:17 Okay.
**Bryce Buchanan** 08:17 In the background, so then it'll cause problems, yeah.
Alright, cool. Well, I'll take a look.
**Billy Zhou** 08:23 At this…
**Bryce Buchanan** 08:24 Hopefully we can get that merged in.
What's that?
**Billy Zhou** 08:26 So, did we do, like, one dedicated package.resolved commit per release, then? Was that, like, kind of the, the idea?
**Bryce Buchanan** 08:34 No, no, we… we don't… we don't… we don't want to commit it at all.
It should be… It should be in the ignore list.
**Billy Zhou** 08:46 Okay.
**Bryce Buchanan** 08:50 Oh, maybe it's not on this one.
Oh, it is. Oh, no, it's counted out. Okay, so that needs to get fixed.
I think we, we added that to the, to the main repo as well.
Two repos. Always forget one or the other.
**Vinod Vydier** 09:08 So the package.resolved changes, right? Every time…
It is in the .ignore.
**Bryce Buchanan** 09:13 No, it's a commented out.
**Vinod Vydier** 09:16 Okay, oh god.
**Bryce Buchanan** 09:16 And the ignore.
Yeah.
**Billy Zhou** 09:19 That was important for, like,
**Bryce Buchanan** 09:21 Here, so…
**Billy Zhou** 09:22 the versions of transitive dependencies?
**Bryce Buchanan** 09:30 So… the… well, the… That's…
It's all managed through the package Swift itself, right? So if you have, you know, dependency libraries set to a version.
depending on how you set it here, then that's what determines it. When you are using a,
Let's say you're using… like…
OpenTelemetry Swift Core in your own project, it does not use your package… it doesn't use the package Resolve that's in the repo. That's only for development, so it's not really, relevant.
In any, in any aspect.
Hey, Ari.
**Ari Demarco** 10:21 Hey, guys.
was fixing my…
**Bryce Buchanan** 10:23 Wasn't sure.
**Ari Demarco** 10:24 Electricity.
**Bryce Buchanan** 10:25 Oh, I had that problem yesterday.
Alright, so I'll take a look at that, and hopefully we can get that merged. Ari, did you have any, anything to say about your PR?
**Ari Demarco** 10:39 Yeah, I created the PR for this.
Already?
**Bryce Buchanan** 10:44 Yeah, it just needs to get looked at.
Yeah, I created two. Cool. One for this, and one for another one, that there was a customer saying that…
**Ari Demarco** 10:52 the URL session instrumentation was crashing, with a crash saying something like, you cannot set effect at delegate after resumption.
I also fixed that one.
**Bryce Buchanan** 11:03 Wasn't.
**Ari Demarco** 11:03 to reproduce it.
**Bryce Buchanan** 11:06 Awesome, that's great.
**Ari Demarco** 11:11 So… Alright.
**Bryce Buchanan** 11:12 Cool.
**Ari Demarco** 11:12 both PRs are… are… are open. The second one, I did… I did some tests, so it's easier for us to…
actually prevent that crash. It's not really anything important, it's mostly to catch up the crash, reproduce the crash, and then fix it.
**Bryce Buchanan** 11:34 Sweet.
Alright, well, I'll take a look at that as well.
**Ari Demarco** 11:39 Yeah.
**Bryce Buchanan** 11:42 Alrighty, let's go on to the new topic. So, configuration options for metric kit instrumentation.
creation.
**Bee Klimt** 11:50 Yeah, hopefully this is not too controversial. I just added configuration options for this that are based on what we have for the URL session instrumentation. You can set your own tracer, you can set it to the Apple stack trace format instead of the hotel one.
That's all that's there right now, but I figure it's a good place to put other stuff in the future.
**Bryce Buchanan** 12:12 Yeah, yeah, that seems pretty straightforward.
Cool.
Got some tests for it, too? Or just, I guess, you're stubbing those out. Oh, no, here's one.
Cool.
I've got lots of PRs I need to review.
Alright, any other topics for today?
Nope.
Shall we take a look at, open issues?
**Ariel Demarco** 12:58 You?
**Bryce Buchanan** 13:06 Nothing too new. I did… I opened this one,
A little while back, related to this other issue, investigating that, Good.
KTOR, which I always think… I always think about that, and I think Knights of the Old Republic, but it's swapped because I'm dyslexic.
Knights of the Old Republic.
**Ariel Demarco** 13:28 One question related to instrumenting, the, oh, the socket?
What events we will want to capture.
Because, like.
**Bryce Buchanan** 13:45 Sorry, say that again, what do we capture for a socket?
**Ariel Demarco** 13:48 Yeah, so, because, you know, you had the start, the end of the end of that, probably it's going to be a spam.
And shall we capture span events per each of the events that we receive with some specific attributes or stuff like that?
There's… there's a semantic measure for that.
That's in some place.
**Bryce Buchanan** 14:08 I assume there is.
**Ariel Demarco** 14:12 Or streaming, because if… if… If there's something, I can give it a try.
**Bryce Buchanan** 14:33 Yeah, it seems like there might be… I don't know.
Might require a little bit of investigation in the, in the semantic convention.
I just assumed that there was something for sockets already, because it, you know, is a whole layer of potential instrumentation on the back end.
Yeah, so there seems to be, yeah, server socket domain. There seems to be some stuff. I'm not sure how it'll fit into…
a client, but yeah, I think it just requires a little invest… investigation.
**Ariel Demarco** 15:07 Okay.
**Bryce Buchanan** 15:08 Yeah, if you wanna… if you wanna snag that up, that'd be cool.
**Ariel Demarco** 15:11 Oh, sure.
**Bryce Buchanan** 15:14 Where did that go?
Today.
Or I'll assign that issue to you.
Cool.
This was another one that came in.
There's a new… New format? Is that what it is? Was this added recently?
Oh, of course, go back to the top.
That's great.
Oh, it's a random trace flag.
**Ariel Demarco** 16:27 Volume U3C, random flag.
**Bryce Buchanan** 16:29 Okay.
Yum.
Interesting, okay.
Yeah, so that's… this is, like, another kind of… I would assume, a rather small, addition to the… to the, span context, so if anybody's interested in a… I would call this a good, like, first issue.
not… I don't think it would, like, really affect too… too much. Like, there wouldn't be, like, a lot of wide,
impact.
to… to this change.
**Ariel Demarco** 17:31 Is there something we plan to do on the understanding IS instrumentation current state?
**Bryce Buchanan** 17:41 I don't know, I haven't heard anything, or we haven't heard anything back from this, this person. I think we just, you know, kind of gave them… answered some of their questions.
We might, there are some, I guess… Spread it.
Kind of add, you know, feature… feature issues for?
didn't really… I wasn't really sure what they were asking about here. I guess touch tracking…
**Ariel Demarco** 18:12 Yeah, it's.
**Bryce Buchanan** 18:12 When are you top.
**Ariel Demarco** 18:14 On a specific part of the screen.
**Bryce Buchanan** 18:18 But yeah, it would be interesting… I think, yeah, to maybe…
I wonder, hmm… I wonder if there is… this might be, like… The, the,
what is that SIG?
the,
The semantic convention.
So, yeah, not the semantic…
**Vinod Vydier** 18:47 declined.
Yeah, the client, yeah, the client instrumentation SIG. I think that these would be…
**Bryce Buchanan** 18:53 like, a good thing to bring to them, and see if there's already some existing, because, yeah, my question here was, like, like, okay, like, you want…
like, things… you want, like, taps, right? Like, but what do you want to know about them? Like, you want to know, like, the XY on the screen? Do you want to take a screenshot? Like, what are all the different… you know, there's, like, a bunch of different things that are… that are moderate, you know, zero usefulness, or moderately useful, or… because, like, I don't know,
I know that…
like, the information in SwiftUI, when you're actually looking at it in the code, or, like, you know, in… when it's running, it's, like, just a bunch of gibberish, basically, so it's like, well, how do you track… like, okay, you tapped on something in SwiftUI, but it's just, like, you know, a bunch of, name-mangled garbage that doesn't… doesn't make any sense. Yeah. So…
**Billy Zhou** 19:46 Oh, go ahead.
**Ariel Demarco** 19:48 No, no, go for it.
**Billy Zhou** 19:51 Alright, yeah, I had the, I had the same…
Reaction to the view interaction suggestion. I wasn't really sure what they were referring to, but I'm, like, working on, like, session replay right now, and I guess it's, like, typically, like, with that. I think it's a little dicey and mobile, but yeah, we'll get it working, and then,
And then, like, I think,
I think people also use this for… to build heat maps as well. I think those are the two big use cases, just, like, session replay and heatmap. I don't know if you guys have anything else. Yeah.
**Ariel Demarco** 20:23 Yeah.
I think that, first-view interaction and SwiftUI support are kinda, like, internally, they… It's, it's like…
mixing concepts, because both of them are UI ways… ways to make UI. One is the clarity, one is imperative, but in terms of interacting with the UI in tabs, it's the same. So XY is the same. Tap event, or scroll, or a gesture, like, drag.
it's the same concept, same for navigating from one place to the other. So, I don't know. The only thing I may mention is that if you want to instrument UI kit, it's way much easier than instrument things with UI.
Because, as with you, I… there's no way to go around
Having to manually go and instrument your abuse, that's…
there's nothing else to do. Like, you can get a lot of stuff, but you have to go and manually at least add an annotation, or a macro, or something like that.
**Bryce Buchanan** 21:25 Yeah, yeah.
**Ariel Demarco** 21:32 But yeah, I think that for interactions, there's nothing on the client side.
Related to that.
I don't know if there's something on clicks for browser, maybe we can search about that, but if there's nothing, that should go first for…
On the client side, or semantic convention side.
**Bryce Buchanan** 21:49 Yeah, yeah, sorting out… sorting out what that looks like, yep, yep. Yeah, that's what I was thinking. I was… I was hoping to get some feedback from…
You know, an actual app developer, see what they're thinking and what they would like to see, but they haven't really
responded at all.
**Vinod Vydier** 22:10 So, do we have access to the logs?
But, so when you do the logging bridge, you are using the OS log.
But what about the stuff that the device itself is logging? Do we have access to that?
**Ariel Demarco** 22:29 Yes.
**Bryce Buchanan** 22:30 I… no.
**Ariel Demarco** 22:33 You have access, but it's extremely verbose, and you have to quit it.
And it only works for the current process that is alive. Like, for example, if you got a crash, and you open up, and you want to know the logs that happened prior to your app existing, there's no way to get it.
At least on iOS. On macOS, it is a bit more friendly.
But yeah, you get… you get a bunch of logs, so the verbosity of this, it's going to be huge. Like, if you export each log independently as a separate log signal.
the amount of logs is going to receive the exporter is going to be gigantic. So, at least from my perspective, it's extremely verbose, unless you apply filters to it.
But if not, I think that most of them is useless and not actionable, and at the same time is extremely verbose.
**Vinod Vydier** 23:29 But it is accessible from another, like, an SDK.
**Ariel Demarco** 23:34 Yeah, yeah, you can… you can go and look to the OS log store and get all the data.
**Bryce Buchanan** 23:42 Yeah, I don't… we don't have any instrumentation that does that, but… That can't be done.
**Ariel Demarco** 23:50 Yun.
I investigated that because some customers asked for the possibility to get the OS logs.
**Vinod Vydier** 23:57 But, when we start doing the actual job to do it.
**Ariel Demarco** 24:01 It was kind of complicated.
we use OS logs mostly whenever there's a critical thing, like, there's no more space on the device.
So, Always Love works in a way that
keeps in memory, so… and the splash-out probably is using, an encache or… or… or something like that.
But in terms of gathering the information and sending it to the backend or to exporter, I think it's not really worth it.
**Bryce Buchanan** 24:35 Yeah, yeah.
**Ariel Demarco** 24:36 That, that's a good.
**Bryce Buchanan** 24:37 I've stayed away from it.
**Ariel Demarco** 24:39 Could be done, and… but probably needs a use case to actually… let's go and instrument it, like, a real use case, not just grab all the data and export it.
**Bryce Buchanan** 24:51 Yeah.
Yeah,
Yeah, I'm kind of hesitant to provide, like, an… you know, like, I would see that kind of as a bad thing to add to your app. You know, I don't want to, you know, flood… you know, have a… have a… it's like, oh yeah, like, here's just this very dangerous, instrument.
patient that's probably not useful to anybody, but it checks a box and says that we have log… logging now, you know, but it's gonna totally destroy your AWS S3 costs or something. Yeah.
Yeah. Okay.
**Billy Zhou** 25:36 Yes.
**Bryce Buchanan** 25:38 Yeah, so, I mean, we can… Go, go ahead, Ben.
**Billy Zhou** 25:41 Alright, yeah, I was gonna put out some CRs for some of this other stuff, though, like, like view support, and then, app launch instrumentation. Do you guys want to, like, align on design first before I do that, or,
Should I just… Send it over.
**Ariel Demarco** 25:59 I… My only concern with…
**Bryce Buchanan** 26:01 Yeah, I think that we should… we should… bent.
**Ariel Demarco** 26:06 Go for it. Go ahead. No, no, go, go.
**Bryce Buchanan** 26:09 Oh, I mean, that's really all. I was just gonna say that maybe we should, discuss it in, like, a separate issue, you know, if we want to discuss, like, startup inter… inter…
Or, or instrumentation.
Come up with, like, a proposal with what you're thinking, and then we can… we can kind of work through it. There may be some… I know… actually, I know there's some existing
Like, semantic conventions around that.
So it's, it's also good to…
Okay, I'll copy the… I'll take a look at that as well.
**Billy Zhou** 26:42 zone.
Share them and stuff.
**Ariel Demarco** 26:46 Yeah, the, the only, the only…
concern for me, in terms of the startup, that in order to actually measure startup in a good way.
you need to have a bridge on Objective-C or Objective-C++.
So you can access some of the moments on the pre-main part of the startup.
if you want just to measure some things from Swift only, you can, but you'll be missing a bunch of stuff that probably is going to be necessary.
**Billy Zhou** 27:21 Yeah, makes sense.
**Ariel Demarco** 27:23 But I think that Bryce is right in terms of, let's create an issue and let's document it, like.
and finally reach a decision. Maybe we want to have a startup measurement.
With some caveats, and that's it.
Or maybe we would want to create a target that it's Objective-C only, or something like that, and maybe we can drop the tooling in there.
I think that it's going to be cumbersome for people using, Swift only, like Vapor, or stuff like that, or on Linux.
I really don't know how that compiles, to be honest. Never… Made a test, so…
it might be worth trying it out, but for example, if you want to understand at which point in time something was linked, or to determine if it was a pre-warmed or a warmth or cold lunch, you maybe need some Objective-C, C++ annotations or attributes.
**Billy Zhou** 28:20 Yeah, sounds good. I also used some, like, system-level commands, like kproc, for hotel… for AWS, disrog. Nice.
Okay, if anyone's gonna be here next week, I can, yeah, send over the summaries,
Preview, so we can… Talk about it.
**Bryce Buchanan** 28:40 I won't be. I won't be.
**Ariel Demarco** 28:43 Damn.
**Bryce Buchanan** 28:44 Patient until the 5th, you know?
**Ariel Demarco** 28:48 I'll be here. If I go on vacation, it will be in January, so it doesn't matter.
**Billy Zhou** 28:53 I noticed…
**Ariel Demarco** 28:53 I don't… I don't know if the SIG is going to be canceled, the SIG meeting, because I saw something on the auto maintainers that there was a…
Something?
**Vinod Vydier** 29:01 canceled on 22nd on month zero.
**Ariel Demarco** 29:04 Okay, so I think the SIG is going to be canceled, but regardless of that, Billy, if you want to submit an issue and… or even let's start talking on SAC, doesn't matter. I think that
It's a great feature, I think that most AS developers care about that.
So maybe worth giving a try, at least, on what we can get.
Problem.
From the suite side.
**Bryce Buchanan** 29:28 Yeah. How does… I'm curious how that stacks up against…
Against the metric kit, like, launch times. Like, there's a launch time metric in Metric Kit, isn't there?
**Ariel Demarco** 29:42 Yeah.
**Bryce Buchanan** 29:43 Yeah.
Yeah, so that's… I'm curious how that looks, and which one will be more accurate, or if they will be the same. I guess one's averages, so…
**Bee Klimt** 29:53 Yeah, I don't remember, but I assume the metric at one is pre-aggregated, and also not real-time.
**Bryce Buchanan** 29:59 Yeah, yeah, that's true, too. That's the other problem. So, the.
**Ariel Demarco** 30:03 That's me.
**Bryce Buchanan** 30:04 Might be valuable for that fact.
**Ariel Demarco** 30:06 And it's sampled, so you know how many devices are actually really having startups.
Yeah.
**Bryce Buchanan** 30:13 Yam.
Yeah, all good points.
**Ariel Demarco** 30:15 hey, Eric, yeah, you can add yourself on the agenda, and add the topic, but…
You can ask it here, no problem.
**Erick Sanchez** 30:29 Hey, folks. Okay, yeah, I just wasn't sure when, open questions was part of the agenda yet.
**Bryce Buchanan** 30:37 Oh yeah, yeah, and help yourself.
**Erick Sanchez** 30:41 Grant, so I've been trying to add… Headers to our… calls using the SDK.
And we've had some set up for baggage.
But, they're not showing up anymore. The only… the only, header that shows up is, of course, the… the auth token, but that… that one is, like, hard-coded when we set up the SDK.
Like, on app launch?
But the header that I need to add is… is dynamic, like, during…
Like, let's say we fetch, you know, the slash me of the user.
That's where the value comes from.
And I'm having trouble trying to understand what's… what's the right approach to… in the SDK to add this to…
To, basically, the baggage.
Header key.
That's really the goal.
**Bryce Buchanan** 31:38 I mean… Hmm…
That is a good question. Off the top of my head. I don't know if I can answer you.
**Erick Sanchez** 31:50 Wayne?
**Bryce Buchanan** 31:51 So you're trying to add a… a baggage header to all the…
**Erick Sanchez** 31:59 Are you… are you.
**Bryce Buchanan** 32:01 Trying to add those to, like, your export requests, or to…
every network request that you're sending, or… or… I'm confused, what do you… are you trying… or do you want to, like, track it as an attribute?
**Erick Sanchez** 32:18 No, it would be part of the… what looks like the exporter, so, like, slash traces, slash metrics,
And we do send it to our own server, so we do have a base URL.
So, you know, it wouldn't be an attribute to, like, the span or the data, it'd be the request itself.
**Bryce Buchanan** 32:38 Okay.
I see.
**Ariel Demarco** 32:41 So you are using an auto exporter, isn't it?
**Erick Sanchez** 32:44 Yes, I believe so. It looks like we're using…
I think this one that you're showing right now?
And I think this is how we get…
**Bryce Buchanan** 32:54 Yeah.
**Ariel Demarco** 32:55 if you enterprise at the top of the document, there's an…
**Erick Sanchez** 33:01 Oh, man.
**Ariel Demarco** 33:02 end header, something like that, and barkheaders.
attributes?
Yeah. So that is a static, property that access a string.
That it's basically a… I think it's a comma-separated… Tupo?
I think you have to provide to the environment the heaters you want to Wide list.
**Erick Sanchez** 33:31 I see.
**Ariel Demarco** 33:33 you… can you enter to that file, Bryce? So…
**Bryce Buchanan** 33:36 Yeah, the… the issue… the issue here, is that these can only be set once, I believe. I'm not sure if there's a… an update.
**Ariel Demarco** 33:44 Yeah, it should be set up on startup, yeah.
**Bryce Buchanan** 33:47 Yeah, yeah, so…
**Ariel Demarco** 33:48 I think it's, aside of being dynamic, and even though you said it once, the problem is how to set it out. It's kind of complicated, like, from… at least from a user perspective, because it's not easy to configure.
But… But yeah, you have to set it once and for all.
**Erick Sanchez** 34:10 I'll just type in on my phone. I think it makes sense. I see that the MVAR headers is a closure, so…
It looks like it's… I'm guessing this is consumed on the fly, like, for every request?
**Bryce Buchanan** 34:30 Yeah, it'll be applied to every request.
**Erick Sanchez** 34:33 Amazing.
Sweet. Okay.
By any chance, are you all familiar with, what's the type off the top of my head? I think it's baggage.
Baggage propagator?
**Bryce Buchanan** 34:47 Yeah.
**Erick Sanchez** 34:48 Is this anything that I should check out as well?
**Bryce Buchanan** 34:52 I am not very familiar with baggage.
I'd have to review it.
I'm not sure if this would… this more of… this more of is, like, applied to,
to the… to the attributes, from what I'm understanding, I'm not sure.
**Erick Sanchez** 35:14 Oh.
**Ariel Demarco** 35:14 Yeah.
**Bee Klimt** 35:15 Yeah, that one's just a span processor.
**Ariel Demarco** 35:18 Exactly.
I think that what you're trying to achieve is mostly how to
allow list, create an allow list of the headers, so I think that should be done on how you configure the auto HTTP… OTLP HTTP exporter.
**Bryce Buchanan** 35:35 Yeah, the exporter now.
**Ariel Demarco** 35:37 what I would suggest, if you don't have the code in…
in hand for… to show up. Maybe you can create an issue if you cannot fix it.
Like, post, how are you configuring the OTLP exporter? So, maybe you can see if it's an actual bug, or if it's a problem in terms of…
I don't know, your configuration or something like that.
**Bryce Buchanan** 36:04 Yeah, I think…
**Erick Sanchez** 36:05 Oh, basically.
**Bryce Buchanan** 36:06 I have an existing issue for being able to update it after the initialization, but yeah, right now you can only set it at the initialization.
**Erick Sanchez** 36:17 Right, okay, I think, you know, I'm looking at the code. Unfortunately, I can't screen share, I'm connecting to my phone.
My laptop just does my life in my hotspot.
But I do see these types. I do see the HTTP trace exporter and nitrix Exporter.
I'm guessing these are the two types we were showing.
So then I can… Let's assume.
Oh, okay, I see that both exporters have this and bar headers. Okay. And you mentioned this is, like, an allow list?
So, after I add these keys here, do I need…
You could set it somewhere else.
**Ariel Demarco** 37:02 No, when I refer about aloud list, it's basically that. E and the bar heater's block.
That we were talking about, like, that is the one that finally
allows you to export the actual heater through HTTP.
**Erick Sanchez** 37:18 Gotcha. Okay, okay, I'll play around with that a bit more. I do see there's, like, an open… OpenTL configuration that has headers there. That's where we pass in that API code in.
But it looks like once it's dead, it can't change it from there.
So I'll give… I'll give that a try.
I guess one last, one last question, because this is just what I see today, but it looks like it hasn't been working, I don't know, since when?
There is a default… Actually, it's on the context provider.
It's a set active baggage.
This is where we've been sending
One… one of the keys, instrumentation.priority. This might be just for us.
I don't think it's the SDK itself.
So yeah, we call setActiveBaggage, and we pass in a baggage builder inside, and this is… this is where I notice those keys are not being sent.
So I'm wondering, should I just… I'm gonna play around with it, but I wanted to get you guys' feedback on, should I just be moving those keys into this M…
this N, these blocks that we just talked about.
**Ariel Demarco** 38:34 Yes, I think.
**Bryce Buchanan** 38:34 Yeah, I think…
**Ariel Demarco** 38:35 You did that.
**Bryce Buchanan** 38:37 the right.
**Ariel Demarco** 38:39 Yes, as we mentioned, it's more for attributes, and it's a processor, so,
I think that is… it's another set of tooling, using the context and the baggage.
**Erick Sanchez** 38:55 Oh, I see, okay. I haven't been looking at the spans themselves for this key. Okay, I'll take a look to see if it's in there.
And then, well, if we need it in the HTTP, then… then I'll know what to do next.
Oh, Bryce, if you're looking for…
**Bryce Buchanan** 39:13 There was, like.
**Erick Sanchez** 39:14 Set active package.
**Bryce Buchanan** 39:17 Oh, I wasn't looking for that, I was looking for, like, the… The config, .
**Erick Sanchez** 39:26 object.
**Bryce Buchanan** 39:28 Because I think… I think there's also, like, header fields on that as well, but… Yeah, I wasn't.
**Erick Sanchez** 39:34 Yeah.
**Bryce Buchanan** 39:35 I don't know.
**Erick Sanchez** 39:35 If it's the one.
**Bryce Buchanan** 39:36 But yeah, if you… if you have any… if you can't figure it out, you can… what's that?
**Erick Sanchez** 39:42 Oh, sorry, I guess I'm out of delay. Yeah, I think I see the one you're talking about was OTLP configuration. Looks like it's a struct with the headers on it.
**Bryce Buchanan** 39:58 Oh.
**Erick Sanchez** 39:59 life.
**Ariel Demarco** 40:00 Well, one tip, Bryce, if you…
Are you in one code, in random code, and you press dot.
**Erick Sanchez** 40:08 I'm excited!
**Ariel Demarco** 40:09 anywhere?
It opens up.
**Vinod Vydier** 40:14 We escorted.
**Ariel Demarco** 40:15 This… this has to be a golden.
On the web.
**Bryce Buchanan** 40:19 Oh, look at that. That's a new… that's new. That's cool.
**Ariel Demarco** 40:27 And you can search easily.
**Bryce Buchanan** 40:31 Yeah, that's cool. Okay, yeah, so there's these, these headers as well. I think those will be applied to your exporter when you, when you utilize that.
**Erick Sanchez** 40:43 Gotcha. Okay, yeah, this is the only one that I see that does work.
But I'll have to use the… the blocks, since, I can only set these… these headers right here, during the app launch, but I don't have my value yet.
**Bryce Buchanan** 40:58 I see, that's the problem, yeah.
**Erick Sanchez** 41:00 Yeah, this is the only one that actually works. All the other ones, like, setbaggage.
Set active baggage, and… baggage builder, those are not looking. But I'll look to see if maybe.
**Bryce Buchanan** 41:12 Yeah, those aren't… those aren't for the exporter. Those are…
Yeah, yeah, those are, those are for,
now that I think about it, I think that the way that works is, like, in the network instrumentation, the baggage headers will be applied to the requests that are being instrumented, so that they can be sent to down…
on stream, like, hotel instrumentations. So those aren't… those aren't, they're being, like, applied as attributes, basically, at, like, you know, in the, the,
what's the word? Like, cross… service tracing.
**Erick Sanchez** 41:50 Gotcha. Okay. Oh, yeah, it seems like I was looking in the wrong spot. So I'll take a look there, make sure I'm not missing anything.
Okay, sweet. Yeah, sounds like, the M block is the way to go.
**Bryce Buchanan** 42:04 Yeah, it sounds like, this issue that we have, might be…
yeah, allow headers to update after initializing exporters. I think that might be…
The sticking point for you, if you don't have that data at initialization.
**Erick Sanchez** 42:22 I see, okay. Hopefully the block will save me.
**Bryce Buchanan** 42:27 Get that addressed.
**Erick Sanchez** 42:28 I jugged what I need.
**Bryce Buchanan** 42:33 Yeah, let us know if you get it figured out. We've got the, the Slack channel and the, CNFC, Slack.
Hotel Swift, or just, open an issue, and then we can help you through that as well.
**Erick Sanchez** 42:48 Oh, sweet. By any chance, do you have a link to that Slack channel?
**Bryce Buchanan** 42:54 Let me see if I can share it.
**Erick Sanchez** 42:59 That's okay.
**Bryce Buchanan** 43:07 Mmm… Copy link, let's see if this works.
There's a link in chat.
**Erick Sanchez** 43:21 Perfect. Awesome, thank you so much.
I guess try and hopefully,
We don't get them in, but they're all right now.
**Bryce Buchanan** 43:29 Alright, cool.
Alright, any other topics before we call it?
Alright.
I think that's, it's good for today. I'm gonna be out, yeah, until the 5th of January, so, feel free, Ari, if you want to hold a meeting next week, if you're around or not. I guess that, that is Christmas, so…
**Ariel Demarco** 43:59 Yeah, I think that it's not going to be done, be not confirmed it, I think.
**Bryce Buchanan** 44:06 Yeah, I would say, yeah, let's… I'll just make a note in our Slack channel, and in our meeting notes that we're just gonna not hold, meetings, because, yeah, both of our next two weeks are on holidays, so we'll just call that.
Cool.
Alright, well, Merry Christmas.
Thanks, everybody, and a Happy New Year.
Alright, see you later.
**Ariel Demarco** 44:34 I guess.
**Vinod Vydier** 44:35 Bye.
