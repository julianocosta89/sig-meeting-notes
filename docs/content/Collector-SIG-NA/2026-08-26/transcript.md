SIG: Collector SIG (NA)
Date: 2026-08-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Pablo Baeyens 00:04:17 Yeah, let's get started, I guess.
I can… To the owners, unless somebody else wants to?
Drive this?
So, in terms of… Priority issues… I think we've got an agreement on the Kubernetes Attributes Processor, I don't know, Tyler, maybe you could summarize that?
Tyler Helmuth 00:04:50 So we're going to… In the next release… Before tagging 1.0, we're gonna follow the existing deprecation process and remove the… Already deprecated config field, and that's gonna be a breaking change.
We also plan to, promote the… internal telemetry… Feature gate in the next release.
And those will just be normal braking changes that we would do for any component that's going through a braking change for forced stability.
And then in the release after, we will tag… 1.0, and in that 1.0 release, we will switch the feature gate for the… SEMCOM version of the attributes that the processor creates.
So on the… there will be some… a few littler breaking changes in this next release that are not tagged 1.0, and then the 1.0 release will have the big Special tag, and with it will come the big, impactful semantic intervention breaking pages.
Pablo Baeyens 00:06:05 Okay, cool.
Then I think there was… a PR for the host metrics receiver process paper?
Let me see if I can find that… Yeah, so it is… this one.
on… Yeah, I don't know of any other… if there's anything worth mentioning about Prometheus, or… Any other component? Yeah, Mikola?
Mikołaj Świątek 00:06:54 Sorry, I thought… I thought you were done. After we're done with the components, I just want to talk briefly about config.HTP, but if you're not, then please continue.
Pablo Baeyens 00:07:05 Yeah, I'm done. Go ahead, and if somebody has something to say about another component, they can raise their hand.
Mikołaj Świątek 00:07:12 I do have something to say about Prometheus, and I keep repeating that, in that component, once it becomes stable, quote-unquote.
we'll just have to, I think, adopt.
versioning after Prometheus itself, and stop pretending that it's actually stable, because it's not really. It just accepts Prometheus configuration, and whatever Prometheus that a given version accepts, it also accepts. So it's not really up to us.
I think we should be.
clear.
About this contract.
Arthur, it looks like he only says something?
Arthur Sens 00:07:52 Just saying hi after a very long time, not… Joining, and Yeah, I'm happy to discuss this. I feel like I'm a little bit out of context.
But, if discussion is needed, I'm happy to discuss.
Mikołaj Świątek 00:08:12 We can adopt a…
Arthur Sens 00:08:14 Collector.
Mikołaj Świątek 00:08:14 Yeah.
Yeah, I mean, basically, it's just that we can't really say debit stable.
Because OpenTelemetry can't say that it's stable, or it's, like, the owners of the component can say that it's stable, because it's… it's not up to us, in effect, right? We support some version of… we, like, have some version of Prometheus pinned in the component, and that's exactly what it accepts. Prometheus itself is largely quite stable, right? But nonetheless, if Prometheus wanted to do a breaking change, then there would also be a breaking change in this component.
In effect, right?
Arthur Sens 00:08:52 Yeah, but, the contract that Prometheus have is also against breaking changes, right? So if Prometheus decides to break, it requires a 4.0 And we can… We can choose when to adopt 4.0.
Mikołaj Świątek 00:09:07 Yeah, I mean, what I'm saying is that it makes sense to say the component version is, like.
aligned with the versioning Prometheus has, so it's clear.
Because if we say it, call it 1.0, that doesn't help anyone with anything, right? If we call it 3.13, 14 it's Prometheus is right now on, right? If we say that, then it's pretty clear what we're promising.
Arthur Sens 00:09:34 Yeah, yeah, I see, I see. Maybe we can, we can have a, like, a matrix.
end up with me saying, like, with version of the receiver, and version of the Prometheus.
That, like, yeah, I think you understood what I meant.
Mikołaj Świątek 00:09:51 Yeah, yeah. But that's, you know, we can move it, we can move it to the issue. That doesn't… that doesn't stop… calling the components label, I think. It just, like, means that we have to be careful about what we do with it afterwards.
So that's one thing. The other thing is that… As far as I'm aware, there's no more blockers for declaring config HTTP stable, so I am planning to do just that, if anyone here knows of.
Any of those, then, you know… This is your last chance. This is your last chance to make yourself heard. I'm gonna put the issue here under the agenda in a second.
And that's it.
Pablo Baeyens 00:10:42 Okay, I guess we can move to… heaven, then.
Evan Bradley 00:10:51 Cool, thank you. So, this one's mostly for Israel, but, I'd be welcoming to any other kind of input from the community.
Basically, the short of it is that I'm doing some service discovery sort of processing, that I want to do in the Collector. I'm gonna do the important bits in the transform processor, but in order to kind of tee that up.
we need to group, so what we're doing here is you have a bunch of spans coming in for a trace. A lot of those spans are going to be local to a specific service, so, you know, like a single OTel SDK within an app that's emitting these spans.
And we want to… move spans from child spans to the root span within a service. So, to do this easily in the transform processor, we need to group it by trace, which works, but the problem is that, there's also concerns that we're gonna have extremely large traces, like 10,000 or more spans.
So, I'd like to make it, since I'm just doing kind of a service discovery sort of, Processing, app, or whatever you want to call it here, I feel like it'd be easier just to admit, like, the sub-traces. So basically, all of a single service's spans come in, we wait some predetermined amount of time that's less than for the overall distributed trace, and then admit just that, service. And so I'm… or I just wanted to present this to see if this is, like, does this make sense? Is there an approach I've missed here?
Just what do you think?
I think, Israel, you're in the meeting, right?
Israel Blancas 00:12:46 Yo, yo.
Evan Bradley 00:12:47 looking for your feedback. Okay.
Israel Blancas 00:12:49 Yeah, I was… I was thinking. I had to look a little bit more deeply into this, but yeah, if you… thing, it's a good feature, I will go with it. I mean… Yeah. I don't know any other way of doing… What you need to do, to be honest.
Oh, yeah.
Yeah, yeah, so yeah, feel free to send a PR, and we can… We can guess the best way to have it done.
Evan Bradley 00:13:21 Cool, thank you.
Okay, in that case, if nobody else has any input, Blake, you're next.
Blake Rouse 00:13:35 Oh yeah, I just brought this up on, I think, the last SIG I was on, about the export helper change for retrial and failure, and there were some questions about whether it was needed, and I went back and looked at it some more, and it does happen, even on a standard shutdown, because The exporter will get, like, a context cancel and propagate that back up.
And it results in the events being lost, so… I just wanted to bring it up here, just because we had talked about it before in there.
I think we were waiting on someone else to… review and look at the issue, and that hasn't been done yet, so I don't know who that is, but, Yeah, that was it. Just, information about, something we had talked about before, just to kind of circle back on it.
That's it. Raleigh, you wanna go?
Evan Bradley 00:15:25 I'm not able to hear you if you're talking.
Blake Rouse 00:15:31 Yeah, I didn't know if that was me, or… I was trying to check my computer there for a second.
Ravishankar 00:15:37 Oh, hello?
Evan Bradley 00:15:39 Now we can hear you.
Ravishankar 00:15:41 Yeah, sorry, my bad. Yeah, mine is more like I brought up in the earlier sequels, which is just a PR review, which has a couple of approvals as well, so… maybe Ivan or anyone who has… how much access wanted to take a look, and we can go ahead for the merch, yeah.
Evan Bradley 00:16:04 Yep, I'm sorry, these are on my list. I haven't been able to look at them yet, but I did see your ping yesterday, and they're, I'm gonna try and take a look as soon as I can.
Ravishankar 00:16:14 Yeah, sure.
krajo (Grafana Labs) 00:16:27 I guess it's my turn now, right?
Yeah, so… Yeah, my name is Djerd Krajovic, but everybody calls me krajo, for obvious reasons.
And, I've applied to be a triager.
And, I've been at Grafon for, like, 5 years, I'm… Prometus maintainer and a Mimir maintainer. Mostly, I've been active in the Prometus SIG.
Or Prometus interoperability SIG to be precise.
And, but recently, my… I agreed with my boss that I'm spending more time on OpenPantry, meaning that basically all my Monday is open territory.
And then I get every day, like, 90 minutes to triage and do OSS work beside project work. Although a lot of my projects are actually related to OSS anyway.
So what I'm saying is that I have a bit more time, and I'd like to move up, so… I asked for a PR to make me a triager, and I… Hope to forward or advance the project.
Stuart Buckingham 00:17:43 I'll go next. I came to this call a few months ago, with a proposal about Making dynamic telemetry syncs. A, we want to be able to route telemetry to different, consumers.
dynamically, and do that without having to rewrite the config all the time. I know that recently there's been some work on dynamic config reloading, but we still want to use objects defined in etcd and Kubernetes to be able to say, okay, route This sort of telemetry to, a certain consumer, whether it's a hosted platform or something else that's defined in the cluster. Paulo put in a PR yesterday that enables the observer to be extended beyond just the Kubernetes primitives.
That we currently use for the receiver creator.
I did want to propose an exporter creator that mirrors the receiver creator.
pattern. But we can also use, custom resources or anything else that the observer could potentially observe, to create those syncs.
I think last time I proposed this, it was seen as a bit of an anti-pattern, in that we should have dedicated resources and route this through the operator, to create those destination targets.
I think that… That is a good pattern, but, limiting people to having to do it that way also seems like it's a little bit against the goals here, which is the, in my mind, the Swiss Army knife.
That does anything you want to do with telemetry. So, really wanted to open this up for discussion and see what, thoughts were, so that I could, focus our efforts here.
Blake Rouse 00:19:57 Yeah, I'll go. So for dynamic routing of… to the exporter, I mean, the graph is built, right, with chaining of functions.
So how do you expect for this to… actually work.
Stuart Buckingham 00:20:13 Yeah, I think the most simple implementation would be, like, all of the telemetry is sent to every single one of the exporters that gets dynamically generated. The routing layer on top of that isn't something that's a hard requirement for us, but something that I do want to solve in the future as well.
Blake Rouse 00:20:35 So, in your mind.
Exporter creator is the exporter, and then nested underneath Export Creator is the exporters, and you're doing the routing at that layer, not in the graph.
Stuart Buckingham 00:20:47 Yeah, sort of just trying to use the pattern that the receiver creator has already, rather than trying to reinvent a lot of components all at once.
Blake Rouse 00:21:02 Okay, Mikola.
Mikołaj Świątek 00:21:05 Do… Are your… do your ex… are your exporters homogeneous, or do you have, like… does this routing have to work across different exporter types?
Stuart Buckingham 00:21:17 Yeah, ideally, we just want to support Prometheus Remote, right, and OTLP as day one.
And that's sort of what we've been able to hack together, but we've moved quite far. You know, we've invented a bunch of components, and until, Paulo's PR yesterday, we sort of had to reinvent the, the whole observers.
Because it wasn't extensible.
But those were the two that are the hard requirements, but ideally, like, this shouldn't be limited to just… it only works for this like, one or two exporters. It should be… able.
Mikołaj Świątek 00:21:57 No, no, what I mean is more like… Does your routing have to be able to go into, like, completely, like… I… if so, we go to OTLP exporter, in a different branch, we go to a different exporter. Because if it's always the same exporter.
and you just… the destinations are different, is the destinations which are dynamic, then there might be a much simpler solution to this. Because in principle, there's nothing stopping anyone from, like, just sticking the URL or destination that you want in an attribute, and then having some exporter-agnostic component for exporters which support this kind of thing to… to just send it to that URL. Like, this is probably not so… not that… easy in practice, I would say, but this… this basic mechanism, I think, is much simpler than actually spawning a full exporter for everything, because if you spawn a full exporter for everything, you suddenly have to think about… but what about queues? What about retries, right? There's a lot of complexity that comes in, and you pay a certain fixed cost for each of them that you have. Like, receiver creator In comparison was more or less created to less… less to just kind of, in a general sense, spawn more exporters, and more in general to kind of respond to a situation where you are kind of, like, you're on a host, and you see, oh, here we've started Redis, so we can spawn a Redis receiver of some sort, right, to automatically react to that event.
But those are events that don't happen very often, and you might have a lot of destinations, potentially, right?
So it's kind of a waste to… to spawn an exporter per destination. I haven't looked into this in detail, but that's kind of my immediate reaction to this problem. Like, if your problem can be scoped to just destinations, then maybe it might have a simpler solution.
Stuart Buckingham 00:23:58 Yeah, and I think it's really up to the person implementing to also see, like, okay, should you have different, collector instances that manage each of the different, exporter destinations, so that they can each manage their own queues in a sandbox, then one doesn't take down the other. But right now, there's none of that… None of the tools in the toolbox that would allow you to do that either.
So, like, if you wanted to have 5 different Prometheus Remote Write exporters, maybe you'd have 5 different instances, and then have just the sort of central collector that routes to all 5 of those, and then they can manage their queues and their memory assignments and things independently, and not take down each other.
But in terms of just being able to send, or being able to… yeah, relay the telemetry to those other five child, collectors. That's not really possible right now without having something like this in the plumbing. Yeah, Blake?
Blake Rouse 00:25:19 I mean, I would say the only weird thing with this is that it's… And I guess it's the same thing with receiver creator, so I don't know if it's necessarily wrong, but I would say the weird thing with this is that it's only for the exporters, it's not… like, pro- you can't, like, put processors on top of it, or anything like that. So, like, because, like, you're gonna have a receiver creators with dynamically create receivers, exporter creator, dynamic creator, exporters. Then the next thing you know, people are like, well, can I dynamically create processors?
Stuart Buckingham 00:25:44 And then now…
Blake Rouse 00:25:44 Now you have this whole thing of, like, should we have actually stepped back and looked at this from a higher level, and said what we really needed was a dynamic way of creating configuration?
Instead of this, I need, you know, something here, something here, something here.
When we're working towards partial reload, and partial reload will enable these things, if we could somehow bring this up another level before configuration, and say, we can dynamically just config… dynamically just create configuration, and the graph knows how to handle it, instead of doing this one piece where, like, you have an exporter, but really it's not an exporter because you have sub-exporters underneath that exporter, and that just gets kind of… confusing, so that's kind of my take on it at the moment, like, where my head is at on this, is that… it's right, I think you're right, like, this, like, aspect of, like, dynamic… configuration, which is something that, you know, holds near to me as I'm trying to get the partial reload work in. But, It just feels like… this is not the right solution. Like, maybe we need to take a step back and look at it overall for dynamic config.
Instead of saying, let's… let's do what Receiver Creator did, because we got that approved, and we got that in, you know what I'm saying?
Stuart Buckingham 00:27:03 Yeah, no, I totally agree, and I think, someone, Harrison, a few weeks back, came back with something similar about, like, enabling multi-tenancy pipelines that, are defined outside of just, like, static config. I just see that as, like, a huge leap.
technological risk of having to go and change a lot of the architecture, and this is sort of a smaller, maybe more palatable Step in that direction.
Because that seems like a huge architectural change.
I don't know.
Blake Rouse 00:27:42 This is such a huge change. I think overall partial reload is a large change, and that's something that RFC's approved and we're working towards.
But I think the ability to dynamically adjust configuration in process builds on top of that, where necessarily where those building blocks are already there, so it's not necessarily a large change. It's just how do we connect the dots, right? How do we connect your etcd configuration to that dynamic reload. I think what you were saying is, is right now, people are saying that's coming in from, like, the Collector supervisor, and that's not something that you like. I mean, I think there's a discussion had there about whether that is wrong.
Because the supervisor has functionality that you just will never get in process, like hard failures, crashes, panics, things like that that you just can't recover from, where… Having a supervisor, you get those benefits. So.
Stuart Buckingham 00:28:33 Yeah.
Blake Rouse 00:28:33 I don't know if, that… Probably not the answer you were looking for, but that's just kind of, like, where I am at the moment.
Stuart Buckingham 00:28:43 Yeah, I think you're right, like, it is the purview of the operator to sort of do that next level up routing and do all of that logic. I also think that the… A lot of people, you know, it's quite a big… step to adopt the hotel Collector, and then to tell them, oh, actually, for this additional functionality, you need to Change a lot of what you're deploying to the operator and then use a whole different package might be a bit of a blocker for some people in adoption.
Blake Rouse 00:29:21 Well, that might be true. I mean, that might bring up just a different question. It's the question really that the supervisor should be something that's built into the Collector, and the Collector just knows how to spawn as supervisor mode and spawn a Collector sub-process automatically under it, would be a different story. Where you're bringing… In this… you're giving the benefits to the user without them really having to do a lot of extra work to get them.
Might be something more to look at in that regard.
Stuart Buckingham 00:29:49 Right. I know as well for Al, application in particular, like, having… dynamic, letting… The operator dynamically create pods or create instances, sort of is unbounded in that we don't know how many things will end up being run, especially if these you know, the destination, syncs are being dynamically created by end users. You end up with, like, an unbounded set of, oh, okay, someone could just Add 100 different configurations, and it spawns 100 different collectors, whereas if you have it Sandbox inside the Collector, you know that you're always running one instance.
Blake Rouse 00:30:37 No, I'm not saying you would get multiple collectors. You would just get one collector, but it would be orchestrated basically through OpAMP to change the configuration of that collector dynamically. Does that make sense?
Stuart Buckingham 00:30:49 this afternoon.
Blake Rouse 00:30:49 I'm talking about the supervisor, I'm not talking about the… Or.
Paulo Janotti 00:30:53 Okay. One thing about the… and I think the configuration is kind of the higher level, destination, I, I, I really think, that, but… One thing that is that the observer brings right now is that you deploy the config, and you are saying what you're gonna watch.
If you're gonna do that outside, you have to feed in some way of configuration to deploy the watchers, you know?
In a sense… and it could be a fair assessment, saying, hey, this should be out of the Collector. That could be a fair assessment. But, On the other hand, that's what we have today with the observers, and just talking about updating the configuration, then we still have to solve that problem. You know, who is listening and watching for the change?
Stuart Buckingham 00:31:54 Right.
I thought that was the PR that you put in there, was to.
Paulo Janotti 00:32:00 Yeah.
Stuart Buckingham 00:32:01 And that… that observer functionality to Not be limited to the…
Paulo Janotti 00:32:07 Because, to be fair, I have a case for a receiver that needs a different, observer, and I could hard code that, hard code. I could make a hack to use, I don't know, a container type.
Stuart Buckingham 00:32:22 But…
Paulo Janotti 00:32:24 Doesn't make sense, right? I'm observing different stuff.
But to Blake's comment, because I really like the idea, kind of, hey, this is a configuration change. We have a new exporter, we have a new receiver, and we update the configuration without the full reload, with the partial reload.
But on the other hand, I'm still thinking about the question, who is doing the observation to trigger the change, you know? And right now, it's in the collector that capability.
When we go to this scenario that is the… the… the full config, then I… I have the question, how we are doing that observation to trigger, those. Where… where the observers are gonna live, you know? And if you think, and… and once more, I'm not saying against that, I'm just saying that this is a capability that the collector has right now, to have these observers to create the receivers.
I… I… I think when we talk about having the solution, as up to date, the configuration, I think really that is kind of the… the… more long-term goal, I think that makes a lot of sense. But on the other hand, I'm still with the question that even if we do that, we have to answer this question about Because right now, we configure who is gonna observe from the collector.
If we're really thinking long-term, and we want to separate that, then we want to have some other means of doing that observation without breaking and dropping that feature.
Stuart Buckingham 00:34:17 Yeah, one other sort of challenge that's come about is that dynamically… Templating and maintaining the configuration.
Is quite difficult, in that we have functions that generate configuration And we're moving towards a point where the… there isn't a single service that may own that. You know, customers might be able to, specify their own Like, destination sync for telemetry from multiple different surfaces, and… having that in etcd solves a lot of those problems, where, you know, each resource can have an ownership property and can only be mutated by a certain service, and so you can end up with destinations being written by different things and combined with the watcher to produce, like, a graph in real time. Whereas if you have to generate the configuration from a single service, you either need to write something that's going to watch for all of those resources and combine that And then, sort of the life cycle around that gets a little bit difficult, in that, I guess you can have, like, a watcher that watches for specific custom resource, and then generates that stuff on the fly, but it's adding a second Link in the chain that could be solved by just having the observer watch for those destinations, or in the receiver side, maybe watch for those receivers dynamically?
Yeah, Dakota?
Dakota Paasman 00:36:02 Hi. I just want to interject on the topic about, config watching and configuration management.
At BindPlan, we have an internal extension component that we've been using.
That implements an OpAM client, and effectively is Similar to the supervisor, in that it manages the collector, or manages its configuration, and allows dynamic configuration rendering from an op-amp server.
I know this is something that we've talked about internally a little bit, about possibly donating upstream, and it sounds like This kind of topic of… Config management.
dynamic config management comes up a decent amount in this SIG.
So I think that's something that I can talk to the wider team about.
And potentially propose to the community, as a potential solution for… This general problem of configuration management. You know, I think it was Blake who, suggested, you know, something that manages a collector process, and that's pretty much what this extension does. It spawns off the Collector process, and… connects to the op-amp server and, you know, waits for Config updates and applies them to the Collector process it's running.
So if there's general interest in that, I think that's something that… we can… Give the community.
Stuart Buckingham 00:37:40 Sure. I'll try and find… are you on, the CNCF Slack? I'll see if I can reach.
Dakota Paasman 00:37:45 Yeah.
Stuart Buckingham 00:37:46 That'd be great. Thanks.
Cool. I'll, leave it to the next person.
Blake Rouse 00:37:58 If I'm… if I'm wrong, though, real quick, isn't there… there's already a supervisor…
Dakota Paasman 00:38:03 There is.
There is. It would be, like, an alternative to using a supervisor. The supervisor… has its own set of benefits that it provides that, you know, same process extension won't be able to provide, like, like a watchdog behavior and being able to restart the collector if it's failing.
But it is… Better, you know.
Blake Rouse 00:38:30 So you're… so, just, I'm just trying to understand, the extension you're talking about runs in process, it's not two processes.
Dakota Paasman 00:38:36 Yeah, correct. It's one process. It just… Yeah, yep.
So it simplifies the deployment challenge of, you know, it's still just a single collector that a user is deploying, and they're just configuring this extension, rather than needing to deploy the supervisor.
And the Collector as well.
Blake Rouse 00:38:59 Okay.
Arthur Sens 00:39:25 Should we move on to the next one?
Stuart Buckingham 00:39:28 Yeah, thank you.
Arthur Sens 00:39:30 Right, my topic is about an issue that Alex created.
to proposing a new collector distribution that includes Prometheus exporters as, as Collector receivers.
I'm wondering… Like, we already put a lot of details on the issue, but, Maybe we should be discussing this here as well.
If we have any maintainers here.
Pablo Baeyens 00:40:04 Yeah, I think one thing that maybe we need to clarify is the… this requirement for all components to live on the OpenTeometry org, we should either rephrase that to be CNCF projects are allowed, or… Think about moving components.
Tyler Helmuth 00:40:23 Yeah, we can update that language. I do want to call out that there is a precedence for not following that already, in our upstreamed OTEL EBPF, We have a component that doesn't live in our repos, but we are including it. It's not quite.
Pablo Baeyens 00:40:42 But that one…
Tyler Helmuth 00:40:42 Prometheus, because, yeah, because Prometheus is in a literally other org-org?
So yeah, I think we'd have to update that language.
Arthur Sens 00:40:51 But, but,
Pablo Baeyens 00:40:51 Right, yeah.
Arthur Sens 00:40:53 that we don't need if it's not needed. Like, the… Oh, I think it's what… One thing is important to understand. There is the Prometheus exporter who lives in the Prometheus org.
And we are refactoring the exporter so they are usable as Go libraries.
And then there is a separate project which provides a Go module that implements the receiver interfaces using the exporter's Go libraries to implement them.
So this module that implements the receiver if needed, I can move this module alone to the hotel collect… to the hotel organization.
And the exporters can live in the Prometheus org just as code libraries.
Pablo Baeyens 00:41:45 I personally like the idea of this living on the Prometheus org, and setting that precedent that for… at least for other large open source projects, we will Alto, but I don't know what other people think.
Arthur Sens 00:42:03 Yeah, I'm happy, I'm happy with this change. I really like the idea of, like.
fostering collaboration with other CNCF projects, and I think this is a good, Yeah, permissions receiver. I mean, well, we already have a permissions receiver.
But yeah, I think this is a good move to foster this kind of collaboration.
There's one… Unsolved problem as well is, the release process For the Collector today, releases all distributions together, and they all… they are all versioned together.
And the release process, when you release Hotel Core.
we automatically have PRs updating the modules in the contrib.
If the… these modules, with including the Prometus exporters, are in the Prometheus org.
how would that automation work? We release Core, we open PRs to Prometheus.
we have… we… we give Prometheus… Collector maintainers access to the Prometheus repository, I don't know, like, this sounds a little bit sketchy.
Pablo Baeyens 00:43:22 What dependencies do the Prometheus? Like, on what modules do we depend? Are those modules one point something?
Arthur Sens 00:43:32 I… I can… I… definitely the component… The component module, the receiver module.
I don't remember all of them, I can double-check.
Pablo Baeyens 00:43:46 Yeah, I think if they are one point something, it shouldn't be an issue. We don't even need to necessarily update those on… on the Prometheus side.
I mean, ideally, we… we validate that they work together, but,
Arthur Sens 00:44:02 Yeah, it's component, component tasks, consumer, consumer test, receiver, receiver tasks.
Component tests and receiver tests are not 1.0 yet.
Pablo Baeyens 00:44:15 But those are supposed to be only used in tests, so, I think we…
Arthur Sens 00:44:20 Yes.
Pablo Baeyens 00:44:21 should be fine.
Arthur Sens 00:44:25 Yeah, if we don't care about that, that's fine.
Pablo Baeyens 00:44:30 I mean, again, speaking for myself, but I don't think it's a problem if it only relies on one point something modules, because, We shouldn't make breaking changes on those.
Arthur Sens 00:44:40 Okay.
Cool, then we can keep this in Prometheus.
The other question…
Pablo Baeyens 00:44:48 I guess… Sorry, before we… on that front, I guess.
we should open up ER to update those rules, and get it formally approved.
Arthur Sens 00:45:00 Yeah, fair, I can open it, yeah.
Tyler Helmuth 00:45:03 I,
Pablo Baeyens 00:45:03 Okay.
Tyler Helmuth 00:45:04 On that topic, should we… Do you want to open it up to all of CNCF right now? Or, since we already have such a close relationship with Prometheus since the beginning of the project.
Is it better to stay specific and say OpenTelemetry org and Prometheus Org, and not try to… I'm a little bit worried if we open it to all of CNCF, we're gonna start getting a lot of requests that we aren't actually interested in taking.
Pablo Baeyens 00:45:33 I mean, adding all of CNCF doesn't mean we need to accept… like, we still will analyze things on a case-by-case basis, right? I don't know.
Oh.
I don't feel like that's a big concern for me, but I don't know.
Arthur Sens 00:45:48 If you want to be more restrictive, you can choose, like, graduated, since you have projects, or incubated.
Sentbox is where you have, like, hundreds of… projects.
Tyler Helmuth 00:46:02 I like… I like… that's a good compromise. Let's… let's use those terms. Let's go with graduated and… and, Incubating, I think.
Arthur Sens 00:46:15 Okay.
The other question that I had is, Regarding, do we recommend this distribution in production? Honestly, I do not.
with… for the same problem as Contrib, I don't recommend people using contrib, since it's, like, a catch-all.
And we are gonna do the same thing with this, like, we're catching all Prometus exporters in one distribution.
I… for production usage, I do recommend people to cherry-pick the components and build their own with OCB.
So I was wondering if… if we are… If we are doing two distributions that we do not recommend.
Why not just keep it simple and having everything in the contribute?
Tyler Helmuth 00:47:09 It seems likely that this will be a short-ish-lived contribution, or distribution… short-ish-lived distribution anyways, because I imagine if this If we do this, and it goes over really well, and, like, the integration is seamless, and people love it, that there's going to be… exporters that we want to put into the KH distribution, for example, that would run on Kubernetes.
So, it feels okay to say that it's not recommended for prod now, only in the sense that this is, like.
a new integration that we are trialing, but as it matures, I think We'll either move things into Contra or move… individual components into distributions that we do recommend for production. Or we'll turn it into a A production-ready distribution itself.
People will use it in production regardless of what we say, so the stance is really all about us being able to say, hey, you shouldn't have done that, in… Trying to cover ourselves.
Arthur Sens 00:48:09 Alright.
Tyler Helmuth 00:48:12 It also helps with our, like, support guarantees.
Arthur Sens 00:48:17 Yeah, I'm also thinking… like… Yeah, Joshua put in the comment, like, does receiver apply relabeling rules just like ordinary receiver? No, it doesn't.
So, to get, like, a premises exporter that's actually usable, you need the processors, like OTTL, all the things that are in Contrib.
So, the Prometheus distribution would not be useful without several contrib… Components as well.
Tyler Helmuth 00:48:55 It's okay to… it's definitely okay for us to build a distribution that, like, Has dependencies in it.
like, if this… if, like, a particular exporter should never be used in the Collector without the transform processor, or the metrics transform processor, or the CA attributes processor, or something, like, it's okay. They're curated distributions.
On purpose, so that we can help take away that, like.
A user would have to know to do that.
So I think that's fine.
Arthur Sens 00:49:27 Alright.
Yeah, sounds good to me. Alright, I'll… I'll work on… all the things we discussed. Thanks.
Mikołaj Świątek 00:49:48 Right, now the final item is also mine.
So this concerns this bit of logic that we have in Contrib.
Where we try to determine what is the status of a pipeline based on the status… statuses of the components in this pipeline.
And up until now, the logic went roughly like this. If any components in error.
Status is an error. And then we go… if all the statuses are okay, and the status is okay, if all the statuses are stopped, the status is stopped.
And if there's some mix, then the status is stopping, because we assume that we're in the middle of shutting everything down. And this used to be true, where there wasn't partial config reload, and you always tore everything down, but it is not true anymore.
So, what I'm proposing in that issue is that, essentially, this logic should change, and the way it should work is that if there's any components at all with status OK in a pipeline, then the status should just be okay.
And then it can be stopped later until after everything actually stops.
And… Yeah, yeah, Evan, I'm sorry. I'm asking for your opinion.
Evan Bradley 00:51:08 No, it's alright. I was gonna ask, does that mean we never have stopping?
Mikołaj Świątek 00:51:14 On a pipeline level, we might have it. If everything is stopped or stopping, then I guess we could have stopping at the pipeline level. I'm not sure if this is a problem or not.
It's hard to tell what is actually stopping or not, if, like, components are allowed to be, you know, I… I guess… I guess we could have some kind of more clever heuristic, which says something like, you know, it's a pipeline.
So, if you can… if there's, like, a line of okay components through it, then… then it's okay, otherwise it's stopping, but I don't know if, like, the… complexity of that is actually worth trying to do it. I'm not sure if anyone actually cares about seeing pipeline… their pipeline and state stopping.
Evan Bradley 00:52:03 That's fair. I think okay and stopped are much more important.
I'd be… yeah, I would be okay with that, personally. I mean, I'd welcome others' opinions who might have used this a little bit more.
Blake, I see your hands up.
Blake Rouse 00:52:20 Yeah, I would say that I think… I mean, I think you want to see it, but to me, it's almost that, like.
the instance that it's gone also means it's stopped, so, like, I don't know if we necessarily could just… Clean up from the stopped status.
Instead of letting it linger.
Mikołaj Świątek 00:52:43 That's honestly also kind of a thing in court that's, I think, not completely resolved right now.
Where… If you stop a component, it's gonna be stopped forever.
That's probably something that we need to figure out in CORP.
Rather than… rather than do it in this data segregation. Because it is also, like.
There isn't really anything in the model, in the status reporting model, that tells you… what should happen after you emit a stopped status. In principle, you emit stopped, and that's it. So you could remove it in the status. But, like, the difference between having emitted stopped and reporting stopped and just not there is, in this case, like.
not very ba… it's something that exists in the sense that You omit the stopped, so somebody can actually see the event wherever you're sending it, but in terms of just the whole pipeline as it exists right now, there isn't really any difference between stopped and non-existent.
Next stop is essentially something that existed in the past and doesn't exist anymore, if you just look at snapshots.
That's right, Tyler.
Tyler Helmuth 00:54:07 Is the aggregation level… like, what's the aggregation that's getting rolled up to here? Is it… Is this all talking about a component, a pipeline, or the entire status of the collector?
Mikołaj Świątek 00:54:18 Right now, I'm talking about pipeline based on components. Like, in core, only components have statuses.
Tyler Helmuth 00:54:25 Okay.
Mikołaj Świątek 00:54:25 And in contribib, we want to say what the status of a pipeline is, based on the statuses of the components in it.
Tyler Helmuth 00:54:31 Okay.
Mikołaj Świątek 00:54:33 Then there's also the question of what the status of the whole collector is based on this. Maybe there's something to be fixed in there, too. Do we even report the status of the whole Collector based on this way? I don't even… I'm not even aware.
Tyler Helmuth 00:54:49 I'm not sure.
For the individual pipeline for this question, though, if you're… if we're rolling up the status of a pipeline.
And let's say… The receiver is stopped, and all of the other components are okay.
Is the proposal that that pipeline report okay?
Mikołaj Świątek 00:55:09 more stuff. Yes.
You know, it's…
Blake Rouse 00:55:12 I'm not interfering.
Mikołaj Świątek 00:55:13 It's okay. It's okay.
You could have some kind of… You could have a special case, right? Because it's a question of, are there any receivers in this pipeline that are okay, right? You could ask a question, you could ask, are there any exporters that are okay?
But… I guess I'm…
Tyler Helmuth 00:55:36 Like, an individual pipeline… And maybe this is too complex, and… And we don't have the heuristic for this yet, but, like.
if I'm thinking about the status okay, maybe all the processors and exporters are okay, but if I have no way to get data to that pipeline, it doesn't seem like that pipeline is okay.
Unless stopped is, like, a known… healthy state that you might purposely want to be in. Like, it's not errored, right? It's not like all of my receivers have erred. So I guess that's… I… Is that the thinking for the report in the pipeline as okay?
Mikołaj Świątek 00:56:13 So… With the way… with the way the constraints in core are right now, it's… if you have a pipeline where all of the receivers are stopped, but there are still other components in that pipeline which are okay, that pipeline is definitely stopping, because you're not allowed to have a pipeline without receivers.
Okay. Right.
But it is possible… as of, you know, 2 months ago, roughly, I think, to have a pipeline which has some amount of receivers, and some of them are stopped, and some of them are okay.
Tyler Helmuth 00:56:49 I mean, that's.
Mikołaj Świątek 00:56:49 case, we should, we should report okay, is… is, I suppose, the crux.
Tyler Helmuth 00:56:55 Yeah, that's.
Mikołaj Świątek 00:56:56 Sure.
Tyler Helmuth 00:56:56 That feels okay. I think that feels okay. That situation where there's some way to get data through the pipeline still, I think reporting is okay, is fine, as long as, like, the stopped Status is also reported for that component, so that if someone that's receiving the status, it's gonna say, okay, the pipeline can receive data, export data, but not from these receivers.
Mikołaj Świątek 00:57:18 Yeah, technically, there's also the case where you can have a pipeline that can… data can flow through it, but if one of the components is, like, in a permanent error state, right? That's possible. And in that case, we report the permanent error state, which I think is also correct.
Tyler Helmuth 00:57:36 Yes, I agree.
Mikołaj Świątek 00:57:37 Okay, so that makes sense to me. I can… I can update the issue to propose, like, a more… Kind of, if at least one… if at least one exporter and one receiver are okay, then the pipeline is okay.
Blake Rouse 00:57:52 I think we also have the case here, though, that we need to handle when it comes to just, like, memory leak, right? Because, like, if we don't remove the stopping after a point of time, they exist forever.
I mean, the stopped, not stopping, the stopped. Like, they, you know, then they just exist forever.
And we wouldn't want that, either.
Mikołaj Świątek 00:58:14 Yes.
But that's, like, a separate problem.
We should actually have an issue file for that if we don't have it yet.
Tyler Helmuth 00:58:24 The other… the other cases, maybe, where… Some components are okay, and some components are stopped, and it should be considered Not okay would be, like, if all of your exporters are stopped.
That's… I don't know if the core… what CORE's doing with that, but that feels like, not okay.
Mikołaj Świątek 00:58:43 I think that's impossible. I think that's impossible. It's, like, it's… you have to… in some sense, that's an implementation detail. It has to do with how core actually stops a pipeline, because it goes… with… starts with receivers and goes down. So this is, I think, impossible to actually happen.
But… Maybe we should… we should try to detect that and say something, if it happens. Yeah, because I think it would be possible if a.
Tyler Helmuth 00:59:14 Oh my goodness.
Mikołaj Świątek 00:59:15 I've encountered a bug, you know?
Tyler Helmuth 00:59:16 Yeah, like, if a component implements itself poorly, where, like, something can happen, and it calls its own shutdown function.
then, like, you're effectively stopped, but the service… I don't know if that matters yet, but there's… there's edge case… there's probably ways to get into an edge case.
Mikołaj Świątek 00:59:33 A component can definitely report itself stopped.
Yeah. I'm pretty sure nothing really stops… nothing prevents them from doing it.
All right, cool. I think… I think I'm good. I'm going to update the issue, and then I'm just gonna ping, actually, both you, Evan, and you, Tyler, to… to say if you agree with a change. And independently, yeah, we should also try to… we also need to decide What we're doing about dropping the stopped statuses, exactly.
From the snapshot that we put out, because it's now possible to… to have them linger in there.
Theoretically.
Okay, I'm good. Thank you. I think we're… Exactly on time.
