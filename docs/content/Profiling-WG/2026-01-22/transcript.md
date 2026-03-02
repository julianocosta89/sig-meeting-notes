SIG: Profiling WG
Date: 2026-01-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Brennan Vincent (Polar Signals) 00:01:47 Good morning, or afternoon.
Florian Lehner 00:01:53 Hello.
Frederic Branczyk 00:02:10 Hello, nope.
Ivo Anjo 00:02:36 Hello.
Felix Geisendörfer 00:04:54 Almost 5 minutes in, so…
I think we could get started. I will be sharing my screen so we can see the agenda.
Right?
So, first of all, welcome everybody, and thanks for showing the profiling SIC.
And what we usually do is we start reviewing previous action items, and then we go through the regular agenda. Today, we seem to have a pretty light schedule ahead of us. Ibo has an item. If anybody here is like, oh, I joined today to be, like, discussing this thing or that thing, now is a really good time to add it to the agenda, and so we'll make sure to cover it once we've worked through the previous action items.
on that front, I guess there's also some good news that things look,
much more small than before, seems like our to-do list is shrinking, but I will copy here the things that I think still need discussion, and we'll go through them.
Doom?
I think one of them was checked. A P-Prof converter, I think, can take out.
I think the red.
Florian Lehner 00:06:11 Sorry, I will move it to archived as it's done.
Felix Geisendörfer 00:06:15 Oh, that's great, thank you so much, and I think, yeah, those two can probably also
Be moved out of… The… the line here.
So, yeah, maybe for…
efficiency's sake, I'm gonna… I think Alexi's here, at least I see his name on the list, so I will move his items together and get us started by talking about
Writing a profile signal, protoconsistency check tool, initial PR sent, I think last time this was pending on refuse. Alexi, let me know if there's any updates.
Nayef Ghattas 00:06:49 I think he left a comment on the doc to say that he'll be 20 minutes late.
Felix Geisendörfer 00:06:53 But he already put his name there in anticipation of his arrival. Okay, then we will just put his stuff to the bottom, we might come back, or when?
Then I think the next item would be…
Review Process Context Propagation OTAB. I suspect that is Evo who could be talking about it. I was planning to do another review of that, which I haven't gotten to yet, but I will shortly. Evo, any
Things to share here.
Ivo Anjo 00:07:27 Yes, so, I've gotten, green, nice checkmarks from Christos, Florian, and Naev.
Thanks, thanks for that and the feedback. So, if anyone else could kind of give it a pass and give it a green check, I think if we have a bunch of green checks from our side, it's easier to make the, I think, our case to the specification seek that we're all in agreement and we like this, and can you please consider this?
and merge Zapier.
Felix Geisendörfer 00:07:57 Basically, I forgot, missed one name here, somebody.
Ivo Anjo 00:08:00 I think it says 3, yeah, 3.
Felix Geisendörfer 00:08:01 Oh, sweet, okay, okay.
It's green, gave a green check.
Christos Kalkanis 00:08:13 Ivo, just a question, Ivo, have you started reaching out to SDK, hotel SDK people? Because, I guess these are the most important ones in terms of stakeholders for this.
Ivo Anjo 00:08:25 Yes, so I did reach, I think back in December? Or maybe it was the end of November, something like that, and I did speak with folks from the Java,
from the JavaSig, and got some feedback on it as well. That's when I experimented with, like, auto-instrumentation in Java. Not in auto-instrumentation. Basically, plugging this automatically in Java and whatnot, so people seem, like, okay-ish, like, kind of lukewarm.
But they were a bit like, okay, but is this going forward or not? So I'm… yeah, we need to break the loop, so hopefully the plan will be now to reach out to specification and the other SDKs and ask them to give this a pass.
Christos Kalkanis 00:09:06 Okay, cool, thanks.
Felix Geisendörfer 00:09:14 Yeah, I would say getting at least a few of the language 6 to explicitly approve these plans would really help. I think once we have traction there, I think that's the critical step forward to getting this to the next stage. So thanks for raising that, Christos.
Yeah, anybody else? Fuse, questions, comments on this right now?
No, going once, going twice, no takers, and we will move on.
to our biggest blogger for getting to Alpha733, the resource attribute saga. Florian, do you want to update us on the latest?
Florian Lehner 00:10:04 Yeah, I think there's consens at the moment between, Josh.
Tigran and Bokhtan about how it should be done.
The how it should be done is, implemented in the PR, so the PR is updated.
The only person that approved it at the very moment is Felix, so I'm hoping for approvals at some point.
to move this forward, the most important approvers will be Josh Chiker and Bogdan.
But at least, I think we are all on the same page at the moment.
Felix Geisendörfer 00:10:42 Yeah, I think it would be great still to have more, clear SICK buy-in, because that's something that TC members are also looking for before they give their approvals, so please, please, please look at this. This is our biggest blocker for getting to Alpha.
Just for everybody else, Florian, if I remember correctly, the decision here was to go back to the kind of initial way you had the PR, to add a new field to the any value, to have a string reference, rather than having a dedicated
any value refs thing, which, yeah, I like that better as well, but,
I guess, yeah, for everybody who hasn't followed that too closely, we are back to where we started, and now we have consensus around it, so hopefully this can move forward. And yeah, thanks everybody who has pushed and nudged on this. I know Christos, I think you did some more nudging and pushing as well.
And Florian, for all the work on this. This is gonna be very exciting once we have this merged and landed, because then I think we can literally just pull the alpha trigger, almost.
maybe… maybe looking forward, we could add an agenda item, for Alpha, like, maybe all those things we are… we're getting right now.
Yeah, anybody else with thoughts or comments on… on that pull request, and the resource attributes dictionary stuff?
Christos Kalkanis 00:12:04 Yeah, I just approved it myself.
Felix Geisendörfer 00:12:07 Nice.
Christos Kalkanis 00:12:07 I guess it's fine, like, the way it is right now, even though it's specific to profiling, maybe both then will come back to us at some point and say, okay, why don't we make it more generic in the sense that, you know, maybe other signals could use it if they wanted in the future or whatever. But I guess the pressing concern here now
assuming this… this is done, is to… to do the proof of concept, right? Where we, work
With the references.
Josh?
Josh Suereth 00:12:39 Yeah, I was just looking at the PR,
Didn't you need the key to also be in the string dictionary?
Felix Geisendörfer 00:12:48 I think so.
Florian Lehner 00:12:51 The key is the element that was added to any ref, any value in the once element, and that's the key that can be used as a lookup in the string table, the profiles dictionary string table.
Josh Suereth 00:13:04 No, what I mean is, you're touching any value, but then there's key value, as well, in resource, that has raw strings.
And do you need the key, part of key value? Let me, let me find a link.
Florian Lehner 00:13:19 I think the key uses any value.
Josh Suereth 00:13:23 It does…
Florian Lehner 00:13:24 Alright, thank you.
Josh Suereth 00:13:26 Not for the key.
Florian Lehner 00:13:27 Yeah, for the key. I'm not sure if you want to open this discussion.
With the progress we made, we can'.
Josh Suereth 00:13:36 So, I mean, what is…
Florian Lehner 00:13:39 For me, it's just a small change to edit.
Josh Suereth 00:13:44 Yeah, yeah, I think it's a small change that. So, I have two questions on this,
And I don't want this to take a long time, and I apologize for how long this has taken, but I think we're finally past the initial gut reaction of don't do it, and we're down to just, like, how to do it, right?
Alright, so…
first of all is just, if you're… if you're trying to reduce the duplication of resource and strings, I think you do need to have the key be a ref. Like, in, like.
the technical solution you're looking for in this, key value thing, there's a string key and any value-value. I think you need to have key somehow be
in your string dictionary. I would recommend… you can do it as a second PR, like a follow-up, if that makes sense, but I think you're going to want and need that to get the reduction that we were talking about in size, because the number of duplicated keys will still be high.
And you're probably gonna get more of a reduction from doing key over value.
Right? Like, we know.
Florian Lehner 00:14:48 Yeah, I see the… I see the point. With the key value, and the key… in key value, I think the risk is we cannot use, one-off at this point.
For one of string or string reference as a key, because this would… is a hard break for the protocol.
So it would be a dedicated field.
And we have the same discussion as we have now for any value. Any value is a little bit simpler, because we just add, the string reference into,
One-off field to integrate a one-off field.
And so there can be less conflicts, than we have with, if there are… if there is a dedicated field in, key value for the, string key.
Josh Suereth 00:15:43 Yeah.
Florian Lehner 00:15:45 I would love to.
Tackle this as a follow-up, to be honest, just to…
Have a little bit of progress.
Josh Suereth 00:15:52 that I'm… again, I'm fine with doing it as a follow-up, I just… I think you'll need it, so I don't… how do I want to phrase this? I don't want you to lose the attention of Tigran, Bogdan, and I until that's resolved, because we want to… we want to…
do this quickly, right? So, I would just make sure that you're aware of that. The other thing that I,
Yeah, there's different ways to solve this. The other thing I'm curious about is, do you need any other dictionary support or just strings out of the value field? I think you're not allowing complex attributes in value the way OpenTelemetry is. Is that correct?
Florian Lehner 00:16:33 I would say so, yeah. Also, we have this dedicated attribute, in… in use in the profiling signals, so key value unit.
Which is also different, which is also different to, key value in OTEL.
But this is also a separate discussion, as we rely on this additional unit field.
And, most of Auto does not.
Josh Suereth 00:17:01 OTEL has, like, in metrics, unit is… further out.
Right? And it's… it's a dedicated thing. We, you're… but you're doing multivariate data. So, like, I still see profiling as a mix between metrics and multivariate… sorry, multivariate metrics, and then, its own thing.
Okay, the…
The reason I'm asking, we in the entity SIG and the SEMCOM SIG had debated trying to put restrictions on resource.
So that we would actually completely disallow complex attributes, in the ecosystem. And if you experience them, you would, like, consider it an error. So that when you send resource from profiling, you could basically rely on the fact that it cannot be complex. We didn't do that.
It's just, this is another…
piece of fuel to the fire, which is why I wanted to check on that, because that's another discussion happening that we could align with. Okay, anyway, I took a quick look at it. I have…
Minor knit comments, but I'm going to approve it after the knits are taken care of.
Florian Lehner 00:18:12 Yeah, I will be super fast with this.
Christos Kalkanis 00:18:16 So, Josh, since we have you here, what would be your preference for adding a reference to key value? We would just add an extra field to the key value itself, or do we would…
Creating your message?
Josh Suereth 00:18:26 So, my preference is different than Bogdan's, and I am less strong-willed than Bogdan, so I think you're gonna have to find out what Bogdan wants here, because I'm just gonna defer.
I… I would prefer that… that we… like, what I would have liked to have set up is you actually have a different resource message to begin with in profiling.
It's a different proto.
And the collector abstracts between the two different protos. I think that gives us all the flexibility we want. You could actually have yours only have,
you could have your support dictionaries, and we could have the collector generate code that blends the two and serializes appropriately. Not a problem, right? That, for some reason, isn't viable. I'm not sure why,
So, but that… that… if you want to know my personal preference, that's what I'd rather have. So we would have, in resource profilers.
profile.
Profiles? Sorry, I'll enunciate it eventually.
We would have, like, a profile resource, and a profile resource would have a, like, key-value ref.
That the string is a ref, and the values are refs.
And that's what you would use, and the collector would abstract between that proto and the other stuff. And there'd be a set of inconsistencies in OTLP, but honestly, I think this is better for consumers of OTLP generally. It might be harder in the collector, but better overall for the ecosystem. That is my preference.
We had a discussion on this, and Tigrin and Bogdan kind of convinced me that maybe,
maybe I'm overemphasizing some of the things I care about, but they also have very strongly held opinions that they have to do it a certain way, so I'm… I'm deferring, effectively. Otherwise, I think it would be another 2 months of this discussion, and it's been, what, 6 months? It's been a while.
Florian Lehner 00:20:23 Yeah, makes things… makes sense. Yeah, I think I really like to separate the discussion between any value and the key value,
Just to stay focused and… have little progress on this. Yeah.
Felix Geisendörfer 00:20:38 Can I quickly throw out that the version we benchmarked had the key as a ref, like, you had a field for the.
Christos Kalkanis 00:20:46 Yeah.
Felix Geisendörfer 00:20:46 We're keeping around.
Christos Kalkanis 00:20:48 Yeah, that's also visible in the comments. Like, if you open… if you see the comments on the pull request, it's… the key rep is there.
Felix Geisendörfer 00:21:01 Yeah, so I think we really need to bring it back, but I'm also okay with just doing this in another cycle if it feels like you're worried about getting this much. We do want this much. We all want this very much, so that makes sense.
Florian Lehner 00:21:17 I think we could…
Felix Geisendörfer 00:21:18 Go ahead.
Florian Lehner 00:21:19 to show a little bit of progress, I think it would be best for us if we can get this any value change merged.
and bring the changes into the AutoCollector before we merge the changes for the key value for the reference. So, because then we have all the infrastructure for this references already in the collector.
So, adoption and experimenting and all these phases will be much simpler than it is at the very moment, where we have
A hard time, getting these things with this reference started with the, with the collector.
Yeah, that's why I would prefer, saying that we,
Go on with any value now, and build up on this, with the key… with the reference and the key value.
Felix Geisendörfer 00:22:10 I mean, I'm not gonna work on the collector stuff, but it doesn't immediately sound true to me that it's going to be less effort to do it as a separate phase in the collector implementation. I think it might be easier to do all the dictionary ref stuff in one go. I don't know.
Christos Kalkanis 00:22:24 Yeah, I agree with that. I think we should do those in your… like, what we need to avoid is going to the collector, doing work there, and then having to redo parts of it. Let's wrap up. We know that Bogdan, his preference is also to resolve key-value unit, right? So we have to… we have two things we need to resolve now. Key-value unit is one with Bogdan, the other one is key refs.
So let's clarify and resolve both of those before we do anything with the collector or the proof of concept, because we don't want to go back reworking and redoing things that we've done.
Felix Geisendörfer 00:23:02 Yeah, do you feel strongly about this, Florian, or would that work also for you?
Florian Lehner 00:23:06 Yeah, we'll be fine.
Felix Geisendörfer 00:23:09 Okay.
Okay, yeah, I think that in terms of PRs, we don't care if this lands in, like, two separate PRs or in one, but I think we do want both of these in before we go to the collector experiments and implementation experiments. So let me just…
Capture this consensus.
Florian Lehner 00:23:37 For an organizational question. Currently, we have a breaking change of the profiles protocol in Autel Proto main that is not released yet. Do we want to ask for a release of OTLP so that it will be pushed to
020, I think it is, the next… would be the next version, that we can say with…
0.21, there will be, this, this reference-based changes, so…
They would be separated, and we could… Could iterate faster.
Where it's town.
Felix Geisendörfer 00:24:16 Having one… one proto-release without the key refs and one with.
Florian Lehner 00:24:21 Nope.
Felix Geisendörfer 00:24:22 I don't… to me, I think having it both in one release seems easier, but…
Florian Lehner 00:24:28 Okay, just wanted to hear your preference. At the moment, we have a breaking change that…
Yeah, just wanted to separate them.
Felix Geisendörfer 00:24:39 Yeah, I don't know if anybody else feels… I don't feel super strongly about having two proto-releases. I mean, it does give us a little bit more flexibility, but then, at the end of the day, it also means somebody has to cut two releases, and I think we're pretty sure that we don't want the in-between state to actually be, like, yeah.
Christos Kalkanis 00:24:54 Yeah.
Felix Geisendörfer 00:24:54 22…
Christos Kalkanis 00:24:55 I agree, yeah.
I would keep things in monarchies.
Josh Suereth 00:25:07 Yeah, I'd prefer not to have two releases as well. If you need, like, a branch release of some sort, where we tag
the proto-release, and you can pull in, like, a, you know, a beta or something where you can try it out incrementally. Cool. But my… I do have some fear that once Bogdan wraps his head around the key ref problem as well, that the decision around value ref may change.
I… I don't… I…
I still don't think this is sticky until we have his approval. So, let's… that's why I prefer not to do two releases. And I'd prefer to make sure we solve the key ref problem.
Florian Lehner 00:25:51 Yeah, I will follow up with both.
Felix Geisendörfer 00:26:07 Okay, yeah, I… hopefully, he won't change his mind.
Fingers crossed for that, I'm hopeful. And then, yeah, it would be great to have both the key refs and the value refs.
Anymore.
Thoughts on this item?
Jonathan Halliday (IBM) 00:26:23 Do we have a version of…
the Profiles Proto that has been modified to use these proposed common changes.
I'm trying to wrap my head around why we need this QRef thing.
Because Profiles Proto, as it stands, uses…
key value and unit, which already has the RIF.
Felix Geisendörfer 00:26:44 This is on the resource level.
So this is not, like, the resource is a common element in the protocol, which is used by all the signals, and that's why we're having all these difficult discussions around it, because it does, to some degree, impact all the existing signals.
And yeah, so it's unrelated to the, key-value unit thing.
Jonathan Halliday (IBM) 00:27:05 Right, so you don't… you don't want it for direct use, you want it only for indirect use?
So it's going to exist alongside key value and unit.
Felix Geisendörfer 00:27:14 Yes.
I guess.
Christos Kalkanis 00:27:18 Yeah, that's what we have right now. Bogdan has expressed a preference for actually, being uniform, so the key value in unit maybe would go away, and then we'd reuse the same attributes as the resource.
Like, I don't see that happening with things as they are right now, but I don't know, maybe we can bridge that gap by talking to him.
Felix Geisendörfer 00:27:47 Okay.
Yeah, thanks for the question. Any… any other questions or thoughts?
going once… Going twice…
Three times? Okay, then, yeah, let's hope we can make some progress on this async, as we discussed now the direction.
Did Alexei join? I don't see all the people in the…
Alexey A 00:28:14 Yes, I, I'm here.
Felix Geisendörfer 00:28:16 Perfect timing. Welcome, and we are now moving on to your action items. Do you want to give an update here? Are you still waiting on refuse? What's the status?
Alexey A 00:28:26 So… the first one for the consistency check, yeah, I think I would like to get more feedback, because I think I saw an OGDM from Florin.
But, like, more eyes would be useful.
And,
And I need to finish the, there are some, like, optional checks that I still need to add, which are, the consistency of dictionaries, which is, orphan entries and,
And duplicate entries.
I haven't added that yet. But I also kind of, like, I wanted to submit this code first, because otherwise I will just keep filing… filing things up on top of what I already have, and it's… it's just, like, at some point it becomes, like, oh, I want…
Like, I want this to be… to get reviewed first.
And the sample type order, default sample type, I just… I just need to get that done. I… nothing is blocking, but I haven't sent it yet. But, I will… it's…
Yeah, I've been…
I wanted to send it before this meeting, but didn't get to that, but hopefully over the next couple days, I'll do that. I don't think there's anything complicated we discussed, and we have a document that documents what we want to do there, so it should be…
Pretty simple.
Felix Geisendörfer 00:29:48 Okay, cool, makes sense. Anybody have, thoughts, questions, comments on these two items?
Going once… Going twice.
Then, I think this has, concluded our review of the previous action items.
We can obviously come back to anything if you have a thought while we're talking about the next stuff.
But yeah, then our main action items for today is gonna be EVO giving some more thoughts on thread-level context sharing, and I think I added up an item here to maybe think a little bit more on what else would be required for alpha, what other steps,
to go forward with that. Ivo, you're, you're up next. Go for it.
Ivo Anjo 00:30:36 Yes, me, let me… Can I share my screen? I think it's kind of easier if you don't.
Felix Geisendörfer 00:30:41 I think you can. Let me… Give you the powers.
Ivo Anjo 00:30:48 Wait, I'm not seeing the button… And this.
Felix Geisendörfer 00:30:55 Minus in the middle.
Ivo Anjo 00:30:58 Shift.
Felix Geisendörfer 00:30:58 Command S, keyboard shortcut.
Are you on Linux?
Ivo Anjo 00:31:09 I am.
Okay, I see it, sorry. Please, please ignore whatever I was not seeing.
And…
Okay, cool. So, I've put here, I dropped here a link to, this document, so we had, like, this is the document where we, in the past had, like, some notes on the thread-level context sharing.
And I have, put here our, in, as a second tab, our kind of proposal tab for, doing the thread-level context sharing.
And, so, like, yeah, I would like to, to ask for feedback from folks. I can get, give a, I don't know, a 5-minute intro, which is that…
A bit like the elastic and polar signals implementations that we've discussed in the past. This is… basically uses a thread local variable and TLS desk format.
It's not format, like, using the TLS desk descriptor for, for finding it.
And then there's, like, a few extra distinctions. I think the key distinctions are, one.
that, this… the thread-level context kind of announces itself and some of the details of how it's set up, using the process context. So, instead of you, instead of you having to discover them, like, separately or something like that, you can kind of, like, read the process context.
And then, if the process context says, oh, there's a thread context, then you'll be able to do the next steps. You don't need to have separate versions of the code or, like, probe two different things. So that's one of the big differences from the previous implementations.
The other difference is that, the format of the record, so the format of the record is kind of a mix between… we started from the polar signals format, but we kind of stole a few ideas from the elastic format as well.
So the main difference is that we've made, a few fields, like,
First-class citizens, so they get, like, the specific representation in the thread local structure, and then you can kind of add, like, more stringy-like arguments.
And, this, to avoid kind of pointer chasing, we kind of just have, like, a big, a big continuous buffer, and we just kind of, we just place.
all of the values there. And there's, like, a key difference is that the keys are not stored in the record. The idea is that the keys are identified by an index, and we kind of have a way to declare the keys
in the process record. So you go in the… you go in the process record, and you say, like, okay, these are the keys I'm going to use, 0, 1, and 2, and then to avoid, like.
repeating those strings again and again, or, like, having to do with them, like, you don't need to do that. Here, you kind of just…
Include, like, key number 0, like, the length for the string, and then you put the bytes there.
And, that's kind of mostly it. The rest is just us trying to make it pretty in the, kind of, like, for, the hotel, specification repo. And right now, there's a Rust Reader and a Rust Writer, which are linked here at the top.
And, we, we are working to, to, to, to add the, to kind of implement this in the full host, the eBPF profiler. We.
We are kind of, like, slightly late on that, but we plan to have on that soon, and we plan to have, like, a Java implementation soon as well. And… and yeah, basically, I created the Google Doc because I think for…
Collaboration, like, in this group, I think it's kind of easier to go with the Google Doc, and once things calm down, I'm thinking I will turn this into the PR in the…
Hotel specification repo, but yeah, let me know if you have any thoughts on anything.
And that's my, spill.
Christos Kalkanis 00:35:27 Yes, sounds good to me. I like that you used the process record to save some of the work for the third context.
Brennan Vincent (Polar Signals) 00:35:38 So we talked about this a bit on the document, but, can we talk about this, max record size, and maybe some…
other people have an idea how this should be handled. So…
Yeah, like you said, this is…
polar signals… well, in parka, we have something similar to this feature already, and…
Rather than having, like, a max…
total size for the record in bytes. We have…
Like, a max number of label pairs, and then within each label pair, each key and value can be…
Up to some maximum length.
Which… The reason we did it like that is because, obviously, in the eBPF code, you can't have…
like, unbounded loops, you have to, you know, have hard-coded maximum, like, numbers of iterations for all your loops. So, we'll…
like, the eBPF side
Regardless of whether you encode it that way or as, like, a total size of the buffer.
We'll have to impose some maximum value on the, like…
record size, or on the number of keys, whatever. So,
Yeah, what I was wondering is, should we make that… Actually, part of the…
Like, hard-coded as part of the protocol, rather than being something that the process…
Communicates to the agent like this.
Given that, like, it'll… like, if the agent communicates something that's higher than what the profiler can handle, then it's not gonna work anyway, and…
If not, if you need to use less space on that, then why not just support, like, the max that the profiler can handle in any case?
Scott Gerring 00:37:36 I think there's kind of… Sorry, I haven't joined this before. I'm Scott, nice to meet you all.
I think there's kind of… Two things there.
The first is that if we let the rider communicate that it's going to use less of a buffer beneath some arbitrary ceiling, that's probably good from a cost and efficiency perspective. So maybe in the spec, we work out a hard ceiling and say it has to be under this
But the writer can still communicate that it's gonna send less.
So the reader can profit from that. The second is that I think you can still degrade gracefully if
you can't read the entire contents of the buffer, because we have this fixed chunk at the beginning with the core, trace, the W3C stuff, essentially.
If you get that, that's probably also already useful in many cases, and you can kind of gracefully drop attributes that are further down. Like, it's not desirable, but it's still workable if you can't get the whole way through, is my point.
I don't know if that's a helpful insight.
Brennan Vincent (Polar Signals) 00:38:34 Well, that's definitely true. I mean, if you… Yeah, you can…
Just stop reading things and report what you found.
Which is what we do already, by the way.
Yeah, another sort of tangentially… well, another sort of related point is that,
is it actually necessary to always have the buffers be the same size? Because… yeah, I know, you mentioned… we talked about this, I think, privately, but,
you don't want people to have to make multiple, like, BPF probe read user calls, you want them to be able to read everything in one shot, which is the reason for a fixed size
buffer, but another thing you could do is just have, like.
The buffer stored as a length, and then a buffer, then it doesn't have to always be the same size, and then you're doing…
Yeah, you have to do two read calls for, like, the length, and then get the entire buffer, which…
That would probably also do something to mitigate the cost concerns. Like, if you don't have to… if every time this runs, you don't have to allocate, like, the maximum possible size of memory, but just,
what you're actually using. But, I don't know,
I'm not really, like, advocating for one way or another, just wanted to know, kind of, what people think.
Scott Gerring 00:39:52 I think other people in the group probably have stronger opinions about balancing the number of read calls
against the efficiency of the size than I personally do, and I'd be super interested to hear those.
Felix Geisendörfer 00:40:09 I think Florian has his hand up.
Florian Lehner 00:40:11 Yeah, yeah, but it might be a little bit… not… maybe not a direct answer to this, but,
Was there consideration to use some kind of eBPF to share this information between different processes?
In particular for use cases where you have different
deployments that use already EVPath, that… so that they can share this information, and, like.
like it was just mentioned, BPF Pro Bread is probably not a way to scale this. I know the Obi, OTEL Obi project is also very interested in this.
So,
I see the point that this approach works quite well if the other side or one component is using purely in user space, but maybe not in… not for observability in kernel space.
Was this considered in some way?
Or is there an idea to have something like, hey,
If you share this information this way, you can map it into eBPF maps another way.
Scott Gerring 00:41:24 Evo, I think this is a good one for you.
Ivo Anjo 00:41:28 Yeah, so, the… Yes, so, we are aware of the efforts to also support OBI.
And, we've not… we've, we've not gone very far into, like, how would that, look like. My personal thoughts is that,
I think we'll have to do both. So, the… kind of forcing, forcing user space to always go into kernel to set the maps is kind of…
Like, looks like a tougher pill to… to swallow, where this version, like, changing a thread local variable, it's, like, just…
kind of doing a memory write, which seems, like, much cheaper. But I do think that, like, as much as possible, we should, as you kind of were mentioning, try to make this
friendly to be, like, copied very easily to the kernel, and then, like, maybe shared using the map. So, I'm hoping we can kind of support both in kind of a strategy, but I think they need to kind of be, like, one on top of the other, or side by side, not one or the other, in my opinion.
But not gotten very far yet.
Florian Lehner 00:42:51 Yeah, I also don't see them as a replacement, just as an addition, add-on.
For the respective components.
Alexa?
Alexey A 00:43:08 I have a question purely about the format itself. This thread local,
thread local fields. So these thread local fields will be added to the… to the process context, correct? .
Ivo Anjo 00:43:24 You mean this thing, or the…
Alexey A 00:43:27 No, no, no, yes, yes, this, this feels…
Ivo Anjo 00:43:30 Yes, yes.
Alexey A 00:43:31 Okay.
Okay.
And…
There is this schema type and schema version, so is this for, like, flexibility? Because, like, someone else, or…
Like, because this document describes a particular schema for the thread local… for the thread local structure, but at the same time, we have the schema type.
which is TLS disk. Does it mean that, like, we think that, like, someone else might want to use a different format, and we try to prepare for that? Because on the other hand, we do have this red local attribute key map field here, which already dictates
Kind of, like, parts of the format, so it's gonna get… It's just a purely…
This flexibility versus being rigid.
Scott Gerring 00:44:19 We talked about this… sorry, we talked about this a little bit before, I think we actually landed on the idea that we should just combine it into a single version field, Evo, and we're kind of mirroring what the Polar Signals folk…
are doing here with their labeling, so you have the flexibility to say, it's still this general format, but we're version 2, so interpret the bytes beyond this point differently or so. But yeah, I think it should be probably at most, one
One key within the record, because you already know what you're looking for at that point.
If that makes sense.
Ivo Anjo 00:44:52 But I… I think there was, like, a deeper comment, if I understood Alexei's question, which is to say that, if this thing and this thing are related to this thing.
like, does it make sense to add the keys like this? And maybe the question is, like, we should do something like this, or something like that, to…
kind of… to… to make… to relate them to the specific schema type, if we want to make them related to the schema type? Is that, like, something like what you were saying?
Alexey A 00:45:26 I was wondering, like, do you even need the schema type field, and whether schema version is enough? And if a completely new format ever comes up, then maybe it will just use different field names, or something like that. It's just…
It's unclear that, like, trying to prepare to every possible future extension is worth it sometimes, so.
Ivo Anjo 00:45:50 the,
Yes, we can simplify this. I think the intention when we put the schema type… and actually, we decided to combine them, but we haven't updated here, so the idea is for them to be together, but it's the same idea. The idea was that we already have, like, an existing mechanism for Go, which reads directly the Go routine PROF labels.
So, maybe for a go-up, the go-up would say, the schema type…
Go, or something like that, and this way, the reader, the BPF profiler, could know, oh yeah, this is a Go app, and I should use the Go mechanism rather than having to probe for itself. Maybe that's kind of, like.
I know, too much future and it doesn't matter, but that was kind of the thinking behind saying, like, there is this schema because there's already an existing schema for the ABPF profiler, which is Go.
Alexey A 00:46:47 Okay, maybe mention this in the text, it's kind of, like, the motivation, and maybe this, like, potential future example, so that it's… so that it's clear that it's not exactly abstract.
But you also had some more specific codes in mind. And I also had a question, which is probably… was probably… I'm sure it was discussed already, just using just one byte for… for the key indexing. Like, are we sure that this is… like, no one is ever going to have, like.
257 keys.
And say, like, well, they have very short ones, so this is okay in terms of, like, memory usage, or something, or something like that.
Scott Gerring 00:47:26 I think that's a really good question. I wonder if anyone who's
already doing this, and I guess I'm largely addressing the polar signals folk here, have a strong opinion about that.
Brennan Vincent (Polar Signals) 00:47:38 Well, Frederick can give his opinion also if he has one, but I… I…
None of our customers are using anywhere close to 256 keys. It's more, it's more like…
You know, they might use 10 or 20 unique keys or something like that.
But… I can imagine it being possible if,
Well, if you have some large organization with, like, tons of code, and each team is sort of independently deciding what
Keys they want to track, or whatever, but we haven't seen that yet.
Alexey A 00:48:22 Yeah, it's probably fine, and if this comes up, then, like, the version could be bumped or something like that, and
It is tempting, on the other hand, to have just, like, one byte for the indexing, because it's more compact.
Brennan Vincent (Polar Signals) 00:48:39 Yeah, or you could make it, like, a variable length and quoted index or something.
Scott Gerring 00:48:45 Yeah.
I think it probably goes without saying, but it would be great for everyone who's interested in this to tear this document to shreds with feedback. That would be really helpful for us.
Felix Geisendörfer 00:49:02 I have a quick question. Is variable int, an issue for eBPF when you don't know how much to read ahead of time, or is that solvable?
Brennan Vincent (Polar Signals) 00:49:15 Well, you have to write some C code to decode it, but it shouldn't be too bad, especially because the maximum
The… you know, there's a very tightly bonded maximum size, it's not like you're gonna get a 10-byte long index or something.
Felix Geisendörfer 00:49:33 Well, I think 10 byte is the maximum you can have for warrant encoding, but yeah, you know what it is. I guess that makes sense. You would always do a maximum size byte read and then decode, or…
Brennan Vincent (Polar Signals) 00:49:46 Well, I think that, yeah, I think the idea here is, you always read in this entire buffer in eBPF, so, like, you're only ever doing one buffer, like, one read, no matter what, and then…
Felix Geisendörfer 00:49:56 Okay, you already know the tools. Yeah, yeah, yeah.
I generally like bar ends when we try to be dense for the encoding, so if that's the main goal here, that's worth considering. If the main goal is
ease of decoding and speed of decoding, then Warrens are often not the right choice, so yeah, I guess…
Scott Gerring 00:50:17 That's a good tip.
Christos Kalkanis 00:50:19 We can also send the entire backup to user space for decoding. You don't have to decode in eBPF.
Felix Geisendörfer 00:50:25 Okay.
Okay.
Christos Kalkanis 00:50:26 I have a question for Ivo. You mentioned opening a pulley request for a VPF profiler to support this. Do you plan to do it, like, while this document is in review, or are you waiting after we review it, and then you open the pulley request in OpenTelemetry spec? Like.
Ivo Anjo 00:50:48 The, the plan is to have it, before, I think, like, or, like, in parallel. So we… we… we are a bit late, because the person that was working on it, was out.
But hopefully, we'll be able to resume that and have that done, and we have the PR, so that we… I think it makes sense to look at the spec and the implementation side by side, so we can, like, sweat about the details. So, yes.
Christos Kalkanis 00:51:12 Yeah, so I think some questions are going to be clarified just by having something to run, and then also look how it looks… examine how it looks in eBPF.
Scott Gerring 00:51:23 We have a little toy eBPF reader at the moment. For what that's worth, it's obviously not nearly as serious as getting into the proper profiler, though.
Christos Kalkanis 00:51:35 Yeah, from our point of view, it doesn't have to be production-ready, like, it doesn't have to be, you know, the final thing that ends up in the paper file. As long as there is something that we can look at to better review this proposal, for me, that would be enough.
Alexey A 00:51:54 Couple quick questions on the thread, on the thread structure, thread attributes. I'm curious, root span ID, why is it, a part of the record? Because I think in the, for example, in the profiler format.
We only have trace ID and span ID, so I wonder why…
What's the use case for that?
Scott Gerring 00:52:14 I gather that it's something that we need on our side internally for the profilers, Evo and Felix?
Florian Lehner 00:52:22 I think the span ID on our side is 16 byte, so, you just split it up.
It looks like to me.
Alexey A 00:52:31 I thought span ID is 8 bytes, or is it… is it… sorry, I… Maybe I'm…
Ivo Anjo 00:52:43 I believe… oh, go ahead.
Scott Gerring 00:52:44 No, no, please, I was gonna say, I'm deferring this because I'm not totally sure.
Ivo Anjo 00:52:51 So, I believe, we, so two things, yes. So, one, I believe there was, like, yeah, already some experimentations, with this, and I was, yeah, double checking.
the, elastic format, also has this, called the transaction ID. I believe that was exactly the span ID local would spend, so we kind of kept this as well, because, yes, at Datadog, we find this useful, but, yeah, since… since things can move from here to here.
If people think that this is not useful to be a top-level item, and we'll just record this here.
Alexey A 00:53:33 To me, it's more like, if this is proposed to be part of OLTP specification, then different parts, like, different
places in the spec should be mutually consistent, and if… and I checked, so the link in the profiler format, the link is 16 byte trace ID and 8 byte span ID.
And I think that's… that's kind of like the span referencing model overall in OpenTelemetry. So having just, like, root span ID here as part of OpenTelemetry specification would seem a bit random, I would say.
Scott Gerring 00:54:08 Yeah, that sounds fair.
Felix Geisendörfer 00:54:11 I think the to-do on our end would be to, like, dive a little bit more into what we find useful in it and share that, to form the discussion, but I guess if nobody else finds it useful, then I think we would be okay with withdrawing at EVO, right?
Ivo Anjo 00:54:27 Yep.
Felix Geisendörfer 00:54:30 Brennan has his hand up.
Brennan Vincent (Polar Signals) 00:54:33 This is,
Related to the previous topic of, like, when this implementation will be added to the profiler and so on. So,
Today or tomorrow, I'll…
publish, like, a sort of draft PR that I don't expect to land, but just so people can see the difference.
that would, like, add the functionality we have in Parka to…
the eVPF profiler. And, like, the Parka agent is all open source, so you guys can feel free to use as much or little of that as, you want in order to base, your stuff on.
But I'll show you that. Yeah, it's like, what I'm working on now is sort of cleaning up the history of our repo to get these things as atomic commits, so once I do that, I'll send it to you.
Ivo Anjo 00:55:27 Thank you.
Felix Geisendörfer 00:55:32 Okay, any more questions here? If not, we have, like, 5 minutes to discuss alpha, but…
Alexey A 00:55:40 I have a question, but I will ask it probably as a comment in the document.
Felix Geisendörfer 00:55:44 Okay, then… yeah.
Other than Alexei going once, going twice, three times?
Yeah, I wanted to briefly, like, bring up Alpha again, now that we are hopefully getting very close with, two more, or one more PR, depending on how it's split, to the, OTLP to, to get the, any value and, key refs in place.
I think, yeah, what would be the sequence? I think Florian already mentioned after these steps, going to the collector and trying its implementation, would maybe make sense before we call it alpha, but if we…
Is that only critical path to calling going to alpha? Is it not? I'm curious how people feel about that. I think it should be, because, like, if Bogdan tries it out and doesn't like it, then we're kind of back to square one.
Christos Kalkanis 00:56:42 Yeah, we need to have a final acceptance.
Felix Geisendörfer 00:56:48 Okay.
Florian Lehner 00:56:50 once these changes land in the protocol and are released, I think we also have to refactor the reference implementation, I would say, before TeleProfiler.
Because the relevant resource attributes that we have at the moment are mostly on the message sample, and we have to push them up to the hotel resources, so that they can actually be used on filtering and other processing. So that's… that's an essential part, I would say, for the
You have profiler.
But.
Felix Geisendörfer 00:57:24 For the eBPF profiler, correct me if I'm wrong, but we don't expect any dragons to be there, that's, like, relatively work. I hope not.
Okay. I mean, yeah, we should probably still do it, but I think the biggest question mark to me is…
that's all the ideas we had for how this can work in the collector without ruining everybody's PData day, and if Bogdan's gonna like it, if that all comes together, I think that's the biggest risk, so we should probably give Bogdan a little time to put this in the collector. But in the meeting we had with him, he was very, like.
He seems like once he likes it, he could do it pretty quickly, so hopefully this is not going to hold us off too long. And then I think, yeah, is there any other steps that we're missing, other than potential implementation in Collector and the profiler, before we can move to Alpha? Any… anybody has more thoughts?
Christos Kalkanis 00:58:15 Document… documentation, yeah.
We had Fabrizio join,
months ago, he's going to help us out. He's a technical writer, and also part of telemetry.
But, yeah, I will ping him again. Once we know what we have, and we know that the path forward is clear.
Then we have to immediately jump on the documentation.
Felix Geisendörfer 00:58:38 Yeah.
That makes sense.
Okay, so basically three things. Maybe the docs are dependent a little bit on the collector stuff to get that on the road first, but yeah, once we have the collector stuff and the profiler, then the docs, and then…
victory, or any… any other gaps that we're missing about? Just thinking ahead so we don't…
find ourselves surprised a couple days before KubeCon, and Florian and I will have to deliver the bad news to… to people that were not in alpha.
No?
I guess, and let's hope we are not missing anything. Of course, if anybody thinks of something in between now and our next meeting, please communicate in the Slack channel or wherever you find convenient.
And then, yeah, I will…
I guess we have a minute. Anybody has any last thoughts or questions before we… Finish off?
Nope.
dalehamel 00:59:42 Hey, just a real quick item on, Ruby stuff. Thanks so much for all the, reviews on 907, it's landed now.
I've got a couple PRs up, but I've seen some reviews on those already. Just a heads up, I'm gonna be out next week and the week after, but I'll try to get back to any reviews on that.
But yeah, Ruby is really progressing, so thanks so much, guys.
Felix Geisendörfer 01:00:06 Cool, and thank you, Dale, for all the work you're doing on that. It's really cool.
dalehamel 01:00:12 Cheers, guys.
Felix Geisendörfer 01:00:13 Cheers. Then yeah, I guess if nobody else has any things, thank you so much for attending, for all the work being done between these meetings, and see you all next time. Have a nice local time.
Ivo Anjo 01:00:26 Deal.
Brennan Vincent (Polar Signals) 01:00:27 Yes, ma'am.
