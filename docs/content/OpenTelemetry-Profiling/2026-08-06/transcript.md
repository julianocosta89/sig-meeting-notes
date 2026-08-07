SIG: OpenTelemetry Profiling
Date: 2026-08-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Florian Lehner** 02:05 Looks like everyone has… some kind of issues with the Linux Foundation Zoom setup.
Mmm, probably.
**Jonathan Halliday** 02:14 Yeah, I didn't notice if the underlying link has changed, or just the way it's presented has changed.
**Florian Lehner** 02:23 Yeah, first he was asking…
**Jonathan Halliday** 02:24 put meeting things into Zoom directly, but now I click a link in the browser and it starts Zoom for me with some black magic, so I don't know what it's doing.
**Florian Lehner** 02:36 I was facing issues not being able to join us, I guess, but need to register first, which is kind of… Strange.
**Jonathan Halliday** 02:44 No, it seems to be working as guest for me.
**Nayef Ghattas** 03:15 Hello.
**Jonathan Halliday** 03:16 Yeah.
**Florian Lehner** 03:17 Bonjour.
**Nayef Ghattas** 03:20 I had a bit of a hard time joining the meeting because the link changed.
**Jonathan Halliday** 03:25 Yes, they like to keep us on our toes.
Shaking up my base.
**Florian Lehner** 03:55 I suggest to wait maybe 2-3 more minutes, before we go. I guess more people will have, or do have problems with the new Linux Foundation setup.
Let's wait 3 more minutes, and then start the meeting. I perhaps posted that, link to the new LFX Zoom meeting into the document, maybe more people can not showing… In the meantime, I will start sharing my screen, Unless someone else wants to volunteer, or… moderating the meeting, please let me know.
Now you should see my screen with the current Profiling Signal Meetings.
Okay, we are 10 minutes in. Welcome, everyone. As no one volunteered, I will just start moderating the meeting. Please put your name into the attendees list if you did not have yet.
And then I will start, with… the topics for today, starting with the review action items. If you have any topic you want to talk about, please add it to the agenda, so it will not get missed.
First off, I think, everyone saw it already, at least everyone in the meeting. There is a new Linux Foundation, Zoom link meeting. This will stay now.
hope there will be no further issues, and if there are issues, I think we should report them back to, We should report back to, Morgan.
Yeah, otherwise I will start with the review action items.
The first one is for Alexei, I did not say… I don't see Alexi… present in… the call, so I will continue for this, unless someone else can speak up for it, but I think the offense check is still missing.
Continuing with the… Prof… Prof Check.
There are still the CIC Profiling PR… That needs approval.
We have one approval, would be nice to have a second approval for the duplicates mapping check.
And as I was tasked in the last meetings.
There's also now the PR for the functions, lines, and locations, and links. So, a very similar PR to the mappings.
Just for the other ones.
This was Toronto link.
Yeah. Why it's on my fork?
This PR is based on the still-open Mappings Check PR, because it, there are some duplicates, and I don't want to duplicate this, these parts, but otherwise it falls really, like, the structure, have a type for, for the various kinds.
put them into a map, and, checked if they exist, so, it's really, like, always the same. The most part of this, of this change is really, like, tests.
Otherwise it should be straightforward.
If you have time, please have a look.
Other than this, I will continue. Nayef, do you want to talk about the OTLP version? Do you have updates on the OTLP version in payloads?
**Nayef Ghattas** 12:21 Yeah, I think since the last meeting, Tichen reviewed the doc and approved it, and I discussed with him about how we should move forward with this, and he thinks we can just do an OpenTelemetry PR, with the content of the doc and the changes… OpenTelemetry protot, sorry. So, appear in that repo with, content of the… of the proposal, and just a change in one of the markdown files in the OpenTelemetry Proto repo. So I was on PTO the last couple weeks, so I wasn't able to do that, but I'll… I'll follow up on this, each time. If anyone has any other comments on this before we make the PR, feel free to drop them on the doc.
**Florian Lehner** 13:12 Thank you, working on this, and I… I think I… I hope… I don't remember if I've said it, but, it already looked good.
to me the last time, so, looking forward, having this change done, and, this looks also… or once this, once this is done, I think we have an easier time with the braking change that we already have pending in OTLP Proto.
So this will give us a more smooth going forward, towards the beta, so I really appreciate the work.
Okay, if there are no… Other comments on this?
I will continue.
Also, the next topic is for Alexei. I think I didn't see any… changes, PRs around this, so I think there will be still pending I don't… It feels like no one knows any other updates, and then I would probably go back to Nayef again, and Scott.
**Nayef Ghattas** 14:22 Yeah, I think Scott wanted to be here, but he couldn't, so he tasked me to say that we appreciate all the reviews on the proposal and the implementation PR for memory profiling, and we're still seeking feedback, so… If anyone has general feedback on either the proposal or the, all the implementation draft PR, feel free to drop them. I think Scott has responded on most of the feedback that was on the… on both changes, and we're happy to… to continue any of the discussions that are also open there.
**Christos Kalkanis** 15:00 And Nayef, so I think I can approve this today, actually, because I saw this morning that Scott has replied to all the bits, the questions I had, so it looks fine to me. I'll approve the proposal. It's essentially a design document, we can merge it.
And then the next step, we have a sample implementation.
I'm guessing then, we're working towards measuring that, right?
**Nayef Ghattas** 15:24 Yes, I think he opened it as a draft PR, but we can open it as a PR as soon as the proposal.
**Christos Kalkanis** 15:30 Okay.
Okay, cool. And I guess then… Sorry, go ahead, Claire.
**Florian Lehner** 15:35 The draft PR is based on the probes API and changes to, process manager sync processes, so there will be an, for the USCT handling and the process starting, there will be a new API.
Yeah, but, it really depends on the Probes API, that's why I'm pushing a little bit for this.
**Nayef Ghattas** 15:57 I think we did two implementations for this, an initial one that didn't depend on the Probes API, but contained a lot of, repeated stuff and overlap with the probes API stuff, and we modified it to depend on the Probes API stuff, but, yeah, if the Probes API stuff has a good chance of, of landing soon, I think it makes sense to… to continue basing it on the Probes API and… I'm waiting on that.
**Christos Kalkanis** 16:27 So my question is, I guess we know what we need to do for the eBPF Profiler, because we're fully in control of that, so that's fine. We'll merge approach API, we'll merge the memory Profiling there. The next question is, how do we make sure that we advertise that this way to do memory profiling now exists?
So that, you know, people can actually start to use it.
Is there a good way to do that?
Maybe a blog post, maybe publishing the protocol somewhere?
**Nayef Ghattas** 17:00 Yeah, that's a good question.
I think one, one thing we… we need to put forward is the… One way to use that proposal is to use JEmalloc or TCMalloc with USDTs that are on the allocation hooks, and this is what we've been doing internally, where we have sort of a slightly modified build of JEmalloc and TCMalloc that uses config options from both to add the USDTs on the hooks, and… once we have, once we have that somewhere publicly available, I think we can… We can, have people try it out and, try it out in conjunction with the eBPF Profiling OPR, and test this.
And as for, like, more general usage, I think, yeah, a blog post would make sense.
**Florian Lehner** 18:15 Yeah, I'm not as good as moderating and logging everything like Felix does, so I hope everyone is fine with the notes I take.
Otherwise, I think we can go to the next Topic?
And go back to Nayef again.
**Nayef Ghattas** 18:41 Yes. So, one use case that we've… we've found, is that sometimes we're comparing profiles that come from the same service, but using different versions of runtimes. And right now, there's not an easy way, to know which profile corresponds to which version of the runtime. So we would run a service, I don't know, with Java… 22 and Dover 23, and we want to compare the performance between both. And so… we were thinking of a way to make that information available in the OTLP profile.
We had an initial proposal that put that information in resource attributes, but as Florian pointed out, a single resource profile could have multiple runtimes in it, where we could have Go invoking Python invoking something else. I think in that proposal, what we did is try to pick the one that is available in the main executable.
And pick one. But one other alternative we could do is just introduce a new semantic convention for the runtime version that we put on the frame level.
Since we have the frame label attributes that are all in a dictionary, that shouldn't add much overhead to the profile size, but we would need to add a new semantic conventions in profile.
Right now, we only have, I think, profile.frame.type under the profile namespace.
So, maybe an… we either keep that one and add a new one, which would be profile.frame.type.version, or we rename that one. Yeah, I'm curious to know whether there's, in general, any thoughts about this approach, or any… and any suggestions on what the… Semantic convention, naming should be, like?
**Florian Lehner** 20:46 as I was the blogger on this PR, I really think that we… should keep this information closer to… to the stacks, so that's why I think the process around… the resource attributes were the right, wrong direction.
I was thinking about this more, and I was wondering if we, instead of attaching it to the profile frame, we attach it to, the message, message mapping, because the, in message mappings, we have attributes, and we can have just, a regular attribute. So, I have here message mapping opens, and we have attributes that we can just, Can just assign to, so here we can put in whatever… whatever we want.
It should follow some kind of, semantic convention, yes. Then maybe profile mapping.
runtime, profile mapping, runtime version, something like this, as an idea. Just putting into the round, might change, maybe.
maybe this is the wrong place. I was just thinking about, hey, what would be best Yeah, that was… maybe I was… that was the stuff I was thinking about.
**Christos Kalkanis** 22:14 Can we flip the question a little bit? Like, can we explore what usage of this new attributes looks like? Because, for example, it may… for me, it looks like there might still be value in having it like the initial proposal was, right? As a… for the entire stack trace, and not going deeper into the trace and attaching it to a frame or to a mapping. For filtering is. Like, for example, maybe you don't want to go deep into the methods.
to look at frames and mappings to figure out what the dominant runtime is. And in the majority of the cases.
Will we have a runtime that… would characterize the entire trace, right? We could call it… let's say you have a Java process, right? So we start… the Java process starts executing C++ code, and then we switch into Java trains, and then maybe it calls into Lua.
you know, just an example. So now you have three runtimes, but Java is a dominant runtime, so maybe the Java runtime ends up at the root.
And then maybe we can have the more specific rantimes be attached to frames or mappings, but if someone wants to filter based on the dominant runtimes, he would only have to look at the rookie. He won't have to go deeper into the message.
I mean, does it make sense?
Is it useful?
**Florian Lehner** 23:42 A question I have, how do you define the dominant runtime? As this would… could change depending on the view, I think.
**Christos Kalkanis** 23:50 Yeah, I think… so that would be on the producer side, right? So the producer would have to decide how to encode that, and the assumption here is that in most cases, the producer knows, or the producer can make that determination. Like, for example, if you have a Java stack trace.
and that JavaStack trace ends up calling into Lua, maybe you have Python there as well, right? Well, on the producer side, you can say, I don't care about this. Python is not the dominant runtime for this trace, it's Java. It's Java that's actually calling into Python.
So you could do that in this way.
Can you always do that in this way?
Probably.
to me, right now, it seems that it would be possible. Maybe it's not 100% accurate, maybe in some cases, there's ambiguity. And maybe in those cases where there is ambiguity, you don't do the… you don't attach it to the root.
Right? So the root will be kind of fallback.
If it's there, it means that there's… that the entire stack trace has a dominant runtime, and that's the… you can use filtering if you want to reject stack traces that are not Java-specific versions, so… But if it's absent.
Then, yeah, maybe you have to go deeper into the message to look at individual frames and mappings and so on.
**Florian Lehner** 25:10 While I see the benefit of this approach, I think it will make it harder for people to handle the protocol, because there's always, like.
you can find this information at this level, but also at this level, and, if you, think of OTTL and, people that then implement some kind of filtering, or, altering the protocol based on information, I think this will… Will not be received well in the hotel world.
Having the same information on two different levels, depending on How it comes from, or where the duration is from.
**Nayef Ghattas** 25:49 Yeah, but at the same time, to Krista's point, I think 99% of the… the profiles… well, I don't have real data to prove it, but should have one clear dominant.
runtime… And… not call into multiple… like, they'll… for all the interpreted languages, they would have native and the interpreted language itself, because of the interpreter calling the interpreted frames, and for the native languages, they would just be, native code.
So… It would have been… Yeah. Sorry, go ahead.
**Christos Kalkanis** 26:31 I was gonna say, it… like, to me, it seems as if… Like, this, the rest on the producer. If a producer can, in the vast majority of cases, make that determination with accuracy, then to me, that would make sense, then, to actually have it. If the producer keeps running into ambiguity.
Which, right now, to me, doesn't seem realistic. It seems that in the vast majority of cases, it's possible to determine what the dominant runtime is and put it for the… and have it for the entire statistics.
Yeah, maybe we can explore this a little bit more, but Like, this is purely from the usability side, right? Like, I would assume that it's valuable to be able to prune stack traces Immediately.
Without having to actually… because then you're forcing that determination.
At the time of the filtering, when you could do it way ahead of time.
That's the trade-off, right?
**Nayef Ghattas** 27:37 Yeah, agreed.
**Christos Kalkanis** 27:39 like, imagine you have a stack trace, and it has, you know, native frameworks… it has two runtimes, Java and Python. Then at filtering time, you have to basically extract those two runtimes and determine okay, you know, which one is… what am I trying to do? Why pay the cost every time if you can do it way ahead of time?
**Florian Lehner** 28:03 Yeah, I see definitely your use case and that users benefit from it. I'm just worried about special cases like you mentioned with Lua that then calls into multiple runtimes.
Untone.
This will work out.
**Christos Kalkanis** 28:22 So, if in the vast majority of cases.
If this assumption holds, if you can determine a dominant runtime in the vast majority of cases, then it also seems likely that… The consumers of this, whether we're talking about filtering or something else, Then, that they would only care about the dominant runtime. They wouldn't care as much about the other interpreters that happen there.
So… They would only… So then, if that's true, we can assume that most of the logic that would act on this data would only have to look at the root, and there would be a minority of cases where they would have to do deeper processing, and then maybe go down into the stack trace and try to determine what additional runtimes are there.
Besides the dominant runtime.
Then, if that's true, the complexity doesn't really… manifest for the vast majority of cases. You only have this additional complexity if you actually want to extract every possible runtime that exists on the stack base.
So you're optimizing for… uses, right? The most common case here.
Which is… the least complexity here. You only look at the root, you determine the dominant runtime for arbitration, you act on that information. And maybe there are additional cases where that's not enough, and you need to go deeper into the space, and that's when you would have to pay those costs, instead of paying them every time.
**Florian Lehner** 29:58 Yeah, makes sense, makes sense. Building on this, I'm wondering if this could be configurable in a way with the… Process attributes… Handling that Roger, I think, suggested.
So, I think this could work hand-in-hand then.
**Nayef Ghattas** 30:26 Sorry, I do not understand exactly what you said. Work hand-in-hand with which part, exactly?
**Florian Lehner** 30:33 Let me quickly open… to know.
Something like, yeah, add this in mind, add additional process meter, callback.
That would allow… extracting this kind of information, or I could imagine that it can At some point, extract such information and attach it.
And, as this processed metadata will probably, go into the resource attributes.
This could benefit, I think.
Now, please correct me, Roger, I think you're on the call, if my idea is completely sane.
**Roger Coll** 31:30 Mmm… no, I think it's… I agree. So, at that moment.
We just have access, let's say, to the… Profile system, so anything that is available there could be added.
And… Yeah, I think that the way that it's being implemented here is that… It can be optional, any, let's say, decorator.
And… Yeah, I think it would work. What we would need to change is that this, at the moment, the additional metadata that we are gathering, it's not, added in the final resource attributes, but I think it's… it makes sense to… to add them there, because, let's say, by default, in the vanilla option, we are just collecting the container ID.
So it makes sense to be a resource attributes.
And probably, if we decide that, Yeah, the runtime information is part of the resource attributes, thing.
Yeah, it would make sense as well. And it's pretty straightforward to disable one decorator under the other. It could be done from the receiver configuration.
**Nayef Ghattas** 32:51 Does that mean we would need to reimplement the version detection for the runtime in a different way? Because right now, I think in the suggested PR that we did, we are getting it from the interpreter.
Because the interpreter needs the runtime version anyway to be able to do the unwinding for the different logic for different versions to kick in.
And I guess if we did it on a completely independent way, we'd need Maybe to extract the logic that is getting the… the runtime version, maybe duplicating it in that case.
**Roger Coll** 33:32 Yeah, that would be the difficult part. I would say I need to check how it's implemented in this PR, I'm not sure if, at the moment, that we call this process decorator we have Let's say, access to the interpreters.
If we have access, I think it… We could still do it, because, Basically, this metadata, let's say, in Richard is just an interface that it gives you access to the process manager.
So if the process manager has access to the interpreter, you can do, kind of whatever that, so… Yeah, need to check… I will check this… this PR, and…
**Christos Kalkanis** 34:21 Yeah, I don't think it's there today, but it should be easy. We can add it, because it's… everything goes through the process manager, so it's good that this came up today, actually, because we're, like, finalizing that.
Maybe we don't even need to give row access to the interpreter. Maybe we only care about passive interpreter. Maybe those can live in the process. The process is something we pass in to that interface anyway.
**Roger Coll** 34:46 Yeah, correct. Now we are just giving the PID, but we could add an extra argument that our interpreters should be… should be fine.
**Florian Lehner** 35:03 Yeah, I just had this PR in the back of my head. As you probably saw, I did not add any comments on it, but I was… curious if this matches, and I think the discussion number works quite well, and I will try to review it tomorrow, so helping get this forward. Sorry for the delay.
**Nayef Ghattas** 35:24 So, does it make sense in terms of next step to, to have everyone, like, review the PR, see if we can find a way to include that in the additional process metadata, with the interpreter info?
And if that's the case, we can edit our PL to… be based on the process metadata work, and put the information for sort of the dominant interpreter at the resource level. Does that make sense?
**Roger Coll** 35:58 Yeah, makes sense to me. I will also review the… your PR and see if it can be joined. So, yeah, thank you.
**Nayef Ghattas** 36:07 Okay.
**Florian Lehner** 36:13 Cool, thank you. Thank you, everyone.
I guess then we can move on to the next topic, and, Christos…
**Christos Kalkanis** 36:26 Yeah, this is pretty brief. This is just a call, a call-out. We need more reviewers, we need more approvers for the BPF Profiling specifically.
The issue that is… it has accumulated a lot of pull requests. My assumption is, as we go forward, that's not going to… the volume is not going to reduce. We're just going to have more and more pull requests come in as it becomes more popular. Right now, the vast majority of the reviews are done by people from Elastic, essentially Timo, Florian, Roger, and myself.
So, it would be nice to actually expand this group, the approvers group, And, you know, that's also a road to becoming a maintainer.
And I think it would be good to expand the responsibilities there outside of Elastic, have more people involved, and so on. And the first step to that is to actually get people doing consistent reviews, right?
Yeah, if they help. Right now.
I… I feel that the volume, yeah, is getting to be too much. There are some organizational changes also happening in the Elastic side.
I'm… I'm going to leave the last observability.
Going back to security, which is really my… my fortress, my background, and book Profiling is not really going to be top priority for me, then I'll still be able to work, let's say, a day of… a day a week.
on Profiling.
But even for that, I would like to focus more on the protocol side of things.
not as much on the agent, just because Timo is really doing a great job, but also because if I'm not… the problem with the agent is, if you're not engaging with the agent codebase every day, you lose the context, and unfortunately.
The agent is a very complicated piece of architecture. If you lose the context of how communication information flows across the various subsystems, it takes hours to bring it back into your head, and a lot of the pulley requests require that context in order to have some substance to them, for the review to actually have substance, instead of being superficial.
cycle. And for me.
I've already lost a lot of that context, so now, if I have to review, for example, a process manager.
PR, yeah, it takes me an hour to swap that in, and then the review ends up taking 3 hours. So, I will continue to do that, but I'm not gonna be how I used to be in the beginning, where, you know, I could review 10 pull requests a day when I was fully working on the agent, and the agent was the only thing I was working on.
So it's… practically that means that Timo is still going to… my expectation is that he's still going to be doing the vast majority of the extremely intricate and low-level and time-consuming reviews.
I'm guessing Florian, will continue to be involved there as well, Roger?
But, yeah, the three people, it's just not enough.
**Florian Lehner** 39:28 And to add to this, if you… are not already an OTEL community member, and you are interested to become an approver, Please… Ping me, I'm happy to sponsor ship hotel memberships.
Then I guess we are moving on to the next topic, Jonathan.
**Jonathan Halliday** 40:10 Yeah, so, I've been chatting to the Java SDK people about… Getting some code upstream into the… into that to do process context and later thread context.
And one of the good points they make is that the SDKs make a very strong distinction between API and implementation. So in Java, that manifests as them having different packages in different jars.
it's essentially impossible to get something into the API unless there's a spec for it.
So, OpenTelemetry works that way because, They want to lower the learning curve.
for… anyone who's using it in multiple languages. So if you… if you know the API for metrics in Java.
you can pretty much go to, you know, Rust or whatever, and it's… not gonna have any surprises for you. It's… it's gonna have roughly the same structure, it will take some language.
changes, and it's, gonna have the same functionality, so if you can do something in Java, the odds are you can do it in any other language as well.
So this… this presents a little bit of an issue for process context, because we haven't spec'd an API. So I can put it into the SDK, but only as an implementation detail of the SDK. There's no way to let users interact with it, because… the maintainers won't let it be an API unless there's a spec for that API.
So the question then becomes, is that enough for us?
And can we do what we want if this is just internal? And… I think for process context, the answer is… Probably yes, in that… if the… the bootstrap of the SDK, whether that's an agent or whatever, when it's installed, it just automatically publishes the context. Then the user doesn't really need to get involved anywhere.
Do they need a conflict fact to stop it doing that if they don't want it to, maybe? Do they need enough control to… to filter what's published, because there might be things they don't want to show up in the context? I don't know. These are… these are the kind of questions we need to consider.
**Florian Lehner** 42:28 maybe to back this point, there is some process context implementation for OBI, So that they are also benefit from process context, and S… Instead of re-implementing everything for the process context, going forward, the eBPF profile is just now a dependency for OBI, just to bring it in.
And, yeah, I'm… I think… I think it would benefit, if… If there would be more… if there would be an API description, that's right. I know for Go, there is this auto-generated Go API, But it's just around, it's really just around, getting the automated, API from the protofy, so, nothing more specific, like, encoding, like you mentioned. Native encoding, Or a big Indian, Little Indian, stuff like this, that's not mentioned at all.
So, I think it would benefit if there would exist something like a process context API.
somewhere.
A specification somewhere.
**Nayef Ghattas** 43:51 Yeah, I think one way that Scott was suggesting we go about this is to… I know that he already has a PR that has been reviewed on Hotel Rust for implementing process context in Rust.
Hmm… And, Jonathan, you have the Java thing, so… maybe we can, like, take the opportunity of what we learned for implementing it in the hotel SDKs in Rust and Java and SharePoints, and see what changes we need to do to the… to the spec. Ideally, what we don't want to do is have many different changes to the spec, and have multiple PRs that will require many reviews, to the… to the OTAP, So if we can bundle… sort of bundle all the learnings and changes we want to do to the spec and, do them at once in the OTAB, that will probably be better.
**Jonathan Halliday** 44:52 Yeah, I think that the protobuf, the auto-generated proto stuff, is the wrong level of abstraction to expose. If you look at something like metrics, yes, you can export them to Protobuff.
But none of the product above is API service. It's… it's implementation detail of OLTP.
I think… there is already some API surface in… the… existing things that we import, because we use resource, so resource is already API surface.
And we use attributes, and they're already API service, they're in common.
So it might be that the API is as simple as you can get a a publisher object, and the publisher object exposes a publish method that takes Those things, and… The rest of the spec in terms of, oh, there's a header and there's a protobuf encoding, that is implementation detail.
Because the user's never going to want to publish stuff direct, they just want to give the thing to be published to the API and let it take care of that.
**Nayef Ghattas** 46:07 In that case, who would be the user? Would it be the developer of the SP?
**Jonathan Halliday** 46:11 Does an actual user ever want to do that? Or do they just want the SDK to take care of it for them?
Do they just have a config that says, yes, please?
They opt into it, or… Opt out of it.
And the SDK, when it… when it boots, just does the right thing.
**Nayef Ghattas** 46:36 Yeah, I'm not personally aware of any… I think the main use case we were targeting is for the resource attributes that are available on the SDK are reflected in that process context, and I think right now, most of the SDKs consider resource attributes to be frozen and not change once they are set.
And so, if we're targeting only the resource attribute case, maybe it doesn't… doesn't need an API, because it will just be internal implementation detail on the SDK side.
**Jonathan Halliday** 47:15 Yeah, I don't think that's quite true for the extra attributes that are put in, because… They're driven by the requirements, the profiling, and can change over time.
They're the keys for the dictionary in the profiling.
data structure, right? So… It depends what's captured by the profiler, I think.
**Nayef Ghattas** 47:37 I think the use case for extra attributes was to use them in… was initially to use them in…
**Jonathan Halliday** 47:45 spec.
**Nayef Ghattas** 47:45 that had context, yeah.
**Jonathan Halliday** 47:47 Yeah.
So that's a runtime thing, right? Until you've got threads, and until they're… Generating context, you don't know what the key set is.
Well, do you think we can pre-compute that? Do you think we can define it?
So that they can be populated at boot time.
But even then, there is going to be some plumbing internal to the SDK that Intercepts thread context somehow and publishes it, right?
That isn't user API service either.
the user API surface there is… The context on the thread into which users can put things, which they already do, but that's not part of our spec, that's part of… Tracing?
**Nayef Ghattas** 48:49 Yeah, I agree. I think… For the… for the thread context.
it definitely seems like we want something to be user-facing, because we want users to add something to the thread message and the thread context, and we can maybe rely on the existing tracing API to do that and grab it from the context that is set on the trace.
Although I'm wondering if there are use cases to get that context that would be completely de-correlated from traces.
But I'll need to think about it a bit more.
**Jonathan Halliday** 49:29 Yeah, I couldn't come up with one.
What I did envisage was maybe, Right now, what happens with the trace context is it goes through an exporters pipeline, which is configurable, and some people want to do, oh, this is a secret, I don't want to publish this. You know, God knows why they put it in the trace context in the first place, but, you know… security requirements, right? Someone… someone might… defined at an enterprise level. Oh, you have to scrubble this data for… PII, or whatever. Currently, there's no way to do that, On the publication pipeline.
for the… Third context.
Because there's no integration point in the way that export is a part of the API, right? So the user configures the exporter pipeline and can plug in filters.
There's… there's no equivalent.
For the… Pipeline that serializes the… The same object, the same raw data, but does so to put it into… The Third Context publication.
So, I think we leave that one open for now, and just be aware that it's a thing, and it's gonna limit… how the SDKs operate. If we don't have an API, they can't… Sort of have a supported public service for… for people to interact with it.
That isn't a limitations yet, but it might become so, in which case we'll have to loop back and define an API.
**Nayef Ghattas** 51:06 Yeah, I think that makes sense.
**Florian Lehner** 51:17 Yeah, thank you for the discussion.
Yeah, feathering on the process context is… Currently not… possible at all, I think, as you said.
Yeah, but I'm also not aware of any, any assembly conventions that will end up in the extra attributes, but this might change, as you mentioned.
Any further topics, or any further comments on this?
**Matt Tichenor** 52:01 Not a topic, but… hey guys, I'm Matt, I'm from ERIAS, with NERV.
I'm joined by my colleague Daniel. We're both interested in profiling.
see how we can participate and contribute to this project, so we were just joining and listening in. This is our first time here. So, interesting to… hear what's going on, and it sounds like there's need for, reviewers on project contributions, so maybe we can look at that as our step toward becoming participants in this project.
**Florian Lehner** 52:32 Yeah, welcome, contributions are always welcome, and That the variety of topics in this meeting really,
**Matt Tichenor** 52:41 Yeah, I can see where…
**Florian Lehner** 52:43 protocol level up to, the implementation and the eBPF Profiling, so there… there is always something to talk about, so… and if you have anything to share, or you want… or do you… if you have any feedback, That is also really appreciated.
**Matt Tichenor** 52:59 Okay, yeah, yeah, for now, we're trying to listen and learn, but yeah, I think we'll both, take a look at getting into reviewer status as a starting point. That sounds like a good entry. And then, hopefully we'll be seeing more of all of you.
**Jonathan Halliday** 53:14 Are you guys involved with async Profiling as well?
**Matt Tichenor** 53:19 We know the guy that is. We're both on the CloudWatch team, so that, async Pro feller.
a different org within Aviat, or within Amazon, but we're also working with the The main person on that, so maybe we'll pull him into this.
Till.
**Christos Kalkanis** 53:48 Welcome, Martin, Daniel. So, the OpenTelempy Profiling work, just to give you kind of a brief skeleton, is split into, let's say, two work groups.
One is more focused on the signal itself.
And the other one is the BPF Profiler, which is the profiling agent that runs on Linux, and it's eBPF-based.
So, yeah, I would suggest you take a look at the profiler and the signal itself. There's documentation on the OpenTelemetry AIO site. You go Docs, Concepts, signals, Profiles is there. That will give you an idea of how the profile signal looks, like, from a high-level view.
And then the agent repository is also linked from there.
And then, you know, whatever feels, But you're attracted to the most would be the way to go. Maybe you… you want to contribute to both, maybe one of them makes sense for you.
But yeah, but we particularly need the reviewers for the agents.
Because so far, it's mostly been an approach… an Elastic-based project, and we've struggled to get more reviewers and approvers from outside of Elastic.
But it's also a codebase that is… it's not simple by any means, so it will take some time to familiarize yourself.
**Matt Tichenor** 55:11 And when you say, you're talking about specifically the eBBF Profiler agent on the GitHub, or are there multiple, or just that?
**Christos Kalkanis** 55:20 No, that's it, that's it.
**Matt Tichenor** 55:22 Okay, I thought I heard you say agents, I just wanted to clarify, thank you.
Yeah. Very cool.
**Christos Kalkanis** 55:27 Yeah.
**Matt Tichenor** 55:29 Okay, yeah, we'll figure that out. I'm interested in both.
I'll probably be more useful in the spec than the agent, but it sounds like there's a need on the agent, so we'll… we'll figure something out.
Cool, thank you.
Daniel, anything to add from you?
**Daniel Padin** 55:54 Oh, for now, it's just saying hello.
We'll try to catch up and contribute as much as we can.
**Matt Tichenor** 56:02 Okay, so, nope.
**Florian Lehner** 56:08 Cool, yeah, and, already, thank you, coming in.
If there are no further topics, I think we can give back everyone.
**Matt Tichenor** 56:18 One more quick question, since Daniel and I are new. Is this meeting the kind of primary place where people decide, kind of, what's happening next, debate topics, like, is there, like, intra the two weeks, like, Slack or anything we need to be paying attention to, or we check in on here every two weeks, are we pretty, pretty…
**Jonathan Halliday** 56:39 OpenTelemetry generally runs by Slack, Time zones permitting, weekly or bi-weekly meetings.
**Matt Tichenor** 56:49 Okay, cool.
**Jonathan Halliday** 56:51 But keep an eye on the OpenTelemetry Slack, there's a…
**Matt Tichenor** 56:57 We're in the Profiler group there, too, I just wanted to confirm.
**Jonathan Halliday** 57:00 As you need to be.
Alright. A lot of people… Also in one or more of the, the SIGs for, for example, an SDK or for the collector, because the… the specs for the signals, like profiling or metrics or whatever.
Have to get implemented and.
Usually, the people who are involved in the specs are also involved in one or more implementations, so I don't know what languages you guys are working in, and the eBPF Profiler is, what, Golang, mostly.
The collectors mostly Golang, that seems to be the dominant language.
**Matt Tichenor** 57:37 Well, I mean, internally, we're… almost all Java, but… I think we're both versatile.
**Jonathan Halliday** 57:44 Don't talk to the… the Java SDK implementation.
So if you want to get into something that's more, sort of, implementation, Hop on the Java channel as well, get involved in the discussion of how we actually implement the profiling spec in Java.
**Matt Tichenor** 58:01 Okay, awesome. Yeah, I appreciate all the tips. Sorry for all the newbie questions, but I appreciate the guidance, and…
**Jonathan Halliday** 58:07 Yeah, it's great to have new people involved. Welcome.
**Matt Tichenor** 58:10 Thank you.
**Florian Lehner** 58:19 Yeah, as I said, welcome again, and I think this is a perfect landing, we are getting close to the hour.
Thank you everyone for joining. I think most of the people are fighting the heat wave already.
So, I wish you a proper nice day, evening, night.
Thank you for joining.
**Daniel Padin** 58:47 Thanks, folks.
**Christos Kalkanis** 58:48 Like, 7…
