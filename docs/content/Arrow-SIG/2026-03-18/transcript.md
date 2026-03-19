SIG: Arrow SIG
Date: 2026-03-18
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 00:31 Hey, Mike?
**Mike "Blanch" Blanchard** 00:34 Hey, Amen.
**Albert Lockett** 00:35 How's it going, man?
**Mike "Blanch" Blanchard** 00:36 Good.
**Albert Lockett** 00:37 Cool. Yeah, same.
Yeah, so, did you have anything that you wanted to discuss today?
**Mike "Blanch" Blanchard** 00:46 I had one question for you.
**Albert Lockett** 00:49 Yeah, shoot.
**Mike "Blanch" Blanchard** 00:50 I saw you did, like, a perf PR, and you implemented the, like, ID map thingy?
**Albert Lockett** 00:57 Yeah, exactly. Yeah, yeah, did you have a specific question about that, or did you just want me to talk about it a bit?
**Mike "Blanch" Blanchard** 01:06 My specific question, as part of that, you put in a pool.
of ID maps.
**Albert Lockett** 01:13 Yeah.
**Mike "Blanch" Blanchard** 01:14 So I've been working, I took your PR… And I've been… applying the changes that make sense to my engine, and then I put in the pool And my perf measuring… I don't see the pool really making a difference, so just kind of curious what you saw.
Why you did that.
**Albert Lockett** 01:35 I, I forget. Sorry. I wish I had the numbers before and after.
Yeah, I guess I've just, like, generally been trying to get in the habit of, Trying to, like, like, if I allocate something on heap, And I'm gonna be like… like, the code that allocated it will, like, run, like, for, like, a bunch of cycles, like, basically, like, run for every batch that you receive, like, try to, like, keep that heap allocation, Because what I've been noticing, Especially, like, when I was working on, like, the, we have, like, another feature I worked on recently that, like, we add, like, delta encoding to, like, some ID columns to basically, like, try to, like, optimize, like, the size of the… of the data when we, like, like, compress it for transport. That, like, reducing the heap allocations, like.
made, like, an incremental difference, but then when I did it, like, across that whole module, it, like, it, like, helps, like, in aggregate, so… that was, like, that was, like, the main motivation there, was… was just to, just, like, to try not to, like, be constantly, like, reallocating and then dropping that, that, that, data structure. But, like, yeah, geez, I wish I still had the, the benchmarks in front of me. I mean, like, yeah, if, like, if you find it, like, doesn't make a difference, then, like, don't, don't, don't, like, feel that, like, there's some kind of, like, obligation to, like, reuse that pool or something, but, that, like, that was basically, like, my thinking.
And, yeah, the heap allocation stuff, like, it makes a difference for the, like, some… sometimes, like, for these, like, vectors and, you know, boxes and stuff like that. But, like, where it really seems to make, like, a big difference is, like, some of, like, the arrow data structures that are, like.
allocated on heaps. So, for example, like, like, if you, like, allocate, like, a bunch of, like, intermediate arrays as you're, like, doing some processing, Depending on, like, what your algorithm is, like, all those, like, arcs that all the buffers are wrapped in, like, start to add up, so, that's kind of where I got into the habit.
Anyway, I apologize, I didn't answer your question directly. I don't have the exact numbers, so sorry if that's not helpful.
**Mike "Blanch" Blanchard** 04:10 No, I mean, if you get a chance to, like.
mess with it again and show me. I'm kind of new to Rust, like, you know, if I was coming from a .NET background.
I would be doing way more pooling.
Because it… Makes a big difference there. I just haven't seen it yet in Rust, and I don't know enough about what it's doing with the heap.
you know, I did a couple Googles, and AI told me, like, Rust is really good, don't worry about it. But I don't really know what that means and what's going on, so I just kind of need to educate myself a little bit.
Because what my initial thinking was.
I took your ID map pool.
And I was gonna make it generic so I could use it to pull ID maps, and bool buffers, and all the different arrow vectors and crap.
But I just measured it first on just the ID map, and I don't even see a blip, like… it's within… it'll go up plus or minus, you know, a percentage here or there, but it's always within the noise, so I can't… determine, like, is this making an impact? I don't really see it on the flame graph.
But I don't even know… If it would show there, you know?
So it's just kind of interesting.
I'll probably leave it out for now and come back to it.
Because then I also got problems with, like.
just the way Rust works, so, like, in your code.
You're basically passing the pool around.
But I didn't want to have to pass a bunch of different pools, so I was like, oh, I need, like, a state.
So then I was, like, messing with, like, lazy statics, and want cells, and all these different things in a Rust.
Which are cool, but they're generally for, like, immutable things. You can't just say, like, here's a mutable… Global pointer to the pool thingy.
Or I couldn't figure out how to do it yet, and I was like, oh, this is getting nasty. So then I was like, I better measure this first before I blow up all the code.
**Albert Lockett** 06:11 Yeah, yeah, interesting. Yeah, so I guess, like, Yeah, and I think, like, usually where stuff like that… Would show up on, like, your flame graph would be things like, Like… like, if you see, for example, something like vector.extend taking a long time, that could be, like, an indication that, like… like, this is, like, more speaking generally, could be, like, an indication that, like, hey, like, you know, I've… I've… like, created this vector, and then, I need to, like, put stuff in it, and then so I needed to, like… there had to be, like, some heap allocation to, like, you know, allocate the memory for that vector.
That's, like, typically where I've seen, this kind of, like… Like, this kind of, like.
**Mike "Blanch" Blanchard** 07:07 This, like, growth penalty.
**Albert Lockett** 07:10 Yeah, but then, like, if you… but then, like, if, like, in that case, like, if you were able to, like, reuse that vector… later on.
and it already had, like, capacity for what you're trying to put into it, then, like, you don't pay, like, the growth penalty the second time, basically. The ID, like, the… the ID pool's a little bit interesting, because, like, it's not, It's… so there's a vector of pages inside it, and those pages are sized such that, like, all the U16 IDs will basically fit in one page, and then, like.
And, like, those ID columns are used for, like, all the IDs and parent IDs that link, like, logs to resource attributes to attributes and things like that, but when, like, you start getting into, like, some of the deeper structures in, in Hotel Arrow, like, like, metrics, data points, data point exemplars, and the attributes on those, like, then we start using 32-bit IDs.
so that was, like… I was trying to, like, future-proof the implementation of that for when we might need to grow it, and add more pages, but, the, But, like, currently the engine only supports, like, U16 IDs, which would all fit in one page. So, like, in the ID pool in particular, we wouldn't actually, like, be, be, like, growing that vector necessarily. But that was the, That was the, Idea, anyway, behind what I was trying to do.
**Mike "Blanch" Blanchard** 08:53 The structure itself is fantastic.
really… so first I had, like, in my code, I was just doing… Probably, like, a hash set.
And then I noticed in… your stuff, it was, like, the roaring bitmap, so I switched to that, and that helped a ton with perf. And now I switched to your ID map, and it helped even more. I was like, this is great!
**Albert Lockett** 09:17 Oh, yeah, well, that was… that was, like, when I, like… Yeah, because I had gone through the exact same thing, basically, like, before we were doing hash set, and then… yeah, so… I'm glad it helped.
**Mike "Blanch" Blanchard** 09:30 I just today switched… I have a hash map I'm using for, like, value deduplication.
I noticed a lot of my perf time was being spent in, like, the random initialization, and then hashing each thing, so I switched to this crate called AHashMap.
**Albert Lockett** 09:54 Yeah, yeah, that's, that's a… that's a… that's… that's definitely, I think, the… the right move there. We… yeah, we also use a HashMap somewhere in our… In our batch processor code for the same reason, to try to make things a little bit faster.
**Mike "Blanch" Blanchard** 10:13 Yeah, it seems like the built-in one in REST is a little more cryptographically strong than you need for some cases.
I have pretty much now my, like, flame graph, it's just… mostly spending time in, like, the Aero compute kernel, so I'm like, cool, like, I've stripped away as much as I can from my side of the house.
**Albert Lockett** 10:36 Yeah, and I think that's… that's a… I think, I think that's the right intention, too. Yeah, that's, like, that's always where I try and, like, end up, is, like, strip away as much as I can from, like, the… the code that I'm writing, and so we just end up in the arrow compute kernels, and then… and then from there, like, you're kind of like… okay, like, is there a different way I can use these kernels, or could, like, the kernels work differently? But… yeah, that's… That, like… that's what I've always found has, like, the best efficacy as well, is doing it that way.
So that sounds good.
**Mike "Blanch" Blanchard** 11:10 Cool.
I don't have really anything else, I just tried.
you have a benchmark in yours called Attribute and OR together.
**Albert Lockett** 11:25 Okay, let me, let me go back and look at that, pipeline filter… And… Adder and OR together. Okay, yeah, I see that one.
**Mike "Blanch" Blanchard** 11:42 So it's doing… you know, a couple ANDs, and then ORing the two, and it's… I was curious about that one, because it's revisiting the same attributes You know, it's looking at, was it code?
And line, or name and line, or something.
Code.namespace and code.wine.
**Albert Lockett** 12:04 Oh, yeah, I suspect that.
**Mike "Blanch" Blanchard** 12:05 Second one is doing line.number.
**Albert Lockett** 12:09 Yeah.
Yeah, I see it there, yup.
**Mike "Blanch" Blanchard** 12:13 I was just curious… Because I tried… in mine, I'm trying to cache… Select attributes, code.namespace.
I should be able to spit back the same thing for the second hit.
But the perf on mine sucks. The perf on yours is much better, so I need to dig in and see what's going on there. I'm guessing I'm not… short-circuiting somewhere where it could be.
I don't know, need to get into some of these more complicated cases.
Yours is really fast. For the 8K records, it's, like, 228 microseconds.
**Albert Lockett** 12:54 Cool, yeah, it's interesting. I wonder if we do have a, a short circuit there. So, I know, so, I don't think, like, in our… in our filter code.
We don't do any, like, caching, I don't think. And I don't… I don't think that we do, like, short circuits on ORs.
In this case, I think we do have, like, a short circuit on… AND, where, if, like, the right side evaluates to know… or, sorry, if, like, we're doing, like, like, filter and, like, right and left, basically, or left and right.
If the left side evaluates to no rows, then we don't evaluate the right side, we just say, okay, well, it's, you know, we're gonna AND nothing with whatever's on the right side, and so we just don't, don't, yeah.
Don't do that. And I think, I'm just looking at this here, like, I know that, like, DataFusion internally also has some, It has some short-circuiting.
It has some short-circuiting.
But it… that, like, does the same thing.
Hmm… And I think they also have, like… Some kind of, like, some kind of, like… internal, like… like… If you're doing, like, like.
two filter criteria that are ANDed together, and the first filter comes back, and it's, like, super selective, then, what it'll do is it'll… Like, apply that filter to the input to the other side to, like, reduce how much stuff has to go into the other side of the filter.
I think it… I think it's… I forget what they call it, it's like some… like, pre-selection threshold, and I'm not actually sure if we're hitting that, but, like, in our case, like, each of these attribute filters, like, where we do, like, attributes code.namespace equals main, that actually, like, filters internally on two different onto, columns. It does, like, a filter where, like, key is equal to code.namespace, and the string column is equal to something called main.
And so… and then… and then data fusion is what's, like, responsible for, like, doing those filtering and giving us back, like, the… the selection vector that, like, has met those two criteria.
So maybe there's some filtering, Like, some, some, something, short-circuiting happening in there, I'm not sure. That… that would be in that… remember, like, last week we looked at, like, the physical, expression trait, and there was, like, a… there was, like, something called, like, binary physical expression that, like, implemented that trait? Like, that would be, like, like.
what is, what's executing that?
But again, I don't know if we're hitting it in this specific case.
**Mike "Blanch" Blanchard** 16:08 Yeah.
I'll dig into it a little bit, see what I can figure out.
**Albert Lockett** 16:12 Sounds good.
**Mike "Blanch" Blanchard** 16:14 It's very, very fast.
I haven't dug into sort of starting with simpler cases, and then working my way out.
**Albert Lockett** 16:31 Sounds good.
Yeah, that's… that's exactly how I started.
**Mike "Blanch" Blanchard** 16:37 In fact, you know, conceptually, like, any… any two… ANDs or ORs.
maybe I'm being naive here, but I feel like algorithmically it's the same, so you just have to figure out the cheat, and hopefully it will speed them all up for me.
**Albert Lockett** 16:56 Yeah, yeah, exactly. I think… and I think, like, our, Yeah, yeah, yeah. And I think that, like, in this case, like, if I look at, like, how we implemented it, so we didn't, like, in the filtering code that I have, it doesn't, like, flatten, it doesn't flatten everything.
Into, like, one record batch, so, like… so there's, like, there's a few different places that, like, ANDs and ORs get, like, get, like, applied.
One of them is, like, if you filter two attributes, I think we return, like, a, a bitmap of, like, the parent IDs, And then we, like, AND and OR those together, but if you, if you do, like… Some property, like, severity text, and, like, filter by some attribute, like the third benchmark there, where it says adder and prop filter.
In that case, like, we produce a, like, a Boolean vector that would say, like, which rows have severity worn, and then we create… for left filter, we create a bitmap of which, IDs have… which parent IDs have, attribute namespace equals main, but then, like, before we do the AND, we have to convert that bitmap of the parent ID back to a selection vector for, like, rows on the root record batch, and then we AND that together, so… So it's… so it's like… Depending on, like, how the filters are, Like, in our case, depending on how the filters like, what is on one side of an AND and an OR? We do the AND and OR in, in slightly different ways, Just to try to, like, reduce the amount of work that happens.
**Mike "Blanch" Blanchard** 19:09 Yeah, makes sense Cool, it's fun stuff.
**Albert Lockett** 19:21 Yeah, yeah, man, it is fun stuff. Yeah, this is, it's, it's fun stuff to work on, it's a great experience, and I feel like, you know, we're both, you know, probably learned a lot about trying to make rust go fast, which is a pretty good skill.
**Mike "Blanch" Blanchard** 19:39 I've… done a few things where I got into, like, unsafe… Like, buffer manipulation to, like.
Allied bounds checks and stuff.
And, like, I measure it, like, it helps a little, but… If it's not significant, I'm trying to keep the code as safe as I can.
**Albert Lockett** 20:00 Yeah, I think… I think that's… I think that's, that's… that's the right call. Yeah, that's, that's typically what we've been doing in, like, the rest of Hotel Arrow as well.
Like, there are a few… there are, like, a handful of cases where it did make, like, that last little bit of difference to, like, code that was, like, already pretty well optimized, but… Yeah, that's a… so I think… I think that's the right approach.
**Mike "Blanch" Blanchard** 20:25 Sure.
**Albert Lockett** 20:31 Yeah, and so, yeah, from my side, I don't know if I'll have it done this week.
But the PR might land next week, but it's, I think the only contribution I'll end up making is probably, like, adding the ability to, like, assign an attribute value. So currently, like, we have the ability to, like, assign attributes from just, Like, static values?
And we basically copied the code from the… the attribute processor, and we used it in the engine, and so I'm trying to write something that can… Assign the value of an attribute, like… In a way that's a lot more performant, but also, like, that you can, Like, compute the value of some expression, and then assign the result to an attribute, and the value… the result might not necessarily be, might not necessarily be a static, it might be… it might have, like, different values for every, for every row, and so you gotta line up the IDs and then, write them back to the, to the attribute record batch, so that's, that's what I'm working on this week. But, but yeah, I don't, like, I don't think in that case there will be any changes to, like, any of… any of, like, the code that's, like, shared between, the… Between, like, there won't be any changes to, like, the expression tree or anything like that, or, like, the KQL parser, OPL parser, so… Yeah, that's pretty much what I'm up to.
**Mike "Blanch" Blanchard** 22:20 Sounds good.
**Albert Lockett** 22:23 Yeah.
Okay, yeah, I didn't have anything else.
We can call it there, and, we can let you, get back to it, and… Just wanna say, hope the, hope the taxes are going well, as well.
**Mike "Blanch" Blanchard** 22:41 Yeah, they're all done.
**Albert Lockett** 22:43 Alright, man, glad to hear it.
**Mike "Blanch" Blanchard** 22:44 Actually, I have to send a check to my… Tax prep person.
**Albert Lockett** 22:49 It's remarkable.
**Mike "Blanch" Blanchard** 22:50 reminded me.
Have a good week, man.
**Albert Lockett** 22:55 Yeah, catch you later. Thanks.
**Mike "Blanch" Blanchard** 22:57 do it.
**Albert Lockett** 22:57 Right.
