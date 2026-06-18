SIG: eBPF instrumentation
Date: 2026-06-17
Duration: 67 minutes
============================================================

## Zoom Recording Transcript

Pellared 00:01:38 Hello, how are you?
Mike Dame 00:01:42 Hey, hello.
Roy Reshef 00:01:47 Hey, good morning, good evening, wherever you are.
Tyler Yahn 00:02:36 Hey.
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:38 Hi, everyone.
Rafael Roquetto 00:02:40 Hello.
Tyler Yahn 00:02:43 How y'all doing?
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:46 I'm good, good.
Roy Reshef 00:02:49 Good, and yourself?
Tyler Yahn 00:02:53 Doing well, doing well Looks like we got a… Pretty full set of people here.
For folks that haven't yet, please go ahead and add your name to the attendees list.
And if you have agenda items you wanted to talk about, go ahead and add them there as well. We could probably jump in here, start sharing my screen.
Maybe.
That's Zoom. Okay, cool. Awesome. Well, welcome everyone. Starting us off, Rob, last week, I think this is a copied one from last week as well, so maybe it was 2 weeks ago we postponed this, discussion this week?
If you wanted to jump in here…
RC Robert Cowart 00:03:56 sure, let me, oh, is it okay if I… I'm sharing on my side?
Tyler Yahn 00:04:06 Not a problem. Yeah, let me stop really quick here.
RC Robert Cowart 00:04:10 Just so I can… Drive a little bit easier.
Nope.
Tyler Yahn 00:04:17 Do we have, Giuseppe? Yeah, Giuseppe's here, okay, cool.
RC Robert Cowart 00:04:20 There we go.
Alright, so, the… the first thing that I… I commented on, let me cover that first, And mostly the… the gist of… my comment.
here we go, getting down here. There was kind of two sets of metrics, right? Some of them were more, I would say, TCP stack on the endpoint, and some of them had to do with, like, the round-trip time of a conversation. And, this is actually something, historically, we went through, where we… You know, for the schema that we've used historically in our company, that we had planned to redo, just because, you know, you start to realize, like, TCP round trip, and then UDP round trip, and then based on where you're looking on the network, you know, where you're actually observing the traffic, You realize there's all these different kinds of points, and soon you have, like, 150 attributes?
that means some version of the same thing, but basically come down to something as simple as latency and jitter. You know, jitter being when you have, you know, if you have multiple measurements.
And, And so it just made a… makes a lot more sense to be able to do a, a more simple metric, that's kind of what I suggested at the bottom. I'll talk through some of these in a second, but what I kind of suggested in the bottom, which was the… a more generic round-trip latency and jitter. Now, arguably, you could also have one way, also. There are, you know, some technologies out there that'll… that'll… focus or give you more, like, one-way measurements. Like, Cisco IPSLA is an example of that, and other vendors that have, end-to-end measurement stuff, CDN was one that, comes to mind.
That also could have one-way measurements of these same things. But then to have some additional things that talk about the observation point.
And I'll talk about what these are in a minute, and then, you know, what was measured.
And then… what is the, like, the measured resources role? And you'll see what I mean here in a second when we kind of walk through these.
So, The basic thing is, let's just talk about, you know, end-to-end, call it like a request response that, you know, is an application.
it's gonna go through the network stack at the endpoint, perhaps over multiple, you know, routers, switches, firewalls, devices forwarding traffic, essentially. Hit the network stack on the other side, go through the application and back again, right?
And so, depending on where you measure, you might have different, You know.
you could focus on different parts of the network connection, so… or of the overall round trip conversation. So where looking at the whole thing might include all the way network and application, so a complete round trip. If you're actually just looking at, and Linux can provide some of these, we'll look at an example in a second, but, like, the actual network itself that has nothing to do with the application. TCP Handshake is a simple example of that, where if we, you know, initially on the three-way handshake of TCP, we send a send packet.
and because this is a Layer 4 negotiation, the application really isn't involved here. This is just about the two network stacks agreeing that they… that they are establishing a session between them, and so you get a more pure network-only version, and that send to SENAC would tell the client in what it thinks the latency is.
Now, in the second and third part of the handshake, where the server will send that Synac back after a send, the client responds with an ACK, now the server knows what the latency of that is, too. This is actually the most pure network… Only latency, because nowhere involved is any, any type of… I'll call it delayed acts, we'll talk about that in a second, as well as, the application's not involved at all. So this actually gives you the purest version or understanding of what the network latency is, at least in that point in time, which is a critical point. While this is a great measurement, it's only then at the handshake. So let's say you have a really long-lived session.
You know, like, typically, for example, systems that cluster the different nodes in the cluster will maintain long-lived sessions between them for state and replication and all that kind of stuff. Might be… might be sessions that are months old, even, they're so long-lived.
And so in that case, you're, you know, that handshake could be completely invalid, that latency. So you want latency over… the history of that connection, or more specifically, more recent history specific to those requests and response you're measuring. On Linux, there are a couple options you have to do that. The one that was suggested originally was this smooth round-trip time microseconds.
Here, the issue with that has to do with the way that TCP works. So, as some of y'all may be aware, TCP, Connection Oriented protocol, you should be getting a… an acknowledgement back.
When a packet's sent. But for efficiency's sake, not every packet's acknowledged. So… and so depending on the… the time, the timing of that.
it's not always the best metric to use, because the round trip time can be really, bloated, I say, or exaggerated, because there might be packets that are… that are skipped, and not everyone's acknowledged. And so there's actually this other metric I suggest using, which is this minimum round trip time.
So, anything TCP that's trying to get on a longer-lived connection, especially, they're trying to understand network latency.
this… and it's kind of funny, actually, it's RTT min is the data point, but you call min-RTT function to actually get the value in Linux. I don't know why they couldn't maintain some degree of consistency in naming, but that's how that is.
But the thing being is that, it actually looks over a 10-second window as the Linux default.
and will return the lowest latency that it's seeing. And so that makes that a little bit more of an accurate measurement to use, was the suggestion there. But then I just go on to point out that, you know, depending on what you're doing, there are different things, like the application itself.
you know, I think we see this in traces, where an HTTP call is made, and the request eventually arrives back, and that was the application's perspective of that happening.
But there are other points along that path that could be measured, because even this simple example is literally taking multiple steps through. And this is more or less walking through, like, if I'm… say I'm measuring at the network stack here, so in other words, I'm, you know, sniffing on the interface like Merman does, for example, I… or even those, those metrics from the Linux kernel, the SRTT and the MinRTT, they would be actually measuring from the client network stack, but are measuring the entire server end-to-end.
And so I've kind of given these some names, but, you know, ultimately they'd have to… I would recommend that these, you know, get some other name for the type of, of place that's being measured.
Vivek Akupatni 00:12:41 I've been… even on.
RC Robert Cowart 00:12:42 On the server end, and again, this is something that the Mermin stuff will do, like, when it connects to a network interface on the server side.
It could actually, then, you could use this measurement to derive just what the server application latency is.
Rather than going into the, you know, more detailed instrumentation of the code.
And so, I'm not gonna go through all of these. The point just being, there are different places to measure on the network. Even in the middle, like, a lot of people don't realize this.
Vivek Akupatni 00:13:12 but there are.
RC Robert Cowart 00:13:13 technologies, like Cisco Application Visibility and control.
Or even increasingly, we're seeing more and more, like, white box switches that run things like Sonic as an operating system, where you could deploy your own containers onto it. For example, something like a Mermin or other type of container that could also be measuring the traffic latencies at any of these hops as well.
And then you can start doing math on the different measurements you have to even derive, like, hop-by-hop latencies and things of that nature to really try to understand or highlight where potential network issues might be. So anyway, the main thing I was just trying to point out here is that, like.
There's lots of different points to measure from, there are lots of different things, like the two different ends, or even both ends, you know, what the metrics are, etc. And so that ultimately could be derived then down into these five attributes for round trip.
And perhaps there are a couple other values for, like, measured resource or, what have you, but, So I was kind of suggesting something along this way. I don't want to, speak for, I'm sorry, was it Giuseppe that wrote this? I forget the… I don't have all the names matched up with the GitHub handles.
Giuseppe Ognibene | Coralogix 00:14:43 Yes.
RC Robert Cowart 00:14:44 Yeah, yeah, so I think you… so I think you agreed with the… the use of the metric there, and also, this type of approach to the… the round-trip stuff. And as I said, there's probably… it's probably fair to also say that there should be one, one-way… similar one-way attributes as well.
I just didn't draw those examples out here.
So I'll pause and see if anyone had any… wanted to comment there further.
Giuseppe Ognibene | Coralogix 00:15:14 from my side, I agree with you regarding the generic approach.
I left some comments regarding, for example, the macro savings should be savings.
And, the immediate resource.
should not overlap between them, because for, aggregation is, it can be a mess, but in general, yeah, it's a good approach. And also for the, TCPRTT, maybe the RTT mean is a better metric compared to the SRTT.
RC Robert Cowart 00:15:50 I actually had a question on the units for, for those fields. You mentioned there were some that were seconds already.
Was it here? Yeah, Heroes, right here, was your thing.
I mean, I'm personally… I'm not gonna say I'm opinionated one way or another. Traditionally, I think on network devices, those get reported in my… those type of things are gonna be reported in microseconds. Like Cisco IPSLA, for example, it'll either report it in milliseconds, or if the, if actually, if all the devices have, are synced with an NTP server, then they can report it in microseconds. But, obviously, if you have something that's, like, 70 microseconds, that's gonna be a pretty small decimal number reported in a seconds field, but… if that's how it's done elsewhere, I don't really have a… like, I'm not having a dogmatic approach, whatever's normal, you know?
Giuseppe Ognibene | Coralogix 00:16:58 Yeah.
As far as I know, it's 7. It's 7 for the San Monday Convention. Only…
RC Robert Cowart 00:17:05 Yeah, yeah, got it. Okay.
The only other thing I wanted to say on this one, and I didn't get a chance to write this comment up, But… You know, we do have some efforts going around to kind of get the network SIG rebooted, and I think is making some progress. And one of the questions raised in the context of that is, what is system, and what is network?
And… In my viewpoint, anyway, it is… I would think, like, the, what I'll call it, the network stack of an endpoint.
and this is, like, meaning, you know, the various layers as far as what is the endpoint device actually seeing, so not something that's forwarding traffic, not some type of protocols that are… supporting the establishment of traffic, but the actual, you know, what's going up and down that OSI stack on an endpoint.
I would agree, actually. I would have said that's probably the right space of delineation to put them in system. So I do think that these type of metrics do make sense in system, to me, if that… if that's the delineation that ultimately ends up being taken. The only thing I was going to point out on these TCP ones is that you know, even, like, on a Linux server and a Windows server, I know, is somewhat… can be somewhat similar, but definitely on Linux for sure, is that in the kernel.
they just pretty much borrow the same attributes that had long existed in SNMP.
And expose those, you know, via the… whatever the net… whatever file system and sets of files and stuff that you can fetch some of these metrics from. And, So, in reality, what I think these are trying to borrow from, or at least most of them, is essentially what's RFC 4022, which is kind of what specifies all of these I'll call them endpoint TCP metrics, you know, like, in and out, well, those are in and out errors, but here, like, in and out segments, in and out bytes.
Retransmissions, that's… that's essentially the one you had here.
Right. So the only thing I would say about these, I feel like retransmits, resets, those things match here?
As, like, an endpoint global metric, if you will.
But then, like, connection duration, that's specific to one single connection.
Handshake duration would be specific to one single handshake, or, you know, of one connection.
So I don't feel like those belong here.
Well, Handshake, we would… we would actually be taken care of with the, those fields that, you know, if we went the way of the ones I suggested below, we'd be handling with probably, with… that style, that, like, handshake duration. But, It just felt like the ones that are specific to a single connection probably don't belong here, would be my call-out.
Meaning, like, not under system, for example, right?
But having said that, I can… I can write up more. I know I was babbling there a bit. I could write up a little bit more, Concrete response just to those as well.
Giuseppe Ognibene | Coralogix 00:20:55 Time moment.
RC Robert Cowart 00:20:57 The only thing I was gonna just say here, and what I meant by mentioning this here, is I actually think this list that you started Needs… probably needs to be a little bit longer just to be complete.
Like, you have some of the items from RFC 4022, but not all of them.
Because I don't think those were pre-existing. I couldn't find, Maybe I didn't look hard enough, but I didn't see them when I was looking.
Sorry.
Giuseppe Ognibene | Coralogix 00:21:31 I will have a look to… to the Red Sea.
RC Robert Cowart 00:21:35 purple.
Giuseppe Ognibene | Coralogix 00:21:36 Oh, thank you.
RC Robert Cowart 00:21:37 That was… that was pretty much all I wanted to share, so…
Tyler Yahn 00:21:50 Cool. Okay, well, that sounds good.
it sounds like we have some homework on that one, then, I'm guessing?
RC Robert Cowart 00:22:01 Yeah, I'm happy to write up the… what I just said about the ones I hadn't written up already, and I'll try to get that done probably tomorrow, so…
Tyler Yahn 00:22:11 Yeah, sounds good. And Giuseppe, you're gonna be taking a look as well?
Yeah, okay, cool.
Giuseppe Ognibene | Coralogix 00:22:16 Yay.
Tyler Yahn 00:22:19 Awesome. Alright, cool, let's, let's jump back in. I think, start sharing my screen here. Roy, I think you're up next.
You wanted to talk about container language detection, doesn't follow, process Tree.
Roy Reshef 00:22:40 Yeah, if you're sharing, you can follow the link. I opened this issue… last week.
We have seen, I mean, We deployed using, bailout survey mode, but it… under the hood, it uses, language detection in OBI.
And we had a bunch of containers that… they're a startup, they usually have a startup script, and sometimes this script spins up another script, and eventually they launch an application, which could be Java or Go or whatever.
And we noticed some inconsistencies in the sense of… We had a deployment of, like, 3 containers of… you know, the same pod, and a few were detected as Java, and a few as generic, and here I created… this is, I mean, a very sample, container image that does it, basically. It's a script that sleeps for a few seconds, launches another script that sleeps for a second, and then launches a stupid Java app that does nothing.
And… and I could replicate it. I could see that two of my replicas here were detected as Java and one as generic, and I had a quick chat with Nikolai about it, and apparently it has to do with a… With the order that we are identifying the processes and attaching them to the container.
We don't follow the process tree in this sense.
And this is… I mean, you have even more complex use cases that are a bit frowned upon or not encouraged to spin up multiple processes, and then what do we do then? That's something that I, referred to in… in that, feature request that I submitted the week before.
for porting the survey mode into OBI, but even… even if we stick to a single process per container.
We need to make sure that this is consistent.
Nikola Grcevski @ Grafana / OpenTelemetry 00:24:44 Yeah, I can shed some light in here a little bit more. Yeah, this is definitely a bug.
I… I think… I mean, the simple fix would be to… Okay, let me explain. We do have multiple processes, but at the end of the day.
From an application observability standpoint, there's just one service that's reported for this pod, right? So we know this is server, I don't know.
card service, right? And this cart service inside may have, like, 5 different processes.
So what happens is that if cart survey has started, then it has these wrapper scripts around, typically what we'll find the… from the pod information on Kubernetes, we will find the containers and so on, but now we have to match process information to a container.
So we do scan of the processes that are running.
And it's unpredictable in which order we get them, back from the… From scanning the processors.
So we may find, first, the bash process, and then the Java process, but in the other, there's cases where we may first find the Java process, and then find the bash process.
And the way it is updated is that once the container metadata is matched between the processes and the service, we establish that. If a new process also has this.
Same container metadata, which is in this case, that will override that information with its own information.
So, last one wins, sort of.
So my first proposal when I discussed this with Roy was to Actually, try to find a child-parent relationship and treat the innermost child as the one that we consider the… The process that will be… Associating with a service.
So that if you have, like, typical cases, maybe, like, an NPM, start, and then launches number of things, eventually launches Node at the base of it. Same with this kind of thing, where people wrap scripts to a script to a script, and eventually the service starts.
I don't know if that's… Gonna solve all cases, but it's a… an attempt.
Otherwise, the situation gets more complicated.
Because at the end of the day, we have to report a language for the service, and the question is, if there's multiple processes on a single container, which one do you report?
Yeah, I don't have an answer to that. We got to pick one.
Tyler Yahn 00:27:36 Well, is there a way to… so… yeah, hard problem.
My other question, though, is, like, are we… are we reporting this right?
Like… Right now, what do we use? We use, like, the telemetry SDK language or something like that, right? Yeah, yeah.
So I think… so first off, I think that that's kind of an interesting… attribute to be using, right? Because that's, like.
talking about the SDK language, which is technically not the instrumented language, Right?
Nikola Grcevski @ Grafana / OpenTelemetry 00:28:08 Yeah.
Tyler Yahn 00:28:09 So… So, yeah, so, I mean, I think that's fine.
For now, but, like, I'm wondering also, like, if we could… Change that to another attribute, and.
Nikola Grcevski @ Grafana / OpenTelemetry 00:28:22 We've just…
Tyler Yahn 00:28:22 added slice attributes to the OpenTelemetry ecosystem, right?
So, if you have this situation where you're, like, multiple in there, you could just put them all, right?
Nikola Grcevski @ Grafana / OpenTelemetry 00:28:34 Oh, okay.
Tyler Yahn 00:28:35 It's kind of an idea.
Nikola Grcevski @ Grafana / OpenTelemetry 00:28:38 Okay, well, yeah, maybe that's the solution. Find the model.
Tyler Yahn 00:28:41 I wouldn't… I would not put a slice attribute in the… in the telemetry SDK, because that's… that's definitely… Nikola Grcevski @ Grafana / OpenTelemetry 00:28:46 approximate.
Tyler Yahn 00:28:47 the convention, right? But, like, if we wanted to choose, like, I don't know… like, the… maybe, like, an instrumented language or something, I don't know, we can choose another attribute. Yeah, and then just take an attribute that's, like, all of the detective languages, I think.
Nikola Grcevski @ Grafana / OpenTelemetry 00:29:02 Yeah, that's better. I like that.
Rafael Roquetto 00:29:04 Just… just one… asterisk, like, footnote to this, that we gotta be mindful if we go down the road, is because sometimes with, like, Node.js or Java, we have these special agents.
And then… I'm not sure.
Nikola Grcevski @ Grafana / OpenTelemetry 00:29:19 This would be.
Rafael Roquetto 00:29:19 a problem.
Because if you're detecting a Java, it depends on the code, because usually you get the instrumentable needs to have the rights Language type, even if the service metrics Don't reflect that, reflect, like, this set of all.
Per instrumentable, we need to have the proper language, otherwise we won't be able to have this.
Nikola Grcevski @ Grafana / OpenTelemetry 00:29:38 That… that… that works, actually. That's not a problem, because we… that's associated to the process, right? So we still have the process information, we know that's the node runtime, or we know this is the Java process, so we will load the right thing.
The problem is, what language does the service get associated with at the end of the day? Because it's sort of like.
It's a service, but underneath there's, like, 5 different executables that may be… Involved in handling the… The service, so… I like this approach of maybe trying our best to determine the one SDK language, and then… But then have a secondary field where we say instrumented language is something that we write it.
Because…
nimrodavni 00:30:21 Good.
Sorry.
I think that… I have, like, a couple, like, objections, but tell me if you… what do you think otherwise. Like, one is, I think, even though telemetry SDK language is not the, like, correct… real thing that… because we're not an SDK, that's not the language of the… I think there was some discussion around it with, like, the distro name, whatever. I think most backends expect SDK language to be the language of the service.
Yeah, yeah. And maybe, like, and maybe we can say, okay, that's wrong, but I think a lot of backends do that.
The other thing is that instead of doing a list of languages, maybe we can… let's say there is a container, like a single… runs two processes, one in Java, one in Python. We still do detect, like, which process does, like, the request, right? Maybe we can save two resources, both of them have the same container metadata and pod and whatever, just each one have, like, basically one per process.
And we can optimize it, like, by saying if for some reason.
you have, like, a Python… like, you have a multi-processed, like, Python application, all of them will be a single resource, but if you somehow detect one Java, one Python on the same container, we'll split it up, and then, like, you report one language, but, like, it's the correct process.
Nikola Grcevski @ Grafana / OpenTelemetry 00:31:50 I think I see what you're saying, it's like, you're saying that… Huh.
Okay, I need to think about that, see if I can actually make that happen.
I think we might.
nimrodavni 00:32:00 We need to do some quirky stuff with, like, because most of the time, it will be the same.
Nikola Grcevski @ Grafana / OpenTelemetry 00:32:06 Yeah, yeah, yeah.
nimrodavni 00:32:07 Same language, but you just need to…
Endre Sara 00:32:11 Nibro, this is very cool that you're mentioning this, because Mike might have some comment on this. I spent a lot of time with the Odigos team back, like, two years ago, because they are trying to do language detection, and then language-specific instrumentation.
Slightly different purpose, but same problem. And the application that I was testing when I'm still running, is a Java application.
with the same container running a Python process to do debug thingy, and they constantly auto-detected the Python application because it started off first, because Java took longer to start, and it was trying to instrument my debug server, Python server, whereas, like, I really wanted the Java thing to be instrumented here. So, if that helps, I can bring my example and.
Nikola Grcevski @ Grafana / OpenTelemetry 00:32:58 Yeah.
Endre Sara 00:32:58 Try out these things. It's fun, in a way.
Roy Reshef 00:33:05 Well, to relate to how we've seen this a bit in the field from You know, from a lot of organizations, it… I mean, the easiest use case is that they have a smaller shell script that, at the end, launches an application with exec.
Yeah, that's also a use case we need to refer to, because exec actually kind of tears down the old process and replaced it with a new one.
Yep. So if you have shell launching Java, you only care about the… or whatever launches Java, you only care about the Java because that's the end of it.
Then you have another use case, like the one that I demonstrated in this issue, that.
Nikola Grcevski @ Grafana / OpenTelemetry 00:33:42 It's weird.
Roy Reshef 00:33:43 it… you don't use exec, but the script actually launches an application and kind of waits for it to end.
Nikola Grcevski @ Grafana / OpenTelemetry 00:33:49 Yep. So…
Roy Reshef 00:33:50 That's also… in this case, you also care only about the innermost child, like Nikola said, because that's… you know, the other… the wrapper shell script, after it's done what it needs to do to initialize whatever stuff, it launches application and just waits for it. It doesn't do anything else.
The complex case is what Andrea said, is that You have multiple processes, and you launch them, like, in the background, and then which one is actually the application that you care, and which one is, like, a debug utility, or which one is a… so to speak, a sidecar process. I shouldn't use the term sidecar, because it means something completely different, but, you have these cases, too. I mean… We have seen some applications, and some applications of, you know, famous vendors, sorry, containers, that you have, like, up to 6 processes running in the container.
It becomes a bit of a nightmare to determine, okay, which is actually the business process that you care about.
And which are helpers, like Andrea mentioned.
But, yeah, I… I agree, I mean, we should… we should find first a, you know.
Nikola Grcevski @ Grafana / OpenTelemetry 00:35:04 Why are they able to do.
Roy Reshef 00:35:05 the simple solution for the simple use cases, I'll think of it, and then look at The more complex ones.
Nikola Grcevski @ Grafana / OpenTelemetry 00:35:12 I think I… I like Numera's idea, actually. I don't know if it's achievable, but I really like that approach. It's essentially saying there's two services here, really. Like, you can create this pathological case where you have one container launching two services that both serve on different ports.
And in that case.
I mean, you can't clump them under one service. Like, one is gonna have one sort of response times on different ports, the other one's gonna have different kind of request rate on the other port.
So you really want to maybe fabricate, service name dash Python, service name dash Java, whatever it is, or some other way.
And split them up.
I don't have an idea yet, but let me think about that. I like that approach, kind of focusing on a process that actually does the traffic, and then if there's multiple, then… Even go further.
We initially attempted to kind of split them by process ID for all this language detection, but process ID ended up causing such cardinality issues that it was just impossible to manage.
You think about cases where people, it's just one Python application, but it's actually, like, a Python process pool underneath, and then all of a sudden you've got this explosion of… What's happening under the covers, and it's for no good reason.
Okay, good.
Thanks for bringing it up, Roy.
Roy Reshef 00:36:42 Sure.
Tyler Yahn 00:36:43 Cool.
Nikola Grcevski @ Grafana / OpenTelemetry 00:36:43 I'll see a candle this week.
Tyler Yahn 00:36:49 Awesome. Okay, cool. Sounds good.
keep it going. Let's see… next up, looks like I've got this up. So, yeah, I wanted to make a proposal to split the Go updates back into single PRs per update.
This, existing method is having us update all of the Go dependencies at once.
Which means that one dependency that isn't working.
Talking the upgrade of all the others, Which means that we don't upgrade.
Nikola Grcevski @ Grafana / OpenTelemetry 00:37:24 The dependencies, yeah.
Tyler Yahn 00:37:25 Dependencies? Yeah. So, I'd like to… I'd like to switch that back. I know it's gonna increase the volume of PRs, but… I'm fine if you wanted to just put them on my shoulders to handle them, but yeah, I just, like.
There's probably some groupings, obviously, like, openTelemetry.io, like, these kinds of things can all be bundled.
all the collector, all the hotel stuff, but, all the X stuff, yeah, like, so this probably actually would only get split into maybe, like.
1, 2, 3, 4, 5, 6… Yeah, I don't know.
7, 8, 9, 10… something like 10… 10PR, something like that? Maybe a little more.
Steven, yeah.
Stephen Lang 00:38:13 Is there any kind of auto-merge we can use? Because I know we have quite… specific rule set for Renovate.
And obviously we've got the entire test suite.
I wonder if, you know, Renovate offers any auto-merge options, because this is going to be a lot of PRs, and there's already quite a few.
And I'm worried that it's going to create quite a bit of noise in terms of looking for PRs to, you know, to contribute to, and to… this can just be a case of… maybe in most cases, you know, like you said, there's just one dependency here out of, I don't know how many is in the table.
But, you know, say there's, like, 30 or 40 PRs, all of which are, you know, green and good to go.
It'd be awesome if they could just ship themselves.
And then we just worry about the ones which are actually, you know, breaking.
Tyler Yahn 00:39:06 Yeah, we can't do that based on CNCF guidelines. Like, you need human review, before we merge something to the main.
But, like, once you have the human review, you can go through merge queues or things like that. We can look into doing things like that.
But no, not like a… not fully automated, I don't think that's… that's a possibility.
Stephen Lang 00:39:33 Okay. Yeah, it was a shame. I was hoping with things for, like, you know, minor… minor bumps of existing dependencies, we'd… we could specify, like, a minimum age.
Of, you know, a certain amount of days.
Tyler Yahn 00:39:45 I, I, like, I hear ya. I'm also, like, a maintainer in other repos, and, like, it's just… Normal.
I don't know, like, I, yeah, like… I get… I get at least 10 of these a day, kind of thing, and I just churn through them. It's not, like… I don't know, I don't even think about it, but, Yeah, I, I… maybe we can… yeah, it's not even a no-tell policy, it's like a CNCF policy. Like, you need… you need reviews of some level from humans, on this one, yeah.
Okay, so I don't…
Stephen Lang 00:40:19 I have plenty of approvers, right? Yeah. It's just.
Tyler Yahn 00:40:23 Yeah.
We also don't have, like, a linear history. Well, we have a linear history, we don't have, like, a up-to-date requirement on these as well, which is kind of nice. So, as long as the CI passes, they don't have to be, like, based off of main, right? Because that's the thing that was, I think, giving us the heartache before.
When we were trying this, was that, like.
They, like, once one merged, you had to upgrade, update all the others just to pick up that change.
So, yeah, this is, I think, a little bit less impactful because of that, Yeah, we can do merge queues as well. That is more just, like, once it's approved, you put it in a queue, and then the merging functionality is just automated, but… Honestly, if there's not, like, a requirement that things have to be up-to-date, then I don't know if that's even… even needed, but yeah.
Mario Macias 00:41:16 Mario? I wonder if we can do… if we can do an intermediate step that is, any update on the major or minor version is individual, and then updates in the patch and digest Can be grouped.
I don't know.
Tyler Yahn 00:41:40 Yeah, that's, like, of what would be helpful, unfortunately. Like, the… the major updates are always breaking.
Like, that's by, like, Go semantic versioning, right? Like, they have API breaking changes, they have package layout changes, like, those are always breaking, like, most of the time, like, they're closed, just because, like.
You have to literally go in the code to upgrade those. The minor and the patch ones are the ones that, like, are usually… are, like, the ones that, like, matter, and it's super dependent on, like, what the major version is, if it's already a stable package that we're depending on.
They can… those are easy to go. If it's not…
Mario Macias 00:42:20 Okay.
Tyler Yahn 00:42:21 they can be… I mean, that's actually where the problem ones are coming from right now. Like, the psyllium EVPF upgrade, right? Like, that's one of the ones that is breaking us. We keep having to pull that out. The… the SARMA stuff as well, like, that's… yeah, so it's… it's definitely, unfortunately, like, all over the place, yeah.
Mario Macias 00:42:39 Okay, we are a lot of approvers.
Tyler Yahn 00:42:44 Yeah. Mattia?
Mattia Meleleo 00:42:47 Yeah, so we recently introduced some stored demo example, or something like that.
That one is also causing a lot of, PRs for the Valancy upgrades. Maybe we can group them, like, weekly, for all of the examples, or something like that.
Tyler Yahn 00:43:11 Yeah, I…
Mattia Meleleo 00:43:12 Let's.
Tyler Yahn 00:43:12 Like, I… maybe I don't understand the problem, actually, because, like, I… I don't… I've been doing a lot of the upgrades, I have no problem doing the upgrades, like, what's the…
Mattia Meleleo 00:43:24 No, there is no problem at all, it just creates more PR, there are more workflows that starts in the CI. There is no problem, it's just to reduce the… the noise.
Tyler Yahn 00:43:41 Like, to do, like, like, your notifications, you mean? Or, like, where's the noise come from?
Mattia Meleleo 00:43:46 Not only notifications, but, but useless, like, CI jobs that, that start randomly.
Like, one thing is to have, like, 20 of them weekly, and one thing is to have one.
Tyler Yahn 00:44:02 Yeah, like, I hear you, but, like, one… Doesn't work, is the problem.
Like, we're already in that place where, like, we have just one, and it's… it's… like, 3 weeks, and we haven't merged this thing.
Mattia Meleleo 00:44:17 Yup.
For the main GoMode, I agree, but for the examples… I think it works. I don't think we have anything that breaks in there.
Tyler Yahn 00:44:26 Oh, I see, just for the examples, and like.
Mattia Meleleo 00:44:29 Yeah, yeah, yeah.
Tyler Yahn 00:44:30 Obisor one.
Mattia Meleleo 00:44:32 Yeah.
Tyler Yahn 00:44:34 Sure. The thing is there, though, there's, like, you know, 8 different services all at different languages, is kind of the thing. So grouping them, you're going to be grouping Java upgrades with Go, with Python, with Node, with C++, with… Like, all of these other services together.
Mattia Meleleo 00:44:53 If it works… Maybe we can do…
Tyler Yahn 00:44:56 I don't know if it does work, because I think you're gonna run into the exact same problem, right? Like, you're over-grouping at that point, like, you're gonna have upgrade problems because one thing's gonna cause a blockage, and then nothing's gonna get upgraded, is kind of my concern.
Mattia Meleleo 00:45:08 Okay.
Tyler Yahn 00:45:08 Like, I'm happy.
Mattia Meleleo 00:45:09 I'm happy.
Tyler Yahn 00:45:10 be taking on more of a role if we want to make it official, like, of, like, I've maintained these things.
If people just want to ignore them, that's fine, and I can… I can wade through them.
If, like, if that's the noise you're talking about, like, I don't… have a problem.
Mattia Meleleo 00:45:25 No, it's not, it's not an issue for me. It was just to, to, to have less of these PRs, which, I mean, it's not a problem, but…
Tyler Yahn 00:45:35 Okay. Nevermind.
My concern is just, like, it's just that the dependencies are getting stale, right? And, like, we are continually not upgrading things, and, like, that's… becoming more and more of a problem, for me, so… Yeah, I'm happy to… I'm happy to put in the sweat equity, and help make this happen. I'm happy to also reevaluate, like, if there are things that, like, are always grouped together, like.
Absolutely, I would definitely… I wouldn't want to do, like, individual collector package upgrades, right? Like, that's kind of ridiculous.
But, like, yeah, I definitely don't want to have things blocked, or if they are blocked, have them be individual things that we can… we can work on those, I guess, is kind of my key.
Mattia Meleleo 00:46:18 Yep, sounds good.
Stephen Lang 00:46:20 Just one last thing, just on the noise perspective. I was actually thinking from the other point of view, not that it's an issue that there's so many PRs, but say that we have, I don't know, 30, 40 PRs, and we have 10 approvers. A 10 approver's going to be looking at the same, sort of, 5, 6 PRs. Maybe it would make sense to, like, auto-divvy up you know, all of these PRs to have, I don't know, two assignees selected as, like, a round-robin thing, instead of, like, always pinging everyone, because there was maybe a bunch of duplicate approval effort going into looking at, you know, just green builds of prompts.
Tyler Yahn 00:46:59 Yeah, that's a good point. Usually with these, like, it's first time, come first serve, and like, once you approve it, most of the time, it's just merged right away, so it's pretty easy to not have, like, a lot of duplicate reviews. But, I think last time at the maintainer conf, we were, like, the Envoy folks were talking about this, where they have, like.
You know, roles and responsibilities with rolling, like, you know, you're on duty for… well, they had different maintainer, roles, but, like, this one, we can maybe make a maintainer role, where it's, like, this is your week where you're gonna handle the upgrades or something like that. Like, I'm okay with that as well, like, that sounds fine. If other maintainers are up for that, I guess is kind of, you know, the question.
Stephen Lang 00:47:42 Yeah, I'm just thinking how best I can help, because normally when I look at… I'll get, like, an hour or so to look at PR reviews, but by the time I come to look at Obi, you know, there's already somebody that's gone through and blitzed.
Everything.
So, I'm kind of thinking, like, how could I be more effective to help out with the review load?
But, you know…
Tyler Yahn 00:48:01 Yeah, the… Yeah, I mean, it's always a hard question. Definitely, like, Yeah, I don't know, like, I'm open to suggestions here, like, I think what your concern is, is, like, also to a broader… Point, though, like… not just… or, like, dependency upgrade PRs, but also just, like, general PRs, like, is there… a… like, we don't use the assignee, field at all for PRs, right? Like, who's gonna actually do the review and who's not gonna do the review? Other SIGs do that. They'll… they'll automatically rotate.
and assign people, to go, and, like, they are… that approver needs to go look at that PR, unless, like.
you know.
They want to go ahead and switch it with somebody else or something like that, but, like, we could start looking into doing that, I… yeah, I'd love more feedback, like, I'm happy to look into processes around that, I normally try to just review everything, but yeah, like, eventually it becomes, like, in the collector's sig, I know it's, like, not really achievable to do something like that. There's just too much.
volume, so I don't know, maybe we're headed there? What do other maintainers think?
Stephen Lang 00:49:23 Maybe we just try it for now and see how it goes, just with the… you know, flip the setting, get a bunch of PRs, and then, See in another week or two if it's, if it's an issue or not.
Tyler Yahn 00:49:35 Yeah, yeah. Okay.
Yeah, I mean, I… yeah, absolutely.
I think my concern is if it… if we have a bunch of PRs just sitting around without reviews, then… then I think you're right, we'll begin to do some more triaging, but… okay.
Okay, I will look into splitting that up, Next up is also one of my PRs. We're running close on time, so I just wanted to jump in this really quick.
So add the typed config, V2 exporters. This is something that Mario had asked for, in one of the PRs around the typed, or the config V2.
So, yeah, this turned into… It's not… It's not this big, but it's still massive. So it's essentially taking all of the map string, functions and switching those out for specific types.
The licenses, and notices, turns out to be, like, 5,000 lines of code, so… That's where a lot of it is, but this is still probably about 2,000 lines of just, like, actual type definitions that are being added here. So it's a pretty big PR.
I'm happy to… go about this in a particular way of breaking this up if people want, or other reviews. I did see Nicola has already reviewed it. I'm also fine if people are saying, like, let's just merge it with Nicholas approval, But I did want to raise this just so people are aware of it. This is, you know, all internal, nothing is, like, being exported, so it can all still be changed, but… Yeah, this is going through, and each particular section of the config has its own type now. I tried my best to make sure that they're all specific types, not, NEs or interfaces or other things like that, which means that there's, like, some custom unmarshalling functions in particular places.
There is, I think, one other change at, like, the top level. I backed out and added the OTELConf, types as well. So, OTelConf is something that is in the contribib for managing the declarative config.
It has its own types there, so it's using those types here to actually catch the configuration, given this is supposed to be an extension to the configuration. So, yeah, we're doing that. It is an X package, so it's not stable, but… This also is an internal package, so we can, I think, go through those migrations just fine.
But yeah, it needs, eyes, otherwise I'll probably merge this tomorrow, is my idea on this one.
Nikola Grcevski @ Grafana / OpenTelemetry 00:52:14 Yeah, I did the best I could. I mean, it's a large PR, but I… I like the changes. I went… it made sense to me, so… Bye.
Tyler Yahn 00:52:22 Yeah, I tried my best to make it, you know, idiomatic of Go, broken down, section by section, yeah, so it should make sense.
Also, like I said, it's not the end of the world if… if for some reason you aren't able to merge this, this gets merged, and you're like, Mongo instrumentation, that should be called something else. We can change the name. Like, it's all internal, so that isn't locking us in too much yet, so… Yeah.
Mario Macias 00:52:51 Yeah, I think it's fine merging with… without more review, there's nothing we can change, as long as it's very flat.
And… and it's something we can change after Merge.
Tyler Yahn 00:53:03 Yeah, absolutely, absolutely.
Nikola Grcevski @ Grafana / OpenTelemetry 00:53:06 Hey, this reminds me, I sort of was planning to follow up, because I've been messing with this Java… The issue we found with, what the user found with, the root harvesters.
And, I think I noticed something there. I think it says… essentially, right now, in the new format, it's under Discovery, and it says disabled languages, but it's almost like, should be… I think we need another category there, like, in the… like, the routes, and then disabled languages, or something like that.
I don't know what you think.
I think right now, the way in the new config to disable it is under discovery, and then you use disabled languages.
Thinking he's, route somewhere in the… in the naming there.
Tyler Yahn 00:53:55 So, like, instead of disabled languages, you want to, like, disable routes, or disable… Nikola Grcevski @ Grafana / OpenTelemetry 00:53:59 Yeah, or create another category underneath, like routes, and then under there, you can say disabled languages or other stuff, because as it stands right now, it almost means that we're disabling these languages for the discovery.
Tyler Yahn 00:54:15 Mmm, yeah, oh, I see what you're saying, I see what you're saying.
Nikola Grcevski @ Grafana / OpenTelemetry 00:54:17 was, like, saying, discover everything in here, but don't do Java or something.
Tyler Yahn 00:54:22 Oh, okay, okay. But really, it's… don't… when… yeah, that actually means, like, don't discover the routes for this language. Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:54:29 Yeah, use Java, instrument Java, but just don't discover routes, and…
Tyler Yahn 00:54:34 Right, okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:54:35 Yeah.
Tyler Yahn 00:54:35 Okay.
Yeah, could you… could you create an issue for that? I'm happy to… I'm happy to tackle it.
Nikola Grcevski @ Grafana / OpenTelemetry 00:54:41 Because I've been working on that, and I kind of modified it. I was like, okay. I noticed that it's just sort of, like, skipped my mind, but I remember that now, so I'll create an issue.
Tyler Yahn 00:54:52 This is the whole using it in anger sort of thing.
Nikola Grcevski @ Grafana / OpenTelemetry 00:54:54 Yeah, she's great.
Tyler Yahn 00:54:55 what we need. We need more of this, so yeah, that's great feedback, great feedback. Okay.
Okay.
Cool. We have… 5 minutes left, I had another PR in here for the fixed reporter pool, steal cash evictions.
I guess I've got 5 minutes. I can mention this really quick. This is just looking for reviews.
It's a really simple PR, the, this came from… It actually turned out being very similar to another PR that was submitted, but it was to the wrong upstream. So, yeah, this is just a pretty straightforward, PR that is adding, I think 40 lines of tests and 1 line of actual code, or… no, okay, yeah, this is a little bit different. This is… oh, sorry, no, this is a different one.
Yeah, this is, we were looking at the wrong UAUID, so yeah, this is something we just need to, like, make sure we're clearing from the right cache, so… 5 lines of code, and yeah, a lot of tests. So, yeah, just a heads up on that one.
Then, also, don't think we're gonna look at the open PRs. I did wanna look at, Ozzy had a question on supporting Obi and the OpenTelemetry operator.
Ozzy 00:56:17 Oh, sorry, I muted. Yes, that's right. It's something that we've been, looking into, and we wanted, maybe.
thought maybe it'd be good to get some input from, from the OB team.
two of my colleagues are here as well, but one of the… I think one of the initial questions was to do it… there was an idea that OB might replace the need for traditional auto instrumentations. As I understand, that's not necessarily the case, though.
Mario Macias 00:56:41 Thank you.
Ozzy 00:56:41 Complement each other, yeah?
Nikola Grcevski @ Grafana / OpenTelemetry 00:56:43 Yeah. Yep.
Tyler Yahn 00:56:45 Yeah, that's… so, they do complement each other. This is something we've talked a little bit about before. Right now, we have something that's in there that, for, like, Go, it's in the experimental auto-insertation for Go.
That's run really well as, like, a sidecar, in the deployment using, the operator, and I think the operator's kind of well-suited for just, like, looking at a particular pod and then instrumenting that pod.
Obi's run really well as a Daemon set.
That being said, we have a lot of work going on right now, I think Mike Dame's on the call, to try to make it work, I think, in a… operate in a different way. Like, there's still, I think, some optimizations that aren't going to be included in there, but, like, running it as a sidecar is… I mean, it's possible now, it's going to be possible to do it dynamically, going in the future, if I'm not mistaken.
So, I would say, like, yeah, there's definitely some… some work to be done, or exploration, maybe, is a better way to say that.
But yeah, I don't see Mike, oh, no, there's Mike.
Mike Dame 00:57:44 here.
Ozzy 00:57:44 The sidecar, thing as well, because I just wanted… I think that was another question that had been raised that, Yeah, that, which of the deployment methods that we should support in the operator? And, you know, was there an existing preference in the community to how to deploy it? Because a sidecar is… is kind of convenient, because it's a bit like the… existing instrumentation injection that happens in the operator, where it, for, but, yeah, as I understand it, the Demon set is perhaps more efficient, and then with the Demon set, it can either be a standalone OB daemon set, or it's also possible to run it as a collector-receiver, and I was just curious about that as well.
Tyler Yahn 00:58:24 All great questions. Yeah, I think the preferred way to do it is probably the daemon set, is what I would say. Just, like, what you said, like, optimization for resources, like, there's definitely universal processes that you aren't going to be duplicating, there's, yeah, like, a lot of overhead that you don't incur, not running it as a, sidecar.
the, collector receiver, I think, is still… that's a work in progress. I think that'd actually be my preference, you have to run the collector as, sometimes you have to run it with, like, elevated permissions with other people aren't gonna be into that. So, like, there's a trade-off there, so I'd probably say, probably, if you could do both of those, maybe all three even?
But yeah, like, the Damon set, I think, is, like, the standard way we recommend running Obi, so if you had a choice, that'd be the way I'd recommend.
Ozzy 00:59:12 Okay, yeah, because, I mean, the dedicated demon set and the collector receiver, I suppose they both… yeah, they both a demon set, and they both require the same privileges as such.
I think, the collector receiver, I think there is some preference for that in the operator, because, well, yeah, it's convenient, and the existing collector COR can already be configured by changing the privileges, adding volume mounts, and it works.
Is there going to be a… a distribution of that available? Because at the moment, one has to build the image themselves, the collector image, which I've tried doing, and that might be a bit inconvenient, I suppose.
Nikola Grcevski @ Grafana / OpenTelemetry 00:59:50 Oh, Lord.
Tyler Yahn 00:59:50 That is what we're trying to do. There's an issue tracking it upstream? But I don't have a timeline for you on that one. I know Nimrod's all… there's a lot of people on the call aren't involved in this one, so yeah, it's definitely a… We're working on it, you will hear it, there will be a splash when that happens. But I… right now, no, it doesn't exist.
Ozzy 01:00:12 Yeah.
nimrodavni 01:00:13 There's, Sorry, there's, like, the… as you said, there's an issue on that, and we're trying to push for a solution.
And if you… I see you tagged the issue, or I think Israel tagged the issue in your PR. If you could either, like, thumbs up or comment the issue, I think it just showed that people, like, more people need it from different things, and I think it will help push But we're trying to, like, approach it with a few different solutions of how to do it, so it's accepted by everyone.
Tyler Yahn 01:00:47 Yeah.
But yeah, would really appreciate some support on that one, for sure.
I'm sorry, we are at time, but Ozzy, if you wanted to come back next week, we can put you at the top of the agenda as well, we could talk more about this. There's definitely a lot more depth to it, so I apologize, this is kind of an interrupted conversation.
Nikola Grcevski @ Grafana / OpenTelemetry 01:01:04 Yeah, I wanted to quickly say that, now that, Pino has added the map resizing capability, maybe we can create an image that is sort of like sidecar okay?
So it'll be lighter on resources, so you can… we can do that for Sidecar, at least for Go, and people want to try Rust or other languages that are just not amenable to other instrumentation. We can do it, but it won't be optimal, because we'll still be querying all the Kubernetes attributes and everything else over and over for… from every pod, and yeah.
Tyler Yahn 01:01:34 Dammit.
Yeah, absolutely. Ozzy, I'd appreciate it if you'd come back, would love to talk more about this one, that sounds great. Otherwise, asynchronously in Slack or, in issues would be great. Otherwise, thanks everyone, talk to you later.
Ozzy 01:01:47 Thank you.
Nikola Grcevski @ Grafana / OpenTelemetry 01:01:48 Bye!
