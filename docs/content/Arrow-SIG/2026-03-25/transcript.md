SIG: Arrow SIG
Date: 2026-03-25
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Mike "Blanch" Blanchard** 01:47 Hey, Albert.
**Albert Lockett** 01:48 How's it going?
**Mike "Blanch" Blanchard** 01:49 Good. How about you?
**Albert Lockett** 01:51 Yeah, not bad. Yeah, cool.
Yeah, did you have anything, you wanted to start off with today?
**Mike "Blanch" Blanchard** 02:04 Nothing pressing, I've just been still working on the… Excuse me. On the perf… on my engine…
**Albert Lockett** 02:15 Cool, yeah.
**Mike "Blanch" Blanchard** 02:17 They're really good, some things.
I'm less happy with.
**Albert Lockett** 02:20 Dude, that sounds like the… the classic story of, I don't know, all turf-related stuff, maybe.
Yeah.
Cool.
Yeah, I, like, so, I don't know if, like, is there anything you wanted to dig into there too deeply? I, I didn't, I didn't really have much to, To, discuss this week.
I guess, like, I can give you a quick rundown of what, like, what I'm… what I… what I've done.
So, last week, was working on, like, Attribute, assignment in, in OTAP, or sorry, in the engine that I've been working on. So, like, when you, have some, like, expression you've evaluated and you say, okay, now I'm gonna, like.
evaluate, like, the set transform expression and the source is, an attribute, then it's time to go in and, and, and update those attributes, so… That was… that was pretty much, like, the… the work that I was doing. It's, it's a little bit, like, of a tricky thing to do in OTAP, because, like, I don't know if you've seen how, like… like, actually, you've seen how the attributes work, how we have, like, that type column and the key column, and you've got all the values columns, so you need to, like.
Figure out, like, okay, so this attribute is… is going to this, this… this row, and here's what the… the type of the attribute is, so I need to change the… the, the value in the type column, maybe, and then I need to assign the attribute in the correct row, Or in the correct values column, in that row, and then, and then, possibly null out the, The, the other, columns, for that row, which isn't strictly necessary, but, But, but we do it.
And so, like, the majority of the work that I was doing was, like, sort of, like.
basically, like, writing that kernel and making it go fast. And then, And then from there, like, all the work in the engine is really just, like, lining up the data and invoking that, that helper function, so… That was, so that was what I worked on last week, and then, the only thing I've worked on on the query engine this week has been, like, When we have our conditional, data statements, so, like, that… that data expression that backs, like, the… the if-else expression that we added in OPL, what we do there is we split the… the OTAP batch, based on, like, which rows, Which rows pass, like, the logical expression and the if statement, and then, and then we evaluate the… the data expressions in the branch on each on the split, and then we can cat everything back together at the end. And so, Like, before, when we were concatenating the record batches back together, we were doing some, like, a really naive concatenation, where it was just, like.
Like, just call arrows, like, concat batches, compute kernel, and we actually, like, need to do something a bit smarter, because, If, like, one of the record batches got modified somehow by the transform, like, if, you know, now that we have the ability to assign attributes, like, maybe the schema changed, because before you didn't have an integer attribute, and now you have one, and so now there's an integer column.
So we… we just needed to have, like, a more schema-aware concatenation, And so, we already had that, code written, that it was written for the batch processor, and so it was just, like, plugging that into the calendar query engine, and so, I worked on that earlier in the week, and I think that code is already merged.
And, and yeah, and that's it on the, on the query engine side. The rest of the tasks that I've got going on this week are, are, kind of, like, unrelated to the query engine stuff. It's a few… a few bugs related to OTLP proto-encoding, and… And, and stuff like that. Yeah.
So, that's what I'm working on. Actually, I did, so… I'm happy to answer questions about that. I did have one other thing, too, that, that, Might be worth… mentioning, I can… I can share my screen, and I can show you it, and, like, maybe… maybe this is something that's, like, not interesting to you, or maybe it's… maybe it is interesting and relevant.
I'm gonna share my screen.
**Mike "Blanch" Blanchard** 07:57 Fair enough.
**Albert Lockett** 07:59 So… Is this the issue? No, this isn't the issue. Let me make this big, big… Okay, this is the PR that I had open for this. And again, this isn't, like, strictly related to the query engine, but it, like, kind of is.
So… Basically, like, what can happen when you use the arrow… compute kernels, and of course, like, that's what we're using inside the… the columnar query engine as well.
Just like, just like you are.
Like, if you… If you, like, if you've used the filter, compute kernel on some record batch.
And there are keys that are dictionary encoded, The filter will just, like, it will just filter on the dictionary keys, but it won't actually filter on the dictionary values. And so, you would expect that, like, if I ran, like.
Filter to try to remove, like, One sec here… Okay, anyway, I guess, I guess maybe these examples are a little bit funny, but I guess, like.
Yeah, let me fix the, Let me fix the example here, one sec.
Because the example that I gave in the thing was wrong.
Okay, so I guess, is that right?
Sorry, I forgot. Anyway, I guess, like, the moral of my story, though, is, like, you can end up in a situation where your result looks like this, where you can have, like, a value in your dictionary array, and there's no key that, like, points to it.
And, And I think that, like, they basically do that in the compute kernel for performance reasons, so they don't have to, like, go through and, and, like, remove these, like, orphaned values.
And, you bet.
And… Sorry, did you say something?
**Mike "Blanch" Blanchard** 10:41 It's so interesting.
**Albert Lockett** 10:42 Yeah, and so, like, the reason… the reason that I think, like, this was… this is relevant, is because, like, if someone came along and said, oh, well, I'm gonna try to use, like, the query engine to redact, like, sensitive data, well, it, It, like… like, I guess, like… You'd end up in this… in this… with this, with this array that, like, yeah, like, there's… like, you… like, this is a sensitive value, but there's no key pointing to it, but, like, it's still sitting there in, like, the… in the array, and then so, like, if you did something like, oh, well, now I'm gonna, like, serialize my OTAP badge's arrow IPC and, like, send it out somewhere.
Then your sensitive… then this would end up in the… in the IPC payload, and that's… that's a bummer, because then, like, you… you've sent your sensitive data off to somewhere where maybe you didn't want it.
So… anyway, I guess, like, but, like, what, like, whether that, whether that's something that's important depends on how you're gonna use your query engine, but, so… So, I was trying to fix this, and it actually decided that I wouldn't, like, fix it in the query engine itself. What I added was, like, this post-processing step that sanitizes the, That, like, sanitizes the word we use, that effectively, like, sanitizes all the record batches, and so, you can see that, like, here we've got, like.
sanitize column, if it's a dictionary column, go into it, and then… Go through and, and and figure out, like, all the… all the dictionary values that are orphaned, and take them out and adjust all the keys, and… basically do what you'd expect. So, Anyway, like, I guess, like, the… and then, like, so… so we actually call this in the… in the transform processor, like, after we invoke the query engine to do the transformation, so it's not part of, like, the query engine code itself.
So maybe you're… like, maybe, you know, it's not, like, the most relevant thing to talk about in the query engine, like, sig call that we're doing, but I just figured, like, I'd tell you that, like, this is here, so in case, like, as, like, as you get, like, your instance of your query engine, like, more built out, and someone says, hey, I want to do, like, sensitive value reduction, this is, like.
This kind of concern about these, like, orphan dictionary values is something that, like, you can… like, now you know of, and if you want to use this utility to sanitize them, it's here in the PDA to crate. Does that make sense?
**Mike "Blanch" Blanchard** 13:21 Yeah, totally. Are you defaulting that to false?
**Albert Lockett** 13:27 That is the, That's the question that I've been debating with Laurent today, what, like, whether… where we… where we run this. So I was… I was defaulting the skip to false. So the… this would default to… do this sanitize step. And I think that's the most reasonable, because, like, just, like, someone who didn't know Arrow very well might not even think that, like, this is something that they need to do, and so I think that, like, it's better to err on the side of, like.
**Mike "Blanch" Blanchard** 14:01 Yeah.
**Albert Lockett** 14:01 more secure.
**Mike "Blanch" Blanchard** 14:02 Safe default.
**Albert Lockett** 14:04 Yeah, yeah, yeah, so that was… that was my thinking, but then, like, after talking to the raw, like, there was kind of a question, like, oh, do we even do it in the transform processor, or do we actually do it in the OTAP processor, and where is the security boundary? But, like, I think, you know, regardless of where we land, like, I think, like, in the data flow engine, like, we probably will end up… I would advocate that we would end up, you know, keep, like, doing this by… Doing this by default.
So, I think, you know, the short answer, is this on by default?
Currently, yes, and I don't think that will change, but again, like, this PR is still in review.
**Mike "Blanch" Blanchard** 14:45 Good to know. I was not aware of that arrow behavior.
**Albert Lockett** 14:49 Yeah, I was… Mike "Blanch" Blanchard 14:50 Why it's so fast? Because it's cheating.
**Albert Lockett** 14:54 Yeah, exactly. Exactly. It's like, you tell it to filter out, like, the dictionary array, and it's like, yep, no problem. You hit the keys, filter them out, put the dictionary values back on there, and there you go. And you're like, well, wait a sec, like… I had some extra data hanging in there that I didn't want.
Yeah, so, Anyway, I thought, I thought that was totally weird behavior, but, turn, like, you know, in all my testing, it turns out that's what's happening, I haven't started a thread on this yet. I was gonna, like, post this in the Arrow, Discord, and maybe just ask, like.
**like, what, like, has anyone else ran into this? And, like, like, like, what are you… what are you people doing? Like, maybe, maybe no one cares, but… Mike "Blanch" Blanchard** 15:45 kind of surprising. It's not, like, an option.
**Albert Lockett** 15:49 Yeah.
**Mike "Blanch" Blanchard** 15:49 When you call the filter record batch, or whatever it is.
You can't tell it to, like… You know… Drop values or something.
**Albert Lockett** 16:02 Yeah.
**Mike "Blanch" Blanchard** 16:02 I get why it's hard, and you have to track, you have to, like, go through the keys, and you'd have to track all the values.
**Albert Lockett** 16:11 Yeah.
**Mike "Blanch" Blanchard** 16:11 Just build, like, you know, it's basically like a hash set, or, you know, like your ID bitmap.
It wouldn't be the worst thing in the world, but… They see the challenge.
**Albert Lockett** 16:25 Yeah.
Yeah, it's, and that was the thing, and it, like, I… this… this PR that I did, I tried to make it, like… I didn't spend a huge amount of time optimizing it, but it's… it's definitely, like, something that's, like, not… not free from a performance perspective, right? Like, it has quite a bit of overhead.
**Mike "Blanch" Blanchard** 16:47 Yeah, and if you're not… Dropping anything, or redacting anything, then it's just wasted.
**Albert Lockett** 16:55 Yeah, yeah, exactly, so… That was, And that's… that's, like, the other tricky part about this, too, is I was trying to figure out, like.
You know, like, is there a way that… that I could just be smart about this, and And try to, like, figure out, like, when I need to, when I need to run it, based on, like, inspecting the, the query plan, and that… That doesn't seem like something that is… really trivial. It seems like something that is pretty hard, And so I didn't want to get it wrong, so for now I'm just doing the stupid thing and, like, doing it every time.
And then, obviously, we have this flag that the user can tell us, like, hey, there's nothing sensitive going on, don't do that. But… Yeah, it's pretty tough. And, like, like, especially where, like, you might… you might think, oh, well, the user's just gonna write a query that's, like, you know, filter out all the log records where, like, the, the, the body is this, this string, right? And then we say, oh, well, body's clearly the, the sensitive… feel, I'll do my redaction on that, but, like.
it's tough because, like, the, like, you might end up in a situation where, like, the user knew, like, a priori, oh, well, like, every time the body is this, I have a sensitive value in some other column, and then you're like, shoot, well… Right, so our little heuristic of, like, checking the query plan didn't really work that well. So, that's, like, just to avoid, like, stuff like that, that's why I was like, okay, I'm just gonna do this the… the… the… The stupid way, and just do it every time.
Yeah, so… Anyway, that's, That's my weekly update, all the tasks I've been doing.
**Mike "Blanch" Blanchard** 18:57 I have a random question for you.
**Albert Lockett** 18:59 Sure.
**Mike "Blanch" Blanchard** 19:00 So when you look at, like, the attribute.
Child table, or whatever you want to call it.
Like, it's… it's possible you could have, like, two log records.
Let's say they both have an attribute called Attribute 1.
The first log… log record for attribute 1 could point to a string.
The second one could point to an integer.
You kind of get what I'm saying?
**Albert Lockett** 19:28 Yep. I, yep, I do get what you're saying.
**Mike "Blanch" Blanchard** 19:33 Do you have support for that in your engine?
**Albert Lockett** 19:37 No. Unfortunately not. Yeah, we don't have support for that yet, so.
**Mike "Blanch" Blanchard** 19:47 What would you do? You just see the first one as a string, and then you just pull all values from the string table, child table thingy?
**Albert Lockett** 19:55 Yup, and I think we actually check. So we say, like, like, okay, the user's gonna try to do something with, attribute X, so, like, look at the first one.
Figure out what its type is. And then, like… for the rest of the rows that have attribute X, like, try to make sure that they all have the same type. And if they don't, then, we return an error and say, hey, you, we can't, we can't, execute this.
Which is pretty… which is kind of crappy. And And so I don't have… I don't have the solution for it yet. I mean, like… Yeah, I don't, I don't have the solution for it yet.
one… like, on one side, I was gonna try to see, like, is there a way that we could, like, you know, have some, like… Expression that, like, that you can check to be like, okay, like, is, like… is the value of the attribute, like, this type? And then you could use our, like, conditional data expression to, like, split the batch and say, like, okay, when the value's this type, like.
you know, go down this branch, and when the value's the other type, go down the other branch or something. That could be one solution to it. Or the solution could be, like, you know, make the engine really smart, and then it could say, like.
okay, like, I'm gonna evaluate this expression, I'm gonna figure out the ranges in the attribute record batch where the values are a certain type, and then I'm gonna, like.
evaluate on all those ranges separately, so the result type of my expression will be different for each range, and then, then for, like, each resulting range, they all have different types, I could figure out, like.
what to do with them, depending on, like, what I'm doing with the results of the expression, so… But But yeah, so, so… like, the engine that I've been working on doesn't have support for that yet, but, like, those were two options that I kind of had in mind that I just haven't got around to actually, like, implementing or really doing a lot of investigation on yet.
**Mike "Blanch" Blanchard** 22:19 I have the support in my engine.
Because, you know, it was kind of built to handle that case, because record set does, like, you can have… And records of every individual record.
Can have a completely different schema than… what it saw before, it just doesn't care.
And I also have this little abstraction in between the arrow record and what the engine's running on.
So there's basically, like, an enum You can give… sort of like, I don't know if you've looked at Record Set, but it has these ideas like resolved value, it has these things that get passed around So in my engine, I have, like, a basically resolve table, and you can give it Keys?
And those are all Aero compatible. They're, like.
The dictionary with the arrow key, generic.
So in, like, our case, they're all what? The words? You know, Uint 16s or whatever?
But then when it comes to values, I have an enum.
And you can give different kinds of values. You can give a pointer to something from the record, so like a primitive array that's just a pure arrow structure pulled from the batch.
Or, if you're computing things, you can give it, like, a vector, an array of a different abstraction.
So you can have intermediary types, like regexes and things that Arrow might not necessarily know about, and you can also mix types freely, because you're not You're not locked into an arrow array which has a single type. So it's sort of a non-issue in my engine by design.
The reason I'm asking is, like, I'm running… I took your whole benchmark suite.
And I can run all of those in my engine, and I'm just looking at the results, and most of them are the same, slightly better, slightly worse, but a couple of them yours is, like, 40 microseconds, mine's, like, 60 microseconds. So I've been, like, bearing in on the ones that have a big difference.
And it seems like in one of them, or the one I've been spending a lot of time on.
it's because of that thing, so every time I pull off, you know, an attribute.
I have to look at the types.
Then I have to go and find, okay, the int table, which might be optional, or the string table, and then I have to check if the key is valid, and then I have to pull the value, so I'm just… I'm doing more work per row than you are.
And it's… You know, it looks significant on the benchmark, you know, it's 60 versus 40, but, you know, at the end of the day, it's microseconds.
So I have to decide, like.
it's not exactly apples to apples, now that I know you're not supporting that, so I can say, okay, mine's gonna be a little bit slower, but it has support, some different support characteristics.
So I'm just trying to figure out how much time I should spend toiling on these benchmarks.
**Albert Lockett** 25:34 Yeah, is this the filtering benchmark, or is this the other one where we're assigning attribute values?
**Mike "Blanch" Blanchard** 25:39 This is all filters.
**Albert Lockett** 25:41 Okay, okay, cool. Yeah. Yeah, because we added… Mike "Blanch" Blanchard 25:45 One in particular, where it's like… It's doing, like, code… Line or line number greater than 1,000.
**Albert Lockett** 25:55 what's… Mike "Blanch" Blanchard 25:55 Pulling records, they all have a value, but they all evaluate to false, and then it short-circuits the whole thing.
That's the one particular one I'm looking at, and it's just… my short circuit is fast, but getting the data into the short circuit is taking longer, because I'm just spending more time Building my…
**Albert Lockett** 26:17 Agreed.
**Mike "Blanch" Blanchard** 26:18 clear, if.
**Albert Lockett** 26:19 And for… so, so for the, So, for the filter ones, in particular, Sorry, yeah, I told you something that was, like, maybe, When I was telling you how our, how are, like, how our type… like, resolution works in the expression valuation. I was talking about, like, as we're, like, evaluating, like, arithmetic expressions or things like that. For filtering, for those filtering benchmarks, we actually do something, even a little bit, less sophisticated.
What we do is we, let's say we have, like, the filter expression you mentioned, where it's, like, code.line is greater than 1,000, I think.
we look at that, like, so we look at that binary expression, like, attribute code line number is greater than 1,000, and we say, okay, so the right-hand side is an integer. That means that I'm going to assume that the, the value I'm looking for is in the int column on the left-hand side.
So we… so we don't even, like… We don't even, like, look at the data, we just say, like, like, go, like, go to the attribute record batch, like, look for… look for an int column, and then, like, check if, like, the values in that int column are, are greater than, are greater than 1,000. And I think… I'm pretty sure we actually check that the type column is all integer 2. If we don't, then… We should probably check that, but, But yeah, that's basically what we're doing.
**Mike "Blanch" Blanchard** 28:23 You're cheating.
**Albert Lockett** 28:24 Yeah, yeah.
Do we check the type column? If we don't, we should. Because I guess, like, technically you could… You could, have a non-zero value in that int column that's not null , I forget where that code is.
Yeah, that's… that's what we do. We just basically say, like, what's the thing on the other side of the binary expression?
Oh, it's an int? I know to go look in the int column.
**Mike "Blanch" Blanchard** 29:01 It's good to know.
**Albert Lockett** 29:02 Yeah.
Yeah.
**Mike "Blanch" Blanchard** 29:05 What would you do if the right hand was another table?
**Albert Lockett** 29:10 So, still figuring that out. When we… so, but, like, when we evaluate, So when we evaluate expressions, like, let's say the other side was, like, let's say it was, like, code.lineNumber is greater than, I don't know, let's use a… let's use a different example. Let's say it was, like, attribute X equals to… event name or something, right? So it's a different table.
So, our engine, we know that, event name is a string column.
So then we would do the same thing. We would be able to do that same cheat.
And, in the case where we, in the case where we… don't know the other side.
then we have to do that same thing that I talked about before. You gotta do… You gotta evaluate it.
I think currently our engine would probably do the, the thing that we said before, where you usually look at the first value, and then check if they're all the same. If they're not, then, than… than error. If they are, then… Then treat the, treat the, On the other side is that type.
And then you know which type to get from the attribute column when you go to check, like, the… the… The equals, or the greater than expression.
**So it's like… Mike "Blanch" Blanchard** 31:04 Dough.
**Albert Lockett** 31:06 Yeah.
So it's like, we would… the short answer is we would try and cheat as much as we can, but in the case where we, like, don't know, like, when the other side is some dynamic type, then yeah, then we have to go, like, evaluate the other side, figure out what the type was, and then… And then, you, like, you can't, you can't check it statically, basically.
But, but we don't.
we don't have support for that kind of filtering yet. So I was gonna, that's probably something that I'll have to do in, Either later in April or in May, basically.
Currently, you can only do, like, like… Is this column, like, greater than, equal to, not equal to, like, a static, static literal?
**Mike "Blanch" Blanchard** 32:03 I have support in line for, like, You can do table-to-table… In selection and filtering.
But I haven't… I haven't gone deep in the perf on that yet, because you don't have comparable benchmarks, but I have some code written.
But it's easier for me because, if you remember.
I sort of normalize all the tables, so… If you did, like, severity text to attributes, name. Just some random thing.
The severity text, which comes off the root table, you know, has a row for every log record.
But the attributes have the funky structure where they're referenced by, like, parent ID, so you always have to sort of, like, massage them.
So I do that all in selection.
So, if you took severity text table, and then you got a table back from the attribute's name.
the name table comes transformed as though it came off the root, so you have… the keys are no longer by parent ID, they're actually by the record.
So you can easily… Take those two tables and do things with them, like select one from the other, filter them against each other, because they're just… they always have the same number of rows, and, you know.
Index 0 in severity text table and attributes name table is going to refer to the same record, if that makes sense.
**Albert Lockett** 33:43 Yeah, yeah, it does make sense. So, Yeah, it does make sense. And so, like, when, like.
In the engine number, when we, like, when we evaluate expressions, like, so we don't do that, like, that, what did you call it? Normalization?
We don't do that up front.
we kind of, like, do it dynamically as, as we're going along. So, for example, like, in our… Like… When we evaluate an expression, let's say it's, like, an arithmetic expression or something, We build, like, an expression tree, You know, so you'd have, like, your binary expression with plus at the top, and you have your left and your right.
And in our planning, we keep track of, like… Okay, like, this… this particular, like, segment of the tree, is going to be relative to this record batch, and this particular segment of the tree is going to be relevant to, like, this… like, relative to this other record batch.
And then when we get to a point where it's, like, a binary expression where you have, like.
one side has a different, like, data, like, layout, effectively, than the other side, that's when we do the join. And so we have, like, joins going, like, like, from root to attribute, or attribute, attribute, to other attribute with, like, a different key, or we have, like, resource attribute to scope attribute.
And so, that's, so, so I think it's something similar, but, like, we… We kind of, like, do it, Do it on the fly.
As the expression evaluates, as opposed to, like, doing it all up front, and then just, like, having the expression evaluate, assuming that, like, everything is the same.
like, like, the same length and the same order, for every step.
**Mike "Blanch" Blanchard** 36:08 Yeah, sounds complicated.
The one nice thing about the way that I have it set up is, like.
Well, first of all, it was a necessity, because… what the OPTAP has done with the attributes thing is not like… it's not like a standard arrow concept, right? It's like… how do we get OpenTelemetry represented efficiently inside of Arrow?
So I needed a way to, like, generalize All of that.
Stuff.
So I have, in my engine.
There's only one type of table that you can give back, and it's up to… Whoever's implementing it.
Doing that work with the abstraction.
to figure out what they need to do. So I've taken all that open telemetry logic and put it in, like, my OTAP bridge project.
But what's cool about it is, like, it just makes… It makes all the other code… Simple.
Because you're only ever operating on, like, one of four scenarios. You're either comparing, like, two scalars, a scalar to a table.
Left table, right scalar, or left and right, or both tables.
So you just have to cover those cases And a lot of the times, there's, like, an arrow compute thing already sitting there, so it's kind of simple. So I'm hoping to gain a lot of velocity implementing Things in the engine.
with that abstraction. I haven't proved that out yet, but… It's costing a little bit more up front.
So I'm… mentally… Kind of going back and forth off.
Should I make that a real… normalization, or should I do, like, a… some kind of structure that, like, gives you an API where you can just say, give me record 0, give me record 1, and it's, you know, in flight doing that translation. I'm not sure, I haven't decided yet. I thought the performance would be really great this way, but you can get yourself in a situation where Like, let's say that code, or the line number attributes query. Let's say you have, you know, 8,000 log records, but only, like, 2 of them have the value.
So what you get is a table with 8,000 rows, because you're going to get a row for every log record, but only 2 of them have values, so you still need to, like, loop and check 8,000 things when it really knew, oh, there were only 2.
So there's… There's a downside to it.
I have to decide if it's… It's just, I gotta put the trade-off somewhere.
**Albert Lockett** 39:00 Yeah.
**Mike "Blanch" Blanchard** 39:02 I might try to do some kind of, like, virtual table… I don't know It's been interesting getting really deep in the perf on stuff, because, like.
There's just a lot of things that go on these, like, these operations, like building a null buffer.
Like, it's… you gotta be really intentional, like, it's really simple code, just as you're looping through the data, just push true, push false, push true, push false.
That's super slow. So then I was just doing, okay, let me just allocate The entire null buffer as false.
And then I'll push the trues when I see them. But then you're sort of doing this random access, so you're getting all these bound checks and CPU things, and I'm like, oh man, it's tricky to do it, like, hyper-performant.
**Albert Lockett** 39:57 Yeah, hey man, no kidding.
**Mike "Blanch" Blanchard** 39:59 Especially in the case of the attributes table, so I… if I'm… if I have a table already, like, let's say I go and I pull that, like, line number table.
And then I want to run, like, where greater than 1,000.
That's pretty easy for me to do, because it's already normalized. I can just… rip through it. But when I'm building that initial table.
The structure of the attributes table is so weird, where, like.
You have, what is it, attribute keys.
And then you could have 3 rows that all represent the first log record, or parent ID 0. And then you could have, like, 4 more records that all associate to parent ID 1.
but those parent IDs aren't necessarily sequential in the root, so it's like, it's sort of forcing me into random access It's pretty structured… In the real world, I think.
You'll get pretty close to, like, everything's gonna be in order.
But, like, there's nothing that guarantees that, either. Like, you could get somebody, some client that's building you records, and they got the order messed up, and, like, there's nothing wrong with that, but it forces me to be defensive and make sure that, like… like, I can't just kind of cheat that all IDs and parent IDs will be increasing.
you know, monotonic, I guess you could say. So, it's just… it's interesting.
**Albert Lockett** 41:34 Yeah, yeah, that's the… that's the really hard part.
And yeah, it's like, as… I feel like I go through, like, some of the same stuff, not just in the query engine, but in, like, a lot of… a lot of places where Like… It'd be nice if we could assume that the parent IDs were increasing, but, like, the fact of the matter is, like… It's, we… we can't really, because you're right, like, you could have a… an evil client, or… Through some kind of transformation, you could get them out of order.
And, the other thing is, when we, when we… Transmit the data?
We sort it in a way that, makes it, like, so it compresses really well, but it, like, completely jumbles up the row order. Like… We, we, we actually end up… we sort by, first by type, and then by key, and then by value, and then by parent ID. So it's like, if you got, a record batch that, like, came from the OTAP receiver, which would… which… which presumably the OTAP exporter is what sent it to that receiver, which means that, like, now the… you received it in this transport, optimized sort order.
the, the parent IDs are gonna be, like, for a given, For a given, The parent IDs for, like, a given log record are gonna be basically all over the batch.
**Right? But if… Mike "Blanch" Blanchard** 43:29 Well, it's good to know my…
**Albert Lockett** 43:31 can, like.
**Mike "Blanch" Blanchard** 43:32 Defensive code won't be wasted.
**Albert Lockett** 43:35 Oh, exactly, yeah, yeah, but then, like, then, like, conversely, when we convert OTLP to OTOP… then, like, just by pure hazard, the parent IDs will be sorted, or the attribute will be sorted by parent ID, so… Yeah, so it's… no, you're good to be… you're right to be, defensive on the… on that side, for sure.
**Mike "Blanch" Blanchard** 44:09 Is there anything in, like… So in the arrow… Code, you know, there's primitive arrays, and then there's dictionaries.
The dictionaries are kind of weird, because you have the keys.
And they can have the null buffer thing.
And then they have values… And you can have a non- null key, like it's set as non- null in the buffer, and then you get the value… it could be null in the value, because it also has a null buffer. I think the expectation is you wouldn't have null s in there, but you still have to kind of deal with them in the code.
Have you done anything in that area? Do you just respect that you may actually end up with a null , even though the key says you should have a value?
**Albert Lockett** 45:00 I think we just… defer to… I'm actually, I'm actually dealing with that right now, so, I'm actually dealing with that, right now, and I did notice that, the, like, in, in, in Arrow, You can have a, You have, like, your dictionary array, and then you can do a thing like downcast dict, so you get it into something called a type dictionary array, where you can treat it like a, Just treat it like a native array.
And so the reason… the reason I, the reason I say that is because I thought that if the key wasn't null , but it pointed to a value that was null , then we're supposed to treat the row like it was null .
But the typed dictionary… Array, or whatever they call it.
doesn't do that.
And so… So, I actually don't know what the answer is, and I've been trying… I've been trying to figure that out. I was trying to figure that out before the call, so, I'll, I'll let you know, cause, Because, yeah, I think, like, for the purposes of, like, Like, comparing… comparing that value and stuff, We were just, we were just, like… Basically, like, throwing it into the compute kernel and, and saying, letting the compute kernel… deal with it.
And, and same thing, like, when we… like, if we need to ever, like, expand the dictionary to, like, a native type to, like, do something, like, arithmetic, we were just throwing it into the cast kernel and letting Arrow deal with it, and so, So I actually don't know, what the, what exactly the right way to deal with it is.
Although, as I say this, and I'm talking to you.
I've also been trying to read the documentation.
And it says, note that a dictionary is permitted to contain duplicate values or null s.
The null count… Okay, let me see here.
It says, note that a dictionary is permitted to contain duplicate values or null s. The null count of such arrays is only dictated by the validity bitmap of the indices, irrespective of any null s in the values dictionary.
News.
**Mike "Blanch" Blanchard** 48:03 It's super weird. There's this whole concept of, like, logical…
**Albert Lockett** 48:11 Yeah. It's like… Mike "Blanch" Blanchard 48:13 The null buffer thing is, like, it's suggestive.
But it's actually really hard. I had to unit test this case, and if you use, like, the… Dictionary builder arrow things.
It doesn't allow you to have a non- null key with a null value. In order to even create that situation, you have to, like, manually construct the things and hand them, like, the, here's the value, or here's the buffer behind it. I can kind of… I'll try to dig up my unit test code and send it to you if you want to see, but it is… it is possible.
But it seems more like a quirk of the code and the API than… What was really intended?
**Albert Lockett** 48:56 Yeah.
And I would say that, like.
like, I think at least in OTAP, we try to avoid doing that.
We try to avoid, like, constructing those as much as possible.
I mean, clearly, like, like you said, there's nothing stopping an evil client from going ahead and deciding he's gonna build his.
**Mike "Blanch" Blanchard** 49:22 Yeah, that's the problem.
**Albert Lockett** 49:24 This thing… Mike "Blanch" Blanchard 49:25 test it using, like, the P data.
like, I create an OTLP message that has, like, you know, an attribute with, like, a null .
when I get the arrow back.
it's done the correct thing. It's removed that and just flipped the null bit.
Handles it appropriately, but… If I manually cook something, I'm able to, like, manifest it, like, oh, this is… this could happen.
**Albert Lockett** 49:54 Yeah.
Yeah, no, I know what you mean, and so I guess, like, the… The moral of the story there is, I guess, like, the only thing I can say for certain is that… I don't have, like, a blanket rule for how I deal with it.
**Mike "Blanch" Blanchard** 50:17 It sucks, it's like, it's not… It's pretty easy code to write.
It's just slope, because anytime you want to look at something, you have to go check, okay, is the key null ? No. Okay, what's the value index? Then you go to the values, and you say, okay, is this null ? No. Okay, I can pull the value.
You're just doing a… Couple extra array lookups.
Let's just add… Add time to everything.
**Albert Lockett** 50:47 Yeah, yeah, exactly, and like, and, yeah.
And what's, what's kind of… Weird… Oh, never mind.
Nevermind.
I was gonna say something that wasn't true, so I won't say anything.
Yeah.
I don't know. I mean, geez, it'd be nice if we could just say, hey, you know what, if you've given us null s in your… If you've given us null s in your… Dictionary values. We're just gonna treat them as non- null s, and you should have made the keys null .
I don't think that's super unreasonable.
**Mike "Blanch" Blanchard** 51:38 I… I'd have to go double-check, but… If you don't code properly by checking first, You wouldn't know… Because if you call, like, getValue… it's gonna give you back a value. It's just gonna be default, so if it's, like, an integer, you'll just get 0 back, presumably. It's kind of undefined, but… Because the values come from some, like, contiguous byte array at the end of the day.
You'll get back, you know, whatever the… Representative thing is for a zero range of bytes.
Which might be okay.
It's just, if you want to do proper, you know, you're doing, like.
a null comparison. You want to do, like, an is null .
Maybe you would end up with a different result.
Just something to think about.
**Albert Lockett** 52:39 Yeah, yup.
Yeah.
Hell yeah.
Oh, lots of things to think about, I'll tell ya.
**Mike "Blanch" Blanchard** 53:00 Alright, I'll stop.
I thought maybe your head hurt.
**Albert Lockett** 53:05 That's all good.
Hey, man. Look, I get a jet, this is cool. Love to… Was it… I'm interested to see, the, the engine that you're working on. I know you showed me a few bits of the code, but Anyway, if you ever have, like, a draft PR you want me to have a look at, happy to… Happy to get some eyes on it.
**I think I'm still pretty far away from, like… Mike "Blanch" Blanchard** 53:36 I still want to tackle… like, all I've done is filtering.
I want to do some kind of mutation, like an extend operation, because that's just, like, completely different.
I want to figure out that that will fit in this model. Once I can kind of mutate and filter.
I'll probably start PRing stuff, but I can… I kind of… my code's kind of a mess right now, because I've been perf-hacking everything, but in the next… days or weeks, I'll get this branch somewhere where you can look at it.
**Albert Lockett** 54:09 Cool, yeah, sounds good. Sounds good. Yeah, I know how, that can go when you're hacking away at perf, how it kind of… Makes the code look like a crazy person.
**Mike "Blanch" Blanchard** 54:20 notepad windows open with, like, bits of code.
**Albert Lockett** 54:24 Yeah, I know, exactly.
dive in.
Cool.
**Mike "Blanch" Blanchard** 54:31 Take care, I'll talk to you next week.
**Albert Lockett** 54:33 See you next week. Have a good one. Bye.
