SIG: Go SIG
Date: 2026-06-11
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 02:09 Hey, Brian.
**Bryan Boreham** 02:21 I said hi, and I was muted.
**Tyler** 02:24 Ugh.
How's it going? Yeah.
Going well, yeah.
Just, busy as always, yeah.
Are you guys having some sort of, like, hackathon or something like that at Grafana right now?
**Bryan Boreham** 02:37 Not this week, no. We… we got hacked.
**Tyler** 02:43 That's… that's the worst version of that, yeah.
**Bryan Boreham** 02:48 That was about three, three and a half weeks ago. Okay.
**Tyler** 02:51 Yeah.
**Bryan Boreham** 02:52 So we had a big, We had a security hardening week.
**Tyler** 02:57 Oh, okay. Yeah.
**Bryan Boreham** 03:02 And there is a… there is a hackathon in a couple of weeks, I think, which is, again, going to be security-focused.
**Tyler** 03:08 Hmm.
Yeah, some of your colleagues had mentioned it. For some reason, I thought it was this week, but yeah, I couldn't remember. Yeah.
**Bryan Boreham** 03:16 Yeah, yeah, now we got hit by some of this, NPM… Stuff.
**Tyler** 03:23 Oh, that, like… Credential stealing stuff, where the… yeah, supply chain… yeah, that was… That was nuts.
Yeah, you're kinda like… You gotta keep all your packages up to date, because otherwise you're gonna get hit with vulnerabilities. Oh, but don't go to Bleeding Edge, because then you're gonna get hit with vulnerabilities, yeah, it's like, oh my goodness, like… Yeah, that was… that was tough.
That was a tough one, yeah.
Are you, are you looking at submitting to the… what's like, Observability Days in EU? It's like the… What is that?
**Bryan Boreham** 04:00 Not sure I know about, huh?
**Tyler** 04:03 Yeah… what was I just looking at it? Yeah, it's Overly Summit EU. It's happening in Prague, it looks like, October 5th. There's, like, a… CFP open to July 7th.
**Bryan Boreham** 04:15 Yeah, I might… okay, I might have looked at that and, because we have… Yeah, October 5th is my wife's birthday.
**Tyler** 04:27 Ugh.
**Bryan Boreham** 04:29 And I… and we have PromCon… like, the 7th, 8th, so it would kind of work to do Prague and then Munich, but…
**Tyler** 04:38 Oh, Munich's… oh, yeah, that's not too bad, yeah.
**Bryan Boreham** 04:41 It… but I would have to explain things to my wife.
**Tyler** 04:45 No, just bring her with you. Yeah.
Doesn't she really want to go to some, like, observability summit for her birthday?
Yeah, fair enough.
**Bryan Boreham** 04:58 Well, our own…
**Tyler** 04:59 She probably would want to go to Prague, that sounds great, but the… Yeah.
**Bryan Boreham** 05:03 No, she does… I mean, our eldest daughter lives in Prague, so…
**Tyler** 05:07 Cool.
**Bryan Boreham** 05:08 So, yeah.
Anyway, thanks, we… David has joined the call, so…
**Tyler** 05:14 Yeah.
Hey, dude.
**David Ashpole** 05:17 Abe?
Park sounds fun.
**Tyler** 05:20 I know, right?
I don't know if my body really wants to do an international flight again, but Prague does sound fun. Yeah.
That does sound fun. I don't see any agenda items, but I did want to touch base with you, David. Missed you last week, because it seems like there was a lot in flux with things that we needed. The only thing that I found that I think is unmerged from you right now is, like, the… with unsafe attribute PR, but it looks like it's got the approvals, to get.
**David Ashpole** 05:50 Yeah, yeah.
**Tyler** 05:50 I didn't know if there's anything else top of mind for you that you needed somebody to take a look at, or something like that, yeah?
**David Ashpole** 05:58 No, no, no, I haven't.
I did, like, a whole bunch of stuff, and then was like, okay, I should stop opening pull requests.
**Tyler** 06:06 I disagree. I think those are great. I think you did a lot of really.
**David Ashpole** 06:09 No, no, they're all good, they're all good. I just…
**Tyler** 06:11 Yeah.
**David Ashpole** 06:13 I have a hard time, once I get more than, like, 15 already.
**Tyler** 06:17 Like, staying safe. Yeah, I know.
**David Ashpole** 06:19 So I was like, okay, I'll move on and spam somebody else with pull requests for a little while.
**Tyler** 06:24 Yeah.
**David Ashpole** 06:26 So I haven't actually… I've tried to get the ones that were approved merged. I think a bunch of them need, like.
Rebases, let's see.
**Pellared** 06:38 Hello, sorry for being late.
**David Ashpole** 06:44 Is this one ready? Did I send this one out?
Sorry, I've got… Too many tabs.
Okay, so… There's a pull request out to use… Let's see, I can just add them to the list. I think most of the ones that are open are probably not urgent, and they're also large, so I totally understand that People might take, A week or two to get to them.
Let me find the SIG meeting notes.
So, for the exponential histogram one, if you vaguely probably recall at this point, I had talked about Implementing some sort of very fancy, guard that would detect overflow.
For when you had, like, one or two buckets for an exponential histogram as your max buckets.
Yeah. Because it's the only cases it can… and I realized later, like.
That should be such a rare case that instead of implementing something complicated, If you have… two or fewer buckets, then you just get a regular lock around the whole thing, and don't get optimal performance. Instead of… instead of 300 lines of implementation and tests to… Implement something fancy, specific to that case.
So I think that's actually a much better solution there.
Let me find… find other PRs.
Is this one ready for review?
Some of these need to be rebased.
But… Wow, this one… Yeah, yeah.
These can be reviewed, they just have some conflicts now.
this one…
**Tyler** 09:24 Oh, okay, it's lazy compute, filtered?
Oh, April 19th, okay, I was like, I've seen this before.
**David Ashpole** 09:33 Yeah, we had discussed this one in the past. There was an issue that I had to fix where This was the one where, like.
We were evaluating the filter multiple times.
**Tyler** 09:46 Right.
**David Ashpole** 09:46 And so the only way to fix that is to encapsulate the filter's decision.
**Tyler** 09:51 Right, right.
**David Ashpole** 09:52 In this other struct. So, I think the trade-off here is just, like, whether we think the additional API surface is worth it.
**Tyler** 10:07 Yeah, okay.
**David Ashpole** 10:08 It's not, like, super user-facing.
**Tyler** 10:13 So it adds another filter type to the attribute package, is the thing?
**David Ashpole** 10:18 I mean, I…
**Tyler** 10:19 Oh, lazy. That's a whole other set. Okay.
Hmm…
**David Ashpole** 10:26 Yeah, so I think… I think that's the… the trade-off we need to evaluate, is… Is it actually worth it to introduce this new concept? Lazy Filtered set?
That basically encapsulates A set that is filtered.
Otherwise, I don't think there's really a way to make this. I think the elephant in the room is, like, if we are going to move toward, bound attributes eventually. Then… This is, like, this is a stepping stone.
But it's… it's not actually… Like, it wouldn't be, like, the performant way to do things anyways.
If… if we had bound attributes.
**Tyler** 11:08 Yeah.
**David Ashpole** 11:09 That, by the way, I've been having a lot of trouble implementing the most recent spec, so I might have to go back to them with some feedback.
**Tyler** 11:16 Oh, interesting, okay.
**David Ashpole** 11:18 Yeah, in particular, like… That's, yeah.
Bound in the… right now, because it's, like… There are different storage requirements.
for bound instruments and regular attribute recordings.
And… If you make observations on a bound handle, and then also record the same attribute set, like, make measurements on the same attribute set with the non-bound handle. Right. It's, like, very, very hard.
**Tyler** 11:48 Have you resolved those two? Correctly. Yeah.
**David Ashpole** 11:50 Yeah, so… so, like, that's… and… You know, you can make it work, but it's like… it's a lot of code to make it work, and there's a lot of edge cases, and I don't like it, so, Yeah, if I remember correctly…
**Tyler** 12:06 one of the things that, like, I don't know if this, like, sparks some thought, but, like, Josh's, original, like, POC way, way, way back in the day, it was, like, essentially, like, all of those storage mechanisms, they were, like, completely independent, and then it was only at collect time, like, there was a separate API for, like, add, delete, essentially, like, resolve conflict at that point, yeah.
I don't think histograms were implemented at that point either, though, so… I don't think that that's actually… That's a harder one. That was always going to be, like, the harder one. And then exponential histograms didn't exist, so that definitely was a harder one.
**David Ashpole** 12:44 Like, all that's possible.
**Tyler** 12:46 Yeah, exactly.
**David Ashpole** 12:48 I was hoping… I was hoping not to have to do that.
But at least, like… I would be more… if we went that route, I would be more confident that it would be correct and bug-free.
Because I can reason about, like, how to merge two exponential histograms, and, like, it's a lot of code, but it's not… It's no, like… I feel like I have to introduce a lot of new concepts to get this right right now.
**Tyler** 13:15 I think you would, yeah, exactly.
**David Ashpole** 13:17 Okay.
**Tyler** 13:19 But otherwise, I think you're gonna deal with synchronization issues in the measurement pipeline, right? Because you're always gonna have that problem of, like.
check if this exists in this storage structure, check if this exists in another storage structure, and then you have, like, a race condition there as well, right? Like…
**David Ashpole** 13:37 Yes.
**Tyler** 13:38 Yeah.
**David Ashpole** 13:39 And, like, cardinality limiting becomes very bizarre.
**Tyler** 13:43 Oh, I didn't think of that. Yeah, that's even harder, yeah, okay.
**David Ashpole** 13:46 So… Like, right, the… I may go… I may not finish the prototype, I may go back to the spec first.
And see if… if there's any interest in… First, I want to check and see how other languages are handling it, I think, because, like.
you know, CJO and, and Jack pumped out prototypes, like.
You know, right away, so… I don't know if they're just not solving this, or if they have a solution we haven't thought of.
**Tyler** 14:17 Jack, I would imagine he's solving it the way I'm kind of talking about, because I think they did, like, the storage mechanism sort of structures, and then CJO, I'd be interested to know, because, yeah, Rust followed us, so their internals look similar, so I'm with you on that one, yeah, I'd be interested to hear that solution.
**David Ashpole** 14:34 Part of me wonders if they're… they are okay accepting that you will get duplicated metrics if you record on the bound and unbound path. I could see us saying that.
I don't love it.
**Tyler** 14:50 Yeah.
**David Ashpole** 14:51 book on point of view.
But I also, like, Yeah, I don't know, I… I feel like at this… like, I haven't worked on it in a few weeks, but I feel like I got far enough along that I was like, something's not adding up here.
**Tyler** 15:09 Yeah, okay.
**David Ashpole** 15:09 off the rails.
**Tyler** 15:11 I do think, going back to the spec and just surfacing this is a great idea. So, yeah, I would encourage that, yeah.
**David Ashpole** 15:17 But that's where that is, and if the feedback on the lazy computation PR is, we don't want this.
Or we wanna, like… close it for now and revisit it later, I think that's acceptable. I'm sure it's not that hard to resurrect later, if… if, for whatever reason, bound instruments don't work out, or we're having this conversation, like… Next year or something.
**Tyler** 15:40 Yeah, I'm a little hesitant on this, so one of the questions I have for you is, like, how does… how does this get added to the metrics pipeline?
**David Ashpole** 15:49 For the lazy filtered piece.
**Tyler** 15:51 Yeah, is it just, like, another option that's added?
**David Ashpole** 15:56 No, so this is… let me see if I can figure out where this… That's in.
**Tyler** 16:08 Oh, so it's, like, it's being used internally?
**David Ashpole** 16:12 Let me… actually, maybe there's a… maybe there's a second option. So, the place that this actually shows up in the public API is, I think, as part of the exemplar reservoir.
**Tyler** 16:24 Yeah, yeah, that's what I'm seeing. Yeah, okay.
**David Ashpole** 16:29 So, if we didn't… so ba- you can think about it, like.
The more lazily you compute attributes.
The more places you can remove allocations.
So, if you just lazily compute attributes in the metrics SDK, That saves you one allocation. And then if you can also lazily compute it in the exemplar reservoir, that'll save you a second allocation.
The only thing with the reservoir one is that it only saves you an allocation if the reservoir is sampling.
Or no?
No, it always costs you an allocation, because the reservoir doesn't know if it's gonna sample or not, so you have to pass it the resolved dropped attributes.
**Tyler** 17:14 Oh, right, right.
**David Ashpole** 17:14 allocation comes from. So…
**Tyler** 17:16 Yeah.
**David Ashpole** 17:17 basically, Right. If one option is to scale this back and to not put it into the exemplar reservoir.
API Or to define it.
In… It could be part of the public API surface of Exemplar Reservoir.
But that would be a little bit weirder.
**Tyler** 17:39 Hmm, yeah.
**David Ashpole** 17:40 But it's an option, if we don't want to pollute the attributes package. Otherwise, we could keep it internal to the Metrics SDK and get One… we would remove one allocation, and a bunch of work.
rehashing.
So that… that would be, like, a good chunk of the win.
without any, public API service, and then it could just be internal to the Metrics SDK for now.
**Tyler** 18:05 Yeah, I think I kind of like that approach.
I'd prefer that approach.
Yeah, and I think… Yeah, because I think it just becomes a little bit muddier, like, when you get it in the public API of, like, well, what do I do with this, like, lazy filter set? It's like, can I actually use this? It's like, not really, like, this is meant for internals of metrics.
So I think that's a great place to start and prove it out, at least. And then I think that, like, it could always evolve. Like, maybe we could find a use case, maybe people are like, I'd rather pass this, you know, or something like that.
**David Ashpole** 18:39 Yep.
Let me just take notes on the PR.
**Tyler** 18:48 Yeah.
Sounds good.
I think while you're doing that, we did get a few more… entries into the agenda.
**David Ashpole** 19:01 I'll be…
**Tyler** 19:02 we can jump in a little bit here. So, Igor, I see you also added a PR for, the contrib… let me start sharing my screen, we can maybe talk about this.
I think it's… yeah, okay. This is the one, right? You are?
**Igor Peschinskii** 19:23 Yeah, right, thanks. There is a discussion in the last comment to the peer. As Robert and David are here, maybe we can, like… Yeah, decide on what to do with the schema URL when we're creating default.
resource.
Yeah, this one. This one, yeah.
**Pellared** 19:52 So, I blocked it, because as far as I understand the declarative config, it says that if it's omitted, then it should be, Yeah, no schema rail should be used.
And also, it was approved by Alex before this was introduced, and Alex is also the configuration signer.
So, I wanted him to take a look. I know that Tyler is also a maintainer, but I'm not sure how much Tyler is involved there, so I have… I would just prefer To have their opinion, because it is also possible that it's their mistake.
in the declarative configuration, you know, specification, so I think it's just a great opportunity to figure out what is the correct way with the SIG.
And, yeah, and then, probably, Yves… if it was… if the decision to have it, you know, I think that David's suggestion is reasonable.
and maybe it should be considered as a bug fix, but I'm not sure, yeah, I think… Then other languages should follow you as well.
Because all languages should have the same behavior.
**Tyler** 21:13 Yeah.
God, I hate this thing. So.
Yeah, I mean, I think if you can be reasonably certain about, like, what schema URL encapsulates the semantic conventions that are, you know, being used in that resource, you should… you should use that schema URL. I think that makes sense.
I don't know if you have to say that you're 100% certain, like.
So I think David's point would make sense here.
Yeah, I think it's… I don't know. I think this may just be something you could surface up to the configuration SIG as well, but I mean, I'm fine with… I don't know. I probably wouldn't block this PR on this level of detail. I'd maybe just track this as, like, a follow-up issue, if I were… if I were… Just trying to make this, because I think it's more important to get something.
**Pellared** 22:12 That's fine, that's fine for me. We can just create an issue for tracking purposes, but I think, Igor, I think, I think it's worth, it's worth following up, especially that probably you want to use in the collector.
And it will be very strange if, you know, the collector, which is, like, the main thing, or probably the config will be used, will not follow the declarative configuration specification.
**Igor Peschinskii** 22:38 Yeah, right.
**Tyler** 22:42 Yeah, I think that that's… All good. I would go with that route, yeah.
**David Ashpole** 22:47 Do we?
**Igor Peschinskii** 22:48 I also wanted to add that… sorry, sorry.
**David Ashpole** 22:51 I was gonna say, do we ignore schema merge conflict errors, or, like, log them as warnings in our declarative config thing today?
Or do we force you to use the same versions of all your detectors?
**Igor Peschinskii** 23:06 Right now, it's an error, as far as I know.
**David Ashpole** 23:10 Okay.
You know.
**Tyler** 23:12 You should probably ignore it.
**David Ashpole** 23:14 I, like, I feel like, honestly.
The other lesson here is, like, we should just be logging those as warnings, and probably not failing, because, like, what's someone gonna do, you know?
When they're… I guess the answer is, like, please compile your binaries with matching things, but that's hard.
So…
**Tyler** 23:36 Yeah, sometimes impossible, even, yeah.
**David Ashpole** 23:39 sometimes impossible, so… Yeah.
Yeah, maybe as part of the follow-on issue, we can also… Make sure that… Because in some ways, it's helpful to know that you've… thrown together 3 different schema URLs in a resource, and that the SDK is picking one of them.
And, like, if we could use the standard resource merge logic, and then ignore those, or then, like, log those errors, but still continue, like, that feels like something like the optimal… Optimal is a strong word, but, like, the least bad behavior we could, give.
But I'm happy to approve this if we just want to do it in pieces. I don't think… I think this is a step in the right direction.
**Tyler** 24:26 that resource merge stuff, or not even resource, just semantic convention, like, schema URL translation stuff is, like… a can of worms, right? Like, we've tried to add it here before, and then, like.
We, like, it ultimately comes back to, like.
it being resistance from the spec, because they don't actually want to fix the schema URL, like, translation rules, because they're going into, like, moving towards entities, and entities are supposed to replace this whole thing.
So, like, they're actually, like, yeah, it's… it's not a stable spec for the schema URL, by the way. Like, that's step one, and they don't want to, like, actually adjust it, yeah.
**David Ashpole** 25:02 I didn't realize it wasn't stable. I think entity detectors will help this.
**Tyler** 25:07 Yeah, that was… that's why it's not stable, is because people are like, no, like, let's just go solve this with entities, and yeah.
**David Ashpole** 25:13 This other thing.
**Tyler** 25:15 Yeah, I think that's exactly it. So… so yeah, we're kind of stuck on that part.
And I think, given we're stuck, that's where we came back to the point where, like, we just exposed these as those specific errors with the recommendation that, like, technically we are correct, because we were saying that this is a schema merge error, which is what the spec requires, but, like… You should probably just ignore this, is kind of what our guidance has always been, yeah.
So, yeah, I think, David, I think your point is correct. Like, we should try to log it if it's possible, or just ignore it, yeah.
**David Ashpole** 25:50 But for this PR, I think you can revert the change you made With respect to my comment.
So we should be… Compliant with, Config spec.
And then, we can get it merged.
**Igor Peschinskii** 26:07 Okay, thanks.
**Tyler** 26:09 And then just track in upstream if we want to change that. David, is that what the idea is?
**David Ashpole** 26:15 Yeah, it sounds like we should… the first step would be to file an issue with the config.
Spec.
**Tyler** 26:21 Yeah.
**David Ashpole** 26:22 Right? And then, once the config spec is updated, then we can follow suit.
And we'll just stay compliant with that.
**Tyler** 26:32 Sounds good.
Igor, does that sound good?
**Igor Peschinskii** 26:35 Yeah, that sounds good. Thank you.
**Tyler** 26:37 Yep.
Cool. Robert, you wanted to talk about the… map type? I thought I had it open.
**Pellared** 26:44 So that both you, David and Tyler, have approved it, so maybe just, I call out that I will merge it tomorrow morning, but I will be happy if I don't know. Brian or Igor, you will take a look. I'll be very happy. It's… yeah.
It's a quite big PR, there have been some, PR art, but yeah.
So yeah, I responded to you, Tyler, to this one. I don't think it was also blocking, I just prefer to have consistency here on this one. I remember it was just some nanoseconds.
**Tyler** 27:17 Oh, no, it's not, like… Smells? It's not quite the same. Sorry, it's not blocking, but, like… Like, if you're… if you're taking… If you're taking this and passing it to this function, and then iterating over this, like.
The fact that you know that this is a size 1 array isn't an optimization Like, if you wanted… if you wanted this to be an optimization.
**Pellared** 27:47 You need to inline it.
**Tyler** 27:49 Yeah, inline it and do…
**Pellared** 27:51 It's like…
**Tyler** 27:51 no iterations, right? It should just be like, okay, here's the first index, hash it, here's the second index, hash it, kind of thing, is what I'm saying here. Like, that's where the optimization would come from. But it's, again, not blocking, it's just…
**Pellared** 28:05 Like, it will be a bigger optimization, because Hero is the reflect.
But I agree, it will be a step further. But yeah, I think… we can create the issue, and I can solve the same also for the slices, because I think the same pattern is used in slices, if I remember correctly.
**Tyler** 28:20 Oh, really? Oh, okay, alright, then I missed…
**Pellared** 28:23 Okay, so I just used the same password, but yeah, I haven't realized that we… yeah, so you're just proposing another… another layer, which will improve.
**Tyler** 28:30 Yeah, and we're talking, like, probably tens of nanoseconds, so it's not…
**Pellared** 28:34 Massive, but… It is a hot pass.
**Tyler** 28:37 But yeah.
**Pellared** 28:38 Yes, it's happening, it's husband, so yeah, what I'm doing.
Okay.
**Tyler** 28:44 But cool, yeah.
cool, alright, so that's the end of the… Items on the agenda… Any other topics people wanted to talk about?
**Pellared** 29:00 I can just say, personally, that, David, if you have any PRs that will get reviewed.
you can just write me direct messages, because I'm so… I'm just not…
**Tyler** 29:10 That's how we started off.
**Pellared** 29:12 Okay, okay. So, yeah.
People for me as well.
**Tyler** 29:16 Yeah, take a look at the 2PRs he posted at the top of the agenda.
**Pellared** 29:19 I will, I will, because I saw it.
**Tyler** 29:21 Yeah.
**Pellared** 29:22 Wait.
**David Ashpole** 29:23 Oh, the lazy one doesn't need review anymore, I need to trim that back, so… Just… the only one that I think is actually reviewable right now is the sync.map for exponential histogram Aggregations.
**Pellared** 29:36 Okay.
**Tyler** 29:39 But yeah, you're thinking the same thing that we all were.
**Pellared** 29:42 David, do you need any reviews or help, regarding this, also, this specification site right now, or right at this point of time, nothing?
**David Ashpole** 29:52 No, no, I'm in a… I'm down a rabbit hole with… Prometheus and resource right now, and I need to think… I… I'm trying not to respond too quickly to anything. I need to think it through so that I don't flip-flop, but yeah.
**Pellared** 30:08 I see.
Thanks.
**David Ashpole** 30:12 Yep.
**Tyler** 30:17 Well, cool. Yeah, if that's it, there's no other topics, we can end the meeting early here.
It's good seeing y'all. I will see you all in a week's time. Until then…
**David Ashpole** 30:26 Welcome back.
**Tyler** 30:28 Bye.
