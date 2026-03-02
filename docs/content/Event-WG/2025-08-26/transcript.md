SIG: Event WG
Date: 2025-08-26
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/HrcOJsqfbcVZJlraEpYmhQW0ckpdfuyBxdx6TqhgukK61-hUykSl-w-EAjyZeIix.bUpkW6PMR5TW04vQ
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:01 I trust. Long time no see.
**Trask Stalnaker** 01:03 Yes, hey, Lamilla.
How are things?
**Liudmila Molkova** 01:09 Things are good. I learned how to make CTRL-C, Ctrl-V work on Mac.
It's my biggest achievement.
**Trask Stalnaker** 01:20 Yeah, I'm pretty lost when I…
get onto a Mac as well.
**Liudmila Molkova** 01:28 Yeah, it's hard. I learned that my fingers know what I'm doing, and my brain doesn't even think about it. And then when it doesn't work, I need to understand what is it that I was trying to do?
**Trask Stalnaker** 01:41 Yeah… Yeah, it's the whole, like, IDE shortcuts… Like, I need my keyboard… With the same layout.
**Liudmila Molkova** 01:56 Yeah, IDs are good in customization. You can usually configure them pretty well.
Mac is super bad at customizing shortcuts.
**Trask Stalnaker** 02:08 Hey, Robert, welcome back.
**Robert Pająk** 02:09 Boom.
Nice to see you. How are you doing, all?
**Liudmila Molkova** 02:12 Good, how are you?
How was your vacation?
**Robert Pająk** 02:16 It was pretty well. I wish to be longer, as always. But yeah, feeling good. And also.
Very happy to work with you again.
**Liudmila Molkova** 02:30 Yay!
**Trask Stalnaker** 02:30 Yeah, hey, congrats on, getting the… Prod… the proposal accepted.
the coup car.
**Robert Pająk** 02:38 Yeah, thanks. Thanks. Yeah. Yeah, the one which will be together, yeah, for… Yes, yeah.
**Liudmila Molkova** 02:46 I'll finally meet you in person.
**Robert Pająk** 02:49 Yeah.
**Trask Stalnaker** 02:51 Yeah!
Let's see where, … Working on… yes, thank you for…
Jumping right back in to things this week, Robert.
**Robert Pająk** 03:12 Yeah, I have not changed the date.
I went for a walk before I had done it. I'll just make it in a second.
Gosh.
**Trask Stalnaker** 03:22 V… Okay.
**Robert Pająk** 03:26 Okay.
**Liudmila Molkova** 03:30 Oh, you already have a draft, wow.
**Trask Stalnaker** 03:36 Yeah, thanks for putting this out, because that, this made it clear to me, and that's why I was asking in the spec re… spec meeting for….
**Robert Pająk** 03:45 Yeah, thanks for the heads up, and I saw Tigran also is also very responsive in the proto-PR for the profiles, so he also wanted to move quickly with it.
**Trask Stalnaker** 03:56 Great.
Is there… do you want us to… Review… is there much?
Even to review here….
**Robert Pająk** 04:15 You… Here, there's not much to review, you can just double check.
It's mostly just removing these phrases. I also added this behavior of software, it says duplicated this… you see this one?
Yeah, because, yeah, I think… I thought that maybe it's nice, given that I am removing a similar sentence, which you can see here in line 288. So I thought that maybe it's good to keep in a similar… 289, sorry, 289.
So I just thought maybe something similar would be good to have.
**Trask Stalnaker** 04:53 Yeah.
Cool.
Do you want approvals already?
**Robert Pająk** 05:01 Doesn't matter for me, you can approve if you want.
**Liudmila Molkova** 05:05 What is it, blocked on?
**Robert Pająk** 05:07 on the release.
**Liudmila Molkova** 05:09 Oh, I see.
**Robert Pająk** 05:09 Yeah. So that the current, … so that the recent PR, which added this is released first, so then we can follow up with this PR in the next release.
**Liudmila Molkova** 05:22 Sounds good.
**Trask Stalnaker** 05:24 Yeah.
**Robert Pająk** 05:27 This one needs more review, more eyes.
So… I did it, like, in…
maybe 2 hours, or something like that, so I might miss a lot of things. A lot of things was based… based on my, …
on my experience, because I was reading it a lot of times.
This kind of spec, and…
I have put one comment,
But we do not need to address it now. Basically, even in the… basically.
I try to have the terms right, meaning, you know, the terminology. So, for instance, when we are removing this, when we are extending the list of
attribute types, I have removed the standard attribute name, because I don't think it's… it's needed anymore.
That's one of the things that… which I did.
Another thing which I was thinking, I have decided to add this name AnyValue, which was not there in the spec, it was only in the proto, because I think it's a good name describing that it can be, you know, basically
kind of, some union that it can… that can be something, so I decided to keep it. One problematic thing is that the spec already has something which is called Attributes Collection.
which, which is kind of similar to the, like, map string of any value. The protocol has a name for it, key value list.
I do not like the name list, because it kind of tells that it could be repeated values, etc. I was thinking about key value map, but then we have this
not one-to-one translation of the proto, so this is, like, a gray area for me, which I do not know how to handle. Should we call it just, you know, any, …
like… key value, any map, or things like that, … I was having this before.
I must check… I had this before, you can check the rename, there's a commit for it. I can rename it.
because I had this attribute value, but then I thought, if it's something inside the attribute, you know, nested, is it still an attribute value, or is it something else?
**Trask Stalnaker** 08:02 And I decided to keep it also because of the.
**Robert Pająk** 08:05 Of the limits, because right now, the limits are only for the attribute value.
Which kind of means that it doesn't have to be nested. And this is, for example, how we implemented AutelGo.
So we are applying the limits only on attribute values, not on any value. So it's something, you know, deep nested, we are not, applying attributes. So, attribute value is only the… any value set on the highest… The root. Yeah, on the root. So that's… yeah.
And I think that maybe…
probably, both you, Tras and Ludomua, may also have, you know, experience for semantic conventions, whether it's good to have this distinction of the root value, like, like, you know, this attribute value basically is like a composite root, or aggregate.
And any value could just resemble, you know, anything inside, like a leaf, or it could be also a root, but not a root, also a…
Branch, but it doesn't… it won't be the root of the, you know, attribute value.
So, yeah, these are my thoughts, basically, about the terminology. And you have any, you know.
thoughts around this, based on your experience, then yeah, I'm open to hearing.
That's all from my site.
**Liudmila Molkova** 09:31 Yeah, actually… Don't like the idea of separating attribute value and any value.
I think it's just some… Unnecessary complication.
But, … it's like I'm not going to die on this hill if somebody wants to have attribute value.
Separate from any value.
**Robert Pająk** 09:57 I think attribute value is also better, because then we will still, in the APIs and SDKs, use the attribute value type, probably.
We won't create anything separate.
In the types, in the language types, right?
So if we could….
**Trask Stalnaker** 10:16 So, let me lie, I think we could still call it attribute value, but it doesn't… it can be…
a nest, it can be…
the thing that's nested as well. It doesn't have to only mean the top-level thing.
**Robert Pająk** 10:30 Yep.
**Liudmila Molkova** 10:31 Would we have a different type for event body? I know we are not going to use event body, but we do have a type for event body, and it's any value.
**Robert Pająk** 10:42 Yeah, so we can call that it's just an attribute value, basically.
**Liudmila Molkova** 10:48 So event body is an attribute value type.
**Robert Pająk** 10:51 Yes.
if you go to the comments, Trask, I think you're showing Trask, right?
**Trask Stalnaker** 11:00 Yeah.
**Robert Pająk** 11:01 If you go to the commits.
I think there's a separate tab, and probably it would be something like the…
or from the bottom, or something like that. There's a rename… oh, yeah.
Yeah, you can check the places where… where this change has been affecting.
**Trask Stalnaker** 11:25 Yeah, it's a good question, though, of the… log body…
My… Goal with finding something… Oh, go ahead.
**Robert Pająk** 11:44 Read what was before, right?
**Trask Stalnaker** 11:47 Yeah, yeah.
**Robert Pająk** 11:49 Body.
**Trask Stalnaker** 11:59 I mean, I agree, this reads… Kinda weird.
Versus any value here.
**Robert Pająk** 12:08 But this is… but this is how the… how the languages will design anyway.
**Trask Stalnaker** 12:15 Yeah, so in Java, I remember we, …
We named our AnyValue thing just Value.
Because… Any value seemed very…
like, tied to the proto, like, ….
**Robert Pająk** 12:33 Yes.
**Trask Stalnaker** 12:34 Wouldn't have been… what we would have named it in Java, at least anyway, it's just a… Value.
**Robert Pająk** 12:42 What is also in the attributes package, right?
**Trask Stalnaker** 12:48 Should be, let's see….
**Robert Pająk** 12:54 Hold on one.
**Liudmila Molkova** 12:55 I mean, it could be a structured value.
And then it's descriptive, and it's not… Attached to a specific… ….
**Trask Stalnaker** 13:07 Attribute body, or something.
I like that.
**Liudmila Molkova** 13:15 And it's also high… I think that one of the problems with any value, the small problems, I see that… well, int is also an any value.
But when you design the API, you kind of want them to be different. You want to say, okay, this is separate, this is structured, complex, don't go there unless you have to.
**Robert Pająk** 13:35 You mean… you mean that's…
Strictly… strongly typed languages should not use objects or any, right, to represent it. That's what you mean, Le DMI?
**Liudmila Molkova** 13:46 I mean, like.
**Robert Pająk** 13:46 It is any value suggests that you can put anything there, which is not the intention, because it represents just a structured value.
**Liudmila Molkova** 13:54 Right, so you wouldn't want to pass int as any value, right?
You don't want to convert into any ULU.
So the… the API you would give is, let's say, in Java, you add string attribute, you add int attribute, and you add
Complex attribute, which is… structure.
**Trask Stalnaker** 14:16 Yeah, so the current value, …
API in Java sucks, it's very… it's… very inefficient.
…
It's not what we would use for the attributes. We want a new, one for the attributes, because…
It basically just wraps everything, like, in…
Boolean, you know, we wrap it, we wrap, we just continually wrap everything, it's just super inefficient.
…
So you're suggesting, possibly… Truck.
shirt value….
**Liudmila Molkova** 15:08 So here, this is….
**Robert Pająk** 15:10 Problem is that it also… structured value doesn't have to be structured, it can be also primitives.
**Liudmila Molkova** 15:17 Oh, yeah.
So we, we kinda…
maybe we don't, but it feels like we need two different terms. One says, okay, this is any possible thing, and it describes all possible attribute types. But when we go into the details of what attribute types could be, we actually want to say, okay, these are the
What we have there, plus we have nothing.
….
**Robert Pająk** 15:46 I just want to, … I just missed one thing. What's wrong with the name attribute value? Have we, have we agreed on it, or are we just not sure if the attribute value
Is a better term.
**Liudmila Molkova** 16:00 I don't hate it, but there are two things that I kind of want to improve. First is adding
Using attribute value as a nested thing and attribute values is not us.
And the second thing is the event body is also an attribute value.
And I would love us to find A solution to this.
**Trask Stalnaker** 16:24 The first problem… Yeah, so, currently….
**Robert Pająk** 16:27 Currently, the log data model defines it simply as N.
Question, should we change the search for a different name, or…?
Or just keep it simpler and reuse what we have right now in the logs data model.
**Liudmila Molkova** 16:50 So the data model has an advantage, it's not user-facing KPI per se, right? Well, it's user-facing, but it can get away with bad API ergonomics.
Now we are making it public API API.
Attrask, you wanted to say something.
**Trask Stalnaker** 17:08 Yeah, so you mentioned two things.
The first one of, like, It being… having different concepts for the top-level one, the nested one.
Do you think, like, I was thinking of…
From the flat… from the perspective of, like, future, like.
Complex attributes and flattened attributes are the same, like, you could flatten or complexify things that… It sort of…
Potentially, I could see them… not… Being… that being as important?
**Robert Pająk** 17:47 I see.
**Liudmila Molkova** 17:49 Yeah, okay, yeah.
**Robert Pająk** 17:51 Makes sense.
**Trask Stalnaker** 17:54 This one I don't love, but, like, maybe we just call it body value, and, like, as an alias to attribute value.
**Robert Pająk** 18:09 Okay, we can figure it later.
**Liudmila Molkova** 18:11 The collet in the… …
spec language is one thing, and calling it… what should we call it in, let's say, Java API? Would you…
Would you… oh, you always call it all… you would call all of it value. You wouldn't care much, right?
**Trask Stalnaker** 18:31 Yeah.
**Liudmila Molkova** 18:34 And it's already in the stable APIs.
**Trask Stalnaker** 18:38 That's a whole different problem, because, I mean, we… …
So I wouldn't… I wouldn't overly… …
Pay attention to what Java did here.
Because we may have to work ourselves out of a hole anyways, because we don't…
Because of the inefficiency of this…
implementation. We haven't really looked strongly at it yet.
**Liudmila Molkova** 19:07 Robert, wearing your goal maintainer hat, would you be happy to accept attribute value as a type in the event body?
**Robert Pająk** 19:18 Yes, that's what we'll do anyway.
**Trask Stalnaker** 19:23 Will you call it the class… will you call the class attribute value, or just value?
**Robert Pająk** 19:34 Like, we will reuse for sure the attribute value.
Maybe we'll make an alias.
Just for readability, but I don't think it will be necessary.
And even an alias, not even nesting one type or another, just maybe creating an alias for, for better naming. Like, type, for example, body value equals attribute.value, something like that. It's in Go.
**Liudmila Molkova** 20:00 Okay, so he… oh, he didn't know you have typole as a single goal.
**Robert Pająk** 20:04 Yeah, we have… Probably we will consider it unnecessary, but we can do it.
If we find it as a ghostic, you know, Worth doing it.
**Liudmila Molkova** 20:18 Stan, I mean, let's go, there's attribute value. I think if we get more feedback from maintainers, we could reconsider it, but I… I don't feel any… anywhere strong on removing attributes.
**Robert Pająk** 20:31 I'm thinking of naming… but I'm just worried that it may have more… maybe more confusing, instead of saying attribute value, something like same as attribute value, but I'm just…
I'm just worried that it will Carry more confusion.
What does it mean, same as?
**Trask Stalnaker** 20:53 Any value is not a bad choice.
… Maybe we'd… maybe just throw in some options?
into this PR….
**Robert Pająk** 21:10 Yep.
**Trask Stalnaker** 21:11 … I can even… I can leave a comment, options, … Options….
**Robert Pająk** 21:27 The good thing about having attribute value
is that I would, instead of creating a new type, like, map of, … …
key value map.
you know, for a nested. I would just not need to create such a new type.
we could just reuse the attributes collection, which is already defined in the specification. If we introduce something like any value.
I think for… to have it…
Similar, you should probably also create a new type which describes, you know, a nested collection of something like attributes, like this heterogeneous maps.
And having it, … Having attribute value makes the specification simpler.
**Trask Stalnaker** 22:19 Let's see, I will try to, …
Look… get to, thanks for adding the, ….
**Robert Pająk** 22:30 Yeah, that's the last point. Do you think that it's well described, or…?
**Trask Stalnaker** 22:36 Yeah, or at least enough for me, and I'll probably pick the… I will try to pick this up in the next week and look at it, because I think that will help me inform my opinion.
on this… discussion, so I wouldn't change anything in your PR yet.
And let's… Try a couple prototypes and see what feels good.
**Robert Pająk** 23:07 If you don't mind, Trask, I'll just maybe revert this change from any value to attribute value, because I think it will, it will be a more consistent PR, a more complete one. That's fine. Because, yeah, okay, so I will just do just this one change.
**Trask Stalnaker** 23:22 I'm just gonna delete my comment. It's just pending comment here, and then once, …
You revert, then either add that comment.
We're all at it.
**Robert Pająk** 23:36 Do you think, …
I think that it's better to wait before I create issues for other languages. Do you have other feelings through the muentrask?
Like, this thing that you just opened… I just opened for Java.
Or you think it's good to create them now?
For all languages.
**Liudmila Molkova** 23:58 I prefer to… Maybe pick an option and be more definitive before we go to other languages.
**Robert Pająk** 24:07 Okay. … also pay safer if Trask Review is, and yeah, Ludimu as well.
**Trask Stalnaker** 24:15 So let's, … Have you prototyped this in Go already?
**Robert Pająk** 24:21 Yes, there… it's the… if you go to the issue in Java, I have put a hyperlink.
Like, we did what we found necessary for our, you know, for our seed bigger.
**Trask Stalnaker** 24:49 You've got value…
So, I mean, you are just calling it value.
**Robert Pająk** 25:13 Yep.
**Trask Stalnaker** 25:17 And this is consistent with what you're kind of proposing here in the spec, to call it attribute value.
**Robert Pająk** 25:24 Yes.
**Trask Stalnaker** 25:25 Yeah, okay.
Yeah, I think that's great.
**Robert Pająk** 25:28 It's something which we already have, it's not something we're introducing in this PR.
**Trask Stalnaker** 25:34 Nice.
Yeah, then I think it makes sense especially to align your spec PR draft with your prototype, since that's your preference at this point.
And I will try to prototype in Java by next week, and, so we can get some more
perspective.
**Liudmila Molkova** 25:58 Yeah, so from Python side, they don't expose… Type alias for attribute value.
And it's effectively any, the Python thing.
… they…
Based on our discussions in the past, they didn't want to introduce a new one. They didn't have it, and there is no need to do
…
I would imagine the same for .NET, but of course we will hear from them, because they have just object as a type.
And they would do something in the SDK to understand the type of the subject.
**Trask Stalnaker** 26:36 But they would probably introduce any value.
**Liudmila Molkova** 26:39 type, I would imagine. They wouldn't parse arbitrary objects and convert them into the
any value in the SDK. They would probably have an API, but …
It won't be the attribute value.
When you add an attribute.
**Trask Stalnaker** 26:58 He lost me, sorry.
**Liudmila Molkova** 27:00 But let's wait for them to express their opinion anyway.
**Trask Stalnaker** 27:05 Cool.
**Robert Pająk** 27:09 It's hard to say Ludovila, because…
for instance, in Go, we are doing this kind of reflection-based conversion in log bridges.
So, one of the options was doing it in SDK, but we decided not doing it SDK because it gives you this, you know, opportunity
to have the choice, if you want to reduce the reflection or not, because if they're using reflection, then they have no other choice, and it's always slower than having strict types, so that's why we decided to go this way. So…
probably .NET will introduce it, but I don't think it will be a blocker for it. I think they can adapt it later. They can even, you know, first
Do a reflection base, and then introduce this type for improving performance.
**Liudmila Molkova** 28:02 Yeah, yeah, I agree that the reflection thing makes sense.
**Trask Stalnaker** 28:07 We discussed….
**Liudmila Molkova** 28:08 Yeah.
**Trask Stalnaker** 28:09 in Java also, and I think what we were…
thinking would be we would have a separate reflection-based, just conversion to value, like, create the value struct from this object, but the APIs, the log APIs themselves would
Only take that.
Strongly typed.
**Liudmila Molkova** 28:34 So it would be the caller responsibility to first convert.
**Trask Stalnaker** 28:38 Yeah, yeah.
Just to basically… You're opting in to performance issues.
**Liudmila Molkova** 28:47 Yeah.
**Robert Pająk** 28:48 we have this functionality in Go, but it is internal, and we're just copy-pasting in each language this functionality, because we're afraid exposing it.
That people will overuse it.
**Trask Stalnaker** 29:03 It is convenient. I love my, JSON parsing… object to JSON parsing.
**Liudmila Molkova** 29:11 Dumping and then parsing. Love it.
**Trask Stalnaker** 29:20 … Do… what else do we have here?
There's… I have not checked in… On my… log-based sampling…
Okay, so… I just need to follow up.
And then…
Okay.
Yeah, I will, I'll sync this back up.
This week, and then… ask for… Reviews from both of you.
**Liudmila Molkova** 30:22 Nice.
**Trask Stalnaker** 30:24 Robert, did you want to… prototype before reviewing, or were you okay with reviewing.
**Robert Pająk** 30:32 I'm okay, I just want to remind you that we have some notes from the last meeting regarding the proposed structure.
And you said that you'll explore it. Yeah, this one.
**Trask Stalnaker** 30:44 I forgot that.
**Robert Pająk** 30:45 But yeah, but it was basically also about Ludomiwa's comments, how we could address it.
**Trask Stalnaker** 30:51 Okay, let's… So that I don't forget.
Da-da-da…
This was… severity… Oh, yes, yes, yes. We were talking about… …
Yeah, maybe we should talk about… Your… let's see, for zero… Yes.
Mercerary set to zero should not be… okay.
By default. Oh, yeah, yeah, this was fine to me, I just… I only kind of care about the default behavior, but, … So then the question related to that is…
Should we… do we see that being…
something that should be supported in declarative config?
what to do with zero?
Value… and the reason why it's relevant is… Right now, the structure… The proposed declarative config structure.
is, … Minimum severity worn.
But if we're going to have other options.
like, what to do with the unspecified value. We might want to create a nesting there.
Like this, severity filter, minimum worn, Drop and specified true.
… Or we could have, you know.
Of course, just as a separate top-level config there.
Not quite as nice.
Oh, there was also this proposal of Robert, kind of, and I kind of agreed, the severity filter
gives some… Could be a good… I don't know.
Thoughts?
**Robert Pająk** 33:14 Buffal work.
Just a metro preference, right?
And what's more readable, maybe?
Which is subjective.
**Liudmila Molkova** 33:26 I feel like… I like that the severity configuration is the most important one, right? It's, I don't know, 80% of scenarios is just configuring the severity. The faster somebody gets to this configuration, the better. The more deeply nested it, the harder.
For them.
… Also, ideally, nobody sh… like, in my mental model, that we should not ever write
Logs or events without any severity.
**Trask Stalnaker** 33:58 Yeah.
So it becomes less important what to do with them.
**Liudmila Molkova** 34:04 Right.
So I like this structure more than more deeply nested.
And even if we need deeply nested structure, It's okay.
It will have it separate.
**Robert Pająk** 34:24 I'm fine with it.
I think it makes sense. Let's go with the simpler structure, with just meme severity.
**Trask Stalnaker** 34:34 Whoa.
I'm just going to commit this, because this made sense.
There's the artistry with? I hate trees.
**Liudmila Molkova** 34:46 I'm just summing it up, I don't remember why it was important, but let's just resolve it.
**Trask Stalnaker** 34:51 Oh, yes, yes, I, yes, right, yes.
Okay.
Cool. So yeah, yeah, whenever you have a chance, take a…
Look. I will take a look tomorrow.
Yeah, maybe by, if we can get approval…
from both of you by next spec meeting, then, I can push it out more broadly there.
**Liudmila Molkova** 35:22 Cool. Thank you.
**Trask Stalnaker** 35:26 Alright.
Anything else for us to chat about today?
Cool?
then… See you.
**Liudmila Molkova** 35:45 See you around.
**Robert Pająk** 35:47 Good to have your back covered.
Bye.
