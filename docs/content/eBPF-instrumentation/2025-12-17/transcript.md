SIG: eBPF instrumentation
Date: 2025-12-17
Duration: 52 minutes
Zoom Recording URL: https://zoom.us/rec/share/NtlapKQmRTUUPa3V4wD_SurTu35NWYsZMNkqTVkA1oIs0doauWDxPbMufLQFKJOB.4W89K9ckLX12Y_sn
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:50 Hey.
**Giuseppe Ognibene | Coralogix** 00:52 we want.
**Tyler Yahn** 00:53 How's it going?
**Mario Macias** 00:54 Hello?
**Tyler Yahn** 01:02 I guess he needs to play me.
**Mario Macias** 01:03 is AI note-taker. It's from some… From someone of you.
**Tyler Yahn** 01:10 No.
Soundquan, yeah. I'm guessing… Oh… I think I might have seen this, like.
like, you can use, like, an AI companion on Zoom or something like that, and it will, like, join the meeting.
I'm pretty sure they're, like, expressly forbidden from being used in OTEL, but… I really don't want to go… Claim the admin thing and figure out how to do that again, just to…
**Mario Macias** 01:39 Yeah, okay.
**Tyler Yahn** 01:40 Yeah.
**Mario Macias** 01:40 Anyway, this… the record is published online, it's public and published, but yeah, it's a bit weird, it's a bit weird. This San Juan… San Juan's AI Yeah. Hello, Zanquans!
They'll read the transcripts. It'll be great. Yeah. Actually, maybe that's a good point, like…
**Tyler Yahn** 02:01 Well, I guess, like you said, it's recorded, but I was thinking, like, maybe if they get it transcribed into another language, but it's probably just… you can do the same thing from the recording, so, yeah.
But… Yeah, I don't know. I've noticed there's also, like, another one for, like, Bill I've seen in the past. He used to be pretty regular. I've never seen him in the meeting, but yeah.
Cool. Alright, we can jump in here in just a second. If you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you want to talk about, go ahead and add them there as well.
I think… We're probably getting close to quorum.
Mario or Steven, do you guys know if, Nicola's able to join today?
**Mario Macias** 02:45 I met him a few… One hour ago, he didn't tell me he wouldn't join, but…
**Tyler Yahn** 02:56 No, yeah, I didn't know if he was already on vacation or not, but it sounds like that's.
**Mario Macias** 02:59 It's, it's, it's, yes, he's, he's starting tomorrow, vacation. Okay. He's today.
Here.
**Tyler Yahn** 03:07 Yeah. Okay.
Okay, well, we could probably jump in here, and, I just wanted to ask, actually, I probably don't need to… share my screen, but I'm stuck at this point.
Yeah, we can, we can just go jump in here, So, yeah, I wanted… I was talking with some other folks in the hotel community, yesterday, and one of the questions that they were asking is, like, there's this… there's the Hotel Injector Project, so I guess maybe just background for folks that aren't aware of the Hotel Injector Project. It's a pretty sweet project.
It is a project, essentially, that, like, looks when you go to start up an application on your host, and it uses… it runs in SystemD, and it will, like.
Mutate the environment that it runs in, so that it includes specific environment variables to start and use the OpenTelemetry, auto, The auto-instrumentation packages for languages like Java, Node.js, Python, and, there's one more.
That I'm forgetting. But anyways, like, the big ones. And so, it's a cool idea, but essentially it deals with, like, this auto-instrumentation, like, idea.
And one of the things that they were asking me, like, well, one of the things that they're doing is, like, they have to detect languages.
As those languages are getting started on the system, and it's being, you know, through some sort of runtime, And they wrote their own, I think it was, like, a DART language, injector, or ZIG, that's what it was, yeah. A ZIG language, like, injector. So, yeah, it's kind of an interesting… it's not kind of… it is… it's a very interesting project, but one of the things that they were asking is, like, when it comes to, like, runtime detection of applications, like… it seems like, Obi is better positioned for this, because you can very easily see when anything starts, and what that thing is, is, you know, just a little bit of an interrogation. So, like, we actually already have a very, like, rich discovery system in Obi.
And the question was, is, like, is there any way that we could, like, merge these two projects together? Meaning that when you detected say, a Java program starting, you could… tell that program, you know, through the environment variables and through its dependency chain, just to start using the operator instead… I'm sorry, the autoimm rotation instead of us instrumenting it with, EVPF.
And then, you know, obviously for things that we can't instrument with auto instrumentation, or if a user configures it to not instrument it with auto instrumentation, we would just instrument it with eBPF as well, through our general processes.
And it seemed to me like that was a possibility, but I wanted to kind of bring it here, and hear if I'm crazy, and it's never gonna work, or, If it's just a bad idea, or people's thoughts on the idea.
**Mario Macias** 06:02 I think something that might be worth exploring. I don't know which pitfalls we could find when trying to merge.
Z, go… but, I think it's worth exploring. Either the auto-injector won't work, with some… some kind of programs, like, for example, with Go, I think the hotel injector cannot work.
the same way that some… some languages will work better with the injector rather than with OBI. So, yeah, maybe prototyping a proof of concept and see how it can work. Yeah.
**Tyler Yahn** 06:49 I foresee the ZIG component going away, to be honest, and it's more like… OB itself would do the discovery, and then take over the functionality of what that zig, like, script is doing, where it's saying, like, hey.
**Mario Macias** 07:03 No.
**Tyler Yahn** 07:04 I have a process starting, can I mutate it via eBPF, its environment variables, and can I, like, update its dependencies through some sort of, like, chain like that? I think that that's kind of, like, where I see this going. But… Yeah, so I would see it as essentially, like, can you do the same thing that the ZIG functionality is doing, but just do it in EVPF, I guess, is the question.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:26 It would be quite difficult to kind of trick the process for getting the environment variable, yeah.
**Tyler Yahn** 07:35 Yeah, Florian's saying you can't… you can't update the environment variables in a safe way. I'm guessing it's the same thing that we're dealing with, like, the UPREB stuff here. You'd have to essentially, like, have extra permissions to be able to set that in eBPF.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:47 Yeah, and another disadvantage, perhaps, is that it only works on eBPF-enabled platforms, so if you're on some… Kubernetes managed that eBPF is not available, then… It would be a shame not to be able to inject.
**Mario Macias** 08:04 Yeah, but… even… or we can do it even if… without using EVPF, the same way the ZIK, the current injector, injects it another way.
I mean, just because we are eBPF doesn't mean we have to use eBPF always.
**Tyler Yahn** 08:24 That's what you're saying?
**Mario Macias** 08:25 It's…
**Tyler Yahn** 08:26 Like, we could do it in, like, the runtime, right?
**Mario Macias** 08:30 Yeah, same as we are working on, for example, in injecting the Java agent.
an alternative to the… I mean, a part of EVPF, if we can inject the Java agent, but we can also inject the… the hotel injector, or any other SDKs.
We can have a very complete solution.
**Tyler Yahn** 08:52 I don't know if we can find other pitfalls.
**Nimrod Avni** 08:55 I think it will also require.
**Mario Macias** 08:57 Why not researching?
**Nimrod Avni** 08:59 like a restart of the service in most cases, right? Or…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:03 So that's, like…
**Nimrod Avni** 09:04 I guess that's, like, something that is known when you do the injector, but, like, when you deploy OB on, like, a cluster, I guess it's… it's not, like, you don't want all your services restarted, or, like… At the same time.
**Tyler Yahn** 09:18 Oh yeah, so, like, the injector right now doesn't… it only works, when a service is started.
So, deployments or something? Yeah, yeah, so essentially when the service starts, then it will… then it will actually go through its process of, like, mutating its environment. Yeah, I think Florian's saying that the… yeah, P-Trace could also use interrupt… yeah, essentially doing that, as well. Doing some sort of, like, interrupt… signal when something has started, not necessarily restarting something. I think that that's… that wasn't… yeah.
In fact, that might be a good way to, like, think about it, like, you could do instrumentation using eBPF for a running service, and then as the service restarted, maybe you go through a different processing pipeline to, like, get richer information, if that's possible.
So we have, like, a very comprehensive way to instrument things there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:04 Yeah.
**Nimrod Avni** 10:04 We might want to, like, then improve the way we… kind of… because right now, having, both, like, auto-instrumentation and OB instrumentation, we, like.
it's basically choosing either or, but let's say in Obi, we have stuff, I don't know, like, stuff Nikola worked on, like DNS and TCP, and some stuff that even, like, normal instrumentation couldn't get, maybe you want to combine them.
So we… it's like… we need to think how to integrate it between processes that are fully BPF, and, like, you can't even inject to them, like, I don't know, like Go and Rust, and Zig. Stuff that are auto-instrumentation, and stuff that are, like, you can… you want both.
Or, like, combination of them, but without duplication.
**Tyler Yahn** 10:54 Yeah, I think that's a really important thing, and the thing is, is that I think that that problem it already exists, because I think there are people that are already running both, right? And they're like, I would really love this feature, and I'd really love this feature, but like, if they're going to be separate systems, like, they're definitely not gonna interop, right? Like… So it'd be really cool if we could do something like that, like you're saying, like the DNS, and essentially, like, the external client span could wrap in the eBPF space, and then the auto-instrumentation stuff could take over, you know, internal to that. It'd be, you know, much richer in that situation.
I agree, like, I think that you could have a very, like, comprehensive solution if we could try to get that integration to work.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:34 That would be actually the best of both worlds, actually, now that I think about it. That's a good point. I'm not sure we can pull it off.
So one of the advantages of OBO has always been, compared to ethnic instrumentation, that it captures the actual request time, not whatever… after the thread has actually started instrumenting, and it's quite a bit. If you spam the application.
If it's actually on its knees, it cannot serve as many requests as you push to it, you get vastly different results from what OB will give you, which is the actual time the request took versus what the application is reporting.
With regular instrumentation, so if we can actually produce the BPF span for the application to pick up, so then we get, kind of, this immediately from eBPF, we create that trace ID, With a span that can maybe then be linked into the application SDKs, if we can pull it off. I don't know if it's possible, but… That could be weird.
Really, really cool.
**Tyler Yahn** 12:32 Yeah, I definitely don't see why it couldn't… Well, maybe, maybe a little harder to link it, but it has to have some sort of, like, context propagation form of some… some form, but, like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:41 I think you should be able to…
**Tyler Yahn** 12:43 Yeah, I think, I think you should still be able to make that work.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:45 Yeah, because right now, with a trace… trace IDs we inject on client requests, but there's nothing… to say that we could not override, using the same approach, the trace ID of an incoming request. So we would take the incoming.
Use that as our route.
passed down to the application that's instrumented a different trace ID. So when they read the trace ID, it's linked to ours.
So, I think it's doable, it's a really cool idea.
**Tyler Yahn** 13:16 Yeah.
Yeah, and I think, like, the key thing, though, is that, like, I, like, I'm glad to hear that you think it's doable, because I wasn't sure if it's doable. I think that there's, like, a lot of still questions, like Mario was pointing out as well.
But it's more about, like, people I was talking to are, like, in the project, but also, like, on, like, the governance and the technical committees, asking, like, you know, can we provide OTEL users one… one thing to do? Instead of having, like, this, like, very complicated story of, like, well.
use the injector here, but you could also run OB next to it, and, like, there's this… there's, like, sometimes they interop, sometimes, like, they'll just ignore each other, and, like, it'd be nice if it was just a cohesive solution with, like, a single deployment, I think is kind of the idea.
And so, I think this is, like, from what I'm hearing, like.
it's worth exploring, at least. And so, yeah, I can go back and say, like, this group is somewhat interested, or this group is interested and open to… Yeah, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:15 I mean, we definitely want to make sure, that whatever the injector does works really well with Obi, so that… especially… so, let's think of it this way, like, some… some integration… some SDKs do not even have metrics, so it would be really cool if we could run one by side by side, so then use OB to produce the metrics, if you want, and… And then use the tracer.
traces from the SDK.
But I had some comment you made, like, do you think the zip code is just going to get replaced with something else, or…
**Tyler Yahn** 14:48 Well, that's how I was thinking about it, but, like, it's super up in the air. I don't, like… so, like, I was thinking about doing this whole thing with eBPF, but, like, to the points being made here, like, that might be very challenging.
So it may be something that we'd want to, like, integrate at, like, the Go runtime or somewhere up at that level. I know they chose Zig for a specific reason, so that they could ship it and not have a dependency on libc.
Yeah. So, like, we would have to be careful about that, because I think there was some, like… circular dependency on trying to, like, find some sort of, like, libc action that's going on into the kernel space. I don't remember exactly from the talk that I listened to, but, like, that was why Zig was, you know, existed. So, like, if that's not something we can work around in trying to work on this integration, then maybe, yeah, there's some sort of way we have to, like.
shoehorn in the ZIG process, but, like.
Maybe not, I don't know, like, I really don't. It's such an early stage at this point, I couldn't say.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:45 I mean, the ZIG issue is… I mean, Zig is pretty cool, in the sense that you produce a binary that doesn't depend on libc, but the way people do this with other programming languages is really just build one for Alpine, the other one for… And one for Mosul, and the other one for… Right. So, it's not… Unsurmountable if you had to build two different builds and just pick the right one based on what's arrived on the system, so…
**Tyler Yahn** 16:08 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:10 But yeah, you need… I mean, technically you can build it with Go, but it has to be a shared object library that… if it's gonna use the same mechanism of faking the getEnf call… So whenever somebody does getEnv to pull environment variable, is this there? This Java tool options that loads the agent?
**Tyler Yahn** 16:28 Yeah. And it just fakes it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:29 Essentially.
Saying, yeah, there is one, and it's this.
**Tyler Yahn** 16:38 But yeah, okay. We don't have to solve it. It sounds like there's… there is a path to explore, at least, and I will… I'm gonna go back and say that there was a positive reception here, and that we can, We can look further into it in the next year. I think it's kind of the…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:51 Take away from here.
Mind you, like, there's… there's an interesting, I just want to bring… I know we're on this topic, it's a little bit off-topic, but there was an interesting, project from a company, I think, I don't know, I think… The product's called Mirror D, it's open source, company's MetalBear.
But they… Actually, in… Use this approach of the injector, and supercharge it to intercept many, many of the standard library calls.
So… you can argue that you can write something like OB, maybe not fully OB with the propagation, but just by doing what the injector does. It's sort of faking the system calls. Essentially.
We tap into the syscalls, to track the requests in and out.
they actually fake the std.lib calls with their own wrappers around it. So, MirrorD is not actually using it for purpose of observability, they're using it to So you can kind of locally debug something that's in a remote Kubernetes cluster, so it kind of… takes every of the… your loc… you say, locally, I want to open this file on my disk, but that file does not exist on a disk, it exists on the remote cluster.
they actually proxy that request all the way to the remote cluster through SSH or whatever. You get the file back, and you're, like, stepping in the debugger as if you are actually on the actual cluster.
And they had done Go support as well, so they're using Go they're patching the Go binaries to add this, because this doesn't work for Go, right?
Okay. You cannot… you cannot… Go doesn't use standard libraries, so you cannot actually override GetAn for Go. Right. So they patch it, and… It's quite neat, quite neat. When I saw that, I thought, yeah, you can actually write something that sniffs everything just by faking this.
**Tyler Yahn** 18:48 Hmm. Yeah, that's really interesting. I'll have to take a look at that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:51 Yeah, it's called Mirror D, the project.
**Tyler Yahn** 18:54 Yeah, I think I…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:55 middle there.
**Tyler Yahn** 18:57 I think I found it. I guess I'm not sharing. Let me start sharing again.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:02 Yeah, they're done a lot of work. They use Frida… Core or something? Yeah.
**Tyler Yahn** 19:09 I'm guessing this is it, right? Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:11 Yeah, it's quite neat, like, when you think about it, they… you drop this proxy on the remote Kubernetes cluster, and then you practically can open IntelliJ or your favorite debugger and step through your code, act as if you're actually on that cluster debugging application locally.
**Tyler Yahn** 19:28 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:30 it proxies everything. Like, if you're touching a SQL database that's remote exactly as it is, then… It would be, yeah.
**Tyler Yahn** 19:42 Yeah. Quite impressive.
Cool, yeah, I'll have to… have to take a look at this, yeah. Sounds interesting.
Okay.
Mario, you wanted to talk about MongoDB crashing?
**Mario Macias** 19:55 Yes, I wanted just for some advice. We found today, we already submitted a patch.
In the… in the user space part of the code that is parsing the binary MongoDB over the wire, protocol, we found some missing checks, and it crashed due to, trying to access out of the bounds of an array. So we fixed it, but I don't know if there might be an underlying reason of… for example, not parsing correctly the chunk of the buffer that is submitted to the user space. So maybe you can advise, or some of you can advise me, where could I look To verify that the buffer is properly selected and forwarded.
If you don't know it now, because you need to look at the code, it's fine, just saying, I don't know.
**Nimrod Avni** 20:58 What's the… like, are there any, like, error logs or something before OB crashes, or is it just…
**Mario Macias** 21:05 No, we just crashed it because it tried to access an unallow… there is already merge, if you look into the closed PRs, there.
I mean, the fix was just adding a check, fix MongoDB client panic, yeah.
So it was basically adding a new check, but I don't know if that might be some… there might be some underlying reason for… For getting this data in a wrong format that is worth checking, just to avoid just having an error and ignoring it, and nobody noticed the data is wrong.
Any way we can.
**Stephen Lang** 21:59 The… with the logo…
**Mario Macias** 22:01 the offline.
**Stephen Lang** 22:02 the Mongo buffers on TCP detect transform, but I don't know how it gets there.
Have you had a look at the TCP detector?
**Nimrod Avni** 22:10 I'm looking at the code, and it seems like it's… Where it tries to parse the length.
Like, line 286 is trying to binary Little Indian…
**Mario Macias** 22:24 Yeah, yeah, it's like, the chunk, the slice it tries to get is bigger than the actual available slice. Yeah, no, I think this part is fixed, but I didn't know if there could be something wrong, and it's worth looking in the VPF site, for example, as… it was mentioned.
**Nimrod Avni** 22:48 Yeah, currently it's, like, I think there's no, like, any large buffer or, like, any… relation to Mongo, we're in a place that's not in user space, in, like, this, like, transform…
**Mario Macias** 23:01 Okay.
Okay, okay.
**Mattia Meleleo** 23:03 I think this happened a couple of times with SQL buffers as well, and the last time it happened was because the buffers were truncated.
So every time we parse some TCP code, we need to check, Every single bound, because it…
**Mario Macias** 23:21 So it's… Okay, it's expected… yeah, that was my main… what I needed to know. So this… this is not something unusual, so it is expected that at some point you get the buffer truncated, and it's… is… you can expect that from time to time, you will try to read beyond this size, so you need to check. Okay, okay, that's fine, that's fine.
Okay.
**Mattia Meleleo** 23:50 Yeah, I think so.
**Mario Macias** 23:52 Okay, okay.
Thank you.
**Tyler Yahn** 23:56 Okay.
Yeah, I guess, also, if you have more questions on that, Mario, or more requests, an issue, or Slack, or something like that, we can always jump in there. Yeah.
**Mario Macias** 24:07 Yeah.
**Tyler Yahn** 24:10 Okay, cool. So, Last up on the list, I just want to review open pull requests, so maybe we can just jump through this. There's still, collector work here that we can do in an update, I think, Mattia, you're still working on your implement trace log correlation, I think. I saw a push here this morning.
**Mattia Meleleo** 24:31 Yeah, I'm still doing some load testing. I discovered a couple of issues, which I now fixed. I'm still doing some testing here.
**Tyler Yahn** 24:40 Okay.
**Mario Macias** 24:40 Right. Not blocked by anything?
**Tyler Yahn** 24:42 Other than…
**Mattia Meleleo** 24:43 No, not blocked. I'm, right now, I'm mostly trying to find workarounds to BPF probate user.
Other than that.
**Tyler Yahn** 24:53 That's a… that's the favorite pastime of this group, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:56 Yeah.
**Mattia Meleleo** 24:57 Very funny. Yeah.
**Tyler Yahn** 25:00 Okay.
Cool, I don't know if I saw Mark on, but there was also this PR for Async.io, I think we talked about this last week as well.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:11 Yeah, Mark's, is… On vacation until next year, so…
**Tyler Yahn** 25:18 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:18 It's niece work, essentially. I think there's… I left a lot of comments, I'm… questions.
That'll lie, certain things are like they are.
I think it just needs more work.
**Tyler Yahn** 25:32 Okay.
Yeah, yeah.
Cool, alright, then we'll just wait for next year, and we'll talk more about it then.
Okay, some more dependency updates, just need some tender love and attention. So then, add config template that Opie accepts. I think I saw… another… yeah, the schema generation PR… I don't think there's been any movement on this.
Oh, okay, alright, so it does look like they also opened up this…
**Nimrod Avni** 26:06 No, that's me.
**Tyler Yahn** 26:08 Oh, Nimrod, sorry. Okay.
**Nimrod Avni** 26:11 I saw that PR, and I toyed around with basically generating… I can talk about it in an hour, when you reach my PR.
**Tyler Yahn** 26:22 No, let's talk about it now. Sorry, let me open it up, and then.
**Nimrod Avni** 26:26 Yeah, so it's basically, kind of parsing the config struct.
With some, with some relation to stuff like stringified enums and the comment, and using some JSON schema library to generate… automatically generate the JSON schema for our config.
And also validating CI and stuff like that.
It's still… it's mainly, like… most of it seems to work. There are some stuff that, as we, like, will improve the config, things also similar to work that, Giuseppe did, of, like, making sure our config types are more, like, closed and enumified, and, that will make our schema better. And you can also have, like, manual overrides, like I did in the… Context propagation mode, which is a bit complex to represent as a type, because it's either, like, you give all, or it's an array of some stuff.
But you can, like, take this, I took it to some, like, JSON schema to JSON website, and it generates a similar enough config.
**Tyler Yahn** 27:40 Oh, cool. Nice. Yeah, that's always… It's always great to validate.
**Nimrod Avni** 27:44 So he also asked me now on… stuff like the Kubernetes, under Discovery, there's, like, metadata, which is a map, but it actually accepts only, like.
some values of, like, Kubernetes namespace, Kubernetes, pod, there's, like, a set list of values it accepts, but it only validates them in, like, the isValid function, and it's not embedded in the types. So I'm trying to embed that in the type, but, like, generally, everything that we will, embed more in the types, the schema will be more accurate.
**Tyler Yahn** 28:22 Yeah, right, exactly.
Yeah, this looks great. I, obviously, like, there's a lot of the review on this one, but it looks like something… this is exactly like what I was thinking as well.
To Mark's question around this, like, existing in another place, I don't… I don't know, It's probably actually worse. So this… I mean, I think this is a great place to keep it to start with. I don't think that this should block this PR. I think that, like, we should try to progress with something here.
In the long haul, I think that maybe it should make sense to keep this in maybe a centralized place, because we do something similar for the OTELConf package in the contrib package for OpenTelemetry Go Contrib.
But yeah, so I think that there's also some, like, tooling we use there as well. Another thing, though, that comes to mind in, like, seeing this is that, like, you can take… One of the things that's really nice is, maybe we just take a look at this really quick, see if I can find it. So the telemetry configurations is where they also use JSON schema, and in… It was recently added.
But essentially, like, what you can do is you can create, I think it was here… No, it's not here. Yeah, it's like this meta schema that was… defined, and it will produce these, like, markdown files. Yeah, here's a bunch of, like, this meta schema, compilation stuff. And essentially what that'll do is it'll, like, give you understanding of, like, what is allowed and what isn't allowed, through, like.
it essentially generates docs for you, which is really cool, and I think that this is something that we may want to take a look at here. I can't seem to find it.
**Nimrod Avni** 30:04 I mean, generating docs from JSON schema to, like, more human-readable…
**Tyler Yahn** 30:09 Yeah, yeah, exactly. And so… and it also tells you, like, defaults and things like that, and so, like, there's a lot of really cool, like, tooling that we could… we can start building up on top of this, because, like, one of the things with, like, our configuration right now was, like, the original PR that opened it was, like.
how do you… how do you find all of the configuration? Because we have a pretty good job documenting most of it, but it's not like… here's just, like, a configuration file with everything in it, and then also, like, once you get there, like, what is the description for each one of these fields, or something like that? So it'd be cool if you can, like, start to do that, essentially, and saying, like.
put notes in some sort of, like, format that says, this is what the description is, this is, like, maybe what a default value is if it isn't actually found, and so, like, yeah, it's cool.
**Nimrod Avni** 30:53 The description comes from the comments above the fields, basically.
way… and I tried to… there were some comments that were, like, more internal, development comments, so I tried to separate them up a line, stuff about, like, let's say, integration with Bela, and I tried to, like, get Bela out mostly out of, like, OB comments.
And regarding default values, we… I tried to do something, and I didn't fully work. Like, you need to kind of take the default config, like, const.
And, like, match it with the schema and take the default from there.
I think that's the… That's, like, the… the… the way to do it.
I think it's… yeah.
I think what you can…
**Tyler Yahn** 31:41 also do is, like, you can go the other way as well. So, I think this is a great way to start in, like, getting this generated.
But eventually, what you can also do is define the defaults here, and then regenerate the Go code, right? And so that, I think, that becomes, like, the more powerful direction, because all of that, it just, like, if you wanted to update a particular configuration value or a configuration, like, setup.
you do it in one place, it updates your docs, it updates the code, it updates, like, and all of your APIs start to get, like, tuned in the way that you wanted it, yeah, so… Yeah, I think, like, that's the correct way to find your defaults currently, like, it's going to be hard, right? Because, like, you just said, like, sometimes, like, it's super not obvious where the defaults are, but, like, once you get them all in JSON schema, you can regenerate this and start building a library for the config in, like, a centralized place that will have all the defaults at, like, the start of the parsing, yeah.
**Nimrod Avni** 32:35 Yeah, ideally you can even, like, create the whole config struct from the schema.
We're just doing it the other way around, because that's what exists. Yeah, I think…
**Tyler Yahn** 32:45 I think I'd love to go, eventually, getting to that point, because it will help unify and help you understand, like, where it's coming from, yeah.
And now, what you can do is you can also take this… JSON schema that you've added.
And we don't have to do any validation in the Go code anymore.
you can use the JSON schema toolings to validate the, you know, the ingested YAML or the ingested JSON file to say, like, oh, this is valid config at this point.
**Nimrod Avni** 33:16 Yeah, I think most of the… Yeah, if I'm, most of the stuff here I'm taking from, like, the type system, so I'm guessing… Like, if you say, you know, that this thing is, like, an enum of 3 strings, then you won't be able to ingest, like, any value into it.
Actually, I don't… I'm not sure how that works with, because it's just an alias to a string.
**Tyler Yahn** 33:45 You can do enums here as well, in JSON schema.
**Nimrod Avni** 33:48 In JSON schema, yeah, I'm just not sure in Go, like, the stuff that we have… For, like… I don't know, like, not propagation mode, because that's, like, an int, but…
**Tyler Yahn** 34:01 Or, like, the JSON printers, or the, the.
**Nimrod Avni** 34:04 Yeah, does that validate, like, does that validate it on the code goal level, or does it need to be… you can look for, like, trace printer here, it will give you all the… values, because it comes from the enum. But that's not built-in, I had to do some… Or it's, like, print? I don't know where it comes from.
**Tyler Yahn** 34:25 Yeah… huh.
Yeah.
**Nimrod Avni** 34:30 No.
I can't remember the exact, I thought it was… Adjacent, yeah, this one.
**Tyler Yahn** 34:38 Yeah.
**Nimrod Avni** 34:38 But I'm not sure, like, this will generate this, but I'm not sure if in the Go code, if you just put, like, some random value, will that… will that work?
And just crash at runtime or something. So…
**Tyler Yahn** 34:52 To generate this, you mean? Or the other way around?
**Nimrod Avni** 34:56 Let's say we don't have this config, and I just create a YAML, and I put trace printer, some random value. Yeah. Will it, like, crash during the config parsing if we don't have any special validations, or will it just generate a crash at runtime?
**Tyler Yahn** 35:14 Yeah, see, that's a, yeah, I think it all depends on, like, how you want to use this, right? Because you can definitely use tooling to say, like, you can get an error at the end, and then determine what that error is, and if it's an unrecoverable one, then forget about it. But, like, if we had, like, a default value here, right, you can just say, like.
alright, you just passed me garbage. I'm just going to go ahead and use the default value at that point, right? And so you can ignore custom values if you wanted to do something like that.
**Nimrod Avni** 35:44 Yep.
**Tyler Yahn** 35:45 Yeah, I mean, there's a lot I think we could do to work on this, but I think the first step is just what you have Generated here, and so we can… Yeah.
**Nimrod Avni** 35:53 Okay, so I'll continue trying to improve some minor stuff in it, and at least get it out.
**Tyler Yahn** 36:01 Yeah, that sounds good. I think this is great. I think once we have something like this.
Building tooling around it is going to be very helpful and easy to… easier to… to make shifts in the configuration, versus trying to build yeah. Track docs and implementation all in one place, yeah, or one PR, yeah.
Any other thoughts on this from other folks?
Okay, cool. Then, yeah, we'll keep tuned. Thanks, Nimrod, for working on this.
Okay. Next up, update semantic conventions to 137. Still need updates from this. I haven't seen Alex this week, I'm guessing he's out, actually, on vacation, so we'll check back in on this one.
Ads, or update IPv4 option code? Raphael, I don't know if I saw Raphael on…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:56 No, he's on vacation as well until mid-January.
**Tyler Yahn** 37:00 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:00 Yeah, I asked the question, I think Mario had some comments, so… needs to take a look.
**Tyler Yahn** 37:08 Yeah, okay, we'll… we'll check back in then.
When Raphael is back.
Update all patches, this is still… Got issues, so needs some help on this one. I think this is a Ruby thing, if last I looked?
Yeah, it was, like, some Ruby issue.
So, I have to jump in here as well.
**Mario Macias** 37:36 Yeah, so sometimes closing and letting renovate or re-trigger it.
**Tyler Yahn** 37:42 Yeah, I thought it was just… yeah, it just re-triggered 13 hours ago.
**Mario Macias** 37:48 Okay.
**Tyler Yahn** 37:48 I tried, yeah, so… Yeah, I don't know. I think it's sometimes, like, it just… I don't know why that would be… Yeah, I really don't know why that would have changed, like, the permission denied on some sort of file here, but… Yeah, take a look at it, it's not… we don't have to debug in the meeting here.
Okay, we talked about the config.json schema generation.
Mara, you have a work in progress for per-application metric features. This is something I think we saw a while ago, if I'm not mistaken, but maybe…
**Mario Macias** 38:29 Yes, I started to implement it, but it still requires some work and create proper integration tests, yeah, it's… it's just left there as a draft to get some… to try to get some CI errors in advance, but nothing… It's worth start reviewing right now.
**Tyler Yahn** 38:51 Okay.
Cool, alright, yeah, I, yeah, understand. Definitely do the same.
And then, Nikola, similar, I'm guessing, for the Inject OB Java agent, for Java processes?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:02 Yeah, and someone was there, but I started writing the tests, which is what I've had as a local test for various, like, libraries and whatnot.
And then I'm debugging an issue. Somewhere along the lines, we're just merging this code, I guess, without tests, because it wasn't done. So, from my prototype, something's not quite working, so I gotta… for that.
**Tyler Yahn** 39:24 Is this… is this exactly what I was talking about at the beginning with, like, the injector thing? Where you're, like, you're adding… The honesty.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:30 Explain. I'll explain, maybe. So… OB had ability to inject the hotel SDK, Java agents.
Because for Java, we couldn't do TLS.
because it's… It's just, you know, there's no way to decrypt that traffic, they're not using standard libraries to generate code and whatnot.
But… Recently, I mean, not recently, last time I did this work to inject the Java agent, we knew of that the OTEL SDK Java agent Dynamic injection does not work for all instrumentations.
And… I went and fixed them on my branch, which was pinned on version 2.14 of the OTO Java agent.
But that was from earlier this year, so I fixed those issues, and I got it to instrument almost everything.
maybe some AWS things still had some things that needed to be fixed, but… Most things work. However, since then, the… the actual… that project, the OTEL, Java SDK, are working on, refactoring, And unfortunately, the way they're kind of… Refactoring the, instrumentations don't… doesn't work anymore with… dynamic injection.
So that ship has sailed.
they've been working for the past year, so I tried to make my code work on the latest version, I couldn't.
So… In the meantime, I worked on a much smaller Agent that we can definitely dynamically inject.
Which will give OB ability to at least look at the TLS traffic.
So it's not the… so we used to inject the auto Java SDK engine, but now we're injecting a tiny, small agent that we have.
And we can in the future use this agent as well to maybe do better, thread correlation.
So, like, instrument the executors.
But right now, it only instruments the TLS traffic, so that we can actually capture it in EPF.
**Tyler Yahn** 41:42 Okay, I see.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:44 So the OTEL Java agent, as much as I want to be able to inject, it's not… I mean, I don't know, maybe I don't… I don't know enough bytebuddy, I… I only know a little bit.
So I'm trying to make do with what I know.
But… The way they're refactoring the classes no longer… I don't know. If I revert the changes they've made, to the way they were, and things start working again, but… There's an ongoing project, and they're gonna change all instrumentations in this new way. It's called INDI.
This project's supposed to finish sometime next year.
God.
Yeah, it's gonna give him the ability to dynamically attach my understanding.
into an existing, running Java process and tweak instrumentations, so for serviceability.
Which is why they're doing that, I guess?
Yeah. Unless there's some bite-buddy magic to make it happen.
**Tyler Yahn** 42:44 Okay. Yeah, it might be worth… getting a Java expert, to take a look, but I imagine you're probably right, there's probably some crazy stuff going on in there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:55 Yeah, it's difficult, yeah. I know, I see the people that are working on it, so maybe they can help me, but, I want to get this small agent at least working.
With our Java process, it's much lighter, it's, It's only a handful of instrumentations, and it's… And so, hopefully that… That will be sufficient to get…
**Tyler Yahn** 43:17 But when you say you see the people working out, are you talking about, like, people like Trask, or are you talking external to OTEL?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:23 No, no, within a hotel, there's these guys from Elastic, they're making these changes, and I think Lori is a, engineer on that team, they know this bike buddy stuff much better than I do, so it might be worthwhile asking questions. So, I'll get to it eventually.
to say, hey, what do I do here if I wanted to do that? I know the stance has always been on the project, we don't support dynamic inject.
Which is unfortunate, because it almost works. Or it did almost work for a version like that I had.
from February this year.
**Tyler Yahn** 43:59 Okay.
Alright, well, yeah, maybe we'll talk more about this, I think, in the new year, then. That sounds like definitely worth looking more into, so, cool.
Okay, and then last up, Mario, you had conditional log level for ring buffer errors.
**Mario Macias** 44:19 Yeah, I was fixing today a very verbose error message that was not… was not really so important to be logged as an error. I lowered it to the back.
But then I realized that it would lower to the bug any ring buffer errors, so I tried to provide some… to try a pattern to distinguish between some ring buffer errors that could be logged as the bug and others as warnings.
It's a bit experimental, I don't know if… if you… if you know this error, logable error.
If you don't like it, just close the… let's close the PR, and that's it, yeah.
**Tyler Yahn** 45:04 Hmm, okay. Alright, yeah, looks like it needs reviews, so yeah, please take a look, folks, on the call.
**Mario Macias** 45:11 Hmm.
**Tyler Yahn** 45:14 Okay, cool, that's all the open PRs. Jump back really quick to the agenda, nothing on there. Okay, so this is the last meeting of the year, by the way. I guess I probably should have started with that. The next two weeks, they're canceled, so don't show up. We won't be here.
But yeah, I think that, I guess it's just maybe something to think about is, like, a year in review. I'd love to maybe, in the next, Meaning we have, in January, come along and say, do some, I think, some retrospective, or maybe even some planning around, like, what our goals are for the next year. I'd love to maybe, like.
I'll probably ping people in Slack as well, but next, just maybe think about it over the next two weeks, like.
things you thought that went well. Obviously, getting this accepted into the project, is probably on the list, but but also, like, maybe in the next year, what some of our goals and priorities are going to be. And so, like, there's definitely a lot of, like, vagery around, like, what we can do right now, so I'd love to get some more focus on, like, what we're going to try to do.
And then to communicate that out, I think Obi's got a lot of, attention right now from external, like.
Contributors as well as external, like, companies trying to look at this sort of thing, so… keeping that going by keeping the story, communicating, talking about, like, what we plan to improve, getting people continually excited about it is always great. So, yeah, if you have some really great ideas of what you're looking to do, I'd love to hear about them when we come back, and we can document them, and hopefully get a blog post out for it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:45 Yeah.
That's awesome.
**Tyler Yahn** 46:47 It's awesome. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:48 Hey, I just wanted to mention something I forgot. I think it would be useful for us. I found out, I haven't tried it, but apparently .NET 9 and 10 automatically propagate, trace parents.
I didn't know this, but if you supply .NET a transparent… but it has to be 9 and 10, so, seems like .NET… one of the major issues that we've had with context propagation may Be solved, actually, by the framework itself.
So we just need to be better at reading.
Whatever they've done. It works appropriately for gRPC as well.
**Mario Macias** 47:24 Wow.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:25 So, we just need to be producing the telemetry, and we'll get .NET for free, without actually doing any work.
**Tyler Yahn** 47:33 That's super exciting. Yeah, apparently there's something as well since .NET 5, but I couldn't quite get my head around what that meant.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:42 I read the documentation, but I wasn't quite clear on Are you doing it? Do I need to enable some option? It seemed like in .NET 5, you needed to have some instrumentation loaded, or some… some sort of flag to be on, and then they'll do it.
But apparently this is owned by default now, and… Don't know.
So… I have to try, but it's exciting.
bastions of… eBPF can do.
**Tyler Yahn** 48:09 Right? Yeah. Yeah. So, okay. Well, cool, yeah, definitely interesting. I'm excited to hear more about that one. That's a thing we could add to the blog post.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:17 It works. I had to go try, yeah.
**Tyler Yahn** 48:19 We'll say we have .NET support, even though we did nothing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:22 That was quite cool.
**Tyler Yahn** 48:26 Yeah, probably really quick, yeah.
Well, cool. Any other cool ideas or topics people are looking at?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:35 I was in a… sort of, like, Was it Observable Lightning Talks or something? They invited me to talk about Obi?
So I gave a little presentation yesterday, there were other people, Something about lousy… Wasm?
Mazimoto?
Somebody was talking about adding support for WASM and OTEL.
And, there was somebody from Istio about Proxy, and she actually asked a really valid question, which… I sort of didn't have a good answer to, or I didn't actually have an answer, so she asked us if… You know, having an Istio proxy is actually worse than having eBPF or better.
it's not the case we've actually considered, but I guess, from their perspective, is that if you're running Istio in your cluster, they will collect The metrics and service graphs, sort of.
automatically for you, which is sort of the same thing that Obi does without the tracing.
So, with proxies, you cannot actually see what's happening within the application to do the context propagation, but But you could collect the, the, sort of, the outside telemetry as well.
So she asked a question, which… Might be useful for us to actually do some measurements and figure out How do we compare?
If you're.
**Tyler Yahn** 49:56 Yeah, I think it's, like, I think on, like, the apples-to-apples, like, the service graph stuff and, like, the metrics, I think that that's worth looking into, but, like.
The trace context is kind of a big one, like…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:10 Yeah, yeah.
**Tyler Yahn** 50:11 Like, that's actually, like, one of the reasons I stopped using Istio many, many years ago, is because, like, I could not get trace context to, like, correctly work, and, like, yeah.
So I definitely think that, like, one of the hallmarks that we're able to accomplish is that, like, distributed context, as well as, like.
the introspective into certain services, like, you know, Go or something like that, as well.
So, I think that, like, it's more of a… maybe there's a competition there, but I think there's just a lot more feature sets in Obi that we're able to handle.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:41 I mean, it would be good. I saw an issue today open, somebody complaining about performance impact, instrumenting Redis.
We gotta look into that, I guess.
**Tyler Yahn** 50:50 Oh, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:51 Yeah.
But, you know, Redis is a really fast database, so it seems to spot if we're adding any overhead.
Might be, but probably we're hitting some probe.
or something, But, Pavel, he's opened a couple of issues, he's very good, he provides a lot of these, like a GitHub repo with reproduction, so… It should be, should be easy to investigate.
We're all back for vacation next.
**Tyler Yahn** 51:18 Yeah, right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:19 Yeah, I'm taking off.
Until next year as well.
Oh, tomorrow.
**Tyler Yahn** 51:25 Well, cool.
Yeah, I will, I'm gone the last two weeks as well, although we'll see how if I leave the computer behind, but yeah. Maybe on that note, Cool. Everyone, good to see you, good to take some time off, hopefully get some rest, and we'll see you all in the new year.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:45 And please don't be angry with us if we don't jump on your pull requests.
Because most of us will not be here.
**Tyler Yahn** 51:53 Yeah, absolutely.
Okay, everyone, I'll talk to you later.
**Stephen Lang** 51:59 Right.
**Mattia Meleleo** 52:00 Bye. Bye.
