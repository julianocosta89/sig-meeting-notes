SIG: Community Demo App SIG
Date: 2026-01-28
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/vD1DiZ-53QKubaj7AmoHTRGzQaNULSgp3VnmRREzNt6lxucDzvT9R70qYoC0MPdo.Hfz1E2LycCAIvnaX
============================================================

## Zoom Recording Transcript

**Jonathan Munz** 01:58 Blue.
**Cyrille Le Clerc** 02:00 Hello?
Oof.
Are people joining? I am adding items that I would like to discuss today.
**Jonathan Munz** 03:37 I'm not sure, I haven't attended in a while, actually, so I was just gonna…
**Cyrille Le Clerc** 03:42 Okay.
**Jonathan Munz** 03:42 fit in and see if anything came up, but, yeah, I didn't have any… Items for the agenda myself.
Juliano usually… Right. Like, he hasn't been here a couple weeks?
**Cyrille Le Clerc** 04:08 I am DMing with him, at the moment, he's in the… in New York, he told me yesterday.
**Jonathan Munz** 04:15 Okay.
**Cyrille Le Clerc** 04:22 Are you coming to Hotel Unplugged next week?
**Jonathan Munz** 04:26 No, I'm not.
**Cyrille Le Clerc** 04:36 I guess you're working more on mobile observability.
Vienna.
back-end observability.
Working at Embrace.
**Jonathan Munz** 04:45 Yeah, web and mobile, mostly.
And then, yeah, just trying to kinda… Checking every now and then on the demo application.
But, yeah, haven't, haven't done much on the backend for OTEL in a while.
**Cyrille Le Clerc** 05:04 Okay… I have not followed much, evolution of the, So Juliano will not, Will not join.
**Jonathan Munz** 05:20 Okay, okay.
**Cyrille Le Clerc** 05:22 Yeah. How is, mobile… OpenTemmetry instrumentation progressing at the moment?
**Jonathan Munz** 05:33 Yeah, I mean, I think… I think the big ones I'm aware of that Embrace was involved in was, Pushing for, Kotlin… contributing a Kotlin SDK for OpenTelemetry and creating a SIG specifically for Kotlin that's separate from… the Android Java, Discussions.
And then a fair bit on web, as it pertains to browser, because the JavaScript libraries for OTEL, they've had browser support, but it tends to be more focused on the Node, use case. So, it's more on the code side, like, making things work.
more stable in those environments.
I'm not too aware of anything at the moment on the, semantic conventions side. I know we had a couple things we were trying to push forward.
around… concepts for, client-side-specific crashes and sessions and things like that. I'm less aware of.
Any progress in, kind of, that area?
**Cyrille Le Clerc** 06:46 Okay, and so you said a Kotlin SDK, does it mean that we would… today, we have a… We have an Android SDK, or it's just a Java Upstream SDK that is being used?
**Jonathan Munz** 06:58 There is an Android SDK, it is written in Java and built on top of the Java SDK, as far as I'm aware. This is a new contribution, totally separate codebase for a Kotlin SDK.
I don't believe it shares any code.
But I might be wrong about that. But, yeah, that's also… and there is a potential use case. I know that's similar to Swift, where you can actually use Kotlin server-side as well as client-side. But yeah, this was a new, code contribution, and, I believe the SIG… I have the link here. I don't think the SIG has started meeting yet, but I saw a pull request to the community repo, to… start launching… Oh yeah, here it is. To start launching ads. Okay.
**Cyrille Le Clerc** 07:50 On the fact that it's in Kotlin, if it's written in Kotlin, it can still instrument some stuff written in Java.
**Jonathan Munz** 07:58 Yes, so, yeah, you could use this… Yeah, I'm not sure what the long-term plans are of how this would relate to the existing Android SDK, because yes, you could use it in an Android application in place of.
**Cyrille Le Clerc** 08:12 It would be a kind of new generation of Android instrumentation agent.
**Jonathan Munz** 08:17 I think so, yeah.
**Cyrille Le Clerc** 08:18 I believe it can pull… but it can… it should be able to pull in.
**Jonathan Munz** 08:21 like, if there's standalone instrumentations, like, written in Java, they would be able to use that from the Conlet SDK. Okay.
It would work in the same ecosystem.
**Cyrille Le Clerc** 08:33 on the, so maybe, yeah, it would be the next gen. I was wondering if the first generation of, what we did in Java Android, was more like we took the server-side Java SDK, and we said, okay, let's deploy it on a mobile phone, on Etsy, if it works.
Right. On, maybe not the best.
story.
**Jonathan Munz** 09:00 I think, yeah, and actually I found that, that, that, PR has a link to that. This, this gives a better… Like, summary, like, hey, why was this, why was this donated? But yeah, I think it's… it's largely because that is the… that is where the Android ecosystem is moving, is Kotlin being sort of the standard, standard language, and then developing it with the mobile use case.
in mind from the beginning, I think, was an opportunity to, I mean, we noticed this with some of the JavaScript SDKs, like, it is difficult to… Have one codebase that satisfies both.
Even though it's the same language, both client-side use case and the server-side use case, so I think a lot of… I think a lot of that could have been possible, but maybe just ends up with a codebase that's, like, too different, for those two different use cases, even though it's the same language. So, I think just reading through this, that seemed like part of the motivation was to, Have sort of a mobile-first implementation, for this…
**Cyrille Le Clerc** 10:08 Yeah, I wouldn't be surprised if the cultures are so different, in fact, the problems are so different.
**Jonathan Munz** 10:14 Yeah, yeah.
**Cyrille Le Clerc** 10:15 And that you… you… Quickly, you have to rewrite from scratch.
You have to make them completely diverge.
Yeah. Maybe not on day one, because on day one, you don't have enough headspace to do both simultaneously, but very soon, as soon as possible, you have to diverge completely.
**Jonathan Munz** 10:31 Yeah, So yeah, so I'd be curious, that's a good question, once that starts meeting, like, what sort of the long-term plan is for… the existing Android SDK, but yeah, I could see code being shared, or eventually maybe, it becomes sort of the Java SDK and the Kotlin SDK and that sort of server-side and client-side, but maybe there is still a room for the… existing Android SDK in that plan, I'm not… I'm not sure.
**Cyrille Le Clerc** 11:00 Are there vendors productizing solutions on top of the existing Java Android SDK? Are you aware of this, or not?
**Jonathan Munz** 11:08 Well, Embrace does that, like, Embrace, pulls in dependencies.
**Cyrille Le Clerc** 11:13 Okay. But you donated the new version, this Kotling, so you wouldn't be uncomfortable if we… if the hotel community decided to promote this Kotlin donation as a new recommended way?
**Jonathan Munz** 11:25 Right, because, yeah, I think, I think for our, That's the idea with our code as well, you know, will… we'll be trying to share as much as we can with the Kotlin SDK. It's possible the Kotlin SDK, Yeah, I don't know, let's see.
I'd have to check. It's, it's, yeah, it binds OpenTelemetry Java. I'm curious if it calls anything… Yeah, I wonder if it shares any code, from OpenTelemetry Android. I guess it doesn't.
Yeah, who prefers to use it? But yeah, so that's the idea, like, we, like, Embrace would… Try and make… our SDKs kind of use as much of the… recommended community SDK as possible, and then build our.
**Cyrille Le Clerc** 12:10 Yeah. Kind of net new stuff on top of that.
on an… the JavaScript or the browser instrumentation?
From what I understood, a version 2 of the OpenTeametry JS SDK that is intended to also do browser instrumentation. Version 2 was cut something like… A few quarters ago.
Yeah, I think that was last year, they did a version 2.
And we have vendors like Honeycomb sell a product on top of it.
So I guess it's… not easy to say sorry, but now there is a version 3 that is completely different. Right.
Is there this kind of challenge?
**Jonathan Munz** 12:56 Yeah, the… so there's browser support before version 2, I forget, it was, it was, a breaking change for some reasons, but the API stayed stable, like, there wasn't a breaking change on the API. I forget why exactly the 2.0 was needed, But, but yeah, I think there was just some… kind of, unavoidable braking changes that, that, that contributed to that.
Yeah, it depends, like, so the Embrace web SDK is built on top of that as well. If there is a major version on the hotel dependency, it doesn't necessarily mean our vendored solution would need, A braking change, because it's possible that whatever that braking change was is something we can transparently deal with.
**Cyrille Le Clerc** 13:46 Okay.
**Jonathan Munz** 13:47 in our SDK, and doesn't actually affect our vendored customer interface? Like, that's happened before, because we're… not necessarily just re-exporting the internal APIs, where, hey, here's our API, and it works by hitting this, this, and this. If there's a breaking change in that, it's possible it's transparent.
So, so yeah, it really depends. But, yeah, we have a similar pro… so there's a different approach with the JavaScript case, which is… The long-term plan looks like having having a large part of the codebase support Node, And browser environments.
**Cyrille Le Clerc** 14:22 Okay.
**Jonathan Munz** 14:22 Whereas now we have the browser SIG, the idea is to pull out just… instrumentations and specific things that only make sense in the browser, so that can live in a… in a… in a clear spot. And then there… I… presume long-term, just because there's so much code in there that makes sense in both environments, that there would still be a core that runs in both Node and browser, but anything that's very browser-specific, or very node-specific.
Starts to split off a little bit more, so it's easier to see, like, okay, this is… the interface and what's available in browsers, and this is the interface of what's available in Node, because it is a very different…
**Cyrille Le Clerc** 15:04 Kind of instrumentation you're probably going to want to do in those two different environments.
And you said that the embrace… browser SDK is built on top of the Hotel.js SDK 2.x.
**Jonathan Munz** 15:18 Yes.
**Cyrille Le Clerc** 15:19 Oh, thank you, that's interesting.
**Jonathan Munz** 15:22 Yeah, I can send you the link, too. But yeah, that's the idea, too. We… there is a… hotel browser repo and SIG as well.
They're still in the process of… spinning up and… they haven't published a package from there yet, but that would be the idea, that the Embrace SDK would start, depending on packages from… That's… .
**Cyrille Le Clerc** 15:44 Okay, OpenTelemetry Browser is… yeah, I was not aware of this.
**Jonathan Munz** 15:47 Yeah, so…
**Cyrille Le Clerc** 15:48 Technically, it's JavaScript, but yeah, the fact that it's JavaScript is less important than the fact that it's… Intended for browser instrumentation.
**Jonathan Munz** 15:56 Exactly, yes. So that, that gives a little more flexibility, because, there's just… there's a lot of surface area for the JavaScript SIG as a whole, having to deal with Node and… And browsers, so this is an opportunity to have a place that can focus entirely on the browser issues.
And yeah, and maybe move some code over and have that be, specific, Specific to, to browser environments.
**Cyrille Le Clerc** 16:26 Okay, I'm sorry for my ignorance, but… Server-side JavaScript now is synonym to Node.js. There is no other way than Node.js, no popular other way than Node.js to run server-side JavaScript.
**Jonathan Munz** 16:38 That's a really good question. I would… I would treat them as synonymous, That's a great question. I'm not… I can't… I'm not 100% sure people aren't doing something else, but yes, that's my… My interpretation is, you know, if you're… that's the runtime environment you're using if you're writing JavaScript in, in a service item.
**Cyrille Le Clerc** 17:00 Okay, thank you very much. Only, in the demo, how do you… Because today, we don't demo browser instrumentation, In the hotel demo.
**Jonathan Munz** 17:13 We do. Yeah, the… it's a… it's a Next.js application. It has both the server-side and the client side. So part of that instrumentation is instrumenting the server-side calls to that web application. Yeah. But another part is instrumenting the, the client-side interactions.
**Cyrille Le Clerc** 17:34 But we… do we have dashboards for this?
**Jonathan Munz** 17:38 It would be the same, the traces go to the same, let me try and find it. The traces go to the same… Like, Grafana…
**Cyrille Le Clerc** 17:47 Okay. I have to… I should have started my, demo, but, shame on me.
**Jonathan Munz** 17:54 Yeah, let me, Let me see…
**Cyrille Le Clerc** 18:00 Yeah, I've never looked at the browser instrumentation demo in.
**Jonathan Munz** 18:06 Encihotel Demo.
Yeah, so eventually, I think, when that… when some of that code in the browser repo is, published and ready, using it in the demo probably is a next step. At the moment, Yeah, it uses the, yeah, so here…
**Cyrille Le Clerc** 18:29 OpenDimetry JSOM.
**Jonathan Munz** 18:31 This is the front-end tracer, so, Yeah, this is specifically instrumenting… I think mainly what you're getting is the network requests, so the fetch calls that are coming from the browser are instrumented, Here.
I think, the re… oh, there's a resource detector, so the browser resource detector is there, too. So, the instrumentation should include, like, Chrome, Safari, whatever, user agent.
**Cyrille Le Clerc** 19:00 Okay.
**Jonathan Munz** 19:00 made this fetch request, it took this long, there would be a span for that from the… From the web application.
**Cyrille Le Clerc** 19:08 Okay, and do you know if the load generator that we use makes sense of it?
**Jonathan Munz** 19:13 I don't think it does. I think you'd only… you'd have to… once you spun the demo up, you'd have to manually…
**Cyrille Le Clerc** 19:20 Generate traffic, okay.
**Jonathan Munz** 19:21 your browser and, like, click around and refresh, and then you would see it. I… it's possible.
I've never actually looked at the load generator. I guess it would be a little bit more complicated, because you'd actually have to have a… What's it called? .
**Cyrille Le Clerc** 19:36 browser emulator.
**Jonathan Munz** 19:38 but yeah, you'd have to actually do a…
**Cyrille Le Clerc** 19:41 Which wouldn't be that difficult, I mean, we… the Embrace repo have…
**Jonathan Munz** 19:46 Unit testing integration.
**Cyrille Le Clerc** 19:47 You already used to do this, it's your job too.
**Jonathan Munz** 19:51 Yeah, basically you would spin it up, and you would have a script that tells the load generator to go to… you know, whatever.com to see the, browser, and then click on a couple buttons and whatever, but I don't believe it's currently doing that, Load generator… Dockerfile… Oh. Oh.
Okay.
They're installing Playwright, so yeah, actually, I think…
**Cyrille Le Clerc** 20:22 I, yeah, play right, yeah.
**Jonathan Munz** 20:24 Playwright browsers, Chromium, so yeah.
**Cyrille Le Clerc** 20:28 Okay.
**Jonathan Munz** 20:29 Yeah, it must work with it, then. Yeah, I've never, I've never tried running that.
**Cyrille Le Clerc** 20:33 And so it would materialize in, in traces. If we look at traces, we should be able to…
**Jonathan Munz** 20:42 Trying to think if there'd be any logs, but definitely traces, because the network… Requests are being instrumented, so… Each… each client-side network request should be… a span, and then ideally, those spans would sort of propagate to… Because I see they're… they're instantiating the W3C… Trace Propagator.
So, the headers that those requests make should include… the trace ID from the client side. So, in theory, if you're looking in Grafana, the parent of the trace…
**Cyrille Le Clerc** 21:14 Can I share my screen? I think I have it.
Maybe you wouldn't.
So here I have a trace that comes from load generator, so it's locust.
So that's what we want.
And then I have a GET request.
**Jonathan Munz** 21:44 Okay, yep.
Yeah, and if you look at the resource attributes, there should be a… browser…
**Cyrille Le Clerc** 21:52 But the GET request is on the client side. This is Python, I think this is then frontend proxy… In the span attributes, I should see the browser, yes.
**Jonathan Munz** 22:03 But the front-end proxy… So the… the front-end code is split between the Next.js server-side code and the client-side code, so the front-end proxy, actually, would be server-side.
**Cyrille Le Clerc** 22:16 Yeah.
Oh, and I think it's… Does not capture the browser… or user agent.
**Jonathan Munz** 22:25 Right, but that's still… that's still server-side code, because that's… that's the endpoint defined on the… on the front-end.
**Cyrille Le Clerc** 22:32 I think this is… This is, server or client side?
Shimonin.
**Jonathan Munz** 22:44 I haven't seen any client… nothing has looked client-side yet.
**Cyrille Le Clerc** 22:49 This is not client, I think this is load generator is client-side.
**Jonathan Munz** 22:55 Would you agree?
True?
Oh, because that's the Playworks. Yeah, but then I'm surprised that it's not… If you actually, Right, that's coming from…
**Cyrille Le Clerc** 23:16 This is a load generator, so that looks like what we want.
It's a low generator, locust… this is Locust on this, I guess Lokust is doing Python stuff.
**Jonathan Munz** 23:31 Yeah.
Yeah, so, huh, I don't know. Yeah, I don't see an originating… Like, browser… Click, or, on anything. So, yeah, maybe it's not doing that. I'm not… I'm curious what it's using Playwright for, then, if it's not doing that.
**Cyrille Le Clerc** 23:46 Or maybe job is not finished.
**Jonathan Munz** 23:49 Maybe, yeah. If you go deeper, actually… oh, sorry.
**Cyrille Le Clerc** 23:52 I'm sorry, yeah.
**Jonathan Munz** 23:53 I thought one level deeper after the front-end proxy, I was curious if that…
**Cyrille Le Clerc** 23:58 Yeah, let me find the share button, again, share here… You said one level deeper than…
**Jonathan Munz** 24:11 Yeah, so if you open up front-end proxy… Oh.
**Cyrille Le Clerc** 24:17 Boom.
**Jonathan Munz** 24:18 Oh, never mind. I thought I had seen something else, previously, but, No, that's fine. Yeah, so, so yeah, it might not be originating from a browser then, Yeah. That's what it's doing, yeah. Let's see… people.json, locustfile.py…
**Cyrille Le Clerc** 24:42 the user.
**Jonathan Munz** 24:46 Yeah, it seems like it's doing stuff, so yeah, I don't know. We'd have to, I guess, dig into where those would show up. Like, there's stuff in that playwright script where it's like… go to the binoculars page, click Add to Cart, wait… so it is doing the interactions directly in a browser, but I'm just not seeing the, the spans.
**Cyrille Le Clerc** 25:07 Yeah, I guess if we cannot find it.
**Jonathan Munz** 25:10 Yeah.
**Cyrille Le Clerc** 25:10 It will be hard for community members to receive.
**Jonathan Munz** 25:15 Yeah, yeah, so some things, yeah, some things…
**Cyrille Le Clerc** 25:18 Here, it's called.
**Jonathan Munz** 25:20 Yeah, so that's the first, yeah, interesting.
**Cyrille Le Clerc** 25:22 Okay, we, maybe it's, Something that could be improved in the demo.
**Jonathan Munz** 25:28 Yeah, totally.
**Cyrille Le Clerc** 25:32 Yeah, it's not my skill set. I work at making Graphana, Prometus, Kubernetes deployment look good.
**Jonathan Munz** 25:40 Got it.
**Cyrille Le Clerc** 25:41 It keeps me busy already.
**Jonathan Munz** 25:43 Yeah, yeah. Yeah, no, it's good to know that this is something I think, like I said, when this feels like a good… Next step for the browser sig, you know, when they have things ready to… Release and deploy and show, like, making sure that… It's clear how you would see this stuff, From the demo application, if it's not already, so, yeah.
**Cyrille Le Clerc** 26:07 Yeah. Yeah, I tried to… I started to contribute to the hotel demo, last spring, I think, on a… I try to ensure that we showcase hotel best practices.
Production-grade hotel best practices, and so, On… I've used it internally at Grafana Labs.
To showcase challenges to implement stuff.
Okay. Because people… to bring an evidence of a challenge.
**Jonathan Munz** 26:39 I tell people here, you can use the hotel demo, the challenge we are working on is reproducible here.
**Cyrille Le Clerc** 26:46 Play with it, you're completely self-sufficient to to work on it. On it, in some cases, it has been successful on people who are just on board, on their playground, on, And so I would imagine that we could do something similar for, browser implementation, is to… to say, well, let's see on this demo if it looks good on, If there are gaps, it's likely that they will be a painful experience for practitioners.
**Jonathan Munz** 27:15 Yeah. Yeah, and I like the fact that even if it's not… maybe not used, the way we need it to, the fact that Playwright's already sort of part of the toolchain in that repo, that will give us some… stuff to play with to kind of demonstrate different use cases, too. I think that's what's useful.
Okay… Hmph.
Yeah, I didn't have agenda, and I probably can't help with the ones I saw you… Added for today, so I might need to wait till… Until folks are back.
I guess, oh, that conference is next week, okay. So, yeah, maybe after that conference.
**Cyrille Le Clerc** 28:00 Okay.
Thank you.
Jonathan, yeah, thank you. Have a great week. Bye.
**Jonathan Munz** 28:07 Bye.
