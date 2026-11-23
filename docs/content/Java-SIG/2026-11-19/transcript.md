SIG: Java SIG
Date: 2026-11-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:53 Hey, everyone.
Please add any topics you have to the agenda.
**Robert Niedziela** 02:31 Boom.
**Trask Stalnaker (Microsoft Corporation)** 02:37 We'll start in one minute.
Alright, so… let me share my screen… Not much on the agenda today. I don't think we have any significant Thing to talk about here, unless anybody has anything.
So, let's go to Robert.
**Robert Niedziela** 03:51 Yeah, So, the PR I wanted to show you here, this is for socializing the idea. If you have some, objections or suggestions or recommendations.
I wanted to extend the JMX configuration in the instrumentation development Java, with possibility of defining inline rules.
with the same format as it is done in current YAML external files.
Yeah, it seemed natural to me that it would be beneficial for users to have this ability and distribute just one file instead of set of files.
So, yeah, that's what I wanted to add here. If you could scroll down a bit, there are some… yeah, that's the, let's say, more rich example.
With… combined with, available options that you have right now, so config, metrics, filtering, right, included, excluded stuff, plus rules.
Mmm… The change is not very big, it's just a few files, and with some extension of JMX Metrics Builder.
That started some discussions around, so if you could go a little bit down.
Yeah, so that's the discussion, if we should add this, add one more add rule variant to the public API of JMX Telemetry Builder, or keep it… As an internal, I've been very grateful for some feedback on it from other reviewers as well.
I see some benefits of having it in public API, but yeah, I know that there is some, Cost to it, about future changes.
And yeah, Lauri already suggested that, the internal API approach is also reasonable… Yeah, that's… To me, it's okay.
**Trask Stalnaker (Microsoft Corporation)** 06:14 Oh, I see, so this is something you needed access to… Or implementing the declarative config.
Yeah, so we do, I don't see Larry's comment, but yes, we do that, in… Several places where we need Internal access, so yeah, we'll do, like, a .internal, a class called internal, in there.
That just gives us access.
**Robert Niedziela** 06:52 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 06:52 So I would, yeah, I would design the API around what users, the public API around what external users want.
Need.
**Robert Niedziela** 07:04 Okay, so I have to tell you that I need this in my custom code as well, so that's why I also started adding it to public API, but that's fine for me to use internal as well, if there's some concern.
Yeah, and the question.
**Trask Stalnaker (Microsoft Corporation)** 07:28 Yeah, maybe you can explain, yeah.
**Robert Niedziela** 07:30 Also, the question is if we should use the list of maps that keep the YAML tree.
Or we should use the clarityconfigProperties class.
I didn't use it because at the time I started working on it, this was still in incubator, so I decided not to put incubating stuff in public API, but now it stabilized, so the situation changed.
**Trask Stalnaker (Microsoft Corporation)** 08:10 Yeah, so what would that, Maybe you can kind of lay out what that would look like.
sort of the options. Maybe, maybe you could, like, if you could write up, sort of, what the different options are in both of these cases.
public.
**Robert Niedziela** 08:34 Okay, in this PR, just for reviewer, right? Or, or…
**Trask Stalnaker (Microsoft Corporation)** 08:38 Yeah.
Yeah.
**Robert Niedziela** 08:40 Okay, okay.
So, yeah, that's what I wanted to show today, and we'd be grateful for feedback.
I will do what you suggested, Trask, and add options that we can use here.
**Trask Stalnaker (Microsoft Corporation)** 08:59 Cool, and this is awesome. Yeah, yeah, I'll… This is very nice to get rid of the external file.
**Robert Niedziela** 09:08 I mean…
**Trask Stalnaker (Microsoft Corporation)** 09:09 We can… we could… So, I see you're… it still has the ability to load from an external file.
Is that something that… are you thinking that… is that, like, a backwards compatibility thing, or is that… are you imagining people sort of having these shared…
**Robert Niedziela** 09:32 It's for…
**Trask Stalnaker (Microsoft Corporation)** 09:33 files…
**Robert Niedziela** 09:35 you know, it's hard to tell, right, what customers want. It was there, it's just kept for backward compatibility, But we can get rid of it at some point. The issue is that it's not… the schema is not defined anywhere here, right? So if we just remove possibility that we had.
Someone might be not happy.
**Trask Stalnaker (Microsoft Corporation)** 10:00 So, in, external GMX… files in the existing schema, you could reference other external files from that one, so that you only load the one, and then that one, that references others? Is that how it works today?
**Robert Niedziela** 10:19 I don't think we have other files referencing in YAML files. I'm referring to this here, the config option where you can point to external file, right?
Actually, you can refer to multiple external files if you need.
**Trask Stalnaker (Microsoft Corporation)** 10:39 Oh, this exi- this one here, you can give it a list today?
**Robert Niedziela** 10:45 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:47 Gotcha.
Yeah, always looking for opportunities to simplify Things, and not, include things that… Especially in a new feature. I mean, this is, sort of net new, like, that if people want them.
They can sort of combine them all together. But I also know those JMX rule files can be very large.
So, maybe… Some people, like…
**Robert Niedziela** 11:30 I checked our built-in mappings, and the biggest one has 16 kilobytes, so… No, there's no tragedy, let's say, here, so… But I can imagine that someone will create really huge roll files.
**Trask Stalnaker (Microsoft Corporation)** 11:49 Yeah, what 16 kilobytes is… how many lines of… how many lines? More I'm thinking of, like.
Could explode somebody's declarative config file.
**Robert Niedziela** 12:01 It may, but in this case, in this edge case, this config option may be useful, so the external file is there, and file is there, and if someone wants to have really big mapping, can use external file.
**Trask Stalnaker (Microsoft Corporation)** 12:16 Right.
Okay.
Cool. Anybody… any… anything else you want to say about this, or anybody else have… Comments?
At this point.
**Robert Niedziela** 12:38 Okay, thank you.
**Trask Stalnaker (Microsoft Corporation)** 12:40 Thank you.
Hey, we're at the end of our agenda.
**Aditya Kousik** 12:49 Oh, would you… hi. Hi there. Aditya. My name is Aditya. Should I have added an agenda before the meeting? Sorry, this is my first time.
**Trask Stalnaker (Microsoft Corporation)** 12:58 Oh, yeah, it's fine, we, we add… Topics on the fly all the time.
**Aditya Kousik** 13:04 Okay.
Maybe I'll, I'll add my, piece to the agenda.
So I was looking to discuss, this issue, if we have the time.
So, quick contest, hi, I'm from Apple. My name is Aditya. I work on a lot of the Apache Kafka instrumentation at Apple, and one of the, current blockers right now is… the way Kafka works is you pull a batch of records, and you can process them one at a time. The expectation of the library is that you process each record in, you know, in the same thread that you would poll. So, the way instrumentation works is you instrument the iterator.
And the time between next and hasNext is the time it took to process. But this has some issues, and there have been, known bugs because of this, and I've linked one of the 1947 there, it's an outstanding bug in the client's code.
Where you can create a duplicate span, you can create, if your iterator throws an exception midway, your trace is sort of, like, out of whack.
So, there are some issues with the current API. So, I wanted to propose a way, an API, such that, you know.
we can sort of extract the trace parent from an annotated consumer record method. So, the idea is, people, what they expect is, since consumer records is an iterator.
I can just, like, iterate through each record, and then submit to another thread pool. But the context is held in the consumer records iterator, so the minute that consumer records leaves that iteration, its trace is lost, the trace parent is lost, and it, every time I start a process in a new thread, it starts a new parent.
And that link is gone.
And so, for example, if you have, like, ingestion workflows where I have fan out of, like, you know, tens of thousands of records from a single trace parent, it… I know I've lost that link, and, you know, it's now 10,000 new root spans.
So the… the proposal I wanted to have is, if I'm processing in the instrumentation annotation, if I can add, like, an at-span parent annotation on a consumer record.
And this, by the way, this is not just restricted to Apache Kafka. This applies to SQS and other message carriers as well.
where, you know, I can… in a method where, you know, if you have kind consumer, I can annotate a method as a parameter as this is a span parent.
And it can extract the trace pattern header from that carrier. And for consumer record, it would be the record headers, and you can apply this for other APIs as well. And so this is useful for, like, pool-based models where you can Fetch a batch, and then you want to set the context current based on that object, and not opposed to… as opposed to, you know, the batch itself, which typically has the context.
So, there are some intricacies here, you know, like, in terms of you don't want to ma- right now, we only support, like, a single, like, a one-to-one, so you don't have batches, against the span parent.
And I think it won't work against… we need to make sure that it only works against known heights. So, for instance, like, any arbitrary type can't be annotated with the span pattern. In that case, we'll have to default to the context current.
And, yeah, basically, that's the gist of it. So this is, this is… this is a problem, I think. The root cause of this is, again, that Kafka and other message-carrying types treat iteration as processing, because they do it in the same thread.
And, I've seen it in OTEL, I've seen it in other vendors, like Datadog as well, where it's a known, list, it's a known issue, and they have workarounds, and the typical workaround is… because consumer records is a list of consumer records, what you can do is, because the GET method is not it's not instrumental, you don't go through the… sorry, it creates a sublist. So you can create a sublist of I and I plus 1 when you're going through list by list, and then you can iterate a sublist of an item 1, and that'll work, because it's still… the iteration is passed down to… all the way down to the the last list iterator. And so that's a known workaround. OTEL doesn't support it, but Datadog does, because we don't instrument the sublist in. So, anyways, it's… it's a bit of a hacky step there.
But, this will help, you know, customers who tend to sort of, like, you know, hand it off to another thread pool. And even… I don't even need to do a thread pool. For instance, I could just, like, pre-aggregate and, like, filter, right? Like, I could just go through the list, and from 100 records, I could just filter down to 10 records that I'm going to process. It could be in the same thread, but once I'm done iterating.
context is lost. I have to find a way to extract it anew.
So this method, I think, can help achieve that.
That's my… my taste.
**Trask Stalnaker (Microsoft Corporation)** 18:20 Did you, so I'm curious, Your thoughts on annotation-based solution to this versus, API… based solution… Yep.
They're…
**Aditya Kousik** 18:39 I think there's an incubating API that I saw, which actually, like, you can actually set the… I remember there was, like, a context wrapper that you could add.
Where, you could, like, pass it… you know, if you have the API, yes, it does allow you. Like, you know, you can… there's a… there are certain boilerplate that you could do to set that up. I'm blanking on exactly which
**Trask Stalnaker (Microsoft Corporation)** 19:07 Yeah, I think we… I think… I think, there was an attempt… I think what…
**Lauri Tulmin** 19:17 Trask was asking is, Did you consider just, like, calling a Java method instead of using an annotation?
**Aditya Kousik** 19:26 Yes, I did consider it. So, at our place, it's, teams want to, we, we prefer the Java agent method, where auto-instrumentation is the method, it's the way, rather than… but yes, it's, Java does work. Like, you can use the API to set up your context, and that does work.
But for cases where, teams just automatically just add a Java… attach the OTL Java agent, and, you know, you get instrumentation for free for Kafka client metrics and all of the context propagation.
**Lauri Tulmin** 19:58 What I was meaning more is, like, what you're trying to do is that you have a method that accepts a consumer record, and you have the annotation, but instead, you could call some sort of Java class method, where you pass a consumer record and get the same information from there.
Did you consider that?
**Aditya Kousik** 20:19 Yes, that still requires, creating a common, method that teams across would share, and, That has… yes, that would work.
And that's the…
**Lauri Tulmin** 20:33 It would be, like, an API method similar to the annotation.
That you include some sort of external library.
That somehow just works.
**Aditya Kousik** 20:44 Yes, that does. And that's a… that's an alternate, considered. It's just, From my experience, it's… it's been teams that are a little hesitant on, depending on even the OTEL SDK as part of the dependencies. They just… they prefer the auto-instrumentation that the Java agent provides, because they can attach it, they can point it to an, you know, OTL collector, and, you know, they're onboarded already.
But… I'll take… I do take your point. A custom library that does actually call out to the SDK does work.
**Trask Stalnaker (Microsoft Corporation)** 21:23 So, it's worth looking at this attempt. I dropped a link. This was sort of a thought, around providing some kind of a common, like, a lib… like a… Library that we could ship.
And I think we had thought that if this worked out, we would move it into the… not the contribib rep repo, but in the library… in the instrumentation repo itself.
Yup. Worth looking at it.
It's also worth, I would say, sending, you know, send a PR, I mean, go ahead and, like, kind of… play this out, and send a PR, like, that's sort of what helps us to evaluate it better, is.
**Aditya Kousik** 22:13 Okay.
**Trask Stalnaker (Microsoft Corporation)** 22:13 How… seem… how it works out.
**Aditya Kousik** 22:16 How it looks… yeah, yeah, that makes sense. I thought this would have been the first, you know, to do sort of, like, a design doc, sort of, to get… and if the approach looks right, I'm more than happy to, to submit a PR, to get a picture.
**Trask Stalnaker (Microsoft Corporation)** 22:28 Trust.
**Aditya Kousik** 22:29 what the instant.
**Trask Stalnaker (Microsoft Corporation)** 22:29 Yeah.
So it… I mean, we may… End up not liking it, still.
**Aditya Kousik** 22:37 Yeah, that's fine.
**Trask Stalnaker (Microsoft Corporation)** 22:38 But, it's… a lot of times, going through those details can kind of show us if… if it's working out Well or not.
**Aditya Kousik** 22:52 Yeah.
There's a… there's another approach that I've mentioned in the alternative, but it's more long-term, and it's nowhere close. If you actually scroll down, there's a link to, KIP1305. So, this is a very Kafka-specific proposal. So, my proposal is actually I'm making a change in the upstream client itself, saying, say, here's the, you know, current, limitation.
It would be helpful if we can have a per-record context processing for… from… at least for the Kafka consumer perspective. And so, this would allow OTEL and other vendors to move away from having the iterated model, and have… I basically propose, like, an auto-closable method in the consumer record. So I could say, hey, open a context from the, from the consumer, and basically, context.run with a lambda, and so it'll capture error rate, you know, exceptions, timing, and all of that. It's, like, if you scroll down, it's like an example. But this is, again.
This is a more community-based, approach, so that example is what I'm trying to, trying to get to.
Right now, if I do, execute it or execute in a processor record, it breaks. But, what I'd like is I could say record.nuert context, and then I could run with that handle method. That handle method is what I want to annotate with that, annotation now.
But this would sort of, like, if you can have an OTEL context processor, like, you know, like OTEL metrics, reporter, etc, like, basically, it would buy into the… It's a first-party API for, instrumentation library to implement, and you can add an interceptor to the, you know, that'll auto-inject itself.
And this would just… This would work, so that every time someone… if the people call it with new context.runwith.
And if OTEL has a context processor registered, then we could capture all of the timing within this landlord.
And… or it could be on whatever thread, because we've already, the record has the actual, trace parent header in it, and it will set itself up.
So, this is another, option.
But the Apache governance means, you know, we have to participate in the KIPP mailing list, like, if you scroll to the top, there's, like, a discussion thread. And already I, I have other vendors, like Datadog also commenting that it might be a useful feature. So, again, that's an alternative.
But yeah, this, tackles the client itself, as opposed to You know, having to work with, you know, workarounds with.
At the hotel layer.
**Trask Stalnaker (Microsoft Corporation)** 25:27 So this, I mean, the… this doesn't solve, sort of, the… we still leak… the context… Right in this approach, where if there's an exception thrown.
Cause we make… we make it current.
**Aditya Kousik** 25:49 During…
**Trask Stalnaker (Microsoft Corporation)** 25:50 iterator.
**Aditya Kousik** 25:51 But, run with is the one that actually… so the new context would have to, like, suppress the iterator context, because then you'll be double counting, right? So, my assumption is that iterator is sort of, like, no longer the… source of truth of the context, and that record.nute context is the one that actually loads the context, and we'll have to, like… otherwise, you'll double count, you'll… the UI will look like, you know, you have an iterator, and then the actual… there's a gap, and then there's the actual processing. Because if… if the executor.execute you know, has, like, a queue and delay, then it's gonna show up as, like, two different spans. But this way, you can sort of, like, suppress the iteration, context, and just use the record.nuteContext.run with. That lambda captures the runtime and exceptions caught, so you can tag whatever exception class as well in that.
So, that'll handle that.
**Trask Stalnaker (Microsoft Corporation)** 26:43 From an auto instrumentation perspective, how would we know that this was being used, or, you know, I'm using this also as an example for your current proposal, where you're withspanning this method.
How would… how would we know to not instrument the iterator?
**Aditya Kousik** 27:14 I mean, the default is that we always fall back to context current, and so if we already have a current context, and it matches the context, pattern context that we extract from the header, then we know already we're already running it in that scope.
The way we know that hotel should auto-instrument is, that it's part of the public API. There's an interface that I'm defining called a context processor, which, you create the Kafka config, or the Kafka consumer with.
And we intercept the config object when you create the consumer. So there we could say, oh, here's an OTel context processor, in addition, because that's what we do right now with metrics reporters. We actually, like, add our custom metrics reporter to the Kafka config object.
In that config object, we would add an OTelContextProcessor, and so every time someone calls record.newt context, the hotel context… and it's meant to be, like, a composite, so you could have multiple context processors, so OTel would be one of them.
And so, when… anytime some user calls record.newcontext, they would get The hotel context, automatically, applied within that scope.
Of the runWith method.
**Trask Stalnaker (Microsoft Corporation)** 28:33 So, I was… sort of the API that, if I recall here.
I was hoping to, like, not basically have a different API that didn't involve the iterator, like a for-each kind of style, basically, like you would do on records, and… like, the problem to me with the Kafka API is there's not, like, a… It's not a callback, it's not like a, process this.
**Aditya Kousik** 29:04 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 29:05 And… So, I felt like if there was something that, you know, was, like, processed this, processed these records one at a time.
And then… And then we can wrap that successfully, you know, in our own tri-finally.
**Aditya Kousik** 29:24 Yes.
And that's what I'm proposing here. So, if you scroll down, like, there's a public interfaces section, And what I'm proposing is, so that create context would create that consumer record context. So this would be the, consume a single record. That action is the thing that I'm, proposing.
So, that would be a first-class API that Kafka would propose, and that run with method is now going to be public API, and so now we have a context of… you know, what to do. So that's your try-finally wrapped.
**Trask Stalnaker (Microsoft Corporation)** 30:02 I see, and this is… so this is sort of super afloat.
**Aditya Kousik** 30:06 an exemplar.
**Trask Stalnaker (Microsoft Corporation)** 30:06 as…
**Aditya Kousik** 30:07 Yeah, it's just an example to show that, you know, you can do it from another thread pool, and it will still work. Whereas right now, if you do record.process, handleRecord, it's broken.
**Trask Stalnaker (Microsoft Corporation)** 30:21 Handle record here… so… do… don't we make… I would have thought that the context would have gotten propagated here… If I'm remembering the iterator, we make current when it… we make current, and so shouldn't that current one propagate across the… into the.
**Aditya Kousik** 30:43 The correct poo?
**Trask Stalnaker (Microsoft Corporation)** 30:44 Executor? Yeah.
**Aditya Kousik** 30:46 The examples that I ran, it did not, and the reason for that… Yes, I see your point.
And… I'll have to, dig into that. Yeah.
**Trask Stalnaker (Microsoft Corporation)** 31:02 Cause I don't remember…
**Aditya Kousik** 31:03 Same thing with HTT.
**Trask Stalnaker (Microsoft Corporation)** 31:04 Yes.
**Aditya Kousik** 31:04 Kim.
**Trask Stalnaker (Microsoft Corporation)** 31:06 I don't remember hearing this particular problem with the iterator approach. The problem that I've always heard is the leaking of the context because of the exception. Basically, we have no final…
**Aditya Kousik** 31:20 Yeah, yeah.
maybe this is a contrived example that maybe doesn't apply. But I… let me run a quick… a small test, and I'll… maybe we… if we could continue the discussion on the issue, maybe I could summarize the approaches here, the Java API-based one, and, you know, the example that I gave.
I guess. Yeah.
**Trask Stalnaker (Microsoft Corporation)** 31:44 Again, though, like, a PR, you know, then we have tests, and, you know, that can… I'd be fine with going and discussing it on the PR.
**Aditya Kousik** 31:55 Yeah, that sounds good. So if this is also a useful API, then, you know, if you scroll to the top, there's a discussion thread, there's, like, a mailing list that you can also mail to, saying, you know, there's a… right above there, there's a discussion thread.
**Trask Stalnaker (Microsoft Corporation)** 32:08 Oh,
**Aditya Kousik** 32:11 So, yeah, there's a… you know, you can just reply to that, you know, on the context of… I remember. Like, I gave examples of, like, where it works. The UI is a bit broken, but this is the place where, you know, these design discussions can go on.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 32:33 Cool.
**Aditya Kousik** 32:34 Yeah, thank you for giving me the opportunity to talk about this, and I appreciate the…
**Trask Stalnaker (Microsoft Corporation)** 32:41 Yeah, and let's, I think probably what I would do… will do is, wait until we sort of figure out what approach we want to do in, OpenTelemetry, and then, yeah, and then that will also give me the context to fully understand this proposal, and then I'm happy to comment on that.
**Aditya Kousik** 33:03 Perfect. That's all I wanted. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 33:06 Yeah, thank you for tackling this long… that's a… What do we got?
**Aditya Kousik** 33:12 It's… it takes years. 1947 is 2020.
**Trask Stalnaker (Microsoft Corporation)** 33:15 Yes, very old issue.
**Aditya Kousik** 33:18 Yeah, 2020 December, yeah. 2020, those are 6 years, yeah.
Yeah.
Hopefully we get some closure on that.
**Trask Stalnaker (Microsoft Corporation)** 33:32 Alright, let's see if any… nobody snuck in with another topic.
So, last call for topics.
Otherwise, enjoy the day!
**John Watson** 33:53 Well, I guess only one very small topic, which I think is barely relevant.
Do we need to make sure we have all of our images upgraded for all of our test stuff for Java for Shell?
**Trask Stalnaker (Microsoft Corporation)** 34:10 I don't… see how… I don't think that should impact our tests, but yes, all our… all our images should be on, Renovate, should get auto-updated via Renovate.
**John Watson** 34:27 I mean, who knows, maybe somebody figures out in Track, and they put in a PR, and it runs stuff.
**Trask Stalnaker (Microsoft Corporation)** 34:31 Right, right.
**John Watson** 34:32 does… Totally. …gets our… gets secrets out of the container, or get our running container, or whatever, right? You can… I can imagine… If you can get shell on a CI machine, you can get stuff that we wouldn't want people to have.
I'm not sure how feasible that is today, but… you know, AI is clever, figure out something.
**Trask Stalnaker (Microsoft Corporation)** 34:55 But yeah, better to be safe. Yeah, I'll… I'll double check that, all the images are… getting updated.
**John Watson** 35:11 Cuckoo, that's all I had.
**Trask Stalnaker (Microsoft Corporation)** 35:15 Alright.
See y'all!
**Aditya Kousik** 35:18 Thank you, thank you.
**Robert Niedziela** 35:21 Bye. See you.
