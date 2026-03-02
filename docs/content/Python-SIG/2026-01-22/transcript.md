SIG: Python SIG
Date: 2026-01-22
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/FxugT_-c7ZwZHkCEdCWZRmxn4Cbuhj1xDWHkBshV7sLk90C_KvivDaSUWEe1NGvJ.tijdL_y6RLXAzDQ7
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:47 Hello.
**Dylan Russell** 00:51 B.
**Riccardo Magliocchetti** 01:46 Welcome, everyone, to this week's Python Recall.
We're waiting a few more minutes for more people to join.
In the meantime… Please add yourself, as an attendee to the notes.
And also, if you have any topic you want to discuss, feel free to add it to the notes as well. And I shared the link to the notes on the Zoom chat.
**Aaron Abbott** 03:13 Everyone, it's going…
**Rowe, James** 03:22 Hey, Ricardo, James Rowe here from J.K. Morgan. I'm working here with Manny, who's on the call as well. Is it okay if we add,
Topic for this call, just now.
**Riccardo Magliocchetti** 03:35 Yeah, sorry, could you…
**Rowe, James** 03:38 Yeah, I… Yeah, just, asking if it's okay if Manny adds a topic right now,
**Riccardo Magliocchetti** 03:45 Yeah, sure, of course.
**Rowe, James** 03:46 Perfect, thanks.
**Munir Abdinur** 04:19 Hey folks, I don't have any topics for this call, but I just wanted to join and just introduce myself. My name is Munir, I work at Datadog, I maintain DD TracePi, and I want to start being more involved with, like, the OpenTelemetry Python community.
Nice to meet y'all.
**Aaron Abbott** 04:34 Yeah, awesome, nice to meet you. It's always good to see new faces.
**Riccardo Magliocchetti** 04:42 What com… Yeah, I think we can start.
We have quite, quite, Lots of stuff on the agenda.
Okay, the first one is from me.
Yeah.
like… an update on…
stabilization work. First thing, I would like to, well, if you can take a look of this comment, about,
the move… like, moving the logging handler, at the moment is inside the SDK, but we would like to move it outside that.
And the only issue we see.
on the proposal of just copying the code, some… somewhere else.
Is that we should decide that we'll be handling the same, Environment viable.
Yeah, like, for me, it's a good time to do, like, the real breakage, so… for me, it's fine to move the handling to underrep package, and I think…
On… of moving stuff inside the logging instrumentation.
Or… Yeah. What's the alternative to just kind of leave it…
**Aaron Abbott** 06:06 Or it is, and do, like, a lazy import or something like that.
**Riccardo Magliocchetti** 06:19 Like… Could you please elaborate a bit? Because, like, I don't…
I'm not sure you're following? Like, what do you mean we're busy in my work, or…
**Aaron Abbott** 06:28 Yeah, like, do… Where would you want to move the handling to, I guess, so I didn't get…
**Riccardo Magliocchetti** 06:36 I don't know, like, one place, but to me looks sensible, since this is, like,
attached to the Python log implementation.
I think will be, like, the… OpenTraimeter Instrumentation Logging Package.
But this is in country.
Okay, yeah.
**Aaron Abbott** 07:00 No, that sounds good to me.
Yeah, I think this is good.
**Riccardo Magliocchetti** 07:10 Okay, so you're fine moving the handling of the AutelPython longing, auto-instrumentation enabled, as well?
**Aaron Abbott** 07:17 Yeah, I mean, if we broke that… if we move the handler out anyway, like, it won't work if it's in the SDK, right? Like…
You have to make sure both packages are installed.
**Riccardo Magliocchetti** 07:27 Yeah.
Yeah, but I think you proposed to just copy?
The code, until, like… But, yeah, like, this one would be, like, enough for breaking.
**Aaron Abbott** 07:45 I see. The old data.
**Riccardo Magliocchetti** 07:46 Not manual… users, yeah.
**Aaron Abbott** 07:49 Yeah, I see what you mean.
**Riccardo Magliocchetti** 07:54 Well, like… We kind of think a bit on this, discuss on the issue.
**Aaron Abbott** 08:00 Yep. Okay, sounds good.
**Riccardo Magliocchetti** 08:03 And the other one, I opened a PR to tackle another issue, but it's not too urgent or important, but it's…
annoying?
That is wet at the moment, this, logging instrumentation is…
adding some autospec stuff to the Python, logging log record.
And then, when log shipping is enabled, these attributes are then added as an attribute to the LTP logs exported.
And so, like… some stuff that… Does not look like, Correct. Is exported.
And so, I created this PR, so if you have time, please take a look. And it's just, like, making the…
The addition of his, of these attributes.
Depending on the fact that you're actually, using that to format the Python log record.
the catalog message.
Because, like, by default, they're not used, but they're, added, anyway, and so, like, at least, like, out of the box, we can avoid just that random stuff, but it's not used.
Yeah, sorry for that, Mr. Cook.
Sure. Ben?
Next topic, also for me, yeah, like, I have a bunch of PRs on the Core Reaper, adding some stuff.
Yeah, we'll appreciate some reviews, if you have time.
One is adding a rule-based, experimental sampler.
Composite sample.
One is, being a test configurator.
And I would like also to add, the meter and low configurator after this.
And then one, another one, but it's some more configuration for instrumentation, that is, like…
like, at the moment, without instrumentation, when you do the SDK config, we are called the…
batch span processor has only span processor, and only as…
At the process of wrapping this quarter.
And I just added, like, some more parameters to the init.
Function to being able to specify different processes.
But, yeah, again, in short time, please take a look.
Then, another thing is that we are working at Elastic on implementing SDK metrics.
Anrac, what is doing the work, started with PR.
At the moment, I think we have… we are blocked on… contribute test.
Because when we add another producer of metrics, all the code that is asserting the expected metrics start failing.
Because we don't have, at the moment, a way to filter, like, the metrics by the scope.
So, yeah, we're working on… Updating the various test helpers and the test.
And then, yeah, we make, like…
I'll probably ping you again to take a look at the PR once we have the…
green CI, but… For your information, we are working on this.
A couple more, topics from me.
Unless you have any comments?
Okay, next one is, Tammy has, done a bunch of PR since, rather opens is a few.
or, the support for a stable HTTP, cementing convention on… a couple of…
Server instrumentation that are missing them?
I think one is Tornado, and the other one is Pyramid.
I view the booth, but…
yeah, like, a second look would be appreciated. I added a last-minute comment after approval today from one of them, because I noticed that
We are missing sanitization of the query parameters.
And… yeah, also, I think we are missing wet sanitization in more places.
But, yeah, I'll try to, understand, because I'm saying, right?
**Marcelo Trylesinski** 13:20 Sorry, sorry to interrupt, but do we care about packages that are unmaintained? Like, for example, Pyramid is unmaintained for 2 years and a half already.
**Riccardo Magliocchetti** 13:34 I don't know, I don't think we don't have any…
Feedback on if our stuff are used or not.
But… Yeah, like, probably, like, if we're maintained,
a good opportunity to the breakout stuff, I guess.
**Marcelo Trylesinski** 13:55 Yeah, no, I mean, I'm just saying, maybe we should have process to… Like, don't care about,
observability on packets that are no longer being maintained, or something, I don't know.
I'm just saying that because you mentioned a library that's not being maintained anymore.
**Aaron Abbott** 14:17 I mean, like, pyramid itself, not this instrumentation. Yeah.
**Marcelo Trylesinski** 14:21 Yeah, yeah, not the instrumentation, I meant the… Deliverito.
**Aaron Abbott** 14:28 Yep, that's a good point.
**Lukas** 14:30 but it was not used anymore either, so there's probably quite a few that we could just remove, I'm not sure what the process we want to do there is.
**Marcelo Trylesinski** 14:43 I mean, I'm not suggesting the removal itself, but I'm suggesting maybe not working on it, or do something…
Work on a process towards, achieving Removal, actually, yeah.
**Riccardo Magliocchetti** 15:04 Like, I don't think we have a process in place.
But, like, I think I opened an issue
Signaling, the… the plan to remove their boat instrumentation.
Betters being, like,
not updated since, I guess, if I remember correctly, like, 7 years, or something like that.
So… Like, it was like… Python 3.2 times, or something like that, so…
So, yeah, probably, like, we should probably,
Like, if any of you knows of any abundant, Package we have instrumentation for.
Maybe it'll… Drop a note or open an issue, and we can discuss.
**Marcelo Trylesinski** 15:52 I mean, I think it's useful, the discussion about how we do this, more than, finding, like.
What's the process of…
Stop creating, like, working on instrumentation for a package, and when we stop supporting other versions of that package.
I don't have any proposals.
**Riccardo Magliocchetti** 16:16 Okay, I don't any answer for that.
But yeah.
I should think about this.
**Aaron Abbott** 16:25 Yeah, I mean, maybe, like, Tammy, on this PR in particular, was it… was it just kind of, like, for completeness sake, or was there a…
Did you have a use case to update Pyramid in particular?
**Tammy Baylis** 16:37 It was for completion of a now-years-old issue to migrate several framework instrumenters. I don't use Pyramid myself.
**Aaron Abbott** 16:49 Gotcha.
Okay. I mean, I think… I wasn't aware of that, but I think that's really useful going forward to know. Yeah, we could probably focus our efforts. I think…
we might have had the issue based on, like, PyPi stats for each HTTP instrumentation, and maybe Pyramid was popular, but…
Yeah.
Also, the PyPy stats are notoriously, like.
you know, it could be CI, noise, and stuff like that, so…
I think that was part of the reason we chose Pyramid, but… All good points.
**Riccardo Magliocchetti** 17:31 Thank you. When… okay, last,
topic for me, for a few list. And, yeah, just a quick, FYI… I'm trying to,
implement, Sampling that cares about the… HTTP, attributes.
on SPANS, and I audited, our instrumentation, and, I noticed… noticed it, but some,
added the attributes later, after, span creation.
And so… Yep.
I would like, like, to, to move the, like, adding these, the, the request attributes.
At span creation, so they are available to the sampler.
And do you send it back, or…
This is fine. Also, like, since I think it's trivial.
We can also make this a good first issue if anyone wants to.
There could be. Like, most of the time, it's just a matter of moving align,
Before the span creation.
Okay, so… No objection?
Next one.
It's from Tammy?
**Tammy Baylis** 19:13 Hi, yeah, thanks again. So,
I would just like, more reviews of this PR. It's to add a labeler, like the Golang implementation has, and integration of it into a few, HTTP server instrumenters, and we talked about this a while ago.
The ability to add custom attributes should be okay with the semconv, and this would be easier to use than baggage, and I have an explanation on the linked issue for why.
Our use case is that it would make, metrics querying, easier if the value's known only after an HTTP request is received, and without changing something like the span name.
But yeah, that's,
That's a mouthful of just… if anyone has time, I'd appreciate some reviews. Thank you.
**Aaron Abbott** 20:18 Cool. I haven't looked at the PR yet, but
So, does Labeler… is Labeler, like, part of the public API, or is this kind of,
Like, you just set a special key in the context, and then everything else kind of works from there.
**Tammy Baylis** 20:33 It's more the latter, and I think this isn't part of the… this wouldn't be part of the core SDK, it's part of the instrumentation library.
**Aaron Abbott** 20:45 Okay, and then so, like, it's pretty much a no-op for most people,
If you don't set anything in the, in the context key, nothing different happens, right?
**Tammy Baylis** 20:56 Yes.
**Aaron Abbott** 20:57 Okay.
Yeah, sounds good to me. I kind of vaguely remember talking about this, so…
**Tammy Baylis** 21:05 Yeah, thanks, Erin.
**Riccardo Magliocchetti** 21:19 Okay, any other comments?
Otherwise, another quick one for me. I would like to get…
VPR on the next, release?
Dylan already reviewed it. Thank you.
And I think… yeah.
Versus, CI, you see red, but issue at time?
Since this is, like, an exporter code.
please take a look.
Okay… Next topic, from Maridima.
**Ridhima Satam** 22:09 Yeah, so the Spear is the line chain using geneal Speer. I got initial reviews and approval from
Keith, so… I'm just asking for maintainers, to review it.
Oh, yeah. So, it's just telemetry, we have moved to a Gen AI utils, so initially, the Langchain had support for producing the telemetry, it's just now going to use the Gen AI utils.
**Aaron Abbott** 22:45 Yeah, I'm sorry, I owe you a review.
If anybody else wants to take a look, that would be super helpful, but,
I'm kind of inclined to just merge it, or approve with Keith, since he wrote the…
The handler thing, so… Yeah, sorry for the delay.
Thanks for the PR.
**Ridhima Satam** 23:06 Sure.
Yeah, and the second PR is mostly about the SEMCAF… Introducing workflows.
And I guess, again, I have initial review from Ankit and approval from him.
And also, I think Ludmilia looked at it. She was just asking me to open a ticket, follow-up ticket for the workflow metrics, so I've created that.
Yeah, so… They're waiting for approvals from maintainers for both of the peers, yeah. That's all.
**Riccardo Magliocchetti** 23:43 Okay, thank you.
Next… Topic is from Kif.
**Keith Decker** 23:59 So I had done reviews on this one for adding events to JAIutils, I didn't actually write the PR, just looking for more…
Refuse from… from other maintainers as well.
If… Cerilia doesn't address comments in the next week or so.
should I recreate this PR under my own PR and keep pushing it, or how do we handle that if the original author kind of…
Doesn't come back.
I know he's pretty active, so this is probably more of a…
General question, not necessarily for this peer.
**Aaron Abbott** 24:44 Yeah, I mean, if they're, like, truly unresponsive, we can do that.
Also, like, if its maintainers and stuff are gonna work on it, we might just push commits to the branch, assuming that they open the branch up to pushing, but…
I don't know if that applies here. I would say, have you been in touch on Slack at all?
**Keith Decker** 25:05 No, I'm planning on messaging him today.
But yeah, so I would try to push a…
An update and didn't have rights, so…
**Aaron Abbott** 25:16 Yeah, yeah, makes sense.
**Marcelo Trylesinski** 25:19 Just ping them.
Yeah, it was more of a general question on if an author disappears, so that was… I think that if they don't reply in some days, you can create a branch on top.
**Keith Decker** 25:34 Okay, thank you.
**Aaron Abbott** 25:39 Okay, thanks, Kate.
**Marcelo Trylesinski** 25:40 Always, always keeping the commits, so you keep the author.
**Keith Decker** 25:44 Sounds good.
**Riccardo Magliocchetti** 25:52 Right?
But…
Excellent.
Okay.
Last topic from Manny?
**Rowe, James** 26:18 Manny, can you… we can't hear you.
Seems that Manny's microphone's just broken at the most. In an opportune moment, sorry about this, guys.
**Yazdankhah, Mani** 26:33 Can you hear me?
**Riccardo Magliocchetti** 26:35 Yes.
**Yazdankhah, Mani** 26:36 Sorry, yeah, this was raised…
I think in early December, it took a while to come back with the PR, but we discussed adding new APIs to add and remove metric readers at runtime, because this isn't something that's currently supported in the SDK, but it's a functionality we need.
We got agreements that we just add two functions to the…
Metric provider, or sorry, meter provider, to achieve this?
And would appreciate some reviews on this.
It's the first time I'm contributing, so I'm not sure what the…
Proper steps are to get this reviewed and moved.
**Riccardo Magliocchetti** 27:24 I think the answer will be, like, have a bit of patience, because we are always, like, a bit late on our reviews. We have, like, a ton of stuff to review, and not enough reviewers, but yeah.
Hopefully, like, eventually, someone will take a look.
But yeah, I think it's… Yeah.
is tested, so, like, won't take long, I hope.
**Aaron Abbott** 27:55 Yeah, and likewise, I…
I just want to say, like, anybody is welcome to review, you don't have to have a green checkmark or anything like that in the repo, like.
Coworkers or whoever, if you want to take a look, it's super helpful to just have you know.
Multiple people taking a bus.
**Rowe, James** 28:17 Yes, I've, I've…
worked with Manny, and I've reviewed the code in our private repo, first of all, and happy with it, so it's really just with the open source community wanting to make sure that
There's no, no issues, so thanks, guys.
**Aaron Abbott** 28:36 Okay.
**Riccardo Magliocchetti** 28:40 Okay, so these were all the topics for today. Anyone has something else you want to discuss?
Not, so… Thank you, everyone.
Yep.
**Dylan Russell** 29:02 There he goes.
**Aaron Abbott** 29:03 Till later.
**Rowe, James** 29:04 Bye.
**Marcelo Trylesinski** 29:04 2…
