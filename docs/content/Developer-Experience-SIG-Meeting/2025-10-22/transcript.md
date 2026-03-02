SIG: Developer Experience SIG Meeting
Date: 2025-10-22
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Turan 00:01:25 Hello?
Tristan Sloughter 00:01:31 Right.
Damien Mathieu 00:01:31 Good morning.
Turan 00:01:33 Good morning. Hello?
Tristan Sloughter 00:01:35 Boop.
Where's my camera?
One second.
Alright One sec, let me pull up…
Alright.
Rearrange some stuff. I can't do it.
Thank you for joining us.
Turan 00:02:11 Yeah, no problem anything we can do to help out the open source community?
Tristan Sloughter 00:02:19 Awesome.
Hmm.
So yeah, we can dive right into this, the interview.
You looked over the questions I sent over?
Turan 00:02:30 Yeah, just one thing I might be lacking is a diagram, but the setup is simple enough that I think I can convey it in words that
You might be able to understand what the layout is like here.
Tristan Sloughter 00:02:45 And do you mind if…
you… so you give, like, the details of what it looks like. If I were to…
create a config out of that and put it into OTelBin and graph it, like…
Turan 00:02:59 Yeah, that's no problem. I've got the hotel bin URL, we can just send you that to visualize it on your end. There might be some, you know, internal cluster URLs, but, you know, that's not sensitive to us.
Tristan Sloughter 00:03:12 No, okay.
Pull up my notes.
Turan 00:03:17 And, I'm just joined by my colleague as well, Bjorn, who has been helping me out with, observability in DC here.
And, well, they open telemetry and got all that stuff here.
Tristan Sloughter 00:03:30 Okay. Well, we can… Jump right into it.
So the…
Well, can you tell us first, I guess, a little bit about the company? Both, like, what you do and the, you know, what the company structure's like, I guess, and then more…
the immediate details of what the… how the collector is managed? Like, is there a team of… for observability, or infrastructure, or something like that?
Turan 00:03:56 Joe?
So yeah, this company is called Dance Commodities.
And we're kind of like an energy trader slash balancer.
We take excess energy, from, parties in Europe, or…
America, Singapore, and then we try and find ways to balance out any shortages or gaps in other countries. There are large power cables that travel across Europe to be able to trade energy between one another.
And, dance quantities act as kind of like a balancer in order to ensure
These large electrical operators are able to, use their energy, effectively, especially since, it can be quite volatile over here with, green energy, solar, wind, so… and, you know, storage technology hasn't come as far as yet, so…
It's quite, it's in our interest to try and sell that to other countries,
When there's a… when there's a shortage, when the weather isn't on our side, for example.
And in terms of structure, we've been undergoing quite a restructuring right now, but we are…
We've kind of… Have recently, a developer experience, a large developer experience team.
And then a large, kind of, enterprise platform infrastructure… enterprise infrastructure team.
And they tend to focus on, hypervisors, the bare metal,
The, networking, some of the core foundations of, of…
Our, of our infrastructure here.
And then, we have some metal management, and then it's the CTO,
And then our CIO, is relatively flat here, as is custom in Scandinavia.
Yeah, we could maybe say the same thing. We are on a… on a… also on a journey going from Windows VMs to…
So, Kubernetes.
So a lot of the hotel you collected is actually from Windows.
Yeah.
Yeah, just to, talk about who manages that stuff. For a long time, that was me and Bjorn here, who managed the OpenTelemetry collectors.
We received a,
We're quite early on, or at least when we adopted OpenTelemetry, we were quite early in our, kind of, containerization journey, looking into Kubernetes, establishing OpenShift here, and then the developers were also very interested in OpenTelemetry at the time.
And this was quite in its infancy. I mean, I think the collector at the time was around 0.12.
And, if I remember correctly, your logs… logs was in alpha. The developers had to kind of, yeah, try and, well, we were quite early adopters of the OpenTelemetry project.
And then, initially it was quite focused on workloads within Kubernetes, but we've kind of fanned that out to Windows workloads as well.
Collector setup.
Tristan Sloughter 00:07:28 is…
Turan 00:07:30 Pretty standard, I think, or trying to follow best practices, on what documentation says.
we have… At that time, we were running an OpenTelemetry sidecar, in one of, alongside our workloads.
And that was forwarding information to a gateway or a… or an aggregator collector that then did Kubernetes enrichment, metadata enrichment. It did any other kind of processing that we needed.
And then it sent that off to…
Wherever, you know, exporters or data sources that,
Yeah, wherever we were persisting that type of data.
And we have that… we have, kind of, a handful of clusters now, maybe 4 or 5 Kubernetes clusters, where we were copying that, that deployment,
Judd in?
We've since moved away from, sidecars.
And now we have used a daemon set on each of the worker nodes that run these workloads in order to, yeah, reduce the overhead,
From all these, sidecar collectors, since we've just been growing and growing, and we found the, yeah, the sidecars tend to, were consuming quite a lot of resources.
And at the time, early on in our platform… in our container journey, that would have been fine, but now we've kind of scaled to,
we have around 1,000 different services, and so the overhead kind of quickly starts to pile on. So we've adopted the OpenTelemetry operator.
collector operator, and that really helps us with managing the lifecycle of these, node-level collectors, the daemon sets, as well as these aggregator collectors that we have in each of our clusters.
Tristan Sloughter 00:09:28 Nice.
Turan 00:09:29 We're also getting, metrics from the Windows portion of things as well.
We have, a very similar setup where
We have a Windows virtual machine running a workload.
From, from ourselves, and, we have a collector instance running locally.
Very basic configuration, as well, just input OTEL, output hotel, try and keep it as light as possible, and then that also ships to a central collector.
Which then will do any kind of enrichment or filtering. And that's where we manage our… a lot of the complex configuration that we might want to do there as well at the central aggregators, and then it will just be persisted on, from there on.
So we have these kind of, aggregators dotted around, depending on network availability, network accessibility, you know, DMZ, VLANs, or any kind of network, constraints that we might have,
That,
Might make the setup a bit more easier for us to manage by having these aggregated, known points of collectors.
Tristan Sloughter 00:10:52 Is the collector doing… so you said with the windows…
the metrics from the Windows VM, is that… you said it was just OTLP in, so it's not grabbing any Windows-specific, metrics that it needs to know? Well, actually…
Turan 00:11:07 Yeah, we've just started to expand on that, and we're making use of the Prometheus receiver, and we're making use of the Windows exporter, so these Prometheus receiver will scrape the Windows exporter that we have. We would have loved to have used the built-in one, that's present in the OpenTelemetry Collector.
But, there are some, like, Windows-centric things, such as the Windows services, or ISS metrics, or the task scheduler, modules that I believe were absent in the built-in,
in the built-in one in the OpenTelemetry Collector, so that's why we resorted to using an external Windows exporter.
Tristan Sloughter 00:11:51 Okay.
It's a good little.
Turan 00:11:54 I guess we also split our data a bit, right? So we have the infrastructure data, and we have the…
the application data. Yeah, yeah, to make it easier for our developers, we try to,
We were previously running with Mimiya, on-prem.
And, so we try to isolate
Developer metrics with our platform metrics.
To make it easier for our developers, so they can just go to a particular data source and find all of their workload metrics. And this is also helpful for us to,
Tristan Sloughter 00:12:28 for a cost basis to try and ice… to try and.
Turan 00:12:33 Easily visualize the cost differences between workload telemetry and infrastructure and platform telemetry.
So, the source of the open… maybe we could talk a bit about that, I think?
what, sorry? The source of the OpenTelemetry, where… how do we generate the OpenTelemetry metrics? How…
how would a developer start interacting with it? Oh, yeah. Would you find that interesting?
Or is that something you'd like?
Yeah, so, we have a variety of different, develop, Developer maturities here.
We have a large software development team.
But we also have, kind of…
the mathematicians and the quants and the analysts who are writing in Python, who might not be, so mature with software practices,
even, things like Git, may, may not come natural to them. And so, in order to reduce, lower the bar, we've kind of made these, packages and extensions to kind of abstract a lot of the setup involved into adding,
OpenTelemetry, or alerting, or some of these basic features to make it easier for them to incorporate into their applications.
And, one of the which is, we've kind of wrapped the OpenTelemetry SDK for .NET and Python into their own, modules in order to bring some consistency, into some of the data they might send, and also,
To make it easier for them to adopt.
Yup.
Tristan Sloughter 00:14:24 Yeah, that's great to know. The… So you… Easier to adopt, so you're… providing a…
an API that's more familiar to them, or just easier.
Turan 00:14:38 Good question. I think it's… It's more familiar to them.
For example, using known environment variables to share stuff like service name and service namespace, and to have those conform to a naming convention that we've established here.
Some… and some things like that.
Yeah, so we try to set a lot of sensible defaults so they don't have to think about it. So, things we always need when we do
The telemetry stuff.
Tristan Sloughter 00:15:13 Yeah.
Juliano Costa | Datadog 00:15:14 By the way, when they, just a question for me. Hi, Giuliano, by the way.
Sorry for being late. When you say that you have that for them, that are not too much developers, or not familiar with coding.
do they use another platform to send those metrics? And within this platform, you have your .NET instrumentation set.
Okay, cool.
Turan 00:15:41 No, well, actually, I think metrics and telemetry as a concept might… they might not be fully aware of.
Because these guys are mathematicians, or they're meteorologists in nature, and they don't really know what observability is, or what telemetry is, so it's something that doesn't really,
come to them. Common things that I've seen is the typical printf, I am here thing when debugging, for example. So, this is, kind of, we have quite a varied level of maturity… software development maturity here, and these packages really just allow the…
Just to lower the bar a little bit with enabling certain things like telemetry.
If that makes sense.
Tristan Sloughter 00:16:25 away sometimes.
Bye, but…
So, do you use any auto instrumentation, then? Or is this fairly… they include it in their application, and…
We're off.
Turan 00:16:42 I think they, you know, they had the SD… do you mean, from the collector's perspective, like, the injection of.
Tristan Sloughter 00:16:50 Right, right, like, the operator supports… Auto-instrumentation stuff, injecting it.
Turan 00:16:55 No, we haven't made use of that. They primarily make use of the, yeah, SDK directly in their apps.
I think one of the main…
things during this kind of period where we're running both Windows and.
Tristan Sloughter 00:17:12 Kubernetes is that they just want, like, a level playing field where, they can have one way of doing things, so…
Turan 00:17:19 I think it would scare our developers a little bit if we were to say, well, you don't have to do it for Kubernetes workloads, but you do have to do it for Windows. They'd rather just apply the OpenSDK across all their workloads, and then they can rest assured that it works anywhere.
Tristan Sloughter 00:17:36 So it's an actual Python library they just include like they would anything else with pip or whatever, and…
Turan 00:17:42 Yeah, cool.
Tristan Sloughter 00:17:42 Right now, with the new, whatever the dependency management is. Okay. That's right. Yeah, I think that's a really useful thing to include, because we've been hearing,
People with different ways of, including the necessary
SDK or instrumentation, and making it consistent across the company, and getting more of that… because we don't… I don't think there's much, any documentation on…
different ways of doing that, aside from, like, the auto instrumentation on the website. But, yeah, giving people stories of what companies are successfully doing to ease the adoption inside is great.
Turan 00:18:19 It's also to help us to ensure that we get the right data, because they often don't think about what we need, or how we need to name things, or something like that, so we can kind of enforce that as well.
Tristan Sloughter 00:18:29 Yeah.
So, oh yeah, we've… Talked about the deployment of…
One question there is, what collector are you using? Are you using a Trib? Are you building your own?
Turan 00:18:48 For a time, we were building our own, early on, using the hotel, the builder.
But since we've now, adopted the OpenTelem, the operator, we've.
Tristan Sloughter 00:19:01 Hmm.
Turan 00:19:02 I think we were kind of, micro-optimizing, or I was micro-optimizing, just wanted to include the exporters and the, the right modules needed, but I've since just, used… we're using the contrip, images now since, and, yeah, just wanted to forego that extra administrative…
That extra maintenance involved in doing that.
We do still have to customize somewhat the images initially, as you might know, like, the sidecar concept in Kubernetes.
when to tell the sidecar to terminate, or when to prevent these long-running pods we've had great problems with, but I believe that was recently fixed in the native sidecars now in Kubernetes, so that definitely helps us a little bit, because
We need to package up these, shell scripts to know when the side
needed to self-execute when the main workload is terminated, but now with native sidecars, I believe that's not a problem. So, I think we can, yeah, minimize the amount of customization we need to add to these images.
Tristan Sloughter 00:20:07 So you still have some sidecars? Is that… that it's going away? You're transitioning from it? You're not done?
Turan 00:20:14 It's definitely… so we have, like, kind of, like, a deployment pipeline that our developers have to adhere to, but,
Some development teams are slower than others to update their deployment pipelines, and so we're kind of maintaining both the sidecars, which are dwindling in numbers, and having to move over to, yeah, a sidecar-less, workload.
Or experience.
Tristan Sloughter 00:20:41 How do you enforce the deployment pipeline? Are you using something like Flux or Argo, or is it a home chart template everybody uses?
Turan 00:20:50 Yeah, so, in the last couple of… in the last couple of years, we've been really been focusing upon, a developer portal, putting a lot of effort into Backstage. That, in turn, will template out a repository, a Helm repository, where it pulls, or…
It pulls these Helm charts that we've developed for these workloads, Python and .NET,
And that is synced by Argo CD.
So they don't really have much of an option to change,
To, to do much else, but to stick to this golden path that we've, laid out for them.
Tristan Sloughter 00:21:31 Nice.
And you mentioned the… so with the configuration,
You mentioned a little bit about it, and you said you could actually get us an OTEL bin rendering?
Turan 00:21:46 of what you're…
Would you like… is there any particular way you'd like it, like a URL, or a image, or…
Tristan Sloughter 00:21:54 Yeah, anything's… Either way.
Turan 00:21:58 You're alliance.
It's gonna be a huge new URL, shit.
Juliano Costa | Datadog 00:22:13 I think Zone may not allow the paste.
Turan 00:22:17 Yeah, it's a Jewish URL. I'll, I'll upload the image here if.
Juliano Costa | Datadog 00:22:26 Because to get the tiny URL, you need… you need to be logged in.
Turan 00:22:36 Now, how do I… Attach… is this button here? File? Yeah, I forgot it now.
Juliano Costa | Datadog 00:22:41 Oh, I wasn't even aware that we could attach stuff in some chats?
Tristan Sloughter 00:22:48 Any…
Turan 00:22:49 We're not very used to Zoom, so… There you go.
Oh, it's uploading right now.
Tristan Sloughter 00:22:56 Okay, hold on.
Juliano Costa | Datadog 00:22:57 Nice.
Tristan Sloughter 00:22:58 Awesome, thank you.
Let me… Save this…
Juliano Costa | Datadog 00:23:05 Oh, this is awesome.
Tristan Sloughter 00:23:11 Oops.
Cool.
Quick look.
Juliano Costa | Datadog 00:23:30 Sorry if I missed that, but just to… to see if I got, things right. The logs in on the top is… that's… that's something running in the cloud, and then, you know, the logs on-prem is something on-prem, and that's why it's not the same pipeline, right?
Turan 00:23:47 That's right, so we're currently in the process of migrating
our on-prem Alasa Search to, Grafana Cloud, Loki.
And, we're kind of doing it bit by bit, and, we thought the best way to do that was to have… separate the pipelines
Yeah.
Tristan Sloughter 00:24:09 Oh, so…
The cloud versus on-prem refers to where the telemetry backends are, not to where the services logging are.
Turan 00:24:19 Yes.
For the user, everything is in the cloud, but we still pull stuff from on-prem.
Yeah.
Tristan Sloughter 00:24:32 Routing… Sorry, what?
Turan 00:24:34 That's one.
Yeah, so, we've set up, like, in Grafana Cloud, you can establish a tunnel or something like, so you can still establish a connection from your cloud deployment in Grafana to on-prem Elasta Search.
And then we've just made that available as a data source for people to be able to, you know, query their metrics and…
With some guidance and documentation, I think it's a little… it helps the developers know where to go for their metrics, but we try and keep it as easy as we can for them.
That's huge.
Tristan Sloughter 00:25:09 you're routing… Based on prod versus non-prod. So you have,
All your environments going to the same collectors?
Turan 00:25:19 Yeah,
One of the difficulties that we've had, not related to OpenTelemetry, is trying to, is configuration management, that isn't… that is on these wind… that is on these virtual machines, outside of Kubernetes.
And, and… Setting up these…
differentiating between a non-prod and a production. We have very… a lot of environments, and then trying to map that to a collector.
It's not that easy here.
And… We've seen, resource utilization of the collectors seem to be small enough that we can
Not have them, you know, not have them too overworked, that the collectors are still very much able to cope with, traffic.
We've had some cases in the past with a lot of log data being shipped to us that might affect
the experiences in my production environment, but I…
I think we've since mitigated that, and
We haven't had any problems with this setup since, since…
Tristan Sloughter 00:26:34 But the majority of the collectors all land in Kubernetes. These aggregators run in Kubernetes anyway, even for the Windows stuff, we are able to scale that.
Turan 00:26:42 You know, quite easily in Kubernetes by just spinning up more replicas.
Tristan Sloughter 00:26:48 And is this actually the… the demon set?
Or the deployment, because you…
Turan 00:26:54 These aggregators would be the, deployments.
Tristan Sloughter 00:26:57 Either of the deployments are good. So the aggregators are basically just shipping it right to these aggregators? They're not doing…
Any other processing in them?
Turan 00:27:07 I'm sorry, can you repeat that?
Tristan Sloughter 00:27:09 So these are the… the aggregator deployments, and so you have a daemon set running on each, or you have a…
pod of collector running on each node, right? So it's just shipping directly, not doing any processing.
Turan 00:27:21 Yeah, so this… this image is, yeah, the, I'm not sure what the right terminology is, the gateway, or collector, or…
The uploader. Yeah, the… the.
Tristan Sloughter 00:27:35 The last hop before it persisted in some data source somewhere.
Turan 00:27:40 But yeah, the node daemon sets are much simpler, just, hotel in, hotel out, and we might have some configuration there to pass through the node IP, or the pod IP, just so we can do enrichment later on in these, gateway collectors.
Tristan Sloughter 00:27:59 Okay.
Juliano Costa | Datadog 00:28:02 Don't… you don't do… Any enrichment on the… on the sidecars and stuff? Like…
Turan 00:28:09 No, I think our worry there was… I think we…
With our deployment pipelines and, and,
RBAC configurate and the RBAC necessary to provide access to those… to that information. I think we just wanted to keep the sidecars as simple and as, plain as possible.
Juliano Costa | Datadog 00:28:29 Whereas, we have much more control over these, gateway collectors where we can.
Turan 00:28:36 customize the RBAC as necessary for these, for a limited set of, pods.
Juliano Costa | Datadog 00:28:44 Okay, and, again, sorry if I missed, but, the sidecar ones is…
This one, you are not using the contribib, right?
Turan 00:28:55 No, we're just using, the plain, basic image, or just a non-contrib image, yeah.
Juliano Costa | Datadog 00:29:02 the… the… I think the car has just OTLP components, so…
Turan 00:29:07 Yep, and that's all we need.
Juliano Costa | Datadog 00:29:08 I think there is even a smaller one, which is called OTLP. It has… just have, just has OTLP receiver and OTLP exporter.
Cool, cool, okay.
Nice. Tristan, do we have any docs? Are you taking notes?
Tristan Sloughter 00:29:29 I'm taking… this is recorded, right? And I'm taking notes. Oh, yeah, that's recorded, yeah.
Juliano Costa | Datadog 00:29:33 Okay, cool.
Tristan Sloughter 00:29:37 Yeah, I hope you're okay with… this is recorded. I guess it gives you a warning in the beginning, because all the hotel meetings are recorded.
I don't think they're anymore put on YouTube, at least.
Turan 00:29:48 Yeah, funny. That's nice. I'm shy.
Tristan Sloughter 00:29:54 the… So how… you mentioned, so you have…
you're running Katrip, how often do you… do you update the images? Is it just when you think you need it, or a regular cadence?
Turan 00:30:09 We try once a month, Yeah.
updating the Windows side of things, they tend to lag a little more because the automation is a little bit rough around the edges for the Windows VMs.
So, we're able to apply a much more regular cadence on the Kubernetes clusters and due to the operator, and due to our infrastructure as code approach to managing those clusters.
We're also in the process of,
adopting Renovate as well, which can also assist with the maintenance of those.
Tristan Sloughter 00:30:53 Yeah, that can also help if you're using OCB. It'll send you pull requests to update the different components in your image, if you wanted to ever go back to OCB.
Instead of having them.
Turan 00:31:05 But I don't think we'll… Yeah.
Tristan Sloughter 00:31:08 Yeah.
So,
Does anybody have any more on these first few topics of the deployment, management, configuration, or should we move on to…
the last few…
So then we were wondering, is there anything…
missing from the collector? I know you mentioned some stuff was missing from the Windows, exporter, so that… that could be one, we mentioned.
Is there anything else that you've wanted from the collector that you know of, maybe from another
Vendor, or just anything in general that you said, Oasis was there?
Turan 00:31:53 Yeah, the main one, a really big wish from us, has been rate limiting.
We have… Sometimes struggled to cope with the amount of telemetry that we received from our developers.
This can be…
And there are cases where applications, for example, they start crash looping, or they get into… or they lose connectivity.
And there's no sleep, or pause, or there's no… and so they just continue to loop and log, failure, failure, failure, failure. And some apps can do this every 10 milliseconds, and then what we find is that we just… we just log a lot of useless crap.
And now that we're… and then, previously, that was able to take down our Elasticsearch cluster, pretty easily. But now, of course, in the cloud, that incurs a cost now.
and… A big, a big…
Wish from us has been to, try and be able to limit the flow of telemetry from these workloads within the collector.
I've seen…
Alexis Search have a custom module that we were, prepared to try out and,
yeah, to experiment with, but we didn't get very far with it. And I know there is a larger effort, within OpenD, OpenTelemetry developer, development to add this as well. I've been keeping a close eye on it. But it would be, I think that's a really big feature that we kind of need, is to be able to,
To have a handle on some of these, on the flow of telemetry that we receive.
Especially, like, just like a… This is the maximum you can…
Yeah, there's some runaway processes sometimes, and because the maturity level is so different, they don't know how dangerous it is to put things in a while loop without any…
back off. So they can really be a packet cannon sometimes.
especially if there's something central that goes down, so all the applications start slogging like crazy. Yeah, we get, like, a thundering herd effect, where all these applications are complaining about something, and then we suddenly find ourselves over, you know, yeah, the issue cascades to our observability, setup.
But, something like a leaky bucket, algorithm, where we are able to have some kind of
E, where we can say.
this particular service from this environment has its own rate limit, and if you surpass that, then this one service will be rate limited, and all the others that don't match this particular pattern will be, you know, unaffected. And I think that allows us to, in a granular way.
Yeah, put a stop to a service that might potentially be a noisy neighbor for other
Other services utilizing that particular collector?
Tristan Sloughter 00:35:06 Is… So aside from rate limiting, is there anything you find frustrating with your usage of the collector?
Turan 00:35:18 None comes to mind, really. Since our adoption of Grafana, cloud.
we've started making use of their alloy collector, which has some OpenTelemetry parts within it. And there are some things that we like, such as the UI. I think the UI is quite nice for being able to debug in real time.
And see the flow of data passing from one component to another. That's a nice to have.
But, for the most part, I can't think of many… hey, Kat. I can't think of many,
annoyances that we've had by operating the collector.
To be honest,
just that, yeah, the rate-limiting one was a big one, and then the GUI would have been nice, but otherwise, it's a nice-to-have and not a necessity. But, the experience with the collector has been, fairly solid, actually.
Yeah.
Tristan Sloughter 00:36:20 Yeah, do you have any…
specifics on what you love about the Collector? It sounds like, I mean, you're using it in different environments, and that's been… that's been working fine, so it's able to run and…
Different places, and it's been solid in the sense of it's fairly stable for you, and…
Turan 00:36:41 Yeah, I think the, the components seem to be, like, all the parts that make it up seem to…
Really give us, the freedom to be able to pick Grafana, or mirror, you know.
It's assisted in the migration, very easily due to its… the amount of exporters available to us.
So, developers themselves, they don't really notice anything while we start mirroring the data to the cloud, and all that can be… is due to all these pipelines that we have running, and that's definitely a huge benefit of that,
Bingo, what's also really powerful is the OpenTelemetry transformation language.
I seem to find myself using that more and more with regards to being able to…
Do the routing, which is a really handy, component to have.
For our case here.
And, applying truncation where necessary, or…
modifying attributes where necessary, so I really, have begun to, like the TTL language, the OTTL language more.
And…
hotel bin, I think, has been quite helpful in that regard to verify or do some syntax,
validation, just to make sure that I don't get anything right. Yeah, just to test my validation off of…
Of the language.
Tristan Sloughter 00:38:23 You mentioned rooting.
So are you… you're doing something with the root span and a trace, or…
Turan 00:38:29 Oh, no, the routing component, the routing processor?
Tristan Sloughter 00:38:33 Oh, the round… sorry, yeah.
Turan 00:38:35 officer.
Tristan Sloughter 00:38:36 That's mine.
Turan 00:38:36 Recruiting, routing?
Tristan Sloughter 00:38:38 Good point.
Turan 00:38:40 Oh, and, I think we're… we're quite excited, or looking forward to using,
getting the internal telemetry from the hotel collector and packing… packaging that as part of the regular stream, instead of using some kind of external process to fetch that. I think that, from an operations perspective, that greatly simplifies being able to
monitor all these distributed collectors and set up alerting on these metrics that might be emitted. So, having that ship as open telemetry,
Helps us, in the administration of those collectors.
Tristan Sloughter 00:39:28 Was there anything else you… I'd like to add that you think should be included in those posts about…
How are you using OTEL in general, in the collector?
Turan 00:39:45 Get Microsoft on board?
Microsoft, yeah.
Juliano Costa | Datadog 00:39:51 Microsoft is one of the top contributors of.
Tristan Sloughter 00:39:53 Yeah, they're really involved. Is there something with, like, the… so the Windows components, is that… that's what you mean?
Turan 00:40:00 Yeah, no, I was more thinking about how well is it integrated with the Sentinel and the…
Tristan Sloughter 00:40:05 Hmm.
Turan 00:40:07 Oh, oh yeah, so I think what you might be talking about is the current exporter is focused around application insights, whereas I think we've been looking
We've… oh, that reminds me? Yeah, we've been looking forward to maybe seeing the next quarter that just ships logs to Azure Log Monitoring, without needing application insights, because we're using,
Azure Sentinel, and they're always desperate for needing more sources of information, and…
As far as I know, there isn't an opportunity yet to use the OpenTelemetry collector with Azure Logs, if I remember correctly.
Without using Application Insight.
We have a lot of compliance…
Things in terms of our applications, how they decide stuff, and so they have to lock that all the time for compliance, and…
as we are still a Microsoft house, somewhat, a lot of things tend to interact with that.
Tristan Sloughter 00:41:18 too many.
Juliano Costa | Datadog 00:41:20 Are you using Kubernetes in Windows?
Turan 00:41:23 Oh.
Juliano Costa | Datadog 00:41:25 Okay.
Turan 00:41:26 No, no, that's running on Linux.
Juliano Costa | Datadog 00:41:28 Good.
Tristan Sloughter 00:41:29 They have, like, two separate…
Juliano Costa | Datadog 00:41:31 Yeah, that will be brief.
I know companies that run K8s on Windows, and yeah.
Turan 00:41:40 No.
Juliano Costa | Datadog 00:41:42 Cool.
Turan 00:41:42 always transitioning from Windows to Kubernetes, but definitely not on Windows, that's…
Juliano Costa | Datadog 00:41:49 That would be silly.
One… one question that may help you answer this last question from… from Tristan. If you guys could think…
about yourselves, like, when you're starting. If you could give a tip for you, like, your younger self, Oh…
That may help you, kind of, answer.
this thing, like…
Like, what you would like to add to the blog post. So imagine you, a couple of years ago, reading this blog post, what would you like to, or what would you think would be beneficial to read?
Tristan Sloughter 00:42:28 What would have saved you some time? Headaches.
Turan 00:42:33 To be honest
We've been running the same setup for a while now, since the initial deployment, and I think the thing that greatly helped us is being able to
think about having these local collectors and these gateway collectors, and I think that's helped us scale this, setup.
And, our setup hasn't very much changed since the initial, adoption of this either. So, the one thing,
Then I… then I might say to myself… my younger self, it may be to invest more time in configuration management in order to,
Try and,
push out and keep the Windows portion of these collectors up-to-date and configured correctly. I know that there is some way of using remote configuration in,
In open symmetry, I can't remember of the technology…
Tristan Sloughter 00:43:34 Abandon.
Turan 00:43:34 Yeah, that's the one, yeah. But it wasn't very clear to me how to make use of that.
But I think Grafana's one is very accessible, because they have the GUI, it's all built into Grafana, and so, probably having that a bit more accessible, in the, in the collector might be, yeah, more worthwhile.
But yeah, I think configuration management and investing time in
managing these, remote Windows collectors, that could have saved me some time in the past.
Tristan Sloughter 00:44:06 Cool.
Turan 00:44:10 How about you? Awesome. You're… you're the… you're the OG. I'm just tagging along.
Tristan Sloughter 00:44:19 Just so when, when I'm writing this and describing stuff, so the…
The mathematicians and meteorologists, so are you… you're have… they're, like.
Predicting the upcoming, you know, winds and sun availability to predict where you might be moving electricity next?
Turan 00:44:38 Or, like, they also would look into the status of our… we have… we own some batteries, so they would want to look into the capacity, or…
How…
utilize these batteries are, and they try and predict whether we would need to sell energy offshore. Same with gas, gas storage.
See, okay, now, the power's probably going to be expensive here, because they are going to need a lot, because it's getting cold, or something like that.
Nope.
We're not really into what they are doing, but they seem to use a lot of compute when they calculate it, at least.
Tristan Sloughter 00:45:28 Nice.
Okay.
Do you guys have anything else you want to ask of them?
Turan 00:45:40 How's your involvement in terms of how we got in contact?
I'm a bit curious about that, in terms of…
Tristan Sloughter 00:45:49 Oh, how we got in contact with you.
Yeah, we were… so we started this, after we did a survey.
For end users, or not… of users of OpenTelemetry, and found that people were…
finding the issue with, like, production environments, how they wanted to deploy the collector, and not finding the documentation around, like, actual real-world deployments. We decided to
do this, set of blog posts interviewing companies, and then… so we reached out to… there's another SIG, the…
And you.
Juliano Costa | Datadog 00:46:24 Can you see, sir?
Tristan Sloughter 00:46:25 Yeah, and… Told them the…
Type of companies we were looking for, and they, put us in contact,
Can't remember the exact name of the person who… Set that.
Turan 00:46:38 Yeah, someone from Grafana, I think, I can't… I can't remember their name, but…
Tristan Sloughter 00:46:42 I think so. Oh, so, yeah, because you're a customer of Grafana, I guess, and that's how they knew you.
Turan 00:46:51 It's just curious, it was not, nothing wrong.
We're quite interested in just know what's going on there, so… Hmm.
Tristan Sloughter 00:46:58 Let's so…
Turan 00:46:59 It's cool that we can use this open
open set of standards so we can move around, and we have our freedom. If something doesn't fit us, we can move. That's really, really a big thing for us.
Tristan Sloughter 00:47:12 Both on-prem and cloud and so on.
Yeah, that you've… you're moving from Elastic to Grafana, right?
Turan 00:47:20 Yeah, we, we had a large…
Grafana, installation here, Mimeo, and…
Tristan Sloughter 00:47:28 Right.
Turan 00:47:29 Tempo, and alas as such.
Tristan Sloughter 00:47:32 Here, but it has now been.
Turan 00:47:35 A…
strategic initiative, to utilize more of the cloud. So we're trying to vacate on-prem and utilize cloud a bit more, and Profana Cloud is the… seemed to be a no-brainer for develop… for, for the effort needed to… to do this without, yeah.
Adding too much of an overhead or a burden to our developers.
Tristan Sloughter 00:47:58 Right, yep.
Cool.
I think that's all from us, I guess, can…
Everybody else stick around, we can talk about the blog post.
For Mastodon?
Juliano Costa | Datadog 00:48:19 Yeah, sounds good.
Damien Mathieu 00:48:20 Bad, sounds good.
Really appreciate it, guys.
Tristan Sloughter 00:48:23 Yeah, thank you.
Juliano Costa | Datadog 00:48:24 Joining?
Turan 00:48:25 Yeah, you're welcome. Sorry to say, sorry that it took a while for us to do this, considering the office reshuffle and things like that, but I'm glad we've done it, finally.
Tristan Sloughter 00:48:35 Yes, but we finally got it done. Awesome.
Turan 00:48:37 Yes.
Well, have a good evening, or a good afternoon, or good morning, wherever you may be.
Juliano Costa | Datadog 00:48:44 Yeah, that's the spirit.
Turan 00:48:48 Bye, guys.
Tristan Sloughter 00:48:53 However… Alright, so it…
Sorry it took me so long on the blog post, but I finally put some notes in there.
Juliano Costa | Datadog 00:49:04 No worries. Some of the things… some of the things that I will ask Tim to see if he can share this info with us, because, yeah, I do think it's,
It's about it.
information.
Regarding the number of pods, I have no idea, but yeah, he may know.
I've never run… have you ever ran a server? A mustardon server, Damien?
Damien Mathieu 00:49:29 No.
Juliano Costa | Datadog 00:49:31 Okay.
Damien Mathieu 00:49:32 Oh, so why…
Tristan Sloughter 00:49:33 Ooo, sir.
Damien Mathieu 00:49:34 Why?
Juliano Costa | Datadog 00:49:36 Because, the, they have the two servers that they run, the…
Damien Mathieu 00:49:41 Mastered on social and master in online.
Juliano Costa | Datadog 00:49:44 Yeah, exactly. Those two are deployed in one cluster that has from 8 to 15 nodes, and they have autoscale, but yeah, we don't know, like, what are the limits, and when it scales up, or when it scales down.
Tristan Sloughter 00:50:01 That… that's what… so I put, yeah, a note on the two servers thing, because I…
Didn't read that right, so maybe.
Juliano Costa | Datadog 00:50:09 Okay.
Tristan Sloughter 00:50:09 So you mean two Mastodon deployments that use.
Amazing.
Juliano Costa | Datadog 00:50:14 Yeah.
Tristan Sloughter 00:50:15 the dome.
Juliano Costa | Datadog 00:50:16 They call it servers, or… Yeah.
Damien Mathieu 00:50:19 Yeah, it's a deployment, for sure. It's a… I mean, it's a Rails app, so.
auto-scaling, can probably be done based on CPU usage, I think.
But we should… it really depends how we fare doing it.
Yeah.
Tristan Sloughter 00:50:40 Yeah, I guess just, yeah, making it clear, that's referring to, like, Macedon… independent Macedon, like, setups, that they run.
Because I run it as just meaning two services they were running that…
Didn't necessarily mean they were full mastodon, deployments.
So is it just a monolith? They just have one…
Monolith that runs to host everything?
Juliano Costa | Datadog 00:51:09 That's a good question. It's not a monolith, but it is a monolith, so…
Damien Mathieu 00:51:15 Yes, Mastodon is a monolith. It's a Rails app, an API, and a React app for frontend, and it does not manage multi-tenancy, so each of their instances… I think, I guess that's why they mention a server. Each of them has to be a separate deployment.
Tristan Sloughter 00:51:35 Okay.
Yeah, get the… Yeah, the main thing's…
I took away was that it would be nice if we had more on
how it's deployed and how a user of Macedon would deploy it, because I think that might…
Be… like, one of the interesting things that people would be able to take away was…
How they would include it in their own project without forcing it on users or something.
Damien Mathieu 00:52:12 I think it's…
I don't know if it's the best example, because, Mastodon… I mean, it's interesting to mention, but Mastodon does, like, being open source, they follow thematic versioning, and they cut releases, like, every month or so, but Mastodon.social runs on the nightly release, which is a container that is built every night.
And most people probably don't want to do that.
Tristan Sloughter 00:52:38 Yeah.
Okay.
Juliano Costa | Datadog 00:52:45 Don't they want to run the latest stuff? Like, that's the bleeding edge.
Tristan Sloughter 00:52:50 Everyone loves that.
Juliano Costa | Datadog 00:52:58 We are, I'm running a talk with a colleague,
in two weeks in Portal, and in the abstract, we mentioned the OTLP Batcher, but OTLP Batcher got rebranded to
OTLP batch.
So…
So then, in the abstract, we have, like, all dimensions to, hey, you should move away from batch processor to OTLP batcher, but OTLP batcher doesn't exist.
So, yeah.
It's gonna be fun.
Tristan Sloughter 00:53:35 And then it might… It'd be nice if we could… Yeah, if we had…
I don't know, some numbers around.
Their telemetry, and then we could also tie that into… if they have numbers around
Their collectors set up.
like… Any batching or memory limits, and… because that we can… Cause they… that's all…
Juliano Costa | Datadog 00:54:00 But, we do have the whole thing, don't we? I think it's just, minimized, right behind your cursor.
Yeah, I just opened the drop-down.
Tristan Sloughter 00:54:11 Oh!
Juliano Costa | Datadog 00:54:14 It's just that… It was too… Too big, so I…
Tristan Sloughter 00:54:20 Yeah, okay.
Juliano Costa | Datadog 00:54:20 oppressed.
Tristan Sloughter 00:54:21 Yeah, maybe…
Juliano Costa | Datadog 00:54:21 So this… this also answers the thing about, like, the renaming, but I see your point. Maybe I can,
Explain one of those transform.
Tristan Sloughter 00:54:32 Right, pull some of it out into…
Juliano Costa | Datadog 00:54:34 Yep.
Tristan Sloughter 00:54:35 what they're doing. Cool, okay. The same with, maybe… Well, I wonder…
So this is their… for their deploy… it might be useful if we're able to show or mention something about how
The… because, like, one of the unique things about them is that other people are deploying it, so, like, how they configure their own when they're deploying, and they have a different
They don't need, like, as much, like, their memory limits would be different than, like, how they're configuring their own collector, could be…
Just a neat point to point out how the operator is used to
So, other users can deploy their own form of the collector, I guess, or they might.
Juliano Costa | Datadog 00:55:27 This is…
Tristan Sloughter 00:55:28 they're pushing it somewhere else, and stuff like that. Like, you have to deploy… you have to configure… they're not pushing the Datadog, so they wouldn't use the Datadog exporter.
Things like that. Just… kind of… Talking about how…
use of the operator and Kubernetes resources makes it easier.
For end users, I guess.
Juliano Costa | Datadog 00:55:57 Where would we add that?
Tristan Sloughter 00:56:01 Hmm.
Juliano Costa | Datadog 00:56:05 Before the… so after the… the collector, after the config, And…
Before they're staying up to date?
Tristan Sloughter 00:56:18 Yeah, maybe… or the external setups.
Oh wait, no, that's… Yeah, in the external setup section, maybe?
Juliano Costa | Datadog 00:56:30 Because that's where you talk about… There you go,
Tristan Sloughter 00:56:33 How it's used by other people, I guess.
Juliano Costa | Datadog 00:56:49 Huh.
Okay.
Tristan Sloughter 00:56:57 Yeah, I guess just… Yeah, the operator…
how a user deploying the Mastodon helm chart or something would configure their own…
Collector. Like, you don't have to use… you don't use the same one.
Mastodon uses.
You know.
Just, yeah, the unique things about…
their setup and how it utilizes OpenTelemetry to make that easier, I guess.
I do have a knit, but it's a direct quote, so I don't know that we can do anything about it.
When he says, if it crashed for some reason, we didn't even notice, the operator brought it back up automatically.
It's just a knit that the Kubernetes is what's bringing it back up, unless it's, like, a…
something else wrong. So, I don't know if that matters, or just leave… because it is… the operator makes it easier to use.
But…
Juliano Costa | Datadog 00:57:54 That's do it.
Tristan Sloughter 00:57:54 pod crashes, Kubernetes restarts it.
It's under the collector.
Can't really change it, because it's a.
Juliano Costa | Datadog 00:58:09 I mean, I don't… I don't… I don't think he'll… he will care.
If we… if we change to the…
Damien Mathieu 00:58:19 I mean, we can, we are asking them to review, so we can add a comment saying we have changed this direct quote to make things better. Do you still agree with it?
Tristan Sloughter 00:58:29 Yep.
Burke.
Yeah, and so they don't use any auto instrumentation, right? They're just…
Using, what, instrumentation libraries from Ruby and stuff?
Damien Mathieu 00:58:57 I think so.
Tristan Sloughter 00:58:59 Okay.
Juliano Costa | Datadog 00:59:04 Sorry, what was the question?
Tristan Sloughter 00:59:06 Not just if they use any auto instrumentation.
Juliano Costa | Datadog 00:59:09 they use, Ruby, and that's, they use the…
They define the packages, so they use instrumentation libraries, not the auto-instrumentation.
I know because, yeah, I contributed that.
Tristan Sloughter 00:59:37 Brilliant.
We're out of time, we can… Call it here.
Juliano Costa | Datadog 00:59:43 Yeah, but thanks for reviewing. I'll take a look, apply the things, and adapt, and then I'll…
a ping team, just because, yeah, he always… he always replies on the third ping, so… Helping him.
Next week I'll be in the New York
office of Datadog, so I may not join. And the following one, I'll be in Porto, presenting at a conference.
So, I also won't join, so that will be 2 weeks of me off.
Tristan Sloughter 01:00:27 What's the next one we want to get out? We have… Adobe Skyscanner, Atlassian…
Juliano Costa | Datadog 01:00:34 This, the one today is for.
Damien Mathieu 01:00:36 Sorry, I actually need to drop.
Tristan Sloughter 01:00:38 Yeah, no problem.
Damien Mathieu 01:00:40 Text you later. I think we can, decide that asynchronously.
Tristan Sloughter 01:00:44 Yeah. Yep. Okay.
Juliano Costa | Datadog 01:00:45 Cool. Sounds good.
Yep.
What was the name of the company that we interviewed today?
Tristan Sloughter 01:00:55 Bonst? D-A-N-S-K-E.
Juliano Costa | Datadog 01:00:58 Okay. Are they… are they the medium one? Because I think that they could be the second one.
Tristan Sloughter 01:01:05 Yeah, I think they're the second one.
Yeah. Okay.
And I can get to work on that.
So, we have… Atlassian, Skyscanner, Adobe, Dunks…
And mastodon. I think that's all of them, right?
Okay.
Yep, they should be the next one then.
Juliano Costa | Datadog 01:01:31 Atrasin, Mastodon, Skyscanner, Adobe, And this one today. Yeah.
Tristan Sloughter 01:01:38 Cool.
Cool, alright.
Juliano Costa | Datadog 01:01:41 One sec, let me just make sure I downloaded the image.
From the chat.
Tristan Sloughter 01:01:50 Oh, yeah.
Juliano Costa | Datadog 01:01:51 Otherwise, we may lose it.
Yeah, okay, it's here. Great.
Oh, wait, where is it?
Okay.
Cool.
Thanks!
Then, serum on the internet.
Tristan Sloughter 01:02:20 Alright.
Nope.
