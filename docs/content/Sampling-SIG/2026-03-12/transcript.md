SIG: Sampling SIG
Date: 2026-03-12
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Otmar Ertl (Dynatrace)** 01:58 Hello, Chris.
**Chris Marchbanks** 01:59 Hello, Otmar.
How are you?
**Otmar Ertl (Dynatrace)** 02:04 Fine, how are you?
**Chris Marchbanks** 02:06 Pretty good.
**Otmar Ertl (Dynatrace)** 02:25 Alright, pizza.
**Peter Findeisen** 02:27 Hello?
**jmacdonald** 02:53 Hi, can you hear me?
**Peter Findeisen** 02:55 Yes.
**jmacdonald** 02:55 Alright, good morning. Sorry I'm a little late.
**Peter Findeisen** 03:00 We're here again.
**jmacdonald** 03:01 doesn't mean that I have an agenda. I'm gonna look at the notes, and I know you on the ones are doing some work that at least shows some progress, and hello, Chris, good to see you again.
Here comes.
Here comes.
Well, folks, do we have anything new in the world of sampling?
The notes don't have anything, but that's sort of normal.
Since I see you here, Chris… Why don't we ask you if you maybe have an agenda item?
Today.
**Chris Marchbanks** 03:52 Yeah, I was… jmacdonald 03:54 I remember… yeah, let's go… what do I remember?
Actually, I don't remember what I remember. You were talking about partial trace sampling.
**Chris Marchbanks** 04:02 I was a little curious about partial trace sampling. Really, the general idea is I'm very curious around… Having a little bit more… a little bit easier to configure sampling rates for services, which partial choice sampling was also… was one option. I was a little curious around… I know, like, Jaeger remote sampling is supported if you use the shim.
I was curious if there's anything related to that.
Planned for?
Otel as a whole, not specifically, must use Jaeger stuff.
**jmacdonald** 04:41 Yeah, well, that's, a fine topic and relevant. So, we have a good group to talk about it. I hope, that we can ask both Peter and Atmar for their positions on this topic. I would start with Peter.
Mainly because I… I want to recognize and applaud his work on declarative configuration for sampling, and the OTEP 250 was a step in that direction.
And there's a whole topic here with declarative config. And then I would pass to Atmar, who has done some tremendous work on partial trace estimation, I think is what I might say. And, it's a nice topic.
And of course, I have thoughts. Jaeger has been a presence for a long time in OTEL, and Yeah, like, I would hand it to Peter, like, what… we've been talking about declarative configuration for sampling, and that's at least a major part of it.
**Peter Findeisen** 05:41 Yeah, so… With respect to partial trace sampling, I can… I can share my thoughts and, experiences, So, yes, consistent probability sampling was designed with partial trace sampling in mind, so it was definitely possible.
When we implemented this using the old version with its powers of 2, I got quite a lot of friction within the company. They did not want to see partial Traces… On the back end, because it was a logistical nightmare for them.
So… Yeah, well, this is where we are with that.
I… well, we all know that Jaeger Remote Sampling was there for a long time, and it is… it is so far the only remotely controlled Standard way of sampling.
We are all anticipating that OpAMP will replace it.
And, with… with declarative… Including the declarative, Configuration of the agent, something will be changed dynamically.
That will replace Jaeger remote sampling altogether.
That, these are my thoughts here.
**Chris Marchbanks** 07:25 Excellent.
**Otmar Ertl (Dynatrace)** 07:27 Yes.
From my side, so, I mean, the paper is already pretty old.
Yeah, it was… back then, it was, you know, more like, you know, a vision, how to… What you could do, what you could estimate, yeah, but provided that everything is sampled consistently.
So, this was also my motivation to also… you know, define… consistent sampling properly in OpenTelemetry.
Yeah, and I think, how we've defined it, I think it's not possible. I mean, there's still a lot of things missing in open telemetry, because I think it only It really makes sense if you also ask, you know, like, throttling, automatic throttling, or, you know, the idea is that every… at every service, you can choose the sampling rate independently.
According to the local… Constraints, resource constraints, whatever.
**Chris Marchbanks** 08:39 Or… Otmar Ertl (Dynatrace) 08:40 Dependent on local properties, if it's locally considered as an important spend, or whatever.
And still, you can do unbiased estimation, not only on the span itself, but also across the trace.
**Chris Marchbanks** 09:00 Yep.
Okay.
So, kind of, definitely friction, then.
In terms of actually just deploying any of these ideas that you saw.
And I will read through OTEP250. Thank you for the link on that one.
**jmacdonald** 09:21 Aha! I would second everything I heard, you know, like, I was admiring all the work that was just mentioned as it happened.
I do have some more resources I would pull up, but it's gonna take a second. One thing is that the, as Peter mentioned, the old power of two approach that we took years ago, we actually wrote, like, a lot more comprehensive documentation about it.
And I want to find that document, because it does talk about… as I remember it, there are producer and consumer recommendations that, you know, like, if you take the entire possibility space of partial sampling, it's nuts, because you can end up with, like, every possibility of parentless children, and childless parents, and ancestors that are connected with missing nodes in between, and we have never tackled the larger space, although I think both the people here have I've thought about it a little bit.
So, as I recall, in the… maybe in the current document, but definitely in the older document, we published at least some sort of… not normative.
text saying, if you really want partial trace sampling to work, there has to be some sort of, like, smaller set of rules that we observe. And that usually tends to be, a non… non-inflationary, or, like, the probabilities can only rise as you fall down the trace. Otherwise, you end up with parents that have no children, and that's often not very helpful.
But often is only true, like, some of the times, you're gonna need that if you have a large trace space, or, like, 5,000 children just happened, and that's when we got… the last week we talked… the last time we talked about trace pruning, I know that's under development. So, So, and the… for me, the backstory goes even further. Like, at Google, in my ancient past, there was this inflationary sampler approach that, would use conditional probabilities. It's, like, hard to understand, but, like, it works out so that you can say, my parent was sampled at 50%, and I want to be sampled at 25%, so I need to flip a coin that's not 25% anymore. It's some, you know, the math tells you where that lands.
So that was what we… what was being done at Google, and and so… But… And then… And then Jaeger came around, and Zipkin came around, and OpenTelemetry came around, and we've been talking about sampling for years, and there's no, And we've only recently gotten to the point where we can at least count those things and encode the fact that this was probability. So we still have to follow those consumer and producer recommendations, which, the way I think of them, are to get what I call sub-trace completeness. So.
The simple case is your parents are not always sampled, but if you're a rare child, you can sample yourself and get your children sampled, because you're rare. And as long as there's no rate limiter to turn the other… to, like, force the other direction, then you've got a simple case of a complete subtrace.
**Chris Marchbanks** 12:24 And that was, yeah, that was some of my experiments when, like, okay, that seems valuable to me. Like, there's concrete use cases for that. I tried a little bit around, yeah, the other problem you mentioned, where you'll lose parentage, where you'll have, like, service A is sampled, service B isn't, service C is sampled again, and you lose that.
**jmacdonald** 12:45 Tomorrow, at least I remember talking about this once, the idea of maybe… maybe using some sort of additional trace state field to, like, indicate how many parents were skipped, or how many descent… like, I don't know, this is so far into the, like… Otmar Ertl (Dynatrace) 12:59 And, also to have the direct connection to, you know, to your ancestor. So, it means… if, you know, one note is skipped in between, you do not have… you have lost that parent relationship, because usually you just have the parent.
a Spain ID.
But, you know, if you skip the sampling of the parent, then it would be nice to have maybe the grandparent IDE instead to have this link, at least, and maybe in addition, the knowledge that, you know, there's one One span between this train.
**Chris Marchbanks** 13:33 Yeah, I did kind of a hacky, like, played around with getting it working with basically unsampled spans in the middle. I collapsed all the information and just had, here's my parent, like… here's… so you could build it up afterward, because, like, our system, like, we're doing sampling, and then we're also doing tail sampling. So, like, I'll rebatch the spans, and I can delete all these intermediate spans.
And it still saved some on egress, and it was like, okay, this helps some, but it was still, like, this is a pretty small niche. I think starting with the, here's a complete sub, like, sub-tree is probably a better approach.
**jmacdonald** 14:11 Yeah, this also touches on, I would say, like, dark corners of the hotel specification, where it's not only a sampling problem, you can make this into a wider issue about verbosity. Like, in logging, you can have a debug statement that gets skipped, that's normal. And in tracing, we start with this sort of, like, assumption that all things are trace-level verbosity or something like that, and you either have them all or not.
And really.
that's just not fine enough for the real world, where you might have verbose tracing that you want to turn off, and that shouldn't break your parentage. It's just, like.
take out more detail, but… If you look at the hotel spec closely, there are some, like, haphazard or historical remnants that are sort of just, like, warning you away from that.
because… because of a must statement that doesn't have a great justification. Like, a must statement saying you must create a trace… a span ID even when you skip a span, and that gets in the way of this discussion, but it's… I think an accident.
Yeah Let's come back to Jaeger Remote. I think the dream is still alive, and that's been my… one of my guiding, pushes here.
Sure, it took years to get our… Probability sampling working Because, to me, that was the… to me, 5 years ago, that was the elephant in the room. Like, my ex-Googler compatriots back at my old company were like, Josh, why does OTEL not have probability sampling figured out? And I'm like, hmm, let's see if we can convince them to take the Google approach. Definitely not.
it's harder. It's harder when you have the real world, and you don't control the entire monorepo, for example. So, So, the Google approach didn't work, and Peter and Atmar and I and others have worked this out. I'm very pleased with what we've done, but it's time to move forward.
And the dream for me, I don't know, I've said this enough times, but I'll say it again since your fresh ears are in the room, Chris.
Jaeger Remote is still… what users think they want, and I say think they want because, if you give them what they want, we will find out that they don't quite want it. And so, the idea of even what, you know, OTEP250 and the idea of declarative configuration is nice, but don't ask the users to set it. They will get themselves into a mess very quickly.
But an agent, like OpAMP, should be able to control sampling through declarative configuration. That leaves an open question, which is where my dream fits, or at least I think, well, my, I don't know, my role in OpenTelemetry often is to try and find the open source benefit. Like, I know what my company wants, and I know what your company wants, and I know what all the companies want, but I think of the user who's not represented by an observability company often, and so then I end up looking at whatever sort of feedback loop is popular these days, and I think Jaeger Remote gave us an example, a kind of proof of concept, that you can have a remote configurator Controlling your configuration, and you can have a server with knowledge of more than one client deciding how to sample, and then you can have a feedback loop.
Or you can have at least some sort of full information exchange, where… and I ran into trouble with Jaeger remote, and I asked Jaeger's people very directly, more than one time, wouldn't it be nice to kind of fit the probability sampling work that we've done onto Jaeger Remote, like, I'm really just trying to add probability sampling so I can count my span, I've declared so many times. On arrival, I need to be able to look at the span and count it. I don't have to wait for trace assembly and so on.
Because in the Jaeger world.
You… you… you look at the spans coming in, and you… you have to assume the policy that was used to sample that. It's like… it's not encoded in the data, so you can't just say, oh, I see this span. It was sampled by my policy from exactly 2 minutes ago, which said it should have 37% sampling.
All it has is a spin arrived, and It doesn't tell you the probability, or the policy, or how it got to the configuration, so it's hard to count.
So all I wanted to do was retrofit the counting capabilities using our TraceState solution on top of Jaeger Remote, but there was never any interest from the Jaeger side, and I'm thinking of leaders in the Jaeger space who are also leaders in OpenTelemetry. So… where that leaves me still, I mean, I'm talking a lot, and I, you know, I worked for a trace company that did tail-based sampling and so on, so I kind of get what people are after from the business side.
But today, I think… The easiest example to point out is the Datadog.
Agent, which has, Since many years now, had a pretty solid solution that's, like.
not especially complicated.
It is not… full-blown, in a sense. Like, it doesn't send the data all the way to the back end. There's no feedback loop all the way to the back end. There's just a feedback loop between the clients and the server on the local network.
And that Datadog agent will return from you… like, you send me some traces, I will return you new sampling instructions. You send me traces, I will return you new sampling instructions. And that loop… is… that's what we're waiting for, on top of declarative configuration, is we want a collector component that's a processor sitting there, looking at all the traces, saying, we've got too many of this type, I'm going to turn down the sampling rate of that type. And… At that point, it becomes research, and not… there's not a well-known solution that's obviously going to work.
But that's where the math gets really interesting for me.
if we could only be talking about how to make the feedback loop really work in this room, I would be so happy, like, but we're years from there still.
**I mean, I've looked at… Well, my… my… Peter Findeisen** 20:28 The term for this is inverse probability sampling.
**Chris Marchbanks** 20:31 Yes.
**jmacdonald** 20:32 We talk about it once in a while, but, like, when you have a set of data and you can categorize those sets of data, at least along one dimension, then you just apply inverse probability, and you come up with an expected value that's uniform. That's the basic math that, like, works until you have an open, like, an infinite set, or, like.
unknown elements are arriving, so it's, like, not static anymore. So once it becomes dynamic, that's where it really is a hard math problem, but not so hard that we can't at least come up with good heuristics or works-most-of-the-time solutions.
**Chris Marchbanks** 21:07 Okay.
**jmacdonald** 21:08 And, honestly, this is where I like to, like, turn it over to others. I've been talking a lot, but, I… I have two pieces of, like, I'm super excited about this topic.
to say, and I've said it before here, but since you're new, again, I'm gonna repeat myself a little bit. I did a deep dive into the world of mathematical ecology? Ecomaticians study biological diversity in the world.
And I can find you a paper after the talk, I can Slack it to you, I can Slack it, put it in the notes.
There's a woman named, Ann Chow, who… and it started for me with, So, starting with that observation about inverse probability sampling, I went to a researcher back in my old company, Google, right? And I said, I see this inverse probability sampling quality, I want that, but I don't know what the full set of things is. What can I do? And the first thing I learned about is called the good Turing Frequency Estimate.
**Chris Marchbanks** 22:12 Yep, okay.
**jmacdonald** 22:13 Okay.
**Chris Marchbanks** 22:14 Yes, I'm familiar with that one.
**jmacdonald** 22:15 run that forward for, like, 5 decades of mathematicians studying it, and you end up with this woman, Ann Chow, who has published so many good papers, and I barely can scratch into them, but you come up with these frequency estimates that are first-order approximations for how many unknown species are there.
first of all, and then finally also answered the touring question from back then as well, which is, what's my sampling coverage estimate? So I've just received a bunch of sample items, and I know how many species there are from in my sample, and I can estimate how many species there are.
but I also need to estimate what my coverage is, which is to say, how many species did I cover of the unexpected total space out there? And anyway, so you follow all that, and you come up with, well.
In theory, if I was better at math, I could take a… take that inverse probability thing, adjust it just a little bit with this frequency estimate for unknown coverage.
And now you have a fair, undiased, I think, estimate for unseen species. You just need to reserve some inverse of the unknown species proportion.
to capture all the other stuff. And then your feedback loop works. That's how I… that's my understanding.
**Otmar Ertl (Dynatrace)** 23:30 There… there is just one… one pivot. I mean, this… There's a paper which shows that, if you sample too much, you cannot do this estimation of the Distinct elements in your data stream anymore, So I think if you're, for example, reduced by 1, the data by one, or whatever magnitude, I think you're already lost, yeah. So, if you're interested, I can forward you the paper, which, He's claiming that, but I think this… estimation from… Samples is somehow limited in practice, so it's… Yeah. Like, you can reduce by many orders of magnitude, and can still accurately estimate the number of distinct items in your… Original data set.
**Chris Marchbanks** 24:24 It's fair.
**jmacdonald** 24:25 this is the part of sampling that's always left me with a little mystery. Like, you read enough, and you end up with this sort of, like, what Otmar just said, which is, without enough data, all bets are off. And okay, I don't know what to do with that either, but I know that in practice, we have more than enough data.
Most of the time, and then… You know, anyway, mathematical tools.
**Chris Marchbanks** 24:50 Anyway, I would definitely be curious on that paper, that's also relevant to things I've been working on, which is, yeah, very similar, like… I mean, what I've been working on recently is identifying which attributes are best to use.
To divide up those buckets.
**jmacdonald** 25:04 Interesting.
**Chris Marchbanks** 25:05 So that we can create that feedback loop without… A user having to go configure it, because… Most of them won't, or they will do it poorly, or things change, and they won't do it again.
**jmacdonald** 25:17 Yeah, yeah, absolutely. So that's exciting, Chris. I'm very interested in both supporting you and seeing what you do and helping as much as I can.
**Chris Marchbanks** 25:25 Cool.
**jmacdonald** 25:26 Thank you.
Yeah, I also… this is where… I like this room because we can, like, bounce ideas off Artmar and Peter, who have, like, I don't know, more math background. I once read the algorithm that we know as expectation maximization, or EM.
It's, like, from the 70s. It's a pure math algorithm. It's like… I didn't cover it in computer science, but I did come across it and try to read it. It's just sort of a general statistical method for filling in unknowns in your data space. And, my… my… at my level of mathematics, the understanding I built was sort of like a… like an intuition says that the inverse probability sampling logic is the same as expectation maximization. There may be a proof that the Or close to a proof that says that if you follow expectation maximization and fill in unknowns correctly, you end up converging. The point is to say that my feedback loop converges.
Somehow.
And, that's where I would search.
**Chris Marchbanks** 26:43 Okay. I am curious, somewhat related to the math side of things, one of the struggles I've had is, okay, is estimating cardinality of combinations of attributes.
Specifically, because many of them depend on each other.
And I'm curious if there's any… I haven't found anything great yet for how to approach that problem. Like, it's not too hard… yeah, like, great, we can measure the carnality of this attribute, we can go do the Turing stuff to estimate what we're missing, and how much we're missing.
And then I need to do cross products of this.
Effectively. And you can't just multiply it.
**jmacdonald** 27:28 Wait, I have something for you on this. Excellent. This is a… this is, This is, again, where I am… not the right person. Like, I… I was good at math, always better than most of the people, but I, like, I know my limits, right? Okay. Yeah. So, The topic that I understand is called correspondence analysis.
And, they're at least for two dimensions.
I have in my head… I have, like, a feeling for what… what to do in this situation, which is to… So… So, inverse probability is a one-dimensional solution.
Chi-squared analysis, or chi-squared distance, is the two-dimensional generalization of it, and correspondence analysis is the topic that will explain that to you.
So this is a, like, a mechanism of… I mean, I'm gonna give you the dumb Wikipedia page. I have a book that's my, like, helped me read this stuff, and it's been a while, but, like, there's only so many textbooks on this topic.
So, where… where are we? Like, here's my Wikipedia page, right? And, Like, what are the good books on this topic?
I found one that walked me through it, and I, at one point, proved to myself that I could do two-dimensional sampling, where I knew a latency bucket, and I knew a… well, latency is a continuous measurement. This is more for category variables, but waving my hands a little bit. Can I say tea digest one more time? Sorry.
I had thought about what to do with latencies, and TDigest is one of my favorite algorithms, even if it's a heuristic and approximate, but So… If you have two category variables, and you have, build the correspondence analysis, compute the chi-square distance, use that as your inverse probability, it will lead you to the same place. You're maximizing your expectation, essentially.
I could be… I could have made so many lies just now, but this is an interesting topic for me.
**Cool. This is a place to… Chris Marchbanks** 29:39 go read more. Excellent, thank you. Yeah, yeah.
**jmacdonald** 29:41 I appreciate it, and if you find anything out, brilliant, you should share it here.
**Chris Marchbanks** 29:44 Yeah, for sure.
**Thank you. Well, those are my topics, so… jmacdonald** 29:49 Cool. Still have the notes up. So, I didn't take notes on that. Josh talks about… Good… Turing, frequency, estimates, and CHOWs.
Research into frequency estimates, What else did I talk about? X spec… maximization algorithms? That's not how you spell that.
**Chris Marchbanks** 30:18 And correspondence.
**jmacdonald** 30:20 Remote Sampling, correspondence, analysis… It says, Chris will dig in.
That's my notes. Cool. Great.
Thank you for entertaining me, Atmar and Peter, by listening.
To this.
And we'll see… I think we were finished today. I'll see you all again in two weeks, and I'll catch up with Yuan Yuan on the Slack, because I know she's waiting for me to review some stuff.
Go, trace state probability sampling.
Yeah, thank you.
I'll see you next time. Thank you.
**Otmar Ertl (Dynatrace)** 30:59 Yeah.
**Chris Marchbanks** 30:59 Bye.
**Otmar Ertl (Dynatrace)** 31:00 Nothing.
