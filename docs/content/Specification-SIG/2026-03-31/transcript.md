SIG: Specification SIG
Date: 2026-03-31
Duration: 67 minutes
============================================================

## Zoom Recording Transcript

Jack Berg 00:02:55 Hi, everyone.
Trask Stalnaker 00:03:01 Ayy.
Jack Berg 00:03:02 We've got a packed agenda today. All right.
We'll give it 2 minutes, and then we'll get started.
Pellared 00:03:41 Hello, can you hear me?
Jack Berg 00:03:44 Yeah.
Pellared 00:03:45 Awesome.
Nice to see you all.
Jack Berg 00:03:49 You as well. Hope everybody had a good time at KubeCon.
Pellared 00:03:53 It was great to see somebody.
Alive, not just on Zoom call.
Jack, you're muted, because I think you're already…
Jack Berg 00:05:18 Sorry about that. Yeah, okay, let me repeat myself. Okay, so it's, we have a smaller… audience than normal, but it's 3 after, and we have a full agenda, so let's get started. Carlos has the first topic.
Carlos Alberto Cortez 00:05:33 Yeah, I have the first few ones, sorry about that. Yeah, the first one is this step, which is about, Exposing resource attributes information to an ex… the process. This is mostly for, If you give.
And, it's an OTEP, this is some extension that some SDKs can add. There are many prototypes, and as I just said, this is an optional thing that SDKs can implement, so it's not something that SDKs, all of SDKs will have to implement. We have enough reviews, which, for an epist, we need four.
Well, yeah, in case you want to say something, please, this is the time to do that. Like, grid this corner later. But otherwise, since we have enough approvals, probably would be a good idea to merge it by the end of the week.
Jack Berg 00:06:27 And, Carlos, were you planning on merging this at the end of the week?
Carlos Alberto Cortez 00:06:31 That was my proposal, not my plan. Okay. I don't know, like… So, I guess that thing is that I am not an expert on this one, even though I did my best to review this.
But at the same time, I feel like Ivo has been trained to push for this.
Updating the document very often, and all that.
Jack Berg 00:06:56 I think we lost Carlos.
Ivo Anjo 00:07:13 So yes, while we're waiting for Carlos to come back, I'll just say that, yes, I think I've tried to address all of the points in the doc, but if anyone has Thoughts, concerns, please do share, chime in.
Reiley 00:07:30 Yeah, my proposal would be we merge it by end of this week, and I can handle that, and we leave a note in the… AgendaDoc, letting people know that if they… Haven't got a chance to take the last-minute, like, scan.
and they want to see if there's any, like, late update they want to comment on, they have, like, 3 days to do that. Otherwise, we'll just merge.
Jack Berg 00:07:55 I'm just gonna comment on the PR to that effect, Riley.
Reiley 00:07:58 Yeah, thank you.
Pellared 00:08:02 And just maybe add a few sentences.
this OTAP. So, first of all, people, thanks for it, and it's in my to-do list to review it again, like, since a few days, but I will do it in a few days. I just want to say that we had some discussions.
around EV, OB, and other, like, SDKs interoperability, and we think it is very cool, and we are… we… I think… most of the community, if not all communities support it, and we are even thinking about scenarios like, SDKs should be able to tell, for instance, what is instrumented by SDK, what instrumentation is already there, so if something is missing, then OB can add missing stuff. So, yeah, I think this is a first step.
And it will be further improved later.
Jack Berg 00:08:50 Great.
Alright.
Well, we're over the one-minute mark for this topic, so, Carlos seems to have dropped, so let's skip the next couple of items and move on to, Robert until he gets back.
Robert, do you want to talk about… This decoupling topic?
Pellared 00:09:16 It's like, yes, please feel free to share, because at least you'll… the type box.
So, this is about, trying, like, improving the environmental variable context propagation.
this is basically, so I was, I'm bad at names, but there was, there was a new module, or in GoConstrip, to add the context, environmental context propagation carrier.
And when I was reviewing it, I was simply trying to polish the documentation, because a lot of things which were specified here was overlapping with existing like, kind of responsibilities of the propagation themselves. So this is, like, more of the cleanup PR. It also matches the current implementations in other languages.
There was only one implementation which does it a little bit differently, which is in Swift. I tried to reach out to the Swift maintainers. Unfortunately, they're not responsive since more than two weeks already, and I even made a PR for Swift, which resembles other implementations, which is more composable and can be used with more, more propagators than just trace context, if I remember correctly, and trace state, so yeah, And I also try to basically… I just want to make sure that this document is well-written, so it's easier to be adopted by more languages. So, it's more about… this is more like clarification and removing stuff which is kind of unnecessary here, because this should be not the concerns of the propagation.
And he already has, like, 4 approvals, but… and I think it's good to merge, but, you know, I just want to call it out if any one person, you know.
Things that they want to call out, and… yep. Agora.
Jack Berg 00:11:10 No, you know, I was looking for… because I saw a bit removed that looked like it was related to, the normalization process, and, and it, like, and I was looking to make sure that that normalization behavior was still reflected in this document. It was just collapsed, so I found that…
Pellared 00:11:31 It's still there. Yeah.
Jack Berg 00:11:35 Okay, yeah, this makes sense to me. I, too, was a little confused when I was reviewing the Java PR for this, and seeing references specifically to, you know, baggage and W3C, propagation, so… Yeah.
I'll give this another review, and probably an approval.
Pellared 00:11:56 Thank you.
Jack Berg 00:11:57 Any other comments?
Alright, moving on. You have the next topic as well.
Pellared 00:12:13 You're familiar, Jack, so you can even, you know, Share yourselves.
Jack Berg 00:12:19 Yeah, okay, maybe I'll share this myself, just for a change of pace. Okay, so, a number of different language implementations have identified the same class of bug in the OTLP exporters, and the bug is that the exporters don't have any protection mechanism against large OTLP responses.
And so, you know, there's a vulnerability that can happen where a compromised OTLP endpoint exhausts resources for an application by issuing large responses, and therefore large memory allocation in applications that are exporting over OTLP.
And so… what Robert's done here, and I think this is a great thing to do, is to update the proto-specification, to add clarifications on the requirements of OTLP, OTLP clients in terms of their behavior around, responses, just so that, you know, according to the spec, there's, like, you know, built-in mechanisms to protect against this, or safeguards.
So, yeah, please take a look at this, and if you're a maintainer, I think I've looped in all of the maintainers at this point, but please take a look at your OTLP exporter implementations and, and decide whether it is vulnerable to this type of exploit, and if it is.
Please, you know, rapidly provide a a fix to that. And, you know, there's a number of PRs that Robert has linked here about how this has been fixed in other languages.
So, any other… anything else to say, Robert?
Pellared 00:14:06 I have a question myself. Yeah.
Do we want, as a following PR… Say something about the server implementation, that they should not, you know, kind of give such big responses, for instance, for partial successes, and trim the result, and say something, you know, some of the data points were incorrect, and just give a few samples like that.
Jack Berg 00:14:33 That's an interesting point. So, you know, what you've added here is you basically establish a 4MB, default limit, or recommended default limit, for clients, and so… in a sense, that is guidance to a server, right? So, a server that exceeds 4 megabytes will, you know, have clients that, you know, have these resource-exhausted errors and other sorts of, like, unretryable errors, so… we could make that explicit. We could have some sort of link in the server portion of this document to just, like, you know, make servers aware of this client recommendation, something like that, so they're not flying blind.
Pellared 00:15:18 work on it on a future PR. I didn't want to do this one, because it would be a scope creep, and I think it will be a lot harder to establish what the server should do in this, you know, kind of… what should… what is the expected behavior. So I will work in a future PR, try to address it somehow.
I added this as a follow-up in the description.
I added this as a follow-up, to the PR description.
I think it's my last comment, also.
Jack Berg 00:15:45 And I think Armin talks about, an example.
Pellared 00:15:49 Yeah.
Jack Berg 00:15:49 What a large response might look like.
If I can find it…
Armin (Dynatrace) 00:15:56 Second comment.
Jack Berg 00:15:59 The second comment?
Armin (Dynatrace) 00:16:03 And then you can… yep. Yeah.
Jack Berg 00:16:06 Oh, right, it's a collapsible, I see.
So, like, what… just hypothetically, if we… in this follow-up, Robert, so, you know, this is an example of a long response, and if a server is generating a long response, but detects that its serialized representation would be over 4 megabytes, it would be something like, hey.
When you're approaching the 4MB limit, like, scrap additional details, or, like, reduce your verbosity in some way.
Pellared 00:16:38 This is the idea.
Armin (Dynatrace) 00:16:40 Or only lock the first, so many arrows that, that fit.
Jack Berg 00:16:46 Yep.
Daniel Dyla (Dynatrace) 00:16:48 It may also be reasonable to just… remove the resource and attributes from this. Like, the… just the metric name… Is likely enough to track something down.
Jack Berg 00:17:06 I think it depends, like, that's kind of what I meant with, like, reduce the verbosity. So, like, the verbosity can come in the form of, like, you know, repetitive messages, so you kind of repeat messages with the same shape over and over again for each metric or each data point. That's, like, more verbose, or, you know, the detail level. So, you know, with each message for each metric, you give a lot of details versus, like, a few details, so… Yeah, I think that's gonna be why Robert wants to break this out into a separate PR.
Okay, so, Let's see, we've got approvals from Armin and myself. Does anyone from the TC side want to volunteer to merge this?
If not, I can.
Alright, we'll wait for a couple more.
Reviews on that?
Or to the end of the week, and then we'll get that merged.
Okay.
This is… seems related.
Pellared 00:18:21 Yep.
Jack Berg 00:18:28 Wait, didn't we already look at that? Which one are we looking at?
Pellared 00:18:32 It should be 8, 782.
Maybe just, maybe my hype link was wrong.
Jack Berg 00:18:39 Okay.
Pellared 00:18:41 cup.
Jack Berg 00:18:48 Oh, so this is a new one.
Pellared 00:18:50 Yeah, so this is a new one.
for the servers, so I even checked how the OTLP receiver and collector handles it, if someone would like to, you know, just put a very, large payload. So, the OTLP, receivers and collector already handle it, this kind of… So, the previous PR was about The response, this is about the request.
Handling request, not the response.
And, here… I… this language here, I tried to, I tried to describe what the OTLP collector does, the receivers. However, I am concerned with the limits that are currently on the collector. And here, it's just a call to the… mainly to the profiling SIG. If 4 megabytes is large enough for the profiles, because it seems very low for me. And this is the current default for the OTLP Recyverse.
Jack Berg 00:19:49 And also the 20 megabyte, the difference.
Pellared 00:19:51 I think it… yeah, I think it's… It probably is reasonable, but I'm also not sure.
Jack Berg 00:19:58 I just mean the difference between gRPC and HTTP. So, like, that's kind of interesting.
Pellared 00:20:04 Yep, indeed.
I think I added my comment myself. I think we added… Jack, I think I already did the same comment as yourself. I'm just not sure where… It's outdated, probably, yeah.
Jack Berg 00:20:37 Oh, yeah, I see. Where we agreed on the same size for a gRPC and HTTP.
Okay, so this is, this is probably slightly lower priority than the client side of things, but, Still something that should be addressed.
Alright, so please review and, leave your comments. Thanks.
The next topic.
Reporting, aggregated… Errors and exceptions.
Robert, take it away.
Pellared 00:21:20 Okay, so in Go, it's a very… popular, that the errors that are reported are, like, wrapped, or they're joined, multiple errors.
In .NET, there's something like aggregated exceptions.
when… even when you use some async code and using the async libraries, and there are some… and you're joining, joining… the result for multiple, like, asynchronous methods, and if some… some… you can get aggregated, like, async exceptions, stuff like that. I think in Java, there's also, like, concept of inner exceptions, if I am not mistaken correctly.
So I was trying just to put out some semantic conventions around that, that is as much language-agnostic and reusable as possible.
Because there are a lot of patterns, you can, you know, draw in aggregate, etc. And then… I do not think… I think just putting it as an array, like, even… like, putting arrays probably is the easiest way how… how we can handle it, but yeah, I think… Yeah, forego… It's really problematic, because we added this capability that TrustQ recently added to the Logs SDK of setting the error.
So… already people reported, like, problems that just having the top error does not provide you enough information, and they would like to, you know, have the deeper… they would like to have the deeper information.
on the attributes. So, yeah.
I need feedback here, and at least for Go, it's kind of important.
Jack Berg 00:22:58 I see Lyudmila and Traska on the call, I think, and Armin.
who have all been deeply involved with semantic conventions. I know that there's been a lot of debates about Representing exceptions, representing errors over the years. I'm sure this has come up before, or something like a question of a similar shape.
Liudmila Molkova 00:23:22 Yeah, I think I need to spend some time thinking about it, I'm not ready to… Talk about it right now.
Jack Berg 00:23:29 Okay.
Liudmila Molkova 00:23:35 Robert, should we bring it up on the logs call later today?
Pellared 00:23:39 Otherwise, yeah, there's like that, if I'm not mistaken.
Jack Berg 00:23:46 All right, I guess the one question that I have, so that it doesn't just all happen on the logs call, or semantic conventions call, is, like.
Suppose… Suppose you do have an exception, which is, like, some sort of composite.
you know, right now we have this record exception operation, and it's on spans and on logs, or spans in the form of, like, you know, it's captured as an event, and on logs, it's just recorded as attributes on the log record.
Are you… in your head, are you imagining something where, you know, you're proposing things like, like, maybe this is one of your proposals, there's different proposals, but in one of them, there's different except… there's different attributes to represent a composite exception versus, like, a singular exception.
And would, you know, would you imagine, then, that the record exception operations are sort of, like, the behavior becomes dependent on which type of exception is detected?
And.
Pellared 00:24:51 Indeed.
Jack Berg 00:24:52 Okay.
Liudmila Molkova 00:24:58 I don't see this listed, Robert, and maybe I missed the point, but shouldn't we leverage complex types here?
So you're right there, why do we need to flatten down types?
Messages…
Pellared 00:25:12 I think it's easier. I think for backends, it will be just easier to… to index them, etc.
I was thinking about using Complex, I'm just not sure if it's not an overkill.
people probably just want to, you know, filter out for… filter out for the error types, etc. Yeah, I think it's an option.
I just didn't put it because I'm not sure if this is the efficient way to be doing it.
Liudmila Molkova 00:25:40 It's the most flexible way.
Backends can always serialize if they need to, but, like, merging different arrays by index is not… Awesome.
Pellared 00:25:52 Yeah, we can put it later, or I can add it.
Yeah, next bullet point.
Jack Berg 00:25:58 One thought, and I just… I'm making this from, you know, the experience of, you know, writing backends that consume this data and look specifically for these error attributes.
So I'm thinking about, like, sort of backwards compatibility, and, like, you know, if you went with this option of 3, where there's this, like, plural.
version of the attributes. Like, I wonder if you could do both, where you could populate the plural version of these attributes, and also populate the singular version with some sort of, like, well-known marker or something that indicates that you should look for the plural version.
Liudmila Molkova 00:26:38 Yeah, it also, at least, I think in .NET and Java, there is a composite type.
Right, and you would keep the singular. It's still, let's say, aggregate exception.
But yes, there are some extra attributes that describe individual exceptions, or an extra attribute that describes the typed exception.
Jack Berg 00:27:04 Yep.
Aaron Abbott 00:27:06 I was just gonna say we have exception groups in Python, also. But one kind of interesting thing is, it's like a list, but you could have a list of exception groups.
So you get this kind of, like, tree structure.
So the stack traces render nicely by default in Python, which is handy.
But, like, if you just do it, like, at one level to capture the types, I'm not sure how… I mean, maybe it's enough, just a thing to think about.
Trask Stalnaker 00:27:37 Yeah, I think that part that I'm missing, Robert, is in… because, like, Java is like Python there, where, like, you have a primary exception, and you can attach causation or suppression… suppressed exceptions to that exception.
So you always have a main exception, and so that is the type that we capture, and the stack trace renders, you know, all of them together.
So… Are you wanting to have all of those caused-by types?
essentially… At the top level, to be able to report on them.
Or does Go… like, you don't have a primary exception?
And so you need…
Pellared 00:28:29 In this proposal here, I propose to have always this error type, which is, like, the primary, the top level.
and add additional these error types, which will be, like, the causers, but this is just one proposal, and this is why I bring it up here, because maybe it is indeed better just to, you know, model the error attribute in the way that they were really composed. Like, have these inner… inner errors and compose them inside, so yeah.
Trask Stalnaker 00:28:55 Because that starts to blend into the… there's a long-time open issue about modeling exceptions as structured More, width structure, so having, As opposed to, right now, just the massive stack trace, which has… You know, you're… Type name, your file name, your line number, your causation, Cosize.
Pellared 00:29:27 So the structured error may be a way of, kind of, addressing this issue.
Is what you say?
Trask Stalnaker 00:29:36 Yeah.
Liudmila Molkova 00:29:37 Or probably there are… I'm sorry.
Trask Stalnaker 00:29:41 if I'm understanding the motivation, which I'm still not quite sure, because if I was mapping this to Java.
That's what I would be… I'm… my understanding is you want to be able to capture the structure, not necessarily just that there are multiple… Top-level exceptions you want.
The structure of the top-level exception.
Pellared 00:30:08 Yeah, this will be ideal.
I agree.
Liudmila Molkova 00:30:11 It's probably both, right? So there is the exception that we want to record better, and as a part of the information than the exception, there could be multiple other exceptions.
And then it's an aggregate one.
Where the one with the causes.
Trask Stalnaker 00:30:32 Right, but in a complex… a complex attribute, those Would be nested under the exception.
Liudmila Molkova 00:30:45 Yeah, so we can have the same solution for these two problems, or it could be two solutions, and I don't know if it should be one or two different ones.
Like, if the stinks are… Different enough, yeah.
Jack Berg 00:31:16 Alright, so we're gonna pick up this conversation asynchronously, and maybe in the logs later today, is that right?
Pellared 00:31:24 I have just one, ask, Trask, are you able to find this, issue regarding the Structured error, and link it to the Sikh agenda.
Trask Stalnaker 00:31:33 Sure.
Pellared 00:31:35 Thank you.
Jack Berg 00:31:37 Yeah, I remember that issue. If I were to guess.
I bet it's one of the most upvoted.
I don't know, though.
Maybe not.
Alright, I'm not gonna dig around for it right now.
Liudmila Molkova 00:31:53 We promised, when we did complex attributes, that we will not revisit the existing attributes and start introducing structure.
But yeah, for maybe it's the… the new thing.
Maybe they can coexist.
Jack Berg 00:32:17 Okay.
Carlos.
I see you're back. The next topics are yours. We pushed them to the end of the agenda because we lost you.
Carlos Alberto Cortez 00:32:29 Yeah, my internet has been wonky today, and nobody's… nobody from my, service is trying to fix it, seems, but let's try. I'm turning my camera off.
Hopefully that will help.
Yeah, the first is mostly just an iteration on this step, Basically, we don't… well, we don't have to discuss it here. I already summarized what's the latest.
big, important update last time, like, two weeks ago or two weeks ago. If you could actually come back in the document, Jack, there are some questions that I would like to discuss briefly here, or probably just for people, you know, to think about.
The first one is that I made some clarifications on how this is expected to work. I think that the initial object that Christian posted was initially a little bit vague on how it just would work. Now I am making it clear that when you have context scope attributes.
Those attributes are attached to the telemetry item, like span or block record item, right at creation time.
So that's hopefully clearer for, the maintainers.
The second thing, based from feedback from David, Ashbold, and CEO, is that now, the context part, which is purely DPI, So there's no split between having these, calls defined in the API, and you actually define the actual propagation of the SDK. Now it's… That's in the APA. And the SDK only consumes that.
That means that users can actually go and see what's in the context videos if they want to. I think that's totally not too… not too dangerous.
The third, and that's probably the most, important thing, is whether metrics should be the same by default.
daily dashboard, you were, Suggesting this, but, Sam, who is another commentator.
Think that we shouldn't go for this.
So I would like to… I think Sam's not hearing the call.
Well, that's probably something for, you know, for discussing offline. But that's an important one, because we have to decide, I mean, it's not okay, we can still change that, but it would be great to at least understand what would be the consequences of Making things, enabled by default or not on metrics.
And finally, the, the configuration part is that… and that's… This will be affected by the previous point.
Because… depending on what approach we take, we need to make configuration more or less granular. And Jack, you see your point, yeah, we… Yeah, I think that it's a good idea. It's a good trade-off that for notep, we have a rough idea, and then we just iterate on the… On the spec, making it super clear what we need to have, In the end, even if we don't have a specific, set of details.
Yeah, OTEP's our…
Jack Berg 00:35:34 Sorry, just… OTEPs are never the final say, and even the spec merged PR isn't the final say. It's not final until it's in the spec and it's stable, so, you know, we don't need to have all of the argument up front.
Carlos Alberto Cortez 00:35:51 Okay.
Liudmila Molkova 00:35:54 So, I wanted to talk about metrics as well, and the defaults. So… from… we had a bunch of use cases for this in, let's say, GenAI-Seq, and most of the use cases involve high cardinality attributes.
And it's also my intuition that most of the context attributes would be somewhat harsh cardinality.
So, it would be… Dangerous to enable metrics by default.
But also, if user explicitly wrote a code that added context sculpt Attributes. It would be wrong to… Ask them to also enable them.
So I think we… there are two things. First, we definitely need per-signal configuration.
I think it's the… the… we need to start with it.
And second, I think we should consider different defaults for different signals.
And… besides this.
I think we should talk about, is it a good idea for instrumentations to ever use it?
I… again, my intuition tells that if one instrumentation Does it wrong, then it could be very problematic for the whole application.
But having it in SDK only is also not a great solution. It just changes everything we do, and I don't know, the extensions, for example, that… things like vSpan and Java.
This… they would need to depend on SDK to provide access to this API, and it would not be great. But at least we should… I think we should decide if we ever recommend auto instrumentations, too.
said context scoped attributes, and I think the answer is no.
Carlos Alberto Cortez 00:37:52 Yeah, correct. I think that this was the motivation that Christian also had when he made… wanted to make this separation, that instrumentation, you know, they don't access this.
Sorry, Jeff.
Jack Berg 00:38:04 I was just going to clarify something that I'm pretty sure you said, but I just want to reiterate it. So, you know, I was thinking the same thing about, like, oh, should instrumentations be able to use this? And if If we say no, because of the reasons you state, then it has an impact on the defaults, because, you know, you've laid this out. Like, if the user… if we always know the user is adding these context-scoped attributes, then they've already expressed the intent for them to be added to the telemetry, so we don't need them to opt in via configuration, so essentially opting in twice.
But yeah, the key question was, like, how do we restrict instrumentation from using them? And so, is this your idea? Add this capability to the SDK modules instead of the API?
Liudmila Molkova 00:38:48 This could be the solution, but I don't like it because it makes it hard for users to actually leverage it with zero-code instrumentation.
So I don't think it's a viable option, and the only way to restrict… well, we probably cannot enforce it, but at least we can.
advise instrumentations to never use it up until after instrumentations.
Jack Berg 00:39:18 Okay.
Liudmila Molkova 00:39:20 I… Yeah, I kind of feel that instrumentations will want to use it, at least the Gen AI ones, but… so I think we… We can start indo, at least.
With advising against it, but maybe we can find some safer means in the future.
Aaron Abbott 00:39:41 So just to be clear, that would mean that, like, a user or the person who writes the code would be the person using this API?
Liudmila Molkova 00:39:51 The end-user application.
Aaron Abbott 00:39:53 Okay.
Carlos Alberto Cortez 00:39:56 Okay, I will update the API… sorry, the tab to mention this part regarding instrumentation. Yeah, that's a good call.
David Ashpole (dashpole) 00:40:05 And I left this comment on the OTEP as well, but in terms of like.
defaults. I think that in most cases, you'll actually know At the point when you're adding something to the context, whether the attributes Are safe for use in metrics or not.
So I would actually prefer if this wasn't something that was Done via configuration, but that was where, at the call site, you could just say.
Here are some attributes. Oh, and by the way, they don't apply to metrics.
Or they… You know, or they do apply to metrics, whatever we want the default to be.
Liudmila Molkova 00:40:44 Like, some marker of high cardinality.
David Ashpole (dashpole) 00:40:47 Yeah, or… right, I think the… whatever the… the default, I think we can argue over whether, like, you should have to opt in or opt out, but… some way to say, like, oh yeah, here I'm adding a thing that's mostly constant.
Or here I'm adding a thing that is an ID associated with My user, or something.
That's gonna end up being high cardinality.
Jack Berg 00:41:10 You know what's interesting about that, David, is that, you know, if you… if you start to add those capabilities at the… at the call site.
you know, some sort of annotation to indicate whether it's high cardinality. And maybe you extend that further, where it's, like, you know, some sort of annotation to indicate whether it's applicable to, you know, all signals, or metrics, or traces, or logs. And so, like, if you're doing all that at the call site, it starts to make configuration at the SDK seem, like, redundant altogether, and maybe that's a way that this could play out.
is, like, there is no configuration. It's only, you know, the only way that you can control this is, you know, programmatically at the call site.
David Ashpole (dashpole) 00:41:54 I think it's nice to have a big red button.
But otherwise, yeah, I agree.
Like, turn on… TechScope attributes if they're causing problems, but yeah.
Jack Berg 00:42:03 Yeah, exactly. So, like, if you… If you, if you have all of that expressiveness at the call site, then you're… you can accept a much simpler configuration surface area, just a big red button, right? Rather than, finer granularity.
David Ashpole (dashpole) 00:42:19 And to be clear, I don't… I wouldn't say that they don't apply to metrics at all.
I would love to see them Apply the same way that our, like, default disabled attributes do, where you still get to see them on exemplars and stuff.
But they just don't add to the cardinality of the metrics.
Carlos Alberto Cortez 00:42:43 Okay, so I guess we can keep, discussing this offline. As I mentioned before, I would like to get some answers for Sam at the end of the commentator besides David and, Tyler and Robert. Yeah, the important part is, like, depending on that is, like, how much we can go Configuration-wise.
The minimum will be, as Lumila said, by signal, but depending on that, we may decide to make it You know, to try to explore a little bit more in detail.
how more configuration will be needed. Also, from the API side, like, hey, David, with your snippet, like, basically, we would have to massage a little bit the new API calls, for example, so that will depend on this one. So please, yeah, provide some feedback, everybody.
jmacdonald 00:43:34 Hi.
Can you hear me? This conversation, I'll put this feedback on the PR, but I just wanted to say it kind of reminds me of how the profiling group is proposing to add units to attribute values, and here we have a discussion about sort of metadata applied to attributes, and it's making me think whether this is an opportunity to revise our attribute interfaces, perhaps to create a first-class API for registering attributes, maybe statically, so that you could put this information not at the call site where you're instrumenting.
but at the top of your file, where you declare your schemas and your metadatas, or maybe even in a configuration file, or a schema file somewhere, where you say, this attribute, here are its units, it's high cardinality, so recommending not to use it for metrics, except exemplars and so on, would be something I would be leaning towards if I were given the opportunity. Thank you.
Liudmila Molkova 00:44:27 This is a perfect example of what we can do in semantic conventions, where we can describe which attributes are sensitive for cardinality units and whatnot, and the schema is exactly the semantic convention schema, and it fits nicely in the code generation, where we would just generate this code altogether.
Without users thinking much about it.
Jack Berg 00:44:50 Yeah, so essentially capture more metadata with the attribute keys, right? So the metadata being the unit and potentially some sort of description of which signals this is applicable to, or the cardinality.
Liudmila Molkova 00:45:03 Yeah, and it doesn't need to even be passed to OTLP, right, because this is the… the within API or SDK only concern.
jmacdonald 00:45:16 Or you could treat the registration of attributes like an event. Like, here I am registering my attribute, this is its description, it becomes a log event or some other type of, you know, sort of meta signal.
Jack Berg 00:45:35 Okay, any other comments on this topic before we move on?
Liudmila Molkova 00:45:40 I have a small ask, Carlos. I think there are a lot of proposals in the SATAP, and probably they are historical ones. And maybe we can just remove them, because I don't think we are seriously considering getting another Prada layer of attributes for these things.
Carlos Alberto Cortez 00:46:00 Yeah, actually, I was wondering the same. The historical reason for keeping them, if I remember correctly, is that back then, which was, like, 4 years ago, Christian received, the regional authorities attempt. He received a lot of, feedback and a lot of counter-proposals.
Which people wanted to keep track in case, you know, this proposal didn't work. But yeah, I think that… Some of them are, too complex, you know, to say the least.
And, as I mentioned before, they were mentioned for historical reasons, but yeah, I think it's time to remove them. Okay, so if that makes sense, I would go read and just keep the ones that are realistically Alternatives, anything that… is not a great alternative, I would use from you.
Liudmila Molkova 00:46:47 Yeah, we can… We still have them and all that up, we can just link to it, and people can read.
Carlos Alberto Cortez 00:46:53 Yep.
Jack Berg 00:46:54 And in the Git history.
Yeah. Of this, Pierre.
Oh, right.
Carlos Alberto Cortez 00:47:05 6 points by… yeah.
This is a new issue, this is more related to a different issue as well.
You could open that issue Jack, yeah, first, just people… are in the loop. This related issue is about finding a stamp processor.
That emits span lifecycle events.
So, basically, this is, for long-running spans, mostly.
And, okay, so now we can go back to the previous point. And as part of this, which is, you know, an issue we have, and that is accepted and only needs a sponsor.
The thing is that, in order… so, the general idea is you have this spam processor that is reporting events.
Then you have all start, which you send initial information you get when you are creating a new span. And for on-end, likewise, you're getting the, you know, the status of the span.
And then you… you are sending hoard bits every number of, you know, seconds as configured in the processor. So… so the backend knows that this span is still live. However, we also want to report actual data Regarding span, And for that, we could send everything we have at a given moment, as part of the heartbeats, but that's most likely an overkill. And the thing is that you want to report what's the, The span name, which may change.
Attributes and links. We are describing events because, you know, they are deprecated, or they will be deprecated pretty soon.
And one alternative Besides sending all these spam, spam data together, is that we just add some hooks into spam processors.
This seems like a good solution, but of course, I know this can be polemical among, maintainers, so that's why I wanted to ask, for opinions here.
Jack Berg 00:49:06 Robert?
Pellared 00:49:09 I think, set span status is missing.
If I remember correctly.
But good otherwise.
Carlos Alberto Cortez 00:49:20 Jimmy Lincoln.
Daniel Dyla (Dynatrace) 00:49:27 Like, I think he's saying on span status change, or something like that.
Carlos Alberto Cortez 00:49:32 Oh, usually status is reported at the end, when Spanish ended.
But anyway, yeah, we can… Also report that in case it's, changed. I think… It's funny.
Daniel Dyla (Dynatrace) 00:49:44 I think there's also a set status… Method, isn't there?
Pellared 00:49:49 Yeah, but what Carlos says, that is probably good enough just to report it at the end, right?
Carlos Alberto Cortez 00:49:56 Yeah.
Pellared 00:49:57 Okay.
Same could be said for, you know, name change, in theory.
But maybe not.
Jack Berg 00:50:13 Yeah, so this is actually kind of pointing at this, this comment that I'm writing here. So, you know, you're trying to be able to add listeners for all the different types of things that could change on a span, and that's gonna get cluttered, because there's several fields, and we could add more fields in the future. What if you could collapse all these into a single on-change listener, where you can just have, like, a switch statement that allows you to listen for the specific Fields that you're, that you're interested in listening to.
But that's kind of, like, an implementation detail. I think, this question that you're asking, Carlos, is about, like, should we add this capability at all?
Carlos Alberto Cortez 00:50:55 Yeah, that's correct. I think that either way, with a single operation or multiple operations, either of them would work.
Well, yeah, you maintainers don't think this is an overkill for whatever reason.
If everything's fine, I think we can probably make progress in this one.
Jack Berg 00:51:18 Aaron?
Carlos Alberto Cortez 00:51:18 Yes, Araon?
Aaron Abbott 00:51:19 Yeah, yeah. So, maybe I'm out of the loop, but, could you maybe give, like, an example of what you might implement in one of these on-change listeners?
Carlos Alberto Cortez 00:51:30 Oh yeah, that's on the issue that Jack was opening earlier, with this, another issue where we are defining, you know, indirect decision is accepted, which is that we will be defining a spam processor that will be reporting spam lifecycle, events, you know?
And this is mostly for long-running spans.
That they may last for hours or days.
I'm… You don't want to keep such span… well, yeah, you keep the span in memory and all that, but you also want the backend to know that this is still happening, you know?
Aaron Abbott 00:52:04 Okay, so is it, is there, like, a specific OTLP thing that's supposed to happen, or is it kind of just adding a generic interface to start? Like, I could see you emitting logs or something like that, but yeah.
Carlos Alberto Cortez 00:52:17 So it could be, no, not… I mean, it's just, like, standard events, you know? With, like, certain of events, yes. And actually, for that, we would need to define semantic conventions.
For, those events.
But yeah, that's, we are not modifying OTLP, if that's the question.
Aaron Abbott 00:52:38 Okay. Yeah, I mean, I guess I see where it's going. So I was just, Out of the loop. Thank you.
Jack Berg 00:52:47 Hey, Carlos, two quick things that are coming up as I'm thinking about this. One, so, I think you need to think through the mechanics of… of when these listeners are invoked. So, are they… are they invoked recursively?
you know, if a listener changes the span itself, what happens? Or can a listener change the span, or does it just get, like, an immutable read-only copy of the span? And then, on a related thing.
on a related note, it's like… so you talked about, like, hey, I want… I have these long-running spans, I want to know that there's still… that something is still happening with them. Is this actually sufficient to solve that problem? Like, what if there's a long-running span, and… it's not changing. Like, do you want to have some sort of notification that is, like, time-based, rather than, like, change-based? Or does that not make sense? Like, basically, does.
Carlos Alberto Cortez 00:53:47 You're not listening to it.
Jack Berg 00:53:48 Pages solve your use case.
Carlos Alberto Cortez 00:53:51 No, I mean, that just expands. We have this notion of.
Jack Berg 00:53:58 I think… Carlos, if you can still hear me.
Carlos Alberto Cortez 00:54:01 configure a user, like, let's say Yes.
Jack Berg 00:54:05 Sorry, I think you're dropping off a bit, so I can hear you again now.
Carlos Alberto Cortez 00:54:09 Okay, great, sorry for that wonkiness. Yeah, so basically, the notion of 4bit It's also part of this.
Because at some moment, sooner or later, you may stop receiving updates on the span.
But we didn't want to send all the information as part of the hard bits. So now we are decoupling them.
So we would have all of these things, plus the heartbeats. But the heartbeats, for that to happen, we don't need that To, change the spam processor server.
Okay. That's just the span… the new spam process or internal stuff.
Reporting Gabriel Mina, for example.
Jack Berg 00:54:50 Got it.
Alright, any other comments on this?
Carlos Alberto Cortez 00:54:59 So, if that makes sense, I will create a prototype, which is the one, the part where we can see what would be the, any side effects.
Jack Berg 00:55:11 Danielle, did you have something to say?
Daniel Dyla (Dynatrace) 00:55:15 Yeah, I was just gonna raise that, actually more related to the heartbeats than this one. I had not seen it previously, but in some languages, you know, JavaScript included.
It lacks language features around… Like, being able to iterate over weak references. So it's… You know, it's not necessarily impossible to prevent memory leaks, but we'll have to have, you know, some sort of purge mechanism or something like that. Like, we don't know… in the… in the SDK, even, Whether or not some… caller… Still has a reference to the spam.
Or whether they've decided to just drop it and never end it. So, do we just continue heart beating forever? At what point do we stop heartbeating?
Do we depend on maybe this… requires, like.
an API method to call, like, this span is still alive, or something like that. I'm not sure how a heartbeat mechanism can work in a language like JavaScript, but I haven't looked very closely at that, proposal, so that might be addressed.
But I am getting an initial feeling that it might be impossible to do in a reliable way that doesn't cause memory leaks.
Carlos Alberto Cortez 00:56:37 Yeah, so in my prototype in Java, I use weak references.
But it's a great question, what could we do if not all languages?
transport these.
Daniel Dyla (Dynatrace) 00:56:48 JavaScript definitely does not have iterable weak references. It's, like, you can't… it has weak maps, but you cannot iterate over them.
There's no iterable week collections that I'm aware of.
Jack Berg 00:57:07 Robert?
Pellared 00:57:09 The initial PR before I created the issues in semantic conventions were about adding this, heartbeat events.
for long spans, and I didn't like this approach because of the reasons that Daniel Ruck right now mentioned. And I think, I think the one who is instrumenting the application, may not know, you know, what is the good amount of time when you want to report this. You know, this can lead to unbounded memory, like.
in my mind, it's just not a flexible approach. I think that just having these lifecycle events, you can just… yeah, I think it's just a more flexible approach, but this is just my few cents, and I just want to take… call out that it was in the initial proposal, instead of this span lifecycle operations to have hard bees for spans, and I didn't like this approach.
Daniel Dyla (Dynatrace) 00:58:03 The life cycle doesn't solve the problem, though, because if you start a span, and then, you know, never end it, and you drop the reference to it, and the garbage collector picks it up, you won't receive any more lifecycle events.
Pellared 00:58:20 I don't follow.
Could you repeat? Why doesn't it install?
If you don't… if you get the spend that it has started, and you never got an event that it… was… It was not ended.
then you can have a backend, which, I see.
Daniel Dyla (Dynatrace) 00:58:38 Yeah, you have to have a timeout. You're in the same position you're at. That's no different than having on start and on end.
Josh McDonald has his hand raised.
jmacdonald 00:58:52 I… I wanted to add to this conversation, like, this… this… we've merged… we've moved into talking about leakage of tracers or something, something along those lines. It's, like, a problem as old as tracing itself.
And I kind of agree with Daniel that there's not a… there's often not a solution, because the semantics of the language give you the power to hold something forever.
And… the solution that I have seen for that is to break the kind of model into having a reference. Like, you have a reference to a span, and the SDK is considering that, like, an aggregate, that it's computing. The span is an aggregate of events, and it will keep them alive as long as it needs to, and it's waiting for the end event.
Or it's waiting for some kind of event to keep it alive. Like, you have to use the handle if you want it to stay alive, and that's on you somehow. So, like, as was mentioned, you could have a new interface, like, keep me alive, or you could have, like, a… tell the user to just set another attribute, or overwrite an attribute every minute.
And then configure your SDK with a 2-minute timeout. That's the solution I've seen for this going back, you know, as long as time.
on this topic. Thank you.
Carlos Alberto Cortez 01:00:02 By the way, my prototype touches on a lot of those things, which I thought they were this thing, but maybe it's easy only for Java, and for some languages, but I guess that we only have two minutes. The big question is, what… what do people feel we should do if This can be implemented.
in most languages, but they cannot in some others, because there are limitations that even like these, you know, suggestions are similar, they cannot be implemented. Do we support this? We don't support this at the specification level.
I'm not sure.
Daniel Dyla (Dynatrace) 01:00:34 I would say, you know, as a maintainer of a language, that is a limiting factor here.
I wouldn't want one language to limit a feature from another language if that feature is legitimate and useful.
You know, there's other ways that this could be implemented.
you know, as language-specific workarounds. If it works in other languages, and JavaScript has to have a keep-me-alive function, then so be it. Or maybe… JavaScript spans can have, you know, R event emitters, and every now and then they… they call some callback that says.
you know, return true if this span is still alive, and then we control the timing, or something more along those lines. You know, there's workarounds that can be done that make sense in JavaScript, or, you know, at least aren't terrible, that don't make sense in other languages, and I think that we… I wouldn't want the JavaScript limitations to leak into Java.
Jack Berg 01:01:41 Well, I've got to call time on us, so if you want to keep this conversation going, let's do it asynchronously. You know, we can continue with prototypes and conversations without having to answer these questions up front, so let's do that and see if there's language-specific workarounds.
As a parting note, I added a late agenda item. I'm looking at Josh McDonald here and anybody else that's interested in metrics. There's a long-standing issue to add support for bound instruments for open telemetry. I'm proposing switching this from community feedback to accepted and, you know, and volunteering to be the sponsor for this, so if anybody disagrees with that, please comment on the issue, else I'm going to pick it up and move it forward.
Thanks.
And with that, I'll see you all next time, and on Slack. Take care. Bye.
