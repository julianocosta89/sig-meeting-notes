SIG: CI/CD SemConv SIG
Date: 2026-07-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:35 Hello?
**Adriel Perkins** 00:39 Hey, good day.
**Christophe Kamphaus** 00:42 Oh, are you doing?
**Adriel Perkins** 00:43 Okay, how are you?
**Christophe Kamphaus** 00:45 Mine, and your dog.
**Adriel Perkins** 00:48 Still waiting, actually. They're… It's kind of… there's… she was supposed to… we took her there early this morning, but, they haven't started. It looks like they had another emergency surgery, so… She's… my dog's still waiting to be seen.
**Christophe Kamphaus** 01:07 Yeah, I wish you the best.
**Adriel Perkins** 01:09 Thank you.
It should be okay, it should be fine.
They turn teeth pulling into… A whole circle.
**Christophe Kamphaus** 01:19 To a life and death struggle.
**Adriel Perkins** 01:22 Yeah, exactly, exactly.
But I appreciate it. Thank you.
**Robert Pająk (Splunk Inc.)** 01:32 Bill?
**Adriel Perkins** 01:33 Yo.
**Robert Pająk (Splunk Inc.)** 01:37 Have you changed the URL to Zoom, or…
**Adriel Perkins** 01:40 Yeah, all the, I think Linux Foundation changed all the Zoom links for all the SIGs.
So, I did just update the workflow, Christophe, thanks for calling that out.
I just updated it, so…
**Christophe Kamphaus** 01:59 Yeah, so it's not every SIG that has done the update yet.
**Adriel Perkins** 02:03 Oh, really? Okay.
Just ours, and a few others.
**Christophe Kamphaus** 02:09 Yeah.
**Adriel Perkins** 02:19 Cool.
**Christophe Kamphaus** 02:21 And not much from my side. I've, I've asked again for the request review on our Jenkins PR.
**Adriel Perkins** 02:32 Awesome.
**Christophe Kamphaus** 02:33 Let's see how it goes.
**Adriel Perkins** 02:39 Cool deal.
I, opened up DSU in Tekton this morning. Andre… Andreas has already… responded, so, I might end up going to one of their calls, see if I can slate it for this week or something.
But we'll be working on that. I'm not sure if they have the bandwidth to contribute it, so, I will, if necessary.
But, I'm fairly unfamiliar with the project, other than using the technology, so, well, it might take me a little bit.
Of course, everything takes me a little bit these days, so… Anyway, hopefully that, that makes progress, though. They're, there's questions about CD events.
**Christophe Kamphaus** 03:28 Yeah, I saw the comment.
And one thought I had was, would it be possible to also transmit the same contacts, so… parent trace ID through their CD events.
So that we could maybe, transform one into CICD spense, and… emits CD events.
Be interoperable with that.
**Adriel Perkins** 03:54 Yeah, is it possible? Probably? Should we? I don't know.
There's, like, such a long… conversation about not doing CDI… CD events when we started this endeavor.
And making our own, and the structure of a CD event is definitely different.
OTEL technically supports it?
I think it's still technically an experimental, because no one's, like, really Taken and driven.
Like, beyond just saying that, like, we allow this.
Let's see if I can find it, actually. I'm curious.
**Christophe Kamphaus** 04:37 If I remember right, OTEL supports cloud events, which,
**Adriel Perkins** 04:43 That's what it is, yeah.
**Christophe Kamphaus** 04:44 defense is.
But there's no one-to-one mapping between CICD conventions and CD events.
**Adriel Perkins** 04:51 Right.
Yep, that's… that's what it is.
Yeah, Cloud Events is still in development.
itself.
Stuckle.
Yeah, I don't know.
I kind of don't necessarily want to revisit the original conversation that led us away from CD events, but… I'm open up… I'm open to suggestions, for sure.
**Christophe Kamphaus** 05:37 It was just a sword.
I don't have bandwidth for that either on my side.
**Adriel Perkins** 05:49 Income.
We'll see how the conversation with Technology proceeds, and then maybe… maybe more information will come out of that, and then we can revisit that thought.
**Christophe Kamphaus** 06:03 Yeah, I just thought it might be good to keep in mind.
If we start contributing code to Tektron.
If, say, you want to have both working together CD events and CICD, Context propagation.
**Adriel Perkins** 06:27 Yeah.
Cool.
Barbara, do you have anything?
**Robert Pająk (Splunk Inc.)** 06:35 Unfortunately not.
**Adriel Perkins** 06:38 Cool, no worries.
I haven't been able to keep up, with the… chat we had on the blog post and the, the inventory carrier blog post.
Is there… I have any…
**Robert Pająk (Splunk Inc.)** 06:57 I also have done nothing. I just thought that, yeah, I started to think if we should really, you know, start to prepare something, doing something, you know, more, you know, improving this observability, or we just try to publish a more simple blog post, just describing what we have.
Just to not pause for me too much.
**Adriel Perkins** 07:20 Okay. What's the… Target date that you want the blog post by?
**Robert Pająk (Splunk Inc.)** 07:29 For sure, before KipCon North America. That's for sure. Anything, yeah.
It could be sooner, but there's no rush, in my opinion.
**Adriel Perkins** 07:40 Okay.
Yeah, before KubeCon, I think, I feel like super doable.
that also, I think, opens the door for, like, well, do we want to just, like, since we already have a bunch of… We have all of our workflows and our GitHub org instrumented, through the collector. Do we want to just go ahead and start instrumenting some of the shared workflows that they have?
We could… we could possibly do that as an option and showcase that.
Cause they're, like, they're going full steam, Let's see, is this Trask and, pablo, and… Rilia? Rilia?
I don't know if I said her name right.
**Robert Pająk (Splunk Inc.)** 08:33 Marilla, right?
That's proof.
**Adriel Perkins** 08:35 Yeah, she's also our, liaison as well, for the CICD SIG. But yeah, they've been going, like, full steam on the shared workflow stuff. I'm like, I can't even… I can't even… I have to just ignore the emails at this point. I'm like, I can't even…
**Christophe Kamphaus** 08:51 Yeah, I saw Trask was setting up a shared workflow for pull request dashboards.
**Adriel Perkins** 08:57 Yeah. So, like, we could instrument… a lot of those are… those shared workflows are Python under the hood.
So we could actually just instrument the Python code to accept the environment carrier, and then update the workflow to put in the right context, like we've defined it in the GitHub receiver, and we can get those lower-level step stuff if we wanted to.
For the blog post.
**Robert Pająk (Splunk Inc.)** 09:21 Sounds reasonable.
like, anything we can showcase, I think, you know.
I think it would be better than just Roltex.
**Adriel Perkins** 09:30 Yep, agreed.
**Christophe Kamphaus** 09:32 Yep.
**Adriel Perkins** 09:32 Boom.
Alright, well, I'll take, I'll put… let me put this… where's my list?
I will take a look at, the shared workflow, see if we can find a good spot for it. I do need… I will need to update, Share workflow… I do need to… Nope, I never forgot what I was gonna say.
Anyway, I'll take a look at the shared Workflow stuff, see if there's a good spot for us to instrument. Oh, that's what I was gonna say. All right, there we go, I just had to recycle and repeat the same thing to remember what I was trying to say. I have to update the GitHub collector for… That actually gets all that information, because it's a bit out of date, so… for those spans and stuff to work well, I'll just have to update… update that, which it's been on my… backlog. No one's really been using it other than me occasionally, so… I will take that as well.
So, yeah, I guess between that, those two things, and then the Tekton thing, That's… that's, I guess, my area of focus for the next bit.
**Robert Pająk (Splunk Inc.)** 11:12 If you need any review feedback, you can always ask me, maybe I can, you know… Also, try to take a… Where?
**Adriel Perkins** 11:18 Okay.
Cool, yeah.
Yeah, appreciate it.
Alright, well, if there's nothing else, I guess we can call it early.
Appreciate y'all joining.
**Christophe Kamphaus** 11:35 It too?
**Robert Pająk (Splunk Inc.)** 11:35 Thank you.
**Christophe Kamphaus** 11:36 Have a good week.
You too.
**Robert Pająk (Splunk Inc.)** 11:38 I think so.
Bye.
