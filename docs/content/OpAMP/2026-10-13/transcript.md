SIG: OpAMP
Date: 2026-10-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan (Splunk Inc.)** 01:39 Hello.
**Andy Keller** 01:40 Hello.
**Israel Blancas** 01:44 Hi.
**Andy Keller** 01:46 And… What's up, Tyler? How are you?
**Tyler Helmuth** 01:49 Hello, I'm good.
**Tigran Najaryan (Splunk Inc.)** 02:45 Okay, I think we can start. Tyler, you have the first.
Topic in the agenda. Wanna go ahead?
**Tyler Helmuth** 02:51 So I've been researching some more about OpAMP and How it works in Kubernetes. And I've come across, I guess a big… difference when you're using OpAMP and Kubernetes versus other platforms, at least as As we have designed it in our own.
OpenTelemetry OpAMP supported clients.
So, what I mean is, when you're using OpAMP on a Linux server, you're using the supervisor if you've got some other client or whatever.
The thing that is running represents one.
Executable on the machine, for example.
But when you use OpAmp and Kubernetes.
if you use the only Opamp client that the community has built, which is the Opamp Bridge.
The individual agent is no longer… A single process that's running.
It's not the container in a pod.
Or the pod itself. It is the entire workload.
And I… based on my own research, I can see why we went that way. Kubernetes is its own platform that has a lot of Expectations for how things are run, and how things are managed, and kept up to date, desired, and current, and the reconciliation cycle, and all that stuff.
Of course, upgrades can't be done at an individual pod level, you have to change The workload, and then get everything redeployed in order to do an update.
But I'm kind of curious what… other people are running into when running OpAMP and Kubernetes, because for me, what the end result is, your OpAMP server has to know two different Client formats, in order to use OpAMP across multiple different platforms.
So, like, if you wanna use OpAMP in Linux, you gotta know that the agent is the individual service. If you wanna use OpAMP in Kubernetes, you either have to do unsupported stuff.
like, build a… a container that contains the OpAMP supervisor and the collector, which is what.
I know a lot of people are doing. Or you've got to use the OpAMP Bridge, which is like a totally different paradigm from using OpAMP other places. So I'm kind of curious what other people are thinking about this, how other people are solving this problem or handling this, like, discrepancy.
**Andy Keller** 05:33 Yeah, I can talk a little bit about what we're doing.
We… we just recently added operator support, and It is really different, and that's why it took so long for us to add it, because the whole user experience around what you're managing You know, you mentioned managing a workload. Just to be clear, you're managing every workload in the cluster, so it could.
**Tyler Helmuth** 05:57 Yeah.
**Andy Keller** 05:58 It could be a daemon set, it could be also a deployment you're using as a gateway, or another deployment you're using for… Cluster metrics, there's… You know, there's that… usually, you know, we see in most clusters, you've got at least 3 different workloads.
Container logs.
You know, and in Cubit Metrics.
In a Damon set, and then… deployment for your gateway, and then another deployment for, usually Stapleset, for the gateway.
And then another deployment for, for events, and… Cluster metrics, so… Yeah, it's… it's… I don't… I don't really know how to, like… put it mildly, it's… it's way different. It's not just the OpenTelemetry config that you're managing either, it's the entire CRD, so…
**Tyler Helmuth** 07:08 Yeah, that.
**Andy Keller** 07:08 You're even specifying things.
**Tyler Helmuth** 07:13 Well, I'll get into that, keep going, keep going. Sure.
Follow up.
**Andy Keller** 07:17 Yeah, But you're… you also are controlling, you know, is this a Damon set or a staple set? Is this… how many replicas do I have? Am I using auto-scaling? What's my… Requests, you know, my resource requests and limits, all of that is… in that payload.
So… Yeah, really different.
I I.
you know, I've been working on this for a while, so I'm pretty deep in it, and I can say that I do think it's… a great model for managing workloads in Kubernetes. I think building a container with a supervisor is a little awkward, because… You might be crash looping, you're… collector, but you don't really know it, because the supervisor's hiding that from you. Yep.
You know, it's just a little bit of a strange… container image to be using, so… Yeah.
And the other thing we've done historically, and, you know, as I mentioned, we're just really adding operator support now, what we've always done is, use our own embedded OpAMP implementation, Which, by the way, I know we talked about this in the past, it's finally, Just about usable by anyone.
I can… I can tell you more about that if you're curious, but But we would build a container with that.
But the things, you know, to your point.
Upgrades are weird, you're upgrading the… Binary in the container.
**Tyler Helmuth** 09:00 Yeah.
That was my solution for that as well. That's obviously not going to last.
**Andy Keller** 09:06 And then… Even configuration changes are strange, because you're… you know, you might have… you might be bootstrapping with a no-op config.
But then you're reliant on your management platform being available instantaneously when that pod gets launched, right? And if it's not, then you've got a problem, so…
**Tyler Helmuth** 09:27 I assume that the… the… building the client directly into the collector also allows you to do stuff where different pods in the workload could end up with different configurations.
That's something that Alloy lets you do, for example, which is, like.
all like Kubernetes wouldn't really want you to do that. It would rather you have the the config map. Yeah.
**Andy Keller** 09:48 Yeah.
**Tyler Helmuth** 09:49 Okay.
**Andy Keller** 09:51 Okay.
**Tyler Helmuth** 09:53 So the answer is, you definitely feel strongly that the answer is.
the Bridge's architecture is the right architecture, and it is the right architecture because Kubernetes is a much different platform than running on a Linux server.
**Andy Keller** 10:07 That's… that's my personal opinion. I will… I will just caveat that You know, Tigran and I have been maintainers of this of the OpAMP.
Effort for a long time, and… Neither of us really had involvement in the development of the bridge. That was largely Jacob, and I think he did a great job, but I don't want it to sound like that architecture came out of this group.
**Tyler Helmuth** 10:35 So but the if we if we wanted to continue to improve OpAMP's story and the OpenTelemetry project support of OpApp and Kubernetes, you would definitely say continue to improve the bridge, like, that… Yes. The idea of managing the workloads, make the workload the client.
Client.
And move that forward.
**Andy Keller** 10:57 Yeah, and there are a lot of… Aspects of the way the bridge and the operator itself.
Work, like, understanding… You know, receivers and what ports they need available, and exposing those ports.
And there's just a lot of capabilities built into the operator that are really powerful, and the bridge gives you access to them over OpAMP.
**Tyler Helmuth** 11:26 the.
**Andy Keller** 11:26 I found it to be, I mean, really great. We were using it in production for all of our… Self-monitoring of all of our clusters. They're all deployed using the OpenTelemetry Operator and the bridge of ROP AMP.
**Tyler Helmuth** 11:42 So.
**Andy Keller** 11:43 At this point. One of the…
**Tigran Najaryan (Splunk Inc.)** 11:44 I guess, maybe to chime in a bit.
**Andy Keller** 11:47 Yeah, of course.
**Tigran Najaryan (Splunk Inc.)** 11:48 Those two models, right? Essentially, one is… sort of what the bridge does today. It's kind of… it relies on the fact that Kubernetes is a managed platform. There's an API that allows you to control it, and it uses that API, the CRD, essentially.
It bridges the OPAMP concepts into the Kubernetes' control plane.
The other model is what Andy was describing is the bootstrap approach. You do absolute minimum to bring up your system on Kubernetes, and then ignore the capabilities of Kubernetes' control plane, and bypass it. Essentially, you have a complete side channel of managing Kubernetes.
It is a viable approach, but in a way, it ignores the fact that probably most people don't manage Kubernetes that way. They would prefer to continue using the native concepts of Kubernetes, which is what the bridge recognizes and tries to use that. In some ways, doing that The second approach with the bootstrapping and site control.
you may… you are fighting, actually, the Kubernetes control play, like, the upgrades and all that stuff that you're describing. It may be successful.
And it may be a viable approach. I don't know if we want to have that as an official OpenTelemetry.
**Tyler Helmuth** 13:12 Thinking too. So, like, we know that today people will build a supervisor collector, put them in the same image and go run that in product like, go run that with a an OpAMP server. We know like, I know people are doing that today.
The community specifically does not release a combo image, because I don't think we want to, like, promote that use case.
**Tigran Najaryan (Splunk Inc.)** 13:33 Yeah. One of the ways that you can make it work is by… heavily restricting what you do through OPMAP, mostly run it in a read-only mode, essentially. Yeah. These allow the upgrades and all the config updates and all that stuff. As long as you're just reading the status, that's fine, right? Nothing, nothing new.
**Tyler Helmuth** 13:53 Sure.
**Tigran Najaryan (Splunk Inc.)** 13:53 with that approach. But when you enter the realm of now I need to do the supervisor executable updates and all that stuff, now we are in conflict with what Kubernetes is trying to do.
You either have to implement it very carefully so that the two things can coexist properly, which may be hard, right?
**Tyler Helmuth** 14:15 Yeah.
**Tigran Najaryan (Splunk Inc.)** 14:15 It's so easy to do. So, I think it was the simpler approach, what Jacob did in the bridge. Like Candy said, we didn't, I guess, participate much, but it seems to me that may be the right approach. We haven't made any special calls on that, to be clear.
**Tyler Helmuth** 14:33 Okay.
One, I guess, last question on this topic.
The end of September, we did a hackathon internally, just trying to explore What it would, like, look like to incorporate this pattern.
and and also use it for some other stuff. But one of the things that I get scared about this pattern Is that you're now… remotely… deploying CRs, not just config, right? So you're not… you're not just specifying what config is the collector gonna run. You're specifying the workload, the resources, the permissions, everything on the Alloy CR you now get to push.
Which is essentially, like, remote deploying, like, remote of doing a Helm apply, or a Helm install, right? Or a K apply, which is… It's incredibly powerful. Like, it solves so many problems to be able to be like, I changed my config. Now I wanna update the port that my service is deploying. Like, there's so many cool things that you can do with it. But from a security perspective, the idea of, like, would I really let someone Push.
**Tigran Najaryan (Splunk Inc.)** 15:41 Yes. Remote. I think that's one of the key questions. Yes. As a, as a person who is responsible for managing a Kubernetes cluster, do I want my observability?
**Tyler Helmuth** 15:51 vendor.
**Tigran Najaryan (Splunk Inc.)** 15:52 to have an ability to manage my cluster.
**Tyler Helmuth** 15:55 do that actually.
**Tigran Najaryan (Splunk Inc.)** 15:56 overstepping the, I guess, the boundaries, what observability is.
**Tyler Helmuth** 16:01 Seems very scary.
**Tigran Najaryan (Splunk Inc.)** 16:02 Yeah, yes.
**Tyler Helmuth** 16:03 There's probably ways to simplify it by throwing some, like, some extra… services in there that, like, they're the ones that talk to Op. But yeah, at the end of the day, it's… it's… it seems like a massive risk, like, I guess Andy is someone who's implemented a server that supports this. Have you, like, run into… Like, does the community really actually want to do this?
**Andy Keller** 16:26 more.
**Kelsey Ma** 16:26 I just wanted to call out, sorry.
**Andy Keller** 16:28 Yeah, no, go ahead.
**Kelsey Ma** 16:29 There is a newly added mode in OpAMP Bridge called standalone mode, which only will operate on the config maps. So it actually has no reliance on CRDs or the operator. And that was, I think, added as sort of a middle ground to avoid some of these security concerns.
**Tyler Helmuth** 16:46 Okay.
**Tigran Najaryan (Splunk Inc.)** 16:49 Anything else, Kelsey, you want to add about what we're doing, maybe internally at Splunk, if you know? I don't know if… Yeah, so that was a.
**Kelsey Ma** 16:57 Yeah, that was added, for our, sort of, remote config, needs at Splunk.
I think that's kind of currently where we're at with the OpAMP Bridge, like, the standalone mode, because we didn't really want to, use the CRDs.
I don't really have much data yet on how it is, like, going out. I think it's, like, just recently released, but yeah, that could be… standalone mode could be something that we, like, augment if you're, like, trying to avoid, like, changing the entire cluster as a whole.
**Andy Keller** 17:36 Yeah, I think there's gonna be different… people are gonna have different opinions about this kind of thing. If, you know.
walk around KubeCon and see how many Kubernetes management platforms there are that are remotely managing your Kubernetes cluster via the API. Like, there's… you're gonna see 20 booths, you know? And we use one of them, and I think a lot of people are using something to.
to manage their deployments to Kubernetes.
So… I don't think… you know, now, when you say… your observability provider, you know, do you trust them to do it? Like, I don't know if that means, you know, anything in particular. Like, it's… If any of these other companies that can manage Kubernetes clusters, can do it, I would think we could do it as well.
I do think it's it's limited to the, collector CRDs, it's, you know, you're not…
**Tyler Helmuth** 18:30 course.
**Andy Keller** 18:31 You're not able to just, you know, deploy services.
**Tyler Helmuth** 18:33 Call, whatever.
**Andy Keller** 18:35 Yeah, at the same time, you can specify the image.
**Tyler Helmuth** 18:41 looks.
**Andy Keller** 18:42 Like a collector.
And you specify an image and give it a collector CRD, it'll… it'll run. So.
There are definitely, you know, concerns there, and that's… Something that, needs to be, like, clear and transparent, and, But at the same time.
There's tons of really useful platforms out there that will… Help you manage your Kubernetes deployments, so…
**Tyler Helmuth** 19:08 Yeah. The image one is is hard to get around, but the idea of of, like, is there do we have any concept in the OpAMP spec of, like, a signed message?
where… Where the client can, like, check that… This message really did come from the server I expected it to come from and not from like someone trying to like.
**Andy Keller** 19:29 Well, it's in the spec as of a couple weeks ago. Cool. Cool. Stanley, you can talk about that a little bit if you want, but,
**Stanley Liu** 19:35 Yeah, I can… I can link the proposal if you're interested, but…
**Tyler Helmuth** 19:39 Yeah, definitely.
**Stanley Liu** 19:40 The merging of that spec, so…
**Tyler Helmuth** 19:43 Thank you. That's really cool.
**Andy Keller** 19:46 Yeah, I don't know if… Stanley, do you have any intention on… Implementing that in the bridge.
**Stanley Liu** 19:52 Yes, definitely want to implement it in the bridge. After the GO implementation, or the OpAMP GO PR, we're gonna work on the supervisor bridge and extension.
**Tyler Helmuth** 20:03 Awesome.
**Andy Keller** 20:04 Okay.
**Tigran Najaryan (Splunk Inc.)** 20:08 On that, by the way, Stanley, I did a review of the attestation in Go last week, so… I think it's waiting for your responses there.
**Stanley Liu** 20:16 Yes. Yeah. I saw that. Thanks so much. We'll take a look today.
**Tigran Najaryan (Splunk Inc.)** 20:21 Cool.
Tyler, did you have a chance to talk to Dmitri? He may have some thoughts on this as well.
**Tyler Helmuth** 20:29 I haven't talked to Dimitri. I did see… And I have researched the standalone mode a little bit. I saw that Dimitri was one of the contributors to that as well. I noticed, I think he opened the issue, which is why I recognized it.
**Tigran Najaryan (Splunk Inc.)** 20:42 Yeah, maybe one.
**Tyler Helmuth** 20:43 Right, the…
**Tigran Najaryan (Splunk Inc.)** 20:44 Yeah.
**Tyler Helmuth** 20:45 The standalone mode is really cool. It does still have the agent as the workload, which is reasonable because it's still the bridge.
doing stuff. And so, whether you're using the standalone mode or the… the full CRD support, we are essentially asking OpAMP server implementations to think of… or to… to reply with different types of… remote message formats, which is fine. Servers are capable of doing multiple things. So I think that's okay.
**Tigran Najaryan (Splunk Inc.)** 21:21 Yeah.
**Andy Keller** 21:22 Yeah.
**Tigran Najaryan (Splunk Inc.)** 21:22 There's an expectation that the server understands the type of the.
**Tyler Helmuth** 21:27 yeah.
**Tigran Najaryan (Splunk Inc.)** 21:27 Client connecting and tailors its behavior.
**Tyler Helmuth** 21:31 Totally.
**Tigran Najaryan (Splunk Inc.)** 21:32 The type of the client, yeah.
**Andy Keller** 21:34 Yeah, and that's gonna be the… I mean, it's always been the intent of OpAMP to be… neutral on the collector and its configuration, so, you know, we're still… still hoping for support for FluentBit or some other collector, but… At the moment, it's… it's all OTEL.
I think I did see a project out there.
Can't remember the company, but working on a supervisor that can manage lots of different things.
Using OpAMP, so… it's cool.
The good news is the semant… well, the content… yeah, I'll just say one last thing. The content of the config map.
You know, it's very different for… the bridge, but the, you know, semantics of OpAMP in general are entirely consistent, so it's, you know.
**Tyler Helmuth** 22:36 Yeah.
**Andy Keller** 22:37 You know, just in terms of… The row config, and the hash, and understanding…
**Tyler Helmuth** 22:43 All that's the same.
**Andy Keller** 22:44 Yeah.
**Tyler Helmuth** 22:45 The status report, I think, is instead of the individual aging, it's like a summary of multiple agents, which can still be aggregated and such.
**Andy Keller** 22:55 Jim.
**Tigran Najaryan (Splunk Inc.)** 23:11 Okay.
Talk to Dmitry, he may have also something interesting for you.
this topic.
Shall we move on?
Unless there's other comments?
I'm good.
Okay, this one from Israel, he is not.
In the call anymore?
No way to correlate supervisor and collector telemetry.
Just click the loads belong to that.
So I looked at the issue, I think, and was proposing to… Record the supervisor identifier as a collector dimension in the matrix.
Which is one possibility.
Another possibility would be when we have the entity relationships to record the supervisor entity and the collector entity as being in a relationship.
We don't have that.
Ability, unfortunately, yet, but it's something that we could maybe consider.
comment on this PR.
as an… as a possible option. But if we need it now, that's not going to work. That's something for the future.
I don't know if anybody else said any other.
other… comments, douglas is not here either.
Okay.
I'll comment on it.
Let's move on, Evan.
**Evan Bradley** 24:48 Yep, so Dakota has this PR out that adds, cosign as a package verifier. I wanted a second review, maybe from you, Tigran, but, if anybody else would like to take a look, that would be welcome as well. Just since it's security-related, I'd like… Just somebody to have another pass at it.
It's fairly straightforward, and it's not wired up right now, but I figure, review it while there's a clean diff to look at.
**Tigran Najaryan (Splunk Inc.)** 25:18 Okay, yeah, I'll try to.
I find that this cosine stuff is… Almost never straightforward, but I'll try to.
Yeah.
Okay.
Appreciate it.
Yeah, of course.
We have also another round of security reviews that we need to do on the office station.
Pr, as well. That's also sort of pending for me, at least.
Okay.
That's all in the agenda.
Anything else?
**Andy Keller** 26:04 Just curious, it's a month away, but who's going to Cape Town?
No Tigran.
**Tigran Najaryan (Splunk Inc.)** 26:18 Yeah.
I'm not, no.
**Andy Keller** 26:24 I'll see the rest of you there.
**Tigran Najaryan (Splunk Inc.)** 26:28 Alright.
Thank you all.
**Andy Keller** 26:30 Great, bye.
**Tigran Najaryan (Splunk Inc.)** 26:32 I…
