SIG: Arrow SIG
Date: 2026-03-11
Duration: 99 minutes
============================================================

## Zoom Recording Transcript

Mike "Blanch" Blanchard 00:36:49 Hey, Albert.
Albert Lockett 00:36:52 How's it going?
Mike "Blanch" Blanchard 00:36:53 Sorry about that, man, I was totally spaced, forgot what day it was.
Albert Lockett 00:36:57 Oh, man, no sweat. Yeah, sorry, I know you're busy with your tax stuff, but I figured it's probably better for us to meet today, actually, from my side, just because, like, we're supposed to get a pretty bad storm tonight, and I don't know if I'll have power tomorrow, so… Okay.
Okay, I want to talk about this. Yeah, so if it's okay, maybe we could talk about 2190 first, that message I sent.
Yeah, so basically, like, you remember last week how we talked about this PR where I was trying to have, like, these nested
pipelines that we apply to attributes, and we had, like, that nested pipeline data expression, and then the thought was, like, oh, let's change that to be… to use the pipeline function expression instead.
So that's what I did. Basically, like, verbatim what we talked about, but there were a few, like, kind of, like, implications of it that I wanted to, like, get your thoughts on. So, the first thing was, actually, so let me just go through the changes here, so…
We see that in, in pipeline function expression, I added a new variant somewhere,
I added a new variant to it somewhere with the data discard here. And then… alright, so here it is. And then the first, kind of.
thing that I ran into was, the calendar query engine, like.
What it does is it, like…
it… it basically just, like, pulls… pulls out this data discard expression, then treats it like one of the stages of this pipeline. So,
When it was receiving it from, like, a regular, data expression, like we would have from…
From this, the expression would already be, folded, and the, the, like, you know how we have that tri-fold method, right?
So… and then… so when we were playing in the query, we're expecting the expression to be folded, and we're making some assumptions, and then it turns out that it wasn't getting folded.
when we have it inside a, inside a pipeline function expression. So what I added, and this is one of the things I wanted to confirm with you,
was in our, in our optimize method for the pipeline expression now, it goes and it folds all the,
all the data expressions, but then it also goes through all the functions, and if the body of the function is a set of expressions, then it goes through and it folds those expressions as well. And so, you can see that that
And like, so that's what this is doing. The reason there's so much code here, and it's a little bit tricky, is because
the, like, the pipeline resolution scope wants to have the functions as a borrowed reference, but we're actually, like, mutating something that was inside the function expression, so I do this little shuffle where I, like.
take the function expressions, out of the function, and then, and then fold it, and then put them back in. And that seems to work. It just makes it so, like, basically, if you have, like, a recursive function, then, like.
You wouldn't be able to, like, see the body of that function while you're folding an invoke function call that is calling that function, but,
But I… I think that's okay, because our only folding logic that we have for…
functions as if they have a static, return value and no mutable val- one static return and no mutable values.
Then we're able to fold them, but you wouldn't write a recursive function like that, so…
Anyway, so that's what this is doing. You, like, you can stop me anytime and tell me that, like, like, if you have feedback, otherwise I'll just keep going. I have, like, one or two other things.
Mike "Blanch" Blanchard 00:41:17 No, that's fine, I might be able to…
improve this so it's not necessary, but I'm fine with the hack.
For now, just to unblock yourself.
Albert Lockett 00:41:26 Okay. Okay, cool, thanks, yeah, thanks. Yeah, it is a little bit of a hack, I tried to… that's why I tried to put some comments about what it's doing here.
Mike "Blanch" Blanchard 00:41:33 here.
Albert Lockett 00:41:34 We have a dozen lines.
So the other thing that I… so what else did I say that I wanted to talk to you about? So there was this kind of, like, fold-the-function body thing.
Right, okay, so… The other thing was,
So, in our record set engine here,
So this is, like, the… this is the method in the record set engine where it's, like, evaluating the, the invoke function.
Mike "Blanch" Blanchard 00:42:06 Yep.
Albert Lockett 00:42:08 And so I wasn't sure if… like, so I added this discard pipeline function expression, and I wasn't sure if…
like, I should just leave this as, like, a dangling to-do, or if I should actually try to, like, you know, help out and, and implement this behavior. So what it… so, the way I have it implemented is,
It tries to evaluate the discard expression, and then if it thinks that the… the… the, I guess…
The value that was input to it should be discarded, then the function just returns null .
And so, like, I… again, I don't know if this is, like, the behavior we want, this is the behavior I implemented it, I'm happy to back this out.
What do you… what do you think about that?
Mike "Blanch" Blanchard 00:43:02 Yeah… Discard in the record set is kind of a challenge.
Because… At the root level, at the engine level.
it returns you, so you give it a batch of records. In its results, it gives you two vectors. It goes, here's everything that was included, here's everything that was discarded.
That is difficult in the function, because you can pass in any array or map and discard from it.
it doesn't necessarily know it's the source. It sort of… it would have to understand, oh, I'm actually discarding from the source, and it would need to somehow push those records up
So the overall thing works.
Now, I don't know if anyone actually needs that, so…
I'm okay if you just leave this a to-do for now.
Okay. That's sort of why I didn't put discard in there initially, because I was like, oh shit, this is going to be kind of difficult.
I'm okay if you just leave it at to-do.
And then I'll have to go in and sort that out at some point.
Albert Lockett 00:44:09 Awesome. Yeah, I'll, okay, so I'll leave this as a to-do for now. So I'll back this out, I'll back out these…
these tests, that I think were invoking that. And then, yeah…
Mike "Blanch" Blanchard 00:44:21 So, like, what it really needs to do… So the return value…
For a function is like a scalar.
You can return
some scalar thing, you're not required to. But the discard expression should run on, like, some mutable argument.
So what the discard should really do in this case is…
Figure out which argument, go and grab it.
Check the predicate, and then remove records from that map or array.
That's not too difficult, but then the whole idea of propagating those dropped ones back up for the source, that's harder.
But even that is kind of non-trivial, so if you just want to leave it a to-do.
I'm fine with that.
Albert Lockett 00:45:10 Okay, okay, cool. Yeah, that's… that's super interesting to know, and that's not… like, that's not what I thought a discard was doing, so I'm happy I know that, because I thought it was, like, basically, like, I have some input, I'm gonna either
evaluate the function or throw the input away, and then return null . So, okay, so yeah, so I'll… I'll turn this back to a to-do, I'll back out these tests I have for it, and then,
Yeah, and then I guess the other thing I was gonna talk to you about is not really relevant anymore, because what I was going to say was I also changed how,
how fold works for invoke function, because before we were, like, checking, like, oh, does it only have one return, and now it returns null if there's a discard, but if we're gonna… if we're gonna back discard the discard change yet, then I'll back out these changes to fold as well, because we don't need those.
Yeah, okay, so cool. So, I'll make those… I'll make those few changes to this, to this PR, and then I think it's pretty much ready for,
ready for review. I got LaRon to review, like, all the…
all, like, the stuff that's in, like, the OPL parser and the query engine stuff, I just wanted to get, like, your kind of thoughts on, basically, like… I mean, like, I'm happy if, like, you want to look at all this extra stuff too, but, like, you know, don't feel that, like, you're obligated. I really just wanted to, like, get your thoughts on, like, you know, the expression.
Mike "Blanch" Blanchard 00:46:33 I'm trying to wrap my mind around what your thinking was with the discard, so…
Maybe go back, show me your OPL query?
Albert Lockett 00:46:43 Oh, yeah, so, our… Yeah, so our, our OPL query is,
is this. So this would be, like… what this would, like, represent would be, like,
You've got all your logs, and then, for each log, here is, like, a…
a pipeline, like an OPL pipeline that we're going to apply to the attributes for this log, and then the output of,
the, this kind of, like, nested pipeline that gets assigned back to the log attributes. So currently, like, in our nested pipeline that gets applied to our attributes, we only have one,
operator, and it's this… this WHERE operator, and this is the,
And internally, this gets parsed to that discard expression, so this would…
Mike "Blanch" Blanchard 00:47:42 Basically, setting up a function that takes one argument.
And then you want to discard…
Rows from that argument, and you want to return it?
Albert Lockett 00:47:57 Yeah, I mean, that's… that's… Basically.
Mike "Blanch" Blanchard 00:48:01 You don't want to mutate it, you want to just return, like, a new… Record batch, or whatever?
Albert Lockett 00:48:06 Yeah, yeah, that's basically it, yeah. And so, like, the… I guess, like, in the way that I'm… in the way that I've implemented this,
the, like, the function, the function arguments and the return value, we basically don't use those at all.
I just… I'm just using the, like, the pipeline function expressions as, like, a container for
here's everything I'm gonna do to these attributes.
And then, and then, yeah, then I put a…
Mike "Blanch" Blanchard 00:48:48 A little awkward.
Can you pass the screen to me real quick?
Albert Lockett 00:48:58 Yeah, sure.
Mike "Blanch" Blanchard 00:49:00 Let's see if I can make this… Makes sense.
Sorry, I'm just clearing stuff off my monitor.
Okay, let's see if we can sort this out.
So we basically want to create, like, a function…
What do you call it? Apply?
Albert Lockett 00:49:34 Yeah, I could have… I could have any name. Technically, like, the way I've implemented it just has, like, some anonymous name that is the, is, like.
you know, the… It's just, like, the hash of the… the… the body.
Mike "Blanch" Blanchard 00:49:48 And let's say this is gonna take… Much…
in this world is a man out. Colomar's a little funky.
And then you want to essentially return your thing back
What you want to do, probably, is just…
Introduce a scalar for that.
Albert Lockett 00:50:23 So…
Yeah, maybe…
I mean… I… yeah, I guess, I guess, you know… Maybe we could…
I guess, like, to me, I wanted to… like…
you basically, like, use the exact same query planner that I use for, like, the pipeline that works on, like, the log records themselves. So,
like…
We would have a, like, we would have, like, a log, like a planner that, like, works on discard expression, and it creates a predicate, and then, and then,
And then we apply that predicate to, to the log,
to the, like, the contains the logs, so…
Mike "Blanch" Blanchard 00:51:37 do it that way, but I would expect it more to run on, sort of.
A function that looks more like this.
Where you pass in the mutable thing, and then you're…
I don't know how to express this. You want to set, like.
You know, you're, like, essentially passing in this riff thing.
So you're not using the return semantics, you're modifying that Reference to the thing.
Albert Lockett 00:52:16 Yeah, yeah, pretty much.
Yeah, pretty much.
Yeah, that's pretty much what we're doing.
Although, like I said, like,
Yeah, like, that's pretty much what we're doing. I mean, I could, and I could,
I could model it.
like that.
like I said, though, like, technically all I'm doing is, is I'm just using, like, the function body as, like, a container for, like, here's a bunch of expressions that, like, I know I'm gonna apply to attributes, so, like, even if I did, like, if I did, like, define the function in my expression tree as, like.
it takes… Attributes in their map.
Mike "Blanch" Blanchard 00:53:15 Is it using the same, like, distar data expression struct?
Albert Lockett 00:53:23 Yeah, pretty much.
Mike "Blanch" Blanchard 00:53:28 Let me see, hold on one second…
Albert Lockett 00:53:36 So it has, like, a predicate and a query,
query location audit, I think, is all that's on it.
Mike "Blanch" Blanchard 00:53:46 Find that thing in the curve, let's see… Discard data expression…
I mean, this is kind of what's afraid of.
So, basically how it's coded right now is…
It's just implicit that you're running on the source.
In order to really work in this scoop.
Of a function, it would need to know.
What it's operating over.
Albert Lockett 00:54:32 Yeah, yeah, and so, like, we just, like, in the… in the comic range and in the planner, like, we just kind of make,
Like… Basically, make that, make an assumption that, like,
like, I'm calling a set expression,
the source, or sorry, the destination is a field called, like, attributes, or called, like, like, resource at attributes, and then if the destinate… sorry, that's the destination, and if the source is a,
is a function, invocation, then we know, okay, it's one of these special function invocations. I need to,
like, plan what I'm gonna do accordingly.
Mike "Blanch" Blanchard 00:55:22 Yeah, I'm kind of at odds with, like, your engine versus, like, what the expression tree…
Albert Lockett 00:55:31 Yeah, tonight.
Mike "Blanch" Blanchard 00:55:32 Gross.
Albert Lockett 00:55:33 Yeah, and I mean, like, to be fair.
Mike "Blanch" Blanchard 00:55:36 Would it be…
Albert Lockett 00:55:38 I haven't… I haven't…
Mike "Blanch" Blanchard 00:55:39 A deal-breaker for you to do that for me?
Albert Lockett 00:55:42 To do… to do what, sorry?
Mike "Blanch" Blanchard 00:55:46 Introduce that target.
Albert Lockett 00:55:50 So you…
Mike "Blanch" Blanchard 00:55:51 Mutable value expression already has argument.
So what you need to do for… in your case, where you have source, what was it, like.
and attributes… And then he did wear, not something.
Albert Lockett 00:56:10 Yeah, yeah, basically some predicate there.
Mike "Blanch" Blanchard 00:56:12 So you're basically creating a function that has this as the argument.
And then you would create this as discard…
And then you would set target. It's basically…
And you don't have to actually use that in your stuff, but it would make the…
the expression tree accurate so that I could implement Corresponding in record set.
And make KQL functions work.
Albert Lockett 00:56:47 Okay, okay.
Mike "Blanch" Blanchard 00:56:48 lessons.
Albert Lockett 00:56:49 Yeah, yeah, yeah, yeah. So, so, okay, so, so that's, so that's, so you want, so you want to do that, then. You want to, you want to implement this in, in the record set engine, okay.
Mike "Blanch" Blanchard 00:56:59 I'm not… I'm not planning to do it immediately, but… so in, like, KQL,
Let's see if I can remember this. You can define a function that's, like, Value 1…
You can say it's a string, we can say value 2, it's an int.
And then… Your last line, We'll, like, return some scalar.
So that's, like, basically row.
some temporary thing and said, return T. That's sort of… this is a KQL scalar function.
You can also do tabular functions, where you could say, I want some table, accept anything.
And then I can do, like, what, T2 equals table, where… False.
So I can run, like, a discard into a temporary. I don't think I can return anything from a tabular function.
I'd have to go double check that. But here is where I would need to use…
discard inside of a KQL function, if that makes sense.
But what I would do here, so, like, let's say I have…
row new one, and this is string.
So what I would need to build is discard, kind of similar to this.
But my target here would be the second argument, argument table.
That's why I need that argument.
the target… Property on the discard, does that make sense?
Albert Lockett 00:58:51 Okay, okay, okay, yeah, yeah, yeah, okay, I see what you're saying. So, okay.
Yeah, okay, so, so… I guess then, the changes that…
I would need to make from… from my side.
would be the… the function that I define
its signature, it should take, It should take…
Parameters, it should take one parameter.
And that should be a map.
And then, and then my discard…
Is it… stop me, stop me if I'm going off… if I'm going off base here.
So my… my function that I defined should take parameters, and that parameter… it should have one parameter that's a map.
And then,
discard expression should have an optional target, and that target should be a mutable value expression, and in my case, that mutable val… the…
the…
In my case, that should be a mutable value expression.
with an argument, and then argument scalar expression, argument zero. I think.
Mike "Blanch" Blanchard 01:00:20 Yep.
Albert Lockett 01:00:21 Because right now… because right now, I'm just creating a function with,
With no arguments, and just kind of,
Knowing, like, and just kind of, like, you know, knowing the right thing to do. Yeah, so I can do that. Like I said, I won't, like…
I won't actually be… using those fields, just FYI. Like, I probably won't look at them.
Mike "Blanch" Blanchard 01:00:51 I'm fine with that.
Albert Lockett 01:00:52 Okay, okay.
Mike "Blanch" Blanchard 01:00:53 It just gives me the ability, like, if you drop this in.
then if I go to implement it, it'll… it'll make sense for record set. And maybe in the future, you'll want to do user-defined functions, and you'll actually use it, but…
Albert Lockett 01:01:08 Yeah.
Mike "Blanch" Blanchard 01:01:09 don't need it. I'm… it's fine with me to just ignore it.
Albert Lockett 01:01:13 Yeah, and that's… that's kind of what I was thinking. I was kind of like, like, I don't think I will… I will use this right away, but yeah, like, basically at the end, like, in the future, you're right, if we do have, like, some kind of, like, other functions, then, like, I'll need to check this stuff, just to basically, like, know, like, what to do.
I think. So, okay, so that's what I'll do. That should… that should be pretty straightforward, I think.
And yeah, I should be able to get that done before, like…
tomorrow, basically. I should be able to, like, get rid of those other changes that we, that we talked, like.
like, make the changes that we talked about at the start of the call, and I can make these changes, and then, yeah, and that should be pretty doable within the next day or so.
Cool. Okay, yeah, man, thanks again. This is,
like I said, this expression tree stuff, it's, it's like…
I feel like I'm starting to get my head around the logic of it, but, like, there's a bunch of stuff I don't know, so it's… it's definitely, like, helpful when I get your, your, your feedback on,
on this stuff. So, yeah, definitely appreciate you, like, taking the time and telling me what to do here.
Mike "Blanch" Blanchard 01:02:27 Overall, let me know if you run into anything.
Albert Lockett 01:02:30 Yeah.
Mike "Blanch" Blanchard 01:02:30 If you get the changes, ping me, and I'll… I'll make sure I take a look at the PR.
Albert Lockett 01:02:35 Awesome, sounds good. Yeah, so that was all… that was all I wanted to talk about was, was this PR. I'm still, I'm still interested. Did you get a chance to do benchmarking, between the two, filter, engine implementations?
Mike "Blanch" Blanchard 01:02:52 I've been working on it.
So I have, like… Here's my engine, here's… What's checked in?
As of, like, a few days ago.
Albert Lockett 01:03:07 Okay, so we.
Mike "Blanch" Blanchard 01:03:08 I've just been… working on it, so when I first ran mine, My simple field…
filter… so I took the exact same benchmarks that you have, and they're all runnable in my engine, which is kind of cool. So I can try… I'm trying to get apples to apples.
So I'm as fast or faster faster for the simple stuff, where you're doing, like, severity text, severity number, where you sort of have an arrow table
Ready to rock with all the values.
Albert Lockett 01:03:41 Okay.
Mike "Blanch" Blanchard 01:03:42 The next one I'm working on is the simple filter, which is doing, like, You know, where attributes…
Name equals, equals, like, some string.
My 32 is good. My 32 is, like, ripping fast.
But as the batch size goes up, so I'm in, like, 684, the data fusion stuff is…
less. 56,489. When I first had it, I was, like, in the 800s. I was almost, like, twice, and I've been able to, like, optimize it down.
I'm trying to figure out… how it's faster. I haven't gotten to that yet.
I'm, like, looking at my loops and my algorithms, and I have to dig into DataFusion a little bit and see, like, how is this possible?
So yeah, I am there. I'm just trying to get it better.
Albert Lockett 01:04:40 Okay, interesting. So, if I recall, simple… okay, interesting. Sorry, maybe you had to go.
Filter. That's the benchmark. Simple adder…
Mike "Blanch" Blanchard 01:04:52 Kind of show you what it's actually running.
Albert Lockett 01:04:54 Oh, so we're, yeah, we're filtering by attribute.
Mike "Blanch" Blanchard 01:04:57 I'm looking at this guy.
Albert Lockett 01:04:59 Okay, yeah, so we're checking… we're taking… okay, so look if there's an attribute, and then,
Check if it's, okay, so it's, like, filtering by attribute value, got it, okay.
Yeah, okay, and then, that's cool.
And then, so, interesting. Cool. Okay.
Yeah, I remember…
Mike "Blanch" Blanchard 01:05:24 Maybe, you know, off the top of your head, if you don't…
So, like, when this is… when I'm…
Finally gonna actually do the heavy lifting for this thing.
What I'm calling into are these, like, compute functions in Arrow.
Let's see if I can find it. It's basically… the… Arrow, compute…
filter kernel, which I think you're doing as well, right?
Albert Lockett 01:05:58 So I say I want to take this log batch and filter it, and I basically give it a bool array.
Mike "Blanch" Blanchard 01:06:04 It's this giant, like, keep this guy, drop that guy, keep this guy, drop that guy, blah blah blah. It's just, like, on and on forever. Does that ring any bells?
Albert Lockett 01:06:14 Yeah, we're pretty much doing the same thing.
Mike "Blanch" Blanchard 01:06:18 So, when we talk about the logs batch.
you have zero, I think it's a resource.
you have one, I think it's Scope, then you have two…
It's the actual logs, and then you have 3, it's the log attributes.
Albert Lockett 01:06:38 Yacht?
Mike "Blanch" Blanchard 01:06:39 So… You can filter logs, and that will reduce You know, the log records.
My question is, are you also filtering attributes, scope, and resource?
Albert Lockett 01:06:54 Yeah, basically. So, Yeah, so what,
Yeah, so what we do,
It's… sorry, like, are you talking about, like, do we filter them, like, as we're trying to decide, like, which logs to keep, or are we filtering them, like,
Like, after you've decided which logs to keep.
Mike "Blanch" Blanchard 01:07:22 Basically, like, let's say…
let's say I have log 0, log 1, log 2, and I ran some query, and I decide I'm gonna keep you.
Drop you, and drop you.
So somewhere in the attributes mess, it has, like, the parent IDs, so it might have… let's say it has log 0 and log 1. Log2 doesn't have any attributes for some reason.
I guess when you filter it, you should, like, remove all that stuff.
Albert Lockett 01:07:55 Yeah, we, and we do do that. Let me see if I can find…
where, if I go to filter.rs…
there's a function that does this, and the name is something very stupid. It's, like, filter… It's, like, filter…
record batches or something. It's like something completely, hold on, let me see if I can find it. I didn't give it a good name.
Filter… OTAP batch.
So if you, if you open up,
filter… I don't know if you still have, like, my implementation open.
If not, I can send it to you.
Yeah, so, is that it? Filter? No, that's the benchmarks. Go… Pipeline… Filter…
That one there, and then go on line, 1325.
Filter OTAP badge. Yeah, so if you scroll down here,
a little bit, you can see what it's doing. So it,
It goes through and it filters all the child batches, recursively. And that's… that's what's doing the,
That's what's removed, like, that's where we'd be, like, removing the attributes.
So basically what happens here is, like, we,
like, that… that… that selection vector you were talking about, where we have that vector that's, like, keep the… like, which logs to keep. After we compute that.
then we…
then we come into this function, and we filter, like, the root batch, and then we go through and we filter all the children out by their parent IDs.
Mike "Blanch" Blanchard 01:09:45 Okay, I'll try to figure out… I'm… I'm doing it as well.
So, like, I filter the main logs.
if there's nothing, it… no ops, or it returns quickly. If it does have things, then I, like, I go and I filter the child stuff as well.
I just kind of rolled… some logic, and then I call into the compute kernel.
I just wanted to make sure that your code is doing that as well, so I'm doing apples to apples. So I'm like, well, if he's not filtering the attributes, then of course I'm going to be slower, but if it actually is.
Then I'll try to figure out what it's doing.
Do you know, for Rust, like, these are nice. It's nice to know, like, okay, I'm taking… 500…
Whatever that is, microseconds.
Do you know of a tool to show, like, what functions? Like, I'd like to kind of break it down.
So I can… Figure out the high-value spots to go and optimize.
Albert Lockett 01:10:47 Yeah, do you want me to… I can show you what I do, if you want. Sure. Yeah, let me share here. So, I'll go, share, desktop…
to… Some of this.
Mike "Blanch" Blanchard 01:10:59 I miss… you know, my .NET tools.
Albert Lockett 01:11:03 So, what I do is I use this tool called, Samply.
Here, I'll post this in the chat.
in the Zoom chat. Oh, am I sharing? No, I'm not yet, frig. Okay. There we go.
I'll post this in the Zoom chat here.
So this is this tool. It's a… it's a command line tool, you can install it, I think, Cargo… you can use cargo to install it, because it's written in Rust. And then, and then what you can do…
You can go… Like, usually you'd be able to go cargo, bench, bench, filter.
And then you can give it the name of the filter, but I forget what they're called,
simple field filter, I think.
And then hopefully this will compile pretty quick.
Actually, I'm gonna take out the, there's some,
So here's the other tip,
This can take a really long time to,
to iterate on, so I like to…
remove this, remove this, and then go LTO thin.
Like that. Just redo this. So now this whole… now my benchmark should compile faster. fuck, but it's gotta do a bunch of recompiling.
Okay. Anyway, what I was gonna say when that's done is,
you can basically run, like, the same command you would use to run an individual benchmark. You can go, like, sampling, record.
bench, filter, simple field filter, and then, and that's it. And then, it will… it will run, and then it will pop open a, it'll pop open a,
like, Firefox, dev tools with, with all the profiler stuff up. Frank, I want this to finish, because then, then I will show you how it works, because it is pretty cool, in my opinion.
And this will hopefully just take a minute. It's only got 30-something packages left to do.
Come on.
Mike "Blanch" Blanchard 01:13:27 We were too quickly.
Albert Lockett 01:13:29 Yeah, so what do we… What do we do…
Just going back and looking at that code we were talking about while we're talking,
So we do, filtered child batch, that's this.
So this is where we do it. Cheers.
Where is that defined? That's here.
That's then we try and get the parent payload ID somewhere, and then we,
If we build a bitmap… of the parent ID.
And then we call into this other helper function.
A filter record batch, is what we do.
Build selection back.
Okay, anyway, I forget what this code does.
We're almost done here.
Data fusion stuff, it's building.
Hopefully that won't take too long.
So you're, your implementation of this is, in the,
You haven't checked in, or is it on your fork, or is it still, or is it, like, private, like, like Microsoft,
like, proprietary.
Mike "Blanch" Blanchard 01:14:57 Most of it's local right now, I have some stuff staged, but I haven't pushed it to my fork.
I can, if you want to just, like, poke around and see what I'm doing.
Albert Lockett 01:15:08 Yeah, sure, I mean, I'm just, I'm, like, gen… generally interested, but
like, you know, I don't want to, like, force you if it's not ready, but I mean, I…
Mike "Blanch" Blanchard 01:15:18 Ugh.
Albert Lockett 01:15:19 Fair.
Mike "Blanch" Blanchard 01:15:20 Depending on how these benchmarks come out.
Like, if I can't get it faster, then I'm gonna have to, like… I'll have to switch approaches. I was trying to prove out that, like, you can do this aero-native
you know, use the query expression tree as the plan, essentially, and just rip on all the arrow stuff, but if DataFusion has magic that's gonna be better, then I'm just gonna throw it all away.
Albert Lockett 01:15:50 Okay, yeah,
Yeah, so I think, so, yeah, it's interesting, because, like, half of… so half of what we're doing here… okay, so hold on before I talk about that, let me just, mention this. So I think I can go…
If I do this… So I go Samply Record, and then I run my benchmark like that.
And then this will, this will just take a quick second.
So… like, runs the warm-up, and then it does the benchmark, and then…
Yeah, and then this pops open here, so this is the profiler view, and then, you can kind of zoom in. And so what I usually do is, like, you have to, like, zoom in on the part that, like, it, like, was actually running the benchmark, and then you click it.
And then you can go to Flame Graph, and then you can see where it was, like, spending all the time. And so this is really cool, because then you can also click right on the function.
And then it will take you, like, right in the function, so we can see that, yeah, like, filtering out those child batches was basically what was slow in, in the implementation that,
That I, that I have, at least for, like, when it's 32… when it's 32, rows. So that's, anyway, that's the tool that, that I've been using for pretty much all my, profiling stuff.
Mike "Blanch" Blanchard 01:17:11 Cool.
Albert Lockett 01:17:12 Yeah, things like that.
And then,
Yeah, the other thing I was gonna say was, just, like, while we're talking about the data fusion stuff, so,
Yeah, like, I don't know if there's… so,
in, on this side, there's kind of, like, two, there's two bits to it. Like, we definitely used, like, Data Fusion…
for, Like, like, any expression that would, like, filter, filter, like…
like, something on a given record batch. So, for example, like, if we're doing something like in this benchmark here, where it's, it's attributes, where code.namespace equals main, we, like, we would write a DataFusion
Function to do the,
I just had it there somewhere.
call something.
just had it there somewhere. But we would basically write, yeah, so we would, like, write a data fusion
expression like this to do that filtering. So that's, like, where we're using DataFusion, but, like, there's also a bunch of, like.
Like, after we filter the, the attribute record batch, then we need to, like, join that back to the, to the log record batch to figure out, like, what were the log,
What were the log rows that we had to keep?
And for that, we're not using DataFusion. That's all, like, hand-rolled stuff that happens, in this filter exec.
And the other… so then the other thing I would say about,
Data Fusion is we are using,
like, basically just the data fusion, physical… expressions?
And there's not a huge amount of,
like, magic in those. If I go look at the implementation,
Sorry, maybe you don't care about this, you have to go, but like, if I go look at that implementation,
The main one that gets used everywhere is, like, this… This binary,
implementation of physical expert, and then, if I go look in the source in this,
it's like… Where's function evaluate?
Like, it doesn't have a huge amount of,
of magic, like, it just figures out, like, okay, the operator I'm applying is going to be, like, EQ, and then it calls applyCMP,
And I think that this applaudis CMP is, like.
a pretty thin wrapper around the Arrow compute kernels. So then, like, the only…
The only magic it has on the…
on the outside, I think, is,
It's got this short-circuiting stuff in it, but I,
I don't think that's actually, like, used a heck of a lot.
Anyway, so I guess, like, what I would say is, there's not too much magic to it, I don't think, at least inside Data Fusion, if that's helpful to know.
Mike "Blanch" Blanchard 01:20:49 It is helpful.
Albert Lockett 01:20:51 Okay.
Cool.
Mike "Blanch" Blanchard 01:20:55 I can tell you, like, conceptually.
what I thought would lead to higher perf may be hurting me, and that's like…
Oh, I didn't click share. Share.
So when you have, like, if you do severity text.
You know, you get, like,
arrow, you know, one of these dictionaries.
With keys, and then it has, like, for every log record.
You know, it'll tell you, like, the value.
So, you have one… let's say this is warm. Here, you know all this stuff, but…
That's sort of the aerostructure, right?
Albert Lockett 01:21:48 Yep.
Mike "Blanch" Blanchard 01:21:51 that's all great. The engine that I have, like, it can spin on those all day long. Where it gets a little trickier is if you do, like.
attributes, name… When you jump over to the attribute structure, It's like… You have the parent IDs.
And you don't have, you know, a row for everything, right? You'll have, like, Zero is…
Let's see, 0, 0… And one is one…
But this might actually be, like, this record. This might have parent or ID,
1 index 2, right? So that's that whole thing where you have to join things back together.
You must be so far?
Albert Lockett 01:22:45 Yep.
Mike "Blanch" Blanchard 01:22:46 So what I have in my code is everything's kind of normalized, so even when you… if you say, give me attributes name.
It's going to return you something
that looks like a standard table. So in this case, this'll just be null …
And you'll have, like, you know, Mike… Albert.
So, like, I'm normalizing everything so that
You don't need to join anything in the end, you just… every table looks the same.
And you can just code against, like, okay, keys will always be the number of records.
So you have to do some work up front when you query that to build everything correctly and return it back.
I think maybe the time is being lost there, but I don't know, because I don't have that flame graph, so I've just been kind of guessing, like, where to optimize.
But I was thinking, like, doing that…
I know it's gonna take some upfront effort.
But what's cool about that is then, everywhere in the code, like…
the code base that I'm doing is a lot like RecordSet, right? It doesn't know it's running on OTEL, it doesn't know about these attribute tables. It has this abstraction layer, so, like, there's some normalization that's going into it. But the benefit from that is, like, to code against it, it's very simple, because
every table looks the same. You only get one of two things. Anything you execute, it's either going to give you back a single record.
Like, if you did some static query, like, if you did…
May… So this… the worn here is, like, a static value, it's a singular.
And this is going to be a table results.
But all tables look the same, so this would run the exact same code as would, like, Severity text.
Because it's just a table.
In sort of the standard arrow structure.
It keeps the… The code in the engine is very simple. It looks very close to RecordSynth.
But so far, the perf, like, this is running fantastic.
this perf is kind of sucky compared to what you've done, so I'm trying to understand why, and maybe the normalization up front was the wrong
way to go, and I need, like, some way to…
hide that? I don't know. I'm still kind of exploring, but that's… that was the idea that I had.
Does that make sense at all?
Albert Lockett 01:25:31 Yeah, yeah, that makes sense. Yeah, I think, yeah, it'd be interesting to see the,
Interesting to see the profile, because, yeah, I think that, that.
Mike "Blanch" Blanchard 01:25:41 there's kind of 3 phases I have going on in the mine.
The first phase is select… from attributes.
And… normalize.
Then there's… Second would be, like, the where part.
So… you know, warm. What this is doing is convert…
table to Boolean array, so basically apply that condition on the values, and then the third is, like, actually do the filters.
So there's a little bit of perf being spent on all three.
So I've kind of… I've gone through all three and tried to optimize them. So I was able to shave off, you know, like, 200…
microseconds off my 800, but I still need…
Another 200, 150 or so, so it's… it's close, but… You're still beating it.
Albert Lockett 01:26:40 Interesting. Yeah, that's interesting.
Mike "Blanch" Blanchard 01:26:43 Like, the really small one for 32, this is saying 10… I can rip through… the small things.
But as… as it grows, like, it's…
it's getting slower, so I'm just trying to figure out what's causing that, and if there's anything I can do. Is it just an algorithm tweak? Is there, like, some…
extra loop I have somewhere, I don't know. The profile will probably help me a lot.
Albert Lockett 01:27:12 Yeah.
Yeah, I'll bet. I'll bet. Super… that's super interesting. Yeah, normalization stuff. So then, like, once you… once you've got it normalized,
Like you said, you were doing,
Your second stage is the filter, so if you had, like, like,
let's say it's, like, severity text is equal to Warren, and, attribute name is equal to Albert, you would have, like, presumably you have some logic to, like, do both those filters, and then you've got, like, your selection vector, and then you, like, AND those together, and that becomes, like, the final one or something.
Mike "Blanch" Blanchard 01:27:48 Yeah.
Albert Lockett 01:27:49 Okay, yeah, interesting.
Mike "Blanch" Blanchard 01:27:51 It's more or less exactly like how the record set engine works, where you have an execute logical.
You'll have an execute scaler, So I haven't built…
many, but I built, like, the length, So I could… Mess with, like.
you know, dynamic tables, and then I built source so I could mess with, you know, selecting from the arrow batch initially.
So you'll kind of see, like, you know, it runs the inner scalar. If it's a single value, it has logic, what to do for a single. If it comes back a table, which is currently called dictionary, then it has, like, a dictionary operation. It pretty much works like that across the board, so you can select
You can do… da-da-da-da-da-da, you can do… attributes, Name?
which is select from a table using a single value. You can also do… you know.
Go and give me a table of all the name values, and then give me the corresponding table values, so you can… you can do a table
Selecting another table, which was kind of a…
That was an interesting thing to code.
Albert Lockett 01:29:16 Interesting.
Mike "Blanch" Blanchard 01:29:16 you can see in here. So, like, if you get a single value, it's there. If you get a dictionary, there's logic for that.
The result of a scalar is always… One of those things.
So, like.
in the case of, like, a length. You know, you're passing a table into another operation, but it's always giving you a table back, and it's always in that same normalized structure, so it's kind of easy to, like, compose the little functions.
Logical works basically the same way.
So if we look at, like, equals… You know, it's gonna take…
two inner expressions. It has a left and a right, so it's going to go and say, okay, give me the result of those.
So you'll get a left that's a single or a table, you'll get a right that's a single or a table.
And it calls in this compare function.
So compare knows how to say, okay, if I have a single on the left and a single on the right, then it's a single… so compare single to single. It's like a record set operation.
If it's a single on the left, table on the right, then I have a single-to-table. I have the reverse of that, and I have a table-to-table.
So just those, like, 4 functions…
I was able to support, like, 100% of the logical surface in the expression tree.
So I have everything in Logical working.
Because it's just… it's easier than scalar, you know, it's just bools. It will…
Logical similar to Scalar, it will return either a single bool or a bool table.
one of those two things. And you can composite them kind of in the same way, if that makes sense.
Albert Lockett 01:31:03 Okay, yup, yup.
Mike "Blanch" Blanchard 01:31:04 So, like, 100% of my code
For logical expressions is, like, it's…
in here, and it's done in, like, you know, there's not a lot of tests currently, but it's, like, it's not a lot of code. So just doing the normalization, having the abstractions, like, it keeps the engine implementation super clean and simple, really easy to add widgets to it.
kind of turnkey. I just need to figure out a way to get the perf
where we need it to be, if that makes sense. And it might be impossible, I don't know. I'm still kind of exploring it.
Albert Lockett 01:31:40 Okay, interesting.
Mike "Blanch" Blanchard 01:31:42 Does that sort of make sense?
Albert Lockett 01:31:44 Yeah, I think I would need to, like, like, read through it a little bit more to try to, like, really grok it.
It's interesting, though.
It's… it's interesting.
Mike "Blanch" Blanchard 01:31:58 So how the hotel comes into play…
So I have an OTAP bridge.
And it… it's… it works a lot like Record Set in that…
The engine gives you a couple traits.
There's a factory, and then there's… a table.
That's all you have to implement. So all the logic for knowing, like, the OTEL-specific, like, you know, severity number, severity text, all of the schema, it's all localized to this bridge.
And then all of the attribute child table insanity, I'll call it, is this…
attribute struct that I have set up.
So the root table has this getValue, so when you query
when you say, okay, I want severity text from the source, it kind of falls into this code, and then it will return… so severity text is easy, right? You see here, there's, like, a basic arrow, like, okay, give me the log record, figure out the column, downcast it, you know.
pretty much aero-native, it just wraps it in this thing and spits it back.
for attributes, Record table can return a child table.
So it's saying, okay, if you give me attributes, I'm gonna hand you back a child table.
So I've localized all of that madness into sort of an abstraction. So in the attributes table.
here is where I have that code that kind of normalizes things.
So this is… I'm guessing, where the perf problem is, but…
Who knows? So what this guy's gonna try to do is…
So, it's being asked for some attribute. So, key here is, like, value 1, or attribute 1, or something.
So it's gonna go say, okay, look at the attribute keys, record batch.
Try to figure out the value index, like, does that attribute exist?
If it does… Then I'm gonna go through…
What the hell is this? All the… All the rows…
figure out… so this is, like, the reverse mapping right here, so this is saying, okay, for the ID,
Of that record, what is the true…
index in the parent table, so this is sort of the normalization right here. So it builds…
It builds a, basically an arrow table as if attributes
whatever you're looking for, value one, as if it was, like, severity text. It gives you the same structure where you have keys, and every log record has a row in the keys, and then the values are sort of in their own value array.
Albert Lockett 01:35:04 Okay.
Mike "Blanch" Blanchard 01:35:05 Kinda makes sense.
Albert Lockett 01:35:07 Yeah, val… okay, interesting. Value, VEC… Interesting. Yeah, okay.
Interesting.
Mike "Blanch" Blanchard 01:35:15 Expecting it to perform.
like, lightning. So I'm kind of surprised that it's not. So I must have made a big mistake somewhere, but that was… that's the approach I'm trying to take, which is essentially normalize everything up front so that it's really easy to take any two tables and
Compare them… transform them, Do whatever you need to, basically, inside the engine.
Albert Lockett 01:35:42 Yeah.
Interesting, that's, yeah, okay, geez, that's interesting. Yeah, I'll admit that I kind of feel like I need to read it to crock it a little bit better, but .
Mike "Blanch" Blanchard 01:35:52 I can push… I have a lot of it local, but I'll push it into my branch, and then I'll just send you a link to it. You can go peruse it if you're interested.
I would say it's still highly volatile, like, I expect it to change a ton, but if you want to give me any feedback on the approach and anywhere you might see where I could steal some perf cycles.
Albert Lockett 01:36:14 Sure. Yeah, sounds good.
Mike "Blanch" Blanchard 01:36:16 It could be… a lot of what I'm doing, you know.
you'll see there's a lot of, like, vectors and buffers, like, maybe I'm just overusing the heap and I need to implement some pooling.
I don't really understand deeply in Russ, like, if you…
If you take some storage from the heap.
What's the performance hit there, like, when you…
take it, what does that cost you? When you discard that thing and it goes back, what does that cost you? That's a little unclear to me and Russ.
Albert Lockett 01:36:50 Yeah, and I think it depends on all the factors, depends what the type is, and, like, what the,
Like, what allocator you're using?
But,
Yeah, like, if it was taking a long time, like, you'd probably be able to see it on the profile, you'd see, like,
Like, HashMap, maybe insert, as it's, like, trying to grow the HashMap and trying to…
Or I guess you've got width capacity there, so… so,
You'd either see it, like, there, or you'd see it, like… drop.
Mike "Blanch" Blanchard 01:37:25 Yeah, I wonder if there's, like, a lot of time being spent, like, some kind of DLock method or something.
I don't know. I'll keep… I'll keep banging at it.
Albert Lockett 01:37:37 Yeah, this is cool. Yeah, like, I, I mean, you know, I, like.
feel… I'd love to… I'd love to take a look at it if, if you're gonna… if you're gonna push it, but, you know, like, I don't want you to, like, feel pressured to… to… to… to have to do it if you don't want to share, but I, you know, I'd love to look at this.
Mike "Blanch" Blanchard 01:37:59 No, no problem.
Albert Lockett 01:38:00 Cool.
Okay.
Awesome. Yeah, so, cool, that was all I had.
And I know that you, you gotta get prepared for,
Mike "Blanch" Blanchard 01:38:16 Yeah.
Albert Lockett 01:38:16 the tax thing, so I'll…
Mike "Blanch" Blanchard 01:38:19 beating me.
Albert Lockett 01:38:20 Alright, man, yeah, cool, thanks again.
Mike "Blanch" Blanchard 01:38:26 Good luck with the storm!
Albert Lockett 01:38:27 Jeez, thanks, man. I saw you guys… I saw on your… on your Windows, taskbar, you guys are having a heat warning, so it's complete opposite.
Mike "Blanch" Blanchard 01:38:36 We're gonna get into the 90s.
I don't know what that is for you, like, 30s? What's the human body, like, 33 or something?
Albert Lockett 01:38:44 Oh, yeah, so it's, it's, you guys are hotter than humanly, possible.
It says it's minus 21 Celsius. I don't believe that, but I guess we'll see. Well, I'm not going outside, so I guess we won't see.
Oh, shit.
Mike "Blanch" Blanchard 01:39:01 The storms I worry about are more like wind and heat waves.
A little bit of rain. People freak out here when it rains.
Albert Lockett 01:39:11 Yeah, where are you located, by the way? I thought you were in Seattle, but I guess I'm not.
Mike "Blanch" Blanchard 01:39:14 I'm in Southern California, so, like, Anaheim…
Albert Lockett 01:39:18 Oh, sweet. Okay, cool.
Better weather down there.
Mike "Blanch" Blanchard 01:39:23 Pacific Northwest.
Sunny, sunny pretty much every day.
Albert Lockett 01:39:28 Dude, that's awesome.
Very cool.
All right, well, let you get back to taxes. Thanks again for the tips on, on the, on the AST and stuff.
Mike "Blanch" Blanchard 01:39:39 Cool, sounds good. I'll talk to you soon.
Albert Lockett 01:39:41 Right.
