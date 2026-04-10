SIG: Sampling SIG
Date: 2026-04-09
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/H0Wq2y5M8nosjgWQAZvzgkskv8Z0WiqwgYxy0EonE74hPr4gI65aaafFrjxFdLkw.iPYbxVz6ZfG6E7cu
============================================================

## Zoom Recording Transcript

**Chris Marchbanks** 01:23 Hello, Amar.
**Otmar Ertl (Dynatrace)** 01:35 Hello?
**Chris Marchbanks** 01:38 Apparently, I should try talking before joining the first meeting of the day, my voice did not work at all there.
**jmacdonald** 03:32 Hello, everybody. Good morning.
**Otmar Ertl (Dynatrace)** 03:38 Hello?
**jmacdonald** 03:40 Okay, you can hear me.
**Chris Marchbanks** 03:43 Hmm.
**jmacdonald** 03:43 Cool.
I have, I just got here, I have an agenda item.
That's… is… new.
And while I am preparing to write it, I will tell you what it is.
I volunteered myself Where is it, the 9th?
Look at us. It's almost the same as last week.
Anyway, my agenda item for you all, is that I volunteered myself to speak next Tuesday at the Specifications SIG, which is now the sort of most central meeting of OpenTelemetry.
And we've been asking to go… to get some periodic review going for the various sub-projects, and sampling was mentioned as one that, you know, it's small, but it's been ongoing for a long time, so… What I'm gonna do is prepare, like, you know, maybe some slides with a brief summary of what we've accomplished in the recent time period, maybe last year or two, and I wanted to make sure I can summarize everything we've done. That's my agenda item.
And I made a draft.
Would you like to hear what's on my draft?
So, we have… OTEP235 progress, which was, merged to spec. We are waiting for some implementations.
Inventations… We have.
JavaScript. Python.
I think we're almost there we go.
I have a feeling that there are a couple more.
That's good enough. And… This is… Trying to get us through, Sorry, what I'll say is it's trying to get us… Trying to get to parity with trace ID ratio based… Adobe3c Level 2 randomness.
And random flag.
That's what I think we're getting through with OTEP 235.
And… This will be an opportunity for me to advertise why it's important and press for more implementations, so that's what I'm going to do.
We then… I'm having trouble with my controls here. I then want to go zoop, zoop… There's something about OTEP 250, And composable samplers.
Not sure.
Progress.
Honestly.
My… impression was likely this was stalled because of declarative configuration. My guess is that most people don't care to have a fully configurable sampler API.
with composable features. They want EML files that have composable features. I think. They want OpAMP to send those features out to their samplers, and so on.
That's my guess.
I personally prototyped this in a couple places, but haven't pushed it forward into the spec.
Meaning I haven't pushed it into an SDK, is what I meant.
And… I guess I'm gonna ask the room what they think about it. My… my feeling is probably this group wants to do a little more on declarative Config now that we have declarative config at 1.0.
I think this is the time for us to make some progress. Peter had a draft. I have to… I don't remember where exactly it was, And without him here, I won't be able to ask him.
I'll try and catch up with him on the Slack before next Tuesday.
Anybody have thoughts on OTEP?
250.
Also, all this is misintented. Let's go down.
No one is required to speak at this meeting.
I have a few more notes.
Processors… we have… several pieces of news which I'm going to share, which may be less familiar in this group. So, Tail sampling.
Processor, still very popular, has new ownership. Me. Josh. I have declared ownership of that code, and I now approve PRs. I'm really easy to get an approval from, by the way.
So that has been getting some progress, from interested parties. tail sampling processor, storage extension is underway.
For disk store. So this is for certain users with particular traffic patterns, are willing to put a disk store behind their tail sampling processor. I tend to think this is a low-volume use case, but I'm willing to approve PRs. It's well done.
And I'm sure it's making some user happy somewhere.
So, that's been sort of two features going forward there.
we had a fellow named Alf visit us a couple months ago to push for his feature. That got through, and now it's this other guy working on storage extensions. We also have, Trace Pruning.
How? Is a new processor proposed by Sean Porter, who has been involved in some of this stuff. I think he's employed by Grafana, but it's like a… satellite, somehow. Like, he's been working on…
**Chris Marchbanks** 10:15 fully employed by Grafana at this point, like, so… I can also answer questions around trace.
**jmacdonald** 10:21 Okay, the point I was really trying to make was that I don't quite understand, the full picture of what he's doing, with sort of open source and commercial activities.
But, the way it's been presented, it's a… it's a community-oriented project, and, I looked over it, and I agreed to sponsor it, meaning, again, easy approvals. So I could… Could try and find that for you, just… just for… Just for an example of what we're talking about, it's a big PR, it's like 10,000 lines of code, and So… It's… it's going to take a little bit longer to get in, but there it is.
This is meant to run before your tail sampling processor. It will, limit the size of large traces, and compute some aggregates for you at the same time. So it can compute, like, distribution of latency, and then give you a few examples, rather than sending every trace through to tail sampling. So that's…
**Chris Marchbanks** 11:31 We actually ran after tail sampling, because.
**jmacdonald** 11:34 Sweet.
**Chris Marchbanks** 11:35 Why is a grouped trace.
Or it has to be ran after a trace grouping processor.
**jmacdonald** 11:40 Okay, so… cool, I'm glad you know more than… I thought it was the other way around, but But… Because I asked him that question once.
I can't hear you very well, I have to turn up my audio.
Hold on a second.
Yeah, audio settings. Why is… Windows audio controls, honestly, what are they doing? Okay, here we are. So, now that I can hear you better, Chris.
**Yuanyuan Zhao** 12:09 A quick question? Please.
Yeah. Okay, yeah, sorry, it's a bit late, because you guys seem… could not hear me before. The storage extension, for tail sampling processor is basically, store the, traces on disk.
That's what it is for. Local disk.
**jmacdonald** 12:31 That's right.
**Yuanyuan Zhao** 12:32 whatever kind of disk, right? Okay.
**jmacdonald** 12:37 the… I got involved in what I'm calling extension interface design for the collector. It's sort of like a, what do we do at the Golang level to make sure that we can plug in these… plug these pieces of program together? So, I've been supervising both as a tracing person, or sampling person, and as an extensions person at this point.
the, the, so, if you're familiar with PebbleDB, Pebbledb is a RoxDB in Go by Cockroach, and it… so it's a… there is an existing storage extension which gives you a key value in it, like a key-value store. This is more of a key value with… it's dedicated to traces so that you can do some sort of range-based scan if you need to, like, look up a bunch of prefixes and pull in all your traces.
Point is, it's a little bit designed for tracing… trace and sampling, rather than for key value set.
sat and get.
And the reason why we're calling it extension is that you don't want to put this PebbleDB dependency on every single user of the tail sampling processor. What this will be is a hook that lets you connect the extension if it's there, and then the extension gets compiled separately as a separate component. It's called an extension component. You say, I can find my extension somewhere, it's a PebbleDB, and then you start doing it.
So that's been in progress.
So… Thank you.
Chris, you were saying that the trace pruning runs after tail sampling?
**Chris Marchbanks** 14:09 Yeah, it needs a full trace to be grouped together, so it would be either after tail sampling, or if you're not using tail sampling, you would have to do a trace group processor.
Whichever one that's called.
**jmacdonald** 14:22 I don't know what that one's called, but I've heard of it.
**Chris Marchbanks** 14:25 Yeah, yeah, so it… and then it will take, basically, duplicate trees and collapse them in. We run this on some of our internal workloads that would have, like, hundreds of thousands of parallel basically identical request, it collapses all of those, says, I made this 100,000 times, latency range was in this, and diff… It can do a little bit of, like, statistical, like… Keep a couple outliers as well, if those are interesting to keep.
**jmacdonald** 14:58 Cool.
**Yuanyuan Zhao** 15:00 That's it.
**Chris Marchbanks** 15:00 That data is a bit odd, like, we don't have a great answer to how to actually visualize the output, besides looking at numbers as trace annotation… as trace attributes, but…
**Yuanyuan Zhao** 15:10 So it's like, collapsing… Redundant pieces within a single trace.
**Chris Marchbanks** 15:18 Exactly, yeah.
**Yuanyuan Zhao** 15:19 Okay, and of course, like, providing statistically, like, histograms, right? What are the… those kind of things. Okay.
Makes sense.
**jmacdonald** 15:29 Yes, some sort of histogram-y type of summary.
Yeah. Then we have spanch metrics.
I'm gonna call it span 2 Metrics.
Processor… new… Update.
now recognizes OCHEP235 trace threshold.
I think that's an accurate statement.
**Yuanyuan Zhao** 15:56 Yeah, I didn't track their release cycle, though.
**jmacdonald** 16:00 It's.
**Yuanyuan Zhao** 16:01 It's in forever. Every two weeks.
**jmacdonald** 16:03 I bet it's been released.
**Yuanyuan Zhao** 16:05 Okay, okay.
So this brings back to…
**jmacdonald** 16:12 Yeah.
**Yuanyuan Zhao** 16:13 an import in the Go SDK, you saw that there's a bit of back and forth.
where that should go. We followed their instruction, but they… they've been changing their minds.
You approve.
**jmacdonald** 16:29 LinkedIn.
**Yuanyuan Zhao** 16:30 the one in Contrib, but now they ask us to… move back into the core SDK, but into, a, extension package.
That's, like, the convention they want now, but now they have… Comments… Whether this should be called trace ID Ratio Sampler.
Whether this should be called a probability sampler, those kind of things, and he quoted that, the spec, official spec, is… has marked trace ID ratio-based sampler as deprecated.
So…
**jmacdonald** 17:17 Oh, yeah.
**Yuanyuan Zhao** 17:18 There's a, yeah, a bunch of, like, confusion over there. Did we…
**jmacdonald** 17:24 I remember now at the…
**Yuanyuan Zhao** 17:28 Yeah.
**jmacdonald** 17:29 very last minute that we… as we updated the old spec, people said, no, no, no, we can't change the trace ID ratio at all. Users depend on it. So we will ask for a rename.
And I can't remember now.
what we slipped in at the end, so I think it might be probability sample. Whatever they're saying might be right. This sounds like a correct…
**Yuanyuan Zhao** 17:54 What about other languages?
**jmacdonald** 17:56 Yeah… Okay.
**Yuanyuan Zhao** 17:58 deal there.
It has to be insistent.
**jmacdonald** 18:06 Yeah,
**Yuanyuan Zhao** 18:14 Because it's API level completely, It's APIs that were completely compatible.
It's the inner implementation, and of course, that you could argue that trace states change it, right? And there's different information over there. I provided answer on why.
**jmacdonald** 18:37 the skeleton.
**Yuanyuan Zhao** 18:37 data compatible.
It's probably down there, you have a link to… Yeah, I'll give you an idea.
**jmacdonald** 18:45 Down below, yeah, yeah, yeah, this one.
**Yuanyuan Zhao** 18:47 There's a… no, it's actually… there's a UPR now, because they… they've been asking us to change to a different place. So this is the link. I will update the doc if you couldn't.
**jmacdonald** 18:58 Thank you.
**Yuanyuan Zhao** 19:00 Yeah.
I could go either way. I also don't see that using the same name is anything different, because the previous trace state, even though it's different and it's part of the API, right?
But nothing officially supported to actually use that, if I understand it correctly. But it's a different story if there's, like, any kind of state… stable support of the original P-value, V value.
**jmacdonald** 19:31 Absolutely.
**Yuanyuan Zhao** 19:32 Right? Yeah.
I don't think so.
**jmacdonald** 19:35 I mean…
**Yuanyuan Zhao** 19:36 Yeah, so pitch in on the, PR over there, and hopefully we can wrap that up, then I can move on to the next thing.
Right? And also, you mentioned… composite sampler over there. I was actually also going to look into that for Go as well, after… but this thing with, like, the back and forth has been taking a while.
**jmacdonald** 20:01 I'm.
**Yuanyuan Zhao** 20:02 into that next, and sync up.
**jmacdonald** 20:04 I'm looking for my… I hate Zoom controls. Where are they? I can't find my chat. I'm looking for this link. We'll fill it in.
**Yuanyuan Zhao** 20:11 Both you do. I'll fill you in, I'll fill you in.
**jmacdonald** 20:14 Cool. So… and I will… I will read and follow through on gathering all the information from those links, if you give them to me, so that I can speak coherently next Tuesday.
Yep.
So this is really about the migration and the deprecation lifetime for old behavior. I wasn't understanding what you said about trace state.
**Yuanyuan Zhao** 20:40 Oh, okay.
So, the argument of it is… okay to reuse the same name, because it's API level compatible. We didn't change the API on the Trace ID sampler, it's the internal implementation that was changed.
But of course, one can argue that the trace state is also part of the API, right? That's because it's… it's something generated by the sampler, but used by something else. So it is officially part of the API, that's why I mentioned trace state. But the argument is that the trace state with the old information was never officially supported. The p-value, V-value thing was never officially supported.
And this contains, like, a newer thing, and we are processing things in backwards compatible way, in that if there is a TH, then we're going to use it. If there is not.
the official spam metrics connector falls back to the previous behavior. So that's some argument over there. It's just provided so that we We think from… multiple angles. Personally, I… I can go with either way. Rename it to probability sampler, or… but it has to be something consistent across the SDKs.
**jmacdonald** 22:10 Yeah.
Okay, something happened.
This is not what I mean to look at. I…
**Yuanyuan Zhao** 22:20 Yeah, there's, that link.
**jmacdonald** 22:25 Alright, so… Where are we?
**Yuanyuan Zhao** 22:30 This, this is the link.
**jmacdonald** 22:32 There, there it is. So we left the old trace ID ratio sampler, and then.
**Yuanyuan Zhao** 22:35 Yeah, yeah, you are looking at the right things.
**jmacdonald** 22:37 I forgot about this. Yeah, ugh.
Okay, so now I'm gonna go back and read the… the linked issue.
**Yuanyuan Zhao** 22:50 Right.
**jmacdonald** 22:51 And try and tease apart what was being said about trace state.
And this will be a good topic for the conversation on Tuesday, to try and figure out… You know, because… Okay, I have to read. The Go team is really good at teasing out problems in the spec, I'll give them that. So, we gotta figure out what's wrong here, and I don't quite understand yet.
**Yuanyuan Zhao** 23:20 Okay, yeah, just a note so we can look at it offline.
**jmacdonald** 23:24 Maybe what I'll do… I… I don't have more to say on this right now. I need to catch up on it a little bit, but I think we should do it offline, and yeah.
So, what I would propose is… This is a topic for conversation in the Slack. I may follow up yawn yawn with you, Chris.
anybody in the sampling Slack, essentially, to talk about questions as I find them.
But I'm gonna have to sit down and read the whole, the whole thread.
Does that sound fair?
**Yuanyuan Zhao** 24:00 Yep.
**jmacdonald** 24:00 That was… that was one item for the agenda.
does anybody else have anything they want to talk about?
I'm glad to know that you know about the trace pruning work.
Chris, I will, well, remember I can ask you questions as well.
**Chris Marchbanks** 24:22 Yeah, and Sean did list me as, like, a potential code owner of that as well, to help out with reviews.
**jmacdonald** 24:27 recommend it.
Collector Kinship just needs more code owners, I don't think it's a big amount of work, If you don't… depends on how carefully you treat these code reviews, I don't know.
**Chris Marchbanks** 24:43 I've been tr- I've been trying to do some, at least, so…
**jmacdonald** 24:46 Good. I'm… great. You're the primary. Thank you.
Well, okay, folks, if we don't have any more agenda items before us, this was a good, a good summary, and I like to keep it short, so… Maybe… maybe I'll see you all in 2 weeks?
Or Tuesday, if you want to come talk about sampling in the Spec SIG, 8 AM.
Pacific time.
**Yuanyuan Zhao** 25:08 Next Tuesday, right?
**jmacdonald** 25:09 Yeah, same time as right now, next Tuesday.
Yeah, Yuan Yuan, please join. That would be helpful. Chris, please join. Yeah. Ammar, I don't know. You're the mastermind here, but I'm not sure you, you need to be there to talk about hotel specs.
**Otmar Ertl (Dynatrace)** 25:26 Yes, Probably, I have to pass.
**jmacdonald** 25:29 Okay, thank you all. Two weeks from now, another short meeting. Thank you.
**Otmar Ertl (Dynatrace)** 25:34 Okay, siempa.
**Chris Marchbanks** 25:35 But… Yeah.
**Yuanyuan Zhao** 25:37 Bye.
**jmacdonald** 25:37 Now I find my controls, where are they?
There, there.
