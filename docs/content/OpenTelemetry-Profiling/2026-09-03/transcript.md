SIG: OpenTelemetry Profiling
Date: 2026-09-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Scott Gerring 00:02:24 Hello?
Florian Lehner 00:02:30 Hello.
Scott Gerring 00:02:31 Anyone on holidays, Florian?
Florian Lehner 00:02:33 I am.
Scott Gerring 00:02:35 You're not doing a very good job of showing it.
Florian Lehner 00:02:41 Yes and no, yes and no.
Scott Gerring 00:02:45 Profiling SIG appreciates your commitment. The Profiling SIG appreciates your commitment.
Florian Lehner 00:02:51 No luck.
I have to take a break, I'm waiting for my dishwasher to finish, to go for a run, so… You're right.
Scott Gerring 00:03:00 Nice.
How's unemployment treating you?
Florian Lehner 00:03:32 Officially, I'm still on PTO.
Scott Gerring 00:03:35 Oh, fair enough.
Florian Lehner 00:03:36 So, I… I'm on PTO for… Until 22nd, I think, of September, and only after 22nd of September, I'm unemployed, officially.
Scott Gerring 00:03:47 Okay, cool.
Hey, Felix.
Felix Geisendörfer 00:03:52 Hello?
Right, we are 5 minutes in, so kick us off. Let me find the meeting notes and share my screen.
Hey, can you all see my screen?
Excellent.
So, we have a few agenda items, that I'll walk us through. As usual, we'll start with reviewing previous action items. Is Alexey here today, or will he maybe turn later?
It's not yet, so I'll put his stuff at the bottom.
Okay, then Florian has… something to say, or give updates on CIC Profiling ProfCheck.
Florian Lehner 00:07:42 No big updates on my side, just asking for, review and feedback.
Felix Geisendörfer 00:07:56 So anybody who has a chance to look at it, please take a look.
then NAF has opened the PR, on including versions in the profile payload, I did review that one earlier. I'm not sure if a lot of people have seen it. Oh, this looks like it has a lot of approvals.
Alexey has some open comments.
Okay, yeah, seems like this is on the way and just needs the conversations resolved, but it seems like we are largely aligned there. Does anybody want to Go into details or ask questions while we're here.
Florian Lehner 00:08:52 Maybe a question, do we have a related PR for this on the Auto Collector side?
That sets this field.
Felix Geisendörfer 00:09:01 I think not. I think the… specifically the PR says collector changes will follow separately.
Yep.
Florian Lehner 00:09:11 Okay, yeah, I'm just wondering if there was already a draft or something.
Felix Geisendörfer 00:09:15 Not yet. I think the thing is that we lance this and then we do the collector things, but arguably, if people feel like we should have a collector implementation to show that it works end-to-end, we could also do that.
Florian Lehner 00:09:29 No, no, it's just out of curios.
Totally fine.
Felix Geisendörfer 00:09:33 Oops, it's not coming to… Okay, yeah.
Yeah, so I think maybe one… the only thing worse from my end on this was when Naev originally raised it, he was suggesting we bump the, sort of.
development version number once for every protobuf release, it has a breaking change, but I suggested to do it once every time we merge a change to the Profile's proto files.
Because it's just easier to manage in general, and also less likely that somebody forgets it during the release process. But this might lead to the fact that we have two version bumps in… one, protobuf release, but I think that's totally fine, because… If you… if you support version 5, then you also support version 4 and 3, even if they might be, like, in the same major Proto release.
Okay, then, if there's nothing else here, do we have Christos to talk about?
the OpenPR, or is that still pending refuse?
Oh, it's still pending refuse, I guess.
Take a note Yeah, now we're at Alexey's stuff. I don't think if he's here, nobody else has probably updates.
I know there were some Slack conversations about him starting a document, I don't know where that landed, if anybody can speak to that.
Florian Lehner 00:11:29 I think there was a PR by Frederick?
And, On, on the… Sander type and period type con, in the portal.
Felix Geisendörfer 00:11:42 wasn't.
Florian Lehner 00:11:43 but I think there are… I left a question, and I think there was never a follow-up.
Let me quickly check, make monster duration.
Yeah, I think it's… to swarm.
You know, I was worried about the wording, that's why I raised the question.
It may be preferable to set, something.
Sounds like, not… specific, enough that it should end up in the specification and in the protocol, I would say.
Felix Geisendörfer 00:12:38 And I guess I should also review this one.
Okay, so yeah, maybe ping Frederick to get an answer on this, but yeah, it's just been 3 days, so yeah, if he doesn't reply, then maybe follow up.
And I'll try to take a look at this one as well.
Tommy Reilly 00:12:55 I can mention it to him, too, the next time I talk to him.
Felix Geisendörfer 00:12:58 Oh yeah, that's great, yeah. You should be close to him.
Cool. Then, speaking of Tommy, I guess we are next with your agenda item, Do you want to talk about this?
Tommy Reilly 00:13:13 Yeah, this just came up with some, you know, as we were looking at the, The process context stuff, you know, it seems like the nice thing about that is that, you know, that stuff's gonna work out of the box if, you know, somebody has the right… you know, SDK or whatever, and they have all the… all the P data in there, process context, it'll just flow through. And so we were wondering, why don't we do something like that for the environment variables that people are already using today? So this could just be, like, you know, we have environment variable support, but, like, could we… by default, support some of the key, hotel environment variables, so those flow through. I don't know if this has come up before, but…
Scott Gerring 00:13:56 I guess the hedge here is that it's gonna take… or that we expect it'll take a while for process context to end up on the SDK side of things.
Is that right?
Tommy Reilly 00:14:07 Yes, yeah, so, like, can we do something out of the box so that that stuff just works instead of… People having to type in all these environment variables.
If people seem amenable to that, we can… throw our PR for discussion.
Felix Geisendörfer 00:14:28 So, are you suggesting that people currently configure OTEL applications by setting these environment variables, and we could just pick them up without process context being in those SDKs?
Tommy Reilly 00:14:39 Yeah.
Felix Geisendörfer 00:14:40 Okay, I guess the risk there, but somebody correct me who knows more about this, is that the environment variable, is that a guaranteed override, or would code configuration or configuration files take precedence?
Tommy Reilly 00:14:55 That's a good question. I would think that the… anything the code did.
would override, but I'm not familiar with.
Scott Gerring 00:15:04 But it's…
Tommy Reilly 00:15:05 How that works.
Scott Gerring 00:15:06 That is for sure how it works, I'm the only one I know, which is Rust.
Felix Geisendörfer 00:15:14 So, I guess what that means is… We are trading the current situation where we get nothing, we don't know the service name for getting a service name, but in some cases, it could be the wrong service name.
Tommy Reilly 00:15:28 Right.
Felix Geisendörfer 00:15:29 So, I… think… I think getting something is better than nothing?
So I would be in favor of exposing it and enabling by default, but there should probably be a way to opt out of this, and the eBP profiler would be my gut feeling here, and once we have process contacts, that should obviously take precedence, like, when we determine what service name a process has in the profiler.
Tommy Reilly 00:15:53 So, meaning those just take precedence?
still support the environment variables, and if the process context doesn't have those names, then we allow the environment variables to still flow through, is that what you mean?
Felix Geisendörfer 00:16:07 So, what I mean is, I would expect the process context, once it lands in the SDKs, to be hooked up into everything, so it understands the environment variables, the configuration files, the encode configuration, and it will know the result service name as determined by the hotel SDK, and actually put that in the process context. In other words, CBPF Profiler should always check Does this process expose process context if he has to use the service name and everything from there, and accept that as a source of truth, but if there's no process context.
Then the environment variables are the next fallback.
It's so…
Tommy Reilly 00:16:40 So the existence of the process context will kind of turn off the bid variable thing, or… Yes. It will own everything, and nothing else will be applied.
Felix Geisendörfer 00:16:49 that's… that's my initial suggestion, I think that makes the most sense, but I… we could work out the details in a PR, which would just be…
Tommy Reilly 00:16:57 Yeah, that makes sense.
Felix Geisendörfer 00:16:58 Yes.
Florian Lehner 00:17:23 I might be wrong, but, I think, please, Rafari, correct me in the… In terms of process context, the service name is just a resource.
Whether, where the service name is, coming from. So, if it's hard-coded in the application, if it's coming from an environment variable, it's just a resource that is shared via the process context.
So there's no special handling for this, it's just… Information that is shared.
Felix Geisendörfer 00:17:54 Right, but when there's no process context, then there's nothing, and then the eBPF profiler could just look, hey, is there an hotel service name environment variable set for this process, and if yes, fall back to that as a service name. So basically, yes, it would make a guess for what the resource attribute should be on that process.
Florian Lehner 00:18:12 Yeah, makes sense. But I think we just should be careful on special handling all these kind of stuff, so… If someone doesn't communicate something, we should not have special cases for everything, so, like, have you exposed this or that information? And Oprah Profiling can do and see a lot of stuff, but I'm always questioning, do it needs to… Extract everything.
So, it doesn't… it does have, info, access to the… via the proc file system, to the environment variables of the process, so we can, can use it. But… should this be extended then to, I don't know, container ID information, or, OICD information that is exposed in, in other, in… in the same way properly, and the eBPF profile could also.
extracted, so I think there's a fine, fine grade between, Allowing everything versus restricting it.
And, yeah, sure, in the first place, we should, auto context… auto process context should… Provide as much information as possible, but if the application decides to provide none, I think it's hard to… to everything.
Does this make sense in some way?
Tommy Reilly 00:19:48 Sorry, go ahead. Are you saying that these should be, like, opt-in, or that this should be configured, like, outside or above the level of the eBPF Profiling?
Because you can already do it, right? From… I mean, at least, you know, you can provide these environment variables manually. The question is, is it worth doing it?
Florian Lehner 00:20:15 Yeah, I think that's… that's the question. EBFF Profiling could do a lot of stuff, like also extracting container environments information, but, I think it's not… the first purpose of the EPF Profiler. So, if there is some kind of extension mechanism to say, hey, I'm really curious about something like this, then please go, yeah, makes sense.
That it can hook in, but, I think it should not be the first job, or the chop in the… of the eBPF profile in the first place.
Felix Geisendörfer 00:20:51 I suppose it's what your view is on what CPP Profiling job should be. Like, I think one view is that it's just, hey, you collect CPU samples and not much more, and another job is like, hey, you provide a user experience around profiling stuff.
That is really nice for people to use and doesn't require them to configure 20 different components and settings.
I'm more in the latter camp, to be very clear, but I think we should have discussion around that, yeah.
Florian Lehner 00:21:20 Yeah, I think… I think, Naive, did set up a document about, resource.
metadata, or the process metadata, sorry. And there, the same question did come up, what are attributes that the UPF Profiler should extract?
And, something like the service name and container ID totally makes sense, as these are essential for most parts.
But building on top of that, should we continue adding more, or should we, let other, attributes Do the job.
Roger Coll 00:22:07 Yeah, I think that maybe it's a question more for the specification's sake.
Because, let's say that those environment variables are defined for the SDKs at the moment documentation.
And I was wondering, for example, now in… in other, let's say, receivers, for example, the host metric receiver for the process metrics, we are not extracting these environment variables at the moment, neither.
S… And it would be nice, from a user experience, also to extract it there.
So, yeah, maybe we can ask which… Specific consumers should extract those.
Felix Geisendörfer 00:23:15 So, Raja, I want to make sure I understood all of what you said, because I was typing and I don't think I captured all of it.
you're saying the environment variables are currently just implementation details of the SDKs and not part of the… the spec?
You're muted.
Roger Coll 00:23:33 So, no, they are… so they are part of the spec, but they are just referenced on the SDKs.
Documentation at the moment.
So, basically, those are defined, or… The documentation says that they must be extracted from the SDKs in order to initialize those values.
But it doesn't tell, let's say, external observers of this.
processor or SDKs, if they should also, gather it and use it.
That's my, maybe, clarification.
Felix Geisendörfer 00:24:11 Okay, so in other words, you would say it would be more clear if we actually raised this with the spec sig and maybe made a change to the specs that says, like, these environment variables are not just for the SDKs to pick up as a configuration signal, but also for outside observers.
Roger Coll 00:24:24 Yeah, exactly, exactly. Or… or maybe the decision is not, and it's clear, and we cannot, because maybe the SDKs can change it in runtime, and we should just use the process context. But I think if there's a clarification, other consumers can benefit, like, the host metric receiver, as I was saying, on other, other 6.
Felix Geisendörfer 00:24:49 How would the host metric receiver pick up these environment variables?
Roger Coll 00:24:55 It, it, they, it is not picking them at the moment.
Felix Geisendörfer 00:24:59 But how would it? How would it? It can't, right?
Roger Coll 00:25:02 Well, the same way as, as I guess we would do on DBP Profilinger, just reading the.
Felix Geisendörfer 00:25:08 Oh, wait, wait, does the host metric, receiver create metrics for every process? For every pit? Yeah. Okay, okay.
I would say, yeah, it would be good to raise this with the spec sake, and I think my proposal to them would be, like, this would be a fallback when process context is not available, but the spec should say, like, always read process context if it's available, you said.
If it's not, you can fall back to the environment variables as a best effort. We should probably require something that indicates when this happens, because again, they could be wrong, so I think it would be nice if we had maybe an additional attribute that would be added. In this case, it declares the source of the service name.
Which is a little annoying, but I think it's good to have that, because otherwise a lot of confusion could be created in some environments.
Tommy Reilly 00:26:16 Alright, so who's gonna reach out to the, Spec SIG? Is that, something I should do, or… I can figure that.
Felix Geisendörfer 00:26:21 If you'd be willing to do that, that'd be fantastic, if you would be willing to take an action item.
And I'm just writing down what I just said.
Tommy Reilly 00:27:24 So in this case, that source attribute would say something like eBPF Profiler or something like that.
Felix Geisendörfer 00:27:31 No, I think the source would just be process context, right? Because we picked up the service name from the process context. I guess… the, the question, yeah, so process, context, or environment.
One question is, do we want to do this for every resource attribute that we somehow magically pick up? I think that would get a little annoying, so I think we should propose a mechanism where either all the attributes are picked up from process context, or there's a fallback to the environment, but not, like, a little bit of process context, a little bit of environment. I think that would be messy.
Yeah, so, Tommy, if this makes sense to you and nobody else in the CAIC fields differently, I think it would be awesome if you could take that to the specs and see what CAIC about it.
Tommy Reilly 00:28:42 Cool, I can do that.
Felix Geisendörfer 00:28:44 Cool, thank you so much.
Yeah, will you or somebody else add an action item on top? That'd be great.
Okay, any more thoughts on this? Going once, going twice?
And moving on, you have another one about Kakuda and Tommy.
Tommy Reilly 00:29:21 Yeah, so these… it's just, we have… some… Sample… types, and I guess those are still kind of TBD.
from Alexey, so we can skip those, but we also have, a special frame type for CUDA profiling, that just lets the backend know that it has to resolve symbols differently than a normal kind of ELF binary.
And should we be working to get those into the… The profile… Spec that covers these frame types.
Is that just opening a PR over there, or how does that work?
Felix Geisendörfer 00:30:06 Yeah, I think the only argument against this that I could see is that this hasn't landed in the upstream eBPF profiler yet, but I think if you all are working towards that, then my answer is absolutely yes.
If not, my only answer might be maybe later, but, like, I'm generally in favor of this.
Tommy Reilly 00:30:24 Yeah, I mean, our plan is to land them in the upstream Profiler, and we are currently working on Re-implementing that stuff on top of the new custom probe stuff.
But that is, in process.
Florian Lehner 00:30:47 Did you see the issue that was created, I think, 2 days, 3 days ago, about the request of our GPU Profiling in eBPI Profiler?
Tommy Reilly 00:30:56 I did not. Thank you for mentioning it.
Florian Lehner 00:30:59 maybe it makes sense to leave a comment about your plan and what you're doing. I think I would be super interested. I didn't see your, your, agenda item when I created the PR, but, I think, the agenda item I have at the bottom, is very related to this, where I specify some kind of sample, or list known sample types for for emitted profiles. I did not include GPU yet, but I think it makes sense to add GPU at some point as known values.
Yeah, same for, the frame types. I think frame types, we already have Lua, JIT, Frame types, and in the semantic conventions, but, no implementation for it yet.
So, I think it's fine to add, a frame type for CUDA, I don't know if it makes sense to add a specific CUDA frame type.
And also have, maybe… I think that… JAX is the other format.
And maybe a TPU format, so, I think there are various options.
Can be added at some point.
Alexey?
Alexey Alexandrov 00:32:34 For sample types, is there… was there a discussion in the chat or somewhere, or is there an issue? There are no links in this, in this… in this section, so I'm just curious to… to learn a bit more. I think for sample types, one question is what kind of… what kinds of met… kind of metrics That is, I'm mostly curious to confirm that this, like, either cumulative metric or instantaneous metrics.
Because sometimes it's… sometimes, like, when… It seems like it can be a simple type, but then, like, oh, oh, maybe it actually, A category value that can be Can be a, can be an attribute, so just… I was just curious to look at some examples.
Tommy Reilly 00:33:22 Yeah, I don't have any on hand, but, you know, what we do is we have… two different, types of sample streams that look just like, you know, CPU samples, but, in one case, it's kind of just raw kernel timings, that show how long a particular GPU kernel, took, and in the other case, it's this kind of richer, PC sampling data that shows, You know, the… the Cupti PC sampling data that NVIDIA GPUs have, which gives you, kind of.
More down to the actual instruction level.
Profiling.
Alexey Alexandrov 00:34:03 So the unit would be, kind of, GPU seconds, basically?
Tommy Reilly 00:34:08 for, for the PC sampling, we derive the time unit from the, sampling rate and the Ed.
the, you know, cycle speed of the GPU. And for the kernel, it's just, wall time, kind of.
Alexey Alexandrov 00:34:30 Okay.
So sounds like seconds in GPU circles.
Tommy Reilly 00:34:39 Yeah.
Florian Lehner 00:34:40 Do you already follow the, the semantic conventions for GPU attributes?
Tommy Reilly 00:34:49 I didn't know such a thing existed.
Florian Lehner 00:34:51 Okay, I can, I can link, in the document.
Yep, they're quite new, so, Luke Miller, I think, just added it a few… Moments ago.
Tommy Reilly 00:35:11 Cool.
Felix Geisendörfer 00:35:36 Okay, but yeah, I think the high-level summary is that everybody is supportive of adding GPU-related semantic convention entries as needed, and we can probably hash out the details of What we want for sample types and frame types in, pull requests.
Tommy Reilly 00:35:56 Sweet. Thanks.
Felix Geisendörfer 00:36:24 Does that imply you'll try to do some work in this area, Tommy?
Tommy Reilly 00:36:29 Yes.
Felix Geisendörfer 00:36:31 Thank you so much, that's great.
Sweet. Okay, any more… Questions, thoughts on this?
Once? Going twice?
If not, I know Scott is getting ready, but we have Alexey now, so I might jump us back to the, action items that were on Alexey's list, and then jump back to the regular agenda.
Alexey Alexandrov 00:37:02 Yeah, the first one, not done yet, but yeah, I will take a look. That's for the orphan check in, string references. For the second one, I wrote a doc, so I would appreciate if people take a look and, There's not a lot of, like, proposal there yet. It's mostly the, it's mostly a statement of the problem.
Like, effectively, we… yeah, like, I list different questions that we… We discussed previously, and… Most of them… revolve around the relationship between period and sample type, when When we have these different formats, or different shapes of samples in terms of timestamps and value count.
And the question is.
Do we allow consumers to make implicit assumption that in a particular case, the particular sample type actually captures, kind of, like, the count of periods, because we… but that would be… that would be implicit. This would… I don't think it would be my top choice.
Yeah… Well, I guess one question is how much we want to go into the details now, or people want to first take a look offline, and then we have a deeper discussion.
Felix Geisendörfer 00:38:31 I think every time we try to have these conversations without people being prepped, we sort of struggled to… clearly articulate ourselves, so I'm definitely not able to comment, but if somebody feels like they read the stock or have enough of the context loaded in their hat right now to discuss, feel free to go ahead.
If not…
Alexey Alexandrov 00:38:56 done.
Felix Geisendörfer 00:38:56 And I would propose we reread the doc and start commenting.
Alexey Alexandrov 00:38:59 Yeah.
Felix Geisendörfer 00:38:59 And pick it up next time when we have… everybody has seen it.
Alexey Alexandrov 00:39:03 Sounds good, yeah.
Felix Geisendörfer 00:39:04 Okay.
Cool.
Then, Scott, now it's your turn.
Scott Gerring 00:39:21 Cool. Two things. One, quickly for visibility. Thanks to Frederick, we've got a meeting tomorrow with the MemAlec folks at Microsoft, so it seems like they're interested in getting… observability hooks in there, which would be great, I think, for a few people in the call. I will loop back in the Slack channel afterwards and let you all know how it went.
The second one is… kind of heading off something that I think that's going to come up in the memory profiling.
third PR that adds the allocation profile, and that is that I need, or we need for memory profiling, a few extra bits of information to come back in the trace. This is interesting because we've been talking a lot lately about how to make the probe infrastructure generic.
And the trace is a part we haven't touched yet. So, in the PR, concretely, at the moment.
I've just added a couple of other fields to the trace. I don't think that is particularly appetizing long-term.
Because it's very tightly coupled to memory profiling, right? Like, you can use the value for the pointer, and then you need weighted bytes and allocation count, things like that as well.
I think maybe a pragmatic middle ground would be to have after value, like, value extra, and chuck… Some bytes at that, and then look at how… what happens, and we have a few other examples of things that need to carry extra information back out of the trace, kind of what the generic shape that emerges is, and then trying to generalize back from that.
But I think this is kind of, like, the interesting part that's going to come up when we get to the next PR with memory Profiling, so I wanted to bring it up now in case anyone has any ideas now, and at the very least, to get people's wheels to start turning so that we can… we can think on it collectively.
I spoke a bunch. Does anyone have any opinions or thoughts?
Roger Coll 00:41:10 To me, it sounds good. I think now we can focus on landing memory profiling, and later we can focus on the refactoring, basically.
the process manager, and what we discussed, maybe asynchronously? - Can be a follow-up, so… Yeah, to me, sounds good.
Scott Gerring 00:41:29 Cool.
Yeah, I feel like there's a pragmatic kind of acceptor, an awkward middle ground moment. But once we have some examples of what else we might want on there, it'll also be easier to find a meaningful abstraction for that.
But yeah, if anyone else has opinions, think on it a bit.
I am a bit stuck with other options for the moment, so… opinions would be lovely.
Felix Geisendörfer 00:41:59 Okay, sounds like there's no objections, so you could proceed with what you're doing for now, and then figure out a better solution later.
Scott Gerring 00:42:08 Cool.
And the next one I chucked in on your behalf, Jonathan, because you raised it in the Slack.
Jonathan Halliday (IBM) 00:42:15 Yeah, thanks. So I'm… implementing this for the Java SDK, and it just feels like one of the parts that's maybe a little underspecified. There's a lot of freedom for me as an SDK implementer to make design choices there that might not be consistent with other SDKs.
So it might make more sense to… to try and put some guidelines in the spec for… We want that bit to work.
I think… It would be reasonable to have a default set of the attributes, defined in the spec, to say, unless… unless the user chooses otherwise, These are the ones we're going to pull out of the context on the thread and copy into the… The context that gets exported.
I mean, at one extreme, it's everything. We just, you know… Copy the entire… set of attributes in the context object. I think that's probably overkill.
Scott Gerring 00:43:18 We've also said in the… or the spec also says that we should try and stay under 640 bytes, so there's probably.
Jonathan Halliday (IBM) 00:43:24 Right.
Scott Gerring 00:43:25 Precibly low ceiling, though.
All Evo and I ever came up when we were talking about this is that people obviously want the route, that feels like the first one, but beyond that.
I wonder if anyone from PolarSignals or Dash Zero or Elastic who has similar custom label stuff already in production has opinions on what makes sense there.
Tommy Reilly 00:43:50 I don't, but… I figure Frederick probably would.
Scott Gerring 00:44:00 We can tag him in the thread on Slack and see if he has anything to add.
Tommy Reilly 00:44:03 There you go.
Scott Gerring 00:44:07 Jonathan, do you have any opinions, yourself?
Jonathan Halliday (IBM) 00:44:10 I do not.
Florian Lehner 00:44:18 maybe just… To… going back to the discussion we had earlier, I think 2… Two attributes that are really essential for most parts are container ID and service name.
So maybe this could be a beginning for something.
And everything else is voluntary and…
Jonathan Halliday (IBM) 00:44:40 Yeah, they're process level, so they'll… they'll be in the process context.
I'm talking thread level.
Florian Lehner 00:44:46 Right, right,
Jonathan Halliday (IBM) 00:44:49 I mean, the process context spec might want to go into more depth on what exactly is in the resource, because another issue we had with the process spec was, The way the SDKs are designed, there isn't actually a single resource.
There's… there's one per signal type.
Scott Gerring 00:45:07 I, I had…
Jonathan Halliday (IBM) 00:45:07 In fact, at least for Java, there might be multiple SDKs in the same process, which makes life really awkward.
So yeah, we might want to define what kinds of things to specify in the resource for the process spec as well.
Scott Gerring 00:45:25 I was chatting with Naif the other day about the multiple signal thing, because I was also saying, like, I would like to implement this for Rust as a default operation, but I don't know what resource to use, because you configure the signals independently.
Jonathan Halliday (IBM) 00:45:37 Right. And he was…
Scott Gerring 00:45:38 Saying the pragmatic thing to do is probably to just use it as part of tracing, because that's what people.
Jonathan Halliday (IBM) 00:45:44 Yes and no. The issue with that is that if you're processing, if you're doing this for something like OBI, and OBI is taking care of the tracing, then the SDK doesn't actually have tracing configured, so you can't copy the resource.
Scott Gerring 00:45:58 Yeah, fair enough.
Jonathan Halliday (IBM) 00:46:02 You could word the spec something like, if the tracing one is present, then the process one should be consistent with it, but… Yeah, there's always going to be corner cases.
The other issue was that, at least the way I've got the lifecycle wired in Java, the, The process context comes up very early in the lifecycle, and even if tracing is present, it might not be configured yet.
And there is no lifecycle hook.
When configuration is complete, there's no callback to say, okay, things are stable now.
So you have to have some kind of lazy initialization, or re… republish the context at a certain point, if you want to try and accomplish that.
And that's before we get into, you know, RPAMP dynamically reconfiguring things.
Scott Gerring 00:46:51 That's… it's not, like, a very… satisfying solution, I guess, but the way I've got it in the Rust PR is making it explicit. So there's an APIR, you call it, you give it the resource you want.
Sorry.
Jonathan Halliday (IBM) 00:47:04 This thing is problematic.
Scott Gerring 00:47:05 Also, because it's not…
Jonathan Halliday (IBM) 00:47:06 What I always get from Java is that nothing goes into the public API unless it's in spec, because it never ever changes, right? The API is incredibly stable.
So they literally won't let me define an API, because they say, you know, there's no spec. Therefore, there is no API.
So in the sense of, I can have a public Java class, and people can Talk to it, yeah, that's fine, but, In the sense that there is a jaw that is the… the API jar for OpenTelemetry Java. I can't put anything in there unless it's in the spec.
Scott Gerring 00:47:40 It's also a cop-out, because we want this to work everywhere. We don't want people.
Jonathan Halliday (IBM) 00:47:45 Yeah, exactly right. A user who knows how to configure this in Java should be able to configure it the same in, you know, Rust or Golang.
So yeah, we might want to give some thought to what the API surface for this thing looks like.
I mean, something as simple as, Is there an environment variable? Turn it on.
And is it owned by default?
Scott Gerring 00:48:10 I guess that's another can of worms, in the sense that then it becomes something in the specification, and… That's a whole… that's a whole thing. I'll start a thread with Evo, and yourself, and everyone else who's interested once he's back, because I think he's thought about this a bit harder since we last discussed it and put the spec down, and he might have more ideas in the meantime.
Florian, I don't know if you got any further with yours with the Golang PR, by the way, because I know you were also working on this.
Florian Lehner 00:48:40 guess, turn down my effort at the moment for this.
I did not get further with this, sorry.
Scott Gerring 00:48:50 I think you should take your PTO seriously as well, though, to be honest.
Felix Geisendörfer 00:49:03 Okay, then… the summary is, Scott, you'll check with Evo as a next step, and we'll take it from there. As far as I'm concerned, I always thought we would define a spec at some point for an API to set at least custom labels. Maybe we do need more control over things that are automatically added as well.
or threat context, but I think… I don't see a way around that at some point.
Scott Gerring 00:49:30 Yeah, I think that's fair. I'll make sure that we start a thread so we can kind of push it forward asynchronously with everyone.
And yeah, the other one, the multiple logical applications within one Java container, this has come up before. That's hard.
I had nothing to add.
Jonathan Halliday (IBM) 00:49:54 Yeah, I mean, the… the idea of the process concept as a singleton winds up being messy in Java, because, yeah, you can… you can have one, but only at the class loader level.
So what it's, it's mapping that object down to a single bit of mapped memory.
it gets hairy. I've just avoided it for now.
Felix Geisendörfer 00:50:17 net, as far as I know, also has it frequently, where they run multiple services within one.
Jonathan Halliday (IBM) 00:50:23 Rosa.
Felix Geisendörfer 00:50:35 Okay.
But I guess we have more sources right away. Anybody has more thoughts before we go through the last two agenda items?
Going once… Going twice… And then, next one is from Florian.
Florian Lehner 00:50:55 Yes, just a quick update.
I made a suggestion to the specification for profiles to list, well-known attributes.
When attributes for, sample types, sample types only.
And, I went through, PTROF and Go, and I picked, I think, most interesting one. There's not a complete list, but more like a starting point for backends, where they can say, hey, if I see this combination of, sample type, I can expect this kind of, profile. We have, on multiple occasions, requests from people, that are… want to have such a, such a list of, known value types.
known… sample… known sample types, so I think it just makes sense to just add, Just act on.
Yeah, if you have any comments, please feel… please feel free to, hold on.
If you have feedback, just leave a comment. Thanks.
Felix Geisendörfer 00:52:06 That one.
But we don't discuss it now, unless you want to.
Alexey?
Alexey Alexandrov 00:52:14 Is the plan to eventually make this semantic conventions, or…
Florian Lehner 00:52:21 no, with the reasoning that, we cannot enforce something on PPROF, and I think that's, for keeping the compatibility, it's… it's better to have a specification of, like, hey, these are values which work for PPROF and hotel profiles, and, I think it would be a… not the good move to specify something and then start conflicting with P profit. It's something I want to avoid. So just having a list of such values That are commonly known and well-known, without… Enforcing something about it.
Okay.
Alexey Alexandrov 00:52:57 Another thought that would it make sense to… To document which of these are cumulative versus instantaneous.
Or most of them are cumulu… cumulative?
I guess.
Florian Lehner 00:53:22 I didn't think about this,
Alexey Alexandrov 00:53:25 I think… In use space ones, the space ones are probably instantaneous.
Felix Geisendörfer 00:53:32 Yeah, so the in-use space is instantaneous, the alloc space is cumulative, but you can also sense the analog space as a delta, and I guess we need three types, right?
Like, cumulative can mean since, like, the start of the process, that's what the Go runtime does.
Alexey Alexandrov 00:53:49 Correct.
Felix Geisendörfer 00:53:49 for allocations, but some profiler implementations, including what we do at Datadoc, is actually only sending the delta, like, what has changed since the last profiling, memory profile was submitted, like, allocation.
Alexey Alexandrov 00:54:02 Oh, since the… since the… since the last profile.
Felix Geisendörfer 00:54:05 Yeah.
Alexey Alexandrov 00:54:07 Well, I guess… I would say, like, those are… yeah, I think it, like, depends what you consider part of the type, because you could say, well, this is all… this is still cumulative, it's just, like, over what duration this is cumulative, because it can be cumulative over the duration of the profiling itself, or cumulative over… Since the process start, more cumulative since the…
Felix Geisendörfer 00:54:28 Yeah, but we need to define that, it needs to be clear, I think.
Alexey Alexandrov 00:54:32 Yes, yes. And I would say, like, the duration should be somehow, like, derivable from the profile in this case, in case I… if I want to compute the rate, I should be able to do this one way or another.
Florian Lehner 00:54:54 Boom.
Alexey Alexandrov 00:54:55 And… and as… as another thought is also, we currently, Florian, you currently list this per, kind of, like, per profile type.
Which I think is fine, like, the only… and maybe this is, like, this is… this is a minor worry, but… like, how to avoid duplicates. Like, in the future, someone adds another profile type, but the metric is kind of the same as in another profile. Like, should it be… should this be more of a flat list?
But I don't have a strong preference, because right now the list is fairly small, I think we can manage it.
Florian Lehner 00:55:38 I have no preference on the… on the format, so I just wanted to… Bring something up for discussion, and Bring us forward… forward with this, there are examples, like Felix shows now in the specification of the protocol file, but I think most people don't look at this, so I'm… Yeah, I think it makes sense to have it more in a more visible space.
Alexey Alexandrov 00:56:05 I think it's definitely a great, great start and great initiative, and whenever people come with, look, oh, I want to collect this new type of data, it's… it can be a very good start to… point people to this and say, like, hey, is this similar to what… to anything we already document, or is this completely new? And… and if we put, like, is this cumulative or instantaneous? I think those are, like, very good discussions that Should happen early in making a profiler.
Florian Lehner 00:56:35 Yeah, makes sense.
Felix Geisendörfer 00:56:38 Yeah, just a quick thing for me, Needs… we need to clarify, if this is start or end of collection.
I think it's still left open right now.
Alexey Alexandrov 00:56:58 I assumed it's starch, but…
Felix Geisendörfer 00:57:02 I think that would make sense, given what the rest of the comments said that I just skimmed, but I think being explicit Not hurt.
Alexey Alexandrov 00:57:12 And I'm smiling because I also know that people make different assumptions, so I would not be surprised if… If it's not how… how other people read it, yep.
Felix Geisendörfer 00:57:24 Yeah, I'll take an action item on this, maybe somebody can add it for me on top of the list while I'm gonna move us to the last item, because we have only one left, and I think if we move on now, we have a chance to… Cover the full agenda, unless somebody wants to get in one last comment on this one.
Alexey Alexandrov 00:57:42 In the document that I wrote, there are some discussions about the profile timestamp and duration, so if you want, we can roll that there as well, or this can be fixed independently if it's simple enough.
Felix Geisendörfer 00:57:56 I think it's a fairly simple fix.
Alexey Alexandrov 00:57:58 Okay, okay, okay.
Felix Geisendörfer 00:57:59 I'll just submit a PR.
Okay, any last comments? Going once, going twice, going three times? If not, Matt wants to talk about shower async Profiler Update.
Matt Tichenor 00:58:18 Hey guys, yeah, I'm Matt, I've been only one of these, so first of all, still trying to figure out how to contribute and be a part of this community, but I know it's not related to either the spec or the eBBF profile that I've been managed for this group, but I wanted to share that we've added So I'm from ABS, so technically open source library, but our team's merged support for OT.
There'll be export of profiles thrived out of the async profiler.
Library. So we just merged that this week, so… Just wanted to… Let the team know about that. I don't know if there's anything we need to do.
Just FYI. And then I also wanted to… ask, I don't know if this is, like, a… let me… I should Google, or… it's already covered somewhere, but I'm trying to understand, as this project evolves, and we evolve the spec, like.
Is there any guidance on how we should keep this in sync? Is there any expectations on, oh yeah, we know we're going to be making a breaking change you need to plan for? But basically, now that we've pushed this into the… that SDK, I'm not really sure if there's something I should be aware of as far as process for Understanding changes and timelines and all that kind of thing.
Felix Geisendörfer 00:59:32 Yeah, I'll let Alexey go in a second. Just one thing for you to look at is this pull request that's currently under discussion, Matt. It's on the ProtoRebo 857, and you'll find it in the notes. Here we suggest that exporters, such as Async Profiler, should add a version number, like a development version number, when you make requests, and that development version number will essentially tell receivers which version of the spec… sorry, of the protobuffer.
Matt Tichenor 01:00:01 Okay.
Felix Geisendörfer 01:00:02 you're currently exporting, and be able to reject newer versions that are not understood by the receiver, or to potentially convert older versions into a new format when that is possible. So that is something you probably want to add as soon as possible, and then you basically just need to follow the OpenProto, releases here, and when a new release comes out, such as Profiling Upgrade, and the release notes will include the new development version you should send when you make that upgrade. That's how we're going to manage it until we're stable.
Matt Tichenor 01:00:33 Okay, great panel, thank you.
Felix Geisendörfer 01:00:36 And then Alexico.
Alexey Alexandrov 01:00:38 Yeah, I wanted to mention the same thing about the version. I was also, like, not related to this topic, but kind of related. Like, I wonder if we want to… will it be a good time at some point to do… to make a blog post?
kind of, like, what's happening with profiles, and maybe mention support and other tools like this. Well, if, I remember there was some discussion how much OpenTelemetry wants to mention other tools, because it kind of tries to stay vendor neutral, but I think if we get a good a good collection of items, like what was happening with, profile support in different tools, maybe… maybe this can still be a good OpenTelemetry blog, but anyway, I was… like, we can discuss it next time, like, but I wonder if there's a good time to do some kind of update to the community at some point.
Felix Geisendörfer 01:01:31 I think it would be great to, like, at some point, update the community on which tools and profilers support the OTLP format.
And yeah, the hotel… the hotel marketing guidelines are… had been a nuisance in the last blog post we did, but I think we can generally mention tools, especially if they're open source.
Matt Tichenor 01:01:51 No, it was… open source on their Apache license.
Felix Geisendörfer 01:01:56 Yeah, the hotel project has some interesting views on…
Matt Tichenor 01:02:01 I don't care, I get it, I'm not trying to pitch them in their thing.
Felix Geisendörfer 01:02:06 But the Profiling stick is supportive. Like, any open source tool that implements OTLP and supports a new signal, we're happy to promote as much as we can within OpenTelemetry.
So thank you for, yeah, that upstream stuff.
Matt Tichenor 01:02:23 Thanks for sharing that, Abupta.
Oh.
Felix Geisendörfer 01:02:26 And… I'll take a look at it.
Matt Tichenor 01:02:27 If I saw it.
Felix Geisendörfer 01:02:28 Awesome, yeah, we're time. Does anybody have any last thoughts before we close it out?
If not, then thank you everybody for joining, thank you for all the contributions, and as usual, have a nice local time.
So…
Scott Gerring 01:02:47 It's.
Alexey Alexandrov 01:02:48 Yeah, bye.
