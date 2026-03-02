SIG: Go SIG
Date: 2025-10-16
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 05:01 Hey, Damien.
**Damien Mathieu** 05:07 Hey, good morning.
**Tyler Yahn** 05:09 Morning.
Good evening to you.
How are you?
Good.
**Damien Mathieu** 05:15 Good, too.
**Tyler Yahn** 05:19 How's the, the weather over there in, France these days?
**Damien Mathieu** 05:23 It feels like, it's still, like, June.
**Tyler Yahn** 05:27 Really?
**Damien Mathieu** 05:30 Yeah, it's… it's surprising hot still.
**Tyler Yahn** 05:34 Yeah, it's definitely cooling down over here.
But, yeah. Are you… where… you said you're in the Pyrenees area, right?
**Damien Mathieu** 05:41 Just north of the Pyrenees, yes.
**Tyler Yahn** 05:43 Hmm.
Okay, yeah.
Yeah, well, that's interesting. I didn't… I didn't expect it to stay warm that long, but yeah.
**Damien Mathieu** 05:52 I mean, we are not in the mountain either, like, we're north, but it's, like, 2 hours by car, so…
**Tyler Yahn** 05:57 Yeah, man.
Yeah.
the… I'm guessing the sun is still, coming up later and later, though, right? Like, I guess you're kind of south, right? Yes.
**Damien Mathieu** 06:09 Yeah, we are… yes, we're south compared to other places, obviously, but you're always south compared to other places, but
Yeah, the sun is, is, getting up later, and.
**Tyler Yahn** 06:25 That was definitely something I noticed, like, you go to, like, California, or, like, Southern California especially, like, compared to up here in Portland, Oregon, or even Seattle, like, it's just, like.
you know, the sun always sets at, like, 7pm, like, no matter what. It's just, like, it's so nice compared to, you know, here, where all of a sudden it's going, you know, 5 o'clock at night, it's dark, and you're like, ugh, this is horrible, like…
I mean, Alaska's gotta be even worse, right? Like, you got…
**Damien Mathieu** 06:50 Yes, exactly.
**Tyler Yahn** 06:51 Let's go.
**Damien Mathieu** 06:53 percent is off in March.
**Tyler Yahn** 06:55 Yeah.
It's quite, quite a night, yeah.
I don't know.
Hey, Brian.
**Bryan Boreham** 07:06 Aye.
**Tyler Yahn** 07:08 How's it going?
**Bryan Boreham** 07:10 Oh, pretty good.
Yeah, just… doing everything at once.
**Tyler Yahn** 07:17 Yeah, see, Brian's up there in London. I'm sure his days are becoming much shorter, at this point, yeah.
**Bryan Boreham** 07:23 Yeah, it's… gets dark about 6 now, I think.
**Tyler Yahn** 07:27 Yeah.
**Bryan Boreham** 07:27 And the clocks are gonna change in a… in a week.
**Tyler Yahn** 07:31 Yep, yeah, we were first week in November here, and yeah, that's always a shocker, but the spring one's even more of a shocker, so…
Well, okay, I guess I'm looking at the, agenda. Okay, there's David.
I don't see Robert, I don't know if he's gonna make it, I can't remember.
**David Ashpole (dashpole)** 07:54 Hey, hey.
**Tyler Yahn** 07:55 He's gonna make it today.
**David Ashpole (dashpole)** 07:56 Hey!
**Tyler Yahn** 07:57 But we could probably get started in here in just a second. If you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you want to talk about.
Please go ahead and add them there, and I'll start sharing my screen.
Cool. Alright, alright, so to start us off, Damien, you want to talk about the hotel gen context, reversal in DataRace?
**Damien Mathieu** 08:31 Yes, so there's this PR which started with an issue. Basically what's happening is, because the context is stored within, the request, well, for JIN, it's stored within the JIN struct.
We need to revert it after the middleware has executed, so that, parent middlewares do not get the span, within the context.
But that also means that basically what this person is trying to do is they spawn a Go routine that runs after the request has finished running, and they would like the request, the context to have a span, obviously, because for that point of view, they are still within,
that context. And so the problem is that, we need to revert, because the parent middleware should definitely not have a span, and they would like to have that span, in that goutine. I'm not sure we can do both, not without
major changes in how contexts are handled in HTTP requests in AutelGene and maybe in HTTP.
So I just wanted to bring that up. I think our current behavior is the right one anyway, if we have to only have one.
**Tyler Yahn** 09:56 Yeah, I agree. Why wouldn't they, in their spawned Go routine, pass in the values that they need? Like, the span.
**Damien Mathieu** 10:03 They… yeah, they can pass the current context, so that we… we keep… we keep it.
That's institution.
**Tyler Yahn** 10:12 I mean, I think that's…
Yeah, that seems like the right solution, right? Like, if you want something in the spawn to take a…
**Damien Mathieu** 10:19 I agree.
**Tyler Yahn** 10:19 Yeah.
**Damien Mathieu** 10:21 I mean, I… it's… I think it all comes down to, a flow in the design of how HTTP requests pass the context, probably because context was, set up after, the API was stabilized.
But having the context in… within the HTTP request is also, like, how this breaks.
**Tyler Yahn** 10:46 Yeah, right, yeah, that makes sense.
Wow, there's a lot going on here.
**Damien Mathieu** 10:54 Yeah, it's, like, that person is very,
chatty when they post comments.
**Tyler Yahn** 11:02 Okay.
Is this something that you can respond to, and just kind of…
**Damien Mathieu** 11:08 I can, I can respond to this. I just kind of, said to them that it would be something that would be nice to bring synchronously, to gather feedback. I see they're not here, here today. So I brought it here, for discussion, but I think,
Passing the context directly to the goutine is a better pattern, I agree.
And I can definitely answer to that.
**Tyler Yahn** 11:35 Yeah, and I mean, I also think that, like, especially for, like, asynchronous things, like, there's also,
the pretty common pattern in OpenTelemetry where, like, you'll link the spans, actually, you won't even make them, like, a child reference for that exact reason, but…
I don't know why…
**Damien Mathieu** 11:53 I mean, it really depends what you're doing, I think.
**Tyler Yahn** 11:56 100%, yeah, yeah, yeah, exactly. So, yeah, I mean, I think there's a lot of other options here, assuming that, like.
an asynchronous context is going to hold an active span for something that may have completely already ended, like, that's… I don't… I mean, I think you can do that.
Man, that's such a bad idea, though. Because, like, even if you.
**Damien Mathieu** 12:16 gas.
**Tyler Yahn** 12:16 Context, like, yeah, like, it's just, yeah.
**Damien Mathieu** 12:18 Actually, you know what? I know what I'll do. The collector actually does exactly that, which is that it gets the context from the HTTP requests, and then the HTTP request ends, and the processors and exporters keep running.
And we keep the same context, because we pass the context directly outside of the HTTP request. So I'll just mention that maybe their coroutine should just follow that pattern, and we have one pattern that… where it works, that can be displayed.
**Tyler Yahn** 12:47 Yeah, I think that's a great idea, then, if you have… you have something… I mean, that sounds exactly applicable here, so, yeah.
**Damien Mathieu** 12:53 Yep. Cool.
**Tyler Yahn** 12:55 Okay, cool. Alright, well, we'll let you respond to that one. Thanks, Damien, for taking care of that.
I see also FLC… I feel really bad, because I don't think FLC is actually how you say their name, but anyways…
FLC's, got an issue here also with HotelGinn,
Using middleware causes temporary multi-part forms to not be destroyed?
**Damien Mathieu** 13:20 So this is actually, this has been discussed, heavily for quite some time.
I think there's, yeah, both pull requests and issues coming up.
Basically, I think this solution is to manually…
Delete the data if we see there is some…
**Tyler Yahn** 13:44 Wow. Manually delete the data?
I see, so if, like…
**Damien Mathieu** 13:52 If you look at the, the decks tab, it has a solution, a solution.
**Tyler Yahn** 14:01 Yeah… This is starting to sound familiar now.
Do this, is what you're saying?
**Damien Mathieu** 14:21 Yep.
**Tyler Yahn** 14:22 Yeah.
Okay.
I see there's also some Go issues.
Yeah, and Go's pretty much saying, make your own judgment.
**Damien Mathieu** 14:40 I think, Sean may have committed, commented in one of those PRs or issues.
**Tyler Yahn** 14:48 Yeah, basically.
**Damien Mathieu** 14:48 Yes, this is the way.
**Tyler Yahn** 14:50 Oh, really? Okay, let's take a look.
Yeah, probably not this one.
**Damien Mathieu** 15:05 No, maybe not.
**Tyler Yahn** 15:07 Maybe just this issue, then.
I think, can't remember his name, H something? Act… Tonya.
Oh, actually… Yeah, I wonder if this has been updated.
Okay, no, sorry.
Well, okay.
I mean, I… what you're suggesting, I think, seems right. Is there a reason why this got blocked, Damien? It obviously, like, there were some context issues, it sounds like?
Wow, there's a lot more going on here.
I mean, I… yeah, so, like, this seems like a proposal that is matching what you're… you're recommending as well, right? So, like, this seems reasonable to me.
**Damien Mathieu** 16:01 I mean, I'm not recommending anything, I just say that this is the solution that has been recommended so far.
**Tyler Yahn** 16:08 I see, okay, gotcha.
Who's the owner of Jin? Is that.
**Damien Mathieu** 16:19 I think that's FLC, and maybe Alex Catz, as well.
**Tyler Yahn** 16:24 Yeah, Alex guessed.
Yeah, I mean, I don't have a strong preference. I mean, I think that that seems reasonable,
Obviously, I think that may, like, step on some toes as well, but…
I mean, I think as long as it's documented in the behavior of the, the instrumentation, like, I don't see why that's not a viable solution, so I would probably just defer to the,
The owner's here.
Yeah, I mean, do we want to try to get this PR progressed? Is that kind of like the,
the end goal of this.
**Damien Mathieu** 17:09 I think that's the ask.
**Tyler Yahn** 17:11 Okay.
**Bryan Boreham** 17:15 Can I just… what is the situation in which we start off With a multi-part form.
How do we get here?
**Damien Mathieu** 17:29 It's… so we do not use multipart form. This is for folks using it, and it's because we clone the request, and so after cloning the request, the multipart form is not, duplicated.
And so, remove all that may happen elsewhere. That does not happen anymore.
**Bryan Boreham** 17:52 Right. And what's an instance where somebody Starts using multi-part request.
**Damien Mathieu** 17:59 for phytoplood.
**Bryan Boreham** 18:04 What's that got to do with OpenTelemetry?
**Damien Mathieu** 18:07 If you want telemetry on file upload.
**Bryan Boreham** 18:12 Oh, we're… we're trying to instrument file uploads.
**Tyler Yahn** 18:17 The whole… the whole request, yeah.
**Damien Mathieu** 18:18 Yes.
**Bryan Boreham** 18:19 Okay.
**Damien Mathieu** 18:19 We're instrumenting the HTTP server.
**Bryan Boreham** 18:24 Okay.
Thank you.
**Tyler Yahn** 18:33 I see, yeah.
Okay.
Yeah, I mean, this is… the temporary file is not destroyed. Can be, that seems problematic.
**Damien Mathieu** 18:51 Yeah, I think it's also something that may exist with other instrumentation HTTP.
**Tyler Yahn** 19:00 Yeah, I think you're right, yeah.
**Damien Mathieu** 19:02 At least Echo for sure, maybe not HTTP.
**Tyler Yahn** 19:08 Yeah, yeah, right.
Yeah, I mean, I like all the options that, FLCs
put out here. I mean, I think maybe there's a, a configuration included? What the default is, I think, is… is…
Think up for question?
I think that if we're removing this, that, you know, it cleans up our code, or it cleans… allows the file to get cleaned up, I think that makes sense. Because then we're not hanging on to things. Maybe, I don't know, maybe there's just gonna conflict with the user who wants to not…
They want to do this manually at some stage in their, middleware, so…
They would want to try to configure this, but… Yeah.
Yeah, I guess that's kind of another question, is like, If the user is…
Is this something that's coming from us, Damien? Like, you're saying that, like, we're causing this because, like, we're hanging the context as we're cloning the request?
**Damien Mathieu** 20:10 Yes.
**Tyler Yahn** 20:12 Yeah, okay, so that's not really, like, it's up to the user to decide, like, we have to make some sort of decision here to help facilitate.
**Damien Mathieu** 20:18 I mean, we could… we could have an option that says do not delete, the multiple files,
But I would, if we change this, I would start by not having that option, and then adding it if someone thinks we should add it.
**Tyler Yahn** 20:35 God, man.
**Damien Mathieu** 20:35 I'm not sure anyone would… I don't see why someone would prefer to do this on their own.
**Tyler Yahn** 20:44 I… yeah, I agree.
**Damien Mathieu** 21:16 Or maybe this is, like, the XKCD, where you fix a bug with the fan going up, and someone had something that, they detected, and maybe they detect, their file system not having any space anymore as a proper behavior.
**Tyler Yahn** 21:32 Shift. Yeah.
gotta… gotta… that's really annoying, gotta pick up your hand from the keyboard. Yeah, totally.
I…
Almost certainly that's going to happen, right? It's just in a matter of time before, yeah. So, I think that that's worth…
I like the idea, yeah. I'm also… I wonder if we're…
we should be working on this at all. I don't know if we should be owning this, but…
We have owners, so it is what it is.
Okay, cool. Alright, so moving on.
I want to do a milestone check-in, but, I think maybe we can…
touch on that at the end, so I'm just gonna move this lower. Damien, jumping back to you, you wanted to check in with long-seen code owners triageers?
**Damien Mathieu** 22:27 Yes, actually, I've, I've started already, because I've noticed in, while seeing another issue that, Chengzhen, Scorpion Knives, who is a triager, and code owner for,
the Hotel Zap, I think, or another one, as well as Hotel Echo, and for the record, he is the only owner for Hotel Echo, and he does not have any gita activity since last February.
So I pinged him on Slack today, and we… he has been pinged on at least one pull request, recently,
So, yeah. So we may have to deal with lack of code owners on Hotel Echo.
In the near future.
**Tyler Yahn** 23:20 Okay. So there's been no resp… like, you've reached out to them in Slack, and there's been no response?
**Damien Mathieu** 23:24 I mean, I reached out to him in Slack today, so…
**Tyler Yahn** 23:28 Oh, okay, okay.
**Damien Mathieu** 23:29 I'll wait for at least a couple weeks.
**Tyler Yahn** 23:35 I can't remember what it was exactly, yeah.
**Damien Mathieu** 23:37 I think it's an F rather than a V, but yeah.
**Tyler Yahn** 23:51 Okay, yeah, I mean, I… that sounds good. Obviously, if they're inactive, that we need to…
Clean that up, but, it… yeah.
February's.
**Damien Mathieu** 24:02 I mean, I think, even if they say they are active in a telgo, which, I don't know, maybe they would be answering on that pull request, I think we should remove them to Emeritus for treasure, because they are definitely not active in the overall project.
**Tyler Yahn** 24:20 Yeah.
I mean, I… that sounds good, as long as there's no immediate response saying, like, oh, I'm sorry, I just missed it, or, you know.
**Damien Mathieu** 24:28 Damn.
**Tyler Yahn** 24:29 So…
**Damien Mathieu** 24:29 Of course, of course.
**Tyler Yahn** 24:31 Yeah.
But yeah, seems reasonable to me.
Sounds good.
Okay, Robert, next up he wanted to talk about, this PR.
**Robert Pająk** 24:50 I think the only thing which I wanted to talk about is that, I have addressed, Heather, your comments, but I'm… so, basically, do you think,
But… and I just want to double-check, because I know that you are very occupied right now, so just maybe… just, not sure if we need to wait for your review, or is it enough if we just… someone else will step in and make a, you know, second approval?
Or do you want to review it yourself?
**Tyler Yahn** 25:22 I mean, I am always able to…
submit another PR if I… if I feel it necessary.
So no, I don't think you should block the project on me.
**Robert Pająk** 25:33 Yeah, that's…
**Tyler Yahn** 25:34 Yeah, I definitely think if other people have time to take a look at this, I can, I can, again, I can try to take a look at this, it keeps…
Fallen off my priority queue. But, I mean, I'm… I'm looking at… The algorithm looks…
Like, it hasn't, yeah, this…
Obviously, there's a lot of details here, but I can see, like, the bigger structure, it is following what you… we were talking about before, where it's a single-pass algorithm that's doing these parsing,
This is interesting.
Yeah, so I mean, maybe there's some… yeah, this may need… okay.
I can take another look, hopefully in the next few days. But obviously, if other people have time to take a look, I think that they should take a look.
Are we trying… we are trying to get this in this milestone, right?
**Robert Pająk** 26:27 Yeah, I think it's important to, you know, basically avoid risk consciousness.
**David Ashpole (dashpole)** 26:31 I will take a pass.
**Robert Pająk** 26:34 Okay. Thanks.
**Tyler Yahn** 26:39 Okay, cool. There's another thing I wanted to talk about that I didn't add to the agenda, but, since we're on this point, it's also about this milestone. So, David's PR is about, optimizations.
for the metrics SDK, I want to take a look at these as well.
**David Ashpole (dashpole)** 26:59 The histogram reservoir one is now pretty trivial.
Because, fixing the race… so, fixing the race condition… Made it.
It's performance worse, and made it equivalent to just using a lock.
So, it's now… Extremely simple. Move the lock from…
one lock for the whole reservoir to now one lock per measurement, and you get a 3X perform… or 4x performance improvement.
So this is now much simpler, and I think… Probably anybody could review.
Most of the code changes, I think, are just the added testing for concurrent safety.
**Tyler Yahn** 27:42 Okay.
**David Ashpole (dashpole)** 27:44 Yeah.
Hopefully, we can at least get this in. The other… the histogram one is certainly a harder PR to review, and I can… if it's necessary, I can try and split that up.
**Tyler Yahn** 28:00 Yeah, I haven't… it seems pretty close last time I was looking at this, if I'm not mistaken.
**David Ashpole (dashpole)** 28:09 Yeah, I mean… I think I've resolved all the outstanding comments. It's mostly about, whether others are
Comfortable reviewing it in this state.
**Tyler Yahn** 28:23 Yeah, this is another one where I just haven't gotten back to reviewing it, but I… I agree. I'd really like to get this one in as well. This is a pretty significant improvement, if I remember correctly, right? Like, yeah, 2X, yeah.
I'm gonna add it to the milestone.
**David Ashpole (dashpole)** 28:39 Okay.
**Tyler Yahn** 28:39 And I… yeah, if folks on the call have time, please…
Take a look at this one,
I wonder if there's any things I haven't… Yeah, actually.
Yeah, I mean, I can take another look. Obviously, like, this is, I think, the bulk of it in here.
But it's pretty straightforward, if you've taken a look at the SUM implementation, which I think, like, if you're… we definitely want people to be familiar with this pattern, because, like, this is something that is now a part of the metrics SDK, so, like, it's important to know what's going on here.
So if you haven't yet, I definitely think you should review… if you haven't taken a look at the summit notation, I would definitely say, like, you need to take a look at this one. It builds off of that.
And I think this is… it was pretty straightforward. Yeah, I guess the only thing that we…
we're going back and forth on was just, like, counting min-maxes, but otherwise, like, it looks very similar to what is done in the other one for, like, bucket counts, so.
**David Ashpole (dashpole)** 29:40 We fixed the min-max thing, I think.
**Tyler Yahn** 29:42 Yeah, I agree, yeah, so…
Yeah, but otherwise, like, there's really not much of a difference between the sums, PR and this PR. So, yeah, I think that this is pretty straightforward, and it,
Yeah, if you've reviewed the sums PR, this shouldn't be too hard to take a look at.
But, okay. Yeah, it looks like I need to also take a look at this one. I do want to keep it in this, milestone, though, because I would like to get this one merged.
**David Ashpole (dashpole)** 30:06 I've been working a lot on exponential histogram, but I haven't put anything up because,
yeah, I haven't gotten it to a state yet where it's ready, but I think it is possible to do a lockless, or a… most… this one won't be lockless, but…
to make it easier to do, or I have something similar for exponential histogram.
I figured out some… some ways to… Get scale changes to work.
But that's been fun.
**Tyler Yahn** 30:40 I'm interested to see this.
**David Ashpole (dashpole)** 30:41 It'll be fine.
**Tyler Yahn** 30:43 Yeah. The last value seems like that should be pretty straightforward. What's… is this just waiting on, essentially, like, what we've done with, like, the.
**David Ashpole (dashpole)** 30:51 Atomic.
**Tyler Yahn** 30:52 It shows…
**David Ashpole (dashpole)** 30:52 It shares a bunch of code, yeah, it shares a bunch of code with the histogram one.
**Tyler Yahn** 30:55 Yeah, okay.
**David Ashpole (dashpole)** 30:56 Much simpler than the histogram.
PR, actually, so… but it just includes all the commits.
**Tyler Yahn** 31:03 That makes sense. Okay, we'll…
Cool, maybe we could… here, actually, why don't we add this temporarily in here?
Sure. Into the milestone, and then let's take a look at the milestone.
**David Ashpole (dashpole)** 31:18 I suspect nobody really cares about the performance of last sum.
**Tyler Yahn** 31:23 I'm serious.
**David Ashpole (dashpole)** 31:23 synchronous.
measurements, but… It's good to… good to have it.
**Tyler Yahn** 31:29 Yeah, I feel like, this is a pretty easy follow-up once you get the others, but, I agree, yeah, that's probably not a high priority.
Okay. Jumping in here, let's see… I don't think that this is gonna be too much of a blocker if we're looking at the rest of it. We obviously… this is another one from Robert that needs a PR review, to get this merged, so…
these last… Three are, review-based, trying to resolve.
This is obviously blocked by this, so yeah.
I think progress on this, like, we're looking forward… we talked a little bit about this exposed temporality selector function. I didn't respond to this last time,
Don't know why I didn't.
But maybe, yeah, maybe we can just talk about this for a second here. Last, SIG meeting, we had a discussion about this, where this is… this added… this… this… actually, there was another PR already who… that added these selector functions. This is adding, not selector functions, but, selector enums that would then be translated into selector functions.
And it was recommended in this PR prior that, like, that should just live in the OTELConf package. The thing that came out last week was that, like, that is a very low-level selector, at the aggregation level that would then produce, like, a metric option.
for configuring the SDK. So it seems like a little bit more of a pollution of the API than it did a functional use case. And so it was recommended that, like, instead.
you could try to use, like, a meter provider setup function if you needed it, or provide your own package that just did this. There wasn't really a need, I think, at a high level as to why we would want to provide not only the selector functions and a configuration package, but then also some enum
That users could then write their own code to wrap the enum. So that was kind of, like, the consensus that we were gonna exclude this PR and close it. I just haven't written that up, I think, into…
a cohesive comment. So, yeah, I guess also maybe…
Maybe that was also what I was hoping, is just to run that by every… all the other, maintainers and contributors to the project, and get their thoughts on it.
But if there's no, strong desire to keep this, I will do that after this meeting.
otherwise, the rest of this is, observability-based,
project, so we have the simple span processor.
for tracing, I think there's definitely a PR for this. This is going, pretty slow.
So there's nothing really, I think, blocking any one of these, like, these could all be removed if we need to, but I think that this is something…
Maybe we can just take a look at here.
Also, probably make sure this is in the right milestone.
So there's no review. It's opened last month.
Okay, there's been a lot of review, actually.
So, yeah, it looks like this is just… it needs another…
round of reviews on this one. I think this one was pretty small.
If I'm not mistaken, yeah, well, relatively small, 400 lines.
I actually think this one is closer now that I take a look at it than I was thinking, it was before.
Yeah, this actually looked pretty straightforward. It was pretty straightforward because a lot of the framework was already set up for this due to the fact that we have other instrumentation in the trace package.
So, yeah, I think… I think all the stuff that I had asked for is addressed, so this just needs another round of reviews, so I think keeping this in the milestone makes a lot of sense.
The metrics of observability, the, OTLP metric GRPC exporter metrics…
Mmm… yes. Okay, I was like, I thought there was a PR for this.
This, has one review, it's in the milestone, that's correct. Let's see…
It's been open for quite some time, though, so there may be some changes needed.
Yeah.
Looks like there's a… Yes, this is definitely one where it needs more iteration.
We're waiting on that, so I guess this is one that may get bumped if we have a push to try to get, the…
milestone closed. So I think this is one that could actually get moved out.
I don't know if I'd prioritize reviewing that one, I guess is what I'd say.
The metrics SDK standard out metrics, or standard out, Metrics exporter.
This one, again, I think this actually is the same… Person… no.
let's see… I think this one was pretty close as well.
Yeah, a lot of PRs were replaced, I think, with other PRs.
So, it looks like FLC's been doing some good reviews, there just hasn't been any follow-up from the original author. So, again, this is one, that we could wait a little bit, but I think that this is, hopefully get some iterations on this.
The, standard.log export are very similar to what we just looked at. This is, I don't think there's…
Okay, yes there is.
I haven't… reviewed this PR, I don't think.
That's not true.
I have reviewed this PR.
This isn't a different milestone than…
That's probably just a mistake on my part.
Let's see…
Yes.
There's definitely a lot that needed to get done with this one, after looking at this review.
I left this last week, so there hasn't been any follow-up on it. I don't know if this one needs to get bumped out, but it does not look like there's active work on it, so, we can wait on this one again, and it can get moved out.
And then, I think these are all the PRs at this point, yes, that we've already gone through.
So I think, talking about that, we can close this. I think I'll plan on doing that today.
I don't think any of these, outside of maybe this one, should block the release, because this one's pretty close, and there's active work being done on it.
So, it's more about if we can get the rest of this, resolved?
And if that's the case, then I think we can bump all the rest of these and make a release. So, you know, we're coming up on, I think, over a month at this point for the release, so I think our timing-wise, this is a good idea to try to, push to get some of these,
resolved.
**David Ashpole (dashpole)** 39:11 Whoops.
I think, we lost Tyler.
**Tyler Yahn** 39:16 This one night.
**David Ashpole (dashpole)** 39:17 Oh. Point, so…
**Damien Mathieu** 39:19 We… we lost you for a bit.
**Tyler Yahn** 39:22 Ugh.
Yeah.
**David Ashpole (dashpole)** 39:26 Okay, looks like…
**Tyler Yahn** 39:28 something got transcribed, and all of a sudden my Zoom thing broke, so, okay, hopefully I'm back. Okay.
Sorry, yeah, if we can get these resolved, I think that we can then look at, like, removing some of these from the, milestone. But otherwise, I think we're making a lot of great progress, so, yeah.
Moving on to the contribib milestone.
Yeah, I think this is just another one that needs, some feedback on it.
I don't know if there's any actual, actual work on it, but yeah, it's still included. Needs to get, I think, addressed. There's a lot of conversation here.
I think this has a lot to do with also my recent PR to try to get air type, a little bit more useful, but I think this is more universal, where it's asking about, like, what our pattern should be for HTTP, if I'm not mistaken. So, yeah.
**Robert Pająk** 40:34 It's even more vulnerable.
**Tyler Yahn** 40:36 Right, correct, yeah.
Okay.
So yeah, still work to be done there. Alright, so checking in on that, I think there's definitely some reviews, and then there's the contributel HTTP work to pick up.
But other than that, yeah, that's the end of the agenda. Any other topics people wanted to talk about or discuss?
**David Ashpole (dashpole)** 41:08 Is there anything we wanted to…
it's… it's less than a month to KubeCon now. Is there anything you want to make sure
I don't think we'll be ready for logs, right, Robert, for KubeCon?
No. Okay, so…
**Robert Pająk** 41:23 Not impossible.
**David Ashpole (dashpole)** 41:25 We should think if there's anything we wanna…
not announce, but, like, talk about at KubeCon that's happened in the past few months. I'm trying to think if anything as big as launched.
**Robert Pająk** 41:37 The biggest thing which I would like to…
personally, is having this extended attributes merge in specification and product.
Yeah, but you know it's not right.
**Tyler Yahn** 41:57 Yeah, I mean, I'd love to get some of this observability stuff out.
**David Ashpole (dashpole)** 42:03 Will we have completed the HTTP SEMCOMF migration by then?
**Tyler Yahn** 42:09 Yeah, it's done.
**David Ashpole (dashpole)** 42:12 Yeah, yeah, we've cleaned up all the old stuff, right? That was last release, or was that recently?
**Tyler Yahn** 42:18 Yeah, it might have been the last release, I think, yeah.
Yeah.
**David Ashpole (dashpole)** 42:24 I don't know if we want to…
**Tyler Yahn** 42:25 I mean, I think that there's still cleanup in the repository for code, but yeah, from the user's perspective, like, the functional element, I think is done, yes.
**David Ashpole (dashpole)** 42:34 I think we could… I don't know if we have a project or anything, but we could consider,
Trying to work towards a stable release of those then, right?
**Tyler Yahn** 42:44 for HTTP.
**David Ashpole (dashpole)** 42:46 For the HTTP instrumentation in Contrib.
**Tyler Yahn** 42:50 Yeah, sure. I mean, I think there's a lot of work there to be done, though.
**David Ashpole (dashpole)** 42:55 Yeah, okay.
**Tyler Yahn** 42:56 Yeah, I think that sounds like a great idea. You wouldn't need somebody to, I think, take it on, though.
**David Ashpole (dashpole)** 43:02 Sure. Okay. Well, I'll… I'll think about it, but…
**Tyler Yahn** 43:06 Yeah.
Yeah, I mean, I think… I agree, like, I think it sounds great, but, it's also one of those ones where it's, like, it's lived for so long, and it's got a lot of cruft, and, like, the original design…
it takes about 5 minutes to take a look at the API, and you may ask yourself, like, is there a better way to structure this? So, yeah.
There's… I think there's some, like, larger questions of whether we want to stabilize what's currently there.
**David Ashpole (dashpole)** 43:34 So, yeah.
Okay.
**Tyler Yahn** 43:37 Yeah.
But yeah, I mean, I think…
from the semantic convention-wise, I think it'd be helpful, yeah.
Cool. Anything else? Folks are…
Maybe working on in the background?
Oh, I guess I could share… Yeah, I guess…
in my absence of not doing reviews, and I'm also absent in addressing some, like, custom errors for the OTLP exporters themselves.
that new error type that we were introducing so that we can have in the semantic conventions. I was restructuring, like, right now, we return…
Technically we return, like, a… like, this partial error, but, like, I think that there's… there's actually, like, 3 different errors, really, that we can return from these, OTLP exporters. They're, like.
HTTP or gRPC errors, partial errors, or there's technically these, like, warnings as well, because if you get a partial error without a, like.
rejected span, account, and it's technically called, like, a warning.
So I've actually, like, built these three errors, like, and tried to integrate them. I did integrate them for the, Otel Trace, gRPC.
OTLP trace gRPC, setup, but yeah, it's still, like, a prototype, so I'm still working on it, but, like, it's really helpful in the observability stuff, because, like, you can start to see, like, instead of, like, these, like.
super opaque error types that just say, like, error join, or, format error sort of thing. It tells you, like, oh, like, hey, if this is an RPC error, here's the, like, the words for what the RPC error was, and if it's something else, like.
it's a partial error, it'll tell you, like, this is a partial error, so it's helpful there, but it's also helpful, I think, from the user's perspective when they're writing the instrumentation, where, like, it's a unified, like, error message that's not, like, very opaque at that point. It gives, like, clear understanding of what caused the error.
So, yeah, I was just working on that, I haven't…
pushed it yet. It's not super critical, it's just kind of a nice, thing on the side. So, yeah.
**David Ashpole (dashpole)** 45:53 Cool, very, very important.
**Tyler Yahn** 45:57 Yeah, no, not really. But, yeah, it's… your dashboards, look really nice, by comparison, so, yeah.
Well, cool. Yeah, if there's nothing else, we can end the meeting early here.
Thanks, everyone, for joining. Good to see you all. Looking forward to getting, you know, another release out. Yeah, maybe that should be our goal, is get the release out before KubeCon. Yeah, so…
let's try to… let's try to work towards that. Let's get some reviews done, and then we'll… we'll progress… press this forward, yeah.
Talk to y'all later.
Bye.
**Bryan Boreham** 46:34 Alright.
