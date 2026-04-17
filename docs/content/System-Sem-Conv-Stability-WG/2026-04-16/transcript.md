SIG: System Sem Conv Stability WG
Date: 2026-04-16
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/t2MGv2s07jjQAjKx4hg-fI6WFMVWO73-fKa1MlJROl7StM0WCFBhc75qyDYWm0bK.XPD1XoTgBkZAf9oW
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:45 Hey, Dimitri.
**Dmitrii Anoshin** 04:07 How doin'.
**Donal O'Sullivan** 04:10 Hey, Dimitri, how are you?
**Dmitrii Anoshin** 04:12 Well, how are you?
**Donal O'Sullivan** 04:14 Good, yeah, good. Busy.
**Dmitrii Anoshin** 04:19 Interesting that no one else joined so far.
**Donal O'Sullivan** 04:23 Yeah.
Nearly 5 minutes.
Oh, that's it.
**Fairly OddParents (ca-wat-brt3)** 04:34 Go.
That's convenient.
Hello, how's it going?
**Dmitrii Anoshin** 04:40 Hi, Braden.
**Donal O'Sullivan** 04:41 Hey, Braden.
It's an interesting meeting. Is that it… that's the meeting room name? Is that a fairly odd.
**Fairly OddParents (ca-wat-brt3)** 04:50 You know, it is.
**Dmitrii Anoshin** 04:51 Yeah.
**Fairly OddParents (ca-wat-brt3)** 04:52 The floor is all named after Saturday morning cartoons. That's the theme.
**Donal O'Sullivan** 04:58 Okay.
I thought it was a bot at first, it was like… Yeah.
Interesting.
**Fairly OddParents (ca-wat-brt3)** 05:09 I don't know if we'll have anything… anyone else today, I mean… So I think Christos is on leave.
Roger's in Australia, and Pablo said he can't make it.
I think… The only pressing thing to discuss is the HTL hash, which I think is ready to merge anyway.
**Donal O'Sullivan** 05:34 Yep. Should be good.
I think it's been approved by everybody, right?
**Fairly OddParents (ca-wat-brt3)** 05:41 Yeah, I'm pretty sure.
**Donal O'Sullivan** 05:43 Yeah, just need the maintainers to actually… I think all the comments are resolved as well, so… yeah.
And profiling.
I've approved it as well, so it should be good to go.
**Fairly OddParents (ca-wat-brt3)** 06:01 And I think… Oh, I didn't… I didn't notice that I was asked to review and close the conversations. Okay, I will… I'll go back and do that on the moving process executable to its own entity PR, and then I think… At that point, the release candidate PR is basically unblocked, and we're… we're in release candidate mode for process, which is good.
**Donal O'Sullivan** 06:30 Yeah.
**Fairly OddParents (ca-wat-brt3)** 06:36 I guess the only other thing to talk about related to that is… is how we… Start adopting it in the collector, which is sort of blocked on… You know, how we're going to… define the… How we're gonna manage the double writing.
Because we want to be able to support both schemas at once.
**Donal O'Sullivan** 06:58 Yeah, yeah. Yeah, I was talking to Roger about this today, and the two of us are gonna work on that next week, and hopefully we'll have, like, the two… the two different approaches, and we can just discuss it on the open issue, and then we can all just come to an agreement, whatever approach you guys prefer, we'll just go with that.
Does that make sense?
**Fairly OddParents (ca-wat-brt3)** 07:20 Cool, yeah, I think that makes sense.
**Dmitrii Anoshin** 07:22 Sounds good. Thank you.
**Donal O'Sullivan** 07:25 Yeah, it might take… I guess it might take a couple of weeks just to kind of hammer it out, but… Yep.
**Fairly OddParents (ca-wat-brt3)** 07:32 That is okay.
Does this matter? Just give me one sec just to make sure this is an important call.
**Donal O'Sullivan** 07:47 Yeah, I think I've somewhat of a working POC anyway, so I'll just, kind of… Fix it off a bit, and… Yeah.
**Fairly OddParents (ca-wat-brt3)** 08:00 Sorry, that was a spam call.
**Donal O'Sullivan** 08:02 Yeah, nice. Yeah, no, I was just saying, I have somewhat of a working POC, and I think Roger does as well, so I'm gonna sync with him on it, and we'll just… yeah, we'll see where it is, and then obviously we'll bring that to you guys.
Written.
**Fairly OddParents (ca-wat-brt3)** 08:16 Sounds good.
**Donal O'Sullivan** 08:17 Then… Roger also wanted me to bring an issue today. I know, I know you're… you guys… Braden, I know you're aware of it, but it's the… I have it there in the meeting agenda. I put Roger's name beside it. It was just the guidance for representing the aggregation interval for pre-aggregated and window-based metrics.
**Fairly OddParents (ca-wat-brt3)** 08:40 Yep.
**Donal O'Sullivan** 08:46 Yeah, so… yeah, Iwiki just wanted me to bring it here so that we can have a discussion on it.
And… I think the big thing was… Sorry, sorry. Go ahead, anyway.
**Dmitrii Anoshin** 09:04 I don't think we have anything to discuss regarding that. We discussed that extensively last time. At this point, this is something that we potentially can bring to this pack, probably just joining the spec call and bringing that issue there, and see what people from, like, from GCU think about it.
Like, it's probably… too late to introduce another native field in OpenTelemetry?
**Fairly OddParents (ca-wat-brt3)** 09:32 Yeah.
**Dmitrii Anoshin** 09:33 But… At the same time, it's not a breaking change, and potentially, it can be done.
So, if it's a, like, just native field, recap.
Anyway, if it's native field, it means that potentially it can be part of the identity, and we can just remove that part from the metric name, but that's gonna break a lot of… a lot of stuff on the back.
So maybe we can have, like.
some semantic convention kind of guidance, let's say… Like, suffix with, With the aggregation, but at the same time, aggregation… like, it doesn't make sense to put it everywhere. Like, for example, does it mean that CPU system CPU usage now has to, has to have it.
Right.
Maybe… another alternative is that it can be… As a native field.
For something that… let's say, cannot collide.
Like, for example, metric that has only one window.
It can… that window can be… Set in the new native field, but if the same measure has several windows that are typically supposed to be emitted.
Potentially, it can be part of the metric name as well.
**Fairly OddParents (ca-wat-brt3)** 11:11 Yeah.
**Dmitrii Anoshin** 11:11 negative field, something like that. Anyway, it's just, like, just thoughts, but we have to bring it to the spec.
**Fairly OddParents (ca-wat-brt3)** 11:19 Yeah, there is… There is something to be said about… The, the fact that backends are… Not necessarily designed right now to have a new… another new identity dimension like this one. Like, right now, the metric name and the attributes, most backends are considering that the identity of the metric, and In that… in that regard, adding the Adding the duration as a suffix to the name Lines up well with what current backends are doing and how they're interpreting that.
**Donal O'Sullivan** 11:55 Yeah.
**Fairly OddParents (ca-wat-brt3)** 11:58 So there is something to be said for that.
**Dmitrii Anoshin** 11:59 Yeah, but do we have to put it everywhere in that case, even for the metric that… don't have duration, a window as a…
**Donal O'Sullivan** 12:09 In their name, yeah, you'd have to add it to all those names, wouldn't you?
**Dmitrii Anoshin** 12:12 like.
**Fairly OddParents (ca-wat-brt3)** 12:13 Any… yeah, there…
**Donal O'Sullivan** 12:14 Yes.
**Fairly OddParents (ca-wat-brt3)** 12:15 Yeah.
for, like, this, the system CPU utilization, for example, like, it doesn't have a window right now, you know, I think… I think that's actually just, like.
like, a bad thing. Like, I think we've kind of swept under the rug the fact that the duration… the window by which it's aggregated is not part of the metric at all, and it's mostly… kind of worked anyway, like, I guess… Dashboards, just kind of… Like, figure out that their collection interval is the same rate that they need to be making their dashboards out of, but… Like, it would be better if it somehow encoded the actual, like, dynamically encoded the window. Like, when the host metrics receiver produces system.cpu utilization, it could come with a .60S or something, like, to show that it was a 60 second, but That would… potentially be very annoying if you're trying to filter against that metric in your, like, OTTL pipelines and stuff. Like, if it has a dynamic suffix to it, like, that would be super annoying.
**Dmitrii Anoshin** 13:27 Yeah, and if you want to…
**Fairly OddParents (ca-wat-brt3)** 13:28 reserve.
**Dmitrii Anoshin** 13:29 And if you want to change the interval, you don't expect the metric to change.
Yeah.
**Donal O'Sullivan** 13:35 Oh, yeah, yeah, yeah.
**Dmitrii Anoshin** 13:40 So that's what I'm saying, if we can at least have a new field that will be… Kind of.
Same as we have… same meaning as we currently have for… unit, right? Unit is not part of the identity, but it provides some valuable information.
**Fairly OddParents (ca-wat-brt3)** 13:59 Yeah.
**Dmitrii Anoshin** 14:02 Potentially, something like that can be addressed.
**Donal O'Sullivan** 14:05 They have something like metadata added onto the metric, or something like that, is it?
**Dmitrii Anoshin** 14:09 Yeah, the native field of the OpenTelemetry signal. We already have a few of them, like description, we have unit, we have everything.
**Donal O'Sullivan** 14:20 So the next step is just join the, the spec sig and… Propose this, is it?
**Dmitrii Anoshin** 14:26 Yeah, I guess so.
**Fairly OddParents (ca-wat-brt3)** 14:28 at least open the discussion. I've put the spec seg on my calendar, so at the very least, I'll be there.
Nope, maybe we can… we can discuss it there.
**Dmitrii Anoshin** 14:37 Let's try there.
**Donal O'Sullivan** 14:39 I can… I can try and join it, just even to… just to hear.
But what… when is it?
**Fairly OddParents (ca-wat-brt3)** 14:46 It's… I… in Eastern Time, it's Tuesday at 11.
**Donal O'Sullivan** 14:51 Okay.
Yeah, it should be awesome.
**Fairly OddParents (ca-wat-brt3)** 14:55 It's in the second slot of the hotel working group calendar.
onto…
**Donal O'Sullivan** 15:00 Tuesday.
11… yeah, I guess… Yeah, I guess Roger won't be able to make that call then.
**Fairly OddParents (ca-wat-brt3)** 15:09 No, probably not.
**Donal O'Sullivan** 15:10 No, okay.
**Fairly OddParents (ca-wat-brt3)** 15:11 But I think… I think him and I are mostly aligned on, like, what we need to figure out.
**Donal O'Sullivan** 15:20 Alright, yeah, I can comment back on the issue and just, say that… we've discussed it, and next steps is just to attend the, Spec Sig and… And get their feedback, if that works.
**Dmitrii Anoshin** 15:34 Sounds good.
**Donal O'Sullivan** 15:35 Cool.
Rudy.
I hope nothing else goes in it anyway.
**Fairly OddParents (ca-wat-brt3)** 15:48 Yeah, I don't think I do either.
**Dmitrii Anoshin** 15:50 Cool. Nothing from my side either.
**Donal O'Sullivan** 15:54 Okay.
**Dmitrii Anoshin** 15:55 Thank you, also.
**Fairly OddParents (ca-wat-brt3)** 15:55 call it a little early then. Thanks, everyone.
**Donal O'Sullivan** 15:57 Cheers, guys. Bye-bye.
**Fairly OddParents (ca-wat-brt3)** 15:59 That's fine.
