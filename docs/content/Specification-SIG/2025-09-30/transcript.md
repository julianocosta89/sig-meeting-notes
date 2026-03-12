SIG: Specification SIG
Date: 2025-09-30
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:05 Hi, everyone.
**Lei Wang** 01:12 Hello.
**Liudmila Molkova** 01:53 Do we know who is driving the call today?
**Armin (Dynatrace)** 01:56 I can take care of that.
**Liudmila Molkova** 01:59 Oh, guys.
**Armin (Dynatrace)** 03:01 Robert, have you talked to Bogdan? Will he be joining today to discuss your prototype there?
**Robert Pająk** 03:11 I have not talked about Bogdan.
If you ask me.
**Armin (Dynatrace)** 03:16 Yep. Okay.
Do you want to kick it off, or do you want to… Wait a minute or two for more people to join.
**Robert Pająk** 03:24 I think we can kick it off.
**Armin (Dynatrace)** 03:28 All right, then adios.
**Robert Pająk** 03:32 Crystal, maybe I'll share my screen, then?
Yeah, so basically some time ago, Oh, Jesus.
Can you see my screen? First question.
**Armin (Dynatrace)** 03:43 Yep, all good.
**Robert Pająk** 03:45 Okay, so basically, Bogdan, two weeks ago, created, an issue regarding the confusion whether login API should be actually used by the end users, which is not, because right now, the specification kind of, In the README, in the main section, it does not talk at all about logs API use, that is the fact that it can use the end user. That's one issue. Second issue that some people might find that the Logs API It's not ergonomic for the end users, so it has only, like, emit and enabled, functionalities call out by, call out with specification.
So, I think it might be especially important for Java. So, basically, I propose during the events vision.
I remember that we were talking that, we were, thinking about having a separate ergonomics API, which may be, like, optional for given languages. So, basically, I have just proposed how, I called it here a login facade, which basically is just a front-end for the logs API, how it can look… how it could look.
Basically, it looks like a regular library, so basically this is modeled mostly on S-Log, which is the standard library for, for logging in Go.
The main difference is that it contains the open tele… it's… it's… It's not the standard library. It, for example, could have, dependencies to log attributes. It could also have the kind of data model, which there is driven… which is basically taken from the OpenTermacy logs.
So, for instance, it has things like event name, or it could have event enabled, etc.
So basically, it's very similar to a regular login library, but you just have the concepts from the hotel.
And, yeah, I… so I have just created it, and basically looking for feedback. Is it something that's actually needed, and whether we want to have it in the specification or not.
Any questions, or should we just wait for Bogdan to basically have a feedback? But maybe it's Rask and Udemy also for some feedback here.
**Liudmila Molkova** 06:15 I have some thoughts. I like the idea of having such API.
At the same time, I feel we are trying to stabilize everything around logs and events.
And if we start working on it now, we would distract ourselves from the first wall, and it sounds like it can be added Incrementally.
**Robert Pająk** 06:39 It's already rooted.
Okay, any other thoughts, comments?
One thing which I want to personally add, that in my opinion, this ergonomics API, how it can look like, and what ergonomics people would prefer, may depend on the context and on the applications and libraries, so I thought that it's… It may be rather something for country that just has a dependency to the logs API, there's something which is included in the API itself, but it's just my opinion, it may also be language-specific.
And that's all from my side.
I will stop sharing.
**Armin (Dynatrace)** 07:41 Any more feedback on the topic?
**tsloughter** 07:43 What?
**Armin (Dynatrace)** 07:44 move forward.
**tsloughter** 07:45 Oh, sorry.
**Carlos Alberto Cortez** 07:51 Sorry, I don't know whether I joined late, sorry for that. Something to talk about, just to mention here.
Is that in the past, there was a conversation about having a higher level abstraction for traces and metrics as well.
So that reminds me of these… And if we were to ever do that, I think we should probably prototype traces and metrics at the same time, or something like that, you know?
Just for considering that. There was actually even an OTEP at some point, I think.
**Liudmila Molkova** 08:25 The Instrumentation API tab?
**Carlos Alberto Cortez** 08:28 Correct, that one, yes.
**Robert Pająk** 08:34 Has it been worse, or lost?
So that's… or… No? Okay.
**Armin (Dynatrace)** 08:39 No, I don't think so.
**Carlos Alberto Cortez** 08:41 No, it wasn't.
**Armin (Dynatrace)** 08:42 It's the one providing a type-safe API, right?
Built on semantic conventions.
If you're talking about the same one.
**Carlos Alberto Cortez** 08:54 I think it overlaps with that. I think that probably was just yet another tip.
**Armin (Dynatrace)** 09:03 Oh, okay.
**Carlos Alberto Cortez** 09:05 Yeah. Anyway, just… You know, for your consideration.
**Robert Pająk** 09:11 Carlos, if you find it, you can just add it as, you know, as a bullet point, if it's possible.
**Carlos Alberto Cortez** 09:16 Yeah, actually, that's a good one, yeah, let me look for that.
**Robert Pająk** 09:19 Thank you.
**Armin (Dynatrace)** 09:27 Alright, thanks. Then, next up, Lai, do you want to share your screen, so you can walk us through your issue?
Or should I share it for you?
**Lei Wang** 09:38 So, yeah, can I… can I share my screen?
**Armin (Dynatrace)** 09:41 Sure.
**Lei Wang** 09:45 I'm not familiar with, so… Let me figure out where it is about to share my screen.
Okay, can you see my screen?
**Armin (Dynatrace)** 10:09 Yep.
Terminator right now.
**Lei Wang** 10:13 Alright.
So, right now, I found the… we have semantic collection, defined the coding information.
Like, land number.
file name, function name, but OpenTelemetry Language SDK right now does not have implementation for trace for SPAR.
Nope.
So, right now, we are working on a feature, so… You know, right now, the AI tool is very popular, so I try to copy the raw data of SPAN, the spam data, into cloud code, or CLI, in my IDE, to ask AI to help me address the issue.
If the span status code is error, or the duration is quite long, I just ask AI to help me address the issue. So AI need to figure out where is the code, right?
So I found that if I copy the service mandate, AI is able to infer the code.
Based on URL, right? But if I copy the client span, or internal span, AI cannot find the position of the code, so it's hard to leverage AI to address the issue.
And also, I think, probably customer, if customer is very familiar with his code, they can… he might also leverage this feature to quickly jump to the code directly.
So, that's why I raised this pro- raise this requirement, ask for support this feature for spot. And also, I already, implemented a prototype, in our downstream distro.
And, So, I followed… I refer to this exact inspect, and I figured out that for server span and client span, actually, there are… slightly different. So that's why I just gave a drafted proposal to distinguish color and quality.
So, Leslie… Let's see, for server spa, actually, the coding information, like LAN number, should refer to customer's code, right?
And, this code, I can call it calling. But for client span, producer span, customers could actually call the library's API, right? So if we show the code information, like, call the number, point to the client or producer library, it does not make sense to customer. So actually, this code information will present the caller.
Customer code invokes this library.
But right now, our existing spec does not distinguish that. I think it's okay, as long as we add the simulation there.
Hotel, yeah, just code information represents a different meaning for different spank time.
Alternatively, we can further enrich this if it's inspect, distinguish caller and colleague.
Let's say, for server or consumer spy, actually, customer may more care about the quality.
But for client or producer spend, customer might hear about the color. 1.
I mean, the direct caller, of API. And for internal span, because both caller and colleague are customer code, so we can show both caller colleague code information.
Yeah, that's what I said.
**Liudmila Molkova** 13:53 I have a question, so there are currently no limitations on where the code attributes can be used. They can be used on logs, they can be used on spans.
But I don't believe there is any integration or any instrumentation that would actually stamp them on spends.
**Lei Wang** 14:10 Oh, no.
For log, I think, there is code information, because logging, logger…
**Liudmila Molkova** 14:16 Yeah, there is one for logs, there is nothing for spans.
**Lei Wang** 14:20 Right.
**Liudmila Molkova** 14:20 So is the proposal here that every instrumentation that creates spans would also report code, or is it something else? Is it the processor? How would you actually stem these attributes and spends?
How would you do this?
**Lei Wang** 14:42 So, the question is implementation, right?
**Liudmila Molkova** 14:48 The question is, like, if you want every instrumentation to be smart enough to stamp quad attributes on spans, it's probably very difficult and impossible to do.
So if there is any processor that is capable of doing this, this makes this proposal more, viable.
**Lei Wang** 15:12 Sorry not to follow your question. Your question is, technically, it's hard to implement this feature, right, in Spain, so…
**Liudmila Molkova** 15:22 This, and also that there are hundreds, if not thousands, of instrumentations where it needs to be done.
**Lei Wang** 15:28 Yeah, I think to support this feature, yeah, we have a tool.
We have to support that for each library. The implementation might be different for library.
**Liudmila Molkova** 15:44 Yeah, I see Tristan… Did you want to say something?
**tsloughter** 15:53 No, I can't right now, sorry.
**Robert Pająk** 16:01 I think in most… in many languages, runtimes, it would be done as a spend processor, basically checking the call stack, and based on it, adding.
Authentic attributes.
**Lei Wang** 16:15 I have, I think a laser table, right?
So, some of language might, be able to support this feature. Just, Yeah, but some of language might not. It depends.
And also, it depends on caller or calling. So, for calling case, we can instrument the… sorry, that's not bad. For colleague case, we can instrument the registration method, let's say for service, but It's quite easy. We just need to instrument the measure, customer provided. And, for quality cases, like client spa or producers, we have to Get caller information by call stack.
Yeah, so if it's by step, we can leverage process.
But, how to distinguish color and quality is your library per library. Every client library, we need to implement, respectively.
**Trask Stalnaker** 17:23 How, how much do you think this can be solved by, the pro… profiling correlation between profiling and traces?
It won't give you, right, every single… span, the data for every single span, but at least you would get a, you know, a collection of spans would have corresponding trade, profile, data.
That the backend could then… analyze…
**Lei Wang** 18:05 Yeah, that's a good question. I don't have an answer yet. Actually, my case is, if customer does not enable profiling, customer just has spanned data. And spend data, actually.
represent the error or long duration. So, if customers want to figure out this issue, just based on spend. It doesn't have profiling data, so how do we do?
Right.
And, actually.
in my prototyping, I found that a lot of cases, I depend on cost deck, and the cost deck actually is literally already profiling, so I know there's a relationship, but right now I haven't had an idea how to leverage profiling.
**Trask Stalnaker** 18:53 So I know one of the things that the, profiling, the signal in OpenTelemetry and the implementation, is doing, at least with some languages, correlating those profile stacks with, with trace data, span ID, trace ID, So you could pull that out.
I guess what I'm… the… part of the reason I'm asking, because, I, I, I totally… like, the… the va… The value of this is… very good. I mean, I agree that, being able to Automatically correlate the span data with code is really useful.
But as Lydmila says, you know, it's… I think it would be tricky if it requires us… To modify every instrumentation out there.
And in general, what we try to lean into on the OpenTelemetry in general is all the signals together.
Like, if, like, as far as our first priority, at least for the use case, would be, hey, use all the signals together to solve it.
and then… but then if you don't have profiling, then if… if we could have a… processor.
To Lamila's point, you know, and that could be a contribib processor, it could be specced or unspec'd, There's some interesting processors, like there's in the Java Contrib, there's a span stack trace.
processor that if a span takes over, you know, X milliseconds, it'll stamp the stack trace onto it. There's some other interesting span processors there. This could be an interesting… a very interesting opt-in span processor.
**Lei Wang** 21:11 Okay, thanks for your help. Yeah, I will… I will investigate if we can leverage profiling, and if we really need, I mean, if customer does not want to involve profiling, I can refer to the, existing process.
Thanks.
**Trask Stalnaker** 21:30 Yeah, but share, share what you, if you do go the span processor route.
It would be, I think, a very interesting span processor. Would be happy to post that in the Java contrib repo, and probably other folks.
**Lei Wang** 21:46 All right, and right now, I think, from my team, the priority is Python. Probably we can show the Python implementation once it's done.
Perfect.
Thanks.
I will stop sharing my screen.
**Armin (Dynatrace)** 22:16 Any more comments on the topic?
Alright, passing it on to Carlos.
**Carlos Alberto Cortez** 22:30 Yeah, hello! I posted up on a pair of PRs, they are kind of old, but, they will be merged soon, most likely. The first one is about the plan to deprecase trace IDO, trace ID-based sampler.
Because we never actually clarified what was the exact behavior, so we'll be deprecating that, creating a new one, which will do the same, but, you know, with a proper, explanation of how it's happening. So, it has a pair of reviews, one from Tras, one from mine, from my side, sorry.
this is still experimental, but please take a look at that. Otherwise, we will go ahead and merge that today. So, especially for maintainers, this will be coming your way, so, Please review that. If there are no comments today, I think we can merge that. As said before, it's experimental, but still, you know, it could be great to have some… some eyes.
The second ones are about the changes to… it's a PR that Robert has about changes and whether they should be, like, eventually visible to the disabled configuration.
You may remember that PR, there were some comments on that one. And, trust, what do you think about this one? I remember we wanted to get a prototype in Java or in some other language.
Before we go… went to Canada.
**Trask Stalnaker** 23:55 Sweet.
We have a agreement from the JavaSig.
Okay.
**Carlos Alberto Cortez** 24:02 Perfect.
**Trask Stalnaker** 24:02 Not to block this, the agreement to merge it.
Yep.
**Carlos Alberto Cortez** 24:07 Okay, I wanted to double check. Okay, okay, let's merge that after the call as well. It's looking good.
And that's all from inside. Yeah, if there are no more comments, we can continue offline, or just merge those two PRs.
Okay.
That's all from myself.
**Armin (Dynatrace)** 24:36 Thanks. Also, all that we have from the agenda. Do we have any other last-minute topics?
**Daniel Dyla (Dynatrace)** 24:52 I guess, since we don't have the maintainer's call, it's probably a good time to mention the, election announcement from earlier this week, right?
**Armin (Dynatrace)** 25:05 Good point. Do you want to do so?
**Daniel Dyla (Dynatrace)** 25:09 I don't have it in front of me or anything, I just remember seeing it.
**Armin (Dynatrace)** 25:13 Let me get the… the issue.
Trask might have the dates in mind.
**Trask Stalnaker** 25:19 It's, the blog. I'll… I'll grab the link to the blog first.
So, yes, nominations are open. We would love… people who are interested in running for the GC to nominate themselves.
And That will be from now until… Hmm… my reading… The 17th of October.
And then the voting will be the 27th through the 29th.
**Armin (Dynatrace)** 26:22 Thanks for the reminder, Dan. Any… Questions on that one?
Or any other topics?
Alright, then let's call it here. Thanks, everyone. Have a nice rest of your day. Goodbye.
**Liudmila Molkova** 26:46 Thank you.
