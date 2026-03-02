SIG: FAAS WG
Date: 2025-07-31
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Serkan Ozal** 02:53 Hello!
**Tyler Benson** 02:56 Hello! Hello!
**Warre Pessers** 02:58 Hello!
**Serkan Ozal** 03:01 How are you guys doing.
**Tyler Benson** 03:05 Been a busy summer so far, lots going on.
**Serkan Ozal** 03:11 Okay, let me pass through some, some pull request initially, if
there is not any urgent topic from your side.
and then maybe we can also discuss
about the context propagation what he has been working on that.
And
again for for this week's meetings. I will have to leave in 25 min to to join, I mean the another
meeting. So.
**Tyler Benson** 03:47 That's like.
**Serkan Ozal** 03:48 Yeah. So let let me 1st share my screen.
**Tyler Benson** 03:52 We can keep it brief.
**Serkan Ozal** 03:54 Yeah. I just send the Pr to introduce the the configure logo function and deprecate the logo provider. You remember that from the Gs Maintainers Maintainer Trend has
had sent a Pr. To to fix a Ci failure. Once we migrate to the newer version of the Js. SDK, open telemetry jstk, because the Sm processor function
is not available anywhere over the logo provider. So instead, we should use the logo, configure logger function.
and according to our discussions we were agree on that.
Like tracer and metrics, we should have the configure logo function
to be able to configure the global the logger configuration.
And therefore I just send this small Pr and so, as I said, I just put the deprecated notice to the existing matter provider and the logo provider functions, and then introduce the configure logger function
which will be the way of
configuring the logger by the users at like adding the processor and something like that, because
the adding clock record processor is not
available to the logo provider anymore. Hopefully, we will be removing
these deprecated global functions, as like we already did for for the tracer.
And also this week, I think it was.
I mean, it was about 4 weeks ago we published the the previous release.
If there's no objection, I think we can have another new release next week.
just to be sure that we are releasing something every every month.
Yeah, that is my small Pr, and also.
**Tyler Benson** 06:10 I just approve that that Pr, I think it looks good but I think it'd be also good if we could get worry, or Ivan or some of the Javascript experts to weigh in. But from my perspective, I don't have any problems with it.
**Serkan Ozal** 06:29 Okay, I will add them as a reviewer, too.
**Warre Pessers** 06:33 I will double check right after this meeting.
**Serkan Ozal** 06:38 Sure. Thank you.
And yeah, we have another Pr and Tyler and me, and all of the approach just to adding the invocation. Ids.
To the to the logs
which are produced by the the collector extension by using telemetry Api.
I didn't have a chance to to check it out manually. But as far as I see, the motivational to Pr and the and the implementation looks good looks. Okay?
And do you think Tyler should be merge this
as of now or wait the okay, he just he just respond, okay.
he just respond, 4 min ago, okay.
okay, worry. If you also have time to to check this Pr. It will be good. So I think we. We can also merge this Pr. And have part of the release next week hopefully.
**Warre Pessers** 07:40 Yeah, sure. I'll I'll look at them both or all the the other ones you want to discuss as well right after this meeting and give my approval if
applicable.
**Serkan Ozal** 07:53 Oh, and yeah, I mean, this Pr has been sent to 2 weeks ago. I mean the
I have a few I mean, con, not the concerns, but items we need to check on this.
First.st I'm not sure whether it will have some effect on the call. Start delay, just adding another processor. I don't think so, but still it might be good to to check that. Maybe we can ask to the to the one who sent the Pr. And also I'm not sure. I mean how we are building till the collector extension by by auto, discovering the the processor. But as far as I see from the implementation
the guy just just added the the transformer, the processor.
but not sure how they are automatically registered or discovered by the collector and session during build or runtime so I was not sure whether this, the the current implementation, is okay or not.
So that's the reason that why I have not. I mean, given okay or not to the Pr. But if one of you guys have, I mean more experience on that.
It will be good to to check this out.
Yeah, this was the issue. Yeah, these are the these are things I mean.
I just wanted to quickly pass through.
And do you guys have any other topic to to talk and discuss.
**Tyler Benson** 09:38 No I'm happy to go through some of these on my side and double check, and but overall, I think everything looks good.
**Warre Pessers** 09:50 Yeah, I'll do the same. I'm not really that familiar with go. But I'll look at it anyways.
**Tyler Benson** 10:03 Yeah, thanks for your effort, Cirken. Good job. And I
if you would like, or I would encourage you to add some of these links to the the notes, so that it's
easier for us to find them. But other than that, I think we're good.
**Serkan Ozal** 10:24 Okay? Sure.
Yeah. Also. I mean, as far as I understood, Bori has some progress on the
context. Propagation things for for the event driven communication like like to Sqs. For example.
**Warre Pessers** 10:41 Yeah, so basically, I looked at the pub sub propagation package that is used in the normal Sqs propagation for node as well. It's quite
trivial, let's say, to do the spend linking, which is what we want to see when when processing the spans with another lambda
and also, it's I double checked this for you. But I didn't get back on this. I think it sets the parent context correctly as well. So I think it's all good on that.
so I guess I can now start to work on a proper pr for the repo, and then maybe
also pass this by you, sir, can to maybe look into this as well, because I know we try to do this as non-breaking as possible.
But I'm not quite sure how easy that is going to be.
**Serkan Ozal** 11:48 I, yeah, I am good to to start talking about on the some
some implementation. So I think it will be easier for everyone to to get the to get the idea. Personally.
I am okay with the Pops up propagation. As far as I check the check the implementation. Also.
I find, found their
instrumenting approach interesting like instrumenting the patching, the the array, I mean loop functions. That seems I mean interesting approach to me. But I mean, it looks okay. Yeah, I just
couldn't be sure on that. How
or whether we can use the Pops up propagation functionality to to to customize it for for the spell linkings. Because, as far as I remember it, just connects
the processing depends with the parent context. That's okay. But I just couldn't find. I mean.
find a way. I mean, to to be able to customize the sip linking by using the pubs of propagation.
So that was, I mean, my my only
a point to to check it out. But overall, I am okay with the with the approach you are. We are working on.
**Warre Pessers** 13:18 Yeah, So
I was currently working on that a little bit. But it's like, not really properly coded right now. So let me, maybe just
put this on a branch in my personal repo, and then I can link it in slack. So you and anyone else who's interested can look at it. I'm trying to write like a proper unit test. But I'm not really familiar with the Js contrip project and and the setup there. So it's a little bit ugly at the moment, but I'm trying to
to get something properly, something decent to show you.
**Serkan Ozal** 14:03 Yeah, sure.
Thank you for for all your I mean efforts and
pushing the pushing the things on these
I mean challenging and long. I mean
long term, I mean issue, because I mean, it is really, I mean, because it is not easy to. I mean to find a solution for for such such things. Like the context propagation, because
I mean, it is not, I mean, easy to find a solution that works for every case. So
there will be always cases we need to. We need to handle individually. Yeah.
**Warre Pessers** 14:39 Yeah, I'll I'll definitely continue working on that and and link it as soon as I'm ready. Ready. Or maybe I can share it in in the next
meeting, even if that's if that's better. But right now it's not really finished yet. It's also just some something I'm working on on my personal machine, and I'm right now on my work laptop, so I can show you otherwise
I'd show you what I have until now. But right now that's not not possible, so I'll
I'll get back to you on this as soon as possible.
**Tyler Benson** 15:18 Great?
Or is there anything you need from me, or circan either of you.
**Serkan Ozal** 15:28 No, actually, I mean, there's 1 which is not directly related to the lambda seat. But I just also wanted to mention that. I mean, I have been also working on some kind of side project, which is basically the AI things like, and my target was
providing a kind of AI assistance based on the the open telemetry resources. And then I just started by crawling, indexing, and the the resources for the open telemetry from the open telemetry web pages, the Github and and other things So
I'm planning to to make it available for for everyone as free in
hopefully in September. So I might ask you guys to
to get your initial feedbacks on that just before I mean, I deliver some some basic version of it hopefully, if I will be achieved the the working version of it. So yeah, I will be happy if you I mean once, just before the before the release over the next months
I would be happy to to get your your initial feedbacks like it is like kind of
specialized Llm which is
focusing, which is trained by the by, the open telemetry resources website, Github and other things.
**Tyler Benson** 17:01 Okay.
**Warre Pessers** 17:04 Sounds cool. I'm definitely interested in that.
**Serkan Ozal** 17:10 Yeah, sure. Thank you.
**Tyler Benson** 17:13 Cool.
Have a great day, everyone. I think we can end early and certain you're good to go.
**Serkan Ozal** 17:20 Thank you. Guys. Take care.
**Warre Pessers** 17:22 Yeah. Take care.
