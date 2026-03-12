SIG: Profiling WG
Date: 2025-08-07
Duration: 68 minutes
============================================================

## Zoom Recording Transcript

Antoine Toulme 00:03:58 Hello!
Florian Lehner 00:04:12 I think Felix and Alex will not try today. Anyone want to cheer or volunteer for leading the meeting.
Christos Kalkanis 00:04:28 Yeah, I can take it.
I'm just opening up the headset.
Okay, so hopefully, you can see my screen.
Alright. So let's let's review the action items first.st I didn't. I missed the previous Sig. I had a hospital visits.
So, Florian, the 1st one is yours.
I think the this pull request has been approved.
No, okay.
Jonathan Halliday (IBM) 00:05:27 Yeah, those those 1st 2, both mine. I think they're waiting on spec sponsors, not on profiling people.
Christos Kalkanis 00:05:37 Yeah, so this has 3 approvals.
Jonathan Halliday (IBM) 00:05:42 Yeah, we need Joshua Tigran, but not good to go. I think.
Christos Kalkanis 00:05:48 Okay, I mean, I know. Felix looked at it, and Alex as well like, maybe it would be good to have 1. 1 more approval from either Felix or Lexi, but
Florian Lehner 00:05:58 Yeah, I talked to Tigran and he asked to look for at least 2 approvals from profiling sick maintainers. So that's Felix Christos, Jonathan, and Dimitri. I think in on this Pr. We only have one so far.
but as Jonathan is the author. He cannot approve itself.
Christos Kalkanis 00:06:29 Okay. So essentially, we're waiting for Felix to approve this right?
Florian Lehner 00:06:32 Yeah.
Christos Kalkanis 00:06:33 Okay.
Jonathan Halliday (IBM) 00:06:36 Think.
Christos Kalkanis 00:06:38 What a problem.
Jonathan Halliday (IBM) 00:06:43 So the reviews required thing says 3, but only one of them is a profiling maintainer. That's where the problems coming in what Github requires, and what people who are running Github requiring not the same thing.
Christos Kalkanis 00:07:01 Yeah.
Well, I think the the second requirement, I mean we we it could be depending on on pull request. Right? If it's something extremely simple that all of us have discussed before then.
Yeah, I guess it's up to dig around whoever has authority to manage the pull request. But I don't think like this. I'm pretty sure we all discussed it right. And we we're on the same pace. That's the consensus.
Jonathan Halliday (IBM) 00:07:28 Yeah, I think that's just to get them.
Christos Kalkanis 00:07:30 Alright!
Jonathan Halliday (IBM) 00:07:31 That Felix has looked at it, but I don't think he's re reviewed it since.
Christos Kalkanis 00:07:35 Yeah.
Jonathan Halliday (IBM) 00:07:37 Went through his comments right.
Christos Kalkanis 00:07:41 Okay, so.
Jonathan Halliday (IBM) 00:07:46 Okay. I've just shifted in back to pending.
Christos Kalkanis 00:07:54 Okay, that doesn't work.
Okay, I'll ping Felix and on slack so, or maybe I can. We can add a comment in the pull request, just asking him to take another look.
Nayef Ghattas 00:08:05 Yeah, I'll ping him and tell him.
Jonathan Halliday (IBM) 00:08:06 Yeah, he's on vacation, isn't he?
Nayef Ghattas 00:08:08 Yeah. He's on Pto until next Monday.
so he'll be back next week.
Christos Kalkanis 00:08:16 Okay? And then the second one of Jonathan's pull request is this one? I think.
yeah. The same thing is is the I mean has approvals. But this is me, I think, from maintainers. So Felix and Alexey haven't looked at it.
Okay.
alright. So let's you know. I'll ping people separately and hopefully. Yeah, we can make progress. I think both of those should be met soon. I don't think there's anything left to discuss the second item, we don't have Alexa with us so we can skip it.
Review my benchmarks.
which are here. So those are related to the pull request that Felix opens about the simplified stack representation which is here.
So that's another one of the open. Pr's that we have that needs to get merged. Because, yeah, it's making yeah. And up, it's semantic update to the protocol. And it's holding back some work, a follow up work that we need to change the logic in the in, at least in the agent, also in the collector.
So we've also discussed this. I think we we have consensus so Felix has summarized some of my benchmarks here.
Now, if if anyone wants to take an extra look, please feel free to to do that. Because otherwise we're going to miss this. I think that's the that's the consensus.
And so.
like, I ping Jonathan earlier today on slack. And yeah, he told me that he's fine with this Pr as well. There's just one remaining item for Felix to do, which is, he needs to revise the Ascii diagram that we have at the top of the profile to take into account the new stack methods that she introduces.
But other than that, I think again, we're on the same page I think, in the in the previous previous zig. Alexi also mentioned that he's okay with this. So so this is kind of a last reminder that if if people have concerns about this approach, then yeah, you need to raise your concerns because this is getting messed.
Okay? Moving on, Florian. Add some position attributes to open telemetry.
Florian Lehner 00:10:49 Yeah, so we do have 2 different places there.
One on the protocol side. This is this one, this now merged, or yesterday yesterday morning this morning.
sometime, and to keep the compatibility with people, we have to add elements into the semantic convention.
Not only for the memory mapping mapping message, but also for message location. So this would be just the next topic. And and next, active action item.
And yeah, these are the semantic conventions that keeps us compatible with Pprof, so that we can convert back and forth.
Yeah, please take a look. Praise your concerns.
The problem with semantic conventions is that we cannot treat them as enum so that we cannot say Hi, if you have has the field name and has field name has file name. Sorry, and has line number if these both attributes are set, then merge them together.
we have to work around that we have 2 dedicated attributes for this.
That's unfortunate, not the framework we have to deal with semantic conventions.
The problem for us is not that, big as we can. As we put the attributes in the attribute table in the Profiles dictionary, and reference them always with an index, so we will not have an overhead with this additional attributes.
But yeah, to keep the compatibility and allow us to transform people to hotel profiling and vice versa. Please take a look at the Pr.
Daniel Schwartz-Narbonne [Datadog] 00:12:56 So just a question here, cause I'm so. Things like the build. Id would now be as a semantic convention rather than part of the mapping.
Florian Lehner 00:13:05 Build. Id was always part of the semantic conventions.
Daniel Schwartz-Narbonne [Datadog] 00:13:10 Okay.
Florian Lehner 00:13:13 That's build id. It's not part of this not this pr, but we build id. The semantic convention, semantic conventions for for build. Id was merged, I think.
half a year ago something like this. So for some time already that's why we don't have any more. The field build id and protocol.
That's the very same we do now for the Boolean fields. The Boolean fields now got removed from the protocol, and we have to have the very same features, basically. And semantic conventions. So it's a shift to a different.
Jonathan Halliday (IBM) 00:13:55 So doesn't that Pr. For the semcom need revising.
Florian Lehner 00:14:02 Revising
Jonathan Halliday (IBM) 00:14:03 Well at at the moment we would have to be able to have a list of values.
So if more than one of the Booleans is set.
There would be multiple items in the list. And I think that's not allowed. That's what the conversation is saying.
So, instead of instead of defining one attribute that would need to have multiple values. We need 4 attributes of type. Boolean.
Florian Lehner 00:14:37 I see your point. Yes and no.
There is no general field of an Boolean attribute in semantic convention, as far as I can tell.
And we we could say, Hey, there's a Pprof attribute for mapping, and the values can be has file name has line number and the others wants.
And No! What was the conflict? There's a conflict somewhere.
At the moment. We have to have 4 attributes, or you have to set 4 attributes. But the overhead is minimal, as I said, as these attributes will end up in the attributes table, and we just use an index to point to these attributes.
Does this make sense, or am I on the wrong path.
Jonathan Halliday (IBM) 00:15:41 Well, when I when I look at the actual Centcom Docs.
Florian Lehner 00:15:46 It doesn't seem to be defining 4 attributes. It seems to be defining one which is called profile dot people off dot mapping passport.
Jonathan Halliday (IBM) 00:15:54 Possible values.
Florian Lehner 00:15:56 Yep.
Jonathan Halliday (IBM) 00:15:58 And you can only have one of those values at a time, because you can't have a list of values.
Florian Lehner 00:16:05 I think we can. I think we can set the same attribute key with different values.
Jonathan Halliday (IBM) 00:16:15 I think, in at least in the SDK model. It's a map semantics. You can't.
Christos Kalkanis 00:16:23 Yeah, that would be. That would be a problem.
Florian Lehner 00:16:27 Yeah, makes sense.
Antoine Toulme 00:16:35 Asking about the attribute values for resources or anything.
Christos Kalkanis 00:16:43 The question is, can we set multiple attributes with the same key?
It's because we can. Okay.
Antoine Toulme 00:16:49 It's not really you can. It's like the the type of the attribute can be of type array. In that case you can have multiple values.
Jonathan Halliday (IBM) 00:16:58 No, the conversation there is saying, you can't do that.
Antoine Toulme 00:17:02 Okay.
Jonathan Halliday (IBM) 00:17:02 You can't have an enum array.
We we just want to do students, do we?
Antoine Toulme 00:17:09 That case you need to have a.
Jonathan Halliday (IBM) 00:17:10 Rely on these, just rely on the semicond for the strings.
Florian Lehner 00:17:15 We could make it a string, or we could make it an array, and.
Christos Kalkanis 00:17:23 We could make the narry so profile, mapping.
Florian Lehner 00:17:27 Profile. P. 12. Mapping could become an area that you can then set has function, has file name, has line numbers, and has inline frames altogether.
If does this? If this does make sense.
Jonathan Halliday (IBM) 00:17:49 I don't think it's a huge deal at the SDK level. If they're not enums.
I mean strictly, they could still be enums in something like the Java SDK, and we can just rely on the exporters to convert them to strings.
Florian Lehner 00:18:03 No, I I would love to have a you know that would make things easier.
But I don't see the way how we can achieve this.
Jonathan Halliday (IBM) 00:18:12 Yeah, alright. Let's just go without disease. Then.
Florian Lehner 00:18:16 So I will update. Then the Pr to use array for the profile. Pdf, mapping so that we can set multiple has functions has file names. And whatever does this sound fine for everyone?
Jonathan Halliday (IBM) 00:18:33 Yeah, that sounds great.
Florian Lehner 00:18:34 Okay, yeah, put those up.
Christos Kalkanis 00:18:44 Okay, Florian. The next one is yours, too, I think.
Florian Lehner 00:18:49 It's the very same, just for a different message. Type.
Drop location. Here. We also have the Boolean and the protocol.
So remove the boolean from the protocol and have a semantic convention.
As a as it has as is folded is just a single value. I think we don't need the same like, we not decided for the mappings.
Yeah, that's that's it. So very safe.
Yeah.
Christos Kalkanis 00:19:25 So regarding the non semantic convention. This has all the approvals, I think, Jonathan just being. And Josh, so I I expect this to be merged because both Alex Jonathan and me have approved it. So there's nothing else to do that. But on the somatic conventions one.
let me see.
Florian Lehner 00:19:47 Yeah, somebody mentions. I will update the Pr and then let you know. At the moment.
it doesn't make sense.
Christos Kalkanis 00:19:55 Alright, alright, okay.
Okay. The next item is from naive. So that's context propagation proposal.
Nayef Ghattas 00:20:11 Yeah, I think Elsa has prepared something to share.
Elsa Keirouz [Datadog] 00:20:14 Yeah.
Hi, do you mind if I okay, great share my screen? Thank you.
Alright. So you should be seeing my screen. I need to move the zoom widgets from here.
Okay.
right? So, I think it was end of June. I attended one of these meetings, and we presented a document about context propagation for the Ebpf profiler. And so at the time there was a discussion after I presented it, and we were asked to split the documents into 2, 1 regarding process level information and one for thread level information, and then also present some use cases for both.
So we did that. But to preface the new versions of the documents. We also wanted to talk about resource definition and the Ebpf profiler. So basically, right now, in hotel Sdks, like traces, metrics and logs, we are able to configure resources through environment variables, specifically hotel service, name and hotel resource attributes and also through the code. So right now, the Ebpf profiler does not really take that into account. So the way that it's going to configure resources is it's going to create one resource per container, and then one resource, for, like one common resource for all non containerized processes running on the host on a given host and so and so that's defined in the specification. And we'd like to modify this in order to align with the sdks and So we would in that case have one resource for each unique set of resource attributes, and that is going to be useful for creating resource oriented views like more specifically a service level view, for example, and so that will allow us to keep the views and the data consistent across all different signals for a given service.
So this document specifically goes over how we would like to do that. And why we'd like to do that for for resources that are defined via environment variables. So specifically the 2 that I mentioned a minute ago. But we wanted to so to ensure that we are aligned on the way that resources are defined across all signals. We also have to find a way to share that data when the resources are defined in the code directly through the sdks. So for that. So that comes back to the idea of process level information that I had talked about last time.
And so we are like, we view resource attributes such as like the service name or the deployment environment as process, level information that can be ideally collected once, but that can be in certain situations updated during the process's lifetime.
And we are proposing a way to share those through the S from the Sdks to the open telemetry. Evpf profiler so this would be specifically useful to again have consistent across signal views within open telemetry, but more specifically for being able to correlate data without needing the span span level information or without needing sample based correlation. Specifically, we're proposing to use the service instance, identifier resource attribute to do that.
I go into more details about why? Why that is, and why we think this is this is useful in the documents. I'm not really gonna go into much detail now, but you can consult it, and if you have any questions we'd be happy to answer afterwards.
And also it can be useful for sharing the version of the protocol that we're using for thread level context propagation. This has been done. And so proposals and contributions done by elastic. So an Apm interpreter, and through Parka's lip, custom labels a proposal to. So they. But they share it through a global variable which we don't think is optimal. Because, well, 1st of all.
we're going to need to parse all of our elf symbols in order to find the global variables. There are certain situations when we're dealing with the static binaries where we won't be able to. If the if the binary is stripped find that global variable. So there are a few issues with with that approach. And so, as an alternative, we're proposing to use anonymous mappings.
since well, 1st of all, we won't have to deal with any issues regarding strip binaries. It would also be more straightforward in order to find the mappings and also potentially to identify mappings that are created dynamically during runtime. So like for delayed, delayed, and instrumentation startup, for example, and also creating a mapping mainly requires a map most of the time. So we're not like, it's going to be much easier to have support for that in most of the supported runtimes.
So for that, we're we're proposing some 2 identification mechanisms which I can go into detail. But we can also discuss that later, if you want and yeah, just depending on the sort of features that are available to us in the environment. How we can identify those mappings which ideally we'd be using named anonymous mappings, because that's the easiest way to do it.
Yeah. And yeah. Finally, like, the document goes over some rejected solutions. We had a few last time. But then it was someone, I think, during the meeting suggested using environment variables. So we looked into that. And basically, we document, why we don't agree, and why we don't think it's a great idea for environment variables and other other solutions potential solutions which, yeah, you can also consult in this document.
And yeah, I there's 1 last document. But I don't know if anyone has any questions right now. Before we move over to that.
If you do feel free to ask them.
Florian Lehner 00:27:43 We had a discussion on slack already. Did Josh reach out to someone about the direction hotel is going, because he wanted to share something, and it was not clear where and if he was sharing it.
Nayef Ghattas 00:27:59 Oh, yeah. So what he want? He did not reach out personally, but I did look up the docs of the initial thing he shared. And essentially the open telemetry community is changing the slightly, the concept of resource to introduce entities and allow telescoping between different resources and essentially on a high level. How will this impact us is that the environment variables that we're going to use will be slightly different than the ones that we added in the document when this will be introduced. But this is still very early, from what I understood, and there's no complete documentation yet of the effort that they're that they're working on so.
Florian Lehner 00:28:40 Okay? Then I think my critic in slack still remains. The I speak speaking especially for the Evp profiler.
It's deployed as a demon set, so it has a few to various environments and a closed environments other than every other hotel resource, like blocks, traces, and metrics. And so the 1st document writes, Hey, we want to have only these 2 environment variables as a resource, and then then the resources will be a little bit more, but I think that's manageable.
But the second document that was just shared with the mappings for the process level then tells, hey? We want to have every resource attributes on, on this, on this, on this element, and then everything will explode, and this will not scale with the protocol. I think the issue we here face is that And we had this discussion already. Before that we agreed in the past that on the resource level we have the demon set attributes for for the host.
and on the on the sample level we keep the more precise resources. I see the struggle with mapping resource attributes that are attached to samples with existing hotel infrastructure one approach could be that we can say, Hey, if there are multiple resource attributes in a profile.
This means we have complete view on the system and maybe on processor auto processor can be used to later on. Split them up and say, Hey, Split this profile up into multiple other profiles and then split them up in a way that you can dedicate, have dedicated enclosed entities and moved resource attributes from message sample to the resource level, so that only a single resource will be in the protocol.
Otherwise, otherwise I think it will be hardly possible for the back end to differentiate at a case where the source that sends something to a backend comes from a demon set or a sidecar.
and looking at people, for example, as a as an example it usually will come as a sidecar.
or if the profiling is used from an SDK point of view, then it's also you more likely to become as an sidecar and not have multiple resource types in the profile. Does this make sense in some way.
Nayef Ghattas 00:31:46 I'm not sure I completely understand why you're saying that supporting all resource attributes will explode the number of resources, because essentially my understanding of the definition of a resource in opentelemetry is that it is the instance that is emitting the data. So even if the opentelemetry Vpf profiler is running as a demon set, as you mentioned on the host. The instances that are emitting the data will be individual containers most of the time.
and so, even if we supported both of the suggestions in the general case, we will still have one resource per container. But instead of having one resource for the entire host. We could have one resource for the entire host. If nothing is configuring those resource attributes on the process level individually. But we could have more if people are going to configure them. But I think in the general case we could also recommend that people configure them on the processes for which they care specifically to have observability, so I don't know if they want to have it on. I don't know. System d Journal D, or whatever processes they they would want to split into specific resources, but that would give sort of the option to the, to the user, to set and define what a resource is which is the option that is given also to them in the open telemetry sdks and the different other signals.
Does that make sense? Make sense.
Florian Lehner 00:33:19 Yeah, I have a little bit of different view on resources. If I look into the semantic conventions, I posted just a link into the chat. Then there are quite a number of resources, and if I look into the process, for example, every sample will have some kind of process information process, name process executable and if these are attached and and that's just the next basic step from your from your suggestion, then this will.
The cardinality of the data will just explode.
Nayef Ghattas 00:33:57 So generally, my understanding is that process attributes are not generally attached in the Sdks traditionally, and they're more handled for telemetry, that is, that is running on a host, and that is sort of scraping the data on a process level and sending it by process and a process resource.
So when you are instrumenting. And and this is why they are introducing the concept of telescoping resources. Because you, you see that in those definition of resources there are various levels of different different sort of how how to say that different focuses, different zooming zooming in levels? I think in in most cases. What we're going to have in the Sdks is the service name service instance Id. So it will most of the time map one to one with the container, because it will be defined on as an environment variable or directly in inside of the code of the service as resource attributes.
Does that make sense.
Antoine Toulme 00:35:12 That makes sense.
Christos Kalkanis 00:35:15 So to to summarize a little bit and to check, if my understanding is correct. 1st of all, like the the thing that, like I'm most interested in 1st was to figure out if the if this proposal like all 3 parts require changes to the protocol, and my current understanding is that it doesn't. We're only changing the way we group resource profiles together. We're making it more flexible in a way, right? Because right now the grouping of resource profiles is fixed, depending on a host of containers.
and you're proposing to add degree flexibility there make it configurable essentially, either through those 2 environment variables, or through the your second document here, which goes into essentially more flexibility.
And then it's also opt in opt in right by default. If if it's up to the user to configure this grouping in the way that he wants right?
Nayef Ghattas 00:36:05 I think it's we're proposing to do that by default in the opentelemetry Bpf profiler for the environment variables that the SDK opentelemetry SDK support.
Christos Kalkanis 00:36:16 Right.
Florian Lehner 00:36:18 But this would require a change in the protocol.
Nayef Ghattas 00:36:21 And yeah, this would be the change in the it's not written in the. It's written in a comment, I think in the protocol that this is how we handle resources. Yeah, the comment that Elsa is highlighting. So it would require a change to that comment.
Christos Kalkanis 00:36:34 Right? Okay? But that's not the change of the protocol. We're only changing. Yeah, the the the comment. Essentially, yes. Yeah. Okay, so no structural changes to the protocol. Okay.
Nayef Ghattas 00:36:45 No, but it does require changes. On the open 10th Gbpf. Profile.
Christos Kalkanis 00:36:49 Yeah, yeah, because it needs to change the way it does grouping, right? Because the model it uses now is not gonna be the same. Okay.
Nayef Ghattas 00:36:54 Yep.
Christos Kalkanis 00:36:55 So like I I read the 1st document. I mean, I like the flexibility. So you know I do like the the general idea on the second document, like what I would like to see is an example, just one example of of how like, just give me an example of the the process level attributes that you have in mind, and you know how this would work like the the resource profiles would create just to make it easier to visualize. And I think maybe you also have Florian.
Because right? Yeah, right right now, it's not immediately obvious.
Nayef Ghattas 00:37:24 I think we added an example of one resource attribute we wanted to have, and specifically the hotel service instance. Id.
So service instance Id is a way to uniquely identify an instance of a service service being in the tracing Apm sense of a resource. And so this is a unique identifier that's generated by the SDK, to say that this program that is running right now is uniquely identified by this Id.
and so it allows more easily to be able to do correlation between the different signals by using this Id on the profiles and this id on the traces, logs, metrics, where it will be always present instead of relying on clunky heuristics that will try to find the deployment name the pod name, the container name, depending on the on on how the customer and the resources is deployed. Does that make sense? Or should we like also include more different examples.
Christos Kalkanis 00:38:22 It makes sense. But if there, if there is another example, that's more so, yeah, what you just described is like it comes across is very simple, right in terms of the implications. But if there's a more complex scenario like, you know that you have in mind that would be nice to like the worst case, basically, right?
So if there is a worst case.
it would be good to to have an like an example that captures it in the document, so that we can better understand the the implications.
Florian Lehner 00:38:52 But.
Christos Kalkanis 00:38:53 Yeah. So that said, I haven't like went through the second document in detail. So I haven't actually reviewed this. I wanted to for the previous sake, but unfortunately I had the health thing, so I had to to skip it, and also the meeting.
But I will definitely do it for the for the next meeting. I'll go through it in detail, and probably leave comments in the documents.
Florian Lehner 00:39:15 Yeah, I will just continue this. I I like the approach with the mappings.
That's sad. One thing I'm missing is that the communication between the SDK and the evpf. Profiler for this communication the mapping is used, and that's the way that we are using a mapping. I'm I'm a fan of this.
What I'm missing is we probably need some kind of specification, so that the SDK and the profiler speak and read the same and while on the profiling side we can say, yeah, we like this, approach.
I think we need some buy in also from the from the SDK side.
I think to start with one SDK would be fine. So either go or Java.
But yeah, yeah, I like the approach. I think in the end it should be a good replacement for Apm. And yeah.
Nayef Ghattas 00:40:18 Yeah, just add a small bit there. We're definitely planning to so the way we were thinking about this is discussing this within the profiling sake. If that makes sense for profiling, to ask for this sort of capability from the Sdks, and then we're definitely going to reach out, and we will, for both process, level and thread level attribute sharing. We'll definitely need at least approval from 2 big languages like Java and go. Maybe maybe python as well, and then see if if this approach can be extended to all the sdks.
Florian Lehner 00:40:57 Yeah. Yeah. Sounds good to me. I I would love to see this as a successor to Apm, and.
Christos Kalkanis 00:41:07 Yeah, there's nothing here also for anonymous topics. If I remember correctly, 2 years ago, maybe even longer. We also discussed this internally as a possible way to to transmit information so.
Nayef Ghattas 00:41:24 Yeah, if you have any like sort of conclusions or summary from from those discussions, I think I think that would be helpful.
Christos Kalkanis 00:41:32 I think the the conclusion at the time is that we took Joelle took like a different shortcut thing, which is simple to to implement.
but the whole approach at the time was more like a hacker. 1st of all, we wanted to prove the concept until we wanted to come up with a Java implementation in the softest possible amount of time. We weren't trying to make something generic that's going to work for other cases as well.
which is obviously not the case here.
and one last question to you as I and and I have so we we're aiming to get a release candidate one out by the end of August. I don't know if that's gonna happen it's also with people being on vacation and so on. But I think it's it's a good goal to have. And we have a list of things that like button items.
So this, your proposal is not in the burn items list. So it's not in the list of things that we absolutely must. You know, take care of before the release can be one. Is that so my understanding is that you're not pushing for this to to be part of that right.
Nayef Ghattas 00:42:31 No, we. We don't think, especially as you said, that this will not require changes beside the little command, change on the on the protocol.
Christos Kalkanis 00:42:40 Okay.
Alright! Anybody else have any comments?
Alright. So then I think we can. Continue.
Elsa Keirouz [Datadog] 00:43:04 Yeah. Right? So the last document isn't really a proposal. It's more wanting to like. The aim is to kick, start the conversation or the discussion around how we wanna share thread level information.
So that can be used for a trace to profile correlation based on span and trace ids, and also to potentially share custom attributes like what was done with go and what is proposed through the custom labels parka parka solution. So that's what it would be used used for. And so we sort of just looked into the prior art that was done, and that was proposed and and contributed, and went over the solutions and sort of did a analysis of what the challenges were for each one and and what we think of them. The problem with thread level in general is that it's going to be a bit tricky to find one solution that's going to work for all programming languages. Because we, I mean, a lot of languages have complex concurrency models that are really specific to them. And we don't always have the ability to share data at the thread level like using thread local variables, or the way that it's done and go through a Prof labels. We don't always have access to solutions that are specific to the language. And so we're just we, we just essentially want to gather feedback on and not just feedback, just like opinions on what?
What direction we should go in. And yeah, how we can move forward regarding sharing that that kind of information.
Nayef Ghattas 00:45:09 Maybe one very super quick thing I wanted to add is that both existing solutions that I think, were contributed either to Java or in native. They both require native bindings and native library. So we're also curious to know if there's been any discussion with the hotel sdks on having native bindings and sdks.
Because, yeah, we want to know if this is something that could be feasible and possible to have generally across different languages, or whether this is not. And yeah, we need to think of something else.
Christos Kalkanis 00:45:55 So I guess Josh might be might have some useful input here. But Josh is not here today. Right? Yeah.
Nayef Ghattas 00:46:06 Yeah, we can reach out to him, Async. Then.
Christos Kalkanis 00:46:11 Okay, yeah, thanks. Thanks a lot for putting this together. By the way, this is great. I mean all the documents don't have anything value to add to this. I haven't actually gone through this at all, but it's it's super useful.
alright.
So I think, with the that's it. With the action items like, if we go to the agenda. Felix is not here.
and we don't have a lot of time. We have 15 min left. I think we can skip Felix's for next sig. And then, Francesco.
you have a question around sample type. Like Florian gave you some pointers here do we have Francesco? We have.
Francesco Andreuzzi 00:47:15 Yes, this was clarified online. Thank you.
Yeah. The comments I received from florin are more than enough to solve my my problem from now. Thanks.
Christos Kalkanis 00:47:27 Okay, great.
Then Josh is not here either. So I guess we can. We can skip this, and then no one.
Antoine Toulme 00:47:36 Hey? So about 2 months ago I asked a few questions on slack, and I tried to do an implementation of a people receiver which would be a collector country receiver. With the idea that I would be able to leverage the people off to people conversion, and it did not work as we had multiple discussions about it. We had a lengthy thread on slack about it. Also have a pull request to show, and there's set of comments on it that kind of show where where we are.
So here's simple, simple thing, right in the slack thread discussion that I had with Alexei. He mentioned that the mapping between Prof. And p profile exists and is maintained, if not loosely.
from the spec point of view.
I would like us to consider having an actual test like a Ci test that runs that would check that the portal files that the the conversion is possible.
And I asked at the time, in on slack, where to file this type of issues and how to go about this? Where is there a repository where this type of test should live. Is this a open telemetry portal discussion, or is there another place where we can do this?
Because the closer it is to the spec the better off we'll be otherwise we cannot. We cannot say that we map to people at this time, because it's it's not the case. It's not possible.
Christos Kalkanis 00:49:12 And may have.
Nayef Ghattas 00:49:13 Yeah, if I'm not mistaken, I was going to say that I think there is one action item for Alexei, who was working on this.
Christos Kalkanis 00:49:21 Yeah, we decided to create a repository.
that's going to be essentially ours. We're gonna be managing it. And I I missed the last meeting, so I'm not sure if there was any updates on that.
Antoine Toulme 00:49:34 Is it.
Florian Lehner 00:49:35 Yeah.
Antoine Toulme 00:49:36 Under under open telemetry. You want to create a new repository that's going to do the conversion.
Florian Lehner 00:49:42 Yeah, maybe I can jump in we I think at the moment, Alex say, who is not here today? Is working on a verifier in his private repository. So to make this possible. The challenges he faces is that he has to use the protocol file from March or the status of March, I think, when 1 7 was released, and in the meantime we make some significant changes to the protocol. So fields got removed things got changed. And that's the problem he's facing at the moment.
I think that's also the motivation that we go on and have Rc. One or Alpha one, or whatever that, we have another release, that we can have the latest changes, settle it a little bit, and then can do things like, Hey, we want the Ci job that is always running like converting people to auto perf and vice versa. At the moment. There are so many things in moving that it will be a full time job to keep it up to date.
Antoine Toulme 00:50:55 Okay, so is that work talked somewhere? Is there an issue that I can latch on.
Florian Lehner 00:51:05 I'm not sure if Alex shared his pr somewhere.
Christos Kalkanis 00:51:12 It has a pull request here.
Florian Lehner 00:51:16 Yes, I think that's that's the that's the.
Antoine Toulme 00:51:20 That's not. That's not repository.
Florian Lehner 00:51:24 Yeah, we did.
Christos Kalkanis 00:51:24 Yeah, it's.
Florian Lehner 00:51:25 From the community. We alex reached out but we did not get the repository yet. That's why it's in a private one.
Antoine Toulme 00:51:33 That's not what this is a private repository. I'm sorry. What say this again?
Florian Lehner 00:51:38 Alex. The repository Chris has just showed Alex sent is a private one.
but we, as a profiling sake, ask Hotel to get a repository for an hotel, so this private one will merge them to hotel.
Didn't get this yet.
Did you have a do you have a request up on community for that?
Yes, sir, sorry. I think it's if you look down We had some requests somewhere in the I think it was open telemetry, dev or open territory community.
Christos Kalkanis 00:52:31 Oh, shit.
Antoine Toulme 00:52:33 Yeah, I have to have it on the committee. So 3 weeks ago.
there's discussion with Trask about creating a new seek that profining Github Repository.
Florian Lehner 00:52:44 Yeah, right.
Antoine Toulme 00:52:45 Discussed on July 10.th Okay, so let's wow.
unclear, what's pending for this?
we can. If we can move on that, that'd be great, because then we can have some. I can help bluntly, right? So I'll ask.
Christos Kalkanis 00:53:13 And you leave a comment. And one, you know, ping people again like that's what with open telemetry, you.
there's so many things going on that we we have to keep pinging each other to make things happen. That's my.
Antoine Toulme 00:53:26 Absolutely.
Is there anything pending to create this repository?
Okay, alright. So good to know. So you're having. We're having a long, windy differ here where we need to.
It's kind of a chicken and egg thing, right? We need a repository so we can go write code so we can run tests. So we can check that. The people of conversion works.
Florian Lehner 00:54:08 Yeah, right.
Antoine Toulme 00:54:10 That's fun.
Okay, I put comment up.
I think I might be wrong about this.
There has been significant work from Trasc on automating the maintenance of all the repositories in the Github Repository itself.
So there might be a way for us to also open a Pr against that infrastructure project. They actually have a sync meeting later today. So ask and I can look into it to make sure that it gets done rather than because Trask is out is out this week or is out today tomorrow. It's not that bad. Okay, so okay, alright. Second point, I have second point, the agenda.
don't wanna talk.
Christos Kalkanis 00:54:53 So, yeah.
yeah, before we move to that, can I add an action item for just for that, Antoine? Maybe you can. You can take it for, like next meeting, to just look into this.
Antoine Toulme 00:55:04 I mean. I don't know. I'm not saying I'm coming to your next meeting, but it can.
Christos Kalkanis 00:55:09 Yeah. But if you if you you don't have to attend the next meeting, this can happen asynchronously. But you know, if you just volunteer to to look into this, then we can add it to the agenda, so that, you know we can.
Antoine Toulme 00:55:20 I mean.
Christos Kalkanis 00:55:20 True.
Antoine Toulme 00:55:21 Basically, what I'd like is agenda is great. I like to have github issues because we can actually delegate work with Github issues a bit more, and it can create more of a sense of community. So if there is a ripple all of a sudden you can do a lot more right.
And, for example, I'm not just interested in people. I want to see Jfr. Hotel conversion right? I want to see all sorts of things, and there's more type of this type of conversion that we'll need to maintain. So we can make sure that things work, because right now they just don't. And it's it's still so.
It would be great to have that I'm happy to help on that. If whatever I can push.
Christos Kalkanis 00:56:04 Okay. Great.
Antoine Toulme 00:56:08 Okay?
Okay, all right. So next one. This is from a former colleague. His name is Bogdan. He says that there's a feeling of premature optimization that's coming from the Protophiles. I'm sure you've heard this before.
I think.
I think that's a valid opinion.
It's not backed. I don't I feel like this is.
it would be interesting to have a discussion about the format of that data. We just had discussion about the resources and these type of things.
Please please consider the feedback. I think this is important.
There are implementations that can reduce. If so, I want to understand also, like the the product requirements that went into doing this type of optimization, such as trying to group information into a separate data structure from where it would be found would be worthwhile knowing that. You know, Portobuff is just a. It's a way to transport data for sure. So there is also a problem here is that the Portobuff is also used as a semantic model. If we could kind of separate the concerns, and just to go about the business of having the best profile model there is.
Would you, then, do this type of optimizations.
Christos Kalkanis 00:57:32 Yeah. Unfortunately, like, based on the previous discussions that we've had, there are multiple trade-offs, right? So like.
you know, when you say the best profile model there is like that's not. There's not one thing right? It changes based on where you're coming from. Like different people have different requirements. Also, the protocol itself needs to support multiple use cases that are quite disparate. Like, for example, we have the Sdks on one side, then we have something like the profiler, which right now operates very low sampling frequency, but that could change in the future. We could move it to the very high frequency, sampling and and the requirements for that are quite different to what we have now. And also the volume of data that's going to produce did application becomes way more important in that scenario.
Antoine Toulme 00:58:15 Wait wait. So wait. No, no, I I think we need to separate that concern, actually sending the data over the wire. It's there are multiple initiatives inside open territory to kind of optimize transport right from Apache Arrow. This hotel arrow initiative. You probably, if you talk to the ground for 5 min is going to mention Steph to you. Multiple ways to talk about transport of data, or even encryption or storage at rest. Or all these type of things to help with dedubbing, with making sure things are okay. The problem is that from a semantic point of view.
is, are you? You're ingraining into something that is supposed to be a representation of a profile which is the presentation of reality right into something that you're trying to optimize. For if I was to do the same thing for metrics. So, for example, for metrics, we could say, Look, the number of dimensions that are the same across all those metrics right? Could we just create a dictionary of dimensions at the top?
We could do that right. There's nothing stopping us from doing this. And we could, just, you know, stick all the dimensions into into a big area at the beginning. And then we just have the index for all the dimensions of the metrics in there.
and our model would be incomprehensible for people to understand, and they would not be able to work with it, and and they would probably rightfully come to us and say, we actually want to have this level of duplication of data in between each metric data point, because we're trying to understand the reasoning of this, and we want to separate the concerns of having a descriptive semantic model to having a transport model. That is efficient.
right?
And you know, Zip saved like, you know the world multiple times over. Right? We get compression rates with Gzip and CST and all those things that are absolutely incredible. So you can make all sorts of points. Also that there is in you can be as verbose as you like. Compression will save you.
Christos Kalkanis 01:00:16 Knife.
Nayef Ghattas 01:00:17 Yeah, I think specifically on compression. This is something that we discussed multiple times. And since the Protobuff, since the payload needs to live in memory in the open telemetry profiler, and as well in the collector.
and compared to metrics where payloads generally are relatively small profiles can be tens of megabytes, even hundreds of megabytes while doing the optimization that is done here that we inherited indirectly from from people off.
So if we started duplicating things, we go even to a bigger order of magnitude. And we need to keep that data in memory in the collector, which means using gigabytes of memory in the collector, which is not feasible. So we took that trade-off as it is, and I went and talked to the opentelemetry specification. Sig. And we discussed all the different alternatives, including Arrow and Steph.
And the conclusion from that is that none of those potential transports are currently mature for us to use, and we don't want to block the release of a profiling signal on a transport protocol being available on that. And this is the decision that specification, Sig. Advise us on.
Antoine Toulme 01:01:37 Okay. So, folks, if if you have a transport that is not mature enough, come, make it mature, and then we can solve the problem for good. I mean, what is this?
Okay? All right. So I I'm not sure. Is this not written somewhere like, please send it. Put it on the issue. Let's work on this together, if you'd like or not. But I gotta say I don't think this is the right way to do it.
We're over time. I'm gonna let you go.
Thank you.
Christos Kalkanis 01:02:08 Okay.
I think we can erase this in the in the next week as well. We we like, Nate said. We've discussed this multiple times, right? We thought about the problem as well.
yeah, Florian, last thing, maybe you have. You had something to add, because I saw you raise your hand.
Florian Lehner 01:02:23 Yeah, just would have said the same points as now. If yeah, nothing to add. There.
Christos Kalkanis 01:02:33 All right last time. Some guessing we still know.
Yeah, so quickly. We have some pull requests like, there's a comment in slack. You can find it. Jonathan created. I added the list of pull requests there. If you can go ahead and review some of those if they're missing reviews and so on. We can get them as it's. It's currently blocking us from wrapping up a bunch of issues that need to be resolved also for the Rc. One.
Okay, I think that's it. We don't have anything else unless somebody has anything to say. Last thing we can interrupt this one.
Okay, thank you. Take care. See you next time. Bye.
Elsa Keirouz [Datadog] 01:03:16 Thank you.
