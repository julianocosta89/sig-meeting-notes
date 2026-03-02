SIG: Browser SIG
Date: 2025-10-09
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 02:00 Dude.
Where are you located again?
**Benoît Zugmeyer** 02:08 I'm in, France, Strasbourg.
**Jared Freeze (embrace)** 02:11 Oops.
Hey, David.
**David Luna Bistuer** 02:19 Hello?
Good, it's morning or afternoon, yeah.
**Jared Freeze (embrace)** 02:24 Good morning for me. Yeah.
**David Luna Bistuer** 02:26 Okay, so, here it is afternoon, almost every… almost evening.
**Jared Freeze (embrace)** 02:30 And where are you?
**David Luna Bistuer** 02:31 How are you?
Barcelona, Spain.
**Jared Freeze (embrace)** 02:34 Boom.
**David Luna Bistuer** 02:37 It's the sunny, but not so sunny.
It's raining today, and it's starting autumn already, so… Usually, you have to slide.
Where are you based, Chad?
**Jared Freeze (embrace)** 02:53 I'm in New Orleans, Louisiana, in the US.
**David Luna Bistuer** 02:56 Okay.
**Jared Freeze (embrace)** 03:00 Yeah, beautiful today. It's not, 100, which is great. It's the first cool day.
**David Luna Bistuer** 03:08 Okay, good.
**Tedsuo** 04:10 Yay!
**Jared Freeze (embrace)** 04:12 Hey, Ted.
**Tedsuo** 04:14 I'll go in.
8.
Well, it looks like we got a lot to talk about.
Why don't we get started?
David?
**David Luna Bistuer** 05:49 Okay, I'll start, but mine is really, really shocked, so it's just a heads up that I remember that last sick, we were commenting about, which vendors are going to do with support. We were… we talked with… there was a comment, I think, from Joaquin, about just…
Go backwards and just first think about the features we want to support, and then from that, resolve the list.
And I promise to create an issue for that, issues there, so let's have the conversation there, and that's it.
**Tedsuo** 06:18 Awesome. I think more from my end.
**David Luna Bistuer** 06:20 Thank you.
**Tedsuo** 06:21 Okay, see you on GitHub with that one.
Joaquin, you want to talk about, browser features?
**Joaquín Díaz** 06:29 Yeah, I remember at some point we talked about only supporting things that are, like, widely available, that means, like, available in all major browsers, like, at least, like, 18 months.
But I've been seeing, and after a few comments and everything, it's like.
I'm… I'm afraid that we may miss a lot of, like, good things that could always faster to adopt.
Like, understanding that Chrome is, like, I just saw it today, it's, like, 71% of users globally.
And we can have, like, 5% edge that is… chromiums in the background.
Thank you.
My main question would be, do you want to miss out?
Having more information for 17% of users, just because the other browsers are slow.
To adopt all these new features.
Like, to give you an example, the resource timing API has a lot of more information on Chrome that is really useful.
I saw a comment today on my proposal, like, browser… well, proposal here about the page life cycle. That is also really useful, but it only… it's only on Chrome.
manage.
So yeah, we want to get your thoughts on that. In my opinion, I'll say, like.
if there are things that we know Chrome supports.
another browser's done. I think it's valuable to add them with the corresponding, like, clarifications on the semantic information, saying he's only supporting scrub.
And then we can let the user decide whether that's useful for their use base or not.
I wouldn't add stuff that is broken. In other, like, if Mozilla, for example, isn't following the specs, then I would… I wouldn't have that being reported by Mozilla.
I'll try to… have, like, everything that is following the spec at the first browser
That is probably one of these biggest crumbs, so…
If it is following the spec, we can add it to the telemetry, and then, yeah, just have that in mind that it may not be available for, like, 20% user.
**Tedsuo** 08:41 I mean, that sounds reasonable to me, right? Like, I would say the thing we'd want to avoid is, like, having the data change, right? You'd want to augment the data.
The other thing, it…
it's making me realize is there's sort of, like, what browser features do we support for instrumentation versus what browser features are required to run the SDK and the instrumentation, right?
There's actually two main things. Yeah.
**Joaquín Díaz** 09:11 Yeah, yeah, I think those are two different things, and I think…
the second question we can answer by… in part is, like, what bundles we want to support, and how do they bundle code? And I think…
at least on the base, what we decided is to… I think we used a 2022 expo script.
That runs the SDK. I think… so…
you probably want to have your SDK running on every browser, that is true, and you don't want to…
Use features are not going to work on certain browsers.
But I… in terms of what we collect and what… like, if a browser is providing more information than another browser.
I think it's… it doesn't hurt to add it.
With the clarification about, like, this is only available for Chrome. I know my exception is only Chrome, only because Chrome is, like, 70% of market share, so I think if you're trying to understand your users.
Like, understanding 70% of users is a lot.
More useful than not knowing something about 100% of your users.
But yeah, I agree with Martin, like, there is a challenge on the back end, like, understanding that
If you're looking at 100% of users, and a specific attributes for a log, for example.
There's going to be 30% of users just missing that.
Because I run another browser.
I think, like, it can be useful by also, like, attaching the…
Maybe the browser to all the telemetry.
So when you're looking at something and you know it's only available in Chrome, you can filter by Chrome.
Don't do the analysis.
That could be one way of, dealing with that, I don't know.
**Tedsuo** 11:04 I mean, it seems reasonable to me. Do other people have thoughts?
**Joaquín Díaz** 11:08 Actually, sorry, the website will be under resource, so you have to… Filter our unit.
Telemetry by resource.
**Benoît Zugmeyer** 11:18 What will be the market share limit to collect given information?
Because, okay… In general, Chrome is more advanced than others, but in some small cases… Ehh…
Safarium and Fairfax have a bit of advance, like for
Resource timing, I think the content type is only implemented in Firefox.
Should we collect it, or not?
**Joaquín Díaz** 11:50 Yes.
**Tedsuo** 11:51 That, I think…
**Joaquín Díaz** 11:55 Again, I'm… I'm in favor of collecting what Chrome does, only because it's… A lot of market share.
ums.
But Anna, I… It's hard to draw the line and say we only collect extra stuff for Chrome.
ums.
I think I will say, like.
We shouldn't connect something that is broken, but if the data makes sense for all browsers, then it's fine.
but yeah,
I don't know if you have any other thoughts, like, what would you do? Like, would you collect something that is only on Mozilla, and just say that we only do it from Mozilla, even though it's, like, 2% of people?
**Jared Freeze (embrace)** 12:39 I mean, I think in aggregate it's good, right? Because…
again, if it's not buggy, then having the MIME type along with all the speed information from Chrome combined, again, in aggregate, I think is really useful, so… I would say, yeah, collect content type, even though it's only the one browser, because for any given URL, it's gonna be really… it'll build up that data, I think, and be useful, so…
Yeah, and then back to what you were saying before, yeah, I think syntactically, we just stick to 2022, but for data, just, like, collect everything that's…
possible and accurate. That's, like, how I feel about it.
**Tedsuo** 13:19 I mean, that seems… sorry, go ahead, Martin.
**Martin Kuba** 13:22 No, I was gonna say, like, so I do have a side question about this, like, as far as,
Syntactically.
**Tedsuo** 13:28 Right.
**Martin Kuba** 13:29 Does it, do we want to, to, make… do, like, make an extra effort to make sure that… that the,
The bundle or, like, the package doesn't break any browsers?
You know, like, even if it, like, didn't work, like, that it wouldn't just, like, Break someone's application.
**Jared Freeze (embrace)** 13:47 Great segue. We ran into this this week, because we have a customer that's using a browser from 2019.
Yes, I think we should be aware and run, a compat script against browsers.
like, just to know, not to, like, block PRs necessarily, but to be very aware of, like, what you can download level and what you can't. So, we just saw something with, abortSignal.timeout.
is not available, can't be down-leveled. So, we made the decision
Let's go ahead and just use the setTimeout, because we do want to support, and that's an easy thing to do.
And it doesn't have a polyfill. Decompression and compression stream were the two…
big ones, but everything else in our SDK, including OTEL that we pull in, was totally valid. So, yeah, I think there's a lot more detail there, but I do think we should be checking these things, because a lot of it's really easy to sort of patch, or, like, make
good for very old browsers, even if we're writing modern. So, yes.
Let's… let's, like, start a ticket, do that offline.
**Joaquín Díaz** 15:01 But I just think, like, whatever we do, like, the priority should be not to break the runs line.
so late.
If we're, for example.
for the original assignment API, it's easy because you have another attribute, that wouldn't break it, right? Unless you're doing something to read it.
But if there's, for example, a new API, like, I haven't seen the Page Lifecycle API.
But let's say it's, like, window that page lifecycle, that something, and if you call that on Bacilla, that will break the execution and will break the runtime. Then, in that case, we should be careful and not break the runtime.
So whenever we're dealing with these features that are, not widely available, we should be careful.
**Tedsuo** 15:49 Yeah.
I mean, that all makes sense. I kind of feel like for our very first initial version, you know, let's stick to the universal stuff.
But yeah, I don't see any reason why we can't add additional browser-specific You know, things.
If they… we know that they're gonna be very useful.
Okay, let's keep moving. So, Jared, adding some tooling…
Want us to take a look, basically?
**Jared Freeze (embrace)** 16:24 Yeah, totally. So I think Wolf King had mentioned that…
I think you guys are using Biome. I just set it up for, for our SDK. Looks nice enough, it's very fast, so you can do it pre-commit. I thought that was really cool. Like, it's fast enough to do, just all the time, run against the whole repo.
If anyone has issues, that's fine. One is newer, maybe more controversial. Leave a comment. I don't know. I like it.
We'll see. NPM has enough problems with peer dependencies that I'm kind of done with it, so… .
**Wolfgang Therrien** 16:58 Yeah, I…
I think my preference would be for something that's a little bit more boring, has been around for a lot longer, unless there's, like, a clear, like, we should use Bundt because of these objective reasons, but I'm open to the discussion. We use yarn, so it's like…
**Jared Freeze (embrace)** 17:17 Yeah, it's got a test runner. I mean, that was one of the… it does, like, 5 things, so I thought that was nice. It also bundles, which we can talk about, so…
**Tedsuo** 17:32 Daniel, I don't know if you have any thoughts as a resident JS maintainer.
**Daniel Dyla (Dynatrace)** 17:38 I mean, I…
I have lots of thoughts about it, and I… we've gone so many different ways on this in the JS repo for so many years. We always end up coming back to NPM
We've had a couple of times where… essentially, we've found that it's helpful, in many cases, to be using the same infrastructure that we expect our users to be using.
Because there are, as Jared alluded to, some peer dependency issues and stuff like that that NPM has, that if we use some other package manager that avoids them in our development, we may miss them, and then our users tell them about them, and that's not the best way to find out. So…
We've…
gone… we've stuck with NPM mainly for that reason, that it most closely matches what we expect most of our users to be using. But not all, obviously.
**Tedsuo** 18:40 Yeah.
So, we, we have,
An issue for, like, bundler support.
I feel like maybe we should be continuing this discussion there. I added it into the meeting notes, like…
Because one of the reasons this was brought up, Daniel, is we're wondering whether, like, the browser community is using, like, different
You know, different toolchains than…
than the Node.js community. So, like, if we want to meet them where they're at, does that actually mean we need to move, or is it all still NPM at the end of the day?
**Daniel Dyla (Dynatrace)** 19:17 I don't know… I'm not as plugged into the browser community,
But, definitely we have problems with bundlers in general, and some people use bundlers for Node.js as well, not just for browser.
But, you know, we depend on…
like, require statements, which a lot of bundlers just strip out for obvious reasons, and then we can't instrument anything. We've run into that in the past as well.
**Tedsuo** 19:42 Yeah.
**Jared Freeze (embrace)** 19:44 Yeah, I can… I'll write up something about resolvers, because that's actually what matters here. It's not actually the bundler, it's the resolver. Webpack 4 doesn't have a resolver that looks at the exports key, which is the issue.
Okay, I'll put that on the… On the issue.
**Tedsuo** 20:02 Thanks.
And my personal preference is, like, you know.
roughshod is good enough, right? Let's take a…
Do enough research to figure out what we think is a good starting point, but not sweat it too much, so that we don't block ourselves.
I'm very excited to get us to the point where we're, like, shipping instrumentation, so…
That would be my one request.
Okay… Wolfgang, you having some admin issues?
**Wolfgang Therrien** 20:33 Yep, I basically can't get assigned issues. I'm gonna… I'll post in the OTEL browser channel, I'm just not sure who can help me debug this, like, I'm in the org, I'm in Tainer on the repo, but I still can't be assigned issues, or, and so…
I just wanted to… Flag that, maybe someone could help.
**Tedsuo** 20:54 That's weird.
**Daniel Dyla (Dynatrace)** 20:55 That is… yeah, that sounds like a bug to me.
**Tedsuo** 20:59 Yeah.
Okay.
I'm not gonna try to live debug that.
**Wolfgang Therrien** 21:07 Yeah, no, I just wanted to call it out.
**Tedsuo** 21:10 Yeah.
Okay.
So, I brought this up, I'm glad to see Daniel's here. So, Daniel, you've been making some pretty good progress with the entities prototype, is that correct?
**Daniel Dyla (Dynatrace)** 21:24 Yeah, there have been a couple of different prototypes. We've had some… different,
I guess, ideas about the ways that entities should work, but there is, like, yes, I did write the current prototype.
**Tedsuo** 21:40 Yeah.
I feel like, because that's, like, been a bit of a moving target, and we've kind of changed architectures there, I feel…
like…
it feels almost important to get that hooked up to the session manager and get us working with the entity SIG, just to make sure
That… it seems like a good time to get all that stood up, basically, to help just make sure this… we're not…
solving new requirements while accidentally dropping old requirements in the process. I think we've hit the point where just writing code is the best way to figure this stuff out with entities.
**Daniel Dyla (Dynatrace)** 22:18 Yep, okay.
**Tedsuo** 22:19 It just feels like most of the feedback and most of the changes to the architecture are being driven right now by, like, trying to do it and then discovering
Something is, like, more difficult than we thought it was.
Right? So… Yeah, it would be… it would be cool to… to see that in action.
**Daniel Dyla (Dynatrace)** 22:41 Okay, I guess… so… after, the entities meeting this Monday, which, for those that don't know, we moved it to Monday so that we wouldn't conflict as much with this meeting.
We talked about, A new… a new idea for ways that we can have entities which…
Change, or reporting multiple different resources from,
a single SDK, and fundamentally, that's what Sessions is. So…
Right now, what we're talking about is having, essentially, a way to
bind a meter provider to an entity. So you would have… or, you know, meter provider, tracer provider, whatever, all the providers would have the same
API, but you would say, like, meter provider for entity.
Which would construct a new meter provider with a new resource.
that has that entity attached to it. And then, when you're done with that, you would shut down that meter provider, which flushes it and exports all the metrics and all of that. So then, in that way, you could have, like, the global meter provider, which reports against everything on the SDK,
But then you could have one specifically for a session, for example, by constructing a meter provider for that session entity.
Which would layer that entity on top of the core resource. That's our current thinking.
that is not in the existing JS prototype right now, because we just talked about it
on Monday, a couple days ago, when we're still hashing out details. But that's… that's currently where we're going.
So… Yeah, I'm happy to, work with Martin to,
Join the prototypes together, if we think that we're at that stage.
**Martin Kuba** 24:44 Yeah, Dan, I'm definitely free to help with this.
Does this apply only to meter provider, or the other providers as well?
**Daniel Dyla (Dynatrace)** 24:51 It would be all of them. Yeah.
The meter is the one that we talk about the most, because it's the one that requires… it's the only one that has any real state in it, so it requires, like, flushing and resetting storages and stuff like that. With traces and logs, it's easy, you just start emitting different resources at one point.
**Martin Kuba** 25:16 The rip.
**Joaquín Díaz** 25:16 Yeah, sorry, I've had the same question. So, that means, like,
For example, if we combine the session with, like, session entity, I'm not up to date with this, I have no answer or anything.
So we have, like, a log provider attached to the session, and then when the session ends, we just, like, flash all the logs, or all the traces, and then we start a new one with a new session. Okay.
**Tedsuo** 25:46 Yeah, I'm so excited to… to see that in action.
**Martin Kuba** 25:51 And also, just to clarify, like, this is, like.
Yet another proposal from, like, what we heard, like, a week ago or two weeks ago, about using the,
the instrumentation scope?
**Daniel Dyla (Dynatrace)** 26:02 It's the same API, but instead of putting entities on the instrumentation scope, it is constructing a new resource that's at the top, like, the… where you… and then you would just,
Emit multiple resources in one export, if you have, you know, two different meter providers with different… bound to different entities.
**Tedsuo** 26:25 That is what I wanted. I'm so glad you guys tacked back to that.
I was getting a little nervous about the instrumentation scope thing. This… this sounds good to me.
**Joaquín Díaz** 26:37 And,
is this only one resource source entity active at a time? Like, I'm thinking about the session gates for the browser.
where we couldn't have more than one session at the same time, right? So when you…
We will end the session at whatever.
Browser event, and then start a new one on whatever browser event, or if the user one.
But we only have one at a time. That's fine, right?
**Daniel Dyla (Dynatrace)** 27:04 Yeah, that'd be fine.
**Tedsuo** 27:09 Luis… Okay.
**Daniel Dyla (Dynatrace)** 27:14 Actually, as it stands right now.
One… yeah, yeah. So I was gonna say more than one at a time is more likely to be problematic, but it's actually not.
Nevermind, you can… Ignore that for now.
**Tedsuo** 27:35 You can see an issue if you had multiple things changing this independently, getting some kind of, like, weird cascade of…
Little chopped up things, but… I don't know how much that really matters, since we're.
**Daniel Dyla (Dynatrace)** 27:49 Or how likely it is to happen.
**Tedsuo** 27:51 Right? So, I figured, just wait.
Okay, Abinet? Is that how you pronounce your name?
**Abinet Debele** 28:01 Yeah, that's right, Abernet.
**Tedsuo** 28:03 Thanks.
**Abinet Debele** 28:05 Yeah, so, I've created a new
a new PR for the navigation instrumentation?
That we have been discussing, in the past weeks.
So there was a page view instrumentation before that I was working on, and This one is…
I just copied a part of it, and then…
Modified it so, it, fits our current, definition of the navigation event.
So it uses Navigation API, and, the other History API, if navigation API is, not available.
So you can go through the PR and review it,
I cannot add more reviewers, I don't think I have the right,
So you can, yeah, you can look at it, and so I have… I also have examples, added to it. Maybe, if needed, maybe I can remove the…
The event, hiring, and just some of the…
Show the… the looks that are getting, sent to the…
to the, to the server, so we can, we can go through that if needed, but, for now, I just needed a review for the,
What a change now.
**Tedsuo** 29:26 Awesome.
This is great.
Yeah, please, please post this in Slack as well, if you haven't.
**Abinet Debele** 29:39 Okay, alright.
**Tedsuo** 29:42 Yeah, everyone, please have a look.
Cool. Well, we're coming to the end.
Just FYI, me and Martin are gonna be at a Grafana off-site next week.
That might… conf… but you're coming, right, Arden?
**Martin Kuba** 29:59 Yes, Anne, yes.
**Tedsuo** 30:01 So, I think we… we might not be able to attend the meeting.
So we won't be here, but you all should be here, and continue.
But we'll definitely be on Slack. So, see you there.
**Jared Freeze (embrace)** 30:17 Cool.
