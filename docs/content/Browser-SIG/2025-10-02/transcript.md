SIG: Browser SIG
Date: 2025-10-02
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/TRdAx0v5aEjOIZ7cZ1gBb4k9_sXulPj2yLAC4TxMgb0LoDABgXOvDcJfsC5GEfNc.9kYJFEESDGZl5kBP
============================================================

## Zoom Recording Transcript

**Ted Young** 02:37 Hello, hello!
**Wolfgang Therrien** 02:41 Hello, Ted.
**David Luna Bistuer** 02:42 Bye.
**Ted Young** 02:43 How y'all doing today?
**David Luna Bistuer** 02:48 Good.
**Benoît Zugmeyer** 02:49 Good.
**Ted Young** 02:50 Nice.
Hmm.
**Martin Kuba** 03:48 Hello?
Good morning.
**Ted Young** 03:53 Good morning!
Duke.
Looks like a light agenda today.
I've been pretty… pretty out of the loop with My arm and everything.
How are things going?
**Martin Kuba** 04:56 So from my end, like, we had that discussion about the navigation, page view, events, I… I get a feeling that, like, this group is in agreement, And I'm not sure, like, if… other people outside of this group will have different opinions, but I think… Can we just… I mean, I guess, can we proceed with… You know, going forward with, like, an experimental… Instrumentation that goes with this, with the proposal, that people can try out before we, kind of.
Is that kind of the, you know, the process here?
I don't know how we can… how long to have that issue open before we say, okay, we made the decision, so…
**Ted Young** 05:50 I think we… I really strongly believe we should get to building things.
Especially because we've decided we're focusing on, like, the instrumentation and the semantic conventions right now. That stuff seems, like, totally… Easier for us to think… to get outside opinions about it.
If it's working code, and people can run it.
I strongly suspect it will be, like, any other major OpenTelemetry endeavor, which is, like, we will get, like, everything, like, worked out.
And then be, like, on our way to, like, shipping 1.0, and that's the moment when, like, the heavies in this space will be like, okay, I guess we have to deal with this thing, let us, like, come give you our opinions, now that it seems inevitable.
Right? That's, like, a common trope in OpenTelemetry, that that, like, happens. And so I feel like we should just accelerate that process by, like, how quickly can we get to pretending like we're launching a 1.0?
**Wolfgang Therrien** 06:54 That feels about right.
**Ted Young** 06:59 And I think the best favor we can do for ourselves is, unlike what we have done in the past, is really try to write down our design decisions and reasoning.
in the browser repo, so that when people do come back in, and are like, what, what, what? There's at least, like, something for them to read and critique.
That's definitely a thing I find when we reopen stuff.
and we don't have, like, a big history of, like, design, or it's like, go read these, like, epic, like, 400 post-long, you know, issues on this OTEP that we then turned into.
you know, spec PRs and stuff like that. I think… I think we would benefit from having Like, a very clear… Reasoning, not just a model, but some reasoning for, like, why we picked the things that we did.
That's condensed. I think that will help us in the future.
**Wolfgang Therrien** 08:01 It does… I guess, like, I'm… because I don't know that I've seen this in other places, so I'm like… I'm like, how does that manifest here, right? And there's a lot of different ways we can… we can do that. I think if we… Is this looking like, hey, like, the use case that we're looking at right now is being able to model page counts, and, like, this is how we're… this is how this semantic convention maps to that, this is how this… this is an imp… this instrumentation is an implementation of that, and, like, if you wanted to get Page count, for instance, like, this is, like, you would say, hey, get me all of these events by this name, and these events by this name, because this is hard navigation, and this feels like soft navigation, and if you add those two together, or group or split by them, like, like a one-pager like that, or is it something different?
**Ted Young** 08:46 I think it's like that. I think you've hit the nail on the head. Because we don't have a UI or a database, we tend not to write a lot down about how we expect this stuff To get used, and most of the time, that's fine.
But I feel like this domain in particular, there's a lot of, like, we want to replay everything the browser did, but then there's also a lot of, like… but that doesn't quite tell the story, so we want to create some synthetic things that really, like.
encapsulate what we want to do, and blah blah blah. And there's so many features you could provide.
For, like, Rum client stuff. Being, like, super clear that, like, this is… this is the observability we want to do, and this is why we made this data.
Because then that would give people something to grasp onto that's very concrete. Like, no, you don't want to look at page count, or you don't want to separate soft and hard navigation for these reasons, right? We would cause other people to be coming to us and explaining the observability they're trying to do.
And I think that will help us… Avoid talking past each other.
**Wolfgang Therrien** 10:01 Yeah, anchoring around the use cases, and it might be that we have great ideas for use cases, but maybe we've either put those aside, like some of the synthetics that we're talking about, in favor of getting more, you know, closer to the browser-type events right now, it might help us focus. And it's like, great, write up that use case, and, like, at least then we have it in our pocket so we don't lose it.
**Ted Young** 10:24 Yeah. Okay. Yeah, exactly. I mean, there will be more use cases, and more people will come to us and be like, can you add this thing on, and this thing on, and this thing on, and we'll eventually hit some point where it's like, wow, all the data we want to ship is, like, creating… network resourcing issues, or whatever.
**Wolfgang Therrien** 10:44 for that. I can't wait for that.
**Ted Young** 10:46 Yeah, likewise. I feel like the history of this SIG is kind of maybe over-focusing too much on, like, optimization and kind of, like, 2.0, 3.0 kind of stuff, and be like, we know we're gonna have to do all this stuff in the future, so let's, like, make our data model really weird today.
But what we're kind of finding is actually the browser environment a year from today is, like, pretty different from the browser environment from, like, 5 years ago, so even, like, what we'd have to do to optimize.
It would be so much better if we just were like, this is the data we're trying to produce, this is the observability we're trying to do with that data, and let people come in and tell us that we're dumb.
And, like, there's, like, better ways to accomplish our goals. If we don't provide people with that framework, they're gonna come in, and they're gonna point at, like, little micro-optimizations and, like… you know, it'll be hard to, like, to, like, make a decision with that information.
**Wolfgang Therrien** 11:49 Okay.
**Ted Young** 11:49 Yeah.
I think it's also extra weird, because we're trying to live in this world where we're… this isn't… we're trying to not see this first round as, like, specialized data, or at least I'm not trying to see it as, like, specialized browser data that you do specialized browser-y stuff in. I'm like… step one is, like, can I just get my dashboards and, like, alerts and, like, stuff? Like, all the usual… baseline of observability that I use everywhere? Can I get that for the browser? And can we give people that? And then pivot to, like, maybe more, like.
Real user monitoring specific kind of…
**Wolfgang Therrien** 12:38 Yeah.
**Ted Young** 12:39 kind of tools and things. Like, the basics should be, like, can I just shove this into any old logging tracing metrics backend and get, like, useful stuff out of those backends that they do in, like, a generic way? What does that look like?
So, to that end, what about our, project Board.
If I pull that up… I'm wondering if we could just… just go over it real quick and make sure that the issues that are actually listed, especially under semantic conventions, match what we're currently doing, and then we can get to the rest of the agenda.
So… I just… green… Okay?
So, this is what we currently have.
So, for semantic conventions, We've got some maybe new things in here.
**Martin Kuba** 13:52 So I did…
**Ted Young** 13:53 How's your observability model? Go ahead.
**Martin Kuba** 13:56 Sorry, Ted, so this was, this was just a fucking draft, task there, and I converted it to an issue, since now we have a place to put it as an issue.
**Ted Young** 14:05 Great.
**Martin Kuba** 14:05 And, and I linked it, linked it to the, to the PR that Joaquin is working on.
Did I? Yes, I did.
Because Mark has the proposal for the… for the data model, so…
**Ted Young** 14:21 Okay.
**Martin Kuba** 14:22 I'll do that, yeah.
**Ted Young** 14:23 So Joaquin is working on this one?
**Martin Kuba** 14:25 He's, yeah, he's working on the, he has the PR open, yeah.
**Ted Young** 14:29 Okay.
And this is where…
**Benoît Zugmeyer** 14:33 I have a small question. I noticed that, so, in his PR, he's listing the events that we are… that are related to the browser, but in the semantic convention, there is also the attributes, resource.
resource entities, and that… Like, for example, the device could be interesting.
Should we mention it there also, or should it be in a different document?
**Martin Kuba** 15:08 Yeah, I feel like it's, like, right now, it's just that PRS is for events only. And I had the same question about spans, because I think we'll have… we'll also want to model some things as spans.
So it seems to me like it's not complete.
Yet.
**Benoît Zugmeyer** 15:25 Okay, I guess that's fine.
**Martin Kuba** 15:27 Yeah.
**Benoît Zugmeyer** 15:29 Yeah, I find it super useful to have this list.
**Ted Young** 15:36 And… Is… Joaquin's working on the observability model, right?
So we can put a… In progress label.
**Martin Kuba** 15:46 Yes, I think so, yeah.
**Ted Young** 15:51 That's… Only something I can do here.
Man.
They really did their best to make their project stuff work as stupidly as possible.
Well… In progress.
I find that this table view is the only place where I can, like, actually do everything.
But then I can see everything better when we look at these Kanban boards.
So… that's annoying.
Anyways, I don't want to spend too much time on this, but, since I'm just getting back up to speed… Do we have any more… In progress… events?
That are not listed here.
The things people are working on that are not listed here?
Seems like… We're good.
And we have a couple open that are listed as available. Consolidating the user agent and browser namespace.
Does anyone want to take this on? I know… I think, Martin, you were looking at it before.
**Martin Kuba** 17:24 Is this some… I'm like, I can… I can look at it for sure.
**Ted Young** 17:30 Or somebody else.
**Martin Kuba** 17:32 I'm not sure, like, who opened it, like, was it.
**Ted Young** 17:36 This is, I think, left over from a while back.
**Martin Kuba** 17:40 Yeah.
**Ted Young** 17:42 But we were looking at user agent and browser.
Maybe this is something that goes away?
I don't know how much user agent stuff we already have there.
**Martin Kuba** 17:55 Let me look at… take a look at it and see if there's anything overlapping.
I thought… I thought there was… there were some attributes… I think I understand the intent here.
But there's… there's some attributes in the browser namespace that, are unique to, you know, what we get from the browser.
So I just wonder, maybe we just look at… what's… if there's any overlap, and I can… I can comment on this issue, yeah.
**Ted Young** 18:27 Yeah.
I personally think it's… if there is overlap around user agent stuff with other clients and things, then… I don't know that I'd want to put it under browser, that'd be the number one thing to check.
And then adding platform version to browser resources.
This seems like a pretty straightforward…
**Wolfgang Therrien** 18:54 I can probably look at that one in the next, week or two.
**Ted Young** 18:59 Great.
Who just spoke, sorry.
**Wolfgang Therrien** 19:03 I'm sorry, that was me, Wolfgang.
**Ted Young** 19:05 Okay, great.
So… We go to this one… Chinese… Do we have you in the system?
**Wolfgang Therrien** 19:25 I did… submit that issue, so I can double-check on that. It should be Wolfgang Codes. I think I was added to the org.
**Ted Young** 19:36 Oh.
I expect you to be available in here.
But… We can figure that out afterwards. Alright.
Maybe it's only allowing people to be assigned who are, like, maintainers or something. It's a little weird.
Anyways… And for these listed as in progress, Are these all still open?
Defined browser observability model, obviously.
browser… Page view event.
**Martin Kuba** 20:20 That's the one, that's the navigation one.
**Ted Young** 20:22 Yeah.
And then navigation timing event.
And then Carly…
**Martin Kuba** 20:33 That's for me, so…
**Ted Young** 20:38 And Carly was going to pick this one up again.
**Karlie L** 20:42 Yes.
**Ted Young** 20:48 Are you back to working on it, Carly?
**Karlie L** 20:51 Yes.
And, yeah, because previously, I think I resolved most comments, and there was new comments coming, so I want to, know what everyone thinks, if we should put some fields to the attributes or something. So, yeah, I want to get more comments far from that. Yeah, thank you.
**Ted Young** 21:11 Okay.
Is there something you specifically had a question, that you want our opinion about?
**Karlie L** 21:21 Yeah, I think I left some comments unresolved, and those comments, I need more feedback. Yeah, thank you. Thank you so much.
**Ted Young** 21:29 Just… everyone, just go look.
**Karlie L** 21:30 Yeah, thank you. Great.
**Ted Young** 21:33 Okay That appears to be everything open.
Moving on to the agenda, David, you want to take it?
**David Luna Bistuer** 21:43 Yeah, basically it's a question that was listed yesterday in the JavaScript sync.
Which is that we, from time to time, and recently have been, getting issues, regarding bundlers.
And in order to just, you know, take a decision and to align with the browser seq, the idea is to actually, well, raise the question here, but which browsers, and specifically browsers and versions, sorry, bundlers and versions we want to support.
For that. We… I think that… kind of a month or two months ago, Mark, which is a maintainer from the JavaScript repo.
we… he added some bundle tests, but I think it was with a higher version of Webpack 5, I think, or Rollup.
So… Once we have the list, then we can… we can work on giving support to that, add tests for these bundles, and make sure that we are not breaking changes if we're doing… if we are not breaking bundles, if we are doing changes in our, in our packages in the contribository. So then it's easier. If we do something on browser, and then we want to move it to contribute, or the other way around.
We won't have these compatibility issues.
So, I don't know if you have a list already, take your time, put it here, maybe you can open an issue and have a discussion there.
But…
**Ted Young** 23:10 And just to clarify, this isn't something we have a choice over in the sense of choosing which bundlers we want to use. This is… end users are going to use whatever bundlers.
**David Luna Bistuer** 23:20 Exactly. Exactly.
**Ted Young** 23:22 You have to decide what the spread is.
**David Luna Bistuer** 23:25 Yeah, it's not an API, but it's something that we need, you know, to have a specific list of persons and… and boundaries that we are going to support. And actually, if we do some changes on that, then we should advertise it as breaking changes.
**Ted Young** 23:41 Do people have, like… data… available… is there data available we could use to, like, back our decisions?
I… I'll admit, I don't… I feel like I don't know the state of JavaScript bundling, because it probably changes every 6 months.
**Benoît Zugmeyer** 24:05 I don't have data. Webpack 4, it seems quite outdated.
Webpack 5 could be a good target.
**Ted Young** 24:17 Yeah.
**Benoît Zugmeyer** 24:19 And then, yeah, flights.
It is good.
I don't know.
**Martin Kuba** 24:27 Maybe, maybe you should create an issue for this, and… Get some feedback from a bunch of people.
**Ted Young** 24:34 Yeah.
**David Luna Bistuer** 24:36 Let me create an issue in the browser repository, and then.
**Martin Kuba** 24:40 income.
**David Luna Bistuer** 24:41 discuss it there? Okay, I'll do that.
**Ted Young** 24:43 Yeah.
Yeah.
I… I mean, I guess it's an interesting question, whether the browser community uses different Bundlers Than the Node.js community.
Because is that… is the issue essentially that it's not that we're making things that are breaking, so much as people are maybe trying to use our existing JS stuff with bundlers?
That they maybe weren't trying in the past.
I guess, maybe another way of phrasing it, is it… is the problem new code that we're shipping, or is the problem having to do, like, a review of, like, all of the code currently in the JS repo that we might pull in. It's like, there are lots of code that's having problems with… Webpack and other things.
Does that… does that make sense?
**David Luna Bistuer** 25:58 Kind of.
For what I know, the test that we already have right now is, like, B… gathered components, we create a small… with the SDK APIs, we build something that actually is, We maybe set up the tracer provider and so on.
We did that model scheme that fetches different components from different packages, and then just, we try to bundle that, and see that it's not giving any kind of error.
We kind of… at least what I know is that we have kind of the golden path, what is the easy?
For example, that issue that I was, as I was pointing here in the document is, Webpack 4 doesn't support subpaths.
That we are exposing, but yeah. So, yeah, the idea is, like, okay, if we want to support these versions, then we should, make tests for… not all edge cases, but for specific bundles and for specific use cases that… in that case, I think that they want to just import a specific Component which isn't international path specific for browser, but… Okay, and if you're just importing whatever comes from the package, you get the whole module, and it cannot be 3 shaken. So, this kind of thing. So yeah, it's more of, like.
**Wolfgang Therrien** 27:19 Yeah.
**David Luna Bistuer** 27:21 From the point of view of consuming packages, if it's actually doing the tree shaking properly, and actually it's… We are optimizing the way. I think it's kind of… it will help us on… on this issue that… or it is concerned that we have used in the browser, that it's always either on the bundle size. Right. We had some… I remember Martin tried to promote a Web SDK, but since you are importing a lot of models, the size of the model was some kind of concerning.
So, yeah.
That would be… maybe will help us to shape the modules in Core Repo, and also contribute repo to be more friendly on-tree shaking and bundles. But it's good to know which is the… at least the baseline that we…
**Ted Young** 28:08 Right. We want to support.
**Wolfgang Therrien** 28:11 Yeah.
**David Luna Bistuer** 28:13 There is an ongoing discussion, well, it's been on standby, but, on actually, having proper ESM output on, on, on Contrip.
I'm trying to push that into the agenda.
Which will help us, as well, because right now, it's like, the packages that we are compiling, we are… it's not… it's not ESM, this is ESM-ish.
But not, correct DSM.
So, that would be… The idea is that to make even friendly for funders and for browser… for browser instrumentations to be… to live in the… in the country as well.
**Ted Young** 28:53 Okay.
But it's not… I guess what I was trying to ask about was, like, is there a bunch of code we're trying to share that already exists, you know, that's mostly today gets run in Node, and we're discovering the way that stuff that's already stable and out there has been, like, packaged up in a way that, like.
It's gonna create problems for us.
In the browser. Where reorganizing it would actually be problematic, right, because we'd be…
**David Luna Bistuer** 29:23 There are some packages that are exporting, like, for example, in Exporters and Core Repo, there are… they have different, if you check the packages and they have different export paths for browser and Note.
They're using the browser property to be friendlier for bundlers, but in some situations, it's not working. So some situations, they are pulling, code from Node in browser, they are pulling code from Node, and… or sometimes they… there are types from Node that are linking to browser when you are trying to, do something in browser. That's because of this… You know, this way of we are… yeah, the way that we are publishing the packages.
**Ted Young** 30:07 Okay.
**David Luna Bistuer** 30:08 So they are meant to work in both, or at least to be… to provide only the code that is for… target for each platform, browser or not, but sometimes it's not… we don't… we don't have the… the, perfect solution for that, so… Yep.
**Ted Young** 30:23 But it's possible to go in and just reorganize how it's being bundled and exported for web without… destabilizing.
the node users?
**David Luna Bistuer** 30:36 That's something that is, yeah.
Maybe, but we need to go case-by-case, I think.
**Ted Young** 30:42 Okay. Yeah.
**Benoît Zugmeyer** 30:44 I think if we can come up with a list of requirements instead of a list of vendors that we can support… Could be nice.
Because, like you said, there is lots of bundles different in the world, so… Yep.
And, and Tripath is good, yeah, it's, it's good.
It's a good one.
**Ted Young** 31:10 Seriously.
**David Luna Bistuer** 31:10 Yeah, no.
**Ted Young** 31:11 Like, like, looking at features that… bundling features that we support, and then based on supporting those features, we know which versions of which bundlers work.
**Benoît Zugmeyer** 31:21 Or, all the users will know if their setup will work.
**Ted Young** 31:26 Great.
**Benoît Zugmeyer** 31:27 Give feedback.
**Ted Young** 31:30 Right, okay. That's kind of how we're looking at browser support as well, right? Saying, like, we want to… lean on these APIs, and based on picking that, we now know what our compatibility looks like, but… It's not because we just picked things that are popular.
Cool.
Well, that's it for the meeting, I will see you all, on GitHub and on Slack.
Let's see if we can land some of the… start landing some of these PRs.
**David Luna Bistuer** 32:05 Have a good day. Bye.
