SIG: Rust SIG
Date: 2025-07-15
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Scott Gerring** 00:44 There are other people around.
**Zhongyang** 00:46 Yeah. Just a few minutes late.
**Scott Gerring** 00:49 No worries. I saw you all started editing the document just after I wrote that no one was here, so I came back in.
Does anyone have anything they want to talk about?
**Zhongyang** 01:16 We have a plan for the Spam Api spam process Api refractor Pr, which has been open for like 2 months.
**Scott Gerring** 01:28 This is Paul's 1. Right? I think that's.
**Zhongyang** 01:30 Yeah, I'm sure. Let me find it and paste it here.
hmm!
Oops!
Bombed it as well.
I mean it's so. I may review it last month seems new good to me, but it seems names are failing.
Oh, should we just fix and linked and merge it.
**Scott Gerring** 02:33 Are there any other outstanding questions on it?
Cj. Says nothing.
What? What's it breaking again? Sorry. I've lost context a little bit on it.
**Zhongyang** 02:49 As they just change the function. Signatures introduce a new readable span trait and and modified on end function to pass a finish span. So basically, we introduced a kind of a different type.
Different stage of processing. I would say the readable spam is still readable, and finish that one after you end after the spam has been ended.
**Scott Gerring** 03:19 Yeah, it's the. It's the on end. That's breaking, isn't it? That's the main.
**Zhongyang** 03:24 Yeah, it's a public function.
**Scott Gerring** 03:32 Yeah, I mean Cj's comment. There was just please add an entry to the log file to the change log.
**Zhongyang** 03:37 Yeah, I mean, I can probably do that. I haven't seen Paul wrong.
and I haven't been wrong myself worth few weeks. I'm sorry apologies for that. Should we just.
**Scott Gerring** 03:47 Sorry.
Sorry.
**Zhongyang** 03:50 Do we? Just I mean, we can push. Just push a commit fix later and merge it.
**Scott Gerring** 03:56 I can. I can ping Paul. I was talking to him earlier and ask him if he wants to fix the lens so we can merge it.
**Zhongyang** 04:02 Yeah, I don't think there's a too much trouble. If we speed it with something else, we can just fix the name there for me.
**Scott Gerring** 04:13 I'll I'll reach out to him and ask him to fix the line. And should we also just suggest, on the thread to Cj that we merge it? Or are we happy to do it with that.
**Zhongyang** 04:22 I mean, we can probably ping him as that channel. See that he has any other comments other than the entry entry logs change entry.
Yeah, I think that's my most of.
Otherwise I think we should move sooner than later.
**Scott Gerring** 04:49 Yeah, cause it'll it'll slowly diverge, and then it'll be a pain.
I'll I'll write him right now on the the Datadog channel. I think that should kick him into gear pretty quickly.
**Zhongyang** 04:59 Sounds, good thanks.
**Scott Gerring** 05:28 Cool. Is there anything else we should talk about.
**Zhongyang** 05:32 Not sure what's what's going on? What's going wrong in the last few weeks?
Do you guys, did we get any traction in terms of the Tokyo Turkish racing versus Otr. Tracing store.
**Scott Gerring** 05:48 It's just dragging on. I think that thread on the other side bounces back and forward slowly.
**Zhongyang** 05:55 Oh!
**Scott Gerring** 05:56 Yeah, it would be a really good one to get rid of.
**Zhongyang** 05:59 It's just basically they have been slow to respond.
**Scott Gerring** 06:04 Yeah, I haven't. I was just off for 2 weeks as well. I'm just opening it up again.
But yeah, the last I saw was, it was just like quite a slow feedback cycle on both in in both directions.
I think the issue is always here. It's effectively semi unsupported, I mean in the sense that there's no one who's dedicated significant time to maintaining the crate, and then any large changes, or fraught with risk.
**Zhongyang** 06:40 Interesting.
**Scott Gerring** 06:41 Yeah, yeah, I'm at a loss with it.
The last comment was was Gurn last week saying that he's made the changes that were requested.
**Zhongyang** 06:55 If tracing is state is, if the lack of development work is because of tracing is stable enough for the time being, that no one's asking for new stuff, or just because they were pivot to something else.
**Scott Gerring** 07:11 Yeah, it's hard. It's hard to know nice.
**Zhongyang** 07:17 Yeah, I don't see anything pop up to try to replace Tracy. To be honest, so my guess would be Tracy just stable enough, and Miss meets the requirement of normal use cases, maybe 90% of use cases.
And then people just happy with it.
**Scott Gerring** 07:34 Yeah, and people not trying to use the other signals through the open telemetry Apis, and not realizing the correlation issues there, I guess.
Yeah.
**Zhongyang** 07:45 Cool.
**Paul Le Grand des Cloizeaux** 07:47 Yeah, yeah, so, hey, everyone.
**Scott Gerring** 07:52 We were just talking about you.
**Paul Le Grand des Cloizeaux** 07:55 I have ears behind my head, you know.
**Scott Gerring** 08:01 There's the one. So for the Pr, for the refactor that you've had in for a while. There's there's 1 failing lint on it that looks pretty straightforward.
We would suggest that if you fix that we'll give Cj. One more chance to have an opinion about it, and then it should be good to go, but it seems like all the review feedback has been addressed.
**Paul Le Grand des Cloizeaux** 08:21 Yeah. So I actually, we discussed about that with Cj last week.
and he was of the opinion of putting every breaking change to the trace Api in one Pr, and so that I split it into the breaking changes and the non-breaking changes.
and we, the next release, would contain only the non-breaking changes.
But of course I'm also happy if we can merge it as is, and.
**Scott Gerring** 09:00 This is being actively held open then, until the next release has gone through and then merged afterwards.
**Zhongyang** 09:07 Yeah, I think to you means we have to do environment. It's not necessarily one pr, so as long as we get everything else into every other breaking, changing to the main tree. Before the next 3 days we should be good to go.
**Paul Le Grand des Cloizeaux** 09:22 Yeah.
**Zhongyang** 09:23 So it's worth creating a blocking, blocking with these tracking issues. We don't forget about it in 2 2 exhaust.
**Scott Gerring** 09:32 Yeah, it'd be good to mark that up on the Pr. I guess I'll just write a comment on the bottom, saying that unless somebody else would like to.
Or actually, Paul, do you want to do that quickly? So I'm not misrepresenting what you just told us.
**Paul Le Grand des Cloizeaux** 09:54 Yeah, sure I will put that in the comments of the Pr.
Here, here we go. Thank you.
Yeah.
Well, yeah. So the thing we talked about last week was that basically there was no breaking change in the next release. And so Cj. Wanted to do like a batch a batteries, I mean, yeah.
since we're on 0 dot something.
it wouldn't be a minor release, but technically a minor release.
And so put the Burnetians like them. So that's that's what I'm gonna and.
**Scott Gerring** 10:52 Cool.
I personally have nothing else to discuss. I don't know if anyone else has any points.
**Zhongyang** 11:04 We want to plan for next release.
I mean, I have a sense of this is, gonna be a few weeks or a few months I've seen like with this one. I've seen these 2 blocking issue. We need to resolve before that. So it is so not to get into a get into the next release anytime soon.
2, 9, 6, 2 is one. That's the other. One is the way. Regress the performance of a spam process a little bit by introducing read right now.
which we should probably get rid of.
So another one is this one?
Oh, yeah, it shows.
Oh, yeah, we'll change it. Exporter. To have a reader mark which is necessary for this. Pr, because the mutable reference to it once we we every method take a immutable self reference. This should go away.
So this is another blocking issue. I say, we need to resolve before that 3 days.
So just wonder if anything, anyone have anything else in terms of release time, or if you just wait until those 2 resolved, I guess my question is, is there any reason we should release sooner than later.
**Scott Gerring** 12:42 Yeah, I, personally don't really have a strong view on it.
**Zhongyang** 12:47 Okay, no, that's we just wait on those 2. Resolved.
Then we'll erase the new version.
Anything else we want to discuss.
**Scott Gerring** 13:11 Oh, good on my side! Good cash!
**Utkarsh Umesan Pillai** 13:15 Yeah, nothing from my end, either. Sorry, guys, I haven't been following the spam Api like the Pr's that we are discussing today in the last meeting.
Hey, young man.
**Scott Gerring** 13:34 Cool. Well, I guess in that case have a lovely day or evening, everyone, and chat soon.
**Zhongyang** 13:39 See you guys soon.
**Scott Gerring** 13:41 Cheers, bye.
**Zhongyang** 13:42 Bye.
**Paul Le Grand des Cloizeaux** 13:44 Bye.
