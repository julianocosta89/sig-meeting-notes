SIG: Collector SIG
Date: 2026-06-10
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Jade Guiton** 05:48 August 3rd.
So, are there any updates regarding component stability?
I have a lot of people here, so… Probably not, but… just to check.
**Pablo Baeyens** 06:09 I will merge the batch… batching RFC… well, whenever Josh fixes CI, but it should be soon, so consider it, like, approved done.
**Jade Guiton** 06:23 The batch processor migration RFC?
**Pablo Baeyens** 06:26 It's… yeah, that's it.
**Jade Guiton** 06:28 Alright, nice.
**Pablo Baeyens** 06:31 Yeah, and then… Sorry, I joined a bit late.
There's a couple of advantage NPRs that If you want to… review… you as in the group, it would be… helpful. I mentioned this last week, but… finishing again.
Well, I'll put it on that note.
on the links, I don't want to… Spend a lot of time just searching for it.
**Jade Guiton** 07:14 Are these the ones you linked in the… in the docs for last week?
**Pablo Baeyens** 07:20 Oh, right, yeah, I think… I think that's… Yeah, it's the same thing. So, 15309, this one.
And then… The issue that, braylon mentioned.
**Jade Guiton** 07:45 Hmm, which one is that?
**Pablo Baeyens** 07:53 Let me see if I can find it now, because that one is not linked. I think it was mentioned on the Zoom chat, but that's it.
I'll put it on the links. Sorry, let's… let's go ahead. I don't want to… To stop you all for me.
**Jade Guiton** 08:24 Anyone else has updates on component stability?
Alright, let's move on to the next point, then.
Mike?
**Mike Goldsmith** 08:42 Yes, hello everyone. It was just to bring a new proposal to the attention of everyone, so I did it a little while ago for the drain processor that seems to be quite well received, and people are starting to use it and see good results from.
So what I've got on the agenda, I'll get a link to it, put it in the chat as well, is a dynamic sampler. So, we have the tail sampler in the collector already.
But the… what I am proposing is a different processor, because I'm wanting to introduce what the Honeycombs Refinery does. So, Honeycomb Refinery is a tail sampling solution outside of the collector.
But it uses EMA-based, samplers to generate fluctuating sample rates, and it does that on through Windows, through different aggregation metrics. And it doesn't quite fit naturally into the telesampler for a couple of different reasons.
The issue explains a lot of them. So, the primary ones are that the tail-based sampler wants to work across all of the different policies and apply all of them, and if any of them match, then it gets sampled. And the secondary part is that a single sample rate is what the EMA sampler is trying to achieve, so it tries to generate a single one and then attribute that onto the spans that are selected, so… Downstream users can weight them correctly, so if you've got a sample rate on it, then it knows to extrapolate that based on the actual population size that's received by the processor.
So I do sort of feel like they live alongside each other rather than coexist. There's been some discussion with, Chris Marchbrooks, I think it is, who is the code owner for the tail sampler, talking about some of the differences and things on the issue, so if you've got interest, there's there.
But primarily, I was trying to raise it to the group, sort of introduce it, see if there's anybody that's interested in further discussion, or… If there's anyone that's willing to sponsor it, because I think that's the standard process before it can move forward. The issue's linked both in the chat and on the agenda, and it's got a… I put together, like, a PLC draft PR as well, of what it might look like. So, just looking for feedback and discussion points. If you've got any questions here, or on the issue on Slack, please ask.
**Jade Guiton** 10:54 Thank you very much.
One thing I'm not sure if you've heard, but process for adding components in contribib has changed, I believe.
So now there needs to be an implementation outside of Contrib before you can donate it into Contrib.
**Mike Goldsmith** 11:11 Okay.
**Jade Guiton** 11:12 I'm not sure… If this is something you've looked into?
**Mike Goldsmith** 11:17 Yeah, I can definitely do that. So, as I say, I've got a draft, implementation in a PR open against Contrib repo, so I could… that's already in a personal repo, so I could put it there and show it and link to it directly in the issue, rather than have it as an open PR.
**Jade Guiton** 11:35 Alright, great.
Thank you.
**Mike Goldsmith** 11:38 Where is the recommend… I didn't see that. Where is the notes for how a contribib… pro proposal goes now, I didn't see where those changes were made.
**Jade Guiton** 11:48 Yeah, I think it's this document that I sent in chat.
**Mike Goldsmith** 11:53 Okay.
Okay, thank you. That, yeah, that's helpful.
**Jade Guiton** 12:01 Yeah, no problem.
**Mike Goldsmith** 12:03 But yeah, as I say, we don't have to discuss it here, it's quite a single focus, and there's a lot of context to take in and read through, so… If there's no question, immediate questions, that's fine. If you put it in… if you can add it to the issue, or, I'm available on the CNCF Slack, you can ask questions there too, or in the, the sampling, channel.
**Pablo Baeyens** 12:33 Hi, it's mine.
dumb question without having read the proposal is… If this would be possible to… Integrate with that tail sampling processor, instead of being a new processor?
**Mike Goldsmith** 12:46 Yeah, so there is some discussion around, what… I think the… I think Chris was also, like, leading towards that it possible would be to integrate the two, there are some nuances around it, and I think the primary one that I can feel is always the biggest hurdle is, The… the default operation for the tail sampler is that you define multiple policies, and then if any… then it will apply all of them, and if any of them match, it will then select it to be sampled.
There is an option, a configuration option to do first match.
But that doesn't quite work, and I think that's… I think there was a nuance in there where, if you enable that feature, so basically, the EMA samplers would not function, would not be usable if that feature was not enabled, so putting this particular type of policy behind that feature flag… sorry, that configuration option.
requirement really makes it complicated from a user's point of view. He did say that, the… trace state propagation was something that they were looking… that he was looking at, introducing, so that possibly would help with, like, the attributing a sample rate onto, sampled spans. Similar solution as what I would have done in the proposal of using the new, the newer, OHTC annotation on Trace State.
I'm not totally against putting it in the tail sampler, I just feel as though that it… the… the… what would have been tail sample policies that uses EMA has a lot of intricacies that I think would make it a very difficult setup situation.
**Pablo Baeyens** 14:32 Okay.
I guess another thing that maybe would be useful here is to see what the sampling seed thinks about this. I don't know if you've already done that.
**Mike Goldsmith** 14:48 I've shared it with the sampling SIG in CNCF Slack. I'm not sure when the meeting, the weekly meeting is, but I'll try and attend there as well to see what they feel like, too.
**Pablo Baeyens** 15:00 It looks like it's Thursdays at 8 Pacific time.
**Mike Goldsmith** 15:04 That's very late for me, I'm in the UK. I will try. I will try and engage more on the hotel sampling sig. I know that, Josh McDonald is on that group.
**Pablo Baeyens** 15:13 Yeah.
**Mike Goldsmith** 15:13 interested, so I'll continue a conversation on CNCF Slack if I can't attend that meeting.
**Pablo Baeyens** 15:19 Yeah, I think Joseph Smith would be useful. He's both part of the samplingSeq and a co-owner of the tail sampling process, probably. Sure.
**Mike Goldsmith** 15:27 Yeah, I can do that.
**Pablo Baeyens** 15:29 Cool.
**Jade Guiton** 15:44 Any other comments or questions about Mike's proposal?
Sounds like not.
In that case.
This is the end of the current agenda. Are there any impromptu topics someone wants to bring up?
I was not gonna know as well. So, I guess we can conclude it.
It was a bit of a short meeting today.
Thank you, everyone.
**Pablo Baeyens** 16:15 One 10-second thing, if you are… you have a former role in the project, and you're going to go to Cubeco North America, or you would want to go to CubeCo North America.
Lou, I can share a forum with you to show your interest to be part of the Contrik Fest, organizers, and TripFest is, sort of like a hackathon, where you help people make their first PR against OpenTelemetry. Typically, you get a free ticket for KubeCon, and it typically counts as something that you can Use for your employer to cover.
trouble, to… If you're interested in that, I guess, reach out to me on the CNC Slack, and I'll share the form with you, if you haven't seen it already.
more than 10 seconds, but yeah, we can propagate that here. Thank you.
**Jade Guiton** 17:16 Okay, everyone.
**Mike Goldsmith** 17:19 Yeah, thank you.
