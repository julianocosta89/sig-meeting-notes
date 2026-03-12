SIG: Browser SIG
Date: 2025-12-11
Duration: 21 minutes
============================================================

## Zoom Recording Transcript

**Marco Schäfer** 00:33 Hello. Hi.
**Benoit** 00:36 Hello?
**Jared Freeze** 01:20 Hey, what's up?
**Martin Kuba** 01:23 Hey, Jared, how's it going?
Okay.
I bet on.
Jared, are you in a place where you need sunglasses?
**Jared Freeze** 01:49 Yeah, I live in New Orleans, so it's, I don't know, 65, 70? Fahrenheit?
No.
**Martin Kuba** 01:59 It's, like, so dark here.
**Jared Freeze** 02:03 Yeah.
**Martin Kuba** 02:03 Pacific Northwest, you know, in the winter.
**HL Hugo Levy** 02:18 Nope.
**Martin Kuba** 03:08 I don't think, Dad is gonna be joining today, I think he's traveling.
So, but we can get started.
Hey, David, I think you have the first topic.
**David Luna Bistuer** 03:32 Okay, just in time. Hi, hi everyone. Hi, Martin. You know, basically, This is an, It's… I put it ready to review, it's a PR that I would like to have you to get you informed. So, yesterday I also informed the… in JavaScript sick about this PR.
Which, actually, what it does is, like, it adds a new API to create instrumentations. Instead of just having inheritance from a class, it provides a function that creates instrumentations based on a delegate object that it receives. The idea for giving that is, like, there was kind of… there was this ancient issue About the init method being called While the… the actual instrumentation of the object was not initialized completely.
So it was giving… so depending on how you create the constructor, and you create the instrumentation-wise, the init method, but it's giving you problems.
And also, with this way, we break the inheritance thing, and we just donate an API type.
that it's compatible with Instum Editions, and you can do that kind of some editions. I think that maybe it's interesting for web, so the idea is if we have this method this way of instrumenting, of creating instrumentation, we can have it also for web and maybe get rid of a lot of boiler bread that we have.
Just for the sake of… Compatibility.
So happy to look.
Have a look, maybe give me your, ideas, your suggestions, or maybe We can make something that, that actually it's, it's a good fit for, for both.
So forth, for null and browser.
Okay.
So, anything, any questions, you can ping me, go and drop a message on the Slack, or… or just leave a comment on the PR.
That's it. Thank you for your time.
**Benoit** 05:33 Thanks.
**Jared Freeze** 05:34 Thanks for doing that, by the way.
**Benoit** 05:37 Yes, that's me now. And I created a new this… Last week, about to talk about… to start the discussion about… having some kind of ID to the… to be able to… Build some kind of breadcrumbs, like chronologically… A list of events happening in the same context, which context is… Could be a document, for example.
So, just to give a bit of context at Datadog, we are heavily… Based on… on views, so… The view concept, so, A user can click on a view, and they can list all the events that happened in that view. A view UA is… basically, whatever happens between two navigations.
And… So, but I didn't want to be too opinionated in that direction, for my issue. I tried to to reuse the existing concepts we have on OpenTelemetry, which is… navigation, documents, and app.screen. This is kind of the three things that I… proposed, but I'm totally open to anything else.
Well, in the, in the issue, there are some… Slightly different approaches to the, to this, to this problem.
For example, the document ID will be constant for the lifetime of the document.
Regardless of the negotiations.
But if we choose, for example, to have a screen.id, it could make sense to… for the ID to change for each navigation, for example.
So yeah, for now, I'm just… I just want some feedbacks. What do you feel about… all those… Namings and, and, and concepts.
Yeah, after that, if we kind of settle on some direction, I will work on a… Proposal.
**Wolfgang Therrien** 08:04 Yeah, we, I was at the Client SIG, I guess it would have been Tuesday, and we discussed this… it was very, very small because of the holidays and everything, but we discussed this PR a little bit. I think one of the things that, we touched on was, like.
you know, the… one of the things that's unique to browser for this is that you can have a session, that session ID that might be the same across multiple tabs, right, if they're loading session, you know, say, from local storage.
And so that could be a reason why we might not want to reuse something like screen.appID, because if the use cases are different, it could make sense to use a different attribute name here.
But I think the… I think the concept was well received.
**Benoit** 08:48 Okay, nice.
**Martin Kuba** 08:52 I think one question that I have is whether we want to define this as, as, like you said, like you were saying, Benoit, for, like, the lifetime of the document.
Or have it more, like, logical.
Logical representation of… even, like, between soft navigations.
Or even something that, like, we could maybe provide an API in the future that, you know, you would… users could actually set it, like, this is a different view at this point.
That's… the main question for me right now, like, but they would kind of… like, if it's the whole document, right, then… Maybe it's just, like, document instance ID, like how we discussed, but if we wanted to have it more… more granular, then…
**Benoit** 09:43 Yeah.
I think… equal to 3… Consider having both.
So, document ID and… Something, like, to… that change between navigations?
Maybe we can start with the simpler… Concepts?
And then, introduce… something else later, I'm not… I'm totally fine with it.
**Wolfgang Therrien** 10:16 I think, Martin, is the… is the idea is that, like, a navigation idea is maybe, like, a specific instance of, like, a wider, like, more useful attribute? Is that what you're suggesting?
Because it could be… it could be that navigation events define when this switches, but it could also be sort of like an imperative user action, or something like that, and that gets us more into a logical… Page, like, page view or user activity… stream, like.
I could imagine a world where if it wasn't browser.navigationID, but, like, browser.some other attribute name, like, you could use that to model things like user checkout, or something, as a user progresses through a workflow, and one of those things could be navigation events, but it could also be something that eventually provide an imperative API for that users could use to unify that.
A change in that over time.
But…
**Benoit** 11:14 Yeah.
**Wolfgang Therrien** 11:15 Too complicated to think about that big picture all at once.
But that might be something to think about if browser.navigation ID sort of is too narrow, but I don't know if I'm… if that's what you were suggesting or not.
**Martin Kuba** 11:28 Yeah, that's exactly what I was suggesting, yeah. And so I think… Yeah, aside from what the attribute actually would be called, I don't know if it would be called navigation ID, because, like, we have now navigation timing, and I think there's… The browser, like, provides a navigation ID in some APIs. So I don't know if you want to overload that term.
You know, like, but whether, like, it's… whatever we call it, I think, like, what you were saying.
is, I just wonder, like, if you want to have, more of, like, a… Logical definition of this, of this, as opposed to, like, just the document itself.
Like, the… that… that the browser manages.
But as you were saying, Benoit, maybe you can have both, why not both, so…
**Benoit** 12:32 Okay, thank you. I think.
I'm good, The… Comments are open, like, if you… Have some other thoughts you can always comment.
I will, I will… think about it for a while, and then I will see how it goes.
**Martin Kuba** 13:04 Perfect. Jared, I think you have the next topic.
**Jared Freeze** 13:07 Yeah, so just a couple reviews, from last week and the week before, if you guys could check it out. The generators one, I think.
Trent, you may have chimed in last time. If you're interested, it's… I forget who… exactly who it was. It was, one of the JS maintainers, but… it basically is a turbo command that runs and, like, sets up instrumentation. It's just supposed to be a helper, if there's a choose with it, that's fine. We can iterate on it as well, since nothing's published yet, but that'd be helpful. And then the other one was, I got a little help.
trying… basically, I started doing research in the core repo in Contrib to look at divorcing browser and node stuff.
Because the way the browser, key in all the package JSONs is set up is… I don't love that override style that it's got. Like, it'd be really nice to just have sort of, like, a pure exports. A lot of the keys are in the wrong order.
some of it's a breaking change. Anyways, I'm researching into, like, what to do, and so I was looking into the trace and span ID generation, and I thought I could make it a little faster, and so I started experimenting on both sides. The browser one wound up being 3 times faster, so I think it'd be nice to keep.
the backend one was slightly slower, and somebody chimed in that they're already having issues, and then linked to something that said, like, oh, trace and span ID is too slow already, and it's 76 nanoseconds.
So, we're dealing with numbers I wasn't even really considering. Anyways, I pulled that out, it's just browser now, so that may be helpful, if not, we close it.
So yeah, those are just reminders. I don't know if anyone has comments on that, but… You can check it out. It's pretty straightforward.
**Trent Mick** 14:58 Where… what… which PR are you talking about for the latest work you're talking about?
The trace ID span at each generation.
**Jared Freeze** 15:06 I put it in the doc, I can… I'll post it here as well, if you like.
**Trent Mick** 15:10 Oh, sorry, I was sitting looking at the list of PRs, but I didn't see… oh, sorry, got it.
**Jared Freeze** 15:15 Yeah, it's in the other one, right? Because it's in, it's in the main…
**Trent Mick** 15:19 Yep.
Thanks.
**Jared Freeze** 15:24 Yeah, that's fair.
**Trent Mick** 15:26 So yeah, feedback, welcome. And then the last topic is…
**Jared Freeze** 15:30 Cloudflare has this package PR New, service that basically just does an NPM pack and publish that's private, which is pretty cool. So, you just npm install any commit you want. I wish NPM.js had this already. It'd be pretty cool, but, I thought it'd be really nice because The integration tests I'd like to add to the browser repo I'd like to do a couple things, like pull in main, pull in a particular commit if you've requested it, you know, pull in, the published release.
If we do that, you also have to build it, npm pack it, and then install it. So, it's not terrible, you can do that with a GitHub action, but this, I think, is a little nicer.
Makes life a little easier, too, like, for vendors, you know, if you want to also do this in your own repo, where you're, you know, sort of installing from main. I have some stuff that I have merged that's not in 0.209.0 yet that I'd like to test. I'm doing that manually, right? On my side. I'm NPN packing that manually, so… It looks nice, I don't know how secure it is.
Cloudflare is sponsoring it, so… I just thought it was a nice tool. I posted it in JSDev channel, just to see what the appetite was, because it will live there. It's… so, if we think it's cool, you know, we could also do it, but, Yeah, there's a link if people want to check it out.
**Martin Kuba** 17:01 Cool, thank you.
Take a look at that.
So that's all the topics we had on the agenda. Does anyone have anything else to… to talk about.
Or does anyone have… need any… Feedback, or… Help with anything they're working on right now?
**Daniel Dyla (Dynatrace)** 17:29 If that's it for the agenda, I would… I have a quick question for Jared. You mentioned that your… your sped-up version is faster than the Node version? Did I… did I hear that correctly?
No. Okay.
**Jared Freeze** 17:45 No, it's faster than the previous version. I also sped up the Node version, and it was slower. Like, using the same style, so I just reverted it.
**Daniel Dyla (Dynatrace)** 17:54 Oh, yeah.
**Jared Freeze** 17:54 Totally.
**Daniel Dyla (Dynatrace)** 17:54 Yeah, I got it. Okay, I… because I remember that the only reason they were split out in the first place is that the browser didn't support some of the APIs we were using for the Node one.
And I was gonna say, if… the browser one ended up faster, we could merge it back and just go back to only using one. But, if it's… if the node one is still faster, then… I guess there's No.
**Jared Freeze** 18:20 Yeah, it wound up being 76 nanoseconds versus 126 on the node side, using the browser style.
And so, I was like, oh, that seems okay. And then the first comment was like, definitely not okay. I was like, I will undo.
**Daniel Dyla (Dynatrace)** 18:35 Yeah, I spent some time micro-optimizing that, but it was like… probably 4 years ago now, so I don't know if things have maybe changed.
**Jared Freeze** 18:45 I ran it with no 24… I didn't run it with, like, 18. It's possible you have different results, but, if it's slow on 24, it seemed like It's just, I'm not gonna mess with it, you know what I mean?
**Daniel Dyla (Dynatrace)** 18:57 Yep, okay.
**Wolfgang Therrien** 19:07 So, like, if… big picture, Jared, right, we've been doing a lot of work around, like, getting CI and stuff in the browser repo, like, what is sort of left outstanding for us to be able to, like, say, migrate our first package and, like, migrate, start migrating packages, you know, from some of the other places where they're homed to the browser repo? Like, is there anything stopping us from giving that a whirl?
**Jared Freeze** 19:37 So publishing, so we need, like.
I need to write this down, but we need credentials to publish, we need to actually publish, we need to have integration tests running to make sure the web stuff actually works, so… we already, like, Joaquin had the first PR come in.
**Wolfgang Therrien** 19:54 Yep.
**Jared Freeze** 19:55 It ran through an integration test locally, like, we tested it, but it's not actually running anywhere. So, we need a full, like, webpack.
Yeah. Actually, that's a good point. If everyone could post in Slack just, like, what, bundlers you guys use, like, personally or have used, like, I'd like to just set them all up, because that's not too hard to do a build. And then if we want to have Playwright later, I'd like that security before we actually publish.
**Wolfgang Therrien** 20:20 Cool. Do we have those, those sort of, like, to-dos, like, outlined in an issue?
**Jared Freeze** 20:27 I think they got… I think they got listed, but they should probably be broken out. I think it's all in the same doc, so let… we can… I'll go back and review, I think it was supposed to be there already, but… I'll check it out again.
**Wolfgang Therrien** 20:39 Cool, I was… maybe this is GitHub.
my inability to use GitHub projects, but I was, like, trying to be like, what… what's left here? Thanks for unpacking that.
**Martin Kuba** 21:03 Alright, anything else?
Alright, sounds good. Thanks everyone, and talk to you next week.
**Jared Freeze** 21:16 Cool. Yeah.
**David Luna Bistuer** 21:17 Next week, right?
**Trent Mick** 21:18 Keep…
