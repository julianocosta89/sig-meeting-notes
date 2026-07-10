SIG: Profiling WG
Date: 2026-07-09
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Christos Kalkanis** 06:31 Hey, folks, so it's been 5 minutes. Should we start? I'm trying… I checked on Slack. Felix is not online. I reached out to Felix.
No, sorry.
**Nayef Ghattas** 06:39 So Felix is on parental leave for the week.
**Christos Kalkanis** 06:41 Okay.
Okay.
Okay, cool.
I guess Alexi may join later, he's usually, and Florian said… Yeah, so Florian, he's not going to join from the beginning, too. Okay, let me open the agenda.
All right.
So usually what we do at the beginning of the meeting, we go through the agenda, and we look at the action items that we have, and we review those first, and then we get to the new items for the week.
So we can start with that. First one is Alexis. He's not here, so let's skip. And if Alexis later joins, maybe we can go back to this.
Florian is not here either, so now if… Open GitHub issue on including GitHub.
OTLP versioning payloads.
**Nayef Ghattas** 07:53 Yeah, I didn't get the time to. It's a bit more than a Github issue. I think we want to write a document that explains why we want to do this. I didn't have the time to do it, but I hope that I'll be able to do it this week.
or next week.
**Christos Kalkanis** 08:06 Okay.
Okay, cool.
Actually, share my screen.
So the next one is mine. This is about the specification pull request I opened a long time ago. So this is now ready for merge. It's got the second approval that it needed. So I reached out to Tigran, and he should be merging it quite soon, I imagine.
So… Alexi, what's the next item?
who can skip it, and then Evil.
Let me see… Ivo is not present either.
Update thread context OTAP with appendix of a ghost report. I guess we can take a look.
By the way, I think my impression, because I went over this last week, Evo reached out to me to do a final pass for this OTEP, which is the Threat Contacts OTEP. I approved it. My impression is that it's… Almost.
Ready to be merged, I think, so I expect this to be… Milestone, yeah.
**Nayef Ghattas** 09:21 Yeah, I think it has all the approval from the specification SIG.
So yeah, probably. And all the approvals we need from the profiling Sig as well.
**Christos Kalkanis** 09:33 Yep.
**Nayef Ghattas** 09:34 I think we only did one very small change this week, which was the The last, one of the last commits. I don't know if it's the last one or the one before, based on Timo's feedback that he brought up when we were implementing the spec in the open telemetry Epf profiler.
Oh.
preclude the need to look up things in SimTab. I think that's the…
**Christos Kalkanis** 10:06 Okay.
**Nayef Ghattas** 10:07 The only major change since then. Oh, Evo is here.
**Ivo Anjo** 10:13 Oh, hello. Sorry, I was late.
**Christos Kalkanis** 10:16 Oh, hi, Evo. We are just discussing your item.
The action item from the agenda, so maybe you can, yeah, you can take it from here.
**Ivo Anjo** 10:23 Yes. So basically, the current state here is that we got the green ticks from Josh, the green tick from Josh. So now we have like four from the… Big people. So I'm hoping that we'll get someone to press merge on it soon.
And yeah, I'll keep, like, attending the specification SIG meetings until, I don't know, morale improves, and we get, like, some some some feedback on that.
And the other thing is that we also have the PRs to implement this in the eBPF profiler. I know that I think with Christos has been commenting on it. So thanks. And I guess like if more people can.
Can take a look at it.
yeah, we'll be able to hopefully address the any feedback and get it merged soon in the Bpf profile.
**Christos Kalkanis** 11:18 Okay, great. So, yes, I was commenting on the process context. I'm trying to get, the process context PR, like, we have a final open PR there, so we need to get this in. And Timo left some comments yesterday about the structure of the package.
Because the process context, when the code was first introduced, it was part of the process.
Under… it was under process, and then Florian left the comment that he would prefer if it was a standalone package, so then… It became a standalone package called Process Context. Now it's at the root of BPF Profiler. Timo thinks it's confusing to have a Process Context package at the root.
So we should just move it somewhere else, essentially.
And that would be the thing we can… That's process context. And then let's take a look at thread context as well. Timo left some comments there as well in terms of where to put it. Like he would like to see it in interpreter.
If I remember correctly.
But yeah, let's focus on that. I think process context is mostly done.
**Nayef Ghattas** 12:22 I think, for thread context, we wanted to implement it first as an interpreter. But the current interpreter Api doesn't allow us to implement it. So if if we wanted to do this, we need, we'd need to extend a bit the interpreter Api in the profiler.
I haven't had all of, Timo's comments, but I… I wasn't sure if there's something that we we were open to to extend the interpreter Api to.
to do this.
**Christos Kalkanis** 12:56 Actually, I think he left the comments on the process bound experience. I'll find it here because I was looking at it. Yes.
Okay, yeah, so here it is.
**Nayef Ghattas** 13:33 Okay, probably haven't caught up yet on this. Okay.
**Christos Kalkanis** 13:36 Okay.
Okay.
All right, so I don't think we have any other action items for the agenda. And Alex is still not here, so let's go back.
So, if Alex joins, but we also don't have any other items.
From what I've seen.
Maybe… I don't know.
Would you like to introduce something for discussion?
**Ivo Anjo** 14:11 Is everyone in summer mode?
**Christos Kalkanis** 14:13 Yeah, I guess.
**Ivo Anjo** 14:15 It's,
**Christos Kalkanis** 14:16 On my end, I've been super busy with other things also because Elastic delayed off 20% of the engineering.
Departments like Created, chaos, essentially. So we're dealing with the after effects right now.
**Ivo Anjo** 14:38 Sucks.
**Christos Kalkanis** 14:40 Here.
Okay, I guess, yeah, I mean, if we don't have anything else to discuss, we can… Stop here, and then… get 45 minutes back, I guess.
**Ivo Anjo** 15:01 Sounds good.
**Christos Kalkanis** 15:02 Yeah. Thank you. Take care.
**Ivo Anjo** 15:04 Keep cool, everyone. Bye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 15:05 Bye. Bye.
