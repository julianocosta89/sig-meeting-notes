SIG: CI/CD SemConv SIG
Date: 2026-10-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:47 Hello?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:01 Hey, can you hear me?
**Christophe Kamphaus** 01:03 Yeah, I can hear you now.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:06 I have to take this call from the room, just FYI.
**Christophe Kamphaus** 01:11 Sure.
I've barely been, I've barely returned home from Observability Summit.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:21 Nice, did you have fun?
**Christophe Kamphaus** 01:23 Yeah, it was really interesting. I spoke to many people, many interesting people.
I managed to network a bit. I think you saw the message from Severin.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:35 Yes, thank you.
**Christophe Kamphaus** 01:36 With him about the infrastructural.
we wanted to do for CICD, and he knew about the one Or the website?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:48 Yeah, that's fantastic.
Well, We'll see how it ends up.
Yeah. I appreciate you making that connection, though. I didn't know anybody else was doing anything.
**Christophe Kamphaus** 02:02 No, as well.
So yeah, it's good if we can, join efforts.
Instead of duplicating the efforts there.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 02:12 Yeah, absolutely.
Absolutely.
And I don't know that we because I I remember when like in the early days, I mean the the project infra SIG we've we've shut down.
But when we used to exist, we were talking about getting Cloudflare and moving to them, but I didn't know we actually ever had the, had that sorted out.
So, yeah, I mean, like, if we can do… because I use my own Cloudflare account for… You know, all the Zero Trust stuff.
To be able to put that collector on the internet safely.
As safely, or as securely as possible, since they're technically not supposed to be open to the internet.
And it works really well, but it's also my own account, so it would be absolutely killer to… Be able to migrate that to their account.
**Christophe Kamphaus** 03:09 Yeah, so if it's an account under the OpenTelemetry organization, that would be great.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:15 Exactly. Exactly.
**Christophe Kamphaus** 03:19 Yeah, happy to have helped, Sam.
Another thing was, I talked with, I cannot pronounce his name, but he's a Rust maintainer.
And, Yeah, I think it just fell through. They had so much load in their SIG, they never saw our PR.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:37 Oh, for the, EMV contacts?
**Christophe Kamphaus** 03:40 Yo.
Yeah, so he reopened it, and he, he said he would take a look.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:47 Sweet.
Cool.
Yeah, that is definitely good.
**Christophe Kamphaus** 04:02 And, we took a picture with Robert and Alan.
And Dawson… Yeah, yeah, Dawson posted it in Slack.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:15 Yeah.
**Christophe Kamphaus** 04:22 And we'll have to get together one of these days. But yeah, it's difficult, I know.
To, come over the ocean.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:33 Huh.
Yep, yep.
**Christophe Kamphaus** 04:38 Yeah, other than that, I found Observability Summit very interesting. I found it more focused than the Observability Day at KubeCon.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:54 Makes sense.
Would you do it again?
**Christophe Kamphaus** 04:59 Yeah, yeah, definitely. Was a very nice experience.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 05:04 Was it like really vendor heavy or was it really open source heavy?
**Christophe Kamphaus** 05:09 It was mostly open source.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 05:11 does.
**Christophe Kamphaus** 05:12 So the talks were really open source.
Some were, like ours, about environment variable propagation.
Others were… there were also several about AI, how to observe it.
Or to give it context, and about security.
But there was nothing really, vendored. Of course, you had the big ones, Datadog.
That has their logo on the slides.
Let's say it didn't sell their products.
They also had some boosters.
And you could talk with some of the big sponsors of the event.
Yeah, it was really nice.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 05:56 Cool.
**Christophe Kamphaus** 06:00 So yeah, I don't have anything else.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 06:10 Alright, yeah, I… the only thing I had was… just gonna update on the infra side of the house, so, you know, I did add… Trustman, and… Mary Leah did.
The chat, because they're the ones who took the proposal to the GC, so… on the.
visualization front, so… Streamlining those efforts, I think, will be good, but I'm waiting for Marilea to get back from, PTO. And then, of course, there's a… The governance, or the TC voting session going on right now as well.
**Christophe Kamphaus** 06:53 Is it for the technical committee or the governing committee?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 06:58 I think it's TC.
**Christophe Kamphaus** 07:02 Maybe it's.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:03 I don't know, I'm really not a fan.
**Christophe Kamphaus** 07:04 soon.
If I remember right, it will start soon.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:11 Yep. So, if Marilee gets re-elected, as an example, then she'll probably maintain Her role in the, as our… liaison.
**Christophe Kamphaus** 07:26 Yeah, so I can imagine that they don't want to take big decisions at the moment.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:31 Yeah, that's what I was thinking. I was thinking the same thing. I was like, I, like, might be a little bit of time, just because of that.
**Christophe Kamphaus** 07:39 Yeah.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:40 But… but we'll see, like, I'd like to see, like, where, I think the first thing for me would be, like, see if I can get onboarded to the Cloudflare account.
so… That's it. That's all I've got.
**Christophe Kamphaus** 07:57 Yeah. Oh, yeah, one other thing. I was talking with some from, Octopus Deploy.
They also run into the issue with long traces.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:10 So…
**Christophe Kamphaus** 08:11 Yeah, so they might join one of these days, but they are Australian, so… The time might be an issue for some.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:21 Yeah.
**Christophe Kamphaus** 08:21 Or if I say my join on Slack.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:24 Oh, that's cool.
people.
**Christophe Kamphaus** 08:27 No?
Yeah, I know that Carlos is still, Looking into it, having some prototypes on his site, but yeah, it's… Everyone needs to find the time to progress on stuff like that.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:42 Yep.
Yeah, it's, it's, it's… I don't know. It's interesting because I guess spam is really just a log with a start… as an event with a start and stop time, but, like, you can also just have an event with a start and stop time.
Yeah.
Like, at some point, it's like… Is it being up in a… I feel like having it show up as a span is more impactful.
But there's such there's such there's such a huge ability to blur the lines. I'm gonna hit a dead zone for a second. So if I drop and disconnect, that's why.
Understood.
There's such a, like, overlap.
the oath.
That it's like… Does it even matter? Would it just be best served as an event? Just submit it as an event if it's gonna be such a long running time?
**Christophe Kamphaus** 09:37 Yeah, I think the special thing with Traces is also they have the Iraq.
The hierarchy?
And you can sample some. But of course, for CICD, There's not that many, so you can keep 100%.
That's also what Octopus Deploy do. They said they keep 100% for deploy SunSun 4, Tool calls a sample more heavily.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:08 Yeah.
**Christophe Kamphaus** 10:09 Hi Carlos.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:10 Trace ID and the sampling is a good call out.
Hey, Carlos.
**Carlos Alberto Cortez (Dash0)** 10:16 Hey, hey.
Sorry, my internet… It has been very wobbly today, so join late.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:26 All good.
**Christophe Kamphaus** 10:26 problem.
I will turn off my video, hopefully, that might help.
**Carlos Alberto Cortez (Dash0)** 10:37 Actually.
**Christophe Kamphaus** 10:37 most.
**Carlos Alberto Cortez (Dash0)** 10:38 Yeah, I… my internet, actually, the problem, I would say, it's not, like, the bandwidth is bad, it's just, like.
The modem had to be restarted because he was acting weird, and… anyway.
But I think it's stable now.
**Christophe Kamphaus** 10:58 Okay, hopefully.
Yeah, I was, talking about my experience at Observability Summit, also About the long-running trace issue.
I was talking with some people there about it.
**Carlos Alberto Cortez (Dash0)** 11:17 Yeah, I saw the photos, Adriel asked, yeah, it would be nice to… if it was recorded, to know whenever it's recorded, it's, available.
**Christophe Kamphaus** 11:27 Yeah, it will be available in one week on the YouTube channel of the CNCF.
**Carlos Alberto Cortez (Dash0)** 11:32 Nice.
**Christophe Kamphaus** 11:35 Yeah, we'll also watch it because you can only be in one session at a time.
**Carlos Alberto Cortez (Dash0)** 11:41 Mmm.
**Christophe Kamphaus** 11:48 Yeah.
Anything else? There is the CLC pull request about VCS bands.
But yeah, I think, Sarah, we need to have the author rebase it.
**Carlos Alberto Cortez (Dash0)** 12:04 Yeah, on that PR, I left a question there.
I don't know whether it was addressed, actually, I don't… I cannot find that. But basically.
The VCS spans this new PR.
cast different set of required and recommended attributes compared to the BCS metrics, you know?
**Christophe Kamphaus** 12:31 You know?
**Carlos Alberto Cortez (Dash0)** 12:33 And I I was wondering whether I think it makes sense that they do match, you know, but I cannot see that. Let me look for that.
**Christophe Kamphaus** 12:39 I have it opened. I can paste it here in chat.
**Carlos Alberto Cortez (Dash0)** 12:44 It.
**Christophe Kamphaus** 12:44 You asked about the REFAT name, if that could be made required. Is that your comment?
**Carlos Alberto Cortez (Dash0)** 12:54 Yeah, I don't know why it's… I can see that it's available, but it wasn't posted.
Wait, I'm gonna post comment. I think… oh, it's there, it's super weird.
No, never mind. Yeah, I just… okay. I think it wasn't posted, but basically, there's, in this attributes list, there's a comment I left just now. It's in the VCS repository name.
This is required.
And in VCS metrics repository name, it's recommended.
And the reason that it's not required is that if you have a fork, it will bring the same repository name.
In contrast, the full… the full address, which will include organization, so you can differentiate between forks, is required for the existing VCS metrics. So I think that these VCS funds, they should do the same.
**Christophe Kamphaus** 13:51 Yeah, we should definitely align there.
And about the REF hat.
I think that needs to be recommended, because you could have Yeah, checkouts, plus on the commit.
**Carlos Alberto Cortez (Dash0)** 14:06 Yep.
Yeah, correct. Yeah, on the head one, I think it's recommended. I think it won't hurt, honestly. I mean, it's experimental, so I would say that since it's experimental, let's go in with things that… Can be useful, we can remove them later, you know?
Like, once it's stable, then that's the time to leave things out. But now, you know, I think it's perfectly fine.
**Christophe Kamphaus** 14:41 Yeah, we'll take a look at, at your comments and, answer.
**Carlos Alberto Cortez (Dash0)** 14:46 Yeah, otherwise, it looks… it looks fine, I think. It's a very small prototype, sorry, it's very small PR itself, it's only basically two new spans.
Yeah.
Yeah, true. Yep.
Right.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 15:12 I did post that link with a side note on y'all's thread. Because there was there's been an open issue for the GitHub receiver about how Q spans are represented.
And I…
**Carlos Alberto Cortez (Dash0)** 15:25 correct.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 15:25 Kind of skim the message there.
So I was like, well, you know, he, like, he has a pretty decent, I think, argument, with regards to why the QSPAN should be represented differently than they are today.
In there, from an analysis perspective.
But since y'all were talking about different types of spans that are Not necessarily the CICD span, but, like, kind of… I figured, like, that might be extra context, and also, like, I figured, like, y'all might have some insight on, like, whether or not you agree or disagree with, like, some of the arguments that were made in that thread, so… Jared, I'm sorry.
**Carlos Alberto Cortez (Dash0)** 16:02 Can I share my screen?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 16:05 Sure, I'm driving, but yeah, share your screen.
**Carlos Alberto Cortez (Dash0)** 16:08 Or you want to share? Because, okay, I will share quickly. Yeah, this is the one I wanted to talk about. This is a spinoff.
issue from the one you posted. The model change, you know.
The model changed, so basically you have the job, and then as children, you have the queue, the span, plus the actual subtasks.
But this person has been discussing about probably introducing a slightly different approach.
Which is, like, Q stays… like a child span, but then this setup on the every, every task or subtask.
Instead of being a direct child of Job 1 span, it's, it goes under exec job 1 span, for example.
And you have been discussing with him. It's a long discussion, by the way, but I wonder what's your feeling. I think you're explaining, this makes sense, I agree with this, I think that execution can be derived.
And then he went on explaining, like, some… at the same time, some technical limitations. I don't know, what's your feeling?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 17:18 I haven't fully… Brock, his last response.
I… so I do have a working dashboard query prototype that I can send later in, like, a DM.
For… from the CICD spans that we get from OpenTelemetry community currently, that may provide some additional insight.
But I'm just not entirely sure. We originally had two spans being a child of the job span itself.
And if I remember correctly, we purposefully — it did not align with the way that child-sibling relationships were supposed to work. And so an issue had been opened up, and so we changed it.
**Carlos Alberto Cortez (Dash0)** 18:06 Yep.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 18:06 that kind of proposal seems like it goes a little bit back, but also, I think, like.
I'm like wondering if this is a GitHub issue versus how much of this is a CICD.
**Carlos Alberto Cortez (Dash0)** 18:20 Yeah, yeah, correct, yeah, yeah, correct. Yeah, this is what you're… This is… this is how it's now, right?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 18:32 Yes.
**Carlos Alberto Cortez (Dash0)** 18:33 Right, yeah, okay.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 18:37 I definitely, like, have… screenshots. I can even, like, send you the link, to the dashboard, to the traces, if you want. I can do it within this group, in terms of access, it just has to be on the deal.
**Carlos Alberto Cortez (Dash0)** 18:52 Yeah, it could be nice, because, yeah, some, potential, user, of, was talking to us, and he mentioned about this, he's like.
Is this, like… is this going to stay like this, or should change?
And I said, well, you know, we are still experimental, but this is technically not covered, but it should be fine, etc.
But we are we can discuss a little bit more on that one.
But yeah, as you said yourself, I think it's.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 19:21 Yeah.
**Carlos Alberto Cortez (Dash0)** 19:22 Wolfgang GitHub.
I think more than CACD.
**Christophe Kamphaus** 19:28 Yeah, so… the queuing… It's also a concept in pretty much any CICD system.
Alan also said it's a case for Argo workflows.
in Jenkins, it can also queue before it executes, especially if it's its own Agent being provisioned for a given task.
So I think it makes sense to consider it.
It would also align with the metrics we have. We have task duration, okay.
maybe I'm getting ahead of myself. We have the duration metrics, do we have it Just for pipelines.
Or also for tasks.
Because I know that we had.
See face… As an attribute, so queuing, executing, and finalizing.
**Carlos Alberto Cortez (Dash0)** 20:27 Okay.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 20:28 I don't know if we have it called out explicitly, but since it's span… like, it's just span duration. Right. I mean, we should probably call it out.
I felt like we did have like duration by attribute. Maybe I'm misremembering.
**Christophe Kamphaus** 20:46 Oh.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 20:46 I see.
**Christophe Kamphaus** 20:48 I opened it. It's just for the pipeline run. So we didn't define it for task runs.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 20:55 Sorry.
Yeah.
I still… I still gotta think about… His particular message on here, but, like, all those durations I can calculate now.
As far as I can tell from the argument that's being made.
Cool.
But maybe there is one specific nuance where that's not the case, and that might be just what I'm missing from where where I last read the message. So I will go back and certainly, like, revisit that, and I can send, just like between us, I can send, like, the actual spans and, like, give you access to them if you want to try and look through this stuff as well.
**Carlos Alberto Cortez (Dash0)** 21:41 Yeah, yeah.
I think that makes sense, yeah. Yeah. But it's… okay, it's good to know that this current model is the one, and we are… and yeah, I can say that we are exploring this new one, but no, like, this is the recommended one for now.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 21:58 Yeah, and the other thing, too, is, like, the Q stuff is not… something that is given to you by GitHub.
From their events, right?
Like, it's very, like.
there's a method to the madness in which it was implemented because of the amount of data that you get from GitHub, and the data types that you get from data, from GitHub.
**Carlos Alberto Cortez (Dash0)** 22:27 Gotcha.
Okay.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 22:31 Sorry, go ahead.
**Carlos Alberto Cortez (Dash0)** 22:32 Yeah, I sort of, that… Some people try to extrapolate that by comparing started at versus created at. I don't know if that's actually the queue time.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 22:46 Yes.
That is. I'm pretty sure that's how it's calculated in there. And GitHub can do… I might hit it, so if I break, that's why.
it's the last one on my journey, hopefully. But, GitHub can also give you, like.
negative wrong values in cases that you have to account for that can… like, there were bugs in there, because there was, like, sometimes you could get, like, a negative one, or… or have, like, the started at time be after the created at.
or before the created at time, one of the two, something like that, and it would create these spans that looked like they were 24 hours because of how the spans were created. Like, there's really wild bugs on the event side, actually, just in general in GitHub, that can cause issues with, like, span representation.
So, yeah, I mean, like, those have been fixed, but… And it and it may still be able to like we might still be able to calculate the Q in a different way.
**Carlos Alberto Cortez (Dash0)** 23:50 Yeah, yeah, yeah. Okay, that makes sense. Yeah, yeah, it's like… No.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 23:55 Sorry.
**Carlos Alberto Cortez (Dash0)** 23:57 Yeah, there's… there's an issue that I saw regarding that. When you re-trigger a job.
If, for a short period of time, created at is updated, what it started as is not.
So, you get this, like, weird situation where created is after started at… And then it's corrected later. I don't know if that still exists, but I was going through that. So yeah, I think that this kind of, When you have to consume this kind of stuff, you have to be super, on, like, on the safe side, you know, trying to double-check everything, yeah.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 24:37 Yeah. I really wish they'd just let me, like.
Randall P.
or worked with us to instrument the runners natively, and then just said, hey, you know, just like, here you go, it's all free. Like, OTLP endpoint, if you enable it, great. And, like, our hosted runners will send you OTLP data. But, alas, they, did not.
**Carlos Alberto Cortez (Dash0)** 24:58 Yeah, right.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 24:59 Here we are.
**Carlos Alberto Cortez (Dash0)** 25:01 Here we are.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 25:03 And I don't think they ever will, like, honestly. I hear they use it internally, but every… every effort that has been made to try to have that.
Communication happen has, not worked out.
In person, remote.
It's not worked out, so…
**Carlos Alberto Cortez (Dash0)** 25:24 Okay.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 25:25 what it is.
**Carlos Alberto Cortez (Dash0)** 25:27 Yeah, but in the meantime, we need people who want to use this, so… We have to, yeah.
To try to help.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 25:38 Yeah, exactly, exactly. So we gotta do what we gotta do. And I mean, we do have a lot of users of, actually, this receiver. We use it for… Thousands of repositories and actions.
at my current job, there's another place that… there's actually at least, I think, two other companies that leverage it. pretty heavily that, like, I had a hand in, and then there's, like, just various different adopters in the industry that use it. So it is widely used, but that means, like, we're on the deck for support, yeah.
But some of these issues that people are bringing, like… Wow. I'm impressed, because they think deeply about this stuff, and I appreciate that. It makes it better. But it also means it's a lot to grok mentally. It's like, whoa.
**Carlos Alberto Cortez (Dash0)** 26:22 Yeah, absolutely, yeah.
Okay, very good. Thank you so much for the feedback. Yeah, I think I will, yeah. Yeah, I'm looking forward to, the prototypes, or whatever you have, you know, just for continuing the conversation.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 26:37 Sure. When I get back to the computer this afternoon, I will send you a link to the spans and stuff, and give you access to the analysis backend.
**Carlos Alberto Cortez (Dash0)** 26:47 Great, thanks so much.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 26:50 Thank you.
**Christophe Kamphaus** 26:53 Yeah, thank you both.
Anything else or can we cut it short here?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 27:03 I'm good to go.
**Christophe Kamphaus** 27:04 Then have a nice afternoon and see you next week.
**Carlos Alberto Cortez (Dash0)** 27:08 Perfect, thank you so much.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 27:10 Thanks. Take care.
**Christophe Kamphaus** 27:11 I bought…
