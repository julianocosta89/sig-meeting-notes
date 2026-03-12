SIG: System Sem Conv Stability WG
Date: 2026-02-26
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/TZYQ1HpGffUHw5vlkvv3dsCYVGMgiTIyatXbzFkq5DEpKcbf5KqTHRCw6eCmnb_-.jyVu17rE6nik1pDM
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:44 Christmas.
**Dmitrii Anoshin** 05:25 My faults.
**Donal O'Sullivan** 05:31 Loween.
**Braydon Kains (Google)** 05:31 Lauren.
**Christos Markou** 05:57 How do we start? I don't think we're expecting anybody else.
**Dmitrii Anoshin** 06:02 I think Brisha's done.
**Donal O'Sullivan** 06:11 yeah, cool. So, I just have an item on the agenda there. I have a PR in… semantic conventions to, update the process attribute requirements level. So I've made both… Identifying attributes of process required.
And all the other descriptive attributes as opt-in, bar, I think, process, process command and process, owner, I've made recommended, the rest are opt-in. So, having PR is… I've gotten feedback on it, and I think Pablo's approved it, so… Just wanted to bring it here. There was… Some discussions around, I think it was updating a couple things, so… first, I think someone wasn't too sure about making all the descriptive attributes as opt-in. They'd rather see them as recommended.
And the other thing was… Creating a separate entity for, like, process, executable.
I don't know that you guys have any thoughts on this.
**Dmitrii Anoshin** 07:27 Donald, this… thank you for the PR. This one, it doesn't change anything, right? It's just, other than, requirement level, all the attributes stay the same, right?
Just to clarify.
**Braydon Kains (Google)** 07:40 None of the attributes changed, it's just the…
**Dmitrii Anoshin** 07:42 They used to default to recommended, because if you don't specify, that's what it defaults to.
**Donal O'Sullivan** 07:47 Yeah, exactly, yeah, yeah.
**Dmitrii Anoshin** 07:48 I'm not sure if it's written somewhere in the spec, but I guess we just need to follow the logic that if, Like, we should have recommended some set of attributes, but if there is more descriptive set of attributes that overlaps with existing ones.
we should figure out which one would be opt-in and which one would be recommended. My point is that we shouldn't have let's say… command line and command arcs both as recommended, because, like, command arcs are subset of command line, right?
That would be my, kind of, understanding here.
But yeah, otherwise, yeah, thank you, that was good. I'll… I'll take a look as well.
**Donal O'Sullivan** 08:45 Cool, that, that, yeah, thanks, Dmitry, that, that, that makes sense.
So in terms of, I think, making process executable its own entity is probably something we don't want to do, like, we don't want to be… splitting out the entities. We probably want to keep it as is and just update the requirement levels, I guess.
**Dmitrii Anoshin** 09:12 And I need to look into the discussion about that, but I guess executable, if it's something else that we can attach other set of telemetry.
that cannot be attached to the process itself. In that case, it makes sense to move it out, right? But if it's one-on-one, like, relationship, and it cannot… we cannot have telemetry specifically attached to executable, separately from the process.
I don't think it makes sense to move it out.
**Donal O'Sullivan** 09:45 Okay.
**Dmitrii Anoshin** 09:46 Not, like, able to follow that kind of logic. Braden, go ahead, sorry.
**Braydon Kains (Google)** 09:51 Sorry. I've always liked the idea of executable being a separate entity, because a lot of the stuff that, like, profiling wants to attach to, like, specifically are, like, Like, file-level attributes that, like.
You wouldn't think of those as, properties of the process. You'd think of those properties of the file that the process is running.
So, like, those attributes living on the process always felt a bit strange to me. So I like the idea of it being a separate entity, but I don't know how, I don't know how the profiling people feel with that. I think they're the people who need that stuff the most, so… Not sure.
**Dmitrii Anoshin** 10:34 Will it be an entity called, like, file, essentially?
**Braydon Kains (Google)** 10:39 It would be process… it could be called, like, process.executable, but a lot of the properties of it probably would be, like, under a file namespace or something, since they're information about a file, like…
**Dmitrii Anoshin** 10:51 Yeah, that's my question. Can it be, like, actually, file entity? Because file entity by itself makes sense.
**Braydon Kains (Google)** 10:58 Yeah, that… that also… Could be worth looking into, because, like, we could use a file entity in a lot of places.
**Dmitrii Anoshin** 11:06 Right, right.
**Braydon Kains (Google)** 11:07 So… So maybe that's… maybe that's the direction we take, and then a process can have, a file entity attached for the executable that it's running. That seems pretty reasonable to me.
**Dmitrii Anoshin** 11:22 Yeah.
**Christos Markou** 11:28 Do you think we could just… in this particular PR to, just focus on the requirement levels for now, and… Come up with a follow-up once it is, like, merged.
And decide if we want to detach the executable in a different, issue?
**Dmitrii Anoshin** 11:48 Yeah, that's a good, very good point. Let's maybe comment on that issue, that we have a discussion, we have some ideas, but let's keep it separate from DPR.
I think that that's what should we do.
**Donal O'Sullivan** 12:04 Okay. Cool, I can… I can comment back on, on, on the… on the PR, and just mentioned that, that we… we agreed to just keep the open PR about requirement levels, and we can… we can… Create a new issue about, separating process.executable.
**Dmitrii Anoshin** 12:21 Sounds good. Thank you.
**Donal O'Sullivan** 12:22 Okay. Thanks, guys.
That's all I have, anyway.
**Dmitrii Anoshin** 12:47 Brandon, do you want to bring your, issue?
**Braydon Kains (Google)** 12:50 Sure. So this is… This is happening right now in the host metrics receiver, but… Essentially, we don't produce the… service resource attributes, service name and service instance ID, and this is… more important than I guess I realized, because of the way that Prometheus decides to create target info from OTLP.
So, there… Arvey had… Propose a solution that created a unique service instance ID for each process out of the process scraper.
the… I thought the logic that they were using to produce the instance ID was sound. It uses… it's a generated UUID from Certain information about the process, so that it's deterministic, it's not going to be, like, randomly generated for every scrape.
But… Dude.
I… maybe I just don't understand what service instance ID It's supposed to be, but… the instance ID… each process in a scrape getting its own instance ID and service name.
doesn't feel right. It feels like this… the instance ID Should be the one from the collector.
So the service name and the service and society should be from the collector. I don't know if maybe I'm just misunderstanding.
How… the Prometheus decides to handle this. It's… it seems like, like, what… Ideally, if I was scraping a bunch of processes, and I had all of them in a Prometheus scrape.
The target info would be about the host that the process is associated with.
So… Them… like, we wouldn't want a target info for every single process.
But if it's… if each one gets its own service name and instance ID, isn't that kind of what… That ends up meaning.
I don't know if anybody has experience with this. I saw Chrysalos posted about what Cates does for this.
It might apply?
I'm… I'm not sure.
**Dmitrii Anoshin** 15:09 Just to bring some context, service IDs, service name and service instance ID, they are important for… mostly for tracing instrumentation.
And typically, if we are speaking about processors, It would be.
service name and service instance ID of a service… application level that is running on that particular process, because otherwise it will be hard to correlate between service, like, between actual service that is application that is running on this… on the process.
And the process itself.
So, it's like, it's a bit… Not, let's say, infrastructure-related concept, but more application layer concept.
And, I don't think we should… m-make it.
conflicting and… conflicting with each other, essentially. We need to ensure that whatever metrics are produced by the process, if there is an application there.
we should get service name and service instance ID of that application, that process. Does that make sense?
**Braydon Kains (Google)** 16:20 Kind of. Does it mean that, like, in… that, like, when we scrape the processes, we actually should… that, like, they should each have their own service name and instance ID from our monitoring?
**Dmitrii Anoshin** 16:35 Oh, yes.
like… if we are scraping Prometheus, I'm not sure how Prometheus said that information, but it would be responsibility of instrumentation to set that. If it's instrumented with OpenTelemetry.
I would say… I would guess that OpenTelemetry Prometheus Exporter would set service name and service instance ID.
the same as it produces tracing data. In that case, we should, we should, like, handle that properly. We should take that information and put it on the service entity.
When we scrape Prometheus Endpoint.
**Braydon Kains (Google)** 17:21 In the host metrics receiver, when we… scrape processes.
We can't know anything about whether those processes are instrumented, though.
**Dmitrii Anoshin** 17:30 Right, right, I don't think we should do the process of cosmetic receiver in that case, because it's going to conflict with application instrumentation.
**Braydon Kains (Google)** 17:38 Right.
So, the use case that they're trying to deal with is, like, what we say is host metrics receiver should be used alongside resource detector, so that the resource correlation can work.
**Dmitrii Anoshin** 17:57 Thank you.
**Braydon Kains (Google)** 17:58 the argument from Lyudmila and Aave is that It should work. We should set this information to the best of our ability at the receiver level, such that it works without the resource detector, and can still… Prometheus can still generate target info.
So.
they're asking us to set… from our, like, process scraping, to set a service name and instance ID for every process.
Which…
**Christos Markou** 18:29 But this might differ from… So, if you are collecting metrics for a target process, and this process is also instrumented, and the instrumentation sets a service ID and the service name at first place, you will produce to… the metrics will come with, like, random UAD, But the traces will come with a specific UID, or a name that is set by the instrumentation.
So…
**Braydon Kains (Google)** 18:55 Correlation.
**Christos Markou** 18:56 Won't work, I'll change.
**Braydon Kains (Google)** 18:58 The problem would be, like, if we're sending… if, like, the process is instrumented with OTEL and sending to the same backend as our collector that is just generically scraping every process on the VM.
**Christos Markou** 19:09 Yeah.
**Braydon Kains (Google)** 19:11 So, like, if we… if we produce a service name and service instance ID for our, like, process resource of us just, like, generically scraping the process, and then… The process itself is producing its own service name, and… instance ID.
Then weird… weird stuff will happen in the back end.
I… I… if I'm understanding correctly.
**Dmitrii Anoshin** 19:32 Yeah, like, if it's something that we should set, right, it has to be the lowest priority, somehow.
And if we have, let's say.
I don't know, some kind of correlation on the collector or somewhere else that would get, like, information from the application, from the instrumentation, regarding that service, that should override it. But… Yeah, I don't know… we don't even have that capability at this point, so… I'm not sure if adding that to the… Host management with receiver makes a lot of sense.
**Christos Markou** 20:10 I think the instrumentation itself should set process-related metadata, populate the process entity, let's say.
And then… In the backend, you can correlate process metrics with the traces that come with a specific process.
**Dmitrii Anoshin** 20:28 name, for example, process PAD, whatever.
**Christos Markou** 20:30 I think that's the most accurate way to do it.
**Dmitrii Anoshin** 20:34 Yeah, I think, like, you're… I agree, because it's, like, infrastructure kind of concept, and we don't have anything.
To know about application.
**Braydon Kains (Google)** 20:46 So, the… The issue then, if you look on the issue, Lyudmila commented this as well, but basically, without a service name and service instance ID on the root telemetry that we produce.
the OTLP to Prometheus conversion.
is harmed because it won't generate a target info if there is not a service name and instance ID.
On the… on the telemetry coming in.
So we need to… essentially, they're saying we need to set something.
My opinion is that, like.
You know how the collector has a service name, and it has a resource that comes with the telemetry settings?
I figure… We should just use those on every process.
Because then, if there's no resource detection, all the… all the… The process metrics are at least Correlated with, like, It came from this collector.
**Christos Markou** 21:46 I think you would need, like, a processor that, like the… similar to the KH attributes processor that could correlate, metrics with… Services, somehow, at the collector level.
So, for example, in KH Attributes Processor, we get, for example, the pod ID, and with this, we can correlate the incoming metrics with Kubernetes metadata. So, incoming process metrics.
based on the PID, for example.
should be, correlated somehow with, like, service data. But the question is how you can know this service data, this service information.
**Dmitrii Anoshin** 22:34 To me, it seems like the full requirement is questionable for the premises version. Because, like, why do we need to associate everything with the service? Why, like, host metrics supposed to be a service?
**Braydon Kains (Google)** 22:49 So, I agree… I agree with you. I think it makes no sense.
I haven't been finding it at that level. That might be worth opening a discussion about.
**Dmitrii Anoshin** 23:00 Yeah. Like, what if we have, I don't know, cluster metrics, like, namespace, Kubernetes namespace metrics, what service is that?
That, yeah, that doesn't make a lot of sense to me.
We should, yeah, we should probably bring that.
That requirement to question.
**Braydon Kains (Google)** 23:19 I linked the… the issue in the, in the, the agenda. So maybe we start the discussion there, because they… they… I mean, so there are some things that I question in the original issue, Which is that… One of the things that he describes as a negative effect is that there's no host-to-process correlation if the service name and service instance ID aren't set, but actually, there's none regardless if you don't resource detect.
Like, the only way for this to work is to re… is to have a resource detection.
So, I don't actually… Know if that… part maps.
**Dmitrii Anoshin** 24:05 Quite, either.
I think we can move resource detection for the host to host metrics as well. Like, potentially we can make it a library.
So who's nice.
**Braydon Kains (Google)** 24:16 I could see that working. Like, I could see a world where like, there's just some root… like, the scrapers, when they need to make a resource, they start by grabbing from, like… maybe, like, at host metrics receiver creation time, we detect the host itself, like, the host information itself, and then attach that to all telemetry produced by the host metrics. Like, I could see that working pretty well.
But, Nick, yeah, let's, let's… let's comment on the issue. I… I don't… I don't… I don't mind the idea of setting, like, the collector's service name and service instance ID as a default, just for the instance ID and service name to, like, exist. I don't like the idea of each process getting its own instance ID. That doesn't make much sense to me.
**Dmitrii Anoshin** 25:12 Yeah, for me, either of them… Doesn't sound necessary at all, so…
**Braydon Kains (Google)** 25:19 And I think Ludmila's actually trying to push this as a more general collector problem, that, like, every collector component should produce telemetry with service name and instance ID somehow.
And I don't know how to apply that, either.
**Dmitrii Anoshin** 25:36 Yeah, we can maybe bring that and also discuss. They actually have their own SIG now for the series?
**Braydon Kains (Google)** 25:44 Oh, yeah, I think so, yeah, the service and deployment one, right.
**Dmitrii Anoshin** 25:48 Yeah, we can maybe discuss it there as well.
**Braydon Kains (Google)** 25:51 True.
**Dmitrii Anoshin** 25:52 Thank you, Braden.
**Braydon Kains (Google)** 25:54 Thanks.
**Dmitrii Anoshin** 26:00 I can summarize what we discussed, and maybe… In the issue, and maybe we… Or I don't know how to price it, like, we can summarize it in the issue, right, about how to bring it… Maybe we'll just add to agenda of this service seek.
Or, like, specifically.
Sounds good.
**Braydon Kains (Google)** 26:27 I don't… when is that? I can… I can try and join. Oh, it's, like, in 5 minutes.
Service and Deployment SEMCOM stick?
At 11.
I can enjoy.
**Dmitrii Anoshin** 26:43 Yeah.
I can join as well, I guess, so maybe we can…
**Braydon Kains (Google)** 26:52 Right. I think that's everything for this meeting, then, unless anybody has anything else.
**Christos Markou** 27:01 Sounds good.
**Braydon Kains (Google)** 27:03 Thanks, everyone.
**neil yashinsky** 27:04 Okay, thank you. Thanks, everyone. Bye.
**Donal O'Sullivan** 27:06 Thanks, guys.
