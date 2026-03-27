SIG: Browser SIG
Date: 2026-03-26
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/wIKw2pgv5MiJBhbXQOhLhALypLU19IahzJ4Ub9gyFCK46cZ10c3mOVehANxriFvX.NyxAqJMiNCW5E6Gv
============================================================

## Zoom Recording Transcript

**Maxime Quentin** 00:12 Hello?
**Martin Kuba** 00:14 Hi there, how are you?
**Maxime Quentin** 00:16 Doing great, and you?
**Martin Kuba** 00:18 Not too bad.
You're based in, in Europe, and…
**Maxime Quentin** 00:24 Europe, close to the… to the Alps.
**Martin Kuba** 00:27 Okay, nice.
So it's, like, evening for you, it's morning for me.
**Maxime Quentin** 00:34 Yeah, at your West Coast, right?
**Martin Kuba** 00:37 Damn.
**Maxime Quentin** 00:38 So… Portland, right?
**Martin Kuba** 00:41 Yeah, it's like 8.30.
**Hugo Levy** 00:50 Martin, I think you have a Swedish accent. Am I wrong?
**Martin Kuba** 00:54 Swedish accent?
**Hugo Levy** 00:55 Yes.
**Martin Kuba** 00:57 I'm actually from the Czech Republic originally.
But I don't think I have…
**Hugo Levy** 01:02 Go on it.
**Martin Kuba** 01:03 I don't think I have a typical, like, Slavic accent at all, so… Yeah.
**Jared Freeze** 01:17 Hey, what's up, everybody?
**Maxime Quentin** 01:18 Indeed.
**Martin Kuba** 01:20 Right.
**Maxime Quentin** 01:32 We're dozen notes.
9 I added stuff on the agenda, but I don't know if we want to start a… Hmm.
**Martin Kuba** 01:48 Yeah, I think we can start. There's probably enough of us here. So, yeah, go for it.
**Maxime Quentin** 01:54 Yeah, so, together with, Martin, we… Did you say Martin, or Martin? Martin, sorry.
**Martin Kuba** 02:03 Martin.
**Maxime Quentin** 02:04 Sorry. With marketing, we try to work on, end-to-end demo for the new release of the Boser SDK.
And, I started on a smaller prototype of a, like, web app demo.
That is loading the browser SDK with, like, some kind of default config that you can update.
And then, you have buttons that generate, like, like, browser events, such as, GSERR, or you can trigger logs.
The point would be, like, you can provide, then, some dedicated tracer and log URLs.
Can add custom attributes if you need to price some tokens or stuff like that. And then, you can start, like, ingesting some of it, or at least try to see what are the default instrumentation of the repo.
And my point would be, like, to add any new instrumentation we have, And kind of walk on this demo to update it, and… Right now, I'm hosting it on a GitHub page, on my, like, personal repository, but we could have some… either I have it in a demo section in the… in the browser, Hotel Browser SDK repo, or I have also a page that loads it.
That builds it.
anything that would be relevant for the demo end-to-end. I don't know what will be the future state of this, but it was just, like, a first draft, and also a good opportunity for me to see how you instrument it. I'm still pretty new on the hotel world, so… It was kind of a very cool experience for me to see.
How it works, how instrumentation are, added, how you, how processors are done and everything, so… If you're interested, I can share my prototype, but it's pretty new, so… I was just wanting to give you some insights about, what I've done so far.
So, yeah, that's it. Any question, any, like, feedback, or… Idea to improve this?
On the front tab?
**Jared Freeze** 04:36 I mean, it's awesome.
we should put it in the repo, if you're willing to… to do that, and then the action for pages, I think, is, like, 3 lines, so… That seems cool, you know? We probably just want one intermediate page, like a homepage, so that way we can have other endpoints for pages, because I think you only get one, right?
like, there's, like, one URL, so… Yeah.
Yeah. So I think we just throw an index in front of it, and then that's super cool.
**Maxime Quentin** 05:08 Let me take some notes.
Hmm…
**Martin Kuba** 05:16 So my thoughts on this are… so for context, I created that, issue last… the discussion topic last week. Let me share my screen.
this one. And… So… I think… well, I think what you have, Maximus, is great for, like, if you have it hosted on… on, GitHub pages, and… It… It's, like you… like you were showing, like, there's… you can, like, add in endpoints to actually ingest the data.
Like, that's nice, because it allows, like, someone to, like, not actually have to install anything, they can go, like, directly to the page, and they can, like, test, like, interesting.
The data immediately, like, to their backend of choice.
So I think that's definitely useful, and, like, we can, like Jared said, we can… we can add it, easily. The… the discussion that I created was… was the motivation behind this, was to… we've been asked by the… By… People in the Entity 6 and from the spec, to… Provide kind of an end-to-end demo.
Of how we envisioned things to work, including… Ingesting metrics, and how… and, handling, Entities, like sessions and page views.
So there's been… in the enthatistic, there's been a discussion about, You know, we won't… How, how do we handle, ingesting sessions, and also metrics.
Related, so… I think… The goal here would be to have something like what you have, Maxime, plus… plus also a collector.
And plus, also some backend that actually ingests and can display the data that we collect, the events and spans.
The collector, like, if we decide in this group that, we want to… we don't want to collect… we don't… we never want to send metrics from the browser client, but what we actually want to do is send events and generate metrics in the collector, then we should demo that. We should have some kind of working prototype of how that… how we see that working. And I think that's the direction we want to go to.
But I think that's… that's kind of… like, my… I'm kind of thinking, like, this might take a while for us to, like, work through these use cases in this prototype and demo.
also, and have discussions about it, and then once we have agreement in this group, then I think we should demo it to the… to the wider OTel community, like, go to the specs meeting and… Demo, like, what we… what we are proposing, that browser's gonna look like for all these different use cases.
So that's… that was my, kind of, motivation for this discussion here.
If you haven't seen it, please take a look at it.
And yeah, we'll go from there.
But I think what you have is a good starting point, Maxine.
Marco, you have a question?
**Marco Schäfer** 08:48 Yeah, I know there is this OpenTelemetry demo app, which has a web front end, I think it's, like, a Next.js or something like this, so why don't we use this app? Like, is it not widely used, or is it, like, kind of maybe outdated or something? Is there any reason why not using this? Because it has backend services and everything?
**Martin Kuba** 09:10 That's a good question. I mean, I think we could do that, that's one option. It has… I think the demo has a lot of different… parts to it. It has a lot of different services, I'm not sure if it's too heavy.
Been able to spin up all those things, And if you just want to simplify it, also, if you want to have just, like, a simplified use, like, test cases, like what Maxim has, like, on a single page, as opposed to, like, you know, browsing through, like, a whole application. I don't know which one is better, but I'm open to ideas.
**Maxime Quentin** 09:45 Yeah, if I can add on this, I think my demo, maybe for the end-to-end, might not fit. Maybe, like you were saying, Marco, like a real app would be better for an end-to-end demo.
I think my approach was more, like, to document the instrumentations.
And I have a direct feedback about what is reported when is reported when you generate an error, or stuff like that.
Also, I would see a good place, like, to demo instrumentation, and maybe, like, have a small, like, very brief, like, single page where you see everything, and you can just quickly test your intake, like what Martin was saying.
But your point of having a real app that is instrumented in the real world obviously would make sense for an end-to-end Demo.
I'm… yeah, I'm not just super sure how could, In terms of, deployment, and I'm not super familiar with collectors, so the page, single app, I mean, static app approach was super simple to me.
For the next, next steps, I'm… I'm not super clear what would… what would be the next, Step to other actual collectors and rear backend and stuff like that.
**Jared Freeze** 11:08 Well, I do have a suggestion for what you built already.
I think, now that I'm thinking about it, because you're right, like, you need Docker and all these other things in the… Main repo to get started, and it's… it's pretty big, like, it downloads, you know.
a bunch of layers and all these things. The thing I like about yours is, we have something similar, where we work that is for development, right? So, like, you can see the output of the instrumentation you're working on. So, I think the page you have is, like, closer to, like, documentation, and kind of a place to actually you know, see the output, so I actually think this is very useful for us, right, as authors, and for people that, yeah, want to test instrumentation without you know, needing to spin up anything else. So I do like that, you know, if we're committed to have Docker or not have Docker, I think this is still useful, because at the bottom, you have your event log. So, you know, if you're building something new, just, you know, being able to see Web Vitals here, like, what are the numbers, you know?
whatever, whatever you're working on, so I like that part of it, but yeah, this feels closer to Docs, which, I think has its own place, even if we don't expand it, so…
**Joaquín Díaz** 12:22 Yeah, I… I was about to say the same. I agree with Cherry, like, this serves a different purpose. Mostly, like, if you are working on the SDK, you can… Spin up this page locally, and then just test the output of the new fermentation, or whatever you're changing.
And you can see it, working.
And then, what Martin was sharing earlier is more like a demo. I… I've been… I worked before with the full hotel demo, and it's huge.
it runs, like, tons of services, because it's demoing everything that we do, out of sales, so… I think if I had a chance, I will not do that, and I will just have something in the repo itself, just, you know, for everyone who wants to see just the SDK working end-to-end, and not every other SDK that there is, and every other, like, collector and services.
Because, Yeah, when you run it, it runs so many things, and it's easy to miss the actual, like.
what you are looking at, which is, in our case, a web SDK.
I'm open to start working on that, to create the… just, like, connect the Grafana collector, the… Lt… that's good to me, it's type, I know. RGTM.
Yeah, I can do that as a first step, so we see logs and spawns somewhere in some collector, and then we can go from there.
I guess, like, all the… Session stuff and the entities, we still have to write the actual implementation, right?
So.
I think.
**Martin Kuba** 14:12 Hmm.
**Joaquín Díaz** 14:13 Yeah, I can start with that, so we have a place to play with, and then, we can go from there.
**Martin Kuba** 14:26 So I've been thinking about, where to have this, so we can collaborate.
I think the easiest that I can think of is just having a… A branch, branch in the… in the repo that we have for now.
And just, like, merge things into that branch.
And that way we can… we can con… we can even, like, prototype, like, packages that don't exist, or make changes to the instrumentations on that demo branch.
Does that make sense? Yep, okay, cool.
**Joaquín Díaz** 14:54 Sounds good.
I… I don't think I will… deploy something, like a Grafana stack somewhere, I think everything will work locally, that's fine.
**Martin Kuba** 15:05 Audio.
Yeah, if it's darker ice and easy to spin up, yeah.
**Joaquín Díaz** 15:10 Yeah.
**Martin Kuba** 15:14 Cool.
Anything else on this, can we move on?
**Maxime Quentin** 15:26 Yeah, I mean, I don't want to hijack the full discussion, but I updated the issue about the page URL document question we had, browser document, browser page, browser… I've… So, feel free to, look at the issue and bring any input about it, so I can, like, later update the PR.
like I was saying, I really like the document approach, it's very close to the web API, like, standards.
even if you look at document.url, the definition is pretty close to what we want to add to a hotel, so… Mmm… I found it pretty convenient to go, like, browse out the document.url.foom.
So yeah, feel free to contribute to the issue and… comment, or… Or reply, or… Or add blockers if you feel it's not clear enough.
So yeah, that's pretty much it on the topic.
**Martin Kuba** 16:35 Yeah, I think, I think… Are we in agreement here that, like, we need… we need to add something?
in the name, like, if it's page or document, that having just browser.url full is not enough.
**Jared Freeze** 16:52 Yeah, I agree, because you have the different scopes, right?
**Maxime Quentin** 16:54 later.
**Jared Freeze** 16:55 API frames exist, so if you say browser, it's technically, like, inside the viewport, and I feel like that might be confusing. It's just not intuitive, so I like document a lot, because it is the right scope.
**Martin Kuba** 17:07 Yeah, I'm plus one on that, too. I think I suggested Paige in the past, only because, historically, like, most of the vendors have used page.
In their cement… in their conventions.
But it… but the document actually… is the right term from… based on the W3C spec, so… I'm, you know… I'm in favor of that, if everyone else agrees.
**Maxime Quentin** 17:39 And do you want to… Oh, sorry.
**Joaquín Díaz** 17:43 No weapon.
**Maxime Quentin** 17:45 I was just saying, like, do we want to, put it as a new entity, or do we want to add it to the document, or what do you… What's your take on that?
**Joaquín Díaz** 18:03 I was out to say that, I agree that we shouldn't use beige. Like, we learned before that it's a very loaded term. Like, even for us, it's hard to define.
My only question would be, like, as you were saying, if we want to use browser.document, or just document.
I mean, document is very clear for us in the web, but if it's not prefixed by anything.
Like, anyone can… I've… a document that means something different on a different SDK, on a different platform?
Bye.
I don't know. I don't have a concrete example, but… And yes, it gave, like… I don't know if they're processing some documents, and they have, like, document that file name, or talk about path name, or whatever.
Like, it might be confusing.
**Martin Kuba** 19:06 Yeah, we can… we can bring it up in the, semantic convention seg and see if they have any recommendation here.
**Maxime Quentin** 19:18 Would, like, web.document an option?
Or is it… Web2… like, related to Brother, and then people would…
**David Luna Bistuer** 19:33 I think that if it's within the browser namespace.
It has the semantics that we expect that to be an HTML document and no other format at all.
So, if we put it as a… document as root without any enemy space.
As Joaquin said, okay, it's up to an interpretation.
Yeah, so we are kind of putting the browser prefix, we are scoping that, yeah, what we… talk about documents, when we will talk about browser documents, it's actually HTML documents that are being rendered on the screen, within the browser frame, or within an iframe.
**Martin Kuba** 20:19 I think there's, like, the naming, the attribute naming that does need to be clear. So I think browser.document would make it clear. The only question in my mind is, if we in this group feel like The page context or the document context should be modeled as an actual entity?
You know, that's, that we… you know.
that we manage in the SDK, and then, like, we basically send the entities attributes as resource attributes.
Then I… it's… I don't know… actually know, like, if this would work, and I think I would want to double-check with the semantic conventions and entities group.
**Jared Freeze** 21:03 I mean, would we think of it like a container? So, like, browser is, like, the application, and a document would be, like, tabs and iframes. Like, would that sort of be the scope?
Would it make sense for… browser.document.
I don't know, that kind of does make sense. I mean, document's a loaded term, too. I know it's exactly what it is, but you're right, like, the people working on databases may say, oh, document is… you know, NoSQL, you know, or something like that. So, I get that, too.
I get that, too.
**Martin Kuba** 21:37 Yeah, I don't know, like, if… do you know… do you know David or anyone, if, If you're modeling an entity, like, does it need to have its own top level?
Namespace?
And then at that point…
**David Luna Bistuer** 21:51 Sure about that.
**Martin Kuba** 21:52 Yeah, I don't know that either, so…
**David Luna Bistuer** 21:53 Nope.
But if we take, If I'm not mistaken, so, would… Entities are meant to be… March with Resource, I think?
**Martin Kuba** 22:08 Yep, yep.
**David Luna Bistuer** 22:09 Then, with that, we identify what is the origin of, of, resource, or something that is exporting telemetry to our backend, right?
So, talking about that, document may be… because maybe, as Jared said, so maybe we'll have two different windows, or two different taps.
With the same document, so they're displaying the same document.
But we are doing different actions, and we are doing different interactions with this, and they are generating different telemetry. So maybe document… or at least talking about the URL of the document, it's not enough to actually distinguish between both frames.
Right?
**Joaquín Díaz** 22:53 Also, technically, the document is constantly changing, because you are, like, Pushing stuff.
Into the document. So I don't think it's a good candidate for an entity. I think… I understand your approach. I think we should find a different name.
And that is where I find Beige better.
As an entity, to represent, like, the current URL and other stuffs. It wouldn't work for multiple tabs, although, see, I don't… I think we… may need… I know, we may need a different name for that, but I wouldn't use Tocumen as… Something that is constantly changing.
**Martin Kuba** 23:38 I'm only saying that because, like, I don't know how other vendors do it, but, like, in our SDK, like, we do… send… a separate… information about the page, right? It's not… it's not part of each of the signals, so…
**Joaquín Díaz** 23:55 Yeah.
**Martin Kuba** 23:55 Even though it's changing, but it's changing less frequently than each signal that we generate.
**Joaquín Díaz** 24:03 Yeah, we are tagging each signal with the page.
Which is not ideal, because we are duplicating that attribute a lot.
But, yeah, I see that we have the need of an entity representing that, but I… I don't know how to name it, but I wouldn't use the argument for that.
**Martin Kuba** 24:28 Okay.
I mean…
**Jared Freeze** 24:34 It could be tab. I mean, that's… that's a word we use, too.
Maybe that's the scope instead of page.
I don't know, this could go on forever. Why don't we do it online? Yep.
**David Luna Bistuer** 24:47 At least, at least in session replay, when I was working at Diane Session Replay, the tab was part… was the entity.
We were distinguished between, different types, doing different introductions, and then we were recording different things, so you know what it was, you were displaying one tap or the other. You were switching about that, so yeah, it was… Kind of, yeah, we had kind of this as a part of our set of entities.
**Jared Freeze** 25:15 Yeah, just to respond to Marco real quick. Yeah, that's always the problem, right?
That's always the problem, is like, you have dynamic content, and it's… is it still a pa… is it the same page?
Even if it's a different URL, like, what… yeah.
I know, yes. An app is mobile, so it's like, is it an app or not? Yes.
**Martin Kuba** 25:42 Okay, we've got 4 minutes left, let's go to the next topic.
David?
**David Luna Bistuer** 25:48 Okay, so maybe this is short one. Okay, I've explained, I think, a lot of things here, but since we merged the instrumentations in just a single package, I noticed that we kind of carried the… usually when the scope that we are giving when creating a trade show for Or, or logger for our instrumentations, we set the, packet's name.
For example, one example was the web vitals. So we had, at OpenTennergy slash instrumentation web vitals.
Okay, now, if we introduce more instrumentations.
Okay, there is only one packet's name, is, at OpenTelemnity slides for our service recommendations.
So, yeah, I was thinking, always, I was wondering what should be used as a scope, and if this scope should change or something. We discussed that in the… because I was just, yesterday I was talking with the English JavaScript about this, about doing… moving the… The browser instrumentation series, and then that came up as, like, okay, so what's going to be the scope?
I know that we have an export, so maybe… A good replacement would be… To have the export path of each instrumentation.
So then, this line becomes… at OpenTernity slash Processionism edition.
Sorry, you already… it's already changed, sorry.
So, yeah.
Okay, the other question was about… Those instruments are experimental, so those experimental Maybe people want to, have instrumentations, but, at some point drop the experimental ones, or the telemetry.
being exported by the experimental ones.
Should we use that experimental in the scope name, or not?
Or should we just filter some… some… with some other, Should we use some other logic to filter out things?
**Martin Kuba** 27:54 So from my… from my perspective, like, the experimental path has been… is mostly as, like, a signal that… about stabilization of the package.
**David Luna Bistuer** 28:03 Regional.
**Martin Kuba** 28:04 Not its name, you know, so…
**David Luna Bistuer** 28:05 Okay.
**Martin Kuba** 28:06 I would be in favor of not including experimental, and just have something like what we have here.
Yeah.
**Joaquín Díaz** 28:17 Yeah, I think at some point… We said that If the code is stable, we don't need to name it experimental.
Even though the semantic emissions are not merged yet, or may be changing, I think there's a different tag that's called dev, or in-dev, something like that.
it doesn't need to be experimental, so I'm in favor of not using experimental. Sounds bad if you're a developer trying to use this.
**David Luna Bistuer** 28:47 Okay, good. Then… that's it.
So, let the JavaScript signal about this, and then, you can already move.
the instrumentation from tip here.
Thank you.
**Martin Kuba** 29:03 So we're… we're almost out of time, but I just, very quick, I wanted to just do a quick sync, in this group about… How… how I think about, like, what we have on our plate for… for, like, the… For the foreseeable future, Like, let me just make it quick. I think… so we have… we've basically been in phase one, which is instrumentation, semantic conventions, and it's still not finished. Like, we have, instrumentations, but we still need to consolidate, the instrumentations, like, we have an issue for that, and we also need to finish semantic conventions. So all the instrumentations that we have have corresponding semantic conventions, PRs, and… We should… we should work on, just at least coming to an agreement.
And putting stamps on those PRs that, like, yes, this is how we want that to be, and then we can… we can have them work with the semantic conventions sake to… to get them merged.
So I think this still, in my opinion, should be our top priority, so if you're, like… and I think we need help here, for anyone who has capacity.
And, then we have the SDK distribution package, but I think I would put it as a secondary at this point.
And, this context and data model, which we just talked about, the sessions, entities, and metrics strategy, that's gonna become… a priority, because we've been at… we've been asked by… by other people from… from the entities SIG and SPECSIG to… to work on this, so… These two areas, I think, are top, from my perspective, top, top priority for this group.
Working on the, on the, On this, and this basically, right now, means the prototype, and… Prototype and demo, and then this is more concrete of just finishing the instrumentations that we have.
been working on.
Once… once this is settled, then we can continue on… the developer experience and optimizations.
Does this… align with how other… others are thinking, and I'm… I'm… Basically saying it also, like.
So that we're aligned and, like.
if someone is working… looking for things to contribute, I would point them in these two things.
**Jared Freeze** 31:36 Yeah, I mean, I think sessions is probably the most important thing.
We have to figure out, because it's a lot different than… You know, any backend model?
So, I totally agree. Just a side note, I would add, like, the contributor tooling, like, the thing, that Maxine did, onto developer experience. Like, that would be nice just to have.
documented, prioritized, whatever, because I do think, you know, if we want people to build instrumentation, it's a really nice place to be able to test.
But yeah, I agree, I agree with this. That seems fine. You may want to put… so, for optimization, does protocol also mean, like, compression?
**Martin Kuba** 32:17 Yeah.
Okay.
Okay, we're out of time, so…
**Jared Freeze** 32:34 Cool, thanks.
**Martin Kuba** 32:35 Thanks, everyone.
**David Luna Bistuer** 32:37 this week, mate.
