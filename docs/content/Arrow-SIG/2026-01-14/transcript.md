SIG: Arrow SIG
Date: 2026-01-14
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 00:49 Mike?
**Mike "Blanch" Blanchard** 00:54 Hey, Albert.
**Albert Lockett** 00:56 How's it going?
**Mike "Blanch" Blanchard** 00:59 It's going good, how about yourself?
**Albert Lockett** 01:01 Pretty good.
Let me, the meeting notes started here.
Today is the 14th.
And… Alright, give the others a few minutes to join.
Did, did you have anything you wanted to add to the agenda?
**Mike "Blanch" Blanchard** 02:03 I don't have anything specific.
**Albert Lockett** 02:08 Yeah, alright, yeah, yeah, me neither. I guess, I could follow up, Just based on the… based on the discussion we had last week, so… like, I don't know if you saw the message or any of the PRs that I put in, but I think where we landed last week was, we… we thought… we definitely knew that we were going to have a different grammar for KQL, and in retrospect, that was, like, a super reasonable… or sorry, for OPL, in retrospect, that's… that's super reasonable. And then, when I started looking at, like, how we would actually share the, like, the parsing code, I thought, oh man, there's a lot of, opportunity for… for… for us to screw things, screw things up, and, and, you know, for… for… for, us to… to write parser code that makes certain assumptions about the grammar that… that doesn't hold true for both of our grammars, and both the KQL grammar and the OPL grammar, and then, and then we just… we end up in a… in a… in a crappy place where we… we have bugs in our parser and stuff, so… So I started writing… a new parser for OPL.
like, you… very much inspired by the KQL parser, using a bunch of the same… the same patterns, and using pests and everything.
So the moral of the story here, or the update, is just to say that, like.
the discussion that we had last week, where we kind of landed, like, hey, I think that we'll, you know, maybe have an opportunity to share some of that parser code. In retrospect, after digging in a bit, I don't think we should do that, so… And I, I, you know, it's, it's… We lose the benefit of the code reuse, but in the long term, I think that we gain a much more important benefit, which is we get to be masters of our own destiny. Like you said, it's a really good way to think about it.
And yeah, and then we… I think we just have less opportunity to introduce, like, subtle bugs trying to write one parser that supports two languages. So, yeah, so that's, like, in terms of the, like, the query engine work, that's basically what I've been working on the last, The last week or so has been that.
**Mike "Blanch" Blanchard** 04:48 That sounds good to me. Your reasonings make sense.
So, I'm… I'm supportive.
Just do me a favor, while you're working on your new parser.
If you encounter, you know, new patterns or better ways to do things, please share, because a lot of that code I just made up. I learned it all on the fly.
**Albert Lockett** 05:16 Cool, yeah, oh man, of course, yeah, definitely. I'm, I'm still learning pests as well, and, and using, the… the QQL price here as a… as a bit of an inspiration, but… but yeah, you know.
definitely, I think this will give us the opportunity to, like, learn from one another and explore new patterns, so I'll, you know, I won't keep any secrets from the KQL side, of course.
**Mike "Blanch" Blanchard** 05:41 The math stuff was really interesting, or you have to kind of own… the precedents…
**Albert Lockett** 05:51 Yeah, that stuff was nurture. I saw that, I saw that, in terms of precedent, it looks like for… Kiko, at least, for some of, like, the logical operator precedence. We used, a Pratt parser, And, I ended up, I ended up… Using that as well.
But, I actually, actually didn't… didn't know about that when I started doing it, so… so I started off, like, having, something called, like, a multiplicative expression that a child exp… or an additive expression that had a child expression that was a multiplicative expression.
Instead of just having, like, one expression that would use the Pratt parser with, like, the math operator in the middle. And so that seemed to parse correctly, but then… I figured out that, oh geez, I need these to be, what do they call it? Not left precedent, left associative for subtraction and division, and I had it right associative, so they had to go back and use the Pratt parser, so… Yeah, luckily that Lalik caught that in the code review, because that would have been a pretty crabby bug, in the math.
So…
**Mike "Blanch" Blanchard** 07:16 The big issue that I was running into is, like, the lack of support for left-hand recursion.
**Albert Lockett** 07:23 Yeah, yeah, exactly.
Me too. So that was where the Pratt Parker came in.
**Mike "Blanch" Blanchard** 07:31 Spent a lot of time.
fighting the pest files, and I got pretty far solving it without that Pratt stuff.
But it forced you to put, like, parentheses in places that KQL doesn't force you to do it.
Just to, like, kind of break the left-hand recursion, like, if you start with a paren.
Then it… it's happy.
But then, we weren't as close.
So it ended up working out really nicely, I think, but… for a while, I looked at, like, pests upstream, and was like, should I just try to, like, contribute left-hand recursion?
I found, like, there's a PR out there, like, somebody doing it, and they ran into some problems, so I was like, I had to decide what was the better use of my time.
**Albert Lockett** 08:24 Yeah, I know, okay.
It wasn't.
**Mike "Blanch" Blanchard** 08:27 There wasn't a lot of thought that went into Pest as a choice.
That was kind of drew really early on. He just looked at what was available in Rust.
I think the bigger one is, what, like, Antler? But there was no official stable rust… Runtime for it.
It's like, I'm not… I'm not married to pests.
By any standard, but seems to be working pretty well for us.
**Albert Lockett** 08:56 Yeah, that's kind of where I landed, too.
And, there's some…
**Mike "Blanch" Blanchard** 09:02 like, at least there's some IDE tooling for it, like.
**Albert Lockett** 09:05 Sounds like…
**Mike "Blanch" Blanchard** 09:06 The browser page?
**Albert Lockett** 09:09 no, I found the book… That's…
**Mike "Blanch" Blanchard** 09:14 I'll paste it in the chat for you, it's, like, my go-to… tool anytime I need to work on pests.
Where's… You can basically, like, paste in the grammar, and then type the query, and it will show you the rule tree, like, in real time. It's… it's a huge time saver.
**Albert Lockett** 09:46 Oh, man, this is… this is way better, actually, yeah, because I was, Writing unit tests and printing it out, and so…
**Mike "Blanch" Blanchard** 09:58 I love this tool.
**Albert Lockett** 10:00 Awesome. Okay, yeah, cool. Let me, just throw that in the meeting notes.
So that's bookmarked for later. I guess I could bookmark it in my browser, but… Awesome. Cool. Yeah, that's super helpful. I'll definitely be using that.
Yeah, and then I, like, not too… not too much, like… like, Shocking updates for, like, the week coming forward, at least from my side on the query and transform stuff.
I think that, it's, it's gonna be very, like… like, a lot of time, I think, like, the next week or so is going to be spent, just trying to get back to parity with, like, where we were with the KQL parser, in terms of stuff that's supported in the Cobner Query Engine. So, deleting attributes and some of the, Some of the finer points of filtering, like, like filtering, checking if things are null , and regex matches, and… And string contains and stuff like that, so, Yeah, so, so, but just…
**Mike "Blanch" Blanchard** 11:13 One thing you might want to consider doing, since you're going from the ground up.
So, we don't have this in our KQL parser right now.
Like, you can… you can seed it with some schema information.
You can say, like, I know about these attributes. And then it has some features, like, you can give it the default map thing, you can tell it, I want it to allow unknown things.
And we have a certain… level of functionality.
We're working with this other team that's not an open telemetry team, they just have their own agent.
They're modifying their own tables, they have their own requirements.
And they're, like, gung-ho on a bunch of features around, like, schema validation.
So, we've tried a few things, we haven't been able to crack it yet. What Drew attempted to do is, like.
as… We're parsing the statements… If she was here, you could probably explain it better, but, like, if it sees, like, an extend statement, or something, like, defining a new field or a key.
he, like, updates the schema. So he's trying to track modifications to the schema so that it can be a little smarter, so, like, if you… If you try to return, like, let's say.
attribute ABC, and it doesn't exist, it will give you an error. But then if you extend it, you define it, and then reference it, it will allow that, because it knows, like, oh, this is a thing, I saw it, it exists.
So it's sort of this idea of, like, you can seed it with the schema, it mutates the schema, and then at the end it can give you, like, here is the… output schema to the best of my ability. I say best of my ability because there's certain operations, like.
extract JSON. Like, there's certain things you can do where it's just impossible to know the types of things. We might always know the name, but… so we were… we're kind of kicking around, like, how we could best effort be smarter about the schema as it, like, mutates, so… something to keep in mind, you may want to have that in OPL, I don't know.
**Albert Lockett** 13:33 Yeah, that's, that… Interesting. Yeah, that's a… that's… that's a… that's a really interesting idea. Yeah, I'll make a… I'm just making notes of that, as you're talking, and I can… I can, create an issue for it, and I'll run it by Laurent as well, and I can… I can follow up with Drew and try to… if you can point me directly to that code, if not, I can probably find it. But that's a super helpful tip, for sure.
**Mike "Blanch" Blanchard** 14:05 It's… for us, it's turning out to be a hard retrofit, so maybe if you build it in from the start, you'll be happier.
**Albert Lockett** 14:15 Cool. I'm just taking notes with Paul. Awesome.
Cool, that's super helpful. Thank you.
**Mike "Blanch" Blanchard** 14:25 True.
I don't really have anything else, I can kind of update you, like, what I've been doing is… I'm trying to do a version of the Colomar engine.
That works more like the record set, in that there's, like, a whole abstraction set of traits or an API.
I'm sort of in the weeds, like, fighting rust on Lifetimes, and trying to figure out all that, so I haven't gotten very far, but… It's kind of what I've been noodling.
**Albert Lockett** 15:00 Cool. Yeah, that sounds really interesting. Happy to, if, like, if you ever have anything that's, like, a work in progress, or, like, that you need me to, like, help review, or questions or anything, happy to help out.
**Mike "Blanch" Blanchard** 15:14 I need to get it to life.
It's kind of like what I did with the record set.
I really did it twice, but, like, I built a proof of concept.
And then I redid that whole thing into what became the engine.
and then I, you know, I showed that, reviewed that, and then, ultimately, I opened, like, PRs, like, piece by piece, and then those change, you know, through review, so the final engine was even a little bit different than the two POCs.
But I'm hoping to get sort of that going, where I have… like, here's a POC, it does, like, some of the stuff, maybe not all of it.
it's very reminiscent of what I went through before, it's like with Rust.
I get it all working for, like, one simple thing, like, okay, you can return you know, the severity text off the arrow table. I'm like, okay, cool, that's working. And then I go into, like, the attributes, whatever you call that thing, reference table or child table, and I make, like, one change to my code, and now all the lifetimes are, like, broken.
that's like, I inch forward, but then I constantly have to, like, redo everything, and… My one gripe against Rust is, like, it's a horrible… prototyping language, because it's just so verbose with all the decorations you need to do. And when you need to change one, it's like, oh, you just blew up your whole code base.
**Albert Lockett** 16:37 Oh, yeah. Yeah, for sure, I know what you mean. We went through that.
We went through that with the, The… the views that we implemented over top of the…
**Mike "Blanch" Blanchard** 16:50 You can see that?
**Albert Lockett** 16:51 Yeah, because they all had, like, different lifetimes and traits with different lifetimes and stuff, and yeah, so…
**Mike "Blanch" Blanchard** 16:58 Oh, that's where I am right now, man. Traits on lifetimes is just a nightmare. And then the whole, like, dying keyword… like, I come from, like, a C-sharp.net background, and, like.
interfaces have so much more flexibility than, like, traits and dine and… Rust is just… it's hard.
**Albert Lockett** 17:20 I agree, yeah. I was… I was coming, like, at rest from the Javin Go background, same thing, right? It's just like, why can't I just pass an interface? Why do I need this?
**Mike "Blanch" Blanchard** 17:34 Yeah. The dying keyword is not… as rich as, like, an interface in Java or C Sharp, for sure.
sometimes I'll solve something, and I'm like, oh, great, I figured it out, but then I've made something dying incompatible, and now it's, like, useless to me.
**Albert Lockett** 17:54 Yeah, y'all, man, I know what you mean, yeah.
Well, yeah, hopefully, yeah, I mean, yeah, like you said, though, I think, like.
this, like, iterating on these solutions a few times, building proven concepts, like, that seems to be the way to do it, right? Like, that's, like, the columnar query engine that I'm working on, like, in the OTAB, in the OTAB crate, like.
that one we went through, you know, like, at least a few POCs on, and I think that, like, all that code basically got thrown out, but we ended up with something better at the end, and so it sounds like that's what you're doing, what you did with the record engine, so, you know, no… like, at least in my opinion, right, it's like, no shame in building it, like, the quote-unquote wrong way the first time if, like, it helps you learn a bunch of stuff, and then you build something you actually want. After that, you can always iterate on it, so… Yep. Yeah.
And, yeah, I mean, like, in terms of, like, lifetimes in Arrow, like, I don't know exactly how the engine you're working on works, but, like, one thing I do know is, like, Arrow generally can be, like.
Pretty aggressive about, like, wrapping everything in, arcs. So, like, sometimes you can kind of use that to your advantage, where, for example, like, cloning a record batch Is, is… somewhat cheap, because you don't actually clone the data, you just clone, like, the array of arcs that, are contained, within that record batch, because all the… all the arrays are supposed to be immutable, so… If, like… anyway, not sure if that's helpful, but just something to… to… To keep in mind, it helps you with lifetime health.
**Mike "Blanch" Blanchard** 19:45 Yeah, I have seen, like, you know.
going into the definition… the other thing that's weird about Arrow is, like.
you have, like, string array, which is really, like, a generic byte array, which is really, like, there's all these aliasing of types, like, just trying to figure out what everything really is has been kind of an adventure.
But I have seen the arc, and I haven't used that much in my own code, so maybe that's why. I'll do some research there, that might be helpful.
**Albert Lockett** 20:15 Yeah, I think it… it… it probably could be, because, like, like.
**Mike "Blanch" Blanchard** 20:19 if, like, I'm thinking about, like, the arrow…
**Albert Lockett** 20:22 Like, arrow record batches… all con… they contain, I think they, like, they contain something, like, a field called columns, which is an array of a type called ArrayRef.
But an array ref is a, a type alias for arc dyne array, And so that's, that's kind of nice, because, like, you can, like… You can clone those, those arrays from the record batch, or you can clone the record batch, and it just, like.
it just clones the arc, it doesn't clone the underlying data, and so that just makes things a lot easier, because then, like, as you're passing the record batch around, or the arrays within that record batch or something, like, you don't, you usually don't need to actually own them, which is, which is kind of nice. So, Yeah, that's… anyway, so the, like, Arrow's liberal use of ARC to try to avoid copy could help you a little bit with the lifetime stuff, something to keep in mind.
**Mike "Blanch" Blanchard** 21:27 Yeah, it's already given me some… some ideas.
Thank you.
**Albert Lockett** 21:33 No problem.
Cool. Well, yeah, that sounds like a sane piece of work, so that seemed really cool.
Yeah, so I guess, I want to… I don't have anything else. If you don't have anything else, maybe we can, It's a short, A short week for the query transforms meeting.
**Mike "Blanch" Blanchard** 21:55 Sounds good to me, have a good one. See you next week.
**Albert Lockett** 21:58 Yeah, see you next week. Have a nice, have a nice week. Bye.
**Mike "Blanch" Blanchard** 22:02 See you then.
