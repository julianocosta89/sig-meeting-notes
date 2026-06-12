SIG: Arrow SIG
Date: 2026-06-11
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Albert Lockett 00:01:10 Hey, everyone.
Laurent Querel 00:01:13 Hey, Ben.
Gokhan Uslu 00:01:21 Good morning.
Laurent Querel 00:01:22 Good morning.
Okay, so we have a document, a Google Doc document. I see that, several people are already adding their name, which is great.
If you have some, element to the agenda, I encourage you to add, New bill of prints.
I think today, Joshua McDonald will not be able to… To assist to this meeting is on vacation.
Okay.
Okay, great.
So we had, two days ago, a presentation to the… specification sign-mitting, where a lot of maintainers and tech leads in OpenTelemetry are present, or were present.
That was an opportunity for us to… Basically, to, to present this, slide deck.
I will share the deck directly on the… I will do that now, in fact.
So, we have… You're a dead cat.
So, yeah, we are basically… we did a very quick review on Phase 1, nothing really new there, and then we presented the main question that we tried to answer in Phase 2.
The benchmark result?
Which are great, in my opinion. They have been well received.
And, and then, why we have been able to achieve such a level of performance.
And we talk very quickly about, some key figures regarding the project.
So… Nothing really… not a big discussion there, but definitively, I think we… we raised interest from multiple people.
on this project.
for example, Tigran, which was the… at the origin of OTLP, Steph, had a discussion, with him after the meeting regarding the performance and… The benchmark infrastructure.
I know few other folks that, Are interested also in what we are doing.
So, I think in a few weeks, we will try to reopen a second level of discussion with the governance committee to define more precisely The feature of the project, Phase 3.
And, and how, who will be aligned with the OpenTelemetry project overall.
I think some people, were present, during this meeting at InCigo.
I remember… yeah.
Cijo Thomas (Microsoft) 00:05:39 Awesome.
Laurent Querel 00:05:40 Any additional, feedback?
Cijo Thomas (Microsoft) 00:05:42 No, I think you covered it pretty well, so nothing more to add.
Laurent Querel 00:05:48 Okay, anyone else that I could miss that… It was present during the meeting, yeah.
Matt Wear 00:05:59 How was that?
Laurent Querel 00:05:59 Okay.
Matt Wear 00:06:00 and.
Laurent Querel 00:06:00 Oh, okay.
Matt Wear 00:06:01 it piqued my curiosity, so I started looking at the project. Yeah, I used to work with Josh McDonald, so, like, I'm… kind of aware of this project, but when I used to work with them, it was kind of maybe very much in its infancy, and mainly kind of, targeted towards the GoBase collector, and yeah, I recently got a new job where I am working at a hotel again, and I've seen that it evolved quite a bit, so… Oh.
Laurent Querel 00:06:28 Okay, great. Nice to meet you, by the way.
Matt Wear 00:06:31 Yeah, I guess so.
Laurent Querel 00:06:32 first time we meet together. Yeah, I think, We have a lot… we presented just, a small portion of the project, in fact, during this session. If you come with us regularly, you will see that we have much more to… To present, we have… Plenty of things, like a new processing language, We have, A command line tool to, to basically drive and inspect and manipulate live.
Pipelines and group of pipelines.
manuals or things like that. Hmm.
Matt Wear 00:07:14 Cool, yeah, I'm interested in learning all I can about this, so I'll probably… Great.
Pop in. At least for now.
Laurent Querel 00:07:24 Okay.
Okay, so, I think we will start with triage. I see that we have a lot to say also in terms of additional topics.
So I think we will try to keep triage relatively… Short.
I don't know who created this filter, but that's cool. Thank you so much.
Oh, I still have my issue with my screen. Is my sharing still okay?
drewrelmas 00:07:57 Yes, I can see.
Tom Tan 00:07:58 Yeah.
Laurent Querel 00:07:59 Oh, okay, okay.
So… let's start with Albert. Parquet exporter support Cloud Object Store.
Oh, this one is super old. I don't know why it was.
Albert Lockett 00:08:12 or.
Laurent Querel 00:08:13 I think.
Albert Lockett 00:08:15 additional discussion is needed, I think.
Laurent Querel 00:08:17 I agree, we were just, change the… So I think we can just say triage… Accepted, because it's obviously something we… Already have in place.
Okay… Okay, this one, Aaron, is Aaron with us today.
Aaron Marten 00:08:43 Yes, I'm here.
Laurent Querel 00:08:44 Huh.
Bye, Owen.
Aaron Marten 00:08:46 Hmm.
Laurent Querel 00:08:47 That's a great piece. So, guide us into this, WASM integration.
Aaron Marten 00:08:56 Sure, so this was the first sub-issue of a series of sub-issues I'm working on opening, under the, the top-level one for, binary plugins.
That we've discussed previously. So this one just attempts to go in and, talk about the, you know, have a proposal for what we would do for an interface, defined using WIT.
Wit is the WebAssembly component interface language.
So it allows us to, you know, define functions and enums and all that kind of stuff, and come up with a contract.
So this is… this is just the first attempt to, define that.
And trying to incorporate some of the… some of the feedback from the initial discussion.
Both into the.
Laurent Querel 00:09:47 Okay.
Aaron Marten 00:09:47 into this new one.
Laurent Querel 00:09:50 Yeah, it's a super important, capability, we need to… I think, Albert, at the minimum, you should look at that, Because I see… so, multiple levels of interfaces, the OPL executor.
which, if I understand well, is a way to apply your PL expression to a P data, message.
Aaron Marten 00:10:19 Yep.
Laurent Querel 00:10:20 And that is, a more granular interface offered to WASM component Where they can basically apply some… lower level, action to the same thing, P data, right?
Aaron Marten 00:10:38 Right, right. So the initial, the initial issue, which I've since revised, had a bunch of these very low-level kernel operations, but the feedback that, Laurent, you provided was, you know, we don't want the data to really ever be considered invalid hotel data, which of course makes sense. So, this WIT interface, is proposing two basic groupings of operations. As you noted, there's the OPL, which is essentially just, hey, run this OPL program.
Over the data. But that first category is a set of operations that are intended to Provide guarantees that they are not going to do a transformer that would make it invalid. So it's a… it's a subset Of the operations that could be done.
Laurent Querel 00:11:27 No.
Aaron Marten 00:11:28 But they're still lower level than OPL.
Laurent Querel 00:11:32 Yeah, I think this… part of this issue will require a lot of, discussion.
Albert Lockett 00:11:40 Yeah, I think we can…
Laurent Querel 00:11:40 Easily recognized that it's a super important thing that we need to do right.
Yeah, Alber?
Albert Lockett 00:11:49 I was just gonna say, I can take a deeper look at it, after, after the call, too. I think that, like.
having the OPL, interface to it is, is really nice.
Laurent Querel 00:12:02 Yeah.
Albert Lockett 00:12:02 Because, again, you can, you can say, like, I'm gonna do this transform that's quite complicated and has quite a lot of steps, and guarantee that, like, what you get out won't be basically invalid OTAP data.
I think another thing that might be nice that we might want to explore for this, we might want to explore for, like, invoking OPL programs generally, could be, like, like a builder interface where you programmatically build your program, as opposed to having to, like, build it using text, and that gets you Out of the world of… if you're trying to do some code gen, having to, like, worry about, like, escaping and things like that, and so… I was planning on trying to, design an issue for that anyway, and, like, maybe there's an opportunity to fit this into… fit that into this, this WIT interface as well, but again, I need to learn more about, this technology to understand if that would, like, work correctly, but, But yeah, I'll definitely take a deeper look at this, this issue as well.
Laurent Querel 00:12:59 So, to feedback on that, Albert, I think the… So, I'm not a WASM expert, but I know enough WASM to know that, The builder that you are describing?
It is not necessarily, does not necessarily require a WIT interface.
Because we can, so, it's not like every library Manipulating something neat to have a weak interface.
Because you have access to, to library, for example, let's say that you have a… a Rust, a Rust program compiled in Wesin, it could, it could use a Rust library to, To do some manipulation. So… I think before defining a WIT interface, if we do a WIT interface for that in the future.
we should make sure that we have the library very stabilized, because once we have a weak interface, It's like, put in the stone.
So that's one feedback.
And my second feedback is more for our own, And I think that's also what, Albert is thinking.
In my opinion, the first… Thing to do, and that's where the surface is minimal, or minimal.
is this one, because this one, I think we… we can take time, To refine the low level.
And I'm not sure that we are fully ready for… specifying, With a search interface, the low-level actions.
In my opinion, we take less risk by starting there.
And, and for… a WASM component, it's still super valuable, because they can basically construct an OPL, expression OPL program, for some specific needs.
And and then apply this transformation, on the fly.
Of course, feedback on my side.
But definitively super interesting.
Okay, so I think it's, fair to say that we, yeah, we… We need discussion, but, Definitively something on which we want to invest a lot of time.
Okay.
Don't hesitate to interrupt me if you have any questions on what we just discussed.
So, Siju.
Cijo Thomas (Microsoft) 00:15:48 I think this is something which I opened when you created the PR for adding documentation, where we were using different terminology.
I don't think there is anything immediately actionable, because I just need to look at the entire space and see if we have an opportunity to consult using a… Single type, because type is one, kind is very similar to that.
And we've been using this interchangeably.
So what I'll do is I'll take… now that the document is merged, I'll take another look at it and see if we can consolidate into a… Single name throughout.
Laurent Querel 00:16:27 Okay.
Cijo Thomas (Microsoft) 00:16:28 I'll just send the PR, and we can discuss it in the PR. We don't need to take up the live meeting for that.
Laurent Querel 00:16:35 Wicked.
Any feedback, from the… On there? On that?
Thank you.
Okay, so we have two, Kafka… stuff. Kafka receiver, Kafka Exporter, I'm not sure that Shanmi is present with us today. Let's see.
No. So I can, I can talk about that.
So we, we worked on a Kafka exporter receiver, on a private repo, and we decided, Wi-Fi, and we decided to contribute this, this effort.
To the open source project, so that's the result.
We already have, PR open on this, GitHub issue.
So what we… what we did is… learning from the Kafka receiver exporter from the GoCollector contribib, including also, some, other work in this space, like, what Rotel did, on the Cafica receiver exporter.
So we learned from that, and we… we tried, basically, to… to provide, Something that is covering the same kind of capabilities Learning from the mistake, and, and basically, so… generating those, new component.
So there is two open PR, I encourage for people that are interested by this topic to look at that.
So, that will not be part of the core nodes, but the country nodes, for now.
Any question on that?
Okay, Okay, so validation framework, again, certainly… So, for people that are not aware about the validation framework, So that's, basically, so we… Like, for the benchmark, we use a lot the engine itself to generate traffic, and then we have a system under test.
And, and we have a simulated backend. So for the validation framework, we reproduce basically the same kind of, infrastructure.
We… we generate traffic, the traffic is sent to a system under validation.
Which is basically the pipeline that you want to… to validate all a set of capabilities of the engine that you want to validate. So we generate traffic, send the traffic to this system under validation.
Then we have a special backend that will receive a copy of the traffic sent to the system under validation.
So if there is some comparison between the initial generated traffic and what is produced by the system under validation, the backend has this ability to compare to stream.
So, what we want to achieve specifically with this GitHub issue is… Basically, make much more validation and tests regarding the library configuration capability of the engine.
By level configuration, for people that are not aware of what that means in this context.
The, Arrow Dataflow engine support a set of, admin API that, Give the ability to an operator to create a new pipeline on the fly, to shut down a pipeline, to change the configuration of this pipeline, to add a new node into the the DAG to create a new group. The creation of a new group is not yet supported, but that's part of a PR, an ongoing PR.
So, we… obviously, it's a relatively complicated, stuff, so we need much more validation that we have. Now, we have a set of unit tests. Now, we want to exertite that, on a… A real stream, and, and, and doing that at different scale.
That's the goal of this, This, GitHub issue.
Let me kid.
Any question on that?
Okay, I don't know why this one is still there. Attribute processor handling valid transformation, configurations, optimization.
Albert Lockett 00:21:46 Oh, yeah, this is an old one. I think I don't know what to say about this, I think it's just something we should do. It's basically, like, if you define a bunch of, like, transformations in the attribute processor, we try and apply them all at the same time, and then, like, if you have, any, like, keys that are, like, overlapping between two transformations, we say, hey, you know what, like, this is gonna produce an ambiguous result, and we can't do it, right? And so, the workaround to be attribute transpulses, but we should just, like, fix that in the same processor. So, yeah, that was all that one was.
Laurent Querel 00:22:17 Brooklyn.
For now, I will skip this one, because it's part of the discussion we will have, just after the triage.
Engine structure cross-node validation, yeah.
drewrelmas 00:22:30 So…
Laurent Querel 00:22:31 We'll go.
drewrelmas 00:22:31 We had previously mentioned this one, if you scroll down to the bottom, we talked about it in a previous SIG. This is… Oh, okay.
We have to validate that the same ports aren't being reused across receivers.
And I had written down that we agreed in principle, but there were still some open questions, and I didn't leave more context, so I'm wondering, Laurent, if you remember what If you had any reservations about this, or it should be marked as accepted.
Laurent Querel 00:23:03 Let me see… You know what, I think my brain is limited, so I need to refresh my memory on that.
Utkarsh Umesan Pillai 00:23:15 Yeah, I can just give a very quick, reflection. Yeah, so this was mainly to avoid, scenarios where you have different kinds of receiver, like, let's say syslog and OTLP. Now, we should validate that these two different kinds of nodes are also not listening to the same endpoint.
All our validations currently just check either within node config or, like, nodes of the same type, but we also need, like, cross-node and, Yeah, like…
Laurent Querel 00:23:46 Yeah, I remember that.
Utkarsh Umesan Pillai 00:23:48 Even with, like, file-based receivers, we might have that issue where you have multiple file receivers trying to listen from the same, Indirectory, or, like, the path.
ETW receiver has a similar thing where the session name needs to be unique.
per node. So, there should be, like, a better way to validate these things at a higher level within the engine.
Laurent Querel 00:24:13 Yeah, I think I remember now, also.
One of the options to explore was to maybe… reify the notion of, ingestion endpoints.
That we could separate from the receiver, and then receivers can refer to an ingestion endpoint.
So the… An ingestion endpoint will no longer be just an opaque part of the config of the receiver, but will be something understood by the engine.
That we can easily, verify in terms of, uniqueness.
You see what I mean?
Utkarsh Umesan Pillai 00:25:05 Maybe we can…
Laurent Querel 00:25:06 And we can discuss that offline, but Yeah, I need to read that again. I will… I might maybe suggest an approach for discussion.
Utkarsh Umesan Pillai 00:25:21 Yeah, there's one suggestion that I had already left there, but yeah, I think there might be a better one, since you have more context about… on how the engine works.
Laurent Querel 00:25:28 Okay.
Utkarsh Umesan Pillai 00:25:29 Can do it, yep.
Laurent Querel 00:25:31 Great. So that will be also part of the… a discussion, a specific discussion, so I will skip this one.
And, that's it.
I don't know if LITT is there, I think so.
Yeah, okay.
lalitb 00:25:51 Yeah, so I just created this issue.
Today, so I'm still collecting my thoughts around this. Just to give a bit of background, like, currently we have a process-wide memory limiter Which works well.
As a final and an outer policy-based, out-of-memory safety guard.
But the gap is that it only tells us the… tells us whether the whole process is under pressure. It does not tell us which part of the process, like whether queue, topic, retry, buffer, a batch… the batcher, or the processor state.
Or a pipeline group is holding that memory.
So… so this becomes important for, at least for the multi-tenancy requirement, where we really want to identify whether a specific pipeline group or a tenant scope It's something which is attribute… which is… which is taking lots of memory, and we need… we need that attribution before we can enforce anything at that level.
We're kind of identifying a noisy neighbor.
So the proposal here was for a logical retained work memory budgeting. Like, we're trying to account the memory at the specific retention points, and attach that ownership to the retained work, and then move that ownership as that As that memory or data is moving through queues, topics, or retries, or the runtime boundaries.
Laurent Querel 00:27:26 Yeah.
lalitb 00:27:27 So… just some early thoughts, but probably my plan was, I mean, like, if this gets accepted, plan was to really come up with a better design, how we can really do that, and then start with an observe-only manner, and then use that model once we have a confidence To enforce the admission and the back pressure.
And keeping both the layers, the outer layer will still be there, which is a process-wide limiter, but this would be more of an inner layer, where we need a more micromanaged memory boundaries.
Laurent Querel 00:28:04 If.
Yeah, makes totally sense for me. The multi-tenancy support, and all the… Mechanism to limit… What a tenant can do.
We already have that for the… well, we could have that for the CPU usage. We don't really have a good solution now for the memory limit.
Except the one that you mentioned, global.
Fundamental work, definitively.
Highly supportive of that.
Okay, I think we can go back here and, start the discussion, so let's see, let's see, we have draw, alignment on duration, metric unit.
I think this one is already a bit short, so maybe, Drew, you want to start with this one?
drewrelmas 00:28:57 I think they're both relatively short. This is just something I wanted to call attention to. It's something that I… was thinking about as I was inspecting the GoCollector standard telemetry. Seems OTEL likes to standardize duration around the seconds, whereas a lot of durations in our code are measuring in nanoseconds.
So… Now, on some level, this makes sense for us, because, especially with how we're processing arrow, a lot of our durations are measured in the nanoseconds, so if we did something like seconds, we'd end up with very, very small values, or, you know, it might not make a whole lot of sense for us to do. So, I just wanted… this is specifically a discussion, not an issue. There's no active work planned here. I'm just curious what other people think.
It might be entirely valid to expect consumers of this data to do something like metric scaling, if they need it. So, I know, the Go Collector has transform processor that has a scale metric operator, where you can multiply values by a factor. So, we should think about… You know, this comes back to our internal telemetry pipeline, which we have today for logs, but for metrics, this could be a very real use case for someone wanting to consume our metrics.
So yeah, that's all I had to say about this.
Laurent Querel 00:30:29 Yeah.
Yeah, yeah, I agree, makes sense for me.
I think we can continue to work on the second internally, and having, some alignment.
When we expose that externally, Okay, in the…
drewrelmas 00:30:52 So, that… Christian one.
Laurent Querel 00:30:54 Back on that from others.
kennedybushnell 00:30:59 I think it's pretty normal for… metrics to kind of declare their scale, and for them not to need to match, so I think it's fine for us to pick whichever one we want, and then we let people… Scout them to the unit they want.
Laurent Querel 00:31:16 Yeah, I agree.
Okay.
drewrelmas 00:31:21 The other one was actually something, that I wanted to briefly mention, since Matt had expressed an interest in it.
A while back, we talked about how we're… the engine is automatically embedding… attempting to embed 3 resource attributes based on hosting platform, and also it's a little semantically incorrect, at least for host ID. So Matt was interested in, if you scroll down, he, commented, was interested in taking some of this up. He was thinking to use some of the upstream detectors in, our Rust and RustContrib.
I didn't necessarily see a problem with that, but since we have some, folks who are the Rust and Rust Contrib maintainers, I didn't know if they had anything they wanted to say about this.
Cijo Thomas (Microsoft) 00:32:18 I think it's safe, I don't think there is any risk. One thing to note is, none of them are stable.
The resource detectors rely on unstable semantic conventions.
So, especially the host ID, host name, none of them are stable, so the crates themselves would be… Utilizing themselves as unstable, which should be fine, but just something to keep in mind. None of them are, like, 1.0 great.
Laurent Querel 00:32:45 You know… For me, and I think it's pretty obvious, but just to make sure that we are on the same page, those detectors will… will not be on the outpass.
They will be part of some, initialization phase.
So, we don't really have… I think Strinder.
In terms of implementation, and Sync, the send, not send, and, whatever other constraint that could, be required to implement that. It's not a big deal in this case.
Cijo Thomas (Microsoft) 00:33:21 Yeah, it's usually only at the initialization time, it's not in the actual data flow path.
Yeah. So the fact that Autel SDKs are not, like, threat per core, it should not be a concern for this particular aspect.
Laurent Querel 00:33:35 Yeah, and in terms of detectors, Let's see… Because usually they… they are the common ones, like, Service, host, process, container, and things like that.
But, there is also things related to good providers… Azure, AWS, GCP, or technical platform like Kubernetes. Is it already something… are those detectors already supported by the, No, they don't have it.
Cijo Thomas (Microsoft) 00:34:13 Okay. Yeah, at least in the Rust, we don't have anything for the vendor-specific ones, like AWS or Azure.
thing that exists in many other languages, like .NET, Java, and Tool, but…
Laurent Querel 00:34:24 Which could be…
Cijo Thomas (Microsoft) 00:34:25 implemento.
Laurent Querel 00:34:26 So maybe we also need part of this, Of this effort, maybe, will be to see how that could be extended.
By third party, by pod providers.
So they… we could imagine that they have some kind of extension to describe How to detect the resources.
Cijo Thomas (Microsoft) 00:34:48 Yeah, so detector itself is the extension, so you can write more detectors.
So, the story.
Laurent Querel 00:34:54 Total.
Cijo Thomas (Microsoft) 00:34:54 is the extension officially given by Open Elementary to write your own custom the resource providers. So, they use the word, like, detect, it's more like resource providers.
Laurent Querel 00:35:05 Yeah, that's where, for example, the WASM effort on which Aaron is working could be extremely valuable.
We could have some WASM… plugin that are not on the Outpass, but used during the initialization phase.
to, basically to collect those resources, and because it's quasum that could be, link dynamically.
securely.
That will be a very nice candidate for WASM, I think, at some point.
drewrelmas 00:35:45 I see.
Laurent Querel 00:35:45 Oh, sorry. Go ahead, Sidro.
Cijo Thomas (Microsoft) 00:35:49 No, Andres has his hands up, so Andres, go ahead.
drewrelmas 00:35:51 Yeah, one of the images.
Andres 00:35:53 You know, I just wanted to mention that what I see, those are the detectors are mostly in the SDKs, but in the Go Collector.
They are just, parameters to the resources. So basically, when you load the application, in this case, the collector.
you pass whatever, you know, attributes that you want that are related to the resource. If you are running in a container, you can pass, you know, the attributes of the container, or if you are running in a host, you can pass maybe the host, you know?
Yeah, that's what I've seen in the GoCollector.
drewrelmas 00:36:28 I know we do have the freeform option, so you can… today, in the data flow, you can inject your own variables. So that part should be covered. This is more about the… Automatic detection of some other things.
But I guess users could… should be able to do one or the other, or both.
At the end of the day.
Laurent Querel 00:36:57 Yeah, and we can start with the basic one, for example, the… Environment, variable-based approach.
Which is a very simple.
We checked that both ones are there.
And if they are not there, then we can use, or we can override with, Detectors that are working differently, more dynamically.
Cijo Thomas (Microsoft) 00:37:22 One thing to note here is we just want to… I don't know exactly how the collector handles this.
If they did not take a dependency on the Hotel Go.
resource detectors, but something they maintained in the collector itself, and we may want to check, like, why they decided to do that, and probably adopt that. I mean, my immediate suggestion is let's not add the dependency to the Rust exporters right away, because, like, Joe, she's already planning on the removing OpenTelemetry SDK dependencies and hand-rolled our own.
Laurent Querel 00:37:57 Hmm.
Cijo Thomas (Microsoft) 00:37:57 internal telemetry system, right? So we want to, like, hold on until he's back and done with that work, because we may be, like, introducing a dependency which he's actively trying to get rid from another side. So at least to begin with, immediately, we can… Create them, like, in… like, code it ourselves, but just make it attachable, configurable.
And whether we take a dependency from the upstream repo, that's something which we can defer and make a decision after we are done with the ITS port metrics.
Laurent Querel 00:38:29 So, for tracking, Siju and Andres, can you maybe put your feedback there, when you have time?
Matt Wear 00:38:37 I'm just gonna mention, the collector handles this through the resource detection processor, which does take a dependency on the Go SDK, so it uses the detectors from the Go SDK there.
Cijo Thomas (Microsoft) 00:38:48 Okay.
Matt Wear 00:38:50 Yeah, it's a little weird and a different mechanism in that it's a processor, for some reason, But, But yeah, so there is precedent there, and then the other thing I was just going to mention is that some of the detectors that we would need don't exist in the upstream, so, I could contribute those to kind of Rust Contrib, just as a start, just so we have everything there, and then once… Once… you know, people have had time to think this over and, decide that we… that a dependency on the upstream is okay, then I could start the work on, on… the… the Arrow Collector, So, some prerequisites and stuff. Oh, go ahead.
Cijo Thomas (Microsoft) 00:39:39 Therefore, yeah, one thing we could potentially do is, right now, if you had added resource data from upstream Portal Rust.
it actually brings the entire SDK, because the source is defined as part of SDK, so it brings the entire SDK. So we could potentially do a trimmed-down version, which just defines the detectors without bringing the entire SDK. So we could add some feature flag to control which part of the SDKs are brought.
And since we have, like, enough people, like, working on OpenLelement radius, we should be able to make that happen so that the Arrow project can take a dependency on resource detectors. It will be a very light dependency. It won't bring the whole SDK, and we should be able to control that via feature flag.
So that's something which I should be able to help, like, not just me, like, Utkarsh, Lalit, there are all maintainers here.
So I'll leave a comment, and Matt, I don't know whether it's you, but I did see some PR in the Rustcon trip last day. It's you, right? Oh, okay, okay, so… Okay, yeah, so I'll leave a comment on what to do for the arrow immediately, and I'll also share my thoughts on how to make it as lightweight as possible in the upstream, so it will be much easier for us to take a dependency.
Laurent Querel 00:40:53 Great. Okay.
So, I'd like to talk about this one next, before Phase 3, because this one, is important, or some internal stuff for FAG, and I know it's also important for Microsoft.
I observe, Appear in this area, so we need to focus on that, so let's see.
We have… oh, sorry.
Yeah, that's his description.
So… what I'm trying to achieve here is… So basically, the engine that we are building can be used in a… standalone mode.
Or it could be undated into another… into another process.
And what we want to achieve is a set of extension points.
That lets people unbuilding those libraries, intervene in some important, level of the engine.
So in this specific situation, The goal is to introduce a new type of extension.
controller extension.
That will, give the ability to process unbending this, the defluent gene.
act on the controller API.
To, for example, create a new group.
Create a new pipeline, deploy it.
Take an entire configuration and let the… This, telemetry data plane, Implement the reconciliation, determining what needs to be added, what needs to be stopped.
or to be scaled. So that's the goal of this effort.
And, I know that, let's see, there is something… That is, in fact, a subset of that. I don't know if the person that welcomed that is.
sjmsft 00:43:01 I had created it, in fact, I had an agenda item as well. So, yeah, what I had… my issue was about extending the… the controller today starts with just the state callback, so I was going to extend that to include the metrics callback, but your issue seems to cover even a bigger.
Laurent Querel 00:43:20 Yes.
sjmsft 00:43:21 Full set of my requirements.
Laurent Querel 00:43:23 Yeah, exactly. So, I think we have exactly the same need in… so, yeah, so the… I don't know if I already have exposed, Let's see, maybe I have somewhere… Yeah, so the… So right now, we have an admin HTTP API and an admin client SDK that is used by the the DFCTL, Command.
And that could be used by… A controller by something else that is… that needs to interact with the telemetry data plane.
I want, basically, to reuse… under, like, under the scene there, under the wood, there is, beyond that, a controller API, so I basically want… To let an extension accessing exactly the same a controller API. And this controller API is already, supporting RT threading.
It's not on the outpass.
So we could have multiple concurrent, admin API that interact, basically, with the controller and the engine overall.
So, I will, there is, let's see… Where it is.
There is a TR right now, Which is this one.
So, I will implement that in two PRs. The first PR, still work in progress, where both operations are, now supported. They were not supported until now… So we, we, we can… After that, you will be able to start the telemetry data plane.
With an empty configuration in terms of groups.
The engine section in the configuration file will be there.
But groups could be empty in this… after this PR.
And that gives us a way to… Basically, start the engine and wait for instruction from a control plane to Deployer configuration.
And, something that is also now supported will be the ability to create A group, that was not supported before.
Until now, we were able to Create and redeploy a pipeline, but not create a new group.
And and also, I made a distinction between shut down and delete.
So when we have something running, we can shut down a pipeline, or a group of pipelines.
But, for observability reasons, a management reason, the, The footprint and the description of those pipelines that have been shut down.
We are still into the observed… the internal observed state that is maintained by the engine.
Which is nice, because obviously we can validate that something has been shut down properly, or if it's not shut down properly, for whatever reason, there is a set of conditions that could be, Collected, that will, help for troubleshooting, for monitoring, and so on.
But, the ability to delete such history is important, so that's what we… I added, here.
So once we have this, PR… ready that will give us, I think.
Most of the capability we need to operate dynamically A telemetry that's applying with all the… The group and pipeline concept, available for this Lyro configuration.
And the second will be just, will be a much smaller PR, where I will basically collect the same handle that, you collected.
So yeah, I'm very bad with first names, so your first name is, Samia.
So, basically, I will have, in this control extension, controller extension.
the $200 that you already had, defined into your PR, plus the… the controller API, And that will give the extension the ability to… Yeah, to do a lot of operation.
Any feedback on that?
sjmsft 00:48:33 Yeah, sounds good, like, yeah, so both the state and the metrics would be available in addition to even other control abilities.
Laurent Querel 00:48:40 Yes. Yes.
Okay, so, finally… Phase 3, I think we… we don't have so much time, but we will start the discussion on this, on this area, a little bit close, where… history. Okay.
So, Phase 3 is… it's… it's a proposal of, some important work that we think will be valuable, to explore and validate, to discuss also with the governance committee.
So that's… I don't think that we will cover everything today, probably, for the next, Sweet.
Oh, by the way, I will take this opportunity to mention that during the next 3 weeks, I will be on PTO.
But, Joshua will be there.
So, just very quickly, what we proposed right now, and it's not, necessarily fully approved.
pipeline-level control mechanisms… mechanism. So, we… we… we'd like to… we already discussed multiple things, on this, on this area today, things like tenant-aware resource.
governance, a full library configuration, so that what we just discussed, is already a beginning of that.
Some additional, inter-pipeline, based on topics. So right now, we only support in-memory, but, we'd like also to support things like, like, durable, or persistent topics, like Kafka, so the Kafka exporter receiver.
Could be reused also to implement such variation of the topics.
We… we'd like to… to do a second pass on the core components ecosystem, so as opposed to the Go Collector, where there is a very minimal set of core components.
The discussion that we already had in the past was.
We want to, basically improve the user experience for people that start to use this system.
And, we'd like to identify a larger core set of core components. So we already have things like, for example, us metric.
receiver, drone LED receiver, C-slug receiver. So that's the kind of very, very common, components And similarly, we have, also a set of, processors and exporters that doesn't exist in the core component set for the GoCollector. So the goal is to have something that will cover already, I don't know, 70, 80% of the The menus… the main usage.
And everything else, and that's why we won't… it's connected to this one. Everything else, ideally, will be covered by a WASM-based, Set of components.
or extensions.
So that will give us… that will, in my opinion, solve a big issue with the existing, approach.
Which require to recompile your perfect GoCollector with the right set of extensions, the right set of components.
It's a lot of friction for a new user, so… I think… A better defined set of core components, extensions.
And a way to, link dynamically, WASM-based component extensions.
Will, prevent people to… to have to recompile, and still providing a lot of, security guarantee.
So that's the… A direction that we like to discuss with the governance committee.
And we also have, especially for the processor, where, there is a multitude of processors in the current, collector contribid.
Portuguese.
That address a very small… Set of transformation, filtering, or enrichment.
And we really think that, the effort that we are, on which we are working with OPL, and to some extent OTTL, all based on the same, processing engine.
We'll address most of those, small component. We can already, do a lot with, OPL today.
Covering the transon processor, the attribute processor, and multiple other things.
That's something we'd like also to explore.
What's we… We've shown during the… this, SIG, Spec SIG meeting was to demonstrate that having What's up?
I think when I say end-to-end, it's not purely exact, because end-to-end means that from the producer, so any application instrumented with an SDK, to the backend, we have OTAP. That will be the… the perfect, end-to-end OTAP approach.
Where we will be able to leverage all the benefits.
Today, we don't really have a pure OTAP SDK.
We can simulate that, and that's what we do, because we reuse the engine in with a different role, we use the engine as a producer, like an instrumented application.
But we don't really have an SDK, so that's also an exploration. I think CGO is interested by that.
Obviously, an important aspect of Phase 3 is, discussion with the governance committee, and see How we can make, this, work.
are well aligned with existing systems, like the GoCollector, and how… what will be the best approach to make that smooth, and… And not problematic for the community in general.
And, yeah, also things like, being, involved into the OpenTM3 demo.
the blueprint effort, again, that's something that, Siju added.
That, is, I think once we have this discussion with the governance committee, it will be extremely valuable.
open 10DP profiles, so the… that's the… The new signal type, that has been introduced, Recently.
That we don't support yet for that.
That could be also part of the goals for Phase 3.
I slowly and collagenly went to, To add additional comment there, if you have some other ideas, concerned with, those, specific point.
I think that that could, that could be the… The place where we can distribute.
Any direct feedback?
drewrelmas 00:56:51 I see Joe, you have your hand up.
Laurent Querel 00:56:54 Oh, sedar.
Cijo Thomas (Microsoft) 00:56:54 Not a feedback, Jack, just something which I wanted to share. For the core component ecosystem, the collector, SIG has done an extensive survey in the past to figure out what they really want to stabilize.
in the first version of the collector, so they have already the data and results to determine what components are most used by the ecosystem, so we can just piggyback on the same result and use that.
Yeah, so just a comment, not really a… something to.
Laurent Querel 00:57:24 Yeah, yeah, I remember that you shared this, document in the past. If it's a public… I think it's a public document, right?
Cijo Thomas (Microsoft) 00:57:36 It's actually a GitHub issue.
Laurent Querel 00:57:38 Okay, so if you can add maybe the link to the GitHub issue here, that would be useful.
Cijo Thomas (Microsoft) 00:57:42 ugly.
Laurent Querel 00:57:44 Thank you.
Cijo Thomas (Microsoft) 00:57:46 And one… another thing to note here is, I mean, as soon as the blogs are out, like, more people know about it, I'm pretty sure, like, people would want to contribute.
their own, exporters or other things, so it would be good to take a formal position. Are we going to accept them, or are we going to, ask them to hold off? Because Collector pretty much kept the gate open to the country repo, and It's too many components that force them to now put more safeguards, and they have a very high bar now to get new components, so we don't have that problem right now, but we can totally learn from what.
Laurent Querel 00:58:27 Yeah.
Cijo Thomas (Microsoft) 00:58:28 went through, so maybe, when we announce Phase 3 start, we can make a formal announcement saying that we are open to adding more components, or we are not open, like.
Laurent Querel 00:58:39 Yeah, that's definitely something we need also to… Yeah, discuss between the maintenance, defining this posterior One thing for me that is sure, And it's already announced into this blog post that is not yet published, but will be very visible.
we don't commit today on any stability in terms of APIs, and that's also true for the for the API of the component, like receiver, exporter, processor, and so on.
So, if people are willing to contribute, for example, a new exporter, they have to accept first that maybe tomorrow, they will have to fix their component, because the… It's no longer working.
Cijo Thomas (Microsoft) 00:59:32 My concern was slightly different, I just want to make it clear here. So, let's say someone comes, contributes an exporter, we host it in the repo.
And then we change the, like, core API. Now, at that point, the exporter, whatever is the component, they need to be adjusted. So the question is, like, who owns that responsibility? Because if you're…
Laurent Querel 00:59:53 I agree.
Cijo Thomas (Microsoft) 00:59:53 whoever makes the original PR will be forced to do that, because otherwise the PR won't even merge.
Laurent Querel 00:59:59 Hmm.
Cijo Thomas (Microsoft) 00:59:59 what prompted most reports to spin off to a separate report. So the phase one, like, you make the changes to the core, and then as a separate PR, so we'll need to, like, figure out some logistics. We don't need to solve it right away, but, just something to keep in mind.
Laurent Querel 01:00:14 I agree. Yeah. Okay. Yeah… We are at the end of the hour. Thank you so much, guys.
And, see you in 3 weeks, or 4… yeah, 3 weeks.
drewrelmas 01:00:32 Alright, enjoy your time off, Laurent.
Laurent Querel 01:00:34 Bye, bud. Bye.
drewrelmas 01:00:36 Bye-bye.
