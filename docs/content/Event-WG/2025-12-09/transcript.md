SIG: Event WG
Date: 2025-12-09
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/QkG9dlekkYJXzvpiH6uNqH3RMp9S22BE4oRXBA4O9bFoY9A5IaoBH8NpVgyVPr12.PJSBZI0RiOl13Hji
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:12 Hi, Robert.
**Pellared** 00:20 Hello, hello, how are you?
**Liudmila Molkova** 00:22 I'm good, how are you?
**Pellared** 00:24 I find just… I have been just not one week or something like that, and I'm so swamped.
I haven't managed even to see the recording from the last week.
I saw just some comments in the GitHub issues, thanks for keeping, you know.
To having… having some notes there.
Mr. Chair.
**Liudmila Molkova** 00:47 Hi, Emily!
**Emily Stolfo** 00:48 Hi, it's been a while, how are you?
**Liudmila Molkova** 00:50 I'm good, how are you?
**Emily Stolfo** 00:51 Good.
**Liudmila Molkova** 00:59 I'm not sure what's the agenda today, let's see…
So, what we discussed last week?
Regarding… This one.
We are… We have all the prototypes for stabilization.
And… I think we can just go ahead and propose the change.
**Pellared** 01:46 Okay, I'll try to see my APR tomorrow.
**Liudmila Molkova** 01:52 Okay… So, let me ask if Trask is joining.
And let's get started.
**Pellared** 02:06 You can move the lock C port at the end.
**Liudmila Molkova** 02:10 Huh.
**Pellared** 02:11 I just tried to find the one.
I'll tweet.
**Trask Stalnaker** 02:32 Hey folks, sorry I'm late.
**Liudmila Molkova** 02:34 Oh.
No worries, I was just pinging you.
**Trask Stalnaker** 02:39 Pops.
**Liudmila Molkova** 02:50 This one I approved, Jack left some comments…
**Pellared** 02:59 Oh, that's new, I haven't saw it.
Say yes.
I think there were some use cases for emitting logs from some English libraries, if I remember correctly.
I can try to make an archaeological declinator. I remember there were some reasons to have a possibility to emit logs as well using the API.
**Liudmila Molkova** 03:39 We could…
probably be more explicit for the ergonomic API to say that the ergonomic API should promote structured logs, and should demote string formatting.
**Pellared** 03:53 Yeah, yeah.
But I think that, jack is asking if you are not suggesting it should be only events.
It's.
**Liudmila Molkova** 04:03 Yeah, I think…
**Pellared** 04:05 Got it.
I think I'll find later some rationale why people wanted to emit Knox, because I remember there were some things in the issues, maybe it was even… maybe it was even in the vision of events, I'm not really sure, but I remember there were a few places where people were asking for it.
A few use cases.
**Trask Stalnaker** 04:31 I mean, for sure, in the lock bridging world.
**Pellared** 04:36 But I'm not… No, not logging. I think we'.
**Trask Stalnaker** 04:39 Yeah.
**Pellared** 04:40 There was also use cases for logging libraries, when you want to add some additional… not events, but logs. I will double-check it, I will find, and then based on the use cases provided earlier, we can decide if we want to leave, delete it or not.
I just want to, you know, try to find the history.
Is that…
**Liudmila Molkova** 05:11 Joy, I think we're…
**Trask Stalnaker** 05:12 Were… were there… were there cases? That's what… I mean, I think…
**Pellared** 05:16 Yes, they…
**Trask Stalnaker** 05:17 joined Teresa. Yeah. Okay.
But we don't remember what they were.
**Liudmila Molkova** 05:40 I, I…
I kinda feel like I'd rather limit it, unless there are strong cases, they're gonna make API to only support event name.
**Pellared** 05:50 I think one of the cases.
Of the two was, reporting errors.
as locks instead of, you know… I think this was one of the cases.
Instead of using events.
the spend events.
**Liudmila Molkova** 06:06 If all… every… all… if the only thing you know that it's an error, wouldn't it be better to give it an error or exception name?
Then, no name at all.
It's an event name today exception.
**Pellared** 06:24 Okay.
**Trask Stalnaker** 06:28 Yeah, I mean, I also want to see some convincing reasons why we would want to support it without an event name.
Because…
**Pellared** 06:43 results.
**Trask Stalnaker** 06:44 the…
Event name is… so, like, when we start talking structured logging and doing anything with all of these logs, event name is going to be the first thing that you're going to want to slice by in all cases.
Even if it's some dumb, generic event name, still, like…
**Pellared** 07:06 useful to throw…
**Trask Stalnaker** 07:09 Yeah, something in there.
Maybe it's just your app name, you know, something basic.
**Liudmila Molkova** 07:21 Okay.
Okay.
Cool.
So… Back to the agenda… Emily, do you want to go ahead and talk about your topic?
**Emily Stolfo** 07:44 Sure. You're welcome.
Yeah, hi. So I've not worked on logs before. Recently, I've started contributing to the collector, specifically to add an encoder, a receiver encoder for
parsing logs from various GCP components. And coming from the tracing… traces background, where semantic interventions are
we would kind of lead with semantic inventions before we would write instrumentations, in different languages, so that there was commonality between all the instrumentations. I was wondering…
Given that
many of the providers, or at least some of them, want to eventually export logs in OTLP format.
Does it make sense to put the effort in to write semantic conventions for specific
components like load balancers that have very specific fields that are rarely identical between cloud providers.
this is a question that, like, my team is asking right now, because we're all writing parses for different cloud provider components for this overall, technology that we have called a cloud forwarder that's, I don't need to explain, but it,
We don't know if we should be leading with semantic conventions before we contribute these parsers and define log fields.
Or if… Given the…
trends, or at least the interest, or overall long-term roadmap of providers to emit logs as OTLP, if that would be wasted effort.
what do you think, from the logs SIG perspective? Would you like to see semantic conventions, or is it… doesn't make sense in this case?
**Liudmila Molkova** 09:34 From semantic conventions, we kind of try to
Limit what we put in the core conventions.
And, in the core semantic conventions repo, we're probably, like, let's say you would contribute… you would want to contribute to GCP logs. We would recommend to actually maybe host them in the collector repo, where you,
Defi- like, where you have the parsers.
Then, if there is some part that, like, if there is an intersection, let's say this log record can be emitted by the collector processor, sorry, collector receiver, or instrumentation, then we would consider,
Having them in semantic conventions, but maybe, still we would need some group of people to work on them together.
So we, okay, so are you trust getting some links?
**Trask Stalnaker** 10:36 Yeah, yeah, yeah, but that doesn't… I mean, the… there's kind of two questions, I think, from Emily. One is just defining… should they be defining semantic conventions? And the other question is where.
Would they define them?
And…
I would like to see us… I would like to have that discussion about how to define these,
Logging semantic conventions, sort of log bridge semantic conventions, log…
load balancers, NGINX, this, the second link I added there was an attempt at
You know, defining log conventions for…
You know, load balancers, web servers, like, it was a very specific one, but, there's…
I think those… that…
and even if we end up with different… like, I could almost… I could even see that there being a common…
Like, like, access logs, like your web server access logs, like…
I would like to say something about that in general, semantic conventions, even if all of the specific ones, like GCP, Azure, NGINX,
I'll end up having a lot of, kind of, extending those It feels like there's… a lot of…
similar things… That came up in that prior NGINX pull request.
Such as just basic things like reusing HTTP semantic conventions where they make sense.
**Emily Stolfo** 12:27 Yeah, I mean, that makes sense.
I feel like it would be a great undertaking to start writing semantic conventions for
various cloud provider components. So… In the interim, if we're just interested in specific things, like.
Load balancers and, yeah, I get…
Would it make sense to… so, yeah, something like a load balancer is very specific, and would it make sense to just contribute semantic conventions for that now, or is… or should we take more of a holistic approach and think about
what kind of… fields cloud providers normally have in their component logs, and contribute something like that, or…
Yeah.
**Trask Stalnaker** 13:21 I think my… my initial thought, kind of, to Lyudmila's, like, Earlier…
was getting at about semantic conventions Repo is kind of overwhelmed right now with things and trying to do, initiatives there, that…
I would probably try to just take the collector component that you're working on.
And try to write the semantic conventions for that, and host that in… the collector component.
We are trying to make the weaver tooling
support that use case better. Right now, it's quite painful to use the tooling, so I wouldn't even try to use the tooling. I would just, you know, handwrite the
Kind of… semantic conventions.
And then, you know, at least there's sort of documentation there of what semantic mentions the collector-receiver
Our scraper is using.
And then, as we sort of, and we can definitely share that.
with us, with this group, I would love to take a look and provide feedback and comments on… on it.
And sort of as we get multiple pieces together, then… and there's… then we could probably have a better chance at
pushing some of the common pieces into semantic conventions repository itself.
**Emily Stolfo** 15:13 Okay. Is there an example of this existing, or is this a quantum of a new idea? Is there a template I should work off of, or an example I should work off of, or find a new way of doing this?
**Liudmila Molkova** 15:26 I think there are some components in the collector that have, their metadata, metadata YAML, like, expressing what they are using, and they maybe even support, generating documentation from it.
Let's…
**Trask Stalnaker** 15:44 I would reach out to Antoine.
Intel.
**Emily Stolfo** 15:48 Oof.
**Trask Stalnaker** 15:49 he is a… I think he's a maintainer in Contrib… Collector Contrib, but he's been, very active in
This direction, basically trying to… document the semantic conventions.
in…
the collector contribo, and he's been testing out the Weaver tooling, and he's where we've gotten a lot of this feedback that the Weaver tooling's not great yet for that purpose.
But yeah, he could point you to…
**Emily Stolfo** 16:21 Okay, I was gonna ask his last name, is that his last name?
**Trask Stalnaker** 16:24 Yeah.
**Emily Stolfo** 16:25 Tony? Tony?
Okay, cool. I'll try that. Thank you.
**Liudmila Molkova** 16:34 It seems there is a consensus here that we would love to see the conventions. It makes total sense to define these conventions, and cloud providers may define their own, but it will take them maybe years and years, and it probably will be opt-in, and the old
The receivers you would write would still be around for decades, maybe.
**Emily Stolfo** 16:56 Okay, yeah.
Yeah, but then some… but something written down would be useful, and yeah, just to have,
Some consistency, if possible.
**Liudmila Molkova** 17:08 Yeah, so in this case, it would be more like a documentation for the receiver, rather than a central, unified convention that's shared across providers or something.
**Emily Stolfo** 17:18 Yeah, makes sense.
Cool, thank you. Thanks for that input.
**Trask Stalnaker** 17:26 Yeah, and I was looking for our log…
What do we have? SUMCOM log approvers, yes, so…
Feel free to… I'll put in chat… Ping this team.
just if you throw up a draft PR, or some… or an issue, anything like that, that, we can provide feedback on.
**Emily Stolfo** 17:59 Sounds good. Thanks.
**Liudmila Molkova** 18:04 Cool, thank you, Emily, thanks for coming.
**Trask Stalnaker** 18:08 But Mila, how are you not in… how are you not in this team?
**Liudmila Molkova** 18:13 I don't know.
Nobody edit me?
Oh, thank you.
**Trask Stalnaker** 18:22 We should probably re… I think this is… yeah.
Should probably take out some people. Also, this was kind of the prior… I think prior event, SIG.
I'm just going to do that. None of these people will mind. They were very focused on… Browser events…
**Liudmila Molkova** 18:47 Thank you.
So we talked about this one on the board, right? There is no additional action items to take.
And is this the same?
So, let's take a look at what's in progress. Oh, this…
Is there a difference between a progress and a review?
**Trask Stalnaker** 19:16 Hmm…
I don't think so. Not in my mind.
**Liudmila Molkova** 19:24 Or maybe, I mean…
**Trask Stalnaker** 19:25 It could be, but I don't know if we need…
**Liudmila Molkova** 19:34 Okay, this area the same… Is this in progress?
Roberto, are you familiar? Can you summarize what's going on here?
**Pellared** 20:08 It's just supposed to be kind of a clean-up PR,
But, in my opinion, it removes too much and does not improve clarity.
So, yeah.
**Liudmila Molkova** 20:23 I'm not sure…
**Trask Stalnaker** 20:24 Yeah, I'm not sure this should… do we really care about this in the log sig?
This feels like a spec maintainer.
**Pellared** 20:33 I agree.
Yeah, it's just technically 10 years.
**Trask Stalnaker** 20:36 Yeah, let's remove it from the log sig. This doesn't… It's just not really…
**Pellared** 20:42 Did you have any advocates for social media?
**Trask Stalnaker** 20:44 It's more like a…
**Pellared** 20:45 Consistency chore-y, something.
Yep, I agree.
**Liudmila Molkova** 20:57 Wonderful.
I didn't make any progress on this one.
Not sure if there is something to discuss. Oh, maybe we should, talk about the sensitivity. I think we can make some…
**Pellared** 21:19 Damnia?
This question around that trust you created.
**Liudmila Molkova** 21:25 And this shoe.
and specification.
I don't know why I always.
**Trask Stalnaker** 21:35 Oh, yeah.
**Liudmila Molkova** 21:35 Cheer.
**Trask Stalnaker** 21:37 Yes, yes, the exception messages capturing sometimes PII or sensitive data.
**Liudmila Molkova** 21:46 Yeah.
**Trask Stalnaker** 21:47 Sadly.
**Liudmila Molkova** 21:51 That's funny.
I think… Right.
**Trask Stalnaker** 21:55 That's a diff… Isn't that a different… Oh, I guess it is kind of related.
Yeah, you're… yeah, I guess it is kind of related. I see it as a little bit different, but…
**Liudmila Molkova** 22:09 Exception message.
Even exception. Hi.
Exception message, for sure, and spam status.
**Trask Stalnaker** 22:22 Yeah, cardinality-wise. This one is, I think, the cardinality question.
**Liudmila Molkova** 22:27 Oh…
**Trask Stalnaker** 22:31 should span status error description, does it need to have low cardinality? Oh, okay, maybe I'm… Mixed up.
**Liudmila Molkova** 22:44 What?
Yeah, yeah.
But… It sounds like…
We already have the problem when we define the errors and, exception event, that exception message.
Could be of a high cardinality.
Oh, sorry, could be… could contain sensitive data.
And when it's limited to exception, but…
**Pellared** 23:11 Both are through rules.
Right.
**Liudmila Molkova** 23:14 It's not a problem, the high cardinality is not a problem, unless it's on metrics, right?
**Trask Stalnaker** 23:19 Span status, why did I, can you see what… what kind of spec language I quoted in the issue?
Okay, maybe… My concern was…
documented and predictable?
I don't know what my concern was.
**Liudmila Molkova** 23:53 Oh… For the sake of this group, I think we should talk about Exception message versus error message.
Because the span status… would follow.
And we don't care about predictable.
We cannot demand being documented.
**Trask Stalnaker** 24:20 Yeah, I agree.
So, exception message versus error message.
**Liudmila Molkova** 24:28 Exception message, plus error message, plus… sensitivity.
Because we now have both. We used to have just one exception message.
Now I have both.
And… You're making an argument that
At least, when they were in one place, exception.message.
we could at least make the PII reduction, or some form of reduction.
Easier than if they are spread across multiple.
places.
**Trask Stalnaker** 25:05 I see.
**Liudmila Molkova** 25:10 And it… China Alliance was… what I…
But I was struggling a little bit, in the PR… Here… Which one? This one.
that… We… we're having both error message and exception message.
We are…
**Pellared** 25:38 Breaking.
**Liudmila Molkova** 25:39 things harder.
**Pellared** 25:40 Yes, I agree. Do we have already error message, or is it stable or not? Because I also… even right now, in Go, we are using exception message as an error message.
we are fine with it. I think the distinction is very hard.
development errors.
Message.
**Liudmila Molkova** 26:02 But you're saying you don't care if it is called exception.message.
**Pellared** 26:07 Yeah, we do not care that much.
If it… I think it will simplify and probably make it easier if it's everywhere exception, but we already have error type, which makes it right now more troublesome.
**Liudmila Molkova** 26:22 Now, error type is different than exception type, though.
Even in the languages that have exceptions.
**Pellared** 26:32 Okay.
**Trask Stalnaker** 26:36 Or only in the cases where… Languages have exceptions.
Different.
**Liudmila Molkova** 26:47 No, because in Go, let's say, you can have a server certificate invalid, and whatever
Type of the exception at this…
That type of the error is not the same as, let's say, error code, like 500.
**Pellared** 27:04 Yep.
Cheers.
What I want just to say that it will look awkward, but it's on… I don't think it's a problem that you can have an error tied together with exception message.
Unless we want to keep the exception message.
**Liudmila Molkova** 27:25 In a perfect world, I would… if we were designing it from scratch, I would say that there should be just error message.
**Pellared** 27:31 Yeah, but let's… but we already have exception message, then let's keep it.
**Liudmila Molkova** 27:36 Yeah, and this is the strong reason enough to keep it.
**Pellared** 27:39 I agree. I agree.
So, what's again?
**Liudmila Molkova** 27:47 Let me… Take some notes.
So, let me first.
**Pellared** 28:01 email address, is it even okay to even change this, document that you show this registry, even to note that the error, and here, even change the first attribute and change it to exception message, even though it does not have the prefix.
Of exception, but just to have it on one page for, you know, readers.
Do you think it makes sense, or not really?
**Liudmila Molkova** 28:28 We… we could… we could list it as a dep… we could deprecate this attribute and say, just use exception.message.
**Pellared** 28:36 That's what.
**Liudmila Molkova** 28:36 It would be listed here as to separate deprecated attributes. There is only one convention that uses this message… this thing right now, and they probably would not care either about using exception.messages.
**Pellared** 28:53 Okay.
**Trask Stalnaker** 28:55 I want to talk about it more. Sorry.
**Pellared** 28:59 Yes, okay, goodbye.
**Trask Stalnaker** 29:01 I was struggling with,
Like, logs, like, all these things, all these large domains where… Exception isn't normal terminology.
Like, I'm gonna log my error… my logger. It's an error message.
Exception… was created… in OpenTelemetry, very specifically, I feel like, to model exceptions.
In languages that have exceptions.
And I'm trying to think if there's any path forward for us to…
Keep that.
But, sort of… Reduce its importance.
Like, really box it into that use case, and… introduce error…
**Pellared** 30:30 Have you watched?
**Trask Stalnaker** 30:31 as the… general… Bing.
**Pellared** 30:37 So, Tras, this, like, is kind of in line with my perception that I had before this meeting.
that, we have this span events, and we have this API for record error in spans, and most of the spans that… well, most of the things right now, and we are thinking about stabilization… stabilizing the instrumentation library for HTTP instrumentation.
And basically, we're thinking that instead of creating events, we should simply use this error, type and error message attributes instead of using events when something plays with error. Because it's always a terminating error, it's not like an exception that, you know, something happened, it's not like a real event, it's, you know, basically.
there was a request, there's a response, there's, you know, an HTTP code, like, like, 500 or whatever, and we just want to, you know, mark it as attributes, because we find it more efficient, and using, you know, the exception type there, and we think… we feel that…
It's not a good practice, so we were thinking about just having
So we were just thinking about having recommendations to not use this record error when it's not a terminating error, and just use these attributes instead, basically, this error type error message.
That was what I… we thought, but… and this is also an issue which I'm assigned to, but I happen to have time to, you know, describe everything, and put all my thoughts.
And see how it's also back… and… and think about backwards compatibility.
**Trask Stalnaker** 32:17 Yeah, so we had a… Bunch of discussion at one point around these… Ban, terminating…
Exceptions for span terminating errors.
And…
**Pellared** 32:33 I'm responding.
**Trask Stalnaker** 32:33 I like the idea of… Stamping those directly onto the spans, instead of span events.
There was also… the concern…
**Pellared** 32:49 I think it was brought by Ted, but it…
**Trask Stalnaker** 32:51 Midson… mid-sense about…
Like, you still want your error, like, a lot of people still want their errors in logs.
Like, that's where they are going to see… to find those things, so… But I… Feel like that.
you know, We could say, hey, as this…
OpenTelemetry's default is braided, and spans are, you know, why not capture them directly on spans? But you could also have a span processor that
duplicates… Errors out into logs.
So I… I mean, I…
I think there might, I'm not sure. I think there might be a way forward for…
Introduce for errors and exceptions, sort of, coexisting.
But I… I think we have… to…
There's a lot of work that Lydmilla started in the… in her OTEP.
**Pellared** 34:29 Hello, dear.
on your.
**Trask Stalnaker** 34:32 I think we… Because it will be a… Kind of significant change.
direction… Or a meaningful change of direction, I think we need to…
really play that out and have, like, a pretty good, confident, like, here's how it's all going to play out, and that's what I liked
Lydmila, about your OTEP.
Was that it was kind of attempting 2… map that.
**Liudmila Molkova** 35:09 So then… It sounds like.
We're… Can't try to build a perfect world with…
Exceptions meaning exceptions, error meaning something broader.
I think we could even work with, like, black and pot might not be a problem, because
This is only exposed on span events.
**Trask Stalnaker** 35:38 Technically, yeah.
I think it's leaked out into more places, but at least at the spec…
and semantic level, I think we're… we're kind of safe-ish.
**Liudmila Molkova** 35:54 And then, if we think it's a good start… I think it's the better story than using exceptions for everything. So let's try to build this.
Beautiful.
**Trask Stalnaker** 36:06 I'm just gonna have a hard time in 5 years justifying why, HTTP error… errors are stamped with exception.message instead of error.message.
From, like, I mean, from, like, a HTTP load balancer, or, you know, something like that.
But has no concept of… What we would traditionally think of as exceptions.
**Liudmila Molkova** 36:33 Cool.
So then, the conclusion.
That's the goal is option 1.
I, might regret.
Cool.
And we still believe there is room for both. It's not that we would deprecate exception.message, because we would populate it in a very narrow, well.
Narrow enough cases.
**Trask Stalnaker** 37:16 We could consider it.
I'm… I mean, I… I… I don't wanna… I don't have a… I…
My initial thought was that they would coexist.
And… I think that is probably an easier… back compat story, although…
We have the opportunity with span event deprecation to… Move away from that.
So… Nope.
**Liudmila Molkova** 37:51 Oh, Span Events is one place. The Loggers, Logan Bridges is another one.
**Trask Stalnaker** 37:57 It's crazy.
**Liudmila Molkova** 37:57 It must have leaked there.
**Trask Stalnaker** 38:02 Robert, did it link to…
**Liudmila Molkova** 38:07 Do you use exception message in Go, login bridges?
**Pellared** 38:11 Nope.
**Liudmila Molkova** 38:13 What do you do there?
**Pellared** 38:15 We just have a message about you.
**Liudmila Molkova** 38:19 Oh, the exception message…
Wait, when you use, let's say, as law, can you give a body and exception? An error?
**Pellared** 38:27 Nope.
**Liudmila Molkova** 38:29 Oh, okay.
It's good.
**Trask Stalnaker** 38:36 I think we have one library.
**Pellared** 38:40 I think… I was just double-checking the background one night.
**Trask Stalnaker** 38:49 I feel like from the spec, we might be… Okay, but,
It's definitely leaked into places like… That… Where is…
**Liudmila Molkova** 39:07 And if it… if it has leaked as…
In the languages that support exceptions about exceptions, it makes absolute sense to keep it, right?
It's only the question for other languages that don't have exceptions, or use it unconventionally, and if it's limited to, I don't know, 1, 2, 3 bridges…
then… I mean, they can handle their background story in one way or another.
Okay.
Awesome, we've made some progress here.
Do we want to… Try to design something from the to-do list.
**Trask Stalnaker** 40:02 Not super motivated.
Okay.
**Liudmila Molkova** 40:10 Yeah.
**Pellared** 40:15 Personally, I want to focus on… On stabilizing the complex attributes.
And…
**Trask Stalnaker** 40:22 Yeah…
**Pellared** 40:23 These errors and span events.
and just as a present, as a Christmas present, just have this ergonomic API. I do not want to work on more things right now.
**Trask Stalnaker** 40:36 For the complex attributes, stabilizing those, because,
Yeah, we have Jan 15th is the date that we can start stabilizing them in the SDKs.
So… Do you… do we have an issue with, remaining… any remaining things documented?
Or are we ready to just mark it stable? I mean, I know we have prototype…
**Pellared** 41:07 We're ready… I think we're ready to market and stable. I think I addressed all the comments that were before.
**Trask Stalnaker** 41:15 You want to do the honors?
**Pellared** 41:17 Yep, yep, I… before you joined, I… I said that I was ready to… to… to redo it.
Tomorrow… Or… not the next week.
**Trask Stalnaker** 41:27 Alright.
**Pellared** 41:28 Yeah, yeah.
**Trask Stalnaker** 41:29 Cool, yeah, let's do it, and we can… Doesn't need to merge before…
**Pellared** 41:36 Yes, we can merge it in January, you know, just to have it open.
And… Get feedback, approvals, or…
**Trask Stalnaker** 41:46 Yeah, go ahead and put in there that, you know, that we want to merge it,
By Jan 15th.
Since that's… the… So that, sDKs can start…
stabilizing, because, Java's, we are itching to…
Pull that in, and it'll go as…
**Pellared** 42:13 Yeah, for years old.
**Trask Stalnaker** 42:16 Yeah, yeah, yeah, so you can cite us. Yeah, so let's make sure that people know that we're serious about this. We'll…
Cool, awesome.
**Liudmila Molkova** 42:31 Cool, and thank you all.
**Trask Stalnaker** 42:34 Thank you.
**Liudmila Molkova** 42:36 You're next time?
