SIG: Developer Experience SIG Meeting
Date: 2026-06-24
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 01:02 Hello, hello!
**Johanna Öjeling** 01:04 Hey, Amanda!
**Juliano Costa | Datadog** 01:06 Where are ya?
**Johanna Öjeling** 01:07 I'm good, how are you?
**Juliano Costa | Datadog** 01:10 Git, git.
**Johanna Öjeling** 01:12 Interesting.
**tristan** 01:13 Nope.
**Juliano Costa | Datadog** 01:15 Hello! Long time? I don't see everyone on the same call.
**tristan** 01:21 I know.
**Johanna Öjeling** 01:21 Yeah, it's been a while.
**tristan** 01:25 Yeah, we had someone new last week, but I forget her name. I think she'll be joining again today.
Just from Grafana.
**Johanna Öjeling** 01:34 Oh, was it Fabrizia?
**tristan** 01:36 Yeah, yeah.
**Johanna Öjeling** 01:37 Okay, thanks.
**tristan** 01:39 You're at IKEA now?
**Johanna Öjeling** 01:41 No, I start, next week. So, yeah, I'm on PTO now.
**tristan** 01:46 Oh, cool.
**Juliano Costa | Datadog** 01:50 Nice, nice. I love it here. It's like, LEGO for adults.
**Johanna Öjeling** 01:56 Yeah, exactly.
Yeah, I'm really looking forward to it.
**Juliano Costa | Datadog** 02:04 Starting… I'll create the agenda for today here. Okay. I don't think we have any… I mean, the… Lent.
One sec… My wife just arrived singing.
So, did any of you had a chance to… Take a look at the…
**tristan** 02:41 Verbosity?
**Juliano Costa | Datadog** 02:41 Yeah, the telemetry level idea, I thinky.
**Johanna Öjeling** 02:46 I started to read it, but I still have to go through.
the entire document. If you'd like to, you can… Yeah, present the.
**tristan** 02:56 That's what I was thinking.
**Johanna Öjeling** 02:57 elective.
**Juliano Costa | Datadog** 02:59 Pope.
Yeah, well, I think, well, if we… if we… let me just… yeah, so… One question before, Johanna, do I put yourself as Rafone still, right, on the agenda?
**Johanna Öjeling** 03:15 Yeah, technically I'm still employed today, so yeah, that's fine.
**Juliano Costa | Datadog** 03:19 Okay, so… And Tristan, you are at Serap, right?
**tristan** 03:23 Oh, yep, sir.
**Juliano Costa | Datadog** 03:24 Okay, cool. Okay, so, I think I already, briefly discussed a bit, with you both about this. The… The… the main thing about the… the dock is just, actually.
Structuring the idea and giving more context on why this is actually a problem or an issue.
**tristan** 03:50 Good evening.
**Juliano Costa | Datadog** 03:51 One thing that Ludmila brought up at Auto Unplugged at the beginning of the year was that… Maybe the… maybe the SDKs, Would have a default that is less verbose.
And then, only when people wanted, they would go and opt to a more verbose approach, for a more verbose trace, or a more verbose instrumentation. This would also solve the main problem, because Today, the main problem is… People add instrumentation libraries or, the no-code instrumentation, and they start getting a bunch of spends that not necessarily are useful for them.
And that increases payload, egress, costs on storage, and we are not talking… not even talking about the vendor, part of things. So, like, all of that before all this data reaches the vendor, and then when it reaches the vendor, depending on the vendor, you will pay per, whatever, per amount of data, and you have different pricing things there. And sometimes you're paying for something that you are not using. So, ideally.
Ideally, we have, So, the proposal proposes a couple of things. So, the first thing is setting a default.
Which is kind of what Ludmila proposed at Auto Unplugged, when I presented the Tracerboski idea.
where we… We… the default, we set to server, client, producer, consumer, and then we dropped in… we dropped all internal.
We could… we could have… so, okay, so this is something that… sorry, this is something that, was interesting, actually. So… The boundary value would actually drop all internal expense.
But the default, we would need to kind of change a bit the… this… this pack.
To add, another configuration on the SPAN, so whenever people are creating the instrumentation libraries, they tag these pins as large cooperation or not. I think I… I detailed this… Da-da, a little bit… On the internal details part, the bottom of the document.
So, when I have a SDK integration point with a Python example, when people are creating the spin, so when they are creating the instrumentation for a specific library or whatever.
they add this verbosity to hint, where they say, hey, this is a logical thingy, or a logical piece of code that would make sense to everyone to see, or this is a detailed part of the code that not everyone needs to see. And then.
If the per… if the… if whoever is configuring the… the instrumentation sets… leaves the default, then they would get the internal spends, but just the logical internal spends.
And… If they wanted… they… if they set the trace verbosity to detailed, then they get this extra internal detail dispense.
So this is the… this is the thing. Maybe we could discuss a bit and have a better idea, even, like, I don't know.
a different type of spends? I don't know, like… To be less confusing?
And then the non that would suppress everything.
accept.
So, this is another thing that differs a bit from the current implementation. When we set the SDK instrument… the SDK config to none, nothing is exported.
But with the hotel trace verbosity, if we set that… so, of course, this is all hypothetical, but the idea is, if you set to none, you wouldn't get any expense from any instrumentation library, but you would still get the expense from manual instrumentation.
So you kind of suppress everything that is automatic, and you keep the manual. So you do not suppress the SDK, so, like, the spins are still being created.
**tristan** 09:03 How would you know which is which?
**Juliano Costa | Datadog** 09:16 This is a good question, that I'm gonna ask myself.
**tristan** 09:21 Because that's a nice idea, but… yeah.
I can't…
**Juliano Costa | Datadog** 09:28 the instrumentation… I guess the instrumentation libraries, they do… They do call the same span method creations, right?
**tristan** 09:39 But yeah.
**Juliano Costa | Datadog** 09:40 So they are… they're the same. Hmm.
**tristan** 09:42 I think they would have to pretty much be… told and… no… No, because there's nothing there that would… But they're just calling the API, so they wouldn't be able to…
**Juliano Costa | Datadog** 09:58 Yeah, maybe what we could do, because, for instance, in Java, if you… I think, actually, most of the languages that have automatic instrumentation, you can suppress instrumentation by passing, hey, exclude this library.
So then, when we set to known, basically, that would exclude all the libraries that we have.
And then we keep growing this list whenever a new framework comes up. Not ideal, but, like, yeah.
**tristan** 10:29 Yeah.
**Juliano Costa | Datadog** 10:30 A mess, actually.
But that's a good point, thank you. I haven't thought about that.
**tristan** 10:35 That would be a nice… but that, yeah, it'd be a nice thing to solve, because… That would be good to know.
And be able to toggle. I mean, we just hit this, because we're… We don't have tracing at work yet, and so they're… we're starting to introduce it, and we're trying out different… we're doing… we're luckily on, like… what's it called? Well, trials with companies like Datadog and Grafana and stuff, and so it's… we're not paying for it, but the… like, one of the first apps that is, instrumented and sending stuff just has these massive traces that are, like, I think, 15 minutes, and I think it's because they get cut off by the back end that says, like.
We have a hard limit at 15, and that we just drop it, we just pretend the rest isn't there.
And because it's auto industry, like, just included some instrumentation libraries, and it's, like, Google PubSub and a Node.js app, and it's just… thousands and thousands and thousands and thousands of spans. It's like, something like this would be nice to have as the default, and then you… start adding stuff. I told them to just remove that, because it's not… There's no point in it.
**Juliano Costa | Datadog** 11:58 Yeah, and… but in that case, do you still have manual instrumentation as well, or…
**tristan** 12:04 Yep.
**Juliano Costa | Datadog** 12:05 Okay.
Yeah, so that would be cool, because then we could… take advantage of… because the idea here is taking advantage of Delta instrumentation, because it.
configures everything with the SDK, and then you just pass the environment variables. It's way easier than configuring the SDK manually.
But then… You kind of easily suppress all the instrumentations.
Yeah, I added a note here that it's not easy Both because the instrumentation libraries are calling the exact same spend creation methods, so… Maybe we.
**tristan** 12:45 I definitely like the boundary.
the boundary idea for, verbosity. That's cool.
**Johanna Öjeling** 12:52 Yeah, I really like the boundary level. Is that already existed, or I haven't seen it?
**Juliano Costa | Datadog** 13:01 If that, that's, if that exists.
**Johanna Öjeling** 13:05 I said, no, no, yeah.
**tristan** 13:07 It's just based off of the kind… the kind of the span?
So we know, like, if it's a boundary span, but we don't…
**Johanna Öjeling** 13:15 Excuse me.
**tristan** 13:16 So…
**Johanna Öjeling** 13:18 I think that would be, yeah, a really useful level to have.
**tristan** 13:23 I mean, technically, you could do it in a sampler already, because we pass kind to the sampler, but… It's… yeah, it's a pain to… I have to do a sampler for everything.
**Juliano Costa | Datadog** 13:36 Yeah, one thing that, we could maybe try to… synthesize and have, like, a V1 of this would be to have just the detailed that would have internal spins. The default, that would be actually the boundary one, just with server, client, producer, consumer, and drop all internal.
And then we tried to come up with a solution for the known.
If actually… I mean, I think it makes sense based on your use case, Tristan.
But I don't know if, it's, like… If it's not a lot of workarounds to actually make it work, then it would just be a mess.
In the codebase.
Because I assume, like, these two… two types of internal expense, it is an extra level of complexity that.
**tristan** 14:39 just…
**Juliano Costa | Datadog** 14:40 delay this from landing.
**tristan** 14:42 Good.
I see the only… issue… well, not the only, but the, like, the issue I see people bringing up We'll be saying, you can already do this with samplers on kind. Like, we could have a boundary sampler, And so… Arguing why… Something… something, and how it interacts with it. I mean, I guess it doesn't necessarily have to interact with it. Well, I guess, I mean, like, do you want to be able to, in the sampler, say, if it's kind, internal, still keep it?
And not have the verbosity drop it.
There's gonna be an interaction there, like, does it come first or second to the sampler, and how it interacts with samplers, and… I mean, personally, I think it'd be nice to just be able to toggle it and not have to do a… Cause you, you usually want multiple… you'll want, boop.
probability sampler.
And you'll want this, so then you gotta… chain them, it'd be nice to just be able to set a verbosity level instead of chaining samplers, so… I like the verbosity, but I know that's gonna be a… Sticking point, probably.
**Juliano Costa | Datadog** 16:12 What I'm actually advocating here is that the name of our SIG, like, the developer experience.
I think everything that we are proposing here is doable already, so you can, of course, go and manually instrument your code, and then it will only get the expense that you want.
problem solved. The problem is that we want a good developer experience, so we want to provide whoever is using OTEL To actually easily configure it, and then take the advantage of the project without Struggling with a lot of… things that come afterwards, and then people may even say, yeah, but you can, you can do the SDK, you can configure the sampler on the SDK level, that's… that's a point.
That is valid and, doable.
Another point that people may bring is that you can filter out on the collector, and in this one, I have, I have a good argument here, because then you are consuming CPU and memory to generate all those internal expands.
generating traffic to egress all those spends, and then consuming CPU and memory on the collector to filter out all those spends. So, like, you are… consuming.
Twice. So, in here, I have a win. In the SDK, simpler, I don't know if I have a win. Maybe… people may think that it's overhead… unnecessary overhead for the project maintainers that users can deal with. I don't know.
**tristan** 18:05 Oh, yeah, I agree.
**Juliano Costa | Datadog** 18:15 One… one problem that I see, and I think this we should, try to bring bring up more into conversations, is that we are usually talking with folks that are implementing and developing the hotel.
So, like, the folks that are actually doing your So, we are knowledgeable about hotel. We know how every inner part of hotel, every configuration, and okay, yeah, we may miss one or other parts, but, like, we know how the things work. Sometimes, the user actually don't.
sometimes they do not even have access to the code. They are doing auto-instrumentation via operator, so they need to configure everything via YAML, and, like, they do not touch the code, the, the agent goes and, do the instrumentation automatically for them, so they do not actually know what is going on. So, if there is a way to easily configure.
That will make their life easier, and that's what I'm trying to… To advocate here.
Tristan, I think you are, I think you are the one that has… from the three of us, I believe that you are the one that has more experience with, actually sending all our data to backends. I think Johanna is in the back end itself, right, Johanna?
**Johanna Öjeling** 19:57 Yeah, that's true.
**Juliano Costa | Datadog** 19:58 I'm mostly in… like, I actually don't care what lends to the backend, because I usually don't pay for them.
So, do you feel that the… do you feel internal spends are actually useful? Is there a scenario where internal spends are a good thing? Have you used them?
**tristan** 20:26 I… they can be, but I've, yeah, always advocated to start with boundary, and… Only when you know… Like, you're really clear on what you need internally?
Start adding it, and often that you… like, not to use it like profiling, essentially.
Not to… hurt.
Every function, create a span.
There's definitely… Youth there?
At times, but… Yeah, it… Yeah, you gotta really know what you need before you start adding them, and a lot of times people just add them, and so having that, you know, toggle is… really useful.
Yeah, people just use it, add it, and then don't look at them anyway, too. So it's not even just the… that they're… Clogging it up or anything. There's just traces, even, that people never look at.
Full of spans. Internal spans.
**Johanna Öjeling** 21:33 Yeah, I remember before I joined Grafana, I was at a company, where I, I set up, observability, and, With the auto-instrumentation, we got all the internal spans as well, but as far as I can remember, we never used any of that, and we, like, filtered them in the collector to not, yeah, include them. So I think… like.
an organization getting started with observability, the boundary would be… would make the most sense to get started with. I think that would capture the important, transactions.
Yeah.
And if… if it was me, like, rather than… if I wanted to expand on that and get more details, then maybe I still wouldn't include all the internal spans, but I would, like, create manual instrumentation for those internal operations that I cared about.
**Juliano Costa | Datadog** 22:38 The thing here is that, like, imagine you are in, you know… trouble… you have an incident, so you are in the middle of the chaos. You wouldn't go to the code and instrument and redeploy the code at that moment. At that moment, you would just flip the switch and say, hey, give me a verbosity level, detailed, whatever. And then you'll start getting the internal response, and then see if you get something out of there. Not sure, actually, because usually.
from my perspective, from my usage, I see a lot of internal spends as… As things that are useful for the folks that are developing the framework itself.
And not the users of the framework.
So, this is one thing that I… that I see. But let's say that you want internal expense in, during an incident, you could just, enable that and then get… or that would… That could… oh, that's, something nicer. You could even create manual spends.
And set them, as internal.
So then you just enable them when you have an incident or something.
**Johanna Öjeling** 24:03 That, dead.
**Juliano Costa | Datadog** 24:04 There is also something that could be cool.
**Johanna Öjeling** 24:10 Yeah.
**Juliano Costa | Datadog** 24:14 Okay, yeah, so… go ahead, Tristan.
**tristan** 24:18 This would also be nice just as a checkbox in the, like, I mean, you still have to pay, so it's not as… not as great, but when you're looking at traces in a GUI, if there's a checkbox for, like, you want detailed or not, because… Yeah, there's a lot of… there can be useful information, usually not, but even, like.
because we even have span, conventions for, like, the different stages of a TCP connection. Like, there's very… there's certain circumstances where, yeah, that's useful, you want to know why it's, like, hanging, but the… you don't want to see it every time you open a trace. Just click Detailed, and then it will… Show you the rest, but… Yeah, you have to pay for it still, so that's not as useful.
**Juliano Costa | Datadog** 25:08 Yeah, and… when we… When we say pay, we are not just talking about the storage.
Right.
**tristan** 25:20 It's been with me.
**Juliano Costa | Datadog** 25:22 Yeah, yeah, you're paying with CPU, memory, egress.
**tristan** 25:25 Annie.
**Juliano Costa | Datadog** 25:25 And, like, then you need to ingest, so you have ingress as well, and then the storage.
**tristan** 25:34 Yeah, these giant spans were… Bringing down my collectors, even.
**Juliano Costa | Datadog** 25:40 I… I… I had a… I have a project. I enable… I have a project in Python, and I enabled the rejects instrumentation. I got, two case pens in, you know, one request. Then I removed… I removed the instrumentation on the… on the next, test. I was like, no, that's not for me.
**tristan** 26:04 Oh, man.
**Juliano Costa | Datadog** 26:06 Ugh, Jesus.
I don't know how the instrumentation actually works, but yeah, I don't know what happened, like, it is a… 6 suspense trace.
And I got to… 2K, bridge existence, and I was like, oh, okay, yeah.
So, from… from… From what I hear here, I think… We should try to move on with, The boundary that should… do you all agree that the boundary should be the default?
So, we would… we would have, like, the default, that is boundary, and then detailed, that would include internal.
And should we… Should we… try to… Also bring up the idea of known, that would only have the manual… Or should we start with the easier one, and then move on to a more complex, approach here?
Because I think, technically speaking, it's difficult to implement, because all of them are calling the same.
**tristan** 27:32 Could mention it in case anybody has an idea, but…
**Juliano Costa | Datadog** 27:37 Okay.
So, I'll drop this, mid, though… this middle… Double internal thingy.
Okay.
**Johanna Öjeling** 28:04 What do you, see as the next steps for this, Juliana?
**Juliano Costa | Datadog** 28:11 Well, I will revisit the doc, update the whole description to remove the dimensions of this, to internal thingy, and then ask you again, both for a review, and when you… you both say, yeah, let's go for it, then I'll open an old tab, OTAP, and see And just wait for being bashed, and then I'll call you, you both for help.
**Johanna Öjeling** 28:43 Of course, yeah, I'll review it a bit more thoroughly, but who, like, who do you think will be the… things that need to be convinced. I guess, like, all SDK6 have an interest in this, and then specification…
**Juliano Costa | Datadog** 29:02 Yeah, I think everyone will, and I know that, Austin and Ted, I know that they have strong opinions against that.
**tristan** 29:10 Hmm.
**Juliano Costa | Datadog** 29:11 Because, they made pretty clear on, Hotel Unplugged when I brought up the idea. I know that Jurassi supports the idea, and I know Lyudmila knows… Understands the pain.
So, Ludimila is TC, Jurassi is GC, so, yeah, then we just need to, kind of, Well, I think if we structure it nicely in the way it is, like, make a clear statement of the problem, and then we just need to convince GC that it's a good proposal, and I think… What is the process, Tristan? Do we need support from TC, and then that goes to ISPAC, or do we need approval from ISPAC itself?
How does that work? I never… Raise double tap, actually.
**tristan** 30:05 Yeah, I mean… I don't remember, cause, yeah, I think… I'd have to look at the required approvals, but yeah, I mean, it has to go to spec afterwards, so… Not sure who exactly has to approve it, because it's not spec, it must be TC.
**Juliano Costa | Datadog** 30:34 Okay, well, anyways, I'll race, I'll see who is bashing me, and then we discuss from there.
Cool.
I think that… that the main, the main… the main point is raising awareness of the problem that I think everyone is aware of, but, like, putting it… putting there and, proposing it.
For instance, there is even, in the collector, we… we also have metrics, level, where we say that we want detailed or not.
**tristan** 31:08 Hmm.
**Juliano Costa | Datadog** 31:09 So, the concept already exists.
**tristan** 31:11 Right.
**Juliano Costa | Datadog** 31:12 But, it's not just on spec. We don't have a metrics verbosity on spec.
Also.
So this should, should exist for maybe all, signals?
**tristan** 31:37 True.
**Juliano Costa | Datadog** 31:39 Okay, so then I have that.
**Johanna Öjeling** 31:43 Thank you. Yeah, really nice work on this so far.
**tristan** 31:46 Yep.
**Juliano Costa | Datadog** 31:47 Thank you.
And I know that, Johanna, you worked on the documentation template, right?
**Johanna Öjeling** 31:58 Yes, exactly. But yeah, I haven't revisited that since, I started my video, two weeks ago, so yeah, no updates.
**Juliano Costa | Datadog** 32:12 Okay, no, no worries.
I think one thing.
**Johanna Öjeling** 32:23 But yeah, essentially the, I put one proposal there, and it's essentially that it should work the same way as it does for the spec pages today, with the same, like, pulling the, Through the Git submodules. But then I'll think through if there are other, approaches as well.
One can take two.
Keep the documentation in sync.
**Juliano Costa | Datadog** 32:53 Yeah, I shared here on the, on the… on the chat, because I think Tristan wasn't on the call.
**Johanna Öjeling** 33:00 Tracy.
**Juliano Costa | Datadog** 33:00 Have you seen this page before?
**tristan** 33:03 See, you pointed out.
**Juliano Costa | Datadog** 33:04 The configuration types reference.
**tristan** 33:07 Oh, no.
**Johanna Öjeling** 33:10 Yeah, this is really cool.
**tristan** 33:11 Oh, what?
**Juliano Costa | Datadog** 33:14 So, I came across that, when I was… doing something? I don't remember what I was doing. I think I was, looking for the declarative configuration, things that I… like the… I was looking for the values that I can use on the declarative configuration, and then I came across this page, and then I brought up in the C, because I think, basically, this is… kind of, initial… approach for the idea that we are pitching here, right? We have something that is… fed directly from the other GitHub, so then we reduce the maintainer's burden to keep two pages up to date.
**tristan** 34:07 Nice.
Yeah.
Interesting.
**Juliano Costa | Datadog** 34:24 Oh, if you take a look at the OTLP gRPC metric exporter.
That's a really good one, because it even has an example.
Like, yeah, this is the type of doc that I… that I wish I had all over the place. Like, you have…
**tristan** 34:46 Oh, no, yeah.
**Juliano Costa | Datadog** 34:48 Like, every… you have all the… Other configurations?
**Johanna Öjeling** 34:53 Mmm.
**Juliano Costa | Datadog** 34:55 And then you have… An example, right below him.
Right below it, so that's pretty cool.
What is, kitchen sink?
I have no idea, but it's there.
**tristan** 35:19 That's just the name of a… there's a configuration example that includes every option.
**Juliano Costa | Datadog** 35:29 But it… It's called Kitchen Sink?
**tristan** 35:35 Yeah.
**Johanna Öjeling** 35:36 Where do you see the kitchen sink?
**Juliano Costa | Datadog** 35:38 On the example, we have.
**Johanna Öjeling** 35:41 Oh, okay, yeah.
Amanda.
**Juliano Costa | Datadog** 35:44 And if you go to the OTLPHCP exporter, you have even a tab with Logs Kitchen Sync and Traces Kitchen Sync.
**Johanna Öjeling** 35:52 -
**Juliano Costa | Datadog** 35:54 Okay.
Yep.
I think in the vector, the…
**tristan** 36:02 The… I mean, you know the saying, everything but the kitchen sink?
Where is that at?
American thing.
**Juliano Costa | Datadog** 36:12 I think it's an American theme.
Oh, oh, what is the… what is the same?
**tristan** 36:20 Everything but the kitchen sink means…
**Juliano Costa | Datadog** 36:23 Yeah, right.
**tristan** 36:23 Almost every conceivable option, and so this is the kitchen sink, so it's every option.
**Juliano Costa | Datadog** 36:36 Almost everything imaginable is included in a situation, whether it is necessary or not.
Thanks, Google AI.
Okay, today I learned.
So that's where it comes from.
**tristan** 36:54 I didn't, yeah, I didn't realize… it's gonna be confusing to me.
**Juliano Costa | Datadog** 37:09 I know that in the vector, the collector from like, data. Like, it's not the collector from Datadoc, but, like, the REST collector project, I think the components, they have… yeah, they have… Sources, that is the receiver, transforms that are the processors, and syncs that are the exporters.
So… Yeah, not confusing at all. Thank you.
Cool. Do we have any… anything else to… to discuss?
**tristan** 38:11 That's neat.
**Johanna Öjeling** 38:12 For my slide?
**tristan** 38:13 I'll read up on these.
Documents again.
**Juliano Costa | Datadog** 38:17 Okay, well… I will update, and whenever I do, I ping you… ping you all on the… on chat.
**Johanna Öjeling** 38:30 Sounds good. Thank you.
**Juliano Costa | Datadog** 38:32 Thanks, everyone.
**tristan** 38:33 Okay, thanks.
**Johanna Öjeling** 38:34 Thank you. Bye.
**tristan** 38:35 Okay.
**Johanna Öjeling** 38:35 Bye!
