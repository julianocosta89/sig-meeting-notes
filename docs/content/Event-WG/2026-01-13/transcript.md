SIG: Event WG
Date: 2026-01-13
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Pellared** 01:05 Hello, hello.
**Trask Stalnaker** 01:06 I remember…
**Pellared** 01:08 How are you?
**Trask Stalnaker** 01:11 Doing… pretty good. How about you?
**Pellared** 01:15 I'm good, thanks.
We have a lot of snow in Krakow since the few days, like… Like, for a town, which is kind of crowded, having, like, 40 centimeters of snow is, like, even on the roads, because it was just during one night, it's pretty amazing.
**Trask Stalnaker** 01:44 Is that, do you normally get snow every winter?
**Pellared** 01:48 Yes, every winter, yes, we do it every winter, but usually it's, like, at least in, you know, in towns, it's usually, like, a week or two, depends on the winter.
But when the suburbs, or near mountains, there can be no months.
**Trask Stalnaker** 02:11 Yeah, we get snow, I would say, every other year.
**Pellared** 02:17 I see.
**Trask Stalnaker** 02:17 One snow. Like, one snow where it actually sticks.
**Pellared** 02:21 One weekend, like, or not, or longer?
**Trask Stalnaker** 02:25 It depends. I'd say, yeah, on average, like, you know, a couple days.
**Pellared** 02:32 Yeah.
**Trask Stalnaker** 02:33 Occasionally, it will… will get, like, a week long, and it will, like, shut everything down.
**Pellared** 02:41 Yeah.
I'm not comfortable.
Oh, I have forgotten to place the date, yeah.
**Trask Stalnaker** 02:50 I got it.
Ding…
**Pellared** 02:57 Yes, 13 is correct.
**Trask Stalnaker** 02:58 So this one was wrong. Oh, no, we had an extra special meeting last Wednesday. That's right! I've already forgot.
**Pellared** 03:10 What key?
**Trask Stalnaker** 03:14 I need to page that.
**Pellared** 03:15 No, shut up.
**Trask Stalnaker** 03:16 Back into my brain here.
Longer.
Okay, I saw Lyd Miller.
Said she'll be here.
Just running late.
**Liudmila Molkova** 04:26 Hi, folks!
**Trask Stalnaker** 04:28 Hey, Ludmilla.
**Pellared** 04:33 Where did we leave it?
**Trask Stalnaker** 04:36 Okay, so you had opened… S… To not use span events. Card as… Yes, bypassing… the…
**Pellared** 05:10 I should change it to, log records. Here, I have forgotten to change it.
In this place.
Exceptions record as…
**Trask Stalnaker** 05:23 Oh, oh, this is the co-pilot instructions, gotcha.
So, we're deprecating… Reporting… Exceptions on… spans… The event name… So I do have the general concern about deprecating something before we have a stable… oh, but we decided we do have a stable… Replacement for this?
**Liudmila Molkova** 06:21 And the stable replacement is the log… Records.
**Pellared** 06:27 cash?
**Trask Stalnaker** 06:30 this guy…
**Pellared** 06:31 Catch.
**Liudmila Molkova** 06:34 Which is not an event, it's an attribute group.
**Pellared** 06:38 That's not cheap.
**Trask Stalnaker** 06:43 Okay…
**Liudmila Molkova** 06:51 Like, if we're… do this… It's equivalent of saying we don't… Document event name.
And leave it up to the caller.
To somebody who creates… A log record, and it can be… it can be nameless.
**Pellared** 07:19 Go back.
Do you, Rudumia, want to change it and add this event name as a proposal?
So just, Saty, if you think it's a very good.
**Liudmila Molkova** 07:34 So what I'm thinking, we should, expand this document.
And talk about the event name, the severity, here.
But… whether it's… It doesn't need to happen in the scope of your We'll request.
**Pellared** 07:59 Yeah, I agree. I think we've had the same consensus last night. We had a separate PR to find this document, which is already stable.
This is the third bullet point which I'd like to do to do.
In the agenda notes.
**Trask Stalnaker** 08:14 Oh, gotcha, thank you.
It's already there.
**Pellared** 08:19 Yeah, it's just…
**Trask Stalnaker** 08:21 Yeah.
So, deprecated… C, recording exceptions.
I mean, recording errors, recording… Errors, recording exceptions.
I see you made some changes there…
**Pellared** 08:59 The alternative is to, refer to the… span exceptions, semantic conventions. I was not sure whether to put one on the other. I like this more… as a reader, I'm not sure if I would not prefer the more, you know, like, high level. On the other hand.
maybe you should stay on the same level, and also, this is not a stable document. So we can change this, you know, this first… Yeah… yeah.
This is a reference to something else, if you have an opinion there.
**Trask Stalnaker** 09:54 I think my… I think my opinion, would be to… Hold off on deprecating this.
Let's make these other… let's iron out, you know, make these… this change, and… potentially… The event name and severity.
Into there, so that we can, sort of, When we deprecate, we can point people over to a little bit more full of the story.
But it… I mean, it could… I don't think that's… necessarily required. I think that is just a preference I have.
**Liudmila Molkova** 10:51 I… I… and my preference is not strong either.
Do… how do we feel about deprecating stable document in favor of development document?
**Trask Stalnaker** 11:02 That's the part that I… Don't.
Love, yeah.
I would… I would like to get the… all the other stuff.
table, which… is this one?
Oh, I see, this one is not stable, is what you're saying.
**Liudmila Molkova** 11:25 It's only snow.
**Pellared** 11:27 But logs, exceptions on logs, or something like that is stable.
But we should refine it anyway, right? Regarding severity and event name.
**Liudmila Molkova** 11:37 What we're going to write there regarding severity and event name, we will provide some guidance on… Event name, that it should be anything, right, that you, find useful.
Some considerations, maybe. And for severity, it would also be okay. This depends on the context.
Here are the considerations.
The sections could be in development.
The document status will be mixed.
But… I feel it will be equivalent replacement, because Have an event name set to exception.
Versus having exception.type as an attribute is pretty much the same.
Filter.
**Trask Stalnaker** 12:34 What if we, Robert, what… why did you pick… This versus, yeah, pointing to the stable dock.
**Pellared** 12:44 I think it's better with Stepping Dog. This is what I post right now during the conversation. I'll change it back. Can you add a comment?
**Trask Stalnaker** 12:51 Yeah, yeah.
**Pellared** 12:53 Just reference, yeah, let's point to the stable span.
Spanner also, yeah, stable lock, blocks.
**Trask Stalnaker** 13:05 Okay.
Yeah, I think that's… Good, and then… yeah, you're… I guess… I think that would be fine, then, whether or not we… We can add the event name.
And severity afterwards.
**Liudmila Molkova** 13:25 I've been, thinking about the severity, I think we have it in our tab today.
It essentially doesn't have to be. This is a semantic conventions.
concern on what severity to recommend. We can just extract it from the ATAP, Maybe clean it up, and edit the semantic conventions, and then it makes… add a link from DotApp if necessary.
**Trask Stalnaker** 13:53 Yeah, I like that.
I think, will help also to… That sounds like a… small piece to extract. I mean, it's not small, it's big. I know it's a big part of that OTEP, but, like, at least it's one… Breaking that OTEP out… up a little bit.
**Liudmila Molkova** 14:35 Quote.
**Pellared** 14:42 Have you tried to also open to your PR, or the spec, or not?
**Trask Stalnaker** 14:49 the… add…
**Pellared** 14:51 The first one. Yeah, I added as the first one.
the agenda.
**Trask Stalnaker** 14:56 exception… Yeah, let's see where, we're… Now… it… Okay… So… If you may… Except the following… An exception or error.
What do you mean by error value versus error?
**Pellared** 15:49 It can be an error.
**Trask Stalnaker** 15:51 Okay.
**Pellared** 15:53 You can edit it, yeah.
**Trask Stalnaker** 16:02 I'm good with this.
Ludmilla Does this make sense?
**Pellared** 16:09 My reason… suggest it, it's just, it's less comfortable, sure, maybe for some languages.
**Trask Stalnaker** 16:16 Whether it's actually called exceptions or not.
**Pellared** 16:21 That's one, yeah, it also allows it to add it to Go, to Rust, if we… any of us would want to add it later, but the same API, we see the same, you know, performance improvements.
Or similar, which notices will be needed.
**Liudmila Molkova** 16:38 Okay, and if some language does not add exception… set exception API, it's not the end of the world, because they can always set it later to enable all the cool scenarios and optimizations that… We want them to.
**Pellared** 16:53 Yep, exactly.
That's also why I also added this, for example, enabled methods in logs, metrics, also as made, as far as I remember. Never as should.
This performance optimizations, for the same reason.
Even though most languages already support it.
**Trask Stalnaker** 17:16 Cool, I'm gonna leave this discussion open for another day, because I do think this is an interesting question.
**Pellared** 17:26 to see…
**Trask Stalnaker** 17:27 responses too, but then… but yeah, I will accept this. Change.
Thanks.
**Pellared** 17:35 But regarding this question, can you just show to the comment?
Rust is also bridging Arrow. Yeah, we are also doing it in Go, but should the question be… Do you want to have an API for it?
Or they did it in Rust.
**Liudmila Molkova** 17:54 The question to me is, when you record Rest ever.
as exception.type and exception.message, are they happy with it? And the same question to you, like.
There is an opportunity to change it now, and… If you have any regrets, it would be useful to know.
**Pellared** 18:19 It's fine.
Nobody complained.
**Trask Stalnaker** 18:26 That's… no, that's good feed… that's… that's good feedback. Yeah, because I agree, Lydmilla, that's my question also, is, like… Do they… is it weird? Do the language… communities… Find it weird to call it exception.something.
**Pellared** 18:47 The thing is that a lot of people who then read these kind of things may not be even, you know, understanding what are the differences between the, between the languages.
like, the SREs, etc. They may just see, oh, something happened, something crashed, oh, I see exception message. That's the reason why I do not think, you know, having exception message is wrong, because, you know, for… guys, for SREs, it does not really matter.
They just know that something crashed.
Or, you know…
**Liudmila Molkova** 19:20 The key is… it doesn't. It didn't. But it's also true for exceptions.
**Pellared** 19:25 Yep.
Yep.
**Liudmila Molkova** 19:29 Oh, but use it for panics. You don't use it for… If somebody.
**Pellared** 19:33 No, no, no.
**Liudmila Molkova** 19:34 Insurance scenario.
**Pellared** 19:35 We use it for errors. We do not do it for… yeah, we do it for errors.
**Liudmila Molkova** 19:40 Oh, for everything, if you, if you get… okay, Going.
**Trask Stalnaker** 19:52 What do we have here?
Oh, I see, okay.
I kind of look at that. That's just a precedence question.
Alright, cool. I will, so I think we're in good shape there. I have a couple of follow-ups.
This is… yes, this is your PR that we looked at.
Alright, I think that's some good… Progress… Anything… I'll… What's… Do we want to just try to close out those first, or do we want to think about what's… Next, after that.
**Pellared** 21:03 of a question.
do we need some guidelines for writing log appenders, or log bridges? Do you need something like that for, I don't know, Python, or for Java, or is it no longer needed? Because everything is already there?
**Trask Stalnaker** 21:24 There are a… Decent number of questions, open questions, I know in Java, appenders… Let's see if we have it… Like… So they're kind of like a bunch of miscellaneous Questions, Yeah, like, how to record structured attributes, how to record parameters, how to record different things.
**Pellared** 22:24 Is this something you want to… you want me to work on, or not really? You think it's not right now the priority, to even start working on it?
just to… I think we can tackle it later, but I think we might just want… we may want to have… create a separate document in specification, probably, maybe also systematic conventions as well, but probably post… post-working on, you know, post-deprecating span events, just to not have too many things at the same time.
**Trask Stalnaker** 22:56 I mean, I'm good either way. This is… these things in Java are on my… Short list of things for our next major version bump.
So probably in the next month or so, I will think about Be thinking about them.
I do think this, like, this has… as long as we are sticking, as long as people don't have regrets about exception, and we are moving forward with exception, that helps to clarify a lot of the confusion that I had maybe created, around.
Whether we wanted to revisit error, dot stuff.
Sorry, light.
Yeah, no, go ahead.
**Liudmila Molkova** 24:00 So perhaps we… Should… Deprecate error message.
**Trask Stalnaker** 24:10 Yeah… Right, so we had discussed… The log body is the message, and severity… is, I think that's what we had discussed.
**Liudmila Molkova** 24:42 Hmm… Err… is the message, and severity sees if it's an error. Alright, so let's, let's try to apply it to feature flags who use this guy.
So they have… So they have this feature flag evaluation.
They will have… They don't have severity.
So, what we would recommend them to do.
Bye.
Providing the guidance is to… Set severity to error if evaluation has failed.
And… Wow, not to error.
Because we don't know if it's final.
Okay, so they will… it could be a warning that… that… that… In the grand scheme of things.
Feature flag evaluation failing is not something that this… The end of the world.
It's warning at worst.
**Trask Stalnaker** 26:12 Right, right.
**Liudmila Molkova** 26:14 And… They would… if it fails, they would record their type.
And they would record feature… they would… would record our message as the string body of the This logo record.
An alternative is they would record it as featureflag.error.message or something.
specific to them.
**Trask Stalnaker** 26:50 Right.
And then probably… Go ahead.
**Liudmila Molkova** 27:11 We probably should also, if we want the log message, body.
To match the error message, which should… Added to this log exception document.
**Trask Stalnaker** 27:35 So, Andre, I'm thinking about as a… oh, sorry.
Thinking about it as, the… in a dashboard. You're looking at this feature flag.
Stata, you're looking at these events.
You… Care about using severity Somehow, and error type… to… flag… Things that you want to look at.
Across all events.
Severity. Primarily severity, I guess.
Across all events.
What is your dashboard?
Let's see… event… So it's severity…
**Liudmila Molkova** 29:00 Like, event name and message.
**Trask Stalnaker** 29:08 Right, event name… What is message?
**Liudmila Molkova** 29:17 Oh, sorry, the body.
**Trask Stalnaker** 29:20 Body, okay.
body… Great name.
Body.
This would be kind of your traditional-looking, like, log.
File.
**Liudmila Molkova** 29:39 Yeah, like, logger timestamp.
Well, the logger is… Effectively part of the event name, if it's really unique, so you probably don't even need a logo.
In this new world.
Oh, you need it if there is no event name, or… okay, so this is event-specific dashboard. Okay.
Anyway, not important, probably.
**Trask Stalnaker** 30:42 So, does body make sense… I mean, Ian… Events, we're telling people to encode things as attributes.
Is body just, like… Yeah, a little weird to put things in body.
Not sure what body represents.
**Liudmila Molkova** 31:15 this… I agree with you.
for events dashboard, but it does not make sense. For logs dashboard, It does.
**Trask Stalnaker** 31:42 This is where there was a discussion a while back.
about… event dot… Summary… But… It's kind of, I think… For that idea.
**Liudmila Molkova** 32:17 So if event summary is a human-readable representation of an event, Why attribute Vinead?
Body.
**Trask Stalnaker** 32:28 Could be. We could say that body is… For events, that is kind of the meaning of body, is… a string…
**Liudmila Molkova** 32:49 This kind of marries events and logs.
Because… It… it… There are a bunch of disc… well… Robert have seen it, we had a fun discussion, about it, in… on Grafana YouTube with Jack and some other folks, where we talked about, like, the trade-off between human-readable things and logs versus structured things in events. And sometimes you need both.
you want to return a human-readable, I don't know, error message to your users, but you also want it to be consumable.
In structured manner.
They are redundant, and maybe consumers can opt in into one or another, or both if they want to.
**Trask Stalnaker** 33:47 Does that… solve the, feature flag problem.
**Liudmila Molkova** 33:59 I don't think so, because, like, if we want it, if it is a human-readable representation, it should be, okay, I evaluated this feature flag, and the evaluation failed with this message.
So the message is an attribute, then.
**Trask Stalnaker** 34:15 Right.
And so… Okay, but then it could be… right, it could be a featureflag.error.message, potentially… Because we don't need the unifying aspect of error.message for these dashboards.
**Liudmila Molkova** 34:39 Right.
Right, it's not a grouping key. It's high cardinality.
Their type should be… If you put some attributes, promote them to the top-level properties on the dashboard, the error type would be The one you promote.
**Trask Stalnaker** 35:01 Oh yeah, event names…
**Liudmila Molkova** 35:26 I, I can… Send a PR, because I think… at some point.
We recommended feature flag folks to generalize it.
And they… I think they are actually waiting for the stability of the things to stabilize feature flex.
I can send the PR to deprecate it and switch to feature flags, and we can gather their feedback this way. Maybe they will be even more happier about this change the NSID gives them.
Way forward.
**Trask Stalnaker** 36:02 Cool. I think that sounds good.
Yeah, it feels like we need more… more reasons, like error.message, Needs to have, like, some… Strong use cases behind it to add it, and it doesn't feel like we have that.
Yeah…
**Pellared** 36:53 Thanks so much.
**Trask Stalnaker** 36:59 Alright.
**Pellared** 36:59 I added one… I added one bullet point at the end.
But… let's timebox it, because I may be overthinking, I was just trying to… put a second, like, another pair of hats, so basically, another hat, just a reviewer, and tried to be nitpicky towards, kind of, myself, or someone who reads the… as someone who reads this document. Yeah, I was just having this kind of thoughts.
And, yeah.
**Trask Stalnaker** 37:31 Let's see this… the context here…
**Pellared** 37:35 Yeah, it's not here, I can put it again. The thing is about the place when we rethrow the exception in this example.
Throw… throw X.
Maybe just open the document, yeah, it will be easier.
**Trask Stalnaker** 37:58 No, I lost it, sorry.
Okay.
**Pellared** 38:07 Because we are logging… there is a section which says that we should only record an exception once.
But if we rethrow an exception, then, you know, the caller can also log it.
So, I was just thinking of how we should… documented, like, where is the place it should be, you know, like, locked, or basically. So, it's not even a problem in my PR, It's an existing problem of the document, which makes it a little, maybe not clear what this sentence mean.
My impression is that if you have an instrumentation library, you should do it only once.
And when you… we are also an application author, you should probably also make sure that whenever you create an error, you should only log it once.
And there's nothing that, that will prevent logging twice, like, by the instrumentation library, and also by the caller. If he finds an exception and stepping, he can always, you know, have two logs or whatever.
**Liudmila Molkova** 39:17 So there was a comment before that line on line 100.
wealth, that says that we are recording it here, assuming it was not recorded inside create method.
So what the…
**Pellared** 39:34 Yeah.
**Liudmila Molkova** 39:35 I think I've tried to… Express and .tab that wasn't merged, is that you… as somebody who handles exception for the first time, assuming you know you're the first, or can guess you're the first, it makes sense for you to log it, because this is where you have all the about it. And your colors… should be thinking about, okay, the… this is my code, and I already see… I already logged it there, I shouldn't log it again.
Or… Okay, this is something.
**Pellared** 40:17 That's my contacts.
**Liudmila Molkova** 40:19 Yeah.
And then, essentially, what it means, that log exceptions where they are first shown. Don't log them when you risk row, unless you know they are not locked there. Alright.
**Pellared** 40:40 I think we are…
**Liudmila Molkova** 40:43 But… I think Trask, you suggested it, sometime.
**Pellared** 40:48 Can you repeat? Can you repeat your last sentence? Because I'm sure if I misunderstood, or maybe it was not good for me.
If you, if you misspell the exception, so if you throw the error, Then, you should lock When you're not sure if it's… if it's captured by the client, the color?
**Liudmila Molkova** 41:11 So when you do new exception or return new error, you should always log it in the place where you instantiate new error or exception.
And throw it.
**Pellared** 41:24 Okay.
**Liudmila Molkova** 41:25 E. Oh, that's.
**Trask Stalnaker** 41:26 For application develop… and library developers.
**Liudmila Molkova** 41:30 Right, for application and library developers.
**Pellared** 41:33 Stop?
**Liudmila Molkova** 41:34 Or… If you use some library, then you kind of can use your best judgment, do… does it log the exceptions in a good way? Does it log them at all? Is it the same login framework? And so on.
For instrumentation libraries.
That…
**Pellared** 41:55 It's the same as the, like, the outer, I was saying.
**Liudmila Molkova** 42:00 Yes and no, because the library is already logging these exceptions.
Usually.
**Pellared** 42:07 In some way.
**Liudmila Molkova** 42:08 But it's a different question whether it's logging them in the way we want them to log them, probably not.
**Trask Stalnaker** 42:17 But it still creates duplic- like…
**Pellared** 42:21 F…
**Trask Stalnaker** 42:21 I think probably what you're getting towards, Lydamila, the… my preference is to only, for instrumentation, to only log it when it's the outermost.
to…
**Liudmila Molkova** 42:38 Yeah.
**Trask Stalnaker** 42:39 the duplication.
**Liudmila Molkova** 42:40 Yes, but… so what you've mentioned at some point, that… Assuming we can't… People would log this freaking exceptions on every hub when they, re… even re-throw them.
It… The level of duplication, we control with… we can control this verbosity.
**Trask Stalnaker** 43:09 Severity, yeah.
**Liudmila Molkova** 43:10 Yeah, the severity. So, if you re-throw it.
Probably it should be debug or something.
And only if you know you're the last in the chain.
For the instrumentation library that you set it to error.
**Pellared** 43:33 That makes sense, yeah.
**Trask Stalnaker** 43:35 I like that, and I think that's part of, what Lyudmila's, That… my understanding is that's this, right?
**Liudmila Molkova** 43:45 Yeah, yeah, so the severity piece, and then… We can leverage the severity piece to… the rub, unnecessary exception details, which is primarily stack traces. If we just… Control stacked traces, the rest is not such a big deal.
**Trask Stalnaker** 44:10 So, Robert, I would… So just kind of try to sidestep the question in your PR.
**Pellared** 44:16 I just wanted… yeah, I would just resolve it. I just wanted to make sure that we… I have… I have the understanding.
That's at the core of these documents right now.
I will resolve it, thanks.
**Trask Stalnaker** 44:35 All right.
**Liudmila Molkova** 44:37 Yay!
We're done?
**Trask Stalnaker** 44:43 Go forth and prosper.
**Liudmila Molkova** 44:47 Thank you.
**Trask Stalnaker** 44:48 Thanks.
Bye.
**Pellared** 44:49 Hi, thank you.
