SIG: Event WG
Date: 2026-04-28
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Pellared** 00:51 Hello?
**Liudmila Molkova** 01:02 Oh, sorry, I'm completely muted.
But I was talking to you, I promise.
**Pellared** 01:07 Oh, okay. I'm not able to respond to that, sorry, but I guess it was all in kind words, so yeah. Hello?
**Liudmila Molkova** 01:15 You couldn't read my mind, right?
**Pellared** 01:19 How are you?
**Liudmila Molkova** 01:22 That was the first one?
I was in Barcelona, yeah, Barcelona is awesome. People should not leave, like… like… well, I mean, it's nice here now, but not in winter.
I wish we.
**Pellared** 01:34 return it.
**Liudmila Molkova** 01:35 to Barcelona during wintertime.
**Pellared** 01:37 Yeah, but it won't be there in the summer.
**Liudmila Molkova** 01:41 Yeah, I would prefer this summer, for sure.
**Pellared** 01:44 Was your first time in Barcelona, or not really?
**Liudmila Molkova** 01:46 No, I've been there, like.
For a few days before, but it was 20 or something years ago. It's been… it's been a while.
Have you been?
**Pellared** 01:57 Yeah, I have been when I was, like, 6 or 7 years old, but I still remember the Goldie Park. I think the, the Goldie Park. I remember that the cathedral, was still being, you know, it was still, It was still not that big as now.
the Sagrada Familia. So yeah, I do remember, and I hope that I'll be there in some time, but yeah, no rush.
Maybe…
**Liudmila Molkova** 02:21 CubeCon next year, you know?
**Pellared** 02:22 Exactly, yeah, that's my goal.
Maybe still for one or two days more.
**Liudmila Molkova** 02:27 Yeah.
I stopped by Sagrada de Familia, and I could not, like, I could not be there. There are so many people.
And I thought, oh, maybe I should go inside, but then I saw the amount of people. Oh, my phone stopped working there, this is the amount of people, and it was just… I don't know, Thursday evening.
**Pellared** 02:46 Yeah.
This one is merged, this pack.
This one, is on my, to-do.
Yeah.
**Liudmila Molkova** 03:05 Oh, this one is mine! Oh my god.
**Pellared** 03:07 Yeah.
**Liudmila Molkova** 03:07 Nice to see you.
**Pellared** 03:08 Saturday.
There are the configuration as well.
**Liudmila Molkova** 03:15 Configuration as well, this one?
**Pellared** 03:17 Yeah.
This one is merged as well.
**Liudmila Molkova** 03:20 Nice.
Event to span, event to bridge. Nice.
I'm so merged, and this is merged.
Are we done, Ms. Logs?
**Pellared** 03:42 with logs? That's a good question, because we are right now discussing… and no, because… For the deprecation?
of, because I already, I think, received two PRs on the Do Not Merge on the specification for deprecating records, Record Events API, but I think the consensus was that we want to have something in the database semantic conventions.
If I record correctly, For logging the errors.
**Liudmila Molkova** 04:18 Oh.
Okay, so… So, okay, let's first… I think it was…
**Pellared** 04:27 Notice somewhere here.
**Liudmila Molkova** 04:29 Yeah, we'll find it. So, for this one, We are…
**Pellared** 04:36 This one, I need to create prototypes, and I don't.
**Liudmila Molkova** 04:38 Yes.
**Pellared** 04:38 It's a blocker anyway.
Ultravity's here.
Hey. Yo.
**Liudmila Molkova** 04:43 Should we… should we track it in the logs? Because, it's cool, it's awesome, is it…
**Pellared** 04:50 Or you don't need to track it in the logs.
I don't think so.
It's related.
**Liudmila Molkova** 05:01 Cool, yeah, and I think we already…
**Pellared** 05:04 We are just discussing here because I think it's also Trust… it's also important for UW and Trust because of the semantic conventions. So, yeah.
**Liudmila Molkova** 05:15 Oh, this helps us, stabilize this document.
**Pellared** 05:21 Yes, make it easier to.
**Liudmila Molkova** 05:22 stabilization.
**Pellared** 05:23 Yes.
**Trask Stalnaker** 05:25 It's just a…
**Pellared** 05:27 Convenience.
**Trask Stalnaker** 05:27 Sugar, yeah, yeah.
**Pellared** 05:29 Yep.
It's just a nice-to-have. It's not a blocker.
**Liudmila Molkova** 05:37 So we can just go ahead and stabilize the document, the only caveat is this section.
Which… We should talk about… But essentially, I'm, I'm going to… just say then it's not in the scope for this SIG, even though it's awesome, and I'm happy to support it from the.
**Pellared** 05:58 Yes, we can…
**Liudmila Molkova** 05:59 For the general topic.
**Pellared** 06:00 remove… we can remove it from the meeting cycle, or work on it concurrently.
Trasco, do you remember what was preventing us for deprecating the record exception API? It was some semantic conventions for database logs?
reporting errors.
I always forget about it.
Maybe it's in…
**Trask Stalnaker** 06:24 Oh my god.
**Pellared** 06:24 We are… maybe it was… can you find in semantic conventions, or my open pull requests?
I think I may have… not semantic specification, sorry.
Last one.
**Liudmila Molkova** 06:52 this one.
**Pellared** 06:56 So it's got more approvals.
**Liudmila Molkova** 07:00 Nice.
Or a direct… Oh, we had the opposite, right?
**Pellared** 07:19 Yes, we had the opposite, and I remember, and I remember we had a discussion that We should not, you know, increase the support for this method because we want people not using it.
**Liudmila Molkova** 07:33 Yeah.
Okay, this… I can hit the approval, I didn't, just because there is do not merge.
**Trask Stalnaker** 07:41 Yeah, yeah, I was scared off by that also.
**Pellared** 07:44 So, it's blocked by stabilized recording exception blocks, this one.
**Liudmila Molkova** 07:50 Maybe.
**Pellared** 07:51 There was more information.
**Liudmila Molkova** 07:52 with all ages. Right.
Okay, so we wanted to stabilize a log exception.
Document. And log exception document is just the generalization of individual events, so we wanted to stabilize individual events.
First, and then use it as the… Good.
Justification for… The general doc.
And this would also unblock Java and other country instrumentation repos.
We're stabilizing corresponding instrumentation libraries.
Well, they can't stabilize without it, but they better switch to log-based events from span events that they made today.
**Pellared** 08:41 Let's maybe add this issue to the agenda with me, what do you think?
**Liudmila Molkova** 08:44 Yeah.
**Pellared** 08:45 I think this is the most important one right now.
**Liudmila Molkova** 09:13 Okay, what stops us from stabilizing HTTP and database exception events?
**Trask Stalnaker** 09:20 prototypes.
**Liudmila Molkova** 09:22 yeah.
This is Java instrumentation, and it seems you do have a prototype in Java?
**Trask Stalnaker** 09:30 Yeah.
**Liudmila Molkova** 09:32 Okay.
And… we don't have any others.
So this… Group can offer… Go prototype. Robert, would you be… Interested?
**Pellared** 10:04 The thing is that we do not have a consensus.
If we need additional events, if everything is already in the span, in the span, and we have normal information, because it's not… these are not exceptions, we do not have struct rays.
So, it will not provide any additional value on top of what we have already in the span, which is an error and, you know.
stole.
We can make a prototype.
But we do not have any value in it for us.
**Trask Stalnaker** 10:39 So you don't have a span event today?
**Pellared** 10:42 Nope.
I can double-check. Maybe you have for gRPC?
I'm not sure if JRPC didn't have some… some spots.
**Trask Stalnaker** 10:58 Oh, gRPC had a weird span event, but that's not what I meant. I meant, like…
**Pellared** 11:03 Yeah, this is not a…
**Trask Stalnaker** 11:04 Exception, yeah.
**Pellared** 11:05 Yes. Okay. This is something totally different, exactly.
**Liudmila Molkova** 11:11 Okay.
I remember we've got this feedback… so we considered it, right, that we… Put spend ending exception information on spend itself.
And we didn't, because this breaks the cross language… sorry, the consistency, that sometimes exception appears on spans, yeah, sometimes not. So if Go reports some of the exceptions as logs.
It should probably report all of them unlocks.
Thank God, yeah.
**Pellared** 11:45 Yeah, but we do not report any right now, I think.
**Trask Stalnaker** 11:49 They're not… they're not stamping exception.attributes onto the span.
Is that true, Robert?
**Pellared** 11:59 Would you repeat?
**Trask Stalnaker** 12:00 Are you stamping anyexception.
attributes onto the spans.
**Pellared** 12:08 Mmm… no, if I remember correctly, then no. I will double-check.
Should we go country.
So let's…
**Liudmila Molkova** 12:19 So, I, in theory, can do Python, but it's essentially the cloud will do the Python, and I will just present it at the Python sig, and I will have no ability to push it forward and make it land anytime soon.
**Trask Stalnaker** 12:35 prototypes.
Do they need to lay on the… don't think they necessarily have to land. They do need a… Kind of acceptance from the maintainers, though.
Like, some indication that they would.
Land.
**Liudmila Molkova** 13:00 Okay, not this week.
We'll try to make this next week.
**Trask Stalnaker** 13:06 Not this… nothing for you this week other than Python re… GenAI Python repo.
**Liudmila Molkova** 13:12 Hope so, yeah.
**Trask Stalnaker** 13:15 Before I kept asking me to laugh.
Keep asking… Oh, sorry, go ahead.
**Pellared** 13:19 We just set the span status, span description, and error type, nothing more.
**Trask Stalnaker** 13:27 Say those again, Robert.
**Pellared** 13:30 So we only set this when there's an error in Go, we just set the span status, spend this… fund description? It was? Description?
**Trask Stalnaker** 13:40 Status description.
**Pellared** 13:41 description, and then only the error type attribute. Non-exception.
That's true.
No!
We do report the events in the bridges.
There are bridges, login bridges, and then we are actually reporting it.
I… yeah.
As I said.
**Trask Stalnaker** 14:13 relevant?
**Pellared** 14:14 Not a span event, just as an, you know, as an event according to the semantic conventions.
**Trask Stalnaker** 14:21 Okay.
**Pellared** 14:22 So, exception type, exception message, I think, attributes, I do not remember right now.
So our bridges are doing it. Not instrumentations, but our log bridges.
I feel we… Implemented in all of our, log bridges.
**Liudmila Molkova** 14:41 So you can implement, essentially, this guidance, this part of the guidance that's generic, that's not.
**Pellared** 14:48 Yes, and we didn't think we're just… Yeah.
**Liudmila Molkova** 14:52 Would you be interested in prototyping this?
**Pellared** 14:56 Like, it's already implemented, so I can just put… I can just share the PRs here. Let me write it quickly.
**Liudmila Molkova** 15:03 Oh, it's log event. Oh, right, the Slug events, yeah.
**Pellared** 15:07 Yeah.
**Liudmila Molkova** 15:08 Nice.
**Pellared** 15:10 Let's refine it quickly…
**Liudmila Molkova** 15:13 Oh, so the part that's not applicable is the picking severity, already given a severity, But… .
**Pellared** 15:58 I'm putting, in the nose.
**Liudmila Molkova** 16:02 Pa…
**Pellared** 16:03 I'm logged in.
Gorgeous.
Pure &.
**Liudmila Molkova** 16:14 Alright, fault.
Essentially, then, it applies to every language.
Because all of them… Do this today.
**Trask Stalnaker** 16:30 Yeah, I think the… I think that Java… Oh, well… So we don't put event name.
in the logging… like, we don't make up an event name. If somebody supplies the hotel event name.
Then we… Yeah.
**Pellared** 16:55 Let me check it quickly, because maybe…
**Liudmila Molkova** 16:58 So, if we, were to… So this document is already stable, except for that part.
And what's not stable is supplying the exception. And this… This, this line.
So, we… it's a good coverage to have for this specific line.
**Pellared** 17:28 Yeah, so yeah, you are covering everything except the event name, yep.
Yes, you're right, Uzumiu. Like, our bridges are, I think, handling everything but the event name.
**Liudmila Molkova** 17:40 Right, because this is what this document was about before.
No event name.
**Trask Stalnaker** 17:46 Should… logging bridges, Add an event name… on exceptions, I would… Think no.
**Pellared** 17:59 Yeah, we also agreed that no, because we are… do not know if it follows any semantics. That was our agreement, so, before.
That also, I think it was also in line… I think it was also covered by your PR when you added the set error on the API in the SDK, if I remember correctly, but maybe I'm wrong.
**Liudmila Molkova** 18:20 Yeah. And we even say that this document does not apply to bridges.
**Trask Stalnaker** 18:24 Okay.
Makes sense.
Because it's very specific, yeah.
Bridging is just… there's no semantic conventions, really, in bridging. I mean, the… a little bit, I guess.
**Pellared** 18:42 Yes.
**Liudmila Molkova** 18:46 Cool. So then, the story here. We… The goal is not applicable. We are not going to do anything. We have prototype in Java. Eventually, I will spend some cycles doing the prototype in Python.
What are… are there any other languages that we can even target?
And it's probably a question of what are… who are the people who want to help us? Maybe CGO would be interested in prototyping something for… for Rust?
**Trask Stalnaker** 19:26 Yeah, that's a good… just because he's generally seems interested in logs.
**Pellared** 19:32 The only problem is I'm not sure… not sure… how many, or if there are really instrumentation libraries in Rust.
**Trask Stalnaker** 19:43 There must be.
**Pellared** 19:43 I think he's mostly the SDK and the API.
**Liudmila Molkova** 19:51 Probably never been here, but there is the repo.
**Trask Stalnaker** 19:55 Maybe that's the all-through Tokyo tracing.
**Pellared** 19:58 Instrumentation, there are two?
There are two instrumentations only, some tower and some optics web.
I remember my colleague was saying that there is not even an HTTP client instrumentation.
Open to the mystery.
That's the middleware. Okay.
There is something.
**Liudmila Molkova** 20:33 Our HTTP.
**Pellared** 20:36 It was there.
**Liudmila Molkova** 20:38 Okay, so, but since you would know.
Yes, indeed. We can ping him. Robert, do you want to ping him? I can ping him as well.
**Pellared** 20:48 You can leave them your pink, Kim.
I think we can also ping him even in the channel. He's monitoring the channel.
Lock spec.
**Liudmila Molkova** 20:58 Huh.
**Pellared** 21:02 Because I think he cannot join these meetings because of some conflict.
**Liudmila Molkova** 21:07 Yeah, and I will also just reach out to PyType… I will go to the Python Sig meeting this Thursday, and maybe somebody else will be interested in prototyping this instead of me.
Cool.
Can we do anything before prototypes? Probably not. We all agree? It's just the matter of checking the boxes on the prototypes.
**Trask Stalnaker** 21:39 Yeah, I felt pretty good about where it landed.
**Liudmila Molkova** 21:47 Whoa.
Anything else we can make progress for?
maybe just a few minutes. I think we've… Done.
Maybe not.
**Trask Stalnaker** 22:37 We've been talking about events for a long time.
**Liudmila Molkova** 22:45 I'm not too sure it's applicable. I don't know what is it about.
Okay, it's pretty, probably mostly done.
Oh, we've done this, right?
I think, Robert, you documented it.
**Pellared** 23:09 Yes, but I'm not sure, we have not done the span event to lock event conversion.
But we also agreed that we do not want to do it.
**Liudmila Molkova** 23:18 Right, so imagine that.
**Pellared** 23:19 She was about both words.
And we agreed that we only want to convert from For backwards compatibility for the backends.
**Liudmila Molkova** 23:30 Right.
Can you dig up the PR where we did the… This one? Sorry.
this one.
**Pellared** 23:41 This one is in the meeting notes, from the previous meeting.
**Liudmila Molkova** 23:45 Alright, yeah.
**Pellared** 23:47 I'm rich.
**Liudmila Molkova** 23:48 Not really meh.
**Pellared** 23:50 Oh, it's the second bullet point, yeah.
**Liudmila Molkova** 23:52 Yeah.
I knew that.
What was our justification for not documenting them? I'm sorry, I'm blanking.
**Pellared** 24:26 Because we want to have it deprecated, so we really do not want people to, you know, use old APIs to use new functionality.
Which will still miss information, it will, you know… it does not have severities and stuff like that.
So we prefer not… not doing it until there's, you know, a mass of people who really want it.
**Trask Stalnaker** 24:50 No, it's not needed.
compatibility.
**Pellared** 24:57 Event name is there, but yeah, maybe just…
**Liudmila Molkova** 25:01 Alright, Savannah, of course, yeah.
**Pellared** 25:08 There's no custom fields like severity.
and other fields.
Yeah.
**Liudmila Molkova** 25:37 Amazing progress, we've closed one item.
**Trask Stalnaker** 25:41 Yeah.
**Liudmila Molkova** 25:42 Keep you around.
Cool. Then, Brit is here!
**Pellared** 25:50 Great to see you. Have a nice day.
**Trask Stalnaker** 25:52 Bye.
**Liudmila Molkova** 25:52 Me too.
