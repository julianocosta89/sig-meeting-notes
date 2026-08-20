SIG: OpAMP
Date: 2026-08-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Dakota Paasman** 01:07 Hello.
**Douglas Camata** 01:11 Hello?
**Dakota Paasman** 01:16 How are you all doing?
**Evan Bradley** 01:31 Hi, everyone.
**Dakota Paasman** 01:34 Evan.
**Evan Bradley** 02:56 I think we're good to kick it off, 3 minutes past the hour.
Mikola, it looks like you have the first two.
**Mikołaj Świątek** 03:06 Yeah, I should probably say hello, I believe this is my first time at this SIG meeting, so if we haven't met with her.
Hello, name is Mikhai, I work at Elastic, I'm actually an auto operator maintainer, plus a code owner of some, like, bits and bobs over contribut, collector, contribute.
and core. Here, I'm mostly wearing my elastic hat, because we're adopting OpAMP internally, and there's, like, some things I wanted to ask, talk about, see if there's any non-obvious blockers, or… And, the first, the first one is basically.
Unix domain sockets and name types. There's an issue.
open already for, I think, a few weeks, which is asking for this, just the ability to… Set, essentially to pass a custom listener.
into the OpAMP server and client. I wanted to ask if there's, like, some obstruction to it.
I'm not actually sure of what the contributor who filed that…
**Dakota Paasman** 04:14 That is, sexually me.
**Mikołaj Świątek** 04:17 Okay, great.
**Dakota Paasman** 04:18 Yeah, yeah, I can talk about that.
Basically, yes, there… there is no controversy. I discussed it in a SIG.
A few weeks ago, and it's something we all agreed on. I just… the last few weeks, have not had priority to work on it.
I actually just started looking at it again today.
**Mikołaj Świątek** 04:43 Hope for two.
**Dakota Paasman** 04:44 So… Between today, and I have half a day tomorrow.
Then I'm out the rest of the week, and then next week, for sure, I should have some movement and PRs open for this.
**Mikołaj Świątek** 04:57 Alright, if you're… if you're… if you feel like you don't have, you know, space, then I could go and pick it up as well. You could see me.
**Dakota Paasman** 05:07 Okay.
**Mikołaj Świątek** 05:08 pretty straightforward, so we can… we can talk on SOC.
Yeah.
**Dakota Paasman** 05:13 I have… I have, an implementation for it in my own fork, just a matter of opening issues and opening the PRs. The one thing I did not implement was the Windows Named Pipes part of it.
**Mikołaj Świątek** 05:30 Does it need anything special for that, for that?
**Dakota Paasman** 05:34 No, my primary use case was just Unix domain sockets, so I just haven't touched the Windows use case yet.
So once I get… PR has opened up. If you want… if you're interested in the Windows part of it, happy to tag-team that with you.
**Mikołaj Świątek** 05:53 Well, if the… if the interface really just takes, like, a listener, or, like, some listener factory, then that should be enough, because you can take, like, a library like Go WinIO, which is… the collector already uses for the same thing, collector core.
and you can generate a listener from, like, Windows, Cisco, whatever. If you put up a PR for it, I can look at it and actually test whether actually doing it works end-to-end. But this is generally kind of uncontroversial, like, named flagship for the… a boring piece of technology, essentially. Like, lots and lots of different, similar applications use this, across, many OpenStrash projects, and it works just fine.
**Dakota Paasman** 06:46 Cool. Yeah, I'll, I'll let you know when I get those PRs up.
**Mikołaj Świątek** 06:53 Okay, cool. So that answers that question. The other question, I have a feeling this one might be a little bit controversial, but I'm gonna ask it anyway. It's been a while since there was a release of OpAMP Go.
Is there a reason for that?
**Evan Bradley** 07:10 I can't answer that. I know Tigrin is on, vacation right now?
Andy did reach out to me about, cutting a new… SPAC release, but I don't know if that will… necessitate a Go client release.
**Mikołaj Świątek** 07:30 It doesn't look like it, because there's already been, like, I think 3 spec releases, one of which actually contains New Proto.
And it hasn't turned into an OpAMGO release. That's actually the reason I'm asking, it's because one of the recent spec releases has a new field in, like, the component hell struct, and I want to wire that up in the extension.
I can't until the library is out.
I was, I wanted to know whether there's, like, some… infrastructural holdup, or is it, like, simply, like, nobody… there's no release cadence, and just nobody has done it thus far?
**Evan Bradley** 08:10 It's more the second one, yeah. There's not a set release cadence, so… it just hasn't been released. I… don't normally do OpAMPO releases, but, I'll… see to it if one isn't cut, shortly after Tigran's back.
**Mikołaj Świątek** 08:29 Thanks.
If I can help out with it, I have the latitude.
I might regret this promise later, but…
**Evan Bradley** 08:39 Noted.
**Stanley Liu** 08:54 I think the next one is mine, but I saw that Andy is not here today, and I've been chasing him for review, so I don't think I have much to discuss today. If anyone has context, or, like, is meeting with Andy soon.
I think he said he's really busy, so I'll probably just follow up with him offline, but just waiting for review on the, message attestation prototype.
Yeah, that's… that's all. So, I'll just follow up with him offline.
**Douglas Camata** 09:36 Also, I'll go next, I put up this point there because it's a bit related to… to some of these, health stuff that Mikola mentioned, and also think it's an important issue.
that we have to look into. It has, has a PR already, which is great.
But basically, something… Since when we started reporting… Health… From the memory limiter, it created an interesting situation where If you configure your memory limiter to check memory every second, It will report either Right, like, healthy or unhealthy every second.
Which means… the OpAMP extension will, every second, Push a new message.
To the… to the backend.
at least via HTTP. For sure, I know that's how it is behaving, because that's what, we use at my employer.
Might be the same for, WebSockets as well.
And, well, this can… this can bring down your, backend if you don't have a nice rate limiting, in front of it, that is working well per agent.
Which is the kind of trouble that we had.
and I think… I think there is… There is a relation here to the… to the work that Mikola mentioned, because I imagine, I imagine that, for example, if a new… if health of a certain component Changed, you know, in the sense that Just an attribute there changed, but the… the… Actual health is the same, healthy or unhealthy.
I wonder how we should handle that. I guess it should… it should… that attribute should go up to the backend, right? But, I think that we will have a general… A more generic discussion of… How we compare the… the tree of component health, and whether… We wait until the next.
interval, that the agent will talk to the backend to push the new health.
Or whether we push it immediately.
Interestingly, I checked, I checked the supervisor code, And if you'll have… The collector, behind the supervisor, the supervisor will already take care of, Kind of buffering, right, and aggregating those… those health updates, and… It will only push them when it finally reports to the backend.
But, yeah, I just wanted to bring some attention to this. We might have to rework a bit.
That… that part of the code.
And I think, from my review on the PR, I think right now we… We might also have… Some kind of issue, like, if one component reports unhealthy.
We will push that, and then if another component becomes unhealthy, a different one.
The backend will only know After the previous component became healthy, kind of depending on where in the tree it is, so… I think… I think we might need some bigger refactor there at some point.
not… not urgently, I think urgently we just need but not… push, health… Health updates every time.
Any component changes health if… You know, the… Even though the component is reporting healthy, it was already healthy, so we don't need to push healthy again to the backend.
Yeah, but then there's gonna be some interaction with those attributes later.
Duh.
Yes, Mikolaj, I'm talking too much, sorry.
**Mikołaj Świątek** 14:17 So, like, conceptually, what actually happened and caused this was that we removed the duplication in the collector core status reporting framework itself, and the reason was literally just us. It's because you can emit events with the same status, but with different attributes.
And in that case, it should be omitted.
At the time, we basically said that we don't know if this really matters downstream very much. Like, I don't think we… we were thinking about the OpAMP extension, but we did think about the health check extension, but then the health check extension.
The half-check acclimation is, like, a pool thing rather than a push thing, so it's just, like, whenever it gets an update, it just updates the state it holds, and whenever a… Consumer wants it, they pull it in at their own, Cadence, so it's not a problem in there that you emit, like, the same status multiple times, potentially.
It is a problem here if we're, if we, if we're coupling The status events coming in to what we're pushing out, like, one-to-one.
Pretty much, is what I'm getting, and that probably shouldn't be the case. I would also, personally, I would accept… deduplicating it in the core framework if we, like, looked at the whole identity of the event, essentially, but I kind of get the feeling that the core framework should be simple in this respect. Like, it shouldn't do clever things, and it's the consumers who should do things like, update cadence per their use case. Like, the health check extension doesn't care, because it just holds a single view of what it has.
Understood.
**Douglas Camata** 16:04 100% agree with you.
**Mikołaj Świątek** 16:06 the OpAP extension does have to care, because we're pushing, right? So we do have to actually think about when we're pushing and at what cadence, and it's just, like, a question at this point of… Is this… Is this a fixed thing, where we just say we push at most once per 5 seconds, you know, and debounce internally, or do we check the change, and only push if whatever we have has changed versus what we pushed last time?
That kind of makes sense to me, but I also haven't looked at this code much, and I'm looking at this PR right now, and I don't understand it, so… I shouldn't have too much of an opinion.
**Douglas Camata** 16:51 Yeah, yeah, yeah, there… yeah, on the… on the… on the PR there, it looks… it looks weird, but basically what is being done is… is, checking… if the status is the same, or if there is an error, if the error is the same. But I agree with you, I don't think… I don't think this should be done inside Collector Core, I think this kind of the duplication.
And, potential, like, periodization of the updates should be inside the extension, the OpAMP extension.
Yes, Daniel?
**Daniel Bright** 17:30 Hey, just wanted to introduce myself. I'm Daniel Bright. I'm over here at Expedia Group, in San Jose. Yeah, I think, this… you're talking about the… the, check that I brought up in Slack, I think, a week or so ago, if I'm not mistaken. So, it's good to be here and, just kind of listen to the discussion. I'm happy to kind of go whatever direction.
you guys are leaning towards, and do some testing internally. We're about to roll out, I would say around 30,000 nodes. That's just the start, so that's gonna be a good test.
So…
**Douglas Camata** 18:08 Yeah, yeah, and probably whatever backend you decided to go with, they will be… they will be happy if you don't ping them every second from every agent.
**Daniel Bright** 18:20 Yeah, for sure, for sure. Well, we control that too, that's the beauty of it. We're building the whole solution end-to-end, so we, we get to be very prescriptive in how we decide this, but yeah. So, happy to give that PR a test drive.
you know,
**Douglas Camata** 18:41 That will be great.
**Daniel Bright** 18:41 Doug, yeah.
**Douglas Camata** 18:43 That would be great. I just… I just have one question.
Maybe, maybe Evan will have a good opinion on this.
Will any of you think that this, and this… This decision on whether The update should be pushed… should be pushed.
should live in the extension directly, or even in the OpAMPGO library? Because when I was looking into this, I was, like, thinking… well, I know the extension is used in the library.
And I know that the library HUS as methods, right, that will just change internal state Until a certain time.
It decides to push it out to the backend.
So I wonder… You know, if we might want to… To do this kind of diffing of the tree, and, you know, decision on whether this change in the state of the health.
Does it require that we push a message now instead of when we were supposed to, based on the interval that it talks to the backend on, or Or maybe we should just wait?
And, you know, even when health changes, we just wait until the next plant Push to the backend.
To send it.
**Evan Bradley** 20:20 I think we should probably do this in the extension. I'm a little nervous about making the library opinionated like that.
Also, we don't really control when the, like, the current message is flushed and sent back to the server, so if we wanted to do more, kind of conservative rate limiting, you know, like only 1 or 5 or whatever seconds, we would want that configuration option to be available in the extension.
That's just my take, though.
**Douglas Camata** 20:49 Yeah, because I also think the library exposes Public method for you to, like, Force a flush, right?
**Evan Bradley** 20:57 Right. But I don't think you have, like, an ability to say, you know, wait this period of time before it flushes, if that makes sense, like, in the opposite direction.
**Douglas Camata** 21:07 Yeah, that would be at the extension level, right? Or any other user of the library.
**Evan Bradley** 21:13 Right.
**Mikołaj Świątek** 21:17 It makes sense to me that this should be configurable.
Largely.
So, deduplicating is one thing. I think you can… if you… We should duplicate.
Always.
In addition to duplicating, we should also have some kind of debounce. So… because… keep in… keep in mind, like, the model I have in my mind of, like, components in an Opal Collector, these are essentially just, like.
independent units doing whatever they want. At least in terms of status reporting, they can report whatever they want, however often they want, they can spam you with a million events immediately, either intentionally or accidentally, right? So, we can't really trust them In general, and at this point… up until this point, there was a firewall in core that protected us from it, implicitly, and now we just have to kind of protect ourselves. Like, we're essentially accepting.
**Douglas Camata** 22:16 Yeah.
**Mikołaj Świątek** 22:17 Events from some channel to which we need to apply rate limiting.
that we want, and then we're sending them out at some cadence that should be configurable, prefer whatever the consumer wants. I can easily imagine that somebody is going to want to get, like, status updates every 15 seconds, for example.
Right? They don't… they don't care about lower resolution, and it's like a performance thing for them to… to not want more, and I think it's, like, the extension sounds like the right place.
to me. To… to both make that determination and to have the implementation of it. Though, out of… maybe eventually it makes sense to… to… to move that into OpAMPGO, but I don't think we have that… enough consumers of OpAMPGO to really, like, know what is… what should live there versus… versus anywhere else.
Mmm… There's also the question of, like.
Status itself is not exceptionally well standardized right now.
So, there's a status event that is a well-defined API in Collector Core, but what we're actually consuming in the extension is not that. We're consuming aggregate status, and aggregate status is a contrib construct.
It doesn't even have, like, for example, one of the reasons this exists, right, is that status event doesn't have a canonical serialized way of serializing it.
And we do have to serialize things. In a half-check extension, we have to serialize them, so we basically come up with our own type to do that, which is very similar, but we do have to come up with it, and then the spec also has to come up with its own type to… To represent it on the wire, right?
So… at some point, I imagine those things will… will kind of settle down, and they're gonna be moved to carve, maybe? So… so this is a… so this is clear, but right now, we're… None of this is, like, fully blessed, I would say. So I wouldn't… I wouldn't try to pull it into… pull any of it into OpAMPGO itself in any way.
There shouldn't be a… I'll go right now, anyway, in my opinion, and I agree with Evan on that, should not be opinionated about those.
**Douglas Camata** 24:52 Yeah, that sounds, sounds good. And, to your first point on the configuration of how often things should be sent to the backend.
At least when it comes to HTTP, to the HTTP1, That… that already exists, that includes… but for some reason, Health status changes were, bypassing that.
And they will still bypass it, If we go with the fix that is in the PR link in that issue.
But they won't bypass that if it's really different.
I don't know what will happen in WebSockets. WebSockets may be… Because it's something that I personally don't use.
So, yeah, but, we, we've… So, so maybe what we really should think is, do we want any kind of… Update in the health.
to bypass the… The backend pooling interval?
Or do we want to, right, hold them until the… the time to report to the backend comes, and this time is already configurable, at least. It was just not being… Not being used when there were health status changes.
at least on this, also, we don't need to decide right now, because I think the… the PR there is already a good mitigation of only pushing it.
If it's really different than… than what it was, what it is in the in-memory representation that the extension keeps.
So… That's something we can talk about later.
**Daniel Bright** 26:56 Must be careful.
**Mikołaj Świątek** 26:56 Probably.
**Daniel Bright** 26:58 Go ahead, I'm sorry.
**Mikołaj Świątek** 27:00 I just wanted to say that this PR is probably, Probably should actually compare these by computing, like, a hash of the serialized version of it, rather than doing what it does right now, because that's gonna be more future-proof, but it's, like, it does fix the problem as it exists right now.
It's just… I fucked.
**Douglas Camata** 27:24 I thought the exact same thing when I saw it. Why don't we just hash it and… Include everything, maybe, inside of the struct somehow, and… To be future-proof.
**Mikołaj Świątek** 27:36 The only problem with hashing it, potentially, is that, like, is the serialization consistent? I am… I am infinitely scarred by the iteration order of map keys in Go at this point.
So if that's written, I'll review it. I'll write what I… what I mean here. I am now…
**Douglas Camata** 27:57 The greatest footballer.
**Mikołaj Świątek** 27:59 I am now a proponent of writing… of writing a test that checks whether the struct containing a map hashes to the same thing if you run it, like, 5 times.
**Douglas Camata** 28:13 Yeah, yeah, and in general, it would be good to have your eyes there, as it seems like you are our health status guy.
**Mikołaj Świątek** 28:28 Daniel, I interrupted you, I'm sorry.
**Daniel Bright** 28:31 No, no, you're fine. I was, I was just gonna give some of the use cases for how we're planning on doing this here, just to see if maybe… it could help, you know, drive the conversation a little bit more. So we're going to have different granu- er, the goal is to have different levels of granularity, to where the agent is, actually essentially pulling down a new config.
That's available, so it could be anywhere from a minute to… it could be 30 minutes or an hour, depends on The tier of the service, and, you know, the agent itself, and where it's deployed, a bunch of different factors.
And as far as the, you know, so I guess the thing would be to separate out the, the OpAMP Status versus the status of, you know, data actually flowing through the collector, right? And… we're going to probably, you know, as… just as a company, like, we're going to rely more on, just, like, is the data flowing properly? Do we have, you know, all the things we measure, kind of, now already through our OpenTelemetry gateways, to… to rely on you know, the status of the pipeline itself, is for the actual, supervisor, you know, I was just thinking, like, maybe… maybe one of the options, or this might already be, and I haven't dug too deeply into it, but, getting the status, or having an option to have the status delivered as a, you know, just as a telemetry item, right?
Through the… through the actual collector might be an option, too.
So… I know there's different use cases, for why the status is reporting a health backup to the OpAMP server versus just telemetry.
But… Yeah, I'm just throwing that out there, so… I have a lot more to learn. I haven't dug into the code as much as I'd like to either, so I'm gonna… I'm gonna be doing more deep dives, coming up pretty soon, so…
**Mikołaj Świątek** 30:43 Part of the reason for that is just that there wasn't really a very good signal type to represent this.
But now there is one in events.
**Daniel Bright** 30:53 Yep.
**Mikołaj Świątek** 30:54 It is even named event in Collector Core.
And, in fact.
I might… I'll try to find this… this issue. In the original issue where we added attributes, we already actually talked about this, and kind of, kind of?
got buy-in from… from… from collector car maintainers for this idea, at least from Pablo?
Couple of billions?
Where, essentially the… let me… Let me try and find it… So, essentially, we, we agreed that the kind of end goal for this should be that the status event should just be a pdata.event. pdata as in pipeline data, as in the internal, you know, the way telemetry is internally represented in collector, in a collector pipeline. And it should be that.
And the attributes, the attributes we've added are specifically added in such a way that it's consistent with that approach.
And it probably can be done reasonably well.
there's one question, I think, that needs to be answered before… before it can be done that way, because a status event is really just an interface. So the… we're not pinned to any specific data representation. The only problem will… the only problem there that… or the only question that has to be resolved is that It contains an error.
And an error in Go is, again, just an interface, so there has to be some canonical way of serializing that.
for it to work. Because PData is not allowed to just contain an interface. It has to contain concrete data types, has to contain things which can be written into Protola.
So you have to define what that error exact… is exactly. Maybe it's just a string, right?
Or maybe it's something more complicated. But right, the compatibility problem right there is that right now, an auto component can put literally whatever they want into that error.
Right? It can… like, normally that's just gonna be a string, you know, let's be honest about error handling in Go codebases. But, but it might be whatever. So, there's gonna be something like a breaking change there.
For this to actually happen, so that components can still emit whatever they want, and then at the boundary, we're gonna say, okay, so you omitted an error, we've serialized it into a string.
according to, like, because an error has to have a string method, right? We just turned it into a string, we serialized it, sent it over the wire. On the other end, we just, you know, we just wrap it, that string in an error type again somehow, and, you know, whatever other information was in there that was structured is not structured anymore.
Like, that's something that would need to happen for this to work. But I don't think this is gonna be a very… Strong barrier.
Towards actually implementing this. And it would be nice, it would be nice to just emit status events into a pipeline.
If you wanted to.
Does that make sense?
**Daniel Bright** 34:26 It does, yeah.
**Mikołaj Świątek** 34:28 And I can… I'll get to this… I'm following a long chain of issues.
Over here…
**Douglas Camata** 34:38 chain of events.
**Mikołaj Świątek** 34:41 Yeah.
There we go, it's, like, here, it's this one, I believe. Okay, so I'm gonna put it in chat.
So this is the issue, it is actually closed, because we did what we wanted to do, but it also contains discussion about, like, how you might represent status events in PData.
**Douglas Camata** 35:09 Same.
Yeah, that… that… that will be useful, because whatever way we decide to handle to do… This kind of the duplication slash aggregation in the extension.
Today, we have to do something similar in the supervisor as well, potentially.
Maybe not… But, yeah, that's… that's awesome, that's all very useful stuff, Mikola.
**Mikołaj Świątek** 35:42 It would… this would also solve the problem… the contract package status… the contrib trip status package has… it has to come up with its own representation. This is just P data, then… You don't have to do anything special.
You, you can, you can compose that, however you want, and you're guaranteed that your, that your thing is, both serializable and deserializable in, like, Well-defined way.
So, probably, like, a decent chunk of that package will just be able to go away.
Where it's now, like, it's, like, converting to its own type, and defining how that type goes to JSON, and then so on.
**Douglas Camata** 36:32 Cool.
Yeah, yeah, this was mostly what I wanted to bring to discussion with that point.
And then I hope… I hope we can… Have at least a small fix.
Before the next release, because now we already have 3 releases out with the… With the memory limiter's potential to completely spam, backends.
Hopefully the next one will… will have it fixed.
And then we can do something… Something better.
after some investigation on all those things Mikola said, and of course, bringing more people into the conversation as well, because it seems like a bigger change.
That we are even not sure yet if we want to do right, but we can talk more about it.
Yeah, that's… that's it from my side, and there's no extra points added.
So I guess we're good.
**Evan Bradley** 37:58 Great. Alright. See everyone next time.
**Douglas Camata** 38:01 Thank you, guys, see ya.
**Dakota Paasman** 38:03 See ya.
**Daniel Bright** 38:04 Nice to meet you all.
**Evan Bradley** 38:05 Nice to meet you all.
