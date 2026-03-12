SIG: Specification SIG
Date: 2026-02-03
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 00:02 Because Tao City is smaller than…
**jmacdonald** 02:37 Hi, everybody.
**Jonatan Ivanov** 02:40 Hi.
**jmacdonald** 02:41 I'm going to be your meeting operator today.
Okay.
I'm on call, I guess. Here's the meeting notes. If you have an agenda item, please add it. I think we could probably wait a couple more minutes. I know it's gonna be kind of a light week from the conference in Belgium and Fostem happening, so it could be short, I wouldn't mind, but I'm glad to be here.
And… You may notice from the notes in front of us that I pre-populated a few things just from my review of all the open issues yesterday, so I've given us some things, to talk about, but if we don't have enough people, it could be a short one.
So, while we are waiting, it will start… To… show you what we're looking at here. What are we looking at here?
Whoa… Okay, it's a pretty small group here, and people are gonna continue coming in, but we can, I'll… I'm talking, why don't I keep talking? So, I've gone through all the specifications SIG and the OpenTelemetry proto repositories yesterday, looking for, like, open and loose ends.
And of course, there's lots of things open, but these are the ones that I've found that are kind of substantial and haven't been discussed in a while, as far as I can recall.
So, I thought I would just run through them and see if anyone has open thoughts, or wants to be reminded of these.
So, the first one, is this conversation that's been ongoing since October about introducing reference-based attributes. Has a bunch of approvals now.
So I think, like, we are over the discussion phase and ready to see if we're ready to go on this. Just to remind you all, this is actually a very small PR at this point.
And it is… well, it might not be very easy to read in this environment, but let's see… We're taking, the AnyValue protocol and adding… sorry, that any value protocol now has a string value ref, which is an integer, and it refers to something, and that's basically it, the entire PR.
is, having a reference type. Then key value… can have a key ref in it.
Gives you the ability for the profile signal to have a dictionary.
And… as I was saying, it has a lot of approvals at this point. I know that Tigrin has been, spearheading that one. If you were here, I'd ask him to comment.
And there's a few nits left. Does anybody want to talk about this topic?
You are not required to have an interest in this topic.
Again, it's a short week. I don't know if we have, when we'll see Florian again, or Tigran, but we'll talk about it next time.
**Daniel Dyla (Dynatrace)** 06:07 It's obviously being added for profiling.
But…
**jmacdonald** 06:11 That's my understanding.
**Daniel Dyla (Dynatrace)** 06:12 It's added in the common area. Do we expect this to then also be used for other signals, or is there some… is that explicitly allowed or disallowed, or is it just left to specification?
**jmacdonald** 06:26 I believe it is left to specification. I know that was discussed as a sort of fear, like this is being introduced for profiles only, but it obviously implies that we would do the rest, do the same for the other signals.
I was hoping to have Tigrin to give us the latest update on this, partly because it's quite a long thread, and I don't have the answer to your question at the top of my head.
So I apologize, but I'm not sure I can answer that one. But I can take notes about it.
So… So that'll be an open question for Tigran next time we see him, and or for Florian.
Well, I'm just gonna suggest we keep moving forward without a… without a critical mass on that topic. The other, in my opinion, major effort ongoing that's close and worth discussing happens to be this work on entity event reporting.
This one has been open for a while.
Or for a short while, and, has quite a lot of discussion on it.
And I admit, having an interest in talking about this myself, but I don't have, nearly all the context that others do. Is anyone here, interested in speaking to this particular issue right now?
We don't have to be. This is sort of a run-through, and with the short meeting, or the small meeting today, I think we could probably just move past it. I did have a topic that was connected with this one that I wanted to raise about, No critical… This, this comment below, this might be interesting to a few of us in the room. I'm looking at you, David.
This is, a conversation that came up in the Collector SIG earlier this week.
I'll just open it to give you a feeling for the conversation, and then probably we can just move on. This is, I guess hemming and hawing about the sort of movement in semantic conventions, where we would like to dictate that state-set metrics in the Prometheus world come out looking the same, essentially. And it raises this point that, you know, to have an N-valued state metric, you need n metrics, which feels bloaty and large and overheady.
**David Ashpole (dashpole)** 09:10 Yep. That's what this is about. There's sort of a little bit of resistance just to be adding bloat, and then… and then, in my opinion, there's a sort of…
**jmacdonald** 09:17 Thematic question here about instrumentation.
I wrote my comment, it is linked from the notes.
The comment is that I would prefer to see us instrumenting events event changes at the API surface, and then let the SDKs turn them into status metrics, not to see metric instrumentation generating status metrics. So it's a good opportunity for us to talk about the differences between APIs And what the SDK does. I don't want to see us instrumenting status metrics. We should do state event changes and derive the metric events.
If you will, I connected it with, another topic… Having to do with, The up being the status metric that many people think about, and whether we have the will to talk about uptime and the upstate, So, this is an esoteric comment. We can take that into the, Discussion thread in the issue, if that interests you.
**David Ashpole (dashpole)** 10:21 Oh yeah, this did interest me, actually. I had started writing a response, but I wanted to, I was chatting with some of the Prometheus folks as well, to better understand, like.
When they introduce state sets.
what they had in mind, and why it came about. So I have a little bit… I can also leave this in a comment later, but it might be interesting to people on the call. So… State sets came about partially, actually, to encourage better instrumentation, so I think your point about Writing instrumentation is actually a good one, but… The idea was that with state sets, someone would actually just record state through a separate API, and that it would come out in the current iteration of the Prometheus text format as a bunch of gauge-like series, right, that were zeros and ones. And you could have… it's a bit set, so it's not just an enum, where only one state is allowed to be active at once. It could be, like.
multiple states are allowed to be active at once, right?
And it didn't really get wide-scale adoption, mostly because the client libraries never added, like, explicit support for it, and most people continued to use gauges for it.
We've actually had some discussions in recent weeks as part of the Open Metrics 2.0 group within Prometheus.
About adding a better representation of state sets to the text format.
I can, maybe link those later, but the idea would be that instead of Two dozen different series, one representing each state, that it's actually encoded in a way that's both more human-readable As well as more compact.
So it would be one line basically telling you what the states are and what the active states are, or some representation like that.
I was… I also asked some of the older maintainers about, like.
Why… why the zeros are important?
And it turns out that for some queries.
And particularly for some alerts, you'd like to be able to do things like average over time.
Of a particular value. And then it's… it's quite useful to be able to differentiate between This pod was never running, or was never meant to be running.
And this pod was meant to be running, but was in a state other than running. So… zeros… it is, I think, possible, maybe, to write those queries. You can join the value zero with the up metric.
and then throw it in an OR as, like, a fallback.
**jmacdonald** 13:02 Yeah.
**David Ashpole (dashpole)** 13:03 And it actually gives you some of this behavior, but they're a little bit wonky to write.
So, all that is to say, I think I do think state sets have their uses, and are certainly… I… It does seem like it is valuable to record states as a metric, and not, like… maybe a derived metric, but I don't know if the current representations are that useful. Like, I do agree that the current representations are all very expensive.
And… If you get a lot of states, they become… A lot, a lot expensive.
Yeah.
**jmacdonald** 13:42 I think… I just remember in the data model, kind of trying to find a way or think through what would it take to make it so that we didn't need such a verbose representation, and I put a few of those comments in there, like, you know, delta… delta temporality, you could just have two updates per… per state change, for example, or if you had a bit flag that said, I sum to 1, then 1 implies everything else must be zero, and you can, like, do that on the server side, for example. Those are some ideas that I have thought about in the past.
But thank you, so that was good. We can talk about that again. Appreciate the input, David.
All right, well, that was my little, like, primer to make sure we had some talk in this meeting, which could have been less attended.
And now we're on to agenda items other than mine, so thank you all. Jonathan, I, see you have a point about the binary distribution.
**Jonatan Ivanov** 14:31 Hey, yes, so this is about, OTLP, the protocol, binary distribution. I wanted to, like, ask this question, or, like, raise this, I don't know, like, feature request?
from this spread group, because, like, OTLP is kind of its own thing.
And, like, users should be able to use it on its own.
But right now, as if today, this is, like, rather, rather hard, because OTLP, like, it should have, I think, a stable and official kind of, like, a client library to… which contains basically the, like, the OTLP types, and also some way to, like, serialize them.
But right now, as far as I know, this is not, like, specified, so that, like, language implementations, like, they are doing, like, various things. I'm not sure what, like, others do, but I know that, like, the Java, implementation.
There is, like, an OTRP proto library, which is not intended to use by, like, end users.
So basically, OTLP is released and distributed as a, like, the text file, the proto file, which makes things, like, very hard if you just want to use OTLP.
And, like, these… is basically coming from… and I know that there were, like, a lot of discussions, on this topic, like, before. Not necessarily, like, the OTRP binary distribution, but how hard it is to basically create, and generate the types and use them.
As a user from the profile. Because as far as I know, like, One thing which can get in your way if you want to do this is that CodeChen, because if you use it.
and you modify the version of it, it can break binary dependency? Sorry, binary compatibility for your dependencies.
And as far as I know, that happened, for the… for the Java implementation, like, multiple times. And also, there are customizations in the OTLP spec, so the default, the vanilla protocol gen, as far as I know, it is… it is not going to work.
So, for example, the Java group, they ended up, like, hand-rolling, like, the types and the serialization.
And I guess users can do that, but the problem is that other… it is… other than it is, like, a lot of work, you still need to test it.
Against the proto, so you will end up doing this anyway.
And it can mean, like, a lot of, like, headache to the people.
Other than these, like, generating them is hard.
If you hunt roll them, it is still hard. And also, I guess, since It is a… Like, it is basically, like, distributed as source.
As of today, it's also kind of inconvenient if you want to declare it as a dependency in those languages that has, like, a good, like, dependency resolution, like, ecosystem for binary distributions.
So, to sum this whole thing up, my ask is, is there any way that the OTIP specification can contain, just, like, I don't know, like, one sentence, that library authors should or must provide a binary distribution for OTLP that contains the types.
And, like, some helpers to serialize those types.
**jmacdonald** 18:22 That's an, thank you, Jonathan. I understood the question. I'd be interested in other comments before I, you know, speak. I'm just running the meeting here. Anybody have thoughts?
**Reiley** 18:33 I remembered.
Sorry to death.
**Daniel Dyla (Dynatrace)** 18:36 Somebody else started speaking. Riley, go ahead.
**Reiley** 18:39 I remember this topic being discussed a couple years back, and it was a conscious decision to not publish binaries.
And I even remember some 6, at that time, they were publishing binaries and exposing that, and then, ended up having a lot of breaking changes, and super unhappy users.
Eaters, so they clarified it and decided not to do that.
**Daniel Dyla (Dynatrace)** 19:05 Yeah, that's basically what I was gonna say. My SIG is one of those SIGs that used to publish… Like a library, it was never meant to be used by external users, and we kind of went out of the way in the README to say that Because we don't have control over the code generator, and when we update it, it makes breaking changes, and… you, you know, we put in the README, this will be breaking, don't use this, we don't recommend it. And then people did, and it caused problems. So, we stopped publishing that, and we rolled it directly into the exporter and made it, like, intentionally difficult to get at.
And I think I was not the only maintainer that had similar problems at that time.
Like, we're… we're trying to publish client libraries for OTEL.
And that's an implementation detail.
I think it's additional… maintenance burden for the maintainers that are already buried. I would, as a maintainer, be… strongly against this as a requirement. If other maintainers want to take this on, they're, you know, more power to them, but as long as it's not absolutely required of me, I'm not going to.
**Jonatan Ivanov** 20:23 I think other maintainers has, like, the same situation.
And the interesting problem with all of that that you just said, I wholeheartedly, like.
agree and, like, feel your pain about this, but I also think that if It will not be solved by the hotel maintainers.
then the users need to solve the same thing. They will bump into the exact same problem set.
And instead of, like, this being solved in one place for everyone, everyone needs to solve it one by one, who wants to use OTLP, as its own thing.
And I… Don't think, though, I agree with the part where you said, that this is kind of like an implementation detail. Like, OpenTelemetry protocol, it's its own thing, it is, like, specified, and users, like, should be able to use It… like, on its own.
Does that make sense?
**Reiley** 21:25 I have a different understanding. I… I think the… like, if you have a protocol file.
The… the thinking here is… you're the final user, you don't expose the protocol-generated, like, library or API as a contract, then it shouldn't be very hard for you to generate the binary and use for your internal case. Like, you… of course, you expose something, but you don't expose the protocol-generated contract directly.
That shouldn't be hard.
And if you try to use the protocol file and generate the binary, then it'll be very hard for you to provide a backward compatibility. And this is why I think Google invented protocol instead of, like, just using the generated the binary as a contract.
**Jonatan Ivanov** 22:14 I think in some cases, like, I… I also, like, think about, like, libraries.
that wants to use this. I think in some cases.
It can happen that they, like, surface, like, open telemetry types on there, like, public API. For example, if you want to, like, create, like, I don't know, like, an HTTP or, like, a gRPC client, for that, or, like, I'm not sure, like, what else, like, use cases can happen where they… they want to do this. So, I think they can bump into this problem with, with, with CodeChen.
but also… like, I… I also think that this doesn't need to be this, like, binary distribution. This doesn't need to be, like, proto-generated.
This could be just, like, hand-drawed, like.
I know that the Java team is hand-rolling it because of these issues, and manually creating the types to prevent these binary incompatibility changes, but it can be tested.
By the, by the proto-generated, like, like, files to produce the same output that they would, or to produce, like, an output that can be desirized by the proto-generated files.
**Reiley** 23:38 Yeah, I know OpenTelemetry .NET also did a unrolled version of the… the serial rider, at least, not the.
**Jonatan Ivanov** 23:45 I, I'm… I am not asking, like, having a binary distribution from the proto. I am only asking having a binary distribution.
It can be hand-crawled.
It doesn't need to be…
**Daniel Dyla (Dynatrace)** 23:58 That's even more work.
**Jonatan Ivanov** 24:01 I… I'm not sure. I…
**Daniel Dyla (Dynatrace)** 24:05 I mean, I can tell you, I'm 100% sure. I maintain the JS library. We're generating code right now. If we went to a hand-rolled version, I would then have to write code that I'm not currently writing. That is more work by definition.
**Jonatan Ivanov** 24:20 Yes, up front, yes. Yes, yes, yes, I totally agree. But after that.
Is it, like, more work to, like, fight with the code gen all the time, or just, like, modify the Android version when the OTRP specification changes? I'm not sure, though, like, how many times this specification has changes that would change also the protofile.
**Daniel Dyla (Dynatrace)** 24:44 I've never fought with the co-gen, so I don't know what… issues you're talking about.
**jmacdonald** 24:49 I can't.
**Daniel Dyla (Dynatrace)** 24:50 Any problem with it.
**jmacdonald** 24:51 Can I describe one? I mean, one of the benefits of protocol buffers that's advertised is the ability to, like, make a wire-compatible change, but rename a field, and we've run into so many problems with that. Like, it breaks JSON, so we stopped doing that, but it has broken us in the past.
I'm sympathetic to the question, but I agree with the other commenters here, that… that the burden of supporting a stable binary protobuf interface is, like.
It's, you know, it's essentially saying that the protocol compiler should never change, which we don't control.
Anyway, I have seen this problem as well in all the places I've worked.
the Go SDK has its own proto-library. The collector has this P data abstraction, which is an abstraction meant to give you a data standard API that is stable. So the closest we have right now is the collector's P data.
Which I think would give you what you want, but only in Go. And I would… I would just follow that with… same thing as happening in Rust. The OpenTelemetry SDK has its proto. We're working in the Hotel Arrow project on a new Rust codebase. We've copied the… we have the same proto library, but with different… slight differences, like, do you want to use a Uint 128 for your trace ID, or do you want a 16, byte, you know, slice of bytes instead? Those are choices that you have to make when you choose the binary, and, like, we can't make those choices without forcing ourselves into a future, like.
Corner, I think, is the problem.
So I think I understand the reason why we would not want to formalize, or to support such an interface, and would recommend you use an SDK instead, or a collector library. I know that might not be available.
**Jonatan Ivanov** 26:40 So that, that's the interesting part, like, like, like, using this through the SDK, because that would mean OTL be, like, highly coupled.
And I guess, like, one of the core, like, values of OpenTelemetry is to be loosely coupled, so the bits and pieces should be used, like, on its own, which is… Possible today, but it's very, very hard.
to use OTLT, just on its own.
**jmacdonald** 27:09 Yep.
Yeah, I felt this frustration multiple times as well. It's… unfortunately, the protobuf compiler gets into a can of… like, it's just… it's not clear that this is a sustainable effort, I guess is what I'm thinking.
I don't feel that we've found a good answer for you. May I ask which library you're looking for? Was it Java?
**Jonatan Ivanov** 27:31 Yes, yes, yes. So, it can be basically anything. I… can totally, like, see that this is a problem, not only for Java, but, basically for every single, like, like, language.
**jmacdonald** 27:45 Are you trying to generate a photo, or to receive it? Like, are you writing a reading?
**Jonatan Ivanov** 27:49 I want to create the open telemetry protocol output.
**jmacdonald** 27:53 I see. So you would like to make your own SDK, basically, yeah.
**Jonatan Ivanov** 27:57 No, no, not necessarily. Like, it doesn't really, like… or, like, if you just, like, think about the exporter part of the SDK, then yes.
**Trask Stalnaker** 28:05 Yeah, they are writing an SDK, it's just not an open telemetry SDK, they have a different telemetry SDK called Micrometer.
**jmacdonald** 28:14 Totally.
**Jonatan Ivanov** 28:14 If you are talking about only micrometer, then yes, but it's not… it's not only a micrometer concern.
Like, I… I am talking, like, I met users who, like, want to, like, generate, like, OTLP, like, not using Micrometer, not even using the, like, the, OpenTelemetry SDK, and they want to, I don't know, like, publish the data into, like, Kafka.
and they have their own, like, client library for that, and they have the same problem. I can imagine that, like, Brave right now, which is, like, a tracing library, could produce an OTLP output. They would use that as well. Logging Libraries, who has their own, like, like, output providers, or, like, appenders, like Log4J and LogBack in the Java Word, they could use that as well.
And of course, micrometer as well. Micrometer is my biggest use case here, but that's not the only one.
**Tigran Najaryan** 29:17 It's amazing.
**jmacdonald** 29:17 I just…
**Tigran Najaryan** 29:18 Maybe a compromise… Go ahead, a compromise here would be to produce documentation, proper documentation, on how to generate the OTLP bindings for… Maybe all of the languages?
And maybe provide the… also make the… We have the build tools.
which we use internally. Maybe Nakedet also, sort of an officially published Pocker image you can use for generations. So, give you the means to do it yourself, but… Help you a bit with doing that.
That would be a different approach here, I guess. We will not maintain the libraries, we will only maintain sort of a small documentation, but which would help you to do it yourself when you need it, the right way.
That's a possible approach, I'm guessing.
**jmacdonald** 30:12 Yeah, so I could see us as a pro… the OpenTelemetry protorepository has some apparatus for this already. It does have a Docker image that does contain the Proto-C image we use, I believe. I could imagine with, you know, toil over build process to make it so that for all the, like… we just have a standard thing. For every language we have, a proto-C output generated and built and published.
Somehow.
It's a tremendous amount of work.
The thing that's occurring to me here, now that I think through it a bit more, and Jonathan, I'm sorry I didn't realize before, but now I do recognize you as the author of McCormeter. This is nice to have you there. It's been years since we were here together. The problem I'm concerned about is that If you are… the thing I just described, which would be to publish, you know, say, a set of Proto-C libraries for every language, is, like, just, like, the straight vanilla Proto-C output forces you into the interface of allocating lots and lots of objects. So, to create an OTLP metrics export, you need to create 1, 2, 3, 4, or 5 levels of hierarchy.
Every one of those is an object. You've got objects for your metric, for your data series, for your value, for your number point. Like, there's so many objects being allocated to hand that to the proto-C in the conventional way, which is why the Java SDK has rolled its own.
So that the interface you want to generate OTLP is really, like.
not… like, as soon as you force someone into the objects, you have bad performance, so therefore you want to sort of start with exactly the format you have, and output the data sort of directly. In the Rust area, we've just been writing procedural macros to help us write protocol directly. Like, I know the tag number, I know the bytes, I know the representation, it's very simple, let's just emit these bytes. So I would propose to you what you actually want is, like, the pieces of the Java SDK that are hand-rolling OTLP, they've got some machinery in there. You want to use that machinery, but it's hard to stabilize, which is, like, asking a lot from the Java SDK team, so I don't have a good answer here.
**Jonatan Ivanov** 32:22 Yes, that's also, like, right now internal. Like, it's, it's, it's a private part of the SDK.
**Bob Strecansky** 32:30 Which is, like, exactly for this reason, yes. Yeah.
**jmacdonald** 32:37 So it's sort of a request for a feature, or the… it's very focused on the Java SDK. I would… I would let them speak. I don't have any… I'm certainly not going to try and force them to do this. They've spoken already a bit.
**Reiley** 32:50 And Jonathan, did you see some, like, existing issue on GitHub? I remember people, like, were talking about this topic several years ago. Maybe do a quick search and see if there's something. If not, create an issue, and we'll see, like, how many users share the same problem.
**Jonatan Ivanov** 33:10 None.
**Reiley** 33:11 my guess is there… there's some users, but the number is low. In that case, I… I suspect if this thing will ever get prioritized. So, one option, as Josh mentioned, maybe, like, you take the… existing Java implementation, you try to improve that, and you can negotiate with the Java maintainers and see if they, like, if you're willing to contribute the rest part and maintain that, do they even want to take it? And if the answer is no, then you can bet. If you come and say, I'm not going to write it, and I just want someone to do it, then the answer is always no.
Right, so that's my gut feeling.
**Jonatan Ivanov** 33:46 I can, I can definitely create an issue. I'm not aware that there is one, but this… I remember that this was, like, discussed on multiple, like, issues, like, throughout the, the months and years. Also, like, first I asked this from the Java group, but that was, like, I guess over a year ago, and the answer was… Like, basically, that it is, like, too much work.
And right now, this specification is not, like, mandating, like, anyone to provide a binary distribution for OTRP, so because of that, they are not going to do that.
**Reiley** 34:20 Right. So my take is, if you come and say, hey, I'm Jonathan, I'm waiting to take whatever already exists in the Java implementation, and I'm going to add a bunch of code and maintain the backward compatibility, if you agree to release that. And the answer from the maintainer would be, no, we're not going to allow that.
**Bob Strecansky** 34:39 If that answer is no, then I think when you ask for more, the answer is also going to be no. So maybe, like, explore the first step and see if people can even agree on that.
**jmacdonald** 34:57 Yeah, it sounds like, you know, if someone's gonna step up and make that library work and publish it, and agree to support it, then maybe there's a future path towards the Java SDK agreeing that it's public and maintained indefinitely.
**Jonatan Ivanov** 35:10 Yeah, I… I think from, like, maintenance perspective, like, if the… if the consensus is, hey, this is too much work, we don't really want to do this, that's, like, still have the same risk.
Because, like, even if, like, somebody said, like, hey, let me create this and maintain this for you, what if the next day that people is gone? Or that person is gone?
**Reiley** 35:32 Oh, then they'll keep that before?
they'll keep the library there for 6 months until it has bunched off CVEs, and the security state would find trouble, and they'll remove the component.
**Jonatan Ivanov** 35:42 Okay, I see.
**jmacdonald** 35:48 I'm afraid we don't have much more of a conclusion than that. This is a tricky one. Protobuffs are good and wonderful, and also not so great sometimes.
Love Protobuff.
Okay, well, I propose we move on. Evo, you are next in the agenda, and then I see the people who are, you know, would be good to talk about the first topic that we skipped over at the end, if we have time.
**Ivo Anjo** 36:14 Yes, so, thank you. So, I'm here to kind of ask two questions about that spec, or ask for feedback about, like, two details. One is that, just as a quick reminder, the idea is that for profiling and possibly other things in the future, but right now the main focus is profiling.
We'd like to be able to have, like, the SDK libraries have this mechanism to share, like, process-level information, like, what's my service name, etc, with, like, the eBPF profiler that's sitting outside the process, so it doesn't… might not have, like, all of the information that the process Has, and has been configured via code, or something like that.
And one special detail is that, like, after a bit of back and forth in the specification, the current payload format that we're using is, So if you switch to the, to the, to the, file, to the, to the file. Like, the current format we have, the payload is, a resource message, so it's, like, a resource message that has the usual, like, key value attributes.
And one question came up recently, which is that, we arrived at this, like, use the resource message because we wanted to have the key value attributes, but maybe a resource is not the correct thing to use here, maybe we want the key value attributes, but not the resource, because one of the properties that we want to have here is that we want to be able to update this.
with, like, more information if the process wants to expose more information. And the whole point of a resource, at least according to the specs, is that, like, a resource is supposed to be, immutable. So maybe calling this a resource is wrong, because the resource is supposed to be immutable, and we're saying, like, this can change, it's… Sometimes, like, if there's some extra keys that we want to put in there, So, I was kind of, like, hoping to ask, like, does it… does it make sense to call this a resource, or maybe this is misnamed and it should be the key value attributes, but not naming it a resource, because a resource is something more specific that is supposed to be immutable.
**jmacdonald** 38:31 So I hear two questions. One is about… just asking for a review on the eBPF mechanism here to get resource value, and the other is, what happens when we decide to change that value at runtime?
**Ivo Anjo** 38:46 Yes.
**jmacdonald** 38:48 I would like to hear if anyone has an answer to that one, or a thought.
I feel not in a position to comment on the evolution of entity from the entity SIG. I feel a relationship here, but I can't comment on it, sharply.
**Daniel Dyla (Dynatrace)** 39:15 Yeah, I was gonna say the same thing, but from the opposite side. I know Entities is hoping to solve similar problems, but having not read this OTEP, I don't want to make confident assertions about that.
**Tigran Najaryan** 39:33 What do you… what do you plan to store there in the attributes that you think will change over time? Can you give an example?
**Ivo Anjo** 39:40 So, like, a good example is that, we have… we are preparing, like, a kind of a sister road app to this, which is, like, thread local stuff. So right now, this is, like, process level, where you say, like, oh, this is, like, some attributes about this process, and there will be something that will be the thread level, which you'll be like, oh yeah, there's… here's some information about what this thread is working on right now. This includes trace ID, span ID, and possibly some other things. And one of the things we wanted to was use the… this… the process context to configure the thread context. So the… the… we would put there in some key, some information that would kind of make it easy to decode the thread local information, because the thread local information It's very performance sensitive, so we kind of want to avoid having, having to, like.
that part, like, carry a bunch of configurations, so we would kind of say, like, here's, like, a key that says, like, what's the current configuration of the thread locals, and then you read the thread locals for the… just the specific bits that you need. So… This kind of thing may change, or, like, the application may choose to reconfigure it, and so it's one of the things that we were thinking, oh yeah, this might prompt a change in this mechanism.
**Tigran Najaryan** 40:57 Yeah.
That doesn't sound like a resource to me, I think you're right. Yeah. The thread local information, which changes over time, is… at least it doesn't fit the current definition of the resource, right? The formal definition of the resource is that it's immutable.
And what you're describing is… certainly doesn't fit that. I don't think there's anything wrong with you defining your own message with the key value attributes used.
And then having additional build if you need to have them in the future. I don't see why… why that's a problem at the moment. You could do that.
Anyone who needs to use those attributes on the receiving end to put them into the resource, because they look like a resource attribute, sure, they can do a bit of copying from one field to… from one message to another, no big deal, should be doable.
**Ivo Anjo** 42:01 Yeah.
**Tigran Najaryan** 42:03 And it eliminates the, I guess, the strict dependency that you take if you… if you use the resource. With, with also the… Future possibility of resource… Carrying stuff that is completely unrelated to what you're doing there, right?
with entity refs, I don't know, maybe they are somewhat, because they're referring to the resource attributes, but who knows what else will be added to the resource in the future.
So, a little bit of decoupling… conceptually, I think, won't hurt your case.
And as long as you're reusing the definition of the key value.
That gives you, I guess, the… The right level of compatibility with the rest of the ecosystem, while allowing you to evolve whatever you do at your own pace, without relying on what happens with the resource over time.
I have a similar feeling I have, because it's a bit difficult to tell without, I guess, knowing a bit more about the precise use case you have, but that's what I'm feeling at the moment.
**jmacdonald** 43:16 We've recently done some thread local instrumentation for Rust… for Rust OT Aero stuff, and the mechanism used there, it's not using eBPF, obviously, but we have a thread local that… or more… one or more thread local variables, each of which I expect to map into a pre-encoded OTLP bytes for scope.
So I can then quickly see all of my scope fragments.
concatenate them, and they become a scope object. So essentially, I would recommend not to focus on structs with fields or lists of fields, but to focus on a single byte array, which is the pre-encoded OTLP bytes. And I would use that approach basically everywhere, that's what we're doing in Rust, is to try and just assume that we're never handling objects anymore. This is getting back to the previous conversation. We're just, like, generating bytes wherever you need them, handling them as a vector of bytes.
That would be my recommendation as well. And then you could just, you know, use your thread local variable, find 2 or 3 fragments.
combine them into an OTLP object or something like that, or encoding.
That's a little off the topic, though.
Evo, do you feel like you've received the right type of feedback?
**Ivo Anjo** 44:21 Yes, I think that makes sense. I will kind of look into revising slightly the format and to kind of clear up this confusion, and just wanted to add that, like, yes, I think we are… the way we're kind of preparing our other PR for the other spec for the thread context, I think, is going in the direction of what you're saying, like the contiguous, by the way, for the reasons that you mentioned. So, thanks for the feedback.
**jmacdonald** 44:49 Cool, thank you. That's exciting. I think, I like to hear all this. Very good.
Then, okay, we… we reached the end of this part of the agenda, but now we can wrap around at the beginning again. And I was saying at the top that I had gone through all the spec and proto PRs this… yesterday to see what was hot, and I found this topic, and I see Florian here. I also see Tigran, both of them. We were hoping to discuss this with you, actually, so I'll just open the PR. We looked at it at the top, it's like a very short PR, and the question that came from Daniel was, okay, so do we expect this will happen for other signals, and how… what's the… what's the sort of trajectory for us?
**Florian Lehner** 45:34 Yeah, hi, sorry for joining, Lloyd, I just learned about the meeting. Yeah, Just to answer that question first, do we expect to land this in other segments as well?
The short-term and mid-term answer will probably be no. The reason is that these reference-based attributes require a dictionary approach, and this dictionary approach is not available in other signals.
From the profiling signals, we can do this, because profiling already uses a dictionary approach.
But for, logs, traces, and metrics, this would be something new, and, as these, signals are more established, the introduction will be need to be more careful, I would say. So, that's… that's definitely… I think there is no plan to do it at the moment, not soonish, maybe with a version 2.
But that's up to the future.
the current state of the PR is, please, Tigran, correct me, that we… That's the current agreement.
Josh approved it already. I think, if I remember correctly, the profiling sick. So two stakeholders we are waiting for feedback is, Bogdan and, Tigran.
And, from the PData side, the idea is to have a… have this in a transparent way, so that, the string ref… the reference-based attributes are, handled automatically when, generating… when handling P data, so there should be no, API changes. Yeah, but that's the idea of especially of Bogdan, how he will implement it in Auto Collector.
The advice for other signals, like, blocks, traces, and metrics, is not to use it.
**Tigran Najaryan** 47:47 It's not just a device, it's impossible to use it. So, I agree with everything you said. Today, it's impossible to use it for other signals.
I agree with us not planning to have it for other signals.
For now, But… we still left the door open there. It's a possibility that long-term, we may rethink And… and add it to other signals.
there are probably many implications of trying to do that. Unclear whether we will ever do it, but… it's not… complete… the door is not completely closed there, right? So it's a possibility. Not right now, though.
In terms of the, approving this particular PR, Florian, I was hoping to see the results of the two proposed ways of handling, this NP data.
I am hoping that the approach that Alexei proposed will work.
Which would be great, if we could make it work.
I wanted to see, essentially, the results of trying those approaches before I gave my approval, because I didn't… I don't want to rework this again if… It turns out to be a problem from the P data perspective.
I wanted to have that confirmation, the final confirmation that either one of those approaches, either what I think Bogdan was proposing, or Alexei was proposing, one of those approaches works well, and we're happy with those approaches. There's no more objection from the collector side, from PData side.
And we can just approve and go ahead with the PR. That's why I have not yet approved it myself, but I'm not opposed in any way to the PR.
I just wanted one more additional… Confirmation, to be more confident that this is how we want it to be.
**Daniel Dyla (Dynatrace)** 49:43 I also…
**Florian Lehner** 49:44 I'm not doing whatnot.
**Daniel Dyla (Dynatrace)** 49:46 I just want to clarify that my question was not asking for it to be included in other signals. I just saw that it was included in the common part of the proto, and I… I wanted to make sure that I understood the full implications of the PR, which.
**Tigran Najaryan** 50:02 Yeah, yeah.
Yes, Dan, if you look at what the comment says, that the reference number is an index into a strings table, which only exists for profiles, because there's just no way to compose a valid paragraph that… other signals use, which includes a reference number, because it would be a reference number into nowhere.
**Daniel Dyla (Dynatrace)** 50:27 Right, to nothing. Yeah, that makes sense.
**Tigran Najaryan** 50:29 No.
**jmacdonald** 50:30 Do we have guidance on how to treat those data that arrives with, like, key references within a signal that doesn't have a dictionary?
**Tigran Najaryan** 50:41 I think we have something in the comments. It either would be invalid data, or it would be, like, you ignore the value, or something like that. I think we have that guidance somewhere, Florian.
**Florian Lehner** 50:51 Yeah, in the PR, the comment states that signals that set this should treat this as invalid and continue with the next one.
**jmacdonald** 51:03 I'm thinking through what you will get. I mean, if you have an old protocol, you're never gonna even see them, they're just gonna be, like, unknown.
**Tigran Najaryan** 51:09 Exactly, yeah, yeah.
**jmacdonald** 51:12 So you'll end up potentially confusing them for data that's empty, like an empty key value, is what I would expect. You end up most likely, with an empty, yeah, empty key, essentially. Well, unless somebody also sets the key string.
**Tigran Najaryan** 51:24 As a string, in which case you'll see that.
**jmacdonald** 51:29 Yeah, okay. It's not clear how empty data is handled in a bunch of places to me, but that's a… that's a corner case. We can agree, I think.
Thank you, Florian. Thank you, Tigran. That was one topic. There's 10 minutes left here, if you're all still here. Let's keep moving, then. I suppose we can go back to this one. There was… this is a PR that I think is kind of, like.
maybe stuck, and I wanted to hear if there's time to… what's the… what's the current thinking on this one?
**Tigran Najaryan** 52:02 We don't have Josh, we don't have Dmitry here. It's going to be a bit difficult to discuss without them. I have questions there, I posted my comments and questions there.
I think Josh was suggesting a sort of processing which I disagree with.
So, I would want to have him here for that discussion.
**jmacdonald** 52:26 there was a connection that I made, I want you to hear it, so I'll say it again, is that we were talking about how to instrument state changes. There's a desire to see state-set metrics generated for Prometheus, and there's a resistance to instrumenting it that way, because we think we should be able to derive status metrics from entity state changes. Has anyone, explore that, to your knowledge.
**Tigran Najaryan** 52:52 I never know to wear, no, I don't know.
**jmacdonald** 52:54 There's a comment in the notes, this week about it, which David and I discussed at the top, so we can continue that maybe at another forum.
That… without Josh and Dimitri, we can't really talk about this, and I think we've actually reached the end of the agenda, unless something snuck in.
How does everyone feel about ending the call?
Very good. Thank you all. We'll see you next week.
**Tigran Najaryan** 53:22 Thank you. Bye.
