SIG: CI/CD SemConv SIG
Date: 2026-11-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:22 Hey, good day.
**Christophe Kamphaus** 01:25 Hello.
How goes up.
Fine, aren't you?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:31 But okay, thank you.
**Christophe Kamphaus** 01:41 I do have a few updates this time.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:44 Alright.
**Christophe Kamphaus** 01:47 So, I was asking in the SemConv meeting about the long-running spans.
And the proposal to define semantic conventions for… Spend life cycle events, and Yeah, they basically told us to go back to the spec.
So, I will join the SPAC meeting.
In Nova.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 02:13 Okay.
**Christophe Kamphaus** 02:14 I also, did prepare a draft.
Once, as a craft OTAB, Once as an, Semantic conventions.
Changes.
Basically showing what an hotel span event would look like.
Let me post it in the agenda. It's the second one.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 02:49 Alright.
**Christophe Kamphaus** 02:49 I can share my screen, and we can also go over it.
If you want.
I can walk you through it.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:03 Yeah, whatever you want to do.
**Christophe Kamphaus** 03:11 Here we go.
So it's a main discussion.
Was on this issue.
Basically, this came from… Spec.
Where they said, yeah, we should define semantic conventions.
I did some research, had, explored summarize.
Any past developments on it, past discussions?
And yeah, it's already started, pretty early, so we're… There is some history behind it.
Yeah, and there's open questions about it.
Basically, comes down to the design.
How should these events look like?
What should be the merge semantics be?
If you have multiple events for a single span, And how do you… reconstruct the span based on that. If you have delta.
Attributes, or if you just send changes, you would need all of them.
We'd see the last event be… everything.
So, yeah.
I took some… No, it's on it also.
Some main points that's crystallized out of that research.
than yesterday.
I, I went to the SemConv meeting with it.
And the feedback I got is that… Great work, but it should probably be discussed in the spec.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:59 Yeah, makes sense.
**Christophe Kamphaus** 05:00 Yeah, yeah, especially if we are talking about generic.
span events that would also go into the hotel namespace.
It needs the blessing of the spec.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 05:12 Yeah, for sure.
**Christophe Kamphaus** 05:15 So yeah, there was some discussion comparing it also to the H-Trace model.
What's the game?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 05:25 each trace model?
**Christophe Kamphaus** 05:27 Apache, I don't remember.
Let me check… No, it's Apache h choice.
So, apparently, that had started under the Vance.
Yeah, I also learned something new, sir.
So, based on that feedback, I… I drafted an, OTAP, I didn't post any API yet.
Just as a guest for now.
So I will discuss that one.
And how the spec wants to move forward.
My idea was here is that We could reconstruct the full span based on the ended event.
Which… comes… I thought about the GitHub events, basically, how those could be transformed into spans.
Based on just a single event.
But if you… So, in that case, you could lose some intermediary events and just We see last event reconstructs a full span.
The other way around would also work.
You could have just started an intermediary events.
And if you lose the ended event after… It times out, you don't get any heartbeat anymore.
you could… Reconstruct an incomplete span, but… still have most of the attributes on it.
So the attributes would merge.
What you could not express based on that is if attributes were removed.
on, the SDK.
I don't know if that's… possible at, possible today, but it's something to discuss in the spec.
Yeah, also, the names would be discussed, and all the fields would need to be discussed.
So yeah, I created this, so… We could have a basis for discussion.
Yes, there's also a lot of prior art.
Different companies producing their own events.
Josh also had a prototype in the past.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:23 Yeah.
**Christophe Kamphaus** 08:26 And I also created, My own branch, in my own repo, just to show what it would look like in the semantic conventions.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:40 Cool.
I don't know if I'll be able to attend, today's… I've got, like, two back-to-backs.
During that time. But if I can hop over, I'll try to hop over.
**Christophe Kamphaus** 08:52 Yo.
Yeah, feel free, if it's… Works out for you.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:58 the, at least for the GitHub event, like, they don't have any type of attribute.
That would conform to any of this.
We just take, some of their started at, And… completed app.
Attributes, and that's how we create the… Span, start and end.
Times. I would basically just map them, and then put them in a span.
Was it, Dagger?
I think Dagger just omitted the span early without an end time, and that was how they were able to do live spans.
And in their UI, they would be like, okay, well, like, here's the start of that time, but let's run a calculator showing that it's progressing. And then when the span was done, and was re-emitted as a complete span, they just use that.
**Christophe Kamphaus** 09:54 Yeah, so it was always a full snapshot of C-SPAN, if I remember right.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 09:59 Yeah, yeah.
Gets emitted once… when it starts, and then it gets emitted again as to the same span when it ends, with both values.
**Christophe Kamphaus** 10:11 But I think also in the middle, any heartbeat, it was just a full span each time.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 10:17 Yeah, yeah, sounds right.
**Carlos Alberto Cortez (Dash0)** 10:19 Where in-depth, in… in implementation you are talking about?
**Christophe Kamphaus** 10:24 Dagon.
**Carlos Alberto Cortez (Dash0)** 10:26 Okay, yeah, right. So, basically, in every HD, you're getting the full span data.
**Christophe Kamphaus** 10:32 I think so.
**Carlos Alberto Cortez (Dash0)** 10:34 Oh, interesting, I didn't know that. I thought they were only sending the, because, you know, like, for the, my prototype, which I didn't have time to work on, basically, every time something is added or updated, you're sending We are forcing a heartbeat, let's say.
And that's, of course, when an attribute gets added, or updated.
or span… or a span link is added as well, but you are getting only that piece of information. So basically, the backend has to keep track of what you know, what has been said before, and… but the good thing is that I only said they only get a delta, you know?
**Christophe Kamphaus** 11:13 Yeah, yeah, that was also a part that I thought about in my draft here.
That probably we should just send deltas, At least for the heartbeat.
Because… That's the events that you would send often.
Span takes hours days.
It would send a heartbeat event every X second, so that would be a lot of data.
It makes sense to use DevTOS there.
Yeah, that was my main update. I also saw and put on the agenda Oh, is that C-Spec 1?
Mmm… Sperm metrics and a proposal to rename them.
That came out of discussions in SemConv… To align spans and span duration metrics.
And one of the CICD metrics would be part of that rename.
Oh no, that's just the spend times that were renamed.
And so there is an open proposal.
Rename it like this.
What do you think about it?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 13:11 I mean, the CAD pipeline run duration stuff is stuff we already… Views.
Yeah, is that CV? Yeah, that's Subaru.
**Christophe Kamphaus** 13:20 Current metric.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 13:22 Yeah, but from a generic perspective.
I don't know.
**Carlos Alberto Cortez (Dash0)** 13:39 Well, I think that for version control system, there makes sense, by the way, to have client and server. For CAD, I'm not sure that we… you need to put server. I don't know whether we plan to have CAD client, for example, by the way.
**Christophe Kamphaus** 14:00 Yeah, I don't think so.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 14:03 Agreed.
**Christophe Kamphaus** 14:07 It's basically implied.
**Carlos Alberto Cortez (Dash0)** 14:13 I think that, in that regard, that could be probably, fine if this was a brand new metric, but if we are, like.
Changing the name, even though this is unstable, I would probably prefer not to, but…
**Christophe Kamphaus** 14:27 It's, stability, it's release candidate, if I remember right.
But yeah, it's been so long that it… we should probably consider it.
A de facto stable.
**Dotan Horovits (Amazon Web Services, Inc.)** 14:43 I'm also in favor of, Less changes to things that are widely used, and less really necessary.
We're in struggle now to reach this formal stability, and part of that is, like, showing people they can really rely on things that we've released, so… Should be also very top priority for us as well.
**Christophe Kamphaus** 15:04 Yeah, so probably I will comment on it.
That we shouldn't rename the metric.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 15:14 You're in… Yeah. And honestly, from, like, a red metrics perspective, if there's spans, I'd just be using The red version of them.
**Christophe Kamphaus** 15:30 Yeah, without relying on the metric itself.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 15:34 Yeah. Yeah, I just use the regular span duration.
Juan.
**Christophe Kamphaus** 15:45 Oh, he thinks there is something…
**Dotan Horovits (Amazon Web Services, Inc.)** 15:46 Any, just, sorry, just to make sure I understand, is there any case, just curious, in which the span duration would be different, diverging from this one? Like, intuitively, what Adriel says makes sense. I'm just wondering if there are any specific cases where it should be two distinct durations?
**Christophe Kamphaus** 16:07 No.
It's more that C-spend metric… Or, spend metric durations.
Would always match that one.
for HTTP.
The names match as well. So there, it's… you have HTTP server, And, The HTTP server duration metric match.
And this naming scheme.
**Dotan Horovits (Amazon Web Services, Inc.)** 16:42 Okay, so there's no use case in which these should be different from each other. So, essentially, referring, for example, to the span duration should always match this, right?
**Christophe Kamphaus** 16:55 Yes.
**Dotan Horovits (Amazon Web Services, Inc.)** 16:56 Okay, makes sense, just to make sure.
**Christophe Kamphaus** 17:02 what I also wanted to say is there is some work around specifying… Codifying what's been… spend metric.
Should be in spec.
But yeah.
I just saw it, I'll sync.
So that's it from my site.
Anyone else have something to discuss, or any questions about what I showed?
**Dotan Horovits (Amazon Web Services, Inc.)** 18:09 Nope.
**Christophe Kamphaus** 18:16 And here, have a nice day.
And maybe see you later in the session.
**Dotan Horovits (Amazon Web Services, Inc.)** 18:20 Actually, just very quickly, if we have time, less about the technical and more about, I don't know if you've seen, some of you might have missed it, but Hotel Unplugged is going to take place next year, 2027, Auto Unplugged Europe.
again, as a, as a fringe of, Fossum. Same, same format, same, location even the day after.
So, just flagging it, because it's really around the corner, given also the holidays, the end of year and everything. It's beginning of, like, end of January, beginning of February.
This specifically is beginning of February, but for those who come to Fostom, I mean. So, just wanted to flag that, and obviously, be great to, to see folks, They're, Christophe, I know that you're also based in Europe, so hopefully… and last time I met you at Fosterone, so hopefully.
**Christophe Kamphaus** 19:17 Yeah, I saw the blog post, and I already registered for Hotel Unplugged.
**Dotan Horovits (Amazon Web Services, Inc.)** 19:23 Amazing, amazing. So, yeah. So, just want to put it on everyone's radar, I think it's a good, just to share the experience for those who haven't had the chance to attend, that it was, like, An unconference with, roundtables and, you know, essentially topics that were solicited by the crowd and discussed by the audience, the participants, and… I think it's a great place to bring up topics, including, by the way, even the CAD graduation, and other types that are top of mind for us, and of course, engaging others.
groups and other topics, so… Christophe is already bought in, but for those who are considering, each one with their own constraints, obviously, but highly recommended, and of course, closer to the event, I'd love to see… I'm hoping to be there, and, Hoping to see, to maybe closer to the event, see who is going to be there, and, maybe use it also for, for this group and this forum.
To get together, and to get other folks, engaged, and so on. So, just putting it on everyone's radar, I'll add the link. Thanks for adding it on the agenda items. I will quickly add the links after the meeting.
And, yeah, and if anyone, of course, has any questions about that, I'm happy to just share from my experience from last year. Last year was the first time, by the way, for Europe.
But, happy to try and answer, and
**Christophe Kamphaus** 20:59 Yeah, thanks for shouting that out.
**Dotan Horovits (Amazon Web Services, Inc.)** 21:03 Yeah.
**Christophe Kamphaus** 21:03 I hope to, hope to meet you there.
**Dotan Horovits (Amazon Web Services, Inc.)** 21:05 Yeah, so I'm really hoping that it will work out to be there, and And yeah, I had quite a few chats about this, even the… having this event taking place again with folks from the GC and from others, I think it's a very, very valuable Format, and, lots of the, maintainers, and, and, and SIG leads and so on are actually here, based in Europe, so it definitely makes things easier for many of us to come together on the Europe edition, so really happy that we got to convince them, and they pulled it off, and it worked with the venue and everything, so… I nudged a few folks about that, probably some are tired from hearing from you about that, but really happy that it's happening, and again, if you do have an option, or if you're anyway coming for FostDam, which is the main, I guess, the bigger one, then definitely consider sticking around for an extra day. It's in the same city, so… Just the following day.
Anyway, just want to know that, and of course, again, if anyone has questions, whether now or offline.
Ping me, happy to, to answer anything about that. As far as I know, of course.
Oh, and one last thing, it's unrelated, but of course, we're looking for more community sponsors to support the event, so if your company is into the domain, and it aligns with the interests, feel free, of course, to also share. We're trying to get, This part sorted out as well.
**Christophe Kamphaus** 22:46 Yep.
Thank you.
**Dotan Horovits (Amazon Web Services, Inc.)** 22:48 Thanks.
**Christophe Kamphaus** 22:52 If there's nothing else, then have a great day, and see you next week, or later today.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 22:58 Thanks, y'all, take care.
**Dotan Horovits (Amazon Web Services, Inc.)** 23:00 See you folks, take care.
**Christophe Kamphaus** 23:02 Bye, bye.
