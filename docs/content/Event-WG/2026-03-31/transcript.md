SIG: Event WG
Date: 2026-03-31
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/5DHEpPnpTY6Cqks1OCUU9nsFue_y8FVM7Sx2fn2_IAVAMTwNVD5lfmT1BGa7huBn.00--8eWZBDzVUO90
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:07 Hello, Robert!
**Pellared** 00:10 Hello, how are you?
**Liudmila Molkova** 00:12 I am good.
**Pellared** 00:13 Right in the buck.
**Liudmila Molkova** 00:15 It was… it was good, but I… I wake up every night at 2PM… oh, sorry, 2AM now, and I feel miserable, but today I woke up at 4, it's progress.
**Pellared** 00:26 usually, I once read some article that the average is that people could accommodate, like, 2 hours per day of the jet lag. That's, like, the average.
**Liudmila Molkova** 00:37 Yeah, I wished, like, since it was a relatively short trip, that I wouldn't need to spend much time accommodating back, but no.
How was your flight back?
**Pellared** 00:51 For me, it was very good.
Like… My colleague was giving a previous flight to Krakow.
And, she always was… and, when they started, the engine was trembling, almost resonating, so they took her from Amsterdam and got back.
And then later, she was, like, flying to Krakow almost at the same time as myself, which was, like, 4 hours later.
**Liudmila Molkova** 01:17 Oh, wow.
**Pellared** 01:17 So I had luck, I had luck to, to, to, to choose the, the latest, the most, the, the flight features, the, you know, the latest.
Yeah, but 6 was beautiful. Yeah.
**Liudmila Molkova** 01:33 Did you manage… he stayed in Amsterdam for a bit, right, and did you manage to see anything cool?
**Pellared** 01:39 Yes, I managed to be this time in Van Gogh Museum, Van Gogh Museum.
Because last time, it was 3 years ago, and tickets were sold out, like, 3 weeks before.
**Liudmila Molkova** 01:51 Huh?
**Pellared** 01:52 two weeks before KubeCon, so this time I just, when my, my presentation was approved, I bought the ticket.
Nice!
What's about you? Have you, have you, have you addressed this thing, I think?
**Liudmila Molkova** 02:06 Not much. I have a friend who lives in Amsterdam, well, in the suburb on there, and I spent Thursday at her place, also we've met on Sunday. So, just it. She walked me through the town, and it was great.
**Pellared** 02:22 Yeah, that's still good.
Are you a museum person, or not at all?
**Liudmila Molkova** 02:29 Not at all.
**Pellared** 02:30 Yeah, so you have not missed anything, because Amsterdam is also famous for the museums. I know that some people are just going, you know, for even one day, or two days, just to see the museums, and other people for marijuana.
**Liudmila Molkova** 02:47 We have it here. It's legal.
**Pellared** 02:50 Is Tras joining? Do you know? I think he said during… is Tras joining this meeting? Do you know where?
**Liudmila Molkova** 03:00 I've seen him, in the previous call, like, 10 minutes, 3 minutes ago, maybe.
**Pellared** 03:05 Is there the ice.
**Liudmila Molkova** 03:06 up.
**Pellared** 03:07 Okay.
**Liudmila Molkova** 03:08 Let's see, let's pink him.
**Pellared** 03:15 How was your Gen AI talk, by the way? Oh, trust me joining. How was your Gen AI talk? Are you happy with it? I was not able to join it, unfortunately.
**Liudmila Molkova** 03:23 It was good. There… there… it was the biggest hall, the keynote hall, but, like, the people, like, was a regular amount of people, but it was so intimidating. They have, like, the backstage thing for the keynote speakers, and they offered me some coffee there. It's… yeah.
We're talking about Cube Contrask. The highlight of it is that food was unexpectedly good. It was amazing. Not typical.
**Trask Stalnaker** 03:53 Alright.
**Liudmila Molkova** 03:53 at all.
**Pellared** 03:57 That's a chat?
**Trask Stalnaker** 03:59 Wow. I mean, the bar was pretty low, but… That's…
**Liudmila Molkova** 04:04 Yeah.
**Pellared** 04:04 But usually, each day.
**Trask Stalnaker** 04:05 It was legit.
**Pellared** 04:06 The maintainers, some usually can boot food.
Co-located event sometimes was, like, you know, average, and then KubeCon main event was the worst. I was sometimes not able to eat it at all, and right now it is a total shift. Like, you have… the co-located event had worse meal than the main event, which was very surprising.
**Trask Stalnaker** 04:28 Yeah, because they have to do that on such a mass scale.
**Liudmila Molkova** 04:33 We were joking that there is a spec somewhere, maybe an RFC, that tells… that gives the specification of a terrible food, and they have one place in the world that's able to actually.
**Trask Stalnaker** 04:44 Execute on that.
**Liudmila Molkova** 04:45 Yeah, but this time they probably, I don't know, they abandoned this pack, it was a breaking change.
**Trask Stalnaker** 04:55 Glad to hear it.
**Pellared** 05:01 Laptop back.
What's what I have to say.
**Trask Stalnaker** 05:09 Robert.
**Pellared** 05:10 Shall we chat?
**Trask Stalnaker** 05:11 more about it.
**Pellared** 05:12 Yes.
Do you want to also add to the agenda something from the previous meeting?
What's that?
**Liudmila Molkova** 05:21 I've pasted the next meeting items.
**Pellared** 05:28 I'm not sure if we should not also double-check the ones that we previously…
**Liudmila Molkova** 05:34 Payment here.
**Pellared** 05:37 Yeah, not sure which one. Yeah, at least this reporting logger name, rich name, I think trust me want to create APR for it.
But probably it's not there yet, I guess, but…
**Trask Stalnaker** 05:48 Yeah.
I've been a little sidetracked by Gen AI.
**Liudmila Molkova** 05:57 Be honest, you wanted to have some quiet time to actually work on things.
**Trask Stalnaker** 06:01 That was nice, too.
Not having… not having 8 a.m. meetings was nice.
**Liudmila Molkova** 06:08 Jealous. I'm jealous.
Okay, so no progress on this one.
We don't need to spend time here.
This one…
**Trask Stalnaker** 06:26 Yeah, probably take my name off of that one for the time being, Robert.
In case it's something that you wanted to… Get done sooner.
**Pellared** 06:41 No rush for me.
**Liudmila Molkova** 06:46 Honey.
I think I should talk about span event deprecation, because it's… Near the thing that I wanted to mention.
**Pellared** 06:58 I think we may add this one to the first bullet, because it's about the same thing.
The review issue is just the issue for the feedback of spawn event, so you may just copy this.
Yeah, as a separate bullet mark, responding with…
**Liudmila Molkova** 07:16 Quay.
Oh, somebody shared feedback!
**Pellared** 07:21 Yep.
**Liudmila Molkova** 07:28 Okay.
**Trask Stalnaker** 07:47 Yeah, thanks for replying to those, Robert.
Because I think it's natural that people are going to… You know, have… Concerns about it being… Break, you know, breaking their workflows, and so… just… What you've said is great, just, like, kind of reaffirming that there are.
**Pellared** 08:21 Don't hesitate.
**Trask Stalnaker** 08:22 still options. It's… yes, it's not necessarily gonna be…
**Pellared** 08:27 I mean, yes.
**Trask Stalnaker** 08:29 Seamless, but… There are… it shouldn't be too much work to… .
**Pellared** 08:38 What's your show.
**Trask Stalnaker** 08:38 We'll have that workflow.
I'd probably focus on the, I mean, the SDK translation, Processors, since that's… the easiest…
**Pellared** 08:56 It's not sure for… oh, yeah, it's also not sure for us.
**Trask Stalnaker** 08:59 Yeah.
And doesn't require the complexity of… we know that that's super… Doable and easy.
Versus the collector stuff.
**Pellared** 09:13 during QubeCon, I was talking with both… with Dan, but I saw that it was also added as an agenda item, so he was mentioning the tile sampling.
Yeah, the last bullet, yeah.
I think someone… so the last comment through… the one about processing was similar to this one. I asked Dan if he could try to capture it in this issue, so that it comes from the user, and not from us, this ask.
But I also talked with Dimitri from the maintainer of Collector, and he said that he saw this blog post, and he's totally on board with it, and he said that it's reasonable that they'll add it to the collector, and he sees… he sees that there will be some challenges, but he… but he said no… not blockers and not concerns from his side. Like, he doesn't… he doesn't… he's not worried about, you know, some kind of… Like, there will be challenges, but it's reasonable to add this into a collector. That's what he said.
**Trask Stalnaker** 10:17 Nice.
**Pellared** 10:18 I even think he was not even concerned about the challenges. Yeah.
**Liudmila Molkova** 10:24 So, and it would cover both the… buffering of logs and attaching them as span events, and also the tail-based sampling then. Because, like, the challenges are the same across these two.
**Pellared** 10:39 For… for just table-based sampling.
They could buffer less, because they just need to buffer only the decision.
If it's sampled or not, so it's easier for them.
So this is easier for them.
So, to be… for being efficient, probably it would be better for the end user to use the sampling on the collector, and swapping the event… yeah, but you use one or the other.
So… If you already had… if you just want log sampling, then you just use this one. If you want, if you would like to change logs to events, then you would do it preferably via SDK, but it would be also done by the collector.
**Liudmila Molkova** 11:30 Yeah. I've had a brief chat with Michaela from Dash Zero, and they also saw the blog post, and they were like, yeah, it makes total sense, and they, support it, and they provided some… I don't know the details, but they provided some technical options, too.
Just convert them.
**Trask Stalnaker** 11:54 Cool.
**Liudmila Molkova** 12:00 Okay, so then… it seems we can move in both directions, the SDK-based things and collector-based things?
But if, if we, if collector folks are not… are saying that it's not a big deal to do this. Maybe we should prioritize collector parts?
It's just easier.
**Pellared** 12:28 I… Bing… Like, I think that for sampling, it should be done the collector for… for the backwards compatibility to… I'm just right now to the stream.
Yeah, it could be both supported by Collector.
That's what my originally proposed, but yeah.
Which… because we wanted the process to work.
to translate events back into span events, right?
For backends, so I think this will be better done in the SDK anyway, so they do not have to buffer anything. Because, In the SDK, you have the context, the current span.
**Trask Stalnaker** 13:22 Yeah.
**Pellared** 13:23 I think he's a…
**Trask Stalnaker** 13:24 That one just seems like such an easy, no… like, simple no-brainer that…
**Pellared** 13:31 Yes, so this I will do in the SDK, and on the collector, just implement the sampling for… for logs.
**Liudmila Molkova** 13:43 Okay.
So then… The mitigation, this is the same one as we talked so far, just opting into the… So nothing for now.
But maybe you should create this processor that converts all of the logs to span events.
**Pellared** 14:12 orange as events.
**Liudmila Molkova** 14:14 All the events to spend events. Yeah.
**Pellared** 14:17 Yeah, because they are named, I think.
And for tail sampling, I will do it in the collector.
Even though… I think even now, for today is something people use the collector.
Even for spans.
**Liudmila Molkova** 14:55 Yeah, but then if you convert in the SDK, then you don't need to change anything in the collector at all.
**Pellared** 15:01 I mean something different. People use… Events, but they want to tail sample for the events, not have the span events.
So they want to retain the logic of sampling.
For events in the same way as they do it for tracing.
And this one was already asking the issue. This was one of the first feedbacks, that they want… they like the sampling strategy, and they would like to have them for the rock-based events as well.
**Liudmila Molkova** 15:31 Yeah.
It's cool, I feel it's already taken out of span of deprecation, though. Like, yeah, it can just happen without us.
Supporting it in any way.
**Trask Stalnaker** 15:46 Yeah, I mean, it's related in that, like, if you don't want anything to break, then you use the span processor, and you still use span events.
**Pellared** 15:56 if…
**Trask Stalnaker** 15:57 Do you want to opt… if you do like the new modeling of log-based events?
Then you would need this, and you're using tail sampling.
It's an… it's a feature, it's sort of like an equivalent feature.
**Liudmila Molkova** 16:21 Okay.
**Trask Stalnaker** 16:33 So, while I don't think it's str… like, it's not required from a back compat, perspective.
It's a… Nice to have from making the new stuff as good as the old stuff.
**Liudmila Molkova** 17:25 Okay, yeah, makes sense.
So, do we need to, do something in the… What do we need to do? So, for this pack, we probably want to document this… This is a special processor that we recommend every… Contrip to provide?
**Trask Stalnaker** 17:53 Yeah, we can use the, I think declarative config supports named processors?
Now, so we could establish a name for it.
And the… and a behavior… Where it lives.
I think… could be… Language.
Dependent.
**Liudmila Molkova** 18:33 Right.
So we would not be prescriptive. Like, it can be contrary, it doesn't have to be… the default feature in the SDK.
Mostly because… Well, the only good reason it's not in the query is because some of the new SDKs want me to implement it.
At all, but…
**Pellared** 19:04 also, also in future, in my .be nitus.
Yeah. 10 years.
**Liudmila Molkova** 19:08 Yeah, right, that's a good point.
**Trask Stalnaker** 19:14 We have precedence for deprecating.
Things.
**Pellared** 19:21 We do.
**Trask Stalnaker** 19:27 But yeah, I'm fine with leaving that.
**Pellared** 19:30 I'm also… for me, it can be SDK or Contributes.
Whatever.
**Trask Stalnaker** 19:39 Yeah, if we… I think we'll get, if there's problems with it, we'll get user pushback, and that'll help us.
**Liudmila Molkova** 19:49 Yeah, and it's easier to move from Contrib to the central repo than otherwise.
**Pellared** 19:55 You can assign me to this, I can work on it.
So we have… I may… yeah, I may need to have some help with the declarative conflict part, but I can also… I will try to do it myself, or I can also ask anyone for help if needed.
**Liudmila Molkova** 20:14 Yeah, thank you.
And for the collector, I would imagine…
**Pellared** 20:19 The idea to ask is that I do, at the same time, both PRs and the declarative configs come in the specification.
Sorry for calling you the name. Okay.
**Liudmila Molkova** 20:32 Yeah, I think Jack just sent the pull requests to… To add it to the country pin spec, that you should send both.
**Pellared** 20:42 Okay.
And prototypes, of course.
**Liudmila Molkova** 20:48 Yeah.
And there are a bunch of issues, I think, for the mapping, to document mapping, that we can just close with this.
And for the collector, I would imagine we can create a new shoe.
But do we want to expedite it?
I don't… I wouldn't…
**Pellared** 21:15 I want to wait… I want to wait at least one week, or something like that, because I hope that, Dan mentioned some customer, that we'll have some, you know, more feedback that this is needed.
Just to put more details. But, yeah.
**Liudmila Molkova** 21:44 Okay.
I have a plan?
What?
**Pellared** 22:00 Before going to this one, I remember that we were also discussing the… recording errors document last time, and I've just lost track what are the next steps.
if I have not missed something, or… I'm not sure if it's this one, or… I think it was… In the last meeting?
No, it's just this one? Yeah.
sits on Spyro's locked, it looks like.
**Liudmila Molkova** 22:33 Unrecorded exception.
**Pellared** 22:35 I do not… I do not remember what was missing, so that we can stabilize.
**Liudmila Molkova** 22:44 So let's see what's missing… Yeah…
**Pellared** 22:53 I think we are so close here that I do not want to, you know…
**Liudmila Molkova** 23:02 So… This… oh, okay, so what we talked about?
that… Dabilizing this document.
It's based on specific events.
like, HTTP request… Exception.
It's the generalization of the principles, but the actual events, or… in development.
So I think what we talked about, that it would be cool to stabilize individual exceptions, exception events, like HTTP, database, RPC, when we are moving to RPC stability. And then, once we've done it.
That would be good enough to stabilize this document.
**Pellared** 23:50 Okay, so we first want to have some experience and precedence in, for instance, RPC. Okay.
**Liudmila Molkova** 23:57 like your HTCP database, which are already stable, and I think we are adding those events to instrumentations that will become stable, right, Trask, for the Java?
**Trask Stalnaker** 24:07 Yeah.
Okay.
**Liudmila Molkova** 24:10 Kinda need to stabilize them anyway.
**Trask Stalnaker** 24:18 Yeah, I'll, I'll, I'll… come back to that. I'll start pushing for stabilizing those once, we get a little closer on the Java side.
**Pellared** 24:31 But I think these are, like, the semantic conventions… Stop.
maybe we are able to stabilize the APA parts of setting errors on logs, trust?
the set exception that you added something to go to the API, I think some languages already implemented it. I remember that we had this precedence that we were stabilizing the API, even though the SDK behavior was still, like, not stable.
**Liudmila Molkova** 25:04 to it, we stabilize This pack, right?
**Pellared** 25:07 Established already in spec, or maybe… yeah, maybe, maybe you're right.
**Trask Stalnaker** 25:11 Yeah, we do.
**Pellared** 25:12 It's cool.
Awesome. Okay. What's the further?
If we stabilize.
**Liudmila Molkova** 25:34 Yeah.
**Pellared** 25:35 Okay.
Being able to… Alright.
Thank you.
**Liudmila Molkova** 26:07 And one more thing, I think I created it…
**Pellared** 26:10 Do you think, given this is stable.
We still need to wait for deprecating the span events.
I guess it would be nice to have this processor.
that converts the… Yeah.
I'm not sure what was the reason to stabilize the recording exception document. I think it was… Me who requested it?
But… I'm not sure if it was not too big.
**Liudmila Molkova** 26:45 Because this is the replacement rate.
We need a stable replacement to… for the stable feature.
**Pellared** 26:52 I see, so it's not only the API, but also behavior that the users can rely on.
Okay.
Okay, sorry for drifting.
**Liudmila Molkova** 27:04 That's kind of.
**Pellared** 27:05 Just wanted to remind myself.
**Liudmila Molkova** 27:11 Yeah, and… yeah.
Noswad is another one, but a small thing.
Okay.
Oops.
Perfect here.
Oh, Cricket, there are some exceptions.
**Pellared** 27:41 I added a comment after this spec meeting, you can double check.
**Liudmila Molkova** 28:03 Okay, so there are… There are chained exceptions, there are aggregate exceptions, there are different… Properties and exception.
**Pellared** 28:12 Yep.
**Liudmila Molkova** 28:13 -Oh.
the tricky part, like, I really don't want to change the existing attributes.
Yeah. Can we just support new things?
**Pellared** 28:29 So that was my proposal. My proposal was to keep the existing ones, we just… Define, like, the outermost, or whatever you call it.
And add this additional attribute that gives you the full structure.
**Trask Stalnaker** 28:48 So, I have a question in terms of, the priority or importance of this, Robert. Can you explain, again, sort of how this came up in Go related to the span event change.
Or how… how… why it's… how it's related?
**Pellared** 29:12 So we added this set.
Set error or set exception?
for the log record, and the thing is that the outermost error very often contains no data in Go, because in Go, we kind of have something, like, we usually wrap the errors, giving more context, just using a string, almost. It's, like, a very basic system. So, the thing which… the type… It's mainly about the type.
The message usually contains all the data, because it's a very long string, like, similar to the, you know, outermost exception, but the type is usually, like.
You know, like… Some generic exception, which is used to wrap all the exceptions.
**Liudmila Molkova** 29:58 Classic Java, but in Go.
**Pellared** 30:02 Like, in Java, you usually create your own exception when you're wrapping, you just, you know, that accepts the inner exception, so say it's worse, because you have no type in reality.
**Trask Stalnaker** 30:12 A lot of people just do rapid and runtime exception, so they don't have to Do type check, Yeah.
But, so… I did.
Yeah, so I still don't quite follow how… why wasn't this a problem with recording exceptions and span events.
**Pellared** 30:42 It sh- it would be as well.
Probably nobody cares at this time.
**Trask Stalnaker** 30:48 Okay.
Okay, yeah, I just wanted to… make sure that I'm clear, like, is this… somehow related, did we make this problem worse with band event deprecation?
**Pellared** 31:03 No touches.
**Trask Stalnaker** 31:04 So this problem has existed for years.
**Pellared** 31:07 Yes.
**Trask Stalnaker** 31:09 People were.
**Pellared** 31:10 Just looking at the message, that's how, yeah, they just wanted to have this title a little better.
And Steven… And…
**Trask Stalnaker** 31:17 So we… something we do in Java instrumentation, we actually have in our Instrumenter API, we actually do unwrap automatically a couple of those common Junk exceptions to get it down to the… better type.
So, right, it's not done in the SDK itself.
Because the SDK is more pure.
But in the instrumentation layer.
You could do some unwrapping. Users could do some unwrapping.
You could provide a util, even if there's kind of a common mechanism.
**Pellared** 32:04 Yeah, we thought about doing this SDK in a common way.
**Liudmila Molkova** 32:10 Should we have it in the semantic conventions? Should we recommend unwrapping by default.
Think so.
**Pellared** 32:27 So, there was a PR, which did it for… Goal?
Because one of, also, some other person requested it, but the same person that also said, does it make sense to unwrap, you know, up to the end?
it just makes sense, probably, to unwrap what tasks that some common, you know, common, like, aggravating exceptions and stuff like that. On the other side, if you have agrating exception, then you do not have one error. It's just… It's just when you train the exceptions. But when you have an aggregate, then there's no good way to handle it.
**Liudmila Molkova** 33:05 Yeah, and these are two different problems, right? So, it makes no sense to capture this junk exception, I like the name.
And you might not even have aggregated exception, or this problem at all of multiple things.
**Pellared** 33:21 Yep.
**Trask Stalnaker** 33:24 Yeah, here, this is… just… What we have in… Java, those are the junk ones that we… Strip off.
**Pellared** 33:36 So we thought about something similar for Go. I think there's one or two types in Go, which are in runtime.
I don't…
**Trask Stalnaker** 33:44 I mean, I like the… I like it as May guidance, as kind of like a hint that… the… Yeah, I mean, I guess you don't… you really don't lose anything, do you? Because you still have the stack trace all the way to the top.
**Pellared** 34:09 Like, for us, we didn't want to extract everything, it was just the capturing the name.
So we're still at the top level, Message?
or stack place, or whatever. It was just about the semant… about how… the semantics of the exception type.
**Trask Stalnaker** 34:31 Yeah.
**Liudmila Molkova** 34:34 It's also maybe… I'm just thinking about it out loud, that… There is exception type, and there is error type.
And exception type may be literal, but error type may be the… the root cause, but also… I think, for example, like, there are cases where definitely not, like, this execution exception, or I think there is a similar reactor exception, where you know for sure it's rupt.
**Trask Stalnaker** 35:06 Yeah, yeah, we have a couple of, This is a pattern, and we have a… we… individual instrumenters can override this list, basically.
**Liudmila Molkova** 35:18 Yeah.
**Trask Stalnaker** 35:18 It's behavior.
**Liudmila Molkova** 35:21 Isn't it actually the similar thing with the stacked trace customizer?
That you want to… Maybe even do this in the application, but not for the… Individual attribute, but for the Whole representation of exception.
**Trask Stalnaker** 35:42 Yeah, the customizer is… for… Mmm… Basically, yeah, I mean, trying to just, if you want to capture a small amount, capture, you know, the most relevant amount.
I'm not sure if it's kind… if it's… It could be used, of course, for this, but… It, I don't think you can customize the type.
So the exception.type, which is sort of… I think, Robert, what was motivating Your users the most was getting the correct Except error type.
Exception type.
Although, actually, maybe… I think you can with that exception customizer. You can change the type. Yeah, I think you can.
**Liudmila Molkova** 36:49 You can?
**Trask Stalnaker** 36:50 I think so.
**Liudmila Molkova** 36:58 Okay, but it sounds like… First, we probably can.
Polish the semantic conventions and recommend the unwrapping.
And then, assuming… would… It might be that we don't need to… Add support for the chain for this issue?
But then, the chain where the list of aggregated exceptions can come, as extra… Attribute, or attributes, like, exception.
chain or exception.
Something.
**Trask Stalnaker** 37:42 Structured.
**Liudmila Molkova** 37:43 structures.
**Trask Stalnaker** 37:44 Except…
**Liudmila Molkova** 37:45 Just for the extra properties, maybe.
**Trask Stalnaker** 37:51 I mean, how much does it… Blend into the fully structured exception question.
Right, like, that came up early.
Where some people wanted to capture it as, like, the method names, and the line numbers, and the class, the type names, and… The whole thing as structured.
**Liudmila Molkova** 38:20 I think it's great that exception message and type are not structured, right? They are indexable, they are… Sometimes aggregatable.
The stack trace is more interesting.
But, like, maybe if we postpone this question, so the…
**Trask Stalnaker** 38:43 Oh, I see what you're saying.
So you would… you would structure the chain But then each piece of that has… still has its stack trace as just text.
**Liudmila Molkova** 38:59 Hmm, maybe. So, like… What if we've done that, so there is exception, type… Message, and let's say stack trace, they stay the same.
For now.
Then we introduce, let's say, exception.coes, or maybe causes.
And this is the structured thing.
And… the structured thing is… like… This is the least of… Causes, and each cause is… This time, it's structured, like, and it has individual message, like… stack trace.
And the stack traces, probably… For this one.
Ish.
Always tough.
I don't know.
Whatever, frames. We're numbers.
And then, if it's an aggregate.
then maybe it's not exception causes, but exception… I don't think they're called Call the… call this, but… Dunno.
**Trask Stalnaker** 40:25 I'm not sure what an aggregate is, I think, I think, Robert, you really meant… Causation chain.
**Pellared** 40:33 not really trained.
So, one is training, joining, and aggregate when they are really parallel. Like, for instance, you've got .NET and you have async methods, and then you aggregate all the responses, and some of them failed, they are not one which is more important than others, they are, like, you know, parallel.
Yeah. Okay. Parallels.
or concurrent.
**Trask Stalnaker** 40:56 Yeah, in Java, that's called suppressed exceptions. You can attach these suppressed main exception.
**Liudmila Molkova** 41:11 And nobody knows how to… how they are different from causes, right? But… There is… at least there are two different sides.
**Trask Stalnaker** 41:20 Yeah, it's exactly what Robert said, though. It's a one-to-many versus a chain.
**Liudmila Molkova** 41:27 Ruh, yeah.
**Trask Stalnaker** 41:28 So, yeah.
**Liudmila Molkova** 41:28 If you have many.
**Trask Stalnaker** 41:30 Yeah.
But I agree, it's like a… Generally, just ignore all the suppressed ones.
**Liudmila Molkova** 41:41 Yeah, and if we do this, we need to do, some research on different languages, so this is the typical stuff people do in .NET. There is this thing in their exceptions, and there is no, like, assumption that it's the causation, or it's suppressed, or something, it's just a compounder.
**Pellared** 42:02 Yep.
A screen.
**Trask Stalnaker** 42:06 Suppressed is not a good word.
**Pellared** 42:08 Nope.
**Liudmila Molkova** 42:13 It doesn't sound like we absolutely have to solve this problem. Can we not solve it right now?
**Trask Stalnaker** 42:26 Depends on how motivated Robert is.
**Liudmila Molkova** 42:28 Yeah.
**Trask Stalnaker** 42:29 But, given that it's a long-term It's been there forever. That's all I wanted to confirm, was that we didn't make the problem worse with Spanish.
**Pellared** 42:41 You're like.
**Trask Stalnaker** 42:41 deprecation.
**Pellared** 42:42 I already have a, like, it's already better, because I know that's probably Probably direction going to a structured value is more preferable.
So, it's still a little bit step further, you know.
**Liudmila Molkova** 43:06 I'd suggest not to then think about it.
**Trask Stalnaker** 43:08 I do like the idea of guidance, though, or some kind of guidance.
And that might.
**Pellared** 43:14 I think we can do something for the Chinese ones, at least. The one which are in Java. I think we could try addressing these ones, at least. Maybe some asterisk?
for… for the exception type, and maybe error type, attributes in some cons.
Do you think Ludum trust that this is reasonable, just to address at least this one concern?
**Trask Stalnaker** 43:41 I liked the idea of, just instrumentation may… unwrap.
Exception, junk exceptions.
Something like that.
Because that might make, like, the Go people feel more comfortable with, oh, okay, like, it's okay to unwrap them.
**Pellared** 44:12 Sure.
**Trask Stalnaker** 44:13 the junk ones.
**Pellared** 44:13 It will be easier for our users to do it on the SDK level, because people will also create this junk even by themselves. Even if they have some domain exceptions, then we'll let you wrap it with this junk, and they're really interested with this domain stuff.
That's why our preference is just to have systematic conventions.
And then we already have in the specification that the SDK, you know.
should help following the semantic conventions.
And I think it's implementation-specific how much you do on the instrumentation library, how much you do on the SDK.
**Trask Stalnaker** 44:53 Yeah, I mean, I think that's totally fine to do it in the SDK, because the SDK is already implementing an implementer of the semantic conventions.
In this case.
So, by making it allowable for… in semantic conventions, that should give the SDK leeway.
**Pellared** 45:18 Thanks, Samuel.
Or is it against?
**Liudmila Molkova** 45:26 Something like that.
Look at this trusk.
I haven't seen it.
**Trask Stalnaker** 45:41 Sandbox Semantic Conventions…
**Liudmila Molkova** 45:48 Yeah.
I'm… I'm sorry, it's unrelated, but I'm scared about the amount of issues, like, all the top issues were…
**Trask Stalnaker** 45:59 Gen AI.
**Liudmila Molkova** 46:23 Okay.
Are we done?
**Trask Stalnaker** 46:33 Yeah.
Good topics.
**Liudmila Molkova** 46:37 Yeah.
**Trask Stalnaker** 46:41 See ya.
**Liudmila Molkova** 46:41 Cool. It was great to see you.
**Pellared** 46:44 See you next time. Thank you. Bye.
**Trask Stalnaker** 46:47 I…
