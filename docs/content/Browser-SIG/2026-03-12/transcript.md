SIG: Browser SIG
Date: 2026-03-12
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**David Luna Bistuer** 00:13 Boom.
**Benoît Zugmeyer** 00:15 Yo.
**David Luna Bistuer** 00:19 Good morning.
Hey, what's up?
Thank you.
Hi, Dad.
**Ted Young** 00:33 We have a Jared Freezing on the call? It's cold there.
**Jared Freeze** 00:37 Yeah, so I've been trying to get used to Celsius. It was 30 yesterday, it is… Ted Young 00:41 That doesn't make it colder, because you switched to 16.
**Jared Freeze** 00:44 today.
No, I know.
Just irritating, more than anything.
58, dude. Sucks.
**I'm not into it, I know you live there, but… Ted Young** 00:58 - Yep.
Where are you at again, Jared?
**Jared Freeze** 01:06 New Orleans.
**Ted Young** 01:07 Okay.
**Jared Freeze** 01:08 Yeah.
**Ted Young** 01:09 That is unusual.
**Jared Freeze** 01:13 I was in Kahala for the last two and a half years, so… Ted Young 01:17 Nice.
Hells yeah.
**Martin Kuba** 01:31 Hello.
**Jared Freeze** 01:46 Oh, you're on a vacation trip.
Not yet.
**Trent Mick** 01:50 That starts on Sunday.
**Jared Freeze** 01:52 Sweet.
**Trent Mick** 01:53 Sunday, yeah, soon.
**Jared Freeze** 02:46 You wanna roll, Martin? I think this is more than usual.
**Martin Kuba** 02:53 Sorry, say again?
**Jared Freeze** 02:55 Oh, I was saying, this is more than who usually comes, so I was gonna say we could probably get moving.
**Martin Kuba** 02:59 Yeah, sure. Yeah, I just have a couple things to start with, just a quick update on the release, the release, So we did consolidate the instrumentation packages, the instrumentations into a single package.
Per the discussion on that one issue, so that issue is now closed.
And I have opened… A pull request for adding the release workflow.
release published workflow, so please take a look at it, let me know if you have any comments.
Once that's merged… Trent, I might help… I might need either your help or Mark's help to do the first publish.
to NPM.
**I think you'll… Trent Mick** 03:47 I think you'll need Mark or Dan, I don't actually have perms on NPM, yeah, yeah. Yeah, I'll reach out to Mark about that.
**Martin Kuba** 03:54 All that to say, I think we're getting closer to being able to do first release.
The other thing that I wanted to bring up is we have… two instrumentations, two new instrumentations that got merged into GSContrib.
I think a few months ago, and I would like to move them to this repo. That's the navigation and exceptions instrumentation. Are there any objections or any… they… so these… they were published, but they're not very… I don't think they have much usage at all, so… I think it's fine to move temple.
At this point, but I wanted to hear if anyone has any objections.
**Jared Freeze** 04:41 My only feedback would be to pick the package name we want.
and potentially leave what's there, like, in it, but marked on NPM as deprecated.
for the last package name, and just link. And that way, if there is someone out there, at least it's not breaking for them. But that way, we'll have, you know.
I guess we… it doesn't… it'll… it'll change no matter what. We don't even have the option, right? Because it's gonna be browser slash experimental slash whatever.
**Trent Mick** 05:11 It's moving into the single browser instrumentations package, I assume, right? Or they are. Yeah, that's right. Yeah, okay, yeah. Or in the past, when we've removed ones, we've just replaced the directory with a README that points to the old version of the sources. If you want it, it points forward to where the new place is.
So people don't break links, but yeah, cool.
**Martin Kuba** 05:32 Yeah, so I'll create issues for these, with… checklist of things that need to happen to move those, including updating the README and… Doing last release for the old packages.
**And… Jared Freeze** 05:47 So, I don't know if they got marked stable, but I know that there's semantic conventions, at least from some people on our side, at our company, for, like, Android, iOS, Kotlin, for exceptions that are getting updated, so it'd be cool if we could mark it as experimental on our side.
Until that work is done, and that'd be really nice to have that be the first one that's stable, that includes crashes and exceptions with the finalized, like, stabilized, you know, conventions.
So… Experimental, that's what I would say.
**Martin Kuba** 06:21 Yeah, for sure. Experimental.
**Trent Mick** 06:25 One of the reasons we haven't stabilized any instrumentations yet is we are not feeling like we've stab… are close to stabilizing the instrumentation package, OpenTelemetry instrumentation.
So, I don't know if that's necessarily a requirement, and maybe… browser's using less of the gross stuff in that package, so maybe it's easier to justify stabilizing some of them, but… I mean, they're stable, and then there's using stable semantic conventions, which is a subtlety as well.
**Martin Kuba** 07:04 Okay, tad, you have the next topic.
**Ted Young** 07:11 Yeah.
So, the entity SIG is talking to Josh Surith, and… They think it would be great if these two SIGs had a little more overlap, for the next little bit. We are… since Martin's working on a… A prototype for everyone to play with.
I think it would be good for them to start hearing from us more.
And I'm going on vacation for the next 3 weeks.
So, it's just my request. If there are people from this SIG who have time on Monday.
to drop into the ND SIG, I think they would appreciate it.
On a similar note, on the, Spec SIG. We've been doing these, sort of report backs from different SIGs, and that's turning out to be very popular. So entities did report back, We've had, like, RPC semantic conventions do a report back on what they're up to. Profiling came in and did a report back on what they're up to.
And I think the entity SIG were interested in kind of, like, understanding our roadmap, but I think it would be good to maybe just get on the schedule to give one of these report backs at the Spec SIG.
Mainly so that people understand what our roadmap plans are.
One of the things that came up in the entities, SIG is, like, you know, why are we concerned with the, design of the SDK, if we think we're going to have to build our own custom SDK in the future.
On the browser side.
And my request to Josh Surith was that, well, let's not make this about the browser versus, like, other components.
It's that the browser's a good example of something that needs traces and events, and we've got other systems that are good examples of places where we need to deal with metrics changing.
we haven't found a place necessarily where we need them all at once, so that will probably be Go. And it turns out Josh Surith has some… like, at Google, they have some needs for Python and some of these other SDKs to have this stuff in there.
So it isn't, like, isn't, in fact, just the browser that needs this stuff. We're already seeing other SDKs needing it.
But… we could be representative of those SDKs while we're still using one. So that's the other reason why I think it would be helpful for us to have a little more participation there.
I think one thing that makes it hard is it feels like… different people caring about different parts of it, and because we're the most vocal group caring about traces and events, I think it can come off a little bit like… like that's… that's browser stuff, which isn't true, but it is the stuff we care about the most.
So… Anyways, more long-winded way of saying it would be good for these sigs to be a little more, cross-pollinated, I think, until we get past the… Approving our prototypes and everybody feeling like we've figured the model out.
But it's a good opportunity for other maintainers and approvers in the SIG to go do that, because I'm going on vacation for 3 weeks, so I shall not do it.
There you are.
**Martin Kuba** 11:04 But are these, are these roadmap updates kind of impromptu, or do they have to be scheduled, like, to reserve time for that, or… Ted Young 11:13 We're start… we're starting to schedule them out a little bit. We don't have a formal process for that yet, really. We've just been kind of doing it through the just through the SIG agenda.
But, you can talk to Ludmila, was… was helping to organize some of it. Like, the TC is in charge of the… the spec meeting.
**Daniel Dyla (Dynatrace)** 11:45 I think they said all you have to do is add yourself to the… there should already be a schedule section for next week.
And all you have to do is add yourself there to volunteer. I think it's pretty informal.
**Ted Young** 11:59 Yeah. I don't know if there are people already planning or whatnot. I don't think we've put a list down somewhere yet, but that would easily be the next step, would be to maybe put a little section at the top of the meeting notes, or somewhere.
Where people could… could sign up.
But… But it would be good to do that. Maybe when we have a working version of the demo is, like, a good time to do that. Like, be like, here's a working version of what we're up to, here's our model, go play with this basic version. That'd probably be a good time to get that report back.
**Martin Kuba** 12:34 Yeah.
Makes sense.
Okay, david?
**David Luna Bistuer** 12:52 Yeah, just a heads up, so I'm just redid myself there. I will also bring that topic in the JavaScript sync. Seems that we have kind of an issue with, double prepping some APIs.
So, I just found out by doing testing on using interaction and browser navigation, both Instrumento, they patched the API, the history API.
Since that one wins over the other, and then… One instrumentation is not working, or at least for capturing events for that.
I'll work on… I'm trying to make a reproduction and create an issue, and file an issue with that reproduction.
Well, it's just a heads up on… I don't know, if you have… thoughts already on wrap? Because I know that we've already talked sometimes on… about defining APIs, on what are the browser APIs, and so on, that maybe we should rethink a little bit.
So, do you have any thoughts right now, just… maybe share with us. If not, I'll… maybe when the issues open… I'll share it in the Slack channel, so you can join the conversation and give your two cents.
**Martin Kuba** 14:03 David, does this, actually create some… some issues, like, that those instrumentations don't work together, or… Is it justified?
**David Luna Bistuer** 14:11 That's exactly what's happened. So, my use case, I just tried to bring all different instruments installed together. Browser remitigation was not working because user interaction was… I don't know, maybe it's the last one that was getting there and was winning.
And, yeah, you get user interactions.
But you don't get any browser navigations, you don't get any events from the browser navigation.
**Martin Kuba** 14:35 I see.
**David Luna Bistuer** 14:39 Okay, so, yeah.
**Jared Freeze** 14:41 I mean, my feedback is that it's always a bad idea. Like, this is the hack of all hacks that is to be avoided if you can have a listener. I understand that's not true, especially for Fetch, right? Fetch is the other… one that you just have to wrap. You can't observe it without a worker, and that's not available to third parties, right? So, I would like to see the exact conflict, because just… You know, taking the original and then replacing.
shouldn't, like, kill another part of the system. So, I think there's maybe a detail there to look at.
I don't think we can really make a general rule about it, because it's just required for, like, a lot of the functionality you're gonna want.
You know, to do these things, without observation, so… Yeah, can you post, like, a link? Do you have a repo you can share, something like that? Or is it literally just pulling in the two instrumentations that are there?
**David Luna Bistuer** 15:40 Yeah, I'll make a, for example, on a static web application that has both of them and makes some mitigations, so yeah.
I'll bring a repository.
**Jared Freeze** 15:52 I'd like to see it. Awesome.
**David Luna Bistuer** 15:54 Okay, good.
Thank you.
**Martin Kuba** 15:59 So this is a little bit related to the, to the issue, like, of moving all the instrumentations from JSContrib to our browser, like, to having the same package. Like, if we had these instrumentations in the same package, it would be easier to… To deal with, or to resolve.
They could, like, share some common mechanism for the wrapping.
I think.
Having them as separate packages makes it a little bit more… Difficult.
**Daniel Dyla (Dynatrace)** 16:30 Is that the plan, to publish one package that has everything in it?
**Martin Kuba** 16:36 That's the direction we're going with instrumentations right now, yes.
**Benoît Zugmeyer** 16:40 Oh, man, no.
**Martin Kuba** 16:46 I'll send you… Dan, Daniel, we had a discussion on this and an issue.
I hope you find this.
**Ted Young** 17:00 Yeah, it's all the core instrumentation, not… Everything that might ever exist in the future.
**Martin Kuba** 17:05 Yeah, yeah, that's right.
**Daniel Dyla (Dynatrace)** 17:09 Yeah, I mean, that's fine.
Yes, you could have a mechanism To share for the core mechanism… the core instrumentations, but you can't say that no, like.
user will ever install an instrumentation that also needs the history API. I think it does need to be solved in a more general way.
From what Chair had mentioned, I think you said that… replacing the function shouldn't break other parts of the system. Just from the way you said that made me think that possibly… You didn't… understand the issue here. The issue is that when you wrap a function, it unwraps before wrapping.
So it only breaks other instrumentations. It's not breaking, like.
the rest of the system being monitored, it just, like… kicks out The instrumentation that was applied first, when you apply the second one.
**Trent Mick** 18:08 That unwrapping first is only done in the node-specific instrumentation-based package, so not in the browser one. So that's why there was a discussion we had yesterday, and David was going to go look at why it's causing breakage on the browser side instrumentations, because there's something different going on.
**Daniel Dyla (Dynatrace)** 18:26 I've got it, yeah, okay.
**Jared Freeze** 18:27 Okay, so you're saying it explicitly unwraps.
**Daniel Dyla (Dynatrace)** 18:30 They're not just yet. Well, apparently not.
**Trent Mick** 18:32 The instrumentation base has an underwrap function that exports the Shimmer functionality. That was done at one point to bring the shimmer implementation into the instrumentation package.
For various reasons, the node base version does more than just call shimmer.wrap, it doesn't pass it through. One of those things is it does unwrap and then does a wrap.
It checks if it's wrapped, unwraps it, and then… and so it doesn't allow double wrapping if you have two instrumentations that are trying to wrap the same function. That's not done on the browser side, so… Some difference happening there, if there's a breakage.
**Jared Freeze** 19:10 Don't know yet.
Gotcha. Okay.
So… Tag.
**Martin Kuba** 19:21 Alright, thanks, thanks, dude.
Any other comments on this?
Fair.
So, the last topic we have from Benoit.
**Benoît Zugmeyer** 19:36 Yeah, hi. I wanted to bring up the discussion around, the browser URL.
attributes, so… In the Gita Bichu, there has been… a few back and forth, and… So, Martin, you proposed to introduce a page semantic.
Mmm… So, I wonder what everyone is thinking about it, Should we use both our page or something else?
**Martin Kuba** 20:18 Yeah, we had discussion about this last week, and we decided, like, to go with browser page… browser URL full.
Just to move forward. Then, like, when I was looking at the… PR, so I was realizing that all the attributes that we currently have in the browser namespace are to describe the environment, not the, like, the page or, you know, the page view context.
So I don't mean to rehash, like, the whole discussion, but, I guess my question was, would it actually make sense, like, to have a separate namespace, or separate for attributes that describe the page view, rather than, like, the browser environment?
Like, the browser namespace has… you know, things like the, you know, Chrome version, and… .
**Jared Freeze** 21:16 Yeah, just to… just to give you a little bit of what we talked about, like, the… we started talking about, like, what was immutable, and it was like, oh, there's certain things that are immutable, and then things that… that aren't, and it was, like, user agent. User agent is mutable, which it shouldn't be, but it… but it is.
Orientation, right? So screen size changes.
there's… it seems like there wasn't much, you know, platform, probably, and the browser name itself, like, that vendor name string, but it seemed like everything else was sort of up for grabs.
So, I think that was… At least part of what we talked about.
Yeah, I liked browser.url.full because it's… like, a singleton, and it's about the browser. It's, like, of the browser. So that's why I think it was preferred there, and then we keep the semantic invention. When you do something like app.page.url.full, I think App and page are, like, pretty overloaded, so we have to be really careful, because I think that there was a discussion at a certain point about micro front-ends?
And it's like, would each area be app?
Or is, like.
is apt the whole thing that you see, or, you know, what might that mean? And then page is sort of, like.
A larger scope than app in that definition, so it's kind of mixing the two's a little tough.
I think on mobile, it's way easier, because the app is just, like, everything. It's, like, the main container. For us, that's browser, so it kind of made sense. So that was kind of the rationale, I think, for browser.url.ful.
Sounds good.
**Benoît Zugmeyer** 23:05 Beautiful.
And what about… so, Martin, you proposed the screen, also?
What about the screen?
**Jared Freeze** 23:16 For… for what attribute?
**Benoît Zugmeyer** 23:19 Just screen.uil.fool, or something like this, yeah.
Because it's, it's something the mobile is also using, app.screen.
So, maybe we can… For this empathy.
**Jared Freeze** 23:39 I kind of… I guess I have the same opinion. I'd definitely like to hear from others, but when you have multiple tabs, you're not really describing the screen any longer, like, in the sort of intuitive sense.
You know, or… multiple windows, even. Like, that's probably a better example, is, like, having two separate windows. Would screen describe… You know, just the instance of that window, or just that tab.
**Benoît Zugmeyer** 24:07 Okay, I see.
And… Okay.
Well, I'm fine with any… anything, I guess, in an iframe, browser.url is a… a bit weird, maybe, because it's not the URL of the puzzle.
But… maybe… Doesn't mendell that much.
**Jared Freeze** 24:43 Yeah, I would say that's still legit, right? Because it is, like, a rendered… you know, area, like, context. Like, it is a window context of its own.
**Benoît Zugmeyer** 24:52 Hmm.
**Jared Freeze** 24:52 Maybe we could just label it as such.
You know, like, contained, or, you know, something like that.
But still use it, because, right, I mean, that's technically still… still true. You can't have iframes without URLs, but I think that would be considered part of the… Page context, like, the main page, right?
Even though it's an iframe. I think with that extra window of context with… it's completely self-contained.
I would probably still use browser URL full.
**Benoît Zugmeyer** 25:31 Okay.
Anywhere, let's think about something.
**Martin Kuba** 25:41 Yeah, I mean, to me, to me, like, the page, like, having a separate namespace makes more sense, but yeah, like, if any, I would like to hear maybe from others.
**But… But yeah, I don't want to hold this, hold this, hold this up, but we can, we can… We can… continue with browser URL full, and… Benoît Zugmeyer** 26:07 Okay.
**Jared Freeze** 26:09 I think one of the questions we keep running into is, like, do we need to share these across… like, how much do we want to, sort of.
have keys that share with mobile, right? Because they are, like, different paradigms. Like, is that important? Like, do I ever want to run a query that's like, show me every screen size?
Like, regardless of browser, app, you know, TV, kiosk, like, whatever it might, you know, something like that.
**Martin Kuba** 26:38 Yeah, I wasn't… I wasn't as much concerned about the, like, necessarily sharing, like, with mobile. I was more just, like, if semantically it makes sense, like, in, you know, like, in comparison to the other attributes.
Pro Browser.
Ted?
**Ted Young** 26:56 I wonder… I think moving forward with prototypes and, you know, getting data coming out of the system and trying it on different kinds of pages and environments sounds like… one way to get feedback from the audience. I wonder if, Just keeping track somewhere in a document of questions that have been raised.
like, we're going forwards with prototypes to, like, get stuff into people's hands, so we have some decisions where we're like, that decision seems fine, we're not worried about it, but we maybe have other decisions where we're like, we picked this, But, we're not certain that… that's necessarily the right answer, or we had questions about whether this is the right answer or not, but we picked approach A, and, you know, we wrote a prototype that includes that.
But if we could keep track of, like, question marks, that, you know, that would help us when we ask people to review it.
We could even give them some pointers to be like, what do you think about these parts of our data model?
Because those are probably the places where we'll get user experience feedback, people being like, well, in my world.
For example, Microsoft's not really as represented here as it used to be, but they were an organization that had, I think, lots of… their apps are composed of, like, different components, and each… like, component?
Has a potentially different team associated with the telemetry for that?
So that's an example of, like, having to break this down into, like, smaller pieces.
So, it just feels like maybe just getting, like, like, user experience feedback.
Would be helpful for some of these questions.
**Jared Freeze** 28:48 Probably put that into issues, right?
And then we can move it into the repo if it becomes something You know, sort of the stable… the stable answers.
Into the docs folder, right?
**Martin Kuba** 29:09 Alright, well, we're at time.
We're gonna have the topics… Question?
**Jared Freeze** 29:17 I was just curious if anyone here actually has an app or works on an app that has micro front-ends?
Like, I've personally never encountered it in my… Sort of build, you know, career.
I guess Microsoft is a good example, you know, where they have, like, departments for, like, parts of the page.
**Ted Young** 29:35 Yeah.
**Jared Freeze** 29:35 But any… anybody else?
**Martin Kuba** 29:37 We do.
**Jared Freeze** 29:39 You do.
Do you… are you leveraging, like, service.name at this point, or something else? Something like that?
**Martin Kuba** 29:48 Well, getting the app name, yeah.
**Jared Freeze** 29:50 Yeah. Okay, yeah.
**Ted Young** 29:53 Yeah.
They do their… I think they have all of their own stuff, so they don't do hotel, but Facebook is a great example of… Something laid out like this.
**Jared Freeze** 30:03 Hmm.
Yeah.
**Martin Kuba** 30:08 Yeah, I mean, microfinance is definitely a challenge, like, it's its own topic, I think, big topic.
**Jared Freeze** 30:16 Well, that's why I just keep going back to the word app, because somebody brought it up once, and I was like, that's a really good point. Like, that's an app to them, and the thing next to it is also an app.
**Martin Kuba** 30:26 So… Jared Freeze 30:28 That's why I hesitate to call, like, the whole thing. Like, for a lot of people, it'll just be one thing, but for others, it'll be siblings. Okay.
**Martin Kuba** 30:36 I hadn't consider that.
Okay, yeah, we're out of time, so thanks, everyone.
See you next week.
**David Luna Bistuer** 30:48 Thank you. Bye.
**Benoît Zugmeyer** 30:49 Thanks.
