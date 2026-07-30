SIG: Arrow SIG
Date: 2025-09-09
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**albertlockett** 01:03 Hey, Chris.
Hello there, bro.
Oh, you guys are together. Cool.
**Laurent Quérel** 01:16 We increased the… the volume.
**albertlockett** 01:21 the volume, it sounds okay on my side.
**Laurent Quérel** 01:25 No, no, that's okay, perfect. Now, it was not, high enough for us, but, because we are in, We don't have the headset, and the level of sound in this room is… It's not super high, but high enough to be, to be pintful.
By the way, yesterday, I used your example with Data Fusion.
**albertlockett** 01:52 Oh, good.
**Laurent Quérel** 01:53 Yeah, works very well. I did some modification.
**albertlockett** 01:57 Okay.
**Laurent Quérel** 01:59 what I try to do is having the… the REST engine working with the scenario, the fact, plus, the, Parquette exporter, and, And 3 examples running in parallel with different queries.
in a different CLI window, and… So, slightly different from the queries we did, but… That works pretty well.
**albertlockett** 02:23 Cool.
**Laurent Quérel** 02:25 Yeah, I think we can, we can demonstrate that, During this event. But during this, SIM meeting.
Hey!
**jmacdonald** 02:44 Hello, hello. I will share notes unless we want to jump right into a demo here, and we might want to just do that.
**Laurent Quérel** 02:54 Great.
So, hi, Gersh, we will see you soon.
Hi, Andrew.
So, Chris and I, we are in a F5 internal event.
And, we are spending 3 days here in Seattle to do some, Some demo that we have above, and we, we basically, focus on multiple scenarios. It's using the benchmark infrastructure.
And we present the results, comparing the Go Collector with the… the Western Gene, system.
And, we have a slide deck, but we will not present the slide deck in this session, but just the demo.
I will let, Chris… Explaining that. So, if you can talk… hear me okay, the aspect ratio's a little messed up, but basically we have 3 scenarios running. So the top line here is… OTLP to OTLP, right? So the load generators, talking to both the Go Collector, pictured in green and yellow here, and the rust engine in blue and orange.
So, the first line, of course, is OTLP. You know, CPU-wise, the Go Collector is a little more efficient than us. Still, I think Albert's gonna get these numbers down by the end of the week, and hopefully by the time we're done here, we'll have a better story.
You can see my own traffic.
And we're down.
Big range.
This scenario right here is the… the same thing, but we're operating without parsing, so, in this… in these first two, we do a simple, like, relabel thing, just to force us to decode, if we skip that and just do pass-through.
OTLP to OTLP, you can see we're, you know, significantly more efficient in that mode.
The next scenario down is OTAP to OTAP, so in this case, the Go Collector does the extra translation step from OTAP to OTLP and back, so obviously we're more efficient than them in that case. This… Delta here, I think, is, Probably… maybe, I don't know if you guys already fixed that, but I think that's a known issue.
And then the final one here is kind of the one we're talking mostly to the F5 people about. We've got a syslog message that looks like the format that we use to export a ton of data around, you know, request headers, and things, and timing, and all this good, really useful data. So coming out of the Go Collector.
It's… so going into the Go Collector is, what, 35 megabits per second of uncompressed syslog. Coming out of the Go Collector is down to 5. Same traffic going into us, and coming out is down to, like, 1.2 or something. And to do that, we… we see a savings of, you know, 1.2 two cores, maybe, versus the .7 cores on the Go Collector. So, way more efficient to do the same work and get a much nicer compressed volume out of the thing. So, that's really resonating with people, I feel like, and it's a really good story to be telling.
And back to the… the only place where we have, Inefficiencies, so we identify the issues.
So, on the receiver side, we already have a very nice optimization on which multiple person worked, where we have this direct translation from The, autobi representation of a TLP to this, Apache RO representation, so we have a direct translation between the two.
What we don't have is on the exporter side. We, we have OTAP, Apache All Records.
Translated into, the equivalent of the… the rest, strict protobyte representation, that will be then translated into protobytes. So we can basically, and that's on what Albert is working right now, we can do the same approach, just bypass this intermediary representation.
That will remove a massive amount of allocation and, and basically use less work, and going directly to the… the standardization representation of Protobuf. So that's where we expect to see the… This, because there we are doing much more work than the Go Collector is doing, so we will obviously go probably between these two, these two stairs.
Between the stairs, that is the one where we do basically nothing.
We just route the traffic from point A to point B.
And… and yeah, I think that we'll be closed out for this one.
We also have… any question on this, And the thing on this demo?
**Utkarsh Umesan Pillai** 08:05 So, I had a question around, does this… Like, have the changes for the telemetry, like, we have that per every minute telemetry collection from the receivers? Does the… Does the code already have this? Like, for the code that you're testing here?
**Laurent Quérel** 08:23 I'm not sure to follow the every one-minute, stuff. Which, which.
**Utkarsh Umesan Pillai** 08:27 I think the exporters, sorry, the receivers, had a control message, I think a timer, a triggered control message, which would… Ask them to, like, send them.
**Laurent Quérel** 08:38 Oh, okay, okay, okay, okay, okay, I see. Yes, we, we merged your PR.
Where we had the select and the loop inside?
**Utkarsh Umesan Pillai** 08:49 Yep, yep.
**Laurent Quérel** 08:50 Yeah, yeah, we have that. It's part of the… It's not really visible right now. I think all these numbers up here are based on that, I think, right? Yeah.
So the, I think that we need to compare this, so what… let me reformulate that. Albert did an independent matchmark that was, like, Purely focused on that, demonstrating that, what you suggested was slightly better in terms of performance.
**Utkarsh Umesan Pillai** 09:23 Right now, in… in this…
**Laurent Quérel** 09:25 more global benchmark solution. We didn't measure the difference, because we were more focusing on value scenario and making sure that they were working well.
But we need to go back and, and see, Basically, for me, one of the top priorities for this entire project Is to make sure that We the benchmark infrastructure directly integrated into the CICD pipeline of this project, and making sure that we have well-identified scenarios that we track for every commit.
That's not the purpose of this dashboard. This dashboard was more… design for internal demos. But, we need to do something similar, except that we'll be… Comparing commit over the time with the exact same scenarios, the exact same host where the benchmark will be hosted and run.
Once we have that, I think that would be nice to see the difference between different approaches.
**Utkarsh Umesan Pillai** 10:31 And in my opinion, that's.
**Laurent Quérel** 10:33 The next top priority, for us, making sure that we have that in place.
**Utkarsh Umesan Pillai** 10:40 Okay, cool.
**Laurent Quérel** 10:42 Because we are doing big changes right now, and we have to be… We have to raise the level of confidence when we do these kind of big changes that we are not doing any performance migration.
**Utkarsh Umesan Pillai** 10:53 Right, right, yeah.
And for that syslog, this, I mean, the network discrepancy, like, on that issue, I think Chris has explained what is going on. So… within the GoCollector, there is this configuration called skip priority header, and to set that to true, I think you have to also disable another configuration called octet counting or something. So then, yeah, I think you can have the GoCollector accept the same input as.
**Laurent Quérel** 11:24 Okay. For now, I just hide the line so I don't have to explain it. Yeah, it was easier for us to… This other little discrepancy up here, I think, was an inefficiency or something wrong with the Go Collector that may or may not have been fixed. I haven't been tracking that, but I think that was an identified issue.
**Utkarsh Umesan Pillai** 11:42 Okay.
**Laurent Quérel** 11:44 Any other, question related to this demo?
So, this demo is only running for one CPU per, experiment, so we have one CPU for the Rust engine, one CPU for the GoCollector.
We… I did some experimentation on my own server with multiple cores.
for both the Go Collector and the recent gene. Results are also very encouraging for us.
But, we had some issues here and there, so we decided to, to focus on single, very basic scenarios where we have just one One core per, per option per benchmark.
But, that's also something on which we need to, to focus, making sure that we, We… we don't have… Bad surprise when we are running on a more, Regular and, normal, solution, leveraging multiple cores.
Okay.
**jmacdonald** 12:55 Thank you, that was great. And I love to see Grafana being used for a real, real good.
**Laurent Quérel** 13:01 So, let me see, I think I have… I will show you something that… It's mostly the result of the work of… Albert?
So… let's see… Sure, where is my, ghosty stuff… Okay, so I will run here… a scenario that we name fake, like Parquet, so that's the… the fake data generator that is based on semantic convention.
Generating OTAP, signals.
In this, in this configuration, we generate… Only logs.
That's the 100th year.
Basically, we generate 30, signal per second.
Each batch is about 1,000 logs.
And there are only logs, there is no other type of signals.
So let's run this stuff.
And on the exporter side, it's basically, storing… every log's received into the TMP directory of my laptop.
And here, we have, a bunch of, So this terminal is split in three areas.
Each of those areas are running, a query based on data fusion, and targeting the same, slash TMP folder.
And, and you will see that, time to time, we have an increase there. That's basically the number of logs that have been, stored.
And, yeah, you see that's increase.
And here you have, so it's more a Kunt.
Kundstar.
seeing the, .
**albertlockett** 15:09 the configuration file, plus the… I think we're looking at the wrong terminal, maybe.
**Laurent Quérel** 15:16 Yeah, this configuration file, you mean?
**albertlockett** 15:19 Yeah, were you trying to show some other output? I just… I heard you say that you had a terminal that's split in three… Windows, and we…
**Laurent Quérel** 15:29 Yeah, just for the purpose of the demo, what I did is… Running in parallel 3 examples.
that are slightly different from the one that you submitted into the repo, but those three examples are based on your example and just running different queries in parallel.
just to ease the presentation, I put them into 3 different, you're still seeing… are you still seeing the config?
**albertlockett** 15:57 Yeah, we're not seeing the output of, like, whatever queries you're running.
**Laurent Quérel** 16:01 Oh, oh, that's strange. Sorry, I didn't, understood well. So let's see… Okay, maybe better.
Okay, now it's probably better.
**albertlockett** 16:15 Yeah, this looks, this looks good.
**Laurent Quérel** 16:17 Yeah.
So you have here the… So, each of those, smallpan are, in fact, running Data Fusion queries, targeting the same TMP folder.
where the previous, where the Russian gene is, is sending data.
So we, we have the… So that's a Kunt star query. This one is, like, a filter.
With a select wear, blah blah blah, and this one is a good buy.
And we are displaying in parallel the result of those queries. So nothing super fancy there, but just to prove that we have an end-to-end solution from Producing signals, To sending them and storing them on a packet… set of packet files, and… A way to query that efficiently.
Any question on that?
Cool.
Thanks, Albert, for the… The work there.
**albertlockett** 17:31 No problem.
**Laurent Quérel** 17:42 Yeah, that's the choice.
**jmacdonald** 17:43 very awesome demo, two of those demos, really good ones, both of them. I am so, so pleased to see Data Fusion being used, like.
This is awesome.
Dreams coming true.
**Laurent Quérel** 17:56 Let me show you the… just the… there is one thing I can… an additional thing that I can show you.
Oh… Yes.
Probably this one… no, this one, sorry.
Yeah, that's the, the, the values, example. So, look at this code, it's, it's super basic, we, we just, we just basically initiate the session context for data fusion, and we run, basically, in that case.
this SQL command that was for the filter, for the group by, similar things.
And superior physique for the selected, star.
But, there is nothing really fancy there. We just use the power of that effusion, and that's really cool. I think what will be really important is to see if we can… Flattened the… this… Highly, multi-record, multi-table representation into a single one where we can flatten the attributes to ease the creation of queries.
But otherwise, works pretty well.
**jmacdonald** 19:24 Very cool.
**Laurent Quérel** 19:26 Yup.
**jmacdonald** 19:28 I have also been learning Data Fusion, little bit by little bit, and it's really powerful, so I'm pleased to see this entering OpenTelemetry.
Well, so as for the agenda that we have, I would be glad to, take the stand and share what I was going to put, what I had to say, which is not very much. So, let's see, here we are.
And if you have an agenda item, and want to put it up there, the notes are… well, you can find them.
So here we are.
Yeah, so I merged a big PR, and it had, thanks to Laurent and Albert, especially for reviews, Ukarsh as well. I am… I'm gonna tell you a little bit about it. So… Here we are. I had to touch 20 files. Once I discovered what it would take to introduce back pressure into the pipeline, I found myself handling a very large PR, and it had so many pieces that it was falling apart.
What I did was come down to, a very minimal change that introduces a new context type. The new context type is empty, so all I did was introduce, essentially, a structural wrapper around what we call now the payload, and what we call the P data object.
So I'll just kind of briefly show you that so that you don't get surprised. I… there are a couple of open PRs that have merge conflicts. I apologize. I tried to help with one for David. Let's see, this is the only file in the PR that has a large diff.
He did it itself.
And what I want to show you is that the thing that was once called OTAP P data became OTAP payload.
You may know that there's a… there's a… there are FROM definitions for the FROM trait, for the various types, which are two of them, the bytes of OTLP and the records of arrow. And so now I have a new type called OTAP P data, which is a context and a payload.
So my PR is pretty big, but for the most part, it was a very mechanical change. For the test locations, I've introduced a new method called New Default. So new default will create a P data with a default context, and for testing, that's fine.
There were cases in production code, we'll say.
Mostly receivers, where you create a new pipeline request. Those PDATAS couldn't use new default because it's a test-only method. For those, I created a very ugly method called new to-doContext.
If you're familiar with Golang, you know it has such a thing as well, the context to do. So this is terrible. That will motivate us to get rid of it.
So, to-do is the same as an empty context, but it lets you do it in production code.
I also created a method to unpack, to reverse the structural, to destructure the OTAP P data, called payload, but again, it's test only. That's because we don't want you doing that, because you're going to drop a context if you're not careful.
So, so, there's also this method, which I learned from Albert, has a canonical form called into parts, which is when you turn a thing back into its pieces. This is the method by which you get the payload back and receive the context in order to do the right thing with it.
So everywhere you see in two parts.
either I've done the right thing with context, or I've left a to-do associated with issue number 1098, Or I've used this to-do context method, which very clearly says I'm using a default context, and we need to think about what the right thing to do is for those. The batch processor has, like, 20 of them.
And I think we could probably go into each of those and create, like, a helper method that's just like, for me, the batch context, batch processor, I will create an empty context.
For now, and then we won't have 20 to-dos in there, and we can add whatever we need. I don't know that we need anything in the default context that a batch processor exports, although in the Go Collector, you probably would put a timeout on that request as well.
So, as I mentioned, it… so this is a very large change, but what you see is tons of this.
And tons of this. Payloads and new defaults in all the tests.
there… there were a few cases where we found, like, shenanigans or weird things happening. I get nervous when I see cloning of a payload.
I understand that for OT… for OTAP records, it's going to do a ref count on an ARC or an RC or something like that.
for OTLP bytes, it's going to copy a vector, and that doesn't sound good. So, this code was always copying the data.
It cloned it and did try into. Now, what I do is I call clone, and then I call into parts, and then I call try into. But there's still a clone, I don't like that. Not to criticize, I'm just sort of, like, thinking about… Should we allow automatic cloning, or, like, should we allow this cloning, or should we try to avoid it, if we can?
So then…
**Laurent Quérel** 24:55 I think the… I can provide some principle there, in my opinion at least.
I think we have to follow the same kind of approach that is used by Apache RO.
There, because mostly we are based on that.
Everything is, sorry. Everything is, read-only.
it's… it's immutable. So that's the case of every Apache RO record there. We could apply the same thing for, basically, the OTLP, byte representation. So that means that at the end of the day, in my opinion, cloning P data should be close to a zero cost.
If it's not the case, that's probably something we did we didn't follow the right approach, in my opinion.
Yeah.
**jmacdonald** 25:51 I… yeah, so I'm definitely familiar with, like, I'm starting to be familiar with the RC, and the ARC, and the cell, and all the various approaches that we use for this.
sort of thing. I will definitely follow your guidance, There.
**Laurent Quérel** 26:10 And, so, just also to provide some context for why… We, we have this, big modification. I'm not sure that you mentioned that, but the… this context is super useful to, To create the retry processor and many other control-oriented mechanisms that we want to… To support in the future into this pipeline engine.
So… The retry processor will basically, register itself on the PLATA message to declare the interest of… hack and NAC messages that could be delivered by downstream components like, exporters.
So the… it's a way for us to just use the P data message to declare interest, and to know where to send AC and NAC messages. And we could use the same kind of approach for other type of internal signals.
Control… offer control-oriented signals.
So that's the reason behind the context.
**jmacdonald** 27:27 I… as you were speaking, I pulled up, my other PR, which was a large thing, the thing that fell apart, but just… just to show you where I was with that.
This was my draft of a context type.
Remember it had a register, I had two of them, but maybe I was overcomplicating or prematurely complicating things. Then there was a reply to, which was basically saying who the interest was stated by.
and their node ID, And then they… they could supply their own state, which would come back to them when the request Coming back, propagating backwards.
But then, nothing was really fleshed out. I don't know whether option… whether the deadline should be represented as an instant, which is in the context itself, or whether it should be somehow, like, a map of key value, or a stack, or a map of stacks. We've discussed this a little bit.
But the key, sort of functional interface for the retry processor that I was working on there, is to check whether something has a reply state, and then to push a new, reply state object I'm still looking for better names, actually, but the idea is that you push onto a stack your reply-to state and your delivery address, essentially, and then This PR also shows how to integrate with the exporters to turn around the request to say, this failed, I'm handing it back to you, as well as how the retry processor, functions. What I did notice in this PR is that there's no need for, like, an integer identifier. The context is the entire piece of state. Why do you need an identifier for it?
Unless it's for observability. So, I don't have, in my draft of this, any intention to carry forward a U64 or an I64 message ID.
because I don't know how to generate them without You know, busting the cash, or, you know, some sort of other consequence there.
That's what I thought I'd cover here. My plan for the next week is to continue working in this space, because… thank you, Laurent, this is, like, the control… the making the data plane reliable is our short-term goal, you know, coming along. So, timeout, retry, failover, cancellation, and that sort of thing is what I'm interested in pushing forward as soon as possible.
**Laurent Quérel** 29:51 Yep.
And along the way, with these efforts, we, we, I think we identified, yeah, that's the, this, summary that you created, From the various feedback, But.
**jmacdonald** 30:07 I'm gonna click on one of these comments, just to give us an idea, so that we're all looking at the same kind of thing.
**Laurent Quérel** 30:12 So… Oh, good, sweet.
**jmacdonald** 30:14 here from, in my words, I had, at one point earlier in my PR, used some MUT variables… some MUT bindings, and so, instead of calling try into to split apart a context and payload, Ron is suggesting that we could Essentially.
plumb the P data through everything, but the trouble that we're having right now is that in order to interact with the P data, you have to pick it apart, and then maybe transform the underlying state.
which, causes us to… Destructure and restructure, essentially, those… those variables.
**Laurent Quérel** 30:55 Yeah, so what'd like… think about it.
Yeah, what I… So, sowing the… seeing all the… what we have in this PR, plus what we had before regarding PDATA, and I tried to To think a little bit more, and… let's say, what are the issues with the current approach? And in my opinion, we have multiple small issues, and I think it's the perfect time to try to solve them and avoid to accumulate too much technical debt.
So, in my opinion, the current issues are… The API is a little bit too complex. The API related to P data is a little bit too complex.
Could be sometimes… And when we combine that with the split mechanism context slash payload that Joshua was mentioning.
Then we also have some ways to misuse the API.
So the… it's… it could be error-prone. For example, you forget to provide the context that was, that you get from the incoming message.
So you didn't propagate, basically, the context properly. I lack an API where this kind of issues is just basically impossible to, to miss, or to get. So a more… a safer API, where misuse is not necessarily impossible, but much harder.
To achieve, and, so that's the reasoning behind this set of comments.
that involve multiple modifications, both in P data and in how this, wrapper that, Joshua created, the, the OTAP P data with the context and payload will be designed. So right now, we have, like, an intermediary, temporary, step where… With… that could be error-prone, and we will progressively move to this, in my opinion.
lesser upon, and potentially more efficient, because what I like to do is also adding the complexity of determining what is the most efficient representation of this P data. Do we… do we want to keep the OTLP byte representation, or the OTAP representation?
In my ideal API, we should not see that. It's an internal optimization, and we can decide, based on the operations that are applied, when we have to move from one or two to the other.
So that's the, the… The reasoning behind all this stuff.
**jmacdonald** 33:46 Gotcha. I totally agree with your ideas about, API safety and, like, making APIs that are impossible to misuse. So, I just don't quite feel like I have the skill and experience in Rust to feel that out by myself, so, I look forward to, You know, the future.
**Laurent Quérel** 34:07 No.
**jmacdonald** 34:08 -
**Laurent Quérel** 34:10 I like to use this, this opportunity also to mention I think that could be useful for, For others, maybe to apply sometimes when we are in a similar situation, because that will happen in the future, for some other modification or big, big changes, we have to apply. So… In order to come with a proposal, what I did is I created just a very basic prototype with empty… it's basically a set of signatures.
I created a symmetry of an API, with empty implementation, and you can use the… the unreachable or, unimplemented macro that's, basically authorized to create a function that returns anything, and the compiler will not complain. That's a very powerful thing.
But you can basically, create your mock of APIs and try to see how things Go well together.
And that's exactly what I did to do this, to do this feedback.
So that's why I'm pretty… I'm pretty confident that we can go in this direction?
Because I have, in fact, like, a mock of that, in one file.
And I need to share that into the, the… the GitHub issue that you created.
I'm saying that because I think that's something that we could do, anyone in this team, do at any point of time. When we have a big change, we can model and mock it with this approach.
And it's working well.
So I recommend to use the such approach if you don't know it.
**jmacdonald** 36:03 Interesting. So you're saying we could just throw unreachable statements in our code to, prototype Rust, because otherwise the compiler yells at you.
**Laurent Quérel** 36:13 Yeah, yeah, yeah, yeah, you… in fact, I can show you the file.
**jmacdonald** 36:19 This reminds me of one of my kind of, like, irritation points with Rust at the moment, which is really that I end up, like, making a bunch of mistakes.
wherever it is in my logic code. But the first thing it tells me is that I've got an unused variable.
And… it's like a level of a documentation comment to me, like, do it after everything else works, because otherwise, my mistakes are concealing the use that I'm trying to make, and I can't anyway. I think it's out of order.
**Laurent Quérel** 36:47 So, you see, I just created a file named explore.errs, and it's just a bunch of strict and empty implementations, where you see a lot of those things, where… I had to, to return sometimes, It's not really visible there, but sometimes I had to return a result, and I was not ready to create this result. You just, put this unimplemented, and And it's compiling, so you can check, basically, your mock of an API with this approach?
And making sure that what you are proposing in terms of modification will work overall. And it's, at the end of the day, it's just 200 lines of code.
doing nothing, but, where the signature of the API is correct, and, Yeah, it's, I think it's, a nice approach.
**jmacdonald** 37:48 I don't want it as, Instructions for my co-pilot to tell it.
How to write code that compiles before you implement it, because that seems to be challenging.
Cool.
Well, I have nothing else on my mind for the agenda, and I'd be glad to, you know, let everyone have the rest of their afternoon or something like that.
**Laurent Quérel** 38:16 Nothing else to add on my side, either.
**jmacdonald** 38:20 I don't want to put anyone on the spot, so I think we should just do it. I know what everyone else here is up to, and I communicate with all of you quite frequently, so… so we'll do this again. Thank you, and see you later.
**Laurent Quérel** 38:32 Yep, mate.
