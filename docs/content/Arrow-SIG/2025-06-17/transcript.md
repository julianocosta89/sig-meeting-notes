SIG: Arrow SIG
Date: 2025-06-17
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**David Dahl** 00:38 Hey? What's happening?
**albertlockett** 00:41 Which
looks like we're East Coast guys staying late for do a meeting.
**David Dahl** 00:54 Huh!
**Drew Relmas** 02:19 Hello, everybody! Good afternoon or morning, depending on where you're joining from.
Is my audio coming through.
**albertlockett** 02:31 Yes.
**David Dahl** 02:32 Oh yes!
**Drew Relmas** 02:33 Great. Oh, there's true.
**jmacdonald** 02:34 I agree.
**Drew Relmas** 02:38 Yes, yes, it can cool.
I was gonna try and start the meeting. But please, now that you're here, please go for it.
**jmacdonald** 02:47 Well, would you like to project the meeting notes?
**Drew Relmas** 02:54 Yes, I think I can.
**jmacdonald** 02:59 And then I see Albert's here. David Ukash Jake and drew I have not entered my for myself an agenda in the notes which Drew is bringing up, and however, I know that we have an interesting conversation that I've been part of with Albert and Ukash that. So I'd like to ask for an update on
So this is following my my sort of discussion and presentation about the same topic on Thursday where I had proposed a visitor pattern. So that's the thing I want to talk about. And then depending on interest I'd love for a chance to get updates from everyone else. So who's here? And I see Laurent joining us. That's great.
**Laurent Quérel** 03:44 Bye, guys,
**jmacdonald** 03:47 So I can present the notes myself. If you'll give me a moment.
**Drew Relmas** 03:51 Oh, sorry. Yeah, my, it'd be best if you did. My.
**jmacdonald** 03:55 Nothing's easy, I understand. I'll be right there.
Ugh!
Okay, my browser is crashing. So just hang on.
That was fun just a moment.
Nothing is easy.
Oh, yeah.
it's gonna take me a minute, guys. Albert, would you like to lead a conversation about everything you've learned about visitors, and then we can ask good Karsh what he thinks. He showed me a great demo yesterday. I'll find the notes.
**albertlockett** 04:58 Yeah. Sure can. Can you guys hear me?
**jmacdonald** 05:02 Yep.
**albertlockett** 05:03 Okay, cool. So yeah, so I think. Last week during the same talk, we had an interesting discussion around the visitor pattern. And there were some, I think, legitimate concerns that were not
may maybe concerns is too strong a word, but I I think an opportunity for optimization that was brought up where? We thought, hey, you know what with this visitor pattern, we're making a lot of function calls. We're doing a lot of stack allocations. And
Another thing that I found, at least from working with the visitor pattern was that
as as you try to implement a visitor. And and I. I created a thread about this in the Hotel Arrow dev Channel, and perhaps I wasn't using the right pattern. But like you kind of. You sort of have to make these assumptions around
like how the traversal works in that struct that dictates at least in my understanding the internal state of your visitor. And so
you know, be based on some of those concerns Laurent did some work last week to come up with a different pattern, where we have a
a series of traits. And those traits represent views on the underlying hotel data. And so in the context of this view pattern we think about the context of quote unquote back end, or like an implementation of that view, and that back end could be the the the
the open telemetry. sorry the-the- the
we call it the the Grpc. Object, the the process object. It could be a set of otlp bytes it could be a
Syslog bytes, for example. And then we just implement these views which give us access methods into this Otlp data. And we can then inspect things like you think about it from the context of logs like the resource, the scope, the log, the log attributes and and things like that. So we've had a few
iterations of the view pattern. And sort of how we want the traits to
how we want the trades to be structured in terms of things like things like lifetimes, things like
the the
Sorry and then so anyway, I guess, like what I've been doing is is trying to take the the proof of concept that Lauren did of the view interfaces. Bring that code into
O tap data flow and then use that the implementation of those views backed by the prost
otlp structs to encode otap
record batches. And as I've been going through that, I've been like kind of it's, I think it's shaken out a lot of some of the finer points around these views in terms of like which method should return optional, which message should return? Struct. And and so so I'm kind of in the or sorry which which
which method should return results. And I'm kind of in the process of like going through that right now, and I know that
good Karsh, and Lauren had a
Had a had a conversation
earlier this week, or maybe it was Friday where there was some feedback around. How we can optimize the
the definition of those view traits to
essentially rework the ownership model to to optimize performance. So I'm gonna try to be incorporating those into my work.
As well this week, and I should have a Pr up later this week. Based on network.
**jmacdonald** 09:51 Cool. That's great to hear. I knew a lot of that story so I'm looking forward to hear it, seeing the iterations and the the developments that have happened.
And it sounds like you will have
prototypes or or tried to implement direct from otlp bytes to otap frames.
and I know that Udkars has also done a little bit of work on this, and I'd like to give him a chance to speak because I was enthusiastic about the results he shared with me yesterday, and I'd like to to see how they fit in with your thinking. Could you say something Ukash?
**Utkarsh** 10:27 Yeah, for sure. So yeah. Friday, Lauren. And I had a
chat about these new view based traits.
So
I was just curious to like. See if I can implement something like, basically, I, I tried to implement it for
parsing Otlp bytes directly
So I wanted to have an implementation that can pass Otlp bytes. Directly I I 1st tried it with the prospects, and that was a little simpler, because, yeah, you have the data self. Everything is contained well and like it is easier to implement the trade for the process. But
for I would have to do this for Syslog. But I thought, maybe let me try it for the Otlp bytes directly. If it works for that, then it's definitely gonna work for Syslog, because it's much simpler. So I did that. But then, when I was using the 1st iteration of the traits, I found that
the trade type definitions. The associated type definitions kind of forced me to keep the underlying
children data contained within me. So like, if I'm implementing the Uber level logs, data trait. Then I was forced to keep a handle to all the resource logs. Resource logs, implementer, view implementer would was forced to
can contain all the scope logs, and so on. So that basically led to more allocations and was getting
close to, or actually like, little worse than, the prospects based approach. Because I think frost people have used quite a bit of optimizations in their code.
which I hadn't. So I just wanted to try like a more
lazy like us, like a more like a stateless parser, which doesn't have to keep
all of these accumulate all the children information. So I wrote one way of like doing that, basically passing Otlp bytes into
something consumable. It wasn't implementing. It couldn't implement the 1st iteration of the traits. But it did offer its own methods of consuming like, get resource logs, get log records, get scope logs and so on.
And yeah, then I reached out to like all of you about what I had, what I had seen, and I think last night Laurent.
change the traits again change the associated type specifically, to which allow and I think I've I've noticed that he has already implemented it for passing the bytes directly. So I guess, implementation wise. There's no issues. But
then, today I was trying to see if I can consume these views in a simpler manner, like similar to how?
We have some existing methods on the report that Laurent shared so like basically like counting logs printing them or whatever.
And there I found that we are again running into some kind of lifetime issues, but might be that I'm
not iterating over them correctly, or
something like that, I can. Yeah.
But
but at least implementation. I think what we have the good news is that you can implement like a very performance, 0 copy 0 allocation.
Way of parsing the Otlp bytes and have it implement the viewers implement these traits.
Yeah, but the consumption point. Maybe we can tweak it further to like fix that.
**jmacdonald** 14:02 Cool. I'd like to hear Ron, if you have anything on this topic.
**Laurent Quérel** 14:07 Yeah, I think it was a very interesting set of iterations.
Starting from what you did, Joshua.
Cause. The original idea is is coming from what you did, basically
what we are trying to achieve. And it's not easy if we want to combine all the constraints
and the and those constraints will be making sure that we have an approach that is close to.
or as as good as, or close to, what you could do manually. If you have to decode. Xyz.
Representation of an Otlp project, an Otlp object into what we want to manipulate internally.
Which is otap oriented
batch of information. So the
for that we we absolutely need to for protocols like C slog, cf, or
protobuf, the wire representation of a Protobuf message.
Ideally, we need to pass that one in one bus and and and minimize
it ideally in a lazy fashion. So if you want, for example, just to compute the number of logs into a batch
you don't necessarily need to pass
the interior of a log. All the attributes you don't really care. You just want to determine how many logs you have. So that's the kind of goal that we are trying to achieve
and
having or ending up with the right set of traits that combine all those characteristic. And optimization. Is not that easy? I think we are very, very close.
I'm I'm relatively confident that we will end up with a solution that will.
like like Utkart, mentioned. The the last iteration, I think, is working for every back end model
does not require any allocation on the heap
and could work also with a lazy evaluation, sometimes with some effort, obviously depending on the the nature of the back end. But it's it was expected
now, the I think the the last missing piece is
making sure that this infrastructure of trade that follow basically the the data model.
the logical data model that Otlp, open telemetry is defining. Logs are defined this way. Metrics are defined this way and so on.
The the last piece that is missing is making sure that we have a way to express algorithm
that will consume those trades, and that will be generic over any backend that boost right implement
and so I didn't have any time today to to look at the last feedback that Utkarj sent us this morning.
But I will do that tomorrow. Later today, again, I'm too busy. But I will
do that tomorrow, or depending. If Albert also found, or would catch, found, some solutions, maybe that I will not have to do that, but
that the the last missing piece, because at the end of the day. What we want the for me, the the ideal situation will be the following, because those view mechanism could be used in 2 main places
receiver side or exporter side. So receiver side.
We have Otlp Otap, Syslog, Cef, and maybe some other type of data model protocols
that could be translated into an Otlp model.
The views will be there, and we will create some specific implementation to expose any of those external data model compatible with Otlp
to something that is consumable with exactly the same trait.
Then we are, we will write algorithm, and the main one will be a conversion to a tap.
So if we have, if we are able to achieve that, we will implement one time
something able to create otap records.
and it will just be a matter of creating this adaptation layer. And that's it. So it's a huge, huge simplification, because
like Joshua knew. And like Albert, knew, the
the tap data model is not that easy? Learning aperture is not also that easy, it's relatively
involved. So having a generic algorithm already in place.
and and because we are leveraging the monomorphization mechanism that the rest compiler is able to provide, we'll end up with a very efficient translation mechanism.
where basically all the override will be ideally removed, and we will end up to something very close to the best manual transformation that we could imagine. That's the end goal on the opposite side. We could totally imagine
to map and to tap record to this set of traits.
and then we will write values
transformation in the opposite direction. So we could imagine that if we have those traits in place we can navigate them and recreate very easily a representation of a protograph message
that so it's really a trade that could be used in in various places for for this different transformation.
**jmacdonald** 20:37 Yeah, I'm on board with all this. And of course, that's kind of where I was leading with all that visitor stuff. In the 1st place, I'm so glad to see it come out more efficient.
and I'm of course, more kind of rust idiomatic. And the the lifetime question I knew was going to be tricky. The thing that I'm I I would like to. Maybe one more moment of talking about is
So Protobuf has this like
kind of nice feature, 1 1 of the features you can take advantage of, which is that you can concatenate 2 Protobuff messages. So you have a byte array of one you have byte array of another. You have. Now you have a combined protobuf, and the semantics are well defined. Such, especially when you have only repeated fields at the top level, which we do have. So
if you take a logs, data.
or export logs, request, and you concatenate it with its neighbor, it will still form a valid export logs, request
And so I'm thinking about this like sort of like trying to get towards that ideal which Laurent mentioned is like. We only want to parse every field of the protobuf once, because it's literal work to pro to do the variant decoding. It's worked to to measure how wide each integer value is, and so on.
And if you have to do that twice or more, you're going to end up paying for it. And so here's where I'm like making like propositions, like, I think that most algorithms that we have for these are going to
pass through the data once, so that if we are able to
have a essentially a 1 to one, to one equivalent one to one correspondence between visitor action and field. Then we ought to just synthesize the values on the fly. Like as you're iterating, you're producing a value, and it should be very efficient. But there will be sort of 2 cases. There's a like normal case, I think, where.
if there are a mixture of repeated fields and
and not repeated fields. Now, it sort of depends on the order of the algorithm like, which field order am I going to access this struct in, and you know it won't necessarily be in tag order, and tags are just arbitrary. I can look at the I think most Otlp encoders put them in tag order when they output the data. But there's no requirement to do that, especially because you can concatenate them.
And I. I haven't gone into back in my head. How many Otlp structs have more than one, repeated Field. Because that's gonna be relevant to us. I think because, Mo, the common cases that you have at most one, repeated Field, and then you might have some optional
struct members. So then, the back to the kind of question, what we want is to the most efficient possible is that we only decode each field once.
But what happens when the view asks to iterate through the repeated field before looking at all the other optional field members such that you might have to skip past some stuff
before you get to the 1st thing in the view. Now you've skipped past some stuff, and I'm and this is where this morning. If Karsha and I were chatting and I I like I love this problem. I would love to sync my day into this problem. But I want you guys to do it. I think there's some sort of like algorithm with the amount of space proportional to the number of tags that might might work. And I want us to think about the common case, which is not
having to support not, which is, is that the common case is that you had one object, and you encoded it once, and you have all of your fields contiguous in tag order
and then what we can do is in that. In the Otlp model definition for P data we can actually like
define the order of tags
so that you get the more optimal traversal in the natural field order. So we could go looking at like the real algorithms, mainly the one that produces otap
and
and like, we can figure out what's the most efficient order to present fields for the otap conversion, and then maybe go, have our encoder produce that same order so that we get a better, more optimal traversal.
you know, like, for example, in a tray in a span. I'm probably gonna look at my trace id 1st my span id like, but it's not tag one and not tag 2. So like I'm gonna have to skip over a bunch of stuff before I get to my trace. Id. Maybe that's the kind of thinking and then I imagine that in the common case, all the repeated values are going to be adjacent, so that might simplify some stuff.
But if there's a mixture of repeated fields and concatenation
which I don't believe ever happens at the top level.
so it's unlikely to happen in a nested field, but not impossible.
Anyway, you hear me.
**Laurent Quérel** 25:28 That's what I wanted to bring up.
I was thinking about what you just described, because if you look at the advantage and disadvantages of
the visitor pattern and the view pattern
on one side, the visitor. You could enforce the
you, you could basically use what you are decoding as the the driving mechanism to define in which order
element into your visitor will be called
because you don't. You don't basically guarantee any specific order with the visitor.
So that's very well. So on one side, advantage, side
advantage side. It's very friendly, friendly for what you are decoding disadvantage. The
the implementer of the visitor has no controller
which make this implementer potentially super hard or hard to implement. Because you, for example, I was thinking about converting that into a tap.
Fundamentally, the otap representation is is done differently. It's multiple, like multiple tables
like relational tables. And and we and we generate columns.
And it's not necessarily following the way that the information will be stored on the wire.
So that means that you have to do some mechanic or gymnastic to in your the implementer of this visitor to to work properly at the end
as opposed to so. But but the benefits is, it's friendly for the the, the passing
for the for the view. In fact, we inverse this proposal, or the advantage or the disadvantage of the other one advantage in that case will be, the control is in the end of the implementer of what you want to convert.
but, like you said, bytes are ordered in some way, and and we don't control it. So maybe we will have to memorize
a set of offsets, of seeing that we skip
in order to provide the right information when the implementer or the the not the implementer. In fact, the user of the view will ask something. It's not necessarily the next thing into the the binary representation. So we need to keep track
of those printers somewhere in order to be able to go back efficiently.
And I think, in my perspective, I prefer to put
I think it's not that complicated to maintain this type of array of set and let the the user of this view mechanism decide in which order they want to
to achieve the the traversal of this infrastructure for this data model.
I think that it's working well for everything that is memory based or even file based. If we have a way to go back in in. So some kind of file where we you don't. You can always go back, you you have an upset mechanism to move
forward and backward. I think that's that's not a big deal. The only issue will be some kind of
back end where the the back end does not give you a way to go back in something that was read before. In that case you have to
to memorize or to authorize everything in order to be able to go back.
I don't think we are in this situation because most of the time we are talking about array of things
of U. 8, and and we can always go back
**jmacdonald** 30:06 Cool.
yeah, do you? Do you see a difference between like a 1 pass and a multiple pass like for the Otap construction algorithm. Do you need to
it?
I'm trying to figure out if you need to save or memorize this table of offsets. In order to return to it, or whether you only need to save this table of offsets for things that you've skipped, that you might pass through
in a different order.
**Laurent Quérel** 30:34 Yeah, I think, depending on
like, like we we discussed before. I think there is 2 main usage of this view pattern, either. We want to convert
Otap C slog cf to a tap. In that case.
I don't see. I don't think that we need any multiple pass.
We we we probably need in that case to memorize offset
of things that are not already interpreted
because we skip them to read something else.
So in with the last situation of the view we have now strict that are right now, usually just a reference and offset could be a little bit more complicated if we want to achieve what we I just explained some array of offset that could be maintained in order to go back in the memory layout. Now
we could we could need. I mean, maybe we need to pass for the other usage of views. We have a tap, and we want to convert that to a protobuff wire representation.
Then we need to count to determine, because we, when we have to store a repeated field. We need to put
the number of elements of this repeated field, if I remember well. First.st
**jmacdonald** 32:14 The size of.
**Laurent Quérel** 32:16 Yeah, the size. So it probably means that we will have a way to traverse the this view
that we we put in in front of the tap representation of the attack back end 2 times one to get to compute the size and one to really leverage the site that we
we are, we are maintaining in memory. And then we start to write on the wire, the, the.
the combination between the tags, the size.
**jmacdonald** 32:53 Right.
**Laurent Quérel** 32:54 And the real value that we want to store.
**jmacdonald** 32:56 This is an interesting.
**Laurent Quérel** 32:58 Yeah, I think that's only on this case that we need a to pass algorithm.
But for the other one, I'm not sure that we need. It will be more a set of upset that we have to maintain. But.
**jmacdonald** 33:09 Gotcha.
**Laurent Quérel** 33:09 If you, if you think about it, I think
it's a little bit of complexity. But the win for us will be
potentially super important in comparison with the traditional way to do that where you use
prost, or whatever protobuff system you use, you create the intermediary representation object oriented like a graph of object. So it's a lot of overhead that we can just bypass by a such approach.
**jmacdonald** 33:43 Right. So that's where I'd like to to get us back to. And I I will, as I was saying, try not to think about it and let Albert Nukash and anybody else think about but
I had implemented, as I was saying, this sort of 2 pass algorithm at least like it was implemented. It didn't look efficient, but but but as we've all seen at this point, the cost of encoding prost is actually less than the cost of decoding prost, and that's because you have to allocate a bunch of vectors and small objects to decode from bytes and my benchmarking, since I was working on the encode side
actually was competing against the more efficient thing that prost can do which is to just output bytes. So in that measurement, what I noticed was that my code was inefficient. So constructing that single vector of view size values, even though I could reuse that vector again and again, and not allocate was quite slow. And I think that was just an artifact of the visitor pattern itself.
But what I'm hearing. And maybe you guys can think about this is that.
like in this description of a view mechanism that has some sort of caching or memorization built into it.
the the to pass algorithm of Otlp.
Might be just look like one pass, because you're going to to compute exactly the informations that we've just described, which is offset in length.
For each nested object. So if you've computed lengths
for all the objects, then perhaps we can
make a 1 pass Otlp, encoder out of it.
And it seemed like a potential
like, you have to count the cost of decoding in this into this equation.
In other words, prost is actually very fast at encoding, even though it's doing something that looks inefficient, which is to calculate the the sizes twice.
It's doing it really fast. So it's still was still beating my approach, maybe with a view and all the correct optimizations. You know, Albert or Ukarsh, working together can figure out how to make that fast.
**Laurent Quérel** 36:04 Yeah, and and
and we can also learn from what process is doing. Maybe I mean, I didn't. To be honest, I didn't look precisely on what process is doing to make that fast.
But we we, I think it's or a TV.
**jmacdonald** 36:22 It's doing 2 passes in some sense. So I guess you could call it a log N log, N type of algorithm, because at the top level. You're going to ask the length of each child, and then you're going to go to each child. It's going to ask its length of each child, and so by the time you get to a leaf, you've been asked your size 3 or 4 or 5 times, because the depth is 3 or 4 or 5
and that on paper is inefficient, but it's doing everything on the stack in a very quick way, and it comes out like really fast, so maybe there's a way to beat it where you don't compute the size N. Times for N level steep.
but it has to be done very efficiently to beat prost, because it's just a it's just optimized. Very well.
**Laurent Quérel** 37:03 Yeah. And I I expect that we we could.
during the next, let's say, 5, 6 days we will have some.
I mean a more, a better idea on where we would end up with this approach.
I I really feel optimistic.
Sorry. Go ahead.
**jmacdonald** 37:30 I'm saying I'm optimistic from what I've seen, just from the rough numbers that I've seen from myself, from Ukarsh, that we will get to a place where decoding from Otlp bytes to otap is
within range of what we want to see. It's definitely faster than converting to otap bytes or Otlp, but Otlp message objects, and then to Otap. That's.
**Laurent Quérel** 37:50 Yeah.
**jmacdonald** 37:51 Win. So I think we're gonna be okay.
**Laurent Quérel** 37:53 Yeah, I think if we, if we, if we reason about the the end to end, approach
and eliminating all these
temporarily creation. I don't see why we will not be able to to beat this. I mean.
yeah, I really think that when you combine everything together
because we know that we want to to process and transport the information in what type representation, for all the reasons that we already discuss
so and then we should be able to win in terms of data processing speed.
So, being able to optimize, this conversion will be a second win, and when you accumulate them. I really expect to see
a major difference. Obviously, that right now it's only worlds. But I hope that let's say, in few weeks we will be able to to make some demonstration of that.
**jmacdonald** 38:58 Excellent I have no more to say on that topic. I would like to hear from Mukash. As I was saying, this is a fun topic. I need to not think about this
less fun.
**Utkarsh** 39:08 Yeah, I was thinking more about, like, I think, prost. I'm not sure but I I believe they are. Also. They freely use unsafe when accessing
arrays randomly right? So like the they don't probably have to pay for bounce check, and I don't
know of what our stand is on using unsafe. We probably don't want to use it. But yeah, I mean, like those
optimizations could also like add up to like at least some improvement, I believe, because we are accessing these, this byte array a lot of times just randomly accessing the indices. So
yeah, that was just one.
**Laurent Quérel** 39:49 My philosophy on that is, we. We don't
try to use unsafe first.st I think we could achieve something with reasonable performance.
and and we have enough tests. We have enough integration to check everything. And then, if really we see
some slowness, then we can spend the time to to identify where we have to to use unsafe.
or like removing the, the, the checking on the the array boundary or the slice boundaries.
we we can, always we. We know that it's always an option. I'm just saying that we we should not go there first.st We just have to be
to observe where we really have issues and only optimize this kind of thing based on observation.
**jmacdonald** 40:48 This reminds me that I had this debate with my old company about the rust
gross tonic receiver for Oclp, which I believe uses unsafe to to assert that the data is Utf-eight valid.
which is a nice savings and.
**Laurent Quérel** 41:06 Oh, yeah.
**jmacdonald** 41:06 Always safe.
And this was why they were so upset by it was like the the like.
I basically said the go, the the go collector can produce this condition that you will then unsafely propagate. And
it's a touchy subject, is all I know. Rust people like to pretend that. Never mind.
**Laurent Quérel** 41:26 Yeah, yeah, I remember that. I think go does not check etf suite at all anywhere.
**jmacdonald** 41:32 It's a i believe there's an option now, the last time I looked but it's not enabled. And so you can definitely get into a situation where Otlp, receiver on the collector, takes in some data that was malformed and then passes through, and
you get to a protobuf exporter, which will then
has an option, but it's turned off so it will pass it through, and then you get to a rust receiver which now is holding an invalid. Utf. 8. I I know it's possible, but but the exact.
**Laurent Quérel** 41:59 We. We had this issue together. If I remember when.
**jmacdonald** 42:03 Yeah, that was definitely a thing that we've seen and go. And I was. I had to at at the old Company. I had a thing called sanity processor, which was just a hotel collector processor that would just force all the Utf 8 valid strings to be valid.
is so that you could overcome the the typical case where there's like a tiny little string that was make like 2 MB of data drop
**Utkarsh** 42:30 So like again, if like, if we hadn't
a receiver. That just depends on prost for decoding, I guess. A few things that get simplified that way is, I think I mentioned this earlier, Josh. Yesterday when I was chatting with you like if somebody sends us a malformed request
right like. Now, if we are manually deserializing it.
Is there a way for us to avoid deceitalizing the entire pipes payload
and still know that it's malformed or like.
like, basically, would it always force us to
do you realize the entire payload
like basically everything, not just the offsets and all but
**jmacdonald** 43:16 I see. So this connected with my statement about sanitization, like, if you're not parsing the whole request and you're still passing it through, are you
culpable for downstream errors? Maybe you should. You have been sort of severe, like pedantic, you might call it.
Is that the type of question.
**Utkarsh** 43:36 Yeah, I mean, basically, like, if a user sent you
something alleged like invalid, send them a 400 and let them know rather than
yeah, accepting it, giving back a 200.
**jmacdonald** 43:51 I guess what I was imagining was like, you receive some bytes, and then we have these fancy adapters. All you want to know is, how many items are there? You don't want to parse the object. So you run your visitor.
Your visitor only goes in as far as counting the objects. But inside of one of those objects you've got attributes with invalid Utf. 8. You won't see it. You'll skip over it because you just wanted to count the the log records. I think that's okay.
I probably there's a topic we could break off and like
I could go update an old otap actually where I tried to write down the hotel. What opentometry does in this situation? It didn't. It didn't go very far, but I did once write this down and look at the issue.
For utf 8, specifically.
But I don't have a problem with us. In fact, the the topic as debugging libraries as instrumentation authors as telemetry, SDK, providers, protobuf that are
corrupted often through truncation are like exactly the ones you want to be able to read in your like.
You know, like.
point is, I've seen it before is, you've got a data stream that gets truncated. And you know, it's protobuf data. And you'd like to just like, get as much as possible out of it.
Having a like less strict parser or view implementation is actually very useful.
Right? So otherwise targeting protobuf is hard.
**Utkarsh** 45:23 yeah, just something to keep in mind. I guess. Like, if we differ from the go based collector in terms of behavior here, like
I.
And then there's also, I think, man with manually deserializing payloads. There's always the
the security vulnerability stuff that we might have to focus on, probably like the size of payroll, and like deep recursive structures, because I know our attribute
takes any value, and any value can just like be a highly dp nested stuff.
So I think, yeah, we should be able to like impose some kind of limit on, like, how much we want to recurse. And like.
prevent ourselves from like stack, overflow, and all those things. But just some things that we'll have to be extra careful of.
**Laurent Quérel** 46:10 A question for you, Joshua, you know, in reaction to some element that would characters mentioned.
I believe. But you know photobirth more than me. I believe that you can take any photobirth message
and replace the definition with a byte field.
and then you will be able to use this message in place of the the previous one, except that you will get
the byte representation of the entire message just because everything starts with the lens of everything that is nested.
**jmacdonald** 46:54 Correct. They're wire compatible. You can field.
**Laurent Quérel** 46:58 Okay. So that mean that we we could
and in fact, I think
independently of what we do. And I really think that we, we should go either with a view or derivative of the view, or even go back to to visitor if we need. But eliminating all these intermediary steps.
but in terms of integration with tonic
which is well integrated with prost.
We could imagine that we expose
the the values Otlp Grpc. Based endpoint, and instead of
giving the the Portobuff message definition defined by Otlp, we just define our own things that are basically a single field message with the Byte.
the benefits will be.
First, st we have a very easy to to determine
way to compute the size of what we receive, which which will be super important to implement admission control.
Because if we keep what is on the fly in terms of data processing
in order to to maintain a reliable data pipeline.
We, we know the that we have some limit, and and we need to be able to accept or not what is coming. So having this approach has 2 benefits. So first, st we can
use the view mechanism because we can interpret this byte, and we are not complexifying too much the the way that we are using tonic.
And we have a way to compute any input
very easily, because it's just a slice of bite.
And we can just apply the lens method. And and then we, we can determine, determine, based on that if we accept or not this incoming message.
and then.
**jmacdonald** 49:16 So.
**Laurent Quérel** 49:17 Interpret it with prost, because prost can take this binary. And we use the real message. That's 1 way, or we can use the this view mechanism in order to generate directly a tap, but.
**jmacdonald** 49:31 Yeah. Many a Rpc Grpc implementation that I've seen would actually have a like a raw
Rpc method, where you're basically just getting a bytes, and that's how the middle Grpc. Middleware is implemented by that, I think.
So if you just want to pass through a completely opaque request, then you can just get. Usually you can get that from the Tonic library, maybe, but but from the Rpc library.
The technique that you described is often used when you've got some portion of your structure that you want access to as a protobuf. But then the rest of it sort of don't care. Pass through. So you could imagine having the log record be
just that, or
but you can't do it at the top level, so it has to be the the field. So so at the top level of our Otlp request, we have the export request or the the data object which is repeated, something so you could replace that with repeated bytes and then you would just
parse one level of protobuf object instead of parsing N levels deep. And it reminds me that.
you know, if you're only
for some traversals, and I haven't identified carefully which ones they are. But but I would guess that some of them are
equally efficient if you just treat each field that's not primitive as bytes. And then
you know how to create a child view for those bytes, whether it's the the message type.
It has to be the appropriate message type. But, in other words, that the you could construct a view mechanism where each field was either primitive or bytes, and then you would use the child view type to interpret child messages and so on. That might be efficient. It's worth looking into. It. Probably.
**Laurent Quérel** 51:15 Yep.
**jmacdonald** 51:19 Cool. Well, that was a long conversation about views, and I wanna probably stop here.
As far as
who's on the call and other topics that might be available for us to talk about. I wanted to take the
chance to ask the room they would like to raise anything. I.
And because I'm projecting, I'm having. Okay. So it's still the 6 of us.
At this point. It's just the 6 of us actually according to this true
David. Would you like to raise an agenda item? Since the rest of us it's 7 of us right now.
I've had a long chance to speak.
**David Dahl** 52:11 I'm just a fly on a wall tonight. But thank you.
**jmacdonald** 52:15 Well, train a lot.
Yeah. And I'm I've I've had the ambition to kind of bring up other kind of projects that have our ongoing and experimental, and but I don't want to put you on the spot either, and also we're really close to the end here, and I wouldn't wouldn't mind just calling it if we're here at the end of the meeting. We're here at the end of the meeting.
**Drew Relmas** 52:34 I think I wouldn't get into it today. I would think, Josh, we should also have.
Michael, you know, in attendance if we wanna talk query. So maybe next meeting would be good. I'll I'll chat with him.
**jmacdonald** 52:49 And, Jake, I don't want to leave you out. I know you have interesting ideas and things, probably responses here, but but you also might just want to listen and tune out. So here we are at the end of the meeting. I think.
**Jake Dern** 53:03 Yeah, no, nothing for me. Happy to just listen in.
**jmacdonald** 53:07 You're always welcome to. And thanks for for being here. Okay, everybody we did. It had a meeting next time will be Thursday in a week in a couple of days, and I look forward to hearing more on slack.
Everybody should know that there's a thing going on with Slack.
It just looks like Cncf. Is going down to downgrade to a free plan which I don't think will affect me very much, but it might affect the org. We might switch to discord.
Leave, leave me out of it. I'll be there.
Thanks, and have a good night.
**David Dahl** 53:38 Good night.
**Laurent Quérel** 53:39 Yeah, and they.
**Drew Relmas** 53:41 Bye-bye.
