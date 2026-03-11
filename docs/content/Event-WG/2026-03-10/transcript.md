SIG: Event WG
Date: 2026-03-10
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:46 Hey, Robert!
**Pellared** 00:47 Because I'll trust.
I'm just for, like, 15 minutes today, because there's…
I realized that I missed the spec meeting, because right now there's a 1 hour time travel.
**Trask Stalnaker** 00:59 Ha! Yes, yes.
Three weeks of confusion here.
**Pellared** 01:06 Yeah?
And the funny thing is that my mother-in-law, like, on Saturday, she said, oh, the clothes are changing. I was just, what? What are you talking about? And she can't write, it's just not bullet. Yeah.
**Trask Stalnaker** 01:21 Yeah.
**Liudmila Molkova** 01:25 Hello!
**Pellared** 01:27 alone.
**Trask Stalnaker** 01:29 We've only got Robert for 15 minutes.
**Liudmila Molkova** 01:32 Oh, no.
**Pellared** 01:36 Time travel, one more word.
Yeah. Because the U.S.
**Trask Stalnaker** 01:41 Did a boo-boo.
Actually, I like it. I like more daylight savings.
**Pellared** 01:49 So, I can't complain.
Demo, I saw that you…
in the morning, that you updated the PR, and probably addressed all the comments, but I haven't got a chance to review. I wanted even to review your PR before I addressed your comments in my PR. Is it correct?
**Liudmila Molkova** 02:16 Yeah, I, I updated the PR whenever you have time.
**Pellared** 02:21 Like, in 2 hours, probably.
**Liudmila Molkova** 02:25 Even in two days is fine.
**Trask Stalnaker** 02:30 Alright, let's look at… The blog post.
**Pellared** 02:38 My main question is, should I remove the stuff about the collector?
There were questions about the performance.
Of… it's questionable how they'll implement it, because… Log… logging and…
trace… traces, or spans and logs are separate pipelines in Collector, so they'll need, I don't know, to cache
So… dispense or something like that, to attach them later to span events, which probably will be…
Not ideal, so probably it's better to do it just in the SDKs.
And just skip this, because it can just bring confusion.
Make it shorter.
**Trask Stalnaker** 03:35 I support removing it.
**Liudmila Molkova** 03:41 I should.
**Pellared** 03:44 Et nous du mi.
**Liudmila Molkova** 03:45 And for us to rather remove, because it's not the solution we want people to go with.
**Pellared** 03:50 Yep.
were there any other kind of structural, important comments to the Mua? Because I kind of… I think I agree with all of them.
I think there's only one, which I haven't…
processed yet, but I think all of your comments were legit.
**Liudmila Molkova** 04:11 My main, idea is that we should explain why we're doing this in the beginning, before diving into the details.
Because people will be… Questioning, why are we doing such a big change?
Yeah, and you already moved the deer?
Or maybe I just had some… some thoughts on what we can explain better, that, log signal.
**Pellared** 04:39 Yes.
**Liudmila Molkova** 04:39 It's just about our data model for the… and, like, this is more like implementation details of what
How it's done today.
And other than that, it's just, okay, let's make it just… just…
shorter. Like, there are things we can probably…
explain with less level of detail, so less words, because people who read blog…
**Trask Stalnaker** 05:07 Very long to me.
**Pellared** 05:09 You have…
**Liudmila Molkova** 05:15 So no, no conceptual problems, just… just cosmetic stuff and, like, structuring it in…
The most important to the details down.
**Pellared** 05:29 Okay.
**Trask Stalnaker** 05:33 Do we want to mention anything about the environment variable?
That… instrumentations… Can start using to opt-in.
**Pellared** 05:51 But do we have anything like that right now?
**Liudmila Molkova** 05:56 We do.
**Trask Stalnaker** 05:57 We do.
**Pellared** 05:58 for span events.
**Liudmila Molkova** 06:01 logs, exceptions.
**Trask Stalnaker** 06:03 Oh, yes, only for exceptions, yes.
**Liudmila Molkova** 06:09 Should we have a config for instrumentations, too?
Use… logs?
Just in general?
**Trask Stalnaker** 06:26 Hmm… We don't have any… do we have any semantic conventions that are…
I guess there's some Gen AI stuff that people might be emitting on span events still? No, they've gone to logs.
**Liudmila Molkova** 06:42 It's… it's not in SAMConf. The SAMConf says logs, I think.
**Trask Stalnaker** 06:46 Yeah.
Good, good.
So this is… this is the one, Robert.
**Pellared** 06:54 Oh, shit.
**Trask Stalnaker** 06:55 Yeah, it's… for exceptions…
**Pellared** 06:59 Probably it was during modifications.
**Liudmila Molkova** 07:06 And for things like the instrumentations, actually, some of them emit RPC messages, but we don't want them to switch to logs.
Yeah. Yeah.
**Trask Stalnaker** 07:25 Yeah, I mean, on the Java side, this is the only thing I feel like that I need.
**Pellared** 07:34 Okay.
So, I will reiterate on this.
**Trask Stalnaker** 07:45 Cool, thanks for doing that.
**Pellared** 07:48 Yo.
**Trask Stalnaker** 07:49 In order to help with… Recording exceptions.
Yes.
**Liudmila Molkova** 08:11 So, and it would record… Log record.
**Pellared** 08:16 It's 4 spans, so… I'm not sure it's about adding this, setting the message.
And adding the… adding the exception attributes to the span.
I think the exception type?
And I think this is only… and maybe Stax Race.
to the span.
**Liudmila Molkova** 08:43 Or is it a… like, it could be fun to say set status, and then… Bus exception.
**Pellared** 08:55 Yeah.
**Liudmila Molkova** 08:56 Or… What would it do? Like, do we just set the status properties and… Maybe our type of nutshead.
**Pellared** 09:05 I think only… I do not remember right now, setStatus and end were separate methods, right?
**Liudmila Molkova** 09:14 ER, yeah.
**Pellared** 09:15 And I think we should keep it this way, because there's also, even in the recording errors, there is also a language that an exception may not always be an error, and I remember that there were some cases.
Mmm… Set… not exception. Set status is just message.
Or…
**Trask Stalnaker** 09:39 It's a… Ludmila's saying we could add, status exception.
**Pellared** 09:45 But I will… Just additionally,
I thought only about adding something like setException, or I don't know setException attributes, or end withException.
**Liudmila Molkova** 09:57 This is the question of, do we want to record exception attributes and spends?
**Pellared** 10:04 Yes, so… Go, we want, because usually it's all everything we need.
Usually, we just return error, so this is, like, the status of, kind of, This is basic… this is…
What happened?
So right now, when there is a… there's a method, like, I don't know HD constratician, or whatever, when it returns error, we just set, we set the status to error, and we set… we set the description as the exception message, and we set the error type as the type of the error.
**Liudmila Molkova** 10:38 Okay, so Dan…
**Pellared** 10:39 choices.
**Liudmila Molkova** 10:40 I see. So then, this… this guy…
But for Go, you don't need…
exception attributes, and hence, you would Set status quo to Error.
Description to message, and maybe if there is…
**Pellared** 10:58 Right now, we are adding error type. Maybe we can change it to add… to switch to exception type for consistency.
**Liudmila Molkova** 11:05 N- The error type is the consistent one.
**Pellared** 11:10 Okay. Perception?
**Liudmila Molkova** 11:11 And then, if there is no error type on span, right, because, like, the instrumentation could have said the error type before you do something more specific than the type of the…
**Pellared** 11:23 Yep.
**Liudmila Molkova** 11:23 Exception.
And then you have no case for a stack trace.
For gold.
**Pellared** 11:33 We have, but it's the next case. We may add it.
There is one library which generates errors, and when it's creating error, it creates a stack trace, but…
Usage is dropping.
Because of the overhead.
**Liudmila Molkova** 11:50 I think we wanted to set exception attributes and spans at some point, the spend ending exception, and we got the pushback that it's inconsistent, so sometimes you would find exception information on spend, sometimes on logs, and we decided that it should always be on logs.
This, it would be cool, but I also feel it could be…
Nothing stops SDKs from providing it as a convenience today, or having it co-generated for semantic conventions.
**Pellared** 12:27 But it needs to be an API, and at least in Go, we do not want to add anything on the API
Unless, yeah, this feels more than just opinions, because it also touches the semantic conventions.
**Liudmila Molkova** 12:42 The only semantic convention it attaches is the error.type, right?
**Pellared** 12:47 Or exception stackplaces, maybe.
For other languages.
**Trask Stalnaker** 12:53 That's the one where I think we're…
Need to discuss more if that's on the table, because…
Of… Maybe unnecessary telemetry.
Well, would you then capture it also on… The exception, the log record?
**Pellared** 13:15 I think David Ashbaugh thought about have been emitted into waste.
But because for Go, this is just, you know, just duplicating this error type, and message, we still… it's just about one attribute, so it doesn't feel like unnecessary telemetry, but I think you're right that for other languages that have exceptions, it might be just, you know, unnecessary bloat.
If that's what you are thinking, Trask, too.
Sorry it's been your.
**Trask Stalnaker** 13:46 Yeah, I wouldn't wanna… I wouldn't want to record it in both places by default.
You bet. But at the same time.
**Pellared** 13:56 We think that having the information about the error type
It's probably, it's probably good, even if it is in two places.
**Trask Stalnaker** 14:06 Having which?
**Pellared** 14:07 There are type attributes.
**Trask Stalnaker** 14:09 Oh, yeah. Yeah, yeah.
**Pellared** 14:10 It's good, and the description as the error message is just the de facto standard, basically.
**Liudmila Molkova** 14:29 do they capture this, right? We're talking about logs, capturing both on logs.
Okay.
**Pellared** 14:38 I need to drop.
**Trask Stalnaker** 14:39 Okay.
**Pellared** 14:40 Thanks anyway. Bye.
**Liudmila Molkova** 14:42 Thank you. See ya.
Do you want to talk about, this, or…
**Trask Stalnaker** 14:53 Let's bump it to next week, because I think it needs Robert.
And it's super not.
urgent right now.
**Liudmila Molkova** 15:01 Okay.
Cool.
**Trask Stalnaker** 15:06 Yeah.
**Liudmila Molkova** 15:10 Done?
**Trask Stalnaker** 15:12 Let's get a few minutes back. A lot of minutes back.
**Liudmila Molkova** 15:14 A lot of minutes back. Thank you.
**Trask Stalnaker** 15:17 Bye.
**Liudmila Molkova** 15:19 Bye, see ya.
