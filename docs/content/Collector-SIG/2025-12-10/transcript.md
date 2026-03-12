SIG: Collector SIG
Date: 2025-12-10
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/TwiESivkhspMyNp0pheQ60CwChYKyEQPpvLd8REvvH5FEv6JU8OFNPN1L4uvJA69.WJN87LcVAdZy_bBC
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin** 01:20 Hi, Andrew.
**Andrew Wilkins @ Elastic Observability** 01:22 Hey, Dimitri, how you going?
**Dmitrii Anoshin** 01:24 Pardon.
**Andrew Wilkins @ Elastic Observability** 01:26 Not bad, thanks.
**Dmitrii Anoshin** 01:28 Yes.
**Andrew Wilkins @ Elastic Observability** 01:30 Oh, sorry, go ahead.
**Dmitrii Anoshin** 01:31 Yeah, I've been recently buried with something else at Splunk site, so I'm not really… haven't had a lot of time to work on the collector.
But this… this issue is interesting that you point, Jeremy about, yeah, thanks for… So, I… my concern is that… We moved everything from the batch processor because of the problems that we have with the synchronous back pressure and everything, so we have to make batching.
After… after the queue, in order to prevent that.
Yeah, I saw your suggestion to move that before as a splitting option, right?
But even if we split that, we… like, it means… if we… if we can split before, it's fine.
But we will not be able to batch after that.
Does that make sense? I mean, if we split, let's say, by instrumentation scope, name, right?
We… we still want to optimize the payload that we sent over the wire, and we want to batch. But we cannot batch by… partitioned by that scope name anymore, because if we… we cannot even enable batching if we do the splitting, right? Because batching on the exporter side would batch regardless of instrumentation scope name.
**Andrew Wilkins @ Elastic Observability** 02:58 Okay, so, what I had in mind was… When we do the split.
**Dmitrii Anoshin** 03:03 We would…
**Andrew Wilkins @ Elastic Observability** 03:04 Inject some client metadata?
And we would use that with the batching. So there was this PR that one of my colleagues put up, where you commented.
Where he was adding metadata keys for the batching and partitioning.
So there's… there's batching at the request level, and that would be take… and that would take into account these metadata keys, and basically every… Unique combination of metadata keys would end up in its own partition.
**Dmitrii Anoshin** 03:33 Yeah, yeah.
**Andrew Wilkins @ Elastic Observability** 03:34 And then, on the splitting side, we would… in the example you gave, instrumentation scope, we would… I don't know, Split… let's say we're grouped by the package name, the scope name.
The scope name would… we would group… create all groupings, one per scope name, and then we would introduce a metadata key, which is configurable, which would be scope name, and then we would have that based on… we'd also have that in the configuration for the request level partitioning.
**Dmitrii Anoshin** 04:06 I see, that makes sense. And the metadata YAML, it's like… oh, sorry, metadata YAML. The… That key.
Metadata key.
That wouldn't be part of a TTL, right, expression. It would be probably some kind… some, like… I mean, from my perspective, it should be some kind of obvious thing that we said, rather than OTTL.
**Andrew Wilkins @ Elastic Observability** 04:34 Yeah, yeah, actually, let me just see which one I linked to. I, I… Responded on a different issue just yesterday, so this would be a better one to… look at… Okay, let me… I'm just gonna share my screen, because it'll probably be easier to… Should… Go over then.
But basically, for the, for the metadata level.
partitioning, I would propose that we have just a list of metadata keys.
So, alright, where do we start? So, originally… We… oh, not originally. A while back, we talked about having a single way of partitioning, and then we would have maybe some extensions, they could be OTTL-based, whatever. I think that gets a bit complicated when you're just dealing with metadata, so this is sort of what it would look like if we wanted to partitioned by a tenant ID, for example.
What I had in mind, rather, is something simpler like this, where you just specify the keys as a list.
That's only going to work for metadata keys, though, obviously, so we still need something for instrumentation, scope, and whatever.
**Dmitrii Anoshin** 05:53 To clarify, this is just exactly a replication of what we have in the Butcher process, essentially.
**Andrew Wilkins @ Elastic Observability** 06:00 Yeah, yeah.
**Dmitrii Anoshin** 06:00 I should process at exactly this interface.
**Andrew Wilkins @ Elastic Observability** 06:03 Yep. Yeah, so for the in-Exporter helper, I would propose that we add just this and nothing else.
**Dmitrii Anoshin** 06:10 Yep.
**Andrew Wilkins @ Elastic Observability** 06:10 And then we can have a separate processor, which comes before the exporter.
And that would… let me see if I have an example… yeah, so this is the example where we're… Splitting by service name.
And it would introduce this as a… as a metadata key. Okay.
And then in your exporter, you would also have that. So it's a little bit… it's not great that you have to repeat it, but I think it's the most flexible solution.
Yeah, anyway, that's what I had in mind.
**Dmitrii Anoshin** 06:44 I mean, this solution works, but I would agree on that if we… specifically, that's what we're gonna have going forward, like, long-term, because… The thing is, with… my concern, like, about the conflict that I mentioned, is that we cannot change that anymore. If we decide on this interface, we will not be able to introduce partitioning anymore. And I do like more the partitioning, I just… I mean, you try that out, you probably face some technical complications.
I, that makes sense. Can you maybe, like, sh… Like, give some… idea? What was… what went wrong with that approach, what didn't work?
Why the complica- all the complications are coming from.
**Andrew Wilkins @ Elastic Observability** 07:35 Yeah, trying to refresh my memory now.
**Dmitrii Anoshin** 07:42 I mean, it has to go in the country, right? We would have to introduce some… I remember you mentioned some kind of complicated Go interface that we need to…
**Andrew Wilkins @ Elastic Observability** 07:52 Right, yeah, so it would introduce complexity in the way we configure it, so we'd have to have a extension interface.
or the partitioner. Yeah.
So, I guess, long story short, we could do it. It's not impossible.
**Dmitrii Anoshin** 08:07 But it increases the complexity of the config, and introduces more interfaces.
**Andrew Wilkins @ Elastic Observability** 08:12 So, if you wanted to do that request metadata level partitioning.
it ends up being much more complicated, in my view, but if you're doing just a list of metadata keys, it's simple. We could do both, right? We could… we could have the metadata key list.
And then also have support for extensible partitioning.
**Dmitrii Anoshin** 08:37 Yeah, that's the conflict that I mentioned. If we have both, we would need to also have some kind of, prioritization, if you specify both, and if you have partitioner which does… does metadata, handle metadata as well, which one goes first. So I would really like to avoid having both because of that. It's just, like, to keep things simpler.
**Andrew Wilkins @ Elastic Observability** 09:03 I… I totally understand that for the metadata use case, if you only have already metadata provided somewhere… from somewhere else from the outside, let's say from the application.
**Dmitrii Anoshin** 09:12 SDK, right?
the interface that we currently have with the batch processor is easier. You just replicate that in the The exporter, but at the same time, that… that functionality, like… I'm just, like, thinking about our customers and some, like, others that use them, different backends, probably. It's not very… like, common, in general, to budge by different key, but badging… I wouldn't say that it's significantly higher chances to batch by metadata rather than something else. That's my concern.
So, I think it's probably relatively similar.
use case to batch by instrumentation type, by resource attribute, and by metadata key. But in general, it's not very common to do, like, batching by some partitioning in general, but if we… if I remember all the use cases, they are typically kind of similar.
So, in that case, we are speaking about configuration interface complications. So, it's easier if we… if we… Badge by metadata key only, but it's a bit more complicated if we introduce this additional processor.
**Andrew Wilkins @ Elastic Observability** 10:32 Yeah, basically. The other thing is, partitioning might be useful earlier in the pipeline, so we have all of the… we have at least two processes that do grouping.
Which is essentially the same thing.
**Dmitrii Anoshin** 10:46 Yeah.
**Andrew Wilkins @ Elastic Observability** 10:46 Grouping by attributes, grouping by trace.
**Dmitrii Anoshin** 10:49 They could be replaced by…
**Andrew Wilkins @ Elastic Observability** 10:52 some more general-purpose OTTL-based partitioner.
**Dmitrii Anoshin** 10:57 That's a good point. We do have group by, but we… that group by makes the split as well.
**Andrew Wilkins @ Elastic Observability** 11:08 So actually, no, you're right. It doesn't split the request, it just rearranges the data within a request.
**Dmitrii Anoshin** 11:16 So it's a little different.
**Andrew Wilkins @ Elastic Observability** 11:18 Yeah, it's a bit different.
**Dmitrii Anoshin** 11:22 So, the complexity here is not only… like… It's kind of stateful, in a way, stateful component, because in order to split, you get one request.
And then you have several requests out, right?
And then you need to have some multiplexing, Functionalities, so you would need to send all of the requests, you need to wait for all of them back.
And, respond, to the… Respond to the client after that.
And if you don't use Q, it'll be potentially, like, Pretty… I mean… I don't know how… how potentially we would just do… Same as we do with the panout, I guess.
Similar idea, so it's not that big of a deal, but still, it's kind of…
**Andrew Wilkins @ Elastic Observability** 12:25 I had in mind that they would all execute concurrently, but we can have it configurable if we need to. Okay. Like, one after another.
**Dmitrii Anoshin** 12:33 Yeah, that's fine. Yeah, one after another, probably. That's… I believe that's how we… that's how our finale right now works. It's just, like, sequential.
**Andrew Wilkins @ Elastic Observability** 12:42 Execution.
**Dmitrii Anoshin** 12:43 So, I guess… if I was under impression, I haven't looked into all the issue about, like, why we cannot use the partitioner extension.
But if we… if there is no, like, technical critical limitation, maybe we can discuss it with… further with the others, and decide on the approach, because.
**Andrew Wilkins @ Elastic Observability** 13:06 Like…
**Dmitrii Anoshin** 13:07 I think it's a pretty important decision, right?
**Andrew Wilkins @ Elastic Observability** 13:10 Yeah, I think so. Who do you think we should involve in the discussion, then?
**Dmitrii Anoshin** 13:17 I guess… are you… you are in one of the main pingers or leads channel in Slack, right?
**Andrew Wilkins @ Elastic Observability** 13:25 Oh, yeah.
**Dmitrii Anoshin** 13:26 Maybe we… maybe we… There is some, like, some kind of… some kind of working mechanism that we have been using in the collector, I guess, based on some, like, emojis or whatever.
You can maybe try that as well.
**Andrew Wilkins @ Elastic Observability** 13:44 Okay.
**Dmitrii Anoshin** 13:45 Oh…
**Andrew Wilkins @ Elastic Observability** 13:46 I guess I can just raise the comment.
**Dmitrii Anoshin** 13:49 Look for some, like, practices that you use for, like, getting through some kind of… let's say, decisions that need to involve more people. We've had some… something like that before. But it's just, like, I'm… I think I'm fine with either way, but for… it's still, like, for me, partitioner interface as an extension seems cleaner solution. It's just, I don't… I don't see it's a big of a problem for… to use the metadata, and yeah. My… receiver maybe as well, but… oh, sorry, a processor maybe as well is an option. It's just, like, for me, no-go is only having both. That's… that's why I would like to really Take a chance and consider something that would keep full launch. Especially given that we are stabilizing all the interfaces and exporter as well, right?
We want to have something that we… Introduced for… and do a change coming forward.
I believe there is some another issue. It's pretty unrelated, but it's also something that users are asking.
specifically for the exporter, and make it some kind of an extension, or some pluggable extension, or some… Oh, you're probably involved into that as well.
**Andrew Wilkins @ Elastic Observability** 15:14 Aqua.
**Dmitrii Anoshin** 15:15 That one, that one.
**Andrew Wilkins @ Elastic Observability** 15:17 Yeah, I was actually looking at both of them at the same time, trying to figure out if there's some overlap.
potentially is. One idea I had was… We could add some kind of… processor shim in the exporter helper, so… You could inject processes Only in the exporter, so it happens directly before it sends.
**Dmitrii Anoshin** 15:43 Okay.
**Andrew Wilkins @ Elastic Observability** 15:44 If that makes sense, so we could have some kind of concurrency limiting, processor that you would use in there.
Which you could also use earlier in the pipeline. I don't… not sure that this is the right way to go, it felt a little bit off, but that would be a one way.
**Dmitrii Anoshin** 16:01 introducing another processor, like, exporter processor, that's gonna be super confusing for the end user.
**Andrew Wilkins @ Elastic Observability** 16:09 That's what I…
**Dmitrii Anoshin** 16:09 I still do, see, like, potentially… Like, a necessary… a need to have some kind of pluggable things on the exporter side.
And if we have partitioner as one of the pluggable extensions, potentially we might have something else. I'm just a bit concerned about using exporter term here, because… oh, sorry, exporter processor term here, because it's gonna be just confusing, like, we have.
**Andrew Wilkins @ Elastic Observability** 16:37 Yeah, where do I put my processor?
**Dmitrii Anoshin** 16:38 too many processes. Maybe something else, like, I don't know, exporter extension or something. We do have… Middleware, similar thing, the receiver side.
So we might have something like that on the exporter potential as well.
**Andrew Wilkins @ Elastic Observability** 16:55 And if we… if we go with this thing for the… for the arc.
**Dmitrii Anoshin** 17:00 Maybe we can do… the same for, like, co-similar route for the partitioning. In that case, if we can come up with a common Go interface for the, for, for, For the extension, let's say, like, exporter extension.
That way, it can work by some generic interface where a user can specify one or many extensions.
**Andrew Wilkins @ Elastic Observability** 17:27 They can… they can be different extensions, but one of.
**Dmitrii Anoshin** 17:31 Yeah. Would be partitions.
**Andrew Wilkins @ Elastic Observability** 17:33 That's where I was… that's where I was coming from as well, when I looked into it, and… They're a little different, those two use cases, so the… the Arc one doesn't care about… hey, Antoine.
**Dmitrii Anoshin** 17:44 The Arc one doesn't care about the…
**Andrew Wilkins @ Elastic Observability** 17:47 the payload at all. It just cares about Sort of the… how do I put it? Basically, the concurrency, so… When a request is going to be sent.
How long it took, what errors came back, and the number of them that are in flight.
Whereas the partitioning one definitely cares about the contents of the…
**Dmitrii Anoshin** 18:10 And it doesn't matter if it doesn't care, right? We just… they provide, like, we define interface, extensions implement that interface, and whether they use the payload or not, it doesn't really matter. It'll be just no op for that particular…
**Andrew Wilkins @ Elastic Observability** 18:29 Right, but that's where I ended up with the processor, because the processor is just like.
And I can see when it goes in and out, and…
**Dmitrii Anoshin** 18:38 I understand. It's kind of… the interface would be similar to process, so we might look into the middleware extension on the receiver and see how Josh put that interface, but it can be something similar, essentially. Not similar, because on the receiver, you operate over the client HTTP things, so it's like a different field.
But it's still, like, I believe middleware is kind of a processing pipeline, so there is something, some input, some output.
And it should be something similar on the… On the export. We just don't call it processor to always confuse otherwise, yeah, otherwise.
**Andrew Wilkins @ Elastic Observability** 19:13 Yeah, I suppose it can still use the consumer API. Like, it can provide the consumer API, but it's not a processor, that sort of thing.
**Dmitrii Anoshin** 19:21 That could, that could work.
Yeah, let's ex… let's explore that. I'll… I'll dig… feel free to ping me in Slack, like, I'll dig into the issues and maybe respond with some… some of the input from my side on… on the issues, but otherwise, we can maybe sync in Slack offline, and, like, if brainstorming needed to, something like that.
**Andrew Wilkins @ Elastic Observability** 19:44 Yeah, I'll raise it in the leads channel and see if anyone's got any input.
**Dmitrii Anoshin** 19:48 In this channel, once we have, I would say, like, the def… like, to the point when we need to make a decision, right? But I think right now we might have something to explore before that, right?
**Andrew Wilkins @ Elastic Observability** 20:03 Okay. I mean, yeah, I did spend a while on looking into…
**Dmitrii Anoshin** 20:07 I mean.
**Andrew Wilkins @ Elastic Observability** 20:08 I'll have another look.
**Dmitrii Anoshin** 20:10 But you do have that interface that you were thinking of. If you can send me, and we can maybe discuss it offline before that, or if you already can present an alternative to the SEC in general with those two, you can do that as well.
**Andrew Wilkins @ Elastic Observability** 20:24 Yeah, okay. I'll try and prepare something a bit more for next time, then.
**Dmitrii Anoshin** 20:28 Okay, cool, awesome.
And, it's, like, it's, like, worth, For me, anyway, anytime. It's just sometimes… you, you, like, you send me that message, I… I… tried to look into it, but didn't have enough time to respond, and then got delayed a bit, but if you… if you can have, like, ongoing discussion, that will be much… much quicker from my side.
**Andrew Wilkins @ Elastic Observability** 20:50 Sounds good.
Alright, thanks for chat. Oh… I'll come back to it, and I'll, bring it to the next meeting.
**Dmitrii Anoshin** 20:57 Okay, awesome, thank you.
Antoine, do you have anything to discuss?
**atoulme** 21:04 Not really.
No, I'm okay, I'm just overwhelmed and too much work. But, yeah, no, everything's fine.
Is there anything that we should be paying our attention to? I'll admit I haven't been… the most up-to-date. I just preview PR at this point, just… Try to merge what I can. Would it make sense?
**Dmitrii Anoshin** 21:40 Oh, cool.
**Andrew Wilkins @ Elastic Observability** 21:41 go through the stability phase one issues. I don't have any input on any of them.
**Dmitrii Anoshin** 21:46 For the stability, I have something to put from my site. It's related to the entities interface and, like.
User configuration interface that is generated from metadata YAML when you have metrics and resource attributes, now we need to have entities.
And then I'll output that issue to describe, like, a suggested interface, because we need to change the interface for the entities before we declare them stable, because it's going to be a breaking change, essentially. We potentially can declare… deprecate the old interface.
And they keep it until 1.0 or stable, but whatever. Yeah, this is something that came up on the recent meetings. I've been carrying that, but never really put that in an issue, but it has to be handled before we can stabilize things.
Essentially, if you need some input, like, we have receivers, let's say, we have processors in the receivers, let's say, Cubelet receiver, whatever.
or Kubernetes cluster receiver, it emits several entities, but the interface right now is, like, is based on metrics and resource attributes. You have a huge list of metrics, one list of metrics.
And one list of resource attributes. And it's unclear… Which resource attribute applied to which metric?
And, etc. But now, given that we're gonna emit entities along with the resource, now we have to group it anyway, because, like, for example, like, pod entity would have those metrics, and it will have those, attributes associated with the entities identifying and And on the define, and yeah, it has to be configurable from any test, kind of.
Point of view, rather than… Just two plain lists of metrics, and… resource attributes.
I'm gonna put that in issue, and I'm gonna… once configuration interface is agreed between maintainers, I would… would change to the middle of the table.
**Andrew Wilkins @ Elastic Observability** 23:55 So the metrics will be more entity-centric, is that what you're… More, basically.
**Dmitrii Anoshin** 24:00 both attributes and metrics will be entities and centers. So, essentially, let's say, the configuration interface will allow you to disable pod metrics, but that would mean disabling pod entity.
And, but under pod entity, you don't need to disable it, you can just disable particular metrics under that entity. Or you can disable particular non-identifying attributes of that entity. So, for example, pod has, like, I don't know, some…
**atoulme** 24:30 Because it's soccer.
**Dmitrii Anoshin** 24:31 Right, and you want to disable that particular thing, and it'll go under both, and then you disable that attribute.
And the data, all the metrics will come without that.
all the resources.
Both resources will go without that attribute.
**atoulme** 24:51 Dimitri, we haven't had time to chat about this type of stuff.
I know the cluster receiver We want to have it, emit entities eventually.
**Dmitrii Anoshin** 25:00 And that's a separate thing, and I'll probably have the interface to be…
**atoulme** 25:07 Is that dependent on this? No.
**Dmitrii Anoshin** 25:09 it's kind of not dependent, but it's a bit related, I guess, because, like, that interface would be specifically for metrics, but I need to design it in a way that once we emit NT events, it… it doesn't conflict with that interface. So, like, extensibility part of it would be… would be taken… need to be taken care of.
**atoulme** 25:29 Okay.
Yeah, this is becoming a big deal.
So… Okay.
Cool.
I mean, Yeah, no, otherwise, everything's okay, like, we… I think I have a release manager for the next release.
Is there anything that we need to pay attention to before the next release that I should know?
**Dmitrii Anoshin** 25:54 I remember Bogian was asking about some tweaks to the OTTL, and that's all I know, all I'm aware of.
**atoulme** 26:01 You're right. I think I commented on that issue.
**Dmitrii Anoshin** 26:03 I think it's merged already, so you're good.
**atoulme** 26:06 Right, I put up, he wanted a fix because his PR was inside the same release, so he could kind of get away without declaring it to breaking change.
Which is fine.
But then that means we need to be on top of it, right?
Okay.
Anyways, anything else?
**Andrew Wilkins @ Elastic Observability** 26:25 I guess you're aware everything's broken at the moment, because the config optional?
Changes?
**atoulme** 26:31 I'm not that aware. Is it because between core and contribute?
**Andrew Wilkins @ Elastic Observability** 26:35 Yeah, yep. And there was a change to… I can't remember what, config HTTP, maybe?
**atoulme** 26:42 There's painful PRs, like, about 4 pages deep inside our list of PRs about some changes for config optional. Yeah, I see it. For QBashConfig.
**Andrew Wilkins @ Elastic Observability** 26:52 Yeah, that's the one.
**atoulme** 26:54 We have been for 3 weeks, it's approved, it's full of… It's full of conflicts around the Godot mods, it's gonna need a big rebase.
**Andrew Wilkins @ Elastic Observability** 27:01 Yeah, it's… I believe the Datadog components, there's a… it's hard to change the data doc components, but, Pablo is on it.
**atoulme** 27:11 I mean, the, the… The release changelog, the diff, is 22,000 lines change.
Okay.
**Dmitrii Anoshin** 27:20 Yeah, that seems like a blocker.
Sorry and so on.
But yeah, we need to wait for that to be resolved.
**atoulme** 27:28 Don't feel sorry for me, feel sorry for Josh.
He's… He's merging that before Monday, right?
**Dmitrii Anoshin** 27:35 I hope so.
**atoulme** 27:36 So we'll just revert everything.
**Dmitrii Anoshin** 27:38 Yeah.
**atoulme** 27:39 Because I'm not merging that line. This is… this is way too much. What is this about? What is this, even?
Oh, my… Okay.
**Andrew Wilkins @ Elastic Observability** 27:49 I did review it.
It's okay, it's just there's some, challenges with the Datadog components.
**atoulme** 27:55 This is just the same change over and over, because it's not even displaying the D for me.
**Andrew Wilkins @ Elastic Observability** 28:01 Yeah, it's… mechanical.
**atoulme** 28:05 Yeah, I mean, not too surprising there. I'm just… I'm just complaining.
Yeah, okay.
Okay.
Do we care? Is it… is it a big deal?
**Dmitrii Anoshin** 28:21 No, we should just leave it to this. If Josh handles it, it should be fine.
**atoulme** 28:27 Yeah, should I mark it as a release blocker with a label?
**Dmitrii Anoshin** 28:30 It is a release blockage, technically. You cannot make a release without it. So, like, adding a label would make it explicit, for sure.
**atoulme** 28:40 Yeah, so if you don't mind, I'll just do that so that we can track it explicitly.
**Dmitrii Anoshin** 28:44 Yeah.
**atoulme** 28:45 Okay, done.
Okay, thank you for that call-out. Appreciate it.
Yeah, there was some discussion about, ready to merge in some of the pull requests, so… I think it's the same discussion, but… Do you folks have any wisdom on that?
I believe this was a public discussion around the fact that it's ready to merge is sometimes used by triagers.
When, frankly, they should not be doing that, it should be an approval thing.
**Dmitrii Anoshin** 29:22 Oh, I see what you mean. So, like, they put radio to Merced while they… Triashers, not approvers?
**atoulme** 29:31 Yeah, it's just the one triager was apparently kind of too eager, and put it into Merge a couple times, and maintainers need to kind of, you know, if you're not.
**Dmitrii Anoshin** 29:40 Just because someone says predicted merge does not mean you're off. You're no longer… you can just go ahead and merge. Yeah. I don't think we need to do any technical guardrails against it, we just need to be mindful when we merge stuff.
**atoulme** 29:56 Yeah, I wanted to kind of do some automation around this, and… I don't know. I like the very human and social signal that you think this is ready to merge, because it actually makes you, you know, you're putting your reputation forth, like, as an approver, I think this is ready to merge.
And I think this is great as a signal. Also, it shows you're… you're more ready to move up to maintainer.
Good evening.
**Dmitrii Anoshin** 30:22 And I guess maintainers, while merging PRs, they should have… get them.
take responsibility for that as well. They should never, like, blindly… Merge PRs, if… if they see that.
**Andrew Wilkins @ Elastic Observability** 30:36 From my perspective, I just use it as… I think it's ready for the maintainers to look at, rather than it's ready for merging, necessarily. It's up to the maintainers to decide whether it's ready for merging.
**atoulme** 30:47 My bit.
That might be a good way to kind of reframe that. Ready for maintainers.
**Dmitrii Anoshin** 30:53 Fair.
**atoulme** 30:53 Huh.
I mean, we're far… we still need to work on that workflow, it's just… Okay.
Alright, appreciate the feedback.
**Dmitrii Anoshin** 31:05 Cool. If there is nothing else for today, I guess we can wrap it up.
**Andrew Wilkins @ Elastic Observability** 31:09 Maybe just one quick thing, you… not sure if either of you care, there's this PR that I put up last week, I think, for… Another breaking change to config HTTP to support Unix domain sockets for the server side.
**atoulme** 31:27 I'll turn that.
**Andrew Wilkins @ Elastic Observability** 31:27 Same thing for client, it will break on Trib, so if it is acceptable, then we should wait till after the release, but, yeah, if either of you care, have a look, please.
**Dmitrii Anoshin** 31:39 Always remember, Antonio, you've done… you've tried that before as well, right?
**atoulme** 31:43 I just didn't get that much attention and love.
**Dmitrii Anoshin** 31:46 Oh, God.
**atoulme** 31:47 I don't know if I did… did I do it for config HTTP?
I probably did it because there was actually… this is actually a great way to secure your endpoint.
In some situations, you want to open a socket, not open a port.
And so I thought they would be great to have.
But it didn't go anywhere. The main issue was the motivation to support that was just not there from maintainers.
And so it just fell by the wayside.
not even going to look at it, because it's been multiple years since I've done that, and I don't think we should just say, because Antoine tried it 3 years ago, we should not even look at Andrew's work.
**Dmitrii Anoshin** 32:26 Right?
**atoulme** 32:27 I'm just saying that it's been an uphill battle to get attention on it.
**Andrew Wilkins @ Elastic Observability** 32:34 One of the reasons why I did it is because configGRPC does do it, so I did it for consistency.
**atoulme** 32:40 Not necessarily because…
**Andrew Wilkins @ Elastic Observability** 32:42 I have a burning desire for Unix domain sockets.
**atoulme** 32:45 I know.
**Andrew Wilkins @ Elastic Observability** 32:46 So it's a good place for other config as well.
**atoulme** 32:49 So, I know what you're trying to do, right? You're trying to make ConfigNet somewhat compatible between ConfigHTTP and Configure RPC, so eventually we can have the same ConfigNet between the two, right?
**Andrew Wilkins @ Elastic Observability** 32:59 Yep, exactly.
**atoulme** 33:00 Okay, I mean, I don't mind, whatever can… Happened there, would be great.
**Dmitrii Anoshin** 33:09 And did you have any practical reasons for that when you were writing it?
**atoulme** 33:19 Why did I work on that?
**Dmitrii Anoshin** 33:21 No, I mean, like, Andrew is adding this for consistency, but did you have any practical reasons for that?
Did you need that yourself, or some of the users, I don't know?
Do you remember?
Leading.
**Andrew Wilkins @ Elastic Observability** 33:36 I think Erdogan was saying that it can be more secure, like, you can use file permissions on the Unix domain socket.
Alright, Antoine.
**atoulme** 33:45 Yes, that's the… that's the right reason to use this, but also, I think you have an alternative motive, which is that you want to harmonize the config HTTP and Convig gRPC, right? Because they're slightly different for no reason.
**Andrew Wilkins @ Elastic Observability** 33:58 Yep.
**atoulme** 33:59 Okay. So, yeah, we should be… because we don't use ConfigNet as part of ConfigureCTP, we don't have the same level of support.
of what you can do with the listener. If you have the configNet, you can do more. You can do dial, you can do dial options and stuff like that. And because config HTTP right now, the endpoint is a string, not a whole thing, then you don't get as much value out of that, and… maybe there's something to be said about having some plans. So I know that, Andrew, you talked about that, like, what, 3 months ago? You wanted to kind of harmonize those two things? Now, I told you you're getting straight into this type of problems, where it's difficult to get these config modules changed, because there's this huge pressure to stabilize, and… Yeah, I don't know.
Yeah, here's my old PR, slightly different, so I think I was just looking at it because I wanted to be able to support sockets for the reason of security, and there might be an issue that is… Yeah, there's an issue that I opened just before, I guess.
**Andrew Wilkins @ Elastic Observability** 35:08 Another reason why I want to harmonize these two is, there's a pull request that's been opened for… It'll be more than a month, I think, to add support for SO reuse port. It was added to just config.http, but I think it should be on anything that uses ConfigNet. Obviously, we're not using configignet in HTTP, so, it's… It's not ideal.
If we had it on the S… on the config net at a config, then we could support it for both gRPC and HTTP and anything else.
Dang, so you have comments.
**atoulme** 35:45 It's marked ready to merge.
It's not passing the test, though.
**Andrew Wilkins @ Elastic Observability** 35:52 Yeah, I think I'll…
**atoulme** 35:53 Ugh.
**Andrew Wilkins @ Elastic Observability** 35:54 Oh yeah, the… the card coverage is… not…
**atoulme** 35:59 Well, okay, so just the coverage?
**Andrew Wilkins @ Elastic Observability** 36:02 I think all the other ones are failing because of the issues on… On contribute.
**atoulme** 36:10 Okay.
Yeah, I don't… I don't pay attention to… Core.
These days, I just don't have the… Diamond.
Is this worth merging this stuff, or should we just hold off, have ConfigNet come in, and kind of make everybody happy?
**Dmitrii Anoshin** 36:32 I think if it's gonna be a break and change after that, so it's better to wait.
**atoulme** 36:37 Yeah, right?
**Dmitrii Anoshin** 36:39 Andrew, do you think it's worth adding as a deprecation? I understand that it's only for Go interface, not for the end users, but do you think we can still have the old endpoint as deprecated for now?
**Andrew Wilkins @ Elastic Observability** 36:58 We could… Let me see…
**Dmitrii Anoshin** 37:05 I guess… Yeah, I guess we could… We potentially didn't break on treatment, at least.
**Andrew Wilkins @ Elastic Observability** 37:13 Yeah, I think that could be done.
**Dmitrii Anoshin** 37:15 And also… I'm not sure what… what's our policy for the embedded… embedded fields.
I understand that you… Like, you don't need to… Like, you can reuse… other config methods if it does add anything, but I don't believe it adds anything anyway. It's just… Oh, so, sorry, I don't… I think we have some kind of… Like, restrictions, against embedded… fields. I may be wrong, but I believe there is something more recently… That was…
**Andrew Wilkins @ Elastic Observability** 38:04 I think we… I think we embed, like, the config.http server config?
In lots of places.
**Dmitrii Anoshin** 38:11 By embedding, I don't mean squashing, I mean, like, the embedding goal field.
**Andrew Wilkins @ Elastic Observability** 38:18 Yeah, like an anonymous field.
**Dmitrii Anoshin** 38:20 Yeah, anonymous field, that's that one. I think… I remember someone complained about them, and we kind of make a rule that we shouldn't have them, or something like that. But I may be wrong, to be honest. I…
**Andrew Wilkins @ Elastic Observability** 38:32 Actually, no, in OTL PhDP, we're not embedding it.
**Dmitrii Anoshin** 38:37 Yeah, I don't…
**Andrew Wilkins @ Elastic Observability** 38:38 No strong opinion. I can change that.
**Dmitrii Anoshin** 38:41 I'm not saying you should change that. I'm saying, can you please take a look at some policy or some documentation, whatever, we can have restrictions against that, because I don't.
**Andrew Wilkins @ Elastic Observability** 38:51 Okay.
**Dmitrii Anoshin** 38:52 You remember?
Thank you.
Okay, I think that's… once you… once you take a look at that, deprecation and the potential policy that we have, feel free to ping me, I can… I don't have astronomy, I don't have any… Concerns about just exchanging it.
**Andrew Wilkins @ Elastic Observability** 39:23 Thanks.
**Dmitrii Anoshin** 39:30 We're good for today?
**atoulme** 39:31 Yeah, time to go.
**Dmitrii Anoshin** 39:33 Thank you, folks.
**atoulme** 39:34 Thank you. Bye.
**Dmitrii Anoshin** 39:35 Okay, bye.
