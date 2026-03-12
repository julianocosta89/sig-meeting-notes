SIG: Go SIG
Date: 2025-12-11
Duration: 15 minutes
Zoom Recording URL: https://zoom.us/rec/share/vMmHKCP4nhLYd1KXEDc5Aaw0WbCgxDwRyDlH6Z8VfRXJM2QKk9x6ZIfNxCm6-vGi.4VMdvaHlELd74OhO
============================================================

## Zoom Recording Transcript

**Tyler** 00:52 Hey, Damien.
**Damien Mathieu** 00:57 Hey, good morning.
**Tyler** 01:01 How's it going?
**Damien Mathieu** 01:03 Good, how are you?
**Tyler** 01:05 Doing well.
How's the, evening treating you?
**Damien Mathieu** 01:11 Okay, yeah, okay.
**Tyler** 01:15 Ready to log off, is what I'm hearing?
**Damien Mathieu** 01:20 just, like, as every end of day, I suppose, which doesn't mean I'm not happy to be here. And I'm saying that also because this meeting is recorded.
**Tyler** 01:31 The only person who watches them is Robert, so it's okay.
**Pellared** 01:36 I even stopped watching. I started to just give transcripts to Jed AI and make a summary.
I watch if there's something interesting sometimes.
**Tyler** 01:50 Yeah. Essentially, if we gave the SIG meeting in sign language, then GenAI would not have any idea what we're doing, then.
That's always, like, one of those things I wish that, like.
you guys in Europe always have, like, second languages. You know, I'm speaking to two people with second languages, right? But I'm always, like, I wish, especially in the United States, we kept, like, sign language as, like, a second language, which used to be, like, the thing, like, the pioneer days. I was like, such a great… Great way to communicate over, like, vast distances, or in, like, crowded rooms or something like that. It's like, yeah.
Cool. Well, I'm looking at the agenda, I don't have anything, I don't know if you all have things you wanted to add there, but if you, Do go ahead, and if you also haven't yet, please go ahead and name to the attendees list.
And we can wait a little bit here.
So next week is gonna be our, last, SIG meeting of the year. I guess this is our last EU-friendly SIG meeting of the year.
So… Just maybe on that note, like.
Are there any, like, bookkeeping items we need to keep in mind? I mean, we just did a release, last week? Or this week?
I don't know, time's flying. And recently, and so… yeah, okay, this week, yeah.
Yeah, yeah, it was Monday.
So I don't think we need one of those. We could probably, I think, maybe start off the year with maybe a goal review, from, like, what we had put out last year, and then… I think maybe the second meeting of the year, I'd love to get, like, a, what are we gonna accomplish this year sort of thing, so I'd love to do another publish in January of, of, like, what the SIG goals are and that kind of thing, so, yeah.
So, yeah, I guess maybe, spend the rest of the year reflecting. Seems like a lot of time to do reflections, but… But yeah, I think that's kind of, like, the only bookkeeping things I can think of right now.
David, I saw you merged your, optimization for the histogram, metric histogram stuff. Are you gonna try and merge, some other PRs for optimizations of, like, the counters and things? Or.
**David Ashpole (dashpole)** 04:38 Yeah, so I'm working on… I actually added it to the agenda, but I can talk about it now. I'm working on the last value.
optimization. And the one that's ready for review, if people have time, is the… is the histogram exemplar reservoir one. That one is actually, I think, a pretty straightforward review.
And… Yeah.
**Tyler** 05:08 It is. I totally forgot that you asked me to.
**David Ashpole (dashpole)** 05:11 I now, actually, now that the histogram one is the other histogram PR is merged, I can now rerun the benchmarks and show the impact on collect, which I'm actually kind of curious to see. Like, obviously it will improve, but… How much I think will be.
Interesting.
**Tyler** 05:34 Yeah, I'd love to see that. I, I'm overdue for reviewing this.
I was just gonna go approve it, but I saw I had an outstanding comment.
Yeah, okay.
I can… I can take a look at the… that one, for sure, at the end of this meeting. I have been… Meaning to get to it, I just totally forgot about it. And then the, the last value one, is that ready to review right now?
**David Ashpole (dashpole)** 06:03 Not yet. I'm, like, halfway through rebasing it. I rebased it, and now I need to adapt. We made some, like, tiny changes to functions in the atomic.go file.
In history, yeah. So… It should be, like, super straightforward compared to the histogram one.
**Tyler** 06:21 Yeah, right.
**David Ashpole (dashpole)** 06:22 And then last will be the exponential histogram, which… I'm not expecting to merge until, like.
I'll be happy if it merges by February, I'll put it that way.
**Tyler** 06:34 Yeah, I mean, yeah, I think that, like.
I think this is probably worth… A blog post in itself, by the way, just, like, all the performance improvements.
That we've been doing here, so, like…
**David Ashpole (dashpole)** 06:48 I do think that, like, that will culminate in something that we can actually, like.
**Tyler** 06:51 maybe, maybe announce as well, because I think that was, like, we definitely got a lot of, you know.
I don't know if you call it marketing, for, like, the Prometheus versus, OTEL stuff, so this is… this would be a cool, I think, conversation piece at this point.
**David Ashpole (dashpole)** 07:06 Yep.
**Damien Mathieu** 07:06 And it's, like, performance in metrics is definitely one of the top reasons for new issues.
**David Ashpole (dashpole)** 07:16 Yeah, yeah, I was doing the math, and like, in the worst-case scenarios, this makes performance about 30x better.
Or best case, I suppose, for the performance improvement. So it's… they're pretty substantial.
**Tyler** 07:30 Yeah, absolutely, yeah.
I am glad that we're able to get these in, because, like, there was always, like, in the back burner that we should do something like this.
We said in theory we were able to do it, but I am glad that you've been able to tackle it and make it actually happen, because, like, it was always, like, maybe, like, a 80% confidence interval, so… Yeah, I'm happy we're able to do this, so, yeah.
**David Ashpole (dashpole)** 07:51 I'm actually glad that we got a release out with just the counter changes, because if there are any issues, hopefully we'll catch them before the histogram and exponential histogram and all that stuff actually goes out.
**Tyler** 08:04 Yeah, yeah, good point.
Good point.
**David Ashpole (dashpole)** 08:07 So, I won't write the blog post still.
Till, definitely till we've got, like, everything out and have resolved any, like, issues that come up, if any do.
**Tyler** 08:18 Yeah, that's a good point, yeah.
Cool. I am looking back at the agenda, it looks like… I'm guessing, Robert, maybe you had KubeCon EU talks?
**Pellared** 08:29 Yeah, I just want to say that I got a notification about that my talk has been approved. I'm not sure if anyone has posted some proposals. Damien, what about you? Have you published any proposals?
**Damien Mathieu** 08:39 No, I was not approved.
**Pellared** 08:41 Okay.
I hope you still come.
**Damien Mathieu** 08:46 I hope to, it's, I mean, let's, I guess I haven't said it to this group, but I will also be going on paternity leave, around May 1st.
And QCon is going to be the end of a pregnancy, towards that, so it will really depend on that.
**Pellared** 09:07 I see, yeah.
It's hard.
**Tyler** 09:13 Yeah, definitely, hard… prioritized family, right? So, that makes sense.
**Pellared** 09:18 Exactly.
**Damien Mathieu** 09:19 So, yeah, I'll be… I'll be off, from May to September.
**Tyler** 09:25 Okay.
Yeah, thanks, good for a heads up on that one. Yeah, love to plan accordingly.
**Pellared** 09:33 Autel HTTP, Damien, is there anything needed?
I just can see from my side.
I mean, I mean… I just want to quickly tell you one thing, which I think is also kind of a blocker, this error handling, and, you know, how to handle errors. We had a longer discussion during last logistic meeting.
So, probably, we are thinking about… if there's an error which is terminating the span.
So, all of us think that using this record error, or e-record exception in other languages, It's unnecessary bloat.
And basically, just using… adding the spend attributes is good enough.
There was also a question if we should not emit a log record, or some event.
But then the conclusion was that if some… it's still a redundant thing, because it's already in spam, and if someone would like to have it as the event or lock, or whatever, he can always make a… a span processor, which captures spans which have error, and these attributes, and just emit, you know, logs based on these, on these spans.
If there's… if someone really needs it badly for any reason.
So, probably we'll work with Ludomi Watrask, on, on this.
Probably in January, because right now it's, you know.
**Damien Mathieu** 10:56 Yeah, that makes sense, I think. Thanks. There are a couple other issues before we stabilize. They are written down in the audit hotel HTTP API, issue. A bunch of them have been tackled, with this last issue and deprecations removed.
There are still some things that need to be taken care of.
I actually intend to, take a closer look at the issue either tomorrow or next week, so…
**Pellared** 11:31 Like, specification or semantic convention, why there's nothing more than this one, right?
**Damien Mathieu** 11:35 No, semantic convention-wise, it's only this one.
**Pellared** 11:39 Okay.
**Tyler** 11:47 Well, cool.
Yeah, definitely enough. I think we got plenty of time to shore up.
stabilizing the OTAL HTTP before you're out of here, Damien, so hopefully we get that done, but… Yeah, I know, right. So you say that now, and then things fly really fast, but yeah.
**Damien Mathieu** 12:04 Yeah, last thing she said.
**Tyler** 12:08 Yeah, exactly.
Well, cool.
Looks like that's all we have written down. Any other topics people want to talk about? Otherwise, we can probably end the meeting early.
Well, excellent. It's good seeing y'all. For those…
**Damien Mathieu** 12:27 And…
**Tyler** 12:27 In Europe?
**Damien Mathieu** 12:29 See you next year.
**Tyler** 12:30 Yeah, see you next year. Bye.
**David Ashpole (dashpole)** 12:36 Bye, everyone.
