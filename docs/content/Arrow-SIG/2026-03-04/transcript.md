SIG: Arrow SIG
Date: 2026-03-04
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 00:27 You're like…
**Mike "Blanch" Blanchard** 00:29 Hey, Albert.
**Albert Lockett** 00:31 How's it going?
**Mike "Blanch" Blanchard** 00:32 Good.
**Albert Lockett** 00:33 Cool.
**Mike "Blanch" Blanchard** 00:36 Sorry.
Been doing some PR, so you're back working on things.
**Albert Lockett** 00:41 Yeah, yeah, exactly.
Yeah, I can give a… I can give a little update about what I've been working on. Let me just, Open up the, meeting notes here before I forget.
Let's put in a little new section… For today, it's see… oops.
Today's the merch… 4th… That's 4.30 my time, so that's 1.30 Eastern Pacific.
Okay, there we go.
Yeah, so, yeah, I've been back working on the, query engine and the, the OPL parser a little bit.
So, one thing that we want to do with this in the next few months is have some kind of ability to, do attribute reduction.
And so, you could imagine that you might want to write some… some OPL program that's like, hey, go… go look for attributes that, that have, I don't know, a name or a value that matches some regex, or something, or a key that matches some regex, or whatever. And then, and then… and then change the value, or, like, drop that attribute, or… and the change value could be something like, hey, you know what, I need to evaluate an expression, like, maybe I… take the first letter and then replace the rest of the attribute value with a bunch of stars, or maybe I execute a function that computes the hash of the value or something, right, to mask it.
And so I've been working on a few PRs for the columnar crane engine to try to support that. So the first one was, Sort of, like, a form of… expression evaluation. The idea was, like.
we would basically, like, take our expression AST, and then try to build up, a data fusion plan with it, and then go… or data fusion, I guess in this case, an expression, and then go… and then go execute that expression.
And that's obviously a little bit tricky, where, like, in Data Fusion, it expects, like, the input to an expression to be, like, one record batch, and what we have is an OTAP batch that, like, the data is spread across multiple batches, so what I do when I build up the expression tree is they're, like.
we have these higher-level notes that represent, like, here's a segment of the tree that's all executing on essentially the same record batch, and then when I get to maybe a binary expression that, like, has to join from a different segment of the tree. It, like, joins the data together transparently using the parent ID child relationship, and then that's how it… that's how it executes the, Expressions, and then it… and it also tries to, like, keep track of the types and things while it's doing that, so… That was the first PR that I landed, and then the next PR was to, Take the results of those expressions and be able to assign them to a column in, in OTAP. So, for example, you could write an expression that, like, computes some number, using, like, scalars or arithmetic or whatever, and then you could assign that to severity number, but, like, you know, it also does, like, type checking to make sure that, like, You don't try and assign that to a string column, or you don't try to, assign, like, a null … a result with a bunch of null values to, like, a non- null able column, and so that was the second PR. And then, The third… PR that I have open related to this this week is kind of a… Kind of a weird one, but… what I wanted to have was the ability to treat like, basically, like, in OPL and KQL, yes, like, we have this, like, or at least in the column require engine, we have this, like, pipeline that has a bunch of stages, and each one is… taking a stream of logs or traces or metrics. And what I wanted to have was the ability to say, hey, instead of taking, like, logs or… or traces, or spans, I mean, as the… as, like, the element of that stream that's, like, flowing through your… your program, I wanted to… make that attributes. And so then, like, like, in OPL, you can write a program, and you can do it in KQL, too, where it's like, You've got your logs, and then you get a pipe operator, and then you say where some field is equal to some other field, and some logical expression that operates on the logs.
And then based on that, you could do something with the data, you could drop it or something, or… and, so what I wanted to do was that same thing on… attributes. Actually, I'll share my screen and I can talk about this.
so this is the PR I just got opened a few minutes ago, about an hour ago. And so what I added here was this in OPL, this, new operator called apply, and then you give it the identifier of the attributes that you want to apply the pipeline to, and then under this, you've got, all your pipeline stages.
But each one is… instead of operating on logs, it operates on attributes, and now you've got the attribute fields, like key and value. And of course, if you needed to, you could put in, like, other pipeline stages, like… I don't know, set value… equals… X or something like that, right? So, that was the idea. So… and then, Yeah, and so this was the third PR that I had opened. I just opened this about an hour ago.
This one is… is… Probably the one that, Of the three, that would maybe be, like, the… The one that, like… I think, like, isn't… isn't necessarily just contained to the, to the columnar query engine crate, because I did have to add a new expression, type to support this, so if I go to… data expressions here, I added a new, data expression type.
Called nested data expression.
And then inside this, It just has, The… A source, and then a bunch of, like, children, data expressions.
And so, yeah, there's a new data expression. Not sure if that's kosher, if that's okay, but, that's what I did.
Anyway, yeah, so that's, That's the PRs I've got open this week. Any, Any questions, or comments, or feedback on any of that, or anything you want me to dive into deeper?
**Mike "Blanch" Blanchard** 08:37 I was just thinking about this nested, so I did a… I did a proof of concept when I first started this.
And I had this feature in there, so you could take an array Or a map.
And then… Do things to it, and it would give you… In the case of the array, it had a way to get the index and the value, and for maps, you could get the key or the value.
Trying to remember how I put it in the tree.
I'll go try to dig that up and just refresh myself.
So I don't have an issue with… The idea, or the feature.
I don't know if I love the nested name, but…
**Albert Lockett** 09:24 Yeah, that's… and that's… that's why I wanted to chat with… like, chat with you about it, because, like, I… that was… that was, like, the thing that was, like, the most unclear to me as I was working through this, was, like.
You know, what would be, like, the best way to fit this into, the, the… expression tree, and I thought that, like, I thought that making it a data expression, Could be the right way to go, just because, like, we also have our conditional data expression, which also has, like, as one of its fields, like.
lists of child data expressions, so I thought, you know, that pattern is not so unclear, or not so… it's not like we're, like, doing a whole new pattern, a whole new thing for this. But yeah, like, the… the term… the term nested, I'm not, I'm definitely not tied to, you know, we could… call it, inner data expressions, or, or, or, I don't know, naming is tough. If you can think of a better name.
I'm… I'm totally open to it.
**Mike "Blanch" Blanchard** 10:43 Yeah, let me go dig up what I did and see if I can refresh myself on… were there any lessons there, but… I'm sure we can figure out somewhere to stick it.
**Albert Lockett** 10:54 Okay.
Yeah, sounds good. Yeah, let me know.
if I… if you have it, if you have it handy, like, I'm happy to look at it now, if you, but, like, if… if it's… if it's buried somewhere and you want to send it…
**Mike "Blanch" Blanchard** 11:10 First task is to figure out where I put that proof of concept.
It's probably in my fork somewhere.
It might even be local, I don't even know if I checked it in, but I have it.
See if I can dig it up.
Yeah, it gets… Because the reason you would put it in a scalar is, like, let's say you were doing, like, an extend.
Say, if you wanted to set a field like attributes.
I don't know, this is a bad example, but… Let's say you wanted to, like, set… take the attributes, Only keep the… what was the example? You had the Kates… key values, and set it as body. You want to do something ridiculous like that.
So what you need to do in that case is you have to use the transformation data expression.
And the set. And then you'd have to use a scalar to do the computation.
So you'd take attributes, you'd feed it in, you'd do all the modification. It would essentially hand you back a copy, which you could then set.
as body.
So that's… that's the reason you'd want to put it as a scalar, because then you could pass the results into Anything, essentially.
But putting… beta expression… Then you can get… You can mutate the thing you're modifying.
So, it could be possible we need a similar feature in both.
That's the kind of challenge with the scalers, is they always return something immutable. They don't mutate anything.
So, doing something like filtering elements from a map, or, you know, reducing an array.
If you do them as scalars, and you're introducing a lot of buffering and copying.
So, I did have this a couple places in my proof of concept. Like, I had these scalar operations, but there was, like, a more purpose-built mutating version of them, just kind of like where we have the… the map reduce features.
So I'm not… I'm not opposed to it, I just… I just want to go dig up what I did and see if there were any… Any…
**Albert Lockett** 13:40 Yeah.
**Mike "Blanch" Blanchard** 13:40 used to it.
**Albert Lockett** 13:45 Yeah, interesting. Yeah, yeah, it'd be, like, definitely good to incorporate those learnings.
**Mike "Blanch" Blanchard** 13:52 Yeah, in this case, I guess, like, what I'm trying to do is…
**Albert Lockett** 13:55 Like, treat the, treat this, like, thing that attributes, like, which is a map.
Essentially, as, like, a, sort of a list of… Key-value pairs… And then, like, each element…
**Mike "Blanch" Blanchard** 14:22 Your change, where you introduced the…
**Albert Lockett** 14:25 The data expression.
Oh, yeah, sorry, let me, sorry, I was looking at the… yeah, let me, back out this change to the PR description.
Yeah, here, and I'll go to, go to unified view, so it's just easier to look at. So it's here.
So we've got…
**Mike "Blanch" Blanchard** 14:47 The… the target should not be a source Scalar expression.
That should be a mutable value expression.
**Albert Lockett** 14:57 Oh, okay.
**Mike "Blanch" Blanchard** 14:59 That's an easy change.
**Albert Lockett** 15:01 Yeah.
Okay, I'll just… To-do… Right, okay, add single comment… Yeah, cause… and then in, immutable… Value expression, we can still get a… Oh, we just saw it. What's an immutable value expression?
Sorry, I'm just… this is for my own edification here. We've got our source… okay, and then there's a source inside it, gotcha, okay.
Alright, yeah, that's an easy change.
And then, sorry, did you want to, do you want to keep scrolling down here? Or.
**Mike "Blanch" Blanchard** 16:05 That's the main thing I wanted to tell you, just at first.
**Albert Lockett** 16:09 Okay.
**Mike "Blanch" Blanchard** 16:10 And maybe we'll just change the name, or see if we can come up with something.
Like, could it be… Like, it is essentially a transformation. Could we put it under a transform data expression somehow?
**Albert Lockett** 16:34 So we have… yeah, that's interesting, so…
**Mike "Blanch" Blanchard** 16:38 It is kind of like… Or you might even be able to use, like, for your simple examples, where you're… doing regex expressions. If you look at the remove map keys.
I think you could use regex there. It might already kind of do what you need for at least your… what you have on the… That's great.
**Albert Lockett** 17:00 The… the thing of it is, though, is, like, this is… this is kind of a simple example, but, like, I was picturing that this, like, would eventually become, like, like, a lot more flexible and a lot more complicated. Like, for example.
one of the use cases I had was something like, let's say I wanted to… it's like, okay, if the… if the value has, like, such and such a thing in it, then, then maybe you want to, like, change the value. So in this case, it would be, like, you'd want to do something like if… value… You know, maybe… Value matches, masterCard… I don't know.
**Mike "Blanch" Blanchard** 17:51 Yeah.
**Albert Lockett** 17:52 Or… dot dot dot, then, setValue equals hash value.
Or stuff like this, right? Like, basically, I wanted to, like, build, like, this, have the ability to, like, build this… this whole pipeline that's, like, just operating on, a set of values.
**Mike "Blanch" Blanchard** 18:20 it sort of feels almost like what I have for user-defined functions. So if you look at what I did for user-defined functions.
You can pass in scalars, which are passed by copy and are always immutable, but you can also pass in immutable things, so you could pass in source.attributes.
And then you just get the map in your user-defined function, and you can… You can go wild on it. You'll just get a mutable copy, and anything will just be reflected back.
**Albert Lockett** 18:55 Yeah, so do your users, like, write the user-defined function in… in KQL, or is it, like, a UDF that's, like, written in Rust, and then it gets bound to, it gets banned to, like, some… some UDF, Call that happens in the program.
**Mike "Blanch" Blanchard** 19:19 You can do either. So you can have functions that are just fully part of the query, or when you're building up your parser, you can, like, define functions and their signatures, and then in the record set engine, you can bind them to some Rust callback.
So we give two options, like, we can let users right now, they can just kind of do simplish things in their query, but we have some partners that want to build, like.
You know, they want to give users the tool and the query, and then they're going to say, here are some named functions that we've provided for you that do things they need, like DNS lookup.
Which we were never going to support, you know, natively, but what we allowed them to do is, like, okay, you can define DNS lookup, it takes a string, and then it will just call back some Rust method, and you can go implement it however you want.
**Albert Lockett** 20:15 Yeah.
Okay.
**Mike "Blanch" Blanchard** 20:18 So, what I was thinking, just viewing, like, what you're typing here, like, I'm not saying in OPL you necessarily need to introduce user-defined functions, but… You could, when you parse what's on the screen.
You could just take that body.
and rewrite it so it's effectively defining a function and then calling it. And it would basically do the same thing. I don't know, go… Just to poke around, see what's in there.
**Albert Lockett** 20:45 Trying to find the… The UDF… Function tree.
**Mike "Blanch" Blanchard** 20:54 You go to Pipeline Expression.
**Albert Lockett** 20:58 right here…
**Mike "Blanch" Blanchard** 21:00 See, there's functions.
**Albert Lockett** 21:02 Oh, right here, okay, pipeline function… And then inside this, we've got… Implement pipeline function implementation, pipeline function expression… Okay, then we've got a transform expression and a scalar expression.
And that was a… hold on, where was I?
lifelines… Okay, pipeline… hold on here, pipeline… Okay, and then… oh, and then implementation is… okay, the implementation has a VEC of… Expressions that could be transformed .
**Mike "Blanch" Blanchard** 21:51 It's just…
**Albert Lockett** 21:51 screw it.
**Mike "Blanch" Blanchard** 21:52 Now, this is what I have right now, so if you needed, like, conditional, like, I expect that list to grow, but I just did, like, what was minimal.
the main thing I needed when I worked on it was the external features. I didn't spend a lot of time building out the… What you can express via query, but you can go wild in there if you need more stuff.
**Albert Lockett** 22:16 Oh, this is… okay, this is super interesting. Yeah, so, if I go back to that, that data expression that I had, Where is it? Oh, it's here. And then I go back to Pipeline Expressions, wherever that was. Where was it?
Oh, my God, I don't know how to use VS Code.
pipeline expression. So I could… oh, so you're saying that I could do… I could do something like… this… And then I could… parse my… I could parse my… It's a pipeline function… Pipeline function… pipeline function implementation… yeah, so I could parse my, .
**Mike "Blanch" Blanchard** 23:23 Basically, what you have is the nested body.
**Albert Lockett** 23:25 Yeah, yeah, yeah, yeah. What I have is a nested body. I could parse that into a pipeline, Into a pipeline function implementation.
And then I just need… okay, and… oh, okay, okay, okay, and then, Okay, and then… yeah, so then that could work.
I'd have to figure out how to get that to work with my… OPL… Purse… Sir… okay, so how does, Okay, so I've got… okay, hold on, so I've got my, so let's say I have my, my, my, my pipeline here.
How does that function get… calls, so usually my pipelines are just running over a bunch of data expressions.
So, is there, like, a data expression that has, like, a func… a pipeline function invocation or something?
**Mike "Blanch" Blanchard** 24:27 Should be a scalar. If you don't look at the scalar list, there should be, like, invoke function.
**Albert Lockett** 24:33 Okay, okay, so, Scaler… Where do I find that? Scalar expressions? Okay, and then there's an… Invoke… Oh, there's got… it's gotta be in here somewhere, function… invoke fun… okay, invoke function expression… in function ID… Okay.
Okay, so then, okay, that's interesting. So then this… This… so this expression, then, would get parsed to, like, a, to, like, a set… Attributes… it's like a set, set transform expression.
the dust… is attributes… And the source is a scalar… Scalar, expert, invoke… Function, and then it has, like, a rep to that function.
Yeah, jeez, that's, that could… that could work.
That could… that could work, and then it stops us from having to stick Yet another of one of, Yet another 1 of data expression on this thing. Yeah, I think…
**Mike "Blanch" Blanchard** 26:15 Well, it accomplished a few things, too, because you'd… I don't know what your… End goal is, but if you are ever gonna support functions.
This kind of gives you a two… two birds, one stone type of thing, where, like, you can lay some groundwork.
**Albert Lockett** 26:32 Yeah.
Yep. Okay. Yeah, that sounds… that sounds good. That sounds… I like that. I like that… I like that, solution a lot better. And, so if you're, like… I, and I think… I think the… so, the only… modifications, then, that I would end up making to the expression tree for this would be to stick Conditional and discard expression on the pipeline function expression.
Enum here. Is that… and you said that's probably okay?
**Mike "Blanch" Blanchard** 27:09 Yeah, it seems reasonable.
**Albert Lockett** 27:11 Okay.
**Mike "Blanch" Blanchard** 27:11 You may to… Let me… Megato for one, so, yeah.
Just clearing some junk off my screen.
Windows, Windows, come on, come on. Let me see if I can… articulate this… So… Gosh.
Alright, I'm gonna steal the screen first, then.
**Albert Lockett** 27:54 Yes.
**Mike "Blanch" Blanchard** 27:55 Oh, I'll just stop sharing.
They just told me I'm not allowed to steal.
**Albert Lockett** 27:59 Oh, do you wanna… do you… wrong.
**Mike "Blanch" Blanchard** 28:03 I got it now. I'm good.
So what you were just kind of showing where you were saying you were going to do it as a set transformation with a target.
Tributes, and then… function, whatever.
This will kind of put you into that scalar trap where you're gonna get copies.
What you may want to do… is due kind of what I was hinting at, is, like, there just may need to be some duplication in these things, where, like, on… data expression, you may want to just do an invoke function.
here… Something like this, so you can just do it right at the root.
So what I would expect to see is something like, so you had source… How does it apply?
attributes… oh boy, attributes. And then you have, you know, the bodies here, something like that.
**Albert Lockett** 29:06 Huh.
**Mike "Blanch" Blanchard** 29:07 So, whatever.
But the kind of thing in my mind is you define function, you know, some unspeakable name.
And that gets the body.
And then you rewrite that as a, you know, it's called an invoke function.
Man, my typing is way off today.
Something like this… Computer is not good either. So your actual… so you have, like, pipeline, expression… It has data, expressions, whatever, and then you'll have something To launch that guide.
And then this is gonna be some struct. You might need to… This is specific to a scaler, you might need A different one, because… That might actually work fine, I don't know.
We'll cross that bridge, but… So what this thing is gonna do now is… It wants arguments… Yeah, you can get it mutable, so that's where the money comes in. So you'll do, like… Invoke… And when you define this thing, it's going to give you an ID back for it, so that'll be, like, function 0. So you'll say, I want to kick off function ID 0… Arguments are gonna be, in your case.
Sustainable, value, expression, source… you know, attributes. Just pass in that whole table or map.
And then you're pretty good. So it'll effectively be invoked as… You'll see there's another expression on… Scalar, scalar, scalar, scalar, scalar expression.
I'm doing the same thing you were doing.
So what we looked at earlier was there's invoke function.
There's also argument.
So that's how you go and retrieve the mutable thing.
So, what you pass here, this will become argument… Zero.
So then, when somebody writes this body, like, right here, if you write, key, or value, or attributes.
You need to know, however you define this function, you're also gonna say, oh, it takes parameters.
This is another array.
It's going to be a zero, it's going to be a mutable map, or you could say it's the key.
And then you have… Value is immutable.
But it basically allows you to control what you pass in, and then how it's referred to in this Function body, does that kind of make sense?
**Albert Lockett** 32:25 Yeah, yeah, yeah, yeah, okay. Yeah. I gotcha.
**Mike "Blanch" Blanchard** 32:30 I think you're… you're pretty close. You might have to tweak a couple things, but…
**Albert Lockett** 32:34 Yeah, and that, like, Yeah, yeah, and that scalar trap… That you were talking about, like, that… the copying, is that… do you mean, like, Like, the copying the data, or copying, like, the expressions?
**Mike "Blanch" Blanchard** 32:55 the data.
So the really only difference between a scalar function and a mutable function is, like, a scalar Always has to return.
**Albert Lockett** 33:05 It's data. It can't…
**Mike "Blanch" Blanchard** 33:07 It never modifies, like, you're in… when you're in the tree, you get these value structures, which are just… They only have a read-only surface. There's just no operation for, like, set key, remove key.
If you want to get into that, you need to switch over to the mutable side of the house, which is what those mutable value things are.
**Albert Lockett** 33:31 Oh, okay, I gotcha.
**Mike "Blanch" Blanchard** 33:34 But functions are a little different because they're sort of designed to be mutable, so you might… I'd have to go refresh, but just go in there and poke around and look.
**Albert Lockett** 33:47 Yeah.
**Mike "Blanch" Blanchard** 33:48 when you start, like, you know, finding all references, you should see some prior art in the KQL parser, in the bridge, like, I have some code and tests and examples, so, like, you should be able to find, like, some stuff to kind of see, like, oh, okay, here's how I do it. Just give it a shot.
**Albert Lockett** 34:07 Yeah. Okay.
**Mike "Blanch" Blanchard** 34:09 eat anything.
**Albert Lockett** 34:11 Yeah.
Awesome. Yeah, so I think, yeah, I think, like… Interesting.
Yeah, I… I'll.
**Mike "Blanch" Blanchard** 34:24 Because I see the same need at KQL, like, when it comes to doing anything, Useful. Like, redaction.
KQL doesn't give you a lot. You're sort of forced into functions. Like, if you want to run a regex.
Capture a bunch of matches, and then do things with them.
There's just no way to do that in KQL other than functions.
So I've kind of seen, like.
I haven't got these requests from users yet, nobody's tried to do anything more advanced than, like, oh, I'm just gonna enrich or remove stuff, but… there's gonna come a point in KQL, certainly, where people are gonna need to start relying on the functions.
**Albert Lockett** 35:07 Cool.
Awesome. Yeah, yeah, okay, cool. Okay.
Yeah, I think, I think I have a pretty good idea of, Of what needs to happen?
So, like, I think at a minimum, like we said, the function, expressions, I'll just add those two new variants for, like, discard and conditional.
And then, yeah, and then I can do, I can, I can do some exploring on the, try to, try to, try to, like, educate myself a little bit about how these functions get invoked.
And, and if… if we need to, like, have, a data expression that, like, has a function invocation, or if, like, for the time being, I can get away with, just having it be, like, a set expression, with a function invocation. I think… I do think I could get away with that, and, like, avoid having to copy the data if I'm just careful with my, my planning, of the… of the pipeline execution, but I'll see. But but I probably… I probably won't get to that, until next week, because tomorrow and Friday are, our holidays, so… I'll just leave that PR that I have open in a draft, and I'll put a comment on it, kind of explaining, like, what we talked about. But yeah, I like this idea of the function, invocation, because it, like you said, it kind of… it moves us to a UDF world in OPL, and it just… to me, it just seems like, hey, you know what, like, if the expression tree already supports this kind of stuff, then, like, let's not just add, like, a bespoke new thing, let's try to use what's already there, so…
**Mike "Blanch" Blanchard** 37:02 Alright, yeah.
**Albert Lockett** 37:05 Cool.
Yeah, and that's all from my side.
How are you?
**Mike "Blanch" Blanchard** 37:11 The reason I was pinging you about benchmarks and stuff is I finally got my… sort of abstract version of the Colomar engine.
to the point where I can filter So I want to run some benchmarks and compare it to what DataFusion is doing.
**Albert Lockett** 37:31 Awesome. Yeah, that's… that's super cool. Yeah, so… Yeah, so I sent you the ones that, that I had.
And I'm… I'm curious about this too, so, like, if, like, if there's anything that, like… like, you need me to, like, add to those benchmarks, or have any questions about it, like, I'm happy to, like, try to tweak them, or, you know, try to get you, like, some benchmarks that you can use to do the comparisons you need.
**Mike "Blanch" Blanchard** 38:00 Boom.
At the end of the day, so I've been, like, looking around the code in, like, the filter processor.
At the end of the day, it seems like we're both doing the same thing. We're calling into these arrow compute kernels.
It's just a question of… You're doing way more work.
to tell Data Fusion what it needs to do.
My engine's not using Data Fusion, it's just running on the arrow objects.
So it's probably not cheating where it could as much.
but it's also not spending nearly the amount of time, like, it just gets to executing instantly. So I'm curious to see what the results will look like. It may depend completely on, like, the size that you're running over, so we might have to do some benchmarks of different sizes and see what's going on, but… I'm hoping it performs pretty good.
**Albert Lockett** 38:57 Yeah, that'll be, yeah, that's awesome. Yeah, it'll be interesting to… it'll be interesting to see. You're right, like, we do, we do spend a little bit of time trying to line things up, correctly for, for data fusion, in terms of, like, projecting the columns into the order that the physical expression expects, In terms of, like, all, like, the planning, of the data fusion expressions, it's, like, we do try to do those, basically only once.
And, the… The thing about, like, doing that projection… That we do.
To try to line the data up in the, like, the columns in the right order, basically, is we're also checking if the columns, exist, and we need to do that for OTAP, Just because, like, a lot of columns are optional. So, for example, if you say, hey, I'm gonna filter on severity text, and you get a badge that doesn't have severity text, you're kind of… you're kind of screwed. Or you're not screwed, but, like, you had to handle it. So that's, like, one of the things we do during that lineup process, and then… Yeah, and then, and then, like.
The rest of the code, but, like, all that… all that planning stuff, like, should only be happening once, and then, like, each… each time we, like, get a batch, we just, like, try to, like, project it into the right order.
And then run it through the data fusion expressions, which are kind of, like, sort of a wrapper around the arrow compute, kernels, more or less.
And then, yeah, and then the other thing that filter code does, like, I'm not sure if you saw this, is it… it, It spends a bunch of time trying to, like… Line up the, selection… of… like, attributes that, like, might be used to filter, like, parent, logs. So, for example, like.
you could run, like, your arrow, or in our case, DataFusion, like, like, physical expression, or on, on, on attributes, so let's say if you say, hey, I want all the logs that have this attribute, you filter the attributes first, you get the attribute parent ID, then you have to go back and, like.
filter the log record by those parent IDs, right? And so that's, like, all the extra stuff that we're doing in our filter pipeline stage that, That, that we just don't get out of the box with DataFusion, unfortunately.
**Mike "Blanch" Blanchard** 41:40 Interesting.
There's a lot of code in there, it's hard to… consumable.
**Albert Lockett** 41:46 Yeah.
Yeah, did you want to, did you want me to, like, try to talk through it? Or.
**Mike "Blanch" Blanchard** 41:56 That might be really helpful.
**Albert Lockett** 41:59 Okay. Yeah, sure.
**Mike "Blanch" Blanchard** 42:01 We don't have to do it right now.
**Albert Lockett** 42:04 Okay, it's up to you. It's up to you. We can do it now, or we could do it next week. If you, like, if you wanted to have a chance to read through it first, and then ask questions, I'm happy to do that. Or, like, if… If you want to spend time now hearing me talk about it, I'm happy to do it, it's up to you.
**Mike "Blanch" Blanchard** 42:22 Let's do that next time, so we can… I want to benchmark my, sort of.
I'll say unoptimized, but it's… it's got a lot of optimization, but I didn't spend time, like.
Thinking about ordering, and… you know, I can just imagine a query where you do a bunch of things.
And at the end.
You do one thing that makes everything previously you did pointless, so if that went first, it would be more efficient.
I think that's where Data Fusion might be doing more, but I kind of want to just see, like, you know, what's the first shot look like?
If it's absolutely terrible, then I'll just stop wasting my time.
**Albert Lockett** 43:05 This sounds, hey, sounds good. Yeah, yeah, we can, we can, we can definitely talk about the filter code next week. That'll give me a chance to re-read it, too, so I can speak to it intelligently without scrolling all over the place and looking like a crazy fool, so… Yeah, we've been planning for that next time.
**Mike "Blanch" Blanchard** 43:22 Sounds good. Plus, you're about to go on vacation.
**Albert Lockett** 43:25 Oh, yeah, well, someone booked a meeting with me at 6 o'clock, so, I'm around for a little bit longer, but yeah.
**Mike "Blanch" Blanchard** 43:31 Well, enjoy.
**Albert Lockett** 43:34 Alright, thanks, man. Yeah, have a good… have a good week. Let me know the benchmarks, that's gonna be, it's gonna be really cool.
**Mike "Blanch" Blanchard** 43:41 Cool, I will.
**Albert Lockett** 43:42 Alright, take care.
**Mike "Blanch" Blanchard** 43:43 Good to see you, man.
**Albert Lockett** 43:44 Bye.
