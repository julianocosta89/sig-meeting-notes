SIG: Rust SIG
Date: 2025-07-01
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/Dq3SYoUPvDQ22nlTayd7zAU95qE02cthWylmju0lKjK6SFaa9ZCNX9wQzWDYLOQj.n3I0oC7I1r4FZttc
============================================================

## Zoom Recording Transcript

**Cijo Thomas (Microsoft)** 01:43 Hey! Hello!
**Utkarsh Umesan Pillai** 01:47 Hey? I see Joe.
**Cijo Thomas (Microsoft)** 01:49 Don't have anything in the agenda.
maybe wait for a couple of minutes.
All asked to review the refactoring of span processor Api.
That's probably the only thing in the agenda. There is nothing else.
**Utkarsh Umesan Pillai** 02:20 To you.
**Cijo Thomas (Microsoft)** 02:34 Not seeing the share screen button. Okay, it's back all right.
This is the Pr, it's pulling us to review. I think it's it has some approvals.
**Utkarsh Umesan Pillai** 02:58 Yeah, looks. Like, yum, yang.
**Cijo Thomas (Microsoft)** 03:00 Yeah. It's a good.
**Utkarsh Umesan Pillai** 03:01 Full time.
**Cijo Thomas (Microsoft)** 03:02 Sure how much of a breaking change this is. It says it's a pretty breaking change, you know.
One thing I want to like make a call before we merge is.
since this is a merge breaking change, and we expect more breaking changes would like to see if we can club, all breaking changes into a single release, as opposed to making subsequent one, which also has breaking changes, because, though the bulk of the breaking change will come from removing, like some things from the span which are not supposed to be in the span to begin with.
but that requires the tracing integration to be done which is not yet done.
Sell how to check like, how bad of a breaking changes is before we oh, merge it, pick, else we'll have like sequence of releases all of them with breaking changes.
Yeah, that's the only thing this might be restricted to SDK folks only given its processor.
Yeah, anyway, I'll need to take a closer look. I also don't know whether there is a statement here which doesn't look correct me. It says SDK. Prohibits mutation on span on end. That's correct. Spec says you cannot mutate it on end.
However, it says, modification done in one processor should not impact data passed to other processors.
Okay.
**Utkarsh Umesan Pillai** 04:51 Kind of deviating from our log officer behavior here.
**Cijo Thomas (Microsoft)** 04:55 Thing like the spec says any changes done in one processor should reflect in other processor. That's what the spec says, because you can chain it.
But I'm not sure what Paul meant by this statement.
Yeah, one thing which I can see here is if it's not mutable on on end. Then the second point is kind of irrelevant, because, if you cannot modify it.
then the point about modification should be reflected in the next processor is kind of think that may be? What Ford is suffering to?
You need to check like. What do we do in on? Begin then? Because in own begin also, we are supposed to like change. So any changes done should be reflected in the other.
Yeah, this request, like, some more time for me to review.
Okay, yeah, don't think we need to. Sorry review it right away, but let's preview it. Offline.
Doesn't seem to be any other topics. So let's quickly review the milestone and end the call earlier.
So we had to otlp exporter release, which we don't have a good date.
and we also have the next milestone, which is point 3 1.
This one is also Tbd.
You have to depending on, like, how how much breaking change we take, or whether we take non, we could do it this point 3 0 dot one instead of breaking it, because my main worry is like we. We have a flow of changes which which will be like breaking and I'm not sure we have the bandwidth to touch all of them right now.
Yeah. So let's keep it. I think this is yeah. This is the one which has a bunch of clicking change. All of these are like breaking changes.
Yeah. So we just need to wait to see how much progress we'll make on the tracing integration, because the moment we have tracing integration fixed, then we can start doing all these things and call it breaking change. But finish all the code, all of them in one short.
**Utkarsh Umesan Pillai** 07:33 Hmm.
**Cijo Thomas (Microsoft)** 07:36 Okay, yeah. So I'll just wait. For the tracing progress beyond. Said, it's being reviewed, yeah, this one.
Okay, that are some discussion. But no, not much other than that. But at least it's progressing. It was completely stalled. So it's making some progress.
Okay, yeah, that's pretty much the end. Yeah, there are like few discussion going on in the slack channel where ted was asking like, What's the overall story with tracing?
We don't have a good answer, or or at least we don't have a written down answer. So that's unfortunately, we just have to spend more time right explicitly writing down. What's the end state would look like with the tracing integration, how? How it would look like so and as of now, yeah, no return answer. Maybe it's good idea for me to write down and then make sure everyone has the same idea as me.
Yeah. Any other things which anything you had in mind to discuss. If not, we can end early.
**Utkarsh Umesan Pillai** 08:53 No, not really.
**Cijo Thomas (Microsoft)** 08:55 Okay, was there anything in the last week? I.
**Utkarsh Umesan Pillai** 08:57 No last week when I joined, nobody was there, so I just ended the call after like 5 min.
**Cijo Thomas (Microsoft)** 09:14 Okay, yeah, if that's the case, we can give back time. See you later. Bye, bye.
**Utkarsh Umesan Pillai** 09:18 Okay. See you soon. Bye.
