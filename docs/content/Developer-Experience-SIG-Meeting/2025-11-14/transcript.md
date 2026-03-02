SIG: Developer Experience SIG Meeting
Date: 2025-11-14
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**akasprzok** 00:25 Good morning!
**tristan** 00:31 Hey, I had to… Unplug, I think.
Zoom doesn't recognize my camera anymore, my external camera.
**akasprzok** 00:40 Exciting.
**tristan** 00:41 Yeah, that's fun. It just stopped working, probably an upgrade to Zoom.
**akasprzok** 00:47 Upgrade, quote-unquote.
**tristan** 00:50 Yeah.
You got a festive shirt on, that's nice.
**akasprzok** 00:53 Yeah, I thought I'd dress up.
**tristan** 00:55 Like that.
Like, it's the summer or something.
**akasprzok** 00:58 Yeah, mid-70s here in Denver.
**tristan** 01:01 What!
Wow. We've already got… well, I mean, it melted, but we got a good bit of snow at one point.
Yeah.
**akasprzok** 01:09 It's, it's, like, late summer here.
The… all the, all the ski resorts are panicking.
**tristan** 01:17 Yeah, I bet. Yeah.
**akasprzok** 01:19 I bought… I bought boots too early.
**tristan** 01:22 Oh, yeah.
**akasprzok** 01:22 Thanks to everything.
**tristan** 01:25 You ski or snowboard?
**akasprzok** 01:27 Snowboard.
**tristan** 01:28 Nice, nice.
**akasprzok** 01:29 Yeah.
Are we, are we waiting on people to trickle in?
**tristan** 01:35 So, I don't… I'm not sure the other two are actually gonna join, because it's 4 o'clock their time.
**akasprzok** 01:40 Okay.
**tristan** 01:41 And that's.
**akasprzok** 01:42 Friday.
**tristan** 01:42 Yeah, I'm giving them a chance in case they decide to, but yeah, we can probably just get started, and the…
This is being recorded, is that okay? It won't, like, go out or anything.
**akasprzok** 01:54 That's alright.
**tristan** 01:55 Just so I can… they can look back at it, and I can look back at it.
**akasprzok** 01:58 Yeah, for sure.
**tristan** 01:59 Alright, good.
And I'm taking notes, but .
Yeah, I'll ask questions that…
I know the answer to, but the…
In the recording and stuff.
**akasprzok** 02:11 Yeah.
**tristan** 02:12 Alright, yeah, we can just get started then. So, I sent you that list of questions that we'd go over, or topics we'd go over.
And we can do it.
**akasprzok** 02:21 Have a bit of stuff prepped for it.
**tristan** 02:23 Awesome, perfect. Yep, we can just start from the top, where…
We can talk about the company structure, like.
who owns both, the hotel collectors, but if the company does anything around, SDKs and how people install any auto instrumentation, things like that, which I think it's just the collector, really.
**akasprzok** 02:44 Yeah, is the… the recording is running?
**tristan** 02:48 Yes, I believe so.
**akasprzok** 02:50 Yeah, okay, there's.
**tristan** 02:51 Okay, yeah.
**akasprzok** 02:52 Okay, cool. Yeah, so,
We run hotel collectors as daemon sets, across the board, and people push…
Metrics, logs, traces, whatever, to them, over,
node, host network. We run Kubernetes everywhere, and,
Overall, we have, around 12,700 hotel collectors. Most of them are in data centers,
With the biggest data center having a deployment of around
2,400 and change nodes, and each one of those is running an hotel collector.
And yeah, I manage them.
**tristan** 03:57 Yeah, it's…
**akasprzok** 03:57 Full stop. Yeah.
**tristan** 04:00 the… You're within the team of one, so you can just go with that.
**akasprzok** 04:06 Yes, yeah, I am the observability team at Grok.
**tristan** 04:13 the… Oh, I think… get to that again later. Yeah, update cadence and stuff like that. So…
Yeah, we could… yeah, we'll just cover the team mostly there. We'll stick with that. Well, I guess we'll go with,
Like, so you mentioned the demon sets, this then forwards to,
Like, what they call a gateway collector?
**akasprzok** 04:39 No. Each,
each data center has its own logs and, metric backends. These are fronted by,
They're Victoria metrics, Victoria Logs and Victoria metrics, and I use, VMAuth, which is their, proxy in front of them, and that's what the, the statement sets…
Per, per cluster, slash data center forward to. So there's one logging backend per cluster, one metrics backend, and traces go either to tempo.
For anything that's not in a hot path, and for Honeycomb, for anything that is HotPath, so anything that, like, is involved in serving an inference request.
But, ancillary things like model registry or similar,
those go to, tempo. In… because we're tail sampling, we… and we have data centers, on 4 different continents, we need to be very conscious of… of bandwidth, so…
in order to forward all the traces to Honeycomb Refinery, where we do tail sampling, we use the hotel, with the Apache Arrow,
Receivers and, words are escaping me right now.
Yeah, we use those components to,
stuff the, all the traces into the arrow format, and that saves us, like.
90% of bandwidth, I think, is what I came up with the first time around.
Haven't really touched it since I implemented it. It's just been working very, very well.
**tristan** 06:37 Bird.
And that, and that's a…
Refinery, deployment that's running, right?
**akasprzok** 06:45 Yes, yeah, yeah, it's a refinery deployment. It's running in, in GKE, actually, in, US West 1, and that gets traces from all over the world.
About… I think it's about 80,000 a second right now.
And, a similar volume goes to tempo.
**tristan** 07:11 Throw a bug.
And so But with Tempo, they're… Are… they're going from…
the Demon sets are going directly to Tempo, or is that…
Oh, okay, right.
then… That's an interesting… Because the…
Just to put the scale on what tempo
Can handle it, because it doesn't have, like, a…
There's nothing in front of it, there's all those nodes connecting to it, that's good.
Good.
Point to have in here. Nice.
Perfect.
So then… Or the… Oh, wait, diagram showing where the collectors are deployed.
Forgot we had the… I can…
handle that if you're okay, since you've already.
said all that, so that's basically… I can talk about how many data centers, and oh, you got something?
**akasprzok** 08:15 Yeah.
**tristan** 08:15 That was nice.
**akasprzok** 08:16 I have an auto bin of the collector config. It, it struggles a bit with how big it is.
**tristan** 08:22 Yeah.
Awesome, perfect.
**akasprzok** 08:26 Let me talk about that a little bit. So we have, we grab logs from a variety of sources. We obviously grab Kubernetes pod logs, also, the API server audit logs.
We have several applications that, send logs that they process from other sources, like, Vercel, for example, that are pushed over OTLP.
And also, we get logs from, TELUS, so we learn Telex Linux in all of our data centers.
For receivers, we make a lot of use of host metrics and kubelet stats.
But that doesn't even begin to cover all our use cases. So in…
in the, in the daemon set, in the pods, I also run, kubestate metrics as a pod, that is, tailored to just grab the pod metrics for the node.
Ipmi Exporter, Node Exporter, and, RDMA Exporter.
Node Exporter gives us a lot of stuff that, doesn't have a, an OTEL receiver equivalent, especially around network metrics.
Rdma Exporter also doesn't have an equivalent
And we also scrape CAdvisor.
Ipmi is, is obviously for, you know, IPMI stats,
And, wait, did I mention RDMA Exporter? Rdma Exporter for, direct memory access. So, we… we also run GPUs in addition to our LPUs, and, need those stats as well.
So that, that's a whole lot of metrics. It's around, 300 million data series right now.
**tristan** 10:35 How many data series?
**akasprzok** 10:36 300 million.
And that is not grabbing everything. Like, Node Exporter, we only have, we have a couple collectors, enabled. RDMA Exporter, we throw most of it away. This is all already, like, pre-tailored to just what we need.
What else? We, we run a custom, collector Distro?
We have a… We have a couple receivers that we've built, for example, for,
EDAC, metrics, which are not currently exposed by Host Metrics Receiver. So we just clone Host Metrics Receiver and tore that part out of Node Exporter and chucked it in, but we're…
placing that, again, with Node Exporter. We thought we could get by with, just the OpenTelemetry Collector, but it turns out as we're just, like, kind of, like, refining our operations, we find more and more metrics that we need that
It, we'd either have to write a bunch of custom… Hotel receivers, or…
We can just use Node Exporter.
So… Since, you've left Node Exporter has gone back in.
**tristan** 12:07 Okay.
**akasprzok** 12:17 Totally.
Go ahead.
**tristan** 12:21 Oh, one second, trying to blow this up.
I could see everything.
Oh.
It's gonna be a… Doozy to figure out what to put in the…
**akasprzok** 12:39 Plugged.
Yeah, it's…
It's pretty big.
**tristan** 12:44 Yeah, I was… Let's pull it up to a couple… important things. The…
I think some interesting things people…
We'll want to hear about is simply the…
Demon sets, sending the tempo, the use of arrow…
And how many data centers you're using, and then how many nodes of things are being used, and then once we get into the collector itself, like, the config of the collector itself, probably be…
Number of things on the… what, you know… Messing with attributes, and…
figuring things out, and what people might be able to learn from that. I'll dig into this again as I write the blog post up.
**akasprzok** 13:33 Okay.
**tristan** 13:33 But…
**akasprzok** 13:35 We… the nice thing about running a bunch of containers in the pod alongside UltaCollector is,
is that it makes it really easy to just, like, scrape the stuff, since the datasets are running on host network already anyway, so I can just, like, I can chuck another container in there, and then be like, hey, Prometheus, scrape this port, and it just, like, works.
And, that's very nice. We don't use, we don't use the OpenTelemetry operator.
Mainly because of lack of configuration validation.
And…
Well, I've tried to move to it recently because I wanted to give Target Allocator a try, but we collect certain metrics from applications that are extremely sensitive to missed scrapes.
**tristan** 14:34 So…
**akasprzok** 14:35 I didn't want… I didn't want, oops, like, the… the daemon set rolling to, like, miss a scrape.
So for that, we're still running VM Agent, and we're double scraping everything.
Because that lets us, like, roll those pods, you know, in an HA setup, without interrupting. But for anything that is, that is no specific, the LTEL collector's been great.
So, yeah, I just have a…
like, a straight deployment with bells and whistles instead of using, like, an OpenTelemetry collector CRD.
**tristan** 15:15 Hmm.
And that's deployed through,
**akasprzok** 15:19 Sucks.
Yes. Config map generator for the,
For the config map, and that just, like, works.
Ship changes all day, whenever needed.
to all the data centers all at once.
We got pretty high confidence right now in being able to make changes there.
the… the 200…
hotel collectors that are running in the data centers, in the GKE clusters, excuse me. Those obviously have a different config than the ones in data centers. We don't need all of those, host metrics, for example. So those have a much more slimmed-down
config, but I think the data center one is the interesting one here.
**tristan** 16:09 Yep.
And the, the… So the… Cadence on the deployments is pretty much… ad hoc.
**akasprzok** 16:24 Yeah. Yeah.
Yeah, just, like, straight out of head, main.
Changes go out.
You know, I'm… I'm code owner,
When, when there's stakeholders that need something specific, they generally just work directly with me, and, I roll.
Out any changes that they, they require.
**tristan** 16:53 So, for components, so… And this is using OCB to build an image.
**akasprzok** 17:00 It is, yes.
**tristan** 17:01 And then… So, for different components, it's just…
when there's nothing saying, oh, this component has an update upstream, maybe you should upgrade, it's just, you check…
**akasprzok** 17:15 Yeah, no, we don't, we don't have any automation around that just now. There's no specific reason for that other than that I often have bigger fish to fry, so whenever I make every month or so, I get around to just updating components.
And we have some… we have some smaller, like.
we have some smaller cells in some of the data centers that we have set up as kind of, like, lab environments, that I will often change these, test these changes in first, before I roll them out wide. So it's… we've kind of built, like, our own
Staging or development environment.
That runs, like, on our production racks.
**tristan** 18:07 Okay, that custom build…
**akasprzok** 18:09 The Grok cards themselves?
**tristan** 18:13 Yes.
**akasprzok** 18:13 So our, our big differentiator, the LPU, those push metrics.
to the LTEL collectors, over, OTLP.
**tristan** 18:28 Is that some custom…
**akasprzok** 18:31 That's some custom C code or something that the… It is the C++ OpenTelemetry library.
**tristan** 18:37 Oh, okay, okay.
**akasprzok** 18:38 Huh.
**tristan** 18:41 Nice.
That's cool.
**akasprzok** 18:51 Yeah, and a lot of that is, you know, it's like,
Voltages, current draws, temperatures, that kind of thing.
**tristan** 19:02 The kind of stuff that you never have to worry about if you live in, like, AWS and GCP.
And you're doing that… I mean, you're worrying about kind of stuff like that across…
even outside of the LPUs, because you're running your own data centers and hardware, so…
**akasprzok** 19:19 Yes, so we need metrics off of, like, rear door heat exchangers, inroad chillers, PDUs, you know, the BMCs, all of the network switches, etc. All of that stuff is getting scraped.
**tristan** 19:42 And so, yeah, I think with this hotel bin and the overall layout, I might… ni…
I'll probably ask you… Maybe to write down, or…
I don't know if you could share, like, the image you have of what is in a collector pod.
**akasprzok** 20:04 T.
**tristan** 20:04 If you'd be able to…
**akasprzok** 20:05 I can share that with you, is that gonna grow… I could… Like, in the blog post?
**tristan** 20:14 I could reproduce, like, a slimmed-down, simple… just to say, like, this is what they're running in the Demon…
**akasprzok** 20:20 Okay.
**tristan** 20:21 You know, I can also just write it out, I don't have to put everything, but just to sort of.
Give that.
**akasprzok** 20:29 Yeah, let me…
I can share that with you, but, probably don't want to just, like, straight copy and paste that in.
**tristan** 20:35 Yeah, I won't do that.
**akasprzok** 20:37 It's a good way to do that here.
Nope, that is too big.
Best way to share that with you.
Oh, I know.
What's a good email for you?
T-Slaughter…
**tristan** 21:14 Yeah, well, no, that's Tristan at slaughter.dev.dip.
If you… yeah.
**akasprzok** 21:23 Alrighty.
I just shared with you via email, with also some of my notes.
**tristan** 21:34 Perfect.
Perfect, perfect, got it.
I'm sure you know it.
Alright, it's letting me in. Just make sure this works.
Then we can get to questions about…
Collector… oh, perfect. Alright, I got it.
So good.
So are there any… I guess one pain point you've…
Already mentioned, that's not exactly a pain point, but that you… Move back to NodeMetrics.
**akasprzok** 22:13 Notice Quarter? Yeah.
**tristan** 22:15 Hmm.
**akasprzok** 22:16 Again, there's just, there's a lot of collectors that are missing.
**tristan** 22:23 That…
**akasprzok** 22:24 I get their kind of, like, niche, niche, a little niche, but that are extremely vital to anyone that, you know, is running a data center.
**tristan** 22:41 I often see them.
**akasprzok** 22:43 Proposed, but then… Like, denied.
**tristan** 22:51 Proposed.
As in, like, PR?
**akasprzok** 22:54 As, as, as, issues, sometimes also PRs.
**tristan** 22:58 Oh, interesting.
**akasprzok** 23:00 Some of them eventually, like, they at first, don't get approved, but then end up making it in, like, I think Redfish just recently made it in.
Probably gonna start using that. Currently doing that via,
for BMC access over a tool that I wrote in Go.
But, yeah, that's, that's, like… I get that there's, the quality should be high, you'll want to be picky and choosy about what goes in, what doesn't,
But that's… that's why I run so many additional containers, is so I actually have that, like, Swiss Army knife.
And I'm, like, I'm… I'm… I'm okay with that being the way that, that, things are right now. It would…
it would streamline my workflow to be able to have those receivers in OTEL, and then…
Not have to scrape them via Prometheus, but just, like, being able to use the… everything, like, the pipelining as it stands.
**tristan** 24:11 Yep.
**akasprzok** 24:15 But it's, you know, it's working well, in the state that it is right now.
One of the… one of the other pain points is, around routing for me.
if I have a ton of different use cases that need to go through slightly different pipelines for different types of traces or logs,
I have to either open up another port.
That then gets its own,
I think service pipeline, or I have,
I have to, like, route based on headers, for example.
Right now, I'm mostly doing the former, where I have a bunch of ports open. I think I want to move more toward the latter, but there's no, like.
abstraction around, here's different users or use cases, and their specific needs. That is something that I have, for, like, Victoria Metrics and VMAuth, for example, they have, like, the concept of a user.
That gets, or doesn't get to use different paths.
But I imagine that is, like, a… that's kind of, like, an outlier as far as use cases go.
Simply with, yeah, with being such a vertically integrated company.
You end up having so many different use cases that it just makes the pipeline a little unwieldy at times.
**tristan** 25:59 Yep.
Okay, that's your main… the pain points?
**akasprzok** 26:06 I think that's pretty much it.
I… I would still entertain moving to, OpenTelemetry Operator, once that matures somewhere, but…
Also, just, we're just generally big fans of, like, raw Kubernetes manifests here.
**tristan** 26:27 Keep it simple.
**akasprzok** 26:28 Yeah, and
from that perspective, it's been working real well. I have… I have SLOs around all my OpenTelemetry collectors, both on a per-cluster and a, just, like, production-wise scope. Most of those are based off of,
they're using Sloth based off of Prometheus metrics, and overall,
like, I have… I have four nines of uptime on, on all my pipelines, and, like, from that perspective.
Botel Collector's been fantastic.
**tristan** 27:05 Yeah, thanks for calling that out, because that's a good one, really good one to put. Because there was… yeah, I guess I should have…
So there's also, as OpenTelemetry is working on graduating through the CNCF.
There's, like, a… bunch of…
not… there's things… CNCF is called out that need to be done. One of them getting done, it's called Blueprints, and, like, they're, this…
set of blog posts is sort of being correlated with blueprints, which are, like, production use blueprints of OpenTelemetry.
And, so, yeah, definitely stuff like,
how you do SLOs is gonna be important to call out, so make sure that's in the blog post, and…
**akasprzok** 27:53 Yeah, give me a second here, let me pull something up for that for you.
**tristan** 27:59 Perfect.
**akasprzok** 28:07 It's an observability…
Oh yeah, that's, like, it's pretty straightforward. I'm gonna…
Put that down at the bottom, so it was… Using sloth.
Let's see… recording rules… This cluster is big.
Oh, that did not paste well.
Yeah, Google keeps…
**tristan** 29:08 Markdown now.
Alright, how do I do that?
If you right-click, it should give you a paste markdown option.
Or, like, paste from Markdown or something, I can't remember what it's called.
Seeing that…
**akasprzok** 29:30 I still have to do…
**tristan** 29:33 It doesn't work in Firefox, but I'm pretty sure I've done it in Chrome.
**akasprzok** 29:43 Certainly… Right, and then these, these look something like…
The recording rule looks something like this.
So that's, that's, like,
That's pretty straightforward, and it, you know, it works across the three different, types, and that's what most of my SLOs are around right now.
Obviously, a lot of, networking also, also involved in all of, in all of this.
**tristan** 30:40 Since the memory goes down, I can't sense stuff.
the… So with,
we… what's, like, we sort of discussed some things that are missing from the collector, but for, like.
I guess including the routing stuff, the… is there anything else, like, general purpose that you… you'd see as missing? You could even include… I don't know…
I was gonna say… So yeah, you use Refinery's tail sampler, so…
Would you say, like, the OpenTelemetry collector's tail… have you ever dealt with its tail sampler, or it was just because you were using Honeycomb, so you went with Refinery's tail sampler?
**akasprzok** 31:33 Refinery is more fully featured as far as, like, the rule set that I can express.
To perform tail sampling in it?
So it's, it's, it's more user-friendly, it's, A more, mature product.
And…
it is also extremely memory and CPU efficient now with Refinery 3, so I don't see myself switching to, the OTO collector for that.
The other thing is, introspection.
I'm gonna bring up, Victoria Metrics again, because, you know, that's, like, the other…
toolset that I use. It has… it has little, like, introspection, HTTP, endpoints?
for each of its components, so I can, you know, I can just, like, port forward and go in and see what the configuration is, where the problems are, and also, do some, like,
debugging…
**tristan** 32:49 Right, on the container.
**akasprzok** 32:52 And that is much more difficult with OpenTelemetry Collector,
like, yeah, Target Allocator has some… has some endpoints for that, where I can look at, what the different, like, how targets are getting distributed.
the Prometheus receiver has, the API server attached to it, but it's…
it's still a lot more difficult to introspect on a higher level than some of the other tools that I'm used to.
**tristan** 33:32 Have you used the… I don't know what it provides these days, the… it wasn't much when I tried it… the Z pages for the collector?
**akasprzok** 33:39 No, I have not.
**tristan** 33:41 Yeah, there's an extension called ZPages.
it provides some endpoints to give you at least some Information about what's going on.
**akasprzok** 33:55 Oh, cool. I have not heard about this before.
I should check that out.
**tristan** 34:02 Please.
from… I think it's an old Google thing that is called ZPages.
**akasprzok** 34:07 Okay.
**tristan** 34:09 Cool.
**akasprzok** 34:12 Neat, I will check that out. Thanks.
**tristan** 34:19 So, like, yeah, then we can get to…
If that was everything we can get to… what you love about the collector, you've mentioned a few things of…
I guess.
Just talking about how it's run well, you haven't had any issues, really.
**akasprzok** 34:35 Yeah, uptime has been extremely good.
**tristan** 34:40 Especially, Aero has been…
**akasprzok** 34:43 Amazing.
Kinda… that reminds me of a bit of a frustration again, like, the TTL is not well documented.
The, the, The transformation language, can be a real bear to figure out at times.
But… Yeah, other than that, it's been running extremely well.
Consistency is good with, with logs, it's pretty efficient,
And there's no, like, oh man, I have to periodically restart the thing, or anything like that.
So overall, the experience has been…
Very smooth, and just generally not be… having…
**tristan** 35:33 any sort of lock-in to anybody, obviously.
**akasprzok** 35:38 we can… we can do, like, we can do things like, oh yeah, we set up for… for Honeycomb, but, I don't have the budget for… to meet everyone's needs, so I'm gonna spin up Tempo, and then just starting… start sending some stuff to there, and it, like…
**tristan** 35:51 Hmm, just works.
Who knows?
And the… yeah, the main… Thing that has come up…
Most of the time, in the, like, frustration.
is, and you didn't mention, was, like, changes, breaking dashboards and stuff like that, like, metric names, changes from the collector, something like that. Have you had any issues like that?
**akasprzok** 36:16 No.
**tristan** 36:17 Okay.
**akasprzok** 36:19 I do want… I do want to make, like, semantic conventions and, and just, like, metrics and log schemas more of a focus. I saw Weaver for that. I want to check that out, over the next two quarters, and see if that is something that would make sense to roll out company-wide.
But, other than that, I…
I haven't seen any issues with that, no.
**tristan** 36:48 Okay.
**akasprzok** 36:49 We also, we do keep all of our, all of our dashboards in JSON, and, at least for observability, so when there are breaking changes, it's, you know, it's just like a find-replace.
**tristan** 37:01 Hmm.
That's a good point.
And those are deployed with Flux as well, right? Yeah.
**akasprzok** 37:13 Yeah, using the… making heavy use of the Grafana operator.
**tristan** 37:27 Should I note that? Okay.
So, is there anything… Well, I guess one question I forgot to ask. So, you don't…
You've mentioned you don't use the operator,
There's no, auto instrumentation use at Grok, is there?
**akasprzok** 37:48 Oh, okay, let me rephrase that. We have the operator rolled out.
**tristan** 37:53 Oh, really?
**akasprzok** 37:54 use it for auto-instrumentation purposes. We do not use it to, deploy the dataset.
**tristan** 38:03 Okay.
That's… okay.
Has the…
experience been okay, though, then using auto-instrumentation with the operator? Yeah, seamless. You know, and I really don't have much to talk about, because it just works.
So yeah, we've gone over all these parts. Is there anything you'd like to add that you had.
notes or anything?
**akasprzok** 38:44 I,
I think, okay, one thing that… either I haven't run across the right resources, or…
Or maybe it is just, like, that's just the way it is right now,
Building new receivers is not very intuitive. I'm…
I'm still relatively new to Go, but a lot of the tools that I've used, they provide…
a good out-of-the-box experience for getting started, like Cube Builder, for example.
Makes it really easy to build an operator.
there's no… there's no good harnesses like that around building receivers. Internally, well, the…
Like, the heavy use of the, the,
the inputs and whatnot that stanza, contributed, like, that makes a lot of sense.
It also,
Makes it frustrating, often, to find good prior art to base what you're trying to do off of when a receiver is just, like, stands in a trench coat.
And there's, like, a bunch of levels of indirection.
Just generally, like, building custom receivers is not an intuitive experience at this point.
**tristan** 40:12 I guess most… the experience at Gruk is receivers, no…
Touching processors and exporters, so they might also be similar, but…
**akasprzok** 40:22 Yeah, but mostly what I run into is, wouldn't it be nice if we could just make this a receiver?
**tristan** 40:28 Yeah.
**akasprzok** 40:29 And so that is, like, why we end up going to having more containers in the same pod as OpenTelemetry Collector. If it was something that we could more easily build and maintain ourselves, then we.
**tristan** 40:43 We'd be more invested in the ecosystem.
Gotcha.
Is there… Are there any…
Tips for people reading this who are getting up and running with the collector, so…
**akasprzok** 41:03 Let me think about that one for a second.
Ugh…
Don't be afraid of… Running your own distro.
that is generally just such a big boost in knowledge and understanding of how the OpenTelemetry Collector works.
That, even if you're… not…
writing, like, custom receivers, etc.
just, like, the knowledge gain itself, I think, is worth it.
Also, Huck Puck's Metrics to Attributes Processor, if you're using a tracing provider like Honeycomb, is a huge value add, and I would check that one out.
**tristan** 42:09 Which is it?
**akasprzok** 42:10 Puck Puck, let me, pick out your link.
Lets you take metrics out of your metrics pipeline and attach them to span attributes.
**tristan** 42:26 Oh…
**akasprzok** 42:27 to… to Traces, and, it's fantastic.
**tristan** 42:33 Very nice, okay.
**akasprzok** 42:35 So, you know, just like, when I, when I'm…
if I'm running… When I was, when I decided to, go to a, to
roll Grok's own distro, and go off of just, like, the Open Synergy Collector Contro.
Part of that was so that I could use some processes that other people had written, such as this one.
Edward and, you know, OpenTelemetry Collective concept.
**tristan** 43:12 Interesting.
Buck Puck looks familiar, but I didn't.
**akasprzok** 43:15 Yeah, he's, he's at Hankum.
**tristan** 43:19 Yeah, I thought I knew him from somewhere else, but now, yeah, maybe it is just a hotel in Honeycomb.
**akasprzok** 43:25 Other than that, the header extension can be really freaking useful. If you have certain,
For example, we have some use cases for logs.
Where we want to,
where we want the client to be able to pass through which stream fields are important. So, like, in Victoria metrics, Victoria logs, it's kind of like the fields that should be indexed for a given log stream. And you can just very easily do that with, like, the header extension.
Just have the client send those headers, pass them all the way through to the end,
And there's a… there's a bunch of other neat tricks like that that you can do, like, passing, like, org ID for tempo, things like that, just all the way through. And that makes your OpenTelemmetry Collector more…
Flexible by shifting, some of that configuration left.
**tristan** 44:34 Oops.
Right.
Yeah, I think that's… covers…
Everything we had that we want to cover for the blog post.
Okay.
Do you have anything else you'd like to add?
**akasprzok** 45:01 We talked about a bunch of stuff…
Yeah, I think the… the interesting parts here is the…
Just, like, running all those containers alongside in the same pod. Running kubestate metrics, pods,
For… for sharding, because if you have, like, a big,
if you have a big cluster that has, like, 2,500 nodes, you know, you want CubeSat metrics, but if you try to have just, like, a CubeSat metrics pod that grabs
Metrics for all the pods.
Like, you can't scale that.
There's too many of them, so, sharding that out, they have, they have that in the CubeState Metrics README. I think it's just, like, such a good fit to just chuck that into the OpenTelemetry Collector dataset. Let me find that.
**tristan** 46:01 Yeah, that'd be great.
**akasprzok** 46:22 Yeah, there it is. Damon said sharding for pod metrics.
I'll have that here, too.
easiest way to… to scale to, like, one of the… one of the… the challenges that… that I face is that,
Okay, cool. I want to treat… I want to treat all these data centers like cattle.
But they are all different sizes. Like, one of them might have 800 nodes, another one might have 2,500 nodes. So having something… like, so having a lot of auto-scaling components is vital, and…
**tristan** 47:02 What better way…
**akasprzok** 47:04 To shift as much of the metrics collection that is specific to a node, like the pod metrics on that node, than to just, like, stuff as much as possible in the dataset.
**tristan** 47:17 Yeah, yeah.
Baiting having this one go next, because it kind of shows… the Mastodon is also a team of one.
Running there.
Oh, yeah?
And then… but they're a much smaller deployments, so it kind of shows, like, here's what you can do with.
**akasprzok** 47:49 One person maintaining it. Oh, and also, here's what you could do.
**tristan** 47:54 Oh, look at this.
**akasprzok** 47:56 But this is good timing, because I have somebody else start on Monday, so this is the last chance that I get to brag about doing this all by myself.
**tristan** 48:04 Yeah, I'll get it out quick then.
Alright, cool.
Yeah, thanks for the links in the doc, and the doc, that's gonna be very helpful. I'm sure I'll have some pings for you.
**akasprzok** 48:22 Things, and they might have some questions for me, yeah.
Yeah, I'm happy to follow up.
**tristan** 48:30 Oh.
Alright.
**akasprzok** 48:31 Cool. You wanna stop the recording and, stay on for a minute?
**tristan** 48:35 Yee, if I can do that.
I might not actually have permission to do that.
**akasprzok** 48:42 Okay.
**tristan** 48:44 I'm clicking the recording button, and it's not doing.
**akasprzok** 48:47 Alright.
**tristan** 48:49 I can't do that.
**akasprzok** 48:49 I'll just catch up with you later, then.
**tristan** 48:51 Okay. Sounds good. Thanks, man.
**akasprzok** 48:53 Later. Later.
**tristan** 48:54 But…
