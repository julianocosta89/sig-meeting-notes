SIG: CI/CD SemConv SIG
Date: 2026-03-10
Duration: 15 minutes
Zoom Recording URL: https://zoom.us/rec/share/O7yrQVuDfRr59d_9mV7kQrlnufKmX35Ar8qQlyBzXrP2gmGX5KDgRTcr3bsS5DAf.phErG93CmE_cIT6y
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 00:46 Good day.
**Alan Clucas** 00:51 Hello!
**Adriel Perkins** 00:53 How's it going?
**Alan Clucas** 00:54 Alright, how are you?
**Adriel Perkins** 00:57 Doing okay, thank you.
I only have a few minutes,
Today, got a few conflicts that I've got to go take care of, but
Was there anything in particular that I missed or needed to talk about or discuss while I'm here?
**Alan Clucas** 01:20 Nothing I'm aware of, I'm not necessarily good at… remembering this stuff.
We didn't have a big meeting last week, it was only Christoph and I.
So… Somebody didn't.
discussed that much.
I guess the question I would have asked you if we had more time is,
What you wanted to do about, the environment variable spec changes that were proposed?
**Adriel Perkins** 02:05 What, what exactly… the proposal?
**Alan Clucas** 02:08 The proposal was basically anything that's not, alphanumeric gets converted to an underscore.
**Adriel Perkins** 02:19 Mmm.
**Alan Clucas** 02:19 But that was, Let me bring it up.
Gone.
There's no formal… Spec change here. It's just,
No, no formal proposal yet, I don't think.
Or was there?
So…
**Adriel Perkins** 02:51 I think there's an issue, right?
**Alan Clucas** 02:53 Has it actually raised an issue? I think you might have done now.
So that was 4914.
the spec.
Yeah.
So that's something we probably… should discuss At some point.
Have you got a link? What do you want me to share?
**Adriel Perkins** 03:17 Yep, I put it in the doc, too.
Cool. Yeah, I mean… when I think about the history of this, like, they did not want to…
We didn't want to just accept any and all environment variables, but we didn't want to predefine them either. So, the gist, the intent was that…
You know, environment variables have to be, or they're highly recommended that they're uppercase underscored.
**Alan Clucas** 03:52 Yeah.
**Adriel Perkins** 03:54 That makes sense from the environment variable perspective, when it lives in the environment. But once it's in code.
it doesn't… it doesn't really matter. The… well, it does matter when it's in code, because the text map propagator
Does not respect uppercase underscores.
It only expects whatever Actual specifications for propagator keys exist.
**Alan Clucas** 04:28 Yeah.
**Adriel Perkins** 04:28 So for W3C, it's trace parent, trace state. For B3, it's, I don't know, X whatever, X hyphen whatever, which I guess we didn't normalize for that occurrence.
We might actually just need, like, a dedicated Normalizer per, propagator.
But, like, the original intent was, like, if it's not part of the B3 or the W3 specification, once it's been normalized in the code, it shouldn't be respected.
**Alan Clucas** 05:05 Hmm.
**Adriel Perkins** 05:05 Because then it's, like, making up a whole new set of things and opening the door. But if it's, you know, going through the text map propagator, once it's been normalized in the code, the text map propagator will pick it up, and if it sees it represents whatever is in W3C or B3, then, like, it's good to go.
So that was the intent, and the reason why we didn't get overzealous, or… .
**Alan Clucas** 05:31 Yeah, yeah.
**Adriel Perkins** 05:33 So, like, I don't know that that is what we should do.
But I do think that there's probably a little adjustment for sure.
**Alan Clucas** 05:43 Yeah, my feeling was that… The carrier should… always successfully carry the things.
That was my concern over the current… the proposal was, like, we're just… we're making all this stuff up that says.
About rules for mapping from some undefined set of
words, the keys that we might have in B3, and… W3.
And that sometimes they might clash if you went through some normalization process, and then we would lose one of them, and that felt wrong. I want… from my point of view, the carrier should always
If you put stuff into the carrier and then pull it out again later, you should get the stuff that you put in.
And we don't seem to be… that didn't seem to be a particular concern, so.
**Adriel Perkins** 06:45 Well, once it goes into the carrier, it has to go through the text map propagator.
**Alan Clucas** 06:49 Yeah.
**Adriel Perkins** 06:51 So if it's, like, that happens today, I think, with any of the… like, you can put anything in a header, but it's not gonna necessarily carry if it's not according to the spec.
**Alan Clucas** 07:03 I'm not talking about the values here particularly, it was more the keys.
**Adriel Perkins** 07:06 Yeah, the keys.
Right?
**Alan Clucas** 07:09 Yeah.
**Adriel Perkins** 07:11 Like, the keys, like, like, so once it hits a carrier.
And goes into the propagator.
it's only going to… even in HTTP calls, it's only going to be respected if it aligns with the specification.
So instead of, like, trace parent, if it's, like, trace parent dash 5, like, it's not gonna get respected, right?
like, that's already the way the spec behaves, as far as I… if I'm understanding what you mean by carry, anyway.
**Alan Clucas** 07:41 Yeah, but it… It won't tell you that it's not going to succeed.
It's… at the moment.
It'll just It allows you to put stuff in that's not valid.
I don't know.
**Adriel Perkins** 08:03 I mean, that's… I think that's also the way the other carriers operate, yeah?
**Alan Clucas** 08:08 Maybe, it's just… it feels weird that we're…
We've got this thing, and we're trying to define a bunch of rules around it, one of which is not a rule that it should tell you when it's not going to work.
I don't know.
**Adriel Perkins** 08:23 It's not the carrier's job to do that, though, I don't think. I think it's the text propagator's job to do that, and I don't think the text propagator was intended to do that. I'm not… I'm not unsure why… why they don't do it now, but, like, when I send headers to it, I don't know if it's getting propagated or not until I look at the spans.
And it's like, you could put anything in environment variables inside of the environment, but not all of them are context-related.
In fact, most of them probably aren't, right?
**Alan Clucas** 08:50 Yeah.
**Adriel Perkins** 08:51 And that's why, like, we don't want the… we don't want every single thing to be considered carryable.
We really actually only care that, like, if it… once it's normalized, if it's been…
Translated to what a real specification allows for.
which would be W3CB3, and I think maybe there's, like, one other one.
And that's what I think matters, because it's whatever the text map… like, I don't want to own…
I don't want to own mapping. They didn't want us to own mapping. Anyway, they didn't want to own mapping. They just wanted to, like, use the text map propagator. It was like, alright, well, I mean, this does… this does work effectively, and there is a spec… specification for…
Those things. So this is kind of like a…
Like, part… well, also, part of that… that specification is specification, part of it is supplementary guidance, which is not.
a specification, which is… so, like, you know, the way that I originally did it was defining an ENV propagator, not carrier. But then we got asked, like, carrier is the better option. I was like, okay, but in the propagator, I would map them.
I would just… I just included a map of trace parent to trace parent, trace state to trace state, baggage to baggage, B3 to B3, and it just became part of the propagator, which was very explicit.
Yeah. So you could see it, but, you know, they wanted carriers, so… It's like, like, I get it, but, like.
I almost feel like it's, like, not my problem. You know what I mean? It's like, like, look, you guys got what you asked for, now you don't like it. Part of it is, like, you know, in the specification, what concessions do you want to make? So, that's my hot take for today.
because I'm uncaffeinated, and I should be caffeinated, and I'm not, so that's my excuse. But yeah, like, I can write this up on the issue. I just… I don't…
I don't fully, like… maybe it's that I just don't fully understand
What the real problem is here, like, what the real problem's trying to be solved is.
**Alan Clucas** 11:02 Follow that, I agree. That's why I was a bit surprised there was so much pushback on it.
**Adriel Perkins** 11:10 Yeah.
I'm gonna say no comment to your last statement, and I'll just leave it at that, and you could infer all you want to. I'll put this on my schedule of commenting on this.
**Alan Clucas** 11:27 Thank you.
**neil yashinsky** 11:30 I really wasn't paying attention to this issue at all, but I am now!
Seems interesting, though, from the very surface.
**Adriel Perkins** 11:45 Alright, I've got about, like, 4 minutes left before I have to hop off. Is there anything other… any other critical thing that I should be aware of, or that anyone wants to discuss that would like me to speak to?
**Alan Clucas** 12:01 Not for me.
**neil yashinsky** 12:02 Not for me.
I'm here for the hot takes.
**Adriel Perkins** 12:08 Hey, Dotan, good to… good to see you on.
**Dotan Horovits** 12:13 Hey folks, good to see everyone.
**neil yashinsky** 12:17 Yeah, same.
I owe you a reply to that message, by the way. It was good to hear from you.
**Dotan Horovits** 12:23 Oh, good.
**Adriel Perkins** 12:31 Alright, well.
**neil yashinsky** 12:31 You know, I guess we can come to the conclusion that, hey, for once, there's not a way too much stuff for us to deal with at this meeting, and just rejoice in that moment, I guess.
Sounds like a beast.
**Adriel Perkins** 12:46 Oh, there's nothing else for me.
**Dotan Horovits** 12:47 By the way, who's going to be in Amsterdam for, for KoopCon? Just, I know that I probably asked that before, but, you know.
So, Alan, I know that you're seeing you, but.
**neil yashinsky** 12:58 It's… it's definitely on my list for next year, for sure. Especially you promoting it so effectively.
**Dotan Horovits** 13:04 Yeah, that was a good opportunity for us to get together in person, so we're hoping to, hoping to be there as well, so, yeah.
**Alan Clucas** 13:13 Yeah.
**Adriel Perkins** 13:15 Looking forward to seeing you guys.
**neil yashinsky** 13:18 Thanks, Adriel. Thanks, Doton. Thanks, Alan.
**Dotan Horovits** 13:20 Thanks, everyone. Have a good one.
**Alan Clucas** 13:22 Alright.
**Adriel Perkins** 13:22 See y'all.
