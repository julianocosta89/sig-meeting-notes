SIG: eBPF instrumentation
Date: 2026-02-04
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

**Mattia Meleleo** 00:27 Hello.
**Florian Lehner** 00:35 Hello?
**Giuseppe Ognibene | Coralogix** 00:59 Hi, everyone.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:02 Right?
**Tyler** 01:04 Hey.
How are y'all doing?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:12 Good, good.
**Tyler** 01:16 Have any people coming back from… OpenTelemetry Day, let's see…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:24 Yeah, I think Margot has a topic to talk about.
**Tyler** 01:27 Yeah, I don't see him on the call yet, but…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:32 I think I'm just…
**Tyler** 01:38 Yeah, well, cool. Alright, as I guess we wait for people to filter in, if you haven't yet, please go ahead and add your name to the, attendees list, and if you, have…
Topics you want to talk about, please go ahead and add them there as well, and we can jump in here in just a second.
Florian, were you at the, FOSTEM Community Days?
**Florian Lehner** 02:05 No, actually not, no. But I will be at, KubeCon.
So, if you're in… I think it's Amsterdam, I'm happy to say.
Hello?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:14 See you there, then.
Yeah, I'm going as well.
**Tyler** 02:18 Yeah, there's a chance I'll be there as well, so that'd be great, yeah.
Got the hotel booth. We were talking about this yesterday, we're pretty excited about it.
Mattia, are you gonna make it?
**Mattia Meleleo** 02:30 I don't know, I don't think so. I need to ask Nimrad.
**Tyler** 02:36 Yeah, you guys should make it. It was fun hanging out with y'all last time.
**Mattia Meleleo** 02:40 Yep.
**Tyler** 02:44 Cool, alright, I see…
Mario's on, he's up in space, and so, we could probably jump in here.
Let me, go ahead and start sharing my screen, and yeah, we'll get started.
**Mario Macias** 02:59 Hold.
Yeah, so I would like to start just doing a quick summary. Last Monday, we attended the open… the Hotel Unplugged.
In Brussels, there were some… some topics that might be relevant for this…
for this SEC. So briefly going through them, one is that, there was a discussion about creating a packaging special interest group.
With the… it was proposed by Michele from the… from the Injector team.
So that might be relevant for us, since one of our goals is to start, or to do a proper, operating system level packages for OBI.
Another topic was I raised about an, living room in the hotel demo for auto instrumentation.
for auto-estrumentation mechanisms, it seems there… I mean, I raced it for Obi, but it seems that people from… from the Jetor and even the Java auto-estrumenter, were complaining that… or not complaining, but racing that.
It would be nice to have a version, auto-instrumentable version of the hotel demo.
Also, both in force them, but also in… during the, the discussions, we talk about the, user-defined, I don't remember what is the,
Yes, okay. To start,
Talking with library creators, for people that doesn't know that this is like adding some hooks.
into your code that will let EVPF code to get more information at runtime. It's like invoking some functions that, if you are not instrumenting your code, will have no effect.
in terms of performance, but we'll let providing metadata to UPFCML from Datadoc is very…
interested on this to happen. They, they say they are talking a lot with multiple, with multiple library vendors.
Yeah, Raphael?
**Rafael Roquetto** 05:41 Out of curiosity, did they talk about the mechanism of how they plan to implement that?
**Mario Macias** 05:48 No. It seems that there is a proto… an ongoing prototype in… in the Go runtime.
But not in the current Go version, but there is some fork somewhere with a protocol. I don't know if that prototype comes from Datadog, or comes from the Go team.
I could… I could… it's… it's in the… in the first, slides, I could…
look for them. Ponjo. Thanks.
So… something… Cool.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:25 I just wanted to say, like, I found, after you mentioned this, I found that there's… this might help us with our Rust instrumentation.
So, oxide computers have…
USDTs for, Tokyo Runtime, but they also have… they mentioned here that they're using the Tokyo's runtime hooks.
So, it's quite possible that we'll be able to do something similar to this.
**Mario Macias** 06:48 Mmm.
Interesting.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:51 Yeah, I don't know much about this Tokyo runtime, folks, but, yeah? Yeah.
**Mario Macias** 06:58 Great.
**Mattia Meleleo** 06:59 One other thing that, that we could use USDT for is for, custom, custom probes, like, like business logic spans and stuff like that.
And I know that, some guy from Polar Signals
as propo- as implemented the USDTs.
Somewhere, maybe it has to do with the profiler, and he asked if he… if someone is interested in, contributing some of that work.
Maybe we can, we can start some work on, contributing this, this code to the Silumab library, which, which actually need a link.
Link type for supporting this.
**Mario Macias** 07:45 Nice, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:47 It's a great idea.
**Mario Macias** 07:51 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:53 Awesome.
**Mario Macias** 07:59 Other topics, several people was asking about log exports. We… we told that this is not… we are working on… on…
relating logs with traces, and we are not against logs, exporting logs, that just, okay, we have had other priorities until now, but since there is… it is a…
Common demand, at least from the users attending
there that were interested in… were interested in… in Obi.
Also, another interesting topic, and I agree, so this was raised by Kemal, but, I agree with him after talking with so many customers that don't really know
when to use OB, whether OB can work for them, whether or not, whether they should use SDKs or OBs, or what do we recommend?
So, yeah, it will be interesting to write a doc about when to use OB, the trade-offs, what is good for, what is not good for, some kind of intro… introduction.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:21 We had some of that in our blog post, but .
**Mario Macias** 09:24 Yeah, so something maybe more reachable for FAC, even in a frequently asked question, or section, or something like that, or… yeah, I don't know.
Huh.
And then,
And there, there was, some confusion between attendants also regarding to hotel go out to instrumentation. Not only, hotel users, but also some hotel maintainers.
They were asking about, what's the, the, the role of hotel god instrumentation, when to use Auto Instrumentation or OBI, whether if they use OBI, they should still be using Autel GOT instrumentation for Go.
That was, yeah, something to… to clarify.
Of course, I couldn't provide any… any official… any official response for that.
But, I would suggest, I don't know, what do you think, whether…
we should, deprecate, or… or put in, I don't know, maintenance mode, or something like that, the auto-gold instrumentation.
project, and… Point people directly to Vela.
**Mike Dame** 10:59 Yeah, this has come up. I think that… I don't think that we should, you know, deprecate it, but I think that the distinction
is pretty clearly that end users should almost never be using OTelGo auto instrumentation directly. It's… it's a library, it's a framework. I… I… we had the… the image for it, that we're… I think we're still building.
and the operator uses. I've never been a fan of even publishing that image, especially with, you know, like, tools like Obi that are available. But…
I do see, for vendors, I think that having it as its own distinct, kind of layer, or, you know, library framework, is more friendly to working, building off of that layer directly.
So I think that we could definitely distinguish that a bit better. Tyler, I've talked to… we've all talked about that, too.
I think that was kind of the…
general understanding, but especially as OB came in, anyone that's looking for auto instrumentation should not be, you know, downloading Go Auto Instrumentation itself, and I would say that we should honestly stop publishing an image for it, because it's…
it's very low level. I guess as an example, like, it's a good example image to show, here's how to use this library, but that's really the extent of it, and I think that we could take a more firm stance in that direction.
**Mario Macias** 12:29 Okay. Would it be worth in, pointing to Obi, in the…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:36 I think…
**Mario Macias** 12:36 I don't know, do you read me or in.
**Mike Dame** 12:38 Yeah.
**Mario Macias** 12:39 Your dogs are in.
**Mike Dame** 12:39 I think we could put that right at the top of the README that says, hey, you're probably not looking to use this.
Right, it's,
this is, like, a developer, or vendor, or this… this is not gonna get you the instrumentation that you want, and if you're looking for OTEL, a component that'll get you auto-instrumentation.
go to… go to OB instead. And, I think keeping… continuing to maintain it separately also does benefit the OB project by separating those concerns. Different CI pipelines, allows pinning to different versions of
the library. If we wanted to, we could merge the repos if that makes it easier, but as long as we're able to maintain that, like, kind of independence as it's in a monorepo, you know, as its own modules and its own import paths and tags, but…
for the time being, I think that… It's sat pretty stable.
For a while, I think.
We haven't made too many changes. Our meetings haven't been very active. But as…
you know, more changes and contributions come in in the future, potentially. I think having it in its own separate thing
Because it is kind of big,
makes… makes sense to me. I don't know, Tyler or Nikola, what do you guys think about that?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:09 Yeah, yeah, I agree. We've had that long-term discussion, we just, never actually got to.
Vendor properly the code, and figure out what we should vendor, and so on.
Yeah, we gotta figure out how do we more effectively share the source, to be honest. It's one thing that I don't want to be duplicating effort between the two.
I mean, recently, I was making some improvements, and I know that change now needs to be reported to Go Auto, and I'm like, okay, yeah, where is that on my list? When do I do that?
Yeah, I was optimizing the probe that I added for the backup path for the Go.
the new format of the GoMap.
And I found a better way, and so,
But then the infrastructure I used was all in OB to do the searching for the trace pants, so it's becoming complicated to do all the changes.
At the same time, there's all these instrumentations that were added to Obi that are not in Go Auto.
the different versions. I mean, Mark recently contributed the,
the PGX library and all these things, and so we gotta figure out how do we
how do we make sure that this can be shared or, more effectively? Maybe if we can build that package separately, as you say, for, the ability to vendor or quickly get started with Go… just Go instrumentation, not have to do OB.
The full-blown thing.
Also, maybe… This is not a bad idea. If we can make the images…
Like, consistent and all use the same code to continue pushing the… publishing the image so it can be used in the,
in the hotel, operator. So right now, somebody's asking for us to add Obi to the hotel operator, and I had discussion
Around that.
My preferred way is to put a demon set, because that way we can share all the…
all the common data structures, we would be… it would be inefficient to put OB as a sidecar.
But the operator prefers that we put a sidecar, so I'm thinking, okay,
If it was Go, maybe it would have been more efficient to just extract the Go side, if it's possible.
Actually, I thought about it hard, and I just don't…
Don't know how do we do this efficiently.
**Tyler** 16:46 Yeah, I think that's kind of where I'm a little…
I'm stuck on this one, because we're… we need… we need to move forward at this point.
like…
I haven't seen any movement in trying to get this unification to happen, and I do know that, like Nicholas said, there's
work being done in the Go instrumentation here, but also…
there is, if I'm not mistaken, there's, like, probes that exist in GoTo, or in the auto-instrumentation for Go that don't exist here in OB.
So, like…
it's not a… it's not a great story right now for users, right? Like, they don't have any clear understanding of, like.
well, okay, if I want this instrumentation, I have to use OE. If I want this instrumentation, I have to use the Go Auto. Can they run them at the same time? Like, I mean, there's, like, so many…
issues there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:37 Yeah.
**Tyler** 17:38 I'm happy to… To wait for this to go through some sort of… Integration process, but, like.
I'm also a realist, and, like, we haven't moved on this in 6 months, more than that, since we, like, decided to make this plan. So, like, is this actually gonna happen?
**Mike Dame** 17:59 I think it needs to be a higher priority, and we made the plan, and we've been talking about other stuff for 6 months. So, I think that it could happen. I don't think that there's any reason that it couldn't. I think a lot of the pain kind of comes from
You know, OB being a fork originally and being built its own way, and the more that we continue down that path, the drift is going to get worse.
So, I… I think… Throwing it out is kind of,
Antithetical to, like, the vendor neutrality aspect of…
just OpenTelemetry as a project, you know, is a set of standards and libraries that then there are also components that are built around them, like the collector and the default SDKs, so I think that in the kind of spirit of the project, trying to build everything into a mono tool.
isn't… the right way to go. So I think that if we took the…
you know, really kind of ate our vegetables on it and went back and did our chores to prioritize this. We could…
Get things moving, and, and… Eat some of this pain.
**Tyler** 19:12 Yeah, it's just that in open source, priority is based on users and, like, contributors, right? And, like, I can tell you I'm not going to be working on this in the next 6 months. Like, I'm happy if somebody is going to say, like, I'm going to spearhead this, but, like.
We've already gone through, we've defined our goals in the OB project, and none of this is including.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:33 Yeah.
**Tyler** 19:34 this integration step for OpenTelemetry Auto, right?
And, like, I don't have any movement on the auto side of moving towards this, so, like, I hear what you're saying, and I hear that, like, we should reprioritize it, but, like…
That is kind of meaningless without some sort of commitment from actual contributors to actually do this, right?
**Mike Dame** 19:57 Yeah, I mean, this was… I don't know how it slipped off of the priorities for this year, but I know, like, towards the end of last year, we were talking about making this
a priority. And if it didn't fit into the goals.
I think that we're kind of pushing ahead on, you know, stacking stuff on top of a project that its core isn't complete. So it might take a revisit.
Because…
**Tyler** 20:26 Well, what I'm saying, I guess, Mike, is, like, I… I hear you.
And I'm open to that, but, like, are you saying that this is something that you plan to be working on in the next 6 months? Like, this is something you plan to spearhead, or is there, like, another name we can throw in the hat that's planning to work on this integration?
**Mike Dame** 20:43 Yeah, I would love to come back to this. I mean, we had the whole, steel thread idea, and I thought that the, you know, we…
like, we had steps for this outlined of, we're gonna start with the C libraries, standardize those, then we're gonna move on from there to the probe API,
And then we're gonna try, you know, get our proof-of-concept first probe migrated,
those are 3 big steps, easier said than done, but I think that, like, if we put down… like, because we started each of those, and they kind of got caught up in details of trying to make it
perfect, and I think getting stuck and then losing interest in it. So, if we want to get back and actually
come to a resolution on them. Those are the steps that we need to take so we can go back to doing that.
I think 6 months is a reasonable timeline for it, and I'd be happy to spearhead that if we want to get back to it.
**Tyler** 21:45 It… Yeah, it wasn't…
I think it was more, like, we just needed a prototype. I don't think that there was really any details that were left. It was literally, like, somebody needs to go take a probe and find out what needs to get changed, and go through an investigation step.
Like… We're missing that.
We haven't even got off, like, that step.
**Mario Macias** 22:05 At this point.
Tyler, you mentioned previously that there are some probes in Otego Auto that aren't in Ovid. Do we know which are? Can we enumerate them? Not now, but at some point, so…
Maybe we can start integrating at the probe level.
as an easier… I mean, it's maybe a technical implementation detail now, not much to discuss, but maybe if we enumerate the differences, we can plan better how to
how to… Integrate them.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:43 I think the main advantages of Go Auto is the ability to use the Go SDK tracer. We have sort of an implementation of that, but it's not as,
as deep as when it's in Go Auto. So, if you're gonna add manual probes to your Go application, and we wanted to use the Go Auto as a better approach, although it does use BPF ProBrite User.
The implementation we have does not use BPAProWrite User, but it's not able to use the…
Global Tracer, as well as… The Go Auto SDK.
I think from the other probes, I think it's… it's all… I believe is superset.
actively wrong.
**Mike Dame** 23:34 And ideally, like, the probes themselves, if we get the types.
matched up and they're compatible, it wouldn't be a, it lives here or it lives there, like, probes could
in theory, go anywhere. They could be their own module that could be in a… you know, you could… I could have my repo slash my probe, or private repo, so it's…
But it's, yeah, coming back to that.
compatibility issue of different API types.
And like you're saying, the underlying see, helpers.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:11 So… I guess we can take two approaches. One, we can… One option is to…
Move the code around somehow, and make sure it's able to use in both places, so all probes exist in both repos, so if you want to go auto.
instrument.
Or…
like, we can move it on one repo and make sure we can have the probes in OBSource and make the Go Auto use those probes. Either way, I…
I don't know which one is easier to do, but…
And find the ones that are missing, and do that, or decide if we want to do it.
**Mike Dame** 24:55 Hey, Nicola, didn't you have a…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:57 I had a blind.
**Mike Dame** 24:58 It's one before.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:59 Yeah, I do have a plan. I kind of looked into one to see what I need to do. It's in one of the Go Auto issues, I believe. Let me see if I can find it.
Okay.
There was some…
Hmm…
Huh, I don't know where I found that.
**Mike Dame** 25:44 I don't remember which one it was, I thought you'd…
Said that you had, like, a…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:50 Unicorn…
**Mike Dame** 25:52 Like, you would almost even, like, prototype.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:53 Yeah, I actually… I actually added this onto an issue that Tyler opened. Let me found it.
So, here is it, here's the link,
And I put it in the dock.
So essentially, there's a couple of… yeah, that's the one.
So, there was a couple of, couple of issues that I need to make sure…
That exists. So one is the multiprocess aspect of OB needs to be somehow ported and go, otherwise we're unable to use the pros.
The,
The other thing is the, moving all… we need the ability to… because right now, GoAuto uses BPF maps on the BPF file system for all communication between the different probes.
Obi has, like, a custom map concept that allows us to share the maps without that, so that needs to be ported.
We would not like to rely on the BPFL system to be able to
Share data between the pros.
So, these things need to be refactored.
And… there's…
couple of additional things. Because of the multiprocess aspect of it, Obi keeps track of process information.
So this needs to be on the data structures that the probes use.
For OB, connection information is critical, so that we can do Things like…
Service graph metrics, and things like that.
So, OB does collect connection information, and that must be on every event.
So these things need to somehow…
be resolved in order for us to be able to use the C code. That's what I did at that time.
So there's additional functionalities that,
And none of these are optional, unfortunately, because, for example, the trace context propagation that's done using the common code does need pieces of information like this, the process information.
Or the connection information to identify and
Time that the packets are passing through.
which packet to extend, right? So it's not something we can just use optionally, right?
So while the code is similar in some aspects, it's also, like, evolved in a different area to be able to do this.
So one option is to…
make all these changes into the Go Auto code, and make some of the probes that exist there compatible, and OB vendors those probes into our source, through, like, a submodule or whatever.
Like we do this in Vela, we render all white.
The other option is to have
that go autoprobes use the OB underlying C code.
I don't know what… I haven't investigated that part.
To see if that's more feasible or easier to do.
**Mike Dame** 29:16 Yeah, I'm kind of wondering if the, just making GoAuto adopt the OBC code might be the easiest, easier path.
I don't know if Ron… oh, Ron, are you here? Do you want… do you…
What do you think of that Oh, maybe he's not here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:35 Okay, I see you.
**Mike Dame** 29:37 But that…
Okay. Do you think that that would be the easier way to start this, to at least unify the C code?
Underlying.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:50 a look at that? Yeah, I can take a look at it and see, scope it out, what it would be. I know both codebase as well, so I can take a look.
**Mike Dame** 29:58 Do we make…
**Tyler** 29:59 Can I ask the question, though, like, if you're gonna go that direction, like, why… why does Go Auto exist, then?
**Mike Dame** 30:07 As a… I mean, it doesn't need to be a separate repo, like I was… I was saying, it doesn't technically need to be. It could be merged into the OB repo, but keeping that
as it's… as long as it's not, tightly coupled to OB, the tool.
And so that's…
Having the distinction is a little clearer when they are separate, at least. But, you know, there's…
if you look at, like, Kubernetes, like, the API is underneath the main monorepo, too, so… That's sort of…
Delineation is totally possible.
**Tyler** 30:46 Yeah, I guess I'm just asking because, like, if the whole idea is so that GoAuto can then be vendored into some sort of, like, vendor's code.
And the probes from this repo are being vendored into that.
Why aren't the vendors just gonna vendor the, like, the probes from…
Obi, instead, and just skip the middleman.
**Mike Dame** 31:05 I see the probes as separate… and OB is another layer on top of Go. It's… probes are their own separate thing that, like, plugins plug into this framework, and this framework is built into OB. So…
if you think of probes, like, we could have a, like, Go probes contribib rep repo that's just probe file, like, probe packages, right? So, if we eliminate that, then you just look at what's the…
what is the tooling, the machinery that OB uses to manage and load these, and then OB makes decisions on top of that on how to… how to handle it. It's not just the C code itself, right? Unless I'm misunderstanding that, how OB works.
But that's… that's the idea.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:53 So if we added the required interface into Obi, that it can be easily rendered for that purpose.
Then maybe that resolves the problem.
Would that work?
**Mike Dame** 32:05 That's… that's what I was thinking originally with, like, the…
when I was first working on this, trying to take from, like, the probe API approach, which I see as kind of, like, the middle, right? We have the C code, we have the API, and then we have, like, OB's interface, and that's how they all plug into each other.
But that's, I think, the goal. And then OB serves as a really good example of how to vendor this, and we can encourage
other… other vendors, Splunks and Odegosas to Grafanas to build off of that in different ways.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:40 Yeah, I mean, I don't… I don't… actually, I'm not against adding, unintervention.
**Tyler** 32:45 Well, just like… I also want to point out that, like.
I mean, I'm not interested in, like, vendoring the Hotel Go stuff. I am interested in, like, working in the OB space from, like, the Splunk perspective.
And I think that, like, the Bayless stuff as well does that, where it vendors Obi, right?
So, like, I know Odagos is the one that's fendering
the OpenTelemetry Auto stuff, and so I think that's more of a question about, like, what Odagos is looking for here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 33:11 Yeah.
**Mike Dame** 33:13 Yeah, I mean, we're looking for tying it into… we kind of have our own…
Different opinionated control plane for,
using the Go Auto, the same way that OB kind of builds a control plane for using
with the Go Auto, so we don't… we're not interested at that level, we're interested at the level below. Like how you have the OTEL API and then the OTEL SDK, right? You can… you can build your own SDK that is still going to rely on, like.
the API underneath, you know, just fork the default Go SDK and build off of that.
kind of where I'm coming from. You… you… maybe that doesn't… I mean, that's not technically correct. You know that better than I do, Tyler, so… but that's at least where the…
The intuition is coming from.
**Tyler** 34:00 Yeah, I'm just… but, like, if Otagos is really interested in the probes, right, and, like, they have a different idea of a control plane, like.
Like, why can't they just vendor… why can't you, like, vendor in the probes, though, is what my question is.
**Mike Dame** 34:15 Well, that's the idea, is that the… the framework for the probes… I mean, we have plenty of our own unique custom probes that we've done for different libraries that also… that aren't in either one. So that's using Probe as an API.
And we, like, the idea really being, we also do have our own fork of Go Auto instrumentation right now, because we've added extra features and stuff, too. And that's a pain for us to maintain, and it's, you know, trying to add features in. If that was to be forking Obi, it's adding features into, like, a deep
level of OB going, like, not, you know, two layers deep there. So what we would really…
**Tyler** 34:57 That's what I'm saying, though, is like, if we're going to switch to Go Auto to use the OB probes, right, is that actually going to work for you?
**Mike Dame** 35:05 I think that that, you know, getting towards what we want the ideal world being for us is that we, I think, would react to the OB probes.
going into Go Auto, probably have to make some changes in how we fork Go Auto, but it would contain the surface area of that to be not having to react to, now we've got to fork OB, or vendor OB entirely.
Because I… we kind of see ourselves sitting at that same layer.
as Obi, and so we've kind of done our own
That's the layer that we branched at.
**Tyler** 35:39 like, I guess I can't speak, so I don't know, but, like, it sounds like you're adding probes underneath that layer, as well as above the layer you're consuming on top of the Go Auto API, right?
So, if we change…
everything below the interface layer of GoAuto, is that actually going to work for you, I guess is my question.
**Mike Dame** 35:57 Yeah, because we can… Change how our probes load in, but it's…
what I want us to get to is having much less of a different fork, so that we can contribute a lot of stuff back to the Go Auto framework.
Which isn't totally possible right now, but the probes themselves, I think… I think it would be our own thing that we could catch up on, but it would be a lot more work to catch up on if this was, you know, bundled in to Obi, and…
That's… that's the idea, at least.
Maybe it's not totally clear.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:41 Would it be possible for you to scope out and say which parts are critical?
That you use as an interface, so we know exactly
If you're gonna try to refactor something or make it work.
**Mike Dame** 36:59 Yeah, I mean…
pretty much what we do is we call new instrumentation on a process. So we have our own process manager, and that's really the layer that we hook in, is we call, like, goauto.newinstrumentation.
kind of the… like I'm saying, the exact same layer that Obi hooks in and calls, you know, instrumentation, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:20 I'm guessing you need, something then on the events to come back through, right?
**Mike Dame** 37:25 Yeah, and so we have, like, our own CRDs that we use to keep track of everything, so that's where our
that's literally where we start to differentiate from OB, whereas OB is built as a damage set, and, like, a self-deployed agent, and we build a lot more of the, like, control plane pipeline around that.
just different approaches, but that's why that's a good layer for us to hook into, and it would be too much for us to bundle an Obi. And I, you know, this isn't just to be selfish about Odagos, I really am genuinely thinking, like.
in terms of other vendors, other new companies that might want to start up, this idea, I want to encourage that, you know, differentiation for people.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:15 Yeah, absolutely.
Is it, like, really… I mean, I'm just asking to see how do we get started on this faster,
would it be possible to give a small example, like, some dummy Go project? This is how…
we want to use this, here's how I do go mod imports this thing, this is what we do.
Something that just prints on the screen, or whatever, so that… then we kind of know what exactly you need, and…
I don't think it's…
**Mike Dame** 38:45 Yeah, so you need kind of, like…
show, like, come up with a fake, you know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:50 Yeah.
**Mike Dame** 38:50 project that kind of shows the similarities between O2 Snow Bee. Yeah, and I kind of think that that's what the,
like, the Go Auto image that we were building kind of did, but that was a very basic, you know, that's literally just a command line, calls new instrumentation, but you could build… you could do an operator SDK init, and call Go
new instrumentation, and then start to show an example there of, like, use a CRD, that would be pretty easy to whip off.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:23 But the Go CMD now, the Go AutoCMD should have the total, kind of the total interface to what's needed.
Behind.
**Mike Dame** 39:33 Yeah, I think so. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:34 Okay, fair enough, yeah.
**Mike Dame** 39:36 And that's the benefit that I like. The one thing that I do like about publishing that image is that it serves as kind of the, like, minimal viable example of using the library.
But I… I do wanna, like, if this is now something that…
I hate to be the stick on the project, but I'm happy to take this up and really try to push these things more and revisit some of these issues that have gotten kind of dusty and
Because, like, I want to see both of these projects succeed.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:16 Sounds good.
**Tyler** 40:19 Yeah, that sounds great. Yeah, well, yeah, keep… We'll keep talking about it.
you're coming to all the meetings, so we'll see you in all the meetings, Mike. But yeah, yeah, let's keep up on that time.
Okay, we are 20 minutes left, so let's jump on. Antonio, welcome. Looks like you're a new contributor.
And you're interested in the project, and you're looking for issues?
**Antonio Jimenez** 40:43 Yeah, that's the idea. So, thank you so much for having me here, so interested in OpenTelemetry and learning about eBPF.
So if you see any simple issue, let me know. I want to learn a little bit more about the code. I will try to review some pull requests and get a speed up here.
Thank you, team.
**Tyler** 41:03 Yeah, reviews are always welcome. They're really helpful to jump into the code. Cleaning up,
any sort of codebase, wherever you find it, I think is great. We need a lot of help there, so yeah.
Okay, I did want to go through, at the start of the month and go through our goals, that we've got laid out and see if we can get a little bit of an understanding of our progress here, maybe even provide a status update to the community.
So, on the roadmap, maybe we'll just go through this, I've got the first one, so the stable OB 1.0 release.
I have not prioritized that yet, that is definitely more to do with the configuration, but I did see somehow this binary distribution being a part of that, so I'm starting to tackle that first. So no, no update on that one.
Additional protocol support, this is something, Mark and Nimrod, I don't know if Nimrod's on the call, are the sponsors for. I don't know if there's any update here.
**Mattia Meleleo** 41:56 He's on vacation.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:59 We can take off MQTT, that was merged.
**Tyler** 42:03 Thank you, awesome.
That looks great, yeah. So, did we have…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:13 Hey, Steven…
**Stephen Lang** 42:15 Yeah, so non… non-go is done, so the generic address is.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:19 so I'm cold.
**Stephen Lang** 42:19 Oh, go.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:20 No one needs to be finished, yeah.
**Tyler** 42:21 I'm looking forward…
**Stephen Lang** 42:22 I'm working on Go, but right now, so that will come soon.
But yeah, the initial IQTT spot is, is done.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:35 Okay.
**Tyler** 42:39 Awesome. Thanks, Steven. Any other, protocol support updates on this one?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:47 I think Nimrod did, couchbase.
**Tyler** 42:53 Yep, yep, okay, we've got that one done, as well. So that's the one of the 11, okay. And then, Steven, you're also working on AMQPE, right?
**Stephen Lang** 43:01 Yeah, that's next.
Nimrod, do you know, so Catchbase is based off of the Memcache protocol. Do you know if there's any.
**Tyler** 43:07 He's a…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:08 He's not here.
**Tyler** 43:09 He's on vacation. Sorry, he's out, yeah.
**Stephen Lang** 43:11 No worries.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:13 Yeah.
**Tyler** 43:14 But yeah,
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:14 Yeah.
Sorry.
**Tyler** 43:18 Maybe Mattia also knows, but yeah.
**Mattia Meleleo** 43:21 Something, yeah, not everything, but yeah, maybe I can answer.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:26 I mean, is it a Couchbase protocol based on Memcached, and does this mean we have Memcached support as well?
**Mattia Meleleo** 43:33 Yes… I think it's a superset of Memcache.
And also there is support for another API layer.
which is HTTP-based, which is SQL++.
And that one, is also… like, we know it's catch-based by some headers, if I recall correctly, but there are some other products that, that use this protocol, like,
I don't remember the name, it's some Apache project.
**Stephen Lang** 44:13 not CouchDB, is it? Because Couchbase was based off of, it was Memcaching CouchDB, or just Couch, something like that.
**Mattia Meleleo** 44:24 No, those are two different projects. I… I found.
**Stephen Lang** 44:27 Yeah, I know, so Couchbase was formed off the back of those two projects.
**Mattia Meleleo** 44:31 Oh.
**Stephen Lang** 44:32 And they added.
nickel, or SQL++. So I don't know if that was also…
if, like, Couch supported that query layer as well, or not.
But yeah, I was just wondering with Couchbase being added, because it was kind of based off of other previous products, if we could get, you know, some other protocols, or…
Something for free as part of, you know, that work that was done.
Yeah, I think so. We can, ask Nimrod when he's back, but yeah, I think so.
**Tyler** 45:07 Cool. Alright, moving on, support for .NET. Rafael, I see you on the call. Any update on this one?
**Rafael Roquetto** 45:14 Nothing yet.
So, on the pipeline, yeah. Well, you're working on it, you're working on it. Kinda, kinda. I was gonna talk about it when I explored the point, but yeah, I can,
Yeah, alright, so I can maybe, scratch them together. So, I added this bullet point here, updates on trace parent handling. Earlier this month, or last month, there was, like, a pull request, that was merged, that basically, so this is part one, doesn't really affect .NET, but it…
Basically, at the socket, tracer level.
the one that injects the transparent header into the HTTP requests. Now it detects if the header exists before trying to inject it, otherwise we end up with two trace parent headers, and this was causing problems. It also detects
It also parts the headers if it exists, and then it does… either it will use that information as a gospel, like, as the transparent information, or if it detects that the parent of these transparent is the same, like, same header, then it will,
override this header with a new one, so it's not duplicated. That application happens when you have something like Istio or NGINX, that they just forward the incoming transparent header verbatim to the client, so when you finish fermenting one of those proxies, you end up with the same header twice.
That breaks the spend. So now, if the second header is the same as the incoming header, we detect that, and we override that with a new one. So then we can properly instrument, this process as well. So this is, like, all egress.
What I'm doing now, and that's what affects .NET is ingress, so… we are ready?
Parse.
The tree sprint on ingress.
In the generic tracer.
But what we're trying to do now is to inject the trace printer on ingress if it doesn't exist, and we have this information available because we generated it, or whatever.
Because once it hits the application.NET will see that transparent, and it automatically propagates that trace parent forward. So that… that kind of, helps with context propagation with .NET, so that's the, that's what I'm…
working on at the moment. It's gonna be a few days still, because the verifier is always giving me…
the week. But, yeah, it's, yeah, that's the update for .NET, I guess, together with this.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:50 Yeah, so once we have that, I mean.NET naturally propagates TraceParent, so if it's not the first service, if transparent is applied, it's already done, we don't have any work to do.
But if it's not… if it's the only service, then we probably want to add this header so they can do it.
**Tyler** 48:08 Right, right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:09 So, once we do that, I think that support should be done.
**Tyler** 48:13 Cool.
Yeah, I think that's simpler than I initially thought, even, which I…
**Rafael Roquetto** 48:18 Pain was less.
**Tyler** 48:19 Perfect.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:19 Yeah, right? Yeah, exactly.
**Tyler** 48:24 Okay. And then…
Another epic was the OTEL SDK API integration. This is something that Nicola took on.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:36 Yeah, so I started looking at, the last bit, which is, supplementing the telemetry,
And, because…
the, the other stuff sort of works, I have to look at the, like, the exemplars and things like that, but…
And I've hit sort of a wall with deprecation of the… of the span events. That's what I learned yesterday that span events will be deprecated.
So let me explain what I mean. So, what we wanted to do is, let's say you have an OTEL instrumented application, so it's already handling everything, transparent and whatnot.
However, we know that it cannot correctly determine the total request time, so it can only do the service time.
Well, Obi can do the total request time, so it would be nice if Obi can be, like, sort of the background layer that supplements this…
Timing information with the correct time.
So I initially thought about using, span events for this, because they can be independently shipped
from OB, and it simply will be correlated in the back end.
That will contain the same trace ID as the SDK, so it will naturally work well.
But apparently, I learned yesterday that span events are being deprecated, in favor of log events.
So, I'm not sure where that leaves us.
The alternative is to produce an additional span, using the work that Raphael is doing, to kind of fake a span for the hotel SDK.
And then we'll have two service bands, back-to-back, and I don't know what that looks like for every backend.
I think certain ones will handle it, I know Jaeger does, and Tempo do, but
I don't know about other backends, and that might cause issues.
**Tyler** 50:36 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:37 So I'm of the mind of doing it… yeah. It seems like the process of fully removing the span events…
Will take a while.
So maybe we should use pan events, give it a shot.
I think that's.
**Tyler** 50:50 That seems like a reasonable approach. It hasn't been deprecated yet. I think you can cross the bridge, when it does. I think also log events may be more well-defined, so we could look into doing something like that. Yeah. So, yeah, I think that I would probably just go in that direction for now.
Okay. It's working. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:07 So that's… that was my plan. That's… I also put it on the agenda, I wanted to discuss it here, so that solves that, so we don't have to do that. So I'm gonna prototype with span events, see what happens, because that's just a natural thing for this reason.
**Tyler** 51:22 Yeah, and I think in the deprecation process, it's extremely murky waters right now, but, like, there is some sort of guide to do this migration to try to help all use cases, so I think you'll have more information as the deprecation process happens. So, I think that's… let's just go there, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:40 Okay.
**Tyler** 51:42 Okay, moving on. The standalone binary package, distribution, it's going pretty good. We have, I think, the first phase where we actually get some sort of binary up, not attestation and not the packaging of the, into, like, distribution packages.
It's going, well, there's this…
Oh, this is, 90% done from Robert. He's got the containers being signed right now. He just hasn't been able to verify it. Looks like there's something weird, in the verification process, so, he's still working on that. He's out this week, though.
I'm working on the gated release pipeline. I, owe some feedback on this. I did want to actually maybe ask,
Steven, on this one, Had a question about.
**Stephen Lang** 52:36 the glove, right? Yeah.
**Tyler** 52:38 I didn't see this. Yeah, but this… this, is this it? Sorry.
**Stephen Lang** 52:44 Because there's also, yeah, where it says you might want to check.
**Tyler** 52:48 Yeah, yeah, yeah, okay, thank you, yeah, yeah, this is it, yeah.
Yeah, so I didn't quite understand, but what you're saying is essentially, like, we have different workflows for different things that will get triggered off of a tag, and, like, right now, like, this one will just go even if the tag's invalid, so…
I guess maybe,
Is there… yeah, is your suggestion to just unify them, or to also take the validation I'm doing here and put it there?
**Stephen Lang** 53:11 So, I think what you're doing is great with the gated release pipeline, but you have effectively a race condition here, which is there's two separate workflows which will execute in parallel off the same trigger, which is when you do a git push of a tag with V1.2.3, both your gated release pipeline
And this published Docker Hub name, or, you know, whatever pipeline will, fire at the same time. So your gated release pipeline is going through, doing all these great checks, making sure everything passes, and then it only goes to the release at a certain stage. Whereas the Docker Hub one just doesn't care, it's like, oh, great, you know, new commit, ship it.
So I thought that you probably don't want to publish the actual Docker image itself when you're using Semva.
Unless it's past those same tests. So my suggestion here is likely to remove this, trigger.
from that Docker Hub workflow. You might still want it for main, but to remove the tag trigger, and instead call this workflow off of the end of your sequence on the gated release pipeline, so that we only tag Docker images
Once, you know, they've passed effectively the same criteria that you have on your gated release pipeline. So that was the suggestion. And then I thought maybe you would just want to check for this tag pattern to see if there's any other workflows.
Which would do the same.
**Tyler** 54:34 Yeah, that's… that's great. I think… yeah, thanks for catching that. That makes a lot of sense to me, once you pointed it out. I didn't realize you wanted to do, like, the… the call, approach on that, and that's… that was my misunderstanding, so, like, I… I think that's a great idea. I'll… I'll look into doing exactly what you just described. So, for all of them, not just this, or verify that this isn't the only one, so…
**Stephen Lang** 54:54 Yeah, yeah, it's easy to miss because this, this doesn't execute on PRs. You only see it when you, when you've merged onto main, right?
**Tyler** 55:01 Yeah.
**Stephen Lang** 55:02 And then the other one, the glob, yeah, that looks good, as far as I can tell, but the only thing is.
I tried to use this tool to test the glob, and the tool doesn't support the plus character.
**Tyler** 55:14 Yeah, I found this.
**Stephen Lang** 55:15 So it seems to be, like, a GitHub-specific blob syntax, so…
What you might find is the first time that you do try and run this pipeline.
If the pipeline doesn't trigger, it's probably this long.
In which case, just go back to the asterisk, but yeah.
**Tyler** 55:34 That was my idea. Also, that's why I added the, like, manual override, so you can… you can literally manually kick it off for that, like, because I gotta worry that that or something else is gonna mess up, so I… yeah.
**Stephen Lang** 55:45 Yep, the worst that'll happen is it just won't trigger automatically.
**Tyler** 55:48 Yeah, yeah, exactly. So, okay, yeah, thanks for the review, I'll, I'll, work on the follow-up on that one.
Okay, we are… 5 minutes left,
maybe I'll go about this another way, and if there's anyone on the call who's got another issue left in the rest here, or assigned as an owner here, and you would like to provide an update, or if you have an update, would you just go ahead and let us know what you're working on?
It's also fine if there's no update. I know this is also a lot of busy stuff.
**Stephen Lang** 56:25 Mario is… Nice.
**Mario Macias** 56:26 Yes, sorry, I was mute. Yes, I'm working also in this improved service metadata, we're not running in Kubernetes, to extend it to Docker.
The… the feature is almost done. I would like to add extra… To add extra attributes.
or improve the way the service name is… is gotten, for example, for Docker Compose.
But yeah, it's at 60%, more or less.
**Tyler** 56:57 Oh, cool. Okay. Yeah, this is awesome. And so you,
Are you looking at the VM stuff as well, or are you just looking at the Docker, post stuff?
**Mario Macias** 57:06 Oh, at the moment, only at the… on Docker, yeah, later.
**Tyler** 57:10 Cool.
**Mario Macias** 57:11 I think each platform should be a… A subtask.
**Tyler** 57:17 Okay, yeah, alright. No, that sounds… This is great, okay.
Yeah, I just had another question from that from earlier, but… Yeah, thanks, that's a great update. I've added this to the in-progress, and so we'll keep track of that.
Okay, cool.
Go ahead, yeah.
**Giuseppe Ognibene | Coralogix** 57:38 Mine is in progress, the extended network matrix.
**Tyler** 57:42 Oh, cool. Okay, awesome. Yeah, thank you for letting me know.
**Giuseppe Ognibene | Coralogix** 57:46 Thank you.
**Tyler** 57:50 Okay,
I'll stop sharing my screen here. This is great. There's a lot in progress. I think our… we can update our status on this one, after the meeting, and then…
Yeah, if there are folks that are also working on things in there that I didn't capture as in progress or need updates, please just ping me.
Asynchronously.
And, yeah, any other topics before we close? I know there's more on the agenda, but maybe just, like, any quick shout-outs or anything like that that we needed.
**Rafael Roquetto** 58:19 Real quickly, not important, but since I got Mattia on the call, I am raising a PR, I'd rather raise a PR, Mattia.
that just turns those UBPFFS, errors, when it's now mounted, into warnings, just because when we deployed it to some people who started, oh, there are errors going on, and they got a bit spooked. So, then let me know your thoughts. I'm gonna paste the link to you.
**Mattia Meleleo** 58:41 Yeah, sure, it's fine. I didn't even,
I remember that I was… I set them to error. It's fine.
**Rafael Roquetto** 58:47 Yeah, that's okay, not blaming you, it's just giving you context.
**Mario Macias** 58:51 No.
Also, I'd like to mention a super quick thing. Regarding this, removing the eventually by the standard required, it's great, thank you for doing it, but as probably when it was merged, someone else merged another PR using the old one, so now main is broken.
If… if someone fixes today, it's fine. If not, I will fix it tomorrow morning, first thing I will do.
**Tyler** 59:18 look into that. I… I'm… I'm guilty of, that.
**Mattia Meleleo** 59:21 I wish you said.
**Mario Macias** 59:22 No, no, no problem.
**Tyler** 59:25 Yes.
**Mattia Meleleo** 59:26 I pushed a fix for that, like, one hour ago.
**Mario Macias** 59:28 Okay, okay, amazing, thank you, thank you.
**Tyler** 59:33 Awesome.
Alright. Thanks, Mattia. I appreciate that. Okay, everyone, we're coming up on the hour. I want to be respectful of people's time. Thanks, everyone, for joining, thanks for the conversation, we'll keep progress going, and I'll see you all in a week's time.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 59:46 Bye.
**Florian Lehner** 59:47 Okay.
**Mattia Meleleo** 59:48 Bye.
**Mario Macias** 59:48 Did I…
