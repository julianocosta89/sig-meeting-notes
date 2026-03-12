SIG: Client Instrumentation SIG
Date: 2025-11-25
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 00:18 Jason.
**JP Jason Plumb** 00:21 Ayo.
It's gonna be a slow week, I suppose.
**Martin Kuba** 00:25 Yeah, I'm sure.
I wasn't even sure that this was… this meeting was gonna happen.
**JP Jason Plumb** 00:34 Yeah… Understandable.
I haven't looked at the agenda, I'm assuming it's blank.
**Martin Kuba** 00:42 Yeah, it is bunkie.
**Maciek Grzybowski** 00:44 Hey, hello.
**JP Jason Plumb** 00:46 I…
**Martin Kuba** 01:17 Was there even a meeting two weeks ago?
There's, like, there's nothing…
**JP Jason Plumb** 01:23 2 weeks ago was KubeCon, I think.
**Martin Kuba** 01:25 Oh, you've come.
**JP Jason Plumb** 01:26 Yeah.
**Maciek Grzybowski** 01:28 To what I know, there was no, like, no one in there, because we had a folk from Datadoc joining, but, he was alone.
She didn't record it, so…
**JP Jason Plumb** 01:39 Oh, it was recorded.
Alright, well, I will leave an artifact that I was here, and… I will say that I am in the middle of releasing RC1 for Android.
**Martin Kuba** 02:01 Nice.
Very exciting.
**JP Jason Plumb** 02:06 It is.
I'm doing it while everyone's, like, away. It's, like, kind of… We'll see if it works. So far, so good, but I just expect the build to break at some point, because, like, these version strings are non-standard. Like, they're not what we normally use, and I… there's gonna be some little piece of automation that's gonna be broken, but…
**Martin Kuba** 02:26 Hmm.
**JP Jason Plumb** 02:27 We'll see. We'll see.
**Martin Kuba** 02:37 You put it… you put it on hold, right? Like, you were going to do it, like, a while ago, and…
**JP Jason Plumb** 02:42 Yes, we were planning on doing it in October, and there were some questions about the stability announcements that were made.
We've decided to do it anyway.
We have… we will have our agent be marked stable, like, when we're, you know, we're doing RC1 with the expectation that we'll do… between 0 and 1 or 2 more RCs, depending on how they… how it goes.
And then everything it… everything it depends on, like the core and the instrumentation, they will still be alpha, but then those are targets that we can then immediately begin working towards stability on.
But we expect most people to be using the initializer.
So that API, we want to be stable first.
**Martin Kuba** 03:24 Okay, gotcha.
**Maciek Grzybowski** 03:27 Do you have an idea of which instrumentation, like, we could stabilize first?
**JP Jason Plumb** 03:33 That's a good question, If stability involves the semantic conventions, which it probably does, then maybe the okay HTTP instrumentation, because it's HTTP, that one we could probably… I think that's probably the… that's also complicated, but I think that's one of the first ones we could do.
Yeah, makes sense. So, yes, HTTP spec is full of stable elements, so I think… Right. It's a good target.
Yeah, and then beyond that, I don't think there's much left that's stable, so we'd need… that's gonna be a process.
**Bee Klimt** 04:09 The, unhandled exception one, the exception semantic conventions are pretty stable.
**JP Jason Plumb** 04:16 Do we have unhandled exception instrumentation in the Android?
**Bee Klimt** 04:20 Yeah.
**JP Jason Plumb** 04:21 Okay.
I'm glad you know that.
**Maciek Grzybowski** 04:31 I think what's there is handled exceptions, not unhandled. Unhandled, like, I can imagine those are the, like, native crushes, or…
**JP Jason Plumb** 04:42 I mean, we do have crash instrumentation, but I don't think the semantics are stable.
**Bee Klimt** 04:52 I can… I can look into that, because I… I don't know, I guess I don't know how stable the semantic conventions around exception are, but they've been there for a while, so I assumed they were stable.
**JP Jason Plumb** 05:07 Well, yeah, off the top of my head, I don't know.
**Bee Klimt** 05:12 But yeah, I also agree with your first point of, okay, HTTP is the most obvious one.
**JP Jason Plumb** 05:19 Yeah.
Yeah, we'll do our best now, to try and not have breaking API changes, you know, unless we really think it's gonna… like, we're gonna be careful with it, even though stuff is alpha.
I feel like it's kind of settling in.
We have one core class that in this release also changes from Java to Kotlin, so that was… that was kind of a big change, but I think… It's setting the… it's setting the groundwork for it, you know, us to… to really start to settle down on changes.
Until 2.0 happens.
**Martin Kuba** 06:05 Jason, I don't know, like, much about how you have it structured, but you said there's a… you have the agent and you have a core, so those are two different things?
**JP Jason Plumb** 06:14 Yeah, I can share my screen and show you.
Since we don't have a lot going on, yeah, so in Android… These are all modules, right? So, kind of the top-level module is the Android agent. We expect people in their Gradle to declare a dependency on the bill of materials, on the BOM.
Which, is in here somewhere, this one.
And once you do that, it kind of ties all of the versions of these different components together. We expect most users to be able to… we expect most users to use the agent API, which contains the initializer.
And it kind of looks like this.
So in Kotlin, you know, we… we have this DSL that we're leveraging now for configuration, so you call OpenTelemetry roam initializer initialize.
**Martin Kuba** 07:05 And…
**JP Jason Plumb** 07:07 what you get back, this get or null , what you get back is an instance of OpenTelemetry RUM.
This was newly moved into… A new package.
So the only thing kind of hanging out in here is the OpenTelemetry Rum interface. So we have interface separation now between Core and the agent, but this is kind of where everything happens. I mean.
Sorry, this is the object that users, application developers, would hold onto if they ever need to get the session, if they ever need to get the OpenTelemetry instance, or if they need to send events. That's really the three main things we care about right now.
Yeah. And then the core is where you… we're saying, like, power users or super users For whom the agent is too simple, or is… might be missing some very specific nuanced, esoteric edge case scenarios, which we haven't accounted for, because, I mean, the world is really big, and who knows, like, there's not one size fits all. And that's where we bring in the OpenTelemetry Rum Builder.
So you can use the builder to configure basically everything, and if you want to get really crazy with it, you can use the SDK pre-configured Rum Builder. So build your own OpenTelemetry SDK, and then just plug it into a RUM instance. So this is not stable yet.
Well, it won't be stable even when we release 1.0. It is a separate, it is a separate module, though, so it's… OpenTelemetry Android Core is the artifact that you would depend on.
**Martin Kuba** 08:52 Okay.
**JP Jason Plumb** 08:53 Yeah.
**Martin Kuba** 08:54 So the agent is essentially just, like, a layer of API, there's not much implementation there.
**JP Jason Plumb** 09:00 Yeah, so it does two things. I don't know if we're… so we really do need to boost our… our, docs around this stuff. I don't even think this has a README yet, so it's in the main README, and the thing… The thing that the agent does, Let's see… Yeah, so it doesn't really… I mean, we should do a better job describing what the agent is and what the agent does.
Let's see… So what the agent is… yeah, so this is… this is the thing. This is the main thing that we're providing.
the agent which initializes the SDK and provides auto-instrumentation of apps. So it's those two things. It's like.
Provide instrumentation, and initialize the SDK. That's… that's the goal.
**Bee Klimt** 09:44 And that… that underlying OpenTelemetry Java SDK, that's disabled now, right?
**JP Jason Plumb** 09:49 It is, yeah.
Yep, I think they have… I know.
Thought they had the same… yeah, so… They don't have stability on here, but I can tell you metrics, traces, and I think logs are all stable.
Yeah, the answer is yes.
So does that help a little bit, Martin?
**Martin Kuba** 10:18 It does. I'm just, like, trying to think through if we should do something similar in web.
Because, like, right now, Everything is just… It's complicated to configure things right now, for sure, and everything is built around… Just like the… the… The, like, basic log, span, just the trace…
**JP Jason Plumb** 10:44 Yeah.
**Martin Kuba** 10:44 log providers.
**JP Jason Plumb** 10:46 Yep.
**Martin Kuba** 10:46 And so… But that's kinda how… the JS SDK works, like, it's never been… So yeah, I guess I'm just trying to figure out, like.
If you should follow, like, a similar pattern here, like, provide a simpler… more simpler… API on top of those.
you know, concepts.
**JP Jason Plumb** 11:07 Yeah, so we… we have a set of default instrumentations that we think… like, this is opinionated, like, on purpose. These are the ones that we think most users will want. They're included, they will be bundled, or there will be… there will be a declared dependency that you will get in your project.
If you don't want them to be used, though, you can disable them through… through whatever.
**Martin Kuba** 11:31 Yeah, yeah.
**JP Jason Plumb** 11:32 Yeah, so, like, you know, through this.
**Martin Kuba** 11:36 But I guess, like, were you… were you following, like, doesn't the Java… SDK have a similar pattern? Like, what are you following?
Or was this something that you thought was necessary specifically for Android?
**JP Jason Plumb** 11:52 Yeah, I'm not sure what pattern you're referring to. I mean, I think this is a little bit Android-specific.
**Martin Kuba** 11:56 Okay, okay. Yeah, I thought that there was, like, a Java agent…
**JP Jason Plumb** 12:00 Oh yeah, so there is, and it comes with all of the instrument… well, comes with most of the instrumentations enabled by default, so I guess we are following that… that pattern, is that the agent does provide instrumentations for you.
**Martin Kuba** 12:12 Yeah, yeah.
**JP Jason Plumb** 12:13 You can also bring your own, and you can declare dependencies on any that we don't include, and they will be found at runtime and turned on.
This is very Android-specific, right? So we're… We're setting up the… I mean, I think if you step a few levels back in the API, right, there's the… the tracer provider stuff, but they all have to be configured to the next border, so we… We kind of shorthanded… Ways of creating the log exporter and the trace and the metric exporter.
And if you need more details, you can do that, but, you know, we… you may not… it depends on how detailed you want to configure that.
**Martin Kuba** 13:01 Okay.
Yeah, I kind of feel like… the JavaScript SDKs has… A little bit different patterns.
**JP Jason Plumb** 13:13 I'm sure.
**Martin Kuba** 13:14 Yeah, so… But I do like this approach, yeah.
**JP Jason Plumb** 13:23 Cool.
I'm gonna continue running the build through and hope it works.
**Martin Kuba** 13:28 Okay.
Yeah, thanks for showing that, Jim.
**JP Jason Plumb** 13:33 Yeah, yeah.
**Martin Kuba** 13:39 Is there anything else that you want to talk about today?
**JP Jason Plumb** 13:43 But is Honeycomb using OpenTelemetry Android yet? I think I've already asked you this, like, 3 times. Yes, we've been using it for a while. We've been kind of stuck on an old version, because we were unsure about…
**Bee Klimt** 13:54 The… the breaking changes and keeping up with things, but we're.
**JP Jason Plumb** 13:57 Yeah.
**Bee Klimt** 13:57 Excited about 1.0.
**JP Jason Plumb** 13:59 Cool, awesome.
Thanks for sharing that. I'm sure that I've asked you that.
**Bee Klimt** 14:05 No worries.
**Maciek Grzybowski** 14:12 One topic that I wanted to raise is… Hi, Ken.
it's about moving some semantics towards stable, because a lot of things that I saw, I was playing a lot with Android and ZK, like, very well done, like, I like the idea, optionality of instrumentation and so on.
But after, like, looking at the OTLP data, all the semantics that are used, I noticed that quite a lot of them are, like, still in development.
that's where my question on, like, which instrumentations will follow next, I get the idea that OKHTTP may be exceptions, first good candidates, but there are also other things.
In Datadoc, we, in particular, are looking at the screen semantics, so I think it's part of the app.
authenticity, the screen semantics, so screen name, screen ID, Stuff like that.
So, what's the… what's the take here on moving them… moving them forward, and how we can help?
In getting so.
**JP Jason Plumb** 15:20 Yeah, Martin, you've been, going to the web SIG as well.
I know that there has been some question, because Daniel DM'd me about some questions about alignment. There's, like, some PR, I think, for… Might have been for clicks, but whatever clicks have, like, screen coordinates stuff in them, and there was, like, a question on… like, we have one that's, like, widget coordinates, or widget name, I forget what it is, but, there was some pushback from the web people, they're like, we don't call these things widgets, we call them, you know, divs, or we call them elements, or whatever the, you know, web vernacular.
And I'm like, well, that's specific and detailed to your platform. On Android, we also don't call them widgets. Like, widgets are supposed to be, like, an umbrella term, but whatever. I don't… and then screen, there was always a question of… coordinate systems, and I don't think there's a good consensus yet for that. I think we… I think… The last… from… from my memory, I think we need some kind of, like, enum that is, like, a reference for coordinate… the coordinate system, like, whether they are, like, actual screen glass.
Or if they are window area, if they are displayable window area, if they are widget, or other smaller UI component referenced, I think we tried to map everything over to actual device glass coordinates on Android.
But that won't be one size fits all. Even with an Android, it won't be one size fits all.
Because I think if you have two activities, if you have two apps, like, some Android… you can put apps side by side, and if you do that, I have no idea, I don't think you can calculate your actual… Screen coordinates, I'm sure that breaks.
**Maciek Grzybowski** 17:09 Especially… especially on browser, right? Because, like, websites, it's, like, the screen coordinates will depend on the size of my window, so, like, my picture is another, another thing, required to… To interpret this delta. But, like, I'm looking at this, like, from higher level, like, and you mentioned one thing, like, the discrepancy between, like, what's there in semantic conventions, what's there in Android implementation versus where a browser sync is.
Is standing at, and,
**JP Jason Plumb** 17:38 And there is little pushback on some of the op semantics that are defined, so I'm trying to understand, like, what's the way.
**Maciek Grzybowski** 17:47 What's the path forward to build some consensus?
**JP Jason Plumb** 17:50 Yeah, I wish we had, some… our representative from the GC here, or TC here, to help with this, but I think the idea right now is… The community is looking for someone who will take a topical area, like, let's call it screen coordinates, or… or, Yeah, let's just call it screen coordinates. And Bootstrap, a time-limited special interest group, probably requires, like, writing a one-pager about the intent of it, and gathering people who will meet together to sort of hash that out.
As a… as a time box, like, special interest group.
So, there are… and this is, like, kind of the new… the new format, rather than having one special interest group for… all client semantic conventions, for example, like, kind of what we're sitting in right now. The idea is to have smaller, kind of.
area-based.
Special interest groups with a goal of getting stuff stable in limited time.
So I think, I think to answer your question, it would be, like, to start up a special interest group.
**Maciek Grzybowski** 18:53 Okay, basically, establish, kind of, like, quote-unquote, screen-seq, and do… get the job done in there, and then… okay, got it.
**JP Jason Plumb** 19:02 I think so, yeah.
**Maciek Grzybowski** 19:05 perhaps also pulling, like, people from interested parties in there, so some people from browser seek, some people from Android seek, and maybe from here, right?
**JP Jason Plumb** 19:13 Totally.
**Maciek Grzybowski** 19:15 Oh, okay.
**JP Jason Plumb** 19:15 Yep.
And I think there's examples of that being done. I don't have them on the top of my head, but let's see…
**Martin Kuba** 19:26 I thought there was, like, the HTTP semantic conventions one.
those happening.
**JP Jason Plumb** 19:31 Yeah, there was.
**Martin Kuba** 19:37 So, in browser, we just merged, Experimental instrumentation for, user clicks.
For clicks, and it's, it's essentially just, the event is called… So I can show this.
It's called, like, Browser User Action Click.
And the coordinates… our page.x and page.y.
Like, in browser, we have… they're, like, multiple coordinates based on… Like, if you're looking at just, like, what you can see, or, like, the whole page.
Which includes hidden… Bards.
So I think we settled on, using the page, and, like, we're actually calling it Page, so… Yeah.
So anyway…
**JP Jason Plumb** 20:33 I mean, Paige is blatantly hostile to shared vernacular.
But whatever, I mean… It's progress.
**Martin Kuba** 20:42 Hmm.
**Maciek Grzybowski** 20:46 Is there a ward where… We managed to make this browser user event semantics, like, stable, and on the other hand, in parallel, we managed to make the app.
**JP Jason Plumb** 20:57 click, widget click, or click, like, stable, like, could some…
**Maciek Grzybowski** 21:02 Similar but different semantics coexist together, or that would be no-go at some point.
**JP Jason Plumb** 21:11 I think it's up to us collectively to sort of make that work out, and it's up to the semantic conventions maintainers to… to give their blessing, but… I think it will be very challenging to merge those successfully. I mean, that's kind of what this SIG here, this client group, has been fighting for 2 years, is, like, trying to find that commonality, and that's really… in some cases, I think it just doesn't make sense.
**Martin Kuba** 21:39 Hmm.
**Maciek Grzybowski** 21:39 Gotcha.
**JP Jason Plumb** 21:42 Which is unfortunate, because in some cases, backends are going to have to deal with both.
And we also haven't had a lot of representation from Swift and iOS lately, so hopefully there's not 3, hopefully it's just 2, but… Not.
I wouldn't put money on that.
**Martin Kuba** 22:04 I mean, at the very least, at the very least, like.
Android and Swift should settle on some.
**JP Jason Plumb** 22:10 That's what I mean, yeah, but if there's no representation…
**Martin Kuba** 22:23 I mean, I'm not even clear on, like, how to… how to represent user actions in general, and semantic conventions at this point yet, like, should it be… you know, like, we had a proposal in the past on having, like, a user action event, like a general user action event with types.
**JP Jason Plumb** 22:43 Yeah. So, like, or, like, should every type of…
**Martin Kuba** 22:46 Action have its own event.
With different set of semantic conventions, or… different set of attributes.
**JP Jason Plumb** 22:56 I think that's what a SIG would need to figure out.
**Martin Kuba** 22:58 Boom.
**JP Jason Plumb** 22:59 And then, you know, fortunately, once that work is done, and it has been marked stable, then we can adopt it, and then we don't have to continue bike shedding.
**Martin Kuba** 23:08 Yeah.
**JP Jason Plumb** 23:08 Yeah.
I wonder who the liaison for this, client SIG is these days.
Is it Ted?
**Martin Kuba** 23:21 I don't think it's That's true.
That is for browsers, specifically.
**JP Jason Plumb** 23:31 The GC liaison is Ted.
**Martin Kuba** 23:34 Boom.
**JP Jason Plumb** 23:37 We haven't seen him in a little bit.
**Martin Kuba** 23:39 I don't know, I don't know if he still realizes that, but…
**JP Jason Plumb** 23:46 Yep.
**Martin Kuba** 23:47 It is.
**JP Jason Plumb** 23:49 Yeah.
**Martin Kuba** 23:52 Okay.
**JP Jason Plumb** 24:01 Well, I'm gonna put some more notes about what we talked about into the doc as a record.
**Martin Kuba** 24:06 Thank you.
**JP Jason Plumb** 24:11 So you're… you're interested in, stabilizing clicks? Is that the thing? That's your main focus right now, or that's your idea?
**Maciek Grzybowski** 24:18 Not necessarily clicks, more the screens, screen, screen conventions. In particular, screen name and screen ID, those are the two, interesting pieces.
**JP Jason Plumb** 24:37 Cool.
**Martin Kuba** 24:40 Well, I can imagine we could probably agree on those.
Between… I mean, we could… I think we should probably still, like, think about spinning that group, but… For, like, screen, we can have… screen would make sense in some cases for… for… You know, for browser or desktop applications, right? So…
**JP Jason Plumb** 25:01 Yeah, if the scope is just two things, I think it'll be hard to bootstrap a SIG, but if, you know, if you can sort of, like, figure out what the scope is.
**Maciek Grzybowski** 25:11 There could be something we may… we may want to, like, push for from DataTalk site, and we have our representative in BrowserSig as well, Ben White's joining there. I'm joining here for purpose, on purpose. So, yeah, this could come from our site, if you… if you don't mind.
**Martin Kuba** 25:59 Alright, well… I think we're probably at the end here.
**JP Jason Plumb** 26:06 Yep.
Alright, I'm outta here.
Have a good Thanksgiving, if you do that in the US, and otherwise, see you soon, couple weeks.
Alright.
**Maciek Grzybowski** 26:18 Hey, guys.
**JP Jason Plumb** 26:19 Right.
