SIG: Python SIG
Date: 2026-11-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:22 Hello, everyone.
**Diego Hurtado (Dash0)** 01:26 Ayy… Let's go ahead.
**Pablo Collins (Splunk Inc.)** 01:28 Blue.
**Tammy Baylis** 01:31 Hey, y'all.
**Riccardo Magliocchetti** 01:34 Hey, Tammy.
**Tammy Baylis** 02:30 Hey everyone, I'm sharing screen. Welcome to the Hotel Python SIG meeting.
Meeting notes are in the chat. Please open it up and add your name and any topics you'd like to discuss this week.
We'll start in a couple minutes.
Okay, while we wait for more people to arrive and other topics, I'll just do about five and a half minutes of triage.
Let's look at the contributions today. This is the… Bought maintained PR dashboard.
These are waiting on reviewers, going, first chronological, most recently submitted.
Hmm… Panya, fix the request instrumenter.
Resolve implicit default port for client metrics.
Hmm… Cool, we have a… I dish you? Thank you, yes?
**Riccardo Magliocchetti** 04:49 like this, contributor, OpenAPR, fixing, URLib, and so… Looking and reviewing that.
I see that we have a bunch of to-dos.
Inside every client, HTTP instrumentation, For…
**Tammy Baylis** 05:08 Sorry.
**Riccardo Magliocchetti** 05:09 So I asked him to open an issue instead of… opening just PR, so at least we can track of, all the clients at once.
**Tammy Baylis** 05:20 Yeah, thank you very much.
**Emídio Neto** 05:33 Just a question, Riccardo. Is this something new, or something we just didn't implement?
**Riccardo Magliocchetti** 05:40 I think that when Leighton did the HTTP conversion, something where I… Like, we have a bunch of to-dos, And I don't remember… I think it's about the scheme or something.
And so… the contributor was adding, the same to-do.
And so I said, please open an issue so that at least we track that instead of… Oh, yeah, that's too.
**Emídio Neto** 06:14 Go see.
**Riccardo Magliocchetti** 06:15 That was…
**Emídio Neto** 06:15 Something, I mean, yeah.
Yeah.
**Riccardo Magliocchetti** 06:19 If you go to… if you go to the diff, I think there is the to-do here as well, so we can… Thanks, Steph.
**Tammy Baylis** 06:31 For this PR, or the other one?
**Riccardo Magliocchetti** 06:34 I've… The other one, I think. They will… you or Livia.
Yeah, we swans are.
**Tammy Baylis** 06:39 There we go, yeah.
for,
**Riccardo Magliocchetti** 06:50 a bit up. There was a comment, around that…
**Tammy Baylis** 07:00 Mmm, I wanna be honest.
**Riccardo Magliocchetti** 07:02 They have a 10-year scheme, yes, yeah.
**Emídio Neto** 07:06 I see, I see. Yeah, I remember now.
Thanks.
**Tammy Baylis** 07:14 Yeah, thanks. Thanks, Radhika, for this, too.
Okay.
Yeah, I can't… whoop.
I commented on this as well, please, like, take a look at the comment.
Leave that for now, cool.
Oh, another docs PR. Always welcome.
With a linked issue, excellent.
From 2 years ago.
Mmm, logging… Just wondering how… accurate this is with logging API stabilization.
**Leighton Chen** 08:08 Yeah, I think this issue was created a while ago, before we even had, When we move the log handler to logging instrumentation.
**Tammy Baylis** 08:18 Mmm.
**Leighton Chen** 08:18 It wasn't clear why we had an instrumentation as well as a handler in the SDK that does the… The log worker enrichment.
I'm not… sure where we want to go with this. I haven't taken a look at… the recent documentation, but now that Logging Handlers in Logging Instrumentation, it It, it is… conceptually more clear, which one is used for which scenario, where the API and the SDK are just purely for Creating and managing log records.
So, I don't know if we still need this, to be honest.
**Tammy Baylis** 09:06 Yeah, okay.
Yeah, okay, I'm gonna note something down. Thank you, Leighton.
**Leighton Chen** 09:24 Oh, sorry, I was muted. Yeah, I will… make a comment on it as well, so… Because that was the original, okay.
**Tammy Baylis** 09:34 Thank you.
Meetings right.
Cool. Okay, it's 10 after.
Let's pause on the triage for a while, and we'll look at our, meatier topics for today, starting with Riccardo. Go ahead.
**Riccardo Magliocchetti** 10:21 Yeah, this is a quick one, like, I was reviewing the… DPR issue today.
And I assume this one.
That is just… Using, like, Getatra to assess the kind attribute of the spans.
Because, the kind attribute is not defined.
in the, ABC span, we have in the API.
And so I was wondering if… Like, since Civicism being… 4 years, I guess. Like, do we care about, people using, spans, but are not our SDK in instrumentation.
Oh, so, like, the patch is trivial, it's just, like… But… Yeah.
**Tammy Baylis** 11:20 Right, I see, so…
**Riccardo Magliocchetti** 11:22 Yeah, like, the point is.
An implementation where each recording returns true, but does not have the kind attribute.
So, I think it's kinda niche most of the time.
Leighton.
**Leighton Chen** 11:38 Yeah, I was taking a look at this, given that the change is, like, so trivial, I don't… I don't mind adding this, as it doesn't… Change any behavior, but… I was a little hesitant on setting the precedence that, like.
We will make specific changes based off of, custom implementations. It seems like a kind of a can of worms. So, I think as long as the messaging is right, Like, I'm okay with this.
**Riccardo Magliocchetti** 12:23 Yeah, like, also, I don't have any… strong opinion as well, but I guess we can manage that. The problem would be, like, remember to always use, assume at the… The span is from the SDK, but… Okay.
Thanks.
**Tammy Baylis** 12:49 Yeah, thank you. Yeah, I don't… Have a strong preference either, but yeah, there's… A lot of code that's probably doing this, so… This mark is ready for review.
Okay, and Riccardo again, body and HTTBC.
**Riccardo Magliocchetti** 13:10 Yeah.
**Tammy Baylis** 13:11 Yeah, go ahead.
**Riccardo Magliocchetti** 13:12 So, like, recently, we at Elastic, added to the semantic convention.
An attribute to collect, the… body content of, HTTP… I think both request and response.
And we would like to start implementing that for, HTTP server implementation… instrumentations. This is, of course, obtained.
And… yeah, like, we have… the first, PR for the WSGI instrumentation.
SO… If you want to take a look.
You're more than welcome.
Adam?
**Aaron Abbott (Google LLC)** 14:08 Hey, this is pretty interesting.
I had a question about the body size and, like, truncation behavior, there's attribute limits already in OTEL, and this would be, like, a separate config specifically for HTTP, or… and I guess, is it part of the spec already, the config?
**Riccardo Magliocchetti** 14:31 Not yet.
I don't think it's… Already in the config.
But, the… Our plan is to… I have, like, one bolt to control the… if you want or not.
And… a mandatory size, if you want the invites to capture.
And also, like, for HTTP, Having the… a way to express, like, which media types you want to collect.
To capture, say that… To not, you know… Most of the interesting stuff will be, like, text.
And so, at least limit the collector stuff to only text.
**Aaron Abbott (Google LLC)** 15:25 Yo.
**Riccardo Magliocchetti** 15:26 But… Yeah.
**Aaron Abbott (Google LLC)** 15:30 Okay, yeah, it sounds pretty cool. I can… Maybe take a look, but,
**Riccardo Magliocchetti** 15:36 Like, I, I forgot, like, at the moment, it's just, just parameters for this to mentor class.
And so, like, once we have something in the config, we just need to map the… whatever we get there with the instrumental parameters. Like, I don't expect to be much different.
Okay.
**Aaron Abbott (Google LLC)** 16:00 Cool. One other question was, I don't know if you've seen, but Ludmila added, Underscore ref, like, generic.
Semantic convention for storing large stuff outside of, like, the span, and stamping a reference to, like, an object storage.
I can… I can link it, but I don't know if Elastic has already seen that, but, you know, obviously these are gonna get pretty big. I was wondering if… You were looking into that, or aware of that convention?
**Riccardo Magliocchetti** 16:33 I remember that from the GenAIE… stuff.
**Aaron Abbott (Google LLC)** 16:36 Yeah.
**Riccardo Magliocchetti** 16:37 But, yeah, like… for us, we plan to just… Capture a small part of the body?
Like, we don't… we… like… We would like to only catch text, so avoid binary stuff, and Because, like, the problem with binary stuff is that Also, the adders are obtained.
And so… At the moment in Samcov, it's not already… Specified that you should also collect the useful headers, like content type and… What is the other one?
And, and then coding in order to… The code what you have in binary.
But, yeah.
So, like, I think at the time, this is still, I won't say work in progress, but… endeavor, in development, to use Auto Jericho.
And so, yeah, we made two movies a bit, but the plan was to at least start with something, And update accordingly, but yeah, like… For our backend?
For us, it's better to have staff in attributes than external references.
But yeah, I am aware of that.
Good afternoon.
**Aaron Abbott (Google LLC)** 18:13 Cool. Maybe I'll… I'll take a look at the PRs and poke around, but sounds pretty interesting.
Thanks.
**Riccardo Magliocchetti** 18:20 Thank you.
**Tammy Baylis** 18:30 I guess…
**Aaron Abbott (Google LLC)** 18:30 Thank you.
**Tammy Baylis** 18:30 Very…
**Aaron Abbott (Google LLC)** 18:31 I can ask one more question on that one if nobody else has something.
**Tammy Baylis** 18:33 Yeah.
**Aaron Abbott (Google LLC)** 18:35 Yeah, Riccardo, I don't know if you said you're kind of just adding, like, the API surface right now.
Are we planning to make it so that, like, the body is streamed? That would be my recommendation if we're, like, designing the APIs.
**Riccardo Magliocchetti** 18:55 I think that implementation Is using manga steam wrapper for whiskey.
Yeah.
Like, if you can… Tammy, if you want to open the diff, maybe… Oh, yes.
I think, yeah.
We have a stream wrapper, and we just… we wrap the function that are reading from the stream.
And we accumulate what we got there.
**Aaron Abbott (Google LLC)** 19:29 Okay.
Yeah, I think… I guess the context is I would be… I would be more interested in the… the underscore ref thing that I shared before, so… In those cases, it's nice if we can, not… not, like, buffered all the way, so I think it sounds like it's possible to do that in the… there's some… implementation, that doesn't… Buffer it before it passes it on to the attribute capturing.
**Riccardo Magliocchetti** 19:57 Yeah, like, maybe we could take a look at… I have an option to… Or buffer, or, Just a reference list and everything. But yeah, thanks for the point.
**Aaron Abbott (Google LLC)** 20:12 Cool. Yeah, that's it now. For real.
**Tammy Baylis** 20:17 Thanks.
No other topics written. Does anyone wanna just chat about something? PRs we should look at?
Otherwise, we'll, make this a quick one?
**Riccardo Magliocchetti** 20:35 Well, maybe we can spend a bit more time in… Intrudging, maybe?
Like, 9 minutes, so, yeah.
Natural history going.
**Tammy Baylis** 20:46 That's funny.
**Riccardo Magliocchetti** 20:47 13 years back, yeah.
**Tammy Baylis** 20:49 Sounds good, go back to the contra board, why not? We only did 2.
So long. Oh, look at all of these from the ego.
Wow, okay. Celery!
TJ Sisko.
Bound, signal, created, producer, spam, salary, sent to, so publication tariffs. Finish, span, No issue.
Anyone have any context on this?
Yeah.
Hmm, looks okay, it's not… Oh, hmm… Trace and task.
I think…
**Riccardo Magliocchetti** 22:03 Yeah, like, I've seen a context var, so maybe it's a bit more complicated one.
**Tammy Baylis** 22:08 Yo… Maybe I'll ask for… More information.
Cool.
Next, fix GRPC AIO Client Cancel Propagation.
There's no reviewers on this, I wonder why.
Hmm… I know a sign of yours.
One year ago… Pretty.
Wow, okay.
Oh my goodness.
Thank you, Tony Hong.
Gonna add, You're gonna hit us.
That is… Ready for a look.
Pyramid… I saw you go… Oh, it ignores… The tracer provider, apparently.
**Riccardo Magliocchetti** 23:59 Whoa, like… Yeah, like, 5 years ago.
**Tammy Baylis** 24:07 Yeah, if it's still the case…
**Riccardo Magliocchetti** 24:10 But it looks like we have two concurrent PR for the same thing.
**Tammy Baylis** 24:15 Ricochool.
**Riccardo Magliocchetti** 24:16 Yeah, Sunday-ish.
Yeah. Kodravi, it's okay.
**Tammy Baylis** 24:32 Whoa.
Everyone's at the party.
Okay, sorry, just curious. I'm just gonna quietly say that one's… Reference for review… And I think that's… I'll take a look at this later.
So I'm interested.
Okay, huh.
Mr. Dashpull?
Resource Detector GCP, populate cloud resource ID and detect Cloud Run Jobs.
**Aaron Abbott (Google LLC)** 25:21 Yeah, I think I should probably review this one.
**Tammy Baylis** 25:26 Oh yeah, there you are.
**Aaron Abbott (Google LLC)** 25:28 Yeah.
**Tammy Baylis** 25:30 Thank you, Erin.
This one has a black check already, sQLAlchemy… I'll take a look at this one, too.
Oh, yeah, I've been working with OfMed already.
Yeah, I'll take a look at this one.
AI or HTTP server.
Surrender. Cardigan's none response in the middleware.
Probably, yeah, another slightly old issue.
That's just another issue, okay.
This should be… Everyone to look at.
I'd say that's ready for a look.
Or easy to review.
Ready for review.
This one already has eyes from two of us, but I'll just take a quick peek.
Yeah. Yeah, Lucas is… Away right now, but… We'll let him have a look when he's back.
Did we look at this already last week?
AIOPICA and Publish and Consume Books. Old Issue.
Oh, sorry, Riccardo, you might have had your hand up for a while.
**Riccardo Magliocchetti** 27:45 No, no, no worries. I've added, another topic, like, another PR, to discuss.
Tiana, we can continue.
**Tammy Baylis** 27:56 Okay.
Just this one quickly, and then… probably still relevant, so I'd say… Ready for review, and… That's for us, okay.
Right, yeah, it's been 8 minutes. Let's look at this new topic.
Go ahead, Riccardo.
**Riccardo Magliocchetti** 28:23 Yeah, I'll be quick. We are with PR, but it's deprecating the bedrock, extension for the bottle core instrumentation from Dylan.
And I think it's fine.
But I was wondering, like, if it's a problem if we wait to get the… a bunch of the… I won't say regression, but, some PRs, we already open, But fix some gaps with this one, in the Gen AI one.
So, like, if you are cool to wait a bit, or if you want to have this merged?
Prompt.
**Dylan Russell** 29:09 I think, yeah, I think waiting for the next release makes sense.
Because, yeah, like you said, there's a bunch of bug fixes to the bedrock stuff, so…
**Riccardo Magliocchetti** 29:22 By the way, like, thank you for doing the work on the GenA side here.
**Dylan Russell** 29:28 Yeah.
**Riccardo Magliocchetti** 29:36 Okay.
Goes fast.
**Diego Hurtado (Dash0)** 29:54 Just a question about the deprecation of bedrock, I don't know if you remember, some time ago, we also duplicated, instrumentation, what was the name?
**Riccardo Magliocchetti** 30:07 The last is so… who are.
**Diego Hurtado (Dash0)** 30:09 Yeah, thank you.
Yeah, and there was a… A proposed solution about, making a last release… That will just, Like, remove the… the strict pin on open telemetry instrumentation and so on, so that people could still keep the last release of that instrumentation, and keep updating the rest of the components without breaking. Is that something we can do here as well?
**Riccardo Magliocchetti** 30:46 Here, we're not removing anything. This is just… if… The other, like, this is printing a deprecation warning.
And it just shuts down the current code if the other package is installed.
But…
**Diego Hurtado (Dash0)** 31:03 Okay, okay, alright.
Thank you.
**Riccardo Magliocchetti** 31:06 But yeah, I remember that.
**Diego Hurtado (Dash0)** 31:10 Yeah, I also want to.
**Tammy Baylis** 31:20 Cool, thank you, yeah.
Anything else anyone else wanna talk about? Sajid, hi.
**Sajid Ali Syed** 31:28 Hi, everyone. I attended the Intrip Fest at KubeCon last week, and put in a pull request on the main Opentelemetry.io documentation page on using the declarative configurations. I just wanted to see how to… Reorganize that, if reorganizing that is needed, and also just to stop by and see how to contribute to this project eventually.
**Tammy Baylis** 32:04 Yeah, welcome, thank you for this.
Yeah, where we're flagged, the Python approvers, we have to have a look at this, as well as the docs approvers, so it's in the right place, and thanks for bringing this to our radar.
Yeah, let me think, Yeah, you said you wanted to do more contributions. Did you mean to, the Python-specific code… code repos?
**Sajid Ali Syed** 32:38 Yeah, yeah, I think… I think more proficient, most proficient with Python, so just dropping by the Slack channel and seeing, I saw that a lot of the requirements right now are mainly for code review, so I'll try and better understand how the group works as well.
**Tammy Baylis** 32:53 Yeah, yeah, it's, it's a lot, we have, 2… We have these, Two dashboards, but we… have most of our code in this, Hotel OTELPython repo, and OTELPython Contrib, and we also have, I think… If you're interested, GenAI repo is our third repo. And, if you, like, if you're go… going through, say, the Read the Docs of, Any of these code repos, and you just want to fix the docs here as well, then that's a quick way to start contributing.
Otherwise, every repo has an open issues tab, and… Sometimes… Is there a good… yeah, there's a label for good first issue. Oh, come on now.
There we go.
It is hard to identify, like, what's a good first issue, and then what's the step after that, but there are some issues labeled with this. Feel free to… Say, open one and, like.
Oh, this one's really old, though. Maybe not this one, but feel free to comment, oh, can I contribute? And, like, link a PR and stuff.
Should this… sorry, I picked, like, the worst example. But yeah, just dive in, Sajid, are you also on the Slack channel?
**Sajid Ali Syed** 34:37 Yeah, I'm on the Slack channel.
**Tammy Baylis** 34:40 Yeah, cool, and yeah, as you've seen from our triage, there's always a ton of PR swimming around. If you don't, get attention on them, comment on Slack, or just come to these meetings just like you already did today, and… Yeah, looking forward to more from you. Thank you.
**Sajid Ali Syed** 34:58 Thank you.
**Aaron Abbott (Google LLC)** 34:59 Yep, welcome. Nice to see new people.
**Tammy Baylis** 35:07 Cool.
Anything from anyone else?
Oh, yes, Liudmila.
Please review PRs. Even if you don't have, like, the power of a green check, it always helps us to have more eyes, human eyes on PRs.
**Sajid Ali Syed** 35:25 Is it gated by a particular group membership, or anyone can review PR?
**Diego Hurtado (Dash0)** 35:31 Anyone can review a PR, And actually, review PRs is how you… We've managed to… Is the path toward becoming an approver.
**Sajid Ali Syed** 35:45 I see. Yeah, I was looking at the FastAPI, PR, for instance, and I saw that there was one person who asked the question, so I could go back and look at how fast API now natively exports OTL telemetry, then they want to deprecate it in the contrib packet, so I could take a look at that one first.
**Diego Hurtado (Dash0)** 36:07 Oh yeah, totally.
Go for it.
**Tammy Baylis** 36:21 Cool, alright, thank you very much, everyone, for another, weekly Python SIG meeting. We'll call that for today, and see you next week.
**Aaron Abbott (Google LLC)** 36:32 Cool.
Thank you. Bye, Tammy.
**Leighton Chen** 36:35 Which is one…
**Liudmila Molkova** 36:36 Thank you.
