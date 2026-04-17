SIG: Profiling WG
Date: 2026-04-16
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/dyRdF-HhaYC-21XBuh6Kf3B2i9S0KqZO3jwCimoJvgz-3b1CyuN8PLIlEGhUHjW7.qPf5gxAPrfh0F5Sf
============================================================

## Zoom Recording Transcript

Frederic Branczyk 00:02:15 Hello, hello?
NYC 46.24 Hell's Kitchen 00:05:01 Alright, I guess we're a couple minutes in, so we can get started. I'm trying to share my screen.
One second… Okay?
Oh, did somebody already put the action items here?
Or…
Florian Lehner 00:06:04 Yeah, yep, that was me.
NYC 46.24 Hell's Kitchen 00:06:06 Okay, cool, thank you, that's great.
So I'll sign in.
Okay, so the first item here is commenting on this pull request. I believe this was probably the… the sizes, right?
Yeah, so I… the feedback I left is, based on the discussions, that 32 max would probably work pretty well, but I still want to follow up with, some data, so we… I recently did some analysis of our data, I just didn't have time to write it up yet, so, the update there is, initial comment made, but I need to find some time, next week to actually share the data, so it's not just white-based.
And yeah, this week was a little difficult because I'm traveling, I'm in New York this week. I'll just put an update here.
And… Then, the next one is a key value unit proposal. I saw Florian sent me a doc with some initial ideas. Do you want to talk about it for a second, or…
Florian Lehner 00:07:36 Yeah, basically it's just a summary of what we discussed last week, with Tigran, the use of, unit string index, the use of, unit as a field in key value.
And, the use of… Units in semantic conventions in general.
And what's the impact of the… to the other signals, and if they are interested, the other signals are interested in a unit information attached to key value as well. So, it's just a draft at the very moment that's, that's why it's not shared that much. Yeah, I'll prepare this better, in a better way, larger format for next.
for next week meeting, I would say.
NYC 46.24 Hell's Kitchen 00:08:32 Sounds good, yeah. I think my feedback from just having briefly looked at it is that I think we need to be clear why we need it for profiling. I think when we propose it, we should write this down, because I think it's largely because it's a PPROF heritage, and I think we need to convincingly explain that we cannot make our PPROF round-trip stuff work without, like.
maybe with a hacky other way of doing it. So I think I would like to at least come up with one attempt to, like, hack units on as, like, additional attributes, or sort of describing the other attributes, or something like that, so I think that's… that would be the next step there. But yeah, we will… we'll find some time next week, Florian, to sit down. I see Alexi's hand is up.
Alexey A 00:09:20 Question for the unit field, will we allow it to… Both value and also by reference as well, like we do for, for the key…
Florian Lehner 00:09:36 Yeah, at least my idea would be to have it also as a reference, at least for profiling. For the other signals, reference will not work.
Alexey A 00:09:46 Only by reference, or, like, support both ways, like we do for the value and for the key?
Florian Lehner 00:09:53 I would say, similar to key, with the rule, similar to key, that you cannot set both. So, either you have, key set or key string index, but not both.
Alexey A 00:10:09 And I think we also said that by reference, at least right now, is only for profiling, so will it be documented the same way? That's okay.
Florian Lehner 00:10:16 Yes, yes.
Yeah, that's at least the idea I want to bring out in the future, but it needs more polishing, definitely. Didn't have much time last week. This week was also… felt quite good with CVs, and so, Didn't find too much time, sorry.
Alexey A 00:10:38 Yeah, yeah, yeah, yeah. Mostly, mostly just trying to understand the constraints, and that we… we will… I could see that this will restart some of the conversations of, like, oh, like, why is this for profiling? Should this be more universal? But hopefully we can separate this, because… Yeah, they're kind of separate.
Florian Lehner 00:10:57 Yeah, makes sense.
NYC 46.24 Hell's Kitchen 00:11:02 Any more thoughts on this? Going once, going twice? And, let's move on to the next item. Frederick was gonna create a meta issue for tracking SDK implementations. Any updates on that, Frederick?
Frederic Branczyk 00:11:19 Yes, I created it, like, half an hour ago. I had linked it there, yeah. Oh, sorry, there you go.
I… I think at least Jonathan should probably fact-check what I put in there, in there regarding, Java, I think everything else I did to the best of my abilities. And then, I don't know how you want to go about this. Should we just, ping… all the maintainers of each of the SDKs, or how do we go about this? Should we be opening the issues in all of the SDKs? What do you think?
NYC 46.24 Hell's Kitchen 00:12:04 I don't know if there's, like, a meta-seq for, like, SDKs that is not, like, just SDK-specific. If somebody knows, let me know. Like, if there's, like, a nice forum where we could, like, introduce the idea. If not, then I guess… creating issues in each of the SDKs, Repost makes sense, maybe asking them specifically, like, for meta discussion about, like, hey, adding profiling to SDKs in general, that we would welcome them to join our SIG meetings if they want real-time communications about it, or otherwise comment on this meta-tracking issue that we created, so we don't end up with, like, 20 threads discussing the same conceptual questions around profiling integration into SDKs, so that, that might be, yeah.
important to note when you open issues, but I think, yeah, opening issues seems fine to me.
Frederic Branczyk 00:12:55 I think I can take a subset of this, or if you're cool with me kind of spamming exactly the same issue on each of them, I'm okay with that. But, like, otherwise, I would say let's split this up, but, like.
NYC 46.24 Hell's Kitchen 00:13:10 I think it's gonna be the same issue, you can literally just copy and paste.
Frederic Branczyk 00:13:14 I can take care of that as a next step.
NYC 46.24 Hell's Kitchen 00:13:15 But yeah, you can maybe, maybe before we spam them all, maybe you can send a traffic message in the, in Slack or something, so we can give it a quick thumbs up.
Frederic Branczyk 00:13:24 Sounds good.
NYC 46.24 Hell's Kitchen 00:13:26 I… I can add one thing, is that there's someone from Datadog, Scott, that's already talking to the REST SDK folks.
that I know of.
And, the whole, like, opening the issues in the SDKs, I think to remember there was some reference of a mechanism for doing that in the specification repo, so I'll just check and chat in the chat if I find it.
Frederic Branczyk 00:13:51 Okay.
NYC 46.24 Hell's Kitchen 00:14:19 Okay, sounds good. Any, any more thoughts, questions here?
Frederic Branczyk 00:14:26 Just one more, one more, one more thing. If anybody opened this, you probably have already seen this. I realize we haven't actually… full, like, merged and agreed on the threat, context stuff, but I put it in there already because it'll require support in all of the SDKs as well.
And, you know, I feel like we've come to the point where we all agree that something like this is gonna happen. Just, you know, some details may still be figured out.
NYC 46.24 Hell's Kitchen 00:14:57 Yeah, I think this is an SDK folks who will have lots of questions on that, where we don't have all the answers yet, including… I actually put it on the agenda for later, but maybe we can briefly talk about it.
as we make a list of things we need to figure out for, like, going to beta at some point, I think having APIs for, correlating, trace context to, profiling, is… gonna be needed, right? Like, we expect the SDKs to actually, every time a span is created, to set, like, make some calls, and I think we need to define the API.
for that, I don't know, Ibo, if you've already started thinking about this, or… No. I've explicitly been kind of avoiding that, and I've been thinking, like, oh yeah, this is the mechanism, we'll see the APIs later, but that is definitely going to be needed, so maybe it's time to start thinking about it.
Yeah, that makes sense. So maybe, maybe… we don't have a… go ahead, go ahead.
Frederic Branczyk 00:15:52 maybe I'm thinking about this too naively, but I feel like… This shouldn't need a new API.
Like, this is something that the… SDKs do internally, right? Like, custom labels, as in additional context, those obviously need APIs, but just attaching the trace ID and span ID, that seems like it should be an implementation detail of the SDK itself.
NYC 46.24 Hell's Kitchen 00:16:21 I suppose that's a good point, yeah, maybe unless we do, like, custom attributes, We don't need to think of it as an hotel API.
Frederic Branczyk 00:16:34 Additional labels definitely do.
NYC 46.24 Hell's Kitchen 00:16:37 Yeah, like…
Frederic Branczyk 00:16:38 And as, like, I mean, I know at least some of us in the room have already used this within Go, and, you know, our customers use this with Rust and other languages extensively today already as well. That's, you know, not the trace or span ID, so we definitely need to figure that out.
But yeah, for trace ID and span ID, I would hope that there's no need for that.
NYC 46.24 Hell's Kitchen 00:17:04 Yeah, I think you're right, actually, on that. I think we still need to spell that out clearly for the SDK maintainers. That's fair. There's, like, two levels of support here, and we were probably initially just gonna ask for the first one, which doesn't require an API. And I guess then we can argue whether or not it's on our critical password stable to figure out the attributes API for custom attributes.
Well, custom labels, whatever you want to call them.
Frederic Branczyk 00:17:30 Probably not.
Like, if we're talking… protocol stability, I feel like it's probably not important to figure that out.
NYC 46.24 Hell's Kitchen 00:17:47 Yeah, because on the protocol level, there would just be additional attributes on the sample, I guess.
Frederic Branczyk 00:17:53 Yeah.
NYC 46.24 Hell's Kitchen 00:17:53 Where we have that. Okay, makes sense. I'll take some notes.
Okay, cool, that makes sense, and then I think I can actually remove this… point from later. Any more thoughts, questions on… on this?
Okay, then I'll move us on to the next one. Jonathan has a PR for the moving the original payload to the dictionary. I think we said that we are not going to merge that yet, but… I guess, yeah, Jonathan, is Jonathan here?
Done.
Jonathan Halliday (IBM) 00:19:29 Yeah, I think it's probably better to hold off and make any breaking changes altogether at a later date. I don't know if that really needs to stay on the open action items until it's Merged, or if we just, punted off into done, and hope we remember to come back and take the Do Not Merger label off it at some point.
NYC 46.24 Hell's Kitchen 00:19:54 Yeah, no, I think that makes sense to me to hold off a little bit before we make breaking changes.
But would you like people to review and comment already? I guess that still makes sense, right?
Jonathan?
Jonathan Halliday (IBM) 00:20:14 Yeah, I mean, you can… you can tick it now. I don't think it's gonna change substantially.
So if it's… if it's reviewed now, then it's straightforward to merge it at a later date, I guess.
But equally, there's absolutely no urgency.
NYC 46.24 Hell's Kitchen 00:20:34 Okay.
I'll capture some notes.
Right.
Alexey A 00:20:46 It also looks like we now allow multiple… payload bytes, effectively, because I just noticed that it's repeated, original payload indices, so it can be multiple… Because previously it was just one, but now… I missed that part that probably I should… NYC 46.24 Hell's Kitchen 00:21:11 Yeah.
I don't think that's necessarily a bad idea, but I'd love to hear from Janus on if there was, like, a specific use case that you had in mind when you made that change.
Jonathan Halliday (IBM) 00:21:22 I just made it as general as possible. I don't think there's a strong use case for… multiple files.
Where?
Where you get splitting and combinations.
It tends to be more in… File management situations where you're… You've taken a bunch of recordings and you want to, like, zip them together into one giant recording.
You know, archiving purposes or whatever, but… We probably don't need it on the wire, but it costs next to nothing, so… NYC 46.24 Hell's Kitchen 00:22:01 Yeah, I think if we do that, then maybe it's a little odd to just, like, do two repeated… fields here, maybe it would actually make more sense to…
Jonathan Halliday (IBM) 00:22:12 Create an object, and… Yeah, repeated message at all.
Yeah, I considered that. That has the added advantage that we can preserve additional information in that message, like the original file name might be of interest.
Currently, it's lossy. You can send the file itself, but you can't send the name of the file, because there's nowhere to put it. So having a message that contained that might be useful, potentially.
Don't really know.
NYC 46.24 Hell's Kitchen 00:22:48 Yeah, I actually think the filename is a useful thing to have.
So, I would probably gravitate, like, if we do agree that it could be useful to have multiple original payloads, I think having a message with also filename would be my preference. I don't know how other people feel.
Florian Lehner 00:23:11 Should we… should we generalize it even a little bit more and say, instead of a filename, just payload comment? And comment can be any string that describes this payload?
can be either how it was collected, it can be a file name, whatever. So, a comment could be quite flexible for the use case, as payload is anyway not in the scope of the profile signals.
It will be probably that the collector knows what will be expected on the backend, and vice versa.
Jonathan Halliday (IBM) 00:23:48 Yeah, I think file name's a little bit of a special case, in that… Probably the reason you want to transmit the file in the first place is so you can use some tool For example, if it's a JFL file, you might want to use JMC.
On the receiving end.
And those tools work in terms of the file system, so chances are you're going to want to unpack the… The message and write the file back to the file system in order that external tools can find it there and know what to do with it.
So having the file name is kind of useful for that purpose. I mean, you can… create an arbitrary file name on the receiving end, but it's kind of harder to look at a string comment field and Guess whether it's a reasonable file name or not.
NYC 46.24 Hell's Kitchen 00:24:33 I think, thinking about this for another second.
What we're talking about sounds more like attributes now, so why not have a payload where you can have multiple attributes on it, and just the bytes?
And then we can do semantic conventions for stuff like file name, as well as, moment as well.
Seems like people are nodding, so… cool, Ryan's giving me some subtle.
Does that make sense to you, Jonathan, as well?
Jonathan Halliday (IBM) 00:25:01 Yep.
NYC 46.24 Hell's Kitchen 00:25:04 Okay, cool. Will you iterate on it, or should somebody else?
Jonathan Halliday (IBM) 00:25:11 No, I can… I can push a… Message type for that.
NYC 46.24 Hell's Kitchen 00:25:18 Okay.
Awesome, that's great. Cool.
Any more thoughts on this? I once… And twice… And three times we are on to the next item. Alexi, add duplicate and orphan checks to the performance checker.
Alexey A 00:26:08 No progress yet, still need to allocate some time and get to this.
NYC 46.24 Hell's Kitchen 00:26:17 Okay, then similar here, or this one?
Next item.
Alexey A 00:26:30 not done, but I will… I will do this shortly. This one is… is really small, I just need to do this.
NYC 46.24 Hell's Kitchen 00:26:36 Okay.
Alexey A 00:26:36 I was… I wanted to do this before the meeting, but didn't get to this, yeah.
NYC 46.24 Hell's Kitchen 00:26:42 Yeah, and of course.
Thanks.
This one, I… for me, also no update yet, but I still want to do it.
I'll have more bandwidth starting again next week, so I think I can get this done before the next meeting. Then we have 3 items from Christos. Is Christos here?
Florian Lehner 00:27:10 Not as far… not… no, he's not… sorry, he's not here, sorry.
I think the PRs are still in review. They are… NYC 46.24 Hell's Kitchen 00:27:22 pop…
Florian Lehner 00:27:22 stated, or at least approved by members of the SICK.
So it's up to the specification.
group, to… Finally approved them and merged them.
NYC 46.24 Hell's Kitchen 00:27:38 Okay, I will… Notice here… Okay, seems this one is a little different.
Oh no, wait, is this the same links that I just opened?
Florian Lehner 00:28:24 He looks like a fancy crystal.
NYC 46.24 Hell's Kitchen 00:28:26 what's gonna update this, right? Like, we had a discussion on… Did he do that?
Florian Lehner 00:28:32 Not as far as I know… There was an update a few minutes ago, but I think, the… Last… last meeting, we talked about having the… dedicated messages in the proto, and keep it in the proto, and having the mermaid diagram in this, markdown.
I think this, is still work to do.
NYC 46.24 Hell's Kitchen 00:29:02 Okay.
That makes sense, yeah, I remember the conversation now. Okay.
Then, any… anybody has more thoughts on this, or… If not, then we could go on to Alexi, figure out what to do with the older OTAP. I think the decision was we can just update it, saying it's outdated. Did you have a chance to do that?
Alexey A 00:29:31 No, I actually forgot about this, this actually is a good reminder. I'll take a look.
Florian Lehner 00:29:38 I think it still depends on the work from Christos. We can't just, link to the work from Christos once this is merged.
So we might be, might be blocked, until this is done.
Alexey A 00:30:02 The documentation ones, or.
Florian Lehner 00:30:05 Yes, yes.
I'm not sure the 4932 or 4965, which one of both, but one of them needs to land before we can update this old tab and point to the new documentation.
NYC 46.24 Hell's Kitchen 00:30:24 Yeah, makes sense to me.
Okay, any more thoughts on this?
If not, we are… ready for the regular agenda items. We only have two, items from Ebo right now. If anybody here has, other things they would like to discuss today, I think we might have time on this meeting, so feel free to add more things. But yeah, maybe Ibo can take away the… the process context item here? Yes. So, this first one is kind of a… We were expecting it to be a small one, and it turned out to not be as small as we were expecting, which is… We have the… for the process context, we have a protot format, there's a proto, and we were thinking, oh, yeah, maybe it makes sense for the proto to live in OpenTelemetry proto.
And then when we talked about, to it, to the specification SIG, the specification SIG went like, oh no, OpenTelemetry Proto is OpenTelemetry OTLP protocol.
Not the pro… like… prototops related to OpenTelemetry, and maybe… so maybe this doesn't, this doesn't belong here, so why does it belong?
And, I guess we might have put our hands… in somewhere, like, because there's a few people from the city thinking, oh yeah, maybe this is the beginning of a new thing, so maybe we should create a new repo, should create a lot of new things, and I was like, this is a 20-line program. Hello. So, I don't know, like, I am… I'm a bit unsure… where to proceed here? We could kind of say, okay, maybe let's just put the proto on SIG profiling, is the simple thing we could do.
Or, if y'all think it's kind of worth trying to figure this out, in terms of, okay, the protos for… let's find a place for the protos, I can keep working on this one.
It doesn't block us. It would be nice, I think the intention was to have a nice centralized place for the proto to live.
That, everyone could pull easily, and the problem with having another repo and whatever is that now there is no longer any easy hotel mechanism to easily pull in the proto. But yeah, I just kind of wanted to raise in if anyone has, like, ideas or thoughts on this.
Did we consider putting it in the spec?
It is in the… the spec itself has it? Does it have the photo as well, or… It does, it's inlined in the spec, but we were like, okay, now we copy-paste what's in the spec outside of the spec, so that we can easily, we can easily consume it. Like, inside the markdown is not the easiest place to consume it. Oh, yeah, yeah.
Florian Lehner 00:33:28 Yeah, I take the blame on this, My idea was.
NYC 46.24 Hell's Kitchen 00:33:35 Which was a good idea.
Florian Lehner 00:33:37 My idea was, hey, have it just in a proto-repository, and just use the infrastructure that is already there for publishing, and Distributing everything and having it in one place.
Didn't turn out… That well, on every end?
Yeah, the problem I see, if we move it to Profiling SIG, for example, is that we have to run this infrastructure on our own.
Not only for… for a single language, but all languages, and that's… that would be my biggest concern. Here in the proto repository, the… all the… All the definitions are close together, and we used a common definition for the attributes in this proto.
And that's why I think it's the best to have it in Autel Proto, but, yeah, I'm wrong, obviously.
NYC 46.24 Hell's Kitchen 00:34:38 I mean, did we get a firm no from the right people, or is this still open for discussion?
Oh, Tiklon?
Florian Lehner 00:34:49 Yeah, that's a hard no.
NYC 46.24 Hell's Kitchen 00:34:52 Hmm…
Florian Lehner 00:34:56 So we have both. We have supporters, and we have people that are not in favor of this.
My intermediate thinking is, hey, land it in Proto.
It is marked as alpha, or development, Everything but not stable.
And we can still move it to a different place if there is infrastructure that provides this… all this kind of… publish for all these, SDKs and… Things… Yeah.
But yeah, I wanted to follow up on this and miss this.
NYC 46.24 Hell's Kitchen 00:35:39 Okay, so if I'm reading this correctly, like, Tikron is, is, somewhat opposed, not completely, like, he's open to extending the scope of the repo, and Josh seems to be supportive, right? So, I think this is not a dead end.
just… we need to continue pushing on. I think from what I heard, continue to push to land it in the proto… repo still makes the most sense to me, so if we can get, Tikron and Josh to sort of align with what we want to do here in Wyatt, then I think that would be ideal.
Florian Lehner 00:36:10 Yeah, yeah, I just wrote it down, but I will follow up, and I just got lost on my plate, sorry.
NYC 46.24 Hell's Kitchen 00:36:19 No, me as well. I've been a bit unresponsive on this.
Let's do an update here.
Okay, so we all agree that, like, to basically continue pushing on getting it in the proto. Okay. Absolutely.
Frederic Branczyk 00:36:38 I, I, I do, I do wonder… I don't know, maybe, maybe we… I should have brought this up earlier, but, like.
These are just, like, key-value pairs.
do we really need this to be proto? Like, we can represent this at… Pretty easily without any sort of… NYC 46.24 Hell's Kitchen 00:37:03 Yeah, we… we've… we've been… we've been around on this one. That was the beginning.
I think the intention is, I think the intention is that this will be… having the proto means that it's kind of easier to combine… like, I think if we look at it as, like, the thing for the profiler, I think the profiler doesn't really care, but, having, like.
the protobot format is a way for everyone to, like, have… like, to have many consumers and many writers, and avoid, like, diverting too much, while still have a format that can easily evolve and what have you. And if we have a two-custom format, we were kind of worried in the beginning that Next time we want to change something, it's going to be super painful, because there will be, like, any implementations of the custom format that we need to fix, whereas, like.
And libraries pulling in the proto means we can, like, tweak the proto, and Protopuff already has good mechanisms for evolution, so that's kind of how we… we ended up here.
Frederic Branczyk 00:38:11 I think I… I think I sort of agree from… like, I sort of understand where you're coming from, from the… process perspective doing this, but actually, I do worry a little bit about the consuming perspective from the eBPF profiler here.
Because we do actually have to live with a bunch of limits, right?
And we can't arbitrarily evolve this either.
Because at some point, the, like, eBPF verifier is gonna tell us, no, you've, like, made this… schema is so complex, I'm just not gonna load the program to… Read this.
NYC 46.24 Hell's Kitchen 00:38:55 I, like… I agree with you, and I will clarify one thing. The proto is only used for the process context, and the process context is the thing that kind of is expected to move slower and get updates, but not very fast. And the thing that's expected to be never right from eBPF, it's kind of mostly read from user space, where we have… Oh, okay.
parsing mechanism.
Frederic Branczyk 00:39:19 Okay.
NYC 46.24 Hell's Kitchen 00:39:20 Like, for the thread context, the thread context does… not use Proto, and the thread context does use the more specific, more clamped-down format for all the reasons that you're saying. So, that's how we kind of said, like, okay, for the process, there's, like, a… we don't have as many restrictions, so let's do, like, a nicer thing, and optimize for nicer and evolution, and whatever. And for the thread context, we are limited by all of the things that you are… that you are raising, and so for that one, we are not suggesting to use a proto.
Frederic Branczyk 00:39:50 Got it, I understood it was meant for both, okay.
NYC 46.24 Hell's Kitchen 00:39:53 Yes, it's a bit conf… that… this is the reason why we end up, like, with a different one for either, is… Yeah, yeah.
Frederic Branczyk 00:40:02 Begs the question, should we be doing different things for both? But, okay. No, I think I understand why it's less dramatic here then.
NYC 46.24 Hell's Kitchen 00:40:14 And, I mean, it is kind of nice to use these, like, existing messages, like resource and p-value with, well-described behavior in open telemetry, rather than, like, representing these concepts in a new way. So, I think for process context, I think Rodo makes sense, and for, yeah, for the thread context, technical, realities dictate that the proto does not make sense.
Frederic Branczyk 00:40:40 Yeah, okay.
No, I understood.
NYC 46.24 Hell's Kitchen 00:40:43 Go ahead. I was just going to say, like, the next topic is about the threat context, and I feel like that's part of, like.
we've… I am going to try to push to convince everyone that not going proto in the threat context is the right thing to do, but I… that has come up sometimes in the discussion, and I think we will need to convince people that we shouldn't.
Frederic Branczyk 00:41:14 I guess then what I'm saying is, if… if that becomes a point of contention, I think we should potentially be flexible on saying.
Maybe we make both of them not… not proto.
I guess I'm just saying, right, like, if, like, that ends up allowing us to move forward, I think we should be open to that idea.
NYC 46.24 Hell's Kitchen 00:41:37 Yeah.
Frederic Branczyk 00:41:40 Like, I could see how, you know, people would want consistency one way or another.
NYC 46.24 Hell's Kitchen 00:41:48 And I guess, like, at least the good news is both formats have, like, a version or a mechanism to indicate what they are, so we could have both at the same time if we really wanted to. I'm not sure if we want, but… There is possibility to evolve without being, like, a really big, confusing thing, so yeah, we have some space there.
Yeah, I think I agree with your comment, Frederick, on being flexible there, like, if it's gonna be a huge undertaking to… make the hotel stakeholders happy with us putting a simple proto file somewhere, then maybe it's… as much as I like the reusing the messages, I don't think it's a hill I would die on.
So… I think poke a little bit more on the proto stuff with the upstream, and if it needs much more than poking and turns into a whole thing, then, yeah, go that way. Sounds good.
Hmm, okay.
Any more thoughts on this?
Going once, going twice, and number 3 means we move on to thread context. Yes, so, I think now that the process context has been merged and whatnot, and we are trying to, starting to talk with the SDKs and whatever to implement it.
We want to do the same thing with the thread context, hopefully it will not take as long.
I would say, to mirror the process, how things worked last time, like, I think the SIGs and whatever want to see that we've talked with everyone, and everyone is happy with this.
So I would say, like, people from here, give it a pass. This is, like, we've discussed this, we… we've gotten feedback from a bunch of people, but I think to be able to show the SIG that we have discussed, we want times, like, we want green checks on the PR, so give a pass on the PR.
Share any thoughts and concerns that you still have there, and then, like, yeah, either give a green check, or, like, leave a note on what you're thinking and what we should still be looking at, so that we kind of start tracking the progress there in terms of, like, oh, here's the thing that we're still discussing, and here's the people we're going to still talk about, and we kind of centralize the discussion there, so that We can use the PR as a centralized point to show the SIG, oh, yeah, we've already synced with everyone, we've already, talked about all of the things with everyone, and everyone is happy, and we have a bunch of green checks.
Sounds good to me. Yeah, I agree. Everybody should review who has an interest in this and ability to make the time for it. Yeah, any more thoughts or questions?
Yeah, thanks for all the work on that.
And that brings us to our potentially last agenda item for today, Florian's RC for adding an interface for custom probes, which I guess this is like an eBPF profiler?
Florian Lehner 00:45:35 This is a more EBPF profile topic.
Looking at the agenda, we used to have.
question around GPU profiling and memory profiling, but this was removed.
And I think the person that wrote it already left the meeting, so… That's unfortunate, but I'm lucky. Yeah, GPU profiling, memory profiling, and all these kind of topics. I have written, an MVP, I would say, of making custom probes.
That enables us to get memory providing, GPU profiling, out-of-memory providing, what you can just think of.
And, the idea is to restructure a little bit, the EVPF profile in a way, that People can contribute more easily, with… without the complexity of package tracer that we have at the very moment.
And, also enable people to have, simple, or… Complex configuration as they needed.
In eBPF Profiler, we received a bunch of bunch of requests on… limiting down profiling on a specific application or a PID.
And, it was turned down in the, in the past.
And I think custom probes would, would allow us to enable such use cases in the future more easily.
Yeah, so, overall, That's an idea how it could be done.
don't set the naming in stones, it's just an idea. But I would… if there are resources, I'd like to get feedback on it.
I think, also people that are forking at the moment.
UPF profiler, they would have a more easier way, to say, hey, I want A custom probe that works in this way, that attaches to whatever.
And, wants to trigger something. Yeah, so that's… Maybe a side note for people that are not using the upstream version, but more a custom fork.
Yeah, I'm happy to get feedback.
Frederic Branczyk 00:48:04 No, like, I haven't looked at this in particular, but I see that Tommy already, commented on this. I did want to say that we have actually started work on something like this. As a matter of fact, I don't know if everybody read the GPU profiling post we published sometime last year. We… We essentially did this, with USDT probes, that's how we implemented our CUDA profiler. That's also what I was gonna say to this person who has left the call. Also, just once again, you know, this person probably would have wanted to hear this. We… we do intend on eventually contributing the CUDA profiler we created, back. It's just something that's very fast-moving, a lot of unknowns, but we do… we do plan on eventually contributing this back.
And yeah, I guess my biggest point here is that if we do go down this path, let's make sure that we think about USDTs from day one as well, and not just U-Probes.
Florian Lehner 00:49:16 Yeah, USDDs can be supported already. And, with this custom U-propes.
I think we could solve auto, also.
a maintenance issue, I would say, on the EB ProF, eBPF profiler.
Everyone that is contributing knows there's a… time lag, I would say, and, custom probes could enable People to be responsible for… Custom parts more easily.
So, that would… Could also spread a little bit more to work on more people's shoulders.
Frederic Branczyk 00:49:52 I want to call out one specific thing here, why I mention USDTs.
Because specifically, like, parameter extraction with USDTs is quite important, so that, you know, a random example that we've put together as kind of a prototype before is that you can profile the object store range reads that you do, right? And you put a USDT probe onto your read range call.
and you want to see how many bytes you're reading from those code paths, right? So it's not just that we want to count the executions, we want to actually specifically extract a parameter of that USDT probe.
I realize it's a… it's not terribly difficult, but, like, not a huge difference, but I just wanted to have called it out.
Florian Lehner 00:50:38 That's already implemented in the MVP. I see it really as a value that, custom probes can not just trigger something, but also extract something and report it back, to the reporter and have it directly in the protocol. So the full chain is already covered in this.
Frederic Branczyk 00:50:57 Very cool.
Florian Lehner 00:50:58 It, for me, it was also important to not just say, hey, I want to trigger something, but also I want to trigger selected value for memory profiling, for example, it's important to have also the amount of bytes that was allocated free or requested. And, yeah, that's why I want to have values as a As direct values reported down back to the reporter, yeah.
Frederic Branczyk 00:51:25 If there are no other topics that people want to discuss, I have a lot of.
NYC 46.24 Hell's Kitchen 00:51:29 Yeah, you can go to the second, I just want to also comment before we move to the potentially next topic. I do not have the technical depth right now to, like, review the PR for the technical questions, but I very strongly agree with the problem statement and the use cases that are enabled by this. So… I can sort of leave a light review just supporting that from that direction, and one of my colleagues, Nicola, maybe we can ask him to take a closer look on the technical side. He's been doing some contributions, maybe he has some opinions.
Yeah, so… sounds good. But yeah, thanks for doing that, Foreign. It looks really good.
Frederic Branczyk 00:52:12 Now I lost my train of thought.
It'll come back to me in a second.
Right.
Okay, so, yes, memory profiling is really interesting, like, allocation profiling is really interesting here, but it does beg the question, is this actually low overhead enough, or is there actually something we should try to trigger? So, like, this is an idea that's been kind of… swirling around at polar signals for some time, like, I feel like there is space in the kernel to have probes that, like, probabilistically fire. Does that make sense? Right? Like, because allocating or, like, profiling every single allocation that happens is likely too expensive, right? Which is why, like, memory profilers tend to only sample every 500 kilobytes or something allocated, right? I wonder if there's something that we can do here you know, even if it's long-term, even if this requires, like, kernel patches, but, like, if there's some… something we can kind of start a conversation around here, and I think, Florian, you know this space better than me. For me, it kind of stops at the eBPF layer. I think you've… you've dived more into this kind of stuff, but… Yeah, that's a question that we've been kind of thinking about for some time.
That is what you're thinking.
Florian Lehner 00:53:44 Yeah, I have some opinion on this, I think there will be no general memory profiling. If you look at memory allocations in Java versus Python versus Go.
Frederic Branczyk 00:53:59 Of course.
Florian Lehner 00:54:00 They are very different, and .
Frederic Branczyk 00:54:01 Allocators differ dramatically. Like, this makes perfect sense to me, but, like, even the idea of putting a probe on whatever analog calls in all the allocators, right? Like, that's never gonna work out performance-wise.
Florian Lehner 00:54:21 I would argue it… It does, but this does not give you the full picture.
Because if you do LD preload and, custom memory allocation.
And these are the tricky parts I think we need to solve, and for these, we need for these, we need something like custom probes, and that's also the motivation for me to say, hey, I want to have custom probes, that I can say, hey, I know I have this allocator library, attached using USDs, UPROBES, whatever, and getting these insights. From a kernel level, I think we can just get an high-level overview of the memory requests and allocations, because usually, from, at least from the languages I know, The runtimes try to use, or try to allocate larger blocks, rather than small blocks for everything.
And, yeah, having just the large blocks, not sure if this is sufficient for every case.
Frederic Branczyk 00:55:29 I'll let Yvo speak first.
NYC 46.24 Hell's Kitchen 00:55:31 Yeah, I was going to say that, we have, in the past, Datadog has, but it's kind of in permanent beta, and we're basically going to deprecate it in favor of the eBPF profiler, but we had, like, an earlier profiler for the whole machine that had, like.
allocation capabilities. And, specifically for malloc and 3, but this… the way we ended up doing it is that we kind of had two components, so… We actually did need to have something that lived inside the application, and then reported to the, like, wherever. So there's multiple ways of doing this. I was going to say that we are thinking about, like, experimenting with trying to make this fit in the VPF Profiler, and maybe submitting it upstream, and we might have someone that will have, like, a timed project to join our team to work on this.
So, yes, we are very interested, and hopefully we might have, like, soon, like, someone on the Datadog side experimenting with this activity.
I see Alexi's next, and I want to go up to Alexi.
Alexey A 00:56:44 This is a bit more general about sampling techniques, and maybe we can have one day, More elaborate conversation about that, but if we… One thing we found multiple times is that, if sampling is applied, it's… it's much better to do sampling in terms of some kind of weight, rather than just diffraction of events. For example, here, if it's, like, allocating something, then sampling in the number of bytes will produce much more statistically consistent results, because… If you sample just by the number of events, and they represent different… and they can have different weights, then if you got unlucky and picked something with very large weight, and then And then you unsample that, like, a particular session can just look very weird.
Sometimes it's hard because you don't know to wait until the thing actually ended. Like, for example, in case of contention, for contentions, for example, we do sample in the number of contentions, and this produces weird results, but that's because you don't know for how long you would be contented until you actually got the mutex, and so, yeah, things like that.
NYC 46.24 Hell's Kitchen 00:57:58 Yeah, that makes sense. Plus one to, like, just a comment on sampling techniques. I think, sort of, on the… On the use case thing, like, whether we're targeting, profiling of, like, Java, Go, or Python memory allocations versus, like, libraries that are maybe written in C or Rust, I would say if we can get visibility just in the, like, normal.
Use case where a library is directly calling malloc in free, I think that would be big, because a lot of, yeah, Java, Go, or Python applications actually use native libraries, and then those allocate, and that's the source of very many problems that people have in practice. So I think even if we just nail that use case without, stepping into the turf of, what the runtime profilers currently do for memory profiling within the runtimes, I think that'd be great. I'm also not opposed to extending into that, but I realize there's a lot of problems.
In terms of the overhead question, I guess, I mean, the real problem with the… approaches we see right now is that we sort of rely on the kernel to actually transfer control from user space to the kernel, like, every time, like, an allocation happens, and that is just not going to be feasible. Like, if we do a… a mode switch on every, allocation event. That's gonna be too costly, so we need to figure out some way to mix the, that transition only… like, basically the sampling decision needs to be in user space, is what I'm trying to say. And when we decide to sample then, sure, we can go to the kernel and do the actual collection of the sample data there, but, yeah. But maybe… stuff we could do there could also include, like, contributing upstream to, like, JMalog and TCMallog and other libraries to just, like, have code paths and can enable this. It's just maybe… there are kind of no ops unless somebody is looking for them, but, like, there's actually a function that doesn't get inlined that we could hook into. But yeah, I don't have… all the answers there, but, like, I think this is a challenge that we need to address.
Frederic Branczyk 01:00:04 Since you mentioned it, sorry, Alexei, are you… do you still have your hand up, or did you… do you have it up again?
Alexey A 01:00:13 sort of stale.
Frederic Branczyk 01:00:14 Okay, we, we actually already started this conversation, on me malloc.
Since it's a popular allocator in the Rust, ecosystem. And with JEMalloc, this already exists.
NYC 46.24 Hell's Kitchen 01:00:30 Okay, and is it, like…
Frederic Branczyk 01:00:34 Go ahead.
NYC 46.24 Hell's Kitchen 01:00:34 Do you need to, like, configure it for JMalloc, or do they always do, like, the sampling already, even if there's no… nothing enabled as an option?
Frederic Branczyk 01:00:42 So, you, you, you need to configure it?
But you can also enable it through an environment variable.
NYC 46.24 Hell's Kitchen 01:00:53 Okay.
Which… Well, it's not great for the eBPF profile, because we can't change the environment of the running process, right?
Frederic Branczyk 01:01:02 I can… I can look up the… whether the, like, sampling trigger might trigger anyways, I'm not 100% sure about that.
I'm gonna say it probably doesn't, because, you know, JMULG, as you probably know, has a heap profiler built in, but you do need to enable it, so I'm gonna guess that the entire code path isn't called if it's not turned on explicitly.
NYC 46.24 Hell's Kitchen 01:01:28 Yeah, but I think we could try to influence, like, the upstream allocators to basically just, hey, always call this function, when the sampling decision would dictate, like, to sample this thing. Don't never inline that, we can put a hook there, maybe even a user-defined static probe, or whatever it's called, where we also get the weight, as an argument. And then, when they have their profile enabled, they call the rest of their machinery, but if not, it's just Almost a no-up in terms of cost.
Frederic Branczyk 01:01:55 it does get tricky. Like I said, we've actually spent a bit of time on this with Mimalog. Like, even if we do, have a USDT in Memall directly, there is a problem, at least for heap profiling. Allocation profiling is not terribly difficult, but with heap profiling, it's difficult because you need to make sure that the eBPF profiler has run since before the program has started, otherwise you don't have accurate statistics since… Since launch, which is a little different with… You know, in-process instrumentation.
NYC 46.24 Hell's Kitchen 01:02:33 But…
Frederic Branczyk 01:02:34 personally, excuse my language, but I kind of hate the idea of, like, J.E. Malloc being able to unwind the stack is, like, a horrible… horrible crime against humanity, in my opinion, that the allocator knows how to unwind stacks, but… it's just my…
Florian Lehner 01:02:53 Nope.
NYC 46.24 Hell's Kitchen 01:02:53 I don't.
Florian Lehner 01:02:54 As we run out of.
NYC 46.24 Hell's Kitchen 01:02:55 I don't know if you will get… get people disagreeing with that.
Doesn't sound like an unpopular opinion to me.
Florian Lehner 01:03:03 Yeah, but as we run out of time, I'm happy to see discussions, and that's all the things I want to enable with the RFC.
That we get to this point. That's the motivation, yeah.
NYC 46.24 Hell's Kitchen 01:03:15 Yeah, I think as a group, we fully agree on that direction, like, it would be awesome if we could just have a profiler that can capture memory as well as it can currently do CPU, that'd be great.
Yeah, but yeah, we are indeed at time, so, thank you everybody for, all the work and all the good discussions, and, yeah, have a nice local time. See you next time.
Frederic Branczyk 01:03:36 Enjoy New York.
NYC 46.24 Hell's Kitchen 01:03:38 Thank you. Thank you.
