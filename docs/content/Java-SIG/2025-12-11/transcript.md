SIG: Java SIG
Date: 2025-12-11
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Trask** 03:09 Hey, Steve!
**Steve Rao** 03:10 I trust her.
**Trask** 03:13 Hey, I'm only on my phone, so, maybe if you can share and drive the meeting.
**Steve Rao** 03:22 Okay.
Hmm.
Oh, sorry, maybe I need to reset the privacy of my computer, so I need to re, restock the Zoom again.
**Trask** 04:02 Okay. Okay.
**Steve Rao** 05:18 Okay, can you see my screen now?
Hello, trust me.
**Trask** 05:24 Yep. Yep.
**Steve Rao** 05:26 Okay.
And, yeah, today, yeah, we have to, Content in agenda.
Yeah, one… one is from Mia, another is from Minghui. She, he will join us later.
**Trask** 05:45 Okay.
**Steve Rao** 05:46 And, yeah, it's our first,
Yeah, the first one is about, extension, and maybe we, discard in our own issue before.
And, yeah, we want to add an extension for flexible span filtering before spam creation.
**Trask** 06:14 Right.
**Steve Rao** 06:17 And, yeah, I saw you also left comments, and I explained the reason.
Yeah, the first one, yeah, if we use the assembler to, to filter, some
spam creation, but, but it will… yeah, the metrics will also include the related request. This is the first point.
**Trask** 06:51 Okay.
**Steve Rao** 06:52 And, the… another point is, is about performance.
And, yeah, if we use the sampler, yeah, it will execute some logic in, in Starter.
And, in some, in some case, we want to, filter the related request, as,
Yeah, before the start method in Instrumenter.
to lower the performance. This is the second reason.
**Trask** 07:30 Aha!
Have you seen, the… incubating work in the Java SDK for Tracer is enabled?
**Steve Rao** 07:45 a null .
your means in ST.
Let me check.
Yeah, what is the name of the method, of the class?
**Trask** 08:17 Look for Extended Tracer.
**Steve Rao** 08:23 You can tensor…
Spacer.
**Trask** 08:34 Extended tracer.
**Steve Rao** 08:48 Here.
**Trask** 08:50 Yeah.
So this has is enabled on it.
**Steve Rao** 09:00 Yeah, you mean that it can, achieve a similar effect.
**Trask** 09:05 Yeah…
**Steve Rao** 09:08 Okay, okay, let me check, yeah, nature.
Yeah, okay, yeah.
**Trask** 09:16 Yeah, so this feature hasn't been…
The feature is… the goal is to do something similar to what you want to do.
It may not be… Complete.
But if you could provide feedback on what we would need to do for Extended Tracer is enabled, because there's also a similar for logger, extended logger is enabled.
And, and there's also meter metrics is enabled.
And so, the idea is there is you could configure
These things at a more granular level.
**Steve Rao** 10:05 Okay, yeah, okay, thank you. Yeah, I will check it later, if it can,
achieve, yeah, my demands, yeah, maybe, yeah, it's okay. Yeah, I will close my issue and the PR.
**Trask** 10:20 Cool.
**Steve Rao** 10:21 Okay, thank you.
Okay, yeah, next question, yeah, is from Minghui, yeah.
**Minghui Zhang** 10:30 Sorry for the lead. My computer is out of power, so I just, link this meeting by my phone. Could you share my, PR?
**Steve Rao** 10:42 Okay.
**Minghui Zhang** 10:45 Yes.
**Trask** 10:45 No worries. I'm on my phone also. Steve is driving the meeting today.
**Minghui Zhang** 10:53 Okay, so, I want to show a minimizer, JSON serializer to, resolve the issue that we have, talked about,
Before, two, two, two weeks ago, yeah. We just want to, capture the complex, attributes as a JSON string.
in span. So, that's the PR to, implement it.
Steve, could you please, show… just to show my draft of PR? Yeah.
Let…
**Trask** 11:34 Let's first talk about, I left a comment on the issue.
**Steve Rao** 11:39 Okay.
You mean here?
Do you see?
**Trask** 11:43 Yeah… Did I… I thought I let… Oh, on the issue.
**Minghui Zhang** 11:51 Maybe you see the last one?
**Trask** 11:57 No, no, on… You had a… Issue for this?
No.
Steve, if you can go back to the original issue…
**Steve Rao** 12:15 Fuck here.
**Minghui Zhang** 12:15 -
**Trask** 12:17 About the… no, about the JSON.
Serialization.
**Steve Rao** 12:24 SDK.
**Trask** 12:25 So, he linked to… I think he linked to the wrong issue.
**Minghui Zhang** 12:29 Yeah, you could please, could you please, link to, link to, one file when…
Sorry, could you, check the emigrator the PR named Migorousin.
the right one.
Make… make great.
Mmm… There's a, okay, got it.
**Steve Rao** 13:04 a wasteful.
**Minghui Zhang** 13:05 151… 15174, I mean.
That's the issue.
**Steve Rao** 13:15 Are you sure?
**Minghui Zhang** 13:16 Okay.
**Trask** 13:19 Let me see, I thought I left a comment, but maybe I didn't.
Anyway, my question was, do… is this…
Just temporary until we have complex attribute support on spans.
**Minghui Zhang** 13:40 Yeah, it's very, temporary.
**Trask** 13:44 Okay. So, let's not add it… to the instrumentation API, then?
Let's just… You can just embed it in the… Gen AI… semantic convention PR.
Right? Just hide it as an internal class.
**Minghui Zhang** 14:11 you mean we just added, you mean the package?
Right? The Gene AI package?
**Trask** 14:22 I mean, specifically the OpenAI, so you only need this for one.
**Minghui Zhang** 14:29 Oh, I got hit.
**Trask** 14:31 It doesn't need to be reusable.
**Minghui Zhang** 14:35 Hmm… It makes sense, but, we, it may, might… Mmm…
Let me see… We may add this class for multiple, gene AI,
multiple GNI instrumentations for, like, OpenAI, Spring AI, Spring AI, Alibaba, like this.
So, it's a reutable, cast for me.
**Trask** 15:12 How soon are you going to… because we are,
still hoping, trying to get this all stable, the value… the complex attributes by, early February.
Do you… Are you…
going… that's why I was thinking just go ahead and add it to the one that you need.
**Minghui Zhang** 15:41 Yeah.
It makes sense. So, you mean, what, what do you mean, if I just, add this, class as an inner class in the, specific, instrumentation?
**Trask** 15:59 Yeah, so… in your… OpenAI PR?
**Minghui Zhang** 16:05 Okay.
Okay, I've got…
**Trask** 16:09 Add it as a package-protected or internal class.
**Minghui Zhang** 16:16 Hmm.
Hmm, it makes sense.
**Trask** 16:20 That way, there's less… it's easier to,
Making anything that's public or reusable is going to require a lot more review and scrutiny.
**Minghui Zhang** 16:36 Oh, yes.
Right.
**Trask** 16:41 That's why my recommendation is just to hide it inside of your, your instrumentation PR.
**Minghui Zhang** 16:51 Okay.
So, so let me do it. I will, if I just migrate the, like, something like a JSON writer that we have, what we have held for the minimizer JSON serialized in the OpenAI instrumentation, it's…
It's okay.
I mean, it's, it's runnable for… for… for…
It's viable for us to just add this, class in the instrumentation package.
**Trask** 17:37 Yeah, you can put this class in the OpenAI instrumentation module.
**Minghui Zhang** 17:45 Okay.
**Trask** 17:47 And I didn't check, follow if you copied this from somewhere, but, just to make sure that the license, if it was, like, ported from somewhere, that you include the license headers.
And we can help… I can help you with that if you… Just CC me.
**Minghui Zhang** 18:14 Okay, okay, thank you. So this class is just from, Datadog's, Java, repository. I just copied it.
**Trask** 18:27 Okay, great. So, oh, I see you say there. Yeah, so when you send the PR, or when you add this to your OpenAI PR.
**Minghui Zhang** 18:41 Yeah.
**Trask** 18:42 Will you make a comment and CC me, and I will… point you to,
Our standard format for, Documenting copied material like this.
**Minghui Zhang** 19:02 Okay, okay, thank you.
**Trask** 19:04 Yeah.
**Minghui Zhang** 19:06 Cool. That's horror.
I have no more scenes to, discuss.
**Trask** 19:16 Alright.
**Steve Rao** 19:17 Okay.
Yeah. If we don't have one.
**Trask** 19:22 Third.
**Steve Rao** 19:23 Yeah, maybe… yeah.
Yes, see.
**Trask** 19:25 Well… I think we're… this is our last, APAC meeting of the year.
**Steve Rao** 19:32 Yeah. Yes.
**Trask** 19:33 I will be around, still working next week if you have any questions, and then I'll be out the two weeks after that.
**Steve Rao** 19:44 Okay, thank you.
**Trask** 19:46 And, so yeah, Happy New Year!
**Steve Rao** 19:49 Happy New Year.
**Minghui Zhang** 19:49 Happy New Year.
**Trask** 19:51 Do you…
**Steve Rao** 19:52 goodbye.
**Trask** 19:53 Then, yeah, bye.
**Minghui Zhang** 19:55 Bye.
See you next year.
