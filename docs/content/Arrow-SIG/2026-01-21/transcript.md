SIG: Arrow SIG
Date: 2026-01-21
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 02:12 Hey, Mike?
**Mike "Blanch" Blanchard** 02:15 Hey, Albert.
**Albert Lockett** 02:17 How's it going?
**Mike "Blanch" Blanchard** 02:18 Good! How about you?
**Albert Lockett** 02:20 Oh, not bad. Did you have anything you wanted to discuss today?
**Mike "Blanch" Blanchard** 02:25 Nope.
**Albert Lockett** 02:27 Yeah, me neither. I just want to,
Want to skip it this week?
**Mike "Blanch" Blanchard** 02:31 Sure, I can kind of update on one quick thing.
**Albert Lockett** 02:34 Sure, sure.
**Mike "Blanch" Blanchard** 02:35 A while back, when you were first PRing your work.
We had a little bit of a conversation about, like, naming convention.
Where… what Drew and I have done up to this point is, like.
If you want to specify severity text, it's…
snake case? It's whatever is in the OTEL spec on the data model.
And then what you guys did is, like, whatever it is on the proto. So it's like…
Pascal? It's like little… It's all lowercase with an underscore in between the words.
**Albert Lockett** 03:15 Yeah, yeah, I know what you mean. Yeah, I don't know the… I don't know the exact, right kind of case, whether… but I know what you mean. Yeah, we're using…
Well, we have a team internally working on, like, an exporter.
**Mike "Blanch" Blanchard** 03:28 And they decided to use, like, the JSON representation. So severity text for them is…
Pascal, it's like little s, big T, so it's like a third convention.
So Drew and I think we're gonna retrofit some kind of, like, alias feature So that in our stuff.
you can do those 3 different forms, and it hopefully will do the right thing. The goal being, like.
We want to be forgiving, more or less, so the users don't have to understand, like.
which… which form is being used. Oh, there's Drew. So there'll probably be a PR soon. I don't know if Drew is gonna do it, or I'll end up doing it, but…
It won't impact what you're doing.
I wish there was a way to put all of that into the tree itself.
And you could for things where you have the schema, but there's, like, always the possibility that you're looking up some key based on something you resolved at, like, runtime.
So, there also has to be some code…
in, like, the data, so it's… I think it's gonna be kind of nasty, but…
I'm hoping to find a way to… Make it as… Clean.
as reusable as possible, but I don't know at this point.
**Albert Lockett** 04:58 Awesome. Okay, cool, yeah, that's, that's, that's really good information. So, yeah, I'll… I'll look for that PR when you guys do it, and like…
I can… I can think of a few places that, like, I could slot that into the stuff I'm doing. So, for example, we could say, oh, well, it goes in the parser, or we could say it goes in the
In the planner, because that's what's actually, like.
looking at the column names and stuff, so, I guess, like, what I was gonna say is, like, if you guys can, like, kind of…
implement it however you need to, and I think, like, if we need to pull it onto the OTL… OPL side, or into, like, call my query engine side, like, we have a… we have a few different places we can do it, so… so…
You know, like, however you guys implement it, then we can figure out the best way to integrate it.
**Mike "Blanch" Blanchard** 05:53 Cool.
I think some of it will go into, like, parser abstractions, which is cool.
**Albert Lockett** 05:59 Awesome, awesome.
**Mike "Blanch" Blanchard** 06:00 You can utilize if you are supplying schema to the parser.
And then there'll be a corresponding piece that goes into, like, the record set itself, and then that will have to go into your column resolver. It'll just be kind of custom.
But hopefully you can utilize, like, half of… half of the work.
**Albert Lockett** 06:21 Sounds good.
**Mike "Blanch" Blanchard** 06:23 We'll see.
**Albert Lockett** 06:25 Awesome.
Cool.
**drewrelmas** 06:27 I joined late, but I just want to make sure, Blanks, you're talking about schema mutation, right?
**Mike "Blanch" Blanchard** 06:32 No, we were talking about the aliasing feature.
**drewrelmas** 06:36 Oh, the aliasing, okay.
**Mike "Blanch" Blanchard** 06:38 We did talk a lot…
**drewrelmas** 06:39 I don't stop.
**Mike "Blanch" Blanchard** 06:40 About the mutation.
**drewrelmas** 06:44 I'm sorry, could you repeat that?
**Mike "Blanch" Blanchard** 06:46 We talked a little bit last week about the mutation.
**drewrelmas** 06:49 I just kind of explained the problem to Albert, because…
**Mike "Blanch" Blanchard** 06:54 what they're essentially doing is they're going to make their own parser for OPL, starting from the parser that we did for KQL,
So I just kind of mentioned, like, hey, we're facing this problem with schema mutation, so while you're going in there and building something new, you may want to put that in from the start.
To make it easier on yourself.
**drewrelmas** 07:15 Yeah, okay, get it.
On the aliasing, I do have a P…
I mean, I have the PR out for that, actually.
**Albert Lockett** 07:30 Oh, cool.
**drewrelmas** 07:32 It was like a draft, it's from a few weeks ago, so maybe you hadn't… Seen it,
I opened it on January 5th, but it's, 1725.
Adding aliasing… For parsers, so the main… I don't know how much Lynch had said before, but…
we recognize that originally we worked with the names from the log data model.
But we see you and
other, like, OTTL as well, like, prefer the snake case proto, names, so…
**Albert Lockett** 08:13 Yeah, this should…
**drewrelmas** 08:15 Let you say, you know, severity text or severity underscore text, equivalently.
**Albert Lockett** 08:25 Cool, yeah.
**drewrelmas** 08:26 Anyway, Blanche, you… You had reviewed it a little bit. I think I pushed…
a little bit more… I don't know if you could take another look at some point, but…
It did still feel pretty wasteful, like, there's a lot of repeat in the, the…
logs.rs, but I didn't add any more repeat. It was all… It's already there.
**Mike "Blanch" Blanchard** 08:55 Did you update it? So, originally, when you did it, there were the two
names for everything. Did you add the third one?
**drewrelmas** 09:02 So, I introduced, like, a normalization. So, basically, we only have to provide
all of the implement… the imple for canonical names, and any alias gets, like, converted to the canonical name before we check it,
And, like, the contains key get static.
Get items, etc.
**Mike "Blanch" Blanchard** 09:28 Okay, cool, check it out.
**Albert Lockett** 09:32 Yeah, this looks, this looks, this looks,
Like, what we want true. It looks like we just need to call this, normalize key…
**drewrelmas** 09:43 Yeah, and I mean, there's something to be said for, like.
I think we could go one of two ways. Either we choose one representation and that's all you support, or, like, you can go fully the opposite way of
Let's accept, you know, uppercase attributes, lowercase attributes, like…
that's a bad example, because it's attributes, but, like, I'm saying you could do snake case, you could do camel case severity text, you could do uppercase severity text.
I lean more towards the side of flexibility, as I think Blanche has probably said.
But… Yeah.
**Albert Lockett** 10:30 Yeah, this is cool. Yeah, okay, so I,
I don't think this would be too hard to… fit in.
**drewrelmas** 10:41 I mean, Albert, I saw, like, I… just this morning, I looked a little bit into…
Like, the resolution?
in the columnar engine of, like, well-known keys, like Sveritext, for example.
**Albert Lockett** 10:57 And…
**drewrelmas** 10:58 it's actually a little bit simpler, because everything is just, like a string in a column, right? That just so happens to match, like, severity underscore text, so I feel like it would be pretty easy to make that support aliases as well.
**Albert Lockett** 11:17 Yeah, I… I think so.
Yeah, I think so.
immediately, like… I think, I think eventually, like.
We do need to add some kind of…
what do you call it? Handling of the… of the schema in the columnar query engine, because.
**drewrelmas** 11:41 Like, like you said, it just, it just takes whatever…
**Albert Lockett** 11:46 String you pass it, and then expects there to be a column with that name on the…
on the, OTAP.
record batch. Like, the name from the query and the name in the arrow schema just happened to line up, and so…
Eventually, we probably need to, like… Check that,
and confirm that, like, this… like, this column name you're using is something that's valid in the… in the OTAP schema. I just… I hadn't done that yet. I did have an issue open for it somewhere, so probably I'll… I'll reference this PR1725 on that issue.
**drewrelmas** 12:30 I did pull up my screen, because I just wanted to ask you one other question, which… I was also reviewing OTTL this morning, which, again, is, like.
something we've kind of been avoiding, because our focus so far has been KQL, but theoretically, nothing would stop us from having an OTTL parser that goes into the, you know, the…
Expression tree and use whatever engine we want with it, but…
In OTTL, they're very specific about, like, prefixes.
referring to… like, the, I guess, entity that you're operating over?
So, for example, to refer to body, it's log.body.
I know these… I was wondering if we hold… in the record set engine, Blanche, you and I know well, we have the prefixes for resource and scope, if I remember correctly.
I'm wondering if we should be lenient and just also allow the prefix of the signal, like log dot, even if it's not really necessary.
So I was wondering if you had a thought on that.
**Mike "Blanch" Blanchard** 13:42 For what?
**drewrelmas** 13:44 And then OPL right now, like, just looking at the code, if I said log.body.
It would just tell me that that doesn't exist, because a log isn't found in the
Arrow Record Bash.
**Mike "Blanch" Blanchard** 14:01 What we may want to do, Drew, is allow you…
So where it says, like, log.body, the current way to do that would be source.body.
So, what we may want to do is allow you to alias source.
So you could say, you know, accept log as source.
**drewrelmas** 14:23 Now, but that's also, like, that source key at the beginning of the query, and I know in OP… if I'm remembering in OPL,
the beginning of the query is what entity you're operating on. Albert, is that correct? So it's, like, logs, pipe, and then something?
Yeah, that's right. That's what we're using that for. So, I think in KQL so far, we essentially just… because we only operate over log data there, we, like.
Basically, we don't care what the keyword is at the front, it's just source.
Or it could be anything. Blanche, correct me if I'm wrong.
**Mike "Blanch" Blanchard** 15:03 Yeah, we do parse it.
So it's there, we just drop it on the floor.
**drewrelmas** 15:09 We just don't use it for anything, right?
**Mike "Blanch" Blanchard** 15:11 So we did push that.
**Albert Lockett** 15:13 as an alias.
**Mike "Blanch" Blanchard** 15:15 Per source, or…
Just move away from hard-coded source and make them use whatever they put there.
**drewrelmas** 15:25 And I totally get, like, Albert, I like that we're doing it for resource and scope. That makes perfect sense, because they're quote-unquote attached data, as we have in the record set. I was just curious, because I noticed…
in OTTL, they… But they kind of…
I guess they don't really need it. This log statements colon might be enough of a hint to them what entity they're talking about.
But I guess they just opted for, verbosity.
**Albert Lockett** 15:57 For OTDTL, you'd have to parse this grammar.
So you could…
**Mike "Blanch" Blanchard** 16:03 You know, anytime you see log dot, or whatever your signal is in the OTTL parser, it knows it needs to admit a source lookup.
So, we wouldn't even really need to do anything for what we're looking at here, but…
I'm fine if we want to.
Have the support for aliasing.
**drewrelmas** 16:26 It's not super critical, it was just something I thought about. Albert, you were starting to say something?
**Albert Lockett** 16:31 I was gonna say, like, one thing that's weird is that, like… so I do think, like, having log there and, like, metric is,
like, redundant, kind of, even in…
**drewrelmas** 16:44 Because you know what entity you're talking about.
**Albert Lockett** 16:48 Yeah, exactly, and if you look at the filter processor, they don't put that prefix on, weirdly. Wait really?
**drewrelmas** 16:55 late?
**Albert Lockett** 16:56 Yeah.
**drewrelmas** 16:56 Babylon.
**Albert Lockett** 17:00 Yeah, so check your…
**drewrelmas** 17:01 Goodness, you're right.
**Albert Lockett** 17:02 Yeah, so, like, that's another thing that's super weird.
So we kind of figured, like, when we were looking at OPL, we're like, yeah, let's eat, like, that…
Having, like, log and metric before it seemed, like, kind of…
Redundant, and so we chose, like, not to,
Not… not to, like, have that. That… that prefix on.
**drewrelmas** 17:30 And…
**Albert Lockett** 17:31 On every identifier.
**drewrelmas** 17:34 Yeah, I mean, that makes sense, too. I didn't know that it… I mean.
That's… this is actually quite strange to me that they… That it's so different.
From one processor to the next.
**Albert Lockett** 17:49 And I think, like, Part of me was… was thinking that, like.
Maybe there was, like, a desire at one time in the transform processor to… Be able to, like.
I don't know, like, set a,
A field on a log that you computed from some field on a metric, and maybe there were.
**drewrelmas** 18:18 Oh, boy.
**Albert Lockett** 18:18 design the approach to support that, even though, like, the underlying P data wouldn't have, like, multi-signal data in it, so…
And I think, like, in the transform processor somewhere, it says something like, you can't…
**drewrelmas** 18:34 Old Multi-signal or something like that, so…
**Albert Lockett** 18:38 maybe it was, like, they thought about doing that in language, then put those prefixes on, then realized it wasn't really possible with their data model, but then the prefixes just stayed on there. That would be, like, my guess about what could have happened, but I'm really not sure.
**drewrelmas** 18:52 Yeah, okay. Well, we don't have to worry about it too much, for the moment. It was just something I…
thought I would bring up in this… Venue.
Anyway, I think that's all I have to say about that. How do I…
I need to stop sharing my screen.
There it is.
Yeah, so are there any other topics that you guys wanted to… Dr. Bell?
**Albert Lockett** 19:34 Yeah, I didn't… I didn't have too much of an update from, since last week. Like Mike said, we did start writing our own
A different version.
**drewrelmas** 19:44 Yeah, I've seen some.
**Albert Lockett** 19:45 Let's go ahead.
Yeah, but I don't know if…
Too much update on it since,
last week, so it was mostly focused on, some, some performance… regression that… that…
Rehab related to decoding, delta encoded IDs…
So, so that was, like, not really related to the query engine, I guess, so I've been focused on that.
**drewrelmas** 20:17 I guess, while you're here, I mean, I think this technically falls under… maybe not query engine, but transform in general,
I saw that Tom opened the PR for attribute insertion.
And OTAP transform?
**Albert Lockett** 20:36 Oh, yeah, that was awesome.
**drewrelmas** 20:39 So, I know, Albert, you were reviewing it. You had what looks like a lot of good feedback.
I might ping you sometime. I know, like, I think you were away when I merged it, but I also had that condense, processor that we put in that does the condensed behavior I needed for common security log or Ceph manipulation.
I imagine you probably have a…
Host… you would have a host of comments about the,
performance implementation of it, so maybe someday I'll…
see if I can chat with you about it, but again, not directly related to Query Engine, I guess.
**Albert Lockett** 21:20 Oh, sure. Yeah, I'd be… I'd be happy to take a look at it.
Yeah, and it looks like, it looks like Tom actually…
update a bunch of the feedback I had on the insert.
attribute thing, so… Taking a look at.
**drewrelmas** 21:33 How much?
Nope.
I know he's doing this implementation in, like, the… transform.rs, would you…
maybe I haven't looked at the Commodore query engine enough, but are you using the same
Manipulations, like to do rename and delete, for example.
Or are you not even using what's in this transform.rs for that query engine?
**Albert Lockett** 22:06 Oh yeah, we're using, we're using what's in this, this transform.rus.
**drewrelmas** 22:10 Got it. Okay, that makes sense to me.
Yeah. So, for example, Tom doing this would let you implement Xtend, for example.
Code call insert underneath.
**Albert Lockett** 22:23 Yeah, exactly. Yeah, exactly. So, like, as soon as this gets merged, it'll be… it'll be super trivial to add, extend to the call and recovery engine to insert attributes.
**drewrelmas** 22:38 And, I also… I also want this one in, because I have… Da-da-da…
Should open Issues by me.
Here we go. I also want this in because part of the condensed implementation I started with was, like, essentially rebuilding the entire attributes batch again.
But once we have the insert, I can just call insert instead of needing to build a new batch, so…
it'll be good for me, too, once that goes in.
**Albert Lockett** 23:23 Awesome. Cool. Yeah, I'll, I guess it's, like, it's almost the end of the day here for me, but I'll, like, I'll take a pass of Thomas PR, like, first thing tomorrow.
**drewrelmas** 23:33 Oh yeah, no worries.
**Albert Lockett** 23:34 And yeah, I see he's got, like, 7 or 8 commits.
Or 13 commits since yesterday of… of… Fixing feedback, so… Yeah, we can,
I'll take another pass on it, and then hopefully we can get it merged, since we're both, waiting on it.
**drewrelmas** 23:52 Okay.
Condense has just been really weird, because it's not… Like, you have to build…
A value based on a bunch of other values, so it's… Yeah, it's a slightly different…
type of transform, I think, than the ones that happen in transform.rs on singular rows.
anyway, cool. Thanks for… thanks for helping us out with this.
**Albert Lockett** 24:22 Hey, no problem. Yeah, happy to help.
**drewrelmas** 24:26 Alright.
Well, I didn't have anything else, really, to say, Blanche, unless you do, we might be able to…
And a little early.
**Mike "Blanch" Blanchard** 24:36 I'm good. Thanks, guys.
**Albert Lockett** 24:38 Yeah, me too. Okay, have a nice, rest of your afternoon, guys.
**drewrelmas** 24:42 Yeah, talk to you tomorrow, probably in the SIG.
**Albert Lockett** 24:45 Oh yeah, tomorrow it's sick. Okay, see you then.
**drewrelmas** 24:48 Bye.
