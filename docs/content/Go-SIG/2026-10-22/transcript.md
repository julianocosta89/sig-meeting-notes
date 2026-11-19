SIG: GO SIG
Date: 2026-10-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Puneet Singh** 02:37 Hello.
**Tyler Yahn (Splunk)** 02:40 Hey, how's it going?
**Puneet Singh** 02:43 I'm good. Am I audible? I'm using somewhat low-quality… head form. Yeah.
**Tyler Yahn (Splunk)** 02:51 Yeah, can you hear me?
**Puneet Singh** 02:52 Yeah, yeah, clear.
**Tyler Yahn (Splunk)** 02:53 Okay. Yeah, yeah, yeah. Yeah, no, I can hear you.
Yeah, just, getting signed in and things.
**Puneet Singh** 03:04 I didn't see any activity at the start, so I was thinking, is no one going to be joining today, or, like, usually there's a lot of buzz at the start of the meeting, right? Everyone adding their agenda items.
**Tyler Yahn (Splunk)** 03:17 Yeah, yeah, I think these later meetings, it's more of a North America one, and… Not always, people show up.
Right. For this one.
But yeah, I mean, like… It's, it's a… I don't think there's gonna be a lot of activity. It's probably one that will end early, actually.
**Puneet Singh** 03:38 Cool.
**Tyler Yahn (Splunk)** 03:40 But, yeah, I mean, I don't know if there's… do you have anything you wanted to talk about?
**Puneet Singh** 03:45 Nothing, I'm, I'm… Inactive as planned for the… rest of the October. Meter configurator is still there. I'm planning to… I just want to check if it's feasible to include in the next release.
Which is 1.48.
But I don't know when it's going to be cut from the master.
Do you have any idea?
**Tyler Yahn (Splunk)** 04:14 No.
I imagine it's gonna be a little while.
Maybe… maybe next week, actually? That's actually a good question.
So, probably,
**Puneet Singh** 04:40 I also wanted to ask, actually, that when we create the release milestone.
Would be possible to put some sort of date, which is, like, one or two week… You know, tolerance with the actual date, actually.
**Tyler Yahn (Splunk)** 04:55 Yeah, we can, we can definitely do that, but we normally don't, just because, like, we don't have a normal release cadence.
For certain things that we have tried to hit milestones on, like, that are timeline sensitive, like, we will add a date on them, so, like, when we did, like.
1.0s, or we're trying to hit, like, certain goals for KubeCon, we normally will add them there, but, Yeah, I don't… We… I don't think we had, like, a really strong push… to get this one out. This is mostly just bug fixes, there's not a really big amount of… feature… sorry, I'm looking at your, PR right now. The only other thing is, like, I saw Robert had left a comment But he doesn't have a review, but…
**Puneet Singh** 05:43 Yeah, I think, from my side, there were two PRs. One is the meter configurator, and another is the high debit.
Another is the… the exclusive rejection, which only… which rejects more than one experimental option, those two, I think.
Nothing else on my side.
**Tyler Yahn (Splunk)** 06:06 Yeah, I mean, this looks ready, so I'm actually gonna hit this, version ready. I think the only thing that's blocking it right now is conversations have to be resolved.
I'm trying to find the ones that are not resolved.
But…
**Puneet Singh** 06:21 I've left it purposefully open so that, you know, those who have, like, created the the feedback… They're also content with the status, actually, so, yeah.
**Tyler Yahn (Splunk)** 06:34 Yeah, I… so… That's reasonable.
I would say… be more proactive about it. There's… it's rare that you have… people go back and resolve the conversation. Like, I think… I think what it is, is, like, I can speak personally, like, if I leave a review… And you address it.
The first thing I'm gonna go look at is not your response to the comment, it's the code. And if the code doesn't look like it's been resolved, then I'll go back to your comment and see, like, if you, you know… you know, addressed it or not, or if you did address it, like, what it is, and that's where that it goes, so… Clicking the resolve comment, or the resolve… actually signals to the user that, like, you think that you've actually addressed it, rather than, like… Yeah, so I would probably recommend going in that direction, but it's also a little easier for, like, at this point, when I'm trying to get this thing merged, to know that, like, oh, actually, like, you have addressed all these things, and it's just, like, the, you know, the person who originally made the comment hasn't come back and taken a look as well, But it's understandable why that's not exactly clear.
Yeah, I still can't… I don't see any other unresolved comments at this point, but… It's still not wanting to merge it.
**Puneet Singh** 08:06 I understand, I mean, okay, nevermind.
**Tyler Yahn (Splunk)** 08:09 Oh, there we go. Okay, it's, it's queued. Okay, alright.
Sorry, this is also new. Why is it queued?
**Puneet Singh** 08:19 I don't know.
**David Ashpole (Google LLC)** 08:21 We have a merge queue now.
**Tyler Yahn (Splunk)** 08:23 Yeah, but, like, what's… why… what's blocking it? Like, why hasn't it just merged?
Oh my god.
**David Ashpole (Google LLC)** 08:30 Good question.
**Puneet Singh** 08:31 What about the automation that Damien was talking about, that once it gets the required approval, it will auto-merge?
**Tyler Yahn (Splunk)** 08:39 Yeah, that's what it's doing, but, like.
**Puneet Singh** 08:42 But you had to hit the mush button, right? So it is not automated.
**David Ashpole (Google LLC)** 08:45 I thought there were two things. One is whether… Once it gets two approvals, it automatically enters the queue.
And the second is the queue itself.
The queue is nice, because you can… Simultaneously click the Q button on 20 PRs.
And then… go get a coffee, and they'll come back.
You know, maybe a day later, and they're all merged, right?
But I guess you still have to click the, like, join queue button?
**Tyler Yahn (Splunk)** 09:17 Yeah, that's what's going on here. And it says something about, like, estimated time to merge in the queue is, like, 17 minutes?
**David Ashpole (Google LLC)** 09:27 I don't know if it requires, like, some resource? Like, we have some… you know, GitHub action thing that's… gonna run… And do…
**Tyler Yahn (Splunk)** 09:38 No, it's like, it restarted its entire CI.
**David Ashpole (Google LLC)** 09:43 Interesting. So being up-to-date is really pointless now.
Exciting the update.
**Tyler Yahn (Splunk)** 09:48 Yeah.
**David Ashpole (Google LLC)** 09:49 You know what I mean, right? Like…
**Tyler Yahn (Splunk)** 09:50 No, yeah, I do. Yeah, it is, it is 100%.
**David Ashpole (Google LLC)** 09:53 Remove that button, I think, right? Because there's a setting that lets you click update branch.
**Tyler Yahn (Splunk)** 09:59 Yeah.
**David Ashpole (Google LLC)** 10:00 And, like, nobody should click it anymore.
Because it's gonna do this anyways, even when it's already up to date.
**Tyler Yahn (Splunk)** 10:05 Exactly, it's just gonna thrash CI, like, unless you need to resolve conflicts, but then it still lets you do that, even if that button's not… yeah, okay.
Yeah, I think that's the right way to do it, because it, like, if it goes into the queue and has to rerun the CI anyways, like, it's kind of like, what's the point of… yeah, okay. Right, right.
**Puneet Singh** 10:22 And anywhere you get much conflict, so if it is not mergable, you have to dissolve it anyway, so…
**Tyler Yahn (Splunk)** 10:27 Right, right, yeah, exactly.
Well, okay,
**Puneet Singh** 10:32 It's cute.
It's emerged.
**Tyler Yahn (Splunk)** 10:34 In a little bit, yeah.
**Puneet Singh** 10:35 I'm still in doubt that… what Damien did, how does it benefit? Because if you still have to… cue it yourself, actually. So, whereas… how does… It is…
**Tyler Yahn (Splunk)** 10:47 Well, you don't want it to be fully automated. Like, you definitely don't want it to just, like… automatically, like, merge things without, like, some maintainer saying, like, yeah, we should merge this.
So, like, that adding to the queue is the human approval side of this thing.
**David Ashpole (Google LLC)** 11:04 I think… Approvals stay, even if someone, like, pushes a new commit, right?
Or, I don't.
**Tyler Yahn (Splunk)** 11:11 Remember what?
**David Ashpole (Google LLC)** 11:12 the thing is for that. I think that's the…
**Tyler Yahn (Splunk)** 11:15 They do, technically.
**David Ashpole (Google LLC)** 11:17 We have contributed.
**Tyler Yahn (Splunk)** 11:17 docs that say that, like, if substantial, like, changes have been made, you should be requesting new reviews on the pull request manually, because, like, we didn't want to just, you know.
Yeah, we didn't want to clear them because we merged in main or something like that.
But yeah, that's more of a manual process, so… correct, yeah.
**David Ashpole (Google LLC)** 11:37 I think if you add something to the queue.
Even if they push a new commit afterwards, the thing that was… Present when you click to add is the thing that gets merged.
**Tyler Yahn (Splunk)** 11:47 Excellent sort of, like, thing.
**David Ashpole (Google LLC)** 11:49 Because I thought that was… maybe I'm making things up, but I thought that was the point of the, Like, that was the safety that comes with the queue.
Or maybe it jumps out of the queue, I don't know.
**Tyler Yahn (Splunk)** 12:01 I think it jumps out of the queue, but yeah, I might be… I also maybe don't know.
Yeah.
**Puneet Singh** 12:09 I don't… have a look at PR again, the one that Damien has raised.
Just to understand that what part it basically… Shortcuts, essentially.
**Tyler Yahn (Splunk)** 12:23 Yeah. Yeah, I gotcha.
**David Ashpole (Google LLC)** 12:26 I think it's, in theory, super helpful for, like, Dependabot renovate stuff.
**Puneet Singh** 12:31 Oh, yeah.
**David Ashpole (Google LLC)** 12:33 There's no complex, because… The main thing the queue should let you do is, if you have 20 pull requests you want to get in.
Like, let you queue them all up.
And then hopefully, like, at least half of them drain through, and you don't have to spend your day.
**Puneet Singh** 12:50 Right, rather than clicking one and then coming back and then hitting another. All right, all right, yeah, that makes more sense, actually.
Cool.
**Tyler Yahn (Splunk)** 13:01 Well, cool, yeah, it's in… it should be merged in 20 minutes, it sounds like.
I still have to go back and look at the thermos and meter provider conflicting option thing, but looks like David reviewed it, and so it's just a matter of… yeah. But it should be included in the next release, based on what I'm seeing.
**Puneet Singh** 13:21 Cool.
**Tyler Yahn (Splunk)** 13:24 Yeah, when that goes out, I don't exactly know, but, yeah.
**Puneet Singh** 13:28 That should be fine.
**Tyler Yahn (Splunk)** 13:30 Yeah.
Cool.
Well, I don't, David, do you have any other topics, you wanted to discuss?
**David Ashpole (Google LLC)** 13:40 I don't think so. The thing on my mind has been… Like, if Robert was here, we could talk about… plans for the OTLP, like, just to check in on that, but I don't know if there's a point without him here.
For the OTLP logs export, or GA, because I'd love to… That's the only thing that's on my mind for, like, in before KubeCon.
Hmm.
**Tyler Yahn (Splunk)** 14:05 Actually.
**David Ashpole (Google LLC)** 14:06 Otherwise… For finish, you're doing the instrument types one at a time, right? So I'm… I, I think I…
**Tyler Yahn (Splunk)** 14:15 Got it.
**David Ashpole (Google LLC)** 14:15 Get those as they come in.
**Tyler Yahn (Splunk)** 14:17 The up-down counter and the, the gauge, yeah, currently.
**David Ashpole (Google LLC)** 14:21 Definitely.
**Tyler Yahn (Splunk)** 14:22 open.
And then the histogram aggregation stuff is, draft PR right now. I was just, I didn't really, I think it's a draft.
Actually, I might have clicked the button last night.
If not, it's ready to go. Like, I just didn't want to, like, overload the reviewers. If you wanted to take a look, I guess I could probably also do it, but just, yeah.
**David Ashpole (Google LLC)** 14:41 We'll plan to do all of the finishes.
And then… come back to Bound Instruments, maybe, as, like, a… Process thing, or… I don't know if we wanted to pick that back up, now that we have some precedent for… How we want to integrate.
**Tyler Yahn (Splunk)** 14:57 I don't see why we wouldn't… like, we could start on the boundless stuff now.
**David Ashpole (Google LLC)** 15:01 Okay.
**Tyler Yahn (Splunk)** 15:02 Yeah, like, I think it's just more about… Fighting time.
Like, it's… yeah, like, it's just more about that, yeah.
**David Ashpole (Google LLC)** 15:12 Okay.
**Tyler Yahn (Splunk)** 15:12 Yeah, because, I mean, like, I don't think there's anything… like, the only other thing is, like, the exponential histogram might be a little weird, because it always is weird, but… I actually don't think it's gonna be too weird for the finished stuff, but for the bound instruments stuff, like… Actually…
**David Ashpole (Google LLC)** 15:25 I just merged that PR today, the… The same map stuff.
**Tyler Yahn (Splunk)** 15:29 Yeah, I saw that.
Yeah, I meant just more, like, like the, yeah, the… the general pattern for the finish method, I think, is, like, kind of… Established at this point.
So, like, if there's any, like, conflict, I'd be, kind of odd.
So, yeah, like, if you wanted to start on, like, the bound instrument stuff and, like, splitting it off in the same thing, like, one instrument at a time, or doing something like that, like, I think that that's… I don't know how you want to split it, but, like, I think it's ready. Like, I don't think there's any…
**David Ashpole (Google LLC)** 16:02 Quickly.
**Tyler Yahn (Splunk)** 16:03 conflicts will show up now, rather than in, like, a few more PRs.
But yeah, I think that's all set.
**David Ashpole (Google LLC)** 16:12 We need… I think we discussed this last time, but we do need… it to be possible to use bound and finish instruments together.
**Tyler Yahn (Splunk)** 16:22 I mean, I think that'd be cool, but I don't know of an explicit case that we need it yet. Like, probably… probably an Obi, eventually, but, like… I… I don't have data to tell you that we need that right now. Like, I know we need the finished instruments in Obi, There's maybe, like, an overhead issue, because, like, we're… doing a little bit of a difference in, like, our implementation than what Obi did for finish, that, like, maybe there's, like, a performance hit that we would want to, like, then go for these optimizations with the bound instruments, but, like, it's not, like… no, it's not.
Critical to get that in right now.
**David Ashpole (Google LLC)** 16:58 Cool.
**Tyler Yahn (Splunk)** 16:59 Yeah.
**Puneet Singh** 17:02 Actually, I also raised the question about I was confused, and as in what scenario the bounds to maintain the finisher where Singh instruments fit together, actually.
Because, from what I've seen, the spec-bound instrument is… more about you have fixed cardinality, or small… small cardinality?
And… That is not changing, you don't have any options, and you know that you'll be recording with respect to that fixed set of cardinality options you have.
Whereas in case of Finnish.
obvious instruments, it's more like that. A particular, unique set would be used for, some… Interval a process represents, and then it will go away, so it doesn't make sense to retain it.
So… I mean, any example of that where both will… can fit together, actually? That's what I'm trying to understand.
**Tyler Yahn (Splunk)** 18:09 Yeah, I mean, I think it's just, like.
you know you have a process that's gonna run for a set amount of time, so say, for the next hour, you know that this… this is gonna be used, so you go and create a bound instrument for it. At the end of that hour, you know it's not gonna be used, so you need to, like… if it's a cumulative, like, counter, like, that'll… that'll just persist for the rest of the service lifetime, right? So… If you can finish that and say, like, okay, now I… this is done.
It'll go away, and the cardinality goes down even more.
Cardinality is about, like, internal storage for the OTEL SDK, but it's also about, like, the downstream, like, telemetry platforms, right?
If they keep ingesting the same… Like, metrics, like, that'll keep their carnality up as well, so if you can reduce that number by saying this is done.
It'll stop exporting it.
**Puneet Singh** 19:09 Yeah, I got… I think I got caught up in a particular point and got stuck to that, actually.
But yeah, it makes sense. I'm just thinking that what… what would be more costly, Paying normalization costs in each request, or… Or creating a bound instrument.
for, the… attribute set that you know that it's not gonna change, and then just finish it using the finish-aware sync instrument.
**Tyler Yahn (Splunk)** 19:45 Well, the bound instrument is more about quick access for measurements, right? So every time that you want to make a measurement and you don't have a bound instrument, you need to do that, like, hashing in the.
**Puneet Singh** 19:56 Right.
**Tyler Yahn (Splunk)** 19:56 of an attribute set, which includes that, like, allocations.
So they're kind of… they're orthogonal. They're not really, like, in the same optimization pathways. And so, that… that is about, like, you know, if you're gonna be doing… A million requests per second for an hour.
Probably want to get a bound instrument for that if you know beforehand what those attributes are going to be.
But at the end of the hour Like, then it's more about just cleanup, like.
You know that those are never going to be used again, so then you just want to remove them.
**Puneet Singh** 20:31 Yeah, I mean, yeah, it makes more sense in that way, actually, yeah.
**Tyler Yahn (Splunk)** 20:35 Yeah.
Yeah, they're… I mean, they're… they… they… like I said, like, they're not… they're not competitive. Like, that's why, like, having them work in the same way is, like, it gives more tools to the end user of ways to get, you know, increased, or decreased resource usage. Yeah.
**Puneet Singh** 20:54 top right.
Yeah. Thanks, thanks for explaining, actually.
**David Ashpole (Google LLC)** 20:59 I think the other funny thing is that in our case, it's probably actually going to be more performant to use bound instruments even If it's not long-lived.
**Tyler Yahn (Splunk)** 21:10 Yeah, long lip's relative.
Right? If it's, greater than 100 microseconds, is that long-lived?
Because maybe…
**David Ashpole (Google LLC)** 21:17 Even if it was… Even if it churns on every… Even if you recall bind on every request.
Right.
**Tyler Yahn (Splunk)** 21:28 I don't know about that.
That… That, I think, is… no, I don't know about that, but… Okay.
I could see that being equivalent, but, like, eventually, like, Yeah, I think…
**David Ashpole (Google LLC)** 21:45 just, like… I don't know if you remember this, because it's been a few months, but this is just, like, the API thing, where We always… You always allocate.
**Tyler Yahn (Splunk)** 21:54 Even… even when you're constructing it by an instrument, you have to go through… like, okay, so you construct it by an instrument, and it's quick because you're just doing a hash, and then you have to do, like, the actual measurement recording?
You still have to create the set.
**David Ashpole (Google LLC)** 22:09 Whoa.
Not the dog.
**Tyler Yahn (Splunk)** 22:11 Doing the lazy, the lazy measurement, like, construction, like…
**David Ashpole (Google LLC)** 22:14 You just have.
**Tyler Yahn (Splunk)** 22:14 Period.
**David Ashpole (Google LLC)** 22:15 look upright.
That's only on the first time if it's in memory, right?
**Tyler Yahn (Splunk)** 22:20 that's what I'm saying, like, so if you're continually churning, like, why is that.
**David Ashpole (Google LLC)** 22:23 Oh, I see.
**Tyler Yahn (Splunk)** 22:24 Equivalent?
Like, yeah.
**David Ashpole (Google LLC)** 22:26 Sorry, I meant, like… Even if you aren't, like, saving them at all. Like, you're reconstructing the bound instrument on every… every call.
**Tyler Yahn (Splunk)** 22:37 But you're not, like, doing a one-off thing.
**David Ashpole (Google LLC)** 22:40 Right, instead of, like, trying to save all the bound instruments.
**Tyler Yahn (Splunk)** 22:44 Yeah. Somewhere.
**David Ashpole (Google LLC)** 22:45 You're just.
**Tyler Yahn (Splunk)** 22:45 The lazy, the lazy construction set is what you're saying? Yes.
**David Ashpole (Google LLC)** 22:48 Right, yeah.
**Puneet Singh** 22:50 I have, two questions. One is that… Once you create a bound instrument, you get a reference. What that reference looks like, I'm not sure yet. I haven't looked at it, the sec… I mean, as a part of same question, the request for recording always comes in form of… Attribute set, right?
So…
**Tyler Yahn (Splunk)** 23:16 Kind of, so… So, you have to remember that there's, like.
two ways to identify an attribute set, right? A set is like a unique… collection of attributes that are, like, not duplicate, right? And so you can represent them in memory, because you can do a sorted like, collection of it, and another way to represent that is to take a hash of that. And that hash is another, like, pseudo-unique, representation of that exact same collection. It's just not a one-for-one reproduction, like, of the memory space.
So there's two ways you can reference it. One is by literally, like, comparing the bytes of the full thing, and the other is by comparing the hash key that you generate, right? So this optimization comes in because, like, the hash key is actually pretty cheap to compute.
And it doesn't require… well, you can make that hash key… creation not require allocations under the heat? The set… Construction does require an allocation under the heat, because… what you pass is not what we can actually store and what we can guarantee due to the uniqueness and the deduplication requirements that I just said. And so, like.
because of that, like, set construction requires memory, like, access on the heap versus the, the hashing, right? So if you can build this bind instrument in a way where all you're doing is just looking at the hashing construction, and then, like, storing a reference to that hash.
Then what you can do.
**David Ashpole (Google LLC)** 24:41 You can work.
**Tyler Yahn (Splunk)** 24:42 weight.
until the actual set is needed, to be constructed, and you can reconstruct that at the last possible moment, essentially during the measurement, and you can do it once, right? You can say, like.
okay, I'm actually gonna do a measurement, like, I need to actually put this into, like, some sort of persistent storage, like, here's the full attribute set, do it now, and then every single time you use the bound instrument, or any sort of, like, reference from a new bound instrument, it'll just use the hashing, and since that set's already been constructed, it doesn't do any more allocations.
But if you are trying to just do a completely, like, you know, separate recording of a measurement, every time that you pass in those options, you have to construct that attribute set from the start, and it passes it in. So, like, it's required to do memory allocations at that point.
So it gets around this memory allocation, like, boundary that you have to do per measurement, and, you know, off-puts it into, you know, once per first measurement, is how that gets worked out.
**Puneet Singh** 25:36 So, I understand the part of the instrument creation.
But about recording, which happens at the much faster rate. That request is also going to contain the… the attributes set, or, you know, some sort of attribute with respect to which the recording has to be made. So… how that… part… I mean, that part also needs to be converted to the hash representation in order to find the bound instrument, respective bound instrument, right?
**David Ashpole (Google LLC)** 26:06 making… when you make a measurement, there's really two steps, right? The first is that you're doing a lookup in a map.
To get a handle on the atomic integer that you want to update, say if it's a counter.
And then the second step is actually You know, making the update to the atomic integer, right?
What Bound Instruments lets you do conceptually is split those two operations into two separate API calls.
So when you call bind, It's the equivalent of doing the map lookup.
And then when you call add, it's the equivalent of just doing the add.
So if you… Bind an instrument to an attribute set.
It already has that attribute set looked up, and the thing that gets returned is more or less Like, a reference, or, An increment function, something that is gonna just directly do the atomic counter add with no lookup when you call add.
Does that make sense?
**Puneet Singh** 27:13 It does, I'm… Thinking more from a use case that… from the, you know, from the request point of view, that What kind of use case will already… Keep the hash to the… hash key to the bound instrument.
And also contains the representation of the attribute set, which has, Which represents the exact hash key, actually, that, do these requests Kind of already know in advance that… what bound instrument they have to use, so that the creation app happens only at the start, and then we know that all the requests representing this particular attribute set, so they don't have to do that, The deduplication and the hashing of the attribute set in order to find the binder store.
**Tyler Yahn (Splunk)** 28:13 Yeah, like, yeah, we definitely have, like, a lot of examples. You can even see, like, our self-observability. There's definitely a lot of instruments that we have that are, like, static attributes that we know… we know when we're building them, like, from the start, what they're going to be.
And so… even ones that you don't know from the start, but you know that are gonna be long-lived, you can figure this out. So things like… Like, say a request, if you don't have, like, a path in it, like, or you have, like, a templatized path.
Right? And you're gonna store the method, you're gonna store the templatized path, and all these sort of things, like, you can just create the instrument from the start knowing that that's actually gonna be there. If you're gonna look at, like, export counts, and say, like, hey, these are the number of successful export counts, like, you just know, like.
hey, here's this function, like, it's just gonna get incremented each time, like, that's all you need to do. Things comes in, like, what happens when… That metric for export counts, like, also captures an error, and that error is completely… like, unique. Like, that needs to be, like, a new thing.
But, to David's point, though, that, like.
it needs to be a new thing, but it's… it still can actually be optimized using this Bound Instrument API, because, like.
even in that situation, you say, like, look, I don't know what this error is, I don't know if it's ever been seen before, but I'm gonna pass this in to the Bound Instrument API and say, like, okay, give me the bound, like, retention of this, and I'm gonna increment whatever comes back.
It may be the case that, like, it's already actually seen it, so what that bound instrument is gonna provide for you is it's gonna go through, like, this lazy path, and it's gonna say, like, actually, you've already, like, seen this, I'm just gonna give you this previous reference to it.
And now when you're actually gonna do this measurement, like, it'll… You know, avoid that second structure from the start.
Yeah, it's actually… It's actually more common than you may think if you look through semantic conventions, for metrics that you will know what these, like, attribute, carnality and, like, what the dimensions of them are gonna be.
from the start, by design. Like, semantic conventions actually are kind of, like, that's why we design the semantic conventions the way we do, so that, like, you can reduce carnality, and the one way to reduce it is to, like.
not have a lot of, like, dynamically generated, attributes, which usually results in, like, you will know them from the start, which really helps and leverages this Bind, API.
**Puneet Singh** 30:37 Yeah, I think, yeah, that makes sense, actually.
The other question was that, you know, going forward.
I mean, I'm assuming that there will be some sort of blueprint, would be asking for some… some boundary conditions… I mean, boundary as in that… beyond what cardinality limits or beyond what requests per second I should consider bound instrument versus the regular API, I mean, I guess…
**Tyler Yahn (Splunk)** 31:12 more… actually, I think it's more about, like, I think it's simpler than that. I think it's, like, if you're… If you are performance conscious and you want to use this API, you should look into Bound Instruments.
If you don't, and you just like a convenient API, like, then just don't worry about them.
you know, like, there's a nice, convenient API where you can just build the attributes and maybe your code looks cleaner to you that way, like, just go about it that way. But, like, if, like… you really care about this, then start looking into them, I think is more the case that we would probably put it as.
**Puneet Singh** 31:48 I mean, because the way it looks like, that bound estimate could be, like, a very really efficient version of… of… Regarding the measurements with the… with the given condition of the fixed cardinality, actually. But… but yeah, I think overall, it makes sense. And thanks for explaining both things, actually.
**Tyler Yahn (Splunk)** 32:09 Yeah.
Yeah, I mean, really efficient and performant is, like, subjective, right? Like, yeah, if you're doing some high-frequency trading thing that you're trying to instrument, like, probably really important if you're… running a demo app, and you need some insight into it, probably don't care, right? Like, so, yeah.
**Puneet Singh** 32:27 Got it.
**David Ashpole (Google LLC)** 32:28 I think the… The other thing that you might not be aware of, because, you're relatively new, is that Prometheus has.
instruments as their primary way of recording metrics in their client library.
And if you, you know, Google search Prometheus versus OpenTelemetry performance or benchmarks or anything.
There is… there are a lot of people who, for whatever reason, care a lot about Some of the… the performance of some of these benchmark cases, so… It's kind of been a long-standing, like… This is one of the cases where, OpenTelemetry GO Metrics performs quite a bit worse than you would get with the Prometheus client.
But it's an opportunity for us to close the gap, I guess.
So, a little bit of, like, Friendly, competitive, rationale, too.
**Puneet Singh** 33:26 No, I think that's a good info. And definitely, I'm asking these questions because… I've only seen the open OTL API, and then that's… that's where my imagination of the use cases is, actually. But… but yeah, it… it… it makes more sense day by day, I would say. So, yeah.
**Tyler Yahn (Splunk)** 33:53 Cool.
Well… Still nothing on the agenda. I didn't… I mean, I had just those… PRs I was talking about earlier, actually, I think I had them open.
I did make the explicit bucket histogram reviewable, so I do have 3 PRs open.
But yeah, those are the only things that I think stand out.
They needed a review, but otherwise, you could probably just end the meeting early here, unless folks had other things they wanted to talk about.
**David Ashpole (Google LLC)** 34:25 I think so. Oh, I will, open the next PR.
For exponential histograms. I'll implement the circular… Circular storage.
I think it's next.
**Tyler Yahn (Splunk)** 34:38 Oh, okay.
**David Ashpole (Google LLC)** 34:39 Look out for that.
**Tyler Yahn (Splunk)** 34:41 Sounds good.
**David Ashpole (Google LLC)** 34:43 Cool.
**Tyler Yahn (Splunk)** 34:44 Okay.
**David Ashpole (Google LLC)** 34:44 Cheers.
**Tyler Yahn (Splunk)** 34:45 Talk to y'all later.
**Puneet Singh** 34:47 2…
