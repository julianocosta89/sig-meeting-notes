SIG: Arrow SIG
Date: 2026-04-01
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 01:12 Hey, Mike.
Hello?
**Mike "Blanch" Blanchard** 01:19 Hey, Albert. Sorry, I was on mute.
**Albert Lockett** 01:22 That's what? How's it going?
**Mike "Blanch" Blanchard** 01:23 Good. How about you?
**Albert Lockett** 01:25 Yeah, pretty good. Yeah, pretty good.
Just ran out of, context, talking to Claude, so… Shit. I'm stuck.
No, I'm joking.
Yeah, so, did you have anything, you, you wanted to start off with this week?
**Mike "Blanch" Blanchard** 01:49 Nothing in particular. We've been kind of busy internally getting ready for, like, a release.
So I've just been… Doing some random things, not focusing so much on… columnar and what I want to be doing.
**Albert Lockett** 02:07 Yeah, yeah, yeah, yeah, no, totally.
Sounds good. Yeah, and so have we.
Not really release, more like trying to, like.
get some… get some work organized so, like, another internal team could start trying out, Motel Aero. So, Yeah, so I haven't been too, or I've been focused on, like, trying to line up a few… features in the… in the column of query engine, to, like, support that work.
One of them was, to invoke… function calls, ex- external functions. So, you know how in the, in the… in our expression tree, we have, like, our… we can do our… our pipeline function definitions, and then there's two implementations of the body. There's the, and one of them is, like, an external function that has, like, a name.
So, I was adding, basically support to execute those.
And so, like, DataFusion has a bunch of, a bunch of, like, pre-built functions, like, you can do, take, like, the SHA-256 hash of, of, of a, of a string, or, you can take, like, the substring of a, of a substring. So, basically what I did was, like, in the… in the column recovery engine now, we, like, we register those as, as external functions, with the… with the correct number of arguments, and then when we're doing our parsing, you know, in the parser scope, we call, like, get the function by this name. Oh, it's already registered in the parser scope. I'll just create, a function invocation expression using that function ID, and then our query engine will will… will… when it sees that expression, it will say, okay, like, is this a… is this a data fusion function that I… that I know about based on the name? If it is, then I'll create a DataFusion, expression that invokes that, in data fusion, they call them scalar UDFs, so we invoke that scalar UDF, and and yeah, so that's, And that will produce the value for the… for the column.
So, yeah, I was working on that. Again, it's, it's, it's like, it's no, it's no changes to the, to the expression tree or anything to get that working. I was able to use everything that, that you put in place for the, function invocation expressions on the, on the record set engine.
Yeah, and then, today, just, working on another small feature that'll probably be the last feature I, add this week, and that's, To, support the… the case-insensitive, equals operator, so our equals to operator has that case and sensitive flag, and the callner query engine wasn't, respecting that at all, and we didn't have that as something that would be parsed in OPL, so I added parsing support for that equals tilde sign.
And then, and then fix the, the implementation in, in the columnar query engine, that if we see that equals to expression with case insensitive, then we do a case insensitive equals. So that's, that's the other thing I'm working on this week.
**Mike "Blanch" Blanchard** 06:17 Cool.
So you basically, you want to expose these data fusion functions as, like, OPL functions, essentially?
**Albert Lockett** 06:27 Yeah, pretty much. Yeah.
So we… I don't… I don't know if we'll do, like, all of them, verbatim. We'll probably just pick and choose the ones, like, as we have a need, the ones that are… the ones that are kind of, like, sensible. Like, substring is… is a pretty obvious example of… of a function that you… you kind of want.
**Mike "Blanch" Blanchard** 06:48 So there's already, like, a substring… Expression in the tree.
implement using DataFusion. You don't necessarily need to use the external function thing to do the…
**Albert Lockett** 07:02 Oh, sorry, yeah, I guess, and yeah, you're right. So function, function, so a substring is a bad example, actually, because, you're right that, like, we do have a, a special expression for that, and so, actually, the, the, the OPL parser, like, picks that up. It says, like, oh, you're trying to do a function, the function's called substring, I'm gonna parse that into, like, this substring, the substring expression. Just, just so, like, that way, we produce the exact same expression tree that we would with, like, KQL for… for substring. So substring's a bad example, but… Yeah, like, like, I think that, like, we… we… there's… there's some… let me… let me think… so the other ones that I added were, sHOF256Hash, which is a data fusion function that produces a binary array, and then, the encode function, which you can use to take a binary array and encode it as hex. So, those we… those we… we implement as external functions.
**Mike "Blanch" Blanchard** 08:08 What would you do if, like.
The tree came along and decided to have a hash.
function.
**Albert Lockett** 08:19 I mean, we could, change the parser.
change partial implementation to parsed into that, into, into, that, that, Hash, expression, that would be okay.
**Mike "Blanch" Blanchard** 08:37 You might run into issues with, like, parameters… One suggestion you can consider would be prefix all of these with, like, DF underscore.
So you have sort of… There's OPL, and then there's these Data Fusion extensions.
Prefix being a way to make sure there's no collisions with future stuff.
It's up to you.
Fruit.
**Albert Lockett** 09:10 Yeah, we could do that. We could do that… S… yeah, we could do that.
Yeah, so… Yeah, we could do that.
**Mike "Blanch" Blanchard** 09:28 Are there a lot of them other than the hash?
**Albert Lockett** 09:32 Yeah, I mean, there's quite a few. I can… I can post you the list here, and like I said, I don't know if we'll do necessarily all of them. Some of them probably aren't super useful in the context of, of, of telemetry transformation. Let me just see if I can pull up the list here.
Yeah, call, like, so, like, calling them DF underscore is… It's interesting, because it, like, that's interesting.
Because you're right, it stops us if we, if we, like, if we come back and we modify the exp… let me just post the list here.
So it's, it, it, it, It helps us if we come back and we modify the expression tree so we don't run into a situation where, Oh, we added a hash expression, but now the arguments are different, so that… because that wouldn't be, that wouldn't be cool.
**Mike "Blanch" Blanchard** 10:32 I was just looking at KQL, it has, like, a whole bunch of hash-related… There's, like, a generic hash scalar function, I don't know what that does. There's a hash combine, hash many, hash MD5, hash SHA1, 256, XX hash 64… So, I mean, it might be reasonable that… The expression tree at some point gains hash.
I'm just leaning on, if it's in KQL, it means it was useful to some set of customers.
So I anticipate, you know, as our users start getting ahold of this, you know, they'll start asking for this crap.
**Albert Lockett** 11:18 Yeah. Yeah, yeah, yeah, yeah.
**Mike "Blanch" Blanchard** 11:27 That's sort of the balance that… Drew and I have to find is, like, you know, there's… there's many, many, many, many, many KQL scalar functions.
But we don't want to just go and start blindly throwing things in there. We kind of want to wait for the customer feedback.
engage demand for things. Just sort of what we did, like, in OpenTelemetry.net. We would… You know, somebody would ask for something, we'd put an issue out there and say, if you want this thumb, do the thumbs up or reply, and we would just sort of pick things that had a sufficient level of demand.
**Albert Lockett** 12:08 Yeah, and I think that's what I'm, like, what I'm trying to do, too, here, right?
I mean, we had a demand that I thought was pretty reasonable from… And you just say, like, hey, you know what, as I'm trying to redact, maybe an attribute value, I want to assign it to the hash of the value, so the value becomes opaque, but, I can track and say, oh, well, geez, you know, I'm using this, this value appears all over the place, or, you know, or something like that, right? So, like, that, like, anyway, I say that because, like, you know, you can look at this, this great big list of, like, all the data fusion scalar functions, and we can say, oh geeper scrapers, you know, we're… have so much opportunity to go throw them all into, into, OPL.
But, But, but, you know, my intention, I don't think, was necessarily, like, to just jump in and do that straight away. It was more to, to kind of, like, as… You know, as needs arise from users, to say, okay, you know, we can support that through this, This function or that function, and so that's what we'll do.
**Mike "Blanch" Blanchard** 13:25 I kind of intended the external to be more… So we have, like, our record set engine.
That we can run.
in the Arrow Collector, we can run it in the Go Collector. I have some other team in Microsoft that wants to use the engine and the tree in some completely random agent. It's not doing open telemetry, it's doing whatever their data is.
And they wanted functions like DNS lookup, There was some other one.
And we're just like, no, we're not ever gonna have DNS lookup.
in the record set engine. But… We can give you the way to… For your customers, in their… queries. When you're parsing them, you just seed the parser with that external function, and then when you mount the engine, essentially, you just implement DNS lookup however you want, and then that function just becomes available to all your customers.
**Albert Lockett** 14:28 Sure, but could you not also make the same argument the other way, though? That, like… like, oh, well, like, what if one day we have a DNS lookup, like, expression?
**Mike "Blanch" Blanchard** 14:40 I just don't think that would ever happen.
**Albert Lockett** 14:42 Okay.
**Mike "Blanch" Blanchard** 14:43 Just because…
**Albert Lockett** 14:44 So, Dan.
**Mike "Blanch" Blanchard** 14:45 NSLookup involves, like, network. I mean, there's… it's just a whole can of worms.
**Albert Lockett** 14:50 Okay, yeah, sure, I guess so, but, like, from my perspective, like, I'm trying to figure out, okay, so, you know, like… Like, these things… when we write the expression for them, they… they, they look like functions.
you know, you can picture, like, a hashed… as a… as a function, so… so I guess, like, what I'm trying to figure out here is, like, like, where, you know.
like… Like, how… as we try to, like, add more, you know, capabilities going forward, do we lean… Like… I'm looking for guidance on, like, does it… do we lean on the side of, like, putting these in the expression tree, or do we lean on the side of saying, you know what, these are just external functions?
**Cause, cause, cause… Mike "Blanch" Blanchard** 15:50 I don't know if I have a rule to follow. I mean, I would…
**Albert Lockett** 15:54 Yeah.
**Mike "Blanch" Blanchard** 15:55 I would look at KQL, just personally, I would say, oh, okay, it has a hash function, so if somebody asks for a hash, my bar for, like, accepting it would be lower than if somebody comes and asks for something completely out of the blue that KQL doesn't have.
Because KQL has been around for a long time, and has many different people using it, so I feel like it's… It's had all of these requests already.
So, like, hash for me, I would have no problem adding hash into the tree.
I don't know what other ones you… you sent, but… If it seems generally useful, like, I can see how people would want to compute hashes.
Of course, the question would be.
you know, right now, you have SHA-256, Is there still a… spot for MD5, are there Shaw 512s? You know, is there gonna be some… quantum hash thing that comes along, so I would just make sure that there's a way to either specify the algorithm as a parameter, or have it just in the name, and you just have different expressions for the different hashes, but… Conceptually, that idea of supporting hash in there seems reasonable to me.
**Albert Lockett** 17:10 Okay, yeah, so… Okay.
**Mike "Blanch" Blanchard** 17:16 It's up to you. Like, if you want to just mount it up to the external function, I don't have any problem with that. And then if, you know, Drew and I at some point need hash for KQL, we'll go Do the heavy lifting to build out the expression, and then you could just switch to it if you wanted to at some point.
**Albert Lockett** 17:36 Yeah.
**Mike "Blanch" Blanchard** 17:37 up to you.
**Albert Lockett** 17:38 I mean, I think that's probably what I'll end up doing.
I think that's… I think that's probably what I'll end up doing for now.
Yeah, just cause, like, I mean, we've already got this, this wired up as an external, As an external function.
Yeah, so that's probably what I'll end up doing, is just leave it as an external function now, and if we have a, if we have a hash, something in the expression tree.
Down the line, then, you know, we can definitely switch how it, how it prices… If, if that makes sense.
**Mike "Blanch" Blanchard** 18:30 Sure.
**Albert Lockett** 18:33 Yeah.
Yeah, so that's probably what I'll end up doing.
Just cause, like, that's pretty much what we already had in place.
**Mike "Blanch" Blanchard** 18:54 It's not the use case I had intentioned, but it's… it's fine.
**Albert Lockett** 19:01 Yeah.
I mean, Yeah, I guess.
You know, and I guess maybe, like, from my perspective, I was kind of thinking, like… Maybe we… maybe we had drawn the line at different places in terms of, like, what… what needs to be, internal, what needs to be.
**Mike "Blanch" Blanchard** 19:20 Leo, your engine.
Your engine is completely different than my engine's, because it's already deeply tied to… The collector, the aero collector.
**Albert Lockett** 19:31 Yeah, I mean… Mike "Blanch" Blanchard 19:32 There is no differentiation between the host and the engine.
But it would be very different.
**Albert Lockett** 19:41 I mean, you can understand why, though, because it's, like, it's embedded within the Hotel Arrow project.
**Mike "Blanch" Blanchard** 19:48 Why?
**Albert Lockett** 19:51 Why? Because that's the… that's the project that I'm a maintainer of, that's what I contribute to.
**Mike "Blanch" Blanchard** 19:55 You just don't need the general purpose of it, which is fine.
**Albert Lockett** 20:01 Yeah, well, that's it. That's exactly right.
**Mike "Blanch" Blanchard** 20:04 So… what the external functions, in my mind, are more like. So there's a general purpose tree, there's a general purpose engine.
But if you wanted the arrow users to have a function like getCollectorVersion, I don't know, something that's very specific to the collector, that wouldn't make sense in the expression tree, because it doesn't apply to every potential user In the future, whatever engine, whatever host.
it's an arrow-specific thing. So there's where I would say, okay, you have to use the external function. So when you're running in the open telemetry world, you're parsing the query, you bind the external function, you know, getCollectorVersion, and then in the collector, you implement it with some Rust callback.
So now all the Arrow users have this function available. They don't know it's anything special. To them, it just looks like a function.
But the actual implementation is it's… it's sort of a host function, not… Something part of the tree.
Whereas, like, Shaw, you know, things like Substring, those are, like, more general purpose, which… Could go in the tree, no problem.
DNS Lookup's a strange one, because it's sort of general purpose, but…
**Albert Lockett** 21:29 Yeah, interesting. Okay.
Interesting, interesting, interesting.
Yeah.
Okay, yeah, yeah, yeah, okay, I think I… I think I get what you're saying here.
Okay. Yeah, yeah, okay, I think I get what you're saying. So it's like these, These things that, like, kind of… Like, look-like functions when you call them, like, we don't… we don't parse them all into, like, function invocations. We… we should… we… we have our, Our expression tree has some special handling for some of this stuff that's a bit more… That's a bit more late.
Universally, useful.
Not, not, not necessarily, like, used, like… I don't want to say use case specific.
Maybe use case specific is the right word.
Yeah.
Okay.
Yeah, and I guess that… I guess that makes sense.
Yeah, I was, I guess, like, maybe I was thinking about this more… from, like, the… the data fusion world, because that's, like, what I'm more used to as a query engine, and that… In that engine, they have, like, a very, like, like… thin, set of expressions, and when you want to do things that are, extensions, like, like substring, or string contains, or stuff like that, They all get implemented as a… as scalar UDFs that you have to invoke.
But I guess we're not so restricted because we own the expression tree.
Yeah.
Interesting.
Okay.
Yeah, I mean, so I think, like, For now, I'll probably still… Just leave, That… That, that sh… that… that hash function as a, as, as an external function, and I think it would be relatively easy to… Change going forward, if eventually we did have, a, If we did have a hash expression in our… in our expression tree, and I guess in the future, as we add more capability, we can kind of play it by ear, whether, Whether that's something that makes sense to add into the expression tree, or whether it's something that makes sense to, To keep as an external function.
**Mike "Blanch" Blanchard** 24:44 See a lot of these data fusion.
Functions are also… in KQL.
I don't know what CBRT is.
Let's see that with CBRT?
Cube root of a number, okay.
**Albert Lockett** 25:11 Q.
Cute route.
Jeez, I guess someone must have had a use for that.
**Mike "Blanch" Blanchard** 25:21 Most of them seem they're all, like, mathematical.
Though I'm just looking at the math ones.
**Albert Lockett** 25:28 You'd rude.
Is there a general purpose route? Doesn't look like it.
**Mike "Blanch" Blanchard** 25:37 Scalar functions math. Okay, so that's math, and then there's a bunch more below it, too, okay?
string functions… I mean, just generally scanning this, it seems like.
KQL has a lot of the same… Just little scalar functions.
**Albert Lockett** 26:05 Oh, yeah, yeah.
**Mike "Blanch" Blanchard** 26:09 map function… I don't see anything like… Network.
Which I wouldn't expect out of something like Data Fusion.
**Albert Lockett** 26:21 Oh, yeah, geez, this has a bunch of IP stuff.
IP match.
**Geospatial… Mike "Blanch" Blanchard** 27:22 So anyway, I mean, you're free to do the external functions.
**Albert Lockett** 27:27 Yeah.
**Mike "Blanch" Blanchard** 27:28 I would just say, if there's a particular thing you want, you see it's in KQL, I would be supportive if you just wanted to go and build something in the expression tree, but if you don't, you just want to stick with your external functions, I don't have… I don't have any problem with that.
**Albert Lockett** 27:44 Okay, yeah, yeah, I mean, I think going forward, I can use that as a pretty good rule of thumb to say, like, in terms of, like, trying to figure out where to put it. So, yeah, that's what I'll continue to do.
**Mike "Blanch" Blanchard** 27:55 Sounds good.
**Albert Lockett** 27:55 Yep.
Cool.
**Mike "Blanch" Blanchard** 28:00 Alright, get to it.
**Albert Lockett** 28:03 Get to it. Yeah, it's, get to it. It's April 1st, so I don't know what that means for your taxes, but I hope that they're still going okay.
**Mike "Blanch" Blanchard** 28:16 They sort of are, my… like, how it works, like, I had to… I did my meeting with my, like, preparer.
And then she sent me, like, the stuff I have to, like, sign so that she can file, and then I have to pay her, and then she sends me all this stuff back.
So I've been waiting for it, and I eventually, like, text her, like, hey, are you ever gonna send me the packet? And she's like, oh, my husband had emergency surgery.
So, I think that the deadline here is the 15th of this month, so I have a couple weeks, but I'm starting to get a little nervous.
**Albert Lockett** 28:51 Oh, man.
You can't have emergency surgery during tax season.
**Mike "Blanch" Blanchard** 28:55 It's not good. I'm sure she didn't… she didn't like it either. It wasn't her idea.
**Albert Lockett** 29:02 Alright, yeah.
**Mike "Blanch" Blanchard** 29:03 Her busiest time of the year, she's probably like, oh my god.
**Albert Lockett** 29:07 Alright, Ann, well, yeah, get to it. We'll, we'll have the update next week.
**Mike "Blanch" Blanchard** 29:15 Sounds good, man. I'll talk to you later.
**Albert Lockett** 29:18 He's out.
