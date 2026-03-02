SIG: Ruby SIG
Date: 2025-10-21
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Kayla Reopelle 00:00:22 Hello.
Wendy Smoak 00:00:24 Thank you.
Kayla Reopelle 00:00:43 Hey, Hannah.
Hannah Ramadan 00:00:47 Are you guys?
Kayla Reopelle 00:00:50 doing all right.
Alright, I have to leave today at 10.40, just so you guys know, or at least switch to my phone at that point, if we're still having a discussion.
I can share my screen to start, though. I don't really have much of an agenda.
I just wanted to chat about the…
metric slogging about export, PRs.
Is there anything else that people wanted to talk about today? Oh, hey, Arielle!
Ariel @arielvalentin (ATX, USA) 00:01:54 Hello! Long time no speak.
Kayla Reopelle 00:01:56 Yeah!
Great to, great to see ya!
Ariel @arielvalentin (ATX, USA) 00:02:04 Great to be here for, like, the first time in months.
Kayla Reopelle 00:02:07 Yeah.
Hannah Ramadan 00:02:08 Hell yeah, hey, Aria.
Ariel @arielvalentin (ATX, USA) 00:02:10 How you doing, Hannah?
Kayla Reopelle 00:02:17 All right. Well, yeah, we don't have much of an agenda. I saw that the release is getting set up for Ruby 3.1 Rails 7.1 dropping. Is there anything that, in particular, you want to talk about today? Do you want to lead with that, or…
Ariel @arielvalentin (ATX, USA) 00:02:33 Oh, me?
Kayla Reopelle 00:02:35 Yeah.
Ariel @arielvalentin (ATX, USA) 00:02:36 Oh yeah, so I think we can apply that same thing to the SDKs when, we get them rolled out.
But I don't…
I've got somebody from GitHub trying to contribute a new instrumentation, and we're kind of working.
Kayla Reopelle 00:02:49 came through.
Ariel @arielvalentin (ATX, USA) 00:02:51 some of the details. There's a person, their handle, I think, is, like, Thompson Tomo?
Kayla Reopelle 00:02:56 Oh, yeah. Yeah, I've seen that around.
Ariel @arielvalentin (ATX, USA) 00:02:59 They've been actively engaged, they're engaged a lot in the semantic conventions repo, so I feel like.
This person is a good, asset for, like, they've been looking at
PRs and, looking at semantic convention-related things, which is really nice.
Kayla Reopelle 00:03:16 Huh, yeah.
Ariel @arielvalentin (ATX, USA) 00:03:17 and again, my limited capacity here is just trying to help out with maintenance right now, and…
Encouraging the community to collaborate and participate.
Outside of my team, so…
I was glad to see another hover contributing to the repo.
Kayla Reopelle 00:03:39 That's great.
Yeah, I feel like Thompson Tomo's made a lot of great contributions, or at least, like, starting to, with the race car instrumentation as well, and trying to get the messaging semantic conventions up to speed.
So, that's awesome! That's great to hear that he's involved.
Sorry, I just kind of circumvented the agenda, because I was so excited to see Ariel. There were things to talk about in the spec sig, though, and
The spec sig today was a bit of a… A heart-to-heart on…
the structural problems related to OpenTelemetry in terms of…
you know, messaging about stability, stability of features, how the product of OpenTelemetry is reliable and not reliable in people's environments. And it was kind of the starting of a bunch of different discussions that will turn into four OTEPs over the next few weeks.
These are all points that OpenTelemetry, you know, at the GC level wants to address, and
Try to remedy in their goal to become more stable, to actually have the project itself graduate from an incubating state to a graduated state.
So, I think if you…
have perspectives on this, have opinions about this. You know, some of the things that they put on the table were maybe freezing the spec to try to help, you know, all the SIGs catch up and, have all the features implemented that are actually stable.
They also talked about, you know, maybe focusing on one particular feature across all of the SIGs to try to get more stability there, and then kind of build in other areas.
They're also looking for end-user feedback, I think, to make sure that the things
The new processes that they're trying to put in place will actually benefit users in the ways that they hope them to.
So yeah, so keep an eye out for those, no links to OTEPS yet, but hope to report that more next time.
Wendy Smoak 00:05:58 What's the fourth one?
Kayla Reopelle 00:06:00 The fourth OTEP?
Wendy Smoak 00:06:02 Yeah, there's three. The fourth bullet is blank.
Kayla Reopelle 00:06:05 Yeah, I don't know.
Maybe there's only 3.
Maybe it's the spec phrase?
I was not…
Wendy Smoak 00:06:14 Yeah, I don't know, I just was…
Kayla Reopelle 00:06:17 Yeah, great question. Austin did have 4 clear OTEPs, but I forget what the fourth one is.
So, let's see, then… the next thing that was discussed was kind of around declarative configuration and enabling
disabling things and what the defaults should be. We're not really there yet at declarative configuration, so this doesn't really impact us right now.
And then there was also a question about…
Zipkin compatibility, and, this was just a tag-on at the end of, like, maybe even checking in to see how many people are still using Zipkin, to determine if it should stay up to date with the latest SUMCOM, or if we, as an org, should kind of encourage people to use OTLP instead.
And the final point was they're creating this unconference in Belgium.
If anyone is interested in going.
the intention is to kind of connect with OpenTelemetry users and connect them with maintainers in person, so it sounds like the event itself is still being worked on, but, yeah, wanted to shout that out, too.
So, nothing too meaty on the actual, like, spec side today.
Okay, well, I guess then let's hop into this, metrics logging about…
Ariel @arielvalentin (ATX, USA) 00:07:50 Sorry.
Kayla Reopelle 00:07:51 Oh, yeah.
Ariel @arielvalentin (ATX, USA) 00:07:52 I did have a thought about feedback for Upstream. One thing that… I find particularly challenging.
Is keeping track of the changes to the specification.
Knowing if we've implemented ours.
Kayla Reopelle 00:08:08 So…
Ariel @arielvalentin (ATX, USA) 00:08:09 from a project management perspective, it would be ideal if, say, like, when an OTEP was merged, that issues were generated.
and that different, SIGs, or different language implementations, or whoever it corresponded that OTEP to.
Would it be tagged as part of it, and potentially create sub-issues?
We don't have to do… we don't have to do, like, issue proliferation, but it'd be ideal to give a heads up, because it's hard to keep track of, say, like, oh,
we…
some spec change came in, and we are doing that now, or we've adopted that piece. So that project management portion is a little bit tough, and then sort of, like, the… if there's a certification process, like, we used to have somebody who can come in.
I thought it was Carlos, I think the person's name was Carlos. Originally, we tried to go 1.0 for the SDK and the API, and they walked through, sort of, a certification to let us know, yeah, we are meeting that spec, and I don't know if there's some automation that could be introduced.
to say… There are…
you know, the Ruby SDK satisfies all of these features, because there used to be that… there's that feature matrix that says, hey, you know.
Kayla Reopelle 00:09:23 Yeah.
Ariel @arielvalentin (ATX, USA) 00:09:24 as you're required to have this and that. What sort of compatibility we would have, including, you know, included in our versioning in addition to that, right? And then there's, like, as you mentioned already, there's all these other big projects that we don't have kind of spec'd out and issues. So when somebody came along and said, how can I contribute?
We didn't have the issue that said, hey, look, we need to have, programmatic, I'm sorry, not, declarative configuration with the YAML file support.
Kayla Reopelle 00:09:53 Yeah.
Ariel @arielvalentin (ATX, USA) 00:09:53 or, you know… or Schwan has been, like, had that PR open, I think, still for a very long time for the…
The instrumentation, the… no-to-operator instrumentation for the automatic instrumentation, right?
Kayla Reopelle 00:10:08 I think we got that merged.
Ariel @arielvalentin (ATX, USA) 00:10:08 Or is it…
Kayla Reopelle 00:10:09 Oh, that got merged in? The zero code one? Awesome.
Xuan Cao 00:10:13 No, no, no, it's not, yeah, because some of the test cases,
not a bridge, so I'm still trying to… Mexico.
Ariel @arielvalentin (ATX, USA) 00:10:22 Salvo.
Xuan Cao 00:10:23 Lord.
Yeah, yeah, yeah.
Kayla Reopelle 00:10:25 But we did merge in the initial PR, or is that still open, and I'm just imagining.
Xuan Cao 00:10:30 No, no.
Kayla Reopelle 00:10:31 Nevermind, never mind.
Ariel @arielvalentin (ATX, USA) 00:10:33 And then, you know, and so it's like, I think that,
That's the hard part about being a maintainer, is that we have to do a lot of the work ourselves to try to…
Kayla Reopelle 00:10:42 Damn.
Ariel @arielvalentin (ATX, USA) 00:10:42 Keep up with what's going on.
I'm sure that we could leverage, even us, we can probably leverage some tooling to say, like, hey.
some generative AI thing? Can you create a bunch of issues for me that, like…
Kayla Reopelle 00:10:56 Yeah.
Ariel @arielvalentin (ATX, USA) 00:10:57 You know? Yeah. Based on what's missing in our code here?
do we… do we satisfy the spec in some way? You know…
To… to try to, you know, try to mitigate some of that.
I see Wendy's got her camera on, so…
Wendy Smoak 00:11:19 No, I just finished lunch, so I turned it on. But yeah, this is all good, because we had someone wander by recently and say, I'm at a retreat, what can I help with?
Kayla Reopelle 00:11:27 Mmm.
Wendy Smoak 00:11:28 really clear.
And then, yeah, I was just listening to… they did a What's New in Hotel, and they were talking about the declarative configuration stuff, and it's like, that's neat, but where… where do you… where… where do you start? Like, what… I don't even…
Kayla Reopelle 00:11:42 Yeah. And the one I opened for the…
Wendy Smoak 00:11:45 You can have metrics about the metrics.
Kayla Reopelle 00:11:47 Because…
Wendy Smoak 00:11:47 I found it over in Python, and someone pointed to the, like, here it is in the spec. It's like, okay, we should do that. But again, like, I… how would one even start? Yeah.
Ariel @arielvalentin (ATX, USA) 00:12:00 And we have our… we have, like, our bespoke one that we wrote, you know, had included from the very beginning, that was more of, like, a…
like, a key-value pair kind of thing, an event-oriented one with that metrics reporter, but still, that's, like, off-spec, right? We're just, like, adding stuff ourselves to this thing.
So that you can track metrics yourself, and… You know, there's a…
as you pointed out, Wendy, it's like, there's a lot of useful stuff that our end users ask about, like, how do we…
How do we get that minimum baseline of really good, like, really good stuff in there?
Wendy Smoak 00:12:40 And the other… so that was one… it's just been one of my questions, like, I find something… am I, like, am I supposed… am I allowed to open? I mean, now I've been here a while, so it's okay, but when I first came, it's like, am I allowed to open an issue? This is not already in the issue, it's just someone managing this? Yeah. Like, how does this even work?
Like, communicating more, and, like, getting people more involved, and…
Catch them as they wander by, and try to get them to help, because if they wander off, you may never see them.
Kayla Reopelle 00:13:08 Yeah, great point.
I don't know if we have a contributing guide in the core repo the same way that we do in the contribib rep repo. I think the contribib rep repo has really good steps on… that explain, like, what you can, or how to help.
And maybe we need to add that as well to our core repo.
But.
Wendy Smoak 00:13:29 There's a contributing…
Yeah, it's just basically how to get the…
Please read the contributor guide, and then how to get… fork the repo, and that sort of stuff.
Kayla Reopelle 00:13:46 Okay.
Wendy Smoak 00:13:47 But not really… it kind of assumes a lot before you get to it.
Kayla Reopelle 00:13:49 Yeah, yeah.
Wendy Smoak 00:13:53 Which I just know from, like.
Working with other open source stuff.
If it's too hard, people have plenty of other things to do.
Kayla Reopelle 00:14:05 Yep, good point.
Alright, anything else on this?
That we want to chat about?
Wendy Smoak 00:14:14 On the spec?
I think it's related… where's my issue?
There's an issue that I opened, like, one of the first ones about… You… you don't have…
Access to the.
Kayla Reopelle 00:14:32 Oh, yeah, yeah.
Wendy Smoak 00:14:34 And… and not, like, that specific… yeah, if you do it by author, I think it's, like, the third one I have.
of that. Okay, so…
I'm not fussed, like, specifically about this, but the fact that I haven't been able… so I asked here, and then I went over to SIG, and they pretty much sent me back here.
So, like, how?
Kayla Reopelle 00:14:53 Yeah.
Right.
Yes, and I… I met with the SIG people as well, and they said.
We need to have clearer use cases about why this should exist in the specification, and why, you know, you can't use what's already there.
Wendy Smoak 00:15:15 Yeah, because, I mean, I have a…
I… well, I mean, I… it's in my example project, that's why, because I needed.
Kayla Reopelle 00:15:22 be able to.
Wendy Smoak 00:15:22 get the thing back out, and you can't, so I had to basically keep my own map.
But I just… I don't quite know…
Do I go over there and just be annoying? I can do that. Yeah. I'm very good at that.
Kayla Reopelle 00:15:35 That… that could be a good next step, because they may take you more seriously since you're an end user and not one of the maintainers.
And I would say open something in the specification, OpenTelemetry specification repo, that's proposing adding this, and
They have good instructions when you open a pull request or an issue about, like, what goes where.
Wendy Smoak 00:16:01 Okay.
Kayla Reopelle 00:16:02 And if you want any eyes on that, just let me know. I'm happy to look.
Wendy Smoak 00:16:07 Alright, so I'll do a… an issue that's kind of like a proposal and an explanation of why…
Kayla Reopelle 00:16:13 Yeah.
Wendy Smoak 00:16:13 in there. Okay.
Kayla Reopelle 00:16:15 That's their… their order. Usually, yeah, open the issue first, and then you have a pull request linked to an issue.
Wendy Smoak 00:16:22 Okay, I'll go look at some of the other ones that are coming in.
Alright, yeah, I just need kind of a next step. It's not that big of a deal, I have it wrapped already. I'm probably gonna always have it wrapped for very, like, something, but it's just, like…
This is weird, you can put stuff in, but you can never get it out.
Kayla Reopelle 00:16:38 Yeah, yep.
Wendy Smoak 00:16:40 Thanks.
Kayla Reopelle 00:16:54 All right, so yeah, so another fun thing about OTEL, just semantics of where to log things, I think that this…
Export status logging is outside of the specification, and in… the,
in the tracing SDK and the logs SDK, I think the export status logging went there.
And so that just kind of made me assume that it should be in that place in metrics as well.
But I think the concern that you raise about testing and having a bunch of mocks is also, worth evaluating, and whether or not we should
have… You know, if it's… if it's more difficult.
To really test it well in,
the SDK, is that where we should put it?
Does anyone…
Wendy Smoak 00:17:45 Yeah, I did not even pay… like, I didn't even notice that it was in one place versus the other. So, if it belongs in the SDK,
I can take another pass at the… tests and see, it's…
Kayla Reopelle 00:17:58 Okay.
Wendy Smoak 00:17:58 Quite possibly, because I don't know what I'm doing, and I don't know how all the things fit together.
But my first couple attempts was like, this is awful.
Kayla Reopelle 00:18:06 Hmm, okay.
Ariel @arielvalentin (ATX, USA) 00:18:08 Is there, this is a PR… sorry, so the question is what…
what was the open question? I literally…
Kayla Reopelle 00:18:17 My question is, so we have, some, like, reporting logs around, like, successful export, or, you know, unable to export however many.
Ariel @arielvalentin (ATX, USA) 00:18:28 Mmm.
Kayla Reopelle 00:18:29 Everything exists for spans in some place or another.
Ariel @arielvalentin (ATX, USA) 00:18:32 And the question is.
Kayla Reopelle 00:18:32 is, like, where does that actually belong inside of our mess of gems? Like, should it be in the exporters? Should it just be in the SDK so that it can report on, you know, whatever export code it receives, regardless of the exporter?
Right now, since we only have one exporter for metrics, it,
You know, it functionally would be the same, but eventually,
You know, if we were to have more exporters, would this still be the right choice?
Wendy Smoak 00:19:03 And the root cause… the route was… when I… when I first did logs, I was getting, like… it was… I put it in debug, and it was telling me things, and it was super… and I started doing metrics, and it was just, like, totally silent. I couldn't tell if it was doing anything, like, if it… I couldn't tell if it was exporting, and there was something, like, wrong with the collector, I just… there was just no output.
So, I… basically stole it from the batch log record and plopped it in the wrong place originally.
It just needs to say, like, add debug, which no one will ever use after the first 15 minutes that they're doing this, you know?
Ariel @arielvalentin (ATX, USA) 00:19:38 I work, I work…
Wendy Smoak 00:19:40 be successful, because then you know that the SDK did its thing, and if you're not getting your metrics where they expect, where they're supposed to be, you go look at the next thing, right? It was just…
I just couldn't figure out what was going on, so…
This is not a big deal, but…
It makes it match the logs.
Ariel @arielvalentin (ATX, USA) 00:19:55 So the question is what, how to incorporate the diagnostic logging
Because right at the end, the only thing that we… the last kind of output we have is the diagnostic logger.
That's part of the hotel, you know.
diagnostic logger, the… that global logger, or the handle error, to communicate that there's problems happening in a particular SDK component.
And we're trying to avoid circular references, that's number one.
And number two, because the… that global logger, reps…
A lager that could be injected by an end user.
Which could be trying to export data using… the logging bridge.
Kayla Reopelle 00:20:47 Oh, yeah, well, I guess…
Wendy Smoak 00:20:49 That's already handled.
Kayla Reopelle 00:20:50 That's already handled, yeah.
Ariel @arielvalentin (ATX, USA) 00:20:51 That's all.
Kayla Reopelle 00:20:52 care.
Ariel @arielvalentin (ATX, USA) 00:20:52 That's already handled.
Wendy Smoak 00:20:53 Yeah. Yeah, it… it… it doesn't, like, it won't… it won't get itself into a… into a loop. This is… this is essentially just adding the success message.
There was just no… there was no debug level success.
Ariel @arielvalentin (ATX, USA) 00:21:07 Mmm, and then,
Wendy Smoak 00:21:09 And the problem I ran into is trying to test it, really. I'll take another stab at it.
Ariel @arielvalentin (ATX, USA) 00:21:14 Oh, trying to…
Wendy Smoak 00:21:15 Perfect question.
It was just mocks, all the way down, trying to get it to do anything, and it was… it did not look pretty.
Ariel @arielvalentin (ATX, USA) 00:21:23 matches a Yeah.
So, so, so whether or not to use something like a test double in there instead, and, like, have an in-memory logger or something to check the…
the… the results.
Wendy Smoak 00:21:35 Yeah.
Ariel @arielvalentin (ATX, USA) 00:21:35 Or, or you…
because that's the only other thing that we could use, right? It's gonna be a test double or interaction test, you know, like, a fake or a mock. And the mock is just like, it's the implementation of the code, right, in the test.
And whether or not it's essential or accidental, like, do we…
necessarily have to add the code coverage for debug specifically.
you know, when I look at this and I see that there's the handle error and the logger error.
Then it makes me also wonder about things like…
Hmm… are we at the right interface level, or at the right level of abstraction for…
Interactions between, like, the…
you know how we report these errors or not? Like, this is the metrics SDK, right?
Kayla Reopelle 00:22:26 Yeah.
Ariel @arielvalentin (ATX, USA) 00:22:27 Hmm.
And of course.
Wendy Smoak 00:22:29 When it doesn't work, there's another, like, there's another more specific error that gets output when it doesn't work.
Ariel @arielvalentin (ATX, USA) 00:22:36 -
Wendy Smoak 00:22:36 Yeah.
Ariel @arielvalentin (ATX, USA) 00:22:37 In addition to…
Wendy Smoak 00:22:37 that. But there's just nothing on success, that's all.
Ariel @arielvalentin (ATX, USA) 00:22:42 Yeah, no, no, copy, I copy. I see,
That way you can keep track of if the exporter is running effectively.
Because you want to make sure that the exporter thinks that it's emitting metrics, but if downstream the collector isn't handling those metrics, or sending the metrics anywhere, it's like, why aren't they showing up somewhere?
And you're trying to trace down where that's going. Okay.
Wendy Smoak 00:23:08 It's for brand new users, like, if you put the SDK in debug, you get that reassuring, hey, it worked, it worked, it worked!
Yes, ma'am, yes ma'am. Which you get? What'd you get for logs?
Ariel @arielvalentin (ATX, USA) 00:23:18 Understood. Understood.
Wendy Smoak 00:23:21 I will take another pass at testing it and maybe ask a more intelligent question then. I have no idea which one.
Kayla Reopelle 00:23:27 When I.
Wendy Smoak 00:23:28 I ran out of time on the weekend.
Kayla Reopelle 00:23:30 I think Arielle's mentioned, too, of the, there's, like, a test logger that's inside of the test helpers.
that could be beneficial here. There's also a pull request, that…
has been at the bottom of a long list of pull requests to review. That is to introduce test helpers for the metrics SDK. It was more intended for instrumentation, but they might also be helpful in this case, too.
Fingers.
Ariel @arielvalentin (ATX, USA) 00:23:59 I didn't know, like, the other thing is, like, I know that this might be over-engineering, but would an observer be…
a better friend in these use cases, and we'd have a different implementation on observers.
For these things, so we would inject an object that would receive messages that are, like.
This was successful or not.
You know, to… it's like, it's notified when a success or a failure happens.
Or there's something… And then it's… We can provide a diagnostic
Like, a verbose, observer that's like, log a debug statement every single time, the standard error.
Or… You know, effectively, it could be the… it could use the global logger underneath the hood.
And then that same interface is what we would use for the Trace SDK. So in my case, I'd want metrics emitted from the Trace SDK versus
You know, if for the metrics SDK, it's like, if it can't emit anything, we probably want logs out of that one, or diagnostic error, things to standard error.
Or, does that make sense? I'm just.
Wendy Smoak 00:25:15 When you say observer, is that, like, the pattern, or is there something specific in.
Ariel @arielvalentin (ATX, USA) 00:25:20 Yes, ma'am, the observer pattern. Just pattern. Yes. Yeah, yeah, yeah. As opposed to saying, like, this will always use the logger.
Because I know, like, you know, part of that is kind of like saying that, you know, as far as the internal… the internal metrics that are being reported.
Wendy Smoak 00:25:40 Which we don't have yet. I opened the issue about it.
Ariel @arielvalentin (ATX, USA) 00:25:42 Yeah, so it's like, it might be leaning towards… it might be leaning towards the direction of how we would want.
Wendy Smoak 00:25:47 Oh, how we can implement that.
Ariel @arielvalentin (ATX, USA) 00:25:49 metrics by adding the observer and say.
I'm gonna let you know when a successful batch was emitted.
And that event's, like, successful batch omitted, and then that reporter is a metrics reporter.
And it emits out metrics.
Or we can have a diagnostics reporter, which is just writing to standard… no, I shouldn't say just, but it writes to standard error as its default, or to a file, or to whatever.
But again, that might be…
I might be over-engineering a little bit.
Wendy Smoak 00:26:21 Well, I don't know, because, I mean, I was… I've been trying to kind of, like, think about how would one do metrics about the metrics, and, like, my brain kind of goes, ow, and so I haven't…
Haven't really come up with, so if that is the pattern that we could use to do that, that would also…
Ariel @arielvalentin (ATX, USA) 00:26:35 Derek?
Wendy Smoak 00:26:35 The logs better.
Ariel @arielvalentin (ATX, USA) 00:26:37 we can confirm this with the spec group, but I would think that at the highest level, it's like we, you know, we have the… the thing, we have the self-reporting metrics.
Which is… which we can decouple from the log… from the trace SDK through the existing metrics reporter pattern, right? Because that's, like, more of an, you know, following that pattern.
the metrics SDK can attach a similar interface to it, a thing that it depends on with a similar interface, but its output is gonna be logs
as… You know, like, standard error logs, if…
Metrics can't be exported, because that one is the conundrum.
it's that one.
But if we… if it's self-reporting metrics or whatever. And then lastly, the, the logs themselves.
they can admit… it's great, they can admit metrics about themselves, but it will have to have the same fallback as the metrics SDK will, which is like, I can't write this because the metrics
the metrics endpoint is unreachable at this point, so I have to dump it somewhere, and standard error seems to be, like.
Sort of, like, the, output of last resort.
But, thank you for letting me speak for, like, 10 minutes.
Wendy Smoak 00:27:55 Yeah, that's good.
Kayla Reopelle 00:27:56 Good, it's good brainstorm.
Wendy Smoak 00:27:57 I am not… I am not capable of doing the architecture for this stuff, so…
Ariel @arielvalentin (ATX, USA) 00:28:03 I seriously doubt that, Wendy? Seriously doubt that statement, but you know.
We'll see.
Wendy Smoak 00:28:15 Let's see what we got. Alright, so…
We'll get one of… I'd like to get one of those through with some kind
And then we can look at moving to the observer and other stuff. I think what… which was probably going to happen when we start trying… when we start trying to do metrics about metrics, there's going to have to be
some kind of…
Kayla Reopelle 00:28:34 Yeah.
Wendy Smoak 00:28:34 Framework pattern thing going on, or.
Kayla Reopelle 00:28:36 Yes.
Wendy Smoak 00:28:37 There's gonna be a bunch of conditionals in the code, which isn't… like, it's not gonna work.
Kayla Reopelle 00:28:42 I think it also…
Wendy Smoak 00:28:43 Sounds good.
Kayla Reopelle 00:28:43 Of this pull request, that came up last week, about kind of enhancing the logging related to exporters, and maybe we can take some cues from the needs there whenever we get to a, like, a larger re-architecting of the way we emit,
Messages or diagnostic information that could potentially be helpful here, too.
So, yeah, I have some pending feedback, I think, on this PR, but, if anyone else also wants to…
take a look at it, or has ideas from this discussion, too, about how… I mean, this is only logs, this isn't metrics.
About how it could be better. I think they are…
in some ways, like, creating this export result class, I forget where exactly that would…
maybe handle those things. See here? Yeah, there we go.
Still… More to look at and work on, but, just thematically related.
Okay, so that was everything that was on the agenda. Do we want to switch over to Contrib and just take a look at where things are…
Or I guess we can wrap up CORE.
Let's see, are there any PRs here?
to call out, we do have a release that I'll push out later today, includes some updates to the callback mechanism in metrics, Zipkin annotations, and then fixing the minimum SDK requirements for the OTLP exporter.
Ariel @arielvalentin (ATX, USA) 00:30:31 And somebody remind me again, the Protobus. Are they in the common package?
Kayla Reopelle 00:30:36 They're not, and the common package isn't really used right now. There is a… there's a common package that's for the SDK, there's not a OTLP common package. It's… it's part of the refactoring of, like, a OTLP HTTP…
gRPC exporter.
Ariel @arielvalentin (ATX, USA) 00:30:55 That never got sick.
Kayla Reopelle 00:30:57 Because it didn't have the testing, so I think.
Ariel @arielvalentin (ATX, USA) 00:31:00 Okay.
Kayla Reopelle 00:31:00 Schwan proposed that we create a new package, that will hold all the protobufs, and now that we have, you know, exporters for the different signals, they can maybe all install that as a dependency, so we don't end up in this situation again.
Ariel @arielvalentin (ATX, USA) 00:31:15 Oh, yeah, yeah, that seems sensible. One of the things, too, is, like, it…
I know that this is a little bit, unpleasant, but I'm trying to… like, I was trying to figure out a way of saying, like, can we…
generate Protobus with different, ProTalk-generated versions. Like, we're on a really old version of Protobus.
Kayla Reopelle 00:31:36 In some cases.
Yeah.
Ariel @arielvalentin (ATX, USA) 00:31:38 So we can't, like, upgrade because of the… we can't… we're not generating the packages.
Locally.
And so… I don't know…
Kayla Reopelle 00:31:54 Yeah, and there should be easy tasks. I think there's tasks inside of all of the exporter repositories right now to bump the protobuf versions.
That's just not something that we've been maintaining actively. And I think when I had looked at it before, things weren't really tested, so it was unclear as to what would be breaking if and when we updated it.
But that's… I don't think that's probably a good enough reason to be stuck on a protobuf version that's years old.
Ariel @arielvalentin (ATX, USA) 00:32:25 Yeah.
Kayla Reopelle 00:32:26 You know, we're supposed to have interoperability with other languages, kind of similar to our semantic conventions conundrum that we ran into a while back.
Ariel @arielvalentin (ATX, USA) 00:32:33 Protobuffs itself is backwards compatible, but not the Ruby versions.
Kayla Reopelle 00:32:39 Because they're, like.
Ariel @arielvalentin (ATX, USA) 00:32:41 when you generate protobusing, there's one breaking change, I think it's, like, between 3 and 4, where, you…
The way… the Ruby code that was generated is completely different.
Where it was using,
I can't remember now, but it had, like, message formats built into a consonant or something like that.
Kayla Reopelle 00:33:04 And then there was, like, a DSL that was built on top of…
Ariel @arielvalentin (ATX, USA) 00:33:08 another version, for one that was doing the serialization, and so you can't have two of those versions of Protobuffs,
Kayla Reopelle 00:33:17 So you…
Ariel @arielvalentin (ATX, USA) 00:33:18 So you had an app that, you know, so you had an app that had different protobuf clients in it?
You have to migrate them all to the same protobuf version of generated code.
Kayla Reopelle 00:33:31 So, it's like there's two versions at play. There's the protobuf gem that's installed, but then also the protobuf version of the OTil Protobuffs, is that what you're saying?
Ariel @arielvalentin (ATX, USA) 00:33:41 Yeah.
Kayla Reopelle 00:33:41 different code because of all the different… Yeah. Yeah.
Yep.
Ariel @arielvalentin (ATX, USA) 00:33:47 And so I think, like,
that, you know, that's one of the challenges that we'll have. No one's reported it so far other than us.
Where, you know, you have an older version of generated protos that you have to upgrade all at the same time, and this makes it… that makes it challenging, so we need something a little more, I think, robust in the protobuf generation. Right now, I was just…
historically been generating them by hand, essentially, by running the protop commands in a container.
So… It'd be… it would be great if we could maybe set up an action that is…
generating those protobus for us,
And helping us keep up to date with spec changes.
Kayla Reopelle 00:34:33 Is that something… would you open an issue for that, Arielle? To…
Ariel @arielvalentin (ATX, USA) 00:34:37 Because I opened my mouth, sure.
Kayla Reopelle 00:34:39 I mean, you don't have to work on it, but to at least have an issue that captures these ideas, that would be great.
Cool. Alright, I do have to leave in 5 minutes, but that doesn't mean the meeting has to end. Just wanted to call that out.
Alright, let's look at Contrib. There's a lot of.
Ariel @arielvalentin (ATX, USA) 00:35:00 I can't do without you.
Kayla Reopelle 00:35:01 Do you remember?
Ariel @arielvalentin (ATX, USA) 00:35:03 What's broken?
Kayla Reopelle 00:35:06 All is broken. All is upset.
Ariel @arielvalentin (ATX, USA) 00:35:09 as usual.
Kayla Reopelle 00:35:11 I think.
Ariel @arielvalentin (ATX, USA) 00:35:11 It's long over there.
Kayla Reopelle 00:35:12 Little hand-holding, so… Yeah.
Ariel @arielvalentin (ATX, USA) 00:35:15 Anybody out there who loves to little do, like, little scripting things, we could use a little scripting thing that's, like, these dependencies are changing, so all needs a change as well,
So releasing is so unpleasant.
Kayla Reopelle 00:35:34 Yep, that would be nice.
Ariel @arielvalentin (ATX, USA) 00:35:38 But no, I'll get to try to fix that to get the releases out.
Kayla Reopelle 00:35:42 Okay, thanks.
Ariel @arielvalentin (ATX, USA) 00:35:45 One thing I do have to point out is something that's kind of stinky.
Kayla Reopelle 00:35:50 Yeah.
Ariel @arielvalentin (ATX, USA) 00:35:51 I have a PR for Active Records.
Kayla Reopelle 00:35:55 Yep.
Ariel @arielvalentin (ATX, USA) 00:35:56 Been trying forever to… Add things like,
Support for, cached and asynchronous attributes on… on, on spans?
But, I can't for the life of me, get the test to run in async mode.
Kayla Reopelle 00:36:18 I don't know if that… oh, you mean, the tests run in async mode so that they're doing active record?
Ariel @arielvalentin (ATX, USA) 00:36:26 So, the notifications…
Kayla Reopelle 00:36:27 Thank you.
Ariel @arielvalentin (ATX, USA) 00:36:27 glued, yeah.
Kayla Reopelle 00:36:28 Yeah.
Ariel @arielvalentin (ATX, USA) 00:36:29 It's like.
Kayla Reopelle 00:36:29 fascinating.
Ariel @arielvalentin (ATX, USA) 00:36:30 I'm like, I feel not smart. I have plenty of…
you know, friends who can help me, but for whatever reason, the tests don't want to run in async mode, or, like, the load async functions.
are just getting pipelined, and they're not putting… not getting put into futures, and not resulting in… Async…
call, so I'm super annoyed.
Kayla Reopelle 00:36:56 How does Rails test it? Have you looked at what they do for running the.
Ariel @arielvalentin (ATX, USA) 00:37:00 Of course I haven't, girl, of course I haven't.
But no, I did look, and I did not see any examples in the repo that tested specifically for the attribute being set to true or false.
Kayla Reopelle 00:37:16 Hmm.
Ariel @arielvalentin (ATX, USA) 00:37:17 So, I didn't find examples of the notifications being checked.
Kayla Reopelle 00:37:23 Interesting.
I… don't think I've written any unit tests for this yet.
Ariel @arielvalentin (ATX, USA) 00:37:34 Okay, so if anybody is, like.
Morbidly curious, or wants to be tortured.
check out this PR, and run the test, and let me know what I'm doing wrong.
That's all.
And I was looking at Rails events, and I have no idea…
What the heck we're gonna do.
Kayla Reopelle 00:38:04 So, I think that Rails events need to become a separate bridge for an OpenTelemetry logger. It could… I mean, I don't think it needs to live in the Ruby logger one, because they're different, they are very Rails-centric.
But,
That is what seems like is the most appropriate hotel map point. Because also, in addition, there's a field…
for hotel logs for event name, that I think could also have some comparisons there, and might be able to get
ingested correctly by OpenTelemetry backends, too, in that case.
Ariel @arielvalentin (ATX, USA) 00:38:42 So… so it's not replacing notifications.
Kayla Reopelle 00:38:46 oh, maybe I'm misunderstanding, what exactly… I mean, I did see that they rolled out a whole bunch of,
Event reporters for different… Things that are notifications.
That had never crossed my mind. Do you… did you read something that it sounded like it was replacing notifications?
Ariel @arielvalentin (ATX, USA) 00:39:08 That's what I felt, I don't really know, no, I mean, I'm just extrapolating.
Kayla Reopelle 00:39:11 Interesting.
Ariel @arielvalentin (ATX, USA) 00:39:12 Because I saw that in the blog post, that it said that this would be used for metrics, traces, and logs, and I was like.
Kayla Reopelle 00:39:18 Oh, I haven't seen that blog post yet.
Ariel @arielvalentin (ATX, USA) 00:39:20 And and I said, that doesn't seem right, because it's not cap… it wouldn't allow us to do what we do with notifications today, which is to create a span and finish the span. So we would have no child context available.
When we're doing instrumentation based on…
notifications. That's the part that I was like, oh…
It only has the omit method.
Yup,
Kayla Reopelle 00:39:49 Can you share that blog post with me?
Yeah, or post it here in the notes.
Ariel @arielvalentin (ATX, USA) 00:39:57 Yes, ma'am.
Kayla Reopelle 00:39:58 Yeah.
I think I'm… I think somebody's getting some time to spike on that.
On my team soon, so…
is in probably, like, the next 2 weeks, so hopefully we can have more details then, too.
Okay, I have to…
Ariel @arielvalentin (ATX, USA) 00:40:20 at least stop sharing my screen.
Kayla Reopelle 00:40:23 Does anyone want to take over? Is there more stuff that we want to discuss?
So, hi, Jed, welcome, thanks for coming.
Jed Schneider 00:40:34 No worries, just kind of… Being a fly on the wall, so thanks.
Kayla Reopelle 00:40:37 Right?
We'll appreciate that.
Wendy Smoak 00:40:41 I think we were just looking at Contrib PRs.
Kayla Reopelle 00:40:44 Okay.
Wendy Smoak 00:40:44 Someone else wants to share?
Kayla Reopelle 00:40:46 Yeah, I'll… I'll stop my share, and…
Ariel @arielvalentin (ATX, USA) 00:40:52 Well, you have a wonderful day.
Kayla Reopelle 00:40:55 Thanks, I'll be… I'll work on my phone. I just am driving, so it's not safe to, you know, share my screen.
Ariel @arielvalentin (ATX, USA) 00:41:02 Come on, are you for real?
Kayla Reopelle 00:41:05 Yeah, yeah.
I'll see you guys again. Alright, thanks, Dust.
Ariel @arielvalentin (ATX, USA) 00:41:11 I totally would share my screen if I was driving, that way y'all know I was safe.
Sorry, let me just disable my notifications here so that you don't see my kids asking me to do stuff for them.
And then I'll go ahead and share my screen in a sec.
Thanks, everybody, for your patience here as I take over. And we were looking at the spec PRs today, the core… and contribute PRs, right?
So…
Why is it that this isn't mind going anywhere? Don't mind the background noise. If there's stuff that you don't recognize, it's okay. I get stuff staff shipped to me, so…
when I see it first, you get to see previews of features.
So, there's a couple of them that are on here. Looks like we have a few that… let's see here, review required…
Let's take a look at review required. Okay, so this was the one that was recently… these are all in draft mode, so let's not take a look at those. But it looks like, kind of, you're waiting on a review here for the SQL processor, right?
Hannah Ramadan 00:42:29 Yeah, so when we renamed the gem initially, I just kind of…
copied everything from the SQL obfuscation gem into the game, but because there's gonna be more stuff inside the SQL processor, right now, the idea is just to put the
What's it called? Like, the…
summary… query summary, stuff inside here as well. I just want.
Ariel @arielvalentin (ATX, USA) 00:42:54 Hmm.
Hannah Ramadan 00:42:55 Move some stuff around, to make it…
more, like, extractable and, like, better for the future. So…
Ariel @arielvalentin (ATX, USA) 00:43:03 Sounds great. Okay, so you're… this is effectively a structural refactoring? Yeah. And repackaging, right? Because, oh, we're just doing the renames right now, the packages that are… where it's being used. Okay.
Because instead of it being the obfuscation helper, it's in the processor namespace, and now it's obfuscation jump. Okay, so if, anybody has time to review this, I try to give this a shot of Ana at the end of the week.
When I have a little bit more time.
Does that sound alright?
Hannah Ramadan 00:43:32 Oh yeah, perfect, that's, that's, ideal. Thank you.
Ariel @arielvalentin (ATX, USA) 00:43:35 Okay, so adding latency and retract count instrumentation.
Interesting. So… where are my resident metric people?
Oh, this person hasn't signed the CLA, the EVCLA, so I'm gonna skip this one, sign things later, and then I review.
Alright, and then,
Schwan, you got one in draft here. When you're ready for us to review it, let me know.
Looks like we've got some… we've got a new resource detector, and this contribution came in on September 11th, which…
Woo! More than a month, this person is very patient.
And there's Thompson again, coming on in and helping out with doing the reviews.
Do we have anybody here who uses Render?
Xuan Cao 00:44:30 No.
Jed Schneider 00:44:31 I… this is render.com.
Ariel @arielvalentin (ATX, USA) 00:44:33 Yeah, I think so.
Jed Schneider 00:44:35 the past.
A platform as a service.
Ariel @arielvalentin (ATX, USA) 00:44:38 Yes, Renner.com, yes.
Jed Schneider 00:44:40 Yeah, yeah, so I do actually have a project on there.
Ariel @arielvalentin (ATX, USA) 00:44:44 Cool! Jed, can we leverage your, like, knowledge, expertise around the area here to confirm that the resource detector is doing… is working as expected?
Jed Schneider 00:44:56 I think so. I'd have to look to see how intrusive it is to, you know, get it going, but yeah, I can definitely, like, I have a render account, so I could, like, stand something up, and…
You know, check things out, those kinds of things.
Ariel @arielvalentin (ATX, USA) 00:45:09 Very cool, because this person is looking to contribute this, and the challenge I have is I'm not a render user, and
We would effectively be accepting this contribution, leaving, this person, as a,
Essentially, as a code owner?
And.
Jed Schneider 00:45:28 I…
Ariel @arielvalentin (ATX, USA) 00:45:29 And because it's the contribution that they're putting forward, so any code changes that would come in through here would have to go through them. But we also need a second pair of eyes who can confirm that everything is okay. And if you're a render user, you would be an awesome candidate to help us out with this.
Jed Schneider 00:45:46 Yeah, I can certainly take a look.
Ariel @arielvalentin (ATX, USA) 00:45:48 Thank you so much!
Appreciate it.
Jed Schneider 00:45:51 Yeah.
Ariel @arielvalentin (ATX, USA) 00:45:52 Let's see here, so that was that, and then we've got another one. This is… these are all drafts.
And I think that… oh… gosh darn. These…
These ones are a little bit tough.
So… We've got the… we've got these challenges with…
I think we're just looking at this one, sorry, it was just in the way. We have these challenges with these dyne… with…
How the messaging specification tells us We should handle propagation.
And the, we have a few of these contributions around…
Around propagation and saying whether or not we want it to be sort of dynamic versus static.
On propagation, because there's cases in which A message is coming through.
And right now, we either… we only allow them globally.
across all of the message handlers, and in this case, they're background jobs, right? In the case of Sidekick.
So every single background job will have the same strategy.
Whether it's gonna be, A parent, or a child, or whatever.
The specification doesn't make it easy for us to say how you make that determination.
Right, so this might be a language-specific thing?
For us to look into.
But one of the things that we wanted to try to avoid was to say… allow for…
Custom code to make the determination about whether or not
something, should it be dynamic, or it should be a parent-child, or it should be a link, or both? Because the specification also supports both.
to say… Continue the trace as a parent-child, and add it as a link.
this is weird, because there's, like, these batch semantics, because, you know, you have, a lot of cron-style jobs that say, I'm a… I'm… I'm gonna spin up
a bunch of jobs that I'm gonna run, but in these cases, I don't want these jobs to be…
All part of the same trace.
Just because a single… Sort of batch job generator.
Was the thing that started those jobs off.
And kick those off.
And then you have…
Use cases where, yeah, sometimes you do want a parent-child because of the way that the vendor handles it, right?
You have a… you want to have, say, a web controller.
let's say for… in GitHub's case, right?
Web… you make a comment onto an issue.
And then whatever happens with that comment, there are some cases where you want to see in the same trace.
the comment going into a background job, or into a Kafka message that says, I'm gonna go post this out somewhere, and then a bunch of other systems responding to the fact that the comment was published, you know, whether that's gonna be, like,
community protections, spammers, spam detection, and so on and so forth. You may want all those things connected to one another, but you really don't know, because by the nature of the message being sort of, like,
asynchronous.
You… and not… Not, targeted towards a specific consumer.
We don't know whether or not that should be a parent-child ahead of time, because you don't know who all are the consumers of these messages.
If that makes sense. I know this is… I'm being very verbose and hand-wavy here, but I hope I'm… I'm explaining myself clearly.
And so, what this PR, I believe, I haven't had a chance to review it, but I believe that what this PR is trying to introduce is the ability to dynamically make… to provide custom code hooks, to dynamically determine at runtime
what strategy The job should use to continue the trace.
That this consumer should use to continue to trace.
And that's something that we've been wanting to try to avoid.
For quite some time.
Am I… is that what… I just want to make sure that that's true about what this…
Or, or what this was doing.
Yeah, it's like… it looks like it's trying to add, like, a validator so that we can have…
propagation style be a dynamic value, because right now, the base instrumentation only supports static values. It doesn't support callables, effectively.
for… for value, so…
This is a tough call here.
I'm not sure what to do about this, I don't know, you know, we've tried,
Discussing this with the spec, say a couple of times of, is there any way for us to send hints from the client side, or…
Is there something that we can do with the SDK?
To make a definite, you know, to figure out whether or not something is a root span, whether something should be a local span, like, there's a continuation
I don't… I don't know what to do about this, I guess is what I'm getting at.
Does anybody have any strong feelings or concerns? Or…
Wendy Smoak 00:52:04 I don't know what any of that means. I've only done logs and metrics so far.
Ariel @arielvalentin (ATX, USA) 00:52:09 only logs on metrics so far. Well, if you will… if you had a… if you had a log.
and the log had a trace ID in it.
And the log was omitted from a background job.
that trace ID could either be… it could be the trace ID from which the job was enqueued.
Wendy Smoak 00:52:33 So, say you were in a web controller.
Ariel @arielvalentin (ATX, USA) 00:52:36 and you enqueued the job, you can say, later, you know, later on, there could be a log that says, I've enqueued a job, and it has this trace ID on it. Then when the job runs, and it says, I'm running.
I've got a trace ID on it.
Should that trace ID be the same as the web controller?
Wendy Smoak 00:52:53 Or a new one for just the job itself?
Is that what the question is?
Ariel @arielvalentin (ATX, USA) 00:52:58 Yeah, so then that… that's one scenario. So the messaging spec originally said, well, what we've got is an idea of you get a new trace ID,
But then there's a notion of a link.
And there's a trace parent that's a link.
But… but it cr… but it starts a new trace.
Jed Schneider 00:53:19 Hmm.
Ariel @arielvalentin (ATX, USA) 00:53:20 So… Well, here's the problem, is that if you add sampling and you sample based on trace.
So people are like, no, what I really want is for that job to have the same trace as the controller.
Wendy Smoak 00:53:36 So if you get it, you get everything.
Ariel @arielvalentin (ATX, USA) 00:53:38 Except sometimes that job gets run by a cron job, but sometimes it comes from a controller. But that cron job enqueues 2,000 jobs, because it's the cron job that retries all the dead letters.
Or, like, all the failed jobs. And that cron job will run, and now…
they all have this trace ID of the cron job, because the cron job is the one that enqueued it.
Not…
Wendy Smoak 00:54:02 supposed to be separate.
Ariel @arielvalentin (ATX, USA) 00:54:03 But I want those to be separate, and I want that to be linked originally to the controller.
where it came from, but sometimes… but it could be a link to the cron job, because the cron job was like, oh, the cron job had a trace, and it generated a bunch of stuff, and I want it to be linked somehow. So yeah, apply links in that case.
And then…
Wendy Smoak 00:54:25 Which is why we put attributes on all the things, so that you can go find all the stuff about your tenant, or your… whatever.
Ariel @arielvalentin (ATX, USA) 00:54:32 you're trying to find out about. So what people… so what this… this issue was, well, I want to be able to make that decision on a job-by-job basis. Whether or not the… if the job…
should… would know, you know, if you should attach yourself as a child or continue something new. But this is not a new problem, right? This is the same problem that you have as you have, say, like, a web front end, and you've got an HTTP server. Do you trust the incoming trace parent headers and attach it to your trace?
Because a malicious actor can just give you the same trace ID for a month.
And if you trust that person, the next thing you know, every single web request you've ever made is on the same trace ID.
So it's kind of like, it's a very similar problem. It's like, when do I know that I should start a route?
how do I trust the incoming headers?
what should I, as a single instance of a job, have more information so I can make a decision about how I generate my propagation?
Because the propagator's just… the API is just inject or extract, there's nothing else.
And then the instrumentation is responsible for knowing what to do. And semantically, it's like, for messaging, which, this is what we apply to jobs, because there is no jobs semantics.
For messaging, we're like, oh… by default.
Make it a link, and start a new trace.
But that's not… but we apply that globally, and that's not satisfactory.
That's the problem that we're trying to get at here.
Wendy Smoak 00:56:11 This seems like a reasonable thing, but it's another case where you… it's not really, like, allowed by the spec.
So now we go… now we're in the same situation that, like, I am. Like, we have to go back to the spec and say.
Ariel @arielvalentin (ATX, USA) 00:56:24 Note the date that it was.
Wendy Smoak 00:56:25 in adding it.
Ariel @arielvalentin (ATX, USA) 00:56:27 Yeah, note the date that it was 2024. We engaged all the way back then, and still wasn't resolved, but this person really wants to have this proc option, and I'm not comfortable adding dynamic code to the SDK, for these kinds of situations.
Because it's like, oh, anybody adds arbitrary code, the SDK stops working, and then it's our fault. And it's like, we have to try to debug these arbitrary, like, coding points.
And that's the thing that I'm trying to avoid. So is there something…
That we can add to, like, say, provide a hint of some sort, like.
figure out a way in trade… mate, is it tray state?
that tells us that there's trusted headers, or… what could we do? What could we do to solve this, kind of, in the generic case?
That was a long conversation, but as you can tell, it's been going on for more than a year, and I don't know… I feel terrible just being like, I don't want to accept this contribution.
Because it just doesn't feel cut and dry to me, like…
Wendy Smoak 00:57:33 Without having to deal with the spec. But that's… I mean, that's why we have the spec, so…
Ariel @arielvalentin (ATX, USA) 00:57:39 Yeah, I know.
But at the same time, it's like, we have flexibility.
to be on-spec or off-spec, depending on the circumstance, if that makes sense. It's like, some things are language-specific or use-case-specific.
Wendy Smoak 00:57:53 I saw that in there.
Ariel @arielvalentin (ATX, USA) 00:57:55 So it's not great. But look, we've got about 2 minutes left, and if there's anything that's in this list that is really catching your eye.
That you'd like to dig into?
Right, in the last 2 minutes, please let me know.
Wendy Smoak 00:58:11 What's Sidekick Metrics?
Ariel @arielvalentin (ATX, USA) 00:58:13 Sidekick Metrics.
Wendy Smoak 00:58:16 Is that a PR?
Ariel @arielvalentin (ATX, USA) 00:58:17 Yes, this is a… right now, this is a draft PR.
This person was trying to contribute it, but it looks like they're no longer able to continue to contribute to it.
But I think it was their attempt to add.
Wendy Smoak 00:58:32 In the implementation?
Ariel @arielvalentin (ATX, USA) 00:58:33 Messaging metrics into the instrumentation.
Wendy Smoak 00:58:37 I am personally doing this all by myself for our own code. And I was… as I'm doing it, I'm wondering, like, shouldn't this be part of the instrumentation? How would that work? I shall look at this.
Ariel @arielvalentin (ATX, USA) 00:58:47 Yeah, yeah, so this might be a good starting point to figure out what we want to do next.
But, with that, we're coming up to time.
I want to say to everybody who's been volunteering.
While I've been absent, thank you so much.
Really appreciate it. I'm gonna continue to do what I can, which is essentially get help get releases out.
Which is gonna be my limited capacity at the moment.
Wendy Smoak 00:59:15 And go Schwan on the metrics! Thank you for doing all the metrics things.
Ariel @arielvalentin (ATX, USA) 00:59:19 Yeah, thank you, Shuan. Thank you so much. You've been really pushing that forward, and Hannah, thank you so much for working on SEMCOM. It is not the funnest thing in the world, I know.
It is not the funnest thing in the world.
And Wendy, thank you so much for being so active in the community, and
You know, giving us feedback, really appreciate it.
Wendy Smoak 00:59:38 I just want my stuff to work and escape from this project someday.
Ariel @arielvalentin (ATX, USA) 00:59:41 Yeah. Jed, thank you for helping us take on.
Wendy Smoak 00:59:45 Welcome, Jed.
Ariel @arielvalentin (ATX, USA) 00:59:45 render.
Thank you for joining us today.
Jed Schneider 00:59:48 No problem, I'll do my best to get on every week, so…
Ariel @arielvalentin (ATX, USA) 00:59:53 Excellent. Is this your first time at the SIG, by the way?
Jed Schneider 00:59:57 It is, I connected at Exergy a couple weeks ago, and,
Took me a while to get the calendar invite and stuff, organized, so…
Ariel @arielvalentin (ATX, USA) 01:00:11 Hey, welcome!
Jed Schneider 01:00:12 Yeah, thanks, I appreciate it. I'm working on a Node project right now, so this will still keep me in the Ruby world a little bit.
Nope. Nope, nope.
Ariel @arielvalentin (ATX, USA) 01:00:20 problem at all. You know, we could do… if anybody's got 10 seconds, we could do a round of intros to welcome Jed to the community. I am Arielle, I am an observability engineer at GitHub, and I work… I now mostly work on the infrastructure side, so I work on agents, like the collector.
So I'm doing less and less instrumentation-related work.
But that's what I do. And so, I'll pop corn over to Wendy.
Wendy Smoak 01:00:48 Hey, Wendy, we're doing… we're bringing,
Logs and metrics and probably traces at some point, maybe in-house from
random cloud vendor. So, doing all the, OpenTelemetry things for bunches of Rails apps.
Jed Schneider 01:01:03 Nice.
Wendy Smoak 01:01:05 Hannah?
Hannah Ramadan 01:01:06 Yeah, hey Jed, my name is Hannah, I work on the Ruby agent over at New Relic, and I'm actually on Kayla's team, who popped out a little bit ago. Been working on semantic conventions with the hotel.
It's been a journey, and I'm still, still going, but hopefully we'll get there soon.
Ariel @arielvalentin (ATX, USA) 01:01:27 Honda, you gotta nominate someone else.
Hannah Ramadan 01:01:29 I'm gonna pop one over to Sean.
Xuan Cao 01:01:33 My name is Trun, from Kiana.
I'm mostly just working on the, measures, and then some are part of a country.
F.
Jed Schneider 01:01:48 Nice.
I can do just a small intro myself. So I'm a senior consultant at Test Double,
And, live in Portland, so maybe we'll connect sometime, Hannah, if you're still… if you're here. And
my, like, real experience with, OTEL, Ruby was, kind of January, Christmas time. I was working heavily with Async.
gem, and I got, the hotel async, stuff, trying to wire that up, and it wasn't working, so I connected with Samuel Williams, and kind of, like, shuttled some of that through, so we have,
OpenTelemetry, traces for his async, gems.
So, it seems to be working still, I think, last time I checked it. But he doesn't really maintain it, he just does the Datadog exporter. So,
it needed some…
fine-tuning. But anyway, so that's the only thing I've really done for the… for the hotel community, but, making observability a bit more and more of my, you know, sort of professional focus, so…
I'm trying to learn what I can.
Ariel @arielvalentin (ATX, USA) 01:03:09 Thank you very much. And, isn't that…
serendipitous that you work at Test Double, because we were just talking about Test Double patterns, and maybe, looking at that PR, you might be able to provide a little bit of insight there, as to try to help us with the code smells, so…
Jed Schneider 01:03:27 I'm not sure if I'm a mock or a spy, I don't know.
Ariel @arielvalentin (ATX, USA) 01:03:33 Espionage! Listen, y'all have a great day. It was good to, good to meet.
Wendy Smoak 01:03:38 Yeah.
Jed Schneider 01:03:38 Alright, bye.
