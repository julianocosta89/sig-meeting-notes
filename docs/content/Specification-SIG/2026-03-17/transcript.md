SIG: Specification SIG
Date: 2026-03-17
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Tigran Najaryan 00:02:00 Hello, everyone. We'll start in a minute.
In the meantime, you can add your name to the attendees, or if you have a topic, add it to the agenda, please.
Okay.
I see Trusk has joined. Trusk, you have the first item. You wanna go ahead?
Trask Stalnaker 00:04:02 I think we covered this async already. Yeah, we're good. We don't need… this was a leftover from last week.
Tigran Najaryan 00:04:11 Okay, sounds good.
Let's see, is Robert here?
is not here, I think. He wants us to take a look at this thing offline, I guess? Align environment variable propagation names.
He's not here, right? I don't see his name.
Okay, so change is important, want to stabilize. Let's call for a review, anyway. Please take a look at it.
You can review it offline.
Alright, this Carlos here? Carlos, you're next.
Carlos Alberto Cortez 00:04:59 Yeah, thank you. Is it okay if you share? Yeah, I can probably do a pretty quick, oh, yeah, first, yeah, we… Tigran Najaryan 00:05:09 Do you want to share?
Carlos Alberto Cortez 00:05:10 There are two items.
Tigran Najaryan 00:05:11 Sherry?
Carlos Alberto Cortez 00:05:12 No, you can… you can share for me, I think it's fine. Yeah. Yeah, so basically there are two items that, are going to be… well, now they are stable, this is the first one, always record sampler. So, for your information maintainers, it's a very simple component.
We have… we have prototypes in a few languages.
So, yeah, this is the second one that Jack has, which is Tracer-enabled.
It has a lot of reviews, as you can see, a lot of approvals, but this was important that maintainers are aware of this.
Likewise, there are many prototypes.
We'll get… Tigran Najaryan 00:05:53 Okay.
Carlos Alberto Cortez 00:06:00 Okay, so the next one, yeah, this is something, that you may remember if you were around, late November or December, probably. This is an old tip that Krisha in Nomueller growth in the past, like.
Probably 2 years ago, maybe even 3 years ago.
Yeah.
And this is the original, Tigran Najaryan 00:06:22 More like Fort, yes.
Carlos Alberto Cortez 00:06:24 Oh, four, yeah, there you are, so it's even longer. This is something that has been requested in the past, but we were busy with other stuff.
But now I'm resurrecting that, and it got updated with a few things. Tigran, if you could go back to the document, there's a quick presentation that I can probably run in a couple of minutes.
Many of you may have seen that.
Tigran Najaryan 00:06:49 You want to share, maybe, so that you can advance as you need?
I can stop.
Carlos Alberto Cortez 00:06:54 Yeah, probably, okay, yeah, yeah, that will work.
Yeah, and in that regard, I think that, This is something that would allow… have multi-tenancy?
at the SDK level, so that would be very, like, nice to have. This is something we have been wanted to do for a long time, and they are related efforts, but… They will work more of, like, workarounds more than actual solutions to this, so this could help us.
And, okay, let me share my screen now.
what's happening? Give me a second, it's complaining about the number of dates. I need to tell him… to tell Chrome to ignore that. yeah, give me a second. Oh, there we are.
Sweet.
Perfect. Okay, let's do that. So basically, this is a very small presentation I did. Basically, this could be the scenario that you are having, like, a single service, but you have actually sub-services, or let's say, like, different tenants there.
And when you are performing your requests, like, as you can see in the blue section, you want all the telemetry to also get some specific telemetry that tells you When you're observing that later on, that, hey, this is… was for tenant A.
not 10 and B, you know? And of course, like, resources doesn't… they don't work because, you know, they are global, and they are, as I said before, related OTEFs that could help us there, but they are not actually defined for this specific case. So this is something that we have wanted to do in the past.
There are some options in the past. Actually, they are discussing the tab. We don't have to go over the alternatives. Actually, there are many alternatives there. One of them that I would like to talk about, because it was requested, but I will do that in a second.
And this is how, basically, context scope attributes could look like. Basically, you defined an abstract call at the API level, like this, abstract context attributes.
Which does nothing, and then that has to be implemented by the SDK.
And then, basically, you just define the key in a context and just allow, you know, to put and get attributes from there.
this is how it would look like. And then, basically, what happens is that the SDK, internally, every time you create a log record item, or a span, or in the future metrics, they would check… they could check if there are attributes defined in the previous, using the previous call I showed.
And then, if that's the case, then you just put those… you add those attributes to log record items, spans, or metrics, you know?
So this is something that would be happening transparently, let's say, you know?
And this way, when you get a request, let's say that, in your service, and you know that it belongs to tenant A, for example, or tenant B, and it could be because you defined some specific routes, or because there's an X token, or there's a header that tells you it's tenant A or Tenant B, then you just set that context.
When you start your request, and during the rest of the request, every log record item, spanner matrix will have those extra attributes inside that tenancy.
a scenario.
Yeah, why not baggage? This is something that people were asking. Baggage only supports strings, pretty similar. The second thing is that it's It's, it's propagated, like, crossing process boundaries, which can be, something that we don't want to do. Very often, you only want, you know, you only know about the tenancy at your service level.
Yeah, the other thing is that baggage, it's possible to… it's possible for users to read that, and we're not sure we want to allow that with context scoped attributes. Instrumentation scope was something that was that could be used, but then probably the problem is that you have to be detecting in every request, case, call, and using the attributes and keeping them around, which seems like overdoing that, the problem.
I'm gonna close the slides now, and going back to the… to the call, So, yeah, we don't have to probably discuss everything, we don't have time also, but, as I said before, this is the general idea. There are things that I wanted to mention, and this is important for people reviewing this. Siya and Jack already reviewed this.
So I'm trying to make iterations on that one. The first item to consider is that, as I said before, bug actually was considered for this, but it only supports string, and it's, It's propagated across processes, which is something we don't want to do.
there was a suggestion in the past that we modify baggage for that, but then there would still be the strings-only limitation for attributes. Processors, I think… I don't know who, but remember in the previous call we had, talking about this in December, somebody mentioned that processors could probably do that.
Even if we define, like… we could even define our own built-in processor, but the problem is that You want to offer this, as I said before, these attributes added transparently to span or log record items.
Without the user having to modify samplers, processors, and because of that, exporters. And, the problem with processors is that, like, when you get, only start, it's too late.
to add the attributes, because the sampler should, should sample a call happens before. So we would have, long story short, we would… if we were to support the processor route, we would have to add one more, operation at the processor level, which Actually, it's something… it could be something weird, because it could look like a sampler now.
Also, there was one thing that Josh Survey had mentioned in the past, that since… if we were to support this, and if it gets approved, maybe we can not only, add attributes from the context, but also from Bagash itself.
So it could be done, and it's super straightforward. Once you have this functionality in place, because I have a Java prototype, which is mentioned in the way, but once you have that, it's super straightforward. You just have one loop to add stuff from baggage, if it's… if there's something there.
And finally, configuration-wise, Jack was asking, like, whether this is an open question, how… because by default, in order to not break customers, users, etc, we don't want to enable this by default. This could be an explicit opt-in.
In case there's also an overload, you know? It's not only about breaking users, it's also about potential overload, at this… at the beginning. And, I was mentioning that my idea initially is just to get a default Boolean flag.
But I am open to discuss that, and it's… in my mind, it's more of a to-be-defined thing. Happy to discuss that otherwise.
And that, that's pretty much my presentation, so yeah, let me know. As I said before, probably a lot of people will need to read that To read the actual tab, check the prototype, but yeah, these are the important points to keep in mind.
Do we have any, short comments or questions?
Josh Suereth 00:14:52 I just want to say great work, man. This looks awesome. I think it's a good start, I think you nailed everything. So, the thing I have with baggage, basically what you're saying in the OTEP is, we could do that as a follow-on, and that makes sense.
So there'd be a follow-on where we could use something similar to make sure that we interact with it. And the other thing to make sure I understand is you're proposing that we want to make sure this context is always pulled in early.
Right? So, like, at the time of measurements recorded, at the time of spins… okay, cool. Awesome.
I look forward to reading the whole thing, this is great.
Carlos Alberto Cortez 00:15:26 Perfect.
Tigran Najaryan 00:15:30 Thank you, Carlos.
Carlos Alberto Cortez 00:15:32 Yeah, I see a… Tigran Najaryan 00:15:33 sharing?
Yep, yup.
Carlos Alberto Cortez 00:15:35 Of course. I saw that Jack was… Jack was writing something. I don't know if you want to say that, or we can read your… Your text later on, Jack.
Jack Berg 00:15:44 Sure, I can jump in really quickly. Just, so I have a PR open, which we discussed last week, which is just like, hey, when we're introducing new concepts to the spec that have SDK configuration surface area, let's consider declarative config first. That's going to be an increasingly important user-facing API for the project, and it helps, helps unify the implementations, because it's really hard to misinterpret, or you kind of You know, have sort of… You know, go in different directions with implementations when we are all conforming to the same config spec.
And so, yeah, I'm just thinking about that, and, your, you know, your comment about a single top-level Boolean field to enable or disable this. We have this concept in declarative config called a include-exclude, and, it's, It's a list of… include glob expressions and excluded glob expressions. Each of those is an array, and so, you know, we use this in a variety of places throughout the config data model, and it's really terse to express something like, hey, include all, but it's really expressive, too. So that could be a pattern that we reuse, and there's prior art for that.
Nope.
Carlos Alberto Cortez 00:16:56 Okay, yeah, thanks, yeah, thanks for the point. Okay, let's discuss that offline, since my inbox is, It's finished. But yeah, thank you so much for that. Let's continue discussing the details on that one. I will take a look, especially to put the link.
Thank you. That's all from my side.
Tigran Najaryan 00:17:16 Cheer.
Thank you, Carlos. David, I assume you need no more than 30 minutes. We can do a couple more items before you do the update?
David Ashpole (dashpole) 00:17:25 Yes, go for it. I expect we'll be around 15 minutes, I think.
Tigran Najaryan 00:17:30 Okay, okay, let's… so let's do a few.
Is Ivo here?
Ivo Anjo 00:17:34 Yes, hello?
So, yes, on this OTEP, I've been, kind of iterating on the feedback, and I think I've addressed almost all of the feedback. There's a small discussion on the name of the protobuf package that we started today, but… Yes, I need more feedback or some help moving it forward.
So that's kind of it.
Tigran Najaryan 00:18:04 Okay, thank you.
Carlos Alberto Cortez 00:18:06 I would like to mention something quickly on that front. This, OTEP basically is, ePPF, oriented, of course, and, it's an optional feature, and Evo and his, and his SIG, or people around him that have been working with him, have prototypes, so, please take a look. As I said before, it's an optional component.
For SDKs, don't have to implement that. They can if they want to, so I think it's a good call.
Tigran Najaryan 00:18:46 Cool.
Josh, you have a few more entities?
Josh Suereth 00:18:51 Yeah, sorry. So, we have, we have a few PRs that are ready, and we have some SIG approval here for these now. So the first is the entity merge algorithm.
So this is basically how we're going to, interact with resource and entity together, and merge, merge these things. Please take a look.
This is ready for review. We have a bunch of prototypes. We've kept this, merge algorithm stable for quite some time now, in… throughout a bunch of our prototypes and working, so I'm pretty confident in it. But this is still a, you know, a development-level spec. It's not even alpha or beta yet. So, that's all this is. This just defines the merge algorithm. We'd like to get this in so we can start, making, development level, you know, experimental SDK proposals, so we could actually start putting this into SDKs to generate entities, as part of resource detection. So, this is… this is kind of a, critical thing for us to get through. You can look at the prototypes if you're curious, and then we're obviously going to clean those up and get those kind of production ready for the SDK submission.
So that's fun.
The second one is around the, event definition for entities, so this is getting more clarity on how we're gonna model relationships between entities, and then how we're gonna actually have an event that can be generated for you to actually synchronize state of the resources in your system and the telemetry that's being proposed.
So this one also, recently got approval. This one's ready for full review. I think that most of the comments are addressed in this already, but please take a look.
Because I think this one's ready to go.
And the last one is… actually has enough, approvals to be merged today, just given a heads up that I'm planning to merge it relatively soon.
So, if you have any remaining concerns on this, please let us know, but it definitely has enough approvals that I was planning to merge this. This is just a directional OTEP for how we would do, How we would use… Entities to allow multiple resources in an SDK, so you can record information in an SDK about something you're observing, as opposed to about yourself.
Cool, that's it.
Just looking for reviews and, progress.
Tigran Najaryan 00:21:20 Okay, thank you, Josh.
I think we have a bit more time, since David, you said you need only 15 minutes, so let's do a few more here.
This man here?
Sven Cowart 00:21:32 Yeah, I'm here This already got merged, the clarification, but Severn asked to join two weeks ago, I missed that comment, so I'm here now. I don't know if there's anything we still need to talk about in regards to this.
We'll clarify.
Josh Suereth 00:21:50 Oh, we discussed this in the entity SIG yesterday, and I actually didn't notice Severin's comment, sorry, but we.
Sven Cowart 00:21:59 Oh, no worries.
Josh Suereth 00:21:59 Yeah, we think that this was just, like, this is way better phrasing.
Sven Cowart 00:22:04 Okay.
Josh Suereth 00:22:05 Yeah.
Sven Cowart 00:22:06 Cool, so we're all good, right, Ben?
Josh Suereth 00:22:09 Yeah, yeah, yeah, you had more than enough approvals on this, and we, we talked about it in the, And the entity sig, just to confirm, and then we, kind of approved it and merged it live there, so… Apologies for not waiting for the sig.
Sven Cowart 00:22:23 No, no worries. Thank you for taking care of it.
Josh Suereth 00:22:26 Yeah, well, thank you for the change.
Tigran Najaryan 00:22:32 Alright.
Mattia?
Mattia Meleleo 00:22:41 Nope.
Tigran Najaryan 00:22:41 Yep.
Mattia Meleleo 00:22:42 I'm here, yep.
Yeah, I wanted to bring up to the attention this, OTEP, which, should, dictate how trace-to-profile correlation works between Obi and the BPF profiler.
So there is, one, question which is left to answer, which I think is, Yeah, this one, made by Ludmila, I think. But I think it, it belongs in some higher level document, and I don't know if I should address it here.
So I'm kind of, stuck with that.
Yeah, so the, the options are two. We either make this higher-level document, And dictate what are the priorities between, writers, Such as, for example, the SDKs or Obi.
And, yeah, the priorities for readers.
Or we can just close this hot up and, make just an internal agreement with the eBPF profiler, SIG.
And keep this implementa- implementation.
Liudmila Molkova 00:24:08 Yeah, thanks for coming and raising it. So, in the current shape, it's just the agreement between the BPF Profiler and OBI.
And I think for… what I think we should have in this pack is some vision on how the three correlate together.
And… in the current form, if you're not even considering the correlation with SDK yet, or it's obvious how it just feels… it's hard to review, because most of the spec people are not experts in eBPF, in OBO Profiler.
And… You don't get much reviews because it feels it's… it's not clear where it should be in this pack.
So I think my opinion would be that the best strategy is to write down how it works end-to-end with SDK in place, but if you're not there yet, if you're just experimenting with Zobi and Profiler for now.
It should not be an OTAP.
Mattia Meleleo 00:25:16 Okay, but this… so, my question is, this one dictates how it works between just OB and the profiler. So, SDKs don't, shouldn't implement this, because it's an eBPF-specific implementation. So, should this kind of high-level document be be another hot app, or where should I put this kind of context or information?
Liudmila Molkova 00:25:52 So I'm… I'm impression from the user perspective, I want my correlation to work, between SDK, OBI, and, profiler.
I, as a user, or as an implementer.
this is my priority. If you want a technical document that tells… that controls behavior between a BPF and Profiler, it can live in a BPF or Profiler, and they can link each other.
Mattia Meleleo 00:26:27 Okay, so… so the suggestion is to just close the OTAP and, get to an agreement with, with the Profiler team, and just implement that.
Liudmila Molkova 00:26:39 I'm kind of curious, did you consider SDK, like, the overall experience at all with this OTAP? Does it… would it work? Would it break anything in the overall experience?
For the end user.
Mattia Meleleo 00:26:51 SDKs, I, I don't think, Obi can, can work at, can work in the same way that SDKs do, because we need to share information in the same execution context, so the data shouldn't exit the kernel before the BPF profiler would read it.
Liudmila Molkova 00:27:15 Yeah, and say, if SDK started a span, or has a context, the eBPF, would telemetry emitted by ABPF be correlated to that context?
Mattia Meleleo 00:27:32 I think so, yes, I think we… I think Obi does that.
But, but this is, This is the way for Obi to share that context.
So, let's say that an SDK puts some context in an HTTP call, and then OB reads it.
And then it puts it in a map to be read by the profiler.
I don't know if… if I… if I'm clear.
Tyler 00:28:16 Yeah, hey, Lyudmila, I think, just to… I think you're… you've got a great idea, and the idea is that, like, you want the interoperability between, like, SDK context and Obi.
But Mattia's right in that it already exists.
And the fact that, like, if something in the SDK is already… well, technically, if the SDK is running, and exporting, Obi won't touch it, but if APIs are generating context across some sort of, like, API boundary, Obi actually already automatically, like, will understand that context as it's coming in. So that directionality already exists today.
There is future talk to talk about, like, telemetry overlap, and, like, that's a little bit of a separate issue, in the sense that, like, if the SDKs are producing telemetry and we want to supplement it, we're looking into something like that. But this is more about an optimization, with the profiler, given that both exist in the EUPF space already.
the profiler doesn't know anything about the context propagation, and instead of having it, like, try to recreate the entire pipeline that OB has.
if Obi's already, like, active on a request, we want to make sure that we're annotating with that active context for the profiler to, you know, say, hey, this profile is associated with this request, or something like that. And I think that's more what Mattia's trying to describe here, is specifically in the eBPF space.
Propagating the context, or, you know, allowing that context to be discoverable at that point.
Liudmila Molkova 00:29:41 Cool, so what you're saying that it already works, and this… just makes things better without breaking the channel between the SDK and Obi.
Tyler 00:29:51 Yeah, yeah, that channel does not… that won't be affected by this, no. The only thing that this will change is that the profiler will now be included in that. So, like, say Obi did detect some sort of, like, context that came originally from an SDK or something else, right?
the profiler today doesn't… doesn't see that, right? And so it will, if we can get this communicating on those protocol levels, yeah.
Liudmila Molkova 00:30:12 Yeah, so what do you think, Tyler, like, given your experience working with the spec, do you feel this change, this OTEP, would result in any change in the spec? Should we keep it here?
What is… Tyler 00:30:27 The reason… Liudmila Molkova 00:30:27 of having it here.
Tyler 00:30:29 Yeah, it's just that it was cross-product… a project at this point. Like, having it in the profiler and in here, there needs to be some sort of, like… there needs to be some sort of specification that both of them follow. Whether that specification is defined here, that was the original thought, but if, like, you're saying, like, there's a better place to store this, and we could… we can work at a different… Space as well, if that… if you think that this is just not scoped appropriately here.
Liudmila Molkova 00:30:55 No, I think if… if… there would be a short phrase describing that correlation works end, and there is already a channel. And if both SIGs are approved, then I wouldn't have any concerns having it as an ATAP. It's just nobody reviewed. That's why I suggested that it might not belong here, since nobody seems to Care enough.
Mattia Meleleo 00:31:18 Okay, I'll try to improve a little bit to the end-to-end flow explanation, maybe.
Tyler 00:31:26 I think also, Lyndel, one of the other things, like, right now we've scoped it to the Profiler and, Obi, but there's nothing really stopping other EVPF-like systems from hooking into this in the future, is the idea. But maybe from your point also, We could start by just defining something that works for us, and then if it did become something more universal, we could come back to the specification?
Is that reasonable?
Liudmila Molkova 00:31:51 It sounds reasonable to me, given that both profiling and OB are in… are not stable, and you folks will evolve over time.
We probably should put something in place as a… as a prerequisite to stability.
Tyler 00:32:08 That it would need to be included in the specification at that point?
Liudmila Molkova 00:32:13 That's a great question. I think we avoided putting things into specification that are not SDK, but I don't feel it's right. I wish we had something that's wider.
Tyler 00:32:26 Right, I agree.
Okay.
So, Mattia, I think what I'm hearing from this is that the idea is we can keep iterating with the profilerSig directly, and maybe find some sort of channel to communicate with them. We don't need to specifically have something in the specification to define this, is probably what it is, and we could probably even close this.
you can always close and reopen, like, there's nothing, a problem there. Yeah, that's true. Yeah, it's more just about moving forward on that one, yeah.
Liudmila Molkova 00:32:58 But if you folks would put approvals, from… sorry, green checkmarks, I'm… I'm discriminating, I'm sorry. I feel it could still be here if you find it beneficial.
And long-term, there should be something.
Tigran Najaryan 00:33:16 I see approvals from Profiling SIG here, right? There's a few, at least a couple here. I think, Tyler, the point you're making, though, is important. You want to have this somewhere, right? Even if it's not in the spec, because this involves two SIGs working on something that Needs to interoperate.
Yeah. Is specification repo the right place?
I'm not sure, but if you decide that it's not the right place, I… I think it's worth maybe moving it somewhere else, still having it somewhere, right, in one of the repos.
It's probably beneficial.
To have it written down somewhere.
Tyler 00:33:57 Oh, I… yeah, it absolutely has to be written down, yeah. Where… where I think that works best for… for the profiling in the OB community is… I don't… I don't know.
I might even say that it might be better to not have a specification, because it may, avoid some bureaucracy, but, like… Yeah, I think the end goal, though, that we were talking about, though, like, if this becomes more universal outside of just those two SIGs, like, it needs to be, I think, at a higher level than just, you know, in something like that, but we can probably start by iterating later.
Tigran Najaryan 00:34:28 Yes, exactly, and later you can move it to the spec repo if needed.
Tyler 00:34:34 Yeah, that sounds good. This is a conversation that does need, I think, some profiling people involved, too, though. I don't know if they're on the call.
Ivo Anjo 00:34:45 I'm here, although I can speak for all of the profiling seekers.
Tyler 00:34:51 Yeah, we've been talking a lot with Florian, Evo, but, like, if… yeah, maybe we can… we can discuss, a little bit more about, like, if… if you would be open to not having it in the specification, and having it in Obi's repo, or having it in the profiling repo, I guess is more the question.
Ivo Anjo 00:35:08 Yeah, I think that makes a lot of sense.
I guess, maybe the profiling seed would be the best place to put this, or just drop a note on the Slack channel, because I think it's a small thing, so maybe just dropping a note on the, What's the channel?
Tyler 00:35:24 hotel profile.
Ivo Anjo 00:35:24 Exactly, all profiles, I think we can probably settle that.
Tyler 00:35:30 Mattia, does that, sound good?
Mattia Meleleo 00:35:33 Yeah, yep, sounds good.
Thank you, Talia, for explaining better than me.
Tyler 00:35:38 I don't know if I did, but yeah.
Tigran Najaryan 00:35:44 Okay, let's move on.
Okay, let's try to do one more. Austin, how much time do you need for stable by default?
Austin Parker 00:35:53 Just, like, a minute.
Tigran Najaryan 00:35:55 Okay, let's go for it.
Austin Parker 00:35:57 Yeah, so I'm just asking folks… I see Trask did go through and add some comments, but… If folks could go through just this week, next couple days, do a final read-through, and any comments you have.
So that I can update this, and then it'll be… good to talk about next week at KubeCon, and hopefully we can… I mean, if you think it's in a good place now, just say, yep, good place for us to continue, and if there's specific things that you want to have addressed.
Add comments now, and we'll work on this week, and then we can talk about it next week, and… get it approved, and then move on. So that's my… I ask.
Unless people have specific questions right now that I can answer.
Go in once… Went twice… Alright.
That's all I have.
Tigran Najaryan 00:37:04 Thank you.
Okay, let's try the last one. No more than 5 minutes, please.
Lucas? Is Lucas here?
Lukas Hering 00:37:14 Yeah, yeah, this should only take a few minutes. Yeah, I just wanted to… So the Python SDK, we're looking… It seems like, we sh… we just want clarification on if we should start adopting the draft.
Trace Context Level 2 spec?
And… or if it should be behind, like, opt-in, until the spec is stabilized?
Daniel Dyla (Dynatrace) 00:37:47 Yeah, we discussed this, A few weeks ago in this meeting, maybe it was a couple months ago now.
I don't know, time's weird. But we also discussed it in the W3C group, Hi, if you don't know me, I'm Dan, I work on the W3C Distributed Tracing Group. So, We discussed this, in that group, specifically through the lens of… it's not a stable document, but there are projects like OpenTelemetry, which are… Depending on it, and our… De facto stable, even if not actually stable.
And… We came to the conclusion that we are comfortable Ratifying the document essentially as is, with no breaking changes. It's been… In the wild for, you know, this issue is opened in 2023.
There have not been changes or complaints, in a long time. The various… Complaints that we did have a long time ago were solved using, trace state and things like that.
Thank you to Josh McDonald.
And the reality is that, you know, regardless of what the policy says on paper, this specification can't be changed anymore. So it is… Going to be ratified, essentially, as is.
So… In terms of how the OpenTelemetry community wants to handle that, it's up to the community, but I would not Be overly worried about, stability issues.
beyond the fact that the W3C takes forever to do anything, It might take a long time to actually get it ratified.
But… Yeah, I wouldn't expect there to be problems.
Lukas Hering 00:40:00 Yeah, thanks for… yeah, thanks for that information. I think… I think there was also… I was looking at the… there was a Java prototype implementation, and I guess there was a comment there that… at least the major change in here is just the addition of the random trace ID flag.
To the, transparent header.
The big comment there was that it didn't seem entirely useful, so I don't know if there was still, like, ongoing discussions there.
that you need to be resolved. I'm not sure if anyone's from… the Java implementation year, but… Daniel Dyla (Dynatrace) 00:40:39 Yeah, we, I mean, that's… a question that, partially for the Java implementation, maybe partially for Josh McDonald, because the… the work there was largely motivated by work that he was doing, but I think he solved it in a different way.
There was some discussion in the W3C group around, do we even need a Level 2? Should we… Sort of, you know, let it… Die.
And that's another way we might go.
But… If that ever did happen.
we would at the very least reserve that bit. Right now, we're at the point where that bit is used in stable production systems, so we can't, change the way that it works.
So… the advantage of letting the idea of level 2 die would be to recover that bit, and now we can't. So… we can't use it in the future for something else anyways. We may as well move forward with it, but I believe that the… the actual functionality Related to sampling, Josh already handled in another way, I don't know if you're even using the bit, but there are other use cases that it enables as well, so I think we agreed that there is enough value to move it forward.
But, again, whether OpenTelemetry, you know, how OpenTelemetry wants to handle that is up to the OTEL community. Right now, the spec says to implement it.
Tigran Najaryan 00:42:20 Oops, sorry, guys.
Daniel Dyla (Dynatrace) 00:42:21 Go ahead, you guys.
Tigran Najaryan 00:42:21 Josh, if you can be very quick, or maybe we can take it offline, if possible.
jmacdonald 00:42:26 This is mentioned in the spec, everything Daniel said's true, like, it was… it was good enough, we should take it, we need that bit defined, and move on from here.
Tigran Najaryan 00:42:36 Okay, thanks, Josh. Please take it offline, because we have a topic to cover. David, do you want to take over screen sharing? Do you need screen sharing?
David Ashpole (dashpole) 00:42:45 Oh, I don't need screen sharing. I'll probably just… most of what I'm gonna talk through is written here, but I'll be here to… explain things and answer questions as well. So, I'll start… so the Prometheus Interoperability SIG, when we first started, was mostly about defining how OpenTelemetry collector, or how OpenTelemetry components, like the collector components and SDK exporters, were gonna do translation.
And now, by and large, that effort is wrapping up, and we often talk about other topics, like thing, like, what Prometheus exporters should be doing, or, a lot of us are involved in the open metrics.
Working group and stuff like that, so… work is largely winding down on the actual specs and stuff, which I think is a good thing. Finally, I guess. It's been 3 years.
But, so I'll cover what we're doing… Within OpenTelemetry, which is, we're focused on unblocking the 1.0 of the collector, and that means we need a stable Prometheus receiver, and thus a stable Prometheus to OTLP spec.
And we need a stable Go SDK exporter, which depends on the reverse spec.
we… we're pretty well through… we're pretty far through stabilizing the Prometheus receiver and the Prometheus to OTLP spec, and we haven't really started on… the OTLP to Prometheus spec, but it's largely… Largely, we've already implemented it everywhere consistently. It's just cleaning up language, and making sure that we dot our I's and cross our T's. So it's… it's a lot of small, small things, but that's moving along fairly well.
The one exclusion I wanted to call out is that we haven't really finished the design of how Prometheus is going to handle entities, and there's a number of, I would say, kind of tricky bits there. So, the target info metric will likely be, and the configuration and stuff associated with it, will likely still be in development.
when we kind of mark a lot of these things stable. And so we'll probably have to put that behind, like, feature flags and stuff in various places.
Any questions about… collector… Spec, or… Exclusions.
Tigran Najaryan 00:45:09 Can you, can you clarify why do we think that Collector 1.0 is… dependent on Prometheus receiver's stability.
David Ashpole (dashpole) 00:45:21 So, the Prometheus receiver is, after the OTLP receivers and exporters, the most used component in the collector. So it… it's just, when we originally, or when the collector folks originally did their list of must-have components, the Prometheus receiver was… was one of them.
Tigran Najaryan 00:45:39 Okay.
but not the Prometheus… David Ashpole (dashpole) 00:45:44 Not the Prometheus X.
Tigran Najaryan 00:45:45 Let's see.
David Ashpole (dashpole) 00:45:45 So, yeah. Yeah.
Tigran Najaryan 00:45:47 Okay.
Okay, and that's because primarily it's used for pulling metrics.
From everywhere, essentially.
David Ashpole (dashpole) 00:45:55 Lots of people run on Kubernetes, and everything in Kubernetes is Prometheus, right? So, it's kind of a must-have for real setups.
Do we have usage stats for collector components? I think there have been surveys done.
So, if you look at some of the past surveys and blogs, there's some pretty good, stats there.
Arthur Silva Sens 00:46:14 the way that Collector SIG came up with this list, like, we have a bunch of maintainers working for several vendors.
And we reached out to our internal our employer's data, and we looked what we… what is most used by our customers.
We anonymized everything, we just came up with the list of most used and agreed On this, I think the 7 most used components, besides the usual OTLP stuff.
Sorry, and I'm asking… I'm answering a question in the chat by Daniel Tillis.
David Ashpole (dashpole) 00:47:01 Cool.
There's no more questions there. The next topic I'll cover is OpenMetrics 2.0, which I'll admit is a little bit of a stretch for maybe this group, but I hope people are at least interested in it. And I think there's a lot of good things for OpenTelemetry users that are coming from this.
so… one call-out is that OpenMetrics isn't, like, its own separate thing anymore. It's now, under the Prometheus umbrella, which wasn't always the case. But this basically means that this is something that has been developed by myself and some other Prometheus maintainers.
Some exciting things in this format that… so it's a text format, and there's not going to be any, required special suffixes.
for metrics anymore, which is quite nice for, OpenTelemetry metric names and stuff.
histograms and summaries. People are probably familiar with the… Like, having multiple series for a histogram with underscore bucket, and underscore count, and underscore sum.
Those are now a single line in the text format.
With kind of a composite value type, which is a little bit more aligned with the OpenTelemetry data model.
It also is going to support native histograms, which we call exponential histograms.
And, we've changed a lot with how exemplars are handled in the text format. So now there's multiple exemplars on a single line.
And there's fewer requirements about how they are distributed.
Among… monks say histogram buckets and things like that. So, and it also requires a timestamp, which has been a bit of a pain For receivers and exporters for OpenTelemetry.
And we're gonna recommend some standardized keys for trace and span ID, which weren't current… weren't present in the previous version.
It's also gonna have start timestamps, which is another big pain point for people using, like, the Prometheus receiver.
And this will officially support UTF-8. The previous support in OpenMetrics was, Unofficial and, barred by the spec, but… People implemented it anyways.
And then I'll hand it over. Are there any questions about Open Metrics 2.0? And this is planned by the end of this month, so it's coming soon.
Tigran Najaryan 00:49:34 Do we… do we support the formatting, collector-receiver already?
David Ashpole (dashpole) 00:49:40 Well, it hasn't been… this is just the specification, it has not been prototyped or anything yet.
So, there's no… Tigran Najaryan 00:49:49 Okay. There's no implementation yet in the collector, or anywhere else? Is it just a spec, or there's a Prometheus implementation?
David Ashpole (dashpole) 00:49:57 It's currently just a spec.
Tigran Najaryan 00:50:00 Thank you.
Arthur Silva Sens 00:50:05 Okay, so as David mentioned, the SIG evolved a little bit. We've been doing a lot more stuff besides the working on the spec.
We have a bunch of Formitis maintainers joining the meeting… the meetings regularly.
And giving us updates about things going on in the Prometus ecosystem.
One of the things, I… we could mention is support for delta temporality in Prometheus. Without, The transforming into cumulative, which requires a holding state for every metric.
The main challenge is efficiently storing start time for all samples or data points in the OTLP lingo.
The work is very… pretty much, advanced, like, we, we already have, this… this thing running in staging environments in both Grafana and Google, results are looking good, and I think they will roll out this feature in one or two releases of Prometheus.
This is gonna… as usually very big, features in Prometheus, they roll out under, behind a feature flag.
And this is gonna be no different.
Another thing that we've been doing, we are exploring like, Prometheus has developed, like, thousands of exporters?
that, that are very popular.
And it's… I… I think this is a little bit confusing, like, in Prometheus Language R, An exporter is something that exposes telemetry, and in a hotel collector literature, this is… This is the receiver.
So we are implementing things that generate telemetry, which is equivalent to a collector-receiver.
So Prometheus has a lot of… receivers, which we call exporters, and we… we've been seeing a lot of people getting confused, if they should be using Prometheus exporters or hotel collector receivers.
And, we… we developed… we found a way that a Prometes exporter can work as an OpenTelemet collector receiver out of the box.
And we are making this possible through… we have done a POC already, we don't know yet how to, like, what to do with this thing. Like, we know it's possible, but now, should we do a Prometheus-branded collector distribution? Should we work with the collector SIG and, like… I don't know, promote using this Prometus exporters instead of using the collector receivers, or, like, use both. We don't know what to do with this yet.
There's also a problem that Prometheus exporters don't follow the hotel semantic conventions.
So this is… A problem that we'll need to, to solve in the future as well.
Let me take a break. Any questions?
Until now.
Tigran Najaryan 00:53:26 I assume some of these exporters have the equivalents in the collector. Do you know how many are actually unique, where there isn't an equivalent in the collector?
Arthur Silva Sens 00:53:38 It's hard to… it's hard to tell, because Prometheus exporters have been developed by community members outside of the Prometheus team.
And there are literally hundreds or thousands .
Tigran Najaryan 00:53:57 Yeah.
Arthur Silva Sens 00:53:58 Yeah, so it's hard to tell.
Tigran Najaryan 00:54:02 Okay.
Arthur Silva Sens 00:54:02 But… It is true that there is a lot of overlap, for example, Prometheus Node Exporter and the host metrics receiver. There is a very popular one, CubeSatmetrics, that overlaps with a bunch of different, Kubernetes-related receivers in the collector as well.
Tigran Najaryan 00:54:23 Yeah, I think it would be useful if there was a way to figure out which ones are overlapping, and maybe avoid bringing them in so that there is no confusion about which one to use.
But then, the unique ones.
Likely could be useful, right, for someone who does need to read metrics from that particular source.
Yep. And then, you're right, I guess the… the semantic convention, the lack of usage of the local semantic conventions. Since you're saying it's developed by the community, I'm assuming it uses whatever the person decided to use at the moment, so there is no… consistency, probably, in what the dimension names are. There's no single way for you to find out a translation between those into hotel semantic conventions. There's no way to do that.
Arthur Silva Sens 00:55:17 That… that is true. There is… Like, if these exporters adopt OpenTelemetry schemas, it doesn't need to be the semantic conventions, but the schemas itself.
there is other work going on in the Prometheus where Prometheus is aware of the schema versions.
And they… in the query… during query time, it can translate one metric from one schema to the other, as long as there is a… They'll, I don't remember the name, but, like, the hotel schema can tell how metrics are transformed.
Like, this work is solvable, but it will take a long time, and there's a lot of effort to make this possible.
Tigran Najaryan 00:56:08 Thank you.
Arthur Silva Sens 00:56:10 Yeah, no problems. Some other things that have been happening, the hotel secant user, it has a sibling working group in the Prometus, side. There's a UX and design working group.
And they are both working together to do an in-person survey at KipCon.
Most of those questions… most of the questions in the survey are related to the things that we all… that David and I just said today.
we are also doing some experiments, like, if people like some queryless experience, Prometus is heavily dependent on PromQL today.
And then, this UX and design working group developed some UIs based on hotel entities, sorry, based on hotel entities.
That don't require ProneQL at all.
Yeah, and we are gonna ask people around if they are… if they like this approach or not.
One last update is Hotel Communications SIG and myself, we're doing a mentorship through LFX.
Focusing on improving documentation of Prometheus and Notau interoperability.
we… the mentee that we picked needs to get up to speed with Promises and Hotel. It is a tech writer with little… Experience in the observability space?
But once she gets up to speed, she plans to work on blueprints.
Prometus-related collector components, and the Prometus server documentation.
And that's all for my site.
Jack Berg 00:57:54 Hey, thanks, David and Arthur. So, I'd love to see… the documents that are in the spec related to Prometheus, the compatibility document, the SDK, Prometheus exporter document, marked stable.
And I guess, like, I'm wondering, like, if there's… there's a lot of PRs and issues open about this, like, is there… is there any way you can focus our attention as, as, you know, approvers in the spec repo?
In terms of, like, what's… what's the critical path? What's the things that need the most attention the soonest in order to help you reach your goals?
David Ashpole (dashpole) 00:58:36 I think the blocker is mostly on our side right now. Obviously, like, when stuff gets opened.
Reviews are always appreciated. I… The only other place where we might need help would be… if we look at some piece of it and find that it's not implemented very widely, we might need to at least do prototypes in other languages. I know they go… I'm pretty sure they go in Java. Implementations are completely up-to-date.
Yeah, I think the rest of the implementations… I did go through, like, a year or two ago, but, There might be some work there.
Overall, though, I think the blocker's on us, just to open up the PRs to stabilize things.
Arthur Silva Sens 00:59:26 I al- I think… I think not all… the f- not everybody who joins these permit to Seek meetings understands the review process in the spec repository.
Like, they expect… some people expect immediate responses, some understand that they… it takes a while.
So if the review process is documented somewhere, I would love to share this with the group.
Jack Berg 00:59:59 So, there's probably a review process documented, but whether or not it's followed is something else entirely. It's like, what I find, practically, is that attention is scarce, and there's a million things going on, and, you know, so sometimes things get lost in the shuffle.
So I… I think… I categorize the Prometheus SIG as a spec sub-SIG. You know, it's a sort of topical working group that is working underneath the umbrella of the spec.
And the way that I've seen groups like that have success in the past is if Prometheus opens a PR to the spec.
The, the participants in that SIG should go and review and improve it, and even if they don't have green checkboxes, that's a good signal to the broader spec community that, like, hey, at least there's consensus amongst the Prometheus group.
And, you know, other people can jump in then, or you can explicitly ping people for their attention at that point.
Arthur Silva Sens 01:01:01 One follow-up question to that, Jack. So, to signal to the spec group.
that the Prometus SIC has, reviewed. Does that mean that we need to double-check the… that permit use approval?
We have a… We have a team group in GitHub for Prometes, right? And it's mostly out of date.
Jack Berg 01:01:25 Yeah, so, like, I don't have specifics, there's not, like, a formal process around this, but, like, just, like, maybe as a rule of thumb, if there's, like.
two… and we gotta go, we're at time, but, like, if there's, like, two to three approvals from the Prometheus SIG, and, you know, a Prometheus lead like yourself or David says, hey, spec approvers, come take a look at this. You know, I'm gonna see those approvals and be much more inclined to think that this has already reached consensus and just needs some additional eyes, and is ready for attention.
Arthur Silva Sens 01:01:59 Sounds good, thank you.
Tigran Najaryan 01:02:01 Alright.
Thank you all.
See you next time.
Jack Berg 01:02:04 See ya. Bye.
Arthur Silva Sens 01:02:05 Right.
David Ashpole (dashpole) 01:02:06 Bye, folks.
