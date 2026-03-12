SIG: Event WG
Date: 2026-02-17
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Pellared** 00:54 Hello, Frost.
**Trask Stalnaker** 00:55 Hey, Robert.
**Pellared** 00:57 How are you? I'm good.
**Trask Stalnaker** 00:58 Good, good. Long time no see. How you doing?
**Pellared** 01:02 Pardon.
We had a winter break for 2 weeks.
So, yeah.
A lot of work right now.
**Liudmila Molkova** 01:14 Hello!
**Pellared** 01:16 Hello.
**Trask Stalnaker** 01:16 hay.
**Liudmila Molkova** 01:19 It's the third meeting we have with Trask today.
How are you, Rob?
**Trask Stalnaker** 01:29 Yeah, that… That LLM meeting is, tough one to drive.
**Liudmila Molkova** 01:35 You wanna help me?
**Trask Stalnaker** 01:38 Let me, warm up here for a little bit. We'll see.
I don't have enough context yet to really be very helpful.
But I am gonna meet with, Najkumar?
**Liudmila Molkova** 01:58 Yeah.
**Trask Stalnaker** 02:00 And yeah, look at, look at his PRs. So I'll try to… Yeah, that'll be good. He can help me get up to speed, and I can help him get reviews.
**Liudmila Molkova** 02:13 Yeah, I think he has more context than me, but they just… they… they… they… They need helpers.
up until.
**Trask Stalnaker** 02:22 Yeah.
**Liudmila Molkova** 02:23 More than generous stuff.
**Trask Stalnaker** 02:28 Alright, I… Feel like we… Got it.
this resolved. Let's see what the latest last.
**Pellared** 02:39 Oh, I haven't seen the latest comments, I think.
**Liudmila Molkova** 02:45 We are back to the should vs. Ms territory.
**Trask Stalnaker** 02:49 We should not use…
**Pellared** 02:57 Oh, you don't stop!
**Trask Stalnaker** 02:58 Okay.
**Pellared** 03:00 Can you go to the, conver- like, general conversations?
**Trask Stalnaker** 03:04 Oh, sorry.
**Pellared** 03:04 Include the new address, are there some comments?
**Liudmila Molkova** 03:09 No, I'm happy with should not. I'm not happy with must not.
**Pellared** 03:15 Okay.
That's, that's fine for me. Just want to double check.
**Trask Stalnaker** 03:22 Alright, I think we're good, except that this, grammatically, what is it? Should not use body except… Or… Except… as a string?
**Pellared** 03:38 Awesome.
**Liudmila Molkova** 03:55 So, yes.
**Pellared** 03:56 Supply… please apply the command.
**Liudmila Molkova** 04:00 I use AI to help me with articles.
And I ask it, and then I ask it again after tweaking things, and it gives me different dance service articles. So, at this point, I'm like, okay… No, whatever.
**Trask Stalnaker** 04:13 It's English. There is no right answer.
Okay, so I think we're good here… Alright, da-da-da-da… let's see, when did CJO approved? A while ago… let's see, CJ… Anybody else look at this?
Alright, fine.
**Liudmila Molkova** 04:49 And we can… I think we don't need to ask browser folks, because they're switching to attributes anyway.
**Trask Stalnaker** 05:08 Yeah, I'm… I'm good if CJO gives this, but… Thumbs up to merge it.
Alright, what do we got planned towards stabilization of… Recording errors… Oh, you have a PR, that might be…
**Liudmila Molkova** 05:38 Yep.
**Trask Stalnaker** 05:40 Relevant.
**Liudmila Molkova** 05:42 Sustory 311.
Let me send a link.
**Trask Stalnaker** 05:54 Oh. Or it just…
**Liudmila Molkova** 05:55 Types for 311.
**Trask Stalnaker** 05:57 Thanks.
311.
**Liudmila Molkova** 06:03 So this is a generalization from all the exceptions.
the naming and the severity.
I think Severity might need some… closer review. The naming is pretty straightforward.
Oh, right, so, the key part, we are no longer saying it could be logs or events, it should be events.
And… we used to say, okay, use something as record exception if it was provided. Now we have a real method.
That we're stabilizing, that we can reference here.
**Trask Stalnaker** 07:05 Do you want to reference it here?
**Liudmila Molkova** 07:07 It's, it's down there, line 54, yeah.
**Trask Stalnaker** 07:15 Oh, yes, yes, got it.
Okay, so, event name… I see transforming.
the instrumented operation.
I like it.
**Pellared** 07:47 Is it the only change in this one document, or not only this one?
**Liudmila Molkova** 07:52 There is also the non-normative how-to instrument.
Essentially, it's just this one document.
**Pellared** 08:02 Because I remember there was this example where you were suggesting the event name, in the recording errors, and I think we can just… I think we can just, you know, replace the name there, from error to exception.
**Liudmila Molkova** 08:16 I see that the exception spans the… or recording errors, right?
**Pellared** 08:21 Yes, yeah, I think we can just update this as well.
Together.
**Liudmila Molkova** 08:31 Oh, there is an event name there, so we're good. We can just… okay, but yeah, good point, I'll take a look if we need to update anything there.
**Pellared** 08:41 The change will be probably changing from .error as a suffix to dot exception.
If I read it correctly.
**Liudmila Molkova** 08:48 Yep.
**Trask Stalnaker** 08:52 And can we just reference this doc, or we need it in both.
**Pellared** 08:58 It's already referenced. I think it's already referenced this one.
**Liudmila Molkova** 09:01 It's a court example.
**Trask Stalnaker** 09:02 Oh… Thanks.
So, severity…
**Pellared** 10:08 mid-question, I think it's better to ask here than at a comment.
For the worn, for the worn level.
You say that they're expected to be handled by the application?
Do you think that it could be also kind of exceptions that… Do not require handling, and, you know, do not cause… I'm not sure how to capture it, like, you know, something is just, you know, like, degraded performance, but doesn't mean that something is crashing, things like that.
I don't… Clogged drifts is another example, like, I don't know, clogged drift.
**Liudmila Molkova** 10:52 Just something that says that there are… Excuse me. They are thrown, actually, not handled.
**Pellared** 11:03 Yep.
**Liudmila Molkova** 11:03 So, they are shown here, but handled… maybe handled, so emphasize that those are important ones.
**Trask Stalnaker** 11:14 Sorry, I didn't… I missed something.
Which… What was your example, Robert?
**Pellared** 11:24 So here, it kind of suggests that exceptions will be… Handled by the application.
But some of these do not… probably do not require to be handled.
They just mean that something is a little wrong, but doesn't mean that you know. It's… they need to be error. Like, I have an example, like, I don't know the… Few seconds, clogs drift.
Between…
**Trask Stalnaker** 11:51 Sorry, I didn't… that's the word I missed. I didn't…
**Pellared** 11:54 Drift. Okay, called the Drift.
**Trask Stalnaker** 11:56 Clock drift. Got it.
**Pellared** 12:00 I think if you get a warning, not an error, I'm not sure. What do you think?
**Liudmila Molkova** 12:08 If we think about the… the… narrow case, the one we have in OTL. We instrument, let's say, an operation, right?
And if we detect it's raw as an exception.
Right, if it answers an exception.
we would set it to worn by… default, but if… This is should, so if you know that That the separation… that this specific exception is okay-ish.
Then you could set it to something lower, and we have a… clause for it. I think what's missing here, two points. First, is that These are exceptions that are surrounded by the operation. It's not that It's something important.
It's just… the warrant is justified.
And the second is that I have a clause on Error above, saying that some exceptions are artificial.
Oh, 107.
This, I took it from your PR strask.
Maybe it should be… Higher.
Or it should be in multiple places.
It should apply generically, right?
Just for this section.
**Trask Stalnaker** 13:39 Yeah, I think in my PRs, this was only for the… I think I only added this to the client.
Ones, the worn ones…
**Liudmila Molkova** 13:55 But if it's spring, and somebody throws not found exception, Should it be an exception?
**Trask Stalnaker** 14:06 Is that… Is that how that works?
Makes sense.
Response status exception.
So, at… I know that Java instrumentation, at least, and maybe I'm too in the weeds, We… this wouldn't bubble up to our server instrumentation. This would be more like controller… If we were capturing the controller span, We would get it.
**Liudmila Molkova** 15:21 Mmm.
**Trask Stalnaker** 15:22 But this is handled… By… because spring is not really the… request framework. It's handling the HTTP request itself, where we instrument at a higher level.
**Liudmila Molkova** 15:36 Oh, the… the, like, Tom Cutter or something like that.
**Trask Stalnaker** 15:40 Yeah.
**Liudmila Molkova** 15:43 I see.
I see.
Oh, in case…
**Trask Stalnaker** 15:52 It doesn't mean there couldn't be frameworks that do that, and, like, your only instrumentation point is that framework.
**Liudmila Molkova** 16:05 So… I think this clause applies to all kinds of exceptions, then.
**Trask Stalnaker** 16:13 Makes sense, yeah.
**Liudmila Molkova** 16:20 I'm living in Clemente.
**Trask Stalnaker** 16:23 Yeah, and maybe just a couple examples to make that… I think… one with… I like that, not found, or status.
exception.
side and the client, any of the good examples on the client side?
**Liudmila Molkova** 16:48 And maybe we should say that the lowest severity applies, if, like, an exception can be… Can, in theory, apply to any of these categories, the lowest one.
should be picked.
**Trask Stalnaker** 17:17 I… what's your… I can quite follow, what's your example?
Oh, you're saying to… if you pull this out, then how does, like, how does that mix in with these?
**Liudmila Molkova** 17:38 And more like, let's say it's… yeah, so let's… let's say it's a warning.
And you know this exception is not a problem.
Then… where there is the info and below severity, so it don't indicate an actual issue.
It should be recorded with severity in 4 or below.
And this should have higher priority than, let's say, warning or error.
**Trask Stalnaker** 18:12 Yeah.
**Liudmila Molkova** 18:36 Okay.
**Trask Stalnaker** 18:43 Yeah.
I think it looks great.
I'll wait for your next… Updates.
But… I… Don't see any… I don't see any concerns.
**Liudmila Molkova** 19:06 It's extremely useful that you've sent all that PRs to define exceptions so we can generalize now.
**Trask Stalnaker** 19:12 Yeah, yeah.
**Pellared** 19:20 Alright. To-do list.
**Trask Stalnaker** 19:25 Sorry, what was that?
**Pellared** 19:26 I will add this PR to our discussions here, just in a moment.
**Trask Stalnaker** 19:30 Oh, thank ya.
Let's see, what… happening here.
Oh, this is at the spec. Got it.
Okay… Yeah, I think once we have that… Set… stabilize the set exception.
Then we… Probably could, I… Are people going to… are we… are we ready for people to freak out yet?
**Liudmila Molkova** 20:32 But they're now than later.
So we are planning to merge the… Stabilization by the end of the week.
And we can make them freak out on the next spec call.
Start freaking out.
**Trask Stalnaker** 20:54 Yeah, what I want to make sure is that we have, and I think we're… the PR that you have open, Ludmila.
On the event name and severity. Let's get that in first.
So that we have… I think once we get that in, we have a pretty… Good story for what to do instead of this.
**Liudmila Molkova** 21:30 And we should write a blog about it, because it's huge.
**Trask Stalnaker** 21:34 Yeah.
And we're gonna present in the, spec call in maybe a… Whenever we want.
2-3 weeks.
So we could sort of coordinate around Getting… aligning stuff for that.
Alright.
Yeah, yeah, I, I like it.
Let's get… let's get, yeah, let's get your PR in, Lyudmila.
And then… Let's mark this ready.
**Pellared** 22:24 Do you think we need stabilizing the record exceptions, semantical functions, or you don't think it's needed?
**Trask Stalnaker** 22:33 the… my PR? The set exception thing?
**Pellared** 22:37 No, no, no, there's one… there's one document which is about… because the thing about this PR, if you, if you check… yeah, this one, exactly. Do you want.
**Trask Stalnaker** 22:46 Okay.
**Pellared** 22:47 the one which is currently opened. Do we need this one as table as well?
**Liudmila Molkova** 23:01 It means that… Do we need the… contents of my PR to be stable.
Because it essentially says this is…
**Pellared** 23:13 Maybe below.
**Trask Stalnaker** 23:14 Oh… That's fair.
**Pellared** 23:23 Also, a question, is it masks or shoes?
But I think that the more we stabilize the mapping conventions, maybe the easier it will be… it will be later. I have no strong preference here.
**Liudmila Molkova** 23:38 So.
**Pellared** 23:38 But I think that it will make us easier.
For people, to accept the deprecation, the more we are prepared in the semantic conventions.
**Liudmila Molkova** 23:55 So the, the, the pass… for stabilization might look like… it probably aligns better with what we need for Java, that we're stabilize individual events, like HTTP, request, client, server, database.
And we can do it fairly fast, right? Because we just need some prototypes and existing instrumentations.
And once we have it stable, it's like stabilizing just the… the… What we already have done in practice.
**Trask Stalnaker** 24:33 Yeah, I like that. How about for the spec?
Overview, We can… hose… Pr ready to… Stabilize… Except, some con exceptions, errors… And… basically, sort of… Tried to freak people out at that point, like, hey, this is serious, this is coming, this is the new way.
We are going to… deprecate.
record exception.
As soon as this is stabilized.
**Liudmila Molkova** 25:52 So essentially, this pack call would be focused on all the stabilization efforts. That's it. Which makes sense.
**Trask Stalnaker** 26:02 Yeah, yeah, basically, that, hey, this is our… Our journey is… sort of completed here. And maybe we ju- like, okay, so is it general events, or do we just want to focus on exceptions?
**Liudmila Molkova** 26:22 Beyond exceptions, we just have the… event some DDoc.
Which is… 20 lines off.
Mark down, and we probably… There is nothing we would not… we are not ready to stabilize there.
Right.
Like, once the Roberts PR for the body clarification would work.
**Trask Stalnaker** 26:49 Right.
**Liudmila Molkova** 26:58 We can also probably look at the board.
I… I… Transfer some open issues.
Mmm, that were not on the board, or… Whereabout logs?
And the board should be… Up to date.
**Trask Stalnaker** 27:24 That's… yes, yes, yes, these are great.
**Liudmila Molkova** 27:45 This… maybe we should remove it from this board?
**Pellared** 27:50 Oh, God.
**Trask Stalnaker** 27:51 This?
What is this?
Alright, so much good one for span.
Life cycle… oh, this is the in-progress span stuff.
**Liudmila Molkova** 28:03 Yeah.
**Trask Stalnaker** 28:05 Yeah.
**Liudmila Molkova** 28:08 Oh, we have a related column, if we… Wanna keep an eye on it.
**Trask Stalnaker** 28:16 Fancy.
Right.
**Liudmila Molkova** 28:22 How to say we're not working on it without saying we are not working on it?
**Trask Stalnaker** 28:25 I love it.
Clarify…
**Liudmila Molkova** 28:34 Oh, I think it's waiting for me to follow up.
**Trask Stalnaker** 28:44 Okay, okay.
**Liudmila Molkova** 28:52 Oh, this one!
**Trask Stalnaker** 28:58 This could be good.
**Liudmila Molkova** 29:00 Yeah, this should be part of the deprecation, right?
**Trask Stalnaker** 29:06 Yeah.
**Liudmila Molkova** 29:23 And it's trivial.
**Trask Stalnaker** 29:28 Yeah, shouldn't be… Alright, I… Would it go in… Oh, it is in spec, okay.
Yeah.
This is done, yes?
**Liudmila Molkova** 30:01 The race.
I think it's not on this… well… I… I don't want this group to own the tooling changes to support defining. Yeah.
**Trask Stalnaker** 30:46 So what happened? Did we… we added this, but we haven't stabilized it yet?
**Liudmila Molkova** 30:51 Yep.
**Trask Stalnaker** 30:53 Okay.
**Liudmila Molkova** 30:55 And we have it in one place.
Cool, we would need more prototypes to stabilize.
**Trask Stalnaker** 31:05 Cool, I can add that to Java.
Limits.
**Liudmila Molkova** 31:34 Can we briefly chat about severity being required?
**Trask Stalnaker** 31:40 Yeah.
**Liudmila Molkova** 31:40 I think…
**Pellared** 31:42 I think this one can be assigned to you right now, it's basically your PR, right?
**Liudmila Molkova** 31:47 This one, yes, for semantic conventions. Yeah, I should close it.
I should put it as a fix for… Yeah.
Me.
I wasn't… I mean, the first one.
The first one in this list.
**Trask Stalnaker** 32:12 This one, okay.
**Liudmila Molkova** 32:13 I think it's separate, and I think it makes it required in a mid-log record, but we probably passed the point.
It's already stable.
**Trask Stalnaker** 32:47 Yeah.
**Liudmila Molkova** 32:52 I can… I can leave a comment that it's essentially impossible today without breaking that compatible.
**Pellared** 33:01 Yeah, that's correct.
**Liudmila Molkova** 33:16 Yeah, leave…
**Trask Stalnaker** 33:16 just come… Oh, go ahead.
**Liudmila Molkova** 33:21 Let's talk about this one, yeah. I like it, logger bridge. Logger name, logger bridge, and so on.
This is coming up a lot, but not in the…
**Trask Stalnaker** 33:30 Okay.
**Liudmila Molkova** 33:30 In context, just… let's just have scope attributes for instrumented library.
Whatever it is.
**Trask Stalnaker** 33:38 Right.
**Liudmila Molkova** 33:47 then I don't need to explain that GenAI framework is a bad choice for an attribute.
**Trask Stalnaker** 33:57 Oh, because we would have a logger framework?
**Liudmila Molkova** 34:02 No, because we would have not the logger framework, but the… Instrumented library name and instrumented library version in the scope attributes.
**Trask Stalnaker** 34:20 Okay, as general purpose… Yep. Instrument. Yep.
And that is, today, the instrumentation scope name, like, on spans.
It is the… oh, it's the instrumentation.
Name, not the instrumented library name. Okay.
Yeah.
**Liudmila Molkova** 34:45 Let's do it.
Let's do it, and it's the perfect… Place for us to start using instrumentation scope.
**Pellared** 34:53 Beatra?
**Trask Stalnaker** 34:55 Yeah.
**Liudmila Molkova** 34:58 So maybe it would not change… work for this SIG at all, right?
**Pellared** 35:05 Yeah, that's what I wasn't saying, to be related, or… yeah.
**Trask Stalnaker** 35:13 I mean, it's the… It seems log-sig related.
I mean, more than related?
**Liudmila Molkova** 35:24 related, but…
**Trask Stalnaker** 35:26 Oh, I see, it's a generalization of… yes, I understand.
**Liudmila Molkova** 35:30 Yeah, and it would not change any stabilization plans we have otherwise.
**Trask Stalnaker** 35:35 No. Yeah, I agree. Yeah.
But I would suggest we leave it on our board.
Here, since it's… Come up in the context of logs.
**Liudmila Molkova** 35:51 Yeah.
**Trask Stalnaker** 36:00 Alright, Let's… I.S. Limits.
**Liudmila Molkova** 36:29 Yeah.
**Pellared** 36:34 Oh, okay.
**Liudmila Molkova** 36:36 Do… a body… Makes sense.
Right?
So, ready to text.
**Trask Stalnaker** 36:55 Oh, sorry, I didn't even see that. Yeah, I mean, so body is… Not such a big problem for us anymore, given its lack of importance.
**Liudmila Molkova** 37:10 It is very important for bridges, right?
Okay. The main use case.
**Trask Stalnaker** 37:21 I guess those could be… Long… If somebody was dumping a whole stack trace in the text body.
**Liudmila Molkova** 37:33 They could build longer, this is why it's… it's… reasonable to set a limit on it, so I think what happens when you… your log body is too long, that your backend rejects it and you lose it.
Completely.
**Pellared** 37:54 I think the question was… Also, whether we could apply the same limits, which were used for attributes.
For body, severity, text, etc.
And I think we could do so, especially that we added this, any, any, value type to the attribute, or something like this, I don't remember right now, and added this definition even to the attributes.
Specification.
Yay. Okay, connect.
**Trask Stalnaker** 38:31 Curious, what are we doing?
Limit… Spam limits…
**Pellared** 38:47 Are you kidding?
**Trask Stalnaker** 38:51 Log record limit.
**Liudmila Molkova** 38:59 You know what? Sorry for interrupting.
**Trask Stalnaker** 39:02 Yeah.
**Liudmila Molkova** 39:03 We… We want to deprecate record exception.
And we have a plan for it.
But… We should have a plan for deprecating commute event. Oh, sorry, the record event.
And this is where the mapping quit.
Apply.
Oh, and eventually.
**Trask Stalnaker** 40:17 Let's see, so we have… So for spans, we have different kinds of… Limits… So we could have different kinds of limits.
for logs.
The severity text is weird. Do we really… I mean… Has that been a problem in practice that you're aware of, or that was just, like, theoretical?
**Pellared** 40:56 Just theoretical to have some limits.
**Liudmila Molkova** 41:00 I don't have, The limits on other fields that are, like, assumed to be short, like spend name, for example, right?
Or a status description.
**Pellared** 41:12 Fair.
**Liudmila Molkova** 41:19 And in theory, we could apply the same limits between body and attributes.
Maybe we can get away with it, but it's more… Likely that people want different ones.
**Pellared** 41:38 For body, I think that people may want longer display message.
Then the strings in the attributes?
Okay. Yeah.
**Liudmila Molkova** 41:51 And it kind of makes sense, because the, the, the…
**Pellared** 41:53 I think for map array count of array value, I think I already addressed this, I think it's outdated.
I think in one of my PRs, when I was adding this complex type to attributes, it's already solved.
So, Zillow.
**Liudmila Molkova** 42:11 Yeah.
**Pellared** 42:11 parts are body, and the subject doesn't make sense. So the only… so I think we can leave it open.
Unless nobody asks for the body, and for several text, maybe we can just say that.
We do not have any limit for, for span status, as you said, or name, sorry.
So, and… so, probably, yes, I don't know, postpone or rejected.
**Liudmila Molkova** 42:38 Yeah, so since body was there for logs already, and it didn't change anything around it, and it got stable without the limit.
Or you could say we can always set it once the complaint comes.
**Pellared** 42:54 For meta and arrays, we already have, so… It can be edited. For what?
For map NRA count, I think we already have We already have a limit. I think it's already described.
in the common README MD.
It's just the same.
Is this…
**Trask Stalnaker** 43:15 array… I didn't know we had an array, like, a count… array count limit.
**Pellared** 43:21 Not a separate limit, the existing limits are being applied.
If I remember correctly.
**Liudmila Molkova** 43:30 I think the ask would be that.
**Pellared** 43:32 If it comes.
**Liudmila Molkova** 43:34 That we have Like, imagine the limits as a structure, and it can be on their attributes or on their body.
And in theory, you could be able to provide two different limits at the same time.
But… And this one applies to attributes, not to the body.
**Trask Stalnaker** 43:57 Yeah, I think we're good separating… Those two… And I agree that body… As in, we're not leaning into body… we're leaning into body less than we were before anyways, so, it doesn't feel like a high priority.
The… One that I'm more interested in is… The, because it's kind of related to the complex attributes, is the size… limit of… The whole thing.
And so that's where I was curious, like.
attribute count, like, if I have an attribute count limit of 10, Can I have one array with 11 items in it?
**Pellared** 44:51 Yes.
Currently, yes.
**Trask Stalnaker** 44:59 So that's, I think, what…
**Liudmila Molkova** 45:01 No, no, wait, wait a sec, no.
**Pellared** 45:03 Can you.
**Liudmila Molkova** 45:04 What err.
**Pellared** 45:04 Quebec, maybe not. First, if I didn't get…
**Liudmila Molkova** 45:08 Now, here, it says that the… the limit to each… Oh, Value Lance, I see.
Discard the total number of attributes in an attribute collection.
Counting each attribute in the collection as one. What is it?
**Trask Stalnaker** 45:29 Here, if it's an array of strings, the limit applies to each value separately.
**Liudmila Molkova** 45:37 This is the value lens.
**Trask Stalnaker** 45:40 Right, right. The count.
**Liudmila Molkova** 45:45 The count is the second one, right? And here it says…
**Trask Stalnaker** 45:49 top-level attributes.
**Liudmila Molkova** 46:17 So at some point, we've been thinking about leaf nodes being counted.
But somewhere along the way, we changed it to just the top level.
And… I don't remember it, but if I can imagine why, we probably thought that maybe it's a separate config?
**Trask Stalnaker** 46:39 Probably, I don't remember either, but my guess would be we thought that it would… We would separately add, like, a total size…
**Liudmila Molkova** 46:54 Yeah.
**Trask Stalnaker** 46:55 Because the count is… Which… I mean, if we had…
**Pellared** 47:05 the reason… if I remember correctly, because I was making this PR, and I think at some point, I was adding these leaf notes, but I think one of the comments Was that if we add it to the existing limits, it can be a breaking change for some people.
And thus, they propose rather to have a separate limit for discounts of, you know, nested… nested elements.
Because people can, right now, rely on this behavior that they have a lot of, you know, nested, you know, structures.
And if they add the limit 10, they can, you know, some objects that are locked may be, I don't know, disappeared, or fragments of them are disappeared. So, basically, the preference was just to Keep the existing behavior undocumented.
And propose adding new limits instead.
**Trask Stalnaker** 48:03 That makes sense, especially because if we were counting leaves, we would want to count each… String, in an array of strings, so that… Would have been an existing… Unrelated to complex attributes would have changed the behavior.
**Liudmila Molkova** 48:21 Yeah, and… or it could change the behavior for logs complex attributes that were allowed.
Okay, so then, if we want to evolve it further, we would rather add a new, higher, top-level bullet point.
for the… Leaf nodes.
Or assembled at some top-level size.
We would define this.
Total size in some way.
I kind of feel that people are more interested in the payload size.
other than… Like, individual attributes, or the size of individual value within the map.
**Trask Stalnaker** 49:15 Yeah, at some point, you can't break up the payload, though, like, if you have one array.
That's just enormous, and we have no cap on that.
Like, you couldn't even fit one telemetry record into the payload size.
**Liudmila Molkova** 49:34 I don't even know what you could do.
**Trask Stalnaker** 49:38 I mean, that's where having a limit, a…
**Liudmila Molkova** 49:42 Yeah.
**Trask Stalnaker** 49:42 attribute.
**Liudmila Molkova** 49:51 It's extremely difficult to do. It would need to apply on the exporter level.
Probably.
**Trask Stalnaker** 50:07 I mean, we could have individual, like, have a single… Attribute total size limit.
**Liudmila Molkova** 50:17 Mmm.
Speaking from the… the limitation sense, it's more like either people have… the Azure Monitor has limit on attribute size, right?
I think many other backends limit the total payload.
And they would take whatever fits into this payload.
And it's two different knobs. The one is, yeah, the API, sorry, the spec, the other one is OTLP limits.
**Trask Stalnaker** 51:09 So, do we have… Let's see, the… Somebody reported… I'm just trying to understand if this is something that… We… is a priority now, or can be… driven by… future complaints.
**Liudmila Molkova** 51:29 I'm actually surprised how little complaints we get because of the GenAI stuff.
It's expected to blow up everyone.
And I know it should blow up as you monitor.
But yeah.
**Trask Stalnaker** 51:48 Except, as you say, like, if you have your… you're… You're gonna handle that either in your backend or your ingestion to truncate to the size that you support.
**Liudmila Molkova** 52:01 Mmm.
**Trask Stalnaker** 52:02 So the only advantage of doing it sooner is to save some resources.
I think…
**Liudmila Molkova** 52:30 Yeah.
**Trask Stalnaker** 53:20 Okay, I'll… Finish that.
Alright, cool. Oh, got some good work and a good plan, I think.
**Liudmila Molkova** 53:49 I have one small question to Robert.
And to your task.
Can you scroll up a little bit?
**Trask Stalnaker** 53:57 Yeah.
**Liudmila Molkova** 53:58 I added a topic with a link, so… We had this discussion about, attribute requirement levels on this exception stuff that we have.
So the question to Robert, do you folks populate both exception type and exception message?
And go.
**Pellared** 54:23 I need to double-check. Leave me a note, just in this… in the notes, and I will… Okay.
I can respond here.
**Liudmila Molkova** 54:34 Okay, I'd like to change this, I will do this, I'd like to change it to… Exception type… Should be either required or conditionally required, if applicable.
And same, maybe, on the message, is I… I… think that… It's kind of weird that we're saying neither one of them is required, and it's not helpful.
like… I think exception type is a great candidate for a dashboard.
Right, it's a grouping key, it's the metric aggregation thing.
the message… Well, it's super important, but on the individual event.
But both are… should be provided whenever possible.
**Trask Stalnaker** 55:39 Makes sense. And it seems…
**Liudmila Molkova** 55:40 Rust doesn't populate type, and I think they can. It's just… They probably use this guidance to provide as little information as possible.
**Pellared** 55:53 Okay, so, I found that… Right now… Or… For… we just… for one… One of the lock branches.
We just add the exception message.
I'm a little amazed that we do not add exception type or error type, but I think we have something for populating the error type, not the exception type.
But… We can probably just change it.
the name and use the value of the error type, because we just have some helper functions in the symmetry Conventions helper package.
That basically returns the name, of the type.
for the errors.
**Liudmila Molkova** 56:52 Okay, so… Alpha Law.
Upon this one, then, I would… yeah, the Go and Rust would be the… two languages with the weirdness around it. Hopefully, we don't need to get into exception versus error discussion there.
**Pellared** 57:09 We… the weirdness regarding error type, or which one?
**Liudmila Molkova** 57:15 And when somebody records an exception, like, Provides an error object.
to the log API, and you record exception message, it's kind of natural to also provide exception type, but not error type, because error type has additional meaning.
Yeah.
Anyway, we are out of time.
**Trask Stalnaker** 57:49 Alright.
Thank you.
**Pellared** 57:53 Thank you.
**Liudmila Molkova** 57:54 Yeah.
