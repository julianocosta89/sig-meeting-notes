SIG: Browser SIG
Date: 2025-09-25
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 00:42 Thanks, Jared.
**Jared Freeze (embrace)** 00:43 How's it going?
Hey, thanks for making the doc.
**Martin Kuba** 00:47 No problem.
**Jared Freeze (embrace)** 01:51 Hey, Wolfgang.
**Wolfgang Therrien** 01:56 Hello, hello.
How's everybody doing?
**Jared Freeze (embrace)** 02:03 Good.
I… We'll start by saying, I did not get the NX stuff done. Work's been a little hectic, and we don't have a package to run it on, so, that'll be delayed probably till next week.
**Wolfgang Therrien** 02:16 Dude.
I've also been a little bit delayed with the error instrumentation, because we've been dealing with a little worm that's been going around the internet, so we've been doing a lot of remediation for that kind of stuff, and… So we're digging ourselves out.
Sure.
Thank you, Martin, for putting up that PR based on our discussion earlier this week. I was just taking a look at it this morning.
**Martin Kuba** 02:48 Yeah. Yeah, I can, I can walk you through that, too, if you want, if you have any questions.
**Wolfgang Therrien** 02:56 No, I mean, I think it looks pretty straightforward to me. I guess the one question I had, we can jump into it whenever, was whether or not we wanted to also optionally include URL.template, because I know that we've talked a lot about that templatizing, that being a likely use case, and I wasn't sure if we were thinking that it was maybe premature to add That to the navigation event, because Or if we wanted to wait until we maybe had some proposed instrumentation.
**Martin Kuba** 03:30 Yeah, so… I guess my suggestion would be to… Maybe you start, like, with the few things that are straightforward, that we know for sure we want. You know, get that through, get that merged, and then…
**Wolfgang Therrien** 03:44 Yeah.
**Martin Kuba** 03:45 Then we can add… always add things to it, so…
**Wolfgang Therrien** 03:48 Yep, sure.
Hold on.
**Martin Kuba** 03:54 Yeah, I mean, I guess we're 4 minutes over, we can… we can get… I'm not sure if Ted is gonna join, but… There's… Nothing else on the agenda, so we can just talk about this.
So, I guess, the three… the four of us talked about this. David, you were not in that meeting, but, like, we had… the four of us met, like, on Tuesday and discussed the page view semantic conventions a little bit more, and we, Reached agreements that it made sense to, for now, just put that aside and define the navigation Event or semantic conventions for navigation instead.
The reason being that that's straightforward, and it seems like it meets our… are the use cases that we know of right now.
And then we can… we can… work on PageView later on, like, if you want to.
But, I opened a PR with Symante Conventions for a navigation event, And, yeah, so please take a look at it, I'm happy to talk about it if you have any questions.
**Jared Freeze (embrace)** 05:18 Yeah, I did have a question about same document.
Do you want to kind of explain your thinking around that?
**Martin Kuba** 05:24 Hmm.
Yeah, so, I mean, essentially… the, the navigation events can… Will be fired for… for hard page loads, but also for just, like, when the, when the URL changes without the document loading… without loading a new document.
And… So, like, the question is, how would you know?
Like, which one it is?
So the same, same document attribute is a… is a Boolean, which… which basically says, like, if it's… if it's true, then… then there was no page load. Like, it just… the URL changed, but there was no hard page load. And it's… it's not something that I came up with myself, it's actually in the spec. There's, the navigation event, from the spike.
It has, like, a destination attribute that has the same document attribute on it, too, so…
**Jared Freeze (embrace)** 06:21 And that's W3C. That's where it came from.
**Martin Kuba** 06:23 Navigation. Yes, yes.
**Jared Freeze (embrace)** 06:34 Does anyone know of specific products that are still using HashChange?
I haven't… I haven't seen it.
A long time, just curious.
**Martin Kuba** 06:51 What do you mean by using hash change?
**Jared Freeze (embrace)** 06:54 I mean, like, you know, Twitter in 2011, right, was using, like, pound slash username for a while, when they went to, sort of, SPA, but I haven't seen hash change.
Oh, sorry, using a hash for, like, true navigation in quite a while, so… Not saying we shouldn't support it, but I think that's gonna be pretty rare, right?
**Ted Young** 07:15 Really? I mean, I think that's the basis of, like, React and, like, all single-page applications, is that technique, isn't it?
**Joaquín Díaz** 07:26 Like… But… no, not anymore.
**Ted Young** 07:30 Not… people have just totally moved away from it.
**Jared Freeze (embrace)** 07:33 Yeah, using the fragment itself, yeah, I don't think is common.
**Martin Kuba** 07:39 So I think… With that said, I think that the navigation… Spec actually includes Hash change. So, like, if actually hash change does represent the navigation.
From the spec perspective, so, like, it needs to be captured.
I think… I think if you click, even if you click, like, over on a link with, you know, just, like, a jump to a different section of the page, it would actually count as a navigation.
**Jared Freeze (embrace)** 08:11 That's fair.
**Martin Kuba** 08:12 Yeah.
So, like, and in that case, like, if you wanted to distinguish, like, what… What, like, what a spa, like, a typical spa application would do, as opposed to just, like.
Adding a state, or jumping through, like, the same… the same… content, like, to a different page… different place in the content, then you would use, like, the combination of the same URL and hash change attributes.
Yeah.
**Jared Freeze (embrace)** 08:47 And then the other question, I know that this is older, but what does mobile mean?
Like, browser.mobile.
**Martin Kuba** 08:55 So, so all of the browser, the top-level browser, attributes that, hmm.
They were there before.
This, this edition, they came from, the… The user… user agent?
user agents, API, which gives you, like, the brands, gives you the platform, like the client hints, the client hints API. And there's a… so the mobile actually directly came from that, from that spec. It just… it's just essentially telling you whether it's a mobile device or not.
Hmm.
**Jared Freeze (embrace)** 09:41 Cool.
Yeah, I think it's a great start. I don't really have any feedback other than, my last question was, like.
for these URLs, like, where you have to exclude things, Like, where does that happen today?
Like, in the JS.
Is that, like, in the, like, for url.poll, right? There's, like, things you… you have to leave out. What's the mechanism for that? Because it seems like it's shared in a lot of places.
**Martin Kuba** 10:23 Is there a question, like, how to share… like, how to decide which semantic conventions to share, or… Sorry.
**Jared Freeze (embrace)** 10:31 No, never mind. I'll… I can ask on Slack.
**Martin Kuba** 10:34 Okay.
So, I think the… I think there's, with this navigation event, I think we can proceed with the instrumentation that's already in In flight.
I think it could just be renamed to PageView, but it essentially can… the instrumentation can be finished the way it is. The thing that's still TBD is, how we want to represent soft navigation, specifically.
So we don't have, like, any instrumentation right now, or any plans to implement soft navigations right now, but when the time comes.
Like, we need to… Talk about, you know, whether that should be represented as a new event.
Or as a… with just, like, an attribute on this navigation event.
Or maybe, like, we revisit page view.
I think that's… that's 2BD.
**Joaquín Díaz** 11:31 I think we should use the same event, but it is still navigation, even if it's soft navigation. We can add an ad for you if we have to define that specifically for soft navigation, but I think this event Congrat, you should call it.
I wanted to ask about the instrumentation.
So, I was thinking of… I was still with the idea of having multiple instrumentations that are Some of them optional, some of them suggested. That covers, like, most common use cases.
for navigation. So, for example.
Finding a navigation event when the page loads, which is the most, like, basic navigation, which is someone just load the page.
And then… yeah, I think we decided not to have any other, like.
instrumentation based on URL changes, which is fine, but we may have instrumentation for the different React for example, the different React libraries.
For that to emit navigation events.
**Martin Kuba** 12:38 Yeah, so I thought, I thought that we would… I thought it would make sense to have, like, a single instrumentation that would cover, like, any type of navigation.
Not, you know, not spot, not spot-out changes, but, like, any type of navigation.
Which is essentially what, what, Abinad, who's been working on the pageview instrumentation, has been doing. Like, he has, He captures, like, the hard page load, and he captures, like, history, history API calls, the instruments history.
**Abinet Debele** 13:14 Yeah, so the change… the change needed now, is it, to remove the spa-related, Changes, and only dedicate this to Hard to page load, or… should we still keep the SBA-related, children, like, feature?
**Martin Kuba** 13:34 So my recommendation would be to keep what you have, but just call the event navigation instead.
**Abinet Debele** 13:41 Instead of page view event, call it a navigation event.
**Martin Kuba** 13:44 Yep.
**Abinet Debele** 13:47 Yeah, for the SPA, we are capturing history changes, history push state and replace state.
I think we can also add, like, states and hash change, even if it's required. We can add those Two changes, too, and yeah, for the soft navigation, especially, do we still need to consider the… providing an API for, like.
User recent, page, page changes, like.
**Martin Kuba** 14:22 No, no, not for this.
**Abinet Debele** 14:24 Yeah.
**Martin Kuba** 14:25 Not for this instrumentation, no.
**Abinet Debele** 14:32 Yeah.
So what's the… What's the decision, or what's… what's the change required?
What's your suggestion for now?
**Martin Kuba** 14:48 So I would think that… Sorry, so I think that, renaming the event from page view to navigation.
And also, you might want to add instrumentation for the navigation API.
**Abinet Debele** 15:06 A new… a new instrumentation?
**Martin Kuba** 15:09 Yeah, so the navigation can happen through the history API, but also through the more modern navigation API.
So the Navigation API actually has an event that fires, so you can listen to, like, if the browser supports Navigation API, then you can just listen to the Navigate event.
**Abinet Debele** 15:31 Navigate the event, yeah.
**Martin Kuba** 15:32 And if the browser doesn't support a navigation API, then you'd have to, use the… History, instrumentation, like, wrapping the history.
**Abinet Debele** 15:43 Yeah, okay.
**Martin Kuba** 15:47 Dude.
**Abinet Debele** 15:52 Okay, that makes sense, yeah.
**Martin Kuba** 16:02 Okay, I'll find the link, hold on.
**Jared Freeze (embrace)** 16:05 Yeah, I… so I, that is… I worked backwards from the Kanban board, and that's the file I found. Is that the one you're working on?
**Abinet Debele** 16:20 Sorry, again.
**Jared Freeze (embrace)** 16:22 In the chat, I left a link, is that… is that your work?
**Abinet Debele** 16:26 It's not in the sandbox, it's already in the, the JSC country repo. The one Martin shared now.
On the chart.
**David Luna Bistuer** 16:48 Regarding this, I have a question.
We already have a repository for browser instrumentations.
Is that maybe a good candidate to go there? Maybe?
It's an experimental one.
Or just keep pushing and make it into the country people.
**Abinet Debele** 17:10 I haven't, seen the new repo. Maybe, I can check it, and maybe I can move this one to the dot, but, It depends. I mean, Martin, what do you think? Like, do we… we can also finish it here, and then we can move it to the new repo?
**Martin Kuba** 17:32 Yeah, I'm not sure, like, I… That was gonna be my question, like, I don't know if we've decided to make a decision to… to, actually put code into this repository yet.
But I think, Admin, like, I think for you, like, since you're in the middle of working on this, I would say just finish it. Finish it where it is.
**Abinet Debele** 17:53 Okay.
Just, I, I have one more question, like, so we, we removed one, attribute called state change.
That captures whether it is a replace or, push.
So now if we are, like, Probably considering, like, adding more changes like poked and hash change. Should we, reintroduce it, or name it in some different way, like, maybe… Name it calls and, add it to the… to the event.
So, to just capture what, what, resulted in the… URL change, or in the page view, or in the navigation of it.
**Martin Kuba** 18:45 Do you mean, like, the, the type of the change? Like, the push or replace?
**Abinet Debele** 18:51 Yeah, push, or replace, or pop, or it could be hash change.
Or it could even be Navigate, so…
**Martin Kuba** 18:59 Yeah, I mean, so this, there is a navigation type attribute in the, in the PR.
And that… that actually lines up with the, that includes… push, replace, traverse…
**Abinet Debele** 19:14 And reload.
Alright.
Okay, I can use that.
**Jared Freeze (embrace)** 19:39 That'd be… that'll be good to have, yeah. I agree. Yeah, just leave it where it is, because it's almost done.
And we'll figure out how to package, you know, in a little bit after.
Do a little research here.
Actually, I wanted to ask about that, too. Do we want to try to update some of the tooling and stuff, like, get away from… NPM and ESLint. Npm has a pretty nasty bug right now, that… It does that thing where it's stripping out, cross-platform libraries.
It's a regression they're talking about. There's only, like, one good version of NPM at the moment that doesn't, like, rip out, you know, roll up NES build for Linux.
Like the TVA, I don't know if you guys have seen this, but, Yeah, it'll, like, you know, everything works, and then it'll fail in CI.
So, is anybody interested in, like, fun, or biome, or anything like that?
Or do we need to align with the rest of the organization?
**Joaquín Díaz** 20:48 Do you know, like, I haven't been following all the other publishers, is fun on a stable release, already?
**Jared Freeze (embrace)** 21:01 That's a good question.
I've been using it a lot, but, you'll have to check.
**Wolfgang Therrien** 21:15 Yeah, I… I think it'd be interesting to see, like, what a proposal would look like there.
I mean, I don't necessarily have a problem with, like, moving away, like, moving to Yarn or another, sort of package manager, but I still would like it to be, you know, widely used and stable.
But also respect the fact that, like, maybe the web ecosystem is a little bit different than a node… than what is, than the Node ecosystem.
So, whatever… But I'd like… I'd love to see a proposal on, sort of, the direction there.
**Jared Freeze (embrace)** 21:53 Okay, cool. It is stable, by the way, it's at 1.2. So… Yeah, it's very fast. I know a lot of the tools are getting rewritten, and they're getting very fast, but, like, you know, ESLAN taking, you know, 15 minutes and certain projects and things is, is tough, so…
**Wolfgang Therrien** 22:09 Yeah, we… we just had a huge win moving to Biome for… for our… for our own tank, for sure.
**Jared Freeze (embrace)** 22:16 Okay. Ted, do you have any opinion here about not aligning exactly with the other repos?
**Ted Young** 22:23 I mean, I think alignment is… Really nice, but not the highest priority.
Right?
So, align until… until it's obnoxious, and then stop.
If it's obnoxious, then let's stop.
**Jared Freeze (embrace)** 22:42 Yeah, I mean, replacing it is super easy, too. I mean, if we have to go to Yarn, it's, like, one file.
**Ted Young** 22:47 Yeah.
**Jared Freeze (embrace)** 22:47 No big deal.
**Ted Young** 22:48 But just changing because this week we prefer a different package management system. Please know.
Yeah.
**Jared Freeze (embrace)** 22:56 I… dude, I don't want to go down the new front-end culture of, like.
**Ted Young** 23:01 I got in…
**Jared Freeze (embrace)** 23:02 Email, let's switch the business. Yeah, no, I'm not that kind of person, but… This has been going on for a while.
**Ted Young** 23:09 I'm that much of a browser sig.
**Jared Freeze (embrace)** 23:11 Yeah, no, that's too… too much front-end for me.
**Daniel Dyla (Dynatrace)** 23:15 If the alignment you're talking about is aligning with the other JS repos, too, keep in mind we made those decisions, like, 5 years ago.
**Jared Freeze (embrace)** 23:23 Okay.
**Daniel Dyla (Dynatrace)** 23:24 made them today, we might make them different, like, different tools are available, yeah.
**Wolfgang Therrien** 23:29 Yeah.
**Daniel Dyla (Dynatrace)** 23:29 certain… like, we were depending on Lerna, which is completely deprecated, and, like, there's all kinds of things that, if we started today, we wouldn't do it that way. And right now, you have… an opportunity both to ditch our baggage, which, if you want to, I would say go for it, and then also to model a new… way of doing it that the JS repos may follow, you know, if you… if you solve problems that we're having, we may… we may copy what you have rather than you copying what we have.
**Wolfgang Therrien** 24:03 Yeah.
**Jared Freeze (embrace)** 24:06 Yeah, that sounds great.
**Daniel Dyla (Dynatrace)** 24:07 I would love the JS repos as a model of the right way to do things, in 2025.
**Jared Freeze (embrace)** 24:14 Okay. So, does anyone have, experience with large repos, not using NX, like using TurboPack or some of the other… the other monorepo tools, because I've used NX before. I like the newest version. I think in the middle, it was, like, super verbose, and there was way… way too many… way too much config, but, does anyone have any feedback there?
**Wolfgang Therrien** 24:40 I've used, Turbo in the past, and it was… it was fine. Like, as advertised on the tin, I don't know that I have, you know, like, enough strong opinions to evangelize it.
But I liked a lot of the… I liked a lot of the declarative nature of it. I liked that, you were able to sort of… a lot of the features and the builds, caching stuff was… was useful.
But, yeah, I think, you know, in terms of hitting, like, what our requirements are for a build system, I think would be a really useful place to start, because then we can sort of back into a tool.
Good, good call, Martin.
We have two other topics on the agenda.
**Jared Freeze (embrace)** 25:32 Sorry, I thought it was just yours. Yeah, go ahead.
**Martin Kuba** 25:35 I think Carly is next.
**Karlie L** 25:40 Thank you, Marin. So I just list, one of my semantic conventions PR, for the user actions. So, there was two comments mentioned that there are some fields, they might be better to change to the attributes, so I want to see what, everyone here, think about it.
Because, that's still under the development status, so we can always change the litter, but, I just want to, see if, people think I should change to attributes, or, keep, it as it. So, yeah. So that's, just my, all one item? Yeah, thank you.
**Martin Kuba** 26:34 Okay, yeah, we'll… I'll take a look at this.
**Karlie L** 26:37 Yeah. Thank you, Juan.
**Martin Kuba** 26:39 Thank you, Garland.
Ted, and I think you have one more thing, Ted.
**Ted Young** 26:45 Yeah, we don't have time, but there is a new entities proposal from Josh.
I think, you know, there's been pushback from some SDK implementers around mutable resources. I think the main concern is how complicated… Things get around metrics.
And the metrics SDK.
And so this is a new proposal to leave resources in their current state as immutable and try to leverage instrumentation scope instead as a place to put session information.
I really don't like the idea of using instrumentation scope, because it doesn't… feel like the right, correct scope for something like session. It's not instrumentation by instrumentation, it's… it's holistic for the process.
But I think there's some good feedback. I see Dan's on the call. I know he tried to implement this in JS, the last proposal, and was just concerned by the complexity.
So… We're not out of the woods yet on this front.
Please have a look at this, especially if you've been working on prototypes.
**Daniel Dyla (Dynatrace)** 28:06 It wasn't as bad in JS as it was in Java, because… Java has a lot of, like, multi-threading concerns that we can kind of avoid.
Yeah, it did cause problems with, like, metric lifetimes and stuff. I understand browser is mostly worried about events, but yeah, the specification has to work for everyone.
**Ted Young** 28:27 you know, I would love to… I feel like my main feedback is, like, like, I would love to know those problems, and right now I feel like… like, it's like we don't have a great description of the problems with the last proposal, we just have, like, a new proposal with instrumentation scope.
So, my feeling is, like, instrumentation scope's not the right place to put it, but, like, we definitely learn things from trying to implement the last proposal, so maybe there is some third proposal out there.
That solves the… The… the implementation problems without Dragging instrumentation scope into it, necessarily.
I don't know what that is, but… but I just wanted to let people know, please have a look at this, in its current state, ask questions.
That's all we got.
**Martin Kuba** 29:25 Okay.
Sounds good. Any last thoughts or comments?
**Jared Freeze (embrace)** 29:32 Thanks for all the work.
A lot of PRs.
**Martin Kuba** 29:37 Alright, see you next week.
**Hector Hernandez** 29:42 Thank you.
