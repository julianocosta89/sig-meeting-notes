SIG: Profiling WG
Date: 2025-10-16
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/6m2tJMM3IBeCtqRZaqZVFgaGnbEFZvWC-NErfna-yvv29hscX1RuSY6JGgYDMxhC.BiiHLxON9Lw8byFB
============================================================

## Zoom Recording Transcript

albancrequy 00:01:09 You know, does it work?
Florian Lehner 00:01:12 Yep, hi.
Looks like profiling on-site in Paris.
Paris (21RC)-7.07 Rhone 00:03:10 Yeah.
Yes. That was only one of each of us.
I'm killing it.
Oh, oh, I just want, I just walked me through this.
Felix Geisendörfer 00:05:43 Alright, we're 5 minutes in, and as usual, no volunteers for the moderation.
then I will… I will handle it.
So, welcome everybody to this week's OpenTelemetry Profiling SICK Meeting.
As usual, we'll start by covering previous action items, and then go to… through the agenda.
Let me just get my screen sharing going on here.
Here we go.
So, previous action items. I think I didn't see Alexi here, is he here?
Florian Lehner 00:06:33 Would come later. He started with the PRIs, waiting for feedback on number 12.
Felix Geisendörfer 00:06:39 Okay, number 12 needs feedback.
Okay, let's just look at this real quick.
Rough track tool…
Okay.
Okay, yeah, this… this is pretty fresh.
Put an agenda item here for that. Capture that.
And we have, PProf Hotel Converter, and you have a sub-item there, Florian.
Florian Lehner 00:07:29 Yeah, no progress, there was no feedback in the last 2 weeks.
Felix Geisendörfer 00:07:36 So that's waiting on feedback? It's blocked by feedback? From the sick, or from.
Florian Lehner 00:07:41 Mainly from the, code owners, so, Antoine, it is…
But, yeah, no feedback from them.
Felix Geisendörfer 00:08:00 Okay, have you pinked them, like, a little bump or something already?
Florian Lehner 00:08:04 Slack here.
Okay.
Felix Geisendörfer 00:08:07 Okay, did you get any response back, or…
Florian Lehner 00:08:10 No response.
Felix Geisendörfer 00:08:13 Okay…
Is this only one person who could approve this? Only Antoine, or is this anybody from the collector, or contract maintainer?
Florian Lehner 00:08:36 I think every collector contract maintainer can also
provide feedback, but usually the code owners of the receiver PTROF
Are the first that have to… Take their actions and…
look at the code and do something. That's… that's the missing part.
Antoine is not the only one, there's a second one I did… Don't have free.
His name in mind.
Yeah, GitHub handle is Movie Story Guy, but I don't know him.
Felix Geisendörfer 00:09:25 Oh, movie story guy! That's very famous. I think he's the one who started the initial GitHub issue for starting the profiling SIG, if I remember correctly.
So…
Florian Lehner 00:09:37 Both are from Splunk, so… Okay.
Felix Geisendörfer 00:09:45 Okay, yeah, let's circle back to it, but if it's still blocked, next time, maybe we need to think of some way to get attention.
Or… or get approval from somebody who's not in that group, and get an override from the…
I mean, yeah, whoever has the GitHub powers to do that.
Cool, and let's continue on.
Yes. We have a bunch of.
Paris (21RC)-7.07 Rhone 00:10:17 Yeah.
Felix Geisendörfer 00:10:18 upon text propagation documents, which I assume we're still waiting for, Ivo?
Paris (21RC)-7.07 Rhone 00:10:22 Yes, but I can give a bit of an update, and I think we can clean that up a bit. So, as far as the process-level document, I think I… good feedback. Also, particularly thanks, Florian, for that. I think there's… basically, I think that's the big document where,
I, like, we need more feedback. I think we're at that phase where we need, like, feedback on it. I still want to incorporate some of the feedback that we've gotten, but there's kind of two things that I would call out, which is…
We… the protobuf-based format we're supporting there, we're using… we have a few fixed fields, a small set of fixed fields, and then we have a key value map where we can…
stored extra things. So, we would welcome very much feedback on that. Like, does that, look reasonable? Should we kind of just move everything to a key-value format? Should we just move everything to fixed
brought above fields. So that's one thing.
The other thing we're, I wanted to kind of ask the group is, if we do go with the protobu-based format, would it probably makes sense to have the Dutch proto live somewhere, and also the spec for the process level context sharing live somewhere?
What would be the best place in hotel, or where do we usually put those things in a hotel, like, in a centralized place?
And, so yeah, I think this is the kind of feedback that, in particular, I think we would very much welcome.
Answering this question?
And, for the,
So there's four documents there. For the resource documents, the… so which is the second one? No, the first one, resource definition.
We've been talking about it internally, and we have a kind of a better idea to go in a slightly different direction, so I would, for now, remove it from the list to review, because we want to kind of make a different proposal.
And that, I think, will be, like, a bit more aligned with some of the feedback we've gotten.
So I think we can remove it from the action items, that one.
And,
Yeah, that one, and finally, the last one, the thread-level information. We are at this point where we are prototyping some of the ideas discussed with Java, but… I would also remove it from the list there, because I think it's on…
on our side to prototype it, and if anyone else also wants to help, kind of, prototype some of the ideas here, I think it makes sense for us to chat, but that document right now doesn't have anything to review. We actually need to validate those ideas before we can move forward, so I think it's more on our side than…
actually asking feedback, so I think we can remove that one as well.
Rather than have it, kind of…
Felix Geisendörfer 00:13:22 Yeah, which one is that? Is it this one? Yeah, exactly.
Paris (21RC)-7.07 Rhone 00:13:26 I think from the action items, you can remove that one as well.
Felix Geisendörfer 00:13:28 Okay.
I will remove it.
Paris (21RC)-7.07 Rhone 00:13:35 Yeah, perfect. So I think that's the thing for us right now. Like, both of those… those remaining are relating to the process level thing, so feedback on that, and hopefully figure out some of those questions.
Frederic Branczyk 00:13:50 Yeah. I have some stuff to probably, like, share about this, because we've been doing this for some time, and recently we were exploring how much of this is kind of applicable to other runtimes as well, and I think we should make sure that we…
Scope this appropriately, such that, you know, we only treat
you know, C, C++, Rust, maybe, as part of this. I say this specifically because… maybe Java, I don't know Java well enough to comment on that, I don't know. But, we recently implemented support for this in V8.
And it had to be so that it, you know, isn't entirely performance…
prohibitive, we had to do something completely custom for V8.
So, just wanted to throw that out there.
Paris (21RC)-7.07 Rhone 00:14:45 to… just to clarify, when you say this, do you mean getting the current trace ID and span ID, that kind of thing?
Frederic Branczyk 00:14:51 Yeah.
Paris (21RC)-7.07 Rhone 00:14:52 Okay, yeah. I… I think what you… just to add to that, we already, like, I believe we already have a Go, we have already a Go… a specific solution for Go, so I think, yeah, it may,
In general, that's what that document is saying, but I think we need to document it better, is that it's quite possible that we will not have a one-size-fits-all, and for some runtimes, we need to have specific solutions. That's what's said on that document, but we want to work on it a bit more before we kind of,
Say that we're happy.
Frederic Branczyk 00:15:28 Makes sense. I'll also make sure that our, my team looks at this as well, because, like, we've been working with this custom label stuff for some time, and a lot of our customers are using it already.
Paris (21RC)-7.07 Rhone 00:15:41 Sounds great, thank you.
Felix Geisendörfer 00:15:49 So basically, your team is going to look at the documents we've shared and give feedback? Okay.
Frederic Branczyk 00:15:58 I guess specifically the threat level one, that's really the only thing that we've cared about so far.
Felix Geisendörfer 00:16:05 Okay.
Can you, sorry, just curious, why does the process level stuff not come up in your area?
Frederic Branczyk 00:16:15 Because… so we have, like, we wrap the OpenTelemetry profiler, and we attach process-level metadata in our own reporter.
we, we, like, in that sense, we don't really use, like, OTLP, as the protocol. We have our own protocol for this.
Felix Geisendörfer 00:16:42 I see, but I guess some of that work is about allowing applications to share metadata, like, from the application layer. So if, for example, the application wants to tell you.
What its service name is, or something like that, that is sort of standardizing that
thing, which I would assume you would care about at some point as well, to give more control to people.
Frederic Branczyk 00:17:03 Well, we, we… For us, the philosophy is that this is, like, workload metadata, and the…
The process shouldn't know or care about this.
Like, this is process… this is, like, workload metadata that should be discovered from Kubernetes, or should be discovered on the host, but the process itself shouldn't care about it.
Felix Geisendörfer 00:17:37 So, in other words, you essentially would…
Expect that data to be collected out of band, and then shown together when people, like, use profiling data.
Frederic Branczyk 00:17:48 I don't think we have a strong opinion of, you know, what is the OpenTelemetry
eBPF Profiler capable of, but, like, this must continue to be possible for us, and it's…
not terribly complicated, because all we need is the.
Felix Geisendörfer 00:18:04 Agent.
Okay, yeah, thanks for sharing, I was just curious. Then, I think for Evo, one thing you said, maybe I have a proposal, I think for the…
protobuf schema file, I think the initial place could be this repo we have here, the SIG profiling repo. That's just where we could put it right away, and then maybe we find a better home for it later, but if we need a temporary home, this is probably the best. I don't know if other people have different thoughts.
If not, I will make that a suggestion.
Paris (21RC)-7.07 Rhone 00:18:38 Cool. Thank you.
Felix Geisendörfer 00:18:40 I'll inline that here, because it's easier.
Yeah.
Yeah, because it's a little awkward. I mean, it could go into the main proto repo, where all the other protos are, which maybe is a good idea, but it's kind of awkward in the sense, because it's not part of the protocol, and previously, I think only, yeah, directly protocol-related protos were stored there, not protos that talk about how
A, yeah, process.
Paris (21RC)-7.07 Rhone 00:19:18 for me.
Felix Geisendörfer 00:19:19 It was a full.
Paris (21RC)-7.07 Rhone 00:19:19 Yeah, this is almost an on-disk format and less of a network format, like, almost, yeah.
Felix Geisendörfer 00:19:25 I mean, it is a communication protocol, it's just an inter-process communication, not a network communication protocol, so…
Paris (21RC)-7.07 Rhone 00:19:32 Yup.
Felix Geisendörfer 00:19:35 Okay, cool. Any more context propagation document comments, or should we move on?
And moving on at AS,
Owner wanted, we agree. The document values and timestamp shape should be the same for all.
Samples in the given profile, see overlap was 714.
Flippin' that…
My zoom window's in the way, I don't see what I'm doing.
Okay, 7.14 that's closed.
I guess Jonathan is here and has context, fingers on…
Jonathan Halliday (IBM) 00:20:20 I think you're on 724 now.
Just a replacement for it.
We closed 14 because it had the controversial bit about what do we do when there aren't timestamps, and…
aggregate things.
724 is the same thing, but without that difficult bit.
Felix Geisendörfer 00:20:37 Which message does documentation?
Okay… thus…
Okay, so basically this does not talk about timestamps, right?
Jonathan Halliday (IBM) 00:21:05 Not at the moment, nope.
Okay, okay. I guess since it's not merged yet, I could update it to do so, but…
Felix Geisendörfer 00:21:13 No, I don't… I don't think we have to overload it, I've just… I think this, this was about time… I'm just trying to figure out if we can drop one here, because it's been succeeded, but it seems like the timestamp topic would still be open, even if 724 gets merged right now, right?
Florian Lehner 00:21:29 As we just flew by, the PR, there was,
There was something about sorted attribute indices.
Line 371.
Is this always expected? Does attribute indices are, ordered?
Because I can…
Jonathan Halliday (IBM) 00:21:50 No, I'm… I'm… When you want to aggregate samples together.
you have to check that they have the same primary key. They're referring to the same set of attributes, because if the attributes are different, you can't aggregate two samples.
You have to keep them separate, because they'll be pointing at different… attribute keys, right?
But to know whether two sets of attributes are equivalent or not.
The equals method has to sort them before it does the compare.
Otherwise, 12 is not equal to 2, 1, even though the set is the same.
Florian Lehner 00:22:21 Yep, okay, sorry to make, yeah, makes sense.
Jonathan Halliday (IBM) 00:22:23 Yeah, so it's just defining the primary key as saying when you write the equals method for that, make sure you sort them first.
It's not trying to impose the restriction that it…
on the wire, they have to be sorted. We could do that if we want, but currently we don't.
Florian Lehner 00:22:40 Yeah, makes sense, makes sense.
Frederic Branczyk 00:22:42 strictly necessary? You can do comparisons even when they are…
Like, you can do, like, hash combinations that don't have to be sorted.
Jonathan Halliday (IBM) 00:22:56 Yeah, theoretically.
What you've got is an array of ints.
And normally, when you want to… Compared to raise events.
Your best bet is to sort them in And just do… Are the bytes the same?
Frederic Branczyk 00:23:11 I see. Since… yeah, okay, if we're already doing…
Yeah, if we're already doing, like, dictionary encoding, then…
Jonathan Halliday (IBM) 00:23:19 anything else?
Frederic Branczyk 00:23:20 Yeah, it would be more expensive to hash all the, like, key-value pairs and…
Jonathan Halliday (IBM) 00:23:25 Yes.
Frederic Branczyk 00:23:25 Okay, I get it now. Makes sense.
Felix Geisendörfer 00:23:29 It's still, like, talking about the sorting is talking about what is, like, a good way to implement it, but conceptually, what we're talking about is treating the attribute indices as a set, right?
Jonathan Halliday (IBM) 00:23:41 Yes.
Felix Geisendörfer 00:23:42 Where there's no ordering. Yeah.
Right. Maybe that is a better way to still phrase it, because it's kind of weird to talk about the implementation details of, like, an equal comparison, in terms of, yeah, how to implement it. I think, conceptually, it's a set.
What do you think?
Frederic Branczyk 00:23:57 Yeah, the same combination, like, the same way that you can combine hashes, you can combine indices.
for equality.
Felix Geisendörfer 00:24:11 what do you mean by that?
Frederic Branczyk 00:24:13 I mean, this is, like, a simplified example, but, like, if you sum the indices together, and you see the same sum in a different place, then, you know, you could assume that they're equal. Obviously, we would use something that's cryptographically secure, but…
Felix Geisendörfer 00:24:34 Right, and you're basically saying there's just different ways to implement the equality.
Frederic Branczyk 00:24:37 Exactly.
Felix Geisendörfer 00:24:38 Yeah, and yeah, my point was… yeah, so my… exactly. What we want is set equality semantics, right? And we don't care how that's implemented, definitely not for the specifying the protocol, so I… maybe that could be rewrote a little bit to make that clear. What do you think, Jennison?
Jonathan Halliday (IBM) 00:24:53 Yep, I'll do that.
Felix Geisendörfer 00:24:55 I'll add a comment here directly so we have it.
Zoom is jumping in front of me, I don't know why.
Okay, cool, but otherwise, you're still also looking for more refuse on this, is that correct?
Jonathan Halliday (IBM) 00:25:43 174, yes.
Felix Geisendörfer 00:25:48 74?
Jonathan Halliday (IBM) 00:25:49 724.
Felix Geisendörfer 00:25:51 724, yes.
Jonathan Halliday (IBM) 00:25:52 request, yep.
Felix Geisendörfer 00:25:53 Yes. Okay. Cool.
Let me just get a couple notes here real quick.
Okay.
Yeah, so everybody else who hasn't taken a look yet, please do later on, so we can maybe get one round of feedback then, too.
Go back and forth too much, but it seems pretty straightforward in general.
Thank you for doing that, Jonathan. Okay…
Send PR… okay, no, this is the one we just had. This is an Alexi item.
Does anybody have… Something to say about it, if not, we can skip it.
Then slow.
Alexey A 00:27:21 Sorry, sorry, sorry.
Felix Geisendörfer 00:27:23 Oh, you're here.
Alexey A 00:27:23 I was muted, yes, I joined. I sent a, I sent a pull request for that, so please take a look. I added a note that, yeah.
Felix Geisendörfer 00:27:35 Okay, it seems like it already has a bunch of approvals.
Maybe we can get this done right away, so original payload format.
Right, and I think Florian, I saw, yeah, from you on semantic conventions to define these instead?
Florian Lehner 00:28:01 Yeah, working on the specification, not semantic conventions. Oh, sorry.
Yeah, got some approvals, I don't know when they will get merged, but yeah, on… in progress.
Felix Geisendörfer 00:28:22 Okay, I think I need to take a closer look at this, but I will, I will.
Alexey A 00:28:27 Yep, sure.
Felix Geisendörfer 00:28:30 But otherwise, it seems like we already have a decent amount of refuels on that one.
Alexey A 00:28:36 Yeah, I think it should be fairly straightforward. I think it's the… mostly about… like, which…
Pieces are in semantic conventions, and then what pieces are in the specs, so… and just making sure that the comments are clear, because it's… there's no code change, it's just… it's just a commentation change.
Felix Geisendörfer 00:28:58 Yep.
Yeah, I guess I'm partly duplicating the next agenda item here, Florian, right?
Alexey A 00:29:14 Yeah, it's pretty much related.
Felix Geisendörfer 00:29:15 Yeah.
Yeah, so this is… this is the one, and… but this is not blocked on 6, this is blocked on the specification maintainers, or…
Of course, it looks like it's pretty much ready, right?
Florian Lehner 00:29:29 Yeah, feels ready, I don't know their policy, I will reach out next week, to the specification group and ask for…
The conditions to merge.
Felix Geisendörfer 00:29:54 Okay, and then, let's see what's next.
Yeah, the security issue, and I think we have Alban here as well, should we…
I think we did pull Florian in successfully. I think, Frederick, you were not at it? Is that correct?
Frederic Branczyk 00:30:15 Yeah, no. But I did, I did check, we don't, in the Parker project, we don't have a specific, definition of what constitutes a security…
flaw, or whatever you want to call it. But we, you know, we just have a general guideline on how to submit things.
Felix Geisendörfer 00:30:37 Yeah. I… yeah, let's, let's…
talk about this a little bit more, but let's timebox it since we still have some other things, and if we need more time, then move it maybe further. Yeah, so reminder for…
Those here who don't have the context, the issues are essentially various denial-of-service, attacks against the full host profiler, which
are essentially…
Executed by having a workload that is, tricking the profiler into indefinitely blocking when it's trying to read the
the memory from a process, and I think what they all share in common is that the attacker would need to control the workload that's running on the host, and that workload would need to run with various degrees of elevated permissions. Maybe Albon can confirm if he's here right now.
albancrequy 00:31:37 They… they don't need elevated permissions, but,
Then it, yeah, it's an interesting workload, so… .
Felix Geisendörfer 00:31:48 I thought, like, for one of them, you needed SECOM permissions, and I think for the fuse, you also needed, like, the fuse thing to be explicitly given to you, so, like, just… just if you were to control an image in, like, a containerized environment, let's say Kubernetes, would not be enough to exploit this, or would it be? That's what I'm trying to ask.
albancrequy 00:32:06 Yes, that's correct. That depends if, on your Kubernetes cluster, set comp is enabled or not, but if it's not enabled, then you don't need any privilege.
If it is enabled, by default, then,
You're only vulnerable if the copy is disabled.
Felix Geisendörfer 00:32:22 Okay. What is the default for Kubernetes? Is that comp enabled by default?
albancrequy 00:32:28 I'm not entirely sure. It used to be that it used to be disabled by default, but I'm not sure what it is right now. One of the attacks is like this, it's about,
Well, you need to have second disabled.
But the other, you don't need any, anything, so, just a regular session.
Felix Geisendörfer 00:32:48 The other one is the Fuse file system one, or…
albancrequy 00:32:51 Which other one did you… or the, the… I think it's true.
Felix Geisendörfer 00:32:55 advisory spread.
albancrequy 00:32:57 Yes, the, the…
Yeah, initially, I write something with fuse, but then I find out, okay, actually, you don't need fuse, you can do without Fuse.
And… But this one, you still need some kind of, to have SECOM disabled.
But for the other issue, You don't need any privilege.
Florian Lehner 00:33:22 I think it's important for people that are not aware of the context that
the advisories stall the syscall on the kernel side. So,
this couldn't… so not only eBP Profiler is affected, but every… everyone that is using such disk scores.
Yeah, I see it as a limitation on the Dinux kernel side.
And, yep.
But, as far as I can tell, there's no upstream discussion…
Alexey A 00:34:03 posing more…
Florian Lehner 00:34:04 On the Linux website, right, Albert?
albancrequy 00:34:08 Yeah, I'm not aware of any, I don't know if they are.
I was not sure if I should try to start a discussion, because I'm not sure how to do that, if that's…
I mean, if it should stay in embargo or not, I'm not sure how to approach that.
Felix Geisendörfer 00:34:37 The last thing you said was you're not sure if you should start those discussions, or… sorry, I missed it.
albancrequy 00:34:42 Yes, like, for now, I just reported the issue on GitHub in the security section.
I've not made any public things, so I'm not sure if starting a discussion on LKML
will be good or not, I don't know how to approach that.
Florian Lehner 00:35:06 The news conference do have introduced, security…
Kind of policy where discussions happen not in public.
So maybe that's an option.
So, as they are also handling CVEs recently, or started to handling CVEs.
They take more care of, handling such issues.
albancrequy 00:35:37 Okay, so then I can try to start a discussion on the security minor.
Felix Geisendörfer 00:35:44 Yeah, and one thing that I wanna do is I wanna…
double-check the details on the example you mentioned, where having control… I think when you…
there's two levels here, like, if you control an image, being able to exploit it, but if you need to control an image and the cluster itself, and make some changes on the cluster level, or Kubernetes level, or security level, I think that is, like, sort of… at that point, you've already won, like, you… you're in. But I think just the image is interesting, it's kind of… but it's still somewhere in between. I think most…
people probably don't run untrusted workloads, and I don't know if Kubernetes is even considered to be a suitable sandboxing mechanism for people doing that. So, at some point, I think it's reasonable for us to say the eBPF profiler is not a security sandbox, and this is sort of an orthogonal concern to some degree.
Where, yeah, if you don't have proper sandboxing, then…
there's not much we can do, but yeah, I guess it would be good to check with the kernel folks how they interpret the severity of this, and meanwhile, I want to double check on the…
the case where you don't need any… basically, with default privileges, you could… you could get in, I want to double-check on that. But yeah, thank you for this report, it's super interesting.
Paris (21RC)-7.07 Rhone 00:36:57 My understanding is that for Kubernetes, seccomps are not enabled by default. Like, the feature was GA'd in 1.27, and so you'd need to give a flag to the kubelet.
You enable them by default.
On the other workers.
Felix Geisendörfer 00:37:12 Okay, so seccomp is disabled by default.
Paris (21RC)-7.07 Rhone 00:37:15 Yes.
Felix Geisendörfer 00:37:19 Okay, interesting. So, though we're saying that very likely people who have control over the image could execute these exploits?
Paris (21RC)-7.07 Rhone 00:37:28 Yes.
Felix Geisendörfer 00:37:30 Okay.
Yeah, in that case, I think we should maybe engage the kernel people if we have a way to reach them that's non-public. I think that would be a good next step to get their temperature on the severity of this. Because, yeah, it's going to impact much more than the eBPF profiler itself.
Yeah, Alban, would you… would you be willing to take that?
albancrequy 00:37:54 Yes, I can…
I will follow the link, you posted for you, and I will try to do that.
I had a question about, for the Open Territory project. So far, the issues are, not public, but, there was a discussion to include Ferdiq last week, or two weeks ago, I forgot.
Should we just do that, or is it, like, an administrative issue, or…
Felix Geisendörfer 00:38:20 I don't know why Frederick was not added, I asked for it in several places, and hope it still happens. I don't know why Floyd was added and not Frederick.
Frederic Branczyk 00:38:29 Is there someone that I can ping? Because obviously this is, important for us as well.
albancrequy 00:38:38 Okay, I was in discussion with Raylan Young, Rayla Young at Kosoft, so I can ask him if he can do that as well.
Frederic Branczyk 00:38:48 That'd be great, thank you.
albancrequy 00:38:50 Cool.
Yeah, I was just not aware even.
If it's just a… technical issue, or if it is a decision. I don't know how it works.
Felix Geisendörfer 00:39:01 I think it was probably an oversight, I don't think we have any reason for not including Frederick here.
Frederic Branczyk 00:39:07 I think, technically, I'm not part of the maintainers or something like that. I think that might be why, you know, someone might have looked at a list of people and…
Felix Geisendörfer 00:39:17 And I think that's why you not got added… yeah, you didn't get added originally because of that, but…
Frederic Branczyk 00:39:21 Okay, I see.
Felix Geisendörfer 00:39:22 I don't see… yeah, Florian was also not a maintainer even, so he arguably should be, and we need to fix that as well, but… separate.
Okay,
then I think the next steps here are clear, and we'll push again on getting you added, Frederick.
And… let's see what the next action items are up here…
Jup, Alexi, you have a few. I'll just… I'll just copy those in bulk, so do it faster.
Alexey A 00:39:58 The first one, not…
not done. Yeah, but,
Okay. We'll… we'll send a protocol. I have a quick question related to this.
We discussed that, like, here we want to document that it's recommended that value… dictionary values are unique.
What about… a similar question, what about, dictionary values that are not referenced from anywhere? I would assume that that's… I don't know if it's worth documenting, but I would expect that, like.
Generally, also, like, we don't want dangling values in dictionaries.
Felix Geisendörfer 00:40:47 Didn't we have that discussion already, and concluded, like, last time that we're…
Alexey A 00:40:51 Oh, no, I think last time we discussed unique values.
Like, we discussed that, dictionaries should not have, like, values that are…
Felix Geisendörfer 00:41:01 Duplicates, yeah, yeah, yeah, okay. And remind me, the decision we made on that was, yeah, they shouldn't, but it's not invalid, right, to have duplicates.
Alexey A 00:41:11 Yeah, yes, it's kind of like warning level, like, not… like, you shouldn't have… you shouldn't have a good reason to do this, but, like, nothing will explode.
Felix Geisendörfer 00:41:20 My gut reaction would be this is the same with non-referenced dictionary entries, like, you shouldn't do that, but it's not… it's a warning, it's not a…
Yeah, I think…
Alexey A 00:41:32 I think that makes sense. Except, except the zero and index, because that one can be unreferenced.
Because we just require that it's always present. Like, the zero value that's… Yes, yes, zero, zero one is…
Felix Geisendörfer 00:41:44 Yeah, anybody against that interpretation?
If not, I'll just note we have consensus on this.
Okay, cool. Thanks for pushing that forward, and then send a PR clarifying start them duration conventions.
Alexey A 00:42:15 To do, not done.
Felix Geisendörfer 00:42:22 Okay, profile, comment, string theses as an attribute. What's the status there?
Alexey A 00:42:32 I think I had… I think I have a local pull request for this, but I wanted Florian's change to…
Florence changed to add the semantic convention for this attribute to be submitted, and I think I also wanted my other PR to be submitted, otherwise there are, like, merge conflicts. I can send them both anyway, but I just wanted to. But yeah, we should submit this soon, because comment…
the comment string indexes field is in the middle, like, somewhere in the middle of the profile field list, and it is… this shifts the, the field IDs, so…
we should… Yeah, we should… we should do this sooner rather than later.
Felix Geisendörfer 00:43:19 But it sounds like you're currently not blocked on somebody else, like, when you get a chance, you'll continue pushing forward, or…
Alexey A 00:43:26 Yeah, I'll probably just send the pull request.
Felix Geisendörfer 00:43:30 Okay.
Alexey A 00:43:39 Thank you so much, that's great. Some reviews in OpenTelemetry take, like, a really long time. Sometimes it's, like, a simple change, but, like, I'm seeing that it's just, like, waiting and waiting and waiting, and… and, like, I don't know if it's, like, polite to just, like, start pinging people directly, or…
Understood.
Felix Geisendörfer 00:43:57 Honestly, please, please, like, if I'm the one who can potentially approve, ping me on Slack with a DM, don't… you… or a thread works just as fine, but I need the direct ping, because I… my… I'm bankrupt when it comes to processing email, like… Okay.
Yeah.
Please, please pink. Thank you.
Thumbs.
Okay, Florian, PROF profile comment.
Florian Lehner 00:44:32 Yep, that's, I think that's the one Alex is waiting for.
Felix Geisendörfer 00:44:39 To get more approvals on.
Florian Lehner 00:44:41 Yeah, but I think it's more on the semantic spec…
Maintain a site, not on us. I think, Jonathan…
Felix Geisendörfer 00:44:48 Oh, okay.
Florian Lehner 00:44:49 They already approved it.
Neither.
The auto side is missing.
The other part of it.
Felix Geisendörfer 00:44:57 Okay, okay.
Alexey A 00:45:05 Yeah, so technically I'm blocked on this one, because I don't want to remove the field before we submit the semantic conventions.
Felix Geisendörfer 00:45:14 Okay, and…
Florian Lehner 00:45:14 That one is blocked.
Felix Geisendörfer 00:45:16 That one is blocked on the semantic convention approvers. How long has it been blocked? Do we need to ping?
Florian Lehner 00:45:24 My plan is to join the Semantic Convention's SIG group on Monday.
Again, and ask again for… Feedback.
Alexey A 00:45:48 It would be nice to know a good contact for each repo that we can…
Just ping in situations like this, who would kind of, like, help coordinate.
Felix Geisendörfer 00:46:12 Yes.
Alexey A 00:46:13 We shouldn't have to attend this SIG for every pull request.
That's my naive thinking.
Felix Geisendörfer 00:46:22 Yes, maybe, Florian, if you do go to the sixth, maybe you can also frame the question not just about what about this PR, but, like, who should we ping in the future instead of, like, joining the 6, maybe you can find that out.
Florian Lehner 00:46:34 The usual answer I get is go to Slack and ping the people in AutoCollector Dev.
But that feels often like screaming into the void.
So I am also doing this on a regular base.
seeing my open PRs with OTEL, usually they take about 4 to 5 weeks to get merged.
That's the reality, unfortunately.
Felix Geisendörfer 00:47:08 That sucks. What is… what Slack channel do they tell you to go to, which is one exception?
Florian Lehner 00:47:11 Hotel connector dev, I will update the doc.
Felix Geisendörfer 00:47:15 Okay, 4 or 5 weeks to get it merged.
Alexey A 00:47:22 We can try pinging Tigran, and maybe he can help Oil the necessary cogs.
Felix Geisendörfer 00:47:31 Yeah.
Alexey A 00:47:43 I can… I can send a private, like, APM to… a DM to… to Tigran, just asking for advice, that, like, we're seeing that, like.
We're seeing some simple PRs that take.
a long time to merge in semantic conventions. Do you have any advice on how to handle that? Because… and CNC, and then how that goes, if that sounds good?
Felix Geisendörfer 00:48:04 That's… that sounds good. I'm not sure if it's Tigran or Morgan, is it, like, TC or TC who owns that? But I thought it was Tigran, I take it from there, sounds good.
Alexey A 00:48:14 I think he would at least know, because he probably, like, at least has… has experience submitting many, many, many pull requests to that product… to that repo.
Felix Geisendörfer 00:48:26 Okay, let us know what you find. Thanks for doing that.
Alexey A 00:48:29 Yep.
Felix Geisendörfer 00:48:29 I'll move us on here to,
I guess, NF had an action item, reach out to SpecificationStick, about the schema URL.
Paris (21RC)-7.07 Rhone 00:48:40 Yeah, I reached out earlier today, still waiting for them to respond.
Felix Geisendörfer 00:48:49 How long ago did you reach out? How long have you been waiting?
Paris (21RC)-7.07 Rhone 00:48:53 earlier today, so I haven't been waiting for…
Felix Geisendörfer 00:48:56 Okay.
Okay, thanks for pushing that forward. And now I think we have finally managed to get through the
actual agenda items. We need to get faster than this. Anyway, Alexi, doc ULProf attribute, will we still need to…
Alexey A 00:49:18 Yes, I… I think that pull request is… well, yeah, this one is closed because we tried to first add it as a field, but then we said, like, we need to add it to, to…
to attributes, but I think we never did, and so I added this. It just, like, occurred to me that, well, this is something we still need to do. I was curious, like, Florian, if… since you're… do you want another semantic conventions full request?
Florian Lehner 00:49:49 I can try, probably not fast, but I can try.
Alexey A 00:49:55 Okay, or I will send it. I'm also happy to take it.
Felix Geisendörfer 00:50:02 Yeah, we should have one person on it who wants it.
Alexey A 00:50:08 Assigned to me.
Felix Geisendörfer 00:50:10 Okay.
Alexey A 00:50:13 I can… I… you will, you will move it to the, to the list?
Felix Geisendörfer 00:50:17 Yeah. Yeah, I will give you a… connecting here…
I guess this one is checked. Well, I'll check this off when the break has been added.
WQL.
Then the next one is, sample.
Alexey A 00:50:46 Similarly, I think we… when we removed default sample type, we had a discussion that… and I think you, Felix, had a proposal for how we can handle the order,
and, like, that we would say that in OpenTelemetry Proto, the first profile is always the default one, and then to maintain the compatibility with PProf, we would have this compatibility field that
kind of, like, of an array type that expresses the original order from the conversion, so that it can be restored in a round-trim conversion, but I don't think we added it to semantic convention, so I think this is also still to be… to be done.
And I think the… I think our round-trip converter will depend on this, because otherwise we will not be able to get
Kind of, like, bitwise copy back.
Felix Geisendörfer 00:51:37 Yes, gotcha. I vaguely remember proposing something there, I hope I wrote it down.
Alexey A 00:51:45 I think it's in a comment on the default… on the pull request that removes sample… the default sample type.
But I think the idea was pretty straightforward. Basically, capture the original profile sample order.
Like, names of the sample types.
In an attribute, so that if this OpenTelemetry proto is converted back to PPROF, or if some…
people format aware consumer consumes this OpenTelemetry proto.
they know what the profile… PROF's proto order of sample types would be.
Florian Lehner 00:52:27 And, so…
Felix Geisendörfer 00:52:28 Applying grid.
Florian Lehner 00:52:30 No, no, I just have a follow-up question.
Felix Geisendörfer 00:52:36 Well, go for it.
Florian Lehner 00:52:38 Okay, I think I did run into, when writing the converter, I did run also into the IDs. We had PProfares in function, location, and mapping, I think.
And, we don't have, an attribute or any… anything that lets us convert this ID, is it fine for the conversion from OTA to P-Prof, and vice versa, to have…
different IDs, or do we expect the round-trip conversion to be identical?
Alexey A 00:53:13 That's a good question.
I would expect that it's easier to compare if the IDs are the same, but I don't think it should be a requirement. This seems to be too…
restrictive to maintain, because technically, specific IDs are not a part of, kind of, like, semantical meaning of the profile, so…
maintaining them… It's just like…
I understand, like, comparing them would be easier, but this seems… I don't think it's necessary.
Felix Geisendörfer 00:53:46 I think I'm aligned with that. I think we need the concept of, like, semantically equal, PROFs, I guess, which arguably is not well-defined right now, but, yeah, I don't think the…
the IDs used in the dictionaries, should be considered part of the data. It's…
Just, that's part of Zincoding, it's not the data itself.
Alexey A 00:54:11 ppropCli has dash raw, command, which outputs this, like, profile as a string dump, and that one is supposed to be ID, independent.
And so, naively, I would expect that I do, like, p-proof-raw for a profile, then I do round-trip conversion, then I do p-proof-raw again, and the diff is zero.
Felix Geisendörfer 00:54:35 Mmm, okay.
Florian Lehner 00:54:38 Yeah, makes sense, makes sense. I wasn't aware of RAW and the handling of IDs, yeah, but makes sense.
Felix Geisendörfer 00:54:48 I like that if dashboard gives us basically all the data in the profile without
any details on how that data was encoded on the dictionary level, then that seems like an easy thing. We could also, if we need to write this down somewhere, what we consider to be the requirements for the round trip, defining it in terms of dash raw seems pretty straightforward.
Alexey A 00:55:10 Yes, and if this would not be the case, and people, like, if it turns out that it depends on, like, order or something, I would be, like, I think we would just fix that, because that's there, because the idea is that Dash Raw is…
He's… Yeah.
doesn't depend on the, like, IDs and things like that.
Felix Geisendörfer 00:55:25 Yeah, I guess, Florian, the PR you have opened for the specification talks about the round trip, is that correct?
Florian Lehner 00:55:32 Not directly, no.
Not directly.
Just that, we are compatible in some way, but not in our… I think I did not mention the round trip in the specification.
PR.
Felix Geisendörfer 00:55:47 Yeah, but you hinted at it.
Florian Lehner 00:55:49 taken directly.
Felix Geisendörfer 00:55:49 Should we be more explicit there, and talk about the round trip, and talk about the dash wall, or is there a better place to…
Store that.
Florian Lehner 00:56:00 I mean, if you can become more specific on the specification,
As the PR is not matched, I can just update it.
Keep it simple.
Felix Geisendörfer 00:56:21 I would be in favor of this, I think, especially since we have a pretty succinct way of expressing what we mean.
Okay, do you want me to add an action item, Florin?
Florian Lehner 00:56:41 I just wrote it down myself, and I will add it later, add it later.
Felix Geisendörfer 00:56:47 Okay, cool. Then…
Oh, but the initial thing here was the sample order attribute, we should not lose track of that.
What is it… what's needed there? Does that go into spec or stemconf?
Alexi, do you happen to know what we… where we need to find that?
Alexey A 00:57:12 Oh, so, so, sorry, say it again.
Felix Geisendörfer 00:57:15 The, the… so we dropped the default sample type, and you said we need to,
like, put that somewhere, is it a SEMConf thing?
Alexey A 00:57:23 Oh, oh, yes, yeah, I can, I can take it.
Felix Geisendörfer 00:57:27 Oh, okay, cool.
Will you add your own action item, or should I do it now?
Alexey A 00:57:39 Goodness.
I, I will, I will add it, yes.
Felix Geisendörfer 00:57:44 Okay.
Thank you so much. That's awesome.
Then I think we're through with this item, unless somebody has something else, and I would get, Frederick next on the line, talking about the line.
Frederic Branczyk 00:57:58 I mean, I think this can be fairly quick, hopefully, but I just kind of noticed this because we recently started looking into, like, source map support for JavaScript.
And we need column for that, and we did already add column to the line object in the proto, but now, as we were kind of reviewing the protocol in this regard, we were like.
Is line as the name of the message actually still accurate?
Now that we store both the line number and the column.
I don't know if I feel super strongly about this, but, you know, it could be something people might trip over.
Florian Lehner 00:58:34 But isn't the code just an attribute of the line?
Frederic Branczyk 00:58:38 It is.
Alexey A 00:58:39 It's a field, it's not, it's not…
Frederic Branczyk 00:58:44 Right. Oh, Florian, you don't mean, like, attribute as in, like.
Alexey A 00:58:49 As in, like, open telemetry attribute.
Florian Lehner 00:58:51 Yeah, not in the context as…
Alexey A 00:58:54 at the best.
Florian Lehner 00:58:55 torn.
Alexey A 00:58:56 I don't like, I don't like, I'm used to… I'm used to…
the name of line. And also, lines are… like, this is an… because in other…
It could be, like, position, something, or, like, source, source, source position.
Or coordinates, if you want to.
Frederic Branczyk 00:59:18 Positions is what we were thinking, but again, I don't feel super strongly about this, I just… we just noticed this kind of potential inconsistency, and so I wanted to bring it up, you know, as we're finalizing.
Alexey A 00:59:29 Yeah, yeah, I think it's a good question to discuss, and…
But then, when we have the inline stack, I think, in location, I think, like, having the repeated field position and saying that this is the inline stack would be… I think there, it would be a bit more confusing. It's like…
stack of positions. I think I have slight preference just towards line, but I wonder what other thing…
Frederic Branczyk 00:59:57 The business stack is not terrible either, I think.
Sorry, go ahead, Felix.
Felix Geisendörfer 01:00:06 I think I'm fine with line when I think about it, like, Florian thinks about it, like, basically the column is, like, a…
that's relative to the line, so having column embedded in line makes sense to me, but if people here want to change it, I don't feel strongly, in other words.
Alexey A 01:00:23 For example, I think in Dwarf, it's still line table.
Even though it probably also contains the column.
Frederic Branczyk 01:00:33 I don't think that's true. I think the line table only contains lines, and then it's dwarf entries that contain columns.
It's been a while since I've looked at an actual dwarf dump, but I believe it's a separate entry.
Alexey A 01:00:49 Okay.
Felix Geisendörfer 01:00:54 I guess the question is, does anybody feel like raising a PR? I don't think we'll…
Struggle with merging something if it seems like an incremental improvement, but somebody would have to go and do it.
Going once, going twice.
Frederic Branczyk 01:01:11 It doesn't seem like there's a, like, huge outcry, so I'm fine with just leaving it as is then. I just wanted to make sure that we have talked about it.
Felix Geisendörfer 01:01:21 Okay.
Okay, we had two more items from Alban, which were out of time today. Alban, is it possible for you to join next time again?
albancrequy 01:01:45 Sure, I think the security policy, we already discussed it on the other line. I just wanted to mention, I'm working on augmented PBPF provider, because I want to use it in this beta gadgets, and that's fine, I'm working on that. I'll put the link, that's…
Felix Geisendörfer 01:02:02 I think the Inspector Gadget people were on this SIC meeting before, some other people working on that, if I remember correctly, but that's super interesting. I guess we can talk more about it in future meetings if you want to join again.
albancrequy 01:02:15 Yes.
Thanks.
Felix Geisendörfer 01:02:18 Cool, awesome. Then, thank you, everybody, for showing up and doing a lot of work in between these meetings, and, wish you all a nice local time.
Paris (21RC)-7.07 Rhone 01:02:28 Thank you, Ron.
albancrequy 01:02:30 Good night.
