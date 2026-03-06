SIG: Browser SIG
Date: 2026-03-05
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/ajTKMeiBO3rQ9MUKZI_D_2fUWYKEUsImaYvweNOYNi0-K0IAo8AXhitOHy9surSB.oFXpOHwMjhQu8meH
============================================================

## Zoom Recording Transcript

**Jared Freeze** 00:13 Yeah, Benoit.
**Benoît Zugmeyer** 00:16 Boom.
**Jared Freeze** 00:23 How's it going?
**Benoît Zugmeyer** 00:27 Good.
Nope.
**Jared Freeze** 00:30 Good, good.
Yeah, we have a lot today, which is nice.
Hello?
**Benoît Zugmeyer** 01:09 The first point is… is…
wrote from… someone from my team. He's not there yet, we can maybe start from the second point.
**Martin Kuba** 01:23 Okay, okay.
Yeah, we can, we can start,
So, this is, like, a follow-up on our discussion we've had over the last few weeks about release publishing and versioning.
there's… I added,
you know, you, Jared, commented last week. I… I commented last night, added a proposal.
to, how to move forward. Basically, I think we're all in agreement that we want to have a single package for all instrumentations.
So for that, I already opened PR to consolidate all those instrumentations into one. That's the first link here.
Please take a look, review.
And then, the other part is adding…
this OpenTelemetry browser package, which would be, kind of like the main entry point for… for our users. It would contain,
Like, the… like, the configuration layer, some defaults, that would be recommended defaults.
And, we don't have… and… and…
We can put, like, the session… session management in there for now.
The one thing that I wasn't sure about, is if we needed…
to have a separate SDK and API packages.
I think it's possible, but we don't, you know, it's not…
I don't think that's something we need to solve right now. I think we can just start with the browser package.
And, move on.
Any questions, or…
About this…
**Jared Freeze** 03:21 I left notes on the PR, but yeah, it looks good. I like that it's sort of all one build system. Yeah, the only feedback I had was around testing. Because it's not a single test command, I think it gets a little tricky.
But other than that, I think it's pretty much solved, so thanks for doing that.
**Benoît Zugmeyer** 03:46 in the instrumentation and the browser SDK packages, is there any plan to bring in,
Instrumentations that are not part of the…
OpenTelemetry browser repo at some point.
Or will we focus on the one we have here?
**Jared Freeze** 04:10 Yeah, I think the intent was to bring over absolutely everything. Some will retain names, and I think some will not, because…
I mean, I was kind of thinking about it like navigation timing, where it's using span events, you know, or something like that, and we have something called navigation, which is totally different. Like, it'll generate different data with the same
like, data set?
So, we'll have to decide, like, what names we want to keep, or what we want to deprecate on the other side. So, we may not have to move everything, but we should move all of the things that we find really useful. Yes, I would like to see them in our cell browser. And that was the initial reason, like, for having the repo, and then keeping the name.
Also, changing the name, I mean, there was some… I, you know, Ted brought this up, I think it was in the very first meeting, which is, like, some of them are, like, web- some are, like, instrumentation-web, and some are, like, browser, blah, you know.
So, just aligning those as well. I think we try to do all that in… in this, repo.
**Benoît Zugmeyer** 05:17 Okay.
**Martin Kuba** 05:29 Alright, so if there are any… if there are no more comments on this.
We can circle back to the first,
Staying on the agenda for Maxime.
**Maxime Quentin** 05:41 Yeah, hello everyone, sorry, first, it's my first time to this SIG, so I'm a software engineer, and I'm interested in the, like, Border SIG, for hotel, and I've, opened an issue, this week regarding,
like, navigation and page URLs, because I just wanted to be able to emit a signal of a click with a dedicated URL, and…
Like, for instance, just which page you are clicking on, and stuff like that.
Obviously, the current network URL we have with a URL full is not really relevant here, because we are talking about, like, a location HREF or something like that.
And so, yeah, I was just wondering if, anyone have a suggestion about,
What namespace could we use? What,
New features… fields we could introduce, or stuff like that.
**Jared Freeze** 06:46 Yeah, I had two comments. So, I looked back through our source code, our SDK is fully OTEL.
We actually switch back and forth between the two. So, url.full applies to the resource, and it sometimes applies to the page, depending on the context, which is confusing. I would like to update that to whatever we decide as a group.
This gets into the rest of the discussion, which is, like, what does browser.me? Like, browser.star. Is it things from the browser? Is it things about the browser?
You know, is… app.url.full… like, are you describing the app?
is the app everything in the window? I don't necessarily have good answers to that, but, I think it's sort of all the same topic, which is…
Yeah, I would say we should not be overloading it. Like, URL.full in any given
Like, top-level attribute should not have two meanings.
**Maxime Quentin** 07:45 Yeah, good.
**Jared Freeze** 07:45 So…
**Maxime Quentin** 07:46 end of the…
I mean, by reading the… I naively read the documentation and the specifications, and it specifically said, like, network call.
So, for me, it's like you said, it's a resource URL, and has nothing to do with the location or web app URL, so it could be,
Something that is not… not even, like, a…
That is on a local web view, or something like that.
So I think, like, some… like you say, something like navigation or app.
Location, or stuff like that.
Would feed to me, but .
**Jared Freeze** 08:32 I will say, one of the things, I've been trying to do is reuse as much as we can, right? Like, not inventing stuff if we don't have to. Url is one of those things that, like, doesn't map to the browser, right? Because it… for us, it is location.
There… there is also a URL, but it's… it has historically been location.
So, I guess if we come up with a new…
key, I would say that's… that's fine, too. I like the url.full, url.template.
kind of…
you know, prefix. I… does anyone know off the top of their head if there's any precedent for, like, namespace, dot, and then reusing kind of a top-level key? Like, if we did browser.url.full, would that be…
Like, intuitive, or aloud, or a good idea?
**Ted Young** 09:24 For semantic conventions, you mean?
I think when you prefix everything with browser, it starts to assume that there aren't, like, other things that would want to use the same convention. I think that's the only…
The only issue with that.
But you'd want just URL, url.full if you're… Doing a URL.
But I get that we're also talking about, like.
you know, there's, like, the URL of the page versus the URL of an HTTP request and things like that. I'm not sure.
**Joaquín Díaz** 10:05 I think… I'd like that to be, like, browser that you're loaded up for.
But I'm trying to… I'm looking at the browser, like, current browser attributes.
And they seem to be things that don't change over time, but the URL will change over time.
So I don't know if there's an intention of the browser key to be…
About the browser itself, like, from… Perform, whatever.
But it's about, like, as Jerry was saying, it's about things of the browser, or about the browser that is running the application.
Because if it is things off the browser, then the URL is on the browser, but it will change over time. I don't know, but I…
To me, it's fitting that it's, like, browser.world or something.
I think I wouldn't want to use up that URL…
Because app to me is confusing as a web application.
We, like, usually don't call it an application.
For other things, so… I don't know if there is any other opinions on using browser.
**Maxime Quentin** 11:14 What about location.urheld it for?
**Joaquín Díaz** 11:21 Yeah, that brings a new, like, namespace.
Which will be location.
I… I guess it's fine, I don't know if we… honestly, I don't know if we have to prefix everything with browser or with app, if we're talking all things that we capture as a client-side application, right?
Or can we just say location.url, or… Similar.
**Jared Freeze** 11:46 I think this came up in React Native, too, like, where… They have the idea of…
something that looks like a URL, but it's not… it's not HTTP.
That would be nice to share, right? Like, if… if that was client-side… if it was client-side semantic, you know, convention.
I don't know if that matters, but it wouldn't… it wouldn't be called URL, and it wouldn't be called location either. Or it could be called location, I mean, I guess that's generic, but…
If it's a URL part, I don't know.
It'd be… it'd be nice to share more, because I… I do think, like, yeah, browser.everything is…
Should be really, really specific, like, things that happen in the browser that don't happen anywhere else, you know?
**Ted Young** 12:36 Yeah.
Which is arguably this, though.
Right, like, you could make the case that we're talking about, like, browsers
I mean, I don't know, I feel like I would want… React, you're saying they're just… you're talking about the…
the hashtag partials as their routes, that's the difference. They're just changing the hashtag?
**Jared Freeze** 12:57 No.
**Ted Young** 12:59 It's… it's totally different things. Okay.
**Joaquín Díaz** 13:02 Is React Native, like, a way of describing routes in an application?
But technically, it's not a browser URL, it's just how React Native interprets, like, it knows which view to render, but the user never sees a URL, they see an application, like a mobile application.
So he's like…
it's the same concept, right? You wanna… I guess the question you want to ask… to answer is, where is my user?
And then different clients will have different ways of answering that question. Like, a browser will say, your user is on example.com slash page.
And then, sorry, a mobile application will say, join us this on the product page or product view. And then a React Native application may say.
the user is on this URL, or this component review, I don't know what the user.
It's the same question, right?
**Ted Young** 13:54 It sounds like a client SIG question, because I kind of want to know, like, what else out there in Android and iOS is like this, right? Like, are there lots of frameworks that have, like, some kind of concept like this? Like, an MVC framework is, like, really common, and do people want…
model view controller route thingies everywhere, like, what… like…
**Benoît Zugmeyer** 14:16 That's nice.
**Jared Freeze** 14:22 Yeah, that's a…
That's actually already in the client SIG, or the client, the client side. I looked, it's app.screen.name.
Which is, like, you know, like in Java, it's, like, whatever.whatever.whatever.
It's essentially the same thing, you know, it could be,
yeah, the class name for React, but it could also be the URL.
I could, I could see, I could see either one.
**Joaquín Díaz** 14:47 But, Marie… My concern is that if we use app.screen.n name.
for an Android application, that you get, for example, main view, main activity, whatever.
That doesn't change.
Like, or you have, like, the products view, that doesn't change if you are looking at different products, but they all will change if you're looking at different products, so you cannot use the same thing, because you have, like, different
Cardinality, depending on whether you are on a browser application or a mobile application.
So that is why I don't like that.
app does create a name. I think we need something different.
It's like an instance of a screen, basically.
**Maxime Quentin** 15:32 I think…
**Ted Young** 15:33 Brett, sorry, go ahead. Go ahead.
**Maxime Quentin** 15:35 No, no, no, no, no, I was saying that I also agree that app.screen.name can be, like, you can have several instances of the same navigation, and it will always have the same name, but actually, you can have been to the same page, like, in 20 minutes, difference, so…
Yep.
**Ted Young** 15:58 I feel like the browser is a specific enough thing, and it's a big enough, gigantic domain that it's worth it to have our own stuff that's specific for browser. But I feel like it's a little bit like…
DB versus SQL, right? Like, we have lots of SQL stuff in semantic conventions, because trying to shoehorn all SQL semantics into a generic DB thing, like, doesn't feel good. And I feel like if we try to shoehorn all of the browser stuff into a generic
App location kind of thing.
That wouldn't feel good.
So I kind of wonder if, like, can we just have our own browser stuff, and for something like React Native, could they use the mobile stuff?
And would that feel okay for them?
**Maxime Quentin** 16:46 Could we have… Oh, sorry, sorry.
**Ted Young** 16:49 I was just gonna say, if we could maybe try to do these things separately, and then identify what are… what are important projects that live in some weird brine zone? Maybe it's just React Native is the only thing that's, like…
I'm a native mobile thing, but I try to pretend like I'm a web thing. There might not be that many things that live in that middle ground.
**Maxime Quentin** 17:15 could we introduce an app.web namespace, where we would have, like, URLs that could be both, like, a browser and React Native, or WebViews in mobile?
**Ted Young** 17:34 I think you would just be web. I mean, I would drop the app part of it.
Just for brevity, but…
I don't know.
I wouldn't want to mess up our model just for React Native, I guess.
**Maxime Quentin** 17:49 That's what I'm saying. Oh, I understand. Right. The app is already there, so maybe we couldn't use it, but .
**Ted Young** 17:54 But it's more that, like, with browsers, we have different browsers, right? So it's not like when you say browser semantics, you're talking about a specific implementation. But there's enough details
There.
I kind of worry that if we aren't…
If we have something more generic than just browser, will we be…
**Maxime Quentin** 18:16 Afraid to put browser-specific stuff in there that we actually want.
**Joaquín Díaz** 18:22 Hmm.
**Maxime Quentin** 18:23 Agreed.
**Ted Young** 18:24 I don't know.
I kind of feel like it would be worth it just to try browser, like Jared was suggesting, and just see if that works.
And then bring it… Yeah.
**Joaquín Díaz** 18:36 That makes sense, like…
**Ted Young** 18:39 But yeah, figure out who our weirdos are. We know React Native is one. Are there other ones?
You know, that we need to take a look at when we're modeling this stuff, just to make sure they're not left in the dust.
**Jared Freeze** 18:52 I, yeah, I think the names, too, like, a lot of people will make a distinction. So we talk a lot about, like, marketing sites, or, like, homepages, and think about, like, hardNAV, like, sites that are kind of dominated by hardNAV, or, you know, something like, e-commerce. And then you have, like, a SaaS app, right? Like, everyone says app. They don't say page.
necessarily. Or document, right? And so, I feel like we should make it as intuitive as possible, but, like.
Should we make a distinction between things that are apps and things that are not, you know?
Something to consider, as well.
**Ted Young** 19:31 I think it's more about the mechanics.
It's just the thing I wonder about. That when you're doing hard navigation, are there mechanics to stringing together a session of, like, hard nav changes that are… is, like, is that…
Just a different enough model where you're constantly having to, like, flush things out of the browser and, like.
like, it seems like that's slightly different than a long-running React page, where maybe the URL is changing, but maybe you're also just, like, updating widgets and, like, other things are more appy-like.
**Jared Freeze** 20:05 Yeah, this gets back to what is a session, which is, like, the eternal question. Is it…
the thing on a page, you know? Is it visibility? Is it across hard and app? Maybe we should figure that out first.
**Ted Young** 20:21 Yeah.
I think so.
**Joaquín Díaz** 20:23 for now.
to answer this particular question, I think it makes sense to have, like, browser that URL.4.
**Ted Young** 20:31 Yeah.
**Joaquín Díaz** 20:32 I don't think it will hurt. Like, that's… it's a role in the browser?
That's it.
**Ted Young** 20:40 I guess what I'm thinking is, like, when you've got a string of these hard navigations.
is debugging… is observing that, like, is there a bunch of specific stuff around the mechanics of how that works that's the kind of stuff you want to be digging into? Like, do you end up with gnarly problems?
You know, trying to deal with that stuff enough that we want to just have specific semantic conventions for how hard navigation works, just to make sure
That we can put all the details in there, so that we can debug that… that flow.
**Jared Freeze** 21:15 Yeah, I would…
**Ted Young** 21:17 Mechanically, than an in-page, single-page thing.
**Jared Freeze** 21:20 Yeah, I would say something like browser.navigation.type, which is, like, reload, back, forward.
First, you know, whatever they call that, is pretty important.
Yeah, I would probably put that in the browser namespace, because I don't… that just doesn't exist, right?
I mean, it sort of exists as a concept, but, like, browser.reload is very specific. Browser navigate reload, so…
Yeah, I guess I would… I would say, yeah, let's just start shoving stuff in a browser, call it experimental, and just see how it goes. Yeah.
**Ted Young** 21:53 That's good.
**Maxime Quentin** 21:53 Perfect. Yeah.
So…
I was taking notes, but you were saying, like, first we focus on introducing, like, something like browser.urls.fool, then maybe open, experimental fields, like navigation types, or stuff like that, browser.navigation.type.
**Joaquín Díaz** 22:15 Yeah.
**Jared Freeze** 22:16 Yeah.
**Joaquín Díaz** 22:16 But I think.
**Jared Freeze** 22:17 Yeah.
**Joaquín Díaz** 22:19 Like, I think those are separate concepts, like, the year old, that is the current location.
That is, like, a fact about the page that you are on, and then how you navigate is a different, like, as you were describing it, a mechanism of how you work.
Going through the page, Bob.
the URL is an attribute of the browser, and that's it. There is no much better on that.
**Maxime Quentin** 22:44 In time of implementation, it would be, like, every time you send a signal, you, take the location.href, and you set it to browser.url, .url.fool.
While the navigation will be, like, on navigation trigger, or you would kind of populate this namespace with whatever you need.
But URL will always be there, with always the location href.
continue with us.
**Joaquín Díaz** 23:13 Yeah, the only… Like, we have something similar on our implementation, and the…
Only question that we have… we often have is.
When you create a span, and if…
You add the attribution when you create, or when you end it.
And they may be different URLs, so you may start a span on a page, and then on another page. That's a tough question that we haven't had a good answer yet.
**Maxime Quentin** 23:38 We could have a list.
a list of, of your, of, your full URL, but.
**Joaquín Díaz** 23:44 Yeah.
**Maxime Quentin** 23:46 Okay, understood. I took the note, but Pretty sure…
**Joaquín Díaz** 23:50 And then something else that we do, we have a log processor and a spam processor, so we don't ask each instrumentation to do it.
I don't know if we should have that as part of the browser SDK, so people can just use that, like…
Instead of having… each instrumentation to do this, like, adding the URL.
then we may have the processors instead, and we export them as part of the SDK, and then users can use them if they want.
**Ted Young** 24:22 Martin?
**Martin Kuba** 24:22 I was gonna say, like, if… so, like, maybe this is for a longer discussion, but if… if the URL is shared across all signals, that seems to me very similar to the session…
Concept where, like, we wanna add… we wanna just use entities or resources, attributes for… for all of that, right?
**Joaquín Díaz** 24:41 Yeah, we actually had that discussion earlier this week on the base of the… They…
If a page is an entity, and then once you… every time you change a page, you create a new entity, and then the last entity.
And also, something I didn't know is that, can you have multiple entities at the same time?
And then, if you have multiple, When you create a…
tracer provider, you can use multiple entities to style that tracer provider.
I… I don't remember if I… I've seen the sort of… the…
the PR that you shared earlier, I don't remember if that was part of it.
They're having multiple entities to start up.
**Ted Young** 25:24 So that's…
the last item… so we're a little short on time. I don't think we can actually get into discussing the rest of the stuff.
But, just a quick update, like…
We had a fun… Martin and I had a fun lap around the entity SIG.
Where, you know, we had been making, like, an entity's provider design to kind of solve the problems that you're talking about, Joaquin, and we got feedback from Daniel and other people that it… it didn't work very well, and so we asked for their design, and they gave us back a design that was focused on metrics.
So it turns out there's, like, two problems with entities. The problem that we care about, which is what you were just talking about. We have entities, and we want to make sure that, like, the batches go out with the right resources based on those entities, and then we also maybe want to
Use the fact that entities change over time to… to report on, like, you have a session entity that lasts for this whole thing, and then you have, like…
you know, a page view entity that's, like, getting updated and changing through that session, or something like that. We can model that stuff with entities, and you couldn't really model that with resources in the past.
That seems, like, really valuable for us.
But…
people were really fixated on the metrics API, and they came back and were like, here's a new design for, like, how entities should work based on how you would add entities as labels to a metric.
And it was just, like, 100% not useful for anything we're trying to do.
Basically.
So it was good feedback to know that, like, oh, wow, if you have entities changing, and you want to use them as labels for metrics, that really fucks with our metrics SDK design. Like, the way we designed the metrics SDK, it was not expecting listeners to be in the middle there, being like, some stuff changed under the hood, buddy, and it's like, that would be a complete rewrite of our metrics system to deal with that.
But, we're noticing that, like, We don't give a shit about that problem.
Right? Because we're not shipping metrics, right? Like, we are, like, the metrics, like, API and SDK is, like, the one thing we don't care about. So what we decided was, like, look, let's just build a demo
making this work according to our design, and just stand it up, and then show that to the entity SIG and everybody else. And be like, this is what we need.
Based on the designs we've been pushing.
Because it feels like we've hit a point, at least in that conversation, where just having words in English and specs and stuff, it's like… it's like people are kind of talking past each other.
And I'm noticing some of that here in this SIG, too. It almost… it feels like we've kind of hit a point where we just need a working end-to-end demo of this stuff.
And when we have that, it will be easier to, like, figure out the right choices for…
Basically, everything we talked about today
You know, like, like, so many of these things, I feel like, like, if you play with it and you get the data, you can start to be like, oh, I see why this would or wouldn't work.
And I'm starting to wonder if we just need to have that end-to-end demo before we can…
Like, start finalizing some of the other pieces.
**Jared Freeze** 28:56 I can try to do that. I have a PR out for our SDK for soft navigation that has
like, heuristics for figuring out what changed on the page, which is not necessarily the URL, which I feel like would be a good use case for this, because it's not just URL changes. Like, sometimes, like you said, you're updating just the top half of the page, you know, or transactions, bank transactions, something like that.
I'll try to jam that in, because I do think that's actually a really good place for this, which it… and again, it doesn't necessarily go with URL. It is something else entirely.
So… Cool. Okay, bud.
**Joaquín Díaz** 29:33 Do we also need the, like, the entities?
API or NTT's SDK to be part of this demo? Like, we have to also be done, right?
**Ted Young** 29:45 Yeah, so that's something, Martin, I think you're working on, and I can help you with.
to… to get… like, that's the thing we need to stand up and present first and foremost. We need that piece, no matter what, so we're committed to… to building that, but then it's like, once we have that, it's like, can we also add, like, browser navigation in some of these things? So…
So many of these decisions feel, like, tactical, not…
not, like, strategic design. It's, like, tactically, browsers have certain… it's just, like, it has to work with what this stuff does.
And there's so many weird little details, it probably would be easier to do that by trying to write the code.
That's my take.
Kind of where we're at.
**Martin Kuba** 30:31 So I can… I can share the… what I have done for the entities.
For last week.
And, at least for the entities part, like, that's begin…
Talk about that as a group and see, like, how we wanna… If that…
**Joaquín Díaz** 30:44 How we want to proceed with that, and…
**Martin Kuba** 30:46 But yeah, like, sounds like we need, like, a bigger demo of everything we have.
Yeah.
**Ted Young** 30:54 Cool.
That's all we got time for, but… That's exciting.
Let's, let's start pulling together some demo code and start showing it to each other next week, if we can.
**Jared Freeze** 31:10 Sounds good.
And if you mean that, like, in the browser repo, you can also… like, there's a new…
demo, that if anyone just wants to copy and paste, just start making siblings to just do whatever you feel like, because that'd be really useful. Right now, there's one called All, and the expectation is any instrumentation you make, you just put it in there and see what happens.
So… Cool.
**Ted Young** 31:32 Sweet.
**Martin Kuba** 31:34 Alright.
See ya.
**Jared Freeze** 31:36 See ya.
**Martin Kuba** 31:37 Bye.
**Maxime Quentin** 31:38 No, thank you very much. Bye.
