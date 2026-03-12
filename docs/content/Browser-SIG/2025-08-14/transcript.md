SIG: Browser SIG
Date: 2025-08-14
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/r-KhcswwRNEg5ogL0MgfGMw_MAD6TbMIxcTPSlPHAablklHXXgAkUPxcKKDZi7qq.V90CTUdDgwBejo_1
============================================================

## Zoom Recording Transcript

**Ted Young** 00:57 Hello, hello, hello.
**Joaquín Díaz** 01:05 Pardon.
**Ted Young** 01:07 I… Joaquin, I was able to look over your observability model.
I think it's a great… it's a great start.
**Joaquín Díaz** 01:26 Nice.
Yeah, yeah, I think mostly my intention is to kick off the conversation and… We should… I'll go on.
**Ted Young** 01:36 Yeah.
… Yeah, between that and, like, the test hardness plan, I'm really appreciating all the work you and Embrace are, like, putting into this.
**Joaquín Díaz** 01:51 Yeah, no worries.
**Ted Young** 01:59 Alright.
Well… Feel free to add more things to the agenda. Give people maybe another minute, … To get here… And Joaquin, you can maybe… walk us through….
**Joaquín Díaz** 02:17 Yeah.
**Ted Young** 02:19 ….
**Joaquín Díaz** 02:25 Oh, I'll guys share my screen.
**Ted Young** 02:27 Yeah.
And then… Yeah, Martin, also your doc.
You can look at a way to combine these two things.
**Joaquín Díaz** 02:36 Gifts.
**Ted Young** 02:43 Yeah.
All right. Well, it's a recorded meeting, so people who can't make the meeting can watch the recording.
You wanna kick us off?
**Joaquín Díaz** 02:54 Yeah, so the idea when I wrote this document is just to have, like, an overall overview of what are the things that the browser does and can be, and can be useful for someone to take a look.
mostly, I focus on this for, like, topics, which is the page load, deceptions, network requests, and user interactions.
I didn't focus on what else, like, each new or, like, user of the SDK can then instrument, like, they can do whatever they want with spans and logs, and that's fine.
for mostly this is what we can capture automatically with the SDK, and then have something that can look at it and get information from it.
I wanna say that… You'll… you're going to see a lot of attribute names. These are, like, fillers and samples, these are definitely not final names, thinking, like, proper look into what we can actually get into these, span or events. Sorry, or logs.
I also didn't compare or check with the current semantic omissions, so, some of them might be wrong.
But this was just for… to get the conversation started. So yeah, this… so you can get, like, an idea of what are the things that we can capture for this.
For starting with, I think this is the most important part, the page load.
topic.
… I thought that it would be helpful for us to have some sort of, flowchart or, like, Gantt chart of the things that happen at the browser level when the page loads.
And what are things that are, important to capture, and, like, to have spans that, will tell you, like, mostly, like, the timing of these things, like, how much time it takes to do all the… This is only on the document, so you can take a look, a better look later, but, … pretty much what I'm trying to split is, so we can have something like, a span that is, like, page load, and then within… we'll have a couple of child spans.
Html parsing is the time that it takes for the browser to, you know, total out the HTML and Parse it so it makes sense for the browser, and then start, like, loading stuff based on that.
So you see, like, a log call passed on when it's done.
But, like, since quite a few years now, that doesn't mean that the patient feels all It's probably going to start a lot of other stuff, mainly CSS files and JavaScript files.
So if I have another, span called Document.
Which is how much it takes for the browser to get these things that are blocking. Like, these are mostly things that are blocking the experience for the user. It means that the user will probably see a blank page, or, like, the page loading, or nothing useful.
Until all these assets are loaded.
Some other assets may be triggered to download while these are loading, for example, some analytics tool or images, but since they're not logging, oh, like, that's why I only use, like, the… Time of each of the child, like, logging resources for the document load resource, like, spam time.
And then, after that.
you get, the first Web Vital event, the FCP event, I think it's first Contentful Pain, correct me if I'm wrong.
And this is what the user says since I've been at the browser, but again, it doesn't mean that it's a usable.
Until… like, before this Web Vitals is… like, before Web Vitals went more and less stable.
you may use something like Document. or other events, but now I think web vitals are better to understand when the pages interact, like, usable or ready to be interactive.
For the usurp.
So I thought another, like, the last one would be something that when they're… where you keep getting stuff from other services, or you start doing, like, API requests that you need to show your stuff on the web?
And lastly, you have, the last event is another web vital, which is the LCP, which is Largest Contents for Pain, I think.
Which… It's trying to measure your lashes paint on the page, so you can use that to say.
Right. I'll probably finish loading all the JavaScript, I'll probably finish, like, the other loading another request that I cannot render my page, I am not showing, like, a spin or something, I can show, like, everything so the user can start interacting.
So, this is why… My initial draft idea on how we can, instrument the page load.
I'm… I'm sure.
you'll have, like, other methods or ways that we can do it, and we can discuss it later, but initially, this is how I would do it.
… All this is over here, on the… each span or log that is created, with some, again, sample attributes. These are definitely not final, Like, each one of these requires its own discussion, but at least we can get the idea.
… Then, I have for each topic a section of what metrics what we can get from these sponsor events.
like, for example, like, just measuring the time that it takes for the entire page to span, we can see, like, how much it takes for a user to interact with the page, so I… I press, like, google.com, I press enter, then I have the entire time when I'm waiting for something to happen, then I can start, like, Googling, for example.
Then we can have more specific Metrics, like how much time it takes for the page to download all the, like, resources.
discounts help you understand, like, if my bundle is too big, or my… yeah, pretty much it, like, how can I improve My resources in a way that it takes less time for the user to load the page.
And yeah, you could have other metrics, like how much size you are getting, like, the users getting, how much time is the browser blocked until something happens, like, the time that it takes for these web vitals to… to kick up.
Space. So, some, some examples.
So this… all this will just be there until the page loads, then it's done. Then you have things that will be being captured all the time, for example, exceptions.
You will be just waiting for exceptions to happen using the, the events that the roster has.
And what's an exception happens, you will, like, try the exception, you know?
These are more straightforward, … the only discussion that we've had at Embrace is that It's not common.
So, yeah, it's not, rare that a page has a lot of exceptions. Mostly, you may be using, like, third-party tools, or libraries, or even the same, like, extensions may throw an exception on your page, which may pollute your, like.
exception count, so it's nice to also have, like, something like, for example, a metric that is Tracking how many new exceptions you have over time, because you may have, like, a stable amount of exceptions with your third-party libraries, or whatever you control.
But if you see a spike of new exceptions, then it may mean that something is wrong with the code that you just released, for example.
… Yeah, that's for exceptions, and moving on to network requests. Also, like, it's simpler to understand, it's just all the requests that the roster is making, how much time it takes, the… if… if they are fading, not fading, all the different status calls, but yeah, this is pretty much… And then lastly, two examples of user interactions that we can automatically capture.
For example, user clicks, like, when a user clicks on whatever attitude, sorry, whatever element on the… on the page, we can track that.
And then lastly, we can track, patient navigation.
Which, you know, is different. It depends whether it's a soft navigation, part navigation, like, where you are, like, re-rendering the whole page, or just rendering one part of the page because you have an SPA.
And some sample metrics on that.
… But at least what I have. Hopefully it's enough for, you know, we can start discussing this.
topics individually, and have a deeper conversation around them. But I think for now, yeah, let me know what you think.
**Ted Young** 12:00 I think it's great. So we have a short meeting.
Right?
So to a certain degree, I think I'd like… Us to try to… dig into this through comments and, like, Slack communication, so that we can get to the other topics people want to bring up.
But I think it's amazing. The first thing that comes to my mind, though, is kind of, like, spans versus events.
….
**Joaquín Díaz** 12:32 Yeah.
**Ted Young** 12:32 You've used a lot of spams here, and I like that, personally, because these are things that look to me like operations where you care about the latency and the errors and the hierarchy of operations quite a bit. So, like, tracing tools would be like… generic tracing tools would be very helpful.
to bring to bear in this case. But traditionally, there's been, like, overhead with the tracing component, so people have talked about wanting that to be, like, somewhat optional.
… And to maybe model things with events. I'm not sure where people currently stand in this SIG on that front.
But to me, that's kind of, like, the number one thing I would note about… that your model challenges us with to sort out, is kind of, like, spans versus events when it comes to capturing stuff we're synthesizing out of browser events.
**Joaquín Díaz** 13:29 Yeah.
**Ted Young** 13:30 Yeah, Martin?
Sorry, go ahead.
**Joaquín Díaz** 13:34 I think, like, mostly using spans, because it's actually something that happens in a span of time, but if the metric that we are gathering is how much time it took, and we can do it on, like, a log that says it took 10 seconds or whatever, then it's the same, and if less… if it is less overhead.
to do that, to save a span, I will be okay with that.
I think it's also, like, Yeah.
again, I'm not trying to… already, like, settled down on the specific entities that will produce. I think mostly what I'm… Trying to emphasize this on the things that happen on the browser, and then we can think about how we capture them.
**Ted Young** 14:18 Yeah.
Martin?
**Martin Kuba** 14:20 No, I was gonna say exactly that, that it's, … like, we should make the distinction, maybe, between how the data is collected and how the data is visualized or analyzed in the back end. You know, I think the challenge with these spans that, you know, is that, There's no way to trace this in the browser.
Like, you would just get the data as resource timing, or navigation timing data, and then you would have to, like, create the spans after the fact.
Like, so I'm not even sure how that would work, or, like, if the trace SDK would be helpful in that case, like, running in the client.
So, like, like, as far as data collection, like, you would… you just get… you just, like, take the resource timing data and just, like, send it… send it over, … But, and the other thing that I wanted to… to say about metrics, like, So, like, we've had… We've actually just discussed this in the client instrumentation sig, that's, like, the overlap between mobile and browser, that meets twice, twice a month now.
Last week, we, like, discussed that We wanna… somewhere we want to, like, highlight that we want to discourage from collecting metrics in client applications?
And because of events, right? Like, we would just collect, like, an event from a single… a single client's… client instance, and then the metrics can be… Generated in the backend, but that's… A discussion that's also been happening.
**Joaquín Díaz** 15:53 Yeah, yeah, that would make sense for me, like, yeah.
When I'm talking about all these metrics here, it will be, like, after the fact that the SDK sends it to a collector, and then we can, like, calculate the metrics there, but I wouldn't be capturing, like.
One is… it doesn't make sense to capture one itself metrics, because you'll have, like, multiple users being the same.
**Ted Young** 16:19 Yeah. What I kind of like about this doc is, there… there's… Capturing our model from the perspective of, like, how it's being presented to the users at the end of the day, and then there's capturing our model from the perspective of, like, what tricks and nonsense do we do in the browser to, like, get this data effectively?
to the back end. So, for me, it was helpful to see it kind of laid out more as, like, well, you're caring about the timing information here, and you're trying to generate this set of dashboards using these kinds of metrics. So I think it's, like, really helpful to have a doc that's just kind of, like, from that perspective of, like.
This is what people are trying to do with this data, like, regardless of how we capture it.
**Joaquín Díaz** 17:04 So, maybe that's, like, a distinction.
**Ted Young** 17:08 It's like, we almost have two docks where we want to keep two sections to our docs. One, from the perspective of, like, well, at the end of the day, we want to create a bunch of metrics and dashboards and alerts and things that look like this or that, and then another doc that's like, okay, given that, like, how… how do we actually capture that information?
Because it might be metrics in the end that we want to get, but we're going to capture is, like, events, and then have some, like, collector processor or something.
That can, like, turn that into metrics for you.
… So, so for me, it's helpful to see these as, like, metrics and maybe spans, or something like that. And then, as Martin points out, it's like, in practice, these things might all just be logs.
That we are then processing somewhere along the line into these other things.
… But… I do share his concern around trying to actually make these traces work, given that we get the data Kind of asynchronously.
like, through these events that fire these triggers. I am a little… the thing that seems tricky to me there is, like… actually constructing the parent-child relationship. You kind of have to, like, hold on to all of that information.
And then kind of, like, synthesize that. And that's, like, once you start trying to hold it as, like, a tree that you're gonna… so you can get the trace ID right and stuff when you construct, that's where I suspect that will get tricky in practice.
to do?
When you try to implement that.
But… but I could be wrong.
**Joaquín Díaz** 18:49 Yeah, it makes sense. I mean… If it gets freaky, it may even get opinionated at some point, and we have to, like, start Doing something ourselves on how we can group them, but… Again, it may not be the best for all users, so… They copy metrics that are… Independent, in a way that these are just numbers that you can look at, and we don't have to think about it.
**Ted Young** 19:14 I mean, I do think we want to recreate this diagram, right? Like, but it's a question of, like, are you doing that with generic tracing tools, or are you doing that with a more, like, specialized RUM product that knows how to take all of these specific browser events and kind of construct A flame draft out of it, or whatever.
I don't know. Anyways, I think these are things we should all be thinking about. … And by we, I mean you guys, because I'm gonna be out for the next two weeks. So I'll be thinking about it less, but I'll be coming back on the other side.
Okay, so I want to respect that we've only got 10 minutes left in the meeting, and there's some other topics that people wanted to… to bring up.
… So, let's just, in the interest of time, move on to some of those. So, Jared, intended browser support?
**Jared Freeze** 20:07 Yeah, so I did a little research, trying to make this quick. So baseline Widely Available is, like, an MDN construct of things that have been available for 30 months in major browsers that cover a very, very large swath of the planet.
**Ted Young** 20:22 Right.
**Jared Freeze** 20:23 Most things are evergreen, Safari is always the problem. Sorry if there's any Apple people here, but, … everything that's in ES2022 is widely available, except for static.
class blocks, which becomes widely available next month, so it's actually really nice and convenient. I… am proposing that we commit now to ES2022. So, I know that that's happened on, like, the Node side or the JS side, as far as the code that you write.
But I'm suggesting that we recommend even potentially people bundling at ES 2022.
It's fine, I think we just have a ceiling of, like, that's how our TypeScript configs are set up, and ESLint and all that good stuff, so that, like, it just will warn you, like, hey, you're… you're out of spec, right? Like, you've used something too new, because there's no… you know, there's no, polyfill for, like, temporal API or whatever. I think that's pretty simple. I think it's, you know, a decent, … it's all, like, working really, really well that they picked that. You know, they probably had the same thoughts. Maybe somebody is here from there, but, yeah, that's my vote, is that we just… send people to MDN, and just say, yes, 2022 is what you're looking for. That happens to be widely available, so we don't even necessarily need to say that, but that's kind of the idea.
**Ted Young** 21:48 Did I catch something in there? You're saying it's not just, like, what we should restrict ourselves to, to what we use in our APIs and whatever, but you're saying as far as, like, what we're capable of instrumenting?
We should, like, if people are using newer, brand new.
JavaScript APIs, we may not be able to… like, that library may be out of scope for us to support? Is that what you're saying, or maybe not?
**Jared Freeze** 22:16 … I wasn't saying that, but I think that that's true. You know, I think most things, compile down, right? Like, transpiled down. Not everything, right? You can't down-level absolutely everything, but I guess what I would say is that authoring code for us in, you know, in the repo.
2022, don't move forward. People are willing… are obviously welcome and encouraged to bundle down if they need that for their customers, but I think us saying, like.
that's… that's what we follow internally. As far as what we pull in as packages, yeah, I mean, we should… You know, be aware that it is possible somebody could do something newer.
I don't think it's that common, because, you know, people try to go broad, but….
**Ted Young** 23:02 Yeah.
Well….
**Joaquín Díaz** 23:06 I think it's also worth mentioning that sometimes you… you go to MDM, and you see some, for example, some features from the road, so, like.
performance API.getEntries or whatever, and when it says it's widely available, it means that all these browsers support it.
So I think that's something important to call out, that if we are going to instrument something on the browser, we check that out first, and we see that it's widely available before even working it, because otherwise it may not work for other browsers or older browsers.
So that's the, like, the baseline's going to be two and a half years, I think, of roster support for my year rosters.
**Ted Young** 23:50 Cool.
This seems like something to maybe debate in a, like, a GitHub issue.
Again, pointing out we should figure out where we're gonna write this down.
And then make a PR or an issue or something so people can continue to debate it there. But it makes sense to me.
Dan, I'd like you to jump in on this one.
**Daniel Dyla (Dynatrace)** 24:16 Trent's here also, who's a part of this decision, but we do… I think ES2022 is… What we're currently publishing, in the JS SIG.
… You know, the consequences of it are, like, if you're using something older, you just need to include, like, olifills and such.
It usually is not impossible. It's just… You know, requires some additional work.
… We also publish… like, an ES Next, So, like, we're publishing both side by side.
So if you don't want to use polyfills, and you have a smaller deployment target, and more control or whatever, more greenfield projects, you can use that if you'd like. I don't think it's particularly common for people to do that.
But I think a lot of bundlers do read that, and then bundle to whatever, appropriate level.
… Yeah, so… … ES2022 is already in, like, the baseline widely available, … whatever it's, … you know, I think that's a reasonable target to… to say we… we are targeting baseline widely available as a general policy, and base all of our decisions off of that.
I have to say, I didn't… I wasn't aware that that was even a thing until fairly recently.
But I'm happy to see that it is.
I have a related, topic on the agenda.
The next thing here, there's a PR that adds, fetch support to… The HTTP exporters, which is fine, like, adding fetch support is great, there's some situations that we don't have XHR support, like service workers and such, like that.
But we don't want these things to, like, grow forever, so the question of when do we deprecate and drop XHR … you know.
comes up, and, you know, potentially this baseline widely available policy answers that for us, because Fetch is considered to be widely available, and XHR is considered to be a fallback for that.
Maybe we drop the XHR support, and then for those that need it, they polyfill.
… And… and that's that.
… We talked about this in the JS SIG yesterday, this PR specifically.
… And I told them that I would bring it here today, so I thought it was kind of related to what Jared was already talking about, so good synergy here.
**Ted Young** 27:07 Yeah. I should also note this… things like this, where it's, like, a detail inside of something like an exporter, there's, like, room here if we, like, push on this and then discover we've actually left a chunk of our user base behind. We can just say, oops.
**Daniel Dyla (Dynatrace)** 27:24 Yeah.
**Ted Young** 27:25 and bring it back. So it's not like an API surface-level thing.
**Daniel Dyla (Dynatrace)** 27:30 We would also not do it, you know, we… we would probably… … drop it in a milestone… a major version number, right? We're at SDK 2.0 right now, but as the JS SIG, we have agreed that we're going to rev our major version with some regularity.
I think yearly is kind of what we're targeting, so this would mean that sometime in 2026, early 2026, we drop support for XHR and the HTTP exporters.
And if you need it, you either polyfill, write your own exporter, which is, of course, totally possible.
Or if we get a lot of people complaining, we could even publish, like.
a separate exporter that's like, here's for, like, old browsers, a legacy HTTP XHR exporter that does nothing else.
Or something along those lines.
**Ted Young** 28:26 Yeah.
Yeah, it sounds like there's no reason to not be aggressive there.
**Martin Kuba** 28:33 Yeah, I mean, I would say just as long as we… make that messy documented somewhere, make it clear to users.
Because I think that there are use cases that some people might care about knowing What… where their users are coming from?
But, yeah.
I agree that this is probably fine.
**Ted Young** 28:57 Yeah.
And at any rate, it is undoable and go-aroundable in a variety of ways, so… Yep.
**Daniel Dyla (Dynatrace)** 29:07 I think there are some… I mean, this is probably getting into more detail than we need to in this discussion, but I know that there are some things around XHR, that is handled fundamentally different In Fetch, I believe one of those things is, like, the user agent. Can't be… I think you can override that header in XHR request, but not fetch, if I'm remembering correctly.
… But yeah, there are some things like that, but yeah, we'll….
**Ted Young** 29:42 Yeah.
**Daniel Dyla (Dynatrace)** 29:43 Cross those bridges when we get there.
**Ted Young** 29:45 And we are… we are out of time for this meeting. There was, … a thing about associate browser telemetry, maybe we can move that to Slack. And then the last item, should this meeting be longer? I… I am watching myself fall into the same pattern that we have in the other six of kind of, like, using the meeting to kind of spur me… to, like, work and discuss things, and… and I feel like this is a pattern I would like to see us… break from in OpenTelemetry a little bit more. I would like to see us do more asynchronous work, and feel like we're being productive in Slack, and, like, if this meeting didn't happen, like, progress would still be able to continue.
… I'm gonna go away for 2 weeks, and also not run the meetings, so maybe this thing can kind of, like, self-organize a little more in that.
that direction?
… So that would be my comment on there. I'd like to see us give it a good college try to get things done with just a 30-minute meeting, but still feel like Our velocity is, like, going up instead of going down over the next 2 months.
But if it turns out that's just, like, not how OTEL works, and the only way it works is we, like, sit down and talk to each other, then we can extend the meeting. How about that?
**Jared Freeze** 31:08 I just prefer it. Slack's great, so that's fine.
**Ted Young** 31:11 I prefer it too, but it, like, it stacks up. Sure, absolutely. And it reduces participation, in particular in, like, APAC.
We haven't come up with a solution where we can bring in a lot of APAC participation and still have meetings and live on a spherical planet.
… So, that's kind of the other hope, is if we could make things more productive in Slack and GitHub, then we'll get more people in who can't come to this meeting time.
**Jared Freeze** 31:46 Dell.
Totally fair. Great point.
**Ted Young** 31:48 like that.
I still like the meetings, though. This is helpful to see everybody every week. I'm glad we do this. And when I go into open source projects where no one's meeting with each other, I'm like, how is anyone even keeping track of what's going on here? So, I do appreciate it.
Alright, we're over time. I'll see y'all in a couple weeks.
