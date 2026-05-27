SIG: Event WG
Date: 2026-05-26
Duration: 19 minutes
Zoom Recording URL: https://zoom.us/rec/share/rbzl_7gTZLf3hAujU5fKDTWFfa2-dNS_OulUiMCerHYtvJ4AtLNCNN6u4ETdXqXP.IgaWpf81uinqEJKU
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:50 Hello, hi, Robert.
**Pellared** 00:53 Hello, hello, how are you?
**Liudmila Molkova** 00:55 I'm good, how are you?
You're.
**Pellared** 00:58 Yeah, sure.
**Liudmila Molkova** 00:59 interruption.
**Pellared** 01:00 No, it's the fight.
I would have been very tired today.
was exercising, like, 6 days in a row, and I think it was too much.
**Liudmila Molkova** 01:13 Oh, what do you do? Oh, do you exorcise?
**Pellared** 01:17 Typically.
**Liudmila Molkova** 01:17 Oh!
**Pellared** 01:19 So… Also, some muscle-ups, pull-ups, etc.
**Liudmila Molkova** 01:25 Are you doing Boulder, or…
**Pellared** 01:27 Rock climbing boulder.
But recently, on, only rockaimoolers, because mountaineering, I, like, on, on mountains takes more time. I would need to take days off to go to the mountains and climb there.
**Liudmila Molkova** 01:41 There is a mountain. Do you have a lot of mountains in Poland?
**Pellared** 01:46 Yeah, we have Tetra Maltines, so they are both lines from the granite, and they're, they're… Absolute.
Height is not that high, meaning it's, like, 2,500 meters.
But the relative can be, like, 1,000 or even more than… so… and they're also very compacted, so some people say that there are many Alps that you can go and, for example, have 3 summits in a row, in one day, which, for instance.
**Liudmila Molkova** 02:19 Nice.
**Pellared** 02:20 For, like, France, or things like that, it's almost impossible.
**Liudmila Molkova** 02:25 You're in Krakow, right?
**Pellared** 02:28 Excuse me?
**Liudmila Molkova** 02:29 Are you in Warsaw or in Krakow?
**Pellared** 02:31 I'm in Krakow, so Tatramote is in… I was in the south, in Zacopana, so it's just, like, 2 hours car.
**Liudmila Molkova** 02:39 Nice.
**Pellared** 02:39 Right.
**Liudmila Molkova** 02:43 I trust.
**Trask Stalnaker** 02:44 Trash calls?
**Liudmila Molkova** 02:45 It's not as bothering, right?
**Trask Stalnaker** 02:48 What's that? Oh.
**Liudmila Molkova** 02:49 You, you, you're Boulder, right?
**Trask Stalnaker** 02:51 Yeah, yeah, Robert Boulders. Robert's very good.
**Pellared** 02:56 No, you don't know.
**Trask Stalnaker** 03:01 I can tell. I can tell these things.
**Pellared** 03:06 Even…
**Liudmila Molkova** 03:11 Okay.
**Trask Stalnaker** 03:12 Yes, in, Salt Lake, maybe we should go bouldering in Salt Lake City.
**Pellared** 03:16 Yeah, I'm… I will… it'll be cold.
**Liudmila Molkova** 03:21 So, was it this…
**Pellared** 03:22 Okay, go on, go on, email.
**Liudmila Molkova** 03:25 So, I think De… Dan Dealer… He got a hotel in… Salt Lake City, or KubeCon, or in Atlanta, somewhere, and it was… Next to Climbing Gym, and they've.
**Trask Stalnaker** 03:40 It had a climbing gym in it.
Or something like that.
**Liudmila Molkova** 03:44 gave him the free pass there, so this is the perfect place to stay in Salt Lake City.
**Pellared** 03:50 Okay?
Noted. Important.
**Trask Stalnaker** 03:52 Yeah, yeah.
**Liudmila Molkova** 03:59 So, what is it we have today?
Okay, the same people… Same agenda? I think we've answered this last time, did we?
**Pellared** 04:18 Indeed.
You can remove it, probably.
**Liudmila Molkova** 04:25 Did we have anything for today?
Let's take a look if there's anything new…
**Pellared** 04:37 I was supposed to work on the events, but I have done nothing.
**Liudmila Molkova** 04:43 It's okay.
**Pellared** 04:45 Yeah, CGO was asked, you're asking CGO to make some com… To… I think it was in the related issue.
For feedback, but also he was in, Observability Days? No, I don't remember. Observability Summit?
So, also, he had no friends, probably.
Oh, he did answer here.
**Liudmila Molkova** 05:42 And for… For this one, we wanted… I'm thinking if iLogger is, like, the sufficient prototype.
Can you still hear me?
**Pellared** 06:04 Yes, yes, I can.
Like, there's nothing else right now.
**Liudmila Molkova** 06:09 Yeah.
**Trask Stalnaker** 06:11 Great access.
**Pellared** 06:12 But it's already there in iLogger.
If it is, then I will consider it enough.
**Liudmila Molkova** 06:24 I think this is more, like, the original, the Java prototype is for replacing the span events in instrumentations with logs, right?
**Trask Stalnaker** 06:34 Yeah.
**Liudmila Molkova** 06:36 So this is not… Just pure logger topic.
Okay, so maybe we should clarify it.
**Trask Stalnaker** 06:58 That is recording exceptions and logs? Yeah, yeah.
I think it's… Yeah, because the title reads wrong.
Because egg… Recording exceptions in logs is stable.
Yeah.
**Liudmila Molkova** 07:34 But Martin summed up, maybe we can ask Martin.
Okay… So Nanya's here.
No news here.
Then… the network timings… I think there… you folks had some discussion, did you lead anywhere?
Oh.
So this is the justification for having this as… event.
I, I kinda, I kinda don't buy it for a browser.
So… there is no Spanish instrumentation, but yet we are creating an alternative instrumentation for event.
Like, why shouldn't it be a… shouldn't we create the Span instrumentation?
**Trask Stalnaker** 10:26 I think they said that some of the data came after…
**Pellared** 10:32 Yes, that's correct.
**Liudmila Molkova** 10:35 But should that be a span that then ends after? Because the event will need all the information anyway.
Something evades the final thing.
**Pellared** 10:57 I also am not sure how… You know, how these APIs you turn the data?
if it's something that all the data is in the payload, because I don't think, or… Like, will they need to create an artificial span with, you know, weight? I'm just not sure how the implementation looks like.
But… Asked on me while, like, I thought she not explicitly mention, probably, it would be good to have some explicit I don't know, notice that this should be avoided, and used only if, you know, this data is coming asynchronously, or things like that.
**Liudmila Molkova** 11:34 Which one?
That should be awaiting.
**Pellared** 11:37 these events, these events, I think that they are coming asynchronously, if I read the conversation issue correctly.
I do not remember… if they come as one payload, or as many, you know, kind of events. This is something I'm not sure, because if it comes as something which is, you know, a singular event, then replicating to a span may be very hard.
You know, reconstructing iterations, etc.
So, if it's… if they're just having, you know, if they're instrumenting something that is really captured as the event by this API, then I think having semantic conventions may be helpful for them, but probably just having some additional, you know, footer, or just notice that this event should be only captured if it's not modeled, not possible to model by span. I'm just not sure, just, you know, brainstorming.
Because I kind of agree that maybe having this as an event in most cases, like, you know.
Can be awkward.
It also feels fresh for me.
That they say that they can… have this information about the span, and then later they say they cannot, so I don't know, it's depending on the version of the application, of the, I don't know, mobile platform, so there are a lot of, just, nuances that I do not understand.
I think I should probably read the issue more carefully.
**Trask Stalnaker** 13:23 Yeah, I think there's a lot of… I mean… I don't know how… Deep we want to get into this.
Cause… There's a lot of complications, Like, is this for browser timing? For browser timings, like, it's… I think it's partly, like, an adapter of an existing browser timing event.
That has all these things that we want to, you know, capture, and in that case, I'm… I kind of agree more with, like, Just capturing the browser event as it is.
And, you know, bringing it into OpenTelemetry.
Whereas that comment, that last comment down at the bottom there.
When you're fully… an event for each phase would have made more sense when you're fully instrumenting each phase.
You capture other attributes related to the phase.
I see here that just want the timing boundary.
I mean, it comes back to the overhead question, right? Like, that's the only reason, I guess, or maybe… Correlation… but I mean, correlation should… Not be a problem across the event.
I can reply again. I mean, I would like to push a little bit more on… you know, the… individual events.
**Liudmila Molkova** 15:19 Yeah, because the concern about leaking would apply equally to Spence and to this Uber event with everything.
**Trask Stalnaker** 15:31 Yeah, I really think it's just they're… they're just concerned about overhead. I mean, I feel like that's the only reason to prefer putting them all on one event versus having individual events.
So, we need more… Kind of justification.
**Liudmila Molkova** 15:59 Yeah, I don't see any mentions of overhead from… their site, but I agree, that's probably… D.
**Trask Stalnaker** 16:09 Yeah, that's what I was trying to get, that… them to say that.
What is the… Oh, it is, it was a SEMCOM. Okay, thanks, sorry.
**Liudmila Molkova** 16:31 Okay, it seems they… they even agree on this one, it's not probably long-term.
That's a G.
Okay, so then… Trasky'll reply, well.
**Trask Stalnaker** 16:50 Yep, yep.
**Liudmila Molkova** 16:51 If it's overhead, it's… it could be a justification. The current arguments, I don't feel they justify this choice.
**Trask Stalnaker** 17:00 Yup.
**Liudmila Molkova** 17:07 A, and down, the final one.
Not sure if anything happened since the last week. We probably need to talk more about it in the spec call.
And… I think we're going… we were going to tell Sijo to… Advertise it more, and bring it to the spec, alright?
**Trask Stalnaker** 17:40 Yep.
**Liudmila Molkova** 17:43 Cool.
Anything else I need to talk about in this quote?
Tim's answer is no.
**Pellared** 18:03 Have you submitted, the CFPs for KubeCon?
**Liudmila Molkova** 18:09 Not yet.
**Pellared** 18:10 Not yet.
**Trask Stalnaker** 18:10 Working on it.
**Pellared** 18:12 I think it's the last week, if I'm not mistaken.
For the makeup, con.
**Liudmila Molkova** 18:17 Yeah.
Did you?
**Trask Stalnaker** 18:19 Friday.
**Pellared** 18:21 Yeah, free.
This time, so I think this is the maximum.
**Trask Stalnaker** 18:29 Cool.
**Liudmila Molkova** 18:32 So let's get to this.
**Pellared** 18:34 No, but… One is about complex attributes.
one of our proposals together with CJ.
So, something that we need to do together. Nice!
**Trask Stalnaker** 18:47 Yeah, make them popular, make, all the, everybody support them.
**Pellared** 18:51 Yeah, that's also one of the reasons to make people aware, and that's also probably we're just… we just want to advertise the other main KubeCon. I do not even want to add it on the observability Day.
Just to have, you know, as broad audience as possible, but maybe I'm wrong.
**Trask Stalnaker** 19:12 Cool.
**Pellared** 19:15 Okay.
It was nice to see you.
**Liudmila Molkova** 19:19 Yeah, nice to see ya.
**Pellared** 19:21 Bye!
**Trask Stalnaker** 19:21 Bye.
