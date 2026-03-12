SIG: Python SIG
Date: 2025-09-18
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 04:50 Hello, everyone.
**Shuwen Pan** 04:58 Hello.
**Riccardo Magliocchetti** 05:48 Before starting, in the meantime, please add yourself as an attendee.
to the… Sign notes… And also, if you have any topic, Thanks.
**Aaron Abbott** 06:15 Hey everyone, how's it going?
**Riccardo Magliocchetti** 07:33 Okay, I think we can start. Welcome again to this week, service motorbike. To this week, fantasy call.
Yeah.
For new people, please add yourself as an attendee to the notes.
I've shared the link in the chat.
And… Also, like, please add any last-minute topic, if you have one.
Okay, so the first topping is from me.
And it is the… An overview of the log stabilization PR we are currently open.
I opened up this issue, and I created a vis table listing all the PRO issues, but it may break, the… API or the SDK, and a brack for users or downstream users.
And yeah, I also shared in a comment, like, a possible plan on how to… No, the, the… Serialization, as in the order in which… Applying these changes.
So, yeah, please take a look.
And any comments?
If anyone has already read it and does… Some comments?
We can discuss right now. Otherwise, we can just… Interact, in the… in the issue until we have some… Conclusional.
or agreement.
Okay, so no comments?
And… okay, so we can move to the… Next, topic from Keith.
Other days?
JAI, yeah.
**Keith Decker** 09:57 Hey guys, so this is a cleaned up PR of the other one we've been working on over the last couple of weeks. Went ahead and just kind of compressed our Git history and cleaned up a few of the things from Dialin. Looking for additional feedback on this, as well as, getting this thing moving.
So this is for… creating spans around, LLM invocations. We have… PR is coming as fast follows for doing metrics and events, and… Yeah.
**Aaron Abbott** 10:36 Dylan, you around?
**Dylan Russell** 10:38 Yep.
Yeah, I'll take another look at this.
Yeah, when I looked at it, like, yesterday, I think, it looked like the the Git history was, like, screwed up.
**Keith Decker** 10:51 Yeah, there was a merge that happened on our end that… blew it up, so this is a new clean one to get rid of that, so… I did link them between each other so we can go back and forth for comments if we need to.
Enclosed the old one.
**Dylan Russell** 11:07 Okay, nice.
Yep.
We'll take another look.
**Aaron Abbott** 11:14 Can I… I was just, I haven't taken a look at this one, but, actually, Ricardo, maybe you could click on the code, the file's changed.
I know that there was some, like, overlap with some of the stuff that Dylan was working on, so, like, the types, I think, were, like, slightly different.
We merged that other PR in already, which I'm assuming that we rebased these together, but…
**Keith Decker** 11:42 Yeah, I just repased this from Maine this morning, so it has the updates you pushed.
So Should be up to date.
**Aaron Abbott** 11:52 Okay, and then there's some, like, link chain kind of specific stuff with UUIDs, I think we… do we…
**Keith Decker** 11:59 So we… We took the run IDs out of being required, and now it'll generate a internal UUID if one's not provided in order to reference the span token, so that we can end the span later on. So it's not required, but we do still keep one on the LLM indication, just as an internal identification.
**Aaron Abbott** 12:26 Yeah, I mean, this… feels kind of, like, I don't know of any… anybody besides Blankchain using UUIDs like this. Like, we have… It's pretty much the same purpose as the trace ID, spend ID, right?
**Sergey Sergeev** 12:47 Yeah, in general, it's just asynchronous callbacks in a link chain, so… When you get Quebec to start a warming vacation, you need some identifier to basically to end it, and one chain maintains it.
That's the one very use case, but we started from it.
**Aaron Abbott** 13:09 Yeah, yeah. Like, I was wondering, because I think the lane chain VR is, I approved it at least, I think it's pretty much ready to go, and it has some of the same code. So I guess I was wondering, could we refactor those parts into the Langchain one, and then keep this one pretty much, like, pure Botel.
That makes sense.
**Keith Decker** 13:29 Yeah, I can take a stab at removing… all UUIDs, and what, we're just pulling the trace ID off of the context, then, to return as a… as…
**Aaron Abbott** 13:41 Yeah, yeah, so, like, most, since this is, like, an instrumentation API, the kind of usual thing in OTEL is there's the implicit context, which you can get, so you could call, getSpan from context, or you could pass the context object, which contains, in addition to the actual active span.
you know, like, whatever other context keys people have said. So, you know, for example, if you do logging underneath, it would make sure that the log, The log span correlation works correctly.
Okay. Yeah, so basically what I'm proposing is, if you move this… The mapping stuff to kind of manage the context into… whatever is calling this, and then you reconstruct the context before you call it, I think it would be a little more reusable.
**Keith Decker** 14:26 Okay, I think I'm already doing a good portion of that, I'm just abstracting it behind a UUID that the instrumentation would call, so I'll pull that abstraction out and just directly return the context token.
**Aaron Abbott** 14:40 Okay, cool, and Yeah, the only other thing I would… I would point to, and I can leave a comment on the PR, is we have something pretty similar in, one of the Vertex instrumentations, which… which we can… hopefully kind of inspire the design, like, it's actually pretty similar, so I think maybe you looked at it. There's, like, this context manager, and the sort of benefit with that is that you can use it for You know, all four variants of… Synchronous calls, asynchronous calls, and then synchronous streaming, asynchronous streaming.
So, which, which it looks like we're doing here, so… Cool.
**Keith Decker** 15:17 Okay, yeah, yeah, definitely sending a link over on that would…
**Aaron Abbott** 15:20 Be helpful, too.
Great.
Alright, that's all I had.
**Sergey Sergeev** 15:35 And I just wanted to make sure, Dylan, if you have any questions to Keith, just feel free to ping on Slack or hop on a Zoom call if you need some good walkthrough.
Or if you want to bring some ideas.
**Dylan Russell** 15:54 Okay.
**Sergey Sergeev** 15:59 Are you Pacific Time, Eastern Time, or other time zone?
**Dylan Russell** 16:05 I'm Eastern Time.
**Sergey Sergeev** 16:07 Okay.
**Dylan Russell** 16:08 It helps.
**Sergey Sergeev** 16:09 It is mountain time, I believe.
**Keith Decker** 16:11 Yep, Mountain Time.
**Dylan Russell** 16:18 Yeah, I'll take another look and, yeah, add some comments, and reach out if I… Yeah, need help with anything?
Okay.
**Keith Decker** 16:29 Thank you, yes.
**Riccardo Magliocchetti** 16:32 Thank you.
And are related to the code.
I think we need to update also the code owner.
File to delegate, to generate people, right? Because I expected to see… Or maybe not, or maybe it's working. Anyway, I'll take a look.
Okay, this was the last topic.
For today, so… Daniel, do you want to discuss the log stabilization stuff, or we can just… Very quick today.
**Aaron Abbott** 17:23 What did you want to discuss, Ricardo? Just, like, the plan you put together?
**Riccardo Magliocchetti** 17:28 Yeah, like…
**Aaron Abbott** 17:30 Yeah.
**Riccardo Magliocchetti** 17:32 Like, and maybe I can add this, but… Dina noted that…
**Dylan Russell** 17:40 If you want to do the deprecation of four events.
**Riccardo Magliocchetti** 17:43 Like, and the user doesn't have much choice, because, like, it's all in the hands of people writing instrumentation.
And I just checked, and OpenLelementary is using the Events API.
So probably, like, deprec… deprecating that right now.
We'll probably be pretty annoying for… At least OpenLelementary users, I think.
**Aaron Abbott** 18:14 So you mean not deprecating until the thing to use instead is ready?
**Riccardo Magliocchetti** 18:21 Well, I think at least we can ask the OpenLelementary people to… Try to rebase and add, latest SDK as baseline, and try to use the… the log API, so at least we have the… One of the biggest users.
COVID, yeah.
**Aaron Abbott** 18:46 That sounds… yeah, sounds good, as long as we're not gonna break the logs API.
**Dylan Russell** 18:55 Yeah, I think logs should be usable now, in place of events.
Because Ricardo had a change, like… That I think will help with that.
**Riccardo Magliocchetti** 19:13 Yep.
**Aaron Abbott** 19:14 Yeah.
I just, I think we also had some bugs that were, like.
**Dylan Russell** 19:18 considered not…
**Aaron Abbott** 19:20 Not having a log record at all, and instead just have, like.
Parameters to the emit function, so, like.
I haven't been following that super closely, but if we did that after we moved everybody over, that would be pretty awesome.
**Dylan Russell** 19:34 Yeah, we should decide on those things.
conflict.
Yeah.
**Aaron Abbott** 19:46 So I guess my question, Ricardo, like, I don't see that one here, I see the renamed several classes, and .
**Dylan Russell** 19:52 promote log data and send, so I…
**Aaron Abbott** 19:55 I don't know if you had a good look at the spec, and we're able to…
**Dylan Russell** 19:58 You can sit.
**Aaron Abbott** 19:59 on that one.
**Riccardo Magliocchetti** 20:02 the EMIT interface change, I think, is the second point there.
It's easier for you. And… As far as I understand from the spec.
**Dylan Russell** 20:14 Ms.
**Riccardo Magliocchetti** 20:15 Pexard just to…
**Dylan Russell** 20:16 Very good.
**Riccardo Magliocchetti** 20:17 Drop the separate, parameters.
**Dylan Russell** 20:20 Come on.
**Riccardo Magliocchetti** 20:21 And then emit a log record.
And not take a look record as input, but…
**Dylan Russell** 20:29 Oh, they have a lot of choice here.
Okay, cool.
**Aaron Abbott** 20:38 I mean, sometimes we play, like, 4D chess with the spec, and we're like… Dylan, you got some background noise.
**Dylan Russell** 20:47 Oh, sorry.
**Aaron Abbott** 20:48 We're good.
No, I was gonna say, sometimes we… Really try to interpret the spec.
in a way we want, so I don't know if we've done that and squinted at it, like, we just need to weigh the cost-benefit of changing stuff, so… I know you have it here, and it's, like, decide.
That seems maybe, like, the first step is before we move over people to the… off of the events.
**Riccardo Magliocchetti** 21:25 Yep.
**Dylan Russell** 21:25 So, do we have PRs that are out for this stuff, or we just have the bug?
But what is that?
Like…
**Riccardo Magliocchetti** 21:38 You have a draft PR, but… It's missing tests and stuff like that, so… Considering we just have the issue.
**Dylan Russell** 21:57 Yeah, I kinda like… Leaving that interface as it is, but… Yeah, I know the spec obviously says not to, or… Yeah, the spec is different.
Yeah, I like that it just takes a log record.
And the log record has everything.
That the Logs API needs.
Instead of, like… yeah, you… Pass it, like, 9 different arguments.
I think that's what this one is about.
**Aaron Abbott** 22:42 Yep.
**Dylan Russell** 22:43 I haven't.
**Aaron Abbott** 22:44 I'm taking a really good look at the spec, but… Or, like, the spirit is the same, like… It's just a calling convention for the most part, except that the thing that you pass is mutable.
I mean, one thing to definitely consider is, like, I know this is… This has been a big topic in other SIGs regarding logging, but, like, performance, so… We only have this variant, and I have to… every time… every time you log, there's no… way to avoid, like, garbage collection costs, but I think we would be just constructing this thing behind the hood, but in terms of the API, like, we're shutting ourselves out to different options if we do that. Unless we added, like, a separate overload variant to… You know, call it with just the arguments.
**Dylan Russell** 23:53 Right.
That seems like a good compromise, like, just… Yeah, have a few variants of the method.
**Aaron Abbott** 24:06 Yeah.
And I think that would be the first step regardless, because.
**Dylan Russell** 24:29 Yeah, so if we agree on that, then… That means we won't… at least this issue, we won't be breaking people if… if they migrate to logs now.
Although, I guess maybe we would want this ahead of time.
So they're overloaded.
Yeah.
**Aaron Abbott** 25:07 So, I mean, it sounds like somebody needs to get through the spec decide this.
It's important to us, or not.
Does that… like, part of easing… You can take that.
**Riccardo Magliocchetti** 25:32 Yeah, probably, I've taken on… Maybe next week, yeah.
**Aaron Abbott** 25:42 Okay.
**Riccardo Magliocchetti** 25:44 How about, Rost Fingh?
Probably at least, like, to start moving things forward, we can just start merging the… Like, start to imagine that.
**Dylan Russell** 26:04 Yeah.
**Riccardo Magliocchetti** 26:06 So at least we reduce a bit the stuff we have open.
**Dylan Russell** 26:17 Sounds good to me.
Quick question. Are we planning for a release of the Gen AI package?
**Aaron Abbott** 26:58 Yeah, definitely. I have one more, PR out.
And I think it would be in a decent spot.
**Dylan Russell** 27:09 Cool, because I think there's some other PRs that are blocked on that, A release of that.
**Aaron Abbott** 27:18 Billy?
So, so do you need it, like, today, or…
**Dylan Russell** 27:31 I think it can… and this week would be good, I guess.
Something?
**Aaron Abbott** 27:40 Yeah.
Yeah, I reserved the name on PyPy, so…
**lechen** 27:44 Yeah, I reserved the name of my pie, so… good guy.
Has the Util's package ever been released before?
**Dylan Russell** 27:56 No.
**lechen** 27:59 No.
Okay, did we decide that we're gonna be adding this as part of the regular release process, or is this, like, a manual thing?
**Aaron Abbott** 28:13 This is, like, a one-off one, like the other gen…
**lechen** 28:23 Echoing for you guys, but…
**Aaron Abbott** 28:26 Yeah, it was kind of funny, it happened, like, 5 seconds after what I said.
**lechen** 28:34 Heh, got it.
**Riccardo Magliocchetti** 28:52 Okay, any other topic? Comment?
Okay… So, thank you, everyone.
And see you next week.
**Dylan Russell** 29:10 Thank you.
**Hector Hernandez** 29:13 June.
**lechen** 29:13 Thank you, bye.
**Shuwen Pan** 29:14 Bye.
