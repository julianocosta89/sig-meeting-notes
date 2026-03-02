SIG: Arrow SIG
Date: 2025-07-29
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Drew Relmas 00:00:50 Hey, Albert, how you doing.
albertlockett 00:00:53 Hey? Drew, doing well, how are you?
Drew Relmas 00:00:56 All right.
albertlockett 00:00:58 I think I.
Drew Relmas 00:00:59 Can, only I think I have to leave a little bit early today, but sorry.
albertlockett 00:01:05 Yeah.
Laurent Quérel 00:01:06 I guess.
Drew Relmas 00:01:08 Hey! Rob!
Laurent Quérel 00:01:10 And who
so I guess I know that Joshua should join us. We talk about this meeting earlier this morning
to to give some time to Joshua to join us, maybe.
I I like to in between to share my screen on
some specific scenarios I was investigating
with the with the Ff team.
Something, some goal that we could define, at least for 5 people in terms of
pipeline that we could support in one month.
So
I think it's interesting to share that with the the rest of the people working on this project and see if we can help each other on these on those goals
share. So I guess you can see my screen.
albertlockett 00:03:23 Yeah, we can see it.
Laurent Quérel 00:03:24 Okay? Great, yeah. So we what we discussed with the the 5 team
today, I was trying to identify some very basic scenario
where we could demonstrate some benefits.
basic ones like being able to
to support multiple type of protocols. So Tlp or Tap Syslog
and and demonstrate that we are able to use the same underlying pipeline system
to address those different protocol oriented scenarios. So that's basically the
the the 1st set of scenarios that you have here, and demonstrating that with a single native tap pipeline.
we we can technically support hopefully very well from the Tlp to see slug to tap
and because now we have this benchmark infrastructure, we can do that. For each of those
scenarios. They are also they, they could be implemented also with the go collector. So we can. We can have comparison between the the 2 implementation and see how well or badly we we perform and try to to do much better. So that's so first, st very basic. Right. Now, we have a Tlp to a Tlp
we have a set of 1st results very limited, because right now the
the engine that has been benchmarked is only a single threaded, threaded
What happened. There is a new one that's
There is a pr.
a draft Pr on which we are trying to to implement a multi-core equivalent of this benchmark
free. That will be done for the for the end of the week. So, Joshua, we were I I was using the waiting for you. But in between, I decided just to to show some
demo scenarios that we discussed with my team earlier today. I think I just need 5 to 10 min, Max, to talk about that
and then we can. We I will let you continue and and drive the the meeting.
Sure. So
1st scenario focus on demonstrating protocol, translation, protocol support, and and the fact that we we support with that natively.
So gund set of scenarios there are there to demonstrate
this approach that we are following where we try to lazily deserialize serialize only based on needs. So, for example.
the 1st scenario, when we have an Otlp receiver connected to an Otlp exporter is a scenario where, in fact.
we don't really need to decarularize the the Otp message.
We just need to interpret the the Grpc call and everything that is inside this call
does not require any desalization So
we, we'd like to to end up with
a pipeline solution and an engine that authorize this kind of optimization transparently.
We are very close to that right now.
And a a single type of a single
pipeline definition that will also
We'll also rely on this no salisation solidization. For Tlp is the the following one, where we have no Tlp receiver, we have a specific processor routing the
the Otp messages based on the type. Is it a metric batch? Or if it's a log batch or it's a span batch, and then we would the corresponding batch to
a dedicated exporter.
So that will not necessarily require also the serialization serialization. In that case, another. Interesting
basic pipeline that we could demonstrate is something where we we we use the the C slug receiver on which is working on
that will deliver on a tapped batch message
and then we, we demonstrate. In that case, it's more to demonstrate the the data processing speed and the advantage of
leveraging a different memory representation. Internal memory representation.
So a nice way to demonstrate that, for example, is to rename an attribute, or to delete, or to to insert
an attribute that will that should be super fast with arpeggio as opposed to
an otlp representation that will require to basically mute the entire tree of object.
a a slight variation on that is about a pipeline definition, where, instead of sending an ot to to an otap back end, we we just store
the information in a packet or presentation.
So we basically, we, we do the the same thing system receiver. We do some manipulation of the attributes.
We do some matching. And then we we just store in a 3 bucket. That could be also very interesting.
demonstration. Maybe this one is the the only one that will not necessarily be super easy to achieve with the go collector
but the the all the other, the the all the other 1st 4
set of scenarios. I think the North Street
will be achievable with the the go collector.
and and the last one is a little bit more specialized or specific.
So last week we discussed about leveraging the semantic convention registry as
a way to generate
synthetic synthetic otip traffic synthetic otip traffic that is
not just purely random, but something where it will be good enough to to demonstrate that we have a good compression rate, for example, on a realistic Otlp stream.
And and what we can do is we we could generate
a pipeline configuration that is basically mimicking a load generator, an otap load generator, other generating
otap traffic or otlp traffic. It's just basically a receiver. This signal generator that is connected directly to either the Otap exporter or the Ottp exporter. And then we get
an audition. Obviously we we could imagine some things like right limiting, defining the
the the rights at which we we send the the Otlp traffic. So that's some kind of refine refinement on on this scenario, but that's more or less the
the thing, and and finally
for each of those scenarios. It will be very nice if we can demonstrate 1st
level of libel configuration.
So in my mind, there are multiple level of library configuration that we could support.
The simplest one is you have a pipeline definition.
you have notes that they are interconnected together, they form a dag.
and being able to reconfigure individual nodes into this dag, is for me the 1st level of liver configuration that we could support.
I think that is something that is not too complicated to achieve. And again, that's a goal that we discuss
with my team late earlier this this day.
The second level of a configuration that is much more complicated, but I think is also one of the
let's say capability that we we like to to achieve at some point, for this new engine is
reconfiguration of the pipeline itself. So if you want to introduce a new exporter, so you you're basically adding some new element into the dag you are removing, or you are
rerouting the traffic from one element to another one. So this kind of rewiring of the dag is something that could be supported also to some extent.
So yes, that's the what we have in mind, and we'd like to
to be able to demonstrate for each of those scenario. We we like to to leverage the benchmark infrastructure that is being implemented, and show some visual representation of that
how much messages we are receiving to the pipeline. How much messages are exported by the values exporters. This kind of stuff
don't hesitate if you have any additional. If you have question or suggestion regarding those scenarios.
We are super interested by that, because what
at least clarify what we try to achieve is for beginning of September
trying to to get with this value. Scenario a a 1st version of them, in order to demonstrate the the value of the project, and
and see where we need to do some improvement in terms of performance. And this kind of stuff.
jmacdonald 00:13:44 Great. Thank you. Yeah, I as you and I spoke about today earlier as well. I'm gonna do some follow up work on Microsoft side to kind of help coordinate all the people I see in the room who have that affiliation. So I will follow up both here and with you about some of the
alignment issues that you discussed.
I from your diagram have questions and and QA ideas about the
queuing, and the sorry, the batch processor that you drew as well as the attribute renaming that you drew
and I would be interested. If you I mean, I think that that now we've reached you've shown some great scenarios.
I think, and I have spoken earlier today as well about some questions involving exactly the same like. So this idea of a batch processor for me, the way I would frame this question, and I'll hand it to him is that you know batching an arrow record batch is going to be different than batching. Say, an Otlp batch. We know that we're kind of trying to steer away from batching an Otlp batch
and but we also know that there's efficiency gains and sort of like batching in general. So if we are looking at the Syslog case and we have a stream of
payloads which are individual byte arrays getting into an otap batch without getting into an otap batch. I say, without batching means having single message, otap frames, which sounds like an anti-pattern. It. It makes me wonder whether we have some sort of primitive batcher or Async step. Somehow I want to talk about the architecture that we use to get data
from more than one payload, potentially having conflicting schemas. But really the builder pattern for ocap frames. Ukarj, would you like to to speak.
Utkarsh 00:15:46 Sure, yeah. So like as I was working on the Syslog receiver implementation, I think the most important difference that I noticed between Syslog receiver and the Otlp receiver is that
Otlp receiver receives already batch data. So when you implement views for that that you are carrying like a reasonable number of log records within that
implementation. But for Syslog, like, let's say, if you have a Udp receiver, you get one Syslog message per Udp packet, so
if I just do a views implementation for a Syslog parser like, I essentially just have one resource with, like the default or empty values and one scope.
And then there is one log record for the Udp packet that I received.
So yeah, like, I mean, I could potentially create like multiple single log record otap batches.
and then they could be merged somewhere to like form a bigger batch, which is better for export or processing. Or maybe I can do something.
do some kind of batching before I convert them into views or otam like. So that was what I was trying to understand, and I think I also saw that in your diagram earlier, Laurent, that you had put a batch processor after attribute processor in that Syslog pipeline, so.
Laurent Quérel 00:17:10 Yeah.
so what I had in mind regarding the syslog, because for for the exact problem that you mentioned.
if we receive a Dp message.
I think it will make sense to have some kind of embedded batching into the Syslog receiver.
Because the the the override
of just creating arpetual records with the corresponding schema.
for every single entry will be way too big.
so yeah, I I think if we? I mean it. It means it makes a lot of sense to
to make this sy slog receiver able to do this and daily baching.
So you you get a list of binary representation of sy slogan trees. Then you
you you do the the view mechanism on top of them
and you get a batch, so the now the that will probably require some
configuration element into the Syslog receiver.
Giving the option for the the operator of the sy slug to define the latency that they are
ready to accept. So let's say that we don't want to to wait more than 100 ms.
So the batch is defined by
a maximum set of Udp messages
and a maximum duration.
So the based on those 2 parameters exactly like we have in the batch. The regular batch system. We have multiple conditions to to determine when the batch will be ready to go.
I think we should have something similar.
except that it's lower lower level. Because we, we, we, we basically
only do the review stuff once we have the entire set of
smaller messages, and then they are converted in in one shot into the the auto batch. That's how I was
thinking about this slug receiver.
Utkarsh 00:19:29 Okay. So yeah, I mean, maybe I I could look at some kind of
Spscq or like some other.
I don't know if like this would lead to allocations like for me to like hold certain number of records
Laurent Quérel 00:19:49 But you could accumulate those individual C slogan trees into just vivek.
and and you can also
As for it's it's not yet available in the into the engine. But you can. You can basically use Tokyo for that right now, and we will do some
modification later on. But you, you can basically create a timer
that will represent the the Max duration.
Utkarsh 00:20:23 And every message that you receive, you accumulate that into this.
Laurent Quérel 00:20:28 Internal vec and and then depending on the condition that is triggered the 1st
you, you! You trigger the
the view mechanism, and the generation of the Otap batch on top of those on top of this deck
the pixels.
Utkarsh 00:20:51 Yeah, yeah.
jmacdonald 00:20:55 Well, I have questions. So
Over in the Go side there's an existing pattern that we we have called exporter helper.
And there's been a long and very drawn out migration from a processor export Batcher to a exporter, Batcher
and here we are talking about Receiver Batcher and I understand why. And and it's actually not to make a point about where these things belong, but about there being a sort of piece of common logic that we can reuse, because actually, this stuff is really hard to get right. There's a corner case for everything like extra large sizes and timeouts and clocks that don't work and shutdowns happening. And there's a bunch of concerns there. And
I actually, today, I've been involved in trying to replace the old Batch processor. It's an old legacy, and I've I got my hands in it a long time ago. And, the idea is that you should be able to take this fancy new Batch processor, and, like check, put its logic right into the old one to get rid of the old logic, because we should have a 1 robust, common piece of batching logic when I heard you describe it, though, Laurent, it also made me think.
Well, it's different to batch when the output is bytes when the versus the output is a P data object. And what you've also added is an element of laziness that is interesting. So
what I'm seeing is a kind of a pattern. You know, both protocol message
and this data type that you described at the low level support, appending an item in the frame that's growing where the top level item can just be appended in a very easy way. So for protobuf, you can just append some bytes, concatenate them, and you still have a valid object with more repeated things in it.
And I. What I think you're saying is, you can take a syslog payload which is bytes and concatenate it, or by appending to a batch which, for the vec representation, just simply means putting into a slice, for the Protobuff record means concatenating those bytes, etc, for a ocap representation. It might need a special definition, but it's just appending a bunch of rows with more rows.
So that we have a batching mechanism that works with lazy, instantiated
D data objects. So then, Utkars can produce a
receiver that uses the helper for the receiver helper to get the low level batching. It uses
uses a function that operates over bytes and produces a view for Otlp like objects. Then there's a batcher that concatenates vac a vac of
vac of byte, a a vac of U 8 strings or bytes.
and then you output an otap frame which is constructed by a view over the concatenation of a bunch of lazily instantiated Syslog events.
Does that sound about like what you're imagining.
Laurent Quérel 00:24:00 I think, what you, if I understand well, you are all
advocating to generalize a little bit more than the
the P. Data wrapping that we are already designing. So we we are right right now, what's
Albert is doing is a P data wrapper that could have multiple steps, multiple states. Sorry
one is okay, what we have right now. And it's not deserialized. We have internally into this P data. We have all clp bytes.
And we want to enable scenarios where, depending on the the
the method that will be used on this data wrapper. Sometimes we don't need to do the Deserialization.
and so that the scenario where where we have a Tlp receiver connected to an Otlp exporter is a such scenario.
we need to be able to
put this for this Otlp bytes inside this wrapper, the P. Data wrapper, and then it's transported to the it's communicated to the to the Otlp exporter, and this Otlp exporter will just ask the Pda. Can you give me an Otlp Byte representation of this P. Data? Oh, yes, it's already there, so I give you that directly. There is no serialization, no disserialization, no copy perfect.
Now, we could imagine something similar, for
it's slightly more complex. But we could imagine something similar for C slogan trees.
But the the main difference is if we want to make something more generic at the P data level.
I think that when we, when we construct this speed at a wrapper.
sometimes we could provide. Oh, by the way, here is how to deserialize here is how to combine.
Use that to do this job. And we will provide this kind of function by default. For Tlp, for example, and also for tap. We we could imagine to extend the the P data stuff for
something more open. And then a good example of it is the Syslog stuff.
Why not.
jmacdonald 00:26:20 You're this pattern exists in the go collector like very, very much what you described for the exporter helper. What's curious about it is that we haven't found a good reason for it yet, meaning that the only implementation of that mechanism, the the implementation details, which is the splitting function. The merging function, etc, is the one that produces P data objects.
And so there's no open implementation that anyone can see where you're actually taking advantage of this functionality. But I take it away from what you said that roughly, we're seeing the same kind of kind of architecture. What I what I'm almost imagining is that
as I wrote in the notes, like, if you take one P data and append it to another, the result is pretty well defined even at the view level, meaning that I can form a P data view, which is 2 p datas.
and I can iterate through them at the top level, but meaning to go through one resource thing and then the next.
There's no semantic difference by concatenating things at the top level, as I'm saying and so
I I suspect that there is a low, level helper for the, for the batching that can do
be generalized by T, and can be a vector and then T can be a P data that has its own lazy rule. So that
for the receiver path in your in your scenario. We're gonna have Syslog
registers its decoding function for the Otap view. So the for the Otlp view.
some helper will concatenate those views into a batch of views. Now you'll get. It'll be a view that passes through all the batched views, and then we will instantiate a no tap frame after that.
for example.
Laurent Quérel 00:28:14 Yeah, I I think the in theory, what we we describe
resolving this kind of merging blah blah blah at the P data level think it's feasible. It's definitely complex. If we start to
to make this kind of mechanism generic.
not not only at Tlp, not only at Otab, but in theory more general.
I think what we can do maybe, is a 2 step thing where we we
we do that 48 p. And a tab.
We try to generify it. But for C slug, maybe
we, we start with something simpler. And then we we start. We look at the single step. Where? Okay, what can we do in the tap
into the P data wrapper to make it able to to address the scenario like like Syslog.
jmacdonald 00:29:12 Got it.
Well, I.
Laurent Quérel 00:29:14 What do you think? I think it's otherwise? We we the is it's already complex.
jmacdonald 00:29:22 Yeah. Thanks.
Laurent Quérel 00:29:23 Yeah, I think it.
I don't.
I agree. I think it's it's meaningful. It's it's it's useful to go in this direction.
Maybe we can go there in in multiple steps to avoid, to overcomplexify the next step.
jmacdonald 00:29:37 Thank you. I appreciate being called out for complexity. There is a certain elegance in the approach that I just described, but it was fairly complicated. I did actually have the same conversation earlier with Ukar. So so it's good thing you're both saying the same thing. However, we did talk about. The other alternative, which I feel like is requires just to like
laid out like requires learning a lot more arrow, which right now is a struggle for a few of us. And so I imagined, okay, now that we've spoken out, talked about that complicated code path just now, let's talk about a simple code path where you go straight from Syslog to to the Otap representation.
and it means having a so essentially a builder that works directly at the otap conceptual level. For and and I think for logs. It's pretty simple. Obviously, we know, for spans and metrics. It gets harder, but like for logs, it's like one record is going to arrive at a time.
As you see that record, you're going to create a log record table entry which is going to be one row. And then, as you go through it, you're going to see its attributes. You're going to create. N. Rows in the attributes, table log attributes, table, and then a few more details. I can't remember all the details, but, like.
you know, like one by one, you will add a new record. It will become one more row in all the column builders, one or N. More rows in the column builders that we have, and then at the end you you built, finish the build, and there you have an otap frame. It might be very simple and concise.
Laurent Quérel 00:31:10 Yeah. But I think what the what you are describing the builder stuff. And it's exactly what we have with the view. Now.
the the view is to some extent an abstraction. So it's it's more more than that. It's the view, plus the the algorithm used to create an attack batch.
jmacdonald 00:31:29 So this combination is the builder that you are describing.
Laurent Quérel 00:31:33 Maybe the maybe the what is missing in the in the view. Mechanism, maybe, is incremental views.
So you you provide a binary buffer that feed the view system
right right now you have to provide the entire set of buffers or a single buffer, and then you get the corresponding.
You have the view that are mapped on this big buffer, and then you get if you connect that with the the tap.
let's say, Builder, that will consume the view. You will get another batch.
Maybe there is a way to do that in a more incremental way
and then you don't have to to accumulate the the big batch of C slug messages
internally. And and you can do that. I don't know. I think.
yeah, right now, personally, I will.
jmacdonald 00:32:36 I wanna hear Albert's ideas, or anybody else really.
albertlockett 00:32:39 I was just gonna say, like, where where my head goes with. That is like currently the way that the the view to Otap batch is written is that we take one instance of the view, and then we instantiate the builder, and then we append all the records, and then we call finish, and then that spits out the otap batch like we could maybe figure out a way to rewrite that where we have
an instance of the builder that you just append batches to as they come in. So then.
you know, you could say, Okay, well, I'll I'll have my Syslog come in. It will just be a Syslog log view that has one syslog in it, and I append that to my builder. And then, once we've accumulated enough enough rows. Then we spit out the
Laurent Quérel 00:33:28 Yeah.
albertlockett 00:33:29 Finish on the builder. Essentially.
Laurent Quérel 00:33:30 That's what I meant by the the incremental version of the view mechanism. It's exactly that.
albertlockett 00:33:35 Yeah, okay.
Laurent Quérel 00:33:37 Yeah, and it looks
feasible. I'm not saying it's easy, but it looks familiar. Now, do we need to go there first? st I don't know
but yeah, it doesn't look like something that is impossible. So that means that the the Cisco receiver in that case.
instead of accumulating, if we are able to achieve that, to have this incremental views, then, instead of accumulating
a binary buffer where we we concatenate the various Syslog messages. In fact, we just maintain the the back end of those views. And we inject the the small buffer representing each line of the the Syslog stream
that will feed the
that that will feed the the set of Apache or records. And at some point like you said, we, we say, Okay, we have enough.
We materialize the the set of our records. And and and then we we just create a
a P data wrapper for that.
jmacdonald 00:34:46 Yes, I call this A P data constructor. Whereas, say the Go pdata Otlp model has essentially the protobuf model like you can append to a slice, you can create an empty object, and that's about it, like you can also copy in or move an object by by moving it into the structure, but that's just ownership. And
it's what I'm hearing is that for the Otap frame, the equivalent is much more restricted. But, like you can append a log to a log record batch. There is an Api for that
and so then you're saying.
and it's not very different than saying,
And this is the connection to the like append. Only thing I was saying at the beginning is that, like for a otap
renderer to go imperatively through a list of records and construct otap is not very different than having a stateful object that iteratively accepts one more thing at a time, and all of this is actually just equivalence
methods to do all the same thing. We've described 3 ways. Now, I think I like it.
Laurent Quérel 00:35:58 Yup! You too.
jmacdonald 00:36:01 Okar, should you? I mean, like I, we spoke a lot about something you're working on. I'd love to hear you speak or respond to all that.
Utkarsh 00:36:09 Yeah,
I mean, I think, the start off would probably be that I buffer things in at the receiver level. And then.
when I have enough, or like, when when enough time has elapsed, I convert them into note app. That would probably be the easiest thing to
try.
But I do like this idea of like incrementally building the arrow batch, because then I think it makes things very simple as as and when the receiver gets the
gets a packet, can just call those methods to append that row.
But yeah, and yeah, that, I guess, would require a lot of
more work to explore that that option.
Laurent Quérel 00:36:54 Yeah, I like this incremental approach where we start with something that looks much easier and more line with what we already have. And then we we iterate on that and try to to do even better. Yeah, for me. That
perfect.
jmacdonald 00:37:10 So it does sound then, like we create a Singleton
Syslog events from a byte array we construct a view around it which is a fixed resource, a fixed scope.
And then one record, and then we
append it to the in flight. Constructed otap batch. At the end of that we just flush it out, finished.
Laurent Quérel 00:37:37 What I understood is more, there is some kind of accumulation in this slug receiver
where? I think we catch described accumulating the the individual messages into a binary buffer, and then we we trigger. When we based on some condition, we trigger the the view mechanism and the auto batch construction
on top of this accumulated binary buffers.
Am I wrong, Gersh? I think that's.
Utkarsh 00:38:07 No, yeah. I think that we start off with that, we start off with accumulating things at the receiver level, because that's easier to try.
and then maybe later, we can. That's.
Laurent Quérel 00:38:20 Yeah, I think that's you know.
jmacdonald 00:38:23 I still see 2 sides of the one coin. Anyway, that sounds good.
for the group. I would love to hear Gokhan. You have a question I'd love for you to speak next.
gouslu 00:38:41 Hello.
So the question, by the way, yeah, my name is Gil Khan.
I'm from Microsoft and just today became a member. Thanks Albert and Drew for the support. And yeah.
looking forward to doing more things as you move forward. There was this task that I took a while ago, and I went on a medical leave, and I'm back now. I'm looking back into it again, and that task is about a long running deal job, and that seems to be because of Russ benchmark.
And
it seems like, you know, it just runs it every Pr. And I tried to make it optional. I mean logically, we can make it optional, but it is a required task for the Pr to pass. So
I was wondering if he thinks about it. Does it have to be a required task
because we can still run it optionally? It doesn't have to be a required test, but it could run optionally based on. If there's any changes in the last folder, because if what we are looking for is to see the performance bench benchmark of.
you know, rust code. Then you should only run after changes in the rust folder and
The other thing is, you know, what do we base? Do we set a bar for benchmark? Do we even look at that? Is there is the bar, a manual look, a manual check by the approval. What- what would be the idea?
The about, you know, running that benchmark if there's no bar that we set that it should be passing. So that's the other question.
So just in general, how to handle. And if you think that it is okay to just make it an optional task.
For Pr that is executed also optionally
based on. If there's a change in the rust folder.
And again, the the letter question is.
what is the actual benchmark, we testing it against.
Laurent Quérel 00:40:53 Yeah, I can provide some feedback. But if the others, you you have,
additionally element to to add to that, not hesitate. So that so for me, first, st I think the there is. There are 2 kinds of benchmark.
the micro benchmark that's the one that you are observing.
And and right now there, there are benchmark benchmark. We didn't look at them.
in in terms of quality. I think you you will find value things. Some of them are way too long.
And and we not bring enough value to justify the fact that we we run them for every Pr.
So they definitely should be, in my opinion, optional
and then we have a single category of benchmark that are more the the benchmark that that we will.
That we that we felt that we rely on the benchmark infrastructure, that Chris and and Cidil
designed and implemented.
Right now there are
not fully integrated into the the Ci pipeline.
And those benchmark are the one that it's basically running the entire. Comparing the go collector versus the engine with the same scenario we generate Otmp traffic, and we we check if how the these 2 systems behave in terms of CPU usage in terms of memory usage and blah blah, this kind of stuff.
I think that is where we should put the some set of requirements and that's also where we should historicize the result in order to be able to to see
either every day or ideally, every Pr
merging to the main how the those benchmark evolve over the time
and and making sure that we have a good understanding. Okay, it's normal that we increase slightly. The
the the the CPU usage. Because we introduce this kind of guarantee or this kind of additional features. It's normal, or the let's say the the pipeline definition was slightly different. And we are okay with that. So we we can even maybe add some event into the historicalization of those metrics. And we see on the chart directly. Okay, we, we have this event. And that's why we we see this increase into the the chart.
So this second category of benchmark that is not yet fully integrated into the the Ci. I think that's where we should
very
we have to do a very good job and and we have to make sure that we have this comparison.
Always available the micro benchmark. I think the
yeah. I'm okay for me personally, if they are right now, optional.
I think we need to do some
cleaning there, making sure that we just keep the one that really makes sense, because usually this kind of micro benchmark they don't necessarily edge very well.
At some point you create some of them just for the purpose of placing Xyz library sometimes that makes sense to keep them in order to re replay the the micro benchmark with a new library that came, or new version of this library.
but sometimes it's just something transitory that you forget to remove from your from your Pr. And
and then we don't have to spend the the CPU cycle for something like that.
gouslu 00:44:36 Yeah, okay. So I don't know if I have access to make the cargo bench step optional. But if we can make it optional, then I can.
I kind of had the pull request ready to still run it optionally, I mean, if it is optional for the Pr.
And if I make it, the run for optional for the
for the cargo bench step, then I think that the whoever is reviewing the pull request
can selectively pay attention to it, and then that would be the
check needed for this. If someone can make it optional, then yeah. Will have the benchmark about benchmarking the collector. I at Microsoft. I've been working on
my infrastructure and testing myself for the the
most part, for the most part of this project that we've been working on the auto collector. I completely agree with it when it comes to putting making them a part of Cicd. We are also trying to make it
part of our Cic. They which used to be the case due to some regressions in our internal system. So anyways, long story. But we're trying to put it back.
trying to see if we can use stuff from this new project to actually directly, you know, take advantage of so like a double purpose.
Laurent Quérel 00:45:59 So so on on the F 5 side. The person that is working on this
benchmark infrastructure is the Chris ale
on the Microsoft side. My understanding is C. Joe is also sometimes working that.
gouslu 00:46:21 Yeah, I work with. I work with both of them. So yeah, I.
Laurent Quérel 00:46:25 Okay, perfect and.
jmacdonald 00:46:26 Yeah, yeah, I was, gonna say, I'm I'm syncing up with C. Joe soon. And I I need to to be able to answer this question myself. Because I know we've done something. I would like to see us have a label in the Github sense, be used to run the benchmarks.
so that once in a while someone does something. It looks a little suspicious to me. I'll add the label and say, run the benchmark so I can see it. It's useful to know what the what the old values were which you kind of don't get with that. But
I agree that it's sort of transient stuff like like I added some for Otlp, decoding with prost like no one cares about that maybe a month from now, and we can eliminate them, so running them on on a label would be good, but also.
Laurent Quérel 00:47:10 And regarding the the question that
sorry, for I'm not pronouncing. I did not remember your 1st name, let's say, go through. Sorry sorry.
gouslu 00:47:22 Oh, go! Time!
Laurent Quérel 00:47:23 Gokrant.
gouslu 00:47:25 The ghost is my alias.
Laurent Quérel 00:47:27 Okay. Joshua. Maybe Drew can also help him on the
on making the the cargo benchmarks.
I'm optional.
jmacdonald 00:47:39 Drew has been doing a lot of work on the the build. Go, Con, we can. We can sync up with him as well. I already had already written that down, so I'll take care of following up with both of you, all of us.
Laurent Quérel 00:47:50 Right.
jmacdonald 00:47:52 As far as the agenda folks. I know I'd love to know if Albert has anything to speak about, or Jake has anything to speak about. One thing I want to say is just congratulations on the name Bar K with a B
bar barquette. You can say barquette or Barquet. I'm okay with either. They're they're very good. Jake. Everything.
Jake Dern 00:48:13 Good.
jmacdonald 00:48:14 I don't know. It just sounds like a barbecue mixed up with like I don't know.
I don't know. Just sounds like
it's quite nice, you know. You can crack a beer and enjoy some barquet. And yeah.
I mess up. Rk.
Jake Dern 00:48:27 Yeah, no, no huge update for me. I mean, I'm I'm mostly working on kind of on the side trying to get that delta dictionary support, and I really only wanted to try to merge support for the reader. But it turns out there was no writer support either, and there's not really a good way to test it, and rust without also adding writer support.
So along the way I found a few interesting things actually about. The behavior of like the Ipc writers, and both go and rust and kind of how frequently and under what circumstances, they can actually omit a delta dictionary. It's actually much more limited than I thought. And we don't have to go into it here. I don't want to take up too much time.
but I've been chatting with Albert about it on the side, so he's kind of up to date on that and I just ping some people on the the Pr. That I'm working on to just try to get their thoughts on it as well. So I'll link that in the chat here. But that's it for me.
jmacdonald 00:49:18 Thanks. Jake.
Albert, you've been doing some amazing things with Delta dictionaries. I understand.
albertlockett 00:49:27 No,
yeah, not too much. I did add support to parquet. So now, when you write from Arrow if you have a column, that is, let's say it's a dick
with a value of string, and then you try to write another batch where it's maybe a dict with a different type of key. Or maybe it's like a native string array. Then Parquet will accept that. And so that's going to be useful for us on the parquet exporter, because we have this adaptive schema thing where we sometimes change the type of the field.
And and and now parquet will accept that once we upgrade arrow, so that will be a nice addition.
The
The other thing I wanted to show and this this will just be like a 2 min update was just I added a new type for
P data, otap P data. And unfortunately, I can't share my screen. I was going to show it, but I guess in lieu of that, maybe I can just share the Pr here if I can find it quickly.
and so there's a new P data
module in in the Otap crate, and that module has a type called otap pdata, and that is the type that our otap components can pass between them. And so that type is actually an enum, and that abstracts away the internal representation of the of the P data. Object?
Yeah. So if you click on
there's there should be a file in here called pdata dot Rs somewhere.
Laurent Quérel 00:51:18 Yes, the top 1st 1. 0, no. Yeah. This one.
albertlockett 00:51:23 That one, and then if.
Expand this out, and you scroll down to around. Line 125
down a little bit more down a little bit more.
This. So this is the type that our otap components can pass between one another, and you can see that internally what it has is. It has the actual telemetry data, but it can be in different formats, so it could be just the Otlp byte protobus serialized. It could be that second one Otap arrow bytes. That's another enum that contains the Batch Arrow Record, which has
the Ipc serialized arrow record batches, and then the 3rd one at the bottom Otap arrow records. That's a type that we used to call otap batch, and that has the actual arrow bytes in it. And so, and then the rest of this type just has implementations of, like the from, and try from crate for converting between all of these. And so
this, this should hopefully be relatively, you know, straightforward to use like if your component has.
And you know otlp bytes, you can just wrap it in that otlp protobytes enum, and then use into to convert it to this Otap P data.
Type. And yeah. So this was, this was the addition this week.
jmacdonald 00:53:03 Well, we are moving along. What's nice is
almost everyone's spoken today. Chanley, do you would you like to tell us an update of anything, or ask questions, or.
Chanly Ly 00:53:18 Yeah, I can share an update on the
so right now on the fixed email receiver, I've updated the configuration to accept the
resolved registry as defined in the weaver Simcov crate, I think. Yeah.
So that will be used as a catalog to describe. Like all the different signals you want to basically generate
coming from that receiver.
So right, now.
jmacdonald 00:53:47 Configuration that gives you like numbers.
Chanly Ly 00:53:51 Yeah, right now, I'm just using that as like
to fill in some of the fields. And then I'm planning on using like the annotations field to like. Describe
what kind of values you want, like specifically like to add some entropy
to the type of values like for metrics like, I don't know what kind of range
and what distribution for that range of values as well.
jmacdonald 00:54:16 Great sounds good.
For attributes. I take it like maybe I know I have 3 of them, and they're, you know. One of them has 10 values, and one of them has 20 values. That kind of thing.
Chanly Ly 00:54:28 Yeah, cool. And then,
so I saw on the weaver. Emit I referenced one of the functions they had for generating all like the attributes.
pulling all the attributes, and then just like generating the key value pairs for each of them.
So
right now it's just grabbing, I think the 1st one from the examples. And it's not really taking account the
conditionally. There's like a field condition.
jmacdonald 00:54:54 Additionally required.
Laurent Quérel 00:54:55 It shouldn't really require us.
Chanly Ly 00:54:55 Required. So that's 1 thing taken account in the later Pr.
Laurent Quérel 00:55:01 Yeah.
But so so basically, right now, you you
you use the the semantic convention description for each signals as a way to determine a list of
required attributes potentially like you said, you know, if it appear, you will add that optional conditionary or required attributes, that you will generate randomly
and also the the attribute definition comes sometimes with the possible set of values. For example, the Http method will define. Okay, it's a get. It's supposed to put blah blah.
so that that's a lot of information on which we could rely to generate.
synthetic otap traffic that are meaningful without effort.
We rely on those catalog that are generated by the Semantic convention group or potentially by any
application hotels that
use the the custom Semantic Convention registry option that we, they can now leverage with the hotel weaver and semantic convention projects.
So, for example, at some point, if we if we use the semantic convention to represent
signal produced by this Otype engine.
we could generate a synthetic traffic automatically
representing something that is close to what a normal Congene will do, except that it will be fully fully simulated.
jmacdonald 00:56:45 Is there any way you would recommend? Like I I sense that there's like some attributes have constant value, or there's like one value in the whole system, or maybe 2, and then there's some that are like 10 to 20, and there's some that are like 1,000. Is there? Is there that level of detail in.
Laurent Quérel 00:57:03 Yeah, yeah, definitively.
in in the in the Weaver project, we we don't try to address that yet. We add ideas regarding supporting
annotations.
that could be used, for example, to be to determine. Okay, this metric value. The normal range is about between this this value, and this one or the distribution is
of this kind.
So we could leverage a notation to express what you just said. Cardinality about attributes parameter. I think that
the the right, the right way to do it is either we support annotation directly embedded into the semantic convention descriptions.
That's what we already support in Weber. And and that's what
was also. Certainly looking for integrating at some point.
or we could also support like on on the side annotations
where? Because sometimes you can't modify the an existing registry. It's let's say you are reusing registry version 1 35, defined by the the Semantic convention group.
and you don't have any way to to update it, because it's so one way to do it is to have annotation file on the side that will enrich that based on the the Ids that are
immutable in into this registry. And then we have a way to reattach automatically those annotation that's something that we could imagine to to support at some point.
jmacdonald 00:58:52 Got it so you'd have a config file, saying, This is a Gaussian distribution. Here's my.
Laurent Quérel 00:58:58 And and you refer that to a specific attribute. Id, for example.
and then the the receiver. Looking at these 2 files, we'll be able to
to discover what to do, and we and we can change that without requiring any modification on the registry side.
jmacdonald 00:59:16 I'll share a link here. This is the last time I worked on something like it. We used it early on in the hotel arrow phase one. So you remember it like what the configuration for this was a file that was not just the semantic conventions like with value lists, but also like number of clients, number of resources, number of.
Laurent Quérel 00:59:32 Yeah.
jmacdonald 00:59:33 And so on.
The the thing I remember about this really is it's just a burden for like, if if the project doesn't provide a generator and some user needs to maintain their own generator. It's real pain like this is, this is hard to get right. And we were maintaining it. So every time the collector made an unstable version change we had to go back and fix our generator. It sucked. So let's not do that.
Laurent Quérel 00:59:57 Yeah, they agree.
jmacdonald 00:59:59 Thank you all. I think we've reached the end. Any last words.
Let me know if I can help you, cause I didn't give my update, and I'm just doing go stuff. Ukar says, Hello.
Utkarsh 01:00:11 I just one quick question. So the diagram, the diagram that Laurent showed initially at the start of the call. I was trying to understand like it, said Otap, receiver. Sends to Otlp exporter and Otlp. Exporter sends to otap
so it was the other way around. So that's on purpose. I was just trying to understand if that was.
Laurent Quérel 01:00:32 That. My goal was to
to demonstrate that what we have we'll be able to translate protocol in any direction.
otap to a tap or tap to a Tlp C slug to to a Tlp or C slug to a tap.
I think that's something that that's the kind of
auto control station that we we could demonstrate our TV soon.
Utkarsh 01:00:58 I see.
Got it? Yeah, no. I just wanted to make sure.
jmacdonald 01:01:02 And just to emphasize like we should be able to perform very well if you're not deserializing, which is an important use case for a collector, in my opinion, so that'll be good.
I
Just. We'll we'll say, for the record I am going to follow up with a couple of people at Microsoft that have not been giving updates. And and I need to know more because I have not been giving updates. So I will come back with more information next time.
So thank you all.
Laurent Quérel 01:01:25 And I will share the I will share on the hotel. Maybe the a screenshot of this set of scenarios
always everyone. So maybe that will be useful as a reference.
jmacdonald 01:01:36 Might might be a good document, or, or, you know, issue, file as well. If you, if you want to do it.
Laurent Quérel 01:01:41 Yeah, that's that's maybe we can create just a tier for that. Yeah.
jmacdonald 01:01:45 Alright, thanks, all.
Laurent Quérel 01:01:46 No kidding.
jmacdonald 01:01:47 See you next time.
Laurent Quérel 01:01:48 Bye.
