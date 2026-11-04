SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-11-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:28 Hello, hi everyone.
Andres Borja 00:01:37 Hello.
Liudmila Molkova 00:01:41 Well, I'll get started in a few minutes.
In the meantime, please… And your name?
And if you have anything to discuss, please add to the agenda.
Do we have any fun stuff for the KubeCon?
Does anybody know?
Jason Plumb (Splunk Inc.) 00:02:44 Just contribib fast.
That's pretty fun.
Liudmila Molkova 00:02:51 Which day?
Jason Plumb (Splunk Inc.) 00:02:54 I… don't remember, but I think it's the Tuesday or Wednesday, it's not Thursday.
Dmitrii Anoshin (Splunk Inc.) 00:02:59 It's Tuesday.
Jason Plumb (Splunk Inc.) 00:03:00 Okay.
Liudmila Molkova 00:03:04 Nice. We don't have, the observatory, right?
Dmitrii Anoshin (Splunk Inc.) 00:03:10 Not this time.
It's Tuesday, 11.30.
Ted Young (Raintank, Inc. – Grafana Labs) 00:03:16 But I think we have maybe more space in the project pavilion.
But… We can just go take over the project pavilion. That's what I say.
Liudmila Molkova 00:03:26 Stop.
the whole project pavilion.
Ted Young (Raintank, Inc. – Grafana Labs) 00:03:29 Yeah.
And… I think Splunk is bankrolling a graduation party.
I don't have, like.
Jason Plumb (Splunk Inc.) 00:03:39 We are. Yeah, we are.
Liudmila Molkova 00:03:42 Nice.
Who's invited? How to get on the list.
Jason Plumb (Splunk Inc.) 00:03:46 I can put the link in the chat.
Ted Young (Raintank, Inc. – Grafana Labs) 00:03:48 Yeah.
Jason Plumb (Splunk Inc.) 00:03:49 Yeah, let me go find it, it's gonna take me a minute, because I'm not awake yet.
Liudmila Molkova 00:03:53 You have the whole hour.
Awesome.
So, I think we…
Michele Mancioppi (Dash0 Inc.) 00:04:02 Put it in the notes as well, please.
Liudmila Molkova 00:04:07 We have quite a few people now. Welcome to the spec call. Trask. You are the first one.
Trask Stalnaker (Microsoft Corporation) 00:04:17 Yeah, thanks. So… The first is to, kind of socialize this idea, see what folks think. I, in the declarative configuration, I like the included-excluded, pattern that is being used, in a few places now.
And I am interested in extending that to the request headers and response headers.
Since that's a similar selection, mechanism, you can see some, we've been extending that in Java, as well, to cover anywhere where you're selecting metrics, or, MDC attributes, or, yeah, other things. I did, Shortly hesitate on this, because there's some language in the semantic conventions.
About requiring an explicit, list for our users, but I did… I… asked in the semantic convention SIG yesterday, and, that… Is, the intention there is not to exclude… not to, prevent wildcards, but just to prevent capturing them by default. So it's, explicit, like, opt-in that users have to do.
So, anyway, wanted to… first, if there's any concern about allowing users to use wildcards, I guess is… Probably the only… Contentious part of this.
The other part is, I guess, you know, it's… it is a breaking change to a development feature.
Michele Mancioppi (Dash0 Inc.) 00:06:32 And, when you talk about wildcards, we're talking about the globe syntax, not capture groups and regexes, right?
Trask Stalnaker (Microsoft Corporation) 00:06:40 Correct.
Yeah, and I think it's the same pattern that's used for resource filtering and declarative config, and a couple other things.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:06:54 Yeah, this is… I support this. The more things that we can solve with this include-exclude pattern, the more, familiar it will become, and it'll… it'll reduce the cognitive load for people authoring this. They see the same sort of design cues, in various places. And it's a… it's a really simple concept, and it's very expressive. You can express simple things easily, you can… but you can… it supports the ability to express complex things, so I think it, It's… it's a good pattern.
Trask Stalnaker (Microsoft Corporation) 00:07:35 Awesome. That's all I wanted to share for that one. For the next one, sue… Maybe you can pull up the relate to Liudmila So we were thinking about duration histogram bucket.
buckets, or histogram buckets, in general in semantic conventions. We were thinking about it from the GenAI perspective, but the… this has been a kind of broader question that's come up multiple times when authoring semantic conventions, like, where… what do we pick for buckets? How do we make that choice? It's… There's never, like, a perfect choice, for everybody.
And so it helps us to have some guidance.
So… This is the proposed guidance that, I think I really like this, specifically for duration histograms.
It's a, like, a decimal-friendly approximation of an exponential.
Progression, so… Everything is, like, either, 2.5 or 2 multiplier of 2, or multiplier of 2.5, The… so you get your, Decimal friendly, and then at, At larger values, it snaps to minutes.
and ours.
So… we get, 30, 60, you kind of get, like, I mean, and obviously you don't have to, like, for some histograms, we intentionally only go up to 10 seconds, because that's… kind of the normal range of things, but in some cases, like in Gen AI workflows, you know, we need… we want much larger values, so this would kind of be… Guidance for that.
One… Decision that I made here that's, Was whether to go, 125 or 1 2.55.
if you look at the minutes, they go, 125, so 60, 120, 300.
I do kind of like the 125, but the reason I… on the… ver… the values from 1 to 10, I went with 1, 2.55.
Is because that aligns with our existing HTTP histogram, where we do 1, 2.557.5.
So it's basically the same as… the HTTP histogram today, just dropping the 7.5 value.
So, I feel like it's both a good… It's friendly, and it aligns well with our existing histograms.
So that's… top piece one. Piece two is, if we can go back to the database PR. So with this guidance, today, the database The database histogram buckets are… 1, 5, 10, 50, 100. We… so we skipped the 2.5.
And I'm suggesting here to add in the 2.5, To basically align with that.
Yeah, thank you, that's a good view.
And the question is, is this a backwards compatible change, given that database… Semantic conventions are stable.
And asked in the… Symantec Convention SIG yesterday, and, the… The thought is that it is backwards compatible, like, that that's an evolution that we need to, allow.
But I wanted to bring it to a broader group here, because I know that, you know, the… We haven't… I don't think we've… We haven't said that anywhere that it's not allowed.
But we haven't really… Address this question.
Head-on before.
Until now.
Josh Suereth (Google LLC) 00:12:31 We have addressed it head-on. Do you mean, like, whether or not it's safe to change the boundaries of histograms?
Trask Stalnaker (Microsoft Corporation) 00:12:37 Yeah, I mean, we haven't… we haven't done that in any stable conventions yet. We haven't changed them.
Josh Suereth (Google LLC) 00:12:45 Oh, we… you mean we haven't… we haven't physically done it, but, like, this was a decision we made.
And we… when we… we purposely made the data model so you can change those. Like, that's… that is in the specification.
That's, like, a decision we made in the metrics org, so it's on its way down, and…
Trask Stalnaker (Microsoft Corporation) 00:13:01 I couldn't find that, then.
Josh Suereth (Google LLC) 00:13:05 I'll find it for you, because I remember… I remember driving that, so if you think it's not, it should be written down, but I don't want to re-litigate that, and I don't really think it should change it, but yeah.
Trask Stalnaker (Microsoft Corporation) 00:13:17 Okay.
Yeah, yeah, then that's probably the only… thing was that I… I couldn't find… That ain' well.
Josh Suereth (Google LLC) 00:13:25 I'll find a link and put it in chat.
Trask Stalnaker (Microsoft Corporation) 00:13:27 Okay, awesome. Then, I mean, that will… Definitely settle that question, then.
Prashant 00:13:42 Hey, I, I do have a question, like, related to this one, but not exactly, for this. So… for durations, why… why did OTEL decide to default to explicit bucket instead of the, like, base to exponential, which is an opt-in?
Doesn't even know in this group.
Trask Stalnaker (Microsoft Corporation) 00:14:04 I think the main reason is that we didn't have exponential… one reason, at least, is exponential histograms were not stable.
For a while, and so that wasn't an option, and so changing that now is a breaking… would be a breaking change.
Prashant 00:14:20 I see. Okay. Makes sense, because now, like, we were… at AWS, we were working on the back end, so traditionally, CloudWatch has allowed… like, it's only exponential, but with now.
with this new OTLP backend, it's sort of a challenge to, kind of.
A line in a common bucket.
Okay, good to know.
Liudmila Molkova 00:14:49 And Josh?
Trask Stalnaker (Microsoft Corporation) 00:14:49 Josh.
Josh Suereth (Google LLC) 00:14:56 Sorry, too many windows to mute and unmute. Yeah, I… I thought we also decided that it should not be breaking to move from Fixed size to exponential.
Did we change our minds on that, too?
Tyler Yahn (Splunk) 00:15:14 I, I don't think it was, decided that it's… allowed that you can make that move. It's more that we stopped requiring it being the default, and that new SIGs Can choose to use the exponential histogram as their default, if they wanted to.
Trask Stalnaker (Microsoft Corporation) 00:15:30 Oh, really?
Tyler Yahn (Splunk) 00:15:33 That's my memory of the… Yeah.
Liudmila Molkova 00:15:38 Does it mean that, let's say, Java Distro V3 can move, because it's essentially the default configuration?
Tyler Yahn (Splunk) 00:15:48 Yeah, I'd want to verify with the specification, but that's my understanding, correct? Yeah.
Josh Suereth (Google LLC) 00:15:55 Right, I thought that we had literally specified histograms in a way that, like, you should be using, the histogram function calls in Prometheus, for example, and the buckets need the ability to change. Like, literally, we have a broken metric system.
if users cannot change buckets on their own as well, because you need the buckets to move to adapt to, like, the statistical variance and stuff of what you're seeing in production. So if you cannot change buckets without breaking stability.
The whole ecosystem's broken, honestly.
So, like.
Trask Stalnaker (Microsoft Corporation) 00:16:28 I mean, that's Disagree with that last piece of, like, users changing… I mean, users can change all kinds of things, and that doesn't… impact that's not related to backwards compatibility. I mean, like, you could say somebody who has a, you know, who has a chart, right, of their… shows their… database duration, durations as a histogram, right, as a chart of their actual buckets, they're gonna see something different if we change that. Now, whether that's something that is… fine. I mean, I agree that's fine in that case, like, our… Use case is, you know, alerting on certain thresholds, for example.
Josh Suereth (Google LLC) 00:17:20 the thing that should change is just the, accuracy, right? It shouldn't… I agree with you that if we change where the errors are, that is, like, a user-visible thing, but we need to, like, two things should be true. We should have a good default for histograms, we should have the ability to modify that default.
And users should not depend on any specific bucket, particularly because we actually want users to be able to move them around to improve the accuracy of your observability, right?
Reiley Yang (Microsoft Corporation) 00:17:52 I agree. You can either let the user pick the explicit way of doing things. Or, if they already got used to one existing thing, then changing any bucket strategy might be a surprise for many users. Like, for example, if I'm… I'm using OpenTelemTree today, I got this by default, like, 12 or, like, 15 buckets.
what we got the idea from premises. If all of a sudden we change this to exponential, I think the default is, like, more than 100 buckets.
then someone got to pay for the memory. If the user is not prepared for that, something is going to explode.
So I definitely think changing… changing the bucket, like, strategy to exponential will be a surprise for many users. I'm not prepared, but I'm all for, like, I think that's the right way. We should communicate and do that explicitly. If it requires a major version bump, let's go and do it. But don't do it silently behind the scene.
Trask Stalnaker (Microsoft Corporation) 00:18:51 Which I think is the, like, it sounds like the moving to exponential as the default, and I'll do some… I'll dig that up, later, because that… if new SIGs can use that, then that is a good motivation for, like, major version bumps, being able to… Actually, but that's, SDK, like, so Ludmila, we couldn't do that in the Java instrumentation, because there's no, like, advice.
For exponential… to set exponential, it's an SDK configuration? Oh, we could do it in the agent, yeah. We couldn't do it in the, we can't influence that in the instrumentation itself, though.
And just as a, like, extreme example, Josh, I mean, if we… say if we took away all the… we suddenly said, okay, there's only one bucket, like, okay, like.
That… That's gonna be… annoying to users, for example. And that's where, with the database histogram, like, intentionally we're only adding new boundaries, so I feel like, for sure, that shouldn't affect anything, or not for sure, but, like, in very high… Much less cases, because… You literally can… you're not losing any accuracy.
You're only gaining…
Josh Suereth (Google LLC) 00:20:18 Right, but again, like, you're gonna change the memory footprint, right?
Trask Stalnaker (Microsoft Corporation) 00:20:22 Yeah, yeah.
Josh Suereth (Google LLC) 00:20:23 Is that… is that… that's where we have to make lines of what we consider stability and what we consider instability, and where that is. And I think for histograms, we should be willing to make reasonable changes to bucket defaults, is kind of my position.
And my very, very strict position is we should be able to do whatever the hell we want with buckets.
By policy, but in practice, we're going to be reasonable, because a breaking change is just, does the user notice and complain?
That's the real definition of a breaking change, right?
But we need a line somewhere, and the line is, any bucket change should be allowed.
And I think you're using good judgment here, you have a really good use case, but I don't think we should be afraid of, like, making these changes generally. That's all… that's my main point. And one thing I think might not be clear to people who are coming into Metrics is, like, the importance of being able to move your buckets around.
Trask Stalnaker (Microsoft Corporation) 00:21:20 Cool.
Josh Suereth (Google LLC) 00:21:21 from… yeah, go ahead.
Trask Stalnaker (Microsoft Corporation) 00:21:23 I was just gonna, seed time here. I think we have good follow-ups. Josh, if you can find where it's documented today?
And I will check in to what Tyler was saying about Potentially, because possibly in… we do have the Java 3 release coming up, and, that would be something for us to consider if we can switch to exponential by default.
Thanks.
Liudmila Molkova 00:21:51 Wonderful. Thank you all, great discussion.
Prashant? Is it how I pronounce your name?
Prashant 00:21:57 Yes.
Liudmila Molkova 00:21:59 Welcome. Do you want to present? Do you want me to present?
Prashant 00:22:03 I can just quickly talk through, so you can, yeah, you can present. Basically, so, the motivation for this OTEP is… So I was working on something, like, related to span-derived metrics, and was… relying heavily on the span metrics connector in the OpenTelemetry collector, and what I realized is that… I think it was ported from a processor, and there was never really a formal spec on those metrics.
And, like, one of the things I found discrepancy was the explicit buckets did not follow the semantic convention.
So, I thought… And I think more and more generators are coming up with span-derived metrics, so probably a good idea to have a formal spec for it.
So, yeah, I mean, is this group the best spot, to present it, looking for, like, some… folks to endorse or review and guide me in this OTEP. It… it has turned out to be a big, bulky OTEP, so… Do you guys think it should be split? Or if the community… you guys can help?
Absorb… like, review and absorb this as a one… Big OTEP.
Like, I can talk about it if the specifics of it, some of the things, A lot of things are actually breaking changes.
Actually.
Liudmila Molkova 00:23:46 Thanks for bringing it up. I think there are two things. If it's just a matter of defining semantic conventions.
I'm not sure we would need an ATAP. It's good to know.
For the community that this exists, but… Not necessarily to have OTAP. I think there are a lot of design questions that you might get, and one of them has always been, should it be one metric, or should we convert this? Each spend type becomes its own metric.
Prashant 00:24:21 I see, okay. In my proposal, I'm saying, it's, like, just one metric, because it's… basically, my idea is that today, the span metric connector, generates, like, red metrics, the red error duration, and everything… all three of those can be derived from just one.
So that's what I'm basing this OTIP on, but if there are… Like, More reasons to go with… Metrics for each, span type.
10…
Liudmila Molkova 00:25:00 Yeah.
Prashant 00:25:01 Not sure, but they already exist, right? Like, we already have HTTP server durations and those, which some of the libraries automatically emit.
Liudmila Molkova 00:25:15 So yeah, I think the goal for this fan matrix, at least from what I know, and people can help me here, that not all the backends, supported metrics at some point, or not all instrumentations in OpenTelemetry, a lot of them don't support metrics.
And the user application sometimes only midspans And this is a nice thing that allows to, like.
Create some parity between different producers of telemetry.
And also, to not know about all the different variations, because you can have that many server metrics, right? Exactly, yeah. So there are good reasons for this to exist, maybe they should be server and client.
But I'm curious if, like, in the long run, we don't… like, why do we calculate metrics from spans at all?
Could we use metrics for this directly?
Prashant 00:26:19 That's a good point. I mean, some of the… like, applications I've seen, they only emit, like, traces, and that too, like.
doing this in Collector, kind of, to me, in my mind, makes… More sense, but then the major drawback is that they're all, like, the spans are already sampled.
Liudmila Molkova 00:26:44 Yeah.
Prashant 00:26:46 So there are good reasons. Like, even some of the backends that can, generate this, they only receive spans.
Liudmila Molkova 00:26:57 Yeah, Jack?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:26:59 So I'm not necessarily advocating for the expansion of spandon metrics. I'm with you, Liudmila, that, you know, if we can emit metrics directly at the source, we should. Just on the point of where this should live, specification or semantic conventions, or somewhere else.
One thing that I could maybe tip it into… tip the scales towards a home in the specification, maybe in addition to semantic conventions.
is if there was a proposed built-in processor for the Trace SDK that did spandimetrics, then the specification for this processor could, you know, live in the Trace SDK document and reference semantic conventions for this.
I just have a hard time, with the idea of including specs for collector concepts that live in exactly one place.
Prashant 00:27:54 Zoom… I think what I envision is that, like, I myself have built my own processor in the SDK to do exactly this.
to get metrics from all the spans, whether sampled or not, without exporting all the spans to the collector. So that's exactly the design I went with, and I… believe that, that's exactly what the SDK implementations would be, like some spandom metric processor.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:28:33 Yeah, I mean, well, that makes sense to me, from a, like, you know, from a conceptual standpoint, that there would be… that, you know.
there's this idea of an SDK spAN processor, which does spandimetrics, and how it exactly calculates those is specified such that the collector and the SDK implementations can all be aligned and doing the same thing.
I don't necessarily think it's a great idea. I think, you know, the problems that you talked about, like.
Some backends don't support metrics, well, fix that. Some SDK… some applications only emit traces, well, fix that. So that's kind of where I stand on that, but, like, in terms of, like, concepts, you know.
It seems reasonable to me. And, you know, I think it would just be a matter of getting community consensus on it, that, you know, people want to spend our coins adding this concept across all the languages, because that's not free.
Liudmila Molkova 00:29:43 Robert?
Robert Pająk (Splunk Inc.) 00:29:45 Have you checked how is it different for self-observability metrics for the Trace SDK? Like, I have not checked, but at first glance, it looks like almost identical.
Prashant 00:29:58 The self-observability metrics… no, I haven't checked.
Robert Pająk (Splunk Inc.) 00:30:03 Yeah, I'll double check, because I have a feeling that it's almost identical, just without auto spending, auto-spun type, but maybe I'm wrong.
Liudmila Molkova 00:30:11 Robert, the self-observability would not contain the duration of spends themselves.
Robert Pająk (Splunk Inc.) 00:30:17 Okay.
Liudmila Molkova 00:30:18 Were they statuses?
Robert Pająk (Splunk Inc.) 00:30:21 Okay.
Liudmila Molkova 00:30:24 Okay, so in terms of the next steps, the question is, if it's only the collector, if it stays within the collector, then the collector would own this semantic convention definition. If we want to expand it beyond the collector.
then I think it should still be described in semantic conventions, just because of all the tooling and checks we have there.
And generation and the spec could link to it.
And, I don't know how other semantic conventions Maintain or feel. I think it makes sense to document it in semantic conventions?
And… but I don't see the reason for it to be an auto tap.
Prashant 00:31:09 Okay, so I can, like, directly open probably an issue in the semantic convention repo and start there?
Liudmila Molkova 00:31:17 Yeah, maybe there could be an existing one, like, lookthrough, okay.
I'm looking at other people here, would anybody have an objection from And would need it to be an RTEP.
Okay, I hear silence.
Prashant 00:31:44 Okay, I'll take a look at that.
Thank you.
Liudmila Molkova 00:31:53 Thank you.
Okay, Robert, you are going to merge this.
Robert Pająk (Splunk Inc.) 00:32:01 Yeah, it's just a… advertisement.
And we can go further.
Liudmila Molkova 00:32:08 Awesome.
Yeah, it's dolphin.
Robert Pająk (Splunk Inc.) 00:32:15 This one…
Liudmila Molkova 00:32:17 Go ahead.
Robert Pająk (Splunk Inc.) 00:32:19 This one was, done by Tigran. Tigran doesn't, doesn't have time recently, and he asked me to follow up with this, so I tried to address all the comments and also reviewed it, also made some changes here.
looks, like, very close to being shipped, so this is the only… I think only traces do not have any document around data model, so I'm asking here to take a look. It already has a few approvals, but I think It's okay just to wait one more week.
For double checking, and for more reviews.
Liudmila Molkova 00:33:03 Do you want to merge by the end of the week?
Or… next week, probably.
Robert Pająk (Splunk Inc.) 00:33:09 Maybe even in two weeks, because KubeCon is next week, there's no rush. It doesn't… also, there are no collisions and conflicts, because it's a new document, so there's no rush.
So, with this one, it's just a small PR, but I thought that maybe it's just worth discussing, so… it's just adding, I think, like, 2 weeks ago, or something like that, I… we added this kind of exceptions for making, without making major… to change default con… to change default configs and some behavioral stuff.
It's also as a possibility that if you have a vulnerability, because of some, I don't know, some runtime dependency, or some other dependency, or instrumentation library, or automatic instrumentation, you are also allowed to Bump these, these dependencies without having a major bump.
In .NET, we are… auto-instrumentation, we are using this for years, and yeah, just take a look, and you have any concerns with the phrasing, or with the concept, feel free to comment here. It already has a few approvals, though.
Liudmila Molkova 00:34:29 Okay.
Robert Pająk (Splunk Inc.) 00:34:33 And the last one, hopefully, or not the last one? Yeah, Yeah, and the distinguishability liability is… yeah.
So, this one is trying to have a more granular definition, or distinguishing, like, distinguishing something which is a clear availability vulnerability, for instance.
some kind of asymmetric attack that you make, for instance, one request, and it, it makes, like, null pointer exception, or something which blows totally your memory, the memory leak.
For other, like, kind of availability attacks that you're simply DOSing, and which causes your infrastructure just to run out of sockets, or things like that, which should be, like, mitigated not on collector level, but some other level.
And this is just having a language to… especially for the collector folks.
to kind of faster assess the reports that they are having. So, the idea is having this kind of language here.
And this kind of description will hopefully, one, hopefully reduce the reports that they get. Secondly, it will be easier and faster using AI or anything to just get to make a quick review of these reports, just to close them if they are invalid according to this assessment.
Liudmila Molkova 00:36:00 So it does not affect the posture score, it's just the terminology.
Robert Pająk (Splunk Inc.) 00:36:08 Could you re- could you repeat?
Liudmila Molkova 00:36:12 So it's your same… Go ahead.
Robert Pająk (Splunk Inc.) 00:36:15 So, right now, there are some, like, existing language, which says that availability when there's authentication, etc, do not count, and we are still keeping this language.
right now, because we are, in parallel, trying to make a separate thread model for Collector and other languages, so to, to make kind of this, to harden or just improve the security posture, but this one, this PR, is just trying to have a clear understanding, have a distinction that our security model says that if you're just, you know, trying to make, you know, those Sufire requests.
And it's just linearly, you know, trying… exhausting your machine. It's not a vulnerability. It's just, you know, someone is just, you know, knocking through your door, and your door is just being broken, because everybody knows.
Liudmila Molkova 00:37:09 Yeah, Trask?
Trask Stalnaker (Microsoft Corporation) 00:37:11 Yeah, you mostly answered my question, Robert, but it was about, the collector, and I know they had put in, you know, the language that, availability wasn't a security… Issue.
And so, I just wanted to make sure you're working with them, and that we get, enough representation from them, so they don't feel that we're just, like.
Stomping over there.
So, I try to…
Robert Pająk (Splunk Inc.) 00:37:43 I try to be in the loop with the collector maintainers here, and I'm also, in parallel, I try to help them reviewing and writing a threat model for the collector.
Trask Stalnaker (Microsoft Corporation) 00:37:55 Okay, great.
Thanks.
Robert Pająk (Splunk Inc.) 00:37:57 Thank you, Trask, for calling it out.
Liudmila Molkova 00:38:06 Okay, wonderful.
Robert, the next topic is also yours.
Robert Pająk (Splunk Inc.) 00:38:13 It's mine only because I added to the agenda, so there is one very nice article, created by, Lise.
And it has, like, 3 approvals. I would say that it's a very high-quality audit, and I'm just asking others to review this.
Because I think it should… yeah, I verified this one.
suggest this proposal is to add, you know, ZSDD as an additional compression codec, and it's very well detailed and describes what are… how it should be handled, you know, what we should do when it's not… when it's not supported, like, how other languages, and yeah, it's very detailed, and in a good way, that it's not over-specified, but it also answers a lot of Kind of important questions.
Liudmila Molkova 00:39:09 Okay, it seems we need one more approval here, and then we will be good to merge it.
Robert Pająk (Splunk Inc.) 00:39:21 no questions, I think we can go to Davies, probably, topics right now.
Liudmila Molkova 00:39:27 Yeah, David. Wow, that's a lot of OTABs for one call.
David Ashpole (Google LLC) 00:39:31 I'm… I'm sorry, I committed the cardinal sin of open source and opened two OTEPs. Yeah, let's talk about the first one.
So, yeah, I was inspired by some of the recent conversations, about config, and and APIs and stuff, and… I… this is… this is me taking a stab at Trying to introduce some APIs to actually try and solve the stable by default problem. So, take this… take this as a proposal, but I'm… I'm pretty happy with how it turned out. So the… Right, everybody knows, like, we've got, like, 800 instrumentation libraries, and, like, 6 of them are stable.
And I'm sure we all have our different… our own, assessment of why that is.
But my take is that the contract right now for stabilizing an instrumentation library is pretty rough.
Right, so… You are supposed to be 100% stable.
But all of the semantic conventions usually have, like, a mixture of stable stuff and some development stuff in them. And so you end up needing to add a bunch of feature gates.
To be able to turn all the unstable parts off, and keep them up to date, and that's a lot of work.
And so, a lot of things just sit in, you know, V0.whatever. And I think with TED's original OTEP, I think the idea was good of trying to decouple telemetry stability from… The stability of the library itself.
But I think… I think we're missing a mechanism there, right? Because in an ideal world, you would be able to stabilize a library.
But somehow note that pieces of it were still unstable in a way that, kind of conforms to some standard, right? So… The idea basically is that an instrumentation library should be able to pass You know, development equals true, or stability level equals development, or something.
on… Metric instruments, on log records, on spans that it starts.
And the contract for the instrumentation library, when they do that, is that those pieces of telemetry are allowed to change in breaking ways, outside of major versions, right? So, those are unstable.
So, I think that that contract… Can allow instrumentation libraries to stabilize.
With whatever telemetry they have, whose conventions are stable, and leave the rest of them Kind of, with these experimental tags on them.
And then… The second… the flip side is… so this… what this does is it basically just takes a problem, which today is a problem for instrumentation authors.
And makes it an SDK problem, right? So now the SDK has all these… Experimental tags, and we have to decide what our policy is.
For how to handle experimental telemetry, and what knobs we want to give users for turning it on and off.
And so I've proposed what I think is kind of the minimum set of configuration knobs in the SDK to make this work, and, to be able to match what existing feature gating behavior exists in instrumentation libraries today.
And… Actually, all that I think we need is… Either, like, true, false.
Enables unstable telemetry flag on tracer provider, meter provider, logger provider.
Sorry, I have a cold.
Or, some, like, similar to log severity, like a minimum stability level, if we want to make the stability levels extensible in the future.
But… And then… the final piece of the puzzle, obviously, is, like, the SDK should disable experimental telemetry by default.
So meaning it essentially sets the minimum stability level to stable by default.
And then users have the ability to turn on experimental telemetry using Using this configuration option. And I think… We can always add more granular knobs in the future as well, so this is meant to be a starting point, not the final… all of the knobs that we expect to have on the SDK.
So… Yeah, that's it. I'm happy to take questions, if anyone has any, or Yeah, I'd appreciate reviews.
Liudmila Molkova 00:44:20 I really like the idea. I keep thinking about this. So… If you vent all the way down.
To the point that you have stability spec… specified for your metric.
Then maybe you also bothered, to define conventions for it, and the schema.
And you may be even bothered to provide schema URL to your meter or tracer.
And now, if it's documented, and if you have done to all this extent, Then, this… Knowledge that this is still in development is part of your semantic convention schema that you could know, like, the SDK could know in runtime that it's development.
So… I think… yeah.
David Ashpole (Google LLC) 00:45:16 I think as long as the SDK turns it off by default.
I think the goal of the proposal would be met. So, whether that's explicitly passing the stability and letting the SDK be kind of, like, dumb and say, oh, they passed stability development, so I'll turn it off by default, or whether the SDK is going to know about all the semantic conventions, that it needs to handle and do those lookups, I think either way would… would be fine.
Liudmila Molkova 00:45:46 Yeah, I think either… would work. I'm just thinking that we either put every knob we want in the API, Where we, create this implicit connection between semantic convention and SDK, and we require everything that's not stable, that provides schema to also provide the contents of the schema.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:46:15 I think we are starting to create a connection between semantic inventions and the APIs. Span type is an idea, is an example. The language you've introduced for that, Ludmila, explicitly mentions semantic invention span types.
So we're kind of getting into that territory of having semantic convention-oriented APIs.
Liudmila Molkova 00:46:39 Well, they've always been, right? This is semantic convention-oriented API for metrics.
David Ashpole (Google LLC) 00:46:45 Yes, yeah.
Right, like, we could not pass the unit, I guess, and just look it up, you know?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:46:50 The thing about the other APIs, though, and why metric name is a little bit different, is, like, you're not… you're not, like, mandated to, you know, have the thing defined in semantic conventions. Like, nothing breaks if you don't follow semantic conventions.delimited, format.
Liudmila Molkova 00:47:11 Yes, and same with event name, or spend type, or attributes, or anything, yeah.
So this is the… Like, all the extra things are for things that are not Part of semantic conventions, and that cannot be discovered in runtime.
The other small piece of feedback I had, I'm curious what, David, you thought about this. There is… the attributes are also kind of mixture between stable and development, and it's like the evolution pass, right? You add a development attribute to your span, and it's opted in, but eventually it can become stable, and then you would populate it by default.
We don't want to add similar things to attributes, do we?
David Ashpole (Google LLC) 00:48:07 Well, so I thought this was going to be a problem, and I actually had written a design for how I was gonna solve it.
And then, it turns out, and I'm sure you know this better than me, but, there's a clause in the semantic conventions that requires that experimental… attributes?
Unstable telemetry has to be opt-in.
And so, in a sense, we're… We're, like, encoding stable by default in the way we're allowed to define conventions.
And so I… I do think it's… not necessary.
To, have that be part of the API.
My… Just for kicks. My original idea was that we could actually have A list of stable or unstable attributes be provided to the logger, meter, tracer on creation?
But the performance of doing that filtering is actually pretty bad.
So… I'd rather not… not have to do that if we don't have to, but I think we're, like, we're safe today. The attributes, because of our policies around that, are already essentially stable by default. So I'm really looking to solve the metric… Span and log level stable by default problem.
Trask.
Trask Stalnaker (Microsoft Corporation) 00:49:37 Yeah, that's interesting, because, interests me because, I would say most of… in the Java instrumentations, most of the experimental stuff we have are experimental attributes.
They're not necessarily semantic convention-defined attributes, they're things that miscellaneous library Attributes that people have found useful, and so… but we don't want those to be on by default.
And so… we hide them behind experimental flags. So I was… when I was reading Eurotip, I was assuming that we would… Use the same stability flag.
To… for users to opt in to those experimental attributes.
And I was just assuming we would call the tracer isEnabled stability level, you know, we already have conditions around emitting those experimental attributes, and we would just call that isEnabled Don't necessarily require a separate API.
David Ashpole (Google LLC) 00:50:52 Sorry, help me understand how… how would the SDK know if an attribute was experimental or not, or does it not need to know?
Trask Stalnaker (Microsoft Corporation) 00:51:00 So I would… we would call… The SDK wouldn't know, but we would call isEnabled… On the Tracer, I guess?
And we would pass in is enabled stability level development.
David Ashpole (Google LLC) 00:51:20 The… so the instrumentation… would ask the SDK If something was enabled or not before it emits the attribute.
Trask Stalnaker (Microsoft Corporation) 00:51:29 Yeah.
David Ashpole (Google LLC) 00:51:30 Okay.
Trask Stalnaker (Microsoft Corporation) 00:51:31 Did I miss that? I thought that there was a… is enabled on the tracer.
in your… OTEP that we could draw.
David Ashpole (Google LLC) 00:51:39 Did I leave that in?
Liudmila Molkova 00:51:43 I mean, it has to, even for your design, David, like, instrumentation needs to know if to populate the development attributes, it needs to get this property, or something like this.
Trask Stalnaker (Microsoft Corporation) 00:51:56 Well, I think what David is saying, as a… separately, we could decide that… we could say, oh, those are all opt-in, and everybody has to create another flag in order to opt-in to the experimental attributes.
I think that's what you were suggesting, David.
David Ashpole (Google LLC) 00:52:17 we… So I think that there's two… I think… I think it's covered in the alternatives, but I can double check. I think what I found was that All the experimental attributes were on metrics?
Is that right? That doesn't sound right.
Liudmila Molkova 00:52:33 No, they are everywhere.
The,
Trask Stalnaker (Microsoft Corporation) 00:52:40 Paul Upton.
David Ashpole (Google LLC) 00:52:42 I think it's a good, good piece of feedback.
Trask Stalnaker (Microsoft Corporation) 00:52:45 Yeah, also think about the, Things that aren't in semantic conventions, but that libraries… I mean, you could look at the Java instrumentation repo, we've got experimental span attributes.
As a flag on lots of instrumentations to opt into, sort of, these, like, library-specific things, because Even though I guess we could make them stable, we've taken the stance that we only want to emit semantic convention attributes by default, and all the other, like, library-specific are…
David Ashpole (Google LLC) 00:53:21 I… I think, in a sense, then, we could actually simplify this, because if you can take a tracer and ask it if experimental stuff is enabled.
then you don't need an API on instrument or on span or anything, right?
So… I'll look into reworking it that way, and I'll make sure that attribute stability is something that we can support.
Cool.
Trask Stalnaker (Microsoft Corporation) 00:53:50 Cool, thanks for driving this, yeah.
David Ashpole (Google LLC) 00:53:52 Yep.
Liudmila Molkova 00:53:54 And the next one is also yours, David, and we have 8 minutes, so maybe I will turn it into just FYI.
David Ashpole (Google LLC) 00:54:01 Yeah, I will turn it into an FYI, since you're right after me.
Much less exciting than stable by default for instruments, but, There's been a few prior attempts at defining an authentication interface.
This is my attempt. The main difference, compared to some of the prior attempts, is that I'm trying to define less.
So… It basically leaves a lot of the implementation details up to languages, but does have some requirements around, like, cancellation and other things.
I… Yeah, and it doesn't… I know that there is a hang-up with previous proposals around a, a protocol that requires you to sign the whole payload, and so that's explicitly not a requirement of this, because I think that was incompatible with some of the language implementations for auth plugins. But, much less important than the stable by default one, but I would appreciate reviews if there are people who are interested.
Thanks.
Liudmila Molkova 00:55:13 Nice. Thank you.
Okay, the next topic is mine. Thank you, David, for yours. I'd like to get, to talk about span type. There is a discussion, we can take it offline about, normative things around span type.
requirements. But other than that, it seems we have a good list of approvals.
And, once the discussion settle down, I'd like to merge it.
So, please review if you haven't.
Or let me know if you have any objections.
Moving on… We should probably cancel next week because of the KubeCon, or if you folks have a good quorum, then go ahead, but you can also enjoy a quiet week if you're not going.
Okay, so I consider it as yes.
And then Dmitrii. NTTID school proposal.
Dmitrii Anoshin (Splunk Inc.) 00:56:30 Hi, everyone. Thanks for, giving the time. 5 minutes should be enough for sure. We have this problem in entities, Data model and entities seek that we have a, like, a set of identifying attributes that identify an entity, but it's unclear whether those identifying attributes are, like, globally unique, or they only, identifiable within particular scope. So this proposal, address that issue… addresses that issue. We suggested that we have two additional fields on the entity reference data model in… on the… on the proto that would specify identity scope, being in Arm, whether it's unspecified. This is, like, the current behavior. If it's unspecified, it's unknown which scope of the ID it is.
Whether it's global or local. And if it's local, it's required to… required to specify another field that would tell which entity type this particular entity is unique within. So, for example, if we have a Kubernetes container like, set from… by the computer spec, it would only have the names. It's a… it's a spec, it's not running container. And that… that entity, computer container, would be, given that it has a name, it will be only unique within its spot.
So, it has to have this additional field on the entity reference, saying, ktz.pot would be the scope of this entity. That's the simplest example of local identity.
And, this… PR, has all of the other details related to that.
So I think that's pretty much the whole idea. We can maybe spend some time to just discuss it if you have any questions. Otherwise, feel free to take a look offline.
Liudmila Molkova 00:58:45 So this essentially introduces relationships between.
Dmitrii Anoshin (Splunk Inc.) 00:58:48 That's a good point, it's not relationships. Relationships are supposed to be sent as a part of the side channel for entity events, where you have any kind of relationships.
But this one can relate to the parent relations… relation, and it also may not. So, it's like… Kind of related concept, but it's not one-to-one mapping for the parent relations.
Relationships can be also different. It can be ease a parent and everything, so…
Liudmila Molkova 00:59:23 Yeah.
Go ahead, Josh.
Josh Suereth (Google LLC) 00:59:25 Something in that the scope doesn't have to be the first jump.
2.
Right? So, like, it, like, the name, container name to pod, right? Cool.
It also could be, like, you have a host ID that's unique within a availability zone, right? That's an example of something you could do, where there might be layers between you and availability zone.
But you can skip straight to that with this contextual thing. The idea is we want to make sure that we can get a global identity to every single entity over time.
And there are… like, you can talk to the host, semantic convention group about how hard it is to just get a globally unique ID for hosts generally. So this is kind of an out, where if we can't get something globally unique, we give the best identity we can.
and market as local with, like, okay, we know who we are within some space, but if you need to get a globally unique ID, you have to combine us with other pieces of data.
Liudmila Molkova 01:00:28 I imagine the goal of it, and having it directly in the entities, is to build this globally unique ID for something.
Josh Suereth (Google LLC) 01:00:39 Yeah, so you can do index lookups between them, and so the relationships make sense, yeah. Dmitri might be able to say more, but yeah.
Dmitrii Anoshin (Splunk Inc.) 01:00:47 Yeah, that's correct. Essentially, the goal is to have a global indicator. And I should mention that in this quantity convention, it will not be… like, each entity type might have different, scopes that can be applicable. So, for example, process can be unique within a host, but also if it's part of a container, for example, it can be a container. Or, if we're talking about host, host might be global.
If it's, if we are, like, getting data from UID for that, or it can be local within availability zone. So, we… we send data on the wire, which is exactly tell you what's the… identity scope, but in semantic conventions, we provide, like, possible options for a particular entity type.
Liudmila Molkova 01:01:43 Awesome. Thank you. We are at time. Appreciate y'all coming, and thanks a lot.
See you in two weeks. Thanks, or next week.
Carlos Alberto Cortez (Dash0) 01:01:52 into chaot.
