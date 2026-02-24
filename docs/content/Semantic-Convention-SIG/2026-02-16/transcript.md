SIG: Semantic Convention SIG
Date: 2026-02-16
Duration: 19 minutes
Zoom Recording URL: https://zoom.us/rec/share/vRGv8QNdZcl3RXlvqBTfHd_QEsqIL91KFVjwPpKBnis01WKjRKgSAPGPfn53Lhug.qMdGwtxMIkD1-KA8
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 05:38 Bye, folks.
**Carlos Alberto Cortez** 05:42 Oh, hey, hello!
**Liudmila Molkova** 05:44 It seems it's, the US holiday, and we forgot about it.
**Carlos Alberto Cortez** 05:50 Yeah, actually, that's what I was wondering, because, yeah, there are no topics other than what I have myself, and there are no people here.
**Liudmila Molkova** 06:02 Yeah.
so then probably we should cancel.
You want… you wanted to chat about spun lifecycle.
**Carlos Alberto Cortez** 06:12 Yeah, maybe you have some information, even if it's only you, and I.
Basically, it's about, so, you may remember this, this, issue is regard, regarding adding events.
Or span lifecycle, which could be 3 for now.
using an event when the Spanish started, when the span ended, and a hoard beat, which would be, like, an fixing terrible.
So the thing is that, of course, we are trying to send information… I mean, this is, like, for long-running spans, so in theory, you want to have as much as information as possible. And the thing is that we are essentially resending basically everything
that you could be sending over Proto, or OTLP, sorry, sorry, over OTLP, both using semantic conventions.
And I was wondering whether there's some prior art
on this one, I was… I did a quick look and didn't find anything. Like, for example, how do you…
how do you set the attributes, you know? Like, go JSON? Like, what do you do there, you know? And if there's any guidance.
That exists already, yeah.
**Liudmila Molkova** 07:19 I don't think there is a guidance.
But… Let's say if you record… spend started, there would be…
On event spawn Start, you would provide attributes.
the tube.
That you had at the start time, right? And… the…
The… we would need to find means to record, let's say, parent
spend ID, right? Because it's not on the events otherwise.
**Carlos Alberto Cortez** 07:53 That's correct, yeah. I mean, you can link the span context of the span that the log… the event belongs to, as part of, you know, a normal log… log record, but the parent, you need to specify everything, you know?
**Liudmila Molkova** 08:07 Yeah.
Then… The span name is another one, right? The span name cannot be event name.
**Carlos Alberto Cortez** 08:18 It's done.
**Liudmila Molkova** 08:19 dynamic.
**Carlos Alberto Cortez** 08:22 Yeah, I would say… I was thinking of adding an actual… the event name would be something like Hotel SDK Span Only Start, something like that. Yeah, the actual span name would be something else, like, I don't know, like, it could be in the attributes, you know?
**Liudmila Molkova** 08:39 Yeah, so, you know, we're working on something similar. Maybe I can share and walk you through.
Yep. Not similar, but related.
So, it says this, she talked about,
We are, trained to represent are…
Span exception events as logs because of span events deprecation.
And… what it means… That we need to find a good event name.
And we're calling it, let's say, if we are…
emitting it around HTTP client request, their client request exception.
And it would be… more interesting.
Maybe, I don't know.
To call it spend client request.
Start?
That would be an interesting question.
**Carlos Alberto Cortez** 09:53 Yeah, I mean, the name, I think it's fine, and we can follow whatever you suggest.
What was, sorry, what was the name of that, the number of that issue, so I can review that? Or it was a PR?
**Liudmila Molkova** 10:06 This is a PR…
**Carlos Alberto Cortez** 10:10 If you want to change.
Perfect, yeah. But this is… this is to remember. It's 3311, I think.
**Liudmila Molkova** 10:16 Oh, okay.
**Carlos Alberto Cortez** 10:18 It's easy to remember. Okay, perfect, yeah, we'll review that, yeah, I will come with that. In the meantime, my plan was to present a PR for the spec, because we want to add these processors and these events to the spec. And then, I mean, that's why there are two issues. One of them is for discussing that, like.
in the SEMCOM group, but I just started… because I was just, like, mocking… well, not mocking, just writing a prototype for the… for the coding part, but yeah, this one, I will explore that.
So I will… I will read that PR, see how it goes.
And, yeah, probably I will go with the simple way for now in the prototype regarding trace ID and all those things, probably just use strings, and we can discuss that next week here.
**Liudmila Molkova** 11:03 Yeah.
Yeah, so the only tricky question you'll probably get is.
They're around the Span name and Span identity.
Like, you… you cannot even populate this from… from this plan itself. You don't know.
**Carlos Alberto Cortez** 11:21 Yeah, correct, correct.
Yeah, correct, absolutely. Yeah. And yeah, the other thing that I have in mind about attributes is, like, when you're sending the actual attributes that somebody's providing upon start… start time, we'll be just doing JSON style, you know?
**Liudmila Molkova** 11:40 What, why?
**Carlos Alberto Cortez** 11:43 Like, for example, like, when you're setting a span, and you… the user provides you 5 attributes.
You need to put those attributes, or it could be useful to report that, to report them as part of the event.
Yeah. But you want to separate them from any attributes, like, you yourselves and the event want to put.
**Liudmila Molkova** 12:04 Why?
**Carlos Alberto Cortez** 12:07 So, for example, let's say that as part of the bench, you add an attribute called parent, I mean, just…
Let's sake, for the sake of simplicity, parent…
span.parent, and that is a map that includes, trace ID, trace flags, trace state, everything from the parent. So basically, you don't want… the LEA would say.
You want to separate that from the attributes that the user has, you know?
**Liudmila Molkova** 12:36 Oh, this… oh, but you… the span itself doesn't have any information about parent except parent ID.
It's just one…
**Carlos Alberto Cortez** 12:47 I mean, yeah, the span has everything. The only problem there is, I mean, since it's a long-running span.
you will get the span info… and I don't know if this is what you meant, like, you're getting the actual span only when it's actually exported, you know?
**Liudmila Molkova** 13:04 Right, and even in the processor, you probably are getting the red-white span, right?
**Carlos Alberto Cortez** 13:11 Yes, correct. No, actually, you're getting the, well, the readable span, yeah.
**Liudmila Molkova** 13:15 Oh, readable, right.
**Carlos Alberto Cortez** 13:23 So it's easy.
**Liudmila Molkova** 13:24 you wouldn't need the whole parent anyway, because you'd never export anything on the span. Like, why would you export something on the span event that's
Sorry, why would you export something on the event if you never exported on this path?
**Carlos Alberto Cortez** 13:40 Yeah, actually, that was the third big question, like, why, like, what kind of information do you… you don't actually need to be sending, because…
You know that the Spanish started, and all that, and it's still working, but… Not exported, you know?
Yeah.
Yup.
One of the things that I briefly discussed with the guys at the CICD group is that we could start with sending the most, like, the bare-bones information, you know?
And go start from there. Probably that's a good idea. Sorry, go ahead.
**Liudmila Molkova** 14:22 I would imagine, like, you should not send more information than You would otherwise.
Sand, if it was a span.
**Carlos Alberto Cortez** 14:35 Yep.
**Liudmila Molkova** 14:36 So maybe, okay, there are edge cases when somebody sets an attribute and then sets this attribute to null , effectively removing it, but that… that's an edge case, and you just get multiple states for the same thing.
**Carlos Alberto Cortez** 14:51 Yeah, great.
That way, yeah.
**Liudmila Molkova** 14:55 It will save a ton of…
effort, I think, for this case.
**Carlos Alberto Cortez** 15:03 Yep.
Yeah, totally.
Okay, yeah, I think that's good feedback. Yeah, I think I will stick to then, for now at least, for the minimum information we need.
We can add more information as we go. And of course, this could be experimental at first, so I think we are safe.
**Liudmila Molkova** 15:22 Yeah, is it the… it's part of CICD, right?
**Carlos Alberto Cortez** 15:26 Yes.
**Liudmila Molkova** 15:27 Oh, cool. Yeah, so because we are kind of… we're… Becoming very,
aggressive on prioritizing and scoping things out, and we need a SIG for
to drive anything reasonably big, and since it's parts of CICD, it's great.
**Carlos Alberto Cortez** 15:47 Yeah, to be honest, I think this is something that, if I remember correctly, that the CACD group mark as something to have, good to have, so it's not super part. I know, we know it's a risk, not… there's a big risk about not having this in the current, roadmap stage.
But, yeah, we would like to work on that.
I don't know if… yeah, so…
Yeah, so it can be, like, medium priority or something like that. Like, we need people to actually review that, but yeah, we don't… well, as of the time being, we don't have any rush, let's say, you know.
**Liudmila Molkova** 16:22 Yeah, I would be interested in reviewing it, I think it's great.
**Carlos Alberto Cortez** 16:26 Perfect.
Okay, perfect, yeah, that's good information. Yeah, thank you for… so much for the feedback. Yeah, I think we can call it a day, then.
**Liudmila Molkova** 16:36 Yeah, thanks. Enjoy the day without U.S.
**Carlos Alberto Cortez** 16:41 Yeah, actually, that would be funny, so, yeah. Actually, I have one more call, but it's, with…
people from UK, so probably didn't show up.
So yeah, let's see how that goes. Otherwise, yeah, see you, see you around. Thank you so much for coming back.
**Liudmila Molkova** 16:57 Bye.
