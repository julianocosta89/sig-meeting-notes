SIG: Arrow SIG
Date: 2025-11-26
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/NYcy_krZFOCoDoGfPgNVM5fi_RnEzZLU0pBAscoc8r1laH8dA5Tuuiv8ffWUX4s.DFRtn6Waln3GMFnM
============================================================

## Zoom Recording Transcript

Albert Lockett 00:00:09 Hey, Mike.
Mike "Blanch" Blanchard 00:00:12 Hey, Albert.
Albert Lockett 00:00:14 How's it going, man?
Mike "Blanch" Blanchard 00:00:15 Doing good.
Albert Lockett 00:00:16 Cool.
Mike "Blanch" Blanchard 00:00:17 I think Drew is gonna join in a second. We were on another meeting together.
Albert Lockett 00:00:23 Oh, nice. Yeah, I, I don't know if Laurent's gonna join or not. Let me just.
Mike "Blanch" Blanchard 00:00:29 Lucy's offline.
Albert Lockett 00:00:32 and, but I also saw that he had a conflict, so I don't know,
But that's okay.
Yeah, let me just pull up the, SIG meeting notes here, drop them in the chat.
Are you, taking some time for Thanksgiving?
Mike "Blanch" Blanchard 00:01:18 Just like Thursday, Friday…
Albert Lockett 00:01:21 Nice.
Mike "Blanch" Blanchard 00:01:25 How about you?
Albert Lockett 00:01:28 No, actually, I'm located in Canada, so I don't get the… well, I mean, we do get a holiday for it, but it was, like, back in October, so.
Mike "Blanch" Blanchard 00:01:36 Lafanium.
Albert Lockett 00:01:37 So I'm gonna… well, you know, it's not gonna be too bad, I'm just gonna, you know…
Heads down and try to,
Get some work done. Later on.
Laurent Querel 00:01:49 Yeah, Bill. Hi, Mike.
Mike "Blanch" Blanchard 00:01:52 Hey, Ron.
Gonna waitin' to see if Drew pops on.
Laurent Querel 00:03:37 Amelia?
Albert Lockett 00:03:38 The list that you sent me.
Laurent Querel 00:03:41 That's very funny.
Albert Lockett 00:03:44 Yeah. We were, mike, for your,
benefit. We were talking about how in…
in Quebec, where I live, it's also a French-speaking place, and unlike in France, they tran- they have, like, they translate the name of every film into French.
And it's just like, for whatever reason, the government forces them to do this, even though they don't do it in…
France, and so we were just… we were looking at the list of,
Of films, and laughing about some of the funny, translations.
like, Big Mama's house would be translated to, like, Shay Big Mama or something, right? So it's a little bit goofy, so… That's what we were laughing about before the meeting, we drew.
drewrelmas 00:04:41 Hey, glad I could make it to this one. I unfortunately have a meeting at 2, so I'm only here for the first half, but…
Albert Lockett 00:04:49 Cool.
Sounds good. Okay, well, given that, does anyone have any,
agenda items they want to start with, or I guess the other thing I'll ask is, Drew, given that you're only here for the first half, is there anything that, you would like us to talk about, before you have to take off?
drewrelmas 00:05:14 Yeah, so I spent, like, 30 minutes-ish this morning looking at the initial API scaffolding that you merged, and
the filtering that you pushed in this morning, so… or that you published.
So I… as I'm sure you and Laura are aware, like, I haven't been the most involved personally in a lot of the OTAP stuff, so I'm trying to use this as an opportunity to…
Learn more about…
how the data structure actually works underneath the hood, and because I'm familiar with, like, filter, it's helping me. So I'm still learning, but a question that I wanted to ask you is, you know, I know
there was a point in the code, I don't have it up in front of you right now, where you talk about, we rely on data fusion execution plan to do some things, but other things you just were using the regular arrow, functions to do, similar to Attributes Processor today.
I know Blanche, I think, told me that you had said you were already somewhat running into things where it's just easier to do straight and arrow compared to trying… like, are we trying to fit in data fusion too much? Is it worth…
doing a… like…
raw aero version first, and then seeing how Data Fusion fits in. I'm just curious, with your most recent PR, what you feel about that.
Albert Lockett 00:06:45 Yeah, so, one of the challenges that we ran into with, just using a DataFusion execution plan, which is, like, their,
Their version of, like, a physical plan, physical database query plan.
Was that, you… Let me think about how to put this.
You sort of have these, stages in each plan that…
are, responsible for materializing or producing.
a record batch with some given schema, right? And so, if we think about the OTEL,
the hotel arrow model, each OTAP batch is not just made up of one arrow record batch with a given schema, it's made up of multiple arrow record batches. So, for example, you would have Flake for logs, the root log batch, and then hanging off of that
if you think of it like a UFL diagram, would be like an app.
drewrelmas 00:07:55 attributes, and etc.
Albert Lockett 00:07:56 resource attributes, and… that tree kind of… kinda goes down for the different signal types, so…
One thing that was a little bit tricky when we said, okay, we want to use, like, the data fusion execution plan is you could say, okay, well.
I could have, like, a table scan operator that… or stage in the data fusion plan that produces my log batch, and then if you say, okay, I want to filter by, by attributes, let's say, you could have another scan operator that would
Produce that,
log attributes table, and then you could have a DataFusion join operator that would join those two together.
drewrelmas 00:08:40 Pershing back together, yeah.
Albert Lockett 00:08:41 Yeah, exactly, yeah, you get what I'm saying. And then, so depending on, like, what you're trying to do by filtering attributes, whether you're trying to say, okay, I want to have my logs that have this attribute or this attribute, but not this attribute, and then I want to filter the logs by whether some property is some other thing.
That just got really complicated to plan, because we end up, doing.
drewrelmas 00:09:06 I saw the bitmask thing, you have to find the filter result on the attributes and then persist that back to your root, right?
Albert Lockett 00:09:15 Yeah, exactly. So that… that made things, really… really tricky. And then, so…
what, the… the scheme that I kind of came up with is still using…
data fusion, but it's not actually using the, the physical plans that would, like, produce the record batch, necessarily. There's a,
There's kind of…
I guess you'd call it, like, a layer below the actual plan called, a physical expression, and, that's, DataFusion's representation of, like.
A, an expression that would produce a, like, an arrow array.
And so you can write a physical expression that produces a Boolean array.
that is… we treat as a selection vector, so it's, like, which rows passed this predicate effectively. And if you actually look in the DataFusion, like, filter exec, like, their operator for the physical plan.
drewrelmas 00:10:32 I would use that.
Albert Lockett 00:10:32 It uses that, yeah. So, what I thought might actually be easier in the… in the filtering implementation of our call in your query engine would be, okay, instead of using these
these… these data fusion execution plans and trying to, like, as the output of each plan, materialize the whole record batch and then join them together. It might just be easier to, like, to…
translate, our AST into these physical expressions that we can then run on the, on the record batch that are part of the OTAP batch, and then a lot of the logic in that, that filtering code that I wrote is
combining those selection vectors back together to produce the result of the… of the whole predicate, right? And so, that, that's what I… anyway, that's what I did in that PR.
So it's kind of a… it's kind of a mix of…
using the parts of DataFusion that I think work well for us, and then combining the output of those pieces back together using the, the Arrow compute functions. So, for example, the compute functions we're using are things like, the…
the AND compute kernel to take the intersection of two selection vectors, or the OR compute kernel to take the union of two selection vectors, and so that's what I mean when I'm saying we're using, a combination of
data fusion and the CAN functions. The CAN functions are just combining the selection vectors back together.
So that's, that's, that's… that's how that PR is, is implemented.
Laurent Querel 00:12:31 I'd like to add something on that,
I really like, personally, their approach.
Because…
So, if you think about it, let's say that we are not talking about data fusion, but let's talk about any SQL-oriented
processing engine, or even… the curator.
These two things, they take one table, generate one table.
they are not taking one table and generating multiple tables, or taking multiple tables and generating multi-tables. It's very hard to express, in fact, in a SQL engine, this kind of stuff.
And what we have to achieve is exactly that, unfortunately. We have a data model that is relatively complex.
And then we… so we compose of multiple tables, multiple Apache records with different schema, and we have to produce
multiple of those Apache Arrow records with
More or less the same schema, but with some processing that we operate on it, and still the produce
Apache records have to be, consistent and… and well-formed to represent a correct OTAP batch of signals.
And consistent with the OpenTelemetry model.
So, that's why I think the fundamental reason why Data Fusion was hard to use end-to-end was because of this
A fundamental limitation that you will have anyway.
In any high-level query engine.
So… I really like the approach of
taking some part of the data fusion system.
drewrelmas 00:14:23 We're using some of the internals.
Laurent Querel 00:14:25 Yes, some of the internals, and the benefits is…
The huge amount of work that they did regarding all the… the processing layer and function that already exist and well-defined.
That we can reuse without re-implementing them, because otherwise we will have to do all this stuff.
And also, that's… I'm not sure, I need to check with the… is the optimization of the expression level accessible for us, or it's something… okay, so then we will also get all the optimization that they will apply on those expressions.
And that's… so for me, it's a very well-nice trade-off between raising at the maximum data fusion, but not also
Putting us into a corner where expressing the full piston, will become… Super, super hard.
drewrelmas 00:15:19 Very hard.
Laurent Querel 00:15:19 impossible, because we can imagine a very complicated, pipeline, OPL pipeline.
That will be based on many, many stages, with some branches and some merge
I mean, good luck to express that with a SQL query, or similar things. So, yeah, I think it's really cool.
drewrelmas 00:15:42 Okay.
Yeah, I really like that explanation. Blanche, I'm curious, do you have any thoughts on this? Have you gotten a chance to look at the PR? I know you left the one comment.
No, neat.
Mike "Blanch" Blanchard 00:15:54 A lot of time.
My gut reaction is just, if I see us going back and forth between Arrow and data fusion.
You know, my…
my instinct is there's some cost to do that. And just playing with data fusion, trying to prepare plans and stuff, there's some cost there. So I just want to make sure at some point we measure
And… have an answer for, like, is utilizing these data fusion pieces.
drewrelmas 00:16:22 actually saving us.
Mike "Blanch" Blanchard 00:16:23 providing enough benefit to justify whatever we need to do. And if we just manipulated Arrow directly, would that just be better? I don't know, I don't have enough experience here.
So what I'm doing is I'm trying to wrap up these functions, and then I'm hoping to get into this and help answer some of these questions, but I'm not opposed to anything.
I just… just kind of…
piqued my interest, and I started to question it a little bit, like, okay, well, let's make sure that the juice is worth the squeeze when it comes to data fusion.
Albert Lockett 00:16:57 Yeah, so that was… I think that, you know, trying to quantify that… that overhead, is definitely top of mind. In fact, like, for me, my… my next
direction I'd like to take this before trying to, like.
at, like, fill all the gaps that we don't cover for filtering is to do some, some performance analysis, so…
I started doing that today.
Just using, essentially what's in our filter processor, and then doing the equivalent thing with this, this, the code in this PR, and measuring the output of the two.
And in fact, like, let me get the…
Laurent Querel 00:17:50 You already did that, right?
Albert Lockett 00:17:52 Yeah, I already did that, but that was when I was using the execution plan, so I wanted to.
Laurent Querel 00:17:56 Meaning.
Albert Lockett 00:17:57 with this implementation, where it's… where it's just using the physical expression, and so we're… like, it looks like, depending on the type of query we're doing, we're somewhere between, like.
22… Up to 60% faster, but somewhere between, like, 20…
Mostly somewhere between, like, 20 and,
30% faster, depending on the batch size and, like, what, like, what we're actually filtering, so…
You know, I think that there's, there's, you know, I still probably need to go a little bit deeper, and just try to figure out, like, okay, is, like, there's some,
Is there some bottleneck in our… in our filter processor code that's, like, that's making that slow, and that's why it's not, like, really that, like, a fair comparison, but…
just, like, the initial performance numbers that I'm getting from what was implemented in that PR are comparable to what we implemented in the filter processor, which was just using the arrow
compute functions, so, like, I'm gonna take this deeper, for sure, but,
But, you know, the initial numbers are…
pretty… pretty decent, I think, in my mind, so…
That, that, that, you know, but, but yeah, like, like you said, like, we, we definitely want to, like, understand, like, like.
are… are we, are we… are we, you know, doing… doing too much with Data Fusion gonna cause us some… some overhead? So I'm gonna… I'm gonna continue that investigation, like, that's.
Laurent Querel 00:19:42 Yeah, because…
Albert Lockett 00:19:43 Pretty…
Laurent Querel 00:19:43 Yeah, I think it's… just to clarify the numbers,
what you are saying is you're observing 20% to 60% better results when we are using this combination, DataFusion plus Apache Arrow versus
For the same expression, what we did for the filter processor, right?
Albert Lockett 00:20:04 Yeah.
Laurent Querel 00:20:04 Okay, yeah, for me, it's not a surprise, because, like I said before, the, I mean.
Data Fusion is… The people that are working on Data Fusion are the same people that basically work on Apexio, more or less.
And so they know very well how to use Apache IO first.
And second, they work on that for multiple years. It's not just, like, a one month or two months. So they applied a lot of optimization, and not only purely how to better use Apachello, but also how to
Better organize the expression themselves to make them more efficient.
And without even looking at all the functions that are supported by Data Fusion that are not necessarily directly available from Apache RONAL functions. So…
that's why I'm so confident and so, so happy with this, This approach.
And I can understand your concern, Mike.
But it looks for me like a very good trade-off. And the override by itself, I mean.
The main interface of interaction is… are the Apache Arrow records themselves.
And it's true for all the two approach.
So, in fact, we have exactly the same type of interaction. And, my understanding of what,
Albert did in terms of optimization, for example, to abstract the schemas
In order to reuse the same…
Initially it was the same physical plan, or the logical plan, but now I guess the same expression.
Make the difference even between the two approaches even smaller than it was before.
So we don't pay the overhead of creating a new… a new plan, because we have a new Apache RO record with a slightly different schema.
there is, if I understood well.
an additional optimization that Albert did that just prevents us to do that. Which could be, if that was not the case, could be definitively an override that we are not ready to pay.
And I think that's what we are observing for so good ways now.
Albert Lockett 00:22:35 Yeah, and just to be clear, in, in this, in this PR…
That I've opened. It,
It doesn't handle… yet? How, like…
needing to redo any kind of, any kind of planning. If the schema changes, you'll just get an error, but
I had some… I had done some investigation on how to handle that when I did the original
kind of proof of concept of this. And that was trying to reuse the… the… the execution plans, the physical plans, but we were able to…
achieve that, and even achieve a way to do that sort of efficiently, in cases where, for example, optional schema, optional columns are coming in and out, and the type is changing just by
Slightly changing the, projection of the… of… of what the physical plan received as a table, so…
I'm pretty confident that we can do something similar to get the same kind of performance, with this new approach, and not pay the overhead of, of replanning the physical expressions for every… for every batch. I, like…
need to go implement it, but I'm fairly confident that we can make that optimization.
Laurent Querel 00:24:18 Question, regarding the type provider, the table provider, that's the term, right, used to make this,
the independence between the real schema of the Apachello record coming.
I mean, across batches, right? That's the table provider. My question…
Is the table provider mechanism could be used to create
Some kind of virtual views of…
a collection of Apache Arrow records that are connected together, but will be visible externally as a single
wide Apexio records. Is it possible to…
To use this table provider interface to,
To implement this kind of view approach.
Albert Lockett 00:25:10 Yeah, you, you could, for sure. So,
So, just trying to think about what the schema… Of that would…
look like. You would have a,
I guess, like, your attributes table would be a…
A list array that contains structs.
And you would need to compute the offsets. You would need to sort by parent ID and then compute the offsets.
Laurent Querel 00:25:43 So…
I was thinking… so you are aware, I think, of the… what PolarSignal did,
They, they are basically, storing…
or at least they were, when I discussed with them one year ago, but they were storing Apache RO records… I mean, sorry, OTAB batches directly in Parquet format.
With the approach of creating very wide table.
So they, they are basically inverting, so instead of having…
a table of attributes. They are creating, basically, an inversion of that, and putting all the attributes into the… a single table, so the…
for every attribute name, a distinct attribute name, they have a dedicated column into the global Apache records, or packet table.
And that… and they were doing that per batch. So my question was…
I'm not sure if it's even useful for what we do. I think what you do is even better, but at some point, I had that in mind. I just want to make sure that maybe at some point that could be an option.
We know that
attribute name, so we have this, attribute, Apache Arrow Records, and there is a dictionary to represent every name for those attributes most of the time, because
There is a relatively low cardinality for the attribute name.
So we could look at the…
We could look at the dictionary.
Of all attribute names, and automatically determine what could be the schema of Something that is flattened.
This platinum representation is, in fact.
all the columns that you have into the… let's check for the logs. All the column that you have in the log, Apache, or record.
Combined with all, and combine with all the columns representing each individual attribute name.
And that represents a flattened Apache Arrow record.
Of all logs with their corresponding attribute, except that it's totally flat, and there is no longer, join to achieve and things like that.
That's basically what I had in the first initial, demonstration I did a long time ago, in my first initial REST-oriented collector,
I had this gigantic Apache Arrow record, and it was easy to do some filtering. Just select from log where blah blah blah, and each individual column where, basically, an attribute name.
With sometimes a prefix to avoid collision between the column names.
So, table provider could… Achieve a search transformation, so… which looks like a view mechanism.
Albert Lockett 00:28:56 Yeah, yeah, it could. Like, I don't think, like you said, I don't think it's, like, necessarily something that we would need based on, like, the implementation I did in this PR. Yeah, I think it is. One thing I would wonder about is, how…
We would,
Like, whether we would actually materialize those columns, or whether we would have, like, an ability to,
like… Have, like, a virtual,
some… some kind of, like, virtual, column, and I don't necessarily know how you would do that in Arrow, because, like, what… so what gets passed between DataFusion, like, steps is, like, actual record batches. It's not, like, an interface, so, like, you would need to essentially implement, like, the,
array trait for those virtual columns in a way that's, like, in a way that's.
So that's… that's, like, the engineering challenge, but,
But we might be able to. But like I said, it's not something, like, we need to do based on the implementation.
Laurent Querel 00:30:07 No, no, no, I agree, I agree.
Albert Lockett 00:30:08 It is interesting, yeah.
Laurent Querel 00:30:10 Nope.
Albert Lockett 00:30:11 Nope.
Laurent Querel 00:30:11 Great kid.
Albert Lockett 00:30:13 Cool.
Laurent Querel 00:30:14 A question for Mike, so, Mike, you are aware of the OPL, document…
We have more and more people looking at this document, and we are making some,
basically, Albert just updated this document last week. We have someone here at F5 that is looking at the
The language and try to, to,
To work on the type system and formalizing it a little bit more.
To make this specification a little bit stronger.
So my, my question for you was, how far…
Albert Lockett 00:31:01 Hey, Mike, did you, did you catch that? I just saw in chat that you stepped away, maybe before Laurel started.
Mike "Blanch" Blanchard 00:31:07 for a second, sorry.
Laurent Querel 00:31:08 Oh, okay, okay, okay, sorry. So, just to summarize, I had a question for you, Mike. It was about, the OPL specification.
I don't know exactly from… at which point you have been able to capture, but I will reiterate anyway. So we have people that are looking at this specification, we already observed some interest.
in fact, multiple interests from multiple persons from OpenTelemetry. We have someone inside F5 that is helping us
with, A nice background in programming language in general.
That is looking at this specification to improve the type system.
specification for this, OPL system.
So my question is, how…
far for you, that will be to be more and more compatible. So, two questions. First.
Did… have you been able to check internally if this OPL
initiative, is of interest for Microsoft and for you. Second question,
If the answer is yes, it's interesting.
How far that… I mean, how much effort that represents to…
To help us to build this intermediary representation that you already have.
for more a KQL-oriented approach, which is very close to the OPL in terms of syntax, and…
concept, but with some variation, how that will be difficult to progressively support the…
the values, additional constructs that we, we define into, into APL.
Mike "Blanch" Blanchard 00:32:59 So… I haven't seen anyone… jump at…
the proposal with, like, any level of excitement. The general feel I get from talking to people is.
We're really hesitant to define a new language.
The direct direction I'm getting from my manager is…
the mission that I have is just to make sure that the query engine is not tied to any specific language.
It is a mission to support
any and all languages, right? So, we've talked about T-SQL, PROMQL, I guess there's some interest in, like, some kind of Splunk.
So, I'm fully supportive if this specification needs, like, I saw the conditional expression.
I'm more than happy to help.
with conditional in the tree, and then however you want to express that in the… whatever language is totally fine. And I can help, you know, with my experience building the KQL parser and how you do that, but…
What my goal is to make sure that in the expressions crate, in our tree.
You can express everything you need to do.
conditional, fork, map. I want to make sure that whatever SQL needs, PromQL, this new thing, I want to make sure that
Nothing blocks you. And then if we want to create a new language, if the OpenTelemetry community wants to create a new language, I have no issue with that.
I just don't know how much time I personally will invest on building, like, the compiler or transpiler parser for it, versus making sure the expression tree supports it, and the engines support it, which is sort of…
Laurent Querel 00:34:56 Which… which engine are you talking? Because I didn't see any engine.
Or maybe I'll miss it.
Mike "Blanch" Blanchard 00:35:03 So the engine we have today is the record set engine.
When we're working on…
Laurent Querel 00:35:09 What is the purpose of this record set, Gene? I don't, we understand.
Mike "Blanch" Blanchard 00:35:14 So what we're using the record set engine for today is in the traditional collector, so the Go Collector.
What we do is we take
the batches of… they're like protobuf objects, essentially. We FFI them into Rust.
We run them through our record set engine.
So RecordSet Engine is an implementation of the engine, so we take the tree from KQL, and then we run it over batches of logs, essentially.
So, record set runs on… Batches of records.
So it's not arrow structures, it's like traditional, here's an object, and it has properties, and subproperties, and arrays, and it just runs, sort of, in memory over live objects, if that makes sense.
So if we go and define conditional in the tree, and we want it in arrow, I would probably go and do the work of making sure it's supported in record set as well.
Because we have other partner teams that have their own legacy agents and legacy backend things.
they're not going to be able to move to Arrow anytime soon, but they're interested in using
our feature, which is let the customer bring their own KQL, and then run that thing.
Laurent Querel 00:36:35 But, Justin, can I… Go ahead.
Sorry to interrupt you. I don't capture the… So…
We are supporting the TLP NRO natively.
So for any agent, there is… I don't see the argument of saying that,
We need records set for this specific context.
We don't, in fact, because… They can send us,
OTLP traffic, we are even faster than the Go Collector, even for OTLP traffic.
So what is the benefit, Evan, for a situation where
You have agents that are generating OTIP traffic, Not using the, the internal RO-based query engine.
Just trying to understand that.
Mike "Blanch" Blanchard 00:37:23 Some of these agents aren't doing OTLP.
They have their.
Laurent Querel 00:37:28 Okay.
Mike "Blanch" Blanchard 00:37:28 Park lines for completely different things.
So there's a very strong break between… if you look at the expression tree and the engines that we have today.
Nothing specific to OpenTelemetry in them.
they're definitely built with OpenTelemetry in mind, and they're sort of purpose-built to work really well with OpenTelemetry schema and primitives and stuff like that, but…
It's not an OpenTelemetry solution.
The record set engine allows you to bring your own records with their own schema and run them through queries using their own… like, it doesn't force you to have a resource or instrumentation scope. It's all abstracted away, sort of like Data Fusion is.
Then we have this specific OTLP bridge project.
That's where we put our OTLP logic.
So what Drew has is a GoFFI that calls into that bridge. So what we did is we put all the OpenTelemetry magic in a special crate that kind of customizes everything to make it work.
But these teams that are looking at… they're not looking at that OTLP crate, they're looking at the KQL parser and the records set engine.
On their own, and they want to hook it up in their own pipelines and data that, like, who knows what shape it has, if that makes sense.
So, I wouldn't say necessarily we'd ever use the record set engine inside the OTel Arrow version of the collector. That's not really what it's for. It's… it's just an implementation that allows you to run queries over
complex types.
And then we can integrate that where needed. Then we want to have a columnar engine that takes arrow data structures and essentially does the same thing. That's more interesting for our immediate use case in OpenTelemetry in the Rust collector.
It may be interesting to other parties that are Arab.
But I feel like there's a lot of teams that still… Arrow's new…
it's a little bit more of a rewrite for these teams, you know, they're in .NET, they're working on, you know, classes, like, it's a bigger ask for them to say, you gotta go rewrite your whole pipeline in Arrow to use this query thing, versus, oh, we have a thing that you can pretty much just swap in, you know, you have to shim a little bit, but it's…
It's a little more easy of a adoption for some of our legacy stuff, if that makes sense.
Laurent Querel 00:40:00 there are elements in what you said that makes sense now for me, and there are still elements where I don't see the problem, or I don't see the…
I don't entirely follow, because when you say people have to learn a rogue, I mean, they don't have to learn a row at all.
For example, when we… when I said we have receivers for OTAP, we have receivers for Cislug, we could imagine that we have receivers for anything, in fact.
Mike "Blanch" Blanchard 00:40:29 Imagine.
Laurent Querel 00:40:30 And then the whole thing is not a visible thing for most of the people.
Mike "Blanch" Blanchard 00:40:35 You're thinking.
lecture.
These partners, you're thinking in the perspective of the collector universe.
But for these teams, there's no collector.
they probably have a .NET web service, you know, and it's accepting
a JSON request, and they deserialize that using some .NET library, and they just get a graph of things.
And they want to run some user query on them.
So there's no receiver, there's no arrow, they just have some…
you know.NET class that has an array of, like, records.
So it's more purpose-built for that, if that makes sense.
Laurent Querel 00:41:18 So, are you saying that… It's more or less like an unbeited engine.
That could process various types of data that are not necessarily open telemetry?
Mike "Blanch" Blanchard 00:41:32 100%, yeah, so that's the goal of.
Laurent Querel 00:41:34 But there are so many solutions for that. I mean, already, I'm just trying to understand what is… Min…
If you think about that, we can imp…
Doug DB is an example of embedded database. SQLite is another example of,
Embedded database with a concept of virtual tables and things like that.
So, I'm just trying to understand the…
What will be the value added by this, generic querium gene?
Against other query engines that are also generic, like that.
already integrated in C-sharp, or C++, or whatever system. Just trying to understand the system.
Mike "Blanch" Blanchard 00:42:22 Good one.
The big one for us in Microsoft…
I hope I can say this, is… so we have a KQL engine.
I mean, that's what you see if you use, like, Azure Data Explorer.
it's this Csharp.net implementation of KQL. I don't know if it uses a SQLite or something like that. The problem is…
The thing that is written depends very heavily on reflection.
interme… IL, and .NET, it has to do a lot of dynamic things, which is just not allowed in a lot of our environments. You know, we have, like, government environments and different… and dynamic code is just a non-starter.
Laurent Querel 00:43:09 Okay.
Mike "Blanch" Blanchard 00:43:10 Rust is a solution to that problem.
So we needed a Rust engine, non-dynamic code-based.
You know, with the memory safety and the type safety, and it… there just… nothing existed. So, we sort.
Laurent Querel 00:43:26 Okay.
Mike "Blanch" Blanchard 00:43:26 it will build it, it will check a lot of boxes for us, you know, there's a lot of security things, but there's also… we need… there's a need for it in OTEL, we have these needs in our agents, it just…
it's not my idea, I can't take credit for it, I got it mostly from Riley, but that's sort of the vision, is like, well, if we do this thing that we already need in the collector, and as long as we abstract, you know, correctly, then we have this all-purpose engine that can
You can really write queries in whatever language you want.
Right now, it's really just KQL, but then execute them also wherever you need to, in a hopefully very highly performant way, high security way, low footprint, stuff like that.
Laurent Querel 00:44:13 Okay.
Mike "Blanch" Blanchard 00:44:17 If we can get away with just having one engine, the column art engine.
That would be preferred. Like, I don't want to have to maintain two engines.
And I think that the ultimate goal, you know, a year or two down the line is this OTEL Aero Rust Collector is a massive success, and we can sunset all these legacy things and just switch everything to that, and it'll all be Aero, it'll all be columnar, it's just…
I think the reality is the timing just won't be there, and there'll be teams that need something along the way.
So, I'd really like to not be working on the record set, but…
for the moment, I'm having to kind of deal with it. And I'm not saying we must support everything. If we add some features for the…
you know, open telemetry pipeline language that are only needed in Arrow, they don't necessarily need an implementation and record set.
Laurent Querel 00:45:15 Okay, that's really helpful to see the big picture there. My perspective, and I mean, I totally respect the…
the approach that you are following, and that a rider is trying to, also, to, to advocate.
My perspective is… Based on experience, trying to create the most generic system with
All the abstraction layer that we have to put in order to support multiple engine, because you have multiple…
Data sources with different formats.
is by design, necessarily more complicated than trying to focus on one thing. I think we can all accept that.
So… I mean, if Microsoft had the resource to work on that, fine,
Definitively, on our side, we are only focused, and we are only interested by
Delivering the fastest querion gene.
Or processing on gene on top of, apache Records.
following the, the OTAP, that I'm within?
For me, all the rest is nice to have, but far from a very interesting or very important aspect.
But again, if you are comfortable and confident in the fact that you will be able to create this level of abstraction into the query engine to support all of them, perfect. I'm just saying that if at some point we see that
We are not able to make progress because we have those constraints that are,
Going in the middle that aren't necessarily important for…
for the Hotel Arro project, maybe we'll have to do some other… to follow some other approaches.
Mike "Blanch" Blanchard 00:47:20 Yeah, I think that's fair.
I mean…
when I was given this project, it was all new to me. I mean, I have a lot of experience with open telemetry, but Rust was new.
query languages, like, I'm not an expert, so… I did the best.
Laurent Querel 00:47:36 So, it's great, it's great.
Mike "Blanch" Blanchard 00:47:38 we won't run into any issues with the tree. You know, luckily at this point, there's not really customers. Like, I've pushed back on everyone that's like, we need to publish these crates.
Because I just don't think it's ready. You know, I want to make sure we have a good, stable API before we go down that road. So, that's why we're building everything from source, and nothing's getting pushed out there, because to me, there's still a lot of unknowns, and we may need to switch things, and…
I'm open to all of that. Like, I'm…
Laurent Querel 00:48:09 Hmm.
Mike "Blanch" Blanchard 00:48:10 It did originally start as a proof of concept, where
it was more pipeline-y. It started with fork and map and split. It was really pipeline-focused.
And then it ended up more processor-focused with enrich and transform and aggregation, because that's what the PMs were really asking for. But I tried to leave the structure in there so that those things could be easily brought back. Hopefully I succeeded.
Laurent Querel 00:48:39 Yeah.
Cool.
Mike "Blanch" Blanchard 00:48:42 But what I would really like is…
you know, we call it a query transform engine. To me, it was a pipeline engine, it was an orchestration engine.
I think that's a little bit more interesting of a domain, and it's…
probably closer to what we need for a collector, so maybe we'll rename it at some point and do some things to it, but I'm definitely aligned on that vision.
And I know Riley, I told you the thing last week with, like, he wants…
that whole thing to be decomposed, and some of it run in the receiver. I'm like, I think that's incredibly…
from, like, a geeky computer science perspective, like, what an awesome challenge. Like, there's a lot of opportunity to do something really cool.
I don't know how we get there, but it's an exciting vision.
Albert Lockett 00:49:32 Yeah.
Laurent Querel 00:49:32 I totally agree, that's why we, we,
I think we share the same vision on this front.
Being able to express the entire pipeline directly in OPL.
from the… The receiver slash sources to, to the destination slash exporter.
And everything in the middle.
Is indefinitely, sorry?
Mike "Blanch" Blanchard 00:50:00 You might get a little more traction from the Microsoft folks, if we…
did something a little bit more like it was a YAML-based thing.
for whatever reason, it's not known to me, I'm pretty new to Microsoft, I'm in, like, my three and a half years, but people are really gun-shy about
Trying to define a new language from pain and suffering and past experiences or whatever.
So if we pivoted a little bit and said you…
define your pipeline, it's like a YAML thing, and in that YAML, you can say, here's a transform query, it's KQL, or here's a metrics query, it's PROMQL. That might be a little bit more interesting, I don't… I don't know, I'm just…
Kinda going off my… My gut.
Laurent Querel 00:50:45 Boom.
Yeah, I'm not convinced by that, but maybe I'm alone. No, I think I'm not alone, but maybe there are some people
But like to see things like you are describing them.
I don't think that TML is necessarily the trendy thing these days, but.
Mike "Blanch" Blanchard 00:51:06 Yeah, I don't know.
Laurent Querel 00:51:07 If you look at, for example, I mean, I'm also part of the semantic convention slash Weaver project, and it was initially leveraging YAML to represent the semantic convention.
I know that's… some folks want to,
to separate the project from this, YAML thing, because it's…
It's obviously harder to, to interpret and, and, and…
more complicated for people to read it than it will be with a very purposely built,
Knowledge True or Crescent…
the type of thing that, need to be represented into a semantic convention. I think for the pipeline, that's why we took inspiration from KQL a lot, because it's,
it's, let's say, graphically, syntactically, very, very close to how you will express them, on the paper to represent the pipeline. This pipe representation was nice.
We could obviously translate that into YAML, but I don't… so first, it's not because it's in YAML that it's… you are not defining a language, in fact, you have, because YAML is just a format, so you have to define the syntax that will be accepted by whatever
system reading this SAML will… will… will…
We'll have to follow to be able to interpret it.
So again, people… people that know YAML will not be able to write this subsido YAML, they need to learn how
how to organize the corresponding YAML to make
The pipeline correct at the end.
So they still need, in fact, to learn the language. Same thing for the collector configuration file. You can't write any kind of YAML. You have to follow some schema.
And unfortunately, except if you consider Boolean schema as a potential
schema thing for YAML, there is no real official schema for YAML.
And I suspect that people able to read JSON schema, natively are not so…
Numerous, because it's… it's very wordy.
And very, hard to consume.
Yeah, so that's… I think that's the main reason why we leverage KQL and all relatively nice,
Syntax, in my opinion, to represent For this specific domain.
vape lanes.
And, personally, I value a lot the fact that… the guilty that we can provide with this knowledge.
Take apart the syntax, but the guarantee of making sure that any
Data produced by the pipeline are by design.
Valid and correct,
Open telemetry signals is, in my opinion, one of the very nice things behind this initiative.
And that's also why… Not providing a generic solution for…
stream processing in general, it's… it's on purpose.
we,
especially in the… inside the OpenTelemetry project, I think it makes sense to generate something that is, by design, necessarily valid for open telemetry, and the corresponding data model.
Mike "Blanch" Blanchard 00:55:05 I hear ya, huh?
I understand that point, but we also have that, like, today with our OTLP bridge.
part of what it does is it constructs the KQL parser And… gives it… The… the log record schema…
basically for that purpose. It seeds the parser with, here's your schema, so that if you try to do something, like reference time-generated, or remove it, it'll give you errors. So, we were able to achieve that
still with the abstraction, so I don't have any concerns there. I think as you guys get into it a little bit more, you'll kind of see, like.
That should be no problem.
My only mission, the only really firm direction I get is just make sure that the engine is not tied to any specific query language.
So I'll be here to bug you guys and try to make sure that we have the right abstraction. But I don't have any concerns. I think you guys will be okay once you, like, see it and play with it. Like, that's what we have with Keiku.
Like, we have this crate, the…
you can give it any KQL query, and what it spits you out is an expression tree.
And then that expression tree should be runnable in any engine. You know, we're gonna have a Arrow Data Fusion Column R, we have a record set. Somebody else could go build their own engine if they want, as long as they, you know, take.
Laurent Querel 00:56:34 No, that I understand. That I understand when you say it's a… it's a standard pattern.
Mike "Blanch" Blanchard 00:56:40 It's kind of cool.
Albert Lockett 00:56:42 I wonder, like, how… Like, let's say we did try to…
So, the… the approach that I took with that… that filter… Implementation.
Like you guys saw, it does make some assumptions about which fields represent,
attributes, which fields represent, like, a nested struct, like,
Like, like resource, for example, on the log record as a nested struct.
So we could try to…
abstract… like, well, I'm just spitballing here, right? Let's say we did want to try to make it, like, more abstract. We could abstract away some of those identifiers, so we know, okay, this is a…
Yeah, sticking.
Mike "Blanch" Blanchard 00:57:33 showing you how I do that in record sets.
Albert Lockett 00:57:38 Yeah, I think.
Mike "Blanch" Blanchard 00:57:39 All those concepts are there, and once you kind of see it, it probably will transfer to the stuff you're working on.
Albert Lockett 00:57:46 Yeah, so then, like, I guess where I'm going, though, is I wonder, like, at what point, we end up in a world where we're…
Where we've made something that's so abstract that it's just…
like, I'm not saying that we don't make it abstract, I'm just trying to figure out how far we go with it, right? And I guess we're almost out of time, but, like.
Mike "Blanch" Blanchard 00:58:08 Yeah, maybe I'll just reach out to you after the break, and I'll just kind of give you a deep dive on what I've done so far.
It's not too bad, so, like… there's…
different sources of data. You have…
What we call the source, which is really the record context.
There's attached data, that's where resource and instrumentation scope live.
There's constants, there's variables, and I'm working on arguments for functions.
Albert Lockett 00:58:40 Profess.
Mike "Blanch" Blanchard 00:58:40 So in the tree, you have, like, a scalar expression, Let's say 2 straight.
And it expects another scalar expression as input.
So let's say you see a…
toString, and for input, it's a attached data scalar. It has a field called name.
So that'll be, like, resource. And then it has a path. So that'll tell you, I want resource, attributes, service name.
But the code to, like, traverse all of that is really the same for a variable constant source.
the only, really, pivot is, like, where do I go and find that root thing?
Albert Lockett 00:59:22 I get you, okay. I get what you're saying. Yeah, I was wondering, yeah.
Mike "Blanch" Blanchard 00:59:25 How that tree is built, how it knows, is really the domain of the compiler, the parser.
So in my world, I have a KQL parser. If user writes resource.
it knows, via some options, a resource is attached data. So when it sees a query where the user said resource something, it builds the tree with a scaler saying, okay, attach data, resource. So when it comes to actually executing the thing, it's all static.
It's all been pre-built, and it's fixed.
All of the fuzzy resolution, naming.
attributes, that's all sort of the domain of the parser, so we've kind of built a parser that has all these switches and stuff, so I can kind of give you a little more deep dive on that if you want, it'll probably be helpful.
Albert Lockett 01:00:17 Yeah, that would be helpful. I think, I think I, I think I, I get what, I get what you're saying, because I've seen a little bit of that code, so,
Yeah, so that would be helpful. Let's sync up,
Like, next week or something.
Mike "Blanch" Blanchard 01:00:32 Sound good?
Albert Lockett 01:00:33 Okay, cool, so I guess, that brings us to, the… the end of the hour. So yeah, thanks.
As Josh would say, we've done it. See you next week.
Mike "Blanch" Blanchard 01:00:48 You guys.
Laurent Querel 01:00:49 If you will.
