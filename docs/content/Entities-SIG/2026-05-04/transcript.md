SIG: Entities SIG
Date: 2026-05-04
Duration: 51 minutes
Zoom Recording URL: https://zoom.us/rec/share/FmUIEjrK2x-JxQoxMZwAxH5_fgkUA5YtxW_ZAKQibkIwLBbUjbAZZmarvAOb8_3R.YYz7261JbPORxGwF
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin** 04:53 Hi, everyone. I just, saw a message from Josh, he's not gonna… join. He's got the… cold today, so I think… We should just cancel it today.
Given that he runs it.
Does that sound good?
**Ted Young** 05:16 Unless there are… are there new people showing up who just have, like, questions that could be answered?
Oh.
Okay.
Krajim?
**krajo Krajcsovits** 05:30 Yeah, I'm kind of new.
I do have a… hey, I do have a question, like, kind of a… Just for my understanding, I'm still in this phase of trying to understand entities.
And I think I understand the… The concept, and the goal of, you know, left-hand navigation being actionable.
Being able to put these entities on, kind of.
After the fact, like, with resource detectors or empty detectors and everything.
One aspect that kind of stumps me is that This is kind of… I can think of it as the space dimensions, like, various density.
But we know that, you know, space and time are intervened, so there's a time dimension to all of this.
And when it comes to metrics, and I'm coming from… from A2s, where we are trying to do some… write down some requirements around entities.
So, from metric's point of view.
when I have a time series, it's kind of hard For me to imagine… What will be the difference between the identifying and the descriptive attributes?
In the time series.
Because… You know, we talked about the fact that we'd like to see… A single line on, like, a dashboard.
If only descriptive attributes change. So if I have a time series.
And the identifying attributes are all the same.
It should be the same line, with the same color, even if some descriptive attitude changes.
That's already… Maybe not so trivial to implement, but… Coming to the query side, it's even more complicated, like.
if I query that time series in the past.
Can I use the current name of it?
Or do I have to know the old name for it?
What happens when I aggregate?
do I see those descriptive attributes as different series, or one series? So, I don't know. Where can I read up on, like, more on… How the entities, especially the descriptive attributes, supposed to work in metrics and queries on time series?
**Dmitrii Anoshin** 08:00 I don't think we'll… Ever decided that time series is supposed to be only based on identifying attributes. We still… like, currently… I think having identified an attributes as a time series would be… easier for the backends to maintain, right? But we introduced an option for descriptive attributes to change over time.
So if you… if the backend cares about that descriptive attributes, potentially it should be different MTS in that case.
Otherwise, if, it can be selective if some, some MTS, some, descriptive attributes aren't necessarily… variable.
They can be dropped, but the problem… the thing is that the defined attribute cannot be… Cannot be dropped by the backend.
Like, this is a requirement, and the requirement… a contract from the OpenTelemetry side is that those will never change for the lifespan of the entities involved.
**Ted Young** 09:13 Yeah.
So it's sort of like the difference between a unique identifier is what we're aiming for, and that's what, trying to take the guesswork out of that unique identifier, right? We have resources in OpenTelemetry right now, but no concrete definition of what's a unique identifier for each kind of resource. But if you're talking about metrics and aggregates, you're probably not talking about unique instances anymore, right? You're looking at aggregating across some dimension. So the difference between an identifying attribute and a descriptive attribute isn't as important.
From that perspective. So it's more… less about, like, changing the way we'd be building graphs, and more about changing the way… er, graphs is the wrong word. Less about the way we'd be looking at building time series, and more about changing the way we're building topology and graph You know, like, graph databases of what's going on.
**Arve Knudsen** 10:15 I think, kind of, in my experience from, prototyping, this functionality in Prometheus, basically, identifying attributes will contribute to the time series, identity. I think it's also because, otherwise, if… if resource identity is not part of the time series identity, I think, actually, time series might conflict. That's one reason for it.
But I don't think, I don't think descriptive attributes should, by default, contribute to time series identity. It's something I've discussed with Kai already. They will contribute to time series identity when you include them, e.g. through the… by calling the info from cranial function.
But… but… But then you get new time series in the result set from the call to the info function. So then it's… then it's an explicit choice on the part of the… of the user.
So that's kind of, kind of what my experience tells me.
**krajo Krajcsovits** 11:23 So… Yeah, I heard that, yeah, we can… Basically, even drop descriptive attributes.
I think that will never happen, because people will want to search by them, so we cannot do that in Prometus. That's my… Photonet. Also, I feel like people will search by descriptive attributes.
And that could be a way of saying that, oh, now we are explicit about That we are using the descriptive attribute to find the series, so kind of identify them.
And then I guess that means that… When you're searching by a name, You will only find it when that name is correct, meaning that if the name changed over time.
I will not find the time series with… when the name was different, even though it's a descriptive appreboot, so it shouldn't matter, but if I request by name, then it will Actually matter, right?
So we're not trying to be very smart and say that, oh, I will figure out This descriptive attributes means disidentifying things, and then… Go from there, right?
**Dmitrii Anoshin** 12:41 Right, right. That's exactly expected to be here.
**krajo Krajcsovits** 12:46 Okay.
Right.
But on the other hand, if I show something to the user from… as a time series.
I cannot just show the identify attributes, because those will be IDs that will say nothing to them.
So… I have either the choice of Okay, I will show the… the name as well, because that's what they will understand, but then it will mean that I will show multiple series on the graph, or in the visualization.
Or maybe I can be smart on the visualization side, and maybe That was one idea that we had, that maybe we could be smart on the visualization side and say that, okay, I see… the backend gave me the data, it told me what are the identifying, what are the descriptive, and then I can figure out what to show as one line.
But that's… that would be UI, basically.
side.
**Arve Knudsen** 13:55 I kind of feel like this is a PromQL semantics question, really.
Because, I mean.
When you use the info function, the semantics will be the same as when you join with the infometrics.
But then you could choose, I don't know, to… to have… to introduce some other… PromQL mechanism for treat… for treating research attributes as metadata instead of labels, for example.
**krajo Krajcsovits** 14:30 I mean, to be fair, to me, this is not a, you know, question about the current implementation, but what we want to achieve. Like, what is that we want to, like, to see?
And… Yeah, right now we cannot… show one line. It will be… if you use the info function, it will be two lines, because the name changed.
Info function gave new labels, so it's… It's two lines, so that's… that's perfectly fine. I'm just trying to ascertain, like, what we want to achieve.
**Ted Young** 15:02 I think entities were probably going to change less in terms of Prometheus than it might seem, because we're just talking about creating compound identifiers, right? So, like, for example, you know, for a service instance, like, the identifying attributes or the instance ID, That idea is, like, just a long stream of gobbledygook from a human, and then the other two are, like, the service name and the service namespace, right? So I think you're gonna be much more naturally interested in, like, service name and namespace and things when you're making queries.
And the only time you'd be querying service instance ID is if you were literally splatting that ID in from… somewhere else. So, I don't know if the workflow would really be that much different than what people do today. It's more just about formalizing which ones you should be using.
**krajo Krajcsovits** 15:58 I mean, the relevance comes in when you do something like sum over time, so you want to Find… sum of values.
And, maybe I'll act on that. And then… Aww.
if you… Add the descriptive attributes before the sum, then it's going to be Two results that you get, and not one, and you will not get an alert.
Aww.
On the other hand, if you do the sum first, and then you add the… the, descriptive attribute, you get the correct alert, and you get, like, the current name of the thing, presumably, because you will, you know, get the name from the end of the interval.
Which is what would you expect.
But it's kind of… from Cal is complicated enough.
Without having to.
You know, they're about the same.
**Dmitrii Anoshin** 16:54 I'm not sure I understand why it's gonna change, because if you… if, let's say, name change in between.
I don't think you should sum… with… what names you can do some, because in PromptQL, user would need to specify some aggregation function, right? And if they specify a particular name, then it's gonna be a different one or another MTAS. And if they aggregate over a name by some other attribute.
it will be aggregated automatically with no name involved into that prom queue, so…
**Michele Mancioppi** 17:32 When you make a sum or any aggregation, the resulting metric does not have a name.
Ever.
You can add it with label, the label relabel function, but I've never seen anybody in my life do that. So, going to the aggregations, the names are gone.
Mattress no longer have names, or what do I mean?
**krajo Krajcsovits** 17:52 We're talking about, sorry, we are talking about the, like, a descriptive attribute, not the name of the metric, but the descriptive attribute.
Fuck.
**Ted Young** 18:03 I think the difference between identifying and description stops mattering when you're talking about making dashboards and aggregations, right? Like, we're picking a set of… attributes to be the identifier, because we're just trying to find a… one… a way to create a unique ID that isn't… things generating, like, a grid and attaching it, right? Because you might be getting this information from multiple places, so who's creating that grid? Like, we're not doing that. So instead, we're saying we're using compound attributes that are being generated by the things we're observing.
Rather than slapping our own GUIDs on it. So you have, like, you know, service instance ID, service name, service namespace is, like, the identifier for a service. But there's also, like, service version.
Right? That's a descriptive attribute, but, like, in terms of, like.
Looking at aggregates and, like… like, service version is, like, a very useful attribute, just because we're saying it's… you don't… You could add that in to the identifier, be like, and service version, but because not everything reports a service version, and you've already got uniqueness from the first three, we're saying service version's a descriptive attribute.
But it's not saying it's… it's, automatically something that wouldn't be Useful as a dimension.
So, I think in practice, I don't know that entities are going to change the way people are using Prometheus with OpenTelemetry very much.
**Arve Knudsen** 19:38 I agree with Ted. Like, I think, I mean, again, from my experience prototyping, I really do think what entities bring to the table immediately is that they define which of the research attributes are identifying from the OpenTelemetry point of view.
They, it doesn't really matter to Prometheus whether research attributes are identifying or descriptive from that point on.
It just tells you which identified the resource.
**Ted Young** 20:11 You'll notice when… when we are in situations where the underlying system is reliably giving us a GUID, right? Like, Kubernetes is giving us, like, you know, you have the pod UID, so we're like, that's fine. Like, what's the identifying attribute for a pod? The UID. It literally has a unique identifier, we don't need to create a compound one.
But if you're trying to, like, look at pods across different aggregates and dimensions, then those descriptive attributes, or, like, pod labels and things like that, are… are useful. We're just saying, like, trying to figure out which thing to use to find a unique identifier, we don't need to bother with those, so they're descriptive.
And thus we're also saying, like, if a backend wants to throw those things away or do something with… you know, if something along the pipeline wants to get rid of those things, that might not be a good idea, but we're… We're just trying to limit ourselves to saying, please, please don't get rid of the things necessary for a backend to create an identity.
So it's more like the identifying attributes are, like, the minimum subset.
That we need to… to create a unique identifier to track something.
**Michele Mancioppi** 21:23 So, maybe I can make an example if I understand what the discussion is about, because I'm still not sure.
Let's say that I have a metric about how many HTTP requests I get for each of my pods. The Kubernetus pod UID is identifying for the pod resource.
But I want to calculate in Prometheus the request I get across all my pods, and it is perfectly legitimate for the user to aggregate the Kubernetes pod UID away, just by making a sum, without a buy Kubernetes pod UID.
**Ted Young** 21:54 Crasher, I think your general question was sort of like, from a Prometheus perspective, if people are, you know, sending, you know, OTLP to a Prometheus backend, right, and people are trying to look at metrics there, you know, what is entities going to change about OTLP from the perspective of, like, how you would use it in Prometheus?
So, I think that was the general question, and what we're saying is, like, it probably honestly shouldn't really change anything, that much.
**krajo Krajcsovits** 22:28 Yeah, I think, the… trouble I have is that there's no concept as a descriptive attribute or descriptive label implementers. And I'm… I'm a little bit worried about the consequences of people assuming things, and and then the reality is different. Like, they might read the auto spec saying, this is a descriptive attribute, this might change, but doesn't change the identity. So, if I ask… like, the latest name, like, I ask for something by the latest name, I should get the data back in time, even if the name changed. That could be a reasonable, you know.
thing to… thing to say. I think right now.
my perception is the same as yours, that it will not change much. We can probably put in some warnings, we can return warnings with PromQL results, and we could put in some warnings saying that you did search by descriptive attribute.
results might be weird or something. And that's, like, the MVP that you can do, and that's probably fine, but, like, I'm… I'm just worried that as soon as somebody does an alert, that depends on the script altitude, and that changes, and you don't get all fired, then I get a support case, or we… Which is not the greatest.
**Michele Mancioppi** 23:46 I'm sorry, could you… I… Why would it look weird if the user searches by descriptive attributes?
**krajo Krajcsovits** 23:57 Because, for example.
there's a, like, imagine there's a metric, where the descriptive attribute is some kind of, I don't know what, a name of something that is not an ID, a name, like a human-readable name.
I'm searching for it, and I'm looking back one month.
**Michele Mancioppi** 24:15 Here.
**krajo Krajcsovits** 24:16 And… I see that I don't have data for the last, like, the first 3 weeks, only the last week. Even though I know there is data, but because I searched by the descriptive attribute, it no longer matches the data all the way back.
**Michele Mancioppi** 24:35 How is this different from, any other change to label set?
**krajo Krajcsovits** 24:40 It's not different, but then what is the difference?
I'm getting, by the way, from all the discussions, I'm getting that from Prometer's point of view, there's no difference between identifying and describing.
**Ted Young** 24:51 Exactly. It's… it's just resources, so it's the same, you know, annoyance from Prometheus about, like, what the heck are we supposed to do with these resources that come in with the data? Like, how should we use them? It's just that it's not really… it's that same question, but it's not really changing that question in any… in any way.
**Michele Mancioppi** 25:10 Purely, purely technically. Since, to my understanding, it is not yet settled how our resource attributes going to be exposed In label sets, and there is still Well, I've not kept track, so… correct me if I'm wrong, but still, the idea was to use the discovery.
what is it? Yeah, the discovery attributes, and then, relabeling to actually import that attribute. So technically there, one could say that if you are scraping a metric, and you are not storing one of the Identifying attributes, that is maybe where I would tell you, hey.
Your recording rules… sorry, your labeling rules are missing an important attribute, because that is identifying.
With a capital I. But that's as far as I think the difference goes between identifying attributes and non-identifying attributes in the Prometheus world.
**krajo Krajcsovits** 26:10 I mean, we are… we are about to define… I mean, Prometheus doesn't say anything about entities right now, and identifying and descriptive, so that's what I'm trying to kind of… we need to come up with a proposal for Prometheus folks to review and… and look at. So, I can easily say that basically, there's no difference. Like, we can use the identifying things for some kind of optimizations or whatever, but from, like, the usage and API point of view, there's not… well, not maybe the API, but the… Kind of an overall… concept of primatives, where we don't have the notion of descriptive, it's not going to change. We will not have the…
**Michele Mancioppi** 26:52 For example, you could do some very, very yummy UX things, like when you show the label set, move the identifying attributes first, easy to read, but it's weird.
about those mini tweaks, warnings if your labeling is not storing that stuff, but that's the level we're talking about, I think.
**krajo Krajcsovits** 27:12 Okay, well, that's perfectly fine for me. That actually makes my life easier, so that's…
**Ted Young** 27:17 Something to, yeah, something to tell people over there is, like, you know, one thing we're really making sure of is, like, resources are everywhere, right? OTLP and resources are everywhere, so adding entities can't break resources. We're not… like, this is essentially metadata for resources. If we were starting from scratch, we might, like, organize the data a little bit differently, but But, you know, from the perspective of, like, a Prometheus system ingesting the data, whether entities show up or not is just… just, like, additional metadata. It's not that the resources are gonna start moving around, or, becoming more unstable, or really any different.
than how you would existing. So a legacy system that knew nothing about entities, but knew about resources, wouldn't see any change once systems start emitting this additional entity data.
**Michele Mancioppi** 28:13 Wait, wait, wait, wait. There were still, however, some discussion about extending OTLP with entities.
**Ted Young** 28:21 Yes, like, but as a additional… additional information.
Right, right. Like, we don't want it to be a situation where, like, you get the next batch of OTLP in, and resources are now just blank because there's some new field called entities, and we moved… mutated how we're reporting it. That seems like something that would be really painful on the community, so we're trying to avoid that situation.
**Michele Mancioppi** 28:50 So it's gonna be a break-the-world scenario. So ultimately, we're going…
**Ted Young** 28:54 We don't want to do that. If we were doing it from scratch, then we would, I think, have things more nested. I mean, in general, in OpenTelemetry, if we redid the data model, you could see things being more nested.
than they are. But because we don't want to do that, it's more like you have resources, and then you have some additional entity metadata information Reported, you know, as, like, another field, or as a side channel, or something like that.
**krajo Krajcsovits** 29:22 Yeah, I mean, we currently do deal with resources in, like, some weird ways in Prometus, like, you know that there are some things that we promote, you can select what to promote to identify, blah blah blah, and entities will help with that, for sure, but it is, again, kind of an optimization, it's not a fundamental change Like, to me, again, the fundamental change would be if we had to actually care if it's descriptive or not.
Beyond, you know, optimizing, storage and showing making nice UI, like, but if we had to fundamentally change how we think about it, then that would be a big problem, I think.
**Michele Mancioppi** 30:00 This actually brings me, to one of the pain points that I see in users trying to reconcile Prometheus and OpenTelemetry.
That, they're relabeling configurations, they don't know what to do.
Will you consider… By providing an opt-in or an opt-out, something easy to set, or say, look, all the attributes that are identifying, and they come from entities, they get relabeled on the time series automatically.
Instead of people having to obtain to a bajillion of them.
Because that could remove a lot of the craft that today is about reconciling the two systems.
**Arve Knudsen** 30:45 Don't quite understand your question, Michaela. What do you mean by relate?
**Michele Mancioppi** 30:50 Today, to my understanding, Prometheus still exposes resource attributes in the discovery.
So, you have the metadata that you can additionally put on time series.
And that is an opt-in with our labeling configuration.
**Arve Knudsen** 31:09 These are not resource attributes, right? I mean, resource attributes, they are… they enter Prometheus via OTLP.
**Michele Mancioppi** 31:16 Yes, but when you go and scrape something, Yep.
Then you… there is the, the, the service discoverers.
that, for example, allow you to add to the Kubernetes pod UID If your time series doesn't have it, because it won't scraped that IP, it knows that it is that podio ID. Now you have podium ID as an attribute that you could relabel on the metric.
Yes?
**Arve Knudsen** 31:44 But I don't see… that's a different concept than hotel research attributes. I don't quite see the connection.
**Michele Mancioppi** 31:50 Oh, so it's… they're no longer exposed as a target, target, info?
**Dmitrii Anoshin** 31:56 market info, that metric. I guess that's still how it works.
**Michele Mancioppi** 32:00 Yeah, because… What are you saying?
**Arve Knudsen** 32:02 Oh, y'all.
**Michele Mancioppi** 32:02 Is that… Something that could be done, since you will know which attributes are identifying or not.
to automatically relabel, so effectively take the target info and put it on the… in the label set, because those are very important attributes.
**Arve Knudsen** 32:18 But that has nothing to do with, hotel. This is, like, Prometheus, scraping protocol.
**Michele Mancioppi** 32:24 Yes?
But this is an opportunity.
That is there, because now some resource attributes are going to have They're going to look special in target info, because now you know the resource attributes and identifying.
**Dmitrii Anoshin** 32:41 It's a conversion from TLP to Primetheus protocol, essentially. So it will be that kind of specification, how you convert the TLP to parameters. And in that case, yeah, it makes sense to put identifier and attributes of the labels, potentially.
**Arve Knudsen** 32:59 Yeah, I don't know, but… but the way… I mean, the way we plan to encode, whether attributes are identifying or not is actually not in target info, but in a native metadata representation, which Kayo and I are working on.
So…
**Michele Mancioppi** 33:16 When the user use this?
**Arve Knudsen** 33:19 Sorry?
**Michele Mancioppi** 33:19 How will the user access this information?
**Arve Knudsen** 33:23 the, the method around?
Yeah, what is currently prototyped is that the InfoPromQL function will use native metadata when available.
So that, that is, that, that is the idea, that it will, it will, it will use, this native metadata model instead of target info when enabled.
**Michele Mancioppi** 33:49 So, Fatali, you're telling me that the only way I can get resource attributes is by creating a recording rule.
That is making a join, so on group left, or whatever.
Between my metric and the target info?
**Arve Knudsen** 34:08 I mean, that is the one mechanism we have at the moment, in addition to an API endpoint.
**Michele Mancioppi** 34:14 Yeah, because the… so… For example, I don't manage to reconcile in my head how, when I have a Prometheus pass-through.
How am I going to be able to propagate downstream?
The data that is now only available in the infometric.
Infometrics do not… Get pushed to pass through, right?
**Arve Knudsen** 34:36 I don't… I don't know, to be honest.
**Michele Mancioppi** 34:39 So, I don't know how this idea of the infometric will allow systems downstream to have the metrics with the level things, because also recording rules are not running pass-through, right?
Alerting is not, so I assume that recording rules are neither.
So how the heck are you going to exfiltrate?
Precious attributes in this model.
**Arve Knudsen** 35:03 What do you mean, what password?
**Michele Mancioppi** 35:05 You can set up the Prometheus in pass-through mode.
Well, I don't remember if this is the right word, but you can set a perimeter that it scrapes and it pushes with remote write. It does not run alerting, it does not run recording rules, it does not run federation, I want to say, but I'm not sure.
So, in those situations.
How does the next Prometheus… Asian mode, thank you. How does the next Prometheus have access to the infometrics?
It doesn't, right?
**Arve Knudsen** 35:37 I don't know, like, maybe it's better if we talk about this offline.
**Ted Young** 35:43 I think, where there's more interest, I think, in conversion and, like, communication between the Prometheus community and OTEL is less about, like.
the entities as, like, a protocol or a, you know, a data model, and more once… moving past that to, like, the semantics, and the instrumentation, you know? Like, how does the collector collect host metrics and other kinds of information. Like, what are our semantics for, all of these different pieces of infrastructure? You know, and to what degree are people you know.
to what degree is the data OpenTelemetry is producing matching up well with the kind of dashboarding and, like, other aggregates that people are trying to look at, in, the kind of stuff that entities would be describing. I… I don't know a lot about the Prometheus side, but I do know that there's… there's just differences there. So that's probably the place where the two communities would want to, like.
Just make sure that we're actually, like, there's some clear understanding about what kind of dashboards and other things we're trying to create, and, like, which attributes do we use to create those, and… And just talking more about the specifics of each one of these types of entities, and less about the data model itself is where those conversations will get more interesting.
Grajio?
**krajo Krajcsovits** 37:20 Yeah, I agree. I think, what Michelle, or Mikael? Sorry. Michael. Mikael. What Mikhail raised about the forwarding is very interesting, and we should talk about that another time, but if we can, yeah, let's stick to the, The current, topic of, like, what does it mean for primitives to… To have this information about entities, you know, what are the identifying attributes, what are the, descriptive ones.
And again, just to recap, I think what I heard was that prometheus really shouldn't… Care at this point.
Beyond, you know, having opportunity to optimize and make the info function more efficient, because now we actually know what the heck we are correlating.
And… and that's it. And then… If the user has a… has a, like, a question, like, why does it work this way? We can have a very clear answer that Yeah, we don't… How do I say this? Like… We don't treat the strip with attributes.
differently from, like, regular, like, the identifying attributes, really, just internally. And then.
On top of that, we can add some… UI, syntax, like, sugar to it.
Or… and make optimization, but beyond that, that's out of scope.
And I saw Dimitri.
**Dmitrii Anoshin** 39:03 Yeah, I just want to confirm, that's the right, approach, and to clarify and… well, this way, entities is, something that is built on top in addition, even if, in a telemetry world, it's not gonna break any of existing behavior or anything existing. So, the consumers, the backends, and every, like.
who is involved into that should also treat it as an additive change, and add additional capability on top of it, not… never change what already use that. I mean, it's not expected anything to change.
**Ted Young** 39:51 The backends that are going to… care about this the most are more like graphing databases and less like time series databases. If you're trying to make a graphing database of this stuff right now, it's sort of like… you feel like you're just sort of making it up in terms of what the… What the nodes and edges are supposed to be.
Because our data model and our semantics don't give you a clear way to connect all of these different pieces into a graph.
The data's there, but, like, we haven't explicitly defined What the nodes and edges in those graphs should be.
When it comes to looking at the topology of your system. So it's more about locking that down and reporting it properly.
**krajo Krajcsovits** 40:35 I… This area a little bit. I think we do care, and Arva and myself do plan on adding some specific interfaces for grabbing the entity's information, because when you look at agentic.
use cases, and when you want to have, you know, an agent look at the data and Find anomalies.
You know, fix incidents or whatever.
They will very… they would very much like to see a context. And sure, they can look into the code, the documentation, but if they could get it from the database itself, that's… probably a good idea. So… I think there is a place for it, but again, it doesn't fundamentally change, like, what we have currently.
**Ted Young** 41:21 Right, it's more about the metadata that you're storing in that time series database to be able to connect it to the other kinds of databases that you have, so that you can traverse across them, but less about, like, what time series am I making?
You know, to answer those questions, it's more about looking at each kind of resource we're reporting and being like, hosts, how does OpenTelemetry report host today? Do we like it? Do we not like it? What about containers? What about Kubernetes? You know, etc. What about the actual specifics of the data that we're reporting?
are good, and which attributes do we wish were reported differently, or they're missing, or were inconsistent in how we're reporting it. Like, that… I think that's the stuff Those are the improvements where we'll see, you know, better time series database… time series data come out of this. The rest of it is more like exemplars and other forms of metadata that you would be using to connect those time series to Tracing and topologies and other things.
**Michele Mancioppi** 42:28 Although, to be fair examples, they're already part of the Primeter ecosystem, so that is no upward amount.
It's already there.
**Ted Young** 42:40 Alright.
I think that about covers it for… for today.
Josh is out sick, but, Michele, so we were already discussing just ending the meeting early, because there's no new work to report on outside of what's going on.
**Michele Mancioppi** 42:55 Then I came in, I'm sorry.
**Ted Young** 42:57 No, no, no, but we… this was a good conversation, I think, to… to have.
**Michele Mancioppi** 43:03 Then maybe, Cryo, me and Arna can talk a little more about the agent mode in Prometheus.
Because that part concerns me.
And it just… it came to me as Arne was talking about it, I was like, wait a second.
Something is not… is not clicking.
So… Maybe, Arne, Cryo, I huddled you in the sense of Slack, does that work?
**Arve Knudsen** 43:30 Like, shall they… do you mean after this call, or… Like, I mean, I…
**Michele Mancioppi** 43:35 I'll hand over.
**Arve Knudsen** 43:36 I have to drop, so I'm not able to speak anymore tonight, unfortunately, but Vic, do you want to make, like, an appointment, like, like, Would you like to meet later in the week, for example?
**Michele Mancioppi** 43:52 Yes, I'll send you my calendar, so I can explain again what the problem that I'm seeing, that I heard, and hopefully I'm wrong about it, and I'm too worried for nothing.
**Arve Knudsen** 44:05 Yeah, that sounds good. I think, kind of, what I'm interested in is, kind of, sort of, what concrete use case you have in mind, because then it's much easier for me, or for us, I suppose, to kind of figure out, How it connects to what we have in mind.
**Michele Mancioppi** 44:23 I don't find the username of Clayo in the sense of Slack.
**krajo Krajcsovits** 44:27 It's just cryo, but Wait, do I have it differently? Let me just double-check before I do something.
I should have it.
Yeah, I'm just cruel.
So, K-R-A-J-O, or Kiloroma of Juliet Toscar.
**Michele Mancioppi** 44:52 Alright.
Alright, alright.
**krajo Krajcsovits** 45:13 Did you find me?
**Michele Mancioppi** 45:14 Hey, I found… I'm just so athletic.
You both have my Calendly?
We can set something up.
Alright, bye folks.
**krajo Krajcsovits** 45:27 Alright, thank you.
**Arve Knudsen** 45:29 Yep. All right.
**krajo Krajcsovits** 45:30 Bye-bye.
