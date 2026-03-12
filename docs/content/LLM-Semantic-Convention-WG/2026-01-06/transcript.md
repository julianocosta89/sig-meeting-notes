SIG: LLM Semantic Convention WG
Date: 2026-01-06
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:28 Hello! Hi, everyone!
Welcome to 2026!
**Aaron Abbott** 03:35 Hello?
Welcome.
**Liudmila Molkova** 03:38 Hello.
**Dat Ngo** 03:40 Happy New Year!
**Kipchumba Chelilim** 03:42 Happy New Year.
**Liudmila Molkova** 03:42 beer… So, it's been a while. Let's take a look at what we have in the project board.
New issue, per execution, judgment, and negative proof.
Do we… I'm not sure how to s- Call you. If you're on the call, please.
Come ahead, and dive into the agenda.
**Alex Hall** 04:19 Ludmila, you're not showing your screen.
**Liudmila Molkova** 04:21 Oh, I'm sorry.
Yeah, thanks.
Okay, I'm looking in this issue, and I… I have no idea what is it about. So I… maybe… And if Ankit is here, do you want to take a look? You've contributed the evaluations in the past?
I'm sure I'll get us here.
Okay, I'll keep it in the new issues until we have a chance to understand this.
What do we have in progress?
Okay, we have MCP in progress, and there is a pull request.
And it's approved.
Bye, you folks!
I'm still… Asking general audience to… for the approval here.
I have a draft of the blog, an early draft, I will send it as a pull request once I polish it a little bit.
In case it helps with the review.
Json schema definition for the GenAI I think there's still feedback, it still needs to be addressed.
Let's keep it… Open.
Cash tokens attribute. I didn't have a chance to take a look, but Alex, you approved. Nice.
I'm gonna remove the stale label… Oh, somebody just removed it.
Awesome.
Okay, this is on the Mii.
Okay, wee… I don't think we need to do anything else about the project board.
Does anybody want to come up and introduce themselves? This is just the way to learn who you are, what brings you here.
Anything you wanted to… Discuss.
**Kipchumba Chelilim** 07:03 Yeah, quick intro for me. Gip Chalalam, based in the US.
I am… recently did, work on an open source project, in the observability space called VSPR, and from there, I've just been really trying to get into OpenTelemetry, and in particular, have, gotten interested in semantic conventions and kind of the underlying you know, taxonomy and kind of tooling around observability for AI. So, looking to get involved and start contributing.
**Liudmila Molkova** 07:34 Wonderful, thank you. Which language do you work in? Is it Python?
**Kipchumba Chelilim** 07:40 Across, Python and Type, yeah, Python, TypeScript, and Ruby, for the most part.
**Liudmila Molkova** 07:48 Nice. You might be also interested in the Python instrumentations we have, maybe we will see some… yeah, we will see some PRs here, and if you're interested in contributing, and we have a lot of work to do, but also the… Work is usually… Styled under review.
So, if you want to, contribute, the best place to start is reviewing sample requests, and then people will appreciate it and review your pull requests back, hopefully.
**Kipchumba Chelilim** 08:21 Yeah, absolutely. Anywhere I can help out, happy to… happy to jump in.
**Liudmila Molkova** 08:25 Yeah, so what we discussed in this call are mostly things around top-end pull requests, there are some big discussions, or small discussions, and then if you see something interesting that, where you can provide a Some ideas, or just… just to humanize.
jump in. We would appreciate, even if you don't have a formal status or anything, we still appreciate COD reviews a lot.
**Kipchumba Chelilim** 08:50 Yep, absolutely. Thanks.
**Liudmila Molkova** 08:54 Thank you.
Anyone else want to jump in?
Okay, then moving on to the first topic, Ankit… Ankit, are you here?
He's not here.
Let's put it in the back in case he comes later!
Josh, retrieval span support. I'm so sorry, I didn't take a look. Do you want to?
Discuss it? Do… should we just use this time to review?
**Josh Winerman** 09:30 Yeah, I think it's just mainly a review from the last time we chatted, Lee and Mila. Just addressed every comment, hopefully.
**Liudmila Molkova** 09:38 Nice, let me take a look… so we get the new GenAI operation retrieval.
Search Vector Store API… And we have a document.
We have examples here.
And we have a schema for them, right?
Here, yeah.
**Josh Winerman** 10:09 Yeah.
**Liudmila Molkova** 10:11 And we have a retrieval query.
text.
Okay, on the first… Site that looks good.
I'll probably take a look at some minor details.
But… Looks good to me, in general.
**Josh Winerman** 10:41 Okay, yeah, sounds great. Feel free to, to leave any other comments, and I'd be happy to address them.
**Liudmila Molkova** 10:46 So if I approve it, so the way we… try… what we tried to enforce in semantic… okay, there is an implementation.
Right, we have a prototype for this.
And you intend to essentially repeat what OpenLeetry did here, right?
**Josh Winerman** 11:11 Yep.
**Liudmila Molkova** 11:14 Okay.
Okay, thanks, I'll take a look. Does anybody else wants to take a look?
Silence. Okay.
Thank you, Josh. Surya, Anthropic Sync Messages.
Do you read… U.
**Surya Teja** 11:43 Yeah.
Yep, so this is instrumentation for the messages API that Anthropic has. For keeping it simple, I… just wrote the sync messages, but I don't know why, but it got bloated.
Along with this, I just broke the pattern and added some integration tests, which are going to run only if the SDK's key is available, and they're not going to run on the GitHub Actions runners.
Just to see if everything is working fine or not. Everything passed smelly test on my side, but But just wanted to get your reviews. And also, I guess I was working with Aaron on the side to… get it reviewed, and he suggested me to use telemetry Handler that Keith implemented in Gen AI Utils.
So the first, I started using that, and everything is working fine. The only, Blocker is we don't have a… logged event captures in this telemetry handlers. There is one more PR that is adding it.
if we have time, I want to add… I don't know if that is added in this list or not, but I'll add that also, and that also needs a review.
**Liudmila Molkova** 13:02 You mean, I think it's from Mingkhoi, right?
**Surya Teja** 13:05 I'm sorry, I don't know how to pronounce his name perfectly, so I just don't want to butcher his name, and… Create confusion.
**Liudmila Molkova** 13:14 Yeah, okay, let's add it to the agenda, but yeah, So, you're using the handler here, and…
**Surya Teja** 13:22 Yeah. Done.
**Liudmila Molkova** 13:23 this is a great suggestion, but… And… It will take care of a lot of things, Is there some discussion? You mentioned it was blocked?
**Surya Teja** 13:45 I don't know if it's blocked, but, just, pop.
as far as… Aaron can pitch in and tell me if it's blocked or not, but yeah.
I don't know if we got some time to look into it or not, but I tried to resolve all the… Comments and edit them.
**Aaron Abbott** 14:04 Yep, so just one question was, the thing that you said was missing from Telemetry Handler, did you kind of manually implement in this PR, or…
**Surya Teja** 14:15 No, Aaron. I was waiting for the other PR that I mentioned, which… I don't know the… I don't know how to pronounce the person's name.
He is working on it, and when I spoke with Keith.
Keith told me that he will be coming to this meeting for getting this prioritized and added.
So that I can pull in those changes once, this is merged.
So… I just want to, first get my Anthropic, PR reviewed, and also prioritize the other one that, That was on the screen, the other PR.
So, we can send that, and the next PR that I work on, I can add the logged events also.
**Aaron Abbott** 14:59 Yep, that sounds great. Yeah, I, I can take a look. I had one other question about, like, you mentioned the integration tests.
We're different from the other stuff.
It looks like you do have, like, those VCR cassettes, so I was curious what you meant by that.
**Surya Teja** 15:16 Yeah, so the reason why I added integration tests were to just see if all the semantic stuff were being captured or not.
I mean, in, in the Java land that I work on, I… we usually use, what do you call it as, some test containers for testing if everything is working fine or not. So I wanted to follow the same pattern, and, add the integration tests over here, and I, think, I don't have an API key, and I don't want these tests to be blockers when it is running on GitHub Actions, so I tweaked them to run only if the API key is available, and not run them if API keys are unavailable.
**Aaron Abbott** 16:01 Okay, yeah, I mean, it makes sense, but I thought with the cassette-based tests, there's, like, a reload flag that you can pass to the… to the PyTest extension, which would make it run against the real API as well. But do these have different assertions? Is that… is that kind of the point?
**Surya Teja** 16:16 Yeah, they have a little bit of different assertions and stuff.
**Aaron Abbott** 16:21 Okay.
**Liudmila Molkova** 16:22 I'll take one.
Curious w-why? Why?
Why is it important? I mean, I don't have objections, I'm just trying to understand why is it necessary.
**Surya Teja** 16:36 it's not necessary, but I just added them because in Java land, we use test containers to test it, so I was not familiar with how Python does it, so I manually wrote all this to see, if the API is track… is traced perfectly or not. So that's actually because I was not familiar with Vcr casset stuff, can do that.
But, if, that is not needed, I can remove the integration tests and just keep the VCR casset tests.
**Liudmila Molkova** 17:08 So what we do in other places, we have this VCR test, which is… It's a recorded execution against Anthropic or whatever API, right? And then, when the test is run in actions, the test has no idea it cannot access Anthropic, but the HTTP requests are just replayed back.
And you could still assert whatever span or metric attributes and anything you… we do.
the only difference against the real integration test, that you're not actually hitting the current entropic API, and if they change It would not be, tested. But here, it wouldn't be tested Either because… somebody needs to write it with entropic API key to detect.
**Surya Teja** 18:00 Yeah.
**Liudmila Molkova** 18:01 has failed.
**Surya Teja** 18:02 Yeah, yeah, I know that this is a little bit foolish, on my side to add it.
Yeah.
But I can remove this if you guys think that this is an anti-pattern, and hmm, not needed.
**Liudmila Molkova** 18:17 It's not anti-pattern, but I think it's… it's not needed, and it can be confusing. It's one more thing to maintain without… that actually is not validated by any means.
And if you… if there are some checks that you would want to run that are not included in the cassette tests, I think you should move them over to the cassette tests.
**Surya Teja** 18:39 Yep, okay, agreed, I'll remove this, and, you know, if anything that is not being asserted in the casset test, I can move to a gassert test.
Yeah.
**Liudmila Molkova** 18:48 Thank you.
Okay.
Should we, take a look at this other PR for the inference events?
Since we're already talking about it.
**Surya Teja** 19:12 Yeah, I would be grateful if you guys can take a look at it, and hmm… add any comments or anything, so that I can work with the… Work with the PR, guy to get this merged.
**Liudmila Molkova** 19:26 Yeah.
I… I think this, this, this flag is not necessary, right? We control it with something else.
R.
Aaron or Dylan, do you remember what we call it?
**Aaron Abbott** 19:48 Yeah, it's, it's in the util also, like, the, along with the telemetry handler, but it's… Yes, this one. Copture message content.
**Liudmila Molkova** 19:58 And it has multiple values.
**Keith Decker** 20:03 I think that flag that he has there isn't for the content itself, it's whether to emit an event or not.
Because we… in that PR, we're already checking if the message content should… Should be omitted or not.
But that other flag is… is if the whole event goes or not.
**Liudmila Molkova** 20:31 capturing, oh.
**Keith Decker** 20:38 And go take a look at that again, though.
**Liudmila Molkova** 20:42 So, I… Hoped we could reuse.
So we have this, capture.
Content.
And it… it's… it's an enum.
And it has… Or values, I think?
the… non-span event and span an event.
So we want a separate flag to control whether event is created at all.
Do we need it?
**Keith Decker** 21:33 Yeah, I'm not… Sure on if we need that one or not, because he is using the… the span content one in order to tell whether to put the messages in there.
**Dylan Russell** 21:54 Do we normally have, like, an environment variable to control whether… Something is emitted at all.
**Liudmila Molkova** 22:05 Normally not, but nothing is normal with this event. It's like a… it's a event representation of span, right?
Well, the details on the spend.
**Dylan Russell** 22:24 Thanks. It's gonna do it for me.
**Keith Decker** 22:55 So there was feedback on what you're putting there at one point in the PR, and the feedback was that the event should be emitted even if the… Capture message is set not to.
Because the event might still be useful, even with nothing in there.
So I think that's why that flag was created.
**Liudmila Molkova** 23:17 might still be useful. To whom?
**Keith Decker** 23:20 Yeah, let me.
**Liudmila Molkova** 23:21 Is there, like.
**Keith Decker** 23:23 Let me see who that made that.
Comment.
Because I think that PR started with checking that flag and then just not doing the event if…
**Liudmila Molkova** 23:42 Oh.
Nealon!
**Dylan Russell** 23:44 Yeah, so… We still have the other attributes on the event.
Like, we put, like, the tokens and, like.
**Liudmila Molkova** 23:55 Oh, they are available in spans. The event is essentially a duplicate of SPAN in case somebody wants to record it without sampling.
I mean, there is a world where I can… I can see your point. It's just, is it a practical point, or it's a theoretical one?
And if it's a seretical one, can we address it?
If we get, somebody with this problem.
**Dylan Russell** 24:38 I don't know, it seems… it just seems… Like, so this flag is gonna control, like, message content, and also whether the event is emitted at all.
like… Like, for other instrumentations, do we usually have, like, a flag to control?
Like, whether an event is written at all.
Don't we usually just, like, the instrumentation's… Decide what events and spans are written, and… like… Do we have flags to control those, usually?
**Liudmila Molkova** 25:18 We don't have instrumentations that emit… emits immediate events.
**Dylan Russell** 25:24 Hmm.
**Liudmila Molkova** 25:25 Mostly, the only event we might meet is exception on a regular basis.
And it's somewhat special. The way I could see it is that, It's actually the verbosity that controls it, and maybe there will be a configuration that allows to enable or disable events by name.
So the… there is this logger config where it could be that there is a list of disabled events, let's say, or some other configuration, the regex that enables events by name.
And… But it's, it's not, it's not there yet.
And I think there will be means to control it that are generic.
And by guarding this behind this flag, we kind of leave the room open to… Other options in the future.
**Dylan Russell** 26:30 Okay.
Yeah, it seems it… It is weird to me to not write this event if this… because the flag is for, like, content capture.
Not, like… I don't know, just the way it's named, it seems, like, weird that you would not write the event, given one of these values.
**Liudmila Molkova** 26:58 So let me try to convince you. I'm a user, I want to write events.
I want to enable So I'm just enabling event with a Boolean flag. I see the same content as on the span, and I need to… which makes little sense.
And then I need to… enable another flag.
This capturing mode, to also have a content on event.
So, as a user, I, I do… I need to configure two things.
At the same time.
And it's a much harder thing to do.
**Dylan Russell** 27:43 Yeah, maybe if you're a user that just wants it disabled, it's maybe a little more annoying.
**Liudmila Molkova** 27:50 If you use a… you're a user who wants it disabled, it's just… it's disabled by… Default?
**Dylan Russell** 28:00 Right.
So if you don't set the flag…
**Liudmila Molkova** 28:03 Yeah.
**Dylan Russell** 28:09 Yeah, I don't know if that's good.
Because it defaults to no content, right? And so you would not get the event.
**Keith Decker** 28:22 Is there a use case where you would want… The event, but you want the inputs masked, and using this content capture to do that.
**Dylan Russell** 28:32 I think so.
Because, I mean, I've already hit that in some other instrumentations where they want the…
**Keith Decker** 28:40 The log to come across, but… Don't want the user content in the log, just that it happened.
**Dylan Russell** 28:48 Yeah, exactly.
**Liudmila Molkova** 28:49 What… why do they want it? It's on Spence.
**Keith Decker** 28:53 Well, this was a pretty… Weird use case, but they wanted the log to come because they had some other, Dashboards that showed… they were counting logs, but… They didn't want the actual content for security.
**Liudmila Molkova** 29:09 They can count spans pants.
**Dylan Russell** 29:11 Yeah, okay.
Well, at least for, like, Google, we have different system stores, like, logs and spans.
So you might want, like, it on the log. You might want… Yeah, you might want it in logs and not spans.
**Liudmila Molkova** 29:28 So then, this argument works if it's just on the log and not… if it… it's a log.
Then all spans should be logs.
Because it's the… then a duplicate of a span.
**Dylan Russell** 29:45 Hmm…
**Liudmila Molkova** 29:46 So why this specific span they want as a… also as a log?
And not others.
And why, like, I understand there are custom needs of applications, but we are trying to address the thing that makes sense. The choice here is to make onboarding complicated for everybody.
To support this weird use case for somebody who wants to count things from the logs. Or we can make it reasonable for everybody, and have still means to enable the scenarios in a generic way in the future.
**Dylan Russell** 30:39 Yeah, I'm not sure.
**Liudmila Molkova** 30:45 What, what, what… Makes you hesitant, like, okay, it's weird, a lot of things are weird, but the user experience is better. So what you're not comfortable with?
**Dylan Russell** 30:59 So… We're saying overload this flag to say… Like, no content means no event, right?
**Liudmila Molkova** 31:10 Yep.
**Dylan Russell** 31:12 But I think users want the event, but not the message content on the event. How would they do that?
**Liudmila Molkova** 31:21 Not possible yet. If they come… if they really want it, they will come and tell it.
**Dylan Russell** 31:30 But…
**Liudmila Molkova** 31:30 Or, or, let me put it this way, it makes the configuration, where you say.
enable content on the event, and not emit event.
Makes no sense.
**Dylan Russell** 31:46 Yeah, that makes no sense.
**Liudmila Molkova** 31:51 So then, we don't provide the… No, to turn it on individually, but when somebody already said they want content on the event, it obviously means they want an event.
**Dylan Russell** 32:05 Yeah, I agree with that.
**Liudmila Molkova** 32:09 So then, as a first step, Could we… at least… I don't really care about whether we introduce the knob, the first knob or not, but if we just always submit event, if somebody picked the capturing mode to include event.
**Dylan Russell** 32:29 Yeah, I'm okay with that.
**Liudmila Molkova** 32:31 Okay, thanks.
And there's probably an edge case when… They explicitly… turn this off? I don't know, we can… we can erode.
**Keith Decker** 33:36 I guess for that specific use case, where they want the event emitted, but want to redact the content, they can use a processor on the collector.
**Liudmila Molkova** 33:48 And they… they can, but everybody would be happier if… if they just used pants.
Sorry.
**Keith Decker** 33:57 Fair.
**Liudmila Molkova** 34:01 like, they're… they're doubling the volume of these things. Why? Just because their dashboard, like, logs more?
I've lost the place where I was commenting, I'm so sorry.
I'll write it after I've lost it.
**Keith Decker** 34:33 I've got it at the bottom of your agenda there, the PR, so you can either get out of there.
**Liudmila Molkova** 34:38 Thanks.
Okay, thanks.
Nice dive into the nerdy things.
I have an old PR I would like to get some eyes on. It's kind of a trivial one, we didn't… Mark… attributes that are… may be important for sampling and should be provided at the start time as sampling relevant. That's what we do in semantic conventions, usually.
These are the attributes that are available at start time, and you could say, for example, I don't care about the… create agent spans, using, let's say, operation name. You can say, I don't care about calls to, I don't know, local host.
If I host local model locally, or maybe I don't… care about specific model. It's somewhat theoretical, but people actively use the sampling to optimize costs and reduce their telemetry volume. So this just codifies, what Should be provided at the start time.
No substantial changes here, and I would appreciate your review.
Okay, what else do we have here?
Unkit.
Closed now…
**anksing** 36:36 Yeah, unfortunately, it got close due to inequity, and I have… I couldn't find a way to kind of reopen it. So do I need to create a new one, or… No, no, please don't, okay.
**Liudmila Molkova** 36:50 Do… like… I… I did… I wasn't following what… where are we at? What do we need to discuss?
**anksing** 36:59 Yeah, so I think there were two open… major big open questions that came up. One was, like, how do we represent the built-in tools? Should we break it down into multiple parts for request and response, or could it be just one structure that kind of represents the entire thing, so I'm kind of putting together information from, Cloud, Gemini, and OpenAI, to kind of help make a decision there.
So, I'm not quite, like… there I found, like, there's a mix, kind of… mixed ways where it's being done. For some tools, it's broken down. For some tools, it's not. So, depends on the tool as well.
So that's one question that I'm working on.
And then… Let me see… I think it was my mind. Let me just open it up.
Yeah, and then I think the second one was about, like, is there a generic enough way to represent something like a code interpreter?
So, I think that I feel probably can be a part of a different PR, but I'll, I'll gather some more information on that, because I was trying to compare, Built-in tools from a different provider.
Yeah.
**Liudmila Molkova** 38:34 So, essentially, you're still working on the polishing of the details. We wanted… we had some action items from the previous discussions, and you're still.
Figuring it out, right?
**anksing** 38:47 Yes, yes, yes, that's it.
**Liudmila Molkova** 38:50 Anything we can do here?
**anksing** 38:52 No, I'll probably… I'm gonna post my findings today. I couldn't finish them.
So, once I… once I finish those findings, I'm gonna share that and link them in the PR as well.
It works and take a look, and we can help make a decision.
And move forward, and that'll be great.
**Liudmila Molkova** 39:16 Awesome.
Thank you, and we already talked about this one.
Right. Cool.
I… I have a couple of items I wanted to bring up. Does anybody else wants to talk about anything else?
Okay, I've made a stab at, switching… Okay, I had a long time, For requests for up in the IV2.
To meet different conventions side by side. It, I wanted to use GenAI UTLs for this.
And, I found that there are a couple of things that are missing.
Okay, nice. There are no concerns yet. There are… we didn't provide server address and server… port?
And we didn't allow… Additional metric attributes, to be recorded.
So… what I've done, I've added, the metric attributes to the invocation.
And they would normally apply to metrics.
And these attributes would only apply, or… Only applied to spans and events.
So I would appreciate folks to take a look.
Thank you, Josh, right? Already.
Approved?
**Aaron Abbott** 41:29 Yeah, I can take a look at this one.
**Liudmila Molkova** 41:35 Thanks.
**Aaron Abbott** 41:36 Yeah, Keith, would you mind taking a look? Also, just since…
**Keith Decker** 41:40 I'll go take a look.
**Aaron Abbott** 41:41 Awesome.
**Liudmila Molkova** 41:44 Yeah, thanks. And, once it's, in… I will… Switch to… I will, undraft this one, and we can, follow up.
Here.
Okay, another thing I was going… I was playing with, over the holidays, and it should be in my fork. I will be doing more… around the space, I think we… a lot of the PRs are blocked on reviews, and one of the reasons I don't feel comfortable approving is because I don't… I want to Check how compliant it is with semantic conventions.
And… I want to automate this.
And I've made this tab… at this Viz Weaver, it's kinda early, And it's not perfect.
But I'm curious what you folks… Think.
So what we can do with Weaver?
we can… Sandweaver is OpenTelemetry's semantic convention tooling that allows you to write conventions, validate conventions, generate some parts of the code, and it allows to validate telemetry against definitions.
So, if I, let's say, use OpenAI, or whatever else, I just write my test regularly.
And… I sent telemetry.
to Weaver, overall TLP.
Weaver?
when it receives, let's say, a metric, let's say its operation duration, it knows the definition of this metric, and it can say, oh, okay, this attribute is required on this metric, and it's not present in this data point, so let me, violate on this. Let me complain.
It's less cool for spans, because there is no means to identify a spend in the stream of spends, which is a gap, and hopefully we will solve it one day, but it's not possible today.
But at least we can, automate validation of metrics, and also maybe logs, but… oh, sorry, events. We can also do something for spans. It's less cool, but it's still possible.
So, what I'm doing here. So, I'm setting up Weaver. I have a… abstraction of a Docker container to simplify using it.
And, I just started in the contest.
So it's just the normal part of, hotel setup.
And… the only thing I do here is… I provide Weaver or OTLP endpoint.
It's running… it's starting here locally as a Docker container.
this guy, is here.
What we set up is… the… Policies, we'll take a look in a sec.
And this is for reporting. I hope we… it's just some internal kitchen we probably don't really need to care about much. And then, yeah, we start it, and essentially we stop it. So what happens under the hood?
When Weaver starts, it listens to the port, it listens to the telemetry, it runs this… all the standard checks, like what I mentioned, okay, this metric Is received and it has these attributes, does it include all the required ones and such?
This guy, it's an additional policy that we can write. They are using language called Rigo, defined for defining the policies. It's kind of awkward, but it works.
So here, we can validate spend specifically, because this is how we will do this.
So here, we, let's say, say, okay, this is a span, we're evaluating a span, and we are going to expect the inference span.
And if… if we don't get inference spend, but get something else, we will… Louis will complain.
Yeah, so if it's not one of the inference operations, we're going to, return a violation.
We're also validating that all the expected attributes are present, and there are a bunch of Effectively tests and checks written here, for example, for the spend name that's not… not formatted correctly.
Once we are done, it will write… it will use this template to write a report. What's important?
To know you will have a full report, which is kind of large, and there will be a short report with violations only if something fails.
And then, eventually, the test… Will fail.
And you'll see what exactly the violations are.
I have a bunch of questions I'd like to… discourse with patent folks.
We can probably do it here. Yeah, Aaron?
**Aaron Abbott** 47:35 Yeah, could I just ask, this is awesome, first of all, I really wanted this, so it's super cool to see, and thank you for working on it.
So I had a couple questions, like, first, does the REGO policy, Is it just kind of run all the rules every time, so you have to do the filtering?
On the telemetry there, or can you kind of select Which rule to run, somehow, from the test.
**Liudmila Molkova** 48:01 You can select which rules to run, you're setting it up.
When you set up Fiverr, you, you give it the… oh, sorry, the list of policies. So I would imagine We would say, okay, this is the inference policies.
Or this is the embedding policies, if we want to.
I… I really hope we don't need to write that many, because at some point, we will make Weaver understand how to match spuns.
**Aaron Abbott** 48:32 Yup.
**Liudmila Molkova** 48:32 But yeah, you can provide custom policies.
**Aaron Abbott** 48:37 Okay, and then I was gonna ask, like.
Is this a general issue with the way we've kind of semantic convention specified spans, that there's no discriminator?
Or is it specific to Gen AI, or just, like, spans across the board?
**Liudmila Molkova** 48:52 just spends across the board, that's more even a spec issue that we don't have any… any identifiable characteristics of SPANS.
**Aaron Abbott** 49:01 Yup.
Okay. Is… is there, like, an issue for that already?
**Liudmila Molkova** 49:06 Yeah!
If you can just comment on this, that this is a… a deal, or, I don't know, sums up, it would already help, because at some point, we will need to make a claim to the spec and push for solving it.
**Aaron Abbott** 49:24 Dale.
Yeah, I mean, this has been really annoying because, like.
We're kind of using the GenAI operation.
Name for this, but… It's also not… completely set in stone, like, people can set their own values, and it feels really overloaded, but… Also, I have, you know, people internally be like.
how do I identify that this is a GenAI spend? I'm like, well… you'd have to write some pattern matching right now, which is pretty much what the Rego is doing, I guess, so… Yeah, I can definitely leave a comment on this one. That's, That would really help here.
Yeah, and the last question, I'll wait for you to fill.
Yeah, the last question I had was, Regarding the, like, structured stuff in the JSON schemas.
Is that covered at all here?
**Liudmila Molkova** 50:26 No, not at all. This is a great point. So, how I think it should work is that we're… could… ads.
Describe… we could have a way to describe structured, not in JSON schema, but in whatever Weaver understands. It does not understand it yet.
And then the Beaver would validate compliance.
I mean… It's probably quite a bit of work to make it happen.
there are probably easier ways. Like, for example, what we could do, we could provide some annotation. It's possible today in the semantic conventions to say, okay, this follows that JSON schema.
And if we could use some external tooling to hear in the tests.
to… check.
if it complies with the JSON schema, I imagine… it's… All the pieces are there, it's just a question of plumbing them together.
**Aaron Abbott** 51:38 Yeah, yeah.
Yeah, I think… I think it would be valuable, You know, like, we don't need to… Doesn't need to be super, super detailed, it's just, like, even… identifying keys and stuff like that, and as we kind of do custom stuff in Gen AI, It feels really challenging, both as, like, a reviewer, and if you're trying to do automation to… to validate something is following the convention, so… Yeah, I think, I think this is awesome, I am a little worried. I think the… the JSON schemas we have right now are… how do I… how do I say it? It's like, I think in some cases, they just kind of evaluate to any.
Because of the way that we find generic parts, so we'll have to, probably fix that, but it's kind of a separate issue.
**Liudmila Molkova** 52:29 Yeah.
Yeah, so I'm going to create, An issue from what you mentioned first, and if you want to create an issue for just tracking.
Have we used any? And, like.
making our schemas more specific, it would be great. So what I want to do is… Gen AI in that, structured… contributes, and… application. What is JSON schema?
So today, we just have it in the plain text. We could make it more structured and have access to it.
Great.
Cool. So, Aaron, do you want to… I have some Python-specific questions, can we spend a few minutes talking about them, or…
**Aaron Abbott** 54:19 Yeah, definitely.
**Liudmila Molkova** 54:21 So, I'm doing something stupid, probably.
But what I want to do is… I want to… has… Helpers, like this one.
somewhere in Python contrib.
I think it's not Gen AI. I think it should go somewhere in the general… Tales.
Do we have some task tutorials that are shared across different leaps in Python Contrib?
We have one in the, core repo.
Oh, I see.
I see. So we would… Probably put it here. Oh, here, I see.
**Aaron Abbott** 55:09 Yeah, I think we could do the same thing in Contrib if we don't have it. It actually might be there already.
I can check, also.
Or if somebody else on the call knows.
**Liudmila Molkova** 55:29 We have desk tests.
and Docker tests, but it's not… oh, the UTIO. I can put something… Like, like, here in the root, and then… But it wouldn't be… wouldn't be, like, a module-based.
**Aaron Abbott** 55:47 Yeah, you can kind of copy what we have in the core one.
I just… put it there, or I could put it in the meeting notes.
Yeah, it's a little awkward, because, I think we… we published the test utility one in Core, but that's not, like, a requirement, so we can have just, like, a test library that's reused, But with the kind of setup we have with the talks, you'll have to kind of go and manually add it, which should be pretty straightforward.
**Liudmila Molkova** 56:17 Okay.
Okay, so let me then explore this and make it more similar to the repo. The way I use it today, I imagine it's not how you want it to… to be. So what I do is… Just temper the pass, and then… Yeah.
This is not a good way, you wouldn't embrace it.
**Aaron Abbott** 56:40 No. Yeah, I think if you can add it in, like, as a package, and then add it to Talks so that it installs, that would be great.
**Liudmila Molkova** 56:48 This is just, like, a painful point in the Python.
**Aaron Abbott** 56:52 ecosystem, unfortunately.
**Liudmila Molkova** 56:55 Okay, cool.
Then… I'll keep playing with it, and hopefully we'll get some more or less easy, easy validation in the future.
We are pretty much at time. Anything else we can cover in the 4 minutes we have left?
Done. Thank you all.
Glad to see you, and looking forward to a great year together!
**Aaron Abbott** 57:30 Awesome, thank you, thank you all.
**Liudmila Molkova** 57:32 Thank you.
