SIG: Arrow SIG
Date: 2026-04-16
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/sZT5hI5wwvm9X4Ro5ThxL46P93Bii75IT0J0aHuGHFy0VRljkERiHx5cFPsbh-uR.SZdMbidj7kwQhgJU
============================================================

## Zoom Recording Transcript

Jake Dern 00:01:02 Hey, good morning, guys.
Aaron Marten 00:01:08 Winn.
Gokhan Uslu 00:01:10 Good morning.
Jake Dern 00:01:14 Hey, Laurel.
Laurent Querel 00:01:17 Hey, Jake.
And hey, everyone. Sorry.
Why don't you just realize that, multiple person while they're… whether… Can share my screen.
Tricky… And… Can you please add some, element in the agenda.
As you wish.
So… 1 to… And also the list of attendees.
Thank you for the updates.
Who knows?
Cadence.
Okay, I think we can start with the… Triage felt.
We probably have… we probably have a lot, So, support the Open Telemetry entity protocol, that's something that, Yeah, that looks like an interesting one.
I think it's important to support that.
Any, any issue with that?
place to configure URI provider, I think that's… Yeah, that's something we added that is already supported by the GoCollector.
I don't think that that will be a big deal. I can select it to… to do a… A massive bit. Support the matrikian metadata field.
Yeah, I'm probably not a big deal to detail level metrics for compressed.
Okay, yeah. Add life pipeline or configuration, shut down control.
and the S2Dadmin API.
That's something I want to demo today.
If the time, if we have time I think it's a fundamental, capability. We need it for some internal project inside a file.
I don't think it's a… I think it's a good… a good capability.
That was missing, in the GoCollector.
At least by default, build cash needed.
Oh, yes, I think that's definitively a good… a good thing, evaluating the difference between cargo test and cargo next test. I think we have been, at the minimum, CJ and myself trying to… to leverage Next Test, without success.
And personally, I'm still using cargo tests on this specific project, even if I'm sol… for some other project, I observe a different, an opposite result. But for our project, in my opinion, cargo test is… At least two times faster.
I don't know exactly the reason for it.
But definitively, we need to evaluate.
and a tap exporter can lead to reset stream very often. Yeah, so that's something we discuss, Jack and, and Albert, multiple times, It's basically being smarter to reset the stream, and unless we reset, More we can reuse dictionaries, and reuse the existing schema, and… And beta will be the compression, right? So it's… It's like, Improving the behavior of the protocol to improve, at the end of the day, compression ratio and so on.
Otlp, batch, OTLP, benchmarking metrics have irregularities, you know, definitively.
Trace consistently look worse than the other single types.
Jake Dern 00:09:14 Yeah, just a quick comment on this one. So I think it might just be because the default data generation settings for traces generates just a lot more data.
I think that's supported by the fact that, like, the network bytes is much higher for these benchmarks, than the other ones, but I do think it's worth just double-checking and making sure that's the case. And we might also want to tweak the benchmark, like, data generation, just to try to You know, like, level these out a little bit, just so traces don't, like, always, like, look bad, and then, you know, people are like, oh, why are traces so slow? It's like, well, they're not. It's just generating 3 times as much, like, you know, bytes.
Laurent Querel 00:09:54 Yeah.
Sure, sounds, good to have, I mean, we, we are entering into, Personally, one of the focus for the next week will be to make sure that we have, And accurate, and, and good benchmark comparing the GoCollector with the rest, engine.
So anything that will, buy, additional, like, you know, I see, confidence in.
In what we compare and what we measure, we'll be, More than welcome, in my opinion.
columnar query engine comparing field with different types, nuels, blah blah blah.
Yeah, that's definitely something for OPL that needs to be, address to generalize the system, the language.
OTAC query engines support logical expression with a scalar expression.
No, that's in the same, You want to say something specific, Albert, on that?
Albert Lockett 00:11:01 Oh, no. If you're gonna say that this is something we should do, then I fully agree, we should do this.
Laurent Querel 00:11:06 Same thing for this one.
Support additional weight for variants. So, just before that, I'm super happy to see that we have more and more systematically, GitHub issue here.
For any, bureau?
That's really cool. That gave a lot of context, and that's definitively, a good practice.
So, support additional waveform variants for validation framework test container, yeah, that's something we need, for this validation framework. There are some Generic parameter that were not directly accessible from the The build-up pattern use into this validation framework.
Superparametric internal telemetry level configuration.
support. Oh, Joshua, you are there, and you want to talk about this one?
jmacdonald 00:12:05 Sure. This one… hi, sorry I'm late, reboot. The… the collector… the Go collector had filed one just the same as this recently, and I realized that we didn't file this one. I know that there's an interest in having, like, finer control over metric granularity than just the node level, so… I thought I'd record it, and it's related to the SDK document I have open, so it's something I'm including in my scope.
Laurent Querel 00:12:33 Excellent.
What type query engine support, any value columns in expression?
with different type in same batch. Yeah, that's similarly to the other, OPF stuff.
making the query on genetic a bit more generic, I guess.
track the FNG, that is definitively, We are working on obsolability, we have to do that, definitely.
investigate, make Non-component feature optional.
jmacdonald 00:13:10 I can… I can speak to the four that are, all here. So I started just really wanting to know the binary size. I think that's, almost everyone's going to agree to that. And I did a preliminary analysis to look at, like, where… where is the size going? And you can see it in The second issue is where I list… I kind of just took a course look. Like, if our binary is 100 megabytes.
It's like 20… it's like 20 megabytes of stuff we can't avoid, it's… 22 megabytes of data fusion, it's 11 megabytes of Arrow, and then, and then there's some stuff that we can certainly make optional or remove Cruft. There's more than one copy of the SSL, like, libraries right now, or TLS, and I'm confused about it.
So, we should be able to visit… to observe that. I think we should be able to turn off the admin console. As an example, it has a 1MB JavaScript blob, for example.
That's the easy stuff.
To agree with. I put in a couple more speculative ideas, just to, like, have them out in the world, even if we think they're terrible ideas. I want to just quickly say, the evaluate the feasibility of an arrow-free build is, like, me thinking about how, in a small use case environment where you've got a low resource and you're just moving OTLP around, you might consider… just consider what would it be like if we put feature flags on the Arrow and the OTLP, like, the different representations because 30 megabytes is Arrow and data fusion, for example, just thinking out loud, I… it's not… it's not something that I think is practical, or very practical. And the last one…
Laurent Querel 00:14:44 I'm hoping that you will, you will, just on this one.
That means that you will not support most of the processors, right?
jmacdonald 00:14:52 It's true.
And that's… that's one of the now… the points I discussed. Last one is, looking for a bridge to the Go Collector in one way. We've seen now that you can load WASM plugins really pretty easily from the Go Collector, and if there was a subset of our codebase that could also be compelled to WASM, that would be a very straightforward way to integrate the collector.
With us. And that was one of the things we promised we would try to do, so here's another issue that's sort of about that. It looks into which crates have a dependency on native code, which crates don't, and so on.
It's not impossible, this one.
Laurent Querel 00:15:28 I have a question regarding this one.
Because we could imagine multiple approaches, for a WASM integration.
Are you thinking about having the engine itself as a WASM component?
integrated into the GoCollector, or are you thinking about, for example, a processor that comply with a WASM interface, and this processor could be deployed either in the Go collector supporting WASM, or the REST engine. This one, I totally buy it. The other one, I'm not… maybe.
jmacdonald 00:16:05 Yeah.
I'm thinking of both, and but the issue was about the first of those, and And I've… as I've thought about it since even, like, yesterday when I filed it, it's maybe not practical, and what you're describing sounds more like an alternative engine for running our components inside of a WASM plugin, which… I would also be interested in, but it's a different issue.
I was really thinking about the case where we say, take a Go collector, leave its exporters and receivers untouched, and swap in a data flow engine for the processor chain, which would not be… The only way to configure Walsum or Rust and Go together, but one of the ways.
Laurent Querel 00:16:51 Okay.
But for Cesar nightly benchmark should be using fresh data generation, not pre-generated.
Can you describe this one, Jake?
Jake Dern 00:17:02 Yeah, this is actually how I intended it to work previously. There's just a disconnect in the templates, like, one parameter not getting drilled down, but basically, like, if we're not, using fresh data generation, then the compression rate is insane, because it's just… 5 copies of the data in the same, like, batch. Yeah. So… Yeah, yeah. So there's a PR out for this.
Laurent Querel 00:17:27 There is probably, something to do, I think it's… it's probably already solved, because CJO has, on one side, an issue with… what you name fresh data generation that take much more CPU usage than the pre-generated.
And for the, the scalability tests.
That's a problem because we have more, generator than we have, who are used for the, the system and dotest.
So I think, depending on the type of benchmark and the focus of this benchmark.
I think we… we… we will alternate between these two approaches, probably.
pipeline, right, due to new ROS version with new clip, blah blah, yeah, that's the type of fusion we have to… Okay, so, mark as… no, I try to… I label, and then triage… Excellent.
Ted… I like those bulk.
jmacdonald 00:18:39 action.
Laurent Querel 00:18:41 S-soy?
jmacdonald 00:18:43 I like your bulk action. I was doing it… we were doing it one at a time.
Laurent Querel 00:18:45 Yeah.
Yeah, I think it could be, that could save a lot of time, if that works.
And the true, in fact.
Oh, bulk update in progress! Look at that.
We still have the deciding, but maybe I can now… Deciding and remove it.
Hmm.
I don't know, why I can't.
But, okay, I don't want to spend too much time on that. So, Josh, I, Right now, we have only one item in the agenda.
the live reconfiguration demo. Is there any other, Topic to discuss today.
jmacdonald 00:19:38 I… Don't have anything prepared.
drewrelmas 00:19:43 I… if we have the extra time, we could talk a little bit about, processor chain.
Laurent Querel 00:19:50 Yo.
drewrelmas 00:19:51 I'll… I'll drop a link.
Laurent Querel 00:19:53 Okay.
I can…
jmacdonald 00:19:57 briefly describe my, open PR draft with the metric SDK, just to let people see what I'm up to.
Laurent Querel 00:20:05 Luca.
Well… what is the order? How do you want to proceed, guys, in terms of who is starting?
The next phase of this meeting.
jmacdonald 00:20:22 Drew, do you feel like going next?
drewrelmas 00:20:25 Sure, I can do that.
So I think to start, we should just take a look at the issue and at the latest, comments on it. So it's the top link.
Laurent Querel 00:20:38 No, the top link, okay.
drewrelmas 00:20:43 Okay, so to reiterate, I know some people reviewed my initial draft PR on this, but just to reiterate, we… I'm… for an internal use case that we have, I'm… Was initially looking at ways to… Produce a composite duration metric for a number of well-understood processor interactions that… excuse me… Our, like, from a user perspective, it looks like one logical operation to produce some transformation on the data, but in our internal knowledge, we actually use multiple processors.
Excuse me, my voice is cracking.
we use multiple processors for performance reasons, and they each do their own thing. So I was just thinking about, with our existing metrics, it would be less clear to a user who's expecting, like, one duration from this logical operation.
So I was originally approaching this as simply a composite timing, producing another metric signal, but it became very obvious to me, thanks to Laurent, especially for your feedback, that there's a better benefit here, which is reduced memory consumption. If we actually chain processors together, eliminating channel.
Passage of data.
So, essentially, if we… if processors are doing certain things, and the issue gets into this, especially in my latest comments on it.
Not all processors will be immediately compatible with this, because, take, for example, FanOut. It depends on features like named out ports.
Sending to multiple channel destinations, which kind of breaks the flow here. Lauren, if you could scroll down to the bottom, I think, looking at the most recent comment.
Is probably the best.
Her… my… my big.
jmacdonald 00:22:51 Just a lot of us.
Laurent Querel 00:22:52 Oh, sorry.
drewrelmas 00:22:54 My big one, yeah, that one.
Laurent Querel 00:22:55 Oh, okay.
drewrelmas 00:22:56 So…
Laurent Querel 00:22:57 Starting here, okay.
drewrelmas 00:22:59 Right.
So… There was a world where we just, report a composite metric.
continuing with channels in between processor nodes. I did a little bit of prototyping in this way, we don't have to read through everything here, but one other thing I wanted to bring up that Josh initially suggested was, what if we stamped P… what if the way to compute a composite duration, not just between processors, but between any two nodes, is putting something like a stopwatch on context that's traveling with P data throughout the pipeline? And that way, we could have, you know.
You could technically define any set of nodes as the entry point and exit point for a chain that you're interested in a composite duration about.
However, I think, you know, the more I read people's feedback and thought about the memory reduction, I thought the easier use case to start with is actually the version that eliminates channels, which I'm calling inlined.
Which is a very simple… it's only compatible with processors that have, like, one… one input to one output. It's not expanding, P data size at all. So that's… I do have a new PR draft out, Laura, if you scroll down a little bit more.
there's… I mean, there's a lot of information here that I don't necessarily want.
Laurent Querel 00:24:39 This one? No.
drewrelmas 00:24:41 Yeah, actually, could you scroll down to Lalit's comment? It's the very bottom one. I think that's the one I'd like to talk about.
There were a few issues here. One is that, as I said, like, not all processors can… immediately comply with this channel elimination strategy. So, it was… initially, I was thinking, oh, I'll just put, like, a Boolean on every processor config that says, is it… is chainable or not? But there was some awesome feedback here about making it more structural and introducing a new trait that… Forces processors to comply with the restrictions imposed by… the processor chain. So, the draft PR that I've linked down below has more information about that. There's a note about sub-stage telemetry. This is kind of an optional thing. Basically, does the user Actually want to keep getting metrics from the internal nodes, or should they all be treated as a black box? What I mean by this is, if you declare a processor chain with 3 nodes, do you want to get 4 duration metrics, one for the chain.
and 3 from each of the internals, or do you only want 1 for the chain? This is pretty easily controllable just with a Boolean in the processor chain config, to turn on and off internal metrics.
And then, the third point, again, talks about… How do we get a… how do we, at least for the initial implementation.
Enforce that processors that participate don't violate, Certain constraints that don't really make sense for the inlined chain version.
From… we could jump over to the PR now, if you'd like.
Or I can stop there if anyone has… Commentary.
Laurent Querel 00:26:50 Sorry. I have two commentaries, So, honestly, it's… there are a ton of very interesting ideas into this thread. I need to spend much more time But that's a very, very cool, there are many cool ideas in this thread, definitely.
Thanks for working on that, and all the people that are interacting on it.
The… the Silum thing is… I had multiple times the question why the processor is… the processor thread is designed the way it is.
I think that's a perfect example why it is this way.
To compose a processor together, So, if you look at the trade for receivers and exporters, They are… You have a stop method.
And, they basically consume everything, and then they work in their own world.
But that means also that they are… less composable, because you can't, interact inside. It's their world.
For the processor, we have this process method.
And the loop for the control messages and P-data messages are… is outside.
For this exact reason, that we… we want to… Be able to compose the processors to create More optimized chain, or some chain that will, comply with some properties, or some, I mean, we can imagine many things. The initial rationale was, okay, how can we optimize mechanically By observing the topology and the nature of the processors, how can we optimize them to create shadow processors that get rid of Channel that get rid of some other element that, cost, globally.
So that's… that's an answer to why we, we, we follow this pattern.
And I'm super happy to see that there are many variations around it.
drewrelmas 00:29:00 So, it's funny you mention the process method, because the new trait that I've defined in my… in the draft PR I have open, which is, like, an inline processor trait, it defines a new process inline function, which has slightly different… input parameters compared to the process function that all processors implement today. And essentially, the engine construction, based on where the processor… is it inside a chain or is it not inside a chain? There's a separate, factory method to set it up to either call process… so, like, a processor can implement both process and process inline, and they should both do the same work, just in slightly different ways.
As I'm saying this out loud, it occurs to me that maybe that's not the best, thing to have. It's, like, two duplicate, implementations for every node.
But it's something that we can definitely refine.
Laurent Querel 00:30:02 Yeah, definitely they need to look at that, because having two entrepants doing more or less the same thing looks like, Strong idea, but maybe there is a good reason, we need to think about that.
drewrelmas 00:30:16 The draft that I've linked at the bottom is the new… So, I had a.
Laurent Querel 00:30:21 Previous one?
drewrelmas 00:30:22 Closed. That's the new one, yes.
After this round of feedback.
Laurent Querel 00:30:28 And that's the inline process, supposedly inline.
Okay, the only… I'm not sure that it's really, fundamental.
why the effect on Blur could not be just… because… the effect on Blur is… you have two options. Either you return something.
And you can maybe get rid of some element of the… the effect on blur, which is not always true, because effect on blur will be used for… not only for, For sending data to downstream, Element, but to do Going direction.
drewrelmas 00:31:17 If you scroll down a little bit, it'll talk about what the… yeah, here. So, when the processor chain executes.
It calls process inline on all the subs, and then it uses the real effect handler.
to send out. So, like, the chain is the only one that sees the effect.
Laurent Querel 00:31:37 I understand that.
that's… I don't see a big advantage.
Maybe there is, I need to go much deeper.
Sure. Because that's basically, basically, the approach with the effect holder is a superset of this approach.
drewrelmas 00:31:56 Right.
Laurent Querel 00:31:58 So you, you… And… what I'm saying is, I think there is a way to write those effect on loyal With the same… type of… Benefit that you have here, in terms of performance and control on the result.
But still providing the additional services that the effect on Blur exposed, which are not only about sending data downstream.
Which is entirely lost in this approach.
Yes. And that's the problem for me.
Okay. But, we, we… and not only it's a problem, but the other problem is… Then we have to… Basically, for every processor that could be part of a chain.
It needs to be divided.
drewrelmas 00:32:47 just implement.
Laurent Querel 00:32:48 Yeah, so that becomes super. Yeah. Even with AI, it's not necessarily super beautiful, but.
drewrelmas 00:33:00 Okay, yeah, this is good feedback, thank you. Yeah, I don't want to monopolize the time in the meeting, but.
Laurent Querel 00:33:08 I think in general is, is, is, is, excellent, I think, in general.
drewrelmas 00:33:13 I would close on one more note. If you scroll down, Laurent, I'd like to talk about the performance implications that I see.
So… In terms of… durations. I don't notice any huge regression in terms of time spent. I've tested mainly with attribute processors, simply inserting an attribute. The one thing that was sort of surprising to me is The chained duration that shows on the composite node is higher significantly than the sum of the internal processors.
I'm still trying to figure out why. I think it has something to do with the deserialization cost, which isn't… Properly captured, like, in… The timings of standalone processor nodes.
I'm still thinking about that, but the one thing I do want to make sure I say is the memory consumption. I ran two pipelines side to side, one using… three attribute processors as normal, and one with three chained attribute processors, and I can definitely see the memory reduction from the lack of channels being increased.
Laurent Querel 00:34:37 Yeah, makes sense.
drewrelmas 00:34:38 Which is expected, but it's good to see that.
Laurent Querel 00:34:40 Yeah.
drewrelmas 00:34:41 It's confirmed.
Laurent Querel 00:34:43 That's cool. And, for that… I don't know, that's strange, I will… There is no real…
drewrelmas 00:34:51 I'm gonna keep looking at this, because I'm not too happy not knowing where this is coming from.
Laurent Querel 00:34:57 There is no real serialization, deserialization, staying involved when we are talking… when we are using channel versus not channel. I think maybe a way to… to, to get two things for one effort, I don't know the right expression in English, but, will be to, maybe, draft something that I think, yeah, that… That, Josh, mentioned.
Because if… You want to compare something accurately.
Maybe we could add… A way to, That would be just a draft to begin with. Having a new entry into the context that lets any processor Or, even the, the engine, set times in the context… and then get the last, tying for the last part of the shen, will give us, a representation of this entire, shen. So… It's not perfect, but it's… It's not perfect, because we have a concurrency, even if it's a single thread-based concurrency, we have no… It's pretty hard, in fact, to get the time Combining the time passed in every processor with the time passed in every channel.
It's not necessarily super easy to measure, but maybe that could be a first.
drewrelmas 00:36:46 I saw.
Laurent Querel 00:36:47 initially.
drewrelmas 00:36:47 a little bit. My main problem was I would need to make processors aware of their position in the chain, if that's the best… like, the processor that needs to start it needs some signal that it should be the one that starts.
The ones in the middle need to know to accumulate into it, and then the one at the end needs to know to pull it out, and also report it to internal telemetry with the chain's node ID. So, it… without, like.
It's distributing some of the work of orchestrating the chain into each processor.
Laurent Querel 00:37:32 Yeah, I think we can move away.
drewrelmas 00:37:33 an actual processor chain node which is responsible for doing this.
Laurent Querel 00:37:39 In my opinion, I think we… we… I think we could avoid that, and push the… this, Measurement, in the, at the engine level.
I need to think about that a little bit more, but, I agree, we… it will not be a… Great.
To have the collaboration of every processor's .
drewrelmas 00:38:06 Yeah, that was my main concern, is everyone.
Laurent Querel 00:38:08 That will be pretty bad, but Relatively confident that we can avoid that.
Yeah, I definitively need to spend more time on this, gitHub issue and corresponding PR.
drewrelmas 00:38:23 Sure, thank you.
jmacdonald 00:38:25 I, I thought we'd, sort of evaluated the idea of this stopwatch, at least, and Drew came to me, or we discussed it, and I think there was a contention that there are other metrics that we might like.
drewrelmas 00:38:39 Oh, yes.
jmacdonald 00:38:39 Thank you, Josh.
Not only the stopwatch, because I think if it is only the stopwatch, there's a fruitful discussion there. I could imagine automating it, like Laurent says in the engine, you know, you'd start at zero, and then you just… every context would have an accumulated CPU count, and it would just be always present and always maintained. I'm going to assume it's cheap, I think it is. And then… and then you could have a verbose, like, a detailed level metric, which says.
Give me the cumulative CPU time at the end of me.
And then any node can turn that on, and then as I was… the issue I felt earlier today, or yesterday, was we need a way to selectively choose metrics on a per-node level. So you take those two things together, now you're just like, I want the stopwatch at this specific point.
To tell me cumulative… that's one way to do it. I think it gets harder when you want a difference. Like, the difference in CPU time between these two points is what you can do with your processor chain that you couldn't do as easily with, like, just an accumulated single count at every node with an optional metric to output that.
So, I was left convinced that Stopwatch may be a fancy and useful thing, but not a full solution.
Laurent Querel 00:39:54 Okay, back to the… to the agenda, I think I need, 15 minutes for the demo.
jmacdonald 00:40:05 And I do not need to talk more about Metrox SDKs. I'll bring it next time.
Laurent Querel 00:40:09 Okay, so I need to provide some context on… this specific topic, so I think we have… an issue that was there, add life pipeline or configuration. Yes, I think that would be a good starting point.
So, the overall goal here is to… Enable library configuration of pipelines.
into the existing engine.
there are many ways to do that, and different levels of granularity. In this specific, work.
let's say, first phase, it's about Live reconfiguration of entire pipeline, not library configuration at the node level, which… Will be supported, but not part of this first phase.
Doing that at the… the pipeline level.
Is, slightly easier, in fact, because, It's all of oursing, there is no, No collaboration required by the node.
In fact, I didn't change any… anything in the existing node except It's not exactly true. I changed a little bit the topic receiver, topic exporters.
in order to be… More friendly with shutdown procedure.
I'm sure that I will have to do that with some other processors, but I didn't change fundamentally the work that they had to do.
today. It's more because they had some issue in their shutdown procedure that I had to intervene in their code.
But, as opposed to the… library configuration at the node level, where we need the collaboration of the node to really achieve this capability. So that's why I'm starting with the pipeline-level reconfiguration, because it's easier and does not require node collaboration.
So we already had… A set of, a million points.
in the… in the project. And that's how the… the UI… the web UI, where we see this, a graph of nodes, the DAG, The values, metric, that are displayed, and so on.
It's relying on the admin entrance.
they were mostly, read-only endpoints. We had, an endpoint, if I remember well, to shut down Twisten it.
fully working.
So the… the idea now is to extend this, the same unneeded, The same admin set of endpoints.
To support, shutdown at the group level, shutdown at the pipeline level.
And what I name a rollout, so basically providing a new version Of the pipeline configuration.
And, letting the… the engine to… So let's say that you have a pipeline that is deployed on 3 cores.
And you… you want to act on one element inside this pipeline, so you take the entire configuration, there is a get open to get the configuration of a specific pipeline.
You make this update, then you… you deploy the new version, and we… we like to get an engine able to Look at this newer configuration.
determine, what kind of operation needs to be done. Is it really, an entire reconfiguration of the DAG?
Or is it, a scale-up, scale-down event? So, this player is doing this analysis. If we observe that the number of CPU cores is the only modification, then we have a special, Procedure, which is, much lighter.
So we can determine, oh, we need to kill one of the pipelines, we need to shut down one of the pipelines, because, in fact, the number of CPU cores came from 3 to 2.
But if it was a 3 to 4, then we need to create a new thread, initialize, A pipeline runtime inside, and then we scale up.
As opposed to, a procedure which is a little bit more complex.
That consists through… oh, we have a new node that has been injected into these pipelines.
And what we need to do is, again, with the example of three core for the corresponding pipeline.
The system will start a new thread.
Create a new runtime, initialize with the new configuration, Generation 2.
look at the behavior of this pipeline. Oh, it's working well. Then we can shut down one of the three, Generation, one, pipeline configuration.
And then we go to the next, next step. Oh, now we have 3 core, but 2 with the previous configuration, one with the new.
So we need to reiterate the same process again and again, two times, until we get the entire Existing pipeline replaced by the new one.
So that's the purpose of this, System?
So what now I will show you is a demo of that.
with a new command line, which is another PR that will come later, but for now, So, I will start this, a configuration. It's, a multi… I think they're… We have 7 pipelines connected with, with, Pacific.
In this one, then I will open… Just to show you the… I will open the, So, full page, and there is an option here, I don't know if you're aware of that, that connected view, which gives you, basically.
A way to look at the entire, Connectivity between those pipeline connectivity that is done through the topic.
So we have three, ingress pipelines, one.
at the logical view, I mean, they could have multiple CPU cores for each of them. One, let's say, process-oriented, pipeline, and three… Egress pipeline.
Dude?
And now, I will show you the… this new… DFCTL, so Dataflow CTL, we can rename it, I want something short, that's why it's an MDFCTL.
And this command line, has been designed on top of the previous REST client SDK that has been, merge, last week, if I remember well. So it's a way for any REST programmer to interact with the engine remotely.
With, A resource-oriented interface.
But where the concept of HTTP protocol and the fact that we are using currently and exposing currently the those endpoints with a REST… a set of REST endpoints has been removed. I mean, it's relatively agnostic to the protocol. We could imagine that in a future version, we of this SDK, without changing the interface, we can interact with OpOMP as a protocol. That should be feasible.
So, this DFCTL is using this client SDK.
And, is able to deliver, but to be used either in a non-interactive way, like any command line, and you say the FCTL, groups shut down, with the name of the group.
Or it could be used, in an interactive way, which is the… what I want to show you.
So… This thing is… Connecting to the… to this, server, to this engine, which is exactly the same that we see here.
Except that the interface here is a terminal-oriented.
And we… we have, three… three tabs, engine, group, pipeline, so we retrieve the… the internal hierarchy, that we have into the configuration of this engine.
And, we can inspect, And interact with the… each of those pipelines.
So here we see how much CPU core are, used.
And if we had some rollout events.
So let's, start with something simple, let's see, we have… right now, we have something like, 1,100 messages per signal, so the… each message here represents a batch, so it's 1 million, or 1.7 sometimes. So let's say 1 million, signal per signal.
A way to increase this volume is… or to decrease the volume, will be to act on the number of CPU cores of a specific, traffic gen, pipeline. So… If I use the, the, the key A, Then we can scale up, scale down.
Set a specific number of calls.
edit, or redeploy, or shut down the pipeline. So let's start with scale down.
So we see here now it's 2 instead of 3.
And we should see… We should.
Yeah, we should see a decrease in the number of messages per single, because mechanically, we decreased the number of core that was producing something, some messages, so we see now an effect on this pipeline.
I can go back to the previous… Oh… Let's get up!
So we see also here the impact, but now we have 3, and we should go back to 1.1.
So now, if, I want to test how the shutdown works for, let's say, this specific, pipeline. So the traffic gen tendency is… this one.
So… Again… Key A, and then I can shut down the pipeline.
with a confirmation, And, yes, it's updated.
Bye, by, pipeline?
And we… we have here, so sometimes pipelines don't stop properly, because we have… we still have, probably a lot of bugs here and there in the… the shutdown procedure, and for receiver, also in the drain ingress procedure, so that the mechanic there is, I think better understood now, but still, Not necessarily properly applied everywhere.
So there are ways to diagnose that, and I try to create an interface to simplify the… The troubleshooting of the… of such things.
But for this one, it's working well.
And, so now, let's, say, oh, okay, I want to… Kill this one. Again, shut down.
Now, what about changing the configuration, and that's where we have this more complicated situation where it's not about creating a new thread.
stopping a thread, or a bunch of threads, it's orchestrating the rollout of those pipelines, instances. So that will be demonstrated by, for example, changing the… Also… Oh, yes.
And, so now, I want to update this one.
Edit… or deploy… And let's say that I want to just rename this node sync.
just for the purpose of the demo, I'm not doing it Complicated thing, but, that should work the same way even if we change the configuration itself.
So… now there is… the UI is not necessarily perfect. You have to click here, enter.
So now it's deployed.
and we see sync instead of tenant B sync. So it's… it's a validation that the… and this pipeline was running on a single core, but if it was running on multiple cores, this follow-up mechanism that I mentioned, We'll apply the same way.
And finally, we can decide, okay, let's keep this entire group, Yes, done, and that, look… Beautiful.
Hey, what up?
Any question?
You're on mute, Joshua.
jmacdonald 00:55:35 No questions. I was just chuckling at the sidebar chat here. Very nice, very nice.
Laurent Querel 00:55:44 Cool. So, do we have time? Yes, we have 5 minutes.
Hopefully, if there are questions, I will not repeat to the…
jmacdonald 00:55:51 CFCTL is a large new change that we're about to see land in the… Is this using, Ratatouille or something like that?
Laurent Querel 00:56:00 It is. Yeah. Yeah.
jmacdonald 00:56:02 How many megabytes of binary am I gonna… never mind, that'll be a separate binary.
Laurent Querel 00:56:06 It's a different binary, so, no worries, sure.
Okay.
jmacdonald 00:56:19 This is, really great. As Drew comments, it follows the Kubernetes model, which I think is actually a really good way to go for software projects these days. I think, the more we have conceptual similarity across our tools, the better. So, I'm enjoying this concept.
Laurent Querel 00:56:35 And the… So, so maybe I can explain a little bit more why we… Because we could imagine doing that, Not exactly at the same… I… Because we have a lot of guarantees there. We could avoid any data loss and this kind of thing, and many other things, but, the main reason why it's not just reusing Kubernetes construct… I mean, reusing the same type of construct, but not leveraging the Kubernetes construct, it's because I really want to see this level configuration fully orchestrated by an engine that understands perfectly the nature of those pipelines, and more importantly, I want to do it super fast.
we should be able to update very quickly pipelines for whatever reason. We have a need on our side, but I'm pretty sure that you will have this need at some point also on your side, if it's not already the case.
jmacdonald 00:57:42 My dream sampling system, for example.
Niche update.
So this is very good. Would you say that we're, the next thing to do is to start reviewing one of your code, you know, your changes as soon as it comes out of draft?
Laurent Querel 00:58:01 Soon. Probably by the end of the week, so tomorrow, I still have some, bugs to… To fix, to be satisfied, and then, we will have a review for the… for the engine itself, to support this new set of APIs, and another PR for the DFCTL, which is fully separated.
jmacdonald 00:58:31 Two big PRs.
Laurent Querel 00:58:32 Yeah, 2BLs.
So in the woods.
jmacdonald 00:58:36 No worries, I'm glad to do my part and review.
Any questions out there?
Comments?
Really cool demo. I mean, the polish on your DFCTL surprised me at first, but I guess I shouldn't be surprised. Very nice.
Laurent Querel 00:59:00 Yeah, those days we can do things very interestingly and very fast.
jmacdonald 00:59:05 Yep, yep.
Laurent Querel 00:59:06 I mean, it's, it's, it's, Start to be very used to this tool and how to use them efficiently.
That's an interesting topic, as is, but maybe we can address that in some other future SIG meeting, but the importance of tests is super, super fundamental. It was already the case before, it's even more now, with all this, AI, assistant.
And we need to multiply the number of approaches we have regarding the test.
And we have in this group people looking at various things. I was looking at VST at some point, because it's… I think it's a very interesting approach. I know that, for example, Jake is looking also at VST and, Quint and many other things.
So we, we really need, to have more confidence, even if we are… we have much bigger PR, in the future.
Because that is a trend, for the… because of the use of AI Assistant.
And, I will be very disappointed, personally.
If we are not able to find a way to… Be able to keep the same level of confidence and quality.
But at the same time, being able to absorb much more code, because that's what will happen. And, so we need to absorb more, and keeping the same quality and confidence.
And that will not be easy.
Okay, 9 AM, thank you so much, at least on the West Coast, and see you soon.
Bye.
drewrelmas 01:01:01 Thanks, bye-bye, everyone.
Albert Lockett 01:01:04 ruin…
