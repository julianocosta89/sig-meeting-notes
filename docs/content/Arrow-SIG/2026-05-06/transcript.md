SIG: Arrow SIG
Date: 2026-05-06
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/9dHPS7DO6myqFw6F-60cBOtJP7SLeZOAujSbb4zQYDggceQT2wlnw4jyAGT7-qQW.xxLdU-SicOyI2VsX
============================================================

## Zoom Recording Transcript

**Albert Lockett** 00:11 Hey, Mike.
**Mike "Blanch" Blanchard** 00:14 Hey, y'all heard.
**Albert Lockett** 00:15 Hey, how's it going?
**Mike "Blanch" Blanchard** 00:16 Good. How you doing?
**Albert Lockett** 00:18 Yeah, pretty good.
Yeah, I just… I had a quick, a chance to look over… I didn't… I didn't look too deep into your, into your, your engine yet. I had a… I had, like, about an hour to look at it today, but I… but I didn't have a chance to, like, go super deep, unfortunately.
**Mike "Blanch" Blanchard** 00:42 Any feedback? Thoughts?
**Albert Lockett** 00:45 yeah, like I said, I didn't have a chance to go, like, deep enough into it. I guess, I was more so just trying to understand, like, how the, how, like, the record, like, like, what are the structures, like, record table.
Record… record table dictionary, and And and then the factories that create it, that's kind of as far as I got.
So that all makes sense. And then I guess I started looking at the filtering code.
And, so my… my one question, I guess, and maybe this is, like, a general question, was, like, how much has changed since, like, the last time we kind of talked about this? Because I remember, like.
I think last time you showed me the code, you had, if I recall, like, like an enum that was, like, scalar, array, and then dictionary, and then in the, I think in the filtering code, you were still using the… arrow compute kernels for, like, EQ and GT, maybe, if I'm not mistaken, and then it looks like you… like, that enum isn't there anymore, and the compute kernels aren't there anymore, so it seems like you kind of changed the approach, is that right? Which is fine, I'm just trying to understand.
**Mike "Blanch" Blanchard** 02:08 I mean, a lot has changed, nothing fundamentally.
It might have just moved… So I'm calling compute for the filter, I'm calling compute for, like, NOT and OR, I don't use compute for, like, greater than, less than, or comparison.
**Albert Lockett** 02:31 Okay, cool. Were you ever using it for that?
**Mike "Blanch" Blanchard** 02:34 No.
**Albert Lockett** 02:35 No? Okay, interesting. Interesting. Cool.
Okay, and and that, and that's because the… the record… The record-type dictionaries are not always, not always… arrow arrays, basically. Is that right?
**Mike "Blanch" Blanchard** 02:57 Correct, so…
**Albert Lockett** 02:58 Gotcha.
**Mike "Blanch" Blanchard** 02:59 You're inside the engine, You can operate on native aero things.
But it also allows you to… create what look like arrow arrays. So they always have an arrow key array. So you have, like, the dictionary thing, an arrow, it has keys and values.
So I use the keys everywhere.
And it's always normalized, so any two dictionaries Always have the same number of keys, so even when you're, like, pulling attributes, that's sort of like the normalization part of it.
But the values can be either an Aero-native thing, or… a vector of… engine types.
So the expression has its value API. In my engine, I have this value or ref thing, but it allows you You can even mix those things, so, like, if you're spinning on, like, an arrow string array.
And you want to have, like, 4 rows that just spit back the string, but the 5th row, for some reason, you want… To parse that into, like, a regex.
You can just swap that fifth element with You know, a chrono regex as a value, and everything will just be happy.
That's why I don't use comparison, because I call into my value helpers for… Greater than, less than, compare, equality, those types of things.
**Albert Lockett** 04:35 Gotcha, gotcha. Okay, yeah, that makes sense. So that's the solution to, like, how we have, like, like, essentially an array that has to have, like.
heterogeneous types in it. You can just do it like that, because you don't need to model it as an array.
**Mike "Blanch" Blanchard** 04:53 I don't even care, yeah. You can… you can all day long have a dictionary with mixed with values, you know, you can have ints and bools and strings, and you can have maps in there, like, it doesn't care. It's ultra-forgiving. Now, you'll have to reconcile that It's kind of what I'm working on right now, so I'm working on extend, or, you know, the set transformation.
So I'm trying to make that work, and it's basically… the engine's gonna give you one of these dictionaries that can have all these wild things in it, and it has to be converted now to some Aero-native thing.
So that's… that's currently what I'm messing with.
**Albert Lockett** 05:33 Gotcha. Yeah, yeah, yeah, yeah. And then, and so are you, are you, excuse me.
Is that part of the… the engine calmer itself, or is that part of the… the, engine calmer OTAP bridge?
**Mike "Blanch" Blanchard** 05:52 It's… So the API surface will go on… Like, in the engine, there's, like, a columnar records, and there's a columnar records factory.
**Albert Lockett** 06:06 Yep.
**Mike "Blanch" Blanchard** 06:07 The factory might go away, I don't know, I'm in the middle of trying to make this work, and it's always the case, and whenever I work in Rust.
Like, I get everything all working, and I'm happy with all the lifetimes and stuff.
And then I go to put in a new feature, and suddenly all the lifetimes are a problem. Yeah. Currently battling that.
Filter is kind of nice because, you know, it always gives you a new array of record batches.
I assumed mutation would be the same, but it looks like you can actually take a record batch.
And, like set a new column. So, like, say you're setting, like, severity text, or I don't know.
severity number. You could just replace that array, and everything else is… is okay. So I want to utilize that. I don't want to force a bunch of allocations and stuff, so… where I had kind of assumed certain things would be immutable, now that I'm working on mutation, I'm like, oh, that was invalid, so… I'm in those APIs right now. I never liked that there were two, so I might try to get rid of the factory or do something there, but the idea, essentially, will be there's some API that's like, okay, here's a dictionary, you need to set it on some path.
And then it'll be the OTAP's bridge job to say, okay, I'm setting severity text. I know that needs to be an array of strings.
So I'm gonna take that dictionary and call a helper to swap any value that's not a string into a string, and then I'll have a nice, fully-formed arrow thing to give back to the collector, basically.
**Albert Lockett** 07:50 Gotcha. Yeah, okay, that makes sense.
That makes sense. Cool.
Yeah, yeah, yeah, I see, I see what you mean. Yeah, yeah, and that's, that's, I mean, that is the nice thing about, like, about, about record batches is, like, internally, like, the… the arrow buffers are supposed to be immutable, and they, for, like, most purposes, are, because, like, they're wrapped in an arc, but, like.
the… the columns, it's just, like, a vec of columns, so if you can get ahold of that mutably, then, yeah, you can replace one. And, I mean, you gotta, like… if you change the data type or the column order, you gotta go update the schema as well, and the schema is just a vec of fields, so you just, you know, replace that one field as well. But yeah, you gotta, like, you know, So that's… Okay.
Cool.
**Mike "Blanch" Blanchard** 08:40 When is the last time you got latest on my branch?
**Albert Lockett** 08:44 I think I got laid… I just pulled it today, Let me just… I'll pull again.
**Mike "Blanch" Blanchard** 08:52 No, that's fine, I just… I did a bunch of refactoring over the weekend and, like, Monday.
I ended up.
**Albert Lockett** 08:59 Oh, yeah, I see it. Yeah, I've got merge fixes, refactor lifetimes… Mike "Blanch" Blanchard 09:04 Yeah.
**Albert Lockett** 09:04 And then, like, yeah, I see, a commit about Geneva, so I guess Maine must have merged in.
Cool.
So, yeah, so that… okay, so that's, that answers all the questions I had.
I guess, I guess, just in terms of, like, general approach, so, you mentioned that last week that you were getting some, like, that you were getting or were going to get some… questions about, like, why… like, why have both engines, and, like, what are the use cases? And so, And I think that we had, alignment there. The answer was gonna be, we've got the engine in OTAP data flow that's, like, very OTAP specific, and then we've got the engine columnar, which tries to be, A lot more general.
And I think, like, I'm totally aligned with that, with that messaging, if that's the right, understanding.
Sorry, I had a question, I forgot it.
I guess, I guess, is there a… so… I think the other thing that we might have talked about at one point, at least it came over in the chat with Drew, was, like.
fitting the engine that you're working on into a processor. So it sounded like a… at the time, we might build, like, a… like a KQL transform processor that, That will… the KQL get executed by the engine that you're working on, is that right?
**Mike "Blanch" Blanchard** 10:58 We can, and if you… If you go and look in my branch, I actually dropped one in there.
So if you look in, like, the… whatever the path is, it's like, can trip something, experimental, where the record set KQL processor is. I have a columnar KQL processor that calls this new engine, but… I didn't spend much time on it, I just kind of copied the other one and stitched it up. The engine isn't really feature-rich enough to make that thing useful, but I thought I would need it for testing, so I created it, and then I haven't touched it since, but it's actually sitting there.
**Albert Lockett** 11:39 Oh, gotcha. Okay, cool. Alright.
**Mike "Blanch" Blanchard** 11:41 Because ideally, that's what Drew and my team want at Microsoft, is… they want to just go in and switch our templates or whatever from the record set to KQL, and if I do everything correctly, everything will just work. Like, whatever queries the user have, they'll just function faster.
So that my goal is to deliver that for our users.
**Albert Lockett** 12:08 Oh, is that, sorry, switch the templates to… Sorry, what was the thing? Switch the templates to KQL?
**Mike "Blanch" Blanchard** 12:18 No, so we have users right now… Running the Arrow Collector.
presumably they're running on record batches, they're using, like, the P data stuff.
But to execute their KQL queries, we're using the record batch engine.
So we take their Arrow data structures, we convert it to OTLP, we run the engine, we get OTLP back, we reconvert it to Arrow, and then things flow normally. So we want to just… chop off the KQL record set one, and just say, okay, we're gonna use KQL column R, and it should just work the same. It should just be better.
**Albert Lockett** 12:59 Gotcha, okay, okay, cool. And then, okay, and this, okay, that makes sense. So they're using that, record set KQL, processing… Mike "Blanch" Blanchard 13:09 I know they're using it, so, like…
**Albert Lockett** 13:12 Okay.
**Mike "Blanch" Blanchard** 13:13 Drew could go more into this, it's kind of his world, but, like, we have this whole Azure UI, and I don't even think they're… they necessarily know they're using OpenTelemetry, or the collector, I don't think they know any of that. They're just using this UI and saying, like, I want a pipeline, and I want this KQL query, and then… some giant, I don't know, Terraform, or some kind of… boilerplate infrastructure templates are created, and part of that is it configures that KQL processor, the record set processor.
And then we deploy and… The arrow collector runs with all our configuration, and, like, magic happens.
So my goal is to allow… us to switch that processor at the end of the day. Just instead of the KQL record set processor, it should be the KQL columnR processor, and everything else should just work the same, hopefully.
**Albert Lockett** 14:13 Gotcha.
**Mike "Blanch" Blanchard** 14:13 Just better, faster, stronger.
**Albert Lockett** 14:16 Yeah, yeah, yeah. Okay, cool, okay, cool, I see what you mean. Yes, this is… okay, so it's like… it's hidden… it's hidden, I want to say. It's abstracted behind some Microsoft service, but at the end of the day, your user… like, the users are using… KQL to modify their, their telemetry, I guess.
**Mike "Blanch" Blanchard** 14:34 I don't even think… So they're writing these KQL queries. I don't even think they're using open telemetry terms, they're using… some Microsoft, like, the security, common security, I don't know, there's, like, a whole other set of processors that, like, take the open telemetry data and get it in this shape that's familiar to our users, and then they query that data, so there's, like, a whole bunch of magic that's put on top of everything.
**Albert Lockett** 15:02 Oh, okay, cool. Yeah, and I did see a PR come through about that common… Microsoft Common Schema. I don't know if that's… Mike "Blanch" Blanchard 15:12 Common Scheme is a different thing.
**Albert Lockett** 15:14 Okay.
**Mike "Blanch" Blanchard** 15:17 Common schema is like the Microsoft version of OpenTelemetry semantic conventions.
**Albert Lockett** 15:24 Oh, okay.
Cool. Oh yeah, okay, I guess that would… that would make sense, because that… that… that common schema stuff's not merged yet.
Alright, cool. So I guess then, alright, cool, so that makes sense. That sounds like… so that sounds… okay, so now we… now we know what the plan is, for this engine, or I know what the plan is, so that's… that's helpful. I guess, like, do you guys ever have a, A plan going forward to… Like, expose, like, expose or run, like, OTTL or KQL on… On this engine.
And it's, it's, like, if you don't, it's okay to say no, I'm not gonna be like, oh, use my language, but.
**Mike "Blanch" Blanchard** 16:17 You mean OPL? Because it does KQL currently.
**Albert Lockett** 16:20 Yeah, yeah, that's what I mean. Oh yeah, sorry.
**Mike "Blanch" Blanchard** 16:22 I don't know about OPL, but OTTL, yes, in some capacity. So there's another person on my team, I think it's Mark.
The… he's working on… So we… Drew originally set up, like, an OTTL parser.
It doesn't really do much, but… Mark needs that.
he basically wants to replace… there's, like, a transform processor that uses OTTO, He wants to use… Query engine in that thing.
So he can use RecordSet today, he can just finish the OTTL parser, and then call RecordSet, or he can call column R, or he can use your column R, whichever one satisfies it, but yeah, so he's… Working on that.
I think there's an issue somewhere in the Arrow repo that's, like, he looked at all the expressions.
He wants to utilize your conditional expression, so I have to go implement that in RecordSet somehow, but… There is some stuff happening with OTTO.
I don't think there's any plan in, like, that Azure interface to expose OPL.
But… like, the code's all open source, so you're gonna have an OPL parser. So that's kind of what I was saying on that issue where we were discussing the get record type.
is, in a perfect world, these things are kind of like mix and match. Like, you should be able to take any parser, OPL, KQL, OTTL, or future thing, and get an expression tree, and then you should be able to pick any engine, yours, mine, record set, some third-party thing.
Any expression tree should be runnable on any engine in an ideal, perfect world.
There's always gonna be little edges and stuff, but that's sort of the whole goal.
**Albert Lockett** 18:17 Yeah, okay, interesting. So it sounds like, Yeah, and I guess, like, where I was kind of trying to… what I was trying to figure out here was, like.
If, like, if we actually needed that, that, that common, that common AST, because, like, what, like, I guess, like, where I was… where I was trying to figure out was, like, if it's always gonna be, like, KQL to… record set engine, or KQL to the columnar engine that you're working on. And on the OpenTelemetry side, it's always going to be, like, OPL to the engine that I'm working on, or OTTL to the engine that I'm working on.
then what we could do for these, like, these languages that are very, OpenTelemetry-specific, like OTCL or, like, OPL, we could have a… like a… like, we could parse to an AST that's, like, very, like, like.
OpenTelemetry dedicated, and then we wouldn't have to, like, have this, like, this, this, Like, like you said, like, these edge cases where it's like, oh, like, this is supported in this engine, but it's not support… like, this… this expression supported in this engine, it's not supported in this engine, or, like, this, like, this difficulty of trying to figure out, like.
what does get type represent in this engine or that engine? It's like, we could just know, like, we could have our own semantics, basically. It's like, we could be master… like you said, like, a few months ago, we could be masters of our own domain. Like, if we had our own ASTs, we really could be masters of our own domain, but we lose the… Like you said, the interoperability So I guess, like, that was what I was trying to figure out, was, like, if we actually need that interoperability or not.
**Mike "Blanch" Blanchard** 20:11 It's a big feature to… The people that tell me what to do.
Riley, in particular, There's this really strong… Idea that, like, the moment you tie yourself to a particular language, you've, like, end-of-lifed your… whatever you're doing.
So, like, that was, like… maybe priority number one when I was given this project is, like.
We are not going to define a query language, we are not going to be opinionated. Our goal is to support whatever query language the user wants to bring to solve their particular needs. So we picked KQL first because that's what these Azure customers are using, and a lot of people in Microsoft use it, they seem pretty happy with it.
There are a bunch of, like, weird forks around the company where, like.
you know, the original team built, like, a .NET framework version, and some other team wanted to use it, and the original team was like, we're not gonna support you, so, like, they made a fork of it, and then some other team made a fork of it. So there's, like.
core KQL stuff, and then there's all these, like, KQL add-ons and weird stuff around, but generally, people at Microsoft are pretty happy with it.
Riley's opinion was that, like, you know, for metrics, like, PromQL is probably a better solution.
There's people that like T-SQL, so, like, it was always the mission for Riley that, like, we want people to be able to Use whatever language they want.
hopefully it's already there for them, if not, they can go build it. So he, like, kind of tasked me with, like, your expression tree needs to be general enough to support any query language.
I don't know if I succeeded in that or not, I'm not an expert in many query languages, but that was the goal I was given.
And Riley's ultimate vision for this stuff was, like.
the AST, the engines, would be, like, donated to CNCF as their own thing.
So there'd be some, like… CNCF repository for… querying data.
So that's sort of why it's in its own kind of isolated little world, and I'm like, I'm super… strict or cautious about the dependencies and where the abstractions go, because I'm just trying to execute on that sort of… Crazy, grand, giant vision.
And we have seen some teams inside Microsoft that are interested in using it in other products that have nothing to do with OpenTelemetry. So, so far.
It seems like we're… we're headed in the right direction. There's a lot of people that are excited about it, and some teams playing with it.
Most of those teams only care about record set.
Because they're built on traditional software stacks, you know, where every object is a huge graph of stuff.
We haven't… I haven't seen anyone yet that's like, I have an arrow thing, can I use it? But… We're hoping, as, you know.
teams transition to Rust as Arrow grows, like, we hope it becomes more of a de facto thing, but record set at the moment is kind of important for me, because that's the thing all the teams are excited about.
**Albert Lockett** 23:38 Yeah, okay, interesting, gotcha. And, like, yeah, sorry, and, like, I'm not, like… I'm in, I'm in no way trying to say, like, like, oh, like, there's not a utility to Records and Engine? Like, I, like, I definitely see it, I, like, I see, like, all those arguments. I guess, like, what I'm trying to figure out is, like.
Whether, like… like, the engine that… that we're building that's, like, specifically for OTAP, and and and the… the language that we're trying to design, OPL, like, whether… like, whether there's a need for them to be coupled to the same, To the same, expression tree.
**Mike "Blanch" Blanchard** 24:24 I really leave that up to you.
**Albert Lockett** 24:27 Okay.
**Mike "Blanch" Blanchard** 24:28 until you expose it, you know? If you're not gonna expose, like, an enum.
what language is this? And then give me the string query. If it's just always OPL, and there's no way to pick a different engine, then no, you don't really need it, you can do whatever you want.
**Albert Lockett** 24:47 Yeah, but I guess, like.
**Mike "Blanch" Blanchard** 24:48 funny, I mean… if we succeed on that vision that Riley has, and let's say it becomes its own open source thing, and it gets its own maintainers, and there's people out there building T-SQL, and Splunk query language, and PromQL. There's all these expressions going in, and the community's making sure it's supported in all the engines.
you may want that, you know? You may regret, oh, shoot, I, like, forked it, I did my own thing, I can't utilize, but who knows? You know, that's… that's so far down the road, I'm not even worried about it, but I'm trying to… Keep the boat floating, you know, down the river in that direction.
**Albert Lockett** 25:33 Yeah, yeah, I gotcha. Okay. Okay, cool.
**Mike "Blanch" Blanchard** 25:37 Yeah, like… you know, mutability is a big thing, I have to sort this out somehow, but I'm hoping… you know, I want my columnar engine to have 100% parity with the record set, because it is a need for me to swap them in and out.
I'm hoping the perf is good enough that… You may be interested in just using it.
You know, if you stick the direction you're going, where your OPL spits out, you know, a common syntax tree.
You could just switch the engine at some point and be like, okay, cool.
That's really up to you.
**Albert Lockett** 26:15 Yeah.
Yeah, and I think, Yeah.
Yeah, we could… we could do that, too.
Okay, yeah, let me… let me think about it. So yeah, that's… I mean, that's… yeah, you're right, that is the risk. Like, if, like, the AST that's been designed as part of this work does become, like, a standard, then, like, we kind of… Missed the standard, and then we have a bunch of work to basically, like, go back and, like, retrofit it, which is… which sucks.
But it… but it does give us the opportunity to both be masters of our own domain, which is… which gives us some short-term velocity, so that's, like, the trade-off.
Oh, what was I gonna say? I had another thing I wanted to mention.
Yeah, so then, okay, yeah, there's another thing you said, which I thought was interesting. So you were in the process of implementing implementing mutability, which is… which is… which is really interesting. So that would be another thing that, like, if we did continue to parse to the same AST, then we could try the… the mutable stuff, and then if the performance is good enough and it just works, then… Then maybe that's, then maybe we just swap the engine. That's an interesting idea, too.
I can do that.
**Mike "Blanch" Blanchard** 27:37 like you to look at is, when you have a second in my code.
Go look at the scalar expressions, like, look at how, like, slice is implemented.
**Albert Lockett** 27:49 Okay.
**Mike "Blanch" Blanchard** 27:50 I think that's where I really start deriving value from all the abstracting that I did.
Because all dictionaries are sort of normalized, so you always have a key set. It's always the same number of records everywhere.
It makes implementing the scalars, like, pretty simple, pretty boilerplate.
So, like, all the complexity is really in… How you service, like, give me some data, and you spit back a normalized thing, and then how you set that data and, like, undo the normalization, but it… what it… the benefit from that is it makes… the engine, you know, satisfying, like, a substring, or a slice, or a CONCAT, it makes those, like, really, really simple to do, because you just don't have to worry about, like, you know, the attributes table, and the weird joins, or it's just sort of… I guess boilerplate's a really good way, I hope. I did a few of them, that's why if you go in there, you'll see I did, like, length and slice.
Because I wanted to do a couple reps to test, like, do I have the right helpers? Are these APIs, like, as flexible as they need to be? So I spent a little bit of time, you know, building a couple things to just kind of see that, like, okay, the scalar engine is where I want it to be.
And then once I got that done, that's kind of where it's like, okay, I'm gonna give this to Albert, he can take a look, and now I'm gonna go… Figure out how to make it mutable.
**Albert Lockett** 29:19 Gotcha. And then slice… okay, yeah, I see this. There's a… there's a slice underscore scalar, underscore expression in the scalars module.
Yes, that's interesting, and I guess… so that was another kind of question I had, just based on, like, the, Like, like you said, like, if… if you just have everything aligned, basically.
Then, then it makes, then it makes things a lot simpler, because you don't get, like, halfway through your expression evaluation and say, oh, well, this data's aligned this way, and this data's aligned this way, and I gotta go join them.
Was there ever, like… Did you ever look into, like, maybe just, like, straight up aligning everything into, like, an arrow record batch, and then just, like, feeding that straight into, like, a, like, data fusion, physical expression, because, like… like, I think about data fusion, like, basically, like, you… like, when you evaluate the expressions, you… You… you just have a record batch.
and then you feed it into Data Fusion Expression, it spits out, a, a column or value.
And… Blake.
when I started originally looking at the engine that… that we were gonna do, I thought, like, oh, we'll just use DataFusion verbatim, but then ran into this issue where it was like, oh, well, like, the… attributes column isn't aligned with, the, like, the root record batch, and so you either, like.
Do that alignment… eagerly… and just use DataFusion directly.
Or… we… but I said I didn't want to do that, because it seems kind of like… inefficient, maybe I could do it lazily, Especially for, for… for filtering.
And so I went the other way, and just said, well, we'll use data fusion expressions as much as we can, then when we hit, Like, a misalignment boundary, then we'll realign the… whatever intermediate state we need to have, and then keep… keep evaluating.
But I guess, like… my question when I looked at, like, this engine that you were working on, where it, like, where it does, align the attributes to the, the to, like, the row order of the root record, let's say. Was there ever a thought that, like.
like, if… like, I should just align these into a… into a record batch and just feed them straight into DataFusion.
**Mike "Blanch" Blanchard** 32:04 I didn't try that, no.
**Albert Lockett** 32:06 Okay. Yeah, no sweat. No sweat. And, like, sorry, I'm not, like, I'm not trying to, backseat drive, I was just wondering if, like, that was, that was, something that was, that was tempted.
**Mike "Blanch" Blanchard** 32:18 Not really, like… my thinking was, kind of, you're… you're deep into data fusion, so what I wanted to try was, like, how far can I get just Running on native arrow types.
So I didn't really do much data fusion at all.
**Albert Lockett** 32:35 Gotcha, gotcha. Okay, yeah, no sweat. No, no sweat. Cool. Okay.
**Okay, yeah, so I've… so it sounds like I've got some homework, then, to look at, the, the… look… look deeper into how Slice is, is implemented, and then, and then I can, and then I can understand, like, the… the benefit, the benefit of the, Of how do you… Mike "Blanch" Blanchard** 33:02 Take a look at length, and take a look at slice.
**Albert Lockett** 33:07 Okay.
**Mike "Blanch" Blanchard** 33:08 There's really only four. There's source and attached, but those are kind of special, you know, those pull the data off You know, either the logs, or the resource, or the scope.
But slice and length are just… Any old scalers that you can chain together, you can composite.
So they just operate on, like, here's a dictionary or a scalar, Length is pretty simple, because… it doesn't take any parameters, right? You're just saying length of the source.
Slice is a little bit more interesting because it has a source, it has a start, and it has a length.
And… those three things can individually be a scalar, a single value, or a table dictionary value, so that I had to come up with a way to, like.
Given any random set of scalars or dictionaries.
merge those things into a final single OR table. So that was kind of an interesting one to solve.
**Albert Lockett** 34:10 Oh, yeah, I get what you mean. I get what you mean, yeah.
Okay, cool, yeah, I'll have a look at this. I'll have a look at this, because, like… I'll look at this, because in the engine that, like, we, like, I would use, what we would do is we would, we would basically say, like, okay, I'm at a point where I've got 3… let's say you're calling slice with three arguments, I think that's one of the combinations it accepts, right?
We would say, like.
okay, like, these things might have different alignments. Like, one of them might be aligned to root, one of them might be aligned to an attribute, or it might be, like, root and two scalars.
Then we, like, we figure out how to, like.
basically turn them all into, in this case, it's, like, DataFusion has an enum called columnarvalue, where it's, like, it can either be an array or a scalar, and then you just stick those in a VEC and then fire it into, the, in this case, they call it, like, a scalar UDF, but it's essentially, like, a trait that can, like, take Like, some fact of these column or values as arguments, and then it, like… And internally, then it figures out, like, okay, what am I gonna do if one of them's scalar, or two of them scalars, and then… Go slice the strings and stuff.
So it's, but… Anyway, but I'll, I'll look at this too. So you said slice is an interesting one to look at, length… oh yeah, I see there's four of them here. Slice length, and then you said attached and source are kind of less interesting, so the ones that are pulling the data off the, Off the record, record type trait.
**Mike "Blanch" Blanchard** 35:56 If you look at attached and source, you'll see they basically call into the same, like, helper files.
They're pretty much the exact same code, but… They're sort of specific to the engine, but slice and length are… But more interesting from a… from the perspective of, like, okay, let's say now I want to go and… You know, there's 50 other scalers that are missing. I have to go and implement 50, or ask AI to do it.
I'm hoping the code is simple enough where Like, just given one example. Like, using Slice as an example, go implement CONCAT.
Hopefully it's just… Very easy, repetitive work.
Because all the complexity's sort of removed at that point. You just get, like, these couple structures, you have a couple helper methods, like, there's… Given… some slice of… dictionaries or singles, there's, like, a merge helper.
There's a transform into any helper, there's a transform into Boolean helper that the logicals call, and, like, using those three helpers, I was able to implement all this stuff that I needed.
**Albert Lockett** 37:12 Gotcha. Yeah, okay, sweet, I'll take a look at this. Yeah, it doesn't look like slices.
It's only, it's a couple hundred lines.
Not too bad.
**Mike "Blanch" Blanchard** 37:22 It could… it could have been less, you know? Like, if I forced… there are some helpers where you can take, like, a single and spit out a dictionary, but I tried to fast-path, like, common cases where, like.
okay, you have… they're all single values, so I'm just gonna do a quick, like, exactly what record set would do, and just return a single back.
So I tried to capture, like, the common cases with dedicated, like, matches where I could, and then there's always, like, an Uber one where you get, like.
Okay, these are all dictionaries, go… go treat them all as special, that type of pattern.
**Albert Lockett** 38:00 Yeah.
Okay, cool. Yeah, I'll have to… I'll have to read through this.
Cool. But yeah, it's, it's cool to see this, this, this progress. This is, this is sweet.
This is cool.
Hmm… Okay, I think that was, everything I had… Trying to think what else… No, that's everything I had. Oh, I was thinking, Actually, I might, So currently in, in GitHub, we have… this is, like, a very minor thing. Currently in GitHub, we have a label called, like, engine columnar, and that's what I… that's what I have, like.
every time I have, like, an issue, or a tag, or PR, like, for the query engine I'm working on, it comes up as engine columnar. I was thinking I might switch that to be engine OTAP, so it's, like, the columnar engine that's, like, OTAP-specific, so I can leave that engine columnar for, like.
For the engine that you're working on.
So it's amazing.
Okay, cool. Yeah, that's what I'll do, and then I'll start, like… like, as I've been making issues, I've been making them called, like, OTAP, OTAP Query Engine, just because, like, I know that, like, you have this, like, more general thing coming, What else? Stuff to discuss with Mike. I made a list.
**And there's one thing on it, the label thing, so… okay, so… Mike "Blanch" Blanchard** 39:48 We do plan, at some point, to move this out of a branch.
And, like, you know, get the code in the actual repo, and, like, It's a huge no-no.
to drop, like, code bombs, so I'm getting a lot of pressure, like, when are you gonna start putting in your code and blah blah blah? So my plan is, like, I want to prove mutability.
Because that's sort of the other half that's missing. And then once I have, like, these few scalers going, the set there… I think I'll feel pretty good with that, so then what I'll start doing is I'll… I'll start PRing it, you know, in small… as small as I can, little… chunks.
to get it in the repo, and then once it's all there, then I'll start doing, like, normal PRs for things.
it's just… at this point, I consider it more of a proof of concept, where, like, you know, in a weekend, I went and refactored the whole thing.
there's a sweet spot, you know? I don't want to, like, drown everyone in PRs and noise as I'm, like, blowing it up and rebuilding it and changing it all. I need to kind of get it to, like, a happy… I find, especially with arrests, like, lifetimes, especially when you're… when you're in the proof of concept, like, they're so verbose, you know, you have to put them so many places that, like, it's really hard to change them quickly.
So it's… I tell people I love Rust, but I hate to prototype in it.
**Albert Lockett** 41:13 Yeah, I know what you mean.
I know what you mean, yeah. I had the… I had the same thing when I was working on the, the, view abstraction that we use for proto-encoding, and it's a lot of lifetimes in that, and it was the same thing.
But yeah, that sounds good. And, like, I mean, you know, it's clearly, like, like, I know you said you're getting pressure from, like, the… from, like, your team to, like, get it… get it into… into GitHub, like… I'm not… I'm not, like, putting the pressure on, but, like, as you, as you do start in those PRs, like, if you need to, if you need someone to, like, expedite their abuse, like, I can… I can work on it, because, like, I clearly have, like, probably, like.
of the people who are approvers, I mean, I… I mean, it's probably me and Drew that have, like, the most, context, so I can, I can take a look as well.
Alright, thanks.
**Mike "Blanch" Blanchard** 42:10 I'll try to keep them nice and small, and then… That's always a good opportunity.
you know, when I'm doing that, I'll add the test coverage where it's missing, because I haven't been super focused on, like.
Writing all the tests that I should have, so… That's kind of what I did with Record Set.
Record set was a proof of concept.
a totally different proof of concept, and then I redid that proof of concept, and then I started PR-ing it in pieces, and then Drew would review it, we made some changes as it went, and that's kind of how it came to be as well. I'm just kind of following that same process that I did.
**Albert Lockett** 42:49 Makes sense.
**Mike "Blanch" Blanchard** 42:50 This one's a lot better, because… You know, I'm now 2 years into Rust. The original proof of concept was probably a mess compared to this thing.
**Albert Lockett** 43:03 It's, It's, hey, it's always great to be on, like, the upward trajectory when you feel like you're, like, getting better at, adult language, at least that's how I feel.
**Mike "Blanch" Blanchard** 43:16 It's a lot easier now, like, when I do run into, like, a lifetime problem.
I at least know what it's telling me, you know, I know where I messed up and what I need to do, where before I was just like, what?
**Albert Lockett** 43:28 Oh, man, yeah, it's so intimidating when you run into it for the first time, yeah.
**Mike "Blanch" Blanchard** 43:33 And if you look, if you're super, super bored, there's the commit I did, like, Monday, the refactoring. I actually removed a bunch of lifetimes, and… I sort of… you told me weeks ago, like, look at how Arrow's using Arc.
And I had a little bit in that… in there, but I was still kind of holding pointers back to the batch. I was doing a lot of, like, you know, lifetime A meant the record batch.
But then I started mutability, and that was becoming a big problem, so I just… removed all of that, and I just hold… Everything is a arc, or… the buffer itself, the lower level thing, which I think itself has an arc.
But that kind of allowed me to remove all the lifetimes for anything I need from the arrow side, which means, like, when it comes to mutability.
Rust is happy because I'm no longer holding that first batch when I need to mutate it. I just have a structure that has just arcs in it, or buffers, and then I can… I'm free of the lifetime, essentially.
**Albert Lockett** 44:44 Yeah, it's handy, because you can, Because, yeah, you're right, you're free of… you're free of the lifetime, and and the clones are… the clones are cheap, we need to make a clone of it, so… yeah, you're right, that's a… It's a handy clip on the aero side.
**Mike "Blanch" Blanchard** 45:03 And, when I'm in the aerial world, I use ARC because… A lot of times I had no choice, you know, I'm getting a batch in, I only have ARC. Inside the engine, it will, like, create structures where it doesn't really need arc, I don't think, because it's all single-threaded. So you'll see some things where I use, like, RC and not arc.
Because… I think it's just a little faster, you don't need to worry about, like, you know, synchronizing anything, but when it's, like, a purely arrow thing, I just kept it all arc so it's nice and consistent. You'll see some spots where I'm, like, creating a vector of engine types, and I'll store that as an RC instead of an arc.
**Albert Lockett** 45:46 Yeah, I think… and I think that's the right call.
I think that's the right call, like… in, in the OTAP engine, like, we do… We do something, like, super similar.
Where, like, we're passing around, like, these columnar values, which is the data fusion thing that has, like, an arc, like, an arc dyne array in it, but then, like.
the… the stuff we need to do to, like, figure out, like, like, what is the alignment of the data, like, that is in an RSC, for, like, pretty much the exact same reason that you just explained. Just because, like, we… we needed something that was, like, cheap to clone, but, like, We didn't want, excuse me, We didn't want to have an arc, because we didn't need it, basically. It's a threaded thing.
**Mike "Blanch" Blanchard** 46:42 Yeah, I think ARCs are, like.
probably a few nanos slower than RC's.
**Albert Lockett** 46:47 Yeah.
**Mike "Blanch" Blanchard** 46:48 Yeah, it's cool. It's fun.
**Albert Lockett** 46:51 Yeah, man.
**Mike "Blanch" Blanchard** 46:52 Good stuff.
**Albert Lockett** 46:53 Yeah.
Alright.
Mmm… Cool.
Feel free to ping.
**Mike "Blanch" Blanchard** 47:00 Me if you ever need, like.
You know, an explanation about something in this code, or you want me to walk you through something.
For the time being, I'm pretty much dedicated to this. I just met with my manager yesterday, and he's like, bad news, I gotta put you in the on-call rotation, so my life's gonna get a little more boring in the next few weeks, but for now, I'm just kind of heads down on… get this mutation working.
**Albert Lockett** 47:27 Cool. Hey, I guess it, I mean, depends on how, how bad your on-call is, or, you know.
I've been, like, I've been on on-call rotations that are, like, you just don't get paged, and then I've been on on-call rotations that are, like, pager duty is just going all the time, and I find it depends so much on the culture of the team, so hopefully you find a happy medium.
**Mike "Blanch" Blanchard** 47:50 Yeah, fingers crossed, I hear, like.
you know, if you work on, like, one of these Azure services.
you're on call, you're on the phone 24-7 for that week, because, like, Azure's so big, there's an issue somewhere all the time.
**Albert Lockett** 48:09 Jersey.
**Mike "Blanch" Blanchard** 48:10 So I'm hoping to not get, like, there's… There's one team that just does, like, all the agents.
And, like, we… Our team sort of now, we're… we're in the hotel aero world, we're using that, but there's many, many, many other agents for all sorts of pipelines that, like, our greater team owns.
So if they drop me in that queue, I would have no idea what I'm doing. I would… I'd be on some Linux agent I've never looked at before. So I'm hoping they, like, carve me out just as, like, the hotel collector agent queue, but we'll see.
**Albert Lockett** 48:47 That's right, that's what you need. You gotta be specialized, you gotta be niche.
**Mike "Blanch" Blanchard** 48:50 And we're trying to… converge all that stuff, so, like, we're really betting the farm on this open source version, and we're pushing a lot of these agents to, like, you're going away, you're gonna run on OpenTelemetry.
So that's sort of our team's vision, is to, like, get this thing enterprise-ready and start converging and deprecating and get rid of all these agents.
it just kind of works, I guess, in Microsoft, like… I guess traditionally, like, every… big, big team, like Windows, you know, they had telemetry, they built their own telemetry systems. Office had their own complete systems, you know, Xbox had their own complete systems.
And then as things like reorg, they'll go, like, oh, we have all these telemetry systems, let's just, like, throw that under one manager. So all of a sudden, you wake up one day, you have, like, all of these giant things, and you're like, what the heck is all this?
So that's sort of where we're like, we need to… Get on a standard here.
That's go to work.
**Albert Lockett** 49:50 Hey, what's the… Mike "Blanch" Blanchard 49:51 all these telemetry SDKs everywhere. We've pretty much killed all those off in favor of open telemetry SDKs, so that's been a huge success. Now we just need to repeat that process for all the agents.
**Albert Lockett** 50:06 Dude, that's cool.
That's cool to hear about open telemetry. I mean, I think that was always the promise of it, to have, like, one… Unifying standards, so it's just like, you know… all these years later, I mean… It, like, it's just cool to see that, like, coming to fruition, like, or hear about that coming to fruition in a big way inside a big company.
Cause, like, we, like.
like, the last startup I was at, we did something similar where we had, like, a bunch of, like, different telemetry for a bunch of different apps, and we were, like, putting it into open telemetry, but it was, like… that was, like, a startup with, like, 100 people, so it's not really, like, the same scale of migration, but it's.
**Mike "Blanch" Blanchard** 50:50 Yeah, the real pain.
is, like, everybody wraps, so we had all these telemetry SDKs, but, like, nobody ever used them directly. They always used, like, some other team's wrapper around the thing.
So you just… you just get drowned in these, like, issues that, like… I'm like, I don't even know what this is. Like, I've never even heard of this thing. And then they're like, well, you gotta fix it, it's… it's your thing. And it's just, like, tracking down people, and you… you'll run into, like.
some library that, like, nobody even owns is just sitting out there, and it hasn't been touched in years. It's like, oh my god.
Just the company is just so big.
**Albert Lockett** 51:36 Hey, it's, it's always, I don't know.
It's a challenge, but it sounds, I mean, it sounds like you got enough work to do anyway, so I guess that's a mean thing.
**Mike "Blanch" Blanchard** 51:49 That's cool. It's fun.
**Albert Lockett** 51:50 Yeah.
Cool.
Alright, well… Catch you next week, I guess. Alright.
**Mike "Blanch" Blanchard** 51:58 Well, good luck.
**Albert Lockett** 51:59 Yeah, so, I don't know, we're actually… our whole team from F5 is going to be going to, Seattle next week, so… I probably won't be around for this, this SIG call.
**Mike "Blanch" Blanchard** 52:17 Okay.
**Albert Lockett** 52:17 Sounds good.
**Mike "Blanch" Blanchard** 52:18 You're gonna have met more of the team than I have.
**Albert Lockett** 52:22 Yeah.
Yeah, the only one I've met so far in person is Udkarsh, like, who's like a… he's, like, someone involved in Otel Arrow, so yeah, I'm gonna meet, I guess, the rest of the group, probably.
**Mike "Blanch" Blanchard** 52:33 Oh, funny. I went to one OpenTelemetry conference in Austin, like, right after COVID, so I met one guy from Microsoft who was, like, our PM, but then he left the company, so I'm back to not having met anyone.
**Albert Lockett** 52:49 Oh, crazy. So you're, so you're a bit like, like, it's, like, the same situation for me at F5, where I'm, like, the only F5-er in… in the city of Quebec.
So, like, up until last year, when I went down to Seattle for the first time, I didn't know any other people from F5 at all.
**Mike "Blanch" Blanchard** 53:11 Yeah, pretty much everyone on the team is in, you know, the greater Washington area but me.
Actually, I think my manager, he might be in, like, Ohio or something, but he's kinda… he's kinda newer to the team, he just… we had a different manager who had a kid, so he… he was gone for, like, 4 or 6 months or something, so they brought in Dimitri to kind of help manage while the other manager was out, but then they ended up switching, so now Dimitri's gonna be fully involved, so… We'll see what happens if he relocates, I don't know, but… He's cool, I don't know if you've interacted with him yet.
**Albert Lockett** 53:48 No, I haven't. Yeah, maybe I'll… maybe I'll see you.
**Mike "Blanch" Blanchard** 53:51 He'll probably meet him.
**Albert Lockett** 53:52 Yeah.
So I guess that means, I'll catch you in, in 2 weeks.
**Mike "Blanch" Blanchard** 53:58 Good.
**Albert Lockett** 53:59 Alright, cool.
**Mike "Blanch" Blanchard** 54:01 Yeah. Cheers.
**Albert Lockett** 54:02 He said…
