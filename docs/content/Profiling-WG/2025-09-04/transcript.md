SIG: Profiling WG
Date: 2025-09-04
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Alexey A 00:04:00 Okay, can you hear me?
I can see that… So, looks like, Felix is… Says he's not on the computer.
Hey, Felix, yeah, I can… I'll… I'll take it.
Can you hear me?
Felix 00:04:19 Thank you. Yes, thanks.
Alexey A 00:04:20 Okay, let me just open the notes… And, I also turn on the video.
Okay, I think we usually start with just checking the… the action items… So… Sorry, just moving windows around.
Yes, so for… Yes, review action items. The first one is, for me, right, the profiling signal for the consistency check tool.
This is, this is in progress. I linked, a work-in-progress diff. I added more checks, but I… I still need to add… I still need to complete some, like, the initial set of checks, and also add tests.
And once I do that, I will… I will send a pull request.
One set of checks that I also want to add, but probably it will not be in the initial set of… the initial pull request is, checks for uniqueness. For example, that, a check that For example, like, when we encode… in the stack… in the dictionary tables, basically, I… I think we should check that the… there are no duplicates, because it's… I think it's an easy way to ensure that producers are doing the right thing.
Maybe it should be some… some sort of warnings, but I'll probably just… add them as, mandatory checks as well, but we can… we can discuss also on… on the pull request, it's, yeah.
Then next is Florian, is Florian here? Florian, and yeah, also.
Christos Kalkanis 00:06:36 I think Florian will not join us today.
Alexey A 00:06:40 Florian… okay, Florian will not join, and so I should add myself here.
For actions… I think for review actions, we don't capture, usually, we don't usually capture notes, so we just… okay, And then a review context propagation documents. Was it for everyone? I don't see that it's… there's an action item, but it's not assigned to anyone.
Christos Kalkanis 00:07:11 Yeah, I think it's for everyone in this week. I had a look already, I left some comments myself. I think, you know, additional comments are welcome here.
Ivo Anjo 00:07:22 to share on that, but I think we should leave that for the end, because there's probably more interesting topics to cover first.
Alexey A 00:07:31 Okay, and this is, okay, I see.
context propagation… I should take a look as well. When I hear context propagation, I'm thinking trace, not… quite prof… is it… is it… is it related to trace as well?
Ivo Anjo 00:07:53 Not yet. Basically, we have two documents, one for the process level data and the other for, like, the trace level data, and, like, I… we've been iterating more on the process level and haven't touched the thread level stuff for… for a bit of time.
Alexey A 00:08:06 Okay.
Oh, sounds good. Yeah, so I think… So, like, taking a look at those documents is still… An action item to everyone.
And then, okay, I think this is it for… for the action items. For… for the agenda, Christos… mentions that Fabricio has graciously volunteered to help us with the implementation. Crystal, do you want to talk about this?
Christos Kalkanis 00:09:07 Yeah, so Fabrizio wanted to be here today, unfortunately he couldn't make it, so we agreed that I would introduce him. He's already familiar with OpenTelemetry, he's done documentation work in OpenTelemetry.
And he's volunteered to help us out with any auto-related documentation that we need. That covers both the release candidate, alpha, and also the upcoming stable release.
So, if we… do want to get better documentation out for the alpha, then yeah, we can start coordinating with him. He's already available for this.
Alexey A 00:09:42 Are there any standards for what we have to do, or it's all up to us to decide?
Christos Kalkanis 00:09:53 I think we can reach out to Tigran, and he will… will have better answers. I'm not sure, that's my… But we can circle back on this, I think, after we, like, we talk a little bit about what remains to be done before we have the alpha, at least counted, because maybe, you know, documentation… we need to have some documentation for the… for the alpha, I think.
So I think that's my next point in the agenda. Just a brief update. So Felix opened a 6.45 pull request with a simplified sectorized representation.
So, yeah, we decided… we agreed that I would open a podcast on that. Fortunately, there were merge conflicts, so it was impossible to kind of go ahead with Felix's original PR, so I opened the second PR to resolve the conflicts and try to get this merge in the context of 1.88.
Proto release.
The reason for that was we have an open issue inside Elastic, also for the auto profiling agent, especially. It's been blocked for a long time on this upcoming protocol release, and things, unfortunately, take a long time in OTL. So, now the new protocol is out. Unfortunately, we can't use it immediately in the agent. We have to wait for the auto collector release that will include it.
That's currently in progress.
Damien from Elastic is working on that. We're hoping we could get that done early… by early next week.
And then we can move ahead and update the profiling agents.
To take all the protocol changes that we did in the last weeks into account.
So, that said.
I think my understanding is that we don't have any additional protocol breaking changes in the pipeline. Like, everything we've discussed as much… PRs that must be merged have been merged.
And maybe we have… We need to do review passes on the protocol to ensure that everything looks fine.
From that point of view, but we don't have anything else planned that is a breaking change to the protocol itself.
Alexey A 00:12:09 Other, one… maybe one thing is all the field IDs, is that… because I think one discussion we had is, like, reorder the fields, and if we reorder the fields, this is, like, yet another, like, maybe, like, good opportunity to just get everything in order without gaps, or… we probably don't have gaps, because I think we've been, renaming, like… re… reassigning ID is pretty… Timely recently, but if we want to change the order of any fields…
Christos Kalkanis 00:12:43 Yeah, so I think in the last meeting, Jonathan, we discussed that there are some fields that need to be grouped together to avoid confusion. I think it was repeated, like, the meaning of repeated in the confusion. And Jonathan, I think, volunteered to look at that.
Jonathan Halliday (IBM) 00:13:02 Yeah, that's… Gonna come as part of the agenda item that's down the list, and talking about Merge semantics for samples.
Alexey A 00:13:24 Other than that, I… I also suggested, do we… an agenda item below to discuss, removing aggregation temporality field. I don't know if we can… I don't think, like, I would consider it protocol breaking, because nobody uses it, I think.
Other than that, I don't think anything comes to mind.
Antoine Toulme 00:13:51 Hey folks.
When it comes to these, political maturations, so did you… Did you find a way to make it map to BProf?
Alexey A 00:14:04 I don't think anyone looked into that, or looking.
Antoine Toulme 00:14:08 My understanding is that you were building a GitH repository, so you would be able to make that mapping.
Alexey A 00:14:15 Yeah, but I don't think we treat this as a prerequisite for alpha. I think we agreed that, yes, having, Having a tool, the conversion tool would be useful, but, I don't think this is… we… We treat it as a pregate for our… for our publishing alpha.
Antoine Toulme 00:14:34 Well, I mean, I came to the meeting last time and I asked about this.
Christos Kalkanis 00:14:41 So, Antoine, I think the consensus from the last meeting was that we haven't explicitly… like, it's our goal to maintain convertibility from T-proof to auto-profiling signal, right? And we haven't done anything to our, conscious knowledge that would go against that. But, you know, I mean, coronary cases may remain, so…
Antoine Toulme 00:15:01 No, no, please, let me stop you. I have actually built a POC that shows that there is no mapping, and we have a PR open with over 30 comments that shows the mapping is not working.
Your conscious knowledge is that someone tried and fell.
Christos Kalkanis 00:15:15 Right, so… We raised the same question in the last meeting, right? So the answer then was that we have multiple breaking changes, right, in the pipeline. Now, with the new proto-release 1.80, all of those have been resolved. So the current state of the protocol, as of the proto-release 1.80, Is the one that should be considered you know, alpha is able going forward. So if you did try to convert from Piprov before.
I would suggest maybe you look at the proto as it stands now, meaning 1.80, And, and give it another, another try.
Antoine Toulme 00:15:52 So my understanding is that this was something that we were going to do as part of the profiling SIG that was going to be happening in the SIG profiling repository that was built in GitHub over this summer. Is that not the case?
Christos Kalkanis 00:16:04 Yeah, I think that's the case. We plan to, yeah, to have a convertibility from prequels, and Alexi is working on a tool to do that.
Antoine Toulme 00:16:14 Yes, so last time I asked Alexey if he needed any help, and Alexi's saying no one is working on this.
Let's clarify. Alex, are you working on this? If you're not, let's make sure someone is. It could be me.
Please let me know.
Alexey A 00:16:28 I'm not working on a converter to Pprov. I don't mind working on this in the future, but I don't work on it now.
Antoine Toulme 00:16:36 Okay, so we're going to make an alpha release of profaning And it will not be particularly compatible with PPROF.
Alexey A 00:16:45 I… I cannot say it's not compatible.
Antoine Toulme 00:16:50 It's not, it's been… that's right.
Alexey A 00:16:51 It's…
Felix 00:16:53 Hang on, hang on, hang on a second, sorry, like, we do have evidence that there is some level of compatibility. For example, at Datadoc, we are converting the OpenTelemetry data into PCOS, so that direction of conversion is definitely possible and working. We have it.
Antoine Toulme 00:17:09 In production right now.
Felix 00:17:11 Converting from… People after OpenTelemetry is something we have not done, but it should be easier, because everything we've done in OpenTelemetry's format is a superset of what PProf offers in terms of fields and options, so I understand that your experiment didn't work out, but We're very confident that it's not, like, fundamentally impossible. I think we just need to specify some stuff. Florian has a PR open that introduces semantic conventions for some of the fields, like the isFolded and other things that we didn't carry over from Kitra.
And we feel pretty confident that it's generally possible in the alpha, otherwise we wouldn't go ahead. If you have very specific reasons to think that's not the case, we need to engage a little bit more. I mean, we can definitely pump the brakes a little bit and take a closer look, but I think you're overstating a little bit on how incompatible things are right now, at least in my point of view.
Antoine Toulme 00:18:05 The only thing I have is the open source work that I've done. If you think there is something that I'm missing, I would love to see it. I mean, absolutely. If I'm overstating, or making a bigger point than I should, I want to absolutely get corrected on that. Absolutely.
Felix 00:18:19 So.
Antoine Toulme 00:18:19 And that's what I know.
Felix 00:18:21 Yeah, so what I can do is, I have not had a chance to look at your stuff. I'm sure there's a link somewhere in the notes already. I will take a closer look and let you know what I think is maybe missing, and we can engage from there. And I really appreciate you pushing on this, because we have promised SSX that will make this happen. I just want to make sure that We're not, like.
sort of disagreeing, I think we're not really disagreeing here. Like, we're all in agreement that this is important. I think the only disagreement is on, sort of, how compatible we are right now, and the SICK believes we're pretty compatible. If you think it's less so, we'll sit down and sort it out. I'll comment on your code, and it's a discussion.
Antoine Toulme 00:18:59 Bless you.
Appreciate that.
Is that going to hold up the alpha release, or are we going to go forward with the alpha release regardless, or whatever we find?
Felix 00:19:11 I think if we found, like, really grave issues that could hold up the alpha, and I think we still… I don't know how fast we were going to move to the alpha, but assuming that it's still, like, at least one meeting away, I think we can sort out the issues in between, and if we really find something crazy, we could use it as a reason to hold up the alpha, as far as I'm concerned.
I would be surprised if we do, but I think it's… we should have that option.
Antoine Toulme 00:19:34 Okay.
Alright, we do, we did the freeze.
Felix 00:19:37 This is just my opinion, if you like the other stick numbers, maybe physically, please stick up.
Antoine Toulme 00:19:41 Please speak up.
Alexey A 00:19:42 Yeah, I'm… the thing is, like, I'm familiar with both formats quite a bit, and I don't see things that should be incompatible, so for me personally, like, unless we get to very specific technical, like, this thing is not compatible, then… I cannot really provide a lot of useful input, because, like, just saying, like, there are problems, well, I don't know what the problems are.
And I don't want to… like, I can infer that by just looking at the code, but what I would appreciate if there would be just a list of things that are, like, specific problems.
Antoine Toulme 00:20:15 Sure, you can, well, if you comment on my PR is probably matching up an issue at this point of what mapping should we apply to a particular setting to another.
So you can take a look at that as a starter.
But if there's something else that you can summarize, I'll be happy to try to understand that as well.
Bear in mind.
I'm no expert, I don't understand most of this, so you're going to make mostly I'm going to look bad out of this, but I'd rather look bad than miss the objects on where we are, so…
Alexey A 00:20:48 One thing I want to, like, for questions like, for example, like, what mapping should I use, or how should I write this? This is not, to me, this is not about, like, format incompatibility. I would… I would kind of, like, I would separate questions, like, how do I write a converter from… there is problem X, and… having a list of, like, problems X and Y is what I think would help the most to…
Antoine Toulme 00:21:12 Sure. Well, to me, this is a very practical issue, right? We have a P-Prof receiver we're trying to implement in the collector.
it's receiving PProv data from an endpoint, and it's converting it to a profile open telemetry Proto, and it needs to be somewhat faithful to that, right? So how do we… how do we make that conversion work in a sense that it needs to be somewhat plusless? And I really would like to be able to roundtrip this. So, taking PPROF data, moving it to up until the MS3P profile, and then moving it back to PPROF to make sure that we're not losing information when we make the conversion.
If there's information loss, it needs to be somewhat documented, so we understand what it is that we're dropping in that conversion, so we can advise our customers and make sure we understand where it comes through.
Felix 00:22:01 There should… there should be no information loss if we run trips from PProv to hotel and back. That is the goal of the sick.
If you have a hotel profile that was not originally PPROFs, there might be information loss if it uses more advanced things in OTEL that don't have PPROF mapping. For example, in OTEL, we have attributes that are more than just simple p-value pairs.
But PPROF to OTEL to PPROF needs to run through a loss as well. So if we don't have that working, we need to fix it.
Antoine Toulme 00:22:29 Yeah, please engage with me on the PR.
Be happy to go…
Felix 00:22:32 Yeah, happy to do that, and also let me know if you'd be open to, like, a half an hour Zoom session at some point, maybe it's easier to sort out a meal plan.
Antoine Toulme 00:22:40 It's gonna be rough, but I can try.
Felix 00:22:43 No, we can do offline if you prefer. For me, the preference would be doing… I'm assuming that we… let's do it offline.
Antoine Toulme 00:22:48 I just have travel in the way, that's all. I'm sorry. But yeah.
Felix 00:22:52 No, no worries, we'll just chat and figure it out. I assume you're on the CNCF chat as well?
Antoine Toulme 00:22:57 Yep, yep.
Felix 00:22:58 Okay, I'll ping you back.
Antoine Toulme 00:23:00 Thank you.
Alexey A 00:23:04 Okay, thank you, everyone. If this is… Yeah, I think… If anyone wants to add anything on this agenda item, feel free to, otherwise we are moving to the next one, and that's something I added. Should we remove aggregation temporarily field, for now? Did someone add a comment?
I think there's a plus.
From Florian.
Yeah, we have this, aggregation temporarily field, I don't think we use it, and I'm… I would rather not carry to alpha specifically something that is… just kind of, like, cargo called copy-paste, I think?
But… so I'm happy to send a PR to remove it.
But if there are objections, then please raise them.
This is also related to the sample merge semantics.
discussion, I guess, in the… in the next… In the next bullet, maybe we should discuss these things together. I would say that aggregation temporality field in the current form should probably still be removed.
maybe something… maybe some other form of it, or cleaner form of it will come up… will come out from the sample merge semantics. And for sample merge semantics, I think, This was opened by… Jonathan, I think. So, Jonathan, do you want to…
Jonathan Halliday (IBM) 00:24:41 Yeah, it's just the written version of what we were discussing in the last meeting.
you have… some… raw observations, which are data that's being captured, whether it's by eBPF or something else.
You're trying to pack them into a number of sample messages.
And if there are timestamps, the way to do that is… Fairly clear.
We, we have a… a good model for that. If there were not timestamps.
there is, I think, too much flexibility in the ways you can do that. It's, ambiguous what the… Interpretation of the, the sample is.
So, for example, if you're, Capturing a value that represents the amount of memory allocated.
Then you… you have a stack, which is the specific point in the code that did the allocation.
And you have a number which is How many bytes were allocated?
And you might have several such observations.
They might have different values, because they're allocating different amounts of memory.
It's not clear to me that it is safe or desirable to sum them up into a single sample.
Because that, for me, is a lossy operation.
If… if I have two observations, this… thing allocated 4 bytes, and the next one is it allocated 8 bytes. I do not want a single one to do a single sample of 12 bytes, because… Nowhere in my code was 12 bytes allocated.
And the receiver of that information has no way to know this represents an aggregate.
And even if they did know that, they've got nowhere to separate it back into the two allocations.
So by… By summing them up, I performed a lossy conversion, which is invisible to the receiver.
Christos Kalkanis 00:26:40 Right. Why would you sum them up?
Jonathan, why wouldn't he use multiple values for that?
Jonathan Halliday (IBM) 00:26:45 I could.
But something further down the line needs to know it also can't summit.
Felix 00:26:51 In your example, Jonathan, was it the same stack price, or two different stack prices for each other?
Jonathan Halliday (IBM) 00:26:56 Same… same stack trace, because the stack trace is part of the primary key, so you're always gonna… separate on that anyway. If they had different attributes, or they had different.
Stack traces, they couldn't be sunked, they're not compatible.
Felix 00:27:10 Right, exactly.
Jonathan Halliday (IBM) 00:27:11 The case I'm interested in is where they have the same primary key.
Can you sum the values? Can you aggregate some of that? It's a MapReduce.
Felix 00:27:19 Yeah, yeah, I mean, it's a lossy operation, but I don't see it as a bad operation. Like, this is how Go memory profiles have, say, allocations, I think. You get, like, a sum of the allocations at a given stack place.
Jonathan Halliday (IBM) 00:27:30 And…
Felix 00:27:31 And the underlying data.
Jonathan Halliday (IBM) 00:27:33 The argument is…
Felix 00:27:33 It was a separate.
Jonathan Halliday (IBM) 00:27:34 It's always possible and desirable to some, even though that's lossy.
Felix 00:27:39 I wouldn't say desirable, like, I think a processor needs to be configured by the user. The user needs to be, like, my intent is to make this profile smaller, and as a result, I'm okay with losing some information.
Jonathan Halliday (IBM) 00:27:51 My argument is that configuration is not at the exporter level, it's not the processor level.
It's at the individual sample type level, because some sample types you always want to aggregate, and some you don't.
So you say, for these samples.
Felix 00:28:06 Oh.
Jonathan Halliday (IBM) 00:28:07 police aggregate, and for these subject types, please do not.
Felix 00:28:10 I…
Jonathan Halliday (IBM) 00:28:10 And in order to do that, you have to have the complete list of sample types.
So it's not extensible.
Who needs staff to complete this? The person configuring the lecture?
The code, because there's an if statement or a switch statement in this… in the code, saying, does this aggregate or not?
And it's switching on sample type.
Felix 00:28:34 Oh, but I would think that the user, when they configure the collector, they would specify the sample type at the spring to make that configuration.
Jonathan Halliday (IBM) 00:28:42 Right, so there's no out-of-the-box configuration that will work. They always have to give all the possible sample types and what they want to do with them.
Felix 00:28:51 Yeah, either that, or, like, specify some wildcards. I think the hotel configs typically have, like, ways of… Being either very specific or Using mop plots for stuff like that.
Jonathan Halliday (IBM) 00:29:06 Okay.
I mean, I'm fine.
Felix 00:29:08 It's my imagination, I don't know, maybe somebody else's.
Jonathan Halliday (IBM) 00:29:10 If we're taking the view that there is a closed universe of sample types.
that all the things that I'm manipulating profiles know about.
Like a lookup table kind of thing, then that's fine.
The problem we have is if it's open-ended, if you can define user… specific sample types.
That were not known compile time.
Felix 00:29:34 Then you can't, for example, put them through a collector that doesn't know about them.
I mean, you could configure the collector to just say, always aggregate, right? And then you know that all…
Jonathan Halliday (IBM) 00:29:43 Yeah, yeah, you can wildcard the general case, sure, yeah.
But what you can't do is have a collector That sees a previously unknown sample type and knows a priori how to deal with it.
It has to have that knowledge at compile time, or it has to be provided with a configuration file.
what I was wondering was, is there a case where we want to carry that information on the wire? So as part of the sample type, does a… an enum field or a Boolean saying this is… this can be aggregated or not.
Felix 00:30:18 What would be an example where we would say that to no? Like, you must not aggregate?
I guess the aggregation temporality is one example, where you have, like.
samples from the beginning of time or something across… but that would be an aggregation across resources.
Alexey A 00:30:36 When I read this issue, 706, I thought the example was about something like gorge metrics, where something that is not summable by definition.
And I left a comment there saying that, yeah, like, in the P-Proof universe.
we only put into sample type, things that are actually summable, and I was asking, like, is there an example of something that we… someone would want to capture that is inherently non-summable? Because there are lots of problems with non-summable metrics otherwise, like… you cannot… take a percentage or something like that. So, I usually non-sumable things, I think, go to attributes, Like, for example, size of a location.
If you have, like, the size of a location, size of a location is… Is not summable.
Felix 00:31:27 Like, the size class, like, the size of the structure thing.
Alexey A 00:31:30 Yeah, like, yeah, like, size, size…
Jonathan Halliday (IBM) 00:31:31 Yeah, I mean, we absolutely can deal with it that way. We can say that… Samples are always summable, therefore if, for example, you don't want to sum the memory allocation, you can't use the value field for that. You, as you say, you make it an attribute, so you're making the primary key have a lot of potential values, and, you know, there are issues that come with that, but fine. It's… it's like defining a bunch of metrics.
For different sizes of allocation, instead of having on metric.
Alexey A 00:32:06 Well, I think allocated, like, live bytes metric… I think it's summable. I think your argument… and correct me if I'm wrong, but I think your argument is that, like, some… maybe we don't want to sum it.
Jonathan Halliday (IBM) 00:32:18 Yes, I want to carry the full information, because I want, for example, at the receiving end, I want to calculate a histogram.
Alexey A 00:32:26 Right.
Jonathan Halliday (IBM) 00:32:27 I don't just want an average or a sum.
So for me, aggregating is too lossy.
I don't want to take that hit.
I want the option of saying, yeah, I'll trade extra space on the wire for keeping full fidelity here.
And right now, I don't have that option, because there's no way for me to express it.
Felix 00:32:47 I know.
Jonathan Halliday (IBM) 00:32:48 You can do it through semantic conventions, I can do it by saying… Make it an attribute.
But I have to know how… I have to have some kind of documentation, or some kind of rule for how to drive the format to achieve my aim.
Alexey A 00:33:03 One thought that, comes to mind is… Even… for example, in this consistency conformance checker code that I write, and I think also in the parka code that validates the profiles, we already… we currently have this some set of, like, allowed shapes between values and timestamps. You can have Either you can have just the value, and you don't have timestamps, or you might have multiple values and multiple timestamps.
one option could be that this could be captured… that's kind of… it's not exactly, I think, aggregation temporality as it's now, but maybe there could be some kind of enum in sample… in the sample type structure that actually expresses Like, how exactly… what is the shape of that values and timestamps?
So that producer doesn't need to infer it.
Because I think… what you're saying, Jonathan, is that you could put all these allocation bytes into multiple values, even, like, without timestamps, but they could be… they could be just, like, in a vector. But then you want all intermediate stages to know that that was the intention, and it should not be aggregated. So if that would be… if that would be captured in some sort of enum in sample type, that would say.
This is, like, summable, but in.
Jonathan Halliday (IBM) 00:34:29 Yeah.
Alexey A 00:34:30 kept as individual values. Yeah.
Jonathan Halliday (IBM) 00:34:32 Yeah, and it doesn't… this goes back to the earlier part of the conversation, it doesn't have to be an enum in sample type, it can be known by configuration.
But if we do it by configuration, every node has to have the complete list of… Of sample types and what to do with them.
Felix 00:34:52 I… what I'm curious about is, like, does OpenTelemetry anywhere else have this concept of, like.
specifying what processes are supposed to do or not, because my understanding is that, generally speaking, users of OpenTelemetry are free to configure their processors to do almost anything to the data that flows through them, including aggregations, but also to drop data, to sample data, and stuff like that. Do we have prior art there? Because it strikes me as a little unusual that the needs of the backend would dictate what the processors and the collector could do.
Jonathan Halliday (IBM) 00:35:23 Well, I think that very neat, the ability to write a processor to do anything, requires… That we provide enough information for them to… to do that.
So… Making the enum part of the message format actually helps with that.
Felix 00:35:44 Okay, but going back to the complete use case, your use case is, I want to draw Instagram on the back end.
Or in the, like, UI, for example. And the user might be like, well, because it's a histogram, I need to send you a lot of data, I don't want to pay the bandwidth, so I want to aggregate this away, and all you can give me now is maybe a flame graph. And you want to basically say, for this profile type, you're not allowed to do that.
Or, like, on the… basically on the profiler level that produces the data, you want to say that, on the… on the exporter level, right?
Jonathan Halliday (IBM) 00:36:12 I don't think it's up to me to say whether they can or can't do it, it's they should understand it's a lotty operation.
Because for things that are summable, it's non-lotty, so there's no downside, you just do it, because it saves space and… There's… there's no price to be paid for that savings, so yay.
Felix 00:36:29 Wait, if you lose the timestamp, it's always losty, right?
Jonathan Halliday (IBM) 00:36:31 Yeah, saying this conversation only applies if you don't have timestamps.
Felix 00:36:37 I see, okay.
Jonathan Halliday (IBM) 00:36:37 If you have timestamps, then you have a vector of values as well, because the rule says that your list of values has to be the same length as your list of timestamps. So you can match what value was observed at what point in time.
So you can't aggregate values, because you can't aggregate timestamps.
Christos Kalkanis 00:36:59 So, like, the present…
Felix 00:37:00 I think I understand better now.
Christos Kalkanis 00:37:02 is a hint, right? So you can use the time, the presence of time as a hint to know how to interpret the data, right?
But…
Jonathan Halliday (IBM) 00:37:09 Yes.
Yeah, if you have a timestamp, you know that the corresponding value is a single observation.
Christos Kalkanis 00:37:16 Right.
Jonathan Halliday (IBM) 00:37:18 Whereas if you have a single value and no timestamp, you're not sure whether that value is an aggregate.
Or whether it was a single point in time, but you just didn't recall the timestamp.
You don't know how many observations it represents.
Alexey A 00:37:33 One thing that is kind of related is that we currently don't document or require that the shape of all samples for the same metric should be the same. Like, in theory, I could have one sample that have timestamps, I could have another sample that doesn't have timestamps, and that's pretty That probably… that would probably be odd, at least that's not kind of… That's not the shape of profiles I would expect.
Jonathan Halliday (IBM) 00:37:57 Yes. That presents an issue of, do we consider the presence or absence of timestamps, sorry, the shape, to be part of the primary key? So, can you… Even attempt to aggregate.
two things that have different shapes. Or does it not make sense?
Felix 00:38:17 Yeah, I think we should probably specify in the comments that the shape of all samples should be the same for the same sample type. At least that makes sense to me.
Those things that we can take an action item on that, unless somebody disagrees.
And then going back to your use case, specifically, it's kind of a very specific one where you have Just the values, but no timestamps, and you want to build a histogram?
Part of me kind of thinks, like, if that's the main use case, the right solution would actually be to, like, also transmit a histogram, and, like, use histogram data structures that aggregate.
Jonathan Halliday (IBM) 00:38:53 Yeah, maybe this is a non-problem. Maybe the common case is you do have timestamps, and we're… just gonna say, yeah, if you don't have timestamps, you're stuck. You can't do this without loss.
Felix 00:39:11 Yeah, I think this would be my first recommendation, to just steer people away from the… Like, producing just values with our timestamps, and then we can use the timestamps as a hint to… Say that, yeah, this is going to be lossy if you aggregate in some.
Alexey A 00:39:37 Sorry, I'm capturing some notes.
Jonathan Halliday (IBM) 00:39:39 Yeah, I mean, if we go with that, then this is off the critical path. We don't need to look at adding an enum field, which honestly would be a… I changed the protocol.
Felix 00:39:53 Yeah, I mean, I sort of get it when I see the temptation for the enum field, but at the same time.
It would be yet another complexity in the protocol, so if we can find a simpler solution, that'd be nice.
Alexey A 00:40:09 Yeah, it's tempting to add more structure, but more structure is also more complexity, so maybe we should… I think we can definitely at least, like, leave Alpha without it, and this is… This can be… this can be added. And I think… Adding good documentation would be a good step towards that, because Once we document things better, we would… We would know what the… actual shapes are.
Yeah.
Felix 00:40:41 and look… I had… at some point, I had, like, some examples of combination of shapes and what they're good for. I want to check what I had in mind for the just value state, because I'm not on the computer right now, but… Yeah, maybe we should just discourage that case and say, like, that's not a well-supported state.
Alexey A 00:40:59 Yeah, and in the conformance checker, I plan to ensure that the shape is the same, but it would have to be a bit heuristical. It's like, oh, let's see what the shape of the first sample is, and ensure that everything else has the same shape.
Felix 00:41:16 That works.
Alexey A 00:41:18 Yeah.
What about the grouping of the fields? Because I think that was the original motivation, Jonathan, that you… That you started looking into this?
Jonathan Halliday (IBM) 00:41:33 Yeah, so if we're making other breaking changes anyway, then changing the field order… might make sense. Otherwise, we can probably address it just by putting comments into the proto file to say, this is the tuple over which you Calculate the primary key.
I'm kind of reluctant to break the protocol just for that.
Alexey A 00:41:59 I'm fine either way. I think the current order is, let me… Just look at the proto real quick.
Stone Ball…
Jonathan Halliday (IBM) 00:42:13 One thing that I did notice is that when you're calculating the primary key, if you're hashing something like that.
You've got a set of attributes, a list.
And the order in which things appear in that list matters, so you basically have to sort it before you calculate your key.
For a joke.
Alexey A 00:42:35 attributes, right?
Jonathan Halliday (IBM) 00:42:36 Yeah, yeah, yeah. If you've got multiple attributes, they might be equivalent, but if you present them in a different order, they appear non-equivalent when you do array comparison, so you have to sort the array first.
To what extent do we want to make conventions around, for example, samples have to appear in temporal order, and keys for attributes have to appear sorted, and so forth?
Do we want to write a sort of normalization?
To make it easier to compare things.
That seems to be putting more burden on Anything that generates a message to ensure it's well formatted, but… Then the receiving side has an easier time.
Alexey A 00:43:18 I… I don't have strong opinion. In the checker that I write, I'm going to sort anyway.
And kind of, like, not require that.
I think.
Christos Kalkanis 00:43:35 Yeah.
Alexey A 00:43:36 If we would require… if we would require that every producer does that, then I… I would be glad not to have to do that, but I think it's… I think it's difficult to ensure, and… And also, sometimes I just… I feel that, like.
producers… it's good if producers' life is a bit easier. Of course, if they don't sort, then how do they ensure.
Jonathan Halliday (IBM) 00:44:01 In this specific case, if they want to aggregate samples, they have to sort, because they need to know what the primary key is.
But again, with the checker.
Is it valid to send two samples that have the same primary key? It's inefficient.
But is it broken?
Because the easiest possible thing is just not to get… not to aggregate anything.
Alexey A 00:44:28 I would expect that if there is a single value, then… You should aggregate if you basically don't carry Multiple, well, like, if you don't have timestamps, or, like, if you don't have timestamps…
Jonathan Halliday (IBM) 00:44:42 Now, if I… if I have two observations that have the same primary key, so they could be combined into one sample.
With two timestamps.
What if I instead send two samples with one timestamp each?
Is that actually a protocol error?
It's taking up more space on the wire, but I think it's a valid encoding.
Christos Kalkanis 00:45:02 I think it should be fine.
Felix 00:45:03 I could also state that, yeah, I think it should be valid, and we… the checker could emit a warning, which you suggested earlier, Alexi. I think a warning level makes more sense to us.
Christos Kalkanis 00:45:14 Yeah, I think we should not over-specify implementation requirements from the producer side for multiple reasons. Like somebody else said, yeah, we're making the producer's life harder, and also different producers have different requirements.
Alexey A 00:45:30 Yeah, but at the same time, I think it's also, like… the reason I'm thinking about warning is… it's also nice to inform people, because maybe someone is just doing this because, like, they didn't think of, like, oh, I can actually aggregate these things and make my profile 100 times more compact.
Christos Kalkanis 00:45:47 Yeah, that's… that's great.
Alexey A 00:46:02 Does this apply to other, like, for example, can you have multiple call stacks that are identical? There, I assume the answer is no.
Felix 00:46:13 I'd say this is also one…
Jonathan Halliday (IBM) 00:46:15 I think with the whole dictionary encoding, you can… you can legitimately have… Multiple identical entries in a dictionary table. It's really inefficient.
But you should be allowed to do it.
Felix 00:46:29 Yeah, I would also say inefficiency should be allowed, because maybe a producer sees some space-time trade-offs for making some inefficiencies happen on the wire protocol, and we shouldn't be too strict about it. But we should definitely warn people when they do inefficiencies from the wire protocol perspective.
Alexey A 00:46:57 Okay, cool, I captured that. Feel free to add to… to the nodes, if I missed anything.
It's just… it's a bit difficult to run the meeting and capture all… and participate in discussions and run the… and write the notes at the same time, so if I missed anything, please record that. But other than that, so I think the… the conclusion is we are not adding a num. We will try to improve the documenta… we will review and improve the documentation on on the shape of the samples, we will probably continue this discussion as we learn more. We will not reorder. I think we are leaning towards not reordering the fields in the in the proto, even though, like, the current order is… I, like, I wish values would be near timestamps, and currently they are not, but… Yeah.
Christos Kalkanis 00:47:54 I thought we decided in the previous meeting that we would do that. I don't think it's a problem, to reunion.
Yeah.
Jonathan Halliday (IBM) 00:48:01 Temporarily, we can just reorder the… the text without changing the field numbers, right? Because it's the field numbers that'll break the protocol.
Christos Kalkanis 00:48:13 I think even changing the fill numbers and breaking the protocol is still fine, because, like, for example, the development work that is in the pipeline right now, updating the auto profiling agent to take into account the new protocol, those will not be affected by this change, right?
So what I'm really… Losing by updating the field numbers as well.
Jonathan Halliday (IBM) 00:48:36 Yeah, we potentially have a window of time where someone's on 1-8 and someone's on 1-9, and.
Christos Kalkanis 00:48:42 But I…
Jonathan Halliday (IBM) 00:48:42 He had incompatibilities, but… If we can live with that, then yeah, let's do it.
Felix 00:48:47 Can you remind me on the purpose of changing the ordering? This is not about a picture, this is purely aesthetic, or…
Jonathan Halliday (IBM) 00:48:53 Yes, we have certain fields that are part of the primary key, so what you want to hash over, if you're saying are two samples identically, so they can be summed together.
So they can be aggregated.
And we want those primary key fields to be Listed together.
together.
And then the… the ones that are the data, the aggregate data.
Which is the values and timestamps to be… Listed after them.
So yes, it's purely aesthetic to make it clearer for people reading the The proto file, what the semantics are.
Felix 00:49:35 Okay, yeah, I don't see it strongly about it.
I guess it is a check we could make while we're an offer.
Christos Kalkanis 00:49:56 Yeah, I think we should do it. I mean, now is the time to fix all those little, you know, problems, and, like, people reading through sample, it's confusing. It's at the very least confusing, and yes, we could, you know, iron this out through documentation, but why not go the full way and just make sure that everything is perfect, in that sense?
Alexey A 00:50:16 Sounds good to me.
Felix 00:50:18 I mean, the downside, let's be conscious about, like, early adopters, anybody who rolls out, like.
Working with the old silk ordering.
And already consumes data from them, clients in some environments, we'll have a pretty… Difficult time once we change the fuel bottling, right? Because they will not be able to store the old and the new clients at the same time.
Christos Kalkanis 00:50:41 Right, but… Yeah, go ahead, go ahead, Alex.
Alexey A 00:50:45 But we've been changing field IDs quite a bit back and forth. There's nothing particularly magical about 1.0 release before we declared alpha, no? Or did we want to declare alpha on 1.8?
Sorry, 1.8. Did we want to declare alpha on, like, 1.8 as is?
Felix 00:51:03 Oh, okay, that was sort of my assumption, sorry if that's not the case.
Stop mine.
If we plan to do another protocol release before Alpha, then I have no concerns with changing the script numbers at all.
I think only after Alpha I would be a little concerned.
Christos Kalkanis 00:51:20 Yeah, so Tigran said that we can ask for a new protocol release at any point, and those can happen quickly. Then the Autel Collector team releases every other week.
So, you could probably go for 1.9 and still hit the end of September, which I'm assuming is where we want to be for an alpha release, or close to that, maybe early October.
Felix 00:51:45 Okay, then let's aim for that.
And also, that gives us a chance to work with Antoine on the, deeper of round tripping uncovers anything that gives us a little time, so I would… I would vote for that. I.e. change the field numbers and plan on making the next, proto-release here. It'll be my…
Christos Kalkanis 00:52:08 Sounds good.
Alexey A 00:52:12 Jonathan, will you send… a change to…
Jonathan Halliday (IBM) 00:52:16 Yes, I'll… I'll PR for changing the sample.
Alexey A 00:52:20 Okay, okay.
Jonathan Halliday (IBM) 00:52:24 Are we dumping aggregation temporarily as well, then?
Alexey A 00:52:28 Yes, I… I plan… I will… I will send the PR.
Jonathan Halliday (IBM) 00:52:31 You'll do that one, great. Thanks.
Alexey A 00:52:33 Yep.
Cool.
And the last… we have 8 minutes left, and there's one last bullet update on context propagation.
Christos Kalkanis 00:53:01 Yeah, I have one point, sorry, to hijack your… it's also related to the alpha, maybe we should get this over quickly. It's the Go build ID that we previously discussed. I think someone from Datadog left a comment in the eBPF Profiler repository.
giving reasons for us to keep the GoBuilt ID. I think one reason was that the Go compiler It's only a recent version of the Go compiler that produces the new build IDs.
And then the other reason was that Basel, when it compiles, Go, it puts redacted as the Go build ID, and then it takes that and hashes it and produces the GNUBuild ID based on that.
So, I mean, basically, yeah, there are…
Jonathan Halliday (IBM) 00:53:43 Did we not remove this already?
Christos Kalkanis 00:53:46 I don't think so. Let me… let me have you, as far as… unless it happened while I was away, maybe.
Nayef Ghattas 00:53:51 No, I don't think so. I think it's in semantic convention that we have a profile type for Google Digi.
We will tag it up soon.
Jonathan Halliday (IBM) 00:54:04 Yeah, I don't think there's a field for it in the protocol.
Alexey A 00:54:08 Yeah, I think, I think we moved it to semantic conventions.
Christos Kalkanis 00:54:11 Yeah.
Jonathan Halliday (IBM) 00:54:12 outputs.
That's not a breaking change on the protocol, if we want to.
do that later.
Alexey A 00:54:18 Christos, do you want to take an action item to look into this and… Send the… send the change to remove it. Doesn't have to be… Since it's not protocol breaking change, this can happen at any time, but…
Christos Kalkanis 00:54:30 Yeah, I guess the question is, do we want to remove it? I would be fine with keeping it and maybe deprecating it at some point. It doesn't hurt anything. We already have a semantic convention there, so removing it would be us going back to semantic conventions and just asking for deprecation.
So… Yeah, like, in the sense of supporting existing, use cases, we have someone who, you know, complained and would like it to be there, so it does… I don't think it hurts us to keep it around. And, you know, at some point, we'll mark it as deprecated.
Nayef Ghattas 00:55:01 Yeah, so for more context on this, internally, we use the new build ID as a way to associate symbols with… as a main way to associate symbols with a specific binary.
And so we, for Go versions that are before 1.24, I think we don't have a new build ID.
but also for those… for GoBinoids that are built with Bazel, as you mentioned, Christos, the new build ID we have is just a hash of the string redacted, so we cannot rely on it. So, the use case for us is to be able to just use that extra information to be able to Both, make sure we can associate, the binaries from older Go versions with symbols, but also have a way to detect that a binary was built with Bazel, so we shouldn't take into account the GU build ID, because it is basically not useful.
Alexey A 00:56:08 Okay, keeping it for now sounds good.
Thank you, Christos.
Ivo.
Update on…
Ivo Anjo 00:56:20 Yes, I'll try to make…
Alexey A 00:56:22 You have exactly 4 minutes.
Ivo Anjo 00:56:25 Yes, no… no pressure. Okay, so just to… for context, what we're… what I'm meaning here is, like, this document, which is, like, the… one of the ones that's listed.
Here.
And we're talking about the, having, applications be able to publish, like, process-level information, so things like service name, deployment environment, etc.
And kind of previously, we had this, this kind of proposal where we were saying, okay, we, we're hoping to use anonymous mapping for this.
And… but there were, like, a few open questions about, like, open kernel support and a few more things, so what we've been doing since is we've introduced, like, a reference implementation that, like, does the whole thing, like, in production-like code.
And we've been experimenting with wiring it in, like, Java, Ruby, Go, and also on, like, our own… our branch for the experimental stuff for the OpenTelemetry profiler to make sure that this kind of makes sense.
And the kind of… the… I've just added today a bunch of… on top of this, I've added, like, the format that we're proposing.
And we basically have, like, this header that specifies a few fields, and then we have a payload that's just a string that's encoded with message pack, that then has, like, a few fields, like the host name, environment name, service name, etc.
And kind of what, at this point, what we're hoping to get is, kind of take the temperature of, does the C kind of think that this is in the right direction? In particular, as well as we're using message packs for the payload format, does this make sense, or should we look into JSON, or Protobuff or something else?
And my intention is, if, like, in the profiling SIG, this looks like something reasonable, I will go start chasing the other tracing SIGs and the SDK folks to make sure that this also works for them. So, I was kind of, hoping to, like, just get first, like, temperature from the profiling SIG before I involve way more people in the back-and-forth discussion.
And I just said that, yes, we kind of have this working, and it's, yeah, we've kind of validated this seems to be working fine.
Jonathan Halliday (IBM) 00:58:52 So, as someone who's profiling SIG, but also Java SDK SIG, I loathe adding new dependencies to the VIN SDK, so message pack isn't on Starter.
Given that we've… we've already got Protobuff.
Can we please just use that instead?
Ivo Anjo 00:59:11 Yeah. yes, the… I will add one caveat, but it's not, like, it's not, like, against one or the other, is that it's very easy to implement a message pack encoder, and our reference implementation in C code implements, like, the encoder bits for the format in, like, 100 lines of C code.
Jonathan Halliday (IBM) 00:59:31 But, yes, if…
Ivo Anjo 00:59:32 If we still want Protopath, we can go Protopath.
Jonathan Halliday (IBM) 00:59:45 see what the SDK syncs say, but…
Ivo Anjo 00:59:48 Okay, I'll, I'll add gear now.
Jonathan Halliday (IBM) 00:59:49 I think the answer from the Java world will be… No more dependencies. We hate dependencies.
Ivo Anjo 00:59:56 But, kind of… that's my question. If I can… if I can get you 100 lines or 200 lines of Java code that implements message pack.
Is that still no, a no, or is that…
Jonathan Halliday (IBM) 01:00:08 I mean, at that point, you don't use a dependency, you just copy that code into the SDK codebase, which, they've actually done with protobuf in the Java case. They have their own protobuf encoder, instead of depending on Google's. That's how much they hate dependencies.
Ivo Anjo 01:00:23 Yeah. Because the format is, like, message pack is really stupid, so, stupid easy, so it's, like, yeah.
Jonathan Halliday (IBM) 01:00:31 What's… what's the reason for preferring it over Protobf?
Ivo Anjo 01:00:36 mostly that, like, Protobf is a bit, protobf is a bit more awkward if we want to use it, like, in C, like, the reference implementation, so that's why, like, I don't think… I'm not sure we can make, like.
Jonathan Halliday (IBM) 01:00:46 Has anyone that's using it not already got Protobuf anyway, because it's part of the hotel ecosystem that's using Protobuf every day.
Ivo Anjo 01:00:54 That's a good point.
My, my, yes, kind of my, my, my thinking was, like, if we did, like, the, the, this way, we, we could, like, have a standalone reference implementation that everyone wants to use, that has no dependencies, including That's kind of, like, the thinking that led here, but again, this is the kind of feedback I was,
Jonathan Halliday (IBM) 01:01:18 Yeah, no, I think real-world deployments are probably going to be with an OTEL SDK that already has product buff handling. Yeah.
Ivo Anjo 01:01:26 Yeah, that's very fair.
Alexey A 01:01:31 Okay, and we are out of time, so feel free to add any agenda items for the future meetings, Otherwise, thank you all, and see you in two weeks.
Ivo Anjo 01:01:44 Thanks, everyone!
