SIG: Semantic Convention SIG
Date: 2025-08-11
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:30 Hey, folks.
I think, … we're going to be without Ludmila and Josh.
Today… And… looks like we… let's see, oh yes, I see we've got… Agenda for me.
I will share….
**Christophe Kamphaus** 01:59 I wanted to discuss the info semantic conventions, but if Miller and Josh are not here, then I'll do it next time.
**Trask Stalnaker** 02:08 Yeah, yeah, we may need to… Postpone some topics.
Cool, well, we may as well get started.
And do what we can. James, what's needed to… make progress… OS types…
I would say probably this, we would want to…
get the system semantic, convention sig…
to weigh in here, plus it looks like Yao has… let's see, Yao's not on… okay.
Let's see, triaged… Okay, so I guess there's two things, James. One is…
to confirm from Yao, you know, that he's unblocking it?
And then probably… we would move to awaiting code owner approval, so… the system, semantic convention.
Books to weigh in on it.
And you could ping if they're not…
responsive here, you could… I think they have a Slack.
**James Thompson** 05:02 I've already pinged them on Slack and got no response.
**Trask Stalnaker** 05:06 Okay. Following last week's, I pinged them on Slack and got no response.
Okay, are you able to, attend their meeting?
Let's see if they're still a meeting.
**James Thompson** 05:20 They're not easy, because this is in the middle of the night for me.
**Trask Stalnaker** 05:24 Yeah, yeah.
Do we have anyone from System Submit Conventions here?
All right, well, why don't you start with, … oh.
Yo. Oh, y'all's here. Hey, y'all.
Okay, so….
**Joao G. (Dynatrace)** 05:53 Hello.
**Trask Stalnaker** 05:55 Hey, so do you… on this PR, I don't know if you've caught up on the latest,
It's still… blocked.
by you….
**Joao G. (Dynatrace)** 06:13 No, I have not caught up with the latest. I will take a look.
**Trask Stalnaker** 06:17 Okay.
Cool.
So yeah, maybe, James, once Yao, either, you know, once you get through Yao's, comments, then go ahead and ping the, system SEMCOM folks again.
And see if we can get them to weigh in.
For… this one… okay.
Yeah, oh, more OS, so more…
System SEMCOM folks, yeah, so we'll need the, System SEMCOM folks to weigh in.
Yeah.
Yeah, it kind of… during the summer, it's… it can…
It can be hard to get people's attention on some things, but we will… …
want them. Like, Braden, has been involved in the system semantic conventions, and he often attends the… this meeting, so…
… We could get his attention at some point, probably.
… Difficulty following database migration guidance, hence proposal to use new requirement levels.
When deprecated.
**James Thompson** 07:48 So, the scenario is… for the .NET contribute, right?
there's a Elasticsearch integration, right? Which documents Elasticsearch.
I was asked to follow the database migration, but…
And I ran into difficulty knowing what should I be implementing when Elasticsearch itself is not stable.
Instrumentation, right, because the definition's not stable, but the base database one is stable.
Right, the package is not stable, Where do I go?
Alright, so what I was thinking was, currently, we have the required recommended opt-in, Right?
what I was thinking is, if you deprecate an attribute and you obsolete it, then the plan is to remove it, and I've added explanation around how to move it, remove it, when you're allowed to, when you can't, and that.
So I'm just trying to… Because currently, having those vaguest sentences there, Doesn't really provide enough guidance.
When you look at the database page, for example.
**Trask Stalnaker** 09:00 Okay, yeah, let's look at the database page. So, give me an example here.
**James Thompson** 09:05 Right, so in the DB system, Right? So, db.system became db.system.name.
**Trask Stalnaker** 09:14 Right.
**James Thompson** 09:15 Right, so that's probably the most contentious one.
How do we do that?
Right? When Elasticsearch is not stable.
But the general documentation for database says I need the database flag to opt into the new stable attributes.
But Elasticsearch is not stable.
**MG Marylia Gutierrez** 09:42 Yeah. Well, one thing that I can point out is that we didn't mark all databases stable, not because they're, like, not in a good shape, it's just because during our process of stabilization of the convention, we didn't have people to kind of create, like, the proof of concept, and all
databases. So, you can still follow the semantic conventions, as would be stable, and then when you are doing… you realize, like, something specific doesn't work for Elastic, that is where you can bring
here, and we'll make the adjustments, but I think you can just follow, like, what is here, and use the opt-in. At least this is what we are doing, like, on some other SDKs. For example, I did this for the JavaScript, where we just…
have the opt-in, that would be, like, for example, the DB system. It would be, like, by default, only send the DB system for now. I have the opt-in to send just the new one on both, and then we wait for a… I think it says, like, one or two releases or something like that. Then we can remove the default value of sending the old one.
**James Thompson** 10:51 Yeah, but in my case, I'm… I've got an existing one using db.system, I want to move it to db.system.name, but when you read the description there, it says it can only emit stable conventions.
**MG Marylia Gutierrez** 11:05 So, you have the three options. So, the opt-in, if you send the database, it is only the
stable. If you send database dupe, it's sending the old and the new, and if you don't set up the… this one, it's sending only the old one.
**James Thompson** 11:23 Yep, but for Elastic, if I… say I want to do Elasticsearch.
**MG Marylia Gutierrez** 11:27 Right.
**James Thompson** 11:28 Database will not send anything. It can't send anything.
Because the db.systemName value used is not stable.
Right, so the first one wouldn't work at all.
because you….
**Trask Stalnaker** 11:41 Which one… sorry, can… let's just be really specific, because I'm not quite following…
So, the first one here, you… Can't….
**James Thompson** 11:54 Oh, I see what you're saying.
Yeah. Based on the way it's written now, if Elasticsearch was to be used, and I was to set database, I would not get a single thing emitted.
Because the db.systemNameValue is not stable.
**Trask Stalnaker** 12:16 I see. Yeah, I mean, that's a good, potentially qualification here. The… the general idea here was that,
we want… There to be, …
just… we want to gather up all the changes to the Elasticsearch instrumentation. We don't… we only want to break users once.
**James Thompson** 12:46 Yep.
**Trask Stalnaker** 12:46 … And so, given that Elastic… is not stable.
… We kind of have… I mean…
According to this kind of strictly letter of the law here, you're supposed to wait for elastic to become stable, and then
And then you can emit that by default.
Prior to it being, … in the…
In practice, though, what we have done is, kind of what Marilia described, we did also in Java.
Where we have, essentially.
Included this option, and if you enable this option, then we opt you into the
stable, or closest to stable, like, the latest, I guess, semantic conventions.
If that makes sense.
**James Thompson** 13:52 Yeah.
**MG Marylia Gutierrez** 13:53 Ghost.
**James Thompson** 13:53 Yeah, and that's similar to what I was thinking, but…
Yeah, this message that's shown on the page Right.
Leads to a lot of confusion, and it's, like, for example, it clearly calls out spam name there.
If you change a span name, how can you emit both?
**Trask Stalnaker** 14:15 Yeah, I think we clarified…
That in one… in an issue somewhere, but looks like it didn't make it into this.
**James Thompson** 14:26 And that's in… like, I've seen the same messages in, like, messaging, Alright, it's a common message.
**Trask Stalnaker** 14:34 Yeah, there was an issue, somebody asked that, previously, and we did discuss it, and I think we decided that…
The… stable, takes precedence in that case, like, where there's conflicting Where it's conflicting.
But that… that would be a good… I mean, so I would suggest inst… like, maybe the simplest solution, way to solve your concerns would be to…
Update this message, or add some more, like, clarifications?
Pure.
**James Thompson** 15:16 My hesitation to adding messages is these messages are appearing in a number of pages.
We're now needing to maintain and keep them all in sync across the board.
Right? And they quickly get out of date.
And all that, right? So what I was thinking was having the requirement level… so, for example, db.system is deprecated, so if you have a look at the PR I've introduced.
Alright.
Alright.
And just go to the database attribute requirement levels under general.
Alright? I've talked about, okay, this attribute is in a migrate state, and what that means.
Right?
So I've taken that same description of what was in that paragraph, and said, this attribute is now in a migrate requirement level. You shouldn't be migrating to the replacement, right? Here are the conditions of when you are to switch, and stuff like that.
So I've just tried to make it more informative.
Alright, so that way, when you're looking at these definitions, you can see, okay, this attribute is deprecated, and I should be migrating it.
And then if you look at the requirement level, what does migrate mean? Okay, I'm using a stable instrumentation, this is what I should be doing.
like, I've tried to keep that same concept, I've focused on just the attributes to start with.
Right.
Alright, so I've even talked about having that attribute in there.
Alright, that environment variable.
**Trask Stalnaker** 17:05 Okay, and so then in… let's see how that plays out… And….
**James Thompson** 17:18 Let's see, so… so I… the model doesn't need to be touched, it's purely markdown changes.
**Trask Stalnaker** 17:28 Purely markdown changes….
**James Thompson** 17:31 Yep, that's… Because currently….
**Trask Stalnaker** 17:33 See, where we have removed things, they are coming back with… a message….
**James Thompson** 17:41 And then if you look at the requirement level, it's migrate or remove.
Rather than saying recommended.
**Trask Stalnaker** 17:49 migrate….
**James Thompson** 17:51 Yep.
**Trask Stalnaker** 17:52 Or remove,
**James Thompson** 17:54 Right? And that way, for me, it's nice and clear.
Right, because that's the other thing, is if I'm looking at an old infiltration, what was actually previously documented
Right?
Because… yeah. But this way, you have, okay, db.systems being… needs to be migrated, and what it means to migrate it for that attribute.
**Trask Stalnaker** 18:23 Yeah, no, I mean, at…
Makes sense to me. Let's see, migrate… So… …
I mean, it… It's kind of nice to have this be, like, the… the latest… for people…
To reference, not necessarily be, like, Having, kind of, legacy… Stuff in it.
… But… If this is… if the migration page is causing problems.
Then that could make sense.
I think we'll need, you know, we'll need more… Kind of… Feedback and opinions.
**MG Marylia Gutierrez** 19:20 Yeah, it could even be, because I'm thinking, like, this dish, like, how long are you gonna keep that line?
like, what is the timeline to remove deadline for, like, migrate or things like that, remove? If it is, like, a different table for, like.
no longer stable things, I don't know. That would be, like, the migration, or old versions, things like that. That would be an easier place for people to check. But, yeah, my concern with
having on the same one. It is how long we're gonna keep old names there.
**James Thompson** 19:57 Yeah, like, we can… we could certainly split the attributes out to a separate table, but, like, my focus was on, can I get the deprecated attributes in the table with the status? And then we can look at, okay, I want deprecated attributes in a separate section.
**Trask Stalnaker** 20:20 Sorry, folks, Slack is giving me… Trouble this morning.
**James Thompson** 20:27 Yeah. Yeah, the suggestion was, do we look at splitting out deprecated attributes into a separate table on the spans, for example?
Which… Right. That's no problem to do.
Alright.
**Trask Stalnaker** 20:45 And then, I mean, do we end up bringing… like, doesn't there end up being duplication, then, between that and this page, and do we need to bring back, sort of.
All of these attributes that were… Removed, then.
**James Thompson** 21:03 Alright.
Like, keep in mind, that page there is a mainly created page as well.
**Trask Stalnaker** 21:10 What's that?
**James Thompson** 21:11 That's manually created, that page.
Right, so someone… we have to manually author and write the details there, whereas if we can keep in the tables, it's auto-generated.
We can… if we get to the point of code generation, those…
Attributes can be there, stuff like that.
**Trask Stalnaker** 21:31 Yeah.
Well, that's, … I mean, I think we'll need, potentially, especially because it…
kind of touches on Weaver and migration, I mean, sort of schema migration over time.
We'll probably need, … Josh and… …
Lyudmila's feedback from that perspective, because that may… it might fit into
Something that they have in mind already.
The feedback that I've had on this, on kind of the migration, one-stop migration page, Is that this…
… I mean, yeah, we would need to be able to duplicate, you know, get all of this, because…
… …
The people have found this useful, as far as at least something to go to to see all the changes that are needed when migrating
Which is sort of where, my initial thought of just, like, Like, the minimum…
Changes needed to solve your problem, concern could be just updating this guidance.
**James Thompson** 22:49 Yeah. But you're updated, but… what do you update, though? Right? Right? Like…
like, then I also run into a scenario where I have a database library that uses multiple database providers.
One's stable, one's not.
And that's… that becomes the next scenario.
Yeah.
**Trask Stalnaker** 23:15 Okay. Well, let's bring it back, why don't you bring it back next week, …
And we can get more… unless anybody else on the call today has Thoughts?
**MG Marylia Gutierrez** 23:36 And also somewhat relevant, as a reminder, like, if you are implementing things for, like, Elastic, and you figure out, okay, it's working everything, might be good also to bring back and say, like, thinking this is in a good place, then we can actually mark Elastic as a stable as well.
**Trask Stalnaker** 23:56 But it does sound like something that may have, kind of, may fit into the, kind of, Weaver schema vision already.
I'm just not, … … up-to-date on… dot.
So, sorry, I can't give you, sort of, more specific feedback there, James.
**James Thompson** 24:16 Yeah, but, like, for me, yes, I think it's nice having the automated, but I just thought having those new requirement levels as a quick, easy indicator, right, could help.
Right, it will certainly help me.
**Trask Stalnaker** 24:32 Okay.
Let's see… Florian… Ayyyy.
**Florian Lehner** 24:45 Defiance.
**Trask Stalnaker** 24:47 Conventions for processed labels.
**Florian Lehner** 24:58 So the question is, to give a short summary, …
With profiling, we started to extract, labels from processes, so from a process level.
**Trask Stalnaker** 25:10 And, at the moment, every vendor reports them in a….
**Florian Lehner** 25:14 custom way, basically, and this makes correlation not possible, because the attributes are very different, and so the question comes up, hey, how can we unify the attributes key so they can be correlated across vendors?
There can be different ways, so that we can… could say, hey, we introduced a P-Trov.
Attribute group, that has, a sub-attribute, label, or we attach it, as a…
Like, environment variables to processes.
So that, issue is really about how and where should labels live in a longer context. In most cases, labels are used, at least from the perspective that I have, is that, in Go, but they are also there in Rust, CE, C++, and Java.
And, so, yeah, the question is, hey, …
Where do labels fit in best, so we can make them, autosomantic tension attribute.
**Trask Stalnaker** 26:27 So, can you explain a little… give a little bit more context about where… what these labels are? Is this…
Things arbitrarily, arbitrary things that are put in the context?
**Florian Lehner** 26:41 Yes, yes, they're arbitrary, and, you can label, basically, context. Execution context doesn't need to be HTTP, it just can be an algorithm, or for whatever you want.
And, …
Deep insights we get from profiling extract this information, which, is usually a key and a value, similarly… similar… similar to, environment variables.
And, that's what you want to, report then to the backend. This helps, for example, that you can,
debug,
algorithms, memory allocation, and stuff that is not, covered, with, observability, like, spans and traces. So this is…
I… different area, I would say.
**Trask Stalnaker** 27:38 … How are you handling… how are you extracting the contact
attributes… I know, like, the context attributes are sort of designed to be from the, … …
like, not… they're not strings, right? So you don't really have the, like, baggage. Normally, if you're going to prop… like, it would be baggage, although it would be nice if we had a way to tell baggage not to propagate over the wire.
**Florian Lehner** 28:11 Yeah, what we're doing is, that we look at the thread level, thread local storage of the process, so every thread of the process can have their own, dedicated,
context labels, and we extract this information in the terms of labels. These are usually, really strings. So, the key and the value is, is a string, and the key and value can be arbitrary.
**Trask Stalnaker** 28:42 And would you… do you extract, then, all, like, whatever we put in the context, you're going to stamp that on?
**Florian Lehner** 28:51 Yes, yes, no.
whatever is in the thread local storage, we extract this information.
And, … Provided to user space, and then want to report it, in an ultra-conformed way.
**Trask Stalnaker** 29:07 Yeah.
… I… this actually might be worth bringing to the general specification meeting.
… the reason I says, … there's… So… Context attributes are… …
a little bit limiting, like, you're probably having to not use real API, real OpenTelemetry APIs to read that. You're probably having to…
Go into the data model and extract that data.
**Florian Lehner** 29:48 ….
**Trask Stalnaker** 29:48 So it's kind of unofficial.
… What you're doing there.
To extract the context attributes.
**Florian Lehner** 29:58 Oh, we are extracting not via OpenTelemetry components, we are using eBPF, so we have a few from the kernel side.
**Trask Stalnaker** 30:06 Yeah, I understand that, like, you can get that data, but that data is, the OpenTelemetry…
APIs and SDKs actually don't give you access to that data.
**Florian Lehner** 30:22 Intentionally. Yeah. Well, … You could use the… runtime people in Go.
To get this data.
**Trask Stalnaker** 30:36 Oh, I… yeah, like I said, I… oh, I see the… in Go, yeah, context attributes are special in Go because they have their own built-in context.
… So… At the same time, what you are doing is very, …
useful. Like, this is, so this is a… this is one of my favorite, or probably my favorite, unimplemented, OCEP.
Which would… because there is a lot of times where you want to put stuff into context, and you want that to get stamped onto spans and metrics and profiles and other things, right? Like, I see your question of wanting to stamp what's in the context onto profiles.
I think that
We should have that discussion in the broader context of spans, stamping those things onto spans, metrics.
**Florian Lehner** 31:39 also.
**Trask Stalnaker** 31:40 Right? Wouldn't those be useful things to have on spans and metrics and logs?
**Florian Lehner** 31:47 Yeah, I think we run another issue here. …
especially thinking about the eBPF profiling, is that, we have a system-wide view, and, with the regular, hotel approach, there's… you have only enclosed, view on various components,
usually inside a Docker container or any Kubernetes environment. And, so we don't attach these attributes, on the resource level, but rather on the sec trace level. So there is no one-on-one mapping that, that we have, and
the profiling runs as a daemon set, so it has a complete view on the system, and …
Yeah, hotel… prof… because the resource profiles don't scale that well. If you have
I don't know, 500, 200 Docker containers with I don't know, each… 5 different services.
then this doesn't scale well. So we attach this information, or we have, on the resource level, on the resource level, we have only, system level information.
But the more interesting resources, like, context attributes, or what is really, associated with a process is really only on a stack trace.
**Trask Stalnaker** 33:20 Right, a single sampled stack trace.
**Florian Lehner** 33:23 Nope.
**Trask Stalnaker** 33:24 Yeah, and so, I mean, that… those same context attributes that you're stamping onto the stack trace to give more context about that stack trace.
Are often very… Interesting pieces of data to stamp on spans.
To give more context about your… that span.
**Florian Lehner** 33:45 But for SPANCs, we have a dedicated field and protocol.
So, span… span trace and span ID will not be part of an attribute, but more like, they are directly… for them, we have a direct field in the protocol.
**Trask Stalnaker** 34:04 for context, I might not be quite… I might be missing something.
**Florian Lehner** 34:10 For the, for the span, trace and span ID?
We have dedicated… Message link, I think it is.
**Trask Stalnaker** 34:19 Yeah, but what about arbitrary, context attributes?
**Florian Lehner** 34:24 For them, we don't have a field. For these fields, we use regular auto attributes.
**Trask Stalnaker** 34:31 Right, but there's currently, in the span domain, in tracing, there's no way to… you can't write a span processor?
that stamps context attributes onto your span, because there's no API… there's no OpenTelemetry API for reading context attributes.
Reading the whole… all the context attributes.
**Florian Lehner** 35:00 From an industry point of view, yes.
I think…
or at least there's a patch for… a possible patch for, Autel EVPF, so the donation by Grafana with Belay, they have the same capabilities. They can, extract span trace and span ID, as well as, context information.
And, here, we would… EDRL, in a perfect world, people would love to speak together and correlate.
**Trask Stalnaker** 35:31 Yeah, yeah. No, I understand that there's ways to get the memory data, the data in the memory that's in the context attribute.
But there's no OpenTelemetry SDK, so if I'm… if I wanted to write a span processor.
That stamps context attributes onto spans.
There's no way… There's no way through the official OpenTelemetry SDK to do that.
**Florian Lehner** 36:03 Probably, yeah.
**Trask Stalnaker** 36:04 And so I'm, I'm…
it would be… I think it's worth, …
Having that discussion, having this discussion, basically.
You know, in general, before we decide to go off and do something very, you know, specific to profiling.
It is an issue that has been brought up in the past, like this OTEP
In particular, as a way to… …
Have things that get stamped on your telemetry.
… And I guess that's a question for you from the profiling perspective.
… Right, like…
how do you… how do you know which context attributes… I mean, you're probably grabbing everything, but that… …
I guess from a profiling perspective, since you're already at such a low level.
maybe that makes sense. You're picking up so much data, but also.
You know, that does bring up
obvious security, concerns, like, around sensitive data, that may be in those context attributes.
Versus….
**Florian Lehner** 37:29 Yeah, but this… this we already have.
So, you have already sensitive data. If you look into environment variables, if you look into stack traces, this train is gone, I think.
**Trask Stalnaker** 37:41 Right. Yeah, that's true, if you're capturing all the environment variables already. Yeah, that makes sense.
**James Thompson** 37:49 If I'm not mistaken, isn't the idea is to be able to have a link between spans and profile messages? Because profiles are omitted via a separate API.
Alright.
And there's a issue floating around for sharing IDs between them.
Right? So, wouldn't you have your profile being omitted from your profiler, which could then be connected to your span?
**Florian Lehner** 38:20 I think this is not possible at the very moment, as the traces API, or the…
traces implementation in the collector does… or in the collector, the collector does not know about the message link and the profiles protocol yet at the moment. We are not at this level. The protocol is…
Changing that much, and … we are getting only one sub-message at a time, and …
Refuse on this message, on these changes is, slow.
**James Thompson** 38:54 Yeah, no, but I'm pretty sure there was an issue where, like, there were… I think there was two donations of different approaches to sharing that ID.
Right?
Alright.
And so that way… So… so there's an issue…
Right? So, Elastic has an approach for sharing IDs.
Between profilers and that… between profile and spans.
**Florian Lehner** 39:22 Oh, yes, APM, and, this is… was a proprietary approach with APM, and, will be removed.
**James Thompson** 39:29 Yep. Alright, and there was another approach that was also Discussing that issue, right?
**Florian Lehner** 39:34 There will be an implementation at one day from, probably, Datadoc, but this is… far from…
having stable… so there's just a rough idea that we want to have it, not how it's done. The problem is that the SDK and profiling side need to agree on some kind of communication, and this is far off.
… Sometimes it's missing.
**Trask Stalnaker** 40:06 Florian, so the… looking at the specific proposal here, so process… these can be…
These are gonna change, right, within the, like, over time, within a single process.
**Florian Lehner** 40:26 Yes.
**Trask Stalnaker** 40:27 So, I would… The, at least to me, process doesn't feel like the right… Namespace…
And in fact, I would be kind of tempted to… Call it, like, context.
Something, like, to be very specific that this is, like, hotel context.
**Florian Lehner** 40:48 data extracted….
**Trask Stalnaker** 40:50 ….
**Florian Lehner** 40:52 What about process context, and then process context stable?
**Trask Stalnaker** 40:58 is… Anything….
**Florian Lehner** 41:01 I don't know if process context exists yet, or what discussion maybe that would make sense.
**James Thompson** 41:08 But then the question comes up, do we need the base name, given that these are emitted via a separate API,
What other attributes would we be emitting?
Like, for me, the key is almost… A one-to-one mapping.
Right? Because you already know it's a profile message, because it's submitted via the Profiles API.
**Florian Lehner** 41:29 Not really. It can also be emitted by the instrumentation dominated by Grafana, which was Bile.
**James Thompson** 41:37 But… but shouldn't that… shouldn't that be updated to actually send that data via the Profiles API?
That's why we….
**Florian Lehner** 41:46 No problem.
No, they sent data, probably, we are at, Tracer's API.
**James Thompson** 41:53 But… But the Traces API is quite different to the Profiles API.
**Florian Lehner** 42:00 Yeah, this is correct. That's why I want to have a common label or a common attribute that, at the backend can then correlate the information in some way.
**James Thompson** 42:10 Yeah, but even if we were to get rid of that
base key, we would have… still have that correlation.
Right, it doesn't matter if it's coming in via trace.
or it's coming in via the Profiles API, it's the same key in both scenarios.
**Florian Lehner** 42:26 Yeah, that's why we need some understanding of the same key here.
**James Thompson** 42:30 Yeah, no, but the same key is whatever's being pulled out of the context, for me.
Right? It seems… Unnecessary to be prefixing the keys.
Right? When you know this message is a profile message, right? Especially if it's coming via the Profiles API.
**Florian Lehner** 42:51 So you mean that, …
From the shown example on the screen, we remove process.Delabel dot, and just use key and value.
**James Thompson** 43:00 Yes.
**Florian Lehner** 43:01 How do you want to correlate this? Because, thinking about it at the back end, how would a backend…
Treat this information.
And what's the difference… what's the difference to process and environment variable, where you can say also, hey,
Key and value can be arbitrary.
**James Thompson** 43:21 Alright, so… like, I don't… You already know, based on the message, that it's a… A profile message.
**Florian Lehner** 43:32 Same for the environment variable. I know it's an environment variable, yes.
**James Thompson** 43:37 Not necessarily. We don't have dedicated API messages for environment variables.
We have a decade….
**Florian Lehner** 43:46 I also don't have one for labels.
**James Thompson** 43:48 No, but you have a dedicated profiles one.
**Florian Lehner** 43:51 So… No.
**James Thompson** 43:53 There's a dedicated gRPC service for profiles.
**Florian Lehner** 43:58 Yes, yes, yes, but it's an attribute, that's not a first-class citizen field that we want to communicate. It's just some additional information, just like we collect environment variables and then communicate them.
**James Thompson** 44:13 So… But….
**Trask Stalnaker** 44:14 James, I think that what you're describing is similar to what, like, in the logs bridging, when people set, like, in a third-party logger, they stamp attributes.
And… We have, in that case, …
Doing, like, initially we were going with, like, a prefix, like a log for j dot Label.something.
And we did decide for those that, that wasn't needed.
In… I do see a slight difference here, though. Like, in that case, it's a very active, like, somebody is setting an attribute on their logger.
It is very intentional, like, it's very for that purpose of stamping that on the log message, and so it…
say it makes more sense for us to not prefix that, because that's sort of like them using the OpenTelemetry API, logging API. Otherwise, we don't give them a way to create their own attribute name.
In this case.
It feels a little different to me because we're going in and scrape… basically, we're scraping all the context attributes, which aren't really…
designed for exporting, haven't been designed for exporting previously. And so it does make sense to me to…
Qualify those somehow, … to be specific.
**James Thompson** 45:59 But then the next question comes up, if you look at a profiles message that's come in.
What other attributes would there be other than these contexts?
Bye.
Because….
**Florian Lehner** 46:11 We have a tom. We have a tom.
**James Thompson** 46:14 You know, Other than the internally defined profile ones.
Yep. Alright.
**Florian Lehner** 46:19 Process executable name, for example, process thread name, for example, just to name two.
**James Thompson** 46:26 Yeah, right? So… But that's, for me, no different to a messaging one, right? Attributes.
Right? They, they… Yeah.
**Trask Stalnaker** 46:37 This is kind of… I mean, my… the reason why I… I…
like, prefixing these is, I see this as… …
some of it's going to be junk data, because it's just… it's really not designed for exporting, right? Like, I get the scraping it is, you know, does provide value and does provide insights that you wouldn't get already.
But it's also….
**Florian Lehner** 47:14 We cannot hear you yet.
No.
Maybe I…
I hope Charles can hear us, and I will continue for the moment. The motivation also for this, for this… for a defined attribute is that, AutoCollector can apply filters on it.
Can apply filters on it and say, hey, if this attribute
shows up, keep it or drop it. That's the very same for, process environment variables, where the… where the… where there can be a process, filter.
A filter process, that,
Just removes or drops certain information.
I agree that, We have megabytes of data that we are sending over, over the wire.
And, … Sometimes it can be too much, but, yeah.
**James Thompson** 48:19 Yeah. But I don't see that filtering decreasing by dropping the key… dropping the prefix to the key.
Right? Unless you want to drop every single Right? Process.label attribute.
**Florian Lehner** 48:38 I think it depends on how you define your filter.
**James Thompson** 48:42 Yeah, but that, that would be the only… The ability to drop any… process.label attribute.
right, outside of the profiler is the only scenario that benefits from having that prefix there, is the only scenario I can think of.
Right? Because I don't….
**Florian Lehner** 49:00 I think it….
**Trask Stalnaker** 49:00 Oh, sorry, can you hear me?
We can now.
**Florian Lehner** 49:04 Yes.
**Trask Stalnaker** 49:05 Okay, sorry, my headset died. All kinds of fun, this morning. …
James, I'm not really, … I mean, we'll need other input, but I'm not… it really feels to me like we would prefix
This stuff, somehow.
But let's… I mean, let's wait until we can get more feedback from other folks.
**James Thompson** 49:32 I think another thing to consider is, could any of those context ones be already defined?
Semantic convention attributes already.
Right?
Yeah, and if it does, that….
**Trask Stalnaker** 49:45 They should… they shouldn't be… I mean, context is not where you put those….
**James Thompson** 49:52 But in the links provided by Florian, there's examples of where you… the examples show that scenario. You generically attach attributes to the context.
Via code.
Right, that was in the examples provided.
**Trask Stalnaker** 50:09 Okay, that's not my experience with Java instrumentation.
We… we will… if there's some bundle of things we need to pass down, we'll stick it in an object in the context, and then we'll extract it later, you know, when we need it, by passing around this key that is what
That's the whole, like, reason why the context isn't readable, really, like, because you have to have that key, this kind of opaque key access to it if you want to read it.
Later.
**James Thompson** 50:46 I think if you scroll down, we actually spoke about the examples based on the documentation that was linked
Which showed setting things into the context.
**Trask Stalnaker** 51:01 Can you point me to what… The open telemetry docs?
**James Thompson** 51:07 No, it keeps rolling down.
see the go dot labeled … was it that one? Yeah.
It was in those links.
the… record profile labels.
Mink.
**Trask Stalnaker** 51:21 This one?
**James Thompson** 51:21 Yeah.
**Trask Stalnaker** 51:24 Yeah, I mean, Go is…
A different… slightly different beast with context than because they had… the language has context.
Built in.
And so there may be pro- conventions, right? This is 2017, before OpenTelemetry existed.
**James Thompson** 51:44 Yeah.
**Trask Stalnaker** 51:45 So….
**James Thompson** 51:46 Like, but that's the example I was given around setting the context.
Right, and that showed the code to add things into the context.
**Trask Stalnaker** 52:01 Yeah, so let's….
**Florian Lehner** 52:02 I provided also a rustic sample song in this issue.
**James Thompson** 52:06 Yeah, and that was also similar.
Right? That you could add things in.
Right? So, for me, My hope would be…
That if you're setting things in, ideally they're using already defined attributes where possible.
**Trask Stalnaker** 52:24 No, no, that's not how open telemetry context
works. The OpenTelemetry context is not for setting semantic conventions.
**James Thompson** 52:35 But the example provided for profiling is that.
**Trask Stalnaker** 52:38 Then those examples are not correct.
So let's try to move on, James. we'll… I mean, either way, we're not, you know, we're gonna need more input on this.
My suggestion, Florian, I think the one thing that wasn't… …
clear to me initially was just that these are, and I know you say, but, like, just that these are context attributes, and kind of…
Scraped out of the context.
… And… I don't think… I feel like all the process… Attributes are fixed.
By the process, in the process.
**Florian Lehner** 53:29 ….
**Trask Stalnaker** 53:30 And so that's where the process namespace doesn't feel quite right to me.
… but maybe put in, like, Kind of a couple of…
like, I'll, like, list a few alternatives.
And then, like, concisely.
then we can get more feedback on specific ones. Like, I would include something like.
even though, I don't know, like, hotel context dot something, ….
**Florian Lehner** 54:05 Okay, yep, makes sense, makes sense. Thank you.
**Trask Stalnaker** 54:08 Yeah.
And it's an interesting… yeah, I'm trying to think if there's… I guess…
My initial thought of trying to…
I'm just always trying to move this closed OTEP ahead, so part of me wants to use this as leverage to move this ahead, but I think I understand that it's not really, really you all, you're…
You want to scrape the context attributes.
So… Yeah, and I think I would even, like.
I almost feel like using that term and describing it, that we're… you're scraping it, as opposed to, you know, this is not…
OpenTelemetry data model, official OpenTelemetry data model, Stuff.
**Florian Lehner** 55:02 Okay, I see.
**Trask Stalnaker** 55:08 But we can get more feedback, Next week, hopefully, from, … Josh…
Josh has been pretty involved in the… profiling….
**Florian Lehner** 55:21 Nope.
**Trask Stalnaker** 55:21 And Lumila will probably have thoughts on naming as well.
But thank you, I… I think I understand this.
Now, … Also…
Alright, did we get….
**Florian Lehner** 55:40 Thank you.
**Trask Stalnaker** 55:41 Yeah, thank you. …
We're getting towards the end of our time box. No… any other topics anybody wanted to bring up briefly?
**James Thompson** 55:55 Trust, can you look at that PR that I tagged you in a week and a bit ago? So…
I'm trying to… So there's Java Resource Detector for Azure, which has attributes that are not documented anywhere.
That one.
Alright.
**Trask Stalnaker** 56:19 Okay.
**James Thompson** 56:20 So you're the component owner for the Java one?
I assume that's probably where the .NET example came from, but there's attributes that don't actually exist in semconf, so I've just defined those attributes.
**Trask Stalnaker** 56:32 Okay, cool. Yeah, I will, also, I will ping… …
Gregor, who is actually the author, wrote that.
Alright.
Thanks, folks!
Have a good one.
**Christophe Kamphaus** 56:57 You too.
See you.
