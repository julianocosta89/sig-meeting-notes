SIG: System Sem Conv Stability SIG
Date: 2026-10-15
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:11 Hey, folks.
**Pablo Baeyens** 01:18 Hey.
**Alex Boten** 01:25 Hello.
**Dmitrii Anoshin (Splunk Inc.)** 02:01 Hi, everyone.
Alex, it's a surprise to see you here.
Welcome.
**Alex Boten** 02:08 Yeah.
Yeah, I'm… I'm here because I realized that there's no TC liaison with the SIG, and I thought maybe this would be helpful for me to attend, so I'm here now.
**Dmitrii Anoshin (Splunk Inc.)** 02:21 I thought Josh was oh, Josh just stepped down for STC, I guess, right?
**Alex Boten** 02:27 Yep.
**Dmitrii Anoshin (Splunk Inc.)** 02:28 One.
**Alex Boten** 02:28 Love that Josh is dead.
We have a Max 1 Josh on the committee.
There are no topics on the agenda. Is there no agenda today?
**Dmitrii Anoshin (Splunk Inc.)** 02:54 We are meeting every week. That's probably why.
**Pablo Baeyens** 02:59 Yeah, I guess… There's some PRs from Donal, I don't know how they are doing, maybe we could talk about that?
**Donal O'Sullivan** 03:10 Yeah, sure, so I guess you're talking about the, Promoting the system attributes to a release candidate.
**Pablo Baeyens** 03:19 you.
**Donal O'Sullivan** 03:20 I think everything was addressed that Lilidma had brought up, so there was the CPU.logical number, PR was merged, and there was another one.
I can't remember what that one, yeah, so they were both merged, but, Roger brought up a valid point around, He has a PR open to update the system memory usage metrics.
So he's… It's like, I'll see if I can dig out the PR. He's changing the definition and he's, he's, I think he's making a… Couple different attributes, deprecated.
**Pablo Baeyens** 03:59 Is that the one, the one I sent on?
Zoom chat.
**Donal O'Sullivan** 04:03 Oh, it could be, yeah.
I think I, yeah, I replied to it earlier.
Very quick look.
Yeah!
I think that's it, yeah, yeah.
Yeah, that's the one, so… Yeah, I just, I gave a small bit of feedback, I was more just wondering, I think he was actually wondering about, I know AI had done a review, and it was on… System memory usage with the… State attribute available versus having, like, a specific system memory Linux available.
Metric, so it was kind of around do we need both those separate metrics?
Because I think, like, they're gonna report the same thing.
If that makes sense.
At least that's my understanding of it.
**Pablo Baeyens** 05:18 Sorry, I'm breathing.
Hmm.
I feel like if there's no complaint reason to have system memory Linux available, we… Shouldn't add it now.
I'm just… Do it later if we find something, some compelling argument.
**Donal O'Sullivan** 06:34 Yeah, so like it is, it's already being used, like the metrics already there, but I think it's the main reason for the PR is there's a It's mainly Roger and Braden know about this, but it's that whole thing with Getting an accurate memory available reading from Linux systems.
**Pablo Baeyens** 06:55 Yep.
**Donal O'Sullivan** 06:56 Which you're probably familiar with, and then, yeah, it's just the AI comment brought up that whole thing, because I think… Yeah, it was changing the, the state.
for that metric. So, system memory usage, if it has an available state, what's the point in the Linux version of that metric?
I think that's the only real question with the work. But as you say, like, what's yeah, what's the point in having Specific Linux metric if the generic one emits the same thing, right?
Yeah.
Yeah, I would agree with you.
**Dmitrii Anoshin (Splunk Inc.)** 07:37 Craig, do you mean that… Current used metrics is the same as available.
**Donal O'Sullivan** 07:45 So I think what Roger's change. Yeah, so it's a good question, Dmitri. I think it's around like, He's changing the, the state on that metric, so… The system memory usage will emit a, the value with a state available. But then there's also a different metric on its own for system memory Linux available, which will emit the same
**Dmitrii Anoshin (Splunk Inc.)** 08:16 Yes, and we already have that metric right links available.
**Donal O'Sullivan** 08:21 Yeah, so they're both in the host metrics of Siever's moment, but they emit.
**Dmitrii Anoshin (Splunk Inc.)** 08:24 different.
**Donal O'Sullivan** 08:24 I think memory usage is emitting, like, free, and then Linux memory. Yeah. Yeah, so it's… at the moment, it's relevant, but I think this change would make it irrelevant, maybe.
**Dmitrii Anoshin (Splunk Inc.)** 08:36 But I'm not sure about this whole pull request in that case. If we are… Not touching Linux available metric, like, why do we need to… why do we need to introduce this, like, redundant state? Like, not redundant, but duplicate state. It kind of makes sense. But also, I'm… what about Windows? This available state is only available on Linux. It's not available on Windows, right?
So we need like, have we even looked at I was gonna be mapped to the windows.
machines there.
I'm confused here why we are suggesting, like, changing the states if we… if they are only applicable to Linux.
**Donal O'Sullivan** 09:24 Yeah, I know, it's a cool question, Ravi.
**Dmitrii Anoshin (Splunk Inc.)** 09:31 Maybe I'll… I'll raise it in the PR, and we'll see.
There is nothing.
**Donal O'Sullivan** 09:39 Yeah, because I think the…
**Dmitrii Anoshin (Splunk Inc.)** 09:40 Candles here.
**Donal O'Sullivan** 09:41 Yeah, the win… I think the actual issue is mentioning Windows, so it's saying, or at least I thought it did. Let me just have a quick scan.
Yeah, so by default, to only use and available Linux metrics will align with what is being reported by other operating systems, like Windows.
So he links to, so, on the Windows implementation, it's emitting used and free.
**Dmitrii Anoshin (Splunk Inc.)** 10:10 Hmm.
**Donal O'Sullivan** 10:14 Which is slightly different, I guess. I guess that would have to change then.
**Dmitrii Anoshin (Splunk Inc.)** 10:18 We have to change names. So why do maybe we don't change the name in that case?
To, like, reduce the amount of breaking changes, so we can… Have free and used.
Yeah, I guess we need. We need the to discuss it more.
**Donal O'Sullivan** 10:40 Yeah.
Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 10:57 Also, we don't have Concept of opt-in, opt-out attribute values.
We have that concept only for the attributes themselves.
Which applies re-aggregation if some of them are disabled, and we don't have Not anything like that for values. Probably need to Maker.
at least update the gen first, PR first, and see how If this concept is available in, Vivar.
Sorry before we apply this change.
Does that make sense?
**Donal O'Sullivan** 11:44 Yep.
**Dmitrii Anoshin (Splunk Inc.)** 11:46 Essentially can go through feature gaze, but it's also not very… He'd like user friendly. Yes.
The, I think, in general.
Heaven. Values.
Been… like turn… being able to turn off or not. I think that's, in general, a pretty useful feature.
Going forward.
Oh… I'll post post a comment here. We'll see.
Maybe we'll discuss next time on solutions.
On the call. Does that make sense?
Okay.
Thank you.
**Pablo Baeyens** 13:09 Okay, and I had one… thing, so… I would like to move forward with the RFC on the collector.
But… Well, Braden was going to write this document about the strategy on the host metrics receiver.
So, I was thinking about saying something on the collector FC, like… Individual components will define the strategy for semantic conventions migration, but we will not require them to be stable, necessarily?
To be one something that does not.
Impose any requirements, but also, like.
Gives people the leeway to define things in whatever way they wish for each component.
I guess that's also something for Roger to answer mostly, but I don't know if people have opinions here.
**Donal O'Sullivan** 14:10 So does that mean the components can be V1, but the metrics don't have to be stable? Is that essentially it?
**Pablo Baeyens** 14:20 Yes, that's… That's what we're… what I was aiming for with the RFC, not have that requirement.
I do think that… Like, it seems… just saying that is not enough, like, we need some sort of justification as to why we do that on specific components, so that's why I wanted to say, like.
There should be some sort of… Strategy for each component.
**Donal O'Sullivan** 14:54 Yeah, yeah.
Yeah, makes sense.
**Pablo Baeyens** 15:04 I'll write something and see what people think, including Roger.
**Dmitrii Anoshin (Splunk Inc.)** 15:25 And yes, we can wrap it up earlier today.
Thank you, folks.
**Alex Boten** 15:33 Thank you.
**Pablo Baeyens** 15:33 you.
**Donal O'Sullivan** 15:34 See you guys.
