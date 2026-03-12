SIG: GC Project Management (EU)
Date: 2025-09-01
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/CBPB_9S72Q86qurgguWCse8_sMJJKGZSmVWruaRDF7Ku1VOvCg7CHlucCq25-pQ.AU4lCl9jJLZ9DMCn
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 02:53 Hey.
**Dan Gomez Blanco** 03:11 Hello there.
key.
**Pablo Baeyens** 03:18 How long is it going?
**Dan Gomez Blanco** 03:20 Good. Just getting back from holiday, so I'm…
**Pablo Baeyens** 03:23 Cool.
**Dan Gomez Blanco** 03:24 A little bit over the place. All over the place.
I don't know if anybody else will join.
**Pablo Baeyens** 03:39 Severin said he was here, so…
**Dan Gomez Blanco** 03:42 Okay.
**Pablo Baeyens** 03:43 Maybe he will.
**Dan Gomez Blanco** 03:45 C, coo-coo.
Yeah, I've got nothing set up, so, to share my screen or anything, but let's wait for Saturday.
**Severin Neumann** 05:29 Oh, my God.
Hey, good morning.
**Dan Gomez Blanco** 05:38 Hello, Holt.
**Severin Neumann** 05:43 Did you start already, or…
**Dan Gomez Blanco** 05:45 No, no, we're just waiting for you. I just said that.
**Severin Neumann** 05:47 Okay, thank you. Sorry, like, I was, again, this… this is happening so often to me these days, like, I'm like, oh, I have 5 minutes until my meeting, let me start something new, and then…
**Dan Gomez Blanco** 05:58 Yes.
**Severin Neumann** 05:58 Stop doing that.
**Dan Gomez Blanco** 06:00 I just leave a message, and then…
**Severin Neumann** 06:03 Yeah.
**Dan Gomez Blanco** 06:04 I just write an email or a message to somebody, and then you're, like, completely lost.
**Severin Neumann** 06:08 Yeah, yeah, exactly. Yeah, cool. I don't know how much is there on our… gender…
**Dan Gomez Blanco** 06:18 Yeah, I just got back from Saint Pablo, I just got back from holiday today.
**Severin Neumann** 06:22 No.
**Dan Gomez Blanco** 06:23 I'm a little bit… Lost.
**Severin Neumann** 06:26 I believe it's not a midstream.
Back.
Let's see… I can try to share my screen if you like.
So last week, Pablo and I… Pablo, I think it was the two of us, right? I think we were done in, like, 2 minutes or something like that, because there was not, like… really anything… .
**Pablo Baeyens** 06:48 Yeah, there's a few more today, but yeah, it's, like.
**Severin Neumann** 06:51 Yeah.
**Pablo Baeyens** 06:52 as well.
**Severin Neumann** 06:53 I hope now I share the right window.
**Pablo Baeyens** 06:57 Yep.
**Severin Neumann** 06:59 You can see, like, the spec, right?
Cool.
I need D, I need D, I need D to write a list of… issues, I think I have it here… Awesome. Oh, there's… dose here, right? Yeah.
It's all that's good.
From bottom to top, once again.
And, onSpan name updated method in spanProcessor… Seems to be an ongoing… Discussion.
Maybe we label it… Community feedback.
What do you think?
**Dan Gomez Blanco** 08:09 Is there still discussion going on here?
**Severin Neumann** 08:12 Yeah.
**Dan Gomez Blanco** 08:13 Yeah, I think so, yeah.
**Severin Neumann** 08:14 It's, like, 4 days old, and, like, or 5-4 days old, like, I mean…
**Dan Gomez Blanco** 08:19 Yeah.
**Severin Neumann** 08:20 I mean, we can also say, like, to the author, like, hey, if you join the… if you're able to join the Sikh meeting, then, you can also present your idea here, or something like that.
If you like, I can say that. It's tomorrow, it's Tuesday, right?
**Dan Gomez Blanco** 08:36 Yeah. Yeah.
**Pablo Baeyens** 08:37 Yep.
**Severin Neumann** 08:57 Okay.
One down. Composable sampler naming. I think that's, a sick issue.
Or… The sampling.
I seem to have a sick port, but… Yep.
That's an easy one.
third one, I think I moved that… From the web side.
I think the… I think I see the point. They're here with somewhere.
An exception should be recorded as an event.
And I think it's, like, like here, there's, like, a link missing back to…
**Dan Gomez Blanco** 09:43 Right, yeah.
**Severin Neumann** 09:44 ban event, I guess? I don't know, or like… I'm not exactly sure.
**Dan Gomez Blanco** 09:49 That changed now, didn't it? So… Well, I guess, at the moment, that would be, I guess, yeah. But anyway, we should probably link to… Yeah. Well, it says an event on the span, so yeah, I guess.
**Severin Neumann** 10:00 Yeah, but we are considering deprecating span events, right?
**Dan Gomez Blanco** 10:05 Yep.
**Severin Neumann** 10:06 How would we do, then, an exception? Would we then, like, Collect this as an event.
But still link it with Steam.
With C-SPAN, or how would this work?
**Dan Gomez Blanco** 10:18 As far as I know, that's the intention, that we, we would use the, sort of, the login API to… Create an event that's linked to the span.
**Severin Neumann** 10:29 For now.
**Dan Gomez Blanco** 10:31 that will still be represent… I don't know how that's gonna work, but I think that was in the OTEP, that it will still be represented as a span event until… I guess there's the deprecation of a span event API, but then the underlying representation in the… you know, an OTLP will still be.
**Severin Neumann** 10:48 Yeah. I mean, there's also the record exception.
**Dan Gomez Blanco** 10:54 Yep.
**Severin Neumann** 10:56 Yeah. Anyway…
**Dan Gomez Blanco** 10:57 I guess that's… They shoot Link, I guess there should be.
**Severin Neumann** 11:02 What's, like, the right label here? I think that's more like an editorial thing, right?
**Dan Gomez Blanco** 11:07 Yeah, I think so.
**Severin Neumann** 11:08 And then, right, I think… I think… That can be fixed by linking back to span event.
**Dan Gomez Blanco** 11:18 Every… yeah, I'm assuming…
**Severin Neumann** 11:19 Page.
Note that this is… Currently… The process of being changed.
But for the time being, This is not what we should.
Boeing.
Like that Make sense?
**Dan Gomez Blanco** 11:43 Yep.
**Severin Neumann** 11:43 Because at the end, if the author's open to raise a PR and say, like, hey, I just put there the link.
**Dan Gomez Blanco** 11:51 Do you want to add the link to… I just… Put the link in the chat, in the Zoom chat.
**Severin Neumann** 11:56 I am.
**Dan Gomez Blanco** 11:57 Spanish. Yeah.
**Severin Neumann** 12:03 Yeah.
**Dan Gomez Blanco** 12:11 Shoot up.
Should that be accepted, or who doesn't?
**Severin Neumann** 12:15 I would call it an accepted, right? I mean, if we are… because, like, it's not really… It's small enough, right? It's really like, yeah, just let's add that link. I mean, if anybody from the TC then really disagrees with that and says, like, hey, actually, that's not correct, and whatever, but I think, I would just… Who is like Dad, right?
**Dan Gomez Blanco** 12:41 Yep.
I mean, for now, that's the advice, I guess, you know, if there was a… because it hasn't… Span events haven't been officially deprecated. I guess when they are.
Then… that advice will have to change, right, somehow.
**Severin Neumann** 12:55 Yeah.
Yeah.
this one I copied from… the community repo, because I thought, like, hey, this is actually a spec issue. I think the TLDR is then, like, the suggestion as to when, like, a span is recorded.
or, like, that you include, like, the file name and line number, like, when you say, like, trace or start a span or something like that. I think overall it's a good idea, but I mean, the reasoning totally makes sense, right? I mean, if you… If you record a span, it's of course valuable to know, like, okay, where was it recorded?
But I think the only thing, I don't know, like, if this is really feasible in all the languages.
**Dan Gomez Blanco** 13:47 Yep.
**Severin Neumann** 13:48 Because, like, you would need to walk up… like, like, when I say, like.
call the API or the SDK implementation, like, I would need to go back to, like, where it was called, and then say, like, oh, this is this… and there's a lot of languages where this is basically impossible, right? Because if they're compiled.
You probably have… have no… How would you do that, right? I mean, that's like…
**Dan Gomez Blanco** 14:13 Yep.
And there's… just playing devil's type of kick here, I think that… it makes sense, but, Do you think it's a spec issue, or a… Like an instrumentation… As in, like… something that can be implemented in certain languages as a, you know, optionally, they support it as an instrumentation library.
I can…
**Severin Neumann** 14:38 Yeah, but still, the question is, like, where should it live outside of the spec, right? I mean, it seems like, at the end, my feeling is, like, this boils down to recommendation, where we say, like.
We highly suggest that you're doing that, but we cannot really, like.
But I would like the TC and, like, the spec maintainers to see it, and maybe there's someone who's smarter than me that says, like, oh, actually, this is something we can do by doing X, Y, and Z in I mean, there's languages that support that, right? I mean, there's languages that… they can do this in some extent by… I think even, like, his Python example, I think there's something in it.
where you can figure out, like, the line of code where this method was called, or something like that. In scripted languages, this is possible, but they said in a compiled language, I would not know.
How you would do that.
**Dan Gomez Blanco** 15:35 Yeah.
**Severin Neumann** 15:35 But yeah, so I would, I would just triage it as, that it needs community feedback.
Do we have…
**Dan Gomez Blanco** 15:51 I guess… The code semantic conventions, say, have, like.
**Severin Neumann** 15:58 It's stable, right?
**Dan Gomez Blanco** 16:01 Yeah.
Is that…
**Severin Neumann** 16:05 Oh, you mean that it, like…
**Dan Gomez Blanco** 16:07 Because other semantic conventions say, okay, we… this is how we measure, this is how we, you know, how we do.
**Severin Neumann** 16:12 You mean that it maybe belongs into semantic conventions? Yeah, that could also be that, like… Dead.
Then actually, like… Yeah, but anyways, then someone can move it back into semconf, I just…
**Dan Gomez Blanco** 16:26 Yep.
**Severin Neumann** 16:26 like, if it remains in the community repo, it gets lost, right? I mean, it also can get lost in the spec, but, I can also suggest them to, like.
**Dan Gomez Blanco** 16:47 Yeah.
Hi, Jurassic.
**Juraci Paixão Kröhling** 16:53 Hello, hey there.
**Severin Neumann** 16:56 Hey, good morning.
**Juraci Paixão Kröhling** 16:58 Morning.
I'm sorry I'm being late, and I can only stay for 10 more minutes, but .
**Severin Neumann** 17:04 numbers.
**Juraci Paixão Kröhling** 17:04 What's…
**Dan Gomez Blanco** 17:06 That's cool. No worries, I think we're… there wasn't that much to triage, I think.
**Pablo Baeyens** 17:15 Yeah.
**Severin Neumann** 17:22 Packed up.
**Dan Gomez Blanco** 17:24 Yep.
Oh my god.
**Severin Neumann** 17:27 Just one more.
remove. It is not necessary for implementations to ensure the changes to NFTs.
This… Block?
Yeah.
It's just not… I mean… Riage-wise, there's not a lot we can do right now, right? I mean, it just needs feedback.
**Dan Gomez Blanco** 18:27 Yeah, I think I would call that community feedback.
**Severin Neumann** 18:33 I mean, I suspect that Robert is probably going to the SPAC meeting or something like that, and then getting the kind of feedback he's looking for.
So, yeah.
**Dan Gomez Blanco** 18:43 But that was not specific to logs, right? That was for…
**Severin Neumann** 18:47 Oh yeah, he labeled it as for logs, traces, and metrics and everything, but… There's nothing to follow up with.
Anything else we need to, or should look into? Anything else we'd like to… Don't think…
**Dan Gomez Blanco** 19:09 Is there anything in the community repo, or… I don't think so.
**Pablo Baeyens** 19:25 No, I don't see anything.
**Severin Neumann** 19:30 And I think we're done.
**Dan Gomez Blanco** 19:31 Cool. Just one question that was not there last week, unrelated to triage, but now that you're all here.
How's it going with, elections? Like, has that been set up, or… I know that we talked about, like, starting… Just thinking about…
**Severin Neumann** 19:49 And… I…
**Pablo Baeyens** 19:50 I think.
**Severin Neumann** 19:52 I missed also parts of the GC meeting last week. I think we had to… To non-recorded topics that consumed, like, All the time.
**Juraci Paixão Kröhling** 20:05 We haven't spoken about elections at all this week.
**Severin Neumann** 20:07 Yeah, I was wondering that, like, I think… Oh yeah, Morgan actually, like, was also like, elections was our status, what needs to be done, so probably we should make sure that this is a priority.
this week.
**Dan Gomez Blanco** 20:29 Yeah.
**Severin Neumann** 20:29 Let me copy that just over, I just have to open the… our meeting notes, so I can… When is our meeting, it's, yeah, I just copy everything into place, and then… And…
**Dan Gomez Blanco** 20:47 Good stuff.
**Severin Neumann** 20:50 Yeah.
This is the third grind. Yeah. Oh, no, I moved it, My farm loves me.
Yep. Done.
And let's talk about that on Wednesday.
**Dan Gomez Blanco** 21:06 That's good.
**Juraci Paixão Kröhling** 21:08 Oh my god.
See ya, bye.
