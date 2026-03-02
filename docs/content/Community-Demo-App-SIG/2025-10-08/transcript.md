SIG: Community Demo App SIG
Date: 2025-10-08
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/cTMKVTUQZ8N9FKOTWtT2CcVRrjNQDooM3xJZYMjiehylg8CmjOSnmhXicEErO5gm.9rI2s-2daz43yPjz
============================================================

## Zoom Recording Transcript

**Cyrille Le Clerc** 00:49 Hello?
**Alessio** 00:51 Hey.
Who are you?
**Cyrille Le Clerc** 00:54 Fine on you.
**Alessio** 00:56 I'm very well.
**Cyrille Le Clerc** 01:00 We'll create an entry on the dock.
**Pierre Tessier** 01:03 Hello.
**Cyrille Le Clerc** 01:05 Hello, Pierre.
**Alessio** 01:08 Now that you remind me, I had a pending PR on the Open Telemetry website, actually.
That I should check.
If… was merged, I think so.
Yeah, I was merged.
**Pierre Tessier** 03:26 Hi.
I think we could probably get started.
Yeah, I think so. We don't have cooleanor, right?
Yeah, I'm gonna clean up this stock a little bit here. There we go.
It's been several weeks, months, maybe even, since I've joined one of these.
Been very busy at work.
But, I know we just got a release out.
I've been communicating back and forth with Juliano, who did just let us know that he can't attend today.
Okay. We have… Several pull requests out there?
Not many.
I kind of appreciate that the Hotel Dumma doesn't really have much left going on with it.
Yeah.
I know, Cereal, you want to talk a lot about getting an operator instrumented version of this demo.
Going, right?
**Cyrille Le Clerc** 04:43 That's one topic that we discussed last time, and we had some action items, and we have updates on this. That's one topic, but, there could be others.
**Pierre Tessier** 04:53 Okay.
So…
**Alessio** 05:01 I think that my… I don't know if there's other topics.
**Pierre Tessier** 05:06 And I know last meeting, a lot of it was getting a demo out and released, and that is done now through Kubernetes and everything else.
So, I see here, you know.
Probably look at that, Helm chart pull request.
**Cyrille Le Clerc** 05:34 Yeah, it's a bit, no, it's not that messy, but,
It's almost done, I think.
**Alessio** 05:43 I can.
**Cyrille Le Clerc** 05:46 where, when I say it's a bit messy, that, sometime I have identified some,
Things that look to me like feature gaps, like the pull request I highlight below.
And so I tested the kind of workaround in the demo hand chart.
Before submitting a PR to the cube stack, in charts.
To… before somatic fix in the hotel component, that was,
used in the demo. But otherwise, the M chart looks… the PR that you are looking at is, quite,
Close to, what it could be.
With a… A big limitation to discuss.
**Pierre Tessier** 06:32 Yeah, so I think the idea here is that we're just going to inject all the environment variables automagically, instead of it being specified within the health chart itself, is we're going to use the hotel operator to inject them.
**Cyrille Le Clerc** 06:44 I… that's one dimension, yes. That's for the instrumentation… leveraging the instrumentation CRD, correct?
And also, very interesting lesson learned for me.
is that… that we can share with the instrumentation CRD people is, instrumentation CRD, is designed to just support one OTLP endpoint, so you choose gRPC or HTTP.
And we see in the hotel demo, for example, that some services require HTTP, some other services require gRPC,
out-of-the-box instrumentation CRD.
doesn't work for this use case, which is still simple because it's just a demo, and I felt it was extremely interesting to touch this limitation.
And to be able to… to discuss this with the…
**Pierre Tessier** 07:40 We should be moving to HTTP protocol for everything. I think I've gone on the record to say gRPC was a mistake, and we should never have done it.
I understand why it exists.
But…
it causes a lot of other hard-to-debug issues. The mix is probably because as we… you know, we just need to catch up with the SDKs.
Some SDKs did not support HTTP protobuf, so we had to wait for them, and that's where the mix is. But I have to think now all SDKs have proper support for HTTP protobuf.
And we should make sure that we leverage that At the demo level.
So that, in your operator, you just specify that, and that's it.
That would be my…
**Cyrille Le Clerc** 08:30 direction, I do agree with you, but if us hotel community members, we struggle to align everything on HTTP,
on, top of my mind is the NGINX…
hotel integration, I don't know if it's capable of
What about community members? It will be so hard, and maybe we… it deserves a conversation with the instrumentation CRD people to…
maybe…
**Pierre Tessier** 08:57 Yeah.
**Cyrille Le Clerc** 08:58 to inject either or based on some, I don't.
**Pierre Tessier** 09:00 Let's do this. Maybe what we end up doing is, because we do have a couple components, I think NGINX and Envoy are both used in this.
**Cyrille Le Clerc** 09:11 Yeah.
**Pierre Tessier** 09:12 Everything else, though, is instrumented through an SDK or an agent, a language.
an open television machine, and those should all support HTTP protobuf.
Let's get those done with this.
Properly.
**Cyrille Le Clerc** 09:29 And maybe we make a second or an exception for those two other components where they still need the environment variables?
**Pierre Tessier** 09:36 And we… and we could just override them inline?
**Cyrille Le Clerc** 09:42 Yeah, we do kind of, like…
**Pierre Tessier** 09:43 And then we add comments to specify, like, hey, we did this because this is where the state is of these things.
**Cyrille Le Clerc** 09:50 And I think it will be very interesting for community members to see how we…
how we implement it, because.
**Pierre Tessier** 09:56 Yes.
**Cyrille Le Clerc** 09:57 I'm sure it's a common use case.
**Pierre Tessier** 09:59 And I'm okay with us…
you know, like, look, we should try to implement things as much as we can towards best practices, but if there's something that we cannot use it because of a reason, as long as the documentation is there to explain why, you know, documentation in code as well as on the community website.
To explain why, I think, like you just said, it would help people understand, like, hey, the world's not perfect, there are exceptions, and here's how we handle them.
**Cyrille Le Clerc** 10:26 Yep.
**Pierre Tessier** 10:28 So… If… you said you identified a couple services yourself that were not… HTTP yet, or is that…
**Cyrille Le Clerc** 10:38 As we can see in the pull request, you will see in the pull request. In fact, what I do in the pull request is that the instrumentation CRD
not only publish OTLP endpoint, but also some environment variable, like HTTP port, gRPC port, and sometimes Docker images consume,
**Pierre Tessier** 10:58 Which is she?
**Cyrille Le Clerc** 10:59 Sean Bar.
**Pierre Tessier** 11:00 Is that your home pull request you did that on?
**Cyrille Le Clerc** 11:02 Yes, it's on, except if I took the wrong link.
I can share my screen if you want.
**Pierre Tessier** 11:08 I'm staring at, it's 1884.
**Cyrille Le Clerc** 11:11 Yeah.
**Pierre Tessier** 11:12 Okay.
I will have to go through this and look at it deeper.
**Cyrille Le Clerc** 11:21 Yeah.
**Pierre Tessier** 11:24 Yeah, it's hard to read these darn pull requests sometimes, because of the number of files that change in them.
**Cyrille Le Clerc** 11:30 Another experience that I love doing this is,
How do you hook all the resource detectors?
In what order do you do them?
To properly enrich your metadata.
you have the environment variables that we have plugged, now we are introducing also Kubernetes node metadata. And if you want to come with your AWS or GCP or DigitalOcean resource detector, in which order do you put the things?
**Pierre Tessier** 12:01 I don't know.
I think, we should include them.
**Cyrille Le Clerc** 12:08 Are there resources at all in this?
No, today we just have environmental resource detector.
Enui, y'all.
It's… It's based on the…
**Pierre Tessier** 12:19 Yeah, and I think we try to stay cloud agnostic.
On purpose here?
So we don't support one cloud or another.
Or we don't showcase support for one cloud or another, because, you know, Reasons.
**Cyrille Le Clerc** 12:35 Yep.
**Alessio** 12:36 Understandably.
**Pierre Tessier** 12:37 could we… you know, could we just… I'm sorry, what was that?
**Alessio** 12:41 Understandably. Like, because reasons, but yeah, understandably.
**Pierre Tessier** 12:46 Yeah, like, we want everybody to support OpenTelemetry.
I think including a comment that says, hey.
If you're deploying it here. I know, like, AWS, you have to do the EC2 and the EKS resource detectors, if I'm not mistaken, or you have to include two of them.
Or something like that. But on, in GCP, it's different, so…
I would almost rather we just write documents on how to do it.
**Cyrille Le Clerc** 13:13 maybe on.
**Pierre Tessier** 13:13 Right.
**Cyrille Le Clerc** 13:14 I suspect that we can do something in the presets.
Where you would have a free text preset to give the name of your cloud provider, so that the order of the processor, some detector, would be the…
what's… What we recommend, because there is an order to respect, to… on a… Enriched properly.
That's an idea, at least documentation, to tell people where to… in which order do you do the stuff.
**Pierre Tessier** 13:42 Yeah. Yeah.
I would think that that would be… that would work.
**Roger Coll** 13:48 Yeah, but also.
**Pierre Tessier** 13:50 I just… I would hate for us to include them, because then you'd have to include them all.
Yeah. And then the order of how you include them can foretell some… or miscommunicate some… some favor… some favoritism, and I would not want us to do that.
**Roger Coll** 14:05 Right.
**Pierre Tessier** 14:05 I would rather us just document, like, here, here they are in alphabetical order, so… Aws, Azure, GCP.
**Cyrille Le Clerc** 14:14 Alibaba Cloud, or .
**Pierre Tessier** 14:16 Yeah, see, that's my other problem. Now you have all the other… and that's right, and then somebody else adds one, and… yeah.
**Cyrille Le Clerc** 14:24 But we have to explain people where to hook them versus the environment variables.
**Pierre Tessier** 14:28 Yeah.
**Cyrille Le Clerc** 14:29 use, you see… System, detector, or whatever.
**Pierre Tessier** 14:35 Yeah.
**Roger Coll** 14:38 But that would be more on the CubeStack health chart side, not on the hotel demo. And that's, I think, one of the good reasons why we are switching from the hotel collector to the…
to the CubeStack, because it's more, let's say, Kubernetes opinionated, and we can document those things. We are able to use the… not only the resource detector, but I think the order is also important when using the Kubernetes attributes processor, right, to decorate,
From pots, container, resource attributes, so…
Yeah, there's some work to do there, and I really like the…
the pull request that you did, to basically add the host name based on the Kubernetes node on the kube stack. I'm not sure if it's going to emerge, because,
Yeah, that's… let's say there's not an agreement in the semantic conventions,
field, either if the host name should match the Kubernetes nom name itself, because some vendors do it, some others use another, let's say, reference.
But, so my… in my opinion, it's, let's say, the most common use case, and…
**Cyrille Le Clerc** 15:56 To give context to the other attendees of the call, today, if you use a KubeStack to enable host metrics.
The kube stack does not collect neither the host name or the Kubernetes node name.
So on your metric, like CPU, you just know the cluster name.
But you don't know which node of this cluster has collected this data based on its host name or its Kubernetes node name, and so it's not usable.
And so we need to enrich with at least Kubernetes node name, on, in my opinion, also host name, because if you enreach with host names, then you can share the same dashboard, the same alerts with VM-based, visualization of host metrics.
Or alert software. And so it was really interesting for me to…
Use the hotel demo to connect all the dots together.
**Roger Coll** 16:50 Yeah, I…
I agree on that side, and actually, it's what we use on the elastic values configuration. We map the Kubernetes node name to hostname, as you are doing on that, but…
Copen.
**Cyrille Le Clerc** 17:05 all the vendors who do both Kubernetes monitoring on APM will have the same question for people who use the HotelCube stack.
Which is, my opinion, is… should become the de facto standard, but…
**Roger Coll** 17:19 I agree. And… Maybe if we can go back to this, well, of the using of the inject…
**Pierre Tessier** 17:26 I noticed this only installs a daemon set in your PR.
Should we install a gateway?
**Cyrille Le Clerc** 17:33 So, the reason for this, I discussed with, Juliano, is resource constraints. So, yeah, my stuff is a bit broken.
there is something very smart in the hotel collector demand set deployment with the leader election.
So is that…
**Pierre Tessier** 17:53 done?
**Cyrille Le Clerc** 17:54 Yes, and it's productized in the CubeStack, so that for Kubernetes, Cluster metrics, cluster events.
You don't need a gateway.
Because you have the leader election.
Out of the box.
**Pierre Tessier** 18:09 When did that get released?
**Roger Coll** 18:11 One month ago, or a couple, max.
**Pierre Tessier** 18:15 I feel like that's very recent.
were working on it, but I did not know it was ready already.
**Roger Coll** 18:21 Yeah, yeah, it's already changed in the CubeStack Hamchart itself, because prior to that, it was deploying a collector called cluster.
**Pierre Tessier** 18:32 Yeah… Today, I learned, this is fantastic, because that, to me, was also… A weird thing about… the…
The Kubernetes.
deployment mechanism for OpenTelemetry, is that I needed a gateway and daemon sets But…
**Cyrille Le Clerc** 18:55 We are not done, because now, great thing, we have added the PostgreSQL instance, we have the Valky instance, on when you want to monitor them.
You also need a single aton to collect this.
**Pierre Tessier** 19:07 metrics.
**Cyrille Le Clerc** 19:09 on… To have a singlet on here, we have two solutions. Either we introduce a gateway mode.
or we reuse the hotel collector receiver creator framework donated by Elastic. I'm sure Roger is familiar with this.
So that it will be the demand set based on config as code with pod annotations that we'll discover. This pod is a PostgreSQL, and I have all the annotation, all the instructions to monitor it through,
annotations.
So maybe we can continue to, not need a collector gateway.
if we use the receiver-creator framework to monitor infrastructure components like Bostgrey, Redis, and so on.
Otherwise, we.
**Pierre Tessier** 20:02 Yeah.
**Cyrille Le Clerc** 20:03 Producer Gateway.
And it will be great educational content for our practitioners, and for us.
I want to see the password to monitor your database as a,
per the annotation, because I think it's what we…
**Pierre Tessier** 20:19 That's…
Well, couldn't a pawn annotation say, hey, there's a secret that contains some details about this? Or the config, when you load up the config, it would…
**Cyrille Le Clerc** 20:29 I asked Roger some help, because Elastic Engineers who have donated the code knows more, but I couldn't find details in the blog post that announced it. For me, they didn't cover secrets.
**Roger Coll** 20:42 Yeah, I can ping maybe Christus on that, but it should be pretty straightforward, it's just about…
Setting up the receiver creator with this discovery feature.
And then, on the, let's say, on the Postgres service, and the reddish one, just put an annotation of,
Yeah, with the, let's say, with the scraping URL that the metrics come from.
And that should be it, theoretically. But yeah, I can…
**Cyrille Le Clerc** 21:14 The blog post was about ready so that there is no password, but as Pierre said, something like Postgres.
**Pierre Tessier** 21:21 Yeah.
**Cyrille Le Clerc** 21:22 should connect with a password on… I wish we have a secret tunneling mechanism. Let's see, at least it's a great opportunity to,
distance.
**Roger Coll** 21:31 Making notes.
**Cyrille Le Clerc** 21:31 realistic scenario.
**Roger Coll** 21:33 Yeah.
**Pierre Tessier** 21:34 Yeah, it'd be great if the pot annotation could refer to a secret.
**Cyrille Le Clerc** 21:38 Yep.
**Pierre Tessier** 21:39 Right? And then the receiver creator would just know how to read it.
**Roger Coll** 21:42 Are we using secrets at the moment, or environment variables?
**Cyrille Le Clerc** 21:47 We should use secre.
**Pierre Tessier** 21:48 We should be… it should be a secret.
for a password.
It should be a Kubernetes secret, so that anybody who has a secrets implementation, like Vault or whatever.
Would be able to leverage that.
**Roger Coll** 22:01 Is this Receiver Creator part of, Hotel Upstream, or just the last one?
**Cyrille Le Clerc** 22:06 No way to control them.
**Roger Coll** 22:12 But… so let's say that at the moment, it's…
the, let's say, the receiver, sorry, the NGINX receiver in the hotel demo to connect it uses an environment variable, right?
With the user and password.
**Pierre Tessier** 22:28 Today, it does.
That is… Not ideal.
I, I'm, I'm, you know, for the demo, it's probably fine.
But for a production workload, and if you're trying to showcase to somebody else how to do this as a production workload, which is the demo, it's a demonstration of how to use OpenTelemetry, we should not recommend people to put a password in an environment variable.
We really shouldn't.
**Roger Coll** 23:02 Yeah, but at the same time, I don't know if there's any mechanism to put, to reference, Kubernetes secrets in a collector, configuration.
**Pierre Tessier** 23:11 Yeah, that's where it gets really hairy.
**Cyrille Le Clerc** 23:14 This is one, I think, but I don't know if in the CubeStack end chart it works.
**Pierre Tessier** 23:22 This is the…
**Cyrille Le Clerc** 23:23 Thank you, sir.
**Pierre Tessier** 23:23 Problem to solve. For what it's worth. I would love for somebody to solve, to make it so, via pod annotations or an operator.
CRD, you know, through an instrumentation CRD, some kind, if I could say, hey, go find… like, I love the world of an OpenTelemetry collector where you don't need anything but the daemon sets.
And it'll know how to collect everything. And all the data sets have the same configuration, so that if they read any pod and annotation for any of the pods on their node.
They know how to collect data from it.
Be it Postgres or whatever.
And that would likely require this thing to do Kubernetes API calls, so you probably have to give it, permissions.
for it to make calls to its own internal API.
To figure it out.
And then that way there could read secrets, or it could read whatever it needs. So, I think it's a larger problem for the open technology community to solve for.
And I don't know if we're gonna be able to solve it ourselves in the SIG.
**Cyrille Le Clerc** 24:28 But at least we can showcase it.
I'm doing a PR showing. Here I have a problem, I don't know.
**Pierre Tessier** 24:34 Yeah, I think we could showcase it as pod annotations. Passwords and pod annotations… sounds disgusting.
And maybe we should put a comment in there about that?
**Cyrille Le Clerc** 24:44 Excuse me.
**Pierre Tessier** 24:44 But I think at least it showcases that, hey, there's something here, and it's… there's possibilities here.
That can be leveraged.
**Roger Coll** 24:59 I…
In my opinion, if we can start by just using the discovery mechanism, and not providing, let's say, the raw user and password in the annotation, but just referenced environment variable, as we are doing at the moment, it would be, let's say, the equivalent.
And we can, from there, showcase that it would be much better to reference a secret, right? And… because…
**Pierre Tessier** 25:26 Wait a sec, can you say that again? So, how do you reference the environment variable in this case?
**Roger Coll** 25:31 The same way as we do at the moment in the collector config, so you just…
Let's say the environment variable, normally, it's populated by a secret in the pod definition.
And then.
**Pierre Tessier** 25:44 Yeah.
**Roger Coll** 25:44 collector config uses a reference that,
That environment variable, and the collector will read it.
**Pierre Tessier** 25:51 But… but if it's doing discovery, how does… like…
**Roger Coll** 25:55 Yes, so there's… let's say that there's this issue that… the…
Environment variable must be preset, let's say, Audi… Helm definition.
**Pierre Tessier** 26:10 So it needs to be present on the.
**Roger Coll** 26:11 Yeah, exactly. Yeah, yeah, yeah.
**Pierre Tessier** 26:14 Okay, so we would put the password…
As an environment variable on the collector.
And then…
the pod annotation on the Postgres pod would say, hey, go reference that environment variable, and you'll have your password.
**Roger Coll** 26:28 Yeah, that's it.
**Pierre Tessier** 26:30 I think that's okay.
It's not perfect, but it's okay, and we should definitely do that.
**Roger Coll** 26:37 It allows us to stay on Damon sets for everything.
Yeah, I agree, and I think it's a good point, what we just mentioned about the secret, and I will share it.
with Christine.
**Pierre Tessier** 26:48 Yeah.
**Roger Coll** 26:49 actually made this… this discovery thing, let's see what, what, what here…
**Pierre Tessier** 26:54 Yeah, because the only problem with that discovery thing is that it requires us to…
Redeploy the collector with a new environment variable, effectively, right?
in a true production world, you would only deploy the collect… you know, once you deploy your configuration, you're done, and then you can spin up new Postgres pods.
Using passwords on them, and it would discover.
Today, to do that, I would have to tell the collector about a new username and password each time.
**Roger Coll** 27:21 Yeah, that's totally right.
**Pierre Tessier** 27:26 Which, okay.
We should do that. Sadil, I think we should have a task on the OTEL demo to convert every
SDK, service to HTTP Protobuff. We should do that.
So that this makes your Helm PR much cleaner as well.
**Cyrille Le Clerc** 27:44 Yeah.
**Roger Coll** 27:46 But my question on that is that why do we want to use the operator for the service that we already have on Auto SDK? Because
I, my understanding is that not only injects the environment variables of the collector endpoint, etc, but also injects the, let's say, the jars, for example, for Java, and for Node, the
node SDK agent into the, let's say, into the runtime. And I don't know how it will behave if they are already implemented.
**Pierre Tessier** 28:18 We're just gonna inject the environment variables. We're not gonna inject any SDKs or agents.
**Cyrille Le Clerc** 28:23 It's… it's… you have different… you have two levels of ingestion of… injection of instrumentation. You can inject only the configuration.
Or you can inject configuration on binaries.
On here today, it's just injection of configuration.
And I don't know if you have supported customers with problems on resource attributes that are not right on Kubernetes, like service instance ID that is misaligned everywhere, and I think it's already a great benefit to use just the ingestion of configuration.
**Roger Coll** 28:59 Okay, so with the label… I didn't know that, so with the label that we… the notation that we are adding, that it's inject SDK, it will only inject the environment variables.
**Cyrille Le Clerc** 29:09 Let me, share my screen, maybe…
**Pierre Tessier** 29:12 I do need to have to run for this, Sadil. Let's make it a task that we need to update the SDKs on everything on the hotel demo side to support this, and I'll let you demo this off to Roger.
**Roger Coll** 29:24 Okay.
**Cyrille Le Clerc** 29:25 You want me to demo today, or later, Roger?
**Pierre Tessier** 29:28 I need to run, if you all can stick around.
**Cyrille Le Clerc** 29:30 That's fantastic, I just need to go. Sorry.
I can demo now, Roger, if you want.
**Roger Coll** 29:36 Yeah, half a minute, that's, like, oh, that's…
**Cyrille Le Clerc** 29:41 Okay, so, territorial… Opentelemetry Demo…
Right, I have to change my branch.
And I know only how to do it with sorcery, not with…
So, it's in values.yaml.
Nope.
Value.
resources…
Front 10.
ED3D upgrade.
Yeah, here you can see…
I have a notation, which is… inject SDK.
**Roger Coll** 30:47 Yep.
**Cyrille Le Clerc** 30:48 Until what will happen when…
the Kubernetes operator, the hotel operator, will work.
It will not inject Dockery image with instrumentation, it will just inject All these environment variables.
**Roger Coll** 31:16 Okay, so it doesn't inject the… the site kind of container, but does the address? Okay.
**Cyrille Le Clerc** 31:23 if I used inject Java, inject .NET, inject whatever language.
**Roger Coll** 31:28 Oh, good.
**Cyrille Le Clerc** 31:28 It would have injected also a sidecar container, but here it's just injecting
The resource attribute… the environment variables.
**Roger Coll** 31:38 Okay, that… okay, that's fine. I… I… I… then I… I misunderstood the…
the injection and notation. I thought that it was injecting always the container, not only the environment memorial. Then that's… that's great, I think. I…
It's a great…
**Cyrille Le Clerc** 31:55 first step, I think, for people to embrace hotel operator, it's a great first step.
**Roger Coll** 31:59 And then you have an instrumentation CRD.
**Cyrille Le Clerc** 32:03 Whoa.
I didn't put the link, but where you define
you can define Docker images, sidecar Docker images for each language you want. You define variables that are shared across
all the instrumentation, whatever it's inject SDK, Java.net, and then you have also blocks per language, where you can inject language-specific config.
Untypically here, as we said earlier today,
So we have the temporality preference, because some of us, some vendors want to switch to Delta.
Some of the instrumentation also use a port.
on a specific port, so I ingest the host name.
propagators, yeah, all the stuff. Maybe you're already familiar with the instrumentation CRD.
**Roger Coll** 33:02 Yeah, no, looks great. I definitely support the idea. It will simplify a lot, yeah, the configuration.
**Cyrille Le Clerc** 33:10 Knows everything.
**Roger Coll** 33:11 It's great, yeah.
**Cyrille Le Clerc** 33:12 Something that is ugly in what I do.
Is that this… Helm chart will simultaneously
install OpenTelemetry Operator, OpenTelemetry CRDs, on the services, the hotel demo services.
with Realm Short, you cannot… Put a sequence in which you install the deployments.
Like, the hotel operator deployment.
On the accounting deployment.
So what happens is…
The head charts launch all the deployments at once.
On these deployments, at the beginning, they don't…
They are not… They don't go through the…
instantiation hook of OpenTelemetry… of Kubernetes, so they don't get unreached by the OpenTelemetry operator.
Because the OpenTeametry operator has not yet registered to listen to all these events, to all these Kubernetes pod events.
**Roger Coll** 34:35 Huh.
**Cyrille Le Clerc** 34:35 So, what I do is… I create a job in the hand chart, that…
waits for open telemetry operator to be ready.
inventory operator ready, instrumentation CRD ready, created, visible as well, and then I restart all the hotel services.
**Roger Coll** 35:00 I see.
**Cyrille Le Clerc** 35:00 So it's a bit ugly. It's because we want to package in the same Helm chart.
**Roger Coll** 35:05 through snapshot, but the.
**Cyrille Le Clerc** 35:06 minutes long.
Hotel instrumentation on applications to be instrumented.
**Roger Coll** 35:11 Okay.
**Cyrille Le Clerc** 35:14 On DigitalOcean, it works well on my laptop, which has limited resources.
a bit, slow.
**Roger Coll** 35:22 Yeah, because the other… the only other alternative is to, in the instruction, just… First install the…
let's say a prerequisite step of installing the operator, and then the services, right?
**Cyrille Le Clerc** 35:38 Two hand charts, one after the other, yes.
**Roger Coll** 35:40 Yeah.
I see.
Okay, I will take a look at this ready task, and…
And also test it on my end, and I will try to share some feedback also.
Because, yeah, it's not ideal, the service restart, but yeah, you can think of something.
**Cyrille Le Clerc** 36:01 Yeah, maybe there are some… I just learned hand charts, working on this, so maybe some hand charts specialists will learn.
**Roger Coll** 36:08 Yeah, exactly. Yeah, yeah, maybe you can get some help from the… from the upstream maintainers, there.
**Cyrille Le Clerc** 36:15 Yeah, or people just knowledgeable on hand charts, too.
Create the right sequence of tasks.
**Roger Coll** 36:21 Definitely.
Sounds good, thanks a lot for sharing that. I will… yeah, Dave might comment on the… in…
inject SDK, because I misunderstood that, and yeah, continue my review there.
**Cyrille Le Clerc** 36:36 Longer term, I think I do agree with you. I think the OpenTelemetry demo should show how to inject also the Java SDK.NET SDKs through sidecarl containers, but I guess as a second milestone.
**Roger Coll** 36:48 Yeah, yeah, definitely, definitely, because we will need to create another service or something like that, that it's disabled on the Docker deployment, or…
**Cyrille Le Clerc** 36:58 two container images, one.
**Roger Coll** 37:00 we see it.
**Cyrille Le Clerc** 37:01 Yes, user without, or…
**Roger Coll** 37:03 Yeah, and actually, that would be very valuable also for, I guess, vendors. Normally, they want to compare their classic APMs with the hotel one, but using the same service, and
At the moment, there's no easy way to decouple the SDKs from the…
From the hotel demo service, so that would be a nice idea.
**Cyrille Le Clerc** 37:25 Yeah.
**Roger Coll** 37:27 Okay, I need to run as well.
Thanks for sharing, I don't know if anyone has…
**Alessio** 37:34 Nice.
Oh, actually.
**Cyrille Le Clerc** 37:36 if you could test on, your company, it's K3D, correct?
**Alessio** 37:41 My company is Suze, we make also, yeah, we make friends.
**Cyrille Le Clerc** 37:46 Yeah, you're, which one do you do? But you do… if you can test on your own…
Kubernetes, implementations?
CCPR.
To ensure that…
**Alessio** 37:59 Sure, yeah.
**Cyrille Le Clerc** 37:59 Yeah, so if you're on… it's Rancher Desktop… sorry, I forgot the name, but you told me.
**Alessio** 38:04 Renture, Rancher, Rancher. Like, we also make Rancher Desktop, but yeah.
**Cyrille Le Clerc** 38:10 If you could test on your,
distribution, so we are sure that it works.
**Alessio** 38:16 Sure. Well, for you, that would be great.
**Cyrille Le Clerc** 38:18 Because I could only test Docker Desktop on DigitalOcean.
**Alessio** 38:23 Oh, cool, okay, okay. Yeah, I'll test maybe on, on K3S and Rancher and let you know.
Okay, that would be great.
**Cyrille Le Clerc** 38:34 Thank you very much.
**Alessio** 38:36 Back to you.
**Shenoy Pratik Gurudatt** 38:37 Okay, bye.
out of the lights.
