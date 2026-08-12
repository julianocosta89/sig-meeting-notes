SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-08-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 01:32 Flora.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:31 Light agenda today.
If you have topics, please add them.
**Reiley Yang (Microsoft Corporation)** 03:09 Hey, David.
You're muted.
**David Ashpole (Google LLC)** 03:28 That's right, I'm running this today, aren't I?
Welcome, everyone.
Please put your name on the attendees list if you haven't already.
I think we'll give… actually, it looks like we have a pretty good… number of people on the call, so I think we will go ahead… And, get started. Let me share my screen.
**Reiley Yang (Microsoft Corporation)** 04:24 Okay, I can see it.
**David Ashpole (Google LLC)** 04:25 Alright.
Jack, do you want to kick us off?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:31 Yeah, so… Trask and some others have put together this shared workflow called Poll Request Dashboard.
And, you know, I've been using it and really happy about it in the OpenTelemetry Java repo. And, you know, the basic idea is that I think a lot of people are probably in this position where they're sort of in notification bankruptcy with GitHub.
There's just… there's too many.
And, so, you know, what this kind of does is it switches from a push to a pull-based sort of work structure. You know, the workflow is you go and you look at the dashboard on some sort of periodic basis, whatever makes sense to you, and it has a variety of features that help bubble up the work that needs attention. You can see an example of this in the other link that I shared in the spec.
Meeting notes.
And… So, yeah, so it categorizes all the open PRs by, you know, who they're waiting on, whether it's the Maintainers, reviewers, the author, or other, and it gives you a bunch of useful status information, how long it's been open.
the status of CAI, the author, who's been commenting on it, and others. And so, yeah, this is a great feature, and I was just thinking about how it would probably help improve the spec repo to draw attention to things that… that needed attention, and it would definitely help me as well. So, I propose adding it to the spec repo, and I wanted to hear if anybody Would… would dissent for any reason.
**Reiley Yang (Microsoft Corporation)** 06:17 We use a consumer.
**Liudmila Molkova** 06:20 We use it in semantic conventions and in Python Gen AI repo, and it works awesomely. It changes the contributor experience, though. There is a little bit of… Education we need to do as contributors to tell them that you should show up high in the dashboard to, get a review, so you should resolve conflicts, make sure, like, you address pilot review questions, and so on. It's… it's definitely a learning exercise for me. It's not a reason not to do this, it's just something to keep in mind.
**Trask Stalnaker (Microsoft Corporation)** 07:02 Yeah, it, I did add a feature a little bit ago to nudge, authors if things… when things are stuck in basically waiting on author.
For a week.
So that, yeah, it explains, you know, there's a live dashboard status comment that shows, sort of, what the current state is, but of course that gets lost.
quickly, near the top of PRs.
And, so, yeah, it'll post kind of a… Yeah, this kind of comment.
I have been… I have considered that maybe a week is too long. As you said, Ludmila, it is… Definitely not, the author's expectation that it, initially, that You know, they think that… We're just always reviewing everything that they say.
So I was kind of thinking of moving that to, like, 2 days, just to, help with that. But anyway, yeah, yeah, it's a… definitely a… if anybody has ideas how to make that.
Better.
That would be cool.
I do open issues in that shared workflows repo, where it's… Homed.
That's really how I get feedback on what's working and… or rather what's not working.
**David Ashpole (Google LLC)** 08:44 Very cool. I assume that I can read through here to figure out how to sign up.
A repository as well.
**Trask Stalnaker (Microsoft Corporation)** 08:51 Yeah, so click on the pull request dashboard link.
Yeah, so all the docs are here, and it explains how to add a repo to it.
**David Ashpole (Google LLC)** 09:06 Cool.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 09:07 And it used to be the case that you had to use your own, LLM API key.
And that's, you know, involved in the classification exercise, and it used to be the case that, you know, it would get updated maybe once a day or something like that, but those problems have been… have been resolved, so now it's… it's updated really quickly, and, you know, you don't have to worry about bringing your own API key or anything like that.
**Trask Stalnaker (Microsoft Corporation)** 09:35 Yeah, I finally figured that out, how to do that without, needing to… I did not want to add infrastructure that we had to manage. I didn't want to add a… or, you know, something to Oracle Cloud to manage the, to take the GitHub event, listen to the GitHub event triggers.
But, Netlify… Netlify, which we use for the website, supports… you can write little, like, node… listeners, and so that's where all the GitHub events are going to that, which basically just turns around and fires the GitHub actions in this repo to do all the real work.
**David Ashpole (Google LLC)** 10:26 Really cool.
Thank you, Trask, and thanks, Jack.
Trask, you have the next topic.
**Trask Stalnaker (Microsoft Corporation)** 10:38 Yeah, Ludmila and I were just discussing that we should share this here.
Briefly, so we're… we've spun up a, semantic convention conformance repo. The first link is sort of the, so if you go to the community Link.
This sort of gives the background, the… oh, did I… What did I copy-paste in here?
**David Ashpole (Google LLC)** 11:11 Got 4 links.
**Trask Stalnaker (Microsoft Corporation)** 11:13 Okay, so Issue 3605,
**David Ashpole (Google LLC)** 11:21 Yep.
**Trask Stalnaker (Microsoft Corporation)** 11:22 Yeah, so this kind of gives the background, There's… We sort of started this with, GenAI in mind, because we've seen how, divergent Gen AI instrumentations Are how much they are, Not following semantic conventions, following other things, so we want to really, you know, create some kind of dashboard or something where people, you know, we can advertise this and kind of put industry pressure on people to conform to the semantic conventions.
As we were evolving that, we realized that, hey, it would be great to do for other semantic convention domains as well.
For example, that second, community issue, 3254, was the stable HCP… yeah, this one. This had been a request, from the governance committee at one point, like, who wanted to understand what the, sort of, conformance of our own instrumentations were to the stable HTTP semantic conventions, and So, going forward, that could be something that runs in the conformance repo and just gives us, keeps that up to date.
For HTTP, we could do, you know, database next, etc.
If you go to the next tab.
David, so this is the prototype, in just my repo, and yeah, so you can see here… lots of different languages, lots of different HTTP clients and different HTTP servers, and which attributes they emit.
And if you drill into one of them, like, you can… I think you can click on one of the libraries.
Yeah, this'll give you the full Weaver, like, story from it.
And Liudmila's been doing a lot of work in the new conformance… in the official conformance repo now under OpenTelemetry to, really tie this nicely to Weaver, and also to make it reusable within language.
repos themselves to do… to use it in CI for validation.
Because that's one of the reasons we kind of paused for a while on this conformance repo, was that there's a good argument to be made for, hey, this stuff should really live upstream in the instrumentation repos themselves.
But I think… both is actually the right answer, where I think the conformance repo is still useful for, testing against released versions and building nice dashboards and reports, that… for users.
While also reusing that same infrastructure in the language repos to validate in CI.
So, sort of, the, what… Ludmil is working on the Gen AI, conformance info right now, and I'm starting to build out the… in the real repo, and I'm starting to build out the HTTP infra, and so the ACDP infra, because we have so many instrumentations across all the languages.
language Maintainers, I'll be pinging, I'll be, copying you on those PRs as we add them to the conformance repo.
You don't have to, review them, but would love for your feedback on my AI-generated… my AI understanding of, C-sharp and Ruby and, Erlang, and, I'm sure, there's some… Good feedback that, y'all could provide there.
So when I do ping you, this is some context of why.
**David Ashpole (Google LLC)** 15:50 This is super cool.
Do these actually write, like… are these, like, unit test based, or are they… Static analysis-based, or does it write a little application that uses these, or…
**Trask Stalnaker (Microsoft Corporation)** 16:02 Yeah, so there are lots of, they're little, programs that actually run… run the code, and, the telemetry is output to Weaver, and then the report is generated from the Weaver output.
Cool. If you go to… the actual repo… oh, I don't have a link.
I think in the conformance repo, maybe we have… Do we have the diagram yet? No. Okay. Anyway, it uses Weaver, and Weaver's cool.
**David Ashpole (Google LLC)** 16:49 Awesome.
**Trask Stalnaker (Microsoft Corporation)** 16:51 Yeah, that's it.
**David Ashpole (Google LLC)** 16:55 Anybody else have any questions for Trask?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:01 So, this is on Trask.github.io. Is the… is the goal to have a page like this on maybe OpenTelemetry.io in… in the future?
**Trask Stalnaker (Microsoft Corporation)** 17:15 Yeah, so, We, Jay, who's been working on the… there's a lot of overlap, potential overlap, also with the Ecosystem Explorer, if folks haven't seen that.
If you go to explorer.openTelemetry.io.
Explorer with, two R's.
Yeah.
So this is a project that Jay DeLuca has been, and the OpenTelemetry I.O. website folks have been working on.
Is sort of a next generation of the… The ecosystem… the registry that we have on the website?
With lots more detailed information.
And so there's definitely, so Jay is, involved in the, the conformance repo.
And so we definitely want to see how, you know, these two things work together, so possibly this could be the destination for those Reports, possibly the website, directly.
what we're… Ludmila and I were just discussing this morning on the, the APAC GenAI call that, we… Well, we're gonna… we wanna figure this out relatively quickly, that if, whether we can do that quickly over here, or somewhere, or otherwise, we might stand up just kind of a temporary dashboard in the conformance repo.
Because… so that, I know that the Gen AI Huxing and the Alibaba folks have a, blog post.
Pending that, sort of… talks about the Gen AI ecosystem and, and… Talks about the conformance reports there.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 19:30 Yeah, definitely interlinking opportunities, because you're, you know, you're talking about libraries in both cases, so you should be able to you know, see a library in the conformance report and link over to that library's details in the Explorer, and vice versa. But, like, yeah, to your… Yeah, it is nice to have that top-level conformance view, though, where you just list all the libraries vertically and have that grid that you have. That's a really nice feature, to be able to see things at a glance, so… Gotta find a way to have both.
**Matt Wear** 20:04 So for this grid view, you said that you have, kind of, some small programs that exercise the instrumentation, and then that gets, kind of set to Weaver? Is that… Correct? Yeah. Like, where… Where are these programs that actually ex… or that, yeah, that exercise the implementation, or the instrumentation at?
**Trask Stalnaker (Microsoft Corporation)** 20:27 In the conformance repo itself.
**Matt Wear** 20:38 So there are, like, you know, within there, you have small, small app set exercises, like various Python instrumentations, Ruby, JavaScript, etc.
Yep. I need to take a deeper look through there, then.
**Liudmila Molkova** 20:53 Do you…
**Trask Stalnaker (Microsoft Corporation)** 20:54 link.
Oh, go ahead.
**Liudmila Molkova** 20:55 Oh, sorry. Oh, you dropped the link to yours. There is a PR from Trask to add the HTTP instrumentations to this repo. It's not… it's not populated yet, but we are actively working on adding the test cases, so… It's… Number 29.
**Trask Stalnaker (Microsoft Corporation)** 21:16 I'll drop that link.
So yeah, those are the pieces, and I'm planning to send, for HTTP, send those in language chunks, or, maybe even smaller library chunks.
So that the language Maintainers and instrumentation Maintainers for that specific language or instrumentation can review it.
**David Ashpole (Google LLC)** 21:58 Crazy. And so the plan is that eventually.
We'll be able to have these as pre-submits.
Have you thought about, like… Generating issues from them?
Or anything like that.
Or is that kind of just… Maintainers can copy and paste if they want?
**Liudmila Molkova** 22:18 Most likely, Yeah. Oh, go ahead, Chris.
**Trask Stalnaker (Microsoft Corporation)** 22:21 No, no, please.
**Liudmila Molkova** 22:24 They're slightly different, so the things here… are intended for, like, coverage, and maybe there is some evolution where we assign, I don't know, a conformance score and use it as a beige.
But currently, the idea is that, at least in, like, someConf, sorry, in Python Gen AI, we already have the conformance tests that are, like, the previous generation of this suit, but they are more strict. They actually fail when things go wrong.
Here, they don't fail, they just report.
And there, we would maybe have a little bit more scenarios and much more stricter checks, so that it is part of the CI.
**David Ashpole (Google LLC)** 23:06 Makes sense.
**Liudmila Molkova** 23:09 But yeah, it would be nice to see, like, for the repos that already have a good test suite, and it takes time to switch or add the conformance runs, that we could use a feedback channel from here to their repos.
**Trask Stalnaker (Microsoft Corporation)** 23:32 Yeah, and so, I mean, it doesn't replace, like, integration tests, right? At least for now, these are very much happy paths.
Maybe we could build out more things, like.
with the HTTP, I would, I would love to add even more basic happy paths, like, declarative configuration that… where you use the HTTP header, you can figure which HTTP headers you want to capture.
That could be a… Standard test, conformance test.
But right now, it's… the tests are super basic.
**David Ashpole (Google LLC)** 24:17 Okay.
Cool. I think we'll move to the next topic then.
Josh?
**Josh Suereth (Google LLC)** 24:35 Okay, I do have to leave in 5 minutes, so this will have to be only a 5-minute topic. This is… I've been going through the proto directory and trying to slowly fix all of the bugs that are reasonable and close all the ones that we're not gonna fix. This is one we have discussed ad nauseum in the past.
which is how to handle UTF-8 in, OTLP.
The thing that people keep discovering is that even though protocol buffers specify that you have to use UTF-8 for strings.
the efficiency of this requirement, of, like, forcing strings to be UTF-8 is horrible. So no one actually enforces UTF-8, like, forces it to be UTF-8.
what you end up with, both in the protocol buffer implementations and in OpenTelemetry because of that, is you assume that people know what the hell they're talking about when they pass you a string. They've made it UT of 8.
That was the decision we made oh-so-long ago around UTF-8. So, we follow the protocol buffer spec that says it has to be a UTF-8 string, and if you get something that's not a UTF-8 string.
then it's basically a bug in the person using OpenTelemetry to pass something which is not a set of UTF-8 bytes. I think this impacts more native languages, like Go, C, Rust, more than others, although I think Rust might be native of UTF-8, so it's a little bit less of a concern there. I think it's more Go and C that have some flexibility here.
Java, I believe, has a lot of shenanigans around UTF-8 parsing, just because nobody uses Java string format but Java, so they had to fix it in protocol buffers.
And the rest… it, you know, it's a little bit all over the spectrum, but, I think this specifically hits go in C++ more.
In any case, what I would like to do here is we discuss this ad nauseam.
And we decided the performance hit of forcing out UTF-8 is not worth it.
so we would align with the spec that says it's required to be UTF-8, but consider it a user bug if, say, an instrumentation sends you a string which is not UTF-8. Like, that's just… a documented problem. And so, this would not be an issue with our protocol, because again, the implementation of protocol buffers, and, like, gRPC and all that.
will allow you to pass bytes which are not UTF-H strings over the wire.
And then some implementations of protocol buffers fail.
Because it's not UTF-8, and some do no validation, just pass it through.
So we actually, when we get a string that's not UTF-E, we don't even know what component caused the failure.
So, there's some discussion here, about possibly, like, requiring, like, putting a compliancy, like, processor or something?
I think those are all reasonable things to do, but, my proposal here is I want to write down In probably the proto Specification.
a caveat about how UTF-8 enforcement is in practice, and how we do not go above and beyond what proto… provides out of the box, and that we consider this kind of a perform… like, the performance degradation of doing UTF-8 validation on strings is so significant that we are not going to have it as part of our system. We're going to ask people who use the APIs to provide UTF-8 strings to them.
where those APIs have bytes and things. Like, I want this to be an API SDK thing.
As opposed to something in the proto directory.
I do have to drop right now, but that's… We can… we can discuss. I'm just trying to call out the history of this, the bug as it stands now, and what I'd like to do with it going forward. There's a couple UTF-8 related bugs, I think, across the spec, and I want to kind of… Address them all with the decision we made 2 years ago.
If that's reasonable. If we feel like we don't agree with that decision anymore and want to change direction, that's fine. Like, let's make note of that here and put it on the bug. But whatever folks feel like is the right path forward, I'm giving you my straw man proposal.
Wanted to get feedback on it. Unfortunately, I have to drop, so if you want to discuss and make comments on the bug, please do. But I have to drop now, so I will, I'll see y'all next week.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:04 Does anyone else have enough context on this to have a discussion?
**David Ashpole (Google LLC)** 29:10 Is Tgrin, or maybe Josh McDonald on the call?
**Joshua MacDonald (Microsoft)** 29:15 I do.
Can you hear me?
**David Ashpole (Google LLC)** 29:18 Yup, yep.
**Joshua MacDonald (Microsoft)** 29:20 Good. Yeah, I was the author of the OTEP, and there's another spec issue here. I've seen this problem and been forced to implement that sort of sanity checker that Josh just described.
I agree with Josh's position. It's too costly to do the validation. What we've seen, though, is that, like, without intentionality, you end up accidentally, like, interfering with that data, and then not knowing how to fix it. So, like, a collector-exporter is going to enforce UTF-8, but the collector-receiver doesn't enforce UTF-8. And then you end up in this case where it's just an error.
and you have no idea what's happened. Because the error essentially, like, drops all the data, you can't figure out where it came from either. You can't print it, you can't log it, like, it's just, like, hard to handle non-UTFA data.
My proposal at the time was you know, for a user that falls into this category of, like, you know, the problem is in front of you, what do you do? You know, logging the data can be problematic. It, like, doesn't go through the instrumentation API either, so you can't log the non-UTFA data, can't debug it very easily.
Therefore, I think that an escape hatch is useful, which is to replace an invalid UTF-8 with valid UTF-8. If you find yourself in that situation, and that's mainly meant for compatibility and migration's sake, like, if you have… if you're going to make a breaking change.
you know, or if you are currently breaking the data, maybe this is the right way to go. On the other hand, if you just removed UTF-8 validation from the OTLP exporter.
now you're just pushing that problem to the next… next person. And so it seems to me that a mechanism to allow users to correct this will be good. That's all I have.
I see, Reiley.
**Reiley Yang (Microsoft Corporation)** 31:18 Oh, yeah, I have some contacts back to when we were working on the metrics API. I just shared a link in the chat. So I think for ETF8, for the API spec in metrics, specification, we called out clearly we only support the BMP0.
The last link in the chat.
I just want to call that UTF-8 is a very confusing thing, like, if you ask 10 developers, they will tell you a different thing. I just think we should be very specific. And also, just to add that some programming languages and runtimes, although they claim they support UTF, but if you ask the question, like, what does that mean?
they might come back and say, oh, we only support this, like, basic plans in Unicode or something.
If you could search for BMP, I'll put the keywords there.
I just want to say, like, ETF8 is not a simple thing, it's not a Boolean value supported. And many languages, runtimes, they claim they're supporting. When you ask, what the hell are you supporting, they will have different answers. It's a complex topic. I want us to be very specific about what plan do we support?
**Joshua MacDonald (Microsoft)** 32:29 I've never heard of BMP, so I've got some learning to do.
**Reiley Yang (Microsoft Corporation)** 32:33 Yeah, so the problem is many people believe they support UTF-8. If you gave them a valid UTF-8 string according to the official designation, their runtime would just, like, complain, throw exception, and we ask them… they would say, I don't know what does plan mean, so that's a problem. Ignorance. They don't understand what does UTF mean.
Okay, I'm done. Thank you.
**David Ashpole (Google LLC)** 33:07 Josh, just to… Circle back.
Do you think the correct… the correct next step forward is for someone to open a PR to the protorepo to, basically say something similar to what you had in your OTEP.
Or should we reopen the OTEP and discuss there? What do you think the right next step is for this?
**Joshua MacDonald (Microsoft)** 33:32 I… I support what was in the OCHAP, but I just learned about something called BMP0, and I haven't read that.
And what I'm aware of is that the OTLP exporter of the collector will enforce that by default out of the box, and the receiver does not, so you end up in this situation where something has to change, which someone will find to be… potentially breaking, I think. So the OTEP should address that.
Otherwise, I agree with the sentiment, that this, like, what we have right now is a very painful situation that's very difficult to diagnose when it happens.
**David Ashpole (Google LLC)** 34:29 Do you think… I'm only vaguely familiar with the discussion now. Do you think your OTEP is in line with what Josh was suggesting we do?
**Joshua MacDonald (Microsoft)** 34:42 I think it was a little bit more detailed, just in the sense that, I agree with Josh's main, main proposal, which is we have to tolerate this, it's too expensive otherwise, and that… more or less, I can't remember what I wrote in that, but I was trying to, like, support the user in their… in their journey once this happens. Like, you know, the… the… when you see a UTF-8 error.
There are some steps you can take to help the user understand it, rather than just, like, throwing a really encryptic error, mainly.
And that would imply that you give options to, like, change that behavior. When you're discovering this problem, maybe you turn on the, like.
the special mode that, like, prints it instead of just drops non-UTF-8 bytes onto the console, which propagates that problem somewhere else.
Yeah, it's been a while since I looked at this. I apologize I wasn't up to speed before we began the conversation.
**David Ashpole (Google LLC)** 35:50 That's okay. I think, I think maybe I'll see if Josh is interested in opening up a, pull request, and then we can discuss there.
Cool.
**Joshua MacDonald (Microsoft)** 36:03 Thank you.
**David Ashpole (Google LLC)** 36:05 Does anyone else have any more… Things they want to discuss today. We still have 25 minutes if there are topics.
**Liudmila Molkova** 36:19 Maybe we can try to see if anybody's interested in doing, project updates in the upcoming weeks.
There is a table above.
There are a few ideas here, and I don't know if we have any people who can present on… The remaining topics.
Oh, we have tentative Sven from Networking SIG. I'll reach out to him and confirm the date.
**Michele Mancioppi (Dash0 Inc.)** 36:53 Can do, if you want, an impromptu update for packaging.
**Liudmila Molkova** 37:01 Like, right now?
Yeah.
**Michele Mancioppi (Dash0 Inc.)** 37:04 How hard… how hard can it be?
**Liudmila Molkova** 37:07 Yeah, let's do it.
**David Ashpole (Google LLC)** 37:09 Alright.
Thank you for stopping.
**Michele Mancioppi (Dash0 Inc.)** 37:13 No, good news is, we have the first version of, packaging out.
It is usable.
It allows you to automatically instrument .NET, Java, Python.
And, node applications running on a Linux host.
It implements the package metadata architecture that we laid out in that very long and storied PR in the packaging.
repository. You can do APT install OpenTelemetry, or YAM install OpenTelemetry, and it could pull all the packages, including the, OpenTelemetry injector.
Or you could go piecemeal and, for example, install only the injector and Java, and then it will automatically instrument only the Java applications on the machine.
Functionally, the packages, seemed to work well.
We have some, a couple of early adopters that I know of.
the quality of the instrumentations that, we inject, of course, depend very much on the upstream, so the language SIGs, and this is why I was, I was whooping and whooping as Trask was, was showing the, conformance thing, because the quality and consistency Of instrumentations is, of course, a huge topic.
We are… Although the project was supposed to include also OBI in the mix to cover languages like Rust, C++, and Go, the OBI SIG has not, yet joined the fray, so we have a bunch of issues for that in the packaging repo, but I understand that They have… they prioritized going 1.2 with the BI, And for that, the packaging with system packages had, had to take a, had to take the back seat.
Something else that misses from… is missing from the picture?
Is the collector packages.
there is an issue in OpenTelemetry, collector releases.
To work about that. From my point of view, the integration will be pretty straightforward. We just need to sit down and, with somebody from the, OpenTendric Collector SIG and effectively make it happen. It will be, a small pack of how the package should… yes, check.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:58 I didn't mean to interrupt, I wanted you to finish your thought.
Sorry.
**Michele Mancioppi (Dash0 Inc.)** 40:02 It was closed enough.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 40:04 Okay, so, collector doesn't exist yet. There's some, you know, SDK instrumentation with the injector. The, you know, the place my head goes is, what is the default configuration for the SDK in that configuration? Does it work without you doing anything?
Of course not, because the only choice you could have would be to export to localhost, and there's… there's no collector running.
But, you know, once the collector gets into the mix, then we have to start asking some tough questions about, like, you know, what the out-of-the-box collector configuration is.
**Michele Mancioppi (Dash0 Inc.)** 40:42 In reality, my expectation is that, the default configuration Would work reasonably well, with a caveat about, having, by default, probably debug exporters.
When you go and auto-instrument applications, the biggest, the biggest thing you have from the point of view of the adopter is the fear, uncertainty, and doubt of, does it work yet?
Is it the meeting telemetry? And, probably having by default, the collector that, prints something to To debug, that could be one way to go about it.
We also…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:26 Sorry, go ahead.
**Michele Mancioppi (Dash0 Inc.)** 41:28 I was about to change topics, so if you want to talk more about this, go ahead.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 41:33 Do you think that the packaging SIG should be the sort of, people discussing and deciding what the default configuration is, or do you think that, like, that decision should be sort of delegated to the respective groups that you're bundling up, like, should the collector be the people that are, you know, writing the default configuration of the collector, or should the packaging set?
**Michele Mancioppi (Dash0 Inc.)** 42:02 I believe, neither is correct.
we should come together, one representing the interests of the package software, and the other representing the interests of the particular form factor, the packages. The defaults that one would expect as a system administrator are different than those that one might expect on Kubernetes.
So, I think both expertisees need to come together in one room. Then, one thing is who should define it, and the other is who should own, right?
That is also a matter where I think, as a project, we need to come together, and for example, I'm going to speak now of language 6.
Today, we have a functional gap in OpenTelemetry, where what is happening inside, for example, the OpenTelemetry operator, or the system packages, is largely defined, in different ways.
for different languages. For Java, we just take the Java agent, because it has an excellent automatic injection experience. For other languages, it's very different, right? The, some have auto-instrumentation packages, some don't, some are not… evolving.
Those packages in a way that guarantees that auto-instrumentation can upgrade.
Python, for example, recently broke the upgrade path of the contribib package by dropping instrumentation without an off-ramp.
For it. So, I believe we should, we should talk at the level of the project of, what does it mean.
For a language to be, automatic injectable.
It's gonna be a bunch of requirements, and then, the language SIGs should, commit.
To join them.
I, in my head, The capability for a language to be automatically injected.
is effectively another dimension of compliance of the language SIG with… of a language SDK and instrumentations on… a new set of requirements. I believe we discussed in the past In several forums that it could be something that we put on the language matrix compliance, right?
Now, I also understand that I mean, we have had… we have been having these issues in the OpenTele operator for… Forever.
And, it didn't result in, in coming together and Effectively move parts of these requirements upstream.
I think we should do it.
I think it's coming to a situation where now that you have multiple projects that effectively take out instrumentations and package them up.
I think we should come together as a project and define what it means for a language to be automatically injectable, what kind of stuff you need to do.
The kind of standards you should follow on the quality and consistency of the semantic conventions, what you do in terms of resource detection, what you do and you do not do with, adding or removing instrumentation, so there is A few things to give a very good experience out of the box.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:20 Yeah, that makes sense to me, both of the things you said. So, like, creating a definition of what it means to be auto-injectable, and also, that the decisions of what the defaults should be are not, sort of, done by either the packaging SIG or the collector SIG, or language SIG. There's sort of community issues. And so, the question I have is, like, how do we force that?
how do we force that, those conversations to take place? And, you know, basically, it's this group, this spec call, and the people that are involved in the spec that need… that represent that, like, the community decision. And so, like, one idea is to, when there are questions about, like, what the default should be.
for these components, to open issues in the spec repo, or maybe not the issue in the spec repo, but, like, bring the issue in the packaging SIG to the spec call, and just add it to the agenda, and force everybody to talk about it and consider it.
Just to draw more eyes to it. And on the… on the central definition of, like, what it means to be injectable.
That seems like something that can obviously live in the spec repo. So that would be an opportunity to sort of have the conversation, to, you know, to debate each other, to dissent, whatever, and make everybody aware that, like, you know, in the process of having that debate, everybody sort of comes to terms and sees that this definition of injectable is emerging.
So…
**Michele Mancioppi (Dash0 Inc.)** 46:55 In the packaging SIG, we were assuming that we would have to write a note up.
About what it means for a package to be a language to be auto-injectable. Yes.
And added to the spark that way.
Then…
**Ted Young (Raintank, Inc. – Grafana Labs)** 47:09 We already cover configuration in the spec repo, so I think it's totally natural to… To extend that with packaging.
**Michele Mancioppi (Dash0 Inc.)** 47:18 Nope.
And by the way, so something that also it's likely to happen is, for example, right now we are having And it is something that I'm very open to discuss with the operator SIG.
Right now we have system packages in the packaging SIG, we have container images.
In, in the operator.
it's the same software package in slightly different ways. There is the, the operator can do more. For example, now it injects instrumentations for NGINX, for Apache HTTP that are not in the package in SIG yet.
I think those things should just converge.
The, as, as unwise, it may sound from my side, but we should move that stuff into a packaging SIG, because ultimately, they're just different form factors for the same experience we want to deliver.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 48:12 Yeah, just the final step of, like, how they're bundled is slightly different.
**Michele Mancioppi (Dash0 Inc.)** 48:16 Yeah. It's also, like, to some… to draw some… differences, for example, if you are, if you have different container images, you are, you are going to have a, less restrictive approach to dropping telemetry because you're not upgrading in place. There is a few things there, but ultimately it's the same thing.
Speaking of configuration.
That's, the reason why, we do not have support for Ruby in packaging yet. Ruby has recently released A, auto-instrumentation gem.
But Ruby does not yet have support for declarative configurations, which is why there is no Ruby system package yet. And declarative configurations is a necessary ingredient to the system package's experience.
Some people are working on that.
So I, I hope, in the foreseeable future, we bring another language in the fold.
At least in the early stages of system packages as they are right now.
Riccardo has the hand up.
**Riccardo Magliocchetti** 49:29 Yeah, just a question. You mentioned, that we, as in Python SIG, broke the… They are a great path to let's release.
Have you already reported it?
**Michele Mancioppi (Dash0 Inc.)** 49:43 Yes, there are discussions. Diego was going to talk about it. There is threads in both the Python channel in Slack, and in the packaging channel in Slack. If you want, we can cover it again offline, but it was, It's a rather unfortunate situation, I thought.
**Riccardo Magliocchetti** 50:07 Okay, thanks. We'll take a look at the Slack transfer.
**Michele Mancioppi (Dash0 Inc.)** 50:15 Diego?
**Diego Hurtado** 50:17 Yeah, sorry, just for the record, Riccardo, we are, We wanted to discuss this last week, but we waited for this week so that you will come back.
the Python SIG.
**Michele Mancioppi (Dash0 Inc.)** 50:41 Any questions?
**Ted Young (Raintank, Inc. – Grafana Labs)** 50:48 People should try it.
**David Ashpole (Google LLC)** 50:51 Yep, thank you so much for… for giving this update.
**Michele Mancioppi (Dash0 Inc.)** 50:55 My pleasure.
Oh, yeah, one last thing. The, the, effectively, so we have, some work to be done at the level of the project of the quality of the content delivered by the packages.
The biggest functional gap we have at the level of the packages themselves is the building and hosting.
We have POCs, so that we are covering two package ecosystems right now, the DBN derivatives and the REL slash Fedora.
We have two POCs, one by Denis for using Copper for Fedora, and one from Sina, from Canonical, using Launchpad, and it's something that we are going to look at.
We could not find, one single build system and hosting that, would… Provide a good experience.
We are going to need support at the level of infrastructure, for example, to, set up a, a proxy to expose, like, a consistent URL and consistent SSL certificate in front of the… of the packages, and probably a bucket where we can put the binaries, so, Yeah, when we have an understanding whether Launchpad and Copper are the places where we want to build the packages, then we will need some help in terms of hosting the outcome of the build, somewhere that doesn't… Bind us in unfortunate ways to infrastructure that could go away tomorrow.
This means, effectively, two things, three, DNS name, SSL certificate, and signing key for the packages.
If any of these changes and users need to change configurations in their APT sources, and that is a terrible experience.
Autumn?
**Aaron Abbott** 52:54 Yeah, my question wasn't about this, but I was gonna ask about, like, the release qualification process, and if there's some way that Language SIG can help there, so… maybe if we publish pre-releases, or we can test against HEAD, we can, I don't know, maybe come to some… some way to catch problems early, especially since this seems like a really…
**Michele Mancioppi (Dash0 Inc.)** 53:16 The, one of the ideas we have in the package and SIG is that, when we agree on what it would take for a language to be automatically injectable.
then in the language SIG, the validation of those requirements have to be part of the CI.
the process of generating the packages for a local test environment is pretty straightforward, and it's something that we could give as a GitHub workflow. And then a battery of tests for bunch of… I'm gonna take Python, because we're speaking about a bunch of Python applications, and try out with a collector nearby to see which data it generates. And that is, for example, the same kind of end-to-end tests that, at the Zero we use for our automatic instrumentation.
I've used them at the Instalna before. It provides… when done well, it provides, Pretty excellent coverage.
To avoid, Language 6 from breaking the currently unspoken contract of what it takes for a language to be automatically injectable.
And hopefully, we're going to make that contract explicit soon enough.
**Aaron Abbott** 54:32 Yeah, sounds great, thank you.
**David Ashpole (Google LLC)** 54:49 Awesome.
Thank you for that.
We have a few minutes left, if there are any other topics.
Otherwise, thank you everyone for joining, and I'll see people next week.
**Trask Stalnaker (Microsoft Corporation)** 55:05 Bye.
**Liudmila Molkova** 55:06 OPM.
