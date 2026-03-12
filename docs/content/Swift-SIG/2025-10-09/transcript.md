SIG: Swift SIG
Date: 2025-10-09
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**alexcohen** 00:21 Hey, Bryce.
**Bryce Buchanan** 00:29 I am muted.
I said, hey Alex, and how are you doing?
**alexcohen** 00:34 I'm good, how are you?
**Bryce Buchanan** 00:36 I'm good.
**alexcohen** 00:37 It was fun to watch the, the, the, the thing you guys did the other day.
**Bryce Buchanan** 00:42 Oh, good, yeah, you caught that.
**alexcohen** 00:44 I only got the first 20-30 minutes, because I had to take off, but it was, it was good to watch.
**Bryce Buchanan** 00:49 Oh, yeah, I mean, we… we, really filled up that time, like, we got to the end of it, it was like, oh, wow, we hardly scratched the surface about any of the topics that we wanted to discuss, so we… I think it sounds like we might do another one.
**alexcohen** 01:03 Yeah, good. Well, I mean, that's what happens when you get all these people together trying to… that really like one specific thing, and they just… you can just talk about it forever.
**Bryce Buchanan** 01:13 Oh yeah, for sure. It was a lot of fun.
**alexcohen** 01:17 Yeah, so I was just, dropping in just to say hi. I'm gonna… I have other things to do that I have to do, so I'm just gonna… my video and audio's gonna be off, but I'm gonna listen in to the meeting.
**Bryce Buchanan** 01:27 Cool, sounds good.
Hello, hello!
**nacho** 02:56 Nope.
**Vinod Vydier** 03:06 Good morning, guys.
**Bryce Buchanan** 03:07 Good morning, Vinod.
**Ari Demarco** 03:10 Morning, guys.
**Bryce Buchanan** 03:12 Hey, Ari.
Alright, shall we get started?
**Vinod Vydier** 03:31 Yep.
**Bryce Buchanan** 03:34 Alright, so, let's see. So, topics from last week, document the release behavior for Swift Core and Swift. I added, docs to Swift Core.
And I need to… Add some for… OpenTelemetry Swift, but I think I may just reference the docs added to Swift Core, so… Oh, did they not get merged?
Oh, they're… they're still not merged yet. Oops.
There we go.
I mean, maybe since I have everybody here… Before I merge it, if you could take a look… And see if there's anything you want changed or clarified. But yeah, here they are.
just kind of… breaks down them step… or breaks down the release process step by step, and you know, kind of explains what each step is, at least in a format that made sense to me. So, yeah, please take a look at that. Thank you.
I'll also add that.
to this here. Okay, and I also removed the, the package resolve from… So, of course, So, I'm curious, if, Finad, if you made any progress on this issue?
**Vinod Vydier** 05:06 Not really. I mean, I was… the last week was a blurred, so I didn't… I didn't get to… I… I'm gonna work on it soon, yeah.
**Bryce Buchanan** 05:14 Cool.
**Vinod Vydier** 05:15 So, what's up?
**Bryce Buchanan** 05:16 Yeah, let me know if you need any assistance with that, or have any questions.
**Vinod Vydier** 05:20 Sure, sure.
**Bryce Buchanan** 05:21 we can… we can kind of talk about, what might need to get done there. Let's see, we didn't have any topics from last week. I don't have any topics for this week. Does anybody else have any topics?
**Ari Demarco** 05:36 I… Couldn't add it, but I have one topic to discuss.
That it's basically… my tok… the token I added to do the different releases on embed telemetry Core just was, revoked, because I graded at 30 days.
I can't create a new one, but I think maybe… We should discuss if there's a way to authenticate things, like, in CNCF.
**Bryce Buchanan** 06:06 Yeah, that's a good… that's a good question. I mean, there is… I'm pretty sure there are support Like, worker bots and stuff.
That we could probably use, and I'm… I bet that there's… Some kind of.
**Ari Demarco** 06:27 Yeah, I think that the other day, I don't remember who, but it was from the… Committee that merged something regarding, like, a CNCF bot, or an open telemetry bot.
that does all the GitHub token authentication. I don't know if that's enough.
For this?
Justin, yeah.
I think.
**Bryce Buchanan** 06:54 Yeah, we just need to track down… who owns that stuff in CNCF, and see if they can't help us out with it.
**Ari Demarco** 07:04 I can… I can take that, if you… if you want.
**Bryce Buchanan** 07:07 Yeah, that'd be great. Thanks, Ari.
Alright, cool.
I guess, shall we just, take a look at… The issues we have?
Oh, these are the, PRs.
I feel like we could probably merge some of these ones, maybe not this one. Why does this one say it's okay? That's weird.
Oh, I see, it's not… that's just the version of Swift, not a big deal.
Okay, well, let's look at the issues.
Yes, so… I think that this is… a… Is this a package created by Apple?
Hmm… So…
**Ari Demarco** 08:38 It doesn't seem like Apple graded this.
**Bryce Buchanan** 08:41 Yeah, this package should be evaluated for OTEL spec compatibility. It would be great to understand differences in the implementations versus the official SWIFT library. It would also be useful to understand the use cases where this exporter can be leveraged in providing documentation for users.
So, oops.
**nacho** 09:01 Yeah, let me… About this package, long ago, we, we… they… they started a contact with DC, and they even came… Or, no, they didn't come to any SYNC meeting. People from this team, they just answered in a… in a… GitHub issue about, then it was because we were integrating the Swift metrics and importing them directly into our framework, and With that, they, they start talking about… a bit about this?
This is a private thing they do. They have, they have the own APIs, and what they do is they export to Autel. So they basically have exporters to hotel.
Or, the Swift Traces, or however it's named, the Swift metrics, and all the, all the observability tools that Apple has.
So, what we have done in the past was, for example, with the metrics, importing them as OpenTelemetry metrics, so you could mix that with other things in the OpenTelemetry framework that we have.
For the traces, for example, that they have, they have implemented that in top of the concurrency stuff, and they have implemented on top of the task-specific.
So, you have to manually add In your task, that you want to create a span and things like that, so you have to really Explicitly adding your code.
And very final code, that you see, for example, traces and starting a span.
Once you create that in a task, it's able to title tasks are able to see that task, and so they pass the context using that.
The thing is that… That way, you cannot modify the task.
From outside, so you cannot… zero instrument an app in any way, and you cannot add instrumentation to things that are already Are compiled, or are done.
Because that's not gonna work, because it's… only done on the task side. So, yeah, one of the… Issues are one of the tasks that we had here.
was following the… what we did with Swift Metrics, the possibility to do that with logs, that I think we have something with… Street blocks?
We have an importer, or we had that. At least there was a project that I don't know if we finally merged that, probably not.
It was, like, a summer?
Of code, there was some work on that remains, about using Swift Log, taking those logs as part of… Our… on top of our pandemic is 3 blocks.
And we might do something similar with, with traces, if we can, import that. Because I think we, we are… I mean, they are very limited to, kind of applications, and very limited to the… the… Final developer doing all the stuff, and doing things.
explicitly with the spans.
So they don't implement the API or the SDK, they have something similar.
And they… what they do is they export OTLP.
That's… that's what it does.
**Bryce Buchanan** 12:55 Right, right. Yeah, it kind of… it looks like they have some… some sort of… Yeah, API, but it doesn't look as complete as the… the spec requires…
**nacho** 13:09 Yep.
They just mapped that in order for exporting, I think.
They have that, like, like, extracts to fill in order to export this year.
At least when the last time I checked it, fully.
**Ari Demarco** 13:26 space.
And you said that they support script log, like, the repository, as by default? It's… something like Bing.
An instrumentation thing?
**nacho** 13:42 Sorry, I didn't catch that.
**Ari Demarco** 13:47 I meant, like, they use SwiftLog as a dependency, and they support, basically, creating OTLP logs with Swiss Law.
**nacho** 13:59 Yes, I think so.
**Ari Demarco** 14:02 So it's, it's some sort of instrument item.
**Bryce Buchanan** 14:06 Yeah, yeah.
Interesting.
**nacho** 14:18 I mean, I think we can take ideas, or take… or use some conversor.
Like they do here for the hotel.
In order to be imported in, in the, in the full… in OpenTelemetry Suite, that we really have the full spec, and people have the API, and they can do things, so we can mix things from outside into the, like, the big hub that has all the technology and all the APIs that eats us, I think, so maybe we can… Get ideas from that.
Product in order to import traces and also import, logs into OpenTelemetry Suite, and export later with, with our exporter, and mix with all that.
with other sources of data.
**Bryce Buchanan** 15:12 PM.
Yeah, it's interesting, because it would be… it would be nice if… oops, I keep clicking the wrong one. Yeah, because it seems like their implementation for OTLP export is not very modular, so it's like, if you wanted to use this Package, you would probably set up, you know, you would be, Setting up two separate, like, exporters if you wanted to actually use, like, you know, generic logging or, span generation, so… Yeah, I think I'll also take a look at this package as well, and just kind of write down my thoughts about it. And if anybody else wants to, please do the same. I'm not really sure what the end goal… of this request is, I'll reach out to Alolita and kind of get a little bit more information on what she's looking for, like, what's the kind of purpose.
Yeah, because this sentence doesn't really make sense to me right here. Alright, cool.
**Vinod Vydier** 16:25 Yeah, I mean, even the top of the project, it says it's a client for server-side SWIFT.
**Bryce Buchanan** 16:33 Oh, okay, I missed that part. Interesting.
**Vinod Vydier** 16:43 So if you look at the top of the project, right, if you go to the main site, the GitHub site.
**Bryce Buchanan** 16:51 Oh, right, yeah.
**Vinod Vydier** 16:58 So they probably have a different.
**Bryce Buchanan** 16:59 Oh, backend, yeah.
Wait, where does it… Yeah.
**nacho** 17:12 another OpenTelemetry Swift with the IPI and SDK package? Is that what related repositories… which is that one?
**Vinod Vydier** 17:20 the, oh.
**nacho** 17:21 No, that's our project, I don't know how it's…
**Bryce Buchanan** 17:24 Yeah, it doesn't… it doesn't look like they are actually depending on OpenTelemetry Swift in their project.
**nacho** 17:30 No, no.
**Bryce Buchanan** 17:30 I think they're just… I think they're just referencing our, you know, our… SDK, since it's related.
**Vinod Vydier** 17:39 Okay.
So it's not just for macOS, it's also for iOS and everything? Okay.
**Bryce Buchanan** 17:49 Platforms, support platforms… It's interesting.
**nacho** 17:54 Yep.
Yeah, it's basically that it's the exporter for the tracer, the sweet distributed tracer, that is not OpenTelemetry, and the sweet metrics, and the… and the SwiftLog into Open Telemetry without ALP, so they can… But we also know that.
This is not used by Apple, at least not in all teams. We know we have We saw that they are using, our metrics, for example, in the In some of the… You know, the… with all the… Sorry, all the intelligence thing that they have in the server?
They said something about that, and they were using our… Swift metrics, I don't know if you remember.
**Bryce Buchanan** 18:47 Oh, yeah, vaguely.
**nacho** 18:49 Yep.
So, I mean… Basically, we could take ideas here from… How they are reading from there?
libraries in order to export to OTLP, and use that in our… in our project. I think that will be the… More useful thing, yeah.
**Bryce Buchanan** 19:08 BM.
Interesting. Alright.
It looks like this issue has… we're still waiting for some feedback.
Let's see, haven't heard anything from them for a week, so maybe we'll give it another week and close that issue.
Oh, here we go. This was a new one.
Did we talk about this last week? I can't recall. But.
**nacho** 19:40 Didn't we merge it?
Already? The PR?
**Bryce Buchanan** 19:44 Oh, yeah, look at that.
**nacho** 19:47 I mean, we talked about it, we said that it was great, but they had… they had made some… I mean, they wanted to make those, like, public, but there was no use for them, but I don't know if we really met.
**Bryce Buchanan** 20:02 Yeah, it looks like it's been merged, so… .
**nacho** 20:07 Nope. Oh, yeah.
**Bryce Buchanan** 20:08 Oh.
And… yep, yep, yep. Okay, so go back there.
Closed by number 925… Another crash with test flight. I suspect it has to do with the URL instrumentation, but yeah, again, they haven't gotten back to us in a week, so we'll see if… they come back to us. This is something weird.
they're not being very helpful solving this problem.
we've seen this, like, issue a couple times, a couple people mention it with AF networking, and then all of a sudden, the… User defaults.
Don't work.
But really, they're just asking for a way to disable the AF networking, instrumentation.
And, I think… is… would this be possible to disable by passing, just, like, the blacklist of, delegates to instrument, and just disable that, or is the AF resume a special case?
**nacho** 21:33 Okay, yeah, the only thing… I mean… the only thing I can think of is that maybe Apple has some AF resume method.
that doesn't have anything related with Alamo Fire.
In their, user defaults class.
Because what it basically do is it iterates all the classes in the system and finds a method that says AF resume, right?
**Bryce Buchanan** 22:04 Yeah.
**nacho** 22:04 that's the resume method that Alamo Fire has, or had. Maybe it's too old, and it's not.
**Bryce Buchanan** 22:10 Oops.
**nacho** 22:10 I mean, maybe it's… that worked 4 years ago, and now Aramofire doesn't use that method anymore, and we can remove it.
That would be possible.
But yeah, basically, We check all glasses.
by default. And if Apple has a method with… I mean, if there is a method in any class that has that side network.
we can be trying to swizzle it and prall it, if it's not… .
**Bryce Buchanan** 22:44 But this is… but… it's pretty… It's pretty, like, scoped to just for this specific class.
**nacho** 22:55 It takes the… if… If… if possible, I'm a fire.
And it iterates all the classes.
**Bryce Buchanan** 23:02 Oh, does it?
**nacho** 23:03 Interesting. Yeah, it's not… iterated.
**Bryce Buchanan** 23:06 Oh, it's a… okay, so it just is checking… So if… Oh, well, okay, I see, I see. So it's checking to see if this class exists at all.
And then it iterates all the classes. Okay, yeah. So that's, yeah, that seems a little… that seems a little…
**nacho** 23:26 also steaks.
Yeah, which is… also takes… time. That could be also the other problem with… with very big problems. It could take some time, to find.
So, yeah, either… Yeah, I don't know, if we should… Probably we should check if Alamo Fire still uses that method, in Objective-C, or they have it written now, and it's not needed anymore, which will be great.
**Bryce Buchanan** 24:02 Mmm.
**nacho** 24:11 Okay, maybe it's not needed anymore.
At least not with that name.
**Bryce Buchanan** 24:23 There's a, there's a…
**Ari Demarco** 24:24 When was that code added? Like, that one that checks for AF resume, maybe?
Gives you… gives us a hint.
**nacho** 24:32 2021, maybe? I don't know. It's very old, I mean, the… Yeah, we can blame that, yeah.
Yeah, but we… maybe we… yeah, it was 4 years ago. There are some lines there, but we have reformatted there recently.
**Ari Demarco** 24:54 Yeah, you're right.
**nacho** 24:57 But yeah, could be perfectly 2020-2021.
**Ari Demarco** 25:02 So, the original code was added because… we were having problems whenever AlamoFire was installed, because if… what we can do is basically comment that code, create a sample app with AlamoFire, and check if that still works. If it works, we can just safely remove the code, and that's it.
**nacho** 25:20 Yep.
**Bryce Buchanan** 25:25 Yeah.
**nacho** 25:27 Yeah, also, it looks like it's an objective-C method of… probably they have already rewritten everything.
In a lamb of Fire into Sweet.
So maybe that's really old code that we can't remove.
**Bryce Buchanan** 25:43 Really? That's weird. Am I not in the right folder?
Right, fine.
Okay, well… Oops.
Yeah, I think… I think that, yeah, we should probably just follow up and… and first… Verify whether or not AF networking is… is still… still needs that to be instrumented.
**nacho** 26:15 Or maybe we can just…
**Bryce Buchanan** 26:17 other setting?
**nacho** 26:19 So disabled by default.
X step defeats.
added, like a check? I don't know. I don't know how many people could be using all the stuff.
That's my main concern. People that is targeting old versions of iOS, old versions of S-code, because they are mandatory and they still use some old frameworks.
So maybe we can disable that by default, but leaving a possibility to… to configure?
**Bryce Buchanan** 26:56 Yeah, I'll create a new ticket that lays out what we need to do, to verify that.
whether or not we need Alamo Fire, that instrumentation anymore, if Alamo Fire still works, what version that, was removed in, and if we still need to support instrumentation for those older versions, or if those are all defunct now. So I'll, I'll add that issue.
**Ari Demarco** 27:26 Baby… Natural, you did that code, initially?
**nacho** 27:34 If I implemented that code.
**Ari Demarco** 27:36 Y-yes.
**nacho** 27:37 Yes. Yes.
**Ari Demarco** 27:39 It was for Alamo Fire, or for AF Networking?
Because…
**nacho** 27:44 AF Network… I mean, it was called the Lamb of Fire before. They changed the name to AF Networking.
**Ari Demarco** 27:53 remember the.
**nacho** 27:53 I don't know.
**Ari Demarco** 27:54 the AF networking was in Objective-C, and then they… when they did.
**nacho** 27:59 Oh, okay.
**Ari Demarco** 27:59 It was a lamp of fire, but the creator is the same.
**nacho** 28:02 Okay, yeah, yeah, okay, yeah, that's true.
Yeah, maybe AF… yeah, maybe… no one is using, AF networking, then, anymore, I don't know.
Yeah, I don't, I don't remember, yeah, I… Yeah, you are true about that, about the rename, when they rewrite things should… Maybe no one is using AF networking anymore, and using MFI instead, I don't know.
**Bryce Buchanan** 28:33 Oh yeah, yeah.
Okay, cool. I'll write that up.
**nacho** 28:43 Yeah, but if it's failing with user deposits, it's because the absent method with the same name, that's the only possibility there.
which is, no.
Yeah.
Very expected, but yeah, could happen.
Yeah, in fact, we could put a breakpoint there and see if… Tom Cowey.
It tries.
**Bryce Buchanan** 29:11 To instrument something weird.
**nacho** 29:13 Yes.
Yeah, but it's checking if it's… if the… AF networking manager is there.
to do the tick.
So, probably… If they are checking for that value?
It's because they are using IEF networking, right?
If you go to the.
**Bryce Buchanan** 29:33 Yeah, it'll only do that if AF networking is… Is actually… in the project.
So…
**nacho** 29:46 Yeah, maybe they have still that class here?
But… It shouldn't find that.
**Bryce Buchanan** 29:53 I could find that if it's the same name.
**nacho** 29:56 In Swift also, right?
Like, it generates from an Subject.
**Bryce Buchanan** 30:03 Let me just double check, we can do AF resume… And… This one here… And… we can go up… Come on.
Hmm, interesting.
**Ari Demarco** 30:25 Yeah, that, that one is… if you search in Google or in the repo, it's on AF Networking, that AF URL session manager.
**Bryce Buchanan** 30:35 Okay, so I remember that.
**Ari Demarco** 30:36 Because I used it in the past.
**Bryce Buchanan** 30:38 Okay, so it's not even in this repo, but if somebody's using AF Networking still… Which hasn't been updated in quite a few years.
**Ari Demarco** 31:01 Yeah, it's archived already.
**Bryce Buchanan** 31:04 Yeah, it's archived.
**Ari Demarco** 31:04 They tell you to use… they tell you to use Halam of Fire.
**Bryce Buchanan** 31:07 Yeah, so, yeah, maybe we should just remove that instrumentation altogether, do a little bit testing, or a little bit of testing to see if AA Alamo Fire is, like, actually working with.
**nacho** 31:20 Yeah.
**Bryce Buchanan** 31:21 with our instrumentation or not.
**nacho** 31:24 Yeah, it… So it was failing… for those that were using this library, now they won't have support for networking. Those who have this library, right? But, I mean.
It's just saying, we don't support AF networking anymore. That's…
**Bryce Buchanan** 31:41 Yeah, yeah, yeah.
It, yeah, it seems like this… this library is, you know, it's… it's 5 years out of date. It's archived, it's, you know, the… the owners of it.
Our, my dog's trying to eat a fly.
**nacho** 31:56 Yeah, yeah, definitely they have discarded, yeah.
Yeah, but the only thing is that if they are getting a problem there, it's because they are using it, right? It will follow our code.
**Bryce Buchanan** 32:07 Yeah.
**nacho** 32:08 So, yeah, I…
**Bryce Buchanan** 32:12 Okay.
Alright, well, I'll follow up on that.
Let's get back to our issues.
Update instructions for… Oh yeah, so this needs to get updated.
Looks like…
**nacho** 32:42 They're not interested in adding that.
**Bryce Buchanan** 32:49 I always like the subtle, PRs welcome.
So, does anybody wanna, wanna grab this issue?
It does, it does seem like my, my hypothesis that there would be no necessary, updates to, like, packages with this… with this Swift Core thing was totally wrong, which sucks, but you… so you do need to add Swift Core to your package, or your dependency list, despite, you know, the route Hotel Swift being… like, you're not able to reference it if you don't edit It's kind of like a… SPM thing.
**Vinod Vydier** 33:39 I, I, I can, I can take the, the update of the READMEs and, document.
**Bryce Buchanan** 33:44 Moving. Alright, thank you, Vinod.
Okie dokie.
I really need to just, like, open in a new window, because every time I go back, it just gets me in a different spot. Here we go.
So, I don't really recall… okay, yeah.
So, our instrumentation needs to get updated, at least the documentation for it.
Close that one… here we go.
So, I think that this ought to probably go in… the, sessions readme here… And here… So, I think it's pretty clearly laid out what the issue is in this ticket.
So it's just a matter of kind of describing that problem in, In here somewhere, maybe under Best Practices.
I would say. Because the issue, I think.
without reading through this all, if I recall, is, you can run a URL session with a delegate, or you can run it with a callback, but if you don't use both, then we can't… or if you don't use either, then we can't instrument it, because we need some sort of response, right? Am I…
**nacho** 35:34 Yeah.
the specific thing, I think, is that Or a synchronous network request.
We don't have access to the data.
So the method that we have that allows to filter that data, doesn't work.
We return always need.
**Bryce Buchanan** 35:54 I guess there's a couple of things, too, because also, like.
You need to run the instrumentation before you initialize a URL session, so, like, URL session shared does not work because the system has that initialized before you can run the instrumentation.
So there's… I think there's a couple of things that need to get called out.
**nacho** 36:17 Yep.
**Ari Demarco** 36:18 Yep.
That said, I think the README you linked is the one for sessions, not for URL session instrumentation.
**Bryce Buchanan** 36:25 Oh, you're right, my bad.
I just saw a session and thought, Obviously.
**nacho** 36:31 There it is, URL session.
**Bryce Buchanan** 36:46 There we go, alright.
So that should be a pretty easy addition, just take a couple, or take a couple of, minutes or half an hour to add that in. A little research. Anybody interested?
Going once, going twice.
It's okay.
**nacho** 37:07 Yeah, I can document that then.
**Bryce Buchanan** 37:08 Oh, sure. Thank you. Thank you, Nacho.
Nope, not me, not me.
Okay.
I think that we can close this one, because we haven't gotten any feedback.
**nacho** 38:08 Yep, we asked to… I mean…
**Bryce Buchanan** 38:11 We offer a solution, right? Yeah.
**nacho** 38:13 I mean, maybe, maybe it was solved.
**Bryce Buchanan** 38:24 I don't know.
Receive response doesn't seem to have data…
**nacho** 38:47 Yeah, it is the same issue that.
**Bryce Buchanan** 38:48 Oh, this is that same issue, yeah, okay, so…
**nacho** 38:50 It ends up being the same issue. I mean, he wanted to do something to filter, but yeah, it was not possible because of the other issue.
**Bryce Buchanan** 39:01 Fanad's on the metric filtering, and now we're kind of just down into the… other issues here. Let's see, so in OpenTelemetry Core… Oh, that's the release docs that need to get reviewed. So I am working on this kind of slowly. I think I have a solution for this.
Which is just, you know, kind of rebuilding it through the, through the new APIs.
Basically, my solution is just kind of taking the averages of these buckets and then re-adding them to an actual histogram that results kind of in the same, output. So… I haven't been able to completely… or to complete it yet, but, hopefully it'll… I'll get that, Done in a little bit.
Alright, are there any other… I guess I'll put my name on this, since I'm actually working on it, too. Are there any other topics that anybody would like to discuss?
No?
Alright. Well, I think that we can, call it here, then?
I hope everybody has a good weekend.
**Ariel Demarco** 40:35 See ya.
**Bryce Buchanan** 40:37 Yep, see ya.
**nacho** 40:38 Right?
