SIG: Arrow SIG
Date: 2026-10-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Pierre Mariani 00:00:41 Good morning.
Nev Wylie 00:00:46 8.
Jake Dern 00:01:21 Hey, good morning, folks.
Aaron Marten 00:01:25 Good morning.
Nev Wylie 00:01:29 Morning.
Pierre Mariani 00:01:31 Yeah, it'll be mine.
Joshua MacDonald (Microsoft) 00:03:17 Good morning, everybody.
Jake Dern 00:03:22 Morning.
Joshua MacDonald (Microsoft) 00:03:23 My eyes are always blurry in the morning, so there you go. But I'm gonna stay off, ha.
Huh?
Good morning, again.
Nev Wylie 00:03:32 my screen.
Joshua MacDonald (Microsoft) 00:03:33 Yeah, it's… Yeah. Alright, here we go. I'm gonna find the notes. I put some things in it, And I will project… Right on.
So, hi Nev. You'll see that I put some of your PRs up to discuss, in the agenda. We don't have to take a lot of time, I just want to call out some things that I want others to know about.
And since there's probably, like, another minute while people arrive, I want to just… quickly look… I'm not sure we've been triaging, issues quite as fast as we'd like.
And… there are a bunch of new ones that… Ideally, we go through and look at and ask which ones need discussion. So, for all these reds.
or new ones, if you think it is needing discussion today, now would be a good time to mark it with needs discussion.
And I… I think this one's already done, I think this authenticated one might want it, Nev, for example.
Hear what that means.
Nev Wylie 00:04:53 Yeah, yeah, I agree.
Joshua MacDonald (Microsoft) 00:04:55 Wrong one. And then, Robbie should talk about this one, too.
Laurent 00:05:08 Yeah, I can talk about it, if indeed.
Joshua MacDonald (Microsoft) 00:05:10 Alright, we've got enough people now, and then let me… I'm just going back, this is mine, I don't need to talk about that, see me working on it, Basic auth extension, maybe not, Query engine should rely on par soil to retrieve source identifier. Okay, well… Okay, I think we've got enough to discuss anyway, so here we are. Good morning, everybody. Aaron's got his hand up. Hi, Aaron.
Aaron Marten 00:05:38 I just wanted to mention, you mentioned, folks should tag things. I think unless you're at the triager level or above, you can't edit labels yourself, so…
Joshua MacDonald (Microsoft) 00:05:47 Book care.
Aaron Marten 00:05:48 It's in the chat, and someone will mark it.
Joshua MacDonald (Microsoft) 00:05:50 Thank you. Yeah, we, we'll organize a little bit better on that, but thank you.
So, I guess with the normal, workflow, then, we, that's the first thing up, is these needs discussion.
And, I like to work backwards. I should say, here we go. There's an issue that Tom, filed before leaving the project, oops, and, basically there's a shutdown loss of logging, and this user named Black Sox came in and, Began working on it.
But I wasn't sure I liked… or I think we need to discuss the behavior, because there's a lot of complexity involved in solving this problem, and I… I… I was a little turned off by what I saw, and I wasn't sure what we really wanted. So I said it needs discussion, I wasn't sure the correct… it was even correct, so that's why I wanted to bring it up. If anyone else is familiar with this topic or has thoughts, I'd encourage you to join this discussion. That's really what I wanted, maybe not to discuss it here without context.
Laurent 00:07:08 It's the 4375, right?
Joshua MacDonald (Microsoft) 00:07:11 4375 is the PR, and then the issue was.
Laurent 00:07:16 Oh, that's the PR, okay.
Joshua MacDonald (Microsoft) 00:07:17 Yeah, the issue is 4224255, And I agree there's a problem, I'm pretty sure.
But I don't know what to do about it.
Laurent 00:07:28 Thank you.
Joshua MacDonald (Microsoft) 00:07:29 Okay, somehow I have a debug panel up, great.
This is, an ongoing issue that we've discussed a little bit, and it's gonna come up a little bit again, as we discuss. I listed some of Nev's PRs, and there is continuing to be more, kind of, I would call generic JSON infrastructure being built, and I just want to track it so that we can think about consolidating it and sharing it across implementations.
And Pierre has raised his hand. I know we talked a little bit about Pierre having an interest. Go ahead.
Pierre Mariani 00:08:04 Yeah, thank you, Josh. Yeah, I've been thinking and doing… so, since we talked about this, I think, 2 weeks ago, I've only dedicated around 5 hours to the project, but those 5 hours were dedicated to this issue in particular.
Happy to share what I have, and also, you know, let me know, you know, if time is becoming more pressing to get this done. I haven't had really that much time to work very quickly on it, so I'd be happy to let somebody else take it over, if it's important.
Other than that, I'm trying to keep the scope as small as possible.
you know, just, just move the logic in the code in one central location, use it in the two crates, or the… in the two exporters that are… that are prioritized in the issue. It's pretty straightforward, I think. It's mostly, API design that we need to review.
If I understand.
Joshua MacDonald (Microsoft) 00:09:07 Thank you, and I appreciate that. I've removed the needs discussion label. I don't think we need to bring this back unless there's something to talk about, and I appreciate it. I did put a link to this PR. We'll come across it again in this meeting. 4542 has a bit more of that stuff. We'll see it.
Pierre Mariani 00:09:23 Okay.
Joshua MacDonald (Microsoft) 00:09:24 Oh, wrong way. Okay, and then, Maybe I'll remove the needs discussion on this one, too. So… From NOAA, won't be with us today. This was filed during a PR. It's mostly documenting what we decided to do, and then, I think there are some PRs here. It's just not finished, so I think… is that right? Does anybody recall?
Laurent 00:09:51 Yeah, it's not finished.
Joshua MacDonald (Microsoft) 00:09:52 It's not finished. And then the other thing is to say we…
Laurent 00:09:54 It's an interesting work, so we… I think we should follow up on that.
Yes. Now when, I don't know yet, but
Joshua MacDonald (Microsoft) 00:10:05 Thank you. And then, for those of us who know, Noah's not gonna join the project after all, and so I've asked Gokan to pick up the PRs that he leaves behind with us, and I'm looking forward to that.
Sad about that, but we'll move on.
Oops, okay.
Docs build failing.
Albert.
Albert Lockett 00:10:30 Oh, yeah.
Joshua MacDonald (Microsoft) 00:10:30 Albert Pierre?
Albert Lockett 00:10:31 I noticed, when I was on the docs.rs website for many of our crates, we have this, error. It tells us the docs build failed, so that's, a bit, obnoxious for, for folks who want to use our crates and want to use docs.rs to figure out how to run them. So, this is a screenshot. Oh yeah, and then I guess, thanks, Pierre for putting, at SI check the validity.
Joshua MacDonald (Microsoft) 00:11:06 Oh.
Albert Lockett 00:11:06 Yeah, this is what we should do.
Yeah.
Did you do this?
Joshua MacDonald (Microsoft) 00:11:12 Thank you, Pierre.
I didn't realize we weren't testing, but I guess the testable examples and things aren't tested?
Thought we tested that.
But, very good.
Well, I think we can accept this one, and Look forward to a fix, now that we know what to look at.
Boop.
Oh man, back, back… too far, here we go.
The last one I wanted to talk about today, and we have Nev with us, is, So more than one issue here, and I've triaged it a little bit, so, I can kind of give you my quick summary that I discovered.
is that we're talking about, observed timestamps for telemetry, and there's two cases because logs have a special field for it. So in the data of a logs record, you can have an arrival observed timestamp.
And it's meant for collectors to fill in, so I think we want receivers to fill that in, unless we have a good reason not to.
And that would call for, in my opinion, some shared code. And then the rest of this issue is also talking about putting timestamps into context generally.
And I want to separate that a little bit, because we do have some timestamps and context already. We don't have a raw, like, user-settable U64 or 8-byte field, but we can talk about that. And so Drew and I were adding some notes here. Anything we want to discuss, maybe with Drew?
Drew Relmas 00:12:54 Yeah, my only thinking is… this feels like a very… I don't know if this needs to be a full-fledged processor. That's my… that was my gut feeling when I first read this. It felt like this is something that engine machinery might be able to give for us.
The… I was thinking about it mostly as a policies thing, because I'm familiar with, like, the telemetry policies, which gate you know, the telemetry interest bits. It feels maybe a little weird to have, like, signal-specific policies, but that was one option that I kind of thought about.
But in general, I… Yes, we… I actually did another… well, I say I, I used AI a little bit to go do some research about the Go Collector, and it seems like… There… it might be some behavior in some processors to fill in observed timestamp if it's not already set on the incoming data.
so it feels like something that we should also be able to support, but also I'd love to avoid needing, like, a reimplementation of everything… of this in every single receiver, right? So it should be something receivers get for free.
I guess… when we're talking about OTLP data coming in, it… we could expect, if it was an OTEL SDK that emitted the data, like, it'd probably already be… filled in, but I guess for non-OTLP data, we might want to fill it in ourselves. So, that was my thinking.
Joshua MacDonald (Microsoft) 00:14:39 I think the idea is that this won't be filled in by an SDK. If another collector has already touched it, they might have filled it in already. But this… this… you raise a really good point.
Drew Relmas 00:14:51 Oh, the SDK doesn't… the SDK doesn't,
Joshua MacDonald (Microsoft) 00:14:54 No, it's meant for the first agent that touches the data. Gotcha. Nev's hand. Let me just say one more. It's, you remind me that If we want a uniform and consistent behavior here, I think the sort of best definition for observed timestamp is on arrival, but we're going to have a situation where data is arriving, let's say as syslog data.
In that case, maybe observed timestamp equals timestamp.
No, syslogs have timestamps in them. So, the syslog receiver, with our codec changes, is going to want to mark a timestamp, but have nowhere to put it, and that would be a good, like.
semantic conventional field to put into context, to say that I know the arrival timestamp, the observed timestamp of this data, I just… it's not in the data right now, because it's not OTLP data yet, and so…
Drew Relmas 00:15:40 That's exactly what…
Joshua MacDonald (Microsoft) 00:15:41 context.
Drew Relmas 00:15:42 I see Wylie's hand is up, so I want to… er, sorry, Nev's. Nev. But I will say that's exactly what I was thinking here, where this could be tied into codec logic, and stored on context if we have data that doesn't have a spot for it, actually, in the field.
Joshua MacDonald (Microsoft) 00:16:00 Nev.
Nev Wylie 00:16:04 Yeah, so, just a little bit of context how I found this. So… Effectively, we have… a DF engine sending data to a DF engine, and it sends it as OTLP protobuf, and this field wasn't populated, so,
Joshua MacDonald (Microsoft) 00:16:23 If you have a DF engine sending to a DF engine, we want to use OTAP, ideally, to save us some money, but it will be the same, or it should be the same.
Nev Wylie 00:16:33 Yeah, I didn't find an OTAP out point, so effectively it's, We were sending Monmon data.
So, the internal logs we're sending to an inter… to one of these, so…
Laurent 00:16:47 Can we make sure that we are not observing a bug there?
Joshua MacDonald (Microsoft) 00:16:53 Does anyone know.
Laurent 00:16:54 In the field.
Joshua MacDonald (Microsoft) 00:16:54 implement observed Timestamp TimeUnix nano in the OTAP model?
Laurent 00:17:00 Yes, I think we, we, we do that. We should.
Joshua MacDonald (Microsoft) 00:17:04 Yeah.
Laurent 00:17:04 I think we do.
And… but…
Nev Wylie 00:17:07 So it is sitting on the…
Laurent 00:17:09 CRT, so… Something good.
Nev Wylie 00:17:13 Yeah, but the semantic invention is a case of, as Josh has already pointed out, it's the receiver that has to do it, so that's the point we need to capture, the timestamp.
And then it's just a case of, well, where do we stamp that timestamp onto?
the messages, right? So… I happened to implement this as a separate processor, just so I didn't have to touch the core for what I was doing to get the value, but… I know it's the wrong place, which is sort of why… I think I put some… some proposed things on here, and I'm happy to have the, you know, shared receiver. Like, one of my original implementations modified the call quite heavily to say, on the receiver, a bit like header capture, we just say, hey, capture the observed time step. If that was automatic, that would be great.
But there, then you've got the peculiarity of a log record has a top-level field for it, but metrics and traces don't.
Joshua MacDonald (Microsoft) 00:18:08 Yeah, that one.
Nev Wylie 00:18:08 We populate that, too.
Joshua MacDonald (Microsoft) 00:18:10 Alright, it's a little tricky, this issue, but I think we can agree on it, and I'm going to remove needs discussion. Those of us who care will come back to this.
Okay, we made it through Meetings discussion.
Anybody ready for another one? Here we go. Stale. This is always fun. Flash back to 6 months ago.
I tried to outlaw OpenSSL.
Drew Relmas 00:18:34 Actually, I think, funnily enough, Josh.
We saw this pop up in our internal component governance, as well, because it's coming through the Windows, Kafka.
Joshua MacDonald (Microsoft) 00:18:46 I just don't like Windows. I actually don't mean to ban it on Linux, it's native on Linux, but, like, on Windows, it's… it's… Just… remember the 8-minute build? Okay, so do you think this is done yet, or…
Drew Relmas 00:19:01 I mean, it's not done because the Windows already Kafka… Pulls it in, last I checked.
Joshua MacDonald (Microsoft) 00:19:09 This is, like, a perma issue, then, I'm just gonna say.
Anytime we get OpenSSL, get rid of it.
Hey, this one looks familiar.
This is actually gonna play right into some other conversation. So… I… I don't think we have an engine-wide policy on request size.
At this time, when I was working on this, there was a need to put in a hard limit, and we have it. There's a 256MB hard limit, which is what you get with a 4-byte placeholder invariance from Protobuff. So, there's a max here, but there's no way to configure that. I mentioned it's going to come up because Nev… one of Nev's PRs is aiming in this direction, at least as far as I can tell. I'm going to say this is not stale. Anybody want to talk about it?
And, looks like we have some anomalies in the benchmark. Jake, do you want to talk?
Yes.
Jake Dern 00:20:17 I need to refresh my memory.
Joshua MacDonald (Microsoft) 00:20:18 This is a really old, can we close it?
Jake Dern 00:20:20 Yeah, it's quite old. I think maybe we should just close it for now. I remember when we were doing a lot of these benchmarks, we were observing some things that we couldn't explain. I'm not convinced that we are still observing those things, so…
Joshua MacDonald (Microsoft) 00:20:34 Very good. And then, alright, so, I guess… Deciding? Oh man, this is the one that we're not very good at keeping up with. So, this is where I was asking early… at the beginning of the meeting, if anyone knows something that needs discussion, we should elevate it. But I think I… we shouldn't take the meeting time to go through these 20 red labels.
Drew Relmas 00:20:58 I thought the, GEO IP one was a little interesting.
Joshua MacDonald (Microsoft) 00:21:02 Sure, let's talk about it.
Nev, are you on?
Drew Relmas 00:21:05 Just saw it right before the meeting.
Nev Wylie 00:21:10 Yeah, so basically this is a processor that uses the MaxMind geo-IP library, so as long as the receivers drop in the appropriate client IP address, the MaxMind database effectively resolves that IP address to, lat long country, and state, I think it was? And it gives you more breakdown than what you can get from basic headers coming in from, like, Cloudflare or Azure CDN.
It does require… some additional foundations, which I think I put as related down the bottom, which is the HTTPS one that you've already tagged.
Joshua MacDonald (Microsoft) 00:21:48 Okay.
Nev Wylie 00:21:49 As well as I've created a hot reload, option, which I don't think I've created an issue for yet. I don't recall.
Because as part of the licensing, this does require that the database has to be refreshed on a regular basis, at least for the GeoLite, which is effectively a free version, but there's also a standard one that you pay for. Okay. So, yeah.
But yeah, basically, it's, it's, you know… it grabs all the extra content, and you can put it where you like, right? It populates into attributes. For what I have configured, I happen to put it into resource attributes as the message flows through, but… it's configurable, right? So…
Joshua MacDonald (Microsoft) 00:22:31 Oh, and…
Laurent 00:22:32 One question.
Nev Wylie 00:22:33 Visualization of where the data's coming from.
Joshua MacDonald (Microsoft) 00:22:37 They're.
Laurent 00:22:38 Okay, thank you. That's great, I'm just questioning the fact that, is it a processor?
It could be a processor, it could be a library that will be used by OPL, the transform processor.
depending on what and where, I mean, what we want to do with this IP address, and where we want to store it.
We already have a processing language.
Flexible enough to specify where this thing will go and what transformation you want to apply.
And how you want to configure the… because, if I remember well.
Using this library in the past, you can… Provide in different, level of, geography… precision.
you know, region, city, and so on. So, and what you want to store could be longitude, latitude, oral, city, or zip code, or many things. So, what I'm saying is.
why not using OPL and basically defining All those options directly from there, and then you have a way to Specify easily where to stop.
Joshua MacDonald (Microsoft) 00:23:57 I have a response to that, I want to hear from Drew.
Drew Relmas 00:24:00 Oh.
Okay, yeah, I… I do have a thought on this. It brings me to something else. Blanche isn't in this call to talk about it, but I can. As Laurent and Albert, you guys might be aware.
We recently added the plain text option to the Kafka receiver, with the intention of then using a transform processor downstream. And one of the use cases that, has just recently come to me is… taking the syslog Ceph parser code and using that as an OPL transform function, or, like, in the record set KQL processor. Because, essentially, the business thing we have is, say, a Cephlog embedded in a JSON payload.
And… In the Kafka receiver side, we configure that as plain text, so everything gets stored in the log body. Then you can imagine a transform processor downstream that parses JSON out, and then would call something like a user-defined function to… that is hooked up to the actual syslog Ceph parser code.
So, this is another example of, oh, should this be its own processor, or can we make it a function that the transform processor can leverage. So, I feel it's a different use case, but it's the same argument. Processor versus function and the, transform processor.
Laurent 00:25:34 Yeah. Does that make sense? Yeah, that makes sense totally for me, and I think that the main, what I think we should avoid Is reinventing the wheel for every processor that needs to do some manipulation on the data.
Because… like I said, if we need, so, example that you gave with, format X to format XY, and we extract, some information, and we put this information in some places, attribute, scope, resource.
metric, whatever. If we follow the processor approach, we will have to create configuration.
For each of those processors, with the risk of having divergence, inconsistencies.
And definitively, doing things again and again.
With some slight variation, and sometimes one processor will be able to store something somewhere with some transformation.
Not just the raw data, but some computation on it, and some time no.
when we have a processing language that needs to deal with that, and I think the rational way is just to extend it, and then we inherit automatically All the processing capabilities, the ability to store information in different places.
I think that that will be more rational. Does that mean that we could not have Sometimes, for example, we have attribute processor and transform processor.
Yeah, there is a little bit of history behind that, but, initially, the rationale was, oh, yes, for purely, attribute, renaming, for example, maybe it will be more efficient to have an attribute processor specific and dedicated than the generic transform processor. I think today, we can say that This difference in terms of performance is either non-existent or very, very slow, most of the time.
So… knowing everything I said before, I think it will be… the standard way to go should be, in my opinion, add a function or add some capability in OPL or KQL if we want.
And, and just use the processor approach.
For everything that is related to data transformation, data processing, as a second approach when we demonstrated that it's not efficient enough to use the first one.
Joshua MacDonald (Microsoft) 00:28:21 I have things to say. Nev, do you want to talk?
Nev Wylie 00:28:26 Yeah, I guess I'm just gonna drop in the config that I have for this today. So, effectively, there are semantic interventions of where these fields go, right? So there is already a case of, hey, this is the attribute names… sorry, it's in the chat, not in the the issue.
So, really, the configuration is, where do I fetch it from?
Rather than, where do I start, right? It is supposed to go into resource attributes.
As the client.geo fields, so… Like, another approach could be we have something that sits on the front end that just populates the context, and then we can have the attribute processor that goes and populates it with the fields instead of a separate processor, but we still need that thing that says, hey, I want to process the IP address.
the reason I didn't go down the OT, I keep… the OLP, the KQL path, is from performance, right?
When I did my tests on all this, I was throwing, like, a million requests.
At one instance, from 5 different browsers, which is, you know, where all this came from.
And burning a whole .2 of a CPU in a single Azure container app, right? So…
Laurent 00:29:42 Yeah, but we are not talking about the same thing, Nev. You are talking about KQL?
And we are talking about OPL. And OPL is, the… the OTAP native, Performant option, in my opinion.
Nev Wylie 00:29:57 Okay.
Joshua MacDonald (Microsoft) 00:29:58 Now, now, go ahead, Nev.
Nev Wylie 00:30:02 Sorry, so I haven't looked at OPL, so I can't comment on perf of that, so I'm good.
Joshua MacDonald (Microsoft) 00:30:07 So I'll just add that there may be… I suspect that there is a performance difference there, but I also don't think that we should dwell on it, because the pattern we have right now is, I think.
natural, where we have this attribute processor that's, like, a low-level way to configure movement between contexts and attributes, for example, and then we have a high-level way to do that with query language. But I think what I'm hearing from most of us is that We're… we're trying to separate the… configuration of what gets mapped out of an IP address, into Well, I'm gonna… I'm gonna say context, and then we also have a separate project of what to… how to move data from context into the… into the… values from the context into the data, which is the sum of your problem, I think. So, So, we can imagine a, I can at least imagine thinking of an extension that's just sort of like a context deriver. I could also imagine this being part of the network info. Like, we have a context called network info, like, logically speaking. There's a domain from which you get network info, and that's been used initially just for source IP address, but Network info is a more generic term, and this could be phrased or, I think, expressed as a mapping from network info to more network info, or from network info to Bags of key value information that are part of the context.
And then you can imagine having, configuration that's context-specific or networks… network info-specific that says, I'm gonna… I'm gonna materialize a context, it's gonna have some network info, like source IP, and then I have these derivatives that will derive from source IP more context fields.
And that could be phrased in our current architecture. We have these composite context entries, and we have one type of composite entry that's a transport header map. So if you… this is saying, if the transport header matches, I'm going to accept this… this composite. We could also imagine deriving things in those… those, entries. So you could say, I have a composite entry, it's going to get the source network IP, and then I'm going to produce, using a function call.
some secondary context that came from the source IP, and then you could imagine passing that into the transform processor. There's a lot of ways to solve this problem, and I'm going to turn it over to Laurent.
Laurent 00:32:40 Yeah, the… it was just a reaction to what's said, Nev There is some semantic convention and so on, so… I think we want to build a very flexible system here. Some people will comply with semantic conventions, some not.
it's not only about client IP address, you could imagine scenarios that are not browser-based scenarios, where you have a source-destination address.
You can't want to do some computation on those, longitude-latitude translation that you get from, this, GOIP library, because maybe what you want to get is distance, it's not, and not, a location. So, what I'm saying is, basically.
If we really want to build, something that will be very flexible for different use cases.
At some point, you need a way to express Expressions to express transformation.
And I think OPL, and for some other people, KQL, I think that's the solution we are trying to promote.
And, yeah, and for the other reason I mentioned before, If we don't want to see a jungle of processors with different variation on how to express those extraction or destination and processing.
Which is, in my opinion, not the right way to go. I think we should prefer the… The transform processor approach.
Joshua MacDonald (Microsoft) 00:34:21 I could… I could also imagine that someone has an application where, in their telemetry, they are observing other people's IP addresses, and that's first-class data in their log record or in their… in their trace. So now you've got… it's not the source of the network… of the telemetry itself, it's actual telemetry data that you want to expand into
Nev Wylie 00:34:42 And decorate, yeah.
Joshua MacDonald (Microsoft) 00:34:43 Geo details on the collection path for reasons.
I think we've talked about this. There's a lot of options. I think we should think about it some more. I think I see several approaches. I also want to link now… I think we're going to head back to the agenda in a minute.
I did see these two issues. I know they're… I see how they're both related, and you have mentioned them. Let's come back to them in the natural order of things.
So, Now, we're back here, and I want to run through my agenda. We'll come back to some of those PRs that we just discussed. So, we've already talked about, the log timestamp issue. Move on from that.
This one, I have, I don't want to… this is not meant as a sort of, criticism, Nev. I wanted to start a… us to start paying attention to pieces of code that might be shareable. I also have a side, I'm… Thank you, you've already resolved my comments. I'm… there's certain words that are screaming to me, I'm an AI-authored piece of text, and this word bounded is, like, on the top of my list. I… I don't think anyone uses that word in normal text except AIs. But, so I couldn't quite… The PR description is very… very hard to interpret, Nev, and I… when I dug in, I could see what it was doing. It seems to be… Well, this first piece of code, you've renamed it for me, and I… and you've moved it into common configuration, so you've done what I wanted. I just wanted others to see it. Here we have some limits that are data-specific, that are endpoint-specific, like, this exporter needs particular size limits enforced, and this is connected with that OTLP limits.
issue that I gave from 6 months ago. So, just wanted to call it out, that this… this has the appearance of a common way to limit data, and it belongs in policies somewhere, and I haven't seen the work since yesterday.
Any comments on that topic?
Laurent 00:36:59 I'm not sure to follow the… this data limit… configure, or limit configure.
Is it specific to, the, the exporter, that, on which, Nev is working, or is it generic? Because if it's specific, that has nothing to do with… The coffee crates.
Joshua MacDonald (Microsoft) 00:37:21 Well, I'm… I'm looking at… a policy that's, like, there… the number of attributes, the number of bytes, the number of… I don't know what… what work is, Nev. We gotta… we gotta figure out if this is standard or not, but, like.
I mean… I wonder, Nev, if we can take maximum inspected JSON nodes and turn that into something more like… that's more of a generic term as well. I'd like to hear what others think.
Laurent 00:37:49 But could we, I think what we… what we used to ask before for such a change or additional set of concepts and so on.
at the minimum, to have a GitHub issue describing what we want to achieve, just to make sure that we are aligned on the approach.
Joshua MacDonald (Microsoft) 00:38:08 Yeah.
Laurent 00:38:08 It could be a policy, like you said, it could be a specific configuration. I don't know what it is exactly, but, Right. If we want to minimize the work of, of Nev in that case, contributor, and avoid back and forth, I think we should agree on what we want to add, especially if it's generic, and at the framework, I mean, the engine level.
Joshua MacDonald (Microsoft) 00:38:36 And I would like to see… this is connecting with the issue about JSON, is that I think we should be able to make limits before we turn things into JSON, and then this is, like, JSON infrastructure here.
Which I would keep separate as well. And then, I called this out, Nev. I think we should not be reading config here, but, like, you should be past a configuration object somewhere. So this is mixing up a bunch of stuff that I want to see pulled apart.
And I imagine you have a reason for doing it, but I don't quite see it here.
Why you would be rereading a config file, for example, because most of the nodes are handed their own config.
Laurent 00:39:19 Yeah, it's just not following the… it's not following the definitively, not the…
Joshua MacDonald (Microsoft) 00:39:23 So this seems quite right.
And now I've set it.
So we can sort this out. Aside from… because from the name, I couldn't quite tell what else we're doing. It seems to be a little bit of a grab bag, so I'm gonna turn that back to you, Nev. It looks… I mean, I can see why you're doing all this stuff, so let's just figure it out.
I'll pause for now and see if anyone wants to speak.
Pierre Mariani 00:39:46 Just a quick question. Oh, sorry, now if you have your hand up.
Joshua MacDonald (Microsoft) 00:39:50 Oh, yeah.
Nev Wylie 00:39:51 Just to answer the question, the reason it's re-reading is related to that other issue about effective monitoring. The JSON receiver, sort of answer to Laurentz, this is actually for the receiver, not for the exporter, the JSON receiver has the ability to go and refresh its config.
Using this hot reload options, so that we could have the definition of how we do the mapping from the JSON into semantic conventions, and we can just update it without requiring everyone to go and, effectively reinstall the new version or bounce their system. So, that's it.
Laurent 00:40:27 Yeah, but it's not something new. I mean, we have other, for example, the certification, the CERT rotation.
It's automatically refreshed for some receiver.
And it's a specific configuration of this. It's not something that is visible by the engine, but something that is visible by this specific Component or receiver.
So the… I'm really questioning the fact that everything there is in the config crate.
When it's… when… when… based on your description, it looks like something specific to your receiver.
Joshua MacDonald (Microsoft) 00:41:04 To be fair, I asked him to move it into config, because it didn't look like it belonged in the receiver, but I think we still need to figure.
Laurent 00:41:10 Yeah, I think we should start with a description of what you want to achieve in order for us to guide you and move in the right direction. I think that's… Don't hesitate to ping us, even on Slack.
I mean, you are doing a lot of stuff, so that's great, and I don't want to slow you down, but I don't want to be in a position where I have to say no.
Just because it's not aligned with the principle of the project.
Joshua MacDonald (Microsoft) 00:41:41 And we're working on this, and I'm gonna help Nev. I accept responsibility here, so thank you. I… but just to be clear, we do have a mechanism for getting hot reconfigged, like, during operation, and the receiver will get a message saying, you have new configuration.
Or the engine will restart because the configuration requires it.
And that is in some code called Live Control, which is, one of our dark arts. We have… I'm always looking for more people to understand our Live Control code. Pierre?
Any comments?
Pierre Mariani 00:42:22 Yeah, sorry, I lost my cursor.
Do we want to enforce that every single JSON export is limited in the number of bytes serialized?
And for the exporters that are not doing that today, what is the standard of the project? Do we want to make a breaking change and implement those limits right away, or is there some… Some integration to test, or some… You know, some iterative way to implement that.
Laurent 00:42:58 I think we're not clear.
Joshua MacDonald (Microsoft) 00:43:00 On what limits?
Laurent 00:43:01 For me, it's, it's, The broader question, which is, what are the… Place in the project where we have some flexibility, and some other place where we have already external dependencies, and we… We didn't commit publicly with, with any kind of configuration or API versioning that is stable.
Pierre Mariani 00:43:30 So…
Laurent 00:43:31 Technically, it means that we… we should be able to make some… some times when it's very justified, important changes, but at the same time.
We know for a fact that, either Microsoft or i5 are already using this stuff in production.
So, we have to be smart and, and look at… what, What needs a real change, and if there is a dependency with the main manteller of this project, we need to coordinate and see how that could be done without risk.
That would be my answer. Personally, I'm never, until we declare the project version 1.0, Opposed to a change, if it's really, well thought, shared across different mentors and so on.
And there is a real need for it, it's just not artificial or a… Nicer, but it's really more effective and more, less error-prone, or this kind of stuff, more secure.
But, yeah, so it's, more, A discussion to have and a decision for each item, not a general rule for now.
Pierre Mariani 00:44:57 Maybe… maybe the right… way of acting here is to look at the history of the exporter, you know, I would be considering changing, and see who might be interested, make enough, you know, enough noise so that those people get a chance to, you know, to hear that there could be a new limit coming, and give them a chance to comment or stop for it. So take the time.
Research who has been interested in participating in those exporters, and And make sure that they get a good opportunity to pitch in.
Joshua MacDonald (Microsoft) 00:45:36 I can say that there is definitely a whole topic here, and it's not an easy one. In the Go Collector, we've been working on batching for a very long time, and this connects with batching, because you usually find yourself trying to batch until it's too big, and then, like, how… what do you mean when it's too big?
And in the Go Collector.
there… even today, there's not an easy way to configure more than one limit. Like, I have a limit on bytes, and I have a limit on metric point count, and I don't want to ever create a batch with more than this many points or this many bytes.
And that's very hard to do, and then… And then in this world of JSON, what we're typically doing is saying, I'm going to make a batch, I'm going to put row by row into this batch, and each time I add to that batch, I'm going to increase the buffer until it hits something, and then I'm going to compress it.
And then I'm going to make sure it's not too large, and unfortunately, we have way too many constraints. I wish that there weren't a, like, hard megabyte limit on requests, because it's very hard to batch when you have such limits.
And… but… but in general, I think we do have, like, a… all exporters are going to, at some level, have a limit, and it's not usually just bytes, it's sometimes more than just that, so… and that's what I'm seeing with Nev's PR. It's like node count, or how many… how many, like, objects nested are there? How many points, how many attributes, all those things are reasonable limits.
And I think we want to implement them in the real data model, not, like, convert them to JSON and then implement limits. But I think we should just take this offline and keep thinking about it.
Laurent 00:47:13 Did you see that, Google Doc, does not agree with the… Hotel Air Doc.
Joshua MacDonald (Microsoft) 00:47:18 Sorry, can't spell that one. So this is the last in the list of me bringing up Nev. Sorry to rake you over the coals here, Nev, but this is all good, and I want to see it move, so we're gonna… we're just gonna keep going. This here is another one, this, I think you've already made the changes I asked for, but this is kind of connected with that starting conversation about geo, attribute labeling, is that, we… the context mechanism that I've been working on with MacSat is coming together. It's not optimized yet, it's not coherent completely yet, but it's coming, and then we can now pull out transport headers and authorized identity fields, and a few others we've defined, randomness and constants and so on.
And this is just adding a way to do processor to do that. And again, we're in that, like, this is the low-level, simple attribute processor where you're not using OPL or KQL. And honestly, I don't think I had any real remaining issues here. Mainly, I want to call this one out. This, Nev's already done it. I want to see us standardize how you interact with context, and the original proposal was, not one I liked because there were separate arms of a configuration, one for transport headers and one for named composite entries. And what I'm proposing is that we start unifying on the way you select from context.
And, currently the… the most the precedent in our code looks like this. You'd have a typed selector. Your type tells you which domain you're pulling the context from, and then you give a list of names.
there are ways we could refine this, there are ways we could make syntactic sugar so that there's less to type, but that's mainly what I wanted to focus on, is that we start sort of consolidating and having only one way of doing things. And otherwise, I'm very supportive of this. Does anyone want to talk about it?
Laurent 00:49:17 I think it's… it's okay, but I mean, for me, similarly to the… Conversation we had with, Transform processor, which is a generic way to manipulate information, filter out the information, so on.
For the, for the readers, for the attribute processor. So let's say you want to do some… You have errors, and you want to create an attribute from it.
But it's not just a simple copy, it's some transformation, some function you want to apply.
We would end up with… a variation of a function existing in OPL inside the attribute processor. I'm not saying that it's today the case.
But, I can reasonably imagine that someone is coming and saying, oh, we are already extracting attributes, transforming them into attributes, sorry, extracting headers, transforming them into attributes.
What about adding, a hash function, a CONCAT in a CONCAT function, and so on?
into the SAV processor. When we already have everything we need in the transform processor, in my opinion, the right way to go is having An integration with the context.
Error extraction and so on inside the transform processor, and then we have everything we need, all the functions that already exist, and so on.
So that's the same problem.
Joshua MacDonald (Microsoft) 00:50:49 Yes.
I'm also seeing the similarly an alternate solution, which is to say we could imagine like, with hashing, that's another one of those context entries where I could imagine you've you configure… currently, we have a randomness value that's UUID7, but what if I wanted a randomness value that was the hash of a particular attribute, or a hash of something? Then I could… it almost feels like… but I still feel like we're moving towards both answers, where there might be a simple attribute processor, and it might have access to, like, basic Context manipulation, but… or, like, you can pull out of field from the context, or maybe you can call a static function, and maybe there's a registry of functions that are used both in OPL and in the attribute processor, but at some point, complexity becomes the problem, and you should fall over to a language rather than You know, this low-level facility.
Laurent 00:51:43 Yeah, I think for me, the limit is if we start to define subtle language into the attribute processor, we are not in the right place.
Joshua MacDonald (Microsoft) 00:51:54 Right. I think we're… I think I agree.
Okay.
Nev Wylie 00:52:00 I just jump in there. Go ahead. So I probably should have, updated the PR, because it is… well, it should be now a case of that authority host is now up in the propagation header, and the attribute processor really grew, what Josh was talking about, where it fetches the content from. There's no transformation anymore in this PR. In iteration 1, there was, but iteration 2, it is just a case of, hey, go grab the named… the first named thing from here and drop it in, so… which I think is…
Joshua MacDonald (Microsoft) 00:52:31 I'll review it again.
Nev Wylie 00:52:32 What we want to?
Joshua MacDonald (Microsoft) 00:52:33 No, thank you.
Nev Wylie 00:52:34 Cool.
Joshua MacDonald (Microsoft) 00:52:35 We're close to the, like, end of the meeting and the agenda. I wanted to… cover these real quick. So this is about reloading your geo database. I think we want to call this config reload.
sounds like we might need to extend config reload to, like, I have a file reference in my config, and it needs to be expanded by reading the file, and then you need to get an event saying, please reread this file, or something like that.
Does that sound about, like, what you're looking for?
Nev Wylie 00:53:07 Yeah, I've been able to put it the other way around. So, effectively, the… the processor, receiver, whatever, says, hey, I want to go monitor this thing, whether it's a, you know, and it's effectively reusing the config providers to go fetch the content.
But that content could be config, or it could be in the option I've got down the bottom here, the geodatabase, right? So, not… you know, the config providers can't process the… the MMDB, right? So, it's… it's not YAML, it's not readable by anything other than the MaxMind.
crazy.
Joshua MacDonald (Microsoft) 00:53:41 I see. So I'm hearing an issue about, about… config providers, like, you would like to load config from a control plane, maybe, as well as one about having resources that are configured which still have, like, live reload outside of the system. Like, a file is dropped by the operating system.
Nev Wylie 00:54:06 Yep, yeah, file dropped by the operating system, or it reaches out directly. Either way, which is why I called this a helper, rather than, sort of built in. So, but again, it's, like, whichever works. Like, I don't know the full code base, and I…
Joshua MacDonald (Microsoft) 00:54:19 Yeah. We're just tracking all these issues, Nev, no worries. I just, since we're… let's talk about this for a minute, This sounds… sounds scary. Why do we want unauthenticated HTTPS?
Oh, you're trying to reload configuration. Okay, so this… in the Go Collector, there's a whole plugin system for configuration providers, where you have a YAML provider, and then you have an HTTPS provider, you have a JSON provider, and there are two more, at least. I'm hearing that's what you're looking for, but I don't know why I don't…
Laurent 00:54:52 We, we have the SIMC, we already suppose… Because I hate to…
Nev Wylie 00:54:59 P.
Laurent 00:55:00 Yeah, okay. And, okay, that's just extending the existing support, the existing system to support HTTPS. I was not aware that we didn't support HTTPS, okay.
Joshua MacDonald (Microsoft) 00:55:12 Got it.
Nev Wylie 00:55:12 I think there's a to-do in there to say, support authenticated HTTPS, but there is a case of if you're hosting it up on a CDN which is public, then you don't want… it doesn't need to be authenticated.
Laurent 00:55:25 What do you need?
Nev Wylie 00:55:26 for some authentication in the future, but this is specifically just saying, hey, allow HTTPS as well as HTTP on the existing one.
Joshua MacDonald (Microsoft) 00:55:33 Okay.
Laurent 00:55:34 Okay.
Joshua MacDonald (Microsoft) 00:55:36 Very good. Well, this is the advantage of writing up in the notes before everybody else. I put my own two RFCs up here. I want to briefly advertise them, because they're waiting for reviews.
So, RFC 6 is the second half of my work on context. This is talking about, transferring context across topic boundaries, transferring context through durable buffer, and a few more tightenings of the model that, I'm, proposing and, happy with, so… Looking for reviews on 6, RFC 7 is one that's new.
We realized this is something we're gonna need to… implement our overall approach to bounded memory. There it is, that word.
And I am… I wrote this up because I wanted to see it start moving, but I… I don't plan on working on it myself. I'm fishing around for people within my own team to look… to work on this, and I just wanted to share… hopefully this design can get reviewed, and we're gonna look for someone to work on it.
The proposal is to start with Linux cgroups, because it's very well… it supports our model very well.
Don't talk about Windows yet. That's a future project. Windows makes it a little tricky to do hierarchy. Please, Laurent.
Laurent 00:57:01 Yeah, I started to read the 007, sorry. I like it, personally. I have some comments. I will take the time today to… give you the comments, but in general, I really like it. The fact that you are using the policy approach and the hierarchical Mapping with the group, pipelines, makes total sense for me.
The context propagation, I read, probably a previous RFC. I will take also time to read this one.
Joshua MacDonald (Microsoft) 00:57:35 Thank you. Aaron put some really good questions on the SIG RFC6, which I haven't quite answered, just sort of, like, open-ended questions. I encourage us all to think about it. Like, when it comes to durable storage, there's a lot of ways to think about what we're doing, and well, anyway, interesting topic there.
Well, we have a few minutes left, Jake.
You're the last one here on the agenda, and let's do it.
Jake Dern 00:58:00 Sure. I'll give the briefest introduction. So, you know, we have a lot of things in the engine today, you know, advice, opinions, guidance, whatever you want to call it, sort of about how you should construct your configuration. Some of that stuff… We omit, warnings, today, during config validation or in other places, like, you can think of stuff like, if the batch processor is configured in such a way that it's just forwarding all the data and not doing any batching.
we emit a warning for that. There's also this, like, guidance that we often write in READMEs and in other places, and we say stuff like, well, you shouldn't… Generally placed this component before or after this other one, and a variety of kind of other things.
This PR is kind of exploring, a way to, you know, for the engine to be running some of these checks, automatically, and in kind of a standard way.
And it's also presenting some ideas about, you know, policies and configuration, and then how the engine should generally sort of react when a lint comes up. So there's a fairly big design space here, I think.
This seeks to do something relatively simple, that starts experimenting in a lot of these, these areas.
And I think there's many, many possibilities for extending this in the future. So, yeah, the RFC, it describes sort of some general machinery, how you can register custom links, how those links run.
It describes some very basic things in terms of links having categories and configuring what you want the engine to do when those lints are triggered. If you want to suppress those links, if you want to emit a warning, or if you want to even, like, block the creation of a pipeline.
There's stuff like that in there. So, yeah, give it a read. I'm curious to hear what people think.
Laurent 00:59:52 Nice.
Drew Relmas 00:59:55 One thing I just connected in my head to the, permissions. There's a proposal about permit… permissions, right?
Like, what, what pipelines are allowed to do what sorts of things to data, right? I mean, I guess it's not directly related, but it just scratched an itch when I heard you talk about this, but it all makes sense to me.
Jake Dern 01:00:20 Yeah, definitely.
Yeah, so there's… I could talk a lot about this topic, but I think we're at time, so I'll just leave it there, and I'll read y'all's comments.
Joshua MacDonald (Microsoft) 01:00:31 I've been adding a lint in the Go Collector, I'm gonna give you a link to it.
Double batching.
Very good. I feel like, promoting my PR for structured logging, maybe that can be helpful for your links. You want to put some nice, detailed, structured values in your, in your logs.
leave it at that. Thank you, Jake.
We did it again, thank you all. We'll see you Tuesday, next week.
And anyone who wants to talk about any of these topics, especially you, Nev, let's talk on… offline. Thank you.
Cheers.
Drew Relmas 01:01:09 So I…
Laurent 01:01:09 Bye.
Jake Dern 01:01:10 Yep. Thanks, everybody. Bye.
Nev Wylie 01:01:12 Yep, cheers.
