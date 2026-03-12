SIG: eBPF instrumentation
Date: 2025-07-16
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/VoK0CkVTQlqCxrIoh1TAYHKzROY_N1gIHzu5vsBPh2Rr_4TY0fx-DAK5wfp72ZDA.GVtZa-OB0ejhOE2s
============================================================

## Zoom Recording Transcript

Tyler Yahn 00:00:57 Hey!
Mike Dame 00:01:01 Hello!
Tyler Yahn 00:01:03 How's it going.
Mike Dame 00:01:05 Good. How about you?
Tyler Yahn 00:01:07 Good.
Mattia Meleleo 00:01:08 So.
Stephen Lang 00:01:10 All right.
Tyler Yahn 00:01:28 We could probably get started here in just a second, just getting set up. Start sharing my screen. If you haven't yet. Please go ahead and add your name to the attendees list. If you have agenda items, go ahead and add those as well. And yeah, we'll jump in in just a second awesome welcome. Everyone. Yeah, thanks for joining to start us off, Nicola. You wanted to talk about Java Tls, support discussion.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:02:14 Yeah. So I just wanted to bring this up here. See?
whether there's something that is acceptable or we want to do. I remember that you and I, Tyler, talked about this in the in the Vela initial donation proposal to open telemetry about. You know, this project mainly focusing on compiled languages, or not actually going into space, where we already have really good support. And one example of that is Java.
But I thought, this is important. So I just wanted to bring it up even though it's maybe not the main purpose for ob at the moment. I think it's important that we have good baseline support for any programming language without going into really bells and whistles, such as extensive Java support.
But one thing that's been a sticking point for the current support in Ob for Java is that it does not support Ssl. Tls.
And the reason for that is because the Java itself. The SDK, the Java Jvm. SDK, is using its own implementation of Tls. It's not using Libssl or any of the sort of native libraries that we can tap into with you probes.
So I've looked into this in the past, and we always had an an approach in mind that. We thought that we might implement this pure Ebps solution.
but it's it's a lot of work.
And essentially, the reason why it's a lot of work is because uprobes can now be set on anonymous code regions. So it's just a limitation of the uprobe approach. It requires that there's a filing the file system, or an unknown number they can attach to.
which requires that you be tracing the Jvm. Make it run. A bunch of Sys calls to unmap the memory region for the code cache and remap it to say.
every my file, or something like that, that it will have an ino number.
I'm not sure that Jvm. Will let us do this. It's all hypothetical. At this point there was a sort of a research effort. We proved it out with small programs. But I don't know if that's going to crash the Jvm. And there's lots of open questions there. 1st of all, like, Can the Jvm. Actually allocate an additional cold cash segment.
and then we have to watch for that, and then, like instrument, the Jvm. To do that and then catch it after it's allocated. Then repeat this.
and there's also a lot of trickiness related to the actual instrumentation of generated code.
One thing is that what the what the start address of a generated method in Java is changes from version to version, and it's changed quite a bit in the last few years.
So there will be have to be Jvm version detection, and knowing which offsets and the Jvm itself can run in multiple modes.
So reading buffers is kind of complicated buffers can be compressed.
They can have this mode where they have minimal headers or normal headers, and so so about it.
I guess now, a year ago, more than a year ago, like Valery, from data presented approach at Kubecon, EU. About how they do this for their universal service, monitoring.
So they technically attach a tiny, tiny Java agent that they dynamically load and that helps them find this in the from the Jvm. So if you have a rounding Java process. You can attach a tiny agent to it, and you'll get access to the buffers required to do Tls correlation.
now, I never thought that Tls is actually very important for Java, because I always thought people would likely serve services.
Externally through some sort of proxy. That's not going to be directly Java likely not terminate Tls or the Java layer, but for outgoing calls, client calls is very important. So anytime you're talking to a remote SQL database that's cloud hosted. You're likely going through Tls.
so ob is unable to see any of those signals.
So you know, it's just about tracing. But metrics don't show up.
So I wanted to bring it up here as a proposal. Why, we want to do this. I yeah. And if it's not acceptable. Then.
I mean, that's that's fine, too. And the answer is, no, we don't want to do this in the community project, and I mean, likely we define it, we'll make a decision whether we add it as a additional feature on top of the yeah, just bring it.
I have a prototype that works based on what Billy was talking at.
Cube phone talk.
Tyler Yahn 00:07:31 So have you. So you're talking about like a small agent loading alongside in the Jerry. I'm sorry in the jvm, and Is this something that like would exist already with the the open telemetry, auto instrumentation, like they already have an agent that does that as well like. Is that something you can look into.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:07:52 Yeah. So there's 2 approaches there.
one is. We can have a standalone agent that's unrelated to the open telemetry. Java agent. That is just part of the ob repo that only does abpr support the reason why the Java SDK agent.
So we initially thought that, okay, fine. If this does not work for Java applications, what we would like to do instead is actually dynamically load the Otto SDK, Java agent. Why not load that? If you can load it. Anything. Right?
Yeah. So we wrote that support. And it's experimental in the Ob code base. The problem is that the Hotel Java SDK. Officially does not support dynamic injection.
It does work, and through Gregor from Grafana I gave him a patch that he actually contributed where we could dynamically supply options to the Java agent, such as the exporter and all these other things.
The problem is that it does work. At least I've tried it with Http. And SQL. With postgres. That seems to work fine. But somebody in community have reported there's a couple of reports that various instrumentations do not work.
I think it's just how the instrumentations are implemented. They don't anticipate that somebody would be loading an agent dynamically.
There's trickiness to that, you know, if you're instrumenting classes that are loaded by the Bootstrap class loader, the Java one that the Jdk uses they end up.
I don't know. You need to inject things in a specific way. So, for example, one example, that community pointed out is Grpc does not work instrumentation in Java. If you dynamically load the agent.
So yeah. So it requires a restart. And we're back to.
you know, would be nice if we could just not have to restart any application and just be able to load, then remove so, having a small agent makes it easier to do that.
and this agent can be built in a way that will never interfere with any other agents that the customer may be running. So you have a customer that's perhaps using some sort of like a security agent, I and my also understanding is that the Java Hotel SDK agent is not guaranteed that will work with other agents together.
So if you have, for example, loaded an agent that does some sort of security check. Maybe. I don't know either vendor agent and you load the Java SDK agent together. They may not work, or they may clash with functionality because they both try to instrument the same thing, you know, so.
Oftentimes people don't anticipate that it'll be somebody else trying to instrument the same thing.
When you have something small and targeted like this, then you could potentially have a better control over conflicts.
Tyler Yahn 00:11:09 Would it conflict with somebody? Tried running this alongside the Java, or sorry the open telemetry.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:14 I actually tried that.
I can load both dynamically for my tests. It does work, and that should be one of the tests. If we ever decide to do this.
that you should be able to load both, and there should be no conflicts or any interaction between them.
Tyler Yahn 00:11:35 Yeah. So my concern is is definitely that, like, there's duplicate ways to instruments of Java service. For with open telemetry, which I don't think you're oblivious to and I think that that's like a concern from the open telemetry like community perspective.
But I also see it as like I mean, there's different technologies being used here, right?
And I think I think that that's worth exploring, in my opinion, because what you're describing is to running a small agent and essentially doing the instrumentation and processing out of band using Evpf. And the Java agent is is a you know. It's not in the same thread, I guess, but it's it's definitely a different model for constructing that right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:25 Yeah, this is, if you will, very similar to the opentelemetry Ebpf profiler loading a tiny agent for Java, so they can actually do the work for Java. I know that's not contributed as part of the elastic distribution.
It's not part of the Ebpf profiler, but so you can have a Java profiler. That's just purely like instrumenting, using the Jvm instrumentation infrastructure that requires to be loaded on start. And all these things so that you can actually do profiling. But with the otl Epr profiler you need a tiny bit of support.
So that Java trace context propagation can work together with the Ebpf profile. So they do the same thing. They load a tiny agent that.
Tyler Yahn 00:13:18 Just does a little bit of.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:19 Help to get the stuff across to the Ebpf side.
Tyler Yahn 00:13:26 Perfect. I see you have your hand raised.
Rafael Roquetto 00:13:28 Yeah. So what I'm about to say just to be clear I know both me and Nicola from Grafana. But I swear to God, I don't have my grafana hat on. It's just something a little bit of tangent of the agent argument that Nicholas, putting when I did the working with Node for request correlation to realize it's well pretty much impossible to to get it right only with Ebps. So I believe that we, you know. At least I I think we should be, you know, open minded to extending beyond Evpf for for this corner use cases. I I mean the good thing about Evpf is is very non intrusive, right? And it's like, you're not touching any user space programs. You know, you, you don't have to mess with anything. If if ob dies, for instance, or any Ebpf agent dies, the system continues like, so this this is why I think we should strive to do as much as we can with Ebpf, or like no intrusive code. But there, there's a little bit there's gonna be use cases where we're gonna need to extra help like think outside of the box. If you want to achieve like, literally like auto instrumentation in a in a good quality. So we do the same thing with Node right? We inject a little payload in the node app to help us correlate the requests, and then push it back to to Ob. And ob does the like, as you said, out of band work. And I I feel that this is going.
It might be the case for other technologies as well where Ebpf folks short, so it's just like a more like broad thought of in this case, it was naming this an agent, because that's what it is, and then it conflates a bit with like the hotel agent or SDK or whatnot. But really, the way I see this is really you know, just other means of us trying to do something that it would otherwise not be possible. So yeah, it's just that, like a random thought.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:53 Yeah, so.
Yeah, go ahead.
No, it's just a thought is like, so if you run ob on Java, if there's any Ssl.
Tls, you will not be able to see anything. That's pretty much it.
Then you're resorted, then, to use the Java SDK to do instrumentation. But then that requires that again you modify your your start scripts to add the agent or inject it somehow.
Of yeah. So we, I guess, like, I said, we try to inject the Java agent dynamically. But there's some caveats.
Rafael Roquetto 00:16:33 I I think a good way of seeing it, but obviously it's not. The same is is. This is more like towards a you probe that is not a you probe, then, actually an agent. It's just a way, a hook that we use to instrument an application obviously unlike you probe. We gotta be way more mindful because it has consequences. We are injecting things on on target process. You know, we can. We have the potential of messing things up just like with bps. Probe right? User. Sometimes, you know, we crash applications. So I'm not saying it's the same or ignore that.
I guess what I'm what I'm saying is, there's gonna be cases where your problems will fall short. I know they are good. For go, for instance, we get a really good go coverage they are good for, you know, native applications.
But I mean Nicholas coming from Java. I'm coming from node support. I spent like 6 weeks trying to get Node to work only with the you probes, and I gave up. It's pretty much impossible because of how a lot of of the sync operations happen at the the Javascript engine level, and we don't have any access to that from Evpf. So if we want to support a few technology like 1st class, and you know, for a baseline not like replacing hotel sdks or anything like that. Nothing complex. I think we should be open. But that's just my personal opinion. And I I like Nicholas said. We're a community. I am just trying to put a like a a food for thought, the, you know.
Wish we should be open to, maybe, you know, go going beyond Ebpf when and if Ebpf fall short. So yeah.
Tyler Yahn 00:18:23 Well, I'm not. I'm not opposed to that.
Rafael Roquetto 00:18:25 You.
Tyler Yahn 00:18:26 You know, if you take a look at what we did for go to tie into the manual SDK stuff, we had to go and add our own SDK into like the trace Api, which is something that our you probes, then tie into like. It's not unprecedented to see these kinds of things.
It's more just like the long term like strategy that you tell users of open telemetry like what they should be using.
I don't. I don't see that as necessarily a strong problem. I guess the other concern that I have.
In fact, I see it kind of as like a benefit just to kind of finish. That thought is to have different ways.
Instrumenting like you obviously have different ways of instrumenting. One would be in Evpf, and it'd be kind of nice to have epf support all of these different languages.
i. The feature development, though, is a little bit concerning. So if we go down this route like it makes a lot of sense to me that we would want to support all of the things that we currently support. So like red metrics for these Java transactions. Right? So, Tls is going to be important.
Providing specific instrumentation for like Java packages. And that kind of thing that okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:38 Yeah. So no, no, we're not going to go into that. I don't want to do that. If we're going to start implementing the Apache. Http client. Okay, go. Http. No, no. Okay. Http, no, no, we don't want to do that. Which is why I found this presentation by Valery from Datadog very interesting because he they have discovered a way how you can specifically instrument just 3 Java base SDK classes and get what you need for Ebpf, that's all that this is about not going to anywhere other than that. That's not the point.
We don't want to replicate what Java SDK does auto. Java SDK.
Tyler Yahn 00:20:14 Yeah, yeah, I guess that's that's my only concern. I just wanna make sure that it's clear that we're on the same page there. Because, yeah, I I definitely at that point, I think we should share anyways, like, we're not going to do that. So that I think that's that makes sense.
Yeah, I don't see why we wouldn't want to go in this direction that you're describing. Then, like, I mean, if we're supporting other languages using the Ebpf technology. We would want to support Java. Obviously, like we want to have it for any language, including go or node or anything like that, you can turn it off if you wanted to go. Use another, you know, service or another way of technology to like instrument it. But like, I don't see why, that's different here. And it sounds like that's not going to change. So yeah, this sounds sounds like something I would accept as a proposal. If that's what you're asking.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:01 Okay, yeah, that's all. I brought it up. I just wanted to discuss to see, because I know that we initially discussed that. You know we should not be spending a lot of effort into languages that are well covered by other technologies. But this is just kind of with the initial goals that Ob had as a project just completing that picture, because Java is a very common language, and if people are installing this and running, obviously it will fall short and.
Tyler Yahn 00:21:32 Yeah, yeah, failures.
I mean, I I still have really big goals to have rust covered here. But I don't see why that's gonna conflict with this. So yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:44 Yeah, rust is interesting. Now that we added the custom probe support to be able to run the manual instrumentation. So I wonder if we should try to do that for rust next.
Tyler Yahn 00:21:55 Having.
I think that might be easier to do in rust. But I
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:00 Unless it's pretty symbols. I know that some rust build processes, remove symbols by default, so that might.
Tyler Yahn 00:22:05 Okay. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:06 Some grief, but maybe that will be a requirement if you don't have symbols. No manual choices same for go like if you strip it completely. I think it will not work of.
Tyler Yahn 00:22:18 Yeah, that's true. Yeah, okay, cool. So it sounds like, you have a Poc on this. I'm guessing we'll see some Prs related to this coming in is guessing the plan. So yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:32 Side is is very simple. There's 1 Api that they suggested in that the Ipc the Ipc Api they're using. They found one that was presented. That's extremely fast, and works well with containers, and so on. So I was just going to use the same one. So that's just one small K probe, we need to add, and then is the agent which it's not a lot of code. So I will make a separate Pr for that.
make file changes to build a jar and so on.
Tyler Yahn 00:23:10 Awesome. Alright! That sounds good. Thanks, Nicola.
Rafael Roquetto 00:23:12 Just a thought about rust and other languages like C plus, plus, or even see what we should support when we we take on that work. For the case where symbols are missing is just loading, like it's very common for especially for these projects to provide symbols, separate files like.
So we should support. Just if your buyer doesn't have symbols, you, you know, hope most of these upstream projects provide symbols, separate files. You just load those symbols from this files and and use that. So we could look into that as well. Just just, I'm just mentioning here. So we remember it later. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:50 Well, we maybe open an issue or something. Yeah.
Tyler Yahn 00:23:55 Okay, cool, Raphael. You wanted to talk about contributing that Md, that saw this got merged recently.
Yeah, no, this is a very different thing.
Rafael Roquetto 00:24:06 No, not that one.
I think it picked up the link by mistake.
Tyler Yahn 00:24:12 Oh, okay.
Rafael Roquetto 00:24:14 So yeah, I I raised the Pr. And then it got merged with contributing.md, I forked it off the go they go they go auto project. So you'll see. It looks very familiar. But you know, have a look and propose changes. You know, it's by any means set on stone. It's just like a starting point it's yeah, I I just thought I would start with something and.
Tyler Yahn 00:24:44 Yeah this looks good. I'd I'd reviewed it before. Oh, I guess we might have this in 2 places now.
Rafael Roquetto 00:24:52 I moved it from the
Tyler Yahn 00:24:55 Oh, it was moved. Yeah, it was in review. Okay, yeah. Yeah. Okay. Cool. Alright. Yeah. That's that's fine.
Rafael Roquetto 00:25:00 Yeah.
Tyler Yahn 00:25:01 Perfect.
Yeah, so.
Rafael Roquetto 00:25:03 You guys have a look, feel free to roast it, change it. You know the usual.
Tyler Yahn 00:25:10 Yeah, please don't roast it. Just please provide valuable feedback.
Rafael Roquetto 00:25:14 Yeah.
Tyler Yahn 00:25:16 Okay.
But yeah, thanks for putting that in. Okay, Steven, you're looking for a sponsor for community membership contributions being here and here.
Stephen Lang 00:25:29 Yeah. So I think I need one. I'm sure I can get one from Grafana hopefully. And then I need another one from another company.
So this is just looking for a.
The initial membership.
Tyler Yahn 00:25:45 Hmm, okay, yeah. I'm trying to find something in. I know, David.
He's also going on leave soon.
Where is this other? Sorry? Did this.
Stephen Lang 00:26:07 The 1st link is to prs in
Tyler Yahn 00:26:10 Oh, this is just issues that author. Oh, okay, I see. I see. I see.
Stephen Lang 00:26:14 Yeah, cause. I think you you have to provide some kind of evidence to show what your contributions are. So there's a No, no.
Tyler Yahn 00:26:20 Yeah, absolutely.
yeah, I'm just looking so it looks like both Raphael and oh, and so I'm sorry. Nick. Steven, are you a member of Grafana is what you're asking.
Oh, I see. So you're looking for outside of Grafana. Okay.
Stephen Lang 00:26:36 Yeah. So so I need in in order for the open telemetry, community membership. You need 2 sponsors.
One of which can be, you know, from Rafana.
But then another needs to be from another company that needs to be from 2 different companies.
Yeah. So I'm just wondering if there's anyone.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:56 Would be sponsor. Yeah.
Tyler Yahn 00:26:59 Well, yeah, obviously, I think Nicola sounds motivated. You can put me down as well. I'm Mr. Alias. I'm not on any of these, but I can. I can vouch for it. So yeah, happy to happy to do that. Yeah.
Stephen Lang 00:27:12 Awesome. Thanks.
Tyler Yahn 00:27:13 Yeah.
it should ping me so just if it doesn't, I'm also in slack, so you can find me there. But.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:20 Yeah, just.
Tyler Yahn 00:27:21 Otherwise, yeah.
Stephen Lang 00:27:22 Yeah, I'll do that. Thanks.
Tyler Yahn 00:27:24 Yeah, awesome. Well, welcome to the community as well.
Stephen Lang 00:27:27 Thank you.
Tyler Yahn 00:27:29 Okay, cool. All right. So, moving on, I wanted to double check into our milestone. So we have a few issues open here. Let's see, I don't know if I saw Mark on. I didn't see Mark on. So there's documentation. Oh, okay.
I think he was going to take on this migrate to Bela docs to opentelometry, if I remember correct.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:50 That's already in progress. I believe that Severin and Mario are going long office.
Okay?
Think Mario is helping.
Well, I think there's a chatter on somewhere, I forget where, but most of the stuff is there. So
Tyler Yahn 00:28:10 Yeah, wow, this looks great.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:12 I think Mario is just removing bunch of bailout references and tweaking some stuff. And yeah.
I think slowly but surely, that's that's happening. So Severin and Mario are.
I think Severin did the initial dig.
Mari is away today. So it's a holiday, I believe, or in Spain or.
Tyler Yahn 00:28:34 Yeah, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:36 So.
Tyler Yahn 00:28:36 He's European. So I'm pretty sure this summer you just take the whole thing off. Right?
Yeah, okay, that sounds good, perfect. Oh, then, yeah, this is going a lot further than I thought. So, okay, I've updated that I think also to ensure this documentation, how to exclude services is still something. This looks like it's blocked. We talked about this last time. I can't believe I'm forgetting.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:00 As soon as the dogs get merged, I think it's fine. It will be yeah. Then it's just yeah. Okay.
Tyler Yahn 00:29:06 Yeah, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:06 Do have it? Yeah.
Tyler Yahn 00:29:08 So this is kind of yeah, maybe it's even folded into this one. But anyways, okay.
awesome, all right. And then there's an audit tasks and these changes.
I thought this was resolved. Last week I thought there was a Pr.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:24 A lot of changes did go in. I'm not sure it's the last, though.
Tyler Yahn 00:29:29 Yeah.
Rafael Roquetto 00:29:31 You can assign this one to me.
Tyler Yahn 00:29:33 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:34 That's right.
Tyler Yahn 00:29:40 Okay, yeah, I'm like, I'm pretty sure. But I I have to double check.
okay? And then audit the Bayla name system. This is again something Mario's picked up.
Another one that I was realizing at the end of last week is a vanity, URL, which I'm sure Mike is already getting flashbacks at this point.
like, we have this vanity. URL, we can definitely, it's not like that hard. It's just the deployment thing could be a little Iffy if, instead of releasing it as this, like Github URL, we can have the package. Names be, you know, follow open telemetry standards and have a nice, short, concise things with a prefix that's related to opentelemetry.
which I would prefer. The hard part is like, what do we want to call it? I'm a big fan of Obi, but I know Nicola is also like cautious about this one. So maybe just a question around that like, what do we want to call it?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:36 No, I think it's fine. I just don't want it to kind of make branding out of Ob. But I think for a package name is fine to be a shorthand. I don't know. I'm not a lawyer, but I I don't think it's ever gonna be a conflict because we're not selling home improvement.
Tyler Yahn 00:30:53 Yeah, exactly. We're not in the same market space to to conflict. And yeah, with trademarks. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:59 Yeah.
Tyler Yahn 00:31:00 Okay. But if that's the case, I can. I can put a Pr together to try to propose this to the Vanity Urls, and then.
hopefully, things are still working over there, and we'll get this deployed some. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:14 Awesome.
Mike Dame 00:31:15 Yeah, I'm happy to help out if you need help with anything on the Vanity. URL stuff. I don't think I have access to the projects that we ended up deploying that new image in. But everything, I think, is pretty self service now, through the the new or the repo that we set up. I think we ended up granting things the right Gcp permissions. That was our big problem that we had before Tyler.
Tyler Yahn 00:31:39 The I, Trask and and others are starting to mess with the Ci system that we were using. We're using Circle Ci, I think, and they're trying to migrate us to github actions. And it's reverted twice now. So yeah, I will.
I think you're right hopefully. Yeah. But yeah.
Mike Dame 00:31:56 No, I have. I have seen some updates come from that. I just think. I guess my point being that, like the infra side. The actual Gcp side should be good. That was a big thing that we had hit, for there were like permissions that gotten that had lapsed, or something. So as long as like the tokens and the authentication is the same, then yeah, the migration to to Github actions on its own is its own thing. But yeah, happy to help out or lend a hand with that. If you need anything, just ping me.
Tyler Yahn 00:32:24 Okay, yeah, that sounds good. I will do that.
Okay, that's the last for our milestone, which sounds like we have a good grasp on everything needed, which is great.
Next up Nicola, you want to talk about the kernel, 5.4 support open issue.
Yeah, it's just refund.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:41 It up. I think it. Somebody brought it up, and this has been brought up before.
I think there's still some kernel distributions that we don't support that are common in in. I think cloud fighter images like maybe Amazon Linux, something like that.
It will require the major changes that obviously we have to change the ring buffer to a perf buffer.
Yeah, it was, maybe that's okay.
What people think here. I just wanted to bring it to everyone's attention. If you I don't think it's a big change. I don't know what the downsides might be.
Rafael Roquetto 00:33:20 The downside would be that they that we need to to deal with concurrency right now, because now we we're gonna have.
we need to synchronize between the perfect buffers, whereas the ring buffer is all serialized into. You know the cpus. Take care of it so that that might be some work to do.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:37 Okay. Well, then, it's not gonna be fun.
Tyler Yahn 00:33:43 Yeah, I would like to know? I think a little bit more about what platform this is on.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:48 The Linux. Yeah. Because I, when we initially made that Scott, I kind of looked at the long term support for various Linux distributions, and it didn't seem like it was going to be much longer before these older kernels that don't support these features are going to be around and redhead, which likes to support older kernels, are backboarding everything. So I've had 4 18 supports, ring buffers.
Tyler Yahn 00:34:17 Oh, really. Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:18 Yeah.
Tyler Yahn 00:34:19 Wow!
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:19 Yeah, they. They have a long term support on 4, 18, and they backboarded a lot of the Ep features. So we'll work on red hat, 4.18.
Tyler Yahn 00:34:31 That is cool. Yeah, I think at some point you have to draw a line in the sand. I think it's worth investigating, like you just did, trying to make sure that we can maybe switch to something. But I think if we have like.
like reasons why we aren't doing that, or like we, we need some sort of ring buffer and not using a perf buffer then, like.
I think it's also fair to say that at least, for now we're working on stability. We're working on feature sets. We're working on all these other things like backers, compatible support for 5.4, which I'd like. That's I think that may not be a top. Priority is all I'm saying.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:10 Yep.
Tyler Yahn 00:35:10 I'm not saying we shouldn't do it. But I definitely think that like, yeah, I do know that if this was like, you know, if this is on like Amazon, or something like that, then it does provide some motivation to try to support this.
or to find somebody in their cloud platform to tell them to upgrade. But yeah.
sometimes, obviously you can't. That is also a situation. But I think that maybe we should try to.
Yeah, I think I think moving forward is is something we could try to add support to. But right now I would definitely not prioritize this.
Rafael Roquetto 00:35:47 Am I? Yeah, I'm in agreement. And like, I don't think this like looking at the issue description. Now it's not. It's not as trivial like the well the other downside of replacing the ring buffer buffer, I mean, it's not as bad as having to do with concurrency, but they usually have more overhead, and the map type per CPU array we use. It is everywhere for a scratch memory.
Then we would need to synchronize on that as well, because then we would. We would have multiple cpus accessing the same maps and stretch memory. So it's a it's a bug magnet if we we need to be very careful if we decide to go down that road, if it's just a 5, was just 5, will, you know.
But and just raising those square, those issues up.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:35 That's why I brought it here so.
Tyler Yahn 00:36:37 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:39 Okay.
Tyler Yahn 00:36:41 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:42 Okay, interesting. Mattia believes that is available.
Mattia Meleleo 00:36:46 Yeah, if I recall correctly, that map is already present in that kernel version. But the ring buff note. Yeah.
I was thinking if we could.
you could have a separate version of the probe with one with the ring, buff one with the perforate. But it's it's a little bit of overhead, and I don't know how many customers are requesting this. If it's just one, I I don't think it's worth the the effort, because we we also need to change to support both in the user space.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:37:22 Yes, yes, it's not as simple as the debug probe and non debug probe. Now you have the.
Mattia Meleleo 00:37:28 Yeah, correct.
Tyler Yahn 00:37:34 Okay, I think, yeah, I I think maybe I'd like to get some more information, but probably ended up just just deprioritizing us, maybe even like saying, we're not planning to support this in the near future, so we can close this. But well, I'd like to know a little bit more before we do that. So okay.
all right, last up, I just wanted to do a quick check through of our open Prs, making sure nothing's blocked. I think we've seen these a few times with add the process minimum age to filter out short the process, something we've talked about. I think a few weeks now. It's still just, I think. Maybe take a look where we're at.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:38:12 It's on me. I picked up the branch yesterday. I just haven't had a chance yet to figure out what the bug is need to help the user.
So.
Tyler Yahn 00:38:24 I'm gonna take a look. Yeah.
cool, awesome. Well, yeah, I appreciate you jumping in there and take taking a look. That's yeah. Gonna be very helpful.
Okay, I also saw you jump into this one. The Kubernetes package upgrades. This is something that Mario wanted to take a look at. Seems like, the Pr needs will need some help. Yeah, okay.
yeah, I think you're right. It does. It's gonna need some help. Okay, so we just need somebody to, I think. Maybe take it. Take this on
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:38:53 I broke our Kubernetes Api client, or something that changed. So we need to change our code to adapt to the new client. I think.
Tyler Yahn 00:39:01 Okay.
I will put help wanted. I will try to take a look eventually. But yeah, I think this is if you if you have cycles, and you are familiar with the Kubernetes Api and the Kubernetes packaging would appreciate the help helping us move this through. If you have any questions about how to do this one. You don't have to do it in this branch. You could fork this. You can. You can just start your own branch and do the upgrade as well. If you are, I think, Approver, but maybe just a maintainer. You can push directly to this branch, but otherwise, yeah, just just fork the branch and create your own. So yeah.
for those listening to the recording, we're still looking for help.
Okay, next up Mysql support, prepared statements or factor, event handling.
Mattia Meleleo 00:40:08 Yeah, that's me. So this Pr is almost ready. I need to split this up in multiple smaller prs, because right now it's a solid of refactories and new features and bug fixes also spent some time investigating some some funkiness of the tests, and I noticed that when the data buffers are coming from from Ssl connections.
the response is cut after 4 Byte.
I, I need to investigate that. Better so, for now, I just commented the error case, which is the one that uses the response buffer and the other test tests are passing. But yeah, I need to to investigate that better in a separate Pr.
and I also have one auth test failing regarding Kafka.
Yeah, I also need to look into that. I I don't know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:13 Yeah, this may not be you. I actually noticed this, too. All of a sudden Java Caf is failing. I don't know why.
Mattia Meleleo 00:41:22 Nice to know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:23 Yeah, I will look into this today. Yeah, it's Jala Kafka. It's it's something changed. I don't know if it's some other package that we upgraded, or something.
I'm seeing 2 of this do on my Pr. But then we saw it as well, because we pulled up a Pr. To Sync. Bayla's version with the Ob latest, and our test started failing with Java Kafka.
So it's something that's existing in the code base. But it wasn't caught in the actual Pr.
so I'm going to look into this today.
Tyler Yahn 00:41:59 But also my.
Mattia Meleleo 00:41:59 Nice.
Tyler Yahn 00:42:00 It kind of sounds like one of the things where we're pulling in like a latest version, or we're not pinning a version. And it's something got upgraded in the background, maybe.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:09 As possible. But yeah.
Tyler Yahn 00:42:10 Yeah.
okay. But other than that. So, Mattia, did you have an issue to track the unresolved issue that you wanted to follow up on.
Mattia Meleleo 00:42:22 Sorry? What was the question?
Tyler Yahn 00:42:24 So you were saying that you were seeing some test errors that were unrelated to the Java thing we were just looking at, but like you said that there was a something that you wanted to follow up on after this Pr.
Mattia Meleleo 00:42:34 Yes, it's the ssl. Response buffers. I need to to have a look into that and see why are they being cut in my, in my case.
Tyler Yahn 00:42:45 Yeah, and so is that specific to this pr, or is that a general.
Mattia Meleleo 00:42:49 I think I think it's a general issue but I need to to verify that I need to.
Tyler Yahn 00:42:56 So can you just.
Mattia Meleleo 00:42:56 At the end of.
Tyler Yahn 00:42:58 Can you open an issue just to to track it to make sure you're not, I'm sure, if you're seeing it, other people are probably also seeing it. So we can just start that communication there.
yes, sure.
Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:08 Yeah. So my tea, I think I do have an idea what's happening, but I'm not sure how we will fix it.
The So for the Sso transactions. But I think you're dealing with Mysql as well. Right.
Mattia Meleleo 00:43:26 Yes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:26 So. So what we do is as soon as we switch to direction of the traffic, we take that buffer and we make it the response buffer, and we let the event go.
So the challenge there is that it's not easy to tell when a request will eventually finish.
So so let's say we started a request, and we collect all their bytes for the request. Then it gets served by something right.
and then they start sending response. If the sender, when they respond, send us just 4 Byte or something really small.
we don't wait for the next packet.
The challenge is like, if we start waiting. We do that for Http, because in Http I did find a reliable way that maybe I can tell when the packet finishes. So it has this whole complicated business of delaying the event, sending until we've seen enough bytes, and so on.
So when they may mess us up is that they send us 4 Byte, and then they'll send us another 1,000.
The 1st 4 are the we receive. We switch the direction of the traffic. We say, okay, somebody's responding. So let's just take this and send the event to the user space.
So we have to somehow wait a little bit for the data to come back.
But then, if we wait for the packets and they don't do Tcp close, we don't know when they're finished.
and there's no way to. So the way we do it in Htp is, we see, on the same connection, pair traffic going the other way again. Then we say, Oh, let's push the previous event out, and then start a new event.
But that assumes that there's going to be some traffic going again on the other.
Yes, you can detect I'm all open to ideas how we can make this better. I haven't figured out a solution.
Mattia Meleleo 00:45:33 Actually I do. So. This behavior is the same for the non. Ssl, if I'm not wrong, and for Mysql, I have a check, since we know that the header is being sent before, and it's exactly for bytes I have a check in there which caches these 4 Byte, and do not admit the event, and then, when the next packet comes, it will get these and emit them.
But for some reason, for the Ssl. One doesn't work. So so I need to to investigate that also. One other thing that I wanted to mention is and I forgot. It's that the Ssl. And the non Ssl. Tests are reversed. So.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:17 Okay.
Mattia Meleleo 00:46:18 The yeah, the Mysql Docker file actually doesn't use Ssl, but the default authentication method is caching to password, which requires Ssl, so the server creates a couple of keys by default, and connects via them and the postgres one uses Ssl. But only for the Http. Server, not for the database connection.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:44 Sorry about that.
Yeah.
But so so this is actually quite cool, that now that we have the Ebpf parsing of Mysql, you can kind of do this stuff. You know the protocol. So you expect that? Okay, 4 Byte is not enough. Let me wait a bit more.
Well, with with that with us doing purely in user space, we wouldn't have been able to do this.
Mattia Meleleo 00:47:05 Yeah, we would need to to cache. Well, we can. We can't control from user space, the the packets. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:12 Yeah. Or maybe we send some. Write some Ebpf map from user space and tell it. Oh, uses Mysql. So wait a little bit more or something like that. But still, this is better that we're doing this in Ebpf.
That's 1 of the advantages, and maybe we'll figure out a way how to kind of reliably detect that.
Expect a little bit more bytes here.
because we don't know the protocol. Maybe 4 Byte is enough, you know, like I don't know like that if it's an unknown Tcp protocol like. But yeah, you can't technically.
Mattia Meleleo 00:47:46 Oh, also one other thing I'm remembering stuff. So in this Pr, I also added some cache for the protocol type. So if we figure out that the connection is going via my sequel.
For a certain connection infoty, or whatever is named the stuff. Yeah, I catch the protocol type, because I noticed that that the protocol arcs was per per packet, not per per connection.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:18 Very cool looking forward to it.
Thanks, man.
Tyler Yahn 00:48:24 Cool. All right. So, Mattia, can you definitely open up an issue for this? Ssl thing? But also if you could also open one for the the testing ssl, like mix ups and that kind of thing. Just so we can capture that as well. Obviously not like high priorities, but definitely something we don't wanna just
Mattia Meleleo 00:48:45 Yes, sir.
Tyler Yahn 00:48:45 Forget it.
Mattia Meleleo 00:48:46 A couple of issues I had in mind to fix it myself. That's why I didn't open anything. But I will. I will.
Tyler Yahn 00:48:54 Yeah, I I do that all the time. And then I then I find that I have 20 Prs sitting in my queue. But yeah, yeah, if you just want to capture it. Yeah, even assign it to yourself. That sounds good. If you, if you want to work on it. Just we don't lose it. Yeah.
Okay, cool. Next up the add bound checks to extract Json string from the Json, Rpc.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:20 Yeah, this is in progress. We had a user contribution that they contributed the Json Rpc protocol for go but we immediately found that the tests they made were failing quite frequently, so became unstable. So I think the user is trying to fix this by putting better support. I think it's still ongoing.
Okay, I think Rafael is actively looking as well helping them out.
Tyler Yahn 00:49:51 Perfect. Okay, yeah. Looks like a work in progress. Let's keep an eye on it. Then.
okay, open telemetry. Ghr images and integration tests. Use these. So I saw this as well. This is for Mario. It looks like this has approvals 2 days ago. Looks like the integration tests are failing, though.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:13 I don't know if this is.
Tyler Yahn 00:50:14 Related.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:15 There, all of them failing like that means there's some pool problem. So I don't know.
Tyler Yahn 00:50:23 Yeah, we could just the error code.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:27 It shows 18 or 17 if it's an image issue.
one status one. So that's bad. Okay, so that's not a failure.
Yeah, it just probably couldn't pull the image. So I think it's a I need. I think Mariani probably just needs to fix the point to the new image or something.
Tyler Yahn 00:50:49 Yeah, given, this is a test, or this is up here to change the the actual images we're using. I'm guessing there's just some permissions issues.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:56 Yeah, yeah, some, some issues like that. Yeah.
Tyler Yahn 00:50:58 Okay.
Unexpected error in the rails. Image test.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:04 Yeah.
Tyler Yahn 00:51:06 Looks like this went through. This has been updated.
Okay, so maybe it's something else. Now, yeah, it looks like, okay, just something. Mario can take a look at when he gets back, so.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:16 Yep.
Tyler Yahn 00:51:18 Okay, next up. Try security. Socket. Accept.
This is from Steven. If you're still on.
Stephen Lang 00:51:27 Yeah, I'm here, though, Nicole, you might be able to explain this one a bit better. As we were pairing on this.
Tyler Yahn 00:51:32 Oh, sure. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:34 Yeah, I'll explain. So we we need the information about what connection is being.
what's the connection? Pair. So the peer. So example the client and the server connection pair when we accept a request. So we instrument accept for and accept sys, accept and sys except for.
But we instrument, and so we we tap into the K return, probe or accept.
And then we know that there's a new server connection being activated, we grab the file descriptor for various support that.
for example, Nodejs uses file descriptors and things like that. And so we need the socket information.
But since it's a return probe.
it only gives us the file descriptor of either successfully accepted as a server request or something that didn't work.
So the way we provide the socket information to the the except is that we were tapping also into new into the socket. Alloc sock alloc api in the kernel. So we that probe would just save this temporary information in a map to tell us that a new socket was being allocated.
and then, if the same thread did the allocation and accept. We were saying, Okay, these 2 are correlated. So here's the socket for that accepted request.
However, like, Steven has been testing on an arm kernel that he has, and apparently that's not how Arm behaves so he never calls so catalog that kernel that he has.
Tyler Yahn 00:53:25 Oh, interesting!
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:26 Yeah. So this we do have arm tests, and they're passing. But you know, maybe it's a version thing.
Because of that. We started looking at an alternative. And then we found that there's this other Api that all kernels seem to activate is security socket, analog socket, except which has access to a socket pointer.
and it's specific to accept which is kind of nice.
And so I think this log saw canested.
Not sure that's correct. I think we're is that the one we picked.
Stephen Lang 00:54:05 So I think you, said Nicola, that the lock sock nested one was the easier one to to get working.
But it's also executed all the time when we were looking at the kernel trace. It was. It was like 3 times for every one of the security socket, except but the security socket, except, I think, would need some more work.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:27 Yeah, okay, so we need to tap into security socket, except, I think that's the one we put in. I'm surprised. So what's the generic tracer go. Which one does it point to if you click on.
I can't really change that. It just would.
Yeah, oh, yeah, security socket, except we got it working. It's just you need to rename that probe.
Stephen Lang 00:54:47 Oh, my! Bad!
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:49 Yeah, I think we initially went to another. We went to a saw clock nested, but that gets called all the time. So it will be a high overhead while this security socket, except is only called when a socket is actually accepted. So tapping into that gives us the access to the socket pointer.
and then, when the accept returns, we're able to correlate the socket pointer with the file descriptor, and we're good to go.
Stephen Lang 00:55:17 Okay. So I just need to change all the references from the lock sock nested just over to the security socket access.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:24 Yeah, we just need to rename that. And I think this works on all kernels that we've tried with. So.
Tyler Yahn 00:55:32 Okay, yeah. Cool. Thanks for the explanation. That's pretty helpful. Yeah. So it looks like a little bit more work. And still in draft. So working on it. Yeah.
we'll look forward to the the presented version.
Okay.
I think there's only a few more. So fix Httpt, Grbc, Parse bug thought, I just saw this one come in. Yeah, a little while ago. So this is again, something from Nicola. Looks like Raphael's already reviewed this.
Some flaky tests, but.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:04 Fails the Java Dafca test which I need I'm going to look into, but I can explain quickly for everyone's benefit here.
So what we used to do, and maybe in the files change it will become obvious is that for Http 2, which handles grpc. As well.
we were in the previous version, if you look So we had this else statement. So we were 1st looking, maybe side to side is a little bit better, I don't know like.
let's see if we can.
Tyler Yahn 00:56:39 Yeah, they changed the format of Github. Let's see, it's here. No? Yeah. Split.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:46 This plan? Yeah. Yeah.
So if you look what we used to do. If you scroll up a little on the on the left side. Scroll up?
Oh, oh, sorry the other way.
Oh, sorry that so we were detecting an Ss Http connection.
and then everything else was in this L statement. So the way we detect an Htp. 2 connection is by looking at this preamble which starts with this Pre. Pri star, Htp. 2, and it has a bunch of new lines and carriage returns.
or we look for a settings. Frame.
And then, if we identify one of those we say this is likely. Http 2. So then we start parsing it.
But what did happen when I was experimenting with a job? I had Tls and I ran some Http. 2, because I was talking to an Http service that immediately upgraded the connection to Http 2.
What ended up having Java does is that this preamble, then, after the preamble, it attaches the additional packet.
and none of the other ones do this but Java does it so? So we have the preamble, pri star, http. 2, which is all clear text and right after starts the binary.
So our code previously was doing this? Or did I find the preamble, mark the connection as an Htp 2 connection next time around, find the next packet and then start parsing it.
But we can't do that because these guys send the the next packet in the same packet together.
So I had to kind of composite for that. So I removed the else if there.
So if it was marked as Http. 2, I check to see if the if it has the clear text preface, then obviously will fail parsing. So I push the buffer past the preface, and if it's a settings frame that's fine, because that's a normal Http 2 frame that we can parse.
So.
So I skipped back as a preface and let the Http code. Then parse straight up after that packet made the Java test work. I but I don't have another test. Unfortunately.
to prove this, the existing test should still work. Everything should still pass it.
The there's not much changes. So it's just the code. It's it's shifted.
Tyler Yahn 00:59:20 Yeah, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:21 It's just the else is removed. And then and I did a little. That's pretty much the 9 43 is the addition there where I say, if he has a prefix, then push it past the prefix.
and then let the code run the normal H 2 parsing after the fact.
Okay.
Tyler Yahn 00:59:42 Yeah, that's good. I realize we're also.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:46 Once we do. Yeah, oh, we're a time. Yeah.
Tyler Yahn 00:59:49 Yeah, we're at time. So I'm gonna probably stop sharing here. I think that's that's good. Appreciate some eyes on that. Pr, obviously, Raphael, thanks for reviewing that. But yeah, more eyes would be better.
Okay, I want to respect everyone's time. So thanks everyone for joining. We will see you all in a week's time and talk to you. Then bye.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:06 Bye.
Mattia Meleleo 01:00:08 Bye.
