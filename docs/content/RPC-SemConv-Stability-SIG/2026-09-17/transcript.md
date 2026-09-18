SIG: RPC SemConv Stability SIG
Date: 2026-09-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:00 Hello, hi Steve.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:04 No.
**Liudmila Molkova** 01:11 Let's see if anybody else is going to join.
And Sims Trask is joining.
Okay, what do we have?
**Madhav Bissa** 03:13 Hey, guys.
Sorry for being late.
my… Toddlers just pulled the router wire, so…
**Liudmila Molkova** 03:22 Oh, wow.
**Madhav Bissa** 03:24 I was disconnected.
**Liudmila Molkova** 03:27 Thank you for coming, no worries.
Hey, let me share my screen.
Oh, wow, everybody's here, awesome.
Okay… Okay, this one's from the past… Yay, let's take a look at the board, but I think we haven't met in a while, and I think we have a lot of updates.
**Trask Stalnaker (Microsoft Corporation)** 04:24 Can you hear me now?
**Liudmila Molkova** 04:26 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 04:27 Alright.
**Liudmila Molkova** 04:33 Okay… So, let's take a look at what we have in the progress, and… So, Matt, have we… Yeah, we do have a proposal, a PR… To use the request response metadata.
And if you could take a look and give it a review, that would be wonderful.
**Madhav Bissa** 05:04 Sure, I can do that.
Can you add me as a reviewer or something? That way it will… show up in my GitHub.
Tasks, or something.
It's Missa. B-I-A-S-A.
Yes.
**Liudmila Molkova** 05:19 Sorry.
Give me a sec, I'll find it. I didn't wake up yet, so I'm bad at… Hearing, thanks.
Okay, so would love to get your review on this, and somebody else's, so we have two green check marks. I'm pointing at me too.
And… what else do we have?
This is Matt's PR… Addresses this problem.
So this is also something, Madhav would be nice if you could take a look, so… That… problem here was that the… there was not enough details for JirPC specifically.
And there we are fixing this.
My gosh, ICC.
Okay… And then… this is the same, this is the same… I've sent it yesterday, maybe let's talk about it.
In a sec… But it's related to a bunch of other… error discussions we have, so maybe we'll talk about them together.
there was a, I think, an issue we wanted, Madhav to do for you to… Maybe, check…
**Madhav Bissa** 07:34 Yep.
**Liudmila Molkova** 07:34 the replies?
**Madhav Bissa** 07:37 Yeah, so I did take it back to the leads. I think they are okay to concede for this one. It's redundant, but it's not, like, a very… big, it doesn't break anything, it's just redundant, so we are okay to… Agree with what you guys are proposing.
**Liudmila Molkova** 08:00 Awesome.
**Madhav Bissa** 08:00 Which is to have, yeah, I'll just get it confirmed in writing from them, and then I'll come and comment on this one.
So, I am… just to give you guys an update, I am busy on writing a GRFC, which is a design proposal, for GRPC.
To inculcate, all the… Semantic conventions of open telemetry. My PR should be out End of this week or something.
wherein all of this, will be taken care of, how it will be implemented in gRPC.
So, like… You can also see the… You'll also get insight into what the leads are thinking about the changes that we are proposing.
**Liudmila Molkova** 08:48 Awesome, thank you. Will it be in the public GitHub?
**Madhav Bissa** 08:52 Yeah, it will be in the public GitHub. As soon as the PR is out, I can send you a link.
**Liudmila Molkova** 08:57 Awesome. Thanks a lot.
Okay… And then… Maybe let's talk about… Errors.
Yeah.
**Madhav Bissa** 09:12 That's… that's the bone of contention.
I saw you did quite a good bit of research, and you did put some anecdotes in there.
**Liudmila Molkova** 09:24 Yeah, alright, so let me bring it… let's… Jump in.
**Madhav Bissa** 09:35 Yeah.
**Liudmila Molkova** 09:36 Okay, so if I understand, the RPC approach is that you want to treat everything, but okay as errors.
**Madhav Bissa** 09:46 Yeah, that is not okay as errors, yes.
**Liudmila Molkova** 09:49 Yeah, and both on the server and the client, and the server is where the contention is.
**Madhav Bissa** 09:55 Yup.
**Liudmila Molkova** 09:56 I think, like… where I'm coming from is that on, currently, on metrics.
You do not have an indication of an error.
And spans are arguably not a very popular signal. It's experimental, right? It's hard to enable, and it's, like, not… Does not have a lot of information.
**Madhav Bissa** 10:19 It is expensive, essentially.
**Liudmila Molkova** 10:22 Yeah, so I'm… What I'm trying to say is that you didn't face the scale of complaints because you never marked something as an error on your metrics.
And what they tried to do is to find examples of people, complaining about the GPC stance on this.
And I think this is not interesting, this is probably the most interesting things that I found.
That thinks I can't voy.
they actually, when they report GPC stuff.
they do report, it consistently with HTTP, so, like, the not found is not marked as error on servers, BECAUSE people complained.
And there are some other examples of Linkerd, the Datadog instrumentations that had to change.
And just a bunch of examples from the internet AI found, AI, like, check it, it, it, checks out. But essentially.
The moment you express something as an error.
People start complaining when it's not, and even in the GRPC repos, there is… there are precedents.
Where… Lc consolation is an interesting one. We don't… we treat it as an error.
But… there are some cases where you exclude them from error counters, and this is just the start. Like, in up in telemetry, we feel a full pain of people trying to Say, okay, I want to track… track my… I want to see my error rate.
And they don't want to write a filter that includes 5 levels they care about.
They want to have some good default.
And… not found appearing on the server error rate is meaningless for most of them.
**Trask Stalnaker (Microsoft Corporation)** 12:29 Because it's not an error from the service's perspective, right? It's an error from the client's perspective.
**Madhav Bissa** 12:37 Yeah, I understand that. It's a…
**Liudmila Molkova** 12:45 And you can believe me or not, this is… there are a few problems like this, but what constitutes an error is probably one of the most popular Problems to not tell.
**Madhav Bissa** 12:59 Excellent.
**Liudmila Molkova** 13:00 Bugs and user complaints.
**Madhav Bissa** 13:01 Thing is, for us, there is no way to know Where is that… Status code generating form.
Right?
That's the crux of the problem that I am trying to convey over here. So, for example, Permission denied.
could legitimately be an error, right? Like, let's say the service is trying to do something and it is denied a… permission.
And then… then it's a service error.
It's no longer a client error.
**Liudmila Molkova** 13:42 Yeah… It's, like, whatever you pick, okay can be an error, right? Whatever you pick can be an error or not.
And the trick here is that we need some defaults.
Somewhat reasonable.
And then we… I think we need to have… to be able to customize these defaults. It can be an extra feature.
But, it doesn't have to come right away. But I think it's kind of inevitable that, this doesn't work. And there's another issue from somebody in the hotel community about canceled, or that the deadline exceeded that I also want to have a quick chat about. That's exactly that, where we need customization.
**Madhav Bissa** 14:26 Yeah.
**Liudmila Molkova** 14:27 think…
**Madhav Bissa** 14:27 So that's.
**Liudmila Molkova** 14:27 Most of…
**Madhav Bissa** 14:28 Testing approach, where we allow people to configure What they want to… what status codes they want to consider as errors.
And we can start with the default as everything that is not okay as error. And this is an OTL-advised Plugin, if you… or a flag that, if you want to stick to these error codes.
Here is… you switch this on, and then it will just work like… what total intense… As error… as not error to be not error.
So, that's… that approach I can take back and discuss with the leads.
Where we keep it customizable, and then there is a gRPC default, there is an OTL default, and there is a custom… option to… Edit the list.
That… that… that's… that sounds… That sounds like a good compromise, I would say. I don't even know if it's a good solution or not.
**Liudmila Molkova** 15:29 I mean, the… different applications are different, right, for… or maybe even different requests.
**Madhav Bissa** 15:39 Yeah, that's what… so when I… when I spoke to the leads, they were like, we don't want to decide for the application In which scenarios, they don't want to consider this as not an error.
Because for us, the RPC didn't complete successfully means it's an error. That's it. That's the simplest definition.
So… And cancellation can happen for a number of reasons. It need not be client, it could be something, you know, the pod gets restarted. I don't know, there could be different reasons, different… also, different runtimes behave differently.
So… We don't want to own, the semantics of things that we don't control.
Is what, the leads… Told me.
they also understand that we are trying to align… like, this is a hard problem to solve. We are trying to align with whatever else is going on in the industry. So, there are, obviously, Places where server-side errors are.
Different from client-side errors.
So, it's a good suggestion to have a customizable list.
And, you know, give some defaults.
I don't know.
I will try to build that in Into my proposal.
And, let's see how they react to it.
Let's… That's the best promise I can make as of now, but you will see it in a week or two, how they are reacting, like, I'll keep it public.
**Trask Stalnaker (Microsoft Corporation)** 17:13 Yeah, I think that's fine, as long as the semantic conventions, we will say that, you know, we will say that, by default, you know, errors should the, You know, this list.
And… You know, we can put in language about, configurable… configurability, And then, you know, the gRPC library itself.
Wouldn't be conformant with you know, that… But it would have… you would have an option, a user-configurable option, to opt in to open telemetry conformance, for example.
**Madhav Bissa** 18:06 - sorry, first… I lost you there for a second, can you repeat that? I heard you till the point you were saying you can put in a language where we'll have it configurable?
**Trask Stalnaker (Microsoft Corporation)** 18:17 Yeah, but the default, we would be, specific about the default.
behavior in the semantic conventions, which is what we do in other signals. And what you would do then from the gRPC perspective is you could have a setting for users to opt in to OpenTelemetry compatibility or, you know, OpenTelemetry compliance.
Because your default would not be compliant with the semantic conventions, but you can give users an option to opt in to that.
**Madhav Bissa** 18:53 Yeah, understood. Yeah.
That's… that's… I think that's the… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 18:59 I mean, that's always your choice.
**Madhav Bissa** 19:01 Yeah.
Understood.
Yeah.
Yeah, let me do that. I'll take a note. I'm just busy writing up the design proposal, so I'll take a note.
Off that part.
And, yeah.
**Trask Stalnaker (Microsoft Corporation)** 19:25 Let's see. Is that what they call them? GRFCs?
**Madhav Bissa** 19:30 Yes, it's, a request for comments.
Yeah.
**Liudmila Molkova** 19:39 Wonderful.
Okay.
So then I'm excited we have some next steps.
I want to talk for a sec about exactly this problem, but first, I noticed… Steve, did you send it?
**Madhav Bissa** 20:02 Yes.
**Liudmila Molkova** 20:04 Awesome.
Cool, I'll take a look.
Yes.
We have refinements now.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 20:16 Lovely.
**Liudmila Molkova** 20:18 anything you want to call out?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 20:22 Mmm, no, yeah.
**Liudmila Molkova** 20:25 Okay, great.
Okay, then… about the configuration and errors. So there is an issue somebody else created… So this front.
So… There are different concerns here, but essentially it's about BD streams.
And that… The deadline exceeded is essentially a way to end, look, to set a timeout, well, to set an expiration on the… Be the stream. It's not… A failure is just saying, okay, it's time for me to re-establish new connection.
And… Deadline exceeded, we treat as an error.
And… Yeah, there is a 10-minute deadline.
And an application running for 24 hours will produce this number of failed spans.
But, to Madhav's point, there is no way for us in instrumentation to know whether it was expected or not.
Maybe there could be, if there is some… I don't know, we… there is some education, or there is some very good heuristic to tell, okay, we knew there was a timeout of 10 minutes, and now it's more than 10 minutes, so maybe… Anyway, so there could be a way to, for instrumentation, to know But, In general case, no, we don't know if it's… Benign or non-benign.
And there was some discussion that essentially, it's back to the… Topic that we don't know.
And I've asked people to share their… if they have any good heuristics, and nothing happened.
So, I'm proposing the same solution.
do this problem.
S… to… actually, this is not new. We… it's already in the spec. It's already in the guidance. It's already what we do. But… Since it causes so much contention, I wanted to put it in writing.
That in here, right in place, that the instrumentations may use whatever additional context they have.
And that, they, they can provide instrument, the options to configure.
And, we can be more precise with configuration, with Autel configuration, because Autel Rem provides the way to configure things, but, it can come separately.
**Madhav Bissa** 23:46 Sounds good.
Can you add this in the meeting notes? I'll have a look at it.
**Liudmila Molkova** 23:54 Oh, sure.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 24:23 If we have a minute, there's the… Histogram bucket boundary, Question?
And I'm totally fine with, for gRPC, you know, for now, aligning it with the gRPC bucket boundaries.
I did leave a question, though, that I was hoping to get some feedback from the GRPC team.
on… I'd like to… Learn from you all, like, what would be, like, an ideal… Bucket boundary… that would, you know, not necessarily taking into consideration backwards compatibility, but my question is more for general RPC. Can we learn from you all? Can we take some learnings there for our general RPC bucket boundary?
before we market stable. For example, I think it's a very good… point that, like, our lowest RPC bucket boundary is… today is probably 1 millisecond?
No, 5 milliseconds.
And maybe for RPC, you know, we should make that smaller.
**Madhav Bissa** 25:49 Yeah, that… that is very subjective, because each RPC works In different contexts, and with different speeds.
And what may be… too detailed for one RPC system, maybe too broad for another, right? So I… That's a very hard… job to…
**Trask Stalnaker (Microsoft Corporation)** 26:12 It… it is, and that's why we… Bucket boundaries are configurable.
For users can configure them.
But we still have to pick a default.
Right.
And… The question is what… Our… our goal for the default I think Ural's goal for the default appears to be, you know, given that it has so many buckets, it's… the goal is to cover, you know, a much broader range, of, you know, applications.
like, say, 99% of applications, I think our goal with semantic conventions has been to balance cost a little bit more, and maybe only target 90… Percent of applications, like, ideal, ranges.
And so… I was just trying to think, like, for RPC… would a better default for RPC To cover that 90%, should we go down to… 1 millisecond, should we go down to 500 microseconds?
Something like that.
**Madhav Bissa** 27:35 So, I can tell you from my experience, at least.
Anything that we see is going to 500… Microseconds is too slow for us.
In most cases.
**Trask Stalnaker (Microsoft Corporation)** 27:49 Us being Google?
**Madhav Bissa** 27:52 Us being the RPC.
Okay.
And, yeah, I mean, the most context that I have gRPC being used is internally to Google, but also certain external customers. I think 500 milliseconds is too slow for us, but it's… 500 microseconds… may not be too slow for most applications in the world who are using HTTP or other RPC systems, right?
So I think the better approach would be for OpenTelemetry to define that at least These buckets should be present. If you go any more fine-grained than that, and that should be okay. I mean, that… I would be okay with that language, rather than the other way around, where you have a default which is too broad. You should have a range which should at least be honored.
You should have at least these many buckets, and if you have any more detailed buckets than that, and then that is the RPC system's choice. I think that if you… if you, attempt for that, ideal.
I think that would be a much… That would… that would be a better thing to solve, rather than trying to get a general standard for it.
because if all the RPC systems would stick to the same buckets.
In essence, why would we have different RPC systems?
**Trask Stalnaker (Microsoft Corporation)** 29:27 Lots of reasons to have different RPC systems.
I mean, and I, I would.
**Madhav Bissa** 29:32 The primary reason is performance, always, right? If you get these.
**Trask Stalnaker (Microsoft Corporation)** 29:36 I mean, ask Alibaba, they run their, you know, they run their whole cloud on, Dubbo, and, like, they would fight you vigorously.
**Madhav Bissa** 29:48 Yeah, no, I'm not saying that… It's the only reason, but I'm saying.
**Trask Stalnaker (Microsoft Corporation)** 29:54 Like, why should Dubbo have a different… bucket boundary from GRPC.
**Liudmila Molkova** 30:05 probably, because they are… the compatibility probably shouldn't, but let's say if we pick something JSON RPC-based, I don't know, if we consider MCP some version of RPC, the MCP is much slower, right? Nobody cares about performance, well… Generalization, but…
**Madhav Bissa** 30:28 No, my last talk was actually about that in PyTorch.
If you replace JSON RPC with gRPC, what is the performance gain? But, again, yeah, there is The whole idea behind that is, yeah, we operate in different latencies.
And you… sometimes you pick convenience over latency, performance, and sometimes you'll pick… Performance over convenience. So, yeah. But it will definitely be different sets of In fact, to a great extent, mutually exclusive sets of buckets.
So then, if they're not even in an overlapping zone.
how can you define same buckets for them across the spectrum, right? It's… It doesn't look like a problem you should even try to solve.
**Liudmila Molkova** 31:23 All the RPCs we defined, though, like, for real, the Connect RPC and Double are gRPC compatible, and are probably designed for very similar reasons, with just more extensibility to support Other, like, the web protocols.
So the, like, in reality, if we… I kind of see… why… We could have different boundaries, but in practice, we would have the same ones, most likely.
**Trask Stalnaker (Microsoft Corporation)** 32:03 It's also… I mean, I think we have the precedent, I mean, because you could extend that to HTTP as well, and all the different HTTP frameworks, and certainly some HTTP frameworks are… You know, designed for… different purposes, but we still, in semantic conventions, have to pick a default for HTTP semantic conventions.
**Madhav Bissa** 32:34 Okay, let me come to you from a different perspective.
If you define any bucket boundary which is different than what GRPC is already doing.
then… I'm not sure we can do anything about it. That's what I'm saying.
**Trask Stalnaker (Microsoft Corporation)** 32:51 Oh, yeah, yeah. So, no, I still stand by the first thing I said, which is that GRPC, I'm fine with having a very you know, gRPC bucket boundaries being exactly the… your bucket boundaries, right? From a… and we can justify that from semantic conventions, we can justify that as this is a backwards compatibility Reason, and we may or may not ever, you know.
Work with you all to change that.
That's fine. I'm just trying to, take… you know, I'm trying to ask the follow-up question of, Should we… change the default RPC bucket boundaries, To… based on, you know.
learnings from you all that RPC maybe, in general, might be better to have a couple of lower… boundaries.
And we wouldn't And we wouldn't… I don't think we would extend the RPC bucket boundaries to match the general RPC bucket boundaries to match gRPC Just because it doesn't… it doesn't quite follow, sort of, our… General guidelines around establishing semantic conventions for bucket boundaries.
But adding a few lower buckets would be… Would… would be okay for our… from our.
**Madhav Bissa** 34:25 So, maybe we already have a GitHub issue open, right, where we are discussing the bucket boundaries for gRPC. Maybe we can have every other RPC system… pitch in over there, what… what do their bucket boundaries look like for most of their users? And I think that would be a good way to start And let's say, why bind us that we'll not Have more granular buckets for lower… latencies, or for higher… like, we don't really know. Let's… ask every RPC system to comment.
And then… we decide after that.
**Liudmila Molkova** 35:11 Sounds good. There is an action item to update, then, the gRPC boundaries, what we have in the refined metrics. Maybe, Matthew, could you add it to your refinement PR? Because it's next to the… metrics.
**Matthew Hensley** 35:31 Yep, should be able to do that.
**Liudmila Molkova** 35:34 Awesome, thank you.
Cool, we are way over time. I appreciate you staying longer.
And greatest question. See you, what, in 2 weeks?
Pardon?
**Madhav Bissa** 35:52 Yep, sounds good.
Thanks, everyone.
**Trask Stalnaker (Microsoft Corporation)** 35:54 Thanks. Bye.
**Madhav Bissa** 35:56 Maybe in the next one, we can just touch base upon the, KubeCon?
Agenda also, if you guys are going to still go ahead and announce.
Are you coming?
I… if… if you… if I have strong enough reason, I can convince someone to fund.
I'm not sure.
But it's our… I hold the deer.
When exactly is it? Is it on 12th of November?
**Liudmila Molkova** 36:28 8s to 12, I think, 9s to 12.
**Madhav Bissa** 36:32 9 to 12, so it will be difficult, because we also have GRP conference in India.
GRPC conference in India.
In the next week, so… But I…
**Liudmila Molkova** 36:42 Now it's… it's time to submit to the next KubeCon in Europe, it's closer to So…
**Madhav Bissa** 36:48 Yeah, that sounds correct. Okay, I'll submit something for that. Maybe… maybe around semantic conventions, let's say.
**Liudmila Molkova** 36:54 That, that would be cool.
**Madhav Bissa** 36:56 Okay, cool. Sounds good.
Alright, thanks, everyone.
**Liudmila Molkova** 37:01 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 37:01 I…
**Madhav Bissa** 37:02 Right?
