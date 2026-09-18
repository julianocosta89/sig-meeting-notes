SIG: OpenTelemetry Profiling
Date: 2026-09-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Felix Geisendörfer** 05:17 Warlock route today?
My colleague Nayef is gonna join a little bit later, so he's stuck in another meeting. But, yeah, since we're 5 minutes in, I would suggest to kick us off… I'm gonna copy the action items and share my screen.
Alright… Can everybody see my screen?
**Christos Kalkanis** 05:44 Yep.
**Felix Geisendörfer** 05:45 Okay, cool. Yeah, if it's too small, let me know. If not, I'll just proceed.
Okay, Alexey has an action item about… Orphan checker that needs review, is that still… Still needs to review, okay.
**Alexey Alexandrov** 06:03 I just added the fixed link.
**Felix Geisendörfer** 06:06 Okay.
**Alexey Alexandrov** 06:07 Yeah, but this basically adds when we check for… Orphans, and actually, when we also check for the validity of indices, of string indices, we… we previously wouldn't look into the attributes, the string indices.
**Felix Geisendörfer** 06:27 Hmm.
**Alexey Alexandrov** 06:28 So, The change adds those checks, and when we check for orphans, we also need to collect the string indices from attributes as well.
Working attributes is a bit… Funny, because they can be… as recursive as XML.
**Felix Geisendörfer** 06:58 Okay, cool. I'm definitely going to take a look until next meeting. Any more stuff you want to add, Sarah, or anybody else?
**Alexey Alexandrov** 07:08 Not from my side, I think, otherwise it's pretty straightforward.
**Felix Geisendörfer** 07:12 Okay, the sample type periods, I did get a chance to think about this a little bit today, so we could talk about that.
So, basically, you wrote this document, right? Yep. Where you summarized the current state of things, and sort of see open problems without, as far as I can tell, yet making a recommendation, right?
**Alexey Alexandrov** 07:38 Right. Yeah.
**Felix Geisendörfer** 07:40 Yeah, so my feedback there has been on, sort of, super period. I think this is one of the things where we need to figure out, making it mandatory or optional.
So… I don't know if we ever settled the debate about the use case for the period, but I think this is the most important thing.
Because I think there's, kind of two use cases.
One use case is to use a period to invert from sample values to weights, or vice versa.
And another use case is to treat it more like a description of the configuration of the profiler, but without necessarily expecting it to be detailed enough to perform an inverse.
**Alexey Alexandrov** 08:28 Whether it's… yeah, whether it's actually, like, whether it participates and how… Consumer weighs the data, or whether it's just some sort of, like, show somewhere in the summary information for the profile.
**Felix Geisendörfer** 08:43 Yeah.
So, my feeling is that inversion can be pretty complex. I mean, there's all kinds of different sampling algorithms with non-trivial inversion functions needed to get the actual weights from the values.
But maybe more annoyingly, there is, There are profilers that do adaptive sampling, that means they don't even have a fixed period. They change their period over time, and unless we are willing to maybe create one profile for every time the period change, which could be very small time windows.
I think we don't even necessarily get the choice of using period for, describing the inverse function, unless we want to make something really complicated.
Which I don't think we do. And the last point in favor of not trying to do the inverse with the periods is that A lot of profilers already do the inverse waiting for us. So all the Go profiles, except for one, but basically all the memory profiles emitted by Go are already inversed, where you get the weights and not the values. The CPU profile contains the weights for the samples. It also contains the values, there's two CPU profiles in the case of Go.
But you get to weights, so my preference would be to strongly steer towards saying profilers need to produce weights. I would even go so far to say that on the sample, we have a field called values. We should probably consider naming that weights instead, if we expect it to be the upscaled weights and not the values that were collected.
I'm curious if there's any quick thoughts on this.
**Frederic Branczyk (Dash0)** 10:33 I don't think I feel too strongly on weights versus values, but I think… What you said makes sense, but then we should also explicitly say that what we're seeing on the screen right now That we explicitly want option 1 and not option 2 or 3 ever to be produced by profilers.
Right? That's kind of the consequence, right? Because period has been kind of the thing that infers For timestamps, as well, the value.
**Felix Geisendörfer** 11:15 I wasn't quite, to the point where I was ready to talk about the consequences of our actions, but, I… I guess I would want to hear first if there's any, objection to the idea of not necessarily trying to use period for inversing, and then we could go into what you just said, Frederic, and try to work out what we need to change if we don't want period to work that way.
**Alexey Alexandrov** 11:44 I think, I think…
**Frederic Branczyk (Dash0)** 11:44 Not so good.
**Alexey Alexandrov** 11:46 I think, like, the only… and, I, I, in general, I… I agree with, with, with, with what you… with everything you're saying, Felix, and, yeah, the… but, yeah, the… the consequences is, I wonder if people… or, like, users of the Profile Prado, they would say, well, you special case the… you special case the case of one.
When the value is 1, then you allow to… Not capture those values with the timestamps, and then the profile is more compact.
But I have, like, fixed value of 10, why should this be different? But we could just say, like, well, yes, with special case, the value of 1, And everything else needs to be spelled out explicitly.
**Felix Geisendörfer** 12:32 So, I would not assume that if we just decide period is not for invoicing, that we don't make other changes to the other problems that we have, but I think it would inform us, sort of.
Which directions to go there.
So it sounds like we're all on board with trying to not make period arbitrarily complex to describe inverse function, especially for adaptive profiling and use cases like that. Instead, expect all-day profilers Oh, wow, what's that?
To, basically do the inverse before they produce the samples, right? Like, we're pretty much on board with that.
And I guess in this… the main question then is, that means.
we might not be able to, in some cases, know the values. So we have the weights now, but we don't know the values, because we don't have an inverse function. And I know one use case where it's useful to have the values, which is kind of judging whether or not you trust the statistical powers of a profile.
I'm not super concerned with this, because I think a lot of us think about continuous profiling, where we have plenty of samples and long time ranges, and if people zoom in too far, I think we all know how to do some UI UX to warn them that maybe it gets a little bit coarse-cranked in terms of resolution, but yeah, I'm wondering if anybody feels differently and wants strongly wants the user to have both weights and values, in which case we either need to provide both of them, or have a way to provide both of them, or makes the period more complex, but I think we already ruled out period more complex, so the question is, do we want Values in addition to weights as an optional.
element on the samples, for example. We can discuss how we would do it, but… I'm for no, just to be clear. I think it's too complex, and we don't gain enough from it, but…
**Christos Kalkanis** 14:27 Yeah, same for me, but my background is in continuous Profiling, I don't really have any particular insight regarding use cases that go beyond that.
**Felix Geisendörfer** 14:36 Yep.
My assumption is also a lot of people who are gonna use Profiling through OpenTelemetry are going to be interested in the continuous profiling use case. Or, if they're going to use it for development, if this ever, like, establishes itself as a development tool protocol, they can just crank up the sampling rate and not worry about the number of samples they collected. So I think it's… Practically a non-issue.
**Frederic Branczyk (Dash0)** 15:06 Yeah, I agree. I think there's sort of an interesting, Potential consequence from this, which is Does including the period value have… Any value at that point?
**Felix Geisendörfer** 15:22 Oh yeah, that opens up the door to a lot of questions, yes. I think we should do that, but if we have consensus here on, sort of, what we want the protocol to do and not do, I think I'll just capture that in the notes real quick, and then we can look at the other action items to do a little bit of time management, maybe we'll postpone an item of, like, deriving the next steps exactly, but, yeah, I just want to capture the high-level consensus here.
**Alexey Alexandrov** 15:45 Yeah, and related, briefly, for the sake of time management, but related, like, do we want to rename period to make the name somehow more obvious that it's that it's, that is not supposed to participate in the computations.
**Felix Geisendörfer** 16:03 Potentially, yes. Potentially rename it, remove it, maybe make it a semantic convention thing, rather than, like, a first-class field, like, all kinds of options, I think, should be on the table. But yeah, let's for now capture that we don't expect it to inverse.
**Frederic Branczyk (Dash0)** 16:17 I don't want to drag the topic further out, but I just… a last point on this. I do think there's some value to what Florian, I think, said last time, or the meeting before, where he said.
Period. Essentially… sorry, if sample type and unit and period type and unit are equal, then it means we're looking at the same kind of data that was obtained in the same way. And being able to determine that somehow is, I think, valuable. I'm not saying that it has to continue to be called period or whatever, but I think… being able to determine this from the profile is a valuable thing, and that is something we must, I think, retain in some shape or.
**Felix Geisendörfer** 16:58 Okay, to make that specific, I would appreciate a second to type notes before we keep going, but just to finish that thought up.
The example, I think, that you have in mind, or Florian had in mind, was in Go, for example, there is, analog space as a sample type, and there is a new space. So one is bytes allocated, one is bytes retained by the application at this point in time, LiveHeap.
And they both use the same sampling mechanism underneath. So they both have the same sampling rate for sampling allocations, and you're saying the value is in knowing that, that they both sort of come from the same mechanism? Is that the use case?
**Frederic Branczyk (Dash0)** 17:40 No, it was more like, so our use case here was that we have a… CPU profiler on, like, serverless, workloads that produce CPU nanoseconds.
And… that we can safely combine this data with, you know, profiling data obtained by the ePPF profiler, and that they, like.
Semantically make sense, together, even though they weren't… Collected by the identical profiler, but they were collected in the identical strategy, if that makes sense.
**Felix Geisendörfer** 18:23 But if you have a sample type and you inverse the values to weights, isn't that already a given?
like, if the sample type is CPU time in nanoseconds, and you inverse whatever sampling strategy you use to represent CPU in nanoseconds, then…
**Frederic Branczyk (Dash0)** 18:42 Right, but I'm saying we need to somehow contain what that sampling strategy is.
**Felix Geisendörfer** 18:49 I don't think we need to. I don't think you need to. You just need to make sure that it gets inversed into essentially the same weights, right?
Well, maybe I…
**Frederic Branczyk (Dash0)** 19:01 I think there… I think there can be two… I think there can be… two profiles that both have sample type CPU nanoseconds that reflect totally different things. Maybe CPU nanoseconds is a wrong, like, a bad example, but, like, space bytes?
I can think of, you know, several kinds of profilers that Record space bytes somehow, but may mean totally different things.
**Felix Geisendörfer** 19:31 I mean, I just gave an example of that, right? Like, you've got in-usepace and analog space in bytes for Go, and you would never try to merge them or combine them, because you know it's different sample types. One is in-usep, and one is analog space.
**Frederic Branczyk (Dash0)** 19:43 But I'm saying, I think I can come up with profiling data where the sample type is identical, but it's nonsensical to combine them.
**Felix Geisendörfer** 19:52 Okay, I would like you to do that and come up with one, because I don't want us to have, like, an abstract use case if we do end up making something complicated here. But if you can find one, I'm happy to look at it.
**Frederic Branczyk (Dash0)** 20:04 Yeah, yeah, I can… I can try to, put something together.
**Christos Kalkanis** 20:08 Frederic, can you add the, maybe those comments in the document that Alexey produced, or maybe a link to… if you create another document, add the link to Alexey's document, because I'm going to ask a few more people to take a look at Alexey's documents.
**Frederic Branczyk (Dash0)** 20:20 Yeah, I think it makes sense in that context, yeah.
**Alexey Alexandrov** 20:23 Yeah, or feel free to ask for added access, I'll just… I just…
**Frederic Branczyk (Dash0)** 20:27 Okay.
**Alexey Alexandrov** 20:28 Get the added access, you can add this section.
**Felix Geisendörfer** 21:47 This is summary, roughly.
Sound reasonable?
**Frederic Branczyk (Dash0)** 22:02 Nope.
**Felix Geisendörfer** 22:04 Okay, I think in that case, I mean, I'll leave more time at the end of the agenda today to, maybe if we have more time to keep chatting, but I think we now have enough restriction on the design space for somebody, and I would volunteer to do this, to sit down and propose what changes we could make, but as hinted in the discussions already, there's a few repercussions throughout the protocol that we need to consider. But yeah, maybe that work is better done offline now that we have at least Some part of the direction nailed down.
So yeah, if somebody would be able to add me an action item, that would be great.
Meanwhile, I'm gonna move on an item down here.
More time to discuss. Period.
Okay, do we have Florian here today?
Not, I can probably talk about this real quick, because I think I looked at this PR.
**Christos Kalkanis** 23:08 Yeah, I think Fluffler is out.
**Felix Geisendörfer** 23:10 Yeah, so I looked at this PR today, left a comment, but I didn't want to hold it up and, like, request changes, so I said yes, and apparently it was an order merge, which I regretted a little bit, because I might be a small… small issue here, but I think it's not that consequential. So yeah, I pinged Florian already on Slack to look at it, but I guess for now, this thing is merged.
That's my quick update here.
Note.
Okay, Nayef is gonna join later today, I don't know if he has already joined.
**Nayef Ghattas** 24:06 Yep, I've already…
**Felix Geisendörfer** 24:09 Alright, welcome to the party. Do you want to talk about, versioning?
**Nayef Ghattas** 24:14 Oh, so… I think the PR now has enough reviews from the SIG. There are very good comments in there, mostly small comments that I need to incorporate and update the spec to match, what the different reviewers said. So, yeah, thanks a lot for everyone for reviewing it.
And so I will try to incorporate those comments today or tomorrow, and I'll be joining the Spec SIG meeting next Tuesday to talk about this. I know that the specs tried to put this on their agenda last Tuesday, but it, but there wasn't enough time, so it got delayed to next week's agenda, but now it's one of the top items of next week's agenda.
**Felix Geisendörfer** 25:07 Cool, thank you so much for pushing this forward, and thank you everybody who refute.
That brings us to the next item. Christos, you wanna…
**Christos Kalkanis** 25:20 We've got.
**Felix Geisendörfer** 25:20 It seems.
**Christos Kalkanis** 25:21 Yeah, we… we can… we can skip this. It's been… it's been finished, yeah.
**Felix Geisendörfer** 25:24 Sweet. Then, thanks again to everybody who looked at that.
Tell me about, hotel environment variables.
**Tommy Reilly** 25:35 I reached out, but haven't heard anything back yet, so… Nothing.
to report.
**Nayef Ghattas** 25:42 So I think there was someone on our team who added a comment on the last SID meeting, which is that the profiler today already supports the environment variables. Like, it's already extracting hotel service name and hotel service… hotel resource attributes environment variable.
And, what it's trying to do, I believe, is prioritize process context. So if process context is available, the resource is going to be fetched from process context, and if process context is not available, we use the environment variables to define the resource.
**Frederic Branczyk (Dash0)** 26:19 Is that already how it works? Because I think two meetings ago, that was… the proposal, I believe, Is it how it works?
**Nayef Ghattas** 26:29 the process context PR was already merged, and the.
**Christos Kalkanis** 26:33 Yeah.
**Nayef Ghattas** 26:33 PR does it.
**Frederic Branczyk (Dash0)** 26:35 Okay.
**Christos Kalkanis** 26:36 Yeah, that's been merged for quite some time now, so that's not the case.
**Frederic Branczyk (Dash0)** 26:40 No, I mean the environment variable aspect, in particular, that, like, if the hotel service name environment variable is set, and no process context is available, do we already set the service.name in the profile? In the, like, what is it, resource attributes?
**Nayef Ghattas** 26:59 Yes.
**Frederic Branczyk (Dash0)** 26:59 From that? Okay, cool. Then, I guess…
**Tommy Reilly** 27:02 Great.
**Frederic Branczyk (Dash0)** 27:02 We're done.
**Felix Geisendörfer** 27:05 Well… So we've got this metadata action item here. There are some wrinkles, because there always are, but I would say there's at least a happy path that can work already.
**Frederic Branczyk (Dash0)** 27:18 ServiceName was the most important one for us, at least. This is why we brought up this topic in the first place.
**Felix Geisendörfer** 27:25 Yes, so if you're happy with relying on environment variables, you should be good. If you hope to get process context working properly, there's still some work to be done.
**Frederic Branczyk (Dash0)** 27:35 Am I happy with environment variables? No, but it's what we can give to customers today.
**Felix Geisendörfer** 27:41 Yeah, yeah, yeah, makes sense. Anyway, we've got another action item later, which I think will go more in depth on this right now. Yeah. So, let's keep going through these. Any more thoughts here? But I think we can table them, unless something urgent… Going once, going twice. Tommy has another PR for frame type for GPU.
The store that was merged. Yeah.
**Tommy Reilly** 28:07 Well, Florian did that, and it merged, so…
**Felix Geisendörfer** 28:15 Sweet.
It's funny how these PRs are sometimes more changelogged than anything else.
Oh, we're calling it CUDA, huh?
Interesting.
I guess that's fine. But our plan is to, like, have more disease, items if we support other GPUs, TPUs?
**Frederic Branczyk (Dash0)** 28:48 Unfortunately.
**Tommy Reilly** 28:48 Yeah, I mean…
**Frederic Branczyk (Dash0)** 28:49 CUDA binaries are incredibly non-ELF spec compliant, so, like, it is what it is anyways.
So, like, there's no, like, common thing that we could possibly put together here, so yes, the only thing to do is… do it per platform. Sorry, Tommy.
**Felix Geisendörfer** 29:07 Okay.
**Frederic Branczyk (Dash0)** 29:08 Definitely.
**Tommy Reilly** 29:08 Yeah, I was just gonna say, you know, if we added AMD Rakuten support, it would want to be different, and… Because of that and other reasons.
**Felix Geisendörfer** 29:19 Yeah, I mean, that's fine with me, I just found it a little curious. Cool, thanks for the insights into that.
All right, any, any more comments on this? If not, going once, going twice, I will move on.
**Tommy Reilly** 29:34 I was gonna ask one thing about…
**Felix Geisendörfer** 29:36 Go ahead.
**Tommy Reilly** 29:36 It's kind of a tangential thing, like… We have the frame type, but we also have the sample types. Is there some document or some part of the eBPF profile that's gonna… You know, document what existing Sample types exist and create consensus around those, or… Is that just… anything goes? Is that a… something that should be in the semantic conventions, maybe?
**Frederic Branczyk (Dash0)** 30:03 I think, Christos, you said you wanted to create a docker on this, no?
**Christos Kalkanis** 30:07 Yeah, so that would be part of the specification, so either it ends up in the protobuf definition, or, like, we have a dedicated specification page for the profiler, but I think so far we've been keeping almost everything at the protobuf definition, so maybe we should put those there as well.
Yeah, so, I mean, my question here is… because those mostly come from Piprov, right? And I'm not an expert on Piprov, like, I barely know what the set of acceptable values is over there.
like, if maybe Alexey can help us, like, if… Alexey, could you… is there a repository somewhere with a set that we can look at?
**Alexey Alexandrov** 30:49 I thought Florence and… Something, or… I think we've… we've been… we were discussing, pull requests that… I'm trying to find the link.
**Felix Geisendörfer** 31:04 So, one small thing to say there is maybe that PProf itself does not define any sample types, as far as I know, so we would only be looking at profilers that use PProf, and I guess we'd focus on open source profilers.
I would guess one of the most prominent ones are the profilers built into the Go runtime. I can easily provide all the sample types for that.
The question is, are there other… Popular profilers that we should… take a look at that emitProf. I think the answer is probably, and if I remember correctly, the… Mark Hansen, Mark something, had a Profiler encyclopedia page.
Mindset.
No.
**Alexey Alexandrov** 32:02 Oh, so sorry, this is ish, this is an issue,
**Felix Geisendörfer** 32:06 one.
Okay, here's a list of profilers that emit PPROTH, apparently.
That we could look at.
**Alexey Alexandrov** 32:49 Okay, this is the pull request.
**Christos Kalkanis** 33:02 Yeah, there's a link further down, so play an OpenTPR against the specification, so he has a markdown document in there.
**Felix Geisendörfer** 33:32 Okay, yeah, so we should probably review and… Add to this, as needed.
I think I did that as well at some point, but I think I need to take another look.
**Alexey Alexandrov** 33:56 But, the question about, sample type versus frame type, I… like, the granularity is different, right? Because you could have a, the frame type is per frame in the stack, and you could have… What sample type is… For the whole profile, so it's kind of… the sample type is a… Is a column… of the data, but then each row has the stack associated with it, and then you can have a… you could have a stack that has some CUDA frames, and then some host frames that could be Python or C++, and so on, so… The question, like, what is the difference? It, confused me a little, because the cardinal… kind of like the granularity is different, if that makes sense.
**Felix Geisendörfer** 34:56 I think it's… Tommy, do you have any thoughts on this, or…
**Tommy Reilly** 34:59 Yeah, I mean, we break out the GPU profilers as a separate sample type, just because it's kind of its… its own thing, and the, you know, the stack.
is not a… real stack.
You know, we invent this… stack where we glue together the GPU bits with the CPU stack.
So… I think that warrants a different sample type.
**Felix Geisendörfer** 35:27 I… yeah, I would say that… If you have a… profile where all the frames are expected to be the same frame type, which I think is what you're describing, then maybe the answer is you could omit the frame type.
**Tommy Reilly** 35:42 Well, it's… the… All the application frames are, you know, whatever they are, native.
iPhone, and then…
**Felix Geisendörfer** 35:52 So you have.
**Tommy Reilly** 35:52 Sweet.
**Felix Geisendörfer** 35:52 the same profile in.
**Tommy Reilly** 35:54 Yeah, the GPU CUDA frame is just the last one on the stack, it's the leaf frame.
**Jonathan Halliday (IBM)** 36:01 But even with something like Python, you've got code that is Python, and then you've got C code that Python is calling.
And those are not the same frame type.
Python is not C.
You get that in Java as well. You've got a stack that's Java calling down into some native library.
**Alexey Alexandrov** 36:30 I genuinely view frame type as more of, kind of like a visualization thing, that maybe… Certain frame times are colored differently when you view the profile, or maybe there's a checkbox somewhere, like, filter out Frames of this certain kind.
But I wouldn't expect FrameType to kind of, like, seriously guide the profile processing, or control the profile processing. Maybe there could be some symbolization aspects, like, for example, oh, if it's, like, if it's… If it's GPU framed, then don't even try to symbolize it, but… even there, I think the semantics are usually, do I have a linker build ID, or I… or I don't have a linear build ID, not that… like, for these specific properties of a frame, I will do symbolize versus not.
**Tommy Reilly** 37:21 Yeah, just the way it works in our profiler is that the… there's not really a build ID for the… for the Cubans that… the CUDA frame refers to, it's this weird… you know, CRC that's based on how the CUDA profiler works.
And the visualization aspect is roughly the same as the CPU profile, but we do have all this extra context that, especially in the context of PC sampling, which includes You know, an instruction pneumonic, and this whole stall reason.
attributes, things.
**Felix Geisendörfer** 38:20 Do you think there is some problem with frame types and sample types right now where we need to clarify in the protocol, or…
**Tommy Reilly** 38:27 I think I'll just add a comment to, florian's… spec profiles and…
**Felix Geisendörfer** 38:36 Oh, okay, okay.
**Tommy Reilly** 38:37 People have thoughts, they can chime in there.
**Felix Geisendörfer** 38:39 Okay, that sounds great.
Cool. Then my question is, does anybody… Anything to add here? Going once, going twice… If not, we would be next, with God and Evo, but I don't know, do we have some here today?
Or Jonathan's on this as well.
**Jonathan Halliday (IBM)** 39:16 I don't think that's progressed at all.
**Felix Geisendörfer** 39:20 Okay.
Is it just a matter of the people involved finding more time, or is…
**Jonathan Halliday (IBM)** 39:28 Yeah, it's not blocked, it's just a case of getting everyone together.
Talking about it.
**Felix Geisendörfer** 39:34 Okay.
Okay, sounds good.
Yeah, I had a… this was not supposed to be an action, was it supposed to be an action item?
Yeah, but maybe you can talk about it, and maybe I can make this more explicit.
right now, in profile time Unix Nano, which is saying it's the timestamp of the collection of the profile, which is a little ambiguous in terms of, like, this is when we… started the Profiling window? Is it when we finished it? Is it when we actually exported the data? Like, as in collection can be quite misinterpreted? And I think what it refers to is the start of the profile, so I… actually have a patch, which I didn't place a PR for today yet, but I'll send a patch, basically, unless anybody disagrees with that.
Let me… Give yourself a reminder.
Okay, then we are… To the next point, Nayef threat context implementation in the eBPF Profiler.
**Nayef Ghattas** 41:06 Yes, so I think, the threat context implementation in the eBPF Profiler was originally one big PR, and it got split to multiple, smaller PRs based on feedback. We already got a first round of review on those PRs, and we addressed, the feedback and asked a couple of questions. So I think we'd appreciate, more reviews on these PRs to be able to, move forward with, thread context implementation in the eBPF profile.
**Felix Geisendörfer** 41:50 Okay, then syncs… The work on this, and everybody who's reviewed so far?
And… Yeah, if anybody here has time to review that, that'd be fantastic.
Mmm… Okay, there's no other thoughts, alexey has an item.
**Alexey Alexandrov** 42:15 Yeah, this was when I was adding string index handling. I had to remind myself, like, oh, we're still using key value and unit, the… we're still not using the key value, and then, like, oh, this is because we need the unit.
And then I recall, like, we have these two documents, and I was curious… Top.
Bing ourselves, what's the… what's the plan there? Because I assume it's one of the better items, we need to resolve that before we can… Declare.
**Felix Geisendörfer** 42:46 My recollection is that this got resolved, with the answer being that the rest of OTL doesn't care about units, and we keep our weird key value and unit.
**Alexey Alexandrov** 42:58 Oh, okay, so…
**Felix Geisendörfer** 42:59 Does somebody else remember this, or am I, becoming a language model?
**Alexey Alexandrov** 43:06 I'm trying to search for key value and unit in the notes.
**Felix Geisendörfer** 43:14 We also had something on the roadmap for this one.
**Nayef Ghattas** 43:18 I think we said we're going to keep key value and unit?
**Felix Geisendörfer** 43:22 Yeah, that's what I remember as well. Yeah, this is basically this issue, I think.
And here is C.
**Alexey Alexandrov** 43:33 Okay.
**Felix Geisendörfer** 43:34 unique to a profiling signal, which I don't know why we agreed on that, but I guess it was in the spec sick.
People of compatibility and…
**Alexey Alexandrov** 43:44 Okay, sounds good.
**Felix Geisendörfer** 43:48 I don't know, a CEM dash is here, I don't know what happened there.
Who knows? But yeah, I think for now that at least we've gotten… I think one of the major issues here was the, the blocker from Bogdan who was very unhappy with it, and since this issue has been resolved for… over a month now, two months now, and Bogdan has not come back. We… Or probably okay to proceed with what we're doing.
**Alexey Alexandrov** 44:14 Do you mind linking this comment in the meeting?
**Felix Geisendörfer** 44:33 Okay.
Cool. Any other… So it's here. If not, I'm gonna… Move us on to the next item. Alexey, another item from you.
**Alexey Alexandrov** 44:47 Yeah, when I was looking at, key value, because in key value, we do have key string index, I think this is for resource, for… we added this for resource… for compact resource attributes and coding.
And we say is there something like key string index must not be used if… must not be set if key is used, but then, like, we don't kind of… but this is not an optional field, so as Jonathan mentions here, basically our zero index convention applies.
But if you just look at common.proto, it's not very obvious, so maybe we can… maybe we can clarify that, or link.
To, wherever the convention is documented.
It's just, like, in the local context, it's not super obvious what unset means.
**Felix Geisendörfer** 45:37 I mean… in protobufs, there's no such thing as unsat, right? Like, every field gets its default value, similar to the GoType system, so a… In Tetra field would get 0 always assigned as a value in protobuffer.
**Alexey Alexandrov** 45:53 Right.
Right, but… but in… in this proto, we… we kind of, like, we describe one of… semantics, basically. You either have key, or you have key string index.
And so, if we say…
**Felix Geisendörfer** 46:06 I agree, like, the wording is wrong. We need to word this as either being not zero, the value, But… Yeah, but we can't use the term set, because that term doesn't make any sense.
**Alexey Alexandrov** 46:22 And, and Jonathan seems to propose something like must be zero if key is used.
And I think…
**Felix Geisendörfer** 46:30 I agree.
**Alexey Alexandrov** 46:31 that… I think that would be clearer. I can… I can make the change if… if it all makes sense.
**Felix Geisendörfer** 46:38 That would be great.
Okay, can you add an action item for yourself?
**Alexey Alexandrov** 46:45 Yep.
**Felix Geisendörfer** 46:47 Sweet.
Okay, anybody have more thoughts on this? Going once, going twice?
If not, Scott is not here, but has… asked Nayef to take off over a section item, I don't know if you're prepared to do that.
**Nayef Ghattas** 47:08 Yeah, I think it was, he mostly wanted to raise awareness on, the memory profiling work, so I think we have two first PRs who emerged in the profile log.
And we were currently, blocked on this one, re-sync Probes on MMAP events, because there's a question of architecture we need to resolve in the EPF Profiler on how do we deal with, dynamic libraries, being loaded at runtime, and being able to detect those MMAP events for memory profiles, even if we didn't detect a CPU sample.
on that same library, to be able to have a reliable profiling. So there's a discussion there, I think Scott has addressed all feedback, but we need more eyes to ensure that everyone is aligned with the solution.
**Felix Geisendörfer** 48:26 Okay.
If anybody has immediate thoughts about this, please share them.
**Christos Kalkanis** 48:33 I'll just ask for more people to start maybe taking a look at pull requests like this, which have an architectural component. They're not just implementation requests for the ADPF Profiling.
So I helped push the first two PRs through.
Yeah, that… I spent significant time on those first two PRs, but then… Yeah, I couldn't spend any time on profiling for the last two and a half weeks. Essentially, nobody pays me to do profiling anymore. I switch to security. So, any work I do on profiling is because of the goodwill of Elastic.
But it's not something they're prioritizing.
And that's going to continue for the foreseeable future for me, unfortunately.
So please, yeah, the more eyes we have, the better, and the more people that start reviewing pull requests in the VPF profile, especially pull requests such as this.
the better off you're going to be. So, that said, I will, yeah, I will find the time to… to continue with memory profiling.
One issue here is that now we're getting into discussions that… That's the rest of the profiler as well. For example, the profits manager has become quite complex.
Because almost every information flow goes through it in some way. Roger has created an alternative where he refactors the process manager to be more distributed in its responsibilities.
And Timo, Which is essentially, right now, the main reviewer for the BPA Profile. He does most of the work in terms of reviews.
he had some, feedback regarding sports, work, and Rosa's work, so it's like we're tangled up, and, if we make a decision, like, if the two of us make a decision, let's say me and Florian, and Timo is not involved in that at all, that increases the probability that, you know, we messed up TPR, and then later, Timo will figure out that this happened, maybe he's not gonna like some aspects of that, and we have friction, the same questions keep coming up, and so on, so… I guess… to… to make faster progress here. They keep… reviewers need to be involved in every PR request, so that means Timo has to be involved, right? So, feel free to reach out to him directly to pull him into reviews.
And, yeah, the more eyes we have, the more new people that we can get to… the more stakeholders we can get to review these pull requests, the better we are, all of us.
**Felix Geisendörfer** 51:08 Thank you, that makes sense.
Since we have some other people potentially capable here, I don't know, Frederic, Tommy, if… polar signals, or dash zero now has any bandwidth to look in this. I would imagine that memory Profiling could be of quite some interest to you all as well.
Sorry for calling you out, but figured I should take a shot.
**Tommy Reilly** 51:31 Yeah, we definitely… Are interested in that.
**Felix Geisendörfer** 51:37 Cool, then maybe you all can discuss internally, and if you can make some resources available, that'd be amazing.
Awesome.
Cool. Any more thoughts on this?
not… Thanks to everybody working on this, and also special thanks, Christos for putting time into it when it's not part of your, regular salaried activities anymore, it's really appreciated. And… I will move us on to the next action item, metadata enrichment from Nayef.
**Nayef Ghattas** 52:28 Yeah, and I think this is, sort of closely related with the previous one on the process manager becoming, very complex.
and the different proposals that were brought up to make it simpler. So, one manifestation of that is that we need to add metadata To the profiles that are based either on the process, or on the mapping, or on the sample.
And for metadata that is based on the process. Right now, each time this is done, it's done in an ad hoc fashion inside the process manager, by adding code in specific places, and this doesn't scale very well.
But also, the proposals that were done Including our job's proposal, doesn't necessarily cover all the enrichment use cases that we have.
And that we need to add.
Because the APIs may be lacking, some, some flexibility to implement some of the features we need. So the goal of that document is to list all the use cases that we have for process enrichment. I think most of them are not conversial, like process name, executable path, environment variable, cgroup path, main executable, build ID, process context, and the runtime name and version that we discussed, I think, 2-6 weeks ago.
That would help, be able to compare profiles across different content versions.
And there's a whole section about a proposed direction, to have a policy inside the Profiler on which attributes we support natively in Profiler and we add, which ones would make sense to implement in a processor.
Later on, what representation do we use for those attributes? Discuss a bit lifecycle and precedence, and what need do we have for extensibility?
I've already gotten feedback from Roger and Florian, and I think I applied every feedback that I received. I tried to get Timo involved by pinging him on Slack.
But I did not get the impression that he has reviewed that document.
So, yeah, I'm not sure what we can do, to move forward.
I do view that document as a problem statement that we sort of all need to agree on that this is the basic functionality we need to provide before we discuss the different implementations and possible implementations for the process manager, and also for general, like, attribute enrichment in the process manager.
**Christos Kalkanis** 55:18 Okay, so that sounds great to me. By the way, Nayef, thanks for all the work you've been doing, yeah, for the last couple of months. Those documents that centralized information that act as rough design documents are great, because, you know, if you didn't do it, I guess nobody else would have.
So, Timo is best when we involve him at the implementation stage. I think that's where his feedback would be most valuable. So, for this document, yeah, I think we can… move ahead if he's not responsive. Typically, I think he spends either two days of the week looking at profiling.
He's not a full-time employee on Profiling, he's a contractor.
So… Okay, let's get, Ideally, more people from the SIG to look at it, Felix, if you can look at it, if someone… Has additional feedback?
I would… I would look at it as well.
**Felix Geisendörfer** 56:18 Yeah, I have refuted with NF, and I basically support it at this point, but if needed, I can leave some comments to make it more clear.
**Christos Kalkanis** 56:42 Okay, so Nayef, let's say we all agree on this, that these are the… the set of attributes that we want? What's the next step?
**Nayef Ghattas** 56:51 I think we need to review the existing proposals, because there are multiple proposals around the process manager and attribute enrichment.
Some of them do… I think there was a proposal that implements most of the requirements. We… we need to weigh off the different trade-offs of each proposal and… and try to figure out a direction to move forward for the implementation.
**Christos Kalkanis** 57:19 Okay, so if I remember correctly, Florian has a proposal, like, an implementation proposal, then Roger came up with his process manager.
refactoring?
**Nayef Ghattas** 57:30 And Nicola has, from our side, also has a proposal.
**Christos Kalkanis** 57:36 Okay.
All right, let's… let's try to talk about the problem, like, one piece at a time. Let's start with getting consents. I don't think we need Timo for the first, like, for this document. We can… like, I'll look at it, I'll sign up on it. I didn't see anything controversial in that so far. I mean, it looks good to me.
And then, yeah, we can start talking about possible implementations, weighing the trade-offs, and that's where I will try to get him involved, because he should be involved.
**Nayef Ghattas** 58:05 Okay, makes sense. Thanks a lot.
**Felix Geisendörfer** 58:14 Okay?
Cool, thank you so much for, your help on this, Christos.
And of course, Tenaya for putting it together. Any more thoughts on this?
I mean, once… doing twice… And… We had this item here, but given that we have less than 2 minutes left in our allocated time, I would propose that we Conclude today's meeting, and continue the discussions on period, and what we'll do now that we sort of aligned on it, async, in… for example, Alexey's document, I think, is a good place to continue the discussion.
And thank you everybody again for your time to attend, and all the work done in between the meetings. Yeah, have a nice local time. See you all.
