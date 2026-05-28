SIG: Semantic Convention Tooling
Date: 2026-05-27
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Laurent Querel** 03:29 Hi, Jeremy.
Long time.
**Jeremy Blythe** 03:36 Let's…
**Laurent Querel** 03:36 Let me also move to the video. Okay.
**Jeremy Blythe** 03:43 Gosh.
**Laurent Querel** 03:43 By the way, thank you for the review for CGO.
**Jeremy Blythe** 03:50 Yeah. No, it's good.
I do think those are things that… there are… there are a few items in there that I'd like to move.
**Laurent Querel** 04:00 Yeah, inside we don't.
**Jeremy Blythe** 04:01 Into either itself.
**Laurent Querel** 04:03 Yeah. Definitively, I agree.
**Jeremy Blythe** 04:06 Yeah. For now, it's great, yeah.
**Laurent Querel** 04:08 Yeah, and I would not be surprised if, seedlue is, following up on that.
is working with us on the HotelRo stuff, and also on the client SDK, the REST client SDK.
And, he's, contributing a lot, so that will not be surprising if, Is, continue to work on that.
**Jeremy Blythe** 04:34 Okay, good.
**Laurent Querel** 04:36 So what we are trying to achieve, just to give you… I don't know if you get some context regarding this effort.
Not too much.
**Jeremy Blythe** 04:46 Not a lot.
**Laurent Querel** 04:47 Yeah.
So, so the intent, at least for the Hotel LaRue project, I mentioned that in a long time ago, But we are trying to exercise analytic Convention and Weaver at scale.
Just the beginning, because we started, with, A slightly different approach initially, where we annotated the code to describe metrics, mostly.
Creating on the flag semantic convention registry.
And with the goal to expose the process itself Should be able to expose, any instrumentation presented to the code.
With the full detail in semantic convention format.
But we, we are looking… At, now… Maintaining a semantic convention registry for the entire project, extending that to events, and potentially to traces at some point.
In order to validate the instrument and the coverage, And, and also, in order to generate traffic that is, like the waiver registering it.
Slightly different, but mostly the same idea.
So we have, in this, new collector, we have, But we name a traffic jam receiver.
Which will take a semantic convention registry.
And generate, code, and we use that for, log gen… To exercise more generation.
And I'll test saturation into the… the project.
The problem is with the current existing semantic convention registry, which we are using by default.
The, the, the number of, structured events is relatively small.
So the traffic that we generate is too… Repetitive, and not really realistic, even with a semantic conversion register.
So we decided, okay, let's try to, To eat the bird with one stone… sorry, two birds with one stone, to kill it.
two bad reasons still trying to improve my, my English and, use of, classic expression. So, two birds with one stone.
By… Increasing the integration with Semantic Convention and Weaver into the project.
making sure that we have a good, control in terms of, instrumentation. And second, because we have so much, so many, I should say, so many, metrics and events into the project.
well defined.
That we will get a semantic conventional registry, just for the project.
Which will be a much better basis for the traffic generation.
And that's one of the reasons why we are doing that.
So we will exercise the life check in river, a derivation of river limit, reworked into the project, but where we are also using Weaver in terms of library, for example, to load the registries and reserve them and so on. So it's already, I think, a very nice example of We're using the code of river, or, we're using WIVER in a CI pipeline.
To, to progressively do the thing that I mentioned.
Yeah, that gives you some context, and we will continue, I will say that for the traffic jam, it's there from the beginning.
Well, the, the CI control, it's just the beginning, so we, so we, we will probably continue to discover a few things that, needs to be, improved based on this integration.
And, And we are enough in this project to have people helping in Weaver when we see that there is a… And I will definitely make sure that we, We contribute as much as possible when it's justified.
**Jeremy Blythe** 09:24 So the traffic generation…
**Laurent Querel** 09:27 No.
**Jeremy Blythe** 09:28 Commemorating what you said.
That's using the semantic convention… this… it's using your project-level semantic convention library.
**Laurent Querel** 09:36 We will. That's why we did the, the, this, this effort, to simplify the… Sorry.
The dough.
misunderstood. What we… what CSO did was, for the integration in CI, to control that disinte convention, the custom one.
**Jeremy Blythe** 09:53 Yep.
**Laurent Querel** 09:54 is well covered in all the integration tests. For the traffic jam.
We use that now for… for example, we have a continuous benchmark infrastructure in this project.
And, not all, but most of the tests for the continuous benchmark are based on this traffic gen receiver.
And we are currently still using the standard semantic connection registry, and we will move to this custom registry once we have A version that is big enough.
We are progressively, Adding more and more definition there, and then that will become the… the source for the traffic jam in those continuous benchmarks and other.
**Jeremy Blythe** 10:43 Thanks.
So when you do the traffic generation, Are you, Sort of putting fuzzy data in…
**Laurent Querel** 10:54 Yes, we, we look at the data type for each field.
And, attributes.
And, That has been done a long time ago, so I try to remember the details, but we take into account the name.
And, and we, we generate some, fake data for things that are, like, say, for example, integer and other things. Where we are not entirely satisfied.
That's places like trace ID, site ID, parent ID, this kind of stuff.
I think we should do a much better job.
Because… Depending on what… for what the traffic jel is used. So, if you use it, for example, to validate Different concussion algorithm, or, different protocol.
Then… Having some traits that are more meaningful and more representative is fundamental. Because if you have everything in pure randomness, then the compression will be super low and bad, and that's not necessarily a good validation of the approach.
So we used.
**Jeremy Blythe** 12:15 That's a lot.
**Laurent Querel** 12:16 Oh, yeah, yes.
**Jeremy Blythe** 12:17 How'd you get something representative?
**Laurent Querel** 12:20 Yes, exactly. We want something representative.
**Jeremy Blythe** 12:23 fake.
Right, so it's…
**Laurent Querel** 12:27 Yeah, if it's too fake, it's very hard to validate, because this traffic gen is used for validation, for example, or test the performance. But for validation, it's essential that we have something That is, yeah, like you said, a good representative of all your data.
So that's an example of things where we'd like to… To include the situation.
Being able to Recreate persons with few span.
That, that could be an organized hierarchy, with some hierarchy.
The fact that we have more and more enum.
And we will have a lot of value into the customer history, because we… we try to prevent situations with attributes with high cardinality, so… Which means we can, or we should, be in a situation where most of the attributes, when they are not, at least when they are, I think most of the attributes should be… idium at some point. Either, the numerical Inum, or, string loyalty in NU, so that will give us… Again, something where randomness exists, but in some specific domain.
Yeah, so that's, what we… why we are using the Weaver in many places now, for semantic convention.
**Jeremy Blythe** 14:11 Okay, that's cool.
Yeah, I think originally… one of the ideas for the emit, task in… in Weaver was to… like, an extension of that was to have it, sort of.
produce more.
Traffic than just what it does at the end, is it just… it just regurgitates the examples.
Like, it just uses the example values from the definitions and sends it out just once.
And so… There was an idea.
Back then to go, oh, well, actually, I'd want this to run for some period of time with some, settings that mean I get, like.
Kind of like what you're trying to do there, so… but it sounds like what you've built is built into the… Into this new hotel arrow.
**Laurent Querel** 15:06 Yes, yeah, we have not been able to use… because we have some constraints in this project, So, it's also a REST project, but We, we use a straight-per-core sharing approach. We prevent the use of any synchronization primitives.
So we need a coach ball on what we integrate.
So that's one point. The other point was… Performance, so we… I don't… for this part, I don't think we did a lot of work, but we, it's definitely true that, the code that we have is not fast enough. So, for example, to… For the continuous benchmark, when we try to stress the system at situation level.
We need, for some pipeline definition, we need multiple instances of the traffic gen to saturate.
Because the traffic gen… Itself is consuming too much, CPU, and he's not able to saturate, in fact, well, instead he's not able to saturate, so we need to… to run multiple, and because of this straight-per-core nursing approach, I think when we… we tried to use the code, directly the code from, we write EMIT, We have not been able to do that, so we decided, okay, let's… Extract the image, keep the… the… We've… the registry and the resolution were used from… directly from Weaver.
Oh, maybe I need to revisit the code and see if there is a way to move that back into Weaver, so you could have, the few, evolutions that we did, they integrated into Weaver, and… and maybe there is a way to… to, to share the same code, exactly the same code.
Because… Probably the constraint that we have Oh, not a big deal for Wyvern.
**Jeremy Blythe** 17:17 Hmm.
**Laurent Querel** 17:18 Yeah, I don't know, I need to, to, to see that.
**Jeremy Blythe** 17:23 Yeah, I haven't had a lot of requests.
Like, we haven't seen a lot of requests for that kind of thing for the…
**Laurent Querel** 17:29 Yeah, yeah, yeah.
**Jeremy Blythe** 17:30 compared with LiveCheck, there's, like, lots of things.
**Laurent Querel** 17:33 Yes.
**Jeremy Blythe** 17:33 Live check.
**Laurent Querel** 17:33 Yeah, yeah. You know, I think that will come.
People don't realize the power of this function.
I think that will come because, Well, you are… generating data is super useful in many, many places.
It's useful if you have to, for example, to validate some machine learning algorithm, or, like we do, validation, some, some outcome of this traffic, that could, in our case, validating aquacion algorithm, or validating, the… the… a pipeline transformation.
Carl?
Exercising the… generating traffic, so… for some elements, I think what we need will be a bit, even if it's derived from Weaver, that could be, for example, for a traffic jelly in the context of validating the performance of your system, I think what we did, will be more appropriate.
But, for everything else, I think Weaver will be good enough.
generating, for example, what we… what we don't do in Weaver, I think, you know, maybe something that, Generating a file that is, a dataset, a representative dataset of a scientific conventional registry, with the intent of, applying some, some algorithm on top of it. Probably that will require a little bit more… I think we discussed that together a long time ago.
Being able to use solar notation to, to, to drive the… The simulation of the traffic.
Relatively poor.
Right now, we can express, for example, the… Ratio of how many event metrics, or logs, or span we want to see.
And depending on this ratio, we… We, but it's not enough, I think it's… If you want to represent a specific system, the distribution will matter.
The… obviously, the frequency and how they appear will matter.
So that's definitively things that are missing, but If that starts to be present, yes, people will use that because For validation reason, or… Yep.
Is there anything I can do, like you know, like you saw, I can't put a lot of time in Weaver, but if there are things that you'd like to discuss.
**Jeremy Blythe** 20:36 Yeah, well…
**Laurent Querel** 20:37 of breadstone together, huh?
**Jeremy Blythe** 20:39 Yeah, one thing I was going to bring up today, and I actually have to leave, I've got a 10.30 that I can't miss today.
Sure.
But, one thing I was gonna bring up, so I added the… I added the, the fuzzer.
So there seems like there's two ways of doing it. There's one where you sign up with Google, and you effectively use… I don't know if you know about it, but… So, Google offer this open source service, and some of the other OpenTelemetry projects are already using it. The Go SDK repo, and another one.
Where you, effectively, you offload the fuzzing, task.
to Google, and they run it in their infrastructure, and they use their corpus of fuzz data that they've gathered over, like, long periods to, like, really, stress the… the… your… your little, containers that you wish to first from your parts of your code. That's one way of doing it. Then the other way of doing it is this light version, which is what I've implemented.
But I can't help feeling it… it… it feels a bit like, what do you call it? Like, the sort of… it feels a bit like security theater, in a way. It's like, I'm doing it for the sake of doing it, but I'm… but it's just added, like, a 20-minute.
**Laurent Querel** 22:08 Hmm.
**Jeremy Blythe** 22:09 It's added a 20-minute, job.
To the post.
**Laurent Querel** 22:14 With those three real outcomes.
**Jeremy Blythe** 22:16 with… So I feel like I've done it just because, because Scorecard said you have to have fuzzing to pass scorecard.
And I'm not sure we're going to get any real benefit from it, so I… and what I feel like is we're just going to see… every PR will have a failure in it now, because, you know, Mini Ginger can't cope with.
Some crazy template thing that is unrealistic and nobody's ever gonna do.
**Laurent Querel** 22:47 Yeah, okay.
**Jeremy Blythe** 22:48 You see what I mean?
**Laurent Querel** 22:49 Yeah, yeah, yeah.
**Jeremy Blythe** 22:50 Like, I… I'm tempted to go to abandon it and rip it all back out, to be honest.
But I don't know how important it is.
For the projects to tick all the boxes on the scorecard and get their badge and all that.
**Laurent Querel** 23:06 Hmm.
**Jeremy Blythe** 23:07 You know, as an open telemetry.
project.
**Laurent Querel** 23:12 I don't know, we need to… to ask, probably the… I think, Jurassi is probably the… the person from the Google News Committee.
**Jeremy Blythe** 23:26 Yeah.
**Laurent Querel** 23:27 That could answer this question. Yeah.
I know that, Josh, and probably Lunila, I don't know for Lunila yet, but, Josh, for sure, is part of the technical community, maybe they also have some, Some guidance, there.
But there is… so… you are afraid of having some… especially, I guess, for, yeah, ID dynamic stuff, like, mining ginger, and and GQ.
you are afraid of having some template or PRAM that are so weird that we enter into a problem.
Wash.
That should not happen, but.
**Jeremy Blythe** 24:18 It does. So, Mini Ginger breaks today if you.
**Laurent Querel** 24:21 Oh my god.
**Jeremy Blythe** 24:21 Provide it with a template where it does some… It, it, it, like… It has some equation that it resolves, which makes it open.
**Laurent Querel** 24:35 Yeah.
**Jeremy Blythe** 24:35 Which actually hits, like, an unwrap.
That's in the mini ginger code. So, okay, that's bad. Mini Ginger shouldn't be doing unwraps.
**Laurent Querel** 24:44 Yeah, yeah, yeah. But we have no way to… yeah.
**Jeremy Blythe** 24:47 But it… but it… that's, like… Really? It's, like, it's incredibly unrealistic.
And it's not like we're making code for, you know, life support machines.
**Laurent Querel** 24:59 Yes, yes, yes.
**Jeremy Blythe** 24:59 It's not something that's.
**Laurent Querel** 25:00 collecting production, in front of internet.
Yeah, definitely not, yeah.
I agree. The effort that… Will be required is, is, is not proportionate, to the risk.
**Jeremy Blythe** 25:15 Yeah, so…
**Laurent Querel** 25:16 Yeah.
**Jeremy Blythe** 25:18 Yeah, I think maybe that's a good idea. I'll ask… I'll ask the, unless, in the.
**Laurent Querel** 25:26 good for me.
**Jeremy Blythe** 25:27 It's the threads that, Jurassi,
**Laurent Querel** 25:29 Yeah.
**Jeremy Blythe** 25:30 Runs. I'll ask… I'll ask him now.
**Laurent Querel** 25:32 Yeah, that's what I knew, yeah.
Okay, I will let you, you have this meeting soon.
But.
**Jeremy Blythe** 25:40 Yeah, yeah.
**Laurent Querel** 25:43 Yeah, let me know if there is anything else.
**Jeremy Blythe** 25:50 I don't think… So, I'm not sure what's happened to Josh, but He's been… he's been quiet for a few days, so… what do you got?
Yeah.
**Laurent Querel** 26:04 That's true, I didn't see him. I know that Lyona is moving to Google, or already moved, I don't know.
I know that's, something ongoing.
I don't know.
But for her, yes, I didn't hear about him.
pursue for a few days.
**Jeremy Blythe** 26:23 Yeah.
Okay.
Alright, gentlemen.
**Laurent Querel** 26:26 and, see you soon. Bye.
**Jeremy Blythe** 26:31 Cheers, bye-bye.
